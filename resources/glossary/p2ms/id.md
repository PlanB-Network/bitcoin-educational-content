---
term: P2MS
---

P2MS merupakan singkatan dari *Pay to Multisig*, yang diterjemahkan menjadi "bayar ke beberapa tanda tangan". Ini adalah model skrip standar yang digunakan untuk menetapkan kondisi pengeluaran pada sebuah UTXO. Ini memungkinkan penguncian bitcoin dengan beberapa kunci publik. Untuk menghabiskan bitcoin ini, diperlukan tanda tangan dengan jumlah kunci privat yang telah ditentukan sebelumnya. Sebagai contoh, sebuah `P2MS 2/3` melibatkan `3` kunci publik dengan `3` kunci privat rahasia yang terkait. Untuk menghabiskan bitcoin yang dikunci dengan skrip P2MS ini, diperlukan tanda tangan dengan setidaknya `2` dari `3` kunci privat tersebut. Ini adalah sistem keamanan ambang batas.

Skrip ini ditemukan pada tahun 2011 oleh Gavin Andresen ketika ia mengambil alih pemeliharaan klien Bitcoin utama. Saat ini, P2MS hanya digunakan secara marginal oleh beberapa aplikasi. Mayoritas besar multisignature modern menggunakan skrip lain seperti P2SH atau P2WSH. Dibandingkan dengan ini, P2MS sangat sederhana. Kunci publik yang terdiri dari skrip ini diungkapkan saat menerima transaksi. Menggunakan P2MS juga lebih mahal daripada skrip multisignature lainnya.

> ► *P2MS sering disebut "bare-multisig", yang dapat diterjemahkan sebagai "multisignature telanjang" atau "multisignature mentah". Di awal tahun 2023, skrip P2MS berada di tengah kontroversi karena penyalahgunaannya dalam protokol Stamps. Dampak mereka terhadap set UTXO secara khusus ditunjukkan.*