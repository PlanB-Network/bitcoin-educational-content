---
term: BLK*.DAT

---
Nama file dalam Bitcoin Core yang menyimpan data blok mentah dari blockchain. Setiap file diidentifikasi dengan nomor unik pada namanya. Dengan demikian, blok-blok tersebut dicatat dalam urutan kronologis, dimulai dengan file blk00000.dat. Ketika file ini mencapai kapasitas maksimumnya, blok-blok berikutnya dicatat dalam blk00001.dat, kemudian blk00002.dat, dan seterusnya. Setiap file blk memiliki kapasitas maksimum 128 mebibita (MiB), yang setara dengan sedikit di atas 134 megabyte (MB). File-file ini telah dipindahkan ke folder `/blocks` sejak versi 0.8.0.