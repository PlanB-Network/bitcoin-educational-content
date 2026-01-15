---
name: Sparrow Wallet - Stonewall
description: Memahami dan menggunakan transaksi Stonewall pada Sparrow
---

![cover](assets/cover.webp)




> *Hancurkan asumsi analisis blockchain dengan keraguan yang dapat dibuktikan secara matematis antara pengirim dan penerima transaksi Anda*

## Apa yang dimaksud dengan transaksi Stonewall?



Stonewall adalah bentuk spesifik dari transaksi Bitcoin yang dirancang untuk meningkatkan kerahasiaan pengguna saat melakukan transaksi dengan meniru coinjoin antara dua orang, tanpa benar-benar melibatkan pihak lain. Pada praktiknya, transaksi ini tidak bersifat kolaboratif. Kamu bisa membuatnya sendiri hanya dengan menggunakan UTXO milikmu sebagai input. Jadi, kamu dapat membuat transaksi Stonewall kapan pun dibutuhkan, tanpa harus melakukan sinkronisasi dengan pengguna lain.

Transaksi Stonewall bekerja sebagai berikut: sebagai input transaksi, penerbit menggunakan 2 UTXO miliknya. Di sisi output, transaksi ini menghasilkan 4 output, dengan 2 di antaranya memiliki jumlah yang sama persis. Dua output lainnya adalah output kembalian. Dari 2 output dengan jumlah yang identik tersebut, hanya satu yang benar-benar dikirim ke penerima pembayaran.


Jadi hanya ada 2 peran dalam transaksi Stonewall:




- Penerbit, yang melakukan pembayaran aktual;
- Penerima, yang mungkin tidak menyadari sifat spesifik dari transaksi dan hanya mengharapkan pembayaran dari pengirim.



Mari kita ambil satu contoh untuk memahami struktur transaksi ini. Alice pergi ke toko roti untuk membeli roti baguette seharga '4.000 sats'. Ia ingin membayar dengan bitcoin sambil tetap menjaga kerahasiaan pembayarannya. Karena itu, Alice memutuskan untuk membuat transaksi Stonewall untuk melakukan pembayaran tersebut.


![image](assets/fr/01.webp)



Dengan menganalisis transaksi ini, kita dapat melihat bahwa tukang roti menerima '4.000 sats' sebagai pembayaran untuk baguette. Alice menggunakan 2 UTXO sebagai input: satu sebesar 10.000 sats dan satu lagi sebesar '15.000 sats'. Pada sisi output, ia memulihkan 3 UTXO: satu sebesar '4.000 sats', satu sebesar '6.000 sats', dan satu sebesar '11.000 sats'. Dengan demikian, Alice memiliki saldo bersih sebesar '-4.000 sats' pada transaksi ini, yang sesuai dengan harga baguette.

Dalam contoh ini, aku sengaja mengabaikan biaya mining agar lebih mudah dipahami. Pada praktiknya, biaya transaksi sepenuhnya ditanggung oleh penerbit.



## Apa perbedaan antara Stonewall dan Stonewall x2?



Transaksi Stonewall bekerja secara identik dengan transaksi StonewallX2, kecuali bahwa StonewallX2 membutuhkan kolaborasi, tidak seperti transaksi Stonewall klasik. Karena itu, transaksi ini dinamakan “x2”. Hal ini terjadi karena transaksi Stonewall dieksekusi tanpa memerlukan kerja sama eksternal: pengirim dapat melakukannya sendiri tanpa bantuan pihak lain. Sebaliknya, pada transaksi Stonewall x2, peserta tambahan yang dikenal sebagai “kolaborator” ikut terlibat dalam proses tersebut. Ia menyumbangkan bitcoin miliknya ke dalam transaksi bersama bitcoin milik pengirim, lalu mengambil kembali seluruh jumlah kontribusinya di akhir transaksi, dikurangi biaya mining.

Mari kita kembali ke contoh Alice di toko roti. Jika Alice ingin melakukan transaksi Stonewall x2, ia harus berkolaborasi dengan Bob sebagai pihak ketiga saat menyiapkan transaksi. Keduanya masing-masing akan membawa UTXO. Bob kemudian akan menerima kembali jumlah penuh kontribusinya saat transaksi selesai. Tukang roti tetap menerima pembayaran untuk baguette dengan cara yang sama seperti pada transaksi Stonewall, sementara Alice mendapatkan kembali saldo awalnya, dikurangi biaya baguette.



![image](assets/fr/02.webp)



Dari sudut pandang orang luar, transaksi tersebut akan tetap sama.



![image](assets/fr/03.webp)



Singkatnya, transaksi Stonewall dan Stonewall x2 memiliki struktur yang sama. Perbedaan di antara keduanya terletak pada sifat kolaboratif atau non-kolaboratifnya. Transaksi Stonewall dibuat secara individual tanpa memerlukan kolaborasi. Sebaliknya, transaksi Stonewall x2 bergantung pada kerja sama dua orang untuk menyusunnya.


[**-> Pelajari lebih lanjut tentang transaksi Stonewall x2**](https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)



## Apa gunanya transaksi Stonewall?



Struktur Stonewall menambahkan tingkat entropi yang tinggi pada transaksi, sehingga mengaburkan jalur analisis rantai. Dari sudut pandang eksternal, transaksi seperti ini bisa diartikan sebagai coinjoin kecil antara dua orang. Namun pada kenyataannya, seperti pada transaksi Stonewall x2, transaksi ini adalah sebuah pembayaran. Karena itu, metode ini menciptakan ketidakpastian dalam analisis rantai, bahkan dapat mengarahkan pengamat pada kesimpulan yang keliru.


Mari kita ambil contoh Alice di toko roti. Transaksi pada blockchain akan terlihat seperti ini:



![image](assets/fr/04.webp)



Seorang pengamat luar yang mengandalkan heuristik analisis rantai yang umum mungkin akan salah menyimpulkan bahwa "*dua orang telah membuat sebuah coinjoin kecil, dengan masing-masing satu UTXO sebagai input dan dua UTXO sebagai output*".



![image](assets/fr/05.webp)



Interpretasi ini tidak akurat, karena, seperti yang kamu ketahui, satu UTXO dikirim ke tukang roti, 2 UTXO yang masuk berasal dari Alices, dan dia memulihkan 3 output pertukaran.



![image](assets/fr/01.webp)



Bahkan jika pengamat luar berhasil mengidentifikasi pola transaksi Stonewall, ia tetap tidak memiliki seluruh informasi. Ia tidak dapat menentukan mana dari dua UTXO dengan jumlah yang sama yang merupakan pembayaran. Selain itu, ia juga tidak dapat memastikan apakah dua input UTXO tersebut berasal dari dua orang yang berbeda, atau justru keduanya milik satu orang yang digabungkan. Poin terakhir ini muncul karena transaksi Stonewall x2, seperti yang telah dijelaskan sebelumnya, mengikuti pola yang persis sama dengan transaksi Stonewall. Dilihat dari luar dan tanpa informasi kontekstual tambahan, tidak mungkin membedakan antara transaksi Stonewall dan transaksi Stonewall x2. Yang pertama bersifat non-kolaboratif, sedangkan yang kedua merupakan transaksi kolaboratif. Hal ini menambah tingkat keraguan dalam analisis biaya transaksi.



![image](assets/fr/03.webp)



## Bagaimana cara melakukan transaksi Stonewall di Sparrow?



Awalnya dikembangkan oleh tim Samurai Wallet, transaksi Stonewall kemudian diadopsi oleh aplikasi Ashigaru, sebuah fork dari wallet asli yang dibuat setelah penangkapan pengembang Samurai, serta oleh Sparrow Wallet.

Kamu perlu menginstal Sparrow dan membuat file:


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Tidak seperti transaksi Stowaway atau Stonewall x2 (*cahoots*), transaksi Stonewall tidak memerlukan penggunaan PayNym. Transaksi ini dapat dilakukan secara langsung tanpa persiapan khusus atau kolaborasi dengan pengguna lain.

Untuk melakukan transaksi Stonewall di Sparrow, langkah-langkahnya sangat sederhana: mulailah dengan membuat transaksi seperti biasa, baik melalui menu Kirim maupun dari menu UTXOs jika kamu ingin melakukan Kontrol Coin.



![Image](assets/fr/06.webp)



Kemudian masukkan detail transaksi: alamat penerima, label, jumlah yang akan dikirim, dan jumlah atau tarif, tergantung pada kondisi pasar.



![Image](assets/fr/07.webp)



Sebelum mengonfirmasi, di sinilah kamu dapat memilih struktur Stonewall. Di bagian bawah antarmuka, ganti 'Efficiency' menjadi 'Privacy'. Jika opsi ini tidak muncul, berarti wallet kamu tidak memiliki jumlah UTXO yang cukup untuk membangun jenis transaksi ini.


![Image](assets/fr/08.webp)



Setelah memilih opsi `Privacy`, kamu akan melihat bahwa struktur transaksi sepenuhnya berubah. Transaksi ini menjadi transaksi Stonewall, dengan menggunakan beberapa UTXO milikmu sebagai input dan menghasilkan dua output dengan jumlah yang sama, di mana salah satunya merupakan pembayaran aktual sebesar `100.000 sats`, di samping output kembalian.


![Image](assets/fr/09.webp)



Jika semuanya sudah benar, klik `Buat Transaksi`.



Kamu kemudian dapat memeriksa detail transaksi untuk terakhir kalinya, lalu klik `Finalize Transaction for Signing`.


![Image](assets/fr/10.webp)


Kemudian tandatangani transaksi sesuai dengan metode yang digunakan oleh wallet kamu, lalu klik `Broadcast Transaction` untuk menyiarkannya ke jaringan Bitcoin sambil menunggu konfirmasi.



![Image](assets/fr/11.webp)



Sekarang kamu sudah memahami cara kerja transaksi Stonewall di Sparrow Wallet dan cara membuatnya. Untuk memperdalam penguasaanmu atas alat-alat yang dirancang untuk memperkuat kerahasiaan on-chain kamu, aku mengajak kamu untuk mengikuti pelatihan BTC 204 milikku di Plan ₿ Academy:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c
