---
term: FUNGSI HASH

---
Sebuah fungsi matematika yang mengambil masukan berukuran variabel (disebut pesan) dan menghasilkan keluaran berukuran tetap (disebut _hash_, _hashing_, _digest_, atau sidik jari). Fungsi _hash_ adalah fungsi primitif yang digunakan secara luas dalam kriptografi. Fungsi-fungsi ini menunjukkan sifat-sifat khusus yang membuatnya cocok untuk digunakan dalam konteks yang aman:


- Resistensi terhadap _preimage_: sangat sulit untuk menemukan pesan yang menghasilkan _hash_ tertentu, yaitu, untuk menemukan sebuah _preimage_ $m$ untuk sebuah hash $h$ sedemikian rupa sehingga $h = H(m)$, di mana $H$ adalah fungsi _hash_;
- Resistensi _preimage_ kedua: diberikan sebuah pesan $m_1$, pasti sangat sulit untuk menemukan pesan lain $m_2$ (berbeda dengan $m_1$) sedemikian rupa sehingga $H(m_1) = H(m_2);
- Resistensi tabrakan: sangat sulit untuk menemukan dua pesan yang berbeda $m_1$ dan $m_2$ sedemikian rupa sehingga $H(m_1) = H(m_2);
- Resistensi terhadap manipulasi: perubahan kecil pada input harus menyebabkan perubahan yang signifikan dan tidak dapat diprediksi pada output.

Dalam konteks Bitcoin, fungsi _hash_ digunakan untuk beberapa tujuan, termasuk mekanisme pembuktian kerja (*Proof-of-Work*), pengidentifikasi transaksi, pembuatan alamat, penghitungan _checksum_, dan pembuatan struktur data seperti pohon Merkle. Di sisi protokol, Bitcoin secara eksklusif menggunakan fungsi `SHA256d`, yang juga dinamai `HASH256`, yang terdiri dari _hash_ ganda `SHA256`. `HASH256` juga digunakan dalam perhitungan _checksum_ tertentu, terutama untuk _extended key_ (`xpub`, `xprv`...). Di sisi dompet, berikut ini juga digunakan:


- `SHA256` untuk _checksum_ frasa mnemonik;
- `SHA512` dalam algoritma `HMAC` dan `PBKDF2` yang digunakan dalam proses mendapatkan dompet deterministik dan hirarkis;
- `HASH160`, yang menjelaskan penggunaan `SHA256` dan `RIPEMD160` secara berurutan. `HASH160` digunakan dalam proses pembuatan alamat penerima (kecuali P2PK dan P2TR) dan dalam menghitung sidik jari kunci induk untuk kunci yang diperluas.

> ► *Dalam bahasa Inggris, ini disebut sebagai "hash function".*
