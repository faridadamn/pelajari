# Track 3: Peta Falasi & Bedah Kerancuan Berpikir
## Modul 14: Falasi Bukti Cacat: Cherry Picking & Texas Sharpshooter
> **Referensi Transkrip Primer:** `012 - Science and Scientific Thinking for Everyone.md`, `001 - Thinking Smart in a Stupid Environment.md`  
> **Target Kompetensi:** Mengidentifikasi manipulasi data berbasis Cherry Picking (*suppression of evidence*), membedah mekanisme Texas Sharpshooter Fallacy, membongkar P-hacking dalam analisis statistik, serta membangun protokol audit data yang menuntut pelaporan sampel utuh.

---

### LAYER 1: KAIDAH EMAS (CORE AXIOMS)
1. **The Completeness of Evidence Invariant**: Validitas suatu kesimpulan ilmiah menuntut evaluasi atas SELURUH bukti yang relevan dan tersedia (*Total Evidence Requirement*). Menyeleksi secara sengaja hanya data yang mengonfirmasi hipotesis sambil menyembunyikan atau membuang data yang membantahnya adalah kesesatan *Cherry Picking (Fallacy of Incomplete Evidence)*.
2. **The Texas Sharpshooter Fallacy Axiom**: Menembakkan peluru secara acak ke dinding gudang kosong, lalu baru kemudian menggambar lingkaran target sasaran tepat di sekitar lubang peluru yang paling mengelompok, adalah metafora sempurna dari *Texas Sharpshooter Fallacy*. Pola atau klaster yang terbentuk secara acak tidak boleh ditafsirkan sebagai bukti kausalitas bermakna tanpa pengujian hipotesis *a priori* independen.
3. **The Prohibition of Post-Hoc Hypothesizing (HARKing)**: Merumuskan hipotesis baru SETELAH melihat data hasil eksperimen (*Hypothesizing After the Results are Known / HARKing*) dan menyajikannya seolah-olah hipotesis itu diramalkan sejak awal adalah bentuk penipuan metodologis. Hipotesis yang dirumuskan pasca-fakta wajib diuji pada dataset baru yang terpisah.
4. **The P-Hacking & Publication Bias Boundary**: Jika Anda menguji 100 korelasi acak yang sama sekali tidak berhubungan pada tingkat signifikansi α = 0.05, secara matematis dijamin akan ada sekitar 5 korelasi yang tampak "signifikan secara statistik" murni karena kebetulan acak. Mempublikasikan hanya 5 korelasi ini dan membuang 95 hasil lainnya ke laci meja (*file drawer problem*) adalah korupsi riset.
5. **The Pre-Registration Protocol Shield**: Satu-satunya penangkal absolut terhadap Cherry Picking dan Texas Sharpshooter adalah registrasi protokol riset sebelum data dikumpulkan (*study pre-registration*), di mana hipotesis, metrik variabel, batas sampel, dan metode analisis dikunci secara publik sebelum observasi dimulai.

---

### LAYER 2: MENTAL MODEL & DIAGRAM ASCII
```text
+-------------------------------------------------------------------------------+
|                      THE TEXAS SHARPSHOOTER MECHANISM                         |
+-------------------------------------------------------------------------------+

   [DATA SEBENARNYA: DISTRIBUSI ACAK NOISE]     [MANIPULASI SHARPSHOOTER]
   
       •         •            •                     •         •            •
            •         •                                  •         •
       •       [• • •]       •                     •     ┌───────┐     •
               [• • •]                                   │• • •  │  <-- GAMBAR SASARAN
            •    • •          •                     •    │• • •  │      SETELAH TEMBAKAN!
       •                 •                               └───────┘
                                                    •    "Lihat! Saya jago menembak!"

+-------------------------------------------------------------------------------+
|                        CHERRY PICKING FILTER FUNNEL                           |
+-------------------------------------------------------------------------------+

                  [POPULASI SELURUH DATA EMPIRIS (100%)]
                                     │
           ┌─────────────────────────┴─────────────────────────┐
           ▼                                                   ▼
   [DATA MENGONFIRMASI (5%)]                           [DATA ANOMALI/GAGAL (95%)]
           │                                                   │
           ▼                                                   ▼
   DIJADIKAN HEADLINE BERITA /                         DIBUANG KE DALAM LACI
   KLAIM PEMASARAN PRODUK                              (File Drawer Problem)
           │
           ▼
   KESIMPULAN ILUSIF & DEGENERATIF (Cherry Picking)
```

---

### LAYER 3: SYARAH DAGING (DEEP DIVE 1-TO-1 SYMMETRY)

#### 1. Syarah Kaidah 1: The Completeness of Evidence Invariant
Ketika seorang politisi ingin membuktikan keberhasilan kepemimpinannya, ia memamerkan 5 proyek jembatan megah yang selesai tepat waktu. Apa yang tidak ia sampaikan adalah 95 proyek infrastruktur lainnya yang mangkrak, membengkak anggarannya 400%, dan terjerat kasus korupsi di pengadilan.

Inilah esensi dari *Cherry Picking*. Siapa pun bisa membuktikan klaim apa pun di dunia jika ia diperbolehkan memilah buah ceri yang manis dan membuang buah yang busuk. Industri tembakau selama puluhan tahun membiayai penelitian yang secara spesifik mencari sub-populasi perokok yang tidak terkena kanker untuk membingungkan publik. Kriteria kebenaran menuntut keterbukaan seluruh dataset: sebuah teori harus mampu bertahan di hadapan seluruh spektrum data, terutama data yang paling tidak nyaman.

#### 2. Syarah Kaidah 2: The Texas Sharpshooter Fallacy Axiom
Nama falasi ini berasal dari cerita lelucon Texas: Seorang koboi menembaki dinding kayu secara membabi buta dari jarak jauh. Setelah dinding berlubang ratusan peluru, ia mendekat dengan kuas cat merah dan menggambar lingkaran sasaran tepat di titik di mana peluru paling padat berkumpul. Saat warga kota lewat, ia membual bahwa ia adalah penembak jitu terbaik di dunia.

Dalam dunia medis dan sains semu, ini sering terjadi dalam investigasi klaster kanker (*cancer cluster*):
Di sebuah desa berpenduduk 1.000 orang, ditemukan 8 kasus kanker darah (leukemia) dalam satu RT yang berdekatan dengan menara BTS seluler. Warga panik dan menuntut menara dirobohkan dengan alasan radiasi BTS memicu leukemia.
Apa yang dilupakan warga? Di seluruh Indonesia ada puluhan ribu menara BTS. Berdasarkan hukum probabilitas acak (*Poisson clumping*), pasti akan ada satu atau dua desa di mana kasus kanker secara kebetulan mengelompok di dekat menara tanpa kaitan kausal apa pun. Ketika ratusan desa lain di dekat menara BTS tidak mengalami lonjakan leukemia, data desa-desa tersebut diabaikan. Menarik lingkaran sasaran pasca-fakta adalah ilusi kognitif otak manusia yang haus mencari pola dalam derau (*apophenia*).

#### 3. Syarah Kaidah 3: The Prohibition of Post-Hoc Hypothesizing (HARKing)
Dalam metode ilmiah yang sehat, urutannya adalah:
Hipotesis Awal → Pengumpulan Data → Uji Falsifikasi
Dalam praktik HARKing (*Hypothesizing After the Results are Known*), urutannya dibalik:
Kumpulkan 500 Variabel → Cari Pola yang Menonjol → Tulis Laporan Seolah-olah Pola Itu Hipotesis Asli
Ini adalah pembodohan metodologis. Mengapa? Karena kapasitas prediksi (*predictive power*) dari hipotesis tersebut menjadi nol. Ia tidak memprediksi apa-apa; ia hanya mendeskripsikan ulang kebetulan historis dari dataset yang sudah ada di tangan (*overfitting to noise*).

#### 4. Syarah Kaidah 4: The P-Hacking & Publication Bias Boundary
Ambang batas signifikansi standar dalam jurnal ilmiah adalah p < 0.05 (artinya kemungkinan hasil muncul karena kebetulan murni adalah kurang dari 5%).
Namun bayangkan seorang peneliti menguji pengaruh konsumsi permen jeli (*jelly beans*) terhadap jerawat. 
Ia menguji permen jeli warna merah, hijau, kuning, biru, ungu, hingga 20 warna berbeda.
Pada warna ke-14 (permen jeli hijau), nilai p keluar 0.045.
Peneliti tersebut langsung membuat rilis berita: "PERMEN JELI HIJAU TERBUKTI SECARA ILMIAH MENYEBABKAN JERAWAT (p < 0.05)!".
Apa yang disembunyikan? 19 pengujian warna lainnya yang tidak menunjukkan korelasi apa pun tidak pernah dilaporkan. Mengutak-atik data, membuang outlier tertentu, atau mencoba puluhan kombinasi variabel hingga angka p-value tembus di bawah 0.05 disebut *P-Hacking*. Ini adalah kejahatan epistemik berselubung matematika.

#### 5. Syarah Kaidah 5: The Pre-Registration Protocol Shield
Bagaimana komunitas sains global membasmi Cherry Picking dan P-hacking? Dengan sistem **Pre-Registration (Preregistrasi Riset)**.
Sebelum subjek pertama direkrut atau data pertama diunduh:
- Peneliti wajib mendaftarkan proposal eksperimennya di platform independen terbuka (seperti Open Science Framework atau ClinicalTrials.gov).
- Desain uji, variabel kontrol, ukuran sampel minimum, dan teknik statistik dikunci dengan tanda tangan digital berkala (*timestamp*).
- Jurnal sains berjanji menerbitkan hasil riset tersebut APA PUN HASILNYA (baik hipotesis terbukti maupun gagal total).
Dengan mekanisme ini, peneliti tidak bisa lagi menyembunyikan data yang gagal ke dalam laci meja atau menggambar target di sekitar lubang peluru.

---

### LAYER 4: FIELD PLAYBOOK (TACTICAL SOP & CODE)

#### SOP Audit Data & Deteksi Cherry Picking
1. **Langkah 1: Audit Kerangka Sampel (Denominator Check)**
   - Berapa total populasi atau pengujian awal sebelum data dipangkas?
   - Tuntut rasio: "Berapa rasio kasus sukses dibanding total kasus yang diteliti?"
2. **Langkah 2: Periksa Protokol A Priori**
   - Apakah hipotesis didaftarkan sebelum riset dimulai?
   - Apakah ada indikasi metrik diubah di tengah jalan (*moving the goalposts*)?
3. **Langkah 3: Tuntut Replikasi Dataset Independen (Out-of-Sample Testing)**
   - Jika sebuah algoritma atau teori trading saham mengaku menghasilkan profit 90% pada data historis 2020-2023, jangan percaya. Uji model tersebut pada data baru 2024-2025 yang belum pernah dilihat oleh algoritma. Jika kinerjanya ambruk, model tersebut hanyalah hasil *Texas Sharpshooter / Overfitting*.

#### Script Python: P-Hacking & Random Chance Simulator
```python
# phacking_simulator.py
import numpy as np

def simulate_phacking(num_random_tests=100, alpha=0.05):
    """Membuktikan bagaimana menguji banyak variabel acak pasti menghasilkan korelasi palsu"""
    np.random.seed(123)
    false_positives = 0
    p_values = []
    
    for _ in range(num_random_tests):
        # Dua variabel acak murni yang saling bebas
        var_a = np.random.normal(0, 1, 100)
        var_b = np.random.normal(0, 1, 100)
        
        # Hitung korelasi & estimasi p-value sederhana
        corr = np.corrcoef(var_a, var_b)[0, 1]
        # t-statistic approximation
        t_stat = corr * np.sqrt((100 - 2) / (1 - corr**2 + 1e-10))
        # two-tailed p-value kasar
        p_val = 2 * (1 - 0.5 * (1 + np.math.erf(abs(t_stat) / np.sqrt(2))))
        p_values.append(p_val)
        
        if p_val < alpha:
            false_positives += 1
            
    print(f"Total Uji Korelasi Acak: {num_random_tests}")
    print(f"Hasil Palsu yang Lolos Signifikan (p < {alpha}): {false_positives} kasus")
    print(f"Persentase Ilusi Signifikansi: {(false_positives / num_random_tests) * 100:.1f}%")
    print("KESIMPULAN: Melaporkan hanya hasil yang lolos signifikansi adalah manipulasi Texas Sharpshooter!")

if __name__ == "__main__":
    simulate_phacking()
```

---

### LAYER 5: DIAGNOSTIC DRILL (STUDI KASUS & UJI MANDIRI)

#### Skenario Kasus Lapangan
Sebuah perusahaan suplemen kesehatan meluncurkan produk pil herbal bernama "BrainBoost". Di situs resminya, mereka mengklaim:
> "Terbukti secara klinis meningkatkan daya ingat dan konsentrasi hingga 40%! Riset kami pada 30 partisipan menunjukkan peningkatan signifikan dalam tes memori visual (p = 0.03). Segera konsumsi untuk menjamin prestasi akademik anak Anda!"  
> Sebuah audit independen oleh otoritas pengawas obat mengungkap dokumen rahasia laboratorium perusahaan: ternyata perusahaan melakukan 45 jenis tes kognitif yang berbeda pada partisipan. Dari 45 jenis tes tersebut, 44 tes menunjukkan TIDAK ADA perbedaan signifikan antara peminum BrainBoost dengan kelompok plasebo (bahkan 10 tes menunjukkan penurunan memori). Perusahaan sengaja hanya mempublikasikan 1 tes memori visual yang kebetulan menghasilkan nilai p = 0.03.

#### Pertanyaan Uji Nalar
1. Identifikasi dua falasi metodologis spesifik yang dilakukan oleh manajemen perusahaan herbal tersebut!
2. Mengapa klaim "terbukti klinis (p = 0.03)" pada 1 dari 45 tes secara matematis tidak memiliki nilai ilmiah?
3. Jika Anda seorang auditor regulasi, sanksi epistemik dan koreksi metodologis apa yang wajib Anda jatuhkan pada klaim tersebut?

#### Kunci Jawaban & Bedah Anti-Patterns
1. **Identifikasi Falasi Metodologis:**
   - **Falasi 1: Cherry Picking (Suppression of Evidence).** Menyembunyikan 44 hasil tes yang gagal dan hanya mempublikasikan 1 tes yang menguntungkan.
   - **Falasi 2: Texas Sharpshooter / P-Hacking via Multiple Comparisons.** Menguji 45 metrik berbeda tanpa koreksi signifikansi statistik (seperti *Bonferroni Correction*), lalu menggambar lingkaran sasaran keberhasilan di sekitar 1 hasil yang lolos karena fluktuasi acak.
2. **Kelemahan Matematis Signifikansi:**
   - Pada tingkat signifikansi α = 0.05, jika kita menguji 45 hipotesis acak independen, probabilitas mendapatkan **setidaknya satu hasil positif palsu murni karena kebetulan acak** adalah:
     1 - (1 - 0.05)^{45} = 1 - (0.95)^{45} ≈ 1 - 0.099 = 0.901 = 90.1%!
   - Artinya, ada kepastian 90.1% bahwa satu hasil "signifikan" tersebut adalah derau acak belaka (*statistical fluke*). Tanpa koreksi Bonferroni (ambang baru seharusnya α = 0.05 / 45 = 0.0011), nilai p = 0.03 adalah sampah statistik.
3. **Koreksi Regulasi Standar Emas:**
   - Mewajibkan penarikan klaim iklan "terbukti klinis" dari seluruh kemasan produk.
   - Mengharuskan pendaftaran riset ulang dengan protokol preregistrasi, penetapan *primary endpoint* tunggal sebelum uji klinis dimulai, dan pelaporan seluruh data secara transparan ke basis data publik.
