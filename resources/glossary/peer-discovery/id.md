---
term: PEER DISCOVERY

---
Proses di mana node dalam jaringan Bitcoin terhubung ke node lain untuk mendapatkan informasi. Ketika sebuah node Bitcoin pertama kali diluncurkan, ia tidak memiliki informasi mengenai node lain dalam jaringan. Namun, node tersebut harus membuat koneksi untuk melakukan sinkronisasi dengan _blockchain_ yang memiliki akumulasi pekerjaan paling banyak. Beberapa mekanisme digunakan untuk menemukan rekan-rekan ini, berdasarkan urutan prioritas:


- Node dimulai dengan melihat file `peers.dat` lokalnya, yang menyimpan informasi tentang _node-node_ yang pernah berinteraksi dengannya. Jika merupakan node baru, file ini kosong, dan proses akan pindah ke langkah berikutnya;
- Dengan tidak adanya informasi dalam file `peers.dat` (yang normal untuk node yang baru diluncurkan), node melakukan permintaan DNS ke _seed_ DNS. Server ini menyediakan daftar alamat IP dari node yang mungkin aktif untuk membuat koneksi. Alamat dari seed DNS dikodekan dalam kode Bitcoin Core. Langkah ini biasanya cukup untuk menyelesaikan penemuan _peer_;
- Jika seed DNS tidak merespons dalam waktu 60 detik, maka node tersebut dapat beralih ke _seed_ node. Ini adalah node Bitcoin publik yang terdaftar dalam daftar statis yang terdiri dari hampir seribu entri yang diintegrasikan langsung ke dalam kode sumber Bitcoin Core. Node baru akan menggunakan daftar ini untuk membuat koneksi pertama ke jaringan dan mendapatkan alamat IP dari node lain;
- Dalam kasus yang sangat tidak mungkin di mana semua metode sebelumnya gagal, operator node selalu memiliki opsi untuk menambahkan alamat IP node secara manual untuk membuat koneksi pertama.
