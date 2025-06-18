# Laporan Proyek Machine Learning - Muhamad Akmal Athallah

## Domain Proyek

Proyek ini bertujuan untuk menganalisis kualitas udara di lingkungan urban dengan menggunakan data kualitas udara yang diukur dari beberapa sensor. Kualitas udara yang buruk dapat berdampak negatif pada kesehatan masyarakat dan kualitas hidup secara keseluruhan. Oleh karena itu, penting untuk memantau dan menganalisis data kualitas udara untuk memahami pola, membuat rekomendasi perbaikan, dan pada akhirnya **agar masyarakat dapat hidup dengan lebih sehat. Untuk mencapai hal tersebut, lembaga yang bertanggung jawab harus bisa mengidentifikasi dan menganalisa lebih lanjut tentang kualitas udara, salah satunya melalui proyek ini.**

---

## Business Understanding

### Problem Statements
1. **Pernyataan Masalah 1**: Bagaimana kita dapat memprediksi konsentrasi polutan tertentu (seperti CO, NOx, atau NO2) berdasarkan data historis?
2. **Pernyataan Masalah 2**: Apa faktor lingkungan (seperti suhu dan kelembapan) yang paling mempengaruhi konsentrasi polutan di udara?

### Goals
1. **Jawaban Pernyataan Masalah 1**: Mengembangkan model regresi yang mampu memprediksi konsentrasi polutan (fokus pada CO) berdasarkan fitur yang tersedia dalam dataset.
2. **Jawaban Pernyataan Masalah 2**: Melakukan analisis fitur untuk memahami pengaruh variabel lingkungan terhadap konsentrasi polutan.

### Solution Statements
- **Solusi 1**: Menggunakan algoritma regresi seperti Linear Regression dan Random Forest Regression untuk memprediksi konsentrasi polutan.
- **Solusi 2**: Melakukan analisis pentingnya fitur (*feature importance*) dari model Random Forest untuk menentukan kontribusi masing-masing variabel terhadap model prediksi.

---

## Data Understanding

### Dataset Info

Dataset yang digunakan dalam proyek ini adalah **AirQuality.csv**, yang bersumber dari [Kaggle: Air Quality Data Set](https://www.kaggle.com/datasets/fedesoriano/air-quality-data-set).

Informasi awal tentang dataset adalah sebagai berikut:
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 9471 entries, 0 to 9470
Data columns (total 17 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   Date           9357 non-null   object 
 1   Time           9357 non-null   object 
 2   CO(GT)         9357 non-null   object 
 3   PT08.S1(CO)    9357 non-null   float64
 4   NMHC(GT)       9357 non-null   float64
 5   C6H6(GT)       9357 non-null   object 
 6   PT08.S2(NMHC)  9357 non-null   float64
 7   NOx(GT)        9357 non-null   float64
 8   PT08.S3(NOx)   9357 non-null   float64
 9   NO2(GT)        9357 non-null   float64
 10  PT08.S4(NO2)   9357 non-null   float64
 11  PT08.S5(O3)    9357 non-null   float64
 12  T              9357 non-null   object 
 13  RH             9357 non-null   object 
 14  AH             9357 non-null   object 
 15  Unnamed: 15    0 non-null      float64
 16  Unnamed: 16    0 non-null      float64
dtypes: float64(10), object(7)
memory usage: 1.2+ MB
```

### Kondisi Data Awal
- **Jumlah Baris dan Kolom**: Dataset memiliki 9471 entri dan 17 kolom.
- **Nilai yang Hilang**: Beberapa kolom memiliki nilai yang hilang, khususnya kolom 'Unnamed: 15' dan 'Unnamed: 16' yang seluruhnya tidak memiliki nilai dan kolom lainnya dengan jumlah (9357 non-null).
- **Duplikasi**: Diperiksa dan tidak ditemukan duplikasi di dalam dataset.
- **Outlier**: Dilakukan pemeriksaan visual dan statistik untuk mendeteksi outlier. Nilai ekstrem mungkin membutuhkan penanganan lebih lanjut.

### Deskripsi Kolom
- **Date**: Tanggal pengukuran.
- **Time**: Waktu pengukuran.
- **CO(GT)**: Konsentrasi gas CO, yang dicatat sebagai objek dan membutuhkan konversi.
- **PT08.S1(CO)**: Respon sensor CO.
- **NMHC(GT)**: Non-Methane Hydrocarbons, konsentrasi gas hidrokarbon non-metan.
- **C6H6(GT)**: Konsentrasi benzena, yang juga dicatat sebagai objek.
- **PT08.S2(NMHC)**: Respon sensor NMHC.
- **NOx(GT)**: Konsentrasi gas NOx.
- **PT08.S3(NOx)**: Respon sensor NOx.
- **NO2(GT)**: Konsentrasi gas NO2.
- **PT08.S4(NO2)**: Respon sensor NO2.
- **PT08.S5(O3)**: Respon sensor Ozon.
- **T**: Suhu (dalam derajat Celsius), yang perlu dikonversikan.
- **RH**: Kelembapan relatif (persentase), yang perlu dikonversikan.
- **AH**: Absolute Humidity, yang juga perlu dikonversikan.
- **Unnamed: 15 & 16**: Kolom tidak relevan dengan semua nilai hilang dan dihapus.

---

## Data Preparation

Proses data preparation yang dilakukan meliputi:

1. **Pembersihan Data**:
   - **Menghapus Kolom yang Tidak Berguna**: Kolom 'Unnamed: 15' dan 'Unnamed: 16' dihapus. 
   - **Mengatasi Nilai yang Hilang**: Menghapus baris dengan nilai NaN di kolom sensitif menggunakan `df.dropna(inplace=True)`.
   - **Penghapusan Data Duplikat**: Memastikan tidak ada informasi yang redundan dalam dataset.
   - **Konversi Koma ke Titik**: Pada kolom numerik seperti 'CO(GT)' dan 'C6H6(GT)', koma diganti dengan titik dan dikonversi menjadi tipe float.
   - **Penanganan Eror dalam Kolom Waktu**: Kolom `Time` diformat dengan benar.

2. **Penyusunan Format Waktu**:
   - Mengonversi kolom `Date` dan `Time` menjadi satu kolom `Datetime` untuk analisis yang lebih mudah.  
   - Menyusul itu, kolom `Date` dan `Time` dihapus dengan `df.drop(columns=['Date', 'Time'], inplace=True)`.

3. **Normalisasi**:
   - Menggunakan `MinMaxScaler` untuk menormalkan data numerik agar model *machine learning* dapat belajar secara optimal.
   ```python
   from sklearn.preprocessing import MinMaxScaler

   scaler = MinMaxScaler()
   columns_to_normalize = [
       'CO(GT)', 'PT08.S1(CO)', 'NMHC(GT)', 'C6H6(GT)',
       'PT08.S2(NMHC)', 'NOx(GT)', 'PT08.S3(NOx)',
       'NO2(GT)', 'PT08.S4(NO2)', 'PT08.S5(O3)',
       'T', 'RH', 'AH'
   ]
   df[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])
   ```

4. **Pembagian Data**:
   - Data dibagi menjadi data latih (*training set*) dan data uji (*testing set*) dengan proporsi 80% untuk pelatihan dan 20% untuk pengujian.

---

## Modeling

Dalam tahapan modeling, dua algoritma regresi digunakan untuk memprediksi konsentrasi CO:

1. **Linear Regression**: Model sederhana yang mendasari hubungan linier antara variabel input dan output.
2. **Random Forest Regression**: Model *ensemble* yang dapat menangani data dengan hubungan non-linear dan umumnya lebih robust.

Parameter yang digunakan untuk model Random Forest Regressor yang dipilih sebagai model terbaik adalah:
```python
{'n_estimators': 100, 'random_state': 42}
```
Proses *hyperparameter tuning* dilakukan pada model Random Forest menggunakan *GridSearchCV* dengan 3 *folds cross-validation* untuk mengoptimalkan parameter. Sebanyak 108 kandidat kombinasi parameter dievaluasi. Parameter terbaik yang ditemukan melalui proses ini adalah:
```python
{'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 200}
```

Model Random Forest yang dihasilkan dari *hyperparameter tuning* ini mencapai metrik evaluasi sebagai berikut:
* Mean Absolute Error (MAE): 0.1056
* Root Mean Squared Error (RMSE): 0.2147
* R² Score: 0.6497

Namun, setelah perbandingan, model Random Forest yang dilatih **sebelum *hyperparameter tuning* ekstensif ini (dengan parameter default atau tuning awal)** menunjukkan performa MAE yang sedikit lebih baik (0.1052) dan dipilih untuk evaluasi akhir.

Kelebihan dan kekurangan algoritma yang digunakan adalah:
- **Linear Regression**: Kelebihan - sederhana dan interpretatif; Kekurangan - tidak dapat menangkap hubungan non-linear yang kompleks.
- **Random Forest Regression**: Kelebihan - dapat menangkap hubungan non-linear, lebih robust terhadap *overfitting* (dengan tuning yang tepat), dan dapat memberikan *feature importance*; Kekurangan - kurang interpretatif dibandingkan model linear dan membutuhkan lebih banyak komputasi.

Model terbaik dipilih berdasarkan performa metrik evaluasi, di mana Random Forest menunjukkan hasil yang lebih superior dibandingkan Linear Regression.

---

## Evaluation

Metrik evaluasi yang digunakan untuk menilai performa model adalah:
- **Mean Absolute Error (MAE)**: Mengukur rata-rata kesalahan absolut antara nilai yang diprediksi dan yang sebenarnya.
- **Root Mean Squared Error (RMSE)**: Mengukur akar dari rata-rata kesalahan kuadrat. Metrik ini memberikan bobot lebih pada kesalahan besar.
- **R² Score (Koefisien Determinasi)**: Menunjukkan proporsi varians dalam variabel dependen yang dapat diprediksi dari variabel independen.

Berikut adalah perbandingan hasil evaluasi pada *testing set* untuk kedua model yang dikembangkan:

| Model                 | Mean Absolute Error (MAE) | Root Mean Squared Error (RMSE) | R² Score |
| :-------------------- | :------------------------ | :----------------------------- | :------- |
| Linear Regression     | 0.1580                    | 0.2525                         | 0.5153   |
| Random Forest Regression (Pilihan) | **0.1052** | **0.2154** | **0.6475** |

Berdasarkan tabel di atas, model **Random Forest Regression** menunjukkan performa yang secara signifikan lebih baik daripada Linear Regression di semua metrik evaluasi yang digunakan untuk memprediksi konsentrasi CO. 

Untuk menjawab **Pernyataan Masalah 2** (faktor lingkungan yang paling mempengaruhi konsentrasi polutan), analisis *feature importance* dari model Random Forest akan sangat berguna. Fitur-fitur seperti `PT08.S1(CO)` (respon sensor CO), `C6H6(GT)` (Benzene), dan `PT08.S2(NMHC)` biasanya menunjukkan *importance* yang tinggi dalam memprediksi CO. Variabel lingkungan seperti `T` (Suhu) dan `RH` (Kelembapan Relatif) juga akan memiliki kontribusi yang dapat diukur. *Feature importance* ini akan memberikan wawasan tentang faktor-faktor mana yang paling dominan.

---

## Saran Pengembangan Lanjutan

Untuk pengembangan proyek di masa depan, beberapa hal dapat dipertimbangkan:
1. **Dataset yang Lebih Baru dan Lengkap**: Menggunakan dataset yang lebih baru dan mencakup periode waktu yang lebih panjang. Menambahkan data cuaca yang lebih detail (misalnya, kecepatan dan arah angin, tekanan atmosfer) dapat meningkatkan akurasi prediksi dan pemahaman korelasi.
2. **Relevansi Lokasi**: Menggunakan data yang relevan dengan lokasi spesifik yang ingin dianalisis untuk mendapatkan model yang lebih akurat dan rekomendasi yang lebih tepat sasaran.
3. **Eksplorasi Algoritma Lain**: Mencoba algoritma *machine learning* atau *deep learning* lain yang lebih canggih (misalnya, Gradient Boosting, LSTM untuk data deret waktu).
4. **Feature Engineering Lanjutan**: Membuat fitur-fitur baru dari data yang ada (misalnya, interaksi antar variabel, fitur berbasis waktu seperti jam dalam sehari atau hari dalam seminggu) untuk meningkatkan performa model.
5. **Prediksi Polutan Lain**: Mengembangkan model serupa untuk memprediksi konsentrasi polutan lain seperti NOx dan NO2 secara lebih mendalam, sesuai dengan lingkup awal *problem statement*.
6. **Deployment dan Monitoring**: Mengimplementasikan model dalam sistem *monitoring real-time* untuk memberikan peringatan dini dan informasi kualitas udara secara berkelanjutan.

---
