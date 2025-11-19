---
name: Authy 2FA
description: Bagaimana cara menggunakan aplikasi 2FA?
---
![cover](assets/cover.webp)

Saat ini, autentikasi dua faktor (2FA) telah menjadi sangat penting untuk meningkatkan keamanan akun online dari akses tidak sah. Dengan meningkatnya serangan siber, hanya mengandalkan kata sandi untuk mengamankan akun terkadang tidak cukup. 2FA memperkenalkan lapisan keamanan tambahan dengan membutuhkan bentuk autentikasi kedua selain kata sandi. Verifikasi ini dapat berupa beberapa bentuk, seperti kode yang dikirim melalui SMS, kode dinamis yang dihasilkan oleh aplikasi khusus, atau penggunaan kunci keamanan fisik. Penggunaan 2FA sangat mengurangi risiko akun Anda disusupi, bahkan jika kata sandi Anda dicuri.

## 2FA melalui Aplikasi Autentikasi

Di tutorial lain, kita akan bahas solusi lain seperti kunci keamanan fisik. Tapi di tutorial ini, Saya akan fokus membahas aplikasi 2FA. Cara kerja aplikasi ini cukup simpel: saat 2FA diaktifkan di sebuah akun, setiap kali Anda login, Anda tidak hanya akan diminta kata sandi biasa, tapi juga kode 6 digit. Kode ini dihasilkan oleh aplikasi 2FA Anda. Karakteristik penting dari kode 6 digit ini adalah tidak statis; kode baru akan dihasilkan oleh aplikasi setiap 30 detik.

![AUTHY 2FA](assets/notext/01.webp)

Pembaharuan kode setiap 30 detik sangat menyulitkan penyerang untuk mengakses akun Anda. Sistem ini mencegah penyerang menggunakan kembali kode yang dicuri atau diretas, karena kode tersebut kedaluwarsa dengan cepat. Dengan demikian, meskipun penyerang berhasil mendapatkan kode, mereka hanya dapat menggunakannya dalam kurun waktu yang sangat singkat sebelum kode baru diperlukan. Terlebih lagi, fakta bahwa kode sering berubah secara signifikan mengurangi waktu yang tersedia bagi peretas yang mencoba menebak kode melalui metode *brute force*.

2FA melalui aplikasi autentikasi dengan demikian mewakili metode yang mudah digunakan dan gratis untuk secara signifikan meningkatkan keamanan akun online Anda.

Ada banyak aplikasi untuk mengatur 2FA, di antaranya Google Authenticator dan Microsoft Authenticator adalah yang paling dikenal. Namun, dalam tutorial ini, saya ingin memperkenalkan Anda pada aplikasi lain yang kurang dikenal bernama Authy. Semua aplikasi ini beroperasi menggunakan protokol yang sama, yaitu TOTP (*Time based One Time Password*), sehingga penggunaannya cukup serupa. Authy menawarkan beberapa keunggulan dibandingkan aplikasi lain dari perusahaan teknologi besar. Pertama dan terpenting, Authy memungkinkan Anda menyinkronkan token 2FA Anda di berbagai perangkat, yang dapat berguna jika ponsel hilang atau diganti. Authy juga memungkinkan Anda membuat cadangan terenkripsi dan menyimpannya secara online, memastikan Anda tidak pernah kehilangan akses ke token Anda, bahkan jika Anda kehilangan perangkat utama Anda. Dari perspektif antarmuka pengguna, secara pribadi saya merasa bahwa Authy juga menawarkan pengalaman yang lebih menyenangkan dan intuitif daripada alternatifnya.

## Bagaimana cara menginstal Authy?

Di smartphone Anda, buka toko aplikasi (Google Play Store atau Apple Store), dan cari "*Twilio Authy Authenticator*".

- [Apple](https://apps.apple.com/us/app/twilio-authy/id494168017)
- [Android](https://play.google.com/store/apps/details?id=com.authy.authy)
  
![AUTHY 2FA](assets/notext/02.webp)

Pada saat menjalankan aplikasi pertama kali, Anda akan perlu membuat akun. Pilih kode negara Anda, serta nomor telepon Anda, lalu klik pada "*Submit*".
![AUTHY 2FA](assets/notext/03.webp)
Masukkan alamat email Anda untuk pemulihan kode.
![AUTHY 2FA](assets/notext/04.webp)
Sebuah email akan dikirimkan kepada Anda untuk memverifikasi email Anda. Masukkan 6 digit yang diterima untuk konfirmasi.
![AUTHY 2FA](assets/notext/05.webp)
Pilih salah satu dari dua metode yang tersedia untuk memverifikasi nomor telepon Anda. Jika Anda memilih untuk menerima SMS, masukkan kode 6-digit yang diterima melalui pesan untuk mengonfirmasi nomor Anda.
![AUTHY 2FA](assets/notext/06.webp)
Selamat, akun Authy Anda telah dibuat!
![AUTHY 2FA](assets/notext/07.webp)

## Bagaimana cara mengkonfigurasi Authy?

Untuk memulai, pergi ke pengaturan aplikasi dengan mengklik tiga titik kecil yang terletak di pojok kanan atas layar.
![AUTHY 2FA](assets/notext/08.webp)
Kemudian klik pada "*Settings*".
![AUTHY 2FA](assets/notext/09.webp)
Di tab "*My Account*", Anda memiliki opsi untuk memodifikasi akun Anda. Saya merekomendasikan untuk menambahkan kode PIN pada aplikasi dengan memilih "*App Protection*". Ini akan menambah lapisan keamanan ekstra untuk mengakses aplikasi Anda.
![AUTHY 2FA](assets/notext/10.webp)
Di tab "*Accounts*", Anda dapat mengatur pencadangan untuk token Anda. Pencadangan ini memungkinkan pemulihan kode Anda jika terjadi masalah. Pencadangan dienkripsi menggunakan kata sandi yang harus Anda tentukan. Penting agar kata sandi ini kuat dan disimpan di tempat yang aman. Pengaturan pencadangan ini tidak selalu wajib jika Anda memiliki metode pemulihan lain, seperti perangkat kedua dengan akun Authy yang sama, misalnya.
![AUTHY 2FA](assets/notext/11.webp)
Di tab "*Devices*", Anda dapat melihat semua perangkat yang tersinkronisasi dengan akun Authy Anda. Anda memiliki opsi untuk menonaktifkan penggunaan berbagai perangkat, yang akan membatasi akses ke akun Anda hanya pada perangkat tersebut. Jika Anda hanya menggunakan satu perangkat, hal ini dapat meningkatkan keamanan akun Anda, namun pastikan Anda memiliki metode cadangan lain jika perangkat tersebut hilang.

Jika Anda memilih untuk mengizinkan penambahan perangkat lain, saya menyarankan untuk mengaktifkan opsi yang memerlukan konfirmasi dari perangkat yang sedang diizinkan di akun Authy Anda sebelum menambahkan perangkat baru.
![AUTHY 2FA](assets/notext/12.webp)
Untuk menambahkan perangkat baru, cukup ulangi proses instalasi yang telah dijelaskan sebelumnya menggunakan kredensial yang sama. Anda kemudian akan diminta untuk mengonfirmasi akses baru ini dari perangkat utama Anda.

## Bagaimana cara mengatur 2FA pada sebuah akun?

Untuk dapat mengatur kode autentikasi 2FA melalui aplikasi seperti Authy pada sebuah akun, akun tersebut harus mendukung fitur ini. Saat ini, mayoritas layanan online memang menawarkan opsi 2FA, namun tidak selalu demikian. Mari kita ambil contoh akun email Proton yang telah saya presentasikan dalam tutorial lain:

https://planb.academy/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

![AUTHY 2FA](assets/notext/13.webp)
Anda umumnya akan menemukan opsi 2FA ini di pengaturan akun Anda, seringkali di bawah bagian "*Password*" atau "*Security*".
![AUTHY 2FA](assets/notext/14.webp)
Ketika Anda mengaktifkan opsi ini pada akun Proton mail Anda, sebuah kode QR akan ditampilkan kepada Anda. Anda kemudian harus memindai kode QR ini dengan aplikasi Authy Anda.
![AUTHY 2FA](assets/notext/15.webp)
Di Authy, klik tombol "*+*".
![AUTHY 2FA](assets/notext/16.webp)
Klik pada "*Scan QR Code*". Kemudian pindai kode QR yang ada di situs web.
![AUTHY 2FA](assets/notext/17.webp)
Anda juga memiliki opsi untuk menyesuaikan nama pengguna Anda jika perlu. Setelah melakukan perubahan, klik tombol "*SAVE*".
![AUTHY 2FA](assets/notext/18.webp)
Authy kemudian akan menampilkan kode 6 digit dinamis Anda yang spesifik untuk akun tersebut dan diperbarui setiap 30 detik.
![AUTHY 2FA](assets/notext/19.webp)
Masukkan kode ini di situs web untuk menyelesaikan pengaturan 2FA.
![AUTHY 2FA](assets/notext/20.webp)
Beberapa situs juga akan memberikan Anda kode pemulihan setelah mengaktifkan 2FA. Kode-kode ini memungkinkan Anda untuk mengakses akun Anda jika Anda kehilangan akses ke aplikasi Authy Anda. Saya merekomendasikan untuk menyimpannya di tempat yang aman.
![AUTHY 2FA](assets/notext/21.webp)
Akun Anda sekarang diamankan dengan autentikasi dua faktor melalui aplikasi Authy.
![AUTHY 2FA](assets/notext/22.webp)
Setiap kali Anda masuk ke akun, Anda akan perlu menyediakan kode dinamis yang dihasilkan oleh Authy. Anda sekarang dapat mengamankan semua akun Anda yang kompatibel dengan metode 2FA ini. Untuk menambahkan akun baru di Authy, klik pada tiga titik kecil di pojok kanan atas aplikasi.
![AUTHY 2FA](assets/notext/23.webp)
Kemudian klik pada "*Add Account*".
![AUTHY 2FA](assets/notext/24.webp)
Ikuti langkah yang sama seperti yang digunakan untuk akun pertama. Berbagai kode dinamis Anda akan terlihat di halaman utama Authy.
