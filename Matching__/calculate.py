from Matching__.skill_matcher import hybrid_match

def calculate_skill_match(resume_skills, job_skills):
    resume_result = hybrid_match(resume_skills)
    job_result = hybrid_match(job_skills)

    matched_job_skills = {}
    for m in job_result.get('matched', []):
        key = m.get('mapped_to')
        conf = m.get('confidence', 0.0)
        if key:
            matched_job_skills[key] = max(matched_job_skills.get(key, 0.0), conf)

    total_conf = 0.0
    count = 0

    for j in job_result.get('matched', []):
        count += 1
        total_conf += j.get('confidence', 0.0)

    for j in job_result.get('missing', []):
        count += 1
        total_conf += j.get('confidence', 0.0)

    score = (total_conf / count) * 100 if count > 0 else 0.0
    matching_skills = [m.get('mapped_to') for m in job_result.get('matched', []) if m.get('mapped_to')]

    return round(score, 2), matching_skills, resume_result, job_result

