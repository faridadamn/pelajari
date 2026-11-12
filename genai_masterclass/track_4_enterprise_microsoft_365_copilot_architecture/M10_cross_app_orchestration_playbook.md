# MICROSOFT GENERATIVE AI & COPILOT PROFESSIONAL OS — TRACK 4
## Modul 10: Cross-App Orchestration Playbook: Excel, Word, PowerPoint, Teams & Outlook
> **Sumber Utama:** *Learning Microsoft 365 Copilot for Work (Jess Stratton)* & *Enterprise Productivity Playbooks*.  
> **Target Kompetensi:** Menguasai orkestrasi otomatisasi lintas aplikasi kerja Microsoft 365 Copilot: mengubah dokumen laporan teknis Word menjadi dek presentasi eksekutif PowerPoint, melakukan analisis data numerik mendalam di Excel, mengekstrak risalah rapat Teams secara asinkron, dan menyusun korespondensi berkecepatan tinggi di Outlook.

---

### LAYER 1: KAIDAH EMAS (CORE AXIOMS)

1. **Aksioma Transformasi Lintas Format (Cross-App Modality Translation):**
   Nilai tertinggi dari Microsoft 365 Copilot terletak pada kemampuannya meruntuhkan sekat antar aplikasi (*app silos*). Dokumen narasi teknis 20 halaman di Word dapat ditransformasikan secara instan menjadi 10 slide presentasi visual berstruktur piramida di PowerPoint, lengkap dengan catatan pembicara (*speaker notes*), tanpa perlu proses copy-paste manual yang melelahkan.

2. **Doktrin Deterministik Excel (Formulas & Python in Excel Grounding):**
   Copilot di Excel tidak boleh dibiarkan menebak angka secara probabilitas; ia harus diarahkan untuk bertindak sebagai *formula generator* dan interpreter kode Python dalam spreadsheet. Setiap wawasan (*insight*) bisnis wajib diikat pada rumus tabel terstruktur (seperti `SUMIFS`, `XLOOKUP`, atau skrip visualisasi `matplotlib`) yang dapat diverifikasi secara audit oleh akuntan manusia.

3. **Prinsip Kehadiran Asinkron Teams (The Asynchronous Meeting Synthesis Invariant):**
   Dalam organisasi modern, menghadiri setiap rapat secara langsung adalah pemborosan waktu manajerial yang mahal. Melalui transkripsi real-time dan analisis sentimen Copilot di Teams, seorang eksekutif dapat tetap memegang kendali proyek dengan meminta rekapitulasi 3 menit: keputusan apa yang disepakati, argumen apa yang diperdebatkan, dan daftar tugas (*action items*) siapa yang ditugaskan beserta tenggat waktunya.

4. **Kompresi dan Kalibrasi Nada Outlook (Executive Communication Coaching):**
   Membaca utas email (*email thread*) panjang dengan 25 balasan menghabiskan fokus kognitif harian. Copilot di Outlook berfungsi ganda: sebagai kompresor utas (*thread summarizer*) yang mengekstrak poin perselisihan inti dalam 3 kalimat, dan sebagai pelatih nada (*coaching tone*) untuk memastikan tanggapan email bernada tegas, diplomatis, dan bebas dari pasif-agresif.

---

### LAYER 2: MENTAL MODEL & DIAGRAM ASCII

```text
========================================================================================
             ORKESTRASI ALUR KERJA LINTAS APLIKASI MICROSOFT 365 COPILOT
========================================================================================

    [ FASE 1: INGESTI & ANALISIS DATA ]
    Data Transaksi Mentah ──► [ MICROSOFT EXCEL ]
                              - Formula Terstruktur
                              - Python in Excel (Korelasi & Tren)
                              - Output: Tabel Pivot & Margin Profit
                                      │
                                      ▼
    [ FASE 2: DRAF STRATEGI TEKNIS ]
    Tabel & Analisis Margin ──► [ MICROSOFT WORD ]
                                - Contextual Grounding via Graph
                                - Struktur Laporan Formal 5 Bagian
                                - Output: Dokumen Rekomendasi (Whitepaper)
                                        │
                                        ▼
    [ FASE 3: PRESENTASI EKSEKUTIF ]
    Dokumen Word (.docx)    ──► [ MICROSOFT POWERPOINT ]
                                - Transformasi Lintas Format Instan
                                - Dek 8 Slide Ringkas Berstruktur
                                - Visual Layout & Speaker Notes
                                        │
                                        ▼
    [ FASE 4: ALINYEMEN TIM & RAPAT ]
    Diskusi Slide di Rapat  ──► [ MICROSOFT TEAMS ]
                                - Transkrip Percakapan Real-Time
                                - Rekap Keputusan & Action Items Otomatis
                                        │
                                        ▼
    [ FASE 5: DISTRIBUSI & CLOSING ]
    Risalah & Tugas Disetujui──► [ MICROSOFT OUTLOOK ]
                                 - Kompresi Utas Email
                                 - Coaching Nada Komunikasi Profesional
                                 - Eksekusi Broadcast ke Seluruh Stakeholder
========================================================================================
```

---

### LAYER 3: SYARAH DAGING (DEEP DIVE KNOWLEDGE)

#### 1. Syarah Kaidah 1: Aksioma Transformasi Lintas Format
Sebelum era AI generatif, alur kerja pembuatan laporan korporat adalah proses berantai yang penuh gesekan: seorang analis menghabiskan 3 hari menyusun dokumen Word sepanjang 30 halaman. Kemudian analis tersebut harus membuka PowerPoint, menyalin teks paragraf demi paragraf, memecahnya menjadi poin-poin singkat (*bullet points*), mencari gambar yang sesuai, dan menulis catatan presentasi. Proses ini memakan waktu 2 hari tambahan dan rawan terjadi salah kutip.

Microsoft 365 Copilot mereduksi waktu ini menjadi hitungan detik melalui **Cross-App Modality Translation**:
- Di dalam PowerPoint, lo cukup menekan tombol Copilot dan mengetik: *"Create presentation from file: https://tenant.sharepoint.com/.../Laporan_Strategi_Ekspansi_Q4.docx"*.
- Copilot membaca hierarki dokumen Word (Heading 1, Heading 2, dan tabel data).
- Copilot secara otomatis mengekstrak argumen inti, membuat struktur narasi 8 hingga 10 slide, memilih tata letak visual (*smart layout*), dan menyusun narasi verbal di kolom *Speaker Notes* agar pembicara tidak membaca teks di layar saat presentasi di hadapan dewan komisaris.

#### 2. Syarah Kaidah 2: Doktrin Deterministik Excel
Spreadsheet Excel adalah ranah angka pasti. Dalam audit keuangan atau kalkulasi komisi penjualan, lo tidak boleh menoleransi toleransi kesalahan 0,1% sekalipun. Jika lo bertanya ke LLM biasa: *"Berapa total penjualan produk A di wilayah Jawa Barat?"*, model generatif bebas cenderung memperkirakan angka (*fuzzy guessing*) yang memicu skandal pembukuan.

Copilot di Excel didesain dengan pagar pembatas deterministik (**Formula Grounding**):
- Saat lo meminta: *"Tunjukkan tren produk dengan margin profit terendah tetapi biaya logistik tertinggi"*, Copilot tidak langsung memuntahkan angka tebakan.
- Copilot menganalisis tabel data lo dan menuliskan formula Excel resmi:
  `=IF(AND([@Margin]<0.15, [@Ongkir]>50000), "Evaluasi Vendor", "Aman")`
- Atau untuk analisis tingkat lanjut, Copilot menyuntikkan skrip **Python in Excel** langsung di dalam sel: menjalankan regresi statistik menggunakan library `pandas` dan merender grafik kurva tren menggunakan `matplotlib`. 
Hasil analisis dapat diperiksa (*auditable*), rumus dapat diverifikasi oleh manusia, dan integritas pembukuan tetap terjaga 100%.

#### 3. Syarah Kaidah 3: Prinsip Kehadiran Asinkron Teams
Penyakit terbesar budaya kerja korporat modern adalah sindrom rapat maraton (*back-to-back meeting fatigue*). Banyak manajer menghabiskan 6 jam sehari duduk di depan layar Teams hanya untuk mendengarkan perdebatan teknis yang sebenarnya hanya menghasilkan 1 keputusan penting di 5 menit terakhir.

Copilot di Microsoft Teams mengubah paradigma ini menjadi **Kehadiran Asinkron (Asynchronous Presence)**:
- Lo tidak perlu hadir di rapat yang bukan merupakan domain eksekusi langsung lo. Cukup aktifkan opsi *"Transcribe Meeting"*.
- Setelah rapat selesai (atau bahkan di tengah rapat yang sedang berjalan), lo dapat membuka panel Copilot di Teams dan bertanya:
  1. *"Apa poin keberatan terbesar yang diajukan oleh Tim Keuangan terkait anggaran proyek ini?"*
  2. *"Apakah nama saya disebut dalam penugasan tugas baru?"*
  3. *"Buatkan tabel daftar tindak lanjut (Action Items) lengkap dengan nama PIC dan tenggat waktunya."*
Lo mendapatkan wawasan murni dari rapat 60 menit dalam waktu 90 detik membaca rangkuman.

#### 4. Syarah Kaidah 4: Kompresi dan Kalibrasi Nada Outlook
Kotak masuk email (*inbox*) adalah sumber stres mental tertinggi bagi pekerja kantoral. Sebuah perselisihan proyek antar divisi seringkali menghasilkan utas email (*email thread*) berisikan 30 balasan dengan lampiran yang bertumpuk-tumpuk, di mana setiap orang saling melempar tanggung jawab dengan bahasa pasif-agresif.

Copilot di Outlook menyajikan dua senjata pertahanan kognitif:
1. **Summary by Copilot:** Menghancurkan 30 utas email menjadi 3 butir padat: (a) Akar masalah awal, (b) Posisi terakhir masing-masing departemen, dan (c) Tindakan apa yang sedang ditunggu dari lo.
2. **Coaching by Copilot:** Ketika lo sedang marah dan mengetik draf email balasan yang penuh emosi, lo bisa meminta Copilot untuk melatih nada bicara lo (*Coaching*). Copilot menganalisis persepsi penerima: *"Draf Anda terkesan defensif dan menuduh. Pertimbangkan untuk merevisi kalimat paragraf kedua agar lebih berfokus pada solusi logistik bersama alih-alih menyalahkan keterlambatan vendor."*

---

### LAYER 4: FIELD PLAYBOOK (TACTICAL SOP & CODE)

#### SOP 1: Protokol Eksekusi Lintas Aplikasi (End-to-End Enterprise Sprint)
1. **Fase 1 (Excel):** Rapikan raw data transaksi menjadi Excel Table resmi (tekan `Ctrl + T`). Buka Copilot dan jalankan prompt kalkulasi margin.
2. **Fase 2 (Word):** Buat dokumen baru. Gunakan prompt: *"Draf ringkasan eksekutif 500 kata berdasarkan tabel performa penjualan di file Excel [Link SharePoint]."*
3. **Fase 3 (PowerPoint):** Buat dek slide dari file Word tersebut. Perintahkan: *"Gunakan gaya visual minimalis dengan maksimal 3 poin per slide dan sertakan speaker notes untuk presentasi 10 menit."*
4. **Fase 4 (Teams & Outlook):** Bagikan dek di obrolan tim Teams, minta Copilot merangkum masukan tim, lalu buat email konfirmasi akhir di Outlook dengan nada eksekutif resmi.

#### Template Prompt Produksi Verbatim untuk Masing-Masing Aplikasi M365

##### 1. Prompt Microsoft Excel (Financial & Anomaly Probing):
```text
Analisis tabel transaksi penjualan ini:
1. Tambahkan kolom baru yang menghitung persentase margin kotor: ([@Harga_Jual] - [@HPP]) / [@Harga_Jual].
2. Sorot dengan conditional formatting seluruh transaksi dengan margin di bawah 10%.
3. Tunjukkan 3 produk dengan rasio pengembalian barang (return rate) tertinggi bulan ini dan usulkan tindakan perbaikannya.
```

##### 2. Prompt Microsoft PowerPoint (Word-to-Deck Conversion):
```text
Buatkan presentasi 8 slide berdasarkan file Word 'Laporan_Evaluasi_Vendor_Logistik_2026.docx'.
Panduan Struktur Slide:
- Slide 1: Judul Eksekutif & Ringkasan Dampak Finansial
- Slide 2: Akar Masalah (Keterlambatan TOP & Selisih Tagihan 12%)
- Slide 3-4: Analisis Data Kinerja 5 Ekspedisi Terbesar
- Slide 5-6: Solusi Procurement Tersentral & Dashboard Pengawasan
- Slide 7: Rencana Transisi 30 Hari & Mitigasi Risiko
- Slide 8: Keputusan yang Dimohonkan kepada Direksi
Catatan: Buatkan naskah percakapan lisan lengkap pada kolom Speaker Notes di setiap slide.
```

##### 3. Prompt Microsoft Teams (Meeting Post-Mortem):
```text
Rangkum transkrip rapat mingguan ini:
1. Apa keputusan final terkait perubahan vendor ekspedisi?
2. Siapa yang menyatakan ketidaksetujuan dan apa argumen dasarnya?
3. Buatkan tabel Action Items dengan format: | No | Tugas Spesifik | PIC (Penanggung Jawab) | Deadline |
```

##### 4. Prompt Microsoft Outlook (Email Thread Synthesis & Coaching):
```text
Rangkum utas email ini dalam 3 kalimat padat. 
Kemudian drafkan balasan persetujuan anggaran dengan syarat:
- Vendor wajib menandatangani Service Level Agreement (SLA) ketepatan pengiriman 98%.
- Pembayaran tetap menggunakan termin 45 hari (TOP 45).
- Gunakan nada bicara yang tegas, ramah, namun tidak membuka ruang kompromi terkait denda keterlambatan.
```

#### Skrip Helper Otomasi Python: `m365_prompt_formatter.py`
Skrip Python mandiri untuk memformat parameter prompt lintas aplikasi secara terstruktur:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Microsoft 365 Copilot Prompt Orchestration Formatter
Menghasilkan payload prompt yang siap di-copy-paste ke Excel, Word, PPT, Teams, dan Outlook.
"""

def generate_cross_app_prompt_pack(project_name, source_file_url, target_kpi):
    pack = {
        "EXCEL": f"Analisis tabel di {project_name}. Hitung formula efisiensi untuk mencapai KPI: {target_kpi}.",
        "WORD": f"Tulis laporan operasional 3 halaman untuk {project_name} berbasis data file: {source_file_url}.",
        "POWERPOINT": f"Buat presentasi 8 slide eksekutif dari dokumen {source_file_url}. Wajib sertakan speaker notes.",
        "TEAMS": f"Ekstrak seluruh komitmen tugas dan tenggat waktu dari transkrip rapat {project_name}.",
        "OUTLOOK": f"Rangkum utas email terkait {project_name} dan buat draf balasan penegasan batas waktu {target_kpi}."
    }
    return pack

if __name__ == "__main__":
    print("[*] Menghasilkan Paket Prompt Orkestrasi M365 Copilot:")
    prompts = generate_cross_app_prompt_pack(
        project_name="Evaluasi Ekspedisi Logistik FAT 2026",
        source_file_url="https://tenant.sharepoint.com/sites/logistics/Evaluasi_Ekspedisi.docx",
        target_kpi="Efisiensi Biaya Kirim 15% & TOP 100%"
    )
    for app, prompt_text in prompts.items():
        print(f"\n[{app} PROMPT]:\n{prompt_text}")
```

---

### LAYER 5: DIAGNOSTIC DRILL (STUDI KASUS & UJI MANDIRI)

#### Skenario Kasus Lapangan
Direktur Keuangan (CFO) sebuah perusahaan ritel farmasi di Jakarta dijadwalkan menghadiri rapat dewan komisaris darurat dalam waktu 45 menit. CFO tersebut baru saja menerima file spreadsheet Excel berisikan 150.000 baris transaksi piutang macet dan keterlambatan pembayaran vendor (AP/AR) dari divisi akuntansi. 
Staf analis junior panik dan mencoba membuat slide presentasi manual satu per satu dari Excel tersebut. Pada menit ke-30, sang analis baru menyelesaikan 2 slide yang berantakan dengan tangkapan layar (*screenshot*) tabel yang buram dan tidak terbaca. CFO membutuhkan dek presentasi 5 slide yang merangkum masalah likuiditas kas, 3 vendor paling bermasalah, dan rekomendasi perbaikan sebelum rapat dimulai.

#### Lembar Uji Mandiri
1. Berdasarkan Kaidah 1 dan Kaidah 2, bagaimana alur orkestrasi 15 menit menggunakan Copilot di Excel, Word, dan PowerPoint untuk menyelesaikan krisis di atas?
2. Mengapa memasukkan tangkapan layar tabel spreadsheet buram ke slide presentasi dewan komisaris merupakan pelanggaran standar komunikasi eksekutif, dan bagaimana Copilot di PowerPoint mengatasi masalah ini?
3. Tuliskan prompt spesifik yang harus diketikkan oleh sang CFO di panel Copilot Excel untuk memunculkan 3 vendor paling bermasalah secara instan dari 150.000 baris data tersebut!

#### Kunci Jawaban Lengkap & Analisis Diagnostik
1. **Alur Orkestrasi 15 Menit Penyelamat Krisis:**
   - **Menit 0 - 5 (Excel):** Buka spreadsheet, minta Copilot: *"Identifikasi 3 vendor dengan total keterlambatan pembayaran AP tertinggi dan hitung rasio piutang macet AR > 90 hari. Buat tabel ringkasannya."*
   - **Menit 5 - 10 (Word):** Buka dokumen Word baru, minta Copilot: *"Tulis ringkasan eksekutif 1 halaman tentang risiko likuiditas kas dan 3 vendor paling kritis berdasarkan tabel ringkasan Excel tadi."* Simpan di OneDrive.
   - **Menit 10 - 15 (PowerPoint):** Buka PowerPoint, minta Copilot: *"Create presentation from file [Link Dokumen Word tadi]. Buatkan 5 slide eksekutif dengan struktur: Masalah Kas, Analisis 3 Vendor, Dampak Keterlambatan TOP, Rencana Remediasi Likuiditas, dan Permohonan Keputusan Komisaris."*
2. **Kekeliruan Screenshot Tabel Buram:** Dewan komisaris tidak memiliki waktu untuk menyipitkan mata membaca 20 kolom angka mikro. Presentasi eksekutif menuntut abstraksi level tinggi: grafik tren visual, metrik kerugian moneter tercetak tebal, dan kartu kesimpulan. Copilot di PowerPoint mengekstrak pesan moral dari angka-angka tersebut dan menampilkannya sebagai elemen infografis yang bersih, lengkap dengan narasi pembicara di Speaker Notes.
3. **Prompt Spesifik Copilot di Excel:**
   ```text
   Dari tabel data transaksi 150.000 baris ini:
   1. Filter data untuk transaksi dengan status keterlambatan > 60 hari.
   2. Kelompokkan berdasarkan Nama Vendor dan jumlahkan total nominal keterlambatan (SUM of Saldo_Hutang).
   3. Urutkan dari yang terbesar dan tampilkan tepat TOP 3 Vendor paling kritis dalam tabel ringkasan baru, lengkap dengan persentase kontribusinya terhadap total hutang macet perusahaan.
   ```
