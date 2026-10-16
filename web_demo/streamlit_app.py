import requests
import streamlit as st

st.title("SentiKampus")
st.subheader("Analisis Sentimen Komentar Mahasiswa")

text = st.text_area("Tulis komentar layanan")

if st.button("Analisis"):
    if len(text.strip()) < 3:
        st.warning("Komentar minimal 3 karakter")
    else:
        try:
            response = requests.post(
                "http://127.0.0.1:8000/api/v1/predict",
                json={"text": text},
                timeout=10,
            )
            response.raise_for_status()
            result = response.json()

            st.metric("Label", result["label"])
            st.progress(
                max(0.0, min(1.0, float(result["score"])))
            )

        except requests.RequestException:
            st.error("Layanan FastAPI belum dapat diakses")
        except (ValueError, KeyError, TypeError):
            st.error("Respons API tidak sesuai format yang diharapkan")
