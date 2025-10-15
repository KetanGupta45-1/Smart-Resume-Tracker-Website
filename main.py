from Core__.resume_parser import ResumeParser
import json

token = 'yes sir'
pdf_path = 'Shivank Resume.pdf'
template_path = 'D:/Projects/Machine and Deep Learning/Resume Project/template.json'

parser = ResumeParser(pdf_path, token)
parser.initialize_model()
parser.extract_resume_text()
parser.setup_prompt()
parsed_resume = parser.process_resume()


if parsed_resume:
    output_path = "parsed_data.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(parsed_resume, f, indent=2, ensure_ascii=False)
    print(f"💾 Parsed data successfully saved to '{output_path}'")
else:
    print("❌ No valid JSON parsed — nothing saved.")