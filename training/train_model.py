import pickle
from pathlib import Path

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


texts = [
    "pelayanan sangat cepat",
    "petugas sangat ramah",
    "pelayanan kampus sangat baik",
    "informasi sangat jelas",
    "pelayanan sangat lambat",
    "petugas tidak ramah",
    "pelayanan kampus buruk",
    "informasi sangat membingungkan",
]

labels = [
    "positive",
    "positive",
    "positive",
    "positive",
    "negative",
    "negative",
    "negative",
    "negative",
]


pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("model", LogisticRegression())
])


pipeline.fit(texts, labels)


model_path = Path("models/sentiment.pkl")

with model_path.open("wb") as f:
    pickle.dump(pipeline, f)

print("Model berhasil disimpan ke:", model_path)
