---
name: VirtualBox
description: Instal VirtualBox pada Windows 11 dan buat VM pertama Anda
---
![cover](assets/cover.webp)



___



*Tutorial ini didasarkan pada konten asli oleh Florian Burnel yang dipublikasikan di [IT-Connect](https://www.it-connect.fr/). Lisensi [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Perubahan mungkin telah dilakukan pada teks asli.*



___




## I. Presentasi



Dalam tutorial ini, kita akan mempelajari cara menginstal VirtualBox pada Windows 11 untuk membuat mesin virtual, baik untuk menjalankan Windows 10, Windows 11, Windows Server, atau distribusi Linux (Debian, Ubuntu, Kali Linux, dll.).



Tutorial pengenalan VirtualBox ini akan membantu Anda memulai dengan solusi virtualisasi sumber terbuka yang dikembangkan oleh Oracle, yang sepenuhnya gratis. Nantinya, tutorial lain akan tersedia secara online untuk membawa Anda lebih dalam ke dalam subjek ini.



Ketika berbicara tentang virtualisasi workstation, baik untuk tujuan pengujian sebagai bagian dari proyek atau selama studi TI Anda, VirtualBox jelas merupakan solusi yang baik. Ini juga merupakan alternatif untuk solusi lain seperti Hyper-V, yang terintegrasi ke dalam Windows 10 dan Windows 11 (serta Windows Server), dan VMware Workstation (berbayar)/VMware Workstation Player (gratis untuk penggunaan pribadi).



Konfigurasi saya: **stasiun kerja Windows 11 di mana saya akan menginstal VirtualBox**, tetapi Anda bisa menginstal VirtualBox di Windows 10 (atau versi yang lebih lama), dan juga di Linux. Sejauh menyangkut mesin virtual, VirtualBox mendukung berbagai macam sistem, termasuk Windows (mis. Windows 10, Windows 11, Windows Server 2022, dll.), Linux (Debian, Rocky Linux, Ubuntu, Fedora, dll.), BSD (PfSense), dan macOS.



## II. Unduh VirtualBox untuk Windows 11



Untuk mengunduh VirtualBox untuk instalasi pada mesin Windows, hanya ada satu Address yang bagus: [situs web resmi VirtualBox](https://www.virtualbox.org/wiki/Downloads) di bagian "**Downloads**". Cukup klik "Windows hosts" untuk mulai mengunduh file yang dapat dieksekusi, yang berukuran lebih dari 100 MB.



![Image](assets/fr/025.webp)



## III. Menginstal VirtualBox pada Windows 11



### A. Menginstal VirtualBox



Menginstalasi VirtualBox** sangat mudah, dan prosesnya sama untuk semua versi Windows. Mulailah dengan meluncurkan file executable VirtualBox yang baru saja Anda unduh, lalu klik "**Next**".



![Image](assets/fr/026.webp)



Instalasi ini dapat disesuaikan, tetapi saya sarankan agar Anda menginstal semua fitur: yang merupakan pilihan default. Pada gambar di bawah ini, Anda dapat melihat berbagai Elements, termasuk:





- Dukungan USB VirtualBox** untuk memungkinkan VirtualBox mendukung perangkat USB
- VirtualBox Bridged Network** untuk mengintegrasikan dukungan jaringan dalam mode "Bridge" (mesin virtual dapat terhubung langsung ke jaringan lokal Anda)
- VirtualBox Host-Only Network ** untuk mengintegrasikan dukungan jaringan dalam mode "Host-Only" (mesin virtual hanya dapat berkomunikasi dengan host fisik Windows 11 Anda dan mesin virtual lainnya dalam mode ini)



Klik "**Selanjutnya**" untuk melanjutkan.



![Image](assets/fr/001.webp)



Klik "**Ya**", dengan mengingat bahwa **jaringan akan terputus sejenak pada mesin Windows 11 Anda**, sementara VirtualBox melakukan modifikasi jaringan untuk mendukung jenis jaringan yang berbeda, termasuk mode Bridge.



![Image](assets/fr/002.webp)



Setelah Anda mengonfirmasi, penginstalan akan dimulai... Dan notifikasi "**Apakah Anda ingin menginstal perangkat lunak perangkat ini?**" akan muncul. Centang opsi "**Selalu percayai perangkat lunak dari Oracle Corporation**" dan klik "**Instal**". VirtualBox sebenarnya perlu menginstal beberapa driver di komputer Anda.



![Image](assets/fr/003.webp)



Penginstalan sekarang sudah selesai! Centang opsi "**Mulai Oracle VM VirtualBox 6.1.34 setelah instalasi**" dan klik "**Klik**" untuk meluncurkan perangkat lunak.



![Image](assets/fr/004.webp)



### B. Menambahkan paket ekstensi



Masih di situs resmi VirtualBox (lihat tautan sebelumnya), Anda dapat mengunduh paket ekstensi resmi, yang dapat diakses di bagian "**VirtualBox 6.1.34 Oracle VM VirtualBox Extension Pack**" dengan mengeklik tautan "**Semua platform yang didukung**". Paket ini akan memungkinkan Anda untuk menambahkan fungsi tambahan ke VirtualBox: tidak wajib untuk menambahkannya, tetapi dapat berguna! Sebagai contoh, paket ini mencakup dukungan untuk USB 3.0 pada VM, dukungan webcam, dan enkripsi disk.



Buka VirtualBox, klik "**File**" dan kemudian "**Settings**" pada menu.



![Image](assets/fr/005.webp)



Klik "**Ekstensi**" di sebelah kiri (1), lalu pada tombol "**+**" di sebelah kanan (2) untuk **memuat paket ekstensi VirtualBox** yang baru saja Anda unduh (3).



![Image](assets/fr/006.webp)



Konfirmasikan dengan mengeklik tombol "**Penginstalan**".



![Image](assets/fr/007.webp)



Klik "**OK**": paket ekstensi resmi sekarang terinstal pada instance VirtualBox Anda!



![Image](assets/fr/008.webp)



Mari kita lanjutkan ke pembuatan mesin virtual pertama kita.



## IV. Membuat VM VirtualBox pertama Anda



Untuk membuat mesin virtual baru di VirtualBox, cukup klik tombol "**New**" untuk meluncurkan wizard pembuatan VM. Karena ini adalah pertama kalinya Anda menjalankan VirtualBox, saya ingin memberikan beberapa detail lebih lanjut tentang Interface dan tombol-tombol lainnya.





- Pengaturan**: konfigurasi VirtualBox umum (folder VM default, manajemen pembaruan, bahasa, jaringan NAT, ekstensi, dll.)
- Impor**: mengimpor alat virtual dalam format OVF
- Ekspor**: mengekspor mesin virtual yang sudah ada dalam format OVF untuk membuat alat virtual
- Tambah **: tambahkan mesin virtual yang ada ke inventaris VirtualBox Anda, dalam format VirtualBox standar (.vbox) atau format XML



Di sebelah kiri, bagian "**Tools**" memberikan akses ke **fungsi lanjutan, terutama untuk mengelola jaringan virtual, tetapi juga untuk mengelola penyimpanan VM**. Di bawah entri "**Tools**", mesin virtual Anda akan ditambahkan nanti.



![Image](assets/fr/009.webp)



### A. Proses pembuatan VM



**Sebagai pengingat, VirtualBox mendukung banyak sistem operasi, termasuk Windows, Linux, dan BSD. Dalam contoh ini, saya akan membuat mesin virtual untuk Windows 11. Beberapa bidang perlu diisi:





- Name**: nama mesin virtual (ini adalah nama yang akan ditampilkan di VirtualBox)
- Folder mesin**: tempat menyimpan mesin virtual, dengan mengetahui bahwa subfolder dengan nama VM akan dibuat di lokasi ini
- Jenis**: jenis sistem operasi, tergantung pada OS yang ingin Anda instal
- Versi**: versi sistem yang ingin Anda instal, dalam hal ini Windows 11, jadi "**Windows11_64**"



Klik "**Selanjutnya**" untuk melanjutkan.



![Image](assets/fr/010.webp)



Bergantung pada sistem operasi yang Anda pilih pada langkah sebelumnya, **VirtualBox membuat rekomendasi sumber daya yang akan dialokasikan ke mesin virtual**. Di sini, kita berbicara tentang RAM yang ingin Anda alokasikan ke VM. Anggap saja 4 GB, karena ini memang direkomendasikan untuk Windows 11, tetapi jika Anda kekurangan sumber daya, tentukan 2 GB sebagai gantinya. ** Lanjutkan



**Catatan**: sumber daya yang dialokasikan ke mesin virtual dapat dimodifikasi nanti.



![Image](assets/fr/011.webp)



Untuk disk Hard virtual, kita mulai dari awal, jadi kita harus memilih "**Buat disk Hard virtual sekarang**" agar VM memiliki ruang penyimpanan untuk menginstal sistem operasi dan menyimpan data. Klik "**Buat**".



![Image](assets/fr/012.webp)



VirtualBox mendukung tiga format berbeda untuk disk Hard virtual, yang merupakan perbedaan utama dibandingkan dengan solusi lain seperti VMware dan Hyper-V. Ada tiga format yang dapat dipilih:





- VDI**, format resmi VirtualBox
- VHD**, yang merupakan format resmi Hyper-V, meskipun format VHDX baru lebih sering digunakan akhir-akhir ini
- VMDX** adalah format resmi VMware untuk VMware Workstation dan VMware ESXi



Untuk membuat mesin virtual yang hanya akan digunakan pada instance VirtualBox ini, pilih "**VDI**". Di sisi lain, jika disk Hard virtual akan dipasang ke host Hyper-V di kemudian hari, sebaiknya mulai dengan format VHD agar tidak perlu mengonversinya. Klik "**Next**".



![Image](assets/fr/013.webp)



**Disk virtual dapat berukuran dinamis atau tetap**. Bila dinamis, file yang mewakili **disk virtual (di sini file .vdi) akan bertambah saat data ditulis ke disk** hingga mencapai ukuran maksimumnya, tetapi tidak akan menyusut jika data dihapus. Sebaliknya, ketika ukurannya tetap, **ruang penyimpanan total dialokasikan dengan segera (dan karena itu dicadangkan)**, yang memungkinkan kinerja yang sedikit lebih tinggi, tetapi membutuhkan waktu lebih lama ketika disk virtual pertama kali dibuat.



Secara pribadi, untuk mesin virtual uji coba dengan VirtualBox, saya menganggap mode "**Dynamically allocated**" sudah cukup memadai.



![Image](assets/fr/014.webp)



**Langkah selanjutnya adalah menentukan ukuran disk virtual**, dengan mengingat bahwa secara default, disk akan disimpan di direktori VM (ini dapat diubah pada tahap ini). Saya telah menunjukkan ukuran 64 GB untuk memenuhi persyaratan Windows 11, tetapi di sini sekali lagi, ukuran yang lebih kecil dapat ditetapkan. Klik "**Buat**" untuk membuat VM!



![Image](assets/fr/015.webp)



Pada titik ini, VM sudah ada di inventaris kita, sudah dikonfigurasi, tetapi sistem operasi belum diinstal. Kita perlu menyelesaikan konfigurasi VM sebelum memulainya.



### B. Menetapkan citra ISO ke VM VirtualBox



Untuk menginstal Windows 11, atau sistem lainnya, kita memerlukan sumber instalasi. Pada umumnya, kami menggunakan citra disk dalam format ISO untuk menginstal sistem operasi. **Anda perlu memuat citra ISO Windows 11 ke dalam drive DVD virtual VM kami



Klik pada VM di inventaris VirtualBox (1), lalu pada tombol "**Konfigurasi**" (2), yang memberikan akses ke konfigurasi umum mesin virtual ini. Menu ini digunakan untuk mengelola sumber daya (misalnya, menambah RAM, mengonfigurasi CPU, dll.). Klik "**Penyimpanan**" di sebelah kiri (3), pada drive DVD yang bertuliskan "**Kosong**" untuk saat ini (4), lalu klik ikon berbentuk DVD (5) dan "**Pilih file disk**".



![Image](assets/fr/016.webp)



Pilih image ISO dari sistem operasi yang ingin Anda instal, lalu klik OK. Inilah yang saya dapatkan:



![Image](assets/fr/017.webp)



Tetap di bagian "**Konfigurasi**" pada VM, saya masih memiliki beberapa hal untuk dijelaskan.



### C. Koneksi jaringan VM



Buka bagian "**Jaringan**" di sebelah kiri. Bagian ini memungkinkan Anda mengelola jaringan mesin virtual: jumlah antarmuka jaringan virtual (hingga 4 per VM), MAC Address, dan mode akses jaringan (NAT, akses jembatan, jaringan internal, dll.). **Jika Anda ingin mesin virtual memiliki akses ke Internet, pilih "NAT" atau "Bridge Access "**, tetapi mode kedua ini memerlukan server DHCP untuk aktif di jaringan Anda, atau Anda harus mengonfigurasi IP Address secara manual.



Catatan: Saya akan kembali ke bagian jaringan secara lebih rinci dalam artikel khusus.



![Image](assets/fr/018.webp)



### D. Jumlah prosesor virtual



Seperti halnya komputer fisik, mesin virtual membutuhkan RAM, disk Hard, dan prosesor agar dapat berfungsi. Ketika kami membuat VM, Anda mungkin telah memperhatikan bahwa wizard tidak menyertakan konfigurasi prosesor. Namun, hal ini dapat dikonfigurasi kapan saja melalui tab "**System**", lalu "**Processor**", di mana Anda dapat memilih jumlah prosesor virtual.



Catatan: opsi "**Aktifkan VT-x/AMD-v bersarang**" diperlukan untuk virtualisasi bersarang.



Dalam kasus saya, mesin virtual memiliki 2 prosesor virtual:



![Image](assets/fr/019.webp)



**Jangan ragu untuk melihat bagian lain dari menu konfigurasi.



### E. Booting pertama dan penginstalan OS



Untuk memulai mesin virtual, cukup pilih mesin tersebut di inventaris dan klik tombol "**Mulai**". Jendela kedua akan terbuka, memberikan gambaran umum visual VM.



![Image](assets/fr/020.webp)



Aduh, saya mendapatkan kesalahan yang buruk dan mesin virtual saya tidak mau mulai! Kesalahannya adalah "Login gagal untuk mesin virtual..." dengan rincian sebagai berikut:



```shell
Not in a hypervisor partition (HPV=0)
AMD-V is disabled in the BIOS (or by the host OS)
```



Sebenarnya, hal ini normal karena **fitur virtualisasi tidak diaktifkan pada komputer saya**! Untuk memperbaiki masalah ini, Anda perlu menyalakan ulang komputer untuk mengakses BIOS dan mengaktifkan virtualisasi.



![Image](assets/fr/021.webp)



Tanpa menunggu, saya menyalakan ulang komputer saya dan **menekan tombol "SUPPR" untuk mengakses BIOS** (tombolnya bisa berbeda-beda, tergantung pada mesinnya, dan bisa jadi F2, misalnya) pada motherboard ASUS saya. Untuk mengaktifkan virtualisasi, "Mode SVM" harus diaktifkan dalam kasus saya. Di sini sekali lagi, dari satu motherboard ke motherboard lainnya, dari satu produsen ke produsen lainnya, namanya bisa berubah. Carilah fungsi yang mengacu pada **AMD-V** (untuk CPU AMD) atau **Intel VT-x** (untuk CPU Intel).



![Image](assets/fr/022.webp)



Setelah selesai, simpan modifikasi dan mulai ulang mesin fisik... Kali ini, **VirtualBox dapat memulai mesin virtual** dan memuat citra ISO Windows untuk menginstal sistem operasi 🙂



![Image](assets/fr/023.webp)



Pada host fisik Windows 11, tempat VirtualBox diinstal, kita dapat melihat bahwa folder mesin virtual Windows 11 berisi berbagai file.





- File VBOX** (dalam format XML) yang sesuai dengan konfigurasi VM (RAM, CPU, dll.)
- File VBOX-PREV ** adalah cadangan dari konfigurasi sebelumnya
- File VDI ** sesuai dengan disk Hard virtual dalam mode dinamis, sehingga saat ini hanya 13 GB, sedangkan ukuran maksimumnya adalah 64 GB
- File NVRAM ** berisi status BIOS dari mesin virtual, yang setara dengan memori non-volatile dari mesin fisik



![Image](assets/fr/024.webp)



## V. Kesimpulan



**VirtualBox sekarang sudah aktif dan berjalan di mesin fisik Windows 11 kami! Yang tersisa hanyalah memanfaatkannya dan membuat mesin virtual!** Saya akan kembali membahas penginstalan Windows 11 di VM VirtualBox di artikel lain. Untuk Windows 10, Windows Server, atau distribusi Linux (Ubuntu, Debian, dll.), biarkan kami memandu Anda!