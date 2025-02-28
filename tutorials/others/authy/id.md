---
name: Authy 2FA
description: Bagaimana cara menggunakan aplikasi 2FA?
---
![cover](assets/cover.webp)

Saat ini, autentikasi dua faktor (2FA) telah menjadi esensial untuk meningkatkan keamanan akun online dari akses tidak sah. Dengan meningkatnya serangan siber, mengandalkan hanya kata sandi untuk mengamankan akun Anda terkadang tidak cukup. 2FA memperkenalkan lapisan keamanan tambahan dengan memerlukan bentuk autentikasi kedua selain kata sandi. Verifikasi ini dapat mengambil beberapa bentuk, seperti kode yang dikirim melalui SMS, kode dinamis yang dihasilkan oleh aplikasi khusus, atau penggunaan kunci keamanan fisik. Penggunaan 2FA sangat mengurangi risiko akun Anda dikompromikan, bahkan dalam kejadian kata sandi Anda dicuri.

## 2FA melalui Aplikasi Autentikasi

Kita akan menjelajahi solusi lain seperti kunci keamanan fisik dalam tutorial lain, tetapi dalam ini, saya mengusulkan untuk secara spesifik membahas aplikasi 2FA. Operasi dari aplikasi-aplikasi ini cukup sederhana: ketika 2FA diaktifkan pada sebuah akun, setiap kali login, Anda tidak hanya akan diminta kata sandi biasa Anda tetapi juga kode 6 digit. Kode ini dihasilkan oleh aplikasi 2FA Anda. Karakteristik penting dari kode 6 digit ini adalah bahwa itu tidak statis; kode baru dihasilkan oleh aplikasi setiap 30 detik.
![AUTHY 2FA](assets/notext/01.webp)
Pembaharuan kode setiap 30 detik membuatnya sangat sulit bagi penyerang untuk mengakses akun Anda. Sistem ini mencegah penyerang menggunakan kembali kode yang dicuri atau diintersepsi, karena kode tersebut cepat kadaluarsa. Dengan demikian, bahkan jika penyerang berhasil mendapatkan kode, mereka hanya akan dapat menggunakannya dalam jendela waktu yang sangat singkat sebelum kode baru diperlukan. Selain itu, fakta bahwa kode berubah begitu sering secara signifikan mengurangi waktu yang tersedia bagi peretas yang mencoba menebak kode melalui brute force.

2FA melalui aplikasi autentikasi dengan demikian mewakili metode yang mudah digunakan dan gratis untuk secara signifikan meningkatkan keamanan akun online Anda.

Ada banyak aplikasi untuk mengatur 2FA, di antaranya Google Authenticator dan Microsoft Authenticator adalah yang paling dikenal. Namun, dalam tutorial ini, saya ingin memperkenalkan Anda pada solusi lain yang kurang dikenal bernama Authy. Semua aplikasi ini beroperasi menggunakan protokol TOTP (*Time based One Time Password*) yang sama, membuat penggunaannya cukup serupa.
Authy menawarkan beberapa keuntungan dibandingkan solusi lain dari perusahaan teknologi besar. Pertama dan terutama, itu memungkinkan Anda untuk menyinkronkan token 2FA Anda di beberapa perangkat, yang bisa berguna dalam kasus kehilangan atau pergantian telepon. Authy juga memungkinkan Anda untuk menghasilkan cadangan terenkripsi dan menyimpannya secara online, memastikan Anda tidak pernah kehilangan akses ke token Anda, bahkan jika Anda kehilangan perangkat utama Anda. Dari perspektif antarmuka pengguna, secara pribadi saya merasa bahwa Authy juga menawarkan pengalaman yang lebih menyenangkan dan intuitif dibandingkan alternatifnya.

## Bagaimana cara menginstal Authy?

Di smartphone Anda, buka toko aplikasi (Google Play Store atau Apple Store), dan cari "*Twilio Authy Authenticator*".

- [Apple](https://apps.apple.com/us/app/twilio-authy/id494168017)
- [Android](https://play.google.com/store/apps/details?id=com.authy.authy)
![AUTHY 2FA](assets/notext/02.webp)
Pada peluncuran pertama aplikasi, Anda akan perlu membuat akun. Pilih kode negara Anda, serta nomor telepon Anda, lalu klik pada "*Submit*".
![AUTHY 2FA](assets/notext/03.webp)
Masukkan alamat email Anda untuk pemulihan kode.
![AUTHY 2FA](assets/notext/04.webp)Sebuah email akan dikirimkan kepada Anda untuk memverifikasi alamat Anda. Masukkan 6 digit yang diterima untuk konfirmasi.
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
Di tab "*My Account*", Anda memiliki opsi untuk memodifikasi akun Anda. Saya merekomendasikan menambahkan kode PIN ke aplikasi dengan memilih "*App Protection*". Ini menambahkan lapisan keamanan tambahan untuk mengakses aplikasi Anda.
![AUTHY 2FA](assets/notext/10.webp)
Di tab "*Accounts*", Anda dapat mengatur cadangan untuk token Anda. Cadangan ini memungkinkan pemulihan kode Anda dalam kasus terjadi masalah. Ini dienkripsi menggunakan kata sandi yang harus Anda tentukan. Penting bahwa kata sandi ini kuat dan disimpan di tempat yang aman. Mengatur cadangan ini tidak selalu wajib jika Anda memiliki metode pemulihan lain, seperti perangkat kedua dengan akun Authy yang sama, misalnya.
![AUTHY 2FA](assets/notext/11.webp)Di tab "*Devices*", Anda dapat melihat semua perangkat yang disinkronkan dengan akun Authy Anda. Anda memiliki opsi untuk menonaktifkan penggunaan beberapa perangkat, yang membatasi akses ke akun Anda hanya untuk perangkat tersebut. Jika Anda hanya menggunakan satu perangkat, ini dapat meningkatkan keamanan akun Anda, tetapi pastikan Anda memiliki metode cadangan lain jika Anda kehilangan perangkat tersebut.

Jika Anda lebih memilih untuk mengizinkan penambahan perangkat lain, saya menyarankan Anda untuk mengaktifkan opsi yang memerlukan konfirmasi dari perangkat yang saat ini diizinkan di akun Authy Anda sebelum menambahkan perangkat baru.
![AUTHY 2FA](assets/notext/12.webp)
Untuk menambahkan perangkat baru, cukup ulangi proses instalasi yang disajikan di bagian sebelumnya menggunakan kredensial yang sama. Anda kemudian akan diminta untuk mengonfirmasi akses baru ini dari perangkat utama Anda.

## Bagaimana cara mengatur 2FA pada sebuah akun?

Untuk mengatur kode autentikasi 2FA melalui aplikasi seperti Authy pada sebuah akun, akun tersebut harus mendukung fitur ini. Saat ini, mayoritas layanan online menawarkan opsi 2FA ini, tetapi ini tidak selalu kasusnya. Mari kita ambil contoh akun Proton mail yang saya sajikan dalam tutorial lain:

https://planb.network/tutorials/others/general/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2
![AUTHY 2FA](assets/notext/13.webp)
Anda umumnya akan menemukan opsi 2FA ini di pengaturan akun Anda, seringkali di bawah bagian "*Password*" atau "*Security*".
![AUTHY 2FA](assets/notext/14.webp)
Ketika Anda mengaktifkan opsi ini pada akun Proton mail Anda, sebuah kode QR akan disajikan kepada Anda. Anda kemudian harus memindai kode QR ini dengan aplikasi Authy Anda.
![AUTHY 2FA](assets/notext/15.webp)
Di Authy, klik tombol "*+*".
![AUTHY 2FA](assets/notext/16.webp)
Klik pada "*Scan QR Code*". Kemudian pindai kode QR yang ada di situs web. ![AUTHY 2FA](assets/notext/17.webp)
Anda juga memiliki opsi untuk menyesuaikan nama pengguna Anda jika perlu. Setelah melakukan perubahan, klik tombol "*SAVE*".
![AUTHY 2FA](assets/notext/18.webp)
Authy kemudian akan menampilkan kode 6 digit dinamis Anda yang spesifik untuk akun tersebut dan diperbarui setiap 30 detik.
![AUTHY 2FA](assets/notext/19.webp)
Masukkan kode ini di situs web untuk menyelesaikan pengaturan 2FA.
![AUTHY 2FA](assets/notext/20.webp)
Beberapa situs juga akan memberikan Anda kode pemulihan setelah mengaktifkan 2FA. Kode-kode ini memungkinkan Anda untuk mengakses akun Anda jika Anda kehilangan akses ke aplikasi Authy Anda. Saya merekomendasikan untuk menyimpannya di tempat yang aman.
![AUTHY 2FA](assets/notext/21.webp)Akun Anda sekarang diamankan dengan otentikasi dua faktor melalui aplikasi Authy.
![AUTHY 2FA](assets/notext/22.webp)
Setiap kali Anda masuk ke akun, Anda akan perlu menyediakan kode dinamis yang dihasilkan oleh Authy. Anda sekarang dapat mengamankan semua akun Anda yang kompatibel dengan metode 2FA ini. Untuk menambahkan akun baru di Authy, klik pada tiga titik kecil di pojok kanan atas aplikasi.
![AUTHY 2FA](assets/notext/23.webp)
Kemudian klik pada "*Add Account*".
![AUTHY 2FA](assets/notext/24.webp)
Ikuti langkah yang sama seperti yang digunakan untuk akun pertama. Berbagai kode dinamis Anda akan terlihat di halaman utama Authy.