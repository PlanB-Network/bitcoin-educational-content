---
name: Stonewall x2
description: Memahami dan menggunakan transaksi Stonewall x2
---
![cover stonewall x2](assets/cover.webp)

***PERINGATAN:** Menyusul penangkapan pendiri Samourai Wallet dan penyitaan server mereka pada 24 April, transaksi Stonewallx2 hanya dapat berfungsi dengan pertukaran PSBT secara manual antara pihak-pihak yang terkait, asalkan kedua pengguna terhubung ke Dojo mereka sendiri. Namun, ada kemungkinan alat-alat ini dapat diluncurkan kembali dalam beberapa minggu mendatang. Sementara itu, Anda masih dapat membaca artikel ini untuk memahami operasi teoretis dari Stonewallx2 dan belajar cara melakukannya secara manual.*

_Jika Anda mempertimbangkan untuk melakukan Stonewallx2 secara manual, prosedurnya sangat mirip dengan yang dijelaskan dalam tutorial ini. Perbedaan utama terletak pada pilihan jenis transaksi Stonewallx2: alih-alih memilih `Online`, klik pada `In Person / Manual`. Kemudian, Anda perlu menukar PSBT secara manual untuk membangun transaksi Stonewallx2. Jika Anda berada dekat secara fisik dengan kolaborator Anda, Anda dapat memindai kode QR secara berturut-turut. Jika Anda berada jauh, file JSON dapat ditukar melalui saluran komunikasi yang aman. Sisa tutorial tetap tidak berubah._

_Kami terus mengikuti perkembangan kasus ini serta perkembangan terkait alat-alat yang terkait. Yakinlah bahwa kami akan memperbarui tutorial ini seiring informasi baru tersedia._

_Tutorial ini disediakan hanya untuk tujuan pendidikan dan informasi. Kami tidak mendukung atau mendorong penggunaan alat-alat ini untuk tujuan kriminal. Tanggung jawab setiap pengguna untuk mematuhi hukum di yurisdiksi mereka._

---

> *Jadikan setiap pengeluaran sebagai coinjoin.*

## Apa itu transaksi Stonewall x2?

Stonewall x2 adalah bentuk khusus transaksi Bitcoin yang bertujuan untuk meningkatkan privasi pengguna selama melakukan pembayaran, dengan berkolaborasi dengan pihak ketiga yang tidak terlibat dalam pembayaran tersebut. Metode ini mensimulasikan mini-coinjoin antara dua peserta, sambil melakukan pembayaran kepada pihak ketiga. Transaksi Stonewall x2 tersedia baik pada aplikasi Samourai Wallet maupun perangkat lunak Sparrow Wallet. Keduanya interoperabel.

Operasinya relatif sederhana: kita menggunakan UTXO yang kita miliki untuk melakukan pembayaran dan meminta bantuan dari pihak ketiga yang juga menyumbangkan UTXO milik mereka. Transaksi menghasilkan empat output: dua di antaranya dengan jumlah yang sama, satu ditujukan untuk alamat penerima pembayaran, yang lainnya ke alamat yang dimiliki oleh kolaborator. UTXO ketiga dikembalikan ke alamat lain milik kolaborator, memungkinkan mereka untuk mengambil kembali jumlah awal (sebuah tindakan netral bagi mereka, modulo biaya penambangan), dan UTXO terakhir kembali ke alamat yang dimiliki oleh kita, yang merupakan kembalian dari pembayaran.

Dengan demikian, tiga peran berbeda didefinisikan dalam transaksi Stonewall x2:
- Pengirim, yang melakukan pembayaran sebenarnya;
- Kolaborator, yang menyediakan bitcoin untuk meningkatkan anonimitas keseluruhan transaksi, sambil sepenuhnya memulihkan dana mereka di akhir (sebuah tindakan netral bagi mereka, modulo biaya penambangan);
- Penerima, yang mungkin tidak menyadari sifat spesifik dari transaksi dan hanya mengharapkan pembayaran dari pengirim.

Mari kita ambil contoh untuk lebih memahami. Alice berada di toko roti untuk membeli baguette-nya, yang harganya `4,000 sats`. Dia ingin membayar dengan bitcoin sambil mempertahankan tingkat privasi tertentu untuk pembayarannya. Oleh karena itu, dia meminta bantuan temannya, Bob, yang akan membantu dia dalam proses ini.
![schema stonewall x2](assets/en/1.webp)
Dengan menganalisis transaksi ini, kita dapat melihat bahwa tukang roti memang menerima `4,000 sats` sebagai pembayaran untuk baguette tersebut. Alice menggunakan `10,000 sats` sebagai input dan menerima `6,000 sats` sebagai output, menghasilkan saldo bersih `-4,000 sats`, yang sesuai dengan harga baguette. Sedangkan Bob, dia menyediakan `15,000 sats` sebagai input dan menerima dua output: satu sebesar `4,000 sats` dan yang lainnya `11,000 sats`, menghasilkan saldo `0`. Dalam contoh ini, saya sengaja mengabaikan biaya penambangan untuk memudahkan pemahaman. Dalam kenyataannya, biaya transaksi dibagi rata antara pengirim pembayaran dan kolaborator.

## Apa perbedaan antara Stonewall dan Stonewall x2?

Transaksi StonewallX2 bekerja persis seperti transaksi Stonewall, kecuali yang pertama bersifat kolaboratif sementara yang terakhir tidak. Seperti yang telah kita lihat, transaksi Stonewall x2 melibatkan partisipasi pihak ketiga, yang eksternal terhadap pembayaran, dan yang akan menyediakan bitcoin mereka untuk meningkatkan privasi transaksi. Dalam transaksi Stonewall biasa, peran kolaborator diambil oleh pengirim.

Mari kita kembali ke contoh Alice di toko roti. Jika dia tidak bisa menemukan seseorang seperti Bob untuk menemaninya dalam pengeluarannya, dia bisa melakukan transaksi Stonewall sendirian. Dengan demikian, dua UTXO input akan menjadi miliknya, dan dia akan menerima 3 di output.
![transaksi stonewall](assets/en/2.webp)

Dari sudut pandang eksternal, pola transaksi akan tetap sama.
![Stonewall atau Stonewall x2?](assets/en/5.webp)
Oleh karena itu, logika harus sebagai berikut ketika menggunakan alat pengeluaran Samourai:
- Jika pedagang tidak mendukung Payjoin Stowaway, transaksi kolaboratif dapat dilakukan dengan orang lain yang eksternal terhadap pembayaran menggunakan Stonewall x2.
- Jika tidak ada yang ditemukan untuk melakukan transaksi Stonewall x2, transaksi Stonewall dapat dilakukan sendirian, meniru perilaku transaksi Stonewall x2.
- Akhirnya, opsi terakhir adalah melakukan transaksi dengan JoinBot, server yang dipelihara oleh Samourai, yang dapat, atas permintaan, bertindak sebagai kolaborator dalam transaksi Stonewall x2.

Jika Anda ingin menemukan kolaborator yang bersedia membantu Anda dalam transaksi Stonewall X2, Anda juga dapat mengunjungi grup Telegram ini (tidak resmi) yang dipelihara oleh pengguna Samourai untuk menghubungkan pengirim dan kolaborator: [Make Every Spend a Coinjoin](https://t.me/EverySpendACoinjoin).

[**-> Pelajari lebih lanjut tentang transaksi Stonewall**](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)

## Apa tujuan dari transaksi Stonewall x2?

Struktur Stonewall x2 menambahkan jumlah entropi yang signifikan ke dalam transaksi dan membingungkan analisis rantai. Dari luar, transaksi seperti itu dapat diinterpretasikan sebagai Coinjoin kecil antara dua individu. Namun pada kenyataannya, itu adalah pembayaran. Metode ini menghasilkan ketidakpastian dalam analisis rantai, dan bahkan mengarah pada jejak palsu.

Mari kita kembali ke contoh Alice, Bob, dan Tukang Roti. Transaksi di blockchain akan terlihat seperti ini:
![stonewall x2 publik](assets/en/3.webp)
Seorang pengamat eksternal yang mengandalkan heuristik analisis rantai umum mungkin secara keliru menyimpulkan bahwa "Alice dan Bob melakukan coinjoin kecil, dengan satu UTXO masing-masing sebagai input dan dua UTXO masing-masing sebagai output." ![misinterpretation stonewall x2](assets/en/4.webp) Interpretasi ini salah karena, seperti yang Anda tahu, sebuah UTXO dikirim ke Baker, Alice hanya memiliki satu output kembalian, dan Bob memiliki dua.
![transaction stonewall x2](assets/en/1.webp)
Bahkan jika pengamat eksternal berhasil mengidentifikasi pola transaksi Stonewall x2, mereka tidak akan memiliki semua informasi. Mereka tidak akan dapat menentukan mana dari dua UTXO dengan jumlah yang sama yang sesuai dengan pembayaran. Selanjutnya, mereka tidak akan dapat mengetahui apakah itu Alice atau Bob yang melakukan pembayaran. Akhirnya, mereka tidak akan dapat menentukan apakah dua UTXO input berasal dari dua orang yang berbeda atau jika mereka milik satu orang yang menggabungkannya. Poin terakhir ini disebabkan oleh fakta bahwa transaksi Stonewall klasik, yang telah kita bahas di atas, mengikuti pola yang sama persis dengan transaksi Stonewall x2. Dari luar dan tanpa informasi tambahan tentang konteksnya, mustahil untuk membedakan transaksi Stonewall dari transaksi Stonewall x2. Namun, yang pertama bukanlah transaksi kolaboratif, sementara yang terakhir adalah. Ini menambahkan lebih banyak keraguan tentang pengeluaran ini.
![Stonewall atau Stonewall x2 ?](assets/en/5.webp)

## Bagaimana cara membangun koneksi antara Paynyms untuk dapat berkolaborasi melalui Soroban?

Seperti transaksi kolaboratif lainnya di Samourai (*Cahoots*), melakukan Stonewall x2 melibatkan pertukaran transaksi yang ditandatangani sebagian antara pengirim dan kolaborator. Pertukaran ini dapat dilakukan secara manual, jika Anda secara fisik bersama kolaborator Anda, atau secara otomatis melalui protokol komunikasi Soroban.

Jika Anda memilih opsi kedua, Anda perlu membangun koneksi antara Paynyms sebelum dapat melakukan Stonewall x2. Untuk melakukan ini, Paynym Anda harus "mengikuti" Paynym kolaborator Anda, dan sebaliknya.

**Mengakses Paynym kolaborator:**

Untuk memulai, perlu untuk mendapatkan kode pembayaran Paynym kolaborator Anda. Di aplikasi Samourai Wallet, kolaborator Anda harus menekan ikon Paynym mereka (robot kecil) yang terletak di kiri atas layar, kemudian klik pada julukan Paynym mereka, dimulai dengan `+...`. Sebagai contoh, milik saya adalah `+namelessmode0aF`.

![samourai paynym](assets/notext/6.webp)
Jika kolaborator Anda menggunakan Sparrow Wallet, mereka harus mengklik tab 'Tools', kemudian pada 'Show PayNym'. ![paynym sparrow](assets/notext/7.webp)
**Mengikuti PayNym kolaborator Anda dari Samourai Wallet:**

Jika Anda menggunakan Samourai Wallet, jalankan aplikasi dan akses menu 'PayNyms' dengan cara yang sama. Jika ini adalah kali pertama Anda menggunakan PayNym Anda, Anda perlu mendapatkan identifikasinya.

![request paynym samourai](assets/notext/8.webp)

Kemudian klik pada '+' biru di kanan bawah layar.
![add collaborator paynym](assets/notext/9.webp)
Anda kemudian dapat menempelkan kode pembayaran kolaborator Anda dengan memilih 'PASTE PAYMENT CODE', atau membuka kamera untuk memindai kode QR mereka dengan menekan 'SCAN QR CODE'.
![paste paynym identifier](assets/notext/10.webp)
Klik tombol 'FOLLOW'.
![follow paynym](assets/notext/11.webp)
Konfirmasi dengan mengklik 'YES'.
![confirm follow paynym](assets/notext/12.webp)
Perangkat lunak kemudian akan menawarkan tombol 'CONNECT'. Tidak perlu mengklik tombol ini untuk tutorial kita. Langkah ini hanya diperlukan jika Anda berencana untuk melakukan pembayaran kepada PayNym lain sebagai bagian dari [BIP47](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093), yang tidak terkait dengan tutorial kita.
![connect paynym](assets/notext/13.webp)
Setelah PayNym Anda mengikuti PayNym kolaborator Anda, ulangi proses ini dalam arah yang berlawanan sehingga kolaborator Anda juga dapat mengikuti Anda. Anda kemudian dapat melakukan transaksi Stonewall x2.

**Mengikuti PayNym kolaborator Anda dari Sparrow Wallet:**

Jika Anda menggunakan Sparrow Wallet, buka dompet Anda dan akses menu 'Show PayNym'. Jika Anda menggunakan PayNym Anda untuk pertama kalinya, Anda perlu mendapatkan pengenal dengan mengklik 'Retrieve PayNym'.
![request paynym sparrow](assets/notext/14.webp)
Kemudian masukkan pengenal PayNym kolaborator Anda (baik nama panggilan '+...' atau kode pembayaran mereka 'PM...') di kotak 'Find Contact', dan klik tombol 'Add Contact'.
![add contact paynym](assets/notext/15.webp)
Perangkat lunak kemudian akan menawarkan tombol 'Link Contact'. Tidak perlu mengklik tombol ini untuk tutorial kita. Langkah ini hanya diperlukan jika Anda berencana untuk melakukan pembayaran kepada PayNym yang ditunjuk sebagai bagian dari [BIP47](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093), yang tidak terkait dengan tutorial kita.

Setelah PayNym Anda mengikuti PayNym kolaborator Anda, ulangi proses ini dalam arah yang berlawanan sehingga kolaborator Anda juga dapat mengikuti Anda. Anda kemudian dapat melakukan transaksi Stonewall x2.
## Bagaimana cara melakukan transaksi Stonewall x2 di Samourai Wallet?

Jika Anda telah menyelesaikan langkah-langkah sebelumnya untuk menghubungkan Paynyms, Anda akhirnya siap untuk melakukan transaksi Stonewall x2! Untuk melakukan ini, ikuti tutorial video kami di Samourai Wallet:
![Stonewall x2 Tutorial - Samourai Wallet](https://youtu.be/89oYE1Hw3Fk?si=QTqUZ6IypiR6PPMr)

## Bagaimana cara melakukan transaksi Stonewall x2 di Sparrow Wallet?

Jika Anda telah menyelesaikan langkah-langkah sebelumnya untuk menghubungkan Paynyms, Anda akhirnya siap untuk melakukan transaksi Stonewall x2! Untuk melakukan ini, ikuti tutorial video kami di Sparrow Wallet:
![Stonewall x2 Tutorial - Sparrow Wallet](https://youtu.be/mO3Xpp34Hhk?si=bfYiTl0Gxjs9sNQq)

**Sumber eksternal:**
- https://sparrowwallet.com/docs/spending-privately.html;
- https://docs.samourai.io/en/spend-tools#stonewallx2.