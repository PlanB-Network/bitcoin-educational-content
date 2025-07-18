---
name: Simple Login
description: Identitas dilindungi dengan alias
---

![cover](assets/cover.webp)

## Login = Email = Hilangnya Privasi

Di dunia digital, telah menjadi praktik yang wajar untuk memiliki akun untuk setiap platform yang ingin diakses. Setiap layanan ini memerlukan informasi masuk (login), yang umumnya terkait dengan kombinasi nama pengguna (_username_) dan kata sandi (_password_). Seringkali, nama pengguna tersebut adalah alamat email pribadi pengguna.

Apabila seseorang menggunakan alamat email pribadinya untuk setiap login, konsekuensi pertama yang dapat dibayangkan adalah hilangnya privasi, bisa menjadi sangat penting jika alamat tersebut tersusun dari _name.surename@servicename.com_.

Para pengembang program _tools open-source_ telah menciptakan rangkaian paket aplikasi yang tercipta dengan tujuan untuk membantu pengguna memperoleh kembali sedikit privasi: mereka akan dapat masuk,tetapi menggunakan alias, suatu cara yang tidak mengungkapkan identitas pribadi mereka.

Yang paling sederhana di antara yang telah saya coba secara pribadi dan masih saya uji adalah [Simple Login](https://simplelogin.io/).

## Alias

Alias email hanyalah pengganti bagian nama dari alamat email Anda dengan nama fiktif. Bagi pengguna, tidak ada yang berubah; layanan alias meneruskan email ke dan dari alamat email biasa seperti biasa. Setiap orang dapat terus menggunakan kotak masuk mereka seperti biasa, tetapi alih-alih menampilkan nama asli mereka, ia akan menampilkan pengguna yang tidak dapat dikenali. Layanan ini harus efisien, dan sejauh ini, Simple Login telah membuktikannya.

Saat pertama kali mengunjungi situs Simple Login, Anda harus membuat akun (di sini juga!), menggunakan alamat email "resmi". Di sini, Anda harus memasukkan email, kata sandi, dan memecahkan captcha.
![image](assets/it/02.webp)

Simple Login akan mengirimkan pesan verifikasi ke alamat email yang Anda tunjukkan. Disarankan untuk menyalin tautan verifikasi dan menempelkannya ke kolom alamat (address bar), daripada langsung mengeklik tombol verifikasi.
![image](assets/it/03.webp)
![image](assets/it/04.webp)


Dasbor Simple Login langsung terbuka, dengan tutorial singkat untuk navigasi.
![image](assets/it/05.webp)

Perlu dicatat bahwa Simple Login secara otomatis mengaktifkan langganan buletin (newsletter), yang dapat dinonaktifkan dengan perintah yang disediakan.
![image](assets/it/06.webp)

## Pengaturan

Anda bisa langsung melihat pada _Pengaturan_ untuk menemukan fitur-fitur layanan ini. Login Sederhana dimulai dengan semua opsi aktif, termasuk yang _Premium_, yang tetap dapat digunakan selama 10 hari. Setelah masa uji coba selesai, Anda akan memiliki kemungkinan untuk membuat 10 alias dengan profil ini dan Anda dapat langsung menautkan email Proton Anda, karena Simple Login telah diakuisisi oleh penyedia email Swiss.

Anda bisa langsung melihat _Settings_ untuk mengetahui fitur-fitur layanan ini. Simple Login memulai dengan semua opsi aktif, termasuk opsi Premium, yang dapat digunakan selama 10 hari. Setelah masa percobaan berakhir, Anda memungkinkan untuk membuat 10 alias dengan profil ini dan Anda dapat langsung menautkan email Proton Anda, karena Simple Login telah diakuisisi oleh penyedia email asal Swiss tersebut.
![image](assets/it/07.webp)


Anda bisa mengatur serangkaian parameter, atau memeriksa apakah email Anda telah disusupi dalam hal privasi.
![image](assets/it/08.webp)

Terakhir, Anda bisa mengekspor cadangan profil Anda, atau mengimpornya dari penyedia lain.
![image](assets/it/09.webp)

### Email Kantor

Bagi mereka yang menggunakan email dengan domain pribadi sebagai email kerja, mereka dapat mengatur domain pribadi mereka.
![image](assets/it/10.webp)

Dari panel utama, dengan memilih _Mailboxes_, Anda bahkan bisa menambahkan alamat email lain dan juga menggunakan alias yang akan dibuat sesuai. Dalam tutorial ini, contohnya, saya memutuskan untuk membuat profil dengan _mailbox gmail.com_, lalu mengaitkan alamat _proton.me_.
![image](assets/it/11.webp)

Saat menambahkan alamat baru, terutama jika itu milik penyedia Proton, prosedur yang dipandu menunjukkan kemungkinan untuk memasuki mode _sudo_ (pengguna super). Simple Login akan meminta Anda memasukkan kata sandi _mailbox_ ini untuk membuktikan kepemilikan yang sah.

⚠️ **Saya pribadi menyarankan agar Anda tidak melakukan hal ini**. ⚠️
![image](assets/it/12.webp)

**Lebih baik mengakses kotak email -> salin tautan untuk verifikasi dan tempelkan di kolom URL -> dan dapatkan verifikasi tanpa mengungkapkan kata sandi.**
![image](assets/it/13.webp)

Dari kedua alamat yang Anda masukkan, satu akan menjadi alamat utama (default) dan yang lainnya sebagai sekunder. Keduanya dapat dengan mudah ditukar, dan pengaturannya sangat mudah ditemukan di dasbor.
![image](assets/it/14.webp)

Setelah menambahkan email kedua Address (opsional), mari kita lihat apa yang dapat kita lakukan dengan Simple Login.

## Pembuatan Nama Alias

Pada panel, pilihan menu pertama berlabel _Alias_, tempat Anda dapat membuatnya. Anda memiliki opsi untuk menghasilkan alias secara acak dengan mengeklik tombol _Random Alias_ (tombol hijau yang ditunjukkan pada gambar berikut ini). Fitur ini akan membuat alamat email yang unik dan menarik.
![image](assets/it/24.webp)

Jika Anda ingin membedakan layanan dengan memberikan nama yang berbeda, Anda harus memilih _New Custom Alias_ (Alias Kustom Baru) . Dengan begitu, Anda bisa memberi alias tersebut nama layanan yang ingin Anda akses (media sosial, penyedia layanan, acara online, orang asing yang ditemui secara kebetulan, dll.). Sisanya akan ditangani oleh Simple Login.

Untuk pura-pura (tapi sebenarnya tidak), saya memutuskan untuk membuat alias untuk bank dan menamainya `BANK`. Meskipun benar bahwa bank saya tahu segalanya tentang saya, saya merasa lucu bisa berkomunikasi dengan mereka menggunakan alamat email yang tidak bisa mereka pahami. Simple Login memang menghasilkan nama acak, yang dipisahkan oleh `.` dari nama yang kita pilih.

Di sini, alamat email baru bisa menjadi:
- bank.breeding123@aleeas.com
- bank.platter456@slmails.com
- bank.preoccupy789@8shield.net
- dan seterusnya

Seseorang dapat memilih lebih dari satu domain: domain publik tersedia dengan paket gratis, sementara yang lain, yang ditandai sebagai privat (termasuk _@simplelogin.com_), memperbanyak pilihan bagi pengguna yang memutuskan untuk berlangganan paket berbayar.
![image](assets/it/15.webp)

Setelah akhiran acak dan domain telah dipilih, Anda dapat mengatur apakah Address yang baru (dan aneh) ini akan berfungsi sebagai alias hanya untuk salah satu kotak email pribadi, atau untuk semuanya. Alias menjadi siap dan aktif setelah mengklik _Buat_

Setelah akhiran acak dan domain dipilih, Anda bisa menentukan apakah alamat tersebut (unik dan aneh) ini akan berfungsi sebagai alias untuk salah satu kotak email pribadi Anda saja, atau untuk semua kotak email yang Anda miliki. Alias akan siap dan aktif setelah Anda mengeklik _Create_ (Buat).
![image](assets/it/16.webp)

Alamat email baru telah dibuat dan sekarang sudah terlihat, siap untuk dikirim (ke bank!) hanya dengan menyalinnya.
![image](assets/it/18.webp)

Pada titik ini, Anda dapat berfokus untuk membuat alias untuk setiap layanan atau platform yang ingin Anda akses, di mana email diperlukan sebagai parameter penting untuk membuat akun.
![image](assets/it/19.webp)

Bagi para penggemar privasi, ada juga opsi untuk membuat email generate menjadi Address berdasarkan protokol UUID (bukan berdasarkan nama yang dapat diidentifikasi), yang menciptakan pengenal unik 128-bit yang tidak dikendalikan oleh pihak terpusat. Fitur ini, yang berguna untuk akun-akun sensitif, bisa ditemukan di menu .

Bagi para pegiat privasi, tersedia juga opsi untuk menghasilkan alamat email berdasarkan protokol UUID (bukan pada nama yang dapat diidentifikasi). Fitur ini menciptakan pengenal unik berukuran 128-bit yang tidak dikendalikan oleh pihak terpusat. Fitur ini, yang berguna untuk akun sensitif, dapat ditemukan di menu _Random Alias_ (Alias Acak).
![image](assets/it/21.webp)
![image](assets/it/22.webp)

Seperti yang Anda lihat, ini adalah alamat email yang membutuhkan pengelolaan yang tepat.
Jika Anda berubah pikiran dan tidak ingin lagi menggunakan alias, cukup klik pada perintah _More_ (Lebih) pada masing-masing alias dan pilih _Delete_ (Hapus).
![image](assets/it/23.webp)

## Manajemen Alias

Membuat alias itu mudah, begitu pula pengelolaannya, yang hanya membutuhkan sedikit perhatian dan disiplin. Semua lalu lintas email, pada kenyataannya, akan tetap melalui kotak masuk email yang telah kita definisikan di awal sebagai yang resmi. Notifikasi dan komunikasi penting dari platform akan terus tiba di Gmail, Proton, atau penyedia email lainnya.

Namun, hasilnya adalah kita telah menjaga alamat utama, yang sejak saat pembuatan alias, kita bebas memutuskan kepada siapa akan mengungkapkannya dan kepada siapa tidak.

Sebuah alias berfungsi baik untuk menerima maupun mengirim: pengguna lain akan menerima balasan dari `alias.preoccupy789@8shield.net`, jika ini adalah nama samaran yang dipilih untuk penerima tertentu.

## Kelebihan

Secara keseluruhan, penggunaan alias adalah cara yang efektif untuk melindungi identitas dan privasi Anda. Alamat email sering kali dikumpulkan oleh pialang data dan situs web untuk melacak kebiasaan serta perilaku pengguna. Meskipun alias tidak membuat Anda sepenuhnya tidak terlacak, penggunaan alias secara konsisten merupakan langkah positif untuk mengamankan informasi Anda. Terlebih lagi, di "desa digital global" kita, di mana peretasan, penjualan data, dan pelanggaran keamanan sangat umum terjadi, sangat mungkin email yang Anda gunakan untuk mendaftar di berbagai situs web telah disusupi atau ditargetkan.

Sebuah nama samaran unik, yang digunakan untuk setiap login, **segera memungkinkan kita memahami platform mana yang mengirim spam (atau yang lebih buruk) ke kotak masuk kita, karena email tersebut diidentifikasi oleh alias yang terkait dengannya.** Anda tidak tahu berapa banyak spam dan phishing yang berasal dari saluran yang disebut "andal" karena bersifat institusional, sampai Anda mulai menggunakan alias untuk bank, satu untuk layanan pos, atau yang spesifik untuk beberapa layanan pemerintah yang wajib. Setelah pengirim spam (atau yang lebih buruk) teridentifikasi, Anda akan tahu bahwa situs tersebut telah disusupi, sehingga Anda dapat mengambil setiap tindakan pencegahan untuk melindungi semua data yang diberikan (pikirkan kartu kredit!) ke situs web tertentu tersebut, yang mungkin baru menyadari pelanggaran tersebut berminggu-minggu kemudian.

Mengenai Simple Login, alat ini memiliki fitur-fitur berikut:
- Aplikasi seluler (juga dari F-Droid) dan ekstensi browser, untuk mengelola alias dalam situasi apa pun:
- Autentikasi dua faktor untuk setiap nama samaran baru, yang meningkatkan tingkat kemandirian dari layanan itu sendiri;
- Dukungan PGP (untuk pengguna Premium);
- Pembuatan setiap jenis alias yang sederhana (kustom, acak, dan UUID).
- Di antara paket gratis di sektor ini, kemampuan untuk menggunakan alias dengan lebih banyak kotak email "resmi". Pesaing lain membatasi hanya pada satu.

## Kekurangan

- 10 alias mungkin tidak cukup jika Anda berencana menggunakan Simple Login secara ekstensif. Dalam kasus ini, paket berbayar, yang cukup terjangkau, akan sangat membantu untuk menambah jumlah alias yang tersedia.
- Tidak mungkin membuat alias dengan nama dan domain yang tertentu. Sufiks acak, yang ditambahkan setelah nama yang kita pilih, menghasilkan alamat yang bisa terbilang "aneh". Media sosial tradisional biasanya menolak akun yang dibuat dengan jenis alamat email ini. Nostr menyelesaikan masalah ini!
- Jika Anda menggunakan alias untuk mengirim pesan kepada seseorang, email tersebut mudah masuk ke folder spam penerima. Sebagai langkah awal, disarankan untuk menggunakan nama samaran tersebut hanya untuk menerima, seperti saat membuat akun, berlangganan milis, dll.
