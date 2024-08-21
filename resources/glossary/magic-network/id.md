---
term: MAGIC NETWORK
---

Konstanta yang digunakan dalam protokol Bitcoin untuk mengidentifikasi jaringan spesifik (mainnet, testnet, regtest...) dari sebuah pesan yang ditukarkan antar node. Nilai-nilai ini dicantumkan di awal setiap pesan untuk memudahkan identifikasi mereka dalam aliran data. Magic Networks dirancang agar jarang hadir dalam data komunikasi biasa. Memang, 4 byte ini jarang terjadi dalam ASCII, tidak valid dalam UTF-8, dan menghasilkan integer 32-bit yang sangat besar, terlepas dari format penyimpanan data. Magic Networks adalah (dalam format little-endian):
* Mainnet:

```text
f9beb4d9
```

* Testnet:

```text
0b110907
```

* Regtest:

```text
fabfb5da
```

> ► *4 byte ini terkadang juga disebut "Magic Number," "Magic Bytes," atau "Start String."*