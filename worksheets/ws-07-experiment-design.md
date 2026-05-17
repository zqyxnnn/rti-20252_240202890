# WS-07: Experimental Design & Validity

> **Bab 7 — Experimental Design & Validity**

---

## Ringkasan Materi

### Correlation ≠ Causality

Kausalitas membutuhkan 3 syarat:
1. **Covariance** — X dan Y bergerak bersama
2. **Temporal precedence** — X berubah sebelum Y
3. **Elimination of alternatives** — Tidak ada faktor lain yang menjelaskan Y

Controlled experiment adalah satu-satunya metode yang bisa membuktikan kausalitas.

### Empat Jenis Validitas

| Jenis | Pertanyaan | Ancaman Umum |
|-------|-----------|-------------|
| **Internal** | Apakah hubungan IV→DV nyata? | Confounding variable, selection bias |
| **External** | Apakah bisa digeneralisasi? | Dataset terlalu spesifik |
| **Construct** | Apakah mengukur konsep yang benar? | Metrik tidak sesuai |
| **Conclusion** | Apakah kesimpulan statistik valid? | Sample size kecil, uji salah |

Internal dan external validity sering berkonflik: semakin terkontrol (internal kuat) → semakin artificial (external lemah).

### Tiga Tipe Eksperimen dalam Riset TI

| Tipe | Deskripsi | Kapan Digunakan |
|------|----------|----------------|
| **Comparison Study** | Metode A vs B pada kondisi identik | Membandingkan pendekatan berbeda |
| **Ablation Study** | Full system → lepas komponen satu per satu | Mengukur kontribusi tiap komponen |
| **Parameter Study** | Variasikan satu parameter, amati dampak | Uji sensitifitas/robustness |

### Fairness dalam Perbandingan

Perbandingan yang adil = **kondisi identik** untuk semua metode: dataset sama, preprocessing sama, tuning effort sebanding, environment sama, metrik sama.

Contoh tidak adil: Transformer (30 fitur tambahan + Bayesian optimization) vs RF (default params) → hasilnya misleading.

### Threats to Validity = Diidentifikasi Sebelum Eksperimen

Ancaman validitas harus diidentifikasi **sebelum** eksperimen dan mitigasinya dirancang sebagai bagian dari desain — bukan ditulis sebagai boilerplate setelah selesai.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan testing | Memastikan sistem memenuhi requirement | Membuktikan hubungan kausal antar variabel |
| Baseline | Versi sebelumnya (last release) | Metode tervalidasi dari literatur |
| Kegagalan | Bug → fix → release | H₀ tidak ditolak → tetap kontribusi ilmiah |
| Sukses | 100% test pass | Evidence valid — mendukung atau menolak hipotesis |

### Istilah Penting

- **Causality** — Hubungan sebab-akibat (covariance + temporal + elimination)
- **Controlled Experiment** — Ubah satu variabel, kontrol sisanya, amati efek
- **Fairness** — Semua metode diuji pada kondisi yang benar-benar identik
- **Threats to Validity** — Faktor yang bisa melemahkan kesimpulan jika tidak dimitigasi
- **Conclusion Validity** — Validitas statistik: power, sample size, uji yang tepat

---

## Template A.7 — Desain Eksperimen Lengkap

```
EXPERIMENT DESIGN

Research Question : Apakah model CNN DenseNet-169 menghasilkan akurasi lebih tinggi dibandingkan VGG-19 pada klasifikasi penyakit daun padi menggunakan dataset citra daun padi?
Hypothesis        : H₁: Terdapat perbedaan signifikan akurasi antara DenseNet-169 dan VGG-19 pada klasifikasi penyakit daun padi (H₀ ditolak).
Tipe Eksperimen   : [x] Comparison  [ ] Ablation  [ ] Parameter

Kondisi Eksperimen:
| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | Menggunakan arsitektur baseline VGG-19 | VGG-19 | Dataset Kaggle, LR 0.001, Epoch 50, Seed 42 |
| Treatment | Menggunakan arsitektur usulan DenseNet-169 | DenseNet-169 | Dataset Kaggle, LR 0.001, Epoch 50, Seed 42 |

Fairness Checklist:
  [x] Dataset identik untuk semua kondisi
  [x] Preprocessing setara
  [x] Tuning effort setara
  [x] Environment identik
  [x] Metrik evaluasi sama

Threat Analysis:
| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal    | Data Leakage (foto mirip masuk ke train & test) | Menggunakan Stratified K-Fold agar distribusi kelas konsisten |
| External    | Dataset terlalu bersih/ideal (Kaggle) | Menambahkan augmentasi noise/blur untuk simulasi kondisi nyata |
| Construct   | Akurasi tinggi tapi salah prediksi pada kelas minoritas | Menggunakan F1-Score dan Confusion Matrix sebagai metrik utama |
| Conclusion  | Hasil tinggi hanya karena "kebetulan" satu kali run | Melakukan running eksperimen sebanyak 5-10 kali dan diambil rata-ratanya |

Statistical Plan:
  Uji statistik   : T-Test Independent atau Mann-Whitney U Test
  Justifikasi      : Membandingkan rata-rata akurasi dari dua kelompok model yang berbeda.
  Alpha            : 0.05
  Effect size min  : 0.5 (Medium effect)
```

---

## Latihan 1 — Desain Eksperimen

Susun desain eksperimen berdasarkan RQ, variabel, dan sistem dari WS-04 sampai WS-06.

**RQ:** Apakah model CNN DenseNet-169 menghasilkan akurasi lebih tinggi dibandingkan VGG-19 pada klasifikasi penyakit daun padi menggunakan dataset citra daun padi?
**Tipe eksperimen:** [x] Comparison / [ ] Ablation / [ ] Parameter

| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | VGG-19 sebagai standar arsitektur CNN klasik. | VGG-19 | 710 citra, split 80:20, batch 32. |
| Treatment | DenseNet-169 dengan fitur feature reuse (dense blocks). | DenseNet-169 | 710 citra, split 80:20, batch 32. |

---

## Latihan 2 — Fairness Checklist

Evaluasi apakah desain eksperimen di Latihan 1 sudah fair.

| Kriteria | Status | Detail |
|----------|--------|--------|
| Dataset identik | ✅ — Sama-sama pakai dataset Kaggle (710 citra) | Memastikan kedua model belajar dari sumber data yang sama persis. |
| Preprocessing setara | ✅ — Sama-sama resize 64x64 & normalisasi | Tidak ada perlakuan khusus pada input data untuk salah satu model.|
| Tuning effort setara | ✅ — Sama-sama pakai Adam Optimizer & 50 Epoch | Usaha optimasi dibuat seimbang agar perbandingannya jujur (fair). |
| Environment identik | ✅ — Sama-sama running di Google Colab (Tesla T4) | Menghindari perbedaan hasil yang disebabkan oleh variasi hardware. |
| Metrik evaluasi sama | ✅ — Sama-sama pakai Accuracy & F1-Score | Parameter keberhasilan diukur dengan penggaris yang sama. |

**Ada yang tidak fair?** [ ] Ya / [x] Tidak
> Jika ya, bagaimana cara memperbaikinya? ________________

---

## Latihan 3 — Threat Analysis

Identifikasi ancaman validitas untuk desain eksperimen ini.

| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal | Overfitting karena dataset sangat kecil (710 gambar). | Menggunakan Data Augmentation dan Early Stopping. |
| External | Model tidak bisa mengenali penyakit padi di varietas lokal Indonesia. | Memberikan disclaimer batasan dataset pada laporan akhir. |
| Construct | Akurasi menipu karena jumlah data per kelas tidak seimbang. | Wajib melaporkan Precision dan Recall per kelas penyakit. |
| Conclusion | Jumlah sampel pengujian (test set) terlalu sedikit untuk uji statistik. | Menggunakan Cross-Validation untuk memperbanyak sampel data performa. |

**Ancaman mana yang paling sulit dimitigasi?** External Validity.
**Mengapa?**
> Karena kita menggunakan dataset publik (Kaggle). Tanpa mengambil data langsung dari sawah lokal di Indonesia, kita tidak pernah bisa menjamin 100% bahwa model ini akan seakurat itu jika dipasang di aplikasi petani lokal.

---

## Refleksi

> Sebuah paper melaporkan "metode kami mengalahkan semua baseline." Apa 3 pertanyaan pertama yang harus diajukan untuk mengevaluasi klaim ini?

**Jawaban:**
1. Apakah baseline di-tuning secara adil?
2. Apakah dataset pengujian benar-benar terpisah?
3. Apakah perbandingannya menggunakan metrik yang relevan?