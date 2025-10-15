from Improvement__.extract_json import extract_sections
from Improvement__.clean_text import clean_text_list
from Improvement__.llm_process import llm_process_grouped
from Improvement__.setup_llm import initiate_model

def get_modified_resume_sections_grouped(json_path, role=None, api_token=None):
    """
    Full pipeline: extract -> clean -> LLM -> grouped modified sections.
    """
    raw_sections_dict = {}
    for section_name in ["Projects", "Work Experience", "Achievements"]:
        raw_sections = extract_sections(json_path, key=section_name)
        raw_sections_dict[section_name] = clean_text_list(raw_sections)

    if not api_token:
        raise ValueError("API token is required to initialize the LLM")
    llm = initiate_model(api_token)

    modified_sections_grouped = llm_process_grouped(raw_sections_dict, llm, role=role)

    return modified_sections_grouped
