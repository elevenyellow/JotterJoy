import os
from typing import Optional
from groq import AsyncGroq
from jotterjoy.app.utils.openai_like_service import OpenAILikeService


# llama3-70b-8192
# llama3-8b-8192


class GroqService(OpenAILikeService):
    def __init__(self, model_name: str):
        async_client = AsyncGroq(
            # This is the default and can be omitted
            api_key=os.environ.get("GROQ_API_KEY")
            or "NONE",
        )
        super().__init__(
            async_client=async_client,
            model_name=model_name,
        )

    async def generate_response(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        api_key: Optional[str] = None,
    ) -> str:
        if api_key:
            self.async_client.api_key = api_key

        return await super().generate_response(prompt, system_prompt)
