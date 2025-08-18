---
term: OP_TUCK (0X7D)

---
Menyalin item di bagian atas stack dan menyisipkannya di antara item kedua dan ketiga teratas _stack_. Misalnya, jika _stack_ awalnya sebagai berikut:

```text
A
B
C
D
```

`OP_TUCK` akan menduplikasi item teratas `A` dan menempatkannya di posisi ketiga. _Stack_ yang dihasilkan adalah:

```text
A
B
A
C
D
```
