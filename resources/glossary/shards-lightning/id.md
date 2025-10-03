---
term: SHARDS (LIGHTNING)
---

Dalam konteks *Multi-Path Payments (MPP)* atau *Atomic Multi-Path Payments (AMP)*, _Shard_ adalah bagian kecil dari pembayaran global. Setiap _shard_ mewakili sebagian dari total pembayaran, yang dirutekan secara terpisah melalui rute yang berbeda di Jaringan Lightning.


Pada MPP, semua pecahan memiliki rahasia yang sama, sedangkan pada AMP, setiap _shard_ memiliki rahasia parsial yang unik. Penerima mengelompokkan pecahan-pecahan tersebut untuk menyusun kembali dan menyelesaikan pembayaran penuh. Mekanisme ini menghindari keterbatasan likuiditas pada satu saluran.
