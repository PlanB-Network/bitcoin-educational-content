---
term: OP_IF (0X63)

---
Mengeksekusi bagian skrip berikut ini jika nilai di bagian atas tumpukan bukan nol (benar). Jika nilainya nol (salah), operasi ini dilewati, dan langsung berpindah ke operasi setelah `OP_ELSE`, jika ada. `OP_IF` memungkinkan peluncuran struktur kontrol bersyarat dalam skrip. Struktur ini menentukan aliran kontrol dalam skrip berdasarkan kondisi yang diberikan pada saat eksekusi transaksi. `OP_IF` digunakan dengan `OP_ELSE` dan `OP_ENDIF` dengan cara berikut:

```text
<condition>
OP_IF
<operations if the condition is true>
OP_ELSE
<operations if the condition is false>
OP_ENDIF
```