from fastapi import FastAPI
from app.routers import documents
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()

app.include_router(documents.router)


@app.get("/")
def root():
    return {"message": "Welcome to the Document Processing API"}
