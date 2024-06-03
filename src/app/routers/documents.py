# app/routers/documents.py
from fastapi import APIRouter, UploadFile, File
from app.services import spelling, grammar, tagging

router = APIRouter(prefix="/documents", tags=["documents"])


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    # Process the uploaded document
    content = await file.read()
    text = content.decode("utf-8")

    # Perform document processing tasks
    corrected_text = await spelling.afix_spelling(text)
    tags = await tagging.afind_tags(corrected_text)

    # Return the processed document
    return {
        "corrected_text": corrected_text,
        # "fixed_grammar": fixed_grammar,
        "tags": tags,
    }


@router.post("/spelling")
async def fix_spelling(text: str):
    fixed_text = await spelling.afix_spelling(text)
    return {"fixed_text": fixed_text}


@router.post("/grammar")
async def fix_grammar(text: str):
    fixed_text = grammar.fix_grammar(text)
    return {"fixed_text": fixed_text}


@router.post("/tags")
async def find_tags(text: str):
    tags = await tagging.afind_tags(text)
    return {"tags": tags}
