# Track 2: Logika Formal & Silogisme Penalaran
## Modul 07: Logika Proposisional, Implikasi, Modus Ponens & Modus Tollens
> **Referensi Transkrip Primer:** `007 - Meta Thinking Tips Structured Thinking and Argumentation.md`, `001 - Thinking Smart in a Stupid Environment.md`  
> **Target Kompetensi:** Menguasai kalkulus proposisi, membedakan implikasi material kondisional (P → Q) dengan bikondisional (P ↔ Q), mengeksekusi Modus Ponens dan Modus Tollens dengan presisi, serta membongkar jebakan Affirming the Consequent dan Denying the Antecedent.

---

### LAYER 1: KAIDAH EMAS (CORE AXIOMS)
1. **The Asymmetry of Conditional Implication (P → Q)**: Pernyataan kondisional "Jika P maka Q" hanya menyatakan bahwa kehadiran anteseden (P) adalah kondisi cukup (*sufficient condition*) bagi konsekuen (Q), dan kehadiran Q adalah kondisi perlu (*necessary condition*) bagi P. Implikasi tidak berarti Q menyebabkan P, juga tidak berarti bahwa jika P tidak terjadi maka Q mustahil terjadi.
2. **The Modus Ponens Iron Rule (Affirming the Antecedent)**: Diberikan proposisi implikasi P → Q, jika dan hanya jika anteseden P ditegaskan benar, maka kesimpulan bahwa Q benar adalah keniscayaan logis yang tak terbantahkan. Bentuk valid: [(P → Q) ∧ P] ⊢ Q.
3. **The Modus Tollens Iron Rule (Denying the Consequent)**: Diberikan proposisi implikasi P → Q, jika dan hanya jika konsekuen Q disangkal (terbukti salah, ¬ Q), maka kesimpulan bahwa anteseden P salah (¬ P) adalah keniscayaan logis mutlak. Bentuk valid: [(P → Q) ∧ ¬ Q] ⊢ ¬ P.
4. **The Fallacy of Affirming the Consequent**: Menegaskan kebenaran konsekuen Q TIDAK PERNAH membuktikan bahwa anteseden P benar. Bentuk cacat: [(P → Q) ∧ Q] ⊢ P adalah kesesatan formal (*formal fallacy*), karena Q dapat dihasilkan oleh banyak faktor lain selain P.
5. **The Fallacy of Denying the Antecedent**: Menyangkal anteseden P TIDAK PERNAH membuktikan bahwa konsekuen Q salah. Bentuk cacat: [(P → Q) ∧ ¬ P] ⊢ ¬ Q adalah kesesatan formal, karena ketiadaan P tidak menutup pintu bagi terwujudnya Q lewat jalur independen lainnya.

---

### LAYER 2: MENTAL MODEL & DIAGRAM ASCII
```text
+-------------------------------------------------------------------------------+
|                       TRUTH TABLE: IMPLIKASI MATERIAL (P -> Q)               |
+-------------------------------------------------------------------------------+

   P (Anteseden) │ Q (Konsekuen) │ P -> Q │ Catatan Evaluasi Logis
  ───────────────┼───────────────┼────────┼─────────────────────────────────────
         B       │       B       │   B    │ Janji terpenuhi secara sempurna
         B       │       S       │   S    │ SATU-SATUNYA KONDISI IMPLIKASI PALSU
         S       │       B       │   B    │ Vacuous Truth (Anteseden tidak terjadi)
         S       │       S       │   B    │ Vacuous Truth (Tidak ada janji dilanggar)

+-------------------------------------------------------------------------------+
|                      INFERENCE MATRIX: VALID VS INVALID                       |
+-------------------------------------------------------------------------------+

                  [OPERASI PADA ANTESEDEN (P)]   [OPERASI PADA KONSEKUEN (Q)]
                 ┌─────────────────────────────┬─────────────────────────────┐
   PENEGASAN (+) │        MODUS PONENS         │   AFFIRMING THE CONSEQUENT  │
                 │   P -> Q                    │   P -> Q                    │
                 │   P                         │   Q                         │
                 │   ∴ Q                       │   ∴ P                       │
                 │   STATUS: [ 100% VALID ]    │   STATUS: [ SESAT PIKIR! ]  │
                 ├─────────────────────────────┼─────────────────────────────┤
   PENYANGKALAN  │    DENYING THE ANTECEDENT   │        MODUS TOLLENS        │
       (-)       │   P -> Q                    │   P -> Q                    │
                 │   ¬P                        │   ¬Q                        │
                 │   ∴ ¬Q                      │   ∴ ¬P                      │
                 │   STATUS: [ SESAT PIKIR! ]  │   STATUS: [ 100% VALID ]    │
                 └─────────────────────────────┴─────────────────────────────┘
```

---

### LAYER 3: SYARAH DAGING (DEEP DIVE 1-TO-1 SYMMETRY)

#### 1. Syarah Kaidah 1: The Asymmetry of Conditional Implication
Banyak perdebatan kusut karena orang memperlakukan kalimat kondisional "Jika P maka Q" sebagai kalimat identitas dua arah "P sama dengan Q". Implikasi material adalah relasi satu arah:
- P adalah **Sufficient Condition** (Syarat Cukup): Begitu P terjadi, terjadinya Q sudah dijamin 100%.
- Q adalah **Necessary Condition** (Syarat Perlu): Tanpa kehadiran Q, P mustahil bisa eksis.

Contoh konkret: "Jika hujan turun lebat (P), maka aspal jalanan basah (Q)".
Hujan turun adalah syarat cukup untuk membuat jalanan basah. Tetapi aspal jalan basah adalah syarat perlu bagi hipotesis bahwa baru saja turun hujan lebat tanpa pelindung. Implikasi ini sama sekali tidak menyatakan bahwa satu-satunya penyebab jalan basah adalah hujan. Seseorang bisa menyiram jalanan dengan mobil pemadam kebakaran.

#### 2. Syarah Kaidah 2: The Modus Ponens Iron Rule (Affirming the Antecedent)
Modus Ponens adalah metode penegasan fundamental dalam logika deduktif (*the mode of putting*). Mekanismenya sangat elegan dan linier:
- Premis 1 (Aturan): Jika sebuah negara mengalami hiperinflasi di atas 50% per bulan (P), maka daya beli mata uang domestiknya hancur (Q).
- Premis 2 (Fakta Anteseden): Negara Z mengalami inflasi 75% per bulan (P).
- Kesimpulan: Daya beli mata uang Negara Z hancur (Q).

Jika Premis 1 disepakati dan Premis 2 terbukti faktual, kesimpulan Q mutlak benar. Menolak Q sementara menerima P1 dan P2 adalah kontradiksi logis murni.

#### 3. Syarah Kaidah 3: The Modus Tollens Iron Rule (Denying the Consequent)
Modus Tollens adalah metode penyangkalan konsekuen (*the mode of taking away*). Ini adalah instrumen epistemik terkuat dalam metode sains (falsifikasi Popperian):
- Premis 1: Jika teori gravitasi graviton benar (P), maka detektor radiasi kuantum akan menangkap partikel spin-2 pada frekuensi X (Q).
- Premis 2: Detektor radiasi kuantum tidak menemukan partikel spin-2 pada frekuensi X (¬ Q).
- Kesimpulan: Teori gravitasi graviton salah atau perlu modifikasi mendasar (¬ P).

Kekuatan Modus Tollens terletak pada ketidakmungkinannya dikompromikan: karena konsekuen Q adalah syarat perlu bagi kebenaran P, maka hilangnya Q secara otomatis mencabut keabsahan P.

#### 4. Syarah Kaidah 4: The Fallacy of Affirming the Consequent
Ini adalah salah satu sesat pikir formal paling mewabah dalam dunia investigasi, kedokteran amatir, dan perdebatan politik. Orang melihat akibat (konsekuen), lalu secara gegabah menyimpulkan sebab tunggal tertentu.

Contoh:
- Premis 1: Jika seseorang terkena demam berdarah (P), maka suhu badannya akan panas tinggi (Q).
- Premis 2: Pasien Budi badannya panas tinggi (Q).
- Kesimpulan: Budi pasti terkena demam berdarah (P). (SESAT PIKIR!)

Budi bisa saja mengalami demam tifoid, radang tenggorokan, infeksi saluran kemih, atau heatstroke. Mengonfirmasi konsekuen (Q) tidak pernah cukup untuk membuktikan anteseden (P). Yang terjadi hanyalah kompatibilitas, bukan keniscayaan bukti.

#### 5. Syarah Kaidah 5: The Fallacy of Denying the Antecedent
Kesesatan ini terjadi ketika seseorang menyangka bahwa dengan menghilangkan pemicu spesifik P, akibat Q tidak akan terjadi sama sekali.

Contoh:
- Premis 1: Jika kamu lulusan universitas Ivy League (P), kamu akan sukses berkarier finansial (Q).
- Premis 2: Doni bukan lulusan universitas Ivy League (¬ P).
- Kesimpulan: Doni tidak akan sukses berkarier finansial (¬ Q). (SESAT PIKIR!)

Doni bisa saja membangun perusahaan teknologi rintisan yang mendisrupsi pasar, mewarisi portofolio bisnis keluarga, atau menguasai keterampilan teknis langka secara otodidak. Ketiadaan anteseden P tidak membatalkan potensi munculnya konsekuen Q melalui determinan lain.

---

### LAYER 4: FIELD PLAYBOOK (TACTICAL SOP & CODE)

#### SOP Diagnostik Proposisi Kondisional
1. **Langkah 1: Normalisasi Kalimat Menjadi Notasi Baku**
   - Petakan kalimat diskursus ke bentuk "P → Q". Waspadai jebakan kata:
     - "P hanya jika Q" artinya P → Q.
     - "P syarat perlu bagi Q" artinya Q → P.
     - "P syarat cukup bagi Q" artinya P → Q.
2. **Langkah 2: Periksa Elemen Penentu**
   - Apakah premis kedua menegaskan anteseden? Jika ya → **Modus Ponens (Valid)**.
   - Apakah premis kedua menyangkal konsekuen? Jika ya → **Modus Tollens (Valid)**.
   - Apakah premis kedua menegaskan konsekuen? Jika ya → **Affirming Consequent (Sesat Pikir)**.
   - Apakah premis kedua menyangkal anteseden? Jika ya → **Denying Antecedent (Sesat Pikir)**.

#### Evaluator Logika Proposisional Python
```python
# propositional_logic.py
def evaluate_conditional_argument(rule_p_implies_q, second_premise, target_conclusion):
    """
    rule_p_implies_q: tuple ('P', 'Q')
    second_premise: str, misal 'P', 'not_P', 'Q', 'not_Q'
    target_conclusion: str, misal 'Q', 'not_Q', 'P', 'not_P'
    """
    p, q = rule_p_implies_q
    
    if second_premise == p and target_conclusion == q:
        return "VALID", "Modus Ponens (Affirming the Antecedent)"
    elif second_premise == f"not_{q}" and target_conclusion == f"not_{p}":
        return "VALID", "Modus Tollens (Denying the Consequent)"
    elif second_premise == q and target_conclusion == p:
        return "INVALID", "Fallacy of Affirming the Consequent"
    elif second_premise == f"not_{p}" and target_conclusion == f"not_{q}":
        return "INVALID", "Fallacy of Denying the Antecedent"
    else:
        return "INVALID", "Non-Sequitur / Tidak sesuai kaidah inferensi baku"

if __name__ == "__main__":
    p_q = ('hujan', 'basah')
    print("Test 1:", evaluate_conditional_argument(p_q, 'hujan', 'basah'))
    print("Test 2:", evaluate_conditional_argument(p_q, 'not_basah', 'not_hujan'))
    print("Test 3:", evaluate_conditional_argument(p_q, 'basah', 'hujan'))
    print("Test 4:", evaluate_conditional_argument(p_q, 'not_hujan', 'not_basah'))
```

---

### LAYER 5: DIAGNOSTIC DRILL (STUDI KASUS & UJI MANDIRI)

#### Skenario Kasus Lapangan
Sebuah dewan direksi perusahaan teknologi berdebat mengenai penyebab penurunan retensi pengguna:
> CTO: "Jika arsitektur server kita mengalami latensi di atas 2 detik (P), maka tingkat churn pengguna harian kita akan melonjak melebihi 15% (Q)."  
> VP Product: "Buktinya minggu ini data churn melonjak mencapai 18% (Q). Berarti sudah pasti arsitektur server kita sedang hancur dan mengalami latensi tinggi (P). Seluruh anggaran harus kita alihkan ke infrastruktur server!"  
> Head of Marketing menyela: "Tapi latensi server rata-rata kita minggu ini hanya 120 milidetik, sangat kencang (¬ P). Jadi churn pengguna kita pasti tidak melonjak (¬ Q), data kamu yang salah!"

#### Pertanyaan Uji Nalar
1. Bedah argumen VP Product menggunakan kalkulus proposisional: apakah bentuk penalarannya valid? Sebutkan nama falasinya jika ada!
2. Bedah argumen Head of Marketing: apakah bentuk penalarannya valid? Sebutkan nama falasinya jika ada!
3. Bagaimana rekonstruksi investigasi yang benar secara logika formal untuk menguji penurunan retensi tersebut?

#### Kunci Jawaban & Bedah Anti-Patterns
1. **Analisis Argumen VP Product:**
   - Bentuk argumen: Premis 1: P → Q. Premis 2: Q. Kesimpulan: P.
   - Status: **INVALID**.
   - Cacat: **Fallacy of Affirming the Consequent**. Churn melonjak bisa diakibatkan perubahan kebijakan harga, peluncuran fitur yang membingungkan (*bad UX*), promosi kompetitor, atau libur musiman. Mengonfirmasi konsekuen tidak membuktikan server sebagai biang keladi.
2. **Analisis Argumen Head of Marketing:**
   - Bentuk argumen: Premis 1: P → Q. Premis 2: ¬ P. Kesimpulan: ¬ Q.
   - Status: **INVALID**.
   - Cacat: **Fallacy of Denying the Antecedent**. Ketiadaan masalah server (¬ P) tidak menjamin churn tidak akan terjadi (¬ Q), karena variabel pemicu lain dapat memicu churn.
3. **Rekonstruksi Investigasi Ilmiah:**
   - Gunakan pendekatan **Modus Tollens**: Jika ingin membuktikan arsitektur server BUKAN penyebab utama, tunjukkan bahwa ketika latensi tidak melonjak, lonjakan churn tetap terjadi di lapangan. Ini membuktikan bahwa korelasi tersebut bukan hubungan implikasi tertutup. Tim harus membedah variabel independen lain secara metodologis.
