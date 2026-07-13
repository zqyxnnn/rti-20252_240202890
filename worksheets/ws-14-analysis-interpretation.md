# WS-14: Analysis, Interpretation & Failure Analysis

> **Bab 14 — Analisis Data, Interpretasi & Failure Analysis**

---

## Ringkasan Materi

### Data → Knowledge Model

```
Data → Analysis → Interpretation → Explanation → Knowledge
```

Tiga level yang berbeda:
- **Analysis** — "Apa yang terjadi?" (deskriptif + inferensial)
- **Interpretation** — "Apa artinya?" (konteks RQ + literatur)
- **Failure Analysis** — "Mengapa tidak berhasil?" (boundary conditions)

### Beyond p-value

**Statistical significance ≠ practical significance.** Selalu laporkan:
1. p-value (signifikansi statistik)
2. Effect size (besarnya efek)
3. Confidence interval (rentang ketidakpastian)

| Effect Size (Cohen's d) | Interpretasi |
|-------------------------|-------------|
| < 0.2 | Small |
| 0.2 – 0.8 | Medium |
| > 0.8 | Large |

### Pemilihan Uji Statistik

| Kondisi | Uji yang Tepat |
|---------|---------------|
| 2 grup, normal, paired | Paired t-test |
| 2 grup, non-normal | Wilcoxon signed-rank |
| > 2 grup, normal | One-way ANOVA + post-hoc |
| > 2 grup, non-normal | Kruskal-Wallis + post-hoc |
| 2 variabel kontinu | Pearson (normal) / Spearman (rank) |

### Failure Analysis as Contribution

Hipotesis yang ditolak adalah **temuan yang berharga**:

| Dataset | New (F1) | Baseline (F1) | p-value | Cohen's d |
|---------|---------|--------------|---------|-----------|
| DS-1 (small, clean) | 94.2±1.1 | 89.3±1.5 | <0.001 | **3.7** |
| DS-4 (medium, noisy) | 78.3±3.2 | 82.1±2.8 | 0.008 | **-1.3** |
| DS-5 (large, noisy) | 71.6±4.1 | 80.5±3.0 | <0.001 | **-2.5** |

**Insight:** Metode baru unggul di data bersih tapi gagal di data noisy → asumsi Gaussian dilanggar → **boundary condition** ditemukan → hybrid approach direkomendasikan.

**Partial failure + deep analysis = kontribusi lebih kaya daripada full success tanpa analisis.**

### Limitation Types

| Jenis | Contoh |
|-------|--------|
| Internal validity | Confounders yang tidak dikontrol |
| External validity | Generalisasi ke domain lain |
| Construct validity | Metrik mengukur apa yang dimaksud? |
| Statistical limitation | Sample size, asumsi distribusi |

### Jebakan Kognitif

1. "Signifikan statistik = penting secara praktis" → cek effect size
2. "Hipotesis tidak didukung → cari sudut baru" → p-hacking
3. "Kegagalan tidak perlu dilaporkan detail" → missed insight
4. "Limitasi cukup disebutkan, tidak perlu dianalisis" → kedalaman hilang

---

## Template A.14 — Analysis & Interpretation Report

```
ANALYSIS & INTERPRETATION

1. Statistik Deskriptif:
   | Skenario | Mean | Std | Median | Min | Max | n |
   |----------|------|-----|--------|-----|-----|---|
   | VGG-19 | 84.91 | 4.54 | 83.61 | 78.70 | 91.35 | 35 |
   | DenseNet-169 | 84.50 | 4.22 | 85.03 | 78.16 | 91.35 | 35 |

2. Uji Hipotesis:
   Uji yang digunakan  : Independent T-Test
   Justifikasi          : Eksperimen membandingkan rata-rata performa dari dua model (VGG-19 dan DenseNet-169) yang dijalankan pada kondisi yang setara. Uji ini dipilih untuk menentukan apakah perbedaan rata-rata akurasi antara kedua model tersebut signifikan secara statistik atau hanya karena variasi acak.
   Hasil: p = 0.7004, effect size (d/r/η²) = 0.3864
   CI 95%               : [-2.23, 3.05]

3. Keputusan:
   [ ] H₀ ditolak → H₁ diterima
   [x] H₀ tidak ditolak

4. Interpretasi:
   Hubungan ke RQ       : Hipotesis bahwa DenseNet-169 secara otomatis lebih unggul dari VGG-19 tidak terbukti pada dataset ini. Keduanya menunjukkan performa yang sangat kompetitif.
   Practical significance: Perbedaan rata-rata hanya ~0.4%. Secara praktis, pemilihan model mungkin lebih bergantung pada efisiensi training atau inference speed daripada akurasi.
   Perbandingan literatur: Hasil ini menarik karena DenseNet biasanya dianggap lebih superior, namun pada dataset ini performanya setara, menunjukkan bahwa untuk tugas klasifikasi daun padi ini, kompleksitas model mungkin sudah mencapai titik jenuh (saturation point).

5. Limitation:
   | Jenis | Ancaman | Dampak | Mitigasi |
   | :--- | :--- | :--- | :--- |
   | **Statistical** | *Sample size* terbatas (n=35) | *Power* uji statistik rendah | *Multiple runs* dengan *fixed seed* |
   | **Construct** | Metrik akurasi tunggal | Kurang detail per kelas | Analisis *F1-score* atau *Confusion Matrix* |
   | **Internal** | Variabilitas komputasi | *Noise* pada hasil *training* | Lingkungan eksekusi terkontrol |

6. Failure Analysis (jika H₀ tidak ditolak):
   Penyebab potensial  : Overfitting atau noise pada dataset citra yang membuat keunggulan arsitektur dense connection tidak tereksploitasi maksimal.
   Boundary condition   : Kemungkinan kedua arsitektur mencapai batas kemampuan fitur yang bisa diekstraksi dari resolusi citra yang digunakan.
   Insight              : Tidak ada pemenang tunggal. Rekomendasi riset selanjutnya bisa difokuskan pada hybrid model atau optimasi hyperparameter khusus untuk DenseNet agar bisa melampaui VGG.
```

---

## Latihan 1 — Pemilihan Uji Statistik

Tentukan uji statistik yang tepat untuk eksperimen Anda.

| Pertanyaan | Jawaban |
|-----------|---------|
| Berapa grup yang dibandingkan? | 2 (VGG-19 dan DenseNet-169) |
| Apakah data berpasangan (paired)? | Ya, diuji pada iterasi data yang sama |
| Apakah distribusi normal? (uji normalitas) | Ya, asumsi terpenuhi pada n=35 |
| **Uji yang dipilih:** | Paired t-test |
| **Justifikasi:** | MData bersifat kontinu, berpasangan, dan memenuhi asumsi normalitas untuk membandingkan rata-rata dua kelompok |

**Effect size yang akan dilaporkan:** [x] Cohen's d / [ ] Eta-squared / [ ] Lainnya: ____

---

## Latihan 2 — Interpretasi Hasil

Gunakan data berikut (atau data riil Anda) untuk berlatih interpretasi.

**Data:**
| Model | Accuracy (mean ± std) | n |
|-------|----------------------|---|
| A | 84.91 ± 4.54 | 35 |
| B | 84.50 ± 4.22 | 35 |

p = 0.7004, Cohen's d = 0.09, CI 95% = [-2.23, 3.05]

| Aspek | Interpretasi |
|-------|-------------|
| Signifikansi statistik | p = 0.7004 > 0.05 → Tidak ditemukan perbedaan signifikan secara statistik pada α = 0.05. |
| Effect size | d = 0.09 (Cohen's d) → Efek sangat kecil (negligible), selisih performa antar-model tidak berarti secara statistik. |
| Practical significance | Perbedaan rata-rata hanya 0.41%. Secara praktis, kedua model memberikan hasil yang setara untuk dataset ini. |
| Hubungan ke RQ | Hipotesis bahwa DenseNet-169 lebih unggul tidak terbukti; arsitektur yang lebih kompleks tidak memberikan nilai tambah di sini. |
| Perbandingan literatur | Hasil ini sejalan dengan studi saturation point, di mana pada dataset spesifik, arsitektur sederhana (VGG) bisa menandingi arsitektur kompleks (DenseNet). |

---

## Latihan 3 — Failure Analysis

Latih kemampuan failure analysis: hipotesis TIDAK didukung. Apa yang bisa dipelajari?

**Skenario:** Metode baru Anda mendapat F1 = 83.2%, baseline = 84.7%. p = 0.12 (tidak signifikan).

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah ini "gagal"? | Bukan kegagalan, melainkan negative result yang menjadi kontribusi empiris untuk memetakan batas efektivitas metode baru. |
| Kemungkinan penyebab? | Penambahan kompleksitas pada metode baru memberikan overhead komputasi tanpa adanya peningkatan ekstraksi fitur yang berarti pada dataset saat ini. |
| Boundary condition? | Metode baru tampaknya hanya menunjukkan keunggulan pada dataset skala besar (n > 10.000), sementara pada skala saat ini, baseline lebih efisien. |
| Insight yang bisa diambil? | Adanya trade-off antara kompleksitas arsitektur dan efisiensi; untuk dataset menengah, pendekatan yang lebih ringan lebih direkomendasikan. |
| Apakah layak dilaporkan? Mengapa? | Ya, pelaporan negative result dan boundary condition mencegah redundansi riset di masa depan dan memperkaya literatur domain. |

**Limitation terkait:**
| Jenis | Ancaman | Dampak |
|-------|---------|--------|
| Statistical | Sample size terbatas (hanya 10 runs) | Statistical power yang rendah untuk menangkap perbedaan kecil |
| Internal | Variabilitas pada initialization | Ketidakpastian dalam replikasi hasil pada seed yang berbeda |

---

## Refleksi

> Apakah "failure" dalam riset benar-benar gagal, atau justru kontribusi? Bagaimana failure analysis mengubah cara Anda melihat hasil negatif?

> Kegagalan dalam riset adalah bagian integral dari proses penemuan; hasil negatif yang dianalisis dengan failure analysis justru merupakan kontribusi yang jujur karena memberikan batasan yang jelas bagi komunitas riset. Kegagalan ini mengubah cara pandang saya dari "mencari hasil sukses" menjadi "mencari kebenaran objektif", di mana mengetahui mengapa sebuah metode tidak bekerja sama pentingnya dengan mengetahui kapan ia bekerja. Dengan melakukan analisis ini, saya dapat menghindari jebakan p-hacking dan lebih fokus pada pemahaman mendalam mengenai perilaku model dalam berbagai kondisi boundary.
