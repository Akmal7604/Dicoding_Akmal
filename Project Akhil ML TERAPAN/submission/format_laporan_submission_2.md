# Laporan Proyek Machine Learning - Muhamad Akmal Athallah

## Project Overview

Perkembangan teknologi musik digital telah menghasilkan volume musik yang sangat besar, membuat pengguna kesulitan menemukan lagu yang sesuai dengan preferensi mereka. Menurut penelitian terbaru dalam bidang sistem rekomendasi musik, pendekatan hybrid menggunakan Neural Collaborative Filtering (NCF) telah menunjukkan peningkatan signifikan dalam akurasi rekomendasi.

Sistem rekomendasi musik modern menghadapi tantangan kompleks dalam memahami preferensi musikal pengguna. Penelitian menunjukkan bahwa pendekatan deep learning dapat meningkatkan performa sistem rekomendasi dengan mengekstrak fitur laten dari metadata musik dan pola interaksi pengguna.

Tujuan utama proyek ini adalah mengembangkan sistem rekomendasi musik cerdas yang dapat:  
- Memahami karakteristik detail musik  
- Memberikan rekomendasi personal  
- Mengatasi keterbatasan sistem rekomendasi tradisional  


## Business Understanding  

### Problem Statements  
1. Kompleksitas Preferensi Musik  
   - Kesulitan menemukan lagu yang sesuai dengan preferensi personal  
   - Banyaknya variasi musik dalam dataset mempersulit rekomendasi manual  

2. Keterbatasan Fitur Rekomendasi Konvensional  
   - Sistem rekomendasi tradisional hanya fokus pada genre atau artis  
   - Kurangnya pertimbangan karakteristik detail musik seperti valence, energy, dan danceability  

3. Kebutuhan Personalisasi Pengalaman Musik  
   - Pengguna membutuhkan rekomendasi yang tepat sesuai mood dan aktivitas  
   - Kesulitan mengeksplorasi musik baru di luar zona nyaman  

### Goals  
1. Mengembangkan Sistem Rekomendasi Presisi  
   - Membuat algoritme yang mampu memahami preferensi musikal pengguna secara mendalam  
   - Menghasilkan rekomendasi yang akurat berdasarkan fitur musik kompleks  

2. Meningkatkan Pengalaman Eksplorasi Musik  
   - Memungkinkan pengguna menemukan lagu baru yang sesuai selera  
   - Mengurangi waktu pencarian musik manual  

3. Mengoptimalkan Algoritme Rekomendasi  
   - Memanfaatkan fitur multidimensi seperti valence, energy, danceability  
   - Menghasilkan rekomendasi yang dinamis dan adaptif  

### Solution Statements  
#### Hybrid Recommendation System  
- Mengkombinasikan collaborative filtering (dengan NCF) dan content-based filtering.
- Menggunakan fitur musik spesifik seperti *valence, danceability, energy, acousticness, instrumentalness, dan liveness* untuk menganalisis karakteristik lagu.
- Algoritme: Pendekatan hybrid yang mengintegrasikan *Neural Collaborative Filtering (NCF)* untuk menangkap pola kolaboratif dan preferensi laten, dengan *Content-Based Filtering (CBF)* yang menilai kemiripan berdasarkan atribut lagu. Skor dari kedua pendekatan ini dikombinasikan.
- Kelebihan:  
    - Personalisasi tingkat tinggi melalui pemahaman preferensi implisit.
    - Adaptif terhadap perubahan preferensi pengguna (jika model diperbarui secara berkala).
    - Mengatasi *masalah cold start* (khususnya untuk lagu baru) secara efektif berkat komponen Content-Based Filtering.

## Data Understanding

Dataset yang digunakan dalam proyek sistem rekomendasi musik ini bersumber dari Kaggle, berjudul "Music Recommendation System Datasets" ([https://www.kaggle.com/datasets/mohamedjamyl/music-recommendation-system-datasets](https://www.kaggle.com/datasets/mohamedjamyl/music-recommendation-system-datasets)). Dataset ini menyediakan kumpulan fitur yang kaya untuk setiap lagu, memungkinkan analisis mendalam terhadap karakteristik musik.

### Struktur dan Dimensi Dataset Awal
Dataset awal yang dimuat terdiri dari **170.653 baris (lagu)** dan **31 kolom (fitur)**. Setiap baris merepresentasikan satu lagu unik beserta atribut-atributnya.

### Kondisi Data Awal
Berdasarkan output `df.info()`, kondisi data awal adalah sebagai berikut:
* Sebagian besar kolom tidak memiliki nilai yang hilang (*missing values*).
* Terdapat *missing values* pada dua kolom:
    * `type_of_song_by_loudness(dB)`: Memiliki **9** nilai yang hilang (170.644 dari 170.653 baris terisi).
    * `type_of_tempo_in_Beats_Per_Minute(BPM)`: Memiliki **5.418** nilai yang hilang (165.235 dari 170.653 baris terisi).
* Tipe data pada kolom bervariasi, mencakup `float64` (untuk fitur audio numerik), `int64` (untuk fitur seperti tahun, explicit, dll.), dan `object` (umumnya untuk teks seperti nama, ID, tanggal, dan kategori turunan).

Penanganan *missing values* dan transformasi tipe data (jika diperlukan) akan dibahas lebih lanjut pada bagian Data Preparation.

### Deskripsi Fitur Dataset
Berikut adalah deskripsi untuk ke-31 fitur yang ada dalam dataset awal:

1.  **`valence`** (float64): Mengukur positivitas musik yang disampaikan oleh sebuah lagu. Nilai tinggi menunjukkan kegembiraan (misalnya, senang, ceria), sedangkan nilai rendah menunjukkan negativitas (misalnya, sedih, marah). Rentang 0.0 hingga 1.0.
2.  **`year`** (int64): Tahun rilis lagu.
3.  **`acousticness`** (float64): Ukuran kepercayaan apakah lagu tersebut akustik. Nilai 1.0 merepresentasikan keyakinan tinggi bahwa lagu tersebut akustik. Rentang 0.0 hingga 1.0.
4.  **`artists`** (object): Nama artis atau para artis yang membawakan lagu. Bisa berisi lebih dari satu nama jika lagu tersebut merupakan kolaborasi.
5.  **`danceability`** (float64): Menggambarkan seberapa cocok sebuah lagu untuk menari berdasarkan kombinasi elemen musik termasuk tempo, stabilitas ritme, kekuatan ketukan, dan keteraturan secara keseluruhan. Nilai 0.0 berarti paling tidak bisa ditarikan dan 1.0 berarti paling bisa ditarikan.
6.  **`duration_ms`** (int64): Durasi lagu dalam milidetik.
7.  **`energy`** (float64): Ukuran persepsi intensitas dan aktivitas dalam sebuah lagu. Lagu yang energetik biasanya terasa cepat, keras, dan berisik. Rentang 0.0 hingga 1.0.
8.  **`explicit`** (int64): Menunjukkan apakah lirik atau konten lagu tersebut eksplisit (1 = eksplisit, 0 = tidak eksplisit/bersih).
9.  **`id`** (object): ID unik untuk setiap lagu (track ID dari Spotify).
10. **`instrumentalness`** (float64): Memprediksi apakah sebuah lagu tidak mengandung vokal. Suara "Ooh" dan "aah" dianggap sebagai instrumental dalam konteks ini. Trek rap atau spoken word jelas "vokal". Semakin dekat nilai instrumentalness ke 1.0, semakin besar kemungkinan trek tersebut tidak mengandung konten vokal. Rentang 0.0 hingga 1.0.
11. **`key`** (int64): Kunci nada dasar lagu. Direpresentasikan sebagai integer yang memetakan ke nada menggunakan notasi Pitch Class standar (misalnya, 0 = C, 1 = C♯/D♭, 2 = D, dan seterusnya).
12. **`liveness`** (float64): Mendeteksi kehadiran audiens dalam rekaman. Nilai liveness yang lebih tinggi menunjukkan probabilitas yang lebih besar bahwa lagu tersebut direkam secara live. Rentang 0.0 hingga 1.0.
13. **`loudness`** (float64): Keseluruhan kenyaringan lagu dalam desibel (dB). Nilai loudness dirata-ratakan di seluruh lagu dan berguna untuk membandingkan kenyaringan relatif antar lagu.
14. **`mode`** (int64): Menunjukkan modalitas (mayor atau minor) dari sebuah lagu, yaitu jenis tangga nada dari mana konten melodinya berasal. Mayor direpresentasikan oleh 1 dan minor oleh 0.
15. **`name`** (object): Judul lagu.
16. **`popularity`** (int64): Popularitas lagu. Nilainya berkisar antara 0 hingga 100, dengan 100 sebagai yang paling populer. Popularitas dihitung berdasarkan algoritma dan sebagian besar didasarkan pada jumlah total pemutaran lagu dan seberapa baru pemutaran tersebut.
17. **`release_date`** (object): Tanggal rilis lagu. Dapat berupa format tanggal lengkap atau hanya tahun.
18. **`speechiness`** (float64): Mendeteksi keberadaan kata-kata yang diucapkan dalam sebuah lagu. Semakin eksklusif rekaman tersebut bersifat seperti ucapan (misalnya, acara bincang-bincang, buku audio, puisi), semakin mendekati 1.0 nilai atributnya. Rentang 0.0 hingga 1.0.
19. **`tempo`** (float64): Perkiraan tempo lagu secara keseluruhan dalam ketukan per menit (BPM). Tempo adalah kecepatan atau laju sebuah musik.
20. **`duration_min`** (float64): Durasi lagu dalam menit (kemungkinan besar merupakan hasil konversi dari `duration_ms`).
21. **`type_of_song_by_valence`** (object): Kategori turunan berdasarkan nilai `valence`
22. **`type_of_song_by_acousticness`** (object): Kategori turunan berdasarkan nilai `acousticness` 
23. **`type_of_song_by_danceability`** (object): Kategori turunan berdasarkan nilai `danceability` 
24. **`Energy_Level_of_the_Song`** (object): Kategori turunan berdasarkan nilai `energy` 
25. **`type_of_song_by_instrumentalness`** (object): Kategori turunan berdasarkan nilai `instrumentalness` 
26. **`type_of_song_by_liveness`** (object): Kategori turunan berdasarkan nilai `liveness` 
27. **`type_of_song_by_loudness(dB)`** (object): Kategori turunan berdasarkan nilai `loudness` *Memiliki 9 missing values*.
28. **`type_of_song_by_mode`** (object): Kategori turunan berdasarkan nilai `mode` 
29. **`type_of_popularity`** (object): Kategori turunan berdasarkan nilai `popularity`
30. **`type_of_song_by_speechiness`** (object): Kategori turunan berdasarkan nilai `speechiness` 
31. **`type_of_tempo_in_Beats_Per_Minute(BPM)`** (object): Kategori turunan berdasarkan nilai `tempo` *Memiliki 5.418 missing values*.

---

## Data Preparation

Tahapan persiapan data adalah langkah fundamental dalam alur kerja machine learning, yang bertujuan untuk membersihkan, mentransformasi, dan menstrukturkan data mentah menjadi format yang optimal untuk pelatihan model. Proses ini dalam proyek ini mencakup pembersihan data awal, rekayasa fitur (feature engineering) yang ekstensif, pra-pemrosesan data inti seperti normalisasi dan encoding, serta pembagian dataset.

1.  **Pembersihan Data Awal**
    * Langkah pertama adalah menangani nilai yang hilang (*missing values*). Semua baris yang mengandung setidaknya satu nilai *null* dihapus dari dataset menggunakan metode `dropna()`.
    * Setelah penghapusan baris, indeks DataFrame direset menggunakan `reset_index(drop=True)` untuk memastikan barisan indeks yang kontinu dan menghindari masalah yang mungkin timbul karena indeks yang hilang.
    * Langkah-langkah ini bertujuan untuk memastikan dataset bersih dan siap untuk tahap pemrosesan selanjutnya. Setelah pembersihan, dataset terdiri dari 165.235 entri yang siap digunakan.

2.  **Rekayasa Fitur (Feature Engineering)**
    Rekayasa fitur dilakukan dalam dua tahap utama, pertama melalui fungsi `engineer_features()` dan kemudian sebagian kecil saat pra-pemrosesan data inti. Tujuannya adalah untuk menghasilkan fitur-fitur baru yang lebih deskriptif dan berpotensi meningkatkan performa model.

    * **Transformasi dan Kategorisasi Fitur (dalam `engineer_features()`):**
        * **Konversi Durasi**: Fitur `duration_ms` (durasi lagu dalam milidetik) dikonversi menjadi `duration_min` (durasi dalam menit) untuk interpretasi skala yang lebih mudah.
        * **Pembuatan Fitur Kategorikal Baru**: Sebelas fitur kategorikal baru dibuat dari fitur-fitur audio numerik yang ada menggunakan fungsi `pd.cut()`. Proses ini membagi rentang nilai setiap fitur numerik menjadi beberapa kategori (bin) berdasarkan ambang batas yang telah ditentukan. Fitur-fitur ini meliputi:
            * `type_of_song_by_valence` (misalnya, "Sad song", "Happy song")
            * `type_of_song_by_acousticness` (misalnya, "Highly electronic song", "Mostly acoustic song")
            * `type_of_song_by_danceability` (misalnya, "Not suitable for dance", "Highly danceable song")
            * `Energy_Level_of_the_Song` (misalnya, "Slow song", "High-energy song")
            * `type_of_song_by_instrumentalness` (misalnya, "Song clearly contains lyrics", "Nearly purely instrumental song")
            * `type_of_song_by_liveness` (misalnya, "Pure studio recordings", "Clearly a live recording")
            * `type_of_song_by_loudness(dB)` (misalnya, "Quieter Sound", "Loud song")
            * `type_of_song_by_mode` (berdasarkan fitur `mode`, menghasilkan "Sad tone (Minor)" atau "Happy tone (Major)")
            * `type_of_song_by_speechiness` (misalnya, "Mostly instrumental song", "Podcasts or speech-heavy rap")
            * `type_of_tempo_in_Beats_Per_Minute(BPM)` (misalnya, "Slow song", "Fast-paced song")
            Penanganan nilai `NaN` juga dilakukan untuk fitur kategorikal yang dihasilkan dari `loudness` dan `tempo` jika ada nilai yang berada di luar rentang bin yang ditentukan. DataFrame setelah tahap ini memiliki kolom-kolom baru yang kaya akan informasi kualitatif tentang setiap lagu, seperti yang terlihat pada contoh output: `type_of_song_by_valence` dan `type_of_song_by_acousticness`.

    * **Pembuatan Fitur Target Biner (dalam `prepare_data()`):**
        * Sebuah fitur target biner bernama `is_popular_binary` dibuat dari fitur `popularity` (yang kemudian dinormalisasi). Lagu diklasifikasikan sebagai populer (`1`) jika nilai `popularity`-nya lebih tinggi dari median popularitas keseluruhan dataset, dan sebaliknya (`0`). Fitur ini krusial karena akan menjadi variabel target yang diprediksi oleh model NCF.

3.  **Pra-pemrosesan Data Inti (dalam `prepare_data()`)**
    Setelah rekayasa fitur awal, data melewati tahap pra-pemrosesan lebih lanjut.

    * **Normalisasi Fitur Numerik**:
        * Fitur-fitur numerik diskalakan menggunakan `MinMaxScaler` dari Scikit-learn, yang mengubah setiap fitur ke rentang antara 0 dan 1.
        * Normalisasi ini penting untuk menyeimbangkan kontribusi setiap fitur selama pelatihan model, mencegah fitur dengan skala nilai besar mendominasi fitur lainnya.
        * Fitur-fitur yang dinormalisasi (sesuai variabel `NUMERIC_FEATURES_FOR_SCALING`) adalah:
            * `valence`, `danceability`, `energy`, `acousticness`, `instrumentalness`, `liveness`, `loudness`, `tempo`, `duration_min` (hasil rekayasa fitur sebelumnya), dan `popularity`.
    * **Encoding Fitur Kategorikal**:
        * **Encoding Artis**: Fitur `artists` (nama artis) diubah menjadi representasi numerik menggunakan `LabelEncoder`. Setiap artis unik mendapat ID numerik, yang disimpan dalam kolom baru `artist_encoded`. Encoder ini disimpan secara global (`le_artists_global`).
        * **Encoding ID Lagu**: Fitur `id` (ID unik asli lagu) juga di-encode menggunakan `LabelEncoder` menjadi indeks numerik (dari 0 hingga N-1) dan disimpan dalam kolom `song_index_encoded`. Ini penting untuk layer embedding item pada model NCF. Encoder ini juga disimpan secara global (`le_song_id_global`).
        Contoh output setelah tahap ini menunjukkan kolom-kolom baru seperti `artist_encoded`, `song_index_encoded`, dan `is_popular_binary`.

4.  **Pembagian Dataset (Train-Test Split)**
    * Setelah semua langkah pra-pemrosesan dan rekayasa fitur selesai, dataset yang telah bersih dan diperkaya kemudian dibagi menjadi dua subset: data latih (*training set*) dan data uji (*test set*).
    * Pembagian ini dilakukan menggunakan fungsi `train_test_split` dari Scikit-learn (diimplementasikan dalam fungsi `split_data()` pada kode).
    * Tujuan utama pembagian ini adalah untuk melatih model pada data latih dan kemudian mengevaluasi kinerjanya pada data uji, yang merupakan data baru bagi model.
    * Proporsi pembagian yang digunakan adalah 80% untuk data latih dan 20% untuk data uji (`test_size=0.2`), menghasilkan 132.188 sampel data latih dan 33.047 sampel data uji.
    * Parameter `random_state=42` digunakan untuk memastikan hasil pembagian yang konsisten dan reproduktif.
    * Parameter `stratify=df_to_split['is_popular_binary']` digunakan untuk memastikan bahwa proporsi kelas target (`is_popular_binary`) terjaga secara seimbang di kedua set data (latih dan uji), yang sangat penting untuk tugas klasifikasi.

---

## Modeling

Sistem rekomendasi musik ini mengadopsi pendekatan hybrid, dirancang untuk memberikan rekomendasi lagu yang relevan dan beragam. Pendekatan ini secara cerdas mengintegrasikan dua metode utama: *Neural Collaborative Filtering* (NCF) dan *Content-Based Filtering* (CBF). NCF dimanfaatkan untuk memahami preferensi laten pengguna (dalam konteks ini, 'artis' dianggap sebagai 'pengguna') berdasarkan pola interaksi historis (popularitas lagu) dan fitur-fitur lagu itu sendiri. Sementara itu, CBF berfokus pada analisis kemiripan antar lagu berdasarkan atribut musik intrinsiknya. Kombinasi keduanya bertujuan untuk menghasilkan rekomendasi yang tidak hanya personal tetapi juga mampu mengatasi beberapa keterbatasan yang mungkin dimiliki oleh masing-masing metode jika digunakan secara terpisah.

### 1. Arsitektur Model NCF (Neural Collaborative Filtering)

Komponen inti dari sisi *collaborative filtering* (yang diperkaya dengan fitur konten) adalah model NCF. Model ini secara spesifik dirancang untuk memprediksi probabilitas interaksi antara pengguna (artis) dan item (lagu)—dalam kasus ini, apakah sebuah lagu akan populer (`is_popular_binary`). Model ini juga memperhitungkan serangkaian fitur audio tambahan dari lagu untuk meningkatkan akurasi prediksinya.

* **Input Layer**: Model menerima tiga jenis input:
    * Input Pengguna (`user_input_artist`): ID pengguna (artis yang telah di-encode menggunakan `artist_encoded`). Bentuk: `(1,)`.
    * Input Item/Lagu (`item_input_song_index`): ID lagu (indeks lagu yang telah di-encode menggunakan `song_index_encoded`). Bentuk: `(1,)`.
    * Input Fitur Tambahan (`additional_features_input`): Sebuah vektor yang berisi 5 fitur numerik lagu yang telah dinormalisasi, yaitu: `'valence'`, `'danceability'`, `'energy'`, `'acousticness'`, dan `'instrumentalness'`. Bentuk: `(5,)`.

* **Embedding Layer**: Layer ini bertugas untuk mengubah ID pengguna dan ID item yang bersifat diskrit menjadi representasi vektor padat (vektor laten) yang dapat diproses oleh neural network.
    * Embedding Pengguna (`user_embedding`): Mengubah ID pengguna menjadi vektor laten dengan dimensi 64 (`latent_dim=64`). Dilengkapi dengan regularisasi L2 (`embeddings_regularizer=l2(0.001)`) untuk mencegah overfitting.
    * Embedding Item (`item_embedding`): Mengubah ID lagu menjadi vektor laten dengan dimensi 64 (`latent_dim=64`). Juga dilengkapi dengan regularisasi L2 (`embeddings_regularizer=l2(0.001)`).

* **Arsitektur Neural Network**: Setelah embedding, vektor-vektor tersebut diproses melalui beberapa layer:
    1.  **Flatten Layer**: Vektor laten pengguna dan item yang dihasilkan oleh embedding layer di-flatten (diratakan) menjadi vektor satu dimensi.
    2.  **Concatenate Layer**: Hasil flatten dari embedding pengguna, embedding item, dan input fitur tambahan (`additional_features_input`) digabungkan menjadi satu vektor fitur yang komprehensif.
    3.  **Layer Fully Connected (Dense) Pertama**: Terdiri dari 128 neuron dengan fungsi aktivasi ReLU. Regularisasi kernel L2 (`kernel_regularizer=l2(0.001)`) diterapkan pada layer ini.
    4.  **Dropout Layer Pertama**: Dengan *rate* 0.4 (`Dropout(0.4)`), layer ini secara acak menonaktifkan sebagian neuron selama pelatihan untuk lebih lanjut mencegah overfitting.
    5.  **Layer Fully Connected (Dense) Kedua**: Terdiri dari 64 neuron dengan fungsi aktivasi ReLU dan regularisasi kernel L2.
    6.  **Dropout Layer Kedua**: Dengan *rate* 0.2 (`Dropout(0.2)`).
    7.  **Layer Output**: Satu neuron dengan fungsi aktivasi Sigmoid. Layer ini menghasilkan output berupa probabilitas (nilai antara 0 dan 1) yang menunjukkan kemungkinan lagu tersebut dianggap populer.

### 2. Metode Kompilasi Model NCF

Model NCF yang telah dirancang arsitekturnya kemudian dikompilasi dengan konfigurasi sebagai berikut, yang menentukan bagaimana model akan belajar:
* **Optimizer**: `Adam`, sebuah algoritma optimasi yang efisien dan umum digunakan, dengan laju pembelajaran (learning rate) default `0.001`.
* **Loss Function**: `binary_crossentropy`. Fungsi loss ini sangat sesuai untuk tugas klasifikasi biner seperti memprediksi apakah sebuah lagu populer atau tidak.
* **Metrik Evaluasi**: Serangkaian metrik digunakan untuk memantau kinerja model selama pelatihan dan evaluasi:
    * `accuracy`: Akurasi keseluruhan model dalam mengklasifikasikan lagu.
    * `KerasPrecision` (dengan nama `precision`): Proporsi prediksi positif yang benar-benar positif.
    * `KerasRecall` (dengan nama `recall`): Proporsi kasus positif aktual yang berhasil diidentifikasi dengan benar oleh model.

### 3. Mekanisme Rekomendasi Hybrid

Untuk menghasilkan rekomendasi lagu yang final dan komprehensif, sistem ini mengandalkan fungsi `hybrid_recommend()`. Fungsi ini mengkombinasikan skor dari dua pendekatan utama (NCF dan CBF) untuk setiap lagu kandidat.

* **Skor Neural Collaborative Filtering (NCF)**: Skor ini dihasilkan oleh model NCF yang telah dilatih (`trained_ncf_model`) dan diakses melalui fungsi `recommend_ncf_pure()`. Skor NCF merefleksikan prediksi model mengenai seberapa cocok atau populer sebuah lagu bagi pengguna (artis) tertentu, berdasarkan pola interaksi yang telah dipelajari dan fitur-fitur lagu yang menjadi input NCF.
* **Skor Content-Based Filtering (CBF)**: Skor ini dihitung berdasarkan kemiripan fitur audio intrinsik antar lagu. Proses ini, yang dienkapsulasi dalam fungsi `content_based_similarity_scores()` dan digunakan oleh `recommend_content_based_pure()`, memanfaatkan 6 fitur audio utama: `'valence'`, `'danceability'`, `'energy'`, `'acousticness'`, `'instrumentalness'`, dan `'liveness'`. Jarak Euclidean dihitung untuk mengukur ketidakmiripan antar lagu, yang kemudian dikonversi menjadi skor kemiripan. Skor kemiripan CBF ini selanjutnya dinormalisasi menggunakan Min-Max scaling agar berada dalam rentang [0,1] saat digunakan dalam fungsi `hybrid_recommend()`.
* **Skor Hibrida**: Dalam fungsi `hybrid_recommend()`, skor NCF dan skor CBF yang telah dinormalisasi digabungkan. Secara default, digunakan pembobotan seimbang (masing-masing dengan bobot 0.5) untuk menghitung skor hibrida akhir. Lagu-lagu kemudian diurutkan berdasarkan skor hibrida tertinggi ini, dan Top-N lagu disajikan sebagai rekomendasi. Keseluruhan proses ini, mulai dari input pengguna hingga output rekomendasi dari ketiga metode, difasilitasi oleh fungsi `recommend_by_song_title_all_methods()` yang menerima input berupa judul lagu.

### 4. Contoh Hasil Rekomendasi Top-N

Untuk memberikan gambaran konkret mengenai output sistem, berikut adalah contoh hasil rekomendasi Top-N yang dihasilkan ketika pengguna mencari rekomendasi berdasarkan sebuah lagu. Proses ini melibatkan pemanggilan fungsi `recommend_by_song_title_all_methods()` dengan sebuah judul lagu sebagai input.

**Input Judul Lagu untuk Rekomendasi:** `Kite`
*(Sistem mengidentifikasi lagu referensi sebagai: 'Being For The Benefit Of Mr. Kite! - Remastered 2009' oleh ['The Beatles'])*

**Output Top-5 Rekomendasi yang Dihasilkan:**

**A. Rekomendasi NCF Murni (untuk artis: ['The Beatles'])**
Tabel berikut menunjukkan lagu-lagu yang diprediksi oleh model NCF memiliki skor kecocokan/popularitas tertinggi untuk artis 'The Beatles'.

| Judul Lagu                            | Artis                           | Popularitas | Skor NCF |
| :------------------------------------ | :------------------------------ | :---------- | :------- |
| Joan of Arc                           | ['Night Lovell', '$uicideBoy$'] | 0.65        | 0.988991 |
| Whole Lotta Weed                      | ['Project Pat']                 | 0.36        | 0.988954 |
| Hood Hop                              | ['J-Kwon']                      | 0.37        | 0.988665 |
| Whistle While You Twurk (ColliPark Mix) | ['Ying Yang Twins']             | 0.47        | 0.988165 |
| Kings Never Die                       | ['Eminem', 'Gwen Stefani']      | 0.65        | 0.988084 |

**B. Rekomendasi Content-Based Filtering (CBF) Murni**
Tabel berikut menampilkan lagu-lagu yang memiliki kemiripan fitur audio tertinggi dengan lagu referensi 'Being For The Benefit Of Mr. Kite!'.

| Judul Lagu                                 | Artis                | Popularitas | Valence | Danceability |
| :----------------------------------------- | :------------------- | :---------- | :------ | :----------- |
| Shaman's Blues                             | ['The Doors']        | 0.40        | 0.734   | 0.502626     |
| I Can't Believe That You're In Love With Me  | ['Dinah Washington'] | 0.15        | 0.690   | 0.526209     |
| An Old Fashioned Love Song                 | ['Three Dog Night']  | 0.37        | 0.744   | 0.498339     |
| Inner City Blues (Make Me Wanna Holler)    | ['Gil Scott-Heron']  | 0.36        | 0.742   | 0.511202     |
| I've Been Watching You (Move Your Sexy Body) | ['Parliament']       | 0.31        | 0.689   | 0.545503     |

**C. Rekomendasi Hybrid**
Tabel berikut adalah hasil akhir dari sistem hybrid, yang mengkombinasikan skor NCF dan CBF.

| Judul Lagu                                 | Artis                | Popularitas | Skor Hybrid | Skor CBF (Norm) | Skor NCF |
| :----------------------------------------- | :------------------- | :---------- | :---------- | :-------------- | :------- |
| Shaman's Blues                             | ['The Doors']        | 0.40        | 0.914018    | 0.962288        | 0.865749 |
| I Can't Believe That You're In Love With Me  | ['Dinah Washington'] | 0.15        | 0.906792    | 0.933130        | 0.880455 |
| I've Been Watching You (Move Your Sexy Body) | ['Parliament']       | 0.31        | 0.899673    | 0.916823        | 0.882523 |
| An Old Fashioned Love Song                 | ['Three Dog Night']  | 0.37        | 0.894511    | 0.928597        | 0.860426 |
| Independence Day                           | ['David Byrne']      | 0.31        | 0.892122    | 0.904273        | 0.879972 |

---

## Evaluation

Evaluasi sistem rekomendasi musik ini dilakukan secara komprehensif, mencakup dua aspek utama:
1.  **Evaluasi Performa Model Neural Collaborative Filtering (NCF)**: Penilaian terhadap kemampuan model NCF sebagai komponen inti dalam tugas klasifikasi untuk memprediksi popularitas lagu berdasarkan konteks pengguna (artis) dan fitur lagu.
2.  **Evaluasi Kualitas Rekomendasi Top-N**: Penilaian terhadap kualitas daftar rekomendasi yang dihasilkan oleh sistem Content-Based Filtering (CBF) murni dan sistem Hybrid, dengan menggunakan metrik kuantitatif (Precision@K, Recall@K, NDCG@K) serta analisis kualitatif output rekomendasi.

### 1. Evaluasi Performa Model NCF (Klasifikasi Popularitas)

Komponen NCF dilatih sebagai model klasifikasi biner dengan tujuan memprediksi apakah sebuah lagu akan dianggap "populer" (berdasarkan target `is_popular_binary`). Performanya dievaluasi menggunakan metrik klasifikasi standar selama proses pelatihan, dengan data uji (`test_df`) digunakan sebagai set validasi.

**a. Riwayat Metrik Training dan Validasi NCF**

Model NCF dilatih selama maksimal 10 epoch dengan mekanisme `EarlyStopping` yang memantau `val_accuracy` (dengan `patience=10`). Ringkasan metrik dari proses training model NCF:

| Epoch | Loss Training | Akurasi Training | Presisi Training | Recall Training | Loss Validasi | Akurasi Validasi | Presisi Validasi | Recall Validasi |
| :---- | :------------ | :--------------- | :--------------- | :-------------- | :------------ | :--------------- | :--------------- | :-------------- |
| 1     | 0.6112        | 0.7973 (79.73%)  | 0.7943           | 0.8002          | 0.4999        | 0.8149 (81.49%)  | 0.8226           | 0.8011          |
| 2     | 0.4886        | 0.8211 (82.11%)  | 0.8237           | 0.8153          | 0.4657        | 0.8259 (82.59%)  | 0.8132           | 0.8446          |
| 3     | 0.4585        | 0.8324 (83.24%)  | 0.8370           | 0.8238          | 0.4546        | 0.8331 (83.31%)  | 0.8457           | 0.8131          |
| 4     | 0.4333        | 0.8433 (84.33%)  | 0.8525           | 0.8287          | 0.4367        | **0.8343 (83.43%)** | 0.8493           | 0.8112          |
| 5     | 0.4135        | 0.8491 (84.91%)  | 0.8594           | 0.8332          | 0.4411        | 0.8326 (83.26%)  | 0.8148           | 0.8592          |
| 6     | 0.4037        | 0.8525 (85.25%)  | 0.8667           | 0.8317          | 0.4362        | 0.8338 (83.38%)  | 0.8554           | 0.8019          |
| 7     | 0.4001        | 0.8535 (85.35%)  | 0.8672           | 0.8336          | 0.4342        | 0.8300 (83.00%)  | 0.8146           | 0.8526          |
| 8     | 0.3964        | 0.8519 (85.19%)  | 0.8664           | 0.8307          | 0.4291        | 0.8313 (83.13%)  | 0.8181           | 0.8503          |
| 9     | 0.3938        | 0.8525 (85.25%)  | 0.8670           | 0.8314          | 0.4413        | 0.8294 (82.94%)  | 0.8026           | 0.8719          |
| 10    | 0.3923        | 0.8521 (85.21%)  | 0.8665           | 0.8311          | 0.4284        | **0.8346 (83.46%)** | 0.8450           | 0.8179          |
*Catatan: Akurasi validasi terbaik yang dicapai adalah sekitar 83.46%. Pelatihan berhenti setelah 10 epoch karena mencapai jumlah epoch maksimum yang ditetapkan.*

**b. Analisis Performa Training Model NCF**

* **Karakteristik Pembelajaran**: Model NCF menunjukkan progres pembelajaran yang baik. *Loss training* menurun secara konsisten dari 0.6112 menjadi 0.3923, sementara *akurasi training* meningkat dari 79.73% menjadi 85.21%. Ini mengindikasikan bahwa model mampu mempelajari pola dari data training.
* **Performa Validasi**: *Akurasi validasi* mencapai puncaknya di sekitar 83.46% pada epoch ke-10, setelah berfluktuasi. *Loss validasi* juga menunjukkan tren penurunan, mencapai nilai terendah sekitar 0.4284.
* **Indikasi Overfitting**: Terdapat selisih antara performa training dan validasi (misalnya, akurasi training 85.21% vs. validasi 83.46% di epoch terakhir). Meskipun tidak seekstrem contoh sebelumnya, selisih ini tetap mengindikasikan adanya kecenderungan *overfitting*, di mana model mulai menghafal data training sedikit lebih baik daripada kemampuannya untuk generalisasi ke data validasi. Namun, penggunaan regularisasi L2 dan dropout yang telah disesuaikan tampaknya membantu mengendalikan overfitting menjadi lebih moderat.

**c. Interpretasi Hasil Training NCF**

* **Potensi Model NCF**: Dengan akurasi validasi sekitar 83.46%, model NCF menunjukkan kemampuan yang cukup baik dalam membedakan lagu yang cenderung populer dari yang tidak, dalam konteks artis tertentu dan dengan memanfaatkan fitur-fitur lagu. Ini menandakan bahwa arsitektur dan fitur yang dipilih memiliki potensi.
* **Tantangan Generalisasi**: Meskipun lebih terkendali, *overfitting* tetap menjadi area yang perlu diperhatikan.

### 2. Evaluasi Kualitas Rekomendasi Top-N

Evaluasi kualitas daftar rekomendasi (Top-N) dilakukan untuk sistem CBF Murni dan Hybrid. Pendekatan ini menggunakan metrik kuantitatif standar (Precision@K, Recall@K, NDCG@K) dan dilengkapi dengan analisis kualitatif output rekomendasi.

**a. Definisi Ground Truth untuk Evaluasi Peringkat Kuantitatif**
Untuk menghitung metrik peringkat, "ground truth" (item yang dianggap relevan) didefinisikan sebagai **lagu-lagu lain dari artis yang sama** dengan lagu input (referensi) yang ada dalam dataset. Ini adalah pendekatan umum ketika tidak ada data interaksi eksplisit pengguna-item yang detail. Evaluasi dilakukan pada 10 sampel lagu acak dari `test_df` dengan K=10.

**b. Hasil Evaluasi Kuantitatif Peringkat (K=10)**

| Sistem Rekomendasi | Rata-rata Precision@10 | Rata-rata Recall@10 | Rata-rata NDCG@10 |
| :----------------- | :--------------------- | :------------------ | :---------------- |
| CBF Murni          | 0.0300                 | 0.0020              | 0.1920            |
| Hybrid             | 0.0300                 | 0.0020              | 0.1920            |

**c. Analisis Hasil Evaluasi Kuantitatif Peringkat**

* **Skor Metrik**: Hasil Precision@10 dan Recall@10 untuk kedua sistem (CBF Murni dan Hybrid) menunjukkan skor yang relatif rendah (P@10 = 0.0300, R@10 = 0.0020). Skor NDCG@10 (0.1920) juga tergolong moderat.
* **Kesamaan Skor CBF dan Hybrid**: Skor yang identik untuk CBF Murni dan Hybrid pada sampel evaluasi ini menarik. Ini bisa mengindikasikan beberapa kemungkinan:
    1.  Pada 10 lagu sampel yang dievaluasi, skor NCF mungkin tidak cukup kuat atau beragam untuk mengubah peringkat yang didominasi oleh skor CBF setelah normalisasi dan pembobotan dalam sistem hybrid.
    2.  Definisi ground truth (lagu dari artis yang sama) mungkin lebih mudah dipenuhi oleh logika CBF (jika artis cenderung memiliki suara/fitur yang konsisten) dibandingkan dengan prediksi NCF yang mungkin lebih fokus pada popularitas umum atau asosiasi artis yang lebih luas.
    3.  Jumlah sampel evaluasi (10 lagu) mungkin belum cukup besar untuk menangkap perbedaan kinerja yang signifikan antara kedua metode pada metrik ini.
* **Interpretasi Skor Rendah**: Skor Precision dan Recall yang rendah dapat disebabkan oleh beberapa faktor:
    * **Sifat Ground Truth**: Lagu-lagu dari artis yang sama mungkin tidak selalu menjadi preferensi utama pengguna yang mencari rekomendasi berdasarkan satu lagu tertentu dari artis tersebut (pengguna mungkin mencari diversitas).
    * **Kelangkaan Ground Truth**: Untuk beberapa lagu input, jumlah lagu lain dari artis yang sama dalam dataset mungkin sedikit atau bahkan tidak ada, sehingga secara otomatis membuat Recall sulit untuk tinggi.
    * **Keterbatasan Model**: Model mungkin belum optimal dalam mengidentifikasi item-item relevan (sesuai definisi ground truth ini) dalam Top-10.

**d. Analisis Kualitatif Output Rekomendasi**
Untuk melengkapi evaluasi kuantitatif, dilakukan analisis kualitatif pada output rekomendasi untuk lagu input "Kite" (yang diidentifikasi sistem sebagai 'Being For The Benefit Of Mr. Kite! - Remastered 2009' oleh ['The Beatles']).

* **Input Judul Lagu untuk Rekomendasi:** `Kite`
  *(Lagu Referensi Sistem: 'Being For The Benefit Of Mr. Kite! - Remastered 2009' oleh ['The Beatles'])*

* **Output Top-5 Rekomendasi yang Dihasilkan:**

    **A. Rekomendasi NCF Murni (untuk artis: ['The Beatles'])**
    Lagu-lagu yang diprediksi model NCF memiliki skor kecocokan/popularitas tertinggi untuk artis referensi.

    | Judul Lagu                            | Artis                           | Popularitas | Skor NCF |
    | :------------------------------------ | :------------------------------ | :---------- | :------- |
    | Joan of Arc                           | ['Night Lovell', '$uicideBoy$'] | 0.65        | 0.988991 |
    | Whole Lotta Weed                      | ['Project Pat']                 | 0.36        | 0.988954 |
    | Hood Hop                              | ['J-Kwon']                      | 0.37        | 0.988665 |
    | Whistle While You Twurk (ColliPark Mix) | ['Ying Yang Twins']             | 0.47        | 0.988165 |
    | Kings Never Die                       | ['Eminem', 'Gwen Stefani']      | 0.65        | 0.988084 |

    **B. Rekomendasi Content-Based Filtering (CBF) Murni**
    Lagu-lagu dengan kemiripan fitur audio tertinggi dengan lagu referensi.

    | Judul Lagu                                 | Artis                | Popularitas | Valence | Danceability |
    | :----------------------------------------- | :------------------- | :---------- | :------ | :----------- |
    | Shaman's Blues                             | ['The Doors']        | 0.40        | 0.734   | 0.502626     |
    | I Can't Believe That You're In Love With Me  | ['Dinah Washington'] | 0.15        | 0.690   | 0.526209     |
    | An Old Fashioned Love Song                 | ['Three Dog Night']  | 0.37        | 0.744   | 0.498339     |
    | Inner City Blues (Make Me Wanna Holler)    | ['Gil Scott-Heron']  | 0.36        | 0.742   | 0.511202     |
    | I've Been Watching You (Move Your Sexy Body) | ['Parliament']       | 0.31        | 0.689   | 0.545503     |

    **C. Rekomendasi Hybrid**
    Kombinasi skor NCF dan CBF.

    | Judul Lagu                                 | Artis                | Popularitas | Skor Hybrid | Skor CBF (Norm) | Skor NCF |
    | :----------------------------------------- | :------------------- | :---------- | :---------- | :-------------- | :------- |
    | Shaman's Blues                             | ['The Doors']        | 0.40        | 0.914018    | 0.962288        | 0.865749 |
    | I Can't Believe That You're In Love With Me  | ['Dinah Washington'] | 0.15        | 0.906792    | 0.933130        | 0.880455 |
    | I've Been Watching You (Move Your Sexy Body) | ['Parliament']       | 0.31        | 0.899673    | 0.916823        | 0.882523 |
    | An Old Fashioned Love Song                 | ['Three Dog Night']  | 0.37        | 0.894511    | 0.928597        | 0.860426 |
    | Independence Day                           | ['David Byrne']      | 0.31        | 0.892122    | 0.904273        | 0.879972 |

* **Observasi Umum dari Analisis Kualitatif untuk "Kite"**:
    1.  **NCF Murni**: Menariknya, untuk artis The Beatles, rekomendasi NCF murni menghasilkan lagu-lagu dari genre Hip-Hop/Rap modern. Ini mengindikasikan bahwa model NCF, berdasarkan pembelajarannya (kemungkinan dari popularitas umum atau asosiasi fitur yang tidak terduga), mengaitkan profil "The Beatles" (atau lagu-lagu dengan fitur serupa dengan yang ada di training set untuk The Beatles) dengan lagu-lagu populer dari genre tersebut. Ini bisa jadi "serendipity" yang tidak diinginkan atau indikasi bias dalam model/data.
    2.  **CBF Murni**: Rekomendasi CBF tampak lebih intuitif dalam hal kemiripan sonik atau era, menghasilkan lagu-lagu dari artis seperti The Doors, Dinah Washington, yang mungkin memiliki beberapa kesamaan karakteristik audio dengan lagu The Beatles.
    3.  **Hybrid**: Output hybrid untuk lagu "Kite" tampaknya lebih dipengaruhi oleh skor CBF. Lagu-lagu teratas pada rekomendasi hybrid sama dengan rekomendasi CBF, meskipun skor NCF untuk lagu-lagu tersebut (misalnya, 0.86-0.88) juga berkontribusi. Ini berbeda dengan observasi pada contoh sebelumnya (di laporan versi lama), yang menunjukkan bahwa keseimbangan NCF dan CBF dalam hybrid dapat bervariasi tergantung lagu input dan artisnya.

### 3. Kesimpulan Evaluasi Keseluruhan

* Komponen **NCF** menunjukkan kemampuan belajar yang baik pada data training untuk klasifikasi popularitas (akurasi validasi ~83.46%), meskipun masih ada ruang untuk perbaikan dalam hal generalisasi dan penanganan overfitting.
* Evaluasi **kualitas rekomendasi Top-N** kini mencakup baik metrik kuantitatif maupun analisis kualitatif:
    * **Secara Kuantitatif**: Metrik Precision@10, Recall@10, dan NDCG@10 untuk CBF Murni dan Hybrid (dengan ground truth "lagu dari artis yang sama") menunjukkan skor yang moderat hingga rendah. Skor yang identik antara CBF dan Hybrid pada sampel evaluasi ini memerlukan investigasi lebih lanjut, kemungkinan terkait dengan dominasi salah satu skor pada sampel tersebut atau keterbatasan definisi ground truth.
    * **Secara Kualitatif**:
        * **CBF Murni** cenderung menghasilkan rekomendasi yang relevan secara fitur audio dengan lagu input.
        * **NCF Murni**, ketika digunakan untuk menghasilkan daftar Top-N, dapat menghasilkan rekomendasi yang mengejutkan dan lintas genre, yang mungkin disebabkan oleh cara model menginterpretasikan "preferensi artis" atau asosiasi fitur.
        * **Sistem Hybrid** menunjukkan perilaku yang dinamis; pada contoh "Kite", ia lebih condong ke hasil CBF, menunjukkan bahwa kontribusi masing-masing komponen dapat bervariasi. Ini menyoroti pentingnya strategi pembobotan dan normalisasi skor.

### 4. Rekomendasi Perbaikan (Berdasarkan Evaluasi)

Temuan dari evaluasi ini mengarahkan pada beberapa area perbaikan potensial:

* **Untuk Model NCF (Mengatasi Overfitting dan Meningkatkan Generalisasi)**:
    * Eksplorasi *hyperparameter tuning* yang lebih ekstensif (laju pembelajaran, dimensi laten, arsitektur jaringan).
    * Validasi silang (*k-fold cross-validation*) untuk evaluasi model NCF yang lebih robust.

* **Untuk Kualitas Rekomendasi Top-N (CBF dan Hybrid)**:
    * **Metrik Kuantitatif dan Ground Truth**:
        * Memperluas jumlah sampel untuk evaluasi kuantitatif guna mendapatkan hasil yang lebih stabil.
        * Mengeksplorasi definisi ground truth alternatif atau yang lebih kaya (misalnya, lagu dari genre yang sama, lagu yang sering didengarkan bersama, atau menggunakan data interaksi eksplisit jika tersedia di masa depan).
        * Menganalisis lebih dalam mengapa skor CBF dan Hybrid identik dalam evaluasi saat ini, termasuk sensitivitas terhadap normalisasi dan pembobotan skor.
    * **Content-Based Filtering**:
        * Mempertimbangkan fitur konten yang lebih beragam, seperti genre eksplisit, metadata lirik, atau fitur audio yang lebih canggih.
    * **Sistem Hybrid**:
        * Eksperimen dengan **pembobotan dinamis atau adaptif** antara skor NCF dan CBF.
        * Menyelidiki **strategi hibridisasi alternatif** (misalnya, *switching*, *cascade*, atau model hybrid yang dilatih secara *end-to-end*).
        * Menerapkan teknik untuk **meningkatkan keragaman (diversity)** dan **novelty/serendipity** dalam rekomendasi akhir, misalnya dengan melakukan re-ranking atau menambahkan filter.
    * **Analisis Kualitatif Lanjutan**: Melakukan analisis kualitatif pada lebih banyak contoh lagu input dari berbagai genre untuk memahami perilaku sistem secara lebih holistik.
    * **A/B Testing**: Jika sistem akan diimplementasikan, A/B testing dengan pengguna riil adalah cara terbaik untuk mengukur dampak sebenarnya dari berbagai strategi rekomendasi.

---
