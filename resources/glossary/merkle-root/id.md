---
term: AKAR MERKLE

---
Digest atau "hash teratas" dari sebuah pohon Merkle, yang merepresentasikan ringkasan dari semua informasi yang ada di dalam pohon tersebut. Pohon Merkle adalah sebuah struktur akumulator kriptografi, terkadang juga disebut "pohon hash". Dalam konteks Bitcoin, pohon Merkle digunakan untuk mengatur transaksi dalam sebuah blok dan untuk memfasilitasi verifikasi cepat atas penyertaan transaksi tertentu. Dengan demikian, dalam blok Bitcoin, akar Merkle didapatkan dengan melakukan hashing transaksi secara berpasangan hingga hanya tersisa satu hash (akar Merkle). Ini kemudian dimasukkan ke dalam header blok yang bersangkutan. Pohon hash ini juga ditemukan di UTREEXO, sebuah struktur yang memungkinkan untuk memadatkan kumpulan node UTXO, dan di MAST Taproot.