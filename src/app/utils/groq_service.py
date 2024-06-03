import os
from groq import AsyncGroq
from app.utils.openai_like_service import OpenAILikeService


class GroqService(OpenAILikeService):
    def __init__(self):
        async_client = AsyncGroq(
            # This is the default and can be omitted
            api_key=os.environ.get("GROQ_API_KEY"),
        )
        super().__init__(
            async_client=async_client,
            model_name="llama3-8b-8192",
        )
