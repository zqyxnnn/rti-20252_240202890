# WS-16: Presentation & Defense (UAS)

> **Bab 16 — Presentasi & Pertahanan Ilmiah**

---

## Ringkasan Materi

### Scientific Defense Model

```
Research Work → Presentation → Questioning → Defense → Evaluation → Acceptance
```

### Presentasi ≠ Ringkasan Paper

| Paper | Presentasi |
|-------|-----------|
| Dibaca (self-paced) | Didengar (presenter-paced) |
| Detail lengkap | Ide kunci + highlight |
| Tabel numerik detail | Grafik visual + angka kunci |
| Pembaca bisa re-read | Audiens dengar sekali |

**Prinsip:** Presentasi membutuhkan **reformulasi**, bukan kompresi. Medium berbeda = pendekatan berbeda.

### Claim-Evidence-Reasoning (CER)

Setiap jawaban defense harus memiliki:
1. **Claim** — Pernyataan yang dijawab
2. **Evidence** — Data/fakta pendukung
3. **Reasoning** — Logika yang menghubungkan evidence ke claim

**Contoh:**
| Pertanyaan | Bad Answer | Good Answer (CER) |
|-----------|-----------|-------------------|
| "Kenapa hanya 3 dataset?" | "Tiga sudah cukup" | "3 dataset mewakili variasi: small-clean, medium-clean, medium-noisy [E]. Generalisasi perlu validasi lanjut — listed as limitation [R]" |
| "Hasil DS-3 menurun?" | "Itu outlier" | "Ya, karena distribusi heavy-tail melanggar asumsi Gaussian [E]. Ini menunjukkan boundary condition metode [R]" |
| "Effect size?" | "p=0.003, jadi signifikan" | "Cohen's d=1.2 (large effect) [E] — bukan hanya signifikan tapi substansial [R]" |

### Slide Design — One Slide, One Message

**Optimal 9-Slide Plan (15 menit):**

| # | Slide | Waktu | Pesan |
|---|-------|-------|-------|
| 1 | Title + context | 1 min | Apa ini tentang apa |
| 2 | Problem + motivation | 2 min | Mengapa penting |
| 3 | Gap + RQ | 1.5 min | Apa yang belum terjawab |
| 4 | Method overview | 2 min | Bagaimana dijawab (diagram) |
| 5 | Key result — tabel | 2 min | Temuan utama |
| 6 | Key result — grafik | 2 min | Pola visual |
| 7 | Interpretation + failure | 2 min | Apa artinya |
| 8 | Limitation + future | 1.5 min | Batasan & arah |
| 9 | Conclusion + contribution | 1 min | Closing message |

### Anticipatory Defense

Prediksi pertanyaan berdasarkan kategori:

| Kategori | Contoh Pertanyaan |
|---------|------------------|
| Problem | "Mengapa masalah ini penting?" |
| Gap | "Bagaimana dengan studi X yang sudah menjawab ini?" |
| Method | "Mengapa metode ini, bukan Y?" |
| Results | "Bagaimana menjelaskan anomali di DS-3?" |
| Generalization | "Apakah bisa diterapkan di domain lain?" |

### Tiga Prinsip Jawaban

1. **Direct** — Jawab dulu, elaborasi kemudian
2. **Data-based** — Tunjuk evidence spesifik
3. **Honest** — Akui limitasi jika memang ada

### Jebakan Kognitif

1. "Presentasi = semua yang ada di paper" → terlalu padat
2. "Slide cantik = presentasi bagus" → konten > estetika
3. "Tidak bisa jawab = gagal" → "I don't know, but..." menunjukkan kejujuran
4. "Tidak perlu latihan — saya paham riset saya" → latihan = menemukan celah

---

## Template A.16 — Defense Preparation Sheet

```
DEFENSE PREPARATION

Slide Deck Plan:
  Total slides   : 9 slide konten + 1 title + 1 closing = 11 slide
  Time per slide : ~1.3 min
  Total time     : 15 menit

Slide Outline:

| # | Pesan Utama | Visual | Waktu |
|---|-------------|--------|-------|
| 1 | Title       |    Judul & Foto daun padi    | 1min |
| 2 | Problem     |    Infografis alur deteksi manual    | 2min  |
| 3 | Gap + RQ    |    Gap matrix (VGG vs DenseNet)    | 1.5min  |
| 4 | Method: Pipeline 35 runs & t-Test |    Diagram alir sistem    | 2min |
| 5 | Key result: Tabel Akurasi | Tabel ringkasan akurasi | 2min |
| 6 | Key result: Grafik Box Plot | Box plot distribusi performa | 2min |
| 7 | Interpretation: Hasil setara secara statistik | Analisis saturation point | 2min |
| 8 | Limitation: Resolusi & saran masa depan | Bullet points batasan riset | 1.5min |
| 9 | Conclusion: Efisiensi > kompleksitas | Diagram alir sistem | 1min |


Anticipatory Defense Matrix:
| Kategori | Pertanyaan Potensial | Jawaban (CER) |
|----------|---------------------|---------------|
| Problem  | Mengapa masalah ini penting? | Padi adalah komoditas krusial; deteksi dini otomatis mengurangi gagal panen [C]. Data ekonomi menunjukkan ancaman penyakit blas/hawar daun [E]. Otomasi menurunkan subjektivitas pakar [R]. |
| Gap      | Bagaimana dengan studi terdahulu? | Studi sebelumnya seringkali hanya single-run [C]. Hasil iterasi 35 kali menunjukkan standar deviasi > 4% [E]. Hal ini membuktikan bahwa single-run tidak cukup reliabel [R]. |
| Method   | Mengapa 35 iterasi? | Untuk menjamin reliabilitas statistik [C]. Nilai SD > 4% pada kedua model [E]. Eksperimen berulang memitigasi bias inisialisasi bobot acak [R]. |
| Results  | Mengapa performa setara? | Kedua model mencapai saturation point [C]. Wilcoxon p-value 0.7004 (> 0.05) [E]. Fitur daun padi tidak memerlukan arsitektur yang terlalu dalam untuk diklasifikasi [R]. |
| Generalization | Bisakah diterapkan di domain lain? | Ya, dengan retraining [C]. Arsitektur CNN bersifat agnostik domain [E]. Transfer learning memungkinkan adaptasi ke kelas citra lain [R]. |

Latihan:
  Latihan 1: [tanggal] — 2026-07-13 — Draft slide deck siap.
  Latihan 2: [tanggal] — 2026-07-13 — Simulasi tanya jawab mandiri.
  Latihan 3: [tanggal] — 2026-07-13 — Uji coba presentasi di depan rekan.
```

---

## Latihan 1 — Slide Outline

Rencanakan presentasi 15 menit untuk riset Anda.

| # | Pesan Utama | Visual yang Digunakan | Waktu |
|---|-------------|-----------------------|-------|
| 1 | Judul + Konteks (Penyakit Padi) | Judul & Foto daun padi | 1 min |
| 2 | Problem: Deteksi manual subjektif & lambat | Infografis alur deteksi manual | 2 min |
| 3 | Gap + RQ: Konsensus arsitektur belum ada | Gap matrix (VGG vs DenseNet) | 1.5 min |
| 4 | Method: Pipeline 35 runs & t-Test | Diagram alir sistem | 2 min |
| 5 | Key result: Tabel Akurasi | Tabel ringkasan akurasi | 2 min |
| 6 | Key result: Grafik Box Plot | Box plot distribusi performa | 2 min |
| 7 | Interpretation: Hasil setara secara statistik | Analisis saturation point | 2 min |
| 8 | Limitation: Resolusi & saran masa depan | Bullet points batasan riset | 1.5 min |
| 9 | Conclusion: Efisiensi > kompleksitas | Highlight kontribusi utama | 1 min |

**Total waktu estimasi:** 15 menit

---

## Latihan 2 — Anticipatory Defense

Prediksi 5 pertanyaan yang mungkin diajukan penguji, lalu siapkan jawaban CER.

| # | Kategori | Pertanyaan | Claim | Evidence | Reasoning |
|---|----------|-----------|-------|----------|-----------|
| 1 | Problem | Mengapa masalah ini penting? | Padi krusial bagi ekonomi. | Data penurunan produktivitas. | Otomasi menurunkan subjektivitas. |
| 2 | Gap | Bagaimana dengan studi terdahulu? | Studi terdahulu kurang reliabel. | SD > 4% pada hasil single-run. | Iterasi 35 kali menjamin stabilitas. |
| 3 | Method | Mengapa 35 iterasi? | Memitigasi bias inisialisasi. | Standar deviasi > 4%. | Eksperimen berulang itu mutlak. |
| 4 | Results | Mengapa performa setara? | Kedua model mencapai saturasi. | p-value 0.7004 (> 0.05). | Fitur cukup sederhana. |
| 5 | Gen | Bisa diterapkan di domain lain? | Ya, dengan retraining. | Arsitektur bersifat agnostik. | Transfer learning memungkinkan. |

---

## Latihan 3 — Simulasi Q&A

Minta teman/kolega mengajukan 3 pertanyaan tentang riset Anda. Catat pertanyaan dan evaluasi jawaban Anda.

| # | Pertanyaan | Jawaban Saya | Evaluasi |
|---|-----------|-------------|---------|
| 1 | Kenapa tidak pakai ViT? | Fokus pada perbandingan CNN klasik. | [x] Direct [x] Data-based [x] Honest |
| 2 | Bagaimana jika data ditambah? | DenseNet berpotensi lebih unggul. | [x] Direct [xgit add .] Data-based [x] Honest |
| 3 | Apakah hasil sudah divalidasi? | Penelitian fokus pada 2 arsitektur. | [x] Direct [x] Data-based [x] Honest |

**Pertanyaan yang paling sulit dijawab:**
> "Apakah perbedaan performa ini sudah mencakup optimasi hyperparameter?"

**Apa yang perlu disiapkan lebih baik:**
> Menyiapkan data bahwa fine-tuning dilakukan konsisten di kedua arsitektur agar perbandingan apple-to-apple.

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-16 — dari paradigma riset hingga presentasi — bagian mana yang paling mengubah cara Anda berpikir tentang riset? Apa satu hal yang akan selalu Anda terapkan di riset berikutnya?

**Insight terbesar:**
> Bagian yang paling mengubah cara berpikir saya adalah Consistency Matrix (WS-15). Sebelumnya, saya hanya menulis bagian per bagian secara terpisah. Ternyata, riset yang kuat adalah riset yang "benang merahnya" (RQ, Method, Result) terikat kencang sejak awal, sehingga defense di akhir menjadi jauh lebih mudah karena datanya sudah konsisten.

**Yang akan selalu diterapkan:**
> Saya akan selalu menerapkan pendekatan CER (Claim-Evidence-Reasoning) dalam setiap komunikasi ilmiah maupun profesional. Menjawab dengan data dan logika jauh lebih efektif daripada sekadar berargumen subjektif.
