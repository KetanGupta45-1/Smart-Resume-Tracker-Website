from Improvement__.pipeline import get_modified_resume_sections_grouped

resume_json = "D:/Projects/Machine and Deep Learning/Resume Project/parsed_data.json"
api_token = "yes sir"
role = "Web Developer"

modified_sections = get_modified_resume_sections_grouped(resume_json, role=role, api_token=api_token)

# Pretty print grouped sections
for section, items in modified_sections.items():
    print(f"\n____________ {section} ______________")
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")