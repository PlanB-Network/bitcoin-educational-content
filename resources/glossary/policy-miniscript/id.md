---
term: KEBIJAKAN (NASKAH MINI)

---
Bahasa tingkat tinggi yang berorientasi pada pengguna yang memungkinkan spesifikasi sederhana dari kondisi di mana UTXO dapat dibuka dalam kerangka kerja Miniscript. Kebijakan adalah deskripsi abstrak dari aturan pengeluaran. Kemudian dapat dikompilasi ke dalam miniscript, yang merupakan ekuivalen satu-ke-satu dengan operasi dari bahasa skrip asli Bitcoin.

![](../../dictionnaire/assets/30.webp)

Bahasa kebijakan sedikit berbeda dengan bahasa miniscript. Sebagai contoh, bayangkan sebuah sistem keamanan dengan jalur utama adalah kunci A, dan jalur pemulihan adalah kunci B, tetapi di bawah penguncian waktu selama satu tahun (sekitar 52.560 blok). Dalam kebijakan, ini akan menjadi:

```plaintext
or(pk(A),and(pk(B),older(52560)))
```

Setelah dikompilasi ke dalam miniscript, maka akan menjadi:

```plaintext
andor(pk(B),older(52560),pk(A))
```

Dan setelah dikonversi ke dalam skrip asli, maka akan menjadi seperti itu:

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