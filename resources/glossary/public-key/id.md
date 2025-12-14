---
term: KUNCI PUBLIK

---
Kunci publik adalah sebuah elemen yang digunakan dalam kriptografi asimetris. Kunci publik dihasilkan dari kunci privat menggunakan fungsi matematika yang tidak dapat diubah. Pada Bitcoin, kunci publik berasal dari kunci privat yang terkait melalui algoritma tanda tangan digital kurva elips ECDSA atau protokol Schnorr. Tidak seperti kunci privat, kunci publik dapat dibagikan secara bebas tanpa mengorbankan keamanan dana. Dalam protokol Bitcoin, kunci publik berfungsi sebagai dasar untuk membuat alamat Bitcoin, yang kemudian digunakan untuk membuat kondisi pembelanjaan pada UTXO dengan menggunakan `scriptPubKey`. Kunci publik sering kali disalahartikan sebagai kunci utama atau _extended key_ (xpub...). Pada kenyataannya, elemen-elemen ini sangat berbeda.

> ► *Dalam bahasa Inggris, kunci publik disebut "public key" Istilah ini terkadang disingkat menjadi "pubkey," atau "PK. "*
