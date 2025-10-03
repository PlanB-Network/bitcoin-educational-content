---
term: PEDERSEN COMMITMENT
---

Sebuah _Pedersen Commitment_ adalah sebuah jenis kriptografi _Commitment_ dengan sifat homomorfis terhadap operasi penjumlahan. Ini berarti bahwa dimungkinkan untuk memvalidasi jumlah dari dua komitmen tanpa mengungkapkan nilai-nilai individualnya.


Secara formal, jika :


$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$


kemudian:


$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$


Properti ini menjadi berguna, contohnya, untuk menyembunyikan jumlah token yang dipertukarkan dalam sistem mata uang digital, seperti RGB, namun totalnya tetap dapat diverifikasi.
