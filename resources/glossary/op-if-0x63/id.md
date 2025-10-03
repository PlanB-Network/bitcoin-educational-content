---
term: OP_IF (0X63)

---
Mengeksekusi bagian skrip berikut ini jika nilai di bagian atas _stack_ bukan nol (benar). Jika nilainya nol (salah), operasi ini akan dilewati, dan langsung berpindah ke operasi setelah `OP_ELSE`, jika ada. `OP_IF` memungkinkan peluncuran struktur kontrol bersyarat dalam skrip. Struktur ini menentukan aliran kontrol dalam skrip berdasarkan kondisi yang diberikan pada saat eksekusi transaksi. `OP_IF` digunakan dengan `OP_ELSE` dan `OP_ENDIF` dengan cara berikut:

```text
<kondisi>
OP_IF
<operasi bila kondisi terpenuhi>
OP_ELSE
<operasi bila kondisi tidak terpenuhi>
OP_ENDIF
```
