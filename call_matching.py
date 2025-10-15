from Matching__.extract_json import extract_skills
from Matching__.extract_job_skills import extract_skills_from_job_description
from Matching__.calculate import calculate_skill_match

GROQ_API_TOKEN = 'yes sir'
resume_json_path = 'D:/Projects/Machine and Deep Learning/Resume Project/parsed_data.json'

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

resume_skills = extract_skills(resume_json_path)
job_skills = extract_skills_from_job_description(job_description, GROQ_API_TOKEN)

match_score, matching_skills, resume_result, job_result = calculate_skill_match(resume_skills, job_skills)

print("SKILL MATCHING RESULTS")
print("-"*50)
print(f"Resume has {len(resume_skills)} skills")
print(f"Job requires {len(job_skills)} skills")
print(f"Match Percentage: {match_score:.2f}%")
print(f"Matching Skills: {', '.join([s for s in matching_skills if s])}")

print("\n--- Detailed Resume Skill Mapping ---")
for m in resume_result.get('matched', []):
    print(f"{m['input']} -> {m['mapped_to']} | Confidence: {m['confidence']} | Method: {m['method']}")

print("\n--- Missing Job Skills ---")
for m in job_result.get('missing', []):
    print(f"{m['input']} -> Closest Match: {m.get('closest_match')} | Confidence: {m.get('confidence')} | Method: {m['method']}")
