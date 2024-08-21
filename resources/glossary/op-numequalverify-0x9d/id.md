---
term: OP_NUMEQUALVERIFY (0X9D)
---

Menggabungkan operasi `OP_NUMEQUAL` dan `OP_VERIFY`. Secara numerik membandingkan dua elemen paling atas pada stack. Jika nilai-nilainya sama, `OP_NUMEQUALVERIFY` menghapus hasil benar dari stack dan melanjutkan eksekusi skrip. Jika nilai-nilainya tidak sama, hasilnya adalah salah, dan skrip langsung gagal.