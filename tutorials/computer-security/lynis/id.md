---
name: Lynis
description: Melakukan audit keamanan mesin Linux dengan Lynis
---
![cover](assets/cover.webp)
___

*Tutorial ini didasarkan pada konten asli oleh Fares CHELLOUG yang dipublikasikan di [IT-Connect](https://www.it-connect.fr/). Lisensi [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Perubahan mungkin telah dilakukan pada teks asli.*
___

## I. Presentasi

Dalam tutorial ini, kita akan belajar cara melakukan audit keamanan pada komputer Linux menggunakan Lynis! Bagi Anda yang belum mengenal _Lynis_, yaitu sebuah aplikasi utilitas sederhana berbasis command line yang akan menganalisis konfigurasi server Anda dan memberikan rekomendasi untuk _meningkatkan keamanan komputer Anda_.

Lynis adalah aplikasi open source dari CISOFY, sebuah perusahaan yang berspesialisasi dalam _audit dan pertahanan sistem_. Jika Anda ingin membuat kemajuan dalam memperkuat Linux dan layanan populer (SSH, Apache2, dll.), Lynis adalah pilihan Anda! Lynis tidak hanya memberi tahu Anda apa yang salah, tetapi juga memberikan rekomendasi untuk mengarahkan Anda ke arah yang benar (dan menghemat waktu Anda).

**Lynis** berfungsi pada sebagian besar distribusi Linux, termasuk: **Debian, FreeBSD, HP-UX, NetBSD, NixOS, OpenBSD, Solaris**. Lynis ditujukan untuk pengguna Linux/UNIX, tetapi juga kompatibel dengan **macOS**. Pemasangannya sangat cepat, tidak ada manajemen dependensi pada tingkat paket.

Lynis digunakan untuk berbagai tujuan:

- Audit keamanan
- Pengujian kepatuhan (PCI, HIPAA, dan SOX)
- Konfigurasi sistem yang lebih tangguh
- Deteksi kerentanan

Alat ini digunakan secara luas oleh berbagai macam pengguna, termasuk administrator sistem, auditor TI, dan pentester. Untuk analisis, alat ini didasarkan pada standar seperti **CIS Benchmark, NIST, NSA, OpenSCAP** dan pada rekomendasi resmi dari **Debian, Gentoo, Red Hat**.

Aplikasi ini banyak digunakan oleh berbagai pengguna, termasuk administrator sistem, auditor IT, dan pentesters. Untuk analisis, aplikasi ini didasarkan pada standar seperti **CIS Benchmark, NIST, NSA, OpenSCAP**, dan pada rekomendasi resmi dari **Debian, Gentoo, Red Hat**.

Proyek ini tersedia di kink ini di **Github**:

- [GitHub - Lynis](https://github.com/CISOfy/lynis)
- [Unduh Lynis dari CISOFY](https://cisofy.com/lynis/#download)

Dalam tutorial langkah demi langkah ini, saya akan **menggunakan VPS yang menjalankan Debian 12** dan saya akan berkonsentrasi pada bagian SSH, karena saya ingin memeriksa konfigurasinya dan memperbaikinya.

## II. Pengunduhan dan pemasangan

Ada beberapa cara untuk mengunduh dan menginstal Lynis. Pilih salah satu yang Anda sukai dari daftar di bawah ini.

### A. Instalasi dari repositori Debian

Mode instalasi ini memungkinkan Anda untuk menggunakan perintah **lynis** dari mana saja pada sistem, tidak seperti instalasi dari sumber, di mana Anda harus berada di direktori.

Sambungkan ke server Anda melalui SSH dan masukkan perintah berikut untuk menginstal LYNIS:

```
sudo apt-get update
sudo apt-get install lynis -y
```

Inilah yang Anda dapatkan:

![Image](assets/fr/024.webp)

### B. Unduh dari situs web resmi

Anda juga dapat mengunduhnya dari situs web Cisofy:

```
sudo wget https://downloads.cisofy.com/lynis/lynis-3.0.9.tar.gz
```

Inilah yang Anda dapatkan:

![Image](assets/fr/032.webp)

Selanjutnya, kita akan membuka arsip menggunakan perintah berikut:

```
sudo tar -zxf lynis-3.0.9.tar.gz
```

Inilah yang Anda dapatkan:

![Image](assets/fr/020.webp)

Mari kita pindah ke folder **lynis**:

```
cd lynis
```

Kita dapat memeriksa pembaruan dengan perintah berikut:

```
./lynis update info
```

Inilah yang Anda dapatkan:

![Image](assets/fr/023.webp)

### C. Unduh dari GitHub

Kita akan mengunduh **Lynis** dari repositori resmi GitHub, menggunakan perintah berikut (*git* harus ada di komputer Anda):

```
git clone https://github.com/CISOfy/lynis.git
```

Inilah yang Anda dapatkan:

![Image](assets/fr/060.webp)

## III. Menggunakan Lynis

Lynis sudah terinstall di komputer kita, jadi mari kita pelajari cara menggunakannya!

### A. Kontrol dan opsi utama

Untuk menampilkan perintah yang tersedia, cukup masukkan perintah berikut ini:

```
sudo lynis
# Si vous avez récupéré Lynis depuis les sources, utilisez cette syntaxe:
./lynis
```

Inilah yang Anda dapatkan:

![Image](assets/fr/039.webp)

Dan Anda juga mendapatkan opsi berikut ini:

![Image](assets/fr/040.webp)

Untuk menampilkan semua perintah yang tersedia, masukkan perintah berikut:

```
sudo lynis show
```

Inilah yang Anda dapatkan:

![Image](assets/fr/022.webp)

Jika Anda ingin menampilkan semua opsi, Anda harus memasukkan :

```
sudo lynis show options
```

Inilah yang Anda dapatkan:

![Image](assets/fr/021.webp)

Dalam sisa artikel ini, kita akan belajar cara menggunakan opsi tertentu.

### B. Melakukan audit sistem

Kita akan meminta **Lynis** untuk mengaudit sistem kita, menyoroti apa yang telah dikonfigurasi dengan benar dan apa yang perlu ditingkatkan. Untuk melakukannya, masukkan perintah berikut:

```
sudo lynis audit system
# ou
./lynis audit system
```

Secara default, jika Anda tidak masuk sebagai root saat menjalankan perintah ini, aplikasi ini akan berjalan dengan hak akses pengguna yang sedang masuk. Beberapa tes tidak akan dijalankan dalam konteks ini:

![Image](assets/fr/052.webp)

Berikut ini adalah pengujian yang tidak akan dilakukan dalam mode ini:

![Image](assets/fr/051.webp)

Setelah perintah dijalankan, analisis dimulai. Tunggu sebentar.

Pada akhir audit, Anda akan mendapatkan ini (kita dapat melihat bahwa **Lynis** telah mengidentifikasi sistem **Debian 12** dengan benar dan akan menggunakan **plugin Debian** untuk analisis):

![Image](assets/fr/017.webp)

Selanjutnya, Lynis akan membuat daftar serangkaian poin yang sesuai dengan semua yang telah dia periksa pada sistem kami. Ini disusun berdasarkan kategori, seperti yang akan kita lihat. Perlu juga dicatat bahwa kode warna digunakan untuk menyoroti rekomendasi:





- **Merah** untuk Elements kritis atau praktik terbaik yang tidak dipatuhi (paket yang hilang, misalnya), yaitu server Anda tidak mematuhi poin ini
- **Kuning** untuk saran atau kepatuhan sebagian terhadap rekomendasi (misalnya, mematuhi poin yang disorot dengan warna ini adalah nilai tambah (bukan prioritas))
- **Green** untuk titik-titik di mana konfigurasi server Anda sesuai
- **Putih**, bila netral

Selanjutnya, Lynis akan membuat daftar serangkaian poin yang sesuai dengan semua yang telah diperiksanya pada sistem kita. Ini disusun berdasarkan kategori, seperti yang akan kita lihat. Penting juga untuk dicatat bahwa kode warna digunakan untuk menyoroti rekomendasi:

- Merah: Untuk elemen kritis atau prosedur yang tidak dilakukan (misalnya, paket yang hilang), yaitu server Anda tidak mematuhi poin ini.
- Kuning: Untuk saran atau kepatuhan sebagian terhadap rekomendasi (bisa dibilang ini adalah nilai tambah untuk memenuhi poin yang disoroti dengan warna ini (non-prioritas)).
- Hijau: Untuk poin di mana konfigurasi server Anda sudah sesuai.
- Putih: Ketika netral.

Di sini, kita bisa melihat bahwa Lynis merekomendasikan untuk menginstal **fail2ban**:

![Image](assets/fr/057.webp)

Pada bagian "**Boot and services**", kita melihat bahwa perlindungan layanan melalui *systemd* dapat ditingkatkan. Sisi positifnya, Grub2 hadir dan tidak ada masalah dengan izin pada :

Di bagian "**Boot and services**", kita melihat bahwa perlindungan layanan melalui _systemd_ perlu ditingkatkan. Di sisi positif, Grub2 sudah ada dan tidak ada masalah dengan izin pada:

![Image](assets/fr/029.webp)

Kemudian Anda memiliki bagian "**Kernel**" dan "**Memory and Processes**":

![Image](assets/fr/037.webp)

Selanjutnya, bagian "**Users, Groups and Authentication**". Aplikasi ini menginformasikan kepada kita tentang peringatan pada izin direktori "**/etc/sudoers.d**". Untuk saat ini, kita tidak tahu lebih banyak, tetapi kita akan dapat melihat rekomendasinya di akhir analisis.

![Image](assets/fr/049.webp)

Berikut ini adalah apa yang dapat Anda temukan di bagian "**Shells", "Files Systems", dan "USB Devices "**. Di antaranya, kita dapat melihat bahwa ada saran mengenai titik pemasangan dan bahwa perangkat USB saat ini diizinkan pada komputer ini.

![Image](assets/fr/048.webp)

Selanjutnya, bagian: "**Name services", "Port dan packages", "Networking".** Di sini menunjukkan bahwa paket yang tidak lagi digunakan dapat dihapus dan tidak ada utilitas yang mampu mengelola pembaruan otomatis.

![Image](assets/fr/058.webp)

Kita dapat melihat bahwa firewall diaktifkan (dan ya, ada iptables!). Selain itu, kita dapat melihat bahwa telah ditemukan aturan yang tidak digunakan dan server web Apache sudah terinstal.

![Image](assets/fr/055.webp)

Ini diikuti dengan analisis server web itu sendiri, karena layanan telah diidentifikasi.

Kita dapat melihat bahwa telah ditemukan file konfigurasi **Nginx**, dan untuk bagian SSL/TLS, **cipher** dikonfigurasikan dengan menggunakan protokol yang tidak aman. Di sisi lain, menurut Lynis, manajemen log sudah benar.

![Image](assets/fr/038.webp)

Layanan SSH ada pada server VPS saya. Konfigurasinya dianalisis oleh Lynis. Harus dikatakan bahwa keamanan SSH dapat dengan mudah ditingkatkan! Kita akan kembali ke area ini secara mendetail setelah kita mendapatkan rekomendasinya.

![Image](assets/fr/026.webp)

Berikut ini adalah bagian **"Dukungan SNMP", "Database", "PHP", "Dukungan Squid", "Layanan LDAP", "Pencatatan dan file"**.

Ada satu saran yang sangat penting tentang manajemen log: sangat disarankan agar Anda tidak hanya menyimpan log secara lokal pada komputer Anda. Jika komputer dirusak oleh penyerang, kemungkinan besar dia akan mencoba menghapus jejaknya... Jadi kita perlu mengeksternalisasi log.

![Image](assets/fr/050.webp)

Di sini, kita memiliki audit untuk layanan yang rentan, manajemen akun, tugas terjadwal, dan sinkronisasi NTP. Ditunjukkan bahwa tingkatnya rendah pada bagian banner dan identifikasi: ini dapat dimengerti, karena jika Anda menampilkan versi sistem, itu memberikan indikasi kepada penyerang sistem. Ini adalah pengaturan default.

Akan menarik untuk mengaktifkan **auditd** untuk memiliki log untuk melakukan **analisis forensik**. **NTP** juga diperiksa, karena untuk mencari log secara efisien, lebih baik memiliki sistem yang tepat waktu, yang menyederhanakan pencarian.

![Image](assets/fr/036.webp)

Lynis kemudian melihat elemen kriptografi, virtualisasi, kontainer, dan kerangka kerja keamanan. Beberapa bagian kosong karena tidak ada korespondensi dengan mesin yang dianalisis. Namun, kita bisa melihat bahwa saya memiliki dua sertifikat SSL yang sudah kedaluwarsa dan saya belum mengaktifkan **SELinux**.

Lynis kemudian memeriksa elemen kriptografi, virtualisasi, kontainer, dan kerangka kerja keamanan. Beberapa bagian kosong karena tidak ada kesesuaian dengan komputer yang dianalisis. Namun, kita dapat melihat bahwa saya memiliki dua sertifikat SSL yang kedaluwarsa dan saya belum mengaktifkan **SELinux**.

![Image](assets/fr/027.webp)

Di sini juga ada hal yang harus diperbaiki: tidak ada pemindai anti-virus atau anti-malware, dan ada saran mengenai izin file.

![Image](assets/fr/028.webp)

Lynis selanjutnya berfokus pada pengetatan konfigurasi kernel Linux (termasuk aturan untuk stack IPv4), serta manajemen direktori "Home" pada komputer Linux.

![Image](assets/fr/035.webp)

Kita telah sampai di akhir analisis... Poin terakhir ini menunjukkan bahwa kita akan mendapatkan keuntungan besar dengan memiliki ClamAV pada komputer ini.

![Image](assets/fr/030.webp)

## IV. Rekomendasi

Setelah audit, saatnya untuk membaca dan menganalisis rekomendasi. Di sinilah kita mendapatkan rekomendasi dan penjelasan untuk setiap tes yang dilakukan oleh Lynis.

Sebagai contoh, lihatlah rekomendasi SSH. **Untuk setiap saran, Anda akan menemukan parameter yang direkomendasikan dan tautan yang akan menjelaskan poin keamanan**. Keputusan ada pada Anda, tergantung pada konteks dan penggunaan Anda.

Mari kita lihat beberapa contoh rekomendasi yang secara langsung memaparkan poin-poin yang disoroti di seluruh audit...

### A. Contoh rekomendasi

- Seperti yang kita lihat sebelumnya, NTP penting untuk time stamp log:

![Image](assets/fr/043.webp)

- Lynis juga menyarankan untuk memasang paket **apt-listbugs** untuk mendapatkan informasi tentang kelemahan fatal  selama pemasangan paket melalui **apt**.

![Image](assets/fr/041.webp)

- Aplikasi ini menyarankan kita untuk memasang **needrestart** agar dapat melihat proses mana yang menggunakan versi lama dari library dan perlu restart.

![Image](assets/fr/054.webp)

- Saran ini menyarankan untuk menginstal **fail2ban** agar secara otomatis memblokir host yang gagal diautentikasi (terutama serangan brute force).

![Image](assets/fr/044.webp)

- Untuk memperkuat layanan sistem, kita direkomendasikan menjalankan perintah yang disorot dengan warna biru untuk setiap layanan di komputer kita.

![Image](assets/fr/056.webp)

- Disarankan untuk menetapkan tanggal kedaluwarsa untuk semua kata sandi akun yang dilindungi.

![Image](assets/fr/031.webp)

- Disarankan untuk menetapkan nilai minimum dan maksimum untuk usia kata sandi. Antara lain, hal ini akan memastikan bahwa kata sandi diubah secara teratur.

![Image](assets/fr/042.webp)

- Direkomendasikan untuk menggunakan partisi terpisah, untuk membatasi dampak masalah ruang disk pada satu partisi.

![Image](assets/fr/047.webp)

- Rekomendasi ini menyarankan untuk menonaktifkan penyimpanan USB dan firewire untuk mencegah kebocoran data.

![Image](assets/fr/033.webp)

- Untuk memenuhi rekomendasi ini, cukup pasang dan konfigurasikan **unattended-upgrade**, sebagai contoh.

![Image](assets/fr/053.webp)

### B. Menginstal paket yang direkomendasikan

Untuk meningkatkan konfigurasi sistem, kita akan memasang beberapa paket di komputer: beberapa direkomendasikan oleh Lynis, beberapa saya rekomendasikan secara pribadi.

Anda akan memiliki dasar yang baik untuk dikerjakan, asalkan Anda meluangkan sedikit waktu untuk mengonfigurasinya. Untuk melakukan ini, lihat situs IT-Connect, artikel lain di web, dan dokumentasi aplikasi.

```
sudo apt-get install debsums apt-listbugs needrestart apt-show-versions fail2ban unattended-upgrades clamav clamav-daemon rkhunter
```

Beberapa informasi tentang paket yang diinstal :

- **Clamav** adalah sebuah antivirus.
- **unattend-upgrades** akan memungkinkan Anda untuk mengelola pembaruan secara otomatis dan bahkan me-reboot komputer atau secara otomatis menghapus paket lama, sepenuhnya dapat dikonfigurasi.
- **rkhunter** adalah anti-rootkit yang memindai sistem file Anda.
- **Fail2ban** akan berkerja dengan sendirinya pada file log Anda sesuai dengan apa yang Anda berikan untuk dibaca dan akan bekerja dengan **iptables**, misalnya untuk memblokir alamat IP yang mencoba melakukan "brute force" server SSH Anda.

### C. Rekomendasi untuk SSH

Mari kita lihat rekomendasi SSH. Rekomendasi tersebut tercantum di bawah ini. Jangan khawatir, kita akan segera menjelaskan cara meningkatkan konfigurasinya.

![Image](assets/fr/034.webp)



Mari kita lihat lebih dekat konfigurasi **SSH** saya saat ini di:**/etc/ssh/sshd_config**

![Image](assets/fr/018.webp)

Konfigurasi yang disarankan di bawah ini masih dapat dioptimalkan, tetapi ini sudah memberikan Anda dasar yang baik. _Harap diperhatikan bahwa saya telah menghapus sejumlah komentar agar lebih mudah dibaca_.

Kita akan melakukannya:

- Ubah port koneksi SSH (lupakan port 22 default)
- Kita akan mengatur level verbositas log, dari **INFO menjadi VERBOSE**.
- Mengatur **LoginGraceTime** ke **2 menit**.

Jika tidak ada informasi koneksi yang dimasukkan dalam waktu dua menit, koneksi akan terputus.

- Aktifkan **strictModes**

Menentukan apakah "sshd" harus memeriksa mode dan pemilik file pengguna serta direktori Home pengguna sebelum memvalidasi koneksi. Ini sangat dianjurkan, karena terkadang pemula secara tidak sengaja membiarkan direktori atau file mereka dapat diakses sepenuhnya oleh semua orang. Nilai bawaannya adalah "yes".

- Tetapkan **MaxAuthtries** ke 3

Ini menunjukkan jumlah upaya autentikasi yang gagal sebelum komunikasi ditutup.

- Tetapkan **MaxSessions** ke 2

Ini merupakan jumlah maksimum sesi simultan.

- Mengaktifkan autentikasi public key

```
PubkeyAuthentication yes
```





- Mempertahankan otentikasi kata sandi:

```
PasswordAuthentication yes
```

Melarang kata sandi kosong dan autentikasi **Kerberos**, serta **autentikasi root langsung**

```
PermitEmptyPasswords no
PermitRootLogin no
```



Pastikan Anda memiliki **"PermitRootLogin no"**, jika sama dengan **"yes"**, itu adalah **"absolute evil"**.





- Melarang pengalihan koneksi TCP

```
AllowTcpForwarding no
```

Menunjukkan apakah pengalihan TCP diizinkan, dengan nilai bawaan "yes". Perlu diketahui: menonaktifkan pengalihan TCP tidak meningkatkan keamanan jika pengguna memiliki akses ke shell, karena mereka masih dapat mengatur program pengalihan mereka sendiri.

- Melarang pengalihan X11

```
X11Forwarding no
```

Menunjukkan apakah pengalihan X11 diterima, dengan nilai bawaan "no". Perlu diketahui: bahkan jika pengalihan X11 dinonaktifkan, ini tidak meningkatkan keamanan, karena pengguna masih dapat mengatur program pengalih mereka sendiri. Pengalihan X11 secara otomatis dinonaktifkan jika **UseLogin** dipilih.

- Mengatur batas waktu komunikasi antara klien dan sshd

```
ClientAliveInterval  300
```

Menentukan batas waktu hitungan dalam detik, setelah itu, jika tidak ada data yang diterima dari klien, layanan sshd akan mengirimkan pesan yang meminta tanggapan dari klien. Secara bawaan, opsi ini diatur ke "0", yang berarti bahwa pesan-pesan ini tidak dikirim ke klien. Hanya protokol SSH versi 2 yang mendukung opsi ini.

```
ClientAliveCountMax 0
```

Menurut [dokumentasi (*man page*) untuk sshd](https://www.delafond.org/traducmanfr/man/man5/sshd_config.5.html), inilah arti opsi ini: "Mengatur jumlah pesan tertahan (lihat di atas) yang akan dikirim tanpa tanggapan dari klien untuk **sshd**. Jika ambang batas ini tercapai saat pesan hold telah dikirim, **sshd** akan memutuskan sambungan klien dan mengakhiri sesi. Penting untuk dicatat bahwa pesan hold ini sangat berbeda dari opsi KeepAlive (di bawah). Pesan hold koneksi dikirim melalui terowongan terenkripsi, dan oleh karena itu tidak dapat dipalsukan. Hold koneksi tingkat TCP yang diaktifkan oleh **KeepAlive** dapat dipalsukan. Mekanisme hold koneksi diperlukan ketika klien atau server perlu tahu apakah koneksi sedang tidak aktif."

- Mencegah pengungkapan informasi dengan menonaktifkan **motd, banner, lastlog**

```
PrintMotd no
```

Menentukan apakah sshd harus menampilkan isi file /etc/motd saat pengguna masuk dalam mode interaktif. Pada beberapa sistem, konten ini juga dapat ditampilkan oleh shell, melalui /etc/profile atau file serupa. Nilai bawaannya adalah "yes".

```
Banner none
```

Perlu dicatat bahwa di beberapa yurisdiksi, pengiriman pesan sebelum autentikasi mungkin merupakan prasyarat untuk perlindungan hukum. Isi file yang ditentukan akan dikirimkan ke pengguna jarak jauh sebelum otorisasi koneksi diberikan. Opsi ini perlu dikonfigurasi, karena secara bawaan tidak ada pesan yang akan ditampilkan.

Tampak pada gambar, ini menghasilkan:

![Image](assets/fr/019.webp)

### D. Skor audit



Terakhir, jangan lupa untuk memeriksa **skor audit Lynis**! Kita melihat bahwa **skor Hardening saya adalah 63** dan file laporannya dapat dilihat di "**/var/log/lynis-report.dat**". Ada juga file "**/var/log/lynis.log**".

**Dengan kata lain, semakin tinggi skornya, semakin baik!** Oleh karena itu, Anda perlu memperbaiki konfigurasi Anda untuk mencapai skor setinggi mungkin, sambil tetap memungkinkan komputer dan layanan yang di-hosting berfungsi normal (yang berarti melakukan uji fungsional).

![Image](assets/fr/046.webp)


Mari kita lihat hasilnya di server kedua saya, di mana saya menghabiskan lebih banyak waktu untuk memperkuatnya! Jadi wajar jika skornya lebih tinggi (**76**).

![Image](assets/fr/045.webp)

## V. Perencanaan otomatisasi Lynis

**Lynis** juga menawarkan opsi untuk menjalankan pemeriksaannya melalui tugas terjadwal. Ada opsi **"--cronjob "**, yang akan menjalankan semua tes Lynis tanpa perlu validasi atau tindakan pengguna. Anda kemudian dapat dengan mudah membuat skrip yang akan menjalankan **Lynis** dan menempatkan keluarannya dalam file dengan timestamp dan nama server yang bersangkutan. Berikut adalah contoh file semacam ini yang dapat Anda letakkan di folder */etc/cron.daily*:

```
#!/bin/sh
mkdir /var/log/lynis
NOM_AUDITEUR="tache_crontab"
DATE=$(date +%Y%m%d)
HOTE=$(hostname)
LOG_DIR="/var/log/Lynis"
RAPPORT="$LOG_DIR/rapport-${HOTE}.${DATE}"
DATA="$LOG_DIR/rapport-data-${HOTE}.${DATE}.txt"

cd /root/Lynis./Lynis -c --auditor "${NOM_AUDITEUR}" --cronjob > ${RAPPORT}
mv /var/log/lynis-report.dat ${DATA}
```

Variabel **"AUDITOR_NAME "** hanyalah sebuah variabel yang akan kita atur dalam opsi **"--auditor "** dari **Lynis** sehingga nama ini akan ditampilkan dalam laporan:

![Image](assets/fr/059.webp)

Kita juga akan membuat beberapa variabel kontekstual yang akan membantu kita mengaturnya dengan lebih baik, seperti nama host dan tanggal untuk menamai laporan dan memberikan timestamp, serta jalur ke folder tempat kita ingin menempatkan laporan kita.

## VI. Kesimpulan

Lynis adalah aplo yang sangat praktis yang akan membantu Anda menghemat waktu dan menjadi lebih efisien ketika Anda ingin tahu lebih banyak tentang keadaan konfigurasi server Linux, terutama dalam hal keamanan. Namun, jangan lupa bahwa setiap modifikasi harus diuji sebelum diterapkan dalam role production, dengan mempertimbangkan penggunaan dan konteks Anda sendiri.

Anda mungkin tidak akan menerapkan konfigurasi yang sama untuk VPS yang tersambung ke Net, di mana Anda hanya membutuhkan satu koneksi SSH (karena Anda adalah satu-satunya orang yang terhubung), tidak seperti **bastion** atau **scheduler** yang akan membutuhkan koneksi **SSH** yang berlipat ganda.

Setelah Anda mendapatkan konfigurasi yang cocok untuk Anda bisa memperkuatnya, disarankan untuk menggunakan aplikasi otomatisasi agar Anda tidak perlu mengulang tugas secara manual, karena ini akan memakan waktu dan rawan kesalahan. Misalnya, Anda dapat menggunakan: **Puppet, Chef, Ansible, dll.**

Jangan lupa untuk berkomunikasi dengan tim Anda sebelum implementasi: Anda perlu membuat mereka memahami mengapa Anda membuat perubahan ini, bukan hanya memberi tahu mereka bahwa Anda membuatnya. Pada akhirnya, tujuannya adalah untuk menyampaikan kebiasan-kebiasaan yang baik, dan ini akan meningkatkan peluang keberhasilan Anda.

Terakhir, Anda juga dapat membandingkan **Lynis** dengan aplikasi lain, yang ada beberapa di antaranya. Jika Anda ingin bergerak menuju manajemen terpusat sambil tetap open source, saya merekomendasikan aplikasi [Wazuh](https://wazuh.com/).

**Tutorial ini sudah selesai, selamat bersenang-senang dengan Lynis!**
