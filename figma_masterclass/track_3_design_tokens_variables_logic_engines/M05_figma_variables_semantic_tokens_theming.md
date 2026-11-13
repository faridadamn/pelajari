# Modul 05: Figma Variables, Semantic Tokens & Multi-Brand Theming

> "Design token adalah jembatan atomik antara niat desain dan implementasi kode; variabel Figma adalah tempat di mana jembatan itu didefinisikan secara resmi."

## Modul 05: Figma Variables, Semantic Tokens & Multi-Brand Theming

---

### LAYER 1: KAIDAH EMAS (CORE AXIOMS)

1. **Empat Tipe Variabel Primitif Figma Mengatur Seluruh Dimensi Fisik dan Logika Antarmuka:**
   - *Color:* Mengatur fills, strokes, dan tint ikon.
   - *Number:* Mengatur padding, gap, corner radius, width, height, dan opacity.
   - *String:* Mengatur salinan teks, placeholder, dan string lokalisasi multibahasa.
   - *Boolean:* Mengatur sakelar visibilitas layer dan kontrol logika kondisional.
2. **Koleksi Variabel Wajib Dipisahkan Secara Ortogonal Antara Lapisan Primitif dan Lapisan Semantik:** Nilai mentah (seperti warna heksadesimal `#2563EB` atau angka `16px`) hanya boleh didefinisikan satu kali di dalam *Primitive Collection*. *Semantic Collection* sama sekali tidak boleh berisi nilai mentah, melainkan hanya berisi referensi alias yang menunjuk ke variabel primitif.
3. **Variable Modes Menyediakan Dimensi Paralel untuk Theming Tanpa Perlu Menduplikasi Frame Kanvas:** Mode variabel adalah kolom-kolom nilai berbeda untuk satu set variabel semantik yang sama. Mengubah mode frame dari "Light" ke "Dark" secara instan menukar seluruh nilai warna tanpa memodifikasi satu pun objek geometris di kanvas.
4. **Token Spasial Numerik Menjaga Kedisiplinan 8pt Grid pada Level Kode:** Mengikat properti padding, gap, dan corner radius ke variabel *Number* (`space-xs: 4`, `space-sm: 8`, `space-md: 16`, `space-lg: 24`) mengeliminasi *magic numbers* dan menjamin konsistensi ritme spasial secara deterministik.
5. **Standarisasi Format Token W3C DTCG Memastikan Portabilitas Penuh Antara Figma, Style Dictionary, dan Repositori Kode:** Arsitektur variabel Figma harus dirancang agar kompatibel dengan spesifikasi W3C Design Tokens Community Group (`value`, `type`, `$description`), memungkinkan sinkronisasi otomatis via GitHub Actions menuju CSS Variables, Tailwind Config, atau iOS/Android tokens.

---

### LAYER 2: MENTAL MODEL & DIAGRAM ASCII

```text
[MULTI-COLLECTION VARIABLE ARCHITECTURE]
┌─────────────────────────────────────────────────────────────┐
│ 1. PRIMITIVE COLLECTION (Global Raw Values)                 │
│    • color/blue/500   = #3B82F6                             │
│    • color/blue/600   = #2563EB                             │
│    • color/slate/50   = #F8FAFC                             │
│    • color/slate/900  = #0F172A                             │
│    • spacing/scale/2  = 8px                                 │
│    • spacing/scale/4  = 16px                                │
└──────────────────────────────┬──────────────────────────────┘
                               │ Alias Linkage (Mapping)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. SEMANTIC COLLECTION (Variable Modes as Columns)          │
│                                                             │
│   Variable Name         | Mode: Light       | Mode: Dark    │
│   ──────────────────────┼───────────────────┼────────────── │
│   surface/page          | color/slate/50    | color/slate/900│
│   surface/card          | #FFFFFF           | color/slate/800│
│   action/primary-bg     | color/blue/600    | color/blue/500│
│   text/primary          | color/slate/900   | color/slate/50│
│   padding/card-inner    | spacing/scale/4   | spacing/scale/4│
└──────────────────────────────┬──────────────────────────────┘
                               │ Applied Directly to UI
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. CANVAS CONSUMPTION (Frame with Mode Switch)              │
│    Frame.setMode("Dark") ──► Seluruh token otomatis berganti│
│                              nilai ke kolom "Mode: Dark"!   │
└─────────────────────────────────────────────────────────────┘
```

Formula Resolusi Token Alias:
`Resolve(Token_Semantic, Mode_Active) → Alias_Pointer → Primitive_Value`

---

### LAYER 3: SYARAH DAGING (DEEP DIVE KNOWLEDGE)

#### 1. Syarah Kaidah 1: Empat Tipe Variabel Primitif Figma Mengatur Seluruh Dimensi Fisik dan Logika Antarmuka
Sebelum hadirnya fitur *Variables*, Figma hanya mengenal *Styles* (Color Styles, Text Styles, Effect Styles). Styles memiliki kelemahan mendasar: mereka hanya bersifat statis dan hanya mendukung nilai visual terbatas. Anda tidak dapat membuat style untuk ukuran padding atau radius sudut.

Variables memperkenalkan 4 tipe data komputasional murni:
1. **Color Variables:** Dapat ditempelkan pada *Fill* (latar belakang), *Stroke* (border garis), dan *Text Color*.
2. **Number Variables:** Dapat ditautkan langsung ke properti fisik geometri:
   - Lebar dan tinggi frame (`width`, `height`).
   - Padding internal (top, right, bottom, left).
   - Jarak antar-elemen Auto Layout (`item spacing / gap`).
   - Sudut kelengkungan (`corner radius` individual maupun seragam).
   - Opasitas layer (`opacity: 0 - 100%`).
3. **String Variables:** Mengikat isi teks di kanvas ke variabel teks. Ini memungkinkan pembuatan prototipe multibahasa instan: satu tombol bertuliskan variabel `str_cta_checkout` yang otomatis berganti teks saat mode dialihkan dari bahasa Inggris ke bahasa Indonesia.
4. **Boolean Variables:** Mengontrol visibilitas layer (`visible: true/false`). Dapat diikatkan ke *Component Properties* untuk mengendalikan logika alur interaktif.

#### 2. Syarah Kaidah 2: Koleksi Variabel Wajib Dipisahkan Secara Ortogonal Antara Lapisan Primitif dan Lapisan Semantik
Kesalahan paling umum yang dilakukan tim pemula saat menyusun Variables adalah mencampurkan nilai warna heksadesimal langsung di samping token semantik di dalam satu koleksi yang sama.

Mengapa pemisahan koleksi (*Multi-Collection Separation*) adalah harga mati?
- **Isolasi Perubahan:** Jika nilai brand biru diperbarui dari `#2563EB` menjadi `#1D4ED8`, Anda hanya perlu mengedit satu variabel saja di *Primitive Collection* (`color/blue/600`). Seluruh semantic token di koleksi kedua (`action/primary-bg`, `border/focus`, `badge/accent`) yang merujuk padanya akan otomatis ter-update secara serentak.
- **Pembersihan Hak Akses & Scope:** Tim desain produk sehari-hari HANYA boleh mengakses dan menerapkan variabel dari *Semantic Collection*. Variabel dari *Primitive Collection* disembunyikan (*Hide from publishing*) agar desainer tidak salah memilih warna mentah yang melanggar aturan desain sistem.

#### 3. Syarah Kaidah 3: Variable Modes Menyediakan Dimensi Paralel untuk Theming Tanpa Perlu Menduplikasi Frame Kanvas
Mode variabel (*Variable Modes*) adalah fitur paling revolusioner dalam workflow desain modern. Bayangkan Anda memiliki desain aplikasi mobile lengkap dengan 40 layar. 

Di masa lalu, untuk menyajikan *Dark Mode*, desainer terpaksa menduplikasi ke-40 layar tersebut, lalu secara manual mengganti warna background menjadi hitam dan teks menjadi putih. Setiap kali ada perubahan fitur di mode terang, desainer harus menyalin perubahan tersebut ke mode gelap secara manual.

Dengan *Variable Modes*:
- Anda hanya mendesain 1 set layar tunggal.
- Setiap elemen diwarnai menggunakan semantic token: `surface/background`, `text/primary`, `action/accent`.
- Buat dua mode di panel Variables: Kolom 1 = `Light`, Kolom 2 = `Dark`.
- Saat Anda menduplikasi frame dan memilih dropdown `Layer > Change Variable Mode > Dark`, seluruh 40 layar seketika berganti menjadi Dark Mode secara sempurna dalam 1 milidetik!

Mekanisme yang sama berlaku untuk:
- **Multi-Brand Theming:** Brand A (Warna Merah, Radius 4px) vs Brand B (Warna Hijau, Radius 16px).
- **Spasial Density Theming:** Mode *Compact* (Padding 8px, Font 14px) vs Mode *Comfortable* (Padding 16px, Font 16px) untuk aplikasi dashboard finansial.

#### 4. Syarah Kaidah 4: Token Spasial Numerik Menjaga Kedisiplinan 8pt Grid pada Level Kode
Seringkali desainer berniat baik menerapkan 8pt grid, tetapi tanpa sadar memasukkan angka 13px, 15px, atau 22px karena mengetik manual di input box inspector.

Dengan mendefinisikan *Number Variables* untuk skala spasial:
- `space/none` = 0px
- `space/xxs`  = 2px
- `space/xs`   = 4px (Half grid)
- `space/sm`   = 8px (Base grid)
- `space/md`   = 16px
- `space/lg`   = 24px
- `space/xl`   = 32px
- `space/2xl`  = 48px
- `space/3xl`  = 64px

Desainer tidak lagi mengetik angka acak; mereka cukup menekan ikon *Apply Variable* pada panel padding atau gap dan memilih `space/md`. Ketika developer memeriksa aset di Dev Mode, mereka tidak melihat angka "16px" statis, melainkan token `var(--spacing-md)`, yang langsung terpetakan ke utility class CSS seperti `p-4` di Tailwind CSS.

#### 5. Syarah Kaidah 5: Standarisasi Format Token W3C DTCG Memastikan Portabilitas Penuh Antara Figma, Style Dictionary, dan Repositori Kode
Agar sistem desain tidak terkunci (*vendor lock-in*) di dalam Figma, penamaan dan struktur token harus mematuhi rekomendasi standar resmi dari W3C Design Tokens Community Group (DTCG).

Struktur standar W3C mensyaratkan setiap token memiliki:
- `$value`: Nilai aktual (bisa berupa nilai mentah atau string kurung kurawal `{color.blue.500}` yang menandakan referensi alias).
- `$type`: Tipe data token (`color`, `dimension`, `fontFamily`, `fontWeight`, `duration`, `cubicBezier`).
- `$description`: Dokumentasi fungsi pemakaian token untuk developer.

Dengan mematuhi format ini, file JSON token yang diekspor dari Figma dapat langsung diproses oleh tool otomatisasi seperti *Style Dictionary* milik Amazon untuk dikompilasi menjadi token CSS, SCSS, Swift (iOS), dan XML/Kotlin Compose (Android) secara otomatis dalam pipeline CI/CD GitHub.

---

### LAYER 4: FIELD PLAYBOOK (TACTICAL SOP & CODE)

#### Skema Standar W3C DTCG Design Tokens (JSON Schema)

```json
{
  "primitive": {
    "color": {
      "blue": {
        "500": { "value": "#3b82f6", "type": "color" },
        "600": { "value": "#2563eb", "type": "color" }
      },
      "neutral": {
        "50":  { "value": "#f8fafc", "type": "color" },
        "900": { "value": "#0f172a", "type": "color" }
      }
    },
    "spacing": {
      "sm": { "value": "8px",  "type": "dimension" },
      "md": { "value": "16px", "type": "dimension" },
      "lg": { "value": "24px", "type": "dimension" }
    }
  },
  "semantic": {
    "color": {
      "surface": {
        "page": {
          "$value": "{primitive.color.neutral.50}",
          "$type": "color",
          "$description": "Warna latar belakang utama seluruh viewport halaman"
        }
      },
      "action": {
        "primary": {
          "$value": "{primitive.color.blue.600}",
          "$type": "color",
          "$description": "Warna aksen tombol aksi utama dan fokus navigasi"
        }
      }
    }
  }
}
```

#### SOP Pembuatan Token di Figma:
1. Buka panel Variables (`Local Variables`).
2. Buat Koleksi 1: `Primitives` (isi palet warna mentah dan skala angka). Centang opsi `Hide from publishing` agar tidak mengotori asset picker.
3. Buat Koleksi 2: `Tokens` (buat mode `Light` dan `Dark`).
4. Untuk setiap variabel di `Tokens`, klik kanan pada kolom nilai dan pilih **Create Alias**, lalu arahkan ke variabel di koleksi `Primitives`.
5. Uji pada kanvas: buat frame sederhana, pasang token, lalu klik kanan frame > `Change Variable Mode` untuk memastikan mode switching berjalan 100% mulus.

---

### LAYER 5: DIAGNOSTIC DRILL (STUDI KASUS & UJI MANDIRI)

#### Skenario Kasus Nyata
Sebuah perusahaan software kesehatan mengakuisisi startup telemedicine lain. Manajemen meminta agar satu aplikasi web yang sama dapat berjalan untuk dua merek berbeda:
- **Brand SehatKu:** Warna dominan Biru Medis (`#0066CC`), tombol bersudut melengkung halus (`radius: 8px`), tipografi Sans-Serif (`Inter`).
- **Brand PharmaPlus:** Warna dominan Hijau Apotek (`#00A86B`), tombol bersudut membulat penuh (*Pill Shape*, `radius: 9999px`), tipografi Humanist (`Rubik`).

Desainer lama mencoba menyelesaikan masalah ini dengan menduplikasi seluruh 150 artboard kanvas menjadi dua file terpisah (`App_SehatKu.fig` dan `App_PharmaPlus.fig`). Dua minggu kemudian, terjadi bug fix pada alur pembayaran di file SehatKu, namun desainer lupa memperbarui file PharmaPlus. Developer kebingungan karena spesifikasi layout kedua brand menjadi bercabang dan tidak sinkron.

#### Lembar Uji Mandiri (3 Pertanyaan Kritis)
1. Apa risiko arsitektural dan biaya operasional jangka panjang dari menduplikasi file desain untuk keperluan multi-brand?
2. Bagaimana arsitektur *Figma Variables (Multi-Brand Modes)* dapat mengonsolidasikan kedua brand tersebut kembali ke dalam satu file tunggal yang sinkron?
3. Variabel bertipe apa saja yang wajib dibuat untuk mendukung perbedaan warna, radius sudut, dan font antar kedua brand tersebut?

#### Kunci Jawaban Lengkap & Analisis Anti-Pattern

1. **Risiko Arsitektural Duplikasi File (Codebase Forking):** Menduplikasi file desain menghasilkan kondisi *Design Debt Divergence* (analog dengan git branching tanpa pernah di-merge). Setiap perbaikan UX, perbaikan copy, atau validasi alur di salah satu file harus diulang secara manual di file kedua. Secara statistik, kemungkinan terjadinya inkonsistensi antar-brand mencapai 100% dalam waktu kurang dari 3 bulan, melipatgandakan biaya maintenance dan memperlambat *time-to-market*.
2. **Konsolidasi Single File via Variable Modes:**
   - Hapus file duplikat. Satukan seluruh desain ke dalam satu file tunggal.
   - Buat satu koleksi variabel bernama `Brand Theme`.
   - Buat dua kolom mode: Kolom 1 = `SehatKu`, Kolom 2 = `PharmaPlus`.
   - Seluruh komponen (Button, Card, Input) hanya merujuk pada satu semantic token yang sama (misal: `color/action/primary` dan `radius/button`).
   - Di kolom mode `SehatKu`, isi `color/action/primary` = `#0066CC` dan `radius/button` = `8px`.
   - Di kolom mode `PharmaPlus`, isi `color/action/primary` = `#00A86B` dan `radius/button` = `9999px`.
   - **Hasil:** File desain tetap satu (*Single Source of Truth*). Alur logika pembayaran hanya perlu diedit sekali dan otomatis berlaku untuk kedua brand.
3. **Konfigurasi Tipe Variabel yang Dibutuhkan:**
   - **Color Variable:** `brand/primary` (Biru `#0066CC` vs Hijau `#00A86B`).
   - **Number Variable:** `radius/interactive` (Nilai `8` vs Nilai `9999`).
   - **String Variable (untuk Typography Font Family):** Tautkan font family ke string variable `font/family/primary` (Nilai `"Inter"` vs Nilai `"Rubik"`).
   - Seluruh perbedaan visual terselesaikan secara matematis melalui matrix mode tanpa menduplikasi satu pun frame kanvas!
