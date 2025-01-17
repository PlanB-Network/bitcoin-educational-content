---
term: BIBIT BENIH

---
Daftar statis node Bitcoin publik, terintegrasi langsung ke dalam kode sumber Bitcoin Core (`bitcoin/src/chainparamsseeds.h`). Daftar ini berfungsi sebagai titik koneksi untuk node Bitcoin baru yang bergabung dengan jaringan, tetapi hanya digunakan jika seed DNS tidak memberikan respon dalam 60 detik setelah permintaan mereka. Dalam kasus ini, node Bitcoin baru akan terhubung ke seed node ini untuk membuat koneksi pertama ke jaringan dan meminta alamat IP dari node lain. Tujuan utamanya adalah untuk mendapatkan informasi yang diperlukan untuk melakukan Initial Block Download (IBD) dan melakukan sinkronisasi dengan rantai yang memiliki akumulasi pekerjaan terbanyak. Daftar seed node mencakup hampir 1000 node, yang diidentifikasi sesuai dengan standar yang ditetapkan oleh BIP155. Dengan demikian, seed node mewakili metode koneksi ketiga ke jaringan untuk sebuah node Bitcoin, setelah penggunaan file `peers.dat`, yang dibuat oleh node itu sendiri, dan permintaan seed DNS.

> ► *Catatan, seed node jangan disamakan dengan "seed DNS," yang merupakan metode kedua untuk membangun koneksi.*