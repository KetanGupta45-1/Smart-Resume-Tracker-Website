







# main.py
from fastapi import FastAPI
from Core__.resume_parser import ResumeParser
from Improvement__.pipeline import get_modified_resume_sections_grouped
import json
from call_matching import function_hu
from fastapi import FastAPI, UploadFile, File, Form
import json
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware

api_token = "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"
role = "Web Developer"

app = FastAPI()


# 🚀 Allow all CORS (any origin, any method, any header)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # allow all origins
    allow_credentials=True,
    allow_methods=["*"],       # allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],       # allow all headers (Content-Type, Authorization, etc.)
)

@app.get("/")
def read_root():
    print('aajao')
    return {"message": "Hello, LUND!"}

@app.post("/sections")
async def process_resume_sections(
    pdf_file: UploadFile = File(...),
):
    # Save the uploaded PDF temporarily
    job_description = """
    We are looking for a Full Stack Developer with strong experience in:
    - Python and Django framework
    - React.js and JavaScript
    - Database design with PostgreSQL
    - REST API development
    - Cloud platforms like AWS
    - Version control with Git
    - Agile methodology experience
    - Good communication skills
    """
    

    temp_pdf_path = Path(f"temp_{pdf_file.filename}")
    with open(temp_pdf_path, "wb") as f:
        f.write(await pdf_file.read())

    # Initialize ResumeParser
    parser = ResumeParser(str(temp_pdf_path), api_token)
    parser.initialize_model()
    parser.extract_resume_text()
    parser.setup_prompt()
    
    # Process resume
    parsed_resume = parser.process_resume()
    if not parsed_resume:
        temp_pdf_path.unlink(missing_ok=True)
        return {"error": "Failed to parse resume"}

    # Optionally save parsed resume
    output_path = Path("D:/Projects/Machine and Deep Learning/Resume Project/parsed_data.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(parsed_resume, f, indent=2, ensure_ascii=False)

    # Get modified sections
    modified_sections = get_modified_resume_sections_grouped(str(output_path), role=role, api_token=api_token)

    # Calculate ATS score
    ats_score = function_hu(resume_json_path = output_path, job_description = job_description, token = api_token)

    # Clean up temp file
    temp_pdf_path.unlink(missing_ok=True)

    # Return everything as JSON
    return {
        "parsed_resume": parsed_resume,
        "modified_sections": modified_sections,
        "ATS_SCORE": ats_score
    }