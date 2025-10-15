from Matching__.skill_mapping import skill_mapping
from Matching__.semantic_skill_matcher import SemanticSkillMatcher
from Matching__.utils import normalize_skill_text, expand_compound_skill
from Matching__.config import CONFIDENCE_THRESHOLD

def _get_unique_normalized_targets():
    vals = list(skill_mapping.values())
    uniq = list(dict.fromkeys(vals))
    return uniq

def hybrid_match(user_skills):
    normalized_inputs = []
    for s in user_skills:
        pieces = expand_compound_skill(s)
        for p in pieces:
            normalized_inputs.append(normalize_skill_text(p))

    exact_matches = {}
    remaining = []

    for s in normalized_inputs:
        if s in skill_mapping:
            exact_matches[s] = {'mapped_to': skill_mapping[s], 'confidence': 1.0, 'method': 'exact_key'}
        elif s in skill_mapping.values():
            exact_matches[s] = {'mapped_to': s, 'confidence': 0.99, 'method': 'exact_value'}
        else:
            remaining.append(s)

    targets = _get_unique_normalized_targets()
    sem_results = SemanticSkillMatcher(targets).match(remaining) if remaining else []

    matched = []
    missing = []

    for s, info in exact_matches.items():
        matched.append({'input': s, 'mapped_to': info['mapped_to'], 'confidence': round(info['confidence'], 3), 'method': info['method']})

    for orig, mapped, score in sem_results:
        c = round(score, 3)
        if c >= CONFIDENCE_THRESHOLD:
            matched.append({'input': orig, 'mapped_to': mapped, 'confidence': c, 'method': 'semantic'})
        else:
            missing.append({'input': orig, 'closest_match': mapped, 'confidence': c, 'method': 'semantic'})

    return {'matched': matched, 'missing': missing}
