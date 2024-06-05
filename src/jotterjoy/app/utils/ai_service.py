from abc import ABC, abstractmethod
import re
from typing import Dict, Optional


class AIService(ABC):
    @abstractmethod
    async def generate_response(
        self, prompt: str, system_prompt: Optional[str] = None
    ) -> str:
        pass

    async def extract_entities(self, text: str) -> Dict[str, str]:
        """Extracts entities from the given text based on XML tags.

        Args:
            text (str): The text to extract entities from.

        Returns:
            Dict[str, str]: A dictionary containing the extracted entities.
        """

        pattern = r"<(\w+)>([^<]+)</\1>"

        matches = re.findall(pattern, text)

        tag_dict = {}

        for tag, value in matches:
            # Check if the tag already exists in the dictionary
            if tag in tag_dict:
                raise Exception(f"Duplicate tag found: {tag}")

            # Add the tag and its value to the dictionary
            tag_dict[tag] = value

        return tag_dict
