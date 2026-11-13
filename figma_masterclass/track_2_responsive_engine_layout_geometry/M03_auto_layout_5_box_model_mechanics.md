# Modul 03: Auto Layout 5.0, Box Model Mechanics & Spatial Bounds

> "Desain yang tidak menggunakan Auto Layout hanyalah kumpulan koordinat piksel statis yang rapuh terhadap perubahan data nyata."

## Modul 03: Auto Layout 5.0, Box Model Mechanics & Spatial Bounds

---

### LAYER 1: KAIDAH EMAS (CORE AXIOMS)

1. **Auto Layout adalah Implementasi Visual 1-to-1 dari Model CSS Flexbox dan Box Model:** Setiap kali `Shift+A` diaktifkan pada sebuah frame, frame tersebut bertransformasi menjadi *Flex Container* di mana sumbu utama (*Main Axis*) dan sumbu silang (*Cross Axis*) mengatur perataan, gap, dan padding elemen anak (*Flex Items*) secara deterministik.
2. **Tri-State Resizing (Fixed, Hug, Fill) Menentukan Arah Ketergantungan Dimensi Antara Parent dan Child:**
   - *Fixed:* Dimensi ditentukan oleh angka mutlak independen.
   - *Hug Contents:* Dimensi frame dihitung dari akumulasi ukuran elemen anak ditambah padding dan gap (ketergantungan ke dalam / *inward dependency*).
   - *Fill Container:* Dimensi anak meregang menghabiskan seluruh sisa ruang yang tersedia di dalam frame induk (ketergantungan ke luar / *outward dependency*).
3. **Batas Dimensi Min/Max Bertindak sebagai Pembatas Keras (Hard Clamping) untuk Mencegah Ekstremitas Skala:** Menerapkan `min-width`, `max-width`, `min-height`, dan `max-height` pada elemen responsif mencegah layout hancur saat teks terlalu panjang (mencegah teks meluap) atau saat layar desktop ultra-wide meregangkan kartu hingga tak terbaca.
4. **Auto Layout Wrap Mengubah Alur Geometri Satu Dimensi Menjadi Grid Multi-Baris Dinamis:** Fitur *Wrap* (`flex-wrap: wrap`) mengizinkan elemen anak meluncur ke baris berikutnya secara otomatis saat total lebar anak melampaui kapasitas lebar frame induk, esensial untuk tag chips, galeri produk, dan form responsif.
5. **Absolute Position di Dalam Auto Layout Mengeluarkan Elemen Tertentu dari Alur Normal Menuju Koordinat Bebas:** Tombol *Absolute Position* di inspector atas mengabaikan aturan flex flow bagi elemen terpilih, memungkinkannya mengambang bebas di atas komponen (seperti badge notifikasi di pojok avatar atau tombol floating action) dengan tetap mempertahankan relasi constraints terhadap frame Auto Layout induknya.

---

### LAYER 2: MENTAL MODEL & DIAGRAM ASCII

![Arsitektur Box Model CSS dan Mekanika Figma Auto Layout 5.0 (Padding, Gap, Hug vs Fill Container)](assets/figma/m03_auto_layout_box_model.jpg)

```text
[CSS BOX MODEL vs AUTO LAYOUT FRAME]
┌─────────────────────────────────────────────────────────────┐
│ Auto Layout Parent Frame (Flex Container)                   │
│ Padding: Top=16px, Bottom=16px, Left=24px, Right=24px      │
│ Gap: 12px | Direction: Horizontal (Row)                     │
│                                                             │
│  ┌──────────────┐   Gap: 12px   ┌────────────────────────┐  │
│  │ Child 1      │ ◄───────────► │ Child 2                │  │
│  │ Resizing:    │               │ Resizing:              │  │
│  │ Hug Content  │               │ Fill Container         │  │
│  └──────────────┘               └────────────────────────┘  │
│                                           ▲                 │
│                                           │ (Mengambil sisa │
│                                           │  ruang kosong)  │
└─────────────────────────────────────────────────────────────┘

[TRI-STATE RESIZING ENGINE: VECTOR OF DEPENDENCY]
HUG CONTENTS:         Parent ◄─── Child 1 + Child 2 + Gap + Padding
                      (Dimensi Parent ditentukan oleh isi anak)

FILL CONTAINER:       Child  ◄─── Parent Width - (Padding + Other Children)
                      (Dimensi Child meregang mengikuti sisa ruang Parent)

FIXED DIMENSION:      Child  ◄─── Mutlak misal 320px
                      (Tidak terpengaruh isi anak maupun ukuran parent)

[ABSOLUTE POSITIONING IN AUTO LAYOUT FLOW]
┌─────────────────────────────────────────────────────────────┐
│ Normal Flow Items: [ Item A ] ──gap──► [ Item B ]           │
│                                                             │
│   ┌──────────────┐                                          │
│   │ Item B       │ ◄─── Normal Flow                         │
│   │              │                                          │
│   │       ┌──────┴──────┐ ◄── Absolute Positioned Pin       │
│   │       │ Badge "New" │     (Out of flow, Z-Index top)    │
│   └───────┼─────────────┤     Constraint: Top-Right         │
│           └─────────────┘                                   │
└─────────────────────────────────────────────────────────────┘
```

Formula Lebar Dinamis Child Bertipe *Fill Container*:
`W_child_fill = (W_parent - Padding_left - Padding_right - Σ(W_fixed_children) - Σ(Gap)) / N_fill_children`

---

### LAYER 3: SYARAH DAGING (DEEP DIVE KNOWLEDGE)

#### 1. Syarah Kaidah 1: Auto Layout adalah Implementasi Visual 1-to-1 dari Model CSS Flexbox dan Box Model
Di masa lalu, tools desain UI memperlakukan kanvas seperti meja gambar arsitektur: setiap elemen diletakkan pada titik koordinat absolut (X, Y). Masalah muncul ketika teks diubah dari bahasa Inggris "Buy" menjadi bahasa Jerman "Kaufen" atau bahasa Indonesia "Beli Sekarang". Desainer harus menggeser tombol, melebarkan kotak, dan menata ulang elemen di sebelahnya secara manual.

Auto Layout 5.0 mengadopsi model CSS Flexbox secara native:
- **Direction:** Mendukung Horizontal (`flex-direction: row`), Vertical (`flex-direction: column`), dan Wrap (`flex-wrap: wrap`).
- **Alignment:** Mengontrol perataan silang (`align-items: flex-start, center, flex-end, baseline`) dan perataan utama (`justify-content: flex-start, center, flex-end, space-between`).
- **Box Sizing:** Figma mengadopsi `box-sizing: border-box`, di mana padding dan border (stroke) dihitung ke dalam dimensi total elemen (dapat dikonfigurasi apakah stroke diikutkan atau dikecualikan dalam perhitungan layout flow).

#### 2. Syarah Kaidah 2: Tri-State Resizing (Fixed, Hug, Fill) Menentukan Arah Ketergantungan Dimensi Antara Parent dan Child
Memahami rantai ketergantungan resizing adalah perbedaan antara arsitek antarmuka senior dan desainer pemula:
- **Kapan Menggunakan HUG:** Gunakan HUG pada komponen tingkat daun (*leaf components*) seperti Tombol, Chip, Badge, atau Baris Teks. Tombol harus mengembang jika label teksnya bertambah panjang, dan mengempis jika labelnya pendek. Frame induk yang membungkus deretan chip juga harus HUG secara vertikal agar kartu otomatis memanjang jika chip meluap.
- **Kapan Menggunakan FILL:** Gunakan FILL pada kontainer tingkat perantara (*structural components*) seperti kartu artikel, input form, atau kolom layout. Teks paragraf di dalam Card WAJIB diset ke *Fill Container* pada sumbu horizontal dan *Hug Contents* pada sumbu vertikal. Dengan aturan ini, saat lebar kartu dilebarkan oleh viewport, teks akan melebar ke samping; dan jika teks terdiri dari 3 baris, tinggi kartu akan otomatis bertambah ke bawah mengikuti HUG vertikal.
- **Kapan Menggunakan FIXED:** Gunakan FIXED pada elemen yang terikat pada dimensi fisik perangkat keras atau rasio aspek tetap: misalnya avatar (40×40px), thumbnail gambar 16:9, atau sidebar navigasi tetap (280px).

#### 3. Syarah Kaidah 3: Batas Dimensi Min/Max Bertindak sebagai Pembatas Keras (Hard Clamping) untuk Mencegah Ekstremitas Skala
Pada web modern, tata letak fluid tanpa batas adalah resep bencana. Sebuah modal dialog yang diset *Fill Container* akan terlihat sempurna di laptop 14 inci (lebar 600px), tetapi akan meregang secara mengerikan di monitor ultrawide 4K (lebar 3000px), membuat baris teks terlalu panjang untuk dibaca secara ergonomis.

Dengan menerapkan batas dimensi:
- **Max-Width (misal 640px):** Kartu atau modal dialog akan meregang mengisi layar smartphone hingga mencapai batas 640px, lalu berhenti melebar dan tetap berada di tengah (*align-items: center*).
- **Min-Width (misal 280px):** Mencegah komponen tertekan gepeng hingga memotong teks saat ditempatkan di layar mobile kecil.
- **Min-Height (misal 48px):** Menjamin bahwa setiap tombol aksi memenuhi kriteria *Minimum Target Area* aksesibilitas sentuh Apple HIG dan Google Material Design tanpa perlu trik padding manual.

#### 4. Syarah Kaidah 4: Auto Layout Wrap Mengubah Alur Geometri Satu Dimensi Menjadi Grid Multi-Baris Dinamis
Sebelum hadirnya fitur Wrap pada Auto Layout, mendesain daftar filter tag atau etalase produk adalah siksaan manual. Jika ada 10 tag yang panjangnya berbeda-beda, desainer harus membaginya secara manual ke dalam 3 atau 4 baris frame horizontal terpisah. Jika salah satu tag dihapus, susunan baris hancur.

Fitur *Wrap* mengeksekusi perhitungan pematahan baris (*line-breaking algorithm*) otomatis:
- Elemen anak mengalir secara horizontal dari kiri ke kanan.
- Engine mendeteksi apakah `Lebar_anak_berikutnya > Sisa_lebar_baris_parent`.
- Jika ya, anak tersebut langsung diturunkan ke baris baru dengan jarak vertikal yang diatur oleh properti *Cross-Axis Gap*.
- Ini mencerminkan persis perilaku properti CSS `display: flex; flex-wrap: wrap; gap: 8px 12px;`.

#### 5. Syarah Kaidah 5: Absolute Position di Dalam Auto Layout Mengeluarkan Elemen Tertentu dari Alur Normal Menuju Koordinat Bebas
Seringkali sebuah komponen memiliki dekorasi atau penanda yang melanggar aturan alur linear:
- Badge notifikasi merah di sudut kanan atas ikon lonceng.
- Tombol "Close" (X) di pojok kanan atas modal dialog.
- Tooltip segitiga yang menunjuk ke target form.

Sebelum fitur *Absolute Position in Auto Layout*, desainer terpaksa membongkar Auto Layout seluruh modal dialog dan kembali ke mode manual yang rapuh. Kini, dengan menekan tombol *Absolute Position* di toolbar kanan:
- Elemen tersebut tidak lagi memakan ruang pada flow baris/kolom.
- Elemen dapat digeser bebas menggunakan koordinat X, Y relatif terhadap frame Auto Layout induknya.
- Constraints (Top, Right, Bottom, Left) dapat dipasang sehingga badge akan tetap menempel presisi di pojok kanan atas bahkan saat tombol induknya memanjang karena Auto Layout!

---

### LAYER 4: FIELD PLAYBOOK (TACTICAL SOP & CODE)

#### Tabel Ekivalensi: Figma Auto Layout vs CSS Modern

| Pengaturan di Panel Figma | Ekivalen Kode CSS Modern | Perilaku Layout |
|---|---|---|
| Direction: Horizontal | `display: flex; flex-direction: row;` | Elemen berjejer dari kiri ke kanan |
| Direction: Vertical | `display: flex; flex-direction: column;` | Elemen bertumpuk dari atas ke bawah |
| Direction: Wrap | `display: flex; flex-wrap: wrap;` | Elemen meluncur ke baris baru saat penuh |
| Alignment: Top Left | `justify-content: flex-start; align-items: flex-start;` | Merapat ke sudut kiri atas |
| Alignment: Center | `justify-content: center; align-items: center;` | Rata tengah di kedua sumbu |
| Resizing: Hug Contents | `width: fit-content; height: fit-content;` | Menyusut pas membungkus isi anak |
| Resizing: Fill Container | `flex: 1 1 0%; align-self: stretch; width: 100%;` | Meregang menghabiskan seluruh sisa ruang |
| Item Spacing: Auto | `justify-content: space-between;` | Jarak antar elemen terdistribusi otomatis |
| Stroke: Included in layout | `box-sizing: border-box;` | Ketebalan garis dihitung dalam ukuran frame |
| Absolute Position | `position: absolute;` | Keluar dari flex flow, mengambang bebas |

#### Checklist Audit Layout Anti-Pecah (Responsive Drill Checklist):
1. [ ] Buka frame komponen di kanvas.
2. [ ] Ubah label teks di dalamnya menjadi string ekstrem (misal 3 kata menjadi 15 kata). *Apakah teks ter-wrap dengan rapi atau malah keluar dari batas kartu?* Jika keluar, teks belum diset *Fill Container*.
3. [ ] Tarik handle sisi kanan frame induk ke kiri dan ke kanan (Uji responsif). *Apakah child meregang halus atau diam di tempat?*
4. [ ] Pastikan tidak ada layer frame tersembunyi yang memiliki status *Fixed Width* di dalam kontainer yang seharusnya elastis.

---

### LAYER 5: DIAGNOSTIC DRILL (STUDI KASUS & UJI MANDIRI)

#### Skenario Kasus Nyata
Sebuah e-commerce marketplace merancang komponen *Product Card* untuk katalog web dan mobile. Struktur layer yang dibuat oleh desainer junior adalah sebagai berikut:
- `Card Frame` (Auto Layout Vertikal, Fixed Width: 200px, Fixed Height: 320px).
  - `Image Thumbnail` (Fixed: 200×180px).
  - `Title Text` (Fixed Width: 180px, Height: Hug Contents, isi: "Sepatu Lari").
  - `Price Text` (Fixed: 180×24px, isi: "Rp 850.000").
  - `Buy Button` (Auto Layout Horizontal, Hug Contents).

Ketika tim QA melakukan integrasi data nyata dari katalog API, muncul produk dengan judul panjang: *"Sepatu Lari Pria Ultralight Carbon Plate Marathon Edition 2026 Tahan Air"*.
Akibatnya:
- Teks judul meluas menjadi 4 baris.
- Tombol `Buy Button` terdorong ke bawah dan terpotong secara visual karena tinggi Card Frame dikunci *Fixed Height: 320px* dengan *Clip Content: Active*.
- Rating bintang dan harga produk bertumpuk berantakan.

#### Lembar Uji Mandiri (3 Pertanyaan Kritis)
1. Mengapa mengunci *Fixed Height: 320px* pada kontainer pembungkus konten dinamis (seperti kartu produk) merupakan anti-pattern struktural?
2. Bagaimana cara mengonfigurasi teks judul (*Title Text*) dan `Card Frame` agar tinggi kartu menyesuaikan secara elastis dengan konten tanpa memotong elemen tombol aksi di bawahnya?
3. Jika tim bisnis menginginkan agar semua kartu di dalam grid memiliki tinggi yang seragam (*equal height cards*) meskipun panjang judul berbeda, bagaimana arsitektur Auto Layout harus dirancang?

#### Kunci Jawaban Lengkap & Analisis Anti-Pattern

1. **Akar Kesalahan Fixed Height pada Kontainer Dinamis:** Mengunci dimensi vertikal (*Fixed Height*) pada elemen yang membungkus konten teks tak terduga (*unbounded text strings*) melanggar hukum dasar elastisitas web. Konten teks digital memiliki volume spasial variabel tergantung bahasa, ukuran font, dan panjang data. Ketika tinggi dikunci dan clip content aktif, konten yang meluap akan terpotong (*data truncation bug*); dan jika clip content mati, elemen bawah akan menabrak komponen lain di luar kanvasnya (*overlap collision*).
2. **Konfigurasi Elastis Hug Contents:**
   - Ubah `Card Frame` sumbu vertikal dari **Fixed Height: 320px** menjadi **Hug Contents**.
   - Pada `Title Text`, pastikan Horizontal Resizing = **Fill Container** dan Vertical Resizing = **Hug Contents**.
   - Dengan konfigurasi ini, saat judul bertambah dari 1 baris menjadi 4 baris, teks akan otomatis membuat baris baru (*word wrap*), menambah tinggi intrinsik teks, dan `Card Frame` yang berstatus *Hug Contents* akan otomatis memanjang ke bawah, mendorong `Price Text` dan `Buy Button` dengan jarak gap yang tetap konstan (misal: 12px).
3. **Arsitektur Equal Height Grid:**
   - Untuk baris grid (*Grid Row Frame*), gunakan Auto Layout Horizontal dengan `align-items: stretch`.
   - Di dalam setiap `Product Card`, ubah Vertical Resizing menjadi **Fill Container** (sehingga seluruh kartu di baris tersebut meregang menyamai tinggi kartu yang paling panjang).
   - Di dalam `Product Card`, bungkus bagian informasi teks (`Title` dan `Price`) ke dalam sub-frame vertikal yang diset **Fill Container** pada sumbu vertikal.
   - Set `Buy Button` berada di paling bawah kartu. Dengan sub-frame tengah yang berstatus *Fill*, sisa ruang kosong akan diserap di tengah, sehingga seluruh tombol `Buy Button` di seluruh kartu akan sejajar rapi di garis dasar (*aligned bottom baseline*) terlepas dari variasi panjang judul di atasnya.
