# SentiKampus Backend

Backend untuk aplikasi **SentiKampus**, yaitu layanan analisis sentimen
teks yang dibangun menggunakan Python, FastAPI, dan scikit-learn.
Backend menerima teks dari aplikasi Flutter, memprosesnya menggunakan
model machine learning yang telah dilatih, lalu mengembalikan hasil
prediksi melalui REST API.

## Teknologi

-   **Python** --- bahasa pemrograman backend.
-   **FastAPI** --- framework untuk menyediakan REST API.
-   **scikit-learn** --- digunakan dalam proses pelatihan model machine
    learning.
-   **Uvicorn** --- menjalankan server FastAPI.
-   **Swagger UI** --- menguji endpoint API melalui browser.

## Struktur Proyek

Struktur utama backend berdasarkan implementasi proyek:

``` text
sentikampus_backend/
├── app/
│   ├── main.py
│   ├── model_service.py
│   └── schemas.py
├── models/
│   └── sentiment.pkl
├── training/
│   └── train_model.py
├── .venv/
├── .gitignore
├── requirements.txt
└── README.md
```

> Catatan: sesuaikan nama file pada bagian `training/` dengan nama file
> pelatihan yang benar-benar digunakan di repository jika berbeda.

## Persiapan

Pastikan Python 3, `pip`, dan Git sudah tersedia di sistem.

Clone repository:

``` bash
git clone git@github.com:alhilalakbar/sentikampus_backend.git
cd sentikampus_backend
```

### 1. Membuat virtual environment

Di Linux atau macOS:

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

Di Windows PowerShell:

``` powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Menginstal dependensi

Dengan virtual environment aktif, jalankan:

``` bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Jika scikit-learn belum tercantum dalam `requirements.txt`, tambahkan
dependensi yang dibutuhkan proyek sebelum menjalankan pelatihan model.

## Model Machine Learning

Model sentimen disimpan pada file `models/sentiment.pkl`. Skrip
pelatihan berada di direktori `training/`.

Jalankan skrip pelatihan sesuai nama file yang tersedia di repository.
Contoh jika file-nya bernama `train_model.py`:

``` bash
python training/train_model.py
```

Pastikan proses pelatihan berhasil dan file model `models/sentiment.pkl`
tersedia sebelum menjalankan API.

## Menjalankan Backend

Aktifkan virtual environment terlebih dahulu, lalu jalankan server dari
direktori utama proyek:

``` bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Jika server berjalan, dokumentasi interaktif Swagger UI dapat dibuka
melalui:

-   Komputer yang sama: `http://127.0.0.1:8000/docs`
-   Perangkat lain di jaringan yang sama:
    `http://ALAMAT-IP-KOMPUTER:8000/docs`

Ganti `ALAMAT-IP-KOMPUTER` dengan alamat IP LAN komputer yang
menjalankan backend.

## Endpoint API

  -----------------------------------------------------------------------
  Metode                  Endpoint                Kegunaan
  ----------------------- ----------------------- -----------------------
  `GET`                   `/health`               Memeriksa status
                                                  layanan API.

  `POST`                  `/api/v1/predict`       Mengirim teks untuk
                                                  mendapatkan prediksi
                                                  sentimen.
  -----------------------------------------------------------------------

### Menguji prediksi sentimen

1.  Jalankan backend.
2.  Buka `/docs` pada browser.
3.  Pilih endpoint `POST /api/v1/predict`.
4.  Klik **Try it out**.
5.  Masukkan request body sesuai skema yang ditampilkan Swagger.
6.  Klik **Execute** dan periksa respons API.

Contoh teks yang dapat digunakan untuk pengujian:

-   `Pelayanan sangat cepat`
-   `Pelayanan sangat lambat`
-   `Petugas tidak ramah`

Bentuk request body dan nama field mengikuti skema yang diterapkan pada
endpoint di versi kode saat ini.

### Validasi input kosong

Backend dalam implementasi tugas memvalidasi teks kosong atau teks yang
hanya berisi spasi. Pengujian input tersebut diharapkan menghasilkan
respons HTTP `400` sesuai implementasi yang dijelaskan dalam laporan.

## Integrasi dengan Aplikasi Flutter

Backend ini digunakan oleh aplikasi Flutter `sentikampus2` melalui
layanan API di `lib/services/api_service.dart`.

Pastikan alamat API pada aplikasi Flutter sesuai dengan lingkungan yang
digunakan:

-   **Flutter di komputer yang sama:** gunakan `http://127.0.0.1:8000`
    jika berjalan pada host yang sama.
-   **Flutter pada emulator Android:** gunakan alamat host yang dapat
    diakses dari emulator, umumnya `http://10.0.2.2:8000` untuk Android
    Emulator standar.
-   **Flutter pada handphone fisik:** gunakan alamat IP LAN komputer,
    misalnya `http://192.168.1.6:8000`, dan pastikan kedua perangkat
    berada pada jaringan yang dapat saling menjangkau.

Alamat IP pada contoh di atas hanya contoh. Gunakan alamat yang sesuai
dengan jaringan saat ini.

## Troubleshooting

**Server tidak dapat dijalankan** - Pastikan virtual environment sudah
aktif. - Pastikan dependensi pada `requirements.txt` sudah terpasang. -
Jalankan perintah Uvicorn dari direktori utama repository.

**File model tidak ditemukan** - Pastikan `models/sentiment.pkl` sudah
tersedia. - Jika file belum tersedia, jalankan skrip pelatihan model
sesuai struktur repository.

**Flutter tidak dapat terhubung ke API** - Pastikan server FastAPI masih
aktif. - Periksa kembali alamat API pada `api_service.dart`. - Untuk
handphone fisik, jangan gunakan `127.0.0.1` untuk menunjuk ke komputer;
gunakan IP LAN komputer. - Pastikan firewall dan jaringan mengizinkan
koneksi ke port `8000`.

**Input kosong ditolak** - Periksa teks yang dikirim. API memvalidasi
masukan kosong atau yang hanya berisi spasi.

## Repository

-   SSH: `git@github.com:alhilalakbar/sentikampus_backend.git`
-   HTTPS: `https://github.com/alhilalakbar/sentikampus_backend`

------------------------------------------------------------------------

Proyek ini dikembangkan sebagai bagian dari tugas mata kuliah Kecerdasan
Buatan, Pertemuan 3.
