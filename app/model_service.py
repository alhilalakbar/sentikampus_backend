import pickle
from pathlib import Path


MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "sentiment.pkl"


with MODEL_PATH.open("rb") as f:
    model = pickle.load(f)


def predict_text(text: str):
    label = model.predict([text])[0]

    probabilities = model.predict_proba([text])[0]

    score = float(max(probabilities))

    return {
        "label": label,
        "score": score
    }
