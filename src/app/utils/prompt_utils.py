from enum import Enum


class Prompt(Enum):
    fix_text = "fix_text"
    tagging = "tagging"


def get_prompt(type: Prompt) -> str:
    return _load_prompt_text(type)


# Location src/prompts/*.txt
def _load_prompt_text(prompt: Prompt) -> str:
    with open(f"src/prompts/{prompt.value}.txt") as f:
        return f.read()
