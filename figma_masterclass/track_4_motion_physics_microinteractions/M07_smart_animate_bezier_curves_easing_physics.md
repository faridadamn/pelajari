# Modul 07: Smart Animate Mechanics, Cubic Bézier & Spring Physics

> "Animasi antarmuka yang buruk memperlambat pengguna; animasi antarmuka yang hebat memberikan kejelasan spasial instan tanpa pernah terasa menghabiskan waktu."

## Modul 07: Smart Animate Mechanics, Cubic Bézier & Spring Physics

---

### LAYER 1: KAIDAH EMAS (CORE AXIOMS)

1. **Invarian Pencocokan Smart Animate: Nama Layer dan Posisi Hierarki Pohon Wajib Identik 100%:** Engine Smart Animate hanya menginterpolasi geometri antar-frame jika elemen pada kedua layar memiliki nama layer yang persis sama dan berada di kedalaman struktur parent yang setara. Jika nama berbeda 1 karakter atau struktur pohon berbeda, engine akan gagal dan terdegradasi (*fallback*) ke efek disolusi pudar (*cross-fade*).
2. **Kontinuitas Identitas Objek Mencegah Beban Kognitif Mata Saat Transisi Spasial Terjadi:** Mengubah ukuran atau posisi elemen yang sama di layar tujuan (misal: kartu produk di grid membesar menjadi hero detail di halaman produk) mempertahankan pemahaman pengguna bahwa objek tersebut adalah entitas fisik yang sama yang bertransformasi, bukan halaman baru yang dimuat dari nol.
3. **Kurva Easing Ease-Out adalah Standar Baku untuk Elemen yang Memasuki Layar (Entrance Animation):** Elemen antarmuka digital harus merespons input sentuhan dengan percepatan instan di awal (kecepatan awal tinggi) lalu melambat secara halus saat mencapai posisi akhir (deceleration), meniru hukum gesekan fisik alam nyata.
4. **Fisika Pegas (Spring Dynamics) Menghilangkan Batas Durasi Waktu Statis Menjadi Relasi Massa dan Redaman:** Alih-alih menetapkan waktu statis (misal 300ms), *Spring Physics* menghitung trajektori gerak berdasarkan tiga parameter: Kekakuan (*Stiffness* k), Rasio Redaman (*Damping Ratio* ζ), dan Massa (*Mass* m). Redaman kritis (ζ = 1.0) menghasilkan gerakan tanggap tanpa pantulan berlebih (*no overshoot slop*).
5. **Threshold Latensi Perseptual Menentukan Batas Toleransi Durasi Gerakan:** Mikro-interaksi tombol dan toggle tidak boleh melebihi 100-200ms; transisi komponen lokal (dropdown, kartu ekspansi) dibatasi pada 250-350ms; dan transisi pergantian layar penuh dibatasi maksimal pada 400-500ms agar tidak memicu rasa frustrasi pengguna.

---

### LAYER 2: MENTAL MODEL & DIAGRAM ASCII

```text
[SMART ANIMATE INTERPOLATION ENGINE]
Frame A (Initial State)                   Frame B (Final State)
┌───────────────────────────────┐         ┌───────────────────────────────┐
│ • Layer: "Card/Cover"         │         │ • Layer: "Card/Cover"         │
│   W: 100px, H: 100px, Rad: 8px│ ──────► │   W: 375px, H: 250px, Rad: 0px│
│   Fill: #2563EB, Opacity: 100%│  Smart  │   Fill: #1E40AF, Opacity: 100%│
└───────────────────────────────┘ Animate └───────────────────────────────┘
  (Nama & Struktur Identik:         (Engine menghitung interpolasi tiap frame
   Interpolasi Geometri Mulus!)      antara dimensi, radius, dan warna heks)

[CUBIC BÉZIER vs SPRING DYNAMICS CURVES]
POSISI (Y)
1.0 ┌───────────────────────....... (Target Settle)
    │                      /  \     ▲
    │                     /    \    │ Overshoot (Underdamped Spring: ζ < 1.0)
    │         ┌──────────/───────...│.......................................
    │        /          /           │ Ease-Out (Bézier: Cepat di awal, ngerem)
    │       /          /            │ Critical Damping (ζ = 1.0: Cepat, no bounce)
    │      /          /             ▼
0.0 └───┴───────────────────────────► WAKTU (X)
    Start Click       End (250ms)
```

Formula Fisika Redaman Pegas (*Damped Harmonic Oscillator*):
`m × (d²x/dt²) + c × (dx/dt) + k × x = 0`
Rasio Redaman Kritis: `c_crit = 2 × √(k × m)` ; `ζ = c / c_crit`

---

### LAYER 3: SYARAH DAGING (DEEP DIVE KNOWLEDGE)

#### 1. Syarah Kaidah 1: Invarian Pencocokan Smart Animate: Nama Layer dan Posisi Hierarki Pohon Wajib Identik 100%
Bagaimana cara kerja internal engine *Smart Animate* di Figma?
Ketika Anda menghubungkan Frame A ke Frame B menggunakan opsi Smart Animate:
1. Engine memindai seluruh pohon Document Object Model internal di kedua frame.
2. Engine mencari pasangan layer yang memiliki **Nama Layer yang Identik Persis** (misal: `"Thumbnail-Image"` di Frame A dan `"Thumbnail-Image"` di Frame B).
3. Jika ditemukan, engine memeriksa apakah tipe layernya kompatibel (misal: keduanya berupa Frame, Rectangle, atau Vector).
4. Engine kemudian membuat kurva interpolasi matematis untuk setiap properti yang berubah:
   - Sumbu X dan Y (Perpindahan translasi).
   - Dimensi *Width* dan *Height* (Peregangan skala).
   - *Rotation* (Derajat putar).
   - *Corner Radius* (Lengkung sudut).
   - *Fills* dan *Strokes* (Transisi palet warna).
   - *Opacity* (Transparansi).

Jika Anda mengganti nama salah satu layer menjadi `"Thumbnail-Image-2"` atau memindahkannya ke dalam sub-group yang berbeda, engine menganggap objek tersebut telah dihancurkan di Frame A dan objek baru diciptakan di Frame B. Hasilnya: objek akan memudar hilang (*fade out*) dan objek baru memudar muncul (*fade in*) secara kasar.

#### 2. Syarah Kaidah 2: Kontinuitas Identitas Objek Mencegah Beban Kognitif Mata Saat Transisi Spasial Terjadi
Dalam psikologi persepsi visual Gestalt, otak manusia membutuhkan energi kognitif untuk memproses perubahan visual mendadak. Jika seorang pengguna mengklik kartu artikel kecil di daftar berita dan tiba-tiba seluruh layar berganti putih lalu memunculkan halaman baca, otak pengguna mengalami disorientasi mikro selama 100-200 milidetik untuk memastikan bahwa ia tidak salah tersesat ke halaman lain.

Dengan menerapkan prinsip *Continuous Object Identity* via Smart Animate:
- Kartu berita di daftar grid mengembang secara visual menjadi wadah artikel utama.
- Gambar thumbnail kartu melebar menjadi gambar sampul artikel (*header banner*).
- Judul kartu bergerak naik menjadi judul artikel berukuran besar.
Mata pengguna secara natural melacak pergerakan elemen tersebut. Efek kontinuitas ini mengonfirmasi secara instan bahwa konteks halaman tetap terjaga, memberikan rasa kontrol dan keandalan tinggi pada aplikasi.

#### 3. Syarah Kaidah 3: Kurva Easing Ease-Out adalah Standar Baku untuk Elemen yang Memasuki Layar (Entrance Animation)
Kurva animasi (*Easing Curves*) mendefinisikan percepatan objek sepanjang sumbu waktu:
- **Linear (`cubic-bezier(0, 0, 1, 1)`):** Kecepatan konstan dari awal hingga akhir. Ini adalah kesalahan nomor satu pemula. Gerakan linear terasa kaku, mekanis seperti robot, dan sangat tidak wajar bagi mata manusia. Satu-satunya kegunaan linear adalah untuk indikator loading putar (*spinner*) yang berotasi tanpa henti.
- **Ease-Out (`cubic-bezier(0, 0, 0.2, 1)`):** Kecepatan sangat tinggi di awal, lalu melambat secara halus di akhir. Ini adalah kurva wajib untuk seluruh elemen yang masuk ke layar (seperti modal dialog pop-up, drawer menu yang meluncur dari samping, atau toast notification). Ketika pengguna menekan tombol, sistem harus merespons seketika; keterlambatan gerak di awal membuat aplikasi terasa lelet.
- **Ease-In (`cubic-bezier(0.4, 0, 1, 1)`):** Lambat di awal, lalu melesat kencang di akhir. Hanya digunakan untuk elemen yang keluar dari layar (*exit animation*).
- **Ease-In-Out (`cubic-bezier(0.4, 0, 0.2, 1)`):** Lambat di awal, cepat di tengah, melambat di akhir. Digunakan untuk elemen yang sudah ada di layar dan berpindah posisi (misal: sorting kartu atau carousel geser).

#### 4. Syarah Kaidah 4: Fisika Pegas (Spring Dynamics) Menghilangkan Batas Durasi Waktu Statis Menjadi Relasi Massa dan Redaman
Standar animasi UI modern (seperti yang dipelopori oleh iOS Fluid Interfaces) beralih dari kurva durasi waktu tetap (*time-based Bézier*) menuju simulasi fisika dinamis (*Spring Physics*):
- **Stiffness (k):** Mengatur ketegangan pegas. Semakin tinggi nilainya (misal 300), semakin cepat dan bertenaga respons objek terhadap sentuhan.
- **Damping Ratio (ζ):** Mengatur friksi pengereman:
  - ζ < 1.0 (*Underdamped*): Menghasilkan efek pantulan (*bouncy overshoot*). Hati-hati: pantulan berlebih terlihat kekanak-kanakan dan tidak profesional untuk aplikasi bisnis.
  - ζ = 1.0 (*Critically Damped*): Pegas kembali ke posisi setimbang dalam waktu tercepat yang mungkin tanpa memantul melewati batas sama sekali. Ini adalah standar emas untuk antarmuka profesional: terasa kenyal dan hidup, tetapi berhenti dengan presisi bedah.
  - ζ > 1.0 (*Overdamped*): Pergerakan lamban dan terasa berat seperti bergerak di dalam cairan kental.
- **Mass (m):** Merepresentasikan bobot virtual objek. Elemen kecil (seperti ikon like hati) memiliki massa kecil (m = 0.8), sedangkan modal panel penuh memiliki massa lebih besar (m = 1.2).

#### 5. Syarah Kaidah 5: Threshold Latensi Perseptual Menentukan Batas Toleransi Durasi Gerakan
Penelitian interaksi manusia dan komputer (HCI) oleh Robert Miller dan Nielsen Norman Group menetapkan batas waktu responsivitas kognitif:
- **0 - 100 milidetik:** Terasa instan (*direct manipulation*). Animasi feedback tombol (warna berubah saat ditekan) harus berada di rentang ini.
- **100 - 300 milidetik:** Terasa cepat dan tanggap (*fluid response*). Durasi ideal untuk mikro-interaksi lokal seperti toggle switch, checkbox, accordion expand, dan dropdown list.
- **300 - 500 milidetik:** Batas atas transisi spasial besar (seperti modal dialog layar penuh atau sheet transisi navigasi).
- **> 500 milidetik:** Mulai terasa lambat dan menguji kesabaran pengguna. Pengguna yang menggunakan aplikasi berkali-kali sehari (aplikasi kerja, mobile banking) akan merasa terhambat jika setiap klik dipaksa menunggu animasi lambat selama 800ms.

---

### LAYER 4: FIELD PLAYBOOK (TACTICAL SOP & CODE)

#### Template Konfigurasi Easing & CSS Cubic-Bézier Standar Produksi

```css
:root {
  /* ==========================================================================
     TIMING FUNCTIONS (Ekivalen Kurva Figma ke CSS)
     ========================================================================== */
  
  /* Entrance: Digunakan untuk Modal, Drawer, Toast */
  --ease-out-standard: cubic-bezier(0.16, 1, 0.3, 1);
  
  /* Exit: Digunakan saat elemen menutup / meninggalkan viewport */
  --ease-in-standard:  cubic-bezier(0.7, 0, 0.84, 0);
  
  /* Reposition: Digunakan saat elemen berpindah tempat di dalam layar */
  --ease-in-out-fluid: cubic-bezier(0.65, 0, 0.35, 1);
  
  /* ==========================================================================
     DURATION TOKENS (Perception Latency Limits)
     ========================================================================== */
  --duration-instant:  100ms;  /* Feedback sentuh & hover */
  --duration-fast:     200ms;  /* Toggle switch, dropdown */
  --duration-normal:   300ms;  /* Card expansion, accordions */
  --duration-slow:     450ms;  /* Page navigation, full dialog */
}

/* Contoh Penerapan Microinteraction pada Kartu */
.interactive-card {
  transition: transform var(--duration-fast) var(--ease-out-standard),
              box-shadow var(--duration-fast) var(--ease-out-standard);
}

.interactive-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 24px -8px rgba(0, 0, 0, 0.15);
}
```

#### SOP Setup Smart Animate Morphing di Figma:
1. Siapkan Frame Asal (Layar 1) dan Frame Tujuan (Layar 2).
2. Pastikan layer yang ingin di-morph memiliki **NAMA YANG SAMA PERSIS** (misal `img-product-hero`).
3. Pastikan jenis layer sama (Frame dengan Frame, bukan Frame dengan Rectangle biasa).
4. Di panel Prototype, tarik garis koneksi dari Layar 1 ke Layar 2.
5. Atur interaction details:
   - Trigger: `On click`
   - Action: `Navigate to`
   - Animation: `Smart Animate`
   - Easing: Pilih `Custom Spring` (Stiffness: 250, Damping: 25) atau `Custom Bézier` (`0.16, 1, 0.3, 1`).
   - Duration: `300ms`.

---

### LAYER 5: DIAGNOSTIC DRILL (STUDI KASUS & UJI MANDIRI)

#### Skenario Kasus Nyata
Seorang desainer di platform media sosial sedang merancang animasi interaktif untuk kartu video di feed:
- Saat kartu video diklik, kartu tersebut harus membesar secara mulus memenuhi layar ponsel (*Full-screen Video Player*).
- Desainer telah memilih opsi *Smart Animate (Ease-Out, 350ms)* pada sambungan prototipe.
Namun saat prototipe diuji coba di hadapan Product Manager:
- Gambar video tidak membesar secara elastis, melainkan langsung berkedip kasar (*flicker*) dan memudar pudar (*cross-fade*).
- Teks judul video menghilang sejenak lalu muncul tiba-tiba di posisi baru.
- Seluruh tim sepakat bahwa animasi terlihat "patah, murahan, dan tidak mulus".

#### Lembar Uji Mandiri (3 Pertanyaan Kritis)
1. Apa penyebab teknis paling mendasar mengapa Smart Animate mengalami degradasi (*fallback*) ke efek cross-fade yang patah?
2. Bagaimana cara mengaudit struktur hierarki layer antara Frame Asal dan Frame Tujuan untuk mendeteksi akar masalah tersebut?
3. Langkah perbaikan apa yang harus dilakukan agar kartu video membesar dengan transisi geometri continuous yang sempurna?

#### Kunci Jawaban Lengkap & Analisis Anti-Pattern

1. **Akar Kegagalan Interpolasi Smart Animate:** Smart Animate gagal melakukan morphing geometri dan terdegradasi ke *cross-fade* karena terjadi **Pelanggaran Invarian Pencocokan Layer**. Ini biasanya disebabkan oleh salah satu dari dua hal:
   - Nama layer video pada Frame Asal berbeda dengan Frame Tujuan (misal di Layar 1 bernama `Video Thumbnail`, sedangkan di Layar 2 bernama `Player / Video Stream`).
   - Posisi hierarki berbeda kedalaman (misal di Layar 1 layer tersebut berada langsung di root frame, sedangkan di Layar 2 layer tersebut dibungkus di dalam sub-frame Auto Layout lain).
2. **Prosedur Audit Struktur Pohon Layer:**
   - Buka panel Layers (`Alt+1`) di sebelah kiri.
   - Buka kedua frame secara berdampingan.
   - Periksa layer video di Frame 1 dan Frame 2: pastikan nama karakternya identik huruf besar-kecilnya (misal: ganti keduanya menjadi persis `video-viewport`).
   - Pastikan tipe objeknya sama: jika di Frame 1 berupa Frame dengan image fill, di Frame 2 juga wajib berupa Frame dengan image fill (bukan objek Rectangle atau Vector shape).
3. **Solusi Perbaikan Deterministik:**
   - Samakan nama layer: Ubah nama layer di kedua frame menjadi `video-container`.
   - Di Frame 1 (Feed): `video-container` berukuran 343 × 200px dengan corner radius 12px.
   - Di Frame 2 (Full-screen): `video-container` berukuran 375 × 812px dengan corner radius 0px.
   - Pastikan teks judul di kedua frame dinamai sama persis (`video-title`).
   - Terapkan kembali koneksi *Smart Animate* dengan kurva `Ease-Out (300ms)` atau `Gentle Spring`.
   - **Hasil:** Video akan mengembang membesar secara kontinu dari 200px ke 812px dan sudutnya memipih dari 12px ke 0px secara mulus sempurna tanpa ada kedipan cross-fade sama sekali.
