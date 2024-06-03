from typing import Tuple
from app.utils import DEFAULT_AI_SERVICE
from app.utils.prompt_utils import Prompt, get_prompt


async def afix_spelling(text: str) -> str:
    ai_service = DEFAULT_AI_SERVICE

    prompt, system_prompt = create_prompt(text)
    response = await ai_service.generate_response(prompt, system_prompt)
    entities = await ai_service.extract_entities(response)
    corrected_text = entities.get("corrected_text") or text
    corrected_text = corrected_text.strip()

    return corrected_text


def create_prompt(text: str) -> Tuple[str, str]:
    system_prompt = get_prompt(Prompt.fix_text)
    prompt = text

    return prompt, system_prompt
