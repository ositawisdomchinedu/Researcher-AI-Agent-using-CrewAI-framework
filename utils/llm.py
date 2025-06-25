from crewai import LLM
from config.settings import GROQ_MODEL, GROQ_API_KEY, GROQ_API_BASE

def get_llm(): 
    return LLM(
    model=GROQ_MODEL,
    api_key=GROQ_API_KEY,
    base_url=GROQ_API_BASE,
    temperature=0.3,
    max_tokens=4096
)
