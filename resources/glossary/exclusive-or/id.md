---
istilah: EXCLUSIVE OR
---

Sebuah fungsi dasar dari logika Boolean. "Exclusive Or" atau XOR ("*Exclusive or*") mengambil dua operan Boolean, masing-masing bernilai benar atau salah, dan menghasilkan keluaran yang benar hanya ketika kedua operan tersebut berbeda. Dengan kata lain, keluaran dari operasi `XOR` adalah benar jika tepat satu (tetapi tidak keduanya) dari operan tersebut benar. Sebagai contoh, operasi `XOR` antara `1` dan `0` akan menghasilkan `1`. Kita catat: $1 \oplus 0 = 1$. Demikian pula, operasi `XOR` dapat dilakukan pada urutan bit yang lebih panjang. Sebagai contoh, $10110 \oplus 01110 = 11000$. Setiap bit dari urutan tersebut dibandingkan dengan pasangannya, dan operasi `XOR` diterapkan. Berikut adalah tabel kebenaran untuk operasi `XOR`:

<div align="center">

| $A$ | $B$ | $A \oplus B$ |
|:---:|:---:|:------------:|
| $0$ | $0$ |      $0$     |
| $0$ | $1$ |      $1$     |
| $1$ | $0$ |      $1$     |
| $1$ | $1$ |      $0$     |

</div>

Operasi `XOR` digunakan di banyak area ilmu komputer, terutama dalam kriptografi, karena atribut-atribut menariknya seperti:
* Komutativitasnya: urutan dari operan tidak mempengaruhi hasil. Untuk dua variabel yang diberikan $D$ dan $E$: $D \oplus E = E \oplus D$;
* Asosiativitasnya: pengelompokan operan tidak mempengaruhi hasil. Untuk tiga variabel yang diberikan $A$, $B$, dan $C$: $(A \oplus B) \oplus C = A \oplus (B \oplus C)$;
* Memiliki elemen netral `0`: sebuah operan yang di-xor dengan 0 akan selalu sama dengan operan tersebut. Untuk sebuah variabel yang diberikan $A$: $A \oplus 0 = A$;
* Setiap elemen adalah inversnya sendiri. Untuk sebuah variabel yang diberikan $A$: $A \oplus A = 0$.

Dalam konteks Bitcoin, operasi `XOR` jelas digunakan di banyak tempat. Sebagai contoh, `XOR` digunakan secara massal dalam fungsi `SHA256`, yang banyak digunakan dalam protokol Bitcoin. Beberapa protokol seperti *SeedXOR* dari Coldcard juga menggunakan primitif ini untuk aplikasi lain. Ini juga ditemukan dalam BIP47 untuk mengenkripsi kode pembayaran yang dapat digunakan kembali selama transmisinya.
Dalam bidang kriptografi yang lebih luas, `XOR` dapat digunakan sebagai algoritma enkripsi simetris. Algoritma ini disebut "One-Time Pad" atau "Vernam Cipher," dinamai menurut penemunya. Meskipun tidak praktis karena panjang kunci, algoritma ini adalah salah satu dari sedikit algoritma enkripsi yang diakui sebagai aman tanpa syarat.