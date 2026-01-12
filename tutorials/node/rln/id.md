---
name: RGB Lightning Node
description: Bagaimana cara meluncurkan node Lightning yang kompatibel dengan RGB dengan RLN?
---
![cover](assets/cover.webp)

Dalam tutorial langkah demi langkah ini, kamu bakal belajar cara nyiapin node Lightning RGB di lingkungan Regtest. Kita juga bakal lihat cara bikin token RGB dan mengedarkannya di channel.

## Proyek RLN

Tim RGB Bitfinex udah bekerja sejak 2022 buat memperkaya ekosistem RGB dengan ngembangin rangkaian teknologi yang lengkap. Alih-alih ngejar satu produk komersial, fokusnya ada di penyediaan software building blocks open-source, kontribusi ke spesifikasi protokol RGB, dan bikin implementasi referensi.

Di antara kontribusi penting Bitfinex terhadap ekosistem RGB adalah [pustaka *RGBlib*](https://github.com/RGB-Tools/rgb-lib), yang ditulis dalam bahasa Rust dan dapat diakses melalui binding di Kotlin dan Python, yang sangat menyederhanakan pengembangan aplikasi RGB dengan mengenkapsulasi mekanisme validasi dan keterlibatan yang kompleks.

Tim Bitfinex juga telah merancang dompet seluler RGB, yang disebut "[*Iris Wallet*](https://iriswallet.com/)", tersedia di Android. Dompet ini mengintegrasikan penggunaan server proxy RGB untuk dengan mudah mengelola pertukaran data off-chain (*kiriman*) untuk *Validasi Sisi Klien* pada RGB.

Bitfinex juga ngembangin proyek 'rgb-lightning-node' (RLN). Ini adalah daemon Rust yang dibangun dari fork 'rust-lightning' (LDK) yang dimodifikasi supaya bisa ngitung keberadaan aset RGB di dalam sebuah channel. Waktu channel dibuka, kamu bisa nentuin apakah ada token RGB di dalamnya, dan setiap kali status channel diperbarui, bakal dibuat *state transition* yang ngegambarin distribusi token dalam output Lightning. Ini memungkinkan:


- Buka saluran Lightning dalam USDT, misalnya;
- Rutekan token-token ini melalui jaringan, asalkan jalur perutean memiliki likuiditas yang cukup;
- Manfaatkan hukuman Lightning dan logika timelock tanpa modifikasi: cukup jangkarkan transisi RGB dalam output tambahan dari transaksi komitmen.

Kode RLN masih dalam tahap alfa: kami sarankan untuk menggunakannya di **regtest** atau di **testnet** saja.

## Pengingat protokol RGB

RGB adalah protokol yang berjalan di atas Bitcoin dan meniru fungsionalitas smart contract dan manajemen aset digital tanpa ngebebanin blockchain dasarnya. Berbeda dari smart contract on-chain konvensional (kayak di Ethereum, misalnya), RGB bergantung pada sistem *client-side validation:* sebagian besar data dan riwayat status dipertukarkan dan disimpen secara eksklusif sama para partisipan, sementara blockchain Bitcoin cuma nyimpen komitmen kriptografi kecil lewat mekanisme kayak *Tapret* atau *Opret*. Dalam protokol RGB, blockchain Bitcoin cuma berperan sebagai server pencatat waktu dan sistem proteksi dari double-spend.

Kontrak RGB disusun seperti mesin status yang berevolusi. Semuanya dimulai dengan Genesis yang nentuin state awal, misalnya total pasokan, ticker, atau metadata lain, sesuai Skema yang diketik dan dikompilasi dengan ketat. Lalu State Transitions dan, kalau perlu, State Extensions diterapkan buat ngubah atau ngeperluas state ini. Setiap operasi, entah itu nge­transfer aset yang bisa dipertukarkan (RGB20) atau bikin aset unik (RGB21), selalu melibatkan *single-use seals.* Seal ini ngaitin UTXO Bitcoin ke state off-chain dan mencegah double-spend sambil tetap ngejaga privasi dan skalabilitas.

Untuk mempelajari lebih lanjut mengenai cara kerja protokol RGB, saya sarankan Anda mengikuti kursus pelatihan komprehensif ini:

https://planb.academy/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

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

Pada akhir perintah ini, sebuah eksekusi `rgb-lightning-node` akan tersedia pada `$CARGO_HOME/bin/`. Pastikan jalur ini ada di `$PATH` Anda sehingga kamu bisa memanggil perintah dari direktori mana pun.

## Prasyarat

Agar dapat berfungsi, daemon `rgb-lightning-node` membutuhkan kehadiran dan konfigurasi :


- Sebuah simpul `bitcoind`

Setiap instance RLN perlu berkomunikasi dengan `bitcoind` untuk menyiarkan dan memonitor transaksi on-chain. Otentikasi (login/kata sandi) dan URL (host/port) harus disediakan untuk daemon.


- **Pengindeks** (Electrum atau Esplora)

Daemon harus bisa ngelist dan ngejelajahi transaksi on-chain, khususnya buat nemuin UTXO tempat sebuah aset ditambatkan. Kamu perlu nentuin URL server Electrum atau Esplora yang kamu pakai.


- **Proksi RGB**

Server proxy adalah komponen (opsional, tetapi sangat disarankan) untuk menyederhanakan pertukaran *kiriman* RGB antara rekan-rekan Lightning. Sekali lagi, URL harus ditentukan.

ID dan URL dimasukkan ketika daemon *dibuka* melalui API.

## Peluncuran pengujian ulang

Untuk penggunaan sederhana, ada skrip `regtest.sh` yang secara otomatis memulai, melalui Docker, serangkaian layanan: `bitcoind`, `electrs` (pengindeks), `rgb-proxy-server`.

![RLN](assets/fr/03.webp)

Hal ini memungkinkan kamu buat ngejalanin lingkungan lokal yang terisolasi dan sudah dikonfigurasi sebelumnya. Lingkungan ini bakal bikin dan ngehapus kontainer serta direktori data setiap kali direboot. Kita mulai dengan ngejalanin file:

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

Sekarang kamu bisa ngejalanin perintah ke node RLN kamu langsung dari browser berkat API. Di sinilah kamu bisa buka kunci daemon. Cukup buka browser di komputer yang sama dengan node kamu, dan masukkan URL :

```url
https://rgb-tools.github.io/rgb-lightning-node/
```

Agar sebuah node dapat membuka sebuah saluran, node tersebut harus memiliki bitcoin pada alamat yang dibuat dengan perintah berikut (untuk node n°1, misalnya):

```bash
curl -X POST http://localhost:3001/address
```

Nanti akan memberikan kamu sebuah alamat.

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

Kalau kamu mau nguji skenario yang lebih realistis, kamu bisa ngejalanin node RLN di Testnet daripada di Regtest, yang bakal ngarah ke layanan publik, atau layanan yang kamu kendalikan:

```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```

Secara default, kalau nggak ada konfigurasi yang ditemukan, daemon akan mencoba menggunakan ekstensi :


- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332`
- indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-rpc`

Dengan login :


- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `kata sandi`

Kamu juga bisa menyesuaikan elemen-elemen ini melalui API `init`/`unlock`.

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

Tentu saja kamu bisa menyesuaikan pesanan. Untuk mengonfirmasi transaksi, kami menambang file :

```bash
./regtest.sh mine 1
```

Sekarang kita bisa bikin aset RGB. Perintahnya bakal tergantung pada jenis aset yang mau kamu buat dan parameternya. Di sini aku bikin token NIA (Non Inflatable Asset) bernama “Plan ₿ Academy” dengan suplai 1000 unit. 'Precision' memungkinkan kamu nentuin pembagian unit.

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "Plan ₿ Academy",
"name": "Plan ₿ Academy",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```

![RLN](assets/fr/11.webp)

Tanggapannya mencakup ID aset yang baru dibuat. Ingatlah untuk mencatat pengenal ini. Dalam contohku, ini adalah :

```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```

![RLN](assets/fr/12.webp)

Kamu kemudian bisa transfer token itu secara on-chain atau ngalokasikannya ke dalam channel Lightning. Itu yang bakal kita lakuin di bagian selanjutnya.

## Membuka saluran dan mentransfer aset RGB

Kamu harus sambungin node kamu dulu ke peer di jaringan Lightning pakai perintah /connectpeer. Di contohku, aku ngejalanin kedua node. Jadi aku bakal ngambil kunci publik dari node Lightning yang kedua dengan perintah ini:

```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```

Perintah ini mengembalikan kunci publik dari node saya n°2:

```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```

![RLN](assets/fr/13.webp)

Selanjutnya, kita bakal buka channel sambil nentuin aset yang relevan (Plan ₿ Academy). Perintah '/openchannel' memungkinkan kamu nentuin ukuran channel dalam satoshi dan milih buat menyertakan aset RGB. Tergantung apa yang mau kamu buat, tapi di kasusku, perintahnya adalah:

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

Saluran Lightning sekarang terbuka dan juga berisi 500 token `Plan ₿ Academy` di sisi node n°1. Kalau node n°2 ingin menerima token `Plan ₿ Academy`, ia harus membuat faktur. Berikut cara melakukannya:

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

Sebagai tanggapan, kamu bakal mendapatkan faktur RGB:

```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```

![RLN](assets/fr/16.webp)

Sekarang kita akan membayar faktur ini dari node pertama, yang menyimpan uang tunai yang diperlukan dengan token `Plan ₿ Academy`:

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


- Transaksi keterlibatan lightning mencakup output tambahan (OP_RETURN atau Taproot) dengan penahan transisi RGB;
- Transfer dilakukan dengan cara yang persis sama dengan pembayaran Lightning tradisional, tetapi dengan tambahan token RGB;
- Beberapa node RLN dapat dihubungkan ke rute dan bereksperimen dengan pembayaran di beberapa node, asalkan ada likuiditas yang cukup dalam bitcoin dan RGB aset di jalur tersebut.

Kalau kamu merasa tutorial ini bermanfaat, aku akan sangat berterima kasih kalau kamu memberikan jempol hijau di bawah ini. Jangan ragu untuk membagikan artikel ini di jejaring sosial. Terima kasih banyak!

Saya juga merekomendasikan tutorial lain yang menjelaskan cara menggunakan alat bantu RGB CLI yang dikembangkan oleh asosiasi LNP/BP untuk membuat kontrak RGB:

https://planb.academy/tutorials/node/others/rgb-cli-1f8a28d4-fa99-4261-9d80-48275b496fd4
