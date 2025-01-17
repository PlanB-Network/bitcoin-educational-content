---
term: HASH160

---
Fungsi kriptografi yang digunakan dalam Bitcoin, terutama untuk menghasilkan alamat penerima Legacy dan SegWit v0. Fungsi ini menggabungkan dua fungsi hash yang dieksekusi secara berurutan pada input: pertama SHA256, kemudian RIPEMD160. Oleh karena itu, output dari fungsi ini adalah 160 bit.

$$\text{HASH160}(x) = \text{RIPEMD160}(\text{SHA256}(x))$$