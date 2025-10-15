from langchain_groq import ChatGroq

def initiate_model(token):
    model_name = "llama-3.1-8b-instant"
    chat_model = ChatGroq(
        model=model_name,
        temperature=0.0,
        max_tokens=4096,
        api_key=token
    )
    print("LLM initialized")
    return chat_model
