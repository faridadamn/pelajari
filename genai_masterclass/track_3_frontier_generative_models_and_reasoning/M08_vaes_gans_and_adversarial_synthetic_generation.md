# MICROSOFT GENERATIVE AI & COPILOT PROFESSIONAL OS — TRACK 3
## Modul 08: Generative vs Discriminative: Variational Autoencoders (VAEs) & GANs
> **Sumber Utama:** *AI Literacy for Everyone (Dr. Marily Nika / Google & Meta)* & *Deep Generative Models: VAEs, GANs and Synthetic Augmentation*.  
> **Target Kompetensi:** Membedakan fondasi matematis model Generatif versus Diskriminatif, menguasai arsitektur Variational Autoencoders (VAEs) untuk deteksi anomali medis (CT scan), serta memahami dinamika permainan dua arah Generator-Discriminator pada Generative Adversarial Networks (GANs) untuk sintesis data fraud.

---

### LAYER 1: KAIDAH EMAS (CORE AXIOMS)

1. **Aksioma Probabilitas Gabungan vs Bersyarat (Generative vs Discriminative):**
   Model diskriminatif (*discriminative AI*) belajar membedakan data dengan menghitung batas probabilitas bersyarat P(Y|X)—tujuannya murni mengklasifikasikan atau memberi label (misal: "apakah gambar ini kucing atau anjing?"). Sebaliknya, model generatif (*generative AI*) memodelkan distribusi probabilitas gabungan P(X, Y) atau fitur P(X)—tujuannya adalah memahami bagaimana data tersebut dibentuk agar dapat memproduksi sampel data baru yang serupa.

2. **Prinsip Rekonstruksi Anomali VAE (Variational Autoencoder Anomaly Detection):**
   Variational Autoencoders (VAEs) mengompresi data input ke dalam ruang laten berdimensi rendah (*latent space distribution*) lalu merekonstruksinya kembali. Jika VAE dilatih hanya menggunakan sampel data normal (seperti ratusan ribu CT scan paru-paru sehat), model akan merekonstruksi citra normal dengan sangat sempurna, namun akan menghasilkan kesalahan rekonstruksi (*high reconstruction error*) yang sangat tinggi saat menjumpai anomali (seperti tumor atau lesi), menjadikannya instrumen skrining medis otomatis terbaik.

3. **Dinamika Permainan Dua Arah Minimax (GANs Adversarial Opposition):**
   Generative Adversarial Networks (GANs) terdiri dari dua jaringan saraf tiruan yang saling berlawanan dalam permainan zero-sum game: (1) **Generator** yang bertugas memalsukan data agar tampak asli, dan (2) **Discriminator** yang bertugas mendeteksi apakah data tersebut asli atau palsu. Pertarungan tanpa henti ini memaksa kedua jaringan saling menyempurnakan diri hingga output generator tidak dapat dibedakan dari data nyata.

4. **Sintesis Skenario Langka (The Synthetic Data Augmentation Principle):**
   Dalam domain keamanan siber dan keuangan perbankan, data kejahatan (seperti transaksi penipuan kartu kredit) berjumlah sangat sedikit dibandingkan jutaan transaksi sah (*extreme class imbalance*). GANs memungkinkan organisasi "menciptakan" transaksi penipuan sintetis yang belum pernah terjadi sebelumnya di data historis guna menguji ketahanan sistem pertahanan (*stress-testing*).

---

### LAYER 2: MENTAL MODEL & DIAGRAM ASCII

```text
========================================================================================
     ARSITEKTUR PERBANDINGAN: VAE (DETEKSI ANOMALI) VS GAN (SINTESIS DATA)
========================================================================================

    [ MODEL 1: VARIATIONAL AUTOENCODER (VAE) - DETEKSI ANOMALI MEDIS ]
    Citra CT Scan Input (X)
             │
             ▼
    ┌─────────────────┐
    │     ENCODER     │ ──► Mengompresi ke Ruang Laten (Mean μ & Variance σ²)
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │     DECODER     │ ──► Merekonstruksi Citra Kembali (X_reconstructed)
    └────────┬────────┘
             │
             ▼
    [ EVALUASI RECONSTRUCTION ERROR: ||X - X_reconstructed||² ]
    - Error Rendah (≈ 0)  ──► Jaringan Normal / Sehat (Lolos Skrining Rutin)
    - Error Tinggi (>> 0) ──► ANOMALI TERDETEKSI! (Kirim ke Senior Radiologist)

----------------------------------------------------------------------------------------

    [ MODEL 2: GENERATIVE ADVERSARIAL NETWORK (GAN) - MINIMAX GAME ]
    Vektor Derau Acak (Z) ──► ┌─────────────┐
                              │  GENERATOR  │ ──► Sintesis Transaksi Palsu
                              └──────┬──────┘
                                     │
                                     ├────────────────────────┐
                                     ▼                        ▼
    Data Transaksi Riil   ──► ┌─────────────┐       [ UMPAN BALIK MINIMAX ]
    (Database Historis)       │DISCRIMINATOR│ ──► 1: Asli / 0: Palsu
                              └─────────────┘       - Latih Discriminator makin jeli
                                                    - Latih Generator makin lihai
========================================================================================
Fungsi Objektif Minimax GAN:
min_G max_D V(D, G) = E[log D(x)] + E[log(1 - D(G(z)))]
========================================================================================
```

---

### LAYER 3: SYARAH DAGING (DEEP DIVE KNOWLEDGE)

#### 1. Syarah Kaidah 1: Aksioma Probabilitas Gabungan vs Bersyarat
Secara fundamental dalam matematika statistik, kecerdasan buatan terbelah menjadi dua mazhab besar:
1. **Discriminative AI (Model Diskriminatif):** Menjawab pertanyaan: *"Diberikan data input X, kelas Y mana yang paling mungkin?"* Model ini hanya peduli pada batas pemisah (*decision boundary*) antar kategori. Jika lo memberikan rekaman suara, model diskriminatif menentukan apakah suara tersebut kata "Buka" atau "Tutup". Model diskriminatif tidak tahu cara membuat rekaman suara baru; ia hanya menghakimi dan memberi label.
2. **Generative AI (Model Generatif):** Menjawab pertanyaan: *"Bagaimana ciri-ciri distribusi data X di dunia nyata?"* Model ini mempelajari struktur internal pembentuk data. Karena model menguasai geometri probabilitas data, ia dapat mengambil titik acak dari ruang laten tersebut dan mengubahnya menjadi sampel baru yang belum pernah ada: wajah manusia sintetis, naskah esai baru, atau struktur protein sintetis.

#### 2. Syarah Kaidah 2: Prinsip Rekonstruksi Anomali VAE
Di rumah sakit besar, seorang dokter spesialis radiologi senior menghabiskan ribuan jam setiap tahun untuk memeriksa hasil pemindaian *Computed Tomography (CT Scan)*. Masalah utamanya adalah: 95% dari citra pemindaian tersebut adalah organ tubuh yang sepenuhnya normal dan sehat, sementara 5% sisanya memuat tanda-tanda awal penyakit berbahaya (seperti gumpalan darah atau nodul tumor kecil) yang membutuhkan perhatian segera.

Di sinilah **Variational Autoencoder (VAE)** menjadi terobosan luar biasa:
- VAE terdiri dari **Encoder** yang memampatkan citra CT beresolusi tinggi menjadi representasi statistik ringkas (vektor rata-rata μ dan varians 3σ), serta **Decoder** yang membongkar kembali representasi tersebut menjadi citra asli.
- Rumah sakit melatih VAE hanya menggunakan citra pasien sehat. Model menjadi sangat ahli dalam merekonstruksi jaringan paru-paru atau otak yang normal.
- Ketika seorang pasien dengan lesi otak langka dipindai, decoder VAE mencoba merekonstruksi citra tersebut menggunakan memorinya tentang organ sehat. Akibatnya, area lesi tidak dapat direkonstruksi dengan benar, menghasilkan selisih piksel (*reconstruction error*) yang menyala merah terang pada layar. Sistem secara instan menaikkan status file tersebut ke antrean prioritas darurat dokter senior (*automated clinical triage*).

#### 3. Syarah Kaidah 3: Dinamika Permainan Dua Arah Minimax (GANs)
Diciptakan oleh Ian Goodfellow pada tahun 2014, **Generative Adversarial Network (GAN)** mengadopsi teori permainan matematika (*game theory*):
- **The Generator:** Diibaratkan sebagai sindikat pembuat uang palsu. Generator tidak pernah melihat uang asli secara langsung; ia hanya menerima angka acak (*noise vector*) dan mencoba mencetak gambar yang menyerupai uang kertas.
- **The Discriminator:** Diibaratkan sebagai polisi kasir bank yang berpengalaman. Discriminator menerima dua tumpukan data: uang kertas asli dari brankas bank dan uang kertas palsu dari generator. Tugasnya adalah menilai dengan jujur: mana yang asli dan mana yang tiruan.

Pada putaran pertama, uang generator sangat jelek dan polisi mendeteksinya dengan mudah. Namun setiap kali generator tertangkap basah, sinyal error (*loss*) dikirimkan kembali ke generator untuk memperbaiki kualitas cetakannya. Sebaliknya, setiap kali polisi tertipu, polisi dilatih lebih keras untuk memeriksa serat mikro kertas. Melalui jutaan putaran permainan Minimax, generator akhirnya mampu menghasilkan gambar sintetis yang resolusinya begitu sempurna sehingga polisi paling ahli pun tidak dapat membedakannya.

#### 4. Syarah Kaidah 4: Sintesis Skenario Langka (Synthetic Data Augmentation)
Masalah terbesar dalam industri deteksi penipuan (*fraud detection*) dan pertahanan militer adalah kelangkaan data musuh (*scarcity of adversarial data*). Jika sebuah bank memproses 100.000.000 transaksi gesek kartu kredit dalam sebulan, mungkin hanya ada 500 transaksi yang benar-benar merupakan penipuan canggih. Jika kita melatih neural network biasa pada data yang timpang 99,999% ini, model akan malas dan selalu menebak "transaksi normal" untuk mendapatkan akurasi 99,999% semu.

Dengan menggunakan GANs, tim keamanan siber dapat melatih generator untuk **menciptakan variasi pola penipuan sintetis yang belum pernah terjadi di dunia nyata**. Generator menggabungkan pola peretasan dari berbagai belahan dunia untuk mensimulasikan taktik baru para penjahat. Data sintetis ini kemudian diinjeksikan ke dalam sistem pertahanan bank untuk melatih algoritma firewall sebelum serangan nyata terjadi di pasar.

---

### LAYER 4: FIELD PLAYBOOK (TACTICAL SOP & CODE)

#### SOP 1: Protokol Triage Deteksi Anomali Berbasis VAE
1. **Latih Hanya Pada Data Bersih (Clean Baseline):** Pastikan dataset pelatihan 100% bebas dari data anomali atau data rusak.
2. **Kalkulasi Ambang Batas Rekonstruksi (Threshold Tuning):** Hitung skor Mean Absolute Error (MAE) rekonstruksi pada data validasi normal. Tetapkan ambang batas peringatan (*alert threshold*) pada 3σ (tiga deviasi standar di atas rata-rata normal).
3. **Automated Escalation Rule:** Jika skor rekonstruksi sampel baru melebihi 3σ, langsung kirim notifikasi prioritas tinggi ke kanal operasional manusia (dokter radiolog atau analis fraud level 3).

#### Skrip Implementasi Python: `vae_anomaly_reconstruction.py`
Skrip Python mandiri untuk mensimulasikan mekanisme deteksi anomali rekonstruksi ala VAE:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VAE Anomaly Reconstruction Simulator
Mendemonstrasikan logika deteksi anomali pada CT scan / sinyal sensor
menggunakan ambang batas deviasi rekonstruksi (Reconstruction Error).
"""

import math

# Baseline Profil Normal (Representasi Vektor Jaringan Organ Sehat)
HEALTHY_BASELINE_VECTOR = [1.0, 1.2, 0.9, 1.1, 1.0, 0.95, 1.05]

def simulate_vae_reconstruction(input_vector):
    """
    Simulasi decoder VAE yang telah dilatih hanya pada jaringan sehat.
    Decoder memproyeksikan input kembali ke pola sehat terdekat.
    """
    # Decoder cenderung mengembalikan profil mendekati baseline sehat
    return [(v * 0.2 + b * 0.8) for v, b in zip(input_vector, HEALTHY_BASELINE_VECTOR)]

def evaluate_scan_anomaly(scan_id, scan_pixels, error_threshold=0.35):
    """
    Menghitung selisih rekonstruksi L2 error antara input dan output decoder.
    """
    reconstructed = simulate_vae_reconstruction(scan_pixels)
    # Hitung Mean Squared Reconstruction Error
    mse_error = sum((orig - rec) ** 2 for orig, rec in zip(scan_pixels, reconstructed)) / len(scan_pixels)
    
    is_anomaly = mse_error >= error_threshold
    return {
        "scan_id": scan_id,
        "reconstruction_error": round(mse_error, 4),
        "status": "ANOMALI TERDETEKSI (Segera Tinjau!)" if is_anomaly else "NORMAL (Lolos Otomatis)",
        "action": "ESKALASI_DOKTER_SENIOR" if is_anomaly else "ARSIP_RUTIN"
    }

if __name__ == "__main__":
    print("[*] Menjalankan Pipeline Skrining Anomali VAE Medis...")
    
    # Pasien A: Organ Paru-Paru Sehat (Fluktuasi wajar)
    patient_a = [1.02, 1.18, 0.92, 1.08, 1.01, 0.96, 1.04]
    res_a = evaluate_scan_anomaly("PASIEN_001_NORMAL", patient_a)
    print(f"\n[Hasil {res_a['scan_id']}]")
    print(f"    Error: {res_a['reconstruction_error']} -> Status: {res_a['status']} -> Tindakan: {res_a['action']}")
    
    # Pasien B: Terdapat Nodul Tumor / Anomali (Penyimpangan tajam pada fitur 3 dan 4)
    patient_b = [1.02, 1.18, 4.85, 5.20, 1.01, 0.96, 1.04]
    res_b = evaluate_scan_anomaly("PASIEN_002_TUMOR", patient_b)
    print(f"\n[Hasil {res_b['scan_id']}]")
    print(f"    Error: {res_b['reconstruction_error']} -> Status: {res_b['status']} -> Tindakan: {res_b['action']}")
```

---

### LAYER 5: DIAGNOSTIC DRILL (STUDI KASUS & UJI MANDIRI)

#### Skenario Kasus Lapangan
Direktur Keamanan Kartu Kredit di sebuah bank nasional ingin menguji apakah sistem deteksi fraud berbasis kecerdasan buatan mereka mampu bertahan terhadap metode pembobolan rekening baru yang memanfaatkan malware seluler. 
Manajer IT junior mengusulkan: *"Kita beli saja 10.000 data transaksi kartu kredit yang dicuri dari dark web untuk menguji sistem kita."* 
Direktur menolak karena melanggar hukum perbankan. Lead AI Architect kemudian menyarankan menggunakan **Generative Adversarial Network (GAN)** untuk menciptakan transaksi fraud sintetis. Manajer IT bingung dan bertanya: *"Kenapa harus pakai GAN yang rumit dengan dua neural network yang saling bertengkar? Kenapa tidak pakai neural network biasa saja untuk menduplikasi transaksi fraud lama yang ada di database kita?"*

#### Lembar Uji Mandiri
1. Berdasarkan Kaidah 3 dan Kaidah 4, apa argumen terkuat yang harus diberikan oleh Lead AI Architect untuk meyakinkan Manajer IT tentang keharusan menggunakan GAN?
2. Dalam kasus departemen radiologi rumah sakit dengan jutaan citra CT scan, mengapa arsitektur Variational Autoencoders (VAEs) jauh lebih tepat untuk skrining anomali dibandingkan model klasifikasi supervised biasa?
3. Apa perbedaan mendasar antara model diskriminatif dan model generatif saat menangani berkas foto rontgen dada pasien?

#### Kunci Jawaban Lengkap & Analisis Diagnostik
1. **Argumen Terkuat Keharusan GAN: Kemampuan Menciptakan Skenario Fraud Baru yang Belum Ada di Data Historis.** Menduplikasi transaksi lama dengan neural network biasa hanya menguji apa yang sudah diketahui (*known attacks*). Sindikat kejahatan selalu mengubah nominal, jeda waktu, dan pola belanja. Generator pada GAN dipaksa secara matematis untuk terus menemukan celah baru yang belum pernah dilihat oleh Discriminator, memungkinkan bank mensintesis jutaan variasi penipuan masa depan tanpa melanggar hukum privasi nasabah.
2. **Keunggulan VAE pada Skrining Medis:** Model klasifikasi supervised membutuhkan label positif dari setiap jenis penyakit yang mungkin terjadi. Di dunia medis, terdapat ribuan variasi penyakit langka yang rumah sakit tidak memiliki sampel latihnya. VAE tidak perlu tahu apa nama penyakitnya; VAE hanya belajar bentuk anatomi organ manusia yang sehat. Setiap kali ada jaringan tubuh yang menyimpang dari pola sehat (anomali apa pun), VAE akan gagal merekonstruksinya dan langsung memicu alarm tanda bahaya.
3. **Perbedaan Model pada Foto Rontgen:**
   - **Model Diskriminatif:** Menghitung probabilitas bersyarat P(Y|X) untuk mencocokkan foto dengan salah satu label yang sudah diajarkan (misal: "Pneumonia 92%", "Normal 8%"). Model tidak bisa menggambar foto rontgen baru.
   - **Model Generatif:** Memodelkan distribusi visual P(X) dari paru-paru manusia, mampu merekonstruksi citra normal, atau menghasilkan citra sintetis paru-paru beresolusi tinggi untuk keperluan riset mahasiswa kedokteran.
