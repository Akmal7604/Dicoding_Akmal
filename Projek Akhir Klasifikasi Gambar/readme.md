
# Vegetable Image Classification with Convolutional Neural Network (CNN)

## 🥬 Project Overview
Proyek ini mengimplementasikan model Machine Learning untuk klasifikasi gambar sayuran menggunakan Convolutional Neural Network (CNN) dengan TensorFlow dan Keras.

## 🌟 Project Motivation
Tujuan utama proyek ini adalah mengembangkan model machine learning yang mampu mengklasifikasikan berbagai jenis sayuran berdasarkan gambar input dengan akurasi tinggi.

## 📊 Dataset
- **Sumber**: [Vegetables Dataset - Kaggle](https://www.kaggle.com/datasets/apadoss/vegetables-dataset)
- **Jumlah Kelas**: 15 Jenis Sayuran
- **Total Sampel**: 12.000 Gambar

## 🛠 Tech Stack
- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib

## 📁 Project Structure
```
submission/
├── tfjs_model/
│   ├── group1-shard1of1.bin
│   └── model.json
├── tflite/
│   ├── model.tflite
│   └── label.txt
├── saved_model/
│   ├── saved_model.pb
│   └── variables/
├── notebook.ipynb
├── README.md
└── requirements.txt
```

## 🚀 Model Architecture
### Arsitektur CNN
- Input Layer: 224x224x3 (RGB)
- Convolutional Layers:
  - Conv2D Layer 1: 32 filters, 3x3 kernel
  - Conv2D Layer 2: 64 filters, 3x3 kernel
  - Conv2D Layer 3: 128 filters, 3x3 kernel
- Pooling Layers: MaxPooling 2x2
- Batch Normalizations
- Dropout Layers
- Dense Layers:
  - 256 neurons
  - 128 neurons
- Output Layer: Softmax activation

### Model Performance
- Training Accuracy: 0.8948
- Test Accuracy: 0.9523

## 🔧 Installation

### Prerequisites
- Python 3.8+
- pip

### Setup Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## 🏃 How to Run

### Training
```bash
python train.py
```

### Inference
```python
from tensorflow.keras.models import load_model

# Load model
model = load_model('saved_model')

# Prediksi
predictions = model.predict(image)
```

## 📦 Model Conversion
Proyek ini menyediakan model dalam 3 format:
1. **SavedModel**: Format asli TensorFlow
2. **TF-Lite**: Optimasi untuk perangkat mobile
3. **TensorFlow.js**: Untuk aplikasi web

## 👥 Kontributor
- Muhamad Akmal Athallah

## 🙏 Acknowledgements
- Dataset oleh Apadoss (Kaggle)
- Terinspirasi oleh proyek klasifikasi gambar open-source
