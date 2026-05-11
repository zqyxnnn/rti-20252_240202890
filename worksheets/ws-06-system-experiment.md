# WS-06: System-Experiment Mapping

> **Bab 6 — System Design sebagai Experimental Artifact**

---

## Ringkasan Materi

### Sistem = Instrumen Pengujian, Bukan Produk

Seorang engineer bertanya "apakah sistem bekerja?" — seorang peneliti bertanya "apa yang bisa dibuktikan sistem ini?" Sistem dalam riset adalah **artifact** — objek yang sengaja dibuat untuk menguji klaim spesifik.

### System as Experiment Model

```
RQ → Variable → System Component → Experimental Setup → Output
```

Setiap komponen sistem harus bisa ditelusuri ke variabel riset (top-down), dan setiap pengukuran harus menjawab RQ (bottom-up).

### Mapping Variabel ke Komponen

| Tipe Variabel | Peran di Sistem | Contoh |
|---------------|----------------|--------|
| **IV** (Independent) | Modul yang bisa di-toggle/swap | Algoritma A vs B |
| **DV** (Dependent) | Modul pengukuran | Logger, metrics collector |
| **CV** (Control) | Config yang dikunci | Dataset, parameter tetap |

Jika variabel tidak bisa di-map ke komponen apapun → arsitektur perlu didesain ulang.

### 4 Prinsip Desain Eksperimental

| Prinsip | Pertanyaan Kunci |
|---------|-----------------|
| **Traceability** | Komponen ini melayani variabel yang mana? |
| **Modularity** | Bisakah IV diubah tanpa memengaruhi yang lain? |
| **Controllability** | Apakah CV dieksternalisasi ke config file? |
| **Measurability** | Apakah sistem otomatis menghasilkan data yang dibutuhkan? |

### Variable Isolation melalui Arsitektur

- **Modular architecture** — Pisahkan berdasarkan variabel
- **Configuration-driven** — Ubah config (YAML/JSON), bukan code
- **Feature toggles** — On/off flag untuk ablation study

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan sistem | Memenuhi kebutuhan user | Menguji hipotesis, menghasilkan bukti |
| Arsitektur | Optimasi performa & skalabilitas | Optimasi isolasi variabel & reprodusibilitas |
| Konfigurasi | Sering hardcoded | Dieksternalisasi ke config file |
| Fitur tambahan | Menambah nilai user | Menambah noise jika tidak terkait RQ |

### Istilah Penting

- **Artifact** — Objek yang sengaja dibuat untuk memecahkan masalah atau menguji proposisi
- **Traceability** — Kemampuan menelusuri hubungan RQ → variabel → komponen → output
- **Variable Isolation** — Mengubah hanya satu variabel sambil menahan yang lain konstan
- **Ablation Study** — Menguji kontribusi tiap komponen dengan melepasnya satu per satu
- **Configuration-driven Execution** — Semua parameter di config file, bukan hardcoded

---

## Template A.6 — Mapping RQ ke Arsitektur Sistem

```
SYSTEM-EXPERIMENT MAPPING

Research Question: ____________________

Variable → Component Mapping:
| Variabel | Tipe | Komponen Sistem | Cara Manipulasi/Pengukuran |
|----------|------|-----------------|---------------------------|
| Jenis Model CNN | IV | Model Loader / Classifier Module | Mengganti instance class model (DenseNet169 vs VGG19) via config |
| Akurasi & F1-Score| DV | Evaluation Module / Logger | Menghitung prediksi vs ground truth di akhir tahap testing |
| Dataset & Augmentasi | CV | Data Loader / Preprocessing Pipe | Mengunci source folder dataset dan seed untuk random augmentation |

4 Prinsip Desain:
  [x] Traceability — Setiap komponen bisa ditelusuri ke variabel
  [x] Variable Isolation — IV bisa diubah tanpa mengubah CV
  [x] Measurement Integration — Pengukuran DV built-in
  [x] Reproducibility — Setup bisa direkonstruksi

Experimental Setup:
  Input data     : 710 citra penyakit padi (Kaggle) yang sudah di-resize.
  Parameter      : Learning rate 0.001, Batch size 32, Epoch 50.
  Output format  : Confusion Matrix (Image) & Performance Metrics (CSV).
```

---

## Latihan 1 — Variable-to-Component Mapping

Gunakan RQ dan variabel dari WS-05. Petakan ke komponen sistem.

**RQ:** Apakah DenseNet-169 menghasilkan akurasi lebih tinggi dibandingkan VGG-19 pada klasifikasi penyakit daun padi?

| Variabel | Tipe | Komponen Sistem | Cara Manipulasi / Pengukuran |
|----------|------|-----------------|---------------------------|
| Jenis Arsitektur | IV | Modul Arsitektur (Python Class) | Swap antara models.densenet169 dan models.vgg19 melalui variabel selected_model. |
| Akurasi Klasifikasi | DV | Metric Collector | Menggunakan fungsi accuracy_score dari library Scikit-Learn pada output layer. |
| Hyperparameter (LR, Epoch) | CV | Config Manager (YAML/JSON) | Nilai di-hardcoded dalam file config.yaml agar tidak berubah selama eksperimen. |

**Apakah semua variabel bisa di-map?** [x] Ya / [ ] Tidak
> Jika tidak, komponen apa yang perlu ditambahkan? _________

---

## Latihan 2 — 4 Prinsip Desain

Evaluasi desain sistem terhadap 4 prinsip.

| Prinsip | Status | Bukti / Penjelasan |
|---------|--------|-------------------|
| Traceability | ✅ Berhasil | Perubahan pada hasil (Output) bisa dilacak langsung ke perubahan model (IV) di log eksperimen. |
| Modularity | ✅ Berhasil | Modul Preprocessing terpisah dari Modul Model, ganti model tidak perlu ganti cara resize gambar. |
| Controllability | ✅ Berhasil | Semua parameter seperti learning rate dikumpulkan di satu file config, bukan tersebar di kode. |
| Measurability | ✅ Berhasil | Sistem otomatis menyimpan file results.csv setiap kali satu skenario training selesai. |

**Prinsip mana yang paling sulit dipenuhi?** Controllability.
**Strategi untuk mengatasinya:**
> Menggunakan library seperti Hydra atau Argparse di Python agar semua parameter eksperimen harus dilewatkan melalui perintah eksekusi, sehingga meminimalkan adanya parameter tersembunyi (hidden variables).

---

## Latihan 3 — Ablation Study Planning

Jika sistem memiliki 3 komponen utama, rencanakan ablation study.

| Kondisi | Komponen A | Komponen B | Komponen C | Hasil yang Diharapkan |
|---------|-----------|-----------|-----------|----------------------|
| Full | ✅ Pakai Weights ImageNet | ✅ Rotate, Flip, Zoom | ✅ Dropout 0.5 | Baseline akurasi tertinggi |
| – A | ❌ (Training dari nol) | ✅ | ✅ | Akurasi turun drastis (butuh data lebih banyak) |
| – B | ✅ | ❌ (Data asli saja) | ✅ | Model kemungkinan overfitting |
| – C | ✅ | ✅ | ❌ (Tanpa Dropout) | Kesenjangan akurasi Train vs Test melebar |

**Komponen mana yang diprediksi paling berkontribusi?** Komponen A (Transfer Learning).
**Mengapa?**
> Karena dataset yang digunakan kecil (710 gambar). Tanpa pengetahuan awal dari ImageNet (Transfer Learning), model CNN akan kesulitan mengenali fitur kompleks hanya dari beberapa ratus gambar daun.

---

## Refleksi

> Apa risiko jika sistem dibangun seperti produk (monolitik, fitur lengkap) lalu baru dilakukan eksperimen? Mengapa arsitektur modular penting untuk riset?

**Jawaban:**
> Risikonya adalah Confounding Variables. Jika sistem monolitik, saat akurasi rendah, kita sulit menentukan apakah penyebabnya adalah algoritma yang buruk, preprocessing yang salah, atau data yang kotor karena semuanya menyatu.
> Arsitektur modular penting karena memungkinkan Isolasi Variabel. Kita bisa mengganti satu modul (misal: ganti model CNN) tanpa merusak atau mengubah modul lainnya (misal: modul pengambil data), sehingga kita yakin bahwa perubahan hasil eksperimen benar-benar disebabkan oleh variabel yang kita manipulasi.