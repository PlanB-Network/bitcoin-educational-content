---
term: ROUND PAYMENT
---

Sebuah heuristik internal untuk analisis rantai pada Bitcoin yang memungkinkan hipotesis tentang sifat dari output sebuah transaksi berdasarkan jumlah yang bulat. Umumnya, ketika dihadapkan pada pola pembayaran yang sederhana (1 input dan 2 output), jika salah satu output menghabiskan jumlah yang bulat, maka itu mewakili pembayaran. Dengan eliminasi, jika satu output mewakili pembayaran, yang lainnya mewakili kembalian. Oleh karena itu, dapat diinterpretasikan bahwa kemungkinan pengguna yang memasukkan transaksi masih memiliki output yang diidentifikasi sebagai kembalian.

Perlu dicatat bahwa heuristik ini tidak selalu berlaku, karena sebagian besar pembayaran masih dilakukan dalam unit mata uang fiat. Memang, ketika seorang pedagang di Prancis menerima bitcoin, umumnya, mereka tidak menampilkan harga stabil dalam sats. Mereka lebih memilih untuk melakukan konversi antara harga dalam euro dan jumlah dalam bitcoin yang harus dibayar melalui POS mereka (seperti BTCPay Server, misalnya). Oleh karena itu, seharusnya tidak ada angka bulat dalam output transaksi. Namun demikian, seorang analis dapat mencoba melakukan konversi ini dengan mempertimbangkan nilai tukar yang berlaku saat transaksi disiarkan di jaringan. Jika suatu hari, bitcoin menjadi unit akun yang disukai dalam pertukaran kita, heuristik ini bisa menjadi lebih berguna untuk analisis.

![](../../dictionnaire/assets/11.png)