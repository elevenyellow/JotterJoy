from typing import List


class DocumentOutput:
    text: str
    tags: List[str]

    def __init__(self, text: str, tags: list):
        self.text = text
        self.tags = tags
