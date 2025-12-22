---
name: Ashigaru - Stonewall x2
description: Memahami dan menggunakan transaksi Stonewall x2 di Ashigaru
---
![cover stonewall x2](assets/cover.webp)



> *Jadikan setiap pengeluaran sebagai koin bersama

## Apa yang dimaksud dengan transaksi Stonewall x2?



Stonewall x2 adalah bentuk khusus dari transaksi Bitcoin yang dirancang untuk meningkatkan kerahasiaan pengguna saat melakukan pembelanjaan, dengan cara berkolaborasi dengan pihak ketiga yang tidak terlibat langsung dalam pembelanjaan. Metode ini mensimulasikan mini-coinjoin antara dua partisipan ketika melakukan pembayaran ke pihak ketiga. Transaksi Stonewall x2 tersedia di aplikasi Ashigaru, sebuah fork dari Samourai Wallet, tim di balik pembuatan jenis transaksi ini.

https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Cara kerjanya relatif sederhana: kamu menggunakan UTXO yang kamu miliki untuk melakukan pembayaran, lalu meminta bantuan pihak ketiga yang juga berkontribusi dengan UTXO mereka sendiri. Transaksi ini berakhir dengan empat keluaran: dua di antaranya memiliki jumlah yang sama, satu ditujukan ke alamat penerima pembayaran, dan satunya lagi ke alamat milik kolaborator. UTXO ketiga dikembalikan ke alamat lain milik kolaborator, sehingga ia bisa mendapatkan kembali jumlah awalnya, yang secara bersih bersifat netral baginya, modulo biaya mining, dan UTXO terakhir dikembalikan ke alamat milik aku, yang merupakan kembalian dari pembayaran.



Dengan demikian, ada tiga peran yang berbeda dalam transaksi Stonewall x2:




- Penerbit, yang melakukan pembayaran aktual;
- Kolaborator, yang menyediakan bitcoin untuk meningkatkan anonimitas transaksi, sambil memulihkan dananya secara penuh pada akhirnya (tindakan netral baginya, modulo biaya mining);
- Penerima, yang mungkin tidak menyadari sifat spesifik dari transaksi dan hanya mengharapkan pembayaran dari pengirim.



Mari kita ambil sebuah contoh. Alice sedang berada di toko roti untuk membeli roti baguette seharga `4.000 sats`. Ia ingin membayar dengan bitcoin, namun tetap ingin menjaga kerahasiaan pembayarannya. Jadi dia memanggil temannya Bob, yang akan membantunya dalam hal ini.



![image](assets/fr/01.webp)



Dengan menganalisis transaksi ini, kita dapat melihat bahwa pembuat roti sebenarnya menerima `4.000 sats` sebagai pembayaran untuk roti baguette. Alice menggunakan `10.000 sats` sebagai input dan menerima `6.000 sats` sebagai output, sehingga menghasilkan saldo bersih `-4.000 sats`, yang sesuai dengan harga roti baguette. Sedangkan untuk Bob, Bob memasok `15.000 sats` dalam bentuk input dan menerima dua output: satu sebesar `4.000 sats` dan yang lainnya sebesar `11.000 sats`, sehingga menghasilkan saldo `0`.



Dalam contoh ini, aku sengaja mengabaikan biaya mining agar lebih mudah dipahami. Pada kenyataannya, biaya transaksi dibagi rata antara penerbit pembayaran dan kolaborator.



## Apa perbedaan antara Stonewall dan Stonewall x2?



Transaksi Stonewall x2 bekerja dengan cara yang sama persis dengan transaksi Stonewall, dengan satu perbedaan utama: yang pertama bersifat kolaboratif, sedangkan yang kedua tidak. Seperti yang sudah kita bahas, transaksi Stonewall x2 melibatkan partisipasi pihak ketiga yang berada di luar pembayaran, dan yang menyediakan bitcoin miliknya untuk meningkatkan kerahasiaan transaksi. Dalam transaksi Stonewall klasik, peran kolaborator ini diambil langsung oleh pengirim.

Mari kita kembali ke contoh Alice di toko roti. Jika dia tidak bisa menemukan seseorang seperti Bob untuk menemaninya berbelanja, dia tetap bisa melakukan Stonewall sendirian. Dalam skenario ini, dua UTXO pada sisi input sepenuhnya miliknya, dan dia akan menerima 3 UTXO pada sisi output.



![image](assets/fr/02.webp)




Dari sudut pandang orang luar, transaksi akan tetap sama.



![image](assets/fr/05.webp)



Oleh karena itu, logikanya adalah sebagai berikut ketika kamu ingin menggunakan alat belanja Ashigaru:




- Jika pedagang tidak mendukung Payjoin Stowaway, kamu dapat melakukan transaksi kolaboratif dengan orang lain di luar pembayaran berkat Stonewall x2 ;
- Jika kamu tidak dapat menemukan siapa pun untuk melakukan transaksi Stonewall x2, kamu dapat melakukan transaksi Stonewall saja, yang akan meniru perilaku transaksi Stonewall x2.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-033daa45-d42c-40e1-9511-cea89751c3d4

## Apa gunanya transaksi Stonewall x2?



Struktur Stonewall x2 menambahkan tingkat entropi yang signifikan ke dalam transaksi, sehingga mengacaukan analisis rantai. Dilihat dari luar, transaksi semacam ini bisa ditafsirkan sebagai CoinJoin kecil antara dua orang, padahal pada kenyataannya ini adalah sebuah pembayaran. Karena itu, metode ini menciptakan ketidakpastian dalam analisis rantai, atau bahkan bisa mengarahkan pada kesimpulan yang keliru.

Mari kita ambil contoh Alice, Bob, dan Boulanger. Transaksi di blockchain akan terlihat seperti ini:



![image](assets/fr/03.webp)



Seorang pengamat luar yang mengandalkan heuristik analisis rantai umum mungkin akan salah menyimpulkan bahwa "*Alice dan Bob telah membuat coinjoin kecil, dengan masing-masing satu UTXO masuk dan dua UTXO keluar*".



![image](assets/fr/04.webp)



Interpretasi ini salah karena, seperti yang kamu ketahui, UTXO dikirim ke Boulanger, Alice hanya memiliki satu output pertukaran, dan Bob memiliki dua.



![image](assets/fr/01.webp)



Bahkan jika pengamat luar berhasil mengidentifikasi pola dari transaksi Stonewall x2, dia tetap tidak akan memiliki semua informasi yang dibutuhkan. Dia tidak bisa menentukan mana dari dua UTXO dengan jumlah yang sama yang merupakan pembayaran. Dia juga tidak bisa memastikan apakah Alice atau Bob yang sebenarnya melakukan pembayaran. Terakhir, dia tidak dapat mengetahui apakah dua UTXO input berasal dari dua orang yang berbeda, atau justru milik satu orang yang sama yang digabungkan. Poin terakhir ini muncul karena transaksi Stonewall klasik, yang sudah dibahas sebelumnya, mengikuti pola yang persis sama dengan transaksi Stonewall x2. Dilihat dari luar dan tanpa informasi kontekstual tambahan, tidak mungkin membedakan transaksi Stonewall dengan transaksi Stonewall x2. Yang pertama bukan transaksi kolaboratif, sedangkan yang kedua adalah transaksi kolaboratif. Kondisi ini semakin menambah tingkat ketidakpastian dalam analisis biaya.

![image](assets/fr/05.webp)




## Bagaimana cara membuat koneksi antara Paynyms?



Seperti halnya transaksi kolaboratif lainnya di Ashigaru (Cahoots), Stonewall x2 melibatkan pertukaran transaksi yang ditandatangani sebagian antara pengirim dan kolaborator. Pertukaran ini bisa dilakukan secara manual jika kamu hadir secara fisik bersama kolaboratormu, atau secara otomatis menggunakan protokol komunikasi Soroban.

Jika kamu memilih opsi kedua, kamu perlu membuat koneksi antar PayNym sebelum bisa melakukan Stonewall x2. Untuk melakukannya, PayNym kamu harus "mengikuti" PayNym milik kolaboratormu, dan sebaliknya. Untuk mengetahui caranya, kamu bisa mengikuti bagian awal dari tutorial ini:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## Bagaimana cara melakukan transaksi Stonewall x2 di Ashigaru?



Untuk melakukan transaksi Stonewall x2, klik gambar Paynym kamu di sudut kiri atas layar, lalu buka menu `Collaborate`. Orang yang ikut serta dalam transaksi dengan kamu juga harus melakukan hal yang sama, kecuali jika kamu menukarkan kode QR secara langsung.



![Image](assets/fr/06.webp)



Kamu memiliki dua pilihan: pilih `Memulai` jika kamu adalah pengirim pembayaran, atau `Berpartisipasi` jika kamu adalah orang yang berkolaborasi dalam transaksi tetapi bukan pembayar maupun penerima sebenarnya.



![Image](assets/fr/07.webp)



Jika kamu berperan sebagai kolaborator, prosedurnya sangat sederhana. Untuk kolaborasi jarak jauh melalui jaringan Soroban, klik `Berpartisipasi`, pilih akun yang ingin kamu gunakan, lalu tekan `DENGARKAN PERMINTAAN KOLABORASI` untuk menunggu permintaan yang dikirim oleh pembayar.



![Image](assets/fr/08.webp)



Di sisi lain, untuk kolaborasi langsung melalui pemindaian kode QR, buka halaman beranda wallet kamu, tekan ikon kode QR di bagian atas layar, lalu pindai kode QR yang disediakan oleh pembayar yang memulai transaksi.



![Image](assets/fr/09.webp)



Jika kamu berperan sebagai pembayar, yaitu pihak yang memulai transaksi, buka menu `Collaborate`, lalu pilih `Memulai`.



![Image](assets/fr/10.webp)



Untuk jenis transaksi, karena kita ingin melakukan Stonewall x2, pilih opsi ini.



![Image](assets/fr/11.webp)



Kemudian kamu dapat memilih antara kolaborasi online (*Cahoots* melalui *Soroban*) atau kolaborasi tatap muka, dengan pertukaran kode QR.



![Image](assets/fr/12.webp)



### Cahoots online



Jika kamu telah memilih opsi `Online`, pilih kolaborator Anda dari Paynyms yang kamu ikuti.



![Image](assets/fr/13.webp)



Klik `Siapkan transaksi`, lalu pilih akun yang ingin kamu gunakan untuk melakukan pengeluaran.



![Image](assets/fr/14.webp)



Pada halaman berikutnya, masukkan detail transaksi: alamat penerima pembayaran, jumlah yang akan dikirim, dan tarif biaya. Kemudian klik `Tinjau pengaturan transaksi`.



![Image](assets/fr/15.webp)



Periksa informasi dengan seksama, pastikan kolaborator kamu mendengarkan permintaan *Cahoots*, lalu klik tombol hijau `MULAI TRANSAKSI` untuk memulai pertukaran PSBT melalui Soroban.



![Image](assets/fr/16.webp)



Tunggu hingga kedua peserta menandatangani transaksi, lalu siarkan di jaringan Bitcoin.



![Image](assets/fr/17.webp)



### Diskusi tatap muka



Jika kamu ingin melakukan penukaran secara langsung, pilih jenis transaksi `STONEWALL X2`, lalu pilih opsi `Di Tempat / Manual`.



![Image](assets/fr/18.webp)



Klik `Siapkan transaksi`, lalu pilih akun yang ingin kamu gunakan untuk melakukan pengeluaran.



![Image](assets/fr/19.webp)



Pada halaman berikutnya, masukkan detail transaksi: alamat penerima pembayaran, jumlah yang akan dikirim, dan tarif biaya. Kemudian klik `Tinjau pengaturan transaksi`.



![Image](assets/fr/20.webp)



Periksa detailnya, lalu tekan tombol hijau `MULAI TRANSAKSI` untuk mulai menukarkan PSBT melalui pemindaian kode QR.



![Image](assets/fr/21.webp)



Pertukaran dilakukan dengan cara bergantian memindai dengan kolaborator: klik `TAMPILKAN KODE QR` untuk menampilkan kode QR kamu kepada kolaborator kamu, yang akan memindainya. Dia kemudian akan mengklik `TAMPILKAN KODE QR` untuk menampilkan kode QR miliknya, dan kamu akan memindainya dengan `LAKUKAN PEMINDAH QR`. Ulangi proses ini sampai kelima langkah pertukaran selesai.



![Image](assets/fr/22.webp)



Setelah semua pertukaran selesai, periksa detail transaksi, lalu lepaskan dengan menyeret panah hijau di bagian bawah layar.



![Image](assets/fr/23.webp)



[The transaction has been published](https://mempool.space/testnet4/tx/9082f3d989728aacd290535a1ac374ab8c04a241a1d798b378db626dabea7a24). Strukturnya adalah sebagai berikut:



![Image](assets/fr/24.webp)



*Kredit: [mempool.space](https://mempool.space/)*



Kita bisa mengamati dua input dari portofolio aku, masing-masing `91.869 sats` dan `64.823 sats`, sementara dua input lainnya berasal dari wallet kolaborator aku. Di sisi output, satu UTXO sebesar `100.000 sats` dikirim ke penerima pembayaran yang sebenarnya, dan dua UTXO sebesar `100.000 sats` serta `159.578 sats` kembali ke portofolio kolaborator aku. Bagi dia, operasi ini bersifat netral, karena dia mendapatkan kembali seluruh dana yang dia masukkan sebagai input, tidak termasuk biaya mining yang dia kontribusikan. Terakhir, aku menerima kembalian UTXO sebesar `56.270 sats`, yang sesuai dengan selisih antara total input aku dan pembayaran `100.000 sats` yang dikirim ke penerima.

Tentu saja, aku bisa menjelaskan struktur ini karena aku sendiri yang membuat transaksinya. Namun bagi pengamat luar, umumnya tidak mungkin untuk menentukan UTXO mana yang dimiliki oleh masing-masing partisipan, baik di sisi input maupun output.

Untuk memperdalam pemahaman kamu tentang manajemen privasi onchain di Bitcoin, aku menyarankan kamu untuk mengikuti pelatihan BTC 204 aku di Plan ₿ Academy:


https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c
