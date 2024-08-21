---
term: BIP61
---

Memperkenalkan pesan penolakan dalam protokol komunikasi antar node. Tujuan dari BIP61 adalah untuk menambahkan mekanisme umpan balik ketika sebuah node menerima transaksi atau blok dari node lain yang dianggap tidak valid. Pesan penolakan ini memungkinkan sebuah node untuk memberi sinyal kepada pengirim tentang alasan penolakannya. Jenis komunikasi ini dimaksudkan untuk meningkatkan interoperabilitas di antara klien yang berbeda dan komunikasi antara full node dan klien SPV. Fungsionalitas yang dibawa oleh BIP61 akhirnya ditinggalkan mulai dari versi 0.20.0 dari Bitcoin Core, karena dianggap tidak perlu sementara itu melibatkan kebutuhan bandwidth yang meningkat.