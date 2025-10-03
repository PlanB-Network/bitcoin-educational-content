---
term: BIP0030

---
Proposal ini ditujukan untuk perbaikan yang melibatkan _soft fork_, yang diimplementasikan pada tanggal 15 Maret 2012, untuk menyelesaikan masalah pengidentifikasi transaksi ganda. Sebelum BIP30, secara teknis ada kemungkinan bahwa terdapat dua transaksi yang berbeda dengan pengenal transaksi (TXID) yang sama di dalam _blockchain_. Hal ini terjadi dua kali untuk transaksi _coinbase_: transaksi _coinbase_ di blok 91.880 memiliki TXID yang sama dengan _coinbase_ di blok 91.722, dan _coinbase_ 91.842 memiliki TXID yang sama dengan _coinbase_ di blok 91.812. BIP30 mengatasi kekurangan ini dengan memberlakukan aturan baru yang sederhana: tidak ada transaksi baru yang dapat memiliki TXID yang sama dengan transaksi yang tercatat sebelumnya kecuali jika transaksi asli telah sepenuhnya dibelanjakan (yaitu, semua outputnya telah digunakan). _Soft fork _ini diaktifkan dengan menggunakan metode _flag day_. Dengan demikian, ini adalah salah satu UASF yang pertama diaktifkan.
