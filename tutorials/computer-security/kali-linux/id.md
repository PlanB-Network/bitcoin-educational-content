---
name: Kali
description: Menginstal Kali Linux di VirtualBox, sebagai stik USB yang dapat di-boot, atau sebagai dual boot, langkah demi langkah.
---

![cover-kali](assets/cover.webp)



## Pendahuluan



### Mengapa Kali Linux?



**Kali Linux** adalah distribusi Linux yang mengkhususkan diri pada keamanan TI.


Inilah alasan kami menggunakan Kali Linux:





- Alat ini sudah dikonfigurasikan dengan berbagai alat pentesting (uji keamanan sistem dan jaringan).
- Ini adalah **sumber terbuka dan gratis**, sehingga Anda dapat menggunakan dan memodifikasinya dengan bebas.
- Ini **dapat diandalkan dan aman**, ideal untuk belajar tentang keamanan siber.
- Ini memungkinkan Anda untuk mempelajari cara menggunakan Linux dalam lingkungan yang siap uji coba.
- Ini dapat diinstal dengan berbagai cara: **VirtualBox**, **kunci USB yang dapat di-boot**, atau **boot ganda**.



## Instalasi dan konfigurasi



### 1. Prasyarat



**Peralatan yang dibutuhkan:**





- prosesor 64-bit** (Intel atau AMD).
- minimum RAM 8 GB** (4 GB mungkin cukup untuk instalasi ringan atau VM).
- ruang disk kosong 50 GB** untuk menginstal Kali Linux.
- Koneksi internet** untuk mengunduh citra ISO dan pembaruan.
- Kunci USB minimal 8 GB** untuk membuat media yang dapat di-booting (jika Anda ingin menginstal Kali di PC atau mengujinya di Live USB).



Penting untuk mencadangkan data Anda sebelum menginstal pada PC yang sudah ada.



### 2. Unduh





- Kunjungi [kali.org/get-kali](https://www.kali.org/get-kali/#kali-platforms)
- Pilih gambar ISO untuk aplikasi Anda:
  - Instal Gambar** : untuk instalasi PC.
  - Gambar Virtual**: untuk menginstal Kali di VirtualBox atau VMware.
- Unduh gambar ISO.



![Page de téléchargement Kali](assets/fr/01.webp)



![Sélection de la version Kali](assets/fr/02.webp)



### 3. Membuat kunci USB yang dapat di-boot



Anda dapat menggunakan beberapa alat bantu, seperti Balena Etcher :





- Unduh dan instal [Balena Etcher](https://etcher.balena.io/).



![Page de téléchargement Balena Etcher](assets/fr/03.webp)



![Installation de Balena Etcher](assets/fr/04.webp)





- Buka Balena Etcher, kemudian pilih gambar ISO Kali.
- Pilih kunci USB sebagai media tujuan.
- Klik Flash dan tunggu sampai prosesnya selesai.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### 4. Menginstal dan mengamankan Kali Linux



#### 4.1 Mem-boot pada kunci USB





- Matikan komputer.
- Colokkan kunci USB (berisi Kali Linux).
- Hidupkan komputer Anda. Pada PC terbaru, sistem akan secara otomatis mengenali kunci boot USB. Jika tidak demikian, lakukan boot ulang dengan menahan tombol akses BIOS/UEFI (biasanya F2, F12 atau Delete, tergantung pada merek).
  - Dalam menu BIOS/UEFI, pilih kunci USB Anda sebagai perangkat boot.
  - Simpan dan mulai ulang.



#### 4.2 Meluncurkan penginstalan



##### Layar pengaktifan



Saat mem-boot dari stik USB, layar boot Kali Linux akan muncul. Pilih antara **instalasi grafis** dan **instalasi teks**. Dalam contoh ini, kami memilih instalasi grafis.



![capture](assets/fr/06.webp)



Jika Anda menggunakan gambar **Live**, Anda akan melihat mode lain, **Live**, yang juga merupakan opsi pengaktifan default.



![Mode Live](assets/fr/07.webp)



##### Pemilihan bahasa



Pilih bahasa yang Anda sukai untuk instalasi dan sistem.



![Sélection de la langue](assets/fr/08.webp)



Silakan tentukan lokasi geografis Anda.



![Options d'accessibilité](assets/fr/09.webp)



##### Konfigurasi keyboard



Pilih tata letak keyboard Anda. Bidang uji tersedia untuk memeriksa apakah tombol-tombol tersebut sesuai dengan konfigurasi Anda.



![Configuration du clavier](assets/fr/10.webp)



##### Koneksi jaringan



Instalasi sekarang akan memindai antarmuka jaringan Anda, mencari layanan DHCP, lalu meminta Anda memasukkan nama host untuk sistem Anda. Pada contoh di bawah ini, kita telah memasukkan **"kali "** sebagai nama host.



![Configuration réseau](assets/fr/11.webp)



Anda dapat secara opsional memberikan nama domain default yang akan digunakan sistem ini (nilai dapat diambil dari DHCP atau jika sistem operasi yang sudah ada).



![Choix du type d'installation](assets/fr/12.webp)



##### Akun pengguna



Selanjutnya, buat akun pengguna untuk sistem (nama lengkap, nama pengguna, dan kata sandi yang kuat).



![Création d'un utilisateur](assets/fr/13.webp)



![Mode d'installation](assets/fr/14.webp)



![Sélection des applications](assets/fr/15.webp)



##### Zona waktu



Pilih area geografis Anda untuk mengatur waktu sistem.



![Sélection du fuseau horaire](assets/fr/16.webp)



##### Jenis partisi



Penginstal kemudian memindai disk Anda dan menampilkan beberapa opsi, tergantung konfigurasi Anda.



Dalam panduan ini, kita mulai dari **disk kosong**, yang memberikan **empat pilihan yang memungkinkan**.


Kita akan memilih **Guided - use entire disk**, karena di sini kita akan melakukan instalasi Kali Linux sekali saja (single boot). Ini berarti tidak ada sistem operasi lain yang akan dipertahankan, dan seluruh disk dapat dihapus.



Jika disk Anda telah berisi data, opsi tambahan **Guided - use largest contiguous free space** mungkin akan ditampilkan.



Alternatif ini memungkinkan Anda untuk menginstal Kali Linux tanpa menghapus data yang ada, membuatnya ideal untuk dual booting dengan sistem lain.



Dalam kasus kami, disk kosong, jadi opsi ini tidak muncul.



![Choix du partitionnement](assets/fr/17.webp)



Pilih disk yang akan dipartisi.



![capture](assets/fr/18.webp)



Tergantung pada kebutuhan Anda, Anda dapat memilih untuk menyimpan semua file dalam satu partisi (perilaku default) atau memiliki partisi terpisah untuk satu atau beberapa direktori tingkat atas.



Jika Anda tidak yakin dengan apa yang Anda inginkan, pilih opsi **Semua file dalam satu partisi**.



![capture](assets/fr/19.webp)



![capture](assets/fr/20.webp)



Anda kemudian akan memiliki satu kesempatan terakhir untuk memeriksa konfigurasi disk Anda sebelum program instalasi membuat perubahan yang tidak dapat diubah. Setelah Anda mengklik _Continue_, program instalasi akan diluncurkan dan instalasi akan hampir selesai.



![capture](assets/fr/21.webp)



##### LVM terenkripsi



Jika opsi ini diaktifkan pada langkah sebelumnya, Kali Linux sekarang akan melakukan penghapusan hard disk yang aman sebelum meminta kata sandi LVM.



Gunakan kata sandi yang kuat, jika tidak, peringatan tentang passphrase yang lemah akan ditampilkan.



##### Informasi proxy



Kali Linux menggunakan repositori untuk mendistribusikan aplikasi. Anda harus memasukkan informasi proxy yang diperlukan jika lingkungan Anda menggunakannya.



Jika Anda **tidak yakin** apakah akan menggunakan proxy, **kosongkan**. Memasukkan informasi yang salah akan mencegah koneksi ke repositori.



![capture](assets/fr/22.webp)



##### Metapet



Jika akses jaringan belum dikonfigurasi, Anda perlu **konfigurasi lebih lanjut** saat diminta.



Jika Anda menggunakan gambar **Live**, langkah berikutnya tidak akan ditampilkan.



Anda kemudian dapat memilih [metapackages](https://www.kali.org/docs/general-use/metapackages/) yang ingin Anda instal. Opsi default akan menginstal sistem Kali Linux standar, sehingga Anda tidak perlu memodifikasi apa pun.



![capture](assets/fr/23.webp)



#### Informasi awal



Kemudian konfirmasikan pemasangan boot loader GRUB.



![capture](assets/fr/24.webp)



##### Mulai ulang



Terakhir, klik Lanjutkan untuk memulai ulang instalasi Kali Linux yang baru.



![capture](assets/fr/25.webp)



#### 4.3 Memperbarui dan mengonfigurasi Kali Linux setelah instalasi



Memperbarui sistem Anda adalah langkah penting setelah instalasi baru. Anda memiliki dua opsi:



##### Opsi 1: Melalui antarmuka pengguna grafis (GUI)



Kali, seperti Debian/Ubuntu, menawarkan pengelola pembaruan grafis yang terintegrasi.



1. Klik **menu utama** (kiri atas atau bawah, tergantung desktop Anda).


2. Buka **"Pembaruan Perangkat Lunak "**.


3. Alat ini akan :




    - Periksa paket yang akan diperbarui.
    - Anda akan melihat daftar (dengan ukuran dan versi).
    - Memungkinkan Anda meluncurkan pembaruan dengan sekali klik.


4. Masukkan kata sandi administrator Anda (`sudo`) saat diminta.


5. Biarkan menginstal dan mulai ulang jika perlu.



##### Opsi 2: Melalui terminal



Buka terminal dan jalankan :



```bash
# Mettre à jour les dépôts et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyage
sudo apt autoremove -y && sudo apt autoclean
```



Tidak disarankan untuk menggunakan akun **root** untuk pekerjaan sehari-hari; buatlah pengguna non-root sebagai gantinya.



Pada terminal Anda, ketikkan perintah berikut ini:



```bash
sudo adduser yourname
sudo usermod -aG sudo yourname
```



Keluar dan masuk kembali dengan pengguna baru.



Mari kita rangkum beberapa tugas dasar Kali Linux dalam sebuah tabel.



### Tugas-tugas dasar di bawah Kali Linux




| **Kategori** | **Tugas Dasar** | **Deskripsi / Tujuan** | **Metode Utama** |
| -------------------------- | -------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| **Navigasi Sistem** | Buka terminal | Mengakses baris perintah utama Kali | Klik ikon terminal atau gunakan `Ctrl + Alt + T` |
| | Telusuri folder | Berpindah dalam struktur direktori sistem | `cd /jalur/ke/folder`, `ls` untuk daftar file |
| | Buat / hapus folder | Mengatur file | `mkdir nama_folder`, `rm -r nama_folder` |
| **Manajemen File** | Salin / pindahkan file | Memanipulasi file di terminal | `cp file tujuan`, `mv file tujuan` |
| | Hapus file | Membebaskan ruang disk | `rm nama_file` |
| | Tampilkan isi file teks | Membaca file dengan cepat | `cat file.txt`, `less file.txt` |
| **Manajemen Sistem** | Perbarui Kali Linux | Menginstal versi terbaru dan patch keamanan | `sudo apt update && sudo apt full-upgrade -y` |
| | Instal perangkat lunak | Menambahkan alat atau utilitas baru | `sudo apt install nama_paket` |
| | Hapus perangkat lunak | Membersihkan sistem | `sudo apt remove nama_paket` |
| | Bersihkan dependensi yang tidak perlu | Menghemat ruang disk | `sudo apt autoremove` |
| **Jaringan dan Internet** | Periksa koneksi jaringan | Menguji akses internet | `ping google.com` |
| | Identifikasi alamat IP | Mengetahui konfigurasi jaringan Anda | `ip a` atau `ifconfig` |
| | Ganti jaringan Wi-Fi | Terhubung ke titik akses lain | Ikon jaringan → Pilih Wi-Fi yang diinginkan |
| **Akun dan Izin** | Jalankan perintah administrator | Mendapatkan hak akses root sementara | `sudo perintah` |
| | Buat pengguna baru | Menambahkan akun lokal | `sudo adduser nama_pengguna` |
| | Ubah kata sandi | Mengamankan akun | `passwd` |
| **Tampilan dan Kenyamanan** | Ganti wallpaper | Personalisasi desktop | Klik kanan pada desktop → **Pengaturan Desktop** |
| | Ubah tema / ikon | Meningkatkan keterbacaan dan estetika | Pengaturan → Tampilan / Tema |
| **Alat Kali** | Buka menu alat | Menjelajahi alat pengujian dan keamanan | Menu **Aplikasi → Kali Linux** |
| | Jalankan alat (cth: nmap, wireshark) | Penemuan praktis utilitas keamanan | `sudo nmap`, `wireshark`, dll. |
| **Bantuan dan Dokumentasi** | Dapatkan bantuan perintah | Memahami perintah sebelum menggunakannya | `man perintah` atau `perintah --help` |

## Kesimpulan



Menginstal Kali Linux hanyalah langkah pertama untuk menemukan lingkungan yang kuat yang didedikasikan untuk keamanan siber. Dengan menguasai tugas-tugas dasar dan manajemen sistem, semua orang dapat mulai menjelajahi alat bantu bawaan dan memahami cara kerja sistem Linux. Kali menawarkan platform pembelajaran yang sangat baik, baik untuk memperkuat keterampilan teknis maupun mengembangkan budaya keamanan TI yang sesungguhnya.