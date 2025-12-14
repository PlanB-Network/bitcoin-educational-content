---
term: SIGHASH FLAG

---
Sebuah parameter dalam transaksi Bitcoin yang menentukan komponen transaksi (input dan output) yang dicakup oleh tanda tangan yang terkait, sehingga tidak dapat diubah. _SigHash Flag_ adalah sebuah byte yang ditambahkan ke tanda tangan digital dari setiap input. Oleh karena itu, pilihan _SigHash Flag_ secara langsung mempengaruhi bagian mana dari transaksi yang dibekukan oleh tanda tangan dan mana yang masih dapat dimodifikasi setelahnya. Mekanisme ini memastikan bahwa tanda tangan secara tepat dan aman melakukan komit data transaksi sesuai dengan maksud penanda tangan. Terdapat tiga SigHash Flag utama:


- `SIGHASH_ALL` (`x01`): Tanda tangan ini berlaku untuk semua input dan output transaksi, sehingga mengunci semuanya;
- `SIGHASH_NONE` (`x02`): Tanda tangan ini berlaku untuk semua input tetapi tidak untuk output, sehingga output dapat dimodifikasi setelah tanda tangan;
- `SIGHASH_SINGLE` (`x03`): Tanda tangan mencakup semua input dan hanya satu output yang sesuai dengan indeks input yang ditandatangani.

Sebagai tambahan dari ketiga _SigHash Flag_ ini, pengubah `SIGHASH_ANYONECANPAY` (`x80`) dapat digabungkan dengan masing-masing tipe sebelumnya. Ketika pengubah ini digunakan, hanya sebagian dari input yang ditandatangani, membiarkan yang lainnya terbuka untuk modifikasi. Berikut adalah kombinasi yang ada dengan pengubah tersebut:


- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`x81`): Tanda tangan ini berlaku untuk satu input sekaligus mencakup semua output transaksi;
- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`x82`): Tanda tangan ini mencakup satu input, tanpa melakukan output apa pun;
- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`x83`): Tanda tangan ini berlaku untuk satu input dan hanya untuk output yang memiliki indeks yang sama dengan input ini.

> ► *Sinonim yang terkadang digunakan untuk "SigHash" adalah "Signature Hash Types".*
