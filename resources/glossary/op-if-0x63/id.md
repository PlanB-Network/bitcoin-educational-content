---
term: OP_IF (0X63)
---

Menjalankan bagian skrip berikutnya jika nilai di puncak tumpukan adalah non-nol (benar). Jika nilai tersebut nol (salah), operasi ini akan dilewati, langsung menuju ke operasi setelah `OP_ELSE`, jika ada. `OP_IF` memungkinkan peluncuran struktur kontrol kondisional dalam sebuah skrip. Ini menentukan alur kontrol dalam skrip berdasarkan kondisi yang diberikan pada saat eksekusi transaksi. `OP_IF` digunakan bersama dengan `OP_ELSE` dan `OP_ENDIF` dengan cara berikut:

```text
<kondisi>
OP_IF
<operasi jika kondisi benar>
OP_ELSE
<operasi jika kondisi salah>
OP_ENDIF
```