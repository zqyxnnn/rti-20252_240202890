# WS-13: Data Preprocessing

> **Bab 13 — Preprocessing & Persiapan Data untuk Analisis**

---

## Ringkasan Materi

### Data Refinement Pipeline

```
Raw Data → Cleaning → Transformation → Normalization → Processed Data → Analysis Ready
```

Setiap tahap memiliki tujuan berbeda. **Preprocessing bukan langkah teknis biasa** — setiap keputusan preprocessing adalah keputusan riset yang bisa mengubah kesimpulan.

### Empat Prinsip Preprocessing

| Prinsip | Deskripsi |
|---------|----------|
| **Consistency** | Metode sama untuk data yang sama |
| **Transparency** | Setiap langkah terdokumentasi |
| **Reproducibility** | Orang lain bisa mengulang dengan hasil sama |
| **Minimal Distortion** | Ubah sesedikit mungkin; jika normalisasi tidak perlu, jangan lakukan |

### Cleaning Triad

| Masalah | Strategi | Risiko |
|---------|---------|--------|
| **Missing values** | | |
| — Listwise deletion | Missing < 5%, random | Data loss |
| — Mean/median imputation | Sedikit missing, dist. normal | Mengurangi variabilitas |
| — Model-based imputation | Banyak missing, pola sistematis | Introduces dependency |
| — Flag & separate | Missing karena alasan substantif | Kompleksitas analisis |
| **Duplikat** | Identifikasi → verifikasi → hapus | False positive (data mirip ≠ duplikat) |
| **Error format** | Standardisasi tipe, encoding | Kehilangan informasi saat konversi |

### Normalisasi — Kapan & Metode Mana

| Metode | Formula | Output | Sensitif Outlier? |
|--------|---------|--------|-------------------|
| Min-max | (x-min)/(max-min) | [0, 1] | Ya |
| Z-score | (x-mean)/std | Unbounded | Lebih robust |
| Robust scaling | (x-median)/IQR | Unbounded | Paling robust |

**Kunci:** Parameter normalisasi harus dihitung dari **training set saja** — bukan seluruh data. Pelanggaran = **data leakage**.

### Data Leakage Prevention

Data leakage terjadi ketika informasi dari test set "bocor" ke preprocessing:
- Normalisasi parameter dari seluruh dataset ← **SALAH**
- Cross-validation dilakukan sebelum split ← **SALAH**
- Feature selection menggunakan label test set ← **SALAH**

### Jebakan Kognitif

1. "Preprocessing cuma teknis — tidak perlu detail" → bisa ubah kesimpulan
2. "Lebih banyak preprocessing = lebih bersih = lebih baik" → over-processing distorsi data
3. "Normalisasi selalu diperlukan" → belum tentu, tergantung metode analisis
4. "Imputation sama untuk semua situasi" → strategi harus sesuai konteks

---

## Template A.13 — Preprocessing Documentation Log


PREPROCESSING LOG

Dataset           : Citra Penyakit Daun Padi (710 gambar)
Jumlah data awal  : 710 images

Cleaning:
| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| Missing | 0 | - | Dataset telah dikurasi|
| Duplikat| 0 | - | Dataset telah divalidasi |
| Error   | 0 | - | Format citra sudah standar |

Transformation:
| Transformasi | Variabel | Detail | Alasan |
|-------------|----------|--------|--------|
| Resizing | Image Input | 64x64 piksel | Standarisasi input layer |
| Augmentasi | Image Data | Flip, Rotate | Mengatasi dataset terbatas |

Normalization:
  Metode    : Pixel Scaling (0-1)
  Alasan    : Mengonversi nilai piksel (0-255) ke rentang [0,1] untuk mempercepat konvergensi gradien.
  Parameter : Dihitung dari Training Set saja (menggunakan ImageDataGenerator pada PyTorch/TensorFlow).

Leakage Check:
  [x] Parameter normalisasi dari training set saja
  [x] Tidak ada informasi test set dalam preprocessing
  [x] Cross-validation dilakukan setelah split

Jumlah data akhir : 710 images
Script tersedia   : [x] Ya → path: ____ | [ ] Belum


---

## Latihan 1 — Cleaning Plan

Periksa dataset Anda (atau dataset contoh) dan dokumentasikan masalah yang ditemukan.

| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| Inconsistency | 0 | N/A | Data sudah clean |

**Jumlah data sebelum cleaning:** 710
**Jumlah data setelah cleaning:** 710
**Persentase data yang hilang/berubah:** 0%

---

## Latihan 2 — Normalisasi Decision

Tentukan apakah data Anda perlu normalisasi, dan jika ya, metode apa yang tepat.

| Variabel | Range Asli | Distribusi | Outlier? | Metode Normalisasi | Alasan |
|----------|-----------|-----------|----------|-------------------|--------|
| Piksel Citra | 0 – 255 | Bervariasi | Tidak | Rescaling | Standar input CNN |

**Apakah normalisasi diperlukan?** [x] Ya / [ ] Tidak
**Justifikasi:**
> Normalisasi nilai piksel ke rentang [0,1] sangat penting bagi model CNN agar bobot awal tidak menyebabkan exploding gradients.

**Leakage check:**
- [x] Parameter dihitung dari training set saja
- [x] Normalisasi diterapkan setelah train-test split

---

## Latihan 3 — Preprocessing Report

Buat ringkasan preprocessing lengkap — dokumentasi yang cukup bagi orang lain untuk mereplikasi.

```
PREPROCESSING SUMMARY

1. Dataset: Citra Daun Padi  Citra Daun Padi  
2. Data awal: 710 records, 3 features
3. Cleaning:
   - Missing values: 0 kasus, metode: Tidak diperlukan
   - Duplikat: 0 kasus, tindakan: Tidak diperlukan
   - Error: 0 kasus, tindakan: Tidak diperlukan
4. Transformation: Resizing ke 64x64 piksel dan Data Augmentation untuk mitigasi overfitting.
5. Normalisasi: Rescaling (1./255), parameter dari Training Set.
6. Data akhir: 710 records, input size 64x64x3 features
7. Leakage check: [x] Lulus / [ ] Ada masalah
```

---

## Refleksi

> Apakah Anda pernah melakukan normalisasi "karena biasa dilakukan" tanpa mempertimbangkan apakah benar-benar diperlukan? Apa risiko over-preprocessing?

> Ya, dulu saya sering menerapkan normalisasi Z-Score pada setiap variabel numerik tanpa melihat distribusinya. Risiko over-preprocessing adalah kehilangan informasi substantif. Jika kita melakukan normalisasi berlebihan atau imputation yang salah pada data yang memiliki pola unik (seperti tekstur penyakit pada daun), kita bisa menghapus "sinyal" penting yang justru dibutuhkan model untuk membedakan kelas penyakit. Selain itu, over-preprocessing sering kali menjadi pintu masuk bagi data leakage jika tidak dilakukan secara ketat setelah split dataset.
