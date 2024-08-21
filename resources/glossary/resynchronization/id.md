---
term: RESYNCHRONIZATION
---

Merujuk pada fenomena di mana blockchain mengalami modifikasi strukturnya karena adanya blok yang bersaing pada tingkat yang sama. Hal ini terjadi ketika sebagian dari blockchain digantikan oleh rantai lain dengan jumlah pekerjaan yang terakumulasi lebih besar.

Resynchronizations merupakan bagian dari fungsi alami Bitcoin, di mana penambang yang berbeda mungkin menemukan blok baru hampir secara bersamaan, sehingga membagi jaringan Bitcoin menjadi dua. Dalam kasus seperti itu, jaringan dapat sementara terbagi menjadi rantai yang bersaing. Akhirnya, ketika salah satu dari rantai ini mengakumulasi lebih banyak pekerjaan, rantai lainnya ditinggalkan oleh node, dan blok mereka menjadi apa yang disebut "blok usang" atau "blok yatim." Proses penggantian satu rantai dengan yang lain ini adalah resynchronisasi.

![](../../dictionnaire/assets/9.png)

Resynchronizations dapat memiliki berbagai konsekuensi. Pertama, jika pengguna memiliki transaksi yang dikonfirmasi dalam blok yang ternyata ditinggalkan, tetapi transaksi ini tidak ditemukan dalam rantai yang akhirnya valid, maka transaksi mereka menjadi tidak terkonfirmasi lagi. Inilah mengapa disarankan untuk selalu menunggu setidaknya 6 konfirmasi untuk menganggap transaksi sebagai benar-benar tidak dapat diubah. Setelah 6 blok dalam, resynchronizations sangat tidak mungkin sehingga kemungkinan terjadinya dapat dianggap hampir nol.

Selanjutnya, di tingkat sistem global, resynchronizations menyiratkan pemborosan daya komputasi penambang. Memang, ketika terjadi pemisahan, beberapa penambang akan berada di rantai `A`, dan yang lain di rantai `B`. Jika rantai `B` akhirnya ditinggalkan selama resynchronisasi, maka seluruh daya komputasi yang dikerahkan oleh penambang di rantai ini, menurut definisi, terbuang sia-sia. Jika terlalu banyak resynchronizations di jaringan Bitcoin, keamanan keseluruhan jaringan oleh karena itu berkurang. Inilah sebagian alasan mengapa meningkatkan ukuran blok atau mengurangi interval antar setiap blok (10 menit) dapat berbahaya.

> ► *Beberapa bitcoiners lebih suka menggunakan "blok yatim" untuk merujuk pada blok yang kedaluwarsa. Selain itu, meskipun merupakan Anglicisme, dalam bahasa sehari-hari, "reorganisasi" atau "reorg" sering lebih disukai daripada "resynchronisasi."*