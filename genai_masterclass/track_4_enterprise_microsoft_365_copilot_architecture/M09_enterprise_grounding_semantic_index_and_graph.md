# MICROSOFT GENERATIVE AI & COPILOT PROFESSIONAL OS — TRACK 4
## Modul 09: Enterprise Grounding, Semantic Index & Microsoft Graph Mechanics
> **Sumber Utama:** *Learning Microsoft 365 Copilot for Work (Jess Stratton)* & *Microsoft 365 Copilot Architecture & Security Foundations*.  
> **Target Kompetensi:** Menguasai arsitektur aliran data enterprise pada Microsoft 365 Copilot, memahami peran Microsoft Graph sebagai jembatan konteks, mendalami Semantic Indexing, dan menegakkan protokol keamanan data internal (RBAC & Zero Data Leakage).

---

### LAYER 1: KAIDAH EMAS (CORE AXIOMS)

1. **Aksioma Jembatan Graf Perusahaan (The Microsoft Graph Context Bus):**
   Copilot tidak berbicara langsung dengan model bahasa besar (LLM) secara mentah. Setiap prompt pengguna terlebih dahulu diintersepsi dan dikirim ke **Microsoft Graph** untuk dipasangkan dengan konteks personal kerja pengguna: email Outlook yang belum dibaca, lampiran dokumen Word di OneDrive, riwayat obrolan Teams, dan jadwal rapat kalender. Tanpa Microsoft Graph, Copilot hanyalah LLM publik biasa yang buta terhadap konteks bisnis internal lo.

2. **Indeksasi Semantik Berbasis Vektor (Semantic Index for Copilot Principle):**
   Pencarian data perusahaan pada era modern tidak lagi mengandalkan pencocokan teks biasa (*keyword index*). **Semantic Index for Copilot** membuat peta vektor konseptual dari seluruh data organisasi. Ini memungkinkan Copilot menemukan dokumen relevan meskipun pengguna tidak mengingat judul file yang tepat (misal: mencari *"kebijakan kerja dari rumah"* akan langsung menemukan dokumen berjudul *"SOP Fleksibilitas Operasional Pasca-Pandemi.docx"*).

3. **Batas Isolasi Tenant dan Privasi Mutlak (The Anti-Training Invariant):**
   Seluruh interaksi data perusahaan yang diproses oleh Microsoft 365 Copilot berada di dalam batas kepatuhan keamanan (*security & compliance boundary*) penyewa (*tenant*) organisasi lo. Data prompt, riwayat dokumen bisnis, dan respons model **DIJAMIN SECARA YURIDIS & TEKNIS TIDAK PERNAH DIGUNAKAN** untuk melatih (*train*) atau menyempurnakan (*fine-tune*) model dasar OpenAI publik.

4. **Penegakan Hak Akses Warisan (Inherited RBAC Access Enforcement):**
   Copilot menghormati 100% kontrol akses berbasis peran (*Role-Based Access Control / RBAC*) yang sudah ada di Azure Active Directory (Entra ID). Copilot tidak pernah bisa membocorkan slip gaji direksi atau data rahasia merger kepada staf junior, karena sistem hanya dapat membaca dokumen yang secara eksplisit telah diizinkan untuk dibuka oleh akun pengguna yang bersangkutan.

---

### LAYER 2: MENTAL MODEL & DIAGRAM ASCII

```text
========================================================================================
            ALUR KERJA PRE-GROUNDING & POST-PROCESSING MICROSOFT 365 COPILOT
========================================================================================

    [ USER INPUT DALAM APLIKASI ]
    (Word / Teams / Excel / Outlook)
                 │
                 ▼ (1. Kirim Prompt)
    ┌───────────────────────────────────────────────┐
    │          MICROSOFT 365 COPILOT ENGINE         │
    └───────────────────────┬───────────────────────┘
                            │
                            ▼ (2. Pre-Grounding Request)
    ┌───────────────────────────────────────────────┐
    │               MICROSOFT GRAPH                 │ ◄── [ ENTRA ID / RBAC GUARD ]
    │  - Semantic Index (Pencarian Vektor)          │     (Hanya ambil file yang punya
    │  - Email, Obrolan Teams, Kalender, OneDrive   │      izin akses resmi untuk User!)
    └───────────────────────┬───────────────────────┘
                            │
                            ▼ (3. Prompt Terkayakan + Konteks Bisnis)
    ┌───────────────────────────────────────────────┐
    │     LLM DALAM PERIMETER AMAN ENTERPRISE       │
    │  - Berada di Tenant Boundary Tertutup         │
    │  - Zero Data Logging untuk Training Publik    │
    └───────────────────────┬───────────────────────┘
                            │
                            ▼ (4. Draf Respons Mentah)
    ┌───────────────────────────────────────────────┐
    │ POST-PROCESSING & COMPLIANCE FILTER           │
    │  - Pengecekan Kebocoran Data Sensitif (DLP)   │
    │  - Validasi Keamanan Hak Cipta & Keandalan    │
    └───────────────────────┬───────────────────────┘
                            │
                            ▼ (5. Respons Dikirimkan)
    [ OUTPUT BERSIH DITAMPILKAN DI APLIKASI KERJA ]
========================================================================================
Prinsip Keamanan Inti:
Konteks_Akses_Copilot ⊆ Hak_Akses_Aktif_Pengguna(Entra_ID)
(Copilot tidak memiliki hak istimewa melebihi izin login akun pengguna itu sendiri).
========================================================================================
```

---

### LAYER 3: SYARAH DAGING (DEEP DIVE KNOWLEDGE)

#### 1. Syarah Kaidah 1: Aksioma Jembatan Graf Perusahaan (The Microsoft Graph)
Ketika lo bekerja di perusahaan besar, informasi tidak pernah tersimpan di satu tempat. Catatan kesepakatan harga ada di pesan obrolan Teams, draf proposal ada di dokumen Word SharePoint, jadwal peluncuran ada di kalender Outlook, dan lampiran spesifikasi teknis ada di email.

Jika seorang manajer mengetik ke ChatGPT publik: *"Tolong siapkan ringkasan untuk rapat jam 2 siang nanti dengan Vendor Logistik PT Sinar Roda Utama"*, ChatGPT publik akan menyerah karena tidak memiliki akses ke dunia kerja lo.

Di sinilah peran revolusioner **Microsoft Graph**:
- Microsoft Graph adalah jaring saraf terpadu yang memetakan hubungan antara orang (*people*), dokumen (*files*), percakapan (*conversations*), dan jadwal rapat (*meetings*).
- Saat lo memberikan prompt di atas ke Copilot, Copilot tidak langsung mengirimkannya ke model bahasa. Copilot terlebih dahulu melakukan kueri ke Microsoft Graph untuk mengambil:
  1. Undangan rapat kalender jam 14:00 (mengekstrak nama vendor dan agenda).
  2. Utas email terakhir dari vendor tersebut (mengekstrak lampiran tarif pengiriman).
  3. Catatan risalah dari rapat Teams minggu lalu.
- Data kontekstual ini digabungkan (*pre-grounding*) dengan prompt lo, barulah diumpankan ke LLM untuk dirangkum menjadi satu halaman ringkasan eksekutif yang sempurna.

#### 2. Syarah Kaidah 2: Indeksasi Semantik Berbasis Vektor (Semantic Index)
Sebelum era Copilot, jika lo lupa nama dokumen yang disimpan di server kantor, lo harus mengingat kata kunci yang tepat. Jika file lo bernama `Strategi_Efisiensi_Biaya_2026.docx` dan lo mencari kata `Penghematan Pengeluaran`, search engine Windows tradisional seringkali tidak menemukan apa pun.

**Semantic Index for Copilot** memecahkan masalah ini dengan mengubah setiap paragraf dokumen, email, dan obrolan menjadi **vektor embedding** (deretan ratusan angka floating-point yang merepresentasikan konsep makna di ruang multidimensi):
- Konsep "Efisiensi Biaya" dan "Penghematan Pengeluaran" memiliki koordinat vektor yang sangat berdekatan di ruang laten.
- Semantic Index bekerja pada dua tingkatan:
  1. **User-Level Index:** Memetakan data kerja personal lo (dokumen yang paling sering lo buka, rekan kerja yang paling sering lo ajak bicara, dan email lo).
  2. **Company-Level Index:** Memetakan seluruh repositori SharePoint publik perusahaan yang diizinkan untuk diakses seluruh karyawan.
Hasilnya, Copilot mampu menarik dokumen yang lo maksud dalam hitungan milidetik meskipun lo hanya memberikan deskripsi samar-samar.

#### 3. Syarah Kaidah 3: Batas Isolasi Tenant dan Privasi Mutlak
Kekhawatiran terbesar direksi perusahaan dan penasihat hukum (*General Counsel*) saat mengadopsi AI generatif adalah: *"Apakah rahasia dagang, formula kimia, atau laporan keuangan kami akan bocor ke kompetitor atau dipakai melatih model AI publik?"*

Microsoft menyelesaikan ketakutan ini melalui arsitektur **Enterprise Tenant Boundary**:
- Setiap organisasi yang berlangganan Microsoft 365 memiliki partisi penyewa (*tenant*) tersendiri yang terisolasi secara kriptografis di pusat data cloud.
- Panggilan API ke model bahasa besar (seperti GPT-4o) dieksekusi di dalam instans Azure OpenAI Service yang didedikasikan secara privat.
- **Kebijakan Nol Retensi untuk Pelatihan:** Microsoft dan OpenAI secara kontraktual terikat perjanjian bahwa data prompt, data grounding dari Graph, maupun respons yang dihasilkan TIDAK PERNAH disimpan di log publik dan TIDAK AKAN PERNAH digunakan untuk melatih kembali bobot model dasar (*never used for foundational model re-training*). Rahasia perusahaan lo tetap 100% milik lo.

#### 4. Syarah Kaidah 4: Penegakan Hak Akses Warisan (Inherited RBAC)
Bayangkan seorang staf magang baru di divisi pemasaran bertanya kepada Copilot di aplikasi Teams: *"Berapa bonus akhir tahun dan gaji pokok seluruh direksi perusahaan tahun ini?"*

Apakah Copilot akan menjawab pertanyaan tersebut? **TIDAK AKAN PERNAH.**
Copilot beroperasi di bawah prinsip **Least Privilege Enforcement**:
- Copilot mewarisi izin keamanan akun Microsoft Entra ID (dulu Azure AD) dari pengguna yang sedang login.
- Sebelum Microsoft Graph mengambil data untuk proses pre-grounding, Graph memeriksa hak akses dokumen di SharePoint/OneDrive.
- Karena dokumen penggajian direksi berada di folder dengan pembatasan hak akses (*restricted ACL*) yang hanya bisa dibuka oleh Direktur Keuangan dan HRD, Graph memfilter dokumen tersebut dari hasil pencarian staf magang. Copilot akan menjawab: *"Saya tidak dapat menemukan informasi terkait penggajian tersebut di dokumen yang Anda miliki aksesnya."* 

Copilot tidak menciptakan lubang keamanan baru; ia mematuhi struktur tata kelola dokumen yang sudah lo bangun di perusahaan.

---

### LAYER 4: FIELD PLAYBOOK (TACTICAL SOP & CODE)

#### SOP 1: Protokol Kesiapan Data Perusahaan Pra-Aktivasi Copilot
1. **Audit Kebocoran Izin SharePoint (Over-Sharing Audit):** Periksa tautan "Anyone with the link" atau folder perusahaan yang tidak sengaja disetel ke akses "Everyone in the company".
2. **Terapkan Label Sensitivitas Microsoft Purview:** Pasang label klasifikasi otomatis pada dokumen rahasia (`Highly Confidential - Finance`), sehingga Copilot secara otomatis menerapkan enkripsi dan pelindungan pencegahan kebocoran data (*Data Loss Prevention / DLP*).
3. **Standarisasi Penamaan dan Metadata Dokumen:** Pastikan dokumen penting memiliki judul deskriptif dan tag metadata proyek agar Semantic Index dapat memprioritaskan dokumen versi final di atas draf usang.

#### Skrip Implementasi Python: `graph_rbac_simulator.py`
Skrip Python mandiri yang mensimulasikan mekanisme filter izin akses warisan (*RBAC Filtering*) pada Microsoft Graph:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Microsoft Graph & RBAC Security Boundary Simulator
Mendemonstrasikan logika bagaimana Copilot memfilter dokumen perusahaan
berdasarkan profil izin login pengguna (Role-Based Access Control).
"""

import json

# Database Dokumen Perusahaan di SharePoint / OneDrive
COMPANY_KNOWLEDGE_BASE = [
    {
        "doc_id": "DOC_01",
        "title": "Pedoman Jam Kerja & Cuti Tahunan 2026.docx",
        "content": "Karyawan berhak atas cuti tahunan 12 hari kerja setelah masa kerja 1 tahun.",
        "allowed_roles": ["INTERN", "STAFF", "MANAGER", "DIRECTOR"]
    },
    {
        "doc_id": "DOC_02",
        "title": "Alokasi Anggaran Belanja IT & Server Cloud Q4.xlsx",
        "content": "Total anggaran cloud AWS dan Azure Q4 adalah Rp450.000.000.",
        "allowed_roles": ["MANAGER", "DIRECTOR"]
    },
    {
        "doc_id": "DOC_03",
        "title": "Rencana Restrukturisasi Organisasi & Gaji Direksi.pdf",
        "content": "Penyesuaian kompensasi eksekutif dan opsi saham kuartal 4.",
        "allowed_roles": ["DIRECTOR"]
    }
]

def simulate_copilot_graph_grounding(user_role, user_prompt):
    """
    Simulasi pemfilteran Microsoft Graph: Hanya dokumen yang diizinkan untuk
    user_role yang boleh dimasukkan ke dalam konteks grounding LLM.
    """
    print(f"\n[*] Mengotentikasi Sesi Copilot untuk Peran: [{user_role}]")
    print(f"[*] Prompt Pengguna: '{user_prompt}'")
    
    accessible_docs = []
    blocked_docs = []
    
    for doc in COMPANY_KNOWLEDGE_BASE:
        if user_role in doc["allowed_roles"]:
            accessible_docs.append(doc)
        else:
            blocked_docs.append(doc["title"])
            
    print(f"[-] Dokumen yang diblokir oleh RBAC ({len(blocked_docs)}): {blocked_docs}")
    print(f"[+] Dokumen yang diizinkan untuk Grounding ({len(accessible_docs)}): {[d['title'] for d in accessible_docs]}")
    
    # Sintesis Jawaban Berdasarkan Hak Akses
    if "gaji" in user_prompt.lower() or "direksi" in user_prompt.lower():
        if user_role == "DIRECTOR":
            return "Respons Copilot: Berdasarkan 'DOC_03', penyesuaian kompensasi eksekutif mencakup opsi saham kuartal 4."
        else:
            return "Respons Copilot: Maaf, saya tidak menemukan informasi terkait kompensasi direksi pada dokumen yang Anda miliki izin aksesnya."
            
    return f"Respons Copilot: Informasi berhasil dirangkum dari {len(accessible_docs)} dokumen publik perusahaan."

if __name__ == "__main__":
    prompt = "Berapa anggaran gaji direksi dan rencana restrukturisasi?"
    
    # Uji Coba 1: Akun Staf Magang (Intern)
    res_intern = simulate_copilot_graph_grounding("INTERN", prompt)
    print(f"[>] {res_intern}")
    
    # Uji Coba 2: Akun Direktur (Director)
    res_director = simulate_copilot_graph_grounding("DIRECTOR", prompt)
    print(f"[>] {res_director}")
```

---

### LAYER 5: DIAGNOSTIC DRILL (STUDI KASUS & UJI MANDIRI)

#### Skenario Kasus Lapangan
Sebuah firma konsultan hukum di Jakarta Selatan menguji coba pemasangan Microsoft 365 Copilot untuk 200 karyawannya. Kepala Keamanan Informasi (CISO) mengeluhkan bahwa salah seorang staf paralegal magang berhasil mendapatkan ringkasan rahasia dokumen akuisisi bank yang bernilai triliunan rupiah hanya dengan mengetik: *"Copilot, rangkumkan kesepakatan akuisisi perbankan terbesar yang sedang ditangani kantor kita bulan ini."*
CISO langsung menuduh bahwa sistem Microsoft 365 Copilot memiliki celah keamanan (*vulnerability*) fatal karena membocorkan dokumen rahasia kepada pihak yang tidak berhak. Namun saat tim audit internal Microsoft memeriksa repositori SharePoint firma tersebut, ditemukan bahwa berkas akuisisi tersebut disimpan oleh salah satu partner senior di folder "General Knowledge / Shared Files" yang hak aksesnya disetel ke *"Anyone inside the company can read and edit"*.

#### Lembar Uji Mandiri
1. Berdasarkan Kaidah 4 (Penegakan Hak Akses Warisan), mengapa tuduhan CISO bahwa Copilot mengalami kebocoran sistem adalah salah kaprah?
2. Bagaimana mekanisme kerja Microsoft Graph saat paralegal magang mengetik prompt tersebut di atas?
3. Langkah tata kelola keamanan apa (*data remediation protocol*) yang harus segera dieksekusi oleh tim IT firma hukum tersebut untuk mengamankan seluruh dokumen sensitif?

#### Kunci Jawaban Lengkap & Analisis Diagnostik
1. **Kesalahan Tuduhan CISO:** Copilot tidak mengalami kegagalan sistem. Copilot mematuhi prinsip *Inherited RBAC Enforcement*: sistem hanya membaca dan merangkum dokumen yang secara sah dapat dibuka oleh akun paralegal tersebut. Kegagalan keamanan terletak pada **kesalahan tata kelola manusia (Human Over-Sharing Error)**: partner senior ceroboh dengan menaruh berkas rahasia di folder umum perusahaan dengan izin terbuka untuk seluruh karyawan.
2. **Mekanisme Microsoft Graph:** Saat paralegal magang memasukkan prompt, Microsoft Graph melakukan pencarian vektor di Semantic Index untuk dokumen yang relevan dengan kata "akuisisi perbankan". Graph memeriksa hak akses akun paralegal terhadap berkas yang ditemukan. Karena berkas diletakkan di folder umum dengan izin "Everyone in the company", Graph mengidentifikasi dokumen tersebut sebagai dokumen yang sah untuk dibaca oleh paralegal, lalu menyuapkannya ke dalam konteks LLM untuk dirangkum.
3. **Protokol Remediasi Tata Kelola Keamanan:**
   - **Karantina Hak Akses Folder:** Segera ubah izin akses folder proyek akuisisi di SharePoint dari publik perusahaan menjadi *Restricted Security Group* yang hanya beranggotakan tim partner yang ditunjuk.
   - **Deploy Microsoft Purview Sensitivity Labels:** Terapkan pelabelan dokumen otomatis dengan enkripsi hak akses (misal: label `Confidential - M&A Team Only`). Dokumen berlabel ini secara otomatis tidak akan pernah bisa diindeks atau dibaca oleh Copilot jika akun pengguna bukan anggota grup resmi.
   - **Jalankan Access Review Audit Rutin:** Gunakan dashboard Microsoft Entra ID untuk mengaudit secara berkala folder-folder SharePoint yang memiliki izin akses terbuka terlalu longgar (*over-privileged sites*).
