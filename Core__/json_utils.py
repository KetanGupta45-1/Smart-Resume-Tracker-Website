import re, json

def extract_and_fix_json(text):
    if not text or not isinstance(text, str):
        return {}
 
    text = re.sub(r"```(?:json)?", "", text, flags=re.IGNORECASE).strip("` \n")

    text = re.sub(r"<[^>]+>", "", text)

    match = re.search(r"(\{[\s\S]*\}|\[[\s\S]*\])", text)
    if not match:
        return {}

    json_str = match.group(1).strip()

    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"⚠️ Initial parse failed at position {e.pos}: {str(e)}")
        print(f"⚠️ Text length: {len(json_str)} characters")
        print(f"⚠️ Attempting to fix JSON...")

    json_str = re.sub(r",\s*([}\]])", r"\1", json_str)  
    json_str = re.sub(r"\\'", "'", json_str) 
    
    json_str = re.sub(r'(\w+)(?=\s*:)', r'"\1"', json_str)
    
    json_str = json_str.replace('\n', ' ').replace('\r', ' ')
    json_str = re.sub(r"\s+", " ", json_str).strip()

    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        print("❌ JSON parsing failed after fixes:", str(e))
        print("Problematic text snippet:", json_str[:500])
        
        try:
            open_braces = json_str.count('{')
            close_braces = json_str.count('}')
            open_brackets = json_str.count('[')
            close_brackets = json_str.count(']')
            
            if json_str.count('"') % 2 != 0:
                print("⚠️ Detected incomplete string, attempting to close it...")
                json_str += '"'
            
            # Close any incomplete arrays
            if open_brackets > close_brackets:
                print(f"⚠️ Closing {open_brackets - close_brackets} incomplete arrays...")
                json_str += ']' * (open_brackets - close_brackets)
            
            # Close any incomplete objects
            if open_braces > close_braces:
                print(f"⚠️ Closing {open_braces - close_braces} incomplete objects...")
                json_str += '}' * (open_braces - close_braces)
            
            print("✓ Attempting to parse completed JSON...")
            result = json.loads(json_str)
            print("✅ Successfully recovered incomplete JSON!")
            return result
            
        except Exception as completion_error:
            print(f"❌ JSON completion failed: {str(completion_error)}")
            pass
            
        return {}