---
term: ATOMIC MULTI-PATH PAYMENTS (AMP)

---

Versi MPP (*Multi-Path Payments*) yang disempurnakan di mana setiap fragmen pembayaran memiliki rahasia parsial yang berbeda, memastikan bahwa transaksi diselesaikan secara atomik, yaitu secara penuh atau tidak diselesaikan sama sekali.


MPP adalah teknik pembayaran di _Lightning_ yang memungkinkan sebuah transaksi dipecah menjadi beberapa bagian yang lebih kecil dan dilakukan melalui rute yang berbeda. Dengan kata lain, setiap pecahan pembayaran akan melewati jalur _node_ yang berbeda. Hal ini ditujukan untuk menghindari keterbatasan likuiditas pada satu saluran dalam sebuah rute. Pada MPP dasar, setiap fraksi pembayaran memiliki rahasia yang sama, dan oleh karena itu memiliki _Hash_ yang sama dalam HTLC. Hal ini dapat membuat transaksi dapat dilacak jika ada pengamat yang berada di beberapa rute, karena ia dapat saling menghubungkan semua rahasia ini bersama-sama. Terlebih lagi, karena rahasianya unik untuk semua bagian pembayaran, maka rahasia ini tidak bersifat atomik. Ini berarti bahwa beberapa bagian dari pembayaran dapat dieksekusi dengan sukses, sementara yang lainnya mungkin gagal.


Dalam AMP, rahasia parsial yang unik digunakan untuk setiap pecahan pembayaran. Setelah semua pecahan diterima, mereka memungkinkan penerima untuk merekonstruksi rahasia umum asli dan mengklaim pembayaran penuh. Metode ini membuat penyelesaian pembayaran secara parsial menjadi tidak mungkin, karena kepemilikan semua rahasia parsial diperlukan untuk membuka kunci pembayaran penuh. Hal ini memastikan bahwa pembayaran pasti akan sepenuhnya berhasil atau sepenuhnya tidak berhasil. AMP juga meningkatkan kerahasiaan, karena tidak ada lagi hubungan yang terlihat di antara rute yang berbeda.


Salah satu keuntungan dari AMP adalah bahwa AMP dapat berfungsi meskipun hanya penerima dan pengirim yang menerapkan metode ini. Simpul perantara memproses pembayaran ini sebagai transaksi biasa dengan menggunakan HTLC, tanpa mengetahui bahwa mereka memproses sebagian kecil dari pembayaran yang lebih besar.
