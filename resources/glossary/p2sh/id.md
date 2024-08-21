---
term: P2SH
---

P2SH merupakan singkatan dari *Pay to Script Hash*. Ini adalah model skrip standar yang digunakan untuk menetapkan kondisi pengeluaran pada sebuah UTXO. Berbeda dengan skrip P2PK dan P2PKH, di mana kondisi pengeluaran sudah ditentukan sebelumnya, P2SH memungkinkan integrasi kondisi pengeluaran yang sembarang dan fungsionalitas tambahan dalam skrip transaksi.

Secara teknis, dalam transaksi P2SH, `scriptPubKey` berisi hash kriptografis dari sebuah `redeemScript`, bukan kondisi pengeluaran yang eksplisit. Hash ini diperoleh menggunakan hash `SHA256`. Ketika mengirim bitcoin ke alamat P2SH, `redeemScript` yang mendasarinya tidak diungkapkan. Hanya hashnya yang termasuk dalam transaksi. Alamat P2SH dikodekan dalam `Base58Check` dan dimulai dengan angka `3`. Ketika penerima ingin menghabiskan bitcoin yang diterima, mereka harus menyediakan `redeemScript` yang cocok dengan hash yang ada dalam `scriptPubKey`, bersama dengan data yang diperlukan untuk memenuhi kondisi dari `redeemScript` ini. Sebagai contoh, dalam skrip multisignature P2SH, skrip tersebut bisa memerlukan tanda tangan dari beberapa kunci privat.

Penggunaan P2SH menawarkan lebih banyak fleksibilitas, karena memungkinkan pembuatan skrip yang sembarang tanpa pengirim mengetahui detailnya. P2SH diperkenalkan pada tahun 2012 dengan BIP16.