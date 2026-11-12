# MICROSOFT GENERATIVE AI & COPILOT PROFESSIONAL OS — TRACK 2
## Modul 03: Taksonomi AI Modern: Supervised, Unsupervised, RL & Weak vs Strong AI
> **Sumber Utama:** *Everyday AI Concepts (Doug Rose)* & *Machine Learning Field Architectures*.  
> **Target Kompetensi:** Memahami batasan komputasi Artificial Narrow Intelligence (Weak AI) versus Artificial General Intelligence (AGI), memetakan domain masalah ke algoritma Supervised, Unsupervised, atau Reinforcement Learning secara presisi.

---

### LAYER 1: KAIDAH EMAS (CORE AXIOMS)

1. **Aksioma Batas Kecerdasan Sempit (Narrow AI Invariant):**
   Seluruh sistem kecerdasan buatan komersial yang beroperasi saat ini adalah "Weak AI" (Narrow AI)—sistem yang dirancang dan dibatasi secara ketat untuk mengeksekusi satu tugas spesifik (seperti memprediksi spam email, mengklasifikasikan transaksi kartu kredit, atau memprediksi token berikutnya). Kehebatan komputasi pada satu domain sempit tidak mencerminkan kesadaran umum (*Artificial General Intelligence / Strong AI*).

2. **Hukum Supervisi Berlabel (The Ground Truth Axiom):**
   Supervised Learning membutuhkan data historis yang telah dipasangkan dengan label kebenaran dasar (*ground truth*). Algoritma belajar memetakan fungsi dari input X ke output Y. Jika organisasi tidak memiliki data historis berlabel yang bersih dan terverifikasi manusia, pendekatan Supervised Learning secara matematis mustahil diimplementasikan.

3. **Prinsip Geometri Tak Terbimbing (Unsupervised Cluster Geometry):**
   Unsupervised Learning beroperasi tanpa label target dan tanpa instruksi eksplisit; tujuannya adalah menemukan pola intrinsik, struktur tersembunyi, atau kelompok kedekatan (*clusters*) dalam ruang multidimensi. Algoritma ini sangat unggul untuk segmentasi pelanggan yang belum terpetakan, rekomendasi keranjang belanja, dan deteksi penyimpangan (anomali).

4. **Siklus Kebijakan dan Imbalan (Reinforcement Dynamic Feedback):**
   Reinforcement Learning (RL) tidak belajar dari dataset statis, melainkan melalui interaksi aktif agen (*agent*) dengan lingkungan (*environment*) berbasis uji coba (*trial and error*). Agen mengoptimalkan fungsi kebijakan (*policy*) untuk memaksimalkan akumulasi skor imbalan (*reward*) kumulatif, menjadikannya standar emas untuk navigasi otonom, permainan strategi, dan penyelarasan model bahasa (RLHF).

---

### LAYER 2: MENTAL MODEL & DIAGRAM ASCII

```text
========================================================================================
                     TAKSONOMI LENGKAP KECERDASAN BUATAN MODERN
========================================================================================

                                [ ARTIFICIAL INTELLIGENCE ]
                                             │
               ┌─────────────────────────────┴─────────────────────────────┐
               ▼                                                           ▼
       [ WEAK / NARROW AI ]                                        [ STRONG AI / AGI ]
   (Spesifik 1 Domain Masalah;                                 (Kesadaran Umum Fleksibel;
    99.9% Sistem Riil Saat Ini)                                 Teoretis / Riset Masa Depan)
               │
               ▼
       [ MACHINE LEARNING ]
               │
   ┌───────────┼────────────────────────────────────────┐
   ▼           ▼                                        ▼
[ SUPERVISED ] [ UNSUPERVISED ]                         [ REINFORCEMENT ]
(Data + Label) (Data Tanpa Label)                       (Agen + Lingkungan + Reward)
   │           │                                        │
   ├─► Klasifikasi Biner     ├─► K-Means Clustering     ├─► Game Playing (AlphaGo)
   │   (Fraud / Not Fraud)   │   (Segmentasi Pelanggan) │
   │                         │                          ├─► Robotika Mandiri
   ├─► Klasifikasi Multi     ├─► Reduksi Dimensi (PCA)  │
   │   (Sentimen 3-Kelas)    │   (Kompresi Fitur)       └─► RLHF pada LLM
   │                         │                              (Penyelarasan Nilai Manusia)
   └─► Regresi Numerik       └─► Rekomendasi Asosiasi
       (Prediksi Harga Es)       (Toothpaste + Cleanser)
========================================================================================
Matriks Keputusan Pemilihan Pendekatan:
1. Ada Label Y historis?       ──► YA  ──► Gunakan Supervised Learning.
2. Ingin cari pola kelompok?     ──► YA  ──► Gunakan Unsupervised Learning.
3. Tindakan dinamis berulang?    ──► YA  ──► Gunakan Reinforcement Learning.
========================================================================================
```

---

### LAYER 3: SYARAH DAGING (DEEP DIVE KNOWLEDGE)

#### 1. Syarah Kaidah 1: Aksioma Batas Kecerdasan Sempit (Narrow AI Invariant)
Masyarakat awam dan media massa sering mencampuradukkan antara kemajuan AI saat ini dengan fiksi ilmiah tentang mesin yang memiliki kesadaran subyektif (*sentience*). Dalam terminologi ilmu komputer terapan, semua model yang kita gunakan—mulai dari AlphaFold pemenang Nobel, algoritma deteksi fraud perbankan, filter email spam, hingga ChatGPT-4o—berada di bawah kategori **Weak AI (Narrow AI)**.

Karakteristik utama Weak AI adalah keterbatasan kontekstual yang kaku:
- Model catur tingkat dunia yang mengalahkan grandmaster tidak bisa mengenali perbedaan antara foto kucing dan anjing.
- Model deteksi penipuan kartu kredit yang memproses 100.000 transaksi per detik tidak bisa membaca draf perjanjian kontrak kerja.
- Large Language Model (LLM) tampak "pintar serba bisa" bukan karena memiliki pemahaman konseptual dunia fisik, melainkan karena arsitekturnya menggeneralisasi satu tugas sempit: *prediksi probabilitas token teks berikutnya* pada ruang data pelatihan yang luar biasa masif. Memahami bahwa AI adalah Narrow System melindungi pimpinan bisnis dari ekspektasi magis yang keliru.

#### 2. Syarah Kaidah 2: Hukum Supervisi Berlabel (The Ground Truth Axiom)
Supervised Learning adalah metode paling dominan dalam aplikasi bisnis komersial. Mekanismenya meniru seorang siswa yang belajar menggunakan buku latihan lengkap dengan kunci jawaban di halaman belakang. Setiap baris data dalam dataset pelatihan wajib memiliki dua komponen:
1. **Fitur Input (X):** Variabel independen yang diobservasi (misal: jumlah transaksi, jam transaksi, lokasi geografis, jenis kartu).
2. **Label Target (Y):** Kebenaran dasar (*ground truth*) yang diverifikasi (misal: "Fraud" atau "Not Fraud").

Tantangan terbesar dalam Supervised Learning bukan pada algoritma komputasinya, melainkan pada **ekonomi pelabelan data (Labeling Economics)**. Mengumpulkan 1.000.000 email untuk melatih filter spam membutuhkan kurasi manusia untuk menandai mana email promosi, phishing, dan email pribadi yang sah. Jika label historis lo mengandung kesalahan (misal: auditor ceroboh salah menandai transaksi sah sebagai fraud), model akan mempelajari kesalahan tersebut secara setia (*Garbage In, Garbage Out*).

#### 3. Syarah Kaidah 3: Prinsip Geometri Tak Terbimbing (Unsupervised Cluster Geometry)
Bayangkan lo adalah manajer toko ritel baru yang memiliki 5.000.000 struk belanja pelanggan, tetapi lo sama sekali tidak tahu demografi atau profil mereka. Lo tidak memiliki label target "pelanggan hemat" atau "pelanggan hedonis". Di sinilah **Unsupervised Learning** bekerja.

Alih-alih mencari kecocokan dengan kunci jawaban, algoritma tak terbimbing menghitung jarak spasial antar titik data dalam ruang vektor:
- **Clustering (K-Means / Hierarchical):** Algoritma mengukur jarak Euclidean antar titik belanja dan menemukan bahwa orang yang membeli pasta gigi hampir selalu membeli pembersih wajah (*facial cleanser*) dalam keranjang yang sama. Toko dapat langsung menempatkan kedua barang tersebut di rak yang berdekatan untuk meningkatkan nilai transaksi rata-rata tanpa perlu survei manual.
- **Dimensionality Reduction:** Mereduksi ratusan parameter perilaku nasabah menjadi 2 atau 3 variabel komposit utama tanpa kehilangan informasi inti, memudahkan visualisasi dan analisis risiko kredit.

#### 4. Syarah Kaidah 4: Siklus Kebijakan dan Imbalan (Reinforcement Dynamic Feedback)
Berbeda dengan Supervised Learning yang pasif membaca dataset historis statis, **Reinforcement Learning (RL)** meniru cara melatih anjing sirkus menggunakan sistem imbalan (*treat*) dan hukuman (*punishment*). Komponen utamanya adalah:
- **Agent:** Entitas pembuat keputusan (misal: mobil otonom atau bot catur).
- **Environment:** Dunia tempat agen beroperasi (jalan raya virtual atau papan catur).
- **Action (A):** Keputusan yang diambil agen pada waktu t.
- **Reward (R):** Sinyal numerik yang diterima dari lingkungan (+1 jika menang/bergerak aman, -100 jika menabrak dinding).

Dalam era AI generatif modern, teknik **Reinforcement Learning from Human Feedback (RLHF)** adalah kunci mengapa LLM tidak berbicara kasar atau menyebarkan resep bom. Tim peneliti memberikan skor imbalan positif ketika model merespons pertanyaan dengan sopan, akurat, dan aman, serta skor penalti saat model berhalusinasi atau melanggar etika. Model memperbarui kebijakan probabilitasnya agar selalu memaksimalkan skor imbalan tersebut.

---

### LAYER 4: FIELD PLAYBOOK (TACTICAL SOP & CODE)

#### SOP Audit Pemilihan Tipe Machine Learning (Decision Matrix)
Saat menerima kebutuhan proyek dari manajemen, jalankan checklist 3 pertanyaan sebelum menulis satu baris kode pun:
1. *Apakah kita memiliki kolom target (Y) yang sudah pasti dan terverifikasi?*
   - Jika **YA**: Pilih **Supervised Learning** (Gunakan Regresi jika Y angka kontinu; gunakan Klasifikasi jika Y kategori).
   - Jika **TIDAK**: Lanjut ke pertanyaan 2.
2. *Apakah tujuannya menemukan kelompok alami, segmentasi pasar, atau menyederhanakan ratusan kolom data?*
   - Jika **YA**: Pilih **Unsupervised Learning** (Clustering / PCA).
   - Jika **TIDAK**: Lanjut ke pertanyaan 3.
3. *Apakah masalah melibatkan urutan keputusan interaktif dinamis dengan fungsi skor hadiah/penalti jangka panjang?*
   - Jika **YA**: Pilih **Reinforcement Learning**.

#### Skrip Implementasi Python: `ml_taxonomy_selector.py`
Skrip Python mandiri untuk mendemonstrasikan perbedaan komputasi antara Supervised Classification dan Unsupervised Clustering menggunakan data dummy belanja ritel:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ML Taxonomy Simulator: Supervised vs Unsupervised Pipeline
Mendemonstrasikan perbedaan mendasar antara klasifikasi transaksi fraud (Supervised)
dan clustering keranjang belanja e-commerce (Unsupervised).
"""

import math

# 1. SUPERVISED DATASET: Fitur X (Nominal Transaksi, Jarak Jam) -> Label Y (1: Fraud, 0: Normal)
SUPERVISED_DATA = [
    {"amount": 50000,   "time_delta_hr": 24, "is_fraud": 0},
    {"amount": 120000,  "time_delta_hr": 12, "is_fraud": 0},
    {"amount": 9500000, "time_delta_hr": 0.1, "is_fraud": 1},
    {"amount": 8700000, "time_delta_hr": 0.2, "is_fraud": 1},
]

# 2. UNSUPERVISED DATASET: Fitur X (Frekuensi Beli, Total Belanja) TANPA LABEL TARGET
UNSUPERVISED_DATA = [
    {"cust_id": "C01", "freq": 1, "spend": 45000},
    {"cust_id": "C02", "freq": 2, "spend": 60000},
    {"cust_id": "C03", "freq": 28, "spend": 4500000},
    {"cust_id": "C04", "freq": 32, "spend": 5200000},
]

def rule_based_supervised_predict(amount, time_delta):
    """
    Simulasi model klasifikasi biner supervised tereduksi.
    """
    risk_score = (amount / 1000000) * (1 / max(0.1, time_delta))
    return "FRAUD" if risk_score > 15 else "NORMAL"

def simple_unsupervised_cluster(customers):
    """
    Simulasi clustering 2 segmen (Low Value vs VIP/Whale) berdasarkan ambang jarak vektor.
    """
    clusters = {"Low_Spender": [], "VIP_Whale": []}
    for c in customers:
        # Vektor jarak sederhana
        if c["freq"] >= 15 and c["spend"] >= 2000000:
            clusters["VIP_Whale"].append(c["cust_id"])
        else:
            clusters["Low_Spender"].append(c["cust_id"])
    return clusters

if __name__ == "__main__":
    print("[1] Menguji Prediksi Supervised (Binary Classification):")
    for tx in SUPERVISED_DATA:
        pred = rule_based_supervised_predict(tx["amount"], tx["time_delta_hr"])
        actual = "FRAUD" if tx["is_fraud"] == 1 else "NORMAL"
        print(f"    - Tx Rp{tx['amount']:,} (Delta: {tx['time_delta_hr']}j) -> Pred: {pred} | Actual: {actual}")

    print("\n[2] Menguji Pengelompokan Unsupervised (Clustering):")
    clusters = simple_unsupervised_cluster(UNSUPERVISED_DATA)
    for k, v in clusters.items():
        print(f"    - Kluster [{k}]: {len(v)} Pelanggan ({', '.join(v)})")
```

---

### LAYER 5: DIAGNOSTIC DRILL (STUDI KASUS & UJI MANDIRI)

#### Skenario Kasus Lapangan
Sebuah platform streaming film online di Asia Tenggara mengalami penurunan retensi penonton (*viewer churn*). Direktur Marketing meminta tim data science untuk membuat "Kecerdasan Buatan Canggih ala Netflix" yang bisa merekomendasikan film baru berdasarkan kebiasaan nonton pengguna. 
Tim junior mengusulkan untuk mengumpulkan 10.000 riwayat tontonan pengguna lalu melatih model regresi linier. Saat ditanya oleh Chief Technology Officer (CTO) mengenai kolom target labelnya, tim junior terdiam dan menjawab: *"Kami ingin AI belajar sendiri dari data tanpa perlu memberi label apa pun, tapi nanti harus bisa langsung menebak dengan pasti film apa yang akan ditonton pengguna minggu depan."*

#### Lembar Uji Mandiri
1. Identifikasi kesalahpahaman konsep taksonomi AI yang dialami oleh tim data junior pada skenario di atas!
2. Jika platform ingin membuat fitur "Pelanggan yang menonton genre horor klasik juga menyukai film dokumenter misteri", jenis machine learning apa yang wajib digunakan dan mengapa?
3. Mengapa sistem rekomendasi film dikategorikan sebagai Weak AI, dan apa risikonya jika manajemen menganggapnya memiliki pemahaman selera manusia layaknya kritikus film sejati?

#### Kunci Jawaban Lengkap & Analisis Diagnostik
1. **Kesalahpahaman Konsep:** Tim junior mencampuradukkan antara pendekatan **Supervised Learning** (yang menuntut label target Y pasti untuk melakukan prediksi kejadian masa depan) dengan **Unsupervised Learning** (yang bekerja tanpa label untuk mencari kelompok kedekatan). Menggunakan regresi linier tanpa variabel target yang terdefinisi secara matematis adalah kekeliruan fatal yang mustahil dieksekusi.
2. **Pendekatan yang Wajib Digunakan: Unsupervised Learning (Clustering & Association Rule Mining).** 
   - Karena platform ingin mengelompokkan pola kesamaan film yang ditonton bersamaan tanpa ada definisi benar/salah sebelumnya. 
   - Algoritma memetakan film ke dalam diagram XY berdasarkan durasi tonton dan rating genre, lalu merekomendasikan film berdasarkan kedekatan jarak spasial (*nearest neighbor*).
3. **Risiko Ilusi Weak AI vs Strong AI:** Sistem rekomendasi film adalah Weak AI yang murni memproses kalkulasi korelasi angka koordinat. Jika manajemen menganggap sistem tersebut "mengerti cita rasa seni", manajemen rentan terjebak dalam bias algoritma: sistem akan terus menyajikan film serupa berulang-ulang (*echo chamber/filter bubble*), mengabaikan keragaman konten baru, dan gagal mengantisipasi pergeseran tren kultural yang hanya bisa dianalisis oleh akal sehat manusia.
