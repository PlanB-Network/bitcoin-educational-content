---
term: P2PK

---
P2PK adalah singkatan dari *Pay to Public Key*, yang merupakan model skrip standar yang digunakan pada Bitcoin untuk menetapkan kondisi pembelanjaan pada UTXO. Hal ini memungkinkan untuk penguncian bitcoin secara langsung ke kunci publik dan bukan ke alamat penerimaan.

Secara teknis, skrip P2PK berisi kunci publik dan instruksi yang meminta tanda tangan digital yang sesuai untuk membuka kunci dana. Ketika pemilik ingin membelanjakan bitcoin, mereka harus memberikan tanda tangan yang dibuat dengan kunci privat yang terkait. Tanda tangan ini diverifikasi menggunakan ECDSA (*Eliptic Curve Digital Signature Algorithm*). P2PK sering digunakan pada versi awal Bitcoin, terutama oleh Satoshi Nakamoto. Saat ini, P2PK hampir tidak lagi digunakan.
