---
name: VirtualBox
description: Instal VirtualBox pada Windows 11 dan buat VM pertama Anda
---
![cover](assets/cover.webp)

___

*Tutorial ini didasarkan pada konten asli oleh Florian Burnel yang dipublikasikan di [IT-Connect](https://www.it-connect.fr/). Lisensi [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Perubahan mungkin telah dilakukan pada teks asli.*

___

## I. Presentasi

Dalam tutorial ini, kita akan mempelajari cara memasang VirtualBox di Windows 11 untuk membuat virtual machines, baik untuk menjalankan Windows 10, Windows 11, Windows Server, atau distribusi Linux (Debian, Ubuntu, Kali Linux, dll.).

Tutorial pengantar VirtualBox ini akan membantu Anda memulai solusi virtualisasi open source yang dikembangkan oleh Oracle ini, yang sepenuhnya gratis. Nantinya, tutorial lain akan diunggah secara online untuk membawa Anda lebih dalam ke subjek ini.

Ketika berbicara tentang virtualisasi workstation, baik untuk tujuan pengujian sebagai bagian dari proyek atau selama studi TI Anda, VirtualBox jelas merupakan solusi yang baik. Ini juga merupakan alternatif dari solusi lain seperti Hyper-V, yang terintegrasi ke dalam Windows 10 dan Windows 11 (serta Windows Server), dan VMware Workstation (berbayar) / VMware Workstation Player (gratis untuk penggunaan pribadi).

Konfigurasi saya: **workstation Windows 11 tempat saya akan memasang VirtualBox**, tetapi Anda dapat memasang VirtualBox di Windows 10 (atau versi yang lebih lama), serta di Linux. Adapun virtual machine, VirtualBox mendukung berbagai sistem, termasuk Windows (misalnya Windows 10, Windows 11, Windows Server 2022, dll.), Linux (Debian, Rocky Linux, Ubuntu, Fedora, dll.), BSD (PfSense), dan macOS.

## II. Unduh VirtualBox untuk Windows 11

Untuk mengunduh VirtualBox untuk instalasi pada komputer Windows, hanya ada satu website yang benar: [situs web resmi VirtualBox](https://www.virtualbox.org/wiki/Downloads) di bagian "**Downloads**". Cukup klik "Windows hosts" untuk mulai mengunduh file yang dapat dieksekusi, yang berukuran lebih dari 100 MB.

![Image](assets/fr/025.webp)

## III. Menginstal VirtualBox pada Windows 11

### A. Menginstal VirtualBox

**Menginstalasi VirtualBox** sangat mudah, dan prosesnya sama untuk semua versi Windows. Mulailah dengan meluncurkan file executable VirtualBox yang baru saja Anda unduh, lalu klik "**Next**".

![Image](assets/fr/026.webp)

Instalasi ini dapat disesuaikan, tetapi saya sarankan agar Anda menginstal semua fitur: yang merupakan pilihan default. Pada gambar di bawah ini, Anda dapat melihat berbagai Elements, termasuk :

- **Dukungan USB VirtualBox** untuk memungkinkan VirtualBox mendukung perangkat USB
- **VirtualBox Bridged Network** untuk mengintegrasikan dukungan jaringan dalam mode "Bridge" (virtual machine dapat terhubung langsung ke jaringan lokal Anda)
- **VirtualBox Host-Only Network** untuk mengintegrasikan dukungan jaringan dalam mode "Host-Only" (virtual machine hanya dapat berkomunikasi dengan host fisik Windows 11 Anda dan virtual machine lainnya dalam mode ini)

Klik "**Next**" untuk melanjutkan.

![Image](assets/fr/001.webp)

Klik "**Yes**", dengan mengingat bahwa **jaringan akan terputus sejenak pada mesin Windows 11 Anda**, sementara VirtualBox melakukan modifikasi jaringan untuk mendukung berbagai jenis jaringan, termasuk mode Bridge.

![Image](assets/fr/002.webp)

Setelah Anda mengonfirmasi, instalasi akan dimulai... Dan notifikasi "**Do you want to install this device software?**" akan muncul. Centang opsi "**Always trust software from Oracle Corporation**" dan klik "**Install**". VirtualBox sebenarnya perlu memasang beberapa driver pada komputer Anda.

![Image](assets/fr/003.webp)

Instalasi sekarang selesai! Centang opsi "**Start Oracle VM VirtualBox 6.1.34 after installation**" dan klik "**Finish**" untuk meluncurkan perangkat lunak.

![Image](assets/fr/004.webp)

### B. Menambahkan paket ekstensi

Masih di situs resmi VirtualBox (lihat tautan sebelumnya), Anda dapat mengunduh extension pack resmi, yang dapat diakses di bawah bagian "**VirtualBox 6.1.34 Oracle VM VirtualBox Extension Pack**" dengan mengklik tautan "**All supported platforms**". Pack ini akan memungkinkan Anda untuk menambahkan fungsionalitas tambahan ke VirtualBox: tidak wajib untuk menambahkannya, tetapi bisa berguna! Misalnya, ini mencakup dukungan untuk USB 3.0 di VM, dukungan webcam, dan enkripsi disk.

Buka VirtualBox, klik "**File**" dan kemudian "**Settings**" pada menu.

![Image](assets/fr/005.webp)

Klik "**Extensions**" di sebelah kiri (1), lalu tombol "**+**" di sebelah kanan (2) untuk **memuat extension pack VirtualBox** yang baru saja Anda unduh (3).

![Image](assets/fr/006.webp)

Konfirmasikan dengan mengeklik tombol "**Install**".

![Image](assets/fr/007.webp)

Klik "**OK**": _extension pack_ resmi sekarang terpasang di instance VirtualBox Anda!

![Image](assets/fr/008.webp)

Mari kita lanjutkan ke pembuatan virtual machine pertama kita.

## IV. Membuat VM VirtualBox pertama Anda



Untuk membuat mesin virtual baru di VirtualBox, cukup klik tombol "**New**" untuk meluncurkan wizard pembuatan VM. Karena ini adalah pertama kalinya Anda menjalankan VirtualBox, saya ingin memberikan beberapa detail lebih lanjut tentang Interface dan tombol-tombol lainnya.

Untuk membuat virtual machine baru di VirtualBox, cukup klik tombol "**New**" untuk menjalankan wizard pembuatan VM. Karena ini adalah pertama kalinya Anda memulai VirtualBox, saya ingin memberi Anda beberapa detail tambahan tentang Interface dan tombol-tombol lainnya.

- **Settings**: konfigurasi VirtualBox secara umum (folder VM default, manajemen pembaruan, bahasa, jaringan NAT, ekstensi, dll.)
- **Import**: mengimpor virtual appliance dalam format OVF
- **Export**: mengekspor virtual machine yang ada dalam format OVF untuk membuat virtual appliance
- **Add**: menambahkan virtual machine yang sudah ada ke inventaris VirtualBox Anda, dalam format standar VirtualBox (vbox) atau format XML

Di sebelah kiri, bagian "**Tools**" memberikan akses ke **fungsi-fungsi lanjutan, terutama untuk mengelola jaringan virtual, tetapi juga untuk mengelola penyimpanan VM**. Di bawah entri "**Tools**", mesin virtual Anda akan ditambahkan nanti.

![Image](assets/fr/009.webp)

### A. Proses pembuatan VM

**Sebagai pengingat, VirtualBox mendukung banyak sistem operasi, termasuk Windows, Linux, dan BSD. Dalam contoh ini, saya akan membuat mesin virtual untuk Windows 11. Beberapa bidang perlu diisi:

Sebagai pengingat, VirtualBox mendukung berbagai sistem operasi, termasuk Windows, Linux, dan BSD. Dalam contoh ini, saya akan membuat VM untuk Windows 11. Beberapa kolom perlu diisi:

- **Name**: nama BM (ini adalah nama yang akan ditampilkan di VirtualBox)
- **Machine folder**: tempat menyimpan VM, dengan mengetahui bahwa subfolder dengan nama VM akan dibuat di lokasi ini
- **Type**: jenis sistem operasi, tergantung pada OS yang ingin Anda pasang
- **Version**: versi sistem yang ingin Anda pasang, dalam hal ini Windows 11, jadi "**Windows11_64**"

Klik "**Next**" untuk melanjutkan.

![Image](assets/fr/010.webp)

Tergantung pada sistem operasi yang Anda pilih di langkah sebelumnya, **VirtualBox memberikan rekomendasi tentang sumber daya yang akan dialokasikan ke VM**. Di sini, kita berbicara tentang RAM yang ingin Anda alokasikan ke VM. Mari kita asumsikan 4 GB, karena ini memang direkomendasikan untuk Windows 11, tetapi jika Anda kekurangan sumber daya, **tentukan 2 GB sebagai gantinya**.

**Catatan**: sumber daya yang dialokasikan untuk VM dapat dimodifikasi nanti.

![Image](assets/fr/011.webp)

Adapun hard disk virtual, kita mulai dari awal, jadi kita perlu memilih "**Create virtual hard disk now**" agar VM memiliki ruang penyimpanan untuk memasang sistem operasi dan menyimpan data. Klik "**Create**".

![Image](assets/fr/012.webp)

VirtualBox mendukung tiga format berbeda untuk hard disk virtual, yang merupakan perbedaan utama dibandingkan dengan solusi lain seperti VMware dan Hyper-V. Ada tiga format yang bisa dipilih:

- **VDI**, format resmi VirtualBox
- **VHD**, yang merupakan format resmi Hyper-V, meskipun format VHDX yang baru lebih sering digunakan saat ini
- **VMDX** adalah format resmi VMware untuk VMware Workstation dan VMware ESXi

Untuk membuat VM yang hanya akan digunakan pada instance VirtualBox ini, pilih "**VDI**". Di sisi lain, jika hard disk virtual akan dilampirkan ke host Hyper-V di kemudian hari, mungkin ide yang bagus untuk memulai dengan format VHD untuk menghindari keharusan mengonversinya. Klik "**Next**".

![Image](assets/fr/013.webp)

**Disk virtual dapat berukuran dinamis atau tetap**. Ketika dinamis, file yang mewakili **disk virtual (di sini file .vdi)** akan tumbuh saat data ditulis ke disk hingga mencapai ukuran maksimumnya, tetapi tidak akan menyusut jika data dihapus. Sebaliknya, ketika berukuran tetap, **total ruang penyimpanan dialokasikan segera (dan karenanya dicadangkan)**, yang memungkinkan kinerja sedikit lebih baik, tetapi membutuhkan waktu lebih lama saat disk virtual pertama kali dibuat.

Secara pribadi, untuk VM uji coba dengan VirtualBox, saya menganggap mode **"Dynamically allocated**" sudah cukup.

![Image](assets/fr/014.webp)

**Langkah selanjutnya adalah menentukan ukuran disk virtual**, dengan mengingat bahwa secara default, disk akan disimpan di direktori VM (ini dapat diubah pada tahap ini). Saya telah menentukan ukuran 64 GB untuk mematuhi persyaratan Windows 11, tetapi di sini lagi, ukuran yang lebih kecil dapat dialokasikan. Klik "**Create**" untuk membuat VM!

![Image](assets/fr/015.webp)

Pada titik ini, VM ada di inventaris kita, sudah dikonfigurasi, tetapi sistem operasinya belum terpasang. Kita perlu menyelesaikan konfigurasi VM sebelum memulainya.

### B. Memasang image ISO ke VM VirtualBox

Untuk memasang Windows 11, atau sistem lainnya, kita memerlukan file instalasi. Dalam kebanyakan kasus, kita menggunakan image disk dalam format ISO untuk memasang sistem operasi. Kita perlu memasukan image ISO Windows 11 ke dalam drive DVD virtual VM kita.

Klik VM di inventaris VirtualBox (1), lalu pada tombol "**Configuration**" (2), yang memberikan akses ke konfigurasi umum VM ini. Menu ini digunakan untuk mengelola sumber daya (misalnya, menambah RAM, mengonfigurasi CPU, dll.). Klik "**Storage**" di sebelah kiri (3), pada drive DVD tempat tertulis "**Empty**" saat ini (4) lalu klik ikon berbentuk DVD (5) dan "**Choose a disk file**".

![Image](assets/fr/016.webp)

Pilih image ISO dari sistem operasi yang ingin Anda instal, lalu klik OK. Inilah yang saya dapatkan:

![Image](assets/fr/017.webp)

Tetap di bagian "**Configuration**" pada VM, saya masih memiliki beberapa hal untuk dijelaskan.

### C. Koneksi jaringan VM

Pergi ke bagian "**Network**" di sebelah kiri. Bagian ini memungkinkan Anda mengelola jaringan mesin virtual: jumlah interface jaringan virtual (hingga 4 per VM), MAC address, dan mode akses jaringan (NAT, bridge access, jaringan internal, dll.). **Jika Anda ingin VM Anda memiliki akses ke Internet, pilih "NAT" atau "Bridge Access"**, tetapi mode kedua ini memerlukan server DHCP yang aktif di jaringan Anda, atau Anda harus mengonfigurasi alamat IP secara manual.

**Catatan**: Saya akan kembali ke bagian jaringan secara lebih rinci dalam artikel khusus.

![Image](assets/fr/018.webp)

### D. Jumlah prosesor virtual

Seperti komputer fisik, VM membutuhkan RAM, hard disk, dan prosesor untuk berfungsi. Ketika kita membuat VM, Anda mungkin menyadari bahwa wizard tidak menyertakan konfigurasi prosesor. Namun, ini dapat dikonfigurasi kapan saja melalui tab "**System**", lalu "**Processor**", di mana Anda dapat memilih jumlah prosesor virtual.

**Catatan**: Opsi "**Enable VT-x/AMD-v nested**" diperlukan untuk virtualisasi berlapis.

Dalam kasus saya, VM memiliki 2 prosesor virtual:

![Image](assets/fr/019.webp)

**Jangan ragu untuk melihat bagian lain dari menu konfigurasi.**

### E. Booting pertama dan Instalasi OS

Untuk memulai VM, cukup pilih di inventaris dan klik tombol "**Start**". Window kedua akan terbuka, memberikan gambaran visual dari VM.

Aduh, saya mendapat kesalahan yang tidak menyenangkan dan VM saya tidak mau berjalan! Kesalahannya adalah "Login failed for virtual machine..." dengan detail berikut:

```shell
Not in a hypervisor partition (HPV=0)
AMD-V is disabled in the BIOS (or by the host OS)
```

![Image](assets/fr/020.webp)

Pada kenyataannya, ini normal karena **fitur virtualisasi tidak diaktifkan di komputer saya!** Untuk memperbaiki masalah ini, Anda perlu me-reboot komputer Anda untuk mengakses BIOS dan mengaktifkan virtualisasi.

![Image](assets/fr/021.webp)

Tanpa menunggu, saya me-reboot komputer saya dan **menekan tombol "SUPPR" untuk mengakses BIOS** (tombolnya dapat bervariasi tergantung pada komputer, dan bisa jadi F2, misalnya) dari motherboard ASUS saya. Untuk mengaktifkan virtualisasi, "SVM Mode" harus diaktifkan dalam kasus saya. Di sini sekali lagi, dari satu motherboard ke motherboard lain, dari satu produsen ke produsen lain, namanya dapat berbeda. Cari fungsi yang mengacu pada **AMD-V (untuk CPU AMD) atau Intel VT-x (untuk CPU Intel)**.

![Image](assets/fr/022.webp)

Setelah ini selesai, simpan modifikasi dan restart komputer... Kali ini, **VirtualBox dapat memulai VM** dan memuat image ISO Windows untuk menginstal sistem operasi 🙂

![Image](assets/fr/023.webp)

Pada host fisik Windows 11, tempat VirtualBox diinstal, kita dapat melihat bahwa folder mesin virtual Windows 11 berisi berbagai file.

Pada host fisik Windows 11 kita, tempat VirtualBox diinstall, kita dapat melihat bahwa folder VM Windows 11 berisi berbagai file.

- **File .VBOX** (dalam format XML) yang sesuai dengan konfigurasi VM (RAM, CPU, dll.)
- **File .VBOX-PREV** adalah cadangan dari konfigurasi sebelumnya
- **File .VDI** sesuai dengan hard disk virtual dalam mode dinamis, sehingga saat ini hanya 13 GB, padahal ukuran maksimumnya adalah 64 GB
- **File .NVRAM** berisi status BIOS dari VM, yang setara dengan memori non-volatil dari mesin fisik

![Image](assets/fr/024.webp)

## V. Kesimpulan

**VirtualBox sekarang sudah aktif dan berjalan di mesin fisik Windows 11 kita! Yang tersisa hanyalah memanfaatkannya dan membuat VM!** Saya akan kembali ke instalasi Windows 11 di VM VirtualBox dalam artikel lain. Untuk Windows 10, Windows Server atau distribusi Linux (Ubuntu, Debian, dll.), biarkan kami membimbing Anda!
