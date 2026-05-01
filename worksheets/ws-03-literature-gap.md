# WS-03: Literature Mapping & Gap

> **Bab 3 — Literature Review, Research Gap & Baseline**

---

## Ringkasan Materi

### Literature Review = Positioning, Bukan Ringkasan

Literature review bukan merangkum paper satu per satu. Pendekatan yang benar adalah **concept-centric** — organisasi berdasarkan tema, metode, atau variabel. Tujuan: menemukan **pola, kontradiksi, dan gap**.

### Empat Jenis Research Gap

| Jenis Gap | Deskripsi | Contoh |
|-----------|----------|--------|
| **Performance Gap** | Performa belum memadai | Akurasi deteksi hanya 78% pada kasus tertentu |
| **Method Gap** | Pendekatan belum diterapkan | Belum ada yang pakai transformer untuk task ini |
| **Data Gap** | Dataset terbatas/tidak representatif | Semua studi pakai dataset sintetis |
| **Context Gap** | Belum diuji pada konteks berbeda | Belum ada evaluasi di negara berkembang |

Gap terkuat = kombinasi 2+ jenis.

### Systematic Search Strategy

1. **Database**: IEEE Xplore, ACM DL, Scopus, Google Scholar
2. **Boolean query** yang terdokumentasi eksplisit
3. **Snowballing**: backward (telusuri referensi) + forward (cari yang mengutip)
4. Klaim "belum ada penelitian" harus didukung **bukti pencarian**

### Baseline Selection — 3 Kriteria

| Kriteria | Pertanyaan |
|----------|-----------|
| **Relevan** | Apakah menyelesaikan masalah yang sama? |
| **Representatif** | Apakah mewakili common practice? |
| **State-of-the-Art** | Apakah terbaru/terbaik? |

Membandingkan deep learning 2024 dengan decision tree sederhana tanpa justifikasi = **straw man comparison** (perbandingan tidak jujur).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan baca literatur | Mencari solusi yang sudah ada | Memahami apa yang belum terjawab |
| Cara membaca paper | Tutorial, how-to | Metode, limitasi, gap |
| Baseline | Framework terpopuler | State-of-the-art yang rigorous |
| Dokumentasi pencarian | Tidak diperlukan | Wajib (reproducible) |

### Istilah Penting

- **Concept-centric** — Organisasi literatur berdasarkan konsep/metode, bukan per penulis
- **Snowballing** — Backward (telusuri referensi) + Forward (cari yang mengutip paper kunci)
- **Research Position** — Pernyataan eksplisit posisi riset terhadap studi sebelumnya
- **Straw man comparison** — Memilih baseline lemah agar metode sendiri terlihat lebih baik

---

## Template A.3 — Literature Mapping & Gap Identification

```
LITERATURE MAPPING

Topik      : Klasifikasi Penyakit Daun Padi Menggunakan Deep Learning
Database   : Google Scholar, Jurnal Ilmiah Sinus, & Repositori UMA
Query      : Rice leaf disease classification deep learning EfficientNet MobileNet DenseNet
Tahun      : 2021 – 2025
Hasil awal : 10 paper → Screening → 5 paper final

Literature Matrix (concept-centric):

| Study | Tahun | Method | Data | Result | Limitation |
|-------|-------|--------|------|--------|------------|
| Anggiratih et al. | 2021 | EfficientNet B3 + Transfer Learning | 857 citra (brown spot, bacterial leaf) | Akurasi: 79.53%, Loss: 0.012 | Dataset kecil, hanya 2 kelas penyakit |
| Muhammad Yazid | 2024 | DenseNet-169 + Grid/Random Search | 240 citra (blight, blast, tungro) | Akurasi: 93% (grid search) | Dataset sangat kecil, tidak ada kelas healthy |
| Moh. Heri Susanto | 2025 | Custom CNN (4 conv layers) | 710 citra (blast, blight, tungro, healthy) | Akurasi: 96.47%, F1: 96.47% | Arsitektur sederhana, tidak menggunakan transfer learning |
| Imam Fauzi Annur | 2023 | MobileNetV2 + Transfer Learning | 300 citra tingkat keparahan leafblast | Akurasi: 78.33% | Akurasi rendah, dataset kecil, fokus hanya satu penyakit |
| Rahma Shinta | 2023 | VGG-19 + Hyperparameter Optimization | 440 citra (blast, brown spot, leaf smut, healthy) | Akurasi: 94.31% (dengan augmentasi) | Overfitting pada beberapa eksperimen |

Pola yang ditemukan:
  Metode dominan     : CNN dengan berbagai arsitektur (EfficientNet, DenseNet, MobileNetV2, VGG-19, Custom CNN)
  Dataset umum       : 240-857 citra dengan 2-4 kelas penyakit padi
  Limitasi berulang  : Dataset kecil, overfitting, keterbatasan jenis penyakit yang diklasifikasi

GAP IDENTIFICATION

Gap 1: [Jenis: data / performance]
  Deskripsi    : Ukuran dataset yang konsisten kecil (240-857 citra) namun menghasilkan akurasi tinggi yang berpotensi misleading
  Bukti        : Muhammad Yazid (240 citra → 93%), Imam Fauzi (300 citra → 78.33%), menunjukkan inkonsistensi performa vs ukuran data
  Signifikansi : Dataset kecil dapat menyebabkan overfitting dan generalisasi yang buruk pada kondisi real-world

Gap 2: [Jenis: method]
  Deskripsi    : Belum ada standarisasi arsitektur CNN optimal untuk klasifikasi penyakit padi
  Bukti        : Custom CNN (96.47%) > VGG-19 (94.31%) > DenseNet-169 (93%) > EfficientNet B3 (79.53%) > MobileNetV2 (78.33%)
  Signifikansi : Perlu penelitian sistematis untuk menentukan arsitektur yang konsisten optimal

Baseline Selection:
| Baseline | Relevansi | Representatif | Source |
|----------|-----------|---------------|--------|
| EfficientNet B3 | Tinggi (model modern) | Cukup representatif  | https://p3m.sinus.ac.id/jurnal/index.php/e-jurnal_SINUS/article/view/526 |
| DenseNet-169 | Tinggi (akurasi tinggi) | Sangat representatif | https://repositori.uma.ac.id/jspui/handle/123456789/25314 |
| VGG-19 |Tinggi (banyak dipakai) | Representatif klasik | https://repository.uin-suska.ac.id/71163/1/RAHMA%20SHINTA%2011950125168%20REPOSITORY.pdf |
```

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan Google Scholar atau database lain.

**Topik riset:** Klasifikasi Penyakit Daun Tanaman Padi berbasis Deep Learning
**Query pencarian:** klasifikasi penyakit daun padi CNN deep learning
**Database:** Google Scholar & Repository Kampus

| # | Study | Tahun | Method | Dataset | Result | Limitasi |
|---|-------|-------|--------|---------|--------|----------|
| 1 | Anggiratih et al. | 2021 | CNN (EfficientNet B3) | 857 citra, 2 kelas | Akurasi 79.53% | Kelas sedikit, performa belum tinggi |
| 2 | Muhammad Yazid | 2024 | CNN (DenseNet-169 + tuning) | 240 citra, 4 kelas | Akurasi 93% | Data asli kecil, bergantung augmentasi |
| 3 | Susanto | 2025 | CNN (Custom) | Citra daun padi | Akurasi bervariasi| Belum pakai pretrained model |
| 4 | Annur et al. | 2023 | CNN (MobileNetV2) | 300 citra | Akurasi 78.33% | Dataset kecil, akurasi rendah |
| 5 | Shinta | 2023 | 440 + 1320 augmentasi | Akurasi 94.31% | Sangat bergantung augmentasi & tuning |

**Pola yang terlihat — Metode dominan:** CNN (deep learning) dengan berbagai arsitektur (VGG, DenseNet, EfficientNet, MobileNet)
**Limitasi yang berulang:** dataset kecil, sering butuh augmentasi, dan jumlah kelas terbatas

---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap | Ditemukan? | Gap Statement |
|-----------|-----------|---------------|
| Performance Gap | [x] Ya / [ ] Tidak | Beberapa model masih punya akurasi di bawah 80%, terutama pada dataset kecil |
| Method Gap | [x] Ya / [ ] Tidak | Mayoritas penelitian hanya fokus ke satu arsitektur CNN tanpa eksplorasi metode lain atau kombinasi model |
| Data Gap | [x] Ya / [ ] Tidak | Dataset yang digunakan relatif kecil dan kurang variatif |
| Context Gap | [ ] Ya / [x] Tidak | Fokus penelitian masih di konteks yang sama (citra daun padi) |

**Gap utama yang dipilih:** Data Gap
**Mengapa gap ini penting (bukan sekadar "belum ada yang meneliti")?**
> Kalau datanya sedikit, model jadi gampang overfitting. Di penelitian memang kelihatan akurasinya tinggi, tapi belum tentu kuat kalau dipakai di kondisi nyata (misalnya foto di lapangan dengan pencahayaan beda, daun rusak, dll). Jadi masalahnya bukan cuma datanya sedikit, tapi efeknya ke performa model di dunia nyata juga cukup besar.

---

## Latihan 3 — Baseline Selection

Pilih 2 baseline dari literatur yang sudah dibaca.

| # | Baseline | Mengapa Relevan | Mengapa Representatif | Apakah SOTA? | Sumber |
|---|----------|----------------|----------------------|-------------|--------|
| 1 | DenseNet-169 |Sama-sama klasifikasi citra penyakit padi | Dipakai pada 1 dari 5 paper dengan performa tinggi | Bukan SOTA, tapi kuat | Muhammad Yazid, 2024 |
| 2 | VGG-19 | Banyak dipakai di klasifikasi citra | Digunakan dalam penelitian CNN klasik dan muncul di 1 dari 5 paper | Shinta, 2023 |

**Apakah pemilihan baseline ini bisa dianggap straw man?** [ ] Ya / [x] Tidak
> Justifikasi: Baseline yang dipilih bukan model yang lemah atau asal-asalan. Dua-duanya sudah terbukti dipakai di penelitian sebelumnya dan punya performa yang cukup bagus. Jadi masih fair buat dijadikan pembanding.

---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
> Beda antara “belum ada yang meneliti ini” sama research gap yang valid itu ada di buktinya. Kalau cuma bilang belum ada yang meneliti, itu asumsi doang dan belum tentu benar. Bisa aja sebenarnya sudah ada, tapi kita belum nemu.

Kalau research gap yang valid, biasanya kelihatan dari pola di beberapa paper. Misalnya di kasus ini, hampir semua penelitian pakai dataset kecil. Dari situ bisa ditarik kesimpulan kalau ada masalah yang sama berulang.

Cara ngebuktiin gap itu ada yang dengan cara bandingin beberapa penelitian, terus cari pola yang sama. Jadi bukan cuma satu paper, tapi dilihat secara keseluruhan. Dari situ baru kelihatan mana yang masih kurang dan bisa dijadiin peluang penelitian.
> ___________________________________________________
