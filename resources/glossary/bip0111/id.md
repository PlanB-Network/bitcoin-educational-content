---
term: BIP0111

definition: Penambahan bit layanan NODE_BLOOM yang memungkinkan node untuk memberi sinyal dukungan mereka terhadap Bloom Filter (BIP37).
---
BIP yang mengusulkan penambahan bit layanan bernama `NODE_BLOOM` untuk memungkinkan node secara eksplisit memberi sinyal dukungan mereka untuk _Bloom Filter_ seperti yang dipaparkan dalam BIP37. Pengenalan `NODE_BLOOM` memungkinkan operator node untuk menonaktifkan layanan ini untuk mengurangi risiko DoS. Opsi BIP37 dinonaktifkan secara default di Bitcoin Core. Untuk mengaktifkannya, parameter `peerbloomfilters=1` harus dimasukkan ke dalam file konfigurasi.
