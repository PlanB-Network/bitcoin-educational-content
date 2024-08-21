---
term: SEED (BITCOIN)
---

Dalam konteks Bitcoin, seed adalah nilai 512-bit yang digunakan untuk menurunkan semua kunci privat dan publik yang terkait dengan dompet HD (Hierarchical Deterministic). Secara teknis, seed merupakan nilai yang berbeda dari frasa pemulihan (atau mnemonic). Frasa tersebut, yang biasanya terdiri dari 12 atau 24 kata, dihasilkan secara pseudo-random dari sumber entropi dan dilengkapi oleh checksum. Frasa ini memudahkan pencadangan manusia dengan menyediakan representasi teks dari nilai dasar dompet.

Untuk mendapatkan seed sebenarnya, frasa pemulihan, yang mungkin disertai dengan passphrase opsional, diproses melalui algoritma PBKDF2 (*Password-Based Key Derivation Function 2*). Hasil dari perhitungan ini adalah seed 512-bit. Seed inilah yang digunakan untuk secara deterministik menghasilkan kunci induk, dan kemudian seluruh set kunci untuk dompet HD, sesuai dengan BIP32.

![](../../dictionnaire/assets/31.png)

> ► *Namun, dalam bahasa sehari-hari, mayoritas pengguna Bitcoin merujuk pada frasa mnemonic ketika mereka berbicara tentang "seed," dan bukan pada keadaan perantara derivasi yang berada di antara frasa mnemonic dan kunci induk.*