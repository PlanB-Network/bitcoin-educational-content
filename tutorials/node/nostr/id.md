---
name: NOSTR

description: Temukan dan mulai menggunakan NOSTR
---

Di akhir panduan ini, Anda akan memahami apa itu Nostr, Anda akan telah membuat sebuah akun, dan Anda akan dapat menggunakannya.

![Seorang penantang baru telah tiba](assets/1.webp)

## Apa itu Nostr?

Nostr adalah sebuah protokol yang memiliki kekuatan untuk menggantikan Twitter, Telegram, dan platform media sosial lainnya. Ini adalah protokol terbuka sederhana yang mampu menciptakan jaringan sosial yang tahan global sekali dan untuk semua.

## Bagaimana cara kerjanya?

Nostr didasarkan pada tiga komponen: pasangan kunci, klien, dan relay.

Setiap pengguna memiliki satu atau lebih identitas, dan setiap identitas ditentukan oleh pasangan kunci kriptografi.

Untuk mengakses jaringan, Anda perlu menggunakan perangkat lunak klien dan terhubung ke relay untuk menerima dan mengirimkan konten.

![Sistem kunci](assets/2.webp)

## 1. Kunci Kriptografi

Tidak seperti Facebook atau Twitter, di mana pengguna harus memberikan alamat email dan banyak informasi kepada perusahaan swasta, Nostr beroperasi tanpa otoritas pusat. Pengguna menghasilkan pasangan kunci kriptografi, sebuah kunci rahasia (juga dikenal sebagai kunci privat), dan kunci publik.

Kunci rahasia, nsec, hanya diketahui oleh pengguna, digunakan untuk otentikasi dan penerbitan konten.

Kunci publik, npub, adalah pengenal unik di mana semua konten yang diterbitkan oleh pengguna terlampir. Kunci publik Anda seperti nama pengguna yang memungkinkan pengguna lain menemukan Anda dan berlangganan ke umpan Nostr Anda.

## 2. Klien

Klien adalah perangkat lunak yang memungkinkan interaksi dengan Nostr. Klien utama adalah:

> iOS: damus
> Android: amethyst
> Web: iris.to; snort.social; astral.ninja

Klien memungkinkan pengguna untuk menghasilkan pasangan kunci baru (setara dengan membuat akun) atau otentikasi dengan pasangan kunci yang sudah ada.

## 3. Relay

Relay adalah server sederhana yang dapat Anda tinggalkan kapan saja jika Anda tidak menyukai konten yang mereka sampaikan kepada Anda. Anda juga dapat menjalankan relay Anda sendiri jika Anda mau.

> 💡 Tips Pro: Relay berbayar umumnya lebih efektif dalam menyaring spam dan konten yang tidak diinginkan.

# Panduan

Sekarang Anda sudah cukup tahu tentang Nostr untuk memulai dan membuat identitas pertama Anda pada protokol ini.

Untuk keperluan panduan ini, kami akan menggunakan iris.to (https://iris.to/) karena klien web ini bekerja di platform apa pun.

## Langkah 1: Menghasilkan kunci

Iris akan membuatkan Anda satu set kunci tanpa Anda harus melakukan apa pun selain memasukkan nama (nyata atau fiktif) untuk profil Anda. Kemudian klik pada GO dan Anda selesai!

![Menu utama](assets/3.webp)

> ⚠️ Perhatian! Anda perlu melacak kunci Anda jika Anda ingin dapat mengakses profil Anda lagi setelah sesi Anda ditutup. Saya akan menunjukkan kepada Anda cara melakukan ini di akhir panduan ini.

## Langkah 2: Menerbitkan konten

Untuk menerbitkan konten, sama sederhana dan intuitifnya dengan menulis beberapa kata di bidang publikasi.

![Publikasi](assets/4.webp)

Sudah! Anda telah menerbitkan catatan pertama Anda di Nostr.

![Post](assets/5.webp)

## Langkah 3: Temukan teman

Temukan saya di Nostr dan tidak pernah sendirian lagi. Saya akan berlangganan kembali kepada siapa pun yang berlangganan ke umpan saya. Untuk melakukan ini, cukup masukkan kunci publik saya

npub1hartx53w6t3q5wv9xdqdwrk7h6r5866t8u775q0304zedpn5zgssasp7d3 di bilah pencarian.
![Profil Saya](assets/6.webp)
Klik pada "ikuti" dan dalam beberapa hari paling lama, saya juga akan berlangganan feed Anda. Kita akan menjadi teman. Saya juga akan senang membaca pesan Anda jika Anda ingin menulis satu untuk saya.

Akhirnya, pastikan untuk juga berlangganan feed Agora256 untuk menerima catatan setiap kali kami mempublikasikan sesuatu yang baru: npub1ag0rawstycy7nanuc6sz4v287rneen2yapcq3fd06972f8ncrhzqx

## Langkah 4: Sesuaikan Profil Anda

Anda masih memiliki beberapa pekerjaan untuk menyesuaikan profil Anda. Untuk melakukan ini, klik pada avatar yang secara otomatis dihasilkan oleh iris untuk Anda di sudut kanan atas layar dan kemudian klik pada "edit profil".

![Profil](assets/7.webp)

Yang harus Anda lakukan sekarang adalah memberitahu iris di mana menemukan gambar dan banner profil Anda di internet. Saya merekomendasikan untuk hosting konten Anda sendiri: lindungi apa yang menjadi milik Anda.

![Opsi Lain](assets/8.webp)

Jika Anda mau, Anda juga dapat mengunggah gambar, gambar tersebut akan disimpan untuk Anda oleh iris di nostr.build, sebuah layanan hosting konten visual gratis untuk Nostr.

Seperti yang Anda lihat, Anda juga dapat mengonfigurasi klien Anda untuk dapat menerima dan mengirim sats. Dengan cara ini, Anda dapat memberi penghargaan kepada penulis konten yang Anda suka atau, lebih baik lagi, mengumpulkan sats untuk konten hebat yang akan Anda publikasikan.

## Langkah 5: Cadangkan Pasangan Kunci

Langkah ini sangat penting jika Anda ingin tetap memiliki akses ke profil Anda setelah Anda keluar dari klien atau sesi Anda telah berakhir.
Pertama, klik pada ikon "pengaturan" yang diwakili oleh sebuah roda gigi
![Pengaturan](assets/9.webp)

Kemudian, salin dan tempel satu per satu npub Anda, npub hex, nsec, dan nsec hex ke dalam file teks yang akan Anda simpan dengan aman. Saya merekomendasikan mengenkripsi file ini jika Anda tahu cara melakukannya.

![Kunci](assets/10.webp)

> ⚠️ Perhatikan peringatan yang diberikan oleh iris. Meskipun Anda dapat berbagi kunci publik Anda tanpa takut, ceritanya berbeda untuk kunci pribadi Anda. Siapa pun yang memiliki yang terakhir akan dapat mengakses akun Anda.

## Kesimpulan

Nah, burung unta kecil, Anda telah mengambil langkah pertama Anda di Nostr. Sekarang, Anda perlu belajar berlari dengan kecepatan kilat. Kami akan segera mempublikasikan panduan yang akan menunjukkan kepada Anda cara mengelola kunci Anda dan cara mengintegrasikan lightning ke dalam pengalaman Nostr Anda menggunakan getalby.