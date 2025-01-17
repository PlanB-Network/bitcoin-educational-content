---
term: KUNCI PUBLIK TERKOMPRESI

---
Kunci publik digunakan dalam skrip (baik secara langsung dalam bentuk kunci publik atau sebagai alamat) untuk menerima dan mengamankan bitcoin. Sebuah kunci publik mentah diwakili oleh sebuah titik pada kurva elips, yang terdiri dari dua koordinat (`x, y`) yang masing-masing terdiri dari 256 bit. Dalam format mentah, kunci publik berukuran 512 bit, tidak termasuk byte tambahan untuk mengidentifikasi format. Kunci publik terkompresi, di sisi lain, adalah bentuk representasi kunci publik yang lebih ringkas. Kunci publik ini hanya menggunakan koordinat `x` dan sebuah awalan (`02` atau `03`) yang mengindikasikan paritas dari koordinat `y` (genap atau ganjil).

Jika kita menyederhanakan hal ini ke dalam bidang bilangan real, karena kurva elips simetris terhadap sumbu x, maka untuk setiap titik $P$ (`x, y`) pada kurva tersebut, terdapat titik $P'$ (`x, -y`) yang juga berada pada kurva yang sama. Ini berarti bahwa untuk setiap `x`, hanya ada dua kemungkinan nilai `y`, positif dan negatif. Sebagai contoh, untuk absis `x` yang diberikan, akan ada dua titik $P1$ dan $P2$ pada kurva elips, berbagi absis yang sama tetapi dengan ordinat yang berlawanan:

![](../../dictionnaire/assets/29.webp)

Untuk memilih di antara dua titik potensial pada kurva, sebuah awalan yang menentukan `y` mana yang akan dipilih ditambahkan ke `x`. Metode ini memungkinkan untuk mengurangi ukuran kunci publik dari 520 bit menjadi hanya 264 bit (8 bit prefix + 256 bit untuk `x`). Representasi ini dikenal sebagai bentuk terkompresi dari kunci publik.

Akan tetapi, dalam konteks kriptografi kurva elips, kita tidak menggunakan bilangan real, tetapi menggunakan sebuah bidang terbatas dengan orde `p` (bilangan prima). Dalam konteks ini, "tanda" dari `y` ditentukan oleh paritasnya, yaitu apakah `y` genap atau ganjil. Awalan `0x02` kemudian menunjukkan `y` genap, sedangkan `x03` menunjukkan `y` ganjil.

Pertimbangkan contoh kunci publik mentah (titik pada kurva elips) dalam heksadesimal berikut ini:

```plaintext
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f
6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```

Kita dapat mengisolasi awalan, `x`, dan `y`:

```plaintext
Prefix = 04
To determine the parity of `y`, we examine the last hexadecimal character of `y`:
```

Basis 16 (heksadesimal): f

Basis 10 (desimal): 15

y adalah ganjil

```
The prefix for the compressed public key will be `03`. The compressed public key in hexadecimal becomes:
```

K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6

```