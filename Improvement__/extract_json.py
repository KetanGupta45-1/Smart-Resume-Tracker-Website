import json

def extract_sections(json_path, key=None):
    """
    Extract specific section from resume JSON.
    If key is None, returns all sections flattened.
    """
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"error reading resume json: {e}")
        return []

    sections = []
    keys_to_extract = [key] if key else ['Projects', 'Work Experience', 'Achievements']

    if isinstance(data, dict):
        for k in keys_to_extract:
            raw = data.get(k) or []
            for item in raw:
                if isinstance(item, dict) and 'descriptions' in item:
                    for desc in item['descriptions']:
                        if isinstance(desc, str) and desc.strip():
                            sections.append(desc.strip())
                elif isinstance(item, str) and item.strip():
                    sections.append(item.strip())

    return sections
