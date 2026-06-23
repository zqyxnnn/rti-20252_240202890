Berdasarkan WS 9, 10, dan 11 yang telah Anda berikan, saya telah menyusun ulang file `05-kode/README.md` agar sinkron secara teknis, menggunakan ukuran **64x64 piksel** sesuai aturan WS Anda, serta mencerminkan prinsip *Config-driven*, *Repeatability*, dan *Data Integrity* yang diminta.

Berikut adalah isi lengkap untuk `05-kode/README.md`:

```markdown
# 05-kode

Source code implementasi untuk pengujian stabilitas klasifikasi penyakit daun padi menggunakan arsitektur VGG-19 dan DenseNet-169.

## Struktur Direktori

```text
05-kode/
├── klasifikasi_daun_padi.ipynb   # Jupyter Notebook utama (Data Preprocessing, Arsitektur CNN, & Training)
├── run_stability_test.py         # Skrip Python runner untuk mengeksekusi iterasi otomatis sebanyak 35 kali
└── hyperparams_config.json       # Konfigurasi parameter (batch size, learning rate, epoch, optimizer, image_size)

```

## Deskripsi Komponen

1. **`klasifikasi_daun_padi.ipynb`**:
* **Data Preprocessing**: Melakukan *resize* citra daun padi ke ukuran 64 x 64 piksel sesuai spesifikasi teknis WS 9-11 dan normalisasi nilai matriks warna.
* **Model VGG-19**: Implementasi arsitektur VGG-19 dengan metode *transfer learning* untuk ekstraksi fitur penyakit daun padi.
* **Model DenseNet-169**: Implementasi arsitektur DenseNet-169 memanfaatkan *dense blocks* untuk memitigasi risiko *vanishing gradient*.
* **Evaluasi**: Sistem otomatis mengekspor metrik akurasi akhir setiap sesi pelatihan sesuai kaidah koleksi data terstruktur.

2. **`run_stability_test.py`**:
* **Execution Plan**: Menjalankan eksperimen secara *batch* sebanyak 35 *runs* per skenario model.
* **Determinisme**: Mengubah nilai *random seed* (43–77) secara dinamis di setiap *run* untuk memenuhi syarat pengujian stabilitas statistik.
* **Logging**: Mengekspor hasil akurasi ke `../04-data/training_runs.csv` sebagai *dataset* untuk analisis statistik inferensial (Teorema Limit Pusat).

3. **`hyperparams_config.json`**:
* Berkas konfigurasi *config-driven* agar eksperimen bersifat *reproducible* dan tidak *hardcoded*.
* Parameter utama: `image_size: 64`, `epochs: 50`, `batch_size: 32`, `optimizer: "Adam"`, `learning_rate: 0.001`.

## Cara Menjalankan Eksperimen 35x

Untuk mengeksekusi seluruh 35 *runs* pengujian stabilitas secara otomatis, buka Terminal di direktori `05-kode/` dan jalankan:

python3 run_stability_test.py