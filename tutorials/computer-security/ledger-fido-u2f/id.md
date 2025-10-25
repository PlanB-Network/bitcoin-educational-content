---
name: "Ledger U2F & FIDO2"
description: Tingkatkan keamanan online Anda dengan Ledger
---
![cover](assets/cover.webp)

Perangkat Ledger adalah dompet perangkat keras yang awalnya dirancang untuk mengamankan dompet Bitcoin, tetapi juga memiliki opsi canggih untuk autentikasi kuat di web. Berkat kompatibilitasnya dengan protokol **U2F** dan **FIDO2**, Ledger memungkinkan Anda mengamankan akses ke akun online dengan menyiapkan faktor autentikasi kedua.

Protokol U2F (Universal 2nd Factor) diperkenalkan oleh Google dan Yubico pada tahun 2014, kemudian distandarisasi oleh FIDO Alliance. Protokol ini memungkinkan penambahan faktor autentikasi fisik kedua (2FA) saat login. Setelah diaktifkan, selain kata sandi klasik, pengguna harus menyetujui setiap upaya untuk terhubung ke akun mereka dengan menekan tombol pada perangkat Ledger mereka. Dalam konteks ini, Ledger bekerja mirip dengan Yubikey. U2F sebenarnya adalah sub-komponen dari standar FIDO2, yang mencakupnya sambil membawa peningkatan signifikan, termasuk dukungan asli untuk browser modern dan fleksibilitas yang lebih besar dalam manajemen kunci autentikasi.

Metode-metode ini didasarkan pada kriptografi asimetris: tidak ada data rahasia yang ditransmisikan, sehingga serangan phishing atau intersepsi menjadi tidak efektif. U2F dan FIDO2 sekarang didukung oleh banyak layanan online.

Dalam tutorial ini, kami akan menunjukkan kepada Anda cara mengaktifkan U2F dan FIDO2 untuk autentikasi dua faktor dengan Ledger Anda.

**Catatan:** U2F dan FIDO2 didukung di semua perangkat Ledger yang dilengkapi dengan firmware terbaru: mulai versi 2.1.0 untuk Nano X dan Nano S klasik, serta mulai versi 1.1.0 untuk Nano S Plus. Model Stax dan Flex kompatibel secara bawaan.

## Instal aplikasi Kunci Keamanan Ledger

Jika Anda menggunakan perangkat Ledger, Anda mungkin tahu bahwa firmware saja tidak berisi semua fitur yang diperlukan untuk mengelola dompet kripto. Contohnya, untuk menggunakan dompet Bitcoin, Anda perlu menginstal aplikasi "Bitcoin". Demikian pula, untuk mengelola kunci MFA, Anda perlu menginstal aplikasi "*Security Key*".

Sebelum memulai, pastikan Anda telah menyiapkan dompet Bitcoin di Ledger Anda. Penting untuk menyimpan frasa mnemonik Anda dengan benar, karena kunci yang digunakan untuk 2FA berasal dari frasa mnemonik ini. Jika Ledger Anda hilang atau rusak, Anda dapat memulihkan akses ke kunci Anda dengan memasukkan frasa mnemonik Anda di perangkat Ledger lain (untuk saat ini, identifikasi FIDO2 dalam mode "tanpa kata sandi" belum didukung di Ledger, jadi belum ada identifikasi residen).

Hubungkan Ledger ke komputer Anda dan buka kuncinya.
![Image](assets/fr/01.webp)

Untuk menginstal aplikasi, buka perangkat lunak [Ledger Live] (https://www.Ledger.com/Ledger-live), lalu pergi ke tab "*My Ledger*". Temukan aplikasi "*Security Key*" dan instal di perangkat Anda.
![Image](assets/fr/02.webp)

Aplikasi "*Security Key*" seharusnya kini muncul bersamaan dengan aplikasi lain yang terinstal di Ledger Anda.
![Image](assets/fr/03.webp)

Klik aplikasi tersebut untuk membiarkannya tetap terbuka untuk langkah-langkah selanjutnya dalam tutorial.
![Image](assets/fr/04.webp)

## Penggunaan U2F/FIDO2 untuk 2FA dengan Ledger

Akses akun yang ingin Anda amankan dengan autentikasi dua faktor. Sebagai contoh, saya akan menggunakan akun Bitwarden. Anda biasanya akan menemukan opsi 2FA di pengaturan layanan, di bawah tab "*authentication*", "*security*", "*login*", atau "*password*".
![Image](assets/fr/05.webp)

Pada bagian yang diperuntukan untuk autentikasi dua faktor, pilih opsi "*Passkey*" (istilah ini mungkin berbeda tergantung pada situs yang Anda gunakan).
![Image](assets/fr/06.webp)

Anda akan sering diminta untuk mengonfirmasi kata sandi Anda saat ini.
![Image](assets/fr/07.webp)

Beri nama kunci keamanan Anda agar mudah dikenali, lalu klik "*Read Key*".
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

Keunggulan menggunakan *Hardware Wallet Ledger* untuk autentikasi dua faktor adalah Anda dapat dengan mudah memulihkan kunci Anda berkat frasa mnemonik. Selain cadangan dasar ini, Anda juga bisa menggunakan kode darurat yang disediakan oleh setiap layanan yang Anda mengaktifkan 2FA-nya. Kode darurat ini memungkinkan Anda terhubung ke akun jika Anda kehilangan kunci keamanan Anda. Jadi, kode ini menggantikan 2FA untuk koneksi jika diperlukan.

Pada Bitwarden, misalnya, Anda dapat mengakses kode ini dengan mengeklik "*View recovery code*".
![Image](assets/fr/14.webp)

Saya sarankan Anda untuk menyimpan kode ini di tempat yang berbeda dari tempat Anda menyimpan kata sandi utama Anda, untuk mencegah keduanya dicuri secara bersamaan. Contohnya, jika kata sandi Anda disimpan di pengelola kata sandi, simpan kode darurat 2FA Anda di kertas, secara terpisah.


Pendekatan ini menawarkan Anda dua tingkat cadangan jika Ledger Anda hilang untuk autentikasi 2FA: cadangan pertama menggunakan frasa mnemonik untuk semua akun Anda, dan cadangan kedua yang spesifik untuk akun menggunakan kode darurat. Namun, penting untuk tidak bingung tentang peran mnemonik dengan kode darurat:

- Frasa mnemonik 12 atau 24 kata memberi Anda akses tidak hanya ke kunci yang digunakan untuk 2FA di semua akun Anda, tetapi juga ke bitcoin Anda yang diamankan dengan Ledger Anda;
- Kode darurat memungkinkan Anda untuk sementara melewati permintaan 2FA hanya pada akun yang bersangkutan (dalam contoh ini, hanya di Bitwarden).

Selamat, Anda sekarang sudah mahir menggunakan Ledger Anda untuk MFA! Jika Anda merasa tutorial ini bermanfaat, saya akan sangat berterima kasih jika Anda memberikan acungan jempol hijau di bawah. Jangan ragu untuk membagikan tutorial ini di sosial media Anda. Terima kasih banyak!

Saya juga merekomendasikan tutorial lain, di mana kita melihat solusi lain untuk autentikasi U2F dan FIDO2:

https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e
