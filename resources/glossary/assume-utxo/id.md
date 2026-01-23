---
term: Assume utxo

definition: Parameter Bitcoin Core yang memungkinkan sinkronisasi cepat node baru dengan menggunakan snapshot dari set UTXO yang dianggap valid, sebelum memverifikasi riwayat di latar belakang.
---
Parameter konfigurasi dalam klien mayoritas Bitcoin Core yang memungkinkan node yang baru saja diinisialisasi (tetapi belum melakukan IBD) untuk menunda verifikasi transaksi dan set UTXO sebelum snapshot tertentu. Konsep ini didasarkan pada penggunaan set UTXO (daftar semua UTXO yang ada pada waktu tertentu) yang disediakan oleh Core dan dianggap akurat, yang memungkinkan node untuk disinkronkan dengan sangat cepat pada rantai dengan akumulasi kerja terbanyak. Karena node melewati tahap IBD yang panjang, node tersebut menjadi fungsional bagi penggunanya dengan sangat cepat.

Assume UTXO membagi sinkronisasi (IBD) menjadi dua bagian: Pertama, node melakukan Header First Sync (hanya verifikasi header) dan menganggap valid set UTXO yang disediakan oleh Core; Kemudian, setelah berfungsi, node akan memverifikasi riwayat blok lengkap di latar belakang, memperbarui set UTXO baru yang telah diverifikasi sendiri. Jika yang terakhir tidak cocok dengan set UTXO yang disediakan oleh Core, ia akan memberikan pesan kesalahan.

Assume UTXO memungkinkan percepatan penyiapan node Bitcoin baru dengan menunda proses verifikasi transaksi dan set UTXO berkat snapshot terbaru yang disediakan di Core.





