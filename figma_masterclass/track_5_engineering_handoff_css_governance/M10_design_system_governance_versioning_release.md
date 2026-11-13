# Modul 10: Design System Governance, Versioning & Enterprise Release

> "Sistem desain bukan sebuah proyek sekali jadi yang selesai lalu ditinggalkan; sistem desain adalah produk internal jangka panjang yang membutuhkan tata kelola, versioning yang ketat, dan perjanjian level layanan (SLA) antar-divisi."

## Modul 10: Design System Governance, Versioning & Enterprise Release

---

### LAYER 1: KAIDAH EMAS (CORE AXIOMS)

1. **Tata Kelola Semantic Versioning (SemVer: MAJOR.MINOR.PATCH) Mengamankan Ekosistem dari Kerusakan Rilis Visual:**
   - *MAJOR:* Rilis perubahan yang merusak kompatibilitas (*breaking changes*), seperti menghapus varian, mengubah struktur API properti, atau mengubah nama token semantik.
   - *MINOR:* Penambahan fitur baru yang kompatibel ke belakang (*backward-compatible*), seperti merilis komponen baru atau menambah properti opsional.
   - *PATCH:* Perbaikan bug visual minor yang tidak mengubah kontrak fungsional (misal: perbaikan kontras warna 2% atau perataan teks 1px).
2. **Alur Kerja Branch & Merge di Figma Enterprise Mengisolasi Eksperimen dari Library Produksi Utama:** Library desain utama (*Main Branch*) harus berstatus terproteksi (*protected*). Desainer dilarang melakukan eksperimen atau modifikasi langsung pada file utama; setiap pembaruan wajib dibuat di dalam *Branch* terisolasi, melewati proses *Visual Diff Review*, dan di-merge hanya setelah disetujui oleh Design System Lead.
3. **Strategi Deprecated Mengizinkan Masa Transisi Bertahap Sebelum Sebuah Komponen Dihapus Permanen:** Menghapus komponen lama secara mendadak akan merusak ribuan artboard yang sedang aktif dikerjakan oleh tim produk. Komponen usang wajib melalui fase *Deprecation*: diberi awalan nama `[DEPRECATED]`, dipindahkan ke halaman arsip, dan diberikan masa tenggang (*sunset grace period*) minimal dua kuartal disertai dokumen panduan migrasi (*Migration Guide*).
4. **Paritas Dua Arah Antara Library Figma dan Repositori Kode (NPM Package / Storybook):** Sistem desain yang matang menjaga paritas 1-to-1 antara rilis library Figma dengan rilis paket kode di repositori engineering. Nama varian di Figma harus identik dengan nama props di React/Flutter, dan nomor versi rilis library desain harus berjalan selaras dengan nomor rilis paket NPM.
5. **Perjanjian Tingkat Layanan (SLA) Lintas-Fungsi Mengatur Eskalasi dan Permintaan Komponen Baru:** Tim sistem desain tidak boleh menjadi menara gading yang lambat merespons kebutuhan tim fitur. Wajib ada SLA yang jelas: tinjauan kontribusi komponen dari tim produk harus diselesaikan dalam maksimal 5 hari kerja, dan rilis perbaikan bug darurat (*hotfix patch*) wajib meluncur dalam 24 jam.

---

### LAYER 2: MENTAL MODEL & DIAGRAM ASCII

```text
[ENTERPRISE BRANCH & MERGE WORKFLOW IN FIGMA]
MAIN LIBRARY (❖ Protected) ───────────────────────────────────► MAIN (v2.1.0)
     │                                                           ▲
     │ Create Branch:                                            │ Merge Branch
     │ "feat/date-picker-v2"                                     │ (Visual Diff
     ▼                                                           │  Approved)
BRANCH WORKSPACE (Active Draft)                                  │
┌──────────────────────────────────────────────┐                 │
│ 1. Buat Komponen DatePicker Baru             │                 │
│ 2. Uji Stress-Test Auto Layout & Tokens      │                 │
│ 3. Minta Review ke Design System Lead ───────┼─────────────────┘
└──────────────────────────────────────────────┘

[SEMANTIC VERSIONING (SemVer) DECISION TREE]
APAKAH PERUBAHAN ANDA MERUSAK KOMPATIBILITAS SEBELUMNYA?
  │
  ├───► YA (Contoh: Menghapus properti, mengganti nama komponen)
  │     └───► RILIS MAJOR (v1.4.2 ──► v2.0.0) [Wajib Panduan Migrasi!]
  │
  └───► TIDAK
        │
        ├───► Apakah ada penambahan fitur/komponen baru?
        │     └───► YA  ──► RILIS MINOR (v1.4.2 ──► v1.5.0)
        │
        └───► TIDAK (Hanya perbaikan bug/warna/padding)
              └───► RILIS PATCH (v1.4.2 ──► v1.4.3)
```

Formula Identifikasi Perubahan Berbahaya (*Breaking Change Hazard*):
`Risk_Level = (Jumlah_File_Konsumen × Frekuensi_Penggunaan_Komponen) / Kelengkapan_Panduan_Migrasi`

---

### LAYER 3: SYARAH DAGING (DEEP DIVE KNOWLEDGE)

#### 1. Syarah Kaidah 1: Tata Kelola Semantic Versioning (SemVer: MAJOR.MINOR.PATCH) Mengamankan Ekosistem dari Kerusakan Rilis Visual
Salah satu momok terbesar bagi perusahaan yang memiliki puluhan desainer produk adalah tombol *Publish Library Update*. Di masa lalu, ketika desainer sistem menekan tombol publish tanpa disiplin versioning, 20 desainer produk lain di tim Checkout, Onboarding, dan Dashboard tiba-tiba menerima notifikasi update. Saat mereka mengklik "Update All", layout di file mereka berantakan: tombol yang sebelumnya memiliki ikon mendadak kehilangan teksnya, atau kartu meluap keluar layar.

Penerapan standar *Semantic Versioning* pada library desain memecahkan masalah ini:
- **Patch Release (v2.1.1):** Desainer sistem hanya memperbaiki nilai heksadesimal warna `neutral-700` agar lulus WCAG AAA, atau membetulkan deskripsi token. Desainer produk aman untuk langsung mengklik "Update All" tanpa khawatir layout mereka rusak.
- **Minor Release (v2.2.0):** Tim menambahkan komponen baru bernama `BannerAlert` dan menambahkan properti opsional `size = "xsmall"` pada komponen tombol lama. Komponen lama yang sudah ada di file desainer produk tidak akan terpengaruh sama sekali.
- **Major Release (v3.0.0):** Tim merombak arsitektur tombol dari 3 properti lama menjadi arsitektur baru. Desainer produk diinstruksikan untuk TIDAK mengupdate file secara otomatis; mereka wajib membaca *Migration Guide* dan mengupdate halaman per halaman secara terencana.

#### 2. Syarah Kaidah 2: Alur Kerja Branch & Merge di Figma Enterprise Mengisolasi Eksperimen dari Library Produksi Utama
Pada paket Figma Enterprise dan Organization, fitur *Branching* berfungsi persis seperti Git Branching dalam dunia rekayasa perangkat lunak:
- **Main File:** Adalah kode produksi yang sedang dikonsumsi oleh seluruh desainer perusahaan. File ini dilindungi hak aksesnya; hanya Design System Core Team yang memiliki wewenang merge.
- **Branch:** Ketika seorang desainer ingin menyusun komponen tabel baru yang kompleks, ia membuat cabang bernama `feat/datatable-v1`. Di dalam branch ini, ia bebas memodifikasi layer, menambahkan varian, dan menguji prototipe tanpa memengaruhi siapa pun di tim lain.
- **Review & Conflict Resolution:** Saat pekerjaan selesai, desainer mengajukan permintaan *Review Branch*. Figma menyediakan panel komparasi visual canggih (*Visual Diff*) yang menandai warna merah untuk elemen yang dihapus, warna hijau untuk elemen baru, dan warna kuning untuk modifikasi geometri. Jika ada konflik (misal desainer lain baru saja mengubah token yang sama di Main), Figma meminta pengguna memilih versi mana yang dipertahankan sebelum proses merge disahkan.

#### 3. Syarah Kaidah 3: Strategi Deprecated Mengizinkan Masa Transisi Bertahap Sebelum Sebuah Komponen Dihapus Permanen
Bayangkan sebuah bank dengan 50 fitur perbankan yang berbeda di Figma. Tim Design System memutuskan bahwa komponen `LegacyDropdown` sudah ketinggalan zaman dan harus digantikan oleh `SelectMenu` baru.
Jika tim Design System langsung menghapus `LegacyDropdown` dari file utama:
- Ribuan Instance di seluruh file produk akan mengalami eror *Missing Component*.
- Desainer produk tidak bisa lagi mengedit teks atau varian di file mereka.
- Terjadi kekacauan operasional dan kemarahan antar-tim.

Siklus Hidup Deprecasi yang Benar (*Graceful Deprecation Cycle*):
1. **Fase 1 (Soft Warning):** Ubah nama komponen menjadi `[DEPRECATED] LegacyDropdown`. Tambahkan pesan peringatan di deskripsi inspector: *"Komponen ini sudah usang. Gunakan SelectMenu baru untuk proyek baru. Hubungi #design-system-support jika ada pertanyaan."*
2. **Fase 2 (Documentation & Migration Script):** Terbitkan panduan migrasi visual yang menunjukkan padanan props lama ke props baru.
3. **Fase 3 (Sunset Grace Period):** Biarkan komponen tersebut tetap ada selama minimal dua kuartal bisnis (6 bulan) untuk memberi waktu bagi tim produk melakukan migrasi saat sprint refactoring.
4. **Fase 4 (Hard Removal):** Setelah audit memastikan bahwa jumlah penggunaan instance di analytics library sudah mendekati nol, komponen lama dapat dihapus permanen ke arsip.

#### 4. Syarah Kaidah 4: Paritas Dua Arah Antara Library Figma dan Repositori Kode (NPM Package / Storybook)
Musuh terbesar efisiensi organisasi adalah terjadinya "Divergensi Sistem": di mana desainer menyebut sebuah komponen sebagai `ModalDialog` dengan varian `type = "danger"`, sementara developer di repositori React menyebut komponen yang sama sebagai `<AlertModal variant="destructive" />`.

Ketika nama props dan hierarki tidak sinkron:
- Setiap pertemuan hand-off dipenuhi dengan perdebatan kosakata dan salah paham.
- Dokumentasi tim tidak berguna karena kedua divisi menggunakan kamus yang berbeda.
- Otomatisasi pengujian desain-ke-kode menjadi mustahil dibangun.

Tim sistem desain modern memelihara dokumen kamus nama yang tersinkronisasi (*Design-Code Parity Matrix*). Rilis versi library Figma dan paket kode NPM dilakukan secara tandem: jika library Figma merilis `v2.4.0`, tim front-end engineering juga merilis paket `@company/ui-kit@2.4.0` dengan struktur API yang identik.

#### 5. Syarah Kaidah 5: Perjanjian Tingkat Layanan (SLA) Lintas-Fungsi Mengatur Eskalasi dan Permintaan Komponen Baru
Banyak sistem desain gagal diadopsi oleh organisasi karena tim sistem desain bertindak seperti birokrasi yang lambat: ketika seorang desainer produk membutuhkan komponen baru untuk rilis fitur minggu depan, permohonannya membutuhkan waktu 2 bulan untuk diproses oleh tim desain sistem. Akibatnya, desainer produk frustrasi, melakukan detach component, dan mendesain komponen sendiri secara liar.

SLA Sistem Desain yang Efektif:
- **Triage Permintaan Baru (Maksimal 48 Jam):** Tim sistem desain wajib meninjau tiket permohonan komponen baru dalam waktu 2 hari kerja: apakah kebutuhan ini unik untuk fitur tersebut (cukup dibuat komponen lokal), atau bermanfaat untuk seluruh organisasi (dijadikan komponen global).
- **Rilis Kontribusi dari Tim Produk (*Federated Model*):** Jika tim produk bersedia membuat komponennya sendiri sesuai standar token dan Auto Layout yang benar, tim sistem desain bertindak sebagai *code reviewer* yang memvalidasi branch tersebut dalam maksimal 5 hari kerja.
- **Rilis Patch Darurat (Maksimal 24 Jam):** Bug kritis yang memblokir rilis developer wajib dirilis sebagai hotfix patch dalam 1 hari kerja.

---

### LAYER 4: FIELD PLAYBOOK (TACTICAL SOP & TEMPLATES)

#### Template Catatan Rilis Library Desain (Changelog Template)

```markdown
# Design System Release Notes: v2.3.0 (Minor Release)
*Tanggal Rilis:* 13 November 2026
*Status Kompatibilitas:* Backward-Compatible (Aman untuk Update All)

### 🚀 Komponen Baru (New Components)
- **DatePicker (❖ DatePicker):** Komponen pemilih tanggal kalender responsif lengkap dengan mode Rentang Tanggal (Date Range) dan Token Variabel multi-brand.
- **ToastNotification (❖ ToastNotification):** Komponen umpan balik mengambang dengan 4 varian status (Success, Info, Warning, Error).

### 🛠️ Peningkatan & Perbaikan Bug (Fixes & Polish)
- **Button:** Memperbaiki rasio kontras pada varian `Ghost` status `Hover` untuk memenuhi kriteria WCAG 2.1 AAA (Kontras naik dari 3.8:1 menjadi 7.2:1).
- **InputText:** Memperbaiki bug padding vertikal yang sebelumnya melompat 1px saat pesan error aktif.

### ⚠️ Pemberitahuan Deprecasi (Deprecation Notice)
- Komponen `❖ OldCalendar` resmi ditandai sebagai `[DEPRECATED] OldCalendar`.
- Silakan gunakan `❖ DatePicker` baru untuk proyek baru. Komponen lama akan dihentikan dukungannya pada rilis v3.0.0 (Q2 2027).
- [Buka Panduan Migrasi Kalender di Notion](https://notion.so/company/migration-datepicker)
```

#### SOP Pengajuan Branch Baru di Figma:
1. Buka file library utama. Klik chevron dropdown di samping judul file > **Create branch**.
2. Beri nama branch dengan format konvensi:
   - Fitur baru: `feat/nama-komponen`
   - Perbaikan bug: `fix/nama-isu`
   - Eksperimen: `exp/eksplorasi-topik`
3. Lakukan modifikasi desain dengan disiplin Auto Layout dan token variabel resmi.
4. Uji komponen pada kanvas kosong (stress test teks panjang, resizing, dark mode).
5. Klik **Request review**. Tulis ringkasan perubahan pada kotak deskripsi dan tag akun reviewer utama.
6. Setelah disetujui, klik **Merge branch** dan publikasikan perubahan dengan menyertakan nomor versi SemVer yang tepat.

---

### LAYER 5: DIAGNOSTIC DRILL (STUDI KASUS & UJI MANDIRI)

#### Skenario Kasus Nyata
Di sebuah perusahaan fintech dengan 120 desainer dan developer, tim Design System baru saja merilis pembaruan library besar-besaran:
- Mereka mengubah nama properti pada komponen tombol dari `Style` (Primary, Secondary) menjadi `Variant` (Filled, Outlined).
- Mereka menghapus properti boolean `hasIcon` dan menggantinya dengan struktur baru.
- Tanpa peringatan atau pengumuman changelog, sang lead menekan tombol *Publish Update* pada hari Kamis sore jam 17.00.

Keesokan paginya:
1. Ratusan file produk yang sedang aktif dikerjakan oleh tim mobile banking mengalami error massal: tombol kehilangan warna dan ikonnya terlempar keluar frame.
2. Tim QA memblokir jadwal rilis aplikasi ke Google Play Store karena antarmuka hancur saat diuji.
3. Manajemen senior marah dan menuntut penyelidikan darurat atas kegagalan rilis tersebut.

#### Lembar Uji Mandiri (3 Pertanyaan Kritis)
1. Tiga pelanggaran protokol tata kelola (*governance violations*) apa yang dilakukan oleh tim Design System dalam kasus tersebut?
2. Berdasarkan standar *Semantic Versioning*, jenis rilis apa yang seharusnya ditetapkan untuk pembaruan tombol tersebut, dan bagaimana prosedur mitigasi risikonya?
3. Rancang prosedur rilis standar (*Standard Operating Procedure*) anti-bencana untuk mencegah terulangnya insiden rilis fatal tersebut!

#### Kunci Jawaban Lengkap & Analisis Anti-Pattern

1. **Tiga Pelanggaran Protokol Tata Kelola Berat:**
   - **Melanggar Kompatibilitas SemVer (Uncontrolled Breaking Change):** Mengubah nama properti (`Style` → `Variant`) dan menghapus properti `hasIcon` adalah *Breaking Change* tingkat tinggi. Ketika properti diganti namanya, engine Figma memutus relasi override teks dan warna pada seluruh instance yang sudah ada.
   - **Zero Communication & Missing Changelog:** Merilis perubahan struktural tanpa catatan rilis (*changelog*), tanpa panduan migrasi, dan tanpa pemberitahuan di kanal komunikasi tim.
   - **Pelanggaran Waktu Rilis (Thursday Afternoon Deploy):** Merilis pembaruan kritis pada sore hari menjelang akhir pekan (*Friday Deployment Anti-Pattern*) tanpa menyisakan waktu untuk menangani regresi darurat.
2. **Penetapan SemVer & Prosedur Mitigasi Risiko:**
   - Perubahan ini wajib diklasifikasikan sebagai **MAJOR RELEASE (misal: v2.0.0)**.
   - **Prosedur Mitigasi:**
     - Jangan langsung menghapus properti lama.
     - Tambahkan komponen tombol baru di samping komponen tombol lama, beri tanda tombol lama sebagai `[DEPRECATED] Button v1` dan tombol baru sebagai `Button v2`.
     - Dengan cara ini, file produk yang sudah ada tetap aman dan stabil 100%. Tim produk diberi waktu berminggu-minggu untuk memigrasikan tombol mereka ke versi baru saat waktu luang sprint.
3. **SOP Rilis Anti-Bencana untuk Enterprise:**
   - **Aturan Golden Window Rilis:** Rilis library publik HANYA diizinkan pada hari Selasa atau Rabu pagi (pukul 10.00 - 12.00) agar tim pendukung siaga penuh membantu jika terjadi isu regresi.
   - **Kewajiban Branch Review:** Setiap rilis wajib melalui pengujian *Canary Testing* (diuji terlebih dahulu pada 2 file proyek uji coba nyata untuk melihat apakah update memicu kerusakan layout).
   - **Rilis Catatan Terbuka:** Tombol publish HANYA boleh ditekan setelah dokumen catatan rilis dan panduan migrasi terbit di Notion/Slack.
   - **Pencegahan Breaking Change:** Perubahan nama properti pada komponen inti dilarang keras dilakukan secara mendadak; wajib melalui masa transisi deprecation minimal 2 kuartal.
