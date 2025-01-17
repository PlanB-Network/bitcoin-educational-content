---
term: TWEAK (KUNCI PUBLIK)

---
Dalam bidang kriptografi, "tweak" kunci publik melibatkan modifikasi kunci ini dengan menggunakan nilai tambahan yang disebut "tweak" sehingga tetap dapat digunakan dengan pengetahuan kunci pribadi asli dan tweak. Secara teknis, tweak adalah sebuah nilai skalar yang ditambahkan ke kunci publik awal. Jika $P$ adalah kunci publik dan $t$ adalah tweak, maka kunci publik yang telah diubah menjadi:

$$
P' = P + tG
$$

Di mana $G$ adalah generator dari kurva elips yang digunakan. Operasi ini memungkinkan untuk mendapatkan kunci publik baru yang berasal dari kunci asli dengan tetap mempertahankan sifat kriptografi tertentu yang membuatnya dapat digunakan. Sebagai contoh, metode ini digunakan untuk alamat Taproot (P2TR) untuk mengizinkan penggunaan baik dengan memberikan tanda tangan Schnorr dengan cara tradisional atau dengan memenuhi salah satu kondisi yang dinyatakan dalam pohon Merkle, yang juga disebut "MAST".

![](../../dictionnaire/assets/26.webp)