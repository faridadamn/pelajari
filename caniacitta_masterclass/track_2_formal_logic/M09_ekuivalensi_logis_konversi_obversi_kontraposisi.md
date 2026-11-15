# Track 2: Logika Formal & Silogisme Penalaran
## Modul 09: Ekuivalensi Logis: Konversi, Obversi, Kontraposisi & Hukum De Morgan
> **Referensi Transkrip Primer:** `007 - Meta Thinking Tips Structured Thinking and Argumentation.md`, `010 - Discussing Problem Solving and Cania’s Pregnancy Program.md`  
> **Target Kompetensi:** Menguasai operasi transformasi proposisi kategoris (Konversi, Obversi, Kontraposisi), memverifikasi ekuivalensi semantik tanpa merusak nilai kebenaran, membongkar ilusi kontraposisi palsu, dan mengeksekusi Hukum De Morgan pada negasi disjungtif dan konjungtif.

---

### LAYER 1: KAIDAH EMAS (CORE AXIOMS)
1. **The Invariant of Truth-Value Preservation**: Dua proposisi dikatakan ekuivalen secara logis (P ≡ Q) jika dan hanya jika keduanya memiliki tabel kebenaran yang identik di setiap kemungkinan dunia semesta. Operasi transformasi bentuk hanya sah jika dan hanya jika tidak menambahkan atau membuang informasi semantik dari proposisi asal.
2. **The Limits of Conversion (Perputaran Subjek-Predikat)**: 
   - Proposisi Universal Negatif (E: "Tidak ada S yang merupakan P") dan Partikular Afirmatif (I: "Sebagian S adalah P") dapat dikonversi secara langsung dan sah (S ↔ P).
   - Proposisi Universal Afirmatif (A: "Semua S adalah P") TIDAK DAPAT dikonversi secara langsung menjadi "Semua P adalah S". Konversi A hanya sah melalui pembatasan aksidental (*conversion per accidens*) menjadi "Sebagian P adalah S". Mengklaim "Semua S adalah P ekuivalen dengan Semua P adalah S" adalah kesesatan *Illicit Conversion*.
3. **The Universal Legality of Obversion**: Semua jenis proposisi kategoris (A, E, I, O) dapat diobservi secara sah dengan mengubah kualitas proposisi (afirmatif menjadi negatif, atau sebaliknya) dan menegasikan term predikatnya (P menjadi non-P). Proposisi "Semua S adalah P" secara eksak ekuivalen dengan "Tidak ada S yang merupakan non-P".
4. **The Law of Contraposition**: Kontraposisi (menukar posisi subjek dan predikat sekaligus menegasikan keduanya: S → P ≡ ¬ P → ¬ S) berlaku sah mutlak untuk Proposisi Universal Afirmatif (A) dan Partikular Negatif (O). Kontraposisi TIDAK SAH untuk Proposisi Universal Negatif (E).
5. **De Morgan’s Duality Theorems**: 
   - Negasi dari konjungsi adalah disjungsi dari masing-masing negasi: ¬ (P ∧ Q) ≡ ¬ P ∨ ¬ Q. ("Bukan keduanya" berarti "salah satu tidak, atau keduanya tidak").
   - Negasi dari disjungsi adalah konjungsi dari masing-masing negasi: ¬ (P ∨ Q) ≡ ¬ P ∧ ¬ Q. ("Tidak satu pun dari keduanya" berarti "P tidak dan Q tidak").

---

### LAYER 2: MENTAL MODEL & DIAGRAM ASCII
```text
+-------------------------------------------------------------------------------+
|                    TRANSFORMATION VALIDITY MATRIX                             |
+-------------------------------------------------------------------------------+

  BENTUK PROPOSISI              KONVERSI          OBVERSI         KONTRAPOSISI
  ─────────────────────────────────────────────────────────────────────────────
  A: Semua S adalah P           INVALID*         VALID            VALID
     (Kecuali per accidens)     (Beberapa P..S)  (Tak ada S..non-P)(Semua non-P..non-S)
  
  E: Tidak ada S yang P         VALID            VALID            INVALID
                                (Tak ada P..S)   (Semua S..non-P)
  
  I: Sebagian S adalah P        VALID            VALID            INVALID
                                (Sebagian P..S)  (Sebagian S..bukan non-P)
  
  O: Sebagian S bukan P         INVALID          VALID            VALID
                                                 (Sebagian S..non-P)(Sebagian non-P..bukan non-S)

+-------------------------------------------------------------------------------+
|                        DE MORGAN'S LOGICAL GEARS                              |
+-------------------------------------------------------------------------------+

   NEGASI DARI KONJUNGSI:
   ¬( P  ∧  Q )   <═══════════════════ EKUIVALEN ══════════════════>   ¬P  ∨  ¬Q
   "Bukan [Kaya DAN Bahagia]"                                           "Tidak Kaya ATAU Tidak Bahagia"

   NEGASI DARI DISJUNGSI:
   ¬( P  ∨  Q )   <═══════════════════ EKUIVALEN ══════════════════>   ¬P  ∧  ¬Q
   "Bukan [Hujan ATAU Banjir]"                                          "Tidak Hujan DAN Tidak Banjir"
```

---

### LAYER 3: SYARAH DAGING (DEEP DIVE 1-TO-1 SYMMETRY)

#### 1. Syarah Kaidah 1: The Invariant of Truth-Value Preservation
Ekuivalensi logis adalah fondasi parafrase analitis. Jika Anda menulis esai ilmiah atau menyusun klausul kontrak hukum, Anda sering harus menyajikan proposisi dalam bentuk kalimat yang berbeda agar mudah dipahami publik tanpa mengubah nilai kebenarannya sedikit pun. Dua formula P dan Q ekuivalen hanya jika di bawah kondisi input apa pun, output kebenarannya selalu persis sama. Jika ada satu skenario hipotetis di mana P bernilai Benar sementara Q bernilai Salah, maka P dan Q BUKAN ekuivalen.

#### 2. Syarah Kaidah 2: The Limits of Conversion
Konversi adalah operasi menukar posisi subjek dengan predikat (S menjadi P, P menjadi S).
- Sah pada kalimat E: "Tidak ada ikan yang merupakan mamalia" ≡ "Tidak ada mamalia yang merupakan ikan". Kedua himpunan saling asing sepenuhnya (*mutually exclusive*).
- Sah pada kalimat I: "Sebagian politisi adalah penulis" ≡ "Sebagian penulis adalah politisi". Daerah irisan kedua himpunan simetris.
- **HARAM pada kalimat A**: "Semua dokter adalah manusia" TIDAK EKUIVALEN dengan "Semua manusia adalah dokter". Melakukan konversi langsung pada proposisi A adalah kesalahan berpikir amatir yang disebut *Illicit Conversion*. Konversi hanya sah jika dibatasi skalanya menjadi partikular: "Sebagian manusia adalah dokter".

#### 3. Syarah Kaidah 3: The Universal Legality of Obversion
Obversi bekerja dengan prinsip negasi ganda: mengubah kualitas kalimat afirmatif menjadi negatif (atau sebaliknya), lalu mengganti predikat dengan komplemennya. Obversi berlaku universal tanpa pengecualian untuk semua bentuk proposisi:
- Proposisi A: "Semua warga negara wajib taat hukum" ≡ "Tidak ada warga negara yang kebal hukum (bebas dari kewajiban taat hukum)".
- Proposisi E: "Tidak ada koruptor yang bermoral" ≡ "Semua koruptor adalah orang tak bermoral".
- Proposisi I: "Sebagian pejabat publik jujur" ≡ "Sebagian pejabat publik bukan orang tidak jujur".
- Proposisi O: "Sebagian pegawai tidak kompeten" ≡ "Sebagian pegawai adalah orang non-kompeten".

Penguasaan obversi memungkinkan Anda menguji apakah retorika seorang politisi yang menggunakan kalimat eufimisme sebenarnya hanya membungkus hal yang sama dengan istilah komplemen.

#### 4. Syarah Kaidah 4: The Law of Contraposition
Kontraposisi adalah kombinasi dari obversi, konversi, lalu obversi kembali: tukar posisi subjek dan predikat, lalu beri negasi pada keduanya.
- Berlaku sah pada Proposisi A:
  "Jika sesuatu adalah emas (S), maka ia berkilau (P)" ≡ "Jika sesuatu tidak berkilau (¬ P), maka ia pasti bukan emas (¬ S)".
  Ini adalah alat deduktif yang luar biasa tajam. Jika Anda ingin membuktikan seseorang bukan ilmuwan sejati (S), buktikan dia menolak metode empiris (¬ P).
- **Gagal pada Proposisi E**:
  "Tidak ada kucing yang merupakan anjing". Jika dikontraposisikan: "Tidak ada non-anjing yang merupakan non-kucing". Ini jelas salah; burung adalah non-anjing, namun burung adalah non-kucing (sehingga ada non-anjing yang merupakan non-kucing).

#### 5. Syarah Kaidah 5: De Morgan’s Duality Theorems
Augustus De Morgan merumuskan hukum interaksi fundamental antara negasi, operator "DAN" (∧), dan operator "ATAU" (∨).

Banyak orang gagal ketika menegasikan pernyataan majemuk:
Misal ada aturan: "Untuk mendapatkan promosi, pegawai harus berkinerja tinggi (P) DAN memiliki integritas etis (Q)".
Bagaimana negasinya?
Banyak orang salah mengira negasinya adalah: "Pegawai tidak berkinerja tinggi DAN tidak berintegritas". Ini keliru.
Menurut Hukum De Morgan: ¬ (P ∧ Q) ≡ ¬ P ∨ ¬ Q.
Artinya, seseorang batal mendapatkan promosi cukup dengan SALAH SATU kegagalan: kinerjanya jeblok, ATAU integritasnya cacat, atau kedua-duanya. 

Sebaliknya:
"Restoran ini dilarang menyajikan minuman keras (P) ATAU obat terlarang (Q)".
Negasinya: ¬ (P ∨ Q) ≡ ¬ P ∧ ¬ Q. Restoran beroperasi sah jika dan hanya jika TIDAK menyajikan miras DAN TIDAK menyajikan narkoba.

---

### LAYER 4: FIELD PLAYBOOK (TACTICAL SOP & CODE)

#### SOP Validasi Ekuivalensi Bahasa Hukum & Argumen
1. **Langkah 1: Dekonstruksi Proposisi ke Bentuk Standar**
   - Tetapkan Subjek (S), Predikat (P), Kualitas (Afirmatif/Negatif), dan Kuantitas (Universal/Partikular).
2. **Langkah 2: Terapkan Filter Transformasi**
   - Jika lawan membalik subjek dan predikat: periksa apakah jenis kalimatnya A? Jika A dibalik langsung menjadi A, flag *Illicit Conversion*.
   - Jika lawan membentuk argumen kontraposisi: periksa apakah anteseden dan konsekuen sama-sama dinegasikan?
3. **Langkah 3: Jalankan De Morgan Resolver untuk Kalimat Majemuk**
   - Distribusikan tanda negasi ke setiap komponen, lalu balik operator ∧ menjadi ∨, atau ∨ menjadi ∧.

#### Script Python: De Morgan & Equivalence Engine
```python
# demorgan_engine.py
def demorgan_not_and(p_val, q_val):
    """¬(P ∧ Q) <==> ¬P ∨ ¬Q"""
    lhs = not (p_val and q_val)
    rhs = (not p_val) or (not q_val)
    return lhs == rhs, lhs

def demorgan_not_or(p_val, q_val):
    """¬(P ∨ Q) <==> ¬P ∧ ¬Q"""
    lhs = not (p_val or q_val)
    rhs = (not p_val) and (not q_val)
    return lhs == rhs, lhs

def contraposition_check(p_implies_q_str):
    """Menghasilkan bentuk kontraposisi baku dari 'Jika P maka Q'"""
    # format input: 'Jika P, maka Q'
    parts = p_implies_q_str.replace("Jika ", "").split(", maka ")
    p, q = parts[0], parts[1]
    return f"Jika bukan ({q}), maka bukan ({p})"

if __name__ == "__main__":
    # Verifikasi seluruh tabel kebenaran De Morgan
    all_pass = True
    for p in [True, False]:
        for q in [True, False]:
            valid_and, res_and = demorgan_not_and(p, q)
            valid_or, res_or = demorgan_not_or(p, q)
            if not (valid_and and valid_or):
                all_pass = False
    print("De Morgan Verification across all worlds:", "100% SOUND" if all_pass else "FAIL")
    
    # Test kontraposisi
    arg = "Jika seseorang dokter berlisensi, maka dia memahami anatomi tubuh manusia"
    print("Asli:", arg)
    print("Kontraposisi Ekuivalen:", contraposition_check(arg))
```

---

### LAYER 5: DIAGNOSTIC DRILL (STUDI KASUS & UJI MANDIRI)

#### Skenario Kasus Lapangan
Dalam perdebatan di rapat komite etik universitas, seorang anggota komite mengkritik kebijakan beasiswa luar negeri:
> "Peraturan rektor menyatakan: 'Semua penerima beasiswa prestasi adalah mahasiswa yang memiliki skor TOEFL di atas 600'. Berdasarkan aturan tersebut, jelas bahwa mahasiswa yang memiliki skor TOEFL di atas 600 pastilah mahasiswa penerima beasiswa prestasi. Karena itu, jika ada mahasiswa dengan skor TOEFL 610 yang tidak menerima beasiswa, rektor telah melanggar peraturannya sendiri!"

#### Pertanyaan Uji Nalar
1. Operasi transformasi apa yang dilakukan oleh anggota komite terhadap peraturan rektor?
2. Apakah transformasi tersebut sah secara logika formal? Identifikasi nama kekeliruan transformasinya!
3. Bagaimana bunyi proposisi kontraposisi yang sah dari peraturan rektor tersebut?

#### Kunci Jawaban & Bedah Anti-Patterns
1. **Identifikasi Operasi:**
   - Anggota komite melakukan operasi **Konversi** (*Conversion*): menukar posisi subjek ("penerima beasiswa prestasi") dengan predikat ("mahasiswa dengan TOEFL di atas 600").
2. **Evaluasi Keabsahan:**
   - Transformasi tersebut **TIDAK SAH (INVALID)**.
   - Nama Kesesatan: **Fallacy of Illicit Conversion (Konversi Ilegal Proposisi A)**.
   - Analisis: Pernyataan "Semua A adalah B" tidak berarti "Semua B adalah A". Memiliki skor TOEFL > 600 hanyalah syarat perlu (*necessary condition*), bukan syarat cukup tunggal yang otomatis menjadikan seseorang penerima beasiswa (ada kuota anggaran, tes wawancara, IPK, dll.). Menuntut universitas memberi beasiswa kepada seluruh pemilik TOEFL 600 adalah kebodohan logika formal.
3. **Bentuk Kontraposisi yang Sah:**
   - Kontraposisi dari Proposisi A adalah sah mutlak: "Setiap mahasiswa yang TIDAK memiliki skor TOEFL di atas 600 dipastikan BUKAN penerima beasiswa prestasi" (¬ P → ¬ S). Ini adalah satu-satunya bentuk inferensi ekuivalen yang sah ditarik dari peraturan rektor tersebut.
