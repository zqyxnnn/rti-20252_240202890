# WS-08: Proposal Integration (UTS)

> **Bab 8 — Proposal & Checkpoint**

---

## Ringkasan Materi

### Proposal = Satu Argumen Utuh

Proposal riset bukan kumpulan bab yang independen. Ia adalah **satu argumen** yang mengalir dari masalah ke rencana solusi. Jika satu koneksi putus, seluruh proposal kehilangan koherensi.

### Integration Map — 6 Koneksi Kritis

```
Problem (Bab 2) → Gap (Bab 3) → RQ & H (Bab 4) → Metrik (Bab 5) → Sistem (Bab 6) → Eksperimen (Bab 7)
```

| Koneksi | Pertanyaan Verifikasi |
|---------|----------------------|
| Problem → Gap | Apakah gap muncul dari analisis literatur terhadap masalah? |
| Gap → RQ | Apakah RQ langsung menjawab gap yang teridentifikasi? |
| RQ → Metrik | Apakah setiap variabel di RQ punya metrik terdefinisi? |
| Metrik → Sistem | Apakah setiap metrik bisa diukur oleh komponen sistem? |
| Sistem → Eksperimen | Apakah desain eksperimen menggunakan sistem sebagai instrumen? |

### Koherensi Vertikal + Horizontal

- **Vertikal** — Alur logis atas-ke-bawah (problem → experiment)
- **Horizontal** — Konsistensi terminologi (nama variabel di RQ = di hipotesis = di metrik = di desain)

### Jebakan Kognitif

| Jebakan | Deskripsi |
|---------|----------|
| "Selling" Introduction | Menulis promosi, bukan menyajikan data dan gap |
| Copy-paste Methodology | Menyalin deskripsi tekstbook tanpa menyesuaikan ke RQ |
| Optimistic Timeline | Meremehkan waktu implementasi; selalu tambah buffer 30-50% |
| No Possibility of Failure | Mengimplikasikan hasil pasti sukses — proposal jujur mengakui H₀ mungkin tidak ditolak |

### Struktur Proposal

1. **Pendahuluan** — Latar belakang + problem statement (Bab 1-2)
2. **Tinjauan Pustaka** — Literature review + gap + baseline (Bab 3)
3. **RQ / Kontribusi / Hipotesis** — (Bab 4)
4. **Metodologi** — Metrik + sistem + desain eksperimen (Bab 5-7)
5. **Timeline & Output**

### Istilah Penting

- **Integration Map** — Diagram 6 koneksi kritis antar komponen proposal
- **Vertical Coherence** — Alur logis atas-ke-bawah
- **Horizontal Coherence** — Konsistensi terminologi di semua bagian
- **Checkpoint** — Titik self-assessment sebelum transisi dari desain ke eksekusi

---

## Template A.8 — Integration Checklist

```
PROPOSAL INTEGRATION CHECKLIST

Koneksi Vertikal (Flow Atas-Bawah):
  [x] Problem → Gap: masalah terdokumentasi di literatur
  [x] Gap → RQ: pertanyaan menjawab gap spesifik
  [x] RQ → Hypothesis: hipotesis memprediksi jawaban
  [x] Hypothesis → Metric: metrik mengukur variabel dalam hipotesis
  [x] Metric → System: komponen sistem menghasilkan/mengukur metrik
  [x] System → Experiment: desain eksperimen menggunakan sistem

Koneksi Horizontal (Konsistensi):
  [x] Istilah sama di semua bagian
  [x] Variabel di RQ = variabel di hipotesis = metrik di desain
  [x] Scope tidak berubah dari masalah ke eksperimen

Rubrik Self-Assessment:
| Kriteria | 1 (Lemah) | 2 (Cukup) | 3 (Baik) | Skor |
|----------|-----------|-----------|----------|------|
| Koherensi |          |           |    [x]   |      |
| Specificity |        |           |    [x]   |      |
| Feasibility |        |           |    [x]   |      |
| Rigor     |          |    [x]    |          |      |
```

---

## Latihan 1 — Kompilasi Proposal Mini

Kumpulkan hasil dari WS-02 sampai WS-07 menjadi satu ringkasan proposal.

| Komponen | Sumber | Isi (1-2 kalimat) |
|----------|--------|-------------------|
| Problem Statement | WS-02 | Sistem Deep Learning untuk klasifikasi penyakit daun padi membutuhkan data citra dalam jumlah besar, sedangkan dataset yang tersedia (710 citra) sangat terbatas dan rentan terhadap overfitting. Kondisi ini membuat performa model CNN tradisional menjadi tidak optimal. |
| Gap | WS-03 | Terdapat gap pengetahuan mengenai perbandingan performa secara spesifik dan ketat antara arsitektur VGG-19 dan DenseNet-169 pada dataset penyakit daun padi yang sangat terbatas ini. |
| RQ | WS-04 | *Apakah terdapat perbedaan performa yang signifikan antara arsitektur VGG-19 dan DenseNet-169 dalam klasifikasi penyakit daun tanaman padi pada dataset yang sangat terbatas, jika diukur menggunakan Akurasi dan F1-Score? |
| Hipotesis | WS-0 | H₁: Arsitektur DenseNet-169 menghasilkan performa klasifikasi (Akurasi dan F1-Score) yang secara statistik lebih tinggi dibandingkan dengan arsitektur VGG-19 pada dataset penyakit daun padi yang sangat terbatas. |
| Variabel & Metrik | WS-05 | IV = jenis arsitektur model (VGG-19 vs DenseNet-169); DV = Akurasi dan F1-Score (performa klasifikasi). |
| Sistem | WS-06 | Sistem eksperimen adalah pipeline pemrograman Python modular yang mencakup prapemrosesan citra (reduksi ukuran ke 64x64 piksel), implementasi model VGG-19, implementasi model DenseNet-169, serta modul evaluasi performa yang menghitung Akurasi dan F1-Score secara kuantitatif. |
| Desain Eksperimen | WS-07 | Desain eksperimen adalah repeated runs komparatif dengan 5 kali pengulangan independen untuk setiap model (VGG-19 dan DenseNet-169) pada dataset yang sama untuk mengukur variabilitas dan rata-rata metrik Akurasi serta F1-Score. |

---

## Latihan 2 — Integration Checklist

Verifikasi 6 koneksi kritis. Isi dengan merujuk tabel di Latihan 1.

| Koneksi | Status | Bukti |
|---------|--------|-------|
| Problem → Gap | ✅  | Gap muncul langsung dari masalah keterbatasan data yang menyebabkan overfitting, di mana perlu dicari model yang lebih efisien di antara VGG-19 dan DenseNet-169. |
| Gap → RQ |  ✅  | RQ secara langsung merumuskan pertanyaan mengenai perbedaan performa model CNN spesifik untuk mengatasi keterbatasan data tersebut. |
| RQ → Hypothesis |  ✅  | Hipotesis memberikan prediksi jawaban langsung atas pertanyaan penelitian (DenseNet-169 diprediksi lebih baik). |
| Hypothesis → Metric | | Metrik performa klasifikasi (Akurasi dan F1-Score) yang dipilih di desain eksperimen akan langsung menguji hipotesis ini. |
| Metric → System | ✅ | Sistem yang dibangun memiliki komponen khusus (modul evaluasi) yang menghasilkan output metrik Akurasi dan F1-Score sesuai desain. |
| System → Experiment | ✅ | Desain eksperimen menggunakan sistem sebagai instrumen utama untuk menjalankan model, memproses data, dan mengumpulkan metrik untuk analisis komparatif. |

**Koneksi mana yang paling lemah?** Koneksi antara System → Experiment.
**Bagaimana cara memperkuatnya?**
> Dengan memastikan detail teknis prapemrosesan citra (reduksi 64x64 piksel) sudah benar-benar sesuai dan efektif dalam mengurangi overfitting, serta memastikan konsistensi dalam 5 repeated runs yang direncanakan.

**Konsistensi horizontal — apakah istilah dan scope konsisten?** [x] Ya / [ ] Tidak
> Jika tidak, di bagian mana terjadi inkonsistensi? _________

---

## Latihan 3 — Rubrik Self-Assessment

Evaluasi proposal mini menggunakan rubrik.

| Kriteria | Skor (1-3) | Justifikasi |
|----------|-----------|-------------|
| Koherensi | 3 | Seluruh bagian proposal mengalir secara logis dari masalah keterbatasan data ke desain eksperimen perbandingan model. |
| Specificity | 3  Metrik (Akurasi dan F1-Score), model (VGG-19 vs DenseNet-169), dataset (710 citra), dan parameter teknis (reduksi 64x64 piksel) sudah terdefinisi secara spesifik dan numerik. |
| Feasibility | 3 | Sistem pipeline Python modular dan repeated runs komparatif mudah diimplementasikan dengan sumber daya yang ada dan timeline satu semester. |
| Rigor |2 | Rigor metodologi masih bisa ditingkatkan dengan penjelasan yang lebih mendalam mengenai penanganan overfitting lainnya selain reduksi ukuran citra, serta uji statistik inferensial yang lebih formal untuk membandingkan rata-rata metrik performa. |

**Skor total:** 11 / 12

**Apakah proposal siap untuk fase eksekusi?** [x] Ya / [ ] Belum
> Jika belum, apa yang perlu diperbaiki? __________________

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-08, bagian mana yang paling mudah dan paling sulit? Mengapa? Apa yang akan dilakukan berbeda jika mengulang dari awal?

**Bagian termudah:** Pengerjaan WS-01 (Distorsi Paradigma) dan WS-02 (Problem Statement) adalah bagian paling mudah karena fokusnya adalah pada pemahaman dasar tentang masalah yang akan diselesaikan dan penentuan topik yang relevan, tanpa memerlukan detail teknis yang kompleks.
**Bagian tersulit:** Pengerjaan WS-07 (Experiment Design) dan WS-08 (Proposal Integration) adalah bagian paling sulit karena harus menghubungkan seluruh komponen proposal menjadi satu argumen utuh yang logis dan konsisten, serta menyusun jadwal penelitian satu semester (16 minggu termasuk UTS dan UAS) ke dalam templat matriks 8 fase dua mingguan tanpa mengubah struktur aslinya. Hal ini membutuhkan perencanaan yang matang dan pemahaman yang mendalam mengenai alur pengerjaan Worksheet berdurasi satu semester.
**Yang akan dilakukan berbeda:**
> Lebih fokus pada pemahaman aliran logis antara masalah, gap, pertanyaan penelitian, metrik, dan desain eksperimen sejak awal, agar proses integrasi proposal menjadi lebih mudah dan tidak mengalami tumpang tindih pengerjaan tugas dua mingguan yang kompleks.
> Memastikan detail teknis metodologi seperti prapemrosesan reduksi ukuran citra sudah benar-benar sesuai dan efektif dalam menangani overfitting sebelum melangkah ke desain eksperimen repeated runs komparatif yang ketat.
