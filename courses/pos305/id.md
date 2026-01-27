---
name: Menguasai BTC Pay Server
goal: Mengonfigurasi instance BTC Pay Server untuk bisnis lokal
objectives:
- Memahami dasar-dasar peran BTCPay Server dalam pemrosesan pembayaran
- Menguasai cara kerja internal proses konfigurasi BTCPay Server
- Men-deploy BTCPay Server di lingkungan cloud dan berbasis node
- Menjadi operator BTC Pay Server
---
# Perjalanan Menuju Kedaulatan Finansial

Kepercayaan itu rapuh, terutama dalam hal uang. Kursus pengantar ini memandu Anda melalui BTCPay Server, alat yang kuat yang memungkinkan Anda menerima pembayaran Bitcoin tanpa bergantung pada pihak ketiga. Anda akan mempelajari dasar-dasar menjadi operator BTCPay Server

Dibuat oleh Alekos dan Bas, dan diadaptasi oleh melontwist dan asi0, kursus ini mengungkapkan bagaimana individu dan bisnis membangun alternatif untuk sistem pembayaran tradisional. Baik Anda penasaran tentang Bitcoin atau siap menjalankan infrastruktur pembayaran untuk bisnis, Anda akan menemukan keterampilan praktis yang menantang status quo. Siap untuk menjelajahi seperti apa sebenarnya kemandirian finansial?
+++
# Pendahuluan


<partId>59e43fe3-b494-5da6-b4b4-9df5bdf08916</partId>


## Ikhtisar Kursus


<chapterId>785ed2bc-94ae-4962-a26a-edf5742a3c72</chapterId>


Selamat datang di kursus POS 305 di BTCPay Server!


Tujuan dari pelatihan ini adalah untuk mengajarkan Anda cara menginstal, mengonfigurasi, dan menggunakan BTCPay Server dalam bisnis atau organisasi Anda. BTCPay Server adalah solusi sumber terbuka yang memungkinkan Anda memproses pembayaran Bitcoin secara mandiri, aman, dan hemat biaya. Kursus ini terutama ditujukan untuk pengguna tingkat lanjut yang ingin menguasai BTCPay Server yang dapat dihosting sendiri untuk integrasi penuh ke dalam operasi harian mereka.


**Bagian 1: Pengantar Server BTCPay**

Kita akan mulai dengan presentasi umum BTCPay Server, termasuk layar login, manajemen akun pengguna, dan pembuatan toko baru. Pengenalan ini akan membantu Anda memahami BTCPay Server Interface dan memahami fitur-fitur dasar yang diperlukan untuk mulai menggunakan alat ini.


**Bagian 2: Pengantar Mengamankan Kunci Bitcoin**

Keamanan dana Bitcoin Anda sangat penting. Pada bagian ini, kita akan mempelajari pembuatan kunci kriptografi, penggunaan dompet perangkat keras untuk mengamankan kunci tersebut, dan cara berinteraksi dengan kunci Anda melalui BTCPay Server. Anda juga akan mempelajari cara mengonfigurasi BTCPay Server Lightning Wallet untuk mengoptimalkan transaksi Anda.


**Bagian 3: Server BTCPay Interface**

Bagian ini akan memandu Anda melalui pengguna BTCPay Server Interface. Anda akan mempelajari cara menavigasi dasbor, mengonfigurasi pengaturan toko dan server, mengelola pembayaran, dan memanfaatkan pengaya terintegrasi. Tujuannya adalah untuk memberi Anda alat yang diperlukan untuk menyesuaikan instalasi Anda sesuai dengan kebutuhan spesifik Anda.


**Bagian 4: Mengkonfigurasi Server BTCPay**

Terakhir, kita akan fokus pada instalasi praktis BTCPay Server di berbagai lingkungan. Baik Anda menggunakan LunaNode, Voltage, atau node Umbrel, Anda akan mempelajari langkah-langkah penting untuk menggunakan dan mengonfigurasi BTCPay Server Anda, dengan mempertimbangkan spesifikasi masing-masing lingkungan.


Siap menguasai BTCPay Server dan mengembangkan bisnis Anda? Mari kita mulai!


## Pujian kritis untuk Bitcoin dan Server BTCPay milik Penulis


<chapterId>e1fe6294-3c82-5203-9537-779f9087c35a</chapterId>


Mari kita mulai dengan memahami apa itu BTCPay Server dan asal-usulnya. Kami menghargai transparansi dan standar tertentu untuk membentuk kepercayaan dalam ruang Bitcoin.

Sebuah proyek di luar angkasa telah melanggar nilai-nilai ini. Pengembang utama BTCPay Server, Nicolas Dorier, menanggapi hal ini secara pribadi dan berjanji untuk tidak lagi menggunakannya. Di sinilah kita, bertahun-tahun kemudian, dan bekerja menuju masa depan ini, sepenuhnya open-source, setiap hari.


> Ini bohong, kepercayaanku padamu telah rusak, aku akan membuatmu usang.
> Nicolas Dorier

Setelah kata-kata yang diucapkan oleh Nicolas, tibalah saatnya untuk mulai membangun. Banyak sekali pekerjaan yang dilakukan untuk membangun apa yang sekarang kita sebut sebagai BTCPay Server. Banyak orang yang ingin berkontribusi dalam upaya ini. Yang paling dikenal adalah r0ckstardev, MrKukks, Pavlenex, dan pedagang pertama yang menggunakan perangkat lunak ini, astupidmoose.


Apa yang dimaksud dengan open source, dan apa saja yang ada di dalam proyek semacam itu?


FOSS adalah singkatan dari Perangkat Lunak Bebas & Sumber Terbuka. Yang pertama mengacu pada istilah yang mengizinkan siapa saja untuk menyalin, memodifikasi, dan bahkan mendistribusikan versi perangkat lunak (bahkan untuk mendapatkan keuntungan). Yang terakhir mengacu pada pembagian kode sumber secara terbuka, mendorong publik untuk berkontribusi dan memperbaikinya.

Hal ini menarik pengguna berpengalaman yang antusias untuk berkontribusi pada perangkat lunak yang telah mereka gunakan dan mendapatkan nilai dari perangkat lunak tersebut, yang pada akhirnya terbukti lebih berhasil dalam pengadopsiannya daripada perangkat lunak berpemilik. Hal ini sesuai dengan etos Bitcoin bahwa "informasi ingin bebas." FOSS menyatukan orang-orang yang bersemangat yang membentuk sebuah komunitas dan lebih menyenangkan. Seperti Bitcoin, FOSS tidak bisa dihindari.


### Sebelum kita mulai


Kursus ini terdiri dari beberapa bagian. Banyak hal yang akan diurus oleh guru kelas Anda, lingkungan Demo yang dapat Anda akses, server yang dihosting untuk Anda sendiri, dan mungkin nama domain. Jika Anda menyelesaikan kursus ini secara mandiri, perlu diketahui bahwa lingkungan berlabel DEMO tidak akan tersedia untuk Anda.

NB. Jika Anda mengikuti kursus ini di ruang kelas, nama server mungkin berbeda tergantung pada pengaturan ruang kelas Anda. Variabel dalam nama Server mungkin berbeda karena hal ini.


### Struktur Mata Kuliah


Setiap bab memiliki tujuan dan penilaian pengetahuan. Dalam kursus ini, kami akan membahas masing-masing dan memberikan ringkasan fitur-fitur utama di akhir setiap blok pelajaran (yaitu bab). Ilustrasi ditampilkan untuk memberikan umpan balik visual dan memperkuat konsep-konsep utama dalam aspek visual. Tujuan ditetapkan di awal setiap blok pelajaran. Tujuan-tujuan ini lebih dari sekadar daftar periksa. Tujuan-tujuan ini memberi Anda panduan untuk menguasai keterampilan baru. Penilaian Pengetahuan semakin menantang, setelah penyiapan Server BTCPay Anda selesai.


### Apa yang siswa dapatkan dari kursus ini?


Dengan Kursus BTCPay Server, siswa dapat memahami prinsip-prinsip dasar, teknis dan non-teknis, dari Bitcoin. Pelatihan ekstensif dalam menggunakan Bitcoin melalui BTCPay Server akan memungkinkan siswa untuk mengoperasikan infrastruktur Bitcoin mereka sendiri.


### Alamat web penting atau peluang Kontak


BTCPay Server Foundation, yang memungkinkan Alekos dan Bas menulis kursus ini, berada di Tokyo, Jepang. Yayasan BTCPay Server dapat dihubungi melalui situs web yang tercantum.



- https://foundation.btcpayserver.org
- Bergabunglah dengan saluran obrolan resmi: https://chat.btcpayserver.org


## Pengantar ke Bitcoin


<chapterId>5c0bc234-c188-5b4a-94d5-adee87a120e2</chapterId>


### Memahami Bitcoin melalui latihan di kelas


Ini adalah latihan di kelas, jadi jika Anda mengambil kursus ini sendiri, Anda tidak dapat melakukannya, tetapi Anda masih dapat mengerjakan latihan ini. Untuk menyelesaikan tugas ini, diperlukan minimal 9 hingga 11 orang.


Latihan dimulai setelah menonton pengantar "Cara kerja Bitcoin dan Blockchain" oleh BBC.


:::video id=c20b6df7-0c3a-4785-94b9-42ef59093acc:::


Latihan ini membutuhkan minimal sembilan peserta. Latihan ini bertujuan untuk memberikan pemahaman fisik tentang cara kerja Bitcoin. Dengan memainkan setiap peran dalam jaringan, Anda akan mendapatkan cara belajar yang interaktif dan menyenangkan. Latihan ini tidak melibatkan Lightning Network.


### Contoh: Membutuhkan 9 / 11 orang


Perannya adalah:



- 1 Pelanggan
- 1 Pedagang
- 7 hingga 9 node Bitcoin


**Pengaturannya adalah sebagai berikut:**


Pelanggan membeli produk dari toko dengan Bitcoin.


**Skenario 1 - Sistem Perbankan Tradisional**



- Siapkan:
  - Lihat diagram/penjelasan pada Figjam terlampir - [Skema Kegiatan](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Mintalah tiga sukarelawan siswa untuk berperan sebagai Pelanggan (Alice), Pedagang (Bob), dan Bank.
- Peragakan urutan kejadian:
  - Pelanggan- menjelajahi toko secara online dan menemukan barang seharga $25, yang mereka inginkan, dan memberi tahu Penjual bahwa mereka ingin membeli
  - Pedagang- meminta pembayaran.
  - Pelanggan- mengirimkan informasi kartu ke Merchant
  - Merchant- meneruskan informasi kepada Bank (mengidentifikasi identitas/informasi mereka dan identitas/informasi pelanggan), meminta pembayaran
  - Bank mengumpulkan informasi mengenai Nasabah dan Merchant (Alice dan Bob) dan memeriksa kecukupan saldo Nasabah.
  - Mengurangkan \$25 dari akun Alice, menambahkan \$24 ke akun Bob, mengambil \$1 untuk layanan
  - Merchant menerima jempol dari Bank dan mengirimkan barang ke pelanggan.
- Komentar:
  - Bob dan Alice harus memiliki hubungan dengan bank.
  - Bank mengumpulkan informasi identifikasi mengenai Bob dan Alice.
  - Bank mengambil bagian.
  - Bank harus dipercaya untuk menyimpan uang setiap peserta setiap saat.


**Skenario 2 - Sistem Bitcoin**



- Siapkan:
  - Lihat diagram/penjelasan pada Figjam terlampir - [Skema Kegiatan](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Menggantikan Bank dengan sembilan siswa yang akan memainkan peran sebagai Komputer (Bitcoin Node/Miner) dalam jaringan untuk menggantikan Bank.
- Masing-masing dari 9 Komputer memiliki catatan historis lengkap tentang semua transaksi masa lalu yang pernah dilakukan (sehingga saldo yang akurat tanpa pemalsuan), serta seperangkat aturan:
  - Verifikasi transaksi telah ditandatangani dengan benar (thekeyfitsthelock)
  - Menyiarkan dan menerima transaksi yang valid ke rekan-rekan dalam jaringan, membuang transaksi yang tidak valid (termasuk transaksi yang mencoba membelanjakan dana yang sama dua kali)
- Perbarui/Tambahkan catatan secara berkala dengan transaksi baru yang diterima dari komputer "acak" asalkan semua isinya valid (catatan: untuk saat ini, kami mengabaikan komponen Proof of Work untuk semua ini, untuk mempermudah), jika tidak, tolak dan lanjutkan seperti sebelumnya sampai komputer "acak" berikutnya mengirimkan pembaruan
  - Jumlah yang tepat diberikan jika isinya valid.
- Peragakan urutan kejadian:
  - Pelanggan- menjelajahi toko secara online dan menemukan barang seharga $25 yang mereka inginkan, dan memberi tahu Penjual bahwa mereka ingin membeli
  - Merchant- meminta pembayaran dengan mengirimkan Invoice/Address kepada pelanggan dari Wallet mereka.
  - Pelanggan - membuat transaksi (mengirim BTC senilai $25 ke Address yang disediakan oleh Merchant) dan menyiarkannya ke Jaringan Bitcoin.
- Komputer- menerima transaksi dan melakukan verifikasi:
  - Setidaknya ada $25 BTC dalam Address yang dikirim dari
  - Transaksi ditandatangani dengan benar ("dibuka" oleh pelanggan)
  - Jika tidak demikian, maka transaksi tidak akan disebarkan melalui jaringan, dan jika demikian, maka transaksi akan disebarkan dan ditahan.
  - Pedagang dapat memeriksa apakah transaksi sedang tertunda dan menunggu.
- Satu komputer dipilih secara "acak" untuk mengusulkan penyelesaian transaksi yang diusulkan dengan menyiarkan "blok" yang berisi transaksi tersebut; jika disetujui, mereka akan menerima hadiah BTC.
  - PILIHAN/ LANJUTAN - alih-alih memilih Komputer secara acak, simulasikan Mining dengan meminta Komputer melempar dadu hingga beberapa hasil yang telah ditentukan sebelumnya muncul (misalnya, yang pertama melempar angka enam ganda yang dipilih)
  - Ini juga dapat menggambarkan apa yang akan terjadi jika dua Komputer menang secara bersamaan, yang mengakibatkan perpecahan rantai.
  - Komputer memeriksa validitas, memperbarui/menambahkan catatan ke buku besar mereka jika aturan terpenuhi, dan menyiarkan blok transaksi ke rekan-rekannya.
  - Komputer yang dipilih secara acak menerima hadiah karena mengajukan blok yang valid.
  - Transaksi cek pedagang telah selesai; dengan demikian, dana diterima, dan barang dikirim ke pelanggan.
- Komentar:
  - Perhatikan bahwa tidak diperlukan hubungan perbankan yang sudah ada sebelumnya.
  - Tidak ada pihak ketiga yang diperlukan untuk memfasilitasi; digantikan oleh kode/insentif.
  - Tidak ada pengumpulan data oleh siapa pun di luar Exchange langsung, dan hanya jumlah yang diperlukan yang harus dipertukarkan antara peserta (misalnya, pengiriman Address).
  - Tidak ada kepercayaan yang diperlukan di antara orang-orang (selain Penjual yang mengirim barang), seperti pembelian tunai dalam banyak hal.
  - Uang tersebut dimiliki langsung oleh individu.
  - Bitcoin Ledger digambarkan dalam dolar untuk kesederhanaan, tetapi pada kenyataannya, ini adalah BTC.
  - Kami mensimulasikan satu transaksi yang disiarkan, tetapi pada kenyataannya, banyak transaksi yang tertunda dalam jaringan, dan blok mencakup ribuan transaksi sekaligus. Node juga memverifikasi bahwa tidak ada transaksi pengeluaran ganda yang tertunda (saya akan membuang semua transaksi kecuali satu dalam kasus ini).
- Skenario kecurangan:
  - Bagaimana jika pelanggan tidak memiliki $25 BTC?
    - Mereka tidak akan dapat membuat transaksi karena "membuka kunci" dan "Ownership" adalah hal yang sama, dan komputer memeriksa apakah transaksi ditandatangani dengan benar; jika tidak, mereka akan menolaknya
  - Bagaimana jika komputer yang dipilih secara acak mencoba untuk "mengubah Ledger"?
    - Blokir akan ditolak, karena setiap komputer lain memiliki riwayat yang lengkap dan akan melihat perubahan tersebut, melanggar salah satu aturan mereka.
    - Random Computer tidak akan mendapatkan hadiah, dan tidak ada transaksi dari blok mereka yang akan diselesaikan.


## Penilaian pengetahuan


<chapterId>1461f064-933d-50ea-8935-324b68ec5d5f</chapterId>


### Diskusi kelas KA


Diskusikan beberapa penyederhanaan yang dibuat dalam latihan di kelas pada skenario kedua dan jelaskan apa yang dilakukan oleh sistem Bitcoin yang sebenarnya secara lebih rinci.


### Tinjauan kosakata KA


Definisikan istilah-istilah kunci berikut yang diperkenalkan di bagian sebelumnya:



- Node
- Mempool
- Target Kesulitan
- Blokir


**Diskusikan arti dari beberapa istilah tambahan sebagai sebuah kelompok:**


Blockchain, Transaksi, Pengeluaran Ganda, Masalah Jenderal Bizantium, Mining, Proof of Work (PoW), Fungsi Hash, Block reward, Blockchain, Rantai Terpanjang, Serangan 51%, Keluaran, Kunci Keluaran, Perubahan, Satoshi, Kunci Publik/Privat, Address, Kriptografi Kunci Publik, Tanda Tangan Digital, Wallet


# Memperkenalkan Server BTCPay


<partId>9c8a2d0c-9ba1-5c39-874c-f9eaf1bba663</partId>


## Memahami layar login Server BTCPay


<chapterId>14aad54c-9bd8-54f2-9455-178b8ae63408</chapterId>


### Bekerja dengan Server BTCPay


Tujuan dari blok kursus ini adalah untuk mendapatkan pemahaman umum tentang perangkat lunak BTCPay Server. Dalam lingkungan bersama, disarankan untuk mengikuti demonstrasi instruktur dan mengacu pada Buku Kursus BTCPay Server untuk mengikuti bersama guru. Anda akan belajar cara membuat Wallet melalui beberapa metode. Contohnya termasuk pengaturan Hot Wallet dan dompet perangkat keras yang terhubung melalui BTCPay Server Vault. Tujuan-tujuan ini terjadi di lingkungan Demo, ditampilkan dan diberikan akses oleh instruktur kursus Anda.


Jika Anda mengikuti kursus ini sendiri, Anda dapat menemukan daftar host pihak ketiga untuk tujuan Demo di https://directory.btcpayserver.org/filter/hosts. Kami sangat menyarankan agar Anda tidak menggunakan opsi pihak ketiga ini sebagai lingkungan produksi; namun, opsi ini memiliki tujuan yang tepat untuk memperkenalkan penggunaan Bitcoin dan BTCPay Server.


Sebagai peserta pelatihan BTCPay Server, Anda mungkin memiliki pengalaman sebelumnya dalam menyiapkan node Bitcoin. Kursus ini secara khusus disesuaikan dengan tumpukan Perangkat Lunak Server BTCPay.


Banyak opsi di BTCPay Server yang ada dalam beberapa bentuk atau lainnya di perangkat lunak terkait Bitcoin Wallet lainnya.


### Layar Login Server BTCPay


Ketika Anda disambut di lingkungan Demo, Anda akan diminta untuk 'Masuk' atau 'Buat akun Anda' Administrator server dapat menonaktifkan fitur pembuatan akun baru untuk alasan keamanan. Logo dan warna tombol BTCPay Server dapat diubah karena BTCPay Server adalah Perangkat Lunak Sumber Terbuka. Host pihak ketiga dapat memberi label putih pada perangkat lunak dan mengubah seluruh tampilan.


![image](assets/en/001.webp)


### Jendela Buat Akun


Membuat akun di BTCPay Server membutuhkan string Email Address yang valid; example@email.com adalah string yang valid untuk Email.


Kata sandi harus terdiri dari setidaknya 8 karakter, termasuk huruf, angka, dan karakter. Setelah mengatur kata sandi sekali, Anda harus memverifikasi bahwa kata sandi tersebut sama dengan yang diketikkan di bidang kata sandi pertama.


Setelah kolom Email dan Kata Sandi terisi dengan benar, klik tombol 'Buat Akun'. Ini akan menyimpan Email dan kata sandi di server BTCPay Server milik instruktur.


![image](assets/en/002.webp)


**Catatan!**


Jika Anda mengikuti kursus ini secara mandiri, pembuatan akun ini kemungkinan besar akan dilakukan di host pihak ketiga; oleh karena itu, kami sekali lagi menekankan bahwa ini tidak boleh digunakan sebagai lingkungan produksi, tetapi hanya untuk tujuan pelatihan.


### Pembuatan Akun oleh Administrator Server BTCPay


Administrator Instansi Server BTCPay juga dapat membuat akun untuk Server BTCPay. Administrator Instance Server BTCPay dapat mengklik 'Pengaturan Server' (1), klik tab 'Pengguna' (2), dan klik tombol "+ Tambah Pengguna" (3) di bagian kanan atas tab Pengguna. Pada Tujuan (4.3), Anda akan mempelajari lebih lanjut mengenai kontrol administrator atas Akun.


![image](assets/en/003.webp)


Sebagai administrator, Anda memerlukan Email pengguna Address dan menetapkan kata sandi standar. Disarankan agar Administrator memberi tahu pengguna untuk mengubah kata sandi ini sebelum menggunakan akun untuk alasan keamanan. Jika Administrator tidak menetapkan Kata Sandi dan SMTP telah dikonfigurasi di server, pengguna akan menerima email dengan tautan undangan untuk membuat akun dan menetapkan kata sandi sendiri.


### Contoh


Saat mengikuti kursus dengan instruktur, ikuti tautan yang disediakan oleh instruktur dan buat akun Anda di lingkungan Demo. Pastikan email Address dan kata sandi Anda tersimpan dengan aman; Anda akan memerlukan kredensial login ini untuk tujuan demo lainnya dalam kursus ini.


Instruktur Anda mungkin telah mengumpulkan email Address di awal dan mengirimkan tautan undangan sebelum latihan ini. Jika diinstruksikan, periksa email Anda.


Saat mengikuti kursus tanpa instruktur, buat akun Anda menggunakan lingkungan demo BTCPay Server; buka


https://Mainnet.demo.btcpayserver.org/login.


Akun ini hanya boleh digunakan untuk tujuan demonstrasi/pelatihan dan tidak boleh digunakan untuk bisnis.


### Ringkasan Keterampilan


Dalam bagian ini, Anda telah mempelajari yang berikut ini:



- Cara membuat akun pada server yang dihosting melalui Interface.
- Bagaimana administrator server dapat menambahkan pengguna secara manual dalam pengaturan server.


### Penilaian pengetahuan


#### Tinjauan Konseptual KA


Berikan alasan mengapa menggunakan Server Demo adalah ide yang buruk untuk tujuan produksi.


## Mengelola akun pengguna


<chapterId>b58ca6ee-b7fc-5e81-a6aa-c8ff212b4c55</chapterId>


### Manajemen Akun di Server BTCPay


Setelah pemilik toko membuat akun, mereka dapat mengelolanya di bagian kiri bawah UI Server BTCPay. Di bawah tombol Akun, ada beberapa pengaturan tingkat yang lebih tinggi.



- Mode Gelap/Terang.
- Tombol geser Sembunyikan Info Sensitif.
- Kelola Akun.


![image](assets/en/004.webp)


### Mode Gelap dan Terang


Pengguna BTCPay Server dapat memilih antara versi mode Terang atau Gelap dari UI. Halaman yang berhadapan dengan pelanggan tidak akan berubah. Mereka menggunakan pengaturan yang dipilih pelanggan mengenai mode gelap atau terang.


### Sembunyikan Tombol Info Sensitif


Tombol Sembunyikan Info Sensitif memberikan keamanan Layer yang cepat dan sederhana. Kapan pun Anda perlu mengoperasikan BTCPay Server Anda, tetapi mungkin ada orang yang mengintai Anda di ruang publik, aktifkan Sembunyikan Info Sensitif, dan semua nilai dalam BTCPay Server akan disembunyikan. Orang mungkin dapat melihat dari balik bahu Anda, tetapi tidak dapat lagi melihat nilai yang Anda hadapi.


### Kelola Akun


Setelah akun pengguna dibuat, di sinilah tempat mengelola kata sandi, 2FA, atau kunci API.


### Kelola Akun - Akun


Secara opsional, perbarui akun Anda dengan Email Address yang berbeda. Untuk memastikan email Address Anda sudah benar, BTCPay Server memungkinkan Anda mengirim email verifikasi. Klik simpan jika pengguna menetapkan Address email baru dan mengonfirmasi verifikasi berhasil. Nama pengguna tetap sama dengan Email sebelumnya.


Seorang pengguna dapat memutuskan untuk menghapus seluruh akun mereka. Hal ini dapat dilakukan dengan mengeklik tombol hapus pada tab Akun.


![image](assets/en/005.webp)


**Catatan!**


Setelah mengubah Email, nama pengguna untuk akun tidak akan berubah. Email Address yang diberikan sebelumnya akan tetap menjadi nama Login.


### Kelola Akun - Kata Sandi


Seorang siswa mungkin ingin mengubah kata sandi mereka. Dia dapat melakukan ini dengan membuka tab Kata Sandi. Di sini, dia diminta untuk mengetikkan kata sandi lamanya dan dapat mengubahnya menjadi kata sandi yang baru.


![image](assets/en/006.webp)


### Autentikasi Dua Faktor (2fa)


Untuk membatasi konsekuensi dari kata sandi yang dicuri, Anda bisa menggunakan autentikasi dua faktor (2FA), sebuah metode keamanan yang relatif baru. Anda dapat mengaktifkan autentikasi dua faktor melalui halaman Kelola akun dan tab autentikasi dua faktor. Anda harus menyelesaikan langkah kedua setelah masuk dengan nama pengguna dan kata sandi.


BTCPay Server mendukung dua metode untuk mengaktifkan 2FA: 2FA berbasis aplikasi (Authy, Google, Microsoft Authenticators) atau melalui perangkat Keamanan (FIDO2 atau LNURL Auth).


### Autentikasi Dua Faktor - Berbasis aplikasi


Berdasarkan Sistem Operasi ponsel Anda (Android atau iOS), pengguna dapat memilih di antara aplikasi berikut ini;


1. Unduh autentikator dua faktor.


   - Authy untuk [Android](https://play.google.com/store/apps/details?id=com.authy.authy) atau [iOS](https://apps.apple.com/us/app/authy/id494168017)
   - Microsoft Authenticator untuk [Android](https://play.google.com/store/apps/details?id=com.azure.authenticator) atau [iOS](https://apps.apple.com/us/app/microsoft-authenticator/id983156458)
   - Google Authenticator untuk [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=e%C2%80) atau [iOS](https://apps.apple.com/us/app/google-authenticator/id388497605)

2. Setelah mengunduh dan menginstal Aplikasi Authenticator.


   - Pindai Kode QR yang disediakan oleh Server BTCPay
   - Atau masukkan kunci yang dihasilkan oleh BTCPay Server secara manual ke dalam aplikasi Authenticator Anda.

3. Aplikasi Authenticator akan memberi Anda kode unik. Masukkan kode unik di BTCPay Server untuk memverifikasi penyiapan, dan klik verifikasi untuk menyelesaikan proses.


![image](assets/en/007.webp)


### Ringkasan Keterampilan


Dalam bagian ini, Anda telah mempelajari yang berikut ini:



- Opsi pengelolaan akun dan berbagai cara untuk mengelola akun pada instance Server BTCPay.
- Cara mengatur 2FA berbasis aplikasi.


### Penilaian pengetahuan


#### Tinjauan Konseptual KA


Jelaskan bagaimana 2FA berbasis aplikasi membantu mengamankan akun Anda.


## Membuat toko baru


<chapterId>463b3634-b49f-5512-a711-3b2e096fc2e0</chapterId>


### Buat wizard toko Anda


Ketika pengguna baru masuk ke BTCPay Server, lingkungan masih kosong dan membutuhkan toko pertama. Wizard pengenalan BTCPay Server akan memberikan pilihan kepada pengguna untuk 'Buat toko Anda' (1). Toko dapat dilihat sebagai Rumah untuk kebutuhan Bitcoin Anda. Node Server BTCPay baru akan dimulai dengan menyinkronkan Bitcoin Blockchain (2). Tergantung pada infrastruktur yang Anda gunakan untuk menjalankan BTCPay Server, proses ini dapat berlangsung dalam beberapa jam hingga beberapa hari. Versi instance saat ini ditampilkan di sudut kanan bawah UI BTCPay Server Anda. Ini berguna sebagai referensi saat memecahkan masalah.


![image](assets/en/008.webp)


### Buat wizard toko Anda


Mengikuti kursus ini akan dimulai dengan layar yang sedikit berbeda dari halaman sebelumnya. Karena instruktur Anda telah menyiapkan lingkungan Demo, Bitcoin Blockchain telah disinkronkan sebelumnya, dan oleh karena itu, Anda tidak akan melihat status sinkronisasi node.


Seorang pengguna dapat memutuskan untuk menghapus seluruh akun mereka. Hal ini dapat dilakukan dengan mengeklik tombol hapus pada tab Akun.


![image](assets/en/009.webp)


**Catatan!**


Akun BTCPay Server dapat membuat toko dalam jumlah yang tidak terbatas. Setiap toko adalah Wallet atau "rumah".


### Contoh


Mulailah dengan mengklik "Buat toko Anda".


![image](assets/en/010.webp)


Ini akan membuat Beranda dan dasbor pertama Anda untuk menggunakan BTCPay Server.


(1) Setelah mengklik "Buat toko Anda", BTCPay Server akan meminta Anda untuk memberi nama toko; nama toko dapat berupa apa pun yang berguna bagi Anda.


![image](assets/en/011.webp)


(2) Mata uang penyimpanan default harus ditetapkan selanjutnya, baik mata uang fiat atau mata uang yang berdenominasi Bitcoin atau Sats. Untuk lingkungan demo, kami akan mengaturnya ke USD.


![image](assets/en/012.webp)


(3) Sebagai parameter terakhir pada pengaturan toko, BTCPay Server mengharuskan Anda untuk mengatur "Sumber harga pilihan" untuk membandingkan harga Bitcoin dengan harga fiat saat ini sehingga toko Anda menampilkan kurs Exchange yang benar antara Bitcoin dan mata uang fiat yang ditetapkan oleh toko. Kami akan tetap menggunakan nilai default pada contoh Demo dan mengaturnya ke Kraken Exchange. Server BTCPay menggunakan API Kraken untuk memeriksa kurs Exchange.


![image](assets/en/013.webp)


(4) Setelah parameter toko ini ditetapkan, klik tombol Buat, dan Server BTCPay akan membuat dasbor toko pertama Anda, di mana wizard akan melanjutkan.


![image](assets/en/014.webp)


Selamat, Anda telah membuat toko pertama Anda, dan ini mengakhiri latihan ini.


![image](assets/en/015.webp)


### Ringkasan Keterampilan


Di bagian ini, Anda sudah belajar:



- Pembuatan toko dan mengonfigurasi mata uang default, dikombinasikan dengan preferensi sumber harga.
- Setiap "Toko" adalah rumah baru yang terpisah dari toko lain pada instalasi BTCPay Server ini.


# Pengantar untuk Mengamankan Kunci Bitcoin


<partId>25da22d8-fd37-51c5-af2a-58b9f3b046b2</partId>


## Memahami Pembuatan Kunci Bitcoin


<chapterId>d162735b-847b-578e-83b8-a044ab703ec5</chapterId>


### Apa saja yang terlibat dalam pembuatan kunci Bitcoin?


Dompet Bitcoin, ketika dibuat, menciptakan apa yang disebut "seed". Pada tujuan terakhir, Anda membuat "seed", Rangkaian kata yang dibuat sebelumnya juga dikenal sebagai frasa Mnemonic. seed digunakan untuk mendapatkan Kunci Bitcoin individual dan digunakan untuk mengirim atau menerima Bitcoin. Frasa seed tidak boleh dibagikan dengan pihak ketiga atau rekan yang tidak dipercaya.


Generasi seed dilakukan sesuai dengan standar industri yang dikenal sebagai kerangka kerja "Hierarchical Deterministic" (HD).


![image](assets/en/016.webp)


### Alamat


Server BTCPay dibuat untuk generate menjadi Address yang baru. Hal ini mengurangi masalah penggunaan ulang kunci publik atau Address. Menggunakan kunci Publik yang sama membuat pelacakan seluruh riwayat pembayaran Anda menjadi sangat mudah. Menganggap kunci sebagai voucher sekali pakai akan secara signifikan meningkatkan privasi Anda. Kami juga menggunakan Alamat Bitcoin, jangan bingung dengan kunci Publik.


Sebuah Address didapatkan dari kunci Publik melalui sebuah "algoritma hashing" Akan tetapi, sebagian besar dompet dan transaksi akan menampilkan Alamat daripada kunci publik. Alamat, secara umum, lebih pendek daripada kunci publik dan biasanya dimulai dengan `1`, `3`, atau `bc1`, sedangkan kunci publik dimulai dengan `02`, `03`, atau `04`.



- Alamat yang dimulai dengan `1.....` masih merupakan alamat yang sangat umum. Seperti yang telah disebutkan dalam bab "Membuat toko baru", alamat ini adalah alamat lama. Tipe Address ini dimaksudkan untuk transaksi P2PKH. P2Pkh menggunakan pengkodean Base58, yang membuat Address menjadi sensitif terhadap huruf besar-kecil. Strukturnya didasarkan pada kunci publik dengan sebuah digit tambahan sebagai pengenal.



- Alamat yang dimulai dengan `bc1... ` secara perlahan bergerak ke alamat yang sangat umum. Alamat ini dikenal sebagai Alamat SegWit (asli). Alamat ini menawarkan struktur biaya yang lebih baik daripada Alamat yang disebutkan sebelumnya. Alamat SegWit asli menggunakan pengkodean Bech32 dan hanya mengizinkan huruf kecil.



- Alamat yang dimulai dengan `3...` biasanya masih digunakan oleh bursa untuk alamat penyimpanan. Alamat-alamat ini disebutkan dalam bab "Membuat toko baru," alamat SegWit yang dibungkus atau bersarang. Namun, alamat-alamat ini juga dapat berfungsi sebagai "Multisig Address". Ketika digunakan sebagai SegWit Address, ada beberapa penghematan biaya transaksi, sekali lagi, lebih sedikit dibandingkan dengan SegWit asli. Alamat P2SH menggunakan pengodean Base58. Hal ini membuatnya menjadi case Sensitive, seperti Address yang lama.



- Alamat yang dimulai dengan `2...` adalah alamat Testnet. Alamat-alamat ini dimaksudkan untuk menerima Testnet Bitcoin (tBTC). Anda tidak boleh mencampuradukkannya dan mengirimkan Bitcoin ke alamat-alamat ini. Untuk tujuan pengembangan, Anda dapat mengirimkan generate atau Testnet Wallet. Ada beberapa faucet online untuk mendapatkan Testnet Bitcoin. Jangan pernah membeli Testnet Bitcoin. Testnet Bitcoin ditambang. Ini mungkin menjadi alasan bagi pengembang untuk menggunakan Regtest sebagai gantinya. Ini adalah lingkungan bermain bagi para pengembang, yang tidak memiliki komponen jaringan tertentu. Akan tetapi, Bitcoin sangat berguna untuk tujuan pengembangan.


### Kunci Publik


Kunci publik sudah jarang digunakan dalam praktiknya saat ini. Seiring berjalannya waktu, para pengguna Bitcoin telah menggantinya dengan Alamat. Mereka masih ada dan masih digunakan sesekali. Kunci publik, secara umum, merupakan sebuah string yang lebih panjang daripada alamat. Sama seperti alamat, mereka dimulai dengan sebuah pengenal yang spesifik.



- Pertama, `02... ` dan `03... ` adalah pengidentifikasi kunci publik yang sangat standar yang dikodekan dalam format SEC. Ini dapat diproses dan diubah menjadi alamat untuk menerima, digunakan untuk membuat alamat multi-sig, atau untuk memverifikasi tanda tangan. Transaksi Bitcoin pada masa awal menggunakan kunci publik sebagai bagian dari transaksi P2PK.



- Akan tetapi, dompet HD menggunakan struktur yang berbeda. `xpub... `, `ypub... ` atau `zpub... ` disebut sebagai kunci publik yang diperluas, atau xpub. Kunci-kunci ini digunakan untuk mendapatkan banyak kunci publik sebagai bagian dari HD Wallet. Karena xpub Anda menyimpan catatan seluruh riwayat Anda, yang berarti transaksi di masa lalu dan masa depan, jangan pernah membagikannya kepada pihak yang tidak dipercaya.


### Ringkasan Keterampilan


Dalam bagian ini, Anda telah mempelajari yang berikut ini:



- Perbedaan antara alamat dan tipe data kunci publik dan manfaat menggunakan alamat dibandingkan kunci publik.


### Penilaian pengetahuan


Jelaskan manfaat menggunakan alamat baru untuk setiap transaksi dibandingkan dengan penggunaan ulang Address atau metode kunci publik.


## Mengamankan kunci dengan Hardware Wallet


<chapterId>c54a6d61-5a43-5fdb-93ae-c6750de9c612</chapterId>


### Menyimpan Kunci Bitcoin


Setelah membuat frasa seed, daftar 12 - 24 kata yang dibuat dalam buku ini membutuhkan cadangan dan keamanan yang tepat, karena kata-kata ini merupakan satu-satunya cara untuk memulihkan akses ke Wallet. Struktur dari dompet HD dan bagaimana ia menghasilkan alamat secara deterministik menggunakan satu seed berarti bahwa semua alamat yang anda buat akan dicadangkan dengan menggunakan satu daftar kata Mnemonic, yang mewakili seed atau frase pemulihan anda.


Jaga agar frasa pemulihan Anda tetap aman. Jika diakses oleh seseorang, khususnya yang berniat jahat, mereka dapat memindahkan dana Anda. Menjaga seed tetap aman dan terlindungi, serta mengingat bahwa hal ini merupakan hal yang saling menguntungkan. Terdapat beberapa metode untuk menyimpan private key Bitcoin, masing-masing memiliki kelebihan dan kekurangannya sendiri, dalam hal keamanan, privasi, kenyamanan, dan penyimpanan fisik. Karena pentingnya private key, pengguna Bitcoin cenderung untuk menyimpan dan menyimpan kunci ini dengan aman dalam "penyimpanan sendiri" daripada menggunakan layanan "kustodian" seperti bank. Tergantung pada penggunanya, mereka harus menggunakan solusi penyimpanan Cold atau Hot Wallet.


### Penyimpanan kunci Hot dan Cold untuk kunci Bitcoin


Biasanya, dompet Bitcoin didenominasi dalam Hot Wallet atau Cold Wallet. Sebagian besar trade-off terletak pada kenyamanan, kemudahan penggunaan, dan risiko keamanan. Masing-masing metode ini juga dapat dilihat dalam solusi kustodian. Namun, pertukaran di sini sebagian besar berbasis keamanan dan privasi dan melampaui cakupan kursus ini.


### Hot Wallet


Dompet Hot adalah cara yang paling nyaman untuk berinteraksi dengan Bitcoin melalui perangkat lunak seluler, web, atau desktop. Wallet selalu terhubung ke internet, memungkinkan pengguna untuk mengirim atau menerima Bitcoin. Namun, ini juga merupakan kelemahannya; Wallet, karena selalu online, sekarang lebih rentan terhadap serangan peretas atau malware pada perangkat Anda. Di BTCPay Server, dompet Hot menyimpan kunci privat pada instance. Siapa pun yang mengakses penyimpanan BTCPay Server Anda berpotensi mencuri dana dari Address ini jika mereka jahat. Ketika BTCPay Server berjalan di lingkungan yang di-host, Anda harus selalu mempertimbangkan hal ini dalam profil keamanan Anda dan sebaiknya tidak menggunakan Hot Wallet dalam kasus seperti itu. Ketika BTCPay Server diinstal pada perangkat keras yang dimiliki dan diamankan oleh Anda, profil risiko akan menurun secara signifikan, tetapi tidak pernah sepenuhnya hilang.


### Cold Wallet


Individu memindahkan Bitcoin mereka ke dalam Cold Wallet karena dapat mengisolasi kunci privat dari internet, sehingga melindungi mereka dari potensi ancaman online. Menghapus koneksi internet dari persamaan akan mengurangi risiko malware, spyware, dan pertukaran SIM. Penyimpanan Cold diyakini lebih unggul daripada penyimpanan Hot untuk keamanan dan otonomi, asalkan tindakan pencegahan yang memadai diambil untuk mencegah kehilangan kunci pribadi Bitcoin. Penyimpanan Cold paling cocok untuk Bitcoin dalam jumlah besar, yang tidak dimaksudkan untuk sering digunakan karena kerumitan pengaturan Wallet.


Ada berbagai metode untuk menyimpan kunci Bitcoin dalam penyimpanan Cold, mulai dari dompet kertas hingga dompet otak, dompet perangkat keras, atau, dari awal, file Wallet. Kebanyakan dompet menggunakan BIP 39 hingga generate frasa seed. Namun, dalam perangkat lunak Bitcoin core, belum ada konsensus mengenai penggunaannya. Perangkat lunak Bitcoin core masih akan generate file Wallet.dat, yang perlu Anda simpan di lokasi offline yang aman.


### Ringkasan Keterampilan


Di bagian ini, Anda sudah belajar:



- Perbedaan antara dompet Hot dan Cold dalam hal fungsionalitas dan trade-off-nya.


### Penilaian Pengetahuan Tinjauan Konseptual



- Apa yang dimaksud dengan Wallet?



- Apa perbedaan antara dompet Hot dan Cold?



- Jelaskan apa yang dimaksud dengan "menghasilkan Wallet"?


## Menggunakan tombol Bitcoin Anda


<chapterId>bff488de-5052-56e6-b696-97e896f762ae</chapterId>


### Server BTCPay Wallet


BTCPay Server terdiri dari fitur-fitur standar Wallet berikut ini:



- Transaksi
- Kirim
- Menerima
- Pindai ulang
- Tarik Pembayaran
- Pembayaran
- PSBT
- Pengaturan umum


### Transaksi


Administrator dapat melihat transaksi masuk dan keluar untuk On-Chain Wallet yang terhubung ke toko khusus ini dalam tampilan transaksi. Setiap transaksi memiliki perbedaan antara jumlah yang diterima dan jumlah yang dikirim. Transaksi yang diterima akan berwarna Green, dan transaksi yang dikirim akan berwarna merah. Dalam tampilan transaksi BTCPay Server, administrator juga akan melihat serangkaian label standar.



| Jenis Transaksi | Deskripsi                                         |
| ---------------- | ------------------------------------------------- |
| Aplikasi         | Pembayaran diterima melalui faktur yang dibuat oleh aplikasi |
| Faktur           | Pembayaran diterima melalui faktur                |
| Payjoin          | Belum dibayar, pengatur waktu faktur belum kedaluwarsa |
| Payjoin-terekspos | UTXO terekspos melalui proposal payjoin pada faktur |
| Permintaan pembayaran | Pembayaran diterima melalui permintaan pembayaran |
| Pembayaran       | Pembayaran dikirim melalui pembayaran atau pengembalian dana |

### Bagaimana cara mengirim


Fungsi kirim server BTCPay mengirim transaksi dari Server BTCPay Anda On-Chain Wallet. Server BTCPay memungkinkan berbagai cara untuk menandatangani transaksi Anda untuk membelanjakan dana. Transaksi dapat ditandatangani dengan;



- Hardware Wallet
- Dompet yang mendukung PSBT
- Kunci pribadi HD atau benih pemulihan.
- Hot Wallet


#### Hardware Wallet


BTCPay Server memiliki dukungan Hardware Wallet bawaan, memungkinkan Anda untuk menggunakan Hardware Wallet Anda dengan BTCPay Vault tanpa membocorkan informasi ke aplikasi atau server pihak ketiga. Integrasi Hardware Wallet dalam BTCPay Server memungkinkan Anda untuk mengimpor Hardware Wallet Anda dan membelanjakan dana yang masuk dengan konfirmasi sederhana pada perangkat Anda. Kunci pribadi Anda tidak pernah meninggalkan perangkat, dan semua dana divalidasi dengan Full node Anda, memastikan tidak ada kebocoran data.


#### Menandatangani dengan Wallet yang mendukung PSBT


PSBT (Transaksi Bitcoin yang Ditandatangani Sebagian) adalah format pertukaran untuk transaksi Bitcoin yang masih harus ditandatangani sepenuhnya. PSBT didukung di BTCPay Server dan dapat ditandatangani dengan perangkat keras dan perangkat lunak dompet yang kompatibel.


Pembuatan transaksi Bitcoin yang telah ditandatangani sepenuhnya melalui langkah-langkah berikut:



- PSBT dibuat dengan input dan output tertentu, tetapi tidak ada tanda tangan
- PSBT yang diekspor dapat diimpor oleh Wallet yang mendukung format ini
- Data transaksi dapat diperiksa dan ditandatangani menggunakan Wallet
- File PSBT yang ditandatangani diekspor dari Wallet dan diimpor dengan BTCPay Server
- Server BTCPay menghasilkan transaksi Bitcoin terakhir
- Anda memverifikasi hasilnya dan menyiarkannya ke jaringan


#### Menandatangani dengan Kunci Pribadi HD atau Mnemonic seed


Jika Anda telah membuat Wallet sebelum menggunakan BTCPay Server, Anda dapat membelanjakan dana dengan memasukkan kunci pribadi Anda ke dalam bidang yang sesuai. Tetapkan "AccountKeyPath" yang tepat di Wallet> Pengaturan; jika tidak, Anda tidak dapat membelanjakan.


#### Menandatangani dengan Hot Wallet


Jika Anda membuat Wallet baru saat menyiapkan toko Anda dan mengaktifkannya sebagai Hot Wallet, maka secara otomatis akan menggunakan seed yang tersimpan di server untuk melakukan penandatanganan.


### RBF (Replace-by-fee)


Replace-by-fee (RBF) adalah fitur protokol Bitcoin yang memungkinkan Anda untuk mengganti transaksi yang telah disiarkan sebelumnya (ketika masih belum dikonfirmasi). Hal ini memungkinkan pengacakan sidik jari transaksi Wallet Anda atau menggantinya dengan tarif biaya yang lebih tinggi untuk memindahkan transaksi lebih tinggi dalam antrean prioritas konfirmasi (Mining). Hal ini akan secara efektif menggantikan transaksi asli karena tarif biaya yang lebih tinggi akan diprioritaskan, dan setelah dikonfirmasi, transaksi ini akan membatalkan transaksi asli (tidak ada pembelanjaan ganda).


Tekan tombol "Pengaturan Lanjutan" untuk melihat opsi RBF.


![image](assets/en/017.webp)



- Acak untuk privasi yang lebih tinggi, memungkinkan transaksi diganti secara otomatis untuk pengacakan sidik jari transaksi.
- Ya, tandai transaksi untuk RBF dan diganti secara eksplisit (Tidak diganti secara default, hanya dengan input)
- Tidak, jangan izinkan transaksi diganti.


### Pilihan Coin


Pilihan Coin adalah fitur peningkatan privasi tingkat lanjut yang memungkinkan Anda untuk memilih koin yang ingin Anda belanjakan saat membuat transaksi. Misalnya, membayar dengan koin yang baru dari gabungan koin.


Pemilihan Coin bekerja secara native dengan fitur label Wallet. Hal ini memungkinkan Anda melabeli dana yang masuk untuk pengelolaan dan pengeluaran UTXO yang lebih lancar.


BTCPay Server mendukung BIP-329 untuk manajemen label. Jika Anda mentransfer dari Wallet yang mendukung BIP-329 dan telah mengatur label, BTCPay Server akan mengenali dan mengimpornya secara otomatis. Ketika memigrasi server, informasi ini juga dapat diekspor dan diimpor ke lingkungan yang baru.


### Cara Menerima


Ketika mengklik tombol terima di BTCPay Server, tombol tersebut akan menghasilkan Address yang tidak terpakai yang dapat digunakan untuk menerima pembayaran. Administrator juga dapat membuat Address baru dengan membuat "Invoice" baru


Server BTCPay akan selalu meminta Anda untuk generate Address berikutnya yang tersedia untuk mencegah penggunaan ulang Address. Setelah mengklik "generate BTC Address yang tersedia berikutnya," Server BTCPay menghasilkan Address dan QR baru. Hal ini juga memungkinkan Anda untuk secara langsung mengatur Label ke Address untuk pengelolaan alamat Anda yang lebih baik.


![image](assets/en/018.webp)


![image](assets/en/019.webp)


#### Pindai ulang


Fitur Pindai Ulang bergantung pada "Scantxoutset" Bitcoin core 0.17.0 untuk memindai keadaan Blockchain saat ini (disebut UTXO Set) untuk koin-koin yang termasuk dalam skema turunan yang dikonfigurasi. Pemindaian ulang Wallet mengatasi dua masalah umum yang sering dihadapi pengguna BTCPay Server.


1. Masalah batas celah - Kebanyakan dompet pihak ketiga adalah dompet ringan yang berbagi simpul di antara banyak pengguna. Dompet ringan dan dompet yang bergantung pada Full node membatasi jumlah (biasanya 20) alamat tanpa saldo yang mereka lacak pada Blockchain untuk mencegah masalah kinerja. Server BTCPay menghasilkan Address baru untuk setiap Invoice. Dengan mempertimbangkan hal di atas, setelah BTCPay Server menghasilkan 20 faktur yang belum dibayar secara berurutan, Wallet eksternal akan berhenti mengambil transaksi, dengan asumsi tidak ada transaksi baru yang terjadi. Wallet eksternal Anda tidak akan menampilkannya setelah faktur dibayar pada tanggal 21, 22, dan seterusnya. Di sisi lain, secara internal, BTCPay Server Wallet melacak setiap Address yang dihasilkannya, bersama dengan batas selisih yang jauh lebih tinggi. Ini tidak bergantung pada pihak ketiga dan selalu dapat menunjukkan saldo yang benar.

2. Solusi batas celah - Jika [Wallet eksternal/yang sudah ada](https://docs.btcpayserver.org/WalletSetup/#use-an-existing-Wallet) Anda mengizinkan konfigurasi batas celah, solusi yang mudah adalah meningkatkannya. Akan tetapi, sebagian besar wallet tidak mengizinkan hal ini. Satu-satunya wallet yang saat ini mendukung konfigurasi gap-limit yang kami ketahui adalah Electrum, Wasabi, dan Sparrow wallet. Sayangnya, Anda mungkin akan mengalami masalah dengan banyak dompet lainnya. Untuk pengalaman pengguna dan privasi terbaik, pertimbangkan untuk menggunakan Wallet internal BTCPay Server daripada dompet eksternal.


#### Server BTCPay menggunakan "mempoolfullrbf=1"


Server BTCPay menggunakan "mempoolfullrbf=1"; kami telah menambahkannya sebagai pengaturan default pada penyiapan Server BTCPay Anda. Namun, kami juga menyediakan fitur yang dapat Anda nonaktifkan sendiri. Tanpa "mempoolfullrbf=1", jika pelanggan melakukan pembayaran dua kali dengan transaksi yang tidak menandakan RBF, Penjual hanya akan tahu setelah konfirmasi.


Seorang administrator mungkin ingin tidak menggunakan pengaturan ini. Dengan string berikut ini, Anda dapat mengubah pengaturan default.


```
BTCPAYGEN_EXCLUDE_FRAGMENTS="$BTCPAYGEN_EXCL UDE_FRAGMENTS;opt-mempoolfullrbf"
. btcpay-setup.sh -i
```


### Pengaturan BTCPay Server Wallet


Pengaturan Wallet dalam BTCPay Server memberikan gambaran yang jelas dan ringkas tentang pengaturan umum Wallet Anda. Semua pengaturan ini telah diisi sebelumnya jika Wallet dibuat dengan BTCPay Server.


![image](assets/en/020.webp)


Pengaturan Wallet dalam BTCPay Server memberikan gambaran yang jelas dan ringkas tentang pengaturan umum Wallet Anda. Semua pengaturan ini telah diisi sebelumnya jika Wallet dibuat dengan BTCPay Server. Pengaturan Wallet BTCPay Server dimulai dengan status Wallet. Apakah Wallet ini hanya untuk jam tangan atau Hot? Bergantung pada jenis Wallet, tindakan dapat bervariasi, termasuk memindai ulang Wallet untuk transaksi yang hilang, memangkas transaksi lama dari riwayat, mendaftarkan Wallet untuk tautan pembayaran, atau mengganti dan menghapus Wallet yang saat ini terpasang ke toko. Dalam pengaturan Wallet BTCPay Server, administrator dapat mengatur Label untuk Wallet untuk manajemen Wallet yang lebih baik. Di sini, Administrator juga dapat melihat Skema Derivasi, kunci akun (xpub), Sidik Jari, dan Jalur Kunci. Pembayaran dalam pengaturan Wallet hanya memiliki dua pengaturan utama. Pembayaran tidak valid jika transaksi gagal dikonfirmasi dalam waktu (menit yang ditentukan) setelah Invoice berakhir. Anggap saja Invoice dikonfirmasi ketika transaksi pembayaran memiliki X jumlah konfirmasi. Administrator juga dapat mengatur sakelar untuk menampilkan biaya yang disarankan pada layar pembayaran atau mengatur target konfirmasi manual dalam jumlah blok.


![image](assets/en/021.webp)


**Catatan!**


Jika Anda mengikuti kursus ini secara mandiri, pembuatan akun ini kemungkinan besar akan dilakukan pada host pihak ketiga. Oleh karena itu, kami sekali lagi menyarankan agar ini tidak digunakan sebagai lingkungan produksi, melainkan untuk tujuan pelatihan saja.


### Contoh


#### Menyiapkan Bitcoin Wallet di Server BTCPay


BTCPay Server menawarkan dua metode untuk menyiapkan Wallet. Salah satu caranya adalah dengan mengimpor Bitcoin Wallet yang sudah ada. Impor dapat dilakukan dengan menghubungkan Hardware Wallet, mengimpor file Wallet, memasukkan kunci publik yang Diperpanjang, memindai kode QR Wallet, atau, yang paling tidak disukai, memasukkan Wallet pemulihan seed yang dibuat sebelumnya dengan tangan. Di BTCPay Server, dimungkinkan juga untuk membuat Wallet baru. Ada dua cara yang memungkinkan untuk mengonfigurasi BTCPay Server saat membuat Wallet baru.


Opsi Hot Wallet di BTCPay Server memungkinkan fitur-fitur seperti 'PayJoin' atau 'Liquid'. Akan tetapi, ada kekurangannya: pemulihan seed yang dihasilkan untuk Wallet ini akan disimpan di server, di mana siapa pun yang memiliki kontrol admin dapat mengambilnya. Karena private key Anda berasal dari recovery seed, aktor jahat dapat memperoleh akses ke dana Anda saat ini dan di masa depan!


Untuk mengurangi risiko ini di BTCPay Server, Admin dapat mengatur nilai di Pengaturan Server > Kebijakan > "Izinkan non-admin untuk membuat dompet Hot untuk toko mereka" ke "tidak", karena ini adalah nilai default. Untuk meningkatkan keamanan dompet Hot tersebut, administrator server harus mengaktifkan autentikasi 2FA pada akun yang diizinkan untuk memiliki dompet Hot. Menyimpan kunci pribadi pada server publik adalah praktik yang berbahaya dan memiliki risiko yang signifikan. Beberapa di antaranya mirip dengan risiko Lightning Network (lihat bab berikutnya untuk risiko Lightning Network).


Opsi kedua yang ditawarkan BTCPay Server untuk menghasilkan Wallet baru adalah dengan membuat Watch-only wallet. BTCPay Server akan membuat generate kunci pribadi Anda satu kali. Setelah pengguna mengonfirmasi telah menuliskan Frasa seed mereka, BTCPay Server akan menghapus kunci pribadi dari server. Hasilnya, toko Anda sekarang memiliki Watch-only wallet yang terhubung dengannya. Untuk membelanjakan dana yang diterima pada Watch-only wallet Anda, lihat bab Cara Mengirim, baik dengan menggunakan BTCPay Server Vault, PSBT (Partially Signed Bitcoin Transaction), atau yang paling tidak direkomendasikan, secara manual memberikan frasa seed Anda.


Anda telah membuat 'Store' baru di bagian terakhir. Wizard instalasi akan melanjutkan dengan meminta untuk "Mengatur Wallet" atau "Mengatur simpul Lightning". Dalam contoh ini, Anda akan mengikuti proses wizard "Siapkan Wallet" (1).


![image](assets/en/022.webp)


Setelah mengklik "Siapkan Wallet", wizard akan melanjutkan dengan menanyakan bagaimana Anda ingin melanjutkan; BTCPay Server sekarang menawarkan opsi untuk menghubungkan Bitcoin Wallet yang sudah ada ke toko baru Anda. Jika Anda tidak memiliki Wallet, BTCPay Server menyarankan untuk membuat yang baru. Contoh ini akan mengikuti langkah-langkah untuk "membuat Wallet baru" (2). Ikuti langkah-langkah untuk mempelajari cara "Menghubungkan Wallet yang sudah ada (1).


![image](assets/en/023.webp)


**Catatan!**


Jika Anda mengikuti kursus ini di dalam kelas, harap diingat bahwa contoh saat ini dan seed yang kami buat hanya untuk tujuan pendidikan. Tidak boleh ada jumlah substansial selain yang diperlukan selama latihan pada alamat-alamat ini.


(1) Lanjutkan wizard "New Wallet" dengan mengeklik tombol "Buat Wallet baru".


![image](assets/en/024.webp)


(2) Setelah mengklik "Create a new Wallet," jendela berikutnya dalam wizard akan memberikan opsi "Hot Wallet" dan "Watch-only wallet." Jika Anda mengikuti instruktur, lingkungan Anda adalah Demo bersama, dan Anda hanya dapat membuat Watch-only wallet. Perhatikan perbedaan antara kedua gambar di bawah ini. Saat Anda berada di lingkungan Demo, mengikuti instruktur, buatlah "Watch-only wallet" dan lanjutkan dengan wizard "New Wallet".


![image](assets/en/025.webp)


![image](assets/en/026.webp)


(3) Melanjutkan wizard Wallet yang baru, Anda sekarang berada di bagian Create BTC Watch-only wallet. Di sini, kita dapat mengatur "tipe Address" Wallet BTCPay Server memungkinkan Anda untuk memilih tipe Address yang Anda sukai; pada saat penulisan kursus ini, masih disarankan untuk menggunakan alamat bech32. Anda dapat mempelajari lebih lanjut secara detail tentang alamat di bab pertama bagian ini.



- SegWit (bech32)
  - Alamat asli SegWit dimulai dengan `bc1q`.
  - Contoh: `bc1qXXXXXXXXXXXXXXXXXXXX`
- Warisan
  - Alamat lama adalah alamat yang dimulai dengan nomor `1`.
  - Contoh: `15e15hXXXXXXXXXXXXXXXXXX`
- Taproot (Untuk pengguna tingkat lanjut)
  - Alamat Taproot dimulai dengan `bc1p`.
  - Contoh: `bc1pXXXXXXXXXXXXXXXXXXXXXX`
- SegWit dibungkus
  - Alamat yang dibungkus SegWit dimulai dengan `3`.
  - Contoh: `37BBXXXXXXXXXXXXXXX`


Pilih SegWit (disarankan) sebagai tipe Wallet Address yang Anda sukai.


![image](assets/en/027.webp)


(4) Saat mengatur parameter untuk Wallet, BTCPay Server memungkinkan pengguna untuk mengatur passphrase opsional melalui BIP39; pastikan untuk mengonfirmasi kata sandi Anda.


![image](assets/en/028.webp)


(5) Setelah mengatur tipe Wallet dan mungkin mengatur beberapa opsi lanjutan, klik Buat, dan Server BTCPay akan membuat generate baru Anda. Perhatikan bahwa ini adalah langkah terakhir sebelum membuat frasa seed Anda. Pastikan Anda hanya melakukan ini di lingkungan yang tidak memungkinkan seseorang untuk mencuri frasa seed dengan melihat layar Anda.


![image](assets/en/029.webp)


(6) Pada layar wizard berikut ini, BTCPay Server menunjukkan kepada Anda frasa Pemulihan seed untuk Wallet yang baru Anda buat; ini adalah kunci untuk memulihkan Wallet Anda dan menandatangani transaksi. BTCPay Server menghasilkan frasa seed yang terdiri dari 12 kata. Kata-kata ini akan dihapus dari server setelah layar pengaturan ini. Wallet ini secara khusus adalah Watch-only wallet. Disarankan untuk tidak menyimpan frasa seed ini secara digital atau dengan gambar foto. Pengguna hanya dapat melangkah lebih jauh dalam wizard jika mereka secara aktif mengakui bahwa mereka menuliskan frasa seed mereka.


![image](assets/en/030.webp)


(7) Setelah mengklik Selesai dan mengamankan frasa Bitcoin seed yang baru dibuat, BTCPay Server akan memperbarui toko Anda dengan Wallet baru yang terlampir dan siap menerima pembayaran. Pada Pengguna Interface, di menu navigasi sebelah kiri, perhatikan bagaimana Bitcoin sekarang disorot dan diaktifkan di bawah Wallet.


![image](assets/en/031.webp)


### Contoh: Menuliskan frasa seed


Ini adalah saat yang sangat aman untuk menggunakan Bitcoin. Seperti yang telah disebutkan sebelumnya, hanya Anda yang memiliki akses atau pengetahuan tentang frasa seed Anda. Saat Anda mengikuti kursus bersama instruktur dan ruang kelas, seed yang dihasilkan hanya boleh digunakan dalam kursus ini. Terlalu banyak faktor, termasuk pengintaian dari teman sekelas, sistem yang tidak aman, dan lainnya, membuat kunci ini hanya bersifat edukatif dan tidak dapat dipercaya. Namun, kunci yang dihasilkan harus tetap disimpan untuk contoh kursus.


Metode pertama yang akan kita gunakan dalam situasi ini, yang juga merupakan metode yang paling tidak aman, adalah menuliskan frasa seed dengan urutan yang benar. Kartu frasa seed disertakan dalam materi kursus yang diberikan kepada siswa atau dapat ditemukan di GitHub Server BTCPay. Kita akan menggunakan kartu ini untuk menuliskan kata-kata yang dihasilkan pada langkah sebelumnya. Pastikan untuk menuliskannya dalam urutan yang benar. Setelah Anda menuliskannya, periksa dengan apa yang diberikan oleh perangkat lunak untuk memastikan Anda menuliskannya dalam urutan yang benar. Setelah Anda menuliskannya, klik kotak centang yang menyatakan bahwa Anda telah menuliskan frasa seed dengan benar.


### Contoh: Menyimpan frasa seed pada Hardware Wallet


Dalam kursus ini, kita akan membahas tentang menyimpan frasa seed pada Hardware Wallet. Mengikuti kursus ini dengan instruktur, kadang-kadang mungkin menyertakan perangkat semacam itu. Dalam kursus ini, materi panduan telah menyusun daftar dompet perangkat keras yang cocok untuk latihan ini.


Kami akan menggunakan brankas BTCPay Server dan Blockstream Jade Hardware Wallet dalam contoh ini.


Anda juga dapat mengikuti panduan video tentang cara menghubungkan Hardware Wallet.

:::video id=8e61664b-e0c0-416d-8ef9-b631bf28ec4d:::


Unduh BTCPay Server Vault: https://github.com/btcpayserver/BTCPayServer.Vault/releases


Pastikan Anda mengunduh file yang benar untuk sistem spesifik Anda. Pengguna Windows harus mengunduh paket [BTCPayServerVault-2.0.5-setup.exe](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-2.0.5-setup.exe), pengguna Mac mengunduh paket [BTCPayServerVault-osx-x64-2.0.5.dmg](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-osx-x64-2.0.5.dmg), dan pengguna Linux mengunduh [BTCPayServerVault-Linux-2.0.5.tar.gz](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-Linux-2.0.5.tar.gz)


Setelah menginstal BTCPay Server Vault, jalankan perangkat lunak dengan mengeklik ikon di Desktop Anda. Ketika BTCPay Server Vault terinstal dengan benar dan dijalankan untuk pertama kalinya, perangkat lunak ini akan meminta izin untuk digunakan dengan Aplikasi Web. Ia akan meminta untuk memberikan akses ke Server BTCPay tertentu yang Anda gunakan. Setujui ketentuan ini. BTCPay Server Vault sekarang akan mencari perangkat Hardware. Setelah perangkat ditemukan, BTCPay Server akan mengenali bahwa Vault sedang berjalan dan telah mengambil perangkat Anda.


**Catatan!**


Jangan berikan kunci SSH atau akun admin server Anda kepada orang lain selain administrator saat menggunakan Hot Wallet. Siapa pun yang memiliki akses ke akun-akun ini akan memiliki akses ke dana dalam Hot Wallet.


### Ringkasan Keterampilan


Dalam bagian ini, Anda telah mempelajari yang berikut ini:



- Tampilan transaksi Bitcoin Wallet dan berbagai kategorinya.
- Berbagai pilihan tersedia ketika mengirim dari Bitcoin Wallet, dari perangkat keras hingga dompet Hot.
- Masalah batas celah yang dihadapi saat menggunakan sebagian besar dompet, dan cara memperbaikinya.
- Cara generate Bitcoin Wallet baru di dalam BTCPay Server, termasuk menyimpan kunci dalam Hardware Wallet dan mencadangkan frasa pemulihan.


Pada tujuan ini, Anda telah mempelajari cara membuat generate Bitcoin Wallet baru di dalam BTCPay Server. Kita belum membahas cara mengamankan atau menggunakan kunci-kunci tersebut. Dalam tinjauan singkat pada tujuan ini, Anda telah mempelajari cara menyiapkan toko pertama. Anda telah mempelajari cara membuat generate frasa Bitcoin Pemulihan seed.


### Tinjauan Praktis Penilaian Pengetahuan


Jelaskan metode untuk menghasilkan kunci dan skema untuk mengamankannya, bersama dengan trade-off/risiko dari skema keamanan.


## Server BTCPay Lightning Wallet


<chapterId>1bbece7e-0197-57e6-a93a-561cf384d946</chapterId>


Ketika administrator server menyediakan instance BTCPay Server baru, mereka dapat menyiapkan implementasi Lightning Network, seperti LND, Core Lightning, atau Eclair; lihat Bagian Mengkonfigurasi BTCPay Server untuk petunjuk pemasangan yang lebih terperinci.


Jika diikuti oleh ruang kelas, menghubungkan node Lightning ke BTCPay Server Anda bekerja melalui node Custom. Pengguna yang bukan administrator server di BTCPay Server tidak akan dapat menggunakan node Lightning internal secara default. Hal ini untuk melindungi pemilik server agar tidak kehilangan dana mereka. Administrator server dapat menginstal plugin untuk memberikan akses ke node Lightning mereka melalui LNBank; hal ini berada di luar cakupan buku ini. Untuk informasi lebih lanjut tentang LNBank, lihat halaman plugin resmi.


### Menghubungkan simpul internal (administrator server)


Administrator Server dapat menggunakan Lightning Node internal BTCPay Server. Terlepas dari implementasi Lightning, menghubungkan ke node Lightning internal adalah sama.


Pergi ke tempat penyiapan sebelumnya, dan klik "Lightning" Wallet di menu sebelah kiri. BTCPay Server memberikan dua kemungkinan pengaturan: menggunakan node Internal (hanya admin server secara default) atau node khusus (koneksi eksternal). Administrator server dapat mengklik opsi "Gunakan node internal". Tidak perlu melakukan konfigurasi lagi. Klik tombol "simpan" dan perhatikan notifikasi yang menyatakan, "BTC Lightning node diperbarui". Toko sekarang telah berhasil mendapatkan kemampuan Lightning Network.


### Menghubungkan simpul eksternal (pengguna server/pemilik toko)


Secara default, pemilik toko tidak diizinkan untuk menggunakan Lightning Node administrator server. Koneksi harus dibuat ke node eksternal, baik node yang dimiliki oleh pemilik toko sebelum menyiapkan BTCPay Server, plugin LNBank jika disediakan oleh administrator server, atau solusi kustodian seperti Alby.


Buka toko penyiapan sebelumnya, dan klik "Lightning" di bawah dompet di menu sebelah kiri. Karena pemilik toko tidak diizinkan untuk menggunakan node internal secara default, opsi ini berwarna abu-abu. Menggunakan simpul khusus adalah satu-satunya pilihan yang tersedia secara default untuk pemilik toko.


BTCPay Server membutuhkan informasi koneksi; solusi yang sudah dibuat sebelumnya (atau solusi kustodian) akan memberikan informasi ini yang secara khusus disesuaikan dengan implementasi Lightning. Di dalam BTCPay Server, pemilik Toko dapat menggunakan koneksi berikut ini;



- C-lightning melalui koneksi TCPatauUnixdomainsocket.
- Pengisian Daya Kilat melalui HTTPS
- Eclair melalui HTTPS
- LND melalui proxy REST
- LNDhub melalui REST API


![image](assets/en/032.webp)


Klik "uji koneksi" untuk memastikan Anda memasukkan detail koneksi dengan benar. Setelah koneksi dipastikan baik, klik "Simpan", dan Server BTCPay akan menampilkan bahwa toko telah diperbarui dengan Lightning Node.


### Mengelola simpul Lightning internal LND (Administrator server)


Setelah menyambungkan Lightning Node internal, administrator server akan melihat ubin baru di Dasbor khusus untuk informasi Lightning.



- Keseimbangan Petir
- BTC di saluran
  - Saluran pembukaan BTC
  - Saldo lokal BTC
  - Saldo jarak jauh BTC
  - Saluran penutupan BTC
- BTC On-Chain
  - BTC dikonfirmasi
  - BTC belum dikonfirmasi
  - BTC dicadangkan
- Layanan Petir
  - Ride the Lightning (RTL).


Dengan mengeklik Logo Ride the Lightning di ubin "Layanan Lightning" atau "Lightning" di bawah dompet di menu sebelah kiri, administrator server dapat menjangkau RTL untuk manajemen simpul Lightning.


** Catatan! *


Menyambungkan Lightning Node internal gagal - Jika sambungan internal gagal, konfirmasikan:


1. Node Bitcoin On-Chain disinkronkan sepenuhnya

2. Node petir internal "Diaktifkan" di bawah "Petir" > "Pengaturan" > "Pengaturan Petir BTC"


Jika Anda tidak dapat terhubung ke node Lightning Anda, Anda dapat mencoba memulai ulang server Anda, atau membaca detail lebih lanjut di dokumentasi resmi BTCPay Server; https://docs.btcpayserver.org/Troubleshooting/. Anda tidak dapat menerima pembayaran Lightning di toko Anda hingga node Lightning Anda muncul dalam status "Online". Cobalah untuk menguji koneksi Lightning Anda dengan mengklik tautan "Info Node Publik".


### Petir Wallet


Dalam opsi Lightning Wallet di bilah menu sebelah kiri, administrator server akan menemukan akses mudah ke RTL, Info node Publik, dan pengaturan Lightning yang khusus untuk penyimpanan BTCPay Server mereka.


#### Info simpul internal


Administrator server dapat mengklik info node internal untuk melihat status server mereka (Online/Offline) dan string koneksi untuk Clearnet atau Tor.


![image](assets/en/033.webp)


#### Mengubah koneksi


Untuk mengubah node Lightning eksternal, buka "Pengaturan Lightning" dan klik "Ubah koneksi" (di samping "Info Node Publik"). Ini akan mengatur ulang pengaturan yang ada. Masukkan detail node baru, klik Simpan, dan penyimpanan akan diperbarui.


![image](assets/en/034.webp)


#### Layanan


Jika administrator server memutuskan untuk menginstal beberapa layanan untuk implementasi Lightning, layanan tersebut akan dicantumkan di sini. Dengan implementasi LND standar, administrator akan memiliki Ride The Lightning (RTL) sebagai alat standar untuk manajemen node.


#### Pengaturan BTC Lightning Wallet


Setelah menambahkan node Lightning ke toko pada langkah sebelumnya, pemilik toko masih dapat memilih untuk menonaktifkannya untuk toko mereka dengan menggunakan Toggle di bagian atas pengaturan Lightning.


![image](assets/en/035.webp)


#### Opsi Pembayaran Kilat


Pemilik toko dapat mengatur parameter berikut ini untuk meningkatkan pengalaman Lightning bagi pelanggan mereka.



- Menampilkan jumlah pembayaran Lightning di Satoshi.
- Tambahkan petunjuk lompatan untuk saluran pribadi ke Lightning Invoice.
- Satukan kode URL/QR pembayaran On-Chain dan Lightning pada saat pembayaran.
- Mengatur templat deskripsi untuk faktur kilat.


#### LNURL


Pemilik toko dapat memilih untuk menggunakan atau tidak menggunakan LNURL. URL Lightning Network, atau LNURL, adalah standar yang diusulkan untuk interaksi antara Lightning Payer dan penerima pembayaran. Singkatnya, LNURL adalah URL yang dikodekan bech32 yang diawali dengan LNURL. Lightning Wallet diharapkan untuk memecahkan kode URL, menghubungi URL, dan menunggu objek JSON dengan instruksi lebih lanjut, terutama tag yang mendefinisikan perilaku LNURL.



- Aktifkan LNURL
- Mode Klasik LNURL
  - Untuk kompatibilitas Wallet, URL yang dikodekan Bech32 (klasik) vs URL cleartext (mendatang)
- Izinkan penerima pembayaran untuk memberikan komentar.


### Contoh 1


#### Sambungkan ke Lightning dengan node internal (Administrator)


Opsi ini hanya tersedia jika Anda adalah Administrator dari instans ini atau jika Administrator telah mengubah pengaturan default sehingga pengguna dapat menggunakan lightning node internal.


Sebagai administrator, klik Lightning Wallet di bilah menu sebelah kiri. BTCPay Server akan meminta Anda untuk memilih salah satu dari dua opsi untuk menghubungkan Lightning Node: node internal atau node eksternal khusus. Klik "Gunakan node internal" dan kemudian klik "Simpan"


#### Mengelola simpul Lightning (RTL) Anda


Setelah terhubung ke node Lightning internal, BTCPay Server akan memperbarui dan menampilkan notifikasi "BTC Lightning node diperbarui", yang mengonfirmasi bahwa Anda telah menghubungkan Lightning ke toko Anda.


Mengelola simpul petir adalah tugas administrator server. Hal ini mencakup hal-hal berikut ini:


- Mengelola transaksi
- Mengelola likuiditas
  - Likuiditas masuk
  - Likuiditas keluar
- Mengelola rekan dan saluran
  - Rekan kerja yang terhubung
  - Biaya saluran
  - Status saluran
- Sering membuat cadangan status saluran.
- Memeriksa laporan perutean
- Atau, gunakan layanan seperti Loop.


Semua manajemen lightning node dilakukan sebagai standar dengan RTL (dengan asumsi Anda menggunakan implementasi LND). Administrator dapat mengklik Lightning Wallet mereka di BTCPay Server dan menemukan tombol untuk membuka RTL. Dasbor utama BTCPay Server sekarang diperbarui dengan Ubin Lightning Network, termasuk akses cepat ke RTL.


### Contoh 2


#### Terhubung ke petir dengan Alby


Saat terhubung dengan kustodian seperti Alby, pemilik toko harus terlebih dahulu membuat akun dan mengunjungi https://getalby.com/


![image](assets/en/036.webp)


Setelah membuat akun Alby, buka toko BTCPay Server Anda.


Langkah 1: Klik 'Siapkan simpul Lightning' di Dasbor atau 'Lightning' di bawah dompet.


![image](assets/en/037.webp)


Langkah 2: Masukkan kredensial koneksi Wallet Anda yang disediakan oleh Alby. Pada Dasbor Alby, klik pada Wallet. Di sini Anda akan menemukan "Kredensial Koneksi Wallet". Salin kredensial ini. Tempelkan kredensial dari Alby ke dalam bidang konfigurasi Koneksi di BTCPay Server.


![image](assets/en/038.webp)


Langkah 3: Setelah memberikan detail koneksi kepada BTCPay Server, klik tombol "Uji Koneksi" untuk memastikan koneksi berfungsi dengan baik. Perhatikan pesan "Koneksi ke lightning node berhasil" di bagian atas layar Anda. Ini mengonfirmasi bahwa semuanya berfungsi seperti yang diharapkan.


![image](assets/en/039.webp)


Langkah 4: Klik "Simpan," dan toko Anda sekarang terhubung ke node Lightning oleh Alby.


![image](assets/en/040.webp)


**Catatan!**


Jangan pernah mempercayai solusi Lightning kustodian dengan nilai lebih dari yang Anda rela kehilangan.


### Ringkasan Keterampilan


Di bagian ini, Anda sudah belajar:



- Cara menyambungkan simpul Lightning internal atau eksternal
- Isi dan fungsi berbagai ubin terkait Lightning di Dasbor
- Cara mengonfigurasi Lightning Wallet menggunakan Voltage Surge atau Alby


### Penilaian pengetahuan Tinjauan Praktis


Jelaskan beberapa opsi yang tersedia untuk menghubungkan Lightning Wallet ke toko Anda.


# Server BTCPay Interface


<partId>25e88b81-e1ab-515f-a035-09f2a3075556</partId>


## Ikhtisar dasbor


<chapterId>410ff28b-a272-5c91-93e0-48d5b28c53ab</chapterId>


BTCPay Server adalah paket perangkat lunak modular. Namun, ada standar yang harus dipatuhi oleh setiap BTCPay Server, dan standar ini akan mengatur interaksi antara Administrator dan pengguna. Dimulai dengan Dasbor. Titik masuk utama dari setiap Server BTCPay setelah masuk. Dasbor memberikan gambaran umum tentang kinerja toko Anda, saldo Wallet saat ini, dan transaksi dari 7 hari terakhir. Karena ini adalah tampilan modular, Plugin dapat menggunakan tampilan ini untuk keuntungan mereka dan membuat ubin mereka di Dasbor. Untuk kursus ini, kami hanya akan membahas plugin dan aplikasi standar, bersama dengan tampilan masing-masing, di seluruh BTCPay Server.


### Ubin Dasbor


Di dalam tampilan utama dasbor BTCPay Server terdapat beberapa ubin standar yang tersedia. Ubin-ubin ini dirancang untuk pemilik Toko atau Administrator untuk mengelola toko mereka dengan cepat dalam satu tinjauan.



- Keseimbangan Wallet
- Aktivitas transaksi
- Keseimbangan Petir (jika Petir diaktifkan di toko)
- Layanan Lightning (jika Lightning diaktifkan di toko)
- Transaksi terakhir.
- Faktur Terbaru
- Crowdfunding aktif saat ini
- Performa toko / barang terlaris.


### Keseimbangan Wallet


Ubin Saldo Wallet memberikan gambaran umum singkat tentang dana dan kinerja Wallet Anda. Ini dapat dilihat dalam mata uang BTC atau Fiat dalam grafik Mingguan, bulanan, atau tahunan.


![image](assets/en/041.webp)


### Aktivitas transaksi


Di samping ubin Saldo Wallet, Server BTCPay menampilkan ikhtisar singkat tentang Pembayaran yang tertunda, jumlah Transaksi dalam 7 hari terakhir, dan jika toko Anda telah mengeluarkan pengembalian dana. Mengklik tombol Kelola akan membawa Anda ke dalam pengelolaan pembayaran yang tertunda (pelajari lebih lanjut tentang pembayaran di bab Server BTCPay - Pembayaran).


![image](assets/en/042.webp)


### Keseimbangan Petir


Ini hanya terlihat apabila Lightning diaktifkan.


Ketika Administrator telah mengizinkan akses Lightning Network, dasbor BTCPay Server sekarang memiliki ubin baru dengan informasi node Lightning Anda. Berapa banyak BTC yang ada di saluran, bagaimana hal ini diseimbangkan secara lokal atau jarak jauh (likuiditas masuk atau keluar), jika saluran ditutup atau dibuka, dan berapa banyak Bitcoin yang dipegang On-Chain di node petir.


![image](assets/en/043.webp)


### Layanan Petir


Hal ini hanya terlihat apabila petir aktif.


Selain melihat saldo Lightning Anda di dasbor BTCPay Server, administrator juga akan melihat ubin untuk Layanan Lightning. Di sini, administrator dapat menemukan tombol cepat untuk alat yang mereka gunakan untuk mengelola node Lightning mereka; misalnya, Ride the Lightning adalah salah satu alat standar dengan BTCPay Server untuk manajemen node Lightning.


![image](assets/en/044.webp)


### Transaksi Terakhir


Ubin Transaksi Terbaru menampilkan transaksi terbaru toko Anda. Dengan satu klik, Administrator instance Server BTCPay sekarang dapat melihat transaksi terbaru dan melihat apakah diperlukan perhatian terhadap transaksi tersebut.


![image](assets/en/045.webp)


### Faktur terbaru


Ubin Faktur Terbaru menampilkan 6 faktur terbaru yang dibuat oleh Server BTCPay Anda, termasuk Status dan jumlah Invoice. Ubin ini juga menyertakan tombol "Lihat semua" untuk mengakses gambaran umum Invoice dengan mudah.


![image](assets/en/046.webp)


### Tempat Penjualan dan Crowdfunding


Karena BTCPay Server menyediakan satu set plugin atau aplikasi standar, Point Of Sale dan Crowdfund adalah dua plugin utama BTCPay Server. Dengan setiap toko dan Wallet, pengguna BTCPay Server dapat generate sebanyak mungkin Point Of Sales atau Crowdfund yang mereka inginkan. Masing-masing akan membuat ubin dasbor baru yang menunjukkan kinerja plugin.


![image](assets/en/047.webp)


Perhatikan sedikit perbedaan antara ubin Titik Penjualan dan Crowdfund. Administrator melihat item-item teratas yang terjual di ubin Titik Penjualan. Pada ubin Crowdfund, ini menjadi Top Perks. Kedua ubin memiliki tombol cepat untuk mengelola aplikasi masing-masing dan melihat faktur terbaru yang dibuat oleh item teratas atau fasilitas teratas.


![image](assets/en/048.webp)


**!* Catatan!**


Grafik saldo dan transaksi terakhir hanya tersedia untuk metode pembayaran On-Chain. Informasi tentang saldo dan transaksi Lightning Network ada di daftar yang harus dilakukan. Pada BTCPay Server Versi 1.6.0, saldo dasar Lightning Network tersedia.


### Ringkasan Keterampilan


Dalam bagian ini, Anda telah mempelajari yang berikut ini:



- Tata letak inti ubin pada halaman arahan utama dikenal sebagai Dasbor.
- Pemahaman dasar mengenai isi setiap ubin.


### Tinjauan Penilaian Pengetahuan


Daftarkan sebanyak mungkin ubin dari memori dari Dasbor.


## Server BTCPay - Pengaturan penyimpanan


<chapterId>e8faef7b-278d-550e-a511-bc3a442daf64</chapterId>


Di dalam perangkat lunak BTCPay Server, kami mengenal dua jenis pengaturan. Pengaturan khusus BTCPay Server Store, tombol pengaturan yang terdapat pada bilah menu sebelah kiri di bawah Dasbor, dan pengaturan BTCPay Server, yang terdapat pada bagian bawah bilah menu, tepat di atas Akun. Pengaturan khusus Server BTCPay Server hanya dapat dilihat oleh administrator Server.


Pengaturan toko terdiri atas banyak tab untuk mengkategorikan setiap rangkaian pengaturan.



- Umum
- Tarif
- Tampilan Pembayaran
- Akses Token
- Pengguna
- Peran
- Kait web
- Pemroses Pembayaran
- Email
- Formulir


### Umum


Pada tab Pengaturan Umum, pemilik toko mengatur branding dan default pembayaran. Pada pengaturan awal toko, nama toko diberikan; ini akan tercermin dalam pengaturan Umum di bawah Nama Toko. Di sini, pemilik toko juga dapat mengatur situs web mereka agar sesuai dengan merek dan ID Toko untuk dikenali oleh Administrator dalam database.


#### Pencitraan merek


Karena BTCPay Server adalah FOSS, pemilik toko dapat melakukan branding khusus agar sesuai dengan toko mereka. Atur warna merek, simpan logo merek Anda, dan tambahkan CSS khusus untuk halaman yang berhadapan dengan publik/pelanggan (Faktur, Permintaan Pembayaran, Tarik pembayaran)


#### Pembayaran


Dalam pengaturan pembayaran, pemilik toko dapat mengatur mata uang default toko mereka (baik Bitcoin atau mata uang fiat lainnya).


#### Izinkan siapa saja untuk membuat faktur


Pengaturan ini ditujukan untuk pengembang atau pembangun di atas BTCPay Server. Dengan mengaktifkan pengaturan ini untuk toko Anda, ini memungkinkan dunia luar untuk membuat faktur pada instance BTCPay Server Anda.


#### Menambahkan biaya tambahan (biaya jaringan) ke faktur


Fitur dalam BTCPay untuk melindungi pedagang dari serangan Dust atau klien dari biaya yang tinggi di kemudian hari ketika pedagang perlu memindahkan sejumlah besar Bitcoin sekaligus. Sebagai contoh, pelanggan membuat Invoice seharga $ 20 dan membayar sebagian, membayar $ 1 sebanyak 20 kali hingga Invoice dibayar penuh. Pedagang sekarang memiliki transaksi yang lebih besar, yang meningkatkan biaya Mining jika pedagang memutuskan untuk memindahkan dana tersebut di kemudian hari. Secara default, BTCPay menerapkan biaya jaringan tambahan pada jumlah total Invoice untuk menutupi biaya tersebut bagi pedagang ketika Invoice dibayarkan dalam beberapa transaksi. BTCPay menawarkan beberapa opsi untuk menyesuaikan fitur perlindungan ini. Anda dapat menerapkan biaya jaringan:



- Hanya jika pelanggan melakukan lebih dari satu kali pembayaran untuk Invoice (Dalam contoh di atas, jika pelanggan membuat Invoice seharga 20\$ dan membayar 1\$, maka total Invoice yang harus dibayar adalah 19\$ + biaya jaringan. Biaya jaringan diterapkan setelah pembayaran pertama)
- Pada setiap pembayaran (termasuk pembayaran pertama, dalam contoh kami, totalnya adalah 20\$ + biaya jaringan langsung, bahkan pada pembayaran pertama)
- Jangan pernah menambahkan biaya jaringan (menonaktifkan biaya jaringan sepenuhnya)


Meskipun melindungi dari transaksi Dust, hal ini juga dapat berdampak negatif terhadap bisnis jika tidak dikomunikasikan dengan benar. Pelanggan mungkin memiliki pertanyaan tambahan dan berpikir bahwa Anda menagih mereka secara berlebihan.


#### Invoice kedaluwarsa jika jumlah penuh belum dibayar setelahnya?


Pengatur waktu Invoice diatur ke 15 menit secara default. Pengatur waktu berfungsi sebagai mekanisme perlindungan terhadap volatilitas, karena mengunci jumlah Bitcoin sesuai dengan kurs Bitcoin ke fiat Exchange. Jika pelanggan tidak membayar Invoice dalam jangka waktu yang ditentukan, maka Invoice dianggap kedaluwarsa. Invoice dianggap "terbayar" segera setelah transaksi terlihat di Blockchain (dengan nol konfirmasi), dan dianggap "lengkap" ketika mencapai jumlah konfirmasi yang ditentukan oleh pedagang (biasanya 1-6). Pengatur waktu dapat disesuaikan dalam hitungan menit.


#### Pertimbangkan Invoice yang dibayarkan meskipun jumlah yang dibayarkan X% lebih sedikit dari yang diharapkan?


Ketika pelanggan menggunakan Exchange Wallet untuk membayar langsung untuk Invoice, Exchange akan dikenakan sedikit biaya. Ini berarti bahwa Invoice tersebut tidak dianggap telah selesai sepenuhnya. Invoice ditandai sebagai "dibayar sebagian". Anda dapat mengatur tingkat persentase di sini jika pedagang ingin menerima faktur yang kurang dibayar.


### Tarif


Di BTCPay Server, ketika Invoice dibuat, ia selalu membutuhkan harga Bitcoin-ke-fiat yang paling baru dan akurat. Ketika membuat toko baru di BTCPay Server, administrator akan diminta untuk mengatur sumber harga yang diinginkan. Setelah toko dibuat, pemilik toko dapat mengubah sumber harga mereka di tab ini kapan saja.


#### Skrip aturan tarif tingkat lanjut


Terutama digunakan oleh para pengguna yang memiliki kuasa. Jika diaktifkan, pemilik toko dapat membuat skrip seputar perilaku harga dan cara menagih pelanggan mereka.


#### Pengujian


Tempat pengujian cepat untuk pasangan mata uang pilihan Anda. Fitur ini juga mencakup kemampuan untuk memeriksa pasangan mata uang default melalui kueri REST.


### Tampilan Pembayaran


Tab Tampilan Checkout dimulai dengan pengaturan khusus Invoice dan metode pembayaran default, dan memungkinkan metode pembayaran tertentu ketika persyaratan yang ditetapkan terpenuhi.


#### Pengaturan Invoice


Metode pembayaran default. Server BTCPay, dalam konfigurasi standarnya, menawarkan tiga opsi.



- BTC (On-Chain)
- BTC (LNURL-pay)
- BTC (off-chain & Lightning)


Kita dapat mengatur parameter untuk toko kita, di mana pelanggan hanya akan berinteraksi dengan Lightning ketika harga kurang dari jumlah X, dan sebaliknya untuk transaksi On-Chain, ketika X lebih besar dari Y, selalu tampilkan opsi pembayaran On-Chain.


![image](assets/en/049.webp)


#### Pembayaran


Pada rilis BTCPay Server 1.7, Checkout Interface yang baru, Checkout V2, diperkenalkan. Sejak rilis 1.9 distandarisasi, administrator dan pemilik toko masih dapat mengatur checkout ke rilis sebelumnya. Dengan menggunakan tombol "Gunakan checkout klasik", pemilik toko dapat mengembalikan toko ke pengalaman checkout sebelumnya. BTCPay Server juga memiliki serangkaian preset tertentu untuk perdagangan Online atau pengalaman di dalam toko.


![image](assets/en/050.webp)


Ketika pelanggan berinteraksi dengan toko dan menghasilkan Invoice, ada waktu kedaluwarsa untuk Invoice tersebut. Secara default, BTCPay Server mengaturnya menjadi 5 menit, dan administrator dapat menyesuaikannya dengan preferensi mereka. Halaman checkout dapat disesuaikan lebih lanjut dengan memeriksa parameter berikut:



- Rayakan pembayaran dengan menunjukkan confetti
- Menampilkan tajuk toko (Nama dan logo)
- Tampilkan tombol "Bayar di Wallet"
- Menyatukan URL/QR pembayaran On-Chain dan off-chain
- Menampilkan jumlah pembayaran Lightning di Satoshi
- Mendeteksi bahasa secara otomatis saat pembayaran


![image](assets/en/051.webp)


Jika bahasa deteksi otomatis tidak diatur, BTCPay Server, secara default, akan menampilkan bahasa Inggris. Pemilik toko dapat mengubah pengaturan default ini ke bahasa yang diinginkan.


![image](assets/en/052.webp)


Klik pada menu tarik-turun, dan pemilik toko dapat mengatur judul HTML khusus untuk ditampilkan pada halaman checkout.


![image](assets/en/053.webp)


Untuk memastikan pelanggan mengetahui metode pembayaran mereka, pemilik toko dapat secara eksplisit mengatur kasir mereka untuk selalu meminta pengguna memilih metode pembayaran yang mereka sukai. Setelah Invoice dibayar, BTCPay Server memungkinkan pelanggan untuk kembali ke toko web. Pemilik toko dapat mengatur pengalihan ini untuk diterapkan secara otomatis setelah pelanggan membayar.


![image](assets/en/054.webp)


#### Tanda terima publik


Dalam pengaturan struk publik, pemilik toko dapat mengatur halaman struk menjadi publik, menampilkan daftar pembayaran di halaman struk dan kode QR agar pelanggan dapat mengaksesnya dengan mudah.


![image](assets/en/055.webp)


### Akses Token


Token akses digunakan untuk dipasangkan dengan integrasi e-commerce tertentu atau integrasi yang dibuat khusus.


![image](assets/en/056.webp)


### Pengguna


Pengguna toko adalah tempat pemilik toko dapat mengelola anggota stafnya, akun mereka, dan akses ke toko. Setelah anggota staf membuat akun mereka, pemilik toko dapat menambahkan pengguna tertentu ke toko sebagai pengguna Tamu atau pemilik. Untuk menentukan peran staf lebih lanjut, lihat bagian selanjutnya di "Pengaturan Toko Server BTCPay - Peran."


![image](assets/en/057.webp)


### Peran


Pemilik toko mungkin merasa peran standar pengguna tidak cukup signifikan. Dalam pengaturan peran khusus, pemilik toko dapat menentukan kebutuhan yang tepat untuk setiap peran dalam bisnis mereka.


(1) Untuk membuat peran baru, klik tombol "+ Tambah peran".


![image](assets/en/058.webp)


(2) Masukkan nama Peran, misalnya, "Kasir".


![image](assets/en/059.webp)


(3) Konfigurasikan izin individual untuk peran tersebut.



- Memodifikasi toko Anda.
- Kelola akun Exchange yang ditautkan ke toko Anda.
  - Lihat akun Exchange yang ditautkan ke toko Anda.
- Kelola pembayaran tarikan Anda.
- Buat pembayaran tarikan.
  - Buat pembayaran tarik yang tidak disetujui.
- Memodifikasi faktur.
  - Melihat faktur.
  - Membuat Invoice.
  - Buat faktur dari node petir yang terkait dengan toko Anda.
- Melihat toko Anda.
  - Melihat faktur.
  - Melihat permintaan pembayaran Anda.
  - Memodifikasi kait web toko.
- Ubah permintaan pembayaran Anda.
  - Melihat permintaan pembayaran Anda.
- Gunakan simpul petir yang terkait dengan toko Anda.
  - Melihat faktur kilat yang terkait dengan toko Anda.
  - Buat faktur dari node petir yang terkait dengan toko Anda.
- Menyetor dana ke rekening Exchange yang terhubung ke toko Anda.
- Menarik dana dari rekening Exchange ke toko Anda.
- Perdagangkan dana di akun Exchange toko Anda.


Ketika peran dibuat, nama akan ditetapkan dan tidak dapat diubah setelah dalam mode edit.


![image](assets/en/060.webp)


### Kait web


Di dalam BTCPay Server, cukup mudah untuk membuat "Webhook" baru. Pada pengaturan BTCPay Server Store - tab Webhooks, pemilik toko dapat dengan mudah membuat webhook baru dengan mengklik "+ Buat Webhook". Webhook memungkinkan BTCPay Server untuk mengirimkan peristiwa HTTP yang terkait dengan toko Anda ke server lain atau integrasi e-niaga.


![image](assets/en/061.webp)


Anda sekarang berada di tampilan untuk membuat Webhook. Pastikan Anda mengetahui URL Payload Anda dan tempelkan ke Server BTCPay Anda. Ketika Anda menempelkan URL muatan, di bawahnya akan muncul rahasia webhook. Salin rahasia webhook dan berikan di titik akhir. Ketika semuanya telah diatur, Anda dapat beralih di BTCPay Server ke "Pengiriman ulang otomatis." BTCPay Server akan mencoba mengirim ulang setiap pengiriman yang gagal setelah 10 detik, 1 menit, dan hingga 6 kali setelah 10 menit. Anda dapat beralih di antara setiap peristiwa atau menentukan peristiwa untuk kebutuhan Anda. Pastikan untuk mengaktifkan webhook dan tekan tombol "Tambahkan webhook" untuk menyimpannya.


![image](assets/en/062.webp)


Webhook tidak dimaksudkan untuk kompatibel dengan API Bitpay. Ada dua IPN yang terpisah (dalam istilah BitPay: "Pemberitahuan Pembayaran Instan") di BTCPay Server.



- Webhookp
- Pemberitahuan


Hanya gunakan URL Pemberitahuan saat Anda membuat faktur melalui API Bitpay.


### Pemroses Pembayaran


Pemroses pembayaran bekerja bersama dengan konsep Pembayaran di BTCPay Server. Agregator pembayaran untuk mengumpulkan beberapa transaksi dan mengirimkannya sekaligus. Dengan prosesor pembayaran, pemilik toko dapat mengotomatiskan pembayaran secara berkelompok. BTCPay Server menawarkan dua metode pembayaran otomatis: On-Chain dan off-chain (LN).


Pemilik toko dapat mengklik dan mengonfigurasi kedua prosesor pembayaran secara terpisah. Pemilik toko mungkin hanya ingin menjalankan prosesor On-Chain sekali setiap X jam, sedangkan prosesor off-chain dapat dijalankan setiap beberapa menit. Untuk On-Chain, Anda juga dapat menetapkan target untuk blok mana yang harus dimasukkan. Secara default, ini diatur ke 1 (atau blok berikutnya yang tersedia). Perhatikan bahwa pengaturan prosesor pembayaran off-chain hanya memiliki pengatur waktu interval dan tidak ada target blok. Pembayaran Lightning Network bersifat instan.


![image](assets/en/063.webp)

![image](assets/en/064.webp)


Pemilik toko hanya dapat mengonfigurasi prosesor On-Chain jika mereka memiliki Hot Wallet yang terhubung ke toko mereka.


![image](assets/en/065.webp)


Setelah menyiapkan prosesor Pembayaran, Anda dapat dengan cepat menghapus atau memodifikasinya dengan kembali ke tab prosesor Pembayaran di pengaturan BTCPay Server Store.


**Catatan**


Prosesor pembayaran On-Chain - Prosesor pembayaran On-Chain hanya dapat bekerja pada toko yang dikonfigurasi dengan Hot Wallet yang terhubung. Jika tidak ada Hot Wallet yang terhubung, Server BTCPay tidak akan menyimpan kunci Wallet dan tidak akan dapat memproses pembayaran secara otomatis.


### Email


BTCPay Server dapat menggunakan Email untuk Pemberitahuan atau, jika diatur dengan benar, untuk memulihkan akun yang dibuat pada instance. Sebagai standar, BTCPay Server tidak mengirim email ketika kata sandi hilang, misalnya.


![image](assets/en/066.webp)


Sebelum pemilik toko dapat mengatur aturan Email untuk memicu kejadian tertentu di toko mereka, mereka harus terlebih dahulu mengatur beberapa pengaturan email dasar. BTCPay Server memerlukan pengaturan ini untuk mengirim email untuk peristiwa yang terkait dengan toko Anda atau untuk pengaturan ulang kata sandi.


Server BTCPay mempermudah pengisian informasi ini dengan menggunakan Opsi "Isi Cepat":



- Gmail.com
- Yahoo.com
- Mailgun
- Office365
- SendGrid


Dengan menggunakan opsi pengisian cepat, BTCPay Server akan mengisi kolom untuk server dan port SMTP. Sekarang, pemilik toko hanya perlu mengisi kredensial mereka, termasuk Email Address, Login (yang biasanya sama dengan email Address Anda), dan kata sandi mereka. Opsi lanjutan dalam pengaturan email BTCPay Server adalah Nonaktifkan pemeriksaan keamanan Sertifikat TLS; secara default, opsi ini diaktifkan.


![image](assets/en/067.webp)


Dengan aturan Email, pemilik toko dapat mengatur peristiwa tertentu untuk memicu email ke alamat email tertentu.



- Invoice Dibuat
- Invoice Menerima Pembayaran
- Pengolahan Invoice
- Invoice Kedaluwarsa
- Invoice Mengendap
- Invoice Tidak valid
- Invoice Pembayaran Dilunasi


Jika pelanggan telah memberikan Email Address, pemicu ini juga dapat mengirimkan informasi kepada pelanggan. Pemilik toko dapat mengisi baris Subjek untuk memperjelas mengapa Email ini terjadi dan apa yang memicunya.


![image](assets/en/068.webp)


### Formulir


Karena BTCPay Server tidak mengumpulkan data apa pun, pemilik toko mungkin ingin menambahkan formulir khusus ke pengalaman checkout mereka; dengan cara ini, pemilik toko dapat mengumpulkan informasi tambahan dari pelanggan mereka. Pembangun Formulir BTCPay Server terdiri dari dua bagian: tampilan visual dan tampilan kode yang lebih canggih dari formulir.


Saat membuat formulir baru, Server BTCPay membuka jendela baru yang meminta informasi dasar tentang apa yang Anda inginkan dari formulir baru Anda. Pertama-tama, pemilik toko harus memberikan nama yang jelas untuk formulir baru mereka; nama ini tidak dapat diubah setelah ditetapkan.


![image](assets/en/069.webp)


Setelah pemilik toko memberikan nama pada formulir, Anda juga dapat mengalihkan sakelar untuk "Izinkan formulir untuk penggunaan publik" ke AKTIF, dan akan mengubah Green. Hal ini memastikan formulir digunakan di setiap lokasi yang berhadapan dengan pelanggan. Misalnya, jika pemilik toko membuat Invoice terpisah tidak melalui Point Of Sale mereka, mereka mungkin masih ingin mengumpulkan informasi dari pelanggan. Sakelar ini memungkinkan informasi tersebut dikumpulkan.


![image](assets/en/070.webp)


Setiap formulir dimulai dengan setidaknya 1 bidang formulir baru. Pemilik toko dapat memilih jenis kolom apa yang harus diisi.



- Teks
- Nomor
- Kata sandi
- Email
- URL
- Nomor telepon
- Tanggal
- Bidang tersembunyi
- Fieldset
- Area teks untuk komentar terbuka.
- Pemilih opsi


Setiap jenis dilengkapi dengan parameter yang harus diisi. Pemilik toko dapat mengaturnya sesuai dengan keinginannya. Di bawah kolom yang pertama kali dibuat, pemilik toko dapat menambahkan kolom baru ke formulir ini.


![image](assets/en/071.webp)


#### Formulir khusus tingkat lanjut


BTCPay Server juga memungkinkan Anda untuk membuat Formulir dalam kode. JSON, khususnya. Alih-alih melihat editor, pemilik toko dapat mengklik tombol KODE tepat di sebelah editor dan masuk ke kode Formulir mereka. Dalam definisi bidang, hanya bidang berikut yang dapat diatur; nilai bidang disimpan dalam metadata Invoice:



| Bidang | Deskripsi |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| .fields.constant | Jika true, .value harus diatur dalam definisi formulir, dan pengguna tidak akan dapat mengubah nilai bidang tersebut. (contoh: versi definisi formulir) |
| .fields.type | Jenis input HTML: text, radio, checkbox, password, hidden, button, color, date, datetime-local, month, week, time, email, number, range, search, url, select, tel |
| .fields.options | Jika .fields.type adalah select, daftar nilai yang dapat dipilih |
| .fields.options.text | Teks yang ditampilkan untuk opsi ini |
| .fields.options.value | Nilai bidang jika opsi ini dipilih |
| .fields.type=fieldset | Buat HTML fieldset di sekitar anak .fields.fields (lihat di bawah) |
| .fields.name | Nama properti JSON dari bidang seperti yang akan muncul di metadata faktur |
| .fields.value | Nilai default dari bidang |
| .fields.required | jika true, bidang tersebut wajib diisi |
| .fields.label | Label dari bidang |
| .fields.helpText | Teks tambahan untuk memberikan penjelasan bagi bidang tersebut. |
| .fields.fields | Anda dapat menyusun bidang Anda dalam sebuah hierarki, yang memungkinkan bidang turunan disarangkan di dalam metadata faktur. Struktur ini dapat membantu Anda mengatur dan mengelola informasi yang dikumpulkan dengan lebih baik, sehingga lebih mudah diakses dan diinterpretasikan. Misalnya, jika Anda memiliki formulir yang mengumpulkan informasi pelanggan, Anda dapat mengelompokkan bidang-bidang tersebut di bawah bidang induk yang disebut customer. Di dalam bidang induk ini, Anda mungkin memiliki bidang turunan seperti name, Email, dan address. |

Nama bidang mewakili nama properti JSON yang menyimpan nilai yang diberikan pengguna dalam metadata Invoice. Beberapa nama yang terkenal dapat ditafsirkan dan dimodifikasi untuk menyesuaikan pengaturan Invoice.



| Nama bidang      | Deskripsi             |
| ---------------- | ---------------------- |
| invoice_amount   | Jumlah faktur         |
| invoice_currency | Mata uang faktur      |

Anda dapat mengisi bidang Invoice secara otomatis dengan menambahkan string kueri ke URL formulir, seperti "?your_field=value".


Berikut ini beberapa kasus penggunaan fitur ini:



- Membantu input pengguna: Mengisi kolom dengan informasi pelanggan yang sudah diketahui untuk memudahkan mereka mengisi formulir. Misalnya, jika Anda sudah mengetahui email pelanggan Address, Anda dapat mengisi kolom email untuk menghemat waktu mereka.
- Personalisasi: Sesuaikan formulir berdasarkan preferensi atau segmentasi pelanggan. Misalnya, jika Anda memiliki tingkatan pelanggan yang berbeda, Anda bisa mengisi formulir dengan data yang relevan, seperti tingkat keanggotaan mereka atau penawaran khusus.
- Pelacakan: Lacak sumber kunjungan pelanggan menggunakan bidang tersembunyi dan nilai yang telah diisi sebelumnya. Misalnya, Anda dapat membuat tautan dengan nilai utm_media yang telah diisi sebelumnya untuk setiap saluran pemasaran (misalnya, Twitter, Facebook, Email). Hal ini membantu Anda menganalisis efektivitas upaya pemasaran Anda.
- Pengujian A/B: Bidang pra-isi dengan nilai yang berbeda untuk menguji versi formulir yang berbeda, sehingga Anda dapat mengoptimalkan pengalaman pengguna dan tingkat konversi.


### Ringkasan Keterampilan


Dalam bagian ini, Anda telah mempelajari yang berikut ini:



- Tata letak dan fungsi tab di Pengaturan Toko
- Banyak pilihan untuk menyempurnakan penanganan tarif Exchange yang mendasari, pembayaran parsial, pembayaran kurang, dan banyak lagi.
- Sesuaikan tampilan checkout, termasuk rantai utama yang bergantung pada harga vs. pemberdayaan Lightning pada faktur.
- Kelola tingkat akses toko dan izin di seluruh peran.
- Mengonfigurasi email otomatis dan pemicunya
- Buat formulir khusus untuk mengumpulkan informasi pelanggan tambahan pada saat pembayaran.


### Penilaian Pengetahuan


#### Ulasan KA


Apa perbedaan antara Pengaturan Toko dan Pengaturan Server?


#### KA Hipotetis


Jelaskan beberapa opsi yang mungkin Anda pilih di Tampilan Checkout > Pengaturan Invoice, dan alasannya.


## Server BTCPay - Pengaturan server


<chapterId>1dd858a2-49ea-586b-9bc1-75a65f508df6</chapterId>


Server BTCPay terdiri dari dua tampilan pengaturan yang berbeda. Satu didedikasikan untuk pengaturan Toko, dan yang lainnya untuk pengaturan Server. Yang terakhir ini hanya tersedia untuk administrator server dan bukan untuk pemilik toko. Administrator server dapat menambahkan pengguna, membuat peran khusus, mengonfigurasi server email, mengatur kebijakan, menjalankan tugas pemeliharaan, memeriksa semua layanan yang dilampirkan ke BTCPay Server, mengunggah file ke server, atau memeriksa Log.


### Pengguna


Seperti yang telah disebutkan pada bagian sebelumnya, Administrator Server dapat mengundang pengguna ke server mereka dengan menambahkannya ke tab Pengguna.


### Peran khusus di seluruh server


BTCPay Server memiliki dua jenis peran khusus: peran khusus khusus toko dan peran khusus di seluruh server dalam pengaturan BTCPay Server. Keduanya memiliki serangkaian izin yang serupa; namun, jika diatur melalui tab Pengaturan Server BTCpay - Peran, peran yang diterapkan akan berlaku di seluruh server dan berlaku untuk beberapa toko. Perhatikan tag "Server-wide" pada peran khusus di pengaturan Server.


![image](assets/en/072.webp)


### Peran khusus di seluruh server


Set izin peran khusus di seluruh server;



- Memodifikasi toko Anda.
- Kelola akun Exchange yang ditautkan ke toko Anda.
  - Lihat akun Exchange yang ditautkan ke toko Anda.
- Kelola pembayaran tarikan Anda.
- Buat pembayaran tarikan.
  - Buat pembayaran tarik yang tidak disetujui.
- Memodifikasi faktur.
  - Melihat faktur.
  - Buat Invoice.
  - Buat faktur dari node petir yang terkait dengan toko Anda.
- Melihat toko Anda.
  - Melihat faktur.
  - Melihat permintaan pembayaran Anda.
  - Memodifikasi kait web toko.
- Ubah permintaan pembayaran Anda.
  - Melihat permintaan pembayaran Anda.
- Gunakan simpul petir yang terkait dengan toko Anda.
  - Melihat faktur kilat yang terkait dengan toko Anda.
  - Buat faktur dari node petir yang terkait dengan toko Anda.
- Menyetor dana ke rekening Exchange yang terhubung dengan toko Anda.
- Menarik dana dari rekening Exchange ke toko Anda.
- Perdagangkan dana di akun Exchange toko Anda.


**!* Catatan!**


Ketika peran dibuat, nama akan ditetapkan dan tidak dapat diubah setelah dalam mode edit.


### Email


Pengaturan Email Seluruh Server terlihat mirip dengan pengaturan email khusus Toko. Namun, pengaturan ini tidak hanya menangani pemicu untuk toko atau log administrator, tetapi juga pemicu untuk peristiwa lain. Pengaturan Email ini juga membuat pemulihan kata sandi tersedia di BTCPay Server saat Login. Cara kerjanya mirip dengan pengaturan khusus Toko; administrator dapat dengan cepat mengisi parameter Email mereka dan memasukkan kredensial email mereka, sehingga server dapat mengirim email.


![image](assets/en/073.webp)


### Kebijakan


Administrator kebijakan Server BTCPay dapat mengatur berbagai pengaturan pada topik-topik seperti pengaturan Pengguna yang Sudah Ada, pengaturan Pengguna Baru, pengaturan Pemberitahuan, dan pengaturan Pemeliharaan. Pengaturan ini dimaksudkan untuk mendaftarkan pengguna baru sebagai administrator atau pengguna biasa, atau untuk menyembunyikan Server BTCPay dari mesin pencari dengan menambahkannya ke header server Anda.


![image](assets/en/074.webp)


#### Pengaturan pengguna yang ada


Opsi yang tersedia di sini terpisah dari peran khusus. Izin tambahan ini dapat membuat toko atau pemiliknya rentan terhadap serangan. Kebijakan yang dapat ditambahkan ke pengguna yang sudah ada:



- Izinkan non-admin untuk menggunakan node Lightning internal di toko mereka.
  - Ini akan memungkinkan pemilik toko untuk menggunakan simpul Lightning administrator server dan, oleh karena itu, dananya! Hati-hati, ini bukan solusi untuk memberikan akses ke Lightning.
- Izinkan non-admin untuk membuat dompet Hot untuk toko mereka.
  - Ini akan memungkinkan siapa pun yang memiliki akun di instance BTCPay Server Anda untuk membuat dompet Hot dan menyimpan seed pemulihan mereka di server Administrator. Hal ini dapat membuat Administrator bertanggung jawab untuk menyimpan dana pihak ketiga!
- Izinkan non-admin untuk mengimpor dompet Hot untuk toko mereka.
  - Serupa dengan topik sebelumnya tentang membuat dompet Hot, kebijakan ini mengizinkan untuk mengimpor Hot Wallet, dengan bahaya yang sama seperti yang disebutkan di bagian membuat dompet Hot.


![image](assets/en/075.webp)


#### Pengaturan pengguna baru


Kita dapat mengatur beberapa pengaturan penting untuk mengelola pengguna baru yang masuk ke server. Kita dapat mengatur email konfirmasi untuk pendaftaran baru, menonaktifkan pembuatan pengguna baru melalui layar login, dan membatasi akses non-admin ke pembuatan pengguna melalui API.



- Memerlukan email konfirmasi untuk pendaftaran.
  - Administrator server harus sudah menyiapkan server Email.
- Menonaktifkan pendaftaran pengguna baru di server
- Nonaktifkan akses non-admin ke titik akhir API pembuatan pengguna.


Secara default, Server BTCPay telah mengaktifkan "Nonaktifkan pendaftaran pengguna baru di server" dan mematikan akses non-admin ke titik akhir API pembuatan pengguna. Hal ini dilakukan untuk keamanan, sehingga orang sembarangan yang menemukan login BTCPay Anda tidak dapat membuat akun.


![image](assets/en/076.webp)


#### Pengaturan Pemberitahuan


![image](assets/en/077.webp)


#### Pengaturan Pemeliharaan


BTCPay Server adalah proyek Open Source yang berada di GitHub. Setiap kali BTCPay Server merilis versi baru dari perangkat lunak, Administrator dapat diberitahu bahwa versi baru telah tersedia. Administrator mungkin juga ingin menghindari mesin pencari (seperti Google, Yahoo, dan DuckDuckGo) untuk mengindeks domain BTCPay Server. Karena BTCPay Server adalah FOSS, pengembang di seluruh dunia mungkin ingin membuat fitur baru. BTCPay Server memiliki fitur eksperimental yang, ketika diaktifkan, memungkinkan administrator untuk menggunakan fitur yang tidak dimaksudkan untuk produksi, melainkan untuk tujuan pengujian.



- Periksa rilis di GitHub dan beri tahu ketika versi BTCPay Server baru tersedia.
- Cegah mesin pencari untuk mengindeks situs ini
- Mengaktifkan fitur eksperimental.


![image](assets/en/078.webp)


#### Plugin


BTCPay Server dapat menambahkan Plugin dan memperluas rangkaian fiturnya. Plugin, secara default, dimuat dari repositori pembuat plugin BTCPay Server. Namun, seorang administrator dapat memilih untuk melihat plugin dalam status Pra-rilis, dan jika pengembang plugin mengizinkannya, administrator server sekarang dapat menginstal plugin versi beta.


![image](assets/en/079.webp)


##### Pengaturan Kustomisasi


Penerapan BTCPay Server standar akan dapat diakses melalui domain yang diatur selama instalasi. Namun, administrator server dapat memetakan ulang domain root dan menampilkan salah satu aplikasi yang dibuat dari toko tertentu. Administrator Server juga dapat memetakan domain tertentu ke aplikasi tertentu.



- Menampilkan aplikasi di root situs web
  - Menampilkan daftar aplikasi yang mungkin ditampilkan di domain root.


![image](assets/en/080.webp)



- Memetakan domain tertentu ke aplikasi tertentu.
  - Ketika Anda mengklik untuk mengatur domain tertentu untuk aplikasi tertentu, Administrator dapat mengatur sebanyak mungkin domain yang diarahkan ke aplikasi tertentu sesuai kebutuhan.


![image](assets/en/081.webp)


#### Penjelajah blok


BTCPay Server, sebagai standar, dilengkapi dengan Mempool.space sebagai Block explorer untuk transaksi. Ketika BTCPay Server membuat Invoice baru dan sebuah transaksi terkait dengannya, pemilik toko dapat mengklik untuk membuka transaksi. BTCPay Server akan, secara default, mengarahkan ke Mempool.space sebagai Block explorer; namun, Administrator server dapat mengubahnya ke opsi yang mereka inginkan.


![image](assets/en/082.webp)


### Layanan


Tab "Pengaturan Server BTCPay: Layanan" adalah ikhtisar komponen yang digunakan Server BTCPay Anda. Layanan yang digunakan Server BTCPay Anda mungkin berbeda-beda, tergantung pada metode penerapan.


Administrator Server BTCPay dapat mengklik "Lihat informasi" di belakang setiap layanan untuk membukanya dan mengatur pengaturan tertentu.


![image](assets/en/083.webp)


#### LND (gRPC)


BTCPay mengekspos layanan GRPC LND untuk konsumsi luar; Anda akan menemukan informasi koneksi di menu pengaturan khusus ini; dompet yang kompatibel tercantum di sini. Server BTCPay juga menyediakan kode QR untuk koneksi, yang dapat dipindai dan diterapkan di Wallet seluler.


Administrator server dapat membuka detail lebih lanjut untuk melihat.



- Rincian tuan rumah
- Penggunaan SSL
- Macaroon
- AdminMacaroon
- FakturMacaroon
- HanyaBacaMacaroon
- Rangkaian Cipher SSL GRPC (GRPC_SSL_CIPHER_SUITES)


#### LND (REST)


BTCPay mengekspos layanan REST LND untuk konsumsi luar; Anda dapat menemukan informasi koneksi di [sini](https://docs.btcpayserver.org/FAQ/LightningNetwork/#how-to-find-node-info-and-open-a-direct-channel-with-a-store-using-btcpay); dompet yang kompatibel terdaftar di [sini](https://docs.btcpayserver.org/FAQ/Wallet/#can-i-use-a-hardware-wallet-with-btcpay-server). Di antara dompet yang kompatibel adalah Joule, Alby, dan ZeusLN. BTCPay Server menyediakan kode QR untuk koneksi, yang dapat dipindai dan diterapkan di Wallet yang kompatibel.



- REST URI
- Macaroon
- AdminMacaroon
- FakturMacaroon
- HanyaBacaMacaroon


#### LND seed Cadangan


Cadangan LND seed berguna untuk memulihkan dana dari LND Wallet jika terjadi kerusakan server. Karena node Lightning adalah Hot-Wallet, Anda dapat menemukan informasi rahasia seed di halaman ini.


LND mendokumentasikan proses pemulihan. Lihat https://github.com/lightningnetwork/LND/blob/master/docs/recovery.md untuk dokumentasi.


#### Ride The Lightning


Ride the Lightning adalah alat manajemen node Lightning yang dibangun sebagai perangkat lunak Open Source. BTCPay Server menggunakan RTL sebagai komponen manajemen node Lightning dalam tumpukannya. Administrator BTCPay Server dapat mengakses RTL melalui pengaturan Server - tab Layanan atau dengan mengklik Lightning Wallet.


#### Full node P2P


Administrator server mungkin ingin menghubungkan node Bitcoin mereka ke Wallet seluler. Halaman ini memberikan informasi tentang cara menghubungkan dari jarak jauh ke Full node Anda melalui protokol P2P. Pada saat penulisan kursus ini, BTCPay Server mencantumkan dompet Blockstream Green dan Wasabi sebagai dompet yang kompatibel. BTCPay Server menyediakan kode QR untuk koneksi, yang dapat dipindai dan diterapkan di Wallet yang kompatibel.


#### Full node RPC


Halaman ini menampilkan informasi untuk menghubungkan jarak jauh ke Full node Anda melalui protokol RPC.


#### SSH


SSH digunakan untuk tujuan pemeliharaan. BTCPay Server menampilkan perintah koneksi awal untuk mencapai Server Anda dan kunci publik SSH yang diotorisasi untuk terhubung ke Server Anda. Administrator Server mungkin ingin menonaktifkan perubahan SSH melalui UI Server BTCPay.


#### DNS Dinamis


DNS Dinamis memungkinkan Anda memiliki nama DNS yang stabil yang mengarah ke Server Anda, meskipun IP Address Anda berubah secara teratur. Hal ini direkomendasikan jika Anda meng-hosting Server BTCPay di rumah dan ingin memiliki domain clearnet untuk mengakses Server Anda.


Perhatikan bahwa Anda perlu mengonfigurasi instalasi NAT dan BTCPay Server Anda dengan benar untuk mendapatkan sertifikat HTTPS.


### Tema


BTCPay Server, sebagai standar, hadir dengan dua tema: Mode Terang dan Gelap. Ini dapat diubah dengan mengklik Akun di kiri bawah dan beralih antara tema Gelap dan tema Terang. Administrator BTCPay Server dapat menambahkan tema mereka sendiri dengan menyediakan tema CSS khusus.


Administrator dapat memperluas tema Terang/Gelap dengan menambahkan CSS kustom mereka sendiri atau mengatur tema kustom mereka sebagai kustom penuh.


![image](assets/en/084.webp)


#### Pencitraan Merek Server


Administrator server dapat mengubah branding BTCPay Server dengan mengatur branding di seluruh server perusahaan Anda. Karena BTCPay Server adalah FOSS, administrator server dapat memberi label putih pada perangkat lunak dan menyesuaikan tampilan agar sesuai dengan bisnis mereka.


![image](assets/en/085.webp)


### Pemeliharaan


Sebagai administrator server, pengguna Anda mengharapkan Anda untuk merawat Server dengan baik. Di dalam tab Pemeliharaan Server BTCPay, admin dapat melakukan beberapa pemeliharaan penting. Tetapkan nama domain ke instance Server BTCPay, Mulai ulang atau bersihkan Server. Mungkin yang paling penting, jalankan pembaruan.


BTCPay Server adalah proyek Open Source dan sering diperbarui. Setiap rilis baru diumumkan melalui Notifikasi BTCPay Server Anda atau di saluran resmi yang digunakan BTCPay Server untuk berkomunikasi.


![image](assets/en/086.webp)


#### Nama domain


Setelah Server BTCPay disiapkan, administrator mungkin ingin mengubah dari Domain aslinya. Di dalam tab Pemeliharaan, administrator dapat mengubah Domain. Setelah mengklik konfirmasi dan menyiapkan catatan DNS yang tepat pada Domain, BTCPay Server akan memperbarui dan memulai ulang untuk kembali ke Domain yang baru.


![image](assets/en/087.webp)


#### Mulai ulang


Mulai ulang Server BTCPay dan layanan terkait.


![image](assets/en/088.webp)


#### Bersih


BTCPay Server berjalan dengan komponen Docker; dengan pembaruan, mungkin ada sisa-sisa gambar Docker, file temp, dll. Administrator server dapat mengosongkan ruang dengan menjalankan skrip Clean.


![image](assets/en/089.webp)


#### Memperbarui


Ini adalah opsi paling penting di tab Pemeliharaan. BTCPay Server dibangun oleh komunitas, dan oleh karena itu, siklus pembaruannya lebih sering daripada kebanyakan produk perangkat lunak. Ketika BTCPay Server memiliki rilis baru, administrator akan diberitahu di pusat notifikasi mereka. Dengan mengklik tombol pembaruan, BTCPay Server akan memeriksa GitHub untuk rilis terbaru, memperbarui Server, dan memulai ulang. Sebelum memperbarui, administrator server selalu disarankan untuk membaca catatan rilis yang didistribusikan melalui saluran resmi BTCPay Server.


![image](assets/en/090.webp)


### Log


Menghadapi masalah tidak pernah menyenangkan. Dokumen ini menguraikan alur kerja yang paling umum dan langkah-langkah untuk mengidentifikasi dan menyelesaikan masalah Anda secara efisien, baik secara mandiri maupun dengan bantuan komunitas.


Mengidentifikasi masalah sangat penting.


#### Mereplikasi masalah


Pertama dan terutama, cobalah untuk menentukan kapan masalah terjadi. Cobalah untuk mereplikasi masalahnya. Coba perbarui dan mulai ulang Server Anda untuk memverifikasi bahwa Anda dapat mereproduksi masalah tersebut. Jika hal ini dapat menjelaskan masalah Anda dengan lebih baik, ambil tangkapan layar.


##### Memperbarui server


Periksa versi Server BTCPay Anda jika versi tersebut jauh lebih lama daripada [versi terbaru](https://github.com/btcpayserver/btcpayserver/releases) Server BTCPay. Memperbarui Server Anda dapat menyelesaikan masalah ini.


##### Memulai ulang server


Memulai ulang Server Anda adalah cara mudah untuk menyelesaikan banyak masalah Server BTCPay yang paling umum. Anda mungkin perlu melakukan SSH ke Server Anda agar dapat memulai ulang.


##### Memulai ulang layanan


Anda mungkin hanya perlu memulai ulang layanan tertentu dalam penerapan Server BTCPay Anda untuk beberapa masalah, seperti memulai ulang kontainer letsencrypt untuk memperbarui sertifikat SSL.


```bash
sudo su -
cd btcpayserver-docker
docker restart letsencrypt-nginx-proxy-companion
```


Gunakan docker ps untuk menemukan nama layanan berbeda yang ingin Anda mulai ulang.


#### Melihat-lihat log


Log dapat memberikan informasi yang sangat penting. Pada paragraf berikut, kami akan menjelaskan cara mendapatkan informasi log untuk berbagai bagian BTCPay.


##### Log BTCPay


Sejak v1.0.3.8, Anda dapat dengan mudah mengakses log BTCPay Server dari ujung depan. Jika Anda adalah admin server, buka Pengaturan Server > Log dan buka file log. Jika Anda tidak mengetahui arti dari kesalahan tertentu dalam log, sebutkanlah saat melakukan pemecahan masalah.


Jika Anda menginginkan log yang lebih terperinci dan menggunakan penerapan Docker, Anda dapat melihat log kontainer Docker tertentu menggunakan baris perintah. Lihat [instruksi untuk ssh](https://docs.btcpayserver.org/FAQ/ServerSettings/#how-to-ssh-into-my-btcpay-running-on-vp%C2%80) ini ke dalam sebuah instans BTCPay yang berjalan di VPS.


Di halaman berikutnya, daftar umum nama-nama kontainer yang digunakan untuk BTCPay Server.


Jalankan perintah di bawah ini untuk mencetak log berdasarkan nama kontainer. Ganti nama kontainer untuk melihat log kontainer lainnya.


```bash
sudo su -
cd btcpayserver-docker
docker ps
docker logs --tail 100 generated_btcpayserver_1
```



| Catatan untuk | Nama Kontainer                     |
| ------------ | --------------------------------- |
| BTCPayServer | generated_btcpayserver_1          |
| NBXplorer    | generated_nbxplorer_1             |
| Bitcoind     | btcpayserver_bitcoind             |
| Postgres     | generated_postgres_1              |
| proxy        | letsencrypt-nginx-proxy-companion |
| Nginx        | nginx-gen                         |
| Nginx        | nginx                             |
| c-lightning  | btcpayserver_clightning_bitcoin   |
| LND          | btcpayserver_lnd_bitcoin          |
| RTL          | generated_lnd_bitcoin_rtl_1       |
| Thunderhub   | generated_bitcoin_thub_1          |
| LibrePatron  | librepatron                       |
| Tor          | tor-gen                           |
| Tor          | tor                               |

###### Lightning Network LND - Docker


Ada beberapa cara untuk mengakses log LND Anda saat menggunakan Docker. Pertama, masuk sebagai root:


```bash
sudo su -
Navigate to the correct directory:
cd btcpayserver-docker
# Find container name:
docker ps
Print logs by container name:
docker logs --tail 100 btcpayserver_lnd_bitcoin
```


Sebagai alternatif, Anda dapat dengan cepat mencetak log dengan menggunakan ID kontainer (hanya karakter ID unik pertama yang diperlukan, seperti dua karakter paling kiri):


```bash
docker logs 'add your container ID'
```


Jika, karena alasan apa pun, Anda membutuhkan lebih banyak log


```bash
sudo su -
cd /var/lib/docker/volumes/generated_lnd_bitcoin_datadir/\_data/logs/ bitcoin/mainnet/
ls
```


Anda akan melihat sesuatu seperti


```bash
lnd.log lnd.log.13 lnd.log.15 lnd.log.16.gz lnd.log.17.gz
```


Untuk mengakses log yang tidak terkompresi dari log tersebut, lakukan `cat LND.log` atau jika Anda menginginkan log yang lain, gunakan `cat LND.log.15`.


Untuk mengakses log terkompresi dalam `.gzip`, gunakan `gzip -d LND.log.16.gz` (dalam kasus ini, kita akan mengakses `LND.log.16.gz`). Ini akan memberikan Anda sebuah file baru, di mana Anda dapat melakukan `cat LND.log.16`. Jika cara di atas tidak berhasil, Anda mungkin perlu menginstal gzip terlebih dahulu dengan `sudo apt-get install gzip`.


###### Lightning Network c-petir - Docker


```bash
sudo su -
docker ps
# Find the c-lightning container ID.
docker logs 'add your container ID here'
```


Sebagai alternatif, gunakan ini:


```bash
docker logs --tail 100 btcpayserver_clightning_bitcoin
```


Anda juga bisa mendapatkan informasi log dengan perintah c-lightning CLI.


```bash
bitcoin-lightning-cli.sh getlog
```


#### Bitcoin Log Node


Selain [melihat log](https://docs.btcpayserver.org/Troubleshooting/#2-looking-through-the-logs) dari kontainer bitcoind Anda, Anda juga dapat menggunakan salah satu dari [perintah bitcoin-cli](https://developer.Bitcoin.org/reference/RPC/index.html)


[(membuka jendela baru)](https://developer.Bitcoin.org/reference/RPC/index.html) untuk mendapatkan informasi dari node Bitcoin Anda. BTCPay menyertakan skrip untuk memungkinkan Anda berkomunikasi dengan node Bitcoin dengan mudah.


Di dalam folder btcpayserver-docker, dapatkan informasi Blockchain menggunakan node Anda:


```bash
bitcoin-cli.sh getblockchaininfo
```


### File


BTCPay Server memiliki sistem file lokal, yang memungkinkannya untuk mengunggah aset toko (produk), Logo, dan merek langsung ke Server. Sistem file server hanya dapat diakses oleh Administrator Server; pemilik toko dapat mengunggah logo atau merek mereka di tingkat toko.


Ketika administrator Server berada di tab Penyimpanan File, Anda dapat langsung mengunggah ke Server Anda atau mengubah penyedia penyimpanan file ke sistem file Lokal atau Azure Blob Storage.


![image](assets/en/091.webp)


![image](assets/en/092.webp)


### Ringkasan Keterampilan


Dalam bagian ini, Anda telah mempelajari yang berikut ini:



- Perbedaan antara pengaturan Store dan Server, khususnya yang berhubungan dengan Pengguna, Peran, dan Email
- Tetapkan kebijakan di seluruh server untuk penggunaan dan pembuatan Lightning atau Bitcoin Hot Wallet, pendaftaran pengguna baru, dan notifikasi email.
- Cara menambahkan tema khusus (bukan opsi terang/gelap sederhana yang disediakan) serta membuat logo khusus
- Melakukan tugas pemeliharaan server sederhana melalui GUI yang disediakan
- Memecahkan masalah, termasuk mengambil detail untuk kontainer Docker atau simpul Anda
- Mengelola penyimpanan file


### Penilaian pengetahuan


#### Tinjauan Konseptual KA


Apa perbedaan Peran yang ditetapkan melalui Pengaturan Server vs Pengaturan Toko, dan apa yang menjelaskan potensi penggunaan salah satunya dibandingkan yang lain?


#### Tinjauan Praktis KA


Jelaskan beberapa kasus penggunaan yang mungkin diaktifkan di tab Kebijakan.


#### Tinjauan Praktis KA


Jelaskan beberapa tindakan yang mungkin dilakukan secara rutin oleh administrator di tab Pemeliharaan.


## Server BTCPay - Pembayaran


<chapterId>e2b71ff9-3f4f-5e71-9771-8e03fbbef00f</chapterId>


Invoice adalah dokumen yang diterbitkan penjual kepada pembeli untuk menagih pembayaran.


Di BTCPay Server, Invoice mewakili dokumen yang harus dibayar dalam interval waktu yang ditentukan dengan tarif Exchange yang tetap. Faktur memiliki tanggal kedaluwarsa karena mengunci kurs Exchange dalam jangka waktu tertentu, sehingga melindungi penerima dari fluktuasi harga.


Inti dari BTCPay Server adalah kemampuan untuk bertindak sebagai sistem manajemen Bitcoin Invoice. Invoice adalah alat penting untuk melacak dan mengelola pembayaran yang diterima.


Kecuali jika Anda menggunakan [Wallet](https://docs.btcpayserver.org/Wallet/) yang sudah terpasang untuk menerima pembayaran secara manual, semua pembayaran di dalam toko akan ditampilkan di halaman Faktur. Halaman ini secara kumulatif mengurutkan pembayaran berdasarkan tanggal dan berfungsi sebagai sumber daya pusat untuk manajemen Invoice dan pemecahan masalah pembayaran.


![image](assets/en/093.webp)


### Umum


#### Status Invoice


Tabel di bawah ini mencantumkan dan menjelaskan status Invoice standar di BTCPay, bersama dengan tindakan umum yang disarankan. Tindakan hanyalah rekomendasi. Terserah kepada pengguna untuk menentukan tindakan terbaik untuk kasus penggunaan dan bisnis mereka.



| Status Faktur | Deskripsi | Tindakan |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| New | Belum dibayar, timer faktur belum kedaluwarsa | Tidak ada |
| New (paidPartial) | Dibayar, tidak lunas, timer faktur belum kedaluwarsa | Tidak ada |
| Expired | Belum dibayar, timer faktur sudah kedaluwarsa | Tidak ada |
| Expired (paidPartial) ** | Dibayar, tidak lunas, dan sudah kedaluwarsa | Hubungi pembeli untuk pengembalian dana atau minta pelunasan. Opsional: tandai faktur sebagai settled atau invalid |
| Expired (paidLate) | Dibayar lunas setelah timer faktur kedaluwarsa | Hubungi pembeli untuk pengembalian dana atau proses pesanan jika konfirmasi terlambat dapat diterima. |
| Settled (paidOver) | Dibayar melebihi jumlah faktur, lunas, menerima konfirmasi yang cukup | Hubungi pembeli untuk pengembalian dana kelebihan, atau opsional tunggu pembeli menghubungi Anda |
| Processing | Dibayar lunas, tetapi belum menerima konfirmasi yang cukup sesuai pengaturan toko | Hubungi pembeli untuk pengembalian dana kelebihan, atau opsional tunggu pembeli menghubungi Anda |
| Processing (paidOver) | Dibayar melebihi jumlah faktur, belum menerima konfirmasi yang cukup | Tunggu hingga settled, lalu hubungi pembeli untuk pengembalian dana kelebihan, atau tunggu dihubungi |
| Settled | Dibayar lunas, menerima konfirmasi yang cukup di toko | Penuhi pesanan |
| Settled (marked) | Status diubah secara manual menjadi settled dari status processing atau invalid | Admin toko telah menandai pembayaran sebagai settled |
| Invalid* | Dibayar, tetapi gagal menerima konfirmasi yang cukup dalam waktu yang ditentukan di pengaturan toko | Periksa transaksi di blockchain explorer; jika konfirmasi sudah cukup, tandai sebagai settled |
| Invalid (marked) | Status diubah secara manual menjadi invalid dari status settled atau expired | Admin toko telah menandai pembayaran sebagai invalid |
| Invalid (paidOver) | Dibayar lebih dari jumlah faktur, tetapi gagal menerima konfirmasi yang cukup dalam waktu yang ditentukan | Periksa transaksi di blockchain explorer; jika konfirmasi sudah cukup, tandai sebagai settled |

#### Detail Invoice


Halaman detail Invoice berisi semua informasi yang terkait dengan Invoice.


Informasi Invoice dibuat secara otomatis berdasarkan status Invoice, tarif Exchange, dll. Informasi produk dibuat secara otomatis jika Invoice dibuat dengan informasi produk, seperti di aplikasi Point of Sale.


#### Penyaringan Invoice


Faktur dapat difilter melalui filter cepat yang terletak di sebelah tombol pencarian atau filter lanjutan, yang dapat dialihkan dengan mengklik tautan (Bantuan) di bagian atas. Pengguna dapat memfilter faktur berdasarkan toko, ID pesanan, ID barang, status, atau tanggal.


#### Ekspor Invoice


Faktur Server BTCPay dapat diekspor dalam format CSV atau JSON. Untuk informasi lebih lanjut tentang ekspor dan akuntansi Invoice.


#### Pengembalian dana Invoice


Jika, karena alasan apa pun, Anda ingin mengeluarkan pengembalian dana, Anda dapat dengan mudah membuat pengembalian dana dari tampilan Invoice.


#### Mengarsipkan faktur


Sebagai akibat dari tidak adanya fitur penggunaan ulang Address dari BTCPay Server, adalah hal yang umum untuk melihat banyak faktur kadaluarsa di halaman Invoice toko Anda. Untuk menyembunyikannya dari pandangan Anda, pilih faktur tersebut dalam daftar dan tandai sebagai diarsipkan. Faktur yang telah ditandai sebagai diarsipkan tidak akan dihapus. Pembayaran ke Invoice yang diarsipkan akan tetap terdeteksi oleh Server BTCPay Anda (status paidLate). Anda dapat melihat faktur yang diarsipkan kapan saja dengan memilih faktur yang diarsipkan dari menu tarik-turun filter pencarian.


#### Mata Uang Default


Mata uang default toko, yang ditetapkan di wizard pembuatan toko.


#### Izinkan siapa saja untuk membuat Invoice


Anda harus mengaktifkan opsi ini jika Anda ingin mengizinkan dunia luar untuk membuat faktur di toko Anda. Opsi ini hanya berguna jika Anda menggunakan tombol pembayaran atau jika Anda menerbitkan faktur melalui API atau situs web HTML pihak ketiga. Aplikasi PoS telah diotorisasi sebelumnya dan tidak memerlukan pengaturan ini untuk diaktifkan agar pengunjung acak dapat membuka toko POS Anda dan membuat Invoice.


#### Menambahkan biaya tambahan (biaya jaringan) ke Invoice



- Hanya jika pelanggan melakukan lebih dari satu pembayaran untuk Invoice
- Pada setiap pembayaran
- Jangan pernah menambahkan biaya jaringan


#### Invoice kedaluwarsa jika jumlah penuh belum dibayar setelah .. Menit.


Pengatur waktu Invoice diatur ke 15 menit secara default. Pengatur waktu berfungsi sebagai mekanisme perlindungan terhadap volatilitas, karena mengunci jumlah mata uang kripto berdasarkan nilai tukar kripto-ke-fiat. Jika pelanggan tidak membayar Invoice dalam jangka waktu yang ditentukan, maka Invoice dianggap kedaluwarsa. Invoice dianggap "terbayar" segera setelah transaksi terlihat di Blockchain (dengan nol konfirmasi), dan dianggap "lengkap" ketika mencapai jumlah konfirmasi yang telah ditentukan oleh pedagang (biasanya 1-6). Pengatur waktu dapat disesuaikan.


#### Pertimbangkan Invoice yang dibayarkan meskipun jumlah yang dibayarkan ..% lebih kecil dari yang diharapkan.


Dalam situasi di mana pelanggan menggunakan Exchange Wallet untuk membayar langsung untuk Invoice, Exchange akan dikenakan biaya yang kecil. Ini berarti bahwa Invoice tersebut tidak dianggap telah selesai sepenuhnya. Invoice ditandai sebagai "dibayar sebagian" Jika pedagang ingin menerima faktur yang kurang dibayar, Anda dapat mengatur tingkat persentase di sini


### Permintaan


Permintaan Pembayaran adalah fitur yang memungkinkan pemilik toko BTCPay untuk membuat faktur jangka panjang. Dana dibayarkan sesuai dengan permintaan pembayaran menggunakan kurs Exchange yang berlaku pada saat pembayaran. Hal ini memungkinkan pengguna untuk melakukan pembayaran sesuai keinginan mereka tanpa perlu menegosiasikan atau memverifikasi kurs Exchange dengan pemilik toko pada saat pembayaran.


Pengguna dapat membayar permintaan dengan pembayaran sebagian. Permintaan pembayaran akan tetap berlaku hingga dibayar lunas atau jika pemilik toko meminta waktu kedaluwarsa. Alamat tidak pernah digunakan kembali. Address baru dibuat setiap kali pengguna mengklik bayar untuk membuat Invoice untuk permintaan pembayaran.


Pemilik toko dapat mencetak permintaan pembayaran (atau mengekspor data Invoice) untuk pencatatan dan akuntansi. BTCPay secara otomatis melabeli faktur sebagai Permintaan Pembayaran dalam daftar Invoice toko Anda.


#### Sesuaikan Permintaan Pembayaran Anda



- Invoice Jumlah - Tetapkan Jumlah Pembayaran yang Diminta
- Denominasi - Tampilkan Jumlah yang Diminta dalam Fiat atau Mata Uang Kripto
- Jumlah Pembayaran - Hanya mengizinkan pembayaran tunggal atau pembayaran sebagian
- Waktu Kedaluwarsa - Izinkan pembayaran hingga tanggal atau tanpa kedaluwarsa
- Deskripsi - Editor Teks, Tabel Data, Menyematkan Foto & Video
- Penampilan - Warna dan Gaya dengan Tema CSS


![image](assets/en/094.webp)


#### Buat Permintaan Pembayaran


Di menu sebelah kiri, buka Permintaan Pembayaran dan klik "Buat Permintaan Pembayaran".


![image](assets/en/095.webp)


Berikan Nama Permintaan, Jumlah, Denominasi Tampilan, Toko Terkait, Waktu Kadaluarsa & Deskripsi (Opsional)


Pilih opsi Izinkan penerima pembayaran untuk membuat faktur dalam denominasi mereka jika Anda ingin mengizinkan pembayaran sebagian.


Klik Simpan & Lihat untuk meninjau permintaan pembayaran Anda.


BTCPay membuat URL untuk permintaan pembayaran. Bagikan URL ini untuk melihat permintaan pembayaran Anda. Perlu beberapa permintaan yang sama? Anda bisa menduplikasi permintaan pembayaran menggunakan opsi Klon di menu utama.


![image](assets/en/096.webp)


** PERINGATAN**


Permintaan pembayaran bergantung pada toko, yang berarti setiap permintaan pembayaran dikaitkan dengan toko selama pembuatan. Pastikan Wallet terhubung ke toko Anda yang menjadi tempat permintaan pembayaran.


#### Permintaan Berbayar


Penerima pembayaran dan pemohon dapat melihat status permintaan pembayaran setelah pembayaran dikirim. Status akan muncul sebagai Lunas jika pembayaran telah diterima secara penuh. Jika hanya sebagian pembayaran yang telah dilakukan, Jumlah Terhutang akan menampilkan saldo yang tersisa.


![image](assets/en/097.webp)


#### Menyesuaikan Permintaan Pembayaran


Konten deskripsi dapat diedit menggunakan editor teks permintaan pembayaran. Kedua opsi tersebut tersedia jika Anda ingin menggunakan tema warna tambahan atau gaya CSS khusus.


Pengguna non-teknis dapat menggunakan [tema bootstrap](https://docs.btcpayserver.org/Development/Theme/#2-bootstrap-themes). Kustomisasi lebih lanjut dapat dilakukan dengan memberikan kode CSS tambahan, seperti yang ditunjukkan di bawah ini.


```css
:root {
--btcpay-font-family-base: "Source Sans Pro", -apple-system,
BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
--btcpay-primary: #7d4698;
--btcpay-primary-accent: #59316b;
--btcpay-body-text: #333a41;
--btcpay-body-bg: #fff;
--btcpay-bg-tile: #f8f9fa;
}

#mainNav {
color: white;
background: linear-gradient(#59316b, #331840);
}

#mainNav .btn-link {
color: white;
}
```


### Tarik pembayaran


Secara tradisional, penerima membagikan Bitcoin Address mereka untuk melakukan pembayaran Bitcoin, dan pengirim kemudian mengirim uang ke Address ini. Sistem seperti ini disebut pembayaran Push, karena pengirim memulai pembayaran saat penerima mungkin tidak tersedia, dan mendorong pembayaran ke penerima.


Namun demikian, bagaimana dengan membalikkan peran tersebut?


Bagaimana jika, alih-alih pengirim mendorong pembayaran, pengirim mengizinkan penerima untuk menarik pembayaran pada waktu yang diinginkan oleh penerima? Ini adalah konsep pembayaran Tarik. Hal ini memungkinkan beberapa aplikasi baru, seperti:



- Layanan berlangganan (di mana pelanggan mengizinkan layanan untuk menarik uang setiap jumlah waktu tertentu)
- Pengembalian dana (di mana pedagang mengizinkan pelanggan untuk menarik uang pengembalian dana ke Wallet mereka saat mereka menginginkannya)
- Penagihan berbasis waktu untuk pekerja lepas (di mana orang yang mempekerjakan mengizinkan pekerja lepas untuk menarik uang ke dalam Wallet mereka saat waktu dilaporkan)
- Patronase (di mana pelindung mengizinkan penerima untuk menarik uang setiap bulan untuk terus mendukung pekerjaan mereka)
- Penjualan otomatis (di mana pelanggan Exchange mengizinkan Exchange untuk menarik uang dari Wallet mereka untuk dijual setiap bulan secara otomatis)
- Sistem penarikan saldo (di mana layanan bervolume tinggi memungkinkan pengguna untuk meminta penarikan dari saldo mereka, layanan ini kemudian dapat dengan mudah mengumpulkan semua pembayaran ke banyak pengguna dengan interval yang tetap)


### Pembayaran


Fungsionalitas pembayaran terkait dengan fitur [Tarik Pembayaran](https://docs.btcpayserver.org/PullPayments/). Fitur ini memungkinkan Anda membuat pembayaran dalam BTCPay Anda. Fitur ini memungkinkan Anda untuk memproses pembayaran tarik (pengembalian dana, pembayaran gaji, atau penarikan).


#### Contoh 1: Pengembalian dana


Mari kita mulai dengan contoh pengembalian dana. Pelanggan telah membeli barang di toko Anda, tetapi sayangnya, mereka harus mengembalikannya. Mereka menginginkan pengembalian dana. Di dalam BTCPay, Anda dapat membuat [Pengembalian Dana](https://docs.btcpayserver.org/Refund/) dan memberikan tautan kepada pelanggan untuk mengklaim dana mereka. Setelah pelanggan memberikan Address mereka dan mengklaim dana, maka akan ditampilkan di bagian Pembayaran.


Status pertama yang dimilikinya adalah Menunggu Persetujuan. Pegawai toko dapat memeriksa apakah ada beberapa yang menunggu, dan setelah membuat pilihan, Anda dapat menggunakan tombol Tindakan.


Opsi pada tombol tindakan



- Menyetujui pembayaran yang dipilih
- Menyetujui & mengirim pembayaran yang dipilih
- Membatalkan pembayaran yang dipilih


Langkah selanjutnya adalah menyetujui & mengirim pembayaran yang dipilih, karena kami ingin mengembalikan dana pelanggan. Periksa Address Pelanggan, yang menunjukkan jumlah dan apakah kita ingin biaya dikurangi dari pengembalian dana atau tidak. Setelah Anda menyelesaikan pengecekan, menandatangani transaksi adalah satu-satunya langkah yang tersisa.


Nasabah sekarang mendapatkan informasi terbaru di halaman Klaim. Dia dapat mengikuti transaksi karena dia diberikan tautan ke Block explorer dan transaksinya. Setelah transaksi dikonfirmasi, statusnya akan berubah menjadi 'Selesai'.


#### Contoh 2: Gaji


Sekarang mari kita bahas pembayaran gaji, karena ini digerakkan dari dalam toko dan bukan berdasarkan permintaan pelanggan. Konsep yang mendasarinya sama, yaitu menggunakan pembayaran tarikan. Tetapi alih-alih membuat pengembalian dana, kita akan membuat [Pull Payment](https://docs.btcpayserver.org/PullPayments/).


Buka tab Pembayaran Tarik di server BTCPay Anda. Di bagian kanan atas, klik Tombol Buat Pembayaran Tarik.


Sekarang kita berada dalam pembuatan Pembayaran, berikan nama dan jumlah yang diinginkan dalam mata uang yang dipilih. Isi Deskripsi, sehingga karyawan tahu tentang apa itu. Bagian selanjutnya mirip dengan pengembalian dana. Karyawan mengisi Tujuan Address dan jumlah yang ingin dia klaim dari Pembayaran ini. Dia mungkin memutuskan untuk melakukan 2 klaim terpisah, ke alamat yang berbeda, atau bahkan mengklaim sebagian secara kilat.


Jika ada beberapa Pembayaran yang menunggu, Anda dapat mengumpulkannya untuk ditandatangani dan dikirim. Setelah ditandatangani, pembayaran akan dipindahkan ke tab Sedang Berlangsung dan menampilkan Transaksi. Ketika diterima oleh jaringan, pembayaran akan berpindah ke tab Selesai. Tab yang sudah selesai hanya untuk tujuan historis. Tab ini menyimpan Pembayaran yang telah diproses dan transaksi yang termasuk di dalamnya


### Tarik pembayaran


#### Konsep


Ketika pengirim mengonfigurasi pembayaran Pull, mereka dapat mengonfigurasi sejumlah properti:



- Nama permintaan tarik Nama
- Jumlah batas
- Unit (seperti BTC, SAT, USD)
- Metode Pembayaran
  - BTC On-Chain
  - BTC off-chain
- Deskripsi
- CSS khusus
- Tanggal akhir (opsional untuk Lightning Network BOLT11)


Setelah itu, pengirim dapat membagikan pembayaran tarikan menggunakan tautan kepada penerima, sehingga penerima dapat melakukan pembayaran. Penerima akan memilih pembayaran mereka:



- Metode pembayaran mana yang harus digunakan
- Ke mana harus mengirim uang


Setelah pembayaran dibuat, pembayaran tersebut akan dihitung terhadap batas pembayaran tarik untuk periode saat ini. Pengirim kemudian akan menyetujui pembayaran dengan menetapkan tarif pembayaran yang akan dikirim dan melanjutkan pembayaran.


Untuk pengirim, kami menyediakan metode yang mudah digunakan untuk menggabungkan beberapa pembayaran dari [BTCPay Internal Wallet](https://docs.btcpayserver.org/Wallet/).


#### API Greenfield


BTCPay Server menyediakan API lengkap untuk pengirim dan penerima yang didokumentasikan di halaman `/docs` pada instance Anda. (atau di situs web dokumentasi https://docs.btcpayserver.org)


Karena API kami mengekspos kemampuan penuh pembayaran tarik, pengirim dapat mengotomatiskan pembayaran untuk kebutuhan mereka sendiri.


### Ringkasan Keterampilan


Dalam bagian ini, Anda telah mempelajari yang berikut ini:



- Pemahaman mendalam tentang status Invoice BTCPay Server, serta tindakan yang dapat dilakukan terhadap status tersebut
- Menyesuaikan dan mengelola mekanisme Invoice yang tahan lama yang dikenal sebagai Permintaan.
- Kemungkinan pembayaran fleksibel tambahan terbuka dengan fitur unik Pull Payment dari BTCPay Server, terutama dalam menangani pengembalian dana dan pembayaran gaji.


### Penilaian pengetahuan


#### Tinjauan Konseptual KA


Apa saja perbedaan antara faktur dan permintaan pembayaran, dan apa alasan yang tepat untuk menggunakan faktur?


#### Tinjauan Konseptual KA


Bagaimana pembayaran tarik memperluas apa yang biasanya dapat dilakukan On-Chain? Jelaskan beberapa kasus penggunaan yang dapat dilakukan.


## Plugin Default Server BTCPay


<chapterId>7d673dc4-bd5d-5411-819b-f135f1d86636</chapterId>


### Plugin dan Aplikasi Default


Server BTCPay hadir dengan seperangkat Plugin (Aplikasi) standar yang dapat mengubah Server BTCPay menjadi gateway pembayaran e-commerce. Dengan tambahan Point Of sale, platform Crowdfund, dan tombol Bayar yang mudah, BTCPay Server menjadi solusi yang mudah digunakan.


### Tempat Penjualan


Salah satu Plugin standar BTCPay Server adalah Point of Sale (PoS). Dengan plugin PoS, pemilik toko dapat membuat Webshop langsung dari BTCPay Server; pemilik toko tidak memerlukan solusi e-commerce pihak ketiga untuk menjalankan Webshop. Aplikasi PoS berbasis web memungkinkan pengguna dengan toko fisik untuk dengan mudah menerima Bitcoin, tanpa biaya atau pihak ketiga, langsung ke Wallet mereka. PoS dapat dengan mudah ditampilkan di tablet atau perangkat lain yang mendukung penjelajahan web. Pengguna dapat dengan mudah membuat pintasan layar beranda untuk mengakses aplikasi web dengan cepat.


#### Cara membuat Point of Sale baru


BTCPay Server memungkinkan pemilik toko untuk dengan cepat membuat Point of Sale dalam berbagai tata letak. BTCPay Server menyadari bahwa tidak semua toko adalah e-commerce, dan tidak semua toko adalah bar atau restoran, dan dilengkapi dengan beberapa pengaturan standar untuk PoS Anda.


Ketika pemilik Toko mengklik "Point of Sale" di bilah menu sebelah kiri, BTCPay Server akan meminta nama; nama ini akan terlihat di bilah menu sebelah kiri. Klik Buat untuk membuat PoS.


![image](assets/en/098.webp)


#### Memperbarui Point of Sale yang baru dibuat


Setelah membuat PoS baru, layar berikut ini akan memungkinkan Anda untuk memperbarui Point of Sale dan menambahkan item untuk toko Anda.


##### Nama aplikasi


Nama yang diberikan di sini untuk Point of Sale Anda akan terlihat di menu utama Server BTCPay.


##### Judul Tampilan


Publik akan melihat judul atau nama toko Anda saat berkunjung. Server BTCPay, secara default, menamai toko Anda dengan nama "Kedai Teh" Ganti dengan nama toko Anda.


![image](assets/en/099.webp)


#### Pilih Gaya Kasir


Server BTCPay mampu menampilkan Point Of Sale dalam berbagai cara.



- Daftar produk
  - Tampilan toko di mana pelanggan hanya dapat membeli 1 produk dalam satu waktu.
- Daftar produk dengan troli.
  - Tampilan toko di mana pelanggan dapat membeli beberapa item sekaligus dan mendapatkan gambaran umum keranjang belanja di sebelah kanan layar mereka.
- Hanya keypad
  - Tidak ada daftar produk, hanya keypad untuk faktur langsung.
- Tampilan cetak (Daftar produk yang dapat dicetak dengan QR)
  - Jika Anda tidak dapat selalu menampilkan daftar produk Anda secara digital, Anda memerlukan solusi "offline" untuk produk; BTCPay Server memiliki tampilan cetak untuk berfungsi sebagai toko Offline.


![image](assets/en/100.webp)


#### Gaya Tempat Penjualan - Daftar produk


![image](assets/en/101.webp)


#### Gaya Tempat Penjualan - Daftar Produk + Keranjang


![image](assets/en/102.webp)


#### Gaya Titik Penjualan - Hanya keypad


![image](assets/en/103.webp)


#### Gaya Titik Penjualan - Tampilan cetak


![image](assets/en/104.webp)


#### Mata uang


Pemilik toko dapat menetapkan mata uang yang berbeda untuk Point of Sale mereka dari mata uang default yang telah ditetapkan secara keseluruhan. Mata uang default toko akan secara otomatis mengisi bidang ini.


#### Deskripsi


Ceritakan kepada dunia tentang toko Anda; apa yang Anda jual, dan berapa harganya? Semua yang menjelaskan tentang toko Anda ada di sini.


![image](assets/en/105.webp)


#### Produk


Ketika Point of Sale dibuat, Server BTCPay standar akan menambahkan beberapa item ke toko sebagai referensi. Klik tombol Edit pada salah satu item standar untuk memahami setiap opsi yang memungkinkan untuk sebuah item dengan lebih baik.


Membuat produk baru di toko Anda terdiri dari bidang-bidang berikut;



- Judul
- Harga (tetap, minimum, atau khusus)
- URL gambar
- Deskripsi
- Persediaan
- ID
- Teks Tombol Beli.
- Mengaktifkan/menonaktifkan


Setelah pemilik toko mengisi semua kolom produk baru, klik simpan, dan Anda akan melihat bahwa bagian Produk di Point of Sale sekarang sudah terisi. Selalu simpan di sudut kanan atas layar Anda untuk mencegah kemungkinan pemilik toko kehilangan progres saat menambahkan produk.


Pemilik toko juga dapat menggunakan "Raw Editor" untuk mengonfigurasi produk mereka. Editor mentah memerlukan pemahaman dasar tentang struktur JSON.


![image](assets/en/106.webp)


#### Pembayaran


Server BTCPay memungkinkan kustomisasi pembayaran khusus PoS yang kecil. Pemilik toko dapat mengatur teks "Beli untuk x" atau meminta data pelanggan tertentu dengan menambahkannya ke formulir.


#### Tips


Hanya beberapa toko yang membutuhkan opsi untuk Tips pada penjualan mereka. Pemilik toko dapat mengaktifkan atau menonaktifkannya sesuai kebutuhan toko mereka. Jika toko menggunakan tips yang diaktifkan, pemilik toko dapat mengatur teks di bidang untuk tips yang mereka sukai. Tips BTCPay Server bekerja berdasarkan jumlah persentase. Pemilik toko dapat menambahkan beberapa persentase, dipisahkan dengan koma.


#### Diskon


Sebagai pemilik toko, Anda mungkin ingin memberikan diskon khusus kepada pelanggan pada saat pembayaran; tombol untuk Diskon tersedia di kasir toko Anda. Namun, hal ini sangat tidak disarankan untuk menggunakan sistem checkout mandiri.


#### Pembayaran Khusus


Ketika opsi Pembayaran Khusus diaktifkan, pelanggan dapat memasukkan harga yang ditetapkan sama dengan atau di atas Invoice asli yang dihasilkan oleh toko.


#### Opsi Tambahan


Setelah mengatur semuanya untuk Point of Sale Anda, beberapa opsi tambahan masih tersisa. Pemilik toko dapat dengan mudah menyematkan PoS mereka melalui Iframe atau menyematkan tombol pembayaran yang terhubung ke item toko tertentu. Untuk menata toko PoS yang baru saja dibuat, pemilik dapat menambahkan CSS khusus di bagian bawah opsi tambahan.


#### Menghapus aplikasi ini


Jika pemilik toko ingin menghapus Point of Sale sepenuhnya dari BTCPay Server mereka, di bagian bawah pembaruan PoS, pemilik toko dapat mengklik tombol Hapus aplikasi ini untuk sepenuhnya menghancurkan aplikasi PoS mereka. Ketika mengklik "Hapus aplikasi ini", BTCPay Server akan meminta konfirmasi dengan mengetik `DELETE` dan mengonfirmasi dengan mengklik tombol Delete. Setelah menghapus, pemilik toko akan kembali ke dasbor BTCPay Server.


### Server BTCPay - Crowdfunding


Di samping plugin Point of Sale, BTCPay Server memiliki opsi untuk membuat crowdfund. Sama seperti platform Crowdfund lainnya, pemilik toko dapat menetapkan tujuan, membuat fasilitas untuk kontribusi, dan menyesuaikannya dengan kebutuhan mereka.


#### Cara menyiapkan crowdfunding baru


Klik plugin Crowdfund melalui menu utama di sebelah kiri BTCPay Server Anda, di bawah bagian Plugin. BTCPay Server sekarang akan meminta nama untuk Crowdfund; nama ini juga akan ditampilkan di bilah menu sebelah kiri.


![image](assets/en/107.webp)


#### Memperbarui Point of Sale yang baru dibuat


Setelah Aplikasi diberi nama, layar berikutnya adalah memperbarui Aplikasi agar memiliki konteks.


#### Nama Aplikasi


Nama yang diberikan pada Crowdfund Anda akan terlihat di menu utama BTCPay Server.


#### Judul Tampilan


Judul tersebut diberikan kepada Crowdfund untuk publik.


#### Tagline


Berikan satu kalimat singkat untuk mengenali tentang apa penggalangan dana tersebut.


![image](assets/en/108.webp)


#### URL Gambar Unggulan


Setiap crowdfund memiliki gambar utama, yaitu satu banner yang Anda kenali secara langsung. Gambar ini dapat disimpan di server Anda jika Anda memiliki hak Administratif. Admin dapat mengunggah di bawah pengaturan Server BTCPay - File. Jika Anda adalah pemilik Toko, gambar harus diunggah ke web melalui host pihak ketiga (misalnya, Imgur).


#### Jadikan Crowdfund Publik


Pengalihan ini membuat Crowdfund Anda menjadi publik dan dengan demikian dapat dilihat oleh dunia luar. Untuk tujuan pengujian atau untuk melihat apakah tema Anda diterapkan dengan benar, tetap setel ke OFF selama periode pembuatan crowdfund.


#### Deskripsi


Ceritakan kepada dunia tentang Crowdfund Anda. Untuk apa Anda menggalang dana? Segala sesuatu yang menjelaskan crowdfund Anda ada di sini.


![image](assets/en/109.webp)


#### Tujuan Crowdfunding


Tetapkan target tujuan untuk apa yang harus diperoleh penggalangan dana untuk proyek dan mata uang apa yang harus digunakan untuk tujuan tersebut. Pastikan bahwa jika tujuan Anda ditetapkan di antara tanggal, sertakan tanggal target dan akhir ini di bawah Sasaran di crowdfund.


![image](assets/en/110.webp)


#### Fasilitas


Fasilitas dapat secara signifikan meningkatkan upaya urun dana Anda. Ini karena tunjangan memberi orang cara untuk berpartisipasi dalam kampanye Anda. Mereka memanfaatkan motivasi egois dan kebajikan. Dan mereka memungkinkan Anda mengakses pengeluaran pendukung Anda, bukan hanya dompet filantropi mereka - Anda dapat menebak mana yang lebih signifikan.


Membuat perk baru terdiri dari bidang-bidang berikut.



- Judul
- Harga (tetap, minimum, atau khusus)
- URL gambar
- Deskripsi
- Persediaan
- ID
- Teks Tombol Beli.
- Mengaktifkan/menonaktifkan


Setelah pemilik toko mengisi semua bidang dari fasilitas baru, klik simpan, dan Anda akan melihat bahwa bagian Fasilitas di Crowdfunds sekarang sudah terisi.


![image](assets/en/111.webp)


### Server BTCPay - Tempat Penjualan


#### Kontribusi


Pemilik toko dapat memilih cara menampilkan Perks, cara mengurutkannya, atau bahkan mengurutkannya dengan Perks lainnya. Namun, setelah target Crowdfunds tercapai, pemilik toko mungkin ingin menghentikan donasi yang mengalir ke penggalangan dana ini. Oleh karena itu, ia dapat mengaktifkan "Jangan izinkan kontribusi tambahan setelah mencapai target". Ini akan mencegah Crowdfund menerima donasi.


##### Perilaku urun dana


Standar Crowdfund hanya menghitung faktur yang dibuat dengan Crowdfund untuk mencapai tujuan. Namun, mungkin ada kasus di mana pemilik toko ingin semua faktur yang dibuat di toko ini dihitung dalam crowdfund.


#### Opsi Tambahan untuk penyesuaian


BTCpay Server menawarkan beberapa penyesuaian ekstra. Tambahkan suara, animasi, atau bahkan utas diskusi ke Crowdfund. Pemilik toko juga dapat memodifikasi tampilan dan nuansa Crowdfund dengan memasukkan CSS khusus mereka sendiri.


#### Menghapus aplikasi ini


Jika pemilik toko ingin sepenuhnya menghapus Crowdfund dari BTCPay Server mereka, di bagian bawah pembaruan Crowdfund, mereka dapat mengklik tombol "Hapus aplikasi ini" untuk sepenuhnya menghapus aplikasi Crowdfund mereka. Ketika mengklik "Hapus aplikasi ini", BTCPay Server akan meminta konfirmasi dengan mengetik `DELETE` dan mengonfirmasi dengan mengklik tombol Hapus. Setelah menghapus, pemilik toko akan kembali ke dasbor BTCPay Server.


### Server BTCPay - Tombol Bayar


HTML yang mudah disematkan dan tombol pembayaran yang sangat dapat disesuaikan memungkinkan pemilik toko untuk menerima tip dan donasi. Di bilah menu sebelah kiri BTCPay Server, di bawah bagian Plugin, pemilik toko dapat mengklik "Tombol Bayar" dan klik Aktifkan untuk membuat tombol Pembayaran.


#### Pengaturan Umum


Di dalam Pengaturan Umum untuk Tombol Pembayaran, pemilik toko dapat mengatur



- Harga standar
- Mata Uang Default
- Metode Pembayaran Default
  - Gunakan default toko
  - BTC On-Chain
  - BTC off-chain (Petir)
  - BTC off-chain (LNURL-pay)
- Deskripsi pembayaran
- ID Pesanan


#### Opsi tampilan


Tombol Bayar BTCPay Server dapat dikonfigurasi agar sesuai dengan gaya yang berbeda. Tombol dapat memiliki jumlah tetap atau jumlah khusus, yang ditampilkan dengan penggeser atau tombol plus dan minus.


#### Gunakan Modal


Saat membuat tombol pembayaran, pemilik toko dapat memilih perilakunya saat pelanggan mengkliknya dan menampilkannya dalam modal atau sebagai halaman baru.


**!* Catatan!**


Peringatan: Tombol Pembayaran hanya boleh digunakan untuk tip dan donasi


Menggunakan tombol pembayaran untuk integrasi e-commerce tidak disarankan karena pengguna dapat mengubah informasi terkait pesanan. Untuk e-commerce, Anda harus menggunakan API Greenfield kami. Jika toko ini memproses transaksi komersial, kami sarankan untuk membuat toko terpisah sebelum menggunakan tombol pembayaran.


#### Sesuaikan Teks tombol Bayar


Secara default, tombol pembayaran BTCPay Server menyatakan "Bayar Dengan BTCPay". Pemilik toko dapat mengatur teks ini sesuai keinginan mereka dan mengubah logo BTCPay Server menjadi logo mereka sendiri. Atur teks dengan menggunakan "Teks Tombol Pembayaran" dan tempelkan URL gambar di bawah "URL Gambar Tombol Pembayaran".


##### Ukuran gambar


Ukuran gambar pada tombol hanya dapat ditetapkan ke tiga default.



- 146x40px
- 168x46px
- 209x57px


#### Jenis Tombol


Server BTCPay mengetahui tiga status untuk Tombol Pembayaran.



- Jumlah Tetap
  - Harga yang ditetapkan sebelumnya ada dalam pengaturan umum tombol.
- Jumlah Khusus
  - Tombol Bayar BTCPay Server memiliki tombol + dan - untuk menetapkan harga khusus.
  - Saat menggunakan jumlah khusus, Server BTCPay akan meminta jumlah minimum, maksimum, dan seberapa besar kenaikannya.
  - Tombol dapat ditetapkan ke "Gunakan gaya input sederhana", yang akan menghilangkan tombol +/-.
  - Sesuaikan tombol sebaris di mana tombol dan sakelar muncul sebaris.
- Penggeser
  - Mirip dengan jumlah khusus, namun, secara visual berbeda, karena memiliki penggeser alih-alih tombol +/-.
  - Saat menggunakan Slider, Server BTCPay akan meminta Min, Max, dan seberapa besar peningkatannya.


**!* Catatan!**


Tombol Pembayaran dapat dihapus di bagian atas deskripsi peringatan.


#### Pemberitahuan Pembayaran


Server IPN (Pemberitahuan Pembayaran Instan) dirancang untuk webhook dan dapat dikonfigurasikan dengan URL untuk data pasca pembelian.


#### Pemberitahuan Email


Setiap kali pembayaran telah dilakukan, BTCPay Server dapat memberi tahu pemilik toko.


#### Pengalihan browser


Ketika pelanggan menyelesaikan pembelian, ia akan diarahkan ke tautan ini jika ditetapkan oleh pemilik toko.


#### Opsi Tombol Pembayaran Lanjutan


Tentukan parameter string kueri tambahan yang harus ditambahkan ke halaman checkout setelah Invoice dibuat. Sebagai contoh, `lang=da-DK` akan memuat halaman checkout dalam bahasa Denmark secara default.


#### Gunakan Aplikasi sebagai Titik Akhir


Anda dapat langsung menautkan tombol pembayaran ke item di salah satu aplikasi PoS atau Crowdfund yang telah Anda gunakan sebelumnya.


Pemilik toko dapat mengklik menu tarik-turun dan memilih Aplikasi yang diinginkan; setelah Aplikasi dipilih, pemilik toko dapat menambahkan item yang perlu ditautkan.


#### Kode yang dihasilkan


Karena tombol Pembayaran BTCPay Server adalah HTML yang mudah disematkan, BTCPay Server menampilkan kode yang dihasilkan untuk disalin ke situs web di bagian bawah setelah mengonfigurasi tombol Pembayaran.


Pemilik toko dapat menyalin kode yang dihasilkan ke situs web mereka, dan tombol Pembayaran dari BTCPay Server langsung aktif di situs web mereka.


#### Pemberitahuan Pembayaran


Server IPN (Pemberitahuan Pembayaran Instan) dirancang untuk webhook dan dapat dikonfigurasikan dengan URL untuk mengirim data pembelian.


#### Pemberitahuan Email


Setiap kali pembayaran dilakukan, BTCPay Server dapat memberi tahu pemilik toko.


#### Pengalihan browser


Ketika pelanggan menyelesaikan pembelian, ia akan diarahkan ke tautan ini jika ditetapkan oleh pemilik toko.


#### Opsi Tombol Pembayaran Lanjutan


Tentukan parameter string kueri tambahan yang harus ditambahkan ke halaman checkout setelah Invoice dibuat. Sebagai contoh, `lang=da-DK` akan memuat halaman checkout dalam bahasa Denmark secara default.


#### Gunakan Aplikasi sebagai Titik Akhir


Anda bisa langsung menautkan tombol pembayaran ke item di salah satu aplikasi PoS atau Crowdfund yang sudah Anda gunakan sebelumnya. Pemilik toko dapat mengklik menu tarik-turun dan memilih aplikasi yang diinginkan. Setelah aplikasi dipilih, pemilik toko dapat menambahkan item yang perlu ditautkan.


#### Kode yang dihasilkan


Karena tombol Pembayaran BTCPay Server adalah HTML yang mudah disematkan, BTCPay Server menampilkan kode yang dihasilkan untuk disalin ke situs web di bagian bawah setelah mengonfigurasi tombol Pembayaran. Pemilik toko dapat menyalin kode yang dihasilkan ke dalam situs web mereka, dan tombol Pembayaran dari BTCPay Server langsung aktif di situs web mereka.


### Ringkasan Keterampilan


Di bagian ini, Anda sudah belajar:



- Cara menggunakan plugin PoS terintegrasi BTCPay Server untuk membuat toko kustom dengan mudah
- Cara menggunakan plugin Crowdfund terintegrasi BTCPay Server untuk membuat aplikasi crowdfund kustom dengan mudah
- Menghasilkan kode untuk tombol bayar kustom menggunakan plugin Tombol Bayar


### Penilaian pengetahuan


#### Ulasan KA


Apa saja tiga plugin bawaan yang menjadi standar pada BTCPay Server? Dalam beberapa kata, jelaskan bagaimana masing-masing plugin dapat digunakan.


# Mengkonfigurasi Server BTCPay


<partId>ff38596c-7de3-5e5c-ba50-9b9edbbbb5eb</partId>


## Pemahaman dasar tentang menginstal BTCPay Server di lingkungan LunaNode


<chapterId>d0a28514-ffcf-529b-9156-29141f0b060a</chapterId>


### Menginstal Server BTCPay di Hosted Env (LunaNode)


Langkah-langkah ini akan memberikan semua informasi yang diperlukan untuk mulai menggunakan BTCPay Server di LunaNode. Ada banyak opsi untuk menerapkan perangkat lunak.

Anda dapat menemukan semua detail BTCPay Server di https://docs.btcpayserver.org.


#### Dari mana kita mulai?


Pada bagian ini, Anda akan membiasakan diri dengan LunaNode sebagai penyedia hosting, mempelajari langkah-langkah pertama dalam menggunakan Server BTCPay Anda, dan mempelajari cara menggunakan Lightning Network. Setelah kita melewati semua langkah, Anda dapat menjalankan toko web atau platform crowdfunding yang menerima Bitcoin!


Ini adalah salah satu dari banyak cara untuk menggunakan BTCPay Server. Baca dokumentasi kami untuk informasi lebih lanjut.


https://docs.btcpayserver.org.


### Server BTCPay - Penyebaran LunaNode


#### Penyebaran LunaNode


Pertama, buka situs web LunaNode.com, di mana kita akan membuat akun baru. Klik pada Sign Up di kanan atas atau gunakan wizard Get Started di beranda mereka.


![image](assets/en/112.webp)


Setelah Anda membuat akun baru Anda, LunaNode akan mengirimkan email verifikasi. Setelah Anda memverifikasi akun, dibandingkan dengan Voltage, Anda akan segera dihadapkan pada opsi untuk menambah saldo akun Anda. Saldo ini diperlukan untuk menutupi ruang peladen dan biaya hosting.


![image](assets/en/113.webp)


#### Menambahkan kredit ke akun LunaNode Anda


Setelah Anda mengklik "Deposit kredit", Anda bisa mengatur berapa banyak Anda ingin mengisi ulang akun Anda dan bagaimana Anda ingin membayarnya. LunaNode dan BTCPay Server akan dikenakan biaya antara $ 10 dan $ 20 per bulan.

Dibandingkan dengan Voltage.cloud, Anda mendapatkan akses penuh ke Virtual Private Server (VPS) Anda, memungkinkan Anda untuk memiliki kontrol lebih besar pada peladen Anda. Setelah Anda membuat akun baru, LunaNode akan mengirimkan email verifikasi.

Setelah Anda memverifikasi akun, dibandingkan dengan Voltage, Anda akan segera dihadapkan pada opsi untuk menambah saldo akun Anda. Saldo ini diperlukan untuk membayar ruang peladen dan biaya hosting.


#### Bagaimana cara menggunakan server baru?


Dalam panduan ini, kami akan memandu Anda melalui proses penyiapan dengan membuat satu set kunci API dan menggunakan peluncur BTCPay Server yang dikembangkan oleh LunaNode.


Di dasbor LunaNode Anda, klik API di bagian kanan atas. Ini akan membuka halaman baru. Kita hanya perlu mengatur Nama untuk kunci API. Sisanya akan diurus oleh LunaNode dan tidak akan dibahas dalam panduan ini. Klik tombol Create API Credential.

Setelah membuat kredensial API, Anda akan mendapatkan serangkaian huruf dan karakter yang panjang. Ini adalah kunci API Anda.


![image](assets/en/114.webp)


#### Bagaimana cara menggunakan server baru?


Ada dua bagian dari kredensial ini, kunci API dan ID API; kita akan membutuhkan keduanya. Sebelum kita melanjutkan ke langkah berikutnya, mari kita buka tab kedua di browser dan buka https://launchbtcpay.lunanode.com/


Di sini Anda akan diminta untuk memberikan kunci API dan ID API Anda. Ini untuk memberi tahu Anda bahwa Andalah yang menyediakan server baru ini. Kunci API seharusnya masih terbuka pada tab sebelumnya; jika Anda menggulir ke bawah pada tabel di bawah ini, Anda akan menemukan ID API.


Anda bisa kembali ke halaman dengan Launcher, mengisi kolom dengan kunci API dan ID Anda, dan klik lanjutkan.


![image](assets/en/115.webp)


Pada langkah berikutnya, Anda dapat memberikan nama domain. Jika Anda sudah memiliki domain dan ingin menggunakannya untuk BTCPay Server, pastikan Anda juga menambahkan record DNS (disebut record `A`) pada domain Anda. Jika Anda tidak memiliki domain, gunakan domain yang disediakan LunaNode sebagai gantinya (Anda dapat mengubahnya nanti di pengaturan BTCPay Server) dan klik Lanjutkan.


Baca lebih lanjut tentang cara mengatur atau mengubah catatan DNS untuk Server BTCPay; https://docs.btcpayserver.org/FAQ/Deployment/#how-to-change-your-btcpay-server-domain-name


#### Luncurkan Server BTCPay di LunaNode


Setelah melakukan langkah-langkah sebelumnya, kita dapat mengatur semua opsi untuk server baru kita. Di sini, kita akan memilih Bitcoin (BTC) sebagai mata uang yang didukung. Kita juga dapat mengatur email untuk menerima pemberitahuan tentang sertifikat enkripsi untuk tujuan pembaruan, yang bersifat opsional.


Panduan ini bertujuan untuk menyiapkan lingkungan Mainnet (Bitcoin dunia nyata); namun, LunaNode juga memungkinkan Anda untuk mengaturnya ke Testnet atau Regtest untuk tujuan pengembangan. Kami akan membiarkannya pada opsi Mainnet untuk panduan ini.


Anda dapat memilih implementasi Lightning Anda. LunaNode menawarkan dua implementasi yang berbeda, LND dan Core Lightning. Untuk panduan ini, kami akan menggunakan LND. Ada beberapa perbedaan yang nyata dalam kedua implementasi; untuk lebih lanjut tentang hal ini, kami sarankan untuk membaca dokumentasi yang luas: https://docs.btcpayserver.org/LightningNetwork#getting-started-with-btcpay-server-and-core-lightning-cln


![image](assets/en/116.webp)


LunaNode menawarkan beberapa paket Virtual Machine (VM). Paket-paket ini berbeda dalam hal kisaran harga dan spesifikasi server. Untuk panduan ini, paket m2 sudah cukup; namun, jika Anda telah memilih lebih dari sekadar Bitcoin sebagai mata uang, pertimbangkan untuk menggunakan setidaknya m4.


Mempercepat sinkronisasi Blockchain awal; ini opsional dan tergantung pada kebutuhan Anda. Ada opsi lanjutan, seperti mengatur Lightning Alias, mengarahkan ke rilis GitHub tertentu, atau mengatur kunci SSH; tidak ada yang akan dibahas dalam panduan ini.


Setelah mengisi formulir, Anda harus mengklik Luncurkan VM, dan Lunanode akan mulai membuat VM baru Anda, termasuk BTCPay Server yang terinstal di dalamnya. Proses ini membutuhkan waktu beberapa menit; setelah server Anda siap, LunaNode akan memberikan tautan ke BTCPay Server baru Anda.


Setelah proses pembuatan, klik tautan ke Server BTCPay Anda; di sini, Anda akan diminta untuk membuat akun Administrator.


![image](assets/en/117.webp)


### Ringkasan Keterampilan


Di bagian ini, Anda sudah belajar:



- Membuat dan mendanai akun di LunaNode
- Menggunakan Peluncur Server BTCPay untuk membuat server Anda sendiri


### Penilaian pengetahuan


#### Tinjauan Konseptual KA


Jelaskan beberapa perbedaan antara menjalankan instance BTCPay Server di VPS vs. membuat akun di instance yang dihosting.


## Menginstal Server BTCPay di lingkungan Tegangan


<chapterId>11c7d284-b4d2-5542-872c-df9bd9c1491b</chapterId>


Anda akan mengenal Voltage.cloud sebagai penyedia hosting, mempelajari langkah-langkah pertama dalam menggunakan BTCPay Server, dan mempelajari cara menggunakan Lightning Network. Setelah kita melewati semua langkah, Anda dapat menjalankan webshop atau platform crowdfunding yang menerima Bitcoin!


Ini adalah salah satu dari banyak cara untuk menggunakan BTCPay Server. Baca dokumentasi kami untuk informasi lebih lanjut.

https://docs.btcpayserver.org.


### Server BTCPay - Penerapan Voltage.cloud


Pertama, buka situs web Voltage.cloud dan daftar untuk akun baru. Saat membuat akun, Anda bisa mendaftar untuk uji coba gratis 7 hari. Klik pada tombol Daftar di kanan atas atau gunakan "Coba uji coba gratis 7 hari" pada beranda mereka.


![image](assets/en/118.webp)


Setelah Anda membuat akun, klik tombol `NODES` pada dasbor Anda. Setelah kita memilih Nodes dan membuat node baru, kita akan dihadapkan pada penawaran Voltage yang memungkinkan dari node tersebut. Karena panduan ini juga akan membahas Lightning Network, di Voltage, pertama-tama kita harus memilih implementasi Lightning sebelum membuat Server BTCPay. Klik pada LightningNode.


![image](assets/en/119.webp)


Di sini, Anda harus memilih jenis Lightning node yang Anda inginkan. Voltage memiliki beragam opsi untuk pengaturan pencahayaan Anda. Hal ini berbeda ketika menggunakan, misalnya, LunaNode. Untuk tujuan panduan ini, Lite Node sudah cukup. Baca lebih lanjut tentang perbedaannya di Voltage.cloud.


![image](assets/en/120.webp)


Beri nama node Anda, tetapkan kata sandi, dan amankan kata sandi ini. Jika kata sandi ini hilang, Anda akan kehilangan akses ke cadangan Anda, dan Voltage tidak dapat memulihkannya. Buat node, dan Voltage akan menampilkan progresnya. Voltage telah membuat Lightning Node Anda. Kita sekarang dapat membuat instance BTCPay Server dan langsung mengakses Lightning Network.


Klik Nodes di kiri atas dasbor Anda. Di sini Anda bisa menyiapkan bagian selanjutnya dari instance Server BTCPay Anda. Klik "buat baru" setelah Anda berada di ikhtisar node. Anda akan melihat layar yang sama seperti sebelumnya. Sekarang, alih-alih Lightning Node, kita memilih BTCPay Server.


Voltage menunjukkan geolokasi Server BTCPay Anda, yang dihosting di wilayah AS Barat. Di sini Anda juga akan melihat biaya hosting server. Klik Buat dan beri nama Server BTCPay Anda. Aktifkan Lightning dan Voltage akan menampilkan simpul Lightning yang telah dibuat di langkah sebelumnya. Klik Create, dan Voltage akan membuat instance BTCPay Server.


![image](assets/en/121.webp)


Setelah Anda menekan create, Voltage akan menampilkan nama pengguna dan kata sandi default. Ini mirip dengan kata sandi yang Anda tetapkan sebelumnya di Voltage. Klik tombol Masuk ke Akun untuk mengarahkan Anda ke Server BTCPay.


Selamat datang di instance Server BTCPay baru Anda. Karena kami telah menyiapkan Lightning dalam proses pembuatan, ini menunjukkan bahwa Lightning sudah diaktifkan!


### Ringkasan Keterampilan


Dalam bab ini, Anda telah belajar:



- Membuat akun di Voltage.cloud
- Langkah-langkah untuk menjalankan Server BTCPay bersama dengan node Lightning di akun


### Penilaian pengetahuan


#### Tinjauan Konseptual KA


Apa saja perbedaan utama antara pengaturan Voltage dan LunaNode?


## Menginstal Server BTCPay pada node Umbrel


<chapterId>3298e292-6476-5fe0-836c-7fa021348799</chapterId>


Pada akhir langkah-langkah ini, Anda dapat menerima pembayaran kilat ke toko BTCPay di jaringan lokal Anda. Proses ini juga akan berlaku jika Anda menjalankan umbrel node di restoran atau bisnis. Jika Anda ingin menghubungkan toko ini ke situs web publik, ikuti latihan lanjutan untuk mengekspos umbrel node Anda ke publik.


https://umbrel.com/


![image](assets/en/122.webp)


### Server BTCPay - Penyebaran payung


Setelah node Umbrel Anda disinkronkan sepenuhnya dengan Bitcoin Blockchain, buka Umbrel App Store, dan cari BTCPay Server di bawah Aplikasi.


![image](assets/en/123.webp)


Klik BTCPay Server untuk melihat detail Aplikasi. Ketika detail untuk BTCPay Server terbuka, sudut kanan bawah menunjukkan persyaratan agar Aplikasi dapat berjalan dengan baik. Ini menunjukkan bahwa aplikasi ini membutuhkan Bitcoin dan Lightning node. Jika Anda belum menginstal Lightning Node pada Umbrel Anda, klik Instal. Proses ini dapat memakan waktu beberapa menit.


![image](assets/en/124.webp)


Setelah memasang lightning Node Anda:


1. Klik buka pada detail aplikasi atau pada Aplikasi di dasbor Umbrels.

2. Klik setup a new node; Anda akan diperlihatkan 24 kata untuk pemulihan lightning node Anda.

3. Catatlah ini.


![image](assets/en/125.webp)


Umbrel akan meminta verifikasi kata-kata yang baru saja dituliskan. Setelah node Lightning disiapkan, kembali ke App Store Umbrel dan temukan BTCPay Server. Klik pada tombol instal, dan Umbrel akan menunjukkan apakah komponen yang diperlukan sudah terinstal dan BTCPay Server memerlukan akses ke komponen ini. Setelah instalasi, klik Buka di kanan atas detail Aplikasi atau buka BTCPay Server melalui dasbor Umbrels Anda.


Umbrel akan meminta verifikasi kata-kata yang baru saja ditulis.


![image](assets/en/126.webp)


**!* Catatan!**


Pastikan Anda menyimpannya di lokasi yang aman, seperti yang telah dipelajari sebelumnya saat menyimpan kunci.


Setelah Lightning node disiapkan, kembali ke Umbrel App Store dan temukan BTCPay Server. Klik pada tombol instal, dan Umbrel akan menunjukkan apakah komponen yang diperlukan telah diinstal dan BTCPay Server memerlukan akses ke komponen-komponen ini.


![image](assets/en/127.webp)


Setelah instalasi, klik Buka di bagian kanan atas detail Aplikasi atau buka Server BTCPay melalui dasbor Umbrels Anda.


![image](assets/en/128.webp)


### Ringkasan Keterampilan


Di bagian ini, Anda sudah belajar:



- Langkah-langkah untuk menginstal BTCPay Server dengan fungsionalitas Lightning pada node Umbrel


### Penilaian pengetahuan


#### Tinjauan Konseptual KA


Apa perbedaan penyiapan pada Umbrel dengan dua opsi hosting sebelumnya?


# Bagian Akhir


<partId>d72e6fa5-0870-5f00-9143-9466ed22e2bd</partId>




## Ulasan & Peringkat

<chapterId>d90bb93d-b894-551e-9fd6-6855c739a904</chapterId>

<isCourseReview>true</isCourseReview>

## Kesimpulan Kursus


<chapterId>c07ac2a5-f97e-5c57-8a80-4955b48128d4</chapterId>

<isCourseConclusion>true</isCourseConclusion>