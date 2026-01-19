---
name: RoninDojo v2
description: Memasang node Bitcoin RoninDojo v2 pada Raspberry Pi
---
![cover RoninDojo v2](assets/cover.webp)

**PERINGATAN:** *Menyusul penangkapan pendiri Samourai Wallet dan penyitaan server mereka pada 24 April, beberapa fitur RoninDojo seperti Whirlpool sudah nggak berfungsi lagi. Tapi ada kemungkinan alat-alat ini bisa dipulihkan atau dirilis ulang dengan cara berbeda dalam beberapa minggu ke depan. Selain itu, karena kode RoninDojo di-host di GitLab Samourai yang ikut disita, saat ini kamu nggak bisa mengunduh kode tersebut secara remote. Tim RoninDojo kemungkinan sedang menyiapkan rilis ulang kodenya.*

*Kami terus mengikuti perkembangan kasus ini dan semua update terkait alat-alat tersebut. Tenang aja, kami bakal memperbarui tutorial ini begitu ada info baru yang tersedia.*

*Tutorial ini hanya untuk tujuan edukasi dan informasi. Kami nggak mendukung atau mendorong penggunaan alat-alat ini untuk aktivitas kriminal. Setiap pengguna bertanggung jawab untuk mematuhi hukum di yurisdiksi masing-masing.*

---

> Gunakan Bitcoin dengan privasi.

Dalam [tutorial sebelumnya](https://planb.academy/tutorials/node/bitcoin/ronin-dojo-31d96647-029b-43e8-9fb5-95ec5dde72b0), kami sudah menjelaskan cara memasang dan memakai RoninDojo v1. Tapi selama setahun terakhir, tim RoninDojo udah merilis versi 2 dari implementasi mereka, yang jadi titik balik penting dalam arsitektur software mereka. Mereka pindah dari distro Linux Manjaro ke Debian. Akibatnya, mereka nggak lagi menyediakan image yang sudah dikonfigurasi untuk instalasi otomatis di Raspberry Pi. Tapi tenang, masih ada cara untuk instalasi manual. Ini juga metode yang aku pakai untuk node aku sendiri, dan sejak itu RoninDojo v2 jalan mulus banget di Raspberry Pi 4 aku. Jadi aku bikin tutorial baru tentang cara memasang RoninDojo v2 secara manual di Raspberry Pi.

## Daftar Isi:
- Apa itu RoninDojo?
- Perangkat keras apa yang harus dipilih untuk memasang RoninDojo v2?
- Bagaimana cara merakit Raspberry Pi 4?
- Bagaimana cara memasang RoninDojo v2 pada Raspberry Pi 4?
- Bagaimana cara menggunakan node RoninDojo v2 kamu?

## Apa itu RoninDojo?
Dojo awalnya adalah implementasi node Bitcoin penuh berbasis Bitcoin Core yang dikembangkan oleh tim Samourai Wallet. Solusi ini bisa dipasang di perangkat apa pun. Berbeda dengan implementasi Core lainnya, Dojo dioptimalkan khusus supaya bisa terintegrasi dengan ekosistem aplikasi Android milik Samourai Wallet. Sementara itu, RoninDojo adalah utilitas yang dibuat untuk mempermudah pemasangan dan pengelolaan Dojo, plus berbagai alat pendukung lainnya. Singkatnya, RoninDojo memperkaya implementasi dasar Dojo dengan menggabungkan banyak alat tambahan sambil tetap menyederhanakan proses pemasangan dan pengelolaannya.

Ronin juga menawarkan [solusi node-dalam-kotak, yang disebut "*Tanto*"](https://ronindojo.io/en/products), sebuah perangkat dengan RoninDojo yang sudah dipasang pada sistem yang dirakit oleh tim mereka. Tanto adalah opsi berbayar yang mungkin menarik buat kamu yang pengin menghindari keribetan teknis. Tapi karena kode sumber RoninDojo itu open-source, kamu juga bisa memasangnya di perangkat keras kamu sendiri. Alternatif yang lebih murah ini tetap butuh beberapa langkah tambahan, dan itu yang bakal kita bahas di tutorial ini.

RoninDojo adalah sebuah Dojo, jadi dia memungkinkan integrasi mudah Whirlpool CLI ke dalam node Bitcoin kamu untuk ngasih pengalaman coinjoin terbaik. Dengan Whirlpool CLI, kamu bisa terus remix bitcoin kamu 24 jam sehari, 7 hari seminggu, tanpa harus bikin komputer pribadi kamu tetap nyala.

Selain Whirlpool CLI, RoninDojo juga nyediain berbagai alat buat ningkatin fungsionalitas Dojo kamu. Misalnya, kalkulator Boltzmann buat menganalisis tingkat privasi transaksi kamu, server Electrum buat nyambungin dompet Bitcoin kamu ke node kamu, dan server Mempool buat lihat transaksi kamu secara lokal tanpa bocorin info apa pun.

Kalau dibandingkan dengan solusi node lain seperti Umbrel, RoninDojo jelas fokus ke solusi on-chain dan alat privasi. Nggak seperti Umbrel, RoninDojo nggak mendukung pengaturan node Lightning atau integrasi aplikasi server yang lebih umum. Walaupun RoninDojo lebih sedikit fitur serbaguna dibanding Umbrel, semua fungsionalitas penting buat ngatur aktivitas on-chain kamu itu sudah ada.

Kalau kamu nggak butuh fitur umum atau terkait Lightning Network seperti yang disediain Umbrel, dan kamu cuma pengin node yang simpel, stabil, dengan alat esensial kayak Whirlpool atau Mempool, RoninDojo bisa jadi pilihan ideal. Sementara Umbrel lebih cocok jadi server multitasking mini yang berorientasi Lightning Network dan serbaguna, RoninDojo, sesuai filosofi Samourai Wallet, fokus pada alat-alat fundamental buat privasi pengguna.

Sekarang setelah kami telah menguraikan RoninDojo, mari kita lihat bersama bagaimana cara mengatur node ini.

## Perangkat keras apa yang harus dipilih untuk menginstal RoninDojo v2?
RoninDojo menawarkan sebuah gambar untuk instalasi otomatis perangkat lunaknya pada [RockPro64](https://ronindojo.io/en/download). Namun, tutorial ini fokus ke prosedur instalasi manual di Raspberry Pi 4. Walaupun Raspberry Pi 5 baru dirilis dan secara teori tutorial ini harusnya kompatibel juga dengan model baru itu, aku belum sempat nyoba langsung, dan belum nemu feedback dari komunitas. Begitu aku punya Pi 5 dan komponen yang cocok, tutorial ini bakal aku update supaya kamu tetap dapat info terbaru. Untuk sekarang, aku sarankan tetap pakai Pi 4, karena dia bekerja sempurna untuk node aku.

Dari sisi aku sendiri, aku jalanin RoninDojo di Raspberry Pi dengan 8 GB RAM. Walaupun beberapa anggota komunitas berhasil menjalankannya di perangkat dengan 4 GB RAM, aku belum uji konfigurasi itu sendiri. Mengingat selisih harganya kecil, lebih bijak pilih versi 8 GB RAM. Ini juga berguna kalau di masa depan kamu mau pakai ulang Raspberry Pi kamu buat kebutuhan lain.

Penting dicatat kalau tim RoninDojo sudah melaporkan banyak masalah yang sering muncul terkait casing dan adaptor SSD. Aku sendiri juga pernah ngalamin masalah itu. **Jadi sangat disarankan buat menghindari casing yang pakai kabel USB untuk SSD node kamu.** Sebagai gantinya, pilih kartu ekspansi penyimpanan yang memang dirancang khusus untuk Raspberry Pi kamu:

![kartu ekspansi penyimpanan RPI4](assets/notext/1.webp)
Untuk menyimpan blockchain Bitcoin, kamu akan butuh SSD yang kompatibel dengan kartu ekspansi penyimpanan yang sudah kamu pilih. Saat ini (Februari 2024), kita lagi ada di fase transisi. Diperkirakan dalam beberapa bulan ke depan, SSD 1 TB nggak akan cukup lagi buat menampung ukuran blockchain yang terus tumbuh, apalagi kalau kamu berencana mengintegrasikan berbagai aplikasi ke dalam node kamu. Karena itu, beberapa orang merekomendasikan investasi di SSD 2 TB demi ketenangan jangka panjang. Tapi, dengan tren harga SSD yang terus turun setiap tahun, ada juga yang menyarankan cukup pakai SSD 1 TB, yang harusnya masih aman untuk satu atau dua tahun. Mereka berargumen kalau saat kapasitas itu mulai nggak cukup, harga SSD 2 TB kemungkinan sudah jauh lebih murah. Pilihan ini sepenuhnya tergantung preferensi kamu. Kalau kamu berencana mempertahankan RoninDojo kamu dalam jangka waktu lama dan pengin menghindari repot-repot upgrade beberapa tahun ke depan, SSD 2 TB terlihat sebagai opsi paling bijak, karena ngasih kamu ruang yang lebih lega untuk masa depan.

Selain itu, kamu akan memerlukan berbagai komponen kecil:

- Sebuah casing dengan kipas untuk menampung Raspberry Pi kamu dan kartu ekspansi penyimpanannya. Ada juga kit yang sudah mencakup kartu ekspansi SSD sekaligus casing yang kompatibel, dan itu bisa kamu temukan dengan mudah online.
- Sebuah kabel daya untuk Raspberry Pi kamu.
- Sebuah kartu micro SD minimal 16 GB (walaupun 8 GB sebenarnya cukup, selisih harga antara 8 dan 16 GB biasanya nggak signifikan).
- Sebuah kabel Ethernet RJ45 untuk koneksi jaringan.

![node material](assets/notext/2.webp)

## Bagaimana cara merakit Raspberry Pi 4?
Perakitan node kamu bakal sedikit berbeda tergantung perangkat keras yang kamu pilih, terutama jenis casing. Tapi secara umum, langkah-langkah dasarnya tetap mirip untuk semua jenis perakitan.
Mulailah dengan memasang SSD kamu ke kartu ekspansi penyimpanan, lalu pastikan dua sekrup penguncinya di bagian belakang terpasang dengan aman.

![assembly1](assets/notext/3.webp)

Kemudian pasang Raspberry Pi kamu ke kartu ekspansi.

![assembly2](assets/notext/4.webp)

Juga, pasang kipas ke Raspberry Pi.

![assembly3](assets/notext/5.webp)

Sambungkan semua komponen, pastikan kamu pakai pin yang benar dengan merujuk ke manual casing kamu. Biasanya produsen casing juga menyediakan tutorial video untuk bantu proses perakitan. Di kasus aku, aku pakai kartu ekspansi tambahan yang punya tombol on/off. Ini bukan hal yang wajib untuk bikin node Bitcoin, aku cuma pakai karena pengin ada tombol daya aja.

Kalau kamu juga pakai kartu ekspansi yang punya tombol on/off, jangan lupa pasang jumper kecil "Auto Power On". Ini bakal bikin node kamu otomatis nyala lagi begitu dapat aliran listrik. Fitur ini berguna banget kalau sewaktu-waktu terjadi pemadaman, karena node kamu bisa restart sendiri tanpa perlu kamu sentuh sama sekali.

![assembly4](assets/notext/6.webp)

Sebelum kamu memasukkan semua perangkat keras ke dalam casing, penting buat ngecek dulu apakah Raspberry Pi kamu, kartu ekspansi penyimpanan, dan kipasnya berfungsi dengan benar dengan cara menyalakannya sebentar.

![assembly5](assets/notext/7.webp)
Akhirnya, pasang Raspberry Pi kamu ke dalam casingnya. Ingat, langkah berikutnya bakal butuh kamu memasukkan kartu micro SD ke port yang sesuai di Raspberry Pi. Kalau casing kamu punya bukaan khusus yang memungkinkan kamu masukin kartu SD tanpa harus buka casing lagi (kayak casing yang aku pakai di foto), kamu bisa langsung nutup casing sekarang. Tapi kalau casing kamu nggak punya akses langsung ke port micro SD, kamu perlu menunggu sampai kartu micro SD sudah selesai kamu siapkan sebelum menutup casing sepenuhnya.

## Bagaimana cara menginstal RoninDojo v2 di Raspberry Pi 4?

### Langkah 1: Persiapkan kartu micro SD yang dapat boot
Setelah perangkat keras kamu selesai dirakit, langkah berikutnya adalah menginstal RoninDojo. Untuk itu, kita perlu menyiapkan kartu micro SD yang bisa boot dari komputer kamu, dengan cara membakar image disk yang sesuai ke dalam kartu tersebut.
Kamu perlu menggunakan perangkat lunak _**Raspberry Pi Imager**_, yang dirancang untuk memudahkan pengunduhan, konfigurasi, dan penulisan sistem operasi pada kartu micro SD untuk digunakan dengan Raspberry Pi. Mulailah dengan menginstal perangkat lunak ini di PC pribadi kamu:

- Untuk Ubuntu/Debian: https://downloads.raspberrypi.org/imager/imager_latest_amd64.deb
- Untuk Windows: https://downloads.raspberrypi.org/imager/imager_latest.exe
- Untuk Mac: https://downloads.raspberrypi.org/imager/imager_latest.dmg

Setelah perangkat lunak terinstal, bukalah, dan masukkan kartu micro SD ke dalam komputer pribadi kamu. Dari antarmuka Raspberry Pi Imager, pilih `CHOOSE OS`:

Selanjutnya, pergi ke menu `Raspberry Pi OS (other)`:

Pilih sistem operasi yang bernama `Raspberry Pi OS (Legacy, 64-bit) Lite`, yang berukuran `0.3 GB`:

Setelah memilih sistem operasi, kamu akan diarahkan kembali ke menu utama Raspberry Pi Imager. Klik pada `CHOOSE STORAGE`:

Pilih kartu micro SD kamu:

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

Sebuah pesan akan memberitahu kamu bahwa semua data pada kartu micro SD akan dihapus. Konfirmasi dengan mengklik `YES` untuk memulai proses:

![overwrite micro SD](assets/notext/21.webp)

Tunggu sampai perangkat lunak selesai menyiapkan kartu micro SD kamu:

![writing micro SD](assets/notext/22.webp)

Ketika pesan yang menunjukkan akhir proses muncul, kamu dapat melepas kartu micro SD dari komputer milikmu:

![writing micro SD completed](assets/notext/23.webp)

### Langkah 2: Lengkapi Perakitan Node
Sekarang kamu dapat memasukkan kartu micro SD ke dalam port yang sesuai pada Raspberry Pi Anda.

![micro SD](assets/notext/24.webp)

Kemudian, hubungkan Raspberry Pi ke router menggunakan kabel Ethernet. Akhirnya, nyalakan node dengan menghubungkan kabel daya dan menekan tombol daya (jika setup kamu menyertakannya).

### Langkah 3: Membangun Koneksi SSH dengan Node
Pertama, perlu untuk menemukan alamat IP dari node kamu. Kamu memiliki opsi untuk menggunakan alat seperti _[Advanced IP Scanner](https://www.advanced-ip-scanner.com/)_ atau _[Angry IP Scanner](https://angryip.org/)_, atau memeriksa antarmuka administrasi router Anda. Alamat IP harus dalam bentuk `192.168.1.??`. **Untuk semua perintah berikut, ganti `[IP]` dengan alamat IP sebenarnya dari node Anda**, (menghilangkan tanda kurung).

Luncurkan terminal.

Untuk menghapus kunci yang mungkin sudah terasosiasi dengan alamat IP dari node kamu, jalankan perintah: 
`ssh-keygen -R [IP]`. 

Kesalahan setelah perintah ini tidak serius; itu hanya berarti bahwa kunci tidak ada dalam daftar host yang dikenal kamu (yang cukup mungkin). Misalnya, jika IP dari node Anda adalah `192.168.1.40`, perintahnya menjadi: `ssh-keygen -R 192.168.1.40`.

Selanjutnya, bangun koneksi SSH dengan node Anda dengan menjalankan perintah: 
`ssh pi@[IP]`.

Sebuah pesan akan muncul mengenai keaslian host: `The authenticity of host '[IP]' can't be established.` Ini menunjukkan kalau keaslian perangkat yang kamu coba hubungkan belum bisa diverifikasi karena belum ada kunci publik yang dikenal. Saat pertama kali terhubung lewat SSH ke host baru, pesan seperti ini memang selalu muncul. Kamu cukup jawab `yes` untuk menambahkan kunci publiknya ke direktori lokal kamu, supaya peringatan ini nggak muncul lagi di koneksi SSH berikutnya ke node yang sama. Jadi, ketik `yes` dan tekan `enter` untuk lanjut.

Kamu kemudian akan diminta memasukkan password kamu, yang sebelumnya sudah kamu set sebagai password sementara di langkah 1. Tekan `enter` untuk validasi. Setelah itu, kamu bakal langsung terhubung ke node kamu via SSH.

Ringkasnya, berikut adalah perintah untuk dijalankan:
- `ssh-keygen -R [IP]`
- `ssh pi@[IP]`
- `yes`
- Masukkan kata sandi sementara dan validasi.

### Langkah 4: Pembaruan dan Persiapan
Sekarang kamu terhubung ke node kamu via sesi SSH. Di terminal Anda, prompt perintah harusnya: `pi@RoninDojo:~ $`. Untuk memulai, perbarui daftar paket yang tersedia dan instal pembaruan untuk paket yang sudah ada dengan perintah berikut:
`sudo apt update && sudo apt upgrade -y`
Setelah pembaruan selesai, lanjutkan untuk menginstal *Git* dan *Dialog* menggunakan perintah: `sudo apt install git dialog -y`

Selanjutnya, kloning cabang `master` dari repositori Git _RoninOS_ dengan menjalankan:
`sudo git clone --branch master https://code.samourai.io/ronindojo/RoninOS.git /opt/RoninOS`

Jalankan skrip `customize-image.sh` dengan perintah:
`cd /opt/RoninOS/ && sudo ./customize-image.sh`

**Penting untuk membiarkan skrip berjalan tanpa gangguan dan menunggu dengan sabar hingga prosesnya selesai**, yang memakan waktu sekitar 10 menit. Ketika pesan `Setup is complete` muncul, kamu dapat melanjutkan ke langkah selanjutnya.

### Langkah 5: Menjalankan RoninOS
Jalankan RoninOS dengan perintah:
`sudo systemctl start ronin-setup`

Tampilkan baris-baris file log dengan perintah:
`tail -f /home/ronindojo/.logs/setup.logs`

Pada tahap ini, **penting untuk membiarkan RoninOS berjalan dan menunggu hingga selesai**. Ini memakan waktu sekitar 40 menit. Ketika `All RoninDojo feature installations complete!` muncul, kamu bisa melanjutkan ke langkah 6.

### Langkah 6: Mengakses RoninUI dan Mengubah Kredensial
Setelah instalasi selesai, untuk terhubung ke node kamu lewat browser, pastikan komputer kamu ada di jaringan lokal yang sama dengan node kamu. Kalau kamu lagi pakai VPN di komputer, matikan dulu sementara.

Untuk membuka antarmuka node di browser kamu, masukkan alamat berikut di bilah URL:

- Langsung alamat IP node Anda, misalnya, `192.168.1.??`;
- Atau, ketik `ronindojo.local`.

Setelah berada di halaman utama RoninUI, kamu akan diminta untuk memulai pengaturan. Untuk melakukan ini, klik tombol `Let's start`.

![lets start](assets/notext/25.webp)

Pada tahap ini, RoninUI menampilkan kata sandi `root` kamu. Sangat penting untuk menjaganya dengan aman. Kamu dapat memilih untuk membuat cadangan fisik, di atas kertas, atau menyimpannya dalam [pengelola kata sandi](https://planb.academy/courses/99c46148-7080-4915-a7e0-9df0e145cd47/0b3c69b2-522c-56c8-9fb8-1562bd55930f).

![root password](assets/notext/26.webp)

Setelah menyimpan kata sandi `root`, centang kotak `I have backed up Root user credentials` dan klik `Continue` untuk melanjutkan.

![confirm root password](assets/notext/27.webp)

Langkah berikutnya adalah membuat password pengguna, yang bakal kamu pakai baik untuk akses antarmuka web RoninUI maupun untuk sesi SSH ke node kamu. Pilih password yang kuat dan simpan dengan aman. Kamu perlu memasukkan password ini dua kali sebelum klik `Finish` untuk validasi. Untuk username, disarankan tetap pakai pilihan default, `ronindojo`. Kalau kamu memilih menggantinya, pastikan kamu menyesuaikan perintah di langkah-langkah berikutnya sesuai perubahan tersebut.

![user credentials](assets/notext/28.webp)

Setelah langkah ini selesai, tunggu node kamu selesai inisialisasi. Setelah itu kamu bakal masuk ke antarmuka web RoninUI. Kamu hampir sampai di akhir proses, tinggal beberapa langkah kecil lagi!

![Ronin UI](assets/notext/29.webp)

### Langkah 7: Menghapus Kredensial Sementara
Buka terminal baru di komputer pribadi kamu dan buat koneksi SSH dengan node kamu menggunakan perintah berikut:
`SSH ronindojo@[IP]`
Jika, misalnya, alamat IP dari node kamu adalah `192.168.1.40`, perintah yang tepat akan menjadi: `SSH ronindojo@192.168.1.40`

Jika kamu mengganti nama pengguna kamu pada langkah sebelumnya, menggantikan nama pengguna default (`ronindojo`) dengan yang lain, pastikan untuk menggunakan nama baru ini dalam perintah. Sebagai contoh, jika kamu memilih `planb` sebagai nama pengguna dan alamat IP adalah `192.168.1.40`, perintah yang harus dimasukkan adalah:
`SSH planb@192.168.1.40`
Kamu akan diminta untuk memasukkan kata sandi pengguna. Masukkan dan kemudian tekan `enter` untuk memvalidasi. Kemudian kamu akan mengakses antarmuka RoninCLI. Gunakan tombol panah pada keyboard kamu untuk menavigasi ke opsi `Exit RoninDojo` dan tekan `enter` untuk memilihnya.
![RoninCLI](assets/notext/30.webp)

Pada titik ini, kamu sudah berada di terminal node kamu, dengan prompt perintah seperti:
`ronindojo@RoninDojo:~ $`

Untuk menghapus user sementara yang dibuat saat menyiapkan kartu micro SD yang bisa boot, masukkan perintah berikut lalu tekan `enter`:
`sudo deluser --remove-home pi`

Kamu akan diminta memasukkan password user kamu. Masukkan, lalu tekan `enter`. Tunggu sampai proses selesai, lalu gunakan perintah exit untuk keluar dari terminal.

Selamat! Node RoninDojo v2 kamu sekarang sudah dikonfigurasi dan siap dipakai. Node kamu akan mulai melakukan IBD (*Initial Block Download*), yaitu proses mengunduh dan memverifikasi blockchain Bitcoin mulai dari blok Genesis. Langkah ini mengambil semua transaksi Bitcoin sejak 3 Januari 2009 dan butuh waktu. Setelah blockchain selesai diunduh, indexer akan lanjut mengompresi database. Durasi IBD bisa sangat bervariasi. Node RoninDojo kamu akan sepenuhnya operasional setelah proses ini selesai.

**Kalau kamu migrasi dari node RoninDojo v1 lama** ke versi baru ini sambil mempertahankan SSD yang sama, node kamu harusnya otomatis mendeteksi dan memakai ulang data yang sudah ada di disk, sehingga kamu nggak perlu melakukan IBD ulang. Kamu cuma perlu menunggu sampai node selesai resinkronisasi dengan blok terbaru.

### Langkah 8: "veth fix"

Kalau kamu nemuin bug di RoninDojo v2 di Raspberry Pi, di mana setelah instalasi berjalan lancar tiba-tiba node kamu nggak bisa diakses lewat SSH tapi kembali normal setelah direstart, berarti kamu perlu lakukan langkah 8 ini. Bug umum ini bisa diperbaiki dengan solusi dari komunitas yang disebut *"veth fix".* Perbaikan kecil ini mencegah putus koneksi mendadak. Berikut cara menerapkannya.

Buka terminal baru di komputer kamu dan lakukan koneksi SSH ke node dengan perintah:
`SSH ronindojo@[IP]`

Kalau misalnya IP node kamu adalah 192.168.1.40, maka perintahnya:
`SSH ronindojo@192.168.1.40`

Kamu akan diminta memasukkan password user. Masukkan dan tekan `enter`. Setelah itu kamu bakal masuk ke antarmuka RoninCLI. Gunakan tombol panah untuk navigasi ke opsi Exit RoninDojo lalu tekan `enter`.

Sekarang kamu sudah kembali ke terminal node dengan prompt perintah seperti:
`ronindojo@RoninDojo:~ $`

Untuk menerapkan perbaikan **veth,** jalankan:
`sudo nano /etc/dhcpcd.conf`

Masukkan password lagi, lalu tekan `enter`.

Kamu akan masuk ke file dhcpcd.conf. Salin teks berikut (pastikan asterisk ikut):
`denyinterfaces veth*`

Pindah ke bagian paling bawah file dengan panah bawah, lalu tempel teks tersebut di baris baru.

Setelah selesai, tekan `ctrl X` untuk keluar, `ctrl Y` untuk konfirmasi penyimpanan, lalu tekan `enter` untuk kembali ke prompt. Untuk memastikan perubahan tersimpan, buka lagi file `dhcpcd.conf` dengan perintah yang sama dan cek apakah baris tadi sudah ada.

Untuk menyelesaikan perbaikan, restart node dengan perintah:
`sudo reboot now`

Sekarang kamu bisa menutup terminal. Beri waktu untuk RoninDojo restart, lalu kamu harusnya bisa terhubung lagi lewat antarmuka grafis di browser kamu. Perbaikan ini seharusnya mengatasi bug yang kamu temui.

## Bagaimana cara menggunakan node RoninDojo v2 kamu?

### Menghubungkan perangkat lunak dompet kamu ke Electrs
Penggunaan pertama dari node yang baru saja Anda instal dan sinkronkan adalah untuk menyiarkan transaksi Anda ke jaringan Bitcoin. Anda mungkin ingin menghubungkan berbagai dompet Anda ke node tersebut agar dapat menyiarkan transaksi secara privat. Untuk itu, Anda dapat memanfaatkan Electrum Rust Server (electrs). Aplikasi ini biasanya sudah terpasang di node RoninDojo Anda. Jika belum, Anda dapat menginstalnya secara manual melalui antarmuka RoninCLI di menu `Applications` > `Manage Applications` > `Install Electrum Server`.

Untuk mendapatkan alamat Tor dari Electrum Server kamu, dari antarmuka web RoninUI, pergi ke:
`Pairing > Electrum server > Pair now`
![Pairing](assets/notext/31.webp)
![Electrs](assets/notext/32.webp)
Kamu kemudian perlu memasukkan alamat `Hostname` yang berakhir dengan `.onion` di perangkat lunak dompet kamu, disertai dengan port `50001`. ![hostname](assets/notext/33.webp)
Sebagai contoh, di Sparrow Wallet, cukup pergi ke tab:
`File > Preferences > Server > Private Electrum`

![Sparrow](assets/notext/34.webp)

### Menghubungkan perangkat lunak dompet Anda ke Samourai Dojo
Sebagai alternatif untuk menggunakan Electrs, Dojo memungkinkan kamu untuk menghubungkan perangkat lunak dompet yang kompatibel langsung ke node RoninDojo kamu. Dompet seperti Samourai Wallet dan Sentinel menawarkan fungsionalitas ini.

Untuk membangun koneksi, Anda hanya perlu memindai kode QR dari Dojo kamu. Untuk mengakses kode QR ini melalui RoninUI, navigasikan ke:
`Pairing > Samourai Dojo > Pair now`
![Samourai Dojo](assets/notext/35.webp)
Untuk menghubungkan Samourai Wallet kamu ke Dojo, cukup pindai kode QR ini selama instalasi aplikasi:

![Samourai Wallet connection](assets/notext/36.webp)
Kalau kamu sudah punya Samourai Wallet sebelum menyiapkan Ronin Dojo, kamu perlu membackup dompetmu, menghapus instalasi, lalu menginstal ulang aplikasi Samourai Wallet sebelum mengembalikan dompetmu. Saat kamu meluncurkan aplikasi yang sudah diinstal ulang, kamu akan mendapat opsi untuk terhubung ke Dojo baru. **Hati-hati, proses ini membawa risiko kehilangan bitcoin kamu jika tidak dilakukan dengan benar!** Pastikan kamu punya backup Samourai wallet dalam file kamu dan verifikasi validitas passphrase melalui `Settings > Troubleshoot > Passphrase.` Juga penting untuk punya backup yang dapat dibaca dari frase pemulihan dan passphrase kamu. Untuk ketelitian lebih lanjut dalam operasi ini, disarankan mengikuti tutorial terperinci ini:

[https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai](https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai).

### Menggunakan block explorer Mempool.space milik Anda sendiri
Sebuah block explorer mengubah informasi mentah dari blockchain Bitcoin menjadi format yang terstruktur dan mudah dibaca. Dengan alat seperti *Mempool.space*, dimungkinkan untuk menganalisis transaksi, mencari alamat tertentu, atau bahkan konsultasi tarif rata-rata jaringan mempool secara real-time.

Namun, menggunakan block explorer online membawa risiko terhadap privasi Anda dan mengharuskan Anda mempercayai data yang disajikan oleh pihak ketiga. Saat menggunakan layanan seperti ini tanpa melalui node Anda sendiri, Anda bisa tanpa sengaja mengungkapkan informasi tentang transaksi Anda, dan Anda juga harus bergantung pada akurasi informasi yang diberikan oleh pemilik situs.

Untuk meminimalkan risiko ini, disarankan menggunakan instance Mempool.space Anda sendiri melalui jaringan Tor, yang di-hosting langsung pada node Anda. Pendekatan ini memastikan privasi tetap terjaga dan memberi Anda kendali penuh atas data Anda.

Untuk melakukan ini, mulailah dengan menginstal *Mempool Space Visualizer* dari RoninUI. Di antarmuka web, pergi ke tab `Dashboard` dan klik pada `Manage` di bawah `Mempool Space`:

`Dashboard > Mempool Space > Manage`
![Manage mempool](assets/notext/37.webp)
Kemudian klik pada tombol `Install Mempool visualizer`:
![install mempool](assets/notext/38.webp)
Konfirmasi password kamu:
![password mempool](assets/notext/39.webp)
Tunggu hingga instalasi selesai, kemudian klik lagi pada tombol `Manage`:
![Mempool Manage](assets/notext/40.webp)
Kamu akan mendapatkan link `.onion` untuk mengakses instance *Mempool.space* kamu sendiri melalui jaringan Tor.
![Mempool link](assets/notext/41.webp)
Saya menyarankan Anda untuk menyimpan tautan ini ke dalam bookmark di browser Tor Anda, atau menambahkannya ke aplikasi Tor Browser di smartphone Anda, agar Anda dapat mengaksesnya dengan mudah dan aman dari mana saja.

Jika Anda belum memiliki Tor Browser, Anda dapat mengunduhnya di sini: [https://www.torproject.org/download/](https://www.torproject.org/download/)
![Mempool Tor](assets/notext/42.webp)

### Menggunakan Whirlpool untuk mencampur bitcoin Anda
Node RoninDojo kamu juga mengintegrasikan _WhirlpoolCLI,_ antarmuka baris perintah yang memungkinkan otomatisasi coinjoin Whirlpool, serta _WhirlpoolGUI,_ antarmuka grafis yang digunakan untuk berinteraksi dengan _WhirlpoolCLI._
Melakukan coinjoin lewat Whirlpool membutuhkan aplikasi yang tetap aktif agar proses remix bisa berjalan terus-menerus. Ini bisa menjadi batasan bagi siapa pun yang ingin mencapai tingkat anonimitas tinggi. Perangkat yang menjalankan aplikasi Whirlpool harus tetap menyala tanpa henti. Artinya, jika kamu ingin tetap berpartisipasi dalam remix 24 jam sehari, komputer atau smartphone kamu harus terus menyala dengan Samourai atau Sparrow terbuka sepanjang waktu.

Solusi untuk batasan ini adalah menjalankan _WhirlpoolCLI_ di mesin yang selalu aktif, seperti node Bitcoin kamu. Dengan begitu, koin kamu bisa melakukan remix tanpa terputus, tanpa perlu menjaga perangkat lain tetap menyala.
Aku sedang menyiapkan tutorial lengkap yang akan memandu kamu langkah demi langkah dalam proses coinjoin menggunakan Samourai Wallet dan RoninDojo v2, dari awal sampai akhir.

Untuk memahami coinjoin lebih dalam—baik konsep, logika privasi, maupun cara kerjanya dalam ekosistem Bitcoin—kamu juga bisa membaca artikelku lainnya: Memahami dan menggunakan coinjoin pada Bitcoin, di mana aku menjelaskan semua hal yang perlu kamu tahu tentang teknik ini.

### Menggunakan Whirlpool Stat Tool (WST)

Setelah kamu melakukan coinjoin dengan Whirlpool, penting untuk mengevaluasi secara akurat tingkat privasi yang dicapai oleh UTXO hasil mix kamu. Untuk tujuan ini, kamu bisa menggunakan alat Python Whirlpool Stat Tool. Alat ini memungkinkan kamu mengukur baik skor prospektif maupun retrospektif dari UTXO kamu, sekaligus menganalisis tingkat difusi mereka di dalam pool.

Untuk memperdalam pemahaman kamu tentang mekanisme perhitungan anonset ini, kamu merekomendasikan membaca artikel: [REMIX - WHIRLPOOL](https://planb.academy/tutorials/privacy/on-chain/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa), yang menjelaskan fungsi dari indeks-indeks ini.

Untuk mengakses alat WST, buka RoninCLI. Untuk melakukan ini, buka terminal pada komputer pribadi kamu dan buat koneksi SSH dengan node kamu menggunakan perintah berikut:
`SSH ronindojo@[IP]`

Jika, misalnya, alamat IP node Anda adalah `192.168.1.40`, perintah yang tepat adalah:
`SSH ronindojo@192.168.1.40`

Jika kamu mengubah nama pengguna saat langkah 6 dengan menggantikan nama default (ronindojo) dengan nama lain, pastikan kamu memakai nama baru itu di dalam perintah. Misalnya, jika kamu memilih `planb` sebagai nama pengguna dan alamat IP-nya adalah `192.168.1.40`, maka perintah yang harus kamu masukkan adalah:
`SSH planb@192.168.1.40`

Kamu akan diminta untuk memasukkan kata sandi pengguna. Masukkan lalu tekan enter untuk memvalidasi. Kamu kemudian akan masuk ke antarmuka RoninCLI. Gunakan tombol panah pada keyboard untuk menavigasi ke menu Samourai Toolkit dan tekan `enter` untuk memilihnya.

![Samourai Toolkit](assets/notext/43.webp)

Kemudian pilih `Whirlpool Stat Tool`:

![WST](assets/notext/44.webp)

Setelah menginisialisasi WST, alat akan melanjutkan dengan instalasi otomatisnya. Tunggu selama langkah ini. Instruksi penggunaan akan bergulir. Setelah instalasi selesai, tekan tombol apa saja untuk mengakses terminal WST:

![Perintah WST](assets/notext/45.webp)

Prompt perintah berikut akan ditampilkan:
`wst#/tmp>`

Jika kamu ingin keluar dari antarmuka ini dan kembali ke menu RoninCLI, cukup masukkan:
`quit`

Pertama, perlu mengkonfigurasi proxy untuk menggunakan Tor, untuk memastikan kerahasiaan saat mengekstrak data dari OXT. Masukkan perintah:
`socks5 127.0.0.1:9050`
Selanjutnya, lanjutkan untuk mengunduh informasi pool yang berisi transaksi kamu:
`download 0001`
Ganti `0001` dengan kode denominasi pool yang Anda minati. Kode denominasi tersebut adalah sebagai berikut di WST:
- Pool 0.5 bitcoin: `05`
- Pool 0.05 bitcoin: `005`
- Pool 0.01 bitcoin: `001`
- Pool 0.001 bitcoin: `0001`

Setelah mengunduh, muat data dengan mengganti `0001` dengan kode pool kamu dalam perintah ini: `load 0001`

![WST loading](assets/notext/46.webp)

Tunggu sampai proses pemuatan selesai, yang bisa memakan waktu beberapa menit. Setelah datanya siap, untuk mengetahui skor anonset koin kamu, jalankan perintah `score` diikuti oleh TXID kamu (tanpa tanda kurung).
`score [TXID]`

![WST score](assets/notext/47.webp)

WST kemudian akan menampilkan skor retrospektif (_Backward-looking metrics_), diikuti oleh skor prospektif (_Forward-looking metrics_). Selain skor anonset, WST juga akan menunjukkan tingkat difusi transaksimu dalam pool, relatif terhadap anonsetnya.

**Penting untuk dicatat bahwa skor prospektif koin harus dihitung dari TXID mix awal, dan bukan dari mix terbaru. Sebaliknya, skor retrospektif dari UTXO dihitung dari TXID siklus terakhir.**

### Menggunakan Kalkulator Boltzmann
Kalkulator Boltzmann adalah alat untuk menganalisis transaksi Bitcoin, yang memungkinkan kamu mengukur tingkat entropinya dan berbagai metrik canggih lainnya. Data ini memberikan penilaian kuantitatif tentang privasi sebuah transaksi dan membantu mengidentifikasi potensi kelemahannya. Alat ini sudah terintegrasi ke dalam node RoninDojo kamu, sehingga mudah diakses dan digunakan.

Sebelum aku menjelaskan cara menggunakan Kalkulator Boltzmann, penting untuk memahami dulu makna indikator-indikator ini, bagaimana perhitungannya, dan apa kegunaannya. Walaupun indikator-indikator ini bisa diterapkan pada transaksi Bitcoin apa pun, mereka sangat berguna untuk menilai kualitas transaksi coinjoin.

**Indikator pertama** yang dihitung oleh perangkat lunak adalah jumlah total kombinasi yang mungkin, ditunjukkan di bawah `nb combinations` dalam alat tersebut. Berdasarkan nilai UTXO yang terlibat, indikator ini mengkuantifikasi jumlah cara input dapat dikaitkan dengan output. Dengan kata lain, indikator ini menentukan berapa banyak interpretasi yang masuk akal yang bisa dihasilkan dari sebuah transaksi.Sebagai contoh, coinjoin yang terstruktur menurut model Whirlpool 5x5 menyajikan `1496` kombinasi yang mungkin:
![combinations](assets/notext/50.webp)
Kredit: KYCP

**Indikator kedua** yang dihitung adalah entropi dari transaksi, yang ditandai dengan `Entropy`. Ketika transaksi memiliki jumlah kombinasi yang mungkin tinggi, seringkali lebih relevan untuk merujuk pada entropinya. Ini didefinisikan sebagai logaritma biner dari jumlah kombinasi yang mungkin. Berikut adalah rumus yang digunakan:
- $E$: entropi transaksi;
- $C$: jumlah kombinasi yang mungkin untuk transaksi.
$$E = \log_2(C)$$
Dalam matematika, logaritma biner (logaritma basis 2) sesuai dengan operasi invers dari mengangkat 2 ke suatu pangkat. Dengan kata lain, logaritma biner dari $x$ adalah eksponen yang harus 2 dinaikkan untuk mendapatkan $x$. Oleh karena itu, indikator ini dinyatakan dalam bit. Mari kita ambil contoh perhitungan entropi untuk transaksi coinjoin yang terstruktur menurut model Whirlpool 5x5, yang, seperti disebutkan sebelumnya, menawarkan sejumlah kombinasi yang mungkin sebanyak `1496`:$$ C = 1496 $$
$$ E = \log_2(1496) $$
$$ E \approx 10.5469 \text{ bit}$$

Dengan demikian, transaksi coinjoin ini menampilkan entropi sebesar 10.5469 bit, yang dianggap sangat memuaskan. Semakin tinggi nilai ini, semakin banyak interpretasi berbeda yang diakui oleh transaksi, sehingga meningkatkan tingkat privasinya.

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

Sebagai contoh, transaksi coinjoin tipe Whirlpool tidak menampilkan tautan deterministik, sehingga indikator dan rasionya bernilai 0%. Di sisi lain, pada transaksi kedua yang kita periksa (dengan satu input dan dua output), indikatornya bernilai 2 dan rasionya mencapai 100%. Dengan demikian, indikator nol menunjukkan kerahasiaan yang sangat baik berkat tidak adanya tautan langsung dan tidak dapat disangkal antara input dan output.

**Cara Mengakses Kalkulator Boltzmann di RoninDojo?**
Untuk mengakses alat Boltzmann Calculator, buka RoninCLI. Untuk melakukannya, buka terminal di komputer kamu dan lakukan koneksi SSH ke node kamu menggunakan perintah berikut: `SSH ronindojo@[IP]`

Jika, misalnya, alamat IP node Anda adalah `192.168.1.40`, perintah yang tepat adalah:
`SSH ronindojo@192.168.1.40`

Kalau kamu mengubah nama pengguna selama langkah 6, menggantikan nama pengguna default (`ronindojo`) dengan yang lain, pastikan untuk menggunakan nama baru ini dalam perintah. Misalnya, jika kamu memilih `planb` sebagai nama pengguna dan alamat IP adalah `192.168.1.40`, perintah yang harus dimasukkan adalah:
`SSH planb@192.168.1.40`

Kamu akan diminta untuk memasukkan kata sandi pengguna. Masukkan dan kemudian tekan `enter` untuk memvalidasi. Kamu kemudian akan mengakses antarmuka RoninCLI. Gunakan panah pada keyboard kamu untuk menavigasi ke menu `Samourai Toolkit` dan tekan `enter` untuk memilihnya:

![Samourai Toolkit](assets/notext/43.webp)

Kemudian pilih `Boltzmann Calculator`:

![boltzmann](assets/notext/49.webp)

Kamu akan tiba di halaman utama perangkat lunak:

![boltzmann home](assets/notext/51.webp)

Masukkan TXID dari transaksi yang ingin kamu pelajari dan tekan tombol `enter`:

![boltzmann txid](assets/notext/52.webp)

Kalkulator kemudian menyediakan kamu dengan semua indikator yang telah kami bahas sebelumnya:

![boltzmann result](assets/notext/53.webp)

### Fitur Lain dari RoninDojo v2 Anda
Node RoninDojo kamu mengintegrasikan berbagai fitur lain. Khususnya, kamu bisa memindai informasi tertentu agar ikut diperhitungkan. Misalnya, kadang dompet Samourai kamu yang terhubung ke RoninDojo tidak menampilkan bitcoin yang sebenarnya kamu miliki. Jika saldo menunjukkan 0 padahal kamu yakin ada bitcoin di dompet itu, ada beberapa kemungkinan penyebabnya, seperti kesalahan jalur derivasi. Tapi salah satu penyebab lainnya bisa jadi node kamu tidak memantau alamat kamu dengan benar.

Untuk menyelesaikan masalah ini, kamu bisa memastikan bahwa node kamu memang mengikuti `xpub` kamu menggunakan _xpub tool._ Untuk mengakses alat ini lewat RoninUI, ikuti jalur:

`Maintenance > XPUB Tool`

Masukkan `xpub` yang menyebabkan masalah dan klik tombol `Check` untuk memverifikasi informasi ini:
![xpub tool](assets/notext/54.webp)
Pastikan semua transaksi terdaftar dengan benar. Juga penting untuk memverifikasi bahwa jenis derivasi yang digunakan cocok dengan dompet milikmu. Jika ini bukan kasusnya, klik pada `Retype`, kemudian pilih dari `BIP44`, `BIP49`, atau `BIP84` sesuai dengan kebutuhan kamu.
Di luar alat ini, tab `Maintenance` dari RoninUI penuh dengan fitur berguna lainnya:
- *Transaction Tool*: Memungkinkan pemeriksaan detail dari transaksi tertentu;
- *Address Tool*: Memungkinkan konfirmasi pelacakan alamat tertentu oleh Dojo kamu;
- *Rescan Blocks*: Memaksa node kamu untuk melakukan pemindaian ulang rentang blok tertentu.

Tab `Push Tx` adalah fitur menarik lainnya dari RoninUI, yang memungkinkan penayangan transaksi yang telah ditandatangani di jaringan Bitcoin. Transaksi harus dimasukkan dalam bentuk heksadesimal.
Mengenai tab lain yang tersedia di dashboard RoninUI kamu:
- `Apps`: Menampung aplikasi Whirlpool, dan pasti akan digunakan untuk mengintegrasikan aplikasi baru di masa depan;
- `Logs`: Menawarkan akses real-time ke log event dari perangkat lunak kamu;
- `System Info`: Memberikan informasi umum tentang node kamu, seperti suhu CPU, penggunaan ruang penyimpanan, atau data RAM. kamu juga akan menemukan opsi `Reboot` dan `Shut down` untuk memulai ulang atau mematikan node;
- `Settings`: Memungkinkan kamu untuk mengubah password pengguna kamu.

Itu dia! Terima kasih telah mengikuti tutorial ini sampai selesai. Jika kamu menikmatinya, saya mendorong kamu untuk membagikannya di media sosial. Selain itu, jika kamu memiliki kesempatan, pertimbangkan untuk mendukung para pengembang yang membuat perangkat lunak bebas dan sumber terbuka ini tersedia untuk komunitas kita dengan donasi: [https://donate.ronindojo.io/](https://donate.ronindojo.io/). Untuk memperdalam pengetahuan kamu tentang RoninDojo dan menemukan lebih banyak sumber daya, saya sangat merekomendasikan untuk mengkonsultasikan link ke sumber daya eksternal yang disebutkan di bawah ini.

**Sumber daya eksternal:**
- [https://ronindojo.io/index.html](https://ronindojo.io/index.html)
- [https://wiki.ronindojo.io/en/home](https://wiki.ronindojo.io/en/home)
- [https://gist.github.com/LaurentMT/e758767ca4038ac40aaf](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [https://medium.com/@laurentmt/memperkenalkan-boltzmann-85930984a159](https://medium.com/@laurentmt/memperkenalkan-boltzmann-85930984a159)
- [https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry](https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry)

