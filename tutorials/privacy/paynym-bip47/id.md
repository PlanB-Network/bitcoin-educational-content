---
name: BIP47 - PayNym
description: Gunakan kode pembayaran yang dapat digunakan kembali di Ashigaru
---
![cover](assets/cover.webp)



Kesalahan privasi terburuk yang bisa Anda lakukan di Bitcoin adalah menggunakan ulang alamat. Setiap kali alamat yang sama menerima beberapa pembayaran, transaksi-transaksi ini akan dihubungkan, memberikan peta transaksi Anda kepada dunia. Oleh karena itu, sangat disarankan agar Anda selalu membuat alamat unik untuk setiap tanda terima. Namun untuk beberapa aplikasi Bitcoin, ini bukanlah hal yang mudah.



BIP47, yang diusulkan oleh Justus Ranvier pada tahun 2015, memberikan jawaban yang elegan untuk masalah ini. Ini memperkenalkan konsep **kode pembayaran yang dapat digunakan kembali**: sebuah pengenal unik yang memungkinkan pembayaran bitcoin onchain dalam jumlah yang hampir tidak terbatas untuk diterima, tanpa harus menggunakan ulang sebuah alamat. Berkat mekanisme kriptografi yang didasarkan pada pertukaran ECDH (*Diffie-Hellman pada kurva elips*), setiap pembayaran ke kode yang sama akan menghasilkan alamat yang kosong, khusus untuk hubungan antara pengirim dan penerima.



![Image](assets/fr/01.webp)



Prinsip BIP47 ini diimplementasikan secara khusus oleh **PayNym**, sistem yang awalnya dikembangkan oleh Samourai Wallet dan sekarang diambil alih oleh Ashigaru. Dalam tutorial ini, kita akan melihat cara mengaktifkan PayNym Anda, menukar kode pembayaran dengan koresponden, dan melakukan transaksi tanpa menggunakan alamat.



Saya tidak akan membahas pengoperasian BIP47 secara mendetail di sini. Jika Anda ingin mempelajari lebih dalam tentang hal ini, silakan lihat bab 6.6 dari kursus pelatihan BTC 204.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Prasyarat



Untuk mengikuti tutorial ini, yang Anda perlukan hanyalah wallet pada aplikasi Ashigaru. Jika Anda tidak tahu cara mengunduh, memverifikasi, menginstal aplikasi atau membuat wallet, saya sarankan Anda membaca tutorial ini terlebih dahulu:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

## Minta PayNym



Langkah pertama adalah mengklaim PayNym Anda. Operasi ini hanya perlu dilakukan satu kali per wallet. Operasi ini mengaitkan kode pembayaran BIP47 Anda yang berasal dari seed (`PM...`) dengan pengenal unik yang spesifik untuk implementasi PayNym. Pengidentifikasi yang lebih pendek dan lebih mudah dibaca ini kemudian dapat dikirimkan ke koresponden Anda untuk memfasilitasi pertukaran, tanpa harus membagikan kode BIP47 yang panjang dan lengkap.



Untuk melakukannya, klik gambar PayNym Anda di kiri atas antarmuka, lalu pada kode pembayaran `PM...`.



![Image](assets/fr/02.webp)



Kemudian klik pada tiga titik kecil di sudut kanan atas, dan pilih `Klaim PayNym`.



![Image](assets/fr/03.webp)



Konfirmasikan dengan mengklik tombol `KLAIM PAYNYM ANDA`.



![Image](assets/fr/04.webp)



Segarkan halaman: ID PayNym Anda sekarang ditampilkan di bawah gambar Anda, tepat di atas kode pembayaran BIP47 Anda.



![Image](assets/fr/05.webp)



PayNym Anda sekarang sudah aktif dan siap digunakan untuk transaksi BIP47 pertama Anda.



## Terhubung dengan kontak



Ada dua jenis koneksi antara PayNym: **follow** dan **connect**. Operasi `follow` sepenuhnya gratis. Operasi ini membuat hubungan antara dua PayNym melalui Soroban, protokol komunikasi terenkripsi berbasis Tor yang dikembangkan oleh tim Samourai dan diadopsi oleh Ashigaru. Tautan ini memungkinkan dua pengguna yang saling mengikuti untuk bertukar informasi secara pribadi, khususnya untuk mengoordinasikan transaksi kolaboratif seperti Stowaway atau StonewallX2, yang akan kita bahas di tutorial lain. Langkah ini khusus untuk PayNym dan bukan bagian dari protokol BIP47.



![Image](assets/fr/06.webp)



Operasi koneksi (`connect`), di sisi lain, membutuhkan transaksi on-chain. Transaksi ini terdiri dari melakukan transaksi notifikasi seperti yang didefinisikan dalam BIP47. Transaksi Bitcoin ini berisi metadata dalam output `OP_RETURN`, yang membentuk saluran komunikasi terenkripsi antara pembayar dan penerima. Dari saluran ini, pembayar akan dapat generate alamat penerima yang unik untuk setiap pembayaran, dan penerima akan diberitahukan tentang pembayaran ini, dan akan dapat generate kunci pribadi yang terkait dengan alamat untuk membelanjakan dana ini nanti.



Transaksi notifikasi ini memiliki biaya: biaya mining dan 546 sats yang dikirim ke alamat notifikasi penerima untuk menandakan koneksi. Setelah koneksi dibuat, pembayaran dalam jumlah yang hampir tak terbatas dapat dilakukan melalui BIP47.



Singkatnya:




- follow": gratis, membangun komunikasi terenkripsi melalui Soroban, berguna untuk alat kolaboratif Ashigaru;
- `Hubungkan`: dikenakan biaya, melakukan transaksi notifikasi BIP47 untuk mengaktifkan saluran antara pembayar dan penerima.



Untuk berinteraksi dengan PayNym, Anda harus terlebih dahulu *mengikutinya*. Ini adalah langkah pertama sebelum membuat koneksi BIP47. Katakanlah Anda ingin mengirim pembayaran berulang ke PayNym `+instinctiveoffer10`.



Buka halaman PayNym Anda di Ashigaru, lalu klik tombol `+` di bagian kanan bawah antarmuka.



![Image](assets/fr/07.webp)



Anda kemudian dapat menempelkan kode pembayaran lengkap penerima, atau memindai kode QR mereka.



![Image](assets/fr/08.webp)



Jika Anda hanya memiliki ID PayNym-nya, buka [Paynym.rs] (https://paynym.rs/) untuk menemukan kode QR yang terkait dengan kode pembayarannya.



![Image](assets/fr/09.webp)



Setelah Anda memindai kode QR, klik tombol `FOLLOW` untuk mengikuti PayNym.



![Image](assets/fr/10.webp)



Tindakan `FOLLOW` sudah cukup untuk transaksi kolaboratif (*kongkalikong). Namun, untuk mengirim pembayaran BIP47, Anda harus membuat koneksi: klik `HUBUNGKAN` untuk melakukan transaksi notifikasi.



![Image](assets/fr/11.webp)



Notifikasi transaksi kemudian disiarkan di jaringan. Tunggu hingga setidaknya ada satu konfirmasi sebelum melakukan pembayaran pertama.



![Image](assets/fr/12.webp)



## Melakukan pembayaran BIP47



Anda sekarang terhubung dengan penerima dan dapat mengirim pembayaran ke alamat unik, yang secara otomatis dibuat menggunakan protokol BIP47, tanpa perlu melakukan pertukaran dengan penerima.



Dari halaman utama PayNym Anda, klik kontak yang ingin Anda kirimi pembayaran.



![Image](assets/fr/13.webp)



Di bagian kanan atas antarmuka, klik ikon panah.



![Image](assets/fr/14.webp)



Masukkan jumlah yang akan dikirim. Anda tidak perlu memasukkan alamat penerima: alamat tersebut akan secara otomatis diturunkan menggunakan protokol BIP47.



![Image](assets/fr/15.webp)



Periksa detail transaksi dengan cermat, termasuk biaya, lalu seret panah hijau di bagian bawah layar untuk menandatangani dan menyiarkan transaksi.



![Image](assets/fr/16.webp)



Transaksi telah terkirim.



![Image](assets/fr/17.webp)



Dalam contoh ini, pembayaran dilakukan ke dompet PayNym saya yang lain. Oleh karena itu, saya dapat melihat bahwa dana tersebut telah sampai di Ashigaru wallet saya yang lain, tanpa ada alamat yang ditukar secara manual: hanya pengenal PayNym yang digunakan.



![Image](assets/fr/18.webp)



Anda sekarang tahu cara menggunakan kode pembayaran yang dapat digunakan kembali BIP47 berkat implementasi PayNym pada aplikasi Ashigaru. Sekarang Anda dapat membagikan kode pembayaran ini kepada siapa saja yang ingin mengirimkan pembayaran kepada Anda (terutama pembayaran berulang). Anda juga dapat mempublikasikan ID PayNym Anda di situs web atau jejaring sosial Anda untuk menerima donasi.



Untuk memperdalam pengetahuan Anda tentang protokol ini, memahami secara detail cara kerjanya dan implikasinya terhadap kerahasiaan, saya sangat menyarankan Anda untuk mengambil kursus BTC 204 saya:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c