---
name: Session
description: Mengirim pesan terenkripsi, bukan metadata
---

![cover](assets/cover.webp)

Session adalah aplikasi kirim pesan terenkripsi yang dibuat pada tahun 2020. Aplikasi ini dirancang untuk menawarkan tingkat kerahasiaan yang lebih tinggi daripada perngirim pesan tradisional. Awalnya dikembangkan oleh Oxen Privacy Tech Foundation, kemudian oleh Session Technology Foundation.

Session menawarkan beberapa fitur teknis menarik: enkripsi *end-to-end* pada pesan, jaringan terdesentralisasi yang diatur untuk menjamin ketersediaan dan redundansi, serta *onion routing* yang terinspirasi dari Tor. Selain itu, tidak seperti WhatsApp atau Signal yang memerlukan nomor telepon untuk pendaftaran, Session tidak meminta informasi pribadi apa pun (tanpa nomor, tanpa email, hanya sepasang kunci kriptografi).

Session memungkinkan Anda mengirim pesan, file, pesan suara, panggilan audio, serta grup hingga 100 anggota (dan komunitas lebih dari itu), sekaligus meminimalkan kebocoran metadata.
![Image](assets/fr/01.webp)

Session utamanya ditujukan bagi pengguna yang memprioritaskan kerahasiaan dalam komunikasi mereka. Layanan pesan ini merupakan alternatif yang lebih baik terhadap WhatsApp, dengan arsitektur yang dirancang untuk menghadapi model pengawasan modern.

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

## Instal aplikasi Session

Session tersedia di semua platform. Anda dapat mengunduh aplikasi ini langsung dari toko aplikasi ponsel Anda:
- [Google Play](https://play.google.com/store/apps/details?id=network.loki.messenger);
- [App Store](https://apps.apple.com/us/app/session-private-messenger/id1470168868);
- [F-Droid](https://fdroid.getsession.org/).
  
Di Android, juga dapat [menginstal melalui APK](https://github.com/session-foundation/session-android/releases).

Dalam tutorial ini, kami akan berfokus pada versi seluler. Namun, perlu diketahui bahwa [versi komputer juga tersedia](https://getsession.org/download) (macOS, Linux, dan Windows). Selanjutnya, kami akan membahas cara menyinkronkan akun di berbagai perangkat.

## Buat akun di Session

Saat pertama kali diluncurkan, klik "*Create account*" (Buat akun).

![Image](assets/fr/02.webp)

Pilih nama tampilan untuk profil Anda. Nama ini dapat berupa nama samaran atau nama asli Anda.

![Image](assets/fr/03.webp)

Anda kemudian harus memilih di antara dua mode pengaturan notifikasi:
- Mode Cepat ("*Firebase Cloud Messaging/Apple Push Notification Service*")**: Mode ini memungkinkan Anda menerima notifikasi pesan secara nyaris real-time, berkat layanan notifikasi yang disediakan oleh Google atau Apple (tergantung sistem Anda). Untuk fungsi ini, alamat IP Anda dan ID notifikasi unik akan ditransmisikan kepada Google atau Apple, dan ID akun Session juga akan didaftarkan pada server STF (melalui Tor). Mode ini melibatkan paparan metadata (meskipun minimal), namun tidak mengorbankan konten pesan atau kontak, serta tidak memungkinkan aktivitas Anda yang sebenarnya terlacak. Oleh karena itu, mode ini lebih efisien dalam hal responsivitas, tetapi bergantung pada infrastruktur terpusat dan sedikit kurang efektif dalam hal kerahasiaan.
- Mode Lambat ("*Background Polling*")**: Pada mode ini, aplikasi Session tetap aktif di latar belakang, secara berkala memeriksa jaringan untuk mencari pesan baru. Pendekatan ini menjamin kerahasiaan yang lebih tinggi dibandingkan mode cepat, karena tidak ada data yang ditransmisikan kepada server pihak ketiga; baik Google, Apple, maupun server STF tidak menerima informasi apa pun. Di sisi lain, mode ini memiliki dua kekurangan: notifikasi dapat tertunda (hingga beberapa menit), dan konsumsi energi umumnya lebih tinggi akibat aktivitas aplikasi di latar belakang.

![Image](assets/fr/04.webp)

Anda sekarang terhubung ke aplikasi Session dan dapat mulai bertukar pesan.

![Image](assets/fr/05.webp)

## Simpan akun Session Anda

Hal pertama yang harus dilakukan sebelum Anda mulai menggunakan Session adalah menyimpan akun Anda sehingga Anda dapat memulihkannya jika Anda kehilangan perangkat. Untuk melakukannya, klik tombol "*Continue*" di samping "*Simpan kata sandi pemulihan Anda*".

Sebelum Anda mulai menggunakan Session, hal pertama yang harus dilakukan adalah menyimpan akun Anda. Ini penting agar Anda dapat memulihkannya jika kehilangan perangkat. Untuk melakukannya, klik tombol "*Continue*" (lanjutkan) di samping "*Save your recovery password*" (Simpan kata sandi pemulihan Anda".)

![Image](assets/fr/06.webp)

Session kemudian akan menampilkan frasa mnemonik. Salin frasa tersebut dengan hati-hati dan simpan di tempat yang aman. Frasa ini menyediakan akses penuh ke akun Session Anda, sehingga sangat penting untuk tidak mengungkapkannya. Anda akan membutuhkannya untuk mengakses akun Anda pada perangkat lain, terutama jika ponsel Anda saat ini hilang atau diganti.

![Image](assets/fr/07.webp)

Frasa ini berfungsi serupa dengan frasa mnemonik yang digunakan dalam dompet Bitcoin. Oleh karena itu, saya merekomendasikan Anda untuk melihat tutorial lain ini, di mana saya menjelaskan praktik terbaik untuk menyimpan frasa mnemonik:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Harap diperhatikan**: Tidak seperti frasa Mnemonic yang digunakan pada dompet Bitcoin, pada Session, **Anda harus menyimpan setiap kata secara keseluruhan**. Empat huruf pertama saja tidak cukup!



## Menyiapkan aplikasi Sesi



Untuk mengakses pengaturan aplikasi, klik pada foto profil Anda di kiri atas Interface. Di sinilah Anda dapat menambahkan foto profil.


## Pengaturan pada aplikasi Session

Untuk mengakses pengaturan aplikasi, klik pada foto profil Anda di kiri atas tampilan layar. Di sinilah Anda dapat menambahkan foto profil.
![Image](assets/fr/08.webp)



Dalam menu "*Privacy*", Anda dapat mengaktifkan atau menonaktifkan berbagai fitur (hati-hati, beberapa fitur dapat mengekspos IP Address Anda). Saya juga merekomendasikan untuk mengaktifkan opsi "*Lock App*", yang memerlukan autentikasi untuk mengakses aplikasi.



![Image](assets/fr/09.webp)



Pada menu "*Notification*", Anda akan menemukan pilihan antara "*Fast Mode*" dan "*Slow Mode*" (lihat bagian tutorial sebelumnya). Anda juga dapat menyesuaikan notifikasi agar sesuai dengan preferensi Anda.



![Image](assets/fr/10.webp)



Terakhir, masuk ke menu "*Penampilan*" untuk menyesuaikan Interface dengan selera Anda. Menu "*Recovery Password*" memungkinkan Anda untuk mengambil frasa Mnemonic jika Anda ingin membuat cadangan baru.



![Image](assets/fr/11.webp)

## Mengirim pesan dengan Session


## Mengirim pesan dengan Session



Untuk menghubungi orang lain, klik tombol "*+*" di halaman beranda.



![Image](assets/fr/12.webp)



Tersedia beberapa opsi. Jika Anda ingin membuat atau bergabung dengan grup, pilih "*Buat Grup*" atau "*Gabung Komunitas*".



![Image](assets/fr/13.webp)



Jika Anda ingin seseorang menambahkan Anda sebagai kontak, Anda dapat meminta mereka memindai ID Sesi Anda sebagai kode QR.



![Image](assets/fr/14.webp)



Untuk mengirim login Anda dari jarak jauh, klik "*Unggah Teman*". Anda kemudian dapat menyalin ID Sesi Anda dan mengirimkannya melalui saluran komunikasi lain. Anda juga dapat mengambil informasi ini dengan mengeklik foto profil Anda dari halaman beranda.



![Image](assets/fr/15.webp)



Jika Anda memiliki ID Sesi orang lain dan ingin menambahkannya, klik "*Pesan Baru*".



![Image](assets/fr/16.webp)



Anda kemudian dapat menempelkan pengenalnya dalam teks, atau memindainya secara langsung jika Anda memilikinya dalam bentuk kode QR.



![Image](assets/fr/17.webp)



Kemudian kirimkan pesan awal ke orang ini.



![Image](assets/fr/18.webp)



Segera setelah orang tersebut menerima permintaan Anda, Anda akan melihat nama pengguna mereka muncul, dan Anda akan dapat mengobrol dengan bebas dengannya.



![Image](assets/fr/19.webp)

## Menyinkronkan perangkat lunak Desktop

Untuk menyinkronkan akun Anda di komputer, Anda perlu menginstal perangkat lunak resminya. [Unduh dari situs web resmi](https://getsession.org/download). Saya menyarankan Anda untuk memeriksa keaslian dan integritasnya sebelum menginstalnya.

![Image](assets/fr/20.webp)

Saat pertama kali dijalankan, klik "*I have an account*" (Saya memiliki akun).

![Image](assets/fr/21.webp)

Masukkan frasa Mnemonic Anda, pastikan untuk diberi spasi di antara setiap kata.

![Image](assets/fr/22.webp)

Sekarang Anda dapat mengakses percakapan Anda dari komputer.

![Image](assets/fr/23.webp)

Selamat, Anda sekarang sudah mahir menggunakan aplikasi Session, sebuah alternatif yang sangat baik dari pada WathsApp!
Saya juga merekomendasikan tutorial lain ini, di mana saya menjelaskan tentang Threema, alternatif lain yang menarik untuk aplikasi kirim pesan Anda:

https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74
