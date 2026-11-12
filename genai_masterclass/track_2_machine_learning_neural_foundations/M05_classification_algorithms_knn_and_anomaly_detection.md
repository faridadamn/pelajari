# MICROSOFT GENERATIVE AI & COPILOT PROFESSIONAL OS — TRACK 2
## Modul 05: Algoritma Klasifikasi: K-Nearest Neighbor, Naive Bayes & Binary vs Multiclass
> **Sumber Utama:** *Everyday AI Concepts (Doug Rose)* & *Applied Classification and Distance-Metric Systems*.  
> **Target Kompetensi:** Menguasai algoritma klasifikasi berbasis kedekatan spasial (k-Nearest Neighbor), memahami kalkulasi probabilitas bersyarat Naive Bayes, serta membedakan arsitektur klasifikasi biner dan multi-kelas dalam sistem produksi.

---

### LAYER 1: KAIDAH EMAS (CORE AXIOMS)

1. **Aksioma Kedekatan Geometris (k-NN Spatial Proximity Principle):**
   Algoritma K-Nearest Neighbor (k-NN) bekerja berdasarkan premis dasar: *"Objek-objek yang serupa akan berkumpul berdekatan dalam ruang fitur."* Klasifikasi atau rekomendasi tidak ditentukan oleh rumus abstrak yang rumit, melainkan oleh pemungutan suara mayoritas (*majority voting*) dari k tetangga terdekat di sekitar titik data target pada diagram koordinat multidimensi.

2. **Batasan Komparasi Biner vs Multi-Kelas (Classification Boundary Complexity):**
   Tingkat kesulitan komputasi klasifikasi berlipat ganda saat berpindah dari dua opsi (Klasifikasi Biner: "Fraud" vs "Not Fraud", "Hujan" vs "Tidak Hujan") menjadi banyak opsi (Klasifikasi Multi-Kelas: Sentimen "Sangat Setuju", "Netral", dan "Sangat Tidak Setuju"). Klasifikasi biner hanya membutuhkan satu garis batas pemisah (*decision boundary*), sedangkan multi-kelas membutuhkan partisi bidang cembung yang saling bersilangan.

3. **Doktrin Independensi Naif (The Naive Bayes Conditional Independence Axiom):**
   Pengklasifikasi Naive Bayes membuat asumsi penyederhanaan bahwa setiap fitur dalam data saling bebas (*independent*) satu sama lain terhadap kelas target. Meskipun asumsi independensi ini di dunia nyata hampir selalu tidak realistis (kata "rekening" dan "transfer" biasanya berkorelasi), Naive Bayes secara matematis tetap sangat tangguh dan berkecepatan tinggi untuk filter spam email dan kategorisasi teks.

4. **Kompromi Pembelajar Malas vs Rajin (Lazy vs Eager Learning Trade-Off):**
   Algoritma k-NN adalah "pembelajar malas" (*lazy learner*)—ia tidak membangun model matematis saat pelatihan (*zero training time*), melainkan menyimpan seluruh data di memori. Akibatnya, beban komputasi terberat bergeser ke fase prediksi (*high inference latency*), di mana sistem harus menghitung jarak titik baru terhadap seluruh jutaan data historis secara real-time.

---

### LAYER 2: MENTAL MODEL & DIAGRAM ASCII

```text
========================================================================================
             MEKANIKA KLASIFIKASI K-NEAREST NEIGHBOR PADA DIAGRAM XY
========================================================================================

    Durasi Nonton (Jam)
      ▲
   10 │                  [Action Movie]          [Action Movie]
      │                         \                      /
    8 │                          ●                    ●
      │                                ┌─────────┐
    6 │              [Drama Movie]     │ ? (BARU)│     [Action Movie]
      │                   ▲            └────┬────┘            ▲
    4 │                   ■                 │                 ●
      │                              (Radius k=3)
    2 │         [Drama Movie]               │          [Action Movie]
      │               ■                     ▼                 ●
    0 └─────────────────────────────────────■─────────────────────────►
      0         2         4         6       8        10        12
                                                        Rating Film (1-10)

========================================================================================
Voting Tetangga Terdekat (k = 3):
- Tetangga 1: Jarak d = 1.4 unit ──► Kategori: [Action Movie] ●
- Tetangga 2: Jarak d = 1.8 unit ──► Kategori: [Action Movie] ●
- Tetangga 3: Jarak d = 2.1 unit ──► Kategori: [Drama Movie]  ■
Hasil Keputusan Mayoritas: [Action Movie] (2 vs 1) ──► Rekomendasikan ke Pengguna!
========================================================================================
Formula Jarak Euclidean Antara Dua Titik P(x1, y1) dan Q(x2, y2):
d(P, Q) = √[ (x2 - x1)² + (y2 - y1)² ]
========================================================================================
```

---

### LAYER 3: SYARAH DAGING (DEEP DIVE KNOWLEDGE)

#### 1. Syarah Kaidah 1: Aksioma Kedekatan Geometris (k-NN Spatial Proximity Principle)
Algoritma K-Nearest Neighbor (k-NN) adalah salah satu algoritma paling intuitif namun sangat tangguh dalam machine learning. Bayangkan sebuah layanan streaming film online yang ingin merekomendasikan film baru kepada pelanggan. Tim data membuat diagram bidang kartesius dua dimensi (XY diagram):
- **Sumbu X:** Rating rata-rata film (skala 1 - 10).
- **Sumbu Y:** Durasi tontonan pengguna terhadap film tersebut (dalam menit atau jam).

Setiap film dalam database diposisikan sebagai sebuah titik koordinat (X, Y) di atas grafik. Ketika seorang pengguna baru selesai menonton film bergenre fiksi ilmiah berdurasi 120 menit dengan rating 8,5, sistem mencari film-film lain yang letak fisiknya paling berdekatan dengan koordinat tersebut menggunakan rumus jarak Pythagoras (Euclidean Distance). Nilai k menentukan berapa banyak tetangga yang diajak berunding. Jika kita menetapkan k=5, algoritma akan mengambil 5 titik terdekat dan melihat kategori mayoritasnya untuk membuat rekomendasi.

#### 2. Syarah Kaidah 2: Batasan Komparasi Biner vs Multi-Kelas
Dalam rekayasa sistem klasifikasi, arsitek data wajib membedakan antara masalah biner dan masalah multi-kelas:
1. **Klasifikasi Biner (2 Kelas Target):** Masalah dengan keluaran ya/tidak. Contoh paling krusial di perbankan adalah pendeteksian transaksi mencurigakan: *"Apakah transaksi gesek kartu kredit ini Fraud atau Not Fraud?"* Model hanya perlu menentukan satu nilai probabilitas P. Jika P \ge 0,5, transaksi ditandai sebagai fraud; jika P < 0,5, transaksi lolos.
2. **Klasifikasi Multi-Kelas ( \ge 3 Kelas Target):** Masalah di mana input harus dimasukkan ke dalam salah satu dari banyak kategori yang saling lepas. Contoh: Analisis sentimen media sosial untuk partai politik yang mengelompokkan jutaan komentar netizen menjadi 3 kelas: *"Sangat Setuju"*, *"Netral"*, dan *"Sangat Tidak Setuju"*. 

Tingkat kerumitan klasifikasi multi-kelas jauh lebih tinggi karena model harus menggunakan fungsi probabilitas terdistribusi (seperti *Softmax*) untuk memastikan total penjumlahan probabilitas di seluruh kelas bernilai tepat 1,0 (P_1 + P_2 + P_3 = 1).

#### 3. Syarah Kaidah 3: Doktrin Independensi Naif (The Naive Bayes Invariant)
Algoritma **Naive Bayes** didasarkan pada Teorema Probabilitas Thomas Bayes:
P(A|B) = [P(B|A) \times P(A)] / P(B)

Disebut "Naif" (*Naive*) karena algoritma ini mengasumsikan bahwa keberadaan satu kata atau fitur sama sekali tidak ada hubungannya dengan keberadaan kata lainnya dalam sebuah dokumen. Secara realitas tata bahasa manusia, asumsi ini salah besar: kata "pinjaman" dan "bunga" hampir selalu muncul bersamaan dalam teks penawaran keuangan. 

Namun keajaiban Naive Bayes adalah: meskipun asumsi independensinya keliru, pengklasifikasi ini secara empiris sangat akurat dan luar biasa hemat memori komputasi. Filter spam email yang memindai miliaran pesan per detik di Gmail atau Microsoft Outlook seringkali mengandalkan varian Naive Bayes karena kecepatannya yang mampu mengembalikan hasil dalam hitungan milidetik.

#### 4. Syarah Kaidah 4: Kompromi Pembelajar Malas vs Rajin (Lazy vs Eager Learning)
Mayoritas algoritma pembelajaran mesin (seperti Jaringan Saraf Tiruan, Regresi Linier, atau Decision Tree) adalah **Eager Learners**:
- Mereka menghabiskan waktu berjam-jam saat fase pelatihan untuk menghitung bobot dan menyederhanakan data menjadi formula ringkas.
- Saat fase prediksi di server produksi, mereka sangat cepat karena hanya perlu memasukkan angka ke dalam formula yang sudah jadi.

Sebaliknya, **k-NN adalah Lazy Learner**:
- Pelatihan bernilai 0 detik: k-NN hanya memasukkan raw data ke dalam memori RAM tanpa menghitung rumus apa pun.
- Namun ketika ada 1 transaksi baru yang ingin diklasifikasikan, server harus menghitung jarak titik baru tersebut terhadap seluruh 10.000.000 data historis di dalam database.
Jika ukuran database bertambah besar, latensi k-NN akan meledak secara eksponensial. Oleh karena itu, k-NN sangat cocok untuk dataset berukuran kecil hingga menengah atau sistem rekomendasi offline batching, tetapi berbahaya jika digunakan langsung pada jalur lalu lintas API dengan jutaan concurrent users tanpa indexing spasial (seperti KD-Tree).

---

### LAYER 4: FIELD PLAYBOOK (TACTICAL SOP & CODE)

#### SOP 1: Protokol Normalisasi Fitur Sebelum Menjalankan k-NN
1. **Wajib Skalasi Fitur (Feature Scaling):** Jangan pernah menghitung jarak Euclidean pada fitur dengan rentang nilai yang berbeda drastis. Jika fitur X adalah "Gaji Karyawan" (Rp5.000.000 - Rp50.000.000) dan fitur Y adalah "Jumlah Anak" (1 - 5), maka kalkulasi jarak akan 99,99% didominasi oleh angka gaji, membuat fitur jumlah anak menjadi tidak terlihat oleh algoritma.
2. **Terapkan Min-Max Normalization:** Ubah seluruh nilai fitur ke dalam rentang seragam [0, 1]:  
   X_{norm} = (X - X_{min}) / (X_{max} - X_{min})
3. **Pilih Nilai k Ganjil:** Untuk klasifikasi biner, selalu pilih nilai k ganjil (k=3, 5, 7) guna mencegah terjadinya situasi pemungutan suara seri (*tie-break*).

#### Skrip Implementasi Python: `knn_classifier_engine.py`
Skrip Python mandiri untuk mengimplementasikan algoritma k-Nearest Neighbor murni tanpa library eksternal berat:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
K-Nearest Neighbor (k-NN) Engine from Scratch
Mengklasifikasikan film baru berdasarkan diagram koordinat 2D (Rating vs Durasi).
"""

import math

# Database Film Historis: [ID, Rating (1-10), Durasi (Jam), Kategori]
HISTORICAL_MOVIES = [
    {"title": "Die Hard",          "rating": 8.2, "duration": 2.2, "genre": "Action"},
    {"title": "Mad Max",           "rating": 8.1, "duration": 2.0, "genre": "Action"},
    {"title": "The Godfather",     "rating": 9.2, "duration": 2.9, "genre": "Drama"},
    {"title": "Schindler's List",  "rating": 9.0, "duration": 3.2, "genre": "Drama"},
    {"title": "John Wick",         "rating": 7.4, "duration": 1.7, "genre": "Action"},
    {"title": "12 Angry Men",      "rating": 9.0, "duration": 1.6, "genre": "Drama"},
]

def euclidean_distance(p1, p2):
    """
    Menghitung jarak Euclidean 2 dimensi: sqrt((x2-x1)^2 + (y2-y1)^2)
    """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def knn_classify_movie(new_rating, new_duration, k=3):
    """
    Mengklasifikasikan film baru berdasarkan mayoritas k tetangga terdekat.
    """
    distances = []
    target_point = (new_rating, new_duration)
    
    for m in HISTORICAL_MOVIES:
        m_point = (m["rating"], m["duration"])
        dist = euclidean_distance(target_point, m_point)
        distances.append({"title": m["title"], "genre": m["genre"], "distance": dist})
        
    # Urutkan berdasarkan jarak terkecil
    distances.sort(key=lambda x: x["distance"])
    neighbors = distances[:k]
    
    # Hitung voting mayoritas
    votes = {}
    for n in neighbors:
        genre = n["genre"]
        votes[genre] = votes.get(genre, 0) + 1
        
    predicted_genre = max(votes, key=votes.get)
    return {
        "target": target_point,
        "predicted_genre": predicted_genre,
        "nearest_neighbors": neighbors
    }

if __name__ == "__main__":
    print("[*] Menjalankan Evaluasi Klasifikasi k-NN Film Baru:")
    sample = knn_classify_movie(new_rating=7.8, new_duration=1.9, k=3)
    print(f"[+] Input Titik Baru (Rating: 7.8, Durasi: 1.9 jam)")
    print(f"[+] Kategori Terprediksi: [{sample['predicted_genre']}]")
    print("    3 Tetangga Terdekat:")
    for n in sample["nearest_neighbors"]:
        print(f"    - {n['title']:<18} ({n['genre']:<6}) | Jarak Spasial: {n['distance']:.3f} unit")
```

---

### LAYER 5: DIAGNOSTIC DRILL (STUDI KASUS & UJI MANDIRI)

#### Skenario Kasus Lapangan
Sebuah lembaga survei politik di Jakarta ditugaskan untuk melakukan analisis sentimen publik secara real-time terhadap perdebatan calon gubernur di platform X (Twitter). Tim data science membangun arsitektur kecerdasan buatan untuk mengklasifikasikan setiap tweet ke dalam salah satu dari tiga kategori: *"Mendukung"* (Agree), *"Netral"* (Neutral), dan *"Menolak"* (Disagree). 
Pada rilis pertama, tim menggunakan algoritma klasifikasi biner dan mengelompokkan seluruh tweet yang tidak mengandung kata dukungan langsung sebagai "Menolak". Akibatnya, jutaan tweet netral yang hanya mengajukan pertanyaan atau mengutip berita faktual dilaporkan sebagai opini penolakan keras, memicu kepanikan di tim kampanye.

#### Lembar Uji Mandiri
1. Identifikasi kekeliruan arsitektur model machine learning pada kasus di atas berdasarkan pembagian klasifikasi biner vs multi-kelas!
2. Jika sebuah platform streaming video ingin membangun sistem rekomendasi film berdasarkan posisi koordinat kesukaan penonton di diagram XY, mengapa algoritma k-Nearest Neighbor (k-NN) secara matematis adalah solusi paling tepat dibandingkan algoritma Q-Learning?
3. Sebutkan satu skenario di mana algoritma Naive Bayes jauh lebih unggul untuk diimplementasikan dibandingkan jaringan saraf tiruan deep learning yang memiliki 100 lapisan neuron!

#### Kunci Jawaban Lengkap & Analisis Diagnostik
1. **Kekeliruan Arsitektur: Memaksakan Masalah Multi-Kelas Menjadi Klasifikasi Biner.** Sentimen opini manusia pada isu politik memiliki gradasi spektrum yang jelas: positif, netral, dan negatif (3 kelas). Memaksa sistem menjadi biner ("Agree" vs "Not Agree") menghapus kategori netral secara artifisial. Semua ekspresi netral atau pertanyaan rasa ingin tahu langsung dicap sebagai penolakan ("Disagree"), mendistorsi realitas data sentimen sebesar 40-50%.
2. **Keunggulan k-NN Atas Q-Learning untuk Rekomendasi Spasial:** 
   - k-NN dirancang khusus untuk memetakan koordinat fitur spasial statis (Rating vs Durasi) dan mencari kesamaan geometri jarak fisik antar konten.
   - Sebaliknya, Q-Learning adalah algoritma **Reinforcement Learning** yang dirancang untuk agen interaktif yang mengambil tindakan sekuensial dinamis dalam lingkungan yang berubah (seperti mengendalikan drone atau bermain game catur). Menggunakan Q-Learning untuk mencocokkan titik film statis adalah pemborosan komputasi (*over-engineering*) yang tidak relevan.
3. **Skenario Keunggulan Naive Bayes:** Filter deteksi spam email atau moderasi konten teks berkecepatan tinggi pada perangkat seluler (Edge AI / Termux / Smartwatch). Naive Bayes hanya membutuhkan tabel perkalian frekuensi kata sederhana, mengeksekusi inferensi dalam < 1 milidetik, dan membutuhkan memori RAM < 5 MB, sementara Deep Learning 100 layer membutuhkan akselerator GPU bertenaga tinggi dan memori ratusan megabyte yang boros baterai.
