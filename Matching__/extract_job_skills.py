from langchain.prompts import PromptTemplate
from Matching__.setup_llm import initiate_model
import json
import re

def extract_skills_from_job_description(job_description, token):
    chat_model = initiate_model(token)
    prompt_template = PromptTemplate.from_template("""
You are an expert HR assistant specializing in skill extraction from job descriptions.

TASK: Extract ONLY the specific technical and soft skills mentioned in the job description.

Return ONLY a JSON array of lowercase skill names.
Job Description:
{job_description}
""")
    formatted = prompt_template.format(job_description=job_description)
    try:
        response = chat_model.invoke(formatted)
        text = response.content.strip()
        text = text.replace('*', '').replace('-', '').replace('•', '')
        try:
            arr = json.loads(text)
        except Exception:
            arr = []
            for line in text.splitlines():
                line = line.strip()
                if not line:
                    continue
                line = re.sub(r'^\d+\.\s*', '', line)
                line = re.sub(r'[^\w\s\-\&\+]', '', line).strip()
                if line:
                    arr.append(line.lower())
        arr = list(dict.fromkeys([a.lower().strip() for a in arr if a and isinstance(a, str)]))
        print(f"extracted skills from jd: {arr}")
        return arr
    except Exception as e:
        print(f"error extracting from jd: {e}")
        return []
