---
term: SECP256K1

---
Nama yang diberikan kepada kurva elips tertentu yang digunakan dalam protokol Bitcoin untuk implementasi ECDSA (*Eliptic Curve Digital Signature Algorithm*) dan algoritma tanda tangan digital Schnorr. Kurva `secp256k1` dipilih oleh penemu Bitcoin, Satoshi Nakamoto. Kurva ini memiliki beberapa sifat yang menarik, terutama dalam aspek manfaat kinerja.

Penggunaan `secp256k1` dalam Bitcoin berarti bahwa setiap kunci privat (sebuah angka acak 256-bit) dipetakan ke kunci publik yang sesuai melalui penambahan dan penggandaan titik kunci privat dengan titik generator kurva `secp256k1`. Operasi ini mudah dilakukan dalam satu arah tetapi secara praktis tidak mungkin untuk dibalik, yang menjadi dasar keamanan tanda tangan digital pada Bitcoin.

Kurva `secp256k1` ditentukan oleh persamaan kurva elips $y^2 = x^3 + 7$, yang berarti kurva ini memiliki koefisien $a$ sama dengan $0$ dan $b$ sama dengan $7$ dalam bentuk umum persamaan kurva elips $y^2 = x^3 + ax + b$. `secp256k1` didefinisikan pada bidang terbatas yang urutannya merupakan bilangan prima yang sangat besar, khususnya $p = 2^{256} - 2^{32} - 977$. Kurva ini juga memiliki sebuah urutan grup, yang merupakan jumlah titik yang berbeda pada kurva, sebuah titik generator yang sudah ditentukan sebelumnya (atau titik $G$), yang digunakan pada operasi kriptografi untuk menghasilkan pasangan kunci, dan sebuah kofaktor yang sama dengan $$.

> ► *"SEC" adalah singkatan dari "Standards for Efficient Cryptography". "P256" menunjukkan bahwa kurva tersebut didefinisikan pada bidang $\mathbb{Z}_p$ di mana $p$ adalah bilangan prima 256-bit. "K" merujuk pada nama penemunya, Neal Koblitz. Terakhir, "1" menunjukkan bahwa ini adalah versi pertama dari kurva ini.*
