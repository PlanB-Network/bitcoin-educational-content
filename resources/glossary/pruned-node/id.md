---
term: PRUNED NODE
---

Sebuah pruned node, dalam bahasa Inggris "Pruned Node", adalah full node yang melakukan pemangkasan pada blockchain. Ini melibatkan penghapusan bertahap blok-blok tertua, setelah memverifikasi mereka dengan benar, untuk hanya menyimpan blok-blok terbaru. Batas penyimpanan ditentukan dalam file `bitcoin.conf` melalui parameter `prune=n`, di mana `n` adalah ukuran maksimum yang diambil oleh blok dalam megabita (MB). Jika `0` dicatat setelah parameter ini, maka pemangkasan dinonaktifkan, dan node mempertahankan blockchain secara keseluruhan.

Pruned nodes terkadang dianggap sebagai jenis node yang berbeda dari full nodes. Penggunaan pruned node bisa sangat menarik bagi pengguna yang menghadapi keterbatasan kapasitas penyimpanan. Saat ini, sebuah full node harus memiliki hampir 600 GB hanya untuk menyimpan blockchain. Sebuah pruned node dapat membatasi penyimpanan yang diperlukan hingga 550 MB. Meskipun menggunakan ruang disk lebih sedikit, pruned node mempertahankan tingkat verifikasi dan validasi yang serupa dengan full node. Pruned nodes oleh karena itu menawarkan lebih banyak kepercayaan kepada penggunanya dibandingkan dengan light nodes (SPV).