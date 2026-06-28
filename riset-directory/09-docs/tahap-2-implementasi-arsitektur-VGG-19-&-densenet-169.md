# Tahap 2 — Implementasi Arsitektur VGG-19 & DenseNet-169
**Status:** Selesai
**Acuan arsitektur:** [tahap-1-dataset-dan-preprocessing.md](tahap-1-dataset-dan-preprocessing.md)
**Lokasi kode:** [../05-kode](../05-kode)

---

## Tujuan

Mengimplementasikan dua arsitektur Convolutional Neural Network (CNN) berbasis transfer learning untuk mengklasifikasikan citra penyakit daun padi, dengan membandingkan efektivitas VGG-19 (arsitektur sekuensial) dan DenseNet-169 (arsitektur koneksi padat).

## Deliverable

1. [x] Model Builder: Skrip build_models.py yang memuat bobot pre-trained ImageNet untuk VGG-19 dan DenseNet-169.
2. [x] Custom Head: Modifikasi fully connected layer (top layer) agar sesuai dengan jumlah kelas penyakit padi, termasuk penambahan Global Average Pooling dan Dropout (0.5) untuk regularisasi.
3. [x] Training Configuration: Pengaturan hyperparameters (Learning Rate: 1e-4, Optimizer: Adam, Loss: Categorical Cross-Entropy, Batch Size: 32).
4. [x] Callback System: Implementasi Early Stopping (patience=5) dan Model Checkpoint untuk menyimpan bobot terbaik (best weights) pada setiap run.
5. [x] Environment Control: Skrip environment.yml / requirements.txt untuk menjamin konsistensi versi library (TensorFlow 2.x, NumPy, Matplotlib) di semua run.
6. [x] Experiment Runner: Skrip train.py yang menerima argumen --model_name dan --seed untuk memastikan keterulangan (reproducibility) eksperimen.

## Hasil Verifikasi Model

Diverifikasi melalui proses debugging dan dry-run pelatihan:
- Kompilasi Model: Kedua model berhasil dimuat dan dipetakan dengan input shape (64, 64, 3).
- Integrasi Callback: Checkpoint berhasil menyimpan model dengan akurasi validasi tertinggi tanpa overfitting yang ekstrem.
- Validasi GPU/CPU: Konfigurasi device terdeteksi dengan benar; skrip mampu melakukan switching antara akselerasi GPU dan CPU secara otomatis.
- Debug sanity check: Melakukan training selama 1 epoch untuk memastikan tidak ada mismatch dimensi pada lapisan transisi Dense Blocks (DenseNet) maupun Flatten/Dense (VGG-19).

## Catatan Lingkungan

- Resource Allocation: DenseNet-169 memerlukan VRAM lebih besar saat pelatihan dibandingkan VGG-19 karena mekanisme skip-connections yang menyimpan fitur intermediate; alokasi memori diatur via tf.config.experimental.set_memory_growth.
- Pre-trained Weights: Bobot ImageNet diunduh dari server pusat TensorFlow dan disimpan secara lokal di ~/.keras/models/ untuk menghindari kegagalan download saat menjalankan eksperimen secara offline atau di cluster penelitian.
- Stabilitas: Meskipun arsitektur sudah fixed, stochasticity dari inisialisasi bobot pada dense layer terakhir menjadi alasan utama diperlukannya iterasi (35x run) pada tahap selanjutnya.
