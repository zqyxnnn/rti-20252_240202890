# Tahap 4 — Ekstraksi Data & Visualisasi

**Status:** Selesai — pipeline analisis telah dijalankan pada seluruh data dari 70 run (35 VGG-19, 35 DenseNet-169), tabel & figure tersedia di ../06-output/tables/ dan ../06-output/figures/.
**Bergantung pada:** [tahap-3-stabilitas-eksperimen.md](tahap-3-stabilitas-eksperimen.md)
**Lokasi kode:** [../05-kode/analysis](../05-kode/analysis)

---

## Tujuan

Mengolah data hasil eksperimen (../06-output/) menjadi analisis statistik yang komprehensif untuk memvalidasi perbedaan performa antara arsitektur VGG-19 dan DenseNet-169, serta membuktikan bahwa perbedaan tersebut bersifat signifikan secara saintifik (bukan karena stochastic fluke).

## Deliverable

- [x] Pipeline Analisis: Skrip analyze_results.py untuk mengolah full_runs_log.csv menjadi tabel statistik deskriptif dan inferensial.
- [x] Statistik Deskriptif: Perhitungan Mean, Median, Standar Deviasi, Min, dan Max akurasi untuk tiap arsitektur.
- [x] Uji Signifikansi (Wilcoxon Signed-Rank Test): Implementasi uji beda non-parametrik untuk menentukan apakah performance gap antara VGG-19 dan DenseNet-169 signifikan secara statistik (p < 0.05).
- [x] Visualisasi Data:
    - Boxplot perbandingan distribusi akurasi (menunjukkan sebaran hasil dari 35 run).
    - Line Plot perbandingan akurasi per-run (memperlihatkan konsistensi/stabilitas).
    - Histogram sebaran error (untuk melihat profil outlier pada tiap model).
- [x] Ringkasan Tabel: Tabel akhir yang siap masuk ke dalam bab "Results & Discussion" di jurnal target.

## Desain yang Diimplementasikan

### Struktur kode (`05-kode/analysis/`)

```
05-kode/analysis/
└── run_analysis.py          # Master script: memuat data, uji statistik, visualisasi

### Prosedur Analisis
Analisis dilakukan melalui skrip run_analysis.py dengan langkah-langkah:
1. Agregasi Data: Membaca data raw dari 06-output/tables/full_runs_log.csv.
2. Statistik Deskriptif: Menghitung Mean, Median, Standar Deviasi, Min, dan Max akurasi untuk masing-masing arsitektur. Hasil disimpan ke summary_statistics.csv.
3. Visualisasi: Membuat boxplot perbandingan distribusi akurasi untuk melihat sebaran performa dan konsistensi dari 35 run tersebut. Hasil disimpan ke 06-output/figures/.

## Hasil

### Tabel Perbandingan Performa

| metrik | VGG-19 (35 run) | DenseNet-169 (35 run) | 
|---|---|---|
| Mean Akurasi | 84.90% | 84.50% | 
| Std. Deviasi | 4.544 | 4.215 | 
| Median | 83.61 | 85.03 |

### Catatan untuk Tahap 5

- Interpretasi Performa: Meskipun VGG-19 mencatatkan mean akurasi sedikit lebih tinggi (84.91% vs 84.50%), perbedaan tersebut secara statistik tidak signifikan (p = 0.7004). Hal ini menunjukkan bahwa untuk klasifikasi penyakit daun padi pada dataset ini, kedua arsitektur memiliki efektivitas yang setara.
- Analisis Stabilitas: Perhatikan bahwa DenseNet-169 memiliki median yang lebih tinggi (85.03% vs 83.61%) dan standar deviasi yang lebih rendah (4.22% vs 4.54%). Dalam konteks precision agriculture, hasil ini dapat didiskusikan sebagai indikasi bahwa DenseNet-169 memberikan prediksi yang lebih reliabel (lebih konsisten) dibandingkan VGG-19, meskipun secara rata-rata keduanya mirip.
- Implikasi Saintifik: Dengan nilai $p > 0.05$, kita dapat menyatakan bahwa pemilihan antara VGG-19 dan DenseNet-169 tidak didasarkan pada keunggulan mutlak akurasi, melainkan bisa didasarkan pada pertimbangan lain seperti efisiensi komputasi atau kompleksitas model.
- Poin Diskusi: Di bagian pembahasan, Anda bisa menyoroti mengapa terjadi anomali (VGG-19 memiliki mean lebih tinggi namun median lebih rendah dari DenseNet). Hal ini biasanya disebabkan oleh sebaran data yang tidak simetris (skewed) atau adanya outlier pada performa VGG-19.
