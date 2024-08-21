---
term: SECP256R1
---

Nama yang diberikan kepada kurva elips yang didefinisikan oleh standar NIST untuk kriptografi kunci publik. Ini menggunakan lapangan prima 256 bit dan persamaan kurva elips $y^2 = x^3 + ax + b$ dengan konstanta:

```text
a = -3
```

dan

```text
b = 410583637251521421293261297800472684091144410159937255548542755610749322
77127
```

Kurva `secp256r1` banyak digunakan dalam berbagai protokol, namun tidak digunakan dalam Bitcoin. Memang, Satoshi Nakamoto memilih kurva `secp256k1`, yang saat itu masih kurang dikenal pada tahun 2009. Alasan pasti dari pilihan ini tidak diketahui, namun mungkin untuk meminimalkan risiko backdoor. Parameter dari kurva $k1$ memang jauh lebih sederhana dibandingkan dengan kurva $r1$, terutama konstanta $b$.

> ► *Kurva ini terkadang juga dinamakan "P-256".*