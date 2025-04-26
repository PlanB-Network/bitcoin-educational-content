---
term: SECP256R1

---
Nama yang diberikan kepada kurva elips yang didefinisikan oleh standar NIST untuk kriptografi kunci publik. Kurva ini menggunakan bidang prima 256 bit dan persamaan kurva elips $y^2 = x^3 + ax + b$ dengan konstanta:

```text
a = -3
```

dan

```text
b = 410583637251521421293261297800472684091144410159937255548542755610749322
77127
```

Kurva `secp256r1` digunakan secara luas dalam banyak protokol, tetapi tidak digunakan dalam Bitcoin. Memang, Satoshi Nakamoto memilih kurva `secp256k1`, yang saat itu tidak terlalu dikenal pada tahun 2009. Alasan yang tepat untuk pilihan ini tidak diketahui, tetapi mungkin saja untuk meminimalisir risiko pintu belakang. Parameter kurva $k1$ memang jauh lebih sederhana daripada kurva $r1$, terutama konstanta $b$.

> ► *Kurva ini kadang-kadang juga dinamai "P-256".*