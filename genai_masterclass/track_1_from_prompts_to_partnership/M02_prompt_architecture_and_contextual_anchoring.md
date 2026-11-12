# MICROSOFT GENERATIVE AI & COPILOT PROFESSIONAL OS — TRACK 1
## Modul 02: Prompt Engineering Architecture & Contextual Anchoring
> **Sumber Utama:** *Career Essentials in Generative AI (Jeremy Utley / Stanford d.school)* & *Microsoft Copilot Prompt Crafting Standards*.  
> **Target Kompetensi:** Menguasai arsitektur rekayasa prompt tingkat korporat, menerapkan teknik Contextual Anchoring, menginjeksi Negative Guardrails untuk mengeliminasi bahasa klise AI, dan merancang Few-Shot Exemplars berakurasi tinggi.

---

### LAYER 1: KAIDAH EMAS (CORE AXIOMS)

1. **Aksioma Jangkar Kontekstual (Contextual Anchoring Principle):**
   Akurasi output Large Language Model (LLM) berkorelasi linear dengan ketajaman konteks batas yang diberikan pada 100 token pertama. Tanpa jangkar konteks (siapa pembaca, apa tujuan spesifik, dan di industri mana keputusan ini berlaku), model akan defaulting ke mean distribusi internet—menghasilkan teks generik yang tidak memiliki nilai komersial.

2. **Aksioma Batasan Negatif (The Negative Guardrail Directive):**
   Memberitahu model apa yang *dilarang* dilakukan seringkali jauh lebih efektif daripada hanya memberitahu apa yang *harus* dilakukan. Menetapkan batasan negatif eksplisit (dilarang menggunakan frasa klise seperti "di era digital ini", dilarang menulis lebih dari 3 kalimat per paragraf, dilarang memberi nasihat normatif) memangkas ruang pencarian probabilitas dari respons-respons berbobot rendah.

3. **Doktrin Pembelajaran Dalam-Konteks (Few-Shot Exemplar Dominance):**
   Satu contoh konkret pasangan input-output (*exemplar*) bernilai lebih tinggi daripada 500 kata instruksi deskriptif. Memasukkan minimal 2 hingga 3 contoh nyata (gaya bahasa, struktur argumen, dan format data) mengarahkan pola generasi token (*in-context learning*) secara deterministik tanpa perlu proses fine-tuning model yang mahal.

4. **Prinsip Kontainmen Sintaksis (Syntactic Containment & JSON Schema Enforcement):**
   Dalam alur kerja otomatisasi dan rekayasa perangkat lunak, respons AI harus dibatasi dalam format struktural yang dapat di-parse mesin (JSON / Markdown Tables murni). Kegagalan mendikte kontainmen sintaksis akan memicu kegagalan sistem (*downstream pipeline crash*) akibat model menyisipkan teks pengantar atau penutup percakapan yang tidak dibutuhkan.

---

### LAYER 2: MENTAL MODEL & DIAGRAM ASCII

```text
========================================================================================
                 ANATOMI 6 LAPIS PROMPT ENGINEERING ENTERPRISE (HEXA-PROMPT)
========================================================================================

    [ INPUT STRUKTURAL PENGGUNA ]
                 │
                 ▼
    ┌───────────────────────────────────────────────┐
    │ LAPIS 1: PERSONA & STANDAR OTORITAS           │ ──► "Kamu adalah Lead Enterprise Architect..."
    ├───────────────────────────────────────────────┤
    │ LAPIS 2: JANGKAR KONTEKS & TARGET AUDIENS     │ ──► "Untuk Direktur Keuangan B2B SaaS..."
    ├───────────────────────────────────────────────┤
    │ LAPIS 3: TUGAS UTAMA (VERBA TINDAKAN JELAS)   │ ──► "Audit kelemahan anggaran cloud ini..."
    ├───────────────────────────────────────────────┤
    │ LAPIS 4: FEW-SHOT EXEMPLARS (CONTOH NYATA)    │ ──► "Input Contoh -> Output Standar Emas"
    ├───────────────────────────────────────────────┤
    │ LAPIS 5: NEGATIVE GUARDRAILS (LARANGAN KERAS) │ ──► "Dilarang jargon, maks 4 butir, no filler"
    ├───────────────────────────────────────────────┤
    │ LAPIS 6: SCHEMA OUTPUT & FORMAT KONTAINMEN    │ ──► "Output WAJIB valid JSON murni"
    └───────────────────────┬───────────────────────┘
                            │
                            ▼
    ┌───────────────────────────────────────────────┐
    │          INFERENSI PROBABILITAS LLM           │
    │  (Mempersempit Latent Space ke Target Presisi)│
    └───────────────────────┬───────────────────────┘
                            │
                            ▼
    [ OUTPUT BERSIH, TERUJI, ZERO-SLOP & PARSEABLE ]
========================================================================================
Formula Efektivitas Prompt: E_prompt = (Konteks × Contoh) / (Ambiguitas + Jargon)
Keterangan:
- Konteks   : Ketajaman parameter operasional dan batas audiens (1 - 10).
- Contoh    : Kuantitas dan kualitas few-shot pairs yang disertakan (0 - 3).
- Ambiguitas: Kata-kata abstrak seperti "menarik", "bagus", "kreatif" (wajib diminimalkan).
- Jargon    : Istilah kosong tanpa definisi operasional (wajib 0).
========================================================================================
```

---

### LAYER 3: SYARAH DAGING (DEEP DIVE KNOWLEDGE)

#### 1. Syarah Kaidah 1: Aksioma Jangkar Kontekstual (Contextual Anchoring Principle)
Model bahasa besar seperti GPT-4 atau model Copilot tidak memiliki kesadaran subyektif; mereka adalah mesin penaksir probabilitas urutan token berikutnya berdasarkan bobot miliaran parameter. Ketika lo memberikan prompt kosong tanpa konteks seperti: *"Buat strategi pemasaran produk baru"*, model berada dalam kondisi ekuilibrium probabilitas rata-rata (*mean probability state*). Hasilnya adalah daftar 5 tips klise: riset pasar, buat akun media sosial, pasang iklan di Google, beri diskon peluncuran, dan gunakan influencer. Nasihat ini benar secara tata bahasa, tetapi bernilai Rp0 secara komersial.

Contextual Anchoring bertindak sebagai jangkar gravitasi yang membelokkan probabilitas model ke sektor spesifik:
- **Parameter Industri:** *"Produk ini adalah suplemen herbal diabetes cair berizin BPOM yang menargetkan pria usia 45-60 tahun di kota tier-2 Jawa Tengah."*
- **Kondisi Saluran Distribusi:** *"Produk tidak dijual di minimarket modern; 100% penjualan melalui direct WhatsApp response dari iklan Meta Ads berbasis video testimoni dokter lokal."*
- **Batasan Finansial:** *"Customer Acquisition Cost (CAC) maksimal Rp85.000 dengan Customer Lifetime Value (LTV) 3 bulan sebesar Rp450.000."*
Dengan 3 jangkar konteks di atas, model secara instan mengunci kosakata, pola belanja, kendala regulasi obat, dan psikologi konsumen yang relevan, menghasilkan strategi yang langsung aplikatif.

#### 2. Syarah Kaidah 2: Aksioma Batasan Negatif (The Negative Guardrail Directive)
Salah satu ciri paling mencolok dari teks buatan AI yang tidak difilter (*AI slop*) adalah keberadaan pola kalimat pembuka yang seragam dan kalimat berbunga-bunga tanpa makna. Model secara alami dilatih dengan optimasi kesopanan (*reinforcement learning from human feedback / RLHF*) yang membuatnya suka memuji pengguna, mengulang pertanyaan, atau menggunakan kata transisi basi seperti *"Tentu, ini dia solusinya!"*, *"Di era modern yang serba cepat ini..."*, atau *"Penting untuk diingat bahwa..."*.

Batasan negatif (*Negative Constraints*) berfungsi sebagai dinding pembatas keras yang mematikan cabang pohon probabilitas yang tidak lo inginkan:
- **Larangan Gaya Bahasa:** *"Dilarang menggunakan kata pembuka klise, salam, basa-basi, atau kesimpulan penutup. Langsung mulai dengan butir pertama."*
- **Larangan Jargon Kosong:** *"Dilarang menggunakan kata-kata hampa makna seperti: sinergi, holistik, transformatif, revolusioner, atau ekosistem digital, kecuali disertai metrik kuantitatif terukur."*
- **Larangan Penjelasan Normatif:** *"Jangan jelaskan mengapa sesuatu penting; hanya tuliskan langkah teknis bagaimana cara melakukannya secara fisik di keyboard atau lapangan."*

#### 3. Syarah Kaidah 3: Doktrin Pembelajaran Dalam-Konteks (Few-Shot Exemplar Dominance)
Prompting terbagi menjadi tiga kategori:
1. **Zero-Shot:** Lo hanya memberikan instruksi tanpa contoh sama sekali. Akurasi moderat, gaya bahasa rentan meleset.
2. **One-Shot:** Lo memberikan tepat satu contoh sebelum meminta tugas baru. Meningkatkan konsistensi format hingga 60%.
3. **Few-Shot (2-3 Exemplars):** Lo memberikan 2 atau 3 contoh pasangan input-output yang mencerminkan standar emas kualitas lo. Tingkat konsistensi melonjak di atas 95%.

Few-Shot bekerja karena mekanisme perhatian (*attention heads*) di dalam arsitektur transformer menghitung kesamaan matriks antara token contoh dan token yang sedang diproduksi. Model memetakan sintaksis, panjang kalimat, rasio kata kerja terhadap kata sifat, dan struktur hierarki dari contoh tersebut. Lo tidak perlu menjelaskan panjang lebar: *"Gunakan nada bicara tegas, santai, gaya bahasa lu/gw, kalimat pendek di bawah 12 kata."* Cukup berikan dua paragraf tulisan lo sendiri sebagai contoh, lalu tulis: *"Analisis input berikut dan hasilkan teks dengan ritme serta struktur yang identik dengan contoh di atas."*

#### 4. Syarah Kaidah 4: Prinsip Kontainmen Sintaksis (Syntactic Containment & JSON Schema)
Ketika AI generatif diintegrasikan ke dalam sistem perangkat lunak (misalnya: bot customer service WhatsApp, skrip otomatisasi laporan, atau parser invoice), AI tidak boleh bertingkah seperti teman ngobrol. Jika skrip backend Python mengharapkan JSON mentah tetapi AI membalas dengan: *"Tentu bos, ini data yang lo minta: ```json {...} ``` Semoga membantu ya!"*, maka fungsi `json.loads()` akan mengalami error fatal (*SyntaxError / downstream crash*).

Kontainmen sintaksis menegakkan aturan tak terbantahkan:
- Perintahkan model untuk bertindak sebagai *pure serialization engine*.
- Definisikan tipe data per kunci: string, integer, boolean, atau array of objects.
- Wajibkan output diawali dengan karakter `{` dan diakhiri dengan karakter `}` tanpa spasi, karakter escape Markdown, atau komentar di luar kurung kurawal.

---

### LAYER 4: FIELD PLAYBOOK (TACTICAL SOP & CODE)

#### SOP Formulasi Prompt Hexa-Core (Standar Enterprise)
Sebelum menekan tombol enter pada model AI mana pun, verifikasi bahwa prompt lo telah melewati checklist Hexa-Core:
1. `[ROLE]` Apakah peran sudah spesifik dengan titel fungsional (bukan sekadar "ahli umum")?
2. `[CONTEXT]` Apakah situasi pasar, audiens target, dan limitasi modal sudah ditulis?
3. `[ACTION]` Apakah instruksi menggunakan kata kerja tindakan operasional yang dapat diverifikasi?
4. `[CONSTRAINTS]` Apakah larangan frasa klise dan batas panjang kata sudah dicantumkan?
5. `[EXEMPLAR]` Apakah sudah menyertakan minimal 1 contoh nyata output yang diharapkan?
6. `[OUTPUT SCHEMA]` Apakah format kemasan akhir (JSON/Tabel/Markdown) sudah dikunci?

#### Template Produksi Verbatim: Masterclass B2B Sales Angle Generator
```text
[ROLE]
Kamu adalah B2B Enterprise Copywriter spesialis SaaS Human Resources Information System (HRIS) dengan track record closing kontrak tahunan bernilai miliaran rupiah.

[CONTEXT]
Target prospek adalah Direktur SDM (HRD) perusahaan logistik di Indonesia dengan 1.500 karyawan lapangan (kurir dan staf gudang). Masalah utama mereka adalah kebocoran biaya lembur fiktif dan absensi manual berbasis kertas yang menghabiskan 40 jam kerja HR tiap akhir bulan.

[TASK]
Tuliskan 3 variasi email dingin (cold email outreach) dengan pendekatan Problem-Agitate-Solve (PAS).

[NEGATIVE GUARDRAILS]
- DILARANG menggunakan kata pembuka: "Semoga email ini menemui Anda dalam keadaan sehat", "Perkenalkan nama saya", atau "Di era digital ini".
- DILARANG menulis subjek email lebih dari 6 kata.
- Panjang badan email MAKSIMAL 90 kata per variasi.
- WAJIB menyebutkan metrik kerugian: "40 jam lembur fiktif".

[FEW-SHOT EXEMPLAR]
Input Masalah: Pencatatan inventaris gudang manual.
Output Standar Emas:
Subjek: Selisih stok gudang 12% tiap audit?
Pak Hendra, ketika staf gudang masih mencatat SKU pakai clipboard, selisih 12% selalu dianggap "wajar". Padahal itu bocor Rp40 juta sebulan. Kami memasang barcode scanner mobile yang otomatis sinkron ke ledger keuangan. Selisih stok turun jadi 0,2% dalam 14 hari pertama. Boleh saya kirimkan video demo 2 menit cara kerjanya?

[OUTPUT FORMAT]
Hasilkan tepat 3 variasi email sesuai batasan di atas.
```

#### Skrip Validator Python: `prompt_quality_gate.py`
Skrip otomatis untuk menguji apakah respons LLM mematuhi batasan negatif dan skema sintaksis:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prompt Quality Gate & Negative Constraint Validator
Memverifikasi output model terhadap larangan frasa klise AI dan validitas JSON schema.
"""

import json
import re

FORBIDDEN_PHRASES = [
    "di era digital",
    "tentu, ini dia",
    "semoga membantu",
    "penting untuk diingat",
    "sinergi",
    "holistik",
    "transformasi digital"
]

def audit_llm_output(raw_text, expect_json=False):
    violations = []
    
    # 1. Audit Frasa Klise
    lower_text = raw_text.lower()
    for phrase in FORBIDDEN_PHRASES:
        if phrase in lower_text:
            violations.append(f"Pelanggaran Batasan Negatif: Menemukan frasa terlarang '{phrase}'")
            
    # 2. Audit Sintaksis JSON jika disyaratkan
    parsed_json = None
    if expect_json:
        cleaned = raw_text.strip()
        # Bersihkan pembungkus markdown jika ada
        if cleaned.startswith("```json"):
            cleaned = cleaned[7:]
        if cleaned.endswith("```"):
            cleaned = cleaned[:-3]
        cleaned = cleaned.strip()
        
        try:
            parsed_json = json.loads(cleaned)
        except json.JSONDecodeError as err:
            violations.append(f"Pelanggaran Kontainmen Sintaksis: Gagal parse JSON ({str(err)})")
            
    score = max(0, 100 - (len(violations) * 30))
    return {
        "status": "PASS" if len(violations) == 0 else "FAIL",
        "score": score,
        "violations": violations,
        "payload": parsed_json
    }

if __name__ == "__main__":
    sample_response = '{"lead_name": "Pak Hendra", "score": 92, "status": "qualified"}'
    res = audit_llm_output(sample_response, expect_json=True)
    print("[*] Prompt Quality Gate Audit Result:")
    print(json.dumps(res, indent=2))
```

---

### LAYER 5: DIAGNOSTIC DRILL (STUDI KASUS & UJI MANDIRI)

#### Skenario Kasus Lapangan
Sebuah biro konsultan manajemen pajak merekrut seorang junior associate untuk membuat ringkasan peraturan pajak terbaru terkait tarif natura karyawan. Junior associate tersebut memasukkan prompt ke LLM: *"Ringkas peraturan pajak natura terbaru dan jelaskan dampaknya bagi perusahaan manufaktur secara lengkap dan menarik."* 
Model menghasilkan 1.200 kata dokumen yang tampak meyakinkan, penuh dengan jargon profesional, dan kesimpulan optimis. Namun saat dipresentasikan di hadapan klien direktur keuangan (CFO), sang CFO langsung murka karena ringkasan tersebut salah mencantumkan ambang batas fasilitas laptop kantor (menggunakan peraturan draf lama yang sudah direvisi) dan tidak memuat pasal hukum resmi satu pun.

#### Lembar Uji Mandiri
1. Analisis kegagalan arsitektur prompt yang ditulis oleh junior associate berdasarkan Kaidah 1 (Contextual Anchoring) dan Kaidah 4 (Syntactic Containment)!
2. Mengapa model menyajikan peraturan draf lama secara sangat meyakinkan tanpa memberitahu bahwa data tersebut mungkin usang (halusinasi kepastian)?
3. Tuliskan ulang prompt di atas menggunakan prinsip Hexa-Core agar menghasilkan tabel perbandingan tarif pajak resmi yang bebas dari spekulasi hukum!

#### Kunci Jawaban Lengkap & Analisis Diagnostik
1. **Analisis Kegagalan Prompt:** 
   - **Ketiadaan Jangkar Kontekstual:** Prompt menggunakan kata-kata cair dan subyektif (*"secara lengkap dan menarik"*). Model tidak diberikan nomor undang-undang/PMK yang spesifik, tahun penerbitan, atau kategori aset natura yang hendak dihitung.
   - **Ketiadaan Kontainmen Sintaksis:** Model dibiarkan menulis esai bebas (*freeform narrative*) sepanjang 1.200 kata, sehingga model memprioritaskan kelancaran tata bahasa (*fluency*) di atas kebenaran faktual angka.
2. **Akar Masalah Halusinasi Kepastian:** LLM tidak dirancang untuk memverifikasi kebenaran absolut, melainkan memprediksi token probabilitas tertinggi. Karena peraturan natura banyak diperdebatkan di media massa dengan berbagai versi draf, model menggabungkan cuplikan diskusi umum internet. Tanpa batasan negatif yang melarang asumsi dan mewajibkan sitasi nomor pasal, model akan mengarang detail secara percaya diri (*confident hallucination*).
3. **Formulasi Prompt Perbaikan (Hexa-Core Compliant):**
   ```text
   [ROLE]
   Kamu adalah Konsultan Pajak Senior bersertifikat BKP (Brevet C) di Indonesia.

   [CONTEXT]
   Klien kami adalah perusahaan manufaktur tekstil dengan 3.000 buruh dan 50 level manajerial. Klien membutuhkan kepastian perlakuan pajak PPh 21 atas fasilitas kenikmatan (natura) berdasarkan Peraturan Menteri Keuangan (PMK) No. 66/2023.

   [TASK]
   Ekstrak aturan natura khusus untuk: (1) Makanan/minuman seluruh pegawai, (2) Fasilitas tempat tinggal/mess, (3) Laptop dan ponsel kerja.

   [NEGATIVE GUARDRAILS]
   - DILARANG mengutip peraturan selain PMK 66/2023 atau UU Harmonisasi Peraturan Perpajakan (HPP).
   - JIKA sebuah fasilitas tidak diatur secara eksplisit dalam PMK 66/2023, tuliskan: "TIDAK TERTERA DALAM REGULASI".
   - DILARANG memberikan pengantar basa-basi atau analisis di luar tabel.

   [OUTPUT FORMAT]
   Hasilkan tabel Markdown murni dengan 4 kolom tepat:
   | Jenis Fasilitas | Batasan Nilai Bebas Pajak (Non-Objek) | Dasar Hukum (Pasal & Ayat) | Catatan Kritis Payroll |
   ```
