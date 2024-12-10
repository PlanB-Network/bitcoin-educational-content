---
name: BIP39 Passphrase
description: Memahami cara kerja passphrase
---
![cover](assets/cover.webp)

## Apa itu passphrase BIP39?

Dompet HD biasanya dihasilkan dari frasa mnemonik yang terdiri dari 12 atau 24 kata. Frasa ini sangat penting karena memungkinkan pemulihan semua kunci dompet jika media fisiknya (seperti dompet perangkat keras, misalnya) hilang. Namun, ini merupakan satu titik kegagalan karena jika dikompromikan, penyerang dapat mencuri semua bitcoin.

![PASSPHRASE BIP39](assets/notext/01.webp)

Di sinilah passphrase berperan. Ini adalah kata sandi opsional yang dapat Anda pilih secara bebas, yang ditambahkan ke frasa mnemonik dalam proses derivasi kunci untuk meningkatkan keamanan dompet.

![PASSPHRASE BIP39](assets/notext/02.webp)

Berhati-hatilah untuk tidak mengacaukan passphrase dengan kode PIN dompet perangkat keras Anda atau kata sandi yang digunakan untuk membuka akses ke dompet Anda di komputer. Tidak seperti semua elemen ini, passphrase berperan dalam derivasi kunci dompet Anda. **Ini berarti tanpa itu, Anda tidak akan pernah bisa memulihkan bitcoin Anda.**

Passphrase bekerja bersama dengan frasa mnemonik, mengubah benih dari mana kunci dihasilkan. Jadi, meskipun seseorang mendapatkan frasa 12 atau 24 kata Anda, tanpa passphrase, mereka tidak dapat mengakses dana Anda. **Menggunakan passphrase pada dasarnya menciptakan dompet baru dengan kunci yang berbeda. Memodifikasi (bahkan sedikit) passphrase akan menghasilkan dompet yang berbeda.**

## Mengapa Anda harus menggunakan passphrase?

Passphrase bersifat sembarang dan bisa berupa kombinasi karakter apa pun yang dipilih oleh pengguna. Menggunakan passphrase dengan demikian menawarkan beberapa keuntungan. Pertama, ini mengurangi semua risiko yang terkait dengan kompromi frasa mnemonik dengan memerlukan faktor kedua untuk mengakses dana (pencurian, akses ke rumah Anda, dll.).

Selanjutnya, ini dapat digunakan secara strategis untuk membuat dompet umpan, untuk mengatasi kendala fisik mencuri dana Anda seperti serangan "*$5 wrench attack*". Dalam skenario ini, ideanya adalah memiliki dompet tanpa passphrase yang hanya berisi sejumlah kecil bitcoin, cukup untuk memuaskan penyerang potensial, sementara memiliki dompet tersembunyi. Dompet terakhir ini menggunakan frasa mnemonik yang sama tetapi diamankan dengan passphrase tambahan.

Akhirnya, menggunakan passphrase menarik ketika seseorang ingin mengontrol keacakan dari generasi benih dompet HD.

## Bagaimana memilih passphrase yang baik?
Agar passphrase efektif, harus cukup panjang dan acak. Sama seperti dengan kata sandi yang kuat, saya merekomendasikan memilih passphrase yang sepanjang dan seacak mungkin, dengan berbagai huruf, angka, dan simbol untuk membuat serangan brute force menjadi mustahil.

Juga penting untuk menyimpan passphrase ini dengan benar, sama seperti frasa mnemonik. **Kehilangannya berarti kehilangan akses ke bitcoin Anda**. Saya sangat menyarankan untuk tidak hanya menghafalnya di kepala Anda, karena ini meningkatkan risiko kehilangan secara tidak masuk akal. Yang ideal adalah menuliskannya pada media fisik (kertas atau logam) terpisah dari frasa mnemonik. Cadangan ini tentu saja harus disimpan di lokasi yang berbeda dari tempat frasa mnemonik Anda disimpan untuk mencegah keduanya dikompromikan secara bersamaan.

## Tutorial

Untuk mengatur passphrase pada perangkat Ledger (Stax, Flex, atau Nano), Anda dapat berkonsultasi dengan tutorial ini:

https://planb.network/tutorials/wallet/hardware/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49