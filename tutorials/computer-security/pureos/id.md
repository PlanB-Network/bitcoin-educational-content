---
name: PureOS
description: Distribusi Linux yang memberi Anda kendali atas kehidupan digital Anda.
---

![cover](assets/cover.webp)



Melindungi informasi pribadi di era digital adalah prioritas utama bagi setiap pengguna Internet. Perusahaan, organisasi, dan bahkan sistem operasi adalah sumber informasi yang berguna untuk menentukan profil dan gaya hidup Anda. Memilih sistem operasi yang tepat adalah langkah pertama dalam memperkuat privasi online Anda. Dalam tutorial ini, kita akan melihat pada PureOS, distribusi Linux yang berfokus pada privasi.



https://planb.network/tutorials/computer-security/operating-system/debian-d09a57ec-8372-40ca-bcff-499415209e1f

## Memulai dengan PureOS



PureOS adalah sistem operasi berbasis Debian yang dikembangkan oleh Purism. PureOS cocok untuk para profesional TI dan pengguna yang mencari distribusi yang sederhana dan mudah digunakan. Sistem operasi ini unik karena merupakan *Free Software*, dan berfokus pada perlindungan data pribadi penggunanya dengan membuat kerangka kerja berdasarkan privasi, kebebasan, keamanan, dan stabilitas yang ditawarkan oleh Debian.



### Mengapa memilih PureOS?





- Interface yang sederhana dan intuitif**: GNOME menawarkan desktop Interface yang jelas, dirancang agar mudah digunakan, bahkan bagi mereka yang tidak nyaman dengan baris perintah.





- Gratis**: seperti kebanyakan distribusi Linux, PureOS sepenuhnya gratis untuk digunakan. Namun, tersedia langganan bulanan untuk mendukung para pengembang.





- Keamanan dan stabilitas**: Arsitektur dan mode operasi PureOS menjadikannya distribusi yang sangat aman, menjamin perlindungan data dan stabilitas sistem.





- Dokumentasi dan komunitas yang aktif**: PureOS memiliki dokumentasi yang jelas dan dapat diakses serta komunitas yang berkomitmen dan responsif, membuatnya mudah untuk memecahkan masalah dan mempelajari sistem selangkah demi selangkah.



## Instalasi dan konfigurasi



Menginstal dan mengonfigurasi PureOS di komputer Anda akan memerlukan fitur minimalis berikut ini:




- Kunci USB minimal 8GB untuk mem-flash sistem.
- rAM 4 GB.
- ruang kosong sebesar 30 GB pada disk Hard Anda.



Kunjungi [situs web resmi PureOS](https://pureos.net/) lalu unduh citra ISO sistem operasi sesuai dengan arsitektur mesin Anda.



Untuk meluncurkan instalasi PureOS, Anda perlu membuat kunci USB yang dapat di-boot menggunakan perangkat lunak flash seperti [Balena Etcher](https://www.balena.io/etcher).



Dalam tiga langkah mudah, Anda akan mendapatkan stik USB yang di-boot dengan sistem operasi PureOS.





- Colokkan kunci USB dan jalankan perangkat lunak Balena yang telah diunduh.
- Kemudian pilih gambar ISO PureOS
- Pilih kunci USB sebagai perangkat output, kemudian klik tombol **Flash** dan tunggu sampai prosesnya selesai.



![0_01](assets/fr/01.webp)



Setelah kunci USB di-boot, nyalakan ulang komputer yang ingin Anda instal PureOS.



Saat boot, akses BIOS dengan menekan tombol `ESC`, `F9`, atau `F11`, tergantung mesin Anda. Pilih tombol USB sebagai perangkat boot, lalu tekan `ENTER` untuk mengonfirmasi.



### Layar pengaktifan



PureOS menawarkan beberapa opsi untuk memulai sistem operasinya. Pilih opsi **Test atau Install PureOS** untuk meluncurkan instalasi sistem operasi.



![0_02](assets/fr/02.webp)



Atur bahasa dan tata letak keyboard yang ingin Anda gunakan di komputer.



![0_03](assets/fr/03.webp)



![0_04](assets/fr/04.webp)



Izinkan atau tolak akses ke **lokasi geografis** Anda ke aplikasi untuk mendapatkan rekomendasi yang dipersonalisasi berdasarkan area Anda.



![0_05](assets/fr/05.webp)



Anda dapat menyambung ke akun **NextCloud** yang sudah ada untuk mengambil data yang ditautkan ke office suite yang Anda gunakan di sistem lain.



![0_06](assets/fr/06.webp)



Tersedia tutorial, tetapi Anda bisa menutup jendela jika ingin melewatkan langkah ini.



![0_08](assets/fr/08.webp)



### Meluncurkan penginstalan



Klik menu **Activities** dan jelajahi aplikasi dan alat yang sudah terinstal pada sistem. Klik **Instal PureOS** untuk memulai penginstalan



![0_09](assets/fr/09.webp)



Atur bahasa sistem dan tata letak keyboard sesuai kebutuhan, lalu konfigurasikan mode partisi disk Hard.



![0_10](assets/fr/10.webp)



![0_11](assets/fr/11.webp)



![0_12](assets/fr/12.webp)



![0_13](assets/fr/13.webp)



Anda memiliki dua opsi untuk mempartisi disk Hard Anda:




- Hapus disk**: Untuk penginstalan lengkap PureOS, hapus semua data yang sudah ada sebelumnya pada disk Hard Anda.



![0_14](assets/fr/14.webp)





- Partisi Manual** untuk membuat skor Anda sendiri



⚠️ Saat Anda membuat partisi secara manual untuk sistem operasi, pastikan Anda mengalokasikan minimal 2 GB partisi untuk operasi PureOS dan kemudian partisi lain untuk data.



![0_15](assets/fr/15.webp)



Aktifkan **enkripsi disk** jika Anda ingin mengamankan data Anda. Masukkan kata sandi yang kuat dan rumit.



Kaitkan pengguna dengan sistem operasi Anda dengan menentukan nama pengguna dan kata sandi alfanumerik yang terdiri dari setidaknya 20 karakter untuk memperkuat keamanan data Anda.



![0_16](assets/fr/16.webp)



Tinjau pengaturan yang telah Anda buat dan modifikasi jika perlu.



![0_17](assets/fr/17.webp)



Klik **Instal** lalu **Instal Sekarang** untuk mengonfirmasi bahwa PureOS telah terinstal di komputer Anda.



![0_18](assets/fr/18.webp)



![0_19](assets/fr/19.webp)



Setelah instalasi selesai, centang kotak **Restart sekarang** untuk memulai ulang komputer Anda, lalu konfirmasikan:




- Bahasa.
- Tata letak keyboard.
- Akun NextCloud Anda (opsional).



![0_25](assets/fr/25.webp)



## Pembaruan



Sebelum Anda mulai menggunakan PureOS, sangat penting untuk memperbarui sistem Anda. Ini akan memungkinkan Anda mendapatkan manfaat dari fitur-fitur terbaru dan patch keamanan, dan memastikan stabilitas yang lebih baik.





- Pembaruan melalui grafik Interface**:


Buka aplikasi **Perangkat Lunak**, lalu buka tab **Pembaruan**. Pembaruan yang tersedia akan ditampilkan secara otomatis. Klik **Unduh**, lalu **Instal** setelah pengunduhan selesai.





- Perbarui melalui terminal**:


Buka terminal, lalu masukkan perintah berikut untuk memperbarui daftar paket yang tersedia:



```shell
sudo apt update
```



Masukkan kata sandi Anda dan konfirmasikan. Kemudian instal pembaruan dengan file:



```shell
sudo apt full-upgrade
```



## PureOS untuk pengembangan



Secara default, PureOS tidak menyertakan semua alat yang dibutuhkan untuk pengembangan.


Anda dapat menginstalnya dengan cepat dengan perintah berikut:



```shell
sudo apt install build-essential git curl
```



Ini akan menginstal alat kompilasi **Git** dan **Curl**, yang berguna di sebagian besar lingkungan pengembangan.



## Lingkungan PureOS



PureOS menonjol karena pendekatan inovatifnya terhadap konvergensi sejati: sistem operasi tunggal memastikan pengoperasian yang mulus dan lancar di berbagai perangkat, termasuk laptop, tablet, PC mini, dan ponsel cerdas.



Aplikasi PureOS dirancang untuk menjadi adaptif: aplikasi ini secara otomatis menyesuaikan diri dengan ukuran layar dan mode input (sentuh atau keyboard/mouse). Sebagai contoh, peramban Web GNOME secara dinamis mengadaptasi Interface untuk memberikan pengalaman optimal pada perangkat seluler dan desktop.



PureOS juga menyertakan paket perkantoran **LibreOffice**, yang mencakup:





- Writer**: pengolah kata lengkap untuk membuat dan mengedit dokumen.
- Calc**: program spreadsheet yang kuat untuk mengelola data dan perhitungan Anda.
- Impress**: alat bantu untuk membuat presentasi profesional.



Paket gratis ini memungkinkan Anda bekerja secara efisien tanpa harus bergantung pada perangkat lunak berpemilik.



PureOS menawarkan lingkungan yang terpadu, aman, dan fleksibel, berdasarkan distribusi open source 100% yang menjamin kontrol total dan penghormatan yang ketat terhadap privasi. Konvergensi yang sebenarnya memfasilitasi pembuatan aplikasi yang kompatibel dengan berbagai jenis perangkat, seperti komputer, tablet, dan ponsel cerdas, tanpa perlu adaptasi yang rumit.



Dengan akses asli ke alat penting, manajer paket yang kuat, dan ekosistem sumber terbuka yang kaya, PureOS menyederhanakan pengembangan, pengujian, dan penyebaran aplikasi dalam lingkungan yang aman. Arsitekturnya yang stabil dan Commitment untuk kerahasiaan menjadikannya platform yang andal untuk berbagai penggunaan, termasuk pengembangan Blockchain, pembuatan prototipe cepat, atau lingkungan produksi.



Temukan kursus kami untuk memperkuat keamanan dan melindungi privasi digital Anda.



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1