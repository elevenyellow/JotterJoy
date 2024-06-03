# app/routers/documents.py
from fastapi import APIRouter, UploadFile, File
from app.services import spelling, tagging, title

router = APIRouter(prefix="/documents", tags=["documents"])


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    # Process the uploaded document
    content = await file.read()
    text = content.decode("utf-8")

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


@router.post("/spelling")
async def fix_spelling(text: str):
    fixed_text = await spelling.afix_spelling(text)
    return {"fixed_text": fixed_text}


@router.post("/title")
async def generate_title(text: str):
    fixed_title = await title.aget_title(text)
    return {"slug_title": fixed_title}


@router.post("/tags")
async def find_tags(text: str):
    tags = await tagging.afind_tags(text)
    return {"tags": tags}
