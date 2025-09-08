---
name: Nmap
description: Master Nmap untuk pemetaan jaringan dan pemindaian kerentanan
---

![cover](assets/cover.webp)



*Tutorial ini didasarkan pada konten asli oleh Mickael Dorigny yang dipublikasikan di [IT-Connect](https://www.it-connect.fr/). Lisensi [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Perubahan telah dilakukan pada teks asli.*



___



Selamat datang di tutorial pengantar Nmap ini, yang dirancang untuk siapa saja yang ingin menguasai alat pemindaian jaringan yang hebat ini. Tujuannya adalah untuk memberi Anda pengetahuan dasar yang Anda perlukan untuk menggunakan Nmap secara efektif sehari-hari.



Nmap adalah alat serbaguna yang banyak digunakan oleh para profesional TI, jaringan dan keamanan siber untuk diagnostik, penemuan jaringan, dan audit keamanan. Tutorial ini ditujukan untuk mereka yang baru mengenal bidang ini dan ingin mempelajari dasar-dasar Nmap. Disarankan untuk memiliki pengetahuan dasar tentang sistem dan administrasi jaringan.



Anda akan mempelajari dasar-dasar Nmap, cara melakukan pemindaian port, mengidentifikasi host yang aktif di jaringan, mendeteksi versi layanan dan sistem operasi, melakukan pemindaian kerentanan, dan banyak lagi. Setiap bagiannya mencakup penjelasan mendetail dan contoh-contoh praktis untuk membantumu menguasai penggunaan Nmap dalam berbagai konteks.



Pada akhir tutorial ini, kamu akan memiliki pemahaman yang kuat tentang Nmap dan dapat menggunakannya secara efektif untuk meningkatkan keamanan dan manajemen jaringan kamu. Selamat membaca.



## 1 - Pengantar ke Nmap: Apa itu Nmap?



### I. Presentasi



Pada bagian pertama ini, kita akan melihat alat pemindaian jaringan Nmap. Kita akan melihat kunci Elements yang perlu Anda ketahui tentang alat ini dan cara kerjanya secara umum. Ini akan membantu kita untuk lebih memahami bagian tutorial selanjutnya.



### II. Memperkenalkan alat bantu Nmap



Nmap, untuk _Network Mapper_, adalah alat sumber terbuka gratis yang digunakan untuk **penemuan jaringan, pemetaan, dan audit keamanan**. Alat ini juga bisa digunakan untuk tugas-tugas lain seperti inventarisasi jaringan, diagnostik, atau pengawasan.



Nmap dapat menentukan apakah host pada jaringan yang ditargetkan aktif dan dapat dijangkau, layanan jaringan mana yang terbuka, versi dan teknologi apa yang digunakan, dan informasi analisis lain yang berguna. Nmap dapat digunakan untuk memindai layanan tunggal pada mesin tertentu, atau di sebagian besar jaringan, hingga seluruh Internet.



Kekuatan Nmap sangat banyak:





- Kuat dan fleksibel**: Nmap dapat memindai jaringan yang besar dan menggunakan teknik deteksi tingkat lanjut. Nmap mendukung UDP, TCP, ICMP, IPv4 dan IPv6, dan dapat melakukan deteksi versi, pemindaian kerentanan, atau interaksi khusus protokol. Arsitekturnya modular, khususnya berkat skrip NSE (Nmap Scripting Engine), yang akan kita lihat nanti dalam tutorial ini.
- Kemudahan penggunaan**: dokumentasi resmi berlimpah dan berkualitas tinggi. Berbagai sumber daya komunitas juga tersedia untuk membantu Anda memulai.
- Popularitas dan umur panjang**: Nmap telah menjadi referensi di bidangnya sejak tahun 1998. Versi saat ini, pada saat pembaruan ini, adalah 7.95. Meskipun ada alat lain untuk tugas-tugas tertentu, Nmap tetap harus dimiliki untuk pemetaan dan analisis jaringan.



**Nmap di bioskop**



Nmap adalah salah satu dari beberapa alat keamanan yang telah mendapatkan ketenaran tertentu di kalangan masyarakat umum. Nmap muncul dalam film _Matrix Reloaded_, dalam adegan simbolis di mana Trinity menggunakannya untuk meretas sebuah sistem:



![nmap-image](assets/fr/01.webp)



matriks: Adegan yang dimuat ulang yang menampilkan Nmap



Ia juga muncul dalam karya sinematografi lainnya.



**Umpan balik



Sebagai seorang administrator sistem dan kemudian auditor dan pentester keamanan siber, **Saya menggunakan Nmap hampir setiap hari** dan saya **secara teratur merekomendasikannya kepada administrator sistem yang ingin memperkuat penguasaan jaringan dan meningkatkan kemampuan diagnostik mereka.



### III. Operasi tingkat tinggi



Nmap tersedia untuk Linux, Windows dan macOS. Nmap sebagian besar ditulis dalam bahasa C, C++ dan Lua (untuk skrip NSE). Nmap terutama digunakan pada baris perintah, meskipun antarmuka grafis seperti Zenmap juga tersedia. Namun, kami sangat menyarankan Anda untuk memulai dengan baris perintah untuk lebih memahami cara kerjanya.



Sebuah contoh sederhana:



```
nmap 192.168.10.13 10.10.10.0/24 -sV -sC --top-ports 250
```



Perintah ini akan dijelaskan secara rinci nanti. Dalam tutorial ini, kita akan menggunakan Nmap pada Linux, tetapi penggunaannya serupa pada sistem lain. Pada Windows, Nmap bergantung pada pustaka **Npcap** (menggantikan WinPcap yang sudah tidak digunakan lagi) untuk menangkap dan menginjeksi paket jaringan.



Nmap digunakan seperti biner konvensional, seperti `ls` atau `ip`. Beberapa fitur tingkat lanjut mungkin memerlukan hak yang lebih tinggi, karena alat ini terkadang memanipulasi paket dengan cara yang tidak biasa untuk memancing reaksi tertentu pada sistem target (terutama untuk layanan atau deteksi kerentanan).



### IV. Dampak penggunaan Nmap



Sebelum menggunakan Nmap, sangat penting untuk mengetahui potensi dampaknya pada jaringan dan sistem:





- Ia dapat mengirim **ribuan atau bahkan jutaan paket** dalam waktu singkat, yang dapat memenuhi infrastruktur jaringan tertentu.
- Ini dapat generate **paket **cacat atau non-standar**, yang cenderung mengganggu peralatan tertentu (terutama sistem industri).
- Hal ini dapat menghasilkan **perilaku seperti serangan**, yang dapat memicu peringatan pada sistem keamanan (firewall, IDS/IPS, dll.).



Secara umum, **Nmap adalah alat yang sangat banyak bicara**, karena alat ini menghasilkan banyak lalu lintas untuk mengekstrak informasi sebanyak mungkin. Oleh karena itu, disarankan untuk memahami sepenuhnya cara kerjanya sebelum menggunakannya pada lingkungan yang sensitif atau produksi.



### V. Kesimpulan



Bagian ini memperkenalkan Nmap dan fitur-fitur utamanya. Kita telah melihat bahwa Nmap adalah alat pemetaan jaringan yang penting, kuat, dan fleksibel. Kita juga telah membahas cara kerjanya dan tindakan pencegahan yang perlu Anda lakukan saat menggunakannya, untuk menyiapkan latar belakang untuk bagian tutorial berikutnya.



## 2 - Mengapa menggunakan Nmap?



### I. Presentasi



Pada bagian ini, kita akan melihat penggunaan utama alat pemindaian jaringan Nmap. Kita akan melihat bahwa ini adalah alat yang digunakan secara luas dalam banyak konteks dan profesi, dan memilikinya di kotak peralatan Anda dan mengetahui cara menguasainya jelas merupakan keterampilan yang berguna.



### II. Menggunakan Nmap untuk diagnostik dan pengawasan



Nmap dapat digunakan untuk diagnosa jaringan dan, lebih luas lagi, untuk monitoring. Dengan cara yang sama seperti ping dapat digunakan untuk menentukan apakah dua host berkomunikasi, Nmap dapat digunakan untuk menentukan dengan cepat apakah sebuah host aktif, atau apakah layanan tertentu beroperasi. Berkat [Nmap] (https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/ "Nmap"), kita dapat memperoleh data yang tepat mengenai waktu respon host, rute yang diambil oleh paket, respon yang dibuat oleh layanan tertentu, dll.



Perintah dan hasil berikut ini dapat digunakan, misalnya, untuk mengetahui dengan cepat apakah server web pada host **192.168.1.18** aktif dan merespons dengan benar:



```
nmap --open -p 80 192.168.1.18
```



![nmap-image](assets/fr/02.webp)



*Gunakan Nmap untuk mengambil status layanan web dari server jarak jauh*



Jadi, menggunakan Nmap lebih jauh daripada "tes ping" yang terkenal selama fase debugging atau diagnostik. Kita akan melihat nanti bahwa ada beberapa metode yang digunakan oleh Nmap untuk mengidentifikasi layanan mana yang mendengarkan pada port tertentu, termasuk versinya.



### III. Menggunakan Nmap untuk pemetaan jaringan



Sebagai _Network Mapper_, pemetaan jaringan adalah tujuan utama alat ini. Alat ini dapat digunakan dalam jaringan lokal, atau di beberapa jaringan, subnet, dan VLAN, untuk membuat daftar semua host dan layanan yang dapat dijangkau. Nmap membuat tugas ini jauh lebih cepat dan lebih efisien daripada metode manual.



Sebagai contoh, perintah berikut ini dapat digunakan untuk mengidentifikasi host yang aktif di jaringan **192.168.1.0/24** dengan cepat:



```
nmap -sn 192.168.1.0/24
```



*Catatan: opsi `-sP` sudah tidak berlaku dan sudah digantikan oleh `-sn`.*



![nmap-image](assets/fr/03.webp)



*Menggunakan Nmap untuk menemukan host yang dapat dijangkau di jaringan*



Kita akan melihat nanti bahwa ada beberapa metode yang digunakan oleh Nmap untuk menentukan apakah sebuah host dapat dianggap "aktif", bahkan jika host tersebut tidak mengekspos layanan apa pun secara apriori.



### IV. Menggunakan Nmap untuk mengevaluasi kebijakan penyaringan



Nmap memiliki keuntungan karena bersifat faktual: hasilnya memungkinkan untuk membuat temuan konkret, tidak seperti dokumen arsitektur atau kebijakan penyaringan. Nmap adalah alat utama untuk menilai efektivitas kompartementalisasi sistem informasi, karena memungkinkan Anda untuk **memverifikasi apakah kebijakan penyaringan benar-benar diterapkan**.



Dalam jaringan perusahaan, praktik terbaik menyatakan bahwa sistem harus disegmentasi menurut peran, kekritisan, atau lokasinya. Aturan penyaringan (sering diimplementasikan melalui firewall) harus membatasi komunikasi antar zona. Tetapi konfigurasi ini sering kali rumit dan rentan terhadap kesalahan.



Jadi, untuk memvalidasi bahwa kebijakan telah dipatuhi, tidak ada yang bisa mengalahkan tes konkret. Sebagai contoh, Anda bisa memeriksa bahwa layanan administrasi yang sensitif (SSH, WinRM, MSSQL, MySQL, dll.) tidak dapat diakses dari zona pengguna.



Penggunaan **Nmap untuk menguji kebijakan penyaringan** haruslah sistematis sebelum kebijakan tersebut dimasukkan ke dalam produksi. Sayangnya, pemeriksaan ini sering diabaikan.



Menurut pengalaman saya, banyak kesalahan konfigurasi yang tidak diketahui karena tidak adanya uji validasi. Kesalahan sederhana dalam rentang IP atau kekeliruan aturan dapat membuat zona yang seharusnya terisolasi menjadi rentan.



### V. Menggunakan Nmap untuk audit keamanan dan pengujian penetrasi



Nmap memiliki **banyak fitur yang berguna untuk penilaian keamanan**, pengujian penetrasi (pentest), dan sayangnya juga untuk penyerang.



Fungsi penemuan jaringan sangat penting bagi penyerang, yang perlu memahami topologi jaringan setelah kompromi awal. Tetapi Nmap menawarkan lebih dari itu: dia mengintegrasikan mesin skrip, **banyak di antaranya didedikasikan untuk deteksi kerentanan**.



Sebagai contoh, perintah ini dapat digunakan untuk memeriksa apakah layanan FTP mengizinkan koneksi anonim, tanpa harus terhubung secara manual:



```
nmap --script ftp-anon -p 21 192.168.1.18
```



![nmap-image](assets/fr/04.webp)



*Menggunakan skrip NSE untuk memeriksa autentikasi FTP anonim melalui Nmap.*



Deteksi kerentanan Nmap adalah salah satu langkah pertama dalam audit atau uji penetrasi. Ini memungkinkan Anda untuk dengan cepat mengidentifikasi titik-titik lemah tertentu dan mengoptimalkan upaya analisis Anda.



Namun berhati-hatilah: **Alat pemindaian kerentanan memiliki keterbatasan**. Nmap hanya mencakup sebagian kecil ancaman, dan tidak menjamin bahwa suatu sistem aman jika tidak ada masalah yang terdeteksi. Oleh karena itu, penting untuk **memahami cara kerja skrip yang digunakan** dan tidak hanya bergantung pada keputusan mereka.



### VI. Kesimpulan



Kita telah melihat bahwa menguasai Nmap dapat mencakup berbagai macam kasus penggunaan, mulai dari diagnostik dan pemantauan hingga pemetaan, evaluasi kebijakan keamanan, dan pemindaian kerentanan. Di bagian selanjutnya, kita akan membahas seluk-beluk dan menginstal Nmap.




## 3 - Menginstalasi dan mengonfigurasi Nmap



### I. Presentasi



Pada bagian ini, kita akan mempelajari cara menginstal alat pemindaian jaringan Nmap pada OS Linux dan Windows. Di akhir bagian ini, kita akan memiliki semua yang kita perlukan untuk mulai menggunakan Nmap untuk modul-modul selanjutnya. Terakhir, kita akan melihat hak istimewa apa yang mungkin diperlukan saat digunakan dan mengapa.



### II. Menginstalasi Nmap di Linux



Nmap pada awalnya dirancang untuk berjalan pada sistem operasi GNU/Linux. Sebagai hasilnya, dan berkat umur panjang dan popularitasnya, Anda akan menemukannya di semua repositori resmi distribusi Unix utama. Dalam tutorial ini, saya akan menggunakan sistem operasi berbasis Debian [Kali Linux] (https://www.it-connect.fr/cours/debuter-avec-kali-linux/ "Kali Linux"). Tetapi Anda bisa menggunakannya dengan cara yang sama persis dengan Debian klasik, CentOS, Red Hat, atau apa pun!



Pada Debian, untuk memeriksa apakah Nmap ada pada repositori Anda saat ini, Anda dapat menggunakan perintah berikut:



```
# Debian and derivatives
$ sudo apt search ^nmap$
Sorting... Done
Full Text Search... Done
nmap/kali-rolling,now 7.94+git20230807.3be01efb1+dfsg-2+kali1 amd64
The Network Mapper

# Red Hat and derivatives
$ dnf search '^nmap$'
```



Jawaban di sini dengan jelas menunjukkan bahwa paket "nmap" ada di repositori (di sini, repositori Kali [Linux](https://www.it-connect.fr/cours-tutoriels/administration-systemes/linux/ "Linux")). Mulai sekarang, Anda dapat menginstal Nmap melalui perintah instalasi biasa, tidak ada yang dilucuti untuk saat ini 🙂:



```
# Debian and derivatives
sudo apt install nmap

# Red Hat and derivatives
sudo dnf install nmap
```



Untuk memeriksa apakah Nmap terinstal dengan benar, kami akan menampilkan versinya:



```
nmap --version
```



Inilah hasil yang diharapkan:



![nmap-image](assets/fr/05.webp)



hasil dari menampilkan versi Nmap._ saat ini



Perhatikan keberadaan pustaka "libpcap" (_Packet Capture Library_) dan versinya. Juga digunakan oleh Wireshark, "libpcap" digunakan oleh Nmap untuk membuat dan memanipulasi paket dan mendengarkan lalu lintas jaringan.



### III Menginstalasi Nmap pada Windows



Untuk menginstal pada sistem operasi Windows, mulailah dengan mengunduh biner dari situs resminya (dan bukan yang lain!):





- Halaman pengunduhan Nmap di situs web resmi: [https://nmap.org/download.html#windows](https://nmap.org/download.html#windows)




Anda kemudian perlu mengunduh biner bernama `nmap-<VERSION>-setup.exe`:



![nmap-image](assets/fr/06.webp)



halaman unduhan biner instalasi nmap untuk Windows



Setelah Anda memiliki biner ini di sistem Anda, cukup jalankan untuk menginstal Nmap. Ini adalah instalasi yang mudah, dan Anda bisa membiarkan semua opsi sebagai default.



Refleks saya adalah menghapus centang pada kotak "zenmap (GUI Frontend)". Ini adalah Interface grafis untuk Nmap yang tidak saya gunakan dan tidak akan dibahas dalam tutorial ini, tetapi silakan mencobanya setelah Anda menguasai alat baris perintah Nmap!



![nmap-image](assets/fr/07.webp)



pilihan opsional untuk membatalkan pemilihan Zenmap saat menginstal Nmap di Windows



Pada akhir instalasi Nmap, instalasi kedua diusulkan: instalasi pustaka "Npcap":



![nmap-image](assets/fr/08.webp)



pemasangan pustaka "Npcap" saat menginstal Nmap di bawah Windows



Ini adalah pustaka yang diandalkan Nmap untuk mengelola komunikasi jaringan, yaitu membangun, mengirim, dan menerima paket jaringan. Anda mungkin sudah pernah menemukan pustaka ini jika Anda menggunakan Wireshark di Windows, karena Wireshark juga menggunakannya dan memerlukan instalasi.



Seperti pada Linux, Anda dapat memvalidasi bahwa Nmap telah terinstal dengan membuka Command Prompt atau terminal [Powershell] (https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/ "Powershell") dan mengetikkan perintah berikut:



```
nmap --version
```



Inilah hasil yang diharapkan:



![nmap-image](assets/fr/09.webp)



hasil dari menampilkan versi Nmap._ saat ini



Nmap sekarang sudah terinstal pada Windows. Anda dapat menggunakannya dengan cara yang sama persis seperti pada Linux, dengan mengikuti tutorial ini.



### IV. Hak istimewa lokal yang diperlukan untuk menggunakan Nmap



Namun, ketika menggunakan Nmap, **apakah perlu memiliki hak istimewa lokal yang lebih tinggi pada sistem** Jawabannya adalah: **tergantung**.



Dalam bentuknya yang paling dasar, yaitu tanpa terlalu banyak menggunakan opsi-opsinya, Nmap tidak memerlukan hak istimewa. Namun, Anda akan segera menyadari bahwa lebih baik menggunakan Nmap dalam konteks hak istimewa ("root" pada Linux, "administrator" atau yang setara pada Windows) untuk dapat menggunakannya secara maksimal, dengan risiko mendapatkan pesan kesalahan seperti ini:



![nmap-image](assets/fr/10.webp)



pesan kesalahan di Linux ketika opsi Nmap memerlukan hak root._



Baik pada Linux atau Windows, ada banyak kasus di mana Nmap akan meminta Anda untuk mendapatkan akses istimewa. Alasan utamanya adalah sebagai berikut (daftar tidak lengkap):





- Membangun paket jaringan "mentah" **: Nmap mampu melakukan berbagai macam metode pemindaian, termasuk manipulasi dan konstruksi paket tingkat lanjut. Hal ini terjadi, misalnya, ketika kita ingin melakukan pemindaian TCP SYN, yang tidak menghormati jabat tangan _Tiga arah_ klasik pertukaran TCP. Untuk melakukan hal ini, Nmap perlu menggunakan fungsi selain dari fungsi asli sistem operasi, yang hanya tahu bagaimana menghormati praktik yang baik dalam komunikasi jaringan (Nmap memanggil pustaka "Npcap" dan "libcap" yang terlihat di atas). Karena Nmap tidak melakukan sesuatu dengan cara "standar", Nmap dapat menyimpulkan informasi tertentu tentang OS, layanan, dan kerentanan tertentu.





- Mendengarkan lalu lintas jaringan**: beberapa opsi Nmap mengharuskannya mendengarkan jaringan untuk mengambil informasi tertentu. Tindakan ini dianggap sensitif pada sistem operasi, karena juga memungkinkan Anda untuk mendengarkan komunikasi aplikasi lain pada sistem. Sama seperti Wireshark, Nmap membutuhkan hak istimewa khusus untuk melakukan hal ini, yang lebih mudah diperoleh dengan berada langsung dalam sesi istimewa.





- Mendengarkan pada port yang diistimewakan**: pada sistem operasi, port dari 0 sampai 1024 (TCP dan juga UDP) dikatakan diistimewakan, yaitu port-port tersebut disediakan untuk penggunaan yang sangat spesifik dan oleh karena itu dilindungi. Meskipun ini adalah alasan yang agak usang saat ini, masih perlu untuk memiliki hak istimewa tertentu untuk mendengarkan pada port-port ini, yang mungkin harus dilakukan oleh Nmap tergantung pada bagaimana port tersebut akan digunakan.





- Mengirim paket UDP:** Demikian pula, mendengarkan aplikasi jaringan pada port UDP (protokol tanpa nama) memerlukan hak istimewa pada sistem operasi. Oleh karena itu, sesi istimewa akan diperlukan jika Anda ingin melakukan pemindaian UDP, di mana Nmap harus mendengarkan respons untuk menganalisis balasan dari pemindaiannya.




Lebih tepatnya, dimungkinkan, setidaknya di bawah Linux, untuk menjalankan Nmap dengan semua fungsi dan pilihannya tanpa harus menjadi root. Hal ini dicapai dengan memberikan _kemampuan_ yang tepat pada biner. Namun, ini membutuhkan manipulasi tingkat lanjut dan mungkin tidak sepraktis menjalankan Nmap secara langsung dengan hak istimewa. Selain itu, pendekatan ini kurang umum dan dapat menimbulkan masalah keamanan jika salah konfigurasi.



Namun, ini sedikit menyimpang dari tutorial Nmap kami, jadi kami akan mengabaikannya untuk saat ini.



Untuk sisa tutorial ini, asumsikan bahwa Nmap selalu dijalankan sebagai "root" (dari sebuah shell sebagai "root" atau melalui perintah "sudo"), atau di terminal administrator di Windows, bahkan jika ini tidak ditunjukkan. Jika tidak, Anda mungkin akan mengalami perbedaan yang tidak kentara dari tutorial ini.



### V. Kesimpulan



Selesai! Nmap sekarang terinstal pada sistem operasi kita dan siap digunakan, tidak memerlukan konfigurasi lebih lanjut. Bagian ini menyimpulkan pengenalan dan presentasi Nmap. Saya harap ini membuat Anda tertarik, dan Anda bersemangat untuk mulai berlatih.



Pada catatan yang lebih serius, kita sekarang memiliki gambaran yang lebih baik tentang apa itu alat pemetaan Nmap dan apa penggunaan yang paling umum, serta keterbatasannya. Mari kita lanjutkan!




## 4 - Pemindaian port TCP dan UDP dengan Nmap



### I. Presentasi



Pada bagian ini, kita akan mempelajari cara melakukan pemindaian port pertama kita menggunakan alat pemindaian jaringan Nmap. Kita akan melihat cara menggunakannya untuk menyusun daftar layanan jaringan yang terbuka pada sebuah host, baik yang menggunakan protokol TCP atau UDP.



Mulai sekarang, ingatlah untuk memindai hanya host di lingkungan terkendali yang Anda miliki otorisasi eksplisitnya.





- Sebagai pengingat: [KUHP: Bab III: Serangan terhadap sistem pemrosesan data otomatis](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




**Jika Anda tidak memiliki satu pun**, saya merekomendasikan solusi gratis berikut ini, yang memang tepat!





- [Hack The Box](https://app.hackthebox.com/ "Hack The Box")**: Platform pelatihan peretasan, Hack The Box secara konstan menyediakan sistem-sistem yang rentan untuk Anda serang sesuai keinginan Anda. Beberapa ratus sistem tersedia, tetapi kumpulan 20 mesin yang diperbarui ditawarkan secara gratis sepanjang tahun, dengan akses melalui VPN OpenVPN.





- [Vulnhub](https://www.vulnhub.com/ "Vulnhub")**: Platform ini menawarkan banyak sistem yang sengaja dibuat rentan untuk diunduh, yang bisa digunakan melalui VirtualBox (juga solusi gratis) atau cara lainnya. Setelah diunduh, tidak perlu VPN - semuanya bersifat lokal.




Selain itu, Anda bebas untuk **membuat mesin virtual** pada sistem operasi favorit Anda dan menginstal berbagai layanan di dalamnya sebagai target pengujian. Keuntungannya, Anda juga dapat melihat apa yang terjadi di sisi server selama pemindaian, terutama dengan Wireshark, dan memiliki andil dalam firewall lokal saat kami melakukan pengujian yang lebih canggih.



Mari kita mulai berlatih!



### II. Memindai port TCP host melalui Nmap



#### A. Pemindaian port TCP pertama dengan Nmap



Sekarang kita akan melakukan pemindaian pertama melalui Nmap. Tujuan kita di sini sederhana: kita ingin mengetahui layanan apa saja yang diekspos oleh server web yang baru saja kita gunakan, untuk melihat apakah ada sesuatu yang tidak terduga, seperti layanan administrasi yang seharusnya tidak dapat diakses, atau ekspos port aplikasi yang kita kira telah dinonaktifkan.



Dalam contoh saya, host yang akan dipindai memiliki IP Address "192.168.1.18":



```
nmap 192.168.1.18
```



Ini adalah hasil yang mungkin terjadi. Kami melihat Nmap klasik kembali dengan banyak informasi:



![nmap-image](assets/fr/11.webp)



hasil pemindaian TCP sederhana yang dilakukan dengan Nmap._



Dengan melihat sekilas pada hasil ini, kami memahami bahwa port TCP/22 dan TCP/80 dapat diakses pada host ini.



Secara default, dan jika Anda tidak memerintahkannya, Nmap hanya akan memindai port TCP.



#### B. Memahami hasil pemindaian Nmap sederhana



Namun demikian, mari kita melangkah lebih jauh untuk memahami output ini: setiap baris penting, pertama untuk mengetahui apa yang baru saja dilakukan, dan kedua, menafsirkan hasil pemindaian itu sendiri secara tepat.



Baris pertama pada dasarnya adalah pengingat versi dan tanggal pemindaian (berguna untuk pencatatan dan pengarsipan):



```
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-29 21:59 CEST
```



Baris kedua menunjukkan awal hasil pemindaian untuk hos "debian.home (192.168.1.19)". Informasi ini akan berguna saat kita mulai memindai beberapa host secara bersamaan:



```
Nmap scan report for debian.home (192.168.1.19)
```



Baris ketiga memberi tahu kita bahwa host yang dimaksud adalah "Up", yaitu aktif:



```
Host is up (0.00022s latency).
```



Terakhir, Nmap memberi tahu kita bahwa 998 port TCP yang diidentifikasi sebagai port yang ditutup tidak ditampilkan dalam file:



```
Not shown: 998 closed tcp ports (conn-refused)
```



Hal ini menghemat hampir 1.000 baris output yang terlihat seperti:



```
1/tcp closed
2/tcp closed
3/tcp closed
…
```



Terima kasih kepada beliau yang telah menyelamatkan kami dari hal ini!



Mengapa 998 port "tertutup"? Dengan menambahkan 2 port terbuka menjadi 1000, dan itulah jumlah port yang akan dipindai oleh Nmap dalam konfigurasi defaultnya, bukan 65535 port TCP yang ada! Kita akan melihat nanti bahwa ini sepenuhnya dan dengan mudah dapat disesuaikan. Tetapi jika host yang ditargetkan memiliki layanan yang mendengarkan pada port yang agak eksotis, pemindaian "default" ini tidak akan menemukannya.



Mengikuti informasi ini, kami menemukan hal yang paling menarik: tabel yang disusun menurut tiga kolom "PORT - STATE - SERVICE":





- Kolom "PORT" yang pertama menunjukkan port/protokol yang ditargetkan, dan di sini penting untuk melihat apakah itu port TCP (`<port>/tcp`) atau UDP (`<port>/udp`).





- Kolom "STATE" menunjukkan status layanan jaringan yang ditemukan pada port ini dan ditentukan oleh Nmap berdasarkan respons yang diperoleh. Status ini dapat berupa "terbuka", "tertutup", "difilter", atau "tidak diketahui". Kita akan melihat nanti bagaimana Nmap membedakan antara status yang berbeda ini.





- Kolom "SERVICE" menunjukkan layanan yang terpapar pada port yang bersangkutan. Harap dicatat, bagaimanapun, bahwa kami tidak menggunakan opsi penemuan layanan aktif di sini. Nmap bergantung pada referensi lokal antara port/protokol dan layanan yang seharusnya diberikan: file "/etc/services"




Jika Anda melihat file "/etc/services" pada sistem Linux, Anda akan menemukan tautan "port/protocol - service" yang mirip dengan yang ditampilkan oleh Nmap:



![nmap-image](assets/fr/12.webp)



mengekstrak isi file "/etc/services" di bawah Linux._



Penting untuk dipahami bahwa, untuk saat ini, Nmap belum melakukan penemuan layanan aktif apa pun. Sebagai contoh, Nmap tidak akan dapat mengidentifikasi layanan SSH di belakang port TCP/80 jika ini terjadi. Oleh karena itu, penting untuk mengetahui cara menggunakan opsi yang tepat - ini akan segera hadir!



Mengetahui bagaimana menginterpretasikan output Nmap adalah bagian penting dalam menguasai alat ini. Kabar baiknya adalah bahwa output ini akan sama, apa pun opsi yang Anda gunakan.



#### C. Di balik tenda: analisis jaringan melalui Wireshark



Jika Anda melihat lebih dekat pada apa yang terjadi pada jaringan Interface dari host yang memindai server, atau pada server itu sendiri, tindakan Nmap akan lebih jelas. Itulah yang akan kita lakukan di sini.



Apa yang saya tunjukkan di sini hanyalah sebagian dari apa yang terlihat di Wireshark. Jika Anda ingin melangkah lebih jauh, silakan melakukan penangkapan jaringan sendiri selama pemindaian, dan kemudian menelusuri apa yang telah ditangkap.



Dalam pengujian ini, host pemindaian saya (192.168.1.18) dan host target saya (192.168.1.19) berada di jaringan lokal yang sama.



Nmap mulai dengan mencari tahu apakah host target aktif di jaringan lokal dengan mengirimkan permintaan ARP. Jika ia menerima respons, ia tahu bahwa host tersebut aktif dan memulai pemindaian jaringan:



![nmap-image](assets/fr/13.webp)



permintaan ARP yang dikeluarkan oleh Nmap untuk menentukan apakah host target ada di jaringan lokal



Jika host yang akan dipindai berada di jaringan jarak jauh, Nmap memulai dengan mengirimkan permintaan ping dan mencoba menjangkau beberapa port yang paling sering diekspos (TCP/80, TCP/443):



![nmap-image](assets/fr/14.webp)



permintaan ping yang dikeluarkan oleh Nmap untuk menentukan apakah host target dapat dijangkau di jaringan jarak jauh



Jika mendapatkan respons terhadap salah satu dari tes ini, ia menganggap target tersebut aktif.



Setelah Nmap menentukan bahwa targetnya aktif, Nmap akan mencoba menyelesaikan nama domain dengan server DNS yang dikonfigurasi pada kartu jaringan:



![nmap-image](assets/fr/15.webp)



resolusi dNS pada target pemindaian Nmap



Setelah Nmap mengidentifikasi targetnya dan mengetahui bahwa target tersebut aktif, Nmap memulai pemindaian port TCP:



![nmap-image](assets/fr/16.webp)



transmisi paket tCP SYN dan penerimaan RST/ACK selama pemindaian Nmap



Untuk melakukan ini, pada setiap port TCP dalam rentang defaultnya, **mengirim paket TCP SYN dan menunggu respons**. Pada tangkapan layar di atas, ia menerima paket TCP RST/ACK dari server yang dipindai, yang berarti "lanjutkan, tidak ada yang bisa dilihat di sini" - dengan kata lain, port-port ini ditutup. Seperti yang kita lihat pada hasilnya, ini akan terjadi pada sebagian besar port yang dipindai. Dengan dua pengecualian:



![nmap-image](assets/fr/17.webp)



respons terhadap paket TCP SYN yang dikirim pada port 22, aktif pada target pemindaian



Pada tangkapan layar di atas, kita melihat paket TCP SYN/ACK yang dikirim oleh host target**. Port tersebut aktif dan membuka sebuah layanan. Nmap mengakui penerimaan respons, kemudian mengakhiri koneksi (TCP RST/ACK). **Ini adalah bagaimana Nmap mengetahui bahwa port TCP/22 aktif**.



Kita telah melihat di sini bahwa Nmap menghormati "Jabat Tangan Tiga Arah" ketika memindai jaringan TCP. Untuk alasan kinerja, dimungkinkan untuk memintanya untuk tidak menanggapi balasan dari server, sehingga menghemat beberapa ribu paket ketika memindai jaringan yang besar. Tetapi kita akan melihat opsi dan pengoptimalan ini nanti dalam tutorial.



Sekarang kita memiliki gambaran yang lebih baik tentang bagaimana melakukan pemindaian TCP dan apa yang sebenarnya terjadi ketika dilakukan. Kita juga telah melihat bahwa, secara default, Nmap melakukan pemindaian port TCP pada sejumlah port yang terbatas.



### III. Memindai port UDP dengan Nmap



#### A. Pemindaian port UDP pertama dengan Nmap



Sekarang mari kita lihat cara memindai port UDP host. Seperti yang telah kita lihat, secara default Nmap akan selalu memindai port TCP. Ini bisa berarti kehilangan banyak informasi jika kita tidak menyadarinya.



Sebagai pengingat, untuk tujuan pengujian ini, host pemindaian saya (192.168.1.18) dan host target saya (192.168.1.19) berada pada jaringan lokal yang sama.



```
nmap -sU 192.168.1.19
```



Di sini, hasil yang diperoleh memiliki format yang sama dengan pemindaian TCP, tetapi layanan aktif yang ditampilkan berada di `<port>/UDP`, seperti yang diminta!



![nmap-image](assets/fr/18.webp)



hasil pemindaian UDP sederhana yang dilakukan dengan Nmap._



Opsi "-sU" digunakan untuk memberi tahu Nmap bahwa Anda ingin bekerja pada UDP, dan bukannya TCP seperti standarnya.



Ngomong-ngomong, Anda mungkin akan menyadari bahwa Nmap memerlukan hak "root" untuk pemindaian UDP, seperti yang disebutkan sebelumnya dalam tutorial ini.



catatan: Sejak versi terbaru Nmap, selalu disarankan untuk menjalankan pemindaian UDP dengan hak administrator untuk memastikan hasil yang andal, karena beberapa fitur memerlukan akses mentah ke soket jaringan



Pemindaian UDP dapat memakan waktu yang sangat lama (1100 detik untuk memindai 1000 port dalam contoh saya), karena tidak adanya "Three Way Handshake" dalam UDP, yang berarti bahwa Nmap akan menunggu balasan untuk setiap paket UDP yang dikirim, dan akan menentukan port tersebut sebagai "tertutup" hanya jika tidak ada balasan setelah waktu tertentu (timeout). Respons dari host yang dipindai ini tidak sistematis dan sering kali dibatasi dalam hal jumlah respons per detik, untuk menghindari serangan amplifikasi tertentu. Hal ini berbeda dengan TCP, di mana ada respon langsung dari host yang dipindai, baik port terbuka atau tertutup. Kita akan lihat nanti bagaimana cara mengoptimalkannya.



Kesulitan kedua dengan UDP adalah **bahwa layanan tidak selalu menanggapi paket yang masuk**, secara sederhana karena hal ini tidak selalu diperlukan dan ini adalah prinsip UDP. Ketika ini terjadi, dan tidak ada ICMP "port unreachable" yang diterima, layanan ditandai sebagai "open|filtered" oleh Nmap, seperti yang ditunjukkan pada gambar di atas.



#### B. Di balik tenda: analisis jaringan melalui Wireshark



Seperti halnya pemindaian TCP, mari kita lihat lebih dekat apa yang terjadi pada tingkat jaringan selama pemindaian UDP menggunakan analisis Wireshark. Perilaku Nmap dalam menentukan apakah sebuah host aktif atau tidak adalah sama.



Satu-satunya perbedaan nyata ketika memindai UDP adalah bahwa Nmap tidak akan menunggu "Jabat Tangan Tiga Arah", karena mekanisme ini tidak ada di UDP (protokol tanpa nama):



![nmap-image](assets/fr/19.webp)



transmisi paket uDP dan penerimaan ICMP (port tidak dapat dijangkau) selama pemindaian Nmap



Kita dapat melihat pada gambar di atas bahwa Nmap akan mengirim sejumlah besar paket UDP, dan menerima sebagian besar paket ICMP "Destination unreachable (Port unreachable)" sebagai respons. Hal ini normal, karena ini adalah respon yang sesuai yang ditentukan oleh [RFC 1122] (https://www.freesoft.org/CIE/RFC/1122/41.htm "RFC 1122") ketika port UDP tidak dapat dijangkau:



![nmap-image](assets/fr/20.webp)



ekstrak dari RFC 1122._



Mari kita cermati lebih dekat tangkapan Wireshark ini, yang menunjukkan **tiga skenario yang mungkin terjadi** dalam UDP:



![nmap-image](assets/fr/21.webp)



penangkapan jaringan selama pemindaian UDP pada port yang berbeda dengan Nmap._



Ketiga kasus tersebut adalah sebagai berikut:





- Exchange pertama terdiri dari paket no. 3, 4 dan 8, 9. Nmap mengirimkan paket UDP pada port SNMP klasik dan oleh karena itu **membuat paket yang sesuai dengan protokol terlebih dahulu**. Kemudian mendapatkan respons dari server (paket no. 8 dan 9). Hasil: Nmap telah menerima respons, layanan "terbuka".





- Exchange kedua terdiri dari paket 6 dan 7. Nmap mengirimkan paket UDP "kosong" (tanpa struktur protokol) ke port UDP/165, dan menerima paket ICMP sebagai balasan: "Tujuan tidak dapat dijangkau (Port tidak dapat dijangkau)". Hasil: Nmap telah menerima respons (negatif), host telah aktif, tetapi layanan yang dicoba untuk dijangkau tidak beroperasi pada port ini, yang akan ditandai sebagai "tertutup".





- Exchange terakhir terdiri dari paket no. 12: Nmap mengirimkan paket UDP "kosong" ke port UDP/1235. Tidak ada respons, bahkan penolakan eksplisit dari host yang dipindai. Hasil: Nmap menandai port sebagai "open|filtered", karena tidak dapat membedakan apakah ini disebabkan oleh adanya firewall, yang dikonfigurasi untuk tidak merespons, atau karena layanan UDP yang aktif yang tidak memberikan respons (tidak wajib dalam UDP).




Berikut adalah hasil yang ditampilkan oleh Nmap setelah ketiga kasus ini:



![nmap-image](assets/fr/22.webp)



kemungkinan hasil pemindaian UDP yang dilakukan melalui Nmap._



Sekarang kita memiliki gambaran yang lebih baik tentang cara melakukan pemindaian UDP dan apa yang sebenarnya terjadi ketika dilakukan. Sejauh ini kita baru saja menggunakan Nmap dengan cara yang sangat sederhana, tanpa benar-benar memutuskan port mana yang akan dipindai, tetapi itu akan segera berubah!



### IV. Menyempurnakan pemindaian port dengan Nmap



#### A. Pengingat perilaku default Nmap



Seperti yang telah kita lihat, Nmap sendiri yang memilih nomor dan port yang akan dipindai jika Anda tidak menentukan opsi apa pun. Ini adalah konfigurasi "default" yang digunakan oleh Nmap ketika Anda tidak memberi tahu apa yang harus dilakukan. Opsi default ini dirancang untuk memberikan gambaran tentang port utama yang terpapar, yang dipilih berdasarkan frekuensi paparan (port yang paling umum atau sering) daripada dalam urutan numerik (port 1, 2, 3, dst.) dan juga untuk menghindari memulai pemindaian 65535 kemungkinan port jika Anda tidak menentukan opsi yang sesuai, yang akan terlalu panjang dan bertele-tele untuk kasus penggunaan "default".



**Bagaimana port ini dipilih?



1000 port yang dipindai dalam mode default dipilih berdasarkan frekuensi kemunculannya. Statistik ini dikelola oleh Nmap dan diperbarui dengan cara yang sama seperti biner itu sendiri dan skrip (modul). Anda dapat melihat statistik ini di file "/usr/shares/nmap/nmap-services":



![nmap-image](assets/fr/23.webp)



diekstrak dari file "/usr/shares/nmap/nmap-services"._



Di sini, di kolom ketiga, kita melihat apa yang terlihat seperti probabilitas (antara 0 dan 1) atau distribusi persentase. Ini adalah frekuensi kemunculan setiap pasangan port/protokol. Kita dapat melihat bahwa port yang paling terkenal (FTP, SSH, TELNET dan SMTP dalam ekstrak ini) memiliki nilai yang jauh lebih tinggi daripada yang lain.



#### B. Menentukan port target dengan tepat untuk pemindaian Nmap



Namun, di dunia nyata, kita mungkin hanya perlu memindai port tertentu, atau beberapa port, atau rentang port tertentu. Nmap memudahkan untuk melakukan hal tersebut, dengan cara yang seragam untuk pemindaian UDP dan TCP.



**Memindai port tertentu melalui Nmap**



Jika kita ingin memindai satu port, dan bukan 1000, kita dapat menentukan port ini melalui opsi "-p" atau "--port" pada Nmap:



```
# Scan a single TCP port with Nmap
nmap 192.168.1.19 -p 80

# Scan a single UDP port with Nmap
nmap -sU 192.168.1.19 -p 161
```



Hasilnya, pemindaian secara alami akan jauh lebih cepat dan Nmap hanya akan memancarkan paket yang diperlukan untuk mendeteksi apakah host aktif, dan kemudian apakah port yang ditentukan dapat dijangkau. Hal ini menghemat waktu jika Anda hanya ingin menjalankan tes cepat untuk melihat apakah layanan web pada situs showcase Anda masih aktif.



**Pindai beberapa port melalui Nmap**



Dengan cara yang sama, kita dapat menentukan beberapa port ke Nmap, menggunakan opsi yang sama dan menggabungkan port yang ditentukan dengan koma:



```

# Scan several TCP ports with Nmap

nmap 192.168.1.19 -p 80,10999,22,23,1345

# Scan several UDP ports with Nmap

nmap -sU 192.168.1.19 -p 161,23,69

```



Terlepas dari urutannya, Nmap akan memeriksa semua port ini, dan hanya port yang ada pada host yang ditargetkan. Anda akan melihat pada keluaran Nmap bahwa ia **secara eksplisit memberi tahu kita semua port dan statusnya**, bahkan jika port tersebut "tertutup". Tidak seperti perilaku default, di mana keluaran lengkap ini akan memakan terlalu banyak ruang:



![nmap-image](assets/fr/24.webp)



*Hasil pemindaian TCP Nmap pada port yang ditunjukkan.*



**Memindai berbagai port



Jika jumlah port yang ingin Anda pindai terlalu banyak, Anda dapat menentukannya berdasarkan rentang, misalnya:



```

# Scan TCP ports from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 1000-2000

# Scan UDP ports from 1000 to 2000 with Nmap

nmap -sU 192.168.1.19 -p 100-150

```



Tentu saja, Anda bisa memadupadankan dan mencocokkan sesuai keinginan Anda, misalnya:



```

# Scan TCP ports 22,80, 3389 and from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 22,80,1000-2000,3389

```



**Pemindaian port TCP dan UDP



Anda juga dapat melakukan pemindaian UDP dan TCP secara bersamaan, pada port yang dipilih:



```

# Scan the list of 1000 default ports, in TCP and UDP

sudo nmap 192.168.1.19 -sT -sU

# Scan only UDP/161 and TCP/22

sudo nmap 192.168.1.19 -sT -sU -p U:161,T:22

```



Anda akan melihat pada contoh terakhir ini, adanya "U:" untuk mengindikasikan port UDP dan "T:" untuk mengindikasikan port TCP. Berikut ini adalah kemungkinan output dari jenis pemindaian ini:



![nmap-image](assets/fr/25.webp)



*Hasil pemindaian port TCP dan UDP dengan Nmap.*



Nah, itu cara yang menarik untuk menyesuaikan pemindaian Anda!



**Pindai semua port



Terakhir, Anda dapat menentukan rentang yang jauh lebih besar atau lebih kecil pada Nmap. Kita telah melihat bahwa daftar default yang dipilih oleh Nmap berisi 1000 port. Kita juga dapat meminta 100 port yang paling sering digunakan, atau 200 port yang paling sering digunakan, dengan menggunakan opsi "--top-ports":



```

# Scan the top 100 most common ports with Nmap

nmap 192.168.1.19 --top-ports 100

# Scan the top 200 most common ports with Nmap

nmap 192.168.1.19 --top-ports 200

```



Terakhir, kita bisa memintanya untuk memindai semua port yang memungkinkan (semua 65535), dengan menggunakan notasi "-p-":



```

# Scan all TCP ports from 1 to 65535 with Nmap

nmap 192.168.1.19 -p-

```



Yang terakhir ini akan memakan waktu lebih lama, terutama dengan UDP, tetapi Anda pasti tidak akan melewatkan port yang terbuka.



*Catatan: Opsi "-p-" adalah metode yang direkomendasikan untuk memindai semua port TCP. Untuk pemindaian UDP, disarankan untuk membatasi jumlah port demi alasan performa, karena pemindaian lengkap semua port UDP dapat memakan waktu yang sangat lama.*



Nanti dalam tutorial ini, kita akan melihat cara mengoptimalkan kecepatan pemindaian Nmap agar sesuai dengan kebutuhan kita, yang akan sangat berguna untuk pemindaian pada semua port TCP dan UDP.



### V. Kesimpulan



Pada bagian ini, kita akhirnya mendapatkan beberapa latihan langsung, jadi kita sekarang tahu **cara menggunakan Nmap dengan cara dasar untuk memindai port TCP dan UDP host**. Kita juga telah melihat secara detail apa yang terjadi pada tingkat jaringan dan **bagaimana Nmap menentukan apakah port TCP atau UDP aktif atau tidak**. Akhirnya, kita tahu bagaimana memilih port yang ingin kita pindai dengan baik dan **apa yang sebenarnya dilakukan oleh opsi default Nmap**. Selanjutnya, kita akan menggunakan kembali pengetahuan ini dan menerapkannya untuk memindai seluruh jaringan, termasuk pemetaan global dan penemuan jaringan.




## 5 - Pemetaan dan penemuan jaringan dengan Nmap



### I. Presentasi



Pada bagian ini, kita akan mempelajari cara menggunakan alat pemindaian jaringan Nmap untuk memetakan jaringan Anda. Kita akan melihat seberapa efektif alat ini dalam tugas ini, melalui berbagai pilihannya. Terakhir, kita akan melihat berbagai cara untuk menentukan target pemindaian kita ke Nmap.



Secara khusus, kita akan menggunakan apa yang telah kita pelajari di bagian sebelumnya tentang bagaimana Nmap menentukan apakah sebuah host aktif dan dapat dijangkau.



Seperti yang telah disebutkan dalam pengantar Nmap, ini adalah Network Mapper. Dengan demikian, ini adalah alat yang sempurna untuk membuat daftar host yang dapat diakses di jaringan, baik lokal maupun jarak jauh.



**Kembalinya penulis:**



Faktanya, sebagai auditor keamanan siber dan pentester, saya menggunakan Nmap secara sistematis ketika melakukan tes penetrasi internal untuk mengetahui di mana saya berada, siapa tetangga saya di jaringan lokal dan jaringan lain yang dapat diakses, serta sistem yang ada di dalamnya. Tujuan saya sederhana: memetakan jaringan, menentukan ukuran sistem informasi dan, khususnya, membuat sketsa permukaan serangannya.



Pemetaan jaringan juga dapat berguna dalam konteks diagnosa jaringan, pengawasan, pemetaan aset (apakah Anda benar-benar yakin bahwa IS Anda hanya terdiri dari apa yang ada di Active Directory atau di GLPI/OCS Inventory Anda? Hal ini juga dapat digunakan untuk mendeteksi keberadaan Shadow IT dalam sistem informasi Anda.



### II. Menggunakan Nmap untuk memindai rentang jaringan



#### A. Menemukan jaringan dengan pemindaian Nmap



Sekarang kita ingin meningkatkan kemampuan dan menganalisis seluruh jaringan lokal kita. Tidak ada yang lebih sederhana: yang perlu kita lakukan adalah menggunakan kembali perintah yang kita lihat di bagian sebelumnya, tetapi tentukan CIDR dan bukannya IP Address yang sederhana.



CIDR (**Classless Inter Domain Routing**) adalah notasi "klasik" untuk menentukan jangkauan jaringan dan luasnya (menggunakan mask). Sebagai contoh, "192.168.0.0/24" adalah "terjemahan" dari notasi mask desimal "255.255.255.0".



Untuk menggunakan Nmap dengan menentukan CIDR, kita dapat menggunakannya sebagai berikut:



```
# Scan a CIDR
nmap 192.168.0.0/24
```



Hal ini juga memungkinkan, seperti halnya dengan port pada bagian sebelumnya, untuk menentukan beberapa host, beberapa jaringan, atau jangkauan:



```
# Scan several networks at once via their CIDR
nmap 192.168.0.0/24 192.168.1.0/24

# Scan several hosts via their IP
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20

# Mix of both
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20
```



Berikut ini contoh hasil yang mungkin kita dapatkan ketika menjalankan pemindaian pada jaringan:



![nmap-image](assets/fr/26.webp)



hasil pemindaian Nmap untuk memetakan beberapa jaringan



Secara khusus, kita melihat beberapa host yang aktif, dan setiap bagian host dimulai dengan baris seperti ini:



```
Nmap scan report for <name> (<IP>)
```



Hal ini memungkinkan kita untuk melihat dengan jelas host mana yang dirujuk oleh hasil berikut ini. Baris terakhir juga penting:



```
Nmap done: 512 IP addresses (5 hosts up) scanned in 21.43 seconds
```



Kita tahu bahwa, pada jaringan yang dipindai, Nmap menemukan 5 host yang aktif.



#### B. Di balik tenda: analisis jaringan melalui Wireshark



Sekarang kita akan melihat lebih dekat apa yang terjadi pada tingkat jaringan selama penemuan jaringan yang dilakukan melalui Nmap.



Seperti yang kita lihat pada bagian sebelumnya, secara default Nmap akan menggunakan protokol ARP untuk mendeteksi keberadaan host pada jaringan lokal:



![nmap-image](assets/fr/27.webp)



paket aRP yang ditangkap saat memindai jaringan lokal menggunakan Nmap dan opsi defaultnya



Dengan demikian dapat mendeteksi hampir semua host di jaringan lokal, karena respons terhadap permintaan ARP umumnya diberikan oleh semua host yang aktif di jaringan dan tidak terlihat mencurigakan.



Untuk jaringan jarak jauh, Nmap menggunakan kombinasi teknik:



![nmap-image](assets/fr/28.webp)



paket iCMP dan TCP yang ditangkap saat memindai jaringan jarak jauh menggunakan Nmap dan opsi standarnya



Lebih tepatnya, Nmap menggunakan paket ICMP echo (kasus klasik ping) dan paket ICMP Timestamp, biasanya digunakan untuk menghitung waktu transit paket. Nmap berharap untuk mendapatkan respons dari host di jaringan jarak jauh.



Tetapi ada yang lebih dari itu. Anda dapat melihat pada tangkapan Wireshark di atas bahwa paket **TCP SYN** secara sistematis dikirim pada port TCP/443 dari setiap host potensial di jaringan yang akan dipindai, serta paket **TCP ACK** pada port TCP/80.



**Mengapa mengirim paket TCP ke port sebagai bagian dari penemuan jaringan?



Mengirim paket SYN ke port yang diberikan memungkinkan Nmap untuk **menentukan apakah sebuah layanan mendengarkan pada port tersebut**. Jika sebuah host membalas paket SYN dengan paket SYN/ACK, ini mengindikasikan bahwa host tersebut aktif dan sebuah layanan sedang mendengarkan pada port tersebut. Oleh karena itu, Nmap mencoba peruntungannya pada layanan ini, **meskipun tidak ada respons terhadap ping yang diperoleh**.



Mengirim paket ACK ke port yang diberikan memungkinkan Nmap untuk **menentukan apakah ada firewall pada host tersebut**. Jika sebuah host merespon paket ACK dengan paket RST (Reset), ini mengindikasikan bahwa firewall mungkin ada di host tersebut dan memblokir trafik yang tidak diminta. Dengan demikian, host tersebut mengkhianati keberadaannya di jaringan, bahkan jika host tersebut tidak menanggapi permintaan lain.



Namun, penting untuk dicatat bahwa deteksi firewall menggunakan teknik ini mungkin tidak dapat diandalkan secara sempurna di semua kasus. Beberapa host mungkin merespons generate RST karena alasan selain keberadaan firewall, seperti layanan tertentu atau konfigurasi sistem operasi. Selain itu, firewall modern dapat dikonfigurasi untuk tidak merespons upaya penemuan jenis ini.



Kita sekarang telah melangkah jauh dan dapat melakukan penemuan jaringan dasar. Sekarang kita akan melihat beberapa opsi lain yang akan memberi kita kontrol yang lebih besar atas perilaku Nmap.



### III. Penemuan jaringan tanpa pemindaian port dengan Nmap



Seperti yang mungkin telah Anda ketahui, secara default Nmap **melakukan pemindaian port setelah menemukan host yang aktif**, yang menambahkan sejumlah besar paket dan menunggu jawaban dari pemindaian kita. Jika Anda memiliki 5 host di jaringan Anda, Nmap akan mencoba memeriksa status sekitar 5.000 port, yang akan memakan waktu lebih lama.



Namun, dimungkinkan untuk menggunakan opsi Nmap untuk melakukan **hanya penemuan host yang aktif** pada jaringan, tanpa menemukan layanan mereka.



Jika kita hanya ingin mengetahui host mana yang dapat dijangkau, tanpa informasi apa pun tentang layanan dan port yang mereka buka, maka kita dapat menggunakan opsi "-sn" untuk melakukan **hanya pemindaian menggunakan ICMP Echo (ping) dan permintaan ARP**. Dengan kata lain, nonaktifkan pemindaian port sama sekali:



```
# Scan a CIDR in Echo ICMP
nmap 192.168.1.0/24 -sn
```



Berikut ini adalah hasil penemuan jaringan Nmap yang dilakukan tanpa pemindaian port:



![nmap-image](assets/fr/29.webp)



Hasil penemuan jaringan tanpa pemindaian port dengan Nmap.



Kami telah menyebutkan kemungkinan keterbatasan menggunakan ICMP saja untuk penemuan host (untuk jaringan jarak jauh). Itu sebabnya Nmap juga menggunakan beberapa trik yang dapat mengkhianati keberadaan firewall atau layanan tertentu pada host. Dengan bantuan opsi, kita dapat menggunakan kembali trik ini dan bahkan mengembangkannya, tanpa harus memulai lagi dengan pemindaian port lengkap pada setiap host yang ditemukan.



Untuk melakukan ini, kita akan menggunakan opsi "-PS" (TCP SYN) dan "-PA" (TCP ACK), yang akan memungkinkan kita untuk menentukan port yang ingin kita ikuti sebagai bagian dari penemuan host, dan juga opsi "-PP":



```
# Scan specific ports on a CIDR
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24
```



Pemindaian ini sudah memastikan bahwa penemuan host sedikit lebih lengkap dibandingkan dengan opsi default.



Kita mulai mendapatkan perintah yang cukup komprehensif, menggunakan beberapa opsi. Hal ini karena kita mengetahui cara kerja Nmap dan keterbatasan opsi "default"-nya, yang terkadang dapat membuat kita membuang-buang waktu atau melewatkan Elements yang penting. Itulah gunanya meluangkan waktu untuk menguasainya!



Untuk merinci opsi dari pesanan terakhir kami:





- "`-sn`: menonaktifkan pemindaian port untuk setiap host aktif yang ditemukan oleh Nmap.





- "`-PP`: mengaktifkan ICMP echo (ping scan) untuk penemuan host.





- "`-PS <PORT>`": mengirim paket TCP SYN pada port yang ditunjukkan untuk mendeteksi layanan aktif apa pun yang menunjukkan keberadaan host yang belum merespons ping.





- "`-PA <PORT>`": mengirim paket TCP ACK pada port yang ditunjukkan untuk mendeteksi firewall aktif yang menunjukkan adanya host yang tidak merespons ping.




Pada contoh di atas, saya menentukan port yang saya anggap paling sering diekspos dalam konteks Nmap saya untuk opsi "-PS". Port yang berbeda ini kemudian akan diuji pada setiap host, bukan untuk melihat apakah layanan yang mereka host benar-benar aktif, tetapi untuk melihat apakah ini memungkinkan kita untuk menemukan host yang belum merespons ICMP Echo kita saat masih aktif (melalui respons dari layanan atau firewall host).



Inilah yang dapat dilihat dalam tangkapan jaringan yang diambil pada saat pemindaian semacam itu, dalam hal ini ekstrak pada satu host target:



![nmap-image](assets/fr/30.webp)



paket yang dikirim oleh Nmap selama penemuan jaringan tingkat lanjut, tanpa pemindaian port



Kami menemukan paket TCP SYN kami, ACK TCP kami pada port TCP/80 dan gema ICMP kami. Nmap akan melakukan semua tes ini untuk setiap host yang ditargetkan oleh pemindaian penemuan jaringan kami.



### IV. Menggunakan file aset untuk ditargetkan dengan Nmap



Menentukan target dapat dengan cepat menjadi rumit dalam sistem informasi di kehidupan nyata, yang terkadang terdiri dari puluhan atau ratusan jaringan, subnet, dan VLAN. Inilah sebabnya mengapa lebih mudah menggunakan file sebagai sumber untuk Nmap daripada menentukannya satu per satu pada baris perintah.



Untuk memulainya, buatlah file sederhana yang berisi satu entri per baris:



![nmap-image](assets/fr/31.webp)



yang berisi satu target (host atau jaringan) per baris



Selanjutnya, kita dapat menggunakan semua opsi Nmap yang terlihat sejauh ini dan menentukan opsi "-iL <path/file>":



```
# Scan a list of targets contained in a file
nmap -iL /tmp/mesCibles.txt
```



Nmap kemudian akan menyertakan dalam pemindaiannya semua target yang ada di file kita.



Jika Anda ingin memastikan bahwa semua target Anda akan diperhitungkan, Anda dapat menggunakan opsi "-sL -n". Nmap kemudian hanya akan menginterpretasikan CIDR dan host di dalam berkas dan menampilkannya pada Anda, tanpa mengirimkan paket apa pun melalui jaringan:



```
# Display targets contained in a file
nmap -iL /tmp/mesCibles.txt -sL -n

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-01 14:52 CEST
Nmap scan report for 192.168.0.0
Nmap scan report for 192.168.0.1
Nmap scan report for 192.168.0.2
Nmap scan report for 192.168.0.3
Nmap scan report for 192.168.0.4
Nmap scan report for 192.168.0.5
Nmap scan report for 192.168.0.6
Nmap scan report for 192.168.0.7
Nmap scan report for 192.168.0.8
Nmap scan report for 192.168.0.9
Nmap scan report for 192.168.0.10
Nmap scan report for 192.168.0.11
Nmap scan report for 192.168.0.12
```



Hal ini memastikan bahwa daftar host yang akan dipindai akurat.



Satu tips penting terakhir yang ingin saya bagikan kepada Anda adalah tentang pengecualian host atau jaringan sebagai bagian dari pemindaian. Kebutuhan untuk mengecualikan host ini mungkin diperlukan dalam beberapa kasus, terutama jika kita ingin memastikan bahwa **komponen sensitif dari sistem informasi tidak terganggu atau terganggu oleh pemindaian kita**.



Contoh yang sering terjadi dari kebutuhan tersebut adalah ketika sebuah perusahaan memiliki peralatan industri (PLC) atau peralatan kesehatan. Peralatan semacam itu terkadang dirancang dengan buruk, dan sama sekali tidak dimaksudkan untuk menerima paket yang diformat dengan buruk, atau terlalu banyak. Untuk alasan yang jelas tentang ketersediaan atau risiko bisnis/manusia, lebih baik untuk mengecualikannya dari pengujian.



Untuk mengecualikan alamat IP atau jaringan dari pemindaian, kita dapat menggunakan opsi "--exclude" dari Nmap, misalnya:



```
# Exclude an IP address in a CIDR scan
nmap 192.168.1.0/24 --exclude 192.168.1.140
```



Dalam contoh ini, saya memindai jaringan "192.168.1.0/24" tetapi tidak termasuk host "192.168.1.140" yang terletak di sana. Tidak ada paket yang akan dikirim oleh Nmap ke host ini. Contoh lain dengan pengecualian subnet:



```
# Exclude a subnet in a CIDR scan
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```



Demikian pula, saya memindai jaringan besar "10.0.0.0/16", tetapi jaringan "10.0.100.0/24" tidak akan dipindai. Sekali lagi, saya sarankan untuk menggunakan opsi "-sL -n" untuk mendapatkan tampilan yang sangat jelas tentang host mana yang akan dipindai dan mana yang akan dikecualikan dari pemindaian, terutama jika Anda beroperasi dalam konteks yang sensitif.



### V. Penemuan jaringan dan pemindaian port



Sekarang kita dapat menggabungkan apa yang telah kita pelajari pada bagian ini dengan apa yang telah kita pelajari pada bagian sebelumnya tentang opsi pemindaian port. Secara default, kita telah melihat bahwa Nmap akan memindai 1000 port yang paling sering digunakan pada setiap host aktif yang ditemukannya. Kita telah melihat bagaimana mencegah perilaku ini jika kita tidak menginginkannya, tetapi kita dapat sepenuhnya mengendalikannya, dan bahkan mengembangkannya jika sesuai dengan kebutuhan kita.



Sebagai contoh, perintah berikut ini akan memeriksa keberadaan layanan mendengarkan pada port TCP/22 pada setiap host yang dipindai:



```
# Scan TCP/22 on a CIDR
nmap 192.168.0.0/24 192.168.1.0/24 -p 22
```



Nmap pertama-tama akan melakukan penemuan jaringan untuk membuat daftar host yang aktif, dan untuk setiap host, periksa apakah ada layanan pada port TCP/22.



Dengan cara yang sama, kita dapat melakukan pemindaian penuh semua port TCP pada setiap host yang ditemukan di jaringan "192.168.0.0/24", tidak termasuk host "192.168.0.4" misalnya:



```
# Port scan of a CIDR with exclusion
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```



Anda bebas menggabungkan semua opsi yang telah kita pelajari sejauh ini sesuai dengan kebutuhan Anda.



### VI. Kesimpulan



Pada bagian ini, kita telah melihat cara menggunakan Nmap untuk memetakan jaringan dengan menggunakan berbagai opsi. Kita sekarang memiliki pemahaman yang lebih baik tentang target pemindaian kita, serta perilaku pemindaian port Nmap dan metode penemuan host. Dan yang paling penting, kita tahu apa perilaku dan batasan default Nmap, dan bagaimana menggunakan opsi-opsi utamanya untuk melangkah lebih jauh.



Di bagian berikutnya, kita akan melihat mekanisme dan opsi untuk menemukan versi layanan dan sistem operasi yang dipindai oleh Nmap.




## 6 - Mendeteksi versi layanan dan sistem operasi dengan Nmap



### I. Presentasi



Pada bagian ini, kita akan mempelajari cara menggunakan Nmap untuk menemukan dan mendeteksi secara akurat versi layanan dan sistem operasi yang digunakan oleh host yang dipindai. Kita akan melihat secara mendetail bagaimana Nmap menyelesaikan tugas ini, dan juga keterbatasan alat ini untuk memahami dan menginterpretasikan hasilnya dengan lebih baik.



Seperti yang telah kita lihat pada bagian sebelumnya dari tutorial ini, secara default, Nmap tidak akan melihat layanan apa yang terbuka pada port yang dipindai dan dianggap terbuka. Jadi, jika Anda mendengarkan layanan web pada port TCP/22, Nmap akan terus melaporkannya sebagai terbuka, tetapi sebagai layanan `SSH`. Hal ini karena Nmap menggunakan [database](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) lokal pada sistem Anda untuk mencari hubungan antara port/protokol dan nama layanan (file `/etc/services/`).



Pada sebagian besar kasus, [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) akan memberikan Anda informasi yang benar, karena jarang sekali dalam lingkungan produksi menemukan kasus seperti itu. Namun, kasus yang tersisa adalah situasi di mana layanan klasik ([SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), HTTP, dll.) diekspos pada port non-klasik (mis. 2022 untuk layanan SSH), dalam hal ini Nmap tidak akan menemukan kecocokan dalam basis data lokalnya, atau yang tidak sesuai dengan kenyataan, dan Anda akan kehilangan informasi penting.



Untungnya, Nmap menawarkan opsi dan mekanisme yang sangat tepat untuk menemukan layanan mana yang mungkin bersembunyi di balik port yang terbuka. Ia bahkan memiliki basis data kueri dan tanda tangan untuk mengidentifikasi teknologi dan versi yang tepat. Selain layanan, Nmap juga bisa mengidentifikasi teknologi yang digunakan dan versinya.



Itulah yang akan kita cermati dalam bagian ini.



### II. Cara mendeteksi teknologi atau versi



#### A. Pengingat tentang cara mengidentifikasi teknologi atau versi



Mengidentifikasi teknologi dan versi melibatkan pengambilan nama layanan, CMS, aplikasi, atau perangkat lunak yang mendengarkan pada port yang ditargetkan. Sebagai contoh, sebuah halaman web dikelola oleh CMS (`WordPress`), dijalankan oleh layanan web (`Apache`, IIS, Nginx) dan di-host oleh server (Linux atau Windows). Namun, bagaimana Anda mengetahui layanan web mana yang sedang berjalan?



Metodologi klasik untuk mengetahui informasi ini adalah _banner grabbing_, yang secara sederhana terdiri dari menemukan di mana layanan yang bersangkutan menampilkan informasi ini dan membaca datanya. Sering kali, dalam konfigurasi atau pemrosesan default mereka, layanan menampilkan nama dan bahkan versi mereka sebagai respons pertama setelah koneksi.



![nmap-image](assets/fr/32.webp)



menampilkan versi segera setelah koneksi TCP dibuat oleh layanan FTP



Di sini kita melihat bahwa koneksi TCP sederhana ke layanan ini melalui `telnet` menghasilkan paket TCP yang berisi teknologi dan versinya.



Setelah Anda mengetahui jenis layanan yang Anda hadapi, Anda juga bisa mengirimkan perintah atau permintaan spesifik ke layanan tersebut untuk mengekstrak informasi darinya. Permintaan/perintah ini juga dapat dikirim secara membabi buta (tanpa memastikan jenis layanan yang tepat), dengan harapan salah satunya akan memancing respons dari layanan yang bersangkutan.



Dalam kasus lain yang lebih canggih, perlu mengirim paket tertentu untuk menimbulkan reaksi, seperti kesalahan, yang akan memberikan informasi rinci tentang versi atau teknologi yang digunakan.



Seperti yang bisa Anda bayangkan, Nmap akan menggunakan semua teknik ini untuk mencoba dan mengidentifikasi jenis layanan yang dihosting di sebuah port, serta nama teknologi dan versinya.



#### B. Memahami Probe dan Pencocokan Nmap



Untuk melakukan semua pemeriksaan ini pada setiap port yang dipindai, Nmap menggunakan basis data lokal yang sering diperbarui (seperti halnya biner atau modulnya). Ini adalah berkas teks yang terdiri dari beberapa ribu baris: `/usr/share/nmap/nmap-service-probes`.



File ini terdiri dari banyak entri, semuanya diatur berdasarkan dua panduan utama:





- The `Probe`: ini adalah definisi paket yang akan dikirim Nmap untuk memancing reaksi dari layanan yang akan diidentifikasi. Anggap saja ini sebagai upaya buta seperti _Hello? Guten Tag? Halo? Um... Buenos Dias mungkin?". Segera setelah layanan yang ditargetkan menerima probe yang dimengerti (yaitu berbicara dengan protokol yang benar), layanan tersebut akan merespons Nmap, yang kemudian akan mendapatkan konfirmasi tentang jenis layanan tersebut.





- Match": ini adalah ekspresi reguler yang diterapkan Nmap pada respons yang diperoleh. Jika mengirim permintaan HTTP GET telah memicu respons dari layanan, Nmap akan menerapkan lusinan ekspresi reguler pada respons ini untuk mengidentifikasi keberadaan, misalnya, kata `Apache`, `Nginx`, `Microsoft IIS`, dll.




Ada beberapa arahan lain untuk kasus-kasus tertentu, tetapi yang paling utama untuk memahami cara kerja Nmap dan menyesuaikan penggunaannya adalah ini. Untuk membuat bagian teori ini lebih konkret, berikut ini sebuah contoh:



![nmap-image](assets/fr/33.webp)



contoh Probe dalam file `/usr/share/nmap/nmap-service-probe` milik Nmap



Pada baris pertama contoh ini, kita melihat Probe yang mudah dipahami bernama `GetRequest`. Ini adalah paket TCP yang berisi permintaan HTTP GET kosong ke root layanan web menggunakan HTTP/1.0, diikuti dengan umpan baris dan baris kosong.



Baris `ports` memberi tahu Nmap ke port mana yang akan digunakan untuk mengirim Probe ini. Hal ini memungkinkan Anda untuk memprioritaskan tes dan menghemat waktu.



Terakhir, kita memiliki dua contoh `match`. Yang pertama, misalnya, akan mengkategorikan layanan web yang dipindai sebagai `ajp13` jika ekspresi reguler yang terkandung dalam baris ini cocok dengan respons layanan yang diterima.



Untuk membantu Anda memahami seperti apa bentuk Probe, berikut ini adalah daftar beberapa Probe yang dapat Anda temukan di dalam file ini (ada 188 Probe pada saat tutorial ini ditulis).



![nmap-image](assets/fr/34.webp)



contoh beberapa probe yang digunakan oleh Nmap dan ada di file `/usr/share/nmap/nmap-service-probes`._



Dua yang pertama (disebut `NULL` dan `GenericLines`) adalah yang paling menarik di sini, karena mereka hanya mengirim paket TCP kosong atau paket yang berisi jeda baris. Layanan server sering kali mengumumkan diri mereka sendiri segera setelah koneksi diterima, tanpa tindakan, perintah atau permintaan khusus dari klien.



Berikut ini adalah kasus _match_ yang sedikit lebih kompleks:



```
# Match Nginx + version in an error 400 page
match ssl/http m|^HTTP/1.1 400 Bad Request\r\n.*?Server: nginx/([\d.]+)[^\r\n]*?\r\n.*<title>400 The plain HTTP request was sent to HTTPS port</title>|s p/nginx/ v/$1/ cpe:/a:igor_sysoev:nginx:$1/
```



Ekspresi reguler yang tepat terdapat di sini di antara `m|` dan `|`, yang membatasi ekspresi reguler apa pun di dalam file ini. Mohon luangkan waktu untuk membaca seluruh contoh ini. Anda akan melihat sebuah pilihan di dalam ekspresi reguler: `([\d.]+)`, yang digunakan untuk mengisolasi sebuah versi. Contoh ini juga mendefinisikan Elements lain seperti nama produk `p/nginx/`, versi yang diambil `v/$1/`, dan CPE dengan versi `cpe:/a:igor_sysoev:nginx:$1/`.



CPE (Common Platform Enumeration) adalah sistem notasi standar yang digunakan untuk mengidentifikasi dan mendeskripsikan perangkat lunak dan perangkat keras. Format ini memungkinkan pengelolaan kerentanan dan konfigurasi keamanan yang lebih efisien, dan yang terpenting adalah cara terpadu untuk merepresentasikannya, apa pun produknya. Berikut adalah dua contoh CPE: `cpe:/o:microsoft:windows_8.1:r1` dan `cpe:/a:apache:http_server:2.4.35`



Di sini kami dengan jelas mengidentifikasi jenisnya `o` untuk OS, `a` untuk aplikasi, vendor, produk, dan versi.



Jadi, jika terjadi _match_ dengan salah satu ekspresi reguler ini, kita akan mengambil tidak hanya nama layanan, tetapi juga versi dan CPE yang tepat, sehingga lebih mudah untuk menemukan CVE yang berdampak pada versi ini. Anda akan menemukan informasi ini dalam keluaran standar Nmap, dan Anda akan melihat bahwa informasi ini sangat berguna untuk tujuan lain yang akan kita bahas dalam beberapa bagian.



Sintaks yang tepat dari _matches_ dan, secara umum, arahan dalam file `/usr/share/nmap/nmap-service-probe` tidak berhenti sampai di sini, dan mungkin tampak agak rumit jika Anda tidak terbiasa memanipulasi Nmap dan hasilnya. Namun, setidaknya Anda harus mengingat keberadaan dan operasi umumnya, yang akan berguna di kemudian hari ketika Anda ingin memahami atau men-debug hasil, menyesuaikan pemindaian, atau bahkan berkontribusi pada pengembangan Nmap.



### III. Menggunakan Nmap untuk mendeteksi versi



Sekarang kita akan menggunakan semua mekanisme _Probe_ dan _Match_ yang rumit ini melalui opsi sederhana: `-sV`. Ini hanya memberi tahu Nmap: coba cari tahu dengan tepat layanan dan versi port yang telah Anda tetapkan sebagai terbuka.



```
# Enable service and version detection
nmap 192.168.1.0/24 -sV
```



Berikut ini contoh lengkap hasil dari perintah tersebut:



![nmap-image](assets/fr/35.webp)



hasil deteksi versi Nmap terhadap aplikasi yang terekspos di jaringan



Di sini kita dapat melihat bahwa Nmap telah berhasil mengidentifikasi semua versi layanan jaringan yang diekspos oleh target ini, dan menampilkan informasi ini di kolom `VERSION` yang baru. Kita bisa melihat informasi yang cukup akurat, bahkan sampai ke sistem operasi, jika informasi ini merupakan bagian dari tanda tangan yang dipulihkan.



Untuk memahami secara detail apa yang terjadi selama pemindaian kerentanan, kita dapat menggunakan opsi `--version-trace`. Ini akan memberikan tampilan mode debug, yang menampilkan _Probe_ yang menyebabkan deteksi:



```
# Enable version detection debug
nmap 192.168.1.0/24 -sV --version-trace
```



Sebagai hasilnya, kita akan memiliki banyak informasi untuk dipilah-pilah. Cobalah untuk mengidentifikasi baris yang dimulai dengan `Service scan Hard match`. Anda akan melihat baris seperti ini:



```
Service scan hard match (Probe NULL matched with NULL line 789): 10.10.10.187:21 is ftp. Version: |vsftpd|3.0.3||
Service scan hard match (Probe NULL matched with NULL line 3525): 10.10.10.187:22 is ssh. Version: |OpenSSH|7.4p1 Debian 10+deb9u7|protocol 2.0|
Service scan hard match (Probe GetRequest matched with GetRequest line 10510): 10.10.10.187:80 is http. Version: |Apache httpd|2.4.25|(Debian)|
```



Kita dapat dengan jelas melihat _Probes_ mana yang digunakan untuk mendeteksi teknologi dan versi (dalam hal ini _Probes_ `NULL` dan `GetRequest`), serta informasi yang diambil.



### IV. Menguasai tes dan akurasi deteksi



Sekarang kita akan kembali ke arahan dalam berkas `/usr/share/nmap/nmap-service-probe` yang tidak kita lihat sebelumnya:



![nmap-image](assets/fr/36.webp)



probe `rarity` direktif dalam file `/usr/share/nmap/nmap-service-probes`._



Arahan ini digunakan untuk menunjukkan kelangkaan (yaitu prioritas/probabilitas) yang terkait dengan _Probe_. Notasi dari 1 hingga 9 ini memungkinkan Anda untuk mengontrol kelengkapan analisis yang dilakukan oleh Nmap ketika mengirim _Probe_. Dalam sistem "notasi" Nmap, kelangkaan 1 memberikan informasi dalam sebagian besar kasus, sedangkan kelangkaan 8 atau 9 mewakili kasus yang sangat khusus, khusus untuk konfigurasi atau layanan yang jarang ada.



Untuk lebih jelasnya, dalam kasus default, Nmap akan mengirimkan ke setiap layanan untuk diidentifikasi _Probes_ yang memiliki kelangkaan dari 1 hingga 7. Untuk memberi Anda gambaran yang lebih baik tentang distribusi _Probes_ berdasarkan _kelangkaan_, berikut ini hitungannya:



```
$ grep -E "^rarity" nmap-service-probes |sort |uniq -c

6 rarity 1
1 rarity 2
3 rarity 3
8 rarity 4
9 rarity 5
13 rarity 6
8 rarity 7
81 rarity 8
54 rarity 9
```



Ini mungkin terlihat berlawanan dengan intuisi, ada lebih banyak `rarity` 8 dan 9 daripada yang lainnya. Hal ini disebabkan karena Probe kelangkaan 1 bersifat umum dan bekerja pada sebagian besar kasus, terlepas dari layanannya (ingat Probe `NULL` yang hanya mengirim paket TCP kosong). Sedangkan Probe yang lebih kompleks hampir unik untuk setiap layanan.



Jika kita ingin mengelola secara manual Probe yang ingin kita gunakan dalam pemindaian versi, kita dapat menggunakan opsi `--versi-intensitas`. Berikut adalah dua contoh:



```
# Less accurate version detection than default
nmap 192.168.1.0/24 -sV --version-intensity 2

# Very deep detection, using all existing Probes
nmap 192.168.1.0/24 -sV --version-intensity 9
```



Untuk mengakhiri bahasan ini, berikut adalah contoh _Probe_ 9 dan 8:



![nmap-image](assets/fr/37.webp)



contoh Probe pada rarity 8 dan 9 dalam file `/usr/share/nmap/nmap-service-probe`._



Kedua _Probes_ ini mendeteksi server Quake1 dan Quake2 (video game). Menarik untuk sisi nostalgia, tetapi tidak akan banyak berguna dalam kehidupan sehari-hari.



Tergantung pada kebutuhan Anda akan presisi atau kecepatan, ingatlah bahwa prinsip `kelangkaan` ini ada dan dapat memengaruhi hasilnya.



### V. Menggunakan Nmap untuk mendeteksi sistem operasi



Sekarang kita akan melihat bagaimana Nmap dapat membantu kita mendeteksi sistem operasi host yang dipindai dan terdeteksi pada jaringan. Untuk melakukan hal ini, gunakan opsi `-O` (untuk `OS Scan`) dari Nmap.



```
# Enable OS Scan
nmap -O 10.10.10.0/24
```



Berikut adalah contoh hasilnya. Di sini, Nmap memberi tahu kita bahwa itu mungkin OS Linux, dan menawarkan berbagai statistik mengenai versinya yang tepat.



![nmap-image](assets/fr/38.webp)



deteksi probabilitas identifikasi sistem operasi oleh Nmap



Untuk mencapai hal ini, Nmap akan menggunakan banyak teknik yang bekerja dengan cara yang sangat mirip dengan _Probes_ dan _Matches_ untuk deteksi teknologi dan versi. Perbedaan utamanya adalah bahwa Nmap akan menggunakan parameter yang cukup "tingkat rendah" dari ICMP, TCP, UDP, dan protokol lainnya. Berikut adalah dua contoh pengujian untuk mendeteksi sistem operasi Microsoft Windows 11:



![nmap-image](assets/fr/39.webp)



contoh tes yang dilakukan oleh Nmap untuk mendeteksi OS Windows 11



Mari kita hadapi itu, tes ini sangat sulit untuk ditafsirkan, dan kita tidak akan mencoba untuk memahaminya secara mendalam dalam konteks tutorial pengantar Nmap. Jika Anda ingin menggali lebih dalam ke dalam subjek ini, file yang berisi informasi ini adalah `/usr/share/nmap/nmap-os-db`.



Namun, Anda perlu menyadari bahwa deteksi OS lebih merupakan probabilitas yang ditetapkan oleh Nmap daripada kepastian.



### VI. Kesimpulan



Pada bagian ini, kita telah mempelajari cara menggunakan opsi-opsi Nmap untuk mendeteksi teknologi, versi, dan sistem operasi dari host dan layanan yang dipindai. Kita sekarang memiliki pemahaman yang baik tentang cara Nmap mendapatkan informasi ini dari jarak jauh. Kita juga telah meninjau opsi-opsi untuk mengelola verbositas dan akurasi pengujian, serta keterbatasan alat ini dalam hal ini.



Pada bagian selanjutnya, kita akan mempelajari cara menggunakan skrip NSE Nmap untuk melakukan analisis keamanan pada sistem informasi kita. Luangkan waktu untuk membaca ulang bagian terakhir jika perlu, dan jangan ragu untuk berlatih dan mempelajari inti dari alat ini sendiri untuk lebih menguasai apa yang telah kita pelajari sejauh ini.




## 7 - Analisis keamanan: mendeteksi kerentanan



### I. Presentasi



Pada bagian ini, kita akan mempelajari cara menggunakan alat pemindaian jaringan Nmap untuk mendeteksi dan menganalisis kerentanan pada target pemindaian kita. Secara khusus, kita akan melihat berbagai opsi yang tersedia untuk menyelesaikan tugas ini, dan mempelajari batas kemampuan alat ini untuk memahami dan menginterpretasikan hasilnya dengan lebih baik.



Pada bagian pertama ini, kita akan melihat pemindai kerentanan Nmap, dan melihat cara menggunakan opsi pendeteksian kerentanan dasar. Di bagian berikutnya, kita akan melihat lebih dekat cara kerja fitur ini, dan bagaimana fitur ini dapat dikustomisasi.



### II. Menggunakan Nmap untuk mendeteksi kerentanan



Sekarang kita ingin menggunakan pemindai jaringan Nmap untuk mendeteksi kerentanan pada layanan dan sistem sistem informasi kita. Ini berarti bahwa selain menemukan host yang aktif, menghitung layanan yang terbuka, dan mendeteksi versi dan teknologi, Nmap akan mencari kerentanan.



Untuk mencapai hal ini, Nmap bergantung pada skrip NSE (_Nmap Scripting Engine_), yang dapat dilihat sebagai modul yang memungkinkan pendekatan granular untuk pengujian.



Dengan opsi yang tepat, kita akan meminta Nmap untuk menggunakan berbagai skrip NSE pada setiap layanan yang ditemukan, sehingga kita dapat menemukan layanan:





- Kesalahan konfigurasi ;





- Penemuan versi dan OS tambahan dan yang lebih canggih ;





- Kerentanan yang diketahui (CVE) ;





- Pengidentifikasi yang lemah ;





- Karakteristik Elements dari infeksi malware ;





- Penolakan kemungkinan layanan ;





- Dll.




Seperti yang Anda lihat, skrip NSE secara signifikan memperluas kemampuan Nmap dalam hal operasi jaringan yang dapat dilakukannya. Dan ini untuk melakukan tugas-tugas yang jauh lebih canggih daripada sebelumnya. Kabar baiknya adalah, seperti biasa, fitur-fitur ini dapat digunakan secara sederhana melalui opsi dan dalam konteks default. Inilah yang akan kita lihat selanjutnya.



### III. Contoh pemindaian kerentanan



Skrip NSE dapat digunakan ketika menggunakan Nmap untuk memindai satu port pada sebuah host, semua layanan pada host tersebut, atau semua layanan yang terdeteksi pada beberapa jaringan. Oleh karena itu, kita dapat menggunakan opsi yang akan kita lihat di semua konteks yang telah kita pelajari sejauh ini.



Untuk mengaktifkan pemindaian kerentanan melalui pemindaian Nmap, kita perlu menggunakan opsi `-sC`:



```
# Enable vulnerability scanning during a scan
nmap -sC 10.10.10.152
```



Ingatlah bahwa secara default, jika Anda tidak menentukan apa pun, Nmap hanya akan memindai 1000 port yang paling umum. Dia tidak akan mendeteksi kerentanan pada port yang lebih eksotis yang mungkin diekspos oleh target Anda.



Sebelum menggunakan fungsionalitas ini pada sistem informasi produksi, saya mengajak Anda untuk melanjutkan membaca tutorial ini. Pada bagian berikut, kita akan melihat bagaimana cara mengontrol dampak dan jenis tes yang akan dijalankan dengan lebih baik.



Dengan menggunakan kembali apa yang telah kita pelajari sebelumnya, kita bisa, misalnya, lebih komprehensif dan memindai semua port TCP dari sebuah target:



```
# Enable vulnerability scanning on all ports
nmap -sC -p- 10.10.10.152
```



Berikut adalah hasil pemindaian Nmap menggunakan skrip NSE:



![nmap-image](assets/fr/40.webp)



contoh hasil pemindaian kerentanan pada sebuah host melalui Nmap._



Di sini kita melihat tampilan informasi tambahan yang menarik dalam konteks analisis kerentanan:





- Layanan FTP dapat diakses secara anonim, dan tidak dilindungi oleh autentikasi. Skrip NSE yang bertanggung jawab atas verifikasi ini memberitahukan kepada kita, dan bahkan menampilkan bagian dari struktur pohon layanan FTP. Di sini kita melihat bahwa kita memiliki akses ke direktori `C` pada sistem Windows!





- Skrip NSE yang bertanggung jawab atas pengambilan layanan web tingkat lanjut menampilkan judul halaman, memberi kita gambaran yang lebih baik tentang apa yang dihosting oleh layanan web tersebut.





- Kami juga memiliki analisis mini dari konfigurasi layanan SMB (skrip `smb2-time`, `smb-security-mode` dan `smb2-security-mode`). Informasi ini ditampilkan sedikit berbeda, setelah hasil pemindaian jaringan, agar lebih mudah dibaca. Secara khusus, informasi ini menunjukkan tidak adanya tanda tangan SMB Exchange. Kelemahan konfigurasi ini memungkinkan target untuk digunakan dalam serangan SMB Relay, sebuah kelemahan keamanan yang sering dieksploitasi dalam pengujian intrusi/serangan cyber.




Tentu saja, ini hanyalah satu contoh. Nmap memiliki skrip NSE untuk banyak layanan, yang menargetkan berbagai macam kerentanan. Kita akan melihat lebih dekat pada kemungkinan-kemungkinan ini di bagian selanjutnya.



Untuk mengakhiri pengantar pemindaian kerentanan ini, berikut adalah perintah lengkap untuk penemuan jaringan, pemindaian port TCP, versi, dan deteksi kerentanan:



```
# Complete and realistic vulnerability scan command
nmap -sV -sC -p- 192.168.0.0/24 192.168.1.13 192.168.2.10-20 --exclude 192.168.0.4
```



Berikut ini adalah perintah yang mulai terlihat seperti kasus penggunaan Nmap yang lebih realistis!



### IV. Memahami keterbatasan Nmap dalam pemindaian kerentanan



Mari kita perjelas: Nmap tidak mampu melakukan uji penetrasi lengkap pada sistem informasi Anda, atau mensimulasikan operasi Tim Merah. Nmap memiliki beberapa keterbatasan yang perlu Anda ketahui jika Anda tidak ingin memiliki rasa aman yang palsu:





- Cakupan terbatas**: meskipun skrip NSE Nmap sangat kuat, cakupan pengujiannya mungkin terbatas dibandingkan dengan alat penemuan kerentanan khusus lainnya. Beberapa kerentanan mungkin tidak tercakup oleh skrip NSE yang tersedia, seperti kerentanan Active Directory, pemaparan data sensitif, atau kasus-kasus yang lebih lanjut dari aplikasi web yang rentan.





- Kompleksitas kerentanan**: beberapa jenis kerentanan tertentu mungkin sulit dideteksi menggunakan skrip NSE karena kompleksitasnya. Misalnya, kerentanan yang membutuhkan interaksi kompleks dengan layanan jarak jauh mungkin tidak terdeteksi secara efektif oleh Nmap (seperti dalam kasus izin yang berlebihan dalam berbagi file atau cacat kontrol izin dalam aplikasi web).





- Deteksi pasif**: Nmap berfokus pada pemindaian aktif untuk mendeteksi kerentanan, yang berarti Nmap tidak dapat secara efektif mendeteksi potensi kerentanan tanpa membangun koneksi aktif dengan host target. Kerentanan yang tidak menampakkan diri selama pemindaian aktif dapat terlewatkan (seperti dalam kasus injeksi kode pada aplikasi web).





- Ketergantungan pada pembaruan**: Basis data [database] Nmap (https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) dari skrip NSE terus berkembang, tetapi mungkin ada penundaan antara penemuan kerentanan baru dan penambahan skrip yang sesuai ke Nmap. Akibatnya, Nmap mungkin tidak selalu terbarui dengan kerentanan terbaru.





- Positif palsu dan negatif palsu**: seperti halnya alat keamanan lainnya, skrip NSE Nmap dapat menghasilkan positif palsu (peringatan kerentanan palsu) atau negatif palsu (kerentanan yang sebenarnya tidak terdeteksi). Ini adalah sesuatu yang perlu diingat ketika menganalisis hasil Nmap.




Jadi, sangat penting untuk memahami apa yang dilakukan dan tidak dilakukan oleh Nmap, dan juga untuk mengetahui bagaimana menginterpretasikan hasilnya. Secara khusus, kita telah melihat di sepanjang tutorial ini bahwa opsi default dapat membuat kita melewatkan Elements yang penting yang dapat ditemukan dengan penggunaan yang cermat.



Baik Anda seorang administrator sistem jaringan, insinyur keamanan, atau bahkan CISO, menggunakan Nmap memberikan gambaran umum tentang status keamanan sistem informasi. Ini adalah langkah pertama yang penting dalam mengamankan sistem, yang dapat dilakukan secara teratur oleh tim TI. Namun, hal ini tidak dapat menggantikan intervensi dan saran dari para ahli keamanan siber (https://www.it-connect.fr/cours-tutoriels/securite-informatique/), yang dapat mengungkap kelemahan yang jauh lebih komprehensif daripada Nmap.



### V. Kesimpulan



Pada bagian pertama Modul 3 ini, kita telah memperkenalkan pemindaian kerentanan melalui Nmap. Kita sekarang tahu cara menggunakan opsi utama untuk melakukan tugas ini, tetapi kita juga tahu batasan-batasannya. Pada bagian selanjutnya, kita akan melihat lebih dekat pada fungsionalitas ini, menggunakan skrip NSE untuk memperluas kekuatan Nmap sepuluh kali lipat.



## 8 - Menggunakan skrip NSE Nmap



### I. Presentasi



Pada bagian ini, kita akan melihat lebih dalam pada skrip NSE (_Nmap Scripting Engine_). Secara khusus, kita akan melihat mengapa skrip tersebut merupakan salah satu kekuatan besar dari alat ini, bagaimana cara kerjanya, dan bagaimana cara menelusuri dan menggunakan banyak skrip yang ada.



Bagian ini merupakan kelanjutan dari tutorial sebelumnya, di mana kita telah mempelajari cara menggunakan fitur pemindaian kerentanan Nmap secara dasar. Sekarang kita akan melihat lebih dekat bagaimana cara kerja [Nmap] (https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) dalam hal ini, sehingga kita dapat melakukan pemindaian yang lebih tepat dan terkontrol.



### II. Konsep skrip Nmap NSE



Skrip NSE Nmap memungkinkan Anda untuk memperluas kemampuannya dengan cara yang sangat fleksibel. Skrip ini ditulis dalam LUA, sebuah bahasa skrip yang lebih mudah ditangani dan diakses daripada C atau C# yang digunakan oleh Nmap. Keuntungan menggunakan skrip LUA dengan Nmap daripada alat yang berdiri sendiri adalah bahwa kita dapat memanfaatkan kecepatan eksekusi dan fitur standar Nmap (penemuan host, port, dan versi, dll.).



Naskah-naskah ini disusun berdasarkan kategori, dan satu naskah dapat menjadi bagian dari lebih dari satu kategori:



| Catégorie       | Description |
|----------------|-------------|
| **auth**       | Contient les scripts relatifs à l’authentification sur des services, dont l’accès anonyme ou l’énumération des utilisateurs. Exemples: `oracle-enum-users`, `ftp-anon`. |
| **broadcast**  | Contient les scripts relatifs aux opérations de broadcast sur le réseau, notamment en vue d’exploiter et de découvrir certains services, hôtes ou protocoles reposant sur le broadcast (IPv6, wake on lan, IGMP, etc.). Exemples: `broadcast-dhcp6-discover`, `broadcast-ospf2-discover`. |
| **brute**      | Contient les scripts relatifs aux opérations de brute force de l’authentification sur les services (brute force [SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), MSSQL, etc.). Exemples: `ssh-brute`, `vnc-brute`. |
| **default**    | Contient les scripts utilisés dans le cas par défaut (utilisation de `-sC`). Plusieurs critères sont utilisés afin de valider l’entrée d’un script dans cette catégorie dont la vitesse d’exécution, la structure de la sortie, la fiabilité du test, le caractère “intrusif” ou “risqué”, etc. |
| **discovery**  | Contient les scripts relatifs à la découverte avancée du réseau et des services. On y retrouve par exemple l’énumération du contenu d’un partage SMB, d’une version d’un service VNC, des requêtes SNMP, etc. Exemples: `mysql-info`, `http-security-headers`. |
| **dos**        | Contient les scripts pouvant causer un déni de service. Il peut s’agir de scripts créés pour exploiter une vulnérabilité de type déni de service ou alors de scripts ayant pour effet de bord un déni de service. Prudence donc (ils sont exclus de la catégorie `default`). Exemples: `http-slowloris`, `ipv6-ra-flood`. |
| **exploit**    | Contient les scripts créés pour exploiter de manière directe une vulnérabilité. Exemples: `http-shellsock`, `smb-vuln-ms08-067`. |
| **external**   | Contient les scripts qui nécessitent l’utilisation d’une ressource tierce, comme une base d’information en ligne. Cela indique notamment une tentative de connexion vers l’extérieur (attention à la confidentialité). Exemples: `whois-ip`, `dns-blacklist`, `ip-geolocation-geoplugin`. |
| **fuzzer**     | Contient les scripts conçus pour envoyer des trames, paquets ou paramètres inattendus par un service. Cela permet notamment de causer des erreurs ou dysfonctionnements afin d’obtenir des pistes de vulnérabilité ou des informations techniques. Exemples: `dns-fuzz`, `http-form-fuzzer`. |
| **intrusive**  | Contient les scripts qui sont catégorisés comme “risqués” d’un point de vue disponibilité, ou détection. Ils peuvent provoquer un crash du système ou être détectés comme malveillant par une solution de sécurité. Il s’agit de la catégorie inverse de `safe`. Exemples: `smtp-brute`, `smb-vuln-ms08-067`, `smb-psexec`. |
| **malware**    | Contient les scripts conçus pour détecter la présence d’élément caractéristique d’un malware, tel qu’un port en écoute communément utilisé par une backdoor connue. Exemples: `ftp-proftpd-backdoor`, `smtp-strangeport`. |
| **safe**       | Contient les scripts qui sont considérés comme sûrs d’un point de vue détection ou stabilité. Il s’agit de la catégorie inverse de `intrusive` et elle contient en grande majorité des scripts avancés d’identification de version ou de relevé d’élément de configuration. Exemples: `html-title`, `smb2-security-mode`, `ms-sql-info`. |
| **version**    | Contient les scripts qui permettent une détection avancée de version. Ils peuvent être utilisés en complément des Probes et Matchs étudiés précédemment quand la détection d’une version nécessite des opérations un peu plus complexes. Exemples: `http-php-version`, `vmware-version`. |
| **vuln**       | Contient les scripts conçus pour détecter la présence de vulnérabilité connue (CVE) sans pour autant les exploiter (à l’inverse de la catégorie `exploit`). Ils se contentent en général de rapporter le statut “vulnérable” ou non d’un service. Exemples: `smb-vuln-ms17-010` (eternal blue), `http-phpmyadmin-dir-traversal`. |


Secara teknis, kategori yang dimiliki skrip ditunjukkan secara langsung dalam kodenya.



![nmap-image](assets/fr/41.webp)



kategori skrip nSE `ftp-anon`._



Contoh ini menunjukkan bagian dari kode skrip NSE `ftp-anon.nse`, yang eksekusinya telah kita lihat pada bagian sebelumnya.



### III. Daftar skrip NSE yang ada



Secara default, skrip NSE Nmap berada di direktori `/usr/share/nmap/scripts/`, tanpa struktur pohon atau hirarki tertentu. Berikut ini adalah gambaran umum isi direktori ini:



![nmap-image](assets/fr/42.webp)



mengekstrak isi direktori `/usr/share/nmap/scripts/` yang berisi skrip NSE._



Direktori ini berisi lebih dari 5.000 skrip NSE. Pada umumnya, bagian pertama dari nama skrip berisi protokol atau kategori yang menjadi bagian dari skrip tersebut. Hal ini memungkinkan kita untuk mengurutkan daftar, misalnya, jika kita ingin membuat daftar semua skrip yang menargetkan layanan FTP:



![nmap-image](assets/fr/43.webp)



daftar skrip NSE Nmap dengan nama yang dimulai dengan `ftp-`._



Nmap tidak menawarkan pilihan untuk menelusuri dan membuat daftar skrip NSE; Anda dapat menggunakan perintah `--script-help` diikuti dengan nama kategori atau kata:



```
# List all scripts whose name starts with "ftp-"
nmap --script-help=ftp-*

# List all scripts from the "discovery" category
nmap --script-help=discovery
```



Namun, keluarannya adalah nama setiap skrip dan deskripsinya, yang tidak optimal jika pencarian memunculkan beberapa lusin skrip:



![nmap-image](assets/fr/44.webp)



hasil dari penggunaan perintah `--script-help` dari Nmap



Menurut pendapat saya, metode yang paling efektif adalah dengan menggunakan perintah klasik Linux di direktori `/usr/share/nmap/scripts/`:



```
# List scripts targeting the "ssh" service
ls -al /usr/share/nmap/scripts/ssh*

# List scripts from the "dos" category
grep -rl '"dos"' /usr/share/nmap/scripts/
```



Jangan ragu untuk menelusuri kode modul yang sesuai dengan Anda, untuk lebih memahami cara kerja skrip NSE.



### IV. Menggunakan skrip NSE dari Nmap



Sekarang kita akan mempelajari cara melakukan pemindaian kerentanan dengan memilih skrip NSE yang kita minati dengan cermat.



#### A. Memilih skrip berdasarkan kategori



Untuk memulainya, kita dapat memilih untuk mengeksekusi semua skrip yang termasuk dalam kategori tertentu. Kita perlu menunjukkan kategori ini atau kategori-kategori ini pada Nmap dengan argumen `--script <kategori>`:



```
# Use default NSE scripts
nmap --script default 10.10.10.152
```



Perintah pertama ini setara dengan perintah `nmap -sC`. Secara default, Nmap akan memilih skrip dalam kategori `default`, tetapi itu hanya untuk kepentingan argumen. Perintah berikutnya, misalnya, akan menggunakan semua skrip dalam kategori `discovery`:



```
# Use NSE scripts from the "discovery" category
nmap --script discovery 10.10.10.152
```



Seperti yang telah kita lihat, beberapa kategori memungkinkan kita untuk dengan cepat mengidentifikasi apa yang dilakukan oleh skrip NSE terkait (`discovery`, `vuln`, `exploit`), sementara kategori lainnya menentukan tingkat risiko, deteksi, atau stabilitas pengujian yang dilakukan. Jika kita berada dalam konteks yang sensitif dan tidak memiliki pemahaman yang baik tentang berbagai tindakan yang dilakukan oleh pilihan skrip kita, kita dapat memilih untuk menggabungkan pilihan untuk memilih hanya skrip yang ada dalam kategori `discovery` dan `safe`:



```
# Use scripts from multiple categories
nmap --script "discovery and safe" 10.10.10.152
```



Jika Anda benar-benar dan secara eksplisit ingin mengecualikan skrip dari kategori `dos` dan `intrusif`, Anda dapat menggunakan notasi berikut:



```
# Exclude categories
nmap --script "not intrusive and not dos" 10.10.10.152
```



Harap diperhatikan bahwa menentukan kondisi pengecualian seperti di atas akan mengakibatkan penggunaan semua kategori lain yang tidak secara eksplisit dikecualikan. Agar lebih adil, kita dapat menentukan, misalnya:



```
# Include scripts from the "vuln" category except those that are too risky
nmap --script "vuln and not intrusive and not dos" 10.10.10.152

# Same thing, but only targeting the HTTP protocol
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152
```



Berikut ini beberapa contoh cara menangani skrip NSE berdasarkan kategori, terutama ketika menggunakan Nmap untuk analisis kerentanan dalam konteks kehidupan nyata.



#### B. Memilih skrip sebagai satu unit



Kita juga dapat memilih untuk melakukan satu tes spesifik selama analisis, tes yang sesuai dengan skrip NSE. Untuk melakukan ini, kita perlu menentukan nama skrip dalam parameter `-script <name>`. Mengambil contoh skrip `ftp-anon.nse`:



```
# Use an NSE script and a specific port
nmap --script ftp-anon -p 21 10.10.10.152
```



Kami kemudian mendapatkan hasil yang sangat tepat:



![nmap-image](assets/fr/45.webp)



hasil penggunaan skrip NSE `ftp-anon` pada port FTP melalui Nmap._



Kita melihat hasil menjalankan skrip `ftp-anon` pada port 21, dan tidak ada port lain, karena kita menentukan opsi `-p 21`. Kita juga dapat melakukan pemindaian port dasar, mengeksekusi skrip NSE `ftp-anon` hanya pada layanan FTP yang ditemukan:



```
# Use a specific NSE script
nmap --script ftp-anon 10.10.10.152
```



Dengan demikian, Nmap juga akan menjalankan tes koneksi anonim ini jika menemukan layanan FTP pada port lain.



Untuk penjelasan singkat tentang apa yang dilakukan skrip NSE, Anda dapat menggunakan opsi `--script-help` yang disebutkan di atas:



![nmap-image](assets/fr/46.webp)



bantuan menampilkan hasil untuk skrip NSE `sshv1`._



Singkatnya, sekali lagi kita bisa menggunakan kembali semua opsi penemuan jaringan, layanan, versi, dan teknologi yang telah kita gunakan sampai sekarang!



#### C. Mengelola argumen skrip



Dalam menggunakan Nmap, Anda akan menemukan skrip NSE tertentu yang membutuhkan argumen masukan agar dapat berfungsi dengan benar. Sekarang kita akan melihat bagaimana memberikan argumen ke skrip ini melalui opsi Nmap.



Sebagai contoh, mari kita ambil skrip `ssh-brute`, yang memungkinkan Anda untuk melakukan serangan brute force pada layanan SSH.



Serangan brute force klasik terdiri dari pengujian beberapa kata sandi (kadang-kadang jutaan) dalam upaya untuk mengautentikasi ke akun tertentu. Dengan mencoba begitu banyak kata sandi, penyerang bertaruh pada probabilitas bahwa pengguna telah menggunakan kata sandi yang lemah dalam kamus kata sandi yang digunakan untuk menyerang.



Skrip ini memiliki opsi "default", yang dapat kita sesuaikan agar sesuai dengan konteks kita. Dalam konteks serangan ini, misalnya, kita dapat memberikan daftar pengguna dan kamus kata sandi yang akan digunakan kepada Nmap. Sejauh yang saya tahu, tidak mungkin untuk dengan mudah membuat daftar argumen yang diperlukan untuk sebuah skrip, jadi cara yang paling dapat diandalkan adalah dengan mengunjungi situs web resmi Nmap. Tautan langsung ke dokumentasi untuk skrip NSE dapat diperoleh dengan menggunakan opsi `--script-help`:



![nmap-image](assets/fr/47.webp)



hasil menampilkan bantuan untuk skrip NSE `ssh-brute` dengan tautan ke nmap.org._



Dengan mengklik tautan yang ditunjukkan, kita tiba di halaman web situs ini [https://nmap.org](https://nmap.org/):



![nmap-image](assets/fr/48.webp)



daftar argumen yang dapat diteruskan ke skrip NSE `ssh-brute` Nmap



Di sini kita memiliki pandangan yang jelas tentang argumen yang dapat digunakan, yang utama dalam konteks kita adalah `passdb` (berkas yang berisi daftar kata sandi) dan `userdb` (berkas yang berisi daftar pengguna). Dokumentasi di sini mengacu pada pustaka Nmap internal, karena mekanisme brute force dan opsi terkait telah disatukan untuk digunakan secara seragam di beberapa skrip (`ssh-brute`, `mysql-brute`, `mssql-brute`, dan lain-lain) dan oleh karena itu memiliki argumen yang kurang lebih sama:



```
# Create a file containing my user list
echo "root" > /tmp/userlist

# Create a file containing my password list
echo "123456" > /tmp/passlist
echo "NomEntreprise75" >> /tmp/passlist
echo "changezmoi" >> /tmp/passlist

# Run an SSH brute force via Nmap network scan
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```



Seperti yang Anda lihat pada perintah terakhir ini, kita dapat menentukan argumen yang diperlukan pada skrip Nmap dengan menggunakan opsi `--scripts-args key=value,key=value`. Berikut ini adalah hasil yang mungkin dari keluaran Nmap ketika melakukan brute force SSH melalui skrip NSE `ssh-brute`:



![nmap-image](assets/fr/49.webp)



hasil dari eksekusi bruteforce SSH melalui Nmap._



Seperti yang dapat Anda lihat, informasi yang dihasilkan oleh skrip NSE diawali dengan `NSE: [nama skrip]` pada keluaran interaktif (keluaran terminal), sehingga lebih mudah ditemukan. Dalam tampilan hasil Nmap yang biasa, kita hanya memiliki ringkasan yang mengindikasikan apakah pengidentifikasi yang lemah telah ditemukan atau tidak (termasuk kata sandi, ingat).



Untuk melangkah lebih jauh, dan untuk mengingatkan Anda bahwa semua ini dapat digunakan sebagai tambahan dari semua opsi yang telah kita lihat, berikut ini adalah perintah yang akan menemukan jaringan `10.10.10.0/24`, memindai 2000 port TCP yang paling sering digunakan, dan menjalankan pencarian akses anonim pada layanan FTP dan brute force pada layanan SSH:



```
# Example of a complete command using multiple scripts
nmap --top-ports 2000 10.10.10.0/24 --script ftp-anon,ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist
```



Ini hanyalah salah satu contoh dari sekian banyak skrip yang tersedia dan pilihannya. Namun, sekarang kita memiliki gambaran yang lebih baik tentang cara memahami skrip NSE, apakah skrip tersebut memerlukan argumen dan bagaimana cara meneruskan argumen tersebut ke Nmap.



### V. Kesimpulan



Pada bagian ini, kita telah mempelajari cara menggunakan skrip NSE Nmap untuk melakukan berbagai tugas. Saya mengundang Anda untuk meluangkan waktu untuk menemukan berbagai kategori skrip dan skrip itu sendiri, untuk melihat seberapa banyak pengujian yang dapat diotomatisasi.



Dalam beberapa bagian sekarang, kita telah mengumpulkan lebih banyak opsi penemuan, pemindaian, dan pencacahan tingkat lanjut. Sekarang, Anda seharusnya menyadari bahwa output dan tampilan hasil Nmap mulai menjadi sangat luas, bahkan terkadang terlalu bertele-tele untuk terminal kita. Pada bagian selanjutnya, kita akan belajar bagaimana menguasai keluaran ini, khususnya dengan menyimpannya dalam file dalam berbagai format.






## 9 - Mengelola data keluaran Nmap




### I. Presentasi



Pada bagian ini, kita akan melihat output yang dihasilkan oleh Nmap, dan khususnya pada berbagai pilihan untuk memformat output ini. Kita akan melihat bahwa Nmap dapat menghasilkan beberapa format keluaran untuk memenuhi kebutuhan yang berbeda, dan ini juga merupakan salah satu kekuatan besar dari alat ini.



Secara default, Nmap menawarkan tampilan mendetail tentang hasil pemindaian dan pengujian yang dilakukannya. Ini termasuk host dan layanan yang dipindai, yang terdeteksi dapat diakses, spesifikasi port yang terbuka, status dan versinya. Selain itu, detail skrip NSE juga tersedia di keluaran terminal. Namun, keluaran ini dapat dengan cepat menjadi sangat banyak, bahkan dengan format informasi yang jelas, yang dapat menyulitkan untuk menemukan informasi yang tepat dalam hasilnya.



### II. Menguasai format keluaran Nmap



#### A. Menyimpan hasil pemindaian dalam file teks



Untuk mempermudah, [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) membuatnya sangat mudah untuk menyimpan hasil pengujian dalam file teks. Hal ini dapat berguna untuk pengarsipan, perbandingan dengan tes lain, tetapi juga untuk menelusuri keluaran ini dengan alat pengolah kata khusus atau bahasa skrip, seperti Sublime text, [PowerShell] (https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/), Python, grep, sed, dll. Untuk menyimpan output standar Nmap dalam sebuah file teks, kita dapat menggunakan opsi `-oN <filename>` ("N" pada "normal"):



```
# Save Nmap output to a file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt
```



Tidak mengherankan, karena Nmap akan menampilkan output standar yang biasa di terminal kita, tetapi juga dalam file yang ditentukan.



#### B. Output generate Nmap dalam format ringkas



Ada juga format output kedua dalam gaya "teks" yang dapat dengan mudah ditafsirkan oleh manusia: format "greppable".



Format ini dibuat untuk memberikan tampilan "ringkas" dari keluaran Nmap, terstruktur sedemikian rupa untuk memfasilitasi pemrosesannya dengan alat bantu seperti `grep`. Mari kita lihat contoh jenis keluaran ini:



![nmap-image](assets/fr/50.webp)



pemindaian jaringan nmap dan keluaran dalam format "greppable"



Di sini, saya telah melakukan penemuan jaringan serta pemindaian port dan analisis teknologi dan versi pada jaringan /24, kemudian menyimpan hasilnya dalam sebuah file dalam format "greppable". Saya mendapatkan sebuah berkas yang berisi 2 baris per host yang aktif:





- Baris pertama memberi tahu saya bahwa host ini dan itu adalah _Up_;





- Baris kedua memberi tahu saya port mana yang telah dipindai, statusnya, serta informasi teknologi dan versi yang diambil dalam format yang sangat spesifik: `<port>/<status/<protokol>//<layanan>//<versi>/,`




Pemformatan dengan pembatas tetap ini memungkinkan pemrosesan yang cepat oleh alat pengolah kata seperti `grep`, atau skrip dan bahasa pemrograman. Perintah berikut ini, misalnya, memungkinkan saya untuk dengan mudah mengambil informasi tentang host `10.10.10.5` dalam kasus pemindaian besar-besaran yang dilakukan oleh Nmap yang hasilnya akan sulit untuk ditelusuri:



```
# Filter by IP address in the Nmap "greppable" file
grep '10.10.10.5' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Status: Up
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)
```



Sebaliknya, saya juga dapat dengan mudah membuat daftar semua host yang memiliki port 21 terbuka, karena port dan IP berada pada jalur yang sama:



```
# Filter by open port in the Nmap "greppable" file
grep '21/open' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)

Host: 10.10.10.152 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Indy httpd 18.1.37.13946 (Paessler PRTG bandwidth monitor)/, 135/open/tcp//msrpc//Microsoft Windows RPC/, 139/open/tcp//netbios-ssn//Microsoft Windows netbios-ssn/, 445/open/tcp//microsoft-ds//Microsoft Windows Server 2008 R2 - 2012 microsoft-ds/ Ignored State: closed (995)
```



Untuk membuat output seperti itu, kita perlu menggunakan opsi `-oG <filename>.gnmap` ("G" pada "grep"). Berdasarkan kebiasaan, saya menggunakan ekstensi `.gnmap` di sini untuk file seperti itu, tetapi silakan gunakan yang mana pun yang Anda suka:



```
# Save Nmap output to a file in "greppable" format
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap
```



Format ini dapat digunakan untuk berbagai tujuan dan khususnya berguna untuk pembuatan naskah/penyortiran yang cepat. Namun demikian, format ini cenderung ditinggalkan demi format yang akan kita bahas berikutnya.



catatan: format greppable `-oG` secara resmi sudah tidak digunakan lagi sejak Nmap 7.90. Format ini masih dapat digunakan untuk kompatibilitas. Format ini masih dapat digunakan untuk tujuan kompatibilitas, tetapi disarankan agar Anda menggunakan format XML atau format normal untuk pengembangan atau penguraian otomatis



#### C. Format XML untuk keluaran Nmap



Format terakhir yang perlu disebutkan dalam tutorial ini adalah XML. Tidak seperti dua format sebelumnya, format yang satu ini tidak dirancang untuk dibaca oleh manusia, tetapi oleh alat atau skrip lain.



XML (_eXtensible Markup Language_) adalah bahasa markup yang digunakan untuk menyimpan dan mengangkut data, yang menawarkan struktur hirarkis melalui tag khusus.



Di dalam Nmap, format XML digunakan untuk membuat laporan terperinci mengenai pemindaian yang dilakukan, termasuk informasi tentang host, port, dan kerentanan yang terdeteksi, serta informasi tambahan yang tidak ditampilkan di dalam keluaran Nmap standar.



Untuk generate file output dalam format XML, kita perlu menggunakan opsi `-oX` ("O" dari "XML"):



```
# Save Nmap output to a file in XML format
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```



Hasilnya adalah keluaran standar Nmap di terminal Anda, serta sebuah berkas dalam format XML di direktori Anda saat ini.



Tentu saja, format XML tidak dirancang untuk dibaca dan ditafsirkan oleh manusia. Namun demikian, jika Anda ingin melakukan skrip atau analisis otomatis pada format keluaran Nmap ini, Anda masih perlu memiliki gambaran tentang tag dan struktur yang digunakan. Sebagai contoh, berikut ini adalah bagian dari isi file XML yang dibuat oleh Nmap, yang menunjukkan hasil pemindaian untuk 1 host:



![nmap-image](assets/fr/51.webp)



contoh catatan XML untuk 1 host selama pemindaian Nmap



Ada banyak informasi di sini, dan kami sangat tertarik dengan dua port terbuka:



```
<port protocol="tcp" portid="21"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="ftp" product="Microsoft ftpd" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:ftp_service</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<port protocol="tcp" portid="80"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="http" product="Microsoft IIS httpd" version="7.5" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



Kami memahami bahwa format ini akan memudahkan penguraian hasil secara otomatis, karena setiap bagian informasi disusun dengan rapi dalam tag atau atribut khusus yang diberi nama. Secara khusus, kami menemukan sebuah informasi yang belum pernah kami temukan sebelumnya: CPE.



```
cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



Kami telah menyebutkan CPE secara singkat di bagian 2 modul 2, dan informasi ini ditentukan dalam pencocokan selama deteksi versi. Nmap menggunakan layanan, teknologi, dan mekanisme pendeteksian versi untuk menemukan CPE yang terkait.



Hal ini memungkinkan kita untuk menggunakan kembali informasi ini dengan basis data dan aplikasi yang menggunakannya. Saya secara khusus memikirkan basis data NVD, yang mereferensikan CVE. Untuk setiap CVE, database ini berisi CPE yang terpengaruh oleh kerentanan. Berikut adalah contoh CVE tentang `a:microsoft:internet_information_services:7.5` dari basis data NVD:



![nmap-image](assets/fr/52.webp)



adanya CPE dalam rincian CVE di database NVD



Kita sekarang memiliki pemahaman yang lebih baik tentang manfaat format ini, yang menawarkan struktur informasi yang sangat jelas dan berisi semua data yang dikumpulkan atau diproses oleh Nmap.



Sebagai refleks, saya secara sistematis menyimpan pindaian Nmap saya dalam ketiga format sekaligus. Hal ini dimungkinkan oleh opsi `-oA <nama>` ("A" untuk "Semua"), yang akan membuat file `<nama>.nmap`, file `<nama>.xml`, dan file `<nama>.gnmap`. Dengan cara ini, saya yakin tidak akan kehabisan apa pun ketika saya perlu memeriksa kembali hasilnya.



Dengan ketiga format ini, Anda seharusnya memiliki semua yang Anda perlukan untuk menyimpan dan pada akhirnya memproses hasil Nmap secara otomatis. Kita akan menggunakan format XML lagi di bagian berikutnya, ketika kita melihat penggunaan Nmap dengan alat keamanan lainnya.



#### III. Membuat laporan HTML dari pemindaian Nmap



Format XML menawarkan banyak kemungkinan, tidak terkecuali sebagai dasar untuk menghasilkan laporan dalam format HTML, yang akan lebih enak dilihat secara visual.



Untuk mengubah file Nmap dalam format XML menjadi halaman web, kita akan menggunakan alat `xsltproc`, yang harus kita instal terlebih dahulu:



```
# Install the xsltproc tool
sudo apt install xsltproc
```



Setelah alat ini diinstal, cukup berikan file XML yang akan dikonversi dan nama laporan HTML yang akan dihasilkan:



```
# Create an Nmap HTML report from XML
xsltproc nmap_10.10.10.0.xml -o "Nmap – rapport web 05-2024.html"

# Open the .html file with Firefox
firefox "Nmap – rapport web 05-2024.html"
```



Hasilnya, seluruh hasil pemindaian kita akan terstruktur dengan baik, bahkan dengan beberapa warna dan tautan yang dapat diklik dalam daftar isi!



![nmap-image](assets/fr/53.webp)



ekstrak dari laporan pemindaian Nmap dalam format HTML yang dihasilkan oleh xsltproc._



Secara umum, file XML yang disimpan oleh Nmap berisi referensi ke file lain dalam format XML:



```
<?xml-stylesheet href="/usr/share/nmap/nmap.xsl" type="text/xsl"?>
```



Oleh karena itu, konversi ke HTML merupakan fungsi yang disediakan dan difasilitasi oleh Nmap, `xsltproc` merupakan alat yang umum dan dikenal untuk melakukan tugas ini (yang tidak berasal dari paket alat Nmap).



XSLT (_Extensible Stylesheet Language Transformations_) adalah bagian dari XSL yang memungkinkan data XML ditampilkan pada halaman web dan "ditransformasikan", secara paralel dengan gaya XSL, menjadi informasi yang dapat dibaca dan diformat dalam format HTML.



sumber: [helpx.adobe.com/](https://helpx.adobe.com/fr/dreamweaver/using/xml-xslt.html)_



Tingkat informasi dalam laporan ini setara dengan format XML Nmap dan lebih tinggi daripada output terminal standar (_output interaktif_).



### IV. Mengelola tingkat verbositas Nmap



Sekarang kita akan melihat beberapa opsi untuk Debugger Nmap atau untuk melacak kemajuannya.



Opsi pertama yang harus kita sebutkan adalah opsi `-v`, yang meningkatkan verbositas Nmap. Berikut ini sebuah contoh:



![nmap-image](assets/fr/54.webp)



output verbose nmap menggunakan opsi `-v`._



Pada pemindaian yang menargetkan banyak host dan port, output terminal akan menjadi sulit untuk dieksploitasi karena banyaknya informasi yang ditampilkan. Karena alasan ini, opsi ini harus digunakan bersama dengan opsi yang terlihat sebelumnya, yang memungkinkan Anda untuk menyimpan output standar Nmap dalam sebuah file. Informasi yang berhubungan dengan penggunaan verbosity tidak akan dimasukkan ke dalam berkas keluaran ini. Seperti yang dapat Anda lihat dari contoh di atas, verbosity ini memungkinkan Anda untuk melacak tindakan dan penemuan Nmap secara jelas dan langsung. Untuk pemindaian yang lebih lama di mana tampilan data mungkin lambat, hal ini dapat menghindari ketidaktahuan akan aktivitas Nmap saat ini dan mengetahui bahwa segala sesuatunya sedang berjalan dan seberapa cepat. Untuk meningkatkan verbositas pada tingkat yang lebih tinggi, Anda dapat menggunakan opsi `-vv`.



Untuk melacak aktivitas Nmap lebih lanjut selama pemindaian, Anda dapat menggunakan opsi `--packet-trace`. Dengan opsi `-v`, kita mendapatkan log langsung dari semua port yang terbuka yang ditemukan oleh Nmap, sedangkan dengan opsi ini, kita mendapatkan baris log untuk setiap paket yang dikirim ke sebuah port. Hal ini tentu saja menghasilkan output yang sangat bertele-tele, tetapi memungkinkan pemantauan aktivitas Nmap secara rinci, berikut contohnya:



![nmap-image](assets/fr/55.webp)



pemantauan rinci aktivitas Nmap melalui `--packet-trace`._



Sekali lagi, informasi ini tidak akan direkam dalam file output yang dihasilkan oleh Nmap jika opsi `-oN`, `-oG`, `-oX` atau `-oA` digunakan.



Terakhir, Nmap juga menawarkan dua pilihan debug: `-d` dan `-dd`. Opsi-opsi ini berperilaku mirip dengan opsi verbosity `-v`, tetapi menambahkan informasi teknis tambahan, seperti ringkasan parameter teknis pada awal pemindaian:



![nmap-image](assets/fr/56.webp)



opsi waktu ditampilkan dalam tampilan debug Nmap



Dalam beberapa bagian berikutnya, kita akan mencermati, apa saja opsi "Timing" dan mengapa kita perlu mengetahuinya.



Terakhir, jika Anda hanya ingin mendapatkan gambaran umum sintetis dasar tentang kemajuan pemindaian Nmap, Anda dapat menggunakan opsi `--stats-every 5s`. "5s" di sini berarti 5 detik dan dapat dimodifikasi sesuai dengan kebutuhan Anda. Ini adalah frekuensi di mana kita akan menerima umpan balik dari Nmap tentang kemajuannya:



![nmap-image](assets/fr/57.webp)



informasi yang ditampilkan oleh opsi `--stats-every` dari Nmap



Secara khusus, kita bisa mendapatkan persentase kemajuan, serta indikasi fase yang sedang berlangsung: fase penemuan host melalui [ping] (https://www.it-connect.fr/le-ping-pour-les-debutants/), fase penemuan port TCP yang terbuka, dll. Informasi ini juga dapat diperoleh pada output terminal dengan menekan "Enter" selama pemindaian.



Namun, Nmap tidak terlalu bagus dalam memperkirakan berapa lama sebuah tugas akan berlangsung, paling tidak karena ia tidak tahu sebelumnya berapa banyak host dan layanan yang harus dipindai.



### V. Kesimpulan



Pada bagian ini, kita telah melihat sejumlah opsi untuk menyimpan hasil pemindaian Nmap dalam format file yang berbeda-beda. Ini akan sangat berguna, karena dalam konteks realistis, hasil pemindaian dapat terdiri dari ratusan atau bahkan ribuan baris! Kita juga telah melihat bagaimana meningkatkan tingkat verbositas Nmap untuk tujuan debugging atau untuk mendapatkan laporan kemajuan pemindaian.



Format XML akan sangat berguna pada bagian selanjutnya, di mana kita akan melihat beberapa alat yang dapat bekerja dengan hasil Nmap.




## 10 - Menggunakan Nmap dengan alat keamanan lainnya



### I. Presentasi



Pada bagian ini, kita akan melihat beberapa penggunaan klasik Nmap dengan alat keamanan sumber terbuka dan gratis lainnya. Secara khusus, kita akan menggunakan apa yang telah kita pelajari di bagian sebelumnya untuk lebih meningkatkan kekuatan dan efisiensi Nmap.



Kemampuan untuk menyimpan hasil pemindaian Nmap dalam bentuk XML membuat data tersebut kompatibel dengan sejumlah alat lainnya. Karena hampir semua bahasa pemrograman dan skrip saat ini memiliki pustaka yang mampu mengurai XML, hal ini membuatnya lebih mudah untuk memproses data ini. Sejumlah alat, terutama yang ditujukan untuk keamanan ofensif, memiliki fungsi untuk memproses format XML yang dihasilkan oleh Nmap. Mari kita lihat lebih dekat.



Saya akan menyebutkan beberapa alat ofensif tanpa merinci secara detail bagaimana alat tersebut digunakan atau cara kerjanya. Saya akan mengasumsikan bahwa pembaca sudah terbiasa dengan penggunaan dasar mereka dan sudah beroperasi. Bagian ini akan sangat menarik bagi para profesional [keamanan siber] (https://www.it-connect.fr/cours-tutoriels/securite-informatique/), orang-orang yang sedang dalam pelatihan atau mereka yang telah memutuskan untuk mempelajari lebih dalam tentang topik ini.



### II. Mengimpor hasil Nmap ke Metasploit



Alat pertama yang akan kita lihat untuk menggunakan kembali data Nmap dalam penelitian keamanan dan kerentanan ofensif adalah Metasploit.



Metasploit adalah sebuah kerangka kerja eksploitasi dan serangan. Ini adalah solusi gratis dan alat yang diakui yang berisi sejumlah besar modul yang ditulis dalam Ruby atau Python. Ini memungkinkan kerentanan untuk dieksploitasi, serangan dilakukan, pintu belakang dibuat, panggilan balik dikelola (fungsi C&C atau Komunikasi dan Kontrol) dan semuanya digunakan secara seragam.



Secara khusus, kerangka kerja operasi yang terkenal dan banyak digunakan ini dapat bekerja dengan [database] postgreSQL (https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) di mana host, port, layanan, informasi autentikasi dan banyak lagi disimpan.





- Dokumentasi resmi Metasploit: [https://docs.metasploit.com/](https://docs.metasploit.com/)




Di sinilah Nmap dan keluarannya berperan, karena format XML dari keluaran Nmap dapat dengan mudah diimpor ke dalam basis data Metasploit untuk mengisi basis data host dan layanannya, yang kemudian dapat dengan cepat ditetapkan sebagai target serangan ini atau itu.



Setelah berada di shell interaktif Metasploit, saya mulai dengan membuat ruang kerja, semacam ruang yang khusus untuk lingkungan saya saat itu:



```
# Create a Metasploit workspace
msf6 > workspace -a SI_siege
```



Setelah ruang kerja saya dibuat, kita perlu memvalidasi bahwa komunikasi dengan basis data sudah berjalan:



```
# Retrieve the database status
msf6 > db_status
[*] Connected to msf. Connection type: postgresql.
```



Terakhir, kita bisa menggunakan perintah Metasploit `db_import` untuk mengimpor pemindaian Nmap dalam format XML:



```
# Import a Nmap XML file into the database
msf6> db_import /tmp/nmap_10.10.10.0.xml
```



Berikut ini adalah hasil eksekusi semua perintah ini:



![nmap-image](assets/fr/58.webp)



mengimpor pemindaian Nmap dalam format XML ke dalam basis data Metasploit



Di sini Anda dapat melihat bahwa setiap hos diimpor, bersama dengan layanannya. Data ini kemudian dapat ditampilkan melalui perintah `services` atau `services -p <port>` untuk layanan tertentu:



![nmap-image](assets/fr/59.webp)



daftar layanan yang diimpor dari file XML ke dalam basis data Metasploit



Terakhir, kita dapat dengan cepat dan mudah menggunakan kembali data ini dalam modul berkat opsi `-R`, yang akan "mengubah" daftar layanan yang diperoleh sebagai masukan untuk direktif `RHOSTS`, yang digunakan untuk menentukan target serangan yang akan dilakukan. Berikut adalah contoh dengan modul `ssh_login`, yang memungkinkan Anda untuk melakukan serangan brute force terhadap layanan [SSH] (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/):



![nmap-image](assets/fr/60.webp)



gunakan opsi `services -R` untuk mengimpor layanan yang ditentukan sebagai target serangan



Ini hanyalah contoh kecil dari apa yang dapat dilakukan dengan data Nmap di Metasploit, tetapi ini memberi Anda sedikit gambaran tentang seberapa cepat dan mudahnya informasi ini dapat digunakan kembali sebagai bagian dari uji penetrasi, pemindaian kerentanan, atau serangan siber. Perlu juga disebutkan bahwa Nmap dapat dijalankan langsung dari Metasploit untuk mengimpor hasilnya ke dalam basis data (perintah `db_nmap`), topik lain yang menarik untuk dibahas!



### III. Menggunakan Nmap dengan pemindai web Aquatone



Alat kedua yang ingin saya perkenalkan di bagian ini tentang penggunaan kembali hasil Nmap untuk analisis keamanan dan kerentanan ofensif adalah Aquatone.



Aquatone adalah pemindai web yang dirancang untuk menjelajahi aplikasi web secara efisien di jaringan. Alat ini menawarkan fitur-fitur canggih untuk penemuan layanan web, identifikasi sub-domain, analisis port, dan sidik jari aplikasi web. Semua disajikan dengan jelas dan ringkas dalam laporan HTML, JSON, dan teks untuk analisis keamanan web yang mudah.



Seperti halnya Metasploit, Aquatone dapat secara langsung memproses format XML Nmap dan menggunakannya sebagai target pemindaian. Secara khusus, dia dapat mengekstrak hanya host dan layanan yang diminati (layanan web) dari semua data yang mungkin ada dalam laporan Nmap.





- Tautan alat: [Github - Michenriksen/aquatone](https://github.com/michenriksen/aquatone)




Untuk menggunakan output XML Nmap dengan Aquatone, cukup kirimkan file XML dalam pipa yang akan dikonsumsi oleh Aquatone. Berikut ini sebuah contoh:



```
# Send the Nmap XML output to Aquatone
cat /tmp/nmap_10.10.10.0.xml | ./aquatone -nmap
```



Di mana Aquatone biasanya melakukan penemuan port pada host untuk menemukan layanan web, dalam konteks ini hanya akan mengandalkan hasil dari Nmap, yang telah melakukan operasi ini, sehingga menghemat waktu:



![nmap-image](assets/fr/61.webp)



menggunakan hasil Nmap dalam format XML dengan `aquatone`._



Sebagai informasi, berikut ini adalah kutipan dari laporan yang dibuat oleh Aquatone:



![nmap-image](assets/fr/62.webp)



contoh laporan `aquatone`



Secara pribadi, saya sering menggunakan Aquatone untuk mendapatkan gambaran umum singkat tentang jenis situs web yang ada di jaringan, khususnya berkat fungsionalitas tangkapan layarnya.



Di sini sekali lagi, memiliki laporan Nmap yang lengkap dalam format XML akan menghemat waktu dan membuatnya mudah untuk digunakan kembali di alat lain.



### IV. Kesimpulan



Kedua contoh ini dengan jelas menunjukkan bahwa format XML Nmap memudahkan alat lain untuk menggunakan hasilnya, karena merupakan format data yang terstruktur dan mudah digunakan. Ada banyak alat lain yang mampu memproses hasil ini, seperti alat pelaporan otomatis, representasi grafis, atau pemindai kerentanan yang lebih kompleks dan berpemilik.



Tentu saja, Anda juga dapat mengembangkan skrip dan alat bantu Anda sendiri di Python, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/) atau bahasa lain dengan pustaka penguraian XML untuk memanipulasi dan menggunakan kembali data hasil Nmap sesuai keinginan Anda.



Bagian ini membawa kita ke akhir modul tutorial tentang penggunaan Nmap yang lebih lanjut, khususnya untuk pemindaian kerentanan melalui skrip NSE.



Bagian selanjutnya dari tutorial ini akan berfokus, antara lain, pada beberapa praktik terbaik tambahan yang lebih teknis dan kiat-kiat tentang pemindaian spesifik yang dapat dilakukan oleh Nmap. Kita juga akan melihat opsi pengoptimalan kinerja pemindaian, yang sangat berguna saat memindai jaringan besar.




## 11 - Meningkatkan kinerja pemindaian jaringan



### I. Presentasi



Pada bab ini, kita akan mempelajari cara mengoptimalkan kecepatan pemindaian jaringan yang dilakukan dengan Nmap dengan menggunakan berbagai opsi khusus. Secara khusus, kita akan mempelajari lebih lanjut tentang cara kerja Nmap, mulai dari manajemen _timeout_ hingga konfigurasi yang telah disimpan sebelumnya oleh alat ini.



Sekarang setelah kita melihat fitur-fitur Nmap, mari kita bahas lebih lanjut tentang binatang buas ini dan kekuatannya. Jika Anda pernah menggunakan alat ini pada jaringan besar, Anda mungkin menyadari bahwa beberapa pemindaian dapat memakan waktu lama, terlepas dari kekuatan alat ini. Dan dengan alasan yang bagus: perintah `nmap` yang sederhana dengan beberapa opsi dapat memindai jutaan paket yang menargetkan ratusan ribu sistem dan layanan potensial.



Terlebih lagi, beberapa konfigurasi peralatan jaringan mungkin secara sengaja memaksakan kecepatan yang lebih lambat (jumlah paket per detik), dengan risiko menolak paket Anda atau melarang IP Address Anda karena alasan keamanan.



Tergantung pada konteksnya, mungkin ada baiknya untuk mencoba dan mengoptimalkan semua ini, seperti yang akan kita lihat dalam bab ini.



Bagaimanapun, Anda dapat memeriksa nilai default dari parameter yang akan kita lihat, serta apakah opsi yang akan Anda gunakan telah diperhitungkan dengan benar, melalui debug Nmap (opsi `-d` yang terlihat pada bab sebelumnya):



![nmap-image](assets/fr/63.webp)



melihat opsi Pengaturan waktu melalui opsi `-d` Nmap._



### II. Mengelola kecepatan pemindaian Nmap



#### A. Mengelola paralelisasi



Secara default, Nmap menggunakan paralelisasi dalam pemindaian untuk mengoptimalkannya, dan semua parameter yang digunakannya dapat dimodifikasi melalui berbagai opsi. Namun, kasus yang benar-benar diperlukan untuk memodifikasi parameter ini cukup jarang terjadi, jadi kami tidak akan membahasnya secara mendetail dalam tutorial ini:





- `--min-hostgroup/max-hostgroup <size>`: ukuran grup pemindaian host paralel.





- `--min-paralelisme/max-paralelisme <numprobes>`: paralelisasi Probe.





- `--scan-delay/--max-scan-delay <time>`: menyesuaikan penundaan di antara Probe.




Ketahuilah bahwa mereka ada dan dapat digunakan.



#### B. Mengelola jumlah paket per detik



Secara default, Nmap sendiri menyesuaikan jumlah paket per detik yang dikirimnya sesuai dengan respons jaringan. Tetapi dimungkinkan untuk memaksa pengaturan ini dengan menentukan nilai tinggi dan/atau minimum yang harus diikuti dalam hal jumlah paket per detik. Pengaturan ini dibuat dengan menggunakan opsi `--min-rate <number>` dan `--max-rate <number>` di mana `number` mewakili jumlah paket per detik. Contoh:



```
# Limit the scan speed to 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300
```



Opsi-opsi ini memungkinkan Anda untuk menyesuaikan kecepatan pemindaian sesuai dengan kebutuhan spesifik Anda, baik untuk mempercepat prosesnya atau membatasi bandwidth yang digunakan. Kasus terakhir (membatasi kecepatan pemindaian) adalah yang kemungkinan besar akan mengarahkan Anda ke opsi ini, terutama jika Anda mengalami latensi jaringan saat menggunakan Nmap (yang cukup jarang terjadi).



### III. Mengelola kegagalan koneksi dan batas waktu



Parameter lain yang dapat kita mainkan untuk mengoptimalkan kecepatan pemindaian Nmap (atau menjamin akurasi yang lebih baik) adalah _timeout_ dan _retry_.



Untuk _timeouts_, ini adalah **tidak ada batas waktu respons** setelah itu Nmap akan berhenti menunggu respons dan menganggap layanan atau host tidak dapat dijangkau. Untuk _retry_, ini adalah **jumlah percobaan berturut-turut pada sebuah operasi** yang akan dilakukan Nmap sebelum melanjutkan.



Seperti halnya paralelisasi, manajemen _timeout_ dan _retry_ dapat diterapkan pada fase penemuan host atau layanan:





- `--min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <time>`: menentukan waktu pulang pergi Exchange. Sekali lagi, parameter ini sebenarnya dihitung dan disesuaikan dengan cepat selama pemindaian. Sepertinya Anda tidak perlu menggunakannya, karena Nmap menghitung waktu ini dengan cepat sesuai dengan reaksi jaringan.





- `--max-retries <number>`: membatasi jumlah pengiriman ulang paket selama pemindaian port. Secara default, Nmap dapat melakukan hingga 10 kali pengiriman ulang untuk satu layanan, terutama jika menemukan latensi atau kehilangan pada tingkat jaringan, tetapi dalam kebanyakan kasus hanya satu kali yang dilakukan.





- `--host-timeout <time>`: menentukan waktu maksimum yang akan dihabiskan Nmap pada sebuah host untuk semua operasinya, termasuk pemindaian port, deteksi layanan, dan operasi lain yang terkait dengan host tersebut. Jika interval waktu ini terlampaui tanpa respons atau **penyelesaian operasi**, Nmap akan meninggalkan host ini tanpa menampilkan hasil apa pun yang berhubungan dengannya, dan beralih ke host berikutnya dalam daftar. Hal ini memungkinkan Anda untuk mengontrol waktu maksimum yang dihabiskan Nmap pada host tertentu, menghindari terjebak pada host yang bandel dan mengoptimalkan waktu pemindaian secara keseluruhan.




Dalam pekerjaan saya sehari-hari, saya menggunakan opsi `--max-retries` dan `--host-timeout` untuk mengoptimalkan pemindaian saya:



```
# Optimization of a scan with 0 additional attempts and a timeout of 15 minutes per host
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m
```



Parameter ini menawarkan fleksibilitas tambahan untuk menyesuaikan perilaku pemindaian dengan kebutuhan dan kondisi jaringan tertentu. Namun, Anda harus menyadari implikasinya dalam hal beban pada host yang dipindai dan potensi hilangnya akurasi.



### IV. Penggunaan konfigurasi yang telah disiapkan



Berbagai pilihan yang telah kita lihat pada bab ini dapat digunakan secara terpisah atau sebagai bagian dari konfigurasi siap pakai yang ditawarkan oleh Nmap. Opsi yang memungkinkan _templates_ (template konfigurasi) ini digunakan adalah `-T <number>` atau `-T <nama>`. Terdapat 5 level _templates_ yang dapat digunakan:



```
-T<0-5>: Set timing template (higher is faster)
```



Secara default, Nmap menggunakan _template_ 3 (_normal_), yang secara umum sudah cukup.



Bagi saya, saya biasanya beroperasi dalam konteks di mana saya harus cukup cepat (sambil tetap selengkap mungkin) dan saya sering menggunakan opsi `-T4`.



```
# Use Nmap for a network scan with preset T4 (with debug)
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```



Berikut ini adalah informasi debug untuk pemindaian ini yang ditunjukkan kepada kita:



![nmap-image](assets/fr/64.webp)



penggunaan pengaturan `-T4` selama pemindaian Nmap



### V. Kesimpulan



Pada bab ini, kita telah melihat berbagai teknik dan opsi yang bisa Anda gunakan untuk mengelola kekuatan, agresivitas, dan kinerja Nmap. Opsi-opsi ini sangat berguna terutama ketika memindai jaringan besar, dan lebih jarang untuk tujuan siluman.



Di bab berikutnya, kita akan melihat beberapa praktik terbaik untuk menggunakan Nmap dan memastikan keamanannya.




## 12 - Keamanan dan kerahasiaan data saat menggunakan Nmap



### I. Presentasi



Pada bab ini, kita akan melihat sejumlah praktik yang baik untuk diadopsi sehubungan dengan keamanan dan, terutama, kerahasiaan data yang dihasilkan, diproses, dan disimpan oleh Nmap.



Penggunaan Nmap dalam sebuah sistem informasi dapat dengan cepat dikategorikan sebagai tindakan ofensif. Oleh karena itu, sejumlah tindakan pencegahan perlu dilakukan untuk bertindak dalam kerangka hukum, sekaligus menjamin keamanan target yang dituju, data yang dikumpulkan, dan sistem yang digunakan untuk pemindaian.



### II. Memperoleh otorisasi yang sesuai



Sebelum memindai jaringan atau sistem, pastikan Anda telah mendapatkan otorisasi yang sesuai. Memindai sistem untuk mencari kerentanan (`skrip NSE`) tanpa otorisasi mungkin ilegal, dan dapat menimbulkan konsekuensi hukum, terutama jika keamanan sistem informasi bukan merupakan bagian dari tugas resmi Anda.





- Sebagai pengingat: [KUHP: Bab III: Serangan terhadap sistem pemrosesan data otomatis](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




### III. Melindungi data sensitif



Hasil yang dihasilkan oleh Nmap dapat dianggap sensitif, terutama ketika mengandung informasi tentang kelemahan dalam sistem informasi yang dapat dieksploitasi oleh penyerang. Tetapi juga ketika mereka menyangkut sistem yang tidak dapat diakses oleh semua orang (misalnya sistem informasi yang sensitif, industri, perawatan kesehatan atau [cadangan] (https://www.it-connect.fr/cours-tutoriels/administration-systemes/autres/sauvegarde/)).



Kita juga telah melihat bahwa, tergantung pada skrip NSE yang digunakan, hasil pemindaian NSE dari [Nmap] (https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) juga dapat berisi pengidentifikasi.



Dengan demikian, orang jahat yang berhasil mengakses hasil pemindaian ini akan memiliki peta sistem informasi dan banyak informasi teknis, tanpa harus melakukan tindakan ini sendiri, dengan risiko terdeteksi.



Oleh karena itu, penting untuk berhati-hati agar tidak mengumpulkan atau menyimpan informasi sensitif secara tidak tepat ketika menggunakan Nmap, termasuk, namun tidak terbatas pada, yang berikut ini:





- Mengenkripsi data keluaran: jika Anda perlu menyimpan atau mengirimkan hasil pemindaian Nmap, pastikan untuk mengenkripsinya untuk melindungi kerahasiaan data. Hal ini akan mencegah penyadapan yang tidak sah atas informasi sensitif. Idealnya, data harus dienkripsi segera setelah keluar dari sistem yang digunakan untuk melakukan pemindaian (arsip ZIP yang dienkripsi dengan kata sandi yang kuat adalah awal yang sangat baik).





- Atur kontrol akses: pastikan hanya orang yang berwenang yang memiliki akses ke hasil pemindaian Nmap Anda di tempat penyimpanannya. Siapkan kontrol akses yang sesuai untuk melindungi informasi sensitif dari akses yang tidak sah.





- Kewaspadaan saat menangani data: ketika melakukan transit, menyalin atau memproses data hasil pemindaian, pastikan Anda menjaga keamanan data di bawah kontrol yang ketat. Ini berarti: jangan biarkan mereka tergeletak di direktori `Download` pada workstation yang terhubung ke Internet, jangan biarkan mereka transit melalui aplikasi file HTTP internal Exchange, jangan biarkan Notepad Anda terbuka tanpa mengunci workstation selama istirahat makan siang, dll.




### IV. Mengelola pemindaian agresif



Seperti yang telah kita lihat di sepanjang tutorial ini, Nmap dapat menjadi sangat bertele-tele di tingkat jaringan. Nmap juga dapat mengirim paket yang tidak diformat dengan benar, dan yang tidak secara ketat menghormati struktur protokol dalam frame jaringan dan paket yang dihasilkannya. Semua tindakan ini dapat berdampak pada sistem dan layanan tertentu, kadang-kadang sampai menyebabkan kerusakan atau kejenuhan sumber daya sistem dan jaringan.



Untuk menghindari insiden, Anda perlu menguasai perilaku Nmap dan mengetahui bagaimana menyesuaikannya dengan konteks penggunaannya, dengan menggunakan berbagai pilihan yang dibahas dalam tutorial ini. Kita tidak akan menggunakan Nmap dengan cara yang sama pada sistem informasi yang berisi [perangkat keras] industri (https://www.it-connect.fr/actualites/actu-materiel/) seperti pada jaringan pengguna yang terdiri dari sistem Windows yang dilindungi oleh firewall lokal atau dalam inti jaringan.



Semoga berbagai pelajaran dalam tutorial ini telah mengajarkan Anda cara menguasai dan menganalisis perilaku Nmap, tetapi cara terbaik untuk belajar adalah dengan melakukan. Jadi, pastikan Anda sudah terbiasa dengan opsi-opsi Nmap yang akan Anda gunakan.



### V. Melindungi sistem pemindaian



Pada bab pertama, kita telah melihat bahwa pada kebanyakan kasus, Nmap perlu dijalankan sebagai `root` atau administrator lokal. Hal ini karena Nmap melakukan operasi jaringan, terkadang pada level yang cukup rendah, melalui library jaringan, yang membutuhkan izin yang tinggi dan berisiko dari sudut pandang stabilitas sistem atau kerahasiaan aplikasi lain.



Akibatnya, Nmap dapat dilihat sebagai komponen sensitif dari sistem tempat ia diinstal. Pastikan untuk menggunakan Nmap versi terbaru, karena versi yang lebih lama mungkin mengandung kerentanan keamanan yang diketahui. Dengan menggunakan versi terbaru, Anda bisa meminimalkan risiko yang terkait dengan penggunaan alat ini.



Jika anda memilih untuk menggunakan Nmap tidak melalui sesi sebagai `root`, tetapi dengan memberikan hak istimewa khusus kepada pengguna istimewa sehingga dia memiliki semua yang dia perlukan untuk menggunakan Nmap (`sudo` atau _kemampuan_), ketahuilah bahwa Nmap dapat digunakan sebagai bagian dari peningkatan hak istimewa yang lengkap:



![nmap-image](assets/fr/65.webp)



peningkatan hak istimewa Nmap melalui `sudo`._



Di sini, saya menggunakan perintah Nmap melalui `sudo`, tetapi ini memungkinkan saya untuk mendapatkan shell interaktif sebagai `root` pada sistem, yang bukan merupakan tujuan awal.



Juga sangat tidak disarankan untuk menginstal Nmap pada sistem yang tidak dirancang untuk melakukan pemindaian jaringan. Saya khususnya berpikir tentang server atau workstation. Di satu sisi, ini akan menambah vektor potensial untuk peningkatan hak istimewa, tetapi di atas semua itu akan memberi penyerang akses mudah ke alat ofensif.



Terakhir, keamanan sistem yang digunakan untuk pemindaian harus dipastikan secara lebih luas, sehingga tidak menjadi vektor penyusupan atau kebocoran informasi. Sebagai administrator sistem, lebih baik menggunakan sistem khusus, idealnya dengan masa pakai yang terbatas, daripada menggunakan workstation Anda sendiri.



### VI. Kesimpulan



Kesimpulannya, pastikan Anda telah menguasai Nmap dengan baik sebelum menggunakannya dalam kondisi nyata atau produksi, dan waspada saat memproses dan mengelola hasilnya. Akan sangat disayangkan jika menyebabkan kerusakan, membocorkan data, atau memfasilitasi kompromi, ketika pendekatan awal ditujukan untuk meningkatkan keamanan perusahaan Anda.



## 13 - Pemindaian port melalui TCP: SYN, Connect, dan FIN



### I. Presentasi



Pada bab ini dan bab berikutnya, kita akan melihat lebih dekat berbagai jenis pemindaian TCP yang tersedia di Nmap, dimulai dari yang paling umum digunakan: Pemindaian SYN, Connect dan FIN.



Seperti yang mungkin sudah Anda ketahui, Nmap menawarkan beberapa opsi untuk pemindaian TCP:



![nmap-image](assets/fr/66.webp)



teknik pemindaian yang tersedia di Nmap._



Tujuannya di sini adalah untuk menjelaskan beberapa metode ini, untuk membantu Anda memahami perbedaannya, keuntungan dan keterbatasannya. Anda akan melihat bahwa, tergantung pada konteks atau apa yang ingin Anda ketahui, lebih baik memilih salah satu opsi atau yang lainnya.



### II. Pemindaian TCP SYN atau "Pemindaian Setengah Terbuka



Jenis pemindaian TCP pertama yang akan kita lihat adalah `TCP SYN Scan`, juga dikenal sebagai `Half Open Scan`. Jika Anda ingat pemindaian jaringan yang kita lakukan setelah pemindaian port pertama kita, ini adalah jenis pemindaian yang digunakan secara default oleh [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) ketika dijalankan dengan hak root.



Terjemahan ini akan membantu Anda memahami cara kerja pemindaian ini. Pada kenyataannya, pemindaian TCP SYN akan mengirimkan paket TCP SYN ke setiap port yang ditargetkan, yang merupakan paket pertama yang dikirim oleh klien (yang meminta untuk membuat koneksi) sebagai bagian dari TCP _Three way handshake_ yang terkenal. Biasanya, jika port terbuka di server target, dengan layanan yang berjalan di belakangnya, server akan mengirimkan kembali paket TCP SYN/ACK untuk memvalidasi SYN klien dan menginisialisasi koneksi TCP. Respons ini berupa paket TCP dengan flag SYN dan ACK yang diset ke 1, memungkinkan kita untuk mengonfirmasi bahwa port tersebut terbuka dan mengarah ke sebuah layanan.



Di sisi lain, jika port ditutup, server akan mengirimkan paket `TCP` dengan flag RST dan ACK yang diatur ke 1 untuk mengakhiri permintaan koneksi, sehingga kita akan tahu bahwa tidak ada layanan yang aktif di belakang port ini:



![nmap-image](assets/fr/67.webp)



diagram perilaku Pemindaian tCP SYN untuk port terbuka dan tertutup



Untuk mendapatkan gambaran yang lebih konkret tentang `TCP SYN Scan`, saya melakukan pemindaian port TCP/80 ke sebuah host yang memiliki server web aktif pada port ini. Menjalankan pemindaian jaringan dengan Wireshark, kita dapat melihat alur berikut ini (sumber pemindaian: `10.10.14.84`):



![nmap-image](assets/fr/68.webp)



penangkapan jaringan selama pemindaian TCP SYN untuk port terbuka



Pada baris pertama, kita melihat bahwa sumber pemindaian mengirimkan paket TCP ke host `10.10.10.203` pada port TCP/80. Dalam paket TCP ini, bendera SYN diatur ke 1 untuk mengindikasikan bahwa ini adalah permintaan inisialisasi koneksi TCP.



Kemudian, pada baris kedua, kita melihat bahwa target merespons dengan `TCP SYN/ACK`, yang berarti bahwa ia menerima untuk menginisialisasi koneksi dan oleh karena itu menerima aliran pada port TCP/80. Oleh karena itu, kita dapat menyimpulkan bahwa port TCP/80 terbuka dan server web ada pada server yang dipindai.



Host kita kemudian mengirimkan kembali paket RST untuk menutup koneksi, sehingga host yang dipindai tidak perlu mempertahankan koneksi TCP yang terbuka dan menunggu jawaban. Dalam kasus pemindaian pada banyak port, tidak menutup koneksi TCP dapat menyebabkan penolakan layanan, memenuhi jumlah koneksi yang menunggu untuk dijawab yang dapat dipertahankan oleh server (lihat [Wikipedia - Syn flood] (https://fr.wikipedia.org/wiki/SYN_flood))



Pada Wireshark, Anda akan dapat melihat status flag TCP untuk setiap pengujian yang kita lakukan. Ini akan menunjukkan apakah paket tersebut merupakan paket SYN, SYN/ACK, ACK, dll:



![nmap-image](assets/fr/69.webp)



melihat bendera TCP sebuah paket di Wireshark (TCP SYN di sini)



Sebaliknya, saya menjalankan pengujian yang sama antara kedua mesin, tetapi kali ini memindai port TCP/81 yang tidak ada layanan yang aktif (sumber pemindaian: `10.10.14.84`):



![nmap-image](assets/fr/70.webp)



penangkapan jaringan selama pemindaian TCP SYN untuk port tertutup



Host yang dipindai mengembalikan `TCP RST/ACK` sebagai respons terhadap `TCP SYN` ketika port tidak terbuka.



Seperti yang telah disebutkan, saat menjalankan Nmap dari terminal istimewa, TCP SYN Scan adalah mode default, dan dapat dipaksakan melalui opsi `-sS` (`scan SYN`):



```
# Execution of a TCP Syn Scan_
nmap -sS 192.168.1.15
```




Pemindaian `TCP SYN Scan` adalah pemindaian yang paling sering digunakan untuk alasan kecepatan. Di sisi lain, kegagalan klien untuk menyelesaikan _Three Way Handshake_ (yaitu tidak mengirim ACK setelah server SYN/ACK) dapat terlihat mencurigakan jika diamati terlalu sering pada server atau dari sumber yang sama pada jaringan. Memang, perilaku normal klien setelah menerima paket TCP SYN/ACK dalam menanggapi TCP SYN adalah mengirim `acknowledgement` (ACK) dan kemudian memulai Exchange.



Meskipun demikian, pemindaian ini menyediakan pemindaian yang sedikit lebih cepat, karena tidak perlu repot-repot mengirim ACK untuk setiap respons positif. Keuntungan dari SYN Scan adalah kecepatannya, karena hanya satu paket yang dikirim per port untuk dipindai, dengan mengorbankan peluang deteksi yang lebih besar.



Selain itu, pemindaian TCP SYN dapat mendeteksi apakah sebuah port difilter (dilindungi) oleh firewall. Bahkan, firewall di depan host target dapat dideteksi dari perilakunya saat menerima paket TCP SYN pada port yang seharusnya dilindungi. Firewall tersebut tidak akan merespons. Namun, seperti yang telah kita lihat, pada kedua kasus (port terbuka atau tertutup), ada respon dari host. Perilaku ketiga ini akan mengungkapkan keberadaan firewall antara host yang dipindai dan mesin yang menjalankan pemindaian. Inilah hasil yang dapat dikembalikan oleh Nmap ketika port yang dipindai disaring oleh firewall:



![nmap-image](assets/fr/71.webp)



tampilan nmap saat memindai port yang difilter



Ketika kami melakukan penangkapan jaringan pada waktu pemindaian, kami dapat melihat bahwa tidak ada respons yang diberikan:



![nmap-image](assets/fr/72.webp)



penangkapan jaringan selama pemindaian TCP SYN untuk port yang difilter oleh firewall



Perbedaan antara port tertutup dan port yang difilter adalah sebagai berikut: port yang difilter adalah port yang dilindungi oleh firewall, sedangkan port tertutup adalah port yang tidak ada layanan yang berjalan sehingga tidak dapat memproses paket TCP kami. Beberapa jenis pemindaian TCP, seperti pemindaian TCP SYN, dapat mendeteksi apakah sebuah port difilter, sedangkan jenis pemindaian lainnya tidak.



### III. Pemindaian TCP Connect atau Pemindaian Terbuka Penuh



Jenis pemindaian TCP yang kedua adalah `pemindaian TCP Connect`, juga dikenal sebagai `Pemindaian Terbuka Penuh`. Pemindaian ini bekerja dengan cara yang sama seperti pemindaian TCP SYN, tetapi kali ini mengembalikan `TCP ACK` setelah respons positif dari server (SYN/ACK). Inilah sebabnya mengapa disebut `Full Open', karena koneksi dibuka penuh dan dimulai pada setiap port yang dibuka selama pemindaian, sehingga menghormati TCP _Three Way Handshake_:



![nmap-image](assets/fr/73.webp)



diagram perilaku Pemindaian tCP Connect untuk port terbuka dan tertutup



Berikut ini adalah apa yang dapat dilihat saat transit jaringan selama `pemindaian TCP Connect` yang menargetkan port terbuka:



![nmap-image](assets/fr/74.webp)



mengendus jaringan selama pemindaian TCP Connect untuk port yang terbuka



Kita dapat melihat bahwa paket TCP pertama yang dikirim adalah `TCP SYN` yang dikirim oleh klien, dan server kemudian akan membalas dengan `TCP SYN/ACK`, yang mengindikasikan bahwa port tersebut terbuka dan menjadi tuan rumah sebuah layanan yang aktif. Untuk mensimulasikan klien yang sah secara keseluruhan, Nmap kemudian akan mengirim `TCP ACK` kembali ke server. Sebaliknya, ketika memindai port yang tertutup:



![nmap-image](assets/fr/75.webp)



penangkapan jaringan selama pemindaian TCP Connect untuk port tertutup



Perhatikan bahwa respons server terhadap paket `SYN` kita sekali lagi adalah paket `TCP RST/ACK`, sehingga kita dapat menyimpulkan bahwa port tersebut ditutup dan tidak ada layanan yang berjalan di dalamnya.



Saat menggunakan Nmap, opsi `-sT` (`scan Connect`) digunakan untuk melakukan Pemindaian TCP Connect. Harap diperhatikan bahwa bila Nmap digunakan dari sesi yang tidak diistimewakan, ini adalah mode pemindaian TCP default:



```
# Execution of a TCP Connect Scan
nmap -sT 192.168.1.15
```



`TCP Connect Scan` mensimulasikan permintaan koneksi yang lebih sah, dengan perilaku yang paling mirip dengan klien lambda, sehingga lebih sulit untuk mengenali pemindaian pada jumlah port yang lebih sedikit. Namun, ini lebih lambat, karena sepenuhnya menginisialisasi setiap koneksi TCP pada port yang terbuka pada mesin yang dipindai.



Pemindaian Nmap terhadap 10.000 port masih akan mudah terdeteksi jika layanan deteksi dan perlindungan intrusi jaringan (IDS, IPS, EDR) dipasang. Ketika penyerang ingin tetap low profile, dia akan cenderung berfokus pada sejumlah kecil port yang dipilih secara strategis, seperti 445 (SMB) atau 80 (HTTP), yang sering kali terbuka di server dan menghadirkan kerentanan umum.



Karena TCP Connect Scan mengharapkan respons dalam kedua kasus tersebut, ia juga dapat mendeteksi keberadaan firewall yang mungkin memfilter port pada host target.



### IV. Pemindaian TCP FIN atau "Pemindaian Siluman



Pemindaian FIN TCP, juga dikenal sebagai Pemindaian Siluman, menggunakan perilaku klien yang mengakhiri koneksi TCP untuk mendeteksi port yang terbuka.



Dalam TCP, akhir sesi berarti mengirim paket TCP dengan flag FIN diset ke 1. Dalam Exchange normal, server menghentikan semua komunikasi dengan klien (tidak ada respons). Jika server tidak memiliki koneksi TCP aktif dengan klien, server akan mengirimkan `RST/ACK`. Oleh karena itu, kita dapat membedakan antara port yang terbuka dan tertutup dengan mengirimkan paket `TCP FIN` ke sekumpulan port:



![nmap-image](assets/fr/76.webp)



diagram perilaku pemindaian tCP FIN untuk port terbuka dan tertutup



Saya kembali menangkap jaringan selama _Stealth scan_ dan inilah yang Anda lihat ketika port yang dipindai terbuka:



![nmap-image](assets/fr/77.webp)



penangkapan jaringan selama pemindaian TCP FIN untuk port terbuka



Kita dapat melihat bahwa klien mengirimkan satu atau dua paket untuk mengakhiri koneksi TCP dan server tidak merespons. Server hanya menerima akhir koneksi dan berhenti berkomunikasi.



Inilah yang kita lihat sekarang ketika kita memindai port yang tertutup:



![nmap-image](assets/fr/78.webp)



penangkapan jaringan selama pemindaian TCP FIN untuk port tertutup



Kita melihat bahwa server mengirimkan kembali paket `TCP RST/ACK`, jadi ada perbedaan perilaku antara port terbuka dan port tertutup, dan kita dapat membuat daftar port terbuka pada server dengan mengirimkan paket TCP FIN. Dengan menggunakan Nmap, opsi `-sF` (`scan FIN`) digunakan untuk melakukan TCP FIN Scan:



```
# Execution of a TCP Fin Scan
nmap -sF 192.168.1.15
```



TCP FIN Scan tidak bekerja pada host Windows, karena OS cenderung mengabaikan paket TCP FIN ketika dikirim ke port yang tidak terbuka. Jadi, jika Anda menjalankan TCP FIN Scan pada host Windows, Anda akan mendapatkan kesan bahwa semua port tertutup.



Itulah mengapa penting untuk mengenal beberapa metode pemindaian, dan memahami perbedaan di antara semua metode tersebut.



Karena dalam kedua kasus tersebut, TCP FIN tidak akan menunggu respons, maka ia tidak akan dapat mendeteksi keberadaan firewall di antara host target dan sumber pemindaian.



Berikut ini adalah contoh hasil pemindaian TCP FIN Nmap:



![nmap-image](assets/fr/79.webp)



hasil pemindaian TCP FIN oleh Nmap._



Bahkan, tidak adanya respons dari host pada port tertentu dapat berarti bahwa port tersebut difilter, tetapi juga berarti port tersebut terbuka dan aktif.



Pemindaian ini disebut sebagai "siluman", karena tidak banyak lalu lintas dan umumnya tidak menyebabkan pencatatan pada sistem yang ditargetkan. Ini dapat digunakan untuk menemukan port secara diam-diam di jaringan tanpa menimbulkan alarm. Namun, seperti yang disebutkan di atas, keefektifannya dapat bervariasi tergantung pada sistem target, seperti halnya kebijaksanaannya tergantung pada konfigurasi peralatan keamanan.



### V. Kesimpulan



Sekian untuk bab pertama dari dua bab tentang jenis pemindaian TCP yang berbeda yang ditawarkan oleh Nmap! Di bab berikutnya, kita akan melihat jenis pemindaian TCP XMAS, Null dan ACK, yang beroperasi dengan cara yang berbeda untuk mendeteksi port yang terbuka di sebuah host.





## 14 - Pemindaian port melalui TCP: XMAS, Null dan ACK



### I. Presentasi



Pada bagian ini, kita akan terus mengeksplorasi berbagai metode pemindaian TCP yang ditawarkan oleh Nmap. Di sini kita akan melihat metode `XMAS`, `Null` dan `ACK`, yang menggunakan fitur khusus TCP untuk mengambil informasi tentang port dan layanan yang terbuka pada target tertentu.



### II. Pemindaian TCP XMAS



XMAS Scan TCP sedikit tidak biasa karena sama sekali tidak mensimulasikan perilaku pengguna atau mesin normal pada jaringan. Bahkan, XMAS Scan akan mengirim paket TCP dengan flag `URG` (Mendesak), `PSH` (Dorong), dan `FIN` (Selesai) yang diatur ke 1, untuk mem-bypass firewall atau mekanisme pemfilteran tertentu.



Nama XMAS berasal dari fakta bahwa melihat bendera-bendera ini menyala adalah hal yang tidak biasa. Ketika ketiga bendera ditetapkan secara bersamaan dalam paket TCP, maka akan terlihat seperti pohon Natal yang menyala:



![nmap-image](assets/fr/80.webp)



bendera tCP yang digunakan dalam pemindaian XMAS



Tanpa membahas secara rinci tentang peran flag ini di sini, penting untuk diketahui bahwa ketika mengirim paket dengan ketiga flag ini diaktifkan, layanan yang aktif di belakang port target tidak akan mengembalikan paket apa pun. Di sisi lain, jika port ditutup, kita akan menerima paket TCP RST/ACK. Sekarang kita akan dapat membedakan antara perilaku port terbuka dan port tertutup ketika membuat daftar port pada mesin:



![nmap-image](assets/fr/81.webp)



diagram perilaku Pemindaian tCP XMAS untuk port terbuka dan tertutup



Masih mengikuti logika yang sama, pemindaian jaringan pada port TCP/80 dari sebuah host dengan server web yang aktif menunjukkan perilaku berikut ketika mendeteksi port terbuka (sumber pemindaian `10.10.14.84`):



![nmap-image](assets/fr/82.webp)



penangkapan jaringan selama pemindaian TCP XMAS untuk port terbuka



Kita dapat melihat bahwa sumber pemindaian mengirimkan dua paket TCP XMAS (dengan flag `FIN`, `PSH` dan `URG` diset ke 1) ke host `10.10.10.203` dan tidak ada balasan dari target, yang mengindikasikan bahwa port tersebut terbuka. Sebaliknya, ketika melakukan `TCP XMAS Scan` pada port yang tertutup, hasil yang diamati adalah sebagai berikut:



![nmap-image](assets/fr/83.webp)



penangkapan jaringan selama pemindaian TCP XMAS untuk port tertutup



Tanggapan terhadap paket TCP kita adalah `TCP RST/ACK`, yang mengindikasikan bahwa port tersebut ditutup. Untuk menggunakan teknik ini dengan Nmap, opsi `-sX` (`scan XMAS`) memungkinkan Anda untuk melakukan Pemindaian TCP XMAS:



```bash
# Execution of a TCP XMAS Scan
nmap -sX 192.168.1.15
```



Penting untuk dicatat bahwa pemindaian TCP XMAS tidak dapat mendeteksi firewall yang mungkin ada di antara target dan mesin pemindai, tidak seperti beberapa jenis pemindaian lain seperti TCP SYN atau Connect. Memang, firewall yang aktif di antara dua host akan memastikan bahwa tidak ada TCP yang kembali jika port yang ditargetkan difilter (yaitu dilindungi oleh firewall). Jika tidak ada jawaban, maka tidak mungkin untuk mengetahui apakah port tersebut dilindungi oleh firewall atau terbuka dan aktif. Anda juga harus menyadari bahwa, seperti halnya pemindaian TCP FIN, aplikasi atau sistem operasi tertentu seperti Windows dapat mendistorsi hasil pemindaian jenis ini.



catatan: dukungan untuk pemindaian XMAS/FIN/NULL pada versi Windows terbaru masih terbatas, dan hasilnya mungkin tidak konsisten pada jenis target ini. (Pembaruan 2025)_



### III. Pemindaian TCP Null



Berbeda dengan TCP XMAS scan, TCP Null scan akan mengirimkan paket TCP scan dengan semua flag diset ke 0. Ini juga merupakan perilaku yang tidak akan pernah ditemukan pada Exchange normal antar mesin, karena pengiriman paket TCP tanpa flag tidak ditentukan dalam RFC yang menjelaskan protokol TCP. Inilah sebabnya mengapa hal ini dapat dideteksi dengan lebih mudah.



Seperti pemindaian TCP XMAS, pemindaian ini dapat mengganggu firewall atau modul penyaringan tertentu, sehingga memungkinkan paket untuk melewatinya:



![nmap-image](assets/fr/84.webp)



diagram perilaku Pemindaian Null tCP untuk port terbuka dan tertutup



Berikut ini adalah apa yang dapat dilihat di jaringan selama pemindaian TCP Null pada port terbuka:



![nmap-image](assets/fr/85.webp)



penangkapan jaringan selama pemindaian TCP Null untuk port terbuka



Mesin pemindaian mengirimkan paket tanpa bendera (`[<None>]` di Wireshark) tanpa respons apa pun dari server. Sebaliknya, ketika port target ditutup:



![nmap-image](assets/fr/86.webp)



penangkapan jaringan selama pemindaian TCP Null untuk port tertutup



Untuk melakukan pemindaian TCP Null dengan Nmap, cukup gunakan opsi `-sN` (`pindai Null`):



```bash
# Execution of a TCP Null Scan
nmap -sN 192.168.1.15
```



Karena respons ketika port terbuka dan ketika firewall aktif (tidak ada umpan balik dari server dalam kedua kasus tersebut) adalah identik, pemindaian TCP Null tidak dapat mendeteksi keberadaan firewall. Terlebih lagi, firewall bahkan dapat memalsukan hasilnya dengan menyarankan bahwa port terbuka, karena tidak merespons paket TCP tanpa flag, meskipun port tersebut difilter. Ini adalah informasi penting yang harus diperhatikan ketika menggunakan pemindaian yang tidak dapat membedakan antara port yang terbuka dan port yang difilter (dilindungi firewall), seperti pemindaian `TCP Null`, `XMAS`, atau `FIN`, agar tetap konsisten dalam interpretasi hasil yang diperoleh.



### IV. Pemindaian TCP ACK



Pemindaian TCP ACK digunakan untuk mendeteksi keberadaan firewall pada host target atau antara target dan sumber pemindaian.



Tidak seperti pemindaian lainnya, pemindaian TCP ACK tidak mencoba mengidentifikasi port mana yang terbuka pada host, tetapi lebih pada apakah sistem penyaringan aktif, merespons setiap port dengan `filtered` atau `unfiltered`. Beberapa pemindaian TCP, seperti `TCP SYN` atau `TCP Connect`, dapat melakukan keduanya secara bersamaan, sementara yang lain, seperti `TCP FIN` atau `TCP XMAS`, tidak dapat menentukan keberadaan penyaringan sama sekali. Inilah sebabnya mengapa pemindaian TCP ACK dapat berguna:



![nmap-image](assets/fr/87.webp)



diagram perilaku pemindaian ACK tCP untuk port yang difilter dan tidak difilter



Kita akan menggunakan opsi `-sA` dari Nmap untuk melakukan jenis pemindaian ini. Berikut adalah hasil pemindaian TCP ACK jika port difilter, yaitu diblokir dan dilindungi oleh firewall:



![nmap-image](assets/fr/88.webp)



tampilan nmap selama Pemindaian TCP ACK._



Contoh hasil untuk host dengan firewall dan tanpa firewall. Nmap mengembalikan `filtered` pada port TCP/80 dan TCP/81 dari host `10.10.10.203`. Pada analisis jaringan melalui Wireshark, perilakunya adalah sebagai berikut:



![nmap-image](assets/fr/89.webp)



penangkapan jaringan selama pemindaian TCP ACK untuk port yang tidak difilter oleh firewall



Mesin target tidak mengembalikan apa pun jika ada firewall.



Untuk meluncurkan pemindaian ini dengan Nmap, gunakan opsi `-sA` (`scan ACK`):



```bash
# Execution of a TCP ACK Scan
nmap -sA 192.168.1.15
```



### V. Kesimpulan



Kita telah melihat tiga metode pemindaian yang berbeda melalui TCP sebagai tambahan dari yang sudah disajikan. Metode-metode yang berbeda ini digunakan dalam kondisi dan konteks yang sangat spesifik, terutama dalam konteks uji penetrasi atau operasi Tim Merah, di mana terdapat gagasan tentang kebijaksanaan.



## 15 - Nmap CheatSheet - Ringkasan perintah tutorial



### I. Presentasi



Berikut ini adalah ringkasan singkat dari banyak perintah dan kasus penggunaan Nmap, sehingga Anda dapat dengan cepat menemukan dan menggunakannya kembali dalam penggunaan sehari-hari.



### II. Nmap: CheatSheet IT-Connect



Berikut ini adalah lembar sontekan dari perintah-perintah yang disajikan. Halaman ini memudahkan untuk menemukan penggunaan Nmap yang paling umum.





- Pemindaian port




```bash
# Display installed Nmap version
nmap --version

# Scan for open specific ports on a single IP address
nmap --open -p 80 192.168.1.18

# Scan TCP ports on a selection of ports
nmap 192.168.1.19 -p 80
nmap 192.168.1.19 -p 22,80,1000-2000,3389

# Scan UDP services on an IP address
nmap -sU 192.168.1.19

# Scan UDP services on specific ports
nmap -sU 192.168.1.19 -p 161,23

# Scan the 100 most commonly used TCP ports
nmap 192.168.1.19 --top-ports 100

# Scan all ports on an IP address
nmap 192.168.1.19 -p-

# Scan multiple subnets with specific ports
nmap 192.168.0.0/24 192.168.1.0/24 -p 22

# Scan a subnet while excluding a specific IP address, scan all ports
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```





- Menemukan host yang aktif




```bash
# Scan on CIDR or IP ranges
nmap 192.168.0.0/24
nmap 192.168.0.0/24 192.168.1.0/24
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20

# Host discovery scan (Ping Scan) on a network
nmap -sn 192.168.1.0/24
```



catatan: Opsi `-sP` sudah tidak digunakan lagi selama beberapa tahun dan sebaiknya diganti dengan `-sn`. (Pembaruan 2025)_



```bash
# Host discovery scan without port scan
nmap 192.168.1.0/24 -sn

# Host discovery scan on a local network using various probe techniques
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24

# Scan hosts listed in a text file
nmap -iL /tmp/mesCibles.txt

# Network scan with a specific IP excluded
nmap 192.168.1.0/24 --exclude 192.168.1.140

# Subnet scan excluding another subnet
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```





- Deteksi versi




```bash
# Enable version detection
nmap 192.168.1.0/24 -sV

# Version detection + advanced trace
nmap 192.168.1.0/24 -sV --version-trace

# Version detection with maximum probe rarity of 2
nmap 192.168.1.0/24 -sV --version-intensity 2

# Version detection with all probes
nmap 192.168.1.0/24 -sV --version-intensity 9

# Enable OS detection
nmap -O 10.10.10.0/24
```





- Skrip NSE: mencari kerentanan




```bash
# Run default NSE scripts
nmap -sC 10.10.10.152

# Scan all TCP ports with default NSE scripts
nmap -sC -p- 10.10.10.152

# Display help for script by name
nmap --script-help=ftp-*

# Display help for a category
nmap --script-help=discovery

# Use NSE scripts by category
nmap --script default 10.10.10.152
nmap --script discovery 10.10.10.152

# Inclusion/exclusion filter for NSE script categories
nmap --script "discovery and safe" 10.10.10.152
nmap --script "not intrusive and not dos" 10.10.10.152
nmap --script "vuln and not intrusive and not dos" 10.10.10.152
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152

# Run a specific NSE script
nmap --script ftp-anon -p 21 10.10.10.152
nmap --script ftp-anon 10.10.10.152

# Pass arguments to an NSE script
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```





- Manajemen keluaran Nmap




```bash
# Save scan to text file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt

# Save scan to condensed text file
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap

# Save scan to XML file
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```





- Optimalisasi kinerja




```bash
# Version detection scan with max rate of 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300

# Version detection scan with default scripts, no retry, max host timeout 15min
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m

# Version detection scan with the 2000 most common ports, aggressive scan speed (T4), debug output
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```





- Jenis pemindaian TCP




```bash
# TCP SYN scan (fast, less stealthy)
nmap -sS 192.168.1.15

# TCP Connect scan (classic)
nmap -sT 192.168.1.15

# TCP FIN scan (stealth)
nmap -sF 192.168.1.15

# TCP XMAS scan
nmap -sX 192.168.1.15

# TCP Null scan
nmap -sN 192.168.1.15

# TCP ACK scan (detect firewall)
nmap -sA 192.168.1.15
```



Saya harap Anda menemukan perintah-perintah ini berguna. Jangan lupa untuk menyesuaikan target pemindaian Anda dengan konteks Anda dan merujuk ke dokumentasi resmi untuk menguasai sepenuhnya pengujian yang dilakukan.



### III. Kesimpulan



Tutorial Nmap sekarang sudah selesai. Anda sekarang memiliki dasar-dasar yang Anda perlukan untuk menggunakan alat yang komprehensif dan kuat ini. Kami sangat menyarankan Anda untuk berlatih di lingkungan terkontrol (Hack The Box, VulnHub, mesin virtual) sebelum menggunakannya dalam produksi.



Masih banyak yang harus dieksplorasi tentang cara kerja alat ini dan fitur-fitur canggihnya. Namun, penguasaan perintah dan konsep yang disajikan di sini akan memungkinkan Anda untuk menggunakan Nmap dengan percaya diri dan relevan.