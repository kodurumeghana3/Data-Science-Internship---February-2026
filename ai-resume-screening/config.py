from langchain_groq import ChatGroq

def get_llm(temp=0.0):
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=temp
    )