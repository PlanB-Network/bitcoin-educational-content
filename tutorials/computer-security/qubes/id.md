---
name: Qubes
description: Sistem operasi yang cukup aman.
---

![cover](assets/cover.webp)



Qubes OS adalah sistem operasi sumber terbuka gratis yang dirancang untuk pengguna yang menempatkan keamanan sebagai prioritas utama. Keistimewaannya didasarkan pada ide yang sederhana namun radikal: alih-alih mempertimbangkan komputer secara keseluruhan, sistem ini membagi penggunaannya ke dalam kompartemen-kompartemen independen yang disebut **_qubes_**.



Setiap qube berfungsi sebagai **lingkungan virtual yang terisolasi**, dengan tingkat kepercayaan dan fungsi tertentu. Jadi, meskipun sebuah aplikasi disusupi, serangannya tetap terbatas pada qube-nya tanpa mempengaruhi sistem lainnya.



> Jika Anda serius tentang keamanan, Qubes OS adalah sistem operasi terbaik yang tersedia saat ini. - **Edward Snowden**.

Namun, menginstal Qubes OS membutuhkan lebih banyak persiapan daripada menginstal sistem operasi konvensional. Persiapan ini melibatkan pemeriksaan prasyarat perangkat keras tertentu, memahami dasar-dasar virtualisasi, dan menerima pengalaman yang berbeda, di mana setiap tugas sehari-hari dipikirkan dalam bentuk pemisahan. Namun, setelah terpasang, Qubes OS menawarkan kerangka kerja yang kuat yang mengubah cara Anda berinteraksi dengan komputer setiap hari. Dalam tutorial ini, kami akan menjelaskan cara kerja Qubes OS dan cara menginstalnya dengan mudah di sistem Anda.



## Bagaimana cara kerja Qubes OS?



Qubes OS didasarkan pada prinsip kompartementalisasi. Alih-alih menggunakan sistem tunggal, ia mengandalkan hypervisor **Xen** untuk membuat mesin virtual yang terisolasi, yang disebut qubes. Setiap qube didedikasikan untuk tugas atau tingkat kepercayaan tertentu (pekerjaan, penjelajahan pribadi, perbankan, dll.). Pemisahan ini memastikan bahwa kompromi apa pun dalam satu qube tidak dapat menyebar ke yang lain, bertindak sebagai beberapa komputer independen dalam satu mesin.



Pengguna Interface dikelola oleh domain pusat yang aman yang disebut **dom0**. Domain ini benar-benar terisolasi dari Internet, menjadikannya jantung dari sistem. Meskipun jendela dan menu ditampilkan oleh dom0, eksekusi aplikasi yang sebenarnya terjadi di qubes masing-masing.



## Berbagai jenis qubes



Di sekeliling dom0 berputar berbagai jenis qubes, masing-masing dengan peran yang sangat spesifik.





- AppVM digunakan untuk menjalankan aplikasi sehari-hari: pengguna dapat memisahkan email profesionalnya dari aktivitas penjelajahan web atau perbankan, dengan masing-masing lingkungan yang sepenuhnya independen dari yang lain.





- AppVM ini sendiri didasarkan pada **TemplateVM**, yang berfungsi sebagai templat terpusat untuk menginstal dan memperbarui perangkat lunak, sehingga tidak perlu lagi mengelola setiap qube secara terpisah.



Qubes OS juga mengintegrasikan mesin virtual yang dikhususkan untuk **layanan sistem**.





- **NetVM** secara langsung mengelola **perangkat jaringan** dan memastikan koneksi ke Internet. Mereka sering dikaitkan dengan **FirewallVMs**, yang melakukan intervensi untuk **menyaring lalu lintas** dan membatasi eksposur qubes lain.





- ServiceVM memainkan peran serupa, misalnya dalam manajemen perangkat USB, selalu dengan logika yang sama: mengisolasi komponen yang paling berisiko untuk mengurangi permukaan serangan.



Terakhir, untuk tugas-tugas yang sesekali atau berisiko, Qubes OS menawarkan **DisposableVM**. Qubes sementara ini dibuat dengan cepat untuk **membuka dokumen yang mencurigakan** atau **mengunjungi situs yang meragukan**, kemudian menghilang sepenuhnya ketika ditutup, menghapus semua jejak dan mencegah serangan yang terus-menerus.



### Mekanisme penyalinan yang aman (qrexec)



Pertukaran antar qubes didasarkan pada **qrexec**, sistem komunikasi antar-VM yang dirancang untuk keamanan. Alih-alih membiarkan qubes berkomunikasi secara bebas, qrexec memberlakukan **kebijakan khusus**: file yang disalin dari satu AppVM ke AppVM lainnya, atau teks yang ditransfer melalui clipboard, selalu melewati saluran yang dimonitor dan divalidasi oleh sistem. Dengan cara ini, bahkan tindakan menyalin dan menempel yang sederhana pun dapat dikontrol untuk mencegah penyebaran malware.



### Manajemen disk



Qubes OS menggunakan sistem yang cerdas untuk manajemen penyimpanan. TemplateVM berisi basis perangkat lunak umum, sedangkan AppVM hanya menambahkan data pribadi dan file tertentu. Hal ini mengurangi penggunaan ruang disk dan memfasilitasi pembaruan global. Di sisi lain, DisposableVM menggunakan volume sementara yang akan hilang sepenuhnya ketika ditutup. Model ini tidak hanya menjamin keamanan yang lebih baik, tetapi juga manajemen sumber daya yang efisien.



## Mengapa memilih Qubes OS?



Keunggulan Qubes OS terutama terletak pada model keamanannya yang unik. Inti dari pendekatan ini adalah kompartementalisasi, yang melindungi pengguna dengan mengisolasi setiap tugas dalam mesin virtual yang terpisah. Dalam istilah praktisnya, email yang terinfeksi atau situs web berbahaya hanya dapat membahayakan satu qubes, sehingga seluruh sistem dan data pribadi Anda terlindungi sepenuhnya. Arsitektur ini sangat membatasi serangan kompleks yang, pada sistem konvensional, dapat menyebar dengan bebas.



Qubes OS juga menawarkan transparansi dan kontrol penuh atas lingkungan digital Anda. Anda tahu persis perangkat lunak mana yang memiliki akses ke sumber daya mana, apakah itu jaringan, perangkat USB, atau komponen sensitif lainnya. Sistem ini mengintegrasikan fitur-fitur keamanan tingkat lanjut secara default, seperti enkripsi disk penuh, dan memfasilitasi penggunaan layanan anonimisasi seperti sistem operasi Whonix.



https://planb.academy/tutorials/computer-security/operating-system/whonix-06f9172c-2962-412e-9487-b665d8ca9f59

Daripada berusaha menciptakan sistem yang tidak dapat ditembus, Qubes OS berfokus pada ketahanan: sistem ini merangkum kerusakan jika terjadi kompromi, sehingga mengurangi risiko pada seluruh sistem. Pendekatan pragmatis ini membuat Qubes OS menjadi pilihan utama bagi pengguna dengan kebutuhan keamanan yang tinggi, atau yang ingin mempertahankan kontrol maksimum atas kehidupan digital mereka.



## Menginstal OS Qubes



Sebelum menginstal Qubes OS, sangat penting untuk memastikan bahwa perangkat keras Anda memenuhi persyaratan minimum, karena sistem ini mengandalkan virtualisasi untuk mengisolasi qubes. Komponen utama yang harus diperiksa adalah :




- **Prosesor**: Prosesor 64-bit yang kompatibel dengan virtualisasi perangkat keras (Intel VT-x atau AMD-V).
- RAM: diperlukan minimal 8 GB, tetapi kami merekomendasikan RAM 16 GB atau lebih untuk menjalankan beberapa qubes secara bersamaan.
- **Ruang penyimpanan**: minimal 36 GB, idealnya 128 GB pada SSD untuk performa optimal.



Untuk menginstal Qubes OS, unduh image ISO resmi dari Qubes OS [situs resmi](https://www.qubes-os.org/downloads/). Penting untuk memeriksa integritas ISO menggunakan tanda tangan GPG yang disediakan, untuk memastikan bahwa file tersebut belum dirusak dan unduhannya aman.



https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

![0_01](assets/fr/01.webp)



Setelah ISO diverifikasi, Anda perlu membuat media instalasi yang dapat di-booting, biasanya berupa stik USB. Untuk melakukannya, unduh dan instal perangkat lunak seperti **Rufus** di Windows atau **Etcher** di Windows, Linux, atau macOS. Alat-alat ini memungkinkan Anda menyalin ISO ke stik USB sehingga dapat di-boot.



Sebelum memulai instalasi, Anda perlu mengkonfigurasi **BIOS atau UEFI** komputer Anda untuk **mengaktifkan virtualisasi** dan mengizinkan booting dari USB. Tergantung pada model mesin Anda, mungkin perlu untuk **menonaktifkan Boot Aman**, karena Qubes OS mungkin tidak dapat melakukan booting dengan opsi ini diaktifkan.



![0_02](assets/fr/02.webp)



Setelah kondisi ini terpenuhi, nyalakan kembali komputer Anda dan akses BIOS/UEFI dengan segera menekan **Esc**, **Del**, **F9**, **F10**, **F11**, atau **F12** (tergantung pada produsen). Pada menu boot, pilih kunci USB sebagai perangkat boot untuk meluncurkan instalasi Qubes OS.



**layar pengaktifan** *Layar pengaktifan*


Saat boot dari stik USB, Anda akan langsung dibawa ke menu **GRUB**, di mana Anda dapat memilih tindakan yang akan dilakukan. Dengan menggunakan tombol panah pada keyboard Anda, pilih "Instal Qubes OS" dan tekan "Enter".



![0_03](assets/fr/03.webp)



**Pilihan bahasa** :



Ketika instalasi dimulai, langkah pertama adalah **memilih bahasa** dan **varian regional** yang sesuai untuk konfigurasi Anda. Hal ini memastikan bahwa sistem dan opsi penginstalan ditampilkan dengan benar dalam bahasa pilihan Anda.



![0_04](assets/fr/04.webp)



**Konfigurasi parameter** :



Pada tahap ini, Anda perlu mengonfigurasi sejumlah Elements sebelum meluncurkan instalasi pada mesin Anda.



![0_05](assets/fr/05.webp)



**Tata letak papan ketik** :



Klik opsi **Keyboard**, lalu pilih **tata letak yang sesuai** untuk komputer Anda. Setelah Anda menentukan pilihan, klik **Terminated** untuk melanjutkan ke langkah berikutnya.



**Pilihan tujuan** :



Pilih opsi "Tujuan instalasi" untuk memilih disk tempat Anda ingin menginstal Qubes OS. Secara default, partisi dilakukan secara otomatis, sehingga Anda dapat menghapus semua data dari disk dan menginstal sistem di dalamnya. Namun, Anda dapat memilih **Customized** atau **Advanced Customization** untuk melakukan partisi yang disesuaikan. Kemudian klik "Selesai". Sistem akan meminta Anda untuk mengatur **password**, yang berfungsi sebagai keamanan Layer untuk mengenkripsi data Anda. Pastikan untuk memilih kata sandi yang rumit dan unik.



![0_06](assets/fr/06.webp)



![0_07](assets/fr/07.webp)



**Pilih format tanggal dan waktu**:


Klik opsi Waktu dan tanggal, lalu pilih zona geografis Anda. Anda juga dapat memilih format waktu yang Anda inginkan: 24 jam atau 12 jam.



![0_08](assets/fr/08.webp)



**Pembuatan akun pengguna** :


Klik **Buat pengguna** untuk membuat **akun pertama** Anda, yang akan memungkinkan Anda untuk masuk ke Qubes OS.



![0_09](assets/fr/09.webp)



**Aktifkan akun root** :


Anda juga dapat **mengaktifkan akun root** dengan menetapkan kata sandi terpisah untuk administrasi.



![0_10](assets/fr/10.webp)



Setelah pengaturan ini dibuat, klik **Mulai instalasi** untuk memulai proses.



![0_11](assets/fr/11.webp)



Tunggu hingga **akhir instalasi**, lalu klik **restart sistem** untuk menyelesaikan instalasi dan memulai Qubes OS.



![0_12](assets/fr/12.webp)



**Konfigurasi tambahan** :


Setelah reboot, Qubes OS akan meminta Anda untuk menyelesaikan **template default dan konfigurasi qubes**. Masukkan kata sandi yang ditentukan untuk mengenkripsi disk.



![0_13](assets/fr/13.webp)



Selanjutnya, mulailah dengan memilih **TemplateVM** yang ingin Anda instal. Pilihan yang umum termasuk **Debian 12 Xfce**, **Fedora 41 Xfce** dan **Whonix 17**, yang terakhir ini direkomendasikan untuk penggunaan yang membutuhkan **anonimitas dan keamanan jaringan**. Anda juga dapat menentukan **template default**, yang akan menjadi dasar untuk pembuatan **AppVM** baru.



![0_14](assets/fr/14.webp)



Pada bagian **Konfigurasi utama**, Anda dapat memilih untuk secara otomatis membuat qubes sistem yang penting seperti **sys-net**, **sys-firewall**, dan **default DisposableVM**. Disarankan untuk mengaktifkan opsi untuk membuat **sys-firewall dan sys-usb sekali pakai**, untuk membatasi eksposur perangkat dan jaringan jika terjadi kompromi. Anda juga dapat membuat **AppVM** default, seperti **personal**, **work**, **untrusted**, dan **vault**, untuk mengatur aktivitas Anda sesuai dengan tingkat kepercayaannya.



![0_15](assets/fr/15.webp)



Qubes OS juga memungkinkan Anda membuat **qube yang didedikasikan untuk perangkat USB** (sys-usb) dan mengonfigurasi **Qubes Whonix Gateway dan Workstation** untuk mengamankan komunikasi Anda melalui jaringan Tor. Untuk pengguna tingkat lanjut, bagian **Konfigurasi lanjutan** memungkinkan Anda membuat **LVM thin pool** untuk mengelola ruang disk secara efisien di antara qubes.



Setelah semua opsi ini dikonfigurasikan, klik **Selesai**, kemudian **Selesai konfigurasi**. Tunggu sementara sistem menerapkan pengaturan ini. Anda kemudian akan diminta untuk **login ke akun pengguna Anda**, dan lingkungan Qubes OS Anda akan siap untuk digunakan, aman dan terisolasi dengan baik untuk berbagai aktivitas Anda.



![0_17](assets/fr/17.webp)



Sistem operasi Anda sekarang telah terinstal dan siap digunakan.



![0_18](assets/fr/18.webp)



## Membuat qube pada sistem Anda



Untuk membuat qube, prosesnya dikelola oleh alat **Qube Manager**, yang dapat diakses dari menu Start. Pada jendela alat, cukup klik ikon **Create qube** untuk membuka jendela konfigurasi baru. Pertama, masukkan nama untuk qube Anda, seperti "perso-web" atau "work", untuk mengidentifikasi penggunaannya.



Selanjutnya, Anda akan memilih **Type**, biasanya **AppVM** untuk tugas-tugas rutin, atau **DisposableVM** untuk penggunaan sementara. Sangat penting untuk memilih **Template** yang akan menjadi dasar qube Anda, seperti "fedora-39" atau "debian-12", karena ini akan menyediakan sistem operasi dan perangkat lunak. Anda juga akan menunjuk **NetVM**, yang merupakan qube yang bertanggung jawab untuk akses Internet, secara default **sys-firewall**.



Terakhir, setelah menyesuaikan ukuran penyimpanan dan RAM jika perlu, klik **OK** akan meluncurkan proses pembuatan. Setelah proses selesai, qube baru Anda akan terlihat dalam daftar dan siap digunakan.



Kesimpulannya, Qubes OS bukanlah sistem operasi biasa, tetapi solusi keamanan mutakhir yang memikirkan kembali arsitektur komputer pribadi. Pendekatannya, yang didasarkan pada kompartementalisasi dan isolasi melalui virtualisasi, menawarkan perlindungan yang tak tertandingi terhadap ancaman yang paling canggih. Dengan mengelompokkan lingkungan kerja ke dalam qubes khusus untuk setiap tugas, ini memastikan bahwa malware tidak dapat menyebar dan membahayakan seluruh sistem.



Apakah Anda perlu menjelajahi web dengan aman, melindungi informasi sensitif, atau bekerja dengan berbagai tingkat kepercayaan, Qubes OS menyediakan kerangka kerja yang tangguh dan transparan. Dengan mengadopsi praktik-praktik yang baik dan memanfaatkan fitur-fiturnya secara maksimal, Anda akan memiliki **benteng digital** yang disesuaikan dengan ancaman-ancaman modern. Pelajari lebih lanjut tentang melindungi data dan privasi Anda.



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1