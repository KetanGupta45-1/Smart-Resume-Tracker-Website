import re

def normalize_skill_text(skill):
    s = skill.lower().strip()
    s = s.replace('&', ' and ')
    s = re.sub(r'[\u2018\u2019\u201c\u201d]', '', s)
    s = re.sub(r'[^a-z0-9\s\.\+\-]', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    s = s.replace('  ', ' ')
    return s

def expand_compound_skill(skill):
    skill = skill.strip()
    if '&' in skill or ' and ' in skill:
        parts = re.split(r'&| and ', skill)
        return [p.strip() for p in parts if p.strip()]
    if '/' in skill:
        parts = skill.split('/')
        return [p.strip() for p in parts if p.strip()]
    return [skill]
