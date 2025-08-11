---
name: KeePass
description: Bagaimana cara mengatur manajer kata sandi lokal?
---
![cover](assets/cover.webp)

Di era digital ini, kita semua harus mengelola banyak akun online yang mencakup berbagai aspek kehidupan sehari-hari, mulai dari perbankan, platform keuangan, email, penyimpanan file, kesehatan, administrasi, media sosial, video game, dan lainnya.

Untuk mengautentikasi diri di setiap akun ini, kita menggunakan identifier, yang seringkali berupa alamat email, disertai dengan kata sandi. Karena mustahil mengingat banyak kata sandi unik, Anda mungkin tergoda untuk menggunakan kembali kata sandi yang sama atau memodifikasi sedikit dari basis yang umum agar mudah diingat. Namun, praktik-praktik ini secara serius membahayakan keamanan akun Anda.

Prinsip pertama yang harus Anda ikuti untuk kata sandi adalah jangan menggunakannya kembali. Setiap akun online harus dilindungi oleh kata sandi unik yang sepenuhnya berbeda dari yang lain. Ini penting karena, jika penyerang berhasil menyusupi salah satu kata sandi Anda, Anda tentu tidak ingin mereka memiliki akses ke semua akun Anda. Memiliki kata sandi unik untuk setiap akun akan mengisolasi potensi serangan dan membatasi cakupannya. Sebagai contoh, jika Anda menggunakan kata sandi yang sama untuk platform video game dan untuk email Anda, dan kata sandi itu disusupi melalui situs phishing yang terkait dengan platform game, penyerang bisa dengan mudah mengakses email Anda dan mengambil alih semua akun online Anda yang lain.

Prinsip penting kedua adalah kekuatan kata sandi. Sebuah kata sandi dianggap kuat jika sulit untuk dipecahkan secara paksa (brute force), yaitu ditebak melalui berbagai percobaan. Ini berarti kata sandi Anda harus seacak mungkin, panjang, dan mencakup berbagai jenis karakter (huruf kecil, huruf besar, angka, dan simbol).

Menerapkan kedua prinsip keamanan kata sandi ini (keunikan dan kekuatan) bisa jadi sulit dalam kehidupan sehari-hari, karena hampir tidak mungkin mengingat kata sandi yang unik, acak, dan kuat untuk semua akun kita. Di sinilah pengelola kata sandi (password manager) berperan.

Pengelola kata sandi akan menghasilkan dan menyimpan kata sandi yang kuat secara aman, memungkinkan Anda mengakses semua akun online tanpa perlu mengingatnya satu per satu. Anda hanya perlu mengingat satu kata sandi, yaitu kata sandi utama (master password), yang memberi Anda akses ke semua kata sandi yang tersimpan di pengelola. Menggunakan pengelola kata sandi meningkatkan keamanan online Anda karena mencegah penggunaan kembali kata sandi dan secara sistematis menghasilkan kata sandi acak. Namun, ini juga menyederhanakan penggunaan akun Anda sehari-hari dengan memusatkan akses ke informasi sensitif Anda.

Dalam tutorial ini, kita akan mempelajari cara mengatur dan menggunakan pengelola kata sandi lokal untuk meningkatkan keamanan online Anda. Di sini, saya akan memperkenalkan Anda pada KeePass. Namun, jika Anda adalah pemula dan ingin memiliki pengelola kata sandi online yang mampu melakukan sinkronisasi di berbagai perangkat, saya merekomendasikan untuk mengikuti tutorial kami tentang Bitwarden: https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

---

*Perhatian: Pengelola kata sandi memang sangat bagus untuk menyimpan kata sandi, tetapi **Anda jangan menyimpan frasa mnemonik dompet Bitcoin Anda di dalamnya!** Ingat, frasa mnemonik harus disimpan hanya dalam format fisik, seperti selembar kertas atau logam.*

---

## Pengenalan ke KeePass

KeePass adalah pengelola kata sandi open-source dan gratis, sangat cocok bagi Anda yang menginginkan solusi aman dan gratis untuk pengelolaan lokal. KeePass adalah perangkat lunak yang diinstal di PC Anda dan tanpa penambahan plugin, tidak berkomunikasi dengan internet. Ini adalah pendekatan yang sangat berbeda dari Bitwarden, yang telah kita bahas di tutorial sebelumnya. Bitwarden, tidak seperti KeePass, memungkinkan sinkronisasi di berbagai perangkat sehingga mengharuskan penyimpanan kata sandi Anda di server online.

Secara bawaan, KeePass tidak mendukung penggunaan ekstensi browser seperti Bitwarden; oleh karena itu, Anda perlu menyalin dan menempelkan kata sandi Anda secara manual dari perangkat lunak. Meskipun ini mungkin terlihat sebagai keterbatasan, menyalin dan menempelkan kata sandi daripada menggunakan pengisian otomatis (auto-fill) adalah praktik yang baik untuk keamanan online Anda.

KeePass dirancang agar ringan dan mudah digunakan, sambil tetap memenuhi standar keamanan tinggi. Perangkat lunak ini mengenkripsi basis data Anda secara lokal untuk perlindungan kredensial yang optimal. KeePass juga merupakan satu-satunya pengelola kata sandi yang divalidasi oleh ANSSI (otoritas keamanan siber Prancis).

Salah satu keunggulan utama KeePass adalah fleksibilitasnya. KeePass dapat digunakan dengan berbagai cara berbeda, seperti dari USB stick tanpa perlu instalasi di komputer. Selain itu, berkat [dukungan plugin](https://keepass.info/plugins.html)nya, KeePass dapat disesuaikan untuk memenuhi kebutuhan yang lebih spesifik.
![KEEPASS](assets/notext/01.webp)

## Bagaimana Cara Mengunduh KeePass?

Proses instalasi KeePass bervariasi tergantung pada sistem operasi yang Anda gunakan. Bagi pengguna Windows atau Linux, instalasinya relatif mudah. Namun, jika Anda menggunakan macOS, langkah tambahan diperlukan karena KeePass dikembangkan pada platform .NET, yang tidak didukung secara langsung oleh macOS. Oleh karena itu, Anda perlu mengonfigurasi sistem yang kompatibel agar KeePass dapat berjalan di perangkat Apple.

Untuk pengguna Debian/Ubuntu, buka terminal dan masukkan perintah berikut:

```bash
sudo apt-get update
sudo apt-get install keepass2
```

Untuk Fedora:

```bash
sudo dnf install keepass
```

Untuk Arch Linux:

```bash
sudo pacman -S keepass
```

Jika Anda menggunakan komputer Windows, kunjungi [halaman unduhan KeePass resmi](https://keepass.info/download.html), dan unduh versi terbaru dari installer:
![KEEPASS](assets/notext/02.webp)

Klik pada file yang diunduh untuk menjalankannya, kemudian ikuti instruksi dari "*wizard setup*" untuk menyelesaikan instalasi (lihat bagian selanjutnya).

Bagi pengguna macOS, instalasinya sedikit lebih rumit. Jika Anda ingin menggunakan versi asli KeePass seperti di Windows, ikuti instruksi di bawah ini. Jika tidak, Anda dapat memilih [KeePassXC](https://keepassxc.org/), versi alternatif yang kompatibel dengan macOS, yang menawarkan antarmuka yang sedikit berbeda.

Untuk menggunakan KeePass, Anda memerlukan *runtime environment* untuk aplikasi .NET. Saya merekomendasikan untuk menginstal Mono untuk tujuan ini. Kunjungi [halaman resmi Mono](https://www.mono-project.com/download/stable/#download-mac) di bagian "macOS", lalu klik tautan untuk mengunduh paket instalasi (`.pkg`).
![KEEPASS](assets/notext/03.webp)

Buka file `.pkg` yang diunduh dan ikuti instruksi untuk menginstal Mono di Mac Anda.
![KEEPASS](assets/notext/04.webp)

Selanjutnya, kunjungi situs web resmi KeePass dan unduh versi portabel terbaru dalam format `.zip`.
![KEEPASS](assets/notext/05.webp)

Setelah mengunduh file `.zip`, klik dua kali untuk mengekstraknya. Anda akan mendapatkan sebuah folder yang berisi beberapa file, termasuk `KeePass.exe`. Buka terminal, lalu navigasikan ke folder KeePass (ganti `xx` dengan nomor versi):

```bash
cd ~/Downloads/KeePass-2.xx
```

Dan akhirnya, jalankan KeePass dengan Mono:

```bash
mono KeePass.exe
```

## Bagaimana Cara Menginstal KeePass?

Pada peluncuran pertama, Anda dapat memilih bahasa untuk antarmuka.
![KEEPASS](assets/notext/06.webp)

Terima ketentuan lisensi.
![KEEPASS](assets/notext/07.webp)

Pilih folder tempat KeePass akan diinstal.
![KEEPASS](assets/notext/08.webp)

Anda dapat secara opsional memodifikasi komponen aplikasi yang diinstal. Jika Anda memiliki cukup ruang, Anda bisa memilih "*Full installation*".
![KEEPASS](assets/notext/09.webp)

Dan akhirnya, Anda dapat memilih untuk menambahkan *shortcut* di desktop Anda.
![KEEPASS](assets/notext/10.webp)

Klik tombol "*Install*".
![KEEPASS](assets/notext/11.webp)

Tunggu selama instalasi, kemudian klik tombol "*Finish*".
![KEEPASS](assets/notext/12.webp)

## Bagaimana cara mengonfigurasi KeePass?

Anda sekarang berada di antarmuka KeePass Anda.
![KEEPASS](assets/notext/13.webp)

Untuk membuat database pertama Anda, klik pada tab "*File*".
![KEEPASS](assets/notext/14.webp)

Kemudian pada menu "*New*".
![KEEPASS](assets/notext/15.webp)

Perangkat lunak akan membuat database baru tempat kata sandi Anda akan disimpan. Anda perlu memilih lokasi untuk folder ini. Pilih lokasi yang mudah diakses.
![KEEPASS](assets/notext/16.webp)

Setelahnya, Anda sebaiknya memikirkan untuk secara rutin mencadangkan folder ini untuk menghindari kehilangan kredensial Anda jika komputer hilang, rusak, atau dicuri. Sebagai contoh, Anda dapat menyalin basis data ke USB stick setiap minggu. File yang berisi database Anda bernama `Database.kdbx` (dokumen ini dienkripsi dengan kata sandi utama Anda). Untuk saran lebih lanjut mengenai praktik pencadangan terbaik, saya juga merekomendasikan untuk melihat tutorial ini:

https://planb.network/tutorials/computer-security/data/proton-drive-03cbe49f-6ddc-491f-8786-bc20d98ebb16

Selanjutnya adalah pembuatan master password Anda.
![KEEPASS](assets/notext/17.webp)

Seperti yang telah kita bahas di awal, kata sandi utama (master password) ini sangat penting karena memberikan Anda akses ke semua kata sandi lain yang tersimpan dalam database. Kata sandi ini akan digunakan untuk mengenkripsi Database `Database.kdbx`. Ada dua risiko utama yang perlu diwaspadai: kehilangan dan penyusupan. Jika Anda kehilangan akses ke kata sandi ini, Anda tidak akan lagi dapat mengakses semua kredensial Anda. Jika kata sandi Anda dicuri, selain database yang terenkripsi, penyerang akan dapat mengakses semua akun Anda.

Untuk meminimalkan risiko kehilangan, saya merekomendasikan untuk membuat cadangan fisik kata sandi utama (master password) Anda di kertas dan menyimpannya di tempat yang aman. Jika memungkinkan, segel cadangan ini dalam amplop yang aman untuk secara berkala memastikan tidak ada orang lain yang mengaksesnya.

Untuk mencegah penyusupan kata sandi utama (master password) Anda, kata sandi tersebut harus sangat kuat. Kata sandi itu harus sepanjang mungkin, menggunakan berbagai jenis karakter, dan dipilih secara acak. Pada tahun 2024, rekomendasi minimum untuk kata sandi yang aman adalah 13 karakter yang mencakup angka, huruf kecil dan huruf besar, serta simbol, asalkan kata sandi tersebut benar-benar acak. Namun, saya merekomendasikan untuk memilih kata sandi minimal 20 karakter, termasuk semua jenis karakter yang mungkin, untuk memastikan keamanannya dalam jangka waktu yang lebih lama.

Masukkan *master password* Anda di kolom yang disediakan dan konfirmasikan di kotak berikutnya, kemudian klik pada "*OK*".
![KEEPASS](assets/notext/18.webp)

Namai database Anda dan tambahkan deskripsi jika perlu. Ini dapat membantu Anda membedakan antara database yang berbeda jika Anda membuat beberapa, misalnya, satu untuk penggunaan pribadi dan yang lain untuk penggunaan profesional.
![KEEPASS](assets/notext/19.webp)

Untuk pengaturan lain, saya merekomendasikan untuk mempertahankan opsi default. Kemudian klik tombol "*OK*".
![KEEPASS](assets/notext/20.webp)

KeePass kemudian menawarkan untuk mencetak lembar darurat.
![KEEPASS](assets/notext/21.webp)

Di lembar ini, Anda akan menemukan lokasi basis data Anda di file Anda, ruang untuk menuliskan kata sandi utama (master password) Anda secara manual, serta instruksi untuk mengaksesnya. Lembar ini harus dipercayakan kepada orang yang tepercaya, karena memungkinkan pemulihan akses ke kredensial Anda jika terjadi masalah.

Namun, karena lembar ini memberikan akses ke kata sandi Anda dengan mengungkapkan *master password* Anda, ini harus digunakan dengan sangat hati-hati. Disarankan untuk menyimpannya dalam amplop tersegel, yang memungkinkan pemeriksaan berkala untuk memastikan tidak ada yang melihatnya. Anda tidak diwajibkan untuk menggunakan lembar ini dan dapat mempertimbangkan metode cadangan lain untuk orang yang Anda cintai.
![KEEPASS](assets/notext/22.webp)

Anda kemudian dapat mengakses manajer kata sandi Anda.
![KEEPASS](assets/notext/23.webp)

Sebelum Anda mulai menyimpan kredensial Anda, saya merekomendasikan untuk mengubah pengaturan pembuatan kata sandi. Untuk melakukan ini, pergi ke tab "*Tools*" dan pilih "*Generate Password...*".
![KEEPASS](assets/notext/24.webp)

Saya menyarankan Anda untuk meningkatkan panjang kata sandi yang dihasilkan menjadi 40 karakter. Sekarang Anda memiliki pengelola kata sandi yang dapat mengingatnya untuk Anda, tidak perlu mengurangi jumlah karakter. Terlebih lagi, Anda tidak perlu menulis kata sandi secara manual, karena Anda dapat menyalin dan menempelkannya. Jadi, memiliki kata sandi yang sangat panjang, 40 karakter, tidak akan merepotkan Anda, namun keamanannya akan sangat meningkat. Saya menyarankan Anda untuk melakukan ini, dan juga untuk mencentang kotak untuk karakter khusus.
![KEEPASS](assets/notext/25.webp)

Konfirmasi dengan mengklik ikon kecil *SAVE*.
![KEEPASS](assets/notext/26.webp)

Tambahkan nama ke profil kata sandi Anda.
![KEEPASS](assets/notext/27.webp)

## Bagaimana cara mengamankan akun Anda dengan KeePass?

Untuk mendaftarkan kredensial baru di manajer KeePass Anda, cukup klik pada ikon kunci dengan panah hijau.
![KEEPASS](assets/notext/28.webp)

Di jendela pembuatan dan penyimpanan, klik ikon kunci kecil dan pilih profil kata sandi 40 karakter Anda.
![KEEPASS](assets/notext/29.webp)

Masukkan nama pengguna untuk akun ini serta judul untuk memudahkan pencarian dalam database Anda.
![KEEPASS](assets/notext/30.webp)

Anda juga dapat menambahkan URL jika ingin menggunakan pintasan (jika perlukan nanti) dan sebuah catatan. 
![KEEPASS](assets/notext/31.webp) 

Jika semuanya sesuai dengan keinginan Anda, klik pada "*OK*" untuk menyimpan kata sandi.
![KEEPASS](assets/notext/32.webp) 

Anda dapat menemukan kata sandi Anda di halaman utama manajer KeePass Anda.
![KEEPASS](assets/notext/33.webp) 

Untuk menyalin kata sandi, cukup klik dua kali padanya. Kata sandi itu akan tetap ada di *clipboard* Anda selama 12 detik, sehingga Anda bisa menempelkannya di situs web saat login berikutnya.
![KEEPASS](assets/notext/34.webp)

Jika Anda ingin memperpanjang durasi kata sandi tetap di *clipboard*, klik pada tab "*Tools*", kemudian pada "*Options...*".
![KEEPASS](assets/notext/35.webp)

Di bawah tab "*Security*", sesuaikan durasinya dengan mengubah jumlah detik dalam kolom "*Clipboard auto-clear time*". Kemudian klik tombol "*OK*" untuk menyimpan perubahan Anda.
![KEEPASS](assets/notext/36.webp)

Di sisi kiri antarmuka, Anda akan melihat ada beberapa folder untuk mengatur kata sandimu.
![KEEPASS](assets/notext/37.webp)

Anda memiliki opsi untuk menghapus folder default atau menambahkan yang baru dengan klik kanan dan memilih "*Add Group...*". 
![KEEPASS](assets/notext/38.webp)

Pilih nama untuk folder baru dan pilih ikon. Anda juga dapat mengimpor ikon Anda sendiri dalam format `.ico`. Kemudian klik pada tombol "*OK*" untuk menyelesaikan pembuatan folder.
![KEEPASS](assets/notext/39.webp)

Folder Anda muncul di sebelah kiri.
![KEEPASS](assets/notext/40.webp)

Untuk menambahkan kata sandi ke folder, cukup seret dari database ke folder yang diinginkan.
![KEEPASS](assets/notext/41.webp)

Fitur ini membantu Anda mengatur pengelola kata sandi dan menemukan kredensialmu dengan lebih mudah.

Metode lain untuk menemukan kata sandi adalah dengan menggunakan fungsi pencarian. Ketik judul pengenal yang ingin Anda temukan di kolom pencarian yang terletak di bagian atas antarmuka, dan Anda akan langsung menemukannya.
![KEEPASS](assets/notext/42.webp)

Berhati-hatilah, KeePass bekerja kurang lebih seperti dokumen teks. Sebelum menutup aplikasi, jika Anda telah menambahkan entri baru ke pengelola Anda, ingatlah untuk menyimpan database. Anda bisa melakukannya dengan mengeklik ikon simpan atau dengan menggunakan keyboard shortcut Ctrl+S.
![KEEPASS](assets/notext/43.webp)

Jika Anda membiarkan KeePass tetap terbuka di latar belakang, perangkat lunak ini tidak akan tertutup secara otomatis. Namun, jika Anda menutup KeePass atau mematikan komputer Anda, Anda perlu memasukkan kata sandi utama Anda untuk mendekripsi database saat membuka kembali perangkat lunak.
![KEEPASS](assets/notext/44.webp)

Itu tadi adalah fitur-fitur dasar KeePass. Tentu saja, tutorial yang ditujukan untuk pemula ini baru menejelaskan permukaan dari banyaknya opsi yang tersedia pada perangkat lunak ini. Ada banyak fitur tambahan yang bisa dijelajahi, belum lagi [semua plugin yang dikembangkan oleh komunitas](https://keepass.info/plugins.html) yang dapat lebih jauh memperluas kemampuan KeePass.

Jika Anda tertarik untuk mempelajari cara meningkatkan keamanan akun online Anda secara lebih dalam guna menghindari peretasan dengan 2FA, saya juga merekomendasikan untuk melihat tutorial lain ini:

https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7
