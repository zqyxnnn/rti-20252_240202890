# WS-01: Distorsi & Paradigma

> **Bab 1 — Research Mindset in IT**

---

## Ringkasan Materi

### Research Trust Model

Pengetahuan ilmiah tidak muncul langsung dari kenyataan. Ia melewati **6 tahap transformasi** yang masing-masing rawan distorsi:

```
Reality → Data → Processing → Analysis → Inference → Knowledge
```

Etika mencegah distorsi yang disengaja (fabrikasi, cherry-picking). Validitas mendeteksi distorsi yang tidak disengaja (confounding variable, sampling bias).

### Tiga Jenis Validitas

| Jenis | Pertanyaan | Contoh Ancaman |
|-------|-----------|----------------|
| **Internal Validity** | Apakah hubungan kausal benar ada? | Confounding variable |
| **External Validity** | Apakah bisa digeneralisasi? | Dataset terlalu homogen |
| **Construct Validity** | Apakah mengukur hal yang benar? | Metrik tidak sesuai klaim |

### Paradigma Riset

Mata kuliah ini menggunakan pendekatan **Positivist** (fenomena TI bisa diukur objektif melalui eksperimen terkontrol) diperkuat **Design Science Research** (artefak dibuat sebagai instrumen pengujian hipotesis, bukan tujuan akhir).

### Mode Berpikir Peneliti

**Curious** (mempertanyakan fenomena) → **Critical** (mengevaluasi klaim berdasarkan bukti) → **Systematic** (merancang investigasi terstruktur dan reproducible).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Membuat sistem yang bekerja | Menghasilkan pengetahuan yang valid |
| Pertanyaan khas | "Bagaimana membuatnya jalan?" | "Apakah klaim ini benar?" |
| Ukuran sukses | Sistem berfungsi, client puas | Hipotesis terjawab, temuan tervalidasi |
| Kegagalan | Harus dihindari | Harus dilaporkan (negative result = kontribusi) |

### Istilah Penting

- **Research Mindset** — Pola pikir yang menuntut bukti dan mempertanyakan asumsi
- **Research Ethics** — Prinsip perilaku: kejujuran, objektivitas, keterbukaan, akuntabilitas
- **HARKing** — Hypothesizing After Results are Known — merumuskan hipotesis setelah melihat data
- **Falsifiability** — Hipotesis harus bisa dibuktikan salah

---

## Template A.1 — Research Mindset Self-Assessment

```
Nama Peneliti    : Zakkya Fauzan Alba'asithu
Tanggal          : 19 April 2026

1. Ketika membaca klaim "metode X 95% akurat":
   - Pertanyaan pertama saya: Apakah akurasi tersebut diukur pada data yang seimbang atau apakah ada bias pada kelas mayoritas (misal: daun sehat lebih banyak dari daun sakit)?
   - Data yang dibutuhkan untuk verifikasi: Matriks konfusi (Confusion Matrix) untuk melihat False Negative dan detail distribusi dataset.
2. Posisi paradigma:
   - Pendekatan: [x] Positivis  [ ] Interpretivis  [ ] Design Science  [ ] Mixed
   - Alasan: Karena fokus riset adalah menciptakan artefak teknis berupa arsitektur CNN khusus untuk memecahkan masalah identifikasi penyakit padi secara otomatis.
3. Identifikasi distorsi:
   - Asumsi tersembunyi: Diasumsikan bahwa citra yang diambil di lapangan akan selalu memiliki kualitas dan pencahayaan yang sama dengan dataset Kaggle.
   - Sumber bias potensial : Ketidakseimbangan jumlah sampel per kelas (Hawar daun 220 vs Tungro 80).
   - Langkah mitigasi: Melakukan augmentasi data untuk menyeimbangkan jumlah sampel dan menguji model dengan data di luar dataset pelatihan.

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: Nilai akurasi pengujian dan jumlah data yang digunakan dalam proses training.
   - Batasan yang diakui sejak awal: Model ini mungkin mengalami penurunan performa jika dihadapkan pada varietas padi atau kondisi pencahayaan ekstrem yang tidak ada dalam dataset.
```

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

**Paper yang dipilih:**
> Judul: Klasifikasi Penyakit Padi Menggunakan Convolutional Neural Network (CNN) Berbasis Citra Daun
> Penulis (Tahun): Moh. Heri Susanto, Irwan Budi Santoso, Suhartono, Ahmad Fahmi Karami (2025)
> Sumber / Link DOI : Susanto, M. H., Santoso, I. B., Suhartono, & Karami, A. F. (2025). Klasifikasi Penyakit Padi Menggunakan Convolutional Neural Network (CNN) Berbasis Citra Daun. Jurnal Nasional Teknik Elektro dan Teknologi Informasi (JNTETI), 14(3), 181-190. / https://journal.ugm.ac.id/v3/JNTETI/article/download/18791/6072

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | Mengumpulkan 710 citra dari dataset publik Kaggle (Hawar daun, Blas, Tungro, Sehat). | Sampling Bias: Data berasal dari lingkungan terkontrol, bukan dari pengambilan langsung di berbagai sawah lokal secara acak. |
| Data → Processing | Mengubah ukuran citra menjadi 64 x 64piksel dan normalisasi nilai piksel. | Feature Loss: Pengurangan resolusi ke 64 x 64 dapat menghilangkan detail tekstur kecil pada bercak daun padi. |
| Processing → Analysis | Pengujian 8 skenario model (A1-B4) dengan variasi learning rate dan dropout. | Overfitting Bias: Terlalu banyak mencoba skenario pada satu dataset yang sama hingga menemukan angka tertinggi tanpa validasi silang eksternal. |
| Analysis → Inference | Menyimpulkan model B3 adalah yang terbaik dengan akurasi 0,9647 (96,47%). | Metric Bias: Akurasi tinggi mungkin menutupi kegagalan model pada kelas yang datanya sedikit (seperti Tungro). |
| Inference → Knowledge | Menyatakan model CNN sederhana kompetitif untuk klasifikasi penyakit padi. | Generalization Error: Klaim keunggulan metode mungkin tidak berlaku jika diterapkan pada aplikasi mobile di lapangan terbuka. |

**Distorsi paling besar di tahap:** Reality → Data

**Dua distorsi spesifik yang teridentifikasi:**
1. Data Imbalance: Jumlah data Tungro (80) jauh lebih sedikit dibanding Hawar Daun (220), sehingga model lebih condong mengenali ciri Hawar Daun.
2. Environment Bias: Penggunaan dataset sekunder (Kaggle) membuat model tidak teruji terhadap noise nyata seperti bayangan, tangan manusia, atau gangguan latar belakang sawah.

---

## Latihan 2 — Analisis Kasus Etika

Skenario: Penghapusan 3 data point outlier agar hasil menjadi signifikan.

| Perspektif | Analisis |
|------------|---------|
| Kejujuran ilmiah | Peneliti harus tetap menyertakan 3 outlier tersebut atau memberikan alasan teknis yang kuat mengapa data itu dibuang (misal: gambar rusak). |
| Transparansi | Dalam riset ini, jika ada gambar daun yang gagal diklasifikasi, harus dilaporkan agar diketahui kelemahan algoritma CNN tersebut.|
| Peer review | Reviewer membutuhkan data yang jujur untuk memastikan bahwa keunggulan model B3 bukan karena "keberuntungan" setelah membuang data yang sulit. |

**Keputusan akhir dan justifikasi:**
> Melaporkan hasil dengan dan tanpa outlier (Transparansi Penuh). Justifikasinya adalah objektivitas; dalam informatika, outlier seringkali merupakan kasus penting (edge cases) yang justru menentukan keandalan sistem saat diimplementasikan secara nyata.

---

## Latihan 3 — Posisi Paradigma

**Topik riset:** Klasifikasi Penyakit Padi dengan Arsitektur CNN Khusus

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian dengan topik (1–5) | 4 | 1 | 5 |
| Jenis data yang dikumpulkan | Akurasi, Loss, Precision, Recall. | Tidak ada (bukan data sosial). | Arsitektur Model, Konfigurasi Layer. |
| Hanya fokus pada angka, bukan penyebab di lapangan. | Tidak bisa menghasilkan solusi otomatis. | Terlalu subjektif, sulit dihitung efisiensinya. | Sangat bergantung pada kualitas dataset yang tersedia. |

**Paradigma yang dipilih:** Design Science
**Alasan:**Riset ini bertujuan untuk mengembangkan sebuah "artefak" (arsitektur model CNN yang dioptimasi) sebagai solusi untuk meningkatkan akurasi identifikasi penyakit tanaman padi secara otomatis.
---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> Sebelum membaca materi ini, saya sering menganggap klaim "95% akurat" sebagai bukti bahwa sistem sudah sempurna. Setelah memahami rantai distorsi, pertanyaan yang sekarang akan saya ajukan adalah "Bagaimana rasio distribusi data antar kelas?" dan "Apakah akurasi tersebut tetap bertahan jika model diuji dengan data dari perangkat kamera yang berbeda di luar dataset penelitian?"

