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

Jumlah runs per skenario : 5 repeated runs
Total runs               : 10 total runs

DATA LOG (per run):
  Run ID    : RUN-006-DENSE169-S42
  Timestamp : 2026-05-20T21:15:30Z
  Skenario  : Intervensi (DenseNet-169) dengan Pretrained Weights pada Dataset Terbatas (710 Citra)
  Input     : 710 citra daun padi (resolusi 64x64 px), dipecah acak (Seed 42) menjadi 80% Train, 20% Test
  Output    : Accuracy: 0.8924, F1-Score: 0.8871, Loss: 0.1245
  Anomali   : Tidak ditemukan (GPU VRAM stabil pada pemakaian 4.2 GB)
  Catatan   : Konvergensasi gradien tercapai lebih cepat pada epoch ke-22 dibanding model VGG-19.
```

---

## Latihan 1 — Execution Plan

Susun execution plan untuk eksperimen Anda. Tentukan skenario, jumlah run, dan seed sebelum eksekusi.

| Run # | Skenario | Seed | Parameter Kunci | Status |
|-------|----------|------|----------------|--------|
| 1 | Skenario A: Baseline VGG-19 | 42 | Image=64x64, Adam, LR=1e-4, Epoch=30 | Planned |
| 2 | Skenario A: Baseline VGG-19 | 101 | Image=64x64, Adam, LR=1e-4, Epoch=30 | Planned |
| 3 | Skenario A: Baseline VGG-19 | 2023 | Image=64x64, Adam, LR=1e-4, Epoch=30 | Planned |
| 4 | Skenario B: Intervensi DenseNet-169 | 42 | Image=64x64, Adam, LR=1e-4, Epoch=30 | Planned |
| 5 | Skenario B: Intervensi DenseNet-169 | 101 | Image=64x64, Adam, LR=1e-4, Epoch=30 | Planned |

**Total skenario:** 2 (VGG-19 vs DenseNet-169)
**Run per skenario:** 5 kali pengulangan independen
**Total run keseluruhan:** 10 run

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
| Final Test Accuracy | float | 0.0 – 1.0 |
| Final Test F1-Score | float | 0.0 – 1.0 |
| Execution Duration (Seconds) | float | > 0.0 |

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
> Melalui implementasi multiple runs (5 kali pengulangan independen dengan seed acak yang telah ditentukan), saya dapat menghitung nilai rata-rata (mean) dan simpangan baku (standard deviation). Cara ini akan mengubah kepercayaan hasil riset secara total, karena kesimpulan akhir didasarkan pada distribusi data yang stabil secara ilmiah, sehingga hasil eksperimen komparatif terhindar dari bias subjektivitas dan manipulasi data semu.
