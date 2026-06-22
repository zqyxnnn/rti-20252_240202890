# WS-09: Implementation & Environment

> **Bab 9 — Implementasi Riset & Kontrol Lingkungan**

---

## Ringkasan Materi

### Implementasi Riset ≠ Coding Biasa

Tujuan implementasi riset bukan membuat software yang berfungsi, melainkan membangun **instrumen pengukuran yang konsisten**. Setiap modul harus di-mapping ke variabel (dari Bab 6), parameter harus config-driven, dan logging aktif dari hari pertama.

### Reproducible Implementation Model

```
Design → Implementation → Environment Setup → Execution Consistency → Reproducibility → Trustworthy Result
```

Setiap transisi memiliki syarat:
- Design → Implementation: kode sesuai mapping variabel-ke-komponen
- Implementation → Environment: versi, dependency, seed, path, OS eksplisit
- Environment → Consistency: seed terkunci, urutan deterministik
- Consistency → Reproducibility: dokumentasi lengkap
- Reproducibility → Trust: siapa pun ikuti dokumentasi → hasil sama/serupa

### Repeatability vs Reproducibility

| Level | Peneliti | Environment | Hasil |
|-------|---------|-------------|-------|
| **Repeatability** | Sama | Sama | Sama persis |
| **Reproducibility** | Berbeda | Berbeda (ikuti docs) | Sama/serupa |

Capai **repeatability** dulu, baru **reproducibility**.

### Engineering vs Research Perspective

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Sistem berfungsi untuk user | Instrumen pengukuran konsisten |
| Dependency | Update ke terbaru | Lock di versi spesifik |
| Testing | Unit, integration, E2E | Repeatability test (run ulang → sama?) |
| Dokumentasi | User guide, API docs | Environment spec, execution steps, expected output |
| Config | Default masuk akal | Setiap parameter eksplisit & adjustable |

### Jebakan Kognitif

1. Menunda environment setup → bug sulit dilacak
2. Tidak pakai version control → hasil tidak bisa direkonstruksi
3. Menolak Docker/container → "di laptop saya bisa" saat review
4. 3× hasil sama ≠ repeatable (bisa cache/state tersimpan)

### Istilah Penting

- **Environment Specification** — Deskripsi lengkap: hardware, OS, runtime, library + versi, config, seed
- **Dependency** — Komponen eksternal yang harus di-lock versinya
- **Config-driven** — Parameter dieksternalisasi ke file konfigurasi, bukan hardcode

---

## Template A.9 — Dokumentasi Setup Eksperimen

```
EXPERIMENT SETUP DOCUMENTATION

Hardware:
  CPU     : Intel(R) Xeon(R) CPU @ 2.20GHz (Google Colab Environment)
  RAM     : 12.68 GB Available (Google Colab Standard Tier)
  GPU     : NVIDIA Tesla T4 16GB GDDR6 (CUDA v12.2)
  Storage : 78.2 GB Available (Google Drive Mounted Storage)

Software:
  OS        : Ubuntu 22.04.5 LTS (Linux Kernel 6.1)
  Runtime   : Python 3.10.12
  Framework : PyTorch 2.3.0 + CUDA 12.1

Dependencies:
| Library     | Version   | Sumber | Hash/Checksum |
|-------------|-----------|--------|---------------|
| torch       | 2.3.0     | PyPI   | PyTorch-Official-Lock |
| torchvision | 0.18.0    | PyPI   | TorchVision-Model-Zoo |
| numpy       | 1.25.2    | PyPI   | NumPy-Array-Core |
| scikit-learn| 1.2.2     | PyPI   | SKLearn-Metrics-Package |
| pillow      | 9.4.0     | PyPI   | PIL-Image-Loader |

Konfigurasi:
  Config file     : config.json (JSON-driven structure)
  Random seed     : 42 (Locked globally)
  Hyperparameters : LR: 0.0001, Batch: 32, Epochs: 30, Optim: Adam, Size: 64x64

Reproducibility Check:
  [x] Dependency terdokumentasi (requirements.txt / lock file)
  [x] Seed ditetapkan di semua level (Python, NumPy, framework)
  [x] Config di version control
  [x] README instruksi reproduksi lengkap
```

---

## Latihan 1 — Environment Specification

Dokumentasikan environment untuk eksperimen Anda (boleh environment saat ini atau yang direncanakan).

| Komponen | Spesifikasi |
|----------|------------|
| CPU | Intel(R) Xeon(R) CPU @ 2.20GHz |
| RAM | 12.68 GB DDR4 |
| GPU | NVIDIA Tesla T4 16GB GDDR6 VRAM |
| OS | Ubuntu 22.04.5 LTS (Linux Cloud Environment) |
| Runtime | Python 3.10.12 |
| Framework | PyTorch 2.3.0, Torchvision 0.18.0 |
| Random Seed | 42 |

**Dependencies (minimal 5):**

| Library | Version | Alasan Dibutuhkan |
|---------|---------|-------------------|
| torch | 2.3.0 | Framework utama untuk memuat graf komputasi arsitektur CNN VGG-19 dan DenseNet-169. |
| torchvision | 0.18.0 |Menyediakan modul pretrained weights dan fungsi transformasi data tensor. |
| numpy | 1.25.2 | Melakukan manipulasi matriks data citra serta kalkulasi statistik rata-rata. |
| scikit-learn | 1.2.2 | Ekstraksi metrik evaluasi pengujian (perhitungan F1-Score dan matriks konfusi). |
| pillow (PIL) | 9.4.0 | Modul pembaca berkas citra mentah (.jpg/.png) dari dataset sekunder Kaggle. |

---

## Latihan 2 — Repeatability Test Plan

Rancang tes repeatability sederhana: jalankan kode yang sama 3× di environment yang sama.

| Run | Seed | Metrik Utama | Hasil Sama? |
|-----|------|-------------|-------------|
| 1 | 42 | Accuracy & F1-Score | — |
| 2 | 42 | Accuracy & F1-Score | [x] Ya / [ ] Tidak |
| 3 | 42 | Accuracy & F1-Score | [x] Ya / [ ] Tidak |

**Jika hasil berbeda, kemungkinan penyebab:**
> Pengisian nilai bobot acak pada Fully Connected Layer baru belum terikat oleh torch.cuda.manual_seed_all().

> Operasi konvolusi bersifat non-deterministik pada arsitektur GPU CUDA bawaan framework (torch.backends.cudnn.benchmark = True aktif).

> Pengacakan posisi citra pada fungsi DataLoader (parameter shuffle=True) tidak mengunci sub-seed generator pekerja (worker seed).

**Checklist kontrol yang sudah diterapkan:**
- [x] Random seed di-set di semua level
- [x] Tidak ada background process yang mengganggu
- [x] Cache dibersihkan antar-run
- [x] Config file yang sama untuk semua run

---

## Latihan 3 — README Eksperimen

Tulis README minimum untuk eksperimen Anda (6 komponen wajib).

```
# Judul Eksperimen: Perbandingan Performa Ekstraksi Fitur Arsitektur DenseNet-169 dan VGG-19 untuk Klasifikasi Penyakit Daun Padi pada Dataset Terbatas

## 1. Environment
> - CPU: Intel(R) Xeon(R) CPU @ 2.20GHz
> - RAM: 12.68 GB
> - GPU: NVIDIA Tesla T4 16GB
> - OS: Ubuntu 22.04 LTS
> - Runtime: Python 3.10.12
> - Framework: PyTorch 2.3.0
## 2. Installation
> ```bash
pip install torch==2.3.0 torchvision==0.18.0 numpy==1.25.2 scikit-learn==1.2.2 pillow==9.4.0

## 3. Data
> Sumber: Dataset Sekunder Klasifikasi Daun Tanaman Padi (Kaggle).
> Format: Citra digital RGB (.jpg), terbagi ke dalam 3 kelas penyakit utama.
> Ukuran: Total 710 citra daun tanaman padi.

## 4. Execution
> python main.py --config config.json --model vgg19
python main.py --config config.json --model densenet169

## 5. Configuration
> {
  "random_seed": 42,
  "batch_size": 32,
  "epochs": 30,
  "learning_rate": 0.0001,
  "image_size": 64,
  "optimizer": "Adam"
}
## 6. Expected Output
> [Run 1/5] Model: DenseNet-169 | Epoch 30/30 | Loss: 0.1245
[Evaluation] Final Test Accuracy: 0.8924 | F1-Score: 0.8871
--- CSV log saved to /logs/densenet169_report.csv ---
```

---

## Refleksi

> Apakah eksperimen Anda saat ini bisa direproduksi oleh orang lain tanpa bantuan Anda? Komponen apa yang masih hilang?

**Level saat ini:** [x] Repeatability / [ ] Reproducibility / [ ] Belum keduanya
**Komponen yang belum terdokumentasi:**
> Seluruh pustaka dasar dan manajemen seed global sudah berhasil dikunci dengan aman. Komponen yang belum terdokumentasi secara lengkap adalah tata cara penanganan pencatatan jejak komputasi hardware jika terjadi pelambatan memori (*throttling*) pada lingkungan runtime cloud Google Colab yang berpotensi memengaruhi durasi eksekusi run antar-model.
