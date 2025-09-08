---
term: DIFFIE-HELLMAN

---
Metode kriptografi yang memungkinkan dua pihak untuk menghasilkan rahasia (_secret_) bersama melalui saluran komunikasi yang tidak aman. Rahasia ini kemudian dapat digunakan untuk mengenkripsi komunikasi antara kedua pihak. Diffie-Hellman menggunakan aritmatika modular sehingga, walaupun penyerang dapat mengamati pertukaran yang terjadi, mereka tidak dapat menyimpulkan rahasia bersama tanpa menyelesaikan masalah matematika yang sulit: logaritma diskrit. Dalam Bitcoin, sebuah varian DH yang disebut ECDH yang menggunakan kurva elips terkadang digunakan, terutama untuk protokol alamat statis seperti _Silent Payment_ atau BIP47.
