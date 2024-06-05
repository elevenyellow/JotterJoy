from datetime import datetime
from typing import Tuple

from jotterjoy.app.utils import get_ai_service
from jotterjoy.app.utils.prompt_utils import Prompt, get_prompt
from jotterjoy.app.utils.text_utils import slugify


async def afind_tags(text: str) -> list:
    ai_service = get_ai_service()

    prompt, system_prompt = create_prompt(text)
    response = await ai_service.generate_response(prompt, system_prompt)
    entities = await ai_service.extract_entities(response)
    tags = entities.get("tags") or ""
    # Seperated by dash
    tags = tags.split(",")
    tags = [slugify(tag.strip()) for tag in tags]
    tags = list(filter(None, tags))

    when_tag = datetime.now().strftime("%Y-%m-%d")
    tags.append(when_tag)

    return tags


def create_prompt(text: str) -> Tuple[str, str]:
    system_prompt = get_prompt(Prompt.tagging)
    prompt = text

    return prompt, system_prompt
