# Modul 01: Mental Model Canvas, Vector Networks & Spatial Coordinates

> "Figma bukan sekadar alat gambar vektor di browser; Figma adalah engine rendering geometri 2D berbasis WebGL yang memetakan elemen hierarkis ke dalam model objek geometris otonom."

## Modul 01: Mental Model Canvas, Vector Networks & Spatial Coordinates

---

### LAYER 1: KAIDAH EMAS (CORE AXIOMS)

1. **Frame adalah Kontainer Geometris Otonom, Bukan Sekadar Pengelompokan Elemen (Group):** Group hanyalah seleksi gabungan yang bounding box-nya selalu terikat pasif pada ukuran child di dalamnya, sedangkan Frame memiliki dimensi fisik independen (panjang, lebar, padding, clip content) yang berlaku persis seperti elemen pembungkus (div) pada browser DOM.
2. **Vector Network Figma adalah Graf Terarah (Node-Edge Graph), Bukan Rantai Jalur Berurutan (Sequential Path Loop):** Dalam ilustrator vektor tradisional, sebuah titik hanya dapat menghubungkan dua segmen (in-degree 1, out-degree 1). Vector Network Figma mengizinkan satu simpul (vertex/node) memiliki tiga atau lebih koneksi percabangan simultan tanpa menduplikasi koordinat titik dasar.
3. **Sistem Koordinat Kanvas Beroperasi Berbasis Matriks Relatif Lokal terhadap Parent Frame:** Posisi (X, Y) setiap objek di dalam Frame tidak dihitung terhadap titik origin mutlak kanvas global (0, 0), melainkan terhadap batas kiri-atas (*top-left origin*) dari Frame pembungkus terdekatnya.
4. **Constraints Menentukan Interpolasi Spasial Bounding Box saat Kanvas Mengalami Skala Dimensi:** Aturan constraints (Top, Bottom, Left, Right, Center, Scale) mengunci hubungan jarak proporsional antara batas child dengan batas parent, menjadi fondasi awal sebelum menerapkan tata letak otomatis (*Auto Layout*).
5. **Clip Content Mengisolasi Render Tree dan Mencegah Spillover Spasial di Luar Batas Fisik Frame:** Mengaktifkan *Clip Content* menginstruksikan engine render untuk memotong (*scissor test*) setiap piksel anak yang meluap ke luar kanvas Frame, memfungsikannya setara dengan `overflow: hidden` pada standar CSS.

---

### LAYER 2: MENTAL MODEL & DIAGRAM ASCII

```text
[FRAME CONTAINER: OTONOM (DIV EQUIVALENT)]
┌─────────────────────────────────────────────────────────────┐
│ Parent Frame (W: 400px, H: 200px)                           │
│ Origin: (X_parent: 100, Y_parent: 50)                       │
│ Clip Content: Active [overflow: hidden]                     │
│                                                             │
│   ┌───────────────────────────┐                             │
│   │ Child Element A           │ ◄── Local Coords: (20, 20)  │
│   │ Constraint: Left & Top    │     Global Coords: (120, 70)│
│   └───────────────────────────┘                             │
│                                                             │
│   ┌──────────────────────────────────────────────┐          │
│   │ Child Element B (Meluap ke kanan luar)       │··········│ (Terpotong
│   │ W: 350px, Local X: 100px                     │ [Clipped]│  oleh Clip
│   └──────────────────────────────────────────────┘··········│  Content)
└─────────────────────────────────────────────────────────────┘

[VECTOR NETWORK: GRAPH TOPOLOGY vs SEQUENTIAL PATH]
TRADITIONAL VECTOR (Path Loop):         FIGMA VECTOR NETWORK (Graph):
       A ─────── B                             A ─────── B
                 │                                      / \
                 │ (Harus diduplikasi                  /   \
                 │  untuk cabang baru)                C ─── D (Bercabang bebas
       C ─────── D                                            dari satu node)
Node Max Degree = 2                      Node Degree = Bebas (Degree >= 1)
```

Formula Hubungan Koordinat Global dan Lokal:
`X_global = X_parent_origin + X_local`
`Y_global = Y_parent_origin + Y_local`

---

### LAYER 3: SYARAH DAGING (DEEP DIVE KNOWLEDGE)

#### 1. Syarah Kaidah 1: Frame adalah Kontainer Geometris Otonom, Bukan Sekadar Pengelompokan Elemen (Group)
Banyak desainer pemula yang terbiasa dengan Photoshop atau Illustrator secara reflek menekan shortcut `Ctrl+G` (Group) untuk membungkus elemen. Ini adalah anti-pattern fatal dalam rekayasa antarmuka digital.

Group dalam Figma tidak memiliki kanvas fisik sendiri. Bounding box dari sebuah Group hanyalah kalkulasi batas terluar (*bounding box union*) dari elemen-elemen di dalamnya. Jika elemen anak digeser, ukuran group ikut berubah secara pasif. Sebaliknya, Frame adalah entitas geometris otonom dengan sumbu X, Y, Width, dan Height tersendiri. Anda dapat membuat Frame berukuran 375 × 812 piksel (layar smartphone) yang sama sekali kosong, memberinya latar belakang (*fills*), border (*strokes*), sudut lengkung (*corner radius*), dan layout grid. Dalam arsitektur software web, Frame merepresentasikan `<div>` atau `<section>`, sedangkan Group hanyalah seleksi kolektif sementara.

#### 2. Syarah Kaidah 2: Vector Network Figma adalah Graf Terarah (Node-Edge Graph), Bukan Rantai Jalur Berurutan (Sequential Path Loop)
Pada format SVG klasik dan aplikasi grafis generasi lama (seperti Adobe Illustrator atau CorelDRAW), jalur vektor didefinisikan sebagai rantai titik berurutan (*path list*). Setiap titik hanya memiliki simpul masuk dan keluar. Apabila Anda ingin membuat bentuk payung atau ikon pie-chart dengan garis yang bertemu di titik tengah, Anda terpaksa membuat beberapa path terpisah yang titik akhirnya ditumpuk secara presisi di koordinat yang sama.

Figma mengubah paradigma ini dengan mengadopsi model data graf (*Vector Networks*). Sebuah titik di Figma adalah simpul graf (*vertex*) murni, dan garis di antaranya adalah sisi (*edges*). Satu titik tunggal dapat menjadi muara bagi 3, 4, atau lebih garis berbeda. Hal ini memberikan efisiensi luar biasa:
- Mengurangi ukuran payload file desain karena tidak ada duplikasi koordinat titik yang redundan.
- Memungkinkan manipulasi kurva Bézier yang saling terikat secara elastis.
- Mempermudah pewarnaan bidang kompleks (*fill-regions*) tanpa perlu memecah objek menjadi path terpisah.

#### 3. Syarah Kaidah 3: Sistem Koordinat Kanvas Beroperasi Berbasis Matriks Relatif Lokal terhadap Parent Frame
Kanvas Figma adalah bidang kartesian dua dimensi tanpa batas (*infinite canvas*). Namun, saat sebuah elemen dimasukkan ke dalam Frame, sistem perhitungannya beralih dari koordinat absolut kanvas menjadi koordinat relatif lokal terhadap parent frame terdekat.

Hal ini krusial saat merancang antarmuka modular. Ketika sebuah tombol diletakkan pada posisi `(X: 16, Y: 24)` di dalam Card Component, nilai tersebut mengindikasikan jarak tombol dari sudut kiri atas Card tersebut. Saat Card dipindahkan ke posisi mana pun di kanvas besar, koordinat lokal tombol tetap utuh `(16, 24)`. Konsep ini adalah fondasi langsung dari model Document Object Model (DOM) browser, di mana child dengan `position: absolute` memposisikan dirinya relatif terhadap parent yang memiliki `position: relative`.

#### 4. Syarah Kaidah 4: Constraints Menentukan Interpolasi Spasial Bounding Box saat Kanvas Mengalami Skala Dimensi
Sebelum era Auto Layout, atau ketika mendesain kanvas bebas yang tidak berbasis flow (misalnya ilustrasi latar belakang atau peta interaktif), *Constraints* adalah mekanisme penentu respon elemen saat frame induknya di-resize:
- **Left / Right / Top / Bottom:** Mengunci jarak piksel tetap terhadap batas tepi frame induk.
- **Center:** Mempertahankan posisi relatif terhadap garis tengah frame induk, mengabaikan perubahan jarak ke tepi.
- **Left and Right (Stretch / Horizontal Fill):** Mengikat kedua sisi elemen ke tepi kiri dan kanan frame induk, sehingga lebar elemen akan membesar atau mengecil secara proporsional saat frame di-resize.
- **Scale:** Mengubah posisi dan dimensi elemen berdasarkan persentase geometris dari ukuran frame induk (misalnya elemen akan selalu mengambil 50% dari lebar frame).

#### 5. Syarah Kaidah 5: Clip Content Mengisolasi Render Tree dan Mencegah Spillover Spasial di Luar Batas Fisik Frame
Fitur *Clip Content* pada panel inspector kanan Figma bertindak sebagai batas visual keras (*bounding clipping plane*). Ketika elemen anak memiliki ukuran atau posisi yang keluar dari batas frame induknya:
- Jika *Clip Content* tidak aktif (uncheck): Elemen anak tetap dirender visual di luar kotak frame, meskipun secara hierarki layer elemen tersebut berada di dalam frame tersebut. Hal ini sering menimbulkan kebingungan navigasi klik dan polusi visual pada artboard kanvas.
- Jika *Clip Content* aktif (checked): Engine grafis WebGL Figma menerapkan *scissor test*, memotong semua piksel di luar batas poligon frame. Ini esensial untuk mendesain komponen seperti horizontal carousel, dropdown accordion, bottom sheet, dan masking gambar.

---

### LAYER 4: FIELD PLAYBOOK (TACTICAL SOP & WORKSHEETS)

#### SOP Standarisasi Kontainer UI (Frame vs Group Matrix)

| Kebutuhan Desain | Struktur yang Wajib Digunakan | Alasan Teknis |
|---|---|---|
| Screen / Artboard (Mobile, Tablet, Web) | **Frame** (`F`) | Memerlukan ukuran kanvas tetap, batas clip, dan layout grid. |
| Tombol, Card, Bar Navigasi | **Frame** dengan Auto Layout (`Shift+A`) | Memerlukan dynamic padding, auto-resizing, dan gap terkendali. |
| Ikon Vektor Kompleks (Multi-part) | **Frame** ukuran 24×24px | Memastikan bounding box tap-target konsisten meski bentuk ikon asimetris. |
| Seleksi Sementara untuk Menggeser Aset | **Group** (`Ctrl+G`) | Hanya untuk kemudahan manipulasi gerak sesaat, segera ubah ke Frame bila permanen. |

#### Checklist Konfigurasi Kanvas Presisi:
1. Pastikan fitur **Pixel Preview** (`Ctrl+Alt+Y`) aktif saat memeriksa aset resolusi rendah untuk menghindari blur sub-pixel.
2. Gunakan shortcut `Alt+1` dan `Alt+2` untuk beralih instan antara panel *Layers* dan *Assets*.
3. Setiap membuat ikon SVG baru, kunci bounding box terluar pada ukuran integer genap (misalnya 16×16, 20×20, 24×24) dan lakukan `Flatten` (`Ctrl+E`) pada kurva yang tidak memerlukan edit simpul terpisah.

---

### LAYER 5: DIAGNOSTIC DRILL (STUDI KASUS & UJI MANDIRI)

#### Skenario Kasus Nyata
Sebuah tim desain produk digital di startup fintech sedang menyiapkan komponen *Header Navigation Bar* untuk aplikasi mobile dan web. Desainer junior membungkus logo, menu pencarian, dan avatar profil ke dalam sebuah **Group**, lalu menempatkan group tersebut di dalam Frame layar berukuran 1440px (Desktop). 

Ketika developer mencoba mengekstrak aset dan menguji responsivitas dengan me-resize frame ke ukuran 375px (Mobile), terjadi anomali kritis:
- Input pencarian gepeng dan bertumpuk di atas avatar.
- Tombol aksi terlempar ke koordinat negatif kanvas.
- Nilai koordinat yang terbaca oleh developer di Dev Mode menunjukkan angka pecahan desimal seperti `X: 43.72px, Y: 12.19px`.

#### Lembar Uji Mandiri (3 Pertanyaan Kritis)
1. Mengapa membungkus elemen header di dalam Group menyebabkan elemen gepeng saat di-resize, alih-alih mempertahankan padding dan ukuran intrinsiknya?
2. Bagaimana mekanisme koordinat sub-pixel desimal (`.72px`) dapat muncul pada inspect elemen, dan apa dampaknya terhadap rendering browser engine?
3. Langkah perbaikan deterministik apa yang harus diambil untuk mengubah struktur header tersebut agar scalable dan developer-ready?

#### Kunci Jawaban Lengkap & Analisis Anti-Pattern

1. **Akar Masalah Group Scaling:** Group di Figma tidak memiliki properti *Constraints* otonom dan tidak mendukung *Auto Layout*. Ketika sebuah Group di-resize secara langsung (atau dipaksa mengikuti transformasi induk), Figma menerapkan transformasi matriks skala linier (*Scale Transformation*) pada seluruh vektor anak di dalamnya. Akibatnya, rasio aspek teks dan ikon dipaksa memipih (distorsi rasio) bukannya mengatur ulang aliran spasialnya (*content reflow*).
2. **Penyebab Koordinat Sub-Pixel & Dampaknya:** Koordinat desimal muncul karena transformasi skala persentase pada group membagi dimensi integer menjadi angka pecahan (misal: lebar 100px diskala 43.72%). Dampak pada browser: rasterizer mesin WebKit/Blink akan melakukan *anti-aliasing interpolation* pada garis batas, menghasilkan border dan teks yang tampak kabur (*blurry edges*) dan memicu bug komputasi layout rendering 1px border shift.
3. **Solusi Perbaikan Deterministik:**
   - Bongkar Group dengan `Ctrl+Shift+G` (*Ungroup*).
   - Bungkus logo dan elemen navigasi ke dalam **Frame** baru.
   - Aktifkan **Auto Layout** (`Shift+A`) dengan orientasi horizontal.
   - Atur `justify-content` ke *Space Between* (Auto Gap).
   - Terapkan padding lateral tetap (misal: 24px) dan kunci tinggi frame (misal: 64px) dengan ukuran integer bulat.
   - Set constraint horizontal menjadi *Left and Right* (atau set width menjadi *Fill Container* pada mode Auto Layout).
