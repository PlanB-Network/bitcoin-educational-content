---
name: Ashigaru - Stonewall x2
description: Memahami dan menggunakan transaksi Stonewall x2 di Ashigaru
---
![cover stonewall x2](assets/cover.webp)



> *Jadikan setiap pengeluaran sebagai koin bersama

## Apa yang dimaksud dengan transaksi Stonewall x2?



Stonewall x2 adalah bentuk khusus dari transaksi Bitcoin yang dirancang untuk meningkatkan kerahasiaan pengguna ketika melakukan pembelanjaan, dengan berkolaborasi dengan pihak ketiga yang tidak terlibat dalam pembelanjaan. Metode ini mensimulasikan sebuah mini-coinjoin antara dua partisipan, ketika melakukan pembayaran kepada pihak ketiga. Transaksi Stonewall x2 tersedia di aplikasi Ashigaru, sebuah fork dari Samourai Wallet (tim di balik pembuatan jenis transaksi ini).



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Cara kerjanya relatif sederhana: Anda menggunakan UTXO yang Anda miliki untuk melakukan pembayaran, dan meminta bantuan pihak ketiga yang juga berkontribusi dengan UTXO mereka sendiri. Transaksi berakhir dengan empat keluaran: dua di antaranya dalam jumlah yang sama, satu ditujukan ke alamat penerima pembayaran, yang lainnya ke alamat milik kolaborator. UTXO ketiga dikembalikan ke alamat lain milik kolaborator, memungkinkannya untuk mendapatkan kembali jumlah awal (tindakan netral baginya, modulo biaya mining), dan UTXO terakhir dikembalikan ke alamat milik kami, yang merupakan pertukaran pembayaran.



Dengan demikian, ada tiga peran yang berbeda dalam transaksi Stonewall x2:




- Penerbit, yang melakukan pembayaran aktual;
- Kolaborator, yang menyediakan bitcoin untuk meningkatkan anonimitas transaksi, sambil memulihkan dananya secara penuh pada akhirnya (tindakan netral baginya, modulo biaya mining);
- Penerima, yang mungkin tidak menyadari sifat spesifik dari transaksi dan hanya mengharapkan pembayaran dari pengirim.



Mari kita ambil sebuah contoh. Alice sedang berada di toko roti untuk membeli roti baguette seharga `4.000 sats`. Ia ingin membayar dengan bitcoin, namun tetap ingin menjaga kerahasiaan pembayarannya. Jadi dia memanggil temannya Bob, yang akan membantunya dalam hal ini.



![image](assets/fr/01.webp)



Dengan menganalisis transaksi ini, kita dapat melihat bahwa pembuat roti sebenarnya menerima `4.000 sats` sebagai pembayaran untuk roti baguette. Alice menggunakan `10.000 sats` sebagai input dan menerima `6.000 sats` sebagai output, sehingga menghasilkan saldo bersih `-4.000 sats`, yang sesuai dengan harga roti baguette. Sedangkan untuk Bob, Bob memasok `15.000 sats` dalam bentuk input dan menerima dua output: satu sebesar `4.000 sats` dan yang lainnya sebesar `11.000 sats`, sehingga menghasilkan saldo `0`.



Dalam contoh ini, saya sengaja mengabaikan biaya mining agar lebih mudah dipahami. Pada kenyataannya, biaya transaksi dibagi rata antara penerbit pembayaran dan kolaborator.



## Apa perbedaan antara Stonewall dan Stonewall x2?



Transaksi StonewallX2 bekerja dengan cara yang sama persis dengan transaksi Stonewall, kecuali yang pertama bersifat kolaboratif, sedangkan yang kedua tidak. Seperti yang telah kita lihat, transaksi StonewallX2 melibatkan partisipasi pihak ketiga, yang berada di luar pembayaran, dan yang akan menyediakan bitcoin-nya untuk meningkatkan kerahasiaan transaksi. Dalam transaksi Stonewall klasik, peran kolaborator diambil oleh pengirim.



Mari kita kembali ke contoh Alice di toko roti. Jika dia tidak dapat menemukan seseorang seperti Bob untuk menemaninya berbelanja, dia bisa saja melakukan Stonewall sendirian. Dengan begitu, dua UTXO dalam perjalanan masuk akan menjadi miliknya, dan dia akan mendapatkan 3 UTXO dalam perjalanan keluar.



![image](assets/fr/02.webp)




Dari sudut pandang orang luar, transaksi akan tetap sama.



![image](assets/fr/05.webp)



Oleh karena itu, logikanya adalah sebagai berikut ketika Anda ingin menggunakan alat belanja Ashigaru:




- Jika pedagang tidak mendukung Payjoin Stowaway, Anda dapat melakukan transaksi kolaboratif dengan orang lain di luar pembayaran berkat Stonewall x2 ;
- Jika Anda tidak dapat menemukan siapa pun untuk melakukan transaksi Stonewall x2, Anda dapat melakukan transaksi Stonewall saja, yang akan meniru perilaku transaksi Stonewall x2.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-033daa45-d42c-40e1-9511-cea89751c3d4

## Apa gunanya transaksi Stonewall x2?



Struktur Stonewall x2 menambahkan sejumlah besar entropi ke dalam transaksi, mengacaukan analisis rantai. Dilihat dari luar, transaksi seperti itu dapat ditafsirkan sebagai Coinjoin kecil antara dua orang. Namun pada kenyataannya, ini adalah sebuah pembayaran. Oleh karena itu, metode ini menciptakan ketidakpastian dalam analisis rantai, atau bahkan menyebabkan petunjuk yang salah.



Mari kita ambil contoh Alice, Bob, dan Boulanger. Transaksi pada blockchain akan terlihat seperti ini:



![image](assets/fr/03.webp)



Seorang pengamat luar yang mengandalkan heuristik analisis rantai umum mungkin akan salah menyimpulkan bahwa "*Alice dan Bob telah membuat coinjoin kecil, dengan masing-masing satu UTXO masuk dan dua UTXO keluar*".



![image](assets/fr/04.webp)



Interpretasi ini salah karena, seperti yang Anda ketahui, UTXO dikirim ke Boulanger, Alice hanya memiliki satu output pertukaran, dan Bob memiliki dua.



![image](assets/fr/01.webp)



Bahkan jika pengamat luar berhasil mengidentifikasi patern dari transaksi Stonewall x2, dia tidak akan memiliki semua informasi. Dia tidak akan dapat menentukan mana dari dua UTXO dengan jumlah yang sama yang sesuai dengan pembayaran. Ia juga tidak akan dapat menentukan apakah Alice atau Bob yang melakukan pembayaran. Terakhir, dia tidak akan dapat menentukan apakah dua UTXO yang dimasukkan berasal dari dua orang yang berbeda, atau apakah mereka milik satu orang yang telah menggabungkannya. Poin terakhir ini disebabkan oleh fakta bahwa transaksi Stonewall klasik, yang dibahas di atas, mengikuti pola yang sama persis dengan transaksi Stonewall x2. Dilihat dari luar dan tanpa informasi kontekstual tambahan, tidak mungkin untuk membedakan transaksi Stonewall dengan transaksi Stonewall x2. Yang pertama bukanlah transaksi kolaboratif, sedangkan yang kedua adalah transaksi kolaboratif. Hal ini menambah keraguan terhadap biaya.



![image](assets/fr/05.webp)




## Bagaimana cara membuat koneksi antara Paynyms?



Seperti halnya transaksi kolaboratif lainnya di Ashigaru (*Cahoots*), Stonewall x2 melibatkan pertukaran transaksi yang ditandatangani sebagian antara pengirim dan kolaborator. Pertukaran ini dapat dilakukan secara manual, jika Anda hadir secara fisik dengan kolaborator Anda, atau secara otomatis menggunakan protokol komunikasi Soroban.



Jika Anda memilih opsi kedua, Anda harus membuat koneksi antara Paynym sebelum Anda dapat melakukan Stonewall x2. Untuk melakukan ini, Paynym Anda harus "*mengikuti*" Paynym kolaborator Anda, dan sebaliknya. Untuk mengetahui cara melakukannya, Anda dapat mengikuti bagian awal dari tutorial ini:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## Bagaimana cara melakukan transaksi Stonewall x2 di Ashigaru?



Untuk melakukan transaksi Stonewall x2, klik gambar Paynym Anda di sudut kiri atas layar, lalu buka menu `Bekerja Sama`. Orang yang ikut serta dalam transaksi dengan Anda juga harus melakukan hal yang sama, kecuali jika Anda menukarkan kode QR secara langsung.



![Image](assets/fr/06.webp)



Anda memiliki dua pilihan: pilih `Memulai` jika Anda adalah pengirim pembayaran, atau `Berpartisipasi` jika Anda adalah orang yang berkolaborasi dalam transaksi tetapi bukan pembayar maupun penerima sebenarnya.



![Image](assets/fr/07.webp)



Jika Anda berperan sebagai kolaborator, prosedurnya sangat sederhana. Untuk kolaborasi jarak jauh melalui jaringan Soroban, klik `Berpartisipasi`, pilih akun yang ingin Anda gunakan, lalu tekan `DENGARKAN PERMINTAAN KOLABORASI` untuk menunggu permintaan yang dikirim oleh pembayar.



![Image](assets/fr/08.webp)



Di sisi lain, untuk kolaborasi langsung melalui pemindaian kode QR, buka halaman beranda wallet Anda, tekan ikon kode QR di bagian atas layar, lalu pindai kode QR yang disediakan oleh pembayar yang memulai transaksi.



![Image](assets/fr/09.webp)



Jika Anda berperan sebagai pembayar, yaitu pihak yang memulai transaksi, buka menu `Bekerja Sama`, lalu pilih `Memulai`.



![Image](assets/fr/10.webp)



Untuk jenis transaksi, karena kita ingin melakukan Stonewall x2, pilih opsi ini.



![Image](assets/fr/11.webp)



Anda kemudian dapat memilih antara kolaborasi online (*Cahoots* melalui *Soroban*) atau kolaborasi tatap muka, dengan pertukaran kode QR.



![Image](assets/fr/12.webp)



### Cahoots online



Jika Anda telah memilih opsi `Online`, pilih kolaborator Anda dari Paynyms yang Anda ikuti.



![Image](assets/fr/13.webp)



Klik `Siapkan transaksi`, lalu pilih akun yang ingin Anda gunakan untuk melakukan pengeluaran.



![Image](assets/fr/14.webp)



Pada halaman berikutnya, masukkan detail transaksi: alamat penerima pembayaran, jumlah yang akan dikirim, dan tarif biaya. Kemudian klik `Tinjau pengaturan transaksi`.



![Image](assets/fr/15.webp)



Periksa informasi dengan seksama, pastikan kolaborator Anda mendengarkan permintaan *Cahoots*, lalu klik tombol hijau `MULAI TRANSAKSI` untuk memulai pertukaran PSBT melalui Soroban.



![Image](assets/fr/16.webp)



Tunggu hingga kedua peserta menandatangani transaksi, lalu siarkan di jaringan Bitcoin.



![Image](assets/fr/17.webp)



### Diskusi tatap muka



Jika Anda ingin melakukan penukaran secara langsung, pilih jenis transaksi `STONEWALL X2`, lalu pilih opsi `Di Tempat / Manual`.



![Image](assets/fr/18.webp)



Klik `Siapkan transaksi`, lalu pilih akun yang ingin Anda gunakan untuk melakukan pengeluaran.



![Image](assets/fr/19.webp)



Pada halaman berikutnya, masukkan detail transaksi: alamat penerima pembayaran, jumlah yang akan dikirim, dan tarif biaya. Kemudian klik `Tinjau pengaturan transaksi`.



![Image](assets/fr/20.webp)



Periksa detailnya, lalu tekan tombol hijau `MULAI TRANSAKSI` untuk mulai menukarkan PSBT melalui pemindaian kode QR.



![Image](assets/fr/21.webp)



Pertukaran dilakukan dengan cara bergantian memindai dengan kolaborator: klik `TAMPILKAN KODE QR` untuk menampilkan kode QR Anda kepada kolaborator Anda, yang akan memindainya. Dia kemudian akan mengklik `TAMPILKAN KODE QR` untuk menampilkan kode QR miliknya, dan Anda akan memindainya dengan `LAKUKAN PEMINDAH QR`. Ulangi proses ini sampai kelima langkah pertukaran selesai.



![Image](assets/fr/22.webp)



Setelah semua pertukaran selesai, periksa detail transaksi, lalu lepaskan dengan menyeret panah hijau di bagian bawah layar.



![Image](assets/fr/23.webp)



[The transaction has been published](https://mempool.space/testnet4/tx/9082f3d989728aacd290535a1ac374ab8c04a241a1d798b378db626dabea7a24). Strukturnya adalah sebagai berikut:



![Image](assets/fr/24.webp)



*Kredit: [mempool.space](https://mempool.space/)*



Kita dapat mengamati dua input dari portofolio saya, masing-masing `91.869 sats` dan `64.823 sats`, sedangkan dua input lainnya berasal dari wallet kolaborator saya. Di sisi output, satu UTXO sebesar `100.000 sats` dikirim ke penerima pembayaran yang sebenarnya, dan dua UTXO sebesar `100.000 sats` dan `159.578 sats` kembali ke portofolio kolaborator saya. Baginya, operasi ini netral, karena dia mendapatkan kembali seluruh dana yang telah diinvestasikannya sebagai input (tidak termasuk biaya mining yang dikontribusikannya). Akhirnya, saya menerima pertukaran UTXO sebesar `56.270 sats`, sesuai dengan selisih antara total input saya dan pembayaran `100.000 sats` yang dikirim ke penerima.



Tentunya, saya dapat menggambarkan struktur ini karena saya sendiri yang membuat transaksinya. Tetapi bagi pengamat luar, umumnya tidak mungkin untuk menentukan UTXO mana yang menjadi milik peserta mana, baik dalam hal input maupun output.



Untuk memperdalam pengetahuan Anda tentang manajemen privasi onchain di Bitcoin, saya sarankan Anda mengikuti pelatihan BTC 204 saya di Plan ₿ Academy:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c