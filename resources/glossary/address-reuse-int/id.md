---
term: PENGGUNAAN ULANG ALAMAT (INT)

---
Penggunaan ulang alamat dikatakan "internal" jika terjadi dalam transaksi yang sama, baik sebagai input maupun output. Dalam konfigurasi ini, penggunaan ulang alamat internal merupakan sebuah heuristik analisis blockchain yang memungkinkan adanya sebuah hipotesis yang masuk akal mengenai perubahan transaksi. Memang, jika terdapat dua output dan salah satunya menggunakan alamat penerima yang sama dengan input, maka kemungkinan besar output kedua akan keluar dari kepemilikan pengguna awal. Keluaran dengan alamat yang digunakan kembali kemungkinan besar mewakili perubahan tersebut.

![](../../dictionnaire/assets/10.webp)