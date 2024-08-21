---
term: BIP111
---

Mengusulkan penambahan sebuah bit layanan bernama `NODE_BLOOM` untuk memungkinkan node secara eksplisit menunjukkan dukungan mereka terhadap Filter Bloom seperti yang dijelaskan dalam BIP37. Pengenalan `NODE_BLOOM` memungkinkan operator node untuk menonaktifkan layanan ini guna mengurangi risiko DoS. Opsi BIP37 ini dinonaktifkan secara default di Bitcoin Core. Untuk mengaktifkannya, parameter `peerbloomfilters=1` harus dimasukkan dalam file konfigurasi.