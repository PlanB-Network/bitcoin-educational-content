---
name: Pi-Hole
description: Pemblokir iklan untuk seluruh jaringan Anda
---
![cover](assets/cover.webp)



___



*Tutorial ini didasarkan pada konten asli oleh Florian Duchemin yang dipublikasikan di [IT-Connect](https://www.it-connect.fr/). Lisensi [CC BY-NC 4.0] (https://creativecommons.org/licenses/by-nc/4.0/). Perubahan mungkin telah dilakukan pada teks asli.*



___



## I. Presentasi



Kita semua pasti pernah melakukannya segera setelah memulai peramban favorit kita: memasang **adblocker** (pemblokir iklan). Namun, ketika menggunakan browser TV atau perangkat Android, dll... Agak lebih sulit untuk menemukan sesuatu yang berhasil. Dan jika ada lebih dari satu perangkat di rumah, yah, Anda harus mengulangi operasi untuk setiap browser!



Dalam tutorial ini, kita akan memecahkan masalah sederhana**: menyediakan pemblokir iklan ke semua mesin di jaringan kita dan mengelolanya secara terpusat.**



Untuk melakukan ini, kita akan menggunakan alat yang dikembangkan untuk tujuan ini: **Pi-Hole**



Pi-Hole adalah lubang pembuangan DNS. Pi-Hole akan menggunakan permintaan DNS yang dibuat oleh perangkat Anda untuk memvalidasi atau menolak lalu lintas, sehingga melindungi Anda dari alamat dan domain yang diketahui mendistribusikan iklan, malware, dan sebagainya.



DNS adalah singkatan dari Sistem Nama Domain. Jadi, apa yang dimaksud dengan nama domain? Nah, "it-connect.fr" hanyalah salah satu contohnya. Nama domain adalah pengenal unik untuk satu atau beberapa sumber daya, biasanya dikelola oleh satu entitas.



Nama mesin ditambah nama domain disebut FQDN untuk *Fully Qualified Domain Name*. FQDN memungkinkan Anda menjangkau mesin tertentu hanya dengan "memanggilnya". Misalnya, ketika Anda mengetik "www.trucmachin.com", Anda sebenarnya memanggil mesin "www", yang merupakan bagian dari domain "trucmachin.com".



Kecuali bahwa komputer kita tidak memahami bahasa manusia, yang mereka pahami hanyalah biner, jadi mereka membutuhkan IP Address, yang setara dengan nomor telepon, untuk menjangkau situs web.



Jadi, setiap kali Anda memasukkan nama situs web di peramban, atau mengeklik sebuah tautan, komputer Anda akan meminta server DNS untuk mendapatkan IP Address yang sesuai dengan nama tersebut.



**Pi-Hole kemudian akan memeriksa permintaan-permintaan ini (ada ratusan permintaan setiap harinya!) dan secara otomatis memblokir mereka yang diketahui meng-host iklan atau bahkan berkas-berkas berbahaya



## II. Memasang Lubang Pi-Hole



Dengan nama seperti Pi-Hole, Anda mungkin berasumsi bahwa Anda membutuhkan Raspberry-Pi... Tapi itu tidak sepenuhnya benar. **Pi-Hole dapat diinstal pada komputer Linux apa pun (Debian, Fedora, Rocky, Ubuntu, dll.)



Di sisi lain, Anda perlu mengingat bahwa **perangkat ini harus berjalan 24 jam sehari karena alasan sederhana: tidak ada DNS, tidak ada Internet!** Oleh karena itu, Raspberry adalah ide yang bagus, karena hampir tidak mengkonsumsi energi.



Untuk menginstal, cukup sambungkan ke mesin Linux Anda melalui SSH dan masukkan perintah berikut ini sebagai "*root*":



```
curl -sSL https://install.pi-hole.net | bash
```



> **Catatan**: dalam keadaan normal, tidak disarankan untuk "meretas" skrip tanpa terlebih dahulu mengetahui apa fungsinya. Jika Anda tidak yakin, buka halaman tersebut dengan peramban atau unduh kontennya sebagai file.
>


> **Catatan: pada versi minimal Debian 11, Curl tidak terinstal, jadi Anda perlu menginstalnya secara manual dengan perintah **apt-get install curl** sebelum mengetikkan perintah di atas.

Setelah skrip dijalankan, serangkaian tes akan dilakukan, dan instalasi itu sendiri akan mengurus dirinya sendiri:



![Image](assets/fr/019.webp)



Memasang Lubang Pi-Lubang



Setelah instalasi selesai, Anda akan dibawa ke layar ini:



![Image](assets/fr/020.webp)



Layar starter Pi-Hole



> **Catatan**: jika Anda menggunakan DHCP pada mesin Anda, Anda akan mendapatkan pesan peringatan tentang hal ini. Tentu saja, untuk penggunaan yang tepat, kami sangat menyarankan agar Anda menetapkan IP tetap pada mesin Anda.

Setelah layar ini, Anda akan mendapatkan beberapa pesan informasi, dan kemudian Anda akan dibawa ke wizard konfigurasi, yang pertama-tama akan menanyakan pada Anda ke peladen DNS mana Pi-Hole akan meneruskan permintaan. Saya sendiri memilih Quad9, yang memiliki piagam privasi pengguna.



![Image](assets/fr/021.webp)



Pemilihan DNS - Pi-Hole



> **Catatan: jika Anda berada di sebuah perusahaan, kemungkinan besar server DNS Anda saat ini adalah pengontrol domain Direktori Aktif. Namun jangan khawatir, Anda nantinya bisa menentukan pengarah bersyarat untuk domain pilihan Anda. Biasanya, Anda akan dapat mengalihkan permintaan apa pun terkait domain lokal Anda ke server DNS Anda.

Anda akan melihat bahwa beberapa pilihan menyertakan opsi DNSSEC. Pada dasarnya, protokol DNS tidak aman (pada saat itu tidak dirancang dengan mempertimbangkan hal ini). DNSSEC memecahkan masalah ini dengan menambahkan keamanan Layer melalui enkripsi dan penandatanganan pertukaran, seperti yang dijelaskan dalam artikel terkait: [Keamanan DNS](https://www.it-connect.fr/securite-dns-doh-quest-ce-le-dns-over-https/)



Setiap pemblokir iklan bergantung pada satu atau beberapa daftar untuk melakukan tugasnya. Pi-Hole hadir dengan satu daftar sebagai standar, jadi pilihlah dan tambahkan lebih banyak lagi nanti.



![Image](assets/fr/022.webp)



Muncul pertanyaan tentang Interface web, instalasinya bersifat opsional, karena alat ini memiliki baris perintah sendiri untuk manajemen dan visualisasi. Tetapi Interface ini cukup menyenangkan dan dilakukan dengan baik, jadi saya sarankan Anda menginstalnya pada saat yang sama:



![Image](assets/fr/023.webp)



Jika Anda menginstal Pi-Hole pada mesin yang sudah memiliki server Web, Anda dapat menjawab "tidak" pada pertanyaan berikut. Namun, harap diperhatikan bahwa PHP dan beberapa modul diperlukan agar dapat bekerja. Jika tidak, **lighttpd akan diinstal dengan semua modul yang diperlukan**.



![Image](assets/fr/024.webp)



Anda kemudian ditanya apakah Anda ingin mencatat permintaan DNS. **Jika Anda ingin menyimpan riwayat, atur ke ya; jika tidak, atur ke tidak, tetapi Anda akan kehilangan beberapa fungsionalitas** (lihat layar berikutnya).



![Image](assets/fr/025.webp)



Untuk web Interface-nya, Pi-Hole menggunakan sebuah fungsi sendiri yang disebut FTLDNS, yang menyediakan sebuah API dan menghasilkan statistik dari permintaan DNS. Fungsi ini bisa menyertakan mode "privasi" yang menyembunyikan domain yang diminta, pelanggan di balik permintaan, atau keduanya. Berguna jika Anda ingin melakukan pemantauan tanpa melanggar privasi orang, atau hanya jika Anda ingin mematuhi peraturan yang relevan dalam hal penggunaan pada jaringan publik.



![Image](assets/fr/026.webp)



Pilihan gaya hidup pribadi



Setelah pertanyaan terakhir ini dijawab, skrip akan melakukan apa yang seharusnya dilakukan: mengunduh repositori GitHub dan mengonfigurasi Pi-Hole. Pada akhir instalasi, layar ringkasan akan ditampilkan dengan info penting:



![Image](assets/fr/027.webp)



Layar ringkasan instalasi



Catat kata sandi web Interface dan informasi jaringan. Sekarang saatnya mengkonfigurasi layanan DHCP di lokasi kita saat ini.



## III. Konfigurasi DHCP



Agar dapat berfungsi, Pi-Hole perlu "menyelesaikan" permintaan DNS dari klien, jadi mereka harus tahu bahwa Pi-Hole-lah yang akan mengirimkannya. Ada beberapa cara untuk melakukan ini:





- Ubah pengaturan DNS di server DHCP Anda (misalnya, Box Anda)
- Nonaktifkan server ini dan gunakan server yang disediakan oleh Pi-Hole
- Memodifikasi secara manual setiap perangkat untuk menggunakan Pi-Hole sebagai DNS



Saya pribadi memilih solusi pertama. Kemungkinannya adalah **Anda memiliki server DHCP di tempat Anda berada** (biasanya di dalam kotak komputer Anda). Jadi tidak perlu repot-repot.



Karena ada banyak sekali kemungkinan, antara kotak operator yang berbeda (yang tidak saya ketahui semuanya) dan mereka yang memiliki router sendiri, saya tidak akan memberikan tangkapan layar untuk modifikasi ini. Bagaimanapun, Anda harus masuk ke pengaturan DHCP dan memodifikasi parameter "DNS" untuk memasukkan IP Address dari Pi-Hole Anda.



Setelah ini dilakukan, jika ada perangkat yang telah dinyalakan sebelumnya, perangkat tersebut akan mempertahankan pengaturan lama, jadi Anda harus memulai ulang permintaan konfigurasi.



Pada workstation Windows, dengan prompt perintah:



```
ipconfig /renew
```



Pada stasiun kerja Linux:



```
dhclient
```



Untuk semua perangkat lain, perangkat tersebut harus dimatikan dan dinyalakan kembali.



Jadi, mereka harus mendapatkan parameter yang tepat, untuk diperiksa:



```
ipconfig /all
```



Pada bidang DNS, Anda harus memiliki Address dari Pi-Hole Anda, dalam kasus saya 192.168.1.42:



![Image](assets/fr/029.webp)



## IV. Menggunakan lubang Pi-Hole web Interface



Untuk memfasilitasi administrasi, **Pi-Hole** mendapat manfaat dari Interface web Interface yang dirancang dengan baik. Mudah digunakan dan dapat diakses, memungkinkan Anda:





- Melihat jumlah permintaan, permintaan yang diblokir, dll. secara real time.
- Kelola Daftar Putih dan Daftar Hitam Anda
- Menambahkan entri statis, alias, dll.
- Tambahkan daftar
- Dan masih banyak fungsi lainnya!



Bagi saya, saya akan menambahkan daftar pemblokiran. Seperti disebutkan di atas, hanya satu daftar yang dipasang bersamaan dengan Soft. Ada banyak daftar untuk situs iklan, tetapi yang terbaik adalah memilih setidaknya satu yang spesifik untuk negara tempat Anda tinggal. Salah satu daftar yang paling terkenal adalah **EasyList**, dan salah satunya khusus untuk Prancis: [EasyList-ListFR](https://raw.githubusercontent.com/deathbybandaid/piholeparser/master/Subscribable-Lists/ParsedBlacklists/EasyList-Liste-FR.txt)



Untuk menambahkannya, pertama-tama sambungkan ke admin Interface: **http://<ip_du_PiHole>/admin**



Kata sandi administrator telah dibuat (lihat tangkapan layar akhir instalasi), jadi Anda hanya perlu memasukkannya untuk mengakses Interface:



![Image](assets/fr/030.webp)



Interface dari Pi-Hole



Kita dapat melihat, misalnya, bahwa ada dua pelanggan yang terhubung ke Pi-Hole, bahwa Pi-Hole telah memproses 442 permintaan dan 8 di antaranya telah diblokir. Grafik ini bisa menjadi sumber informasi yang baik, terutama dalam konteks profesional.



Untuk menambahkan daftar, buka menu "**Group Management**" dan "**Adlists**":



![Image](assets/fr/031.webp)



Kita dapat melihat daftar pertama kita "**StevenBlack**", untuk menambahkan daftar kita, salin tautan yang saya berikan di atas dan masukkan ke dalam bidang "**Address**", untuk deskripsinya, saya memilih untuk memasukkan nama daftar:



![Image](assets/fr/032.webp)



Menambahkan daftar di Pi-Hole



Yang tersisa hanyalah mengklik "**Tambahkan**" untuk menambahkannya. Untuk mengaktifkannya, kita perlu melakukan langkah tambahan untuk "memperingatkan" Pi-Hole untuk mengambil alih daftar ini. Untuk melakukan ini:





- Gunakan baris perintah bawaan
- Baik web Interface



Saya pribadi memilih yang kedua, karena jika Anda perhatikan dengan seksama, tautan ke skrip PHP yang melakukan pembaruan langsung ada di halaman tempat kita berada (kata "online"). Jadi, Anda tinggal mengkliknya, yang akan membawa Anda ke halaman yang hanya memiliki satu pilihan:



![Image](assets/fr/033.webp)



Halaman ini akan menampilkan hasil skrip setelah selesai, yang berarti bahwa daftar tersebut telah diperhitungkan (kecuali jika ada pesan kesalahan yang ditampilkan, tentu saja).



Seperti yang diumumkan di awal tutorial ini, Pi-Hole juga memungkinkan Anda untuk memblokir domain yang diketahui mendistribusikan malware. Untuk memperkuat fitur ini, saya sarankan Anda juga menambahkan daftar domain yang diperbarui secara berkala yang didistribusikan oleh Abuse.ch**, yang secara signifikan akan memperkuat keamanan jaringan Anda, tersedia di [Address] (https://urlhaus.abuse.ch/downloads/hostfile/).



Tentu saja, Anda dapat menambahkan daftar apa pun yang Anda anggap relevan, atau mengelola daftar hitam secara manual melalui menu daftar hitam.



## V. Tes Pi-Hole



Sekarang semuanya sudah siap, yang harus Anda lakukan adalah menguji solusi untuk memastikannya berfungsi dengan baik.



Sebagai contoh, saya akan mencoba menjangkau domain *http://admin.gentbcn.org/* yang ada dalam daftar Abuse.ch karena domain ini dikenal sebagai tempat hosting malware:



![Image](assets/fr/034.webp)



Jelas, saya telah diblokir di suatu tempat. Untuk memastikan bahwa Pi-Hole-lah yang melakukan tugasnya, kita dapat memeriksa log kueri di "Log Kueri" web Interface untuk melihat bahwa itu adalah pemblokiran dari entri daftar:



![Image](assets/fr/035.webp)



## VI. Kesimpulan



Dalam tutorial ini, kami telah menunjukkan pada Anda cara menyiapkan server DNS yang tidak hanya menghilangkan sebagian besar iklan demi kenyamanan penjelajahan Anda, tetapi juga menambahkan **keamanan Layer dengan memblokir domain-domain penyebar phishing dan malware**.



Semuanya gratis dan ekonomis jika dipasang pada Raspberry-Pi (dalam hal konsumsi daya).