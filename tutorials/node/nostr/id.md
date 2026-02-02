---
name: Nostr
description: Temukan dan mulai menggunakan Nostr
---


![Seorang penantang baru telah tiba](assets/cover.webp)

*Di akhir panduan ini, kamu akan paham apa itu Nostr, kamu akan bikin akun, dan kamu bakal bisa langsung pakai Nostr.*

## Apa itu Nostr?

Nostr adalah protokol yang punya potensi menggantikan Twitter, Telegram, dan platform media sosial lainnya. Ini protokol terbuka yang sederhana tapi mampu membangun jaringan sosial yang tahan dan berskala global sekali untuk selamanya.

## Bagaimana cara kerjanya?

Nostr dibangun di atas tiga komponen: keypair, klien, dan relay.

Setiap pengguna punya satu atau lebih identitas, dan setiap identitas ditentukan oleh pasangan kunci kriptografi.

Untuk mengakses jaringan, kamu perlu pakai software klien dan terhubung ke relay untuk menerima dan mengirim konten.

![Sistem kunci](assets/2.webp)

## 1. Kunci Kriptografi

Berbeda dengan Facebook atau Twitter, di mana pengguna harus ngasih alamat email dan banyak info pribadi ke perusahaan, Nostr berjalan tanpa otoritas pusat. Pengguna cukup menghasilkan pasangan kunci kriptografi: satu kunci rahasia (kunci privat) dan satu kunci publik.

Kunci rahasia, nsec, cuma boleh diketahui pengguna. Ini dipakai buat autentikasi dan buat nerbitin konten.

Kunci publik, npub, jadi pengenal unik tempat semua konten yang kamu terbitkan menempel. Kunci publik kamu ini mirip nama pengguna yang bikin orang lain bisa nemuin kamu dan subscribe ke feed Nostr kamu.

## 2. Klien

Klien adalah perangkat lunak yang memungkinkan interaksi dengan Nostr. Klien utama adalah:

- iOS: damus
- Android: amethyst
- Web: iris.to; snort.social; astral.ninja

Klien memungkinkan pengguna untuk menghasilkan pasangan kunci baru (setara dengan membuat akun) atau otentikasi dengan pasangan kunci yang sudah ada.

## 3. Relay

Relay adalah server sederhana yang bisa kamu tinggalkan kapan saja kalau kamu nggak suka dengan konten yang mereka kirimkan ke kamu. Kamu juga bisa menjalankan relay sendiri kalau mau.

> 💡 Tips Pro: Relay berbayar umumnya lebih efektif dalam menyaring spam dan konten yang tidak diinginkan.

## Panduan

Sekarang kamu sudah cukup ngerti tentang Nostr buat mulai dan bikin identitas pertamamu di protokol ini.

Untuk keperluan panduan ini, kita akan pakai iris.to (https://iris.to/) karena klien web ini bekerja di platform apa pun.

## Langkah 1: Menghasilkan kunci

Iris bakal buatkan kamu satu set kunci tanpa kamu harus ngapa-ngapain selain masukin nama (asli atau fiktif) buat profil kamu. Habis itu klik GO dan selesai!

![Menu utama](assets/3.webp)

> ⚠️ Perhatian! Kamu harus nyimpen kunci kamu kalau mau bisa akses profil kamu lagi setelah sesi ditutup. Aku bakal tunjukin caranya di akhir panduan ini.

## Langkah 2: Menerbitkan konten

Untuk menerbitkan konten, sama sederhana dan intuitifnya dengan menulis beberapa kata di bidang publikasi.

![Publikasi](assets/4.webp)

Sudah! Kamu baru aja nerbitin catatan pertamamu di Nostr.

![Post](assets/5.webp)

## Langkah 3: Temukan teman

Temuin aku di Nostr dan kamu nggak akan sendirian lagi. Aku bakal subscribe balik siapa pun yang subscribe ke feed aku. Buat itu, cukup masukin kunci publik aku.

npub1hartx53w6t3q5wv9xdqdwrk7h6r5866t8u775q0304zedpn5zgssasp7d3 di bilah pencarian.
![Profil Saya](assets/6.webp)
Klik “ikuti” dan dalam beberapa hari paling lama, aku juga bakal subscribe ke feed kamu. Kita bakal jadi teman. Aku juga senang baca pesan kamu kalau kamu mau nulis satu buat aku..

Akhirnya, pastikan untuk juga berlangganan feed Agora256 untuk menerima catatan setiap kali kami mempublikasikan sesuatu yang baru: npub1ag0rawstycy7nanuc6sz4v287rneen2yapcq3fd06972f8ncrhzqx

## Langkah 4: Sesuaikan Profil Anda

Kamu masih punya sedikit pekerjaan buat nyesuaiin profil kamu. Buat itu, klik avatar yang otomatis dibuat Iris buat kamu di pojok kanan atas layar, lalu klik “edit profil”.

![Profil](assets/7.webp)

Sekarang kamu cuma perlu ngasih tahu Iris di mana dia bisa nemuin foto profil dan banner kamu di internet. Aku saranin kamu hosting kontenmu sendiri supaya apa yang jadi milik kamu tetap aman.

![Opsi Lain](assets/8.webp)

Kalau mau, kamu juga bisa upload gambar. Gambar itu nanti disimpan Iris buat kamu di nostr.build, layanan hosting konten visual gratis buat Nostr.

Seperti yang bisa kamu lihat, kamu juga bisa nyetel klien kamu supaya bisa nerima dan ngirim sats. Dengan cara ini, kamu bisa ngasih apresiasi ke penulis konten yang kamu suka atau, lebih bagus lagi, ngumpulin sats dari konten keren yang bakal kamu publikasikan.

## Langkah 5: Cadangkan Pasangan Kunci

Langkah ini penting banget kalau kamu mau tetap bisa akses profil kamu setelah keluar dari klien atau sesi kamu berakhir.
Pertama, klik ikon “pengaturan” yang digambarkan dengan roda gigi.
![Pengaturan](assets/9.webp)

Lalu, salin dan tempel satu per satu npub kamu, npub hex, nsec, dan nsec hex ke dalam file teks yang bakal kamu simpan dengan aman. Aku saranin kamu enkripsi file ini kalau kamu tahu cara ngelakukannya.

![Kunci](assets/10.webp)

> ⚠️ Perhatiin juga peringatan dari Iris. Walaupun kamu bisa bebas berbagi kunci publik kamu, ceritanya beda untuk kunci privat. Siapa pun yang punya kunci itu bisa akses akun kamu.

## Kesimpulan

Nah, burung unta kecil, Anda telah mengambil langkah pertama Anda di Nostr. Sekarang, Anda perlu belajar berlari dengan kecepatan kilat. Kami akan segera mempublikasikan panduan yang akan menunjukkan kepada Anda cara mengelola kunci Anda dan cara mengintegrasikan lightning ke dalam pengalaman Nostr Anda menggunakan getalby.
