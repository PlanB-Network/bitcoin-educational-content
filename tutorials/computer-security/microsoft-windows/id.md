---
name: Windows 11
description: Instalasi Otomatis Microsoft Windows 11 melalui file konfigurasi
---
![cover](assets/cover.webp)


Dalam tutorial ini, kita akan mempelajari cara menginstal Windows 11 secara otomatis menggunakan metode selain proses instalasi Windows standar.


## Download!


Hal pertama yang Anda perlukan adalah file instalasi. Tempat paling aman dan terpercaya untuk mengunduhnya adalah langsung dari situs web resmi Microsoft.


Cukup kunjungi tautan yang disediakan di bawah ini dan ikuti petunjuk untuk mengunduh [file ISO Windows 11](https://www.microsoft.com/en-us/software-download/windows11)


![Image](assets/en/02.webp)


Setelah Anda berada di halaman pengunduhan, gulir ke bawah ke bagian untuk mengunduh file ISO.


![Image](assets/en/01.webp)


َDan pilih versi yang sesuai.


![Image](assets/en/03.webp)


Setelah memilih Windows 11, klik tombol Konfirmasi.


Pada langkah ini, mungkin diperlukan beberapa detik untuk memproses permintaan, lalu Anda akan melihat halaman berikut:


![Image](assets/en/04.webp)


Setelah mengonfirmasi permintaan, Anda harus memilih bahasa yang Anda inginkan.


![Image](assets/en/05.webp)


Setelah memilih bahasa dan mengklik tombol Konfirmasi, permintaan akan diproses. Langkah ini mungkin memerlukan waktu beberapa detik.


Setelah permintaan berhasil diproses, Anda akan melihat halaman dengan tautan unduhan untuk file .iso. Klik tombol Unduh 64-bit untuk memulai pengunduhan.


Ukuran file sekitar 5,5 GB, dan tautan yang dihasilkan akan berlaku selama 24 jam.


## Otomatisasi!


Pada tahap ini, kita perlu membuat perubahan pada instalasi Windows standar. Pada tahap ini, dengan menggunakan penginstalan tanpa pengawasan, kami menentukan item mana yang akan diinstal, tanpa masukan dari pengguna setelahnya. Bahkan, dalam metode ini, file XML digunakan untuk mengonfigurasi langkah-langkah instalasi dan layanan yang diinstal di Windows. Dengan kata lain, penggunaan file Unattended.xml menciptakan proses otomatisasi selama instalasi, mencegah kebutuhan untuk memilih beberapa opsi dan menghindari langkah-langkah membosankan yang biasanya diperlukan selama pengaturan. Metode ini adalah metode yang tidak biasa tetapi standar yang telah diperkenalkan oleh Microsoft. Informasi lebih lanjut tersedia di [situs web resmi Microsoft](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/update-windows-settings-and-scripts-create-your-own-answer-file-sxs?view=windows-11).


Ada berbagai alat yang tersedia di internet untuk menghasilkan file tanpa pengawasan. Beberapa di antaranya online, sementara yang lainnya offline. Salah satu alat online untuk membuat file ini adalah [situs web ini] (https://schneegans.de/windows/unattend-generator). Setelah membukanya, kita akan dihadapkan pada halaman berikut:


![Image](assets/en/06.webp)


Seperti yang disebutkan di bagian atas halaman, metode ini dapat digunakan untuk menginstal Windows 10 dan 11. Pada langkah pertama, kami memilih bahasa Windows. Jika kita perlu menambahkan bahasa kedua atau bahkan bahasa ketiga ke daftar tampilan Windows dan bahasa keyboard, kita dapat menggunakan kotak di bawah ini:


![Image](assets/en/07.webp)


Pada langkah berikutnya, kami memilih lokasi yang diinginkan.


![Image](assets/en/08.webp)


Pada tahap ini, kita juga dapat menentukan arsitektur prosesor untuk komputer. Pada langkah ini, kita bisa:

1. Tentukan apakah akan mengabaikan fitur keamanan Windows, seperti TPM dan Boot Aman. Fitur Boot Aman memastikan bahwa jika ada file inti Windows yang dirusak selama proses boot, masalah akan terdeteksi dan eksekusinya dicegah. Fitur ini juga membantu melindungi sistem dari menginstal pembaruan berbahaya pada Windows. Mengaktifkan opsi untuk melewati fitur ini terkadang tidak dapat dihindari pada komputer tertentu, terutama model lama. Namun, secara umum disarankan untuk tetap mengaktifkan fitur seperti Boot Aman.

2. Abaikan persyaratan untuk koneksi internet untuk menyelesaikan proses. Hal ini berguna dalam situasi di mana koneksi LAN berkabel tidak tersedia, karena dalam banyak kasus, kartu nirkabel belum dikenali selama instalasi Windows, dan akses internet melalui kabel diperlukan. Mengaktifkan opsi ini akan menyelesaikan masalah yang terkait dengan langkah ini.


Pada langkah berikutnya, kita dapat memilih nama untuk komputer.


![Image](assets/en/09.webp)


Kita juga dapat mengizinkan Windows untuk memilih nama untuk sistem. Pada langkah ini, kita dapat memilih jenis Windows, apakah terkompresi atau tidak terkompresi, atau membiarkan Windows menentukan versi yang sesuai berdasarkan spesifikasi komputer. Zona waktu juga dapat diatur pada tahap ini.


Langkah berikutnya melibatkan pengaturan partisi:


![Image](assets/en/10.webp)


Pada tahap ini, kita dapat menentukan jenis partisi untuk menginstal Windows, serta pengaturan yang diperlukan untuk menginstal Windows Recovery Environment. Dengan memilih opsi pertama, pemilihan partisi dan pemartisian ditunda hingga waktu instalasi Windows, dan selama penyiapan, pertanyaan-pertanyaan ini akan ditanyakan seperti pada metode instalasi normal.


Pada langkah ini, kami memilih versi Windows yang akan diinstal:


![Image](assets/en/11.webp)


Jika kunci produk tersedia, kunci tersebut juga dapat dimasukkan pada tahap ini.


Langkah berikutnya adalah mengonfigurasi akun login Windows:


![Image](assets/en/12.webp)


## Pengaturan akun


Pada tahap ini:


1. Kita dapat menentukan nama dan kata sandi untuk akun admin. Kita juga dapat membuat beberapa akun pengguna atau admin.

2. Di sini, kami menentukan akun mana yang akan digunakan untuk masuk pertama kali setelah instalasi Windows. Opsi yang berbeda untuk bagian ini ditunjukkan pada gambar.

3. Jika Anda tidak ingin ada akun yang dibuat, bersihkan semua akun, dan pilih opsi ini. Dalam hal ini, setelah instalasi Windows, Anda akan secara otomatis masuk ke akun Administrator Windows.


Langkah berikutnya adalah mengonfigurasi pengaturan kata sandi dan file host:


![Image](assets/en/13.webp)


Pada tahap ini, kami menentukan apakah kata sandi harus memiliki periode kedaluwarsa. Selain itu, bagian ini mencakup pengaturan keamanan yang terkait dengan upaya login yang gagal, yang dapat diaktifkan atau dinonaktifkan berdasarkan kebutuhan Anda.


Pada bagian bawah bagian ini, terdapat pengaturan untuk tampilan file. Tak satu pun dari opsi ini tersedia selama instalasi Windows standar dan harus dikonfigurasikan setelah instalasi. Sebaliknya, dengan metode penginstalan Tanpa Pengawasan, pengaturan ini mudah diakses.


Langkah berikutnya adalah mengonfigurasi pengaturan keamanan Windows:


![Image](assets/en/14.webp)


## Pengaturan keamanan


Pada tahap ini:


1. Windows Defender dapat diaktifkan atau dinonaktifkan. Fitur ini berfungsi seperti perangkat lunak keamanan di Windows dan membantu mencegah eksekusi file berbahaya, serangan jaringan tertentu, dan banyak lagi.

2. Pembaruan Windows otomatis dapat dinonaktifkan. Ini adalah salah satu tantangan umum yang dihadapi oleh pengguna Windows!

3. Bagian ini memungkinkan untuk mengaktifkan atau menonaktifkan UAC (Kontrol Akun Pengguna). Fitur ini mencegah aplikasi yang mencurigakan agar tidak berjalan dengan izin yang lebih tinggi untuk membaca dan menulis.

4. Fitur ini digunakan oleh Windows untuk mendeteksi perangkat lunak yang berpotensi berbahaya.

5. Mengaktifkan atau menonaktifkan dukungan untuk jalur panjang dalam aplikasi Windows, seperti PowerShell dan lainnya.

6. Mengaktifkan atau menonaktifkan Remote Desktop untuk mengakses sistem dari jarak jauh.


Tergantung pada versi Windows yang digunakan, beberapa fitur ini mungkin didukung atau tidak didukung.


Langkah berikutnya adalah mengonfigurasi ikon:


![Image](assets/en/15.webp)


Di bagian ini:


1. Ikon desktop terdaftar, yang dapat ditambahkan atau dihapus sesuai kebutuhan.

2. Ikon menu mulai terdaftar, yang juga dapat ditambahkan atau dihapus berdasarkan kebutuhan.

3. Bagian ini memungkinkan untuk mengonfigurasi apakah alat yang terkait dengan virtualisasi diinstal atau tidak. Opsi ini khusus untuk Windows 11 dan tidak berlaku untuk Windows 10.


Langkah berikutnya adalah mengonfigurasi pengaturan Wi-Fi:


![Image](assets/en/16.webp)


Pada bagian ini, pengaturan jaringan Wi-Fi dapat dikonfigurasi. Seperti yang disebutkan sebelumnya, pada sebagian besar kasus, kartu Wi-Fi tidak dikenali sewaktu penginstalan Windows, jadi menghubungkan selama penyiapan biasanya tidak memungkinkan. Namun demikian, dengan mengonfigurasi bagian ini, jika kartu nirkabel terdeteksi, sistem dapat terhubung ke internet.


Langkah berikutnya melibatkan pengaturan yang penting:


![Image](assets/en/17.webp)


Pada bagian ini, kami menentukan apakah informasi masalah sistem harus dikirim ke Microsoft atau tidak.


Langkah berikutnya adalah mengonfigurasi aplikasi default:


![Image](assets/en/18.webp)


## Mengaktifkan/menonaktifkan perangkat lunak default


Pada bagian ini, kita bisa memilih aplikasi apa saja yang tidak ingin diinstal secara default. Sebagai contoh, kita bisa memilih untuk tidak menginstal Cortana atau Copilot.


Langkah berikutnya melibatkan pengaturan keamanan yang terkait dengan eksekusi aplikasi:


![Image](assets/en/19.webp)


Dengan menerapkan pengaturan WDAC, eksekusi aplikasi tertentu dapat dicegah.


Terakhir, setelah menerapkan pengaturan yang diinginkan, file XML yang dihasilkan dapat diunduh:


![Image](assets/en/20.webp)


Dengan mengeklik Download XML File, file autounattend.xml akan diunduh. Untuk menggunakan file ini, cukup pasang ISO yang telah diunduh pada drive USB, letakkan file autounattend.xml di direktori root, lalu lanjutkan dengan penginstalan Windows.


Salah satu alat yang tersedia untuk membuat drive USB yang dapat di-boot adalah Rufus. Rufus dapat membuat flash drive instalasi Windows yang dapat di-booting, dengan file ISO instalasi Windows yang diberikan. Cepat dan sederhana, Anda dapat mengunduhnya [di sini](https://rufus.ie/en/#download)


![Image](assets/en/21.webp)


Dalam perangkat lunak ini, setelah memilih drive USB yang diinginkan dan file ISO yang sesuai, kita klik Start.


![Image](assets/en/22.webp)


Pada tahap ini, kami menonaktifkan semua opsi, karena jika diaktifkan dapat menyebabkan konflik saat menggunakan file Unattend yang dihasilkan. Setelah file disalin ke drive USB, kita tempatkan file autounattend.xml di direktori root:


![Image](assets/en/23.webp)


Pada titik ini, drive USB siap digunakan untuk menginstal Windows secara otomatis, dan penginstalan dapat dimulai dengan menggunakan drive ini.


## Pengeditan ISO


Jika Anda perlu menginstal Windows pada mesin virtual, Anda dapat menggunakan perangkat lunak untuk membuat dan mengedit file ISO. Salah satu perangkat lunak tersebut adalah AnyBurn. Setelah mengekstrak konten file ISO yang diunduh dari situs web Microsoft, letakkan file autounattend.xml di direktori root. Kemudian, dengan menggunakan AnyBurn, buatlah ISO baru dengan konten yang telah diperbarui.


AnyBurn adalah perangkat lunak multifungsi untuk bekerja dengan file ISO. Menawarkan berbagai fitur untuk menangani file ISO, salah satunya adalah membuat gambar ISO yang dapat di-boot; [di sini](https://www.anyburn.com/download.php) adalah situs web aslinya.


Pada halaman utama perangkat lunak, pilih "Buat Gambar dari File/Folder":


![Image](assets/en/24.webp)


Pada halaman berikutnya, pilih semua file yang diekstrak dari ISO bersama dengan file autounattend.xml.


![Image](assets/en/25.webp)


Pada langkah ini, kami mengonfigurasi pengaturan untuk membuat file ISO dapat di-boot:


![Image](assets/en/26.webp)


Pada tahap ini, jalur ke file bootfix.bin harus diatur agar ISO dapat di-boot. File ini terletak di root ISO, di dalam folder boot. Juga disarankan untuk mengaktifkan opsi ISO9660 dan UDF di bagian Properties.


![Image](assets/en/27.webp)


Setelah langkah ini, klik Berikutnya akan membuat file ISO. File ini dapat digunakan dalam perangkat lunak virtualisasi seperti Oracle VirtualBox. Di bawah ini Anda akan menemukan tutorial tentang VirtualBox:


https://planb.academy/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65