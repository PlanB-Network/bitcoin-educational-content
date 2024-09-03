---
name: Bitcoin Core Node (linux)
description: Menjalankan node Anda sendiri dengan Bitcoin Core
---

![cover](assets/cover.webp)

# Menjalankan Node Anda Sendiri dengan Bitcoin Core

Pengenalan tentang Bitcoin dan konsep sebuah node, dilengkapi dengan panduan instalasi yang komprehensif di Linux.

Salah satu proposisi paling menarik dari Bitcoin adalah kemampuan untuk menjalankan program tersebut sendiri, dan dengan demikian berpartisipasi secara granular dalam jaringan dan verifikasi buku besar transaksi publik.

Bitcoin, sebuah proyek open-source, telah didistribusikan secara publik dan tersedia secara gratis sejak tahun 2009. Hampir 15 tahun setelah penciptaannya, Bitcoin kini merupakan jaringan moneter digital yang kuat dan tidak dapat dihentikan, mendapat manfaat dari efek jaringan organik yang kuat. Untuk usaha dan visi mereka, Satoshi Nakamoto pantas mendapatkan rasa terima kasih kita. Ngomong-ngomong, kami menyimpan whitepaper Bitcoin di sini di Agora 256 (catatan: juga di universitas).

## Menjadi Bank Anda Sendiri

Menjalankan node Anda sendiri telah menjadi esensial bagi penganut aksioma Bitcoin. Tanpa meminta izin siapa pun, dimungkinkan untuk mengunduh blockchain dari awal dan dengan demikian memverifikasi semua transaksi dari A sampai Z menurut protokol Bitcoin.

Program ini juga mencakup dompetnya sendiri. Dengan demikian, kita memiliki kontrol atas transaksi yang kita kirim ke sisa jaringan, tanpa perantara atau pihak ketiga. Anda adalah bank Anda sendiri.

Sisa artikel ini adalah panduan untuk menginstal Bitcoin Core — versi perangkat lunak Bitcoin yang paling banyak digunakan — khususnya pada distribusi Linux yang kompatibel dengan Debian seperti Ubuntu dan Pop!_OS. Ikuti panduan ini untuk selangkah lebih dekat ke kedaulatan individu Anda.

## Panduan Instalasi Bitcoin Core untuk Debian/Ubuntu

> Prasyarat
>
> - Minimal 6GB penyimpanan data (node terpotong) — 1TB penyimpanan data (node penuh)
> - Perbolehkan setidaknya 24 jam untuk penyelesaian Initial Block Download (IBD). Operasi ini wajib bahkan untuk node terpotong.
> - Perbolehkan ~600GB bandwidth untuk IBD, bahkan untuk node terpotong.

> 💡 Perintah berikut telah ditentukan sebelumnya untuk versi Bitcoin Core 24.1.

## Mengunduh dan Memverifikasi Berkas

1. Unduh bitcoin-24.1-x86_64-linux-gnu.tar.gz, serta berkas SHA256SUMS dan SHA256SUMS.asc. (https://bitcoincore.org/bin/bitcoin-core-24.1/bitcoin-24.1-x86_64-linux-gnu.tar.gz)

2. Buka terminal di direktori tempat berkas yang diunduh berada. Misalnya, cd ~/Downloads/.
3. Verifikasi bahwa checksum dari berkas versi terdaftar dalam berkas checksum menggunakan perintah sha256sum --ignore-missing --check SHA256SUMS.
4. Output dari perintah ini harus mencakup nama berkas versi yang diunduh diikuti oleh "OK". Contoh: bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK.

5. Instal git menggunakan perintah sudo install git. Kemudian, klon repositori yang berisi kunci PGP dari penandatangan Bitcoin Core menggunakan perintah git clone https://github.com/bitcoin-core/guix.sigs.
6. Impor kunci PGP dari semua penandatangan menggunakan perintah gpg --import guix.sigs/builder-keys/\*
7. Verifikasi bahwa berkas checksum ditandatangani dengan kunci PGP dari penandatangan menggunakan perintah gpg --verify SHA256SUMS.asc.
Setiap tanda tangan akan mengembalikan baris yang dimulai dengan: gpg: Good signature dan baris lain yang berakhir dengan Primary key fingerprint: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320 (contoh dari PGP key fingerprint Pieter Wuille).
> 💡 Tidak diperlukan bagi semua kunci penandatangan untuk mengembalikan "OK". Faktanya, mungkin hanya satu yang diperlukan. Terserah pengguna untuk menentukan ambang batas validasi mereka sendiri untuk verifikasi PGP.
>
> Anda dapat mengabaikan pesan WARNING: This key is not certified with a trusted signature!

> Tidak ada indikasi bahwa tanda tangan tersebut milik pemiliknya.

## Instalasi antarmuka grafis Bitcoin Core

1. Di terminal, masih di direktori tempat file versi Bitcoin Core berada, gunakan perintah tar xzf bitcoin-24.1-x86_64-linux-gnu.tar.gz untuk mengekstrak file yang terkandung dalam arsip.

2. Instal file yang sebelumnya diekstrak menggunakan perintah sudo install -m 0755 -o root -g root -t /usr/local/bin bitcoin-24.1/bin//\*

3. Instal dependensi yang diperlukan menggunakan perintah sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev

4. Mulai bitcoin-qt (antarmuka grafis Bitcoin Core) menggunakan perintah bitcoin-qt.

5. Untuk memilih node yang dipangkas, centang Limit blockchain storage dan konfigurasikan batas data yang akan disimpan:

![welcome](assets/1.webp)

## Kesimpulan Bagian 1: Panduan Instalasi

Setelah Bitcoin Core terinstal, disarankan untuk menjalankannya sebanyak mungkin untuk berkontribusi pada jaringan Bitcoin dengan memverifikasi transaksi dan mengirimkan blok baru ke peer lain.

Namun, menjalankan dan menyinkronkan node Anda secara intermiten, bahkan hanya untuk memvalidasi transaksi yang diterima dan dikirim, tetap merupakan praktik yang baik.

![Creation wallet](assets/2.webp)

# Mengkonfigurasi Tor untuk Node Bitcoin Core

> 💡 Panduan ini dirancang untuk Bitcoin Core 24.0.1 pada distribusi Linux yang kompatibel dengan Ubuntu/Debian.

## Menginstal dan mengkonfigurasi Tor untuk Bitcoin Core

Pertama, kita perlu menginstal layanan Tor (The Onion Router), sebuah jaringan yang digunakan untuk komunikasi anonim, yang akan memungkinkan kita untuk menganonimkan interaksi kita dengan jaringan Bitcoin. Untuk pengenalan tentang alat perlindungan privasi online, termasuk Tor, lihat artikel kami tentang topik ini.

Untuk menginstal Tor, buka terminal dan masukkan sudo apt -y install tor. Setelah instalasi selesai, layanan tersebut biasanya akan secara otomatis diluncurkan di latar belakang. Periksa apakah berjalan dengan benar dengan perintah sudo systemctl status tor. Respons harus menunjukkan Active: active (exited). Tekan Ctrl+C untuk keluar dari fungsi ini.

> Dalam hal apa pun, Anda dapat menggunakan perintah berikut di terminal untuk memulai, menghentikan, atau memulai ulang Tor:

```
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```

Selanjutnya, mari kita luncurkan antarmuka grafis Bitcoin Core dengan perintah bitcoin-qt. Kemudian, aktifkan fitur otomatis perangkat lunak untuk merutekan koneksi kita melalui proxy Tor: Settings > Network, dan dari sana kita dapat memeriksa Connect through SOCKS5 proxy (default proxy) serta Use a separate SOCKS5 proxy to reach peers via Tor onion services.

![option](assets/3.webp)

Bitcoin Core secara otomatis mendeteksi jika Tor terinstal dan, jika ya, secara default akan membuat koneksi keluar ke node lain yang juga menggunakan Tor, selain koneksi ke node yang menggunakan jaringan IPv4/IPv6 (clearnet).
💡 Untuk mengubah bahasa tampilan menjadi Prancis, pergi ke tab Tampilan dalam Pengaturan.
## Konfigurasi Tor Lanjutan (opsional)

Dimungkinkan untuk mengonfigurasi Bitcoin Core agar hanya menggunakan jaringan Tor untuk terhubung dengan peer, sehingga mengoptimalkan anonimitas kita melalui node kita. Karena tidak ada fungsi bawaan untuk ini di antarmuka grafis, kita perlu membuat file konfigurasi secara manual. Pergi ke Pengaturan, lalu Opsi.

![option 2](assets/4.webp)

Di sini, klik pada Buka file konfigurasi. Setelah berada di file teks bitcoin.conf, cukup tambahkan baris onlynet=onion dan simpan file tersebut. Anda perlu memulai ulang Bitcoin Core agar perintah ini berlaku.
Kemudian, kita akan mengonfigurasi layanan Tor sehingga Bitcoin Core dapat menerima koneksi masuk melalui proxy, memungkinkan node lain di jaringan menggunakan node kita untuk mengunduh data blockchain tanpa mengompromikan keamanan mesin kita.

Di terminal, masukkan sudo nano /etc/tor/torrc untuk mengakses file konfigurasi layanan Tor. Di file ini, cari baris #ControlPort 9051 dan hapus # untuk mengaktifkannya. Sekarang tambahkan dua baris baru ke file: HiddenServiceDir /var/lib/tor/bitcoin-service/ dan HiddenServicePort 8333 127.0.0.1:8334. Untuk keluar dari file sambil menyimpannya, tekan Ctrl+X > Y > Enter. Kembali di terminal, mulai ulang Tor dengan memasukkan perintah sudo systemctl restart tor.

Dengan konfigurasi ini, Bitcoin Core akan dapat menetapkan koneksi masuk dan keluar dengan node lain di jaringan hanya melalui jaringan Tor (Onion). Untuk mengonfirmasi ini, klik pada tab Jendela, lalu Peer.

![Nodes Window](assets/5.webp)

## Sumber Daya Tambahan

Pada akhirnya, menggunakan hanya jaringan Tor (onlynet=onion) dapat membuat Anda rentan terhadap serangan Sybil. Itulah mengapa beberapa orang merekomendasikan untuk mempertahankan konfigurasi multi-jaringan untuk mengurangi jenis risiko ini. Selanjutnya, semua koneksi IPv4/IPv6 akan dialihkan melalui proxy Tor setelah dikonfigurasi, seperti yang telah diindikasikan sebelumnya.

Sebagai alternatif, untuk tetap hanya di jaringan Tor dan mengurangi risiko serangan Sybil, Anda dapat menambahkan alamat node terpercaya lain ke file bitcoin.conf Anda dengan menambahkan baris addnode=trusted_address.onion. Anda dapat menambahkan baris ini beberapa kali jika Anda ingin terhubung ke beberapa node terpercaya.

Untuk melihat log dari node Bitcoin Anda khususnya terkait interaksinya dengan Tor, tambahkan debug=tor ke file bitcoin.conf Anda. Sekarang Anda akan memiliki informasi Tor yang relevan di log debug Anda, yang dapat Anda lihat di jendela Informasi dengan tombol File Debug. Juga dimungkinkan untuk melihat log ini langsung di terminal dengan perintah bitcoind -debug=tor.

> 💡 Beberapa tautan menarik:
>
> - Halaman Wiki yang menjelaskan Tor dan hubungannya dengan Bitcoin
> - Generator file konfigurasi Bitcoin Core oleh Jameson Lopp
> - Panduan konfigurasi Tor oleh Jon Atack

Seperti biasa, jika Anda memiliki pertanyaan, jangan ragu untuk berbagi dengan komunitas Agora256. Kita belajar bersama untuk menjadi lebih baik esok hari daripada hari ini!