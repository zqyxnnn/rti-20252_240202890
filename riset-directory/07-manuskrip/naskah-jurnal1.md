# Analisis Komparatif Performa Arsitektur Deep Learning VGG-19 dan DenseNet-169 dalam Klasifikasi Penyakit Daun Padi

**Zakkya Fauzan Alba'asithu**  
Program Studi Ilmu Komputer, Universitas Putra Bangsa  
email: zqyfzn@gmail.com

## ABSTRAK
Deteksi penyakit pada tanaman padi merupakan langkah krusial dalam mendukung ketahanan pangan. Penelitian ini menyajikan analisis komparatif performa arsitektur Convolutional Neural Network (CNN), yaitu VGG-19 dan DenseNet-169, dalam mengklasifikasikan citra penyakit daun padi. Untuk memastikan kestabilan hasil, pengujian dilakukan sebanyak 35 iterasi terkontrol dengan random seed yang bervariasi. Hasil evaluasi menunjukkan bahwa VGG-19 mencapai akurasi rata-rata 84,90%, sementara DenseNet-169 mencapai 84,50%. Uji statistik Wilcoxon Signed-Rank Test menunjukkan bahwa perbedaan performa antara kedua model tidak signifikan secara statistik (p = 0,7004 > 0,05). Hal ini mengindikasikan bahwa kedua arsitektur memiliki efektivitas yang setara dalam mengekstraksi fitur penyakit daun padi pada resolusi 64x64. Penelitian ini memberikan wawasan bagi pengembangan sistem pertanian presisi yang efisien.  

**Kata Kunci:** Klasifikasi Citra; Penyakit Daun Padi; VGG-19; DenseNet-169; Deep Learning

## ABSTRACT
Disease detection in rice plants is a crucial step in supporting food security. This study presents a comparative analysis of the performance of Convolutional Neural Network (CNN) architectures, VGG-19 and DenseNet-169, in classifying rice leaf disease images. To ensure result stability, testing was carried out in 35 controlled iterations with varying random seeds. Evaluation results showed that VGG-19 achieved an average accuracy of 84.90%, while DenseNet-169 reached 84.50%. The Wilcoxon Signed-Rank Test indicated that the performance difference between the models was not statistically significant (p = 0.7004 > 0.05). This indicates that both architectures have equal effectiveness in extracting rice leaf disease features at 64x64 resolution. This research provides insights for developing efficient precision agriculture systems.  

**Keywords:** Image Classification; Rice Leaf Disease; VGG-19; DenseNet-169; Deep Learning

## PENDAHULUAN
Padi merupakan komoditas pangan utama di Indonesia, namun produktivitasnya sering terhambat oleh serangan penyakit. Deteksi dini melalui pengolahan citra digital berbasis deep learning menawarkan solusi otomatisasi yang cepat. Meski arsitektur CNN seperti VGG-19 dan DenseNet-169 telah banyak digunakan, stabilitas hasil klasifikasinya pada dataset spesifik daun padi memerlukan pengujian mendalam dengan iterasi yang tinggi. Penelitian ini bertujuan untuk menguji performa kedua model guna memberikan acuan bagi implementasi sistem deteksi penyakit padi yang andal.

## METODE
Penelitian ini menggunakan desain eksperimental komparatif. Sumber data diperoleh dari dataset citra penyakit daun padi (Bacterial Blight, Blast, Brown Spot). Preprocessing meliputi normalisasi citra ke resolusi 64x64 piksel dan augmentasi data. Model yang diuji adalah VGG-19 (transfer learning) dan DenseNet-169. Prosedur pengujian dilakukan melalui 35 iterasi eksperimen independen untuk memitigasi efek inisialisasi bobot acak. Teknik analisis data yang digunakan adalah statistik deskriptif untuk akurasi dan Wilcoxon Signed-Rank Test untuk menguji signifikansi perbedaan performa.

## HASIL DAN PEMBAHASAN
Hasil evaluasi kinerja selama 35 iterasi eksperimen dirangkum pada Tabel 1.

Tabel 1. Hasil Evaluasi Kinerja Rata-rata Model
| Model | Rata-rata Akurasi (%) | Standar Deviasi |
| :--- | :--- | :--- |
| VGG-19 | 84,90 | 4,544 |
| DenseNet-169 | 84,50 | 4,215 |

Berdasarkan Tabel 2, hasil uji statistik mengonfirmasi bahwa perbedaan performa tidak signifikan.

Tabel 2. Hasil Wilcoxon Signed-Rank Test
| Komparasi Model | Nilai Statistik | p-value | Kesimpulan |
| :--- | :--- | :--- | :--- |
| VGG-19 vs DenseNet-169 | 0,3864 | 0,7004 | Tidak Signifikan |

Diskusi: Variasi akurasi (standar deviasi > 4%) mengonfirmasi bahwa inisialisasi bobot awal sangat memengaruhi konvergensi. Pada resolusi rendah (64x64), kompleksitas arsitektur tidak menjamin peningkatan akurasi, sehingga pemilihan model dapat didasarkan pada efisiensi komputasi.

## SIMPULAN
Penelitian ini menyimpulkan bahwa tidak ada perbedaan performa yang signifikan antara VGG-19 dan DenseNet-169 pada klasifikasi penyakit daun padi. Pengujian iteratif sangat krusial untuk validitas riset deep learning. Penelitian masa depan disarankan menggunakan resolusi lebih tinggi atau arsitektur Vision Transformer (ViT).

## REFERENSI
Annur, I. F., dkk. (2023). Klasifikasi Tingkat Keparahan Penyakit Leafblast Tanaman Padi Menggunakan MobileNetv2. Fountain of Informatics Journal, 8(1), 1-10.  
Asseweth, M. Y. A. (2024). Klasifikasi Penyakit pada Daun Tanaman Padi Menggunakan Arsitektur DenseNet-169 (Skripsi). Universitas Medan Area, Medan.  
Luthans, F. (2011). Organizational Behavior: An Evidence-Based Approach. United States: McGraw-Hill.  
Shinta, R. (2023). Klasifikasi Citra Penyakit Daun Tanaman Padi Menggunakan CNN Dengan Arsitektur VGG-19 (Tugas Akhir). Universitas Islam Negeri Sultan Syarif Kasim Riau, Pekanbaru.  
Susanto, M. H. (2025). Klasifikasi Penyakit pada Tanaman Padi Berbasis Citra Daun Menggunakan Convolutional Neural Network (Skripsi). Universitas Islam Negeri Maulana Malik Ibrahim, Malang.