---
term: DER
---

Singkatan dari *Distinguished Encoding Rules*. DER merupakan bagian yang ketat dari aturan penyandian ASN.1 yang didefinisikan dalam spesifikasi [ITU-T X.690, 2002.] (https://www.itu.int/ITU-T/studygroups/com17/languages/X.690-0207.pdf) dan digunakan untuk menyandikan semua jenis data dalam urutan biner. DER terutama digunakan dalam bidang tertentu, seperti kriptografi, di mana data harus dikodekan dengan cara yang standar dan dapat diprediksi.


Pada Bitcoin, tanda tangan ECDSA dikodekan dalam format DER. Tanda tangan ini terdiri dari dua angka yang dikodekan 32 byte (`r`, `s`). Format tanda tangan terdiri dari _Elements_ (71 byte) berikut ini:


```text
0x30 | length |  0x02 | r-length | r | 0x02 | s-length | s
```


Dengan:


- `0x30` (1 byte): pengidentifikasi struktur komponen;
- `length` (1 byte): panjang data berikutnya;
- `0x02` (1 byte): tipe pengenal data `INTEGER` (bilangan bulat);
- `r-length` (1 byte): panjang nilai `r` berikutnya (32 byte);
- `r` (32 byte): nilai `r` sebagai bilangan bulat besar;
- `0x02` (1 byte): tipe pengenal data `INTEGER` (bilangan bulat);
- `s-length` (1 byte): panjang nilai `s` berikutnya (32 byte) ;
- `s` (32 byte): nilai `s` sebagai bilangan bulat _big-endian_.


Dalam transaksi Bitcoin, sebuah byte ditambahkan pada akhir tanda tangan DER untuk menunjukkan jenis SigHash yang digunakan.
