from langchain.output_parsers import ResponseSchema

def flatten_template(nested_template):
    schemas = []

    for section, content in nested_template.items():
        desc = content["description"]
        if isinstance(desc, dict):
            for key in desc.keys():
                schemas.append(ResponseSchema(name=f"{section}.{key}", description=f"{key} of {section}"))
        elif isinstance(desc, list) and len(desc) > 0 and isinstance(desc[0], dict):
            for key in desc[0].keys():
                schemas.append(ResponseSchema(name=f"{section}.[].{key}", description=f"{key} of each item in {section}"))
        elif isinstance(desc, list):
            schemas.append(ResponseSchema(name=section, description=section))
    return schemas
