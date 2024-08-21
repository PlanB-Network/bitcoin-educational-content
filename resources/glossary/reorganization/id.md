---
term: REORGANISASI
---

Merujuk pada fenomena di mana blockchain mengalami modifikasi strukturnya karena adanya blok yang bersaing pada tingkat yang sama. Hal ini terjadi ketika sebagian dari blockchain digantikan oleh rantai lain yang memiliki jumlah pekerjaan terakumulasi yang lebih besar.

Reorganisasi ini merupakan bagian dari fungsi alami Bitcoin, di mana penambang yang berbeda mungkin menemukan blok baru hampir secara bersamaan, sehingga membagi jaringan Bitcoin menjadi dua. Dalam kasus seperti itu, jaringan dapat sementara terbagi menjadi rantai yang bersaing. Akhirnya, ketika salah satu dari rantai ini mengakumulasi lebih banyak pekerjaan, rantai lain ditinggalkan oleh node, dan blok mereka menjadi apa yang disebut "blok usang" atau "blok yatim". Proses penggantian satu rantai dengan yang lain ini adalah reorganisasi.

![](../../dictionnaire/assets/9.png)

Reorganisasi dapat memiliki berbagai konsekuensi. Pertama, jika pengguna memiliki transaksi yang dikonfirmasi dalam blok yang ternyata ditinggalkan, tetapi transaksi ini tidak muncul dalam rantai yang akhirnya valid, maka transaksi mereka menjadi tidak terkonfirmasi lagi. Inilah mengapa disarankan untuk selalu menunggu setidaknya 6 konfirmasi untuk menganggap transaksi sebagai benar-benar tidak dapat diubah. Setelah 6 blok dalam, reorganisasi sangat tidak mungkin sehingga kemungkinan terjadinya dapat dianggap hampir nol.

Selanjutnya, di tingkat sistem global, reorganisasi menyiratkan pemborosan daya komputasi penambang. Memang, ketika terjadi pemisahan, beberapa penambang akan berada di rantai `A`, dan yang lain di rantai `B`. Jika rantai `B` akhirnya ditinggalkan selama reorganisasi, maka seluruh daya komputasi yang dikerahkan oleh penambang di rantai ini, menurut definisi, terbuang sia-sia. Jika terlalu banyak reorganisasi di jaringan Bitcoin, keamanan keseluruhan dari jaringan tersebut berkurang. Inilah sebagian alasan mengapa meningkatkan ukuran blok atau mengurangi interval antar setiap blok (10 menit) dapat berbahaya.

> ► *Beberapa pengguna Bitcoin lebih suka menggunakan "blok yatim" untuk merujuk pada blok yang kedaluwarsa. Selain itu, dalam percakapan umum, "reorg" digunakan untuk merujuk pada "reorganisasi." Istilah "reorganisasi" adalah Anglicisme. Untuk lebih akurat, seseorang dapat berbicara tentang "resinkronisasi."*