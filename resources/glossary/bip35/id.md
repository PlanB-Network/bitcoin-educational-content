---
term: BIP35
---

Proposal yang memungkinkan sebuah node Bitcoin untuk membuka informasi tentang mempool-nya, yang berarti transaksi-transaksi yang menunggu konfirmasi. Berkat ini, peserta lain dapat menerima data real-time tentang transaksi yang belum dikonfirmasi dengan mengirimkan pesan spesifik ke sebuah node. Sebelum adopsi BIP35, node hanya dapat mengakses informasi tentang transaksi yang sudah dikonfirmasi. Peningkatan ini menawarkan dompet SPV kemampuan untuk menerima informasi tentang transaksi yang belum dikonfirmasi, memungkinkan penambang untuk menghindari kehilangan transaksi dengan biaya tinggi selama restart, dan memfasilitasi analisis informasi mempool oleh layanan eksternal.