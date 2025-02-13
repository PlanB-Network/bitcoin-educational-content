---
name: Simpul Petir RGB
description: Bagaimana cara meluncurkan node Lightning yang kompatibel dengan RGB dengan RLN?
---
![cover](assets/cover.webp)

Dalam tutorial langkah demi langkah ini, Anda akan mempelajari cara menyiapkan node Lightning RGB di lingkungan Regtest. Kita akan melihat cara membuat token RGB dan mengedarkannya di saluran.

## Proyek RLN

Tim RGB Bitfinex telah bekerja sejak tahun 2022 untuk memperkaya ekosistem RGB dengan mengembangkan rangkaian teknologi yang lengkap. Alih-alih bertujuan untuk satu produk komersial, upayanya difokuskan untuk menyediakan batu bata perangkat lunak sumber terbuka, berkontribusi pada spesifikasi protokol RGB, dan membuat referensi implementasi.

Di antara kontribusi penting Bitfinex terhadap ekosistem RGB adalah [pustaka *RGBlib*] (https://github.com/RGB-Tools/rgb-lib), yang ditulis dalam bahasa Rust dan dapat diakses melalui binding di Kotlin dan Python, yang sangat menyederhanakan pengembangan aplikasi RGB dengan mengenkapsulasi mekanisme validasi dan keterlibatan yang kompleks.

Tim Bitfinex juga telah merancang dompet seluler RGB, yang disebut "[*Iris Wallet*](https://iriswallet.com/)", tersedia di Android. Dompet ini mengintegrasikan penggunaan server proxy RGB untuk dengan mudah mengelola pertukaran data off-chain (*kiriman*) untuk *Validasi Sisi Klien* pada RGB.

Bitfinex juga telah mengembangkan proyek `rgb-lightning-node` (RLN). Ini adalah daemon Rust yang didasarkan pada fork dari `rust-lightning` (LDK), yang dimodifikasi untuk memperhitungkan keberadaan aset RGB dalam sebuah saluran. Ketika saluran dibuka, keberadaan token RGB dapat ditentukan, dan setiap kali status saluran diperbarui, transisi status dibuat yang mencerminkan distribusi token dalam output Lightning. Hal ini memungkinkan :


- Buka saluran Lightning dalam USDT, misalnya;
- Rutekan token-token ini melalui jaringan, asalkan jalur perutean memiliki likuiditas yang cukup;
- Manfaatkan hukuman Lightning dan logika timelock tanpa modifikasi: cukup jangkarkan transisi RGB dalam output tambahan dari transaksi komitmen.

Kode RLN masih dalam tahap alfa: kami sarankan untuk menggunakannya di **regtest** atau di **testnet** saja.

## Pengingat protokol RGB

RGB adalah sebuah protokol yang berjalan di atas Bitcoin dan meniru fungsionalitas smart contract dan manajemen aset digital, tanpa membebani blockchain yang menjadi basisnya. Tidak seperti smart contract on-chain konvensional (seperti pada Ethereum, misalnya), RGB bergantung pada sistem "*Validasi sisi klien*": sebagian besar data dan riwayat status dipertukarkan dan disimpan secara eksklusif oleh para partisipan yang terlibat, sedangkan blockchain Bitcoin hanya menyimpan komitmen kriptografi kecil (melalui mekanisme seperti *Tapret* atau *Opret*). Dalam protokol RGB, blockchain Bitcoin hanya berfungsi sebagai server pencatat waktu dan sistem proteksi pembelanjaan ganda.

Kontrak RGB terstruktur seperti mesin status evolusioner. Dimulai dengan Genesis yang mendefinisikan keadaan awal (menggambarkan, misalnya, pasokan, ticker, atau metadata lainnya) menurut Skema yang diketik dan dikompilasi secara ketat. State Transitions dan, jika perlu, State Extensions kemudian diterapkan untuk memodifikasi atau memperluas state ini. Setiap operasi, baik mentransfer aset yang dapat dipertukarkan (RGB20) atau membuat aset unik (RGB21), melibatkan *Segel Sekali Pakai*. Segel ini menghubungkan UTXO Bitcoin ke state off-chain dan mencegah pengeluaran ganda, sekaligus memastikan kerahasiaan dan skalabilitas.

Untuk mempelajari lebih lanjut mengenai cara kerja protokol RGB, saya sarankan Anda mengikuti kursus pelatihan komprehensif ini:

https://planb.network/courses/csv402
## Pemasangan simpul Lightning yang kompatibel dengan RGB

Untuk mengkompilasi dan menginstal biner `rgb-lightning-node`, kita mulai dengan mengkloning repositori dan sub-modulnya, lalu kita jalankan berkas :

```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```

![RLN](assets/fr/01.webp)


- Opsi `--recurse-submodules` juga mengkloning sub-perangkat yang diperlukan (termasuk versi modifikasi dari `rust-lightning`);
- Opsi `--shallow-submodules` membatasi kedalaman klon untuk mempercepat pengunduhan, sambil tetap menyediakan akses ke komit yang penting.

Dari root proyek, jalankan perintah berikut untuk mengkompilasi dan menginstal biner :

```bash
cargo install --locked --debug --path .
```

![RLN](assets/fr/02.webp)


- `--locked` memastikan bahwa versi dependensi dihormati;
- `--debug` tidak wajib, tetapi dapat membantu Anda fokus (Anda dapat menggunakan `--release` jika Anda mau);
- `--path .` memberitahu `cargo install` untuk menginstal dari direktori saat ini.

Pada akhir perintah ini, sebuah eksekusi `rgb-lightning-node` akan tersedia pada `$CARGO_HOME/bin/`. Pastikan jalur ini ada di `$PATH` Anda sehingga Anda dapat memanggil perintah dari direktori mana pun.

## Prasyarat

Agar dapat berfungsi, daemon `rgb-lightning-node` membutuhkan kehadiran dan konfigurasi :


- Sebuah simpul `bitcoind`**

Setiap instance RLN perlu berkomunikasi dengan `bitcoind` untuk menyiarkan dan memonitor transaksi on-chain. Otentikasi (login/kata sandi) dan URL (host/port) harus disediakan untuk daemon.


- Pengindeks** (Electrum atau Esplora)

Daemon harus dapat membuat daftar dan menjelajahi transaksi on-chain, khususnya untuk menemukan UTXO tempat sebuah aset ditambatkan. Anda harus menentukan URL server Electrum atau Esplora Anda.


- Proksi RGB**

Server proxy adalah komponen (opsional, tetapi sangat disarankan) untuk menyederhanakan pertukaran *kiriman* RGB antara rekan-rekan Lightning. Sekali lagi, URL harus ditentukan.

ID dan URL dimasukkan ketika daemon *dibuka* melalui API.

## Peluncuran pengujian ulang

Untuk penggunaan sederhana, ada skrip `regtest.sh` yang secara otomatis memulai, melalui Docker, serangkaian layanan: `bitcoind`, `electrs` (pengindeks), `rgb-proxy-server`.

![RLN](assets/fr/03.webp)

Hal ini memungkinkan Anda untuk meluncurkan lingkungan lokal, terisolasi, dan telah dikonfigurasi sebelumnya. Ini membuat dan menghancurkan kontainer dan direktori data pada setiap reboot. Kita akan mulai dengan memulai file :

```bash
./regtest.sh start
```

Skrip ini akan :


- Buat direktori `docker/` untuk menyimpan file ;
- Jalankan `bitcoind` di regtest, serta pengindeks `electrs` dan `rgb-proxy-server`;
- Tunggu sampai semuanya siap digunakan.

![RLN](assets/fr/04.webp)

Selanjutnya, kita akan meluncurkan beberapa node RLN. Pada shell terpisah, jalankan, misalnya (untuk meluncurkan 3 node RLN) :

```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```

![RLN](assets/fr/05.webp)


- Parameter `--network regtest` mengindikasikan penggunaan konfigurasi regtest;
- `--daemon-listening-port` mengindikasikan pada port REST mana node Lightning akan mendengarkan panggilan API (JSON);
- `--ldk-peer-listening-port` menentukan port p2p Lightning mana yang akan didengarkan;
- `dataldk0/`, `dataldk1/` adalah jalur ke direktori penyimpanan (setiap simpul menyimpan informasinya secara terpisah).

Anda sekarang dapat menjalankan perintah pada node RLN Anda dari peramban, berkat API. Secara khusus, di sinilah Anda dapat membuka kunci daemon. Cukup buka peramban di komputer yang sama dengan node Anda, dan masukkan URL :

```url
https://rgb-tools.github.io/rgb-lightning-node/
```

Agar sebuah node dapat membuka sebuah saluran, node tersebut harus memiliki bitcoin pada alamat yang dibuat dengan perintah berikut (untuk node n°1, misalnya):

```bash
curl -X POST http://localhost:3001/address
```

Jawabannya akan memberi Anda sebuah alamat.

![RLN](assets/fr/06.webp)

Pada Regtest `bitcoind`, kita akan menambang beberapa bitcoin. Jalankan:

```bash
./regtest.sh mine 101
```

![RLN](assets/fr/07.webp)

Kirim dana ke alamat node yang dibuat di atas:

```bash
./regtest.sh sendtoaddress <address> <amount>
```

![RLN](assets/fr/08.webp)

Kemudian lakukan penambangan blok untuk mengonfirmasi transaksi:

```bash
./regtest.sh mine 1
```

![RLN](assets/fr/09.webp)

## Peluncuran Testnet (tanpa Docker)

Jika Anda ingin menguji skenario yang lebih realistis, Anda dapat meluncurkan node RLN di Testnet daripada di Regtest, yang mengarah ke layanan publik, atau layanan yang Anda kendalikan:

```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```

Secara default, jika tidak ada konfigurasi yang ditemukan, daemon akan mencoba menggunakan ekstensi :


- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332`
- indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-rpc`

Dengan login :


- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `kata sandi`

Anda juga dapat menyesuaikan elemen-elemen ini melalui API `init`/`unlock`.

## Menerbitkan token RGB

Untuk menerbitkan token, kita akan mulai dengan membuat UTXO yang "dapat diwarnai":

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```

![RLN](assets/fr/10.webp)

Anda tentu saja dapat menyesuaikan pesanan. Untuk mengonfirmasi transaksi, kami menambang file :

```bash
./regtest.sh mine 1
```

Sekarang kita dapat membuat aset RGB. Perintahnya akan bergantung pada jenis aset yang ingin Anda buat dan parameternya. Di sini saya membuat token NIA (*Non Inflatable Asset*) bernama "PBN" dengan persediaan 1000 unit. `Presision` memungkinkan Anda untuk menentukan pembagian unit.

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "PBN",
"name": "Plan B Network",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```

![RLN](assets/fr/11.webp)

Tanggapannya mencakup ID aset yang baru dibuat. Ingatlah untuk mencatat pengenal ini. Dalam kasus saya, ini adalah :

```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```

![RLN](assets/fr/12.webp)

Anda kemudian dapat mentransfernya secara on-chain, atau mengalokasikannya dalam saluran Lightning. Itulah yang akan kita lakukan di bagian selanjutnya.

## Membuka saluran dan mentransfer aset RGB

Anda harus terlebih dahulu menyambungkan node Anda ke peer di jaringan Lightning menggunakan perintah `/connectpeer`. Dalam contoh saya, saya mengendalikan kedua node. Jadi, saya akan mengambil kunci publik dari node Lightning kedua dengan perintah ini:

```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```

Perintah ini mengembalikan kunci publik dari simpul saya n°2:

```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```

![RLN](assets/fr/13.webp)

Selanjutnya, kita akan membuka channel dengan menentukan aset yang relevan (`PBN`). Perintah `/openchannel` memungkinkan Anda menentukan ukuran saluran di satoshi dan memilih untuk menyertakan aset RGB. Tergantung pada apa yang ingin Anda buat, tetapi dalam kasus saya, perintahnya adalah :

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```

Cari tahu lebih lanjut di sini:


- `peer_pubkey_and_opt_addr`: Pengidentifikasi peer yang ingin kita sambungkan (kunci publik yang kita temukan sebelumnya);
- `kapasitas_sat`: Total kapasitas saluran dalam satoshi;
- `push_msat`: Jumlah dalam milisatos yang awalnya ditransfer ke peer ketika saluran dibuka (di sini saya langsung mentransfer 10.000 sat supaya dia bisa melakukan transfer RGB nanti);
- `jumlah_aset`: Jumlah aset RGB yang akan dikomitmenkan ke saluran;
- `asset_id`: Pengidentifikasi unik dari aset RGB yang terlibat dalam saluran;
- `public`: Menunjukkan apakah saluran harus dibuat publik untuk perutean di jaringan.

![RLN](assets/fr/14.webp)

Untuk mengonfirmasi transaksi, 6 blok ditambang:

```bash
./regtest.sh mine 6
```

![RLN](assets/fr/15.webp)

Saluran Lightning sekarang terbuka dan juga berisi 500 token `PBN` di sisi node n°1. Jika node n°2 ingin menerima token `PBN`, ia harus membuat faktur. Berikut cara melakukannya:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```

Dengan:


- `amt_msat`: Jumlah faktur dalam milisatoshi (minimal 3000 sat);
- `expiry_sec`: Waktu kedaluwarsa faktur dalam hitungan detik;
- `asset_id`: Pengidentifikasi aset RGB yang terkait dengan faktur;
- `jumlah_aset`: Jumlah aset RGB yang akan ditransfer dengan faktur ini.

Sebagai tanggapan, Anda akan mendapatkan faktur RGB:

```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```

![RLN](assets/fr/16.webp)

Sekarang kita akan membayar faktur ini dari node pertama, yang menyimpan uang tunai yang diperlukan dengan token `PBN`:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```

![RLN](assets/fr/17.webp)

Pembayaran telah dilakukan. Hal ini dapat diverifikasi dengan menjalankan perintah :

```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```

![RLN](assets/fr/18.webp)

Berikut ini adalah cara menggunakan simpul Lightning yang dimodifikasi untuk membawa aset RGB. Demonstrasi ini didasarkan pada :


- Lingkungan regtest (melalui `./regtest.sh`) atau testnet ;
- Simpul Lightning (`rgb-lightning-node`) yang didasarkan pada `bitcoind`, sebuah pengindeks dan `rgb-proxy-server`;
- Serangkaian API REST JSON untuk membuka/menutup saluran, menerbitkan token, mentransfer aset melalui Lightning, dll.

Berkat proses ini :


- Transaksi keterlibatan petir mencakup output tambahan (OP_RETURN atau Taproot) dengan penahan transisi RGB;
- Transfer dilakukan dengan cara yang persis sama dengan pembayaran Lightning tradisional, tetapi dengan tambahan token RGB;
- Beberapa node RLN dapat dihubungkan ke rute dan bereksperimen dengan pembayaran di beberapa node, asalkan ada likuiditas yang cukup dalam bitcoin dan RGB aset di jalur tersebut.

Jika Anda merasa tutorial ini bermanfaat, saya akan sangat berterima kasih jika Anda memberikan jempol hijau di bawah ini. Jangan ragu untuk membagikan artikel ini di jejaring sosial Anda. Terima kasih banyak!

Saya juga merekomendasikan tutorial lain yang menjelaskan cara menggunakan alat bantu RGB CLI yang dikembangkan oleh asosiasi LNP/BP untuk membuat kontrak RGB:

https://planb.network/tutorials/node/rgb/rgb-cli-1f8a28d4-fa99-4261-9d80-48275b496fd4