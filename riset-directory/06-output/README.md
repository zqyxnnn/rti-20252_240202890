## 06-output
Hasil olahan data, model, dan visualisasi komparatif arsitektur CNN (VGG19 vs DenseNet169) untuk klasifikasi penyakit daun padi.

## Struktur Direktori
Dihasilkan secara otomatis oleh 05-kode/run_stability_test.py dan dianalisis melalui 05-kode/klasifikasi_daun_padi.ipynb.

06-output/
├── figures/
│   └── fig_distribution_boxplot.png
├── tables/
│   ├── summary_statistics.csv
│   └── full_runs_log.csv
├── models/
│   └── (tempat simpan file .keras/.pkl jika perlu)
└── klasifikasi_daun_padi_executed.ipynb

Daftar File Output
1. Visualisasi (figures/)
- fig_distribution_boxplot.png: Perbandingan sebaran akurasi (VGG19 vs DenseNet169) untuk melihat stabilitas.
- fig_accuracy_trend.png: Line chart tren akurasi per random seed (menunjukkan apakah ada model yang performanya fluktuatif).
- fig_error_distribution.png: Histogram distribusi akurasi masing-masing model.

2. Tabel Hasil Eksperimen (tables/)
- summary_statistics.csv: Ringkasan mean, std, min, max akurasi dari 35 seed.
- t_test_results.csv: Log hasil T-Test (T-statistic dan P-value).
- full_runs_log.csv: Log lengkap 35 eksperimen (isi dari training_runs.csv yang sudah diformat rapi).

3. Model & Metadata (models/)
- vgg19_best_config.json: Konfigurasi parameter terbaik (jika ada).
- densenet169_best_config.json: Konfigurasi parameter terbaik.

4. Salinan Eksperimen (.ipynb)
- klasifikasi_daun_padi_executed.ipynb: Notebook Jupyter yang berisi seluruh alur kerja penelitian—mulai dari loading data, analisis statistik deskriptif, visualisasi perbandingan, hingga pengujian signifikansi (T-Test) dengan keluaran (output) yang sudah tereksekusi.