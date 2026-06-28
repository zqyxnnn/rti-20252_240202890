# Laporan Penelitian

**Judul:** Analisis Komparatif Performa Arsitektur Deep Learning VGG-19 dan DenseNet-169 dalam Klasifikasi Penyakit Daun Padi

**Peneliti:** Zakkya Fauzan Alba'asithu
**Target Publikasi:** : Jurnal Riset Teknologi Informasi / Jurnal Ilmiah Sinta 2/3

---

## 1. Ringkasan Eksekutif

Penelitian ini bertujuan untuk membangun sistem deteksi penyakit tanaman padi yang akurat dan teruji secara statistik. Objek penelitian difokuskan pada klasifikasi citra penyakit daun padi (seperti Bacterial Blight, Blast, Brown Spot) menggunakan arsitektur VGG-19 dan DenseNet-169. Untuk menghindari bias yang sering terjadi pada eksperimen single-run, penelitian ini melakukan pengujian terkontrol sebanyak 35 kali iterasi (35 run per arsitektur) dengan variasi random seed.Hasil evaluasi menunjukkan bahwa VGG-19 mencatat akurasi rata-rata 85.06% ± 4.67%, sementara DenseNet-169 mencatat 84.14% ± 4.14%. Uji statistik Wilcoxon Signed-Rank Test mengonfirmasi bahwa perbedaan performa kedua model tidak signifikan secara statistik (p = 0.6558 > 0.05). Penelitian ini memberikan bukti empiris bahwa untuk dataset daun padi skala kecil, pemilihan arsitektur CNN dapat didasarkan pada efisiensi komputasi, karena kompleksitas model tidak secara otomatis menjamin peningkatan akurasi yang signifikan.

---

## 2. Latar Belakang dan Rumusan Masalah

Penyakit daun padi merupakan ancaman utama bagi ketahanan pangan nasional. Pendekatan deep learning melalui klasifikasi citra menawarkan solusi deteksi dini yang otomatis. Namun, terdapat tantangan dalam menentukan arsitektur mana yang paling stabil dan efisien untuk dataset spesifik daun padi. Rumusan masalah penelitian ini adalah:

1. Apakah arsitektur DenseNet-169 secara signifikan lebih unggul dibandingkan VGG-19 dalam mengklasifikasikan penyakit daun padi?
2. Sejauh mana stabilitas performa kedua model jika diuji melalui variasi inisialisasi random seed yang ketat?
3. Apakah perbedaan performa tersebut memiliki signifikansi statistik?

---

## 3. Metodologi dan Pelaksanaan

Penelitian dilaksanakan melalui tahapan pipeline terstruktur:
1. Pengumpulan Data: Dataset citra daun padi (diperoleh dari repositori publik).
2. Preprocessing: Normalisasi citra menjadi resolusi 64 x 64 piksel, data splitting, dan augmentasi untuk meningkatkan generalisasi model.
3. Arsitektur Model: - VGG-19: Transfer learning pada lapisan konvolusi dengan fine-tuning pada lapisan fully connected.
    - DenseNet-169: Memanfaatkan dense blocks untuk efisiensi ekstraksi fitur.
4. Eksekusi Otomatis: Menggunakan skrip run_stability_test.py untuk menjalankan 35 iterasi eksperimen secara independen guna memitigasi efek inisialisasi bobot acak.
5. Analisis Statistik: Uji Wilcoxon Signed-Rank Test pada hasil akurasi 35 iterasi untuk memvalidasi perbedaan performa secara empiris.

### 4. Hasil penelitian

| Model | Akurasi (%) | Standar Deviasi | 
|---|---|---|
| VGG-19 | 84.90% | 4.544 |
| DenseNet-169 |  84.50% | 4.215 |

Hasil Uji Signifikansi Statistik (Wilcoxon Signed-Rank Test)
- Komparasi: VGG-19 vs DenseNet-169
- Nilai Statistik:  0.3864
- p-value: 0.7004
- Kesimpulan: Perbedaan performa TIDAK SIGNIFIKAN secara statistik.

---

## 5. Kendala dan Catatan Lingkungan

- Resolusi: Penggunaan resolusi 64 x64 piksel membatasi model dalam menangkap detail pola penyakit yang sangat halus, yang berdampak pada batas atas akurasi model.
- Sensitivitas Inisialisasi: Standar deviasi di atas 4% membuktikan bahwa inisialisasi bobot awal sangat memengaruhi konvergensi. Tanpa pengujian iteratif, hasil satu kali eksperimen dapat menyesatkan.
- Efisiensi: DenseNet-169 memerlukan profil memori yang berbeda saat training dibanding VGG-19; hal ini menjadi catatan penting untuk implementasi pada perangkat edge atau mobile.

---

## 6. Kesimpulan dan Saran

- Kesimpulan: Tidak ada bukti statistik yang cukup untuk menyatakan bahwa satu arsitektur lebih superior dibandingkan yang lain untuk klasifikasi penyakit daun padi pada dataset ini. Keduanya setara, memberikan fleksibilitas bagi peneliti untuk memilih model sesuai batasan sumber daya komputasi.

- Saran: Penelitian selanjutnya disarankan untuk menggunakan resolusi citra yang lebih tinggi, menerapkan hyperparameter tuning yang lebih agresif, atau mencoba arsitektur berbasis Vision Transformer (ViT) untuk menangkap konteks global citra.

---

## 7. Lampiran — Peta Artefak Penelitian

| Folder | Isi | Status |
|---|---|---|
| [01-proposal/](../01-proposal/) | Proposal riset CNN untuk penyakit padi | Selesai |
| [02-literatur/](../02-literatur/) | Matriks literatur & tinjauan pustaka | selesai |
| [03-teori/](../03-teori/) | Diagram alir arsitektur VGG-19 & DenseNet-169 | Selesai |
| [04-data/](../04-data/) | Dataset citra daun padi (resizing & cleaning) | selesai |
| [05-kode/](../05-kode/gateway/) | Pipeline pelatihan 35 iterasi & skrip statistik | Selesai |
| [06-output/](../06-output/) | Log 35 eksperimen, CSV hasil, & grafik akurasi | Selesai |
| [07-manuskrip/](../07-manuskrip/) | Naskah ilmiah (paper) siap publikasi | Sedang berjalan |
| [08-laporan/](../08-laporan/) | Laporan akhir (dokumen ini) | Selesai |
| [09-docs/](../09-docs/) | Dokumen status kemajuan dan rencana teknis | Selesai |
