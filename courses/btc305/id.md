---
name: Bitcoin dan BTCPay Server
goal: Menginstal BTCPay Server untuk bisnis Anda
objectives:
  - Memahami apa itu btcpayserver.
  - Meng-host sendiri dan mengonfigurasi BTCPay Server.
  - Menggunakan btcpayserver dalam bisnis sehari-hari Anda.
---

# Bitcoin dan BTCPay Server

Ini adalah kursus pengenalan tentang Operator BTCPay Server yang ditulis oleh Alekos dan Bas, yang diadaptasi dalam Format Kursus Plan ₿ oleh melontwist dan asi0.

SEBUAH CERITA YANG BELUM SELESAI

"Ini Adalah Kebohongan, Kepercayaan Saya Padamu Telah Hancur, Aku Akan Membuatmu Usang".

Diproduksi oleh Yayasan BTCPay Server

+++

# Pengantar

<partId>59e43fe3-b494-5da6-b4b4-9df5bdf08916</partId>

## Pujian kritis untuk Bitcoin dan BTCPay Server oleh Penulis

<chapterId>e1fe6294-3c82-5203-9537-779f9087c35a</chapterId>

Mari kita mulai dengan apa itu BTCPay Server dan dari mana asalnya. Kami menghargai transparansi dan standar tertentu untuk membentuk kepercayaan di ruang Bitcoin.
Sebuah proyek di ruang ini melanggar nilai-nilai tersebut. Pengembang utama BTCPay Server, Nicolas Dorier, mengambil ini secara pribadi dan berjanji untuk membuat mereka usang. Berikut kami, bertahun-tahun kemudian, bekerja menuju masa depan ini, sepenuhnya open-source, setiap hari.

> Ini adalah kebohongan, kepercayaan saya padamu telah hancur, aku akan membuatmu usang.
> Nicolas Dorier

Setelah kata-kata yang diucapkan oleh Nicolas, saatnya untuk mulai membangun. Banyak pekerjaan yang masuk ke dalam apa yang sekarang kita sebut BTCPay Server. Lebih banyak orang ingin membantu dengan dorongan ini. Yang paling dikenal adalah r0ckstardev, MrKukks, Pavlenex, dan pedagang pertama yang menggunakan perangkat lunak tersebut, astupidmoose.

Apa itu open source, dan apa yang masuk ke dalam proyek seperti itu?

FOSS adalah singkatan dari Free & Open-Source Software. Yang pertama merujuk pada syarat yang memungkinkan siapa saja untuk menyalin, memodifikasi, dan bahkan mendistribusikan versi (bahkan untuk keuntungan) dari perangkat lunak tersebut. Yang terakhir merujuk pada berbagi kode sumber secara terbuka, mendorong publik untuk berkontribusi dan memperbaikinya.
Hal ini membawa pengguna berpengalaman yang antusias tentang berkontribusi pada perangkat lunak yang mereka gunakan dan mendapatkan nilai darinya, terbukti seiring waktu untuk menang dalam adopsi dibandingkan dengan perangkat lunak proprietary. Ini konsisten dengan etos Bitcoin bahwa "informasi ingin bebas". Ini membawa bersama orang-orang yang bersemangat yang membentuk komunitas dan lebih menyenangkan. Seperti Bitcoin, FOSS adalah tak terelakkan.

### Sebelum kita mulai

Kursus ini terdiri dari beberapa bagian. Banyak yang akan diurus oleh guru kelas Anda, lingkungan Demo yang Anda dapatkan akses ke, server yang di-host untuk diri Anda sendiri, dan mungkin nama domain. Jika Anda menyelesaikan kursus ini secara mandiri, harap sadar bahwa lingkungan yang diberi label sebagai DEMO tidak akan tersedia untuk Anda.
NB. Jika Anda mengikuti kursus ini melalui kelas, nama server mungkin berbeda tergantung pada pengaturan kelas Anda. Variabel dalam nama Server mungkin berbeda karena ini.

### Struktur Kursus

Setiap bab memiliki tujuan dan penilaian pengetahuan. Dalam kursus ini, kami akan membahas masing-masing dari ini dan memiliki ringkasan fitur kunci di setiap blok pelajaran (mis. bab). Ilustrasi ditampilkan untuk memberikan umpan balik visual dan memperkuat konsep kunci dalam aspek visual. Tujuan ditetapkan di awal setiap blok pelajaran. Tujuan ini melampaui daftar periksa. Ini memberi Anda panduan ke dalam keterampilan baru. Penilaian Pengetahuan secara progresif lebih menantang pengaturan BTCPay Server Anda.

### Apa yang diterima siswa dengan kursus?

Dengan Kursus BTCPay Server, seorang siswa dapat memahami prinsip dasar, baik teknis maupun non-teknis dari Bitcoin. Pelatihan ekstensif dalam menggunakan Bitcoin melalui BTCPay Server akan memungkinkan siswa untuk mengoperasikan infrastruktur Bitcoin mereka sendiri.

### Alamat Web Penting atau Kesempatan Kontak

Yayasan BTCPay Server, yang memungkinkan Alekos dan Bas untuk menulis kursus ini, berada di Tokyo, Jepang. Yayasan BTCPay Server dapat dihubungi melalui situs web yang tercantum;

- https://foundation.btcpayserver.org
- bergabung dengan saluran chat resmi: https://chat.btcpayserver.org

## Pengantar Bitcoin

<chapterId>5c0bc234-c188-5b4a-94d5-adee87a120e2</chapterId>

### Memahami Bitcoin melalui latihan kelas

Ini adalah latihan kelas jadi jika Anda mengikuti kursus ini sendiri, Anda tidak dapat melakukannya tetapi Anda masih dapat melalui latihan ini. Untuk menyelesaikan tugas ini, jumlah orang minimum adalah antara 9 dan 11.

Latihan dimulai setelah menonton pengantar “Bagaimana Bitcoin dan blockchain bekerja” oleh BBC.

![bagaimana bitcoin dan blockchain bekerja](https://youtu.be/mhE_vvwAiRc)

Latihan ini membutuhkan setidaknya sembilan orang untuk berpartisipasi. Latihan ini bertujuan untuk secara fisik mendapatkan ide tentang bagaimana Bitcoin bekerja. Dengan memainkan setiap peran dalam jaringan, Anda akan memiliki cara belajar yang interaktif dan menyenangkan. Latihan ini tidak melibatkan Lightning Network.

### Contoh; Membutuhkan 9 / 11 orang

Peran-perannya adalah:

- 1 Pelanggan
- 1 Pedagang
- 7 hingga 9 node Bitcoin

**Pengaturannya adalah sebagai berikut:**

Pelanggan membeli produk dari toko dengan Bitcoin.

**Skenario 1 - Sistem Perbankan Tradisional**

- Pengaturan:
  - Lihat diagram/penjelas di Figjam terlampir - [Skema Aktivitas](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Dapatkan tiga sukarelawan siswa untuk memainkan peran Pelanggan (Alice), Pedagang (Bob), dan Bank.
- Bertindak sesuai urutan kejadian:
  - Pelanggan- menjelajahi toko online dan menemukan barang seharga $25 yang mereka inginkan, dan memberitahu Pedagang bahwa mereka ingin membeli
  - Pedagang- meminta pembayaran.
  - Pelanggan- mengirimkan informasi kartu ke Pedagang
  - Pedagang- meneruskan informasi ke Bank (mengidentifikasi baik diri mereka sendiri maupun identitas/informasi) meminta pembayaran
  - Bank mengumpulkan informasi tentang Pelanggan dan Pedagang (Alice dan Bob) dan memeriksa bahwa saldo pelanggan cukup.
  - Mengurangi $25 dari akun Alice, menambahkan $24 ke akun Bob, mengambil $1 untuk layanan
  - Pedagang menerima isyarat positif dari Bank dan mengirimkan barang ke pelanggan.
- Komentar:
  - Bob dan Alice harus memiliki hubungan dengan bank.
  - Bank mengumpulkan informasi identifikasi tentang Bob dan Alice.
  - Bank mengambil potongan.
  - Bank harus dipercaya untuk menjaga uang setiap peserta setiap saat.

**Skenario 2 - Sistem Bitcoin**

- Pengaturan:
  - Lihat diagram/penjelas di Figjam terlampir - [Skema Aktivitas](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
- Gantikan Bank dengan sembilan siswa yang akan memainkan peran sebagai Komputer (Node/Miner Bitcoin) dalam jaringan untuk menggantikan Bank.
- Setiap dari 9 Komputer memiliki catatan historis lengkap dari semua transaksi yang pernah dilakukan (sehingga saldo akurat tanpa pemalsuan), serta seperangkat aturan:
  - Memverifikasi transaksi ditandatangani dengan benar (kuncipas)
  - Menyiarkan dan menerima transaksi yang valid ke rekan dalam jaringan, membuang yang tidak valid (termasuk yang mencoba menghabiskan dana yang sama dua kali)
- Memperbarui/Menambahkan catatan secara berkala dengan transaksi baru yang diterima dari komputer "acak" asalkan semua kontennya valid (catatan: untuk saat ini, kita mengabaikan komponen Bukti Kerja dari semua ini, untuk kesederhanaan), jika tidak menolak ini dan lanjutkan seperti sebelumnya sampai komputer "acak" berikutnya mengirim pembaruan
  - Jumlah yang tepat diberikan sebagai hadiah jika kontennya valid.
- Mempraktikkan urutan peristiwa:
  - Pelanggan- menjelajahi toko online dan menemukan barang seharga $25 yang mereka inginkan, dan memberitahu Pedagang mereka ingin membeli
  - Pedagang- meminta pembayaran dengan mengirimkan faktur/alamat dari dompet mereka kepada pelanggan.
  - Pelanggan- membuat transaksi (mengirimkan BTC senilai $25 ke alamat yang diberikan oleh Pedagang) dan menyiarkannya ke Jaringan Bitcoin.
- Komputer- menerima transaksi dan memverifikasi:
  - Ada setidaknya $25 BTC di alamat yang dikirim
  - Transaksi ditandatangani dengan benar (“dibuka” oleh pelanggan)
  - Jika tidak demikian, maka transaksi tidak akan disebarkan melalui jaringan, dan jika iya, maka akan disebarkan dan ditahan menunggu.
  - Pedagang dapat memeriksa bahwa transaksi sedang tertunda dan menunggu.
- Satu komputer dipilih “secara acak” untuk mengusulkan untuk menyelesaikan transaksi yang diusulkan dengan menyiarkan “blok” yang mengandungnya; jika diperiksa, mereka akan menerima hadiah BTC.
  - OPSIONAL/LANJUTAN - alih-alih memilih Komputer secara acak, simulasi penambangan dengan membuat Komputer melempar dadu sampai beberapa hasil yang telah ditentukan terjadi (misalnya, yang pertama mendapatkan dua enam adalah yang dipilih)
  - Ini juga dapat memainkan apa yang akan terjadi jika dua Komputer menang hampir bersamaan, menghasilkan pemisahan rantai.
  - Komputer memeriksa keabsahan, memperbarui/menambahkan catatan ke buku besar mereka jika aturan dipenuhi, dan menyiarkan blok ke rekan.
  - Komputer yang dipilih secara acak menerima hadiah karena mengusulkan blok yang valid.
  - Pedagang memeriksa transaksi telah diselesaikan; dengan demikian, dana diterima, dan barang dikirim ke pelanggan.
- Komentar:
  - Perhatikan tidak ada kebutuhan untuk hubungan perbankan yang sudah ada sebelumnya.
  - Tidak perlu pihak ketiga untuk memfasilitasi; digantikan oleh kode/insentif.
  - Tidak ada pengumpulan data oleh siapa pun di luar pertukaran langsung dan hanya jumlah yang diperlukan yang harus ditukarkan antar peserta (misalnya, alamat pengiriman).
  - Tidak ada kepercayaan yang diperlukan antara orang-orang (selain Pedagang yang mengirim barang), seperti pembelian tunai dalam banyak hal.
  - Uang dimiliki langsung oleh individu.
  - Buku besar Bitcoin digambarkan dalam dolar untuk kesederhanaan, tetapi pada kenyataannya, itu adalah BTC.
  - Kami mensimulasikan satu transaksi yang disiarkan, tetapi pada kenyataannya, banyak transaksi tertunda dalam jaringan, dan blok mencakup ribuan transaksi sekaligus. Node juga memeriksa tidak ada transaksi double-spend yang tertunda (saya akan membuang semua kecuali satu jika itu kasusnya).
- Skenario kecurangan:
  - Bagaimana jika pelanggan tidak memiliki $25 BTC?
    - Mereka tidak akan dapat membuat transaksi karena “membuka” dan “kepemilikan” adalah hal yang sama, dan komputer memeriksa transaksi ditandatangani dengan benar; jika tidak, mereka menolaknya.
- Bagaimana jika komputer yang dipilih secara acak mencoba untuk "mengubah buku besar"?
  - Blok tersebut akan ditolak, karena setiap komputer lain memiliki sejarah lengkap dan akan menyadari perubahan tersebut, melanggar salah satu aturan mereka.
  - Komputer Acak tidak akan mendapatkan hadiah, dan tidak ada transaksi dari blok mereka yang akan difinalisasi.

## Penilaian Pengetahuan

<chapterId>1461f064-933d-50ea-8935-324b68ec5d5f</chapterId>

### Diskusi Kelas KA

Diskusikan beberapa penyederhanaan yang dibuat dalam latihan kelas di bawah skenario kedua dan jelaskan apa yang sebenarnya dilakukan sistem Bitcoin secara lebih detail.

### Ulasan Kosakata KA

Definisikan istilah-istilah kunci berikut yang diperkenalkan di bagian sebelumnya:

- Node
- Mempool
- Target Kesulitan
- Blok

**Diskusikan makna beberapa istilah tambahan sebagai kelompok:**

Blockchain, Transaksi, Double-Spend, Masalah Jenderal Byzantine, Penambangan, Proof of Work (PoW), Fungsi Hash, Hadiah Blok, Blockchain, Rantai Terpanjang, Serangan 51%, Output, Kunci Output, Perubahan, Satoshis, Kunci Publik/Privat, Alamat, Kriptografi Kunci Publik, Tanda Tangan Digital, Dompet

# Memperkenalkan BTCPay Server

<partId>9c8a2d0c-9ba1-5c39-874c-f9eaf1bba663</partId>

## Memahami layar login BTCPay Server

<chapterId>14aad54c-9bd8-54f2-9455-178b8ae63408</chapterId>

### Bekerja dengan BTCPay Server

Tujuan blok kursus ini akan untuk memiliki pemahaman umum tentang perangkat lunak BTCPay Server. Dalam lingkungan bersama, disarankan untuk mengikuti demonstrasi instruktur dan mengikuti bersama dengan Buku Panduan Kursus BTCPay Server untuk mengikuti guru. Anda akan belajar cara membuat dompet melalui beberapa metode. Contoh termasuk pengaturan dompet Hot dan dompet perangkat keras yang terhubung melalui BTCPay Server Vault. Tujuan ini terjadi di lingkungan Demo, ditampilkan dan diberikan akses oleh instruktur kursus Anda.

Jika Anda mengikuti kursus ini sendirian, Anda dapat menemukan daftar host pihak ketiga untuk tujuan Demo di https://directory.btcpayserver.org/filter/hosts. Kami sangat menyarankan agar tidak menggunakan opsi pihak ketiga ini sebagai lingkungan produksi, tetapi mereka melayani tujuan yang tepat untuk pengenalan menggunakan Bitcoin dan BTCPay Server.

Sebagai peserta pelatihan bintang rock BTCPay Server, Anda mungkin memiliki pengalaman sebelumnya dalam mengatur node Bitcoin. Kursus ini akan berbicara secara khusus disesuaikan untuk tumpukan Perangkat Lunak BTCPay Server.

Banyak opsi di BTCPay Server ada dalam beberapa bentuk atau lainnya dalam perangkat lunak terkait Dompet Bitcoin lainnya.

### Layar Login BTCPay Server

Saat Anda disambut ke lingkungan Demo, Anda diminta untuk 'Login' atau 'Buat akun Anda.' Administrator server mungkin mematikan fitur membuat akun baru untuk alasan keamanan. Logo dan warna tombol BTCPay Server dapat diubah karena BTCPay Server adalah Perangkat Lunak Sumber Terbuka. Host pihak ketiga dapat Melabeli-putih perangkat lunak dan mengubah seluruh tampilannya.

![image](assets/en/0.webp)

### Jendela Buat Akun

Membuat akun di BTCPay Server memerlukan string Alamat Email yang valid; example@email.com akan menjadi string yang valid untuk Email.

Kata sandi harus setidaknya 8 karakter panjangnya, termasuk huruf, angka, dan karakter. Setelah menetapkan kata sandi sekali, Anda harus memverifikasi kata sandi yang diketik untuk memastikan itu benar dengan apa yang diketik di kolom kata sandi pertama.
Ketika kedua bidang Email dan Kata Sandi telah diisi dengan benar, klik tombol 'Buat Akun'. Ini akan menyimpan Email dan kata sandi pada instansi BTCPay Server instruktur.
![image](assets/en/1.webp)

**!Catatan!**

Jika Anda mengikuti kursus ini sendirian, membuat akun ini akan menjadi sesuatu yang mungkin Anda lakukan pada host pihak ketiga; oleh karena itu, sekali lagi, kami menyebutkan untuk tidak menggunakan ini sebagai lingkungan produksi tetapi hanya untuk tujuan pelatihan.

### Pembuatan Akun oleh Administrator BTCPay Server

Administrator Instansi BTCPay Server juga dapat membuat akun untuk BTCPay Server. Administrator instansi BTCPay Server dapat mengklik 'Pengaturan Server' (1), klik pada tab 'Pengguna' (2), dan klik tombol "+ Tambah Pengguna" (3) di bagian kanan atas tab Pengguna. Dalam Tujuan (4.3), Anda akan mempelajari lebih lanjut tentang kontrol administrator terhadap Akun.

![image](assets/en/2.webp)

Sebagai administrator, Anda akan memerlukan alamat Email pengguna dan menetapkan kata sandi standar. Disarankan sebagai Administrator untuk memberitahu pengguna bahwa mereka harus mengubah kata sandi ini sebelum menggunakan akun untuk alasan keamanan. Jika Administrator TIDAK menetapkan Kata Sandi dan SMTP telah diatur pada server, pengguna akan menerima email dengan tautan undangan untuk membuat akun mereka dan menetapkan kata sandi mereka sendiri.

### Contoh

Ketika mengikuti kursus oleh seorang instruktur, ikuti tautan yang diberikan oleh instruktur dan buat akun Anda pada lingkungan Demo yang disediakan. Pastikan alamat email dan kata sandi Anda disimpan dengan aman; Anda akan memerlukan kredensial login ini untuk sisa tujuan demo dalam kursus ini.

Instruktur Anda mungkin telah mengumpulkan alamat email terlebih dahulu dan mengirimkan tautan undangan sebelum latihan ini. Jika diinstruksikan, periksa Email Anda.

Ketika mengambil kursus tanpa instruktur, buat akun Anda menggunakan lingkungan demo BTCPay Server; pergi ke

https://mainnet.demo.btcpayserver.org/login.

Akun ini hanya harus digunakan untuk tujuan demonstrasi/pelatihan dan tidak pernah untuk bisnis.

### Ringkasan Keterampilan

Dalam bagian ini, Anda mempelajari hal berikut:

- Cara membuat akun pada server yang dihosting melalui antarmuka.
- Bagaimana seorang administrator server dapat secara manual menambahkan pengguna dalam pengaturan server.

### Penilaian Pengetahuan

#### KA Tinjauan Konseptual

Berikan alasan mengapa menggunakan Server Demo adalah ide buruk untuk tujuan produksi.

## Mengelola akun pengguna

<chapterId>b58ca6ee-b7fc-5e81-a6aa-c8ff212b4c55</chapterId>

### Manajemen Akun pada BTCPay Server

Setelah pemilik toko telah membuat akun mereka, mereka dapat mengelolanya di Bagian Kiri Bawah dari UI BTCPay Server. Di bawah tombol Akun, ada beberapa pengaturan tingkat tinggi.

- Mode Gelap/Terang.
- Tombol Sembunyikan Info Sensitif.
- Kelola Akun.

![image](assets/en/3.webp)

### Mode Gelap dan Terang

Pengguna BTCPay Server dapat memilih antara versi UI Mode Gelap atau Terang. Halaman yang menghadap pelanggan tidak akan berubah. Mereka menggunakan pengaturan yang disukai pelanggan mengenai mode gelap atau terang.

### Tombol Sembunyikan Info Sensitif

Tombol sembunyikan info sensitif membawa lapisan keamanan yang cepat dan sederhana. Kapanpun Anda perlu mengoperasikan BTCPay Server Anda, tetapi mungkin ada orang yang mengintip dari belakang Anda di ruang publik, aktifkan Sembunyikan Info Sensitif, dan semua nilai dalam BTCPay Server akan disembunyikan. Seseorang mungkin dapat melihat dari belakang Anda tetapi tidak lagi dapat melihat nilai yang Anda hadapi.

### Kelola Akun

Setelah akun pengguna telah dibuat, inilah tempat untuk mengelola kata sandi, 2fa, atau kunci API.

### Kelola Akun - Akun

Anda dapat memperbarui akun Anda dengan alamat Email yang berbeda secara opsional. Untuk memastikan alamat email Anda benar, BTCPay Server memungkinkan Anda untuk mengirim email verifikasi. Klik simpan jika pengguna menetapkan alamat email baru dan mengonfirmasi verifikasi berhasil. Nama pengguna tetap sama seperti Email sebelumnya.

Pengguna dapat memutuskan untuk menghapus seluruh akun mereka. Ini dapat dilakukan dengan mengklik tombol hapus pada tab Akun.

![image](assets/en/4.webp)

**!Catatan!**

Setelah mengubah Email, nama pengguna untuk akun tidak akan berubah. Alamat Email yang diberikan sebelumnya akan tetap menjadi nama Login.

### Kelola Akun - Kata Sandi

Seorang siswa mungkin ingin mengubah kata sandinya. Dia dapat melakukan ini dengan pergi ke tab Kata Sandi. Di sini dia diharuskan untuk mengetik kata sandi lamanya dan dapat mengubahnya menjadi yang baru.

![image](assets/en/5.webp)

### Otentikasi Dua-Faktor (2fa)

Untuk membatasi konsekuensi dari kata sandi yang dicuri, Anda dapat menggunakan otentikasi dua-faktor (2fa), sebuah metode keamanan yang relatif baru. Anda dapat mengaktifkan otentikasi dua-faktor melalui Kelola akun dan tab untuk otentikasi dua-faktor. Anda harus menyelesaikan langkah kedua setelah masuk dengan nama pengguna dan kata sandi Anda.

BTCPay Server memungkinkan dua cara untuk mengaktifkan 2FA, 2FA berbasis Aplikasi (Authy, Google, Microsoft authenticators) atau melalui Perangkat Keamanan (FIDO2 atau LNURL Auth).

### Otentikasi Dua-Faktor - Berbasis Aplikasi

Berdasarkan Sistem Operasi ponsel Anda (Android atau iOS), pengguna dapat memilih antara aplikasi berikut;

1. Unduh autentikator dua-faktor;
   - Authy untuk [Android](https://play.google.com/store/apps/details?id=com.authy.authy) atau [iOS](https://apps.apple.com/us/app/authy/id494168017)
   - Microsoft Authenticator untuk [Android](https://play.google.com/store/apps/details?id=com.azure.authenticator) atau [iOS](https://apps.apple.com/us/app/microsoft-authenticator/id983156458)
   - Google Authenticator untuk [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=e%C2%80) atau [iOS](https://apps.apple.com/us/app/google-authenticator/id388497605)
2. Setelah mengunduh dan menginstal Aplikasi Authenticator.
   - Pindai Kode QR yang disediakan oleh BTCPay Server
   - Atau masukkan kunci yang dihasilkan oleh BTCPay Server secara manual ke dalam aplikasi Authenticator Anda.
3. Aplikasi Authenticator akan memberikan Anda kode unik. Masukkan kode unik di BTCPay Server untuk memverifikasi pengaturan, dan klik verifikasi untuk menyelesaikan proses.

![image](assets/en/6.webp)

### Ringkasan Keterampilan

Dalam bagian ini, Anda telah mempelajari hal-hal berikut:

- Opsi manajemen akun dan berbagai cara untuk mengelola akun pada instance BTCPay Server.
- Cara mengatur 2FA berbasis aplikasi.

### Penilaian Pengetahuan

#### KA Tinjauan Konseptual

Jelaskan bagaimana 2FA berbasis aplikasi membantu mengamankan akun Anda

## Membuat toko baru

<chapterId>463b3634-b49f-5512-a711-3b2e096fc2e0</chapterId>

### Membuat Toko Anda dengan Wizard

Ketika pengguna baru masuk ke BTCPay Server, lingkungannya kosong dan memerlukan toko pertama. Wizard pengenalan dari BTCPay Server akan memberikan pengguna opsi untuk 'Membuat toko Anda' (1). Toko dapat dilihat sebagai Rumah untuk kebutuhan Bitcoin Anda. Node BTCPay Server baru akan mulai dengan Menyinkronkan Blockchain Bitcoin (2). Tergantung pada infrastruktur apa Anda menjalankan BTCPay Server, ini bisa berkisar dari beberapa jam hingga beberapa hari. Versi saat ini dari instansi ditampilkan di sudut kanan bawah UI BTCPay Server Anda. Ini berguna untuk referensi saat melakukan troubleshooting.
![image](assets/en/7.webp)

### Wizard Membuat Toko Anda

Mengikuti kursus ini akan dimulai dengan layar yang sedikit berbeda dari halaman sebelumnya. Karena instruktur Anda telah menyiapkan lingkungan Demo, Blockchain Bitcoin telah disinkronkan sebelumnya, dan oleh karena itu Anda tidak akan melihat status sinkronisasi node.

Pengguna dapat memutuskan untuk menghapus seluruh akun mereka. Ini dapat dilakukan dengan mengklik tombol hapus pada tab Akun.

![image](assets/en/8.webp)

**!Catatan!**

Akun BTCPay Server dapat membuat jumlah toko yang tidak terbatas. Setiap toko adalah dompet atau “rumah”.

### Contoh

Mulailah dengan mengklik "Membuat toko Anda".

![image](assets/en/9.webp)

Ini akan membuat Rumah dan dasbor pertama Anda untuk menggunakan server BTCPay.

(1) Setelah mengklik "Membuat toko Anda", BTCPay Server akan meminta Anda untuk menamai toko; ini bisa apa saja yang berguna untuk Anda.

![image](assets/en/10.webp)

(2) Mata uang toko default harus ditetapkan selanjutnya, baik mata uang fiat atau dinominasikan dalam standar Bitcoin / Sats. Untuk lingkungan demo, kami akan menetapkannya ke USD.

![image](assets/en/11.webp)

(3) Sebagai parameter terakhir pada pengaturan toko, BTCPay Server meminta Anda untuk menetapkan "Sumber harga yang disukai" untuk membandingkan harga Bitcoin terhadap harga fiat saat ini sehingga toko Anda menampilkan nilai tukar yang benar antara Bitcoin dan mata uang fiat yang ditetapkan toko. Kami akan tetap menggunakan default dalam contoh Demo dan menetapkannya ke bursa Kraken. BTCPay Server menggunakan API Kraken untuk memeriksa nilai tukar.

![image](assets/en/12.webp)

(4) Sekarang setelah parameter toko ini telah ditetapkan, klik pada tombol Buat, dan BTCPay Server akan membuat dasbor toko pertama Anda, di mana wizard akan dilanjutkan.

![image](assets/en/13.webp)

Selamat, Anda telah membuat toko pertama Anda, dan ini merangkum latihan ini.

![image](assets/en/14.webp)

### Ringkasan Keterampilan

Dalam bagian ini, Anda belajar:

- Pembuatan toko dan mengonfigurasi mata uang default dikombinasikan dengan preferensi sumber harga.
- Setiap "Toko" adalah rumah baru yang terpisah dari toko lain pada instalasi BTCPay Server ini.

# Pengenalan untuk Mengamankan Kunci Bitcoin

<partId>25da22d8-fd37-51c5-af2a-58b9f3b046b2</partId>

## Memahami Generasi Kunci Bitcoin

<chapterId>d162735b-847b-578e-83b8-a044ab703ec5</chapterId>

### Apa yang terlibat dalam menghasilkan kunci bitcoin?

Dompet Bitcoin, ketika dibuat, menciptakan apa yang disebut "seed". Dalam objektif terakhir, Anda telah membuat "seed", Serangkaian kata yang dihasilkan sebelumnya juga dikenal sebagai frasa mnemonik. Seed digunakan untuk menurunkan Kunci Bitcoin individu dari dan digunakan untuk mengirim atau menerima Bitcoin. Frasa seed seharusnya tidak pernah dibagi dengan pihak ketiga atau rekan yang tidak dipercaya.
Generasi seed dilakukan sesuai dengan standar industri yang dikenal sebagai kerangka kerja "Hierarchical Deterministic" (HD).
![image](assets/en/15.webp)

### Alamat

BTCPay Server dibangun untuk menghasilkan Alamat baru. Ini mengurangi masalah penggunaan kembali kunci publik atau Alamat. Menggunakan kunci Publik yang sama membuat pelacakan seluruh riwayat pembayaran Anda menjadi sangat mudah. Memikirkan kunci sebagai voucher sekali pakai akan sangat meningkatkan privasi Anda. Kami juga menggunakan Alamat Bitcoin, jangan bingungkan ini dengan kunci Publik.

Alamat diturunkan dari kunci Publik melalui "algoritma hashing." Namun, kebanyakan dompet dan transaksi akan menampilkan Alamat daripada kunci publik tersebut. Alamat, pada umumnya, lebih pendek dari kunci publik dan biasanya dimulai dengan `1`, `3`, atau `bc1`, sedangkan kunci publik dimulai dengan `02`, `03`, atau `04`.

- Alamat yang dimulai dengan `1.....` masih merupakan alamat yang sangat umum. Seperti disebutkan dalam bab Membuat toko baru, ini adalah alamat warisan. Jenis alamat ini dimaksudkan untuk transaksi P2PKH. P2Pkh menggunakan pengkodean Base58, yang membuat alamat tersebut sensitif terhadap huruf besar atau kecil. Strukturnya didasarkan pada kunci publik dengan tambahan 1 digit sebagai pengenal.

- Alamat yang dimulai dengan `bc1...` perlahan bergerak menjadi alamat yang sangat umum. Ini dikenal sebagai Alamat SegWit (native) SegWit. Ini menawarkan struktur biaya yang lebih baik daripada Alamat yang disebutkan lainnya. Alamat SegWit Asli menggunakan pengkodean Bech32 dan hanya memungkinkan huruf kecil.

- Alamat yang dimulai dengan `3...` umumnya masih digunakan oleh bursa untuk alamat deposit. Alamat ini disebutkan dalam bab Membuat toko baru, alamat SegWit terbungkus atau bersarang. Namun, mereka juga bisa berfungsi sebagai "Alamat Multisig". Ketika digunakan sebagai alamat SegWit, ada beberapa penghematan pada biaya transaksi lagi, meskipun tidak sebanyak Native SegWit. Alamat P2SH menggunakan pengkodean Base58. Ini membuatnya sensitif terhadap huruf besar atau kecil, seperti alamat warisan.

- Alamat yang dimulai dengan `2...` adalah alamat Testnet. Mereka dimaksudkan untuk menerima bitcoin testnet (tBTC). Anda tidak boleh mencampuradukkannya dan mengirim Bitcoin ke alamat ini. Untuk tujuan pengembangan, Anda dapat menghasilkan dompet testnet. Ada beberapa faucet online untuk mendapatkan Bitcoin testnet. Jangan pernah membeli Bitcoin Testnet. Bitcoin Testnet ditambang. Ini mungkin menjadi alasan bagi pengembang untuk menggunakan Regtest sebagai gantinya. Ini adalah lingkungan bermain untuk pengembang, tanpa beberapa komponen jaringan. Namun, Bitcoin, untuk tujuan pengembangan, sangat berguna.

### Kunci Publik

Kunci publik menjadi kurang digunakan dalam praktik hari ini. Seiring waktu, pengguna bitcoin telah menggantinya dengan Alamat. Mereka masih ada dan sesekali masih digunakan. Kunci publik, pada umumnya, adalah string yang jauh lebih panjang daripada alamat. Sama seperti dengan alamat, mereka dimulai dengan pengenal spesifik.

- Pertama, `02...` dan `03...` adalah pengenal kunci publik yang sangat standar yang dikodekan dalam format SEC. Ini dapat diproses dan diubah menjadi alamat untuk menerima, digunakan untuk membuat alamat multi-sig, atau untuk memverifikasi tanda tangan. Transaksi Bitcoin hari-hari awal menggunakan kunci publik sebagai bagian dari transaksi P2PK.

- Namun, dompet HD menggunakan struktur yang berbeda. `xpub...`, `ypub...` atau `zpub...` disebut kunci publik ekstensi atau xpubs. Kunci-kunci ini digunakan untuk menurunkan banyak kunci publik karena merupakan bagian dari dompet HD. Karena xpub Anda menyimpan catatan seluruh riwayat Anda, yang berarti transaksi masa lalu dan masa depan, jangan pernah membagikan ini dengan pihak yang tidak dipercaya.

### Ringkasan Keterampilan

Dalam bagian ini, Anda telah mempelajari hal-hal berikut:

- Perbedaan antara alamat dan tipe data kunci publik serta manfaat menggunakan alamat dibandingkan dengan kunci publik.

### Penilaian Pengetahuan

Jelaskan manfaat menggunakan alamat baru untuk setiap transaksi dibandingkan dengan penggunaan ulang alamat atau metode kunci publik

## Mengamankan kunci dengan dompet perangkat keras

<chapterId>c54a6d61-5a43-5fdb-93ae-c6750de9c612</chapterId>

### Menyimpan Kunci Bitcoin

Setelah menghasilkan frasa benih, daftar 12 - 24 kata yang dihasilkan dalam buku ini memerlukan cadangan dan keamanan yang tepat, karena kata-kata ini adalah satu-satunya cara untuk memulihkan akses ke dompet. Struktur dompet HD dan bagaimana ia menghasilkan alamat secara deterministik menggunakan satu benih tersebut, semua alamat yang Anda buat akan dicadangkan menggunakan daftar kata mnemonik ini yang mewakili frasa benih atau frasa pemulihan Anda.

Jaga frasa pemulihan Anda agar tetap aman. Jika diakses oleh seseorang, khususnya dengan niat jahat, mereka dapat memindahkan dana Anda. Menjaga benih tetap aman dan terjaga tetapi juga mengingatnya adalah saling berkaitan. Ada beberapa metode untuk menyimpan kunci privat Bitcoin, masing-masing dengan kelebihan dan kekurangan, baik dalam keamanan, privasi, kenyamanan, atau sarana fisik. Karena pentingnya kunci privat, pengguna bitcoin cenderung menyimpan dan menjaga kunci ini secara "self custody" daripada menggunakan layanan "custodial" seperti bank. Tergantung pada pengguna, ia harus menggunakan solusi Penyimpanan Dingin atau Dompet Panas.

### Penyimpanan Panas dan Dingin kunci bitcoin

Biasanya, dompet bitcoin dikategorikan dalam Dompet Panas atau Dompet Dingin. Sebagian besar pertimbangan terletak pada kenyamanan, kemudahan penggunaan, dan risiko keamanan. Masing-masing metode ini juga dapat dilihat dalam solusi penitipan. Namun, pertimbangan di sini sebagian besar berbasis keamanan dan privasi dan melampaui lingkup kursus ini.

### Dompet Panas

Dompet panas adalah cara paling nyaman untuk berinteraksi dengan Bitcoin melalui perangkat seluler, web, atau perangkat lunak desktop. Dompet selalu terhubung ke internet, memungkinkan pengguna untuk mengirim atau menerima Bitcoin. Namun, ini juga menjadi kelemahannya, dompet, karena selalu online, sekarang lebih rentan terhadap serangan oleh peretas atau malware pada perangkat Anda. Di BTCPay Server, dompet panas menyimpan kunci privat pada instansinya. Siapa pun yang mengakses toko BTCPay Server Anda dapat mencuri dana dari alamat ini jika berniat jahat. Ketika BTCPay Server berjalan dalam lingkungan yang dihosting, Anda harus selalu mempertimbangkan ini dalam profil keamanan Anda dan sebaiknya tidak menggunakan Dompet Panas dalam kasus seperti itu. Ketika BTCPay Server diinstal pada perangkat keras milik sendiri, yang diamankan dan dipercaya oleh Anda, profil risiko menurun secara signifikan, tetapi tidak pernah hilang!

### Dompet Dingin

Individu memindahkan Bitcoin mereka ke dompet dingin karena dapat mengisolasi kunci privat dari internet. Menghilangkan koneksi internet dari persamaan mengurangi risiko malware, spyware, dan penggantian SIM. Penyimpanan dingin dianggap lebih unggul dari penyimpanan panas untuk keamanan dan otonomi, selama tindakan pencegahan yang memadai diambil untuk menghindari kehilangan kunci privat Bitcoin. Penyimpanan dingin paling cocok untuk jumlah Bitcoin yang besar, yang tidak dimaksudkan untuk sering dibelanjakan karena kompleksitas pengaturan dompet.

Ada berbagai metode tentang cara menyimpan kunci Bitcoin dalam penyimpanan dingin, dari dompet kertas hingga dompet otak, dompet perangkat keras, atau, dari awal, sebuah file dompet. Sebagian besar dompet menggunakan BIP 39 untuk menghasilkan frasa benih. Namun, dalam perangkat lunak Bitcoin Core, masih belum ada konsensus tentang penggunaannya. Perangkat lunak Bitcoin Core masih akan menghasilkan file Wallet.dat yang perlu Anda simpan di lokasi offline yang aman.

### Ringkasan Keterampilan

Dalam bagian ini, Anda telah belajar:

- Perbedaan antara dompet panas dan dompet dingin dari segi fungsionalitas dan pertimbangan mereka.
- Apa itu dompet?
- Apa perbedaan antara dompet panas dan dompet dingin?

- Jelaskan yang dimaksud dengan "menghasilkan dompet"?

## Menggunakan kunci Bitcoin Anda

<chapterId>bff488de-5052-56e6-b696-97e896f762ae</chapterId>

### Dompet BTCPay Server

BTCPay Server terdiri dari fitur dompet standar berikut:

- Transaksi
- Kirim
- Terima
- Pindai ulang
- Pembayaran Tarik
- Pembayaran
- PSBT
- Pengaturan Umum

### Transaksi

Administrator dapat melihat transaksi masuk dan keluar untuk dompet on-chain yang terhubung dengan toko spesifik ini dalam tampilan transaksi. Setiap transaksi memiliki perbedaan antara diterima dan dikirim. Yang diterima akan berwarna hijau dan transaksi keluar akan berwarna merah. Dalam tampilan transaksi BTCPay Server, administrator juga akan melihat set label standar.

| Tipe Transaksi  | Deskripsi                                                    |
| --------------- | ------------------------------------------------------------ |
| App             | Pembayaran diterima melalui faktur aplikasi yang dibuat      |
| invoice         | Pembayaran diterima melalui faktur                           |
| payjoin         | Tidak dibayar, timer faktur masih belum berakhir             |
| payjoin-exposed | UTXO terpapar melalui proposal payjoin faktur                |
| payment-request | Pembayaran diterima melalui permintaan pembayaran            |
| payout          | Pembayaran dikirim melalui pembayaran atau pengembalian dana |

### Cara Mengirim

Fungsi kirim BTCPay server mengirim transaksi dari dompet on-chain BTCPay Server Anda. BTCPay Server memungkinkan beberapa cara untuk menandatangani transaksi Anda untuk menghabiskan dana. Transaksi dapat ditandatangani dengan;

- Dompet Perangkat Keras
- Dompet yang mendukung PSBT
- Kunci privat HD atau benih pemulihan.
- Dompet Panas

#### Dompet perangkat keras

BTCPay Server memiliki dukungan dompet perangkat keras bawaan yang memungkinkan Anda menggunakan dompet perangkat keras Anda dengan BTCPay Vault tanpa membocorkan informasi ke aplikasi atau server pihak ketiga. Integrasi dompet perangkat keras dalam BTCPay Server memungkinkan Anda untuk mengimpor dompet perangkat keras Anda dan menghabiskan dana masuk dengan konfirmasi sederhana di perangkat Anda. Kunci privat Anda tidak pernah meninggalkan perangkat, dan semua dana divalidasi terhadap node penuh Anda sehingga tidak ada kebocoran data.

#### Menandatangani dengan dompet yang mendukung PSBT

PSBT (Partially Signed Bitcoin transactions) adalah format pertukaran untuk transaksi Bitcoin yang masih perlu ditandatangani sepenuhnya. PSBT didukung di BTCPay Server dan dapat ditandatangani dengan dompet perangkat keras dan perangkat lunak yang kompatibel.

Konstruksi transaksi Bitcoin yang sepenuhnya ditandatangani melalui langkah-langkah berikut:

- PSBT dibuat dengan input dan output tertentu tetapi tanpa tanda tangan
- PSBT yang diekspor dapat diimpor oleh dompet yang mendukung format ini
- Data transaksi dapat diperiksa dan ditandatangani menggunakan dompet
- File PSBT yang ditandatangani diekspor dari dompet dan diimpor dengan BTCPay Server
- BTCPay Server menghasilkan transaksi Bitcoin akhir
- Anda memverifikasi hasilnya dan menyiarkannya ke jaringan

#### Menandatangani dengan Kunci Privat HD atau benih mnemonik

Jika Anda telah membuat dompet sebelumnya menggunakan BTCPay Server, Anda dapat menghabiskan dana dengan memasukkan kunci privat Anda ke dalam bidang yang sesuai. Tetapkan "AccountKeyPath" yang tepat di pengaturan dompet; jika tidak, Anda tidak dapat menghabiskan.

#### Menandatangani dengan dompet panas

Jika Anda membuat dompet baru saat menyiapkan toko Anda dan mengaktifkannya sebagai dompet panas, itu akan secara otomatis menggunakan benih yang disimpan di server untuk menandatangani.

### RBF (Replace-By-Fee)

Replace-By-Fee (RBF) adalah fitur protokol Bitcoin yang memungkinkan Anda mengganti transaksi yang telah disiarkan sebelumnya (sementara masih belum dikonfirmasi). Ini memungkinkan pengacakan sidik jari transaksi dompet Anda atau menggantinya dengan tarif biaya yang lebih tinggi untuk memindahkan transaksi lebih tinggi dalam antrian prioritas konfirmasi (penambangan). Ini akan secara efektif menggantikan transaksi asli karena tarif biaya yang lebih tinggi akan diprioritaskan, dan setelah dikonfirmasi, akan membatalkan transaksi asli (tidak ada pengeluaran ganda).
Tekan tombol "Pengaturan Lanjutan" untuk melihat opsi RBF;

![image](assets/en/16.webp)

- Acak untuk privasi yang lebih tinggi, Memungkinkan transaksi diganti secara otomatis untuk pengacakan sidik jari transaksi.
- Ya, Tandai transaksi untuk RBF dan dapat diganti secara eksplisit (Tidak diganti secara default, hanya dengan masukan)
- Tidak, Jangan izinkan transaksi diganti.

### Pemilihan Koin

Pemilihan koin adalah fitur privasi lanjutan yang memungkinkan Anda memilih koin yang ingin Anda belanjakan saat membuat transaksi. Misalnya, membayar dengan koin yang baru dari campuran conjoin.

Pemilihan koin bekerja secara asli dengan fitur label dompet. Ini memungkinkan Anda memberi label pada dana masuk untuk pengelolaan UTXO dan pengeluaran yang lebih lancar.

BTCPay Server juga mendukung BIP-329 untuk pengelolaan label. BIP-329 memungkinkan label pada; jika Anda mentransfer dari dompet yang mendukung BIP tertentu ini dan menetapkan label, BTCPay Server akan mengenali ini dan mengimpor mereka. Saat memigrasi server, informasi ini juga dapat diekspor dan diimpor ke lingkungan baru.

### Cara Menerima

Ketika mengklik tombol terima di BTCPay Server, itu menghasilkan alamat yang belum digunakan yang dapat digunakan untuk menerima pembayaran. Administrator juga dapat menghasilkan alamat baru dengan menghasilkan "Invoice" baru.

BTCPay Server akan selalu meminta untuk menghasilkan alamat BTC yang tersedia berikutnya untuk menghindari penggunaan alamat ulang. Setelah mengklik "Generate next available BTC Address," BTCPay Server menghasilkan alamat baru dan QR. Ini juga memungkinkan Anda untuk langsung menetapkan Label ke alamat untuk pengelolaan alamat Anda yang lebih baik.

![image](assets/en/17.webp)

![image](assets/en/18.webp)

#### Pemindaian Ulang

Fitur Rescan mengandalkan “Scantxoutset” dari Bitcoin Core 0.17.0 untuk memindai keadaan saat ini dari blockchain (disebut Set UTXO) untuk koin yang termasuk dalam skema derivasi yang dikonfigurasi. Pemindaian ulang dompet menyelesaikan dua masalah yang dialami pengguna BTCPay Server.

1. Masalah batas celah - Sebagian besar dompet pihak ketiga adalah dompet ringan yang berbagi node antara banyak pengguna. Dompet yang bergantung pada node ringan dan penuh membatasi jumlah (biasanya 20) alamat tanpa saldo yang mereka lacak di blockchain untuk mencegah masalah kinerja. BTCPay Server menghasilkan alamat baru untuk setiap invoice. Dengan hal di atas, setelah BTCPay Server menghasilkan 20 invoice yang tidak dibayar secara berturut-turut, dompet eksternal berhenti mengambil transaksi, dengan asumsi tidak ada transaksi baru yang terjadi. Dompet eksternal Anda tidak akan menampilkannya setelah invoice dibayar pada ke-21, ke-22, dll. Di sisi lain, secara internal, dompet BTCPay Server melacak alamat apa pun yang dihasilkannya bersama dengan batas celah yang jauh lebih besar. Ini tidak bergantung pada pihak ketiga dan selalu dapat menampilkan saldo yang benar.
2. Solusi Batas Gap - Jika [dompet eksternal/ada](https://docs.btcpayserver.org/WalletSetup/#use-an-existing-wallet) Anda memungkinkan konfigurasi batas gap, solusi mudahnya adalah meningkatkannya. Namun, sebagian besar dompet tidak memungkinkan ini. Dompet yang kami tahu memungkinkan konfigurasi batas gap hanyalah Electrum, Wasabi, dan Sparrow Wallet. Sayangnya, Anda kemungkinan akan menemui masalah dengan banyak dompet lainnya. Untuk pengalaman pengguna dan privasi terbaik, pertimbangkan untuk tidak menggunakan dompet eksternal dan menggunakan dompet internal BTCPay Server.

#### BTCPay Server menggunakan “mempoolfullrbf=1”

BTCPay Server menggunakan “mempoolfullrbf=1”; kami telah menambahkan ini sebagai default pada pengaturan BTCPay Server Anda. Namun, kami juga telah membuatnya sebagai fragmen yang dapat Anda nonaktifkan sendiri. Tanpa “mempoolfullrbf=1,” jika pelanggan melakukan double-spend pada pembayaran dengan transaksi yang tidak menandakan RBF, Merchant hanya akan tahu setelah konfirmasi.

Seorang administrator mungkin ingin memilih keluar dari pengaturan ini. Dengan string berikut, Anda dapat mengubah set default.

```
BTCPAYGEN_EXCLUDE_FRAGMENTS="$BTCPAYGEN_EXCLUDE_FRAGMENTS;opt-mempoolfullrbf"
. btcpay-setup.sh -i**
```

### Pengaturan Dompet BTCPay Server

Pengaturan dompet dalam BTCPay Server memberikan gambaran yang jelas dan cepat tentang pengaturan umum dompet Anda. Semua pengaturan ini telah diisi sebelumnya jika dompet dibuat dengan BTCPay Server.

![image](assets/en/19.webp)

Pengaturan dompet dalam BTCPay Server memberikan gambaran yang jelas dan cepat tentang pengaturan umum dompet Anda. Semua pengaturan ini telah diisi sebelumnya jika dompet dibuat dengan BTCPay Server. Pengaturan dompet BTCPay Server dimulai dengan status dompet. Apakah itu Watch-only atau Hot wallet? Tergantung pada jenis dompet, tindakan dapat bervariasi dari memindai ulang dompet untuk transaksi yang hilang, Memangkas transaksi lama dari riwayat, mendaftarkan dompet untuk tautan pembayaran, atau mengganti dan menghapus dompet saat ini yang terhubung ke toko. Dalam pengaturan dompet BTCPay Server, administrator dapat menetapkan Label untuk dompet untuk manajemen dompet yang lebih baik. Di sini Administrator juga akan dapat melihat Skema Turunan, kunci akun (xpub), Sidik Jari, dan Keypath. Pembayaran dalam pengaturan dompet hanya memiliki 2 pengaturan utama. Pembayaran tidak valid jika transaksi gagal dikonfirmasi dalam (menit yang ditetapkan) setelah kedaluwarsa faktur. Pertimbangkan faktur dikonfirmasi ketika transaksi pembayaran memiliki X jumlah konfirmasi. Administrator juga dapat mengatur toggle untuk menampilkan biaya yang direkomendasikan pada pembayaran atau menetapkan target konfirmasi manual dalam jumlah blok.

![image](assets/en/20.webp)

**!Catatan!**

Jika Anda mengikuti kursus ini sendiri, membuat akun ini mungkin adalah sesuatu yang mungkin Anda lakukan di host pihak ketiga, oleh karena itu lagi kami menyebutkan untuk tidak pernah menggunakan ini sebagai lingkungan produksi, tetapi hanya untuk tujuan pelatihan.

### Contoh

#### Menyiapkan Dompet Bitcoin di BTCPay Server

BTCPay Server memungkinkan dua cara pengaturan dompet. Salah satu caranya adalah mengimpor dompet Bitcoin yang sudah ada. Impor dapat dilakukan dengan Menghubungkan dompet perangkat keras, mengimpor file Dompet, memasukkan Kunci publik yang diperluas, Memindai kode QR dompet, atau yang paling tidak disukai, memasukkan Benih pemulihan Dompet yang dibuat sebelumnya dengan tangan. Di BTCPay Server, juga dimungkinkan untuk membuat dompet baru. Ada dua cara yang mungkin untuk mengonfigurasi BTCPay Server saat menghasilkan dompet baru.
Opsi dompet panas (hot wallet) di BTCPay Server memungkinkan fitur seperti 'Payjoin' atau 'Liquid'. Namun, ada kekurangan, seed pemulihan yang dihasilkan untuk Dompet ini akan disimpan di server, di mana siapa pun yang memiliki kontrol Admin dapat mengambil seed pemulihan tersebut. Karena kunci privat Anda berasal dari seed pemulihan Anda, aktor jahat bisa mendapatkan akses ke dana Anda saat ini dan masa depan!

Untuk mengurangi risiko tersebut di BTCPay Server, seorang Admin dapat mengatur di Pengaturan Server > Kebijakan > "Izinkan non-admin untuk membuat dompet panas untuk toko mereka" menjadi tidak, seperti yang secara default. Untuk meningkatkan keamanan dompet Panas tersebut, administrator server harus mengaktifkan otentikasi 2FA pada akun yang diizinkan memiliki dompet Panas. Menyimpan kunci privat di server publik berbahaya dan datang dengan risiko. Beberapa di antaranya mirip dengan risiko Jaringan Petir (lihat bab berikutnya untuk risiko Jaringan Petir).

Opsi kedua yang ditawarkan BTCPay Server dalam menghasilkan dompet baru adalah dengan membuat dompet Hanya-Pantau (Watch-Only wallet). BTCPay Server akan menghasilkan kunci privat Anda sekali saja. Setelah pengguna mengonfirmasi telah menuliskan Frase Seed mereka, BTCPay Server akan menghapus kunci privat dari server. Akibatnya, toko Anda sekarang memiliki dompet Hanya-Pantau yang terhubung kepadanya. Untuk menghabiskan dana yang diterima di dompet Hanya-Pantau Anda, lihat bab Cara Mengirim, baik dengan menggunakan BTCPay Server Vault, PSBT (transaksi bitcoin yang ditandatangani sebagian), atau, yang paling tidak direkomendasikan, secara manual menyediakan frase seed Anda.

Anda telah membuat 'Toko' baru di bagian terakhir. Wizard instalasi akan melanjutkan dengan meminta untuk "Menyiapkan dompet" atau "Menyiapkan node Petir". Dalam contoh ini, Anda akan mengikuti proses wizard "Menyiapkan dompet" (1).

![image](assets/en/21.webp)

Setelah mengklik "Menyiapkan dompet", wizard akan melanjutkan dengan meminta bagaimana Anda ingin melanjutkan; BTCPay Server sekarang menawarkan opsi untuk menghubungkan dompet Bitcoin yang ada ke toko baru Anda. Jika Anda tidak memiliki dompet, BTCPay Server menyarankan untuk membuat yang baru. Contoh ini akan mengikuti langkah-langkah untuk “membuat dompet baru” (2). Ikuti langkah-langkah untuk belajar cara "Menghubungkan dompet yang ada (1).

![image](assets/en/22.webp)

**!Catatan!**

Jika Anda mengikuti kursus ini di ruang kelas, contoh dan seed yang kami hasilkan saat ini hanya untuk tujuan pendidikan. Seharusnya tidak pernah ada jumlah yang signifikan selain yang diperlukan sepanjang latihan pada alamat-alamat ini.

(1) Lanjutkan wizard "Dompet baru" dengan mengklik tombol "Buat dompet baru".

![image](assets/en/23.webp)

(2) Setelah mengklik “Buat dompet baru,” jendela berikutnya dalam wizard akan memberikan opsi “Dompet Panas” dan “Dompet Hanya-Pantau.” Jika Anda mengikuti bersama instruktur, lingkungan Anda adalah Demo bersama, dan Anda hanya dapat membuat Dompet Hanya-Pantau. Perhatikan perbedaan antara kedua gambar di bawah ini. Karena Anda berada dalam lingkungan Demo mengikuti bersama instruktur, buatlah "Dompet Hanya-Pantau" dan lanjutkan dengan wizard "Dompet Baru".

![image](assets/en/24.webp)

![image](assets/en/25.webp)

(3) Melanjutkan wizard dompet baru, Anda sekarang berada di bagian Membuat dompet BTC Hanya-Pantau. Di sini kita dapat menetapkan tipe alamat dompet "Tipe Alamat" BTCPay Server memungkinkan Anda memilih Tipe Alamat yang Anda inginkan; pada saat penulisan kursus ini, masih direkomendasikan untuk menggunakan alamat bech32. Pelajari lebih lanjut secara detail tentang alamat di bab pertama dari bagian ini.

- Segwit (bech32)
- Native SegWit adalah alamat yang dimulai dengan `bc1q`.
  - Contoh: `bc1qXXXXXXXXXXXXXXXXXXXXXX`
- Legacy
  - Alamat Legacy adalah alamat yang dimulai dengan angka `1`.
  - Contoh: `15e15hXXXXXXXXXXXXXXXXXXXX`
- Taproot (Untuk pengguna lanjutan)
  - Alamat Taproot dimulai dengan `bc1p`.
  - Contoh: `bc1pXXXXXXXXXXXXXXXXXXXXXXXX`
- Segwit Terbungkus
  - Alamat Segwit Terbungkus adalah alamat yang dimulai dengan `3`.
  - Contoh: `37BBXXXXXXXXXXXXXXX`

Pilih segwit (disarankan) sebagai tipe alamat dompet yang Anda inginkan.

![image](assets/en/26.webp)

(4) Saat mengatur parameter untuk Dompet, BTCPay Server memungkinkan pengguna untuk menetapkan passphrase opsional melalui BIP39, pastikan untuk mengonfirmasi kata sandi Anda.

![image](assets/en/27.webp)

(5) Setelah menetapkan tipe Alamat Dompet dan mungkin menetapkan beberapa opsi lanjutan, klik Buat, dan BTCPay Server akan menghasilkan Dompet baru Anda. Perhatikan bahwa ini adalah langkah terakhir sebelum menghasilkan frasa benih Anda. Pastikan Anda hanya melakukan ini dalam lingkungan di mana orang lain mungkin tidak mencuri frasa benih dengan melihat layar Anda.

![image](assets/en/28.webp)

(6) Di layar berikutnya dari wizard, BTCPay Server menunjukkan frasa benih Pemulihan untuk Dompet yang baru dibuat; ini adalah kunci untuk memulihkan Dompet Anda dan menandatangani transaksi. BTCPay Server menghasilkan frasa benih dari 12 kata. Kata-kata ini akan dihapus dari server setelah layar pengaturan ini. Dompet ini secara khusus adalah dompet Hanya-Lihat. Disarankan untuk tidak menyimpan frasa benih ini secara digital atau melalui gambar fotografi. Pengguna hanya dapat melanjutkan dalam wizard jika mereka secara aktif mengakui bahwa mereka telah menuliskan frasa benih mereka.

![image](assets/en/29.webp)

(7) Setelah mengklik Selesai dan mengamankan frasa benih Bitcoin yang baru dihasilkan, BTCPay Server akan memperbarui toko Anda dengan Dompet baru yang terlampir dan siap untuk menerima pembayaran. Di Antarmuka Pengguna, di menu navigasi kiri, perhatikan bagaimana Bitcoin sekarang disorot dan diaktifkan di bawah Dompet.

![image](assets/en/30.webp)

### Contoh: Menuliskan frasa benih

Ini adalah momen yang sangat khusus dan aman untuk menggunakan Bitcoin. Seperti disebutkan sebelumnya, hanya Anda yang harus memiliki akses atau pengetahuan tentang frasa benih Anda. Saat Anda mengikuti bersama instruktur dan kelas, frasa benih yang dihasilkan hanya harus digunakan dalam kursus ini. Terlalu banyak faktor, mata-mata dari teman sekelas, sistem yang tidak aman, dan banyak lainnya membuat kunci-kunci ini hanya bersifat edukatif dan tidak dapat dipercaya. Namun, kunci yang dihasilkan harus tetap disimpan untuk contoh kursus.

Metode pertama yang akan kita gunakan dalam situasi saat ini, juga yang paling tidak aman, adalah menuliskan frasa benih dalam urutan yang benar. Kartu frasa benih ada dalam materi kursus yang disediakan untuk siswa atau ditemukan di GitHub BTCPay Server. Kami akan menggunakan kartu ini untuk menuliskan kata-kata yang dihasilkan di langkah sebelumnya. Pastikan untuk menuliskannya dalam urutan yang benar. Setelah Anda menuliskannya, periksa kembali dengan apa yang diberikan oleh perangkat lunak untuk memastikan Anda menuliskannya dalam urutan yang benar. Setelah Anda menuliskannya, klik kotak centang yang menyatakan Anda telah menuliskan frasa benih Anda dengan benar.

### Contoh: Menyimpan frasa benih pada Hardware Wallet

Dalam kursus ini, kami menyentuh tentang penyimpanan frasa benih pada hardware wallet. Mengikuti kursus ini oleh seorang instruktur mungkin tidak selalu menyertakan perangkat seperti itu. Dalam materi panduan kursus, telah ditulis daftar hardware wallet yang disediakan yang cocok untuk latihan ini.
Kita akan menggunakan BTCPay Server vault dan dompet perangkat keras Blockstream Jade dalam contoh ini.
Anda juga dapat mengikuti video referensi untuk cara menghubungkan dompet perangkat keras.
![BTCPay Server - Cara menghubungkan dompet perangkat keras Anda dengan BTCPay Vault.](https://youtu.be/s4qbGxef43A)

Unduh BTCPay Server Vault: https://github.com/btcpayserver/BTCPayServer.Vault/releases

Pastikan Anda mengunduh file yang benar untuk sistem Anda. Pengguna Windows harus mengunduh paket [BTCPayServerVault-2.0.5-setup.exe](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-2.0.5-setup.exe), pengguna Mac mengunduh [BTCPayServerVault-osx-x64-2.0.5.dmg](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-osx-x64-2.0.5.dmg), dan pengguna Linux harus mengunduh [BTCPayServerVault-Linux-2.0.5.tar.gz](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-Linux-2.0.5.tar.gz)

Setelah menginstal BTCPay Server Vault, mulai perangkat lunak dengan mengklik ikon di Desktop Anda. Ketika BTCPay Server Vault diinstal dengan benar dan dimulai untuk pertama kalinya, itu akan meminta izin untuk digunakan dengan Aplikasi Web. Ini akan meminta untuk memberikan akses ke BTCPay Server spesifik yang Anda kerjakan. Terima kondisi ini. BTCPay Server Vault sekarang akan mencari perangkat Keras. Setelah perangkat ditemukan, BTCPay Server akan mengenali bahwa Vault sedang berjalan dan telah mengambil perangkat Anda.

**!Catatan!**

Jangan memberikan kunci SSH atau akun admin server Anda kepada siapa pun selain administrator ketika menggunakan dompet panas. Siapa pun yang memiliki akses ke akun-akun ini akan memiliki akses ke dana dalam Dompet Panas.

### Ringkasan Keterampilan

Dalam bagian ini, Anda telah mempelajari hal-hal berikut:

- Tampilan transaksi dari dompet Bitcoin dan berbagai kategorisasinya.
- Berbagai opsi yang tersedia saat mengirim dari dompet Bitcoin, dari perangkat keras hingga dompet panas.
- Masalah batas celah yang dihadapi saat menggunakan sebagian besar dompet, dan cara mengatasinya.
- Cara menghasilkan dompet Bitcoin baru dalam BTCPay Server, termasuk menyimpan kunci dalam dompet perangkat keras dan mencadangkan frasa pemulihan.

Dalam tujuan ini, Anda telah belajar cara menghasilkan dompet Bitcoin baru dalam BTCPay Server. Kita belum membahas cara mengamankan atau menggunakan kunci-kunci tersebut. Dalam gambaran singkat tujuan ini, Anda telah belajar cara menyiapkan toko pertama. Anda telah belajar cara menghasilkan frasa Pemulihan Bitcoin.

### Penilaian Pengetahuan Praktis

Jelaskan metode untuk menghasilkan kunci dan skema untuk mengamankannya, bersama dengan trade-off/risiko dari skema keamanan tersebut.

## BTCPay Server Lightning Wallet

<chapterId>1bbece7e-0197-57e6-a93a-561cf384d946</chapterId>

Ketika seorang administrator server menyediakan instance BTCPay Server baru, dia dapat menyiapkan implementasi jaringan petir, LND, Core Lightning, atau Eclair; lihat Bagian Konfigurasi BTCPay Server untuk instruksi instalasi yang lebih rinci.
Jika diikuti oleh sebuah kelas, menghubungkan node Lightning ke BTCPay Server Anda dilakukan melalui node Kustom. Pengguna yang bukan administrator server pada BTCPay Server secara default tidak akan dapat menggunakan node Lightning internal. Ini untuk melindungi pemilik server dari kehilangan dana mereka. Administrator server dapat menginstal Plugin untuk memberikan akses ke node Lightning mereka melalui LNBank; ini di luar cakupan buku ini; baca lebih lanjut tentang LNBank di halaman plugin resmi.

### Menghubungkan node internal (administrator server)

Administrator Server dapat menggunakan Node Lightning internal BTCPay Server. Terlepas dari implementasi Lightning, cara menghubungkan ke node Lightning internal adalah sama.

Pergi ke toko yang telah disetup sebelumnya, dan klik pada dompet "Lightning" di menu kiri. BTCPay Server memberikan dua kemungkinan pengaturan, Menggunakan node internal (hanya admin Server secara default) atau node kustom (koneksi eksternal). Administrator server dapat mengklik opsi "Gunakan node internal". Tidak ada konfigurasi lebih lanjut yang diperlukan. Klik tombol "simpan" dan perhatikan notifikasi yang menyatakan, "BTC Lightning node diperbarui". Toko sekarang telah berhasil mendapatkan kemampuan jaringan Lightning.

### Menghubungkan node eksternal (pengguna server/pemilik toko)

Karena pemilik toko secara default tidak diizinkan menggunakan Node Lightning administrator server. Koneksi perlu dibuat ke node eksternal, baik node yang dimiliki oleh pemilik toko sebelum pengaturan BTCPay Server, plugin LNBank jika disediakan oleh administrator server, atau solusi kustodian seperti Alby.

Pergi ke toko yang telah disetup sebelumnya, dan klik "Lightning" di bawah dompet di menu kiri. Karena pemilik toko tidak diizinkan menggunakan node internal secara default, opsi ini digrayed out. Menggunakan node kustom adalah satu-satunya opsi yang secara default tersedia untuk pemilik toko.

BTCPay Server membutuhkan informasi koneksi; informasi spesifik untuk implementasi Lightning akan disampaikan oleh solusi yang dibuat sebelumnya (atau solusi kustodian). Dalam BTCPay Server, pemilik toko dapat menggunakan koneksi berikut;

- C-lightning via TCPorUnixdomainsocketconnection.
- Lightning Charge via HTTPS
- Eclair via HTTPS
- LND via proxy REST
- LNDhub via API REST

![image](assets/en/31.webp)

Klik "tes koneksi" untuk memastikan Anda memasukkan detail koneksi dengan benar. Setelah koneksi dikonfirmasi baik, klik simpan, dan BTCPay Server menunjukkan toko diperbarui dengan Node Lightning.

### Mengelola node Lightning internal LND (Administrator server)

Setelah menghubungkan Node Lightning internal, administrator server akan melihat ubin baru di Dashboard khusus untuk informasi Lightning.

- Saldo Lightning
- BTC di saluran
  - BTC membuka saluran
  - Saldo lokal BTC
  - Saldo jarak jauh BTC
  - BTC menutup saluran
- BTC On-chain
  - BTC dikonfirmasi
  - BTC belum dikonfirmasi
  - BTC dipesan
- Layanan Lightning
  - Ride the Lightning (RTL).

Dengan mengklik logo Ride the Lightning di ubin "Layanan Lightning" atau "Lightning" di bawah dompet di menu kiri, administrator server dapat mengakses RTL untuk manajemen node Lightning.

**Catatan!**

Menghubungkan Node Lightning internal gagal - Jika koneksi internal gagal, konfirmasi:

1. Node Bitcoin on-chain sepenuhnya tersinkronisasi
2. Node Lightning internal "Diaktifkan" di bawah "Lightning" > "Pengaturan" > "Pengaturan Lightning BTC"
   Jika Anda tidak dapat terhubung ke node Lightning Anda, coba restart server Anda, atau baca lebih lanjut di dokumentasi resmi BTCPay Server untuk detail lebih lanjut; https://docs.btcpayserver.org/Troubleshooting/ . Anda tidak dapat menerima pembayaran lightning di toko Anda sampai node Lightning Anda muncul sebagai "Online". Coba tes koneksi Lightning Anda dengan mengklik link "Informasi Node Publik".

### Dompet Lightning

Dalam opsi dompet Lightning di bilah menu kiri, administrator server akan menemukan akses mudah ke RTL, Informasi node Publik mereka, dan pengaturan Lightning khusus untuk toko BTCPay Server mereka.

#### Informasi node internal

Administrator server dapat mengklik informasi node internal dan melihat status server mereka (Online/ Offline) dan string koneksi untuk Clearnet atau Tor.

![image](assets/en/32.webp)

#### Ubah koneksi

Jika pemilik toko memutuskan untuk menggunakan perubahan dalam Pengaturan Lightning - Ubah koneksi.
Di sebelah informasi Node Publik toko, pemilik dapat menemukan opsi ini. Ini akan mengembalikan pengaturan awal untuk koneksi node lightning eksternal, isi informasi node Lightning baru, klik simpan, dan perbarui toko dengan informasi node baru.

![image](assets/en/33.webp)

#### Layanan

Jika administrator server memutuskan untuk menginstal beberapa layanan untuk implementasi Lightning, mereka akan terdaftar di sini. Dengan implementasi LND standar, administrator akan memiliki Ride The Lightning (RTL) sebagai alat standar untuk manajemen node.

#### Pengaturan dompet BTC Lightning

Setelah menambahkan node Lightning ke toko dalam langkah sebelumnya, dalam pengaturan dompet Lightning, pemilik toko masih dapat memilih untuk menonaktifkannya untuk toko mereka dengan menggunakan Toggle di bagian atas pengaturan Lightning.

![image](assets/en/34.webp)

#### Opsi Pembayaran Lightning

Pemilik toko dapat menetapkan parameter berikut untuk meningkatkan pengalaman Lightning bagi pelanggan mereka.

- Tampilkan jumlah pembayaran Lightning dalam Satoshis.
- Tambahkan petunjuk hop untuk saluran pribadi ke faktur Lightning.
- Seragamkan URL/QR code pembayaran on-chain dan Lightning saat checkout.
- Tetapkan template deskripsi untuk faktur lightning.

#### LNURL

Pemilik toko dapat memilih untuk menggunakan atau tidak menggunakan LNURL. URL Jaringan Lightning, atau LNURL, adalah standar yang diusulkan untuk interaksi antara Pembayar Lightning dan penerima pembayaran. Singkatnya, LNURL adalah url yang dikodekan bech32 dengan awalan lnurl. Dompet Lightning diharapkan untuk mendekode URL, menghubungi URL, dan menunggu objek JSON dengan instruksi lebih lanjut, terutama tag yang mendefinisikan perilaku lnurl.

- Aktifkan LNURL
- Mode Klasik LNURL
  - Untuk kompatibilitas dompet, Bech32 dikodekan (klasik) vs URL teks biasa (mendatang)
- Izinkan penerima pembayaran untuk memberikan komentar.

### Contoh 1

#### Terhubung ke Lightning dengan node internal (Administrator)

Opsi ini hanya tersedia jika Anda adalah Administrator dari instansi ini atau jika Administrator telah mengubah pengaturan default di mana pengguna dapat menggunakan node lightning internal.

Sebagai administrator, klik pada Dompet Lightning di bilah menu kiri. BTCPay Server akan meminta untuk menggunakan salah satu dari dua opsi untuk menghubungkan Node Lightning, node Internal atau node eksternal kustom. Klik pada Gunakan node internal dan klik simpan.

#### Mengelola node Lightning Anda (RTL)

Setelah terhubung ke node lightning internal, BTCPay Server akan memperbarui dan menampilkan notifikasi "BTC Lightning node diperbarui", mengonfirmasi Anda sekarang telah menghubungkan Lightning ke toko Anda.

Mengelola node lightning adalah tugas untuk Administrator server. Ini melibatkan.

- Mengelola transaksi
- Mengelola likuiditas
  - Likuiditas masuk
  - Likuiditas keluar
- Mengelola rekan dan saluran
  - Rekan yang terhubung
  - Biaya saluran
  - Status saluran
- Melakukan backup rutin terhadap status kanal.
- Memeriksa laporan routing.
- Sebagai alternatif, gunakan layanan seperti Loop.

Semua pengelolaan node Lightning dilakukan secara standar dengan RTL (dengan asumsi Anda menjalankan implementasi LND). Administrator dapat mengklik Lightning Wallet mereka di BTCPay Server dan menemukan tombol untuk membuka RTL. Dashboard utama BTCPay Server kini diperbarui dengan Lightning Network Tiles, termasuk akses cepat ke RTL.

### Contoh 2

#### Terhubung ke lightning dengan Alby

Saat terhubung dengan custodian seperti Alby, pemilik toko harus pertama-tama membuat akun, kunjungi: https://getalby.com/

![gambar](assets/en/35.webp)

Setelah membuat akun Alby, pergi ke toko BTCPay Server Anda.

Langkah 1: Klik 'Set up a Lightning node' di Dashboard atau 'Lightning' di bawah wallets.

![gambar](assets/en/36.webp)

Langkah 2: Masukkan kredensial koneksi Wallet Anda yang disediakan oleh Alby. Di Dashboard Alby, klik pada Wallet. Di sini Anda akan menemukan "Wallet Connection Credentials". Salin kredensial ini. Tempelkan kredensial dari Alby ke dalam bidang Konfigurasi Koneksi di BTCPay Server.

![gambar](assets/en/37.webp)

Langkah 3: Setelah memberikan BTCPay Server dengan detail Koneksi, klik tombol "Test Connection" untuk memastikan koneksi berfungsi dengan baik. Perhatikan pesan "Connection to lightning node successful" di bagian atas layar Anda. Ini mengonfirmasi bahwa semuanya berfungsi dengan baik.

![gambar](assets/en/38.webp)

Langkah 4: Klik simpan, dan toko Anda sekarang terhubung dengan node lightning oleh Alby.

![gambar](assets/en/39.webp)

**!Catatan!**

Jangan pernah mempercayai solusi Lightning custodian untuk nilai lebih dari yang Anda bersedia kehilangan.

### Ringkasan Keterampilan

Di bagian ini Anda belajar:

- Cara menghubungkan node Lightning internal atau eksternal
- Isi dan fungsi berbagai ubin terkait Lightning di Dashboard
- Cara mengonfigurasi dompet Lightning menggunakan Voltage Surge atau Alby

### Penilaian Pengetahuan Praktis

Jelaskan beberapa opsi berbeda untuk menghubungkan dompet Lightning ke toko Anda.

# Antarmuka BTCPay Server

<partId>25e88b81-e1ab-515f-a035-09f2a3075556</partId>

## Ikhtisar Dashboard

<chapterId>410ff28b-a272-5c91-93e0-48d5b28c53ab</chapterId>

BTCPay Server adalah paket perangkat lunak modular. Namun, ada standar yang setiap BTCPay Server akan memiliki dan Administrator/pengguna akan berinteraksi dengan. Mulai dengan Dashboard. Titik masuk utama setiap BTCPay Server setelah masuk. Dashboard memberikan gambaran umum tentang bagaimana toko Anda berkinerja, saldo dompet saat ini, dan tx terakhir dalam 7 hari terakhir. Karena ini adalah tampilan modular, Plugin dapat memanfaatkan tampilan ini untuk keuntungan mereka dan membuat ubin mereka di Dashboard. Untuk buku kursus ini, kami hanya akan membahas tentang plugin/aplikasi standar dan tampilan masing-masing di seluruh BTCPay Server.

### Ubin Dashboard

Dalam tampilan utama dashboard BTCPay Server terdapat beberapa ubin standar yang tersedia. Ubin-ubin ini dimaksudkan untuk Pemilik toko atau Administrator untuk mengelola tokonya secara cepat dalam satu gambaran umum.

- Saldo dompet
- Aktivitas transaksi
- Saldo Lightning (jika Lightning diaktifkan di toko)
- Layanan Lightning (jika Lightning diaktifkan di toko)
- Transaksi terbaru.
- Faktur terbaru
- Crowdfunds aktif saat ini
- Kinerja toko / item terlaris.
  Tile Saldo Dompet memberikan gambaran cepat tentang dana dan kinerja dompet Anda. Ini dapat dilihat dalam BTC atau mata uang Fiat dalam grafik Mingguan, bulanan, atau tahunan.
  ![image](assets/en/40.webp)

### Aktivitas Transaksi

Di sebelah Tile Saldo Dompet, BTCPay Server menampilkan gambaran cepat tentang Pembayaran yang tertunda, jumlah Transaksi dalam 7 hari terakhir, dan apakah toko Anda telah mengeluarkan pengembalian dana. Mengklik tombol Kelola membawa Anda ke pengelolaan untuk pembayaran yang tertunda (pelajari lebih lanjut tentang pembayaran di BTCPay Server - Bab Pembayaran).

![image](assets/en/41.webp)

### Saldo Lightning

Ini hanya terlihat ketika Lightning diaktifkan.

Ketika Administrator telah mengizinkan akses jaringan Lightning, dasbor BTCPay Server sekarang memiliki tile baru dengan informasi node Lightning Anda. Berapa banyak BTC dalam saluran, bagaimana ini seimbang lokal atau remote (likuiditas masuk atau keluar) jika saluran sedang menutup atau membuka, dan berapa banyak bitcoin yang dipegang on-chain pada node lightning.

![image](assets/en/42.webp)

### Layanan Lightning

Ini hanya terlihat ketika lightning aktif.

Di sebelah melihat saldo Lightning Anda di dasbor BTCPay Server, administrator juga akan melihat tile untuk Layanan Lightning. Di sini administrator dapat menemukan tombol cepat untuk alat yang mereka gunakan untuk mengelola node Lightning mereka; misalnya, Ride the Lightning adalah salah satu alat standar dengan BTCPay Server untuk pengelolaan node Lightning.

![image](assets/en/43.webp)

### Transaksi Terkini

Tile transaksi terkini akan menampilkan transaksi terbaru toko Anda. Dengan satu klik, Administrator dari instansi BTCPay Server sekarang dapat melihat transaksi terbaru dan melihat apakah perhatian diperlukan terhadapnya.

![image](assets/en/44.webp)

### Faktur Terkini

Tile faktur terkini menunjukkan 6 faktur terbaru yang dihasilkan oleh BTCPay Server Anda, termasuk Status dan jumlah faktur. Tile juga mencakup tombol "Lihat semua" untuk mengakses gambaran Faktur secara lengkap dengan mudah.

![image](assets/en/45.webp)

### Point Of Sale dan Crowdfunds

Karena BTCPay Server menyediakan serangkaian plugin atau aplikasi standar, Point Of Sale dan Crowdfund adalah dua plugin utama dari BTCPay Server. Dengan setiap toko dan dompet, pengguna BTCPay Server dapat menghasilkan sebanyak mungkin Point Of Sales atau Crowdfunds sesuai keinginannya. Masing-masing akan membuat tile dasbor baru yang menunjukkan kinerja plugin.

![image](assets/en/46.webp)

Perhatikan perbedaan kecil antara tile Point of Sale dan Crowdfund. Administrator melihat item teratas yang terjual di tile Point of Sales. Di tile Crowdfund, ini menjadi Top Perks. Kedua tile memiliki tombol cepat untuk mengelola aplikasi yang bersangkutan dan melihat faktur terbaru yang dibuat oleh item teratas atau top perks.

![image](assets/en/47.webp)

**!?Catatan!?**

Grafik saldo dan transaksi terkini hanya tersedia untuk metode pembayaran on-chain. Informasi tentang saldo dan transaksi Jaringan Lightning ada dalam daftar tugas. Sejak Versi BTCPay Server 1.6.0, saldo Jaringan Lightning dasar tersedia.

### Ringkasan Keterampilan

Dalam bagian ini, Anda mempelajari hal-hal berikut:

- Tata letak inti dari tile pada halaman utama yang dikenal sebagai Dasbor.
- Pemahaman dasar tentang isi dari setiap tile.

### Ulasan Penilaian Pengetahuan

Daftar sebanyak mungkin tile dari Dasbor dari ingatan Anda.

## BTCPay Server - Pengaturan Toko

<chapterId>e8faef7b-278d-550e-a511-bc3a442daf64</chapterId>
Dalam perangkat lunak BTCPay Server, kita mengenal 2 jenis pengaturan. Pengaturan spesifik Toko BTCPay Server, tombol pengaturan yang ditemukan di bilah menu kiri di bawah Dashboard, dan pengaturan BTCPay Server, yang ditemukan di bagian bawah bilah menu tepat di atas Akun. Pengaturan spesifik Server BTCPay Server hanya dapat dilihat oleh administrator Server.
Pengaturan toko terdiri dari banyak tab untuk mengkategorikan setiap setelan pengaturan.

- Umum
- Tarif
- Tampilan Pembayaran
- Token Akses
- Pengguna
- Peran
- Webhooks
- Prosesor Pembayaran
- Email
- Formulir

### Umum

Di tab Pengaturan Umum, pemilik toko menetapkan branding dan pembayaran default mereka. Pada pengaturan awal toko, sebuah nama toko diberikan; ini akan tercermin dalam pengaturan Umum di bawah Nama Toko. Di sini pemilik toko juga dapat menetapkan situs web mereka untuk mencocokkan branding dan ID Toko untuk Administrator mengenali dalam database.

#### Branding

Karena BTCPay Server adalah FOSS, pemilik toko dapat melakukan branding kustom untuk mencocokkan toko mereka. Tetapkan warna brand, simpan logo brand Anda, dan tambahkan CSS kustom untuk halaman yang menghadap ke publik/pelanggan (Faktur, Permintaan Pembayaran, Pembayaran Tarik)

#### Pembayaran

Dalam pengaturan pembayaran, pemilik toko mendapatkan untuk menetapkan mata uang default toko mereka (baik dalam Bitcoin atau dalam mata uang fiat apa pun).

#### Izinkan siapa pun untuk membuat faktur

Pengaturan ini dimaksudkan untuk pengembang atau pembangun di atas BTCPay Server. Dengan pengaturan ini diaktifkan untuk toko Anda, ini memungkinkan dunia luar untuk membuat faktur pada instansi BTCPay Server Anda.

#### Tambahkan biaya tambahan (biaya jaringan) ke faktur

Fitur dalam BTCPay untuk melindungi pedagang dari serangan debu atau klien untuk mendorong biaya tinggi nanti ketika pedagang perlu memindahkan banyak bitcoin sekaligus. Misalnya, pelanggan membuat faktur sebesar 20$ dan membayarnya sebagian, membayar 1$ 20 kali sampai faktur tersebut sepenuhnya dibayar. Pedagang sekarang memiliki transaksi yang lebih besar, meningkatkan biaya penambangan jika pedagang memutuskan untuk memindahkan dana tersebut nanti. Secara default, BTCPay menerapkan biaya jaringan tambahan ke jumlah total faktur untuk menutupi pengeluaran tersebut untuk pedagang ketika faktur dibayar dalam beberapa transaksi. BTCPay menawarkan beberapa opsi untuk menyesuaikan fitur perlindungan ini. Anda dapat menerapkan biaya jaringan:

- Hanya jika pelanggan melakukan lebih dari satu pembayaran untuk faktur (Dalam contoh di atas, jika pelanggan membuat faktur sebesar 20\$ dan membayar 1\$, total tagihan yang harus dibayar sekarang adalah 19\$ + biaya jaringan. Biaya jaringan diterapkan setelah pembayaran pertama)
- Pada setiap pembayaran (termasuk pembayaran pertama, dalam contoh kita, totalnya akan menjadi 20\$ + biaya jaringan segera, bahkan pada pembayaran pertama)
- Jangan pernah menambahkan biaya jaringan (menonaktifkan biaya jaringan sepenuhnya)

Meskipun melindungi dari transaksi debu, ini juga dapat mencerminkan negatif pada bisnis jika tidak dikomunikasikan dengan benar. Pelanggan mungkin memiliki pertanyaan tambahan dan berpikir Anda menagih mereka terlalu banyak.

#### Faktur kedaluwarsa jika jumlah penuh tidak dibayar setelah?

Timer faktur diatur menjadi 15 menit secara default. Timer adalah mekanisme perlindungan terhadap volatilitas karena mengunci jumlah Bitcoin sesuai dengan tarif Bitcoin ke fiat. Jika pelanggan tidak membayar faktur dalam periode yang ditentukan, faktur dianggap kedaluwarsa. Faktur dianggap "dibayar" segera setelah transaksi terlihat di blockchain (0-konfirmasi) tetapi dianggap "lengkap" ketika mencapai jumlah konfirmasi yang ditentukan pedagang (biasanya, 1-6). Timer dapat disesuaikan menurut menit.

#### Pertimbangkan faktur dibayar meskipun jumlah yang dibayar X% kurang dari yang diharapkan?

Ketika seorang pelanggan menggunakan dompet pertukaran untuk membayar langsung sebuah faktur, pertukaran tersebut mengambil biaya kecil. Ini berarti bahwa faktur tersebut tidak dianggap sepenuhnya selesai. Faktur tersebut mendapatkan status "dibayar sebagian". Anda dapat menetapkan tingkat persentase di sini jika seorang pedagang ingin menerima faktur yang dibayar kurang.

### Tarif

Di BTCPay Server, ketika sebuah faktur dihasilkan, selalu membutuhkan harga Bitcoin ke fiat yang paling mutakhir dan akurat. Ketika membuat toko baru di BTCPay Server, administrator diminta untuk menetapkan sumber harga yang mereka inginkan; setelah toko diatur, pemilik toko selalu dapat mengubah sumber harga mereka di tab ini.

#### Skrip aturan tarif lanjutan

Umumnya digunakan oleh pengguna berpengalaman. Jika diaktifkan, pemilik toko dapat membuat skrip seputar perilaku harga dan bagaimana menagih pelanggan mereka.

#### Pengujian

Tempat pengujian cepat untuk pasangan mata uang yang Anda inginkan. Ini juga termasuk fitur untuk memeriksa pasangan mata uang default melalui kueri REST.

### Tampilan Pembayaran

Tab Tampilan Pembayaran dimulai dengan pengaturan spesifik faktur dan metode pembayaran default dan mengaktifkan metode pembayaran spesifik ketika persyaratan yang ditetapkan terpenuhi.

#### Pengaturan Faktur

Metode pembayaran default. BTCPay Server dalam konfigurasi standar memiliki tiga opsi.

- BTC (on-chain)
- BTC (LNURL-pay)
- BTC (Off-chain & Lightning)

Kita dapat menetapkan parameter untuk toko kita, di mana pelanggan hanya akan berinteraksi dengan Lightning ketika harga kurang dari jumlah X dan sebaliknya untuk transaksi On-chain ketika X lebih besar dari Y selalu menampilkan opsi pembayaran On-chain.

![image](assets/en/48.webp)

#### Pembayaran

Sejak rilis BTCPay Server 1.7, diperkenalkan antarmuka Pembayaran baru, Checkout V2, seperti yang disebut. Sejak rilis 1.9 distandarisasi, administrator dan pemilik toko masih dapat mengatur pembayaran ke rilis sebelumnya. Dengan menggunakan tombol "Gunakan pembayaran klasik", pemilik toko dapat mengatur toko kembali ke pengalaman pembayaran sebelumnya. BTCPay Server juga memiliki setelan preset terpilih untuk perdagangan Online atau pengalaman di toko.

![image](assets/en/49.webp)

Ketika pelanggan berinteraksi dengan toko dan menghasilkan faktur, ada waktu kedaluwarsa untuk faktur tersebut. Secara default BTCPay Server menetapkannya menjadi 5 menit, dan Administrator dapat menetapkannya menjadi apa pun yang mereka anggap cocok. Halaman pembayaran dapat lebih disesuaikan dengan memeriksa parameter berikut:

- Merayakan pembayaran dengan menampilkan konfeti
- Menampilkan header toko (Nama dan logo)
- Menampilkan tombol "Bayar di dompet"
- Menyatukan URL/QR pembayaran on-chain dan off-chain
- Menampilkan jumlah pembayaran Lightning dalam Satoshis
- Mendeteksi bahasa secara otomatis pada pembayaran

![image](assets/en/50.webp)

Ketika Mendeteksi Bahasa secara otomatis tidak diatur, BTCPay Server, secara default, akan menampilkan Bahasa Inggris. Pemilik toko dapat mengubah default ini ke bahasa yang mereka inginkan.

![image](assets/en/51.webp)

Klik pada Drop down dan Pemilik toko dapat menetapkan Judul HTML Kustom untuk ditampilkan di halaman pembayaran.

![image](assets/en/52.webp)

Untuk memastikan pelanggan mengetahui metode pembayarannya, pemilik toko dapat secara eksplisit menetapkan pembayaran mereka selalu untuk meminta pengguna memilih metode pembayaran yang mereka inginkan. Ketika faktur dibayar, BTCPay Server memungkinkan pelanggan untuk kembali ke webshop. Pemilik toko dapat menetapkan pengalihan ini setelah pelanggan membayar secara otomatis.

![image](assets/en/53.webp)

#### Tanda Terima Publik

Dalam pengaturan tanda terima publik, pemilik toko dapat menetapkan halaman tanda terima ke publik dan menampilkan daftar pembayaran di halaman tanda terima dan kode QR dari tanda terima agar pelanggan dapat dengan mudah mengaksesnya secara digital.

### Token Akses

Token akses digunakan untuk penggabungan dengan integrasi e-commerce tertentu atau integrasi kustom yang dibangun.

### Pengguna

Pengguna toko adalah tempat pemilik toko dapat mengelola anggota stafnya, akun mereka, dan akses ke toko. Setelah anggota staf membuat akun mereka, pemilik toko dapat menambahkan pengguna tertentu ke toko sebagai Pengguna Tamu atau pemilik. Untuk lebih mendefinisikan peran staf, lihat bagian selanjutnya tentang "Pengaturan Toko BTCPay Server - Peran."

### Peran

Seorang pemilik toko mungkin tidak merasa peran standar pengguna cukup signifikan. Dalam pengaturan peran kustom, pemilik toko dapat mendefinisikan kebutuhan spesifik untuk setiap peran dalam bisnisnya.

(1) Untuk membuat peran baru, klik tombol "+ Tambah peran".

(2) Masukkan nama Peran, misalnya, "Kasir".

(3) Konfigurasikan izin individu untuk peran tersebut.

- Modifikasi toko Anda.
- Kelola akun pertukaran yang terhubung dengan toko Anda.
  - Lihat akun pertukaran yang terhubung dengan toko Anda.
- Kelola pembayaran tarik Anda.
- Buat pembayaran tarik.
  - Buat pembayaran tarik yang tidak disetujui.
- Modifikasi faktur.
  - Lihat faktur.
  - Buat faktur.
  - Buat faktur dari node petir yang terkait dengan toko Anda.
- Lihat toko Anda.
  - Lihat faktur.
  - Lihat permintaan pembayaran Anda.
  - Modifikasi webhook toko.
- Modifikasi permintaan pembayaran Anda.
  - Lihat permintaan pembayaran Anda.
- Gunakan node petir yang terkait dengan toko Anda.
  - Lihat faktur petir yang terkait dengan toko Anda.
  - Buat faktur dari node petir yang terkait dengan toko Anda.
- Setor dana ke akun pertukaran yang terhubung dengan toko Anda.
- Tarik dana dari akun pertukaran ke toko Anda.
- Perdagangkan dana pada akun pertukaran toko Anda.

Ketika peran telah dibuat, nama tersebut tetap dan tidak dapat diubah setelahnya dalam mode edit.

### Webhook

Dalam BTCPay Server, cukup mudah untuk membuat "Webhook" baru. Di tab Pengaturan Toko BTCPay Server - Webhook, pemilik toko dapat dengan mudah membuat webhook baru dengan mengklik "+ Buat Webhook". Webhook memungkinkan BTCPay Server untuk mengirimkan event HTTP yang terkait dengan toko Anda ke server lain atau integrasi e-commerce.

Anda sekarang berada dalam tampilan untuk membuat Webhook. Pastikan Anda mengetahui URL Payload Anda dan tempelkan ini ke BTCPay Server Anda. Sementara Anda menempelkan URL Payload, di bawahnya menunjukkan rahasia webhook. Salin rahasia webhook dan berikan pada endpoint. Ketika semuanya telah diatur, Anda dapat mengaktifkan di BTCPay Server untuk Pengiriman Ulang Otomatis. Kami akan mencoba mengirim ulang setiap pengiriman yang gagal setelah 10 detik, 1 menit, dan hingga 6 kali setelah 10 menit. Anda dapat beralih antara setiap event atau menentukan event untuk kebutuhan Anda. Pastikan untuk mengaktifkan webhook dan tekan Tambah webhook untuk menyimpannya.

Webhook tidak dimaksudkan untuk kompatibel dengan API Bitpay. Ada dua IPN terpisah (dalam istilah BitPay: "Pemberitahuan Pembayaran Instan") di BTCPay Server.

- Webhook
- Notifikasi

Hanya gunakan URL Notifikasi ketika Anda membuat faktur melalui api Bitpay.

### Proses Pembayaran

Prosesor pembayaran bekerja bersama dengan konsep Pembayaran di BTCPay Server. Sebuah agregator pembayaran untuk menggabungkan beberapa transaksi dan mengirimkannya sekaligus. Dengan prosesor pembayaran, pemilik toko dapat mengotomatiskan pembayaran yang digabungkan. BTCPay Server menyediakan dua metode pembayaran otomatis, On-chain dan Off-chain (LN).
Pemilik toko dapat mengklik dan mengonfigurasi kedua prosesor pembayaran secara terpisah. Seorang pemilik toko mungkin hanya ingin menjalankan prosesor on-chain setiap X jam, sedangkan off-chain mungkin berjalan setiap beberapa menit. Untuk On-chain, Anda juga dapat menetapkan target untuk blok mana harus dimasukkan. Secara default, ini diatur ke 1 (atau blok berikutnya yang tersedia). Perhatikan bahwa pengaturan prosesor pembayaran Off-chain hanya memiliki timer interval dan tidak ada target blok. Pembayaran jaringan Lightning adalah instan.

![image](assets/en/62.webp)
![image](assets/en/63.webp)

Pemilik toko hanya dapat mengonfigurasi prosesor on-chain jika mereka memiliki Hot-wallet yang terhubung ke toko mereka.

![image](assets/en/64.webp)

Setelah mengatur Prosesor Pembayaran, Anda dapat dengan cepat menghapus atau memodifikasinya dengan kembali ke tab Prosesor Pembayaran di pengaturan Toko BTCPay Server.

**!?Catatan!?**

Prosesor pembayaran on-chain - Prosesor pembayaran onchain hanya dapat bekerja pada toko yang dikonfigurasi dengan Hot wallet yang terhubung. Jika tidak ada hot wallet yang terhubung, BTCPay Server tidak memegang kunci dompet dan tidak akan dapat memproses pembayaran secara otomatis.

### Email

BTCPay Server dapat menggunakan Email untuk Notifikasi atau, ketika diatur dengan benar, untuk memulihkan akun yang dibuat pada instansinya, sebagai standar BTCPay Server tidak mengirim email ketika kata sandi hilang, misalnya.

![image](assets/en/65.webp)

Sebelum pemilik toko dapat menetapkan Aturan Email untuk memicu pada event tertentu dari tokonya, kita harus mengatur beberapa pengaturan email dasar. BTCPay Server memerlukan pengaturan ini untuk mengirim email untuk event berdasarkan toko Anda atau untuk reset kata sandi.

BTCPay Server mempermudah mengisi informasi ini dengan menggunakan Opsi "Isi Cepat":

- Gmail.com
- Yahoo.com
- Mailgun
- Office365
- SendGrid

Dengan menggunakan opsi isi cepat, BTCPay Server akan mengisi otomatis bidang untuk server SMTP dan port; sekarang, pemilik toko hanya perlu mengisi kredensialnya dalam alamat Email, Login (yang biasanya sama dengan alamat email Anda), dan kata sandi Anda. Opsi lanjutan yang BTCPay Server tawarkan dalam pengaturan email adalah untuk Menonaktifkan pemeriksaan keamanan Sertifikat TLS; secara default, ini Diaktifkan.

![image](assets/en/66.webp)

Dengan Aturan Email, pemilik toko dapat menetapkan event tertentu untuk memicu email ke alamat email tertentu.

- Invoice Dibuat
- Invoice Menerima Pembayaran
- Invoice Sedang Diproses
- Invoice Kedaluwarsa
- Invoice Diselesaikan
- Invoice Tidak Valid
- Pembayaran Invoice Diselesaikan

Jika pelanggan telah menyediakan alamat Email, pemicu ini juga dapat mengirim informasi ke pelanggan. Pemilik toko dapat mengisi terlebih dahulu baris Subjek untuk menjelaskan mengapa Email ini terjadi dan apa pemicunya.

![image](assets/en/67.webp)

### Formulir

Karena BTCPay Server tidak mengumpulkan data apa pun, pemilik toko mungkin ingin menambahkan formulir kustom ke pengalaman checkout mereka; dengan cara ini, pemilik toko dapat mengumpulkan informasi tambahan dari pelanggannya. Pembuat Formulir BTCPay Server terdiri dari dua bagian, tampilan visual dan tampilan kode yang lebih lanjutan dari formulir.
Saat membuat formulir baru, BTCPay Server membuka jendela baru yang meminta informasi dasar tentang apa yang Anda inginkan dari formulir baru Anda. Pertama-tama, pemilik toko perlu memberikan nama yang jelas untuk formulir baru mereka, nama ini TIDAK dapat diubah setelah diatur.
![image](assets/en/68.webp)

Setelah pemilik toko memberikan nama pada formulir, Anda juga dapat mengaktifkan tombol "Izinkan formulir untuk penggunaan publik" menjadi ON, dan ini akan berubah menjadi hijau. Ini agar formulir dapat digunakan di setiap tempat yang menghadap pelanggan. Sebagai contoh, jika pemilik toko membuat 1 faktur terpisah tidak melalui Point Of Sale-nya, dia mungkin masih ingin mengumpulkan info dari pelanggan; pengaktifan tombol ini ke ON memungkinkan info tersebut untuk dikumpulkan.

![image](assets/en/69.webp)

Setiap formulir dimulai dengan setidaknya 1 Bidang formulir baru. Pemilik toko dapat memilih jenis bidang apa yang harusnya;

- Teks
- Angka
- Kata Sandi
- Email
- URL
- Nomor Telepon
- Tanggal
- Bidang Tersembunyi
- Fieldset
- Area teks untuk komentar terbuka.
- Pemilih Opsi

Setiap tipe datang dengan parameter yang harus diisi. Pemilik toko dapat menyetelnya sesuai keinginan. Di bawah bidang yang pertama kali dibuat, pemilik toko dapat terus menambahkan bidang baru ke formulir ini.

![image](assets/en/70.webp)

#### Formulir kustom lanjutan

BTCPay Server juga memungkinkan Anda untuk membangun Formulir dalam kode. JSON, khususnya. Alih-alih melihat editor, pemilik toko dapat mengklik tombol KODE tepat di sebelah editor dan masuk ke dalam kode Formulir mereka. Dalam definisi bidang, hanya bidang berikut yang dapat diatur; nilai dari bidang disimpan dalam metadata dari faktur:

| Bidang                | Deskripsi                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| .fields.constant      | Jika benar, .value harus diatur dalam definisi formulir, dan pengguna tidak akan dapat mengubah nilai bidang. (contoh: versi definisi formulir)                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| .fields.type          | Tipe input HTML teks, radio, kotak centang, kata sandi, tersembunyi, tombol, warna, tanggal, datetime-local, bulan, minggu, waktu, email, angka, rentang, pencarian, url, pilih, tel                                                                                                                                                                                                                                                                                                                                                                                                     |
| .fields.options       | Jika .fields.type adalah select, daftar nilai yang dapat dipilih                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| .fields.options.text  | Teks yang ditampilkan untuk opsi ini                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| .fields.options.value | Nilai dari bidang jika opsi ini dipilih                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| .fields.type=fieldset | Membuat fieldset HTML di sekitar anak-anak .fields.fields (lihat di bawah)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| .fields.name          | Nama properti JSON dari bidang seperti yang akan muncul dalam metadata faktur                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| .fields.value         | Nilai default dari bidang                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| .fields.required      | jika benar, bidang akan diperlukan                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| .fields.label         | Label dari bidang                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| .fields.helpText      | Teks tambahan untuk memberikan penjelasan untuk bidang.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| .fields.fields        | Anda dapat mengorganisir bidang Anda dalam sebuah hierarki, memungkinkan bidang anak untuk ditempatkan di dalam metadata invoice. Struktur ini dapat membantu Anda mengorganisir dan mengelola informasi yang dikumpulkan dengan lebih baik, membuatnya lebih mudah untuk diakses dan diinterpretasikan. Sebagai contoh, jika Anda memiliki formulir yang mengumpulkan informasi pelanggan, Anda dapat mengelompokkan bidang-bidang tersebut di bawah bidang induk yang disebut pelanggan. Di dalam bidang induk ini, Anda mungkin memiliki bidang anak seperti nama, Email, dan alamat. |

Nama bidang mewakili nama properti JSON yang menyimpan nilai yang diberikan pengguna dalam metadata invoice. Beberapa nama yang dikenal dapat diinterpretasikan dan mengubah pengaturan invoice.

| Nama Bidang      | Deskripsi         |
| ---------------- | ----------------- |
| invoice_amount   | Jumlah invoice    |
| invoice_currency | Mata uang invoice |

Anda dapat mengisi bidang-bidang pada sebuah invoice secara otomatis dengan menambahkan string kueri ke URL formulir, seperti "?your_field=nilai".

Berikut adalah beberapa kasus penggunaan untuk fitur ini:

- Membantu input pengguna: Isi bidang secara otomatis dengan informasi pelanggan yang diketahui untuk memudahkan mereka dalam menyelesaikan formulir. Sebagai contoh, jika Anda sudah mengetahui alamat email pelanggan, Anda dapat mengisi bidang email secara otomatis untuk menghemat waktu mereka.
- Personalisasi: Sesuaikan formulir berdasarkan preferensi atau segmentasi pelanggan. Misalnya, jika Anda memiliki berbagai tingkatan pelanggan, Anda dapat mengisi formulir dengan data yang relevan, seperti tingkat keanggotaan mereka atau penawaran khusus.
- Pelacakan: Lacak sumber kunjungan pelanggan menggunakan bidang tersembunyi dan nilai yang diisi sebelumnya. Sebagai contoh, Anda dapat membuat tautan dengan nilai utm_media yang diisi sebelumnya untuk setiap saluran pemasaran (misalnya, Twitter, Facebook, Email). Ini membantu Anda menganalisis efektivitas upaya pemasaran Anda.
- Pengujian A/B: Isi bidang dengan nilai yang berbeda untuk menguji versi formulir yang berbeda, memungkinkan Anda untuk mengoptimalkan pengalaman pengguna dan tingkat konversi.

### Ringkasan Keterampilan

Di bagian ini, Anda telah mempelajari hal-hal berikut:

- Tata letak dan fungsi tab dalam Pengaturan Toko
- Berbagai pilihan untuk menyesuaikan penanganan nilai tukar yang mendasari, pembayaran sebagian, pembayaran kurang, dan lainnya.
- Sesuaikan tampilan checkout, termasuk pengaktifan rantai utama vs. Lightning tergantung harga pada invoice.
- Mengelola tingkat akses dan izin toko di berbagai peran.
- Mengonfigurasi email otomatis dan pemicunya
- Membuat formulir kustom untuk mengumpulkan informasi pelanggan tambahan saat checkout.

### Penilaian Pengetahuan

#### Ulasan KA

Apa perbedaan antara Pengaturan Toko dan Pengaturan Server?

#### Hipotetis KA

Jelaskan beberapa opsi yang mungkin Anda pilih dalam Tampilan Checkout > Pengaturan Invoice, dan mengapa.

## BTCPay Server - Pengaturan Server

<chapterId>1dd858a2-49ea-586b-9bc1-75a65f508df6</chapterId>

BTCPay Server terdiri dari dua tampilan pengaturan yang berbeda. Satu ditujukan untuk Pengaturan Toko dan yang lainnya untuk Pengaturan Server. Yang terakhir hanya tersedia jika Anda adalah Administrator Server dan tidak untuk pemilik toko. Administrator Server dapat menambahkan pengguna, membuat peran kustom, mengonfigurasi server email, menetapkan kebijakan, menjalankan tugas pemeliharaan, memeriksa semua layanan yang terhubung ke BTCPay Server, mengunggah file ke server, atau memeriksa Log.

### Pengguna

Seperti disebutkan di bagian sebelumnya, Administrator Server dapat mengundang pengguna ke server mereka dengan menambahkannya ke tab Pengguna.

### Peran Kustom Seluruh Server

BTCPay Server mengenal dua jenis peran kustom, peran kustom spesifik toko dan Peran Kustom Seluruh Server dalam pengaturan BTCPay Server. Keduanya memiliki set izin yang serupa; namun, jika ditetapkan melalui Pengaturan BTCPay Server - tab Peran, peran yang diterapkan akan bersifat seluruh server dan berlaku untuk beberapa toko. Perhatikan tag "Seluruh Server" pada peran kustom dalam pengaturan Server.

### Peran Kustom Seluruh Server

Set izin peran kustom seluruh server;

- Modifikasi toko Anda.
- Kelola akun pertukaran yang terhubung dengan toko Anda.
  - Lihat akun pertukaran yang terhubung dengan toko Anda.
- Kelola pembayaran tarik Anda.
- Buat pembayaran tarik.
  - Buat pembayaran tarik yang tidak disetujui.
- Modifikasi faktur.
  - Lihat faktur.
  - Buat faktur.
  - Buat faktur dari node lightning yang terkait dengan toko Anda.
- Lihat toko Anda.
  - Lihat faktur.
  - Lihat permintaan pembayaran Anda.
  - Modifikasi webhook toko.
- Modifikasi permintaan pembayaran Anda.
  - Lihat permintaan pembayaran Anda.
- Gunakan node lightning yang terkait dengan toko Anda.
  - Lihat faktur lightning yang terkait dengan toko Anda.
  - Buat faktur dari node lightning yang terkait dengan toko Anda.
- Deposit dana ke akun pertukaran yang terhubung dengan toko Anda.
- Tarik dana dari akun pertukaran ke toko Anda.
- Perdagangkan dana pada akun pertukaran toko Anda.

**!?Catatan!?**

Ketika peran dibuat, nama ditetapkan dan tidak dapat diubah setelahnya dalam mode edit.

### Email

Pengaturan Email Seluruh Server terlihat mirip dengan pengaturan email spesifik toko. Namun, pengaturan ini tidak hanya menangani pemicu untuk toko atau log administrator. Pengaturan Email ini juga membuat pemulihan kata sandi tersedia di BTCPay Server saat Login. Cara kerjanya mirip dengan pengaturan spesifik toko; administrator dapat dengan cepat mengisi parameter Email mereka dan memasukkan kredensial email mereka, dan server sekarang dapat mengirim email.

### Kebijakan

Administrator kebijakan BTCPay Server dapat menetapkan beberapa pengaturan pada topik seperti Pengaturan Pengguna yang Ada, Pengaturan Pengguna Baru, Pengaturan Notifikasi, dan Pengaturan Pemeliharaan. Ini dimaksudkan untuk mendaftarkan pengguna baru sebagai admin atau pengguna normal atau bahkan menyembunyikan BTCPay Server dari mesin pencari dengan menambahkannya ke header server Anda.

#### Pengaturan Pengguna yang Ada

Opsi yang tersedia di sini terpisah dari peran kustom. Izin tambahan ini mungkin membuat toko atau pemilik toko rentan terhadap serangan. Kebijakan yang mungkin ditambahkan kepada pengguna yang ada:

- Izinkan non-admin untuk menggunakan node Lightning internal di toko mereka.
  - Ini akan memungkinkan pemilik toko untuk menggunakan node Lightning Administrator server, dan oleh karena itu, dananya! Hati-hati, ini bukan solusi untuk memberikan akses ke Lightning.
- Izinkan non-admin untuk membuat dompet panas untuk toko mereka.
  - Ini akan memungkinkan siapa saja dengan akun di instance BTCPay Server Anda untuk membuat Dompet Panas dan menyimpan benih pemulihan mereka di server Administrator. Ini mungkin membuat Administrator bertanggung jawab atas penyimpanan dana pihak ketiga!
- Izinkan non-admin untuk mengimpor dompet panas untuk toko mereka.
  - Serupa dengan topik sebelumnya tentang membuat Dompet Panas, kebijakan ini memungkinkan mengimpor dompet panas, dengan bahaya yang sama disebutkan di bagian membuat dompet panas.

#### Pengaturan Pengguna Baru

Kita dapat menetapkan beberapa pengaturan penting untuk mengelola pengguna baru yang datang ke server. Kita dapat menetapkan email konfirmasi untuk pendaftaran baru, Nonaktifkan pembuatan pengguna baru melalui layar login, dan batasi akses non-admin ke pembuatan pengguna melalui endpoint API.

- Memerlukan email konfirmasi untuk mendaftar.
  - Administrator server harus telah menyiapkan server Email!
- Nonaktifkan pendaftaran pengguna baru di server
- Nonaktifkan akses non-admin ke endpoint API pembuatan pengguna.

Secara default, BTCPay Server telah mengaktifkan Nonaktifkan pendaftaran pengguna baru dan mematikan akses non-admin ke endpoint API pembuatan pengguna. Ini adalah dari aspek keamanan di mana tidak ada orang acak yang mungkin telah menemukan Login BTCPay server Anda dapat mulai membuat akun.

#### Pengaturan Notifikasi

![image](assets/en/76.webp)

#### Pengaturan Pemeliharaan

BTCPay Server adalah proyek Open Source yang berada di GitHub. Setiap kali BTCPay Server merilis versi baru dari perangkat lunak, Administrator dapat diberitahu bahwa versi baru tersedia. Administrator mungkin juga ingin mencegah mesin pencari (google, yahoo, duckduckgo) dari mengindeks domain BTCPay Server. Karena BTCPay Server adalah FOSS, pengembang di seluruh dunia mungkin ingin membuat fitur baru; BTCPay Server memiliki fitur eksperimental yang ketika diaktifkan, seorang administrator dapat menggunakan fitur yang belum dimaksudkan untuk produksi, murni untuk tujuan pengujian.

- Periksa rilis di GitHub dan beri tahu ketika versi BTCPay Server baru tersedia.
- Mencegah mesin pencari mengindeks situs ini
- Mengaktifkan fitur eksperimental.

![image](assets/en/77.webp)

#### Plugin

BTCPay Server dapat menambahkan Plugin dan memperluas set fiturnya. Plugin, secara default, dimuat dari repositori plugin-builder BTCPay Server. Namun, seorang administrator dapat memilih untuk melihat plugin dalam keadaan Pra-rilis, dan jika pengembang plugin mengizinkannya, administrator server sekarang dapat menginstal versi beta dari plugin.

![image](assets/en/78.webp)

##### Pengaturan Kustomisasi

Penerapan BTCPay Server standar akan dapat diakses melalui domain yang diatur untuknya saat instalasi. Namun, seorang administrator server dapat memetakan ulang domain root dan menampilkan salah satu aplikasi yang dibuat dari toko tertentu. Administrator Server juga dapat memetakan domain tertentu ke aplikasi tertentu.

- Tampilkan aplikasi di root situs web
  - Menampilkan daftar aplikasi yang mungkin untuk ditampilkan di domain root.

![image](assets/en/79.webp)

- Memetakan domain tertentu ke aplikasi tertentu.
  - Ketika Anda klik untuk mengatur domain tertentu untuk aplikasi tertentu, Administrator dapat menetapkan sebanyak mungkin domain yang ditunjuk ke aplikasi tertentu sesuai kebutuhan.

![image](assets/en/80.webp)

#### Eksplorasi Blok

BTCPay Server, sebagai standar, dilengkapi dengan mempool.space sebagai eksplorasi bloknya untuk transaksi. Ketika BTCPay Server menghasilkan faktur baru, dan ada transaksi yang terikat dengannya, pemilik toko dapat mengklik untuk membuka transaksi; BTCPay Server akan standar menunjuk ke mempool.space sebagai eksplorasi blok; seorang Administrator server dapat mengubah ini sesuai preferensinya.

![image](assets/en/81.webp)

### Layanan

Tab pengaturan BTCPay Server: Layanan adalah gambaran umum komponen yang digunakan BTCPay Server Anda. Layanan yang diexpose oleh BTCPay Server Anda mungkin bervariasi tergantung pada metode penyebaran.

Seorang Administrator BTCPay Server dapat mengklik "Lihat informasi" di belakang setiap layanan untuk membukanya dan mengatur pengaturan spesifik.

![image](assets/en/82.webp)

#### LND (gRPC)

BTCPay mengekspos layanan gRPC LND untuk konsumsi luar; Anda akan menemukan informasi koneksi di menu pengaturan spesifik ini; dompet yang kompatibel terdaftar di sini. BTCPay Server juga memberikan kode QR untuk koneksi untuk dipindai dan diterapkan di dompet seluler.

Administrator server dapat membuka lebih banyak detail untuk melihat;

- Detail Host
- Penggunaan SSL
- Macaroon
- AdminMacaroon
- InvoiceMacaroon
- ReadonlyMacaroon
- Suite Cipher SSL GRPC (GRPC_SSL_CIPHER_SUITES)

#### LND (REST)

BTCPay mengekspos layanan REST LND untuk konsumsi luar; Anda akan menemukan informasi koneksi di sini; dompet yang kompatibel terdaftar di sini. Di antara dompet yang kompatibel adalah Joule, Alby, dan ZeusLN. BTCPay Server memberikan kode QR untuk koneksi, pindai dan terapkan di dompet yang kompatibel.

- Uri REST
- Macaroon
- AdminMacaroon - InvoiceMacaroon
- ReadonlyMacaroon

#### Cadangan Seed LND

Cadangan seed LND berguna untuk memulihkan dana dari dompet LND Anda dalam kasus kerusakan Server Anda. Karena node Lightning adalah Hot-wallet, Anda dapat menemukan informasi seed rahasia di halaman ini.

LND mendokumentasikan proses pemulihan. Lihat https://github.com/lightningnetwork/lnd/blob/master/docs/recovery.md untuk dokumentasi.

#### Mengendarai Petir

Ride the Lightning adalah alat manajemen node Lightning yang dibangun sebagai perangkat lunak Open Source. BTCPay Server menggunakan RTL sebagai komponen manajemen node Lightning dalam tumpukannya. Administrator BTCPay Server dapat mengakses RTL melalui pengaturan Server - tab Layanan atau dengan mengklik pada dompet Lightning.

#### Node Penuh P2P

Administrator server mungkin ingin menghubungkan node Bitcoin mereka ke dompet seluler. Halaman ini mengungkapkan informasi untuk terhubung secara remote ke node penuh Anda melalui protokol P2P. Saat menulis buku ini, BTCPay Server mencantumkan Blockstream Green dan Wasabi wallet sebagai dompet yang kompatibel. BTCPay Server memberikan kode QR untuk koneksi, pindai dan terapkan di dompet yang kompatibel.

#### Node Penuh RPC

Halaman ini mengungkapkan informasi untuk terhubung secara remote ke node penuh Anda melalui protokol RPC.

#### SSH

SSH digunakan untuk tujuan pemeliharaan. BTCPay Server menampilkan perintah koneksi awal untuk mencapai Server Anda dan kunci publik SSH yang diizinkan untuk terhubung ke Server Anda. Administrator Server mungkin ingin mematikan perubahan SSH melalui UI dari BTCPay Server.

#### DNS Dinamis

DNS Dinamis memungkinkan Anda memiliki nama DNS yang stabil yang menunjuk ke Server Anda, bahkan jika alamat IP Anda berubah secara teratur. Ini direkomendasikan jika Anda menghosting BTCPay Server di rumah dan ingin memiliki domain clearnet untuk mengakses Server Anda.

Perhatikan bahwa Anda perlu mengonfigurasi NAT dan instalasi BTCPay Server Anda dengan benar untuk mendapatkan sertifikat HTTPS.

### Tema

BTCPay Server, sebagai standar, datang dengan dua tema: Mode Terang dan Gelap. Ini dapat diubah dengan mengklik pada Akun di kiri bawah dan beralih antara tema Gelap atau tema Terang. Administrator BTCPay Server dapat menambahkan tema mereka sendiri dengan menyediakan tema CSS khusus.

Administrator dapat memperluas tema Terang/Gelap dengan menambahkan CSS khusus mereka sendiri atau mengatur tema khusus mereka sebagai kustom penuh.

![image](assets/en/83.webp)

#### Branding Server

Administrator server dapat mengubah branding BTCPay Server dengan menetapkan branding luas Server perusahaan Anda. Karena BTCPay Server adalah FOSS, administrator server dapat memberi label putih pada perangkat lunak dan mengubah tampilannya untuk sesuai dengan bisnis mereka.

![image](assets/en/84.webp)

### Pemeliharaan

Sebagai administrator server, pengguna Anda mengharapkan Anda untuk merawat Server dengan baik. Dalam tab Pemeliharaan BTCPay Server, admin dapat melakukan beberapa pemeliharaan penting. Menetapkan nama domain ke instansi BTCPay Server, Memulai ulang atau membersihkan Server. Mungkin yang paling penting, menjalankan pembaruan.

BTCPay Server adalah proyek Open Source dan sering diperbarui. Setiap rilis baru diumumkan baik oleh Notifikasi BTCPay Server Anda atau di saluran resmi yang dikomunikasikan oleh BTCPay Server.

![image](assets/en/85.webp)

#### Nama domain

Setelah BTCPay Server diatur, administrator mungkin ingin mengubah dari Domain aslinya. Dalam tab Pemeliharaan, administrator dapat mengubah Domain. Setelah mengklik konfirmasi dan menyiapkan catatan DNS yang tepat pada Domain, BTCPay Server memperbarui dan memulai ulang untuk kembali ke Domain baru.

![image](assets/en/86.webp)

#### Memulai Ulang

Memulai ulang BTCPay Server dan layanan terkait.

![image](assets/en/87.webp)

#### Bersihkan

BTCPay Server berjalan dengan komponen Docker; dengan pembaruan, mungkin ada sisa-sisa gambar Docker, file sementara, dll. Administrator Server dapat membersihkan ini dan mendapatkan kembali ruang pada lingkungan mereka dengan menjalankan skrip Bersih.
![image](assets/en/88.webp)

#### Pembaruan

Mungkin opsi paling penting di tab Pemeliharaan. BTCPay Server dibangun oleh komunitas, dan oleh karena itu, siklus pembaruannya lebih sering daripada kebanyakan produk perangkat lunak. Ketika BTCPay Server memiliki rilis baru, administrator akan diberitahu di pusat notifikasi mereka. Dengan mengklik tombol pembaruan, BTCPay Server akan memeriksa GitHub untuk rilis terbaru, memperbarui Server dan memulai ulang. Sebelum memperbarui, administrator server selalu disarankan untuk membaca catatan rilis yang didistribusikan melalui saluran resmi BTCPay Server.

![image](assets/en/89.webp)

### Log

Menghadapi masalah tidak pernah menyenangkan. Dokumen ini menjelaskan alur kerja dan langkah paling umum untuk mengidentifikasi masalah Anda secara efisien dan menyelesaikannya sendiri atau dengan bantuan komunitas.

Mengidentifikasi masalah sangat penting.

#### Mereplikasi masalah

Pertama dan terpenting, coba tentukan kapan masalah terjadi. Coba replikasi masalahnya. Coba perbarui dan mulai ulang Server Anda untuk memverifikasi bahwa Anda dapat mereproduksi masalah Anda. Jika itu menggambarkan masalah Anda dengan lebih baik, ambil tangkapan layar.

##### Memperbarui server

Periksa versi BTCPay Server Anda jika jauh lebih tua dari [versi terbaru](https://github.com/btcpayserver/btcpayserver/releases) BTCPay Server. Memperbarui Server Anda dapat menyelesaikan masalah.

##### Memulai ulang server

Memulai ulang Server Anda adalah cara mudah untuk menyelesaikan banyak masalah BTCPay Server yang paling umum. Anda mungkin perlu SSH ke Server Anda untuk memulainya ulang.

##### Memulai ulang layanan

Untuk beberapa masalah, Anda mungkin hanya perlu memulai ulang layanan tertentu dalam penyebaran BTCPay Server Anda. Seperti memulai ulang kontainer lets encrypt untuk memperbarui sertifikat SSL.

```bash
sudo su -
cd btcpayserver-docker
docker restart letsencrypt-nginx-proxy-companion
```

Gunakan docker ps untuk menemukan nama layanan lain yang ingin Anda mulai ulang.

#### Melihat melalui log

Log dapat memberikan informasi penting. Dalam paragraf berikut, kami akan menjelaskan cara mendapatkan informasi log untuk berbagai bagian BTCPay.

##### Log BTCPay

Sejak v1.0.3.8, Anda dapat dengan mudah mengakses log BTCPay Server dari antarmuka pengguna. Jika Anda adalah admin server, pergi ke Pengaturan Server > Log dan buka file log. Jika Anda tidak tahu apa arti kesalahan tertentu dalam log, sebutkan saat pemecahan masalah.

Jika Anda ingin log yang lebih rinci dan menggunakan penyebaran Docker, Anda dapat melihat log kontainer Docker tertentu menggunakan baris perintah. Lihat [instruksi ini untuk ssh](https://docs.btcpayserver.org/FAQ/ServerSettings/#how-to-ssh-into-my-btcpay-running-on-vp%C2%80) ke instance BTCPay yang berjalan pada VPS.

Di halaman berikutnya, daftar umum nama kontainer yang digunakan untuk BTCPay Server.

Jalankan perintah di bawah ini untuk mencetak log berdasarkan nama kontainer. Ganti nama kontainer untuk melihat log kontainer lain.

```bash
sudo su -
cd btcpayserver-docker
docker ps
docker logs --tail 100 generated_btcpayserver_1
```

| Log untuk    | Nama Kontainer                    |
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
Navigasi ke direktori yang benar:
cd btcpayserver-docker
# Temukan nama kontainer:
<partId>6f124f36-b51c-5e53-a734-08fb1f20db25</partId>
docker ps
Cetak log berdasarkan nama kontainer:
docker logs --tail 100 btcpayserver_lnd_bitcoin
```

Sebagai alternatif, Anda dapat dengan cepat mencetak log dengan menggunakan ID kontainer (hanya karakter ID unik pertama yang diperlukan, seperti dua karakter paling kiri):

```bash
docker logs 'tambahkan ID kontainer Anda'
```

Jika karena alasan apa pun Anda memerlukan lebih banyak log

```bash
sudo su -
cd /var/lib/docker/volumes/generated_lnd_bitcoin_datadir/_data/logs/bitcoin/mainnet/
ls
```

Anda akan melihat sesuatu seperti

```bash
lnd.log lnd.log.13 lnd.log.15 lnd.log.16.gz lnd.log.17.gz
```

Untuk mengakses log yang tidak dikompres dari log tersebut lakukan `cat lnd.log` atau jika Anda ingin yang lain, gunakan `cat lnd.log.15`.

Untuk mengakses log yang dikompres dalam `.gzip` gunakan `gzip -d lnd.log.16.gz` (dalam kasus ini kita mengakses `lnd.log.16.gz`). Ini seharusnya memberi Anda file baru, di mana Anda dapat melakukan `cat lnd.log.16`. Jika cara di atas tidak berhasil, Anda mungkin perlu menginstal gzip terlebih dahulu dengan `sudo apt-get install gzip`.

###### Lightning Network c-lightning - Docker

```bash
sudo su -
docker ps
# Temukan ID kontainer c-lightning.
<partId>8f12e767-13df-5bc4-85e4-00e227091300</partId>
docker logs 'tambahkan ID kontainer Anda di sini'
```

alternatifnya, gunakan ini

```bash
docker logs --tail 100 btcpayserver_clightning_bitcoin
```

Anda juga bisa mendapatkan informasi log dengan perintah cli c-lightning.

```bash
bitcoin-lightning-cli.sh getlog
```

#### Log Node Bitcoin

Selain [melihat log](https://docs.btcpayserver.org/Troubleshooting/#2-looking-through-the-logs) dari kontainer Bitcoind Anda, Anda juga dapat menggunakan salah satu dari [perintah bitcoin-cli](https://developer.bitcoin.org/reference/rpc/index.html)

[(buka jendela baru)](https://developer.bitcoin.org/reference/rpc/index.html) untuk mendapatkan informasi dari node bitcoin Anda. BTCPay menyertakan skrip untuk memungkinkan Anda berkomunikasi dengan node Bitcoin Anda dengan mudah.

Di dalam folder btcpayserver-docker, dapatkan informasi blockchain menggunakan node Anda:

```bash
bitcoin-cli.sh getblockchaininfo
```

### Berkas

BTCPay Server memiliki sistem file lokal dan mengunggah aset Toko (produk), Logo, dan branding langsung ke Server. Sistem file Server hanya dapat diakses oleh Administrator Server; pemilik toko dapat mengunggah logo/branding mereka di tingkat toko.
Ketika Administrator Server berada di tab Penyimpanan File, dimungkinkan untuk langsung mengunggah ke Server Anda atau mengubah penyedia penyimpanan file ke sistem file Lokal atau Azure Blob Storage.

![gambar](assets/en/90.webp)

![gambar](assets/en/91.webp)

### Ringkasan Keterampilan

Dalam bagian ini, Anda mempelajari hal-hal berikut:

- Perbedaan antara pengaturan Toko dan Server, khususnya terkait dengan Pengguna, Peran, dan Email
- Menetapkan kebijakan seluruh server untuk penggunaan dan pembuatan dompet panas Lightning atau Bitcoin, pendaftaran pengguna baru, dan notifikasi email.
- Bagaimana menambahkan tema kustom (bukan hanya opsi terang/gelap yang disediakan) serta membuat logo kustom
- Melakukan tugas pemeliharaan server sederhana melalui GUI yang disediakan
- Memecahkan masalah, termasuk mengambil detail untuk salah satu kontainer Docker atau node Anda
- Mengelola penyimpanan file

### Penilaian Pengetahuan

#### Ulasan Konseptual KA

Apa perbedaan dalam Peran yang ditetapkan melalui Pengaturan Server vs Pengaturan Toko, dan apa yang menjelaskan penggunaan potensial untuk satu daripada yang lain?

#### Ulasan Praktis KA

Jelaskan beberapa kasus penggunaan yang dimungkinkan di tab Kebijakan.

#### Ulasan Praktis KA

Jelaskan beberapa tindakan yang mungkin secara rutin dilakukan administrator di tab Pemeliharaan.

## BTCPay Server - Pembayaran

<chapterId>e2b71ff9-3f4f-5e71-9771-8e03fbbef00f</chapterId>

Faktur adalah dokumen yang dikeluarkan penjual kepada pembeli untuk mengumpulkan pembayaran.

Di BTCPay Server, faktur mewakili dokumen yang harus dibayar dalam interval waktu tertentu dengan kurs tetap. Faktur memiliki batas waktu karena mereka mengunci kurs dalam jangka waktu tertentu untuk melindungi penerima dari fluktuasi harga.

Inti dari BTCPay Server adalah kemampuannya untuk bertindak sebagai sistem manajemen faktur Bitcoin. Faktur adalah alat penting untuk melacak dan mengelola pembayaran yang diterima.

Kecuali Anda menggunakan [Wallet](https://docs.btcpayserver.org/Wallet/) bawaan untuk menerima pembayaran secara manual, semua pembayaran dalam toko akan ditampilkan di halaman Faktur. Halaman ini mengurutkan pembayaran secara kumulatif berdasarkan tanggal dan merupakan bagian pusat untuk manajemen faktur dan pemecahan masalah pembayaran.

![gambar](assets/en/92.webp)

### Umum

#### Status Faktur

Tabel di bawah ini mencantumkan dan menjelaskan status faktur standar di BTCPay dan menyarankan tindakan umum. Tindakan hanyalah rekomendasi. Terserah pengguna untuk menentukan langkah terbaik untuk kasus penggunaan dan bisnis mereka.

| Status Faktur                      | Deskripsi                                                                                                                               | Tindakan                                                                                                                                                             |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Baru                               | Belum dibayar, timer faktur masih belum kedaluwarsa                                                                                     | Tidak ada                                                                                                                                                            |
| Baru (dibayarSebagian)             | Dibayar, tidak penuh, timer faktur masih belum kedaluwarsa                                                                              | Tidak ada                                                                                                                                                            |
| Kedaluwarsa                        | Belum dibayar, timer faktur kedaluwarsa                                                                                                 | Tidak ada                                                                                                                                                            |
| Kedaluwarsa (dibayarSebagian) \*\* | Dibayar, tidak dengan jumlah penuh, dan kedaluwarsa                                                                                     | Hubungi pembeli untuk mengatur pengembalian dana atau meminta mereka untuk membayar yang kurang. Secara opsional tandai faktur sebagai diselesaikan atau tidak valid |
| Kedaluwarsa (dibayarTerlambat)     | Dibayar, dengan jumlah penuh, setelah timer faktur kedaluwarsa                                                                          | Hubungi pembeli untuk mengatur pengembalian dana atau proses pesanan jika konfirmasi terlambat diterima.                                                             |
| Settled (paidOver)                 | Pembayaran melebihi jumlah faktur, diselesaikan, menerima jumlah konfirmasi yang cukup                                                  | Hubungi pembeli untuk mengatur pengembalian dana untuk jumlah ekstra, atau tunggu pembeli menghubungi Anda secara opsional                                           |
| Processing                         | Dibayar penuh, tetapi belum menerima jumlah konfirmasi yang cukup sesuai dengan pengaturan toko                                         | Hubungi pembeli untuk mengatur pengembalian dana untuk jumlah ekstra, atau tunggu pembeli menghubungi Anda secara opsional                                           |
| Processing (paidOver)              | Pembayaran melebihi jumlah faktur, belum menerima jumlah konfirmasi yang cukup                                                          | Tunggu hingga diselesaikan kemudian hubungi pembeli untuk mengatur pengembalian dana untuk jumlah ekstra, atau tunggu pembeli menghubungi Anda secara opsional       |
| Settled                            | Dibayar, penuh, menerima jumlah konfirmasi yang cukup di toko                                                                           | Penuhi pesanan                                                                                                                                                       |
| Settled (marked)                   | Status diubah secara manual menjadi diselesaikan dari status yang sedang diproses atau tidak valid                                      | Admin toko telah menandai pembayaran sebagai diselesaikan                                                                                                            |
| Invalid\*                          | Dibayar, tetapi gagal menerima jumlah konfirmasi yang cukup dalam waktu yang ditentukan dalam pengaturan toko                           | Periksa transaksi di penjelajah blockchain, jika menerima konfirmasi yang cukup, tandai sebagai diselesaikan                                                         |
| Invalid (marked)                   | Status diubah secara manual menjadi tidak valid dari status yang diselesaikan atau kadaluarsa                                           | Admin toko telah menandai pembayaran sebagai tidak valid                                                                                                             |
| Invalid (paidOver)                 | Pembayaran melebihi jumlah faktur, tetapi gagal menerima jumlah konfirmasi yang cukup dalam waktu yang ditentukan dalam pengaturan toko | Periksa transaksi di penjelajah blockchain, jika menerima konfirmasi yang cukup, tandai sebagai diselesaikan                                                         |

#### Detail Faktur

Halaman detail faktur berisi semua informasi terkait faktur.

Informasi faktur dibuat secara otomatis berdasarkan status faktur, nilai tukar, dll. Informasi produk dibuat secara otomatis jika faktur dibuat dengan informasi produk, seperti dalam aplikasi Point of Sale.

#### Penyaringan Faktur

Faktur dapat disaring melalui filter cepat yang terletak di sebelah tombol pencarian atau filter lanjutan, yang dapat diaktifkan dengan mengklik tautan (Bantuan) di atas. Pengguna dapat menyaring faktur berdasarkan toko, id pesanan, id item, status, atau tanggal.

#### Ekspor Faktur

Faktur BTCPay Server dapat diekspor dalam format CSV atau JSON. Untuk informasi lebih lanjut tentang ekspor faktur dan akuntansi.

#### Mengembalikan Faktur

Jika, karena alasan apa pun, Anda ingin mengeluarkan pengembalian dana, Anda dapat dengan mudah membuat pengembalian dana dari tampilan faktur.

#### Mengarsipkan Faktur

Sebagai hasil dari fitur tidak menggunakan alamat ulang dari BTCPay Server, umum untuk melihat banyak faktur yang kadaluarsa di halaman faktur toko Anda. Untuk menyembunyikannya dari tampilan Anda, pilihlah dalam daftar dan tandai sebagai diarsipkan. Faktur yang telah ditandai sebagai diarsipkan tidak dihapus. Pembayaran ke faktur yang diarsipkan masih akan terdeteksi oleh BTCPay Server Anda (status paidLate). Anda dapat melihat faktur yang diarsipkan toko kapan saja dengan memilih faktur yang diarsipkan dari dropdown filter pencarian.

#### Mata Uang Default

Mata uang default toko, ini ditetapkan pada saat pembuatan toko

#### Izinkan Siapa Saja untuk Membuat Faktur

Anda harus mengaktifkan opsi ini jika Anda ingin mengizinkan dunia luar untuk membuat faktur di toko Anda. Opsi ini hanya berguna jika Anda menggunakan tombol pembayaran atau jika Anda mengeluarkan faktur melalui API atau situs web HTML pihak ketiga. Aplikasi PoS sudah diotorisasi dan tidak perlu diaktifkan agar pengunjung acak dapat membuka toko PoS Anda dan membuat faktur.

#### Tambahkan Biaya Tambahan (biaya jaringan) ke Faktur

- Hanya jika pelanggan melakukan lebih dari satu pembayaran untuk faktur
- Pada setiap pembayaran
- Jangan pernah menambahkan biaya jaringan

#### Faktur kedaluwarsa jika jumlah penuh belum dibayar setelah .. Menit.

Timer faktur diatur ke 15 menit secara default. Timer ini adalah mekanisme perlindungan terhadap volatilitas karena mengunci jumlah kriptokurensi sesuai dengan tarif kripto ke fiat. Jika pelanggan tidak membayar faktur dalam periode yang ditentukan, faktur dianggap kedaluwarsa. Faktur dianggap "dibayar" segera setelah transaksi terlihat di blockchain (o-konfirmasi) tetapi dianggap "lengkap" ketika mencapai jumlah konfirmasi yang ditentukan oleh pedagang (biasanya, 1-6). Timer dapat disesuaikan.

#### Anggap faktur dibayar meskipun jumlah yang dibayar ..% kurang dari yang diharapkan.

Dalam situasi di mana pelanggan menggunakan dompet pertukaran untuk membayar langsung faktur, pertukaran mengambil sejumlah kecil biaya. Ini berarti bahwa faktur tersebut tidak dianggap sepenuhnya selesai. Faktur mendapatkan status "dibayar sebagian." Jika pedagang ingin menerima faktur yang dibayar kurang, Anda dapat menetapkan tarif persentase di sini.

### Permintaan

Permintaan Pembayaran adalah fitur yang memungkinkan pemilik toko BTCPay untuk membuat faktur berjangka panjang. Dana dibayar ke permintaan pembayaran menggunakan tarif tukar pada saat pembayaran. Ini memungkinkan pengguna untuk melakukan pembayaran sesuai keinginan mereka tanpa negosiasi atau verifikasi tarif tukar dengan pemilik toko pada saat pembayaran.

Pengguna dapat membayar permintaan dalam pembayaran parsial. Permintaan pembayaran akan tetap valid sampai dibayar penuh atau jika pemilik toko memerlukan waktu kedaluwarsa. Alamat tidak pernah digunakan ulang. Alamat baru dihasilkan setiap kali pengguna mengklik bayar untuk membuat faktur untuk permintaan pembayaran.

Pemilik toko dapat mencetak permintaan pembayaran (atau mengekspor data faktur) untuk pencatatan dan akuntansi. BTCPay secara otomatis memberi label faktur sebagai Permintaan Pembayaran dalam daftar faktur toko Anda.

#### Sesuaikan Permintaan Pembayaran Anda

- Jumlah Faktur - Tetapkan Jumlah Pembayaran yang Diminta
- Denominasi - Tampilkan Jumlah yang Diminta dalam Fiat atau Kriptokurensi
- Kuantitas Pembayaran - Izinkan hanya pembayaran tunggal atau pembayaran parsial
- Waktu Kedaluwarsa - Izinkan pembayaran sampai tanggal tertentu atau tanpa kedaluwarsa
- Deskripsi - Editor Teks, Tabel Data, Sisipkan Foto & Video
- Penampilan - Warna dan Gaya dengan Tema CSS

![image](assets/en/93.webp)

#### Buat Permintaan Pembayaran

Di menu kiri, pergi ke Permintaan Pembayaran dan klik "Buat Permintaan Pembayaran".

![image](assets/en/94.webp)

Berikan Nama Permintaan, Jumlah, Denominasi Tampilan, Toko Terkait, Waktu Kedaluwarsa & Deskripsi (Opsional)

Pilih opsi Izinkan pembayar membuat faktur dalam denominasi mereka jika Anda ingin mengizinkan pembayaran parsial.

Klik Simpan & Lihat untuk meninjau permintaan pembayaran Anda.

BTCPay membuat URL untuk permintaan pembayaran. Bagikan URL ini untuk melihat permintaan pembayaran Anda. Butuh beberapa permintaan yang sama? Anda dapat menduplikasi permintaan pembayaran menggunakan opsi Klon di menu utama.

![image](assets/en/95.webp)

**PERINGATAN**

Permintaan pembayaran tergantung pada toko, artinya setiap permintaan pembayaran dikaitkan dengan toko saat pembuatan. Pastikan untuk memiliki dompet yang terhubung ke toko Anda yang dimiliki permintaan pembayaran.

#### Permintaan Dibayar

Pembayar dan peminta dapat melihat status permintaan pembayaran setelah mengirim pembayaran. Status akan muncul sebagai Settled jika pembayaran telah diterima penuh. Jika hanya pembayaran parsial yang dilakukan, Jumlah yang Harus Dibayar akan menunjukkan saldo yang harus dibayar.

![image](assets/en/96.webp)

#### Sesuaikan Permintaan Pembayaran

Konten deskripsi dapat diedit menggunakan editor teks permintaan pembayaran. Kedua opsi tersedia jika Anda ingin menggunakan tema warna tambahan atau penataan CSS kustom.
Pengguna non-teknis dapat menggunakan [tema bootstrap](https://docs.btcpayserver.org/Development/Theme/#2-bootstrap-themes). Kustomisasi lebih lanjut dapat dilakukan dengan menyediakan kode CSS tambahan, seperti yang ditunjukkan di bawah ini.

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

### Pembayaran Pull

Secara tradisional, penerima membagikan alamat Bitcoin mereka untuk melakukan pembayaran Bitcoin, dan pengirim kemudian mengirim uang ke alamat ini. Sistem seperti ini disebut Pembayaran Push, karena pengirim yang memulai pembayaran sementara penerima mungkin tidak tersedia, mendorong pembayaran ke penerima.

Namun, bagaimana jika peran tersebut dibalik?

Bagaimana jika, alih-alih pengirim yang mendorong pembayaran, pengirim memungkinkan penerima untuk menarik pembayaran pada waktu yang dianggap tepat oleh penerima? Ini adalah konsep dari Pembayaran Pull. Ini memungkinkan beberapa aplikasi baru, seperti:

- Layanan berlangganan (di mana pelanggan memungkinkan layanan untuk menarik uang setiap jumlah waktu tertentu)
- Pengembalian dana (di mana pedagang memungkinkan pelanggan untuk menarik uang pengembalian ke dompet mereka kapan saja mereka anggap tepat)
- Penagihan berbasis waktu untuk freelancer (di mana orang yang mempekerjakan memungkinkan freelancer untuk menarik uang ke dompet mereka seiring waktu dilaporkan)
- Patronase (di mana patron memungkinkan penerima untuk menarik uang setiap bulan untuk terus mendukung pekerjaan mereka)
- Penjualan otomatis (di mana pelanggan dari bursa memungkinkan bursa untuk menarik uang dari dompet mereka untuk dijual setiap bulan secara otomatis)
- Sistem penarikan saldo (di mana layanan volume tinggi memungkinkan pengguna untuk meminta penarikan dari saldo mereka, layanan kemudian dapat dengan mudah mengelompokkan semua pembayaran ke banyak pengguna pada interval tetap)

### Pembayaran

Fungsionalitas pembayaran terikat ke [Pembayaran Pull](https://docs.btcpayserver.org/PullPayments/). Fitur ini memungkinkan Anda untuk membuat pembayaran dalam BTCPay Anda. Fitur ini memungkinkan Anda untuk memproses pembayaran pull (pengembalian dana, pembayaran gaji, atau penarikan).

#### Contoh 1: Pengembalian Dana

Mari kita mulai dengan contoh pengembalian dana. Pelanggan telah membeli sebuah item di toko Anda tetapi sayangnya harus mengembalikan item tersebut. Mereka ingin pengembalian dana. Dalam BTCPay, Anda dapat membuat [Pengembalian Dana](https://docs.btcpayserver.org/Refund/) dan memberikan pelanggan dengan tautan untuk mengklaim dana mereka. Kapan pun pelanggan telah memberikan alamat mereka dan mengklaim dana, itu akan ditampilkan dalam Pembayaran.

Status pertama yang dimilikinya adalah Menunggu Persetujuan. Petugas toko dapat memeriksa jika ada beberapa yang menunggu, dan setelah membuat pilihan, Anda menggunakan tombol Aksi.

Opsi pada tombol aksi

- Setujui pembayaran yang dipilih
- Setujui & kirim pembayaran yang dipilih
- Batalkan pembayaran yang dipilih

Langkah selanjutnya adalah untuk Menyetujui & mengirim pembayaran yang dipilih karena kami ingin mengembalikan dana kepada pelanggan. Periksa Alamat Pelanggan, menunjukkan jumlah dan jika kita ingin biaya dikurangkan dari pengembalian dana atau tidak. Setelah Anda melakukan pemeriksaan, hanya menandatangani transaksi yang tersisa.
Pelanggan kini mendapatkan pembaruan di halaman Klaim. Dia dapat mengikuti transaksi karena dia diberikan link ke block explorer dan transaksinya. Setelah transaksi dikonfirmasi, dan status berubah menjadi Selesai.

#### Contoh 2: Gaji

Sekarang mari kita bahas tentang pembayaran gaji, karena ini dijalankan dari dalam toko dan bukan atas permintaan Pelanggan. Dasarnya sama; ini menggunakan pembayaran Tarik. Tapi alih-alih membuat pengembalian dana, kita akan membuat [Pembayaran Tarik](https://docs.btcpayserver.org/PullPayments/).

Pergi ke tab Pembayaran Tarik di server BTCPay Anda. Di pojok kanan atas, klik tombol Buat Pembayaran Tarik.

Sekarang kita berada dalam pembuatan Pembayaran, beri nama dan jumlah yang diinginkan dalam mata uang yang diinginkan, isi Deskripsi, sehingga karyawan tahu apa maksudnya. Bagian selanjutnya mirip dengan pengembalian dana. Karyawan mengisi Alamat tujuan dan jumlah yang ingin dia klaim dari Pembayaran ini. Dia mungkin memutuskan untuk membuatnya menjadi 2 klaim terpisah, ke alamat yang berbeda, atau bahkan sebagian klaim melalui lightning.

Jika ada beberapa Pembayaran yang menunggu, Anda dapat mengelompokkan ini untuk ditandatangani dan dikirim. Setelah ditandatangani, pembayaran berpindah ke tab Sedang Berlangsung dan menunjukkan Transaksi. Ketika diterima oleh jaringan, pembayaran berpindah ke tab Selesai. Tab selesai murni untuk tujuan historis. Ini menyimpan Pembayaran yang diproses dan transaksi yang termasuk di dalamnya

### Pembayaran Tarik

#### Konsep

Ketika pengirim mengonfigurasi Pembayaran Tarik, mereka dapat mengonfigurasi sejumlah properti:

- Nama Permintaan Tarik
- Jumlah batas
- Satuan (seperti BTC, SAT, USD)
- Metode Pembayaran
  - BTC On-chain
  - BTC Off-chain
- Deskripsi
- CSS Kustom
- Tanggal berakhir (opsional untuk Lightning Network BOLT11)

Setelah ini, pengirim dapat membagikan pembayaran tarik menggunakan link dengan penerima, memungkinkan penerima untuk membuat pembayaran. Penerima akan memilih pembayarannya:

- Metode pembayaran apa yang akan digunakan
- Kemana uang akan dikirim

Setelah pembayaran dibuat, itu akan dihitung terhadap batas pembayaran tarik untuk periode saat ini. Pengirim kemudian akan menyetujui pembayaran dengan menetapkan tarif di mana pembayaran akan dikirim dan melanjutkan dengan pembayaran.

Untuk pengirim, kami menyediakan cara yang mudah digunakan untuk mengelompokkan pembayaran beberapa pembayaran dari [Dompet Internal BTCPay](https://docs.btcpayserver.org/Wallet/).

#### Greenfield API

Server BTCPay menyediakan API lengkap baik untuk pengirim maupun penerima yang didokumentasikan di halaman `/docs` dari instance Anda. (atau di situs web dokumentasi https://docs.btcpayserver.org)

Karena API kami mengekspos kemampuan penuh dari pembayaran tarik, pengirim dapat mengotomatiskan pembayaran sesuai dengan kebutuhannya.

### Ringkasan Keterampilan

Dalam bagian ini, Anda mempelajari hal-hal berikut:

- Pemahaman mendalam tentang status faktur BTCPay Server serta tindakan yang dapat dilakukan pada mereka
- Menyesuaikan dan mengelola mekanisme faktur berumur panjang yang dikenal sebagai Permintaan.
- Kemungkinan pembayaran fleksibel tambahan yang dibuka dengan fitur Pembayaran Tarik unik BTCPay Server, khususnya bagaimana menangani pengembalian dana dan pembayaran gaji.

### Penilaian Pengetahuan

#### KA Tinjauan Konseptual

Apa beberapa perbedaan antara faktur dan permintaan pembayaran, dan apa yang mungkin menjadi alasan baik untuk menggunakan yang terakhir?

#### KA Tinjauan Konseptual

Bagaimana pembayaran tarik memperluas apa yang biasanya dapat dilakukan on-chain? Jelaskan beberapa kasus penggunaan yang mereka aktifkan.

## Plugin Default Server BTCPay

<chapterId>7d673dc4-bd5d-5411-819b-f135f1d86636</chapterId>

### Plugin dan Aplikasi Default

Server BTCPay dilengkapi dengan set standar Plugin (Aplikasi) yang dapat menjadikan BTCPay Server sebagai gateway pembayaran e-commerce. Dengan tambahan Point of Sale, platform Crowdfund, dan tombol Pay yang mudah, BTCPay Server menjadi solusi yang mudah untuk dikerahkan.

### Point Of Sale

Salah satu Plugin standar dari BTCPay Server adalah Point of Sale (PoS). Dengan plugin PoS, pemilik toko dapat membuat Webshop langsung dari BTCPay Server, pemilik toko tidak memerlukan solusi e-commerce pihak ketiga untuk menjalankan Webshop. Aplikasi PoS berbasis web memungkinkan pengguna dengan toko fisik untuk dengan mudah menerima Bitcoin, tanpa biaya atau pihak ketiga, langsung ke dompet mereka. PoS dapat ditampilkan dengan mudah di tablet atau perangkat lain yang mendukung penjelajahan web. Pengguna dapat dengan mudah membuat pintasan layar utama untuk mengakses aplikasi web dengan cepat.

#### Cara membuat Point of Sale baru

BTCPay Server memungkinkan pemilik toko untuk membuat Point of Sale dalam berbagai tata letak dengan cepat. BTCPay Server mengakui bahwa tidak setiap toko adalah e-commerce, dan tidak setiap toko adalah bar atau restoran, dan itu dilengkapi dengan beberapa pengaturan standar untuk PoS Anda.

Ketika pemilik toko mengklik "Point of Sale" di bilah menu kiri mereka, BTCPay Server sekarang akan meminta nama; nama ini akan terlihat di bilah menu kiri. Klik Buat untuk membuat PoS.

![image](assets/en/97.webp)

#### Perbarui Point of Sale yang baru dibuat

Setelah membuat PoS baru, layar berikutnya akan untuk memperbarui Point of Sale Anda dan menambahkan item untuk toko Anda.

##### Nama Aplikasi

Nama yang diberikan di sini untuk Point of Sale Anda akan terlihat di menu utama BTCPay Server.

##### Judul Tampilan

Publik akan melihat judul atau nama publik saat mengunjungi toko Anda. BTCPay Server secara standar menamai toko Anda "Tea shop" Gantikan ini dengan nama toko Anda.

![image](assets/en/98.webp)

#### Pilih Gaya Point of Sale

BTCPay Server mampu menampilkan Point Of Sale-nya dalam beberapa cara.

- Daftar produk
  - Tampilan toko di mana pelanggan hanya dapat membeli 1 produk pada satu waktu.
- Daftar produk dengan keranjang.
  - Tampilan toko di mana pelanggan dapat membeli beberapa item sekaligus dan mendapatkan ikhtisar keranjang belanja di sebelah kanan layar mereka.
- Hanya keypad
  - Tidak ada daftar produk, hanya keypad untuk penagihan langsung.
- Tampilan cetak (Daftar produk yang dapat dicetak dengan QR)
  - Jika Anda tidak selalu dapat menampilkan daftar produk Anda secara digital, Anda memerlukan solusi "offline" untuk produk; BTCPay Server memiliki tampilan cetak untuk berfungsi sebagai toko Offline.

![image](assets/en/99.webp)

#### Gaya Point Of Sale - Daftar Produk

![image](assets/en/100.webp)

#### Gaya Point Of Sale - Daftar Produk + Keranjang

![image](assets/en/101.webp)

#### Gaya Point Of Sale - Hanya Keypad

![image](assets/en/102.webp)

#### Gaya Point Of Sale - Tampilan Cetak

![image](assets/en/103.webp)

#### Mata Uang

Pemilik toko dapat menetapkan mata uang yang berbeda untuk Point of Sale-nya daripada mata uang default yang telah ditetapkan secara keseluruhan. Mata uang default toko akan secara otomatis mengisi bidang ini.

#### Deskripsi

Ceritakan kepada dunia tentang toko Anda; apa yang Anda jual, dan dengan harga berapa? Semua yang menjelaskan toko Anda ada di sini.

#### Produk

Ketika sebuah Titik Penjualan (Point of Sale) dibuat, BTCPay Server standar menambahkan beberapa item ke toko sebagai referensi. Klik tombol Edit pada salah satu item standar untuk memahami setiap opsi yang mungkin untuk sebuah item dengan lebih baik.

Membuat produk baru di toko Anda terdiri dari bidang-bidang berikut;

- Judul
- Harga (tetap, minimum, atau kustom)
- URL Gambar
- Deskripsi
- Inventaris
- ID
- Teks Tombol Beli.
- Aktifkan/Nonaktifkan

Setelah pemilik toko telah mengisi semua bidang produk baru, klik simpan, dan Anda akan melihat bahwa bagian Produk di Titik Penjualan sekarang mulai terisi. Selalu pastikan untuk menyimpan di kanan atas layar Anda untuk menghindari pemilik toko kehilangan kemajuan mereka dalam menambahkan produk.

Pemilik toko juga dapat menggunakan "Editor Mentah" untuk mengonfigurasi produk mereka. Editor mentah memerlukan pemahaman dasar tentang struktur JSON.

#### Pembayaran

BTCPay Server memungkinkan kustomisasi pembayaran spesifik Titik Penjualan yang kecil. Pemilik Toko dapat mengatur teks "Beli untuk x" atau meminta data pelanggan tertentu dengan menambahkan formulir.

#### Tips

Tidak semua toko memerlukan opsi untuk Tips pada penjualan mereka. Pemilik toko dapat mengaktifkan atau menonaktifkan ini sesuai kebutuhan untuk toko mereka. Jika toko menggunakan tips yang diaktifkan, pemilik toko dapat mengatur teks di bidang untuk tips yang mereka suka. Tips BTCPay Server bekerja berdasarkan jumlah persentase. Pemilik toko dapat menambahkan beberapa persentase dengan pemisahan koma.

#### Diskon

Sebagai pemilik toko, Anda mungkin ingin memberikan diskon kustom kepada pelanggan saat pembayaran; tombol untuk Diskon menjadi tersedia di pembayaran toko Anda. Namun, ini sangat tidak disarankan untuk sistem pembayaran mandiri.

#### Pembayaran Kustom

Ketika opsi Pembayaran Kustom diaktifkan, pelanggan mendapat untuk memasukkan harga mereka yang ditetapkan sama dengan atau di atas faktur asli yang dihasilkan oleh toko.

#### Opsi Tambahan

Setelah menyiapkan segalanya untuk Titik Penjualan Anda, masih ada beberapa opsi tambahan. Pemilik toko dapat dengan mudah Menyematkan (Embed) PoS mereka melalui Iframe atau menyematkan tombol pembayaran yang mengarah ke item toko tertentu. Untuk menata toko PoS yang baru dibuat, pemilik toko dapat menambahkan CSS kustom di bagian bawah opsi tambahan.

#### Hapus aplikasi ini

Jika pemilik toko ingin sepenuhnya menghapus Titik Penjualan dari BTCPay Server mereka, di bagian bawah pembaruan PoS, pemilik toko dapat Klik pada tombol Hapus aplikasi ini untuk sepenuhnya menghancurkan aplikasi PoS mereka. Ketika mengklik "Hapus aplikasi ini", BTCPay Server akan meminta konfirmasi dengan mengetik `DELETE` dan mengonfirmasi dengan mengklik tombol Hapus. Setelah menghapus, pemilik toko kembali ke dasbor BTCPay Server.

### BTCPay Server - Crowdfund

Di samping plugin Titik Penjualan, BTCPay Server memiliki opsi untuk membuat crowdfund. Sama seperti platform Crowdfund lainnya, pemilik toko dapat menetapkan tujuan, membuat keuntungan untuk kontribusi, dan menyesuaikannya dengan kebutuhan mereka.

#### Cara menyiapkan crowdfund baru

Klik pada plugin Crowdfund melalui menu utama di sebelah kiri BTCPay Server Anda, di bawah bagian Plugin. BTCPay Server sekarang akan meminta nama untuk Crowdfund; nama ini juga akan ditampilkan di bilah menu kiri.

#### Memperbarui Titik Penjualan yang baru dibuat

Setelah Aplikasi diberi nama, layar selanjutnya akan menjadi untuk memperbarui Aplikasi agar memiliki konteks.

#### Nama Aplikasi

Nama yang diberikan untuk Crowdfund Anda akan terlihat di menu utama BTCPay Server.

#### Judul Tampilan

Judul diberikan untuk Crowdfund bagi publik.

#### Tagline

Berikan satu kalimat untuk Crowdfund agar orang mengenali tujuan penggalangan dana tersebut.

![image](assets/en/107.webp)

#### URL Gambar Utama

Setiap Crowdfund memiliki gambar utamanya, banner yang langsung Anda kenali. Gambar ini dapat disimpan di server Anda jika Anda memiliki hak Administratif, Admin dapat mengunggahnya di pengaturan Server BTCPay - Files. Ketika Anda pemilik Toko, gambar harus diunggah ke web melalui host pihak ketiga (misalnya imgur)

#### Membuat Crowdfund Publik

Tombol ini membuat Crowdfund Anda menjadi publik dan dengan demikian terlihat untuk dunia luar. Untuk tujuan pengujian atau untuk melihat apakah tema Anda diterapkan dengan benar, seseorang mungkin ingin membiarkan ini diatur ke OFF selama periode pembuatan crowdfund.

#### Deskripsi

Ceritakan kepada dunia tentang Crowdfund Anda, apa yang Anda galang dana untuk? Semua penjelasan tentang crowdfund Anda ada di sini.

![image](assets/en/108.webp)

#### Tujuan Crowdfund

Tetapkan tujuan target untuk apa yang harus diperoleh penggalangan dana untuk proyek dan dalam mata uang apa tujuan tersebut harus dinominasikan. Pastikan jika tujuan Anda ditetapkan antara tanggal, sertakan tanggal target dan akhir ini di bawah Tujuan di crowdfund.

![image](assets/en/109.webp)

#### Perks

Perks sangat membantu dengan crowdfunding Anda. Ini karena perks memberikan orang cara untuk berpartisipasi dalam kampanye Anda. Mereka mengetuk motivasi egois serta motivasi altruistik. Dan mereka memungkinkan Anda mengakses pengeluaran pendukung Anda, bukan hanya dompet filantropis mereka -- Anda bisa menebak mana yang lebih signifikan.

Membuat perk baru terdiri dari bidang berikut;

- Judul
- Harga (tetap, minimum, atau kustom)
- URL Gambar
- Deskripsi
- Inventaris
- ID
- Teks Tombol Beli.
- Aktifkan/Nonaktifkan

Setelah pemilik toko telah mengisi semua bidang perk baru yang akan dibuat, klik simpan, dan Anda akan melihat bahwa bagian Perks dalam crowdfunds sekarang mulai terisi.

![image](assets/en/110.webp)

### BTCPay Server - Point Of Sale

#### Kontribusi

Pemilik toko dapat memilih bagaimana menampilkan Perks, bagaimana mereka disortir, atau bahkan diberi peringkat terhadap perks lainnya. Namun, setelah tujuan Crowdfunds tercapai, pemilik toko mungkin ingin menghentikan aliran donasi ke penggalangan dana ini. Oleh karena itu, dia dapat mengaktifkan "Do not allow additional contributions after reaching the target". Ini akan menghentikan Crowdfund dari menerima donasi.

##### Perilaku Crowdfund

Standar Crowdfund hanya menghitung faktur yang dibuat dengan Crowdfund menuju tujuan. Namun, mungkin ada kasus di mana Pemilik toko ingin semua faktur yang dibuat di toko ini dihitung menuju crowdfund.

#### Opsi Tambahan untuk Kustomisasi

BTCPay Server menawarkan beberapa kustomisasi tambahan. Tambahkan suara, animasi, atau bahkan utas diskusi ke Crowdfund. Pemilik toko juga mungkin mengubah tampilan dan nuansa Crowdfund dengan memasukkan CSS kustom mereka sendiri.

#### Hapus aplikasi ini

Jika pemilik toko ingin sepenuhnya menghapus Crowdfund dari BTCPay Server mereka, di bagian bawah pembaruan Crowdfund pemilik toko dapat Klik pada tombol “Delete this app” untuk sepenuhnya menghancurkan aplikasi Crowdfund mereka. Saat mengklik "Delete this app", BTCPay Server akan meminta konfirmasi dengan mengetik `DELETE` dan mengonfirmasi dengan mengklik tombol Hapus. Setelah menghapus, pemilik toko kembali ke dashboard BTCPay Server.

### BTCPay Server - Tombol Bayar

HTML yang mudah tertanam dan tombol pembayaran yang sangat dapat disesuaikan memungkinkan pemilik toko untuk menerima tip dan donasi. Di bilah menu kiri BTCPay Server, di bawah bagian Plugins, pemilik toko dapat mengklik "Pay Button" dan klik Enable untuk membuat tombol Pembayaran.

#### Pengaturan Umum

Dalam Pengaturan Umum untuk Tombol Pembayaran, pemilik toko dapat mengatur

- Harga standar
- Mata uang default
- Metode pembayaran default
  - Gunakan default toko
  - BTC on-chain
  - BTC Off-chain (Lightning)
  - BTC Off-chain (LNURL-pay)
- Deskripsi checkout
- ID Pesanan

#### Opsi Tampilan

Tombol Bayar BTCPay Server dapat dikonfigurasi untuk sesuai dengan berbagai gaya. Tombol dapat memiliki jumlah tetap atau kustom, baik ditampilkan dengan slider atau tombol tambah dan kurang.

#### Gunakan Modal

Saat membuat tombol pembayaran, pemilik toko dapat memilih perilakunya ketika pelanggan mengkliknya dan menampilkannya dalam modal atau sebagai halaman baru.

**!?Catatan!?**

Peringatan: Tombol pembayaran hanya harus digunakan untuk tip dan donasi

Menggunakan tombol pembayaran untuk integrasi e-commerce tidak disarankan karena informasi relevan pesanan dapat dimodifikasi oleh pengguna. Untuk e-commerce, Anda harus menggunakan Greenfield API kami. Jika toko ini memproses transaksi komersial, kami menyarankan Anda untuk membuat toko terpisah sebelum menggunakan tombol pembayaran.

#### Sesuaikan Teks Tombol Bayar

Secara default, tombol pembayaran BTCPay Server menyatakan "Bayar Dengan BTCPay". Pemilik toko dapat mengatur teks ini sesuai keinginan dan mengubah logo BTCPay Server menjadi milik mereka sendiri. Atur teks dengan menggunakan "Pay Button Text" dan tempel URL gambar di bawah "Pay Button Image URL".

##### Ukuran Gambar

Ukuran gambar pada tombol hanya dapat diatur ke tiga default.

- 146x40px
- 168x46px
- 209x57px

#### Tipe Tombol

BTCPay Server mengetahui tiga keadaan untuk Tombol Pembayaran.

- Jumlah Tetap
  - Harga yang telah ditetapkan sebelumnya ada dalam pengaturan umum tombol.
- Jumlah Kustom
  - Tombol Bayar BTCPay Server memiliki tombol + dan - untuk menetapkan harga kustom.
  - Saat menggunakan jumlah kustom, BTCPay Server akan meminta Min, Max, dan seberapa bertahap harus meningkat.
  - Tombol dapat diatur ke “Gunakan gaya input Sederhana”. Ini menghilangkan tombol +/-.
  - Sesuaikan tombol secara inline di mana tombol dan tombol muncul secara inline.
- Slider
  - Serupa dengan jumlah kustom, namun, secara visual berbeda karena memiliki slider alih-alih tombol +/-.
  - Saat menggunakan Slider, BTCPay Server akan meminta Min, Max, dan seberapa bertahap harus meningkat.

**!?Catatan!?**

Menghapus Tombol Pembayaran dapat dilakukan di bagian atas dalam deskripsi peringatan.

#### Notifikasi Pembayaran

Server IPN (Instant Payment Notification) dimaksudkan untuk webhook dan dapat diisi dengan URL untuk memposting data pembelian.

#### Notifikasi Email

Setiap kali pembayaran terjadi, BTCPay Server dapat memberitahu pemilik toko.

#### Pengalihan Browser

Ketika pelanggan menyelesaikan pembelian, dia akan diarahkan ke tautan ini jika diatur oleh pemilik toko.

#### Opsi Tombol Pembayaran Lanjutan

Tentukan parameter string kueri tambahan yang harus ditambahkan ke halaman checkout setelah faktur dibuat. Misalnya, `lang=da-DK` akan memuat halaman checkout dalam bahasa Denmark secara default.

#### Gunakan Aplikasi sebagai Endpoint

Tautkan langsung tombol pembayaran ke item dalam salah satu aplikasi PoS atau Crowdfund sebelumnya.
Pemilik toko dapat mengklik menu dropdown dan memilih Aplikasi yang diinginkan; setelah Aplikasi dipilih, pemilik toko dapat menambahkan item yang perlu dihubungkan.

#### Kode yang Dihasilkan

Sebagai tombol Pembayaran BTCPay Server yang mudah tertanam HTML, BTCPay Server menampilkan kode yang dihasilkan untuk disalin ke dalam situs web di bagian bawah setelah mengonfigurasi tombol Pembayaran.

Pemilik toko dapat menyalin kode yang dihasilkan ke dalam situs web mereka, dan tombol Pembayaran dari BTCPay Server langsung aktif di situs web mereka.

#### Notifikasi Pembayaran

Server IPN (Instant Payment Notification) dimaksudkan untuk webhook dan dapat diisi dengan URL untuk memposting data pembelian.

#### Notifikasi Email

Kapan pun pembayaran terjadi, BTCPay Server dapat memberitahu pemilik toko.

#### Pengalihan Browser

Ketika pelanggan menyelesaikan pembelian, ia akan diarahkan ke tautan ini jika ditetapkan oleh pemilik toko.

#### Opsi Tombol Pembayaran Lanjutan

Tentukan parameter string kueri tambahan yang harus ditambahkan ke halaman checkout setelah faktur dibuat. Misalnya, `lang=da-DK` akan memuat halaman checkout dalam bahasa Denmark secara default.

#### Gunakan Aplikasi sebagai Endpoint

Tautkan langsung tombol pembayaran ke item dalam salah satu aplikasi PoS atau Crowdfund sebelumnya. Pemilik toko dapat mengklik menu dropdown dan memilih aplikasi yang diinginkan, setelah aplikasi dipilih, pemilik toko dapat menambahkan item yang perlu dihubungkan.

#### Kode yang Dihasilkan

Sebagai tombol Pembayaran BTCPay Server yang mudah tertanam HTML, BTCPay Server menampilkan kode yang dihasilkan untuk disalin ke dalam situs web di bagian bawah setelah mengonfigurasi tombol Pembayaran. Pemilik toko dapat menyalin kode yang dihasilkan ke dalam situs web mereka dan tombol Pembayaran dari BTCPay Server langsung aktif di situs web mereka.

### Ringkasan Keterampilan

Dalam bagian ini Anda telah belajar:

- Bagaimana menggunakan plugin PoS terintegrasi BTCPay Server untuk dengan mudah membuat toko kustom
- Bagaimana menggunakan plugin Crowdfund terintegrasi BTCPay Server untuk dengan mudah membuat aplikasi crowdfund kustom
- Menghasilkan kode untuk tombol bayar kustom menggunakan plugin Tombol Bayar

### Penilaian Pengetahuan

#### Ulasan KA

Apa tiga plugin bawaan yang datang standar dengan BTCPay Server? Dalam beberapa kata, jelaskan bagaimana masing-masing dapat digunakan.

# Mengonfigurasi BTCPay Server

<partId>ff38596c-7de3-5e5c-ba50-9b9edbbbb5eb</partId>

## Pemahaman Dasar tentang Menginstal BTCPay Server di Lingkungan LunaNode

<chapterId>d0a28514-ffcf-529b-9156-29141f0b060a</chapterId>

### Menginstal BTCPay Server di Lingkungan yang Dihosting (LunaNode)

Langkah-langkah ini akan memberikan semua informasi yang diperlukan untuk mulai menggunakan BTCPay Server di LunaNode. Ada banyak opsi tentang bagaimana menerapkan perangkat lunak.
Anda dapat menemukan semua detail BTCPay Server di https://docs.btcpayserver.org.

#### Di Mana Kita Mulai?

Dalam bagian ini, Anda akan mempelajari tentang LunaNode sebagai penyedia hosting, mempelajari langkah pertama menggunakan BTCPay Server Anda, dan belajar bagaimana melanjutkan dengan Lightning Network. Setelah kita telah melalui semua langkah, Anda dapat menjalankan webshop atau platform crowdfund yang menerima Bitcoin!

Ini adalah salah satu dari banyak cara untuk menerapkan BTCPay Server. Baca dokumentasi kami untuk lebih detail,

https://docs.btcpayserver.org.

### Penyebaran BTCPay Server - LunaNode

#### Penyebaran LunaNode

Pertama, kunjungi situs web LunaNode.com, di mana kita akan membuat akun baru. Klik pada "Sign Up" di pojok kanan atas atau gunakan wizard "Get Started" di halaman utama mereka.
![image](assets/en/111.webp)

Setelah Anda membuat akun baru, LunaNode mengirimkan email verifikasi. Setelah Anda memverifikasi akun, dibandingkan dengan Voltage, Anda langsung disajikan untuk menambah saldo akun Anda. Saldo ini diperlukan untuk membayar biaya ruang server dan hosting.

![image](assets/en/112.webp)

#### Tambahkan kredit ke akun LunaNode Anda

Setelah Anda mengklik "Deposit credit", Anda dapat menentukan berapa banyak yang ingin Anda tambahkan ke saldo akun Anda dan bagaimana Anda ingin membayarnya. LunaNode dan BTCPay Server akan menelan biaya antara 10$USD dan 20$USD per bulan.
Dibandingkan dengan Voltage.cloud, Anda memang mendapatkan akses penuh ke Virtual Private Server (VPS dari sini) Anda dan oleh karena itu memiliki lebih banyak kontrol atas server Anda. Setelah Anda membuat akun baru, LunaNode mengirimkan email verifikasi.
Setelah Anda memverifikasi akun, dibandingkan dengan Voltage, Anda sekarang langsung disajikan untuk menambah saldo akun Anda. Saldo ini diperlukan untuk membayar biaya ruang server dan hosting.

#### Bagaimana cara menerapkan server baru?

Dalam panduan ini, kita akan melalui pengaturan dengan membuat serangkaian kunci API dan menggunakan peluncur BTCPay Server yang dibuat oleh LunaNode.

Di dashboard LunaNode Anda, klik API di pojok kanan atas. Ini akan membuka halaman baru. Kita hanya perlu menetapkan Nama untuk kunci API. Sisanya akan diurus oleh LunaNode dan tidak akan dibahas dalam panduan ini. Klik tombol Create API Credential.
Setelah membuat kredensial API, Anda akan mendapatkan rangkaian panjang huruf dan karakter. Ini adalah kunci API Anda.

![image](assets/en/113.webp)

#### Bagaimana cara menerapkan server baru?

Ada 2 bagian dari kredensial ini, kunci API dan ID API; kita akan memerlukan keduanya. Sebelum kita melanjutkan ke langkah selanjutnya, mari buka tab kedua di browser dan kunjungi https://launchbtcpay.lunanode.com/

Di sini Anda akan diminta untuk menyediakan kunci API dan ID API Anda. Ini untuk memverifikasi bahwa Anda yang menyiapkan server baru ini. Kunci API seharusnya masih terbuka di tab sebelumnya; jika Anda menggulir ke bawah di tabel di bawah, Anda akan menemukan ID API.

Kembali ke halaman dengan Launcher, isi bidang dengan kunci API dan ID Anda, lalu klik lanjutkan.

![image](assets/en/114.webp)

Pada langkah selanjutnya, Anda dapat menyediakan nama domain. Jika Anda sudah memiliki domain dan ingin menggunakannya untuk BTCPay Server, pastikan Anda juga menambahkan catatan DNS (Disebut catatan `A`) pada domain Anda. Jika Anda tidak memiliki domain, gunakan domain yang disediakan LunaNode sebagai gantinya (Anda dapat mengubah ini nanti di pengaturan BTCPay Server) dan klik Lanjutkan.

Baca lebih lanjut tentang cara menetapkan atau mengubah catatan DNS untuk BTCPay Server; https://docs.btcpayserver.org/FAQ/Deployment/#how-to-change-your-btcpay-server-domain-name

#### Luncurkan BTCPay Server di LunaNode

Setelah mengambil langkah-langkah sebelumnya, kita dapat menetapkan semua opsi untuk server baru kita. Di sini kita akan memilih Bitcoin (BTC) sebagai mata uang yang didukung; kita dapat menetapkan email untuk mendapatkan notifikasi tentang sertifikat enkripsi untuk tujuan perpanjangan; ini tidak wajib.
Panduan ini bertujuan untuk menyiapkan lingkungan Mainnet (Bitcoin dunia nyata); namun, LunaNode juga memungkinkan Anda untuk mengatur ini ke Testnet atau Regtest untuk tujuan pengembangan. Kami akan membiarkannya pada opsi Mainnet untuk panduan ini.
Pilih implementasi Lightning Anda. LunaNode menawarkan dua implementasi yang berbeda, LND dan Core Lightning. Untuk panduan ini, kami akan memilih LND. Ada perbedaan kecil namun nyata di kedua implementasi; untuk lebih lanjut tentang ini, kami merekomendasikan membaca dokumentasi lengkap; https://docs.btcpayserver.org/LightningNetwork#getting-started-with-btcpay-server-and-core-lightning-cln

![image](assets/en/115.webp)

LunaNode menawarkan beberapa rencana Mesin Virtual (VM). Ini berbeda dalam kisaran harga dan spesifikasi server. Untuk panduan ini, rencana m2 akan cukup; namun, jika Anda telah menandai lebih dari hanya Bitcoin sebagai mata uang, pertimbangkan untuk menggunakan setidaknya m4.

Percepat sinkronisasi blockchain awal; ini opsional dan tergantung pada kebutuhan Anda. Ada opsi lanjutan seperti menetapkan Lightning Alias, menunjuk ke rilis GitHub tertentu, atau menetapkan kunci SSH; tidak satu pun dari ini akan disentuh dalam panduan ini.

Setelah mengisi formulir, Anda harus mengklik Launch VM, dan Lunanode akan mulai membuat VM baru Anda, termasuk BTCPay Server yang terinstal di dalamnya. Proses ini memakan waktu beberapa menit; setelah server Anda siap, LunaNode memberi Anda tautan ke BTCPay Server baru Anda.

Setelah proses pembuatan, klik pada tautan ke BTCPay Server Anda; di sini, Anda akan diminta untuk membuat akun Administrator.

![image](assets/en/116.webp)

### Ringkasan Keterampilan

Dalam bagian ini Anda belajar:

- Membuat dan mendanai akun di LunaNode
- Menggunakan BTCPay Server Launcher untuk membuat server Anda sendiri

### Penilaian Pengetahuan

#### KA Tinjauan Konseptual

Jelaskan beberapa perbedaan antara menjalankan instance BTCPay Server pada VPS dibandingkan dengan membuat akun pada instance yang dihosting.

## Menginstal BTCPay Server pada lingkungan Voltage

<chapterId>11c7d284-b4d2-5542-872c-df9bd9c1491b</chapterId>

Anda akan mengenal Voltage.cloud sebagai penyedia hosting, mempelajari langkah-langkah awal menggunakan BTCPay Server Anda, dan belajar bagaimana berurusan dengan Lightning Network. Setelah kita telah melalui semua langkah, Anda dapat menjalankan webshop atau platform crowdfunding yang menerima Bitcoin!

Ini adalah salah satu dari banyak cara untuk menerapkan BTCPay Server. Baca dokumentasi kami untuk lebih detail,
https://docs.btcpayserver.org.

### Penyebaran BTCPay Server - Voltage.cloud

Pertama, pergi ke situs web Voltage.cloud dan daftar untuk akun baru. Saat membuat akun, Anda dapat mendaftar untuk uji coba gratis 7 hari. Klik pada Sign Up di kanan atas atau gunakan "Try a free 7 day trial" di halaman utama mereka.

![image](assets/en/117.webp)

Setelah Anda membuat akun, klik tombol `NODES` di dashboard Anda. Setelah kita telah memilih Nodes dan membuat node baru, kita akan diperkenalkan dengan node yang ditawarkan Voltage. Karena panduan ini juga akan membahas tentang LightningNetwork, di Voltage, kita pertama harus memilih implementasi Lightning kita sebelum kita membuat BTCPay Server. Klik pada LightningNode.

![image](assets/en/118.webp)
Di sini Anda harus memilih jenis node Lightning yang Anda inginkan. Voltage menawarkan berbagai opsi untuk pengaturan pencahayaan Anda. Ini berbeda ketika dikerahkan dengan, misalnya, LunaNode. Untuk tujuan panduan ini, Lite Node sudah cukup. Baca lebih lanjut tentang perbedaannya di Voltage.cloud.
![image](assets/en/119.webp)

Berikan node Anda sebuah Nama, tetapkan kata sandi, dan amankan kata sandi ini. Jika kata sandi ini hilang, Anda kehilangan akses ke cadangan Anda, dan Voltage tidak dapat memulihkannya. Buat node tersebut, dan Voltage akan menunjukkan progresnya. Voltage telah membuat Lightning Node Anda. Sekarang kita dapat membuat instansi BTCPay Server dan langsung mengakses Lightning Network.

Klik Nodes di kiri atas dashboard Anda. Di sini Anda dapat mengatur bagian selanjutnya dari instansi BTCPay Server Anda. Klik "buat baru" setelah Anda berada di overview nodes. Anda mendapatkan layar serupa seperti sebelumnya. Sekarang bukan Lightning Node, kita memilih BTCPay Server.

Voltage menunjukkan geolokasi BTCPay Server Anda, voltage meng-host di wilayah AS Barat. Di sini Anda juga akan melihat biaya hosting server. Klik Buat dan berikan BTCPay Server Anda sebuah nama. Aktifkan Lightning dan Voltage menunjukkan node Lightning yang dibuat pada langkah sebelumnya. Klik Buat, dan Voltage akan membuat instansi BTCPay Server.

![image](assets/en/120.webp)

Setelah Anda menekan buat, Voltage menampilkan username dan kata sandi default. Ini serupa dengan kata sandi yang Anda tetapkan sebelumnya di Voltage. Klik tombol Login to Account untuk mengarahkan Anda ke BTCPay Server Anda.

Selamat datang di instansi BTCPay Server baru Anda. Karena kita sudah mengatur Lightning dalam proses pembuatan, ini menunjukkan bahwa Lightning sudah diaktifkan!

### Ringkasan Keterampilan

Dalam bab ini Anda telah belajar:

- Membuat akun di Voltage.cloud
- Langkah-langkah untuk menjalankan BTCPay Server bersama dengan node Lightning di akun

### Penilaian Pengetahuan

#### KA Tinjauan Konseptual

Apa beberapa perbedaan kunci antara pengaturan Voltage dan LunaNode?

## Menginstal BTCPay Server pada node Umbrel

<chapterId>3298e292-6476-5fe0-836c-7fa021348799</chapterId>

Di akhir langkah-langkah ini, Anda dapat menerima pembayaran lightning ke toko BTCPay Anda di jaringan lokal. Proses ini juga berlaku jika Anda menjalankan node umbrel di restoran atau bisnis. Jika Anda ingin menghubungkan toko ini ke situs web publik, ikuti Latihan Lanjutan untuk mengekspos node umbrel Anda ke publik.

https://umbrel.com/

![image](assets/en/121.webp)

### BTCPay Server - Penyebaran Umbrel

Setelah node Umbrel Anda sepenuhnya sinkron dengan blockchain Bitcoin, pergi ke Umbrel App Store, dan cari BTCPay Server di bawah Apps.

![image](assets/en/122.webp)

Klik pada BTCPay Server untuk melihat detail Aplikasi. Ketika detailnya terbuka untuk BTCPay Server, bagian kanan bawah menunjukkan persyaratan untuk Aplikasi berjalan dengan baik. Ini menunjukkan bahwa diperlukan Bitcoin dan Lightning node. Jika Anda belum menginstal Lightning Node di Umbrel Anda, klik Install. Proses ini bisa memakan waktu beberapa menit.

![image](assets/en/123.webp)

Setelah menginstal Lightning Node Anda:

1. Klik buka di detail aplikasi atau di Aplikasi di dashboard Umbrels.
2. Klik setup a new node; Anda akan ditunjukkan 24 kata untuk pemulihan node lightning Anda.
3. Tulis kata-kata ini.

![image](assets/en/124.webp)
Umbrel akan meminta verifikasi atas kata-kata yang baru saja dituliskan. Setelah node Lightning disiapkan, kembali ke Umbrel App Store dan temukan BTCPay Server. Klik tombol instalasi, dan Umbrel akan menampilkan jika komponen yang diperlukan telah terpasang dan bahwa BTCPay Server memerlukan akses ke komponen-komponen tersebut. Setelah instalasi, klik Buka di pojok kanan atas detail Aplikasi atau buka BTCPay Server melalui dashboard Umbrel Anda.
Umbrel akan meminta verifikasi atas kata-kata yang baru saja dituliskan.

![image](assets/en/125.webp)

**!?Catatan!?**

Pastikan untuk menyimpan ini di lokasi yang tepat seperti yang telah dipelajari sebelumnya dalam menyimpan kunci.

Setelah node Lightning disiapkan, kembali ke Umbrel App Store dan temukan BTCPay Server. Klik tombol instalasi, dan Umbrel akan menampilkan jika komponen yang diperlukan telah terpasang dan bahwa BTCPay Server memerlukan akses ke komponen-komponen tersebut.

![image](assets/en/126.webp)

Setelah instalasi, klik Buka di pojok kanan atas detail Aplikasi atau buka BTCPay Server melalui dashboard Umbrel Anda.

![image](assets/en/127.webp)

### Ringkasan Keterampilan

Dalam bagian ini Anda telah belajar:

- Langkah-langkah untuk menginstal BTCPay Server dengan fungsi Lightning pada node Umbrel

### Penilaian Pengetahuan

#### KA Tinjauan Konseptual

Bagaimana cara pengaturan di Umbrel berbeda dari dua opsi hosted sebelumnya?

# Kesimpulan

<partId>d72e6fa5-0870-5f00-9143-9466ed22e2bd</partId>



## Evaluasi kursus ini
<chapterId>d90bb93d-b894-551e-9fd6-6855c739a904</chapterId>
<isCourseReview>true</isCourseReview>

## Kesimpulan Kursus

<chapterId>c07ac2a5-f97e-5c57-8a80-4955b48128d4</chapterId>

![image](assets/en/128.webp)

Anda juga seharusnya memiliki pemahaman umum tentang apa itu Bitcoin, bagaimana cara kerjanya, dan bagaimana ia dapat berskala dengan lapisan kedua seperti Lightning Network. Dalam kursus ini, kami secara ekstensif membahas bagaimana siapa pun dapat menggunakan BTCPay Server, dari instalasi awal hingga pembuatan toko dan manajemen invoice yang kompleks, untuk menjadi individu atau pedagang yang berdaulat secara finansial.

Selamat atas penyelesaian kursus ini. Kami berharap Anda menikmati konten ini dan terus menggunakan serta menjelajahi BTCPay Server, dan sebagaimana kami, bersemangat tentang masa depan Bitcoin yang menjanjikan dan komunitas pembangun serta peserta yang terus berkembang.

> **FOSS adalah keniscayaan.**

### Glosarium

| Istilah                                               | Definisi                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Serangan 51%                                          | Tindakan membangun rantai blok terpanjang baru secara sengaja untuk menggantikan blok-blok dalam blockchain. Ini memungkinkan Anda menggantikan transaksi yang telah ditambang ke dalam blockchain. Jenis serangan ini paling mudah dilakukan ketika Anda memiliki mayoritas kekuatan penambangan, itulah sebabnya ini disebut sebagai "Serangan Mayoritas" atau "Serangan 51%".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| AccountKey                                            | Kunci akun untuk rebase                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| AccountKeyPath                                        | Jalur dari akar ke kunci akun yang diprefiks dengan sidik jari kunci publik utama.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Alamat                                                | Alamat Bitcoin mengkodekan informasi yang diperlukan untuk membayar penerima secara ringkas. Sebuah alamat modern terdiri dari rangkaian huruf dan angka yang dimulai dengan bc1 dan terlihat seperti bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4. Alamat adalah singkatan dari skrip penguncian penerima, yang dapat digunakan oleh pengirim untuk menandatangani dana kepada penerima. Kebanyakan alamat mewakili kunci publik penerima atau beberapa bentuk skrip yang mendefinisikan kondisi pengeluaran yang lebih kompleks. Contoh sebelumnya adalah alamat bech32 yang mengkodekan program saksi yang mengunci dana ke hash dari kunci publik (Lihat Pay-to-Witness-Public-Key-Hash). Ada juga format alamat lama yang dimulai dengan 1 atau 3 yang menggunakan pengkodean alamat Base58Check untuk mewakili hash kunci publik atau hash skrip.                                                                    |
| Tipe Alamat                                           | Sebuah alamat dapat mewakili beberapa skrip yang berbeda. Alamat dikodekan dan diberi awalan untuk menyampaikan tipe skrip mereka. Alamat warisan menggunakan Base58, dan ketika alamat warisan adalah hash dari kunci publik, alamat P2PKH, itu dimulai dengan ‘1’. Kurang sering, alamat warisan adalah hash dari skrip, dalam hal ini akan dimulai dengan ‘3’. Saat ini, semua alamat SegWit dikodekan dalam Bech32 dan dimulai dengan awalan ‘bc1’.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Aplikasi                                              | BTCPay Server memiliki plugin yang mungkin berfungsi sebagai aplikasi itu sendiri.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| BIP 329                                               | Ekspor/impor label dompet                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| BIP49                                                 | Mendefinisikan skema derivasi untuk dompet HD menggunakan format serialisasi P2WPKH-nested-in-P2SH (BIP 141) untuk transaksi saksi terpisah.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Alamat Bitcoin                                        | String alfanumerik tempat Anda mengirim bitcoin Anda, sehingga "hidup" di sana sekarang adalah identifikasi, yang terdiri dari rangkaian sekitar 33 huruf dan angka yang digabungkan. Dalam versi protokol saat ini, sebuah alamat dimulai dengan 1, 3, atau b. Memiliki alamat penerima adalah bagian yang diperlukan untuk memulai transaksi bitcoin. Alamat Bitcoin dihasilkan dari kunci publik dan beberapa alamat dapat dihasilkan dari satu set kunci publik untuk meningkatkan privasi. Alamat Bitcoin bertindak seperti alamat email, jika Anda ingin mengirim pesan Anda perlu tahu kemana itu akan pergi, sama halnya dengan bitcoin. Sebelum mengirim transaksi bitcoin, Anda perlu memastikan bahwa alamat penerima akurat karena transaksi bitcoin tidak dapat dibatalkan dan Anda mungkin mengirim bitcoin ke alamat yang tidak dimiliki oleh penerima.                                                   |
| bitcoin versus Bitcoin                                | Bitcoin adalah jaringan moneter, dan bitcoin (huruf kecil) adalah unit moneter di jaringan Bitcoin. Anda menggunakan mata uang bitcoin atau token untuk bertransaksi di jaringan Bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Blok                                                  | Blok adalah struktur data dalam blockchain Bitcoin yang terdiri dari header dan badan transaksi Bitcoin. Blok ditandai dengan timestamp dan berkomitmen pada blok pendahulu (orang tua) tertentu. Ketika di-hash, header blok memberikan bukti kerja yang membuat blockchain menjadi tidak dapat diubah secara probabilistik. Blok harus mematuhi aturan yang diberlakukan oleh konsensus jaringan untuk memperpanjang blockchain. Ketika blok ditambahkan ke blockchain, transaksi yang termasuk dianggap telah mendapatkan konfirmasi pertama mereka.                                                                                                                                                                                                                                                                                                                                                                  |
| Eksplorer Blok                                        | Alat online yang memungkinkan Anda untuk mencari informasi real-time dan historis tentang blockchain, termasuk data terkait blok, transaksi, alamat, dan lainnya.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Hash Blok                                             | Hash blok adalah hash SHA-256 dari data blok, dan biasanya direpresentasikan dalam format heksadesimal. Hash blok dapat diinterpretasikan sebagai angka yang sangat besar. Untuk memenuhi persyaratan Proof-of-Work, hash blok harus berada di bawah ambang batas tertentu. Dengan demikian, semua hash blok dimulai dengan serangkaian nol diikuti oleh string alfanumerik. Beberapa blok memiliki hingga dua puluh nol di depan, sementara blok-blok sebelumnya memiliki sedikitnya delapan. Jumlah nol yang diperlukan kurang lebih menunjukkan kesulitan penambangan pada saat blok tersebut diterbitkan.                                                                                                                                                                                                                                                                                                            |
| Tinggi Blok                                           | Setiap blok diberi nomor secara berurutan, dimulai dari nol.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Hadiah Blok                                           | Terdiri dari subsidi blok (bitcoin yang baru diciptakan) dan jumlah semua biaya transaksi dari transaksi yang termasuk dalam blok tersebut.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Ukuran Blok                                           | Setiap blok memiliki jumlah data terbatas yang dapat dimuat. Data yang tidak muat ke dalam blok tertentu, akan dicatat dalam salah satu blok berikutnya. Dalam hal blok bitcoin, blok tersebut dulunya memiliki ukuran blok 1mb, namun setelah soft fork ukuran blok secara teknis dapat memuat hingga 4mb data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Subsidi Blok                                          | Jumlah bitcoin baru yang dicetak dalam setiap blok. Setiap blok yang diproduksi dan ditambahkan ke blockchain memungkinkan pencipta blok untuk mencetak sejumlah bitcoin baru. Subsidi dimulai dari 50 BTC per blok, dan dipotong setengah setiap 210.000 blok atau kira-kira 4 tahun.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Blockchain                                            | Log terdistribusi, atau basis data, dari semua transaksi Bitcoin. Transaksi dikelompokkan dalam pembaruan diskrit yang disebut blok, terbatas hingga 4 juta unit berat. Blok diproduksi kira-kira setiap 10 menit melalui proses stokastik yang disebut penambangan. Setiap blok mencakup "bukti kerja" yang memerlukan komputasi intensif. Persyaratan bukti kerja digunakan untuk mengatur interval blok dan melindungi blockchain dari serangan untuk menulis ulang sejarah: penyerang perlu mengalahkan bukti kerja yang ada untuk menggantikan blok yang sudah diterbitkan, membuat setiap blok secara probabilistik tidak dapat diubah karena tertimbun di bawah blok-blok berikutnya.                                                                                                                                                                                                                             |
| BTCPay Server Vault                                   | Untuk keseimbangan optimal antara kemudahan penggunaan, keamanan, dan privasi, disarankan untuk menggunakan BTCPay Server Wallet dengan hardware wallet. BTCPay Vault dibangun untuk menjembatani Hardware Wallet dan BTCPay Server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Masalah Jenderal Byzantine                            | Masalah teori permainan yang menggambarkan kesulitan pihak-pihak terdesentralisasi dalam mencapai konsensus tanpa mengandalkan pihak pusat yang dipercaya. Nama ini berasal dari skenario beberapa jenderal yang mengepung Byzantium. Mereka telah mengepung kota, tetapi mereka harus secara kolektif memutuskan kapan akan menyerang. Jika semua jenderal menyerang pada saat yang sama, mereka akan menang, tetapi jika mereka menyerang pada waktu yang berbeda, mereka akan kalah. Para jenderal tidak memiliki saluran komunikasi yang aman satu sama lain karena pesan apa pun yang mereka kirim atau terima mungkin telah dis intercept atau dikirim secara menipu oleh pembela Byzantium. Bagaimana cara jenderal-jenderal tersebut berorganisasi untuk menyerang pada saat yang sama?                                                                                                                          |
| Sensor                                                | Kontrol atas informasi apa yang dapat ditransmisikan ke massa. Dalam konteks bitcoin, sensor adalah tentang kemampuan untuk menghentikan transaksi oleh pihak ketiga.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Kembalian                                             | Bagian dari UTXOs yang dikembalikan ke dompet pengirim, biasanya melalui alamat yang berbeda. Jumlahnya adalah jumlah input dikurangi jumlah yang dibelanjakan dan biaya transaksi.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Child Pays For Parent (CPFP)                          | Teknik peningkatan biaya di mana pengguna menghabiskan output dari transaksi yang belum dikonfirmasi dengan biaya rendah dalam transaksi anak dengan biaya tinggi untuk mendorong penambang agar memasukkan kedua transaksi tersebut dalam satu blok.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Coinbase Transaction                                  | Transaksi pertama dalam setiap blok yang mendistribusikan hadiah blok dan biaya transaksi kepada siapa pun yang menambang blok tersebut.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Coincidence of Wants                                  | Fenomena ekonomi di mana dua pihak masing-masing memiliki barang yang diinginkan oleh pihak lain, sehingga mereka bertukar barang tersebut langsung tanpa media moneter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Cold Storage                                          | Cara mengelola data tanpa terhubung ke internet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Cold Wallet                                           | Jenis dompet bitcoin yang menyimpan kunci privat Anda secara offline, biasanya pada perangkat fisik. Juga dikenal sebagai hardware wallet, dan melindungi bitcoin digital Anda dari peretas online dengan menggunakan perangkat mirip flash drive yang tidak terhubung ke internet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Command Line Interface (CLI)                          | Berinteraksi dengan perangkat atau program komputer dengan perintah dari pengguna atau klien, dan respons dari perangkat atau program, dalam bentuk baris teks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Commitment Transaction                                | Transaksi komitmen adalah transaksi Bitcoin, ditandatangani oleh kedua mitra saluran, yang mengkodekan saldo terbaru dari sebuah saluran. Setiap kali pembayaran baru dilakukan atau diteruskan menggunakan saluran, saldo saluran akan diperbarui, dan transaksi komitmen baru akan ditandatangani oleh kedua pihak. Penting, dalam saluran antara Alice dan Bob, baik Alice maupun Bob menyimpan versi mereka sendiri dari transaksi komitmen, yang juga ditandatangani oleh pihak lain. Pada titik mana pun, saluran dapat ditutup oleh Alice atau Bob jika mereka mengajukan transaksi komitmen mereka ke blockchain Bitcoin. Mengajukan transaksi komitmen yang lebih lama (ketinggalan zaman) dianggap sebagai kecurangan (yaitu, pelanggaran protokol) dalam Lightning Network dan dapat dikenai sanksi oleh pihak lain, mengklaim semua dana dalam saluran untuk diri mereka sendiri, melalui transaksi penalti. |
| Confirmation                                          | Setelah transaksi dimasukkan dalam blok, transaksi tersebut memiliki satu konfirmasi. Segera setelah blok lain ditambang di blockchain, transaksi memiliki dua konfirmasi, dan seterusnya. Enam atau lebih konfirmasi dianggap bukti yang cukup bahwa transaksi tidak dapat dibalikkan.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Crowdfund (CF)                                        | Plugin bawaan dari BTCPay Server yang memungkinkan pemilik toko untuk dengan mudah membuat situs web penggalangan dana khas. Mereka dapat dengan mudah menetapkan tujuan, membuat imbalan untuk kontribusi, dan menyesuaikannya dengan kebutuhan mereka.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Cryptography                                          | Sistem khusus, di mana pesan asli diubah sehingga hanya penerima yang dimaksud yang dapat menerimanya.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Dashboard                                             | Halaman utama dari BTCPay Server. Ini memberikan gambaran umum dari semua aktivitas untuk sebuah toko, ditampilkan melalui sejumlah ringkasan.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Demo                                                  | Merujuk pada lingkungan virtual tempat demo perangkat lunak berlangsung.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Deployment                                            | Penyebaran perangkat lunak adalah semua aktivitas yang membuat sistem perangkat lunak tersedia untuk digunakan. Proses penyebaran umumnya terdiri dari beberapa aktivitas yang saling terkait dengan kemungkinan transisi di antara mereka.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Jalur Turunan                                         | Sebuah data yang memberitahu dompet Hierarchical Deterministic (HD) bagaimana cara menurunkan kunci spesifik dalam pohon kunci. Jalur turunan digunakan sebagai standar Bitcoin dan diperkenalkan bersama dengan dompet HD sebagai bagian dari BIP 32.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Penyesuaian Kesulitan                                 | Penyesuaian terhadap target kesulitan, setiap 2016 blok (sekitar dua minggu) untuk mencoba dan memastikan bahwa blok ditambang setiap 10 menit sekali rata-rata. Ini menciptakan waktu yang konsisten antara blok dan penerbitan bitcoin baru ke dalam jaringan (melalui hadiah blok) secara konsisten.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Target Kesulitan                                      | Digunakan dalam penambangan, ini adalah angka yang harus di bawah hash blok agar blok tersebut dapat ditambahkan ke blockchain.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Tanda Tangan Digital                                  | Tanda tangan digital adalah skema matematis untuk memverifikasi keaslian dan integritas pesan atau dokumen digital. Ini dapat dilihat sebagai komitmen kriptografis di mana pesan tidak disembunyikan.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Dapat Dibagi                                          | Sifat dari sebuah barang yang dapat dipecah menjadi jumlah yang lebih kecil tanpa kehilangan nilai. Karena transaksi ekonomi sering terjadi dalam jumlah yang bervariasi, mata uang harus dapat dibagi untuk digunakan secara luas dalam ekonomi.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Docker                                                | Perangkat lunak yang mengemas perangkat lunak ke dalam unit standar yang disebut kontainer yang memiliki segala yang dibutuhkan perangkat lunak untuk berjalan termasuk perpustakaan, alat sistem, kode, dan runtime.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Double-Spend                                          | Hasil dari berhasil menghabiskan uang lebih dari satu kali. Bitcoin melindungi terhadap pengeluaran ganda dengan memverifikasi bahwa setiap transaksi yang ditambahkan ke blockchain mematuhi aturan konsensus; ini berarti memeriksa bahwa input untuk transaksi belum pernah dihabiskan sebelumnya.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Tahan Lama                                            | Sifat uang, di mana mata uang dapat mempertahankan keadaan aslinya dari waktu ke waktu dan menahan penggunaan berulang. Mata uang yang tahan lama harus dapat bertahan dari kerusakan potensial.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Electrum                                              | Electrum adalah salah satu dompet Bitcoin paling populer, dibuat pada tahun 2011.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Kunci Publik Terluas (Xpub)                           | Kunci publik terluas juga dikenal sebagai Xpub, sebuah kunci publik yang berfungsi sebagai induk untuk kunci yang diturunkan dari xpub sebagai fitur dari Dompet HD. Xpub ini adalah standar yang diperkenalkan dalam BIP 32. Dompet menggunakannya di belakang layar untuk menurunkan kunci publik. Berbagi Xpub tidak disarankan, dana Anda tidak akan berisiko langsung dipindahkan, xpub tidak dapat menurunkan kunci privat. Manfaat berbagi xpub mungkin untuk tujuan penggalangan dana di BTCPay Server. Xpub dibagikan melalui sarana online, sementara kunci privat tetap offline di HWW.                                                                                                                                                                                                                                                                                                                       |
| F.U.D.                                                | Singkatan dari Fear, uncertainty and doubt; Biasanya dipicu secara sengaja untuk menempatkan pesaing dalam posisi yang tidak menguntungkan.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Biaya                                                 | Dalam konteks Lightning Network, node akan membebankan biaya routing untuk meneruskan pembayaran pengguna lain. Setiap node dapat menetapkan kebijakan biaya mereka sendiri yang akan dihitung sebagai jumlah dari base_fee tetap dan fee_rate yang bergantung pada jumlah pembayaran. Dalam konteks Bitcoin, pengirim transaksi membayar biaya transaksi kepada penambang untuk memasukkan transaksi dalam blok. Biaya transaksi Bitcoin tidak termasuk biaya dasar dan bergantung secara linier pada bobot transaksi, tetapi tidak pada jumlahnya.                                                                                                                                                                                                                                                                                                                                                                     |
| Fiat                                                  | Mata uang yang dikeluarkan oleh pemerintah yang tidak didukung oleh komoditas seperti emas.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Finite                                                | Merujuk pada pasokan Bitcoin yang terbatas.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Fork                                                  | Perubahan pada protokol atau potongan kode. Fork biasanya diperkenalkan untuk meningkatkan sebuah proyek. Dalam komunitas sumber terbuka, fork ada karena banyak individu memilih untuk mengunduh dan menjalankan perangkat lunak yang sama pada waktu yang berbeda dan tidak selalu memperbarui. Jika dua pengguna mengunduh dan menjalankan versi 1 dari sebuah perangkat lunak, dan hanya satu pengguna yang memperbarui ketika versi 2 dirilis, pengguna yang memperbarui tersebut menjalankan fork dari versi 1.                                                                                                                                                                                                                                                                                                                                                                                                    |
| Funding Transaction                                   | Transaksi yang digunakan untuk membuka saluran pembayaran. Nilai (dalam bitcoin) dari transaksi pendanaan adalah kapasitas tepat dari saluran pembayaran. Output dari transaksi pendanaan adalah skrip multisignature 2-dari-2 (multisig) di mana setiap mitra saluran mengontrol satu kunci. Karena sifat multisignya, hanya dapat dihabiskan oleh kesepakatan bersama antara mitra saluran. Akhirnya akan dihabiskan oleh salah satu transaksi komitmen atau oleh transaksi penutupan.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Fungible                                              | Menjadi sesuatu (seperti uang atau komoditas) yang sifatnya sedemikian rupa sehingga satu bagian atau kuantitas dapat digantikan dengan bagian atau kuantitas yang sama dalam membayar utang atau menyelesaikan akun.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Gap Limit                                             | Merujuk pada jumlah standar alamat publik yang diperiksa untuk transaksi di blockchain untuk menghitung saldo akun. Transaksi yang diterima di alamat di luar batas gap alamat tidak terdeteksi.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Genesis Block                                         | Blok pertama dalam blockchain Bitcoin. Satoshi Nakamoto, pencipta Bitcoin, menambang blok Genesis pada 3 Januari 2009 dan menyertakan headline Financial Times hari itu, “Chancellor on brink of second bailout for banks.”                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Github                                                | Platform dan layanan berbasis cloud untuk pengembangan perangkat lunak dan kontrol versi menggunakan Git, memungkinkan pengembang untuk menyimpan dan mengelola kode mereka.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Gossip Protocol                                       | Node LN mengirim dan menerima informasi tentang topologi Lightning Network melalui pesan gossip yang ditukar dengan peer mereka. Protokol gossip terutama didefinisikan dalam BOLT #7 dan mendefinisikan format dari pesan node_announcement, channel_announcement, dan channel_update. Untuk mencegah spam, pesan pengumuman node hanya akan diteruskan jika node sudah memiliki saluran, dan pesan pengumuman saluran hanya akan diteruskan jika transaksi pendanaan saluran telah dikonfirmasi oleh jaringan Bitcoin. Biasanya, node Lightning terhubung dengan mitra saluran mereka, tetapi tidak masalah untuk terhubung dengan node Lightning lainnya untuk memproses pesan gossip.                                                                                                                                                                                                                                |
| Gresham's Law                                         | Hukum yang menyatakan bahwa “uang buruk mengusir uang baik”. Dengan kata lain, dalam ekonomi di mana dua mata uang digunakan, individu akan menghabiskan uang buruk, yang terus menerus menurun nilainya, dan menyimpan uang baik, yang mempertahankan nilainya. Dengan demikian, uang buruk akan mendominasi dalam hal sirkulasi dan penggunaan dalam transaksi sehari-hari, sementara uang baik akan mendominasi dalam hal tabungan dan investasi jangka panjang.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Halving                                               | Sebuah peristiwa yang mengurangi tingkat penerbitan bitcoin menjadi setengah setiap 210.000 blok (sekitar empat tahun).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Hard Fork                                             | Perubahan konsensus yang tidak kompatibel dengan versi sebelumnya. Ketidakkompatibelan ke belakang terjadi ketika perilaku yang sebelumnya tidak valid dibuat valid. Untuk mempertahankan konsensus melalui hard fork, semua node harus diperbarui. Jika tidak, node lama akan menolak transaksi atau blok sebagai tidak valid menurut aturan lama, sementara node yang diperbarui akan menerimanya sebagai valid. Untuk alasan ini, hard fork dihindari sebisa mungkin dalam Bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Hardware Wallet (HWW)                                 | Jenis khusus dompet Bitcoin yang menyimpan kunci privat pengguna dalam perangkat keras yang aman.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Hash Function                                         | Fungsi hash kriptografi adalah algoritma matematika yang memetakan data berukuran sembarang ke string bit berukuran tetap (hash) dan dirancang sebagai fungsi satu arah, yaitu, fungsi yang sulit untuk diinvert. Satu-satunya cara untuk merekonstruksi data input dari output fungsi hash kriptografi ideal adalah dengan mencoba pencarian brute-force dari input yang mungkin untuk melihat apakah mereka menghasilkan kecocokan.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Hash Rate                                             | Ukuran berapa banyak hash yang dihasilkan oleh penambang secara kumulatif per detik di jaringan Bitcoin. Satu hash adalah upaya untuk menciptakan Proof-of-Work untuk sebuah blok.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Hot Wallet                                            | Perangkat dengan koneksi eksternal, terutama ke internet. Hot wallet adalah dompet Bitcoin yang terhubung ke internet. Dompet ini lebih nyaman untuk pengeluaran sehari-hari, tetapi tidak seaman opsi penyimpanan dingin karena berinteraksi dengan internet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Initial Block Download (IBD)                          | Proses membangun blockchain Bitcoin dari awal. Ketika node baru disiapkan dan bergabung dengan jaringan, ia terhubung ke node lain dan meminta blok. Node baru ini memproses blok-blok tersebut dan membangun blockchain sampai ia terkini dan sinkron dengan jaringan.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Invoice                                               | Dokumen komersial yang dikeluarkan oleh penjual kepada pembeli yang berkaitan dengan transaksi penjualan dan menunjukkan produk, kuantitas, dan harga yang disepakati untuk produk atau layanan yang telah disediakan penjual kepada pembeli.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Know Your Customer (KYC)                              | Undang-undang yang dimaksudkan untuk mencegah institusi keuangan digunakan untuk transfer uang ilegal dengan mewajibkan semua akun keuangan dapat diidentifikasi ke individu atau organisasi.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Layer 2                                               | Jaringan yang dibangun di atas blockchain, misalnya, Lightning Network.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Legacy Address                                        | Alamat legacy menggunakan Base58, dan ketika alamat legacy adalah hash dari kunci publik, alamat P2PKH, ia dimulai dengan ‘1’.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Lightning Network                                     | Protokol di atas Bitcoin. Ini menciptakan jaringan saluran pembayaran yang memungkinkan pengiriman pembayaran tanpa kepercayaan melalui jaringan dengan bantuan HTLC dan onion routing. Komponen lain dari Lightning Network adalah protokol gossip, lapisan transport, dan permintaan pembayaran.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Liquidity                                             | Ukuran beberapa fitur buku pesanan aset tertentu dalam pasar tertentu. Likuiditas adalah indikator seberapa besar dampak pasar yang akan dimiliki oleh pesanan besar terhadap harga aset. Aset dengan likuiditas lebih memiliki kedalaman buku pesanan yang lebih dalam. Ini berarti bahwa ia akan dapat menyerap lebih banyak pesanan dengan pergerakan harga yang lebih kecil.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Rantai Terpanjang                                     | Rantai blok yang membutuhkan usaha terbanyak untuk dibangun. Dinamakan demikian karena secara intuitif blockchain yang memiliki lebih banyak blok di dalamnya akan membutuhkan lebih banyak energi untuk dibangun dibandingkan dengan rantai yang memiliki lebih sedikit blok, tetapi lebih akuratnya adalah rantai yang membutuhkan lebih banyak kerja untuk diproduksi, sehingga nama yang lebih baik mungkin adalah "rantai terberat."                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Rantai Utama                                          | Dalam konteks Lightning Network ini merujuk ke Jaringan Bitcoin                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Media Pertukaran                                      | Sejenis barang yang memfasilitasi pertukaran barang dan jasa lain dalam sebuah ekonomi. Secara historis, item seperti cangkang, manik-manik, dan emas digunakan sebagai media pertukaran.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Mempool                                               | Singkatan dari "memory pool," ini adalah penyimpanan sementara untuk transaksi yang telah diterima oleh sebuah node.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Penambang                                             | Sebuah node yang terlibat dalam proses membangun blockchain dengan menambahkan blok baru melalui proses hashing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Penambangan                                           | Proses membangun sebuah blok dari transaksi Bitcoin terbaru dan kemudian menyelesaikan masalah komputasi yang diperlukan sebagai bukti kerja. Ini adalah proses di mana ledger Bitcoin bersama (yaitu, blockchain Bitcoin) diperbarui dan dengan cara transaksi baru dimasukkan ke dalam ledger. Ini juga proses di mana bitcoin baru dikeluarkan. Setiap kali blok baru dibuat, node penambang akan menerima bitcoin baru yang dibuat dalam transaksi coinbase dari blok tersebut.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Multitanda tangan (multisig)                          | Skrip yang membutuhkan lebih dari satu tanda tangan untuk mengizinkan pengeluaran. Saluran pembayaran selalu dikodekan sebagai alamat multisig yang membutuhkan satu tanda tangan dari setiap mitra saluran pembayaran. Dalam kasus standar saluran pembayaran dua pihak, alamat multisig 2-dari-2 digunakan.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Node                                                  | Komputer yang berpartisipasi dalam jaringan. Khususnya jaringan Bitcoin atau Lightning.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Output                                                | Paket bitcoin yang dibuat dalam transaksi bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Kunci Output                                          | Sekumpulan persyaratan yang ditempatkan pada sebuah output. Persyaratan ini harus dipenuhi untuk dapat menggunakan output dalam transaksi. Contoh paling umum adalah persyaratan sederhana memiliki kunci privat.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Alamat P2SH                                           | Alamat P2SH adalah pengkodean Base58Check dari hash 20-byte dari sebuah skrip. Alamat P2SH dimulai dengan "3." Alamat P2SH menyembunyikan semua kompleksitas, sehingga pengirim pembayaran tidak melihat skripnya.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Alamat P2WPKH                                         | Format alamat "native SegWit v0", alamat P2WPKH dikodekan bech32 dan dimulai dengan "bc1q".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Alamat P2WSH                                          | Format alamat skrip "native Segwi v0", alamat P2WSH dikodekan bech32 dan dimulai dengan "bc1q".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Transaksi Bitcoin yang Ditandatangani Sebagian (PSBT) | Standar Bitcoin yang memfasilitasi portabilitas transaksi yang belum ditandatangani, yang memungkinkan beberapa pihak untuk dengan mudah menandatangani transaksi yang sama. Ini paling berguna ketika beberapa pihak ingin menambahkan input ke transaksi yang sama. PSBT diperkenalkan oleh BIP 174, dan memungkinkan pengguna untuk lebih mudah menandatangani transaksi pada perangkat penyimpanan dingin dan kemudian menyiarkan transaksi yang telah ditandatangani dari perangkat yang terhubung ke internet.                                                                                                                                                                                                                                                                                                                                                                                                     |
| Penentuan Jalur                                       | Proses menemukan jalur pembayaran dari sumber ke tujuan dalam Lightning Network.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Pay-to-Public-Key-Hash (P2PKH)                        | P2PKH adalah jenis output yang mengunci bitcoin ke hash dari sebuah kunci publik. Output yang dikunci oleh skrip P2PKH dapat dibuka (dibelanjakan) dengan menyajikan kunci publik yang cocok dengan hash dan tanda tangan digital yang dibuat oleh kunci privat yang sesuai.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Pay-to-Script-Hash (P2SH)                             | P2SH adalah jenis output yang serbaguna yang memungkinkan penggunaan Skrip Bitcoin yang kompleks. Dengan P2SH, skrip kompleks yang menjelaskan kondisi untuk membelanjakan output (skrip penebusan) tidak disajikan dalam skrip penguncian. Sebaliknya, nilai dikunci ke hash dari sebuah skrip, yang harus disajikan dan dipenuhi untuk membelanjakan output.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Pay-to-Taproot (P2TR)                                 | Diaktifkan pada November 2021, Taproot adalah jenis output baru yang mengunci bitcoin ke pohon kondisi pengeluaran, atau satu kondisi akar tunggal.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Pay-to-Witness-Public-Key-Hash (P2WPKH)               | P2WPKH adalah ekuivalen SegWit dari P2PKH, menggunakan saksi terpisah. Tanda tangan untuk membelanjakan output P2WPKH ditempatkan di pohon saksi alih-alih bidang ScriptSig.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Pay-to-Witness-Script-Hash (P2WSH)                    | P2WSH adalah ekuivalen SegWit dari P2SH, menggunakan saksi terpisah. Tanda tangan dan skrip untuk membelanjakan output P2WSH ditempatkan di pohon saksi alih-alih bidang ScriptSig.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Payjoin                                               | Jenis transaksi Bitcoin khusus di mana baik pengirim maupun penerima menyumbangkan input untuk memecah heuristik kepemilikan input bersama, sebuah asumsi yang digunakan untuk mengurangi privasi dari pengguna bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Saluran Pembayaran                                    | Hubungan keuangan antara dua node di Lightning Network, dibuat menggunakan transaksi bitcoin yang membayar alamat multisignature. Mitra saluran dapat menggunakan saluran untuk mengirim bitcoin bolak-balik antara satu sama lain tanpa harus mencatat semua transaksi di blockchain Bitcoin. Dalam saluran pembayaran yang tipikal hanya dua transaksi, transaksi pendanaan dan transaksi komitmen, yang ditambahkan ke blockchain. Pembayaran yang dikirim melintasi saluran tidak dicatat di blockchain dan dikatakan terjadi "off-chain."                                                                                                                                                                                                                                                                                                                                                                           |
| Permintaan Pembayaran                                 | Fitur yang memungkinkan pemilik toko BTCPay untuk membuat faktur berumur panjang. Dana yang dibayarkan ke permintaan pembayaran menggunakan kurs tukar pada saat pembayaran. Ini memungkinkan pengguna untuk melakukan pembayaran sesuai keinginan mereka tanpa harus menegosiasikan atau memverifikasi kurs tukar dengan pemilik toko pada saat pembayaran.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Pembayaran                                            | Fungsionalitas pembayaran terikat ke Pembayaran Tarik. Fitur ini memungkinkan Anda memproses pembayaran tarik (pengembalian dana, pembayaran gaji, atau penarikan).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Plugin                                                | Add-on perangkat lunak yang dipasang pada program, meningkatkan kemampuannya.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Point Of Sale (PoS)                                   | Plugin bawaan dari BTCPay Server yang memungkinkan pemilik toko untuk membuat webshop langsung dari BTCPay Server. Pemilik toko tidak memerlukan solusi ecommerce pihak ketiga untuk menjalankan webshop.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Portabel                                              | Kemampuan suatu barang untuk diangkut dengan mudah melintasi ruang. Portabilitas adalah fitur penting dari uang yang baik; agar uang dapat diadopsi secara luas, dan oleh karena itu dapat digunakan, uang tersebut harus dapat bergerak lintas batas, antar individu, dan sepanjang jarak dengan relatif mudah.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Proof Of Work (PoW)                                   | Data yang memerlukan perhitungan signifikan untuk ditemukan, dan dapat dengan mudah diverifikasi oleh siapa saja untuk membuktikan jumlah pekerjaan yang diperlukan untuk menghasilkannya. Dalam Bitcoin, penambang harus menemukan solusi numerik untuk algoritma SHA-256 yang memenuhi target seluruh jaringan, yang disebut target kesulitan.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Pseudonim                                             | Nama palsu yang digunakan oleh individu untuk melindungi identitas mereka atau membangun reputasi terpisah dari identitas asli mereka. Kunci publik digunakan untuk memungkinkan pengguna Bitcoin menerima bitcoin sambil tetap pseudonim terhadap blockchain.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Kriptografi Kunci Publik                              | Melibatkan sepasang kunci yang dikenal sebagai kunci publik dan kunci pribadi, yang dikaitkan dengan entitas yang perlu mengautentikasi identitasnya secara elektronik atau untuk menandatangani atau mengenkripsi data. Kunci publik dipublikasikan dan kunci pribadi yang sesuai disimpan secara rahasia. Data yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci pribadi yang sesuai.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Kunci Publik/Privat                                   | Pasangan kunci yang digunakan dalam kriptografi kunci publik. Kunci publik dibagikan dengan orang lain secara terbuka, dan dapat dipikirkan sebagai nomor akun, sementara kunci pribadi disimpan secara rahasia dan dapat dipikirkan sebagai kata sandi.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Pembayaran Tarik                                      | Secara tradisional, untuk melakukan pembayaran Bitcoin, penerima membagikan alamat bitcoin mereka dan pengirim kemudian mengirim uang ke alamat ini. Sistem seperti ini disebut pembayaran dorong karena pengirim yang memulai pembayaran sementara penerima mungkin tidak tersedia, secara efektif mendorong pembayaran ke penerima. Alih-alih skenario tipikal pengirim "mendorong" pembayaran, pengirim memungkinkan penerima untuk menarik pembayaran pada waktu yang dianggap cocok oleh penerima.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Lubang Kelinci                                        | Referensi ke Alice In Wonderland di mana pahlawan memulai petualangan dengan memasuki lubang kelinci. Dalam Bitcoin, ini merujuk pada topik yang tampaknya tidak ada habisnya yang seseorang jelajahi dan lihat dalam cahaya baru setelah mereka mulai memahami Bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Menerima                                              | Proses menerima bitcoin yang dikirim ke alamat yang disediakan.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Mendaftar                                             | Proses membuat akun atau mendaftar untuk layanan yang biasanya dilakukan dengan memilih nama pengguna dan kata sandi.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Ganti Dengan Biaya (RBF)                              | Transaksi Bitcoin dapat ditandai sebagai RBF untuk memungkinkan pengirim mengganti transaksi ini dengan transaksi serupa lainnya yang membayar biaya lebih tinggi. Mekanisme ini ada untuk memungkinkan pengguna merespons jika jaringan menjadi padat dan biaya naik secara tak terduga.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Repositori                                            | Dalam sistem kontrol versi, repositori adalah struktur data yang menyimpan metadata untuk satu set file atau struktur direktori. Tergantung pada apakah sistem kontrol versi yang digunakan adalah terdistribusi, seperti Git atau Mercurial, atau terpusat, seperti Subversion, CVS, atau Perforce, seluruh set informasi dalam repositori mungkin diduplikasi di sistem setiap pengguna atau mungkin dipelihara di satu server. Beberapa metadata yang dimiliki repositori termasuk, di antara lain, catatan historis perubahan dalam repositori, satu set objek commit, dan satu set referensi ke objek commit, yang disebut kepala.                                                                                                                                                                                                                                                                                  |
| Rescan                                                | Proses pemindaian ulang kondisi saat ini dari set UTXO untuk koin yang dimiliki oleh skema derivasi yang telah dikonfigurasi sebelumnya.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Revokation Key                                        | Setiap Revocable Sequence Maturity Contract (RSMC) mengandung dua kunci pembatalan. Setiap mitra kanal mengetahui satu kunci pembatalan. Dengan mengetahui kedua kunci pembatalan, output dari RSMC dapat dihabiskan dalam batas waktu yang telah ditentukan sebelumnya. Saat menegosiasikan keadaan kanal baru, kunci pembatalan lama dibagikan, dengan demikian "membatalkan" keadaan lama. Kunci pembatalan digunakan untuk mencegah mitra kanal menyiarkan keadaan kanal lama.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Routing                                               | Proses menggunakan jalur Lightning Network untuk melakukan pembayaran.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Routing Fees                                          | Dalam Lightning Network, biaya yang dikenakan untuk meneruskan pembayaran pengguna lain. Node individu dapat menetapkan kebijakan biaya mereka sendiri yang akan dihitung sebagai jumlah dari base_fee tetap dan fee_rate yang bergantung pada jumlah pembayaran.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Salability                                            | Kemudahan di mana suatu barang dapat dijual di pasar kapan pun pemiliknya menginginkan, dengan kerugian terkecil dalam harganya.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Satoshi (sat)                                         | Satoshi adalah unit terkecil (denominasi) bitcoin yang dapat dicatat di blockchain. Satu satoshi adalah 1/100 juta (0.00000001) dari satu bitcoin dan dinamai setelah pencipta Bitcoin, Satoshi Nakamoto.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Satoshi Nakamoto                                      | Nama yang digunakan oleh orang atau kelompok orang yang merancang Bitcoin dan menciptakan implementasi referensi aslinya. Sebagai bagian dari implementasi, mereka juga merancang database blockchain pertama. Dalam prosesnya, mereka adalah yang pertama untuk menyelesaikan masalah double-spending untuk mata uang digital. Identitas asli mereka masih belum diketahui.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Satoshi Per Byte                                      | Satuan untuk mengukur prioritas transaksi, didefinisikan oleh biaya transaksi dalam satoshi dibagi dengan ukuran transaksi dalam byte.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Satoshi Per Verabyte                                  | Konsep serupa dengan Satoshi Per Byte, tetapi untuk alamat baru yang menggunakan Segwit. Sama dengan ukuran transaksi dalam unit Berat dibagi dengan 4. Unit Berat dihitung dengan mengambil ukuran transaksi (tanpa saksi) dikali 3, ditambah dengan ukuran transaksi termasuk saksi.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Scarcity                                              | Sifat dari suatu barang yang tidak dapat direplikasi tanpa biaya. Kelangkaan tidak tergantung pada jumlah unit barang yang ada, tetapi lebih pada biaya untuk memproduksi lebih banyak unit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Script                                                | Bitcoin menggunakan sistem scripting untuk transaksi yang disebut Bitcoin Script. Menyerupai bahasa pemrograman Forth, script ini sederhana, berbasis tumpukan, dan diproses dari kiri ke kanan. Script ini sengaja dibuat tidak lengkap Turing, tanpa loop atau rekursi.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Seed Phrase                                           | Daftar kata yang menyimpan semua informasi yang diperlukan untuk memulihkan dana Bitcoin secara on-chain. Perangkat lunak dompet biasanya akan menghasilkan frasa benih dan menginstruksikan pengguna untuk menuliskannya di atas kertas. Jika komputer pengguna rusak atau hard drive mereka menjadi korup, mereka dapat mengunduh perangkat lunak dompet yang sama lagi dan menggunakan cadangan kertas untuk mendapatkan bitcoin mereka kembali.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Segregated Witness (SegWit)                           | Segregated Witness (SegWit) adalah peningkatan pada protokol Bitcoin yang diperkenalkan pada tahun 2017 yang menambahkan bidang saksi baru untuk tanda tangan dan bukti otorisasi transaksi lainnya. Bidang saksi baru ini dikecualikan dari perhitungan ID transaksi, yang menyelesaikan sebagian besar kelas malleability transaksi pihak ketiga. Segregated Witness diterapkan sebagai soft fork dan merupakan perubahan yang secara teknis membuat aturan protokol Bitcoin lebih restriktif.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Self-Sovereignty                                      | Model untuk mengelola identitas digital di mana individu atau bisnis memiliki kepemilikan tunggal atas kemampuan untuk mengontrol akun dan data pribadi mereka.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Send                                                  | Proses memindahkan bitcoin ke sebuah alamat.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Sensitivity Mode                                      | Diaktifkan melalui toggle di pengaturan toko, aktivasi mengakibatkan nilai numerik (mis., jumlah bitcoin) menjadi tersembunyi di semua tampilan.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Server Settings                                       | Pengaturan dalam BTCPay Server yang berlaku untuk seluruh server (berbeda dengan Store Settings yang cakupannya terbatas pada satu toko saja).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| SHA-256                                               | Fungsi hash kriptografi. Merupakan anggota dari keluarga fungsi hash yang disebut Secure Hashing Algorithm (SHA) functions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Shopify                                               | Perusahaan multinasional e-commerce Kanada yang berpusat di Ottawa, Ontario. Shopify adalah nama dari platform e-commerce proprieternya untuk toko online dan sistem titik penjualan ritel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| SMTP                                                  | Simple Mail Transfer Protocol adalah protokol komunikasi standar Internet untuk transmisi surat elektronik.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Soft Fork                                             | Peningkatan protokol yang kompatibel ke depan dan ke belakang, sehingga memungkinkan node lama dan node baru untuk terus menggunakan rantai yang sama.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Software Stack                                        | Dalam komputasi, solution stack atau software stack adalah sekumpulan subsistem atau komponen perangkat lunak yang diperlukan untuk menciptakan platform lengkap sehingga tidak diperlukan perangkat lunak tambahan untuk mendukung aplikasi.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Store                                                 | Toko dalam BTCPay Server dapat dilihat sebagai "Rumah" untuk dompet bitcoin tertentu, diperluas dengan semua fitur BTCPay Server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Store Settings                                        | Pengaturan dalam BTCPay Server yang spesifik untuk sebuah toko.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Taproot                                               | Peningkatan pada Bitcoin yang akan memperkenalkan beberapa fitur baru. Peningkatan ini dijelaskan dalam BIPs 340, 341, dan 342, dan memperkenalkan skema tanda tangan Schnorr, Taproot, dan Tapscript. Bersama-sama, peningkatan ini memperkenalkan cara baru yang lebih efisien, fleksibel, dan privat dalam mentransfer bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Thier's Law                                           | Hukum yang menyatakan bahwa uang yang baik akan mengusir uang yang buruk.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Third-Party Host                                      | Ketika situs web untuk individu atau perusahaan dijalankan dari server yang dimiliki dan dikelola oleh bisnis lain. Alternatifnya adalah memiliki situs web Anda dihosting di server Anda sendiri di pusat data Anda.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Timelock                                              | Timelock adalah jenis penghalang yang membatasi pengeluaran beberapa bitcoin sampai waktu atau tinggi blok tertentu di masa depan. Timelock menonjol dalam banyak kontrak Bitcoin, termasuk saluran pembayaran dan HTLCs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Topologi                                              | Topologi dari Lightning Network menggambarkan bentuk dari Lightning Network sebagai graf matematika. Node dari graf adalah node-node Lightning (peserta/jaringan peer). Sisi dari graf adalah saluran pembayaran. Topologi dari Lightning Network disiarkan secara publik dengan bantuan protokol gossip, kecuali untuk saluran yang tidak diumumkan. Ini berarti bahwa Lightning Network mungkin jauh lebih besar daripada jumlah saluran dan node yang diumumkan. Mengetahui topologi sangat menarik dalam proses routing berbasis sumber pembayaran di mana pengirim menemukan rute.                                                                                                                                                                                                                                                                                                                                  |
| Transaksi                                             | Transaksi adalah struktur data yang digunakan oleh Bitcoin untuk mentransfer bitcoin dari satu alamat ke alamat lain. Beberapa ribu transaksi diagregasikan dalam sebuah blok, yang kemudian dicatat (ditambang) di blockchain. Transaksi pertama dalam setiap blok, yang disebut transaksi coinbase, menghasilkan bitcoin baru.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ID Transaksi                                          | Sebuah string huruf dan angka yang mengidentifikasi transaksi spesifik di blockchain. String tersebut hanyalah hash SHA-256 ganda dari sebuah transaksi. Hash ini dapat digunakan untuk mencari transaksi di node atau block explorer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Autentikasi Dua Faktor (2FA)                          | Metode keamanan manajemen identitas dan akses yang memerlukan dua bentuk identifikasi untuk mengakses sumber daya dan data, seringkali dengan perangkat sekunder selain kata sandi login standar.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Tidak Dapat Disensor                                  | Properti yang tidak ada entitas yang memiliki kemampuan untuk membalikkan transaksi Bitcoin atau mem-blacklist dompet atau alamat.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Tidak Dapat Disita                                    | Properti yang tidak ada entitas yang dapat mengambil bitcoin dari entitas tanpa kehendak mereka.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Output Transaksi Belum Terpakai (UTXO)                | Output yang belum terpakai, sehingga tersedia untuk digunakan dalam transaksi baru.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Pengalaman Pengguna (UX)                              | Bagaimana pengguna berinteraksi dengan dan mengalami produk, sistem, atau layanan. Ini termasuk persepsi seseorang tentang kegunaan, kemudahan penggunaan, dan efisiensi.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Antarmuka Pengguna (UI)                               | Titik interaksi dan komunikasi manusia-komputer dalam sebuah perangkat.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Dapat Diverifikasi                                    | Properti dari sebuah barang yang dapat dengan mudah dibedakan dari peniru dan barang palsu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Virtual                                               | Berada di atau disimulasikan di komputer atau jaringan komputer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Mesin Virtual (VM)                                    | Dalam komputasi, mesin virtual adalah virtualisasi atau emulasi dari sistem komputer. Mesin virtual berdasarkan arsitektur komputer dan menyediakan fungsionalitas dari komputer fisik. Implementasi mereka mungkin melibatkan perangkat keras khusus, perangkat lunak, atau kombinasi dari keduanya.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Server Pribadi Virtual                                | Server pribadi virtual adalah mesin virtual yang dijual sebagai layanan oleh layanan hosting internet. Istilah "server dedicated virtual" juga memiliki arti yang serupa. Server pribadi virtual menjalankan salinan sistem operasi sendiri, dan pelanggan mungkin memiliki akses tingkat superuser ke instansi sistem operasi tersebut, sehingga mereka dapat menginstal hampir semua perangkat lunak yang berjalan pada OS tersebut                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Volatilitas                                           | Ukuran derajat variasi harga aset dari waktu ke waktu. Aset yang mengalami perubahan harga besar secara teratur lebih volatil, sedangkan aset yang memiliki harga lebih stabil kurang volatil.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Dompet                                                | Dompet Bitcoin menyimpan kunci pengguna, memungkinkan pengguna untuk menerima bitcoin, menandatangani transaksi, dan memeriksa saldo akun mereka. Kunci privat dan publik yang disimpan dalam dompet bitcoin memiliki dua fungsi berbeda, tetapi terikat bersama dalam pembuatan. Dompet Bitcoin berisi kunci pengguna, bukan bitcoin mereka secara aktual. Secara konseptual, dompet seperti gantungan kunci dalam arti bahwa ia menyimpan banyak pasangan kunci privat dan publik. Kunci-kunci ini digunakan untuk menandatangani transaksi, memungkinkan pengguna untuk membuktikan bahwa mereka memiliki keluaran transaksi di blockchain, yaitu bitcoin mereka. Semua bitcoin dicatat di blockchain dalam bentuk keluaran transaksi.                                                                                                                                                                                |
| Wasabi Wallet                                         | Dompet Bitcoin yang berfokus pada privasi, non-custodial, open-source untuk Desktop yang mengimplementasikan CoinJoin tanpa kepercayaan.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Dompet Hanya-Pantau                                   | Dompet Bitcoin yang memungkinkan Anda untuk melacak bitcoin Anda dalam penyimpanan dingin sambil menonaktifkan kemampuan untuk menghabiskan dana. Ini karena dompet hanya-pantau tidak menyimpan atau menggunakan kunci privat, dan oleh karena itu tidak dapat mengotorisasi pengeluaran apa pun atas nama pengguna.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Whale                                                 | Dalam konteks Bitcoin, whale adalah seseorang yang memiliki jumlah bitcoin yang besar.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| White-Label                                           | Produk white-label adalah produk atau layanan yang diproduksi oleh satu perusahaan yang kemudian di-rebrand oleh perusahaan lain agar tampak seolah-olah mereka yang membuatnya.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Whitepaper                                            | Memperkenalkan ide atau topik baru untuk diskusi. Whitepaper Bitcoin memperkenalkan Bitcoin sebagai "Sistem kas elektronik Peer-to-peer" yang "tidak memerlukan pihak ketiga yang dipercaya". Satoshi Nakamoto merilis whitepaper pada 31 Oktober 2008 ke daftar email kriptografer dan cypherpunks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Wrapped Segwit                                        | Implementasi desain yang termasuk dalam peningkatan SegWit dimaksudkan untuk memungkinkan dompet dan perangkat lunak Bitcoin lainnya untuk lebih mudah mendukung SegWit. Untuk mencapai ini, dua skrip SegWit asli, P2WPKH dan P2WSH, digunakan sebagai "redeemScript" dari transaksi P2SH, menghasilkan tipe skrip SegWit terbungkus dari P2SH-P2WPKH dan P2SH-P2WSH masing-masing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

![image](assets/en/129.webp)

