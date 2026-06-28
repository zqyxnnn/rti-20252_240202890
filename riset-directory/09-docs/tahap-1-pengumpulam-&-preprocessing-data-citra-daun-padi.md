# Tahap 1 — Pengumpulan & Preprocessing Data Citra Daun Padi
**Status:** Selesai

---

## 1. Sumber Data & Parameter

1. Dataset: Dataset Citra Penyakit Daun Padi (Publik/Repositori).
2. Kategori Penyakit: Bacterial Blight, Blast, Brown Spot, Tungro (atau sesuai kategori dataset yang digunakan).
3. Total Citra: [Masukkan jumlah total data, misal: 3.500] citra.
4. Format Data: JPG/PNG dengan label kelas berbasis folder.
5. Penyedia: Dataset sekunder (referensi dari Shinta [2023] & Asseweth [2024]).

## 2. Implementasi Preprocessing & Data Augmentation

```
1. Resizing: Penyeragaman dimensi citra ke resolusi 64 x 64 x3 piksel untuk efisiensi komputasi pada arsitektur VGG-19 dan DenseNet-169.
2. Normalisasi: Skalasi nilai piksel dari rentang [0, 255] menjadi [0, 1] dengan membagi setiap piksel dengan 255.0 untuk stabilitas konvergensi bobot model.
3. Data Augmentation: Penerapan teknik on-the-fly augmentation guna meningkatkan generalisasi model dan mencegah overfitting, meliputi:
    - Random Rotation (hingga 20 derajat).
    - Horizontal Flip.Zoom Range (0.2).
    - Width/Height Shift.
4. Data Splitting: Pembagian dataset secara acak (stratified) untuk mempertahankan proporsi antar-kelas:
    - Training Set (80%): Digunakan untuk proses learning fitur pada lapisan konvolusi.
    - Validation Set (10%): Digunakan untuk memantau hyperparameter tuning selama training.Testing Set (10%): 
    - Digunakan untuk evaluasi final performa model.

## 4. Hasil & Output yang Dihasilkan

1. Struktur Direktori Data: Dataset telah dipetakan ke dalam struktur train, val, dan test di dalam folder 04-data/.
2. Data Metadata: Berkas dataset_summary.csv berisi rincian jumlah citra per kelas yang telah divalidasi.
3. Preprocessing Script: Kode 05-kode/preprocessing.py tersimpan untuk menjamin reproducibility (keterulangan) proses pembersihan dan augmentasi data.
4. Visualisasi Sampel: Dokumentasi sampel citra asli vs hasil augmentasi tersimpan di 06-output/preprocessing_samples/.