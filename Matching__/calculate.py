from Matching__.skill_matcher import hybrid_match

def calculate_skill_match(resume_skills, job_skills):
    # Run hybrid match for both sides
    resume_result = hybrid_match(resume_skills)
    job_result = hybrid_match(job_skills)

    # Extract mapped skills for comparison
    resume_skill_names = [r['mapped_to'] for r in resume_result['matched']]
    job_skill_names = [j['mapped_to'] for j in job_result['matched']]

    # Calculate overlap between resume and job skills
    matched_skills = [skill for skill in job_skill_names if skill in resume_skill_names]
    missing_skills = [skill for skill in job_skill_names if skill not in resume_skill_names]

    # Compute score based on match ratio
    total_skills = len(job_skill_names)
    matched_count = len(matched_skills)
    score = (matched_count / total_skills) * 100 if total_skills > 0 else 0.0

    # Weighted improvement: add semantic confidence for matches
    total_conf = 0
    for j in job_result['matched']:
        if j['mapped_to'] in resume_skill_names:
            total_conf += j['confidence']

    if matched_count > 0:
        score = ((score + (total_conf / matched_count) * 100) / 2)  # balance between match ratio & confidence


    return round(score, 2), matched_skills, resume_result, job_result

