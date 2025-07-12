---
name: YubiKey 2FA
description: Bagaimana cara menggunakan kunci keamanan fisik?
---
![cover](assets/cover.webp)

Saat ini, autentikasi dua faktor (2FA) telah menjadi penting untuk meningkatkan keamanan akun online terhadap akses tidak sah. Dengan meningkatnya serangan siber, mengandalkan kata sandi saja untuk mengamankan akun Anda terkadang tidak cukup.

2FA memperkenalkan lapisan keamanan tambahan dengan memerlukan bentuk autentikasi kedua selain kata sandi tradisional. Verifikasi ini dapat mengambil berbagai bentuk, seperti kode yang dikirim melalui SMS, kode dinamis yang dihasilkan oleh aplikasi khusus, atau penggunaan kunci keamanan fisik. Penggunaan 2FA secara signifikan mengurangi risiko akun Anda disusupi, bahkan jika kata sandi Anda dicuri.

Dalam tutorial lain, saya menjelaskan cara mengatur dan menggunakan aplikasi 2FA TOTP:

https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Di sini, kita akan melihat cara menggunakan kunci keamanan fisik sebagai faktor autentikasi kedua untuk semua akun Anda.

## Apa itu kunci keamanan fisik?

Kunci keamanan fisik adalah perangkat yang digunakan untuk meningkatkan keamanan akun online Anda melalui autentikasi dua faktor (2FA). Perangkat ini sering kali menyerupai kunci USB kecil yang harus dimasukkan ke dalam port komputer untuk memverifikasi bahwa memang pengguna yang sah yang mencoba untuk terhubung.

Kunci keamanan fisik adalah perangkat keras khusus yang dirancang untuk menyediakan autentikasi faktor kedua (2FA) yang kuat dalam akun online Anda. Kunci-kunci ini, yang sering kali menyerupai stik USB kecil, dicolokkan ke port komputer Anda untuk mengonfirmasi identitas Anda selama proses terhubung.
![SECURITY KEY 2FA](assets/notext/01.webp)

Ketika Anda masuk ke akun yang dilindungi oleh 2FA dan menggunakan kunci keamanan fisik, Anda tidak hanya harus memasukkan kata sandi biasa Anda, tetapi juga harus memasukkan kunci keamanan fisik ke komputer Anda dan menekan tombol untuk memvalidasi autentikasi. Metode ini dengan demikian menambahkan lapisan keamanan tambahan, karena meskipun seseorang berhasil mendapatkan kata sandi Anda, mereka tidak akan dapat mengakses akun Anda tanpa memiliki kunci secara fisik.

Kunci keamanan fisik adalah perangkat keras khusus yang dirancang untuk menyediakan faktor kedua yang kuat dalam otentikasi akun daring Anda. Kunci-kunci ini, yang sering kali menyerupai stik USB kecil, dicolokkan ke porta komputer Anda untuk mengonfirmasi identitas Anda selama proses masuk.

Kunci keamanan fisik sangat efektif karena menggabungkan dua jenis faktor autentikasi yang berbeda: bukti pengetahuan (kata sandi) dan bukti kepemilikan (kunci fisik).

Namun, metode 2FA ini juga memiliki kekurangan. Pertama, Anda harus selalu memiliki kunci keamanan yang tersedia jika Anda ingin mengakses akun Anda. Anda mungkin perlu menambahkannya ke gantungan kunci Anda. Kedua, tidak seperti metode 2FA lainnya, penggunaan kunci keamanan fisik melibatkan biaya awal karena Anda harus membeli perangkat kecil tersebut. Harga kunci keamanan umumnya bervariasi antara €30 hingga €100 tergantung pada fitur yang dipilih.

## Kunci keamanan fisik mana yang harus dipilih?

Untuk memilih kunci keamanan Anda, beberapa kriteria perlu dipertimbangkan. Pertama dan terpenting, Anda perlu memeriksa protokol yang didukung oleh perangkat. Minimal, saya menyarankan untuk memilih kunci yang mendukung OTP, FIDO2, dan U2F. Detail-detail ini biasanya ditonjolkan oleh produsen dalam deskripsi produk. Untuk memverifikasi kompatibilitas setiap kunci, Anda juga dapat mengunjungi [dongleauth.com](https://www.dongleauth.com/dongles/). Selain itu, pastikan kunci tersebut kompatibel dengan sistem operasi Anda, meskipun merek-merek terkenal seperti Yubikey umumnya mendukung semua sistem yang banyak digunakan.

Anda juga harus memilih kunci berdasarkan jenis port yang tersedia di komputer atau smartphone Anda. Misalnya, jika komputer Anda hanya memiliki porta USB-C, pilih kunci dengan konektor USB-C. Beberapa kunci juga menawarkan opsi koneksi melalui Bluetooth atau NFC.
![SECURITY KEY 2FA](assets/notext/02.webp)

Anda juga dapat membandingkan perangkat berdasarkan fitur tambahan seperti ketahanan terhadap air dan debu, serta bentuk dan ukuran kunci.

Mengenai merek kunci keamanan, Yubico adalah yang paling terkenal dengan perangkat YubiKeynya, yang secara pribadi saya gunakan dan rekomendasikan. Google juga menawarkan perangkat dengan Titan Security Key. Untuk alternatif open-source, SoloKeys (non OTP) dan NitroKey merupakan opsi yang menarik, namun saya belum pernah memiliki kesempatan untuk mengujinya.

Mengenai merek kunci keamanan, Yubico adalah yang paling terkenal dengan [perangkat YubiKey](https://www.yubico.com/), yang secara pribadi saya gunakan dan rekomendasikan. Google juga menawarkan perangkat bernama [Titan Security Key](https://store.google.com/fr/product/titan_security_key). Untuk alternatif open-source, [SoloKeys](https://solokeys.com/) (non-OTP) dan [NitroKey](https://www.nitrokey.com/products/nitrokeys) adalah pilihan menarik, namun saya belum pernah memiliki kesempatan untuk mengujinya.

## Bagaimana cara menggunakan kunci keamanan fisik?

Setelah Anda menerima kunci keamanan Anda, tidak diperlukan pengaturan khusus. Kunci tersebut biasanya siap digunakan saat diterima. Anda dapat segera menggunakannya untuk mengamankan akun online Anda yang mendukung jenis otentikasi ini. Sebagai contoh, saya akan menunjukkan cara mengamankan akun Proton Mail saya dengan kunci keamanan fisik ini.
![SECURITY KEY 2FA](assets/notext/03.webp)

Anda akan menemukan opsi untuk mengaktifkan 2FA di pengaturan akun Anda, sering kali di bawah bagian "*Password*" atau "*Keamanan*". Klik pada kotak centang atau tombol yang memungkinkan Anda mengaktifkan 2FA dengan kunci fisik.
![SECURITY KEY 2FA](assets/notext/04.webp)

Sambungkan kunci Anda ke komputer.
![SECURITY KEY 2FA](assets/notext/05.webp)

Sentuh tombol pada kunci keamanan Anda untuk memvalidasi.
![SECURITY KEY 2FA](assets/notext/06.webp)

Masukkan nama untuk mengingat kunci mana yang Anda gunakan.
![SECURITY KEY 2FA](assets/notext/07.webp)

Dan selesai, kunci keamanan Anda telah berhasil ditambahkan untuk otentikasi 2FA dari akun Anda.
![SECURITY KEY 2FA](assets/notext/08.webp)

Dalam contoh saya, jika saya mencoba menyambungkan kembali ke akun Proton Mail saya, saya akan terlebih dahulu diminta untuk memasukkan kata sandi beserta nama pengguna saya. Ini adalah faktor otentikasi pertama.
![SECURITY KEY 2FA](assets/notext/09.webp)

Kemudian, saya diminta untuk memasukkan kunci keamanan saya untuk faktor kedua dari otentikasi.
![SECURITY KEY 2FA](assets/notext/10.webp)

Selanjutnya, saya perlu menyentuh tombol pada kunci fisik untuk memvalidasi otentikasi, dan saya terhubung kembali ke akun Proton mail saya.
![SECURITY KEY 2FA](assets/notext/11.webp)

Ulangi operasi ini untuk semua akun online yang ingin Anda amankan dengan cara ini, terutama untuk akun penting seperti akun email Anda, manajer kata sandi Anda, layanan penyimpanan cloud dan online Anda, atau akun keuangan Anda.
