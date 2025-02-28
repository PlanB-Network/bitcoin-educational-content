---
term: BENIH (BITCOIN)

---
Dalam konteks Bitcoin, seed adalah sebuah nilai 512-bit yang digunakan untuk mendapatkan semua kunci privat dan publik yang terkait dengan sebuah dompet HD (Hierarchical Deterministic). Secara teknis, seed merupakan nilai yang berbeda dengan frasa pemulihan (atau mnemonic). Frasa ini, yang biasanya terdiri dari 12 atau 24 kata, dibuat dengan cara acak semu dari sebuah sumber entropi dan dilengkapi dengan checksum. Frasa ini memfasilitasi pencadangan oleh manusia dengan menyediakan representasi tekstual dari nilai di dasar dompet.

Untuk mendapatkan seed yang sebenarnya, frasa pemulihan, yang mungkin disertai dengan frasa sandi opsional, diproses melalui algoritma PBKDF2 (*Fungsi Derivasi Kunci Berbasis Kata Sandi 2*). Hasil dari perhitungan ini adalah seed 512-bit. Seed inilah yang digunakan untuk menghasilkan kunci utama secara deterministik, dan kemudian seluruh rangkaian kunci untuk dompet HD, sesuai dengan BIP32.

![](../../dictionnaire/assets/31.webp)

> ► *Namun, dalam bahasa umum, mayoritas pengguna bitcoin mengacu pada frasa mnemonik ketika mereka berbicara tentang "seed", dan bukan pada kondisi perantara dari derivasi yang berada di antara frasa mnemonik dan kunci utama*