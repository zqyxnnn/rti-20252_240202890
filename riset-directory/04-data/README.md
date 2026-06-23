# 04-data

Data mentah hasil pengujian dan dataset awal — output dari **Tahap 1 (Pengumpulan Data)** & **Tahap 3 (Eksperimen Model)**, input untuk **Tahap 4 (Analisis & Evaluasi)**.

## Isi yang diharapkan

- **Dataset Citra Mentah (Raw Images):** Kumpulan data gambar asli daun tanaman padi yang belum diolah, terbagi ke dalam kategori penyakit (misal: *Brown Spot*, *Bacterial Leaf Blight*, *Blast*, *Tungro*, atau *Healthy*) berformat JPG/PNG.
- **Log Histori Training Model (CSV/JSON):** File log mentah hasil proses *training* dan *validation* per epoch (mencakup nilai *loss*, *accuracy*, *val_loss*, dan *val_accuracy*) untuk setiap arsitektur yang diuji (seperti EfficientNet B3, DenseNet-169, VGG-19, atau MobileNetv2).
- **Metadata Konfigurasi Uji (`metadata.json`):** Berkas yang mencatat parameter dasar eksperimen seperti total *dataset*, ukuran *resize* gambar (misal: 224x224), nilai *learning rate*, *batch size*, tipe *optimizer* (Adam/SGD), dan pembagian rasio data (*train/val/test split*).

## Catatan

Data di folder ini bersifat mentah (*raw data*) langsung dari repositori dataset (seperti Kaggle/UCI Machine Learning) dan hasil *export* log training program Python/TensorFlow/PyTorch, serta belum diolah menjadi grafik. Hasil olahan akhir seperti *Confusion Matrix*, *Classification Report* (Precision, Recall, F1-Score), dan grafik kurva akurasi disimpan di [../06-output/](../06-output/).