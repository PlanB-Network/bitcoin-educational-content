---
term: EKSKLUSIF ATAU

---
Fungsi mendasar dari logika Boolean. "Exclusive Or" atau XOR ("*Exclusive or*") mengambil dua operan Boolean, masing-masing benar atau salah, dan menghasilkan output yang benar hanya jika kedua operan tersebut berbeda. Dengan kata lain, output dari operasi `XOR` adalah benar jika salah satu (tetapi tidak keduanya) dari operand bernilai benar. Sebagai contoh, operasi `XOR` antara `1` dan `0` akan menghasilkan `1`. Kita mencatat: $1 \ ditambah 0 = 1$. Demikian pula, operasi `XOR` dapat dilakukan pada urutan bit yang lebih panjang. Sebagai contoh, $10110 \oplus 01110 = 11000$. Setiap bit dari urutan tersebut dibandingkan dengan pasangannya, dan operasi `XOR` diterapkan. Berikut ini adalah tabel kebenaran untuk operasi `XOR`:

<div align="center">

| $A$ | $B$ | $A \oplus B$ |

|:---:|:---:|:------------:|

| $0$ | $0$ | $0$ |

| $0$ | $1$ | $1$ |

| $1$ | $0$ | $1$ |

| $1$ | $1$ | $0$ |

</div> </div

Operasi `XOR` digunakan di banyak bidang ilmu komputer, terutama dalam kriptografi, karena atribut-atributnya yang menarik seperti:


- Komutativitasnya: urutan operan tidak mempengaruhi hasil. Untuk dua variabel yang diberikan $D$ dan $E$: $D \oplus E = E \oplus D$;
- Asosiatifitasnya: pengelompokan operan tidak mempengaruhi hasil. Untuk tiga variabel yang diberikan $A$, $B$, dan $C$: $(A \oplus B) \oplus C = A \oplus (B \oplus C)$;
- Ia memiliki elemen netral `0`: sebuah operand yang dikalikan dengan 0 akan selalu sama dengan operand. Untuk sebuah variabel yang diberikan $A$: $A \oplus 0 = A$;
- Setiap elemen adalah kebalikan dari elemen lainnya. Untuk sebuah variabel yang diberikan $A$: $A \oplus A = 0$.

Dalam konteks Bitcoin, operasi `XOR` jelas digunakan di banyak tempat. Sebagai contoh, `XOR` digunakan secara masif dalam fungsi `SHA256`, yang digunakan secara luas dalam protokol Bitcoin. Beberapa protokol seperti *SeedXOR* dari Coldcard juga menggunakan primitif ini untuk aplikasi lain. Ini juga ditemukan di BIP47 untuk mengenkripsi kode pembayaran yang dapat digunakan kembali selama transmisi.

Dalam bidang kriptografi yang lebih luas, `XOR` dapat digunakan sebagai algoritma enkripsi simetris. Algoritma ini disebut "One-Time Pad" atau "Vernam Cipher", yang diambil dari nama penemunya. Meskipun tidak praktis karena panjangnya kunci, algoritma ini merupakan satu-satunya algoritma enkripsi yang diakui aman tanpa syarat.