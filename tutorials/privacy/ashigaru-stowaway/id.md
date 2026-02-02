---
name: Ashigaru - Stowaway
description: Bagaimana cara melakukan transaksi Payjoin di Ashigaru?
---
![cover](assets/cover.webp)



> *Paksa mata-mata blockchain untuk memikirkan kembali segala sesuatu yang mereka pikir mereka ketahui*

Payjoin adalah struktur transaksi Bitcoin yang dirancang untuk meningkatkan kerahasiaan pengguna dengan melibatkan kolaborasi langsung dengan penerima pembayaran. Beberapa implementasi tersedia untuk mempermudah penerapannya sekaligus mengotomatiskan prosesnya. Yang paling dikenal di antaranya adalah Stowaway, yang awalnya dikembangkan oleh tim Samurai Wallet dan kini telah diintegrasikan ke dalam fork Ashigaru.


## Bagaimana cara kerja Stowaway?



Seperti yang telah disebutkan sebelumnya, Ashigaru mengintegrasikan alat PayJoin bernama `Stowaway`. Alat ini tersedia di aplikasi Ashigaru di Android. Agar PayJoin dapat dilakukan, penerima, yang juga berperan sebagai kolaborator, harus menggunakan perangkat lunak yang kompatibel dengan Stowaway, yaitu untuk saat ini hanya Ashigaru.

Stowaway didasarkan pada kategori transaksi yang oleh Samourai Wallet disebut sebagai "Cahoots". Cahoots adalah transaksi kolaboratif antara beberapa pengguna yang melibatkan pertukaran informasi di luar blockchain Bitcoin. Saat ini, Ashigaru menawarkan dua alat Cahoots: Stowaway (PayJoin) dan StonewallX2.


https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b

Transaksi Cahoots membutuhkan pertukaran sebagian transaksi yang telah ditandatangani antar pengguna. Proses ini bisa terasa lama dan membosankan, terutama jika dilakukan dari jarak jauh. Namun, hal ini masih bisa dilakukan secara manual jika para kolaborator berada di lokasi yang sama. Secara konkret, ini melibatkan pemindaian lima kode QR secara berurutan, yang dipertukarkan antara dua peserta.

Untuk transaksi jarak jauh, metode ini menjadi terlalu rumit. Untuk mengatasinya, Samourai mengembangkan protokol komunikasi terenkripsi berbasis Tor yang disebut "Soroban". Berkat Soroban, pertukaran yang dibutuhkan untuk PayJoin dilakukan secara otomatis dan berlangsung di latar belakang.

Komunikasi terenkripsi ini membutuhkan koneksi dan autentikasi antara peserta Cahoot. Inilah alasan Soroban bergantung pada Paynyms pengguna. Jika kamu belum terbiasa dengan cara kerja Paynyms, lihat tutorial khusus ini untuk mempelajari lebih lanjut:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

Singkatnya, Paynym adalah sebuah pengenal unik yang diasosiasikan dengan wallet kamu, yang memungkinkan kamu untuk mengaktifkan berbagai fungsi, termasuk bursa terenkripsi. Bentuknya berupa pengenal yang disertai dengan ilustrasi. Ini, sebagai contoh, adalah yang aku gunakan pada Testnet:



![Image](assets/fr/01.webp)



**Sebagai rangkuman:**





- payjoin" = Struktur transaksi kolaboratif tertentu;





- `Penumpang gelap` = Implementasi Payjoin yang tersedia di Ashigaru;





- `Kongkalikong` = Nama yang diberikan oleh Samourai untuk semua jenis transaksi kolaboratif mereka, khususnya `Penumpang Gelap` Payjoin, yang diambil alih hari ini di Ashigaru;





- soroban = Protokol komunikasi terenkripsi yang dibuat di Tor yang memungkinkan kolaborasi dengan pengguna lain dalam transaksi `Cahoots`;





- paynym" = Pengenal wallet unik yang digunakan untuk menjalin komunikasi dengan pengguna lain di "Soroban", untuk melakukan transaksi "Chahoots".



Untuk melihat lebih dalam tentang cara kerja Payjoins dan kegunaannya dalam privasi onchain, aku merekomendasikan tutorial lain ini:



https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

## Bagaimana cara membuat koneksi antara Paynyms?



Untuk memulai, tentu saja kamu perlu menginstal Ashigaru dan membuat file :



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Untuk melakukan transaksi Cahoots jarak jauh, termasuk PayJoin (*Stowaway*) melalui Ashigaru, kamu harus terlebih dahulu "mengikuti" pengguna yang ingin kamu ajak berkolaborasi, dengan menggunakan Paynym mereka. Dalam kasus Penumpang Gelap, ini berarti mengikuti orang yang ingin kamu kirimi bitcoin. Jika kamu belum mengetahui cara mengikuti Paynym lain, kamu akan menemukan prosedur detailnya di tutorial ini:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## Bagaimana cara membuat Payjoin di Ashigaru?



Untuk melakukan transaksi Penumpang Gelap, klik gambar Paynym kamu di pojok kiri atas layar, lalu buka menu `Kolaborasi`. Orang yang ikut serta dalam transaksi dengan kamu juga harus melakukan hal yang sama, kecuali jika kamu menukarkan kode QR secara langsung.


![Image](assets/fr/02.webp)



Kamu memiliki dua pilihan: pilih `Memulai` jika kamu adalah pengirim pembayaran, atau `Berpartisipasi` jika kamu adalah penerima pembayaran dari payjoin ini.



![Image](assets/fr/03.webp)



Jika kamu adalah penerima, prosedurnya sangat sederhana. Untuk kolaborasi jarak jauh melalui jaringan Soroban, klik `Berpartisipasi`, pilih akun yang ingin kamu gunakan, lalu tekan `DENGARKAN PERMINTAAN CAHOOTS` untuk menunggu permintaan yang dikirim oleh pembayar.


![Image](assets/fr/04.webp)



Di sisi lain, untuk kolaborasi langsung melalui pemindaian kode QR, buka halaman beranda wallet kamu, tekan ikon kode QR di bagian atas layar, lalu pindai kode QR yang disediakan oleh pembayar yang memulai transaksi.


![Image](assets/fr/05.webp)



Jika kamu berperan sebagai pembayar, yaitu pihak yang memulai transaksi, buka menu `Bekerja Sama`, lalu pilih `Memulai`.



![Image](assets/fr/06.webp)



Untuk jenis transaksi, karena kami ingin membuat Payjoin Stowaway, pilih opsi ini.



![Image](assets/fr/07.webp)



Kemudian kamu dapat memilih antara kolaborasi online (*Cahoots* melalui *Soroban*) atau kolaborasi tatap muka, dengan pertukaran kode QR.



![Image](assets/fr/08.webp)



### Cahoots online



Jika kamu telah memilih opsi `Online`, pilih penerima dari Paynyms yang kamu ikuti.



![Image](assets/fr/09.webp)



Klik `Siapkan transaksi`, lalu pilih akun yang ingin kamu gunakan untuk melakukan pengeluaran.



![Image](assets/fr/10.webp)



Pada halaman berikutnya, masukkan detail transaksi: jumlah yang akan dikirim ke penerima dan tarif biaya. Tidak perlu memasukkan alamat penerima, karena penerima akan mengirimkannya sendiri selama pertukaran PSBT.


Kemudian klik `Tinjau pengaturan transaksi`.



![Image](assets/fr/11.webp)



Periksa informasi dengan seksama, pastikan kolaborator kamu mendengarkan permintaan *Cahoots*, lalu klik tombol hijau `MULAI TRANSAKSI` untuk memulai pertukaran PSBT melalui Soroban.



![Image](assets/fr/12.webp)



Tunggu hingga kedua peserta menandatangani transaksi, lalu siarkan di jaringan Bitcoin.



![Image](assets/fr/13.webp)



### Diskusi tatap muka



Jika kamu ingin melakukan penukaran secara langsung, pilih jenis transaksi `STONEWALL X2`, lalu pilih opsi `Di Tempat / Manual`.



![Image](assets/fr/14.webp)



Klik `Siapkan transaksi`, lalu pilih akun yang ingin kamu gunakan untuk melakukan pengeluaran.



![Image](assets/fr/15.webp)



Pada halaman berikutnya, masukkan detail transaksi: jumlah yang akan dikirim ke penerima dan tarif biaya. Tidak perlu memasukkan alamat penerima, karena penerima akan mengirimkannya sendiri selama pertukaran PSBT.


Kemudian klik `Tinjau pengaturan transaksi`.



![Image](assets/fr/16.webp)



Periksa detailnya, lalu tekan tombol hijau `MULAI TRANSAKSI` untuk mulai menukarkan PSBT melalui pemindaian kode QR.



![Image](assets/fr/17.webp)



Pertukaran dilakukan dengan cara bergantian memindai dengan kolaborator: klik 'TAMPILKAN KODE QR' untuk menampilkan kode QR kamu kepada kolaborator kamu, yang akan memindainya. Dia kemudian akan mengklik 'TAMPILKAN KODE QR' untuk menampilkan kode QR miliknya, dan kamu akan memindainya dengan 'LAKUKAN PEMINDAH QR'. Ulangi proses ini sampai kelima langkah pertukaran selesai.



![Image](assets/fr/18.webp)



Setelah semua pertukaran selesai, periksa detail transaksi, lalu lepaskan dengan menyeret panah hijau di bagian bawah layar.



![Image](assets/fr/19.webp)



[The transaction has been published](https://mempool.space/testnet4/tx/82efd3700bba87b0f172e9cc045e441b38622c95a60df9f39a21f63eb4590a96). Strukturnya adalah sebagai berikut:



![Image](assets/fr/20.webp)



*Kredit: [mempool.space](https://mempool.space/)*



Jika kita menganalisis transaksi ini, kita melihat UTXO aku sebesar `164.211 sats` di sisi input, serta UTXO sebesar `190.002 sats` milik penerima pembayaran yang sebenarnya. Di sisi output, aku menerima pertukaran UTXO sebesar `63.995 sats`, sedangkan penerima menerima UTXO sebesar `290.002 sats`. Dengan membandingkan input dan output, kita dapat melihat bahwa penerima memang mendapatkan `100.000 sats`, yang sesuai dengan jumlah pembayaran aku yang sebenarnya, dan bahwa aku kehilangan `100.000 sats`, yang telah aku tambahkan dengan biaya mining.



Tentunya, aku dapat menggambarkan struktur ini karena aku sendiri yang membuat transaksinya. Tetapi bagi pengamat luar, umumnya tidak mungkin untuk menentukan UTXO mana yang menjadi milik peserta mana, baik dalam hal input maupun output.

Untuk memperdalam pengetahuan kamu tentang manajemen privasi onchain di Bitcoin, aku sarankan kamu mengikuti pelatihan BTC 204 aku di Plan ₿ Academy:


https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c
