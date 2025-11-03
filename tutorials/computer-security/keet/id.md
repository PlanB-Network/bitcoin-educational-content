---
name: Keet
description: Obrolan peer-to-peer
---
![cover](assets/cover.webp)

Keet adalah aplikasi pesan instan yang dirancang untuk berfungsi tanpa server apa pun. Diluncurkan pada tahun 2022 oleh Holepunch (sebuah perusahaan yang didanai oleh Tether dan Bitfinex), aplikasi ini sepenuhnya berbasis pada jaringan peer-to-peer dan menampilkan pendekatan desentralisasi radikal: pesan, panggilan, dan file dipertukarkan langsung antar pengguna, tanpa perantara.

Keet mengenkripsi semua komunikasi secara *end-to-end* dan tidak meminta data pribadi apa pun. Pendaftaran bersifat anonim, tanpa memerlukan nomor telepon atau email. Selain bertukar pesan teks, Keet menawarkan panggilan video berkualitas sangat tinggi, serta berbagi file tanpa batas. Oleh karena itu, aplikasi ini dapat digunakan secara hibrida, baik untuk penggunaan pribadi maupun profesional.
![Image](assets/fr/01.webp)

Saat ini (April 2025), Keet belum sepenuhnya *open-source*. Beberapa *source code* tersedia di [repositori GitHub Holepunch](https://github.com/holepunchto), terutama komponen kriptografi dan jaringan, namun antarmuka klien belum tersedia. Holepunch, bagaimanapun, telah mengumumkan niatnya untuk menjadikan seluruh aplikasi *open-source* pada akhirnya. Tergantung kapan Anda menemukan tutorial ini, hal tersebut mungkin sudah terlaksana.


| Aplikasi             | E2EE 1:1       | E2EE grup      | Pendaftaran anonim  | Lisensi open-source Pengguna | Lisensi open-source Server | Server terdesentralisasi | Tahun pembuatan   |
| -------------------- | -------------- | -------------- | ------------------- | ------------------------- | -------------------------- | ------------------------ | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                         | ❌                          | ❌                        | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                         | ❌                          | ❌                        | 2011              |
| Facebook Messenger   | ✅              | 🟡 (opsional) | ❌                   | ❌                         | ❌                          | ❌                        | 2011              |
| Telegram             | 🟡 (opsional) | ❌              | 🟡                  | ✅                         | ❌                          | ❌                        | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                         | ❌                          | ❌                        | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                         | ✅                          | ❌                        | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                         | ❌                          | ❌                        | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                         | ✅                          | 🟡 (gabungan)        | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                         | N/A                        | 🟡 (melalui email)      | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                         | ✅                          | 🟡 (gabungan)        | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                         | ✅                          | ✅                        | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                         | ✅                          | ✅                        | 2021              |
| Olvid                | ✅              | ✅              | ✅                   | ✅                         | ❌                          | 🟡(tidak ada direktori pusat) | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                         | N/A                        | ✅                        | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                         | N/A                        | ✅                        | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                         | N/A                        | ✅                        | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                         | N/A                        | ✅                        | 2013              |

*E2EE = Enkripsi End-to-end (End-to-end encryption)*

## Instal Keet

Keet tersedia di semua platform. Anda dapat mengunduh aplikasi ini langsung dari toko aplikasi ponsel Anda:
- [Google Play](https://play.google.com/store/apps/details?id=io.keet.app&pli=1);
- [App Store](https://apps.apple.com/us/app/keet-by-holepunch/id6443880549);

Di Android, juga memungkinkan untuk [menginstal melalui APK](https://github.com/holepunchto/keet-mobile-releases/releases).

Dalam tutorial ini, kita akan fokus pada versi seluler, tetapi perlu diketahui bahwa [versi komputer juga tersedia](https://keet.io/) (MacOS, Linux, dan Windows). Anda juga bisa menyinkronkan akun Anda di beberapa perangkat.

## Buat akun di Keet

Pada peluncuran pertama, Anda dapat mengabaikan layar presentasi.
![Image](assets/fr/02.webp)

Klik tombol "*I am new user*".
![Image](assets/fr/03.webp)

Setujui persyaratan penggunaan, lalu klik "*Quick setup*".
![Image](assets/fr/04.webp)

Pilih nama atau nama panggilan, kemudian klik "*Finish setup*".
![Image](assets/fr/05.webp)

Profil Anda sekarang telah dibuat. Klik "*Finish setup*" sekali lagi untuk menyelesaikannya.
![Image](assets/fr/06.webp)

Anda dapat menyesuaikan profil Anda kapan saja dari tab "*Profile*".

## Simpan akun Keet Anda

Hal pertama yang perlu Anda lakukan dengan akun baru Keet Anda adalah menyimpan frasa pemulihan Anda. Ini adalah rangkaian 24 kata yang akan memungkinkan Anda memulihkan akses ke akun Anda jika perangkat hilang atau diganti. Frasa ini memberikan akses penuh ke akun Anda kepada siapa pun yang mengetahuinya, oleh karena itu, penting untuk membuat cadangan yang andal dan jangan pernah membocorkannya.

Untuk melakukan ini, klik tab "*Profile*" di kanan bawah Interface.
![Image](assets/fr/07.webp)

Kemudian akses menu "*Settings*".
![Image](assets/fr/08.webp)

Pilih "*Privacy and Security*".
![Image](assets/fr/09.webp)

Kemudian klik "*Recovery phrase*".
![Image](assets/fr/10.webp)

Tekan tombol "*View phrase*" untuk menampilkan frasa pemulihan Anda. Salin dengan hati-hati dan simpan di tempat yang aman.
![Image](assets/fr/11.webp)

## Mengirim pesan dengan Keet

Untuk berkomunikasi di Keet, Anda perlu membuat "*Rooms*". Untuk melakukannya, klik ikon pensil di kanan atas pada tampilan.
![Image](assets/fr/12.webp)

Pilih "*New group chat*".
![Image](assets/fr/13.webp)

Pilih nama dan deskripsi untuk "*Room*" Anda, lalu klik "*Create group chat*".
![Image](assets/fr/14.webp)

"*Room*" Anda sekarang telah dibuat. Klik ikon "*+*" di kanan atas untuk mengundang peserta.
![Image](assets/fr/15.webp)

Tentukan hak akses yang Anda berikan kepada anggota baru melalui tautan undangan, serta durasi validitas tautan tersebut. Kemudian, klik "Generate Invite".
![Image](assets/fr/16.webp)

Keet akan membuat tautan untuk bergabung ke "*Room*" Anda. Anda bisa menyalinnya dan membagikannya, atau meminta orang yang ingin Anda undang untuk memindai kode QR-nya.
![Image](assets/fr/17.webp)

Anda kini bisa mulai bertukar pesan dan file multimedia. Untuk memulai panggilan, klik ikon telepon di sudut kanan atas.
![Image](assets/fr/18.webp)

Dari grup ini, Anda juga bisa mengirim pesan pribadi ke anggota tertentu. Klik pada gambar profil grup, lalu pilih anggota yang diinginkan di bagian "*Members*".
![Image](assets/fr/19.webp)

Klik tombol "*Send DM request*" dan masukkan pesan Anda.
![Image](assets/fr/20.webp)

Setelah permintaan DM (Pesan Langsung) diterima, Anda akan menemukan kontak ini di halaman utama, tempat Anda dapat berbicara dengannya secara pribadi. 
![Image](assets/fr/21.webp)

## Menyinkronkan akun Anda di beberapa perangkat

Sekarang setelah Anda mengetahui cara menggunakan Keet dan memiliki akun, Anda juga bisa menyinkronkannya di perangkat lain, seperti komputer. Untuk melakukannya, buka aplikasi di ponsel Anda, lalu klik "*Profile*" dan akses "*Settings*".
![Image](assets/fr/22.webp)

Kemudian buka menu "*My devices*".
![Image](assets/fr/23.webp)

Klik "*Add device*". Keet akan membuat tautan untuk menyinkronkan perangkat baru. Salin tautan ini.
![Image](assets/fr/24.webp)

Pada perangkat kedua Anda, instal Keet. Pada layar beranda, pilih opsi "*I'm a current user*". 
![Image](assets/fr/25.webp)

Kemudian klik "*Link device*".
![Image](assets/fr/26.webp)

Tempel tautan yang disediakan oleh perangkat pertama Anda, lalu klik "*Start syncing*".
![Image](assets/fr/27.webp)

Pada perangkat pertama Anda, klik "*Confirm link devices*" untuk mengizinkan koneksi.
![Image](assets/fr/28.webp)

Pada perangkat kedua, selesaikan prosesnya dengan mengeklik "*Link devices*".
![Image](assets/fr/29.webp)

Anda sekarang dapat mengakses semua "*Room*" dan percakapan Anda dari perangkat baru ini.
![Image](assets/fr/30.webp)

Selamat, Anda sekarang sudah mahir menggunakan perpesanan Keet, sebuah alternatif yang bagus untuk WathsApp! Jika Anda merasa tutorial ini bermanfaat, saya akan sangat berterima kasih jika Anda memberikan tanda jempol Green di bawah ini. Jangan ragu untuk membagikan tutorial ini di jejaring sosial Anda. Terima kasih banyak!

Selamat, Anda kini telah menguasai penggunaan *Keet messaging*, sebuah alternatif yang sangat baik selain WhatsApp! Jika Anda menemukan tutorial ini bermanfaat, saya akan sangat berterima kasih apabila Anda berkenan untuk memberikan tanda jempol hijau di bawah. Jangan ragu untuk membagikan tutorial ini di media sosial Anda. Terima kasih banyak!

Saya juga merekomendasikan tutorial lain, di mana saya memperkenalkan Anda pada Proton Mail, sebuah alternatif yang jauh lebih mengutamakan privasi daripada Gmail:

https://planb.academy/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2
