# Modul 08: Interactive Components, Nested Flows & State Machines

> "Ketika interaktivitas dienkapsulasi langsung di dalam komponen, setiap instance yang ditarik ke kanvas otomatis hidup dan responsif tanpa membutuhkan kabel navigasi sehelai pun."

## Modul 08: Interactive Components, Nested Flows & State Machines

---

### LAYER 1: KAIDAH EMAS (CORE AXIOMS)

1. **Enkapsulasi Interaktivitas Komponen (Component-Level State Machine) Menjamin Reusabilitas Otomatis di Seluruh Artboard:** Menghubungkan interaksi antar-varian langsung di dalam *Component Set* (misal: Varian `Off` beralih ke `On` saat *On click*) membuat setiap *Instance* komponen tersebut di halaman mana pun langsung interaktif secara native tanpa perlu disambungkan ke layar lain.
2. **Prinsip State Machine Ortogonal: Komponen Hanya Boleh Memiliki Satu State Aktif pada Satu Waktu:** Status interaktif antarmuka (Default, Hover, Focused, Pressed, Disabled) bersifat deterministik dan saling meniadakan (*mutually exclusive*). Transisi antar-status harus memiliki pemicu (*trigger*) dan jalur kembali (*exit path*) yang jelas (seperti *Mouse enter* menuju Hover, dan *Mouse leave* kembali ke Default).
3. **Penyusunan Alur Bersarang (Nested Interactive States) Mengisolasi Kompleksitas Tanpa Mengotori Layar Induk:** Komponen interaktif tingkat rendah (seperti checkbox atau toggle) dapat disematkan di dalam komponen interaktif tingkat tinggi (seperti modal dialog atau form card) tanpa merusak memori rendering prototipe, beroperasi persis seperti pohon komponen React yang mandiri.
4. **Pola Progressive Disclosure Meminimalkan Beban Kognitif dengan Membuka Informasi Bertahap:** Interaksi mikro seperti akordeon, expandable cards, dan bottom sheets memanfaatkan transisi status tinggi dinamis (*Hug Contents* dengan Smart Animate) untuk menyembunyikan detail sekunder sampai pengguna secara eksplisit memintanya.
5. **Indikator Status Aksesibilitas (Focus & Disabled States) Wajib Disediakan Bersamaan dengan Status Visual Interaktif:** Sebuah komponen interaktif belum lengkap jika hanya memiliki status Hover dan Active; status *Keyboard Focus* (garis luar kontras tinggi 2px) dan status *Disabled* (opasitas redup dan pembatalan pointer events) wajib dibangun untuk memenuhi standar usabilitas dan aksesibilitas inklusif.

---

### LAYER 2: MENTAL MODEL & DIAGRAM ASCII

```text
[INTERACTIVE COMPONENT STATE MACHINE: TOGGLE SWITCH]
┌─────────────────────────────────────────────────────────────┐
│ ❖ Component Set: ToggleSwitch                               │
│                                                             │
│   ┌─────────────────────┐                                   │
│   │ Varian: State = Off │                                   │
│   │ [ ●       ]         │ ────┐                             │
│   └─────────────────────┘     │ Trigger: On Click           │
│              ▲                │ Action: Change to           │
│              │ Trigger:       │ Anim: Smart Animate (200ms) │
│              │ On Click       │                             │
│              └────────────────┼────────┐                    │
│                               ▼        │                    │
│   ┌─────────────────────┐              │                    │
│   │ Varian: State = On  │ ◄────────────┘                    │
│   │ [       ● ]         │                                   │
│   └─────────────────────┘                                   │
└─────────────────────────────────────────────────────────────┘
  Ketika ❖ ToggleSwitch ditarik ke 100 Artboard berbeda,
  seluruh 100 Instance otomatis bisa diklik on/off tanpa kabel kanvas!

[PROGRESSIVE DISCLOSURE: ACCORDION EXPANSION MECHANICS]
COLLAPSED STATE (H: 56px, Hug V)         EXPANDED STATE (H: 140px, Hug V)
┌──────────────────────────────┐         ┌──────────────────────────────┐
│ Judul FAQ              [ v ] │ ──────► │ Judul FAQ              [ ^ ] │
└──────────────────────────────┘  Smart  │ ──────────────────────────── │
(Sub-teks: Opacity 0%, Hidden)   Animate │ Teks jawaban penjelasan yang │
                                 (250ms) │ lengkap muncul mulus,        │
                                         │ mendorong konten bawahnya!   │
                                         └──────────────────────────────┘
```

Formula State Machine Deterministik:
`State_Next = f(State_Current, Event_Trigger)`

---

### LAYER 3: SYARAH DAGING (DEEP DIVE KNOWLEDGE)

#### 1. Syarah Kaidah 1: Enkapsulasi Interaktivitas Komponen (Component-Level State Machine) Menjamin Reusabilitas Otomatis di Seluruh Artboard
Sebelum fitur *Interactive Components* dirilis, mendesain formulir dengan 5 switch toggle adalah siksaan prototipe:
Setiap toggle memiliki 2 kemungkinan (On/Off). Untuk membuat prototipe yang akurat di mana pengguna bisa mengklik toggle mana pun secara bebas, desainer harus membuat:
2^5 = **32 artboard layar penuh**!
Hanya untuk 5 buah tombol sakelar kecil.

Dengan *Interactive Components*:
1. Desainer membuka *Component Set* dari tombol switch di file Design System.
2. Tarik garis interaksi dari varian `Off` ke varian `On` dengan event: *On click > Change to: State=On > Smart Animate (150ms)*.
3. Tarik garis balik dari `On` ke `Off` dengan event: *On click > Change to: State=Off > Smart Animate (150ms)*.
4. Selesai! Interaktivitas telah ter-enkapsulasi di dalam Master Component.
Sekarang, masukkan 5 buah instance switch tersebut ke dalam satu layar formulir. Tanpa menarik satu kabel pun di kanvas formulir, kelima switch tersebut langsung bisa diklik hidup dan mati secara independen. Jumlah artboard terpangkas dari 32 menjadi **1 artboard tunggal**.

#### 2. Syarah Kaidah 2: Prinsip State Machine Ortogonal: Komponen Hanya Boleh Memiliki Satu State Aktif pada Satu Waktu
Dalam perancangan sistem interaksi, sebuah komponen antarmuka beroperasi persis seperti sebuah mesin status terbatas (*Finite State Machine* / FSM):
- **Default (Idle):** Status istirahat ketika tidak ada interaksi pengguna.
- **Hover:** Dipicu oleh kursor desktop yang melayang di atas batas bounding box elemen (*Mouse enter*). Bertujuan memberikan umpan balik mikro bahwa elemen ini dapat diklik (*affordance*).
- **Pressed (Active):** Dipicu saat tombol mouse atau jari pengguna menyentuh layar (*While pressing* atau *Touch down*). Ditandai dengan efek elevasi mengecil (*inset shadow*) atau pergeseran posisi 1-2px ke bawah untuk mensimulasikan sensasi tombol fisik yang ditekan.
- **Focused:** Status krusial bagi navigasi keyboard (pengguna menekan tombol `Tab`). Wajib menampilkan cincin fokus (*focus ring*) dengan kontras tinggi untuk aksesibilitas motorik.
- **Disabled:** Status di mana komponen tidak dapat berinteraksi karena prasyarat belum terpenuhi. Semua event pemicu dimatikan.

Komponen yang baik tidak melompati status; transisi harus mengalir dari Default → Hover → Pressed → Default secara mulus.

#### 3. Syarah Kaidah 3: Penyusunan Alur Bersarang (Nested Interactive States) Mengisolasi Kompleksitas Tanpa Mengotori Layar Induk
Arsitektur komponen modern mendukung *Hierarchical State Machines*. Anda dapat memiliki komponen interaktif di dalam komponen interaktif lainnya:
- Contoh: Komponen `Dropdown Menu`.
  - Di dalam `Dropdown Menu`, terdapat komponen anak `Dropdown Item`.
  - Setiap `Dropdown Item` memiliki interaktivitas internalnya sendiri: berubah warna saat di-hover (*Hover State*).
  - Keseluruhan `Dropdown Menu` memiliki interaktivitas sendiri: mengembang saat diklik (*Expand State*).
Engine prototipe Figma mengelola status lokal ini secara independen di memori runtime. Hover pada item tidak merusak posisi expand dari menu induknya, mencerminkan persis arsitektur *Component Composition* pada framework modern seperti React atau Vue.

#### 4. Syarah Kaidah 4: Pola Progressive Disclosure Meminimalkan Beban Kognitif dengan Membuka Informasi Bertahap
Prinsip *Progressive Disclosure* menyatakan bahwa antarmuka harus menyajikan hanya informasi yang esensial pada pandangan pertama, dan menunda penyajian informasi detail sampai pengguna membutuhkannya.
Penerapan paling klasik adalah komponen **Accordion FAQ**:
- **Status Tertutup (Collapsed):** Komponen diset berukuran tinggi kecil (misal: 56px) dengan padding vertikal 16px. Teks jawaban di dalamnya disembunyikan (*hidden / opacity 0%*).
- **Status Terbuka (Expanded):** Ketika judul diklik, komponen beralih ke varian Terbuka. Teks jawaban dimunculkan (*opacity 100%*). Karena komponen menggunakan Auto Layout dengan *Hug Contents* vertikal, tinggi frame secara otomatis bertambah (misal menjadi 140px).
Dengan menyambungkan kedua varian ini menggunakan *Smart Animate (Ease-Out, 250ms)*, accordion akan membuka dengan gerakan meluncur ke bawah yang halus, secara otomatis mendorong elemen-elemen di bawahnya tanpa ada teks yang terpotong.

#### 5. Syarah Kaidah 5: Indikator Status Aksesibilitas (Focus & Disabled States) Wajib Disediakan Bersamaan dengan Status Visual Interaktif
Banyak desainer hanya merancang status Default dan Hover karena mereka menguji desain hanya menggunakan mouse. Ini adalah bias desain yang mengabaikan jutaan pengguna disabilitas atau profesional yang mengandalkan navigasi keyboard murni.

Kriteria Kepatuhan Aksesibilitas:
- **Focus Indicator (WCAG 2.4.7 Focus Visible):** Wajib memiliki cincin luar (*focus outline*) dengan ketebalan minimal 2px dan rasio kontras minimal 3.0:1 terhadap latar belakang sekitarnya. Jangan pernah menghapus garis fokus (anti-pattern CSS `outline: none` tanpa alternatif pengganti).
- **Disabled State (Aksesibilitas Kognitif):** Tombol yang tidak aktif harus mengomunikasikan ketidakaktifannya secara jelas: teks menggunakan warna `text-disabled` (opasitas ~40-50%) dan kursor mouse berubah menjadi `not-allowed`. Lebih baik lagi jika dilengkapi tooltip yang menjelaskan *mengapa* tombol tersebut belum aktif (misal: "Harap isi nomor telepon Anda terlebih dahulu").

---

### LAYER 4: FIELD PLAYBOOK (TACTICAL SOP & WORKSHEETS)

#### Blueprint Matriks State Komponen Tombol Lengkap

```text
[❖ Component Set: InteractiveButton]
Matrix Permutasi 5 Status Interaktif:

1. State = Default
   • Background: #2563EB (Primary Blue) | Text: #FFFFFF | Scale: 100%
   • Interaction: While hovering ──► Change to: State = Hover (Smart Animate 100ms)

2. State = Hover
   • Background: #1D4ED8 (Darker Blue)  | Text: #FFFFFF | Scale: 102%
   • Interaction: While pressing ──► Change to: State = Pressed (Smart Animate 50ms)

3. State = Pressed
   • Background: #1E40AF (Deepest Blue) | Text: #FFFFFF | Scale: 98% (Tactile Press)
   • Shadow: Inset 0 2px 4px rgba(0,0,0,0.2)

4. State = Focused
   • Background: #2563EB | Border: 2px solid #FFFFFF | Outer Ring: 2px solid #2563EB

5. State = Disabled
   • Background: #E2E8F0 (Neutral Grey)| Text: #94A3B8 | Cursor: Not-Allowed
   • Interactions: NONE (Semua interaksi dimatikan)
```

#### SOP Pembuatan Komponen Akordeon Interaktif:
1. Buat Frame Auto Layout vertikal untuk satu item akordeon (beri nama `AccordionItem`).
2. Masukkan baris header (Auto Layout Horizontal: Teks Pertanyaan `Fill Container`, Ikon Chevron `Fixed`).
3. Masukkan teks jawaban di bawah header (Auto Layout Vertikal: Teks Jawaban `Fill Container`).
4. Duplikasi menjadi dua varian:
   - **Varian 1 (`Expanded = False`):** Sembunyikan layer teks jawaban (`eye icon off`). Ikon chevron rotasi 0 derajat. Frame Auto Layout = *Hug Contents*.
   - **Varian 2 (`Expanded = True`):** Munculkan layer teks jawaban. Putar ikon chevron 180 derajat. Frame Auto Layout = *Hug Contents*.
5. Di panel Prototype: Hubungkan Varian 1 ke Varian 2 dengan event:
   - *On click > Change to: Expanded = True > Smart Animate > Ease-Out 250ms*.
6. Hubungkan Varian 2 kembali ke Varian 1 dengan event sebaliknya.

---

### LAYER 5: DIAGNOSTIC DRILL (STUDI KASUS & UJI MANDIRI)

#### Skenario Kasus Nyata
Sebuah aplikasi SaaS manajemen proyek sedang menyiapkan fitur *Kanban Board*. Setiap kartu tugas memiliki menu dropdown tiga titik (`•••`) yang berisi opsi: "Edit", "Pindahkan", "Hapus".
Desainer membuat interaksi dropdown ini dengan teknik usang:
- Ketika ikon tiga titik diklik pada Kartu A, prototipe berpindah layar (*Navigate to Screen B*) di mana Menu Dropdown digambar menutupi kanvas.
Akibatnya:
1. Jika pengguna telah mencentang beberapa tugas di Kartu B dan Kartu C, centang tersebut hilang seketika saat menu di Kartu A dibuka karena layar me-refresh ke Screen B statis.
2. Posisi scroll kanvas melompat kembali ke paling atas setiap kali menu dibuka.
3. Klien mengeluh bahwa prototipe terasa "kaku seperti slide PowerPoint lama".

#### Lembar Uji Mandiri (3 Pertanyaan Kritis)
1. Mengapa menggunakan teknik *Navigate to Screen* untuk mikro-interaksi lokal (seperti dropdown atau tooltip) merusak status data kanvas dan posisi scroll?
2. Bagaimana teknik *Interactive Components* atau *Open Overlay* menyelesaikan masalah persistensi status dan posisi scroll tersebut?
3. Rancang struktur interaksi terbaik untuk menu dropdown tersebut agar dapat digunakan berulang di ratusan kartu tanpa pernah melompatkan posisi layar!

#### Kunci Jawaban Lengkap & Analisis Anti-Pattern

1. **Akar Kerusakan Status pada Navigate to Screen:** Aksi *Navigate to Screen* adalah instruksi penghancuran Document Object Model (*hard page unmount & remount*). Ketika browser prototipe memuat layar baru, seluruh status variabel lokal, status centang checkbox, dan koordinat offset scroll (Y-scroll position) dihancurkan dan direset kembali ke nilai awal kanvas target. Ini adalah anti-pattern berat untuk segala bentuk interaksi lokal.
2. **Solusi Enkapsulasi via Interactive Components atau Open Overlay:**
   - **Metode 1 (Interactive Component):** Bungkus tombol tiga titik dan menu dropdown ke dalam satu Master Component bernama `CardActionMenu`. Varian 1 = Tertutup (hanya ikon), Varian 2 = Terbuka (ikon + menu popup berposisi absolute). Transisi terjadi murni di dalam batas kartu tanpa menyentuh layar induk sedikit pun. Posisi scroll dan data kartu lain di sekitarnya 100% terjaga.
   - **Metode 2 (Open Overlay):** Jika menu dropdown membutuhkan rendering di atas kartu-kartu lain (menghindari clipping boundary): gunakan aksi *Open Overlay* dengan konfigurasi *Manual* atau *Bottom-Right of Clicked Object*, centang *Close when clicking outside*, dan centang *Preserve scroll position*.
3. **Rekomendasi Arsitektur Terbaik:**
   - Gunakan **Interactive Component** untuk elemen yang ukurannya terprediksi dan tidak membutuhkan z-index yang menembus kontainer clipping.
   - Untuk dropdown kanban yang menembus batas kolom, gunakan komponen menu terpisah yang dipanggil via **Open Overlay (Relative to Target)**.
   - Dengan pendekatan ini, pengguna dapat membuka menu pada kartu mana pun di bagian bawah halaman tanpa pernah mengalami lonjakan scroll, menjaga ilusi aplikasi web modern yang sempurna.
