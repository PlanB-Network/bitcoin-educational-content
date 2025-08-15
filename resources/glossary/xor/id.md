---
term: XOR

---
Akronim untuk operasi "_Exclusive OR_", yang merupakan fungsi mendasar dari logika _Boolean_. Operasi ini mengambil dua operan _Boolean_, masing-masing adalah $true$ atau $false$, dan menghasilkan output $_true_$ hanya jika kedua operan tersebut berbeda. Dengan kata lain, output dari operasi XOR adalah $_true_$ jika salah satu (tetapi tidak keduanya) dari operand bernilai $_true_$. Sebagai contoh, operasi XOR antara $1$ dan $0$ akan menghasilkan $1$. Kami mencatat:

$$
1 \oplus 0 = 1
$$

Demikian pula, operasi XOR dapat dilakukan pada urutan bit yang lebih panjang. Sebagai contoh:

$$
10110 \oplus 01110 = 11000
$$

Setiap bit dalam urutan dibandingkan dengan pasangannya, dan operasi XOR diterapkan. Berikut ini adalah tabel kebenaran untuk operasi XOR:

<div align="center">

| $A$ | $B$ | $A \oplus B$ |

|:---:|:---:|:------------:|

| $0$ | $0$ | $0$ |

| $0$ | $1$ | $1$ |

| $1$ | $0$ | $1$ |

| $1$ | $1$ | $0$ |

</div> </div

Operasi XOR digunakan di banyak bidang ilmu komputer, terutama dalam kriptografi, karena atribut-atributnya yang menarik seperti:


- Komutativitasnya: urutan operan tidak mempengaruhi hasil. Untuk dua variabel yang diberikan $D$ dan $E$: $D \oplus E = E \oplus D$;
- Asosiatifitasnya: pengelompokan operan tidak mempengaruhi hasil. Untuk tiga variabel yang diberikan $A$, $B$, dan $C$: $(A \oplus B) \oplus C = A \oplus (B \oplus C)$;
- Variabel ini memiliki elemen netral $0$: sebuah operand yang dikalikan dengan $0$ akan selalu sama dengan operand. Untuk sebuah variabel yang diberikan $A$: $A \oplus 0 = A$;
- Setiap elemen adalah lawan dari elemen lainnya. Untuk sebuah variabel yang diberikan $A$: $A \oplus A = 0$.

Dalam konteks Bitcoin, operasi XOR digunakan di banyak tempat. Sebagai contoh, XOR digunakan secara masif dalam fungsi SHA256, yang digunakan secara luas dalam protokol Bitcoin. Beberapa protokol seperti *SeedXOR* dari Coldcard juga menggunakan primitif ini untuk aplikasi lainnya. Ini juga ditemukan di BIP47 untuk mengenkripsi kode pembayaran yang dapat digunakan kembali selama transmisi.

Dalam bidang kriptografi yang lebih luas, XOR dapat digunakan sebagai algoritma enkripsi simetris. Algoritma ini disebut "_One-Time Pad_" atau "_Vernam Cypher_", yang dinamai sesuai dengan penemunya. Meskipun tidak praktis karena panjangnya kunci, algoritma ini merupakan satu-satunya algoritma enkripsi yang diakui aman tanpa syarat.
