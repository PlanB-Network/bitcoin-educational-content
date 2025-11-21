---
name: Phoenixd
description: Menerapkan simpul Lightning minimalis Anda sendiri dengan Phoenixd
---

![cover](assets/cover.webp)



Otonomi keuangan juga berarti mengendalikan infrastruktur Lightning Anda. Untuk pengembang dan perusahaan yang ingin mengintegrasikan Bitcoin Lightning ke dalam aplikasi mereka, **Phoenixd** merupakan solusi ideal: node Lightning khusus yang minimalis dengan manajemen likuiditas otomatis.



Phoenixd adalah server Lightning yang dikembangkan oleh ACINQ, yang dirancang khusus untuk mengirim dan menerima pembayaran Lightning melalui API HTTP. Tidak seperti implementasi dengan fitur lengkap seperti LND atau Core Lightning, Phoenixd mengabstraksikan semua kerumitan manajemen saluran sambil menjaga keamanan dana Anda.



Dalam tutorial ini, kita akan melihat cara menginstal, mengonfigurasi, dan menggunakan Phoenixd untuk mengembangkan aplikasi Lightning dengan infrastruktur yang dihosting sendiri dan API yang mudah digunakan.



## Apa itu Phoenixd?



Phoenixd adalah simpul Lightning khusus minimal yang dikembangkan oleh ACINQ. Ini adalah solusi yang dirancang untuk pengembang dan perusahaan yang ingin mengintegrasikan Lightning ke dalam aplikasi mereka tanpa kerumitan manajemen Full node.



### Prinsip operasi



**Phoenixd adalah node Lightning minimal yang menggunakan ACINQ sebagai LSP (Lightning Service Provider) untuk likuiditas otomatis. Ketika Anda menerima pembayaran Lightning, secara otomatis membuka saluran dengan node ACINQ untuk mengalokasikan kapasitas masuk yang diperlukan. Likuiditas "on-the-fly" ini bersifat instan, tetapi dibebankan tepat pada **1% + biaya Mining** dari jumlah yang diterima.



**Manajemen otomatis:** Sistem ini mengelola tiga Elements utama:




- Saluran petir**: Buka, tutup, dan kelola secara otomatis sesuai kebutuhan
- Likuiditas masuk/keluar**: Penyediaan otomatis melalui penyambungan dan pembukaan saluran
- Kredit biaya** : Pembayaran kecil yang tidak mencukupi untuk membenarkan suatu saluran disimpan sebagai cadangan untuk biaya di masa mendatang



### Manfaat Phoenixd



**Anda mengontrol kunci pribadi Anda (12 kata seed) dan dana. Phoenixd menghasilkan Wallet Anda secara lokal tanpa pernah membagikan kunci Anda.



**Infrastruktur pribadi:** Phoenixd berjalan di server Anda, memberi Anda akses ke log terperinci, konfigurasi, dan kontrol API. Anda tidak lagi bergantung pada layanan pihak ketiga untuk mengakses dana Anda.



**API terintegrasi:** Phoenixd memiliki fitur HTTP API untuk integrasi dengan layanan lain, dukungan LNURL asli, dan pengembangan aplikasi khusus.



**Kemudahan integrasi:** Berkat API REST-nya yang sederhana, Phoenixd dapat diintegrasikan ke dalam aplikasi atau layanan apa pun yang membutuhkan pembayaran Lightning.



**Catatan penting:** Likuiditas otomatis masih berasal dari ACINQ sebagai LSP (Lightning Service Provider). Phoenixd menggunakan mekanisme yang sama dengan Phoenix mobile untuk manajemen saluran otomatis.



## Menginstal Phoenixd



### Prasyarat



Phoenixd membutuhkan lingkungan Linux (disarankan Ubuntu/Debian), dengan beberapa keterampilan dasar baris perintah. Untuk kinerja optimal, Anda memerlukan :





- Server Linux**: VPS atau mesin lokal dengan koneksi stabil
- OpenJDK 21** : Lingkungan runtime Java
- Koneksi Internet yang stabil**: Untuk sinkronisasi dengan Lightning Network
- Nama domain** (opsional) : Untuk akses HTTPS yang aman ke API



### Unduh dan pemasangan



**1. Unduh Phoenixd**



Buka halaman [rilis GitHub] (https://github.com/ACINQ/phoenixd/releases) dan unduh versi terbaru untuk arsitektur Anda:



```bash
# For Linux x86_64
# Replace with the latest release
wget https://github.com/ACINQ/phoenixd/releases/download/v0.6.1/phoenixd-0.6.1-linux-x64.zip
unzip -j phoenixd-0.6.1-linux-x64.zip
chmod +x phoenixd phoenix-cli
```



**2. Start-up pertama



Mulai Phoenixd untuk inisialisasi:



```bash
./phoenixd
```



Pada peluncuran pertama, Anda akan diminta untuk mengonfirmasi dua langkah penting dengan mengetik "Saya mengerti" :



**Pesan 1 - Cadangan:**


```
This software is self-custodial, you have full control and responsibility over your funds.
Your 12-words seed is located in /home/<user>/.phoenix, make sure to do a backup or you risk losing your funds.
Do not share the same seed with other phoenix instances (mobile or server), it will cause issues and channel force closes.
```



**Simpan 12 kata ini** - ini adalah satu-satunya jaminan Anda untuk sembuh.



**Pesan 2 - Likuiditas otomatis:**


```
Continuous liquidity
Liquidity management is fully automated.
When receiving a Lightning payment that doesn't fit in your existing channel:
- If the payment amount is large enough to cover mining fees and service fees for automated liquidity,
then your channel will be created or enlarged right away.
- If the payment is too small, then the full amount is added to your fee credit,
and will be used later to pay for future fees. The fee credit is non-refundable.
```



Ketik `Saya mengerti` untuk setiap konfirmasi.



![Premier démarrage](assets/fr/01.webp)



*Phoenixd dimulai untuk pertama kalinya: konfirmasi pencadangan dan likuiditas otomatis*



**3. Konfigurasi dalam layanan** (hanya dalam bahasa Prancis)



Untuk pengoperasian yang berkelanjutan, buatlah sistemd :



```bash
sudo nano /etc/systemd/system/phoenixd.service
```



```ini
[Unit]
Description=Phoenixd - Minimalist Lightning node
After=network.target

[Service]
User=your_user
WorkingDirectory=/home/your_user
ExecStart=/home/your_user/phoenixd
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```



```bash
sudo systemctl daemon-reload
sudo systemctl enable phoenixd
sudo systemctl start phoenixd
```



![Service systemd](assets/fr/02.webp)



*Layanan Phoenixd aktif dan beroperasi melalui sistemd dan `auto-likuiditas` pada kecepatan 2 km/jam*



## Konfigurasi dan keamanan



### File konfigurasi



Phoenixd secara otomatis membuat `~/.phoenix/phoenix.conf` dengan parameter penting:



```conf
# Network (mainnet by default)
chain=mainnet

# Size of automatic channels and requested liquidity amount (in satoshis)
auto-liquidity=2000000

# API configuration
http-bind-address=127.0.0.1
http-bind-port=9740
http-password=auto_generated_password
http-password-limited-access=limited_password
```



**Parameter kunci:**




- `kecairan otomatis`: Ukuran saluran yang dibuka secara otomatis (standar: 2M Sats)
- http-password`: Kata sandi admin untuk API (pembuatan Invoice DAN pengiriman pembayaran)
- http-kata sandi-keterbatasan-akses`: Kata sandi terbatas (hanya untuk pembuatan Invoice)



### Akses aman dengan HTTPS



Secara default, API Phoenixd hanya dapat diakses melalui HTTP lokal (`http://127.0.0.1:9740`). Untuk menggunakan node Anda dari luar (aplikasi seluler, server lain, integrasi web), Anda perlu mengonfigurasi akses HTTPS yang aman.



**Prinsip proksi terbalik:**


```
Internet → nginx (port 443 HTTPS) → Phoenixd (port 9740 HTTP local)
```



**Nginx** bertindak sebagai **reverse proxy**: ia mendengarkan permintaan HTTPS dari Internet pada port 443, mengarahkannya ke Phoenixd secara lokal (port 9740), kemudian mengirimkan respons terenkripsi kembali ke klien.



**Sertifikat SSL/TLS** adalah file digital yang :




- Buktikan identitas server Anda** (mencegah serangan man-in-the-middle)
- Mengaktifkan enkripsi HTTPS**: semua data, termasuk kata sandi API Anda, dienkripsi selama pengiriman
- Dikeluarkan secara gratis** oleh Let's Encrypt melalui alat certbot



Konfigurasi ini memungkinkan Anda untuk :




- Akses aman ke API dari Internet**
- Enkripsi kata sandi API** Anda selama pengiriman (untuk mencegahnya dikirimkan dalam bentuk teks yang jelas)
- Mengintegrasikan Phoenixd** ke dalam aplikasi eksternal yang membutuhkan HTTPS
- Kepatuhan terhadap standar keamanan** untuk API keuangan



Konfigurasikan proxy balik HTTPS ini dengan nginx :



**1. Konfigurasi Nginx**



```bash
sudo apt install nginx certbot python3-certbot-nginx
sudo nano /etc/nginx/sites-available/phoenixd.conf
```



```nginx
server {
listen 80;
server_name phoenixd.your-domain.com;

location / {
proxy_pass http://127.0.0.1:9740;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header Host $host;
}
}
```



```bash
sudo ln -s /etc/nginx/sites-available/phoenixd.conf /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```



**2. Sertifikat SSL**



```bash
sudo certbot --nginx -d phoenixd.your-domain.com
```



### Uji fungsi



Periksa apakah Phoenixd berfungsi dengan baik:



```bash
./phoenix-cli getinfo
./phoenix-cli getbalance
```



Perintah-perintah ini akan mengembalikan informasi JSON mengenai status dan saldo node (awalnya kosong).



![Commandes CLI](assets/fr/03.webp)



*Perintah getinfo dan getbalance untuk memeriksa status node*



## Menggunakan API



### Tes penerimaan pertama



**1. Membuat Petir** Invoice



Gunakan API untuk membuat Invoice pertama Anda:



```bash
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='First test' \
-d amountSat=100000
```



### Memahami mekanisme likuiditas otomatis



**Prinsip dasar:** Ketika Anda menerima pembayaran Lightning, Phoenixd terkadang harus membuka saluran baru untuk dapat menerimanya. Pembukaan saluran ini memerlukan biaya yang akan dipotong secara otomatis dari jumlah yang diterima.



**Contoh konkret dengan 100.000 Sats:**



![Premier test de réception](assets/fr/04.webp)



*Uji penerimaan pertama: Sats 100 ribu diterima, saldo akhir Sats 75.561 setelah dikurangi biaya likuiditas*



```bash
# Payment received: 100,000 sats
# Channel created: 2,115,000 sats total capacity
# Liquidity fee: 24,439 sats
# Final balance: 75,561 sats
```



**Perhitungan biaya:**




- Biaya layanan**: 1% dari kapasitas saluran (2.115.000 Sats) = 21.150 Sats
- Biaya Mining**: ~3.289 Sats (untuk transaksi On-Chain)
- Total**: 24.439 Sats dipotong secara otomatis



**Verifikasi dengan perintah CLI:**


```bash
# View details of all channels
./phoenix-cli listchannels

# Important output:
# "toLocal": 75561000 (your balance in milli-sats)
# "toRemote": 2039439000 (ACINQ's balance)
# Total channel: 2,115,000 sats
```



![Nouveau solde après paiement](assets/fr/05.webp)



*Saldo akhir setelah pembayaran terkirim: 257 Sats tersisa setelah pengiriman Lightning*



**Kredit biaya untuk pembayaran kecil:** Jika Anda menerima pembayaran yang terlalu kecil untuk membuka saluran (< sekitar 25k Sats), pembayaran tersebut akan disimpan dalam "kredit biaya" yang tidak dapat dikembalikan. Kredit ini akan digunakan untuk membayar biaya saluran di masa mendatang ketika Anda menerima jumlah yang cukup.



**2. Mengikuti pembukaan saluran**



Perhatikan log Phoenixd:



```bash
journalctl -u phoenixd -f
```



Anda akan melihat pembukaan saluran dan pemotongan otomatis biaya likuiditas. Biaya bervariasi sesuai dengan kondisi Mempool Bitcoin, tetapi selalu termasuk biaya layanan 1% ditambah biaya Mining saat ini.



**3. Periksa saluran**



```bash
./phoenix-cli listchannels
```



Perintah ini menampilkan saluran aktif Anda dengan status dan saldonya.



### Menyelesaikan operasi API



Phoenixd mengekspos API REST pada port 9740 yang memungkinkan:



**Operasi dasar:**


```bash
# Create an invoice
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='Test payment' \
-d amountSat=100000

# Send a payment (routing fee 0.4%)
curl -X POST http://localhost:9740/payinvoice \
-u :your_password \
-d invoice='lnbc...'

# Check balance
curl http://localhost:9740/getbalance \
-u :your_password

# Send on-chain funds (in case of channel closure)
./phoenix-cli sendtoaddress \
--address bc1q... \
--amountSat 50000 \
--feerateSatByte 12
```



**Penting untuk biaya:**




- Tanda terima**: 1% + biaya Mining untuk likuiditas otomatis
- Pengiriman**: 0.biaya perutean 4% untuk Lightning Network



**Webhooks:** Webhooks memungkinkan Phoenixd untuk **secara otomatis memberi tahu** aplikasi Anda ketika suatu peristiwa terjadi (pembayaran diterima, Invoice dibayar, saluran dibuka, dll.). Daripada terus-menerus meminta Phoenixd untuk pembaruan, aplikasi Anda menerima pemberitahuan HTTP instan.



**Toko online Anda secara otomatis menerima notifikasi ketika pelanggan membayar pesanan, sehingga memungkinkan validasi transaksi secara instan.



Konfigurasi di `phoenix.conf` :


```conf
webhook-url=https://your-app.com/webhook-phoenixd
webhook-secret=votre_secret_de_verification
```



## Aplikasi tingkat lanjut



### Integrasi LNURL



Phoenixd secara native mendukung protokol LNURL untuk integrasi tingkat lanjut:



**LNURL-Pay:** Membayar layanan yang kompatibel dengan LNURL


```bash
curl -X POST http://localhost:9740/lnurlpay \
-u :your_password \
-d lnurl=LNURL1DP68GURN8GHJ7MRWW4EXCTN... \
-d amountSat=100
```



**LNURL-Withdraw :** Mengambil dana dari layanan LNURL


```bash
curl -X POST http://localhost:9740/lnurlwithdraw \
-u :your_password \
-d lnurl=lightning:LNURL1DP68GURN8GHJ7MRW...
```



**LNURL-Auth:** Otentikasi melalui Lightning untuk mengakses layanan


```bash
curl -X POST http://localhost:9740/lnurlauth \
-u :your_password \
-d lnurl=lnurl1dp68gurn8ghj7um5v93kket...
```



### Integrasi dengan LNbits



LNbits dapat menggunakan Phoenixd sebagai sumber pendanaan sesuai dengan [dokumentasi resminya] (https://docs.lnbits.org/guide/wallets.html):



**Konfigurasi LNbits:**


```bash
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://localhost:9740/
PHOENIXD_API_PASSWORD=your_password_phoenixd
```



Integrasi ini memungkinkan Anda untuk membuat sub-akun LNbits yang didukung oleh node Phoenixd Anda, menyediakan Interface berbasis web untuk mengelola beberapa dompet Lightning.



### Aplikasi khusus



Berkat API REST-nya yang komprehensif, Anda dapat mengembangkan file :



**E-commerce:** Integrasi langsung pembayaran Lightning ke dalam toko Anda


**Layanan donasi:** Sistem donasi dengan faktur dan webhook otomatis


**Bot jejaring sosial:** Bot Telegram/Discord dengan fungsi tip


**Paywall Lightning:** Konten premium tersedia dengan biaya Lightning



## Keselamatan dan praktik terbaik



### Perlindungan akses



**Kata sandi API:** Kata sandi yang dibuat secara otomatis adalah kunci untuk perbendaharaan Lightning Anda. Jangan pernah membagikannya, dan ubahlah jika Anda ragu.



**Firewall:** Jangan pernah membiarkan port 9740 terbuka secara langsung ke Internet. Selalu gunakan nginx dengan HTTPS.



**Autentikasi yang ditingkatkan:** Pertimbangkan VPN atau Tailscale untuk membatasi akses ke peladen Anda hanya untuk perangkat yang diotorisasi.



### Cadangan penting



*pemulihan *seed:** Simpan 12 kata Anda di tempat yang aman, di luar server. Ini adalah satu-satunya jaminan pemulihan Anda.



*direktori ~/.phoenix:** Cadangkan folder ini secara teratur (setelah Phoenixd dimatikan) untuk mempertahankan status saluran dan mempercepat pemulihan.



**Kode pemulihan layanan:** Juga simpan kode cadangan untuk semua layanan yang Anda aktifkan 2FA dengan Phoenix.



### Pemantauan dan pemeliharaan



**Log pemantauan:**


```bash
journalctl -u phoenixd -f  # Real-time logs
./phoenix-cli getinfo      # Node status
```



**Pembaruan:** Lihat [rilis GitHub] (https://github.com/ACINQ/phoenixd/releases) untuk versi baru. Memperbarui semudah mengganti biner dan memulai ulang layanan.



## Perbandingan dengan alternatif



### Phoenixd vs standar Phoenix



**Standar Phoenix (seluler) :**




- ✅ Instalasi langsung, tanpa konfigurasi
- ✅ Interface intuitif untuk seluler
- ✅ Penyimpanan otomatis yang sama dengan Phoenixd
- ❌ Tidak ada API untuk pengembang
- ❌ Tidak ada akses ke log terperinci



** Phoenixd (server) :**




- ✅ API HTTP untuk integrasi
- ✅ Akses penuh ke log
- ✅ Infrastruktur pribadi
- ❌ Membutuhkan keterampilan teknis
- ❌ Diperlukan pemeliharaan server



**Keduanya menggunakan ACINQ sebagai LSP untuk likuiditas otomatis.



### Phoenixd vs LND / Petir Inti



** LND / Petir Inti :**




- ✅ Kontrol total, protokol Lightning penuh
- ✅ Komunitas besar, ekosistem yang matang
- ❌ Manajemen likuiditas manual yang kompleks
- ❌ Kurva pembelajaran yang besar



** Phoenixd :**




- ✅ Manajemen likuiditas otomatis (seperti Phoenix mobile)
- ✅ API untuk pengembang
- ✅ Konfigurasi yang disederhanakan
- ❌ Menggunakan ACINQ sebagai LSP (tidak ada perutean independen)
- ❌ Kurang fleksibel dibandingkan dengan node lengkap



## Memecahkan masalah umum



### Masalah akses API



*kesalahan "*Autentikasi gagal":**


1. Periksa kata sandi di file `~/.phoenix/phoenix.conf`


2. Periksa format autentikasi `-u:password`


3. Pastikan Phoenixd berjalan (`./phoenix-CLI getinfo`)



**Batas waktu koneksi:**




- Periksa apakah Phoenixd mendengarkan pada port yang benar (9740)
- Menguji akses lokal sebelum mengonfigurasi HTTPS
- Periksa log: `journalctl -u phoenixd -f`



### Masalah likuiditas



**Pembayaran tidak diterima :**


1. Periksa apakah jumlahnya melebihi ambang batas minimum (~30k Sats)


2. Lihat log untuk mengidentifikasi kesalahan saluran


3. Mulai ulang Phoenixd jika perlu



**Saldo dalam "kredit pengeluaran":**


Pembayaran dalam jumlah kecil disimpan sebagai provisi. Terima jumlah yang lebih besar untuk memicu pembukaan saluran dan keluarkan dana ini.



## Kesimpulan



Phoenixd mewakili kompromi yang sangat baik antara kemudahan penggunaan dan kedaulatan teknis bagi para pengembang. Phoenixd menawarkan API Lightning yang sederhana namun kuat dengan manajemen likuiditas otomatis, menghilangkan kerumitan node Lightning tradisional.



Solusi ini sangat cocok untuk pengembang dan perusahaan yang ingin :




- Integrasikan Bitcoin Lightning ke dalam aplikasi Anda
- Hindari kerumitan manajemen saluran Lightning
- Dapatkan manfaat dari infrastruktur yang dikelola sendiri
- API yang sederhana dan andal



Dengan Phoenixd, Anda membangun infrastruktur Lightning pribadi Anda sendiri dengan REST API modern dan manajemen otomatis aspek teknis. Ini adalah solusi ideal untuk mendemokratisasi integrasi Lightning dalam proyek Anda.



## Sumber daya yang berguna



### Dokumentasi resmi




- GitHub Phoenixd** : [github.com/ACINQ/phoenixd](https://github.com/ACINQ/phoenixd) - Kode sumber dan rilis
- Situs Phoenix Server**: [phoenix.acinq.co/server](https://phoenix.acinq.co/server) - Dokumentasi lengkap
- Pertanyaan Umum Phoenixd** : [phoenix.acinq.co/server/faq](https://phoenix.acinq.co/server/faq) - Pertanyaan yang sering diajukan



### Dukungan komunitas




- Masalah GitHub** : [github.com/ACINQ/phoenixd/issues](https://github.com/ACINQ/phoenixd/issues) - Dukungan teknis
- Twitter ACINQ** : [@ACINQ_co](https://twitter.com/ACINQ_co) - Berita dan pengumuman