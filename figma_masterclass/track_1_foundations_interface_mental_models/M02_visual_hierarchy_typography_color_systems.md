# Modul 02: Visual Hierarchy, Typographic Scale & Color Systems

> "Hierarki visual bukanlah persoalan selera estetika subjektif, melainkan orkestrasi matematis antara frekuensi spasial, rasio skala tipografi, dan kontras luminansi fotometrik."

## Modul 02: Visual Hierarchy, Typographic Scale & Color Systems

---

### LAYER 1: KAIDAH EMAS (CORE AXIOMS)

1. **Sistem Spasial 8-Point Soft Grid Menjamin Kelipatan Modular yang Selaras dengan Raster Layar Hardware:** Layar digital modern merender piksel dalam kelipatan biner komputer (2, 4, 8, 16, 32). Mendasarkan seluruh margin, padding, dan dimensi pada kelipatan 8px (dengan subgrid 4px untuk ruang mikro) mengeliminasi fraksi sub-pixel dan menjamin keterbacaan tajam di semua densitas layar (1x, 2x, 3x / @2x @3x Retina).
2. **Skala Tipografi Modular Berakar pada Rasio Geometris Tetap, Bukan Angka Acak:** Hirarki teks yang harmonis dibangun menggunakan rasio progresi matematis (seperti *Major Third* 1.250 atau *Perfect Fourth* 1.333) dari ukuran dasar 16px (1rem), di mana setiap tingkatan heading (H_n) merupakan eksponensial dari rasio pengali terhadap baseline.
3. **Line-Height Geometris Wajib Mengunci Ritme Vertikal pada Grid Kelipatan 4px:** Tinggi baris (*line-height*) teks tubuh (*body*) dan judul (*heading*) harus dibulatkan ke kelipatan 4px (misal: teks 16px dengan line-height 24px; teks 24px dengan line-height 32px) agar tidak merusak keselarasan vertikal (*vertical baseline rhythm*).
4. **Kontras Warna Beroperasi Berdasarkan Perceived Luminance (Luminansi Relatif), Bukan Nilai Hex RGB:** Mata manusia mempersepsikan kecerahan warna hijau jauh lebih terang daripada biru pada nilai RGB yang identik. Standar kepatuhan aksesibilitas (WCAG 2.1 AA rasio 4.5:1 untuk teks normal, atau APCA Lc 60+) dihitung menggunakan formula luminansi relatif fotometrik, bukan sekadar perbedaan kode warna.
5. **Abstraksi Palet Warna Terdiri dari Tiga Lapisan Taksonomi: Primitif, Semantik, dan Komponen:** Warna antarmuka tidak boleh di-hardcode langsung ke kode HEX; sistem warna wajib memisahkan nilai palet dasar (primitif: `blue-500`), tujuan fungsional (semantik: `color-surface-action`), dan penerapannya pada UI (komponen: `btn-primary-bg`).

---

### LAYER 2: MENTAL MODEL & DIAGRAM ASCII

```text
[8-POINT MODULAR SPATIAL GRID]
8px    16px     24px      32px       40px        48px
├───┼────────┼─────────┼──────────┼───────────┼───────────►
Gap   Padding  Section   Card Gap   Hero Spacing Touch Target

[TYPOGRAPHIC MODULAR SCALE: MAJOR THIRD (1.250)]
Base: 16px (1.000)
Level        Multiplier       Font Size   Line Height (4px Grid)
Display      16 × 1.25^4    = 39.06px → 40px     48px (12 × 4)
H1           16 × 1.25^3    = 31.25px → 32px     40px (10 × 4)
H2           16 × 1.25^2    = 25.00px → 24px     32px (8 × 4)
H3           16 × 1.25^1    = 20.00px → 20px     28px (7 × 4)
Body (Base)  16 × 1.25^0    = 16.00px → 16px     24px (6 × 4)
Caption      16 × 1.25^(-1) = 12.80px → 12px     16px (4 × 4)

[COLOR TAXONOMY HIERARCHY]
┌────────────────────────────────────────────────────────┐
│ 1. Primitive Palette: blue-500 = #0066FF               │
│    (Definisi warna mentah tanpa konteks kegunaan)      │
└──────────────────────────┬─────────────────────────────┘
                           │ Aliasi
                           ▼
┌────────────────────────────────────────────────────────┐
│ 2. Semantic Token: action-primary = blue-500           │
│    (Makna fungsional sistem desain)                    │
└──────────────────────────┬─────────────────────────────┘
                           │ Konsumsi
                           ▼
┌────────────────────────────────────────────────────────┐
│ 3. Component Token: button-primary-bg = action-primary │
│    (Konteks spesifik elemen antarmuka)                 │
└────────────────────────────────────────────────────────┘
```

Formula Rasio Kontras Relatif WCAG:
`Contrast Ratio = (L1 + 0.05) / (L2 + 0.05)`
di mana `L1` adalah luminansi relatif warna yang lebih terang dan `L2` adalah warna yang lebih gelap.

---

### LAYER 3: SYARAH DAGING (DEEP DIVE KNOWLEDGE)

#### 1. Syarah Kaidah 1: Sistem Spasial 8-Point Soft Grid Menjamin Kelipatan Modular yang Selaras dengan Raster Layar Hardware
Mayoritas layar gawai (smartphone, tablet, monitor komputer) memiliki densitas fisik dengan rasio piksel hardware yang dapat dibagi rata oleh angka 8. Angka 8 dipilih dalam rekayasa antarmuka digital karena memiliki fleksibilitas pembagian matematika yang unik: 8 dapat dibagi dengan 2 dan 4 tanpa menghasilkan sisa pecahan desimal.

Dalam *Soft Grid*, desainer tidak memaksakan penempatan elemen secara kaku pada garis grid absolut kanvas, melainkan memastikan bahwa:
- Setiap ukuran komponen (lebar dan tinggi).
- Setiap jarak antar-komponen (*margin* dan *gap*).
- Setiap bantalan internal komponen (*padding*).
selalu bernilai kelipatan 8: `8px, 16px, 24px, 32px, 40px, 48px, 56px, 64px`.

Pengecualian berlaku untuk elemen mikro (seperti padding vertikal tombol ramping, border icon, atau badge counter) di mana *Half-Grid* 4px diizinkan: `4px, 12px, 20px`. Dengan disiplin ini, desainer menghemat ribuan keputusan mikro sehari-hari, dan developer tidak perlu menebak apakah jarak antar kartu adalah 17px, 19px, atau 21px.

#### 2. Syarah Kaidah 2: Skala Tipografi Modular Berakar pada Rasio Geometris Tetap, Bukan Angka Acak
Salah satu tanda paling mencolok dari desain antarmuka amatir adalah ukuran huruf yang melompat secara acak: misalnya 14px, 17px, 22px, 29px, 38px. Mata manusia membutuhkan proporsi yang terprediksi untuk mengenali hierarki kepentingan informasi.

Skala tipografi modular (*Modular Typographic Scale*) meminjam prinsip interval nada musik. Menggunakan rasio pengali tetap (rasio r):
- *Minor Third* (r = 1.200): Bagus untuk dashboard data padat dengan keterbatasan ruang vertikal.
- *Major Third* (r = 1.250): Standar emas untuk antarmuka web modern, SaaS, dan aplikasi mobile standar.
- *Perfect Fourth* (r = 1.333): Sangat kontras dan bertenaga, ideal untuk landing page editorial atau e-commerce premium.

Dengan rasio 1.250 dan basis 16px:
- Level 0 (Body Base): 16px
- Level 1 (H3 / Subtitle): 16 × 1.25 = 20px
- Level 2 (H2 / Section Title): 20 × 1.25 = 25px (dibulatkan ke 24px agar selaras dengan 8pt grid)
- Level 3 (H1 / Page Title): 25 × 1.25 = 31.25px (dibulatkan ke 32px)
- Level 4 (Display / Hero): 31.25 × 1.25 = 39.06px (dibulatkan ke 40px)

#### 3. Syarah Kaidah 3: Line-Height Geometris Wajib Mengunci Ritme Vertikal pada Grid Kelipatan 4px
Menentukan ukuran font saja tidak cukup. Dalam rendering browser, teks menempati ruang vertikal yang ditentukan oleh properti `line-height`, bukan `font-size`. Jika font berukuran 16px diberi line-height default browser (seringkali 1.15 atau ~18.4px), seluruh elemen di bawah teks tersebut akan bergeser ke koordinat desimal pecahan.

Oleh karena itu, setiap text style di Figma wajib memiliki *line-height* eksplisit dengan nilai bilangan bulat yang merupakan kelipatan 4px:
- Teks 12px (Caption): line-height 16px (4 × 4).
- Teks 14px (Body Small): line-height 20px (5 × 4).
- Teks 16px (Body Regular): line-height 24px (6 × 4).
- Teks 20px (Heading 3): line-height 28px (7 × 4).
- Teks 24px (Heading 2): line-height 32px (8 × 4).
- Teks 32px (Heading 1): line-height 40px (10 × 4).

Ketika line-height dikunci pada kelipatan 4px, kartu dan blok konten apa pun yang berisi teks multi-baris akan selalu memiliki total tinggi yang genap dan presisi saat dibungkus Auto Layout.

#### 4. Syarah Kaidah 4: Kontras Warna Beroperasi Berdasarkan Perceived Luminance (Luminansi Relatif), Bukan Nilai Hex RGB
Secara biologis, retina mata manusia memiliki reseptor sel kerucut (cones) yang sangat sensitif terhadap panjang gelombang hijau dan merah, tetapi jauh lebih tidak sensitif terhadap biru murni. Formula luminansi relatif fotometrik standar sRGB mendefinisikan kontras:
`L = 0.2126 × R + 0.7152 × G + 0.0722 × B`

Perhatikan bahwa komponen hijau (Green) menyumbang lebih dari 71% dari total kecerahan yang dirasakan mata, sementara biru (Blue) hanya menyumbang 7.2%. Itulah sebabnya teks kuning (#FFFF00) di atas putih terasa menusuk dan sulit dibaca, sedangkan teks biru tua (#000088) di atas putih terasa sangat kontras.

Standar WCAG 2.1 menetapkan:
- **Teks Reguler (< 18pt normal atau < 14pt tebal):** Wajib rasio kontras minimal 4.5:1 (AA) atau 7.0:1 (AAA).
- **Teks Besar (≥ 18pt normal atau ≥ 14pt tebal):** Wajib rasio kontras minimal 3.0:1 (AA) atau 4.5:1 (AAA).
- **Elemen Antarmuka & Ikon Grafis (Borders, Focus States):** Wajib rasio kontras minimal 3.0:1 terhadap latar belakang sekitarnya.

#### 5. Syarah Kaidah 5: Abstraksi Palet Warna Terdiri dari Tiga Lapisan Taksonomi: Primitif, Semantik, dan Komponen
Jika seorang desainer langsung mewarnai tombol dengan `#0066FF`, apa yang terjadi ketika perusahaan memutuskan untuk mengubah warna brand dari biru ke ungu, atau ketika sistem harus mendukung tema Gelap (*Dark Mode*)? Seluruh ribuan artboard dan ratusan file komponen harus diedit satu per satu.

Arsitektur token warna membagi palet ke dalam 3 tier taksonomi:
1. **Tier 1 (Primitive Ramp):** Kamus warna mentah yang dinamai berdasarkan rona (*hue*) dan bobot luminositas numerik: `blue-50`, `blue-100`, ..., `blue-500`, ..., `blue-900`.
2. **Tier 2 (Semantic Tokens):** Menautkan peran antarmuka (*role/intent*) ke token primitif:
   - `color-surface-base`: `neutral-50` (pada Light Mode) atau `neutral-900` (pada Dark Mode).
   - `color-action-primary`: `blue-500` (pada Light Mode) atau `blue-400` (pada Dark Mode).
   - `color-feedback-danger`: `red-500`.
3. **Tier 3 (Component Tokens):** Menautkan bagian spesifik komponen ke semantic token:
   - `button-primary-bg`: `color-action-primary`.
   - `input-border-error`: `color-feedback-danger`.

Dengan 3 layer ini, perombakan tema, rebranding, atau adaptasi Dark Mode dapat dieksekusi dalam hitungan detik tanpa menyentuh struktur geometri komponen satu pun.

---

### LAYER 4: FIELD PLAYBOOK (TACTICAL SOP & CODE)

#### Template Definisi CSS Variables untuk Arsitektur Token 3-Tier

```css
/* ==========================================================================
   TIER 1: PRIMITIVE TOKENS (Palet Mentah)
   ========================================================================== */
:root {
  --primitive-blue-50:  #eff6ff;
  --primitive-blue-500: #3b82f6;
  --primitive-blue-600: #2563eb;
  --primitive-neutral-50:  #f8fafc;
  --primitive-neutral-100: #f1f5f9;
  --primitive-neutral-800: #1e293b;
  --primitive-neutral-900: #0f172a;
  --primitive-red-500:     #ef4444;
}

/* ==========================================================================
   TIER 2: SEMANTIC TOKENS (Light Mode Default)
   ========================================================================== */
:root {
  --color-surface-bg:        var(--primitive-neutral-50);
  --color-surface-card:      #ffffff;
  --color-text-primary:      var(--primitive-neutral-900);
  --color-text-secondary:    #64748b;
  --color-action-primary:    var(--primitive-blue-600);
  --color-action-hover:      var(--primitive-blue-500);
  --color-feedback-danger:   var(--primitive-red-500);
}

/* SEMANTIC TOKENS (Dark Mode Override) */
[data-theme="dark"] {
  --color-surface-bg:        var(--primitive-neutral-900);
  --color-surface-card:      var(--primitive-neutral-800);
  --color-text-primary:      var(--primitive-neutral-50);
  --color-text-secondary:    #94a3b8;
  --color-action-primary:    var(--primitive-blue-500);
  --color-action-hover:      var(--primitive-blue-600);
}

/* ==========================================================================
   TIER 3: COMPONENT USAGE (Contoh Tombol)
   ========================================================================== */
.btn-primary {
  background-color: var(--color-action-primary);
  color: #ffffff;
  padding: 8px 16px;       /* 8pt Grid */
  border-radius: 8px;
  font-size: 16px;
  line-height: 24px;       /* 4pt Vertical Rhythm */
  transition: background-color 0.15s ease-in-out;
}

.btn-primary:hover {
  background-color: var(--color-action-hover);
}
```

---

### LAYER 5: DIAGNOSTIC DRILL (STUDI KASUS & UJI MANDIRI)

#### Skenario Kasus Nyata
Sebuah aplikasi perbankan B2B meluncurkan fitur audit transaksi baru. Setelah rilis, tim CS menerima ratusan komplain dari pengguna di lapangan (para akuntan senior):
1. Pengguna mengeluhkan mata cepat lelah saat membaca tabel mutasi laporan yang berisi ratusan baris.
2. Saat aplikasi dibuka di monitor laptop 13 inci luar ruangan, teks instruksi berwarna abu-abu muda `#999999` di atas background putih `#FFFFFF` sama sekali tidak terlihat.
3. Jarak antar baris tabel terasa melompat-lompat dan tidak konsisten ketika terdapat baris dengan catatan multi-line.

Audit desain menemukan bahwa desainer menggunakan ukuran font 13px dengan line-height browser bawaan (normal), padding sel tabel diisi secara acak (7px atas, 11px bawah, 13px samping), dan warna teks abu-abu dipilih hanya karena terlihat "estetik dan minimalis di monitor Mac desainer".

#### Lembar Uji Mandiri (3 Pertanyaan Kritis)
1. Berapa rasio kontras aktual antara warna teks abu-abu `#999999` dengan background `#FFFFFF`, dan apakah nilai tersebut memenuhi ambang batas minimum WCAG 2.1 AA untuk teks reguler?
2. Mengapa kombinasi font 13px dengan line-height browser bawaan dan padding ganjil (7px, 11px) merusak keterbacaan tabel dan menyebabkan mata cepat lelah?
3. Rancang perbaikan sistem spasial dan tipografi berbasis standar 8pt grid dan kalkulasi kontras WCAG AAA untuk sel tabel tersebut.

#### Kunci Jawaban Lengkap & Analisis Anti-Pattern

1. **Kalkulasi Rasio Kontras #999999 vs #FFFFFF:**
   - Luminansi `#FFFFFF` (L_1) = 1.0.
   - Luminansi `#999999` (L_2) = 0.318.
   - Rasio kontras: (1.0 + 0.05) / (0.318 + 0.05) = 1.05 / 0.368 ≈ 2.85:1.
   - **Analisis Kepatuhan:** Nilai 2.85:1 **GAGAL** memenuhi standar WCAG AA (syarat minimum teks reguler: 4.5:1). Ini adalah pelanggaran aksesibilitas berat yang membuat teks tidak terbaca oleh pengguna dengan penurunan sensitivitas kontras atau pada lingkungan beriluminasi tinggi. Untuk memenuhi syarat minimal 4.5:1, warna teks abu-abu paling terang yang diizinkan adalah `#757575` (rasio 4.6:1), atau lebih aman `#595959` (rasio 7.0:1 untuk standar AAA).
2. **Penyebab Kelelahan Mata & Ketidakseimbangan Vertikal:**
   - Ukuran font 13px berada di bawah batas nyaman mata normal untuk data padat (standar minimum body data: 14px atau 16px).
   - Line-height bawaan menghasilkan angka pecahan sub-pixel (misal: 13 × 1.2 = 15.6px). Ketika dikombinasikan dengan padding atas 7px dan bawah 11px, total tinggi baris menjadi: 7 + 15.6 + 11 = 33.6px.
   - Angka desimal ini memaksa browser merender baseline teks pada posisi anti-aliasing yang blur. Selain itu, asimetri padding (7px vs 11px) membuat teks terlihat melayang ke atas (*unbalanced baseline*), memaksa otot mata bekerja ekstra keras untuk melacak baris horizontal saat membaca data numerik.
3. **Rekomendasi Rekayasa Perbaikan Deterministik:**
   - **Tipografi:** Gunakan font 14px dengan line-height dikunci mutlak ke **20px** (kelipatan 4px).
   - **Warna Teks:** Ubah teks data menjadi semantic token `text-primary` (`#0f172a`, rasio 15.8:1) dan teks metadata/timestamp menjadi `text-secondary` (`#475569`, rasio 7.4:1 - memenuhi WCAG AAA).
   - **Padding Sel Tabel:** Terapkan padding simetris berbasis 8pt grid: **12px vertikal** (4px half-grid) dan **16px horizontal** (8px grid).
   - **Total Tinggi Baris Tabel:** 12px (top) + 20px (line-height) + 12px (bottom) = 44px (tepat memenuhi standar minimum target sentuh dan modularitas antarmuka).
