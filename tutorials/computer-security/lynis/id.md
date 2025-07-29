---
name: Lynis
description: Melakukan audit keamanan mesin Linux dengan Lynis
---
![cover](assets/cover.webp)



___



*Tutorial ini didasarkan pada konten asli oleh Fares CHELLOUG yang dipublikasikan di [IT-Connect](https://www.it-connect.fr/). Lisensi [CC BY-NC 4.0] (https://creativecommons.org/licenses/by-nc/4.0/). Perubahan mungkin telah dilakukan pada teks asli.*



___



## I. Presentasi



**Dalam tutorial ini, kita akan belajar cara melakukan audit keamanan pada mesin Linux menggunakan Lynis! Bagi Anda yang belum mengenal **Lynis,** ini adalah sebuah utilitas baris perintah kecil yang akan menganalisis konfigurasi server Anda dan membuat rekomendasi untuk **meningkatkan keamanan mesin Anda.**



Lynis adalah alat sumber terbuka dari CISOFY, sebuah perusahaan yang berspesialisasi dalam **audit dan pengerasan sistem**. Jika Anda ingin membuat kemajuan dalam mengeraskan Linux dan layanan populer (SSH, Apache2, dll.), Lynis adalah sekutu Anda! Lynis tidak hanya memberi tahu Anda apa yang salah, tetapi juga memberikan rekomendasi untuk mengarahkan Anda ke arah yang benar (dan menghemat waktu Anda).



**Lynis** dapat digunakan pada sebagian besar distribusi Linux, termasuk: **Debian, FreeBSD, HP-UX, NetBSD, NixOS, OpenBSD, Solaris**. Lynis ditujukan untuk pengguna Linux / UNIX, tetapi juga kompatibel dengan **macOS**. Sangat cepat untuk menginstal, tidak ada manajemen ketergantungan pada tingkat paket.



Ini digunakan untuk berbagai tujuan:





- Audit keselamatan
- Pengujian kepatuhan (PCI, HIPAA, dan SOX)
- Konfigurasi sistem yang lebih tangguh
- Deteksi kerentanan



Alat ini digunakan secara luas oleh berbagai macam pengguna, termasuk administrator sistem, auditor TI, dan pentester. Untuk analisis, alat ini didasarkan pada standar seperti **CIS Benchmark, NIST, NSA, OpenSCAP** dan pada rekomendasi resmi dari **Debian, Gentoo, Red Hat**.



Proyek ini tersedia di Address ini di **Github**:





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



Selanjutnya, kita akan membongkar arsip menggunakan perintah berikut:



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



Lynis hadir di mesin kami, jadi mari kita pelajari cara menggunakannya!



### A. Kontrol dan opsi utama



Untuk menampilkan perintah yang tersedia, cukup masukkan perintah berikut ini:



```
sudo lynis
# Si vous avez récupéré Lynis depuis les sources, utilisez cette syntaxe :
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



Kita akan meminta **Lynis** untuk mengaudit sistem kita, menyoroti apa yang telah dikonfigurasi dengan benar dan apa yang dapat ditingkatkan. Untuk melakukannya, masukkan perintah berikut:



```
sudo lynis audit system
# ou
./lynis audit system
```



Secara default, jika Anda tidak masuk sebagai root saat menjalankan perintah ini, alat ini akan berjalan dengan hak akses pengguna yang sedang masuk. Beberapa tes tidak akan dijalankan dalam konteks ini:



![Image](assets/fr/052.webp)



Berikut ini adalah pengujian yang tidak akan dilakukan dalam mode ini:



![Image](assets/fr/051.webp)



Setelah perintah dijalankan, analisis dimulai. Tunggu sebentar.



Pada akhir audit, Anda akan mendapatkan ini (kita dapat melihat bahwa **Lynis** telah mengidentifikasi sistem **Debian 12** dengan benar dan akan menggunakan **plugin Debian** untuk analisis):



![Image](assets/fr/017.webp)



Selanjutnya, Lynis akan membuat daftar serangkaian poin yang sesuai dengan semua yang telah dia periksa pada sistem kami. Ini disusun berdasarkan kategori, seperti yang akan kita lihat. Perlu juga dicatat bahwa kode warna digunakan untuk menyoroti rekomendasi:





- Merah** untuk Elements kritis atau praktik terbaik yang tidak dipatuhi (paket yang hilang, misalnya), yaitu server Anda tidak mematuhi poin ini
- Kuning** untuk saran atau kepatuhan sebagian terhadap rekomendasi (misalnya, mematuhi poin yang disorot dengan warna ini adalah nilai tambah (bukan prioritas))
- Green** untuk titik-titik di mana konfigurasi server Anda sesuai
- Putih**, bila netral



Di sini, kita bisa melihat bahwa Lynis merekomendasikan untuk menginstal **fail2ban**:



![Image](assets/fr/057.webp)



Pada bagian "**Boot dan layanan**", kami melihat bahwa perlindungan layanan melalui *systemd* dapat ditingkatkan. Sisi positifnya, Grub2 hadir dan tidak ada masalah dengan izin pada :



![Image](assets/fr/029.webp)



Kemudian Anda memiliki bagian "**Kernel**" dan "**Memori dan Proses**":



![Image](assets/fr/037.webp)



Selanjutnya, bagian "**Pengguna, Grup, dan Otentikasi**". Alat ini menginformasikan kepada kita tentang peringatan pada izin direktori "**/etc/sudoers.d**". Untuk saat ini, kita tidak tahu lebih banyak, tetapi kita akan dapat melihat rekomendasinya di akhir analisis.



![Image](assets/fr/049.webp)



Berikut ini adalah apa yang dapat Anda temukan di bagian "**Shells", "Files Systems", dan "USB Devices "**. Di antaranya, kita dapat melihat bahwa ada saran mengenai titik pemasangan dan bahwa perangkat USB saat ini diizinkan pada mesin ini.



![Image](assets/fr/048.webp)



Selanjutnya, bagian: "**Layanan nama", "Port dan paket", "Jaringan".** Di sini menunjukkan bahwa paket yang tidak lagi digunakan dapat dihapus dan tidak ada utilitas yang mampu mengelola pembaruan otomatis.



![Image](assets/fr/058.webp)



Kita bisa melihat bahwa firewall telah diaktifkan (dan ya, ada iptables!). Selain itu, kita dapat melihat bahwa ia telah menemukan aturan yang tidak digunakan dan server web Apache telah terinstal.



![Image](assets/fr/055.webp)



Ini diikuti dengan analisis server web itu sendiri, karena layanan telah diidentifikasi.



Kita dapat melihat bahwa ia telah menemukan berkas konfigurasi **Nginx**, dan untuk bagian SSL/TLS, **cipher** dikonfigurasikan dengan menggunakan protokol yang tidak aman. Di sisi lain, menurut Lynis, manajemen log sudah benar.



![Image](assets/fr/038.webp)



Layanan SSH ada pada server VPS saya. Konfigurasinya dianalisis oleh Lynis. Harus dikatakan bahwa keamanan SSH dapat dengan mudah ditingkatkan! Kami akan kembali ke area ini secara mendetail setelah kami mendapatkan rekomendasinya.



![Image](assets/fr/026.webp)



Berikut ini adalah bagian **"Dukungan SNMP", "Database", "PHP", "Dukungan Squid", "Layanan LDAP", "Pencatatan dan file" **.



Ada satu saran yang sangat penting tentang manajemen log: sangat disarankan agar Anda tidak hanya menyimpan log secara lokal pada mesin Anda. Jika mesin dirusak oleh penyerang, kemungkinan besar dia akan mencoba menghapus jejaknya... Jadi kita perlu mengeksternalisasi log.



![Image](assets/fr/050.webp)



Di sini, kami memiliki audit layanan yang rentan, manajemen akun, tugas terjadwal, dan sinkronisasi NTP. Diindikasikan bahwa levelnya rendah pada bagian spanduk dan identifikasi: ini dapat dimengerti, jika Anda menampilkan versi sistem, ini memberikan indikasi kepada penyerang potensial. Ini adalah pengaturan default.



Akan sangat menarik untuk mengaktifkan **auditd** untuk memiliki log dalam hal analisis **forensik**. **NTP** juga diperiksa, karena untuk mencari log secara efisien, lebih baik memiliki sistem yang tepat waktu, yang menyederhanakan pencarian.



![Image](assets/fr/036.webp)



Lynis kemudian melihat kriptografi Elements, virtualisasi, kontainer, dan kerangka kerja keamanan. Beberapa bagian kosong karena tidak ada korespondensi dengan mesin yang dianalisis. Namun, kita bisa melihat bahwa saya memiliki dua sertifikat SSL yang sudah kedaluwarsa dan saya belum mengaktifkan **SELinux**.



![Image](assets/fr/027.webp)



Di sini juga masih ada ruang untuk perbaikan: tidak ada pemindai anti-virus atau anti-malware, dan kami memiliki saran tentang izin file.



![Image](assets/fr/028.webp)



Selanjutnya, Lynis berfokus pada pengetatan konfigurasi kernel Linux (termasuk aturan untuk tumpukan IPv4), serta manajemen direktori "Home" mesin Linux.



![Image](assets/fr/035.webp)



Kita telah sampai pada akhir analisis... Poin terakhir ini menunjukkan bahwa kita akan mendapatkan segalanya dengan memiliki ClamAV pada mesin ini.



![Image](assets/fr/030.webp)



## IV. Rekomendasi



Setelah audit, saatnya untuk membaca dan menganalisis rekomendasi. Di sinilah kami mendapatkan rekomendasi dan penjelasan untuk setiap pengujian yang dilakukan oleh Lynis.



Sebagai contoh, lihatlah rekomendasi SSH. **Untuk setiap saran, Anda akan menemukan parameter yang direkomendasikan dan tautan yang akan menjelaskan poin keamanan ** Terserah Anda untuk memutuskan, tergantung pada konteks dan penggunaan Anda.



Mari kita lihat beberapa contoh rekomendasi yang secara langsung menggemakan poin-poin yang disoroti selama audit...



### A. Contoh rekomendasi





- Seperti yang kita lihat sebelumnya, NTP penting untuk log pencatatan waktu:



![Image](assets/fr/043.webp)





- Lynis juga menyarankan untuk menginstal paket **apt-listbugs** untuk mendapatkan informasi tentang bug kritis selama instalasi paket melalui **apt.**



![Image](assets/fr/041.webp)





- Alat ini menyarankan kita untuk menginstal **needrestart untuk dapat melihat proses mana yang menggunakan versi lama dari pustaka dan perlu dimulai ulang.



![Image](assets/fr/054.webp)





- Saran ini menyarankan untuk menginstal **fail2ban** untuk secara otomatis memblokir host yang gagal mengautentikasi (terutama brute force).



![Image](assets/fr/044.webp)





- Untuk mengeraskan layanan sistem, dia merekomendasikan kita menjalankan perintah biru untuk setiap layanan pada mesin kita.



![Image](assets/fr/056.webp)





- Dia menyarankan untuk menetapkan tanggal kedaluwarsa untuk semua kata sandi akun yang dilindungi.



![Image](assets/fr/031.webp)





- Saran ini menyarankan untuk menetapkan nilai minimum dan maksimum untuk usia kata sandi. Di antaranya, hal ini akan memastikan bahwa kata sandi diubah secara teratur.



![Image](assets/fr/042.webp)





- Kami merekomendasikan penggunaan partisi terpisah, untuk membatasi dampak masalah ruang disk pada satu partisi.



![Image](assets/fr/047.webp)





- Rekomendasi ini menyarankan untuk menonaktifkan penyimpanan USB dan firewire untuk mencegah kebocoran data



![Image](assets/fr/033.webp)





- Untuk memenuhi rekomendasi ini, cukup instal dan konfigurasikan **unnatended-upgrade**, misalnya.



![Image](assets/fr/053.webp)



### B. Menginstal paket yang direkomendasikan



Untuk meningkatkan konfigurasi sistem, kita akan menginstal beberapa paket pada mesin: beberapa paket yang direkomendasikan oleh Lynis, beberapa paket yang saya rekomendasikan secara pribadi.



Anda akan memiliki dasar yang baik untuk bekerja, selama Anda meluangkan sedikit waktu untuk mengonfigurasinya. Untuk melakukan hal ini, lihat situs IT-Connect, artikel lain di Web, dan dokumentasi alat.



```
sudo apt-get install debsums apt-listbugs needrestart apt-show-versions fail2ban unattended-upgrades clamav clamav-daemon rkhunter
```



Beberapa informasi tentang paket yang diinstal :





- Clamav** adalah sebuah antivirus.
- unattend-upgrades** akan memungkinkan Anda untuk mengelola pembaruan secara otomatis dan bahkan me-reboot mesin atau secara otomatis menghapus paket lama, sepenuhnya dapat dikonfigurasi.
- rkhunter** adalah anti-rootkit yang memindai sistem file Anda.
- Fail2ban** akan mendasarkan diri pada file log Anda sesuai dengan apa yang Anda berikan untuk dibacanya dan akan bekerja dengan **iptables**, misalnya untuk memblokir alamat IP yang mencoba untuk "memaksa" server Anda di SSH.



### C. Rekomendasi untuk SSH



Mari kita lihat rekomendasi SSH. Mereka tercantum di bawah ini. Jangan khawatir, kami akan segera menjelaskan cara meningkatkan konfigurasinya.



![Image](assets/fr/034.webp)



Mari kita lihat lebih dekat konfigurasi **SSH** saya saat ini di :**/etc/ssh/sshd_config**



![Image](assets/fr/018.webp)



Konfigurasi yang disarankan di bawah ini masih bisa dioptimalkan, tetapi memberikan Anda dasar yang baik. *Harap diperhatikan, bahwa saya sudah menghapus sejumlah komentar agar lebih mudah dibaca*.



Kami akan melakukannya:





- Ubah port koneksi SSH (lupakan 22 default)
- Meningkatkan tingkat kata kerja log, dari **INFO ke VERBOSE**
- Tetapkan **Waktu Tenggang Masuk** ke **2 menit**



Jika tidak ada informasi koneksi yang dimasukkan dalam waktu dua menit, koneksi akan terputus.





- Aktifkan **ModeKetat**



Menentukan apakah "sshd" harus memeriksa mode dan pemilik berkas pengguna serta direktori home pengguna sebelum memvalidasi sambungan. Hal ini biasanya diinginkan, karena terkadang pemula secara tidak sengaja membiarkan direktori atau berkas mereka dapat diakses oleh semua orang. Standarnya adalah "ya".





- Tetapkan **MaxAuthtries** ke 3



Ini menunjukkan jumlah upaya autentikasi yang gagal sebelum komunikasi ditutup.





- Tetapkan **MaxSessions** ke 2



Ini merupakan jumlah maksimum sesi simultan.





- Mengaktifkan autentikasi kunci publik



```
PubkeyAuthentication yes
```





- Mempertahankan otentikasi kata sandi :



```
PasswordAuthentication yes
```



Melarang kata sandi kosong dan autentikasi **Kerberos**, serta **autentikasi root langsung**



```
PermitEmptyPasswords no
PermitRootLogin no
```



Pastikan Anda memiliki "**PermitRootLogin no", jika sama dengan "yes", itu adalah "absolute evil".





- Melarang pengalihan koneksi TCP



```
AllowTcpForwarding no
```



Menunjukkan apakah pengalihan TCP diizinkan, dengan "ya" sebagai pengaturan default. Harap diperhatikan: menonaktifkan pengalihan TCP tidak meningkatkan keamanan jika pengguna memiliki akses ke shell, karena mereka masih dapat menyiapkan alat pengalihan mereka sendiri.





- Melarang pengalihan X11



```
X11Forwarding no
```



Menunjukkan apakah pengalihan X11 diterima, dengan "tidak" sebagai pengaturan default. Harap diperhatikan: meskipun pengalihan X11 dinonaktifkan, hal ini tidak meningkatkan keamanan, karena pengguna masih dapat mengatur pengalihan mereka sendiri. Pengalihan X11 secara otomatis dinonaktifkan jika **UseLogin** dipilih.





- Mengatur batas waktu komunikasi antara klien dan sshd



```
ClientAliveInterval  300
```



Menentukan batas waktu dalam hitungan detik, setelah itu, jika tidak ada data yang diterima dari klien, layanan sshd akan mengirim pesan yang meminta respons dari klien. Secara default, opsi ini diatur ke "0", yang berarti bahwa pesan-pesan ini tidak dikirim ke klien. Hanya protokol SSH versi 2 yang mendukung opsi ini.



```
ClientAliveCountMax 0
```



Menurut [dokumentasi (*man page*) untuk sshd] (https://www.delafond.org/traducmanfr/man/man5/sshd_config.5.html), inilah arti dari opsi ini: "Mengatur jumlah pesan penahanan (lihat di atas) yang akan dikirim tanpa respons dari klien untuk **sshd**. Jika ambang batas ini tercapai saat pesan hold telah dikirim, **sshd** akan memutuskan sambungan klien dan mengakhiri sesi. Penting untuk dicatat bahwa pesan-pesan penahanan ini sangat berbeda dengan opsi **KeepAlive** (di bawah). Pesan penahanan koneksi dikirim melalui terowongan terenkripsi, dan oleh karena itu tidak dapat dipalsukan. Penahanan koneksi tingkat TCP yang diaktifkan oleh **KeepAlive** dapat dipalsukan. Mekanisme penahanan koneksi menjadi menarik ketika klien atau server perlu mengetahui apakah koneksi tidak aktif."





- Mencegah pengungkapan informasi dengan menonaktifkan **motd, banner, lastlog**



```
PrintMotd no
```



Menentukan apakah sshd akan menampilkan isi berkas "/etc/motd" saat pengguna masuk dalam modus interaktif. Pada beberapa sistem, konten ini juga dapat ditampilkan oleh shell, melalui /etc/profile atau berkas serupa. Nilai defaultnya adalah "yes".



```
Banner none
```



Perlu dicatat bahwa di beberapa yurisdiksi, mengirim pesan sebelum autentikasi mungkin merupakan prasyarat untuk perlindungan hukum. Isi dari file yang ditentukan akan dikirim ke pengguna jarak jauh sebelum otorisasi koneksi diberikan. Opsi ini perlu dikonfigurasi, karena secara default tidak ada pesan yang akan ditampilkan.



Dalam gambar, ini memberikan hasil :



![Image](assets/fr/019.webp)



### D. Skor audit



Terakhir, jangan lupa untuk memeriksa **skor audit Lynis**! Kita melihat bahwa **skor Hardening saya adalah 63** dan file laporannya dapat dilihat di "**/var/log/lynis-report.dat**". Ada juga file "**/var/log/lynis.log**".



**Dengan kata lain, semakin tinggi skornya, semakin baik! Oleh karena itu, Anda perlu memperbaiki konfigurasi Anda untuk mencapai skor setinggi mungkin, sekaligus memungkinkan mesin dan layanan yang di-host berfungsi secara normal (yang berarti melakukan pengujian fungsional).



![Image](assets/fr/046.webp)



Mari kita lihat hasilnya di server kedua saya, di mana saya menghabiskan lebih banyak waktu untuk melakukan hardening! Jadi wajar jika skornya lebih tinggi (**76**).



![Image](assets/fr/045.webp)



## V. Perencanaan otomatis Lynis



**Lynis** juga menawarkan opsi untuk menjalankan pemeriksaan melalui tugas terjadwal. Sebenarnya ada opsi **"--cronjob "**, yang akan menjalankan semua tes Lynis tanpa perlu validasi atau tindakan pengguna. Anda kemudian dapat dengan mudah membuat skrip yang akan menjalankan **Lynis** dan meletakkan hasilnya dalam berkas yang diberi cap waktu dengan nama server yang bersangkutan. Berikut ini adalah file jenis ini yang dapat Anda letakkan di folder */etc/cron.daily*:



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



Kita juga akan membuat beberapa variabel kontekstual yang akan membantu kita mengatur diri kita dengan lebih baik, seperti nama host dan tanggal untuk menamai laporan dan memberi stempel waktu, dan jalur ke folder tempat kita ingin menaruh laporan kita.



## VI. Kesimpulan



Lynis adalah alat yang sangat praktis yang akan membantu Anda menghemat waktu dan menjadi lebih efisien ketika Anda ingin mengetahui lebih banyak tentang keadaan konfigurasi server Linux, terutama dalam hal keamanan. Namun, jangan lupa bahwa setiap modifikasi harus diuji sebelum diterapkan dalam produksi, dengan mempertimbangkan penggunaan dan konteks Anda sendiri.



Anda mungkin tidak akan menerapkan konfigurasi yang sama untuk VPS yang terpapar ke Net, di mana Anda hanya membutuhkan satu koneksi SSH (karena Anda satu-satunya orang yang terhubung), tidak seperti **bastion** atau **scheduler** yang perlu memperbanyak koneksi **SSH.**



Setelah Anda mendapatkan konfigurasi yang cocok untuk Anda dalam hal pengerasan, disarankan untuk mengadopsi alat otomatisasi sehingga Anda tidak perlu mengulang tugas-tugas secara manual, karena hal ini akan memakan waktu dan rentan terhadap kesalahan. Sebagai contoh, Anda dapat menggunakan **: Puppet, Chef, Ansible, dll...**



Jangan lupa untuk berkomunikasi dengan tim Anda sebelum implementasi: Anda perlu membuat mereka memahami mengapa Anda membuat perubahan ini, bukan hanya mengatakan bahwa Anda akan melakukannya. Pada akhirnya, tujuannya adalah untuk meneruskan praktik-praktik yang baik, dan ini akan meningkatkan peluang keberhasilan Anda.



Terakhir, Anda juga bisa membandingkan **Lynis** dengan alat lain, yang mana ada beberapa di antaranya. Jika Anda ingin beralih ke manajemen terpusat namun tetap open source, saya merekomendasikan alat [Wazuh] (https://wazuh.com/).



**Tutorial ini sudah selesai, selamat bersenang-senang dengan Lynis!