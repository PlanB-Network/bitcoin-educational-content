---
name: LNbits
description: Platform Akuntansi Pedagang
---
![presentation](assets/lnbits-intro.webp)

# Sistem akuntansi

LNbits dilengkapi dengan banyak alat untuk mengontrol dan menyalurkan dana masuk dan keluar Anda, menghubungkan toko web Anda atau bahkan perangkat seperti dompet perangkat keras atau ATM yang Anda buat sendiri. Jenis pengguna termasuk:


- Pemilik dompet yang ingin menggunakan LNbits sebagai antarmuka untuk manajemen dana mereka serta fitur tambahannya.
- Pedagang online dan offline atau penyedia layanan yang ingin menerima pembayaran Bitcoin onchain dan Lightning Network.
- Pengembang yang ingin membangun aplikasi Lightning Network.
- Operator node yang ingin mengintegrasikan node mereka dengan sistem LNbits untuk tujuan akuntansi.
- Semuanya memiliki kebutuhan yang berbeda. Kami membangun LNbits dengan cara modular sehingga setiap pengguna dapat menggunakan fitur-fitur kami dengan cara yang paling sesuai untuk Anda.

# Manajer dompet

LNbits adalah sistem akuntansi sumber terbuka dan gratis - bukan pengelola node. Manajemen saluran adalah domain node Lightning yang terhubung ke LNbits sebagai sumber pendanaan seperti LND atau c-lightning. Pengguna Superuser atau Admin dalam sistem LNbits bertanggung jawab untuk mengelola keseluruhan akses dan konfigurasi fitur akuntansi dan ekstensi internal.

LNbits bertindak sebagai antarmuka antara pengguna dan node Lightning, menyediakan cara yang sederhana dan mudah digunakan untuk mengelola dan berinteraksi dengan jaringan pembayaran.

Bayangkan LNbits seperti "kerangka kerja modular wordpress" untuk node Anda. Platform yang mudah dikelola, berdasarkan ekstensi yang dapat Anda kombinasikan untuk berbagai kasus penggunaan.

Bayangkan LNbits sebagai perangkat lunak manajemen keuangan bank Anda sendiri. Node Anda menawarkan saluran untuk membayar dan LNbits memperluas node Anda untuk dapat menjalankan lebih dari satu dompet kilat yang disertakan dengan node Anda. Dompet-dompet ini tidak harus menjadi milik Anda sendiri. Katakanlah Anda, sebagai pengelola node LN, telah memiliki likuiditas dan dana yang cukup dan sekarang Anda ingin menawarkan beberapa layanan perbankan bitcoin kepada teman, keluarga, toko Anda sendiri, atau pedagang reguler lainnya.

Anda akan menawarkan cara sederhana kepada mereka untuk membuka "akun perbankan" di node Anda tanpa memiliki akses ke dompet lain di node Anda dan ke semua likuiditas node Anda, tetapi hanya bagian mereka. Node Anda (bank) hanya bertindak sebagai penyedia transportasi untuk pembayaran mereka (masuk/keluar).

CATATAN: semua dana yang disetorkan oleh "pelanggan" Anda ke rekening bank LNbits mereka di node Anda, akan langsung masuk ke saluran LN node Anda. Itu berarti ANDA sebenarnya adalah pemilik sebenarnya dari dana tersebut. Anda akan memiliki tanggung jawab yang besar atas dana mereka. Jangan menjadi jahat dan melarikan diri dengan dana tersebut, jangan menjadi jahat dan membebankan biaya yang tinggi. Kami ingin bercinta dengan para bankir fiat, bukan bercinta dengan satu sama lain (pengguna bitcoin).

# Platform demo

Demo dapat ditemukan di [https://legend.lnbits.com](https://legend.lnbits.com). Demo ini berfungsi penuh dan dapat digunakan untuk mempelajari tentang Lightning Network dan fitur-fitur LNbits dan LNURL secara umum. Meskipun kami tidak dapat mencegah Anda untuk menggunakannya, kami ingin meminta Anda untuk tidak menggunakannya untuk pengaturan produksi Anda. Kami tidak hanya sering bekerja di server untuk menguji fitur-fitur baru, tetapi kami juga ingin mendorong Anda untuk menjalankan node dan LNbits Anda sendiri dengan cara yang berdaulat. Jika Anda merasa menjalankan node terlalu berat untuk saat ini, Anda dapat menghubungkan LNbits ke layanan pendanaan kustodian di cloud seperti Opennode, Luna atau Votage atau ke Lightning Tipbot di Telegram.

# Selebaran LNbits

Ingin memberikan beberapa informasi dasar kepada pedagang atau teman Anda yang sedang membangun? Kami dengan senang hati mengumumkan brosur pertama kami yang dapat digunakan oleh semua orang. Ukurannya adalah format brosur yang umum digunakan secara global dengan 6 halaman (2 lipatan) dan lebar 3508 dan tinggi 2480px.

LNbits untuk pedagang: [EN](/assets/lnbits-merchants-en.pdf) | [DE](/assets/lnbits-merchants-de.pdf) | [ES](/assets/lnbits-merchants-es.pdf) | [IT](/assets/lnbits-merchants-it.pdf) | [PL](/assets/lnbits-merchants-pl.pdf)

LNbits untuk pembangun: [EN](/assets/lnbits-builders-en.pdf) | [DE](/assets/lnbits-builders-de.pdf) | [ES](/assets/lnbits-builders-es.pdf) | [IT](/assets/lnbits-builders-it.pdf) | [PL](/assets/lnbits-builders-pl.pdf)

# Beberapa Hal Dasar

LNbits bekerja berdasarkan protokol LNURL yang berarti bahwa permintaan dapat dilakukan dalam dua bentuk: sebagai tautan https:// clearnet (tidak ada sertifikat yang ditandatangani sendiri) atau sebagai tautan http:// v2/v3 onion. Untuk menawarkan layanan LNbits seperti kode QR LNURLp/w atau Kartu NFC, yang dapat digunakan di alam liar, Anda harus membuka LNbits ke clearnet (https).

Sebelum Anda menginstal LNbits, pastikan Anda telah membaca dan memahami panduan umum berikut ini tentang apa itu LNbits dan apa saja yang bisa dilakukan oleh LNbits untuk Anda.


- [Panduan LND](https://docs.lightning.engineering/) | Menginstalasi LND
- [Contoh Konfigurasi LND](https://github.com/lightningnetwork/lnd/blob/master/sample-lnd.conf) | Pengaturan LND
- [Panduan CLN](https://docs.corelightning.org/docs/installation) | Menginstal CLN
- [LUDs](https://github.com/lnurl/luds) LNURL Spec | [NIPs](https://github.com/nostr-protocol/nips) Nostr Spec
- [Jalankan menara pengawas](https://docs.lightning.engineering/lightning-network-tools/lnd/watchtower) | Sangat penting!

Panduan lebih rinci menggunakan LNbits dalam skenario kasus penggunaan tertentu di sini:


- [Memulai dengan LNbits](https://darthcoin.substack.com/p/getting-started-lnbits) | Panduan substack
- [ToDos untuk keamanan Anda dengan LNbits](https://youtu.be/i5FQf96e6zg) | Video Youtube
- [Bank Swasta di Jaringan Lightning](https://darthcoin.substack.com/p/bitcoin-private-banks-over-lightning) | Panduan Substack
- [Jalankan dompet kustodian untuk teman & keluarga Anda](https://darthcoin.substack.com/p/the-bank-of-lnbits) | Panduan Substack
- [LNbits untuk restoran / hotel kecil](https://darthcoin.substack.com/p/lnbits-for-small-merchants) | Panduan substack
- [Menggunakan kopilot LNbits Streamer](https://darthcoin.substack.com/p/lnbits-streamer-copilot) | Panduan substack
- [Mulai Pasar NOSTR Anda dengan LNbits](https://darthcoin.substack.com/p/lnbits-nostr-market) | Panduan Substack
- [Menggunakan LNbits untuk proyek sekolah atau acara festival](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools) Panduan substack

# Instal LNbits

## Panduan instalasi dasar

LNbits dapat diinstal pada mesin OS Linux apa pun. Tidak membutuhkan mesin atau server yang kuat, hanya cukup memori RAM dan ruang disk untuk database. LNbits dapat dijalankan secara terpisah dari node BTC/LN (PC lokal atau VPS jarak jauh) atau bersama-sama pada mesin yang sama dengan node atau sudah diinstal dalam mesin perangkat lunak node bundel.

Anda dapat memilih di antara manajer paket yang paling umum seperti poetry dan nix. Secara default, LNbits akan menggunakan SQLite sebagai basis datanya. Anda juga dapat menggunakan PostgreSQL yang direkomendasikan untuk aplikasi dengan beban tinggi. [Berikut ini adalah panduan untuk instalasi dasar menggunakan poetry atau nix](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md).

Untuk semua orang yang baru mengenal hal ini, Anda akan menemukan panduan langkah demi langkah yang lebih terperinci untuk menjalankan LNbits Anda di lingkungan tertentu:


- [LNbits di clearnet](https://ereignishorizont.xyz/lnbits-server/en/) oleh Axel
- [LNbits pada VPS](https://github.com/TrezorHannes/vps-lnbits) oleh Hannes
- [LNbits di cloudflare](https://www.nodeacademy.org/lnbits) oleh Leo

Anda juga dapat menemukan video tentang [Pengaturan dockerised pada VPS dengan PostgreSQ, LightningTipBot sebagai sumber pendanaan menggunakan nginx](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/).

[Skenario instalasi lebih lanjut di sini](https://darthcoin.substack.com/p/build-your-own-lnbits-app-server).

Untuk node perangkat lunak bundel, silakan merujuk ke dokumentasi khusus tentang LNbits: [Citadel](https://runcitadel.space) | [Umbrel](https://umbrel.com) | [MyNode](https://mynodebtc.com) | [RaspiBlitz](https://raspiblitz.org/) | [RaspiBolt](https://raspibolt.org)

## LNbits SaaS

Jika Anda tidak tertarik dengan hal-hal teknis dan tidak ingin meng-host sumber pendanaan atau lnbits Anda sendiri, ada [versi LNbits SaaS] (https://saas.lnbits.com) (Perangkat Lunak sebagai layanan) yang dapat Anda gunakan. Pada dasarnya ini seperti LNbits di cloud tetapi Anda dapat menentukan sumber pendanaan (misalnya Node Anda, dompet LNbits, LNtipbot, fakewallet, dll.) dan variabel lingkungan Anda sendiri - yang sebagian besar tidak terjadi pada solusi cloud lainnya.

[Berikut adalah panduan rinci bagaimana menggunakan LNbits SaaS untuk kasus penggunaan tertentu] (https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools).

## Sumber pendanaan

LNbits bukanlah perangkat lunak manajemen node, melainkan sebuah sistem akuntansi yang berfokus pada LN di atas sumber pendanaan LND atau CLN. Setelah instalasi pertama, Anda dapat mengunjungi LNbits di http://localhost:5000/.

Untuk memodifikasi sumber pendanaan, buka super-user-URL Anda dan pilih sumber pendanaan di dalam "Kelola Server" atau edit file .env dengan memodifikasi `LNBITS_BACKEND_WALLET_CLASS` menjadi sumber yang Anda butuhkan jika Anda menetapkan `adminUI = TRUE` pada `.env`.

Anda dapat menemukan berkas .env di dalam folder lnbits/ atau lnbits/apps/data dengan memperpanjang perintah untuk membuat daftar berkas di direktori Anda dengan `ls -a`.

Anda mungkin juga perlu menginstal paket tambahan atau melakukan langkah-langkah pengaturan tambahan, memilih sumber pendanaan yang diinginkan. Setelah restart, pengaturan baru Anda akan aktif.

Sumber pendanaan apa saja yang dapat saya gunakan untuk LNbits?

LNbits dapat berjalan di atas banyak sumber pendanaan jaringan petir. Saat ini ada dukungan untuk CoreLightning, LND, LNbits, LNPay, OpenNode, dan masih banyak lagi yang akan ditambahkan secara berkala.

Penting untuk memilih sumber yang memiliki likuiditas yang baik dan terhubung dengan rekan-rekan yang baik. Jika Anda menggunakan LNbits untuk layanan publik, pembayaran pengguna Anda dapat mengalir dengan lancar ke dua arah.

Dompet backend (sumber pendanaan) dapat dikonfigurasikan menggunakan variabel lingkungan LNbits berikut ini di file `.env` atau di dalam akun pengguna super Anda di bagian Kelola Server.

Jika Anda ingin menggunakan versi .env, Anda dapat menemukan parameternya di sini:

### CoreLightning


- CLN
  - `LNBITS_BACKEND_WALLET_CLASS`: **CoreLightningWallet**
  - `CORELIGHTNING_RPC`: /file/path/ petir-rpc
- Percikan (c-petir)
  - `LNBITS_BACKEND_WALLET_CLASS`: **SparkWallet**
  - `SPARK_URL`: http://10.147.17.230:9737/rpc
   - `SPARK_TAKEN`: kunci_akses_rahasia

### Daemon Jaringan Petir


- LND (REST)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndRestWallet**
  - `LND_REST_ENDPOINT`: http://10.147.17.230:8080/
  - `LND_REST_CERT`: /file/path/tls.cert
  - `LND_REST_MACAROON`: /file/path/admin.macaroon atau Bech64/Hex
  - `LND_REST_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn
- LND (gRPC)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndWallet**
  - `LND_GRPC_ENDPOINT`: ip_address
  - `LND_GRPC_PORT`: port
  - `LND_GRPC_CERT`: /file/path/tls.cert
  - `LND_GRPC_MACAROON`: /file/path/admin.macaroon atau Bech64/Hex

Anda juga dapat menggunakan macaroon terenkripsi AES (info lebih lanjut) dengan menggunakan


  - `LND_GRPC_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn

Untuk mengenkripsi macaroon Anda, jalankan `./venv/bin/python lnbits/wallets/macaroon/macaroon.py`.

### LNbits (contoh LNbits lainnya)


- Instance LNbits dihosting di server cloud atau server rumah Anda sendiri
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://lnbits.mydomain.com
  - `LNBITS_KEY`: my-lnbits-AdminKey
- LNbits Legend Demo Server (!! JANGAN gunakan yang ini untuk tujuan produksi/komersial, hanya untuk pengujian !!)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://legend.lnbits.com
  - `LNBITS_KEY`: legenda-lnbits-AdminKey

### TipBot Petir

Untuk menghubungkan [Lightning Tipbot] (https://t.me/LightningTipBot) Anda dari Telegram, Anda perlu mengatur parameter berikut:


  - `LNBITS_BACKEND_WALLET_CLASS`: ** LnTipsWallet**
  - `LNBITS_ENDPOINT`: https://ln.tips
  - `LNBITS_KEY`: Untuk mendapatkan Key, Anda harus menjalankan /api dalam obrolan pribadi dengan LightningTipbot di Telegram satu kali.

Lihat juga tutorial ini cara menginstal [LNbits dengan LightningTipBot melalui vps] (https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/)

### IBEX HUB

Daftarkan [di sini] (https://ibexpay.ibexmercado.com/onboard) kemudian dapatkan kunci/token Anda dari sana, titik akhir adalah https://ibexpay-api.ibexmercado.com.

Info lebih lanjut lihat [IBEX API-Documentation](https://ibexpay-api.readme.io/reference/getting-started-with-your-api).

### LNPay

Agar pendengar faktur dapat berfungsi, Anda harus memiliki URL yang dapat diakses publik di LNbits Anda dan harus menyiapkan [LNPay webhook] (https://dashboard.lnpay.co/webhook/) yang mengarah ke `<host LNbits Anda>/wallet/webhook` dengan event "Wallet Receive" dan tidak ada rahasia yang diberikan. Pengaturan `https://mylnbits/wallet/webhook` akan menjadi url titik akhir yang akan diberitahukan tentang pembayaran apa pun.


  - `LNBITS_BACKEND_WALLET_CLASS`: **LNPayWallet**
  - `LNPAY_API_ENDPOINT`: https://api.lnpay.co/v1/
  - `LNPAY_API_KEY`: sak_apiKey
  - `LNPAY_WALLET_KEY`: waka_apiKey

### OpenNode

Agar faktur dapat berfungsi, Anda harus memiliki URL yang dapat diakses publik di LNbits Anda. Pengaturan webhook bersifat opsional.


  - `LNBITS_BACKEND_WALLET_CLASS`: **OpenNodeWallet**
  - `OPENNODE_API_ENDPOINT`: https://api.opennode.com/
  - `OPENNODE_KEY`: opennodeAdminApiKey

### Alby

Alby adalah ekstensi browser dengan fungsi dompet LN dan akun LNDHUB yang dapat digunakan sebagai sumber pendanaan untuk LNbits. [Selengkapnya di sini] (https://getalby.com/).

Agar faktur dapat berfungsi, Anda harus memiliki URL yang dapat diakses publik di LNbits Anda. Tidak diperlukan pengaturan webhook manual. Anda dapat membuat token akses Alby di sini: https://getalby.com/developer/access_tokens/new


- `LNBITS_BACKEND_WALLET_CLASS`: AlbyWallet
- `ALBY_API_ENDPOINT`: https://api.getalby.com/
- `ALBY_ACCESS_TOKEN`: AlbyAccessToken

## Panduan Tambahan / Pemecahan Masalah

Berikut ini adalah beberapa petunjuk tambahan jika Anda membutuhkannya. Klik tanda panah untuk memperluas deskripsi.

### Tombol Pembunuh 🚨

Ada begitu banyak bug berbahaya akhir-akhir ini tidak hanya di seluruh dunia tetapi juga di LNbits sehingga kami memutuskan untuk melakukan sesuatu. Sekarang Anda dapat memilih untuk menerima peringatan dan/atau mengambil tindakan langsung, ketika kerentanan atau bug yang dapat menyebabkan hilangnya dana terjadi lagi.

![killswitchn](assets/lnbits-killswitch.webp)

Jika dialihkan ke void-wallet, semua usertype pada instance akan melihat spanduk kuning di mana biasanya Anda akan menemukan pemberitahuan "LNbits dalam versi Beta" di sebelah area tema/bahasa di sebelah kanan - dan ini merupakan petunjuk yang paling jelas, bahwa ada sesuatu yang terjadi. Lihatlah tab server baru Anda yang disorot dengan warna hijau di bagian kiri jendela.

Bagaimana cara kerjanya? Ketika killswitch diaktifkan, repositori github rahasia yang hanya tersedia untuk tim inti LNbits akan diperiksa pada interval X menit (yang dapat ditentukan). Jika bug yang rentan dipublikasikan di repositori ini, ini berfungsi sebagai sinyal yang memicu killswitch pada semua instalasi yang berlangganan dan mentransisikan instance lnbits Anda untuk menggunakan void wallet. Jika awan telah hilang dan Anda telah menginstal pembaruan keamanan, Anda dapat mengatur sumber pendanaan Anda ke node, dompet, atau apa pun yang Anda gunakan lagi melalui bagian Kelola Server. Wiki ini memiliki bagian tentang mengganti sumber pendanaan jika Anda tidak tahu apa yang harus dikonfigurasi.

### Perbedaan antara admin dan pengguna super

LNbits Admin UI memungkinkan Anda mengubah pengaturan LNbits melalui frontend LNbits. Ini dinonaktifkan secara default dan saat pertama kali Anda mengatur variabel lingkungan `LNBITS_ADMIN_UI = true` di file `.env`, pengaturan diinisialisasi dan akan digunakan. Selanjutnya, pengaturan yang sesuai dari database akan digunakan sebagai pengganti pengaturan dari file .env.

### Pengguna Super

Dengan Admin UI, kami memperkenalkan super user yang memiliki akses ke server sehingga dapat mengubah pengaturan yang dapat merusak server atau membuatnya tidak responsif melalui frontend dan api, seperti misalnya mengubah sumber pendanaan. Pengguna super hanya disimpan di dalam tabel pengaturan database. Setelah pengaturan "diatur ulang ke default" dan restart, super user baru akan dibuat. Kami juga menambahkan sebuah dekorator untuk rute API untuk memeriksa keberadaan super user. ID-nya tidak pernah dikirim melalui API dan frontend dan hanya menerima bool (ya/tidak) jika Anda pengguna super atau bukan.

Hanya pengguna super yang diizinkan untuk melakukan brrrr satoshi ke dompet yang berbeda melalui bagian "Top Up".

Anda juga dapat memposting pengguna super melalui webhook ke layanan lain ketika dibuat. Info lebih lanjut di sini https://github.com/lnbits/lnbits/blob/main/lnbits/settings.py `class SaaSSettings`

Di bagian depan, Anda juga akan menemukan kemungkinan untuk mengubah gambar toko yang ditampilkan pada halaman "buat dompet" dengan membuka bagian Kelola Server dan memilih Tema -> Logo Kustom.

### Pengguna Admin

Variabel lingkungan: `LNBITS_ADMIN_USERS`, daftar ID pengguna yang dipisahkan dengan tanda koma. Pengguna Admin dapat mengubah pengaturan di ui admin - dengan pengecualian pengaturan sumber pendanaan, karena hal ini akan membutuhkan restart server dan berpotensi membuat server tidak dapat diakses. Mereka juga memiliki akses ke semua ekstensi yang didedikasikan untuk mereka di `LNBITS_ADMIN_EXTENSIONS`.

### Pengguna yang Diizinkan

Variabel lingkungan: `LNBITS_ALLOWED_USERS`, daftar ID pengguna yang dipisahkan dengan tanda koma. Dengan mendefinisikan pengguna ini, LNbits tidak lagi dapat digunakan oleh publik. Hanya pengguna dan admin yang telah ditentukan yang dapat mengakses frontend LNbits.

#### Perbarui LNbits

Pembaruan normal dari instance lokal LNbits Anda cukup dengan menyalin dan menempelkan perintah CLI berikut ini:

```
cd lnbits
## Stop LNbits with `ctrl + x`
git pull
## Keep your poetry install up to date, this can be done with
poetry self update
poetry install --only main
## or
git checkout main && git pull && poetry install
## Start LNbits with
poetry run lnbits
```

Jika Anda menjalankan Raspiblitz atau MyNode, Anda mungkin juga membutuhkan

```
sudo systemctl restart lnbits
```

di bagian akhir, karena menjalankan LNbits sebagai layanan.

Pada Umbrel/Citadel, perintahnya adalah

```
cd ~/apps/lnbits
git pull upstream main
sudo ~/scripts/app start lnbits
```

#### Migrasi SQLite ke PostgreSQL

Jika Anda telah memiliki LNbits yang terinstal dan berjalan di database SQLite, kami sangat menyarankan untuk bermigrasi ke postgres jika Anda berencana menjalankan LNbits dalam skala besar.

Ada sebuah skrip yang disertakan untuk melakukan migrasi dengan mudah. Anda harus memiliki Postgres yang sudah terinstal dan harus ada kata sandi untuk pengguna (lihat panduan instalasi Postgres di atas). Selain itu, instance LNbits Anda harus dijalankan sekali pada Postgres untuk mengimplementasikan skema basis data sebelum migrasi dapat berjalan:

```
# STOP LNbits
# add the database connection string to .env 'nano .env' LNBITS_DATABASE_URL=
# postgres://<user>:<password>@<host>/<database> - alter line bellow with your user, password and db name
LNBITS_DATABASE_URL="postgres://postgres:postgres@localhost/lnbits"
# save and exit
# START LNbits
# STOP LNbits
poetry run python tools/conv.py
# or
make migration
```

Semoga sekarang semuanya sudah berfungsi dan dimigrasi... Luncurkan LNbits lagi dan periksa apakah semuanya berfungsi dengan baik.

#### Pencadangan dan pemulihan basis data

Silakan lihat [panduan yang sangat rinci tentang proses pencadangan & pemulihan] (https://ereignishorizont.xyz/lnbits-server/en/#94_LNbits_-_Databases_Backup_Restore).

#### Mendanai dompet LNbits saya dari node saya tidak berfungsi

Jika Anda ingin mengirim sats dari node yang sama dengan sumber pendanaan LNbits Anda, Anda perlu mengedit file lnd.conf.

Parameter yang harus disertakan adalah: `allow-circular-route=1`

Silakan lakukan di bagian Opsi aplikasi pada lnd.conf Anda. Pada beberapa simpul bundel, permulaan LND dapat gagal.

CATATAN: Disarankan untuk menggunakan ekstensi adminUI baru dengan opsi "TopUp" untuk menambahkan dana ke akun LNbits.

#### Kesalahan 426

Saya mendapatkan kesalahan: "lnurl harus dikirim melalui domain https atau tor yang dapat diakses publik. diperlukan peningkatan 426" </ ringkasan>

Kesalahan ini biasanya disebabkan karena LNbits Anda yang berada di belakang terowongan ngnix tidak meneruskan alamat LNURL dengan benar. Hentikan LNbits Anda dan edit berkas .env dengan menambahkan baris ini:

`FORWARDED_ALLOW_IPS=*`

Juga jika Anda menggunakan pengaturan ngnix, pastikan Anda memiliki header ini dalam konfigurasi ngnix:

```
RequestHeader set "X-Forwarded-Proto" expr=%{REQUEST_SCHEME}
RequestHeader set "X-Forwarded-SSL" expr=%{HTTPS}
```

#### Kesalahan Jaringan

Saya mendapat "kesalahan https", kesalahan jaringan" atau lainnya saat memindai QR< /ringkasan

Kabar buruknya, ini adalah kesalahan perutean yang mungkin memiliki banyak alasan. Pertama-tama, periksa LNURL QR dengan [Lightning Decoder] (https://lightningdecoder.com/) jika Anda menemukan sesuatu yang aneh di sana. Mari kita coba beberapa masalah yang paling mungkin terjadi dan solusinya.

LNbits hanya berjalan melalui Tor, Anda tidak dapat membukanya di domain publik seperti lnbits.yourdomain.com


- Karena Anda ingin pengaturan Anda tetap seperti ini, buka dompet LNbits Anda menggunakan URI .onion dan buat lagi. Dengan cara ini, QR dibuat agar dapat diakses melalui URI .onion ini, jadi hanya melalui tor. Jangan membuat QR tersebut dari URI .local, karena QR tersebut tidak akan dapat diakses melalui internet - hanya dari dalam LAN rumah Anda.
- Buka aplikasi dompet LN yang Anda gunakan untuk memindai QR tersebut dan kali ini dengan menggunakan tor (lihat pengaturan aplikasi dompet). Jika aplikasi tidak menawarkan tor, Anda bisa menggunakan Orbot (Android) sebagai gantinya. Lihat bagian instalasi untuk petunjuk terperinci tentang cara membuka LNbits Anda untuk clearnet/https.

#### Mencegah orang lain membuat dompet di LNbits saya

Ketika Anda menjalankan LNbits Anda di clearnet, pada dasarnya semua orang dapat membuat dompet di dalamnya. Karena dana dari node Anda terikat pada dompet ini, Anda mungkin ingin mencegahnya. Ada dua cara untuk melakukannya:

Konfigurasikan pengguna dan ekstensi yang diizinkan dalam berkas `.env` ([lihat contoh env di sini](https://github.com/lnbits/lnbits/blob/main/.env.example)). Ini hanya berfungsi jika Anda menggunakan pengaturan `adminUI=FALSE` pada .env, jika tidak, Anda harus melakukannya pada bagian Kelola Server -> Pengguna -> Pengguna yang Diizinkan. Semua orang tidak akan diizinkan setelah itu.

#### Sesuaikan jangka waktu kedaluwarsa faktur

Sekarang Anda dapat membuat faktur dengan masa berlaku khusus. Kompatibel dengan backend: LndRestWallet, LndWallet, CoreLightningWallet, EclairWallet, LnbitsWallet, SparkWallet sejauh ini!

Anda dapat mengatur `LIGHTNING_INVOICE_EXPIRY` di file .env Anda atau menggunakan AdminUI untuk mengubah nilai default untuk semua faktur. Ada juga bidang baru di titik akhir /api/v1/payments di mana Anda dapat mengatur masa berlaku dalam data JSON.

## Dompet-URL dihapus

### Dompet di server demo legend.lnbits

Selalu simpan salinan wallet-URL, Export2phone-QR atau LNDhub Anda di tempat yang aman. LNbits TIDAK dapat membantu Anda untuk memulihkannya ketika hilang.

### Dompet pada sumber/simpul pendanaan Anda sendiri

Selalu simpan salinan wallet-URL, Export2phone-QR atau LNDhub Anda di tempat yang aman. Anda dapat menemukan semua pengguna LNbits dan wallet-ID di ekstensi pengelola pengguna LNbits Anda atau di database sqlite Anda. Untuk mengedit atau membaca database LNbits, masuk ke folder LNbits /data dan cari file bernama sqlite.db. Anda dapat membuka dan mengeditnya dengan excel atau dengan SQL-Editor khusus seperti [SQLite browser] (https://sqlitebrowser.org/).

Anda juga dapat membuang dompet melalui cli dan melihat setiap dompet di dalam basis data Anda.

```
cd ~/app-data/lnbits/data
sqlite3 database.sqlite3
.dump wallets
```

Output akan terlihat seperti ini

```
INSERT INTO wallets VALUES('f8a43fc363ea428db5c53b3559935f1f','NAME OF WALLET','1280ff5910a9c485a782a2376f338b6c','33b95b099ce848e3b484124373f681e5','2cca208ae6d94d438227b9487ff216f9');
```

dan Anda ingin memasukkan nilai-nilai ini ke dalam url seperti ini

```
https://your.lnbits.com/wallet?usr=1280ff5910a9c485a782a2376f338b6c&wal=f8a43fc363ea428db5c53b3559935f1f
```

Di mana Anda mengganti f8a43fc363ea428db5c53b3559935f1f dengan nilai yang muncul sebelum nama (dalam contoh kita f8a43fc363ea428db5c53b3559935f1f) dan 1280ff5910a9c485a782a2376f338b6c adalah pengguna Anda dan harus menjadi nilai yang ditampilkan setelah nama. Untuk keluar dari sqlite3, masukkan

```
.quit
```

#### LNURL untuk alamat kilat dan sebaliknya

Cobalah [encoder](https://lnurl-codec.netlify.app/) dari fiatjaf atau [yang ini](https://lightningdecoder.com/). Untuk membayar atau memeriksa LNURLp, Anda juga dapat menggunakan [LNurlpay](https://wwww.lnurlpay.com/). Ini harus menyatakan HTTPS BUKAN HTTP.

#### Mengonfigurasi komentar yang dilihat orang saat membayar ke QR LNURLp saya

Ketika Anda membuat LNURL-p, secara default kotak komentar tidak diisi. Ini berarti komentar tidak diizinkan untuk dilampirkan ke pembayaran.

Untuk mengizinkan komentar, tambahkan panjang karakter pada kotak, dari 1 hingga 250. Setelah Anda memasukkan nomor di sana, kotak komentar akan ditampilkan dalam proses pembayaran. Anda juga dapat mengedit LNURL-p yang sudah dibuat dan menambahkan nomor tersebut.

![lnbits comments](assets/lnbits-comments.webp)

#### Menyetor onchain BTC ke LNbits

Ada dua cara untuk menukar satoshi dari onchain BTC ke LN BTC (resp. ke LNbits).

##### Melalui layanan swap eksternal.

Pengguna lain yang tidak memiliki akses ke LNbits Anda dapat menggunakan layanan swap seperti [Boltz] (https://boltz.exchange/), [FixedFloat] (https://fixedfloat.com/), [DiamondHands] (https://swap.diamondhands.technology/), atau [ZigZag] (https://zigzag.io/). Ini berguna jika Anda hanya menyediakan faktur LNURL/LN dari instance LNbits Anda, tetapi pembayar hanya memiliki satelite sehingga mereka harus menukar satelite tersebut terlebih dahulu di sisi mereka. Prosedurnya sederhana: pengguna mengirimkan btc onchain ke layanan swap dan memberikan faktur LNURL/LN dari LNbits sebagai tujuan swap.

##### Menggunakan ekstensi Onchain dan Boltz LNbits.

Perlu diingat bahwa ini adalah dompet terpisah, bukan dompet LN btc yang diwakili oleh LNbits sebagai "dompet Anda" pada sumber pendanaan LN Anda. Dompet onchain ini juga dapat digunakan untuk menukar LN btc ke (mis. Dompet perangkat keras Anda) dengan menggunakan ekstensi LNbits Boltz atau Deezy. Jika Anda menjalankan toko web yang terhubung ke LNbits Anda untuk pembayaran LN, akan sangat berguna untuk mengalirkan semua sat dari LN ke onchain secara teratur. Hal ini akan memberikan lebih banyak ruang di saluran LN Anda untuk dapat menerima sat yang baru.

Prosedur untuk mereka yang tidak memiliki dompet perangkat keras bitcoin:


- Gunakan Electrum atau dompet Sparrow untuk membuat dompet onchain baru dan simpan seed cadangan di tempat yang aman.
- Buka informasi dompet dan salin xpub.
- Buka LNbits - Ekstensi Onchain dan buat dompet khusus jam tangan baru dengan xpub tersebut.
- Buka LNbits - ekstensi Tipjar dan buat Tipjar baru. Pilih juga opsi onchain di samping dompet LN.
- Opsional - Buka LNbits - ekstensi SatsPay dan buat biaya baru untuk onchain btc. Anda dapat memilih antara onchain dan LN atau keduanya. Ini kemudian akan membuat faktur yang dapat dibagikan.
- Opsional - Jika Anda menggunakan LNbits yang ditautkan ke halaman Wordpress + Woocommerce, setelah Anda membuat/menautkan dompet khusus jam tangan ke dompet LN btc shop Anda, pelanggan akan memiliki kedua opsi untuk membayar di layar yang sama.

Ketika Anda menerima pembayaran di LNbits, log transaksi hanya akan menampilkan jenis transaksi yang dilanjutkan.

![lnbits payment details](assets/lnbits-payment-details.webp)

Dalam ikhtisar transaksi Anda, Anda akan menemukan panah hijau kecil untuk dana yang diterima dan panah merah untuk dana yang dikirim.

Jika Anda mengeklik tanda panah tersebut, popup detail akan menampilkan pesan terlampir serta nama pengirim jika ada.

Untuk mengonfigurasi nama yang akan muncul dalam pembayaran, di LNbits saat ini hal tersebut tidak dapat dilakukan - kecuali untuk menerima. Hal ini hanya dapat dilakukan jika dompet LN pengirim mendukung [LUD-18] (https://github.com/lnurl/luds/blob/luds/18.md) (nameDesc) seperti [OBW, Blixt, Alby, ZBD, BitBanana] (https://github.com/lnurl/luds?tab=readme-ov-file#lnurl-documents).

Anda akan melihat nama alias/nama samaran di bagian detail transaksi LNbits Anda (klik tanda panah). Perhatikan bahwa Anda dapat memberikan nama apa pun di sana dan nama tersebut mungkin tidak terkait dengan nama pengirim sebenarnya jika Anda menerimanya.

![lnbits namedesc](assets/lnbits-namedesc.webp)

Untuk mengimpor akun LNbits Anda di aplikasi dompet, buka LNbits Anda dengan akun/dompet yang ingin Anda gunakan, buka "kelola ekstensi" dan aktifkan ekstensi LNDHUB. Buka ekstensi LNDHUB, pilih dompet yang ingin Anda gunakan dan pindai QR "admin" atau "hanya faktur", tergantung pada tingkat keamanan yang Anda inginkan untuk dompet tersebut.

Anda dapat menggunakan [Zeus] (https://zeusln.app/) atau [Bluewallet] (https://bluewallet.io/) sebagai aplikasi dompet untuk akun lndhub di mana BW mendukung lebih dari satu dompet.

Ketika melakukan ini, kami merekomendasikan untuk mengatur URI jaringan LN ke salah satu simpul Anda sendiri. Jika instance LNbits Anda hanya menggunakan Tor, Anda juga harus menggunakan aplikasi yang sama dengan Tor yang diaktifkan. Juga dalam hal ini Anda harus membuka halaman LNbits melalui alamat Tor .onion Anda.

Jika Anda mengalami kesalahan "tipe hash tidak didukung" saat menggunakan ypub dalam ekstensi On-chain, periksa apakah instance LNbits Anda menggunakan python 3.10 yang mungkin terpengaruh oleh [masalah ini] (https://stackoverflow.com/questions/72409563/unsupported-hash-type-ripemd160-with-hashlib-in-python). Edit openssl.cnf seperti yang dijelaskan di jawaban stackoverflow dan mulai ulang LNbits Anda.

## Perkakas & Bangunan dengan LNbits

LNbits memiliki berbagai macam [API terbuka] (https://legend.lnbits.com/docs) dan alat untuk memprogram dan terhubung ke banyak perangkat yang berbeda untuk bermilyar-milyar kasus penggunaan.

Jika Anda baru dalam membangun, mulailah dengan [presentasi MakerBits] (https://www.youtube.com/channel/UCZhKfzK6_KWZ-CFC2wXQVBw/videos) dari Ben Arc tentang membangun gadget berdasarkan LNbits.

### PENTING:


- LNbits bekerja berdasarkan protokol LNURL yang permintaannya dapat dilakukan dalam dua bentuk: baik sebagai tautan https:// clearnet (tidak ada sertifikat yang ditandatangani sendiri) atau sebagai tautan http:// v2/v3 onion. Untuk menawarkan layanan LNbits seperti kode QR LNURLp/w atau Kartu NFC, yang dapat digunakan di alam bebas, Anda harus membuka LNbits ke clearnet (https).
- Hanya gunakan kabel DATA untuk menyalakan esp32 Anda. Tidak semua kabel mendukung data selain untuk menyalakan esp. Anda tidak akan menjadi yang pertama jika kabel yang disertakan dengan esp adalah kabel khusus daya
- Pastikan untuk tidak menggunakan USB-Hub dengan perangkat lain yang terpasang. Hal ini dapat menyebabkan efek aneh yang sulit di-debug (misalnya, tidak dapat memulai atau berhenti).
- Untuk merealisasikan proyek-proyek khusus dengan MacOS, Anda akan membutuhkan Driver Jembatan UART. Jika Anda memiliki masalah dengan driver pada sistem Mac atau Linux, Anda dapat menemukannya di sini atau, jika TTGO Display terlibat, Anda dapat menemukannya di sini. Jika Anda menggunakan Windows dan mengalami masalah koneksi, pastikan untuk mengunduh versi LAMA 11.1.0 karena versi yang lebih baru tidak berfungsi! Anda juga dapat menemukan terminal serial di sini untuk memeriksa koneksi Anda - atur ke baudrate 115200.
- Meskipun jauh lebih nyaman untuk menggunakan Platform.io (misalnya dependensi diinstal secara otomatis), kami merekomendasikan penggunaan Arduino untuk semua orang yang baru dalam membangun.
- TT-Go Display S3: Warna tab pada film pelindung layar memberi tahu Anda pengontrol mana yang tepat (ST7735_redtab, ST7735_blacktag, ST7735_greetab, greentab128,..) yang digunakan untuk membuatnya. Simpanlah agar dapat melakukan debug jika Anda memprogram sendiri dan layar tidak menampilkan grafik dengan benar, misalnya warna yang salah, gambar yang dicerminkan, atau piksel yang tersesat di bagian tepi. Jika Anda perlu melakukan hal ini, ada panduan yang sangat bagus untuk menyesuaikan tampilan yang berbeda
- Selalu gunakan huruf kecil lnurl239xx, bukan LNURLl239xx
- Menambahkan lightning:lnurl1234xyz akan membuat QR yang meminta untuk membuka dompet pengguna untuk faktur ini saat pemindaian (aplikasi lightning yang terakhir diinstal di iOS, pengaturan di Android)
- Jika Anda mem-flash esp32 melalui web, maka hanya akan bekerja dengan browser-browser ini (TL: DR Chrome, Edge & Opera).
- Harap perhatikan referensi PIN-KELUAR ini untuk esp
- Ketika Anda menggunakan FOSSoftware atau FOSGuides, mohon untuk selalu menautkan penulisnya. Semua orang suka melihat bayi mereka tumbuh dan ini juga memulai sebuah rantai pembangunan yang cukup mengagumkan untuk dilihat :)

Datanglah ke [Grup Telegram Makerbits](https://t.me/makerbits) jika Anda membutuhkan bantuan untuk sebuah proyek - kami siap membantu Anda!

![lnbits hackathlon](assets/lnbits-hackathlon.webp)

Berikut adalah beberapa kategori proyek yang dapat Anda buat dengan LNbits:


- [Perangkat Penandatanganan Nostr](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#nostr-signing-device)
- [Mesin Archade](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#arcade-machine)
- [Gerty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#gerty)
- [Nostr Zap Lamp](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#zap-lamp)
- [ATM BTC/LN](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#atm)
- [LNPoS](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lnpos-terminal)
- [Lightning Piggy] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lightning-piggy)
- [Dompet Perangkat Keras](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#hardware-wallet)
- [Bitcoin Switch](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bitcoin-switch)
- [Mesin penjual otomatis](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#vending-machine)
- [Bolty] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bolty)
- [Nerdminer](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Nerdminer)
- [Bitcoin Ticker](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bitcoin-ticker)
- [BTClock](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#btclock)
- [Lora dan Jaringan Mesh](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lora)
- [PEMBANTU & SUMBER DAYA](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#resources)
- [Contoh lain dari proyek "Didukung oleh LNbits" di sini] (https://github.com/lnbits/lnbits/wiki/Powered-by-LNbits).
- [Kasus penggunaan untuk LNbits](https://github.com/lnbits/lnbits/wiki/Use-Cases-of-LNbits)