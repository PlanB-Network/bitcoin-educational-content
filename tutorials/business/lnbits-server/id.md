---
name: LNbits Server
description: Instalasi dan konfigurasi server LNbits yang dihosting sendiri di Ubuntu VPS dengan Phoenixd atau di Umbrel
---

![cover](assets/cover.webp)



LNbits adalah antarmuka web sumber terbuka yang mengubah backend Lightning apa pun (LND, Core Lightning, Phoenixd) menjadi platform layanan yang lengkap. Solusi yang dihosting sendiri ini memungkinkan Anda untuk mengelola beberapa portofolio Lightning secara terpisah, menerapkan titik penjualan, membuat sistem donasi atau layanan penagihan, sambil mempertahankan kendali penuh atas dana Anda.



Tutorial ini mencakup dua pendekatan instalasi: **VPS Ubuntu dengan Phoenixd** (solusi ringan tanpa node Bitcoin penuh) dan **Umbrel** (integrasi dengan node LND yang sudah ada). Tidak seperti tutorial LNbits umum Plan ₿ Academy, yang mencakup konsep dan ekstensi, panduan ini berfokus pada prosedur instalasi teknis langkah demi langkah.



## Apa yang dimaksud dengan LNbits?



LNbits adalah sistem akuntansi Lightning yang dikembangkan dalam Python (FastAPI) yang terhubung ke backend yang sudah ada (LND, Core Lightning, Phoenixd). Tidak seperti node Lightning tradisional, LNbits menawarkan antarmuka yang dapat diakses untuk mengelola beberapa portofolio yang terisolasi dengan kunci API mereka sendiri. Anda dapat membuat sub-rekening untuk keluarga, karyawan, atau proyek Anda, tanpa memberi mereka akses ke semua dana Anda.



Arsitektur terpisah menyimpan informasi dalam SQLite (default) atau PostgreSQL (produksi), sementara dana tetap dikelola oleh backend Lightning Anda. Pemisahan ini menjamin portabilitas: Anda dapat bermigrasi dari Phoenixd ke LND tanpa kehilangan data pengguna Anda.



## Fitur utama



LNbits menawarkan **sistem ekstensi** yang serbaguna: TPoS (tempat penjualan), Paywall (monetisasi konten), Acara (tiket), LndHub (server untuk BlueWallet), Kartu Bolt (pembayaran NFC), Pembayaran Terpisah (distribusi otomatis), dan Manajer Pengguna (manajemen pengguna dengan otentikasi).



Dasbor **dashboard** menampilkan saldo waktu nyata, riwayat transaksi, dan alat penagihan. Setiap wallet memiliki URL unik yang berisi kunci API, sehingga memungkinkan akses tanpa login tradisional. Sistem kunci API tiga tingkat** (admin, faktur, hanya-baca) menawarkan kontrol perizinan yang terperinci untuk integrasi yang aman.



LNbits secara native mengimplementasikan **LNURL** (LNURL-pay, LNURL-withdraw, LNURL-auth) dan mendukung **Lightning Address**, menjamin kompatibilitas dengan dompet Lightning modern dan memfasilitasi penyebaran layanan profesional.



## Platform yang didukung



**VPS Ubuntu**: Solusi ringan tanpa node Bitcoin penuh. Prasyarat: 1 vCPU, RAM 1-2 GB, Ubuntu 22.04 LTS, Python 3.10+, Git, UV. HTTPS + nama domain diperlukan untuk eksposur publik (layanan LNURL).



**Tenggelamkan**: Instalasi mudah dari App Store. Prasyarat: simpul Umbrel fungsional dengan LND yang disinkronkan dan saluran terbuka. Konfigurasi otomatis.



Di bawah ini adalah tautan ke tutorial Umbrel dan Umbrel LND:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Instalasi pada VPS Ubuntu dengan Phoenixd



### Langkah 1: Mengamankan server VPS



**Sebelum melakukan instalasi, Anda perlu mengamankan server VPS Ubuntu Anda sesuai dengan aturan yang berlaku. Langkah ini **kritis** untuk melindungi infrastruktur dan dana Lightning Anda.



Berikut adalah panduan terperinci untuk membantu Anda memulai: **[Konfigurasi server Ubuntu awal - Panduan langkah demi langkah](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/)** oleh Daniel P. Costas.



Panduan ini mencakup konfigurasi pengguna, SSH yang aman, firewall (UFW), fail2ban, pembaruan otomatis, dan praktik keamanan sistem yang baik.



### Langkah 2: Menginstal Phoenixd



Setelah server Anda aman, Anda perlu menginstal dan mengonfigurasi Phoenixd. Plan ₿ Academy menawarkan tutorial khusus yang komprehensif yang mencakup instalasi, generasi seed, dan konfigurasi layanan systemd:



https://planb.academy/tutorials/node/lightning-network/phoenixd-beb86edd-f9c0-4bec-ad36-db234c88e7b1

Setelah Phoenixd aktif dan berjalan (periksa dengan `./phoenix-cli getinfo`), catat kata sandi **HTTP** di `~/.phoenix/phoenix.conf** - Anda akan membutuhkannya untuk menghubungkan LNbits ke Phoenixd.



### Penyebaran LNbits



Instal UV dan kloning LNbits :


```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
git clone https://github.com/lnbits/lnbits.git && cd lnbits
uv sync --all-extras
```



Konfigurasikan backend Phoenixd:


```bash
cp .env.example .env && nano .env
```



Tambahkan ke `.env` :


```
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://127.0.0.1:9740
PHOENIXD_API_PASSWORD=<mot-de-passe-phoenix.conf>
```



Uji dengan `uv run lnbits --host 0.0.0.0 --port 5000` lalu buat layanan systemd dengan `Wants=phoenixd.service`.



## Penyiapan awal dan penggunaan pertama



### Aktivasi Pengguna Super



Aktifkan antarmuka administrator di `.env` :


```
LNBITS_ADMIN_UI=true
```



Mulai ulang LNbits (`sudo systemctl restart lnbits`) dan ambil ID Pengguna Super:


```bash
cat ~/lnbits/data/.super_user
```



Buka `http://<IP-VPS>:5000/wallet?usr=<SuperUserID>` untuk panel administrasi. Menu "Server" memungkinkan Anda mengonfigurasi sumber pendanaan, ekstensi, dan akun pengguna.



### Pembuatan akun yang aman



**Penting untuk eksposur publik**: Jika Anda mengekspos contoh LNbits Anda pada nama domain publik yang dapat diakses dari Internet, sangat penting untuk menonaktifkan pembuatan akun pengguna secara gratis.



Dari antarmuka administrasi SuperUser, masuk ke "Pengaturan" dan kemudian ke bagian "Manajemen Pengguna". Di sana Anda akan menemukan opsi "Izinkan pembuatan pengguna baru".



![Gestion des utilisateurs - Sécurité](assets/fr/17.webp)



**Untuk pameran publik dengan nama domain**:




- Anda harus menonaktifkan** opsi "Izinkan pembuatan pengguna baru"
- Tanpa perlindungan ini, siapa pun di Internet bisa membuat akun di instans Anda
- Penyerang dapat membuat akun dan menggunakan likuiditas node Lightning Anda tanpa sepengetahuan Anda
- Anda harus membuat akun pengguna secara manual dari antarmuka SuperUser



**Hanya untuk penggunaan lokal**:




- Opsi ini tidak terlalu penting jika instans Anda hanya dapat diakses secara lokal (http://localhost:5000)
- Namun, menonaktifkan opsi ini adalah praktik keselamatan umum yang baik



Setelah dikonfigurasi, hanya administrator SuperUser yang dapat membuat akun pengguna baru melalui antarmuka "Pengguna". Pendekatan ini menjamin kontrol penuh atas siapa saja yang bisa mengakses infrastruktur Lightning dan menggunakan dana Anda.



### Membuka saluran pertama



Phoenixd secara otomatis mengelola saluran melalui likuiditas otomatis. Hasilkan faktur Lightning sebesar ~30.000 sats dari LNbits dan bayarkan dari wallet lainnya. Phoenixd secara otomatis membuka saluran ke ACINQ. Biaya pembukaan (~20-23k sats) dipotong, sisa saldo (~7-10k sats) muncul setelah konfirmasi on-chain.



Periksa status dengan `./phoenix-cli getinfo`. Kemudian pertimbangkan untuk menonaktifkan likuiditas otomatis (`auto-liquidity=off` di `phoenix.conf`) untuk mengontrol pembukaan saluran.



### Tampilan publik dan HTTPS



**Penting**: HTTPS wajib untuk tampilan publik (keamanan kunci API + kompatibilitas LNURL). Lewati langkah ini hanya untuk penggunaan lokal.



**Caddy (disarankan)**: SSL otomatis. `sudo apt install -y caddy`, edit `/etc/caddy/Caddyfile` :


```
votre-domaine.com {
reverse_proxy 127.0.0.1:5000
}
```


Restart: `sudo systemctl restart caddy`.



** Nginx** : Lebih banyak kontrol. Instal `nginx certbot python3-certbot-nginx`, buat `/etc/nginx/sites-available/lnbits`:


```nginx
server {
listen 80;
server_name votre-domaine.com;
location / {
proxy_pass http://127.0.0.1:5000;
proxy_set_header Host $host;
proxy_set_header X-Forwarded-Proto $scheme;
}
}
```


Aktifkan: `sudo ln -s /etc/nginx/sites-available/lnbits /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl reload nginx && sudo certbot --nginx -d domain-your-domain.com`



Tambahkan ke `.env`: `FORWARDED_ALLOW_IPS=*`



## Pemasangan payung



### Penyebaran dari App Store



Buka Umbrel App Store, cari "LNbits", dan klik "Install".



![Installation LNbits Umbrel](assets/fr/01.webp)



Umbrel secara otomatis memeriksa ketergantungan yang diperlukan. LNbits membutuhkan Lightning Node (LND) untuk bekerja. Jika Lightning node Anda sudah beroperasi, klik "Instal LNbits" untuk mengonfirmasi.



![Dépendances LNbits](assets/fr/02.webp)



Umbrel mengunduh citra Docker, secara otomatis mengonfigurasi koneksi dengan LND, dan memulai kontainer (2-5 menit). Penginstalan berlangsung sepenuhnya di latar belakang.



### Konfigurasi Pengguna Super awal



Saat pertama kali diluncurkan, LNbits meminta Anda untuk membuat akun administrator SuperUser. Masukkan nama pengguna dan kata sandi yang aman untuk melindungi akses ke antarmuka administrasi.



![Configuration SuperUser](assets/fr/03.webp)



**Penting**: Akun SuperUser ini memiliki hak istimewa penuh pada instance LNbits Anda. Pilih kata sandi yang kuat dan simpan dengan aman.



Setelah Anda membuat akun, Anda secara otomatis dibawa ke antarmuka administrasi utama. Umbrel telah menyiapkan LND sebagai sumber pendanaan Anda - semua pembayaran Lightning akan melalui saluran yang ada.



### Akses ke antarmuka administrator



Pada menu sebelah kiri, klik "Pengaturan" untuk mengakses panel administrasi lengkap.



![Interface Settings](assets/fr/04.webp)



Bagian "Manajemen Dompet" menampilkan informasi penting tentang konfigurasi Anda:




- Sumber Pendanaan** : LndBtcRestWallet (koneksi langsung ke node LND Umbrel Anda)
- Saldo Simpul** : Total likuiditas yang tersedia di saluran Lightning Anda
- Saldo LNbits**: Dana yang dialokasikan untuk sistem LNbits (awalnya 0 sats)



Sekarang Anda dapat langsung memanfaatkan likuiditas node Umbrel Anda untuk semua dompet LNbits yang Anda buat. Tidak ada konfigurasi tambahan yang diperlukan - LNbits sudah aktif dan berjalan.



### Manajemen pengguna



Salah satu fitur LNbits yang paling hebat adalah kemampuannya untuk membuat beberapa pengguna independen, masing-masing dengan otentikasi kata sandi dan dompet yang terisolasi. Arsitektur ini memungkinkan untuk memanfaatkan likuiditas node Umbrel Anda sambil menawarkan sub-akun yang benar-benar terisolasi untuk penggunaan yang berbeda: bisnis, keluarga, karyawan, proyek, dll.



Pada menu samping, klik "Pengguna" untuk mengakses manajemen pengguna. Klik "BUAT AKUN" untuk menambahkan pengguna baru.



![Gestion des utilisateurs](assets/fr/05.webp)



Isi formulir pembuatan pengguna:




- Nama pengguna**: Nama pengguna masuk (contoh: "satoshi")
- Atur Kata Sandi**: Aktifkan opsi ini untuk mengatur kata sandi autentikasi
- Kata sandi** dan **Ulang kata sandi**: Mengatur kata sandi untuk pengguna ini



![Création utilisateur satoshi](assets/fr/06.webp)



Kolom opsional (Nostr Public Key, Email, Nama Depan, Nama Belakang) dapat dikosongkan untuk konfigurasi minimal. Klik "BUAT AKUN" untuk mengonfirmasi.



![Confirmation utilisateur créé](assets/fr/07.webp)



Pengguna baru Anda sekarang muncul di daftar pengguna dengan pengenal unik dan nama pengguna.



![Liste des utilisateurs](assets/fr/08.webp)



**Poin penting**: Setiap pengguna dapat masuk sepenuhnya secara mandiri dengan kata sandinya sendiri. Administrator SuperUser tetap memegang kendali penuh melalui antarmuka administrasi.



### Manajemen wallet pengguna



Sekarang setelah pengguna "satoshi" telah dibuat, Anda perlu memberikannya wallet Lightning. Klik ikon wallet (ikon kedua) untuk pengguna yang bersangkutan, kemudian pada "BUAT DOMPET BARU".



![Gestion des wallets](assets/fr/09.webp)



Kotak dialog meminta Anda untuk memberi nama wallet. Masukkan nama deskriptif (misalnya "Wallet Dari Satoshi") dan pilih mata uang tampilan (CUC, USD, EUR, dll.).



![Création wallet](assets/fr/10.webp)



Klik pada "BUAT". LNbits langsung menghasilkan wallet Lightning yang berfungsi untuk pengguna ini.



![Confirmation wallet créé](assets/fr/11.webp)



Anda sekarang melihat dua dompet yang ada: wallet default "LNbits wallet" yang dibuat secara otomatis, dan "Wallet Of Satoshi" yang baru. Untuk menyederhanakan pengalaman pengguna, Anda dapat menghapus wallet default dengan mengklik ikon hapus (tempat sampah berwarna merah).



![Wallet final unique](assets/fr/12.webp)



Pengguna "satoshi" sekarang memiliki satu wallet yang teridentifikasi dengan jelas. Setiap pengguna wallet beroperasi sepenuhnya secara otonom saat menggunakan likuiditas dari node LND yang mendasarinya.



**Konsep kunci**: Semua dompet ini berbagi likuiditas global dari node Umbrel Anda. Anda tidak membuat saluran Lightning baru untuk setiap wallet - LNbits bertindak sebagai lapisan akuntansi cerdas yang mengelola alokasi dana dalam infrastruktur Lightning Anda yang sudah ada. Itulah kekuatan sistem multi-wallet LNbits.



### Login pengguna



Keluar dari akun SuperUser (ikon di kanan atas) dan kembali ke halaman login LNbits. Anda sekarang dapat masuk dengan kredensial pengguna baru.



![Connexion utilisateur satoshi](assets/fr/13.webp)



Masukkan nama pengguna ("satoshi") dan kata sandi yang telah ditentukan sebelumnya, lalu klik "LOGIN". Pengguna mendapatkan akses langsung ke wallet pribadinya, yang sepenuhnya terisolasi dari antarmuka administrasi.



### Interface dari pengguna wallet



Setelah masuk, pengguna mengakses antarmuka wallet Lightning yang lengkap.



![Interface wallet utilisateur](assets/fr/14.webp)



Fitur antarmuka :




- Saldo saat ini**: Ditampilkan dalam sats dan dalam mata uang yang dipilih (CUC dalam contoh ini)
- Tindakan utama**: PERMINTAAN TEMPATKAN, BUAT Faktur, ikon QR (pemindaian cepat)
- Riwayat transaksi** : Daftar lengkap semua pembayaran dan penerimaan
- Panel sisi kanan**: Opsi konfigurasi dan akses



### Akses seluler ke wallet



Panel sisi kanan menawarkan fitur yang sangat praktis: akses seluler ke wallet. Buka bagian "Akses Seluler" untuk menemukan opsi yang tersedia.



![Mobile Access](assets/fr/15.webp)



LNbits menawarkan beberapa cara untuk menggunakan wallet ini pada smartphone:



**Opsi 1: Aplikasi seluler yang kompatibel




- Unduh **Zeus** atau **BlueWallet** dari App Store atau Google Play
- Aktifkan ekstensi **LndHub** di LNbits untuk wallet ini
- Pindai kode QR LndHub dengan aplikasi seluler untuk menghubungkan wallet



**Opsi 2: Akses langsung melalui browser seluler**




- Kode QR yang ditampilkan dalam "Ekspor ke Ponsel dengan Kode QR" berisi URL lengkap wallet dengan autentikasi terintegrasi
- Pindai kode QR ini dari ponsel cerdas Anda untuk membuka wallet secara langsung di browser seluler Anda
- Menambahkan halaman ke layar beranda untuk akses cepat



**Keamanan penting**: URL ini berisi kunci API untuk akses penuh ke wallet. Jangan pernah membagikannya secara publik. Perlakukan kode QR ini seperti Anda memperlakukan kunci pribadi Bitcoin Anda - siapa pun yang memindai kode QR ini akan mendapatkan akses penuh ke wallet.



Fitur seluler ini mengubah instance LNbits Umbrel Anda menjadi server Lightning wallet yang sesungguhnya untuk Anda dan teman-teman Anda, sambil mempertahankan kedaulatan penuh atas dana Anda berkat node yang dihosting sendiri.



### Berbagi akses pengguna



Kasus penggunaan utama untuk konfigurasi multi-pengguna ini adalah **berbagi dompet dengan keluarga atau lingkaran dekat Anda**. Setelah Anda membuat pengguna dengan wallet khusus (seperti "satoshi" dalam contoh kami), Anda bisa membagikan kredensial login ini dengan anggota keluarga Anda yang tepercaya.



**Keamanan akses di Umbrel**: Akses ke instans LNbits Anda di Umbrel secara alami dilindungi, karena hanya dapat diakses :




- Di jaringan lokal Anda** : Anggota rumah tangga Anda yang tersambung ke jaringan WiFi/Ethernet yang sama dapat mengakses instance
- Melalui VPN**: Jika Anda menggunakan VPN seperti Tailscale yang dikonfigurasikan pada server Umbrel Anda, pengguna yang diotorisasi bisa mendapatkan akses jarak jauh yang aman



Lapisan perlindungan ganda ini (akses jaringan + autentikasi pengguna) membuat opsi "Izinkan pembuatan pengguna baru" tidak terlalu penting pada Umbrel. Hanya orang yang sudah memiliki akses ke jaringan atau VPN Anda yang bisa mencapai antarmuka login.



**Skenario umum**: Anda membuat akun "ayah", akun "ibu", akun "bisnis", dan seterusnya. Setiap anggota keluarga memiliki wallet Lightning yang terisolasi, sambil memanfaatkan likuiditas bersama dari node Umbrel Anda. Cukup bagikan nama pengguna dan kata sandi - pengguna kemudian dapat terhubung dari perangkat apa pun di jaringan lokal Anda atau melalui VPN Tailscale Anda. Silakan lihat tutorial khusus Tailscale kami untuk informasi lebih lanjut:



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Jelajahi ekstensi yang tersedia



Kembali ke antarmuka SuperUser dan akses menu "Extensions" di panel sebelah kiri untuk menemukan ekosistem ekstensi LNbits yang lengkap.



![Extensions disponibles](assets/fr/16.webp)



LNbits menawarkan katalog ekstensi yang kaya yang mengubah instance Anda menjadi platform layanan Lightning yang sesungguhnya:





- Jukebox**: Sistem jukebox bertenaga sats (pembayaran Spotify)
- Tiket Dukungan**: Sistem dukungan berbayar (menerima satss untuk menjawab pertanyaan)
- TPoS**: Terminal point-of-sale seluler yang aman untuk peritel
- Manajer Pengguna**: pengguna tingkat lanjut dan manajemen wallet (yang baru saja kami gunakan)
- Acara**: Penjualan dan validasi tiket acara
- Perangkat LNURLDevice**: Manajemen titik penjualan, ATM, sakelar yang terhubung
- SMTP**: Memungkinkan pengguna untuk mengirim email dan mendapatkan satss
- Boltcards**: Memprogram kartu NFC untuk pembayaran tap-to-bayar Lightning
- NostrNip5**: Buat alamat NIP5 untuk domain Anda
- Pembayaran terpisah**: Distribusi pembayaran secara otomatis di antara beberapa dompet



Setiap ekstensi diaktifkan dengan satu klik dari antarmuka ini. Ekstensi bertanda "GRATIS" tidak dikenai biaya, sementara beberapa tersedia sebagai versi "BERBAYAR". Jelajahi katalog untuk mengidentifikasi ekstensi yang sesuai dengan kebutuhan Anda - baik untuk bisnis, manajemen keluarga, atau bereksperimen dengan kemampuan Lightning Network.



## Keuntungan dan keterbatasan



**Manfaat**: Kedaulatan finansial (kontrol penuh atas dana/kunci/data), fleksibilitas arsitektur (migrasi VPS lossless→full node), sistem ekstensi profesional, antarmuka yang intuitif.



**Keterbatasan** : Perangkat lunak dalam versi beta (hati-hati dengan jumlah), keamanan di bawah tanggung jawab administrator, URL yang mengandung kunci API yang sensitif (wajib HTTPS), manajemen multi-pengguna menyiratkan tanggung jawab kustodian.



## Praktik terbaik



**Cadangan**: Kredensial Phoenixd Seed / LND, basis data LNbits, file .env. Otomatis setiap hari, jauhkan dari server produksi, terenkripsi. Tes pemulihan secara teratur.



**Pemeliharaan**: Periksa pembaruan secara teratur (LNbits, Lightning backend, sistem operasi). Selalu periksa catatan rilis sebelum pembaruan besar.





- Pada Payung**: App Store secara otomatis memberi tahu Anda tentang versi baru. Menyelaraskan ekstensi melalui "Kelola Ekstensi" > "Perbarui Semua". Periksa penyertaan pangkalan data SQLite dalam pencadangan automatik Umbrel.
- Pada VPS**: Perbarui secara manual dengan `cd lnbits && git pull && uv sync --all-extras && sudo systemctl restart lnbits`. Memantau log sistem: `sudo journalctl -u lnbits -f`.



## Kesimpulan



Self-hosting LNbits menawarkan jalur konkret menuju kedaulatan keuangan Lightning. VPS+Phoenixd menawarkan solusi ringan untuk layanan cepat, integrasi penuh Umbrel dengan node Bitcoin yang ada. Arsitektur yang dapat diskalakan memungkinkan evolusi dari wallet multi-pengguna yang sederhana ke kasus penggunaan bisnis yang canggih.



Self-hosting menyiratkan tanggung jawab: mencadangkan benih, melindungi akses, memulai dengan jumlah yang tidak terlalu besar. Dengan tindakan pencegahan ini, LNbits menjadi solusi yang kuat untuk ekonomi Lightning, sambil mempertahankan desentralisasi dan otonomi.



## Sumber daya



### Dokumentasi resmi




- [Dokumentasi LNbits](https://docs.lnbits.org)
- [LNbits GitHub](https://github.com/lnbits/lnbits)
- [Phoenixd GitHub](https://github.com/ACINQ/phoenixd)
- [Panduan instalasi resmi](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md)



### Panduan komunitas




- [Konfigurasi server Ubuntu awal](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/) oleh Daniel P. Costas (keamanan VPS langkah demi langkah)
- [Instalasi LNbits + Phoenixd di Ubuntu VPS] (https://danielpcostas.dev/install-lnbits-phoenixd-vps-ubuntu/) oleh Daniel P. Costas (panduan lengkap)
- [LNbits Server di Clearnet](https://ereignishorizont.xyz/lnbits-server/en/) oleh Axel
- [LNbits on VPS](https://github.com/TrezorHannes/vps-lnbits) oleh Hannes