---
term: SELFISH Mining
---

Strategi (atau serangan) dalam Mining, di mana sebuah Miner atau sekelompok penambang dengan sengaja menahan blok dengan Proof of Work yang valid tanpa segera melepaskannya ke jaringan. Tujuannya adalah untuk tetap berada di depan penambang lain dalam hal Proof of Work, yang memungkinkan mereka untuk melakukan Miner beberapa blok secara berurutan dan mempublikasikannya sekaligus, sehingga memaksimalkan keuntungan mereka. Dengan kata lain, kelompok penambang yang menyerang tidak menambang di blok terakhir yang divalidasi oleh seluruh jaringan, melainkan di blok yang mereka buat sendiri, yang berbeda dengan blok yang divalidasi oleh jaringan.


Proses ini menghasilkan semacam cabang rahasia dari Blockchain, yang tidak diketahui oleh seluruh jaringan sampai rantai alternatif ini berpotensi melebihi Blockchain yang jujur. Ketika rantai rahasia penambang yang menyerang menjadi lebih panjang (dengan kata lain, mengandung lebih banyak akumulasi pekerjaan) daripada rantai publik yang jujur, rantai ini kemudian disebarkan ke seluruh jaringan. Pada titik ini, node-node dalam jaringan yang mengikuti rantai terpanjang (dengan akumulasi pekerjaan terbanyak) akan melakukan sinkronisasi ke rantai baru ini. Jadi, terjadi reorganisasi.


Keegoisan Mining sangat mengganggu bagi pengguna, karena mengurangi keamanan sistem dengan membuang sebagian daya komputasi jaringan. Jika berhasil, hal ini juga menyebabkan reorganisasi Blockchain, yang mempengaruhi keandalan konfirmasi transaksi bagi pengguna. Akan tetapi, praktik ini tetap berisiko bagi kelompok penambang yang menyerang, karena seringkali lebih menguntungkan untuk Miner yang biasanya berada di atas blok terakhir yang diketahui publik daripada mengalokasikan daya komputasi ke cabang rahasia yang mungkin tidak akan pernah melebihi Blockchain yang sebenarnya. Semakin besar jumlah blok dalam reorganisasi, semakin rendah kemungkinan serangan yang berhasil.