---
name: Graylog
description: Memusatkan dan menganalisis log Anda dengan mudah
---
![cover](assets/cover.webp)



___



*Tutorial ini didasarkan pada konten asli oleh Florian BURNEL yang dipublikasikan di [IT-Connect](https://www.it-connect.fr/). Lisensi [CC BY-NC 4.0] (https://creativecommons.org/licenses/by-nc/4.0/). Perubahan mungkin telah dilakukan pada teks asli.*



___



## Menerapkan Graylog pada Debian 12



### I. Presentasi



Graylog adalah solusi "log sink" sumber terbuka yang dirancang untuk memusatkan, menyimpan, dan menganalisis log dari mesin dan perangkat jaringan Anda secara real time. Dalam tutorial ini, kita akan belajar cara menginstal Graylog versi gratis pada mesin Debian 12!



Dalam sebuah sistem informasi, setiap **server**, baik yang menjalankan **Linux** atau **Windows**, dan setiap **perangkat jaringan** (sakelar, router, firewall, dll...) **menghasilkan lognya sendiri**, yang disimpan secara lokal. Dengan log yang disimpan secara lokal di setiap mesin, analisis peristiwa dan korelasi menjadi sangat sulit... Di sinilah **Graylog** masuk. Ini akan bertindak sebagai **log sink**, yang berarti bahwa **semua mesin Anda akan mengirimkan log mereka (melalui syslog, misalnya). Graylog kemudian akan menyimpan dan mengindeks log-log ini, dan mengizinkan Anda untuk melakukan pencarian global dan membuat peringatan.



Graylog adalah alat analisis dan pemantauan yang memudahkan untuk mengidentifikasi perilaku yang mencurigakan dan berbagai masalah (stabilitas, kinerja, dll.).




![Image](assets/fr/034.webp)



**Catatan: versi gratisnya, **Graylog Open**, bukanlah SIEM seperti Wazuh, terutama karena tidak memiliki fungsi deteksi penyusupan yang nyata.



### II. Prasyarat



Tumpukan Graylog didasarkan pada **beberapa komponen** yang harus kita instal dan konfigurasi. Di sini, kita akan menginstal semua komponen pada server yang sama, tetapi dimungkinkan untuk membuat cluster berdasarkan beberapa node dan mendistribusikan peran di beberapa server. Untuk keperluan tutorial ini, kita akan menginstal **Graylog 6.1**, versi terbaru hingga saat ini.





- MongoDB 7**, versi yang direkomendasikan saat ini untuk Graylog (minimum 5.0.7, maksimum 7.x)
- OpenSearch**, sumber terbuka Fork dari Elasticsearch yang dibuat oleh Amazon (minimum 1.1.x, maksimum 2.15.x)
- OpenJDK 17**



Server **Graylog** berjalan pada **Debian 12**, tetapi instalasi dapat dilakukan pada distribusi lain, termasuk melalui Docker. Mesin virtual ini dilengkapi dengan **8 GB RAM** dan **256 GB ruang disk**, agar memiliki sumber daya yang cukup untuk semua komponen (jika tidak, hal ini dapat berdampak signifikan pada kinerja). Namun, saya memberikan ini sebagai panduan kasar, karena **ukuran arsitektur Graylog tergantung pada jumlah informasi yang akan diproses**. Graylog dapat memproses 30 MB atau 300 MB data per hari, serta 300 GB data per hari... Ini adalah **solusi yang dapat diskalakan** yang mampu menangani **terabyte log** (lihat [halaman ini] (https://go2docs.graylog.org/current/planning_your_deployment/planning_your_deployment.html?tocpath=Plan%20Your%20Deployment%7C_____0)).



![Image](assets/fr/032.webp)



Sumber: Graylog



Sebelum memulai konfigurasi, tetapkan IP statis Address ke mesin Graylog dan instal pembaruan terbaru. Pastikan untuk mengatur zona waktu mesin lokal dan menentukan server NTP untuk sinkronisasi tanggal dan waktu. Inilah perintah yang harus dijalankan:



```
sudo timedatectl set-timezone Europe/Paris
```



**Catatan: **Penginstalan OpenSearch bersifat opsional** jika Anda menggunakan **Graylog Data Node** sebagai gantinya.



### III Instalasi Graylog langkah demi langkah



Mari kita mulai dengan memperbarui cache paket dan menginstal alat yang kita perlukan untuk yang akan datang.



```
sudo apt-get update
sudo apt-get install curl lsb-release ca-certificates gnupg2 pwgen
```



![Image](assets/fr/030.webp)



#### A. Menginstal MongoDB



Setelah selesai, kita akan mulai menginstal MongoDB. Unduh kunci GPG yang sesuai dengan repositori MongoDB:



```
curl -fsSL https://www.mongodb.org/static/pgp/server-6.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor
```



Kemudian tambahkan repositori MongoDB 6 ke mesin Debian 12:



```
echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg] http://repo.mongodb.org/apt/debian bullseye/mongodb-org/6.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
```



Selanjutnya, kita akan memperbarui cache paket dan mencoba menginstal MongoDB:



```
sudo apt-get update
sudo apt-get install -y mongodb-org
```



MongoDB tidak dapat diinstal karena ketergantungan hilang: **libssl1.1**. Kita harus menginstal paket ini secara manual sebelum dapat melanjutkan, karena Debian 12 tidak memilikinya di repositori.



```
Les paquets suivants contiennent des dépendances non satisfaites :
mongodb-org-mongos: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
mongodb-org-server: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
E: Impossible de corriger les problèmes, des paquets défectueux sont en mode « garder en l'état ».
```



Kita akan mengunduh paket DEB bernama "**libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb**" (versi terbaru) dengan perintah **wget**, lalu menginstalnya dengan perintah **dpkg**. Ini menghasilkan dua perintah berikut:



```
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
```



![Image](assets/fr/028.webp)



Mulai ulang instalasi MongoDB:



```
sudo apt-get install -y mongodb-org
```



Kemudian mulai ulang layanan MongoDB dan aktifkan untuk memulai secara otomatis saat server Debian diluncurkan.



```
sudo systemctl daemon-reload
sudo systemctl enable mongod.service
sudo systemctl restart mongod.service
sudo systemctl --type=service --state=active | grep mongod
```



Setelah MongoDB terinstal, kita dapat melanjutkan untuk menginstal komponen berikutnya.



#### B. Menginstal OpenSearch



Mari kita lanjutkan dengan menginstal OpenSearch pada server. Perintah berikut ini menambahkan kunci tanda tangan untuk paket OpenSearch:



```
curl -o- https://artifacts.opensearch.org/publickeys/opensearch.pgp | sudo gpg --dearmor --batch --yes -o /usr/share/keyrings/opensearch-keyring
```



Kemudian tambahkan repositori OpenSearch sehingga kita dapat mengunduh paket dengan **apt** setelahnya:



```
echo "deb [signed-by=/usr/share/keyrings/opensearch-keyring] https://artifacts.opensearch.org/releases/bundle/opensearch/2.x/apt stable main" | sudo tee /etc/apt/sources.list.d/opensearch-2.x.list
```



Perbarui cache paket Anda:



```
sudo apt-get update
```



Kemudian **instal OpenSearch**, dengan hati-hati menentukan kata sandi default untuk akun Admin** instans Anda. Di sini, kata sandinya adalah "**IT-Connect2024!**", tetapi ganti nilai ini dengan kata sandi yang kuat. **Hindari kata sandi yang lemah** seperti "**P@ssword123**" dan gunakan setidaknya **8 karakter** dengan setidaknya satu karakter dari setiap jenisnya (huruf kecil, huruf besar, angka, dan karakter khusus), jika tidak, maka akan terjadi kesalahan pada akhir instalasi. **Ini adalah prasyarat sejak OpenSearch 2.12.**



```
sudo env OPENSEARCH_INITIAL_ADMIN_PASSWORD=IT-Connect2024! apt-get install opensearch
```



Harap bersabar selama pemasangan...



Setelah selesai, luangkan waktu sejenak untuk melakukan konfigurasi minimum. Buka file konfigurasi dalam format YAML:



```
sudo nano /etc/opensearch/opensearch.yml
```



Apabila file sudah terbuka, tetapkan opsi berikut ini:



```
cluster.name: graylog
node.name: ${HOSTNAME}
path.data: /var/lib/opensearch
path.logs: /var/log/opensearch
discovery.type: single-node
network.host: 127.0.0.1
action.auto_create_index: false
plugins.security.disabled: true
```



Konfigurasi OpenSearch ini dirancang untuk menyiapkan satu node. Berikut ini beberapa penjelasan tentang berbagai parameter yang kami gunakan:





- cluster.name: graylog**: parameter ini memberi nama kluster OpenSearch dengan nama "**graylog**".
- node.name: ${HOSTNAME}**: nama simpul diatur secara dinamis agar sesuai dengan nama mesin Linux lokal. Meskipun kita hanya memiliki satu node, penting untuk menamainya dengan benar.
- path.data: /var/lib/opensearch**: jalur ini menentukan di mana OpenSearch menyimpan datanya di mesin lokal, dalam kasus ini di "**/var/lib/opensearch**".
- path.logs: /var/log/opensearch**: jalur ini mendefinisikan di mana file log OpenSearch disimpan, di sini, di "**/var/log/opensearch**".
- discovery.type: single-node**: parameter ini mengonfigurasi OpenSearch untuk bekerja dengan simpul tunggal, oleh karena itu, pilihlah opsi "**single-node**".
- network.host: 127.0.0.1**: konfigurasi ini memastikan bahwa OpenSearch hanya mendengarkan pada loop lokal Interface, yang sudah cukup karena berada di server yang sama dengan Graylog.
- action.auto_create_index: false**: dengan menonaktifkan pembuatan indeks otomatis, OpenSearch tidak akan secara otomatis membuat indeks ketika dokumen dikirim tanpa indeks yang ada.
- plugins.security.disabled: true**: opsi ini menonaktifkan plugin keamanan OpenSearch, yang berarti tidak akan ada autentikasi, manajemen akses, atau enkripsi komunikasi. Pengaturan ini menghemat waktu ketika menyiapkan Graylog, tetapi sebaiknya dihindari dalam produksi (lihat [halaman ini] (https://opensearch.org/docs/1.0/security-plugin/index/)).



Beberapa opsi sudah tersedia, jadi Anda hanya perlu menghapus "#" untuk mengaktifkannya, lalu tunjukkan nilai Anda. Jika Anda tidak dapat menemukan opsi, Anda dapat mendeklarasikannya secara langsung di akhir file.



![Image](assets/fr/023.webp)



Simpan dan tutup file ini.



#### C. Mengkonfigurasi Java (JVM)



Anda perlu mengonfigurasi Java Virtual Machine yang digunakan oleh OpenSearch untuk menyesuaikan jumlah memori yang dapat digunakan oleh layanan ini. Edit file konfigurasi berikut ini:



```
sudo nano /etc/opensearch/jvm.options
```



Dengan konfigurasi yang digunakan di sini, **OpenSearch akan dimulai dengan memori yang dialokasikan sebesar 4 GB dan dapat bertambah hingga 4 GB**, sehingga tidak akan ada variasi memori selama pengoperasian. Di sini, konfigurasi memperhitungkan fakta bahwa mesin virtual memiliki total **8 GB RAM**. Kedua parameter harus memiliki nilai yang sama. Ini berarti mengganti baris:



```
-Xms1g
-Xmx1g
```



Dengan garis-garis ini:



```
-Xms4g
-Xmx4g
```



Berikut ini gambar modifikasi yang akan dilakukan:



![Image](assets/fr/022.webp)



Tutup file ini setelah menyimpannya.



Sebagai tambahan, kita perlu memeriksa konfigurasi parameter "**max_map_count**" pada kernel Linux. Parameter ini mendefinisikan batas area memori yang dipetakan per proses, untuk memenuhi kebutuhan aplikasi kita. **OpenSearch**, seperti Elasticsearch**, merekomendasikan untuk mengatur nilai ini ke "262144" untuk menghindari kesalahan manajemen memori.



Pada prinsipnya, pada mesin Debian 12 yang baru diinstal, nilainya sudah benar. Tetapi mari kita periksa. Jalankan perintah ini:



```
cat /proc/sys/vm/max_map_count
```



Jika Anda mendapatkan nilai selain "**262144**", jalankan perintah berikut ini, jika tidak, perintah ini tidak diperlukan.



```
sudo sysctl -w vm.max_map_count=262144
```



Terakhir, aktifkan mulai otomatis OpenSearch dan luncurkan layanan terkait.



```
sudo systemctl daemon-reload
sudo systemctl enable opensearch
sudo systemctl restart opensearch
```



Jika Anda menampilkan status sistem, Anda akan melihat proses Java dengan RAM 4 GB.



```
top
```



![Image](assets/fr/029.webp)



Langkah selanjutnya: instalasi Graylog yang sudah lama ditunggu-tunggu!



#### D. Menginstal Graylog



Untuk **menginstal Graylog 6.1** dalam versi terbarunya, jalankan 4 perintah berikut untuk **mengunduh dan menginstal Graylog Server**:



```
wget https://packages.graylog2.org/repo/packages/graylog-6.1-repository_latest.deb
sudo dpkg -i graylog-6.1-repository_latest.deb
sudo apt-get update
sudo apt-get install graylog-server
```



Setelah ini selesai, kita perlu membuat beberapa perubahan pada konfigurasi Graylog sebelum mencoba meluncurkannya.



Mari kita mulai dengan mengonfigurasi kedua opsi ini:





- password_secret**: parameter ini digunakan untuk mendefinisikan kunci yang digunakan oleh Graylog untuk mengamankan penyimpanan kata sandi pengguna (dalam semangat kunci pengasinan). Kunci ini haruslah **unik** dan **acak**.
- root_password_sha2**: parameter ini sesuai dengan kata sandi administrator default di Graylog. Password ini disimpan sebagai Hash SHA-256.



Kita akan mulai dengan membuat kunci 96 karakter untuk parameter **password_secret**:



```
pwgen -N 1 -s 96
wVSGYwOmwBIDmtQvGzSuBevWoXe0MWpNWCzhorBfvMMhia2zIjHguTbfl4uXZJdHOA0EEb1sOXJTZKINhIIBm3V57vwfQV59
```



Salin nilai yang dikembalikan, lalu buka file konfigurasi Graylog:



```
sudo nano /etc/graylog/server/server.conf
```



Rekatkan kunci ke dalam parameter **password_secret**, seperti ini:



![Image](assets/fr/027.webp)



Simpan dan tutup file.



Selanjutnya, Anda perlu mengatur kata sandi untuk akun "**admin**" yang dibuat secara default. Dalam file konfigurasi, Hash dari kata sandi harus disimpan, yang berarti kata sandi tersebut harus dihitung. Contoh di bawah ini memberikan Hash dari kata sandi "**LogsWells@**": sesuaikan nilainya dengan kata sandi Anda.



```
echo -n "PuitsDeLogs@" | shasum -a 256
6b297230efaa2905c9a746fb33a628f4d7aba4fa9d5c1b3daa6846c68e602d71
```



Salin nilai yang diperoleh sebagai keluaran (tanpa tanda hubung di akhir baris).



Buka kembali file konfigurasi Graylog:



```
sudo nano /etc/graylog/server/server.conf
```



Rekatkan nilai tersebut ke dalam opsi **root_password_sha2** seperti ini:



![Image](assets/fr/026.webp)



Ketika Anda berada dalam berkas konfigurasi, tetapkan opsi "**http_bind_address**". Tentukan "**0.0.0.0:9000**" sehingga web Interface Graylog dapat diakses pada port **9000**, melalui IP server Address.



![Image](assets/fr/024.webp)



Kemudian atur opsi "**elasticsearch_hosts**" ke `http://127.0.0.1:9200` untuk mendeklarasikan instans OpenSearch lokal kita. Ini diperlukan, karena kita tidak menggunakan **Graylog Data Node**. Dan tanpa opsi ini, kita tidak dapat melangkah lebih jauh...



![Image](assets/fr/025.webp)



Simpan dan tutup file.



Perintah ini mengaktifkan Graylog sehingga memulai secara otomatis pada boot berikutnya, dan segera meluncurkan server Graylog.



```
sudo systemctl enable --now graylog-server
```



Setelah ini selesai, cobalah untuk menyambung ke Graylog dari peramban. Masukkan IP server Address (atau nama) dan port 9000.



**Untuk informasi Anda:**



Belum lama ini, jendela autentikasi yang mirip dengan jendela di bawah ini muncul ketika Anda pertama kali masuk ke Graylog. Anda harus memasukkan login "**admin**" dan kata sandi Anda. Dan kemudian Anda akan terkejut ketika mengetahui bahwa koneksi tidak berhasil.



![Image](assets/fr/031.webp)



Perlu untuk kembali ke baris perintah pada server Graylog dan membaca log. Kita kemudian dapat melihat bahwa **untuk koneksi pertama**, perlu **menggunakan kata sandi sementara**, yang ditentukan dalam log.



```
tail -f /var/log/graylog-server/server.log
```



![Image](assets/fr/021.webp)



Anda kemudian harus mencoba kembali koneksi dengan pengguna "**admin**" dan kata sandi sementara, dan ini memungkinkan Anda untuk masuk!



**Hal ini sudah tidak berlaku lagi. Yang harus Anda lakukan adalah masuk dengan akun admin dan kata sandi yang dikonfigurasikan pada baris perintah



![Image](assets/fr/033.webp)



**Selamat datang di Interface Graylog!



![Image](assets/fr/019.webp)



#### E. Graylog: membuat akun administrator baru



Daripada menggunakan akun admin yang dibuat secara bawaan oleh Graylog, Anda dapat membuat akun administrator pribadi Anda sendiri. Klik pada menu "**Sistem**", lalu pada "**Pengguna dan Tim**" untuk mengklik tombol "**Buat pengguna**". Kemudian isi formulir dan tetapkan peran administrator ke akun Anda.



![Image](assets/fr/020.webp)



Akun yang dipersonalisasi dapat berisi informasi tambahan, seperti nama depan dan belakang serta email Address, tidak seperti akun admin asli. Selain itu, hal ini memastikan penelusuran yang lebih baik ketika setiap orang bekerja dengan akun bernama.



## Kirim log ke Graylog dengan rsyslog



### I. Presentasi



Pada bagian kedua ini, kita akan mempelajari cara mengonfigurasi mesin Linux untuk mengirim log ke server Graylog. Untuk melakukannya, kita akan menginstal dan mengkonfigurasi Rsyslog pada sistem.



### II. Mengkonfigurasi Graylog untuk menerima log Linux



Kita akan mulai dengan mengkonfigurasi Graylog. Ada tiga langkah yang harus diselesaikan:





- Pembuatan **Input** untuk membuat titik masuk yang memungkinkan mesin Linux untuk **mengirim log Syslog melalui UDP**.
- Pembuatan **Indeks** baru untuk menyimpan dan **mengindeks semua log Linux**.
- Pembuatan **Stream** untuk **mengalihkan** log yang diterima oleh Graylog ke Indeks Linux yang baru.



#### A. Membuat Input untuk Syslog



Masuk ke Graylog Interface, klik "**System**" pada menu dan kemudian pada "**Input**". Pada daftar drop-down, pilih "**Syslog UDP**" kemudian klik tombol berlabel "**Luncurkan input baru**". Anda juga dapat membuat Input Syslog TCP, tetapi ini memerlukan penggunaan sertifikat TLS: nilai tambah untuk keamanan, tetapi tidak dibahas dalam artikel ini.



![Image](assets/fr/001.webp)



Sebuah wizard akan muncul di layar. Mulailah dengan memberi nama pada Input ini, misalnya "**Graylog_UDP_Rsyslog_Linux**" dan pilih port. Secara default, portnya adalah "**514**", tetapi Anda dapat mengubahnya. Di sini, port "**12514**" dipilih.



![Image](assets/fr/016.webp)



Anda juga dapat mencentang opsi "**Simpan pesan lengkap**" untuk menyimpan pesan log lengkap di Graylog. Klik "**Luncurkan Input**".



![Image](assets/fr/017.webp)



Input baru telah dibuat dan sekarang aktif. Graylog sekarang dapat menerima log Syslog pada port 12514/UDP, tetapi kita belum selesai mengonfigurasi aplikasi.



![Image](assets/fr/018.webp)


**Catatan: satu Input dapat digunakan untuk menyimpan log dari beberapa mesin Linux.



#### B. Membuat Indeks Linux baru



Kita perlu membuat Indeks di Graylog untuk menyimpan log dari mesin Linux. Sebuah **index** di Graylog adalah struktur penyimpanan yang berisi log yang diterima, yaitu pesan yang diterima. Graylog menggunakan OpenSearch sebagai mesin penyimpanannya, dan pesan-pesan diindeks untuk memungkinkan pencarian yang cepat dan efisien.



Dari Graylog, klik "**System**" pada menu, kemudian pada "**Indices**". Pada halaman baru yang muncul, klik "**Create index set**".



![Image](assets/fr/005.webp)



Beri nama indeks ini, misalnya "**Linux Index**", tambahkan deskripsi dan awalan, sebelum mengonfirmasi. Di sini, kita akan menyimpan semua log Linux dalam indeks ini. Anda juga dapat membuat indeks khusus untuk menyimpan log tertentu saja (hanya log [SSH] (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/ "SSH"), log layanan Web, dll.).



![Image](assets/fr/006.webp)



Sekarang kita perlu membuat stream baru untuk merutekan pesan ke indeks ini.



#### C. Membuat Aliran



Untuk membuat stream baru, klik "**Streams**" di menu utama Graylog. Kemudian klik tombol "**Buat stream**" di sebelah kanan. Pada jendela yang muncul, beri nama stream, misalnya "**Linux Stream**" dan pilih indeks "**Linux Index**" untuk bidang bernama "**Index Set**". Konfirmasikan pilihan Anda.



**Catatan: pesan yang terkait dengan stream ini juga akan disertakan dalam "**Default Stream**", kecuali jika Anda mencentang opsi "**Hapus kecocokan dari 'Default Stream'**".



![Image](assets/fr/002.webp)



Kemudian, dalam pengaturan steam Anda, klik tombol "**Tambahkan aturan stream**" untuk menambahkan aturan perutean pesan baru. Jika Anda tidak dapat menemukan jendela ini, klik "**Streams**" pada menu, lalu pada baris yang sesuai dengan stream Anda, klik "**Lebih Banyak**" lalu "**Kelola Aturan**".



Pilih jenis "**cocokkan input**" dan pilih **input Rsyslog yang telah dibuat sebelumnya di UDP**. Konfirmasikan dengan tombol "**Buat Aturan**". Semua pesan ke Input baru kita sekarang akan dikirim ke Index untuk Linux.



![Image](assets/fr/003.webp)



Stream baru Anda akan muncul dalam daftar dan harus dalam status "**Berjalan**". Bandwidth pesan menunjukkan "**0 msg/s**", karena saat ini kami tidak mengirimkan log apa pun ke input UDP Rsyslog. Untuk melihat log aliran, cukup klik pada namanya.



![Image](assets/fr/004.webp)



**Semuanya sudah siap di sisi Graylog**. Langkah selanjutnya adalah mengkonfigurasi mesin Linux.



### III. Menginstalasi dan mengkonfigurasi Rsyslog pada Linux



Masuk ke mesin Linux, baik secara lokal maupun jarak jauh, dan gunakan akun pengguna dengan hak akses untuk meningkatkan privilese (melalui sudo). Jika tidak, gunakan akun "root" secara langsung.



#### A. Menginstal paket Rsyslog



Mulailah dengan memperbarui cache paket dan menginstal paket bernama "**rsyslog**".



```
sudo apt-get update
sudo apt-get install rsyslog
```



Kemudian periksa status layanan. Pada kebanyakan kasus, layanan ini sudah berjalan.



```
sudo systemctl status rsyslog
```



#### B. Mengkonfigurasi Rsyslog



Rsyslog memiliki file konfigurasi utama yang terletak di sini:



```
/etc/rsyslog.conf
```



Selain itu, direktori "**/etc/rsyslog.d/**" digunakan untuk menyimpan file konfigurasi tambahan untuk Rsyslog. Pada berkas konfigurasi utama, terdapat perintah Include untuk mengimpor semua berkas "**.conf**" yang berada pada direktori ini. Hal ini memungkinkan adanya file tambahan untuk mengkonfigurasi Rsyslog tanpa mengubah file utama.



Pada direktori ini, Anda harus menggunakan angka untuk menentukan urutan pemuatan, karena file dimuat dalam urutan abjad. Menambahkan awalan numerik memungkinkan Anda untuk mengatur prioritas di antara beberapa file konfigurasi. Di sini, kita hanya memiliki satu berkas tambahan, jadi tidak masalah.



Dalam direktori ini, kita akan membuat berkas bernama "**10-graylog.conf**":



```
sudo nano /etc/rsyslog.d/10-graylog.conf
```



Dalam file ini, sisipkan baris ini:



```
*.* @192.168.10.220:12514;RSYSLOG_SyslogProtocol23Format
```



Berikut ini cara menafsirkan baris ini:





- `*.*`: berarti mengirim semua log Syslog dari mesin Linux ke Graylog.
- `@`: mengindikasikan bahwa transportasi dilakukan dalam UDP. Anda harus menentukan "**@@**" untuk beralih ke TCP.
- `192.168.10.220:12514`: menunjukkan Address dari server Graylog, dan port yang digunakan untuk mengirim log (sesuai dengan Input).
- `RSYSLOG_SyslogProtocol23Format`: sesuai dengan format pesan yang akan dikirim ke Graylog.



Setelah selesai, simpan file dan mulai ulang Rsyslog.



```
sudo systemctl restart rsyslog.service
```



Setelah tindakan ini, pesan pertama akan tiba di server Graylog Anda!



### IV. Menampilkan log Linux di Graylog



Dari Graylog, Anda dapat mengklik "**Streams**" dan pilih stream baru Anda untuk melihat pesan terkait. Atau, klik "**Pencarian**" dan pilih Steam Anda dan luncurkan pencarian.



Berikut ini sebagian fitur utama Interface:



**1** - Pilih periode untuk menampilkan pesan. Secara default, pesan dari 5 menit terakhir ditampilkan.



**2** - Pilih stream yang akan ditampilkan.



**3** - Aktifkan penyegaran otomatis daftar pesan (setiap 5 detik, misalnya). Jika tidak, daftar pesan akan menjadi statis dan Anda harus menyegarkannya secara manual.



**4** - Klik pada kaca pembesar untuk meluncurkan pencarian setelah mengubah periode, aliran, atau filter.



**5** - Bilah masukan untuk menentukan filter pencarian Anda. Di sini, saya menetapkan "**source:srv\-docker**" untuk hanya menampilkan log dari mesin baru yang baru saja saya siapkan Rsyslog.



Log dikirim oleh mesin Linux:



![Image](assets/fr/015.webp)



### V. Mengidentifikasi kegagalan sambungan SSH



Kekuatan Graylog terletak pada kemampuannya untuk mengindeks log dan memungkinkan pencarian dilakukan menurut berbagai kriteria: mesin sumber, Timestamp, isi pesan, dll... Kita bisa mencari untuk mengidentifikasi koneksi SSH yang gagal.



Dari mesin jarak jauh (server Graylog, misalnya), coba sambungkan ke server Linux yang baru saja Anda konfigurasikan Rsyslog. Sebagai contoh:



```
ssh [email protected]
```



Kemudian dengan sengaja memasukkan **username** dan **password** yang salah, untuk **kesalahan koneksi generate**. Pada file "**/var/log/auth.log**", ini akan mencatat pesan log generate yang serupa dengan yang berikut ini:



```
Failed password for invalid user it-connect from 192.168.10.199 port 50352 ssh2
```



Anda akan menemukan pesan-pesan ini di Graylog.



Pada Graylog, gunakan filter pencarian berikut untuk menampilkan hanya pesan yang cocok:



```
message:Failed password AND application_name:sshd
```



Jika Anda memiliki beberapa server dan ingin menganalisis log server tertentu, tentukan namanya sebagai tambahan:



```
message:Failed password AND application_name:sshd AND source:srv\-docker
```



Berikut ini adalah ikhtisar hasil pada mesin di mana saya menghasilkan beberapa kesalahan koneksi, pada waktu yang berbeda dalam sehari:



![Image](assets/fr/009.webp)



Upaya koneksi yang gagal dilakukan dari mesin dengan IP Address "**192.168.10.199**". Jika Anda ingin tahu lebih banyak tentang aktivitas host ini, Anda dapat **mencari IP Address ini**. Graylog akan menampilkan semua log di mana IP Address ini direferensikan, pada semua host (yang pengiriman lognya dikonfigurasi).



Dalam hal ini, filter yang akan digunakan dapat berupa:



```
message:"192.168.10.199"
```



Kami mendapatkan hasil tambahan (tidak mengherankan, karena kami tidak memfilter pada aplikasi SSH):



![Image](assets/fr/008.webp)



### VI. Kesimpulan



Dengan mengikuti tutorial ini, Anda seharusnya dapat mengonfigurasi mesin Linux untuk mengirim lognya ke server Graylog. Dengan cara ini, Anda akan dapat memusatkan log dari hos Linux Anda di log sink Anda!



Untuk melangkah lebih jauh, pertimbangkan untuk membuat dasbor dan peringatan untuk menerima notifikasi ketika anomali terdeteksi.



![Image](assets/fr/007.webp)