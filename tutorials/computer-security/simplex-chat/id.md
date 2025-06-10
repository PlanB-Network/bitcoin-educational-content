---
name: Obrolan SimpleX
description: Kotak surat pertama tanpa ID pengguna
---
![cover](assets/cover.webp)



Diluncurkan pada tahun 2021, SimpleX adalah aplikasi perpesanan instan gratis dengan pendekatan privasi yang sangat berbeda. Tidak seperti WhatsApp, Signal, dan layanan perpesanan terpusat lainnya, SimpleX menonjol dalam hal manajemen penggunanya: tidak ada pengidentifikasi pengguna, nama samaran, nomor, atau kunci publik yang terlihat. Ketiadaan pengenal ini membuat hampir tidak mungkin untuk menghubungkan pengguna, menjamin tingkat privasi yang tinggi.



Tidak seperti kebanyakan aplikasi yang membutuhkan akun atau nomor telepon, SimpleX memungkinkan Anda memulai percakapan dengan membagikan tautan atau kode QR sementara. Setiap tautan menciptakan saluran terenkripsi yang unik, dan kontak tidak dapat menemukan atau menghubungi kembali pengirim tanpa Exchange eksplisit. Pesan dienkripsi dari ujung ke ujung, dan melewati server relai yang menghapusnya setelah pengiriman, dan tidak melihat pengirim maupun penerima, atau kunci mereka.



![Image](assets/fr/01.webp)



Arsitektur jaringan sepenuhnya terdesentralisasi dan tidak terpusat: server tidak mengenal satu sama lain, tidak menyimpan direktori global, dan tidak meng-host profil pengguna apa pun. Lebih baik lagi, setiap pengguna bisa menyebarkan dan menggunakan server relai mereka sendiri, sambil tetap bisa dioperasikan dengan yang ada di jaringan publik.



SimpleX sepenuhnya sumber terbuka (klien, protokol dan server), tersedia di Android, iOS, Linux, Windows dan macOS. Penyimpanan lokalnya terenkripsi dan portabel, sehingga Anda bisa mentransfer profil dari satu perangkat ke perangkat lainnya tanpa bergantung pada server terpusat.



SimpleX mengintegrasikan semua fitur klasik aplikasi perpesanan. Namun, ergonominya tetap kurang lancar dibandingkan dengan WhatsApp atau Signal. Aplikasi ini juga bisa lebih ketat dalam penggunaannya, terutama saat menambahkan kontak. Jadi, menurut saya, SimpleX adalah alternatif yang relevan untuk WhatsApp atau Signal bagi pengguna yang menempatkan kerahasiaan sebagai prioritas utama, dan yang siap, karena alasan itu, untuk memberikan sedikit kelonggaran pada kenyamanan pengguna sehari-hari.



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



## Instal aplikasi SimpleX Chat



SimpleX Chat tersedia di semua platform. Anda dapat mengunduh aplikasi ini langsung dari toko aplikasi ponsel Anda:




- [Google Play](https://play.google.com/store/apps/details?id=chat.simplex.app);
- [App Store](https://apps.apple.com/us/app/simplex-chat-secure-messenger/id1605771084);
- [F-Droid](https://simplex.chat/fdroid/).



Di Android, juga memungkinkan untuk [menginstal melalui APK](https://github.com/simplex-chat/simplex-chat/releases).



Dalam tutorial ini, kami akan berkonsentrasi pada versi seluler, tetapi harap dicatat bahwa [versi desktop juga tersedia] (https://simplex.chat/downloads/) (MacOS, Linux, dan Windows). Anda dapat menautkan versi desktop ke profil pengguna seluler yang sudah ada, tetapi agar sinkronisasi ini berfungsi, kedua perangkat harus terhubung ke jaringan lokal yang sama.



![Image](assets/fr/02.webp)



## Buat akun di SimpleX Chat



Ketika Anda pertama kali meluncurkan aplikasi, klik tombol "*Buat profil Anda*".



![Image](assets/fr/03.webp)



Pilih nama pengguna, yang dapat berupa nama asli atau nama samaran, lalu klik "*Buat*".



![Image](assets/fr/04.webp)



Selanjutnya, atur frekuensi aplikasi akan memeriksa pesan baru. Jika daya tahan baterai ponsel Anda tidak menjadi masalah, pilih "*Instant*" untuk menerima pesan secara langsung. Jika Anda lebih suka menghemat baterai dan mencegah aplikasi berjalan di latar belakang, pilih "*Saat aplikasi berjalan*": Anda hanya akan menerima pesan saat aplikasi terbuka. Kompromi yang mungkin dilakukan adalah memilih pemeriksaan berkala setiap 10 menit.



Setelah Anda menentukan pilihan, klik "*Gunakan obrolan*".



![Image](assets/fr/05.webp)



Anda sekarang terhubung ke SimpleX Chat dan siap untuk mulai mengobrol.



![Image](assets/fr/06.webp)



## Menyiapkan Obrolan SimpleX



Pertama-tama, akses pengaturan dengan mengeklik foto profil Anda di sudut kanan bawah, kemudian "*Settings*".



![Image](assets/fr/07.webp)



Pengaturan default pada umumnya sesuai untuk sebagian besar pengguna. Namun, saya sarankan Anda untuk membuka menu "*Database passphrase & export*". Di sinilah Anda bisa mengekspor basis data akun SimpleX Anda untuk tujuan pencadangan.



Anda juga dapat memodifikasi passphrase yang digunakan untuk mengenkripsi basis data ini. Secara default, basis data ini dibuat secara acak dan disimpan secara lokal pada perangkat Anda. Jika Anda mau, Anda dapat menentukan passphrase Anda sendiri dan menghapus cadangan passphrase lokal: Anda harus memasukkannya secara manual setiap kali Anda membuka aplikasi, dan juga ketika Anda bermigrasi ke perangkat lain.



**Harap diperhatikan**: jika Anda memilih opsi ini, hilangnya passphrase akan mengakibatkan hilangnya semua profil dan pesan SimpleX Anda secara permanen.



![Image](assets/fr/08.webp)



Saya juga menyarankan Anda untuk membuka menu "*Privacy & security*", di mana Anda dapat mengaktifkan opsi "*SimpleX Lock*". Ini melindungi akses ke aplikasi dengan kode kunci.



![Image](assets/fr/09.webp)



Terakhir, menu "*Notifikasi*" dan "*Penampilan*" memungkinkan Anda menyesuaikan SimpleX Chat agar sesuai dengan preferensi Anda.



![Image](assets/fr/10.webp)



## Mengirim pesan dengan SimpleX Chat



Untuk terhubung dengan orang lain di SimpleX, Anda memiliki dua opsi:




- Gunakan tautan sekali pakai;
- Gunakan Address statis yang dapat digunakan kembali.



Address statis memungkinkan siapa pun yang mengetahuinya untuk menghubungi Anda di SimpleX. Ini adalah Address yang persisten, yang dapat digunakan beberapa kali, oleh orang yang berbeda, tanpa batas waktu. Kegigihan inilah yang membuatnya lebih rentan terhadap spam. Namun, tidak seperti aplikasi perpesanan lainnya, menghapus SimpleX Address Anda sudah cukup untuk menghentikan semua spam, tanpa mempengaruhi percakapan yang ada. Faktanya, Address ini hanya digunakan untuk membuat koneksi awal, dan tidak lagi diperlukan setelah Exchange dimulai.



Tautan sekali pakai, di sisi lain, hanya dapat digunakan sekali, oleh pengguna mana pun. Setelah kontak menggunakannya, tautan menjadi tidak valid. Anda harus membuat tautan baru untuk setiap koneksi baru.



### Dengan Address statis



Jika Anda ingin menggunakan Address, klik gambar profil Anda di bagian kiri bawah Interface, lalu pilih "*Create SimpleX Address*". Kemudian klik "*Buat SimpleX Address*" sekali lagi.



![Image](assets/fr/11.webp)



Address Anda yang dapat digunakan kembali sekarang telah dibuat. Anda dapat membagikannya kepada orang-orang yang ingin menghubungi Anda, baik dengan menunjukkan kode QR, atau dengan mengirimkan tautannya kepada mereka.



![Image](assets/fr/12.webp)



Klik tombol "*Pengaturan Address*". Di sini Anda dapat mengonfigurasi izin yang terkait dengan Address Anda. Opsi "*Berbagi dengan kontak*" membuat Address Anda dapat dilihat pada profil SimpleX Anda. Kontak Anda kemudian akan dapat melihat dan meneruskannya kepada orang lain yang ingin menghubungi Anda.



Opsi "*Auto-accept*" secara otomatis menerima koneksi yang masuk melalui Address Anda. Ini berarti bahwa siapa pun yang memiliki Address Anda akan dapat melihat profil Anda dan mengirimkan pesan kepada Anda, kecuali jika Anda mengaktifkan opsi "*Accept incognito*". Opsi ini akan menyembunyikan nama dan foto profil Anda ketika koneksi baru dibuat, dan menggantinya dengan nama samaran acak, yang berbeda untuk setiap lawan bicara.



![Image](assets/fr/13.webp)



### Dengan tautan yang dapat digunakan kembali



Cara kedua untuk terhubung dengan seseorang adalah dengan membuat tautan satu kali. Untuk melakukannya, klik ikon pensil di sudut kanan bawah Interface, lalu pilih "*Create 1-time link*".



Jika kontak Anda telah mengirimi Anda tautan, klik "*Pindai / Tempel tautan*" untuk memindai atau menempelkannya.



![Image](assets/fr/14.webp)



SimpleX kemudian menghasilkan tautan sekali pakai. Anda dapat meneruskannya ke kontak Anda dengan cara apa pun: Exchange fisik, pesan lain, dll.



![Image](assets/fr/15.webp)



Anda juga dapat memilih profil mana yang akan dikaitkan dengan tautan undangan ini. Untuk melakukannya, klik profil Anda tepat di bawah kode QR. Anda kemudian akan dapat :




- pilih salah satu profil Anda yang sudah ada (kita akan melihat cara membuat beberapa profil di bagian berikutnya);
- atau pilih mode "*Incognito*", yang menyembunyikan nama dan foto profil Anda dengan nama samaran yang dibuat secara acak untuk koresponden Anda.



Di sini, saya memilih mode "*Incognito*".



![Image](assets/fr/16.webp)



Kontak saya menggunakan tautan tersebut. Sementara itu, dia tidak mengaktifkan mode "*Incognito*", itulah sebabnya saya melihat nama profilnya, "*Bob*". Di sisi lain, Bob tidak melihat nama asli saya "*Loïc Morel*", tetapi nama samaran acak, dalam hal ini "*RealSynergy*".



![Image](assets/fr/17.webp)



Saya bisa langsung mulai mengobrol, tetapi pertama-tama saya ingin memastikan bahwa saya berbicara dengan Bob, dan bukan dengan orang jahat yang mungkin telah menyadap tautan atau melakukan serangan MITM.



Untuk melakukan ini, kita akan memeriksa tautan keamanan **di luar aplikasi**. Ini penting, karena jika terjadi serangan MITM, verifikasi internal akan terganggu. Jadi, gunakan sistem perpesanan lain yang aman, atau lebih baik lagi, periksa kodenya secara langsung.



Dalam obrolan, klik pada foto Bob, lalu pada "*Verifikasi kode keamanan*". Bob harus melakukan hal yang sama di sisinya.



![Image](assets/fr/18.webp)



Jika Anda bekerja dari jarak jauh, bandingkan kode pada sistem perpesanan aman lainnya (keduanya harus sama). Atau lebih baik lagi, jika Anda bisa bertemu langsung, pindai kode QR kontak Anda dengan mengeklik "*Pindai kode*".



![Image](assets/fr/19.webp)



Jika verifikasi berhasil, ikon perisai dengan tanda centang akan muncul di sebelah nama kontak Anda. Ini adalah jaminan bahwa Anda sedang melakukan pertukaran dengan Bob. Jika verifikasi tidak berhasil, peringatan "*Kode keamanan salah!*" akan muncul.



![Image](assets/fr/20.webp)



Anda sekarang dapat dengan bebas Exchange pesan, panggilan, dan file dengan Bob, tergantung pada izin yang Anda tetapkan untuk percakapan ini.



## Sesuaikan profil SimpleX Chat Anda



Salah satu fitur SimpleX yang paling hebat adalah kemampuan untuk mengelola beberapa profil pengguna yang benar-benar terpisah, semuanya dapat diakses dari akun lokal yang sama. Hal ini memungkinkan Anda untuk memisahkan identitas Anda yang berbeda dengan rapi, tanpa manajemen pesan yang rumit.



Contohnya, Anda bisa membuat file :




- Profil dengan nama asli dan foto asli untuk pertukaran profesional Anda;
- Profil dengan nama asli Anda dan foto lucu untuk pertukaran keluarga Anda;
- Profil dengan foto palsu dan nama samaran untuk percakapan pribadi Anda;
- Profil pseudonim lain untuk mengobrol dengan orang asing.



Itulah yang akan kita lakukan di sini. Saya mulai dengan mengonfigurasi profil utama saya, yang ditautkan ke identitas asli saya. Untuk melakukannya, saya klik pada foto profil saya di sudut kanan bawah, lalu pada nama pengguna saya.



![Image](assets/fr/21.webp)



Saya kemudian mengeklik foto profil saya untuk mengubahnya dan menambahkan foto baru.



![Image](assets/fr/22.webp)



Untuk menambahkan profil lain, klik menu "*Profil obrolan Anda*".



![Image](assets/fr/23.webp)



Di sini Anda akan melihat semua profil Anda. Klik "*Tambah profil*" untuk membuat profil baru.



![Image](assets/fr/24.webp)



Kemudian pilih informasi untuk profil baru Anda: nama, foto, dll. Di sini, saya menggunakan nama samaran dan gambar yang berbeda untuk menyembunyikan identitas asli saya di bursa tertentu.



![Image](assets/fr/25.webp)



Dengan menahan jari Anda pada profil, Anda dapat menyembunyikannya. Hal ini akan membuatnya tidak terlihat dalam aplikasi, bersama dengan semua percakapan terkait. Anda juga dapat memilih untuk "*Mute*" untuk berhenti menerima pemberitahuan.



![Image](assets/fr/26.webp)



Setelah Anda membuat profil, Anda dapat mengelolanya secara mandiri. Dari halaman beranda, cukup pilih profil yang aktif untuk ditampilkan.



![Image](assets/fr/27.webp)



Ketika Anda membuat tautan undangan atau Address statis, Anda sekarang dapat memilih profil mana yang akan dikaitkan dengannya. Misalnya, jika saya memilih profil "*Satoshi Nakamoto*" untuk tautan generate dan mengirimkannya ke Alice, dia hanya akan melihat identitas pseudonim saya "*Satoshi Nakamoto*", tanpa mengetahui identitas asli saya "*Loïc Morel*". Sebaliknya, jika saya memberinya tautan dari profil asli saya, dia tidak akan bisa menautkan ke profil pseudonim saya.



![Image](assets/fr/28.webp)



Selamat, Anda sekarang sudah bisa menggunakan perpesanan SimpleX, sebuah alternatif yang sangat baik untuk WathsApp!



Saya juga merekomendasikan tutorial lain ini, di mana saya menyajikan Threema, alternatif lain yang menarik untuk aplikasi perpesanan Anda:



https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74