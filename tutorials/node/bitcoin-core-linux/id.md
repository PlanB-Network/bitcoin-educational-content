---
name: Bitcoin Core (Linux)
description: Menjalankan simpul Anda sendiri dengan Bitcoin core di Linux
---

![cover](assets/cover.webp)


## Menjalankan node Anda sendiri dengan Bitcoin core


Pengantar ke Bitcoin dan konsep simpul, dilengkapi dengan panduan instalasi yang komprehensif di Linux.


Salah satu aspek yang paling menarik dari Bitcoin adalah kemampuan untuk menjalankan program sendiri, dan dengan demikian berpartisipasi pada tingkat granular dalam jaringan dan verifikasi transaksi publik Ledger.


Bitcoin, sebagai proyek sumber terbuka, telah tersedia secara bebas dan didistribusikan secara publik sejak 2009. Hampir 17 tahun setelah didirikan, Bitcoin sekarang menjadi jaringan moneter digital yang kuat dan tak terbendung, yang diuntungkan oleh efek jaringan organik yang kuat. Atas upaya dan visi mereka, Satoshi Nakamoto layak mendapatkan ucapan terima kasih. Omong-omong, kami menghosting whitepaper Bitcoin di sini di Agora 256 (catatan: juga di universitas).


### Menjadi bank Anda sendiri


Menjalankan node Anda sendiri telah menjadi hal yang penting bagi para penganut etos Bitcoin. Tanpa meminta izin siapa pun, Anda dapat mengunduh Blockchain dari awal dan dengan demikian memverifikasi semua transaksi dari A hingga Z sesuai dengan protokol Bitcoin.


Program ini juga menyertakan Wallet sendiri. Dengan demikian, kami memiliki kendali atas transaksi yang kami kirimkan ke seluruh jaringan, tanpa perantara atau pihak ketiga. Anda adalah bank Anda sendiri.


Oleh karena itu, sisa artikel ini adalah panduan untuk menginstal Bitcoin core - versi perangkat lunak Bitcoin yang paling banyak digunakan - secara khusus pada distribusi Linux yang kompatibel dengan Debian seperti Ubuntu dan Pop!OS. Ikuti panduan ini untuk selangkah lebih dekat dengan kedaulatan pribadi Anda.


## Panduan Instalasi Bitcoin core untuk Debian/Ubuntu


*prasyarat** *Persyaratan


- Penyimpanan data minimum 6GB (node pruned) - Penyimpanan data 1TB (Full node)
- Pengunduhan Blok Awal (IBD) membutuhkan waktu setidaknya 24 jam. Operasi ini wajib dilakukan bahkan untuk node pruned.
- Izinkan ~600GB bandwidth untuk IBD, bahkan untuk node pruned.


**Catatan:💡** perintah berikut ini sudah ditetapkan untuk Bitcoin core versi 24.1.


### Mengunduh dan Memverifikasi File



- [Unduh](https://bitcoincore.org/en/download/) `Bitcoin-24.1-x86_64-linux-gnu.tar.gz`, serta file `SHA256SUMS` dan `SHA256SUMS.asc` (tentu saja Anda harus mengunduh versi terbaru dari perangkat lunak ini).



- Buka terminal di direktori tempat file yang diunduh berada. Contoh: `cd ~/Downloads/`.



- Verifikasi bahwa checksum file versi tercantum dalam file checksum menggunakan perintah `sha256sum --ignore-missing --check SHA256SUMS`.



- Keluaran dari perintah ini harus menyertakan nama file versi yang diunduh diikuti dengan `OK`. Example: `Bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK`.



- Instal git menggunakan perintah `sudo apt install git`. Kemudian, kloning repositori yang berisi kunci PGP dari penandatangan Bitcoin core menggunakan perintah `git clone https://github.com/Bitcoin-core/guix.sigs`.



- Impor kunci PGP dari semua penandatangan menggunakan perintah `gpg --import guix.sigs/builder-keys/*`



- Verifikasi bahwa file checksum ditandatangani dengan kunci PGP dari penandatangan menggunakan perintah `gpg --verify SHA256SUMS.asc`.



Setiap tanda tangan yang valid akan menampilkan baris yang dimulai dengan: `gpg: Tanda tangan yang bagus` dan baris lain yang diakhiri dengan: `Sidik jari kunci utama: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320` (contoh sidik jari kunci PGP Pieter Wuille).


**Catatan💡:** Tidak perlu semua tombol penanda tangan mengembalikan "OK". Bahkan, hanya satu saja yang diperlukan. Terserah kepada pengguna untuk menentukan ambang batas validasi mereka sendiri untuk verifikasi PGP.


Anda dapat mengabaikan peringatan tersebut:



- "Kunci ini tidak disertifikasi dengan tanda tangan tepercaya!



- 'Tidak ada indikasi bahwa tanda tangan tersebut adalah milik pemiliknya'


### Pemasangan Bitcoin core grafis Interface



- Pada terminal, masih pada direktori di mana file versi Bitcoin core berada, gunakan perintah `tar xzf Bitcoin-24.1-x86_64-linux-gnu.tar.gz` untuk mengekstrak file-file yang terdapat pada arsip.



- Instal berkas yang telah diekstrak sebelumnya dengan menggunakan perintah `sudo install -m 0755 -o root -g root -t /usr/local/bin Bitcoin-24.1/bin/*`



- Instal dependensi yang diperlukan menggunakan perintah `sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev`



- Mulai _bitcoin-qt_ (Bitcoin core grafis Interface) menggunakan perintah `Bitcoin-qt`.



- Untuk memilih node pruned, centang _Limit Blockchain storage_ dan konfigurasikan batas data yang akan disimpan:


![welcome](assets/fr/02.webp)


### Kesimpulan Bagian 1: Panduan Instalasi


Setelah Bitcoin core dipasang, disarankan untuk tetap menjalankannya sebanyak mungkin untuk berkontribusi pada jaringan Bitcoin dengan memverifikasi transaksi dan mengirimkan blok baru ke rekan-rekan lainnya.


Namun, menjalankan dan menyinkronkan node Anda sesekali, bahkan hanya untuk memvalidasi transaksi yang diterima dan dikirim, tetap merupakan praktik yang baik.


![Creation wallet](assets/fr/03.webp)


## Mengkonfigurasi Tor untuk Node Bitcoin core


**Catatan💡:** Panduan ini dirancang untuk Bitcoin core 24.0.1 pada distribusi Linux yang kompatibel dengan Ubuntu/Debian.


### Menginstalasi dan mengkonfigurasi Tor untuk Bitcoin core


Pertama, kita perlu menginstal layanan Tor (The Onion Router), sebuah jaringan yang digunakan untuk komunikasi anonim, yang memungkinkan kita untuk menganonimkan interaksi kita dengan jaringan Bitcoin. Untuk pengenalan pada perangkat perlindungan privasi online, termasuk Tor, lihat artikel kami tentang topik ini.


Untuk menginstal Tor, buka terminal dan masukkan `sudo apt -y install tor`. Setelah instalasi selesai, layanan ini biasanya akan diluncurkan secara otomatis di latar belakang. Periksa apakah Tor berjalan dengan benar dengan perintah `sudo systemctl status tor`. Respons yang muncul seharusnya adalah `Active: active (exited)`. Tekan `Ctrl+C` untuk keluar dari fungsi ini.


**Tip:** Dalam hal apa pun, Anda dapat menggunakan perintah berikut ini di terminal untuk memulai, menghentikan, atau memulai ulang Tor:


```shell
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```


Selanjutnya, mari kita luncurkan Bitcoin core grafis Interface dengan perintah `Bitcoin-qt`. Kemudian, aktifkan fitur otomatis perangkat lunak untuk merutekan koneksi kita melalui proxy Tor: pengaturan > Jaringan, dan dari sana centang _Hubungkan melalui proksi SOCKS5 (proksi default)_ serta _Gunakan proksi SOCKS5 yang terpisah untuk menjangkau rekan-rekan melalui layanan Tor onion_.


![option](assets/fr/04.webp)


Bitcoin core secara otomatis mendeteksi jika Tor terinstal dan, jika iya, secara default akan membuat koneksi keluar ke node lain yang juga menggunakan Tor, di samping koneksi ke node yang menggunakan jaringan IPv4/IPv6 (clearnet).


**Catatan💡:** untuk mengubah bahasa tampilan ke bahasa Prancis, buka tab Display (Tampilan) dalam Pengaturan.


### Konfigurasi Tor Lanjutan (opsional)


Dimungkinkan untuk mengkonfigurasi Bitcoin core untuk hanya menggunakan jaringan Tor untuk terhubung dengan rekan-rekan, sehingga mengoptimalkan anonimitas kita melalui node kita. Karena tidak ada fungsionalitas bawaan untuk ini dalam Interface grafis, kita perlu membuat file konfigurasi secara manual. Masuk ke Pengaturan, lalu Opsi.


![option 2](assets/fr/05.webp)


Di sini, klik _Buka file konfigurasi_. Setelah berada di file teks `Bitcoin.conf`, cukup tambahkan baris `onlynet=onion` dan simpan file tersebut. Anda perlu memulai ulang Bitcoin core agar perintah ini dapat diterapkan.


Kita kemudian akan mengkonfigurasi layanan Tor sehingga Bitcoin core dapat menerima koneksi yang masuk melalui proxy, sehingga memungkinkan node lain dalam jaringan untuk menggunakan node kita untuk mengunduh data Blockchain tanpa mengorbankan keamanan mesin kita.


Pada terminal, masukkan `sudo nano /etc/tor/torrc` untuk mengakses berkas konfigurasi layanan Tor. Pada berkas ini, cari baris `#ControlPort 9051` dan hapus `#` untuk mengaktifkannya. Sekarang tambahkan dua baris baru pada berkas tersebut:


```
HiddenServiceDir /var/lib/tor/bitcoin-service/
HiddenServicePort 8333 127.0.0.1:8334
```


Untuk keluar dari berkas sambil menyimpannya, tekan `Ctrl+X > Y > Enter`. Kembali ke terminal, mulai ulang Tor dengan memasukkan perintah `sudo systemctl restart tor`.


Dengan konfigurasi ini, Bitcoin core akan dapat membuat koneksi masuk dan keluar dengan node lain di jaringan hanya melalui jaringan Tor (Onion). Untuk mengonfirmasi hal ini, klik pada tab _Window_, kemudian _Peers_.


![Nodes Window](assets/fr/06.webp)


### Sumber Daya Tambahan


Pada akhirnya, hanya menggunakan jaringan Tor (`onlynet=onion`) bisa membuat Anda rentan terhadap Sybil Attack. Itulah mengapa beberapa orang merekomendasikan untuk mempertahankan konfigurasi multi-jaringan untuk mengurangi jenis risiko ini. Lebih jauh lagi, semua koneksi IPv4/IPv6 akan dirutekan melalui proksi Tor setelah dikonfigurasi, seperti yang ditunjukkan sebelumnya.


Sebagai alternatif, untuk tetap berada di jaringan Tor dan mengurangi risiko Sybil Attack, Anda dapat menambahkan Address dari simpul tepercaya lainnya ke berkas `Bitcoin.conf` Anda dengan menambahkan baris `addnode=trusted_address.onion`. Anda dapat menambahkan baris ini beberapa kali jika Anda ingin menyambung ke beberapa simpul tepercaya.


Untuk melihat log dari node Bitcoin Anda yang secara khusus berhubungan dengan interaksinya dengan Tor, tambahkan `debug=tor` pada berkas `Bitcoin.conf`. Anda sekarang akan memiliki informasi Tor yang relevan dalam log debug Anda, yang dapat Anda lihat di jendela _Information_ dengan tombol _Debug File_. Anda juga dapat melihat log ini secara langsung pada terminal dengan perintah `bitcoind -debug=tor`.


**Kiat💡:** Berikut ini ada beberapa tautan yang menarik:


- [Halaman Wiki yang menjelaskan Tor dan hubungannya dengan Bitcoin] (https://en.Bitcoin.it/wiki/Tor)
- [Generator file konfigurasi Bitcoin core oleh Jameson Lopp](https://jlopp.github.io/Bitcoin-core-config-generator/)
- [Panduan konfigurasi Tor oleh Jon Atack](https://github.com/Bitcoin/Bitcoin/blob/master/doc/tor.md)


Seperti biasa, jika Anda memiliki pertanyaan, jangan ragu untuk berbagi dengan komunitas Agora256. Kita belajar bersama untuk menjadi lebih baik di hari esok daripada hari ini!