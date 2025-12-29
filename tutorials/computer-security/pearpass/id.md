---
name: PearPass
description: Dapatkan kembali kendali atas kata sandi Anda dengan pengelola kata sandi lokal, peer-to-peer, dan bebas cloud
---

![cover](assets/cover.webp)



Pada saat setiap individu mengelola puluhan, bahkan ratusan akun online, keamanan login telah menjadi masalah utama dalam keamanan TI. Jejaring sosial, sistem perpesanan, layanan profesional, platform keuangan: setiap akses ini bergantung pada rahasia, yang jika dibobol bisa berakibat serius pada kehidupan Anda.



Namun, meskipun jumlah serangan terus bertambah, praktik-praktik buruk tetap tersebar luas di kalangan masyarakat: kata sandi yang lemah, kata sandi yang digunakan ulang, kata sandi yang disimpan dalam teks yang jelas, atau kata sandi yang mudah diingat. Untuk mengatasi masalah ini tanpa membuat hidup Anda menjadi lebih rumit setiap hari, solusinya adalah dengan menggunakan pengelola kata sandi.



Lusinan pengelola kata sandi sudah ada, dan Plan ₿ Academy menawarkan tutorial untuk sebagian besar dari mereka. Tetapi dalam tutorial ini, saya ingin memperkenalkan Anda pada salah satu yang jelas-jelas berbeda dari yang lain dalam hal cara kerjanya: **PearPass**.



**PearPass adalah sebuah pengelola kata sandi peer-to-peer bersumber terbuka, lokal, dan dirancang untuk memberikan kontrol penuh pada pengguna atas data mereka



![Image](assets/fr/01.webp)



## Mengapa memilih PearPass?



Pengelola kata sandi adalah sebuah program perangkat lunak yang menghasilkan, menyimpan, dan mengatur semua kata sandi Anda dengan cara yang aman. Daripada menghafal atau menggunakan ulang kata sandi, Anda hanya memiliki satu rahasia yang harus dilindungi: kata sandi utama, yang mengenkripsi seluruh brankas Anda. Pendekatan ini memungkinkan penggunaan kata sandi yang unik, panjang, dan acak untuk setiap layanan, sehingga mengurangi risiko lupa dan kompromi, sekaligus membatasi dampak kebocoran yang mungkin terjadi. Saat ini, ini adalah alat TI dasar yang harus digunakan semua orang.



Ada dua kategori utama pengelola kata sandi. Di satu sisi, ada perangkat lunak khusus lokal, yang sangat aman karena data tidak pernah disimpan di server pusat, tetapi tidak terlalu praktis, karena tidak memungkinkan Anda untuk dengan mudah menyinkronkan kredensial Anda di antara beberapa perangkat (komputer, ponsel cerdas, tablet...). Di sisi lain, pengelola kata sandi berbasis awan menyimpan kredensial Anda pada peladen mereka dan menyinkronkannya di semua perangkat Anda. Keuntungan utama mereka adalah kenyamanan, tetapi melibatkan kompromi pada keamanan, karena kata sandi Anda disimpan pada infrastruktur yang tidak dapat Anda kendalikan.



PearPass dengan sengaja memisahkan diri dari kedua model tersebut. Memposisikan dirinya di antara manajer lokal dan solusi awan: memungkinkan sinkronisasi kata sandi Anda, sambil menjamin bahwa kata sandi tersebut tidak pernah disimpan di server jarak jauh. Hasilnya, semua kredensial Anda disimpan secara lokal pada perangkat Anda, dan sinkronisasi antara beberapa mesin secara eksklusif bersifat peer-to-peer. Arsitektur ini menghilangkan satu titik kegagalan yang terkait dengan basis data terpusat: tidak ada server yang perlu dikompromikan, dan tidak ada infrastruktur pihak ketiga yang dapat mengakses kredensial Anda. Komunikasi antara perangkat Anda dienkripsi dari ujung ke ujung, memastikan bahwa hanya kunci yang Anda pegang yang dapat mengakses data.



![Image](assets/fr/02.webp)



Untuk memungkinkan hal ini, seperti namanya, PearPass mengandalkan **Pears**, sebuah ekosistem teknologi peer-to-peer yang didedikasikan untuk pembuatan dan eksekusi aplikasi tanpa server. Pears menyediakan lingkungan eksekusi, mekanisme distribusi, dan lapisan jaringan yang diperlukan untuk menjalankan aplikasi yang sepenuhnya terdesentralisasi, yang mampu melakukan sinkronisasi secara langsung di antara sesama pengguna, tanpa infrastruktur pusat. Dalam kasus PearPass, Pears menyediakan penemuan perangkat, pembuatan koneksi terenkripsi, dan sinkronisasi brankas kata sandi di antara mesin-mesin Anda. Pendekatan ini memastikan bahwa PearPass tetap berfungsi, tangguh, dan tidak bergantung pada otoritas eksternal apa pun.



https://planb.academy/tutorials/computer-security/communication/pears-6d42b312-c69f-4504-8f71-b03b56c42fdd

Di luar arsitektur yang inovatif ini, PearPass sepenuhnya open-source, dan semua fungsinya gratis. Perangkat lunak ini juga telah diaudit secara independen oleh Secfault Security. Selain arsitekturnya yang spesifik, PearPass tentu saja menawarkan semua fitur klasik yang diharapkan dari sebuah pengelola kata sandi yang bagus, yang akan kita temukan di sepanjang tutorial ini.



Singkatnya, di mana pengelola kata sandi tradisional meminta Anda untuk mempercayai sebuah perusahaan dan peladennya, PearPass mengadopsi logika kedaulatan: tidak ada awan, tidak ada akun terpusat, tidak ada perantara. Anda tetap memegang kendali eksklusif atas kredensial Anda, sambil mendapatkan keuntungan dari sinkronisasi antar perangkat Anda.



## Bagaimana cara menginstal PearPass?



PearPass tersedia di semua platform: Windows, Linux, macOS, Android, iOS, dan ekstensi peramban. Tidak perlu menginstal Pears pada komputer Anda: PearPass bekerja dengan sendirinya.



### Instalasi pada Windows



Pada Windows, PearPass disediakan sebagai penginstal klasik. Buka [halaman unduhan resmi](https://pass.pears.com/download), lalu klik tombol `Unduh Penginstal Windows`.



Setelah file diunduh, buka penginstal dan ikuti langkah-langkah yang ditunjukkan oleh wizard. Aplikasi ini kemudian dapat diakses dari `Menu Mulai` atau melalui pintasan desktop.



![Image](assets/fr/03.webp)



### Instalasi di macOS



Di macOS, PearPass didistribusikan sebagai gambar disk (`.dmg`). Buka [halaman unduhan resmi](https://pass.pears.com/download) dan pilih versi yang sesuai dengan arsitektur Mac Anda (Intel atau Apple Silicon). Setelah mengunduh, buka file `.dmg` dan luncurkan aplikasi dari folder `Aplikasi`.



Saat pertama kali dijalankan, macOS akan menampilkan pesan keamanan yang mengindikasikan bahwa aplikasi tersebut berasal dari Internet: cukup konfirmasikan untuk melanjutkan.



### Instalasi di Linux



Di Linux, PearPass tersedia dalam format `.AppImage`, yang menjamin kompatibilitas yang luas dengan sebagian besar distribusi tanpa ketergantungan khusus. Unduh file `.AppImage` dari [halaman unduhan resmi](https://pass.pears.com/download), lalu jalankan secara langsung dengan mengklik dua kali.



Tergantung pada lingkungan Anda, Anda mungkin perlu membuat file dapat dieksekusi melalui properti file (klik kanan) atau dengan perintah `chmod +x`. Setelah diotorisasi, PearPass akan diluncurkan sebagai aplikasi yang berdiri sendiri.



### Pemasangan ekstensi browser



PearPass menawarkan sebuah ekstensi peramban untuk login otomatis dan akses cepat ke brankas Anda ketika menjelajahi web. Ekstensi saat ini tersedia untuk Google Chrome dan peramban yang kompatibel. Untuk menginstalnya, kunjungi [halaman unduhan resmi](https://chromewebstore.google.com/detail/pearpass/pdeffakfmcdnjjafophphgmddmigpejh).



![Image](assets/fr/04.webp)



Setelah ditambahkan, Anda bisa menyematkannya pada bilah alat untuk akses cepat. Untuk mengaktifkan ekstensi ini, Anda memerlukan tautan dengan aplikasi PearPass yang diinstal secara lokal di komputer Anda (kita akan membahasnya nanti dalam tutorial).



### Instalasi di iOS dan Android



Pada iPhone dan Android, cukup unduh aplikasi dari toko aplikasi Anda:




- [Google Play Store](https://play.google.com/store/apps/details?id=com.pears.pass);
- [App Store](https://apps.apple.com/us/app/pearpass/id6752954830).



![Image](assets/fr/05.webp)



Selain metode instalasi klasik ini, Anda juga dapat mengunduh perangkat lunak secara langsung dari repositori GitHub, untuk setiap file :




- [Desktop](https://github.com/tetherto/pearpass-app-desktop);
- [Seluler](https://github.com/tetherto/pearpass-app-mobile);
- [Ekstensi peramban](https://github.com/tetherto/pearpass-app-browser-extension).



Setelah PearPass terinstal di satu atau beberapa platform, Anda dapat melanjutkan ke konfigurasi awal. Dalam tutorial ini, kita akan mulai dengan mengonfigurasi perangkat lunak di desktop, lalu menyinkronkannya dengan ekstensi peramban dan aplikasi seluler.



## Bagaimana cara membuat brankas PearPass?



Ketika Anda pertama kali menjalankan PearPass di komputer, aplikasi ini akan memandu Anda melalui dua langkah: mengatur kata sandi utama, lalu membuat brankas pertama Anda.



### Mengatur kata sandi utama



Ketika aplikasi pertama kali dijalankan di desktop, klik tombol `Lewati` lalu `Lanjutkan` untuk melewati layar pengenalan dan mencapai tahap konfigurasi kata sandi utama.



![Image](assets/fr/06.webp)



Berikutnya adalah langkah penting untuk memilih kata sandi utama Anda. Seperti yang telah kita lihat di bagian pendahuluan, kata sandi ini sangat penting, karena memberikan Anda akses ke semua kata sandi lain yang tersimpan di pengelola. Secara teknis, kata sandi ini digunakan untuk mendapatkan kunci kriptografi yang digunakan untuk mengenkripsi data Anda.



Kata sandi utama memiliki dua risiko utama: kehilangan dan penyalahgunaan. Jika Anda kehilangan akses ke kata sandi ini, Anda tidak akan lagi dapat mengakses detail login Anda. PearPass tidak pernah menyimpan kata sandi utama Anda: **Jika hilang, detail login Anda akan hilang secara permanen**. Tidak ada mekanisme pemulihan. Sebaliknya, jika kata sandi ini dibobol dan penyerang mendapatkan akses ke salah satu perangkat Anda, dia akan dapat mengakses semua akun Anda.



Untuk membatasi risiko kehilangan, Anda dapat membuat cadangan fisik kata sandi utama Anda, misalnya di atas kertas, dan menyimpannya di tempat yang aman. Idealnya, tutuplah cadangan ini di dalam amplop agar Anda bisa memeriksa secara berkala bahwa cadangan tersebut belum diakses. Di sisi lain, jangan pernah membuat cadangan digital dari kata sandi ini.



Untuk mengurangi risiko pembobolan, kata sandi utama Anda harus kuat. Kata sandi ini harus sepanjang mungkin, mencakup berbagai macam karakter dan dipilih dengan cara yang benar-benar acak. Pada tahun 2025, rekomendasi minimumnya adalah setidaknya 13 karakter termasuk huruf besar dan kecil, angka dan simbol, asalkan kata sandi dibuat secara acak. Namun, saya akan merekomendasikan kata sandi setidaknya 20 karakter, jika tidak lebih, dengan semua jenis karakter, untuk memastikan tingkat keamanan yang lebih tahan lama.



Masukkan kata sandi utama Anda pada bidang yang tersedia, konfirmasikan untuk kedua kalinya, lalu klik tombol `Lanjutkan`.



![Image](assets/fr/07.webp)



Anda kemudian akan diarahkan ke layar login: masukkan kata sandi utama Anda untuk memeriksa apakah semuanya berfungsi dengan benar.



![Image](assets/fr/08.webp)



### Buat brankas pertama Anda



Setelah Anda masuk, PearPass akan meminta Anda untuk membuat brankas pertama Anda. Brankas adalah sebuah wadah terenkripsi tempat menyimpan kata sandi, ID, catatan aman, dan informasi lainnya. Setiap brankas terisolasi dan dapat diidentifikasi dengan nama yang berbeda, sehingga Anda dapat mengatur data Anda sesuai dengan kegunaannya (pribadi, profesional, proyek tertentu...).



Klik tombol `Buat brankas baru`.



![Image](assets/fr/09.webp)



Pilih nama untuk vault ini, lalu klik `Buat vault baru` sekali lagi untuk menyelesaikan pembuatannya.



![Image](assets/fr/10.webp)



Brankas Anda segera siap digunakan. Anda bisa langsung menambahkan kata sandi, login atau catatan aman.



![Image](assets/fr/11.webp)



## Bagaimana cara menambahkan login ke PearPass?



Setelah membuat brankas, Anda bisa mulai menyimpan item di dalamnya. PearPass mendukung pendaftaran berbagai jenis barang:




- masuk ke situs atau layanan ;
- identitas: informasi pribadi Anda untuk mengisi formulir dengan cepat, tetapi juga untuk menyimpan dokumen identitas secara langsung di PearPass ;
- kartu kredit: nomor kartu kredit Anda untuk pembayaran yang lebih cepat saat berbelanja online;
- Wi-Fi: kata sandi untuk jaringan Wi-Fi Anda;
- PassPhrase: frasa rahasia yang terdiri dari beberapa kata (peringatan: Saya sangat menyarankan agar tidak menggunakannya untuk frasa mnemonik wallet Bitcoin);
- catatan: membuat catatan yang aman ;
- custom: fitur ini memungkinkan Anda membuat jenis elemen khusus, yang disesuaikan dengan kebutuhan spesifik Anda.



Mulailah dengan membuka PearPass dan masuk dengan kata sandi utama Anda.



![Image](assets/fr/12.webp)



Pilih brankas tempat Anda ingin menyimpan pengenal ini.



![Image](assets/fr/13.webp)



Pada halaman beranda, klik tombol untuk menambahkan item baru, tergantung pada jenis informasi yang ingin Anda rekam. Dalam kasus saya, saya ingin menambahkan login untuk akun saya di situs web Plan ₿ Academy: jadi saya mengklik tombol `Buat Login`.



![Image](assets/fr/14.webp)



Setelah Anda memilih jenis item yang ingin Anda tambahkan, sebuah formulir akan muncul, memungkinkan Anda untuk memasukkan informasi yang terkait dengan layanan yang dimaksud. Tergantung pada kebutuhan Anda, Anda dapat memasukkan nama layanan, login, kata sandi, dan, jika diperlukan, alamat situs web dan catatan tambahan.



PearPass juga dilengkapi dengan generator kata sandi, memungkinkan Anda untuk membuat kata sandi yang kuat secara langsung dari formulir. Untuk menggunakannya, klik pada ikon yang mewakili tiga titik kecil di bidang `Kata Sandi`, pilih panjang yang diinginkan, lalu klik `Masukkan kata sandi`.



Setelah semua kolom diisi, klik tombol `Save` untuk menyimpan pengenal di brankas.



![Image](assets/fr/15.webp)



Pengidentifikasi sekarang disimpan. Ini muncul dalam daftar item di brankas yang dipilih, dan dapat dilihat dengan mengekliknya.



![Image](assets/fr/16.webp)



Anda dapat dengan mudah memodifikasi sebuah elemen dengan mengeklik elemen tersebut, kemudian pada tombol `Edit`. Anda juga dapat menghapusnya dengan mengeklik tiga titik kecil di bagian kanan atas antarmuka, kemudian pada `Hapus elemen`.



![Image](assets/fr/22.webp)



Pada perangkat seluler, logikanya tetap sama, meskipun antarmukanya sudah disesuaikan. Setelah masuk, pilih brankas yang diinginkan, ketuk tombol `+`, pilih jenis item yang akan dibuat, lalu isi informasi yang diperlukan.



![Image](assets/fr/17.webp)



## Bagaimana cara mengatur PearPass?



Seperti yang telah kita lihat pada bagian sebelumnya, PearPass memungkinkan Anda untuk membuat beberapa brankas yang berbeda. Hal ini memungkinkan untuk memisahkan penggunaan yang berbeda dan merupakan tingkat organisasi pertama untuk pengelola kata sandi Anda. Dari halaman beranda, Anda bisa dengan mudah beralih dari satu brankas ke brankas lainnya dengan mengeklik tanda panah di kiri atas antarmuka.



![Image](assets/fr/18.webp)



Cara lain untuk mengatur kata sandi Anda, bahkan di dalam brankas, adalah dengan membuat folder. Untuk melakukannya, pada kolom sebelah kiri antarmuka, klik simbol `+` di sebelah `Semua Folder`, kemudian masukkan nama folder yang ingin Anda buat.



![Image](assets/fr/19.webp)



Anda kemudian dapat menyimpan pengenal pilihan Anda, baik secara langsung ketika membuat item, atau nanti dengan mengeklik `Edit`. Anda tinggal memilih folder yang diinginkan di sudut kiri atas formulir.



![Image](assets/fr/20.webp)



Setelah membuka suatu item, misalnya login, Anda bisa mengeklik ikon bintang di bagian kanan atas antarmuka untuk menambahkannya ke favorit. Favorit dapat dengan cepat ditemukan dalam folder khusus, selain folder dasarnya.



![Image](assets/fr/21.webp)



Terakhir, ada bilah pencarian di bagian atas antarmuka, sehingga Anda dapat dengan cepat menemukan item yang Anda cari, bahkan jika brankas Anda berisi banyak pengenal.



## Bagaimana cara menyinkronkan PearPass di ponsel saya?



Sekarang setelah Anda memiliki brankas yang berfungsi dengan item-item yang tersimpan di komputer, Anda mungkin ingin mengakses kata sandi Anda dari ponsel pintar atau perangkat lain. PearPass memungkinkan anda untuk menyinkronkan manajer anda pada beberapa mesin dengan aman menggunakan Pears. Mari kita cari tahu caranya.



Untuk memulai, pada mesin sumber (komputer Anda, misalnya), masuk ke brankas menggunakan kata sandi utama Anda. Setelah berada di halaman beranda, klik tombol `Tambahkan Perangkat`, yang terletak di kanan bawah antarmuka.



![Image](assets/fr/23.webp)



PearPass kemudian menghasilkan tautan undangan, yang juga tersedia sebagai kode QR, untuk menyinkronkan brankas yang dipilih pada perangkat pilihan Anda.



![Image](assets/fr/24.webp)



Jika Anda ingin menyinkronkan di perangkat seluler, pertama-tama instal aplikasi, lalu luncurkan. Anda akan diminta untuk membuat kata sandi utama untuk manajer seluler Anda. Anda bisa memilih untuk menggunakan kata sandi yang sama dengan yang ada di komputer, atau kata sandi yang berbeda. Dalam semua kasus, ikuti rekomendasi yang sama: kata sandi yang kuat dan acak yang disimpan di media fisik.



![Image](assets/fr/25.webp)



Anda kemudian dapat mengaktifkan autentikasi biometrik jika Anda mau, untuk menghindari keharusan memasukkan kata sandi utama secara manual setiap kali Anda membuka kunci ponsel.



![Image](assets/fr/26.webp)



Masukkan kembali kata sandi utama Anda, lalu klik tombol `Lanjutkan`.



![Image](assets/fr/27.webp)



Pilih opsi `Muat brankas`, lalu klik `Pindai Kode QR` dan pindai kode QR undangan yang ditampilkan oleh PearPass pada mesin sumber Anda (komputer).



![Image](assets/fr/28.webp)



Brankas Anda di komputer dan ponsel Anda sekarang tersinkronisasi. Setiap ID yang ditambahkan di satu perangkat akan disimpan dengan aman dan direplikasi di perangkat lainnya.



![Image](assets/fr/29.webp)



Pada ponsel, Anda juga dapat mengaktifkan pengisian bidang otomatis. Untuk melakukannya, buka `Pengaturan > Tingkat Lanjut`, lalu klik tombol `Tetapkan sebagai Default` di bagian `Isi Otomatis`.



![Image](assets/fr/30.webp)



## Bagaimana cara menyinkronkan PearPass dengan ekstensi browser?



Memiliki pengelola kata sandi yang tersinkronisasi antara komputer dan ponsel cerdas Anda sudah sangat praktis, tetapi mengintegrasikannya secara langsung ke dalam peramban Anda akan lebih praktis lagi. Untuk melakukannya, mulailah dengan [menambahkan ekstensi PearPass resmi ke peramban Anda](https://chromewebstore.google.com/detail/pearpass/pdeffakfmcdnjjafophphgmddmigpejh).



![Image](assets/fr/31.webp)



Dari perangkat lunak PearPass yang terinstal di komputer lokal Anda, buka `Pengaturan > Lanjutan`, lalu aktifkan opsi `Aktifkan ekstensi peramban`.



![Image](assets/fr/32.webp)



PearPass menghasilkan file pasangan token. Salinlah.



![Image](assets/fr/33.webp)



Kemudian buka ekstensi PearPass di peramban Anda, tempelkan pasangan token, dan klik tombol `Verifikasi`, diikuti dengan `Selesai`.



![Image](assets/fr/34.webp)



Pengelola kata sandi Anda sekarang disinkronkan dengan ekstensi browser.



![Image](assets/fr/35.webp)



Sekarang Anda dapat menggunakannya untuk terhubung dengan mudah ke berbagai akun web Anda.



![Image](assets/fr/36.webp)



Sekarang Anda sudah tahu cara menggunakan pengelola kata sandi PearPass. Di luar alat ini, keamanan digital sehari-hari bergantung pada penggunaan solusi yang tepat. Jika Anda ingin mempelajari cara menyiapkan lingkungan digital pribadi yang aman, stabil, dan efisien, saya mengundang Anda untuk mengikuti kursus pelatihan kami yang didedikasikan untuk topik ini:



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1