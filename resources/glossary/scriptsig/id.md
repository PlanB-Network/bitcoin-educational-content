---
term: SCRIPTSIG

---
Sebuah elemen dalam transaksi Bitcoin yang terletak di input. `scriptSig` menyediakan data yang diperlukan untuk memenuhi kondisi yang ditetapkan oleh `scriptPubKey` dari transaksi sebelumnya dari mana dana dibelanjakan. Dengan demikian, ini memainkan peran pelengkap untuk `scriptPubKey`. Biasanya, `scriptSig` berisi tanda tangan digital dan kunci publik. Tanda tangan dibuat oleh pemilik bitcoin dengan menggunakan kunci pribadi mereka dan membuktikan bahwa mereka memiliki otorisasi untuk membelanjakan UTXO. Dalam kasus ini, `scriptSig` menunjukkan bahwa pemilik input memiliki private key yang sesuai dengan public key yang terkait dengan alamat yang ditentukan dalam `scriptPubKey` pada transaksi keluar sebelumnya.

Ketika transaksi diverifikasi, data dari `scriptSig` dieksekusi dalam `scriptPubKey` yang sesuai. Jika hasilnya valid, itu berarti kondisi untuk mengeluarkan dana telah terpenuhi. Jika semua input dari transaksi memberikan `scriptSig` yang memvalidasi `scriptPubKey`, transaksi tersebut valid dan dapat ditambahkan ke blok untuk dieksekusi.

Sebagai contoh, berikut ini adalah `scriptSig` P2PKH klasik:

```text
<signature> <public key>
```

`scriptPubKey` yang sesuai adalah:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```

![](../../dictionnaire/assets/35.webp)

> ► *`ScriptSig` terkadang juga disebut "skrip pembuka" dalam bahasa Inggris.*