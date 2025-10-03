---
name: SimpleX Chat
description: Kotak surat pertama tanpa ID pengguna
---
![cover](assets/cover.webp)

Diluncurkan pada tahun 2021, SimpleX adalah aplikasi pesan instan gratis dengan pendekatan privasi yang sangat berbeda. Tidak seperti WhatsApp, Signal, dan layanan kirim pesan terpusat lainnya, SimpleX unggul dalam pengelolaan penggunanya: tidak ada pengenal pengguna, nama samaran, nomor, atau kunci publik yang terlihat. Tidak adanya pengenal ini membuat hampir tidak mungkin untuk mengungkap pengguna, sehingga menjamin tingkat privasi yang tinggi.

Berbeda dengan sebagian besar aplikasi yang memerlukan akun atau nomor telepon, SimpleX memungkinkan Anda memulai percakapan dengan membagikan tautan atau kode QR sementara. Setiap tautan menciptakan saluran terenkripsi yang unik, dan kontak tidak dapat menemukan atau menghubungi kembali pengirim tanpa pertukaran eksplisit. Pesan dienkripsi dari ujung ke ujung (end-to-end), dan melewati server relai yang menghapus pesan setelah pengiriman, serta tidak melihat pengirim, penerima, maupun kunci mereka.
![Image](assets/fr/01.webp)

Arsitektur jaringannya sepenuhnya terdesentralisasi dan tidak terpusat: server tidak saling mengenal, tidak menyimpan direktori global, dan tidak menghosting profil pengguna. Lebih baik lagi, setiap pengguna dapat menyebarkan dan menggunakan server relai mereka sendiri, sembari tetap dapat beroperasi dengan server yang ada di jaringan publik.

SimpleX sepenuhnya open source (klien, protokol dan server), tersedia di Android, iOS, Linux, Windows dan macOS. Penyimpanan lokalnya terenkripsi dan portabel, sehingga Anda bisa mentransfer profil dari satu perangkat ke perangkat lainnya tanpa bergantung pada server terpusat.

SimpleX mengintegrasikan semua fitur klasik aplikasi kirim pesan. Namun, ergonomisnya tetap kurang lancar dibandingkan WhatsApp atau Signal. Penggunaannya juga bisa lebih membatasi, terutama saat menambahkan kontak. Jadi, menurut saya, SimpleX adalah alternatif yang relevan untuk WhatsApp atau Signal bagi pengguna yang menempatkan privasi sebagai inti prioritas mereka, dan yang bersedia, karena alasan tersebut, untuk membuat beberapa kelonggaran pada kenyamanan penggunaan sehari-hari.

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

## Instalasi Aplikasi SimpleX Chat

SimpleX Chat tersedia di semua platform. Anda dapat mengunduh aplikasi ini langsung dari toko aplikasi ponsel Anda:
- [Google Play](https://play.google.com/store/apps/details?id=chat.simplex.app);
- [App Store](https://apps.apple.com/us/app/simplex-chat-secure-messenger/id1605771084);
- [F-Droid](https://simplex.chat/fdroid/).
- 
Di Android, juga memungkinkan untuk [menginstal melalui APK](https://github.com/simplex-chat/simplex-chat/releases).

Dalam tutorial ini, kita akan fokus pada versi seluler. Namun, perlu diingat bahwa [versi desktop juga tersedia](https://simplex.chat/downloads/) (MacOS, Linux, dan Windows). Anda bisa menautkan versi desktop ke profil pengguna seluler yang sudah ada, tapi untuk sinkronisasi ini, kedua perangkat harus terhubung ke jaringan lokal yang sama.
![Image](assets/fr/02.webp)

## Buat Akun di SimpleX Chat

Ketika Anda pertama kali meluncurkan aplikasi, klik tombol "_Create your profile_" (Buat profl anda).
![Image](assets/fr/03.webp)

Pilih nama pengguna, yang dapat berupa nama asli atau nama samaran, lalu klik "_Create_" (Buat).
![Image](assets/fr/04.webp)

Selanjutnya, atur frekuensi aplikasi memeriksa pesan baru. Jika daya tahan baterai ponsel Anda bukan masalah, pilih "_Instant_" (Instant) untuk menerima pesan secara real-time. Jika Anda ingin menghemat baterai dan mencegah aplikasi berjalan di latar belakang, pilih "_When app is running_" (Saat aplikasi berjalan): Anda hanya akan menerima pesan saat aplikasi dibuka. Kondisi yang mungkin adalah memilih pemeriksaan berkala setiap 10 menit.

Setelah Anda menentukan pilihan, klik "_Use Chat_" (Gunakan obrolan).
![Image](assets/fr/05.webp)

Anda sekarang terhubung ke SimpleX Chat dan siap untuk mulai mengobrol.
![Image](assets/fr/06.webp)

## Menyiapkan Obrolan SimpleX

Pertama-tama, akses pengaturan dengan mengeklik foto profil Anda di sudut kanan bawah, kemudian "*Settings*" (Pengaturan).
![Image](assets/fr/07.webp)

Pengaturan default umumnya cocok untuk sebagian besar pengguna. Namun, saya menyarankan Anda untuk masuk ke menu "_Database passphrase & export_". Di sinilah Anda dapat mengekspor database akun SimpleX Anda untuk tujuan pencadangan.

Anda juga dapat mengubah passphrase yang digunakan untuk mengenkripsi database ini. Secara default, passphrase ini dibuat secara acak dan disimpan secara lokal di perangkat Anda. Jika Anda mau, Anda bisa menentukan passphrase Anda sendiri dan menghapus cadangan passphrase lokal: Anda kemudian harus memasukkannya secara manual setiap kali Anda membuka aplikasi, serta saat Anda bermigrasi ke perangkat lain.

**Harap diperhatikan**: jika Anda memilih opsi ini, hilangnya passphrase akan mengakibatkan hilangnya semua profil dan pesan SimpleX Anda secara permanen.
![Image](assets/fr/08.webp)

Saya juga menyarankan Anda untuk membuka menu "*Privacy & security*" (Privasi dan keamanan), di mana Anda dapat mengaktifkan opsi "*SimpleX Lock*" (Kunci SimpleX). Ini melindungi akses ke aplikasi dengan kode kunci.
![Image](assets/fr/09.webp)

Terakhir, menu "*Notifications*" (Notifikasi) dan "*Appearance*" (tampilan) memungkinkan Anda menyesuaikan SimpleX Chat agar sesuai dengan kesukaan Anda.
![Image](assets/fr/10.webp)

## Mengirim pesan dengan SimpleX Chat

Untuk terhubung dengan orang lain di SimpleX, Anda memiliki dua opsi:
- Gunakan tautan sekali pakai;
- Gunakan alamat statis yang dapat digunakan kembali.

Alamat statis memungkinkan siapa pun yang mengetahuinya untuk menghubungi Anda di SimpleX. Ini adalah alamat yang sama, yang dapat digunakan beberapa kali oleh orang yang berbeda, tanpa batasan waktu. Sifat persisten inilah yang membuatnya lebih rentan terhadap spam. Namun, tidak seperti aplikasi kirim pesan lainnya, menghapus alamat SimpleX Anda cukup untuk menghentikan semua spam, tanpa memengaruhi percakapan yang sudah ada. Faktanya, alamat ini hanya digunakan untuk membangun koneksi awal, dan tidak lagi diperlukan setelah percakapan dimulai.

Sementara itu, tautan sekali pakai (single-use links) hanya dapat digunakan sekali oleh satu pengguna. Setelah kontak menggunakannya, tautan tersebut menjadi tidak valid. Anda perlu membuat yang baru untuk setiap koneksi baru.

### Dengan Address statis

Jika Anda ingin menggunakan alamat statis, klik gambar profil Anda di bagian kiri bawah Interface, lalu pilih "*Create SimpleX Address*" (Buat alamat SimpleX). Kemudian klik "*Create SimpleX Address*" (Buat alamat SimpleX) sekali lagi.
![Image](assets/fr/11.webp)

Alamat yang bisa Anda gunakan berulang kali sekarang telah dibuat. Anda bisa membagikannya kepada orang-orang yang ingin menghubungi Anda, baik dengan menunjukkan kode QR, atau dengan mengirimkan tautannya.
![Image](assets/fr/12.webp)

Klik tombol "*Address settings*" (Pengaturan alamat). Di sini Anda dapat mengonfigurasi izin yang terkait dengan alamat Anda. Opsi "_Share with contacts_" (Bagikan dengan kontak) membuat alamat Anda terlihat di profil SimpleX Anda. Kontak Anda kemudian dapat melihatnya dan meneruskannya ke orang lain yang ingin menghubungi Anda.

Opsi "_Auto-accept_" (Terima otomatis) secara otomatis menerima koneksi masuk melalui alamat Anda. Ini berarti siapa pun yang memiliki alamat Anda akan dapat melihat profil Anda dan mengirimi Anda pesan, kecuali jika Anda mengaktifkan opsi "_Accept incognito_" (Terima penyamaran). Ini menyembunyikan nama dan foto profil Anda saat koneksi baru dibuat, menggantinya dengan nama samaran acak, berbeda untuk setiap lawan bicara.
![Image](assets/fr/13.webp)

### Dengan tautan yang dapat digunakan kembali

Cara kedua untuk terhubung dengan seseorang adalah dengan membuat tautan satu kali. Untuk melakukannya, klik ikon pensil di sudut kanan bawah Interface, lalu pilih "*Create 1-time link*".

Cara kedua untuk terhubung dengan seseorang adalah dengan membuat tautan sekali pakai (one-time link). Untuk melakukannya, klik ikon pensil di pojok kanan bawah antarmuka, lalu pilih "_Create 1-time link_" (Buat tautan 1-kali).

Jika kontak Anda telah mengirimi Anda tautan, klik "*Pindai / Tempel tautan*" untuk memindai atau menempelkannya.
![Image](assets/fr/14.webp)

SimpleX akan membuat tautan sekali pakai. Anda bisa meneruskan tautan ini ke kontak Anda melalui cara apa pun yang Anda inginkan: pertukaran langsung, aplikasi pesan lain, dan sebagainya.
![Image](assets/fr/15.webp)

Anda juga bisa memilih profil mana yang akan dikaitkan dengan tautan undangan ini. Caranya, klik profil Anda tepat di bawah kode QR. Anda kemudian dapat:
- pilih salah satu profil Anda yang sudah ada (kita akan melihat cara membuat beberapa profil di bagian berikutnya);
- atau pilih mode "*Incognito*", yang menyembunyikan nama dan foto profil Anda dengan nama samaran yang dibuat secara acak untuk penerima Anda.

Di sini, saya memilih mode "*Incognito*".
![Image](assets/fr/16.webp)

Kontak saya menggunakan tautan tersebut. Sementara itu, dia tidak mengaktifkan mode "*Incognito*", itulah sebabnya saya melihat nama profilnya, "*Bob*". Di sisi lain, Bob tidak melihat nama asli saya "*Loïc Morel*", tetapi nama samaran acak, dalam hal ini "*RealSynergy*".

Kontak saya menggunakan tautan tersebut. Dari sisi dia, dia tidak mengaktifkan mode "*Incognito*", itulah sebabnya saya melihat nama profilnya, "*Bob*". Di sisi lain, Bob tidak melihat nama asli saya "Loïc Morel", melainkan nama samaran acak, dalam kasus ini "*RealSynergy*".
![Image](assets/fr/17.webp)

Saya bisa langsung memulai obrolan, tapi pertama, saya ingin memastikan saya benar-benar berbicara dengan Bob, bukan dengan orang jahat yang mungkin telah menyadap tautan atau melakukan serangan MITM (Man-in-the-Middle).

Untuk melakukan ini, kita akan memeriksa kode keamanan **di luar aplikasi**. Ini penting karena jika terjadi serangan MITM, verifikasi internal di dalam aplikasi akan terganggu. Jadi, gunakan sistem pesan aman lain, atau lebih baik lagi, periksa kode secara langsung.

Dalam obrolan, klik pada foto Bob, lalu pada "*Verifikasi kode keamanan*". Bob harus melakukan hal yang sama di sisinya.
Dalam obrolan, klik pada foto Bob, lalu pilih "_Verify security code_" (Verifikasi kode keamanan). Bob juga harus melakukan hal yang sama di sisi dia.
![Image](assets/fr/18.webp)

Jika Anda bekerja dari jarak jauh, bandingkan kode pada sistem perpesanan aman lainnya (keduanya harus sama). Atau lebih baik lagi, jika Anda bisa bertemu langsung, pindai kode QR kontak Anda dengan mengeklik "*Pindai kode*".

Jika Anda bekerja dari jarak jauh, bandingkan kode-kode tersebut di sistem pesan aman lain (kodenya harus sama). Atau, lebih baik lagi, jika Anda bisa bertemu langsung, pindai kode QR kontak Anda dengan mengeklik "_Scan code_" (Pindai kode).
![Image](assets/fr/19.webp)

Jika verifikasi berhasil, ikon perisai dengan tanda centang akan muncul di sebelah nama kontak Anda. Ini adalah jaminan bahwa Anda sedang melakukan pertukaran dengan Bob. Jika verifikasi tidak berhasil, peringatan "*Kode keamanan salah!*" akan muncul.

Jika verifikasi berhasil, ikon perisai dengan tanda centang akan muncul di sebelah nama kontak Anda. Ini adalah jaminan Anda bahwa Anda sedang berkomunikasi dengan Bob. Jika verifikasi tidak berhasil, peringatan "*Kode keamanan salah!*" akan muncul.
![Image](assets/fr/20.webp)

Anda sekarang dapat dengan bebas kirim pesan, panggilan, dan file dengan Bob, tergantung pada izin yang Anda tetapkan untuk percakapan ini.

## Sesuaikan profil SimpleX Chat Anda

Salah satu fitur yang paling hebat SimpleX adalah kemampuannya untuk mengelola beberapa profil pengguna yang sepenuhnya terpisah, semuanya dapat diakses dari akun lokal yang sama. Ini memungkinkan Anda memisahkan identitas-identitas berbeda Anda dengan rapi, tanpa mempersulit pengelolaan pesan.

Contohnya, Anda bisa membuat file:
- Profil dengan nama asli dan foto asli untuk percakapan profesional Anda;
- Profil dengan nama asli Anda dan foto lucu untuk percakapan keluarga Anda;
- Profil dengan foto palsu dan nama samaran untuk percakapan pribadi Anda;
- Profil samaaran lain untuk mengobrol dengan orang asing.

Itulah yang akan kita lakukan di sini. Saya akan memulai dengan mengonfigurasi profil utama saya, yang terhubung dengan identitas asli saya. Untuk melakukan ini, saya mengeklik foto profil saya di pojok kanan bawah, lalu mengeklik nama pengguna saya.
![Image](assets/fr/21.webp)

Saya kemudian mengklik foto profil saya untuk mengubahnya dan menambahkan foto baru.
![Image](assets/fr/22.webp)

Untuk menambahkan profil lain, klik menu "*Your chats profiles*" (Profil obrolan Anda).
![Image](assets/fr/23.webp)

Di sini Anda akan melihat semua profil Anda. Klik "*Add profile*" (Tambah profil) untuk membuat profil baru.
![Image](assets/fr/24.webp)

Kemudian berikan informasi untuk profil baru Anda: nama, foto, dll. Di sini, saya menggunakan nama samaran dan gambar yang berbeda untuk menyembunyikan identitas asli saya di percakapan tertentu.
![Image](assets/fr/25.webp)

Dengan menekan dan menahan jari Anda pada sebuah profil, Anda dapat menyembunyikannya. Ini akan membuat profil tersebut tidak terlihat di aplikasi, beserta semua percakapan terkait. Anda juga bisa memilih untuk "*Mute*" (Bisukan) untuk berhenti menerima notifikasi.
![Image](assets/fr/26.webp)

Setelah Anda membuat profil, Anda dapat mengelolanya secara mandiri. Dari halaman beranda, cukup pilih profil yang aktif untuk ditampilkan.
![Image](assets/fr/27.webp)

Saat membuat tautan undangan atau alamat statis, Anda sekarang bisa memilih profil mana yang akan dikaitkan dengannya. Misalnya, jika saya memilih profil "*Satoshi Nakamoto*" untuk membuat tautan dan mengirimkannya ke Alice, dia hanya akan melihat identitas nama samaran saya "*Satoshi Nakamoto*", tanpa pernah mengetahui identitas asli saya "Loïc Morel". Sebaliknya, jika saya memberinya tautan dari profil asli saya, dia tidak akan punya cara untuk menautkannya ke profil nama samaran saya.
![Image](assets/fr/28.webp)

Selamat, Anda sekarang sudah bisa menggunakan aplikasi SimpleX, sebuah alternatif yang sangat baik daripada WathsApp!

Saya juga merekomendasikan tutorial lain, di mana saya memperkenalkan Threema, alternatif lain yang menarik untuk aplikasi kirim pesan Anda:

https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74
