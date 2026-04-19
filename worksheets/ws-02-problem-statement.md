# WS-02: Problem Statement

> **Bab 2 — Problem Formulation & System Context**

---

## Ringkasan Materi

### Problem Formation Model

Masalah riset melewati 5 tahap transformasi. Melompat langsung dari Reality ke Variable adalah kesalahan paling umum.

```
Reality → Observed Issue (Symptom) → Diagnosed Problem (Root Cause)
→ Researchable Problem (Scoped) → Measurable Variable (Operationalized)
```

### Topic ≠ Problem ≠ Research Problem

| Level | Contoh | Status |
|-------|--------|--------|
| **Topik** | Keamanan IoT | Terlalu luas, tidak bisa diuji |
| **Problem** | MQTT tidak terenkripsi | Spesifik tapi belum riset |
| **Research Problem** | Belum ada studi membandingkan overhead TLS 1.3 vs DTLS pada MQTT di IoT RAM < 64KB | Bisa dirancang eksperimennya |

### Symptom vs Root Cause

Apa yang diamati (gejala) ≠ mengapa terjadi (akar masalah). Gunakan **5 Whys** atau **Fishbone Diagram** untuk menggali.

Contoh: "User meninggalkan checkout" (symptom) → "Waktu loading > 8 detik karena API call sequential" (root cause).

### System Thinking

Setiap masalah riset TI harus terikat pada komponen sistem: **Input → Process → Output → Outcome → Constraints → Stakeholders**.

### Problem Quality Check

Masalah riset yang layak harus memenuhi 5 kriteria:
- **Clarity** — Satu orang membaca akan paham
- **Measurability** — Ada metrik kuantitatif
- **Relevance** — Penting untuk domain
- **Testability** — Bisa gagal (falsifiable)
- **Impact** — Ada kontribusi jika terjawab

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Menyelesaikan masalah (*solve*) | Memahami dan membuktikan (*understand & prove*) |
| Masalah | Bug, error, fitur belum ada | Gap dalam pengetahuan |
| Scope | Selesaikan semua yang perlu | Batasi agar bisa dibuktikan |
| Output | Working system | Evidence, paper, replicable findings |

### Istilah Penting

- **Problem Statement** — Formulasi tertulis: konteks sistem + gap + dampak + justifikasi
- **System Context** — Deskripsi lengkap: input, proses, output, outcome, constraints, stakeholders
- **Problem Drift** — Masalah "bermutasi" dari pendahuluan ke metodologi karena statement awal tidak presisi
- **Solution-First Thinking** — Memulai dari solusi tanpa masalah yang jelas — berbahaya dalam riset
- **Operational Definition** — Definisi variabel yang cukup jelas agar peneliti lain bisa mengukur hal yang sama

---

## Template A.2 — Problem Statement Builder

```
PROBLEM STATEMENT BUILDER

Domain & Konteks
  Domain   : Machine Learning / Computer Vision
  Konteks  : Deteksi dini penyakit tanaman pada sektor pertanian (Padi).

System Context
  Input       : Citra (gambar) daun padi dalam format digital (RGB).
  Process     : Ekstraksi fitur otomatis menggunakan lapisan Convolutional Neural Network (CNN).
  Output      : Label klasifikasi (Blight, Blast, Tungro, atau Sehat).
  Outcome     : Petani dapat mengidentifikasi penyakit padi secara cepat tanpa ahli botani.
  Constraints : Kapasitas komputasi untuk pelatihan model dan keterbatasan jumlah dataset.
  Stakeholders: Peneliti, Praktisi Pertanian, dan Petani.

Fenomena → Problem
  Fenomena yang diamati             : Penyakit padi menurunkan produktivitas pertanian secara drastis.
  Gejala (symptom) yang terukur     : Identifikasi manual oleh manusia sering kali lambat dan subjektif.
  Masalah yang didiagnosis          : Kurangnya model klasifikasi yang efisien dan akurat untuk deteksi otomatis.
  Masalah riset (researchable)      : Sejauh mana arsitektur CNN sederhana dengan optimasi Adam dapat meningkatkan akurasi klasifikasi penyakit padi dibandingkan model sebelumnya?
  Variabel yang terukur             : Akurasi (Accuracy), Precision, Recall, dan F1-Score.

Problem Quality Check
  [x] Clarity — Apakah satu orang membaca akan paham? (Ya, fokus pada padi dan CNN)
  [x] Measurability — Apakah ada metrik kuantitatif? (Ya, skor akurasi 0-1)
  [x] Relevance — Apakah penting untuk domain? (Ya, ketahanan pangan)
  [x] Testability — Apakah bisa gagal? (Ya, jika model tidak mencapai akurasi target)
  [x] Impact — Apakah ada kontribusi jika terjawab? (Ya, efisiensi diagnosis penyakit)

Problem Statement (1 paragraf):
  Identifikasi penyakit padi yang terlambat berisiko menurunkan hasil panen secara signifikan, namun proses identifikasi manual saat ini masih lambat dan memerlukan tenaga ahli. Meskipun teknologi Computer Vision mulai digunakan, masih terdapat gap dalam efisiensi performa model klasifikasi otomatis. Penelitian ini bertujuan mengimplementasikan arsitektur CNN sederhana yang dioptimasi dengan algoritma Adam untuk meningkatkan akurasi deteksi penyakit padi (Hawar, Blas, Tungro) agar dapat memberikan solusi klasifikasi yang cepat dan akurat bagi sektor pertanian.
```

---

## Latihan 1 — Dari Topik ke Masalah Riset

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** Klasifikasi Penyakit Tanaman Padi dengan Deep Learning.

| Tahap | Hasil |
|-------|-------|
| Reality | Petani kesulitan mendeteksi penyakit daun padi secara akurat di sawah yang luas. |
| Observed Issue (Symptom) | Terjadi gagal panen akibat serangan penyakit yang baru terdeteksi saat sudah parah. |
| Diagnosed Problem (Root Cause) | Kurangnya sistem pakar otomatis yang bisa mendiagnosis penyakit daun hanya dari foto. |
| Researchable Problem | Perbandingan efektivitas berbagai parameter arsitektur CNN dalam mengenali pola tekstur penyakit padi. |
| Measurable Variable | Tingkat akurasi klasifikasi dan nilai Loss pada proses pelatihan model. |

**Apakah terjebak solution-first thinking?** [ ] Ya / [x] Tidak
> Jika ya, kembali ke tahap mana? ________________________

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | Dataset citra daun padi (710 gambar) dari Kaggle. |
| Process | Feature learning melalui 4 lapis konvolusi dan 2 lapis pooling. |
| Output | Prediksi kategori penyakit dalam bentuk probabilitas. |
| Outcome | Diagnosa penyakit padi yang objektif dan konsisten. |
| Constraints | Dataset yang tidak seimbang (imbalance) dan resolusi input yang terbatas ( 64 x 64).|
| Stakeholders | Peneliti Informatika dan pengembang aplikasi teknologi pertanian. |

**Komponen mana yang paling relevan dengan masalah riset?** Process (Arsitektur CNN yang dirancang).

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | 5 | Sangat jelas: Input daun padi, metode CNN, output klasifikasi. |
| Measurability | 5 | Menggunakan standar pengukuran ML (Akurasi, F1-Score) yang jelas. |
| Relevance | 4 | Sangat relevan bagi Indonesia sebagai negara agraris. |
| Testability | 5 | Model bisa diuji ulang dan dibandingkan performanya dengan metode lain. |
| Impact | 4 | Berdampak pada efisiensi pemantauan lahan pertanian. |

**Skor total:** 23 / 25

**Problem statement versi final (1 paragraf):**
> Penurunan produktivitas padi akibat penyakit daun memerlukan solusi diagnosis cepat, namun model klasifikasi otomatis yang ada saat ini masih perlu dioptimalkan akurasinya untuk berbagai jenis penyakit seperti Hawar dan Tungro. Penelitian ini meneliti penggunaan model CNN dengan optimasi Adam melalui skenario eksperimen arsitektur khusus untuk mengukur peningkatan performa klasifikasi citra daun padi. Hasil penelitian ini diharapkan memberikan bukti empiris mengenai efektivitas parameter CNN dalam menangani keterbatasan jumlah data namun tetap menghasilkan akurasi yang kompetitif.

---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> Perbedaan fundamentalnya terletak pada tujuan akhirnya. Masalah coding (bug/error) bersifat praktis dan biner (selesai atau tidak selesai) untuk memperbaiki fungsionalitas sistem agar bisa berjalan. Sebaliknya, masalah riset bertujuan untuk memahami dan membuktikan sebuah gap pengetahuan. Dalam coding, "kenapa error" dijawab dengan perbaikan baris kode. Dalam riset, "kenapa model tidak akurat" dijawab dengan analisis data, eksperimen metodologi, dan pembuktian statistik yang dapat direplikasi oleh orang lain. Masalah riset menuntut validasi ilmiah, bukan sekadar sistem yang "bekerja".
