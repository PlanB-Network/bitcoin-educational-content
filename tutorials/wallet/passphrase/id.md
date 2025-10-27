---
name: Passphrase BIP39
description: Memahami cara kerja passphrase
---
![cover](assets/cover.webp)

## Apa itu passphrase BIP39?

Dompet HD biasanya dibuat dari seedphrase yang terdiri dari 12 atau 24 kata. Seedphrase ini sangat penting karena memungkinkan kamu memulihkan semua kunci dompet kalau media fisiknya (misalnya hardware wallet) hilang. Tapi, seedphrase juga jadi satu titik kegagalan karena kalau sampai bocor, penyerang bisa mencuri semua bitcoin kamu.

![PASSPHRASE BIP39](assets/notext/01.webp)

Di sinilah passphrase berperan. Ini adalah kata sandi opsional yang bisa kamu pilih sesuka hati, dan akan ditambahkan ke seedphrase dalam proses pembentukan kunci untuk meningkatkan keamanan dompet.

![PASSPHRASE BIP39](assets/notext/02.webp)

Berhati-hatilah untuk tidak mengacaukan passphrase dengan PIN dompet hardware atau kata sandi yang dipakai untuk membuka dompet di komputermu. Tidak seperti elemen-elemen itu, passphrase berperan langsung dalam derivasi kunci dompetmu. Ini berarti tanpa passphrase, kamu tidak akan pernah bisa memulihkan bitcoinmu.

Passphrase bekerja bersama seedphrase, mengubah seed dari mana kunci dihasilkan. Jadi, meskipun seseorang mendapat seedphrase 12 atau 24 kata kamu, tanpa passphrase mereka tidak bisa mengakses dana kamu. Menggunakan passphrase pada dasarnya menciptakan dompet baru dengan kunci yang berbeda. Mengubahnya sedikit saja akan menghasilkan dompet yang berbeda.

## Mengapa Anda harus menggunakan passphrase?

Passphrase bersifat bebas dan bisa berupa kombinasi karakter apa pun yang kamu pilih. Menggunakan passphrase dengan demikian menawarkan beberapa keuntungan. Pertama, ini mengurangi semua risiko yang terkait dengan kompromi seedphrase dengan memerlukan faktor kedua untuk mengakses dana (pencurian, akses ke rumahmu, dll.).

Selanjutnya, ini bisa dipakai secara strategis untuk membuat dompet umpan, untuk mengatasi kendala fisik pencurian dana seperti serangan "$5 wrench attack". Dalam skenario ini, idenya adalah punya dompet tanpa passphrase yang hanya berisi sejumlah kecil bitcoin, cukup untuk memuaskan penyerang potensial, sementara punya dompet tersembunyi. Dompet terakhir ini memakai seedphrase yang sama tetapi diamankan dengan passphrase tambahan.

Akhirnya, memakai passphrase menarik kalau seseorang ingin mengontrol keacakan dalam proses generasi seed dompet HD.

## Bagaimana memilih passphrase yang baik?
Agar passphrase efektif, harus cukup panjang dan acak. Sama seperti kata sandi yang kuat, aku merekomendasikan kamu memilih passphrase sepanjang dan seacak mungkin, dengan campuran huruf, angka, dan simbol agar serangan brute force jadi mustahil.

Menurut [sebuah studi yang dilakukan oleh Trezor pada tahun 2019](https://blog.trezor.io/is-your-passphrase-strong-enough-d687f44c63af), seorang penyerang yang memiliki akses ke seed Anda dan menggunakan GPU kelas atas yang disewa di AWS (NVIDIA Tesla V100) dapat menguji hampir 620 juta passphrase hanya dengan 1 dolar. Sebagai gambaran, dengan kemampuan tahun 2019, sebuah passphrase yang terdiri dari 12 huruf kecil acak akan memerlukan biaya rata-rata **77 juta dolar** untuk dibobol.

Tapi aku nggak nyaranin kamu cuma pakai 12 karakter. Sebaiknya ikuti standar terbaru untuk kata sandi kuat: di tahun 2025 ini, gunakan minimal 13 karakter acak yang mencakup angka, huruf kecil, huruf besar, dan simbol; atau 14 karakter kalau kamu cuma pakai huruf kecil dan huruf besar. Tentu aja, makin panjang makin bagus—misalnya passphrase sepanjang 20 karakter dengan simbol—buat ngantisipasi perkembangan di masa depan dan mempertimbangkan risiko manusia yang nggak selalu diperhitungkan dalam studi-studi itu.

Penting juga untuk menyimpan passphrase ini dengan benar, sama seperti seedphrase. **Kehilangannya berarti kamu kehilangan akses ke bitcoin kamu.** Aku sangat nggak nyaranin buat cuma menghafalnya di kepala, karena itu bikin risiko kehilangan jadi nggak masuk akal. Cara paling aman adalah menuliskannya di media fisik (kertas atau logam) yang terpisah dari seedphrase. Cadangan ini juga harus disimpan di lokasi berbeda dari tempat kamu menyimpan seedphrase, biar keduanya nggak bisa dikompromikan sekaligus.

## Tutorial

Untuk mengatur passphrase pada perangkat Ledger (Stax, Flex, atau Nano), kamu bisa cek tutorial ini:

https://planb.network/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

Pada COLDCARD:

https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

Pada Jade Plus:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

Pada Passport (batch-2):

https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Pada perangkat Trezor (Safe 3, Safe 5, atau Model One):

https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

