---
term: FUNGSI HASH
---

Sebuah fungsi matematika yang mengambil input berukuran variabel (disebut pesan) dan menghasilkan output berukuran tetap (disebut hash, hashing, digest, atau sidik jari). Fungsi hash digunakan secara luas sebagai primitif dalam kriptografi. Mereka menunjukkan properti spesifik yang membuatnya cocok untuk digunakan dalam konteks keamanan:
* Ketahanan terhadap pencarian citra balik: harus sangat sulit untuk menemukan pesan yang menghasilkan hash tertentu, yaitu, untuk menemukan citra balik $m$ untuk sebuah hash $h$ sedemikian sehingga $h = H(m)$, di mana $H$ adalah fungsi hash;
* Ketahanan terhadap pencarian citra balik kedua: diberikan sebuah pesan $m_1$, harus sangat sulit untuk menemukan pesan lain $m_2$ (berbeda dari $m_1$) sedemikian sehingga $H(m_1) = H(m_2)$;
* Ketahanan terhadap tabrakan: harus sangat sulit untuk menemukan dua pesan berbeda $m_1$ dan $m_2$ sedemikian sehingga $H(m_1) = H(m_2)$;
* Ketahanan terhadap perubahan: perubahan kecil pada input harus menyebabkan perubahan signifikan dan tidak terduga pada output.

Dalam konteks Bitcoin, fungsi hash digunakan untuk beberapa tujuan, termasuk mekanisme bukti-kerja (*Proof-of-Work*), pengidentifikasi transaksi, generasi alamat, perhitungan checksum, dan pembuatan struktur data seperti pohon Merkle. Di sisi protokol, Bitcoin secara eksklusif menggunakan fungsi `SHA256d`, juga disebut `HASH256`, yang terdiri dari hash `SHA256` ganda. `HASH256` juga digunakan dalam perhitungan checksum tertentu, terutama untuk kunci ekstensi (`xpub`, `xprv`...). Di sisi dompet, yang berikut ini juga digunakan:
* `SHA256` sederhana untuk checksum dari frasa mnemonik;
* `SHA512` dalam algoritma `HMAC` dan `PBKDF2` yang digunakan dalam proses derivasi dompet deterministik dan hierarkis;
* `HASH160`, yang mendeskripsikan penggunaan berturut-turut dari `SHA256` dan `RIPEMD160`. `HASH160` digunakan dalam proses generasi alamat penerima (kecuali P2PK dan P2TR) dan dalam perhitungan sidik jari kunci induk untuk kunci ekstensi.

> ► *Dalam bahasa Inggris, ini disebut sebagai "hash function".*