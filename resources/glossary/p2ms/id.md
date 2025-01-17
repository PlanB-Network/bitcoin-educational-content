---
term: P2MS

---
P2MS adalah singkatan dari *Bayar ke Multisig*, yang diterjemahkan menjadi "bayar ke beberapa tanda tangan". Ini adalah model skrip standar yang digunakan untuk menetapkan kondisi pengeluaran pada UTXO. Hal ini memungkinkan penguncian bitcoin dengan beberapa kunci publik. Untuk membelanjakan bitcoin ini, dibutuhkan tanda tangan dengan sejumlah kunci privat yang telah ditentukan sebelumnya. Sebagai contoh, `P2MS 2/3` melibatkan `3` kunci publik dengan `3` kunci privat rahasia yang terkait. Untuk membelanjakan bitcoin yang terkunci dengan skrip P2MS ini, dibutuhkan tanda tangan dengan setidaknya `2` dari `3` private key. Ini adalah sistem keamanan ambang batas.

Skrip ini ditemukan pada tahun 2011 oleh Gavin Andresen ketika ia mengambil alih pemeliharaan klien Bitcoin utama. Saat ini, P2MS hanya digunakan secara marginal oleh beberapa aplikasi. Sebagian besar multisignature modern menggunakan skrip lain seperti P2SH atau P2WSH. Dibandingkan dengan ini, P2MS sangatlah sepele. Kunci publik yang ada di dalamnya akan diungkap pada saat menerima transaksi. Menggunakan P2MS juga lebih mahal dibandingkan dengan skrip multisignature lainnya.

> p2MS sering disebut "bare-multisig", yang dapat diterjemahkan sebagai "multisignature telanjang" atau "multisignature mentah". Pada awal tahun 2023, skrip P2MS menjadi pusat kontroversi karena disalahgunakan dalam protokol Stamps. Dampaknya terhadap set UTXO sangat disoroti.*