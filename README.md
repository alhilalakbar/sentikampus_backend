# SentiKampus Backend

Backend untuk aplikasi **SentiKampus**, yaitu layanan analisis sentimen teks menggunakan Python, FastAPI, dan scikit-learn.

Backend menerima komentar, memprosesnya menggunakan model machine learning yang telah dilatih, lalu mengembalikan hasil prediksi melalui REST API. API ini digunakan bersama oleh aplikasi web Streamlit, Gradio, dan aplikasi Flutter.

## Teknologi

- **Python** — bahasa pemrograman backend.
- **FastAPI** — framework REST API.
- **Uvicorn** — server ASGI untuk menjalankan FastAPI.
- **scikit-learn** — pelatihan dan pemrosesan model machine learning.
- **Streamlit** — antarmuka web untuk analisis sentimen.
- **Gradio** — antarmuka web alternatif untuk analisis sentimen.
- **HTTPX/Requests dan HTTP** — komunikasi antar-komponen sesuai kebutuhan dependensi aplikasi.

## Struktur Proyek

```text
sentikampus_backend/
├── app/
│   ├── main.py
│   ├── model_service.py
│   └── schemas.py
├── models/
│   └── sentiment.pkl
├── training/
│   └── train_model.py
├── web_demo/
│   ├── streamlit_app.py
│   └── gradio_app.py
├── requirements.txt
├── .gitignore
└── README.md
```

Folder `.venv/` dibuat secara lokal ketika menyiapkan virtual environment dan tidak perlu diunggah ke Git.

## 1. Persiapan

Pastikan Python 3, `pip`, dan Git sudah terpasang.

Clone repository:

```bash
git clone git@github.com:alhilalakbar/sentikampus_backend.git
cd sentikampus_backend
```

Jika menggunakan HTTPS:

```bash
git clone https://github.com/alhilalakbar/sentikampus_backend.git
cd sentikampus_backend
```

## 2. Membuat Virtual Environment

Di Linux atau Linux Mint:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Jika perintah `venv` belum tersedia, pasang paket pendukung Python sesuai versi Python pada sistem.

Di Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## 3. Menginstal Dependensi

Dengan virtual environment aktif:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Pastikan dependensi untuk aplikasi web demo juga tersedia. Jika belum tercantum di `requirements.txt`, instal:

```bash
pip install streamlit gradio requests
```

## 4. Memastikan Model Machine Learning

Model yang digunakan API berada di:

```text
models/sentiment.pkl
```

Skrip pelatihan model berada di:

```text
training/train_model.py
```

Jika file model belum tersedia, jalankan:

```bash
python training/train_model.py
```

Pastikan proses pelatihan berhasil sebelum menjalankan backend.

Jika file model sudah tersedia dan dapat dimuat oleh aplikasi, pelatihan ulang tidak diperlukan setiap kali server dijalankan.

## 5. Menjalankan FastAPI

Pastikan terminal berada di direktori utama `sentikampus_backend` dan virtual environment sudah aktif.

Jalankan:

```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Biarkan terminal ini tetap berjalan selama aplikasi frontend digunakan.

Dokumentasi API dapat dibuka melalui:

- Swagger UI: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/health

## 6. Menguji Endpoint API

Endpoint utama untuk analisis sentimen:

```text
POST /api/v1/predict
```

Buka Swagger UI, pilih `POST /api/v1/predict`, klik **Try it out**, lalu masukkan contoh berikut:

```json
{
  "text": "Pelayanan kampus sangat baik"
}
```

Klik **Execute** dan periksa respons yang berisi label sentimen dan skor prediksi.

Contoh komentar lain:

- `Pelayanan sangat cepat`
- `Pelayanan sangat lambat`
- `Petugas tidak ramah`

Hasil prediksi dan skor bergantung pada model yang digunakan.

## 7. Menjalankan Streamlit

Buka terminal baru. Masuk ke direktori backend dan aktifkan virtual environment:

```bash
cd ~/projects/project_kecerdasan_buatan/sentikampus_backend
source .venv/bin/activate
```

Jalankan aplikasi Streamlit:

```bash
streamlit run web_demo/streamlit_app.py
```

Streamlit biasanya tersedia melalui:

http://localhost:8501

Masukkan komentar, kemudian tekan tombol **Analisis**. Aplikasi akan mengirimkan komentar ke FastAPI dan menampilkan hasil prediksi.

## 8. Menjalankan Gradio

Buka terminal baru dan aktifkan virtual environment yang sama:

```bash
cd ~/projects/project_kecerdasan_buatan/sentikampus_backend
source .venv/bin/activate
```

Jalankan:

```bash
python web_demo/gradio_app.py
```

Buka alamat lokal yang ditampilkan di terminal Gradio. Masukkan komentar dan tekan tombol submit untuk melihat hasil analisis sentimen.

**Catatan:** FastAPI harus tetap berjalan saat Streamlit maupun Gradio digunakan.

## 9. Integrasi dengan Flutter

Frontend Flutter merupakan proyek terpisah dari repository backend.

Untuk praktikum Pertemuan 4, proyek Flutter yang digunakan adalah `sentikampus_mobile`.

Alamat API harus disesuaikan dengan perangkat yang menjalankan Flutter:

- **Flutter di komputer yang sama:** `http://127.0.0.1:8000`
- **Android Emulator standar:** `http://10.0.2.2:8000`
- **Handphone fisik:** gunakan alamat IP LAN komputer yang menjalankan FastAPI, misalnya `http://192.168.1.6:8000`.

Untuk handphone fisik, pastikan kedua perangkat dapat saling terhubung melalui jaringan dan firewall mengizinkan koneksi ke port 8000.

## 10. Mengambil Perubahan Terbaru dari GitHub

Jika repository sudah pernah di-clone:

```bash
cd sentikampus_backend
git switch main
git pull origin main
```

Jika belum memiliki repository lokal, gunakan perintah `git clone` pada bagian persiapan.

`git pull` mengambil perubahan yang sudah diunggah ke repository remote. Dependensi baru tetap perlu dipasang secara lokal jika diperlukan.

## Troubleshooting

### FastAPI gagal dijalankan

- Pastikan virtual environment aktif.
- Pastikan dependensi sudah terpasang.
- Jalankan Uvicorn dari direktori utama backend.
- Pastikan port 8000 tidak sedang digunakan proses lain.

### Model tidak ditemukan

Pastikan file `models/sentiment.pkl` tersedia dan dapat dibaca oleh backend. Jika belum tersedia, jalankan skrip pelatihan model.

### Streamlit atau Gradio tidak dapat menghubungi API

- Pastikan FastAPI masih berjalan.
- Pastikan alamat endpoint benar.
- Pastikan dependensi frontend sudah terpasang.
- Periksa pesan error pada terminal masing-masing aplikasi.

### Flutter tidak dapat terhubung

- Periksa alamat API di layanan Flutter.
- Untuk handphone fisik, gunakan IP LAN komputer, bukan `127.0.0.1`.
- Pastikan jaringan dan firewall mengizinkan koneksi ke port 8000.

## Repository

- SSH: `git@github.com:alhilalakbar/sentikampus_backend.git`
- HTTPS: https://github.com/alhilalakbar/sentikampus_backend

Proyek ini dikembangkan sebagai bagian dari tugas mata kuliah Kecerdasan Buatan, khususnya praktikum Pertemuan 3 dan Pertemuan 4.