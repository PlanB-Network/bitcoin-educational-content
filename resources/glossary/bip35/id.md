---
term: BIP35

---
Proposal yang mengizinkan sebuah node Bitcoin untuk membuka informasi mengenai mempool-nya, yang berarti transaksi yang menunggu konfirmasi. Berkat ini, peserta lain dapat menerima data real-time tentang transaksi yang belum dikonfirmasi dengan mengirimkan pesan tertentu ke sebuah node. Sebelum adopsi BIP35, node hanya dapat mengakses informasi tentang transaksi yang sudah dikonfirmasi. Peningkatan ini menawarkan dompet SPV kemampuan untuk menerima informasi tentang transaksi yang belum dikonfirmasi, memungkinkan penambang untuk menghindari transaksi yang hilang dengan biaya tinggi selama restart, dan memfasilitasi analisis informasi mempool oleh layanan eksternal.