# WS-15: Scientific Writing

> **Bab 15 — Penulisan Ilmiah**

---

## Ringkasan Materi

### Scientific Argument Flow

```
Problem → Gap → RQ → Method → Result → Analysis → Conclusion → Contribution
```

Paper ilmiah adalah **satu argumen utuh** dari masalah ke kontribusi. Setiap node harus terhubung logis ke node sebelum dan sesudahnya.

### Struktur IMRAD

| Section | Peran | Pertanyaan Kunci |
|---------|-------|-----------------|
| **Introduction** | Motivasi + frame | Why is this needed? |
| **Method** | Deskripsi (reproducible) | How was it done? |
| **Results** | Laporan objektif | What was found? |
| **Discussion** | Interpretasi + refleksi | What does it mean? |
| **Conclusion** | Ringkasan + kontribusi | So what? |

### Logical Flow — "Red Thread"

Setiap paragraf menjawab satu pertanyaan dan memicu pertanyaan berikutnya. Alur logis ini harus terasa di tiga level:
1. **Antar-kalimat** dalam paragraf
2. **Antar-paragraf** dalam section
3. **Antar-section** dalam paper

### Internal Consistency

Setiap elemen yang dijanjikan di Introduction harus hadir di Discussion/Conclusion.

**Consistency Matrix:**
```
           Intro  Method  Result  Discuss  Conclude
RQ1          ✓      ✓       ✓       ✓        ✓
RQ2          ✓      ✓       ✓       ✗ ←      ✓
Metrik-X     ✗      ✗       ✓ ←     ✗        ✗
```
**Masalah:** RQ2 dibahas di semua bagian kecuali Discussion. Metrik-X muncul di Result tapi tidak diperkenalkan di Method.

### Writing Quality Triad

| Kualitas | Deskripsi | Contoh Buruk → Baik |
|----------|----------|---------------------|
| **Clarity** | Dipahami sekali baca | "Performa meningkat" → "Accuracy meningkat dari 85.3% ke 89.7%" |
| **Precision** | Istilah eksak, tanpa ambiguitas | "signifikan" → "signifikan secara statistik (p=0.003, d=1.2)" |
| **Conciseness** | Setiap kata menambah informasi | Hapus kalimat redundan, filler words |

### Urutan Penulisan yang Disarankan

1. **Method & Results** — paling stabil, tulis pertama
2. **Discussion** — interpretasi berdasarkan hasil
3. **Introduction** — frame sesuai temuan aktual
4. **Abstract & Conclusion** — terakhir

### Target Jumlah Kata

| Section | Target |
|---------|--------|
| Introduction | 500–700 |
| Related Work | 700–1000 |
| Method | 800–1200 |
| Results | 500–800 |
| Discussion | 600–900 |
| Conclusion | 200–400 |

### Jebakan Kognitif

1. "Lebih panjang = lebih lengkap" → conciseness lebih berharga
2. "Introduction harus ditulis pertama" → justru ditulis terakhir
3. "Jargon teknis = lebih ilmiah" → clarity lebih penting
4. "Discussion = ringkasan Results" → Discussion = interpretasi + konteks

---

## Template A.15 — Paper Structure Checklist

```
PAPER STRUCTURE CHECKLIST

Title   : Komparasi Kinerja Arsitektur VGG-19 dan DenseNet-169 pada Klasifikasi Citra Penyakit Daun Padi
Target  : [x] Jurnal  [ ] Konferensi  [ ] Laporan

Section Check:
  [x] Abstract — masalah, metode, hasil utama, kontribusi (max 250 kata)
  [x] Introduction — konteks → gap → RQ → kontribusi → struktur paper
  [x] Related Work — concept-centric, gap positioning
  [x] Method — reproducible: desain, variabel, metrik, setup, prosedur
  [x] Results — tabel + grafik + observasi (tanpa interpretasi)
  [x] Discussion — interpretasi, perbandingan, implikasi, limitation
  [x] Conclusion — jawaban RQ, kontribusi, future work

Consistency Matrix:
  [x] RQ di Introduction = RQ di Method = RQ di Conclusion
  [x] Variabel di Method = variabel di Results
  [x] Klaim di Discussion didukung data di Results
  [x] Limitasi di Discussion di-address di Conclusion/Future Work

Writing Quality:
  [x] Clarity — mudah dipahami tanpa re-read
  [x] Precision — tidak ada istilah ambigu
  [x] Conciseness — tidak ada kalimat redundan
```

---

## Latihan 1 — Paper Outline

Buat outline paper untuk riset Anda menggunakan struktur IMRAD.

| Section | Konten Utama (2-3 kalimat) | Target Kata |
|---------|---------------------------|------------|
| Abstract | Masalah: Penyakit daun padi menurunkan produktivitas. Metode: Komparasi VGG-19 dan DenseNet-169 dengan 35 iterasi. Hasil: Akurasi setara secara statistik ($p=0.7004$). Kontribusi: Bukti empiris efisiensi model. | 200-250 |
| Introduction | Konteks: Pentingnya deteksi penyakit padi. Gap: Belum ada konsensus performa arsitektur pada dataset terbatas. RQ: Apakah DenseNet-169 secara signifikan lebih unggul?. | 500-700 |
| Related Work | Tinjauan CNN dalam pertanian. Fokus pada feature reuse DenseNet vs sekuensial VGG dan gap penelitian pada dataset < 1000 citra. | 700-1000 |
| Method | Prosedur akuisisi dataset daun padi, preprocessing citra, arsitektur model, dan pengaturan training (35 runs). Penggunaan Independent T-Test untuk verifikasi signifikansi. | 800-1200 |
| Results | Pelaporan statistik deskriptif (mean, std) dan hasil uji t. Visualisasi box plot menunjukkan distribusi akurasi kedua model.| 500-800 |
| Discussion | Interpretasi: Performa setara karena saturation point fitur pada dataset kecil. Implikasi: Pemilihan model dapat didasarkan pada efisiensi, bukan sekadar kedalaman. | 600-900 |
| Conclusion | Jawaban RQ: Tidak ada perbedaan signifikan. Kontribusi: Validasi reliabilitas lewat multi-run. Future work: Optimasi resolusi/ViT. | 200-400 |

---

## Latihan 2 — Consistency Matrix

Buat consistency matrix untuk memverifikasi internal consistency paper Anda.

|  | Intro | Method | Result | Discussion | Conclusion |
|--|-------|--------|--------|-----------|-----------|
| *Contoh: RQ1* | *✓* | *✓* | *✓* | *✓* | *✓* |
| *Contoh: Metrik-X* | *✗ ←* | *✗ ←* | *✓* | *✗ ←* | *✗ ←* |
| RQ1 (Arsitektur) | *✓* | *✓* | *✓* | *✓* | *✓* |
| RQ2 (Stabilitas/Seed) | *✓* | *✓* | *✓* | *✓* | *✓* |
| Metrik utama | *✓* | *✓* | *✓* | *✓* | *✓* |
| Variabel IV | *✓* | *✓* | *✓* | *✓* | *✓* |
| Variabel DV | *✓* | *✓* | *✓* | *✓* | *✓* |
| Klaim/kontribusi | *✓* | *✓* | *✓* | *✓* | *✓* |

**Isi setiap sel:** ✓ (ada & konsisten), ✗ (missing), ~ (ada tapi inkonsisten)

**Inkonsistensi yang ditemukan:**
> KEkspektasi awal di proposal yang mengasumsikan DenseNet lebih superior (H1) tidak terbukti di hasil akhir.

**Tindakan perbaikan:**
> Merevisi Introduction dan Conclusion untuk menyajikan hasil ini sebagai kontribusi "hasil negatif" (negative result) yang berharga bagi literatur.

---

## Latihan 3 — Writing Quality Check

Ambil satu paragraf dari tulisan Anda (atau tulis paragraf baru) dan evaluasi kualitasnya.

**Paragraf asli:**
> "Metode VGG-19 sama DenseNet-169 ini dicoba buat klasifikasi penyakit daun padi, dan dari 35 kali eksperimen, kita bisa liat kalau hasilnya nggak beda jauh secara statistik, jadi milih salah satunya itu bisa tergantung kebutuhan hardware."  

| Kriteria | Evaluasi | Perbaikan |
|----------|---------|-----------|
| Clarity | Terlalu informal ("liat", "nggak beda jauh"). | Gunakan bahasa formal. |
| Precision | "Nggak beda jauh" ambigu. | Gunakan terminologi "tidak signifikan secara statistik". |
| Conciseness | Kalimat terlalu panjang. | Fokus pada hasil pengujian. |

**Paragraf setelah perbaikan:**
> Eksperimen komparatif melalui 35 iterasi menunjukkan bahwa arsitektur VGG-19 dan DenseNet-169 tidak memiliki perbedaan performa yang signifikan secara statistik dalam klasifikasi penyakit daun padi (p = 0.7004). Temuan ini mengindikasikan bahwa pemilihan arsitektur dapat disesuaikan dengan batasan sumber daya komputasi yang tersedia.

---

## Refleksi

> Apa perbedaan antara menulis "tentang" riset dan menulis sebagai "argumen" riset? Bagaimana urutan penulisan (Method → Discussion → Introduction) mengubah kualitas tulisan?

> Perbedaan menulis "tentang" riset vs "argumen" riset: Menulis "tentang" riset hanya melaporkan apa yang terjadi (deskriptif), sedangkan menulis "argumen" riset membangun narasi logis untuk menjawab Research Question dan meyakinkan pembaca akan validitas temuan Anda.
> Urutan penulisan (Method → Discussion → Introduction): Urutan ini krusial karena memastikan bahwa Introduction (bingkai penelitian) dibangun berdasarkan fakta hasil yang sudah valid, bukan berdasarkan ekspektasi awal, sehingga mencegah inkonsistensi argumen dalam paper.
