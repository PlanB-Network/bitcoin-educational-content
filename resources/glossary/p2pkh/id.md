---
term: P2PKH

---
P2PKH adalah singkatan dari *Pay to Public Key Hash*, yang merupakan model skrip standar yang digunakan untuk menetapkan kondisi pengeluaran pada UTXO. Skrip ini memungkinkan penguncian bitcoin pada _hash_ kunci publik, yaitu pada alamat penerima. Skrip ini terkait dengan standar Legacy dan diperkenalkan pada versi awal Bitcoin oleh Satoshi Nakamoto.

Tidak seperti P2PK, dimana kunci publik secara eksplisit disertakan dalam skrip, P2PKH menggunakan sidik jari kriptografi dari kunci publik. Skrip ini menyertakan _hash_ `RIPEMD160` dari `SHA256` dari kunci publik dan menetapkan bahwa, untuk mengakses dana, penerima harus memberikan kunci publik yang cocok dengan _hash_ ini, serta tanda tangan digital yang valid yang dihasilkan dari kunci privat yang terkait. Alamat P2PKH dikodekan menggunakan format `Base58Check`, yang memberikan ketahanan terhadap kesalahan penulisan melalui penggunaan _checksum_. Alamat-alamat ini selalu dimulai dengan angka `1`.
