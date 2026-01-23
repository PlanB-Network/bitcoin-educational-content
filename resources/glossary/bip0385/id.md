---
term: BIP0385

definition: Fungsi addr() dan raw() untuk mendeskripsikan skrip output berdasarkan alamat atau dalam heksadesimal dalam deskriptor.
---
Memperkenalkan fungsi deskriptor `addr(ADDR)` dan `raw(HEX)`. Fungsi `addr(ADDR)` memungkinkan deskripsi skrip keluaran menggunakan alamat penerima, sedangkan fungsi `raw(HEX)` memungkinkan untuk menentukan skrip keluaran menggunakan representasi heksadesimal mentah dari skrip tersebut. BIP385 diimplementasikan bersama dengan semua BIP terkait deskriptor lainnya (kecuali BIP386) dalam versi 0.17 Bitcoin Core.
