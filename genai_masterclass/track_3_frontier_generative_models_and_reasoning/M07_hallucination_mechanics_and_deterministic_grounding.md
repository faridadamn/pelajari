# MICROSOFT GENERATIVE AI & COPILOT PROFESSIONAL OS — TRACK 3
## Modul 07: Anatomi Halusinasi AI & Mitigasi Deterministik
> **Sumber Utama:** *AI Literacy for Everyone (Dr. Marily Nika / Google & Meta)* & *Microsoft Copilot Grounding Architecture Guides*.  
> **Target Kompetensi:** Membongkar patologi halusinasi pada model bahasa besar (LLM), memahami kalkulasi probabilitas token versus kebenaran faktual, menyetel parameter suhu (temperature) dan sampling, serta mengimplementasikan teknik Retrieval-Augmented Grounding (RAG) untuk menjamin akurasi data enterprise.

---

### LAYER 1: KAIDAH EMAS (CORE AXIOMS)

1. **Aksioma Stokastik Generasi Token (Probability Over Truth):**
   Large Language Model (LLM) tidak memiliki pemahaman epistemologis mengenai apa yang "benar" atau "salah"; model adalah mesin penaksir probabilitas bersyarat yang memilih token kata berikutnya berdasarkan korelasi statistik dari triliunan data latih. Oleh karena itu, kalimat yang secara tata bahasa sempurna (*grammatically flawless*) bisa jadi sepenuhnya merupakan kebohongan faktual (*factually fabricated*).

2. **Patologi Halusinasi Percaya Diri (Confident Fabrication Pathology):**
   Halusinasi AI terjadi ketika model menyajikan informasi fiktif (seperti nama eksekutif perusahaan yang salah, tanggal rilis produk yang tertukar, atau referensi hukum palsu) dengan nada bicara yang sangat formal, meyakinkan, dan percaya diri. Ketiadaan rasa ragu ini berbahaya karena dapat mengecoh pengguna yang mengira kefasihan bahasa (*fluency*) sama dengan akurasi (*truthfulness*).

3. **Doktrin Penjangkaran Bukti Deterministik (The Grounding Doctrine):**
   Satu-satunya cara yang terbukti secara teknis untuk menghentikan halusinasi pada domain berisiko tinggi (hukum, keuangan, kesehatan, regulasi) adalah **Grounding**: menyuntikkan dokumen sumber fakta terverifikasi langsung ke dalam jendela konteks (*context window*) model, disertai instruksi keras (*hard boundary constraint*) yang melarang model menjawab di luar fakta yang dilampirkan.

4. **Hukum Modulasi Termodinamika Sampling (The Temperature Zero Rule):**
   Parameter suhu (*temperature*) mengatur tingkat keacakan pemilihan token pada lapisan Softmax. Untuk tugas kreatif dan pembangkitan ide divergen, nilai temperature tinggi (T \ge 0,7) sangat dianjurkan; namun untuk tugas operasional analitis, ekstraksi data, dan laporan faktual, temperature wajib dikunci ke titik nol (T = 0,0) untuk memaksa model memilih jalur token dengan probabilitas tertinggi (*deterministic greedy search*).

---

### LAYER 2: MENTAL MODEL & DIAGRAM ASCII

```text
========================================================================================
             ANATOMI HALUSINASI VS DETERMINISTIC GROUNDING PIPELINE
========================================================================================

    [ SKENARIO A: PROMPTING TANPA GROUNDING (RAW LLM -> RAWAN HALUSINASI) ]
    Pertanyaan User: "Siapa CEO PT Sinar Roda Utama dan apa rencana belanja modal 2026?"
            │
            ▼
    ┌───────────────────────────┐
    │  Jaringan Syaraf LLM      │ ──► Model tidak punya data internal perusahaan!
    │  (Prediksi Token Bebas)   │ ──► Menggabungkan nama acak dari industri sejenis.
    └─────────────┬─────────────┘
                  │
                  ▼
    [ OUTPUT SALAH: "CEO adalah Bapak X..." (Percaya Diri, Padahal Fiktif!) ]

----------------------------------------------------------------------------------------

    [ SKENARIO B: DETERMINISTIC GROUNDING (RAG PIPELINE -> ZERO HALUSINASI) ]
    Pertanyaan User: "Siapa CEO PT Sinar Roda Utama dan apa rencana belanja modal 2026?"
            │
            ▼
    ┌───────────────────────────┐
    │  1. RETRIEVAL SEARCH      │ ──► Ambil Dokumen Notulen Rapat Direksi 11 Nov 2026
    ├───────────────────────────┤
    │  2. CONTEXT INJECTION     │ ──► Masukkan Teks Resmi ke dalam Context Window
    ├───────────────────────────┤
    │  3. HARD BOUNDARY GUARD   │ ──► "Jawab HANYA dari dokumen ini. T = 0.0"
    ├───────────────────────────┤
    │  4. INFERENSI REASONING   │ ──► Ekstraksi Fakta Literal Tanpa Karangan
    └─────────────┬─────────────┘
                  │
                  ▼
    [ OUTPUT AKURAT: Jawaban Terverifikasi 100% Sesuai Notulen + Sitasi Halaman ]
========================================================================================
Formula Pemilihan Token Softmax Berdasarkan Temperatur T:
P(Token_i) = exp(Z_i / T) / ∑ exp(Z_j / T)
Keterangan:
- Z_i : Logit numerik mentah untuk token ke-i sebelum normalisasi.
- T   : Parameter Temperature (Jika T -> 0, probabilitas terkonsentrasi pada logit maks).
========================================================================================
```

---

### LAYER 3: SYARAH DAGING (DEEP DIVE KNOWLEDGE)

#### 1. Syarah Kaidah 1: Aksioma Stokastik Generasi Token
Salah satu ilusi terbesar dalam kecerdasan buatan generatif adalah anggapan bahwa model "menyimpan ensiklopedia fakta" di dalam chip komputernya. Faktanya, sebuah model berukuran 70 miliar parameter tidak memiliki tabel baris-dan-kolom fakta seperti database SQL. 

Yang tersimpan di dalam bobot sinapsis neural network adalah **korelasi distribusi probabilitas**. Ketika model memproduksi sebuah kalimat, setiap kata (token) dipilih satu per satu berdasarkan kata-kata sebelumnya:
P(W_t | W_1, W_2, \dots, W_{t-1})

Jika sebuah entitas sering muncul bersamaan di internet (misalnya nama perusahaan Elon Musk seperti Tesla, SpaceX, dan Neuralink), model dapat menghubungkannya dengan baik. Tetapi jika lo menanyakan topik yang lebih spesifik atau tanggal yang presisi, model tetap dipaksa oleh arsitekturnya untuk menyelesaikan kalimat. Karena model tidak memiliki mekanisme sensor internal untuk mengatakan *"saya tidak tahu"* (kecuali diprogram secara khusus), model akan memilih token yang secara linguistik tampak paling cocok untuk mengisi kekosongan tersebut. Inilah yang mendasari mengapa model bisa mengarang tanggal lahir tokoh atau mencampuradukkan CEO antar perusahaan.

#### 2. Syarah Kaidah 2: Patologi Halusinasi Percaya Diri (Confident Fabrication)
Bahaya terbesar dari halusinasi AI bukanlah kebohongannya, melainkan **ketiadaan keraguan dalam gaya bahasanya**. 

Ketika manusia tidak yakin akan sebuah jawaban, manusia akan menunjukkan keragu-raguan: menggunakan jeda, mengubah intonasi suara, atau menyelipkan frasa seperti *"seingat saya"* atau *"saya kurang yakin"*. Sebaliknya, model bahasa besar dilatih untuk memproduksi teks dengan gaya penulisan ensiklopedis yang formal dan tegas. Model akan menyajikan data palsu dengan tingkat keyakinan 100%, menggunakan kalimat pasif yang terstruktur rapi, tabel yang indah, dan penomoran butir yang sempurna.

Fenomena ini sering mengecoh para profesional di bidang pemasaran, hukum, dan manajemen. Mereka mengira bahwa karena tata bahasanya sangat elegan (*high fluency*), maka isinya pasti akurat (*high factuality*). Dalam Masterclass OS, kita menetapkan aturan emas: **Kefasihan Sintaksis Tidak Pernah Menjadi Bukti Kebenaran Faktual**.

#### 3. Syarah Kaidah 3: Doktrin Penjangkaran Bukti Deterministik (Grounding)
Untuk menghilangkan risiko hukum dan finansial akibat halusinasi di lingkungan perusahaan, industri teknologi mengandalkan arsitektur **Grounding** atau **Retrieval-Augmented Generation (RAG)**.

Prinsip kerja Grounding sangat elegan:
1. Kita memisahkan peran model: Model tidak lagi difungsikan sebagai *pustaka memori pengetahuan*, melainkan sebagai *mesin penalaran logis* (Logic Processor).
2. Data pengetahuan diambil secara deterministik dari database terpercaya perusahaan (file PDF SOP, database transaksi SQL, atau email resmi).
3. Data terverifikasi tersebut dimasukkan langsung ke dalam prompt bersama instruksi pembatas: *"Kamu adalah mesin pemeriksa kepatuhan. Jawab pertanyaan pengguna HANYA berdasarkan teks kutipan di bawah ini. Jika jawabannya tidak tertulis secara eksplisit dalam teks kutipan, jawab tegas: 'INFORMASI TIDAK TERSEDIA DALAM DOKUMEN'. Dilarang berasumsi atau mengekstrapolasi."*

Dengan arsitektur Grounding, tingkat halusinasi model anjlok dari 15-20% menjadi mendekati 0%.

#### 4. Syarah Kaidah 4: Hukum Modulasi Termodinamika Sampling (The Temperature Zero)
Di balik proses komputasi LLM, terdapat parameter matematika yang disebut **Temperature (T)**:
- Ketika T = 1,0 (Suhu Normal): Distribusi probabilitas Softmax menyebar rata. Model memiliki kebebasan untuk memilih token-token yang berada di urutan kedua atau ketiga. Ini menghasilkan tulisan yang variatif, metaforis, dan kaya kosa kata, sangat ideal untuk menulis puisi, novel, atau brainstorming ide kampanye iklan.
- Ketika T \to 0,0 (Suhu Nol / Greedy Decoding): Distribusi probabilitas Softmax menjadi sangat curam (*spiky*). Peluang token tertinggi mendekati 1,0 sementara token lainnya bernilai nol. Model dipaksa secara deterministik untuk selalu memilih kata yang paling pasti dan paling langsung.

Di lingkungan enterprise, menjalankan otomatisasi keuangan atau parsing dokumen legal dengan parameter T = 0,8 adalah tindakan bunuh diri operasional. Semua pipeline ekstraksi data, ringkasan regulasi, dan kode script wajib dikunci pada **T = 0,0** untuk menjamin hasil yang konsisten dan dapat direproduksi (*reproducible results*).

---

### LAYER 4: FIELD PLAYBOOK (TACTICAL SOP & CODE)

#### SOP 1: Protokol Anti-Halusinasi Tiga Lapis (Tri-Guard Architecture)
1. **Lapis 1 (Prompt Constraint Injection):** Selalu pasang klausul larangan ekstrapolasi: *"Batas Pengetahuan: Hanya gunakan data yang dilampirkan. Jika ada fakta yang tidak disebutkan, jangan coba menebak."*
2. **Lapis 2 (Temperature Lockdown):** Pastikan parameter `temperature=0.0` pada pemanggilan API atau konfigurasi agent runtime.
3. **Lapis 3 (Post-Generation Fact Check Filter):** Jalankan skrip validator otomatis untuk memeriksa apakah entitas angka, tanggal, atau nama orang yang muncul pada output benar-benar ada di dalam dokumen konteks sumber.

#### Skrip Implementasi Python: `deterministic_grounding_rag.py`
Skrip Python mandiri untuk mengimplementasikan verifikasi grounding deterministik dan mendeteksi halusinasi entitas:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deterministic Grounding & Hallucination Guard
Memverifikasi apakah entitas faktual pada output LLM dijangkarkan secara sah 
pada dokumen sumber terverifikasi.
"""

import re
import json

# 1. Dokumen Sumber Terverifikasi (Enterprise Grounding Truth)
SOURCE_DOCUMENT = """
Notulen Rapat Direksi PT Sinar Roda Utama tanggal 11 November 2026.
Peserta: Ibu Pimpinan, Tim FAT, dan Tim Logistik.
Keputusan Sasaran Strategis 2026:
1. Target penagihan piutang usaha (AR) terverifikasi mencapai 98,5 persen.
2. Pembayaran hutang dagang (AP) tepat waktu sesuai syarat pembayaran (TOP) mencapai 100 persen.
3. Seluruh divisi wajib merevisi format pelaporan ke konsep Procurement Tersentral untuk pengendalian biaya.
"""

def extract_numbers_and_percentages(text):
    """Mengekstrak angka dan persentase untuk audit grounding."""
    return set(re.findall(r'\b\d+(?:[.,]\d+)?%?', text))

def audit_grounding_integrity(generated_output, source_text):
    """
    Memeriksa integritas grounding output terhadap dokumen sumber.
    Jika output mencantumkan angka/persentase yang TIDAK ADA di sumber -> INDIKASI HALUSINASI.
    """
    source_facts = extract_numbers_and_percentages(source_text)
    output_facts = extract_numbers_and_percentages(generated_output)
    
    # Cari fakta liar (unsupported entities)
    unsupported = output_facts - source_facts
    
    is_safe = len(unsupported) == 0
    return {
        "status": "VERIFIED SAFE" if is_safe else "HALLUCINATION DETECTED",
        "supported_facts": list(output_facts & source_facts),
        "unsupported_wild_facts": list(unsupported),
        "audit_note": "Output mematuhi dokumen sumber." if is_safe else f"Ditemukan entitas angka fiktif: {list(unsupported)}"
    }

if __name__ == "__main__":
    print("[*] Menguji Validator Grounding Deterministik...")
    
    # Skenario 1: Output Terjangkar Bersih (Grounded)
    output_good = "Sesuai rapat 11 November 2026, target AR adalah 98,5% dan pembayaran AP tepat TOP 100%."
    res_1 = audit_grounding_integrity(output_good, SOURCE_DOCUMENT)
    print("\n[Pengujian 1: Output Grounded]")
    print(json.dumps(res_1, indent=2))
    
    # Skenario 2: Output Berhalusinasi (Menyebut angka 85% dan tahun 2025 yang tidak ada di dokumen)
    output_bad = "Target penagihan piutang adalah 85% untuk kuartal pertama tahun 2025."
    res_2 = audit_grounding_integrity(output_bad, SOURCE_DOCUMENT)
    print("\n[Pengujian 2: Output Berhalusinasi]")
    print(json.dumps(res_2, indent=2))
```

---

### LAYER 5: DIAGNOSTIC DRILL (STUDI KASUS & UJI MANDIRI)

#### Skenario Kasus Lapangan
Manajer Pemasaran sebuah perusahaan retail fesyen ingin membuat buletin opini mingguan (*weekly industry newsletter*) yang mengulas tren bisnis dan kepemimpinan merek global menggunakan model AI generatif. Pada edisi percobaan pertama, manajer tersebut memberikan prompt umum: *"Buatkan opini mingguan tentang dinamika pergantian CEO di industri ritel fesyen global minggu ini."*
Saat naskah dibaca, manajer mendapati bahwa model menyebutkan nama CEO Gucci telah digantikan oleh CEO H&M, serta tanggal pelantikan yang tertukar antara tahun 2024 dan 2026. Ketika ditegur, staf pemula menjawab: *"ChatGPT ini kan versi paling canggih dan pintar, mungkin sistemnya lagi lelah atau kita harus memintanya lebih sopan."*

#### Lembar Uji Mandiri
1. Berdasarkan Kaidah 1 dan Kaidah 2, jelaskan mengapa staf pemula salah mendiagnosis penyebab masalah di atas!
2. Mengapa AI generatif tidak boleh digunakan untuk penulisan artikel opini berbasis berita terkini secara langsung tanpa proses penyuapan data (*context feed*)?
3. Rancanglah sebuah template prompt operasional untuk memproduksi buletin opini di atas dengan jaminan 0% kesalahan nama CEO dan tanggal!

#### Kunci Jawaban Lengkap & Analisis Diagnostik
1. **Kesalahan Diagnosis Staf Pemula:** Staf mengatribusikan sifat manusiawi (*antropomorfisme*) kepada model AI (mengira sistem "lelah" atau "kurang dimintai secara sopan"). Masalah sebenarnya adalah keterbatasan arsitektural: model bahasa besar menghasilkan teks berdasarkan kalkulasi probabilitas kata (*next-token prediction*), bukan pencarian fakta secara langsung. Model tidak memiliki basis data berita langsung, sehingga ketika diminta menulis berita kepemimpinan korporat terkini, model mencampuradukkan pola nama eksekutif dan merek yang ada di data latih masa lalunya.
2. **Larangan Penulisan Berita Terkini Tanpa Context Feed:** Berita terkini, pergantian pimpinan, dan tanggal kejadian adalah data spesifik berdimensi temporal tinggi yang berubah setiap hari. LLM memiliki batas waktu pemotongan data pelatihan (*static knowledge cutoff*). Mengandalkan model mentah tanpa menyertakan tautan atau teks berita resmi yang terjadi hari ini menjamin terjadinya halusinasi nama dan kronologi waktu.
3. **Template Prompt Operasional (Grounding Compliant):**
   ```text
   [ROLE]
   Kamu adalah Editor Opini Bisnis Fesyen Senior.

   [TASK]
   Tuliskan analisis opini profesional sepanjang 200 kata mengenai dampak pergantian kepemimpinan terhadap arah desain produk.

   [GROUNDING CONTEXT - DATA TERVERIFIKASI WAJIB]
   Hanya gunakan data fakta dari siaran pers resmi berikut:
   "Tanggal 10 November 2026: Stefano Cantino resmi ditunjuk sebagai CEO Gucci menggantikan Jean-François Palus, efektif per 1 Januari 2027."

   [NEGATIVE CONSTRAINTS]
   - DILARANG menyebutkan nama CEO atau merek lain selain yang tertulis di teks konteks di atas.
   - DILARANG mengubah tanggal atau tahun yang telah ditetapkan.
   - JIKA kamu memerlukan data latar belakang yang tidak ada di teks di atas, nyatakan implikasinya secara konseptual tanpa menyebut angka fiktif.
   ```
