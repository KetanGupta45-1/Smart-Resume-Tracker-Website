from langchain.schema import AIMessage

def get_resume_prompt(title, descriptions, section_name, role=None):
    """
    Construct a prompt for LLM to improve the descriptions for a single item.
    """
    role_text = f"for the role of {role}" if role else ""
    descriptions_text = "\n".join(f"- {desc}" for desc in descriptions)

    prompt = f"""
You are a professional resume editor. Improve the descriptions for the {section_name} entry titled "{title}" {role_text}.
Make them more official, concise, impactful, and resume-style.
Keep the meaning intact, use quantifiable achievements where possible, and strong action verbs.
IMPORTANT: Do not add '-' in start of new descriptions.

Descriptions to improve:
{descriptions_text}

Return the improved descriptions as a list, keeping each item separate.
Do not add extra commentary.
"""
    return prompt

def llm_process_grouped(structured_sections, llm, role=None):
    """
    structured_sections: dict with keys 'projects', 'workExperience', 'achievements'
    Each value is a list of dicts with 'title'/'projectTitle' and 'description' list.
    Returns same structure with improved descriptions.
    """
    improved_sections = {
        "projects": [],
        "workExperience": [],
        "achievements": []
    }

    # Mapping to unify keys
    section_map = {
        "projects": "Projects",
        "workExperience": "Work Experience",
        "achievements": "Achievements"
    }

    for section_key, items in structured_sections.items():
        for item in items:
            title_key = "projectTitle" if section_key == "projects" else "title"
            title = item.get(title_key, "")
            descriptions = item.get("description", [])
            if not descriptions:
                improved_sections[section_key].append({title_key: title, "description": []})
                continue

            # Create prompt for LLM
            prompt = get_resume_prompt(title, descriptions, section_map[section_key], role=role)
            response = llm.invoke(prompt)
            raw_output = response.content if isinstance(response, AIMessage) else str(response)

            # Parse improved descriptions as a list
            improved_descriptions = []
            for line in raw_output.split("\n"):
                line = line.strip()
                if line and (line[0].isdigit() and (". " in line or ") " in line)):
                    # remove numbering if exists
                    line = line.split(". ", 1)[-1] if ". " in line else line.split(") ", 1)[-1]
                    improved_descriptions.append(line.strip())
                elif line:
                    improved_descriptions.append(line.strip())

            # Append back to the same structure
            improved_item = {title_key: title, "description": improved_descriptions}
            improved_sections[section_key].append(improved_item)

    return improved_sections
