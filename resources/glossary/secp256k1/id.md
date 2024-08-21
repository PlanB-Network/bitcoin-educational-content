---
term: SECP256K1
---

Nama yang diberikan kepada kurva eliptik spesifik yang digunakan dalam protokol Bitcoin untuk implementasi algoritma tanda tangan digital ECDSA (*Elliptic Curve Digital Signature Algorithm*) dan Schnorr. Kurva `secp256k1` dipilih oleh penemu Bitcoin, Satoshi Nakamoto. Kurva ini memiliki beberapa properti menarik, terutama manfaat kinerja.

Penggunaan `secp256k1` dalam Bitcoin berarti bahwa setiap kunci privat (angka acak 256-bit) dipetakan ke kunci publik yang sesuai melalui penambahan dan penggandaan titik kunci privat oleh titik generator kurva `secp256k1`. Operasi ini mudah dilakukan dalam satu arah tetapi praktis mustahil untuk dibalik, yang menjadi dasar keamanan tanda tangan digital pada Bitcoin.

Kurva `secp256k1` ditentukan oleh persamaan kurva eliptik $y^2 = x^3 + 7$, yang berarti memiliki koefisien $a$ sama dengan $0$ dan $b$ sama dengan $7$ dalam bentuk umum dari persamaan kurva eliptik $y^2 = x^3 + ax + b$. `secp256k1` didefinisikan di atas lapangan hingga yang urutannya adalah bilangan prima sangat besar, khususnya $p = 2^{256} - 2^{32} - 977$. Kurva ini juga memiliki urutan grup, yang merupakan jumlah titik berbeda pada kurva, titik generator yang telah ditentukan sebelumnya (atau titik $G$), yang digunakan dalam operasi kriptografi untuk menghasilkan pasangan kunci, dan koefaktor sama dengan $1$.

> ► *“SEC” berarti “Standards for Efficient Cryptography”. “P256” menunjukkan bahwa kurva didefinisikan di atas lapangan $\mathbb{Z}_p$ di mana $p$ adalah bilangan prima 256-bit. “K” merujuk pada nama penemunya, Neal Koblitz. Akhirnya, “1” menunjukkan bahwa ini adalah versi pertama dari kurva ini.*