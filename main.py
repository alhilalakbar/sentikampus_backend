from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="SentiKampus API")


class CommentRequest(BaseModel):
    comment: str


@app.get("/")
def root():
    return {
        "message": "SentiKampus API berjalan"
    }


@app.post("/predict")
def predict(request: CommentRequest):
    return {
        "comment": request.comment,
        "sentiment": "positif"
    }
