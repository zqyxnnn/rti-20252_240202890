# Tahap 5 — Penulisan Draf Paper Jurnal

**Status:** Selesai
**Bergantung pada:** [tahap-4-ekstrasi-data-&-visualisasi.md](tahap-4-ekstrasi-data-&-visualisasi.md) — *Selesai*

---

## Tujuan

Menyusun naskah ilmiah yang merefleksikan hasil eksperimen aktual: VGG-19 (Mean: 84.91%) dan DenseNet-169 (Mean: 84.50%) dengan $p$-value 0.7004 (tidak signifikan secara statistik).

## Rencana Deliverable (Struktur Naskah)

| Bagian | File | Status |
|---|---|---|
| Naskah konsolidasi (template jurnal) | [../07-manuskrip/naskah-jurnal.md](../07-manuskrip/naskah-jurnal.md) | Selesai — gabungan §1–§5 + Daftar Pustaka |
| Laporan Hasil & Latar Belakang | [../08-laporan/laporan-penelitian.md](../08-laporan/laporan-penelitian.md) | Selesai |

## Catatan

- Metodologi: Mendokumentasikan desain eksperimen komparatif antara VGG-19 dan DenseNet-169, mencakup proses augmentasi data, konfigurasi training dengan 35 kali pengulangan (repeated measures) untuk setiap arsitektur, serta penggunaan metrik akurasi sebagai tolok ukur utama.
- Hasil & Pembahasan: Mengintegrasikan rekapitulasi statistik deskriptif (mean ± std, median) dari 35 run untuk mengevaluasi akurasi dan stabilitas model. Analisis performa dilakukan melalui perbandingan sebaran data (boxplot) untuk memberikan justifikasi objektif mengenai konsistensi model dalam menangani variasi inisialisasi bobot.
- Daftar Pustaka: Mengacu pada sitasi standar terkait arsitektur Convolutional Neural Network (CNN) dan studi perbandingan performa model deep learning dalam klasifikasi citra pertanian/penyakit tanaman.
