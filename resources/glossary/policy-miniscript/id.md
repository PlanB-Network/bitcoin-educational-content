---
term: POLICY (MINISCRIPT)
---

POLICY (MINISCRIPT) adalah bahasa tingkat tinggi yang berorientasi pada pengguna yang memungkinkan spesifikasi sederhana dari kondisi di mana sebuah UTXO dapat dibuka dalam kerangka kerja Miniscript. Policy adalah deskripsi abstrak dari aturan pengeluaran. Kemudian, policy dapat dikompilasi menjadi miniscript, yang merupakan ekivalen satu-ke-satu dengan operasi dari bahasa skrip asli Bitcoin.

![](../../dictionnaire/assets/30.png)

Bahasa policy sedikit berbeda dari bahasa miniscript. Sebagai contoh, bayangkan sistem keamanan dengan jalur utama adalah kunci A, dan jalur pemulihan adalah kunci B, tetapi di bawah timelock selama satu tahun (sekitar 52,560 blok). Dalam policy, ini akan ditulis sebagai:

```plaintext
or(pk(A),and(pk(B),older(52560)))
```

Setelah dikompilasi menjadi miniscript, akan menjadi:

```plaintext
andor(pk(B),older(52560),pk(A))
```

Dan setelah dikonversi menjadi skrip asli, akan menjadi:

```plaintext
<B>
OP_CHECKSIG
OP_NOTIF
<A>
OP_CHECKSIG
OP_ELSE
<50cd00>
OP_CHECKSEQUENCEVERIFY
OP_ENDIF
```