---
name: Banteng Bitcoin Wallet
description: Ketahui cara menggunakan Wallet Bull Bitcoin
---

![cover](assets/cover.webp)



Panduan ini memandu Anda melalui instalasi, konfigurasi, dan penggunaan Bull Bitcoin Mobile. Anda akan mempelajari cara menerima dan mengirim dana pada tiga jaringan: onchain, Liquid dan Lightning, dan cara mentransfer Bitcoin Anda dari satu jaringan ke jaringan lainnya. Lampiran menyediakan sumber daya dan kontak, informasi latar belakang, dan penjelasan singkat tentang konsep teknis.



## Pendahuluan



**Bull Bitcoin Mobile**, yang dikembangkan oleh **[Bull Bitcoin](https://www.bullbitcoin.com/)** ([buat akun](https://app.bullbitcoin.com/registration/orangepeel)), merupakan **self-custodial** Bitcoin Wallet, yang berarti Anda memiliki kontrol penuh atas kunci pribadi Anda dan juga dana Anda, tanpa bergantung pada pihak ketiga. Bersifat open-source dan berakar pada filosofi Cypherpunk, Wallet ini menggabungkan kesederhanaan, kerahasiaan, dan fitur-fitur canggih seperti pertukaran lintas jaringan dan dukungan PayJoin. Ini memungkinkan Anda untuk mengelola bitcoin Anda di tiga jaringan: **Bitcoin onchain**, **Liquid** dan **Lightning**, masing-masing disesuaikan untuk penggunaan tertentu.



### Konteks pengembangan



Wallet menjawab tantangan besar: Biaya jaringan Bitcoin tidak cocok untuk pembayaran dalam jumlah kecil, atau untuk membuka saluran Lightning kecil yang dihosting sendiri. Wallet Bull Bitcoin Mobile menawarkan solusi kustodian mandiri dengan tetap mengandalkan 3 jaringan utama Bitcoin:





- Jaringan Bitcoin (onchain)**: Ideal untuk penyimpanan UTXO jangka menengah hingga jangka panjang dan transaksi bernilai besar, di mana biaya dapat diabaikan secara proporsional.
- Liquid Network**: Dirancang untuk transaksi yang cepat (~2 menit), lebih rahasia (jumlah tersembunyi), dan berbiaya rendah, cocok untuk mengakumulasi jumlah kecil atau melindungi privasi Anda.
- Jaringan Lightning**: Dioptimalkan untuk pembayaran instan dan berbiaya rendah, cocok untuk transaksi harian bernilai kecil hingga menengah.



Dengan Bull Bitcoin Mobile, misalnya, Anda bisa mengakumulasi sejumlah kecil dalam portofolio **Liquid** atau **Lightning** dan kemudian, setelah Anda mencapai jumlah yang signifikan, Anda bisa:





- Transfer ke jaringan onchain untuk penyimpanan jangka menengah atau jangka panjang yang aman, memiliki kerahasiaan yang lebih baik dengan Liquid dan / atau Lightning di bagian hulu, dan dengan biaya onchain untuk satu transaksi



### Evolusi berkelanjutan



Wallet terus berkembang, jadi jangan kaget jika Anda menemukan perbedaan antara tutorial ini dan aplikasi Anda yang terbaru.




- Misalnya, pada 19/07/2025, tombol **"Beli / Jual / Bayar "** terlihat tetapi berwarna abu-abu di aplikasi, karena opsi ini, tersedia di Exchange [bullbitcoin.com] (https://app.bullbitcoin.com/registration/orangepeel), akan segera diintegrasikan untuk pengalaman yang terpadu. Penggunaannya akan tetap sepenuhnya opsional. Banyak perkembangan lain yang sedang berlangsung atau direncanakan: manajemen multi-Wallet, passphrase, kompatibilitas dengan dompet perangkat keras ...
- Di [BullBitcoin GitHub] (https://github.com/orgs/SatoshiPortal/projects/49), Anda dapat melihat topik-topik terkini dan perkembangan yang akan datang. Karena proyek ini 100% open-source dan "dibangun untuk umum", Anda juga dapat mengirimkan saran dan bug yang Anda temui kepada kami.




## 1. Prasyarat



Sebelum Anda mulai menggunakan **Bull Bitcoin Mobile**, pastikan Anda memiliki item berikut ini:





- Smartphone yang Kompatibel**: Perangkat **iOS** (iPhone atau iPad) atau **Android**
- Koneksi internet
- Media cadangan yang aman**: Tuliskan **frase pemulihan** (12 kata) di atas kertas atau logam dan simpan di tempat yang aman.
- Pengetahuan dasar**: Pemahaman minimum mengenai konsep Bitcoin (alamat, transaksi, biaya) sangat berguna, meskipun tutorial ini menjelaskan setiap langkah untuk pemula.



## 2. Instalasi





- Unduh aplikasi** :
 - [Google Play Store](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&pcampaignid=web_share)** Unduh dari toko aplikasi untuk perangkat Android
 - [GitHub](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) Unduh APK untuk perangkat Android secara langsung**
 - [iOS](https://testflight.apple.com/join/FJbE4JPN)** Unduh melalui TestFlight untuk perangkat Apple
 - Periksa nama pengembang (Bull Bitcoin) untuk menghindari aplikasi palsu.
 - Pastikan versi yang diunduh sesuai dengan versi stabil terbaru yang ditunjukkan di GitHub.
 - Bull Bitcoin Mobile adalah **sumber terbuka**. Untuk melihat kodenya: [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49)





- Instal aplikasi




## 3. Konfigurasi awal



### 3.1 Luncurkan aplikasi :



Aplikasi ini menggunakan frasa pemulihan 12 kata yang unik untuk kedua portofolio:




 - mengamankan Bitcoin 'Wallet**: Untuk transaksi di jaringan Bitcoin (onchain)
 - pembayaran instan Wallet**: Untuk transaksi instan pada jaringan Liquid dan Lightning



Pada saat membuka, Anda diminta untuk mengimpor frasa pemulihan yang sudah ada, atau membuat Wallet yang baru:



![image](assets/fr/02.webp)



### 3.2 Frasa pemulihan :



Jika Anda ingin menggunakan kembali Wallet yang sudah ada, klik "**Pulihkan Wallet**" dan isi 12 kata frasa pemulihan Anda.



Jika tidak, klik "**Buat Wallet Baru**" :




- Tuliskan frasa pemulihan Anda dengan sangat hati-hati. Tuliskan di atas kertas atau logam dan simpan di tempat yang aman (brankas, lokasi offline). Frasa ini merupakan satu-satunya cara Anda untuk mengakses bitcoin jika perangkat Anda hilang atau aplikasi dihapus.
- Penting juga untuk diperhatikan bahwa siapa pun yang memiliki frasa ini dapat mencuri semua bitcoin Anda. Jangan pernah menyimpannya secara digital:
 - Tidak ada tangkapan layar
 - Tidak ada cadangan awan, email, atau pesan
 - Tidak ada salin/tempel (risiko menyimpan ke clipboard)



**! Poin ini sangat penting**. Untuk bantuan lebih lanjut :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 3.3 Mengamankan akses :





- Masuk ke pengaturan lalu klik **Kode PIN**.
- Siapkan **kode PIN** yang kuat untuk melindungi akses ke aplikasi.
- Langkah ini bersifat opsional, tetapi sangat disarankan untuk mencegah siapa pun yang memiliki akses ke ponsel Anda mendapatkan akses ke Wallet Anda.



![image](assets/fr/03.webp)



### 3.4 Sambungan ke node pribadi (opsional):



BullBitcoin Wallet terhubung ke server Electrum secara default: yang pertama dikelola oleh Bull Bitcoin dan server sekunder dari Blockstream, yang keduanya dianggap tidak menyimpan log, sehingga mengurangi risiko pelacakan.



Untuk kerahasiaan yang lebih baik, Anda dapat menghubungkan aplikasi ke node Bitcoin Anda sendiri melalui server Electrum (instruksi tersedia di [BullBitcoin's GitHub] (https://github.com/orgs/SatoshiPortal/projects/49)).




## 4. Menerima dana



Menerima dana dengan **Bull Bitcoin Mobile** sederhana dan disesuaikan dengan kebutuhan Anda, baik Anda menggunakan :




  - jaringan **Bitcoin (onchain)** untuk konservasi jangka panjang,
  - jaringan **Liquid** untuk jaringan Confidential Transactions yang lebih cepat dan lebih banyak,
  - jaringan **Lightning** untuk pembayaran instan dan bernilai rendah.



Aplikasi ini secara otomatis menghasilkan penerimaan Lightning atau alamat Invoice, tergantung pada jaringan yang dipilih. Berikut ini adalah cara melanjutkan untuk setiap jaringan.



### 4.1. onchain (jaringan Bitcoin)



Pada layar Beranda, Anda dapat :




- atau pilih **Amankan Bitcoin Wallet** lalu klik "**Terima "** :



![image](assets/fr/04.webp)





- atau klik "**Terima "**, lalu pilih jaringan **Bitcoin**:



![image](assets/fr/05.webp)



#### 4.1.1. Opsi "Salin atau pindai Address saja" dinonaktifkan (default)



![image](assets/fr/06.webp)





- Ini memberikan akses ke parameter lanjutan opsional. Anda dapat menentukan :
 - Jumlah tertentu dalam BTC, Sats, atau fiat.
 - Sebuah **catatan pribadi** untuk disertakan dalam salinan URI/Kode QR.
 - Aktivasi **PayJoin** (lihat Lampiran 3 untuk detailnya), yang meningkatkan kerahasiaan dengan menggabungkan entri pengirim dan penerima.





- Contoh URI yang dibuat secara otomatis**:



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=2.1e-7&message=Exemple+de+note&pj=HTTPS%3A%2F%2FPAYJO.IN%2FUJA9LJ6L4CMHY%23RK1QT3YSGFC6PMKRUXND2DSGQMLESTUNH29AY0305XAQ678742CVT5ES+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1RRH8C6Q
```





- Penggunaan**: Salin URI untuk dibagikan kepada pengirim, atau biarkan dia memindai kode QR.



#### 4.1.2. Opsi "Salin atau pindai Address saja" diaktifkan



![image](assets/fr/07.webp)





- Dengan mengaktifkan opsi **"Salin atau pindai Address saja "**, aplikasi ini menghasilkan Bitcoin Address sederhana dalam format SegWit (bech32).





- Contoh:



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```



Meskipun Anda memasukkan jumlah atau catatan, jumlah atau catatan tersebut tidak akan disertakan dalam kode QR atau dalam salinan Address





- Penggunaan**: Salin Address untuk dibagikan kepada pengirim, atau biarkan dia memindai kode QR.



#### 4.1.3. Menghasilkan Address baru





- Mengapa menggunakan Address baru untuk setiap transaksi? Hal ini **melindungi privasi Anda** dengan mencegah beberapa pembayaran ditautkan ke Address yang sama, dan membatasi kemungkinan pelacakan pada Blockchain.
 - Secara default, Bull Bitcoin secara otomatis menghasilkan Address yang tidak terpakai.**
 - Anda dapat memaksa pembuatan Address baru dengan mengeklik **"New Address"** di bagian bawah layar.
 - Semua alamat Anda ditautkan ke frasa seed Anda: berapa pun jumlah alamat yang Anda gunakan, portofolio Anda akan menampilkan satu saldo, dan secara otomatis dapat mengkonsolidasikan dana saat pengiriman dilakukan.





- Tip: Selalu gunakan Address** baru yang disediakan oleh Bull Bitcoin, kecuali jika Anda memiliki kebutuhan khusus (misalnya Address publik untuk menerima donasi).



### 4.2. Liquid



Pada layar Beranda, Anda dapat :




- atau pilih **Pembayaran Instan Wallet** lalu klik **"Terima "** kemudian **"Liquid"** :



![image](assets/fr/08.webp)





- atau klik "**Terima "**, lalu pilih jaringan **Liquid**:



![image](assets/fr/09.webp)



Setelah Anda berada di layar **"Terima "**, salin Liquid Address:





- Tidak ada jumlah atau catatan. Contoh:



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```





- Atau dengan menentukan **jumlah** (dalam BTC, Sats atau fiat) dan/atau **catatan pribadi** yang akan disertakan dalam salinan URI/Kode QR. Contoh:



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



**Gunakan**: Salin Address/URI untuk dibagikan kepada pengirim, atau biarkan dia memindai kode QR.



### 4.3. Petir



Pada layar Beranda, Anda dapat :




- atau pilih **Pembayaran instan Wallet** lalu klik "**Terima "** :



![image](assets/fr/10.webp)





- atau klik "**Terima "**, lalu pilih jaringan **Lightning**:



![image](assets/fr/11.webp)



#### 4.3.1. Pengoperasian, batasan dan manfaat





- Mekanisme**: Bull Bitcoin Wallet adalah Wallet yang memungkinkan pembayaran dilakukan dan diterima melalui Lightning. Dana yang diterima melalui Lightning disimpan di jaringan **Liquid** (dalam Pembayaran Instan Wallet) berkat pertukaran otomatis melalui **Boltz**. Hal ini memberikan Anda kemampuan untuk berinteraksi dengan Lightning tanpa harus mengelola saluran likuiditas, namun tetap berada dalam penyimpanan sendiri.





- Batasan:** Batas
 - Jumlah minimum** 100 satoshi (per 19/07/2025) saat Anda membeli generate atau Invoice.
 - Anda membayar biaya**, yang akan dipotong dari jumlah yang dikirim oleh pengirim, tidak seperti menerima dengan Wallet Lightning asli, di mana hanya pengirim yang membayar biaya transfer selain jumlah yang dikirim. Pada 19/07/2025, 47 Sats dikurangkan dari jumlah yang dikirim.





- Manfaat** :
 - Kustodian mandiri**: Dana Anda tetap berada di bawah kendali Anda, disimpan di Liquid Network.
 - Tidak ada biaya onchain yang tinggi**: Penyimpanan di Liquid menghindari setoran onchain yang mahal untuk membuka saluran Lightning Anda atau menambah likuiditas. Operasi ini dapat dilakukan nanti, ketika jumlah yang terkumpul di Liquid sesuai dengan biaya.





- Tip:** Jika pengirim memiliki Wallet Bull Bitcoin, gunakan Liquid Network secara langsung untuk menghindari biaya swap



#### 4.3.2. generate Invoice





- Masukkan **jumlah** (dalam BTC, Sats, atau fiat)





- Tambahkan **catatan pribadi** yang akan diintegrasikan ke dalam Invoice. Jika pengirim membayar Invoice, Wallet Anda juga akan menyertakannya dalam rincian transaksi.





- Masa berlaku Invoice:** Lightning Invoice berlaku selama **12 jam**. Setelah waktu tersebut, masa berlakunya akan berakhir dan tidak dapat dibayar lagi. Invoice baru harus dibuat.





- Penggunaan**: Salin Invoice untuk dibagikan kepada pengirim, atau biarkan dia memindai kode QR.




## 5. Mengirim dana



### 5.1. Prinsip dasar



Baik dari halaman beranda, atau dari dompet :



![image](assets/fr/12.webp)



untuk mengakses layar kirim:



![image](assets/fr/13.webp)



**Bull Bitcoin Mobile** memudahkan pengiriman uang dengan secara otomatis mendeteksi jaringan (Bitcoin, Liquid, atau Lightning) berdasarkan Address atau Invoice yang dimasukkan (disalin atau dipindai melalui kode QR).



### 5.2. Transmisi onchain (jaringan Bitcoin)



#### 5.2.1. Layar kirim



**Tindakan**: Memasukkan atau memindai Bitcoin onchain Address





- Jika jumlahnya belum ditentukan, misalnya :



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```





- Kemudian, Anda dapat memilih pada layar kirim :
 - Jumlah dalam BTC, sat atau fiat. Jumlah minimum: 546 satoshi pada tanggal 22/07/2025.
 - Catatan opsional untuk mengidentifikasi transaksi. Hanya dapat dilihat oleh Anda, dalam detail transaksi.



![image](assets/fr/14.webp)





- Jika jumlahnya sudah ditentukan, misalnya :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



Anda kemudian akan dibawa langsung ke layar konfirmasi di bawah ini.



#### 5.2.2 Layar konfirmasi



Luangkan waktu untuk memeriksa semua parameter, terutama jumlah, tujuan Address dan biaya.


Setelah itu, Anda dapat menyesuaikan parameternya:



![image](assets/fr/15.webp)




- Biaya**: Anda dapat memilih :
  - Kecepatan eksekusi** transaksi Anda, dan biaya terkait akan diperkirakan
  - Baik biaya**, dalam mode biaya absolut (total biaya dalam satoshi) atau biaya relatif (biaya per byte), dan kecepatan transaksi Anda akan diperkirakan





- Pengaturan lanjutan** :





 - Replace-by-fee (RBF)**: Diaktifkan secara default, fungsi ini mempercepat transaksi dengan membayar biaya yang lebih tinggi (lihat Lampiran 4 untuk rinciannya).





 - Pemilihan UTXO secara manual**: Jika dana Anda disimpan di beberapa alamat Wallet yang berbeda, Anda dapat memilih alamat yang akan digunakan untuk mengirim dana. Mengapa Anda harus melakukan ini? Dengan meningkatnya penggunaan Bitcoin, biaya transfer meningkat. Mengirim dari beberapa alamat dengan jumlah kecil lebih mahal daripada mengirim dari satu Address, tetapi dengan melakukannya sekarang, Anda tidak perlu melakukannya nanti, ketika biaya akan menjadi lebih tinggi. Hal ini disebut **konsolidasi UTXO.**



![image](assets/fr/16.webp)





- Mengirim dengan PayJoin**: Jika fungsi ini telah diaktifkan oleh penerima yang memberikan URI, mis:



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



Kemudian Bull Bitcoin Mobile akan mengonfigurasi pengiriman dengan menggabungkan UTXO Anda dengan UTXO penerima sebagai input, sehingga meningkatkan kerahasiaan (lihat Lampiran 3 untuk detailnya).



### 5.3. Kirim ke Liquid



#### 5.3.1 Layar Kirim



Jaringan **Liquid** memungkinkan transaksi yang cepat (~2 menit berkat satu blok per menit), lebih rahasia (jumlah yang disembunyikan) dibandingkan dengan jaringan onchain, dan dengan biaya yang sangat rendah. Dana ditarik dari **Pembayaran Instan Wallet**.



**Tindakan**: Memasukkan atau memindai Liquid Address





- Jika jumlahnya belum ditentukan, misalnya :



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```



Kemudian, Anda dapat memilih pada layar kirim :




- Jumlah dalam BTC, sat atau fiat. Tidak ada minimum, 1 Satoshi mungkin;
- Catatan opsional untuk mengidentifikasi transaksi. Hanya dapat dilihat oleh Anda, dalam detail transaksi.



![image](assets/fr/17.webp)





- Jika jumlahnya sudah ditentukan, misalnya :



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



Anda kemudian akan dibawa langsung ke layar konfirmasi di bawah ini.



#### 5.3.2 Layar konfirmasi



Luangkan waktu untuk memeriksa semua parameter, terutama jumlah dan tujuan Address.



![image](assets/fr/18.webp)





- Biaya**: Proporsional dengan kompleksitas transaksi, umumnya berdasarkan 0,1 sat/vB, yaitu 20-40 satoshi untuk transaksi sederhana (33 Sats pada 22/07/2025).



### 5.4. Kirim ke Lightning



#### 5.4.1 Layar Kirim



Jaringan **Lightning** memungkinkan pembayaran instan dan berbiaya rendah untuk jumlah kecil, ideal untuk transaksi harian yang kecil.



**Aksi**: Memasukkan atau memindai Lightning Invoice





- Jika Anda memindai LN-URL Address yang memungkinkan Anda mengatur jumlahnya


Contoh: `orangepeel@walletofsatoshi.com`.


maka Anda dapat memilih pada layar kirim :




 - Jumlah dalam BTC, satoshi atau fiat. Jumlah minimum 1000 satoshi pada tanggal 23/07/2025
 - Catatan opsional untuk mengidentifikasi transaksi. Catatan ini akan dikirim ke penerima.



![image](assets/fr/19.webp)





- Jika Anda memindai Lightning Invoice yang berisi jumlah tertentu


Contoh:



```
lnbc210n1p58hhk6bullbitcoint4a9jq34dmrmcrursjmw3wjf8elz0nxtdsw9pscqzyssp52jg9dm8vc3xy26er5rc965lxjllhd82je97au7ysvv6lpq7r7shs9q7sqqqqqqqqqqqqqqqqqqqsqqqqqysgqdqqmqz9gxqyjw5qrzjqwryaup9lh50kkranzgcdnn2fgvx390wgj5jd07rwr3vxeje0glclle6wrlm37k39uqqqqlgqqqqqeqqjqnf7w9f2evnzptm2vtdknk7483hsndkl98c4mv2kfe64v5pkq0j6x2dqt9y9wayszv3z33az7c8hkj3yqj9jd7ans7ugq8xv0xefp23gqltph72
```



Anda kemudian akan dibawa langsung ke layar konfirmasi di bawah ini.



Catatan: jumlah harus lebih besar dari 21 Sats pada 23/07/2025



#### 5.4.2 Pengoperasian, batasan dan manfaat





- Mekanisme**: Dana diambil dari **Pembayaran Instan Wallet** (Liquid) dan dikonversi melalui swap **Liquid → Lightning** dengan **Boltz**.





- Batasan:** Batas
 - Jumlah minimum** lebih tinggi dari Wallet Lightning asli (lihat di atas)
 - Biaya** ditambah Liquid → Lightning swap melalui Boltz





- Manfaat** :
 - Penitipan mandiri**: Dana Anda tetap berada di bawah kendali Anda, disimpan di Liquid Network, dan dapat ditransfer melalui Lightning jika diperlukan
 - Tidak ada biaya onchain yang tinggi**: Menyimpan di Liquid telah menghemat deposit onchain yang mahal untuk membuka saluran Lightning Anda atau menambah likuiditas. Operasi ini dapat dilakukan nanti, ketika jumlah yang terkumpul di Liquid sesuai dengan biaya.





- Tip:** Jika penerima memiliki Wallet Bull Bitcoin, gunakan Liquid Network secara langsung untuk menghindari biaya swap



#### 5.3.3 Layar konfirmasi



Luangkan waktu untuk memeriksa semua parameter, terutama jumlah dan tujuan Address.



![image](assets/fr/20.webp)




## 6. Lihat riwayat



**Bull Bitcoin Mobile** memudahkan untuk melacak transaksi Anda di jaringan **Bitcoin (onchain)**, **Liquid**, dan **Lightning**. Riwayat dapat diakses dengan dua cara, dan menampilkan informasi terperinci untuk setiap jenis transaksi. Anda juga dapat memeriksa transaksi Anda menggunakan browser blok eksternal.



### 6.1. Riwayat akses





- Melalui layar beranda** :
 - Klik pada **Secure Bitcoin Wallet** untuk melihat transaksi **onchain**, atau pada **Pembayaran Instan Wallet** untuk transaksi **Liquid** dan **Lightning**.
 - Riwayat ditampilkan langsung di bawah total portofolio, disaring menurut jenis Wallet yang dipilih.



![image](assets/fr/21.webp)





- Melalui halaman khusus** :
 - Pada layar Beranda, klik **simbol riwayat** (ikon jam atau yang serupa).
 - Mengakses halaman yang berisi daftar semua transaksi, dengan filter berdasarkan jenis tindakan: **Kirim**, **Terima**, **Tukar**, **PayJoin**, **Jual**, **Beli** (catatan: Jual dan Beli sedang dalam pengembangan dan belum tersedia untuk saat ini, 20 Juli 2025).



![image](assets/fr/22.webp)



### 6.2. Rincian transaksi



Setiap transaksi menampilkan informasi spesifik tergantung pada jaringan dan jenis tindakan (mengirim atau menerima). Berikut adalah detail yang tersedia untuk **transaksi di blockchain**:



![image](assets/fr/23.webp)



### 6.3. Memeriksa melalui Block explorer



Daftar penjelajah untuk jaringan **Bitcoin onchain**, **Liquid** dan **Lightning** ada di Lampiran 4.



Untuk **Lightning**, transaksi tidak terlihat di browser umum. Periksa detail (termasuk Swap ID untuk Boltz) di aplikasi.




## 7. Pengaturan



Halaman "Pengaturan" dapat diakses secara langsung dari halaman beranda aplikasi Bull Bitcoin, dan digunakan untuk mengonfigurasi dan mengelola berbagai aspek portofolio dan pengalaman pengguna.



![image](assets/fr/24.webp)





- Wallet Pencadangan**: Menampilkan frasa pemulihan portofolio untuk pencadangan yang aman. Lihat bagian 3. tentang pembuatan portofolio untuk praktik terbaik dalam mengelola dan menyimpan frasa pemulihan.





- Detail Wallet**:
 - Kunci publik**: Kunci publik yang terkait dengan Wallet, digunakan untuk alamat penerimaan generate Bitcoin.
 - Jalur Turunan**: Jalur turunan yang digunakan untuk alamat generate Wallet dari kunci privat.





- Server Electrum (Node Bitcoin)**: Siapkan koneksi ke node Bitcoin yang disesuaikan untuk transaksi onchain.





- Kode PIN**: Mengaktifkan dan/atau memodifikasi kode keamanan untuk melindungi akses ke aplikasi dan fungsi Wallet.





- Mata uang**: Pilih apakah akan menampilkan jumlah dalam BTC atau Sats, dan mata uang fiat default (dolar, euro, dll.).





- Pengaturan Penukaran Otomatis**: Fungsi _Auto Swap_ memungkinkan Anda untuk mengotomatiskan transfer BTC Anda dari **Pembayaran Instan Wallet (Liquid)** ke **Bitcoin On-Chain** Wallet Anda, segera setelah jumlahnya mencapai ambang batas yang Anda anggap cukup tinggi untuk menjustifikasi biaya transaksi.





- Log**: Log aktivitas yang dapat dilihat, yang dapat dibagikan dengan dukungan teknis untuk memfasilitasi pemecahan masalah.





- Akses Telegram untuk mendapatkan bantuan** : Tautan langsung ke saluran Telegram resmi untuk bantuan pengguna.





- Akses Github** : Tautan ke [repositori Github Bull Bitcoin] (https://github.com/SatoshiPortal) untuk melihat kode sumber terbuka atau melaporkan masalah.




## LAMPIRAN



### A1. Penjelasan tentang PayJoin (P2EP)



![image](assets/fr/25.webp)



**Definisi** :




- PayJoin, atau **Pay-to-EndPoint (P2EP)**, adalah teknik transaksi Bitcoin yang meningkatkan kerahasiaan pada jaringan **onchain**. Teknik ini menggabungkan entri pengirim dan penerima dalam satu transaksi, membuat jumlah dan alamat lebih sulit dilacak.



**Operasi:**




- Dalam transaksi PayJoin, pengirim dan penerima bekerja sama melalui server PayJoin yang kompatibel untuk melakukan transaksi bersama generate.
- Alih-alih hanya pengirim yang menyediakan entri (UTXO), penerima juga berkontribusi dengan salah satu UTXO-nya sendiri. Hal ini mengaburkan informasi yang terlihat pada Blockchain: alih-alih satu entri yang sesuai dengan jumlah sebenarnya, sekarang ada dua entri, dan output tidak secara langsung mencerminkan jumlah yang dipertukarkan.
- Transaksi akhir menyerupai transaksi Bitcoin standar (multi-input/multi-output), tetapi menyembunyikan jumlah aktual yang dikirim dan tautan antar alamat berkat struktur steganografi.



**Untuk digunakan di Bull Bitcoin Mobile**




- Menerima** (Address Supply): PayJoin diaktifkan secara default.
- Kirim** : Wallet secara otomatis mendeteksi URI PayJoin dan mengonfigurasi transaksi yang sesuai, misalnya:



```
bitcoin:bc1qp2nxbullbticoinzt6tx7x5tlnpzhv37?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F475QR36G3ZCFZ%23...
```




**Manfaat**




- Kerahasiaan yang ditingkatkan**: PayJoin mematahkan asumsi bahwa semua entri dalam sebuah transaksi adalah milik satu entitas. Dengan PayJoin, input berasal dari pengirim dan penerima, mematahkan asumsi ini.
- Penyembunyian jumlah** : Jumlah aktual yang dipertukarkan tidak muncul secara langsung di output. Jumlah ini dihitung sebagai selisih antara UTXO masuk dan keluar dari penerima, sehingga membuat analisis menjadi tidak akurat.



**Batas**




- PayJoin mengharuskan pengirim dan penerima untuk menggunakan dompet yang kompatibel, jika tidak, transaksi onchain standar akan digunakan.
- Transaksi ini sedikit lebih kompleks (lebih banyak input dan output), sehingga menghasilkan biaya yang sedikit lebih tinggi.
- Meskipun dirancang untuk menyerupai transaksi standar, heuristik tingkat lanjut (misalnya output yang ambigu, server PayJoin yang dikenal) dapat membuat seseorang mencurigai penggunaannya, meskipun tanpa kepastian mutlak.



**Info lebih lanjut:**




- [Glosarium](https://planb.network/fr/resources/glossary/payjoin)
- Chapitre [Les transactions PayJoin](https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c/c1e90b95-f709-4574-837b-2ec26b11286f)




### A2. Penjelasan tentang Replace-by-fee (RBF)



**Definisi**: Replace-by-fee (RBF) adalah fitur jaringan Bitcoin yang memungkinkan pengirim untuk mempercepat konfirmasi transaksi **onchain** dengan menyetujui untuk membayar biaya yang lebih tinggi.



**Batas** :




- RBF tidak tersedia untuk transaksi Liquid atau Lightning.
- Transaksi awal harus ditandai sebagai kompatibel dengan RBF saat dibuat, yang dilakukan secara otomatis oleh Bull Bitcoin Mobile kecuali jika dinonaktifkan.



**Info lebih lanjut:**




- [Glosarium](https://planb.network/fr/resources/glossary/rbf-replacebyfee)




### A3. Praktik terbaik



Untuk menggunakan **Bull Bitcoin Mobile** dengan aman dan efisien, ikuti rekomendasi berikut ini. Rekomendasi ini akan membantu Anda melindungi dana Anda, mengoptimalkan transaksi Anda, dan menjaga kerahasiaan Anda di jaringan **Bitcoin (onchain)**, **Liquid**, dan **Lightning**.





- Amankan frasa pemulihan Anda** :
 - Tutorial: [Save your Mnemonic phrase](https://planb.network/fr/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270)
 - Cours [La phrase mnémonique](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8f9340c1-e6dc-5557-a2f2-26c9669987d5)





- Gunakan autentikasi yang aman** :
 - Aktifkan **PIN yang kuat** atau **otentikasi biometrik** (sidik jari atau pengenalan wajah) untuk melindungi akses ke aplikasi.
 - Jangan pernah membagikan PIN atau data biometrik Anda.





- Lindungi privasi Anda** :
 - generate Address baru untuk setiap penerimaan onchain atau Liquid untuk membatasi penelusuran pada Blockchain.
 - Gunakan PayJoin jika tersedia untuk meningkatkan kerahasiaan mengenai jumlah yang dikirim pada blockchain
 - Untuk kerahasiaan maksimum, sambungkan Wallet Anda ke node Bitcoin Anda sendiri melalui server Electrum alih-alih menggunakan node publik





- Pilih jaringan yang paling sesuai dengan kebutuhan Anda**:
 - Onchain**: Lebih disukai untuk penyimpanan jangka panjang atau transaksi bernilai besar (biaya dapat diabaikan dalam kaitannya dengan jumlah).
 - Liquid**: Digunakan untuk transfer cepat dan berbiaya rendah dengan kerahasiaan yang ditingkatkan.
 - Kilat**: Pilihlah transfer instan dan berbiaya rendah untuk jumlah kecil. Jika Anda adalah dua pengguna Wallet Bull Bitcoin, pilih Liquid untuk menghindari biaya pertukaran Lightning <> Liquid melalui Boltz.





- Selalu periksa alamat pengiriman**:
 - Sebelum mengirim dana, periksa Address dengan cermat. Dana yang dikirim ke Address yang salah akan hilang selamanya. Gunakan salin/tempel atau pemindaian kode QR, jangan pernah menyalin/memodifikasi Address dengan tangan.





- Mengoptimalkan biaya**:
 - Untuk transaksi onchain, pilih biaya yang sesuai (lambat, sedang, cepat) sesuai dengan urgensi dan kepadatan jaringan.
 - Gunakan Liquid, atau Lightning untuk jumlah kecil.
 - Aktifkan Replace-by-fee (RBF) (lihat Lampiran 4) untuk pengiriman onchain jika Anda mengantisipasi kebutuhan untuk mempercepat konfirmasi.





- Selalu perbarui aplikasi




### A4. Sumber daya tambahan





- Tautan dan dukungan resmi:** Tautan resmi
 - [staff@bitcoinsupport.com](mailto:staff@bitcoinsupport.com)**, support@bullbitcoin.com : email dukungan
 - [Situs web resmi Bull Bitcoin] (https://bullbitcoin.com/) :** Informasi tentang layanan Bull Bitcoin, pembuatan akun, akses ke aplikasi
 - [GitHub Bull Bitcoin Mobile](https://github.com/SatoshiPortal/bullbitcoin-mobile) :** Lihat kode, evolusi dan peta jalan, berkontribusi pada pengembangan...
 - [Akun X - Twitter Banteng Bitcoin](https://x.com/BullBitcoin_)**
 - Grup Telegram** untuk ponsel Wallet: obrolan grup dengan dukungan, lihat halaman "Pengaturan".





- Penjelajah Blok: ** Penjelajah Blok
 - on chain: **[Mempool.space](https://Mempool.space/)**
 - Liquid: ** [Info Blockstream] (https://blockstream.info/Liquid) **
 - Petir: **[1ML (Lightning Network)](https://1ml.com/)**





- Pembelajaran dan tutorial:** **[Plan ₿ Network](https://planb.network/)** :
 - Mengamankan frasa pemulihan Anda



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Liquid Network**:
 - [Glosarium](https://planb.network/resources/glossary/liquid-network)**




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727





- Lightning Network**:
 - [Glosarium](https://planb.network/resources/glossary/lightning-network)**




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


### A5. Banteng Bitcoin



#### Gambaran umum perusahaan



**[Bull Bitcoin](https://www.bullbitcoin.com/fr)**, adalah platform Exchange non-depositori tertua yang didedikasikan khusus untuk Bitcoin, didirikan pada tahun 2013 di Kedutaan Besar Bitcoin di Montreal, Kanada. Dipimpin oleh Francis Pouliot, pelopor yang diakui dalam ekosistem Bitcoin, perusahaan ini memposisikan diri sebagai pemain kunci dalam mempromosikan kedaulatan keuangan dan otonomi pengguna. Misinya adalah memungkinkan individu untuk mendapatkan kembali kendali atas uang mereka dengan menggunakan Bitcoin sebagai alat untuk kebebasan dan pembayaran, sambil menolak mata uang fiat dan mata uang kripto selain Bitcoin.



![image](assets/fr/26.webp)



[Buat akun Anda] (https://app.bullbitcoin.com/registration/orangepeel) dengan diskon 0,25% untuk pembelian dan penjualan Bitcoin.



#### Nilai-nilai dan filosofi



Bull Bitcoin menonjol karena prinsip-prinsip Commitment hingga Cypherpunk dan etika Bitcoin:





- Fokus eksklusif pada Bitcoin**: Platform ini sesuai dengan visi mata uang yang terdesentralisasi dan tahan sensor.





- Bukan kustodian**: Pengguna memegang kendali penuh atas Bitcoin mereka dengan mengirimkan dana ke portofolio mereka sendiri.





- Kerahasiaan**: Meminimalkan pengumpulan data pribadi, dengan opsi pembelian bebas KYC untuk transaksi di bawah 999 USD. Data dilindungi sesuai dengan peraturan (FINTRAC di Kanada, AMF di Prancis).





- Transparansi**: Tidak ada biaya tersembunyi, biaya sudah termasuk dalam spread (selisih antara harga beli dan harga jual).





- Kedaulatan finansial**: Bull Bitcoin mendorong kemandirian dari sistem perbankan tradisional dan lembaga-lembaga terpusat.



#### Layanan utama





- Setoran fiat**: Pengguna dapat mendanai akun Bull Bitcoin dengan mata uang fiat (CAD, EUR, dll.) melalui transfer bank atau kartu tunai/debit di kantor pos Kanada tertentu.





- Membeli Bitcoin**: Pengguna dapat membeli Bitcoin yang dikirim langsung ke portofolio non-deposito mereka, menjamin kontrol penuh atas dana mereka.





- Pembelian Bitcoin terjadwal**: Bull Bitcoin menawarkan layanan pembelian berulang otomatis (DCA - Dollar Cost Averaging) secara berkala, menggunakan saldo Anda yang tersedia, dengan transfer Bitcoin langsung ke Wallet yang dikendalikan pengguna, sehingga mengurangi dampak volatilitas harga.



Perhatikan bahwa opsi yang disebut "AutoBuy" memungkinkan Anda untuk mengonversi fiat Anda segera setelah menyentuh saldo Bull Bitcoin Anda, dan mengirim Bitcoin Anda ke Wallet Anda sendiri. Opsi ini juga dapat dikombinasikan dengan transfer bank berulang yang dijadwalkan dengan bank Anda untuk membuat DCA. Opsi ini mengotomatiskan akumulasi Bitcoin Anda tanpa harus membuka aplikasi.






- Membeli Bitcoin pada harga tetap 'Limit Order'**: Memungkinkan Anda membeli Bitcoin pada harga yang ditentukan sebelumnya oleh pengguna, yang secara otomatis dieksekusi ketika harga indeks Bull Bitcoin mencapai atau turun di bawah batas yang ditetapkan.





- Menjual Bitcoin**: Pengguna dapat menjual Bitcoin mereka dan menerima dana dalam mata uang fiat langsung ke rekening bank mereka melalui transfer bank atau SEPA.





- Pembayaran pihak ketiga**: Bull Bitcoin memungkinkan pengguna untuk mengirim uang fiat ke rekening bank dari Bitcoin mereka, sepenuhnya transparan kepada penerima.





- Bull Bitcoin Prime**: Bull Bitcoin Prime adalah layanan premium untuk nasabah dengan kekayaan bersih tinggi dan nasabah perusahaan, yang menawarkan solusi khusus dan dukungan premium. Layanan ini mencakup akses ke biaya yang lebih rendah, manajer akun khusus, dan layanan korporat yang disesuaikan. Layanan ini ditujukan untuk institusi, trader profesional, dan klien korporat yang mencari keahlian mendalam dan layanan prioritas.





- Mobile Wallet**: Bull Bitcoin menawarkan Wallet seluler sumber terbuka, kustodian mandiri, tersedia di Android dan iOS, yang mendukung transaksi onchain, Liquid, dan Lightning Network.





- Dukungan pendidikan**: Panduan gratis dan pelatihan yang dipersonalisasi untuk membantu pengguna membuat, mengamankan, dan mengelola portofolio Bitcoin mereka, sehingga memperkuat otonomi keuangan.



#### Kepatuhan dan keamanan





- Regulasi**: Terdaftar di FINTRAC (Kanada) dan AMF (Prancis), Bull Bitcoin mematuhi persyaratan KYC/AML.





- Keamanan**: Penggunaan portofolio yang aman dan rekomendasi penyimpanan offline. Data pribadi dihosting pada infrastruktur Bitcoin Bull, yang 100% dihosting sendiri dan tidak bergantung pada pihak ketiga mana pun.