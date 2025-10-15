import re

def clean_text_list(text_list):
    cleaned = []
    for text in text_list:
        if not isinstance(text, str) or not text.strip():
            continue
        text = re.sub(r'^[\-\*\•\u2022]\s*', '', text)
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'^[\-\*\•\u2022]\s*', '', text)
        cleaned.append(text.strip())
    return cleaned
