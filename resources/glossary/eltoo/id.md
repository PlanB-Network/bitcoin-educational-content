---
term: ELTOO
---

Sebuah protokol umum untuk lapisan kedua Bitcoin yang mendefinisikan cara untuk mengelola kepemilikan UTXO secara bersama. Eltoo dirancang oleh Christian Decker, Rusty Russell, dan Olaoluwa Osuntokun, khususnya untuk menyelesaikan masalah yang terkait dengan mekanisme negosiasi dari keadaan saluran Lightning, yaitu, antara pembukaan dan penutupan. Arsitektur Eltoo menyederhanakan proses negosiasi dengan memperkenalkan sistem pengelolaan keadaan yang linear, menggantikan pendekatan berbasis hukuman yang telah ada dengan metode pembaruan yang lebih fleksibel dan kurang punitif. Protokol ini memerlukan penggunaan jenis SigHash baru yang memungkinkan untuk mengabaikan semua input dalam tanda tangan transaksi. SigHash ini awalnya disebut `SIGHASH_NOINPUT`, kemudian `SIGHASH_ANYPREVOUT` (*Output Sebelumnya Apapun*). Implementasinya direncanakan dalam BIP118.

> ► *Eltoo terkadang juga disebut sebagai "LN-Symmetry".*