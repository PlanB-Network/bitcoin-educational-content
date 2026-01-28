---
term: HASH256

definition: Fungsi yang menerapkan SHA256 dua kali berturut-turut, digunakan dalam berbagai aplikasi Bitcoin.
---
Fungsi kriptografi yang digunakan untuk berbagai aplikasi pada Bitcoin, yang melibatkan penerapan fungsi SHA256 dua kali pada data input. Pesan dilewatkan melalui SHA256 satu kali, dan _hash_ dari operasi ini digunakan sebagai input untuk melewati SHA256 yang kedua. Oleh karena itu, output dari fungsi ini berukuran 256 bit.

$$\text{HASH256}(x) = \text{SHA256}(\text{SHA256}(x))$$
