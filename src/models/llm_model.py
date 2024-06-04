from enum import Enum


class LLMModel(str, Enum):
    groq_llama3_70b_8192 = "groq:llama3-70b-8192"
    groq_llama3_8b_8192 = "groq:llama3-8b-8192"
