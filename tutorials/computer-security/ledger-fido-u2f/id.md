---
name: Ledger U2F & FIDO2
description: Tingkatkan keamanan online Anda dengan Ledger
---
![cover](assets/cover.webp)



Perangkat Ledger adalah dompet perangkat keras yang pada awalnya dirancang untuk mengamankan Bitcoin Wallet, tetapi juga dilengkapi dengan opsi lanjutan untuk autentikasi yang kuat di web. Berkat kompatibilitasnya dengan protokol **U2F** dan **FIDO2**, perangkat ini memungkinkan Anda untuk mengamankan akses ke akun online Anda dengan menyiapkan faktor autentikasi kedua.



Protokol U2F (Universal 2nd Factor) diperkenalkan oleh Google dan Yubico pada tahun 2014, kemudian distandardisasi oleh Aliansi FIDO. Protokol ini memungkinkan faktor autentikasi fisik kedua (2FA) untuk ditambahkan saat masuk. Setelah diaktifkan, selain kata sandi klasik, pengguna harus menyetujui setiap upaya untuk terhubung ke akun mereka dengan menekan tombol pada Ledger mereka. Dalam konteks ini, Ledger bekerja dengan cara yang mirip dengan Yubikey. U2F sebenarnya merupakan sub-komponen dari standar FIDO2, yang mencakup standar tersebut sambil membawa peningkatan yang signifikan, termasuk dukungan asli untuk peramban modern dan fleksibilitas yang lebih besar dalam manajemen kunci otentikasi.



Metode-metode ini didasarkan pada kriptografi asimetris: tidak ada data rahasia yang ditransmisikan, membuat serangan phishing atau intersepsi menjadi tidak efektif. U2F dan FIDO2 sekarang didukung oleh banyak layanan online.



Dalam tutorial ini, kami akan menunjukkan kepada Anda cara mengaktifkan U2F dan FIDO2 untuk autentikasi dua faktor dengan Ledger Anda.



**Catatan:** U2F dan FIDO2 didukung pada semua perangkat Ledger yang dilengkapi dengan firmware terbaru: dari versi 2.1.0 untuk Nano X dan Nano S classic, dan dari versi 1.1.0 untuk Nano S Plus. Model Stax dan Flex kompatibel secara bawaan.



## Instal aplikasi Kunci Keamanan Ledger



Jika Anda menggunakan perangkat Ledger, Anda mungkin tahu bahwa firmware-nya saja tidak berisi semua fitur yang dibutuhkan untuk mengelola dompet kripto. Sebagai contoh, untuk menggunakan Bitcoin Wallet, Anda harus menginstal aplikasi "*Bitcoin*". Demikian pula, untuk mengelola kunci MFA, Anda perlu menginstal aplikasi "*Security Key*".



Sebelum memulai, pastikan Anda telah menyiapkan Bitcoin Wallet pada Ledger Anda. Penting untuk menyimpan Mnemonic Anda dengan benar, karena kunci yang digunakan untuk 2FA berasal dari Mnemonic ini. Jika Ledger Anda hilang atau rusak, Anda dapat memulihkan akses ke kunci Anda dengan memasukkan frasa Mnemonic Anda pada perangkat Ledger lainnya (untuk saat ini, pengenal FIDO2 dalam mode "*passwordless*" belum didukung di Ledgers, jadi tidak ada pengenal residen).



Hubungkan Ledger ke komputer Anda dan buka kuncinya.



![Image](assets/fr/01.webp)



Untuk menginstal aplikasi, buka perangkat lunak [Ledger Live] (https://www.Ledger.com/Ledger-live), lalu buka tab "*My Ledger*". Temukan aplikasi "*Security Key*" dan instal pada perangkat Anda.



![Image](assets/fr/02.webp)



Aplikasi "*Security Key*" sekarang akan muncul di samping aplikasi lain yang terinstal pada Ledger Anda.



![Image](assets/fr/03.webp)



Klik pada aplikasi untuk membiarkannya terbuka untuk langkah berikutnya dalam tutorial.



![Image](assets/fr/04.webp)



## Gunakan U2F/FIDO2 untuk 2FA dengan Ledger



Akses akun yang ingin Anda amankan dengan autentikasi dua faktor. Sebagai contoh, saya akan menggunakan akun Bitwarden. Anda biasanya akan menemukan opsi 2FA di pengaturan layanan, di bawah tab "*authentication*", "*security*", "*login*", atau "*password*".



![Image](assets/fr/05.webp)



Pada bagian yang didedikasikan untuk autentikasi dua faktor, pilih opsi "*Passkey*" (istilah ini mungkin berbeda tergantung pada situs yang Anda gunakan).



![Image](assets/fr/06.webp)



Anda akan sering diminta untuk mengonfirmasi kata sandi Anda saat ini.



![Image](assets/fr/07.webp)



Beri nama kunci keamanan Anda agar mudah dikenali, lalu klik "*Baca Kunci*".



![Image](assets/fr/08.webp)



Rincian akun Anda akan muncul pada layar Ledger. Tekan tombol "*Register*" untuk mengonfirmasi (atau kedua tombol secara bersamaan, tergantung model yang Anda gunakan).



![Image](assets/fr/09.webp)



Kunci akses telah berhasil didaftarkan.



![Image](assets/fr/10.webp)



Daftarkan kunci keamanan ini.



![Image](assets/fr/11.webp)



Mulai sekarang, ketika Anda masuk ke akun Anda, selain kata sandi yang biasa Anda gunakan, Anda akan diminta untuk menghubungkan Ledger Anda.



![Image](assets/fr/12.webp)



Anda kemudian dapat menekan tombol "*Log in*" pada layar Ledger untuk mengonfirmasi autentikasi (atau kedua tombol secara bersamaan, tergantung model yang Anda gunakan).



![Image](assets/fr/13.webp)



Keuntungan menggunakan Hardware Wallet Ledger untuk autentikasi dua faktor adalah Anda dapat dengan mudah memulihkan kunci Anda berkat frasa Mnemonic. Selain cadangan dasar ini, Anda juga bisa menggunakan kode darurat yang disediakan oleh setiap layanan yang telah Anda aktifkan 2FA-nya. Kode darurat ini memungkinkan Anda untuk terhubung ke akun Anda jika Anda kehilangan kunci keamanan. Oleh karena itu, kode ini menggantikan 2FA untuk koneksi jika diperlukan.



Pada Bitwarden, misalnya, Anda dapat mengakses kode ini dengan mengeklik "*Lihat kode pemulihan*".



![Image](assets/fr/14.webp)



Saya sarankan Anda menyimpan kode ini di tempat yang berbeda dengan tempat Anda menyimpan kata sandi utama Anda, untuk mencegah keduanya dicuri. Sebagai contoh, jika kata sandi Anda disimpan di pengelola kata sandi, simpan kode darurat 2FA Anda di atas kertas, secara terpisah.



Pendekatan ini menawarkan dua tingkat pencadangan jika terjadi kehilangan Ledger untuk autentikasi 2FA: pencadangan pertama menggunakan frasa Mnemonic untuk semua akun Anda, dan pencadangan kedua yang khusus untuk akun tertentu dengan menggunakan kode darurat. Namun, penting untuk tidak mengacaukan peran Mnemonic dengan kode darurat:




- Frasa Mnemonic yang terdiri dari 12 atau 24 kata memberi Anda akses tidak hanya ke kunci yang digunakan untuk 2FA di semua akun Anda, tetapi juga ke bitcoin Anda yang diamankan dengan Ledger;
- Kode darurat memungkinkan Anda untuk melewati permintaan 2FA untuk sementara waktu hanya pada akun yang bersangkutan (dalam contoh ini, hanya pada Bitwarden).



Selamat, Anda sekarang sudah mahir menggunakan Ledger untuk MFA! Jika Anda merasa tutorial ini bermanfaat, saya akan sangat berterima kasih jika Anda mau memberikan tanda jempol pada Green di bawah ini. Jangan ragu untuk membagikan tutorial ini di jejaring sosial Anda. Terima kasih banyak!



Saya juga merekomendasikan tutorial lain ini, di mana kita melihat solusi lain untuk autentikasi U2F dan FIDO2:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e