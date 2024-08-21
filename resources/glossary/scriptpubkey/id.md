---
term: SCRIPTPUBKEY
---

Sebuah skrip yang terletak di bagian output dari sebuah transaksi Bitcoin yang mendefinisikan kondisi di mana UTXO terkait dapat digunakan. Skrip ini dengan demikian mengamankan bitcoin. Dalam bentuk yang paling umum, `scriptPubKey` berisi sebuah kondisi yang memerlukan transaksi berikutnya untuk memberikan bukti kepemilikan kunci privat yang sesuai dengan alamat Bitcoin yang ditentukan. Ini seringkali dicapai melalui skrip yang menuntut tanda tangan yang sesuai dengan kunci publik yang terkait dengan alamat yang digunakan untuk mengamankan dana ini. Ketika sebuah transaksi mencoba menggunakan UTXO ini sebagai input, ia harus menyediakan `scriptSig` yang, setelah digabungkan dengan `scriptPubKey`, memenuhi kondisi yang ditetapkan dan menghasilkan skrip yang valid.

Sebagai contoh, berikut ini adalah `scriptPubKey` P2PKH klasik:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <alamat> OP_EQUALVERIFY OP_CHECKSIG
```

`scriptSig` yang sesuai akan berupa:

```text
<tanda tangan> <kunci publik>
```

![](../../dictionnaire/assets/35.png)

> ► *Skrip ini juga terkadang disebut sebagai "locking script" dalam bahasa Inggris.*