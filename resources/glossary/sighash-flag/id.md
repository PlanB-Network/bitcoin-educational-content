---
term: BENDERA SIGHASH

---
Sebuah parameter dalam transaksi Bitcoin yang menentukan komponen transaksi (input dan output) yang dicakup oleh tanda tangan yang terkait, sehingga tidak dapat diubah. SigHash Flag adalah sebuah byte yang ditambahkan ke tanda tangan digital dari setiap input. Oleh karena itu, pilihan SigHash Flag secara langsung mempengaruhi bagian mana dari transaksi yang dibekukan oleh tanda tangan dan mana yang masih dapat dimodifikasi setelahnya. Mekanisme ini memastikan bahwa tanda tangan secara tepat dan aman melakukan komit data transaksi sesuai dengan maksud penanda tangan. Terdapat tiga SigHash Flag utama:


- `SIGHASH_ALL` (`x01`): Tanda tangan ini berlaku untuk semua input dan output transaksi, sehingga mengunci semuanya;
- `SIGHASH_NONE` (`x02`): Tanda tangan ini berlaku untuk semua input tetapi tidak untuk output, sehingga output dapat dimodifikasi setelah tanda tangan;
- `SIGHASH_SINGLE` (`x03`): Tanda tangan mencakup semua input dan hanya satu output yang sesuai dengan indeks input yang ditandatangani.

Sebagai tambahan dari ketiga SigHash Flags ini, pengubah `SIGHASH_ANYONECANPAY` (`x80`) dapat digabungkan dengan masing-masing tipe sebelumnya. Ketika pengubah ini digunakan, hanya sebagian dari input yang ditandatangani, membiarkan yang lainnya terbuka untuk modifikasi. Berikut adalah kombinasi yang ada dengan pengubah tersebut:


- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`x81`): Tanda tangan ini berlaku untuk satu masukan sekaligus mencakup semua keluaran transaksi;
- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`x82`): Tanda tangan ini mencakup satu masukan, tanpa melakukan keluaran apa pun;
- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`x83`): Tanda tangan ini berlaku untuk satu masukan dan hanya untuk keluaran yang memiliki indeks yang sama dengan masukan ini.

> ► * Sinonim yang terkadang digunakan untuk "SigHash" adalah "Jenis Hash Tanda Tangan".*