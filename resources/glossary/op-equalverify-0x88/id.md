---
term: OP_EQUALVERIFY (0X88)
---

Menggabungkan fungsi dari `OP_EQUAL` dan `OP_VERIFY`. Pertama, memeriksa kesamaan dari dua nilai teratas pada stack, kemudian memastikan bahwa hasilnya bukan nol, jika tidak, transaksi tersebut tidak valid. `OP_EQUALVERIFY` secara khusus digunakan dalam skrip verifikasi alamat.