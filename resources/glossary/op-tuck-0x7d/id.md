---
term: OP_TUCK (0X7D)
---

Menyalin item di puncak tumpukan dan memasukkannya di antara item kedua dan ketiga dari tumpukan. Sebagai contoh, jika tumpukan adalah:

```text
A
B
C
D
```

`OP_TUCK` akan menduplikasi item paling atas `A` dan menempatkannya di posisi ketiga. Tumpukan yang dihasilkan akan menjadi:

```text
A
B
A
C
D
```