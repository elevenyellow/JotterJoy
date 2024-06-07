import json
from typing import Annotated, Any
from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel, model_validator
from jotterjoy.app.services import spelling, tagging, title
from jotterjoy.app.utils import init_ai_service
from jotterjoy.models.llm_model import LLMModel

router = APIRouter(prefix="/documents", tags=["documents"])


# InputParams
class InputParams(BaseModel):
    model: LLMModel = LLMModel.groq_llama3_8b_8192

    @model_validator(mode="before")
    @classmethod
    def validate_to_json(cls, value: Any) -> Any:
        print(value)
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value


# File is markdown
@router.post("/upload")
async def upload_document(
    file: Annotated[
        UploadFile,
        File(
            media_type="text/markdown",
            description="Markdown file",
            example="markdown.md",
            alias="file",
        ),
    ],
    input_params: InputParams = InputParams(),
):
    if file.content_type != "text/markdown":
        raise HTTPException(
            status_code=400,
            detail="File must be a markdown file",
        )

    # Process the uploaded document
    content = await file.read()
    text = content.decode("utf-8")

    # Initialize the AI service
    init_ai_service(input_params.model)

    # Perform document processing tasks
    fixed_text = await spelling.afix_spelling(text)
    tags = await tagging.afind_tags(fixed_text)
    fixed_title = await title.aget_title(fixed_text)

    # Return the processed document
    return {
        "fixed_text": fixed_text,
        "slug_title": fixed_title,
        "tags": tags,
    }


@router.post("/tags")
async def get_tags(
    text: str,
    input_params: InputParams = InputParams(),
):
    init_ai_service(input_params.model)
    tags = await tagging.afind_tags(text)
    return {"tags": tags}


@router.post("/fix-text")
async def fix_text(
    text: str,
    input_params: InputParams = InputParams(),
):
    init_ai_service(input_params.model)
    fixed_text = await spelling.afix_spelling(text)
    return {"fixed_text": fixed_text}
