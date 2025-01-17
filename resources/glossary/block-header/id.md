---
term: HEADER BLOK

---
Header blok adalah sebuah struktur data yang berfungsi sebagai komponen utama dalam pembangunan blok Bitcoin. Setiap blok terdiri dari header dan daftar transaksi. Header blok berisi informasi penting yang memastikan integritas dan validitas sebuah blok di dalam blockchain. Header blok berisi 80 byte metadata dan terdiri dari elemen-elemen berikut:


- Versi blok;
- Hash dari blok sebelumnya;
- Akar pohon Merkle dari transaksi;
- Stempel waktu blok;
- Target kesulitan;
- The nonce.

Sebagai contoh, berikut ini adalah header dari blok nomor 785.530 dalam format heksadesimal, yang ditambang oleh Foundry USA pada tanggal 15 April 2023:

```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```

Jika kita memecah tajuk ini, kita bisa mengenali:


- Versi:

```text
00e0ff3f
```


- Hash sebelumnya:

```text
5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
```


- Akar Merkle:

```text
206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
```


- Cap waktu:

```text
bcb13a64
```


- Target:

```text
b2e00517
```


- The nonce:

```text
43f09a40
```

Agar valid, sebuah blok harus memiliki header yang, setelah di-hash dengan `SHA256d`, menghasilkan hash yang kurang dari atau sama dengan target tingkat kesulitan.

> ► *Dalam bahasa Inggris, ini disebut sebagai "Block Header" (tajuk blok)