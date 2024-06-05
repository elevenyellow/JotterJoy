import os
from groq import AsyncGroq
from jotterjoy.app.utils.openai_like_service import OpenAILikeService


# llama3-70b-8192
# llama3-8b-8192


class GroqService(OpenAILikeService):
    def __init__(self, model_name: str):
        async_client = AsyncGroq(
            # This is the default and can be omitted
            api_key=os.environ.get("GROQ_API_KEY"),
        )
        super().__init__(
            async_client=async_client,
            model_name=model_name,
        )