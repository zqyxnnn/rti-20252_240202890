# WS-05: Variabel & Metrik

> **Bab 5 — Metric, Measurement & Data**

---

## Ringkasan Materi

### Measurement Alignment Model

Setiap pengukuran yang valid harus bisa ditelusuri melalui rantai ini tanpa lompatan logis:

```
Problem → Concept → Variable → Metric → Data → Result
```

### Operationalization = Keputusan Desain

Menerjemahkan konsep abstrak menjadi variabel terukur bukan proses mekanis. "Code quality" yang diukur via SonarQube code smells membawa asumsi implisit. Setiap operasionalisasi harus didokumentasikan dan dijustifikasi.

### Empat Tipe Data (NOIR)

| Tipe | Ciri | Contoh | Operasi Valid |
|------|------|--------|---------------|
| **Nominal** | Kategori, tanpa urutan | Jenis algoritma (RF, SVM, CNN) | Modus, chi-square |
| **Ordinal** | Urutan, interval tidak sama | Skala Likert (1-5) | Median, Spearman |
| **Interval** | Jarak bermakna, tanpa nol absolut | Suhu Celsius | Mean, Pearson, t-test |
| **Ratio** | Jarak bermakna + nol absolut | Waktu eksekusi (ms) | Semua operasi |

Tipe data menentukan uji statistik yang valid. Kebanyakan metrik performa TI = ratio; persepsi pengguna = ordinal.

### Kriteria Pemilihan Metrik

- **Representative** — Mewakili konsep yang diteliti
- **Sensitive** — Cukup peka menangkap perbedaan bermakna (hindari ceiling effect)
- **Feasible** — Bisa dikumpulkan dalam batasan waktu dan biaya

### Pre-registration

Metrik harus ditentukan **sebelum** eksperimen. Memilih metrik setelah melihat data = **p-hacking**. Metrik tambahan yang ditemukan kemudian dilaporkan sebagai *exploratory*, bukan *confirmatory*.

### Primary vs Secondary Metric

- **Primary Metric** — Langsung terikat ke hipotesis, menentukan kesimpulan
- **Secondary Metric** — Pendukung, dilaporkan di samping primary; statusnya suplementer

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Pemilihan metrik | Berdasarkan kebiasaan/tool yang ada | Berdasarkan construct validity |
| Anomali | Dihapus untuk laporan bersih | Diinvestigasi — bisa jadi temuan |
| Kapan dipilih | Setelah sistem jadi (monitoring) | Sebelum eksperimen (by design) |

### Istilah Penting

- **Operationalization** — Transformasi konsep abstrak menjadi variabel terukur
- **Construct Validity** — Sejauh mana pengukuran benar-benar mengukur konsep yang dimaksud
- **Measurement Scale** — Klasifikasi data (NOIR) yang menentukan analisis valid
- **Multi-metric Evaluation** — Menggunakan beberapa metrik untuk menangkap konsep kompleks

---

## Template A.5 — Definisi Variabel, Metrik & Justifikasi

```
VARIABLE & METRIC DEFINITION

Research Question:  Apakah DenseNet-169 menghasilkan akurasi lebih tinggi dibandingkan VGG-19 pada klasifikasi penyakit daun padi?

| Variabel | Tipe | Konsep | Metrik | Skala | Satuan | Cara Mengukur | Justifikasi |
|----------|------|--------|--------|-------|--------|---------------|-------------|
| Jenis model CNN | IV | Pendekatan klasifikasi | DenseNet-169 vs VGG-19 | Nominal | — | Menggunakan dua arsitektur berbeda pada dataset yang sama | Mewakili perbedaan metode yang diuji |
| Akurasi klasifikasi | DV | Performa model | Accuracy | Ratio | % | (jumlah prediksi benar / total data) × 100 | Langsung menggambarkan performa model |
| Dataset (jumlah & augmentasi) | CV | Variasi data | Jumlah data & teknik augmentasi | ratio | jumlah citra | Menentukan jumlah data latih & augmentasi yang digunakan | Mengontrol pengaruh data terhadap hasil |

Alignment Check:
  RQ → Concept → Variable → Metric → Data → Result
  [x] Setiap langkah terdokumentasi
  [x] Tidak ada "lompatan logis"
  [x] Metrik mengukur apa yang dimaksud (construct validity)
```

---

## Latihan 1 — Operationalization Chain

Gunakan RQ dari WS-04. Definisikan variabel dan metriknya.

**RQ:** Apakah DenseNet-169 menghasilkan akurasi lebih tinggi dibandingkan VGG-19 pada klasifikasi penyakit daun padi?

| Variabel | Tipe | Konsep Abstrak | Metrik Konkret | Skala (NOIR) | Satuan |
|----------|------|---------------|----------------|-------------|--------|
| Jenis model | IV | Metode klasifikasi | DenseNet-169 vs VGG-19 | Nominal | — |
| Performa model | DV | Kinerja klasifikasi | Accuracy | Ratio | % |
| Dataset | CV | Kualitas & jumlah data | Jumlah citra & augmentasi | Ratio | jumlah |

**Apakah ada lompatan logis dalam rantai?** [ ] Ya / [x] Tidak
> Jika ya, di mana? ____________________________________

---

## Latihan 2 — Evaluasi Metrik

Evaluasi metrik DV yang dipilih di Latihan 1 menggunakan 3 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Representative | 4 | Accuracy cukup mewakili performa model klasifikasi |
| Sensitive | 3 | Kurang sensitif kalau data tidak seimbang (class imbalance) |
| Feasible | 5 | Mudah dihitung dan umum digunakan |

**Apakah perlu secondary metric?** [x] Ya / [ ] Tidak
> Jika ya, apa dan mengapa? F1-Score, karena bisa menangkap keseimbangan antara precision dan recall, terutama kalau dataset tidak seimbang.

**Contoh kasus ceiling effect untuk metrik ini:**
> Kalau dataset terlalu mudah (misalnya citra jelas semua), akurasi bisa tinggi semua (>95%) sehingga sulit membedakan model mana yang benar-benar lebih baik.

---

## Latihan 3 — Data Quality Check

Bayangkan data yang akan dikumpulkan dari eksperimen. Evaluasi 4 dimensi kualitas data.

| Dimensi | Pertanyaan | Jawaban | Strategi Mitigasi |
|---------|-----------|---------|------------------|
| Completeness | Apakah semua data point terkumpul? | Belum tentu, karena dataset terbatas | Tambah data atau gunakan augmentasi |
| Consistency | Apakah ada kontradiksi internal? | Bisa terjadi karena perbedaan label |Validasi ulang label dataset |
| Validity | Apakah benar-benar mengukur yang dimaksud? | Cukup valid karena pakai citra nyata | Gunakan data yang sudah diverifikasi |
| Representativeness | Apakah sampel mewakili populasi target? | Belum sepenuhnya | Ambil data dari berbagai kondisi (cahaya, lokasi)|

---

## Refleksi

> Mengapa memilih metrik setelah melihat data dianggap p-hacking? Apa bedanya dengan eksplorasi data yang sah?

**Jawaban:**
> Memilih metrik setelah melihat data itu disebut p-hacking karena kita bisa “milih” metrik yang paling menguntungkan hasil kita. Jadi hasilnya kelihatan bagus, tapi sebenarnya nggak objektif dari awal.
> Bedanya sama eksplorasi data yang sah itu di niat dan tahapnya. Kalau eksplorasi, metrik tambahan dilaporkan sebagai temuan tambahan, bukan buat membuktikan hipotesis utama. Jadi tetap jujur kalau itu bukan bagian dari rencana awal.