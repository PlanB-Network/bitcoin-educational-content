---
term: P2PK
---

P2PK merupakan singkatan dari *Pay to Public Key*. Ini adalah model skrip standar yang digunakan pada Bitcoin untuk menetapkan kondisi pengeluaran pada sebuah UTXO. Ini memungkinkan penguncian bitcoin langsung ke sebuah kunci publik, daripada sebuah alamat.
Secara teknis, skrip P2PK mengandung sebuah kunci publik dan sebuah instruksi yang menuntut tanda tangan digital yang sesuai untuk membuka dana tersebut. Ketika pemilik ingin menghabiskan bitcoin mereka, mereka harus menyediakan tanda tangan yang dihasilkan dengan kunci privat yang terkait. Tanda tangan ini diverifikasi menggunakan ECDSA (*Elliptic Curve Digital Signature Algorithm*). P2PK sering digunakan dalam versi awal Bitcoin, terutama oleh Satoshi Nakamoto. Saat ini, hampir tidak digunakan lagi.