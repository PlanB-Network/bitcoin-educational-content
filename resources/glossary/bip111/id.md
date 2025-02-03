---
term: BIP111

---
Mengusulkan penambahan bit layanan bernama `NODE_BLOOM` untuk memungkinkan node secara eksplisit memberi sinyal dukungan mereka untuk Bloom Filter seperti yang dijelaskan dalam BIP37. Pengenalan `NODE_BLOOM` memungkinkan operator node untuk menonaktifkan layanan ini untuk mengurangi risiko DoS. Opsi BIP37 dinonaktifkan secara default di Bitcoin Core. Untuk mengaktifkannya, parameter `peerbloomfilters=1` harus dimasukkan ke dalam file konfigurasi.