---
name: OPNsense
description: Bagaimana cara menginstal dan mengonfigurasi firewall OPNsense?
---
![cover](assets/cover.webp)



___



*Tutorial ini didasarkan pada konten asli oleh Florian BURNEL yang dipublikasikan di [IT-Connect](https://www.it-connect.fr/). Lisensi [CC BY-NC 4.0] (https://creativecommons.org/licenses/by-nc/4.0/). Perubahan mungkin telah dilakukan pada teks asli.*



___



## I. Presentasi



Dalam tutorial ini, kita akan melihat pada firewall sumber terbuka OPNsense. Kita akan melihat fitur-fitur utamanya, prasyaratnya, dan cara menginstal solusi berbasis FreeBSD ini.



Sebelum memulai, Anda harus tahu bahwa **OPNsense dan pfSense adalah firewall sumber terbuka** yang berbasis FreeBSD. Bisa dikatakan bahwa pfSense adalah saudara tua dari OPNsense, karena pfSense adalah Fork yang dibuat pada tahun 2015. Terakhir, penting untuk diketahui bahwa sejak tahun 2017, **OPNsense telah beralih ke HardenedBSD dan bukannya FreeBSD**. HardenedBSD adalah versi yang disempurnakan dari FreeBSD, dengan fitur keamanan yang canggih



OPNsense menonjol karena pengguna Interface yang lebih modern dan irama pembaruan yang lebih sering. Memang, jadwal pembaruan OPNsense mencakup dua rilis utama per tahun, yang diperbarui setiap dua minggu atau lebih (menghasilkan rilis minor). Tindak lanjut ini sangat menarik dibandingkan dengan pfSense, jika kita melihat versi komunitas dari solusi ini.



![Image](assets/fr/050.webp)



## II. Fitur OPNsense



OPNsense adalah sistem operasi yang dirancang untuk bertindak sebagai firewall dan router, meskipun fitur-fiturnya sangat banyak dan dapat diperluas dengan menginstal paket tambahan. Cocok untuk penggunaan produksi, terutama digunakan untuk keamanan jaringan dan manajemen aliran.



### A. Fitur utama



Berikut ini adalah beberapa fitur utama OPNsense:





- Firewall dan NAT**: OPNsense menyediakan fungsionalitas firewall stateful tingkat lanjut dengan pemfilteran stateful, serta kemampuan penerjemahan jaringan Address (NAT).





- DNS/DHCP**: OPNsense dapat dikonfigurasikan untuk mengelola layanan DNS dan DHCP di jaringan. OPNsense dapat bertindak sebagai server DHCP, tetapi juga dapat digunakan sebagai penyelesai DNS untuk mesin di jaringan lokal. Dnsmasq juga terintegrasi secara default.





- VPN**: OPNsense mendukung beberapa protokol VPN, termasuk IPsec, OpenVPN dan WireGuard, yang memungkinkan koneksi aman untuk akses jarak jauh ke workstation seluler atau interkoneksi situs.





- Proksi web**: OPNsense menyertakan proxy web untuk mengontrol dan memfilter akses Internet. Proxy ini juga dapat digunakan untuk memfilter konten dan mengelola akses jaringan.





- Manajemen bandwidth (QoS)**: OPNsense menawarkan fitur manajemen Kualitas Layanan (QoS) untuk memprioritaskan lalu lintas jaringan dan mengelola bandwidth jaringan dengan lebih baik.





- Captive portal**: fitur ini memungkinkan Anda mengelola akses pengguna ke jaringan melalui halaman autentikasi (basis lokal, voucher, dll.). Ini adalah fitur yang umumnya digunakan untuk jaringan Wi-Fi publik.





- IDS/IPS**: OPNsense mengintegrasikan Suricata untuk menawarkan fungsi deteksi dan pencegahan intrusi (IDS/IPS) untuk melindungi jaringan dari serangan.





- Ketersediaan tinggi (CARP)**: OPNsense mendukung CARP (*Common Address Redundancy Protocol*) untuk ketersediaan tinggi di antara beberapa firewall OPNsense, memastikan bahwa layanan tetap aktif meskipun terjadi kegagalan perangkat keras.





- Pelaporan dan Pemantauan**: OPNsense menyediakan alat pelaporan dan pemantauan waktu nyata untuk melacak kinerja jaringan (dengan NetFlow) dan mendeteksi potensi masalah, berkat pembuatan log. Ini termasuk grafik. Alat Monit terintegrasi ke dalam OPNsense dan memungkinkan pengawasan terhadap firewall itu sendiri.



### B. Paket tambahan



Ini hanyalah gambaran umum dari fitur-fitur yang ditawarkan oleh OPNsense. Selain itu, **katalog paket** yang dapat diakses dari administrasi OPNsense Interface memungkinkan Anda untuk **memperkaya firewall dengan fungsi tambahan**. Ini termasuk klien ACME, agen Wazuh, layanan NTP Chrony, dan Caddy sebagai proksi terbalik.



![Image](assets/fr/051.webp)



## III. Prasyarat OPNsense



Pertama-tama, Anda harus memutuskan di mana Anda akan menginstal OPNsense. Ada beberapa solusi yang memungkinkan, termasuk pemasangan di :





- Hypervisor sebagai mesin virtual, baik Hyper-V, Proxmox, VMware ESXi, dll.
- Sebuah mesin sebagai sistem *bare-metal*. Ini bisa berupa PC mini yang bertindak sebagai firewall.



Anda juga dapat membeli **alat yang dapat dipasang di rak OPNsense** melalui toko online kami.



Anda perlu mempertimbangkan sumber daya perangkat keras yang diperlukan untuk menjalankan OPNsense. Hal ini dijelaskan secara rinci pada [halaman dokumentasi ini](https://docs.opnsense.org/manual/hardware.html).



**Sumber daya minimum dan yang direkomendasikan untuk produksi:**



| Caractéristiques | Minimum | Recommandation |
| --- | --- | --- |
| Processeur | 1 GHz - 2 cœurs | 1.5 GHz - Multi-coeurs |
| Mémoire vive (RAM) | 2 Go | 8 Go |
| Espace de stockage pour le système | Disque dur, disque SSD ou carte SD (4 Go) | 120 Go en SSD |

Terakhir, **kebutuhan sumber daya Anda sangat bergantung pada jumlah koneksi yang akan dikelola**, dan oleh karena itu pada **kebutuhan bandwidth Anda**. Selain itu, Anda perlu **memperhatikan layanan yang akan diaktifkan dan digunakan** (proxy, deteksi penyusupan, dll...) karena layanan ini mungkin membutuhkan CPU dan/atau RAM yang besar.



Anda juga memerlukan image ISO instalasi OPNsense, yang dapat Anda unduh dari [situs web resmi](https://opnsense.org/download/). Untuk instalasi pada VM, pilih "**dvd**" sebagai jenis image untuk mendapatkan image ISO (dan lakukan apa pun yang Anda inginkan...). Untuk instalasi melalui kunci USB yang dapat di-boot, pilih opsi "**vga**" untuk mendapatkan file "**.img**".



![Image](assets/fr/048.webp)



Anda juga memerlukan komputer untuk administrasi dan pengujian OPNsense.



## IV. Konfigurasi target



Tujuan kami adalah untuk





- Buat jaringan virtual internal (192.168.10.0/24 - LAN)**, yang dapat mengakses Internet melalui firewall OPNsense. Untuk penggunaan produksi, ini bisa berupa jaringan lokal, kabel dan/atau Wi-Fi.
- Aktifkan dan konfigurasikan NAT** agar VM di jaringan virtual internal dapat mengakses Internet
- Aktifkan dan konfigurasikan server DHCP pada OPNsense** untuk mendistribusikan konfigurasi IP ke mesin masa depan yang tersambung ke jaringan virtual internal
- Konfigurasikan firewall** untuk mengizinkan hanya aliran keluar LAN ke WAN dalam HTTP (80) dan HTTPS (443).
- Konfigurasikan firewall** untuk mengizinkan LAN virtual menggunakan OPNsense sebagai resolver DNS (53).



Jika Anda menggunakan platform Hyper-V, ini akan memberi Anda representasi berikut:



![Image](assets/fr/033.webp)



## V. Menginstal firewall OPNsense



### A. Mempersiapkan kunci USB yang dapat di-booting



Langkah pertama adalah menyiapkan media instalasi: **kunci USB yang dapat di-booting dengan OPNsense**. Ini tentu saja opsional jika Anda bekerja di lingkungan virtual, tetapi bagaimanapun juga, Anda perlu mengunduh citra ISO instalasi OPNsense.



Setelah mengunduh, Anda akan mendapatkan **arsip yang berisi gambar dalam format ".img". Anda dapat **membuat stik USB yang dapat di-boot** dengan berbagai aplikasi, termasuk **balenaEtcher**: sangat mudah digunakan. Terlebih lagi, aplikasi ini akan mengenali gambar dalam arsip, sehingga Anda tidak perlu mendekompresnya terlebih dahulu.





- [Unduh balenaEtcher](https://etcher.balena.io/)



Setelah aplikasi terinstal, pilih gambar Anda, kunci USB Anda, lalu klik tombol "Flash! Tunggu sebentar.



![Image](assets/fr/049.webp)



Sekarang Anda siap untuk menginstal.



### B. Menginstal Sistem OPNsense



Mulai jalankan mesin yang menghosting OPNsense. Anda akan melihat halaman selamat datang yang mirip dengan yang di bawah ini. Selama beberapa detik, layar yang ditampilkan akan terlihat di jendela. Biarkan prosesnya berjalan dengan sendirinya...



![Image](assets/fr/019.webp)



Gambar OPNsense dimuat ke dalam mesin, sehingga sistem dapat diakses dalam mode "**live**", yaitu disimpan sementara dalam memori.



![Image](assets/fr/025.webp)



Kemudian Anda akan sampai pada Interface yang mirip dengan yang di bawah ini. Masuk dengan login "**installer**" dan kata sandi "**opnsense**". Harap diperhatikan bahwa keyboard yang digunakan saat ini adalah **QWERTY**. Pada titik ini, kita akan **memulai proses instalasi OPNsense**.



![Image](assets/fr/026.webp)



Wizard baru muncul di layar. Langkah pertama adalah memilih tata letak keyboard yang sesuai dengan konfigurasi Anda. Untuk keyboard AZERTY, pilih opsi "**Prancis (tombol aksen)**" dari daftar, lalu klik dua kali**.



![Image](assets/fr/027.webp)



Langkah kedua adalah memilih tugas yang akan dilakukan. Di sini, kita akan melakukan instalasi menggunakan sistem file **ZFS**. Posisikan diri Anda pada baris "**Install (ZFS)**" dan konfirmasikan dengan **Enter**.



![Image](assets/fr/028.webp)



Pada langkah ketiga, pilih "**stripe**" karena mesin kami dilengkapi dengan **hanya satu disk**: tidak ada redundansi yang memungkinkan untuk mengamankan penyimpanan firewall dan datanya. Hal ini sangat relevan ketika menginstal pada mesin fisik untuk melindungi dari kegagalan perangkat keras disk, melalui prinsip RAID.



![Image](assets/fr/029.webp)



Pada langkah keempat, cukup tekan **Enter** untuk mengonfirmasi.



![Image](assets/fr/030.webp)



Terakhir, konfirmasikan dengan memilih "**YES**" lalu tekan tombol **Enter**.



![Image](assets/fr/031.webp)



Sekarang Anda harus menunggu sementara OPNsense diinstal... Proses ini membutuhkan waktu sekitar 5 menit.



![Image](assets/fr/032.webp)



Setelah instalasi selesai, kita dapat mengubah kata sandi "**root**" sebelum melakukan boot ulang. Pilih "**Root Password**", tekan **Enter** dan masukkan kata sandi "**root**" dua kali.



![Image](assets/fr/020.webp)



Terakhir, pilih "**Complete Install**" dan tekan **Enter**. Gunakan kesempatan ini untuk **mengeluarkan disk dari drive DVD VM**. Dalam pengaturan VM, Anda juga dapat mengatur boot pertama ke disk.



![Image](assets/fr/021.webp)



Mesin virtual akan melakukan boot ulang dan memuat sistem OPNsense dari disk, karena kita baru saja menginstalnya. Masuk dengan akun "root" di konsol, dan kata sandi baru Anda (jika tidak, kata sandi default adalah "**opnsense**").



### D. Menghubungkan antarmuka jaringan



Layar yang ditunjukkan di bawah ini akan muncul. Pilih "**1**" dan tekan **Enter** untuk mengaitkan kartu jaringan mesin dengan antarmuka OPNsense.



![Image](assets/fr/022.webp)



Pertama, wizard akan meminta Anda untuk mengonfigurasi agregasi tautan dan VLAN. Tentukan "**n**" untuk menolak, dan setiap kali, validasi jawaban Anda dengan **Enter**. Selanjutnya, Anda perlu menetapkan dua antarmuka "**hn0**" dan "**hn1**" ke **WAN** dan **LAN**. Pada prinsipnya, "**hn0**" berhubungan dengan WAN dan Interface lainnya ke LAN.



Begini cara kerjanya:



![Image](assets/fr/023.webp)



Kami sekarang memiliki :





- Interface **LAN** yang terkait dengan kartu jaringan "**hn1**" dan dengan IP default OPNsense Address, yaitu **192.168.1.1/24**.
- Interface **WAN** terkait dengan kartu jaringan "**hn0**" dan dengan IP Address yang diambil melalui **DHCP** di jaringan lokal (berkat sakelar virtual eksternal kami).



Secara default, administrasi OPNsense Interface hanya dapat diakses dari LAN Interface, untuk alasan keamanan yang jelas. Oleh karena itu, Anda harus tersambung ke LAN Interface firewall untuk melakukan administrasi. Jika hal ini tidak memungkinkan, Anda dapat mengelola OPNsense untuk sementara waktu dari WAN. Hal ini melibatkan penonaktifan fungsi firewall.



Untuk melakukan ini, alihkan ke mode shell melalui opsi "**8**" dan jalankan perintah berikut:



```
pfctl -d
```



![Image](assets/fr/024.webp)



### E. Akses ke sistem manajemen OPNsense Interface



Administrasi OPNsense Interface dapat diakses melalui HTTPS, menggunakan IP Address dari LAN** Interface (atau WAN). Browser Anda akan membawa Anda ke halaman login. Masuk dengan akun "root" dan kata sandi yang telah Anda pilih sebelumnya.



![Image](assets/fr/034.webp)



Tunggu beberapa detik... Anda akan diminta untuk mengikuti panduan untuk melakukan konfigurasi dasar. Klik "**Next**" untuk melanjutkan.



![Image](assets/fr/036.webp)



Langkah pertama adalah menentukan nama host, nama domain, memilih bahasa dan menentukan server DNS yang akan digunakan untuk resolusi nama. Menyimpan opsi "**Enable Resolver**" akan memungkinkan firewall digunakan sebagai DNS resolver, yang akan berguna untuk mesin-mesin di LAN virtual kita.



![Image](assets/fr/037.webp)



Lanjutkan ke langkah berikutnya. Wizard memberi Anda pilihan untuk **menentukan server NTP untuk sinkronisasi tanggal dan waktu**, meskipun sudah ada server yang dikonfigurasikan secara default. Selain itu, penting untuk memilih zona waktu yang sesuai dengan lokasi geografis Anda (kecuali jika Anda memiliki persyaratan khusus).



![Image](assets/fr/038.webp)



Kemudian, tibalah pada langkah yang penting: **mengkonfigurasi WAN Interface**. Saat ini, ini dikonfigurasikan dalam DHCP dan akan tetap berada dalam mode konfigurasi ini, kecuali jika Anda ingin menetapkan IP statis Address.



![Image](assets/fr/039.webp)



Masih pada halaman konfigurasi WAN Interface, Anda perlu menghapus centang pada opsi "**Block access to private networks via WAN**" jika jaringan pada sisi WAN menggunakan pengalamatan privat. Ini mungkin akan terjadi jika Anda menjalankan Lab, dan dapat mencegah Anda mengakses Internet.



![Image](assets/fr/040.webp)



Selanjutnya, Anda dapat **menentukan kata sandi "root "**, tetapi ini opsional karena kita sudah melakukannya.



![Image](assets/fr/041.webp)



Lanjutkan hingga akhir untuk memulai pemuatan ulang konfigurasi. Jika Anda perlu melanjutkan kontrol melalui WAN, mulai ulang perintah di atas setelah proses ini selesai.



![Image](assets/fr/042.webp)



Hanya itu saja yang bisa dilakukan!



![Image](assets/fr/035.webp)



### E. Konfigurasi DHCP



Tujuan kita adalah menggunakan server DHCP OPNsense untuk mendistribusikan alamat IP pada LAN virtual. Untuk melakukan ini, kita perlu mengakses lokasi menu ini:



```
Services > ISC DHCPv4 > [LAN]
```



**Seperti yang Anda lihat, DHCP sudah diaktifkan secara default pada LAN ** Jika Anda tidak tertarik dengan layanan ini, Anda harus menonaktifkannya. Meskipun sudah diaktifkan dan kita ingin menggunakannya, penting untuk meninjau ulang konfigurasinya.



Jika diperlukan, Anda dapat mengubah rentang alamat IP yang akan didistribusikan: **192.168.10.10** hingga **192.168.10.245**, tergantung pada pengaturan saat ini.



![Image](assets/fr/046.webp)



Kita juga bisa melihat bahwa bidang "**Server DNS**", "**Gateway**", "**Nama domain**", dan lain-lain, kosong secara default. Bahkan, ada pewarisan otomatis opsi tertentu dan nilai default untuk berbagai bidang ini. Misalnya, untuk server DNS, IP Address dari LAN Interface akan didistribusikan, sehingga memungkinkan firewall OPNsense digunakan sebagai DNS resolver.



Simpan konfigurasi setelah melakukan perubahan, jika perlu.



![Image](assets/fr/047.webp)



Untuk menguji server DHCP, Anda perlu menyambungkan mesin ke jaringan LAN firewall Anda.



Mesin ini harus mendapatkan IP Address dari server DHCP OPNsense, dan mesin kita harus memiliki akses ke jaringan. Akses internet harus berfungsi. Harap diperhatikan bahwa jika Anda telah menonaktifkan fungsi firewall untuk mengakses OPNsense dari WAN, hal ini akan menonaktifkan NAT, sehingga Anda tidak dapat mengakses Web.



**Catatan**: sewa DHCP yang saat ini dikeluarkan dapat dilihat dari administrasi OPNsense Interface. Untuk melakukannya, buka lokasi berikut ini: **Layanan > ISC DHCPv4 > Sewa**.



![Image](assets/fr/045.webp)



### F. Mengkonfigurasi aturan NAT dan firewall



Kabar baiknya, sekarang kita bisa mengakses administrasi OPNsense Interface dari LAN.



```
https://192.168.1.10
```



Setelah masuk ke OPNsense, mari kita temukan konfigurasi NAT. Pergi ke lokasi ini: ** Firewall > NAT > Outbound**. Di sini Anda dapat memilih antara pembuatan aturan NAT keluar secara otomatis (default) dan manual.



Pilih mode otomatis melalui opsi "**Pembuatan aturan NAT keluar secara otomatis**" dan klik "**Save**" (pada prinsipnya, konfigurasi ini sudah menjadi konfigurasi aktif). Dalam mode otomatis, OPNsense sendiri akan membuat aturan NAT untuk setiap jaringan Anda.



![Image](assets/fr/043.webp)



Untuk saat ini, semua komputer yang tersambung ke LAN virtual "**192.168.10.0/24**" dapat mengakses Internet tanpa batasan. Namun, tujuan kami adalah untuk membatasi akses ke WAN ke protokol HTTP dan HTTPS, serta DNS pada LAN Interface firewall.



Jadi kita perlu membuat aturan firewall... Jelajahi menu sebagai berikut: ** Firewall > Rules > LAN**.



**Secara default, ada dua aturan untuk mengesahkan semua lalu lintas LAN keluar, dalam IPv4 dan IPv6**. Nonaktifkan kedua aturan ini dengan mengklik panah Green di ujung kiri, di awal setiap baris.



Kemudian buat tiga aturan baru untuk mengesahkan **jaringan LAN** (yaitu "**LAN net**") ke :





- mengakses semua tujuan menggunakan **HTTP**.
- mengakses semua tujuan dengan **HTTPS**.
- meminta **OPNsense** pada **Interface LAN** (yaitu "**LAN Address**"), melalui **protokol DNS** (ini berarti menggunakan firewall sebagai DNS), jika tidak, otorisasi DNS resolver Anda melalui IP Address.



Ini memberikan hasil sebagai berikut:



![Image](assets/fr/044.webp)



Yang tersisa hanyalah mengklik "**Terapkan perubahan**" untuk mengalihkan aturan firewall baru ke produksi. **Harap diperhatikan bahwa semua aliran yang tidak diotorisasi secara eksplisit akan diblokir secara default



Mesin LAN dapat mengakses Internet, menggunakan HTTP dan HTTPS. Semua protokol lain akan diblokir.



![Image](assets/fr/018.webp)



## IV. Kesimpulan



Dengan mengikuti panduan ini, Anda akan dapat menginstal OPNsense dan segera memulai. OPNsense menawarkan berbagai macam fitur untuk mengamankan dan mengelola lalu lintas jaringan Anda secara efisien, dan cocok untuk digunakan di lingkungan profesional.



Instalasi ini hanyalah permulaan: silakan menjelajahi menu dan mengonfigurasi fitur-fitur lain untuk menyesuaikan OPNsense dengan kebutuhan Anda.