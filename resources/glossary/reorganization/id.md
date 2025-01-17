---
term: REORGANISASI

---
Mengacu pada sebuah fenomena di mana blockchain mengalami modifikasi struktur karena adanya blok yang bersaing pada ketinggian yang sama. Ini terjadi ketika sebagian blockchain digantikan oleh rantai lain yang memiliki jumlah akumulasi pekerjaan yang lebih besar.

Reorganisasi ini merupakan bagian dari fungsi alami Bitcoin, di mana penambang yang berbeda dapat menemukan blok baru hampir secara bersamaan, sehingga membagi jaringan Bitcoin menjadi dua. Dalam kasus seperti ini, jaringan dapat terbagi menjadi dua rantai yang saling bersaing untuk sementara waktu. Pada akhirnya, ketika salah satu rantai ini mengumpulkan lebih banyak pekerjaan, rantai lainnya akan ditinggalkan oleh node, dan blok mereka menjadi apa yang disebut "blok usang" atau "blok yatim piatu" Proses penggantian satu rantai dengan rantai yang lain adalah reorganisasi.

![](../../dictionnaire/assets/9.webp)

Pengorganisasian ulang dapat memiliki berbagai konsekuensi. Pertama, jika pengguna memiliki transaksi yang telah dikonfirmasi dalam sebuah blok yang ternyata ditinggalkan, tetapi transaksi ini tidak muncul dalam rantai yang valid, maka transaksi mereka menjadi tidak terkonfirmasi lagi. Inilah sebabnya mengapa disarankan untuk selalu menunggu setidaknya 6 konfirmasi untuk mempertimbangkan sebuah transaksi sebagai transaksi yang benar-benar tidak dapat diubah. Setelah 6 blok, reorganisasi sangat kecil kemungkinannya sehingga kemungkinan terjadinya reorganisasi dapat dianggap hampir nol.

Lebih jauh lagi, pada tingkat sistem global, reorganisasi menyiratkan pemborosan daya komputasi para penambang. Memang, ketika perpecahan terjadi, beberapa penambang akan berada di rantai `A`, dan yang lainnya di rantai `B`. Jika rantai `B` pada akhirnya ditinggalkan selama reorganisasi, maka semua daya komputasi yang digunakan oleh para penambang di rantai ini, menurut definisi, akan terbuang. Jika terdapat terlalu banyak reorganisasi dalam jaringan Bitcoin, maka keamanan secara keseluruhan akan berkurang. Inilah sebagian alasan mengapa meningkatkan ukuran blok atau mengurangi interval antara setiap blok (10 menit) dapat menjadi berbahaya.

> ► *Beberapa pengguna bitcoin lebih suka menggunakan "orphan block" untuk merujuk pada blok yang sudah kadaluarsa. Selain itu, dalam bahasa umum, "reorg" digunakan untuk merujuk pada "reorganisasi" Istilah "reorganisasi" adalah sebuah Anglikanisme. Agar lebih akurat, seseorang dapat berbicara tentang "sinkronisasi ulang. "*