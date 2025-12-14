---
term: BIP0152

---
Proposal tentang "_Compact Block Relay_" yang bertujuan untuk mengurangi _bandwidth_ yang dibutuhkan untuk transmisi blok melalui jaringan Bitcoin. Diadopsi pada bulan November 2016 dalam versi 0.13.0 Bitcoin Core, protokol ini memungkinkan komunikasi informasi blok secara ringkas, berdasarkan asumsi bahwa node telah memiliki sebagian besar transaksi blok terbaru dalam mempool mereka. Alih-alih mengirimkan setiap transaksi secara penuh, yang akan mengakibatkan duplikasi, BIP152 mengusulkan untuk hanya mengirimkan pengenal singkat untuk transaksi yang sudah diketahui oleh _peer_-nya, disertai dengan beberapa transaksi yang dipilih (terutama transaksi _coinbase_ dan transaksi yang tidak diketahui oleh node). Node kemudian dapat meminta transaksi yang hilang dari rekan-rekannya. _Compact Block Relay_ mengurangi jumlah data yang dipertukarkan selama penyebaran blok, yang mengurangi lonjakan _bandwidth_ dan meningkatkan efisiensi jaringan secara keseluruhan.
