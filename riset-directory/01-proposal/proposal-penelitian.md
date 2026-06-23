# Proposal Penelitian: Perbandingan Performa Ekstraksi Fitur Arsitektur DenseNet-169 dan VGG-19 untuk Klasifikasi Penyakit Daun Padi pada Dataset Terbatas

---

## 1. Pendahuluan
Sektor pertanian merupakan pilar utama perekonomian Indonesia, di mana padi menjadi komoditas pangan paling krusial. Namun, produktivitas padi sering kali menurun akibat serangan penyakit tanaman, seperti blas (*blast*), hawar daun bakteri (*bacterial leaf blight*), dan tungro. Keterlambatan atau kesalahan dalam mengidentifikasi jenis penyakit ini dapat menyebabkan kegagalan panen skala besar. Secara konvensional, identifikasi dilakukan secara visual oleh petani atau pakar agraria, yang membutuhkan waktu lama dan rentan terhadap subjektivitas.

Seiring perkembangan teknologi kecerdasan buatan, metode *Deep Learning* dengan arsitektur *Convolutional Neural Network* (CNN) seperti VGG-19 dan DenseNet-169 banyak diterapkan untuk klasifikasi citra penyakit tanaman. VGG-19 memiliki keunggulan pada struktur konvolusi $3 \times 3$ yang dalam dan sekuensial, namun membutuhkan parameter besar sehingga rentan mengalami *overfitting* pada dataset terbatas. Di sisi lain, DenseNet-169 menawarkan mekanisme *feature reuse* melalui *dense connectivity*, di mana setiap *layer* menerima *input* dari seluruh *layer* sebelumnya, menjadikannya lebih efisien dalam memanfaatkan parameter pada dataset kecil. Penelitian ini mengusulkan analisis komparatif performa ekstraksi fitur dari arsitektur VGG-19 dan DenseNet-169 untuk menentukan model yang paling optimal, ringan, dan akurat dalam mengklasifikasikan penyakit daun padi pada kondisi data yang terbatas.

---

## 2. Rumusan Masalah
1. Apakah arsitektur DenseNet-169 menghasilkan akurasi dan nilai error (*Loss*) yang lebih baik dibandingkan VGG-19 saat menangani klasifikasi penyakit daun padi pada dataset terbatas?
2. Bagaimana perbandingan performa metrik evaluasi (Akurasi, Presisi, *Recall*, dan *F1-Score*) kedua model setelah diterapkan teknik augmentasi data?
3. Apakah perbedaan performa akurasi antara arsitektur VGG-19 dan DenseNet-169 signifikan secara statistik berdasarkan pengujian *t-Test* atau *Wilcoxon Signed-Rank Test*?

---

## 3. Hipotesis Penelitian [M1-07]
Berdasarkan rumusan masalah yang diajukan, hipotesis yang akan diuji dalam penelitian ini adalah:
* **$H_1$:** Penggunaan arsitektur DenseNet-169 secara signifikan menghasilkan akurasi klasifikasi yang lebih tinggi dan konvergensi *loss* yang lebih cepat dibandingkan arsitektur VGG-19 pada kondisi dataset daun padi yang terbatas.
* **$H_2$:** Terdapat perbedaan performa metrik akurasi yang signifikan secara statistik (nilai $p < 0.05$) antara arsitektur VGG-19 dan DenseNet-169 berdasarkan pengujian *t-Test* (atau *Wilcoxon Signed-Rank Test*) di seluruh 10 *independent runs* terkontrol.

---

## 4. Tujuan Penelitian
1. Mengimplementasikan arsitektur VGG-19 dan DenseNet-169 sebagai *feature extractor* untuk klasifikasi penyakit daun padi.
2. Mengevaluasi secara komparatif performa kedua model menggunakan metrik Akurasi, Presisi, *Recall*, dan *F1-Score* pada data *testing*.
3. Menguji signifikansi perbedaan performa model secara statistik menggunakan pengujian statistik (*t-Test* / *Wilcoxon*) di seluruh 10 *runs* terkontrol untuk menjamin reliabilitas.
4. Menyediakan rekomendasi empiris mengenai pemilihan arsitektur CNN yang efisien untuk diimplementasikan pada perangkat dengan keterbatasan komputasi di sektor pertanian.

---

## 5. Tinjauan Pustaka & Gap Penelitian
Penelitian terdahulu menunjukkan bahwa arsitektur VGG-19 sangat tangguh dalam mengenali pola citra yang kompleks karena kedalaman layernya. Namun, kendala utama VGG-19 adalah jumlah parameter yang sangat padat, yang memicu risiko tinggi terjadinya *overfitting* jika dilatih pada sampel yang sedikit. Sementara itu, DenseNet-169 terbukti andal dalam mereduksi masalah *vanishing gradient* dan memperkuat perambatan fitur (*feature propagation*) melalui koneksi langsung antar-layer. *Gap* penelitian yang ingin diselesaikan adalah belum adanya evaluasi komparatif yang mendalam secara statistik (*multi-run validation*) antara VGG-19 dan DenseNet-169 yang dikhususkan pada pemanfaatan dataset penyakit daun padi lokal dengan jumlah sampel terbatas (< 1000 citra).

---

## 6. Metodologi Penelitian

### 6.1 Populasi, Sampel, dan Objek Analisis [M2-02]
* **Objek Penelitian / Unit Analisis:** Objek dalam penelitian ini adalah fitur visual dari citra digital daun tanaman padi (*Oryza sativa*).
* **Populasi Penelitian:** Populasi data dalam penelitian ini mencakup seluruh citra digital daun padi yang sehat maupun yang terinfeksi penyakit tanaman padi di lahan pertanian.
* **Sampel Penelitian:** Sampel diambil menggunakan teknik **Purposive Sampling** dari dataset publik (seperti Kaggle atau UCI Machine Learning Repository) yang relevan. Jumlah total sampel yang digunakan adalah sebanyak **800 citra** daun padi yang terbagi ke dalam 4 kelas (Blas, Hawar Daun, Tungro, dan Sehat), di mana masing-masing kelas memiliki 200 citra (kondisi dataset terbatas).
* **Kriteria Inklusi Sampel:**
    1. Citra daun padi fokus pada bagian helai daun yang menunjukkan gejala penyakit secara jelas atau daun sehat tanpa bercak.
    2. Format citra bertipe standard (`.jpg`, `.jpeg`, atau `.png`) dengan resolusi minimal $224 \times 224$ piksel.
* **Kriteria Eksklusi Sampel:**
    1. Citra yang terlalu buram (*blurry*), memiliki pencahayaan ekstrem (*overexposed/underexposed*), atau objek daun terpotong lebih dari 50%.

### 6.2 Preprocessing & Feature Engineering
- **Resizing:** Mengubah resolusi seluruh citra menjadi $224 \times 224$ piksel agar sesuai dengan syarat *input* arsitektur VGG-19 dan DenseNet-169.
- **Augmentasi Data:** Untuk mengatasi keterbatasan dataset dan mencegah *overfitting*, diterapkan teknik *Horizontal Flip*, *Vertical Flip*, *Random Rotation* (0-30 derajat), dan *Brightness Adjustment*.
- **Normalisasi:** Melakukan *scaling* nilai piksel citra dari rentang `[0, 255]` menjadi `[0, 1]` atau standardisasi z-score berdasarkan bobot ImageNet.
- **Splitting:** Membagi dataset secara acak terkontrol dengan proporsi **70% Training set** (560 citra), **15% Validation set** (120 citra), dan **15% Testing set** (120 citra).

### 6.3 Implementasi Model
- **VGG-19 Baseline:** Menggunakan arsitektur VGG-19 pra-latih (*pretrained* ImageNet) sebagai *feature extractor*, diikuti oleh *Global Average Pooling*, *Dense Layer* (256 unit, fungsi aktivasi ReLU, Dropout 0.5), dan *Output Layer* dengan fungsi aktivasi Softmax (4 kelas).
- **DenseNet-169:** Menggunakan arsitektur DenseNet-169 pra-latih (*pretrained* ImageNet) dengan modifikasi *top-layer* yang identik (Dense 256, Dropout 0.5, Softmax 4 kelas) demi perbandingan yang adil (*apple-to-apple*).

### 6.4 Evaluasi & Validasi
Proses *training* dijalankan sebanyak 10 kali *independent runs* menggunakan *seed* acak yang berbeda untuk menguji konsistensi model. Metrik evaluasi yang dicatat meliputi matriks kebingungan (*Confusion Matrix*), Akurasi, Presisi, *Recall*, dan *F1-Score*. Terakhir, perbedaan rata-rata akurasi akhir diuji menggunakan **Wilcoxon Signed-Rank Test** atau **Paired t-Test** untuk membuktikan signifikansi secara statistik.