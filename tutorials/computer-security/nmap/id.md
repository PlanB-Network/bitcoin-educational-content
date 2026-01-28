---
name: Nmap
description: Master Nmap untuk pemetaan jaringan dan pemindaian kerentanan
---

![cover](assets/cover.webp)

*Tutorial ini didasarkan pada konten asli oleh Mickael Dorigny yang dipublikasikan di [IT-Connect](https://www.it-connect.fr/). Lisensi [CC BY-NC 4.0(https://creativecommons.org/licenses/by-nc/4.0/). Perubahan telah dilakukan pada teks asli.*

___

Selamat datang di tutorial pengantar Nmap ini, yang dirancang untuk siapa pun yang ingin menguasai aplikasi pemindai jaringan yang andal ini. Tujuannya adalah untuk memberi Anda pengetahuan fundamental yang Anda butuhkan untuk menggunakan Nmap secara efektif dalam kegiatan sehari-hari.

Nmap adalah aplikasi serbaguna, yang banyak digunakan oleh para profesional IT, jaringan, dan keamanan siber untuk diagnostik, penemuan jaringan, dan audit keamanan. Tutorial ini ditujukan bagi mereka yang baru di bidang ini dan ingin mempelajari dasar-dasar Nmap. Disarankan untuk memiliki pengetahuan dasar tentang sistem dan administrasi jaringan.

Anda akan mempelajari dasar-dasar Nmap, cara melakukan pemindaian port, mengidentifikasi host aktif di jaringan, mendeteksi versi layanan dan sistem operasi, melakukan pemindaian kerentanan, dan banyak lagi. Setiap bagian menyertakan penjelasan terperinci dan contoh praktis untuk membantu Anda menguasai penggunaan Nmap dalam berbagai konteks.

Pada akhir tutorial ini, Anda akan memiliki pemahaman yang kuat tentang Nmap dan dapat menggunakannya secara efektif untuk meningkatkan keamanan dan manajemen jaringan Anda. Selamat membaca.

## 1 - Pengantar ke Nmap: Apa itu Nmap?

### I. Presentasi

Di bagian pertama ini, kita akan melihat aplikasi pemindai jaringan Nmap. Kita akan membahas elemen-elemen kunci yang perlu Anda ketahui tentang alat ini dan cara kerjanya secara umum. Ini akan membantu kita untuk lebih memahami bagian tutorial selanjutnya.

### II. Memperkenalkan aplikasi Nmap

Nmap, singkatan dari _Network Mapper_, adalah aplikasi open-source gratis yang digunakan untuk **pencarian jaringan, pemetaan, dan audit keamanan**. Aplikasi ini juga dapat digunakan untuk tugas lain seperti inventarisasi jaringan, diagnostik, atau pengawasan.

Aplikasi ini dapat menentukan apakah host di jaringan target aktif dan dapat dijangkau, layanan jaringan apa yang terbuka, versi dan teknologi apa yang digunakan, dan informasi analisis berguna lainnya. Nmap dapat digunakan untuk memindai satu layanan pada perangkat tertentu, atau di seluruh bagian jaringan yang luas, hingga seluruh Internet.

Kelebihan Nmap sangat banyak:

- **Andal dan fleksibel**: Nmap dapat memindai jaringan besar dan menggunakan teknik deteksi canggih. Nmap mendukung UDP, TCP, ICMP, IPv4, dan IPv6, dan dapat melakukan deteksi versi, pemindaian kerentanan, atau interaksi spesifik protokol. Arsitekturnya modular, berkat skrip NSE (Nmap Scripting Engine), yang akan kita bahas nanti di tutorial ini.
- **Mudah digunakan**: Dokumentasi resminya melimpah dan berkualitas tinggi. Sumber daya komunitas yang tak terhitung jumlahnya juga tersedia untuk membantu Anda memulai.
- **Popularitas dan jangka panjang**: Nmap telah menjadi rujukan di bidangnya sejak tahun 1998. Versi saat ini, pada saat pembaruan ini, adalah 7.95. Meskipun aplikasi lain ada untuk tugas-tugas spesifik, Nmap tetap menjadi aplikasi yang wajib dimiliki untuk pemetaan dan analisis jaringan.

**Nmap dalam film**

Nmap adalah salah satu dari sedikit aplikasi keamanan yang telah memperoleh popularitas tertentu di kalangan masyarakat umum. Aplikasi ini muncul di film _Matrix Reloaded_, dalam sebuah adegan ikonik di mana Trinity menggunakannya untuk meretas sistem:

![nmap-image](assets/fr/01.webp)

_matriks: Adegan yang dimuat ulang yang menampilkan Nmap_

Nmap juga muncul dalam karya sinematografi lainnya.

**Ulasan**

Sebagai administrator sistem dan kemudian auditor keamanan siber dan pentester, **saya menggunakan Nmap hampir setiap hari** dan **saya secara teratur merekomendasikannya kepada administrator sistem yang ingin memperkuat penguasaan mereka terhadap jaringan dan meningkatkan kemampuan diagnostik mereka**.

### III. Operasi tingkat tinggi

Nmap tersedia untuk Linux, Windows, dan macOS. Aplikasi ini terutama ditulis dalam bahasa C, C++, dan Lua (untuk skrip NSE). Nmap terutama digunakan pada command line, meskipun interface grafis seperti Zenmap juga tersedia. Namun, kami sangat menyarankan Anda untuk memulai dengan command line untuk lebih memahami cara kerjanya.

Berikut contoh sederhana:

```
nmap 192.168.10.13 10.10.10.0/24 -sV -sC --top-ports 250
```

Perintah ini akan dijelaskan secara rinci nanti. Dalam tutorial ini, kita akan menggunakan Nmap di Linux, tetapi penggunaannya serupa pada sistem lain. Pada Windows, Nmap mengandalkan library **Npcap** (menggantikan WinPcap yang sekarang sudah usang) untuk menangkap dan menginjeksi paket jaringan.

Nmap digunakan seperti biner konvensional, seperti `ls` atau `ip`. Beberapa fitur canggih mungkin memerlukan hak istimewa yang lebih tinggi, karena aplikasi ini terkadang memanipulasi paket dengan cara yang tidak biasa untuk memancing reaksi spesifik pada sistem target (terutama untuk deteksi layanan atau kerentanan).

### IV. Efek penggunaan Nmap

Sebelum menggunakan Nmap, penting untuk menyadari efek potensial yang dapat ditimbulkannya pada jaringan dan sistem:

- Nmap dapat mengirim **ribuan bahkan jutaan paket** dalam waktu singkat, yang dapat memenuhi infrastruktur jaringan tertentu.
- Nmap dapat menghasilkan paket yang **tidak terbentuk dengan baik atau non-standar**, yang kemungkinan besar akan mengganggu peralatan tertentu (terutama sistem industri).
- Nmap dapat menghasilkan **perilaku seperti serangan**, yang dapat memicu peringatan di sistem keamanan (firewall, IDS/IPS, dll.).

Secara umum, **Nmap adalah aplikasi yang sangat "cerewet"**, karena menghasilkan banyak lalu lintas untuk mendapatkan informasi sebanyak mungkin. Oleh karena itu, disarankan untuk sepenuhnya memahami cara kerjanya sebelum menggunakannya di lingkungan yang sensitif atau dalam produksi.

### V. Kesimpulan

Bagian ini memperkenalkan Nmap dan fitur-fitur utamanya. Kita telah melihat bahwa Nmap adalah aplikasi pemetaan jaringan yang penting, andal, dan fleksibel. Kami juga telah membahas cara kerjanya dan tindakan pencegahan yang perlu Anda ambil saat menggunakannya, untuk menyiapkan materi untuk bagian-bagian tutorial berikutnya.

## 2 - Mengapa menggunakan Nmap?

### I. Presentasi

Di bagian ini, kita akan melihat penggunaan utama dari aplikasi pemindai jaringan Nmap. Kita akan melihat bahwa ini adalah aplikasi yang banyak digunakan dalam berbagai konteks dan profesi, dan memilikinya di deretan aplikasi Anda serta mengetahui cara menguasainya pastinya merupakan keterampilan yang berguna.

### II. Menggunakan Nmap untuk diagnostik dan pengawasan

Nmap dapat digunakan untuk diagnostik jaringan dan, secara lebih luas, untuk pemantauan. Sama seperti ping dapat digunakan untuk menentukan apakah dua host berkomunikasi, Nmap dapat digunakan untuk dengan cepat menentukan apakah sebuah host aktif, atau apakah layanan tertentu beroperasi. Berkat [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/ "Nmap"), kita bisa mendapatkan data yang akurat mengenai waktu respons host, rute yang diambil oleh paket, respons yang dibuat oleh layanan tertentu, dll.

Perintah dan hasil berikut dapat digunakan, misalnya, untuk dengan cepat mengetahui apakah server web pada host **192.168.1.18** aktif dan merespons dengan benar:

```
nmap --open -p 80 192.168.1.18
```

![nmap-image](assets/fr/02.webp)

_Menggunakan Nmap untuk mengetahui status layanan web dari server jarak jauh_

Jadi, menggunakan Nmap melampaui "uji ping terkenal" selama fase debugging atau diagnostik. Kita akan melihat nanti bahwa ada beberapa metode yang digunakan oleh Nmap untuk mengidentifikasi layanan mana yang berkomunikasi pada port tertentu, termasuk versinya.

### III. Menggunakan Nmap untuk pemetaan jaringan


- **Kuat dan fleksibel**: Nmap dapat memindai jaringan yang besar dan menggunakan teknik deteksi tingkat lanjut. Nmap mendukung UDP, TCP, ICMP, IPv4 dan IPv6, dan dapat melakukan deteksi versi, pemindaian kerentanan, atau interaksi khusus protokol. Arsitekturnya modular, khususnya berkat skrip NSE (Nmap Scripting Engine), yang akan kita lihat nanti dalam tutorial ini.
- **Kemudahan penggunaan**: dokumentasi resmi berlimpah dan berkualitas tinggi. Berbagai sumber daya komunitas juga tersedia untuk membantu Anda memulai.
- **Popularitas dan umur panjang**: Nmap telah menjadi referensi di bidangnya sejak tahun 1998. Versi saat ini, pada saat pembaruan ini, adalah 7.95. Meskipun ada alat lain untuk tugas-tugas tertentu, Nmap tetap harus dimiliki untuk pemetaan dan analisis jaringan.

Misalnya, perintah berikut dapat digunakan untuk dengan cepat mengidentifikasi host aktif di jaringan **192.168.1.0/24**:

```
nmap -sn 192.168.1.0/24
```

*Catatan: opsi `-sP` sudah tidak berlaku dan sudah digantikan oleh `-sn`.*

![nmap-image](assets/fr/03.webp)

*Menggunakan Nmap untuk menemukan host yang dapat dijangkau di jaringan*

Kita akan melihat nanti bahwa ada beberapa metode yang digunakan oleh Nmap untuk menentukan apakah sebuah host dapat dianggap "aktif", meskipun pada dasarnya tidak mengekspos layanan apa pun secara apriori.

### IV. Menggunakan Nmap untuk mengevaluasi kebijakan penyaringan

Nmap memiliki keuntungan sebagai aplikasi yang faktual: hasilnya memungkinkan untuk membuat temuan nyata, tidak seperti berupa dokumen arsitektur atau kebijakan penyaringan. Ini adalah aplikasi penting untuk menilai efektivitas kompartementalisasi sistem informasi, karena memungkinkan Anda **memverifikasi apakah kebijakan penyaringan benar-benar diterapkan**.

Dalam jaringan perusahaan, pengalaman terbaik menentukan bahwa sistem disegmentasi sesuai dengan peran, tingkat kekritisan, atau lokasinya. Aturan penyaringan (sering kali diimplementasikan melalui firewall) harus membatasi komunikasi antar zona. Tetapi konfigurasi ini sering kali rumit dan rawan kesalahan.

Jadi, untuk memvalidasi bahwa kebijakan telah dipatuhi, tidak ada yang lebih baik dari uji konkret. Misalnya, Anda dapat memeriksa bahwa layanan administrasi yang sensitif (SSH, WinRM, MSSQL, MySQL, dll.) tidak dapat diakses dari zona pengguna.

Penggunaan **Nmap untuk menguji kebijakan penyaringan** harus sistematis sebelum kebijakan tersebut dimasukkan ke dalam produksi. Sayangnya, pemeriksaan ini sering diabaikan.

Dalam pengalaman saya, banyak kesalahan konfigurasi tidak terdeteksi karena tidak adanya uji validasi. Kesalahan sederhana dalam rentang IP atau kelalaian aturan dapat membuat zona yang seharusnya terisolasi menjadi rentan.

### V. Menggunakan Nmap untuk audit keamanan dan pengujian penetrasi

Nmap memiliki **banyak fitur yang berguna untuk penilaian keamanan**, pengujian penetrasi (pentests), dan sayangnya juga untuk penyerang.

Fungsi penemuan jaringan sangat penting bagi penyerang, yang perlu memahami topologi jaringan setelah penyusupan awal. Tetapi Nmap menawarkan lebih dari ini: Nmap mengintegrasikan mesin skrip, **banyak di antaranya didedikasikan untuk deteksi kerentanan**.

Misalnya, perintah ini dapat digunakan untuk memeriksa apakah layanan FTP mengizinkan koneksi anonim, tanpa harus terhubung secara manual:

```
nmap --script ftp-anon -p 21 192.168.1.18
```

**Umpan balik**

*Menggunakan skrip NSE untuk memeriksa autentikasi FTP anonim melalui Nmap.*

Deteksi kerentanan Nmap adalah salah satu langkah pertama dalam audit atau pengujian penetrasi. Ini memungkinkan Anda untuk dengan cepat mengidentifikasi titik lemah tertentu dan mengoptimalkan upaya analisis Anda.

Tetapi hati-hatilah: **aplikasi pemindai kerentanan memiliki keterbatasan**. Nmap hanya mencakup sebagian kecil dari ancaman, dan tidak menjamin bahwa sebuah sistem aman jika tidak ada masalah yang terdeteksi. Oleh karena itu, penting untuk memahami cara kerja skrip yang digunakan dan tidak hanya mengandalkan keputusannya.

### VI. Kesimpulan

Kita telah melihat bahwa menguasai Nmap dapat mencakup berbagai kasus penggunaan, mulai dari diagnostik dan pemantauan hingga pemetaan, evaluasi kebijakan keamanan, dan pemindaian kerentanan. Di bagian selanjutnya, kita akan mulai dengan hal-hal yang lebih mendalam dan menginstal Nmap.

## 3 - Menginstalasi dan mengonfigurasi Nmap

### I. Presentasi

Di bagian ini, kita akan belajar cara menginstal aplikasi pemindai jaringan Nmap di Linux dan OS Windows. Di akhir bagian ini, kita akan memiliki semua yang kita butuhkan untuk mulai menggunakan Nmap untuk modul-modul selanjutnya. Terakhir, kita akan melihat hak istimewa apa yang mungkin diperlukan saat digunakan dan mengapa.

### II. Menginstalasi Nmap di Linux

Nmap awalnya dirancang untuk berjalan pada sistem operasi GNU/Linux. Sebagai hasilnya, dan berkat ketahanan dan popularitasnya, Anda akan menemukannya di semua repositori resmi distribusi utama Unix. Dalam tutorial ini, saya akan menggunakan sistem operasi berbasis Debian, [Kali Linux](https://www.it-connect.fr/cours/debuter-avec-kali-linux/ "Kali Linux"). Tetapi Anda dapat menggunakannya dengan cara yang sama persis dari Debian klasik, CentOS, Red Hat atau apa pun!

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

Jawaban di sini dengan jelas menunjukkan bahwa paket "nmap" ada di repositori (di sini, repositori [Kali Linux](https://www.it-connect.fr/cours-tutoriels/administration-systemes/linux/ "Linux")). Mulai sekarang, Anda dapat menginstal Nmap melalui perintah instalasi biasa, tidak ada yang membingungkan untuk saat ini 🙂 :

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

_hasil dari menampilkan versi Nmap saat ini._

Perhatikan keberadaan library "libpcap" (_Packet Capture Library_) dan versinya. Juga digunakan oleh Wireshark, "libpcap" digunakan oleh Nmap untuk membuat dan memanipulasi paket dan memantau lalu lintas jaringan.

### III Menginstalasi Nmap pada Windows

Untuk menginstal pada sistem operasi Windows, mulailah dengan mengunduh biner dari situs resminya (dan bukan yang lain!):

Halaman pengunduhan Nmap di situs web resmi: [https://nmap.org/download.html#windows](https://nmap.org/download.html#windows)

Anda kemudian perlu mengunduh file bernama `nmap-<VERSION>-setup.exe`:

![nmap-image](assets/fr/06.webp)

Halaman unduhan file instalasi nmap untuk Windows

Setelah Anda memiliki file ini di sistem Anda, cukup jalankan untuk menginstal Nmap. Ini adalah instalasi yang mudah, dan Anda bisa membiarkan semua opsi sebagai default.

Refleks saya adalah menghapus centang pada kotak "zenmap (GUI Frontend)". Ini adalah Interface grafis untuk Nmap yang tidak saya gunakan dan tidak akan dibahas dalam tutorial ini, tetapi silakan mencobanya setelah Anda menguasai command line pada Nmap!

![nmap-image](assets/fr/07.webp)

Pilihan opsional untuk membatalkan pemilihan Zenmap saat menginstal Nmap di Windows

Pada akhir instalasi Nmap, instalasi kedua diusulkan: instalasi library "Npcap":

- Ia dapat mengirim **ribuan atau bahkan jutaan paket** dalam waktu singkat, yang dapat memenuhi infrastruktur jaringan tertentu.
- Ini dapat generate **paket cacat atau non-standar**, yang cenderung mengganggu peralatan tertentu (terutama sistem industri).
- Hal ini dapat menghasilkan **perilaku seperti serangan**, yang dapat memicu peringatan pada sistem keamanan (firewall, IDS/IPS, dll.).

pemasangan library "Npcap" saat menginstal Nmap pada Windows

Ini adalah pustaka yang diandalkan Nmap untuk mengelola komunikasi jaringan, yaitu membangun, mengirim, dan menerima paket jaringan. Anda mungkin sudah pernah menemukan pustaka ini jika Anda menggunakan Wireshark di Windows, karena Wireshark juga menggunakannya dan memerlukan instalasi.



Seperti pada Linux, Anda dapat memvalidasi bahwa Nmap telah terinstal dengan membuka Command Prompt atau terminal [Powershell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/ "Powershell") dan mengetikkan perintah berikut:

Ini adalah library tempat Nmap mengandalkan untuk mengelola komunikasi jaringan, yaitu membangun, mengirim, dan menerima paket jaringan. Anda mungkin pernah menemukan library ini jika Anda menggunakan Wireshark di Windows, karena Wireshark juga menggunakannya dan memerlukan instalasi.

Seperti halnya Linux, Anda dapat memvalidasi bahwa Nmap terpasang dengan membuka Command Prompt atau terminal [Powershell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/ "Powershell") dan mengetik perintah berikut:

```
nmap --version
```

Inilah hasil yang diharapkan:

![nmap-image](assets/fr/09.webp)

_hasil dari menampilkan versi Nmap saat ini._

Nmap sekarang sudah terinstal pada Windows. Anda dapat menggunakannya dengan cara yang sama persis seperti pada Linux, dengan mengikuti tutorial ini.

### IV. Hak istimewa lokal yang diperlukan untuk menggunakan Nmap

Namun, saat menggunakan Nmap, **apakah perlu memiliki hak istimewa lokal yang lebih tinggi di sistem?** Jawabannya adalah: **tergantung**.

Dalam bentuknya yang sangat dasar, yaitu tanpa melangkah terlalu jauh dalam menggunakan opsi-opsinya, Nmap tidak selalu memerlukan hak istimewa. Namun, Anda akan segera menyadari bahwa lebih baik menggunakan Nmap dalam konteks istimewa ("root" di Linux, "administrator" atau yang setara di Windows) untuk dapat menggunakannya secara maksimal, dengan risiko mendapatkan pesan kesalahan seperti yang satu ini:

![nmap-image](assets/fr/10.webp)

_pesan kesalahan di Linux ketika opsi Nmap memerlukan hak root._

Baik pada Linux atau Windows, ada banyak kasus di mana Nmap akan meminta Anda untuk mendapatkan akses istimewa. Alasan utamanya adalah sebagai berikut (daftar tidak lengkap):

- **Membuat paket jaringan "mentah"**: Nmap mampu melakukan berbagai metode pemindaian, termasuk manipulasi dan pembuatan paket tingkat lanjut. Ini adalah kasus, misalnya, ketika kita ingin melakukan pemindaian TCP SYN, yang tidak seusai dengan Three-way handshake klasik dari pertukaran TCP. Untuk melakukan ini, Nmap perlu menggunakan fungsi selain yang asli dari sistem operasi, yang hanya tahu cara sercara aturan baku yang baik dalam komunikasi jaringan (Nmap memanggil library "Npcap" dan "libcap" yang terlihat di atas). Karena Nmap tidak melakukan hal-hal dengan cara yang "standar" itulah Nmap dapat menyimpulkan informasi tertentu tentang OS, layanan, dan kerentanan tertentu.
- **Memantau lalu lintas jaringan**: beberapa opsi Nmap mengharuskannya untuk memantau jaringan untuk mengambil informasi tertentu. Tindakan ini dianggap sensitif pada sistem operasi, karena juga memungkinkan Anda untuk memantau komunikasi aplikasi lain di sistem. Sama seperti Wireshark, Nmap membutuhkan hak istimewa khusus untuk melakukan ini, yang lebih mudah didapat dengan berada langsung dalam sesi istimewa.
- **Memantau pada port khusus**: pada sistem operasi, port dari 0 hingga 1024 (TCP maupun UDP) dikatakan istimewa, yaitu mereka entah bagaimana dicadangkan untuk penggunaan yang sangat spesifik dan karenanya dilindungi. Meskipun ini adalah alasan yang agak kuno saat ini, masih perlu untuk memiliki hak istimewa tertentu untuk memantau port ini, yang mungkin harus dilakukan Nmap tergantung pada bagaimana Nmap akan digunakan.
- **Mengirim paket UDP**: Demikian pula, memantau aplikasi jaringan pada port UDP (protokol stateless) memerlukan hak istimewa pada sistem operasi. Sesi istimewa karenanya akan diperlukan jika Anda ingin melakukan pemindaian UDP, di mana Nmap harus memantau respons untuk menganalisis balasan terhadap pemindaiannya.

Agar lebih tepat, dimungkinkan, setidaknya di Linux, untuk menjalankan Nmap dengan semua fungsi dan opsinya tanpa benar-benar menjadi root. Ini dicapai dengan memberikan capabilities yang tepat pada file. Namun, ini memerlukan manipulasi tingkat lanjut dan mungkin tidak sepraktis menjalankan Nmap secara langsung dengan hak istimewa. Juga, pendekatan ini kurang umum dan dapat menimbulkan masalah keamanan jika salah dikonfigurasi.

Namun, ini sedikit menyimpang dari tutorial Nmap kita, jadi kita akan mengabaikannya untuk saat ini.

Untuk sisa tutorial ini, asumsikan bahwa Nmap selalu dijalankan sebagai "root" (dari shell sebagai "root" atau melalui perintah "sudo"), atau di terminal administrator pada Windows, bahkan jika ini tidak ditunjukkan. Jika tidak, Anda mungkin mengalami perbedaan halus namun nyata dari tutorial.

### V. Kesimpulan

Selesai! Nmap sekarang terpasang di sistem operasi kita dan siap digunakan, tidak memerlukan konfigurasi lebih lanjut. Bagian ini mengakhiri pengantar dan presentasi Nmap. Saya harap ini telah membuat selera Anda tergugah, dan Anda bersemangat untuk mulai berlatih.

Secara lebih serius, kita sekarang memiliki gagasan yang lebih baik tentang apa itu aplikasi pemetaan Nmap dan apa penggunaan yang paling umum, serta keterbatasannya. Mari kita lanjutkan!

## 4 - Pemindaian port TCP dan UDP dengan Nmap

### I. Presentasi

Di bagian ini, kita akan belajar cara melakukan pemindaian port pertama kita menggunakan aplikasi pemindai jaringan Nmap. Kita akan melihat cara menggunakannya untuk menyusun daftar layanan jaringan yang terbuka pada sebuah host, baik menggunakan protokol TCP maupun UDP.

Mulai sekarang, ingatlah untuk hanya memindai host di lingkungan terkontrol yang telah Anda dapatkan otorisasi eksplisit untuknya.

Sebagai pengingat: [KUHP: Bab III: Serangan terhadap sistem pemrosesan data otomatis](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)

**Jika Anda tidak memilikinya**, saya merekomendasikan solusi gratis berikut, yang sangat cocok!

- **[Hack The Box](https://app.hackthebox.com/ "Hack The Box")**: Platform pelatihan hacking, Hack The Box terus-menerus menyediakan sistem yang rentan untuk Anda serang sesuka hati. Beberapa ratus sistem tersedia, tetapi hanya 20 perangkat yang diperbarui yang ditawarkan secara gratis sepanjang tahun, dengan akses melalui VPN OpenVPN.

- **[Vulnhub](https://www.vulnhub.com/ "Vulnhub")** : Platform ini menawarkan banyak sistem yang sengaja dibuat rentan untuk diunduh, yang dapat digunakan melalui VirtualBox (juga solusi gratis) atau cara lain. Setelah diunduh, tidak perlu VPN—semuanya bersifat lokal.

Selain itu, Anda bebas untuk **membuat virtual machines** pada sistem operasi favorit Anda dan memasang berbagai layanan di dalamnya sebagai target pengujian. Keuntungannya di sini adalah Anda juga akan dapat melihat apa yang terjadi di sisi server selama pemindaian, terutama dengan Wireshark, dan memiliki kendali atas firewall lokal saat kita melakukan uji yang lebih lanjut.

Mari kita mulai berlatih!

### II. Memindai port TCP host melalui Nmap



#### A. Pemindaian port TCP pertama dengan Nmap

Kita sekarang akan melakukan pemindaian pertama kita melalui Nmap. Tujuan kita di sini sederhana: kita ingin mencari tahu layanan apa yang terbuka oleh server web yang baru saja kita pasang, untuk melihat apakah ada sesuatu yang tidak terduga, seperti layanan administrasi yang seharusnya tidak dapat diakses, atau port yang terbuka dari aplikasi yang kita pikir sudah tidak berfungsi.

Dalam contoh saya, host yang akan dipindai memiliki IP Address "192.168.1.18":

```
nmap 192.168.1.18
```

Ini adalah hasil yang mungkin terjadi. Kami melihat Nmap klasik kembali dengan banyak informasi:

![nmap-image](assets/fr/11.webp)

_hasil pemindaian TCP sederhana yang dilakukan dengan Nmap._

Dengan melihat sekilas pada hasil ini, kita memahami bahwa port TCP/22 dan TCP/80 dapat diakses pada host ini.

Secara default, dan jika Anda tidak memerintahkannya, Nmap hanya akan memindai port TCP.

#### B. Memahami hasil pemindaian Nmap sederhana

Mari kita melangkah lebih jauh, bagaimanapun juga, untuk memahami hasil ini: setiap baris itu penting, pertama untuk mengetahui apa yang baru saja dilakukan, dan kedua untuk menafsirkan hasil pemindaian dengan benar.

Baris pertama pada dasarnya adalah pengingat versi pemindaian dan tanggal (Berguna untuk pencatatan dan pengarsipan!):

```
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-29 21:59 CEST
```

Baris kedua menunjukkan dimulainya hasil pemindaian untuk host "debian.home (192.168.1.19)". Informasi ini akan berguna ketika kita mulai memindai beberapa host pada saat bersamaan:

```
Nmap scan report for debian.home (192.168.1.19)
```

Baris ketiga memberi tahu kita bahwa host yang dimaksud "Up", yaitu aktif:

```
Host is up (0.00022s latency).
```

Terakhir, Nmap memberi tahu kita bahwa 998 port TCP yang diidentifikasi sebagai port tertutup tidak ditampilkan dalam hasil:

```
Not shown: 998 closed tcp ports (conn-refused)
```

Hal ini menghemat hampir 1.000 baris output yang terlihat seperti :

```
1/tcp closed
2/tcp closed
3/tcp closed
…
```

Terima kasih untuk ini yang telah menyelamatkan kami dari hal ini!

Mengapa 998 port "tertutup / closed"? dan ditambah 2 port yang terbuka menjadikan 1000, dan itu adalah jumlah port yang akan dipindai Nmap dalam konfigurasi default-nya, bukan 65.535 port TCP yang ada! Kita akan melihat nanti bahwa ini sepenuhnya dan mudah disesuaikan. Tetapi jika host yang ditargetkan memiliki layanan yang berkomunikasi pada port yang agak unik, pemindaian "default" ini tidak akan menemukannya.

Setelah informasi ini, kita menemukan apa yang paling menarik: sebuah tabel yang diatur sesuai dengan tiga kolom "PORT - STATE - SERVICE":

- Kolom "PORT" yang pertama menunjukkan port/protokol yang ditargetkan, dan di sini penting untuk melihat apakah itu port TCP (`<port>/tcp`) atau UDP (`<port>/udp`).
- Kolom "STATE" menunjukkan status layanan jaringan yang ditemukan pada port ini dan ditentukan oleh Nmap berdasarkan respons yang diperoleh. Status ini dapat berupa "terbuka / open", "tertutup / closed", "difilter / filtered", atau "tidak diketahui / unknown". Kita akan melihat nanti bagaimana Nmap membedakan antara status yang berbeda ini.
- Kolom "SERVICE" menunjukkan layanan yang terbuka pada port yang dimaksud. Namun, harap dicatat, bahwa kita belum menggunakan opsi penemuan layanan aktif di sini. Nmap mengandalkan referensi lokal antara port/protokol dan layanan yang seharusnya ditetapkan: file "/etc/services"

Jika Anda melihat file "/etc/services" pada sistem Linux, Anda akan menemukan tautan "port/protocol - service" yang mirip dengan yang ditampilkan oleh Nmap :

![nmap-image](assets/fr/12.webp)

_mengekstrak isi file "/etc/services" pada Linux._

Penting untuk dipahami bahwa, untuk saat ini, Nmap belum melakukan penemuan layanan aktif. Misalnya, Nmap tidak akan mampu mengidentifikasi layanan SSH di balik port TCP/80 jika ini yang terjadi. Oleh karena itu, penting untuk mengetahui cara menggunakan opsi yang tepat—ini akan segera hadir!

Mengetahui cara menginterpretasikan keluaran Nmap adalah bagian penting dari menguasai aplikasi ini. Kabar baiknya adalah bahwa keluaran ini sebagian besar akan sama, apa pun opsi yang Anda gunakan.

#### C. Di balik layar: analisis jaringan melalui Wireshark

Jika Anda melihat lebih dekat apa yang terjadi pada Interface jaringan dari host yang memindai server, atau pada server itu sendiri, tindakan Nmap akan jauh lebih jelas. Itulah yang akan kita lakukan di sini.

Apa yang dapat saya tunjukkan di sini hanyalah bagian dari apa yang terlihat di Wireshark. Jika Anda ingin melangkah lebih jauh, silakan lakukan Pengambilan data jaringan sendiri selama pemindaian, dan kemudian jelajahi apa yang telah ditangkap.

Dalam pengujian ini, host pemindaian saya (192.168.1.18) dan host target saya (192.168.1.19) berada di jaringan lokal yang sama.

Nmap mulai dengan mencari tahu apakah host target aktif di jaringan lokal dengan mengirimkan permintaan ARP. Jika Nmap menerima respons, Nmap tahu bahwa host itu aktif dan memulai pemindaian jaringannya:

![nmap-image](assets/fr/13.webp)

_permintaan ARP yang dikeluarkan oleh Nmap untuk menentukan apakah host target ada di jaringan lokal_

Jika host yang akan dipindai berada di jaringan jarak jauh, Nmap memulai dengan mengirimkan permintaan ping dan mencoba menjangkau beberapa port yang paling sering diekspos (TCP/80, TCP/443):

![nmap-image](assets/fr/14.webp)

_permintaan ping yang dikeluarkan oleh Nmap untuk menentukan apakah host target dapat dijangkau di jaringan jarak jauh_

Jika mendapatkan respons terhadap salah satu dari tes ini, Nmap menganggap target tersebut aktif.

Setelah Nmap menentukan bahwa targetnya aktif, Nmap akan mencoba menyelesaikan nama domain dengan server DNS yang dikonfigurasi pada kartu jaringan:

![nmap-image](assets/fr/15.webp)

_resolusi dNS pada target pemindaian Nmap_

Setelah Nmap mengidentifikasi targetnya dan mengetahui bahwa target tersebut aktif, Nmap memulai pemindaian port TCP:

![nmap-image](assets/fr/16.webp)

_transmisi paket TCP SYN dan penerimaan RST/ACK selama pemindaian Nmap_

Untuk melakukan ini, pada setiap port TCP dalam rentang bawaannya, **mengirimkan paket TCP SYN dan menunggu respons.** Pada tangkapan layar di atas, Nmap menerima paket TCP RST/ACK dari server yang dipindai, yang berarti "lanjutkan saja, tidak ada yang perlu dilihat di sini"—dengan kata lain, port-port ini tertutup. Seperti yang kita lihat dalam hasilnya, ini akan menjadi kasus untuk sebagian besar port yang dipindai. Dengan dua pengecualian:

![nmap-image](assets/fr/17.webp)

_respons terhadap paket TCP SYN yang dikirim pada port 22, aktif pada target pemindaian_

Pada tangkapan layar di atas, kita melihat paket TCP SYN/ACK yang dikirim oleh host target. Port itu aktif dan membuka sebuah layanan. Nmap mengakui penerimaan respons, lalu mengakhiri koneksi (TCP RST/ACK). Inilah cara Nmap tahu bahwa port TCP/22 aktif.

Kita telah melihat di sini bahwa Nmap mematuhi "Three Way Handshake" saat memindai jaringan TCP. Karena alasan kinerja, dimungkinkan untuk memintanya untuk tidak merespons pengembalian server, sehingga menghemat beberapa ribu paket saat memindai jaringan yang besar. Tetapi kita akan melihat opsi dan optimasi ini nanti di tutorial.

Kita sekarang memiliki gambaran yang lebih baik tentang cara melakukan pemindaian TCP dan apa yang sebenarnya terjadi saat itu dilakukan. Kita juga telah melihat bahwa, secara default, Nmap melakukan pemindaian port TCP pada sejumlah port yang terbatas.

### III. Memindai port UDP dengan Nmap

#### A. Pemindaian port UDP pertama dengan Nmap

Sekarang mari kita lihat cara memindai port UDP sebuah host. Seperti yang telah kita lihat, secara default Nmap akan selalu memindai port TCP. Ini bisa berarti kehilangan banyak informasi jika kita tidak menyadarinya.

Sebagai pengingat, untuk tujuan pengujian ini, host pemindaian saya (192.168.1.18) dan host target saya (192.168.1.19) berada di jaringan lokal yang sama.

```
nmap -sU 192.168.1.19
```

Di sini, hasil yang diperoleh memiliki format yang sama dengan pemindaian TCP, tetapi layanan aktif yang ditampilkan berada di `<port>/UDP`, seperti yang diminta!

![nmap-image](assets/fr/18.webp)

_hasil pemindaian UDP sederhana yang dilakukan dengan Nmap._

Opsi "-sU" digunakan untuk memberi tahu Nmap bahwa Anda ingin bekerja pada UDP, dan bukannya TCP seperti standarnya.

Ngomong-ngomong, Anda mungkin akan menyadari bahwa Nmap memerlukan hak "root" untuk pemindaian UDP, seperti yang disebutkan sebelumnya dalam tutorial ini.

**catatan:** Sejak versi terbaru Nmap, selalu disarankan untuk menjalankan pemindaian UDP dengan hak administrator untuk memastikan hasil yang andal, karena beberapa fitur memerlukan raw access ke soket jaringan

Pemindaian UDP bisa memakan waktu yang sangat lama (1100 detik untuk memindai 1000 port dalam contoh saya), karena tidak adanya "Three Way Handshake" di UDP, yang berarti Nmap akan menunggu balasan untuk setiap paket UDP yang dikirim, dan akan menentukan port sebagai "closed" hanya jika tidak ada balasan setelah waktu tertentu (timeout). Respons dari host yang dipindai ini tidak sistematis dan sering kali dibatasi dalam hal jumlah respons per detik, untuk menghindari serangan amplifikasi tertentu. Ini berbeda dengan TCP, di mana ada respons segera dari host yang dipindai, baik port itu terbuka maupun tertutup. Kita akan melihat nanti cara mengoptimalkannya.

Kesulitan kedua dengan UDP adalah **bahwa layanan tidak selalu merespons paket masuk**, hanya karena ini tidak selalu diperlukan dan itu adalah prinsip dari UDP. Ketika ini terjadi, dan tidak ada ICMP "port unreachable" yang diterima, layanan ditandai sebagai "open|filtered" oleh Nmap, seperti yang ditunjukkan pada tangkapan layar di atas.

#### B. Di balik layar: analisis jaringan melalui Wireshark

Seperti halnya pemindaian TCP kita, mari kita lihat lebih dekat apa yang terjadi di tingkat jaringan selama pemindaian UDP menggunakan analisis Wireshark. Perilaku Nmap dalam menentukan apakah sebuah host aktif adalah sama.

Satu-satunya perbedaan nyata saat memindai UDP adalah bahwa Nmap tidak akan menunggu "Three Way Handshake", karena mekanisme ini tidak ada di UDP (protokol stateless):


![nmap-image](assets/fr/19.webp)

_transmisi paket uDP dan penerimaan ICMP (port tidak dapat dijangkau) selama pemindaian Nmap_

Kita dapat melihat pada tangkapan layar di atas bahwa Nmap akan mengirimkan sejumlah besar paket UDP, dan menerima untuk sebagian besar dari mereka paket ICMP "Destination unreachable (Port unreachable)" sebagai respons. Ini normal, karena itu adalah respons yang sesuai yang didefinisikan oleh [RFC 1122](https://www.freesoft.org/CIE/RFC/1122/41.htm "RFC 1122") ketika port UDP tidak dapat dijangkau:

![nmap-image](assets/fr/20.webp)

_ekstrak dari RFC 1122._

Mari kita cermati lebih dekat tangkapan Wireshark ini, yang menunjukkan **tiga skenario yang mungkin terjadi** dalam UDP :

![nmap-image](assets/fr/21.webp)

_Pengambilan data jaringan selama pemindaian UDP pada port yang berbeda dengan Nmap._

Ketiga kasus tersebut adalah sebagai berikut:

- Pertukaran pertama terdiri dari paket nomor 3, 4, dan 8, 9. Nmap mengirimkan paket UDP pada port SNMP klasik dan karena itu **membuat paket yang sesuai dengan protokol sebelumnya**. Nmap kemudian mendapatkan respons dari server (paket nomor 8 dan 9). Hasil: Nmap telah menerima respons, layanan "open".
- Pertukaran kedua terdiri dari paket 6 dan 7. Nmap mengirimkan paket UDP "kosong" (tanpa struktur protokol) ke port UDP/165, dan menerima paket ICMP sebagai balasan: "Destination unreachable (Port unreachable)". Hasil: Nmap telah menerima respons (negatif), host telah aktif, tetapi layanan yang coba dijangkaunya tidak operasional di port ini, yang akan ditandai sebagai "closed".
- Pertukaran terakhir terdiri dari paket nomor 12: Nmap mengirimkan paket UDP "kosong" ke port UDP/1235. Tidak ada respons, bahkan tidak ada penolakan eksplisit dari host yang dipindai. Hasil: Nmap menandai port sebagai "open|filtered", karena tidak dapat mengatakan apakah ini karena keberadaan firewall, yang dikonfigurasi untuk tidak merespons, atau karena layanan UDP yang aktif yang tidak memberikan respons apa pun (tidak wajib di UDP).

Berikut adalah hasil yang ditampilkan oleh Nmap setelah ketiga kasus ini:

![nmap-image](assets/fr/22.webp)

_kemungkinan hasil pemindaian UDP yang dilakukan melalui Nmap._

Kita sekarang memiliki gambaran yang lebih baik tentang cara melakukan pemindaian UDP dan apa yang sebenarnya terjadi saat itu dilakukan. Sejauh ini kita hanya menggunakan Nmap dengan cara yang sangat sederhana, tanpa benar-benar memutuskan port mana yang akan dipindai, tetapi itu akan segera berubah!

### IV. Menyempurnakan pemindaian port dengan Nmap

#### A. Pengingat perilaku default Nmap

Seperti yang kita ketahui, secara bawaan Nmap akan memilih sendiri jumlah dan port yang akan dipindai jika Anda tidak menentukan opsi apa pun. Konfigurasi "default" ini dirancang untuk memberikan gambaran tentang port utama yang terbuka, yang dipilih berdasarkan frekuensi kemunculannya (umum atau sering muncul) daripada berdasarkan urutan numerik (seperti port 1, 2, 3, dan seterusnya). Hal ini juga untuk menghindari dimulainya pemindaian 65.535 port yang akan memakan waktu terlalu lama.

**Bagaimana Port Ini Dipilih?**

1.000 port yang dipindai dalam mode bawaan dipilih berdasarkan frekuensi kemunculannya. Statistik ini dikelola dan diperbarui oleh Nmap bersamaan dengan file dan skrip (modul). Anda dapat melihat statistik ini sendiri di berkas /usr/shares/nmap/nmap-services.

![nmap-image](assets/fr/23.webp)

_diekstrak dari file "/usr/shares/nmap/nmap-services"._

Di kolom ketiga, kita melihat nilai yang terlihat seperti probabilitas (antara 0 dan 1) atau distribusi persentase. Ini adalah frekuensi kemunculan dari setiap pasangan port/protokol. Kita dapat melihat bahwa port-port yang paling dikenal (FTP, SSH, TELNET, dan SMTP pada kutipan ini) memiliki nilai yang jauh lebih tinggi daripada yang lain.

#### B. Menentukan port target dengan tepat untuk pemindaian Nmap

Namun, di dunia nyata, kita mungkin hanya perlu memindai port tertentu, atau beberapa port, atau rentang port tertentu. Nmap memudahkan untuk melakukan hal tersebut, dengan cara yang seragam untuk pemindaian UDP dan TCP.

**Memindai port tertentu melalui Nmap**

Jika kita ingin memindai satu port, dan bukan 1000, kita dapat menentukan port ini melalui opsi "-p" atau "--port" pada Nmap:

```
# Scan 1 TCP port dengan Nmap
nmap 192.168.1.19 -p 80

# Scan 1 UDP port dengan Nmap
nmap -sU 192.168.1.19 -p 161
```

Hasilnya, pemindaian secara alami akan jauh lebih cepat dan Nmap hanya akan mengirimkan paket yang diperlukan untuk mendeteksi apakah host aktif, dan kemudian apakah port yang ditentukan dapat dijangkau. Hal ini menghemat waktu jika Anda hanya ingin menjalankan tes cepat untuk melihat apakah layanan web pada situs tersebut Anda masih aktif.

**Pindai beberapa port melalui Nmap**

Jawaban di sini dengan jelas menunjukkan bahwa paket "nmap" ada di repositori (di sini, repositori Kali [Linux](https://www.it-connect.fr/cours-tutoriels/administration-systemes/linux/ "Linux")). Mulai sekarang, Anda dapat menginstal Nmap melalui perintah instalasi biasa, tidak ada yang dilucuti untuk saat ini 🙂:

```

# Scan beberapa TCP port dengan Nmap
nmap 192.168.1.19 -p 80,10999,22,23,1345

# Scan beberapa UDP port dengan Nmap
nmap -sU 192.168.1.19 -p 161,23,69

```

Terlepas dari urutannya, Nmap akan memeriksa semua port ini, dan hanya port yang ada pada host yang ditargetkan. Anda akan melihat pada keluaran Nmap bahwa ia **secara eksplisit memberi tahu kita semua port dan statusnya**, bahkan jika port tersebut "tertutup / tertutup". Tidak seperti perilaku default, di mana keluaran lengkap ini akan memakan terlalu banyak ruang:

![nmap-image](assets/fr/24.webp)

*Hasil pemindaian TCP Nmap pada port yang ditunjukkan.*

**Memindai berbagai port**

Jika jumlah port yang ingin Anda pindai terlalu banyak, Anda dapat menentukannya berdasarkan rentang, misalnya :

```

# Scan TCP port dari 1000 ke 2000 dengan Nmap
nmap 192.168.1.19 -p 1000-2000

# Scan UDP port dari 1000 ke 2000 dengan Nmap
nmap -sU 192.168.1.19 -p 100-150

```

Tentu saja, Anda bisa memadupadankan dan mencocokkan sesuai keinginan Anda, misalnya:

```

# Scan TCP port nomer 22,80, 3389 dan dari 1000 ke 2000 dengan Nmap
nmap 192.168.1.19 -p 22,80,1000-2000,3389

```

**Pemindaian port TCP dan UDP**

Anda juga dapat melakukan pemindaian UDP dan TCP secara bersamaan, pada port yang dipilih:

```

# Scan 1000 port default, in TCP and UDP
sudo nmap 192.168.1.19 -sT -sU

# Scan hanya UDP/161 and TCP/22
sudo nmap 192.168.1.19 -sT -sU -p U:161,T:22

```

Anda akan melihat pada contoh terakhir ini, adanya "U:" untuk mengindikasikan port UDP dan "T:" untuk mengindikasikan port TCP. Berikut ini adalah kemungkinan output dari jenis pemindaian ini:

![nmap-image](assets/fr/25.webp)

*Hasil pemindaian port TCP dan UDP dengan Nmap.*

Nah, itu cara yang menarik untuk menyesuaikan pemindaian Anda!

**Pindai semua port**

Terakhir, Anda dapat menentukan rentang yang jauh lebih besar atau lebih kecil pada Nmap. Kita telah melihat bahwa daftar default yang dipilih oleh Nmap berisi 1000 port. Kita juga dapat meminta 100 port yang paling sering digunakan, atau 200 port yang paling sering digunakan, dengan menggunakan opsi "--top-ports":

```

# Scan top 100 port yang paling sering dipakai dengan Nmap
nmap 192.168.1.19 --top-ports 100

# Scan top 200 port yang paling sering dipakai dengan Nmap
nmap 192.168.1.19 --top-ports 200

```

Terakhir, kita bisa memintanya untuk memindai semua port yang memungkinkan (semua 65535), dengan menggunakan notasi "-p-":

```

# Scan semua TCP ports dari 1 ke 65535 dengan Nmap
nmap 192.168.1.19 -p-

```

Yang terakhir ini akan memakan waktu lebih lama, terutama dengan UDP, tetapi Anda pasti tidak akan melewatkan port yang terbuka.

*Catatan: Opsi "-p-" adalah metode yang direkomendasikan untuk memindai semua port TCP. Untuk pemindaian UDP, disarankan untuk membatasi jumlah port demi alasan performa, karena pemindaian lengkap semua port UDP dapat memakan waktu yang sangat lama.*

Nanti dalam tutorial ini, kita akan melihat cara mengoptimalkan kecepatan pemindaian Nmap agar sesuai dengan kebutuhan kita, yang akan sangat berguna untuk pemindaian pada semua port TCP dan UDP.

### V. Kesimpulan

Pada bagian ini, kita akhirnya melakukan praktik langsung, sehingga sekarang kita tahu **cara menggunakan Nmap secara dasar untuk memindai port TCP dan UDP sebuah host**. Kita juga telah melihat secara rinci apa yang terjadi di tingkat jaringan dan **bagaimana Nmap menentukan apakah sebuah port TCP atau UDP aktif atau tidak**. Terakhir, kita tahu cara memilih port yang ingin kita pindai secara terperinci dan **apa yang sebenarnya dilakukan oleh opsi default Nmap**. Pada bagian selanjutnya, kita akan menggunakan kembali pengetahuan ini dan menerapkannya untuk memindai seluruh jaringan, termasuk pemetaan global dan penemuan jaringan.

## 5 - Pemetaan dan penemuan jaringan dengan Nmap

### I. Presentasi

Di bagian ini, kita akan belajar cara menggunakan aplikasi pemindai jaringan Nmap untuk memetakan jaringan Anda. Kita akan melihat seberapa efektif aplikasi ini dalam tugas ini, melalui berbagai opsinya. Terakhir, kita akan melihat cara yang berbeda untuk menentukan target pemindaian kita kepada Nmap.

Secara khusus, kita akan menggunakan apa yang kita pelajari di bagian sebelumnya tentang bagaimana Nmap menentukan apakah sebuah host aktif dan dapat dijangkau. Seperti yang disebutkan dalam pengantar Nmap, ini adalah Network Mapper. Dengan demikian, ini adalah aplikasi yang sempurna untuk menyusun daftar host yang dapat diakses di jaringan, baik lokal maupun jarak jauh.

**Feedback penulis:**


Faktanya, sebagai auditor keamanan siber dan pentester, saya menggunakan Nmap secara sistematis saat melakukan pengujian penetrasi internal untuk mencari tahu di mana saya berada, siapa tetangga saya di jaringan lokal, dan jaringan lain apa yang dapat diakses, serta sistem yang berada di dalamnya. Tujuan saya sederhana: memetakan jaringan, menentukan ukuran sistem informasi dan, khususnya, memetakan celah serangannya.

Pemetaan jaringan juga dapat berguna dalam konteks diagnostik jaringan, pengawasan, pemetaan aset (apakah Anda benar-benar yakin bahwa IS Anda hanya terdiri dari apa yang ada di Active Directory atau di GLPI/OCS Inventory Anda?). Ini juga dapat digunakan untuk mendeteksi keberadaan Shadow IT di sistem informasi Anda.

### II. Menggunakan Nmap untuk memindai rentang jaringan

#### A. Menemukan jaringan dengan pemindaian Nmap

Sekarang kita ingin meningkatkan kemampuan dan menganalisis seluruh jaringan lokal kita. Tidak ada yang lebih sederhana: yang perlu kita lakukan adalah menggunakan kembali perintah yang kita lihat di bagian sebelumnya, tetapi tentukan CIDR dan bukannya IP Address yang sederhana.

CIDR (**Classless Inter Domain Routing**) adalah notasi "klasik" untuk menentukan jangkauan jaringan dan luasnya (menggunakan mask). Sebagai contoh, "192.168.0.0/24" adalah "terjemahan" dari notasi mask desimal "255.255.255.0".

Untuk menggunakan Nmap dengan menentukan CIDR, kita dapat menggunakannya sebagai berikut:

```
# Scan CIDR
nmap 192.168.0.0/24
```

Hal ini juga memungkinkan, seperti halnya dengan port pada bagian sebelumnya, untuk menentukan beberapa host, beberapa jaringan, atau jangkauan :

```
# Scan beberapa jaringan sekaligus melalui CIDR mereka
nmap 192.168.0.0/24 192.168.1.0/24

# Scan beberapa host melalui IP mereka
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20

# Kombinasi keduanya
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20
```

Berikut ini contoh hasil yang mungkin kita dapatkan ketika menjalankan pemindaian pada jaringan:

![nmap-image](assets/fr/26.webp)

_hasil pemindaian Nmap untuk memetakan beberapa jaringan_

Secara khusus, kita melihat beberapa host yang aktif, dan setiap bagian host dimulai dengan baris seperti ini:

```
Nmap scan report for <name> (<IP>)
```

Hal ini memungkinkan kita untuk melihat dengan jelas host mana yang dirujuk oleh hasil berikut. Baris terakhir juga penting:

```
Nmap done: 512 IP addresses (5 hosts up) scanned in 21.43 seconds
```

Kita tahu bahwa, pada jaringan yang dipindai, Nmap menemukan 5 host aktif.

#### B. Di balik tenda: analisis jaringan melalui Wireshark

Kita sekarang akan melihat lebih dekat apa yang terjadi di tingkat jaringan selama penemuan jaringan yang dilakukan melalui Nmap.

Seperti yang kita lihat di bagian sebelumnya, secara default Nmap akan menggunakan protokol ARP untuk mendeteksi keberadaan host di jaringan lokal:

![nmap-image](assets/fr/27.webp)

_paket aRP yang ditangkap saat memindai jaringan lokal menggunakan Nmap dan opsi defaultnya_

Dengan demikian, Nmap mampu mendeteksi hampir semua host di jaringan lokal, karena respons terhadap permintaan ARP umumnya disediakan oleh semua host yang aktif di jaringan dan sama sekali tidak tampak mencurigakan.

Untuk jaringan jarak jauh, Nmap menggunakan kombinasi teknik:

![nmap-image](assets/fr/28.webp)

_paket iCMP dan TCP yang ditangkap saat memindai jaringan jarak jauh menggunakan Nmap dan opsi standarnya_

Lebih tepatnya, Nmap menggunakan paket ICMP echo (kasus klasik dari ping) dan paket ICMP Timestamp, yang biasanya digunakan untuk menghitung waktu transit paket. Nmap berharap mendapatkan respons dari host di jaringan jarak jauh.

Namun, ada lebih dari itu. Anda dapat melihat pada tangkapan Wireshark di atas bahwa paket **TCP SYN** secara sistematis dikirim pada port TCP/443 dari setiap host potensial di jaringan yang akan dipindai, serta paket **TCP ACK** pada port TCP/80.

**Mengapa mengirim paket TCP ke port sebagai bagian dari penemuan jaringan?**

- **Mengirim paket SYN**: Mengirim paket SYN ke port tertentu memungkinkan Nmap untuk **menentukan apakah suatu layanan mendengarkan pada port tersebut**. Jika sebuah host membalas paket SYN dengan paket SYN/ACK, ini menunjukkan bahwa host tersebut aktif dan bahwa sebuah layanan mendengarkan pada port itu. Oleh karena itu, Nmap mencoba peruntungannya pada layanan ini, **bahkan jika tidak ada respons terhadap ping yang diperoleh**.
- **Mengirim paket ACK**: Mengirim paket ACK ke port tertentu memungkinkan Nmap untuk **menentukan apakah sebuah firewall hadir pada host tersebut**. Jika sebuah host merespons paket ACK dengan paket RST (Reset), ini menunjukkan bahwa sebuah firewall mungkin hadir pada host tersebut dan memblokir lalu lintas yang tidak diminta. Host tersebut dengan demikian menutupi kehadirannya di jaringan, bahkan jika host tersebut tidak merespons permintaan lain.

Namun, penting untuk dicatat bahwa deteksi firewall menggunakan teknik ini mungkin tidak sepenuhnya andal dalam semua kasus. Beberapa host dapat menghasilkan respons RST karena alasan selain keberadaan firewall, seperti konfigurasi layanan atau sistem operasi tertentu. Selain itu, firewall modern dapat dikonfigurasi untuk tidak merespons upaya penemuan jenis ini.

Kita sekarang telah melangkah jauh dan dapat melakukan penemuan jaringan dasar. Kita sekarang akan melihat beberapa opsi lagi yang akan memberi kita kendali yang lebih besar atas perilaku Nmap.

### III. Penemuan jaringan tanpa pemindaian port dengan Nmap

Seperti yang mungkin telah Anda perhatikan, secara default Nmap **melakukan pemindaian port setelah menemukan host yang aktif**. Hal ini menambahkan sejumlah besar paket dan waktu tunggu respons terhadap pemindaian kita. Jika Anda memiliki 5 host di jaringan Anda, Nmap akan mencoba memeriksa status sekitar 5.000 port, yang akan memakan waktu lebih lama.

Namun, dimungkinkan untuk menggunakan opsi Nmap untuk melakukan **hanya penemuan host aktif** di jaringan, tanpa menemukan layanannya.

Jika kita hanya ingin tahu host mana yang dapat dijangkau, tanpa informasi apa pun tentang layanan dan port yang mereka buka, maka kita dapat menggunakan opsi "-sn" untuk melakukan **hanya pemindaian menggunakan ICMP Echo (ping) dan permintaan ARP**. Dengan kata lain, menonaktifkan pemindaian port sama sekali:

```
# Scan sebuah CIDR di Echo ICMP
nmap 192.168.1.0/24 -sn
```

Berikut ini adalah hasil penemuan jaringan Nmap yang dilakukan tanpa pemindaian port:

![nmap-image](assets/fr/29.webp)

_Hasil penemuan jaringan tanpa pemindaian port dengan Nmap._

Kita telah menyebutkan kemungkinan keterbatasan menggunakan ICMP saja untuk penemuan host (untuk jaringan jarak jauh). Itulah mengapa Nmap juga menggunakan beberapa trik yang dapat menunjukkan keberadaan firewall atau layanan tertentu pada host. Dengan bantuan opsi, kita dapat menggunakan kembali trik ini dan bahkan memperluasnya, tanpa harus memulai lagi dengan pemindaian port lengkap dari setiap host yang ditemukan.

Untuk melakukan ini, kita akan menggunakan opsi "-PS" (TCP SYN) dan "-PA" (TCP ACK), yang akan memungkinkan kita untuk menentukan port yang ingin kita gabungkan sebagai bagian dari penemuan host kita, serta opsi "-PP":

```
# Scan port tertentu pada sebuah CIDR
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24
```

Pemindaian ini sudah memastikan bahwa penemuan host sedikit lebih lengkap dibandingkan dengan opsi default.

Kita mulai mendapatkan perintah yang cukup komprehensif, menggunakan beberapa opsi. Hal ini karena kita mengetahui cara kerja Nmap dan keterbatasan opsi "default"-nya, yang terkadang dapat membuat kita membuang-buang waktu atau melewatkan Elements yang penting. Itulah gunanya meluangkan waktu untuk menguasainya!

Berikut adalah rincian opsi dari perintah terakhir kita:

- "`-sn`: menonaktifkan pemindaian port untuk setiap host aktif yang ditemukan oleh Nmap.
- "`-PP` : mengaktifkan ICMP echo (ping scan) untuk penemuan host.
- "`-PS <PORT>`": mengirim paket TCP SYN pada port yang ditunjukkan untuk mendeteksi layanan aktif apa pun yang menunjukkan keberadaan host yang tidak merespons ping.
- "`-PA <PORT>`": mengirim paket TCP ACK pada port yang ditunjukkan untuk mendeteksi firewall aktif yang menunjukkan adanya host yang tidak merespons ping.


Pada contoh di atas, saya menentukan port yang saya anggap paling sering diekspos dalam konteks Nmap saya untuk opsi "-PS". Port yang berbeda ini kemudian akan diuji pada setiap host, bukan untuk melihat apakah layanan yang mereka host benar-benar aktif, tetapi untuk melihat apakah ini memungkinkan kita untuk menemukan host yang belum merespons ICMP Echo kita saat masih aktif (melalui respons dari layanan atau firewall host).

Dalam contoh di atas, saya menentukan port yang saya anggap paling sering diekspos dalam konteks Nmap saya untuk opsi "-PS". Port yang berbeda ini kemudian akan diuji pada setiap host, bukan untuk melihat apakah layanan yang mereka host benar-benar aktif, tetapi untuk melihat apakah ini memungkinkan kita untuk menemukan host yang belum merespons ICMP Echo kita tetapi masih aktif (melalui respons dari layanan atau firewall host).

Berikut adalah apa yang dapat dilihat dalam tangkapan jaringan yang diambil pada saat pemindaian seperti itu, dalam hal ini kutipan pada satu host target:

![nmap-image](assets/fr/30.webp)

_paket yang dikirim oleh Nmap selama penemuan jaringan tingkat lanjut, tanpa pemindaian port_

Kita menemukan paket TCP SYN, TCP ACK kita pada port TCP/80 dan ICMP echo kita. Nmap akan melakukan semua uji ini untuk setiap host yang ditargetkan oleh pemindaian penemuan jaringan kita.

### IV. Menggunakan file aset untuk ditargetkan dengan Nmap

Menentukan target dapat dengan cepat terbukti rumit dalam sistem informasi di kehidupan nyata, yang terkadang dapat terdiri dari lusinan atau ratusan jaringan, subnet, dan VLAN. Inilah sebabnya mengapa lebih mudah menggunakan file sebagai sumber untuk Nmap daripada menentukannya satu per satu pada baris perintah.

Untuk memulai, buatlah file sederhana yang berisi satu entri per baris:

Terakhir, Nmap memberi tahu kita bahwa 998 port TCP yang diidentifikasi sebagai port yang ditutup tidak ditampilkan dalam file:

_yang berisi satu target (host atau jaringan) per baris_

Selanjutnya, kita dapat menggunakan semua opsi Nmap yang terlihat sejauh ini dan menentukan opsi "-iL <path/file>":

```
# Scan daftar target yang terkandung dalam sebuah file
nmap -iL /tmp/mesCibles.txt
```

Nmap kemudian akan menyertakan dalam pemindaiannya semua target yang ada di file kita.

Jika Anda ingin memastikan bahwa semua target Anda akan diperhitungkan, Anda dapat menggunakan opsi "-sL -n". Nmap kemudian hanya akan menafsirkan CIDR dan host dalam file dan menampilkannya kepada Anda, tanpa mengirimkan paket apa pun melalui jaringan:

```
# Menampilkan target yang terkandung dalam sebuah file
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

_Hal ini memastikan bahwa daftar host yang akan dipindai akurat._

Satu tips penting terakhir yang ingin saya bagikan kepada Anda berkaitan dengan pengecualian host atau jaringan sebagai bagian dari pemindaian. Kebutuhan untuk mengecualikan host mungkin diperlukan dalam sejumlah kasus, terutama jika kita ingin memastikan bahwa **komponen sensitif dari sistem informasi tidak terganggu atau terganggu oleh pemindaian kita**.

Contoh yang sering terjadi dari kebutuhan semacam itu adalah ketika sebuah perusahaan memiliki peralatan industri (PLC) atau perawatan kesehatan. Peralatan semacam itu terkadang dirancang dengan buruk, dan sama sekali tidak dimaksudkan untuk menerima paket yang diformat dengan buruk, atau terlalu banyak darinya. Karena alasan ketersediaan atau risiko bisnis/manusia yang jelas, lebih baik mengecualikannya dari pengujian.

Untuk mengecualikan alamat IP atau jaringan dari pemindaian, kita dapat menggunakan opsi "--exclude" dari Nmap, misalnya :

```
# Mengecualikan alamat IP dalam pemindaian CIDR
nmap 192.168.1.0/24 --exclude 192.168.1.140
```

Dalam contoh ini, saya memindai jaringan "192.168.1.0/24" tetapi tidak termasuk host "192.168.1.140" yang terletak di sana. Tidak ada paket yang akan dikirim oleh Nmap ke host ini. Contoh lain dengan pengecualian subnet:

```
# Mengecualikan subnet dalam pemindaian CIDR
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```

Demikian pula, saya memindai jaringan besar "10.0.0.0/16", tetapi jaringan "10.0.100.0/24" tidak akan dipindai. Sekali lagi, saya sarankan untuk menggunakan opsi "-sL -n" untuk mendapatkan tampilan yang sangat jelas tentang host mana yang akan dipindai dan mana yang akan dikecualikan dari pemindaian, terutama jika Anda beroperasi dalam konteks yang sensitif.

### V. Penemuan jaringan dan pemindaian port

Kita sekarang dapat menggabungkan apa yang telah kita pelajari di bagian ini dengan apa yang kita pelajari di bagian sebelumnya tentang opsi pemindaian port. Secara default, kita telah melihat bahwa Nmap akan memindai 1.000 port paling sering digunakan pada setiap host aktif yang ditemukannya. Kita telah melihat cara untuk mencegah perilaku ini jika kita tidak menginginkannya, tetapi kita dapat mengendalikannya sepenuhnya, dan bahkan mengembangkannya sesuai kebutuhan kita.

Sebagai contoh, perintah berikut akan memeriksa keberadaan layanan yang mendengarkan pada port TCP/22 pada setiap host yang dipindai:

```
# Scan TCP/22 pada sebuah CIDR
nmap 192.168.0.0/24 192.168.1.0/24 -p 22
```

Nmap pertama-tama akan melakukan penemuan jaringan untuk membuat daftar host yang aktif, dan untuk setiap host, periksa apakah ada layanan pada port TCP/22.

Dengan cara yang sama, kita dapat melakukan pemindaian penuh semua port TCP pada setiap host yang ditemukan di jaringan "192.168.0.0/24", tidak termasuk host "192.168.0.4" misalnya:

```
# Port port dari sebuah CIDR dengan eksklusi
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```

Anda bebas menggabungkan semua opsi yang telah kita pelajari sejauh ini sesuai dengan kebutuhan Anda.

### VI. Kesimpulan

Pada bagian ini, kita telah melihat cara menggunakan Nmap untuk memetakan jaringan menggunakan berbagai opsi. Kita sekarang memiliki pemahaman yang mendalam tentang target pemindaian kita, serta perilaku pemindaian port Nmap dan metode penemuan host. Dan yang paling penting, kita tahu apa perilaku default dan keterbatasan Nmap, serta cara menggunakan opsi utamanya untuk melangkah lebih jauh.

Pada bagian selanjutnya, kita akan melihat mekanisme dan opsi untuk menemukan versi layanan dan sistem operasi yang dipindai oleh Nmap.

## 6 - Mendeteksi versi layanan dan sistem operasi dengan Nmap

### I. Presentasi

Di bagian ini, kita akan mempelajari cara menggunakan Nmap untuk menemukan dan mendeteksi secara akurat versi layanan dan sistem operasi yang digunakan oleh host yang dipindai. Kita akan melihat secara rinci bagaimana Nmap menyelesaikan tugas ini, serta keterbatasan aplikasi tersebut agar dapat memahami dan menafsirkan hasilnya dengan lebih baik.

Seperti yang telah kita lihat di bagian tutorial sebelumnya, secara default Nmap tidak akan mencari tahu layanan apa yang terbuka pada port yang dipindai dan dianggap terbuka. Jadi, jika Anda berkomunikasi layanan web pada port TCP/22, Nmap akan terus melaporkannya sebagai terbuka, tetapi sebagai layanan SSH. Ini karena Nmap menggunakan [database](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) lokal pada sistem Anda untuk mencari hubungan antara port/protokol dan nama layanan (file `/etc/services/`).

Dalam sebagian besar kasus, [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) akan memberikan Anda informasi yang benar, karena jarang ditemukan kasus seperti itu di lingkungan produksi. Namun, kasus-kasus sisanya adalah situasi di mana layanan klasik ([SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), HTTP, dll.) diekspos pada port non-klasik (misalnya 2022 untuk layanan SSH), yang dalam kasus ini Nmap tidak akan menemukan kecocokan dalam database lokalnya, atau kecocokan yang tidak sesuai dengan kenyataan, dan Anda akan kehilangan informasi penting.

Untungnya, Nmap menawarkan opsi dan mekanisme yang sangat tepat untuk menemukan layanan pasti apa yang mungkin bersembunyi di balik port yang terbuka. Nmap bahkan memiliki database kueri dan tanda tangan untuk mengidentifikasi teknologi dan versi yang tepat. Selain layanan, Nmap juga dapat mengidentifikasi teknologi yang digunakan dan versinya.

Itulah yang akan kita bahas di bagian ini.

### II. Cara mendeteksi teknologi atau versi

#### A. Pengingat tentang cara mengidentifikasi teknologi atau versi

Mendeteksi sebuah teknologi dan versinya melibatkan pengambilan nama layanan, CMS, aplikasi, atau perangkat lunak yang berkomunikasi pada port target. Sebagai contoh, sebuah halaman web dikelola oleh CMS (`WordPress`), dijalankan oleh layanan web (`Apache`, IIS, Nginx), dan di-host oleh server (Linux atau Windows). Tetapi bagaimana cara mengetahui layanan web mana yang berjalan?

Metodologi klasik untuk mengetahui informasi ini adalah _banner grabbing_, yang hanya terdiri dari menemukan di mana layanan yang bersangkutan menampilkan informasi ini dan membaca datanya. Sangat sering, dalam konfigurasi atau pemrosesan default mereka, layanan menampilkan nama dan bahkan versi mereka sebagai respons pertama setelah koneksi.

![nmap-image](assets/fr/32.webp)

_menampilkan versi segera setelah koneksi TCP dibuat oleh layanan FTP_

Di sini kita melihat bahwa koneksi TCP sederhana ke layanan ini melalui telnet menghasilkan paket TCP yang berisi teknologi dan versinya.

Setelah Anda mengetahui tentang jenis layanan yang Anda hadapi, Anda juga dapat mengirimkan perintah atau permintaan spesifik ke layanan tersebut untuk mengekstrak informasi darinya. Permintaan/perintah ini juga dapat dikirim secara membabi buta (tanpa yakin bahwa itu adalah jenis layanan yang benar), dengan harapan salah satunya akan memprovokasi respons dari layanan yang bersangkutan.

Dalam kasus lain yang lebih canggih, perlu mengirimkan paket-paket spesifik untuk menyebabkan reaksi, seperti kesalahan, yang akan memberikan informasi rinci tentang versi atau teknologi yang digunakan.

Seperti yang dapat Anda bayangkan, Nmap akan menggunakan semua teknik ini untuk mencoba mengidentifikasi jenis layanan yang tepat yang di-host pada sebuah port, serta nama teknologi dan versinya.

#### B. Memahami Probe dan Pencocokan Nmap

Untuk melakukan semua pemeriksaan ini pada setiap port yang dipindai, Nmap menggunakan database lokal yang sering diperbarui (sama seperti binari atau modulnya). Ini adalah file teks beberapa ribu baris: `/usr/share/nmap/nmap-service-probes`.

File ini terdiri dari banyak entri, semuanya diatur berdasarkan dua panduan utama:

- The `Probe`: ini adalah definisi dari paket yang akan dikirim Nmap dalam upaya memprovokasi reaksi dari layanan yang akan diidentifikasi. Anggap saja sebagai upaya buta seperti _Hello? Guten Tag? Halo? Um... Buenos Dias mungkin?_. Segera setelah layanan yang ditargetkan menerima probe yang dipahaminya (yaitu, berbicara protokol yang benar), layanan akan merespons Nmap, yang kemudian akan mendapatkan konfirmasi tentang jenis layanannya.

- Match: ini adalah ekspresi reguler yang diterapkan Nmap pada respons yang diperoleh. Jika pengiriman permintaan HTTP GET telah memprovokasi respons dari layanan, Nmap akan menerapkan puluhan ekspresi reguler pada respons ini untuk mengidentifikasi keberadaan, misalnya, kata `Apache`, `Nginx`, `Microsoft IIS`, dll.

Ada beberapa arahan lain untuk kasus-kasus spesifik, tetapi yang utama untuk memahami cara kerja Nmap dan menyesuaikan penggunaannya. Agar bagian teori ini lebih nyata, berikut adalah contohnya:

![nmap-image](assets/fr/33.webp)

_contoh Probe dalam file `/usr/share/nmap/nmap-service-probe` milik Nmap_

Di baris pertama contoh ini, kita melihat Probe yang mudah dipahami bernama `GetRequest`. Ini adalah paket TCP yang berisi permintaan HTTP GET kosong ke root layanan web menggunakan HTTP/1.0, diikuti oleh line feed dan baris kosong.

Baris `ports` memberi tahu Nmap untuk port mana mengirim Probe ini. Ini memungkinkan Anda untuk memprioritaskan tes dan menghemat waktu.

Terakhir, kita memiliki dua contoh `match`. Yang pertama, misalnya, akan mengategorikan layanan web yang dipindai sebagai `ajp13` jika ekspresi reguler yang terkandung dalam baris ini cocok dengan respons layanan yang diterima.

Untuk membantu Anda memahami seperti apa Probes, berikut adalah daftar beberapa Probes yang akan Anda temukan dalam file ini (ada 188 Probe pada saat tutorial ini ditulis).

![nmap-image](assets/fr/34.webp)

_contoh beberapa probe yang digunakan oleh Nmap dan ada di file `/usr/share/nmap/nmap-service-probes`._

Dua yang pertama (disebut `NULL` dan `GenericLines`) sangat menarik di sini, karena mereka hanya mengirim paket TCP kosong atau paket yang berisi pemisah baris. Layanan server sering kali mengumumkan diri mereka secara tepat segera setelah koneksi diterima, tanpa tindakan, perintah, atau permintaan spesifik apa pun dari klien.

Berikut ini adalah kasus _match_ yang sedikit lebih kompleks:

```
# Match Nginx + version in an error 400 page
match ssl/http m|^HTTP/1.1 400 Bad Request\r\n.*?Server: nginx/([\d.]+)[^\r\n]*?\r\n.*<title>400 The plain HTTP request was sent to HTTPS port</title>|s p/nginx/ v/$1/ cpe:/a:igor_sysoev:nginx:$1/
```

Ekspresi reguler yang tepat di sini terkandung di antara `m|` dan `|`, yang membatasi ekspresi reguler apa pun dalam berkas ini. Harap luangkan waktu untuk membaca seluruh contoh ini. Anda akan melihat sebuah seleksi dalam reguler: `([\d.]+)`, yang digunakan untuk mengisolasi sebuah versi. Contoh ini juga mendefinisikan elemen lain seperti nama produk `p/nginx/`, versi yang diambil `v/$1/`, dan CPE dengan versi `cpe:/a:igor_sysoev:nginx:$1/`.

CPE (Common Platform Enumeration) adalah sistem notasi terstandarisasi yang digunakan untuk mengidentifikasi dan mendeskripsikan perangkat lunak dan perangkat keras. Format ini memungkinkan pengelolaan kerentanan dan konfigurasi keamanan yang lebih efisien, dan yang terpenting, cara terpadu untuk merepresentasikannya, apa pun produk yang bersangkutan. Berikut adalah dua contoh CPE: `cpe:/o:microsoft:windows_8.1:r1` dan `cpe:/a:apache:http_server:2.4.35`

Di sini kita dengan jelas mengidentifikasi jenisnya `o` untuk OS, `a` untuk aplikasi, vendor, produk, dan versi.

Jadi, jika terjadi _match_ dengan salah satu ekspresi reguler ini, kita akan mendapatkan tidak hanya nama layanannya, tetapi juga versi dan CPE yang tepat, sehingga lebih mudah untuk menemukan CVE yang memengaruhi versi ini. Anda akan menemukan informasi ini dalam keluaran standar Nmap, dan Anda akan melihat bahwa itu sangat berguna untuk tujuan lain yang akan kita bahas dalam beberapa bagian.

Sintaks yang tepat dari _matches_ dan, secara lebih umum, dari arahan dalam file `/usr/share/nmap/nmap-service-probe` tidak berhenti di situ, dan mungkin tampak agak rumit jika Anda tidak terbiasa memanipulasi Nmap dan hasilnya. Namun, Anda setidaknya harus mengingat keberadaan dan operasi umumnya, yang akan berguna nanti ketika Anda ingin memahami atau men-debug hasil, menyesuaikan pemindaian, atau bahkan berkontribusi pada pengembangan Nmap.

### III. Menggunakan Nmap untuk mendeteksi versi

Kita sekarang akan menggunakan semua mekanisme _Probe_ dan _Match_ yang kompleks ini melalui opsi sederhana: `-sV`. Ini hanya memberi tahu Nmap: cobalah untuk mencari tahu secara persis layanan dan versi apa dari port yang telah Anda tetapkan yang terbuka.

```
# Mengaktifkan deteksi layanan dan versi
nmap 192.168.1.0/24 -sV
```

Berikut ini contoh lengkap hasil dari perintah tersebut:

![nmap-image](assets/fr/35.webp)

_hasil deteksi versi Nmap terhadap aplikasi yang terekspos di jaringan_

Di sini kita dapat melihat bahwa Nmap telah berhasil mengidentifikasi semua versi layanan jaringan yang diekspos oleh target ini, dan menampilkan informasi ini dalam kolom baru bernama `VERSION`. Dimungkinkan untuk melihat informasi yang cukup tepat, bahkan hingga sistem operasi, jika informasi ini merupakan bagian dari tanda tangan yang ditemukan.

Untuk memahami secara detail apa yang terjadi selama pemindaian kerentanan, kita dapat menggunakan opsi `--version-trace`. Ini akan memberikan tampilan mode debug, yang menampilkan _Probe_ yang mengarah ke deteksi:

```
# Mengaktifkan debug deteksi versi
nmap 192.168.1.0/24 -sV --version-trace
```

Sebagai hasilnya, kita akan memiliki banyak informasi untuk disortir. Cobalah untuk mengidentifikasi baris yang dimulai dengan `Service scan Hard match`. Anda kemudian akan melihat baris-baris seperti ini:

```
Service scan hard match (Probe NULL matched with NULL line 789): 10.10.10.187:21 is ftp. Version: |vsftpd|3.0.3||
Service scan hard match (Probe NULL matched with NULL line 3525): 10.10.10.187:22 is ssh. Version: |OpenSSH|7.4p1 Debian 10+deb9u7|protocol 2.0|
Service scan hard match (Probe GetRequest matched with GetRequest line 10510): 10.10.10.187:80 is http. Version: |Apache httpd|2.4.25|(Debian)|
```

Kita dapat dengan jelas melihat _Probes_ mana yang digunakan untuk mendeteksi teknologi dan versi (dalam hal ini _Probes_ `NULL` dan `GetRequest`), serta informasi yang diambil.

### IV. Menguasai tes dan akurasi deteksi

Sekarang kita akan kembali ke instruksi pada file `/usr/share/nmap/nmap-service-probe` yang tidak kita lihat sebelumnya:

![nmap-image](assets/fr/36.webp)

_probe `rarity` direktif dalam file `/usr/share/nmap/nmap-service-probes`._



Arahan ini digunakan untuk menunjukkan kelangkaan (yaitu prioritas/probabilitas) yang terkait dengan _Probe_. Notasi dari 1 hingga 9 ini memungkinkan Anda untuk mengontrol kelengkapan analisis yang dilakukan oleh Nmap ketika mengirim _Probe_. Dalam sistem "notasi" Nmap, kelangkaan 1 memberikan informasi dalam sebagian besar kasus, sedangkan kelangkaan 8 atau 9 mewakili kasus yang sangat khusus, khusus untuk konfigurasi atau layanan yang jarang ada.

Instruksi ini digunakan untuk menunjukkan kelangkaan (yaitu, prioritas/probabilitas) yang terkait dengan sebuah _Probe_. Notasi dari 1 hingga 9 ini memungkinkan Anda untuk mengontrol kelengkapan analisis yang dilakukan oleh Nmap saat mengirimkan _Probes_. Dalam sistem "notasi" Nmap, kelangkaan 1 memberikan informasi dalam sebagian besar kasus, sedangkan kelangkaan 8 atau 9 mewakili kasus yang sangat spesifik, khusus untuk konfigurasi atau layanan yang jarang ada.

Secara lebih jelas, dalam kasus default, Nmap akan mengirimkan kepada setiap layanan yang akan diidentifikasi _Probes_ yang memiliki kelangkaan 1 hingga 7. Untuk memberi Anda gambaran yang lebih baik tentang distribusi _Probes_ berdasarkan _kelangkaan_, berikut ini hitungannya:

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

Mungkin tampak kontraintuitif, ada lebih banyak kelangkaan 8 dan 9 daripada yang lainnya. Ini justru karena Probes kelangkaan 1 bersifat generik dan berfungsi di sebagian besar kasus, terlepas dari layanannya (ingat Probe `NULL` yang hanya mengirimkan paket TCP kosong). Sementara itu, Probes yang lebih kompleks hampir unik setiap layanan.

Jika kita ingin mengelola secara manual Probe yang ingin kita gunakan dalam pemindaian versi, kita dapat menggunakan opsi `--versi-intensitas`. Berikut adalah dua contoh:

```
# Deteksi versi kurang akurat dari default
nmap 192.168.1.0/24 -sV --version-intensity 2

# Deteksi sangat mendalam, menggunakan semua Probes yang ada
nmap 192.168.1.0/24 -sV --version-intensity 9
```

Untuk mengakhiri bahasan ini, berikut adalah contoh _Probe_ 9 dan 8:

![nmap-image](assets/fr/37.webp)

_contoh Probe pada rarity 8 dan 9 dalam file `/usr/share/nmap/nmap-service-probe`._

Kedua _Probes_ ini mendeteksi server Quake1 dan Quake2 (video game). Menarik untuk sisi nostalgia, tetapi tidak akan banyak berguna dalam kehidupan sehari-hari.

Bergantung pada kebutuhan Anda akan presisi atau kecepatan, ingatlah bahwa prinsip `kelangkaan` ini ada dan dapat memengaruhi hasilnya.

### V. Menggunakan Nmap untuk mendeteksi sistem operasi

Sekarang kita akan melihat bagaimana Nmap dapat membantu kita mendeteksi sistem operasi dari host yang dipindai dan ditemukan di jaringan. Untuk melakukan ini, gunakan opsi `-O` (untuk `OS Scan`) dari Nmap.

```
# Mengaktifkan OS Scan
nmap -O 10.10.10.0/24
```

Berikut adalah contoh hasilnya. Di sini, Nmap memberi tahu kita bahwa itu mungkin OS Linux, dan menawarkan berbagai statistik mengenai versinya yang tepat.

![nmap-image](assets/fr/38.webp)

_deteksi probabilitas identifikasi sistem operasi oleh Nmap_

Untuk mencapai ini, Nmap akan menggunakan banyak teknik yang bekerja dengan cara yang sangat mirip dengan _Probes_ dan _Matches_ untuk deteksi teknologi dan versi. Perbedaan utamanya adalah bahwa Nmap akan menggunakan parameter protokol ICMP, TCP, UDP, dan lainnya yang cukup "tingkat rendah". Berikut adalah dua contoh pengujian untuk mendeteksi sistem operasi Microsoft Windows 11:

![nmap-image](assets/fr/39.webp)

_contoh tes yang dilakukan oleh Nmap untuk mendeteksi OS Windows 11_

Terus terang, tes ini sangat sulit ditafsirkan, dan kita tidak akan mencoba memahaminya secara mendalam dalam konteks tutorial pengantar Nmap. Jika Anda ingin mempelajari subjek ini lebih dalam, file yang berisi informasi ini adalah `/usr/share/nmap/nmap-os-db`.

Namun, Anda perlu menyadari bahwa deteksi OS lebih merupakan probabilitas yang ditetapkan oleh Nmap daripada kepastian.

### VI. Kesimpulan

Pada bagian ini, kita telah belajar cara menggunakan opsi Nmap untuk mendeteksi teknologi, versi, dan sistem operasi dari host dan layanan yang dipindai. Kita sekarang memiliki pemahaman yang baik tentang bagaimana Nmap mendapatkan informasi ini dari jarak jauh. Kita juga telah meninjau opsi untuk mengelola verbosity dan akurasi uji, serta keterbatasan aplikasi pada subjek ini.

Di bagian selanjutnya, kita akan belajar cara menggunakan skrip NSE Nmap untuk melakukan analisis keamanan pada sistem informasi kita. Luangkan waktu untuk membaca kembali bagian-bagian terakhir jika Anda perlu, dan jangan ragu untuk berlatih dan mendalami seluk beluk aplikasi itu sendiri untuk lebih menguasai apa yang telah kita pelajari sejauh ini.

## 7 - Analisis keamanan: mendeteksi kerentanan

### I. Presentasi

Di bagian ini, kita akan belajar cara menggunakan aplikasi pemindai jaringan Nmap untuk mendeteksi dan menganalisis kerentanan pada target pemindaian kita. Secara khusus, kita akan melihat berbagai opsi yang tersedia untuk menyelesaikan tugas ini, dan mempelajari batasan kemampuan alat agar dapat memahami dan menafsirkan hasilnya dengan lebih baik.

Di bagian pertama ini, kita akan melihat pemindai kerentanan Nmap, dan melihat cara menggunakan opsi dasar deteksi kerentanan. Di bagian selanjutnya, kita akan melihat lebih dekat cara kerja fitur ini, dan bagaimana fitur ini dapat disesuaikan.

### II. Menggunakan Nmap untuk mendeteksi kerentanan

Kita sekarang ingin menggunakan pemindai jaringan Nmap untuk mendeteksi kerentanan dalam layanan dan sistem dari sistem informasi kita. Ini berarti bahwa selain menemukan host aktif, menghitung layanan yang terbuka, dan mendeteksi versi serta teknologi, Nmap akan mencari kerentanan.

Untuk mencapai ini, Nmap mengandalkan skrip NSE (_Nmap Scripting Engine_), yang dapat dilihat sebagai modul yang memungkinkan pendekatan terperinci untuk pengujian.

Dengan opsi yang tepat, kita akan meminta Nmap untuk menggunakan berbagai skrip NSE-nya pada setiap layanan yang ditemukan, yang memungkinkan kita untuk menemukan :

- Kesalahan konfigurasi
- Penemuan versi dan OS tambahan dan lebih canggih
- Kerentanan yang diketahui (CVE)
- Pengidentifikasi yang lemah
- Elemen karakteristik dari infeksi malware
- Kemungkinan Denial of Service
- Dan lain-lain

Seperti yang Anda lihat, skrip NSE secara signifikan memperluas kemampuan Nmap dalam hal operasi jaringan yang dapat dilakukannya. Dan ini untuk melakukan tugas yang jauh lebih canggih dari sebelumnya. Kabar baiknya adalah, seperti biasa, fitur-fitur ini dapat digunakan secara sederhana melalui opsi dan dalam konteks default. Inilah yang akan kita lihat selanjutnya.

### III. Contoh pemindaian kerentanan

Skrip NSE dapat digunakan saat menggunakan Nmap untuk memindai satu port pada sebuah host, semua layanan pada host tersebut, atau semua layanan yang terdeteksi pada beberapa jaringan. Oleh karena itu, kita dapat menggunakan opsi yang akan kita lihat di semua konteks yang telah kita pelajari sejauh ini.

Untuk mengaktifkan pemindaian kerentanan melalui pemindaian Nmap, kita perlu menggunakan opsi `-sC`:

```
# Mengaktifkan pemindaian kerentanan selama pemindaian
nmap -sC 10.10.10.152
```

Ingatlah bahwa secara default, jika Anda tidak menentukan apa pun, Nmap hanya akan memindai 1.000 port paling umum. Ini tidak akan mendeteksi kerentanan pada port-port yang tidak umum yang mungkin diekspos oleh target Anda.

Sebelum menggunakan fungsionalitas ini pada sistem informasi produksi, saya mengundang Anda untuk melanjutkan membaca tutorial. Di bagian selanjutnya, kita akan melihat bagaimana cara mengontrol dampak dan jenis tes yang akan dijalankan dengan lebih baik.

Dengan menggunakan kembali apa yang telah kita pelajari sebelumnya, kita dapat, misalnya, menjadi lebih komprehensif dan memindai semua port TCP dari target:

```
# Mengaktifkan pemindaian kerentanan pada semua port
nmap -sC -p- 10.10.10.152
```

Berikut adalah hasil pemindaian Nmap menggunakan skrip NSE:

![nmap-image](assets/fr/40.webp)

_contoh hasil pemindaian kerentanan pada sebuah host melalui Nmap._

Di sini kita melihat tampilan informasi tambahan yang menarik dalam konteks analisis kerentanan:

- Layanan FTP dapat diakses secara anonim, dan tidak dilindungi oleh otentikasi. Skrip NSE yang bertugas melakukan verifikasi ini memberi tahu kita, dan bahkan menampilkan sebagian dari struktur direktori layanan FTP. Di sini kita melihat bahwa kita memiliki akses ke direktori `C` dari sistem Windows!
- Skrip NSE yang bertugas mengambil layanan web lanjutan menampilkan judul halaman, memberi kita gambaran yang lebih baik tentang apa yang di-host oleh layanan web tersebut.
- Kita juga memiliki analisis kecil dari konfigurasi layanan  SMB (skrip `smb2-time`, `smb-security-mode` dan `smb2-security-mode`). Informasi ini ditampilkan sedikit berbeda, setelah hasil pemindaian jaringan, untuk membuatnya lebih mudah dibaca. Secara khusus, informasi ini menunjukkan tidak adanya tanda tangan pertukaran SMB. Kelemahan konfigurasi ini memungkinkan target untuk digunakan dalam serangan SMB Relay, kelemahan keamanan yang sering dieksploitasi dalam pengujian intrusi/serangan siber.

Tentu saja, ini hanyalah satu contoh. Nmap memiliki skrip NSE untuk banyak layanan, menargetkan berbagai kerentanan. Kita akan melihat lebih dekat kemungkinan-kemungkinan ini di bagian selanjutnya.

Untuk mengakhiri pengantar pemindaian kerentanan ini, berikut adalah perintah lengkap untuk penemuan jaringan, pemindaian port TCP, deteksi versi, dan kerentanan:

```
# erintah pemindaian kerentanan yang lengkap dan realistis
nmap -sV -sC -p- 192.168.0.0/24 192.168.1.13 192.168.2.10-20 --exclude 192.168.0.4
```

Berikut ini adalah perintah yang mulai terlihat seperti kasus penggunaan Nmap yang lebih realistis!

### IV. Memahami keterbatasan Nmap dalam pemindaian kerentanan

Mari kita perjelas: Nmap tidak mampu melakukan pengujian penetrasi lengkap pada sistem informasi Anda, atau mensimulasikan operasi Red Team. Ada beberapa batasan yang perlu Anda ketahui agar tidak memiliki rasa aman yang semu:

- **Cakupan Terbatas**: Meskipun skrip NSE Nmap kuat, cakupan pengujiannya mungkin terbatas dibandingkan dengan aplikasi deteksi kerentanan khusus lainnya. Beberapa kerentanan mungkin tidak tercakup oleh skrip NSE yang tersedia, seperti kerentanan Active Directory, paparan data sensitif, atau kasus yang lebih canggih dari aplikasi web yang rentan.
- **Kompleksitas Kerentanan**: Jenis kerentanan tertentu mungkin sulit dideteksi menggunakan skrip NSE karena kompleksitasnya. Misalnya, kerentanan yang memerlukan interaksi kompleks dengan layanan jarak jauh mungkin tidak terdeteksi secara efektif oleh Nmap (seperti dalam kasus izin yang berlebihan dalam berbagi file atau kelemahan kontrol izin dalam aplikasi web).
- **Deteksi Pasif**: Nmap berfokus terutama pada pemindaian aktif untuk mendeteksi kerentanan, yang berarti mungkin tidak secara efektif mendeteksi kerentanan potensial tanpa membangun koneksi aktif dengan host target. Kerentanan yang tidak muncul selama pemindaian aktif mungkin terlewatkan (seperti dalam kasus injeksi kode dalam aplikasi web).
- **Ketergantungan pada Pembaruan**: [Database](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) skrip NSE Nmap terus berkembang, tetapi mungkin ada keterlambatan antara penemuan kerentanan baru dan penambahan skrip yang sesuai ke Nmap. Akibatnya, Nmap mungkin tidak selalu up-to-date dengan kerentanan terbaru.
- **Positif Palsu dan Negatif Palsu**: Seperti halnya aplikasi keamanan lainnya, skrip NSE Nmap dapat menghasilkan positif palsu (peringatan kerentanan palsu) atau negatif palsu (kerentanan nyata tidak terdeteksi). Ini adalah sesuatu yang perlu diingat saat menganalisis hasil Nmap.

Jadi, penting untuk memahami apa yang Nmap lakukan dan tidak lakukan, dan demikian pula, mengetahui cara menginterpretasikan hasilnya. Secara khusus, kita telah melihat di seluruh tutorial ini bahwa opsi default dapat membuat kita melewatkan elemen penting yang dapat diungkap dengan penggunaan yang cermat. 

Terlepas apakah Anda seorang network system administrator, security engineer, atau bahkan CISO, menggunakan Nmap memberi Anda gambaran umum tentang status keamanan sebuah sistem informasi. Ini adalah langkah pertama yang penting dalam mengamankan sebuah sistem, yang dapat dilakukan secara teratur oleh tim IT. Namun, ini tidak dapat menggantikan intervensi dan nasihat dari ahli keamanan siber (https://www.it-connect.fr/cours-tutoriels/securite-informatique/), yang akan dapat mengungkap kelemahan jauh lebih komprehensif daripada Nmap.

### V. Kesimpulan

Pada bagian pertama Modul 3 ini, kita telah memperkenalkan pemindaian kerentanan melalui Nmap. Kita sekarang tahu cara menggunakan opsi utama untuk melakukan tugas ini, tetapi kita juga tahu batasannya. Pada bagian selanjutnya, kita akan melihat lebih dekat fungsionalitas ini, menggunakan skrip NSE untuk memperluas kekuatan Nmap hingga sepuluh kali lipat.

## 8 - Menggunakan skrip NSE Nmap

### I. Presentasi

Di bagian ini, kita akan melihat secara mendalam skrip NSE (_Nmap Scripting Engine_). Secara khusus, kita akan melihat mengapa mereka adalah salah satu kekuatan besar dari alat ini, bagaimana cara kerjanya, dan bagaimana cara menelusuri serta menggunakan banyak skrip yang ada.

Bagian ini merupakan kelanjutan dari tutorial sebelumnya, di mana kita belajar cara menggunakan fitur pemindaian kerentanan Nmap secara dasar. Sekarang kita akan melihat lebih dekat bagaimana [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) bekerja dalam hal ini, sehingga kita dapat kembali melakukan pemindaian yang lebih tepat dan terkontrol.

### II. Konsep skrip Nmap NSE

Skrip NSE Nmap memungkinkan Anda untuk memperluas kemampuannya dengan cara yang sangat fleksibel. Mereka ditulis dalam LUA, sebuah bahasa skrip yang lebih mudah ditangani dan diakses daripada C atau C# yang digunakan oleh Nmap. Keuntungan menggunakan skrip LUA dengan Nmap daripada aplikasi mandiri adalah memungkinkan kita untuk memanfaatkan kecepatan eksekusi dan fitur standar Nmap (host, port dan penemuan versi, dll.).

Skrip ini diorganisir berdasarkan kategori, dan satu skrip dapat termasuk dalam lebih dari satu kategori:

 
| Kategori | Deskripsi |
|----------------|-------------|
| **auth** | Berisi skrip yang berkaitan dengan autentikasi pada layanan, termasuk akses anonim atau enumerasi pengguna. Contoh: `oracle-enum-users`, `ftp-anon`. |
| **broadcast** | Berisi skrip yang berkaitan dengan operasi broadcast di jaringan, terutama untuk mengeksploitasi dan menemukan layanan, host, atau protokol tertentu yang mengandalkan broadcast (IPv6, wake on lan, IGMP, dll.). Contoh: `broadcast-dhcp6-discover`, `broadcast-ospf2-discover`. |
| **brute** | Berisi skrip yang berkaitan dengan operasi brute force autentikasi pada layanan (brute force [SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), MSSQL, dll.). Contoh: `ssh-brute`, `vnc-brute`. |
| **default** | Berisi skrip yang digunakan dalam kasus default (penggunaan `-sC`). Beberapa kriteria digunakan untuk memvalidasi masuknya skrip ke dalam kategori ini, termasuk kecepatan eksekusi, struktur keluaran, keandalan pengujian, sifat "intrusif" hoặc "berisiko", dll. |
| **discovery** | Berisi skrip yang berkaitan dengan penemuan jaringan dan layanan tingkat lanjut. Misalnya, enumerasi konten berbagi SMB, versi layanan VNC, kueri SNMP, dll. Contoh: `mysql-info`, `http-security-headers`. |
| **dos** | Berisi skrip yang dapat menyebabkan denial of service. Ini bisa berupa skrip yang dibuat untuk mengeksploitasi kerentanan jenis denial of service atau skrip yang memiliki efek samping denial of service. Oleh karena itu, berhati-hatilah (skrip ini dikecualikan dari kategori `default`). Contoh: `http-slowloris`, `ipv6-ra-flood`. |
| **exploit** | Berisi skrip yang dibuat untuk mengeksploitasi kerentanan secara langsung. Contoh: `http-shellsock`, `smb-vuln-ms08-067`. |
| **external** | Berisi skrip yang memerlukan penggunaan sumber daya pihak ketiga, seperti basis informasi daring. Ini terutama menunjukkan upaya koneksi ke luar (perhatikan kerahasiaan). Contoh: `whois-ip`, `dns-blacklist`, `ip-geolocation-geoplugin`. |
| **fuzzer** | Berisi skrip yang dirancang untuk mengirim frame, paket, atau parameter yang tidak diharapkan oleh suatu layanan. Hal ini terutama memungkinkan terjadinya kesalahan atau malfungsi untuk mendapatkan petunjuk kerentanan atau informasi teknis. Contoh: `dns-fuzz`, `http-form-fuzzer`. |
| **intrusive** | Berisi skrip yang dikategorikan sebagai "berisiko" dari sudut pandang ketersediaan atau deteksi. Skrip ini dapat menyebabkan sistem crash atau terdeteksi sebagai malware oleh solusi keamanan. Ini adalah kategori kebalikan dari `safe`. Contoh: `smtp-brute`, `smb-vuln-ms08-067`, `smb-psexec`. |
| **malware** | Berisi skrip yang dirancang untuk mendeteksi keberadaan elemen karakteristik malware, seperti port mendengarkan yang umum digunakan bởi backdoor yang dikenal. Contoh: `ftp-proftpd-backdoor`, `smtp-strangeport`. |
| **safe** | Berisi skrip yang dianggap aman dari sudut pandang deteksi atau stabilitas. Ini adalah kategori kebalikan dari `intrusive` và sebagian besar berisi skrip identifikasi versi tingkat lanjut atau pengumpulan elemen konfigurasi. Contoh: `html-title`, `smb2-security-mode`, `ms-sql-info`. |
| **version** | Berisi skrip yang memungkinkan deteksi versi tingkat lanjut. Skrip ini dapat digunakan sebagai pelengkap Probes dan Matchs yang dipelajari sebelumnya ketika deteksi versi memerlukan operasi yang sedikit lebih kompleks. Contoh: `http-php-version`, `vmware-version`. |
| **vuln** | Berisi skrip yang dirancang untuk mendeteksi keberadaan kerentanan yang diketahui (CVE) tanpa mengeksploitasinya (kebalikan dari kategori `exploit`). Skrip ini umumnya hanya melaporkan status "vulnerable" atau tidak dari suatu layanan. Contoh: `smb-vuln-ms17-010` (eternal blue), `http-phpmyadmin-dir-traversal`. |

Secara teknis, kategori yang dimiliki skrip ditunjukkan secara langsung dalam kodenya.

![nmap-image](assets/fr/41.webp)

_kategori skrip nSE `ftp-anon`._

Contoh ini menunjukkan bagian dari kode skrip NSE `ftp-anon.nse`, yang eksekusinya telah kita lihat pada bagian sebelumnya.

### III. Daftar skrip NSE yang ada

Secara default, skrip NSE Nmap berada di direktori `/usr/share/nmap/scripts/`, tanpa struktur folder atau hirarki tertentu. Berikut ini adalah gambaran umum isi direktori ini:

![nmap-image](assets/fr/42.webp)

_mengekstrak isi direktori `/usr/share/nmap/scripts/` yang berisi skrip NSE._

Direktori ini berisi lebih dari 5.000 skrip NSE. Dalam banyak kasus, bagian pertama dari nama skrip berisi protokol atau kategori tempat ia berada. Ini memungkinkan kita untuk menyortir daftar, misalnya, jika kita ingin membuat daftar semua skrip yang menargetkan layanan FTP:

![nmap-image](assets/fr/43.webp)

_daftar skrip NSE Nmap dengan nama yang dimulai dengan `ftp-`._

Nmap tidak menawarkan pilihan untuk menelusuri dan membuat daftar skrip NSE; Anda dapat menggunakan perintah `--script-help` diikuti dengan nama kategori atau kata :

```
# Membuat daftar semua skrip yang namanya dimulai dengan "ftp-"
nmap --script-help=ftp-*

# Membuat daftar semua skrip dari kategori "discovery"
nmap --script-help=discovery
```

Namun, keluarannya adalah nama setiap skrip dan deskripsinya, yang tidak optimal jika pencarian memunculkan beberapa lusin skrip:

![nmap-image](assets/fr/44.webp)

_hasil dari penggunaan perintah `--script-help` dari Nmap_

Menurut pendapat saya, metode yang paling efektif adalah dengan menggunakan perintah klasik Linux di direktori `/usr/share/nmap/scripts/`:

```
# Membuat daftar skrip yang menargetkan layanan "ssh"
ls -al /usr/share/nmap/scripts/ssh*

# Membuat daftar skrip dari kategori "dos"
grep -rl '"dos"' /usr/share/nmap/scripts/
```

Jangan ragu untuk menelusuri kode modul yang menarik bagi Anda, untuk lebih memahami cara kerja skrip NSE.

### IV. Menggunakan skrip NSE dari Nmap

Sekarang kita akan mempelajari cara melakukan pemindaian kerentanan dengan memilih skrip NSE yang kita minati dengan cermat.

#### A. Memilih skrip berdasarkan kategori

Untuk memulainya, kita dapat memilih untuk mengeksekusi semua skrip yang termasuk dalam kategori tertentu. Kita perlu menunjukkan kategori ini atau kategori-kategori ini pada Nmap dengan argumen `--script <kategori>` :

```
# Menggunakan skrip NSE default
nmap --script default 10.10.10.152
```

Perintah pertama ini setara dengan perintah `nmap -sC`. Secara default, Nmap akan memilih skrip dalam kategori `default`, tetapi itu hanya untuk keperluan argumen. Perintah berikutnya, misalnya, akan menggunakan semua skrip dalam kategori`discovery`:

```
# Menggunakan skrip NSE dari kategori "discovery"
nmap --script discovery 10.10.10.152
```

Seperti yang telah kita lihat, beberapa kategori memungkinkan kita untuk dengan cepat mengidentifikasi apa yang dilakukan oleh skrip NSE terkait (`discovery`, `vuln`, `exploit`), sementara yang lain mendefinisikan tingkat risiko, deteksi, atau stabilitas dari pengujian yang dilakukan. Jika kita berada dalam konteks yang sensitif dan tidak memahami dengan baik berbagai tindakan yang dilakukan oleh pemilihan skrip kita, kita dapat memilih untuk menggabungkan seleksi untuk hanya memilih skrip yang berada dalam kategori `discovery` dan `safe`:

```
# Menggunakan skrip dari beberapa kategori
nmap --script "discovery and safe" 10.10.10.152
```

Jika Anda benar-benar dan secara eksplisit ingin mengecualikan skrip dari kategori `dos` dan `intrusif`, Anda dapat menggunakan notasi berikut:

```
# Mengecualikan kategori
nmap --script "not intrusive and not dos" 10.10.10.152
```

Harap diperhatikan bahwa menentukan kondisi pengecualian seperti di atas akan mengakibatkan penggunaan semua kategori lain yang tidak secara eksplisit dikecualikan. Agar lebih adil, kita dapat menentukan, misalnya:

```
# Sertakan skrip dari kategori "vuln" kecuali yang terlalu berisiko
nmap --script "vuln and not intrusive and not dos" 10.10.10.152

# Hal yang sama, tetapi hanya menargetkan protokol HTTP
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152
```

Berikut adalah beberapa contoh cara menangani skrip NSE berdasarkan kategori, terutama saat menggunakan Nmap untuk analisis kerentanan dalam konteks nyata.

#### B. Memilih skrip sebagai satu unit

Kita juga dapat memilih untuk melakukan satu tes spesifik selama analisis, tes yang sesuai dengan skrip NSE. Untuk melakukan ini, kita perlu menentukan nama skrip dalam parameter `-script <name>`. Sebagai contoh skrip `ftp-anon.nse`:

```
# Menggunakan skrip NSE dan port tertentu
nmap --script ftp-anon -p 21 10.10.10.152
```

Kita kemudian mendapatkan hasil yang sangat tepat:

![nmap-image](assets/fr/45.webp)

_hasil penggunaan skrip NSE `ftp-anon` pada port FTP melalui Nmap._

Kita melihat hasil dari menjalankan skrip `ftp-anon` pada port 21, dan tidak ada port lain, karena kita menentukan opsi `-p 21`. Kita juga bisa melakukan pemindaian port dasar, mengeksekusi skrip `ftp-anon` hanya pada layanan FTP yang ditemukan:

```
# Menggunakan skrip NSE spesifik
nmap --script ftp-anon 10.10.10.152
```

Dengan begitu, Nmap juga akan menjalankan pengujian koneksi anonim ini jika menemukan layanan FTP pada port lain. 

Untuk deskripsi singkat tentang apa yang dilakukan skrip NSE, Anda dapat menggunakan opsi `--script-help` yang disebutkan di atas:

![nmap-image](assets/fr/46.webp)

_bantuan menampilkan hasil untuk skrip NSE `sshv1`._

Singkatnya, sekali lagi kita bisa menggunakan kembali semua opsi penemuan jaringan, layanan, versi, dan teknologi yang telah kita gunakan sampai sekarang!

#### C. Mengelola argumen skrip

Dalam penggunaan Nmap, Anda akan menemukan beberapa skrip NSE yang membutuhkan argumen masukan agar dapat berfungsi dengan benar. Sekarang kita akan melihat cara meneruskan argumen ini ke skrip melalui opsi Nmap.

Sebagai contoh, kita akan mengambil skrip `ssh-brute`, yang memungkinkan Anda melakukan serangan brute force pada layanan SSH.

Serangan brute force klasik terdiri dari pengujian beberapa kata sandi (terkadang jutaan) dalam upaya untuk mengautentikasi ke akun tertentu. Dengan mencoba begitu banyak kata sandi, penyerang bertaruh pada kemungkinan bahwa pengguna telah menggunakan kata sandi lemah dari kamus kata sandi yang digunakan untuk serangan. 

Skrip ini memiliki opsi "default", yang dapat kita sesuaikan agar sesuai dengan konteks kita. Dalam konteks serangan ini, misalnya, kita dapat menyediakan daftar pengguna dan kamus kata sandi kepada Nmap untuk digunakan. Sejauh yang saya tahu, tidak mungkin untuk dengan mudah membuat daftar argumen yang diperlukan untuk sebuah skrip. Jadi cara paling andal untuk mengetahui argumen yang diperlukan untuk sebuah skrip adalah dengan mengunjungi situs web resmi Nmap. Tautan langsung ke dokumentasi untuk skrip NSE dapat diperoleh dengan menggunakan opsi `--script-help`:

![nmap-image](assets/fr/47.webp)

_hasil menampilkan bantuan untuk skrip NSE `ssh-brute` dengan tautan ke nmap.org._

Dengan mengklik tautan yang ditunjukkan, kita membuka halaman web situs ini [https://nmap.org](https://nmap.org/):

![nmap-image](assets/fr/48.webp)

_daftar argumen yang dapat diteruskan ke skrip NSE Nmap `ssh-brute` _

Sekarang Anda memiliki pemahaman yang jelas tentang argumen yang dapat digunakan, terutama `passdb` (file daftar kata sandi) dan `userdb` (file daftar nama pengguna). Dokumentasi Nmap merujuk pada library internal karena mekanisme brute force dan opsi terkait disatukan, atau distandardisasi, untuk digunakan secara seragam di berbagai skrip seperti (`ssh-brute`, `mysql-brute`, `mssql-brute`, dan lain-lain). Oleh karena itu, skrip-skrip ini akan memiliki argumen yang hampir sama :

```
# Buat berkas berisi daftar pengguna
echo "root" > /tmp/userlist

# Buat berkas berisi daftar kata sandi
echo "123456" > /tmp/passlist
echo "NomEntreprise75" >> /tmp/passlist
echo "changezmoi" >> /tmp/passlist

# Jalankan serangan brute force SSH melalui pemindaian jaringan Nmap
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```

Seperti yang dapat Anda lihat pada perintah terakhir ini, kita dapat menentukan argumen yang diperlukan untuk sebuah skrip Nmap menggunakan opsi `--scripts-args key=value,key=value`. Berikut adalah kemungkinan hasil keluaran Nmap saat melakukan brute force SSH melalui skrip NSE `ssh-brute`:

![nmap-image](assets/fr/49.webp)

_hasil dari eksekusi bruteforce SSH melalui Nmap._

Seperti yang Anda lihat, informasi yang dihasilkan oleh skrip NSE diawali dengan `NSE: [nama skrip]` pada keluaran interaktif (keluaran terminal), sehingga lebih mudah ditemukan. Dalam tampilan hasil Nmap yang biasa, kita cukup mendapatkan ringkasan yang menunjukkan apakah identifier yang lemah telah ditemukan atau tidak (termasuk kata sandi, ingat).

Untuk melangkah lebih jauh, dan untuk mengingatkan Anda bahwa semua ini dapat digunakan di samping semua opsi yang telah kita lihat, berikut adalah perintah yang akan menemukan jaringan `10.10.10.0/24`, memindai 2.000 port TCP paling sering, dan menjalankan pencarian akses anonim pada layanan FTP serta brute force pada layanan SSH:

```
# Example of a complete command using multiple scripts
nmap --top-ports 2000 10.10.10.0/24 --script ftp-anon,ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist
```

Ini hanyalah salah satu contoh dari sekian banyak skrip dan opsi yang tersedia. Sekarang kita memiliki pemahaman yang lebih baik tentang cara memahami dengan baik skrip NSE, baik yang memerlukan argumen maupun tidak, dan cara meneruskan argumen ini ke Nmap.

### V. Kesimpulan

Di bagian ini, kita telah belajar cara menggunakan skrip NSE Nmap untuk melakukan berbagai tugas. Saya mengundang Anda untuk meluangkan waktu menemukan berbagai kategori skrip dan skrip itu sendiri, untuk melihat seberapa banyak pengujian yang dapat diotomatisasi.

Selama beberapa bagian terakhir, kita telah mengumpulkan opsi penemuan, pemindaian, dan enumerasi yang lebih atau kurang canggih. Saat ini, Anda seharusnya sudah menyadari bahwa keluaran dan tampilan hasil Nmap mulai menjadi cukup luas, terkadang bahkan terlalu bertele-tele untuk terminal kita. Di bagian selanjutnya, kita akan belajar cara menguasai keluaran ini, khususnya dengan menyimpannya dalam berkas dalam berbagai format.

## 9 - Mengelola data keluaran Nmap

### I. Presentasi

Di bagian ini, kita akan melihat keluaran yang dihasilkan oleh Nmap, dan khususnya berbagai opsi untuk memformat keluaran ini. Kita akan melihat bahwa Nmap dapat menghasilkan beberapa format keluaran untuk memenuhi berbagai kebutuhan, dan ini juga merupakan salah satu kekuatan besar dari aplikasi ini.

Secara default, Nmap menawarkan tampilan detail dari hasil pemindaian dan pengujian yang dilakukannya. Ini termasuk host dan layanan yang dipindai, yang terdeteksi sebagai dapat diakses, rincian port terbuka, status, dan versinya. Selain itu, detail dari skrip NSE juga tersedia dalam keluaran terminal. Namun, keluaran ini dapat dengan cepat menjadi sangat banyak, meskipun dengan format informasi yang jelas, yang dapat menyulitkan untuk menemukan informasi yang tepat dalam hasil.

### II. Menguasai format keluaran Nmap

#### A. Menyimpan hasil pemindaian dalam file teks

Untuk mempermudah, [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) membuatnya sangat mudah untuk menyimpan keluarannya dalam file teks. Ini dapat berguna untuk pengarsipan, perbandingan dengan pengujian lain, tetapi juga untuk menelusuri keluaran ini dengan aplikasi pengolah kata khusus atau bahasa skrip, seperti Sublime Text, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/), Python, grep, sed, dll. Untuk menyimpan keluaran standar Nmap dalam berkas file, kita dapat menggunakan opsi opsi `-oN <filename>` ("N" pada "normal"):

```
# Simpan keluaran Nmap ke berkas
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt
```

Tidak mengherankan, karena Nmap akan menampilkan output standar yang biasa di terminal kita, tetapi juga dalam file yang ditentukan.

#### B. Output generate Nmap dalam format ringkas

Ada juga format keluaran kedua dalam gaya "teks" yang mudah diinterpretasikan oleh manusia: format "greppable".

Format ini dibuat untuk menyediakan "tampilan ringkas" dari keluaran Nmap, yang terstruktur sedemikian rupa untuk memfasilitasi pemrosesannya oleh aplikasi seperti `grep`. Mari kita lihat contoh dari jenis keluaran ini:

![nmap-image](assets/fr/50.webp)

_pemindaian jaringan nmap dan keluaran dalam format "greppable"_

Di sini, saya telah melakukan penemuan jaringan, pemindaian port, dan analisis teknologi serta versi pada jaringan /24, kemudian menyimpan keluarannya ke dalam berkas dalam format "greppable". Saya mendapatkan file yang berisi dua baris per host aktif:

- Baris pertama memberi tahu bahwa host tersebut dalam keadaan _Up_;
- Baris kedua memberikan informasi port yang telah dipindai, statusnya, serta informasi teknologi dan versi yang diambil dalam format yang sangat spesifik: `<port>/<status/<protokol>//<layanan>//<versi>/,`

Format dengan pembatas tetap ini memungkinkan pemrosesan cepat oleh aplikasi pengolah kata seperti `grep`, atau bahasa skrip dan pemrograman. Perintah berikut, misalnya, memungkinkan saya dengan mudah mengambil informasi tentang host `10.10.10.5` dari pemindaian besar Nmap yang hasilnya akan sulit untuk ditelusuri:

```
# Saring berdasarkan alamat IP di file Nmap "greppable"
grep '10.10.10.5' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Status: Up
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)
```
Sebaliknya, saya juga dapat dengan mudah membuat daftar semua host yang memiliki port 21 terbuka, karena port dan IP berada pada jalur yang sama:

```
# Saring berdasarkan port terbuka di berkas Nmap "greppable"
grep '21/open' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)

Host: 10.10.10.152 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Indy httpd 18.1.37.13946 (Paessler PRTG bandwidth monitor)/, 135/open/tcp//msrpc//Microsoft Windows RPC/, 139/open/tcp//netbios-ssn//Microsoft Windows netbios-ssn/, 445/open/tcp//microsoft-ds//Microsoft Windows Server 2008 R2 - 2012 microsoft-ds/ Ignored State: closed (995)
```

Untuk menghasilkan keluaran seperti itu, kita perlu menggunakan opsi `-oG <filename>.gnmap` ("G" pada "grep"). Saya menggunakan ekstensi `.gnmap` sebagai kebiasaan untuk file seperti itu, tetapi Anda bisa menggunakan ekstensi apa pun yang Anda suka.

```
# Simpan keluaran Nmap ke berkas dalam format "greppable"
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap
```

Format ini dapat digunakan untuk berbagai tujuan dan khususnya berguna untuk pembuatan naskah/penyortiran yang cepat. Namun demikian, format ini cenderung ditinggalkan demi format yang akan kita bahas berikutnya.

_Catatan: format greppable `-oG` secara resmi dihentikan (deprecated) sejak Nmap versi 7.90. Meskipun masih dapat digunakan untuk tujuan kompatibilitas, disarankan untuk menggunakan format XML atau format normal untuk pengembangan atau analisis otomatis._

#### C. Format XML untuk keluaran Nmap

Format terakhir yang patut disebutkan dalam tutorial ini adalah XML. Berbeda dengan dua format sebelumnya, format ini tidak dirancang untuk dibaca oleh manusia, melainkan oleh aplikasi atau skrip lain.

XML (_eXtensible Markup Language_) adalah bahasa markah yang digunakan untuk menyimpan dan mengangkut data, menawarkan struktur hierarkis melalui tag khusus. 

Di dalam Nmap, format XML digunakan untuk membuat laporan terperinci tentang pemindaian yang dilakukan, termasuk informasi mengenai host, port, dan kerentanan yang terdeteksi, serta informasi tambahan yang tidak ditampilkan dalam keluaran standar Nmap.

Untuk generate file output dalam format XML, kita perlu menggunakan opsi `-oX` ("O" dari "XML"):

```
# Simpan keluaran Nmap ke berkas dalam format XML
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```

_Hasilnya adalah keluaran standar Nmap di terminal Anda, serta sebuah file dalam format XML di direktori Anda saat ini._

Meskipun format XML tidak dirancang untuk dibaca dan ditafsirkan oleh manusia. Namun demikian, jika Anda ingin melakukan skrip atau analisis otomatis pada format keluaran Nmap ini, Anda perlu memiliki gambaran tentang tag dan struktur yang digunakan. Contoh berikut adalah sebagian dari isi file XML yang dibuat oleh Nmap, yang menunjukkan hasil pemindaian untuk 1 host:

![nmap-image](assets/fr/51.webp)

_contoh catatan XML untuk 1 host selama pemindaian Nmap_

Ada banyak informasi di sini, dan kita sangat tertarik dengan dua port terbuka:

```
<port protocol="tcp" portid="21"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="ftp" product="Microsoft ftpd" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:ftp_service</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<port protocol="tcp" portid="80"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="http" product="Microsoft IIS httpd" version="7.5" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```

Kita dapat melihat banyak informasi di sini, dan kita sangat tertarik pada dua port yang terbuka. Informasi diatur dalam tag-tag yang rapi, yang memfasilitasi analisis otomatis. Kita juga menemukan bagian informasi yang sebelumnya belum kita temui: CPE.

```
cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```

Kita telah secara singkat menyebutkan CPE di bagian 2 modul 2, dan informasi ini ditentukan dalam kecocokan selama deteksi versi. Nmap menggunakan mekanisme deteksi layanan, teknologi, dan versinya untuk menemukan CPE yang terkait.

Ini memungkinkan kita untuk menggunakan kembali informasi ini dengan database dan aplikasi yang menggunakannya. Secara khusus, saya memikirkan database NVD, yang merujuk CVE. Untuk setiap CVE, basis data ini berisi CPE yang terkena dampak kerentanan. Berikut adalah contoh CVE yang berkaitan dengan `a:microsoft:internet_information_services:7.5` dari database NVD:

![nmap-image](assets/fr/52.webp)

_adanya CPE dalam rincian CVE di database NVD_

Dengan pemahaman ini, kita sekarang tahu bahwa format XML menawarkan struktur informasi yang sangat jelas dan berisi semua data yang dikumpulkan atau diproses oleh Nmap.

Sebagai kebiasaan, saya secara sistematis menyimpan hasil pemindaian Nmap saya dalam ketiga format sekaligus. Hal ini dimungkinkan oleh opsi `-oA <nama>` ("A" untuk "Semua"), yang akan membuat file `<nama>.nmap`, file `<nama>.xml`, dan file `<nama>.gnmap`. Dengan cara ini, saya yakin tidak akan kekurangan data apa pun saat perlu meninjau kembali hasilnya.

Dengan ketiga format ini, Anda memiliki semua yang dibutuhkan untuk menyimpan dan memproses hasil Nmap secara otomatis. Kita akan menggunakan format XML lagi di bagian selanjutnya, ketika kita melihat cara menggunakan Nmap dengan aplikasi keamanan lainnya.

#### III. Membuat laporan HTML dari pemindaian Nmap

Format XML menawarkan banyak kemungkinan, salah satunya adalah berfungsi sebagai dasar untuk membuat laporan dalam format HTML, yang akan lebih menarik secara visual.

Untuk mengubah file Nmap dalam format XML menjadi halaman web, kita akan menggunakan aplikasi `xsltproc`, yang harus kita instal terlebih dahulu.

```
# Install the xsltproc tool
sudo apt install xsltproc
```

Setelah aplikasi ini diinstal, cukup berikan file XML yang akan dikonversi dan nama laporan HTML yang akan dihasilkan:

```
# Membuat HTML laporan Nmap dari XML 
xsltproc nmap_10.10.10.0.xml -o "Nmap – rapport web 05-2024.html"

# Buka file .html dengan Firefox
firefox "Nmap – rapport web 05-2024.html"
```

Hasilnya, seluruh hasil pemindaian kita akan terstruktur dengan baik, bahkan dengan beberapa warna dan tautan yang dapat diklik dalam daftar isi!

![nmap-image](assets/fr/53.webp)

_ekstrak dari laporan pemindaian Nmap dalam format HTML yang dihasilkan oleh xsltproc._

Secara umum, file XML yang disimpan oleh Nmap berisi referensi ke file lain dalam format XML:

```
<?xml-stylesheet href="/usr/share/nmap/nmap.xsl" type="text/xsl"?>
```

Oleh karena itu, konversi ke HTML merupakan fungsi yang disediakan dan difasilitasi oleh Nmap, `xsltproc` merupakan aplikasi yang umum dan dikenal untuk melakukan tugas ini (yang tidak berasal dari paket aplikasi Nmap).

XSLT (_Extensible Stylesheet Language Transformations_) adalah bagian dari XSL yang memungkinkan data XML ditampilkan pada halaman web dan "ditransformasikan", secara paralel dengan gaya XSL, menjadi informasi yang dapat dibaca dan diformat dalam format HTML.

sumber: [helpx.adobe.com/](https://helpx.adobe.com/fr/dreamweaver/using/xml-xslt.html)_

Tingkat informasi dalam laporan ini setara dengan format XML Nmap dan lebih baik daripada output terminal standar (_output interaktif_).

### IV. Mengelola tingkat verbositas Nmap

Sekarang kita akan melihat beberapa opsi untuk Debugger Nmap atau untuk melacak kemajuannya.

Opsi pertama yang harus kita sebutkan adalah opsi `-v`, yang meningkatkan verbositas Nmap. Berikut ini sebuah contoh:

![nmap-image](assets/fr/54.webp)

_output verbose nmap menggunakan opsi `-v`._

Pada pemindaian yang menargetkan banyak host dan port, keluaran terminal akan sulit untuk dieksploitasi karena banyaknya informasi yang ditampilkan. Oleh karena itu, opsi ini harus digunakan bersamaan dengan opsi yang sudah dibahas sebelumnya, yang memungkinkan Anda menyimpan keluaran standar Nmap dalam file. Informasi terkait penggunaan verbosity (tingkat detail) tidak akan disertakan dalam fi;e keluaran ini. Seperti yang Anda lihat dari contoh sebelumnya, tingkat detail ini memungkinkan Anda untuk melacak tindakan dan penemuan Nmap secara langsung. Untuk pemindaian yang lebih lama di mana tampilan data mungkin lambat, ini menghindari Anda dari "buta" terhadap aktivitas Nmap saat ini dan mengetahui bahwa pemindaian sedang berjalan. Untuk meningkatkan tingkat detail lebih lanjut, Anda dapat menggunakan opsi `-vv`.

Untuk melacak aktivitas Nmap lebih jauh selama pemindaian, Anda dapat menggunakan opsi `--packet-trace`. Dengan opsi `-v`, kita mendapatkan log langsung dari semua port terbuka yang ditemukan oleh Nmap, sedangkan dengan opsi ini, kita mendapatkan baris log untuk setiap paket yang dikirim ke sebuah port. Ini secara alami menghasilkan keluaran yang sangat bertele-tele, tetapi memungkinkan pemantauan detail dari aktivitas Nmap. Berikut adalah contohnya:

![nmap-image](assets/fr/55.webp)

_pemantauan rinci aktivitas Nmap melalui `--packet-trace`._

Sekali lagi, informasi ini tidak akan direkam dalam file output yang dihasilkan oleh Nmap jika opsi `-oN`, `-oG`, `-oX` atau `-oA` digunakan.

Terakhir, Nmap juga menawarkan dua pilihan debug: `-d` dan `-dd`. Opsi-opsi ini berkerja mirip dengan opsi verbosity `-v`, tetapi menambahkan informasi teknis tambahan, seperti ringkasan parameter teknis pada awal pemindaian:

![nmap-image](assets/fr/56.webp)

_opsi waktu ditampilkan dalam tampilan debug Nmap_

Dalam beberapa bagian berikutnya, kita akan mencermati, apa saja opsi "Timing" dan mengapa kita perlu mengetahuinya.

Terakhir, jika Anda hanya ingin mendapatkan gambaran umum yang dasar dan ringkas tentang kemajuan pemindaian Nmap, Anda bisa menggunakan opsi `--stats-every 5s`. Angka "5s" di sini berarti 5 detik dan dapat diubah sesuai kebutuhan Anda. Ini adalah frekuensi di mana kita akan menerima umpan balik dari Nmap tentang kemajuannya:

![nmap-image](assets/fr/57.webp)

_informasi yang ditampilkan oleh opsi `--stats-every` dari Nmap_

Secara khusus, kita dapat mendapatkan persentase kemajuan, serta indikasi fase yang sedang dijalani, seperti: fase penemuan host melalui [ping](https://www.it-connect.fr/le-ping-pour-les-debutants/), fase penemuan port TCP yang terekspos, dan sebagainya. Informasi ini juga dapat diperoleh di keluaran terminal dengan menekan tombol "Enter" selama pemindaian.

Namun, Nmap tidak terlalu baik dalam memperkirakan berapa lama suatu tugas akan memakan waktu, terutama karena ia tidak tahu di awal berapa banyak host dan layanan yang harus dipindai.

### V. Kesimpulan

Di bagian ini, kita telah melihat sejumlah opsi untuk menyimpan hasil pemindaian Nmap dalam berbagai format file. Hal ini akan sangat berguna, karena dalam konteks nyata, hasil pemindaian dapat mencapai ratusan bahkan ribuan baris! Kita juga telah melihat cara meningkatkan tingkat verbositas Nmap untuk tujuan debugging atau untuk mendapatkan laporan kemajuan pemindaian.

Format XML akan sangat berguna pada bagian selanjutnya, di mana kita akan melihat beberapa aplikasi yang dapat bekerja dengan hasil Nmap.

## 10 - Menggunakan Nmap dengan alat keamanan lainnya

### I. Presentasi

Di bagian ini, kita akan melihat beberapa penggunaan klasik Nmap dengan aplikasi keamanan gratis dan open source lainnya. Secara khusus, kita akan menggunakan apa yang telah kita pelajari di bagian sebelumnya untuk lebih meningkatkan kekuatan dan efisiensi Nmap.

Kemampuan untuk menyimpan hasil pemindaian Nmap dalam format XML membuat data tersebut kompatibel dengan berbagai aplikasi lainnya. Karena hampir semua bahasa pemrograman dan skrip saat ini memiliki library yang mampu melakukan parsing XML, ini membuatnya jauh lebih mudah untuk memproses data. Sejumlah aplikasi, terutama yang berorientasi pada keamanan ofensif, memiliki fungsi untuk memproses format XML yang dihasilkan oleh Nmap. Mari kita lihat lebih dekat.

Saya akan menyebutkan beberapa aplikasi ofensif tanpa benar-benar merinci cara penggunaannya. Saya akan mengasumsikan bahwa pembaca sudah akrab dengan penggunaan dasar aplikasi tersebut dan sudah menginstalnya. Bagian ini akan sangat menarik bagi para profesional [keamanan siber](https://www.it-connect.fr/cours-tutoriels/securite-informatique/), mereka yang sedang menjalani pelatihan, atau mereka yang telah memutuskan untuk mendalami subjek ini lebih jauh.

### II. Mengimpor hasil Nmap ke Metasploit

Aplikasi pertama yang akan kita bahas untuk menggunakan kembali data Nmap dalam keamanan ofensif dan penelitian kerentanan adalah Metasploit.

Metasploit adalah kerangka kerja exploit dan serangan. Ini adalah solusi gratis dan Aplikasi yang diakui yang berisi sejumlah besar modul yang ditulis dalam Ruby atau Python. Modul-modul ini memungkinkan eksploitasi kerentanan, pelaksanaan serangan, pembuatan backdoor, pengelolaan callback (C&C atau Communication and Control), dan semua itu dapat digunakan secara seragam.

Secara khusus, kerangka kerja operasional yang banyak digunakan ini dapat bekerja dengan [database PostgreSQL](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) untuk menyimpan informasi host, port, layanan, informasi otentikasi, dan lainnya.

- Dokumentasi resmi Metasploit: [https://docs.metasploit.com/](https://docs.metasploit.com/)

Di sinilah Nmap dan keluarannya berperan, karena format XML dari keluaran Nmap dapat dengan mudah diimpor ke dalam database Metasploit untuk mengisi database host dan layanannya, yang kemudian dapat dengan cepat ditetapkan sebagai target serangan ini atau itu.

Setelah berada di shell interaktif Metasploit, saya mulai dengan membuat ruang kerja, semacam ruang yang khusus untuk lingkungan saya saat itu:

```
# Membuat sebuah Metasploit workspace
msf6 > workspace -a SI_siege
```

Setelah ruang kerja saya dibuat, kita perlu memvalidasi bahwa komunikasi dengan basis data sudah berjalan:

```
# Menerima status database
msf6 > db_status
[*] Connected to msf. Connection type: postgresql.
```

Terakhir, kita bisa menggunakan perintah Metasploit `db_import` untuk mengimpor pemindaian Nmap dalam format XML:

```
# Import file XML Nmap ke dalam database
msf6> db_import /tmp/nmap_10.10.10.0.xml
```

Berikut ini adalah hasil eksekusi semua perintah ini:

![nmap-image](assets/fr/58.webp)

_mengimpor pemindaian Nmap dalam format XML ke dalam basis data Metasploit_

Di sini Anda dapat melihat bahwa setiap host diimpor, bersama dengan layanannya. Data ini kemudian dapat ditampilkan melalui perintah `services` atau `services -p <port>` untuk layanan tertentu:

![nmap-image](assets/fr/59.webp)

_daftar layanan yang diimpor dari file XML ke dalam basis data Metasploit_

Terakhir, kita dapat dengan cepat dan mudah menggunakan kembali data ini di dalam sebuah module berkat opsi `-R`, yang akan "mengonversi" daftar layanan yang diperoleh menjadi masukan untuk direktif `RHOSTS`, yang digunakan untuk menentukan target serangan yang akan dilakukan. Berikut adalah contoh dengan module modul `ssh_login`, yang memungkinkan Anda untuk melakukan serangan brute force pada layanan [SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/):

![nmap-image](assets/fr/60.webp)

_gunakan opsi `services -R` untuk mengimpor layanan yang ditentukan sebagai target serangan_

Ini hanyalah contoh kecil dari apa yang bisa dilakukan dengan data Nmap di Metasploit, tetapi ini memberikan gambaran kecil tentang betapa cepat dan mudahnya informasi ini dapat digunakan kembali sebagai bagian dari penetration test, pemindaian kerentanan, atau serangan siber. Patut disebutkan juga bahwa Nmap dapat dijalankan langsung dari Metasploit untuk mengimpor hasilnya ke dalam database dengan (perintah `db_nmap`), yang merupakan topik menarik lain untuk dibahas!

### III. Menggunakan Nmap dengan pemindai web Aquatone

Aplikasi kedua yang ingin saya perkenalkan di bagian ini tentang penggunaan kembali hasil Nmap untuk keamanan ofensif dan analisis kerentanan adalah Aquatone.

Aquatone adalah pemindai web yang dirancang untuk menjelajahi aplikasi web pada sebuah jaringan secara efisien. Aplikasi ini menawarkan fitur-fitur canggih untuk penemuan layanan web, identifikasi subdomain, analisis port, dan fingerprinting aplikasi web. Semuanya disajikan secara jelas dan ringkas dalam laporan HTML, JSON, dan teks untuk memudahkan analisis keamanan web.

Sama seperti Metasploit, Aquatone dapat secara langsung memproses format XML dari Nmap dan menggunakannya sebagai target pemindaian. Secara khusus, Aquatone dapat mengekstrak hanya host dan layanan yang relevan (layanan web) dari semua data yang mungkin terkandung dalam laporan Nmap.

- Tautan Aquatone: [Github - Michenriksen/aquatone](https://github.com/michenriksen/aquatone)

Untuk menggunakan keluaran XML Nmap dengan Aquatone, cukup kirimkan file XML dalam sebuah pipe yang akan diproses oleh Aquatone. Berikut adalah contohnya:

```
# Mengirim outptu XML Nmap ke Aquatone
cat /tmp/nmap_10.10.10.0.xml | ./aquatone -nmap
```

Biasanya, Aquatone melakukan penemuan port pada host untuk menemukan layanan web. Namun, dalam konteks ini, Aquatone akan hanya mengandalkan hasil dari Nmap, yang telah melakukan operasi tersebut, sehingga menghemat waktu.

![nmap-image](assets/fr/61.webp)

_menggunakan hasil Nmap dalam format XML dengan `aquatone`._

Sebagai informasi, berikut ini adalah kutipan dari laporan yang dibuat oleh Aquatone:

![nmap-image](assets/fr/62.webp)

_contoh laporan `aquatone`_

Secara pribadi, saya sering menggunakan Aquatone untuk mendapatkan gambaran umum singkat tentang jenis situs web yang ada di jaringan, khususnya berkat fungsionalitas tangkapan layarnya.

Di sini sekali lagi, memiliki laporan Nmap yang lengkap dalam format XML akan menghemat waktu dan membuatnya mudah untuk digunakan kembali di aplikasi lain.

### IV. Kesimpulan

Kedua contoh ini dengan jelas menunjukkan bahwa format XML Nmap memudahkan aplikasi lain untuk menggunakan hasilnya, karena ini adalah format data yang terstruktur dan mudah digunakan. Ada banyak aplikasi lain yang mampu memproses hasil ini, seperti aplikasi pelaporan otomatis, representasi grafis, atau pemindai kerentanan yang lebih kompleks dan berpemilik.

Tentu saja, Anda juga dapat mengembangkan skrip dan aplikasi Anda sendiri di Python, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/), atau bahasa lain dengan library XML parsing untuk memanipulasi dan menggunakan kembali data hasil Nmap sesuai keinginan Anda.

Bagian ini membawa kita ke akhir modul tutorial tentang penggunaan Nmap yang lebih lanjut, khususnya untuk pemindaian kerentanan melalui skrip NSE.

Bagian tutorial berikutnya akan berfokus pada, antara lain, beberapa pengalaman terbaik dan kiat tambahan yang lebih teknis mengenai pemindaian spesifik yang dapat dilakukan oleh Nmap. Kita juga akan melihat opsi optimalisasi performa pemindaian, yang sangat berguna saat memindai jaringan besar.

## 11 - Meningkatkan kinerja pemindaian jaringan

### I. Presentasi

Di bab ini, kita akan belajar cara mengoptimalkan kecepatan pemindaian jaringan yang dilakukan dengan Nmap menggunakan berbagai opsi spesifik. Secara khusus, kita akan mempelajari lebih lanjut tentang cara kerja internal Nmap, mulai dari manajemen timeout hingga konfigurasi prasetel aplikasi.

Sekarang kita sudah memahami fitur-fitur Nmap dengan baik, mari kita mulai menguasai aplikasi canggih ini dan kekuatannya. Jika Anda pernah menggunakan aplikasi ini pada jaringan besar, Anda mungkin menyadari bahwa beberapa pemindaian bisa memakan waktu lama, meskipun aplikasi ini sangat kuat. Ada alasan kuat untuk itu: perintah nmap sederhana dengan beberapa opsi dapat menghasilkan jutaan paket yang menargetkan ratusan ribu potensi sistem dan layanan.

Selain itu, beberapa konfigurasi perangkat jaringan dapat dengan sengaja memaksakan laju yang lebih lambat (jumlah paket per detik), dengan risiko menolak paket Anda atau memblokir alamat IP Anda karena alasan keamanan.

Tergantung pada konteksnya, mengoptimalkan semua ini mungkin bermanfaat, seperti yang akan kita lihat di bab ini.

Bagaimanapun, Anda dapat memeriksa nilai default parameter yang akan kita lihat, serta apakah opsi yang akan Anda gunakan telah dipertimbangkan dengan benar, melalui mode debug Nmap (opsi `-d` yang terlihat pada bab sebelumnya):

![nmap-image](assets/fr/63.webp)

_melihat opsi Pengaturan waktu melalui opsi `-d` Nmap._

### II. Mengelola kecepatan pemindaian Nmap

#### A. Mengelola paralelisasi

Secara default, Nmap menggunakan paralelisasi dalam pemindaiannya untuk mengoptimalkan kinerja, dan semua parameter yang digunakannya dapat diubah melalui berbagai opsi. Namun, kasus di mana benar-benar perlu untuk memodifikasi parameter ini cukup jarang, jadi kita tidak akan membahasnya secara rinci dalam tutorial ini:

- `--min-hostgroup/max-hostgroup <size>`: ukuran grup pemindaian host paralel.
- `--min-paralelisme/max-paralelisme <numprobes>`: paralelisasi Probe.
- `--scan-delay/--max-scan-delay <time>`: menyesuaikan penundaan di antara Probe.

Ketahuilah bahwa mereka ada dan dapat digunakan.

#### B. Mengelola jumlah paket per detik

Secara default, Nmap sendiri menyesuaikan jumlah paket per detik yang dikirimnya sesuai dengan respons jaringan. Namun, dimungkinkan untuk memaksakan pengaturan ini dengan menentukan nilai maksimum dan/atau minimum dalam hal jumlah paket per detik. Pengaturan ini dilakukan menggunakan opsi `--min-rate <number>` dan `--max-rate <number>` di mana `number` mewakili jumlah paket per detik. Contoh:

```
# Batasi kecepatan pemindaian hingga 300 paket per detik
nmap -sV 10.10.10.0/24 --max-rate 300
```

Opsi-opsi ini memungkinkan Anda untuk menyesuaikan kecepatan pemindaian sesuai dengan kebutuhan spesifik Anda, baik untuk mempercepat proses maupun untuk membatasi penggunaan bandwidth. Kasus terakhir (membatasi kecepatan pemindaian) adalah yang paling mungkin membuat Anda menggunakan opsi ini, terutama jika Anda mengalami latensi jaringan saat menggunakan Nmap (yang cukup jarang terjadi).

### III. Mengelola kegagalan koneksi dan batas waktu

Parameter lain yang dapat kita ubah untuk mengoptimalkan kecepatan pemindaian Nmap (atau menjamin akurasi yang lebih besar) adalah _timeout_ dan _retry_.

Untuk _timeouts_, ini adalah **batas waktu tidak ada respons** setelah itu Nmap akan berhenti menunggu respons dan menganggap layanan atau host tidak dapat dijangkau. Untuk retry, ini adalah **jumlah percobaan berturut-turut pada suatu operasi** yang akan dilakukan Nmap sebelum beralih.

Sama seperti paralelisasi,  manajemen _timeout_ dan _retry_ dapat diterapkan pada fase penemuan host atau layanan:

- `--min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <time>`: Menentukan waktu perjalanan bolak-balik (round-trip time) dari suatu pertukaran. Sekali lagi, parameter ini sebenarnya dihitung dan disesuaikan secara otomatis selama pemindaian. Kecil kemungkinan Anda perlu menggunakannya, karena Nmap menghitung waktu ini secara instan sesuai dengan respons jaringan.
- `--max-retries <number>`: Membatasi jumlah pengiriman ulang paket selama pemindaian port. Secara default, Nmap dapat melakukan hingga 10 percobaan ulang untuk satu layanan, terutama jika menemukan latensi atau kehilangan pada tingkat jaringan, tetapi dalam banyak kasus, hanya satu yang dilakukan.
- `--host-timeout <time>`: Menentukan waktu maksimum yang akan dihabiskan Nmap pada satu host untuk semua operasinya, termasuk pemindaian port, deteksi layanan, dan operasi lain yang terkait dengan host tersebut. Jika batas waktu ini terlampaui tanpa respons atau **penyelesaian operasi**, Nmap akan mengabaikan host ini tanpa menampilkan hasil apa pun dan beralih ke host berikutnya dalam daftarnya. Ini memungkinkan Anda untuk mengontrol waktu maksimum yang dihabiskan Nmap pada host tertentu, menghindari pemindaian yang "terjebak" pada host yang tidak responsif, dan mengoptimalkan waktu pemindaian secara keseluruhan.

Dalam pekerjaan saya sehari-hari, saya menggunakan opsi `--max-retries` dan `--host-timeout` untuk mengoptimalkan pemindaian saya:

```
# Optimalisasi pemindaian diisi 0 upaya tambahan dan batas waktu 15 menit per host
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m
```

Parameter-parameter ini menawarkan fleksibilitas tambahan untuk menyesuaikan perilaku pemindaian dengan kebutuhan spesifik dan kondisi jaringan. Namun, Anda perlu menyadari implikasinya terkait beban pada host yang dipindai dan potensi hilangnya akurasi.

### IV. Penggunaan konfigurasi yang telah disiapkan

Berbagai opsi yang telah kita lihat di bab ini dapat digunakan secara individual atau sebagai bagian dari konfigurasi siap pakai yang ditawarkan oleh Nmap. Opsi yang memungkinkan penggunaan _templates_ (template konfigurasi) ini digunakan adalah `-T <number>` atau `-T <nama>`. Terdapat 5 level _templates_ yang dapat digunakan:

```
-T<0-5>: Set timing template (higher is faster)
```

Secara default, Nmap menggunakan _template_ 3 (_normal_), yang secara umum sudah cukup.

Bagi saya pribadi, saya umumnya beroperasi dalam konteks di mana saya perlu cukup cepat (sambil tetap selengkap mungkin), dan saya sering menggunakan opsi `-T4`.

```
# Gunakan Nmap untuk pemindaian jaringan dengan T4 yang telah ditetapkan (dengan debug)
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```

Berikut ini adalah informasi debug untuk pemindaian ini yang ditunjukkan kepada kita:

![nmap-image](assets/fr/64.webp)

_penggunaan pengaturan `-T4` selama pemindaian Nmap_

### V. Kesimpulan

Di bab ini, kita telah melihat berbagai teknik dan opsi yang dapat Anda gunakan untuk mengelola kekuatan, agresivitas, dan performa Nmap. Opsi-opsi ini sangat berguna saat memindai jaringan besar, dan lebih jarang untuk tujuan stealth.

Di bab berikutnya, kita akan melihat beberapa pengalaman terbaik untuk menggunakan Nmap dan memastikan keamanannya.

## 12 - Keamanan dan kerahasiaan data saat menggunakan Nmap

### I. Presentasi

Di bab ini, kita akan melihat sejumlah praktik baik yang harus diterapkan terkait dengan keamanan dan, yang terpenting, kerahasiaan data yang dihasilkan, diproses, dan disimpan oleh Nmap.

Penggunaan Nmap dalam sebuah sistem informasi dapat dengan cepat dikategorikan sebagai tindakan ofensif. Oleh karena itu, sejumlah tindakan pencegahan perlu diambil untuk bertindak dalam kerangka hukum, sambil menjamin keamanan target yang dituju, data yang dikumpulkan, dan sistem yang digunakan untuk pemindaian.

### II. Memperoleh otorisasi yang sesuai

Sebelum memindai jaringan atau sistem, pastikan Anda telah memperoleh izin yang sesuai. Memindai sistem untuk mencari kerentanan (`skrip NSE`) tanpa otorisasi bisa jadi ilegal dan dapat memiliki konsekuensi hukum, terutama jika keamanan sistem informasi bukan bagian dari tanggung jawab resmi Anda.

- Sebagai pengingat: [KUHP: Bab III: Serangan terhadap sistem pemrosesan data otomatis](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)

### III. Melindungi data sensitif

Hasil yang dihasilkan oleh Nmap dapat dianggap sensitif, terutama ketika berisi informasi tentang kelemahan dalam sistem informasi yang dapat dieksploitasi oleh penyerang. Hal ini juga berlaku ketika hasil tersebut berkaitan dengan sistem yang tidak dapat diakses oleh semua orang (misalnya, sistem informasi sensitif, industri, perawatan kesehatan, atau cadangan).

Kita juga telah melihat bahwa, tergantung pada skrip NSE yang digunakan, hasil pemindaian Nmap juga dapat berisi identifier. 

Dengan demikian, individu jahat yang berhasil mendapatkan akses ke hasil pemindaian ini akan memiliki peta sistem informasi dan banyak informasi teknis tanpa harus melakukan tindakan tersebut sendiri, yang berisiko terdeteksi.

Oleh karena itu, penting untuk berhati-hati agar tidak mengumpulkan atau menyimpan secara tidak tepat informasi sensitif saat menggunakan Nmap, seperti hal-hal seperti ini (namun tidak terbatas pada hal-hal berikut):

- Mengenkripsi data keluaran: Jika Anda perlu menyimpan atau mengirimkan hasil pemindaian Nmap Anda, pastikan untuk mengenkripsinya guna melindungi kerahasiaan data. Ini akan mencegah intersepsi informasi sensitif yang tidak sah. Idealnya, data harus dienkripsi segera setelah meninggalkan sistem yang digunakan untuk melakukan pemindaian (sebuah arsip ZIP yang dienkripsi dengan kata sandi yang kuat adalah awal yang sangat baik).
- Siapkan kontrol akses: Pastikan hanya orang yang berwenang yang memiliki akses ke hasil pemindaian Nmap di mana akan disimpan. Atur kontrol akses yang sesuai untuk melindungi informasi sensitif dari akses yang tidak sah.
- Kewaspadaan saat menangani data: Saat mentransitkan, menyalin, atau memproses data pemindaian, pastikan Anda menjaga keamanan data di bawah kendali yang ketat. Ini berarti: jangan biarkan data tergeletak di direktori `Download` pada workstation yang terhubung ke Internet, jangan biarkan data transit melalui aplikasi pertukaran file HTTP internal Anda, jangan biarkan Notepad Anda terbuka tanpa mengunci workstation selama istirahat makan siang Anda, dll.


### IV. Mengelola pemindaian agresif

Seperti yang telah kita lihat di seluruh tutorial ini, Nmap bisa sangat bertele-tele di tingkat jaringan. Nmap juga dapat mengirim paket yang tidak diformat dengan benar, dan yang tidak secara ketat mengikuti struktur protokol dalam bingkai dan paket jaringan yang dihasilkannya. Semua tindakan ini dapat berdampak pada sistem dan layanan tertentu, kadang-kadang hingga menyebabkan malfungsi atau kejenuhan sumber daya sistem dan jaringan.

Untuk menghindari insiden apa pun, Anda perlu menguasai dan menganalisis perilaku Nmap dan tahu cara menyesuaikannya dengan konteks di mana akan digunakan, melalui berbagai opsi yang dibahas dalam tutorial ini. Kita tidak akan selalu menggunakan Nmap dengan cara yang sama pada sistem informasi yang berisi [perangkat keras industri](https://www.it-connect.fr/actualites/actu-materiel/) seperti dalam jaringan pengguna yang terdiri dari sistem Windows yang dilindungi oleh firewall lokal atau di inti jaringan.

Semoga berbagai pelajaran dalam tutorial ini telah mengajari Anda cara menguasai dan menganalisis perilaku Nmap, tetapi cara terbaik untuk belajar adalah dengan melakukan. Jadi, pastikan Anda familiar dengan opsi Nmap yang akan Anda gunakan.

### V. Melindungi sistem pemindaian

Di bab pertama, kita melihat bahwa dalam banyak kasus, Nmap perlu dijalankan sebagai `root` atau administrator lokal. Ini karena Nmap melakukan operasi jaringan, terkadang pada level yang cukup rendah, melalui library jaringan, yang memerlukan izin tinggi dan berisiko dari sudut pandang stabilitas sistem atau kerahasiaan aplikasi lain.

Akibatnya, Nmap dapat dianggap sebagai komponen yang sensitif pada sistem tempat Nmap dipasang. Pastikan untuk menggunakan versi Nmap terbaru, karena versi yang lebih lama mungkin mengandung kerentanan keamanan yang sudah diketahui. Dengan menggunakan versi terbaru, Anda dapat meminimalkan risiko yang terkait dengan penggunaan Nmap ini.

Jika Anda memilih untuk menggunakan Nmap tidak melalui sesi sebagai `root`, tetapi dengan memberikan hak istimewa khusus kepada pengguna yang memiliki semua yang Nmap butuhkan untuk menggunakan Nmap (`sudo` atau capabilities), ketahuilah bahwa Nmap dapat digunakan sebagai bagian dari peningkatan hak istimewa yang lengkap:

![nmap-image](assets/fr/65.webp)

_peningkatan hak istimewa Nmap melalui `sudo`._

Di sini, saya menggunakan perintah Nmap melalui `sudo`, namun ini memungkinkan saya untuk mendapatkan shell interaktif sebagai `root` pada sistem, padahal itu bukan tujuan awalnya.

Sangat tidak disarankan juga untuk memasang Nmap pada sistem yang tidak dirancang untuk melakukan pemindaian jaringan. Saya secara khusus memikirkan server atau workstation. Di satu sisi, ini akan menambah potensi celah untuk peningkatan hak istimewa, tetapi di atas semua itu, ini akan memberikan penyerang akses mudah ke aplikasi ofensif.

Terakhir, keamanan sistem yang digunakan untuk pemindaian harus dipastikan secara lebih luas, agar sistem itu sendiri tidak menjadi celah penyusupan atau kebocoran informasi. Sebagai seorang administrator sistem, lebih baik menggunakan sistem khusus, idealnya dengan masa pakai terbatas, daripada workstation Anda sendiri.

### VI. Kesimpulan

Sebagai kesimpulan, pastikan Anda telah menguasai Nmap dengan baik sebelum menggunakannya dalam kondisi nyata atau produksi, dan bersikaplah waspada saat memproses dan mengelola hasilnya. Akan sangat disayangkan jika Anda menyebabkan kerusakan, membocorkan data, atau memfasilitasi penyusupan, padahal pendekatan awal Anda bertujuan untuk meningkatkan keamanan perusahaan.

## 13 - Pemindaian port melalui TCP: SYN, Connect, dan FIN

### I. Presentasi

Di bab ini dan bab berikutnya, kita akan melihat lebih dekat berbagai jenis pemindaian TCP yang tersedia di Nmap, dimulai dengan yang paling umum digunakan: pemindaian SYN, Connect, dan FIN.

Seperti yang mungkin sudah Anda perhatikan, Nmap menawarkan beberapa opsi untuk pemindaian TCP:

![nmap-image](assets/fr/66.webp)

_teknik pemindaian yang tersedia di Nmap._

Tujuannya di sini adalah untuk menjelaskan beberapa metode ini, untuk membantu Anda memahami perbedaan, keunggulan, dan keterbatasannya. Anda akan melihat bahwa, tergantung pada konteks atau apa yang ingin Anda ketahui, lebih baik memilih salah satu opsi dibandingkan yang lain.

### II. Pemindaian TCP SYN atau "Pemindaian Setengah Terbuka"

Jenis pemindaian TCP pertama yang akan kita lihat adalah `SYN TCP Scan`, yang juga dikenal sebagai `Half Open Scan`. Jika Anda mengingat pemindaian jaringan yang kita lakukan setelah pemindaian port pertama kita, ini adalah jenis pemindaian yang secara default digunakan oleh [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) saat dijalankan dengan hak root.

Penjelasan ini akan membantu Anda memahami cara kerja pemindaian ini. Faktanya, pemindaian SYN TCP akan mengirimkan paket SYN TCP ke setiap port yang ditargetkan, yang merupakan paket pertama yang dikirimkan oleh klien (pihak yang meminta untuk membuat koneksi) sebagai bagian dari jabat tangan tiga arah TCP yang terkenal. Biasanya, jika port terbuka pada server target, dengan layanan yang berjalan di belakangnya, server akan mengirimkan kembali paket SYN/ACK TCP untuk memvalidasi SYN klien dan menginisialisasi koneksi TCP. Respons ini berbentuk paket TCP dengan flag SYN dan ACK diatur ke 1, memungkinkan kita untuk mengonfirmasi bahwa port terbuka dan mengarah ke layanan.

Di sisi lain, jika port tertutup, server akan mengirimkan paket TCP kepada kita dengan flag RST dan ACK diatur ke 1 untuk mengakhiri permintaan koneksi, sehingga kita akan tahu bahwa tidak ada layanan yang tampaknya aktif di belakang port ini:

![nmap-image](assets/fr/67.webp)

_diagram perilaku Pemindaian tCP SYN untuk port terbuka dan tertutup_

Untuk mendapatkan gambaran yang lebih nyata tentang `TCP SYN Scan`, saya melakukan pemindaian port TCP/80 ke host yang memiliki server web aktif pada port ini. Menjalankan pemindaian jaringan dengan Wireshark, kami dapat melihat alur berikut (sumber pemindaian: `10.10.14.84`):

![nmap-image](assets/fr/68.webp)

_Pengambilan data jaringan selama pemindaian TCP SYN untuk port terbuka_

Pada baris pertama, kita melihat bahwa sumber pemindaian mengirimkan paket TCP ke host `10.10.10.203` pada port TCP/80. Dalam paket TCP ini, flag SYN diatur ke 1 untuk menandakan bahwa ini adalah permintaan inisialisasi koneksi TCP.

Kemudian, pada baris kedua, kita melihat bahwa target merespons dengan `TCP SYN/ACK`, yang berarti ia menerima untuk menginisialisasi koneksi dan karenanya menerima aliran data pada port TCP/80. Kita dapat menyimpulkan bahwa port TCP/80 terbuka dan server web ada pada server yang dipindai.

Host kita kemudian mengirim kembali paket RST untuk menutup koneksi, memungkinkan host yang dipindai tidak mempertahankan koneksi TCP terbuka yang menunggu respons. Dalam kasus pemindaian pada banyak port, tidak menutup koneksi TCP dapat menyebabkan penolakan layanan, dengan menjenuhkan jumlah koneksi yang menunggu untuk dijawab oleh server  (lihat [Wikipedia - Syn flood](https://fr.wikipedia.org/wiki/SYN_flood))

Di Wireshark, Anda akan dapat melihat status flag TCP untuk setiap uji coba yang kita lakukan. Ini akan menunjukkan apakah paket tersebut adalah paket SYN, SYN/ACK, ACK, dan sebagainya:

![nmap-image](assets/fr/69.webp)

_melihat bendera TCP sebuah paket di Wireshark (TCP SYN di sini)_

Sebaliknya, saya menjalankan pengujian yang sama antara kedua perangkat, tetapi kali ini memindai port TCP/81 yang tidak ada layanan yang aktif (sumber pemindaian: `10.10.14.84`):

![nmap-image](assets/fr/70.webp)

_Pengambilan data jaringan selama pemindaian TCP SYN untuk port tertutup_

Host yang dipindai mengembalikan `TCP RST/ACK` sebagai respons terhadap `TCP SYN` ketika port tidak terbuka.

Seperti yang telah disebutkan, saat menjalankan Nmap dari terminal istimewa, TCP SYN Scan adalah mode default, dan dapat dipaksakan melalui opsi `-sS` (`scan SYN`):

```
# Eksekusi Pemindaian Sinkronisasi TCP
nmap -sS 192.168.1.15
```

`TCP SYN Scan` adalah pemindaian yang paling umum digunakan karena alasan kecepatan. Di sisi lain, kegagalan klien untuk menyelesaikan _Three Way Handshake_ (yaitu tidak mengirim ACK setelah server SYN/ACK) mungkin terlihat mencurigakan jika diamati terlalu sering pada server atau dari sumber yang sama di jaringan. Padahal, perilaku normal klien setelah menerima paket TCP SYN/ACK sebagai respons terhadap SYN TCP adalah mengirimkan `acknowledgement` (ACK) dan kemudian memulai pertukaran.

Meskipun demikian, pemindaian ini memang memberikan kecepatan yang sedikit lebih tinggi, karena tidak perlu repot-repot mengirimkan ACK untuk setiap respons positif. Keuntungan dari SYN Scan adalah kecepatannya, karena hanya satu paket yang dikirim per port yang dipindai, dengan risiko kemungkinan deteksi yang lebih besar.

Selain itu, pemindaian TCP SYN Scan mampu mendeteksi apakah suatu port disaring (dilindungi) oleh firewall. Faktanya, firewall di depan host target dapat dideteksi dari perilakunya saat menerima paket SYN TCP pada port yang seharusnya  dilindungi. Firewall tidak akan merespons sama sekali. Padahal, seperti yang telah kita lihat, dalam dua kasus (baik port terbuka atau tertutup), ada respons dari host. Perilaku ketiga ini akan mengungkapkan keberadaan firewall di antara host yang dipindai dan perangkat yang melakukan pemindaian. Berikut adalah hasil yang dapat dikembalikan Nmap ketika port yang dipindai disaring oleh firewall:

![nmap-image](assets/fr/71.webp)

_tampilan nmap saat memindai port yang difilter_

Ketika kita melakukan Pengambilan data jaringan pada waktu pemindaian, kita dapat melihat bahwa tidak ada respons yang diberikan:

![nmap-image](assets/fr/72.webp)

_Pengambilan data jaringan selama pemindaian TCP SYN untuk port yang difilter oleh firewall_

Perbedaan antara port tertutup dan port tersaring adalah sebagai berikut: port difilter adalah port yang dilindungi oleh firewall, sedangkan port tertutup adalah port di mana tidak ada layanan yang berjalan dan oleh karena itu tidak dapat memproses paket TCP kita. Beberapa jenis pemindaian TCP, seperti TCP SYN scan, mampu mendeteksi apakah sebuah port tersaring, sementara jenis pemindaian lainnya tidak bisa.

### III. Pemindaian TCP Connect atau Pemindaian Terbuka Penuh

Jenis pemindaian TCP kedua adalah 'TCP Connect scan', juga dikenal sebagai `Full Open Scan`. Pemindaian ini bekerja dengan cara yang sama seperti TCP SYN scan, tetapi kali ini ia mengembalikan `TCP ACK` setelah respons positif dari server (SYN/ACK). Inilah sebabnya mengapa pemindaian ini disebut `Full Open`, karena koneksi dibuka sepenuhnya dan diinisiasi pada setiap port yang terbuka selama pemindaian, sehingga mematuhi TCP _Three Way Handshake_.

![nmap-image](assets/fr/73.webp)

_diagram perilaku Pemindaian tCP Connect untuk port terbuka dan tertutup_

Berikut ini adalah apa yang terlihat saat transit jaringan selama `TCP Connect scan` yang menargetkan port terbuka:

![nmap-image](assets/fr/74.webp)

_mengamati jaringan selama pemindaian TCP Connect untuk port yang terbuka_

Kita dapat melihat bahwa paket TCP pertama yang dikirim adalah `TCP SYN` yang dikirim oleh klien, dan server kemudian akan membalas dengan `TCP SYN/ACK`, yang menunjukkan bahwa port terbuka dan meng-host layanan yang aktif. Nmap kemudian akan mengirimkan `TCP ACK` kembali ke server untuk menyimulasikan klien yang sah secara utuh. Sebaliknya, saat memindai port tertutup:

![nmap-image](assets/fr/75.webp)

_Pengambilan data jaringan selama pemindaian TCP Connect untuk port tertutup_

Perhatikan bahwa respons server terhadap paket `SYN` kita sekali lagi adalah paket `TCP RST/ACK`, sehingga kita dapat menyimpulkan bahwa port tersebut ditutup dan tidak ada layanan yang berjalan di dalamnya.

Saat menggunakan Nmap, opsi `-sT` (`scan Connect`) digunakan untuk melakukan TCP Connect scan. Harap diperhatikan bahwa bila Nmap digunakan dari sesi yang tidak diistimewakan, ini adalah mode pemindaian TCP default:

```
# Esekusi dari TCP Connect Scan
nmap -sT 192.168.1.15
```

`TCP Connect Scan` menyimulasikan permintaan koneksi yang lebih sah, dengan perilaku yang paling mirip dengan klien biasa, sehingga lebih sulit untuk mendeteksi pemindaian pada sejumlah kecil port. Namun, pemindaian ini lebih lambat karena sepenuhnya menginisialisasi setiap koneksi TCP pada port yang terbuka dari perangkat yang dipindai.

Pemindaian Nmap terhadap 10.000 port akan tetap mudah dideteksi jika layanan deteksi dan perlindungan intrusi jaringan (IDS, IPS, EDR) terpasang. Ketika seorang penyerang ingin menjaga low profile, ia akan cenderung berfokus pada sejumlah kecil port yang dipilih secara strategis, seperti 445 (SMB) atau 80 (HTTP), yang sering terbuka pada server dan memiliki kerentanan umum.

Karena TCP Connect Scan mengharapkan respons dalam kedua kasus (terbuka atau tertutup), pemindaian ini juga dapat mendeteksi keberadaan firewall yang mungkin memfilter port pada host target.

### IV. TCP FIN scan or "Stealth Scan"

TCP FIN Scan, juga dikenal sebagai Stealth Scan, menggunakan perilaku klien yang mengakhiri koneksi TCP untuk mendeteksi port yang terbuka.

Dalam TCP, akhir sesi berarti mengirimkan paket TCP dengan flag FIN diatur ke 1. Dalam pertukaran normal, server menghentikan semua komunikasi dengan klien (tidak ada respons). Jika server tidak memiliki koneksi TCP yang aktif dengan klien, server akan mengirimkan `RST/ACK`. Oleh karena itu, kita dapat membedakan antara port terbuka dan tertutup dengan mengirimkan paket `FIN TCP` ke sejumlah port.

![nmap-image](assets/fr/76.webp)

_diagram perilaku pemindaian TCP FIN untuk port terbuka dan tertutup_

Saya kembali menangkap jaringan selama _Stealth scan_ dan inilah yang Anda lihat ketika port yang dipindai terbuka:

![nmap-image](assets/fr/77.webp)

_Pengambilan data jaringan selama pemindaian TCP FIN untuk port terbuka_

Kita dapat melihat bahwa klien mengirimkan satu atau dua paket untuk mengakhiri koneksi TCP dan server tidak merespons. Server hanya menerima akhir koneksi dan berhenti berkomunikasi.

Inilah yang kita lihat sekarang ketika kita memindai port yang tertutup:

![nmap-image](assets/fr/78.webp)

_Pengambilan data jaringan selama pemindaian TCP FIN untuk port tertutup_

Kita melihat bahwa server mengirim kembali paket `TCP RST/ACK`, sehingga ada perbedaan perilaku antara port terbuka dan tertutup, dan kita dapat membuat daftar port yang terbuka pada server dengan mengirimkan paket TCP FIN. Menggunakan Nmap, opsi `-sF` (`scan FIN`) digunakan untuk melakukan TCP FIN Scan:

```
# Esekusi dari TCP Fin Scan
nmap -sF 192.168.1.15
```

TCP FIN Scan tidak berfungsi pada host Windows, karena OS cenderung mengabaikan paket TCP FIN ketika dikirim ke port yang tidak terbuka. Jadi, jika Anda menjalankan TCP FIN Scan pada host Windows, Anda akan mendapatkan kesan bahwa semua port tertutup.

Itulah mengapa penting untuk terbiasa dengan beberapa metode pemindaian, dan untuk memahami perbedaan di antara metode tersebut.

Karena dalam kedua kasus tersebut, TCP FIN tidak akan menunggu respons, maka ia tidak akan dapat mendeteksi keberadaan firewall antara host target dan sumber pemindaian.

Berikut adalah contoh hasil pemindaian TCP FIN dari Nmap:

![nmap-image](assets/fr/79.webp)

_hasil pemindaian TCP FIN oleh Nmap._
Faktanya, tidak adanya respons dari host pada port tertentu bisa berarti bahwa port tersebut difilter, tetapi juga bisa berarti bahwa port tersebut terbuka dan aktif.

Pemindaian ini disebut sebagai "stealth", karena tidak menghasilkan banyak lalu lintas dan umumnya tidak menyebabkan pencatatan pada sistem yang ditargetkan. Pemindaian ini dapat digunakan untuk menemukan port secara diam-diam di jaringan tanpa memicu alarm apa pun. Namun, seperti yang disebutkan di atas, efektivitasnya dapat bervariasi tergantung pada sistem target, begitu juga kerahasiaannya tergantung pada konfigurasi peralatan keamanan.

### V. Kesimpulan

Demikianlah bab pertama dari dua bab tentang berbagai jenis pemindaian TCP yang ditawarkan oleh Nmap! Di bab berikutnya, kita akan melihat jenis pemindaian TCP XMAS, Null, dan ACK, yang beroperasi dengan cara berbeda untuk mendeteksi port yang terbuka pada sebuah host.

## 14 - Pemindaian port melalui TCP: XMAS, Null dan ACK

### I. Presentasi

Pada bagian ini, kita akan terus mengeksplorasi berbagai metode pemindaian TCP yang ditawarkan oleh Nmap. Di sini kita akan melihat metode `XMAS`, `Null` dan `ACK`, yang menggunakan fitur khusus TCP untuk mengambil informasi tentang port dan layanan yang terbuka pada target tertentu.

### II. TCP XMAS scan

XMAS Scan TCP tidak seperti biasanya karena sama sekali tidak menyimulasikan perilaku normal pengguna atau mesin pada jaringan. Faktanya, XMAS Scan akan mengirimkan paket TCP dengan flag `URG` (Urgent), `PSH` (push), dan `FIN` (Finish), untuk melewati firewall atau mekanisme pemfilteran tertentu.

Nama XMAS berasal dari fakta bahwa melihat flag ini menyala adalah hal yang tidak biasa. Ketika ketiga flag diatur secara bersamaan dalam paket TCP, paket itu terlihat seperti pohon Natal yang menyala.

![nmap-image](assets/fr/80.webp)

_bendera tCP yang digunakan dalam pemindaian XMAS_

Tanpa merinci peran flag-flag ini di sini, penting untuk diketahui bahwa saat mengirim paket dengan ketiga flag ini diaktifkan, layanan aktif di balik port target tidak akan mengembalikan paket apa pun. Di sisi lain, jika port tertutup, kita akan menerima paket TCP RST/ACK. Kita sekarang akan dapat membedakan antara perilaku port terbuka dan tertutup saat membuat daftar port pada sebuah perangkat.

![nmap-image](assets/fr/81.webp)

_diagram perilaku Pemindaian TCP XMAS untuk port terbuka dan tertutup_

Masih mengikuti logika yang sama, pemindaian jaringan pada port TCP/80 dari sebuah host dengan web server aktif menunjukkan perilaku berikut saat mendeteksi port terbuka (sumber pemindaian `10.10.14.84`):

![nmap-image](assets/fr/82.webp)

_Pengambilan data jaringan selama pemindaian TCP XMAS untuk port terbuka_

Kita dapat melihat bahwa sumber pemindaian mengirimkan dua paket TCP XMAS (dengan flag `FIN`, `PSH` dan `URG` diset ke 1) ke host `10.10.10.203` dan tidak ada respons dari target, yang menunjukkan bahwa port tersebut terbuka. Sebaliknya, saat melakukan TCP XMAS Scan pada port tertutup, hasil yang diamati sebagai berikut :

![nmap-image](assets/fr/83.webp)

_Pengambilan data jaringan selama pemindaian TCP XMAS untuk port tertutup_

Respon terhadap paket TCP kita adalah `TCP RST/ACK`, yang mengindikasikan bahwa port tersebut ditutup. Untuk menggunakan teknik ini dengan Nmap, opsi `-sX` (`scan XMAS`) memungkinkan Anda untuk melakukan Pemindaian TCP XMAS:

```bash
# Esekusi dari TCP XMAS Scan
nmap -sX 192.168.1.15
```

Penting untuk dicatat bahwa pemindaian TCP XMAS tidak mampu mendeteksi firewall yang mungkin berada di antara target dan perangkat pemindai, tidak seperti beberapa jenis pemindaian lain seperti TCP SYN atau Connect. Memang, firewall yang aktif di antara kedua host akan memastikan bahwa tidak ada respons TCP yang dibuat jika port yang ditargetkan disaring (yaitu, dilindungi oleh firewall). Jika terjadi tidak ada respons, oleh karena itu tidak mungkin untuk mengetahui apakah port tersebut dilindungi oleh firewall atau terbuka dan aktif. Anda juga harus menyadari bahwa, seperti TCP FIN Scan, aplikasi atau sistem operasi tertentu seperti Windows dapat mendistorsi hasilnya dari jenis pemindaian ini.

_Catatan: Dukungan untuk pemindaian XMAS/FIN/NULL pada versi Windows terbaru masih terbatas, dan hasilnya mungkin tidak konsisten pada jenis target ini. (Pembaruan 2025)_

### III. TCP Null scan

Berbeda dengan  TCP XMAS scan, TCP Null scan akan mengirimkan paket pemindaian TCP dengan semua flag diatur ke 0. Ini juga merupakan perilaku yang tidak akan pernah ditemukan dalam pertukaran normal antar perangkat, karena mengirimkan paket TCP tanpa flag tidak ditentukan dalam RFC yang menjelaskan protokol TCP. Inilah mengapa pemindaian ini dapat dideteksi lebih mudah.

Sama seperti TCP XMAS scan, pemindaian ini dapat mengganggu firewall atau modul pemfilteran tertentu, memungkinkan paket untuk melewatinya :

![nmap-image](assets/fr/84.webp)

_diagram perilaku TCP Null scan untuk port terbuka dan tertutup_

Berikut ini adalah apa yang dapat dilihat di jaringan selama TCP Null scan pada port terbuka:

![nmap-image](assets/fr/85.webp)

_Pengambilan data jaringan selama TCP Null scan untuk port terbuka_

Perangkat pemindaian mengirimkan paket tanpa bendera (`[<None>]` di Wireshark) tanpa respons apa pun dari server. Sebaliknya, ketika port target ditutup:

![nmap-image](assets/fr/86.webp)

_Pengambilan data jaringan selama pemindaian TCP Null untuk port tertutup_

Untuk melakukan TCP Null scan dengan Nmap, cukup gunakan opsi `-sN` (`pindai Null`):

```bash
# Esekusi dari TCP Null Scan
nmap -sN 192.168.1.15
```

Karena respons ketika sebuah port terbuka dan ketika firewall aktif (tidak ada umpan balik server dalam kedua kasus) adalah identik, TCP Null scan tidak mampu mendeteksi keberadaan firewall. Terlebih lagi, firewall bahkan dapat memalsukan hasilnya dengan menyarankan bahwa port terbuka, karena ia tidak merespons paket TCP tanpa flag, meskipun port tersebut difilter. Ini adalah informasi penting untuk disadari saat menggunakan pemindaian yang tidak mampu membedakan antara port terbuka dan yang disaring (dilindungi firewall), seperti pemindaian `TCP Null`, `XMAS`, atau `FIN`, agar tetap konsisten dalam menafsirkan hasil yang diperoleh.

### IV. TCP ACK scan

TCP ACK scan digunakan untuk mendeteksi keberadaan firewall pada host target atau antara target dan sumber pemindaian.

Tidak seperti pemindaian lainnya, TCP ACK scan tidak mencoba mengidentifikasi port mana yang terbuka pada host, melainkan apakah sistem pemfilteran aktif, dengan merespons setiap port dengan `filtered` atau `unfiltered`. Beberapa pemindaian TCP, seperti TCP SYN atau TCP Connect, dapat melakukan keduanya pada saat yang sama, sementara yang lain, seperti `TCP FIN` atau `TCP XMAS`, sama sekali tidak dapat menentukan keberadaan pemfilteran. Inilah mengapa TCP ACK scan dapat berguna.

![nmap-image](assets/fr/87.webp)

_diagram perilaku pemindaian ACK tCP untuk port yang difilter dan tidak difilter_

Kita akan menggunakan opsi `-sA` dari Nmap untuk melakukan jenis pemindaian ini. Berikut adalah hasil TCP ACK scan jika port difilter, yaitu diblokir dan dilindungi oleh firewall:

![nmap-image](assets/fr/88.webp)

_tampilan nmap selama Pemindaian TCP ACK._

Contoh hasil untuk host dengan firewall dan tanpa firewall. Nmap mengembalikan `filtered` pada port TCP/80 dan TCP/81 dari host `10.10.10.203`. Pada analisis jaringan melalui Wireshark, perilakunya adalah sebagai berikut:

![nmap-image](assets/fr/89.webp)

_Pengambilan data jaringan selama pemindaian TCP ACK untuk port yang tidak difilter oleh firewall_

Perangkat target tidak mengembalikan apa pun jika ada firewall.

Untuk menjalankan pemindaian ini dengan Nmap, gunakan opsi `-sA` (`scan ACK`):

```bash
# Esekusi dari TCP ACK Scan
nmap -sA 192.168.1.15
```

### V. Kesimpulan

Kita telah melihat tiga metode pemindaian berbeda melalui TCP selain yang telah disajikan sebelumnya. Metode-metode yang berbeda ini akan digunakan dalam kondisi dan konteks yang sangat spesifik, terutama dalam konteks uji penetrasi atau Red Team operations, di mana unsur kerahasiaan hadir.

## 15 - Nmap CheatSheet - Ringkasan perintah tutorial

### I. Presentasi

Berikut ini adalah ringkasan singkat dari banyak perintah dan kasus penggunaan Nmap, sehingga Anda dapat dengan cepat menemukan dan menggunakannya kembali dalam penggunaan sehari-hari.

### II. Nmap: CheatSheet IT-Connect

Berikut ini adalah lembar sontekan dari perintah-perintah yang disajikan. Halaman ini memudahkan untuk menemukan penggunaan Nmap yang paling umum.

- Pemindaian port

```bash
# Tampilkan versi Nmap yang terpasang
nmap --version

# Scan port spesifik yang terbuka pada satu alamat IP
nmap --open -p 80 192.168.1.18

# Scan port TCP pada pilihan port
nmap 192.168.1.19 -p 80
nmap 192.168.1.19 -p 22,80,1000-2000,3389

# Scan layanan UDP pada sebuah alamat IP
nmap -sU 192.168.1.19

# Scan layanan UDP pada port spesifik
nmap -sU 192.168.1.19 -p 161,23

# Scan 100 port TCP yang paling umum digunakan
nmap 192.168.1.19 --top-ports 100

# Scan semua port pada sebuah alamat IP
nmap 192.168.1.19 -p-

# Scan beberapa subnet dengan port spesifik
nmap 192.168.0.0/24 192.168.1.0/24 -p 22

# Scan sebuah subnet sambil mengecualikan alamat IP spesifik, Scan semua port
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```

- Menemukan host yang aktif

```bash
# Scan pada rentang CIDR atau IP
nmap 192.168.0.0/24
nmap 192.168.0.0/24 192.168.1.0/24
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20

# penemuan host (Ping Scan) pada sebuah jaringan
nmap -sn 192.168.1.0/24
```

_catatan: Opsi `-sP` sudah tidak digunakan lagi selama beberapa tahun dan sebaiknya diganti dengan `-sn`. (Pembaruan 2025)_

```bash
# Scan penemuan host tanpa pemindaian port
nmap 192.168.1.0/24 -sn

# Scan penemuan host pada jaringan lokal menggunakan berbagai teknik probe
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24

# Scan host yang terdaftar dalam berkas teks
nmap -iL /tmp/mesCibles.txt

# Scan jaringan dengan IP spesifik dikecualikan
nmap 192.168.1.0/24 --exclude 192.168.1.140

# Scan subnet yang mengecualikan subnet lain
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```

- Deteksi versi

```bash
# Aktifkan deteksi versi
nmap 192.168.1.0/24 -sV

# Deteksi versi + jejak lanjutan
nmap 192.168.1.0/24 -sV --version-trace

# Deteksi versi dengan kelangkaan probe maksimum 2
nmap 192.168.1.0/24 -sV --version-intensity 2

# Deteksi versi dengan semua probe
nmap 192.168.1.0/24 -sV --version-intensity 9

# Aktifkan deteksi OS
nmap -O 10.10.10.0/24
```

- Skrip NSE: mencari kerentanan

```bash
# Jalankan skrip NSE default
nmap -sC 10.10.10.152

# Scan semua port TCP dengan skrip NSE default
nmap -sC -p- 10.10.10.152

# Tampilkan bantuan untuk skrip berdasarkan nama
nmap --script-help=ftp-*

# Tampilkan bantuan untuk kategori
nmap --script-help=discovery

# Gunakan skrip NSE berdasarkan kategori
nmap --script default 10.10.10.152
nmap --script discovery 10.10.10.152

# Filter inklusi/eksklusi untuk kategori skrip NSE
nmap --script "discovery and safe" 10.10.10.152
nmap --script "not intrusive and not dos" 10.10.10.152
nmap --script "vuln and not intrusive and not dos" 10.10.10.152
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152

# Jalankan skrip NSE spesifik
nmap --script ftp-anon -p 21 10.10.10.152
nmap --script ftp-anon 10.10.10.152

# Teruskan argumen ke skrip NSE
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```

- Manajemen keluaran Nmap

```bash
# Simpan hasil scan ke berkas teks
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt

# Simpan hasil scan ke berkas teks yang padat
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap

# Simpan hasil scan ke berkas XML
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```

- Optimalisasi kinerja

```bash
# Scan deteksi versi dengan kecepatan maksimum 300 paket per detik
nmap -sV 10.10.10.0/24 --max-rate 300

# Scan deteksi versi dengan skrip default, tanpa percobaan ulang, batas waktu host maksimum 15 menit
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m

# Scan deteksi versi dengan 2000 port paling umum, kecepatan pemindaian agresif (T4), keluaran debug
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```

- Jenis pemindaian TCP

```bash
# TCP SYN scan (cepat, kurang tersembunyi)
nmap -sS 192.168.1.15

# TCP Connect scan (klasik)
nmap -sT 192.168.1.15

# TCP FIN scan (stealth)
nmap -sF 192.168.1.15

# TCP XMAS scan
nmap -sX 192.168.1.15

# TCP Null scan
nmap -sN 192.168.1.15

# TCP ACK scan (deteksi firewall)
nmap -sA 192.168.1.15
```

Saya harap Anda menemukan perintah-perintah berguna ini. Jangan lupa untuk menyesuaikan target pemindaian Anda dengan konteks Anda dan merujuk pada dokumentasi resmi untuk menguasai sepenuhnya uji coba yang dilakukan.

### III. Kesimpulan

Tutorial Nmap kini telah selesai. Anda sekarang memiliki dasar-dasar yang diperlukan untuk menggunakan aplikasi yang komprehensif dan kuat ini. Kami sangat menyarankan Anda untuk berlatih di lingkungan yang terkontrol (Hack The Box, VulnHub, virtual machines) sebelum menggunakannya di lingkungan produksi.

Masih banyak hal yang bisa dieksplorasi tentang cara kerja internal dan fitur-fitur canggih dari aplikasi ini. Namun, penguasaan perintah dan konsep yang disajikan di sini akan memungkinkan Anda untuk menggunakan Nmap dengan percaya diri dan relevan.
