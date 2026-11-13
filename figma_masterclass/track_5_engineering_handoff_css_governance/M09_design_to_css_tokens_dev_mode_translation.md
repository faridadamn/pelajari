# Modul 09: Design-to-CSS Translation, Dev Mode & Asset Pipelines

> "Hand-off yang sukses bukanlah saat desainer mengirimkan tautan file Figma kepada developer lalu berdoa; hand-off yang sukses adalah ketika desain dan kode berbicara dalam bahasa token yang identik."

## Modul 09: Design-to-CSS Translation, Dev Mode & Asset Pipelines

---

### LAYER 1: KAIDAH EMAS (CORE AXIOMS)

1. **Dev Mode adalah Jembatan Kompilasi Semantik, Bukan Sekadar Penggaris Digital Pengukur Piksel:** Dev Mode Figma mengabstraksi kanvas visual menjadi representasi kode struktural (CSS, Swift, Kotlin, React JSX). Nilai yang diinspeksi oleh developer bukan lagi koordinat absolut (X, Y), melainkan nama token semantik, status Auto Layout Flexbox, dan properti komponen yang terhubung langsung ke repositori kode.
2. **Translasi Box Model Wajib Mematuhi Box-Sizing: Border-Box Secara Konsisten:** Seluruh kalkulasi padding, stroke (border), dan ukuran frame di Figma mencerminkan aturan CSS `box-sizing: border-box`. Ketebalan border dihitung ke dalam dimensi total elemen, mencegah terjadinya bug pergeseran layout 1px (*1px border shift bug*) saat diimplementasikan ke browser.
3. **Ekspor Vektor SVG Wajib Melewati Pipeline Sanitasi dan Normalisasi ViewBox:** Aset SVG yang diekspor langsung dari kanvas seringkali mengandung metadata kotor editor (`id`, `xmlns:xlink`, `clip-path` redundan). Pipeline ekspor profesional wajib menormalisasi *viewBox* (misal: `0 0 24 24`), mengonversi teks menjadi path kurva, dan menghapus seluruh artefak metadata biner.
4. **Code Connect Menautkan Instance Figma ke Komponen Nyata di Storybook dan Repositori Kode:** Menggunakan fitur *Figma Code Connect*, developer tidak melihat kode CSS generik otomatis, melainkan cuplikan kode komponen produksi nyata tim mereka sendiri (misal: `<Button hierarchy="primary" icon={<SendIcon />} />`) lengkap dengan dokumentasi props yang valid.
5. **Kebijakan Zero Inline Base64 Raster pada Aset Grafis Vektor:** Ikon dan ilustrasi antarmuka dilarang keras memuat gambar raster biner yang di-embed (`data:image/png;base64`) di dalam file SVG; seluruh aset visual wajib merupakan kurva matematika murni (*pure vector paths*) demi menjaga ketajaman resolusi tak terbatas dan ukuran payload mikro (< 2KB).

---

### LAYER 2: MENTAL MODEL & DIAGRAM ASCII

```text
[DEV MODE: BRIDGING DESIGN CANVAS TO CODE ENGINE]
FIGMA INSPECTOR CANVAS                  DEVELOPER CODE PARITY
┌──────────────────────────────┐         ┌──────────────────────────────┐
│ Frame: "Card/Article"        │         │ .card-article {              │
│ • Auto Layout: Vertical      │ ──────► │   display: flex;             │
│ • Padding: 16px 24px         │         │   flex-direction: column;    │
│ • Gap: 12px                  │         │   padding: 16px 24px;        │
│ • Fill: Token(surface-card)  │         │   gap: 12px;                 │
│ • Radius: Token(radius-md)   │         │   background: var(--surface);│
│ • Stroke: 1px Token(border)  │         │   border-radius: var(--rad); │
│ • Resizing: Fill Container   │         │   border: 1px solid var(--b);│
└──────────────────────────────┘         │   width: 100%;               │
                                         │   box-sizing: border-box;    │
                                         │ }                            │
                                         └──────────────────────────────┘

[SVG ASSET NORMALIZATION PIPELINE]
DIRTY FIGMA EXPORT (3.8 KB):
<svg width="28" height="27" viewBox="2 1 28 27" xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs><clipPath id="clip0_123_45"><rect width="28" height="27" .../></clipPath></defs>
  <g clip-path="url(#clip0_123_45)"><path d="..." fill="#333333"/></g>
</svg>
                          │
                          ▼ Sanitasi & Minifikasi (SVGO Pipeline)
CLEAN PRODUCTION SVG (420 Bytes):
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
  <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
</svg>
(Bebas ID acak, viewBox terpusat, mendukung Pewarnaan Dinamis via `currentColor`)
```

Formula Mapping Box-Sizing Border-Box:
`Total_Width = Content_Width + Padding_Left + Padding_Right + Border_Left + Border_Right`

---

### LAYER 3: SYARAH DAGING (DEEP DIVE KNOWLEDGE)

#### 1. Syarah Kaidah 1: Dev Mode adalah Jembatan Kompilasi Semantik, Bukan Sekadar Penggaris Digital Pengukur Piksel
Di masa lalu, proses hand-off desain ke developer dikenal dengan istilah "Redlining": desainer menghabiskan waktu berjam-jam menggambar garis merah untuk menunjukkan jarak 16px dari tombol ke batas tepi kartu, lengkap dengan anotasi manual kode warna HEX `#2563EB`.

*Figma Dev Mode* memutus inefisiensi ini secara radikal:
- **Status Inspeksi Terpisah:** Developer memiliki ruang kerja khusus yang tidak bisa menggeser atau merusak artboard secara tidak sengaja.
- **Deteksi Perubahan Komparatif (*Compare Changes*):** Developer dapat membandingkan versi desain saat ini dengan versi sebelumnya (seperti `git diff`), melihat secara visual layer mana yang dipindahkan, diubah warnanya, atau dihapus.
- **Inspeksi Berbasis Token:** Saat developer mengarahkan kursor ke sebuah tombol, inspector tidak menampilkan `#3B82F6`, melainkan menampilkan token `var(--color-primary-bg)`. Ini mengeliminasi 100% perdebatan warna dan menjamin integritas desain sistem langsung ke codebase.

#### 2. Syarah Kaidah 2: Translasi Box Model Wajib Mematuhi Box-Sizing: Border-Box Secara Konsisten
Dalam CSS klasik, properti default adalah `box-sizing: content-box`. Artinya, jika Anda membuat kotak dengan lebar 300px, lalu menambahkan padding 20px di kiri dan kanan serta border 1px, lebar fisik kotak tersebut di browser membengkak menjadi:
300 + 20 + 20 + 1 + 1 = **342.2px**!

Figma Auto Layout beroperasi secara default menggunakan model modern: `box-sizing: border-box`.
Ketika sebuah Frame Auto Layout diberi lebar 300px dan padding 20px, total lebar frame tetap terkunci pada 300px, sedangkan ruang konten di dalamnya yang mengecil menjadi 260px (300 - 40).
Pengaturan ini harus dipahami secara mutual oleh desainer dan front-end engineer:
Pada file CSS global (reset CSS), pastikan deklarasi berikut selalu terpasang:
`*, *::before, *::after { box-sizing: border-box; }`
Tanpa deklarasi ini, seluruh ukuran komponen yang diimplementasikan dari Figma akan terlihat lebih besar dan meledak mematahkan grid responsif di browser.

#### 3. Syarah Kaidah 3: Ekspor Vektor SVG Wajib Melewati Pipeline Sanitasi dan Normalisasi ViewBox
SVG (*Scalable Vector Graphics*) adalah dokumen XML berbasis teks. Ketika seorang desainer mengekspor ikon langsung dari kanvas tanpa persiapan:
- Seringkali ukuran bounding box tidak beraturan (misal: 23.4 × 24.1px).
- Seringkali terdapat tag `<clipPath>` dan ID acak seperti `id="clip0_491_20"`. Jika ada 10 ikon berbeda dengan ID yang sama di halaman web yang sama, browser akan mengalami tabrakan ID (*ID collision bug*), menyebabkan ikon kedua salah merender bentuk ikon pertama!
- Warna di-hardcode ke atribut `fill="#000000"`, sehingga developer tidak bisa mengubah warna ikon saat hover via CSS.

Pipeline Normalisasi SVG:
1. Pastikan ikon dibungkus di dalam Frame berukuran bulat integer (misal: tepat 24 × 24px).
2. Lakukan *Flatten* (`Ctrl+E`) pada kurva internal.
3. Hapus fill latar belakang frame (transparan).
4. Ubah warna kurva menjadi token atau biarkan developer menggantinya dengan `fill="currentColor"` (atau `stroke="currentColor"`). Dengan `currentColor`, ikon akan otomatis mewarisi warna teks elemen induknya di CSS!

#### 4. Syarah Kaidah 4: Code Connect Menautkan Instance Figma ke Komponen Nyata di Storybook dan Repositori Kode
Salah satu fitur paling mutakhir untuk tim enterprise adalah *Figma Code Connect*.
Masalah klasik hand-off:
Desainer membuat instance dari komponen `Button` dengan properti `hierarchy = "destructive"` dan `size = "small"`. Saat developer membuka Dev Mode, jika tanpa Code Connect, inspector hanya menampilkan kode CSS mentah (`background: red; font-size: 14px;`). Developer pemula mungkin akan tergoda untuk menyalin CSS tersebut dan membuat tag `<button>` baru, bukannya memanggil komponen React yang sudah ada di repositori!

Dengan Code Connect:
Tim engineering menghubungkan repositori React/iOS mereka ke Figma via CLI. Saat developer mengklik tombol tersebut di Dev Mode, panel samping langsung menampilkan kode produksi verbatim:
```jsx
<Button variant="destructive" size="sm" onClick={handleDelete}>
  Hapus Akun
</Button>
```
Lengkap dengan link langsung menuju Storybook dan dokumentasi internal tim. Ini menjembatani paritas 1-to-1 antara desain sistem dan repositori kode.

#### 5. Syarah Kaidah 5: Kebijakan Zero Inline Base64 Raster pada Aset Grafis Vektor
Kadang desainer junior mengimpor logo dari format PNG atau PDF lama ke Figma, lalu mengekspornya kembali sebagai SVG. Secara visual di kanvas terlihat seperti vektor, tetapi saat file SVG tersebut dibuka di teks editor, isinya adalah:
`<image width="500" height="500" xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA..." />`

Ini adalah racun performa antarmuka:
- Ukuran file membengkak dari 1KB menjadi 150KB.
- Gambar akan pecah dan buram saat dibuka di layar monitor beresolusi tinggi (Retina / 4K).
- Tidak dapat dimanipulasi dengan CSS atau SVG path animation.
Aturan baku: Setiap aset yang diekspor sebagai SVG WAJIB merupakan kurva vektor murni (`<path>`, `<rect>`, `<circle>`). Jika gambar memiliki gradasi fotorealistik kompleks yang tidak bisa divektorkan, ekspor gambar tersebut sebagai WebP atau AVIF modern, jangan pernah menyelipkannya sebagai base64 di dalam SVG.

---

### LAYER 4: FIELD PLAYBOOK (TACTICAL SOP & CODE)

#### Skrip Pipeline Sanitasi Ekspor SVG Otomatis (Node.js SVGO Script)

```javascript
// scripts/clean-svg.mjs
import fs from 'fs';
import path from 'path';
import { optimize } from 'svgo';

const SVG_DIR = './src/assets/icons';

const config = {
  multipass: true,
  plugins: [
    { name: 'removeViewBox', active: false },
    { name: 'removeDimensions', active: true },
    { name: 'cleanupIds', active: true },
    {
      name: 'addAttributesToSVGElement',
      params: {
        attributes: [{ fill: 'currentColor' }]
      }
    }
  ]
};

const files = fs.readdirSync(SVG_DIR).filter(f => f.endsWith('.svg'));

console.log(`[+] Memproses ${files.length} ikon SVG...`);
for (const file of files) {
  const filePath = path.join(SVG_DIR, file);
  const rawSvg = fs.readFileSync(filePath, 'utf-8');
  const result = optimize(rawSvg, { path: filePath, ...config });
  fs.writeFileSync(filePath, result.data, 'utf-8');
  console.log(`    Optimized: {file} ({rawSvg.length}B -> ${result.data.length}B)`);
}
console.log('[*] Seluruh ikon bersih dan siap dikonsumsi sebagai React Component!');
```

#### SOP Verifikasi Hand-Off Developer (Ready for Dev Checklist):
1. [ ] Pastikan Frame utama ditandai dengan badge **Ready for Dev** (ikon hijau di pojok kanan atas).
2. [ ] Periksa apakah ada layer tersembunyi yang tidak terpakai; lakukan pembersihan (*purge unused layers*).
3. [ ] Pastikan seluruh warna dan tipografi terikat pada Styles/Variables resmi, tidak ada kode warna hex *unlinked*.
4. [ ] Sertakan link tiket Jira / Notion Task dan link Storybook pada panel deskripsi komponen.

---

### LAYER 5: DIAGNOSTIC DRILL (STUDI KASUS & UJI MANDIRI)

#### Skenario Kasus Nyata
Sebuah agensi pengembang web sedang meluncurkan website baru untuk klien korporat. Setelah implementasi kode selesai oleh tim front-end, tim desainer melakukan audit *Design QA* dan menemukan lebih dari 40 perbedaan visual (*visual regressions*):
1. Seluruh kartu artikel di website terlihat 2px lebih tinggi dan 2px lebih lebar dibanding ukuran di Figma.
2. Ikon centang hijau di dalam tombol berhasil muncul di Google Chrome desktop, namun di Safari iOS ikon tersebut berubah menjadi kotak hitam pekat yang merusak tampilan.
3. Developer mengeluh: *"Desainer menaruh warna abu-abu `#2A323D` di navbar, `#2B333E` di footer, dan `#29313C` di sidebar. Kami pusing menentukan warna mana yang benar, jadi kami hardcode saja semuanya."*

#### Lembar Uji Mandiri (3 Pertanyaan Kritis)
1. Mengapa seluruh kartu di website menjadi 2px lebih besar di browser dibanding ukuran di Figma, dan deklarasi CSS apa yang hilang di sisi developer?
2. Mengapa ikon centang hijau berubah menjadi kotak hitam pekat di Safari iOS?
3. Solusi tata kelola apa yang harus diterapkan di Figma untuk menghentikan munculnya variasi warna abu-abu "kembar tetapi beda 1 bit" tersebut selamanya?

#### Kunci Jawaban Lengkap & Analisis Anti-Pattern

1. **Akar Masalah Pembengkakan Ukuran 2px:** Kartu di Figma memiliki ketebalan border (stroke) sebesar 1px di seluruh sisi. Di Figma, border tersebut dihitung dengan model `border-box`. Namun di file CSS website, developer lupa menambahkan deklarasi global `box-sizing: border-box`. Akibatnya, browser merender dengan `content-box`, menambahkan 1px border kiri + 1px border kanan (+2px lebar) dan 1px border atas + 1px border bawah (+2px tinggi).
   - **Solusi CSS:** Tambahkan deklarasi di root stylesheet: `*, *::before, *::after { box-sizing: border-box; }`.
2. **Penyebab Ikon Menjadi Kotak Hitam di Safari iOS:** Ini adalah bug klasik ekspor SVG di mana desainer menggunakan fitur *Masking* atau *Clipping Path* internal dengan ID acak, atau kurva vektor tidak di-expand (*unflattened strokes*). Engine WebKit di Safari memiliki penanganan `<clipPath>` yang sangat ketat: jika elemen mask memiliki transformasi koordinat ganjil atau nilai ID yang duplikat dengan elemen lain di halaman, Safari membatalkan pemotongan mask dan merender seluruh area bounding box poligon sebagai warna hitam pekat default (`#000000`).
   - **Solusi:** Buka ikon di Figma, pilih layer vektor, lakukan *Flatten* (`Ctrl+E`), pastikan tidak ada layer mask yang tersisa, dan ekspor ulang sebagai path murni.
3. **Solusi Tata Kelola Warna Anti-Kembar:** Tiga warna abu-abu tersebut (`#2A323D`, `#2B333E`, `#29313C`) adalah contoh nyata dari *Color Drift Pollution* akibat desainer menggunakan color-picker tetes manual di kanvas.
   - **Tindakan Perbaikan:** Kunci sistem palet warna dengan **Figma Variables**.
   - Hapus hak edit variabel bebas bagi desainer produk umum.
   - Buat satu token semantik resmi: `color-surface-dark = #2A323D`.
   - Jalankan plugin *Design System Linter* untuk memindai seluruh kanvas: setiap layer yang menggunakan warna heksadesimal unlinked akan ditolak dan wajib di-relink ke token resmi sebelum status artboard dapat diubah menjadi *Ready for Dev*.
