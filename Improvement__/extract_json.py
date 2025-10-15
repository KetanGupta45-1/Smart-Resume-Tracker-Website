import json

def extract_sections(json_path, key=None):
    """
    Extract structured sections from a resume JSON file in nested format.

    Parameters:
    - json_path: path to the JSON resume file
    - key: optional; if provided, only extracts that section ("Projects", "Work Experience", "Achievements")

    Returns a dictionary with keys:
    - "projects", "workExperience", "achievements"
    Each contains a list of dicts with 'title'/'projectTitle' and 'description' list.
    """
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ Error reading resume JSON: {e}")
        return {}

    # Mapping JSON keys to structured keys
    key_map = {
        "Projects": "projects",
        "Work Experience": "workExperience",
        "Achievements": "achievements"
    }

    # Decide which keys to extract
    json_keys_to_extract = [key] if key else key_map.keys()

    output = {
        "projects": [],
        "workExperience": [],
        "achievements": []
    }

    for json_key in json_keys_to_extract:
        struct_key = key_map[json_key]
        items = data.get(json_key, [])

        for item in items:
            if not isinstance(item, dict):
                continue  # skip invalid entries

            # Determine title field
            title_key = "projectTitle" if struct_key == "projects" else "title"
            title = item.get("project_name") or item.get("job_title") or item.get("title") or ""

            # Determine description list
            if struct_key == "achievements":
                # Achievements usually have a single description string
                desc = item.get("description", "")
                descriptions = [desc.strip()] if isinstance(desc, str) and desc.strip() else []
            else:
                descs = item.get("descriptions", [])
                descriptions = [d.strip() for d in descs if isinstance(d, str) and d.strip()]

            output[struct_key].append({
                title_key: title,
                "description": descriptions
            })

    return output
