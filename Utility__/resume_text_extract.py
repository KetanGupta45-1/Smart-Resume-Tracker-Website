from PyPDF2 import PdfReader

def return_text_from_pdf(pdf_path):
    pdf = PdfReader(pdf_path)
    text = ""

    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + " "
    
    return text.strip()
