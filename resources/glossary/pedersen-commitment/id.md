---
term: Pedersen commitment
---

Sebuah Pedersen commitment adalah sebuah jenis kriptografi Commitment dengan sifat homomorfis terhadap operasi penjumlahan. Ini berarti bahwa dimungkinkan untuk memvalidasi jumlah dari dua komitmen tanpa mengungkapkan nilai individual.


Secara formal, jika :


$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$


kemudian:


$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$


Properti ini menjadi berguna, contohnya, untuk menyembunyikan jumlah token yang dipertukarkan dalam sistem mata uang digital, seperti RGB, namun tetap dapat memverifikasi totalnya.