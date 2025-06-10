---
name: Sinyal
description: Ekspresikan diri Anda dengan bebas
---
![cover](assets/cover.webp)



Signal adalah aplikasi perpesanan terenkripsi ujung ke ujung, yang dirancang untuk menawarkan kerahasiaan yang baik secara default. Setiap pesan, panggilan, dan file dilindungi oleh protokol Signal, yang dikenal sebagai salah satu protokol perpesanan yang paling kuat. Protokol ini digunakan kembali oleh banyak aplikasi lain, termasuk WathsApp, Facebook Messenger, Skype, dan Google Messages untuk komunikasi RCS.



Signal diluncurkan pada tahun 2014 oleh Moxie Marlinspike (nama samaran) dan dikembangkan sejak tahun 2018 oleh Signal Foundation, sebuah organisasi nirlaba yang didirikan dengan dukungan Brian Acton (salah satu pendiri WhatsApp).



![Image](assets/fr/01.webp)



Dibandingkan dengan WhatsApp, Signal menonjol dalam hal transparansi: kode aplikasi, baik dari sisi klien maupun server, sepenuhnya open source. Hal ini memungkinkan siapa pun untuk mengauditnya, dan khususnya untuk memeriksa apakah enkripsi diterapkan seperti yang diiklankan.



Namun, Signal bergantung pada penggunaan nomor telepon, yang merupakan kelemahan utamanya dalam hal anonimitas dibandingkan dengan solusi lainnya. Meskipun demikian, aplikasi ini, menurut pendapat saya, salah satu yang paling dapat diandalkan dalam hal keamanan dan kerahasiaan, berkat arsitekturnya yang sepenuhnya terbuka dan protokol enkripsi yang diadopsi secara luas, dan oleh karena itu telah diuji dan diaudit, tidak seperti aplikasi lain yang lebih marjinal.



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




## Instal aplikasi Signal



Signal tersedia di semua platform. Anda dapat mengunduh aplikasi ini langsung dari toko aplikasi ponsel Anda:




- [Google Play](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms);
- [App Store](https://apps.apple.com/us/app/signal-private-messenger/id874139669);



Di Android, juga memungkinkan untuk [menginstal melalui APK](https://github.com/signalapp/Signal-Android/releases).



Dalam tutorial ini, kami akan berkonsentrasi pada versi seluler, tetapi harap dicatat bahwa [versi desktop juga tersedia] (https://signal.org/fr/download/) (MacOS, Linux, dan Windows). Namun, Anda harus menyiapkan aplikasi seluler terlebih dahulu sebelum Anda dapat menyinkronkan akun Anda dengan versi desktop.



## Buat akun di Signal



Apabila Anda meluncurkan aplikasi untuk pertama kali, klik tombol "*Lanjutkan*".



![Image](assets/fr/02.webp)



Masukkan nomor telepon Anda, lalu klik "*Next*".



![Image](assets/fr/03.webp)



Kode verifikasi akan dikirimkan kepada Anda melalui SMS. Masukkan kode ini di aplikasi Signal.



![Image](assets/fr/04.webp)



Pilih kode PIN untuk mengamankan akun Signal Anda. Kode ini mengenkripsi data Anda, dan dapat digunakan untuk memulihkan akses ke akun Anda jika perangkat Anda hilang. Jadi, penting untuk memilih kode PIN yang kuat, yang panjang dan acak, serta menyimpan catatan yang dapat diandalkan.



![Image](assets/fr/05.webp)



Konfirmasikan kode PIN ini untuk kedua kalinya.



![Image](assets/fr/06.webp)



Sekarang Anda dapat mempersonalisasi profil pengguna Anda. Pilih foto, masukkan nama Anda atau nama panggilan. Pada tahap ini, Anda juga dapat menentukan siapa saja yang dapat menemukan Anda di Signal melalui nomor Anda. Pilih "*Semua orang*" jika Anda ingin terlihat, atau "*Tidak ada orang*" untuk tetap tidak dapat dilacak melalui nomor telepon (Anda hanya dapat ditambahkan dengan "*Nama Pengguna*"). Setelah Anda menentukan pilihan, klik "*Selanjutnya*".



![Image](assets/fr/07.webp)



Anda sekarang terhubung ke Signal dan siap untuk mengirim pesan Exchange.



![Image](assets/fr/08.webp)



## Menyiapkan akun Signal Anda



Klik pada foto profil Anda di sudut kiri atas untuk mengakses pengaturan aplikasi.



![Image](assets/fr/09.webp)



Menu "*Akun*" memungkinkan Anda mengelola pengaturan profil Anda. Saya menyarankan Anda untuk mempertahankan pengaturan default. Anda juga dapat mengaktifkan opsi "*Kunci Registrasi*", yang melindungi akun Anda dari jenis serangan tertentu. Menu ini juga berisi opsi yang Anda perlukan untuk mentransfer akun Anda ke perangkat baru.



![Image](assets/fr/10.webp)



Mengklik lagi gambar profil Anda dalam pengaturan akan membawa Anda ke opsi untuk mempersonalisasi profil Anda. Saya sarankan Anda menetapkan "*Username*": ini akan memungkinkan Anda untuk berhubungan dengan orang lain tanpa memperlihatkan nomor telepon Anda.



![Image](assets/fr/11.webp)



Dengan memilih "*Kode QR atau tautan*", Anda akan mendapatkan informasi yang Anda perlukan untuk dibagikan kepada seseorang yang ingin menambahkan Anda ke Signal.



![Image](assets/fr/12.webp)



Menu "*Privacy*" sangat penting. Di sini Anda akan menemukan opsi untuk mengontrol visibilitas nomor Anda, pengelolaan pesan dengan kontak Anda, serta berbagai otorisasi yang diberikan pada aplikasi.



![Image](assets/fr/13.webp)



Dan jangan ragu untuk menjelajahi menu "*Tampilan*", "*Obrolan*" dan "*Pemberitahuan*" untuk menyesuaikan Interface dan pengoperasian aplikasi dengan kebutuhan pribadi Anda.



## Hubungkan aplikasi desktop



Untuk menghubungkan aplikasi desktop, mulailah dengan menginstal perangkat lunak di komputer Anda (lihat bagian pertama tutorial ini). Kemudian, pada ponsel Anda, buka Pengaturan dan buka bagian "*Perangkat yang ditautkan*".



![Image](assets/fr/14.webp)



Klik tombol "*Tautkan perangkat baru*".



![Image](assets/fr/15.webp)



Di komputer Anda, luncurkan perangkat lunak, lalu pindai kode QR yang ditampilkan di layar menggunakan ponsel Anda. Jika Anda ingin mengimpor percakapan Anda, pilih opsi "*Transfer riwayat pesan*".



![Image](assets/fr/16.webp)



Perangkat Anda sekarang telah tersinkronisasi sepenuhnya.



![Image](assets/fr/17.webp)



## Mengirim pesan dengan Signal



Untuk berkomunikasi dengan seseorang di Signal, pertama-tama Anda harus menambahkannya sebagai kontak. Terdapat beberapa pilihan: Anda dapat menambahkannya melalui nomor telepon mereka (jika orang tersebut telah mengaktifkan pilihan untuk ditemukan dengan cara ini), atau menggunakan Signal ID mereka.



Klik ikon pensil di sudut kanan bawah Interface.



![Image](assets/fr/18.webp)



Dalam kasus saya, saya ingin menambahkan orang berdasarkan nama pengguna. Jadi saya klik "*Temukan berdasarkan nama pengguna*".



![Image](assets/fr/19.webp)



Anda kemudian dapat menempelkan login atau memindai kode QR-nya.



![Image](assets/fr/20.webp)



Kirimkan pesan kepadanya untuk menjalin kontak.



![Image](assets/fr/21.webp)



Percakapan kemudian akan muncul di halaman beranda. Jika orang tersebut menerima permintaan kontak Anda, Anda akan melihat nama dan foto profilnya.



![Image](assets/fr/22.webp)



Selamat, Anda sekarang sudah mahir menggunakan perpesanan Signal, sebuah alternatif yang bagus untuk WathsApp! Jika Anda merasa tutorial ini bermanfaat, saya akan sangat berterima kasih jika Anda memberikan tanda jempol Green di bawah ini. Jangan ragu untuk membagikan tutorial ini di jejaring sosial Anda. Terima kasih banyak!



Saya juga merekomendasikan tutorial lain ini, di mana saya memperkenalkan Anda pada Proton Mail, sebuah alternatif yang jauh lebih ramah privasi daripada Gmail:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2