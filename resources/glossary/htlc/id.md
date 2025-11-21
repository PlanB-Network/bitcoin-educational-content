---
term: HTLC
---

Singkatan dari "*Hashed Timelock Contract*". Hal ini adalah mekanisme kontrak pintar yang terutama digunakan pada Jaringan Lightning, yang kadang-kadang juga ditemukan dalam pertukaran atom (_atomic exchange_). Pada dasarnya, HTLC membuat transfer uang bergantung pada pengungkapan suatu rahasia (_secret_), dan juga menyertakan kondisi waktu untuk melindungi uang pengirim jika terjadi transaksi yang gagal.


Pada Lightning, HTLC memungkinkan Anda untuk mengirim bitcoin ke sebuah node yang tidak memiliki saluran langsung dengan Anda, dengan melewati beberapa saluran, tanpa memerlukan kepercayaan di sepanjang jalan. Pembayaran antara setiap node bergantung pada penyediaan pra-gambar (rahasia yang, ketika di-_hash_, sesuai dengan nilai yang disepakati). Jika penerima akhir memiliki pra-citra ini, ia dapat mengklaim dana, dan tentu saja memungkinkan setiap node perantara untuk mengklaim dana secara bertingkat.


Sebagai contoh, jika Alice ingin mengirim 1 BTC ke David, tetapi tidak memiliki saluran langsung dengannya, ia harus melalui Bob dan Carol, yang memiliki saluran pembayaran satu sama lain. Berikut cara kerja transaksinya:




- David memberikan Alice sebuah _Invoice_ Lightning. Ini berisi _Hash_ $h$ dari rahasia $s$ (_preimage_) yang hanya diketahui oleh David. Jadi: $h = \text{Hash}(s)$ ;
- Alice membuat HTLC dengan Bob, yang menawarkan untuk mengiriminya 1 BTC dengan syarat Bob memberinya rahasia $s$ (_preimage_) yang sesuai dengan _Hash_ $h$;
- Bob membuat HTLC dengan Carol, yang menawarkan untuk mengiriminya 1 BTC dengan syarat dia memberikan rahasia $s$ yang sama;
- Carol membuat HTLC dengan David, yang menawarkan 1 BTC lagi jika dia mengungkapkan preimage $s$;
- David mengungkapkan $s$ (yang hanya diketahui olehnya) kepada Carol untuk menerima 1 BTC. Carol sekarang dapat menggunakan $s$ untuk mendapatkan BTC dari Bob. Dan Bob, yang sekarang mengetahui $s$, melakukan hal yang sama dengan Alice.


Akhirnya, Alice mengirimkan 1 BTC kepada David melalui Bob dan Carol, tanpa harus saling percaya satu sama lain, karena semuanya dijamin secara berjenjang oleh ketentuan HTLC.


Dengan demikian, HTLC memungkinkan apa yang disebut sebagai pertukaran "atomik": transfer sepenuhnya berhasil, atau gagal, dan dana dikembalikan. Hal ini menjamin keamanan transaksi, bahkan di antara banyak peserta tanpa perlu kepercayaan.
