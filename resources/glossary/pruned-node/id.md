---
term: PRUNED NODE

---
Sebuah node yang dipangkas, dalam bahasa Inggris "_Pruned Node_", adalah sebuah node penuh yang melakukan pemangkasan pada _blockchain_. Hal ini melibatkan penghapusan blok-blok tertua secara progresif, setelah memverifikasinya dengan benar, dan hanya menyimpan blok-blok terbaru. Batas penyimpanan ditentukan dalam file `bitcoin.conf` melalui parameter `prune=n`, di mana `n` adalah ukuran maksimum yang diambil oleh blok dalam megabyte (MB). Jika `0` dicatat setelah parameter ini, maka pemangkasan dinonaktifkan, dan node akan menyimpan _blockchain_ secara keseluruhan.

Node yang dipangkas terkadang dianggap sebagai jenis node yang berbeda dari node penuh. Penggunaan _pruned node_ dapat menjadi sangat menarik bagi pengguna yang menghadapi kendala kapasitas penyimpanan. Saat ini, sebuah node penuh harus memiliki hampir 600 GB hanya untuk menyimpan _blockchain_. Sebuah _pruned node_ dapat membatasi penyimpanan yang dibutuhkan hingga 550 MB. Meskipun menggunakan lebih sedikit ruang disk, pruned node mempertahankan tingkat verifikasi dan validasi yang serupa dengan node penuh. Oleh karena itu, _pruned node_ menawarkan kepercayaan yang lebih besar kepada penggunanya dibandingkan dengan node ringan (SPV).
