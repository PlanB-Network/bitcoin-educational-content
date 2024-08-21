---
term: MERKLE ROOT
---

Digest atau "hash puncak" dari sebuah pohon Merkle, yang mewakili ringkasan dari semua informasi yang ada dalam pohon tersebut. Pohon Merkle adalah struktur akumulator kriptografi, yang terkadang juga disebut sebagai "pohon hash". Dalam konteks Bitcoin, pohon Merkle digunakan untuk mengorganisir transaksi dalam sebuah blok dan untuk memfasilitasi verifikasi cepat inklusi transaksi tertentu. Dengan demikian, dalam blok Bitcoin, Merkle root diperoleh dengan secara berurutan meng-hash transaksi dalam pasangan sampai hanya satu hash yang tersisa (Merkle root). Ini kemudian dimasukkan dalam header dari blok yang bersangkutan. Pohon hash ini juga ditemukan dalam UTREEXO, sebuah struktur yang memungkinkan kondensasi set UTXO dari node, dan dalam MAST Taproot.