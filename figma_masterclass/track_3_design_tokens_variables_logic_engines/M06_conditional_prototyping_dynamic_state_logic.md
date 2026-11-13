# Modul 06: Conditional Prototyping, Logic Engines & Dynamic State

> "Prototipe interaktif modern tidak lagi membutuhkan 50 artboard dengan kabel laba-laba yang rumit; variabel dan percabangan logika mengeksekusi komputasi state langsung di dalam satu frame."

## Modul 06: Conditional Prototyping, Logic Engines & Dynamic State

---

### LAYER 1: KAIDAH EMAS (CORE AXIOMS)

1. **Model State Dinamis Menggantikan Spaghetti Wires: Satu Frame Berkemampuan Variabel Mengeliminasi Ratusan Artboard Redundan:** Di era klasik, untuk membuat alur keranjang belanja dengan 3 item dan toggle kupon, desainer harus menduplikasi belasan layar untuk setiap kemungkinan kombinasi (2^N permutasi). Dengan variabel Figma, satu layar tunggal dapat merender seluruh state dinamis melalui manipulasi variabel numerik dan boolean.
2. **Ekspresi Matematika dan Manipulasi String Menjalankan Komputasi Real-Time di Sisi Klien Prototipe:** Prototipe mendukung operator aritmatika dasar (`+`, `-`, `*`, `/`) dan penggabungan teks (*string concatenation*). Nilai variabel dapat dihitung secara dinamis saat runtime prototipe berjalan (misal: `subtotal = itemQuantity * unitPrice`).
3. **Percabangan Logika (Conditional If / Else) Mengarahkan Alur Pengguna Berdasarkan Evaluasi Ekspresi:** Aksi interaksi dapat mengevaluasi kondisi logika Boolean (`==`, `!=`, `>`, `<`, `>=`, `<=`). Jika kondisi terpenuhi (*true*), blok instruksi `if` dieksekusi; jika tidak (*false*), alur dialihkan ke blok `else`.
4. **Multi-Action Stacking Mengizinkan Rantai Eksekusi Beberapa Tindakan dalam Satu Event Pemicu:** Satu pemicu klik (*On click*) tidak lagi terbatas pada satu navigasi saja. Desainer dapat menyusun urutan aksi simultan: (1) Set Variable `itemCount = itemCount + 1`, (2) Set Variable `subtotal = subtotal + 150000`, (3) Set Boolean `isToastVisible = true`, (4) Scroll to Section.
5. **Validasi Formulir Interaktif Meniru Perilaku Input Nyata untuk Pengujian Usabilitas Berkecepatan Tinggi:** Dengan menautkan input teks ke String Variables dan mengevaluasi status pengisian form sebelum mengaktifkan tombol submit, tim riset UX dapat menguji skenario kegagalan dan pesan error tanpa perlu bantuan coding front-end satu baris pun.

---

### LAYER 2: MENTAL MODEL & DIAGRAM ASCII

```text
[KLASIK: SPAGHETTI WIRES]                [MODERN: STATE MACHINE VARIABLE]
Screen 0 Items ──► Screen 1 Item         ┌───────────────────────────────┐
      │                  │               │ Single Screen Prototype       │
      ▼                  ▼               │ • Variable: cartCount = 0     │
Screen 1 Item + Coupon   Screen 2 Items  │ • Variable: subtotal  = 0     │
      │                  │               │                               │
(Kabel laba-laba, 16 layar duplikat,     │ [Button: + Tambah Keranjang]  │
 memeliharanya adalah mimpi buruk)       └──────────────┬────────────────┘
                                                        │ Trigger: On Click
                                                        ▼
                                         ┌───────────────────────────────┐
                                         │ Action Stack:                 │
                                         │ 1. Set cartCount = cartCount+1│
                                         │ 2. Set subtotal = subtotal+50k│
                                         │ 3. If cartCount >= 5:         │
                                         │      Set freeShipping = true  │
                                         │    Else:                      │
                                         │      Set freeShipping = false │
                                         └───────────────────────────────┘
```

Formula Evaluasi Percabangan Kondisional:
`IF (Kondisi_Logika) THEN [Rangkaian_Aksi_A] ELSE [Rangkaian_Aksi_B]`

---

### LAYER 3: SYARAH DAGING (DEEP DIVE KNOWLEDGE)

#### 1. Syarah Kaidah 1: Model State Dinamis Menggantikan Spaghetti Wires: Satu Frame Berkemampuan Variabel Mengeliminasi Ratusan Artboard Redundan
Salah satu masalah paling melelahkan dalam pembuatan prototipe interaktif tingkat tinggi (*high-fidelity prototype*) adalah ledakan artboard (*artboard sprawl*).
Bayangkan fitur checkout sederhana:
- Keranjang bisa berisi 0, 1, 2, atau 3 item (4 state).
- User bisa mencentang opsi asuransi pengiriman (2 state).
- User bisa memasukkan kode promo valid atau tidak valid (2 state).
Total artboard yang harus digambar dan disambungkan dengan kabel interaksi: 4 × 2 × 2 = **16 artboard**! Jika ada perubahan kecil pada warna header, desainer harus memperbarui 16 artboard tersebut.

Dengan Figma Variables:
- Desainer HANYA MEMBUAT 1 ARTBOARD TUNGGAL.
- Teks angka pada badge keranjang ditautkan ke variabel numerik `cartCount`.
- Teks total harga ditautkan ke variabel numerik `totalPrice`.
- Banner asuransi dan diskon dikontrol oleh variabel boolean `showInsurance` dan `showDiscount`.
Saat pengguna mengklik tombol di mode prototipe, variabel-variabel tersebut diperbarui di memori runtime, dan tampilan 1 artboard tersebut langsung berubah dinamis secara in-place!

#### 2. Syarah Kaidah 2: Ekspresi Matematika dan Manipulasi String Menjalankan Komputasi Real-Time di Sisi Klien Prototipe
Prototipe Figma kini dilengkapi engine ekspresi aritmatika dasar. Pada panel interaksi prototipe, saat memilih aksi **Set variable**, Anda dapat memilih variabel target dan mengisinya dengan ekspresi:
- Penjumlahan: `cartTotal = cartTotal + itemPrice`
- Pengurangan: `cartCount = cartCount - 1`
- Perkalian: `subtotal = quantity * 250000`
- Pembagian: `installmentMonth = totalLoan / 12`

Selain matematika, manipulasi string (*string concatenation*) memungkinkan pembuatan sapaan dinamis. Jika variabel `userFirstName` bernilai `"Adam"`, Anda dapat mengatur ekspresi:
`greetingText = "Halo, " + userFirstName + "! Selamat datang kembali."`
Ketika prototipe dijalankan dan input form diisi nama pengguna, teks di halaman beranda seketika menampilkan nama tersebut secara otomatis!

#### 3. Syarah Kaidah 3: Percabangan Logika (Conditional If / Else) Mengarahkan Alur Pengguna Berdasarkan Evaluasi Ekspresi
Di masa lalu, prototipe hanya bersifat "jalur bahagia" (*happy path*): pengguna mengklik tombol apa pun dan langsung diarahkan ke layar sukses berikutnya. Ini menghasilkan bias pengujian yang besar saat riset usabilitas, karena pengguna tidak pernah mengalami konsekuensi dari kesalahan input.

Dengan aksi **Conditional** (`if / else`):
- Anda dapat memeriksa kondisi logika sebelum mengizinkan aksi navigasi.
- Contoh: Pada tombol kupon promo, ketika diklik:
  - `IF (promoCodeInput == "DISKON50")`:
    - Set `discountAmount = subtotal * 0.5`
    - Set `promoSuccessMessage = "Kupon berhasil diterapkan!"`
    - Set `isPromoValid = true`
  - `ELSE`:
    - Set `promoErrorMessage = "Kode kupon tidak valid atau kadaluarsa."`
    - Set `isPromoValid = false`
Dengan alur ini, partisipan riset usabilitas yang mengetikkan kode yang salah akan benar-benar melihat pesan error asli, memvalidasi apakah salinan teks dan letak pesan kesalahan mudah dipahami pengguna nyata.

#### 4. Syarah Kaidah 4: Multi-Action Stacking Mengizinkan Rantai Eksekusi Beberapa Tindakan dalam Satu Event Pemicu
Sebelum pembaruan logika Figma, satu klik hanya bisa memicu satu hal: entah itu *Navigate to*, *Open Overlay*, atau *Scroll to*. Desainer seringkali bingung bagaimana caranya mencatat penambahan barang belanjaan SEKALIGUS memunculkan toast banner dan memperbarui total harga.

Fitur *Multi-Action Stacking* memungkinkan desainer menumpuk daftar instruksi berurutan di bawah satu event pemicu (misal: *On click* atau *While hovering*):
1. Aksi 1: **Set variable** `cartItems = cartItems + 1`
2. Aksi 2: **Set variable** `subtotalPrice = subtotalPrice + currentProductPrice`
3. Aksi 3: **Set variable** `toastMessage = "Item berhasil ditambahkan ke tas belanja"`
4. Aksi 4: **Set variable** `showToastNotification = true`
5. Aksi 5: **Conditional**: `IF (cartItems >= 3) -> Set freeGiftAwarded = true`
Semua instruksi di atas dieksekusi dalam satu kali klik pengguna, menciptakan ilusi aplikasi fungsional 100% nyata.

#### 5. Syarah Kaidah 5: Validasi Formulir Interaktif Meniru Perilaku Input Nyata untuk Pengujian Usabilitas Berkecepatan Tinggi
Salah satu rintangan terbesar pengujian form pendaftaran atau transaksi keuangan adalah perilaku tombol submit:
- Tombol submit harus berada dalam status `Disabled` jika email belum diisi atau password kurang dari 8 karakter.
- Tombol baru berubah menjadi `Active` dan berwarna biru cerah jika seluruh syarat input terpenuhi.

Dengan menggabungkan *Key / Gamepad Triggers* atau *Focus Loss (On click outside)* dengan variabel Boolean:
- Setiap kali form field diisi, nilai teks diperiksa.
- Pasang kondisi: `IF (isEmailFilled == true AND isPasswordFilled == true) -> Set isFormValid = true`.
- Varian tombol submit ditautkan ke properti variabel: jika `isFormValid == true`, tombol otomatis beralih ke varian `Active`; jika `false`, tombol tetap `Disabled`.
Hal ini memungkinkan tim produk menguji *mental effort* pengguna saat mengisi formulir yang rumit jauh sebelum tim teknis menulis satu baris kode backend pun.

---

### LAYER 4: FIELD PLAYBOOK (TACTICAL SOP & BLUEPRINT)

#### Blueprint Alur Logika: Dynamic Quantity Stepper & Cart Engine

```text
[TRIGGER: Tombol Plus (+)]
Action Stack:
  1. Set variable: quantity = quantity + 1
  2. Set variable: subtotal = quantity * unitPrice
  3. Conditional:
       IF (quantity > 10)
         Set variable: quantity = 10
         Set variable: errorMessage = "Maksimal pembelian 10 unit per akun"
         Set variable: showWarningBanner = true

[TRIGGER: Tombol Minus (-)]
Action Stack:
  1. Conditional:
       IF (quantity > 1)
         Set variable: quantity = quantity - 1
         Set variable: subtotal = quantity * unitPrice
         Set variable: showWarningBanner = false
       ELSE
         Set variable: showDeleteConfirmDialog = true
```

#### SOP Pembuatan Prototipe Variabel di Figma:
1. Tekan tombol `Prototype` di panel kanan atas.
2. Pilih elemen interaktif (misal tombol `+`).
3. Tambahkan interaksi `On click`.
4. Pada menu dropdown aksi, pilih **Set variable** (pilih variabel target dan masukkan formula).
5. Untuk menambahkan aksi kedua, klik ikon `+` di bawah aksi pertama dan pilih **Conditional** atau aksi variabel lainnya.
6. Tekan tombol `Preview` (`Shift+Space`) untuk menguji langsung di dalam kanvas tanpa perlu membuka tab presentasi baru.

---

### LAYER 5: DIAGNOSTIC DRILL (STUDI KASUS & UJI MANDIRI)

#### Skenario Kasus Nyata
Sebuah agensi produk digital sedang merancang prototipe aplikasi mobile banking untuk pengajuan pinjaman kilat (*Fast Loan*). Desainer menyiapkan slider kalkulator pinjaman:
- Pengguna dapat menggeser nominal pinjaman antara Rp 1.000.000 hingga Rp 10.000.000.
- Durasi pinjaman: 3 bulan, 6 bulan, atau 12 bulan.
- Prototipe harus menampilkan estimasi cicilan bulanan secara instan saat slider digeser atau durasi dipilih.

Desainer junior tidak memahami variabel dan conditional. Ia mencoba membuat kalkulator ini dengan membuat **30 artboard terpisah** (10 nominal pinjaman × 3 durasi). Hasilnya:
1. Kabel prototipe saling silang tak beraturan (*wire knot*).
2. Ketika klien mencoba mengklik durasi "6 bulan" pada nominal "Rp 4.000.000", prototipe melompat ke artboard nominal "Rp 1.000.000 durasi 6 bulan" karena desainer salah menyambungkan kabel navigasi.
3. Klien kecewa dan menganggap prototipe "rusak dan tidak profesional".

#### Lembar Uji Mandiri (3 Pertanyaan Kritis)
1. Berapa efisiensi reduksi artboard jika desainer menggunakan variabel matematika dan conditional alih-alih membuat 30 artboard manual?
2. Bagaimana formula matematika ekspresi Figma untuk menghitung cicilan bulanan (`monthlyInstallment`) dengan bunga tetap 2% per bulan?
3. Tuliskan arsitektur variabel lengkap yang dibutuhkan untuk menjalankan kalkulator pinjaman tersebut di atas 1 artboard tunggal!

#### Kunci Jawaban Lengkap & Analisis Anti-Pattern

1. **Efisiensi Reduksi Artboard:**
   - Jumlah artboard awal: 30 artboard.
   - Jumlah artboard modern: **1 artboard tunggal**.
   - **Efisiensi: 96.7% reduksi beban kanvas**. Mengeliminasi 100% risiko salah sambung kabel prototipe karena tidak ada navigasi perpindahan layar sama sekali; seluruh perubahan murni evaluasi state numerik di dalam memori frame.
2. **Formula Matematika Ekspresi Figma untuk Cicilan 2%:**
   - Rumus total pengembalian: Pokok + (Pokok × Bunga × Tenor).
   - Formula ekspresi Figma:
     - Langkah 1 (Hitung Total Bunga): `totalInterest = loanAmount * 0.02 * tenorMonths`
     - Langkah 2 (Hitung Total Pembayaran): `totalRepayment = loanAmount + totalInterest`
     - Langkah 3 (Hitung Cicilan Bulanan): `monthlyInstallment = totalRepayment / tenorMonths`
3. **Arsitektur Variabel Lengkap (Single Frame Solution):**
   - `num_loanAmount` (Number, Default: 5000000)
   - `num_tenorMonths` (Number, Default: 6)
   - `num_monthlyInstallment` (Number, Default: 933333)
   - `str_tenorActive` (String, Default: "6 Bulan")
   - Pada tombol pilihan tenor "3 Bulan", pasang aksi:
     - `Set num_tenorMonths = 3`
     - `Set str_tenorActive = "3 Bulan"`
     - `Set num_monthlyInstallment = (num_loanAmount + (num_loanAmount * 0.06)) / 3`
   - Slider pinjaman mengikat nilai posisi ke variabel `num_loanAmount` dan langsung memicu kalkulasi ulang cicilan secara instan.
