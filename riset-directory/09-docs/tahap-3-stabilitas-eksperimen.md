# Tahap 3 — Otomasi Eksperimen 35x Run

**Status:** Selesai — matrix 35 run (per arsitektur) telah dijalankan, data tersimpan di ../06-output/ (arsip eksperimen awal 10-run telah dipindahkan ke ../06-output/_archive/).
Bergantung pada: tahap-2-arsitektur-dan-training.md
**Bergantung pada:** [tahap-2-implementasi-gateway.md](tahap-2-implementasi-gateway.md)
**Lokasi kode:** [../05-kode/analysis/](../05-kode/analysis/)

---

## Tujuan

Menjalankan otomasi eksperimen untuk membandingkan performa akurasi VGG-19 dan DenseNet-169 dalam klasifikasi penyakit daun padi. Pengujian dilakukan melalui iterasi (run) sebanyak 35 kali per arsitektur dengan variasi random seed untuk memastikan reliabilitas statistik dan memitigasi stochastic fluke.

## Deliverable

- [x] Runner Script: run_stability_test.py yang mengotomatisasi inisialisasi model dan training loop.
- [x] Random Seed Generator: Modul pengatur seed dinamis (43 s.d. 77) untuk setiap iterasi.
- [x] Logging System: Skrip untuk mencatat setiap hasil akurasi, loss, dan durasi pelatihan ke dalam format CSV.
- [x] Resource Monitor: Skrip monitor_gpu_usage.sh untuk memantau penggunaan VRAM selama proses pelatihan.
- [x] Data Aggregator: Script untuk menggabungkan hasil dari 70 total eksperimen (35 VGG + 35 DenseNet) menjadi satu matriks perbandingan.

## Desain Eksperimen

### Struktur kode (05-kode/)

```
05-kode/
├──analysis
├  └── run_analysis.py
├── hyperparams_config.json
├── klassifikasi_daun_padi.ipynb
├── README.md    
└── run_stability_test.py 

1. Untuk setiap kombinasi <arsitektur> dan <seed>:
2. Mengatur Environment (Reset TensorFlow backend untuk membersihkan memori GPU).
3. Memuat arsitektur model sesuai argumen model_name.
4. Menjalankan Training selama 20 epoch dengan EarlyStopping.
5. Mengambil metrik akurasi validasi final dan menyimpannya ke ../06-output/tables/
6. Menghapus bobot model sementara untuk menghemat ruang disk (kecuali best weights).

```

## Hasil Eksperimen

Matrix 35 run dijalankan per arsitektur (Total 70 run). Eksperimen dilakukan untuk membandingkan stabilitas model terhadap inisialisasi bobot awal yang berbeda.

| Arsitektur | Jumlah Run | Status |
|---|---|---|
|   vgg-19 | 35 | Selesai |
|   DenseNet-169 | 35 | Selesai |

Output: ../06-output/tables/ , total ukuran seluruh data eksperimen ~2.8 MB, mencakup log pelatihan lengkap untuk kebutuhan audit dan reproducibility.

## Catatan Lingkungan

- Otomatisasi: Eksperimen dijalankan secara terotomatisasi sebanyak 35 kali per arsitektur menggunakan seed acak dinamis (43 s.d. 77) untuk menjamin reliabilitas statistik. Seluruh metrik, visualisasi plot, dan model biner disimpan secara terstruktur di folder ../06-output/.
