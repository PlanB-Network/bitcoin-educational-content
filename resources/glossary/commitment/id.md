---
term: Commitment
---

Sebuah Commitment (dalam pengertian kriptografi) adalah sebuah objek matematis, dilambangkan dengan $C$, yang diturunkan secara deterministik dari sebuah operasi pada data terstruktur $m$ (pesan) dan sebuah nilai acak $r$. Kami menulis :


$$
C = \text{commit}(m, r)
$$


Mekanisme ini terdiri dari dua operasi utama:




- Commit: kita menerapkan fungsi kriptografi pada sebuah pesan $m$ dan sebuah pesan acak $r$ untuk menghasilkan $C$;
- Verifikasi: kita menggunakan $C$, pesan $m$ dan nilai $r$ untuk memeriksa apakah Commitment ini sudah benar. Fungsi ini mengembalikan `True` atau `False`.


Commitment harus menghormati dua properti:




- Pengikatan: tidak mungkin menemukan dua pesan berbeda yang menghasilkan $C$ yang sama:


$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$


Seperti :


$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$




- Menyembunyikan: pengetahuan tentang $C$ tidak boleh mengungkapkan isi dari $m$.


Dalam kasus protokol RGB, sebuah Commitment disertakan dalam transaksi Bitcoin untuk membuktikan keberadaan informasi tertentu pada waktu tertentu, tanpa mengungkapkan informasi itu sendiri.