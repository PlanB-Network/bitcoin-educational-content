---
term: P2PKH
---

P2PKH merupakan singkatan dari *Pay to Public Key Hash*. Ini adalah model skrip standar yang digunakan untuk menetapkan kondisi pengeluaran pada sebuah UTXO. Ini memungkinkan penguncian bitcoin pada hash dari kunci publik, yaitu, pada alamat penerima. Skrip ini terkait dengan standar Legacy dan diperkenalkan dalam versi awal Bitcoin oleh Satoshi Nakamoto.

Berbeda dengan P2PK, di mana kunci publik secara eksplisit disertakan dalam skrip, P2PKH menggunakan sidik jari kriptografis dari kunci publik. Skrip ini mencakup hash `RIPEMD160` dari `SHA256` kunci publik dan menetapkan bahwa, untuk mengakses dana, penerima harus menyediakan kunci publik yang cocok dengan hash ini, serta tanda tangan digital yang valid yang dihasilkan dari kunci privat yang terkait. Alamat P2PKH dikodekan menggunakan format `Base58Check`, yang memberikan ketahanan terhadap kesalahan ketik melalui penggunaan checksum. Alamat-alamat ini selalu dimulai dengan angka `1`.