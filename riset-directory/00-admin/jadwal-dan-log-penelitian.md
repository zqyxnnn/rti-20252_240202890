# Jadwal & Log Pelaksanaan Penelitian

Catatan kronologis pelaksanaan tiap tahap (sumber: riwayat commit git & dokumen `worksheets/ws-*.md`). Tanggal mengikuti `git log`.

## Log Pelaksanaan

| Tanggal | Tahap | Aktivitas | Referensi |
|---|---|---|---|
| 2026-06-23 | WS-09 | Perancangan arsitektur pipeline eksperimen, penyusunan konfigurasi hyperparameter (`config.json`), dan penentuan seed pool dasar untuk replikasi data daun padi | commit `c161a2f` ("ws-09 selesai") |
| 2026-06-23 | WS-10 | Implementasi skrip otomatisasi training loop PyTorch di Google Colab; eksekusi matrix penuh 70 runs (35 runs VGG-19 vs 35 runs DenseNet-169); pencatatan log akurasi data mentah lengkap | commit `f38361f` ("ws-10 selesai") |
| 2026-06-23 | WS-11 | Validasi integritas data menggunakan metode Interquartile Range (IQR); pembuktian 0 outlier pada sebaran data, penyusunan laporan validasi formal, dan refleksi ilmiah | commit `d6bcac8` ("ws-11 selesai") |

## Status Ringkas

- **WS-09 (Experiment Design)**: Selesai (Desain pipeline terkunci via commit `c161a2f`).
- **WS-10 (Execution Data)**: Selesai (Dataset mentah 35 runs terisi lengkap dan jujur via commit `f38361f`).
- **WS-11 (Data Validation)**: Selesai (Kalkulasi IQR membuktikan data valid, homogen, dan siap uji statistik inferensial via commit `d6bcac8`).

## Item Tindak Lanjut (Checklist Sebelum UTS Selesai)

- [x] Sinkronisasi nilai rata-rata akurasi VGG-19 (80.82%) dan DenseNet-169 (88.78%) di semua dokumen
- [x] Pengisian tabel data mentah 35 baris secara utuh di WS-10
- [x] Perhitungan batas atas dan batas bawah IQR secara formal di WS-11
- [x] Sinkronisasi referensi log administrasi dengan hash commit Git riil
- [ ] Pastikan seluruh worksheet lolos verifikasi sinkronisasi Git tanpa ada file yang tertinggal

## Korespondensi

*(belum ada — tambahkan catatan korespondensi dengan asisten laboratorium atau dosen pembimbing di sini saat tersedia)*