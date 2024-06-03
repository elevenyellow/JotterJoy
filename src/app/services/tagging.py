from typing import Tuple

from app.utils import DEFAULT_AI_SERVICE
from app.utils.prompt_utils import Prompt, get_prompt


async def afind_tags(text: str) -> list:
    ai_service = DEFAULT_AI_SERVICE

    prompt, system_prompt = create_prompt(text)
    response = await ai_service.generate_response(prompt, system_prompt)
    entities = await ai_service.extract_entities(response)
    tags = entities.get("tags") or ""
    # Seperated by dash
    tags = tags.split(",")
    tags = [tag.strip().lower() for tag in tags]
    tags = list(filter(None, tags))

    return tags


def create_prompt(text: str) -> Tuple[str, str]:
    system_prompt = get_prompt(Prompt.tagging)
    prompt = text

    return prompt, system_prompt
