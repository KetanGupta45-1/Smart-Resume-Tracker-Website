from langchain.schema import AIMessage

def get_resume_prompt(section_name, sections_list, role=None):
    role_text = f"for the role of {role}" if role else ""
    sections_text = "\n".join(f"- {s}" for s in sections_list)

    prompt = f"""
You are a professional resume editor. Rewrite the following {section_name} sections {role_text} 
to make them more official, concise, and impactful, using resume-style language.
Keep the meaning intact but improve readability, quantification, and action words.

Sections to improve:
{sections_text}

Return the improved sections as a numbered list, keeping each item separate.
Do not add extra commentary.
"""
    return prompt

def llm_process_grouped(sections_dict, llm, role=None):
    grouped_output = {}
    for section_name, cleaned_sections in sections_dict.items():
        if not cleaned_sections:
            continue

        prompt = get_resume_prompt(section_name, cleaned_sections, role=role)
        response = llm.invoke(prompt)

        raw_output = response.content if isinstance(response, AIMessage) else str(response)

        modified_sections = []
        for line in raw_output.split("\n"):
            line = line.strip()
            if line and (line[0].isdigit() and line[1:3] in [". ", ") "]):
                line = line.split(". ", 1)[1] if ". " in line else line
                modified_sections.append(line.strip())
            elif line:
                modified_sections.append(line.strip())

        grouped_output[section_name] = modified_sections

    return grouped_output
