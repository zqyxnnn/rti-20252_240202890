# WS-12: Result Presentation & Visualization

> **Bab 12 — Penyajian Hasil & Visualisasi**

---

## Ringkasan Materi

### Data → Insight Model

```
Validated Data → Structured Presentation → Visualization → Pattern Recognition → Insight
```

Penyajian **mendahului** analisis. Tabel dan grafik membantu peneliti "melihat" data sebelum menghitung. Langsung ke uji statistik tanpa visualisasi berisiko kesimpulan yang secara teknis benar tapi kontekstual salah (Anscombe's Quartet, 1973).

### Tabel = Presisi, Grafik = Pola

Keduanya **saling melengkapi**:
- Tabel: angka presisi, self-contained (dipahami tanpa teks), sortable
- Grafik: pola visual, tren, perbandingan cepat

### Jenis Grafik Berdasarkan Tujuan

| Tujuan | Jenis Grafik |
|--------|-------------|
| Perbandingan antar-skenario | Bar chart (grouped/stacked) |
| Distribusi per-skenario | Box plot / violin plot |
| Tren temporal | Line chart |
| Korelasi dua variabel | Scatter plot |
| Proporsi (total = 100%) | Pie chart (hati-hati!) |

### Contoh Tabel Hasil yang Baik

| Model | Accuracy (%) | F1-Score (%) | Training Time (min) |
|-------|-------------|-------------|---------------------|
| BERT | 88.4 ± 1.2 | 87.1 ± 1.4 | 45.2 ± 3.1 |
| LSTM | 86.1 ± 1.8 | 84.5 ± 2.0 | 12.8 ± 1.2 |
| SVM | 82.3 ± 0.9 | 80.7 ± 1.1 | 0.3 ± 0.1 |

*N=10 per model. Mean ± std. Diurutkan berdasarkan Accuracy.*

### Visualization Bias — Yang Harus Dihindari

| Bias | Deskripsi | Dampak |
|------|----------|--------|
| Truncated axis | Y tidak dari 0 | Memperbesar perbedaan kecil |
| Inconsistent scale | Dua grafik skala beda | Perbandingan menyesatkan |
| Cherry-picked data | Hanya tampilkan yang "menang" | Selektif, tidak jujur |
| 3D effects | Efek 3D tanpa dimensi data ke-3 | Distorsi tanpa informasi |
| Missing error bar | Tidak ada variabilitas | Menyembunyikan ketidakpastian |

### Engineering vs Research Presentation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan grafik | Dashboard monitoring | Mendukung argumen ilmiah |
| Informasi wajib | KPI, threshold | Mean, std, CI, N, p-value |
| Bias handling | Less critical | Wajib dihindari (peer-review) |

---

## Template A.12 — Result Presentation Plan

RESULT PRESENTATION PLAN

Research Question : pakah DenseNet-169 memberikan performa klasifikasi penyakit daun padi yang lebih stabil dan akurat dibandingkan VGG-19 pada dataset terbatas?
Metrik Utama      : Akurasi (%) dan F1-Score (%)

Tabel Hasil:
| Skenario | Metrik 1 (mean ± std) | Metrik 2 (mean ± std) | n |
|----------|----------------------|----------------------|---|
| DenseNet-169 | 88.78 ± 1.60 | 88.15 ± 1.75 | 35 |
| VGG-19 | 80.82 ± 1.79 | 79.92 ± 1.85 | 35 |

Visualisasi yang Direncanakan:
| # | Jenis Grafik | Pesan Utama | Metrik |
|---|-------------|-------------|--------|
| 1 | Bar Chart + Error Bar | Menunjukkan keunggulan performa DenseNet-169 yang signifikan dibanding VGG-19. | Mean Akurasi ± SD |
| 2 | Box Plot | Membandingkan distribusi dan konsistensi (rentang nilai) antar model. | Akurasi (semua run) |
| 3 | Scatter Plot | Memetakan stabilitas performa (stdev) terhadap rata-rata. | Akurasi vs Stdev |

Bias Check:
  [x] Y-axis mulai dari 0 (atau dijustifikasi)
  [x] Error bar/CI ditampilkan
  [x] Semua data disertakan (tidak cherry-picked)
  [x] Tidak menggunakan 3D tanpa alasan

---

## Latihan 1 — Tabel Hasil

Buat tabel hasil eksperimen Anda (boleh dengan data simulasi jika belum punya data riil).

| Skenario | Metrik 1 (mean ± std) | Metrik 2 (mean ± std) | n |
|----------|----------------------|----------------------|---|
| DenseNet-169 | 88.78 ± 1.60 | 88.15 ± 1.75 | 35 |
| VGG-19 | 80.82 ± 1.79 | 79.92 ± 1.85 | 35 |

**Checklist tabel:**
- [x] Self-contained (judul jelas, satuan ada, N tercantum)
- [x] Mean ± std (bukan single number)
- [x] Diurutkan berdasarkan metrik utama
- [x] Format konsisten di semua baris

---

## Latihan 2 — Rencana Visualisasi

Rencanakan 2-3 grafik untuk menyajikan data dari Latihan 1. Setiap grafik = satu pesan.

| # | Jenis Grafik | Pesan | Data yang Digunakan |
|---|-------------|-------|---------------------|
| 1 | Bar chart + error bar | Menunjukkan keunggulan performa DenseNet-169 secara signifikan dibandingkan VGG-19. | Mean accuracy ± SD |
| 2 | Box plot | Memvisualisasikan konsistensi dan sebaran data (stabilitas) model di antara 35 kali pengulangan. | Seluruh data Akurasi 35 run |
| 3 | Scatter plot | Memetakan hubungan antara rata-rata akurasi dengan variabilitas (stdev) untuk mengukur kestabilan model. | Mean Akurasi vs Stdev Akurasi |

---

## Latihan 3 — Bias Detection

Evaluasi visualisasi berikut untuk bias (skenario dari contoh):

**Skenario:** Metode A = 91.2%, Metode B = 90.8%. Bar chart dengan Y-axis mulai dari 90%.

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah Y-axis menyesatkan? | Tidak. Sumbu Y pada Bar Chart akan dimulai dari 0 agar perbedaan 8% (80.82% ke 88.78%) terlihat proporsional dan tidak berlebihan. |
| Apakah error bar ditampilkan? | Ya. Error bar akan disertakan pada Bar Chart untuk menunjukkan standar deviasi (± 1.60 dan ± 1.79), memberikan konteks ketidakpastian. |
| Apakah semua kondisi ditampilkan? | Ya. Seluruh 35 run untuk kedua skenario disertakan dalam Box Plot tanpa ada data yang disembunyikan (no cherry-picking). |
| Apa solusinya? | Tidak ada tindakan perbaikan. Desain rencana visualisasi sudah memenuhi kaidah integritas ilmiah. |

**Evaluasi grafik Anda sendiri dari Latihan 2:**
- [x] Semua bias check lulus
- [ ] Ada yang perlu diperbaiki: ____

---

## Refleksi

> Mengapa tabel dan grafik keduanya diperlukan — tidak cukup salah satu saja? Pernahkah Anda membuat grafik yang (tanpa sengaja) menyesatkan?

> Tabel dan grafik memiliki fungsi kognitif yang berbeda namun saling melengkapi dalam riset. Tabel diperlukan untuk menyajikan presisi angka yang akurat, sehingga pembaca dapat melihat nilai eksak dari performa model tanpa ambiguitas. Di sisi lain, grafik diperlukan untuk memberikan pengenalan pola (pattern recognition) secara instan; grafik memudahkan peneliti dan audiens untuk melihat tren, fluktuasi, atau perbandingan antar-model yang mungkin sulit terdeteksi hanya dengan melihat deretan angka pada tabel. Dalam riset ilmiah, keduanya harus digunakan bersamaan agar argumen yang dibangun memiliki bukti yang transparan (tabel) sekaligus mudah dipahami secara visual (grafik).
> Ya, sebelumnya saya pernah membuat grafik yang tidak menyertakan error bar atau menggunakan skala sumbu Y yang terpotong untuk menonjolkan perbedaan performa yang sebenarnya kecil. Tanpa disadari, tindakan tersebut membuat perbedaan yang tidak signifikan secara statistik tampak terlihat sangat dramatis, yang secara etika riset dapat menyesatkan pembaca. Pengalaman ini menjadi pengingat bagi saya bahwa dalam riset, objektivitas visual harus diutamakan di atas estetika, dan setiap visualisasi harus disertai dengan standar deviasi atau interval kepercayaan untuk menunjukkan ketidakpastian data.
