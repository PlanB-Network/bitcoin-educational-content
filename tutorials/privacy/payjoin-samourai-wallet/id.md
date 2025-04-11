---
name: Payjoin - Samourai Wallet
description: Bagaimana cara melakukan transaksi Payjoin di Samourai Wallet?
---
![samourai payjoin cover](assets/cover.webp)

***PERHATIAN:** Menyusul penangkapan pendiri Samourai Wallet dan penyitaan server mereka pada tanggal 24 April, Payjoins Stowaway di Samourai Wallet hanya dapat berfungsi dengan menukar PSBT secara manual antara pihak-pihak yang terkait, dengan syarat kedua pengguna terhubung ke Dojo mereka sendiri. Sedangkan untuk Sparrow, Payjoins melalui BIP78 masih berfungsi. Namun, ada kemungkinan bahwa alat-alat ini akan diluncurkan kembali dalam beberapa minggu mendatang. Sementara itu, Anda masih dapat membaca artikel ini untuk memahami cara kerja teoritis dari Stowaway.*

_Jika Anda berencana untuk melakukan Stowaway secara manual, prosedurnya sangat mirip dengan yang dijelaskan dalam tutorial ini. Perbedaan utama terletak pada pilihan jenis transaksi Stowaway: alih-alih memilih `Online`, klik pada `In Person / Manual`. Kemudian, Anda perlu menukar PSBT secara manual untuk membangun transaksi Stowaway. Jika Anda berada dekat secara fisik dengan kolaborator Anda, Anda dapat memindai kode QR secara berurutan. Jika Anda berada jauh, file JSON dapat ditukar melalui saluran komunikasi yang aman. Sisa tutorial tetap tidak berubah._

_Kami terus mengikuti perkembangan kasus ini serta perkembangan terkait alat-alat yang terkait. Yakinlah bahwa kami akan memperbarui tutorial ini seiring informasi baru tersedia._

_Tutorial ini disediakan hanya untuk tujuan pendidikan dan informasi. Kami tidak mendukung atau mendorong penggunaan alat-alat ini untuk tujuan kriminal. Tanggung jawab setiap pengguna untuk mematuhi hukum di yurisdiksi mereka._

---

> *"Paksa mata-mata blockchain untuk memikirkan ulang segala yang mereka pikir mereka tahu."*

Payjoin adalah struktur transaksi Bitcoin spesifik yang meningkatkan privasi pengguna selama pembayaran dengan berkolaborasi dengan penerima pembayaran. Ada beberapa implementasi yang memfasilitasi pengaturan dan otomatisasi PayJoin. Di antara implementasi tersebut, yang paling dikenal adalah Stowaway, dikembangkan oleh tim di Samourai Wallet. Tutorial ini menjelaskan cara melakukan transaksi Payjoin Stowaway menggunakan aplikasi Samourai Wallet.

## Bagaimana Stowaway bekerja?

Seperti yang disebutkan sebelumnya, Samourai Wallet menawarkan alat PayJoin yang disebut "Stowaway." Ini dapat diakses melalui perangkat lunak Sparrow Wallet di PC atau aplikasi Samourai Wallet di Android. Untuk melakukan Payjoin, penerima, yang juga bertindak sebagai kolaborator, harus menggunakan perangkat lunak yang kompatibel dengan Stowaway, yaitu Sparrow atau Samourai. Kedua perangkat lunak ini interoperabel, memungkinkan transaksi Stowaway antara dompet Sparrow dan dompet Samourai, dan sebaliknya.

Stowaway mengandalkan kategori transaksi yang Samourai sebut sebagai "Cahoots." Cahoot pada dasarnya adalah transaksi kolaboratif antara beberapa pengguna, yang memerlukan pertukaran informasi off-chain. Sampai saat ini, Samourai menawarkan dua alat Cahoots: Stowaway (Payjoins) dan StonewallX2 (yang akan kita jelajahi dalam artikel mendatang).

Transaksi Cahoots melibatkan pertukaran transaksi yang ditandatangani sebagian antara pengguna. Proses ini bisa panjang dan merepotkan, terutama saat dilakukan dari jarak jauh. Namun, masih bisa dilakukan secara manual dengan pengguna lain, yang bisa nyaman jika kolaborator berada dekat secara fisik. Dalam praktiknya, ini melibatkan pertukaran lima kode QR yang harus dipindai secara berurutan.
Ketika dilakukan secara remote, proses ini menjadi terlalu kompleks. Untuk mengatasi masalah ini, Samourai telah mengembangkan protokol komunikasi terenkripsi berbasis Tor, yang disebut "Soroban." Dengan Soroban, pertukaran yang diperlukan untuk Payjoin diotomatisasi di balik antarmuka yang ramah pengguna. Ini adalah metode kedua yang akan kita pelajari dalam artikel ini.

Pertukaran terenkripsi ini memerlukan pembentukan koneksi dan autentikasi antara peserta Cahoots. Komunikasi Soroban oleh karena itu didasarkan pada Paynyms pengguna. Jika Anda tidak familiar dengan Paynyms, saya mengundang Anda untuk membaca artikel ini untuk detail lebih lanjut: [BIP47 - PAYNYM](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093).

Secara sederhana, Paynym adalah pengenal unik yang terkait dengan dompet Anda yang memungkinkan berbagai fungsionalitas, termasuk pesan terenkripsi. Paynym disajikan dalam bentuk pengenal dan ilustrasi yang mewakili robot. Berikut adalah contoh milik saya di Testnet: ![paynym samourai wallet](assets/en/1.webp)

**Ringkasan:**
- _Payjoin_ = Struktur spesifik dari transaksi kolaboratif;
- _Stowaway_ = Implementasi Payjoin yang tersedia di Samourai dan Sparrow Wallet;
- _Cahoots_ = Nama yang diberikan oleh Samourai untuk semua jenis transaksi kolaboratif mereka, termasuk Payjoin Stowaway;
- _Soroban_ = Protokol komunikasi terenkripsi yang didirikan di Tor, memungkinkan kolaborasi dengan pengguna lain dalam konteks transaksi Cahoots;
- _Paynym_ = Pengenal unik dari sebuah dompet yang memungkinkan komunikasi dengan pengguna lain di Soroban, untuk melakukan transaksi Cahoots.

[**-> Pelajari lebih lanjut tentang transaksi Payjoin dan kegunaannya**](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f)

## Bagaimana cara membangun koneksi antara Paynyms?

Untuk melakukan transaksi Cahoots secara remote, khususnya PayJoin (Stowaway) via Samourai, diperlukan untuk "Mengikuti" pengguna yang ingin Anda kolaborasi, menggunakan Paynym mereka. Dalam kasus Stowaway, ini berarti mengikuti orang yang ingin Anda kirimkan bitcoin.

**Berikut adalah prosedur untuk membangun koneksi ini:**

Untuk memulai, Anda perlu mendapatkan kode pembayaran dari Paynym penerima untuk Payjoin. Dalam aplikasi Samourai Wallet, penerima harus mengetuk ikon Paynym mereka (robot kecil) yang terletak di kiri atas layar, lalu klik pada julukan Paynym mereka, yang dimulai dengan `+...`. Sebagai contoh, milik saya adalah `+namelessmode0aF`. Jika kolaborator Anda menggunakan Sparrow Wallet, saya mengundang Anda untuk membaca tutorial khusus kami dengan mengklik di sini.

![koneksi paynym samourai](assets/notext/2.webp)

Kolaborator Anda kemudian akan diarahkan ke halaman Paynym mereka. Dari sana, mereka dapat berbagi kredensial Paynym mereka dengan Anda atau berbagi kode QR mereka untuk Anda pindai. Untuk melakukan ini, mereka harus mengetuk ikon "share" kecil yang terletak di kanan atas layar mereka.
![berbagi paynym samourai](assets/en/1.webp)

Di sisi Anda, jalankan aplikasi Samourai Wallet Anda dan akses menu "PayNyms" dengan cara yang sama. Jika ini adalah kali pertama Anda menggunakan Paynym Anda, Anda akan perlu mendapatkan pengenalnya.

![meminta paynym](assets/notext/3.webp)

Lalu klik pada "+" biru di kanan bawah layar.
![menambahkan paynym kolaborator](assets/notext/4.webp)
Anda kemudian dapat menempelkan kode pembayaran kolaborator Anda dengan memilih `COLLER LE CODE PAIEMENT`, atau membuka kamera untuk memindai kode QR mereka dengan menekan `SCANNEZ LE CODE QR`. ![tempel pengenal paynym](assets/notext/5.webp)
Klik tombol `SUIVRE`.
![ikuti paynym](assets/notext/6.webp)
Konfirmasi dengan mengklik `YES`.
![konfirmasi ikuti paynym](assets/notext/7.webp)
Perangkat lunak kemudian akan menawarkan Anda tombol `SE CONNECTER`. Tidak perlu mengklik tombol ini untuk tutorial kita. Langkah ini hanya diperlukan jika Anda berencana untuk melakukan pembayaran ke Paynym lain sebagai bagian dari [BIP47](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093), yang tidak terkait dengan tutorial kita.
![hubungkan paynym](assets/notext/8.webp)
Setelah Paynym penerima diikuti oleh Paynym Anda, ulangi operasi ini dalam arah yang berlawanan sehingga penerima juga mengikuti Anda. Anda kemudian dapat melakukan Payjoin.

## Bagaimana cara melakukan Payjoin di Samourai Wallet?

Jika Anda telah menyelesaikan langkah-langkah awal ini, Anda akhirnya siap untuk melakukan transaksi Payjoin! Untuk melakukan ini, ikuti tutorial video kami:

![Tutorial Video Payjoin - Samourai Wallet](https://youtu.be/FXW6XZim0ww?si=EXalYwK1t9DT48aE)

**Sumber eksternal:**
- https://docs.samourai.io/en/spend-tools#stowaway.