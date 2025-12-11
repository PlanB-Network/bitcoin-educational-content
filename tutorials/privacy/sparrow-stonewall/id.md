---
name: Sparrow Wallet - Stonewall
description: Memahami dan menggunakan transaksi Stonewall pada Sparrow
---

![cover](assets/cover.webp)




> *Hancurkan asumsi analisis blockchain dengan keraguan yang dapat dibuktikan secara matematis antara pengirim dan penerima transaksi Anda*

## Apa yang dimaksud dengan transaksi Stonewall?



Stonewall adalah sebuah bentuk spesifik dari transaksi Bitcoin yang dirancang untuk meningkatkan kerahasiaan pengguna ketika melakukan transaksi dengan meniru coinjoin antara dua orang, tanpa benar-benar menjadi satu. Pada kenyataannya, transaksi ini tidak bersifat kolaboratif. Seorang pengguna dapat membuatnya sendiri, dengan hanya menggunakan UTXO yang dimilikinya sebagai input. Jadi, Anda dapat membuat transaksi Stonewall untuk setiap kesempatan, tanpa harus melakukan sinkronisasi dengan pengguna lain.



Transaksi Stonewall bekerja sebagai berikut: sebagai input untuk transaksi, penerbit menggunakan 2 UTXO yang dimilikinya. Di sisi output, transaksi menghasilkan 4 output, 2 di antaranya memiliki jumlah yang sama persis. Dua lainnya adalah valuta asing. Dari 2 output dengan jumlah yang sama, hanya satu yang akan benar-benar masuk ke penerima pembayaran.



Jadi hanya ada 2 peran dalam transaksi Stonewall:




- Penerbit, yang melakukan pembayaran aktual;
- Penerima, yang mungkin tidak menyadari sifat spesifik dari transaksi dan hanya mengharapkan pembayaran dari pengirim.



Mari kita ambil sebuah contoh untuk memahami struktur transaksi ini. Alice pergi ke toko roti untuk membeli roti baguette seharga `4.000 sats`. Ia ingin membayar dengan bitcoin, namun tetap menjaga kerahasiaan pembayarannya. Jadi, dia memutuskan untuk membuat transaksi Stonewall untuk pembayarannya.



![image](assets/fr/01.webp)



Dengan menganalisis transaksi ini, kita dapat melihat bahwa tukang roti telah menerima `4.000 sats` sebagai pembayaran untuk baguette. Alice menggunakan 2 UTXO sebagai input: satu dari `10.000 sats` dan satu lagi dari `15.000 sats`. Pada output, ia telah memulihkan 3 UTXO: satu dari `4.000 sats`, satu dari `6.000 sats` dan satu dari `11.000 sats`. Oleh karena itu, Alice memiliki saldo bersih sebesar `- 4.000 sats` pada transaksi ini, yang sesuai dengan harga baguette.



Dalam contoh ini, saya sengaja mengabaikan biaya mining agar lebih mudah dipahami. Pada kenyataannya, biaya transaksi ditanggung sepenuhnya oleh penerbit.



## Apa perbedaan antara Stonewall dan Stonewall x2?



Transaksi Stonewall bekerja secara identik dengan transaksi StonewallX2, kecuali bahwa transaksi StonewallX2 membutuhkan kolaborasi, tidak seperti transaksi Stonewall klasik, oleh karena itu dinamakan "x2". Hal ini dikarenakan transaksi Stonewall dieksekusi tanpa membutuhkan kerja sama eksternal: pengirim dapat melakukannya tanpa bantuan orang lain. Sebaliknya, untuk transaksi Stonewall x2, peserta tambahan, yang dikenal sebagai "kolaborator", bergabung dalam proses tersebut. Ia menyumbangkan bitcoin-nya sendiri ke dalam transaksi, bersama dengan bitcoin milik pengirim, dan mengambil alih seluruh jumlah di akhir transaksi (dikurangi biaya mining).



Mari kita kembali ke contoh kita dengan Alice di toko roti. Jika dia ingin melakukan transaksi Stonewall x2, Alice harus berkolaborasi dengan Bob (pihak ketiga) saat menyiapkan transaksi. Mereka masing-masing akan membawa UTXO. Bob kemudian akan menerima jumlah penuh kontribusinya saat keluar. Tukang roti akan menerima pembayaran untuk baguette-nya dengan cara yang sama seperti pada transaksi Stonewall, sementara Alice akan mendapatkan kembali saldo awalnya, dikurangi biaya baguette.



![image](assets/fr/02.webp)



Dari sudut pandang orang luar, transaksi tersebut akan tetap sama.



![image](assets/fr/03.webp)



Singkatnya, transaksi Stonewall dan Stonewall x2 memiliki struktur yang sama. Perbedaan antara keduanya terletak pada sifat kolaboratif atau non-kolaboratif. Transaksi Stonewall dikembangkan secara individual, tanpa perlu kolaborasi. Transaksi Stonewall x2, di sisi lain, bergantung pada kerja sama antara dua orang untuk mengaturnya.



[**-> Pelajari lebih lanjut tentang transaksi Stonewall x2**](https://planb.academy/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)



## Apa gunanya transaksi Stonewall?



Struktur Stonewall menambahkan sejumlah besar entropi pada transaksi, mengaburkan garis analisis rantai. Dilihat dari luar, transaksi seperti ini dapat diartikan sebagai sebuah koin kecil antara dua orang. Namun pada kenyataannya, seperti transaksi Stonewall x2, transaksi ini adalah sebuah pembayaran. Oleh karena itu, metode ini menghasilkan ketidakpastian dalam analisis rantai, atau bahkan menyebabkan petunjuk yang salah.



Mari kita ambil contoh Alice di toko roti. Transaksi pada blockchain akan terlihat seperti ini:



![image](assets/fr/04.webp)



Seorang pengamat luar yang mengandalkan heuristik analisis rantai yang umum mungkin akan salah menyimpulkan bahwa "*dua orang telah membuat sebuah coinjoin kecil, dengan masing-masing satu UTXO sebagai input dan dua UTXO sebagai output*".



![image](assets/fr/05.webp)



Interpretasi ini tidak akurat, karena, seperti yang Anda ketahui, satu UTXO dikirim ke tukang roti, 2 UTXO yang masuk berasal dari Alices, dan dia memulihkan 3 output pertukaran.



![image](assets/fr/01.webp)



Bahkan jika pengamat luar berhasil mengidentifikasi pola transaksi Stonewall, dia tidak akan memiliki semua informasi. Dia tidak akan dapat menentukan mana dari dua UTXO dengan jumlah yang sama yang sesuai dengan pembayaran. Selain itu, ia tidak akan dapat menentukan apakah dua entri UTXO tersebut berasal dari dua orang yang berbeda, atau apakah keduanya milik satu orang yang telah menggabungkannya. Poin terakhir ini disebabkan oleh fakta bahwa transaksi Stonewall x2, yang disebutkan di atas, mengikuti pola yang sama persis dengan transaksi Stonewall. Dilihat dari luar dan tanpa informasi kontekstual tambahan, tidak mungkin untuk membedakan antara transaksi Stonewall dan transaksi Stonewall x2. Yang pertama bukanlah transaksi kolaboratif, sedangkan yang kedua adalah transaksi kolaboratif. Hal ini menambah keraguan pada biaya.



![image](assets/fr/03.webp)



## Bagaimana cara melakukan transaksi Stonewall di Sparrow?



Awalnya dikembangkan oleh tim Samurai Wallet, transaksi Stonewall diambil alih oleh aplikasi Ashigaru, fork dari portofolio asli yang dibuat setelah penangkapan pengembang Samurai, dan juga pada Sparrow Wallet.



Anda harus menginstal Sparrow dan membuat file :



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Tidak seperti transaksi Stowaway atau Stonewall x2 (*kongkalikong*), transaksi Stonewall tidak memerlukan penggunaan Paynyms. Transaksi ini dapat dilakukan secara langsung, tanpa persiapan khusus atau kolaborasi dengan pengguna lain.



Untuk melakukan transaksi Stonewall pada Sparrow, prosedurnya sangat sederhana: mulailah dengan membuat transaksi seperti biasa, baik melalui menu `Kirim`, atau dari menu `UTXOs` jika Anda ingin melakukan *Kontrol Coin*.



![Image](assets/fr/06.webp)



Kemudian masukkan detail transaksi: alamat penerima, label, jumlah yang akan dikirim, dan jumlah atau tarif, tergantung pada kondisi pasar.



![Image](assets/fr/07.webp)



Sebelum mengonfirmasi, di sinilah Anda dapat memilih struktur Stonewall. Di bagian bawah antarmuka, ganti `Efficiency` dengan `Privacy`. Jika opsi ini tidak muncul, ini berarti portofolio Anda tidak memiliki jumlah UTXO yang cukup untuk membangun jenis transaksi ini.



![Image](assets/fr/08.webp)



Setelah memilih opsi `Privasi`, Anda akan melihat bahwa struktur transaksi sepenuhnya dimodifikasi: transaksi ini menjadi transaksi Stonewall, menggunakan beberapa UTXO Anda sebagai input dan menghasilkan dua output dengan jumlah yang sama, yang salah satunya sesuai dengan pembayaran aktual sebesar `100.000 sats`, di samping output pertukaran.



![Image](assets/fr/09.webp)



Jika semuanya sudah benar, klik `Buat Transaksi`.



Anda kemudian dapat memeriksa detail transaksi Anda untuk terakhir kalinya, dan klik `Finalize Transaction for Signing`.



![Image](assets/fr/10.webp)



Kemudian tandatangani transaksi sesuai dengan metode khusus untuk portofolio Anda, dan klik `Broadcast Transaction` untuk menyiarkannya di jaringan Bitcoin, sambil menunggu konfirmasi.



![Image](assets/fr/11.webp)



Sekarang Anda sudah mengetahui cara kerja transaksi Stonewall pada Sparrow Wallet dan cara membuatnya. Untuk memperdalam penguasaan Anda atas alat-alat yang dirancang untuk memperkuat kerahasiaan onchain Anda, saya mengundang Anda untuk mengikuti pelatihan BTC 204 saya di Plan ₿ Academy:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c