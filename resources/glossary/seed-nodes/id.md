---
term: SEED NODES
---

Daftar statis dari node Bitcoin publik, yang terintegrasi langsung ke dalam kode sumber Bitcoin Core (`bitcoin/src/chainparamsseeds.h`). Daftar ini berfungsi sebagai titik koneksi untuk node Bitcoin baru yang bergabung dengan jaringan, tetapi hanya digunakan jika DNS seeds tidak memberikan respons dalam waktu 60 detik dari permintaan mereka. Dalam kasus ini, node Bitcoin baru akan terhubung ke seed nodes ini untuk membangun koneksi pertama ke jaringan dan meminta alamat IP dari node lain. Tujuan utamanya adalah untuk memperoleh informasi yang diperlukan untuk melakukan Initial Block Download (IBD) dan sinkronisasi dengan rantai yang memiliki pekerjaan terakumulasi terbanyak. Daftar seed nodes mencakup hampir 1000 node, yang diidentifikasi sesuai dengan standar yang ditetapkan oleh BIP155. Dengan demikian, seed nodes mewakili metode ketiga koneksi ke jaringan untuk sebuah node Bitcoin, setelah penggunaan file `peers.dat` yang dibuat oleh node itu sendiri, dan permintaan terhadap DNS seeds.

> ► *Catatan, seed nodes tidak boleh dikacaukan dengan "DNS seeds," yang merupakan metode kedua untuk membangun koneksi.*