import json

def extract_skills(json_path):
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading resume JSON: {e}")
        return []

    skills = []

    if isinstance(data, dict) and 'Skills' in data:
        raw_categories = data.get('Skills') or []
        for category in raw_categories:
            if isinstance(category, dict) and 'skills' in category:
                for skill in category['skills']:
                    if isinstance(skill, str) and skill.strip():
                        skills.append(skill.strip())

    print(f"Skills in resume {json_path}: {skills}")
    return skills
