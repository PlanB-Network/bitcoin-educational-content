---
term: KUNCI PUBLIK TERKOMPRESI
---

Kunci publik digunakan dalam skrip (baik langsung dalam bentuk kunci publik atau sebagai alamat) untuk menerima dan mengamankan bitcoin. Kunci publik mentah diwakili oleh sebuah titik pada kurva eliptik, yang terdiri dari dua koordinat (`x, y`) masing-masing 256 bit. Dalam format mentah, kunci publik oleh karena itu berukuran 512 bit, tidak termasuk byte tambahan untuk mengidentifikasi formatnya. Sebaliknya, kunci publik terkompresi adalah bentuk representasi kunci publik yang lebih kompak. Ini hanya menggunakan koordinat `x` dan sebuah prefiks (`02` atau `03`) yang menunjukkan paritas dari koordinat `y` (genap atau ganjil).

Jika kita menyederhanakan ini ke bidang bilangan riil, mengingat kurva eliptik simetris terhadap sumbu-x, untuk setiap titik $P$ (`x, y`) pada kurva, ada titik $P'$ (`x, -y`) yang juga akan berada pada kurva yang sama. Ini berarti bahwa untuk setiap `x`, hanya ada dua nilai `y` yang mungkin, positif dan negatif. Sebagai contoh, untuk sebuah absis `x` yang diberikan, akan ada dua titik $P1$ dan $P2$ pada kurva eliptik, yang berbagi absis yang sama tetapi dengan ordinat yang berlawanan:

![](../../dictionnaire/assets/29.png)
Untuk memilih antara dua titik potensial pada kurva, sebuah prefiks yang menentukan `y` mana yang dipilih ditambahkan ke `x`. Metode ini memungkinkan pengurangan ukuran kunci publik dari 520 bit menjadi hanya 264 bit (8 bit prefiks + 256 bit untuk `x`). Representasi ini dikenal sebagai bentuk terkompresi dari kunci publik.

Namun, dalam konteks kriptografi kurva eliptik, kita menggunakan bukan bilangan riil, tetapi sebuah lapangan hingga berorde `p` (sebuah bilangan prima). Dalam konteks ini, "tanda" dari `y` ditentukan oleh paritasnya, yaitu, apakah `y` genap atau ganjil. Prefiks `0x02` kemudian menunjukkan `y` genap, sementara `0x03` menunjukkan `y` ganjil.

Pertimbangkan contoh berikut dari sebuah kunci publik mentah (sebuah titik pada kurva eliptik) dalam heksadesimal:
```plaintext
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f
6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```

Kita dapat memisahkan prefiks, `x`, dan `y`:
```plaintext
Prefiks = 04
Untuk menentukan paritas dari `y`, kita periksa karakter heksadesimal terakhir dari `y`:
```plaintext
Basis 16 (heksadesimal): f
Basis 10 (desimal): 15
y ganjil
```

Prefiks untuk kunci publik terkompresi akan menjadi `03`. Kunci publik terkompresi dalam heksadesimal menjadi:
```plaintext
K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6
```