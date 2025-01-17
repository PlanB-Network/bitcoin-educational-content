---
term: ASUMSI UTXO

---
Sebuah parameter konfigurasi pada klien Bitcoin Core terkemuka yang memungkinkan sebuah node yang baru saja diinisialisasi (tetapi belum menjalani IBD) untuk menunda verifikasi transaksi dan set UTXO hingga snapshot yang diberikan. Konsep ini bergantung pada penggunaan set UTXO (daftar semua UTXO yang ada pada waktu tertentu) yang disediakan oleh Core dan dianggap akurat, yang memungkinkan node disinkronkan dengan sangat cepat dengan rantai yang memiliki akumulasi pekerjaan paling banyak. Karena node melewatkan langkah IBD yang panjang, maka node dapat beroperasi dengan sangat cepat bagi penggunanya. Asumsikan UTXO membagi sinkronisasi (IBD) menjadi dua bagian:


- Pertama, node melakukan Header First Sync (verifikasi header saja) dan menganggap set UTXO yang disediakan oleh Core sebagai valid;
- Kemudian, setelah beroperasi, node akan memverifikasi riwayat blok lengkap di latar belakang, memperbarui set UTXO baru yang telah diverifikasi sendiri. Jika set UTXO baru ini tidak cocok dengan yang disediakan oleh Core, maka akan menghasilkan pesan kesalahan.

Oleh karena itu, Asumsikan UTXO mempercepat persiapan node Bitcoin baru dengan menunda proses verifikasi transaksi dan set UTXO melalui snapshot terbaru yang disediakan di Core.