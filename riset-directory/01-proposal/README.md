# Proposal Penelitian: Perbandingan Performa Ekstraksi Fitur Arsitektur DenseNet-169 dan VGG-19 untuk Klasifikasi Penyakit Daun Padi pada Dataset Terbatas

## A. JUDUL

Judul penelitian: Perbandingan Performa Ekstraksi Fitur Arsitektur DenseNet-169 dan VGG-19 untuk Klasifikasi Penyakit Daun Padi pada Dataset Terbatas

## B. RINGKASAN

Ancaman gagal panen akibat serangan penyakit daun seperti bacterial leaf blight, brown spot, dan smut sampai saat ini masih menjadi momok yang merugikan produktivitas petani padi. Kendala utama di lapangan berakar dari lambatnya proses identifikasi penyakit yang masih mengandalkan pengamatan manual dan cenderung subjektif. Di sisi lain, pemanfaatan teknologi klasifikasi otomatis berbasis Convolutional Neural Network (CNN) konvensional juga belum sepenuhnya stabil, sebab model arsitektur dasar sering kali mengalami penurunan performa drastis akibat gejala overfitting ketika dipaksa berlatih dengan jumlah sampel gambar yang minim.

Penelitian ini dirancang untuk membuktikan secara empiris solusi atas kendala keterbatasan data tersebut melalui studi komparasi arsitektur. Fokus utama riset ini adalah menguji keunggulan mekanisme feature reuse pada struktur Dense Block milik DenseNet-169, yang kinerjanya akan diadu langsung dengan model klasik linier VGG-19 selaku kondisi baseline atau standar pembanding awal. Eksperimen dilakukan di laboratorium menggunakan skrip pemrograman Python modular untuk mengolah dataset sekunder berupa 710 citra penyakit daun padi yang diperoleh dari platform Kaggle. Pengujian dilakukan dengan mengunci seluruh variabel kontrol parameter training secara konstan dan mereduksi dimensi gambar ke ukuran 64x64 piksel. Tingkat keberhasilan klasifikasi dari kedua model selanjutnya akan dinilai secara kuantitatif melalui metrik Accuracy dan F1-Score, sebelum akhirnya ditarik kesimpulan valid lewat uji statistik inferensial Paired-Sample T-Test pada taraf signifikansi 5%.

Luaran yang ditargetkan dari penelitian ini adalah berupa draf rekomendasi empiris mengenai efisiensi arsitektur CNN pada dataset skala kecil untuk referensi akademis, serta sebuah prototipe pipeline kode pemrograman klasifikasi yang siap diintegrasikan sebagai engine deteksi otomatis penyakit padi pada pengembangan aplikasi pertanian digital ke depan.

## C. KATA KUNCI

Penyakit daun padi; CNN; DenseNet-169; VGG-19; Dataset terbatas

## D. PENDAHULUAN

### D.1. LATAR BELAKANG DAN RUMUSAN MAŞALAH

Dalam usaha menjaga produktivitas komoditas pangan, sektor pertanian padi saat ini sering kali dihadapkan pada ancaman nyata berupa risiko gagal panen akibat serangan penyakit daun infeksius seperti bacterial leaf blight, brown spot, dan smut. Kendala utamanya, para petani di lapangan sampai sekarang masih mengandalkan proses identifikasi gejala penyakit secara manual yang karakternya cenderung lambat serta sangat subjektif. Masalah ini diperparah oleh keterbatasan aspek teknologi komputasi, di mana arsitektur CNN konvensional yang ada saat ini membutuhkan pasokan ribuan gambar latihan agar mampu mengenali pola penyakit secara akurat; akibatnya, saat dihadapkan pada situasi dataset yang terbatas, model komputer tersebut justru mengalami ketidakstabillan performa dan cenderung menghafal data latih (overfitting). Dampak dari kegagalan adaptasi model ini sangat fatal, karena nilai akurasi klasifikasi otomatis akan langsung merosot tajam saat sistem dipaksa menguji gambar baru di kondisi lapangan nyata, yang pada akhirnya membuat deteksi dini gagal total dan petani tetap terlambat dalam menyelamatkan lahan mereka dari wabah.

### D.2. PENDEKATAN PEMECAHAN MASALAH

Penelitian ini bertujuan untuk membuktikan secara empiris arsitektur mana yang lebih adaptif dan minim risiko overfitting saat jumlah sampel citra penyakit padi tidak ideal. Untuk mencapai tujuan tersebut, eksperimen lab ini dirancang secara spesifik guna menguji dan mengukur langsung perbandingan performa antara dua variabel model, yaitu DenseNet-169 melawan VGG-19, dengan tolok ukur metrik evaluasi yang jelas.

Sebagai pendekatan solusi, intervensi yang diusulkan dalam riset ini adalah menerapkan arsitektur DenseNet-169 sebagai model alternatif untuk mengevaluasi apakah perubahan struktural pada jalur propagasi fitur mampu mendongkrak akurasi dan kestabilan klasifikasi pada dataset berskala kecil. Prediksi awal menempatkan DenseNet-169 memiliki keunggulan teoretis berupa kemampuan feature reuse melalui dense blocks, di mana koneksi langsung antar-layer tersebut dapat meminimalkan jumlah parameter latih sehingga dihipotesiskan jauh lebih tangguh terhadap bahaya overfitting pada data kecil dibandingkan model yang strukturnya linier dan padat parameter.

Model alternatif tersebut nantinya akan dihadapkan langsung dengan VGG-19 yang diposisikan sebagai kondisi baseline atau standar pembanding dalam penelitian ini. Arsitektur klasik linier dengan jumlah parameter besar tersebut sengaja dipilih sebagai tolok ukur awal untuk melihat tingkat kerentanan arsitektur dasar Deep Learning saat dipaksa bekerja dengan jumlah sampel yang sedikit.

### D.3. STATE OF THE ART DAN KEBARUAN

Jika memotret peta riset saat ini, mayoritas penelitian terdahulu yang berfokus pada deteksi penyakit tanaman berbasis Convolutional Neural Network (CNN) standar sebetulnya sudah berhasil mencapai performa yang sangat impresif, bahkan mencatatkan angka akurasi di atas 90%. Namun, jika dibedah lebih dalam, tren positif tersebut memuat keterbatasan yang berulang; benchmark akurasi tinggi tersebut rata-rata diperoleh karena model dilatih menggunakan pasokan dataset berskala sangat besar serta diambil dalam kondisi pencahayaan laboratorium yang serba ideal. Akibatnya, arsitektur-arsitektur bawaan tersebut belum teruji sama sekali keandalannya jika dipaksa bekerja di bawah tekanan keterbatasan jumlah data di lapangan nyata.

Kondisi eksisting ini memicu munculnya gap atau selisih pengetahuan yang sangat eksplisit antara kondisi ideal dan kondisi aktual di ranah riset komputer visi. Kondisi ideal yang diharapkan sebenarnya adalah kepemilikan model klasifikasi yang tetap efisien dan presisi meskipun hanya disuplai oleh dataset yang terbatas, yakni di bawah 1000 sampel gambar. Sementara kondisi aktualnya, alih-alih menguji batas minimum ketahanan model, para peneliti terdahulu justru langsung mengambil jalan pintas dengan menggunakan dataset besar. Akibatnya, ada ruang kosong yang belum terjawab mengenai bagaimana pengaruh perbedaan struktural antar-arsitektur terhadap risiko penuaan performa saat jumlah sampel data ditekan seminimal mungkin.

Di sinilah posisi penelitian ini hadir untuk menutup celah tersebut melalui sebuah studi komparatif yang terukur. Kebaruan (novelty) yang ditawarkan dalam riset ini bukan sekadar mengulang klaim bahwa topik penyakit padi itu penting, melainkan menguji secara kritis batas ketahanan arsitektur Deep Learning pada kondisi minim data dengan menghadapkan dua ideologi struktur yang kontras. Penelitian ini memposisikan model klasik VGG-19 sebagai kondisi baseline atau standar pembanding awal. Karakteristik VGG-19 yang memiliki struktur linier konvensional namun padat parameter dinilai sangat relevan sebagai tolok ukur untuk melihat seberapa rapuh arsitektur dasar terhadap risiko overfitting. Logika pembanding tersebut nantinya akan digunakan untuk menguji efektivitas arsitektur DenseNet-169 yang membawa mekanisme interkoneksi Dense Block, guna membuktikan secara empiris apakah pendekatan feature reuse mampu menjadi solusi konkret dalam menjaga stabilitas akurasi pada keterbatasan dataset.

### D.4. PETA JALAN PENELITIAN

Peta jalan (roadmap) penelitian ini dirancang sebagai satu kesatuan rangkaian kerja komputasi yang terukur, yang membagi fokus riset ke dalam tiga tahapan besar: tahapan pondasi yang telah dicapai, tahapan inti eksperimen laboratorium yang diusulkan saat ini, serta tahapan hilirisasi lanjutan di masa depan. Perkembangan dari setiap fase tidak bergerak sebagai daftar aktivitas mandiri, melainkan sebagai batu pijakan yang saling menentukan kesiapan artefak dan validitas pengujian.

Tahapan awal yang telah dicapai sebelum usulan ini diajukan berfokus pada fase formulasi konsep, studi literatur terstruktur, serta penyiapan data (data gathering). Pada tahap ini, telah dilakukan eksplorasi terhadap berbagai riset terdahulu mengenai performa Convolutional Neural Network (CNN) pada citra agrikultur, yang memicu temuan celah riset (research gap) berupa kerentanan model klasik terhadap overfitting saat pasokan data di bawah 1000 sampel. Dari pondasi teori tersebut, langkah nyata yang telah diselesaikan adalah mengakuisisi dataset sekunder dari platform Kaggle berisi penyakit daun padi (bacterial leaf blight, brown spot, dan smut) serta mengunci jumlah sampel secara sengaja pada angka terbatas yaitu 710 citra. Selain itu, tahap ini juga berhasil merumuskan rancangan arsitektur komparatif dan mengamankan kesiapan lingkungan komputasi berbasis GPU pada Google Colab.

Tahapan yang dikerjakan pada usulan penelitian ini merupakan fase eksekusi laboratorium dan validasi ilmiah inti. Tahap ini diawali dengan mentransformasikan rancangan konsep ke dalam bentuk artefak perangkat lunak nyata berupa bundel skrip Python modular. Langkah kerja nyata dimulai dari pengodean fungsi pemrosesan awal (data loader) untuk memaksa reduksi dimensi gambar menjadi 64x64 piksel, diikuti oleh isolasi variabel kontrol parameter latihan (learning rate 0.001, optimizer Adam, tanpa augmentasi). Selanjutnya, skenario pengujian dieksekusi dengan melatih model baseline VGG-19 dan model intervensi DenseNet-169 masing-masing sebanyak 5 kali pengulangan (repeated runs) independen. Output metrik Accuracy dan Fl-Score dari tiap sesi kemudian diekspor ke dalam file .csv. Fase ini ditutup dengan pengujian statistik inferensial menggunakan Paired-Sample T-Test (α=0.05) untuk menghasilkan kesimpulan ilmiah yang sah mengenai dampak mekanis feature reuse terhadap mitigasi overfitting.

Tahapan lanjutan yang direncanakan setelah penelitian ini selesai adalah fase hilirisasi teknologi dan perluasan skala generalisasi. Artefak berupa pre-trained model weight terbaik hasil eksperimen ini nantinya tidak akan dibiarkan menjadi dokumen teknis mati. Langkah berikutnya adalah membangun sebuah Application Programming Interface (API) atau classifier engine berstatus ready-to-deploy. Mesin kecerdasan buatan yang sudah teruji kebal pada data terbatas ini direncanakan akan dicangkokkan ke dalam prototipe aplikasi seluler pertanian digital berbasis Android atau iOS. Melalui aplikasi tersebut, model hasil riset ini dapat digunakan secara praktis oleh petani di lapangan untuk melakukan deteksi dini penyakit daun padi secara real-time langsung lewat kamera smartphone. Selain itu, pengembangan riset ke depan akan diarahkan pada pengujian model menggunakan variasi dataset penyakit tanaman pangan lain untuk menguji batas akhir fleksibilitas arsitekturnya.

## E. METODE

### E.1. Desain Penelitian, Hipotesis, dan Unit Analisis

Penelitian ini menggunakan jenis penelitian kuantitatif dengan tipe desain eksperimental laboratorium secara komparatif. Pendekatan eksperimen murni di dalam lingkungan simulasi komputasi ini dipilih agar seluruh variabel pengujian dapat diisolasi secara ketat demi menghasilkan kesimpulan yang valid.

* **Hipotesis:** H1: Terdapat pengaruh signifikan perbedaan arsitektur (IV) terhadap performa akurasi dan F1-Score (DV), di mana arsitektur DenseNet-169 menghasilkan nilai yang lebih tinggi secara signifikan dibandingkan arsitektur VGG-19 dalam memitigasi overfitting pada dataset citra penyakit daun padi.
* **Populasi:** Seluruh citra penyakit daun padi yang tersedia pada dataset publik Kaggle.
* **Sampel:** Sebanyak 710 citra penyakit daun padi (bacterial leaf blight, brown spot, dan smut) yang diambil menggunakan teknik random sampling.
* **Kriteria Inklusi:** Citra yang memiliki resolusi memadai untuk direduksi menjadi 64x64 piksel.
* **Kriteria Eksklusi:** Citra yang buram atau memiliki noise latar belakang yang dominan yang tidak merepresentasikan gejala penyakit.
* **Unit Analisis:** Matriks piksel citra daun padi yang merepresentasikan fitur visual penyakit pada area permukaan daun.

### E.2. Variabel, Metric, Instrumen, dan Data

Desain evaluasi dalam eksperimen ini berpusat pada satu variabel bebas utama (Independent Variable IV), yaitu variasi jenis arsitektur model deep learning (VGG-19 baseline vs DenseNet-169 intervensi). Dampak dari manipulasi arsitektur ini diukur melalui variabel terikat (Dependent Variable - DV), yaitu output performa Accuracy dan F1-Score (%). Instrumen yang digunakan adalah fungsi bawaan library Scikit-Learn untuk membandingkan matriks prediksi terhadap ground truth labels. Sumber data observasi adalah dataset sekunder 710 citra dari Kaggle.

### E.3. Skenario dan Prosedur Pengujian

Prosedur pengujian dieksekusi secara ketat untuk menjamin validitas hasil, dengan membandingkan VGG-19 dan DenseNet-169 pada kondisi yang sama (learning rate 0.001, optimizer Adam, 64x64 piksel, tanpa data augmentation). Pengujian dilakukan dengan pengulangan (repeated runs) untuk mengantisipasi noise, di mana hasil log metrik diekspor ke format .csv untuk analisis lebih lanjut.

### E.4. Artifact, Setup, dan Teknik Analisis

Artefak utama adalah modul skrip Python modular yang memisahkan fungsi data loader dan model klasifikasi. Setup komputasi menggunakan GPU Google Colab. Teknik analisis data menggunakan Paired-Sample T-Test (α=0.05) untuk membuktikan signifikansi perbedaan performa secara statistik, dengan asumsi bahwa dataset publik Kaggle sudah valid dan tidak mencakup optimasi hyperparameter ekstensif.

## F. HASIL YANG DIHARAPKAN

Penelitian diharapkan dapat membuktikan secara statistik bahwa arsitektur DenseNet-169 memiliki ketahanan yang lebih baik terhadap risiko overfitting pada dataset terbatas dibandingkan arsitektur linier VGG-19, serta menghasilkan prototipe pipeline klasifikasi yang dapat diintegrasikan pada sistem deteksi dini penyakit tanaman.

## G. JADWAL PENELITIAN

| No | Nama kegiatan | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Identifikasi masalah dan topik | x | x |  |  |  |  |  |  |
| 2 | Literatur dan gap |  | x | x |  |  |  |  |  |
| 3 | RQ dan desain metode |  |  | x | x |  |  |  |  |
| 4 | Implementasi atau instrumen |  |  |  | x | x |  |  |  |
| 5 | Pengujian atau eksperimen |  |  |  |  | x | x |  |  |
| 6 | Analisis dan penulisan |  |  |  |  |  | x | x |  |
| 7 | Revisi final |  |  |  |  |  |  | x | x |

## H. DAFTAR PUSTAKA

1. Sahrul, A. E. Minarno, and Y. Munarko, "Komparasi Arsitektur VGG16 dan MobileNet pada Klasifikasi Penyakit Daun Padi," Jurnal RESTI, 2021.
2. M. Y. A. Asseweth, "Klasifikasi Penyakit Daun Padi Menggunakan Algoritma Convolutional Neural Network (CNN)," Skripsi, Universitas Medan Area, 2022.
3. A. T. Huda, "Klasifikasi Penyakit Tanaman Padi Berdasarkan Citra Daun Menggunakan Convolutional Neural Network (CNN) Berbasis Arsitektur DenseNet," Skripsi, UIN Maulana Malik Ibrahim, 2024.
4. M. Hamdan, A. E. Minarno, and Y. Munarko, "Klasifikasi Tingkat Keparahan Penyakit Blast pada Daun Padi Menggunakan Convolutional Neural Network," Jurnal RESTI, 2021.
5. R. Shinta, "Klasifikasi Penyakit Daun Tanaman Padi Menggunakan Arsitektur DenseNet-121 Pada Convolutional Neural Network (CNN)," Skripsi, UIN Sultan Syarif Kasim Riau, 2024.

```