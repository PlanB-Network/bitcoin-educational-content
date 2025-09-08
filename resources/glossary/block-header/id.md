---
term: HEADER BLOK

---
_Header_ blok adalah sebuah struktur data yang berfungsi sebagai komponen utama dalam pembangunan blok Bitcoin. Setiap blok terdiri dari header dan daftar transaksi. Header blok berisi informasi penting yang memastikan integritas dan validitas sebuah blok di dalam _blockchain_. _Header_ blok berisi 80 byte metadata dan terdiri dari elemen-elemen berikut:


- Versi blok;
- _Hash_ dari blok sebelumnya;
- Akar pohon Merkle dari transaksi;
- Stempel waktu blok;
- Target kesulitan;
- Nilai _nonce_.

Sebagai contoh, berikut ini adalah _header_ dari blok nomor 785.530 dalam format heksadesimal, yang ditambang oleh Foundry USA pada tanggal 15 April 2023:

```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```

Jika kita memecah _header_ ini, kita bisa mendapatkan:


- Versi:

```text
00e0ff3f
```


- _Hash_ blok sebelumnya:

```text
5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
```


- Akar Merkle:

```text
206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
```


- Stempel waktu:

```text
bcb13a64
```


- Target kesulitan:

```text
b2e00517
```


- Nilai _nonce_:

```text
43f09a40
```

Agar valid, sebuah blok harus memiliki _header_ yang setelah di-hash dengan `SHA256d`, menghasilkan _hash_ yang hasilnya kurang dari atau sama dengan target tingkat kesulitan.

> ► *Dalam bahasa Inggris, ini disebut sebagai "Block Header"*
