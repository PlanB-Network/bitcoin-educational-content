---
name: RoninDojo v2
description: Memasang node Bitcoin RoninDojo v2 Anda pada Raspberry Pi
---
![cover RoninDojo v2](assets/cover.webp)

***PERINGATAN:** Menyusul penangkapan pendiri Samourai Wallet dan penyitaan server mereka pada 24 April, beberapa fitur RoninDojo, seperti Whirlpool, tidak lagi beroperasi. Namun, ada kemungkinan bahwa alat-alat ini dapat dipulihkan atau diluncurkan kembali dengan cara yang berbeda dalam beberapa minggu mendatang. Selain itu, karena kode RoninDojo di-host di GitLab Samourai, yang juga disita, saat ini tidak mungkin untuk mengunduh kode secara remote. Tim RoninDojo kemungkinan sedang bekerja untuk menerbitkan ulang kode tersebut.*

_Kami sedang mengikuti perkembangan kasus ini serta perkembangan terkait alat-alat yang terkait. Yakinlah bahwa kami akan memperbarui tutorial ini seiring dengan tersedianya informasi baru._

_Tutorial ini disediakan hanya untuk tujuan pendidikan dan informasi. Kami tidak mendukung atau mendorong penggunaan alat-alat ini untuk tujuan kriminal. Tanggung jawab setiap pengguna untuk mematuhi hukum di yurisdiksi mereka._

---

> "*Gunakan Bitcoin dengan privasi.*"

Dalam [tutorial sebelumnya](https://planb.network/tutorials/node/bitcoin/ronin-dojo-31d96647-029b-43e8-9fb5-95ec5dde72b0), kami telah menjelaskan prosedur untuk memasang dan menggunakan RoninDojo v1. Namun, selama setahun terakhir, tim RoninDojo telah meluncurkan versi 2 dari implementasi mereka, yang menandai titik balik penting dalam arsitektur perangkat lunak. Memang, mereka beralih dari distribusi Linux Manjaro ke Debian. Akibatnya, mereka tidak lagi menawarkan gambar yang telah dikonfigurasi sebelumnya untuk instalasi otomatis pada Raspberry Pi. Namun, masih ada metode untuk melanjutkan dengan instalasi manual. Inilah yang saya gunakan untuk node saya sendiri, dan sejak itu, RoninDojo v2 telah bekerja dengan luar biasa di Raspberry Pi 4 saya. Oleh karena itu, saya menawarkan tutorial baru tentang cara memasang RoninDojo v2 secara manual pada Raspberry Pi.

## Daftar Isi:
- Apa itu RoninDojo?
- Perangkat keras apa yang harus dipilih untuk memasang RoninDojo v2?
- Bagaimana cara merakit Raspberry Pi 4?
- Bagaimana cara memasang RoninDojo v2 pada Raspberry Pi 4?
- Bagaimana cara menggunakan node RoninDojo v2 Anda?

## Apa itu RoninDojo?
Dojo pada awalnya adalah implementasi node Bitcoin penuh, berbasis Bitcoin Core, dan dikembangkan oleh tim Samourai Wallet. Solusi ini dapat dipasang pada perangkat apa pun. Tidak seperti implementasi Core lainnya, Dojo telah dioptimalkan khusus untuk berintegrasi dengan lingkungan aplikasi Android dari Samourai Wallet. Sedangkan untuk RoninDojo, ini adalah utilitas yang dirancang untuk memfasilitasi pemasangan dan pengelolaan Dojo, serta berbagai alat pelengkap lainnya. Singkatnya, RoninDojo memperkaya implementasi dasar Dojo dengan mengintegrasikan banyak alat tambahan, sambil menyederhanakan pemasangan dan pengelolaannya.

Ronin juga menawarkan [solusi node-dalam-kotak, yang disebut "*Tanto*"](https://ronindojo.io/en/products), sebuah perangkat dengan RoninDojo yang sudah dipasang pada sistem yang dirakit oleh tim mereka. Tanto adalah opsi berbayar, yang mungkin menarik bagi mereka yang ingin menghindari komplikasi teknis. Namun, karena kode sumber RoninDojo terbuka, juga mungkin untuk menerapkannya pada perangkat keras Anda sendiri. Alternatif ini, yang lebih ekonomis, tetap memerlukan beberapa manipulasi tambahan, yang akan kami bahas dalam tutorial ini.
RoninDojo adalah sebuah Dojo, sehingga memungkinkan integrasi mudah dari Whirlpool CLI ke dalam node Bitcoin Anda untuk memberikan pengalaman coinjoin terbaik yang mungkin. Dengan Whirlpool CLI, menjadi mungkin untuk terus menerus remix bitcoin Anda, 24 jam sehari, 7 hari seminggu, tanpa memerlukan komputer pribadi Anda untuk tetap menyala.

Lebih dari Whirlpool CLI, RoninDojo mencakup berbagai alat untuk meningkatkan fungsionalitas Dojo Anda. Di antaranya, kalkulator Boltzmann menganalisis tingkat privasi transaksi Anda, server Electrum memungkinkan untuk menghubungkan dompet Bitcoin Anda ke node Anda, dan server Mempool memungkinkan Anda untuk melihat transaksi Anda secara lokal, tanpa membocorkan informasi.

Dibandingkan dengan solusi node lain seperti Umbrel, RoninDojo jelas fokus pada solusi on-chain dan alat privasi. Tidak seperti Umbrel, RoninDojo tidak mendukung pengaturan node Lightning maupun integrasi aplikasi server yang lebih umum. Meskipun RoninDojo menawarkan alat yang lebih sedikit serbaguna daripada Umbrel, ia memiliki semua fungsionalitas esensial untuk mengelola aktivitas on-chain Anda.

Jika Anda tidak memerlukan fungsionalitas umum atau yang terkait dengan Jaringan Lightning seperti yang ditawarkan oleh Umbrel, dan Anda mencari node sederhana, stabil dengan alat esensial seperti Whirlpool atau Mempool, RoninDojo bisa menjadi solusi ideal. Sementara Umbrel cenderung menjadi server multitasking mini yang berorientasi pada Jaringan Lightning dan serbaguna, RoninDojo, sejalan dengan filosofi Samourai Wallet, fokus pada alat fundamental untuk privasi pengguna.

Sekarang setelah kami telah menguraikan RoninDojo, mari kita lihat bersama bagaimana cara mengatur node ini.

## Perangkat keras apa yang harus dipilih untuk menginstal RoninDojo v2?
RoninDojo menawarkan sebuah gambar untuk instalasi otomatis perangkat lunaknya pada [RockPro64](https://ronindojo.io/en/download). Namun, tutorial kami berfokus pada prosedur instalasi manual pada Raspberry Pi 4. Meskipun Raspberry Pi 5 telah diluncurkan baru-baru ini, dan tutorial ini secara teoritis harus kompatibel dengan model baru ini, saya belum memiliki kesempatan untuk mengujinya secara pribadi, dan saya belum menemukan umpan balik dari komunitas. Secepatnya saya mendapatkan Pi 5 dan komponen yang kompatibel, saya akan memperbarui tutorial ini untuk menjaga Anda tetap terinformasi. Sementara itu, saya merekomendasikan untuk memprioritaskan Pi 4, karena bekerja dengan sempurna untuk node saya.
Dari pihak saya, saya menjalankan RoninDojo pada Raspberry Pi yang dilengkapi dengan 8 GB RAM. Meskipun beberapa anggota komunitas telah berhasil membuatnya bekerja pada perangkat dengan hanya 4 GB RAM, saya belum menguji konfigurasi ini sendiri. Mengingat perbedaan harga yang kecil, tampaknya bijaksana untuk memilih versi RAM 8 GB. Ini juga bisa berguna jika Anda berencana untuk menggunakan kembali Raspberry Pi Anda untuk kegunaan lain di masa depan.
Penting untuk dicatat bahwa tim RoninDojo telah melaporkan masalah yang sering terkait dengan casing dan adaptor SSD. Saya telah menghadapi masalah ini sendiri. **Oleh karena itu, sangat disarankan untuk menghindari casing yang dilengkapi dengan kabel USB untuk SSD node Anda.** Sebagai gantinya, pilihlah kartu ekspansi penyimpanan yang dirancang khusus untuk Raspberry Pi Anda:

![kartu ekspansi penyimpanan RPI4](assets/notext/1.webp)
Untuk menyimpan blockchain Bitcoin, Anda akan memerlukan SSD yang kompatibel dengan kartu ekspansi penyimpanan yang telah Anda pilih. Saat ini (Februari 2024), kita berada dalam fase transisi. Diperkirakan, dalam beberapa bulan, disk 1 TB tidak akan lagi cukup untuk menampung ukuran blockchain yang terus bertambah, terutama mengingat berbagai aplikasi yang Anda rencanakan untuk diintegrasikan ke dalam node Anda. Beberapa orang oleh karena itu merekomendasikan untuk berinvestasi pada SSD 2 TB demi ketenangan pikiran dalam jangka panjang. Namun, dengan tren penurunan harga SSD dari tahun ke tahun, yang lain menyarankan untuk memilih disk 1 TB, yang seharusnya cukup untuk satu atau dua tahun, dengan argumen bahwa pada saat itu menjadi usang, biaya model 2 TB kemungkinan akan telah menurun. Pilihan ini tergantung pada preferensi pribadi Anda. Jika Anda berencana untuk menjaga RoninDojo Anda untuk durasi yang signifikan dan ingin menghindari penanganan teknis dalam beberapa tahun mendatang, opsi SSD 2 TB tampaknya menjadi pilihan yang paling bijaksana, karena menawarkan Anda margin yang nyaman untuk masa depan.
Selain itu, Anda akan memerlukan berbagai komponen kecil:
- Sebuah casing yang dilengkapi dengan kipas untuk menampung Raspberry Pi Anda dan kartu ekspansi penyimpanan Anda. Kit yang mencakup baik kartu ekspansi SSD dan casing yang kompatibel tersedia secara online;
- Sebuah kabel daya untuk Raspberry Pi Anda;
- Sebuah kartu micro SD setidaknya 16 GB (meskipun 8 GB secara teknis bisa cukup, perbedaan harga antara kartu 8 dan 16 GB sering kali tidak signifikan);
- Sebuah kabel Ethernet RJ45 untuk koneksi jaringan.

![node material](assets/notext/2.webp)

## Bagaimana cara merakit Raspberry Pi 4?
Perakitan node Anda akan bervariasi tergantung pada perangkat keras yang dipilih, terutama jenis casing. Namun, garis besar umum langkah-langkah yang harus diikuti umumnya serupa dalam perakitan.
Mulailah dengan memasang SSD Anda pada kartu ekspansi penyimpanan, dengan berhati-hati mengamankan dua sekrup pengunci di bagian belakang.

![assembly1](assets/notext/3.webp)

Kemudian pasang Raspberry Pi Anda ke kartu ekspansi.

![assembly2](assets/notext/4.webp)

Juga, pasang kipas ke Raspberry Pi.

![assembly3](assets/notext/5.webp)

Sambungkan berbagai komponen, dengan memperhatikan untuk menggunakan pin yang benar, merujuk pada manual casing Anda. Produsen casing sering menawarkan tutorial video untuk membantu Anda dalam perakitan. Dalam kasus saya, saya memiliki kartu ekspansi tambahan yang dilengkapi dengan tombol on/off. Ini bukan hal yang esensial untuk membuat node Bitcoin. Saya terutama menggunakannya untuk memiliki tombol daya.

Jika, seperti saya, Anda memiliki kartu ekspansi yang dilengkapi dengan tombol on/off, jangan lupa untuk memasang jumper "Auto Power On" kecil. Ini akan memungkinkan node Anda untuk mulai secara otomatis segera setelah dinyalakan. Fitur ini sangat berguna dalam hal terjadi pemadaman listrik, karena memungkinkan node Anda untuk memulai ulang sendiri, tanpa intervensi manual dari Anda.

![assembly4](assets/notext/6.webp)

Sebelum memasukkan semua perangkat keras ke dalam casing, penting untuk memeriksa fungsi yang benar dari Raspberry Pi Anda, kartu ekspansi penyimpanan, dan kipas dengan menghidupkannya.

![assembly5](assets/notext/7.webp)
Akhirnya, pasang Raspberry Pi Anda ke dalam casingnya. Perlu diingat, langkah selanjutnya akan memerlukan penambahan kartu micro SD ke dalam port yang sesuai pada Raspberry Pi. Jika casing Anda dilengkapi dengan bukaan yang memungkinkan Anda memasukkan kartu SD tanpa harus membukanya (seperti pada kasus saya yang diilustrasikan dalam foto), Anda dapat melanjutkan untuk menutup casing sekarang. Namun, jika casing Anda tidak memiliki akses langsung ke port micro SD, Anda perlu menunggu sampai Anda telah mempersiapkan kartu micro SD untuk memasukkannya sebelum menyelesaikan perakitan.

## Bagaimana cara menginstal RoninDojo v2 di Raspberry Pi 4?

### Langkah 1: Persiapkan kartu micro SD yang dapat boot
Setelah merakit perangkat keras Anda, langkah selanjutnya adalah menginstal RoninDojo. Untuk ini, kita akan menyiapkan kartu micro SD yang dapat boot dari komputer Anda, dengan membakar gambar disk yang sesuai ke dalamnya.
Anda perlu menggunakan perangkat lunak _**Raspberry Pi Imager**_, yang dirancang untuk memudahkan pengunduhan, konfigurasi, dan penulisan sistem operasi pada kartu micro SD untuk digunakan dengan Raspberry Pi. Mulailah dengan menginstal perangkat lunak ini di PC pribadi Anda:
- Untuk Ubuntu/Debian: https://downloads.raspberrypi.org/imager/imager_latest_amd64.deb
- Untuk Windows: https://downloads.raspberrypi.org/imager/imager_latest.exe
- Untuk Mac: https://downloads.raspberrypi.org/imager/imager_latest.dmg

Setelah perangkat lunak terinstal, bukalah, dan masukkan kartu micro SD Anda ke dalam komputer pribadi Anda. Dari antarmuka Raspberry Pi Imager, pilih `CHOOSE OS`:

Selanjutnya, pergi ke menu `Raspberry Pi OS (other)`:

Pilih sistem operasi yang bernama `Raspberry Pi OS (Legacy, 64-bit) Lite`, yang berukuran `0.3 GB`:

Setelah memilih sistem operasi, Anda akan diarahkan kembali ke menu utama Raspberry Pi Imager. Klik pada `CHOOSE STORAGE`:

Pilih kartu micro SD Anda:

Setelah memilih sistem operasi dan kartu micro SD, klik pada `NEXT`:

Jendela baru akan muncul. Pilih `EDIT CONFIGURATION`:

Di jendela ini, pergi ke tab `GENERAL` dan buat pengaturan berikut (yang sangat penting agar dapat bekerja):
- Aktifkan opsi dan tetapkan `RoninDojo` sebagai hostname;
- Aktifkan `Set username and password`, masukkan `pi` sebagai username, pilih password, dan catat informasi ini, karena akan dibutuhkan nanti. Kredensial ini bersifat sementara dan akan dihapus setelahnya;
- Nonaktifkan `Configure Wi-Fi`;
- Aktifkan `Set locale settings` dan pilih zona waktu Anda serta jenis keyboard yang sesuai dengan komputer Anda;

Di tab SERVICES, klik pada kotak `Enable SSH` dan pilih `Use a password for authentication`:

Juga, pastikan bahwa di tab `OPTIONS`, telemetri dinonaktifkan:

Klik pada `SAVE`:
Konfirmasi dengan mengklik `YES` untuk mulai membuat kartu micro SD yang dapat boot:

![settings yes](assets/notext/20.webp)

Sebuah pesan akan memberitahu Anda bahwa semua data pada kartu micro SD akan dihapus. Konfirmasi dengan mengklik `YES` untuk memulai proses:

![overwrite micro SD](assets/notext/21.webp)

Tunggu sampai perangkat lunak selesai menyiapkan kartu micro SD Anda:

![writing micro SD](assets/notext/22.webp)

Ketika pesan yang menunjukkan akhir proses muncul, Anda dapat melepas kartu micro SD dari komputer Anda:

![writing micro SD completed](assets/notext/23.webp)

### Langkah 2: Lengkapi Perakitan Node
Anda sekarang dapat memasukkan kartu micro SD ke dalam port yang sesuai pada Raspberry Pi Anda.

![micro SD](assets/notext/24.webp)

Kemudian, hubungkan Raspberry Pi Anda ke router menggunakan kabel Ethernet. Akhirnya, nyalakan node Anda dengan menghubungkan kabel daya dan menekan tombol daya (jika setup Anda menyertakannya).

### Langkah 3: Membangun Koneksi SSH dengan Node
Pertama, perlu untuk menemukan alamat IP dari node Anda. Anda memiliki opsi untuk menggunakan alat seperti _[Advanced IP Scanner](https://www.advanced-ip-scanner.com/)_ atau _[Angry IP Scanner](https://angryip.org/)_, atau memeriksa antarmuka administrasi router Anda. Alamat IP harus dalam bentuk `192.168.1.??`. **Untuk semua perintah berikut, ganti `[IP]` dengan alamat IP sebenarnya dari node Anda**, (menghilangkan tanda kurung).

Luncurkan terminal.

Untuk menghapus kunci yang mungkin sudah terasosiasi dengan alamat IP dari node Anda, jalankan perintah: 
`ssh-keygen -R [IP]`. 

Kesalahan setelah perintah ini tidak serius; itu hanya berarti bahwa kunci tidak ada dalam daftar host yang dikenal Anda (yang cukup mungkin). Misalnya, jika IP dari node Anda adalah `192.168.1.40`, perintahnya menjadi: `ssh-keygen -R 192.168.1.40`.

Selanjutnya, bangun koneksi SSH dengan node Anda dengan menjalankan perintah: 
`ssh pi@[IP]`.
Sebuah pesan akan muncul mengenai keaslian host: `The authenticity of host '[IP]' can't be established.` Ini menunjukkan bahwa keaslian perangkat yang Anda coba hubungkan tidak dapat diverifikasi karena kurangnya kunci publik yang dikenal. Ketika menghubungkan via SSH ke host baru untuk pertama kalinya, pesan ini akan selalu muncul. Anda harus merespon `yes` untuk menambahkan kunci publiknya ke direktori lokal Anda, yang akan mencegah pesan peringatan ini muncul selama koneksi SSH masa depan ke node ini. Oleh karena itu, ketik `yes` dan tekan `enter` untuk memvalidasi.
Anda kemudian akan diminta untuk memasukkan kata sandi Anda, yang sebelumnya ditetapkan sebagai sementara di langkah 1. Validasi dengan `enter`. Anda kemudian akan terhubung ke node Anda via SSH.

Ringkasnya, berikut adalah perintah untuk dijalankan:
- `ssh-keygen -R [IP]`
- `ssh pi@[IP]`
- `yes`
- Masukkan kata sandi sementara dan validasi.

### Langkah 4: Pembaruan dan Persiapan
Anda sekarang terhubung ke node Anda via sesi SSH. Di terminal Anda, prompt perintah harusnya: `pi@RoninDojo:~ $`. Untuk memulai, perbarui daftar paket yang tersedia dan instal pembaruan untuk paket yang sudah ada dengan perintah berikut:
`sudo apt update && sudo apt upgrade -y`
Setelah pembaruan selesai, lanjutkan untuk menginstal *Git* dan *Dialog* menggunakan perintah: `sudo apt install git dialog -y`

Selanjutnya, kloning cabang `master` dari repositori Git _RoninOS_ dengan menjalankan:
`sudo git clone --branch master https://code.samourai.io/ronindojo/RoninOS.git /opt/RoninOS`

Jalankan skrip `customize-image.sh` dengan perintah:
`cd /opt/RoninOS/ && sudo ./customize-image.sh`

**Penting untuk membiarkan skrip berjalan tanpa gangguan dan menunggu dengan sabar hingga prosesnya selesai**, yang memakan waktu sekitar 10 menit. Ketika pesan `Setup is complete` muncul, Anda dapat melanjutkan ke langkah selanjutnya.

### Langkah 5: Menjalankan RoninOS
Jalankan RoninOS dengan perintah:
`sudo systemctl start ronin-setup`

Tampilkan baris-baris file log dengan perintah:
`tail -f /home/ronindojo/.logs/setup.logs`

Pada tahap ini, **penting untuk membiarkan RoninOS berjalan dan menunggu hingga selesai**. Ini memakan waktu sekitar 40 menit. Ketika `All RoninDojo feature installations complete!` muncul, Anda dapat melanjutkan ke langkah 6.

### Langkah 6: Mengakses RoninUI dan Mengubah Kredensial
Setelah menyelesaikan instalasi, untuk terhubung ke node Anda melalui browser, pastikan komputer pribadi Anda terhubung ke jaringan lokal yang sama dengan node Anda. Jika Anda menggunakan VPN pada mesin Anda, nonaktifkan sementara. Untuk mengakses antarmuka node di browser Anda, masukkan di bilah URL:
- Langsung alamat IP node Anda, misalnya, `192.168.1.??`;
- Atau, ketik `ronindojo.local`.

Setelah berada di halaman utama RoninUI, Anda akan diminta untuk memulai pengaturan. Untuk melakukan ini, klik tombol `Let's start`.

![lets start](assets/notext/25.webp)

Pada tahap ini, RoninUI menampilkan kata sandi `root` Anda. Sangat penting untuk menjaganya dengan aman. Anda dapat memilih untuk membuat cadangan fisik, di atas kertas, atau menyimpannya dalam [pengelola kata sandi](https://planb.network/courses/secu101/4/2).

![root password](assets/notext/26.webp)

Setelah menyimpan kata sandi `root`, centang kotak `I have backed up Root user credentials` dan klik `Continue` untuk melanjutkan.

![confirm root password](assets/notext/27.webp)

Langkah selanjutnya melibatkan pembuatan kata sandi pengguna, yang akan digunakan baik untuk mengakses antarmuka web RoninUI maupun untuk menjalin sesi SSH dengan node Anda. Pilih kata sandi yang kuat dan pastikan untuk menyimpannya dengan aman. Anda perlu memasukkan kata sandi ini dua kali sebelum mengklik `Finish` untuk memvalidasi. Untuk nama pengguna, disarankan untuk mempertahankan pilihan default, `ronindojo`. Jika Anda memutuskan untuk mengubahnya, ingat untuk menyesuaikan perintah pada langkah-langkah berikutnya sesuai kebutuhan.

![user credentials](assets/notext/28.webp)

Setelah tindakan ini selesai, tunggu node Anda untuk diinisialisasi. Anda kemudian akan mengakses antarmuka web RoninUI. Anda hampir di akhir proses, hanya beberapa langkah kecil lagi!
![Ronin UI](assets/notext/29.webp)

### Langkah 7: Menghapus Kredensial Sementara
Buka terminal baru di komputer pribadi Anda dan buat koneksi SSH dengan node Anda menggunakan perintah berikut:
`SSH ronindojo@[IP]`
Jika, misalnya, alamat IP dari node Anda adalah `192.168.1.40`, perintah yang tepat akan menjadi: `SSH ronindojo@192.168.1.40`

Jika Anda mengganti nama pengguna Anda pada langkah sebelumnya, menggantikan nama pengguna default (`ronindojo`) dengan yang lain, pastikan untuk menggunakan nama baru ini dalam perintah. Sebagai contoh, jika Anda memilih `planb` sebagai nama pengguna dan alamat IP adalah `192.168.1.40`, perintah yang harus dimasukkan adalah:
`SSH planb@192.168.1.40`
Anda akan diminta untuk memasukkan kata sandi pengguna. Masukkan dan kemudian tekan `enter` untuk memvalidasi. Anda kemudian akan mengakses antarmuka RoninCLI. Gunakan tombol panah pada keyboard Anda untuk menavigasi ke opsi `Exit RoninDojo` dan tekan `enter` untuk memilihnya.
![RoninCLI](assets/notext/30.webp)

Pada titik ini, Anda berada di terminal node Anda, dengan prompt perintah mirip dengan: `ronindojo@RoninDojo:~ $`. Untuk menghapus pengguna sementara yang dibuat selama konfigurasi kartu micro SD yang dapat di-boot, masukkan perintah berikut dan tekan `enter`:
`sudo deluser --remove-home pi`

Anda akan diminta untuk mengonfirmasi kata sandi pengguna Anda. Masukkan dan validasi dengan menekan `enter`. Tunggu hingga operasi selesai, kemudian gunakan perintah `exit` untuk meninggalkan terminal.

Selamat! Node RoninDojo v2 Anda sekarang dikonfigurasi dan siap digunakan. Ini akan memulai IBD (*Initial Block Download*), melanjutkan untuk mengunduh dan memverifikasi blockchain Bitcoin dari blok Genesis. Langkah ini melibatkan pengambilan semua transaksi Bitcoin yang dilakukan sejak 3 Januari 2009, dan membutuhkan waktu. Setelah blockchain sepenuhnya diunduh, pengindeks akan melanjutkan untuk mengompresi database. Durasi IBD dapat bervariasi secara signifikan. Node RoninDojo Anda akan sepenuhnya operasional setelah proses ini selesai.

**Jika Anda bermigrasi dari node RoninDojo v1 lama** ke versi baru ini dengan tutorial ini sambil mempertahankan SSD yang sama, node Anda seharusnya secara otomatis mendeteksi dan menggunakan kembali data yang ada di disk, menghemat Anda dari keharusan melakukan IBD lagi. Dalam kasus ini, Anda hanya perlu menunggu node Anda untuk resinkronisasi dengan blok terbaru.

### Langkah 8: "veth* fix"
Jika Anda menemui bug dengan RoninDojo v2 Anda di Raspberry Pi, di mana setelah instalasi tanpa masalah, node Anda tiba-tiba menjadi tidak dapat dijangkau melalui SSH tetapi pulih setelah restart sederhana, maka Anda perlu mengikuti langkah 8 ini. Bug umum ini dapat dengan mudah diperbaiki dengan solusi yang dikembangkan oleh komunitas: "_veth fix_". Koreksi kecil ini secara permanen mengatasi pemutusan mendadak. Berikut cara menerapkannya.

Buka terminal baru di komputer pribadi Anda dan buat koneksi SSH dengan node Anda menggunakan perintah berikut:
`SSH ronindojo@[IP]`

Jika, misalnya, alamat IP node Anda adalah `192.168.1.40`, perintah yang tepat akan menjadi:
`SSH ronindojo@192.168.1.40`

Anda akan diminta untuk memasukkan kata sandi pengguna. Masukkan dan tekan `enter` untuk memvalidasi. Anda kemudian akan mengakses antarmuka RoninCLI. Gunakan panah keyboard Anda untuk menavigasi ke opsi `Exit RoninDojo` dan tekan `enter` untuk memilihnya.
Pada titik ini, Anda berada di terminal node Anda, dengan prompt perintah serupa dengan: `ronindojo@RoninDojo:~ $`. Untuk menerapkan perbaikan veth*, ketik perintah berikut dan tekan `enter`: `sudo nano /etc/dhcpcd.conf`

Konfirmasi password Anda lagi dan tekan `enter`.

Anda akan tiba di file `dhcpcd.conf`. Anda perlu menyalin teks berikut, pastikan untuk menyertakan asterisk, dan tambahkan ke bagian bawah file:
`denyinterfaces veth*`

Untuk melakukan ini, pindah ke bagian bawah file menggunakan panah bawah pada keyboard Anda, kemudian gunakan klik kanan mouse Anda untuk menempelkan teks pada baris independen.

Setelah menambahkan teks, tekan `ctrl X` untuk mulai keluar, diikuti dengan `ctrl Y` untuk mengonfirmasi menyimpan perubahan, dan tekan `enter` untuk menyelesaikan dan kembali ke prompt perintah. Untuk memastikan bahwa modifikasi telah diterapkan dengan benar, buka kembali file `dhcpcd.conf` menggunakan perintah yang sesuai.

Untuk menyelesaikan penerapan perbaikan, restart node Anda dengan menjalankan:
`sudo reboot now`

Pada titik ini, Anda dapat menutup terminal Anda. Berikan waktu yang diperlukan untuk RoninDojo Anda untuk restart, setelah itu Anda seharusnya dapat terhubung kembali melalui antarmuka grafis browser Anda. Proses ini seharusnya memperbaiki bug yang ditemui.

## Bagaimana cara menggunakan node RoninDojo v2 Anda?

### Menghubungkan perangkat lunak dompet Anda ke Electrs
Penggunaan pertama dari node yang baru saja Anda instal dan sinkronkan akan untuk menyiarkan transaksi Anda ke jaringan Bitcoin. Anda mungkin ingin menghubungkan berbagai dompet Anda ke node Anda untuk menyiarkan transaksi Anda secara rahasia. Anda dapat melakukan ini melalui Electrum Rust Server (electrs). Aplikasi ini biasanya sudah terpasang di node RoninDojo Anda. Jika tidak, Anda bisa menginstalnya secara manual melalui antarmuka RoninCLI di `Applications > Manage Applications > Install Electrum Server`.

Untuk mendapatkan alamat Tor dari Electrum Server Anda, dari antarmuka web RoninUI, pergi ke:
`Pairing > Electrum server > Pair now`
![Pairing](assets/notext/31.webp)
![Electrs](assets/notext/32.webp)
Anda kemudian perlu memasukkan alamat `Hostname` yang berakhir dengan `.onion` di perangkat lunak dompet Anda, disertai dengan port `50001`. ![hostname](assets/notext/33.webp)
Sebagai contoh, di Sparrow Wallet, cukup pergi ke tab:
`File > Preferences > Server > Private Electrum`

![Sparrow](assets/notext/34.webp)

### Menghubungkan perangkat lunak dompet Anda ke Samourai Dojo
Sebagai alternatif untuk menggunakan Electrs, Dojo memungkinkan Anda untuk menghubungkan perangkat lunak dompet yang kompatibel langsung ke node RoninDojo Anda. Dompet seperti Samourai Wallet dan Sentinel menawarkan fungsionalitas ini.

Untuk membangun koneksi, Anda hanya perlu memindai kode QR dari Dojo Anda. Untuk mengakses kode QR ini melalui RoninUI, navigasikan ke:
`Pairing > Samourai Dojo > Pair now`
![Samourai Dojo](assets/notext/35.webp)
Untuk menghubungkan Samourai Wallet Anda ke Dojo, cukup pindai kode QR ini selama instalasi aplikasi:

![Samourai Wallet connection](assets/notext/36.webp)
Jika Anda sudah memiliki Samourai Wallet sebelum mengatur Ronin Dojo Anda, perlu untuk membackup dompet Anda, menghapus instalasi dan kemudian menginstal ulang aplikasi Samourai Wallet, sebelum mengembalikan dompet Anda. Saat meluncurkan aplikasi yang telah diinstal ulang, Anda akan memiliki opsi untuk terhubung ke Dojo baru. **Hati-hati, proses ini membawa risiko kehilangan bitcoin Anda jika tidak dilakukan dengan benar!** Pastikan Anda memiliki backup dari Samourai wallet Anda dalam file Anda dan verifikasi validitas passphrase Anda melalui `Settings > Troubleshoot > Passphrase`. Juga penting untuk memiliki backup yang dapat dibaca dari frase pemulihan dan passphrase Anda. Untuk lebih presisi dalam operasi ini, disarankan untuk mengikuti tutorial terperinci ini: [https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai](https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai).

### Menggunakan block explorer Mempool.space milik Anda sendiri
Sebuah block explorer mengubah informasi mentah dari blockchain Bitcoin menjadi format yang terstruktur dan mudah dibaca. Dengan alat seperti *Mempool.space*, dimungkinkan untuk menganalisis transaksi, mencari alamat tertentu, atau bahkan konsultasi tarif rata-rata jaringan mempool secara real-time.

Namun, menggunakan block explorer online menimbulkan risiko terhadap privasi Anda dan melibatkan kepercayaan pada data yang disediakan oleh pihak ketiga. Memang, dengan menggunakan layanan ini tanpa melalui node Anda sendiri, Anda dapat tanpa sengaja mengungkapkan informasi tentang transaksi Anda dan harus mengandalkan akurasi informasi yang disajikan oleh pemilik situs.
Untuk mengurangi risiko ini, disarankan untuk menggunakan instance *Mempool.space* Anda sendiri melalui jaringan Tor, langsung dihosting pada node Anda. Solusi ini memastikan pelestarian privasi Anda dan otonomi data Anda.
Untuk melakukan ini, mulailah dengan menginstal *Mempool Space Visualizer* dari RoninUI. Di antarmuka web, pergi ke tab `Dashboard` dan klik pada `Manage` di bawah `Mempool Space`:
`Dashboard > Mempool Space > Manage`
![Manage mempool](assets/notext/37.webp)
Kemudian klik pada tombol `Install Mempool visualizer`:
![install mempool](assets/notext/38.webp)
Konfirmasi password pengguna Anda:
![password mempool](assets/notext/39.webp)
Tunggu hingga instalasi selesai, kemudian klik lagi pada tombol `Manage`:
![Mempool Manage](assets/notext/40.webp)
Anda akan mendapatkan link `.onion` untuk mengakses instance *Mempool.space* Anda sendiri melalui jaringan Tor.
![Mempool link](assets/notext/41.webp)
Saya menyarankan Anda untuk menyimpan link ini di favorit Anda pada browser Tor atau menambahkannya ke aplikasi Browser Tor di smartphone Anda untuk akses yang mudah dan aman dari mana saja. Jika Anda belum memiliki browser Tor, Anda dapat mengunduhnya di sini: [https://www.torproject.org/download/](https://www.torproject.org/download/)
![Mempool Tor](assets/notext/42.webp)

### Menggunakan Whirlpool untuk mencampur bitcoin Anda
Node RoninDojo Anda juga mengintegrasikan _WhirlpoolCLI_, antarmuka baris perintah yang memungkinkan otomatisasi Whirlpool coinjoins, dan _WhirlpoolGUI_, antarmuka grafis yang dirancang untuk berinteraksi dengan _WhirlpoolCLI_.
Melakukan coinjoin melalui Whirlpool memerlukan aplikasi yang digunakan untuk tetap aktif dalam melakukan remix. Kondisi ini bisa menjadi pembatas bagi mereka yang ingin mencapai tingkat anonim yang tinggi. Memang, perangkat yang menghosting aplikasi yang mengintegrasikan Whirlpool harus tetap menyala secara terus-menerus. Ini berarti untuk berpartisipasi dalam remix 24 jam sehari, komputer atau smartphone Anda harus tetap menyala dengan Samourai atau Sparrow terbuka terus-menerus. Solusi untuk kendala ini adalah menggunakan _WhirlpoolCLI_ pada mesin yang selalu aktif, seperti node Bitcoin, memungkinkan koin Anda untuk remix tanpa gangguan, dan tanpa perlu menjaga perangkat lain tetap menyala.
Tutorial terperinci sedang disiapkan untuk memandu Anda langkah demi langkah melalui proses coinjoining dengan Samourai Wallet dan RoninDojo v2, dari A sampai Z.

Untuk pemahaman yang lebih mendalam tentang coinjoin dan penggunaannya pada Bitcoin, saya juga mengundang Anda untuk membaca artikel lain ini: [Memahami dan menggunakan coinjoin pada Bitcoin](https://planb.network/tutorials/privacy/on-chain/coinjoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2), di mana saya menjelaskan segala hal yang perlu Anda ketahui tentang teknik ini.
### Menggunakan Whirlpool Stat Tool (WST)

Setelah melakukan coinjoins dengan Whirlpool, berguna untuk mengevaluasi secara tepat tingkat privasi yang dicapai untuk UTXO campuran Anda. Untuk melakukan ini, Anda dapat menggunakan alat Python *Whirlpool Stat Tool*. Alat ini memungkinkan Anda untuk mengukur baik skor prospektif maupun retrospektif dari UTXO Anda, sambil menganalisis tingkat difusi mereka di kolam.

Untuk memperdalam pemahaman Anda tentang mekanisme perhitungan anonset ini, saya merekomendasikan membaca artikel: [REMIX - WHIRLPOOL](https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa), yang menjelaskan fungsi dari indeks-indeks ini.

Untuk mengakses alat WST, buka RoninCLI. Untuk melakukan ini, buka terminal pada komputer pribadi Anda dan buat koneksi SSH dengan node Anda menggunakan perintah berikut:
`SSH ronindojo@[IP]`

Jika, misalnya, alamat IP node Anda adalah `192.168.1.40`, perintah yang tepat adalah:
`SSH ronindojo@192.168.1.40`

Jika Anda mengubah nama pengguna Anda selama langkah 6, menggantikan nama pengguna default (`ronindojo`) dengan yang lain, pastikan untuk menggunakan nama baru ini dalam perintah. Misalnya, jika Anda memilih `planb` sebagai nama pengguna Anda dan alamat IP adalah `192.168.1.40`, perintah yang harus dimasukkan adalah:
`SSH planb@192.168.1.40`

Anda akan diminta untuk memasukkan kata sandi pengguna. Masukkan dan tekan `enter` untuk memvalidasi. Anda kemudian akan mengakses antarmuka RoninCLI. Gunakan tombol panah pada keyboard Anda untuk menavigasi ke menu `Samourai Toolkit` dan tekan `enter` untuk memilihnya:

![Samourai Toolkit](assets/notext/43.webp)

Kemudian pilih `Whirlpool Stat Tool`:

![WST](assets/notext/44.webp)

Setelah menginisialisasi WST, alat akan melanjutkan dengan instalasi otomatisnya. Tunggu selama langkah ini. Instruksi penggunaan akan bergulir. Setelah instalasi selesai, tekan tombol apa saja untuk mengakses terminal WST:

![Perintah WST](assets/notext/45.webp)

Prompt perintah berikut akan ditampilkan:
`wst#/tmp>`

Jika Anda ingin keluar dari antarmuka ini dan kembali ke menu RoninCLI, cukup masukkan:
`quit`

Pertama, perlu mengkonfigurasi proxy untuk menggunakan Tor, untuk memastikan kerahasiaan saat mengekstrak data dari OXT. Masukkan perintah:
`socks5 127.0.0.1:9050`
Selanjutnya, lanjutkan untuk mengunduh informasi pool yang berisi transaksi Anda:
`download 0001`
Ganti `0001` dengan kode denominasi pool yang Anda minati. Kode denominasi tersebut adalah sebagai berikut di WST:
- Pool 0.5 bitcoin: `05`
- Pool 0.05 bitcoin: `005`
- Pool 0.01 bitcoin: `001`
- Pool 0.001 bitcoin: `0001`

Setelah mengunduh, muat data dengan mengganti `0001` dengan kode pool Anda dalam perintah ini: `load 0001`

![WST loading](assets/notext/46.webp)

Tunggu hingga proses pemuatan selesai, yang mungkin memakan waktu beberapa menit. Setelah data dimuat, untuk mengetahui skor anonset koin Anda, eksekusi perintah `score` diikuti oleh TXID Anda (tanpa tanda kurung):
`score [TXID]`

![WST score](assets/notext/47.webp)

WST kemudian akan menampilkan skor retrospektif (_Backward-looking metrics_), diikuti oleh skor prospektif (_Forward-looking metrics_). Selain skor anonset, WST juga akan menunjukkan tingkat difusi transaksi Anda dalam pool, relatif terhadap anonsetnya.

**Penting untuk dicatat bahwa skor prospektif koin Anda harus dihitung dari TXID mix awal Anda, dan bukan dari mix terbaru Anda. Sebaliknya, skor retrospektif dari UTXO dihitung dari TXID siklus terakhir.**

### Menggunakan Kalkulator Boltzmann
Kalkulator Boltzmann adalah alat untuk menganalisis transaksi Bitcoin, menawarkan kemampuan untuk mengukur tingkat entropinya di antara metrik canggih lainnya. Data ini memberikan penilaian kuantitatif tentang privasi transaksi dan membantu mengidentifikasi potensi kelemahan. Alat ini sudah terintegrasi ke dalam node RoninDojo Anda, membuatnya mudah diakses dan digunakan.

Sebelum menjelaskan prosedur penggunaan Kalkulator Boltzmann, penting untuk memahami makna indikator-indikator ini, metode perhitungannya, dan kegunaannya. Meskipun berlaku untuk transaksi Bitcoin apa pun, indikator-indikator ini khususnya berguna untuk menilai kualitas transaksi coinjoin.

**Indikator pertama** yang dihitung oleh perangkat lunak adalah jumlah total kombinasi yang mungkin, ditunjukkan di bawah `nb combinations` dalam alat tersebut. Berdasarkan nilai UTXO yang terlibat, indikator ini mengkuantifikasi jumlah cara di mana input dapat dikaitkan dengan output. Dengan kata lain, ini menentukan jumlah interpretasi yang masuk akal yang dapat dihasilkan oleh transaksi. Sebagai contoh, coinjoin yang terstruktur menurut model Whirlpool 5x5 menyajikan `1496` kombinasi yang mungkin:
![combinations](assets/notext/50.webp)
Kredit: KYCP

**Indikator kedua** yang dihitung adalah entropi dari transaksi, yang ditandai dengan `Entropy`. Ketika transaksi memiliki jumlah kombinasi yang mungkin tinggi, seringkali lebih relevan untuk merujuk pada entropinya. Ini didefinisikan sebagai logaritma biner dari jumlah kombinasi yang mungkin. Berikut adalah rumus yang digunakan:
- $E$: entropi transaksi;
- $C$: jumlah kombinasi yang mungkin untuk transaksi.
$$E = \log_2(C)$$
Dalam matematika, logaritma biner (logaritma basis 2) sesuai dengan operasi invers dari mengangkat 2 ke suatu pangkat. Dengan kata lain, logaritma biner dari $x$ adalah eksponen yang harus 2 dinaikkan untuk mendapatkan $x$. Oleh karena itu, indikator ini dinyatakan dalam bit. Mari kita ambil contoh perhitungan entropi untuk transaksi coinjoin yang terstruktur menurut model Whirlpool 5x5, yang, seperti disebutkan sebelumnya, menawarkan sejumlah kombinasi yang mungkin sebanyak `1496`:$$ C = 1496 $$
$$ E = \log_2(1496) $$
$$ E \approx 10.5469 \text{ bit}$$

Dengan demikian, transaksi coinjoin ini menampilkan entropi sebesar 10.5469 bit, yang dianggap sangat memuaskan. Semakin tinggi nilai ini, semakin banyak interpretasi berbeda yang diakui transaksi, sehingga meningkatkan tingkat privasinya.

Mari kita ambil contoh tambahan dengan transaksi yang lebih konvensional, yang memiliki satu input dan dua output: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://mempool.space/en/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce)
Dalam kasus transaksi ini, satu-satunya interpretasi yang mungkin adalah: `(inp 0) > (Outp 0 ; Outp 1)`. Akibatnya, entropinya ditetapkan pada `0`:
$$ C = 1 $$
$$ E = \log_2(1) $$
$$ E \approx 0 \text{ bit}$$
**Indikator ketiga** yang disediakan oleh Kalkulator Boltzmann dinamakan `Efisiensi Dompet`. Indikator ini menilai efisiensi transaksi dengan membandingkannya dengan transaksi optimal yang dapat dibayangkan dalam pengaturan yang identik. Ini membawa kita untuk membahas konsep entropi maksimum, yang sesuai dengan entropi tertinggi yang secara teoritis dapat dicapai oleh struktur transaksi tertentu. Dengan demikian, untuk struktur coinjoin Whirlpool 5x5, entropi maksimum ditetapkan pada `10.5469`. Efisiensi transaksi kemudian dihitung dengan menghadapkan entropi maksimum ini dengan entropi aktual dari transaksi yang dianalisis. Rumus yang digunakan adalah sebagai berikut:
- $ER$: entropi aktual dari transaksi, dinyatakan dalam bit;
- $EM$: entropi maksimum yang mungkin untuk struktur transaksi tertentu, juga dalam bit;
- $Ef$: efisiensi transaksi, dalam bit.
$$Ef = ER - EM$$ $$Ef = 10.5469 - 10.5469$$
$$Ef = 0 \text{ bit}$$

Indikator ini juga dinyatakan sebagai persentase, rumusnya kemudian adalah:
- $CR$: jumlah kombinasi aktual yang mungkin;
- $CM$: jumlah maksimum kombinasi yang mungkin dengan struktur yang sama;
- $Ef$: efisiensi yang dinyatakan sebagai persentase.
$$Ef = \frac{CR}{CM}$$
$$Ef = \frac{1496}{1496}$$
$$Ef = 100\%$$

Efisiensi sebesar `100%` ini menunjukkan bahwa transaksi memaksimalkan potensinya untuk privasi berdasarkan strukturnya.
**Indikator keempat**, kepadatan entropi, atau `Entropy Density`, menawarkan perspektif tentang entropi relatif terhadap setiap input atau output dari transaksi. Indikator ini berguna untuk mengevaluasi dan membandingkan efisiensi transaksi dari berbagai ukuran. Untuk menghitungnya, cukup bagi total entropi transaksi dengan jumlah total input dan output yang terlibat. Mengambil contoh dari Whirlpool 5x5 coinjoin:
- $ED$: kepadatan entropi yang diungkapkan dalam bit;
- $E$: entropi dari transaksi yang diungkapkan dalam bit;
- $T$: jumlah total input dan output dalam transaksi.
$$T = 5 + 5 = 10$$
$$ED = \frac{E}{T}$$
$$ED = \frac{10.5469}{10}$$
$$ED = 1.054 \text{ bit}$$
**Informasi kelima** yang disampaikan oleh Kalkulator Boltzmann adalah tabel probabilitas kecocokan antara input dan output. Tabel ini menunjukkan, melalui `skor Boltzmann`, probabilitas bahwa input tertentu terhubung dengan output tertentu. Mengambil contoh dari Whirlpool coinjoin, tabel probabilitas akan menyoroti peluang keterkaitan antara setiap input dan output, memberikan ukuran kuantitatif dari ambiguitas atau prediktabilitas asosiasi dalam transaksi:

| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
|---------|----------|----------|----------|----------|----------|
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |

Di sini, jelas bahwa setiap input memiliki peluang yang sama untuk dikaitkan dengan output mana pun, yang memperkuat ambiguitas dan kerahasiaan transaksi. Namun, dalam kasus transaksi sederhana dengan satu input dan dua output, situasinya berbeda:

| %       | Output 0 | Output 1 |
|---------|----------|----------|
| Input 0 | 100%     | 100%     |

Di sini, kita melihat bahwa probabilitas untuk setiap output berasal dari input 0 adalah 100%. Probabilitas yang lebih rendah dengan demikian menerjemahkan ke kerahasiaan yang lebih besar, dengan mengencerkan tautan langsung antara input dan output.

**Informasi keenam** yang disediakan adalah jumlah tautan deterministik, dilengkapi dengan rasio tautan ini. Indikator ini mengungkapkan berapa banyak koneksi antara input dan output dalam transaksi yang dianalisis adalah tidak dapat disangkal, dengan probabilitas 100%. Rasio, pada gilirannya, menawarkan perspektif tentang bobot tautan deterministik ini dalam total tautan transaksi.

Sebagai contoh, transaksi coinjoin tipe Whirlpool tidak menampilkan tautan deterministik, dan oleh karena itu menampilkan indikator dan rasio 0%. Di sisi lain, dalam transaksi kedua yang kami periksa (dengan satu input dan dua output), indikatornya ditetapkan pada 2 dan rasionya mencapai 100%. Dengan demikian, indikator nol menandakan kerahasiaan yang sangat baik berkat ketiadaan tautan langsung dan tidak dapat disangkal antara input dan output.
**Cara Mengakses Kalkulator Boltzmann di RoninDojo?**Untuk mengakses alat *Boltzmann Calculator*, buka RoninCLI. Untuk melakukan ini, buka terminal pada komputer pribadi Anda dan buat koneksi SSH dengan node Anda menggunakan perintah berikut: `SSH ronindojo@[IP]`

Jika, misalnya, alamat IP node Anda adalah `192.168.1.40`, perintah yang tepat adalah:
`SSH ronindojo@192.168.1.40`

Jika Anda mengubah nama pengguna Anda selama langkah 6, menggantikan nama pengguna default (`ronindojo`) dengan yang lain, pastikan untuk menggunakan nama baru ini dalam perintah. Misalnya, jika Anda memilih `planb` sebagai nama pengguna Anda dan alamat IP adalah `192.168.1.40`, perintah yang harus dimasukkan adalah:
`SSH planb@192.168.1.40`

Anda akan diminta untuk memasukkan kata sandi pengguna. Masukkan dan kemudian tekan `enter` untuk memvalidasi. Anda kemudian akan mengakses antarmuka RoninCLI. Gunakan panah pada keyboard Anda untuk menavigasi ke menu `Samourai Toolkit` dan tekan `enter` untuk memilihnya:

![Samourai Toolkit](assets/notext/43.webp)

Kemudian pilih `Boltzmann Calculator`:

![boltzmann](assets/notext/49.webp)

Anda akan tiba di halaman utama perangkat lunak:

![boltzmann home](assets/notext/51.webp)

Masukkan TXID dari transaksi yang ingin Anda pelajari dan tekan tombol `enter`:

![boltzmann txid](assets/notext/52.webp)

Kalkulator kemudian menyediakan Anda dengan semua indikator yang telah kami bahas sebelumnya:

![boltzmann result](assets/notext/53.webp)

### Fitur Lain dari RoninDojo v2 Anda
Node RoninDojo Anda mengintegrasikan berbagai fitur lain. Khususnya, Anda memiliki kemampuan untuk memindai informasi spesifik untuk memperhitungkannya. Misalnya, terkadang dompet Samourai Anda, yang terhubung ke RoninDojo, mungkin tidak menampilkan bitcoin yang sebenarnya Anda miliki. Jika saldo menunjukkan 0 sementara Anda yakin memiliki bitcoin di dompet ini, beberapa alasan dapat menjelaskan situasi ini, seperti kesalahan dalam jalur derivasi. Tapi salah satu penyebabnya juga bisa karena node Anda tidak memantau alamat Anda dengan benar. Untuk menyelesaikan masalah ini, Anda dapat memastikan bahwa node Anda memang mengikuti `xpub` Anda menggunakan _xpub tool_. Untuk mengakses alat ini melalui RoninUI, ikuti jalur:
`Maintenance > XPUB Tool`

Masukkan `xpub` yang menyebabkan masalah dan klik tombol `Check` untuk memverifikasi informasi ini:
![xpub tool](assets/notext/54.webp)
Pastikan semua transaksi terdaftar dengan benar. Juga penting untuk memverifikasi bahwa jenis derivasi yang digunakan cocok dengan dompet Anda. Jika ini bukan kasusnya, klik pada `Retype`, kemudian pilih dari `BIP44`, `BIP49`, atau `BIP84` sesuai dengan kebutuhan Anda.
Di luar alat ini, tab `Maintenance` dari RoninUI penuh dengan fitur berguna lainnya:
- *Transaction Tool*: Memungkinkan pemeriksaan detail dari transaksi tertentu;
- *Address Tool*: Memungkinkan konfirmasi pelacakan alamat tertentu oleh Dojo Anda;
- *Rescan Blocks*: Memaksa node Anda untuk melakukan pemindaian ulang rentang blok tertentu.

Tab `Push Tx` adalah fitur menarik lainnya dari RoninUI, yang memungkinkan penayangan transaksi yang telah ditandatangani di jaringan Bitcoin. Transaksi harus dimasukkan dalam bentuk heksadesimal.
Mengenai tab lain yang tersedia di dashboard RoninUI Anda:
- `Apps`: Menampung aplikasi Whirlpool, dan pasti akan digunakan untuk mengintegrasikan aplikasi baru di masa depan;
- `Logs`: Menawarkan akses real-time ke log event dari perangkat lunak Anda;
- `System Info`: Memberikan informasi umum tentang node Anda, seperti suhu CPU, penggunaan ruang penyimpanan, atau data RAM. Anda juga akan menemukan opsi `Reboot` dan `Shut down` untuk memulai ulang atau mematikan node Anda;
- `Settings`: Memungkinkan Anda untuk mengubah password pengguna Anda.

Itu dia! Terima kasih telah mengikuti tutorial ini sampai selesai. Jika Anda menikmatinya, saya mendorong Anda untuk membagikannya di media sosial. Selain itu, jika Anda memiliki kesempatan, pertimbangkan untuk mendukung para pengembang yang membuat perangkat lunak bebas dan sumber terbuka ini tersedia untuk komunitas kita dengan donasi: [https://donate.ronindojo.io/](https://donate.ronindojo.io/). Untuk memperdalam pengetahuan Anda tentang RoninDojo dan menemukan lebih banyak sumber daya, saya sangat merekomendasikan untuk mengkonsultasikan link ke sumber daya eksternal yang disebutkan di bawah ini.

**Sumber daya eksternal:**
- [https://ronindojo.io/index.html](https://ronindojo.io/index.html)
- [https://wiki.ronindojo.io/en/home](https://wiki.ronindojo.io/en/home)
- [https://gist.github.com/LaurentMT/e758767ca4038ac40aaf](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [https://medium.com/@laurentmt/memperkenalkan-boltzmann-85930984a159](https://medium.com/@laurentmt/memperkenalkan-boltzmann-85930984a159)
- [https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry](https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry)