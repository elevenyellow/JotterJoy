import re
from typing import Optional, Tuple
import unicodedata
from app.utils import DEFAULT_AI_SERVICE
from app.utils.prompt_utils import Prompt, get_prompt


async def aget_title(text: str) -> Optional[str]:
    ai_service = DEFAULT_AI_SERVICE

    prompt, system_prompt = create_prompt(text)
    response = await ai_service.generate_response(prompt, system_prompt)
    entities = await ai_service.extract_entities(response)
    corrected_text = entities.get("file_name") or None
    corrected_text = corrected_text and corrected_text.strip()
    corrected_text = corrected_text and slugify(corrected_text)

    return corrected_text


def create_prompt(text: str) -> Tuple[str, str]:
    system_prompt = get_prompt(Prompt.generate_title)
    prompt = text

    return prompt, system_prompt


def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize("NFKC", value)
    else:
        value = (
            unicodedata.normalize("NFKD", value)
            .encode("ascii", "ignore")
            .decode("ascii")
        )
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-\s]+", "-", value).strip("-_")
