# Track 4: Motion Physics & High-Fidelity Microinteractions

> "Gerakan dalam antarmuka bukan hiasan pemanis kosmetik; gerakan adalah fisika spasial yang memandu perhatian mata, memberi umpan balik taktual, dan mengonfirmasi kontinuitas status sistem."

Track 4 membawa Anda masuk ke ranah fisika gerak (*motion design*) dan rekayasa mikro-interaksi presisi tinggi. Alih-alih transisi kasar yang memotong alur pengguna, Anda akan membedah mekanika internal *Smart Animate*, kurva Bézier kustom, dinamika pegas (*spring physics*), dan arsitektur *Interactive Components* yang hidup mandiri di dalam hierarki komponen tanpa perlu mengotori kanvas utama.

---

### Peta Navigasi Kurikulum Track 4

```text
[MOTION PHYSICS & COGNITIVE CONTINUITY]
                   │
                   ▼
┌───────────────────────────────────────────────┐
│ Modul 07: Smart Animate & Easing Curves       │
│ • Layer Name & Hierarchy Matching Invariant   │
│ • Continuous Geometry & Shape Morphing        │
│ • Cubic Bézier (Ease-Out vs Ease-In-Out)      │
│ • Spring Dynamics: Stiffness, Damping & Mass  │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│ Modul 08: Interactive Components & Flows      │
│ • Self-Contained Component-Level State Machine│
│ • Nested Interactive States (Toggle, Dropdown)│
│ • Progressive Disclosure (Accordion, Modal)   │
│ • Perception Latency & Cognitive Feedback     │
└───────────────────────────────────────────────┘
```

---

### Tujuan Pembelajaran Kompetensi

1. **Pemahaman Mendalam Engine Smart Animate:** Menguasai aturan pencocokan layer (*layer matching*) dan hierarki pohon dokumen agar elemen bertransformasi secara mulus (*seamless morph*) tanpa efek disolusi (*cross-fade*) yang patah.
2. **Karakteristik Fisika Kurva & Pegas (*Spring Physics*):** Menerapkan parameter kekakuan (*stiffness*), redaman (*damping*), dan massa (*mass*) untuk menghasilkan gerakan antarmuka yang terasa natural, tanggap, dan bebas dari kelembaman berlebih (*no bouncy slop*).
3. **Arsitektur Komponen Interaktif Otonom:** Membangun *Interactive Components* (seperti switch toggle, input field focus, checkbox, dan dropdown) yang menyimpan animasi statusnya sendiri, membebaskan artboard presentasi dari ratusan duplikasi layar transisi.
