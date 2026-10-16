import gradio as gr
import requests


API_URL = "http://127.0.0.1:8000/api/v1/predict"


def analisis_sentimen(text):
    if not text or len(text.strip()) < 3:
        return "Komentar minimal 3 karakter.", ""

    try:
        response = requests.post(
            API_URL,
            json={"text": text},
            timeout=10,
        )
        response.raise_for_status()
        result = response.json()

        label = result["label"]
        score = float(result["score"])

        return label, f"{score:.2%}"

    except requests.RequestException:
        return "Layanan FastAPI tidak dapat diakses.", ""
    except (ValueError, KeyError, TypeError):
        return "Respons API tidak sesuai format.", ""


demo = gr.Interface(
    fn=analisis_sentimen,
    inputs=gr.Textbox(
        label="Komentar Mahasiswa",
        placeholder="Tulis komentar layanan kampus...",
        lines=4,
    ),
    outputs=[
        gr.Textbox(label="Label Sentimen"),
        gr.Textbox(label="Score"),
    ],
    title="SentiKampus",
    description="Analisis Sentimen Komentar Mahasiswa",
    submit_btn="Analisis",
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
