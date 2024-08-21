---
term: KUNCI PUBLIK
---

Kunci publik adalah elemen yang digunakan dalam kriptografi asimetris. Kunci ini dihasilkan dari kunci privat menggunakan fungsi matematika yang tidak dapat dibalik. Pada Bitcoin, kunci publik diturunkan dari kunci privat yang terkait melalui algoritma tanda tangan digital dari kurva eliptik ECDSA atau Schnorr. Berbeda dengan kunci privat, kunci publik dapat dibagikan secara bebas tanpa mengompromikan keamanan dana. Dalam protokol Bitcoin, kunci publik berfungsi sebagai dasar untuk membuat alamat Bitcoin, yang kemudian digunakan untuk membuat kondisi pengeluaran pada UTXO menggunakan `scriptPubKey`. Kunci publik sering kali disalahartikan dengan kunci induk atau dengan kunci ekstensi (xpub...). Namun, elemen-elemen ini sangat berbeda.

> ► *Dalam bahasa Inggris, kunci publik disebut "public key." Istilah ini terkadang disingkat sebagai "pubkey," atau "PK."*