# Track 6: Pengambilan Keputusan Strategis
## Modul 27: Opportunity Cost & Expected Value dalam Mengarungi Ketidakpastian
> **Referensi Transkrip Primer:** `003 - The Struggles of a People Pleaser, the Importance of Mentors in Learning, & Managing Priorities.md`, `010 - Discussing Problem Solving and Cania’s Pregnancy Program.md`  
> **Target Kompetensi:** Menguasai kalkulasi Opportunity Cost (Biaya Peluang) mutlak, membangun pohon probabilitas Expected Value (EV = ∑ P_i × V_i), membedakan kualitas proses keputusan (*decision quality*) dari hasil keluaran (*outcome quality / resulting bias*), serta menaklukkan Risk Aversion yang irasional.

---

### LAYER 1: KAIDAH EMAS (CORE AXIOMS)
1. **The Invisibility of Opportunity Cost**: Setiap kali Anda memilih untuk melakukan sesuatu (A), Anda secara otomatis dan tak terelakkan sedang memilih untuk TIDAK melakukan alternatif terbaik lainnya yang mungkin (B). Biaya peluang (*opportunity cost*) adalah nilai dari alternatif terbaik yang Anda korbankan (*the next best alternative forgone*). Menghitung biaya tanpa menghitung apa yang Anda korbankan dari ketiadaan opsi B adalah kebutaan ekonomi fundamental.
2. **The Expected Value Formula (EV = ∑ P_i × V_i)**: Dalam kondisi ketidakpastian, nilai rasional dari suatu taruhan strategis adalah Nilai Harapan (*Expected Value*): jumlah dari perkalian probabilitas setiap kemungkinan hasil (P_i) dengan nilai utilitas hasil tersebut (V_i). Keputusan yang rasional secara matematika adalah keputusan yang memaksimalkan EV positif kumulatif dalam jangka panjang, bukan keputusan yang menghindari risiko secara mutlak.
3. **The Resulting Fallacy (Annie Duke)**: Menilai kualitas suatu keputusan semata-mata berdasarkan hasil akhirnya (*outcome*) adalah kesesatan bernalar *Resulting Bias*. Keputusan yang brilian dengan EV positif tinggi bisa saja berujung pada kegagalan karena faktor probabilitas acak 5%; sebaliknya, keputusan bodoh dan ceroboh bisa saja berujung pada keberuntungan sesaat. Pemikir master memuji kualitas proses kalkulasi, bukan hasil kebetulan.
4. **The Asymmetry of Gambler’s Ruin (Zero Ruin Probability)**: Betapapun tingginya nilai harapan (EV) positif dari suatu peluang, Anda DILARANG mengambil taruhan yang memiliki probabilitas non-nol terhadap kehancuran total atau kebangkrutan mutlak (*risk of ruin / absorb state*). Keuntungan matematis tidak ada artinya jika Anda tereliminasi dari permainan (*survival precedes optimization*).
5. **The Kelly Criterion Framework**: Besaran alokasi modal atau energi yang optimal dalam suatu peluang ber-EV positif ditentukan oleh Formula Kelly: f^* = (b · p - q) / b. Mempertaruhkan terlalu sedikit modal memperlambat pertumbuhan; mempertaruhkan modal melebihi Fraksi Kelly menjamin kehancuran portofolio akibat volatilitas.

---

### LAYER 2: MENTAL MODEL & DIAGRAM ASCII
```text
+-------------------------------------------------------------------------------+
|                       THE PROBABILITY DECISION TREE (EV)                      |
+-------------------------------------------------------------------------------+

                             [KEPUTUSAN STRATEGIS: LUNCURKAN PRODUK X]
                                                │
                      ┌─────────────────────────┴─────────────────────────┐
                      │ Peluang Sukses: P1 = 0.40                         │ Peluang Gagal: P2 = 0.60
                      ▼                                                   ▼
             [SKENARIO SUKSES]                                   [SKENARIO GAGAL]
             Laba: + Rp 500 Juta                                 Rugi: - Rp 100 Juta
                      │                                                   │
                      ▼                                                   ▼
             BOBOT NILAI HASIL                                   BOBOT NILAI HASIL
             0.40 × (+500 Juta) = + Rp 200 Juta                  0.60 × (-100 Juta) = - Rp 60 Juta
                      │                                                   │
                      └─────────────────────────┬─────────────────────────┘
                                                ▼
                                EXPECTED VALUE (EV) BERSIH:
                                + Rp 200 Juta - Rp 60 Juta = + Rp 140 JUTA!
                                (KEPUTUSAN HIGHLY POSITIVE EV -> WAJIB DIEKSEKUSI)

+-------------------------------------------------------------------------------+
|                      RESULTING BIAS MATRIX (ANNIE DUKE)                       |
+-------------------------------------------------------------------------------+

                                       HASIL AKHIR: SUKSES          HASIL AKHIR: GAGAL
                                    ┌────────────────────────────┬────────────────────────────┐
   PROSES KEPUTUSAN: BAIK (+EV)     │ KEPUTUSAN CEMERLANG        │ NASIB BURUK / ANOMALI ACAK │
                                    │ (Ulangi Proses Ini!)       │ (Jangan Salahkan Proses!)  │
                                    ├────────────────────────────┼────────────────────────────┤
   PROSES KEPUTUSAN: BURUK (-EV)    │ KEBERUNTUNGAN SEMU         │ KONSEKUENSI BODOH WAJAR    │
                                    │ (Bahaya: Ilusi Kepintaran!)│ (Perbaiki Pola Nalar!)     │
                                    └────────────────────────────┴────────────────────────────┘
```

---

### LAYER 3: SYARAH DAGING (DEEP DIVE 1-TO-1 SYMMETRY)

#### 1. Syarah Kaidah 1: The Invisibility of Opportunity Cost
Bayangkan seorang pemilik toko ruko yang bangga menyatakan: "Bisnis saya menghasilkan laba bersih Rp 10 juta per bulan!".
Ketika ditanya: "Ruko ini sewa atau milik sendiri?", ia menjawab: "Milik sendiri warisan orang tua, jadi gratis tanpa biaya sewa!".
Secara akuntansi kasir sederhana, ia merasa untung Rp 10 juta.
Namun bagaimana dari kacamata **Opportunity Cost**?
Jika ruko tersebut disewakan ke pihak bank atau waralaba minimarket, uang sewa pasarannya adalah Rp 180 juta per tahun (Rp 15 juta per bulan). Ditambah lagi, pemilik toko menghabiskan 60 jam seminggu menjaga kasir ruko, padahal dengan kompetensinya ia bisa bekerja sebagai manajer ritel dengan gaji Rp 12 juta per bulan.
Hitung Biaya Peluang:
Nilai alternatif yang dikorbankan = Sewa ruko (Rp 15 juta) + Gaji manajer (Rp 12 juta) = Rp 27 juta per bulan.
Bisnis yang ia sangka "untung Rp 10 juta" sesungguhnya sedang **merugi Rp 17 juta setiap bulan**! 
Biaya peluang adalah hantu tak terlihat yang diam-diam memiskinkan orang-orang yang tidak memahami ekonomi.

#### 2. Syarah Kaidah 2: The Expected Value Formula (EV = ∑ P_i × V_i)
Banyak orang lumpuh mengambil keputusan karena mereka menuntut kepastian 100%. "Bagaimana kalau saya gagal? Bagaimana kalau bisnis baru ini rugi?".
Di dunia nyata, tidak ada kepastian 100%. Dunia ini dikendalikan oleh probabilitas.
Alat bantu seorang pemikir rasional adalah **Expected Value (Nilai Harapan)**:
Bayangkan Anda ditawari melempar dadu:
- Jika angka 1 sampai 4 keluar (Peluang 4/6 = 66.7%), Anda mendapatkan Rp 300.000.
- Jika angka 5 atau 6 keluar (Peluang 2/6 = 33.3%), Anda kehilangan Rp 200.000.
Berapa EV-nya?
EV = (0.667 × 300.000) + (0.333 × -200.000) = 200.000 - 66.600 = + Rp 133.400
Setiap kali Anda melempar dadu, Anda secara rata-rata mencetak kekayaan Rp 133.400. Apakah Anda bisa kalah pada lemparan pertama? Tentu saja! Anda bisa melempar angka 6 dan rugi Rp 200.000. Tetapi jika Anda memainkan permainan ini 1.000 kali, hukum bilangan besar (*Law of Large Numbers*) menjamin Anda pulang membawa jutaan rupiah. Orang rasional fokus mengejar taruhan dengan EV positif berulang kali dalam hidup.

#### 3. Syarah Kaidah 3: The Resulting Fallacy (Annie Duke)
Annie Duke, seorang juara dunia poker profesional sekaligus ilmuwan kognitif, mengidentifikasi bias mematikan yang disebut *Resulting*:
Seorang pengemudi mabuk berat pulang ke rumah dengan kecepatan tinggi, menerobos 4 lampu merah, dan sampai di rumah dengan selamat tanpa lecet sedikit pun. Apakah mengemudi mabuk adalah keputusan yang baik? Jelas tidak! Itu keputusan yang sangat bodoh dan berisiko kematian tinggi, namun kebetulan hasil malam itu tidak terjadi tabrakan (*dumb luck*).
Di sisi lain, seorang dokter bedah melakukan prosedur operasi darurat sesuai protokol medis terbaik dengan probabilitas keselamatan 90%. Pasien meninggal di meja operasi karena komplikasi alergi obat yang sangat langka (peluang 1%). Apakah dokter tersebut mengambil keputusan yang salah? Tidak! Keputusannya 100% tepat secara EV.

Jangan pernah mengevaluasi keputusan hanya dari hasil akhirnya. Audit **kualitas proses bernalarnya**: Apakah informasinya lengkap? Apakah probabilitasnya dihitung cermat? Apakah trade-offs-nya ditimbang? Jika prosesnya benar, hasil buruk adalah variansi statistik acak yang tidak perlu disesali secara emosional.

#### 4. Syarah Kaidah 4: The Asymmetry of Gambler’s Ruin (Zero Ruin Probability)
Ada satu aturan mutlak dalam matematika ketidakpastian: **Jangan pernah mengalikan probabilitas dengan angka nol**.
Jika Anda memainkan permainan Russian Roulette dengan pistol revolver 6 peluru berisi 1 peluru:
- Peluang selamat: 5/6 (83.3%). Hadiah jika selamat: Rp 10 Miliar.
- Peluang mati: 1/6 (16.7%). Konsekuensi jika kena peluru: Kematian.
Kalkulasi matematis kasar mungkin menunjukkan EV moneter yang luar biasa tinggi (+ Rp 8.3 Miliar!). Tetapi tidak ada orang waras yang mau menarik pelatuk pistol ke kepalanya.
Mengapa? Karena kematian adalah **Absorbing Barrier (Titik Henti Mutlak)**. Sekali Anda mati, Anda tidak bisa lagi bermain di putaran berikutnya.
Dalam karier dan investasi: Jangan pernah mengambil manuver yang memiliki risiko penjara, kebangkrutan utang tanpa batas (*infinite liability*), atau kematian reputasi moral. Pertahanan diri (*survival*) mendahului maksimalisasi laba.

#### 5. Syarah Kaidah 5: The Kelly Criterion Framework
Fisikawan John Kelly di Bell Labs merumuskan formula matematika untuk alokasi modal optimal:
f^* = (b · p - q / b)
Di mana p adalah peluang menang, q adalah peluang kalah (1-p), dan b adalah rasio pembayaran (*odds*).
Formula Kelly membuktikan:
- Jika Anda bertaruh terlalu kecil di bawah Fraksi Kelly, portofolio Anda bertumbuh sangat lambat.
- Jika Anda bertaruh melebihi Fraksi Kelly (*overbetting* karena serakah), volatilitas acak dalam jangka panjang **dipastikan 100% menghabiskan seluruh modal Anda**.
Pelajaran hidup: Ketika Anda menemukan peluang karier atau bisnis dengan EV positif yang terbukti, jangan bertaruh sembarangan dengan menghabiskan seluruh tabungan hidup Anda sekaligus. Alokasikan fraksi modal terukur secara proporsional sesuai keunggulan probabilitas Anda.

---

### LAYER 4: FIELD PLAYBOOK (TACTICAL SOP & CODE)

#### SOP Pengambilan Keputusan Berbasis Expected Value & Opportunity Cost
1. **Langkah 1: Petakan Alternatif Terbaik yang Hilang (Opportunity Cost Scan)**
   - "Jika waktu/uang ini tidak saya alokasikan ke proyek X, ke mana alokasi terbaik berikutnya yang bisa saya tempatkan?"
2. **Langkah 2: Konstruksi Pohon Skenario (Scenario Mapping)**
   - Buat 3 skenario: *Best Case* (Optimis), *Base Case* (Realistis), dan *Worst Case* (Pesimis).
   - Beri bobot probabilitas pada tiap skenario (total wajib 1.0 / 100%).
3. **Langkah 3: Hitung Expected Value (EV)**
   - Kalikan bobot dengan nilai utilitas/rupiah. Jumlahkan seluruhnya.
4. **Langkah 4: Terapkan Filter Risiko Kehancuran (Zero Ruin Filter)**
   - Periksa skenario terburuk (*Worst Case*): Apakah skenario terburuk bisa memicu kebangkrutan total, penjara, atau cacat permanen? Jika YA, batalkan keputusan seketika terlepas dari tingginya EV.

#### Script Python: Expected Value & Kelly Criterion Portfolio Simulator
```python
# ev_kelly_calculator.py
class DecisionProbabilityEngine:
    @staticmethod
    def calculate_ev(scenarios):
        """
        scenarios: list of dict -> [{"prob": 0.4, "value": 500}, {"prob": 0.6, "value": -100}]
        """
        total_prob = sum(s["prob"] for s in scenarios)
        assert abs(total_prob - 1.0) < 1e-5, "Total probabilitas seluruh skenario wajib 1.0 (100%)"
        
        ev = sum(s["prob"] * s["value"] for s in scenarios)
        return ev

    @staticmethod
    def calculate_kelly_fraction(win_prob, win_loss_ratio):
        """Formula Kelly: f* = (b*p - q) / b"""
        p = win_prob
        q = 1.0 - p
        b = win_loss_ratio
        kelly = (b * p - q) / b
        return max(0.0, kelly)

if __name__ == "__main__":
    engine = DecisionProbabilityEngine()
    # Kasus: Peluncuran lini produk baru (skenario optimis, normal, gagal)
    my_scenarios = [
        {"name": "Sukses Besar", "prob": 0.25, "value": 800000000},
        {"name": "Moderat Normal", "prob": 0.50, "value": 200000000},
        {"name": "Gagal Pasar", "prob": 0.25, "value": -150000000}
    ]
    net_ev = engine.calculate_ev(my_scenarios)
    print(f"Nilai Harapan (Expected Value) Bersih: Rp {net_ev:,.2f}")
    
    # Hitung alokasi modal Kelly jika peluang menang 60% dan payoff ratio 2:1
    fraction = engine.calculate_kelly_fraction(win_prob=0.60, win_loss_ratio=2.0)
    print(f"Alokasi Modal Maksimal Menurut Formula Kelly: {fraction * 100:.1f}% dari modal lancar")
```

---

### LAYER 5: DIAGNOSTIC DRILL (STUDI KASUS & UJI MANDIRI)

#### Skenario Kasus Lapangan
Rudi adalah pemilik toko roti tradisional keluarga yang sudah beroperasi 15 tahun di lokasi prima pusat kota. Toko roti tersebut menghasilkan keuntungan bersih stabil Rp 15 juta per bulan. 
Suatu hari, seorang pengembang waralaba minimarket nasional menawarinya kerja sama: Rudi tidak perlu lagi bangun jam 04:00 subuh untuk memanggang roti; ruko tersebut akan disewa oleh minimarket seharga Rp 30 juta per bulan selama kontrak 5 tahun penuh.
Rudi menolak tawaran tersebut dengan alasan:
> "Toko roti ini adalah keringat saya sendiri, dan saya bangga punya usaha yang untung Rp 15 juta per bulan tanpa bergantung pada korporasi minimarket!".  
> Dua tahun kemudian, jalan di depan ruko Rudi diubah menjadi satu arah oleh dinas perhubungan kota, omzet pembeli rotinya ambruk 70%, laba bersih tokonya turun menjadi hanya Rp 3 juta per bulan, sementara tawaran sewa minimarket sudah ditarik dan dialihkan ke ruko tetangga.

#### Pertanyaan Uji Nalar
1. Hitung berapa *Opportunity Cost* moneter yang dikorbankan Rudi selama 2 tahun pertama akibat keputusannya menolak sewa minimarket!
2. Analisis bagaimana kebiasaan Rudi menolak melihat alternatif terbaik membuatnya menjadi korban dari ilusi akuntansi kasir!
3. Jika dievaluasi secara *Expected Value* dan analisis ketidakpastian tata ruang kota, mengapa keputusan Rudi mempertahankan toko roti merupakan keputusan dengan EV negatif jangka panjang?

#### Kunci Jawaban & Bedah Anti-Patterns
1. **Perhitungan Opportunity Cost Rudi (2 Tahun Pertama):**
   - Nilai alternatif sewa minimarket yang dikorbankan: Rp 30.000.000 × 24 bulan = Rp 720.000.000 (pendapatan pasif tanpa kerja fisik).
   - Pendapatan toko roti yang diterima Rudi: Rp 15.000.000 × 24 bulan = Rp 360.000.000 (ditambah beban kerja fisik bangun jam 04:00 subuh setiap hari).
   - **Kerugian Biaya Peluang Rudi:** Rp 720.000.000 - Rp 360.000.000 = **RUDI MEMBAYAR Rp 360 JUTA** dari kantong pribadinya selama 2 tahun hanya demi memuaskan rasa bangga memegang gelar "pemilik usaha mandiri"!
2. **Kebutaan Akuntansi Kasir:**
   - Rudi menganggap sewa ruko adalah "bebas biaya" karena ruko milik sendiri. Ia gagal melihat bahwa ruko tersebut adalah aset modal yang memiliki nilai sewa pasar. Dengan mengoperasikan toko roti yang untung Rp 15 juta di atas ruko yang bernilai sewa Rp 30 juta, Rudi sesungguhnya sedang mensubsidi bisnis rotinya sendiri sebesar Rp 15 juta per bulan dari potensi sewa yang hilang.
3. **Analisis EV dan Ketidakpastian Kota:**
   - Kontrak minimarket 5 tahun menawarkan arus kas bergaransi korporasi nasional dengan probabilitas pembayaran mendekati 99% (EV ≈ Rp 30 juta/bulan stabil).
   - Bisnis roti tradisional rentan terhadap volatilitas lalu lintas jalan, inflasi tepung/mentega, dan pergeseran selera konsumen. Mempertahankan bisnis fisik rapuh dengan keuntungan di bawah nilai sewa pasar adalah keputusan dengan EV rendah yang menanggung risiko kehancuran asimetris (*high fragility*), sebagaimana terbukti ketika arah jalan diubah oleh dinas perhubungan.
