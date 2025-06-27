---
name: Keet
description: Obrolan peer-to-peer
---
![cover](assets/cover.webp)



Keet adalah aplikasi pesan instan yang dirancang untuk bekerja tanpa server. Diluncurkan pada tahun 2022 oleh Holepunch (sebuah perusahaan yang dibiayai oleh Tether dan Bitfinex), aplikasi ini sepenuhnya didasarkan pada jaringan peer-to-peer dan menampilkan pendekatan yang terdesentralisasi secara radikal: pesan, panggilan, dan berkas dipertukarkan secara langsung di antara para pengguna, tanpa perantara.



Keet mengenkripsi semua komunikasi dari ujung ke ujung dan tidak meminta data pribadi. Pendaftaran bersifat anonim, tanpa memerlukan nomor telepon atau email. Selain bertukar pesan teks, Keet menawarkan panggilan video berkualitas sangat tinggi, serta berbagi file tanpa batas. Oleh karena itu, aplikasi ini dapat digunakan dengan cara hibrida, baik untuk penggunaan pribadi maupun profesional.



![Image](assets/fr/01.webp)



Saat ini (April 2025), Keet belum sepenuhnya menjadi sumber terbuka. Beberapa kode sumber tersedia di [repositori GitHub Holepunch] (https://github.com/holepunchto), terutama komponen kriptografi dan jaringan, tetapi klien Interface belum. Akan tetapi, Holepunch telah mengumumkan niatnya untuk membuat seluruh aplikasi menjadi sumber terbuka pada akhirnya. Tergantung pada saat Anda menemukan tutorial ini, hal ini mungkin sudah dilakukan.




| Aplikasi             | E2EE 1:1       | E2EE grup      | Pendaftaran anonim  | Lisensi klien open-source | Lisensi server open-source | Server terdesentralisasi | Tahun pembuatan   |
| -------------------- | -------------- | -------------- | ------------------- | ------------------------- | -------------------------- | ------------------------ | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                         | ❌                          | ❌                        | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                         | ❌                          | ❌                        | 2011              |
| Facebook Messenger   | ✅              | 🟡 (opsional) | ❌                   | ❌                         | ❌                          | ❌                        | 2011              |
| Telegram             | 🟡 (opsional) | ❌              | 🟡                  | ✅                         | ❌                          | ❌                        | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                         | ❌                          | ❌                        | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                         | ✅                          | ❌                        | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                         | ❌                          | ❌                        | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                         | ✅                          | 🟡 (terfederasi)        | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                         | N/A                        | 🟡 (melalui email)      | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                         | ✅                          | 🟡 (terfederasi)        | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                         | ✅                          | ✅                        | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                         | ✅                          | ✅                        | 2021              |
| Olvid                | ✅              | ✅              | ✅                   | ✅                         | ❌                          | 🟡(tidak ada direktori) | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                         | N/A                        | ✅                        | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                         | N/A                        | ✅                        | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                         | N/A                        | ✅                        | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                         | N/A                        | ✅                        | 2013              |

*E2EE = Enkripsi ujung ke ujung*



## Instal Keet



Keet tersedia di semua platform. Anda dapat mengunduh aplikasi ini langsung dari toko aplikasi ponsel Anda:




- [Google Play](https://play.google.com/store/apps/details?id=io.keet.app&pli=1);
- [App Store](https://apps.apple.com/us/app/keet-by-holepunch/id6443880549);



Di Android, juga memungkinkan untuk [menginstal melalui APK](https://github.com/holepunchto/keet-mobile-releases/releases).



Dalam tutorial ini, kami akan berkonsentrasi pada versi seluler, tetapi harap dicatat bahwa [versi komputer juga tersedia] (https://keet.io/) (MacOS, Linux, dan Windows). Anda juga dapat menyinkronkan akun Anda di beberapa perangkat.



## Buat akun di Keet



Pada peluncuran pertama, Anda dapat mengabaikan layar presentasi.



![Image](assets/fr/02.webp)



Klik tombol "*Saya pengguna baru*".



![Image](assets/fr/03.webp)



Setujui persyaratan penggunaan, lalu klik "*Penyiapan cepat*".



![Image](assets/fr/04.webp)



Pilih nama atau nama panggilan, kemudian klik "*Selesai penyiapan*".



![Image](assets/fr/05.webp)



Profil Anda sekarang sudah dibuat. Klik "*Selesai penyiapan*" sekali lagi untuk menyelesaikannya.



![Image](assets/fr/06.webp)



Anda dapat menyesuaikan profil Anda kapan saja dari tab "*Profil*".



## Simpan akun Keet Anda



Hal pertama yang harus dilakukan dengan akun Keet baru Anda adalah menyimpan frasa pemulihan Anda. Ini adalah urutan 24 kata yang akan memungkinkan Anda untuk memulihkan akses ke akun Anda jika terjadi kehilangan atau pergantian perangkat. Frasa ini memberikan akses penuh ke akun Anda kepada siapa pun yang mengetahuinya, jadi penting untuk membuat cadangan yang dapat diandalkan dan jangan pernah membocorkannya.



Untuk melakukan ini, klik tab "*Profile*" di kanan bawah Interface.



![Image](assets/fr/07.webp)



Kemudian akses menu "*Pengaturan*".



![Image](assets/fr/08.webp)



Pilih "*Privasi dan Keamanan*".



![Image](assets/fr/09.webp)



Kemudian klik "*Frase pemulihan*".



![Image](assets/fr/10.webp)



Tekan tombol "*Lihat frasa*" untuk menampilkan frasa pemulihan Anda. Salin dengan hati-hati dan simpan di tempat yang aman.



![Image](assets/fr/11.webp)



## Mengirim pesan dengan Keet



Untuk berkomunikasi di Keet, Anda perlu membuat "*Rooms*". Untuk melakukannya, klik ikon pensil di kanan atas Interface.



![Image](assets/fr/12.webp)



Pilih "*Obrolan grup baru*".



![Image](assets/fr/13.webp)



Pilih nama dan deskripsi untuk "*Room*" Anda, lalu klik "*Buat obrolan grup*".



![Image](assets/fr/14.webp)



"*Room*" Anda sekarang telah dibuat. Klik ikon "*+*" di kanan atas untuk mengundang peserta.



![Image](assets/fr/15.webp)



Tentukan hak yang Anda berikan kepada anggota baru melalui tautan undangan, serta durasi validitas tautan. Kemudian klik "*Undangan generate*".



![Image](assets/fr/16.webp)



Keet akan mengirimkan tautan untuk bergabung dengan "*Room*" Anda. Anda dapat menyalinnya dan membagikannya, atau meminta kode QR-nya dipindai oleh orang yang ingin Anda undang.



![Image](assets/fr/17.webp)



Anda sekarang dapat mulai bertukar pesan dan file multimedia. Untuk memulai panggilan, klik ikon telepon di sudut kanan atas.



![Image](assets/fr/18.webp)



Dari grup ini, Anda juga dapat mengirim pesan pribadi ke anggota tertentu. Klik gambar profil grup, lalu pilih anggota yang diinginkan di bagian "*Anggota*".



![Image](assets/fr/19.webp)



Klik tombol "*Kirim permintaan DM*" dan masukkan pesan Anda.



![Image](assets/fr/20.webp)



Setelah permintaan DM diterima, Anda akan menemukan kontak ini di halaman beranda, di mana Anda dapat berbicara dengannya secara pribadi.



![Image](assets/fr/21.webp)



## Menyinkronkan akun Anda di beberapa perangkat



Sekarang setelah Anda mengetahui cara menggunakan Keet dan memiliki akun, Anda juga dapat menyinkronkannya pada perangkat lain, seperti komputer. Untuk melakukannya, buka aplikasi di ponsel Anda, lalu klik "*Profile*" dan akses "*Settings*".



![Image](assets/fr/22.webp)



Kemudian buka menu "*Perangkat saya*".



![Image](assets/fr/23.webp)



Klik "*Tambahkan perangkat*". Keet akan membuat tautan untuk menyinkronkan perangkat baru. Salin tautan ini.



![Image](assets/fr/24.webp)



Pada perangkat kedua Anda, instal Keet. Pada layar beranda, pilih opsi "*Saya pengguna saat ini*".



![Image](assets/fr/25.webp)



Kemudian klik "*Tautkan perangkat*".



![Image](assets/fr/26.webp)



Rekatkan tautan yang disediakan oleh perangkat pertama Anda, lalu klik "*Mulai sinkronisasi*".



![Image](assets/fr/27.webp)



Pada perangkat pertama Anda, klik "*Konfirmasi perangkat tautan*" untuk mengesahkan koneksi.



![Image](assets/fr/28.webp)



Pada perangkat kedua, selesaikan prosesnya dengan mengeklik "*Tautkan perangkat*".



![Image](assets/fr/29.webp)



Sekarang Anda dapat mengakses semua "*Room*" dan percakapan Anda dari perangkat baru ini.



![Image](assets/fr/30.webp)



Selamat, Anda sekarang sudah mahir menggunakan perpesanan Keet, sebuah alternatif yang bagus untuk WathsApp! Jika Anda merasa tutorial ini bermanfaat, saya akan sangat berterima kasih jika Anda memberikan tanda jempol Green di bawah ini. Jangan ragu untuk membagikan tutorial ini di jejaring sosial Anda. Terima kasih banyak!



Saya juga merekomendasikan tutorial lain ini, di mana saya memperkenalkan Anda pada Proton Mail, sebuah alternatif yang jauh lebih ramah privasi daripada Gmail:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2