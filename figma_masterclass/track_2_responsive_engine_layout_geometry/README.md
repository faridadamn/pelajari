# Track 2: Responsive Engine & Mathematical Layout Geometry

> "Auto Layout bukan sekadar cara cepat merapikan tombol; Auto Layout adalah implementasi visual murni dari CSS Flexible Box Module (Flexbox) dan Box Model di dalam engine kanvas 2D."

Track 2 membekali Anda dengan penguasaan arsitektur tata letak dinamis dan sistem komponen modular berskala perusahaan. Anda akan membedah bagaimana geometri antarmuka beradaptasi terhadap konten dinamis, cara menyusun hierarki komponen berakar pada metodologi *Atomic Design*, dan teknik mengelola ratusan permutasi visual menggunakan matriks *Variant & Component Properties* tanpa meledakkan kompleksitas file.

---

### Peta Navigasi Kurikulum Track 2

```text
[CSS BOX MODEL & FLEXBOX MECHANICS]
                  │
                  ▼
┌───────────────────────────────────────────────┐
│ Modul 03: Auto Layout 5.0 & Box Model         │
│ • Direction (Row/Col/Wrap), Gap & Padding     │
│ • Resizing Logic: Fixed vs Hug vs Fill        │
│ • Min/Max Width & Height Constraints          │
│ • Absolute Positioning in Auto Layout Flows   │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│ Modul 04: Component Architecture & Variants   │
│ • Master Component vs Instance Inheritance    │
│ • Atomic Design: Atoms, Molecules, Organisms  │
│ • Component Properties (Boolean, Swap, Text)  │
│ • Mitigasi Ledakan State (Variant Explosion)  │
└───────────────────────────────────────────────┘
```

---

### Tujuan Pembelajaran Kompetensi

1. **Pemetaan Sempurna ke CSS Flexbox:** Menghilangkan friksi komunikasi antara desainer dan front-end engineer dengan menggunakan aturan `flex-direction`, `flex-wrap`, `justify-content`, dan `align-items` secara native di Figma.
2. **Rekayasa Geometri Responsif Deterministik:** Memanfaatkan kombinasi *Hug Contents*, *Fill Container*, serta *Min/Max Dimensions* sehingga layout tidak pernah pecah saat diisi string multibahasa yang panjang atau saat viewport menyusut.
3. **Arsitektur Komponen Skala Industri:** Mengurangi jumlah varian dalam *Component Set* hingga 70% dengan memanfaatkan *Component Properties* ortogonal (boolean visibility, text content, dan instance swap) alih-alih menduplikasi seluruh frame untuk setiap perubahan status mikro.
