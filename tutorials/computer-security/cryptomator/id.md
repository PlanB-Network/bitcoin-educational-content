---
name: Cryptomator
description: Enkripsi file Anda di awan
---
![cover](assets/cover.webp)



___



*Tutorial ini didasarkan pada konten asli oleh Florian BURNEL yang dipublikasikan di [IT-Connect](https://www.it-connect.fr/). Lisensi [CC BY-NC 4.0] (https://creativecommons.org/licenses/by-nc/4.0/). Perubahan mungkin telah dilakukan pada teks asli.*



___



## I. Presentasi



Dalam tutorial ini, kita akan menggunakan aplikasi Cryptomator untuk mengenkripsi data yang tersimpan di Cloud, baik di Microsoft OneDrive, Google Drive, Dropbox, Box, atau bahkan iCloud.



Mengenkripsi data yang Anda simpan di solusi penyimpanan online seperti Drive adalah cara terbaik untuk melindungi file dan privasi Anda. Berkat enkripsi, Anda adalah satu-satunya orang yang dapat mendekripsi dan membaca data Anda, meskipun data tersebut disimpan di server di Amerika Serikat atau negara lain di seluruh dunia.



Dalam demonstrasi ini, mesin Windows 11 22H2 dengan OneDrive akan digunakan, tetapi prosedurnya sama pada versi Windows lainnya dan layanan penyimpanan lainnya. Yang perlu Anda lakukan adalah menginstal klien sinkronisasi dan menambahkan akun Anda. Ini akan memungkinkan Cryptomator untuk menyimpan datanya di lemari besi.



![Image](assets/fr/020.webp)



Cryptomator merupakan alternatif dari aplikasi lain, terutama Picocrypt yang disajikan pada artikel lain, yang terlihat berbeda, tetapi sama-sama mudah digunakan. Cryptomator juga **sumber terbuka**, sesuai dengan RGPD, dan akan mengenkripsi data dengan algoritma enkripsi AES-256 bit**. Sebaliknya, Picocrypt mengandalkan algoritma XChaCha20 yang lebih cepat (juga 256-bit).



https://planb.network/tutorials/computer-security/data/picocrypt-98c213bd-9ace-425b-b012-bea71ce6b38f

Aplikasi Cryptomator tersedia di **Windows** (exe / msi), **Linux**, **macOS,** tetapi juga **Android** dan **iOS**. Omong-omong, semua aplikasi gratis, kecuali aplikasi Android, yang harus Anda bayar (14,99 euro).



Pada komputer Anda, **Cryptomator akan membuat sebuah folder yang di dalamnya akan dibuat brankas**. Di dalam brankas tersebut, yang mungkin disimpan di OneDrive, Google Drive, atau sejenisnya, data Anda akan dienkripsi. Jadi, jika Anda menyimpan semua data Anda di brankas yang di-host di ruang penyimpanan Drive Anda, data tersebut akan terlindungi (karena dienkripsi).



**Catatan**: dalam artikel ini, layanan penyimpanan online digunakan sebagai contoh, tetapi Cryptomator dapat digunakan untuk mengenkripsi data di disk lokal, disk eksternal, atau bahkan NAS. Sebenarnya tidak ada batasan.



## II. Memasang Cryptomator



Untuk memulai, Anda perlu mengunduh dan menginstal **Cryptomator**. Setelah pengunduhan selesai, hanya perlu beberapa klik untuk menyelesaikan instalasi. Seperti [Rclone](https://www.it-connect.fr/rclone-un-outil-gratuit-pour-synchroniser-vos-donnees-dans-le-cloud/), Cryptomator akan bergantung pada WinFsp untuk memasang drive virtual pada mesin Windows Anda.





- [Unduh Cryptomator dari situs web resmi](https://cryptomator.org/downloads/)



![Image](assets/fr/025.webp)



## III. Menggunakan Cryptomator pada Windows



### A. Membuat brankas baru



Untuk membuat brankas baru, klik tombol "**Tambah**" dan pilih "**Brankas baru...**". Brankas yang sudah ada dan diketahui di mesin ini akan muncul di Interface, di sebelah kiri. **Brankas yang dibuat di mesin A dapat dibuka dan dimodifikasi di mesin B**, asalkan mesin tersebut dilengkapi dengan Cryptomator (dan kunci enkripsinya diketahui).



![Image](assets/fr/015.webp)



Mulailah dengan memberikan nama pada brankas, misalnya "**IT-Connect**". Ini akan membuat direktori bernama "**IT-Connect**" di OneDrive saya.



![Image](assets/fr/011.webp)



Pada langkah berikutnya, Cryptomator kemungkinan akan **mendeteksi "Drive "** yang ada di komputer Anda: Google Drive, OneDrive, Dropbox, dll.... Untuk memungkinkan Anda memilih penyedia secara langsung. Saya sudah mencobanya di dua mesin Windows 11 yang berbeda, dengan beberapa Drive, dan tidak terdeteksi. Ini bukan masalah, cukup tentukan "**Lokasi Khusus**" dan pilih root dari ruang penyimpanan Anda. Sebagai contoh: **C:\Users\<Nama Pengguna>\OneDrive**.



![Image](assets/fr/018.webp)



Berikutnya, Anda dapat menyesuaikan opsi di bawah pengaturan pakar.



![Image](assets/fr/021.webp)



Selanjutnya, Anda perlu menentukan kata sandi yang sesuai dengan kunci enkripsi. Kata sandi ini akan memungkinkan anda untuk membuka kunci brankas Cryptomator dan mengakses datanya. **Jika Anda kehilangan kata sandi ini, Anda akan kehilangan akses ke data Anda. Terakhir, anda masih memiliki pilihan untuk **membuat kunci cadangan** dengan mencentang opsi "**Ya, lebih baik aman daripada menyesal**", dengan semangat yang sama dengan kunci pemulihan [BitLocker] (https://www.it-connect.fr/comment-activer-bitlocker-sur-windows-11-pour-chiffrer-son-disque/). Hal ini disarankan, tetapi jangan simpan kunci cadangan ini di root OneDrive Anda!



Klik "**Buat brankas**".



![Image](assets/fr/019.webp)



Salin kunci pemulihan dan simpan di pengelola kata sandi favorit Anda. Klik "**Selanjutnya**".



![Image](assets/fr/013.webp)



Selesai, bagasi baru Anda sudah dibuat dan siap digunakan!



![Image](assets/fr/014.webp)



### B. Angka akses



Untuk mengakses brankas dan datanya, baik untuk **membaca data yang ada atau menambahkan data baru**, Anda perlu **membuka kuncinya**. Cryptomator menampilkan daftar brankas yang dikenal: brankas IT-Connect muncul, jadi pilih saja dan klik "**Buka Kunci**".



![Image](assets/fr/016.webp)



Anda harus memasukkan kata sandi untuk membuka kunci brankas. Kemudian klik "**Lepaskan drive**".



![Image](assets/fr/022.webp)



**Brankas Anda dipasang pada mesin Windows sebagai drive virtual.** Drive ini, yang di sini mewarisi huruf E, memberi Anda akses ke data Anda (dalam teks biasa, karena brankas tidak terkunci).



![Image](assets/fr/017.webp)



Di sisi OneDrive, kita tidak bisa menelusuri brankas Cryptomator secara langsung. Kita tidak bisa melihat datanya (baik nama file maupun isinya). Ini berarti Anda tidak perlu menambahkan data ke brankas Cryptomator melalui pintasan OneDrive biasa. **Anda harus menambahkan data Anda menggunakan drive virtual Cryptomator



![Image](assets/fr/012.webp)



### C. Opsi bagasi



Pengaturan brankas dapat diakses melalui tombol "**Opsi volume terenkripsi**" (saat terkunci) dan akan mengaktifkan penguncian otomatis jika tidak ada aktivitas, seperti yang dapat Anda lakukan pada brankas kata sandi. Opsi "**Buka kunci volume terenkripsi saat startup**", seperti namanya, akan membuka kunci drive tanpa campur tangan Anda, dan menyambungkan drive virtual. Demi alasan keamanan, sebaiknya hindari mengaktifkan opsi ini.



Melalui tab "**Mounting**", Anda juga dapat memutuskan untuk memasangnya hanya-baca atau menetapkan huruf tertentu.



![Image](assets/fr/024.webp)



Selain itu, dalam pengaturan Cryptomator, Anda dapat **mengaktifkan pengaktifan aplikasi otomatis**.



## IV. Kesimpulan



Dengan **Cryptomator**, Anda bisa **membuat brankas terenkripsi** hanya dalam beberapa menit untuk melindungi data yang ingin Anda simpan di OneDrive dan konsol. Sangat mudah digunakan ketika harus "memasangkannya" dengan Drive: untuk tujuan ini, aplikasi ini lebih saya sukai daripada Picocrypt.