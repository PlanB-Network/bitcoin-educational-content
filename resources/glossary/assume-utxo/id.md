---
term: ASSUME UTXO
---

Sebuah parameter konfigurasi pada klien Bitcoin Core terdepan yang memungkinkan sebuah node yang baru diinisialisasi (namun belum menjalani IBD) untuk menunda verifikasi transaksi dan set UTXO sampai sebuah snapshot tertentu. Konsep ini bergantung pada penggunaan set UTXO (daftar semua UTXO yang ada pada suatu waktu tertentu) yang disediakan oleh Core dan dianggap akurat, yang memungkinkan node untuk disinkronkan dengan sangat cepat dengan rantai yang memiliki pekerjaan terakumulasi terbanyak. Karena node melewatkan langkah IBD yang memakan waktu, ia menjadi operasional untuk penggunanya dengan sangat cepat. Assume UTXO membagi sinkronisasi (IBD) menjadi dua bagian:
* Pertama, node melakukan Sinkronisasi Header Pertama (verifikasi header saja) dan menganggap set UTXO yang disediakan oleh Core sebagai valid;
* Kemudian, setelah operasional, node akan memverifikasi sejarah blok lengkap di latar belakang, memperbarui set UTXO baru yang telah diverifikasi sendiri. Jika set UTXO baru ini tidak cocok dengan yang disediakan oleh Core, itu akan menghasilkan pesan kesalahan.

Oleh karena itu, Assume UTXO mempercepat persiapan node Bitcoin baru dengan menunda proses verifikasi transaksi dan set UTXO melalui snapshot yang diperbarui yang disediakan di Core.