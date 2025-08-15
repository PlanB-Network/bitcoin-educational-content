---
term: POLICY (MINISCRIPT)

---
Bahasa tingkat tinggi yang berorientasi pada pengguna yang memungkinkan spesifikasi sederhana dari kondisi di mana UTXO dapat dibuka dalam kerangka kerja _Miniscript_. Kebijakan adalah deskripsi abstrak dari aturan pengeluaran. Kemudian dapat dikompilasi ke dalam _miniscript_, yang merupakan ekuivalen satu-ke-satu dengan operasi dari bahasa skrip asli Bitcoin.

![](../../dictionnaire/assets/30.webp)

Bahasa _Policy_ sedikit berbeda dengan bahasa _miniscript_. Sebagai contoh, bayangkan sebuah sistem keamanan dengan jalur utama adalah kunci A, dan jalur pemulihan adalah kunci B, tetapi di bawah penguncian waktu selama satu tahun (sekitar 52.560 blok). Dalam kebijakan, ini akan menjadi:

```plaintext
or(pk(A),and(pk(B),older(52560)))
```

Setelah digabungkan ke dalam _miniscript_, maka akan menjadi:

```plaintext
andor(pk(B),older(52560),pk(A))
```

Dan setelah dikonversi ke dalam skrip asli, maka akan menjadi seperti di bawah:

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
