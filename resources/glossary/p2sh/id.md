---
term: P2SH

---
P2SH adalah singkatan dari *Bayar ke Skrip Hash*. Ini adalah model skrip standar yang digunakan untuk menetapkan kondisi pengeluaran pada UTXO. Tidak seperti skrip P2PK dan P2PKH, di mana kondisi pengeluaran sudah ditentukan sebelumnya, P2SH memungkinkan integrasi kondisi pengeluaran sewenang-wenang dan fungsi tambahan dalam skrip transaksi.

Secara teknis, dalam transaksi P2SH, `scriptPubKey` berisi hash kriptografi dari `redeemScript`, dan bukan kondisi pengeluaran eksplisit. Hash ini diperoleh dengan menggunakan hash `SHA256`. Ketika mengirimkan bitcoin ke alamat P2SH, `redeemScript` yang mendasarinya tidak diungkapkan. Hanya hash-nya saja yang disertakan dalam transaksi. Alamat P2SH dikodekan dalam `Base58Check` dan dimulai dengan angka `3`. Ketika penerima ingin membelanjakan bitcoin yang diterima, mereka harus memberikan `redeemScript` yang sesuai dengan hash yang ada di `scriptPubKey`, bersama dengan data yang diperlukan untuk memenuhi persyaratan `redeemScript` ini. Sebagai contoh, dalam skrip multisignature P2SH, skrip tersebut dapat membutuhkan tanda tangan dari beberapa private key.

Penggunaan P2SH menawarkan fleksibilitas yang lebih besar, karena memungkinkan untuk membuat skrip yang berubah-ubah tanpa pengirim mengetahui detailnya. P2SH diperkenalkan pada tahun 2012 dengan BIP16.