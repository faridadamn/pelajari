# Track 6: Pengambilan Keputusan Strategis
## Modul 29: Framework Root Cause Analysis: 5-Whys Iteratif & Diagram Ishikawa
> **Referensi Transkrip Primer:** `010 - Discussing Problem Solving and Cania’s Pregnancy Program.md`, `007 - Meta Thinking Tips Structured Thinking and Argumentation.md`  
> **Target Kompetensi:** Menguasai metodologi Root Cause Analysis (RCA), mengeksekusi teknik 5-Whys tanpa terjebak pada rantai kausalitas semu, menyusun Diagram Tulang Ikan (*Ishikawa Fishbone* 6M), memisahkan gejala permukaan dari patologi struktural, serta merancang tindakan korektif permanen.

---

### LAYER 1: KAIDAH EMAS (CORE AXIOMS)
1. **The Symptom vs Pathology Demarcation**: Mengobati gejala permukaan (*symptoms*) tanpa menyentuh akar patologi struktural (*root cause*) hanya akan menunda bencana dan melipatgandakan keparahan masalah saat kambuh di kemudian hari. Plester luka tidak pernah menyembuhkan kanker; peredam demam tidak pernah membunuh bakteri infeksi di dalam darah.
2. **The 5-Whys Iterative Drilling Invariant (Sakichi Toyoda)**: Menemukan akar masalah menuntut penelusuran kausalitas vertikal ke belakang sekurang-kurangnya lima tingkat (*5-Whys*). Jawaban atas setiap pertanyaan "Mengapa?" wajib berupa fakta mekanistik terverifikasi, bukan asumsi tebakan emosional, hingga investigasi bermuara pada kegagalan sistemik atau disinsentif struktural.
3. **The Multi-Causal Fishbone Axiom (Kaoru Ishikawa)**: Masalah kompleks di dunia nyata jarang memiliki penyebab tunggal (*monocausal fallacy*). Diagram Ishikawa mewajibkan dekonstruksi masalah ke dalam enam dimensi independen (6M dalam industri: *Manpower, Machine, Method, Material, Measurement, Milieu/Environment*), sehingga investigasi tidak bias mencari kambing hitam pada kesalahan satu individu (*operator error*).
4. **The Stop Rule at Actionable Systems**: Penggalian 5-Whys harus dihentikan ketika Anda telah mencapai tingkat di mana: (a) Penyebab berada di dalam lingkup kendali sistem Anda (*within sphere of control*), dan (b) Solusi yang dirancang mampu mencegah masalah tersebut terulang kembali secara otomatis (*foolproof / Poka-Yoke*). Melanjutkan 5-Whys melampaui titik ini hingga menyalahkan "kondisi alam semesta" atau "takdir Tuhan" adalah kemalasan analitis.
5. **The Permanent Corrective Action (CAPA Protocol)**: Setiap analisis akar masalah wajib diakhiri dengan CAPA (*Corrective and Preventive Action*): mengubah prosedur operasional baku (SOP), mengubah arsitektur kode perangkat lunak, atau mengubah sistem insentif kompensasi. Jika penyelesaian masalah hanya berupa "nasihat agar karyawan lebih berhati-hati", maka akar masalah belum terselesaikan sama sekali.

---

### LAYER 2: MENTAL MODEL & DIAGRAM ASCII
```text
+-------------------------------------------------------------------------------+
|                       THE 5-WHYS ROOT CAUSE DRILL                             |
+-------------------------------------------------------------------------------+

   [GEJALA PERMUKAAN] : Server database aplikasi ambruk selama 4 jam!
            │
            ▼
   [MENGAPA 1?]       : Karena ruang disk penyimpanan server penuh (100% capacity).
            │
            ▼
   [MENGAPA 2?]       : Karena file log transaksi tidak pernah dihapus/diarsipkan otomatis.
            │
            ▼
   [MENGAPA 3?]       : Karena skrip otomatis log-rotation crash dan tidak berjalan.
            │
            ▼
   [MENGAPA 4?]       : Karena tidak ada sistem monitoring yang memantau kesehatan skrip log.
            │
            ▼
   [MENGAPA 5?]       : AKAR SISTEMIK: Standar deployment arsitektur tidak mewajibkan
   [ROOT CAUSE]         monitoring service sebagai prasyarat rilis ke server produksi.
                        (SOLUSI: Pasang Healthcheck Alert wajib di CI/CD pipeline)

+-------------------------------------------------------------------------------+
|                     ISHIKAWA FISHBONE DIAGRAM (THE 6M)                        |
+-------------------------------------------------------------------------------+

     MAN (MANUSIA)          MACHINE (MESIN)         METHOD (METODE)
            \                     \                     \
             \                     \                     \
    Kurang     Ganti Shift     Server     Sensor       SOP Tidak    Tidak Ada
    Pelatihan   Buru-buru      Jadul      Rusak        Ada          Checklist
          \         \              \         \           \          \
           ─────────────────────────────────────────────────────────────> [MASALAH:
           /         /              /         /            /         /   CACAT PRODUK
          /         /              /         /            /         /    TINGGI 12%]
    Bahan Baku  Kualitas      Alat Ukur  Salah        Suhu Udara  Ventilasi
    Substandar  Vendor Jelek  Kalibrasi  Metrik       Panas/Lembap Buruk
            /                     /                     /
    MATERIAL (BAHAN)       MEASUREMENT (UKURAN)     MILIEU (LINGKUNGAN)
```

---

### LAYER 3: SYARAH DAGING (DEEP DIVE 1-TO-1 SYMMETRY)

#### 1. Syarah Kaidah 1: The Symptom vs Pathology Demarcation
Ketika seorang pasien datang ke dokter mengeluh batuk berdahak darah, dokter yang bodoh akan meresepkan sirup pereda batuk untuk menghentikan refleks batuknya. Apa yang terjadi seminggu kemudian? Pasien tersebut pingsan karena paru-parunya hancur digerogoti bakteri *Mycobacterium tuberculosis*. Batuk hanyalah gejala permukaan (*symptom*); patologi aslinya adalah infeksi mikrobakteri (*pathology*).

Dalam manajemen organisasi dan bisnis, sebagian besar manajer beroperasi seperti dokter bodoh:
- Penjualan turun → langsung bikin promo diskon gila-gilaan (padahal masalah aslinya adalah kualitas produk yang buruk).
- Karyawan sering telat datang → langsung pasang mesin sidik jari dan ancaman denda (padahal masalah aslinya adalah budaya lembur larut malam tak terencana yang dipaksakan manajemen).
Merespons gejala hanya menghabiskan anggaran tanpa menyelesaikan masalah. Seorang pemikir master selalu menembus kabut gejala untuk menemukan sarang tumor di akarnya.

#### 2. Syarah Kaidah 2: The 5-Whys Iterative Drilling Invariant (Sakichi Toyoda)
Sakichi Toyoda, pendiri Toyota Industries, mengembangkan teknik *5-Whys* sebagai pilar utama *Toyota Production System* (TPS).
Kekuatan 5-Whys terletak pada kedisiplinannya menolak berhenti di lapisan pertama.
Ketika sebuah mesin robotik di pabrik perakitan mobil berhenti beroperasi:
- Mengapa mesin berhenti? Sekringnya putus karena beban berlebih (*overload*).
(Manajer medioker akan berhenti di sini: "Ganti sekringnya sekarang!". Dan besok sekringnya putus lagi!).
- Mengapa beban berlebih? Karena bearing poros tidak terlumasi oli dengan baik.
- Mengapa tidak terlumasi? Karena pompa sirkulasi oli tersumbat kotoran serbuk besi.
- Mengapa pompa tersumbat kotoran? Karena tidak ada filter saringan pada saluran masuk pompa.
- Mengapa tidak ada filter? **Karena spesifikasi desain awal pengadaan mesin tidak mewajibkan filter oli**.

Perhatikan: dari "sekring putus", akar masalah sesungguhnya bermuara pada "cacat klausul pengadaan mesin". Dengan menambahkan filter oli pada pengadaan mesin, mesin tidak akan pernah putus sekring lagi selama 20 tahun ke depan. Inilah kekuatan solusi permanen di tingkat sistem.

#### 3. Syarah Kaidah 3: The Multi-Causal Fishbone Axiom (Kaoru Ishikawa)
Ketika terjadi kesalahan fatal di sebuah rumah sakit (misalnya perawat salah memberikan dosis obat kepada pasien anak hingga koma), naluri pertama manajemen yang primitif adalah: "Pecat perawat itu! Dia lalai dan tidak becus!".
Ini adalah falasi kambing hitam (*scapegoating fallacy*).

Diagram Tulang Ikan Kaoru Ishikawa membongkar kompleksitas kecelakaan dengan membedah 6 cabang M:
1. **Man (Manusia)**: Perawat tersebut sedang menjalani shift ganda 18 jam nonstop karena ketiadaan staf pengganti (kelelahan kognitif ekstrem).
2. **Machine / Tool**: Label botol obat dicetak dengan font ukuran 6 yang sangat kecil dan pudar.
3. **Method**: Prosedur rumah sakit tidak mewajibkan verifikasi ganda (*double-check sign-off*) oleh dua tenaga medis independen sebelum injeksi disuntikkan.
4. **Material**: Botol obat bius mematikan dan botol vitamin anak memiliki warna tutup dan bentuk botol yang identik 95% dari pabrik vendor.
5. **Environment**: Ruang farmasi darurat saat itu gelap dan berisik oleh sirene ambulans.
Jika Anda memecat perawat tersebut dan merekrut perawat baru, perawat baru tersebut cepat atau lambat **akan melakukan kesalahan persis yang sama** karena seluruh sistem di sekitarnya dirancang untuk memicu kegagalan! Solusi sejati adalah merombak keenam cabang sistemik tersebut.

#### 4. Syarah Kaidah 4: The Stop Rule at Actionable Systems
Kapan Anda harus berhenti bertanya "Mengapa"?
Banyak pemula yang berfilsafat kebablasan:
- Mengapa spesifikasi pengadaan tidak ada filter? Karena staf procurement terburu-buru.
- Mengapa terburu-buru? Karena manusia punya sifat cemas.
- Mengapa cemas? Karena manusia terlempar ke bumi yang fana.
- Mengapa manusia eksis? Karena ledakan Big Bang 13.8 miliar tahun lalu!
Ini konyol. Anda tidak bisa merancang SOP untuk membatalkan Big Bang.

**Aturan Henti (Stop Rule)**:
Berhentilah tepat di simpul di mana Anda memiliki otoritas dan kapasitas teknis untuk merancang intervensi sistem yang dapat ditindaklanjuti (*actionable system*). Dalam contoh Toyota: Anda berhenti di perombakan spesifikasi pengadaan mesin dan penambahan checklist filter oli. Itu adalah titik henti yang sempurna.

#### 5. Syarah Kaidah 5: The Permanent Corrective Action (CAPA Protocol)
Dalam standar manajemen mutu internasional (ISO 9001 / FDA QSR), ada perbedaan tegas antara dua istilah:
- **Koreksi Langsung (Correction)**: Memadamkan api saat kebakaran (membersihkan tumpahan oli di lantai pabrik).
- **Tindakan Korektif & Preventif (CAPA)**: Merombak pipa oli agar oli tidak pernah bocor ke lantai lagi seumur hidup pabrik.

Jika tindak lanjut dari investigasi insiden di kantor Anda hanya berupa kalimat normatif: "Karyawan telah diberi teguran lisan dan diimbau agar lebih teliti di masa depan", itu tandanya analisis akar masalah Anda gagal total. Manusia secara biologis tidak bisa dipaksa "selalu teliti 100%" setiap detik. Anda harus merancang sistem yang kebal terhadap kelalaian manusia (*Poka-Yoke / Foolproofing*): misalnya soket kabel yang bentuknya asimetris sehingga mustahil dicolokkan terbalik bahkan oleh orang yang mengantuk sekalipun.

---

### LAYER 4: FIELD PLAYBOOK (TACTICAL SOP & CODE)

#### SOP Fasilitasi Sesi RCA & 5-Whys Tim
1. **Langkah 1: Perumusan Rumusan Masalah Spesifik (Problem Statement)**
   - Wajib memuat: Apa yang terjadi, Kapan, Di mana, Seberapa besar deviasi dari standar (Gunakan angka terukur). Dilarang memasukkan spekulasi penyebab di judul masalah.
2. **Langkah 2: Sesi Brainstorming Ishikawa 6M**
   - Buat diagram tulang ikan di papan tulis. Tim mengisi post-it note pada 6 cabang: Man, Machine, Method, Material, Measurement, Milieu.
3. **Langkah 3: Jalankan 5-Whys Vertikal pada Cabang Paling Kritis**
   - Uji setiap tingkat dengan verifikasi empiris: "Dapatkah kita membuktikan di lapangan bahwa faktor X benar-benar memicu faktor Y?". Jika hanya dugaan, lakukan tes fisik.
4. **Langkah 4: Tetapkan Solusi CAPA Bertingkat Poka-Yoke**
   - Prioritas 1: Eliminasi fisik (membuat kesalahan mustahil terjadi secara arsitektur).
   - Prioritas 2: Otomasi deteksi (sistem alarm otomatis mematikan mesin jika ada anomali).
   - Prioritas 3: Revisi SOP dan checklist verifikasi silang ganda.

#### Script Python: 5-Whys Recursive Tree Logger & Verifier
```python
# rca_tree.py
class FiveWhysInvestigator:
    def __init__(self, problem_statement):
        self.problem = problem_statement
        self.chain = []

    def add_why(self, level, cause, evidence):
        self.chain.append({
            "level": level,
            "cause": cause,
            "evidence": evidence
        })

    def print_report(self):
        print(f"=== LAPORAN INVESTIGASI ROOT CAUSE ANALYSIS (5-WHYS) ===")
        print(f"RUMUSAN MASALAH: {self.problem}
")
        for step in self.chain:
            indent = "  " * step["level"]
            print(f"{indent}[WHY LEVEL {step['level']}]: {step['cause']}")
            print(f"{indent} └── BUKTI EMPIRIS: {step['evidence']}")
        
        root = self.chain[-1]
        print(f"
AKAR MASALAH SISTEMIK (ROOT CAUSE): {root['cause']}")
        print(f"STATUS AKSI: Rancang intervensi Poka-Yoke permanen pada level ini.")

if __name__ == "__main__":
    rca = FiveWhysInvestigator("Tagihan Listrik Pabrik Membengkak Rp 80 Juta Melebihi Anggaran")
    rca.add_why(1, "Kompresor pendingin utama bekerja nonstop 24 jam dengan beban 100%", "Data log meteran listrik sub-panel")
    rca.add_why(2, "Sensor termostat ruang penyimpanan dingin membaca suhu 18°C terus-menerus", "Pemeriksaan fisik sensor oleh teknisi")
    rca.add_why(3, "Sensor termostat tertutup kerak es tebal sehingga terisolasi dari suhu ruangan", "Foto dokumentasi visual sensor")
    rca.add_why(4, "Kipas pemanas defrost otomatis pada sensor terbakar dan mati", "Uji multitester kelistrikan koil defrost")
    rca.add_why(5, "Jadwal pemeliharaan preventif bulanan ditiadakan demi efisiensi biaya vendor", "Notulen rapat manajemen kuartal lalu")
    rca.print_report()
```

---

### LAYER 5: DIAGNOSTIC DRILL (STUDI KASUS & UJI MANDIRI)

#### Skenario Kasus Lapangan
Sebuah platform aplikasi pesan-antar makanan (*food delivery*) mengalami krisis reputasi: dalam seminggu terakhir, tingkat pembatalan pesanan (*order cancellation rate*) melonjak drastis dari 2% menjadi 14%. Ratusan pelanggan mengamuk di media sosial karena makanan mereka tidak kunjung dijemput oleh pengemudi ojek online.
Manajer Operasional yang panik segera memanggil seluruh serikat pengemudi dan mengeluarkan surat peringatan:
> "Mulai besok, pengemudi mana pun yang menolak atau membatalkan orderan makanan akan langsung dibekukan akunnya (*suspend*) dan didenda Rp 100.000! Kalian pengemudi harus disiplin dan jangan malas!".  
> Hasilnya: bukannya membaik, 2.000 pengemudi justru mogok massal, mematikan aplikasi secara serempak, dan aplikasi mengalami kerugian transaksi Rp 3 miliar dalam sehari.

#### Pertanyaan Uji Nalar
1. Mengapa tindakan Manajer Operasional merupakan contoh klasik penanganan gejala permukaan yang memperburuk masalah (*treating symptoms, triggering backlash*)?
2. Jalankan simulasi analisis **5-Whys** untuk menelusuri akar masalah riil di balik fenomena penolakan orderan makanan oleh pengemudi!
3. Susun diagram rekomendasi solusi struktural jangka panjang berbasis perombakan sistem insentif yang memecahkan masalah tanpa perlu ancaman denda!

#### Kunci Jawaban & Bedah Anti-Patterns
1. **Analisis Kegagalan Manajer Operasional:**
   - Manajer menyerang gejala permukaan ("pengemudi menolak order") dengan instrumen hukuman agresif (*suspend & denda*). Ia berasumsi pengemudi berbuat jahat karena "malas" (*Fundamental Attribution Error / Scapegoating*), tanpa menelusuri **mengapa** pengemudi rasional menolak orderan tersebut. Kebijakan hukuman sepihak memicu kemarahan kolektif dan mogok massal yang melumpuhkan ekosistem bisnis.
2. **Simulasi Rantai 5-Whys Vertikal:**
   - **Gejala:** Pengemudi menolak/membatalkan orderan makanan.
   - **Why 1:** Mengapa pengemudi menolak order makanan? Karena mereka harus mengantre lama di resto selama 45-60 menit tanpa kompensasi waktu.
   - **Why 2:** Mengapa pengemudi mengantre 45-60 menit? Karena restoran baru mulai memasak makanan SETELAH pengemudi tiba di resto fisik.
   - **Why 3:** Mengapa resto baru memasak saat pengemudi tiba? Karena resto takut rugi jika makanan sudah dimasak tapi pesanan dibatalkan pembeli (*ghost cancellation*), atau makanan menjadi dingin karena pengemudi terjebak macet.
   - **Why 4:** Mengapa aplikasi memanggil pengemudi bersamaan dengan masuknya tiket ke dapur resto? Karena algoritma dispatcher lama mengasumsikan waktu persiapan makanan sama dengan 0 menit untuk seluruh jenis makanan (baik burger cepat saji maupun bebek panggang yang butuh 40 menit).
   - **Why 5 (Root Cause):** **Arsitektur algoritma dispatching tidak memiliki metrik estimasi waktu masak dinamis (*Dynamic Kitchen Prep Time*) yang menahan pemanggilan kurir hingga makanan 80% siap saji.**
3. **Rekomendasi Solusi Sistemik Standar Emas:**
   - **Solusi Algoritma (Poka-Yoke Dispatcher):** Pasang model machine learning prediksi waktu masak di aplikasi resto. Sistem baru memanggil pengemudi ojek online 5 menit sebelum pesanan diperkirakan selesai dimasak. Pengemudi tiba di resto tepat saat makanan dibungkus (waktu tunggu pangkas dari 50 menit menjadi 3 menit).
   - **Solusi Insentif Finansial:** Berikan uang tunggu (*wait-time fee*) otomatis Rp 1.000 per 5 menit jika resto mengalami keterlambatan masak, yang dibebankan sebagian ke resto yang lalai. Pengemudi senang karena waktu mereka dihargai, pelanggan senang makanan tiba panas dan cepat, dan tingkat pembatalan order seketika anjlok di bawah 1%.
