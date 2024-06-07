from abc import ABC
from typing import Any, Optional
from jotterjoy.app.utils.ai_service import AIService


class ClientInterface:
    api_key: str

    def __init__(self):
        # Initialize the client interface
        pass

    def chat(self) -> Any:
        # Method to handle chat completions
        pass


class OpenAILikeService(AIService, ABC):
    async_client: ClientInterface
    model_name: str

    def __init__(self, async_client, model_name: str):
        self.async_client = async_client
        self.model_name = model_name

    async def achat_completion(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
    ) -> str:
        messages = []
        if system_prompt:
            messages.append(
                {
                    "role": "system",
                    "content": system_prompt,
                }
            )

        messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        chat_completion = await self.async_client.chat.completions.create(
            messages=messages,
            model=self.model_name,
            temperature=0.0,
        )

        result = chat_completion.choices[0].message.content

        return result

    async def generate_response(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        api_key: Optional[str] = None,
    ) -> str:
        result = await self.achat_completion(prompt, system_prompt)
        return result
