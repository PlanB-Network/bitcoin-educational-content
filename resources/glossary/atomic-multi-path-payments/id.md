---
term: PEMBAYARAN MULTI-JALUR ATOMIK
---

Versi MPP (*Multi-Path Payments*) yang disempurnakan di mana setiap fragmen pembayaran memiliki rahasia parsial yang berbeda, memastikan bahwa transaksi diselesaikan secara atomik, yaitu secara penuh atau tidak sama sekali.


MPP adalah teknik pembayaran di Lightning yang memungkinkan sebuah transaksi dipecah menjadi beberapa bagian yang lebih kecil dan dirutekan melalui rute yang berbeda. Dengan kata lain, setiap pecahan pembayaran mengambil jalur node yang berbeda. Hal ini menghindari keterbatasan likuiditas pada satu saluran dalam rute. Pada MPP dasar, setiap fraksi pembayaran memiliki rahasia yang sama, dan oleh karena itu memiliki Hash yang sama dalam HTLC. Hal ini dapat membuat transaksi dapat dilacak jika ada pengamat yang berada di beberapa rute, karena ia dapat menghubungkan semua rahasia yang identik ini bersama-sama. Terlebih lagi, karena rahasianya unik untuk semua bagian pembayaran, maka rahasia ini tidak bersifat atomik. Ini berarti bahwa beberapa bagian dari pembayaran dapat dieksekusi dengan sukses, sementara yang lainnya mungkin gagal.


Dalam AMP, rahasia parsial yang unik digunakan untuk setiap pecahan. Setelah semua pecahan diterima, mereka memungkinkan penerima untuk merekonstruksi rahasia umum asli dan mengklaim pembayaran penuh. Metode ini membuat penyelesaian pembayaran secara parsial menjadi tidak mungkin, karena kepemilikan semua rahasia parsial diperlukan untuk membuka kunci pembayaran penuh. Hal ini memastikan bahwa pembayaran sepenuhnya berhasil atau sepenuhnya tidak berhasil (yaitu, atomik). AMP juga meningkatkan kerahasiaan, karena tidak ada lagi tautan yang terlihat di antara rute yang berbeda.


Salah satu keuntungan dari AMP adalah bahwa AMP dapat berfungsi meskipun hanya penerima dan pengirim yang menerapkan metode ini. Simpul perantara memproses pembayaran ini sebagai transaksi konvensional menggunakan HTLC, tanpa menyadari bahwa mereka memproses pecahan dari pembayaran yang lebih besar.