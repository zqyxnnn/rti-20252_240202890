# Arsitektur & Skema Model

Dokumen ini berisi rancangan arsitektur pemrosesan data citra, skema model VGG-19, DenseNet-169, dan mekanisme evaluasi pengujian independen.

## 1. Alur Pemrosesan Data (Pipeline)

```mermaid
graph TD
    A["Data Mentah Citra Daun Padi (.jpg Kaggle)"] --> B["Data Cleaning & Pelabelan 4 Kelas"]
    B --> C["Resize Resolusi (64x64 piksel) & Normalisasi Tensor"]
    C --> D["Data Augmentasi (Random Horizontal/Vertical Flip)"]
    D --> E["Data Splitting Dinamis (Seed 43-77)"]
    E --> F["Training Set (Fase Otomasi 35 Epoch)"]
    E --> G["Testing Set (Metrik Akurasi & F1-Score)"]

## 2. Arsitektur Model VGG-19 (Deep Learning Baseline)

graph TD
    A["Input Layer: 3D Tensor [Batch, 64, 64, 3]"] --> B["Block 1 & 2: 4 Conv Layers + MaxPool"]
    B --> C["Block 3 & 4: 8 Conv Layers + MaxPool"]
    C --> D["Block 5: 4 Conv Layers + MaxPool"]
    D --> E["Adaptive Average Pooling"]
    E --> F["Flatten Layer"]
    F --> G["Fully Connected Layer (Logits 4 Kelas)"]

## 3. Arsitektur Model DenseNet-169 (Intervensi Deep Feature)

graph TD
    A["Input Layer: 3D Tensor [Batch, 64, 64, 3]"] --> B["Convolution & MaxPool (7x7 Conv, Stride 2)"]
    B --> C["Dense Block 1 (6 layers) & Transition Layer 1"]
    C --> D["Dense Block 2 (12 layers) & Transition Layer 2"]
    D --> E["Dense Block 3 (32 layers) & Transition Layer 3"]
    E --> F["Dense Block 4 (32 layers)"]
    F --> G["Global Average Pooling (GAP)"]
    G --> H["Linear Classifier Output (4 Kelas dengan Softmax)"]

## 4. Hyperparameter Eksperimen Riil

### Konfigurasi Umum Ekstraksi Fitur
* **Image Input Size:** 64 x 64 piksel (RGB)
* **Optimizer:** Adam Optimizer
* **Learning Rate:** 0.001 (1e-3)
* **Batch Size:** 32
* **Total Epochs:** 35 per independent run
* **Total Independent Runs:** 35 kali pengulangan dinamis per skenario (Total 70 runs gabungan)
* **Target Classes:** 4 Kelas (Blas, Hawar Daun, Tungro, Sehat)

### Spesifikasi Arsitektur VGG-19 Baseline
* **Pretrained Weights:** VGG19_Weights.DEFAULT (ImageNet)
* **Feature Extractor:** Frozen Backbone (Konvolusi terkunci)
* **Classifier Head:** Custom Fully Connected Layer dengan Dropout Rate = 0.5
* **Loss Function:** Cross-Entropy Loss

### Spesifikasi Arsitektur DenseNet-169 Intervensi
* **Pretrained Weights:** DenseNet169_Weights.DEFAULT (ImageNet)
* **Feature Extractor:** Frozen Backbone dengan blok koneksi padat (k = 32)
* **Classifier Head:** Custom Linear Layer menyesuaikan representasi fitur GAP menuju 4 output nodes
* **Loss Function:** Cross-Entropy Loss