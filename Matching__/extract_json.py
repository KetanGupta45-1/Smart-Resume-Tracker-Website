import json

def extract_skills(json_path):
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"error reading resume json: {e}")
        return []
    skills = []
    if isinstance(data, dict) and 'Skills' in data:
        raw = data.get('Skills') or []
        for s in raw:
            if isinstance(s, str) and s.strip():
                skills.append(s.strip())
    print(f"skills in resume {json_path}: {skills}")
    return skills
