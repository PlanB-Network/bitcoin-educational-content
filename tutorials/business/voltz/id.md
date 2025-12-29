---
name: Voltz
description: Lightning wallet all-in-one untuk bisnis Anda.
---

![cover](assets/cover.webp)



Ide untuk platform Voltz berasal dari sekelompok bitcoiners yang ingin menyediakan layanan wallet bitcoin mereka sendiri. Hasilnya adalah sebuah infrastruktur yang lengkap untuk menerima bitcoin secara eceran. Dalam tutorial ini, kami akan mengajak Anda berkeliling Voltz dan kemungkinan integrasi bitcoin yang ditawarkan oleh platform ini.



## Memulai dengan Voltz



Selain sebagai kustodian Lightning wallet yang memungkinkan Anda mengirim, menerima, dan membayar setiap hari, Voltz adalah platform lengkap yang menyediakan banyak ekstensi untuk mengintegrasikan bitcoin sebagai titik penjualan atau pasar dalam bisnis Anda.



Buka platform [Voltz] (https://www.voltz.com/en) dan buat akun dengan mengeklik tombol "Coba sekarang".



![voltz](assets/fr/01.webp)



![login](assets/fr/02.webp)



⚠️ Penting untuk menetapkan kata sandi alfanumerik yang kuat untuk meningkatkan peluang Anda terhadap serangan brute-force, dan pastikan bahwa Anda memang berada di situs web resmi Voltz untuk mengisi detail login Anda untuk melindungi Anda dari phishing.



Antarmuka Voltz sangat mirip dengan platform LnBits.



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

Voltz sebenarnya dibangun di atas server LnBits; lihat tutorial kami untuk mempelajari cara memasang server LnBits Anda sendiri dan membangun solusi Anda di atasnya.



https://planb.academy/tutorials/business/others/lnbits-server-6a406046-3cef-4a64-a82b-8d8f0f82a192

Platform ini memungkinkan Anda untuk mengelola beberapa portofolio secara efisien. Secara default, ketika Anda mendaftar, Anda secara otomatis memiliki portofolio Lightning. Namun, Anda bisa menambahkan portofolio lain.



![wallets](assets/fr/03.webp)



### Portabilitas



Voltz tidak terbatas pada antarmuka web: di bagian **Akses Seluler**, Anda dapat menghubungkan Voltz wallet yang aktif ke aplikasi seperti Zeus atau Blue Wallet.



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

Untuk melakukan ini, Anda perlu menginstal dan mengaktifkan ekstensi **LndHub** pada platform.



![lndhub](assets/fr/04.webp)



Pilih portofolio Voltz Anda yang aktif dan, tergantung pada hak yang ingin Anda berikan, pindai kode QR yang sesuai.




- Kode QR faktur hanya memungkinkan Anda untuk membaca riwayat portofolio Anda dan faktur baru generate.
- Kode QR admin memungkinkan Anda untuk melihat riwayat, faktur generate, dan juga membayar faktur Lightning.



![qrs](assets/fr/05.webp)



Dalam tutorial ini, kami menghubungkan Voltz wallet ke aplikasi Blue Wallet.



![connect](assets/fr/06.webp)



Setelah portofolio kami terhubung, semua tindakan yang dilakukan akan disinkronkan antara Blue Wallet dan Voltz. Sebagai contoh, ketika Anda membuat faktur di Blue Wallet, Anda juga memiliki riwayat di Voltz.



![sync](assets/fr/07.webp)



Pada bagian **Konfigurasi portofolio**, Anda akan menemukan parameter minimal seperti penyesuaian nama portofolio dan mata uang yang Anda inginkan untuk menerima pembayaran.



![config](assets/fr/08.webp)



### Ekstensi



Salah satu fitur istimewa dari platform Voltz adalah modularitasnya, yang memungkinkan Anda untuk mengaktifkan ekstensi yang Anda butuhkan. Daftar ekstensi dapat ditemukan di menu **Ekstensi**.



![extensions](assets/fr/09.webp)



Di antara ekstensi ini adalah TPoS, terminal point-of-sale yang dapat Anda gunakan untuk menyimpan inventaris dan mengumpulkan pembayaran dari pelanggan Anda.



![tpos](assets/fr/10.webp)



Dari terminal Point of Sale, Anda dapat :




- Dapatkan halaman web yang dapat Anda bagikan dengan pelanggan dan mitra Anda;
- Mengelola inventaris produk;
- Hasilkan faktur Lightning;
- Pembayaran tunai melalui kartu Bolt.



Ekstensi ini tersedia dalam versi gratis dan versi berbayar untuk fitur-fitur yang lebih canggih. Untuk membuat terminal POS, klik tombol **Buka** di bawah logo ekstensi, lalu klik **New POS**.



![new_tpos](assets/fr/11.webp)



Tentukan nama kasir Anda, lalu hubungkan Voltz wallet ke terminal Anda untuk mengumpulkan pembayaran. Anda dapat mengaktifkan gratifikasi dengan mencentang kotak **Aktifkan gratifikasi**. Aktifkan juga opsi pencetakan faktur jika Anda ingin menerbitkan tanda terima kepada pelanggan Anda (fungsi ini masih dalam pengembangan, jadi mungkin ada kegagalan fungsi).



Terminal point-of-sale juga menyertakan konfigurasi pajak ketika Anda ingin menerapkan pajak negara Anda secara langsung ke produk Anda.



![tpos](assets/fr/12.webp)



Setelah terminal POS Anda dibuat, Anda dapat menambahkan produk dan layanan yang sudah dikonfigurasi sebelumnya untuk memastikan pengalaman pembayaran dan akuntansi yang lancar bagi Anda dan pelanggan Anda.



![product](assets/fr/13.webp)



Buat produk Anda dengan menentukan nama, menambahkan gambar, dan menetapkan harga jual.  Anda dapat mengkategorikan produk Anda untuk memudahkan pelacakan. Anda dapat menerapkan pajak secara langsung ke produk tertentu. Jika produk tidak memiliki pajak yang diterapkan, pajak yang dikonfigurasikan pada tahap pembuatan terminal point-of-sale akan diterapkan secara otomatis.



![products](assets/fr/14.webp)



Anda dapat mengimpor daftar produk Anda secara otomatis dari format JSON dengan mengklik tombol **Import/Export**.



![exports](assets/fr/15.webp)



Akses area checkout melalui tautan dengan mengklik ikon **Tab Baru**, atau bagikan platform POS Anda melalui kode QR kepada pelanggan dengan mengklik ikon **Kode QR**.



![lien](assets/fr/16.webp)



![qr](assets/fr/17.webp)



Pelanggan Anda dapat melihat katalog Anda dan melakukan pembayaran dari antarmuka ini.



![pos](assets/fr/18.webp)



![chose](assets/fr/19.webp)



![pay](assets/fr/20.webp)



![checkout](assets/fr/21.webp)



Dalam kelompok ekstensi yang tersedia, Anda juga akan menemukan alat bantu seperti ekstensi **Invoice** dan **Payment Link**, yang memungkinkan Anda membuat faktur generate dengan produk tertentu untuk mengumpulkan pembayaran yang terisolasi tanpa melalui terminal POS.



## Melacak pembayaran Anda



Di menu **Pembayaran**, Voltz memberi Anda gambaran umum tentang pembayaran ke berbagai portofolio Anda.


Anda dapat melacak pembayaran Anda dengan :




- Status.
- Label: misalnya **TPOS** untuk pembayaran di tempat penjualan dan **lnhub** melalui koneksi seluler di dompet Zeus dan Blue Wallet.
- Portofolio koleksi.
- Total pembayaran masuk dan keluar.
- Periode yang terdefinisi dengan baik.



![payments](assets/fr/22.webp)



## Opsi lainnya



Voltz juga merupakan infrastruktur tempat Anda dapat membangun solusi Anda sendiri. Di bagian **Ekstensi**, Anda akan menemukan panduan untuk mengembangkan ekstensi Anda sendiri dalam ekosistem Voltz dan LnBits.



![build](assets/fr/23.webp)



Jika Anda ingin mengembangkan solusi di luar ekosistem tetapi masih menggunakan infrastruktur mereka, di bagian **URL node**, Anda akan menemukan kunci API dan informasi dokumentasi dengan contoh apa yang dapat Anda lakukan dengan data ini.



Anda dapat membuat faktur Lightning dari aplikasi Anda menggunakan Voltz wallet, membayar faktur Lightning, memecahkan kode, dan memverifikasi faktur.



![keys](assets/fr/24.webp)



Sekarang Anda sudah memiliki pemahaman yang baik tentang Voltz. Jika Anda menikmati tutorial ini, kami yakin Anda akan belajar lebih banyak tentang metode dan alat terbaik untuk mengintegrasikan bitcoin ke dalam bisnis Anda dengan kursus kami: Bitcoin untuk bisnis.



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a