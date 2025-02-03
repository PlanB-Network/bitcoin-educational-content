---
term: BIP61

---
Memperkenalkan pesan penolakan dalam protokol komunikasi antar node. Tujuan dari BIP61 adalah untuk menambahkan mekanisme umpan balik ketika sebuah node menerima transaksi atau blok dari node lain yang dianggap tidak valid. Pesan penolakan ini akan memungkinkan sebuah node untuk memberi sinyal kepada pengirim alasan mengapa pesan tersebut ditolak. Jenis komunikasi ini dimaksudkan untuk meningkatkan interoperabilitas di antara klien yang berbeda dan komunikasi antara node penuh dan klien SPV. Fungsi yang dibawa oleh BIP61 pada akhirnya ditinggalkan mulai dari versi 0.20.0 Bitcoin Core, karena dianggap tidak perlu sementara mereka melibatkan peningkatan kebutuhan bandwidth.