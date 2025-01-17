---
term: OP_TUCK (0X7D)

---
Menyalin item di bagian atas tumpukan dan menyisipkannya di antara item kedua dan ketiga tumpukan. Misalnya, jika tumpukannya adalah:

```text
A
B
C
D
```

`OP_TUCK` akan menduplikasi item teratas `A` dan menempatkannya di posisi ketiga. Tumpukan yang dihasilkan adalah:

```text
A
B
A
C
D
```