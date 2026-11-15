# Track 3: Peta Falasi & Bedah Kerancuan Berpikir
## Modul 13: Falasi Kausalitas: Post Hoc, Korelasi vs Kausasi & Confounder
> **Referensi Transkrip Primer:** `012 - Science and Scientific Thinking for Everyone.md`, `010 - Discussing Problem Solving and Cania’s Pregnancy Program.md`  
> **Target Kompetensi:** Membedakan urutan temporal dari relasi sebab-akibat (*Post Hoc Ergo Propter Hoc*), membedah korelasi semu (*spurious correlation*), mengidentifikasi variabel pengganggu (*confounding variables*), serta menguasai kriteria kausalitas Bradford Hill.

---

### LAYER 1: KAIDAH EMAS (CORE AXIOMS)
1. **The Temporal Fallacy Axiom (Post Hoc Ergo Propter Hoc)**: Fakta bahwa peristiwa B terjadi secara kronologis setelah peristiwa A (A mendahului B) sama sekali TIDAK MEMBUKTIKAN bahwa peristiwa A adalah penyebab dari peristiwa B. Urutan waktu adalah syarat perlu (*necessary condition*), bukan syarat cukup (*sufficient condition*) bagi pembuktian kausalitas.
2. **Correlation Does Not Equal Causation**: Dua variabel X dan Y yang bergerak bersamaan secara statistik (*covariance / correlation*) dapat merefleksikan empat kemungkinan realitas yang berbeda: (a) X menyebabkan Y, (b) Y menyebabkan X (*reverse causality*), (c) X dan Y sama-sama disebabkan oleh faktor ketiga Z (*confounding variable / common cause*), atau (d) Hubungan tersebut murni kebetulan matematis (*spurious correlation*).
3. **The Confounder Elimination Invariant**: Mengklaim hubungan sebab-akibat langsung antara X dan Y tanpa mengendalikan atau mengisolasi variabel perancu (*confounding variables*) adalah kekeliruan analisis data paling fatal. Uji kausalitas yang sahih mewajibkan isolasi variabel melalui Randomized Controlled Trial (RCT) atau teknik ekonometrika kontrol (*instrumental variables, difference-in-differences*).
4. **The Directionality Invariant (Reverse Causality)**: Dalam banyak fenomena sosial dan psikologis, panah kausalitas sering kali berjalan berlawanan arah dari apa yang diasumsikan secara intuitif. Menemukan bahwa "orang yang berolahraga teratur lebih bahagia" tidak otomatis berarti olahraga menyebabkan kebahagiaan; bisa jadi orang yang sudah bahagia secara mental memiliki energi dan motivasi lebih tinggi untuk berolahraga teratur.
5. **The Bradford Hill Criteria for Causality**: Penarikan kesimpulan kausalitas dari data observasional hanya sah jika memenuhi standar Bradford Hill: kekuatan korelasi (*strength*), konsistensi lintas studi (*consistency*), spesifisitas relasi (*specificity*), gradien dosis-respons (*biological gradient*), dan mekanisme biologis/mekanistik yang masuk akal (*plausibility*).

---

### LAYER 2: MENTAL MODEL & DIAGRAM ASCII
```text
+-------------------------------------------------------------------------------+
|                       THE CAUSALITY DECISION TREE                             |
+-------------------------------------------------------------------------------+

                       [DUA VARIABEL BERKORELASI: X & Y]
                                       │
            ┌──────────────────────────┴──────────────────────────┐
            ▼                                                     ▼
     [KORELASI SEMU]                                      [KORELASI RIIL]
    Murni Kebetulan Acak                                          │
   (P-Hacking / Coincidence)                   ┌──────────────────┴──────────────────┐
            │                                  ▼                                     ▼
            ▼                        [ADA FAKTOR KETIGA: Z]               [HUBUNGAN KAUSAL LANGSUNG]
     GUGUR TOTAL                     Confounding Variable                            │
  (Contoh: Penjualan Es Krim                   │                          ┌──────────┴──────────┐
   vs Serangan Hiu di Laut)                    ▼                          ▼                     ▼
                                     Z MEMPENGARUHI X & Y               X -> Y                Y -> X
                                    (Z = Musim Panas Terik)         Kausasi Normal      Reverse Causality

+-------------------------------------------------------------------------------+
|                   CONFOUNDING VARIABLE VISUALIZATION                          |
+-------------------------------------------------------------------------------+

                               [MUSIM PANAS TERIK (Z)]
                                 (Confounding Factor)
                                      /        \
                                     /          \
                                    ▼            ▼
                   [PENJUALAN ES KRIM (X)] <....> [KASUS TENGGELAM (Y)]
                                      KORELASI SEMU
                       (Es krim BUKAN penyebab orang tenggelam!)
```

---

### LAYER 3: SYARAH DAGING (DEEP DIVE 1-TO-1 SYMMETRY)

#### 1. Syarah Kaidah 1: The Temporal Fallacy Axiom (Post Hoc Ergo Propter Hoc)
"Ayam jantan berkokok pada pukul 05:00 subuh. Pukul 05:30 matahari terbit. Oleh karena itu, kokok ayam jantan menyebabkan matahari terbit."

Secara intuitif kita tertawa mendengar contoh ayam tersebut. Namun dalam kehidupan sehari-hari, masyarakat modern melakukan kekeliruan persis yang sama ribuan kali:
- "Kemarin saya minum ramuan rebusan daun sirih, hari ini flu saya sembuh. Berarti daun sirih menyembuhkan flu!" (Mengabaikan fakta bahwa sistem imun tubuh manusia secara alami memang membersihkan virus flu dalam siklus 3-5 hari).
- "Setelah presiden baru dilantik bulan lalu, harga cabai langsung melonjak. Berarti presiden baru adalah biang keladi naiknya harga cabai!" (Mengabaikan faktor gagal panen akibat cuaca ekstrem El Nino di daerah sentra produksi).

Menyandarkan sebab-akibat hanya pada urutan waktu adalah insting hewani primitif (*magical thinking*). Urutan temporal hanyalah titik awal investigasi, bukan kesimpulan kausal.

#### 2. Syarah Kaidah 2: Correlation Does Not Equal Causation
Jika Anda mengunduh data publik, Anda akan menemukan korelasi matematis sebesar 99% antara "Tingkat perceraian di negara bagian Maine" dengan "Konsumsi margarin per kapita di Amerika Serikat". Apakah margarin menyebabkan perceraian? Apakah perceraian memaksa orang makan margarin? Jelas tidak. Keduanya adalah dua deret angka independen yang kebetulan bergerak searah pada periode waktu yang sama (*spurious correlation*).

Ada empat kemungkinan relasi saat dua variabel bergerak bersamaan:
1. **X → Y**: Rokok menyebabkan kanker paru (kausasi sejati).
2. **Y → X**: Kepemilikan senjata vs kejahatan (apakah senjata memicu kejahatan, atau tingginya kejahatan memaksa warga membeli senjata?).
3. **Z → X dan Y**: Tingkat konsumsi kopi vs umur panjang (mungkin orang yang minum kopi punya status ekonomi lebih mapan [Z] yang memberi akses ke fasilitas kesehatan terbaik).
4. **Acak**: Fluktuasi kebetulan tanpa keterkaitan logis apa pun.

#### 3. Syarah Kaidah 3: The Confounder Elimination Invariant
Variabel perancu (*confounder*) adalah musuh nomor satu analis data. Confounder adalah variabel tersembunyi yang mempengaruhi variabel independen sekaligus variabel dependen.
Perhatikan studi klasik:
"Siswa yang mengikuti les musik instrumental memiliki nilai matematika lebih tinggi daripada siswa yang tidak les musik. Kesimpulan: Les piano membuat otak anak lebih pintar matematika!"

Sebelum Anda buru-buru membelikan anak Anda piano seharga 50 juta rupiah, periksa variabel perancunya: **Tingkat Sosial Ekonomi dan Pendidikan Orang Tua (Z)**.
Orang tua yang mampu menyekolahkan anaknya les piano biasanya memiliki penghasilan tinggi, pendidikan sarjana, lingkungan rumah yang tenang, dan nutrisi gizi terbaik. Gizi dan kestabilan ekonomi inilah yang mendongkrak nilai matematika anak, bukan tuts piano. Begitu faktor kekayaan orang tua dikontrol secara statistik, efek les piano terhadap nilai matematika sering kali menyusut mendekati nol.

#### 4. Syarah Kaidah 4: The Directionality Invariant (Reverse Causality)
*Reverse Causality* terjadi ketika peneliti atau pembuat kebijakan salah membaca arah jarum kompas kausalitas.
Contoh dalam kebijakan pendidikan:
"Sekolah-sekolah yang memasang proyektor pintar dan pendingin udara (AC) di setiap kelas memiliki tingkat kelulusan siswa 98%. Oleh karena itu, kita harus membagikan AC dan proyektor ke seluruh sekolah pelosok untuk mendongkrak kepintaran siswa!"

Ini membalik arah kausalitas. Sekolah memasang proyektor pintar karena mereka adalah sekolah unggulan dengan anggaran berlimpah yang disaring dari siswa-siswa paling berprestasi sejak awal (*reverse causality*). Membagikan proyektor ke sekolah pelosok tanpa melatih kompetensi guru tidak akan mengubah kapasitas intelektual siswa.

#### 5. Syarah Kaidah 5: The Bradford Hill Criteria for Causality
Sir Austin Bradford Hill merumuskan standar emas epidemiologi untuk memvalidasi kausalitas sebelum RCT dapat dijalankan secara etis:
1. **Strength**: Seberapa besar *Odds Ratio* atau *Relative Risk*? (Rokok melipatgandakan risiko kanker 10-30 kali lipat, bukan hanya 1.05 kali).
2. **Consistency**: Apakah hasil riset yang sama ditemukan oleh peneliti di Jepang, Brasil, dan Jerman dengan metode berbeda?
3. **Biological Gradient (Dose-Response)**: Apakah semakin banyak dosis paparan X, semakin besar efek dampak Y? (Makin banyak jumlah batang rokok dihisap per hari, makin tinggi risiko tumor).
4. **Plausibility & Coherence**: Apakah ada mekanisme biokimiawi atau fisika yang masuk akal menjelaskan transmisi kausalitas tersebut?

---

### LAYER 4: FIELD PLAYBOOK (TACTICAL SOP & CODE)

#### SOP Diagnostik Kausalitas Data Lapangan
1. **Langkah 1: Periksa Kronologi (Temporal Precedence)**
   - Apakah penyebab benar-benar mendahului akibat? Waspadai data cross-sectional yang diambil pada satu titik waktu bersamaan.
2. **Langkah 2: Buru Variabel Pengganggu (The Confounder Hunt)**
   - Buat daftar faktor latar belakang: status sosial ekonomi, usia, genetik, tren musiman, bias seleksi diri (*self-selection*).
   - Apakah penelitian melakukan kontrol statistik terhadap variabel-variabel ini?
3. **Langkah 3: Uji Gradien Dosis-Respons (Dose-Response Check)**
   - Jika dosis intervensi dilipatgandakan, apakah dampaknya ikut membesar secara proporsional? Jika grafiknya acak-acakan, waspadai korelasi semu.
4. **Langkah 4: Tuntut Mekanisme Transmisi (Mechanism Verification)**
   - Jelaskan rantai fisik/perilaku: dari mana atom atau keputusan manusia berpindah dari X ke Y? Tanpa mekanisme yang masuk akal, tolak klaim kausalitas.

#### Script Python: Confounder Correlation Simulator
```python
# correlation_causality.py
import numpy as np

def simulate_confounding():
    """Simulasi bagaimana variabel ketiga (Z: Musim Panas) menciptakan korelasi semu antara X dan Y"""
    np.random.seed(42)
    n_days = 365
    
    # Z: Temperatur luar ruangan (15 - 35 derajat celcius)
    temperature_z = np.random.uniform(15, 35, n_days)
    
    # X: Penjualan es krim dipengaruhi oleh temperatur Z + noise acak
    ice_cream_x = 50 + (3.5 * temperature_z) + np.random.normal(0, 5, n_days)
    
    # Y: Kasus tenggelam di pantai dipengaruhi oleh temperatur Z (lebih banyak orang berenang) + noise acak
    drownings_y = 2 + (0.4 * temperature_z) + np.random.normal(0, 2, n_days)
    
    # Hitung korelasi mentah X dan Y
    raw_corr = np.corrcoef(ice_cream_x, drownings_y)[0, 1]
    
    print(f"Korelasi Mentah Penjualan Es Krim (X) vs Kasus Tenggelam (Y): {raw_corr:.4f}")
    print("STATUS: Korelasi statistik sangat kuat (r > 0.8), namun kausasi = 0%!")
    print("PENJELASAN: Kedua variabel semata-mata digerakkan oleh Confounder Suhu (Z).")

if __name__ == "__main__":
    simulate_confounding()
```

---

### LAYER 5: DIAGNOSTIC DRILL (STUDI KASUS & UJI MANDIRI)

#### Skenario Kasus Lapangan
Sebuah lembaga survei merilis laporan riset sosial yang menghebohkan media nasional:
> "Ditemukan korelasi positif yang sangat signifikan (r = 0.82, p < 0.001) antara jumlah konsumsi kopi per cangkir per hari dengan tingkat kesuksesan finansial (pendapatan bulanan di atas Rp 50 juta). Oleh karena itu, jika generasi muda ingin cepat kaya raya, minumlah minimal 4 cangkir kopi specialty setiap hari sejak usia dini!"

#### Pertanyaan Uji Nalar
1. Mengapa klaim kesimpulan lembaga survei tersebut merupakan bentuk sesat pikir *Correlation as Causation*?
2. Identifikasi sekurang-kurangnya dua *confounding variables* yang paling masuk akal menjadi pemicu riil di balik hubungan statistik tersebut!
3. Jelaskan potensi terjadinya *reverse causality* dalam temuan riset tersebut!

#### Kunci Jawaban & Bedah Anti-Patterns
1. **Analisis Kerancuan Kausalitas:**
   - Lembaga survei melakukan lompatan nalar dari korelasi statistik (r = 0.82) menjadi rekomendasi kausal resep kekayaan ("minumlah 4 cangkir agar cepat kaya"). Hubungan statistik tidak pernah membuktikan bahwa senyawa kafein memiliki khasiat mencetak uang di rekening bank.
2. **Dua Confounding Variables Utama:**
   - **Tipe Profesi & Industri Pekerjaan (Z1):** Pekerja kerah putih di sektor keuangan, hukum korporasi, konsultan strategi, dan rekayasa perangkat lunak memiliki pendapatan tinggi sekaligus beban kerja analitis berjam-jam di depan komputer yang membutuhkan kopi sebagai stimulan fokus.
   - **Gaya Hidup & Lokasi Tempat Tinggal (Z2):** Penduduk kota metropolitan kelas menengah-atas memiliki akses finansial untuk nongkrong dan membeli kopi premium Rp 50.000 per cangkir setiap hari di kafe, sementara pekerja dengan upah minimum tidak memiliki daya beli untuk konsumsi tersebut. Pendapatan tinggilah yang memungkinkan konsumsi kopi mahal, bukan sebaliknya.
3. **Analisis Reverse Causality:**
   - Orang berpenghasilan tinggi (> Rp 50 juta/bulan) memiliki daya beli untuk membeli 4 cangkir kopi specialty tanpa terbebani anggaran bulanan (Y → X). Menyarankan mahasiswa miskin menghabiskan uang sakunya untuk membeli 4 cangkir kopi mahal justru akan memicu kebangkrutan finansial (*destruction of capital*), bukan kekayaan.
