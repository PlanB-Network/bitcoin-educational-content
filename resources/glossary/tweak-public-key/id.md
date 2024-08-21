---
term: TWEAK (PUBLIC KEY)
---

Dalam bidang kriptografi, "tweaking" sebuah kunci publik melibatkan modifikasi kunci ini dengan menggunakan nilai tambahan yang disebut "tweak" sehingga tetap dapat digunakan dengan pengetahuan tentang kunci privat asli dan tweak tersebut. Secara teknis, tweak adalah nilai skalar yang ditambahkan ke kunci publik awal. Jika $P$ adalah kunci publik dan $t$ adalah tweak, maka kunci publik yang telah di-tweak menjadi:

$$
P' = P + tG
$$

Dimana $G$ adalah generator dari kurva eliptik yang digunakan. Operasi ini memungkinkan untuk mendapatkan kunci publik baru yang berasal dari kunci asli sambil mempertahankan sifat kriptografis tertentu yang membuatnya dapat digunakan. Sebagai contoh, metode ini digunakan untuk alamat Taproot (P2TR) untuk memungkinkan pengeluaran baik dengan menyajikan tanda tangan Schnorr secara tradisional atau dengan memenuhi salah satu kondisi yang dinyatakan dalam pohon Merkle, yang juga disebut "MAST".

![](../../dictionnaire/assets/26.png)