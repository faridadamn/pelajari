# Modul 04: Component Architecture, Atomic Design & Variant Matrices

> "Komponen antarmuka yang baik bukan sekadar simbol grafis yang bisa di-copy-paste, melainkan kontrak arsitektur perangkat lunak yang memisahkan definisi logika dari instansiasi visual."

## Modul 04: Component Architecture, Atomic Design & Variant Matrices

---

### LAYER 1: KAIDAH EMAS (CORE AXIOMS)

1. **Prinsip Single Source of Truth (SSOT): Master Component Menentukan Kontrak Struktur, Instance Mewarisi Nilai Dinamis:** Master Component (`❖`) adalah cetak biru mutlak. Setiap perubahan geometri, padding, dan susunan layer pada Master Component akan otomatis diteruskan ke seluruh Instance (`◇`). Instance hanya diizinkan menyimpan *overrides* pada properti visual permukaan (teks, warna isi, visibilitas ikon, gambar latar).
2. **Hukum Larangan Keras Detach Component:** Melepaskan keterikatan komponen (*Detach Instance* / `Ctrl+Alt+B`) adalah anti-pattern fatal yang merusak integritas sistem desain. Kebutuhan variasi visual baru wajib diselesaikan melalui penambahan properti, varian, atau slot instansiasi (*Instance Swap*), bukan dengan memutus relasi inheritance.
3. **Metodologi Atomic Design Menyusun Hierarki Komponen Secara Skalabel dan Berlapis:** Antarmuka disusun secara piramidal dari Atoms (token warna, ikon, label teks), Molecules (tombol, input text field), Organisms (header navigasi, product card), hingga Templates dan Pages. Komponen tingkat tinggi dilarang memanipulasi geometri atom secara langsung tanpa melalui API properti yang sah.
4. **Component Properties (Boolean, Text, Instance Swap) Memotong Ledakan Varian (Variant Explosion) Hingga Skala Logaritmik:** Menduplikasi seluruh varian komponen untuk setiap kemungkinan status kecil (misal: tombol dengan ikon kiri vs kanan vs tanpa ikon) menghasilkan perkalian kartesian (2 × 3 × 4 = 24 varian). Memindahkan status tersebut ke *Component Properties* ortogonal mereduksinya menjadi varian status esensial saja.
5. **Variant Matrix Wajib Dinamai Berdasarkan Status Eksklusif (Mutually Exclusive), Bukan Gabungan Bebas:** Properti varian hanya boleh digunakan untuk status yang tidak bisa eksis bersamaan (misal: `State = Default | Hover | Pressed | Disabled` atau `Size = Small | Medium | Large`). Status independen wajib diubah menjadi properti Boolean atau Swap.

---

### LAYER 2: MENTAL MODEL & DIAGRAM ASCII

```text
[SINGLE SOURCE OF TRUTH: MASTER vs INSTANCE]
┌───────────────────────────────────────┐
│ Master Component (❖ Button)           │
│ • Layout: Auto Layout Horizontal      │
│ • Padding: 12px 24px | Radius: 8px    │
│ • Master Style: Primary Blue          │
└──────────────────┬────────────────────┘
                   │ Inheritance
         ┌─────────┴─────────┐
         ▼                   ▼
┌──────────────────┐  ┌────────────────────────────────────┐
│ Instance A (◇)   │  │ Instance B (◇)                     │
│ Overrides:       │  │ Overrides:                         │
│ Text: "Kirim"    │  │ Text: "Batal"                      │
│ Icon: Send.svg   │  │ Fill: Danger Red (Allowed Override)│
└──────────────────┘  └────────────────────────────────────┘

[VARIANT EXPLOSION MITIGATION MATRIX]
PENDEKATAN LAMA (Kartesian Murni):
Size (3) × Type (3) × HasIconLeft (2) × HasIconRight (2) × State (4)
Total = 3 × 3 × 2 × 2 × 4 = 144 VARIAN TERPISAH! (File berat, maintenance neraka)

PENDEKATAN MODERN (Component Properties + Varian Inti):
Varian Inti: Size (3) × Type (3) × State (4) = 36 Varian.
Properti Ortogonal di dalam Varian:
  - Boolean: `showIconLeft` (True/False)
  - Boolean: `showIconRight` (True/False)
  - Instance Swap: `iconLeftAsset` -> Slot Ikon
  - Text Property: `buttonLabel` -> "Label Teks"
Total Varian Fisik Turun dari 144 menjadi 36 (Efisiensi 75%)!
```

Formula Kompleksitas Matriks Varian Kartesian:
`Total_Varian = Π(Jumlah_Pilihan_Setiap_Properti)`

---

### LAYER 3: SYARAH DAGING (DEEP DIVE KNOWLEDGE)

#### 1. Syarah Kaidah 1: Prinsip Single Source of Truth (SSOT): Master Component Menentukan Kontrak Struktur, Instance Mewarisi Nilai Dinamis
Dalam rekayasa piranti lunak berorientasi objek (OOP), Master Component di Figma analog dengan sebuah *Class*, sedangkan Instance adalah *Object Instantiation*. Ketika Anda membuat 500 halaman dengan tombol "Daftar", tombol-tombol tersebut tidak berdiri sendiri.

Figma memiliki engine pelacakan *overrides* yang sangat canggih. Jika Anda mengubah label teks pada Instance dari "Button" menjadi "Beli Tiket", Figma mencatat override teks tersebut pada ID layer lokal. Namun, ketika sang desainer sistem memperbarui Master Component—misalnya mengubah sudut membulat (*corner radius*) dari 4px menjadi 12px, atau mengganti warna dasar—seluruh 500 Instance akan langsung menerima pembaruan tersebut secara instan tanpa menghapus teks "Beli Tiket" yang sudah Anda tulis.

#### 2. Syarah Kaidah 2: Hukum Larangan Keras Detach Component
Salah satu dosa terbesar desainer dalam tim kolaboratif adalah menekan tombol *Detach Component* (`Ctrl+Alt+B` atau klik kanan > Detach). Alasan klasik desainer melakukan detach adalah: *"Saya butuh tombol ini tapi ada ikon kecil di tengahnya yang tidak didukung oleh komponen utama"*.

Ketika komponen di-detach:
- Keterikatan dengan sistem desain terputus selamanya.
- Komponen tersebut menjadi "anak yatim" (*orphaned pixels*) yang tidak akan pernah menerima update warna, audit aksesibilitas, atau perbaikan bug di masa depan.
- File desain membengkak karena memory tree menduplikasi seluruh data vektor secara mentah.
- Developer bingung saat memeriksa kode: apakah ini komponen resmi yang sudah ada di repositori React/Flutter, atau komponen custom baru yang harus dibuatkan kode dari nol?

Jika komponen tidak mendukung kebutuhan Anda, lakukan salah satu dari tiga tindakan arsitektural:
1. Hubungi tim Design System untuk merilis variasi properti resmi.
2. Gunakan teknik *Slot Component* (komponen kontainer dengan Instance Swap kosong).
3. Buat sub-komponen baru yang mengekstensi komponen dasar tersebut.

#### 3. Syarah Kaidah 3: Metodologi Atomic Design Menyusun Hierarki Komponen Secara Skalabel dan Berlapis
Diperkenalkan oleh Brad Frost, metodologi *Atomic Design* menjadi standar baku dalam penyusunan sistem antarmuka di Figma:
- **Atoms (Atom):** Blok pembangun dasar yang tidak dapat dipecah lagi tanpa kehilangan fungsi visualnya. Contoh: Ikon SVG 24px, Token Warna, Token Spasial, Label Tipografi, Avatar bulatan.
- **Molecules (Molekul):** Kumpulan atom yang terikat bersama untuk membentuk unit fungsional tunggal. Contoh: Tombol (Teks + Ikon + Frame Background), Input Field (Label + Form Border + Placeholder + Ikon Hapus).
- **Organisms (Organisme):** Kumpulan molekul dan atom yang membentuk bagian utuh dari antarmuka pengguna. Contoh: Header Navigasi (Logo + Search Input + Menu Navigasi + Tombol Profil), Product Card (Gambar + Badge Diskon + Judul + Rating + Harga + Tombol Add-to-Cart).
- **Templates:** Struktur tata letak halaman yang menghubungkan berbagai organisme dalam grid tanpa isi data nyata (wireframe presisi tinggi).
- **Pages:** Template yang diinjeksi dengan konten data nyata (teks, gambar, angka transaksi riil).

#### 4. Syarah Kaidah 4: Component Properties (Boolean, Text, Instance Swap) Memotong Ledakan Varian (Variant Explosion) Hingga Skala Logaritmik
Di era awal Figma, satu-satunya cara membuat tombol yang memiliki ikon di sebelah kiri adalah dengan membuat varian baru bernama `IconLeft = True`. Jika tombol tersebut juga bisa memiliki ikon kanan, dibuat varian `IconRight = True`. Jika ada 3 ukuran (Small, Medium, Large) dan 4 status (Default, Hover, Active, Disabled), jumlah varian fisik yang harus digambar di kanvas melonjak menjadi:
2 × 2 × 3 × 4 = 48 varian.

Dengan *Component Properties*:
1. **Boolean Property (`showIconLeft`, `showIconRight`):** Diterapkan pada visibilitas layer ikon di panel kanan. Desainer dapat menyembunyikan atau memunculkan ikon cukup dengan toggle switch on/off pada inspector, tanpa membutuhkan varian terpisah!
2. **Instance Swap Property (`iconLeftChoice`):** Menautkan layer ikon ke library ikon global. Pengguna dapat mengganti ikon panah menjadi ikon unduh langsung dari dropdown inspector.
3. **Text Property (`labelContent`):** Mengekspos string teks ke panel properti atas, mempercepat pengisian konten tanpa perlu melakukan double-click berkali-kali ke dalam layer terdalam.

Dengan memisahkan properti ortogonal ini, jumlah varian fisik yang perlu digambar di kanvas menyusut drastis menjadi hanya 3 × 4 = 12 varian saja!

#### 5. Syarah Kaidah 5: Variant Matrix Wajib Dinamai Berdasarkan Status Eksklusif (Mutually Exclusive), Bukan Gabungan Bebas
Varian di dalam sebuah *Component Set* harus diposisikan seperti *State Machine* dalam pemrograman:
- Sebuah tombol tidak mungkin berada dalam status `Hover` DAN `Disabled` secara bersamaan (keduanya bersifat saling meniadakan / *mutually exclusive*). Oleh karena itu, jadikan keduanya sebagai nilai dari properti `State`.
- Sebuah tombol tidak mungkin berukuran `Small` DAN `Large` secara bersamaan. Jadikan keduanya nilai dari properti `Size`.
- Namun, apakah tombol `Large` bisa memiliki ikon? YA. Karena kepemilikan ikon independen dari ukuran, kepemilikan ikon TIDAK BOLEH dijadikan varian; ia wajib dijadikan *Boolean Property*.

Aturan baku penamaan properti di Figma:
Gunakan huruf besar untuk nama properti dan nilai terstandarisasi:
`Size = Small | Medium | Large`
`Hierarchy = Primary | Secondary | Tertiary | Destructive`
`State = Default | Hover | Focused | Pressed | Disabled`

---

### LAYER 4: FIELD PLAYBOOK (TACTICAL SOP & CODE)

#### Anatomi Arsitektur Komponen: Tombol Standar Industri

```text
[❖ Component Set: Button]
Properties Configured:
  • Variant Property 1: Hierarchy (Primary, Secondary, Outline, Ghost)
  • Variant Property 2: Size (Small, Medium, Large)
  • Variant Property 3: State (Default, Hover, Pressed, Disabled)
  • Boolean Property: hasIconLeft (Default: False)
  • Boolean Property: hasIconRight (Default: False)
  • Instance Swap: iconLeft (Linked to: "Icons/20px/*")
  • Instance Swap: iconRight (Linked to: "Icons/20px/*")
  • Text Property: label (Default: "Button Action")

Total Variants in Set: 4 × 3 × 4 = 48 Variants (Mencakup seluruh status interaktif)
```

#### TypeScript Schema Representasi Component Properties:

```typescript
// Ekivalen TypeScript yang mencerminkan API Figma Component Properties
export interface ButtonProps {
  // Variant Properties (Mutually Exclusive)
  hierarchy?: 'primary' | 'secondary' | 'outline' | 'ghost';
  size?: 'small' | 'medium' | 'large';
  state?: 'default' | 'hover' | 'pressed' | 'disabled';
  
  // Component Properties (Orthogonal)
  label: string;
  hasIconLeft?: boolean;
  hasIconRight?: boolean;
  iconLeft?: React.ComponentType<{ className?: string }>;
  iconRight?: React.ComponentType<{ className?: string }>;
  
  // Event Handlers
  onClick?: () => void;
}
```

---

### LAYER 5: DIAGNOSTIC DRILL (STUDI KASUS & UJI MANDIRI)

#### Skenario Kasus Nyata
Sebuah tim desain di perusahaan teknologi skala unicorn memiliki file komponen tombol yang sangat lambat dimuat. File tersebut berisi satu Component Set raksasa bernama `MegaButton` yang memiliki **384 varian fisik**.
Saat diteliti, desainer sebelumnya membuat properti varian untuk:
- `Size`: Small, Medium, Large (3 nilai)
- `Hierarchy`: Primary, Secondary, Ghost, Danger (4 nilai)
- `State`: Default, Hover, Disabled (3 nilai)
- `Theme`: Light, Dark (2 nilai)
- `Icon`: NoIcon, IconLeft, IconRight, IconBoth (4 nilai)
- `Rounded`: Square, Pill (2 nilai)
Kalkulasi: 3 × 4 × 3 × 2 × 4 × 2 = 576 varian (sebagian varian dihapus manual sehingga tersisa 384).

Akibatnya:
1. Browser sering mengalami tab-crash (*Out of Memory*) saat membuka halaman desain sistem.
2. Ketika tim brand mengubah warna `Primary` dari `#0066FF` menjadi `#4F46E5`, desainer membutuhkan waktu 3 hari penuh untuk mengupdate ratusan varian satu per satu secara manual.
3. Developer menolak menggunakan library Figma karena dropdown varian di inspector terlalu panjang dan membingungkan.

#### Lembar Uji Mandiri (3 Pertanyaan Kritis)
1. Identifikasi 3 properti mana dalam `MegaButton` yang merupakan anti-pattern dan seharusnya TIDAK dijadikan varian fisik?
2. Bagaimana strategi restrukturisasi modern untuk memangkas 384 varian fisik tersebut menjadi kurang dari 40 varian tanpa kehilangan fungsionalitas visual satu pun?
3. Mengapa variasi tema (`Light` vs `Dark`) dilarang keras dibuat sebagai varian komponen di era Figma modern?

#### Kunci Jawaban Lengkap & Analisis Anti-Pattern

1. **Tiga Properti Anti-Pattern yang Bukan Varian Fisik:**
   - `Icon (NoIcon, IconLeft, IconRight, IconBoth)`: Ini adalah kombinasi boolean ortogonal. Memisahkan ikon menjadi varian fisik adalah pemborosan eksponensial.
   - `Theme (Light, Dark)`: Tema adalah layer variabel lingkungan (*contextual mode*), bukan variasi anatomi tombol.
   - `Rounded (Square, Pill)`: Jika sebuah tombol memiliki bentuk Pill untuk konteks tertentu (misal: tombol filter vs tombol form), ini lebih tepat dipisahkan menjadi komponen yang berbeda atau diatur melalui token radius.
2. **Strategi Pemangkasan Varian Drastis:**
   - **Langkah 1 (Eliminasi Tema via Variables):** Hapus seluruh varian Dark Mode. Buat variabel warna Figma dengan dua mode (*Light Mode* dan *Dark Mode*). Varian tombol berkurang separuh (384 / 2 = 192).
   - **Langkah 2 (Migrasi Ikon ke Component Properties):** Hapus variasi IconLeft/IconRight. Di dalam Master Button, pasang dua layer ikon dengan *Boolean Property* `showIconLeft` dan `showIconRight`, serta pasang *Instance Swap*. Varian berkurang hingga seperempatnya (192 / 4 = 48).
   - **Langkah 3 (Konsolidasi Varian Inti):** Hanya pertahankan:
     - `Hierarchy`: Primary, Secondary, Ghost, Danger (4)
     - `Size`: Small, Medium, Large (3)
     - `State`: Default, Hover, Disabled (3)
     Total varian fisik murni: 4 × 3 × 3 = **36 varian**!
   - **Hasil:** Memangkas lebih dari **90%** beban render kanvas, memulihkan performa browser, dan menyederhanakan panel inspector developer.
3. **Mengapa Tema Dilarang Menjadi Varian:**
   Membuat varian Light dan Dark menduplikasi seluruh geometri antarmuka secara redundan. Ketika struktur tombol berubah (misal padding diubah), desainer harus memperbarui tombol dua kali (di versi Light dan versi Dark). Dengan fitur **Figma Variables (Color Modes)**, tombol cukup didesain satu kali menggunakan *Semantic Color Token*. Ketika frame halaman dialihkan ke Dark Mode, engine Figma akan secara otomatis menukar seluruh nilai warna token tanpa membutuhkan duplikasi varian fisik.
