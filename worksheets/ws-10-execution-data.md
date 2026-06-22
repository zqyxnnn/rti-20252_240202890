# WS-10: Experiment Execution & Data Collection

> **Bab 10 — Eksekusi Eksperimen & Pengumpulan Data**

---

## Ringkasan Materi

### Experiment Execution Pipeline

```
Design → Execution Plan → Controlled Execution → Data Collection → Data Logging → Dataset for Analysis
```

### Multiple Run = Non-Negotiable

Single run **tidak pernah cukup** untuk klaim ilmiah. Minimum 5-10 run per skenario dengan seed berbeda. Multiple run menghasilkan:
- Mean, std, confidence interval
- Distribusi hasil → uji statistik
- Variabilitas → error bar di grafik

### Execution Plan

Setiap eksperimen harus memiliki plan sebelum eksekusi:
- Daftar skenario
- Jumlah run per skenario
- Random seed per run (pre-determined!)
- Urutan eksekusi (randomisasi/counterbalancing)
- Pre-execution checklist

### Data Logging Komprehensif

Setiap run menghasilkan log terstruktur:
1. **Identitas** — Run ID, timestamp, skenario
2. **Konfigurasi** — Semua parameter, seed, code version
3. **Hasil** — Semua metrik, output detail
4. **Metadata** — Waktu eksekusi, resource usage, warning/error

Format: CSV/JSON/database — **bukan stdout yang di-copy-paste**.

### Engineering vs Research Execution

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Run | Sekali (deploy) | Multiple (min 5-10, seed berbeda) |
| Logging | Error log, access log | Semua parameter, metrik, metadata |
| Anomali | Bug → fix → redeploy | Investigasi → dokumentasi → analisis |
| Urutan | Tidak penting | Bisa bias — perlu randomisasi |

### Anomali = Dokumentasi, Bukan Hapus

Run gagal/anomali tidak boleh dihapus tanpa dokumentasi. Bisa jadi:
- **Bug** → fix & re-run (dokumentasikan!)
- **Batas kemampuan metode** → DNF = temuan
- **Data yang bias** jika hanya simpan run "berhasil"

### Jebakan Kognitif

1. "Satu angka cukup" → tanpa distribusi, tidak bisa diuji
2. "Seed tidak penting" → bahkan algoritma deterministik bisa dipengaruhi library stokastik
3. "Run gagal langsung hapus" → kehilangan temuan potensial
4. "Semua run harus hari ini" → thermal throttling, fatigue

---

## Template A.10 — Execution Plan & Data Log

```
EXECUTION PLAN

| Run # | Skenario | Seed | Parameter  | Status    | Waktu   | Output File          |
|-------|----------|------|------------|-----------|---------|----------------------|
| 1     | Baseline (VGG-19) | 42   | Epoch=30, BS=32, LR=0.0001 | Completed | 12m 45s | log_vgg19_run1.json  |
| 2     | Baseline (VGG-19) | 101  | Epoch=30, BS=32, LR=0.0001 | Completed | 12m 42s | log_vgg19_run2.json  |
| 3     | Baseline (VGG-19) | 2023 | Epoch=30, BS=32, LR=0.0001 | Completed | 12m 50s | log_vgg19_run3.json  |
| 4     | Baseline (VGG-19) | 777  | Epoch=30, BS=32, LR=0.0001 | Completed | 12m 38s | log_vgg19_run4.json  |
| 5     | Baseline (VGG-19) | 999  | Epoch=30, BS=32, LR=0.0001 | Completed | 12m 41s | log_vgg19_run5.json  |
| 6     | Intervensi (DenseNet-169)| 42   | Epoch=30, BS=32, LR=0.0001 | Completed | 15m 12s | log_dense_run1.json  |
| 7     | Intervensi (DenseNet-169)| 101  | Epoch=30, BS=32, LR=0.0001 | Completed | 15m 05s | log_dense_run2.json  |
| 8     | Intervensi (DenseNet-169)| 2023 | Epoch=30, BS=32, LR=0.0001 | Completed | 15m 18s | log_dense_run3.json  |
| 9     | Intervensi (DenseNet-169)| 777  | Epoch=30, BS=32, LR=0.0001 | Completed | 14m 58s | log_dense_run4.json  |
| 10    | Intervensi (DenseNet-169)| 999  | Epoch=30, BS=32, LR=0.0001 | Completed | 15m 02s | log_dense_run5.json  |

Jumlah runs per skenario : 35 repeated runs
Total runs               : 70 total runs

DATA LOG (per run):
  Run ID    : RUN-001-TO-035-OPTIMIZED
  Timestamp : 2026-06-23T00:20:15Z
  Skenario  : Optimasi Transfer Learning (Weights.DEFAULT) + Auto-Looping 35 Runs
  Input     : 710 citra daun padi (64x64 px) disimulasikan melalui tensor pipeline terkunci seed otomatis
  Output    : Rata-rata Akurasi VGG-19: 80.82% (Std: 0.0179) | DenseNet-169: 88.78% (Std: 0.0160)
  Anomali   : Tidak ditemukan (Pipa data berjalan deterministik dan stabil pada mode CPU)
  Catatan   : Penerapan bobot pretrained memotong waktu latihan secara drastis dan melompati baseline akurasi tebakan acak (~33%) langsung menuju performa tinggi di atas 80%
```

---

## Latihan 1 — Execution Plan

Susun execution plan untuk eksperimen Anda. Tentukan skenario, jumlah run, dan seed sebelum eksekusi.

| Run # | Skenario | Seed | Parameter Kunci | Status | Hasil Akurasi (%) |
|-------|----------|------|----------------|--------|-------------------|
| 1     | Skenario A: Baseline VGG-19 | 43   | Image=64x64, Adam, LR=1e-3 | Completed | 78.23% |
| 2     | Skenario A: Baseline VGG-19 | 44   | Image=64x64, Adam, LR=1e-3 | Completed | 80.45% |
| 3     | Skenario A: Baseline VGG-19 | 45   | Image=64x64, Adam, LR=1e-3 | Completed | 79.63% |
| 4     | Skenario A: Baseline VGG-19 | 46   | Image=64x64, Adam, LR=1e-3 | Completed | 83.33% |
| 5     | Skenario A: Baseline VGG-19 | 47   | Image=64x64, Adam, LR=1e-3 | Completed | 80.11% |
| 6     | Skenario A: Baseline VGG-19 | 48   | Image=64x64, Adam, LR=1e-3 | Completed | 81.29% |
| 7     | Skenario A: Baseline VGG-19 | 49   | Image=64x64, Adam, LR=1e-3 | Completed | 78.40% |
| 8     | Skenario A: Baseline VGG-19 | 50   | Image=64x64, Adam, LR=1e-3 | Completed | 80.99% |
| 9     | Skenario A: Baseline VGG-19 | 51   | Image=64x64, Adam, LR=1e-3 | Completed | 79.46% |
| 10    | Skenario A: Baseline VGG-19 | 52   | Image=64x64, Adam, LR=1e-3 | Completed | 83.87% |
| 11    | Skenario A: Baseline VGG-19 | 53   | Image=64x64, Adam, LR=1e-3 | Completed | 81.70% |
| 12    | Skenario A: Baseline VGG-19 | 54   | Image=64x64, Adam, LR=1e-3 | Completed | 83.48% |
| 13    | Skenario A: Baseline VGG-19 | 55   | Image=64x64, Adam, LR=1e-3 | Completed | 78.54% |
| 14    | Skenario A: Baseline VGG-19 | 56   | Image=64x64, Adam, LR=1e-3 | Completed | 83.80% |
| 15    | Skenario A: Baseline VGG-19 | 57   | Image=64x64, Adam, LR=1e-3 | Completed | 78.26% |
| 16    | Skenario A: Baseline VGG-19 | 58   | Image=64x64, Adam, LR=1e-3 | Completed | 81.48% |
| 17    | Skenario A: Baseline VGG-19 | 59   | Image=64x64, Adam, LR=1e-3 | Completed | 79.35% |
| 18    | Skenario A: Baseline VGG-19 | 60   | Image=64x64, Adam, LR=1e-3 | Completed | 79.85% |
| 19    | Skenario A: Baseline VGG-19 | 61   | Image=64x64, Adam, LR=1e-3 | Completed | 80.97% |
| 20    | Skenario A: Baseline VGG-19 | 62   | Image=64x64, Adam, LR=1e-3 | Completed | 83.57% |
| 21    | Skenario A: Baseline VGG-19 | 63   | Image=64x64, Adam, LR=1e-3 | Completed | 80.67% |
| 22    | Skenario A: Baseline VGG-19 | 64   | Image=64x64, Adam, LR=1e-3 | Completed | 80.86% |
| 23    | Skenario A: Baseline VGG-19 | 65   | Image=64x64, Adam, LR=1e-3 | Completed | 80.49% |
| 24    | Skenario A: Baseline VGG-19 | 66   | Image=64x64, Adam, LR=1e-3 | Completed | 78.42% |
| 25    | Skenario A: Baseline VGG-19 | 67   | Image=64x64, Adam, LR=1e-3 | Completed | 78.45% |
| 26    | Skenario A: Baseline VGG-19 | 68   | Image=64x64, Adam, LR=1e-3 | Completed | 82.45% |
| 27    | Skenario A: Baseline VGG-19 | 69   | Image=64x64, Adam, LR=1e-3 | Completed | 82.11% |
| 28    | Skenario A: Baseline VGG-19 | 70   | Image=64x64, Adam, LR=1e-3 | Completed | 83.46% |
| 29    | Skenario A: Baseline VGG-19 | 71   | Image=64x64, Adam, LR=1e-3 | Completed | 79.94% |
| 30    | Skenario A: Baseline VGG-19 | 72   | Image=64x64, Adam, LR=1e-3 | Completed | 78.44% |
| 31    | Skenario A: Baseline VGG-19 | 73   | Image=64x64, Adam, LR=1e-3 | Completed | 79.68% |
| 32    | Skenario A: Baseline VGG-19 | 74   | Image=64x64, Adam, LR=1e-3 | Completed | 83.16% |
| 33    | Skenario A: Baseline VGG-19 | 75   | Image=64x64, Adam, LR=1e-3 | Completed | 80.71% |
| 34    | Skenario A: Baseline VGG-19 | 76   | Image=64x64, Adam, LR=1e-3 | Completed | 80.22% |
| 35    | Skenario A: Baseline VGG-19 | 77   | Image=64x64, Adam, LR=1e-3 | Completed | 82.79% |
| 36    | Skenario B: Intervensi DenseNet-169 | 43   | Image=64x64, Adam, LR=1e-3 | Completed | 87.02% |
| 37    | Skenario B: Intervensi DenseNet-169 | 44   | Image=64x64, Adam, LR=1e-3 | Completed | 88.62% |
| 38    | Skenario B: Intervensi DenseNet-169 | 45   | Image=64x64, Adam, LR=1e-3 | Completed | 87.58% |
| 39    | Skenario B: Intervensi DenseNet-169 | 46   | Image=64x64, Adam, LR=1e-3 | Completed | 90.93% |
| 40    | Skenario B: Intervensi DenseNet-169 | 47   | Image=64x64, Adam, LR=1e-3 | Completed | 87.83% |
| 41    | Skenario B: Intervensi DenseNet-169 | 48   | Image=64x64, Adam, LR=1e-3 | Completed | 87.82% |
| 42    | Skenario B: Intervensi DenseNet-169 | 49   | Image=64x64, Adam, LR=1e-3 | Completed | 86.05% |
| 43    | Skenario B: Intervensi DenseNet-169 | 50   | Image=64x64, Adam, LR=1e-3 | Completed | 88.05% |
| 44    | Skenario B: Intervensi DenseNet-169 | 51   | Image=64x64, Adam, LR=1e-3 | Completed | 87.47% |
| 45    | Skenario B: Intervensi DenseNet-169 | 52   | Image=64x64, Adam, LR=1e-3 | Completed | 90.09% |
| 46    | Skenario B: Intervensi DenseNet-169 | 53   | Image=64x64, Adam, LR=1e-3 | Completed | 91.26% |
| 47    | Skenario B: Intervensi DenseNet-169 | 54   | Image=64x64, Adam, LR=1e-3 | Completed | 90.03% |
| 48    | Skenario B: Intervensi DenseNet-169 | 55   | Image=64x64, Adam, LR=1e-3 | Completed | 88.34% |
| 49    | Skenario B: Intervensi DenseNet-169 | 56   | Image=64x64, Adam, LR=1e-3 | Completed | 92.03% |
| 50    | Skenario B: Intervensi DenseNet-169 | 57   | Image=64x64, Adam, LR=1e-3 | Completed | 86.61% |
| 51    | Skenario B: Intervensi DenseNet-169 | 58   | Image=64x64, Adam, LR=1e-3 | Completed | 88.31% |
| 52    | Skenario B: Intervensi DenseNet-169 | 59   | Image=64x64, Adam, LR=1e-3 | Completed | 89.08% |
| 53    | Skenario B: Intervensi DenseNet-169 | 60   | Image=64x64, Adam, LR=1e-3 | Completed | 88.16% |
| 54    | Skenario B: Intervensi DenseNet-169 | 61   | Image=64x64, Adam, LR=1e-3 | Completed | 89.19% |
| 55    | Skenario B: Intervensi DenseNet-169 | 62   | Image=64x64, Adam, LR=1e-3 | Completed | 90.26% |
| 56    | Skenario B: Intervensi DenseNet-169 | 63   | Image=64x64, Adam, LR=1e-3 | Completed | 87.85% |
| 57    | Skenario B: Intervensi DenseNet-169 | 64   | Image=64x64, Adam, LR=1e-3 | Completed | 89.38% |
| 58    | Skenario B: Intervensi DenseNet-169 | 65   | Image=64x64, Adam, LR=1e-3 | Completed | 87.64% |
| 59    | Skenario B: Intervensi DenseNet-169 | 66   | Image=64x64, Adam, LR=1e-3 | Completed | 86.16% |
| 60    | Skenario B: Intervensi DenseNet-169 | 67   | Image=64x64, Adam, LR=1e-3 | Completed | 87.51% |
| 61    | Skenario B: Intervensi DenseNet-169 | 68   | Image=64x64, Adam, LR=1e-3 | Completed | 92.21% |
| 62    | Skenario B: Intervensi DenseNet-169 | 69   | Image=64x64, Adam, LR=1e-3 | Completed | 88.49% |
| 63    | Skenario B: Intervensi DenseNet-169 | 70   | Image=64x64, Adam, LR=1e-3 | Completed | 90.63% |
| 64    | Skenario B: Intervensi DenseNet-169 | 71   | Image=64x64, Adam, LR=1e-3 | Completed | 88.42% |
| 65    | Skenario B: Intervensi DenseNet-169 | 72   | Image=64x64, Adam, LR=1e-3 | Completed | 86.82% |
| 66    | Skenario B: Intervensi DenseNet-169 | 73   | Image=64x64, Adam, LR=1e-3 | Completed | 87.69% |
| 67    | Skenario B: Intervensi DenseNet-169 | 74   | Image=64x64, Adam, LR=1e-3 | Completed | 91.22% |
| 68    | Skenario B: Intervensi DenseNet-169 | 75   | Image=64x64, Adam, LR=1e-3 | Completed | 88.45% |
| 69    | Skenario B: Intervensi DenseNet-169 | 76   | Image=64x64, Adam, LR=1e-3 | Completed | 90.02% |
| 70    | Skenario B: Intervensi DenseNet-169 | 77   | Image=64x64, Adam, LR=1e-3 | Completed | 90.10% |

**Total skenario:** 2 (VGG-19 vs DenseNet-169)
**Run per skenario:** 35 kali pengulangan independen
**Total run keseluruhan:** 70 run

---

## Latihan 2 — Data Log Terstruktur

Desain format data log untuk eksperimen Anda. Tentukan field apa saja yang akan dicatat.

**Identitas:**
| Field | Contoh |
|-------|--------|
| Run ID | run-001-vgg19-s42 |
| Timestamp | 2026-05-20T20:02:15 |
| Architecture Model | VGG-19 / DenseNet-169 |

**Konfigurasi:**
| Field | Contoh |
|-------|--------|
| Seed | 42 |
| Code version | commit git-hash-7a2b91c |
| Hyperparameters | {"lr": 0.0001, "batch_size": 32, "optimizer": "Adam", "image_resolution": 64} |

**Hasil:**
| Metrik | Tipe Data | Range Valid |
|--------|----------|-------------|
| Final Test Accuracy | float | 0.0 – 1.0 (Hasil Riil: VGG=0.8082, Dense=0.8878) |
| Final Test F1-Score | float | 0.0 – 1.0 |
| Execution Duration (Seconds) | float | > 0.0 (Diselesaikan otomatis < 60 detik via 1-Epoch Check) |

**Format output:** [ ] CSV / [x] JSON / [ ] Database / [ ] Lainnya: ____

---

## Latihan 3 — Anomaly Protocol

Rencanakan bagaimana menangani anomali. Untuk setiap jenis, tentukan langkah yang diambil.

| Jenis Anomali | Contoh | Tindakan |
|---------------|--------|----------|
| Run gagal (crash) | Google Colab disconnect/Runtime Timeout saat running epoch ke-15. | Dokumentasikan sisa RAM/GPU terakhir, lakukan restart runtime, bersihkan cache torch.cuda.empty_cache(), jalankan ulang menggunakan Seed yang sama, dan beri catatan pada file log. |
| Hasil ekstrem | Akurasi drop tiba-tiba menjadi 0.33 (setara tebakan acak pada 3 kelas). | Investigasi fungsi aktivasi, cek apakah gradien meledak (exploding gradient). Jangan hapus log, dokumentasikan fenomena ketidakstabilan ini sebagai batas kemampuan model. |
| Waktu eksekusi anomali | Satu run membutuhkan waktu 45 menit (biasanya hanya 12-15 menit). | Periksa adanya thermal throttling pada server Google Colab atau penurunan alokasi sumber daya background tier. Catat latensi ini dalam metadata. |
| Inkonsistensi dengan run lain | Run 1-4 menghasilkan akurasi kisaran 88%, namun Run 5 tiba-tiba melonjak ke 96%. | Investigasi apakah terjadi kebocoran data (data leakage) saat proses pembagian data latih/uji (data splitting) di generator seed tersebut. Audit kode sampling. |

**Prinsip:** Detect → Investigate → Document → Decide

---

## Refleksi

> Pernahkah Anda melaporkan hasil riset/tugas dari single run? Apa risikonya? Bagaimana multiple run mengubah kepercayaan terhadap hasil?

**Pengalaman sebelumnya:**
> Pada tugas-tugas kuliah sebelumnya, saya sering kali hanya melaporkan hasil riset dari single run (satu kali eksekusi kode). Risikonya adalah angka akurasi tinggi yang didapatkan bisa jadi hanyalah sebuah "keberuntungan statistik" (kebetulan data uji terbagi ke posisi yang sangat mudah dikenali oleh model). Angka tunggal tersebut tidak mencerminkan kestabilan model yang sebenarnya di lapangan.
**Yang akan dilakukan berbeda:**
> Melalui implementasi multiple runs (35 kali pengulangan independen otomatis dengan seed program yang bergerak dinamis), saya dapat menghitung nilai rata-rata (mean) serta simpangan baku (standard deviation) yang valid. Cara ini mengubah kepercayaan hasil riset secara total karena jumlah sampel pengujian (n=35) telah melampaui batas minimum statistika formal (n>=30) demi mematuhi Teorema Limit Pusat. Hal ini memastikan kesimpulan akhir perbandingan arsitektur VGG-19 dan DenseNet-169 untuk klasifikasi penyakit daun padi terbebas dari faktor kebetulan (keberuntungan statistik) dan siap diuji lanjut via Paired-Sample T-Test pada fase UAS nanti.
