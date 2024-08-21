---
term: HASH160
---

Fungsi kriptografi yang digunakan dalam Bitcoin, terutama untuk menghasilkan alamat penerima Legacy dan SegWit v0. Ini menggabungkan dua fungsi hash yang dieksekusi secara berurutan pada input: pertama SHA256, kemudian RIPEMD160. Output dari fungsi ini adalah 160 bit.

$$\text{HASH160}(x) = \text{RIPEMD160}(\text{SHA256}(x))$$