---
term: OP_2 TO OP_16 (0X52 TO 0X60)
---

Opcodes dari `OP_2` sampai `OP_16` mendorong nilai numerik yang sesuai dari 2 sampai 16 ke dalam stack. Opcodes ini digunakan untuk menyederhanakan skrip dengan memungkinkan penyisipan nilai numerik kecil. Jenis opcode ini terutama digunakan dalam skrip multisignature. Berikut adalah contoh dari `scriptPubKey` untuk multisig 2/3:

```text
OP_2
<Public Key A>
<Public Key B>
<Public Key C>
OP_3
OP_CHECKMULTISIG
```

> ► *Semua opcode ini terkadang juga disebut OP_PUSHNUM_N.*