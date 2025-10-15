import json
from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate
from Models__.initalise_model import initiate_model
from Utility__.resume_text_extract import return_text_from_pdf
from Core__.json_utils import extract_and_fix_json

class ResumeParser:
    def __init__(self, pdf_path, token):
        self.pdf_path = pdf_path
        self.token = token
        self.model = None
        self.resume_text = ""
        self.prompt_template = None

    def initialize_model(self):
        print("Initializing model...")
        self.model = initiate_model(self.token)
        print("Model initialized.")

    def extract_resume_text(self):
        print("Extracting resume text from PDF...")
        self.resume_text = return_text_from_pdf(self.pdf_path)
        print("Resume text length (words):", len(self.resume_text.split()))
        if not self.resume_text:
            raise ValueError("Resume text is empty! Check your PDF extraction function.")

    def setup_prompt(self):
        schema_example = """You are a resume parser. Extract information from the resume and return ONLY a valid JSON object. Do not include any explanations, markdown formatting, or additional text.
Extract full linkedIn and github links correctly (with https and do not forget slashes).
Return EXACTLY this structure:

{{
  "Profile": {{
    "name": "",
    "email": "",
    "phone_number": "",
    "country": "",
    "github": "",
    "linkedin": "",
    "summary": ""
  }},
  "Education": [
    {{
      "institution_name": "",
      "degree": "",
      "field_of_study": "",
      "cgpa_or_percent": "",
      "start_date": "",
      "end_date": ""
    }}
  ],
  "Work Experience": [
    {{
      "company_name": "",
      "job_title": "",
      "location": "",
      "start_date": "",
      "end_date": "",
      "descriptions": []
    }}
  ],
  "Projects": [
    {{
      "project_name": "",
      "tech_stack": "",
      "start_date": "",
      "end_date": "",
      "descriptions": []
    }}
  ],
  "Achievements": [
    {{
      "title": "",
      "organization": "",
      "date": "",
      "description": ""
    }}
  ],
  "Skills": []
}}

IMPORTANT : Skills should be in a single list not multple bracket.

Resume Text:
{resume_text}

JSON Output (no markdown, just pure JSON):"""
    
        self.prompt_template = PromptTemplate(
            template=schema_example,
            input_variables=['resume_text']
        )

    def process_resume(self):
        print("Processing resume...")
        prompt = self.prompt_template.format(resume_text=self.resume_text)
        human_msg = HumanMessage(content=prompt)
        response = self.model.invoke([human_msg])
        raw_output = response.content.strip()

        parsed_output = extract_and_fix_json(raw_output)
        
        if parsed_output:
            print("✅ Final Parsed Structured Output:")
            print(json.dumps(parsed_output, indent=2))
        else:
            print("❌ Failed to parse any valid JSON from output")
            
        return parsed_output