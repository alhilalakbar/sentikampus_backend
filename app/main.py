from app.model_service import predict_text
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .schemas import SentimentRequest, SentimentResponse


app = FastAPI(title="SentiKampus API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post(
    "/api/v1/predict",
    response_model=SentimentResponse
)
def predict(data: SentimentRequest):
    if not data.text.strip():
        raise HTTPException(
            status_code=400,
            detail="Komentar tidak boleh kosong"
        )

    result = predict_text(data.text)

    return SentimentResponse(**result)
