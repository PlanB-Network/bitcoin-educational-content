---
term: P2SH

---
P2SH adalah singkatan dari *Pay to Script Hash*, yang merupakan model skrip standar yang digunakan untuk menetapkan kondisi pengeluaran pada UTXO. Tidak seperti skrip P2PK dan P2PKH, di mana kondisi pengeluaran sudah ditentukan sebelumnya, P2SH memungkinkan integrasi kondisi pengeluaran yang bisa dikustomisasi dan fungsi tambahan dalam skrip transaksi.

Secara teknis, dalam transaksi P2SH, `scriptPubKey` berisi _hash_ kriptografi dari `redeemScript`, dan bukan kondisi pengeluaran eksplisit. _Hash_ ini diperoleh dengan menggunakan fungsi _hashing_ `SHA256`. Ketika mengirimkan bitcoin ke alamat P2SH, `redeemScript` yang mendasarinya tidak diungkapkan. Hanya _hash_-nya saja yang disertakan dalam transaksi. Alamat P2SH dikodekan dalam `Base58Check` dan dimulai dengan angka `3`. Ketika penerima ingin membelanjakan bitcoin yang diterima, mereka harus memberikan `redeemScript` yang sesuai dengan _hash_ yang ada di `scriptPubKey`, bersama dengan data yang diperlukan untuk memenuhi persyaratan `redeemScript` ini. Sebagai contoh, dalam skrip _multisignature_ P2SH, skrip tersebut mungkin membutuhkan tanda tangan dari beberapa kunci privat.

Penggunaan P2SH menawarkan fleksibilitas yang lebih besar, karena memungkinkan untuk membuat skrip yang berbeda-beda, dan pengirim mengetahui detailnya. P2SH diperkenalkan pada tahun 2012 dengan BIP16.
