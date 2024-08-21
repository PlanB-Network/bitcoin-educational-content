---
term: SIGHASH FLAG
---

Sebuah parameter dalam transaksi Bitcoin yang menentukan komponen mana dari transaksi (input dan output) yang dicakup oleh tanda tangan terkait, sehingga menjadi tidak dapat diubah. SigHash Flag adalah byte yang ditambahkan ke tanda tangan digital dari setiap input. Oleh karena itu, pilihan SigHash Flag secara langsung mempengaruhi bagian mana dari transaksi yang dibekukan oleh tanda tangan dan mana yang masih dapat dimodifikasi setelahnya. Mekanisme ini memastikan bahwa tanda tangan secara tepat dan aman mengikat data transaksi sesuai dengan niat penandatangan. Ada tiga SigHash Flag utama:

- `SIGHASH_ALL` (`0x01`): Tanda tangan berlaku untuk semua input dan output dari transaksi, sehingga menguncinya sepenuhnya;

- `SIGHASH_NONE` (`0x02`): Tanda tangan berlaku untuk semua input tetapi tidak untuk output mana pun, memungkinkan output untuk dimodifikasi setelah tanda tangan;

- `SIGHASH_SINGLE` (`0x03`): Tanda tangan mencakup semua input dan hanya satu output yang sesuai dengan indeks dari input yang ditandatangani.

Selain ketiga SigHash Flag ini, modifikator `SIGHASH_ANYONECANPAY` (`0x80`) dapat dikombinasikan dengan masing-masing tipe sebelumnya. Ketika modifikator ini digunakan, hanya sebagian dari input yang ditandatangani, meninggalkan yang lain terbuka untuk modifikasi. Berikut adalah kombinasi yang ada dengan modifikator:

- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): Tanda tangan berlaku untuk satu input sambil mencakup semua output dari transaksi;

- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`): Tanda tangan mencakup satu input, tanpa berkomitmen pada output mana pun;

- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): Tanda tangan berlaku untuk satu input dan hanya untuk output yang memiliki indeks yang sama dengan input ini.

> ► *Sinonim yang terkadang digunakan untuk "SigHash" adalah "Jenis Hash Tanda Tangan".*