from Improvement__.extract_json import extract_sections
from Improvement__.clean_text import clean_text_list
from Improvement__.llm_process import llm_process_grouped
from Improvement__.setup_llm import initiate_model

def get_modified_resume_sections_grouped(json_path, role=None, api_token=None):
    """
    Full pipeline: extract -> clean -> LLM -> grouped modified sections in structured format.

    Returns a dictionary with keys: 'projects', 'workExperience', 'achievements'.
    Each contains a list of dicts with 'title' (or 'projectTitle') and a 'description' list.
    """
    if not api_token:
        raise ValueError("API token is required to initialize the LLM")
    llm = initiate_model(api_token)

    # Step 1: Extract structured sections
    raw_structured_sections = extract_sections(json_path)  # returns dict with projects/workExperience/achievements

    structured_sections = {
        "projects": [],
        "workExperience": [],
        "achievements": []
    }

    for section_key, items in raw_structured_sections.items():
        for item in items:
            if not isinstance(item, dict):
                continue
            # Determine title key
            title_key = "projectTitle" if section_key == "projects" else "title"
            title = item.get(title_key, "")

            # Clean descriptions
            raw_descriptions = item.get("description", [])
            cleaned_descriptions = clean_text_list(raw_descriptions) if raw_descriptions else []

            structured_sections[section_key].append({
                title_key: title,
                "description": cleaned_descriptions
            })

    # Step 2: Process each section with LLM
    modified_sections_grouped = llm_process_grouped(structured_sections, llm, role=role)
    return modified_sections_grouped