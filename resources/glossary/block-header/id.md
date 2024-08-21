---
term: BLOCK HEADER
---

Block header adalah struktur data yang berfungsi sebagai komponen utama dalam pembangunan sebuah blok Bitcoin. Setiap blok terdiri dari sebuah header dan daftar transaksi. Block header mengandung informasi penting yang menjamin integritas dan validitas sebuah blok dalam blockchain. Block header berisi 80 byte metadata dan terdiri dari elemen-elemen berikut:
* Versi blok;
* Hash dari blok sebelumnya;
* Akar pohon Merkle dari transaksi;
* Timestamp blok;
* Target kesulitan;
* Nonce.

Sebagai contoh, berikut adalah header dari blok nomor 785,530 dalam format heksadesimal, yang ditambang oleh Foundry USA pada 15 April 2023:

```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```

Jika kita memecah header ini, kita dapat mengenali:
* Versinya:

```text
00e0ff3f
```

* Hash sebelumnya:

```text
5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
```

* Akar Merkle:

```text
206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
```

* Timestamp:

```text
bcb13a64
```

* Target:

```text
b2e00517
```

* Nonce:

```text
43f09a40
```

Untuk valid, sebuah blok harus memiliki header yang, setelah di-hash dengan `SHA256d`, menghasilkan hash yang kurang dari atau sama dengan target kesulitan.

> ► *Dalam bahasa Inggris, ini disebut sebagai "Block Header".*