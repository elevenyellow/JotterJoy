import multiprocessing
from fastapi import FastAPI
import uvicorn
from jotterjoy.app.routers import documents
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()

app.include_router(documents.router)


@app.get("/")
def root():
    return {"message": "Welcome to the Document Processing API"}


if __name__ == "__main__":
    multiprocessing.freeze_support()  # For Windows support
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False, workers=1)
