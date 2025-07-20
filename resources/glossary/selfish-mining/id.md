---
term: SELFISH MINING
---

Strategi (atau serangan) dalam penambangan Bitcoin, di mana seorang atau sekelompok penambang dengan sengaja menahan blok dengan _Proof-of-Work_ yang valid tanpa segera melepaskannya ke jaringan. Tujuannya adalah untuk tetap berada di depan penambang lain dalam hal _Proof-of-Work_, yang memungkinkan mereka untuk melakukan penambangan beberapa blok secara berurutan dan mempublikasikannya sekaligus, sehingga memaksimalkan keuntungan mereka. Dengan kata lain, kelompok penambang yang menyerang tidak menambang di blok terakhir yang divalidasi oleh seluruh jaringan, melainkan di blok yang mereka buat sendiri, yang berbeda dengan blok yang divalidasi oleh jaringan.


Proses ini menghasilkan semacam cabang rahasia dari _blockchain_, yang tidak diketahui oleh seluruh jaringan sampai rantai alternatif ini berpotensi melebihi penambangan yang jujur. Ketika rantai rahasia penambang yang menyerang menjadi lebih panjang (dengan kata lain, memiliki lebih banyak akumulasi pekerjaan) daripada rantai publik yang jujur, rantai ini kemudian disebarkan ke seluruh jaringan. Pada titik ini, node-node dalam jaringan yang mengikuti rantai terpanjang (dengan akumulasi pekerjaan terbanyak) akan melakukan sinkronisasi ke rantai baru ini sehingga terjadi reorganisasi _blockchain_.


_Selfish Mining_ sangatlah mengganggu bagi pengguna, karena mengurangi keamanan sistem dengan membuang sebagian daya komputasi jaringan. Jika berhasil, hal ini juga menyebabkan reorganisasi _Blockchain_, yang mempengaruhi keandalan konfirmasi transaksi bagi pengguna. Akan tetapi, praktik ini tetap berisiko bagi kelompok penambang yang menyerang, karena seringkali lebih menguntungkan untuk penambang yang biasanya berada di atas blok terakhir yang diketahui publik daripada mengalokasikan daya komputasi ke cabang rahasia yang mungkin tidak akan pernah melebihi _blockchain_ yang sebenarnya. Semakin besar jumlah blok dalam reorganisasi, semakin rendah kemungkinan serangan yang berhasil.
