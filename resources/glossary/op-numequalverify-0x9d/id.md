---
term: OP_NUMEQUALVERIFY (0X9D)

---
Menggabungkan operasi `OP_NUMEQUAL` dan `OP_VERIFY`. Operasi ini secara numerik membandingkan dua elemen paling atas pada tumpukan. Jika nilainya sama, `OP_NUMEQUALVERIFY` akan menghapus hasil yang benar dari tumpukan dan melanjutkan eksekusi skrip. Jika nilainya tidak sama, hasilnya salah, dan skrip langsung gagal.