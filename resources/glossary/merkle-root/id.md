---
term: AKAR MERKLE

---
_Digest_ atau "_hash_ teratas" dari sebuah pohon Merkle, yang merepresentasikan ringkasan dari semua informasi yang ada di dalam pohon tersebut. Pohon Merkle adalah sebuah struktur akumulator kriptografi, terkadang juga disebut "pohon _hash_". Dalam konteks Bitcoin, pohon Merkle digunakan untuk mengatur transaksi dalam sebuah blok dan untuk memfasilitasi verifikasi cepat atas penyertaan transaksi tertentu. Dengan demikian, dalam blok Bitcoin, akar Merkle didapatkan dengan melakukan _hashing_ transaksi secara berpasangan hingga hanya tersisa satu _hash_ (akar Merkle). Ini kemudian dimasukkan ke dalam _header_ blok yang bersangkutan. Pohon _hash_ ini juga ditemukan di UTREEXO, sebuah struktur yang memungkinkan untuk memadatkan kumpulan node UTXO dan di MAST Taproot.
