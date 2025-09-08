---
name: Fedora
description: Distribusi Linux yang menyediakan ruang kerja gratis, lengkap, dan aman bagi Anda.
---


![cover](assets/cover.webp)





Fedora adalah sistem operasi berbasis Linux sumber terbuka gratis yang diluncurkan pada tahun 2003, dikembangkan oleh komunitas **Fedora Project** dan didukung oleh **Red Hat Linux**. Fedora terkenal dengan stabilitas, kinerja yang baik, dan kemudahan penggunaannya, menjadikannya pilihan yang sangat baik untuk pemula dan pengguna tingkat lanjut. Sistem ini berjalan pada sebagian besar arsitektur prosesor modern, membuatnya mudah dipasang pada hampir semua komputer. Fedora juga tersedia dalam beberapa edisi yang telah dikonfigurasi sebelumnya, yang disebut "Fedora Spins" atau "Edisi Fedora", yang dirancang untuk kebutuhan khusus (video game, astronomi, pengembangan...).



## Arsitektur Linux Fedora



Seperti yang Anda baca sebelumnya, Fedora adalah sistem operasi gratis yang berbasis kernel Linux. Kernel Linux adalah bagian dari sistem operasi yang berkomunikasi dengan perangkat keras komputer dan mengelola sumber daya sistem seperti memori dan daya pemrosesan.



Fedora Linux menyertakan berbagai alat perangkat lunak dan aplikasi yang diperlukan untuk menjalankan sistem operasi di atas kernel Linux. Arsitektur modular Fedora berarti bahwa Fedora sebagian besar terdiri dari kumpulan komponen individual yang dapat dengan mudah ditambahkan, dihapus, atau diganti sesuai kebutuhan. Hal ini memungkinkan Anda untuk membentuk sistem operasi hanya dengan menggunakan sumber daya yang Anda butuhkan.



Fedora juga menyertakan lingkungan desktop, yang merupakan Interface yang digunakan pengguna untuk melakukan tugas dan mengakses aplikasi. Lingkungan desktop default Fedora adalah GNOME, lingkungan desktop yang ramah pengguna, mudah digunakan, dan sangat mudah dikustomisasi.



## Mengapa memilih Fedora?



Di antara sekian banyak distribusi Linux yang tersedia, Fedora menonjol khususnya untuk distribusi:





- Modularitas**: Kompatibel dengan arsitektur prosesor yang berbeda, Fedora dapat diinstal pada sebagian besar komputer, bahkan komputer dengan daya rendah, beradaptasi dengan sempurna dengan kebutuhan Anda.





- Interface yang sederhana dan intuitif**: Fedora menggabungkan Interface grafis modern dengan Interface baris perintah yang kuat, membuatnya mudah digunakan untuk semua profil.





- Stabilitas Kernel**: Berbasis Red Hat, Fedora terkenal dengan keandalan pembaruannya, terutama pembaruan kernel, yang dilakukan tanpa bug besar berkat kontribusi gratis dari komunitas yang besar.





- Instalasi cepat dan mudah**: dengan ukuran gambar hanya 3 GB, instalasi menjadi cepat dan mudah, bahkan pada mesin dengan sumber daya yang terbatas.



## Edisi Fedora



Bergantung pada profil dan penggunaan Anda, Fedora menawarkan edisi yang sesuai dengan kebutuhan Anda. Anda terutama akan menemukan:





- Fedora Workstation**: Ideal untuk penggunaan pribadi dan/atau profesional pada komputer Anda, edisi ini diinstal dengan utilitas umum seperti peramban, office suite (editor teks), dan perangkat lunak pemutaran media.





- Server Fedora**: Edisi ini didedikasikan untuk manajemen server. Fedora Server menyertakan berbagai alat untuk membantu Anda menggunakan dan mengelola server dalam skala Anda sendiri.





- Fedora CoreOS**: Ingin menjalankan dan menggunakan aplikasi cloud dengan mudah? Fedora CoreOS adalah edisi yang memberi Anda alat untuk membuat dan mengelola image dengan Docker dan Kubernet, misalnya.



Dalam tutorial ini, kita akan membahas edisi Fedora Workstation. Namun, proses yang dijelaskan di bawah ini serupa untuk edisi lainnya.



## Menginstalasi dan mengonfigurasi Fedora Workstation



Menginstalasi Fedora Workstation membutuhkan konfigurasi perangkat keras berikut ini:




- Kunci USB minimal **8 GB** untuk mem-boot sistem operasi.
- Setidaknya **40 GB ruang kosong** pada disk Hard komputer Anda.
- rAM 4 GB** untuk pengalaman yang lancar.



### Unduh Fedora Workstation



Anda dapat mengunduh edisi [Fedora Workstation] (https://fedoraproject.org/fr/workstation/download) dari situs web resmi proyek Fedora. Kemudian pilih versi yang sesuai dengan arsitektur prosesor Anda (32-bit - 64-bit) dan klik ikon **Download**.



![download](assets/fr/01.webp)



![telecharger](assets/fr/02.webp)


### Membuat kunci USB yang dapat di-boot



Untuk menginstal Fedora, Anda perlu membuat kunci USB yang dapat di-boot menggunakan perangkat lunak seperti [Balena Etcher](https://etcher.balena.io/).



![flashOs](assets/fr/03.webp)



![flash](assets/fr/04.webp)



Setelah Anda selesai menginstal Balena Etcher, buka aplikasi dan pilih citra ISO Fedora Workspace yang telah diunduh. Pilih kunci USB Anda sebagai media tujuan dan klik tombol **Flash** untuk mulai membuat kunci yang dapat di-boot.



![boot](assets/fr/05.webp)


### Menginstal Fedora



Setelah Anda selesai mem-boot kunci USB, matikan komputer Anda.


Hidupkan komputer Anda, lalu akses BIOS selama pengaktifan dengan menekan tombol `F2`, `F12`, atau `ESC`, tergantung komputer Anda.



Pada pilihan boot, pilih kunci USB Anda sebagai perangkat boot utama. Dengan mengonfirmasi pilihan ini, komputer Anda akan memulai ulang dan secara otomatis menjalankan pemasang Fedora** yang ada pada kunci USB.



Setelah komputer Anda melakukan booting dari stik USB, layar **GRUB** akan muncul.



Pada tahap ini, Anda memiliki opsi berikut:




- Media uji**: Opsi ini memungkinkan Anda memeriksa integritas stik USB dan memastikan bahwa semua dependensi yang diperlukan untuk instalasi yang benar sudah ada. Ini adalah langkah opsional, tetapi disarankan jika Anda ragu dengan stik USB.



![install](assets/fr/06.webp)



![testing](assets/fr/07.webp)





- Mulai Fedora**: Ini meluncurkan Fedora dalam mode "langsung", tanpa instalasi.



Pada desktop Fedora (mode langsung), klik **Instal Fedora** (atau Instal pada disk Hard) untuk memulai proses instalasi. Anda dapat memilih untuk menginstal nanti dan menguji Fedora tanpa harus menginstalnya.



![install-live](assets/fr/08.webp)



Langkah pertama adalah memilih **bahasa instalasi** dan **tata letak keyboard** Fedora



![language](assets/fr/10.webp)





- Memilih disk instalasi:



Pilih disk Hard tempat Anda ingin menginstal Fedora.



Jika disk kosong, Fedora akan secara otomatis menggunakan semua ruang yang tersedia. Jika tidak, Anda dapat menyesuaikan partisi (manual atau otomatis).



![disk](assets/fr/11.webp)





- Enkripsi:



Pada tahap ini, Fedora menyarankan untuk mengenkripsi disk Anda untuk menambahkan keamanan ekstra Layer. Ini memastikan bahwa data Anda hanya dapat dibaca oleh sistem Fedora Anda.



![chiffrement](assets/fr/12.webp)



Sebelum meluncurkan instalasi, Fedora menampilkan ringkasan pilihan Anda. Konfirmasikan dan klik pada tombol instal untuk memulai instalasi Fedora.



![resume](assets/fr/13.webp)



Selama instalasi, Fedora menyalin file dan mengonfigurasi sistem. Setelah selesai, komputer akan melakukan boot ulang secara otomatis.



![installation](assets/fr/14.webp)



### Konfigurasi dasar


Pada penggunaan pertama kali, Anda harus menyelesaikan beberapa pengaturan:




- Ubah bahasa sistem jika perlu.



![language](assets/fr/15.webp)





- Pilih tata letak keyboard yang sesuai dengan preferensi Anda.



![keyboard](assets/fr/16.webp)





- Pilih zona waktu Anda dengan mengetikkan nama kota Anda di bilah pencarian, lalu klik saran yang sesuai.



![timezone](assets/fr/17.webp)





 - Mengaktifkan atau menonaktifkan akses ke posisi Anda untuk aplikasi yang membutuhkannya, serta pengiriman laporan bug secara otomatis.



![location](assets/fr/18.webp)





- Tentukan apakah Anda ingin mengaktifkan repositori perangkat lunak pihak ketiga.



![logs](assets/fr/19.webp)





- Masukkan nama lengkap Anda dan tentukan nama pengguna untuk akun Anda.



![name](assets/fr/20.webp)





- Buat kata sandi yang aman untuk sesi Anda: sepanjang mungkin (minimal 20 karakter), seacak mungkin, dan dengan berbagai karakter (huruf kecil, huruf besar, angka, dan simbol). Ingatlah untuk menyimpan kata sandi Anda.



![mdp](assets/fr/21.webp)



Setelah semua langkah ini selesai, luncurkan Fedora dan segera mulai menggunakannya, tanpa perlu reboot.



![welcome](assets/fr/22.webp)



![start](assets/fr/23.webp)



Setelah instalasi Anda selesai, Anda dapat berkonsultasi dengan rumah Interface Anda dengan beberapa utilitas yang sudah terpasang.



![install-now](assets/fr/09.webp)



## Temukan tugas-tugas dasar



### Menjelajahi Internet


Peramban bawaan Fedora adalah **Firefox**. Browser ini mudah digunakan dan cocok untuk sebagian besar kebutuhan.


Jika Anda lebih suka browser lain, Anda dapat menginstalnya dari **manajer perangkat lunak** atau melalui **terminal**.


### Pengolah kata


Fedora menyertakan paket perkantoran **LibreOffice** secara default, yang menawarkan beberapa alat yang berguna:




- Writer** untuk pengolah kata.
- Calc** untuk spreadsheet.
- Impress** untuk membuat presentasi.


## Menginstal aplikasi


Untuk menginstal aplikasi baru, Anda dapat menggunakan **manajer perangkat lunak** Fedora (disebut _Software_), yang membuat instalasi menjadi mudah dan visual.  Namun, menggunakan **terminal** sering kali lebih cepat dan akurat.



Sebelum menginstal perangkat lunak apa pun, selalu ingat untuk memperbarui **repositori** untuk memastikan Anda memiliki akses ke versi terbaru yang tersedia.



Kemudian gunakan perintah berikut ini untuk meluncurkan penginstalan aplikasi yang diinginkan:


sudo dnf instal nama_perangkat_lunak`


## Memperbarui sistem operasi Anda


Setelah instalasi, penting untuk memperbarui Fedora untuk mengambil keuntungan dari patch keamanan dan pembaruan perangkat lunak terbaru.


### Opsi 1: Melalui grafik Interface




- Buka **Pengaturan** Fedora, lalu buka bagian **Sistem**.
- Klik **Pembaruan perangkat lunak**.
- Mulailah mengunduh pembaruan dan tunggu hingga prosesnya selesai.



Pengaktifan ulang **restart** mungkin diperlukan setelah pembaruan diinstal.


### Opsi 2: Melalui terminal




- Buka terminal dan mulailah dengan memperbarui **repositori** untuk memastikan Anda memiliki versi terbaru dari:



```shell
sudo dnf check-update
```





- Selanjutnya, perbarui semua perangkat lunak yang terinstal dengan perintah berikut:



```shell
sudo dnf upgrade
```



Sekarang sistem Fedora Anda sudah mutakhir dan siap digunakan untuk semua tugas sehari-hari. Temukan tutorial kami tentang Linux Mint, distribusi Linux lainnya, dan cara menyiapkan lingkungan yang sehat dan aman untuk transaksi Bitcoin Anda.



https://planb.network/tutorials/computer-security/operating-system/linux-mint-da44852e-513f-4004-949a-8fde60c1bca5