---
term: SCRIPTSIG
---

Sebuah elemen dalam transaksi Bitcoin yang terletak pada input. `scriptSig` menyediakan data yang diperlukan untuk memenuhi kondisi yang ditetapkan oleh `scriptPubKey` dari transaksi sebelumnya dari mana dana tersebut dihabiskan. Dengan demikian, ia memainkan peran pelengkap terhadap `scriptPubKey`. Biasanya, `scriptSig` berisi tanda tangan digital dan kunci publik. Tanda tangan dihasilkan oleh pemilik bitcoin menggunakan kunci privat mereka dan membuktikan bahwa mereka memiliki otorisasi untuk menghabiskan UTXO. Dalam kasus ini, `scriptSig` menunjukkan bahwa pemegang input memiliki kunci privat yang sesuai dengan kunci publik yang terkait dengan alamat yang ditentukan dalam `scriptPubKey` dari transaksi keluar sebelumnya.

Ketika transaksi diverifikasi, data dari `scriptSig` dieksekusi dalam `scriptPubKey` yang sesuai. Jika hasilnya valid, itu berarti kondisi untuk menghabiskan dana telah terpenuhi. Jika semua input dari transaksi menyediakan `scriptSig` yang memvalidasi `scriptPubKey` mereka, transaksi tersebut valid dan dapat ditambahkan ke blok untuk dieksekusi.

Sebagai contoh, berikut ini adalah `scriptSig` P2PKH klasik:

```text
<tanda tangan> <kunci publik>
```

`scriptPubKey` yang sesuai akan menjadi:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <alamat> OP_EQUALVERIFY OP_CHECKSIG
```

![](../../dictionnaire/assets/35.png)

> ► *`scriptSig` juga terkadang disebut sebagai "skrip pembuka" dalam bahasa Inggris.*