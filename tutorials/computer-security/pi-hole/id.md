---
name: Pi-Hole
description: Pemblokir iklan untuk seluruh jaringan Anda
---
![cover](assets/cover.webp)

___

*Tutorial ini didasarkan pada konten asli oleh Florian Duchemin yang dipublikasikan di [IT-Connect](https://www.it-connect.fr/). Lisensi [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Perubahan mungkin telah dilakukan pada teks asli.*
___

## I. Presentasi

Kita semua pernah melakukannya begitu memulai browser favorit kita: memasang **adblocker** (pemblokir iklan). Namun, ketika menggunakan menggunakan TV atau perangkat Android, dan lain-lain, agak sulit menemukan sesuatu yang berfungsi. Dan jika ada lebih dari satu perangkat di rumah, Anda harus mengulanginya untuk setiap browser!

Dalam tutorial ini, kita akan menyelesaikan masalah sederhana: menyediakan ad blocker untuk semua perangkat di jaringan kita dan mengelolanya secara terpusat.

Untuk melakukan ini, kita akan menggunakan alat yang dikembangkan untuk tujuan ini: **Pi-Hole**.

Pi-Hole adalah DNS sinkhole. Pi-Hole akan menggunakan permintaan DNS yang dibuat oleh perangkat Anda untuk memvalidasi atau menolak lalu lintas, sehingga melindungi Anda dari alamat dan domain yang dikenal mendistribusikan iklan, malware, dan lain sebagainya.

DNS adalah singkatan dari _Domain Name System_. Jadi, apa itu nama domain? "it-connect.fr" hanyalah salah satu contoh. Nama domain adalah pengenal unik untuk satu atau lebih sumber daya, biasanya dikelola oleh satu entitas.

Nama perangkat yang ditambah nama domain disebut FQDN (_Fully Qualified Domain Name_). Ini memungkinkan Anda untuk mencapai perangkat tertentu hanya dengan "memanggilnya". Misalnya, ketika Anda mengetik "www.trucmachin.com", Anda sebenarnya memanggil perangkat "www", yang termasuk dalam domain "trucmachin.com".

Kita perlu tahu komputer kita tidak mengerti bahasa manusia, yang mereka mengerti hanyalah biner, jadi mereka membutuhkan alamat IP, yang setara dengan nomor telepon, untuk mencapai situs web.

Jadi, setiap kali Anda memasukkan nama situs web di browser Anda, atau mengklik tautan, komputer Anda pertama-tama meminta server DNS untuk alamat IP yang sesuai dengan nama tersebut.

**Pi-Hole kemudian akan memeriksa permintaan-permintaan ini (ada ratusan setiap hari!) dan secara otomatis memblokir yang diketahui menjadi host iklan atau bahkan file berbahaya.**

## II. Memasang Pi-Hole

Dengan nama seperti Pi-Hole, Anda mungkin benar berasumsi bahwa Anda memerlukan sebuah Raspberry-Pi... Tetapi itu tidak sepenuhnya benar. Pi-Hole dapat dipasang di komputer Linux mana pun (Debian, Fedora, Rocky, Ubuntu, dll.).

Di sisi lain, Anda perlu ingat **bahwa perangkat ini harus menyala 24 jam sehari untuk alasan sederhana: tanpa DNS, tidak ada Internet!** Oleh karena itu Raspberry adalah ide yang bagus, karena hampir tidak mengonsumsi energi.

Untuk menginstal, cukup sambungkan ke komputer Linux Anda melalui SSH dan masukkan perintah berikut ini sebagai "*root*":

```
curl -sSL https://install.pi-hole.net | bash
```

> **Catatan**: Dalam keadaan normal, tidak disarankan untuk "menjalankan" sebuah skrip tanpa terlebih dahulu mengetahui apa yang dilakukannya. Jika Anda tidak yakin, buka halaman dengan browser atau unduh kontennya sebagai file.

> **Catatan**: Pada versi minimal Debian 11, Curl tidak terinstal, jadi Anda perlu memasangnya secara manual dengan perintah **apt-get install curl** sebelum mengetik perintah di atas.

Setelah skrip berjalan, serangkaian tes akan dilakukan, dan instalasi itu sendiri akan berjalan secara mandiri:

![Image](assets/fr/019.webp)

meng-install Pi-Hole

Setelah instalasi selesai, Anda akan dibawa ke layar ini:

![Image](assets/fr/020.webp)

Layar starter Pi-Hole

> **Catatan**: Jika Anda menggunakan DHCP pada komputer Anda, Anda akan mendapatkan pesan peringatan tentang hal ini. Tentu saja, untuk penggunaan yang tepat, kami sangat menyarankan agar Anda menetapkan IP tetap ke komputer Anda.

Setelah layar ini, Anda akan mendapatkan beberapa pesan informasi, dan kemudian Anda akan dibawa ke wizard konfigurasi, yang pertama-tama akan menanyakan server DNS mana yang akan menjadi tempat Pi-Hole meneruskan permintaan. Dari sisi saya, saya telah memilih Quad9, yang memiliki piagam privasi pengguna.

![Image](assets/fr/021.webp)

Pemilihan DNS - Pi-Hole

> **Catatan**: Jika Anda berada di sebuah perusahaan, kemungkinan server DNS Anda saat ini adalah pengontrol domain Active Directory. Tetapi jangan khawatir, Anda nantinya dapat menentukan redirector bersyarat untuk domain pilihan Anda. Biasanya, Anda dapat mengarahkan setiap permintaan yang berkaitan dengan domain lokal Anda ke server DNS Anda.

Anda akan melihat bahwa beberapa pilihan menyertakan opsi DNSSEC. Pada dasarnya, protokol DNS tidak aman (tidak dirancang dengan mempertimbangkan hal ini pada saat itu). DNSSEC memecahkan masalah ini dengan menambahkan lapisan keamanan melalui enkripsi dan penandatanganan pertukaran, seperti yang dijelaskan dalam artikel yang sesuai: [Keamanan DNS](https://www.it-connect.fr/securite-dns-doh-quest-ce-le-dns-over-https/)

Setiap ad blocker mengandalkan satu atau lebih daftar untuk melakukan pekerjaannya. Pi-Hole hadir dengan satu daftar sebagai standar, jadi pilihlah dan tambahkan lebih banyak nanti.

![Image](assets/fr/022.webp)

Kemudian muncul pertanyaan tentang Interface web, instalasinya opsional, karena aplikasi ini memiliki command line sendiri untuk manajemen dan visualisasi. Tetapi Interface ini cukup menyenangkan dan dibuat dengan baik, jadi saya sarankan Anda menginstalnya pada saat yang sama:

![Image](assets/fr/023.webp)

Jika Anda memasang Pi-Hole pada komputer yang sudah memiliki server web, Anda dapat menjawab "no" untuk pertanyaan berikut. Namun, harap dicatat bahwa PHP dan beberapa modul diperlukan agar ini berfungsi. Jika tidak, **lighttpd akan dipasang dengan semua modul yang diperlukan**.

![Image](assets/fr/024.webp)

Anda kemudian ditanya apakah Anda ingin merekam permintaan DNS. **Jika Anda ingin menyimpan riwayat, atur ini ke "yes"; jika tidak, atur ini ke "no", tetapi Anda akan kehilangan beberapa fungsionalitas** (lihat layar berikutnya).

![Image](assets/fr/025.webp)

Untuk Interface web-nya, Pi-Hole menggunakan fungsi sendiri yang disebut FTLDNS, yang menyediakan API dan menghasilkan statistik dari permintaan DNS. Fungsi ini dapat menyertakan mode "privasi" yang menyamarkan domain yang diminta, klien di balik permintaan, atau keduanya. Berguna jika Anda ingin melakukan pemantauan tanpa melanggar privasi orang, atau hanya jika Anda ingin mematuhi peraturan yang relevan dalam kasus penggunaan pada jaringan publik.

![Image](assets/fr/026.webp)

Pilihan mode privasi pribadi

Setelah pertanyaan terakhir ini dijawab, skrip akan melakukan apa yang seharusnya: mengunduh repositori GitHub dan mengonfigurasi Pi-Hole. Di akhir instalasi, layar ringkasan akan ditampilkan dengan info penting:

![Image](assets/fr/027.webp)

Layar ringkasan instalasi

Catat kata sandi Interface web dan informasi jaringan. Sekarang saatnya mengonfigurasi layanan DHCP di lokasi kita saat ini.

## III. Konfigurasi DHCP

Agar dapat berfungsi, Pi-Hole perlu "menyelesaikan" permintaan DNS dari klien, jadi mereka harus tahu bahwa Pi-Hole-lah tempat untuk mengirimnya. Ada beberapa cara untuk melakukan ini:

- Memodifikasi pengaturan DNS di server DHCP Anda (misalnya, router Anda)
- Menonaktifkan server ini dan menggunakan yang disediakan oleh Pi-Hole
- Secara manual memodifikasi setiap perangkat untuk menggunakan Pi-Hole sebagai DNS

Saya pribadi memilih solusi pertama. Kemungkinan besar **Anda memiliki server DHCP di tempat Anda berada** (biasanya router Anda). Jadi tidak perlu repot.

Karena ada banyak kemungkinan, antara router operator yang berbeda (yang tidak saya ketahui semuanya) dan mereka yang memiliki router sendiri, saya tidak akan menyediakan tangkapan layar untuk modifikasi ini. Bagaimanapun, Anda perlu pergi ke pengaturan DHCP dan memodifikasi parameter "DNS" untuk menyertakan alamat IP dari Pi-Hole Anda.

Setelah ini selesai, jika ada perangkat yang telah dihidupkan sebelumnya, mereka akan mempertahankan pengaturan lama, jadi Anda perlu memulai ulang permintaan konfigurasi.

Pada workstation Windows, dengan prompt perintah:

```
ipconfig /renew
```

Pada workstation Linux :

```
dhclient
```

Untuk semua perangkat lain, perangkat tersebut harus dimatikan dan dinyalakan kembali.

Jadi, mereka harus mendapatkan parameter yang tepat, untuk diperiksa:

```
ipconfig /all
```

Pada bagian DNS, Anda harus memiliki Address dari Pi-Hole Anda, dalam kasus saya 192.168.1.42 :

![Image](assets/fr/029.webp)


## IV. Menggunakan Pi-Hole web Interface

Untuk memfasilitasi administrasi, **Pi-Hole** memiliki Interface web yang dirancang dengan baik. Ramah pengguna dan mudah diakses, hal ini memungkinkan Anda untuk:

- Melihat jumlah permintaan, permintaan yang diblokir, dll. secara real time.
- Mengelola Whitelist dan Blacklist Anda.
- Menambahkan entri statis, alias, dll.
- Menambahkan daftar.
- Dan banyak fungsi lainnya!

Dari sisi saya, saya akan menambahkan daftar pemblokiran. Seperti yang disebutkan di atas, hanya satu daftar yang dipasang pada saat yang sama dengan perangkat lunak. Ada banyak daftar untuk situs iklan, tetapi yang terbaik adalah memilih setidaknya satu yang spesifik untuk negara tempat Anda tinggal. Salah satu daftar yang paling terkenal adalah **EasyList**, dan salah satunya spesifik untuk Prancis: [EasyList-ListFR](https://raw.githubusercontent.com/deathbybandaid/piholeparser/master/Subscribable-Lists/ParsedBlacklists/EasyList-Liste-FR.txt)

Untuk menambahkannya, pertama-tama masuk ke admin Interface: **http://<ip_du_PiHole>/admin**

Kata sandi administrator telah dibuat (lihat tangkapan layar akhir instalasi), jadi Anda hanya perlu memasukkannya untuk mengakses Interface:

![Image](assets/fr/030.webp)

Interface dari Pi-Hole

Kita dapat melihat, misalnya, bahwa ada dua klien yang terhubung ke Pi-Hole, bahwa Pi-Hole telah memproses 442 permintaan dan 8 di antaranya telah diblokir. Grafik ini bisa menjadi sumber informasi yang baik, terutama dalam konteks profesional.

Untuk menambahkan daftar, buka menu "**Group Management**" dan "**Adlists**":

![Image](assets/fr/031.webp)

Kita dapat melihat daftar pertama kita "**StevenBlack**", untuk menambahkan daftar kita, salin tautan yang saya berikan di atas dan masukkan ke dalam bidang "**Address**", untuk deskripsinya, saya memilih untuk memasukkan nama daftar:

![Image](assets/fr/032.webp)

Menambahkan daftar di Pi-Hole

Yang tersisa hanyalah mengklik "**Add**" untuk menambahkannya. Untuk mengaktifkannya, kita perlu melakukan langkah tambahan untuk "memperingatkan" Pi-Hole untuk mengambil alih daftar ini. Untuk melakukan ini :

- Gunakan command line bawaan
- Menggunakan web Interface

Saya pribadi memilih yang kedua, karena jika Anda telah melihat dengan cermat, tautan ke skrip PHP yang melakukan pembaruan langsung ada di halaman tempat kita berada (kata "online"). Jadi, yang harus Anda lakukan hanyalah mengkliknya, yang akan membawa Anda ke halaman dengan hanya satu opsi:

![Image](assets/fr/033.webp)

Halaman tersebut akan menampilkan hasil skrip setelah selesai, yang berarti daftar tersebut telah diperhitungkan (tentu saja, kecuali jika pesan kesalahan ditampilkan).

Seperti yang diumumkan di awal tutorial ini, Pi-Hole juga memungkinkan Anda memblokir domain yang dikenal mendistribusikan malware. Untuk memperkuat fitur ini, saya sarankan Anda juga menambahkan daftar domain yang diperbarui secara teratur yang didistribusikan oleh **Abuse.ch**, yang akan secara signifikan memperkuat keamanan jaringan Anda, tersedia di [alamat ini](https://urlhaus.abuse.ch/downloads/hostfile/).

Tentu saja, Anda dapat menambahkan daftar apa pun yang menurut Anda relevan, atau mengelola blacklist Anda secara manual melalui menu blacklist.

## V. Tes Pi-Hole

Setelah semuanya terpasang, yang perlu Anda lakukan hanyalah menguji solusi ini untuk memastikannya berfungsi dengan baik.

Sebagai contoh, saya akan mencoba menjangkau domain _http://admin.gentbcn.org/_ yang ada di daftar **Abuse.ch** karena dikenal sebagai host malware:

![Image](assets/fr/034.webp)

Jelas, saya telah diblokir di suatu tempat. Untuk memastikan bahwa Pi-Hole yang telah melakukan pekerjaan ini, kita dapat memeriksa log permintaan di Interface web "Query Log" untuk melihat bahwa itu adalah blok dari entri daftar:

![Image](assets/fr/035.webp)

## VI. Kesimpulan

Dalam tutorial ini, kami telah menunjukkan kepada Anda cara mengatur server DNS yang tidak hanya menghilangkan sebagian besar iklan untuk kenyamanan penjelajahan Anda, tetapi juga menambahkan lapisan **keamanan dengan memblokir domain phishing dan penyebar malware**.

Semuanya gratis dan ekonomis jika dipasang di Raspberry Pi (dalam hal konsumsi daya).
