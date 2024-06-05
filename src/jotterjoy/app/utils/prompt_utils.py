from enum import Enum
import os
import sys


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS  # type: ignore
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Prompt(Enum):
    fix_text = "fix_text"
    tagging = "tagging"
    generate_title = "generate_title"


def get_prompt(type: Prompt) -> str:
    return _load_prompt_text(type)


# Location src/prompts/*.txt
def _load_prompt_text(prompt: Prompt) -> str:
    path = resource_path(f"src/jotterjoy/prompts/{prompt.value}.txt")
    with open(path) as f:
        return f.read()
