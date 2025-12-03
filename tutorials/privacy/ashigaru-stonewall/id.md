---
name: Ashigaru - Stonewall
description: Memahami dan menggunakan transaksi Stonewall di Ashigaru
---
![cover stonewall](assets/cover.webp)



> *Hancurkan asumsi analisis blockchain dengan keraguan yang dapat dibuktikan secara matematis antara pengirim dan penerima transaksi Anda*

## Apa yang dimaksud dengan transaksi Stonewall?



Stonewall adalah sebuah bentuk khusus dari transaksi Bitcoin yang dirancang untuk meningkatkan kerahasiaan pengguna ketika melakukan transaksi dengan meniru coinjoin antara dua orang, tanpa benar-benar menjadi satu. Pada kenyataannya, transaksi ini tidak bersifat kolaboratif. Seorang pengguna dapat membuatnya sendiri, dengan hanya menggunakan UTXO yang dimilikinya sebagai input. Jadi, Anda dapat membuat transaksi Stonewall untuk setiap kesempatan, tanpa harus melakukan sinkronisasi dengan pengguna lain.



Transaksi Stonewall bekerja sebagai berikut: sebagai input untuk transaksi, penerbit menggunakan 2 UTXO yang dimilikinya. Di sisi output, transaksi menghasilkan 4 output, 2 di antaranya memiliki jumlah yang sama persis. Dua lainnya adalah valuta asing. Dari 2 output dengan jumlah yang sama, hanya satu yang akan benar-benar masuk ke penerima.



Jadi hanya ada 2 peran dalam transaksi Stonewall:




- Penerbit, yang melakukan pembayaran aktual;
- Penerima, yang mungkin tidak menyadari sifat spesifik dari transaksi dan hanya mengharapkan pembayaran dari pengirim.



Mari kita ambil sebuah contoh untuk memahami struktur transaksi ini. Alice pergi ke toko roti untuk membeli roti baguette seharga `4.000 sats`. Ia ingin membayar dengan bitcoin, namun tetap menjaga kerahasiaan pembayarannya. Jadi, dia memutuskan untuk membuat transaksi Stonewall untuk pembayarannya.



![image](assets/fr/01.webp)



Dengan menganalisa transaksi ini, kita dapat melihat bahwa si pembuat roti telah menerima pembayaran sebesar `4.000 sats` untuk roti baguette tersebut. Alice menggunakan 2 UTXO sebagai input: satu dari `10.000 sats` dan satu lagi dari `15.000 sats`. Di sisi output, ia telah memulihkan 3 UTXO: satu dari `4.000 sats`, satu dari `6.000 sats` dan satu dari `11.000 sats`. Oleh karena itu, Alice memiliki saldo bersih sebesar `- 4.000 sats` pada transaksi ini, yang sesuai dengan harga baguette.



Dalam contoh ini, saya sengaja mengabaikan biaya mining agar lebih mudah dipahami. Pada kenyataannya, biaya transaksi ditanggung sepenuhnya oleh penerbit.



## Apa perbedaan antara Stonewall dan Stonewall x2?



Transaksi Stonewall bekerja secara identik dengan transaksi StonewallX2, kecuali bahwa transaksi StonewallX2 membutuhkan kolaborasi, tidak seperti transaksi Stonewall klasik, oleh karena itu dinamakan "x2". Hal ini dikarenakan transaksi Stonewall dieksekusi tanpa membutuhkan kerja sama eksternal: pengirim dapat melakukannya tanpa bantuan orang lain. Sebaliknya, untuk transaksi Stonewall x2, peserta tambahan, yang dikenal sebagai "kolaborator", bergabung dalam proses tersebut. Ia menyumbangkan bitcoin-nya sendiri ke dalam transaksi, bersama dengan bitcoin milik pengirim, dan mengambil alih seluruh jumlah di akhir transaksi (ditambah dengan biaya mining).



Mari kita kembali ke contoh kita dengan Alice di toko roti. Jika dia ingin melakukan transaksi Stonewall x2, Alice harus berkolaborasi dengan Bob (pihak ketiga) saat menyiapkan transaksi. Mereka masing-masing akan membawa UTXO. Bob kemudian akan menerima seluruh kontribusinya kembali. Tukang roti akan menerima pembayaran untuk baguette-nya dengan cara yang sama seperti pada transaksi Stonewall, sementara Alice akan mendapatkan kembali saldo awalnya, dikurangi biaya baguette.



![image](assets/fr/02.webp)



Dari sudut pandang orang luar, transaksi tersebut akan tetap sama.



![image](assets/fr/03.webp)



Singkatnya, transaksi Stonewall dan Stonewall x2 memiliki struktur yang sama. Perbedaan antara keduanya terletak pada sifat kolaboratif atau non-kolaboratif. Transaksi Stonewall dikembangkan secara individual, tanpa perlu kolaborasi. Transaksi Stonewall x2, di sisi lain, bergantung pada kerja sama antara dua orang untuk mengaturnya.



[**-> Pelajari lebih lanjut tentang transaksi Stonewall x2**](https://planb.academy/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)



## Apa gunanya transaksi Stonewall?



Struktur Stonewall menambahkan sejumlah besar entropi pada transaksi, mengaburkan garis analisis rantai. Dilihat dari luar, transaksi seperti itu dapat diartikan sebagai sebuah koin kecil antara dua orang. Namun pada kenyataannya, seperti transaksi Stonewall x2, ini adalah sebuah pembayaran. Oleh karena itu, metode ini menghasilkan ketidakpastian dalam analisis rantai, atau bahkan menyebabkan petunjuk yang salah.



Mari kita ambil contoh Alice di toko roti. Transaksi pada blockchain akan terlihat seperti ini:



![image](assets/fr/04.webp)



Seorang pengamat luar yang mengandalkan heuristik analisis rantai yang umum mungkin akan salah menyimpulkan bahwa "**dua orang telah membuat coinjoin kecil, dengan satu UTXO masing-masing sebagai input dan dua UTXO masing-masing sebagai output**".



![image](assets/fr/05.webp)



Interpretasi ini tidak akurat, karena, seperti yang Anda ketahui, satu UTXO dikirim ke tukang roti, 2 UTXO yang masuk berasal dari Alices, dan dia memulihkan 3 output nilai tukar.



![image](assets/fr/01.webp)



Bahkan jika pengamat luar berhasil mengidentifikasi pola transaksi Stonewall, dia tidak akan memiliki semua informasi. Dia tidak akan dapat menentukan mana dari dua UTXO dengan jumlah yang sama yang sesuai dengan pembayaran. Selain itu, ia tidak akan dapat menentukan apakah dua UTXO yang dimasukkan berasal dari dua orang yang berbeda, atau apakah mereka milik satu orang yang telah menggabungkannya. Poin terakhir ini disebabkan oleh fakta bahwa transaksi Stonewall x2, yang disebutkan di atas, mengikuti pola yang persis sama dengan transaksi Stonewall. Dilihat dari luar, dan tanpa informasi kontekstual tambahan, tidak mungkin untuk membedakan antara transaksi Stonewall dan transaksi Stonewall x2. Yang pertama bukanlah transaksi kolaboratif, sedangkan yang kedua adalah transaksi kolaboratif. Hal ini menambah keraguan terhadap biaya.



![image](assets/fr/03.webp)



## Bagaimana cara melakukan transaksi Stonewall di Ashigaru?



Awalnya dikembangkan oleh tim Samourai Wallet, transaksi Stonewall telah diambil alih oleh aplikasi Ashigaru, sebuah fork dari wallet asli yang dibuat setelah pengembang Samourai ditangkap. Anda harus menginstal Ashigaru dan membuat wallet:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Tidak seperti transaksi Stowaway atau Stonewall x2 (*cahoots*), transaksi Stonewall tidak memerlukan penggunaan Paynyms. Transaksi ini dapat dieksekusi secara langsung, tanpa persiapan atau kolaborasi dengan pengguna lain.



Bahkan, Anda tidak benar-benar membutuhkan tutorial untuk melakukan transaksi Stonewall, karena Ashigaru membuatnya secara otomatis setiap kali Anda melakukan pembelanjaan, segera setelah wallet Anda berisi cukup UTXO.



Klik tombol `+` di bagian kanan bawah layar, lalu pilih `Kirim`.



![Image](assets/fr/06.webp)



Pilih rekening yang ingin Anda gunakan untuk melakukan pengeluaran.



![Image](assets/fr/07.webp)



Kemudian masukkan detail transaksi: alamat penerima dan jumlah yang akan dikirim, lalu tekan tanda panah untuk mengonfirmasi.



![Image](assets/fr/08.webp)



Di sini, Anda tentu saja dapat menyesuaikan biaya transaksi default sesuai dengan kondisi pasar. Namun, elemen yang paling menarik di halaman ini adalah tipe transaksi. Anda akan melihat bahwa Ashigaru secara otomatis memilih `STONEWALL`. Klik tombol `PREVIEW` untuk mengetahui lebih lanjut.



![Image](assets/fr/09.webp)



Anda bisa melihat bahwa transaksi ini memang merupakan tipe Stonewall: terdiri dari 2 input dengan jumlah yang sama, 2 output dengan jumlah yang sama, serta output penukaran, dan, dalam kasus saya, sebuah input tambahan untuk memenuhi jumlah pembayaran.



![Image](assets/fr/10.webp)



Jika Anda tidak ingin melakukan transaksi Stonewall, tetapi lebih memilih pembayaran konvensional, klik ikon pensil di bagian kanan atas layar, lalu pilih `Simple`, bukan `STONEWALL`.



![Image](assets/fr/11.webp)



Setelah Anda memeriksa semua detail, seret panah hijau di bagian bawah layar untuk menandatangani dan melepaskan transaksi.



![Image](assets/fr/12.webp)



Sekarang Anda sudah mengetahui cara melakukan transaksi Stonewall, dan yang lebih penting lagi, bagaimana cara kerjanya. Jika Anda ingin mengetahui lebih lanjut, lihat tutorial saya di Ashigaru Terminal, yang menjelaskan cara membuat coinjoin melalui Whirlpool.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add