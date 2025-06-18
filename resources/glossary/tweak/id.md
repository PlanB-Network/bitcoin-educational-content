---
term: TWEAK
---

Dalam kriptografi, untuk "mengubah" kunci publik adalah dengan memodifikasinya menggunakan nilai tambahan yang disebut "tweak", sehingga kunci tersebut tetap dapat digunakan dengan pengetahuan tentang kunci privat asli dan tweak. Secara teknis, tweak adalah sebuah nilai skalar yang ditambahkan ke dalam kunci publik yang asli. Jika $P$ adalah kunci publik dan $t$ adalah tweak, maka kunci publik yang di-tweak menjadi :


$$
P' = P + tG
$$


Di mana $G$ adalah generator dari kurva elips yang digunakan. Operasi ini menghasilkan kunci publik baru yang berasal dari kunci asli, dengan tetap mempertahankan sifat kriptografi tertentu yang memungkinkan untuk digunakan. Sebagai contoh, metode ini digunakan untuk alamat Taproot (P2TR), untuk memungkinkan penggunaan baik dengan memberikan tanda tangan Schnorr dengan cara tradisional, atau dengan memenuhi salah satu kondisi yang ditetapkan dalam Merkle Tree, yang juga dikenal sebagai "MAST".