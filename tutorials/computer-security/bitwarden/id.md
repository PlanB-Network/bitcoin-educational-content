---
name: Bitwarden
description: Bagaimana cara mengatur manajer kata sandi?
---
![cover](assets/cover.webp)

Di era digital ini, kita semua harus mengelola banyak akun online yang mencakup berbagai aspek kehidupan sehari-hari, mulai dari perbankan, platform keuangan, email, penyimpanan file, kesehatan, administrasi, media sosial, video game, dan lainnya.

Untuk mengautentikasi diri di setiap akun ini, kita menggunakan identifier, yang seringkali berupa alamat email, disertai dengan kata sandi. Karena mustahil mengingat banyak kata sandi unik, Anda mungkin tergoda untuk menggunakan kembali kata sandi yang sama atau memodifikasi sedikit dari basis yang umum agar mudah diingat. Namun, praktik-praktik ini secara serius membahayakan keamanan akun Anda.

Prinsip pertama yang harus Anda ikuti untuk kata sandi adalah jangan menggunakannya kembali. Setiap akun online harus dilindungi oleh kata sandi unik yang sepenuhnya berbeda dari yang lain. Ini penting karena, jika penyerang berhasil menyusupi salah satu kata sandi Anda, Anda tentu tidak ingin mereka memiliki akses ke semua akun Anda. Memiliki kata sandi unik untuk setiap akun akan mengisolasi potensi serangan dan membatasi cakupannya. Sebagai contoh, jika Anda menggunakan kata sandi yang sama untuk platform video game dan untuk email Anda, dan kata sandi itu disusupi melalui situs phishing yang terkait dengan platform game, penyerang bisa dengan mudah mengakses email Anda dan mengambil alih semua akun online Anda yang lain.

Prinsip penting kedua adalah kekuatan kata sandi. Sebuah kata sandi dianggap kuat jika sulit untuk dipecahkan secara paksa (*brute force*), yaitu ditebak melalui berbagai percobaan. Ini berarti kata sandi Anda harus seacak mungkin, panjang, dan mencakup berbagai jenis karakter (huruf kecil, huruf besar, angka, dan simbol).

Menerapkan kedua prinsip keamanan kata sandi ini (keunikan dan kekuatan) bisa jadi sulit dalam kehidupan sehari-hari, karena hampir tidak mungkin mengingat kata sandi yang unik, acak, dan kuat untuk semua akun kita. Di sinilah pengelola kata sandi (password manager) berperan.

Pengelola kata sandi akan menghasilkan dan menyimpan kata sandi yang kuat secara aman, memungkinkan Anda mengakses semua akun online tanpa perlu mengingatnya satu per satu. Anda hanya perlu mengingat satu kata sandi, yaitu kata sandi utama (master password), yang memberi Anda akses ke semua kata sandi yang tersimpan di pengelola. Menggunakan pengelola kata sandi meningkatkan keamanan online Anda karena mencegah penggunaan kembali kata sandi dan secara sistematis menghasilkan kata sandi acak. Namun, ini juga menyederhanakan penggunaan akun Anda sehari-hari dengan memusatkan akses ke informasi sensitif Anda.

Dalam tutorial ini, kita akan menjelajahi cara mengatur dan menggunakan pengelola kata sandi untuk meningkatkan keamanan online Anda. Saya akan memperkenalkan Anda pada Bitwarden, dan dalam tutorial lain, kita akan membahas solusi lain yang disebut KeePass. Anda bisa menemukan tutorial KeePass di sini: 

https://planb.network/tutorials/computer-security/authentication/keepass-f8073bb7-5b4a-4664-9246-228e307be246

Peringatan Penting: Pengelola kata sandi sangat bagus untuk menyimpan kata sandi, **tetapi Anda tidak boleh menyimpan frasa mnemonik dompet Bitcoin Anda di dalamnya!** Ingat, frasa mnemonik harus disimpan secara eksklusif dalam format fisik, seperti selembar kertas atau logam.

## Pengenalan ke Bitwarden

Bitwarden adalah pengelola kata sandi yang cocok untuk pemula maupun pengguna lebih mahir. Aplikasi ini menawarkan banyak keunggulan. Yang paling utama, Bitwarden adalah solusi multi-platform, artinya Anda bisa menggunakannya sebagai aplikasi seluler, aplikasi web, ekstensi browser, dan perangkat lunak desktop.

![BITWARDEN](assets/notext/01.webp)

Bitwarden memungkinkan Anda menyimpan kata sandi secara online dan menyinkronkannya di semua perangkat Anda, sambil memastikan enkripsi *end-to-end* dengan kata sandi utama (master password) Anda. Ini memungkinkan Anda, misalnya, mengakses kata sandi baik di komputer maupun smartphone Anda, dengan sinkronisasi antara keduanya. Karena kata sandi Anda dienkripsi, kata sandi tersebut tetap tidak dapat diakses oleh siapa pun, termasuk Bitwarden, tanpa kunci dekripsi yang merupakan kata sandi utama Anda.

Selain itu, Bitwarden adalah perangkat lunak sumber terbuka (open-source), yang berarti perangkat lunak ini dapat diaudit oleh para ahli independen. Mengenai harga, Bitwarden menawarkan tiga paket:
- Versi gratis yang akan kita jelajahi dalam tutorial ini. Meskipun gratis, versi ini menyediakan tingkat keamanan yang setara dengan versi berbayar. Anda dapat menyimpan kata sandi dengan jumlah tidak terbatas dan menyinkronkan sebanyak mungkin perangkat yang Anda inginkan;
- Versi premium seharga $10 per tahun yang mencakup fitur tambahan seperti penyimpanan berkas, pencadangan kartu bank, kemampuan untuk mengatur 2FA dengan kunci keamanan fisik, dan akses ke autentikasi 2FA TOTP langsung dengan Bitwarden;
- Dan paket keluarga seharga $40 per tahun yang memperluas manfaat versi premium hingga enam pengguna berbeda.

![BITWARDEN](assets/notext/02.webp)

Menurut pendapat saya, harga-harga tersebut cukup adil. Versi gratisnya merupakan pilihan yang sangat baik bagi pemula, dan versi premium menawarkan nilai uang yang sangat bagus dibandingkan dengan pengelola kata sandi lain di pasaran, sekaligus menyediakan lebih banyak fitur. Selain itu, fakta bahwa Bitwarden adalah perangkat lunak sumber terbuka (open-source) merupakan keunggulan utama. Oleh karena itu, ini adalah tawaran yang menarik, terutama bagi pemula.

Fitur lain dari Bitwarden adalah kemampuan untuk menjalankan sendiri pengelola kata sandi (self-host) Anda jika Anda memiliki, misalnya, sebuah NAS (*Network Attached Storage*) di rumah. Dengan pengaturan ini, kata sandi Anda tidak disimpan di server Bitwarden, melainkan di server Anda sendiri. Ini memberikan Anda kendali penuh atas ketersediaan kata sandi Anda. Namun, opsi ini membutuhkan pengelolaan cadangan (backup) yang ketat untuk menghindari kehilangan akses. Oleh karena itu, *self-hosting* Bitwarden lebih cocok untuk pengguna mahir, dan akan kami bahas dalam tutorial terpisah.

## Bagaimana cara membuat akun Bitwarden?

Kunjungi [situs web Bitwarden](https://bitwarden.com/) dan klik pada "*Get Started*".
![BITWARDEN](assets/notext/03.webp)

Mulailah dengan memasukkan alamat email Anda serta nama atau nama panggilan Anda.
![BITWARDEN](assets/notext/04.webp)

Selanjutnya, Anda perlu mengatur kata sandi utama (master password) Anda. Seperti yang telah kita bahas di awal, kata sandi ini sangat penting karena memberikan Anda akses ke semua kata sandi lain yang tersimpan di pengelola. Oleh karena itu, ada dua risiko utama yang perlu diwaspadai: kehilangan dan penyusupan. Jika Anda kehilangan akses ke kata sandi ini, Anda tidak akan lagi bisa mengakses semua kredensial Anda. Jika kata sandi ini dicuri, penyerang akan dapat mengakses semua akun Anda.

Untuk meminimalkan risiko kehilangan, saya merekomendasikan untuk membuat cadangan fisik kata sandi utama Anda di kertas dan menyimpannya di tempat yang aman. Jika memungkinkan, segel cadangan ini dalam amplop yang aman untuk secara berkala memastikan tidak ada orang lain yang mengaksesnya.

Untuk mencegah penyusupan kata sandi utama Anda, kata sandi tersebut harus sangat kuat. Kata sandi itu harus sepanjang mungkin, menggunakan berbagai jenis karakter, dan dipilih secara acak. Pada tahun 2024, rekomendasi minimum untuk kata sandi yang aman adalah 13 karakter yang mencakup angka, huruf kecil dan huruf besar, serta simbol, asalkan kata sandi tersebut benar-benar acak. Namun, saya menyarankan untuk memilih kata sandi minimal 20 karakter, termasuk semua jenis karakter yang mungkin, untuk memastikan keamanannya dalam jangka waktu yang lebih lama.

Masukkan kata sandi utama Anda di kolom yang tersedia dan konfirmasi di kolom berikutnya.
![BITWARDEN](assets/notext/05.webp)

Jika Anda mau, menambahkan petunjuk untuk kata sandi utama Anda. Namun, saya menyarankan untuk tidak melakukannya. Petunjuk ini tidak menyediakan metode pemulihan yang bisa diandalkan jika Anda kehilangan kata sandi, dan bahkan bisa berguna bagi penyerang yang mencoba menebak atau melakukan brute force pada kata sandi Anda. Sebagai aturan umum, hindari membuat petunjuk publik yang dapat membahayakan keamanan kata sandi utama Anda.
![BITWARDEN](assets/notext/06.webp)

Kemudian klik tombol "*Buat akun*".
![BITWARDEN](assets/notext/07.webp)

Anda sekarang dapat masuk ke akun Bitwarden baru Anda. Masukkan alamat email Anda.
![BITWARDEN](assets/notext/08.webp)

Kemudian ketik kata sandi utama Anda.
![BITWARDEN](assets/notext/09.webp)

Anda sekarang berada di antarmuka web dari manajer kata sandi Anda.
![BITWARDEN](assets/notext/10.webp)

## Bagaimana cara mengatur Bitwarden?

Untuk memulai, kita akan mengonfirmasi alamat email kita. Klik pada "*Kirim Email*".
![BITWARDEN](assets/notext/11.webp)

Kemudian klik pada tombol yang diterima melalui email.
![BITWARDEN](assets/notext/12.webp)

Akhirnya, masuk lagi.
![BITWARDEN](assets/notext/13.webp)

Pertama dan terpenting, saya sangat menyarankan Anda untuk mengatur autentikasi dua faktor (2FA) demi mengamankan pengelola kata sandi Anda. Anda memiliki pilihan untuk menggunakan aplikasi TOTP atau kunci keamanan fisik. Dengan mengaktifkan 2FA, setiap kali Anda masuk ke akun Bitwarden Anda, Anda tidak hanya akan diminta kata sandi utama (master password) Anda, tetapi juga bukti faktor autentikasi kedua Anda. Ini merupakan lapisan keamanan tambahan, yang sangat berguna jika cadangan kata sandi utama Anda yang berbentuk fisik (kertas) sampai disusupi.

Jika Anda tidak yakin bagaimana cara mengatur dan menggunakan perangkat 2FA ini, saya menyarankan mengikuti 2 tutorial lain ini:

https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e

Untuk melakukan ini, pergi ke tab "*Keamanan*" dalam menu "*Pengaturan*".
![BITWARDEN](assets/notext/14.webp)

Kemudian klik pada tab "*Login dua langkah*".
![BITWARDEN](assets/notext/15.webp)

Di sini, Anda dapat memilih metode 2FA yang Anda sukai. Sebagai contoh, saya akan memilih 2FA dengan aplikasi TOTP dengan mengklik tombol "*Kelola*".
![BITWARDEN](assets/notext/16.webp)

Konfirmasi kata sandi utama Anda.
![BITWARDEN](assets/notext/17.webp)

Kemudian pindai kode QR dengan aplikasi 2FA Anda.
![BITWARDEN](assets/notext/18.webp)

Masukkan kode 6 digit yang tercatat pada aplikasi 2FA Anda, kemudian klik tombol "*Turn On*".
![BITWARDEN](assets/notext/19.webp)

Autentikasi dua faktor telah berhasil diatur pada akun Anda.
![BITWARDEN](assets/notext/20.webp)

Sekarang, jika Anda mencoba masuk kembali ke pengelola Anda, Anda harus terlebih dahulu memasukkan kata sandi utama (master password) Anda, kemudian kode dinamis 6 digit yang dihasilkan oleh aplikasi 2FA Anda. Pastikan Anda selalu memiliki akses ke kode dinamis ini; tanpanya, Anda tidak akan dapat memulihkan kata sandi Anda.
![BITWARDEN](assets/notext/21.webp)

Pada pengaturan, Anda juga memiliki opsi untuk menyesuaikan pengelola Anda di tab "Preferences". Di sini, Anda dapat mengubah durasi sebelum pengelola Anda terkunci secara otomatis, serta bahasa dan tema antarmuka.
![BITWARDEN](assets/notext/22.webp)

Saya sangat merekomendasikan untuk menyesuaikan panjang kata sandi yang dihasilkan oleh Bitwarden. Secara bawaan, panjangnya diatur menjadi 14 karakter, yang mungkin tidak cukup untuk keamanan optimal. Kini setelah Anda memiliki pengelola untuk mengingat semua kata sandi Anda, sebaiknya manfaatkan untuk menggunakan kata sandi yang sangat kuat.

Untuk ini, pergilah ke menu "*Generator*".
![BITWARDEN](assets/notext/23.webp)

Di sini, Anda dapat meningkatkan panjang kata sandi Anda menjadi 40, dan centang kotak untuk menyertakan simbol.
![BITWARDEN](assets/notext/24.webp)

## Bagaimana cara mengamankan akun Anda dengan Bitwarden?

Kini pengelola kata sandi Anda telah terkonfigurasi, Anda dapat mulai menyimpan kredensial untuk akun online Anda. Untuk menambahkan entri baru, klik langsung tombol "*New item*" atau pada tombol "*New* yang terletak di kanan atas layar, lalu pilih "Item".
![BITWARDEN](assets/notext/25.webp)

Dalam formulir yang terbuka, mulailah dengan menentukan sifat dari item yang akan disimpan. Untuk menyimpan kredensial login, pilih opsi "*Login*" dari menu dropdown.
![BITWARDEN](assets/notext/26.webp)

Di kolom "*Name*", masukkan nama deskriptif untuk kredensial Anda. Ini akan memudahkan Anda dalam mencari dan mengatur kata sandi, terutama jika Anda memiliki banyak. Contohnya, jika Anda ingin menyimpan kredensial untuk situs PlanB Network, Anda bisa menamai entri ini sedemikian rupa agar langsung dikenali saat pencarian di kemudian hari.
![BITWARDEN](assets/notext/27.webp)

Opsi "*Folder*" memungkinkan Anda untuk mengklasifikasikan kredensial Anda ke dalam folder. Saat ini, kita belum membuat folder apa pun, namun akan saya tunjukkan cara melakukannya nanti.
![BITWARDEN](assets/notext/28.webp)

Di bidang "*Username*", masukkan nama pengguna Anda, yang biasanya adalah alamat email Anda.
![BITWARDEN](assets/notext/29.webp)

Selanjutnya, di kolom "*Password*", Anda bisa memasukkan kata sandi Anda. Namun, saya sangat merekomendasikan untuk membiarkan Bitwarden menghasilkan kata sandi yang panjang, acak, dan unik untuk Anda. Ini akan memastikan Anda memiliki kata sandi yang kuat. Untuk menggunakan fitur ini, cukup klik ikon panah ganda di atas kolom yang akan diisi.
![BITWARDEN](assets/notext/30.webp)

Anda dapat melihat bahwa kata sandi Anda telah dihasilkan.
![BITWARDEN](assets/notext/31.webp)

Di kolom "*URI 1*", Anda dapat memasukkan nama domain dari situs web.
![BITWARDEN](assets/notext/32.webp)

Dan akhirnya, di kolom "*Notes*", Anda dapat menambahkan detail tambahan jika diperlukan.
![BITWARDEN](assets/notext/33.webp)

Ketika Anda telah selesai mengisi semua bidang ini, klik pada tombol "*Save*".
![BITWARDEN](assets/notext/34.webp)

Pengenal Anda sekarang muncul di manajer Bitwarden Anda.
![BITWARDEN](assets/notext/35.webp)

Dengan mengkliknya, Anda dapat mengakses detailnya dan memodifikasinya.
![BITWARDEN](assets/notext/36.webp)

Dengan mengklik tiga titik kecil di sebelah kanan, Anda memiliki akses cepat untuk menyalin kata sandi atau pengenal.
![BITWARDEN](assets/notext/37.webp)

Selamat! Anda telah berhasil menyimpan kata sandi pertama Anda di pengelola. Jika Anda ingin mengorganisasi identifikasi Anda dengan lebih baik, Anda dapat membuat folder khusus. Untuk melakukannya, klik tombol "*New*" yang terletak di kanan atas layar, lalu pilih "*Folder*".
![BITWARDEN](assets/notext/38.webp)

Masukkan nama untuk folder Anda.
![BITWARDEN](assets/notext/39.webp)

Kemudian klik pada "*Save*".
![BITWARDEN](assets/notext/40.webp)

Folder Anda sekarang muncul di manajer Anda.
![BITWARDEN](assets/notext/41.webp)

Anda dapat menetapkan folder untuk sebuah pengenal ketika membuatnya, seperti yang telah kita lakukan sebelumnya, atau dengan memodifikasi pengenal yang sudah ada. Sebagai contoh, dengan mengklik identifikasi saya untuk PlanB Network, saya kemudian dapat memilih untuk mengklasifikasikannya ke dalam folder "*Bitcoin*".
![BITWARDEN](assets/notext/42.webp)

Dengan cara ini, Anda dapat menyusun pengelola kata sandi Anda untuk memudahkan pencarian pengenal. Anda bisa mengelompokkan dengan folder seperti pribadi, profesional, bank, email, media sosial, langganan, belanja, administrasi, streaming, penyimpanan, perjalanan, kesehatan, dan lain-lain.

Jika Anda lebih memilih untuk hanya menggunakan versi web Bitwarden, itu sangat mungkin. Saya kemudian merekomendasikan untuk menambahkan pengelola kata sandi Anda ke bookmark browser Anda agar mudah diakses dan untuk menghindari risiko phishing. Namun, Bitwarden juga menawarkan berbagai klien (client) yang memungkinkan Anda menggunakan pengelola Anda di berbagai perangkat dan untuk menyederhanakan penggunaan sehari-hari. Mereka secara khusus menawarkan aplikasi seluler, ekstensi browser, dan perangkat lunak desktop. Mari kita lihat cara mengaturnya bersama.

![BITWARDEN](assets/notext/43.webp)

## Bagaimana cara menggunakan ekstensi browser Bitwarden?

Pertama, Anda dapat mengatur ekstensi browser jika diinginkan. Ekstensi ini berfungsi sebagai versi ringkas dari pengelola Anda dan menawarkan Anda kemampuan untuk secara otomatis menyimpan kata sandi baru, menghasilkan saran kata sandi yang aman, serta secara otomatis mengisi kredensial Anda pada halaman login situs web.

Penggunaan ekstensi ini sehari-hari sangatlah praktis, namun juga dapat membuka vektor serangan baru. Oleh karena itu, beberapa pakar keamanan siber menyarankan untuk tidak menggunakan ekstensi peramban untuk pengelola kata sandi. Namun, jika Anda memilih untuk menggunakan ekstensi Bitwarden, berikut adalah cara untuk melanjutkannya:

Mulailah dengan pergi ke [halaman unduhan resmi Bitwarden](https://bitwarden.com/download/#downloads-web-browser).
![BITWARDEN](assets/notext/44.webp)

Pilih browser Anda dari daftar yang tersedia. Untuk contoh ini, saya menggunakan Firefox, jadi saya diarahkan ke ekstensi Bitwarden resmi di Firefox Add-ons Store. Prosedurnya cukup mirip untuk browser lain.
![BITWARDEN](assets/notext/45.webp)

Klik pada tombol "*Add to Firefox*".
![BITWARDEN](assets/notext/46.webp)

Anda kemudian bisa menempelkan Bitwarden ke extension bar Anda agar mudah diakses. Klik pada ekstensinya untuk login.
![BITWARDEN](assets/notext/47.webp)

Masukkan alamat email Anda.
![BITWARDEN](assets/notext/48.webp)

Kemudian kata sandi utama Anda.
![BITWARDEN](assets/notext/49.webp)

Dan akhirnya, masukkan kode 6-digit dari aplikasi autentikasi Anda.
![BITWARDEN](assets/notext/50.webp)

Anda sekarang terhubung ke manajer Bitwarden Anda melalui ekstensi browser.
![BITWARDEN](assets/notext/51.webp)

Sebagai contoh, jika saya kembali ke situs PlanB Network dan mencoba masuk ke akun saya, Anda dapat melihat bahwa ekstensi Bitwarden yang terintegrasi di browser mengenali kolom login dan secara otomatis menawarkan saya untuk memilih pengenal yang sebelumnya telah saya simpan.
![BITWARDEN](assets/notext/52.webp)

Jika saya memilih pengenal ini, Bitwarden akan mengisi kolom login secara otomatis untuk saya. Fitur ekstensi ini memungkinkan koneksi cepat ke situs web, tanpa perlu menyalin-tempel kredensial dari aplikasi web atau perangkat lunak Bitwarden.
![BITWARDEN](assets/notext/53.webp)

Ekstensi ini juga dirancang untuk mendeteksi pembuatan akun baru. Sebagai contoh, saat membuat akun baru di PlanB Network, Bitwarden akan secara otomatis menyarankan untuk menyimpan identifikasi baru tersebut.
![BITWARDEN](assets/notext/54.webp)

Saat Anda mengeklik saran yang muncul, ekstensi akan terbuka. Ini memungkinkan saya untuk memasukkan detail pengenal baru dan membuat kata sandi yang kuat serta unik.
![BITWARDEN](assets/notext/55.webp)

Setelah menyelesaikan informasi dan mengklik pada "*Save*", ekstensi menyimpan kredensial.
![BITWARDEN](assets/notext/56.webp)

Kemudian, ekstensi secara otomatis mengisi kredensial kita di kolom yang sesuai di situs web.
![BITWARDEN](assets/notext/57.webp)

## Bagaimana cara menggunakan perangkat lunak Bitwarden?

Untuk menginstal perangkat lunak desktop Bitwarden, mulailah dengan membuka [halaman unduhan](https://bitwarden.com/download/#downloads-desktop). Pilih dan unduh versi yang sesuai dengan sistem operasi Anda.
![BITWARDEN](assets/notext/58.webp)

Setelah unduhan selesai, lanjutkan dengan instalasi perangkat lunak di komputer Anda. Pada peluncuran pertama perangkat lunak Bitwarden, Anda perlu memasukkan kredensial Anda untuk membuka kunci pengelola kata sandi Anda.
![BITWARDEN](assets/notext/59.webp)

Kemudian, Anda akan tiba di halaman utama manajer Anda. Antarmukanya hampir sama seperti pada aplikasi web.
![BITWARDEN](assets/notext/60.webp)

## Bagaimana cara menggunakan aplikasi Bitwarden?

Untuk mengakses kata sandi Anda dari ponsel, Anda dapat menginstal aplikasi mobile Bitwarden. Mulailah dengan membuka [halaman unduhan](https://bitwarden.com/download/#downloads-mobile) dan gunakan smartphone Anda untuk memindai kode QR yang sesuai dengan sistem operasi Anda.
![BITWARDEN](assets/notext/61.webp)

Unduh dan instal aplikasi mobile Bitwarden resmi. Pada pembukaan aplikasi pertama, masukkan kredensial Anda untuk membuka akses ke manajer kata sandi Anda.
![BITWARDEN](assets/notext/62.webp)

Setelah terhubung, Anda bisa langsung melihat dan mengelola semua kata sandimu dari aplikasi.
![BITWARDEN](assets/notext/63.webp)

Untuk meningkatkan keamanan aplikasi Anda, saya menyarankan untuk masuk ke pengaturan dan mengaktifkan perlindungan PIN. Ini akan menambahkan lapisan keamanan ekstra jika ponsel Anda hilang atau dicuri.
![BITWARDEN](assets/notext/64.webp)

## Bagaimana cara membackup Bitwarden?

Untuk memastikan Anda tidak pernah kehilangan akses ke kata sandi Anda, bahkan jika Anda kehilangan kata sandi utama atau terjadi bencana yang memengaruhi server Bitwarden, saya menyarankan Anda untuk secara rutin melakukan pencadangan terenkripsi dari pengelola Anda ke media eksternal.

Ide ini bertujuan untuk mengenkripsi semua kredensial Bitwarden Anda dengan kata sandi yang berbeda dari kata sandi utama Anda. Simpan cadangan terenkripsi ini di USB stick atau hard drive yang Anda simpan di rumah, misalnya. Anda kemudian dapat menyimpan salinan fisik kata sandi dekripsi di lokasi yang terpisah dari tempat media cadangan disimpan. Sebagai contoh, Anda bisa menyimpan USB stick di rumah dan menitipkan salinan fisik kata sandi enkripsi kepada teman yang tepercaya.

Metode ini memastikan bahwa meskipun media cadangan Anda dicuri, data Anda akan tetap tidak dapat diakses tanpa kata sandi dekripsi. Demikian pula, teman Anda tidak akan dapat mengakses data Anda tanpa memiliki media fisik tersebut.

Namun, jika terjadi masalah, Anda dapat menggunakan kata sandi dan media eksternal tersebut untuk mendapatkan kembali akses ke kredensial Anda, secara independen dari Bitwarden. Dengan demikian, bahkan jika server Bitwarden hancur, Anda masih memiliki kemungkinan untuk mengambil kembali kata sandi Anda.

Oleh karena itu, saya menyarankan Anda untuk melakukan pencadangan ini secara rutin agar selalu mencakup kredensial terbaru Anda. Untuk menghindari merepotkan teman Anda, yang memegang salinan kata sandi enkripsi, setiap kali ada pencadangan baru, Anda dapat menyimpan kata sandi ini di pengelola kata sandi Anda. Ini bukan dimaksudkan sebagai cadangan, karena teman Anda sudah memiliki salinan fisiknya, melainkan untuk menyederhanakan prosedur ekspor Anda di masa mendatang.

Untuk melanjutkan ekspor data, caranya cukup mudah: buka bagian  "*Tools*" pada pengelola Bitwarden Anda, lalu pilih "*Export vault*".
![BITWARDEN](assets/notext/65.webp)

Untuk formatnya, pilih "*.json (Encrypted)*".
![BITWARDEN](assets/notext/66.webp)

Kemudian pilih opsi "*Password protected*".
![BITWARDEN](assets/notext/67.webp)

Di sini, penting untuk memilih kata sandi yang kuat, unik, dan dibuat secara acak untuk mengenkripsi cadangan. Ini memastikan bahwa, bahkan jika cadangan terenkripsi Anda dicuri, penyerang tidak akan bisa mendekripsinya dengan brute force.
![BITWARDEN](assets/notext/68.webp)

Klik pada "*Confirm format*" dan masukkan kata sandi utama Anda untuk melanjutkan dengan ekspor.
![BITWARDEN](assets/notext/69.webp)

Setelah ekspor selesai, Anda akan menemukan file cadangan terenkripsi di unduhan Anda. Pindahkan file tersebut ke perangkat penyimpanan eksternal yang aman, seperti USB stick atau hard drive. Ulangi operasi ini secara berkala tergantung pada penggunaan Anda. Misalnya, Anda dapat memperbarui cadangan setiap minggu atau setiap bulan, sesuai kebutuhan Anda.
