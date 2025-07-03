---
term: ASSUME UTXO

---
Sebuah parameter konfigurasi pada klien Bitcoin Core terkemuka yang memungkinkan sebuah _node_ yang baru saja diinisialisasi (tetapi belum menjalani IBD) untuk menunda verifikasi transaksi dan set UTXO hingga _snapshot_ yang diberikan. Konsep ini bergantung pada penggunaan set UTXO (daftar semua UTXO yang ada pada waktu tertentu) yang disediakan oleh Core dan dianggap akurat, yang memungkinkan _node_ disinkronkan dengan sangat cepat dengan rantai terpanjang (rantai dengan kerja paling banyak). Karena _node_ melewati langkah IBD yang memakan waktu lama, maka _node_ dapat beroperasi dengan sangat cepat bagi penggunanya. _ASSUME UTXO_ membagi proses sinkronisasi (IBD) menjadi dua bagian:

- Pertama, _node_ melakukan _Header First Sync_ (verifikasi _header_ saja) dan menganggap set UTXO yang disediakan oleh Core valid;
- Kemudian, setelah beroperasi, _node_ akan memverifikasi riwayat blok lengkap di belakang layar, memperbarui set UTXO baru yang telah diverifikasi sendiri. Jika set UTXO baru ini tidak cocok dengan yang disediakan oleh Core, pesan kesalahan akan muncul.

Oleh karena itu, _ASSUME UTXO_ mempercepat persiapan awal _node_ Bitcoin baru dengan menunda proses verifikasi transaksi dan set UTXO melalui _snapshot_ terbaru yang disediakan di Core.
