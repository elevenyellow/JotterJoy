from typing import Optional, Tuple
from jotterjoy.app.utils import get_ai_service
from jotterjoy.app.utils.prompt_utils import Prompt, get_prompt


async def aget_title(text: str) -> Optional[str]:
    ai_service = get_ai_service()

    prompt, system_prompt = create_prompt(text)
    response = await ai_service.generate_response(prompt, system_prompt)
    entities = await ai_service.extract_entities(response)
    corrected_text = entities.get("file_name") or None
    corrected_text = corrected_text and corrected_text.strip()

    return corrected_text


def create_prompt(text: str) -> Tuple[str, str]:
    system_prompt = get_prompt(Prompt.generate_title)
    prompt = text

    return prompt, system_prompt
