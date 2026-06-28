# Rencana Penelitian: Analisis Komparatif Performa Arsitektur Deep Learning VGG-19 dan DenseNet-169 dalam Klasifikasi Penyakit Daun Padi
## 1. Ringkasan

| Item | Keterangan |
|---|---|
| Judul | Analisis Komparatif Performa Arsitektur Deep Learning VGG-19 dan DenseNet-169 dalam Klasifikasi Penyakit Daun Padi |
| Target Publikasi | Sinta 2 (Jurnal Riset Teknologi Informasi) |
| Stack | Python, TensorFlow/Keras, VS Code, Git, Wilcoxon Statistical Test |
| Masalah | Ketidakpastian stabilitas model (stochastic fluke) pada klasifikasi citra penyakit tanaman akibat inisialisasi bobot acak (single run bias) |
| Solusi | Eksperimen iteratif 35 run terkontrol dengan variasi random seed + validasi statistik menggunakan Wilcoxon Signed-Rank Test |

## 2. Alur Kerja (Roadmap)

Setiap tahap memiliki file rencana detail tersendiri agar lebih rapi:

- [x] **Tahap 1** — [Pengumpulan Data & Preprocessing](tahap-1-pengumpulam-&-preprocessing-data-citra-daun-padi.md) — *Selesai*
- [x] **Tahap 2** — [Implementasi Arsitektur VGG-19 & DenseNet-169](tahap-2-implementasi-arsitektur-VGG-19-&-densenet-169.md) — *Selesai*
- [x] **Tahap 3** — [Otomasi Eksperimen 35x Run](tahap-3-stabilitas-eksperimen.md) — *Selesai*
- [x] **Tahap 4** — [Ekstraksi Data & Visualisasi](tahap-4-ekstrasi-data-&-visualisasi.md) — *Selesai*
- [ ] **Tahap 5** — [Penulisan Draf Paper Jurnal]

---

## 3. Catatan

Dokumen ini adalah indeks utama. Detail teknis, skema, dan keputusan masing-masing tahap dicatat pada file tahap-N-*.md terkait. Eksperimen ini dijalankan secara terotomatisasi sebanyak 35 kali menggunakan seed acak dinamis (43 s.d. 77) untuk menjamin reliabilitas statistik dan memitigasi stochastic fluke. Seluruh metrik kinerja, visualisasi plot, dan model biner disimpan secara terstruktur di folder 06-output/.
