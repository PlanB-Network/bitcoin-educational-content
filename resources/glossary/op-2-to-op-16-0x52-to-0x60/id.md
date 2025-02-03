---
term: OP_2 HINGGA OP_16 (0X52 HINGGA 0X60)

---
Opcode dari `OP_2` hingga `OP_16` mendorong nilai numerik masing-masing 2 hingga 16 ke dalam stack. Opcode ini digunakan untuk menyederhanakan skrip dengan mengizinkan penyisipan nilai numerik yang kecil. Jenis opcode ini terutama digunakan dalam skrip multisignature. Berikut ini adalah contoh `scriptPubKey` untuk multisig 2/3:

```text
OP_2
<Public Key A>
<Public Key B>
<Public Key C>
OP_3
OP_CHECKMULTISIG
```

> ► *Semua opcode ini terkadang juga disebut OP_PUSHNUM_N.*