---
term: MAGIC NETWORK

---
Konstanta yang digunakan dalam protokol Bitcoin untuk mengidentifikasi jaringan tertentu (mainnet, testnet, regtest...) dari sebuah pesan yang dipertukarkan antar node. Nilai-nilai ini dituliskan pada awal setiap pesan untuk memudahkan identifikasi mereka dalam aliran data. _Magic Network_ dirancang untuk jarang hadir dalam data komunikasi biasa. Informasi 4 byte ini jarang ditemukan dalam ASCII, tidak valid dalam UTF-8, dan menghasilkan bilangan bulat 32-bit yang sangat besar, apa pun format penyimpanan datanya. _Magic Network_ (dalam format _little-endian_):


- Mainnet:

```text
f9beb4d9
```


- Testnet:

```text
0b110907
```


- Regtest:

```text
fabfb5da
```

> ► *Keempat byte ini kadang-kadang juga disebut "Angka Ajaib," "Byte Ajaib," atau "String Awal."*
