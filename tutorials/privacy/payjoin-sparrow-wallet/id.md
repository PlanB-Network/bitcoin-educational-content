---
name: Payjoin - Sparrow Wallet
description: Bagaimana cara melakukan transaksi Payjoin pada Sparrow Wallet?
---
![gambar tutorial sparrow payjoin](assets/cover.webp)

_**PERINGATAN:** Menyusul penangkapan pendiri Samourai Wallet dan penyitaan server mereka pada 24 April, Payjoins Stowaway di Samourai Wallet kini hanya dapat dilakukan dengan pertukaran PSBT secara manual antara pihak-pihak yang terlibat, asalkan kedua pengguna terhubung ke Dojo mereka sendiri. Sedangkan untuk Sparrow, Payjoins melalui BIP78 masih berfungsi. Namun, alat-alat ini mungkin akan diaktifkan kembali dalam beberapa minggu mendatang. Sementara itu, Anda tetap dapat membaca artikel ini untuk memahami fungsi teoritis dari payjoins._

_Kami terus mengikuti perkembangan kasus ini serta perkembangan terkait alat-alat yang terkait. Yakinlah bahwa kami akan memperbarui tutorial ini seiring dengan tersedianya informasi baru._

_Tutorial ini disediakan hanya untuk tujuan pendidikan dan informasi. Kami tidak mendukung atau mendorong penggunaan alat-alat ini untuk tujuan kriminal. Tanggung jawab setiap pengguna adalah untuk mematuhi hukum di yurisdiksi mereka._

---

> *"Paksa mata-mata blockchain untuk memikirkan ulang segala yang mereka kira mereka tahu."*

Payjoin adalah struktur transaksi Bitcoin spesifik yang meningkatkan privasi pengguna saat melakukan pembayaran dengan berkolaborasi dengan penerima pembayaran. Ada beberapa implementasi yang memfasilitasi pengaturan dan otomatisasi PayJoin. Di antara implementasi tersebut, yang paling dikenal adalah Stowaway yang dikembangkan oleh tim Samourai Wallet. Tutorial ini bertujuan untuk memandu Anda melalui proses melakukan transaksi Payjoin Stowaway menggunakan perangkat lunak Sparrow Wallet.

## Bagaimana cara kerja Stowaway?

Seperti yang disebutkan sebelumnya, Samourai Wallet menawarkan alat PayJoin yang disebut "Stowaway." Ini dapat diakses melalui perangkat lunak Sparrow Wallet di PC atau aplikasi Samourai Wallet di Android. Untuk melakukan Payjoin, penerima, yang juga bertindak sebagai kolaborator, harus menggunakan perangkat lunak yang kompatibel dengan Stowaway, yaitu Sparrow atau Samourai Wallet. Kedua perangkat lunak ini interoperabel, memungkinkan transaksi Stowaway antara dompet Sparrow dan dompet Samourai, dan sebaliknya.

Stowaway mengandalkan kategori transaksi yang Samourai sebut sebagai "Cahoots." Cahoot pada dasarnya adalah transaksi kolaboratif antara beberapa pengguna yang memerlukan pertukaran informasi di luar rantai. Saat ini, Samourai menawarkan dua alat Cahoots: Stowaway (Payjoins) dan StonewallX2 (yang akan kita jelajahi dalam artikel mendatang).

Transaksi Cahoots melibatkan pertukaran transaksi yang ditandatangani sebagian antara pengguna. Proses ini bisa panjang dan merepotkan, terutama saat dilakukan dari jarak jauh. Namun, ini masih bisa dilakukan secara manual dengan pengguna lain, yang bisa nyaman jika kolaborator berada dalam jarak dekat secara fisik. Dalam praktiknya, ini melibatkan pertukaran lima kode QR yang harus discan secara berurutan.

Ketika dilakukan dari jarak jauh, proses ini menjadi terlalu kompleks. Untuk mengatasi masalah ini, Samourai telah mengembangkan protokol komunikasi terenkripsi berbasis Tor, yang disebut "Soroban." Dengan Soroban, pertukaran yang diperlukan untuk Payjoin diotomatisasi di balik antarmuka yang ramah pengguna. Ini adalah metode kedua yang akan kita jelajahi dalam artikel ini.

Pertukaran terenkripsi ini memerlukan pembentukan koneksi dan otentikasi antara peserta Cahoots. Komunikasi Soroban mengandalkan Paynyms pengguna. Jika Anda tidak familiar dengan Paynyms, saya mengundang Anda untuk merujuk ke artikel ini untuk detail lebih lanjut: [BIP47 - PAYNYM](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093).
Untuk menyederhanakannya, Paynym adalah pengenal unik yang terkait dengan dompet Anda yang memungkinkan berbagai fungsi, termasuk pesan terenkripsi. Paynym disajikan dalam bentuk pengenal dan ilustrasi yang mewakili sebuah robot. Berikut adalah contoh milik saya di Testnet: ![Paynym Sparrow](assets/en/1.webp)
**Ringkasan:**
- *Payjoin* = Struktur transaksi kolaboratif tertentu;
- *Stowaway* = Implementasi Payjoin yang tersedia di Samourai dan Sparrow Wallet;
- *Cahoots* = Nama yang diberikan oleh Samourai untuk semua jenis transaksi kolaboratif mereka, termasuk Payjoin Stowaway;
- *Soroban* = Protokol komunikasi terenkripsi yang didirikan di Tor, memungkinkan kolaborasi dengan pengguna lain dalam konteks transaksi Cahoots.
- *Paynym* = Pengenal unik dari sebuah dompet yang memungkinkan komunikasi dengan pengguna lain di Soroban, untuk melakukan transaksi Cahoots.

[**-> Pelajari lebih lanjut tentang transaksi Payjoin dan kegunaannya**](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f)

## Bagaimana cara menghubungkan Paynyms?

Untuk melakukan transaksi Cahoots dari jarak jauh, khususnya PayJoin (Stowaway) melalui Samourai atau Sparrow, diperlukan untuk "Mengikuti" pengguna yang ingin Anda kolaborasi dengannya, menggunakan Paynym mereka. Dalam kasus Stowaway, ini berarti mengikuti orang yang ingin Anda kirimkan bitcoin.

**Berikut adalah prosedur untuk menghubungkan ini:**

Pertama, Anda perlu mendapatkan pengenal Paynym penerima. Ini dapat dilakukan menggunakan nama panggilan atau kode pembayaran mereka. Untuk melakukan ini, dari dompet Sparrow penerima, pilih tab `Tools`, lalu klik pada `Show PayNym`.
![Show Paynym](assets/notext/2.webp)
![Paynym Sparrow](assets/en/1.webp)
Di sisi Anda, buka Sparrow Wallet Anda dan akses menu `Show PayNym` yang sama. Jika Anda menggunakan Paynym Anda untuk pertama kalinya, Anda perlu mendapatkan pengenal dengan mengklik `Retrieve PayNym`.
![Retrieve paynym](assets/notext/3.webp)
Selanjutnya, masukkan pengenal Paynym kolaborator Anda (baik nama panggilan mereka `+...` atau kode pembayaran mereka `PM...`) di kotak `Find Contact`, lalu klik tombol `Add Contact`.
![add contact](assets/notext/4.webp)
Perangkat lunak kemudian akan menawarkan Anda tombol `Link Contact`. Tidak perlu mengklik tombol ini untuk tutorial kita. Langkah ini hanya diperlukan jika Anda berencana melakukan pembayaran ke Paynym yang ditunjukkan dalam konteks [BIP47](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093), yang tidak terkait dengan tutorial kita.

Setelah Paynym penerima diikuti oleh Paynym Anda, ulangi operasi ini dalam arah yang berlawanan sehingga penerima Anda juga mengikuti Anda. Anda kemudian dapat melakukan Payjoin.

## Bagaimana cara melakukan Payjoin di Sparrow Wallet?
Jika Anda telah menyelesaikan beberapa langkah awal ini, Anda akhirnya siap untuk melakukan transaksi Payjoin! Untuk melakukan ini, ikuti tutorial video kami:
![Payjoin Tutorial - Sparrow Wallet](https://youtu.be/ZQxKod3e0Mg)

**Sumber eksternal:**
- https://docs.samourai.io/en/spend-tools#stowaway ;
- https://sparrowwallet.com/docs/spending-privately.html.