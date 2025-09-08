---
term: MULTI PATH PAYMENT (MPP)
---

Istilah umum untuk semua teknik pembayaran di Lightning yang memungkinkan sebuah transaksi dipecah menjadi beberapa bagian yang lebih kecil dan dilewatkan rute yang berbeda. Dengan kata lain, setiap pecahan pembayaran mengambil jalur node yang berbeda. Hal ini memungkinkan untuk melewati batasan likuiditas pada satu saluran dalam rute.


MPP juga menawarkan sedikit keuntungan dalam hal kerahasiaan, karena menjadi lebih sulit bagi pengamat untuk menghubungkan setiap fragmen pembayaran dengan keseluruhan transaksi. Akan tetapi, pada versi dasarnya, semua fragmen memiliki rahasia (_secret_) yang sama untuk HTLC, yang dapat membuat transaksi dapat dilacak jika ada pengamat yang hadir di beberapa rute. Terlebih lagi, karena rahasianya unik untuk semua pecahan pembayaran, rahasia ini tidak bersifat atomik. Ini berarti bahwa beberapa bagian dari pembayaran dapat dieksekusi dengan sukses, sementara yang lainnya mungkin gagal. Kelemahan ini diatasi dengan implementasi "_Atomic Multi-Path Payment_" atau "Pembayaran Multi-Lintasan Atom".
