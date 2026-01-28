---
term: OP_NUMEQUALVERIFY (0X9D)

definition: Menggabungkan OP_NUMEQUAL dan OP_VERIFY, gagal jika nilai numeriknya berbeda.
---
Gabungan antara operasi `OP_NUMEQUAL` dan `OP_VERIFY`. Operasi ini secara numerik membandingkan dua elemen paling atas pada _stack_. Jika nilainya sama, `OP_NUMEQUALVERIFY` akan menghapus hasil yang benar dari tumpukan dan melanjutkan eksekusi skrip. Jika nilainya tidak sama, hasilnya salah, dan eksekusi skrip langsung gagal.
