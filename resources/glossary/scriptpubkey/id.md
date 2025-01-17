---
term: SCRIPTPUBKEY

---
Skrip yang terletak di bagian output dari transaksi Bitcoin yang mendefinisikan kondisi di mana UTXO terkait dapat dibelanjakan. Dengan demikian, skrip ini mengamankan bitcoin. Dalam bentuk yang paling umum, `scriptPubKey` berisi sebuah kondisi yang mengharuskan transaksi berikutnya untuk memberikan bukti kepemilikan private key yang sesuai dengan alamat Bitcoin yang ditentukan. Hal ini sering kali dicapai dengan sebuah skrip yang meminta tanda tangan yang sesuai dengan kunci publik yang terkait dengan alamat yang digunakan untuk mengamankan dana tersebut. Ketika sebuah transaksi mencoba untuk menggunakan UTXO ini sebagai input, transaksi tersebut harus menyediakan `scriptSig` yang, setelah digabungkan dengan `scriptPubKey`, memenuhi kondisi yang ditetapkan dan menghasilkan sebuah skrip yang valid.

Sebagai contoh, berikut ini adalah `scriptPubKey` P2PKH klasik:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```

`scriptSig` yang sesuai adalah:

```text
<signature> <public key>
```

![](../../dictionnaire/assets/35.webp)

> ► *Skrip ini juga terkadang disebut sebagai "skrip pengunci" dalam bahasa Inggris.*