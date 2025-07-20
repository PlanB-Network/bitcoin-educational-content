---
name: Trezor U2F & FIDO2
description: Perkuat keamanan online Anda dengan Trezor
---
![cover](assets/cover.webp)



Perangkat Trezor adalah dompet perangkat keras yang awalnya dirancang untuk mengamankan Bitcoin Wallet, tetapi juga dilengkapi dengan opsi-opsi canggih untuk autentikasi yang kuat di web. Berkat kompatibilitasnya dengan protokol **U2F** dan **FIDO2**, perangkat ini memungkinkan Anda untuk mengamankan akses ke akun online Anda tanpa hanya mengandalkan kata sandi.



Protokol U2F (*Universal 2nd Factor*) diperkenalkan oleh Google dan Yubico pada tahun 2014, kemudian distandardisasi oleh Aliansi FIDO. Protokol ini memungkinkan faktor autentikasi fisik kedua (2FA) untuk ditambahkan saat masuk. Setelah diaktifkan, selain kata sandi klasik, pengguna harus menyetujui setiap upaya untuk terhubung ke akun mereka dengan menekan sebuah tombol pada Trezor mereka. Dalam konteks ini, Trezor bekerja dengan cara yang mirip dengan Yubikey.



Metode ini didasarkan pada kriptografi asimetris: tidak ada data rahasia yang ditransmisikan, membuat serangan phishing atau intersepsi menjadi tidak efektif. U2F sekarang didukung oleh banyak layanan online.



Selain U2F, yang memungkinkan autentikasi dua faktor, Trezors juga mendukung FIDO2 (*Fast IDentity Online 2.0*), sebuah evolusi dari U2F. Ini merupakan protokol autentikasi standar dari tahun 2018, yang memperluas logika U2F dan bertujuan untuk sepenuhnya menggantikan kata sandi. Protokol ini didasarkan pada dua komponen: *WebAuthn* (sisi peramban) dan *CTAP2* (sisi kunci fisik). FIDO2 memungkinkan otentikasi "tanpa kata sandi": pengguna mengidentifikasi diri mereka sendiri hanya melalui perangkat Trezor mereka, yang bertindak sebagai token kriptografi yang unik, tanpa kata sandi tambahan. Protokol ini sekarang kompatibel dengan sejumlah layanan online, terutama yang ditujukan untuk perusahaan.



Selain fungsionalitas "tanpa kata sandi*", FIDO2 juga memungkinkan autentikasi dua faktor dengan cara yang mirip dengan U2F.



FIDO2 juga memperkenalkan gagasan tentang kredensial residen, yaitu pengidentifikasi yang disimpan langsung di Trezor, yang mencakup kunci pribadi yang memungkinkan koneksi dan informasi identifikasi pengguna. Mekanisme ini memungkinkan otentikasi yang benar-benar bebas kata sandi: cukup colokkan Trezor Anda dan konfirmasikan akses, tanpa memasukkan ID atau kata sandi. Sebaliknya, kredensial non-residen, yang lebih konvensional, hanya menyimpan kunci privat di dalam perangkat; ID pengguna tetap tersimpan di sisi server, dan oleh karena itu harus dimasukkan pada setiap koneksi. Kita akan melihat bagaimana cara menyimpannya dengan Trezor nanti.



Dalam tutorial ini kita akan menemukan cara mengaktifkan U2F atau FIDO2 untuk autentikasi dua faktor, dan kemudian cara mengonfigurasi FIDO2 untuk mengakses akun Anda tanpa kata sandi, langsung dengan Trezor Anda.



**Catatan:** U2F kompatibel dengan semua model Trezor, tetapi FIDO2 hanya didukung pada Safe 3, Safe 5, dan Model T, bukan Model One.



## Menggunakan U2F/FIDO2 untuk 2FA pada Trezor



Sebelum memulai, pastikan Anda sudah menyiapkan Bitcoin Wallet pada Trezor Anda. Sangat penting untuk menyimpan Mnemonic Anda dengan benar, karena kunci yang digunakan untuk U2F dan FIDO2 pada otentikasi dua faktor berasal dari Mnemonic ini. Jika Trezor anda hilang atau rusak, anda dapat memulihkan akses ke kunci anda dengan memasukkan frasa Mnemonic anda pada perangkat Trezor lainnya (perhatikan bahwa untuk kredensial FIDO2 pada mode "*passwordless*", seed saja tidak cukup, seperti yang akan kita lihat pada bagian selanjutnya).



Hubungkan Trezor Anda ke komputer dan buka kuncinya.



![Image](assets/fr/01.webp)



Akses akun yang ingin Anda amankan dengan autentikasi dua faktor. Sebagai contoh, saya akan menggunakan akun Bitwarden. Anda biasanya akan menemukan opsi 2FA di pengaturan layanan, di bawah tab "*authentication*", "*security*", "*login*", atau "*password*".



![Image](assets/fr/02.webp)



Pada bagian yang didedikasikan untuk autentikasi dua faktor, pilih opsi "*Passkey*" (istilah ini mungkin berbeda tergantung pada situs yang Anda gunakan).



![Image](assets/fr/03.webp)



Anda akan sering diminta untuk mengonfirmasi kata sandi Anda saat ini.



![Image](assets/fr/04.webp)



Beri nama kunci keamanan Anda agar mudah dikenali, lalu klik "*Baca Kunci*".



![Image](assets/fr/05.webp)



Detail akun Anda akan muncul di layar Trezor. Sentuh layar atau tekan tombol untuk mengonfirmasi. Anda juga akan diminta untuk mengonfirmasi kode PIN Anda.



![Image](assets/fr/06.webp)



Daftarkan kunci keamanan ini.



![Image](assets/fr/07.webp)



Mulai sekarang, ketika Anda ingin terhubung ke akun Anda, selain kata sandi yang biasa Anda gunakan, Anda akan diminta untuk menghubungkan Trezor Anda.



![Image](assets/fr/08.webp)



Anda kemudian dapat menekan layar Trezor Anda untuk mengonfirmasi autentikasi.



![Image](assets/fr/09.webp)



Keuntungan menggunakan Trezor Hardware Wallet untuk autentikasi dua faktor adalah Anda dapat dengan mudah memulihkan kunci Anda berkat frasa Mnemonic. Selain cadangan dasar ini, Anda juga bisa menggunakan kode darurat yang disediakan oleh setiap layanan di mana Anda telah mengaktifkan 2FA. Kode darurat ini memungkinkan Anda untuk terhubung ke akun Anda jika Anda kehilangan kunci keamanan. Oleh karena itu, kode ini menggantikan 2FA untuk koneksi jika diperlukan.



Pada Bitwarden, misalnya, Anda dapat mengakses kode ini dengan mengeklik "*Lihat kode pemulihan*".



![Image](assets/fr/10.webp)



Saya sarankan Anda menyimpan kode ini di tempat yang berbeda dengan tempat Anda menyimpan kata sandi utama Anda, untuk mencegah keduanya dicuri. Sebagai contoh, jika kata sandi Anda disimpan di pengelola kata sandi, simpan kode darurat 2FA Anda di atas kertas, secara terpisah.



Pendekatan ini menawarkan dua tingkat pencadangan jika terjadi kehilangan Trezor Anda untuk otentikasi 2FA: pencadangan pertama menggunakan frasa Mnemonic untuk semua akun Anda, dan pencadangan kedua khusus untuk setiap akun dengan kode darurat. Akan tetapi, penting untuk tidak mengacaukan peran Mnemonic dengan kode darurat:




- Frasa Mnemonic dengan 12 atau 24 kata memberi Anda akses tidak hanya ke kunci yang digunakan untuk 2FA di semua akun Anda, tetapi juga ke bitcoin Anda yang diamankan dengan Trezor;
- Kode darurat memungkinkan Anda untuk melewati permintaan 2FA untuk sementara waktu hanya pada akun yang bersangkutan (dalam contoh ini, hanya pada Bitwarden).



## Menggunakan FIDO2 pada Trezor



Selain otentikasi dua faktor, FIDO2 juga memungkinkan otentikasi "tanpa kata sandi", yaitu tanpa harus memasukkan kata sandi ketika masuk ke sebuah situs. Cukup hubungkan Trezor Anda ke komputer untuk mengakses akun aman Anda dengan cara ini. Berikut ini cara mengonfigurasi fitur ini.



Sebelum memulai, pastikan Anda sudah menyiapkan Bitcoin Wallet pada Trezor Anda. Sangat penting untuk menyimpan Mnemonic, karena pengenal FIDO2 "*passwordless*" dienkripsi dengan seed Anda (kita akan mengetahui bagaimana cara menyimpan pengenal ini dengan benar di bagian selanjutnya).



Hubungkan Trezor ke komputer Anda dan buka kuncinya.



![Image](assets/fr/01.webp)



Akses akun yang ingin Anda amankan dalam mode "*tanpa kata sandi*". Saya akan menggunakan akun Bitwarden sebagai contoh. Opsi ini biasanya ditemukan di pengaturan layanan, biasanya di bawah tab "*authentication*", "*security*" atau "*password*".



Pada Bitwarden, misalnya, opsi ini dapat ditemukan di bawah tab "*Kata sandi utama*". Klik pada "*Nyalakan*" untuk mengaktifkan autentikasi melalui FIDO2.



![Image](assets/fr/11.webp)



Anda akan sering diminta untuk mengonfirmasi kata sandi Anda.



![Image](assets/fr/12.webp)



Detail akun Anda akan muncul di layar Trezor. Sentuh layar atau tekan tombol untuk mengonfirmasi. Anda juga perlu mengonfirmasi kode PIN Anda.



![Image](assets/fr/13.webp)



Di situs, tambahkan nama untuk mengingat kunci keamanan Anda, lalu klik "*Nyalakan*".



![Image](assets/fr/14.webp)



Anda kemudian akan diminta untuk mengidentifikasi diri Anda untuk memeriksa apakah kunci berfungsi dengan baik.



![Image](assets/fr/15.webp)



Mulai sekarang, ketika masuk ke akun Anda, Anda tidak perlu lagi memasukkan email Address atau login. Cukup klik tombol untuk mengautentikasi diri Anda dengan kunci fisik pada formulir login.



![Image](assets/fr/16.webp)



Konfirmasikan koneksi ke Trezor Anda dengan memasukkan PIN Hardware Wallet Anda.



![Image](assets/fr/17.webp)



Anda akan terhubung ke akun Anda tanpa harus memasukkan kata sandi.



![Image](assets/fr/18.webp)



**Harap diperhatikan bahwa meskipun Anda mengaktifkan otentikasi "*passwordless*" melalui FIDO2 di Trezor, kata sandi utama untuk akun online Anda akan tetap berlaku untuk tujuan login**



## Simpan kredensial FIDO2 Anda (penghuni kredensial)



Jika anda menggunakan FIDO2 atau U2F untuk autentikasi dua faktor, yaitu untuk masuk ke akun yang membutuhkan kata sandi sebagai tambahan validasi 2FA melalui Trezor anda, maka frasa Mnemonic saja yang akan mengambil akses ke kunci anda. Akan tetapi, jika anda menggunakan FIDO2 dalam mode "*passwordless*" seperti yang dijelaskan pada bagian sebelumnya, anda harus membuat sebuah salinan dari kredensial FIDO anda sebagai tambahan untuk mencadangkan frasa Mnemonic anda yang mengenkripsi kredensial ini.



Untuk melakukan ini, Anda membutuhkan sebuah komputer yang sudah terinstal Python. Buka sebuah terminal dan jalankan perintah berikut untuk menginstal perangkat lunak Trezor yang diperlukan:



```shell
pip3 install --upgrade trezor
```



Sambungkan Trezor Anda ke komputer melalui USB dan buka kuncinya menggunakan kode PIN.



![Image](assets/fr/01.webp)



Untuk mengambil daftar pengenal FIDO2 yang tersimpan di Trezor, jalankan perintah berikut:



```shell
trezorctl fido credentials list
```



Konfirmasikan ekspor di Trezor Anda.



![Image](assets/fr/19.webp)



Informasi login FIDO2 Anda akan ditampilkan di terminal Anda. Sebagai contoh, untuk akun Bitwarden saya, saya mendapatkan informasi ini:



```shell
WebAuthn credential at index 0:
Relying party ID:       vault.bitwarden.com
Relying party name:     Bitwarden
User ID:                6e315ebabc8b6945a253b1c50116538d
User name:              tutoplanbnetwork@proton.me
User display name:      PBN
Creation time:          2
hmac-secret enabled:    True
Use signature counter:  True
Algorithm:              ES256 (ECDSA w/ SHA-256)
Curve:                  P-256 (secp256r1)
Credential ID:          f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Salin dan simpan semua informasi ini dalam sebuah file teks. Tidak ada risiko signifikan yang terkait dengan cadangan ini, selain mengungkapkan bahwa Anda menggunakan layanan ini dengan FIDO2. "*Credential ID*" dienkripsi menggunakan Wallet dan seed Anda, yang berarti bahwa penyerang yang mendapatkan cadangan ini tidak akan dapat terhubung ke akun Anda, tetapi hanya mengetahui bahwa Anda menggunakan akun-akun ini. Untuk mendekripsi ID ini, Anda memerlukan seed di Wallet Anda.



Oleh karena itu, Anda dapat membuat beberapa salinan file teks ini, dan menyimpannya di tempat yang berbeda, misalnya secara lokal di komputer Anda, di layanan file-hosting, dan di media eksternal seperti stik USB. Namun, perlu diingat bahwa cadangan ini tidak diperbarui secara otomatis, jadi Anda harus memperbaruinya setiap kali Anda membuat koneksi "*passwordless*" yang baru dengan Trezor.



Sekarang mari kita bayangkan Anda telah merusak Trezor Anda. Untuk mendapatkan kembali kredensial FIDO2 Anda, pertama-tama Anda harus memulihkan Wallet Anda menggunakan frasa Mnemonic Anda pada perangkat Trezor baru yang kompatibel dengan FIDO2.



Setelah pemulihan selesai, untuk mengimpor pengenal FIDO2 Anda pada perangkat baru, jalankan perintah berikut ini di terminal Anda:



```shell
trezorctl fido credentials add <CREDENTIAL_ID>
```



Cukup ganti `<CREDENTIAL_ID>` dengan salah satu pengenal Anda. Sebagai contoh, dalam kasus saya, ini akan menghasilkan :



```shell
trezorctl fido credentials add f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Trezor Anda akan meminta Anda untuk mengimpor pengenal FIDO2 Anda. Konfirmasikan dengan menekan pada layar.



![Image](assets/fr/20.webp)



Login FIDO2 Anda sekarang sudah dapat digunakan di Trezor. Ulangi prosedur ini untuk setiap pengidentifikasi Anda.



Selamat, Anda sekarang sudah bisa menggunakan Trezor Anda dengan U2F dan FIDO2! Jika Anda merasa tutorial ini bermanfaat, saya akan sangat berterima kasih jika Anda memberikan jempol Green di bawah ini. Jangan ragu untuk membagikan tutorial ini di jejaring sosial Anda. Terima kasih banyak!



Saya juga merekomendasikan tutorial lain ini, di mana kita melihat solusi lain untuk autentikasi U2F dan FIDO2:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e