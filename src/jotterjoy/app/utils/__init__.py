from jotterjoy.app.utils.ai_service import AIService
from jotterjoy.app.utils.groq_service import GroqService
from jotterjoy.models.llm_model import LLMModel


llmmodel = LLMModel.groq_llama3_8b_8192


def init_ai_service(model: LLMModel):
    global llmmodel
    llmmodel = model


def get_ai_service() -> AIService:
    if llmmodel == LLMModel.groq_llama3_8b_8192:
        return GroqService(model_name="llama3-8b-8192")
    elif llmmodel == LLMModel.groq_llama3_70b_8192:
        return GroqService(model_name="llama3-70b-8192")
    else:
        raise ValueError(f"Unsupported model: {llmmodel}")
