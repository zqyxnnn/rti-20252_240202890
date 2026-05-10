# WS-04: Research Question & Hypothesis

> **Bab 4 — Research Question, Contribution & Hypothesis**

---

## Ringkasan Materi

### RQ Bukan Pertanyaan Biasa

Research Question yang baik secara implisit mengandung cetak biru eksperimen: subjek, baseline, metrik, domain, dataset.

| Kualitas | Contoh |
|----------|--------|
| **Buruk** | "Bagaimana pengaruh deep learning terhadap deteksi malware?" |
| **Baik** | "Apakah CNN menghasilkan F1-Score lebih tinggi dari RF pada CIC-MalMem-2022?" |

Perbedaan: RQ yang baik menyebutkan **metode spesifik**, **metrik terukur**, **baseline**, dan **dataset**.

### Tiga Jenis RQ

| Jenis | Pola | Kebutuhan |
|-------|------|-----------|
| **Comparison** | A vs B → mana lebih baik? | ≥ 2 metode, metrik sama |
| **Improvement** | A' vs A → modifikasi lebih baik? | Pre/post, bukti perbaikan |
| **Exploratory** | Faktor X₁...Xₙ → pengaruh terhadap Y? | Multi-variabel, korelasi/regresi |

### Contribution Statement

Tiga jenis kontribusi: **Improvement** (metode terbukti lebih baik), **Comparison** (perbandingan sistematis yang belum ada), **Novel Approach** (pendekatan baru). Kontribusi harus terhubung langsung dengan gap — kontribusi tanpa gap = klaim tanpa justifikasi.

### Hypothesis H₀ / H₁

- **H₀** (Null) = Tidak ada perbedaan signifikan — asumsi default, harus dibuktikan salah
- **H₁** (Alternative) = Ada perbedaan signifikan — diterima hanya jika H₀ ditolak
- Harus **falsifiable**, mengandung **metrik terukur**, dirumuskan **SEBELUM eksperimen**

### Rantai Operasionalisasi

```
RQ → Variable → Metric → Data → Analysis
```

Jika rantai ini tidak lengkap, RQ belum mature. Bi-directional: RQ yang tidak bisa jadi hipotesis testable harus direvisi mundur.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan pertanyaan | Apa yang harus dibangun? | Apa yang harus dibuktikan? |
| Bentuk jawaban | Sistem yang berfungsi | Bukti empiris terukur |
| Sukses diukur oleh | User satisfaction, uptime | Signifikansi statistik, effect size |
| Jika gagal | Debug dan perbaiki | Laporkan, analisis mengapa |

### Istilah Penting

- **Research Question (RQ)** — Pertanyaan spesifik: variabel terukur + metrik + konteks
- **Contribution Statement** — Apa yang diketahui setelah riset selesai yang sebelumnya belum ada
- **H₀ / H₁** — Null vs Alternative Hypothesis
- **Falsifiability** — Kondisi hipotesis ditolak harus bisa didefinisikan sebelum eksperimen
- **Operationalization** — Proses mewujudkan konsep abstrak menjadi variabel terukur

---

## Template A.4 — RQ-Contribution-Hypothesis

```
RQ-CONTRIBUTION-HYPOTHESIS

Gap Statement  : Dataset yang digunakan pada penelitian klasifikasi penyakit daun padi masih terbatas sehingga performa model belum stabil di kondisi nyata

Research Question:
  Tipe         : [x] Comparison  [ ] Improvement  [ ] Exploratory
  Formulasi    : Apakah model CNN DenseNet-169 menghasilkan akurasi lebih tinggi dibandingkan VGG-19 pada klasifikasi penyakit daun padi menggunakan dataset citra daun padi?
  Variabel IV  : Jenis model CNN (DenseNet-169 vs VGG-19)
  Variabel DV  : Akurasi klasifikasi
  Metrik       : Accuracy
  Dataset      : Dataset citra daun padi (gabungan dataset penelitian sebelumnya + augmentasi)
  Baseline     : VGG-19


Quality Check RQ:
  [x] Variabel spesifik
  [x] Metrik jelas
  [x] Baseline ada
  [x] Konteks disebutkan
  [x] Memerlukan eksperimen (bukan hanya survei literatur)

Contribution Statement:
  Apa yang baru diketahui : Perbandingan performa antara DenseNet-169 dan VGG-19 pada dataset daun padi yang lebih variatif
  Jenis kontribusi        : [ ] Improvement  [x] Comparison  [ ] Novel approach
  Gap yang diisi          : Keterbatasan studi perbandingan model CNN pada dataset kecil dengan performa yang belum stabil


Hypothesis Pair:
  H₀ : Tidak ada perbedaan signifikan akurasi antara DenseNet-169 dan VGG-19 pada klasifikasi penyakit daun padi
  H₁ : Terdapat perbedaan signifikan akurasi antara DenseNet-169 dan VGG-19 pada klasifikasi penyakit daun padi
  Threshold              :  α = 0.05
  Justifikasi threshold  : Nilai α = 0.05 umum digunakan dalam penelitian untuk menentukan signifikansi statistik
```

---

## Latihan 1 — Dari Gap ke RQ

Gunakan gap yang ditemukan di WS-03. Transformasikan menjadi Research Question.

**Gap dari WS-03:** Dataset kecil menyebabkan model kurang stabil dan performa belum optimal di kondisi nyata

**RQ versi pertama (tulis bebas):**
> Apakah DenseNet lebih baik dari VGG untuk klasifikasi penyakit daun padi?

**Evaluasi RQ:**

| Komponen | Ada? | Isi |
|----------|------|-----|
| Metode spesifik | Ya | DenseNet vs VGG |
| Metrik terukur | Tidak | Belum disebut |
| Baseline | Tidak| Belum jelas |
| Dataset/konteks | Tidak | Belum disebut |

**Tipe RQ:** [x] Comparison / [ ] Improvement / [ ] Exploratory

**RQ versi revisi (setelah evaluasi):**
> Apakah model DenseNet-169 menghasilkan akurasi lebih tinggi dibandingkan VGG-19 pada klasifikasi penyakit daun padi menggunakan dataset citra daun padi?

---

## Latihan 2 — Hypothesis Pair

Rumuskan pasangan hipotesis dari RQ di Latihan 1.

| Komponen | Isi |
|----------|-----|
| H₀ | Tidak ada perbedaan signifikan akurasi antara DenseNet-169 dan VGG-19 |
| H₁ | Terdapat perbedaan signifikan akurasi antara DenseNet-169 dan VGG-19 |
| Metrik | Accuracy |
| Threshold | 0.05 |
| Justifikasi threshold | Standar umum dalam uji statistik penelitian |

**Apakah hipotesis ini falsifiable?** [x] Ya / [ ] Tidak
> Bagaimana cara membuktikannya salah? Dengan melakukan eksperimen dan uji statistik. Jika hasil uji menunjukkan p-value > 0.05, maka H₁ ditolak dan H₀ tidak bisa ditolak.

---

## Latihan 3 — Rantai Operasionalisasi

Lengkapi rantai dari RQ hingga metode analisis.

| Tahap | Isi |
|-------|-----|
| RQ | Apakah DenseNet-169 menghasilkan akurasi lebih tinggi dibandingkan VGG-19 pada klasifikasi penyakit daun padi |
| Variable (IV) | Jenis model CNN (DenseNet-169 vs VGG-19) |
| Variable (DV) | Akurasi klasifikasi |
| Metric | Accuracy |
| Data source | Dataset citra daun padi (gabungan + augmentasi) |
| Analysis method | Perbandingan akurasi + uji statistik (t-test atau sejenisnya) |

**Apakah rantai lengkap?** [x] Ya / [ ] Tidak
> Jika tidak, tahap mana yang perlu direvisi? ______________

---

## Refleksi

> Ambil satu judul skripsi/paper yang pernah dibaca. Coba ekstrak RQ-nya. Apakah RQ tersebut memenuhi semua komponen (metode, metrik, baseline, konteks)? Jika tidak, apa yang hilang?

**Judul:** Klasifikasi Citra Penyakit Daun Tanaman Padi Menggunakan CNN dengan Arsitektur VGG-19
**RQ yang diekstrak:** Bagaimana performa CNN VGG-19 dalam mengklasifikasikan penyakit daun padi?
**Komponen yang hilang:** Tidak ada baseline pembanding, tidak ada metrik spesifik di pertanyaan (walau ada di hasil), dan tidak disebutkan konteks dataset secara eksplisit.