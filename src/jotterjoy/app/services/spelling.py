from typing import Optional, Tuple
from jotterjoy.app.utils import get_ai_service
from jotterjoy.app.utils.prompt_utils import Prompt, get_prompt


async def afix_spelling(text: str, api_key: Optional[str]) -> str:
    ai_service = get_ai_service()

    prompt, system_prompt = create_prompt(text)
    response = await ai_service.generate_response(
        prompt,
        system_prompt,
        api_key,
    )
    entities = await ai_service.extract_entities(response)
    corrected_text = entities.get("corrected_text") or text
    corrected_text = corrected_text.strip()

    return corrected_text


def create_prompt(text: str) -> Tuple[str, str]:
    system_prompt = get_prompt(Prompt.fix_text)
    prompt = text

    return prompt, system_prompt
