---
name: Lightning Watchtower
description: Memahami dan menggunakan Watchtower pada simpul Lightning Anda
---
![cover](assets/cover.webp)



## Bagaimana cara kerja Menara Pengawal?



Bagian penting dari ekosistem Lightning Network, _Watchtowers_ memberikan tingkat perlindungan ekstra untuk saluran Lightning pengguna. Peran utama mereka adalah memantau status saluran dan mengintervensi jika salah satu sisi saluran mencoba menipu sisi lainnya.



Bagaimana Watchtower dapat menentukan apakah suatu saluran telah disusupi? Watchtower menerima dari pelanggan (salah satu pihak dalam saluran) informasi yang diperlukan untuk mengidentifikasi dan menangani pelanggaran dengan benar. Informasi ini termasuk rincian transaksi terakhir, status saluran saat ini, dan Elements yang diperlukan untuk membuat transaksi penalti. Sebelum mengirimkan data ini ke Watchtower, pelanggan dapat mengenkripsinya untuk menjaga kerahasiaan. Jadi, meskipun Watchtower menerima data tersebut, Watchtower tidak akan dapat mendekripsinya sampai pelanggaran benar-benar terjadi. Mekanisme enkripsi ini melindungi privasi pelanggan dan mencegah Watchtower mendapatkan akses yang tidak sah ke informasi sensitif.



Dalam tutorial ini, kita akan mencermati 3 cara menggunakan **Watchtower**:




- pertama, metode baku klasik melalui LND,
- kemudian pendekatan lain dengan Eye of Satoshi,
- dan terakhir, konfigurasi sederhana Watchtower pada node Lightning Anda yang dihosting dengan Umbrel.



## 1 - Mengkonfigurasi Watchtower atau klien melalui LND



*Tutorial ini diambil dari [dokumentasi resmi LND] (https://github.com/lightningnetwork/LND/blob/master/docs/Watchtower.md). Beberapa perubahan mungkin telah dilakukan pada versi aslinya



Sejak v0.7.0, `LND` mendukung eksekusi Watchtower altruistik pribadi sebagai subsistem yang terintegrasi penuh dari `LND`. Menara Pengawal menyediakan garis pertahanan kedua terhadap skenario pelanggaran yang berbahaya atau tidak disengaja ketika node pelanggan offline atau tidak dapat merespons pada saat terjadi pelanggaran, sehingga menawarkan tingkat keamanan yang lebih tinggi untuk dana saluran.



Tidak seperti _reward watchtower_, yang meminta bagian dari dana saluran sebagai imbalan atas layanannya, _altruist watchtower_ mengembalikan semua dana korban (dikurangi biaya On-Chain) tanpa mengenakan komisi. Menara pengawas hadiah akan diaktifkan di versi selanjutnya; mereka masih dalam tahap pengujian dan perbaikan.



Selain itu, `LND` sekarang dapat dikonfigurasikan untuk berfungsi sebagai _watchtower client_, menyimpan transaksi remediasi pelanggaran yang terenkripsi (yang disebut "transaksi keadilan") dari menara pengawas altruistik lainnya. Watchtower menyimpan gumpalan terenkripsi dengan ukuran tetap dan hanya dapat mendekripsi dan mempublikasikan transaksi keadilan setelah pihak yang melanggar menyiarkan status Commitment yang dicabut. Pelanggan ↔ Komunikasi Watchtower dienkripsi dan diautentikasi menggunakan pasangan kunci yang bersifat sementara, yang membatasi kemampuan Watchtower untuk melacak pelanggannya melalui kredensial jangka panjang.



Perlu diketahui bahwa kami telah memilih untuk menggunakan serangkaian fitur terbatas dalam rilis ini yang telah memberikan keamanan yang signifikan bagi pengguna `LND`. Banyak fitur terkait Watchtower lainnya yang hampir selesai atau sudah sangat maju; kami akan terus memberikannya saat kami mengujinya, dan segera setelah dianggap aman.



catatan: untuk saat ini, menara pengawas hanya menyimpan keluaran `ke_lokal` dan `ke_remote` dari komitmen yang dicabut; menyimpan keluaran HTLC akan digunakan di versi mendatang, karena protokol dapat diperluas untuk menyertakan data tanda tangan tambahan dalam gumpalan terenkripsi



### Mengkonfigurasi Watchtower



Untuk menyiapkan Watchtower, pengguna baris perintah perlu mengkompilasi sub-server `watchtowerrpc` opsional, yang memungkinkan interaksi dengan Watchtower melalui gRPC atau `lncli`. Binari yang dipublikasikan menyertakan sub-server `watchtowerrpc` secara default.



Konfigurasi minimum untuk mengaktifkan Watchtower adalah `Watchtower.active=1`.



Anda dapat mengambil informasi konfigurasi Watchtower Anda dengan `lncli tower info`:



```shell
$  lncli tower info
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"listeners": [
"[::]:9911"
],
"uris": [
],
}
```



Set lengkap opsi konfigurasi Watchtower tersedia melalui `LND -h`:



```shell
$  lnd -h
...
watchtower:
--watchtower.active                                     If the watchtower should be active or not
--watchtower.towerdir=                                  Directory of the watchtower.db (default: $HOME/.lnd/data/watchtower)
--watchtower.listen=                                    Add interfaces/ports to listen for peer connections
--watchtower.externalip=                                Add interfaces/ports where the watchtower can accept peer connections
--watchtower.readtimeout=                               Duration the watchtower server will wait for messages to be received before hanging up on client connections
--watchtower.writetimeout=                              Duration the watchtower server will wait for messages to be written before hanging up on client connections
...
```



#### Antarmuka mendengarkan



Secara default, Watchtower mendengarkan pada `:9911`, yang sesuai dengan port `9911` pada semua antarmuka yang tersedia. Pengguna dapat menentukan antarmuka pendengar mereka sendiri melalui opsi `--Watchtower.listen=`. Anda dapat memeriksa konfigurasi Anda di bidang `"listeners"` pada `lncli tower info`. Jika Anda mengalami masalah dalam menyambung ke Watchtower Anda, pastikan bahwa `<port>` terbuka atau proxy Anda dikonfigurasikan dengan benar ke Interface yang aktif.



#### Alamat IP eksternal



Pengguna juga dapat menentukan IP eksternal Watchtower Address(es) dengan `Watchtower.externalip=`, yang mengekspos URI lengkap Watchtower (pubkey@host:port) melalui RPC atau `lncli tower info`:



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911"
]
```



URI Watchtower dapat dikomunikasikan kepada pelanggan untuk disambungkan dan digunakan dengan perintah berikut:



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



Jika pelanggan Watchtower perlu mengaksesnya dari jarak jauh, pastikan untuk :




- Buka port 9911 (atau port yang ditentukan melalui `Watchtower.listen`).
- Gunakan proxy untuk mengarahkan lalu lintas dari port terbuka ke Watchtower yang mendengarkan Address.



#### Layanan tersembunyi Tor



Watchtowers mendukung layanan tersembunyi Tor dan dapat secara otomatis generate saat startup dengan opsi berikut:



```shell
$  lnd --tor.active --tor.v3 --watchtower.active
```



.onion Address kemudian muncul di bidang `"uris"` selama kueri `lncli tower info`:



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@bn2kxggzjysvsd5o3uqe4h7655u7v2ydhxzy7ea2fx26duaixlwuguad.onion:9911"
]
```



catatan: kunci publik Watchtower berbeda dengan kunci publik node `LND`. Untuk saat ini, ini bertindak sebagai "daftar putih Soft", karena pelanggan perlu mengetahui kunci publik Watchtower untuk menggunakannya sebagai cadangan, sambil menunggu mekanisme daftar putih yang lebih canggih. Kami menyarankan untuk TIDAK mengungkapkan kunci publik ini secara terbuka, kecuali jika Anda siap untuk mengekspos Watchtower Anda ke seluruh Internet._



#### Direktori basis data Watchtower



Basis data Watchtower dapat dipindahkan dengan menggunakan opsi `Watchtower.towerdir=`. Perhatikan bahwa akhiran `/Bitcoin/Mainnet/Watchtower.db` akan ditambahkan ke jalur yang dipilih untuk mengisolasi basis data dengan string. Dengan demikian, pengaturan `Watchtower.towerdir=/path/to/towerdir` akan menghasilkan basis data di `/path/to/towerdir/Bitcoin/Mainnet/Watchtower.db`.



Di bawah Linux, misalnya, basis data default Watchtower terletak di :


`/home/$USER/.LND/data/Watchtower/Bitcoin/Mainnet/Watchtower.db`



### Mengkonfigurasi klien Watchtower



Untuk mengonfigurasi klien Watchtower, Anda memerlukan dua item:





- Aktifkan klien Watchtower dengan opsi `--wtclient.active`.



```shell
$  lnd --wtclient.active
```





- URI dari Watchtower yang masih aktif.



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



Anda dapat mengonfigurasi beberapa menara pengawas dengan cara ini.



#### Tarif biaya untuk transaksi legal



Pengguna dapat secara opsional mengatur tarif biaya untuk transaksi keadilan melalui opsi `wtclient.sweep-fee-rate`, yang menerima nilai dalam sat/byte. Nilai defaultnya adalah 10 sat/byte, tetapi dimungkinkan untuk menetapkan tarif yang lebih tinggi untuk mencapai prioritas yang lebih tinggi selama biaya puncak. Mengubah `sweep-fee-rate` berlaku untuk semua pembaruan baru setelah daemon dimulai ulang.



#### Pengawasan



Dengan perintah `lncli wtclient`, pengguna sekarang dapat berinteraksi langsung dengan klien Watchtower untuk mendapatkan atau memodifikasi informasi tentang semua menara pengawas yang terdaftar.



Sebagai contoh, dengan `lncli wtclient tower`, Anda dapat mengetahui jumlah sesi yang saat ini dinegosiasikan dengan Watchtower yang ditambahkan di atas dan menentukan apakah sedang digunakan untuk cadangan berkat bidang `active_session_candidate`.



```shell
$  lncli wtclient tower 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": []
}
```



Untuk mendapatkan informasi tentang sesi Watchtower, gunakan opsi `--include_sessions`.



```shell
$  lncli wtclient tower --include_sessions 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": [
{
"num_backups": 0,
"num_pending_backups": 0,
"max_backups": 1024,
"sweep_sat_per_vbyte": 10
}
]
}
```



Semua opsi konfigurasi klien Watchtower tersedia melalui `lncli wtclient -h`:



```shell
$  lncli wtclient -h
NAME:
lncli wtclient - Interact with the watchtower client.

USAGE:
lncli wtclient command [command options] [arguments...]

COMMANDS:
add     Register a watchtower to use for future sessions/backups.
remove  Remove a watchtower to prevent its use for future sessions/backups.
towers  Display information about all registered watchtowers.
tower   Display information about a specific registered watchtower.
stats   Display the session stats of the watchtower client.
policy  Display the active watchtower client policy configuration.

OPTIONS:
--help, -h  show help
```




## 2 - Memasang Eye of Satoshi Anda sendiri



*Tutorial ini sebagian diambil dari artikel di [Summer of Bitcoin Blog] (https://blog.summerofbitcoin.org/). Modifikasi telah dilakukan terhadap versi aslinya*



Eye of Satoshi ([Rust-TEOS] (https://github.com/talaia-labs/Rust-teos)) adalah Watchtower Lightning non-depositori, yang sesuai dengan [Bolt 13] (https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org). Terdiri dari dua komponen utama:





- teos**: termasuk baris perintah Interface (CLI) dan fitur-fitur server penting dari Watchtower. Dua binari - **teosd** dan **teos-CLI** - dihasilkan ketika _crate_ ini dikompilasi.





- teos-common**: mencakup fungsionalitas sisi server dan sisi klien yang digunakan bersama (berguna untuk membuat klien).



Untuk menjalankan Watchtower dengan benar, Anda perlu menjalankan **bitcoind** sebelum meluncurkan Watchtower dengan perintah **teosd**. Sebelum menjalankan kedua perintah ini, Anda perlu mengonfigurasi file **Bitcoin.conf**. Berikut ini cara melakukannya:





- Instal Bitcoin core dari sumbernya atau unduh. Setelah mengunduh, letakkan file **Bitcoin.conf** di direktori pengguna Bitcoin core. Lihat tautan ini untuk informasi lebih lanjut tentang di mana menempatkan file, karena ini tergantung pada sistem operasi yang digunakan.





- Setelah lokasi diidentifikasi, tambahkan opsi berikut:



```shell
# RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

# chaîne
regtest=1
```





- server**: untuk permintaan RPC





- rpcuser** dan **rpcpassword**: mengautentikasi klien RPC ke server





- regtest**: tidak diperlukan, tetapi berguna jika Anda merencanakan pengembangan.



Nilai untuk **rpcuser** dan **rpcpassword** harus dipilih oleh Anda. Nilai-nilai tersebut harus ditulis tanpa tanda petik. Sebagai contoh:



```shell
rpcuser=aniketh
rpcpassword=strongpassword
```



Sekarang, jika Anda menjalankan **bitcoind**, node akan mulai.





- Untuk bagian Watchtower, Anda harus terlebih dahulu menginstal **teos** dari sumbernya. Ikuti petunjuk yang diberikan dalam tautan ini.





- Setelah Anda berhasil menginstal **teos** pada sistem Anda dan menjalankan tes, Anda dapat melanjutkan ke langkah terakhir: menyiapkan berkas **teos.toml** pada direktori pengguna teos. File ini harus ditempatkan pada sebuah folder bernama **.teos** (perhatikan tanda titik) di bawah direktori home Anda. Sebagai contoh, **/home//.teos** pada Linux. Setelah lokasi ditemukan, buatlah sebuah berkas **teos.toml** dan aturlah pilihan-pilihan ini sesuai dengan perubahan yang dibuat pada **bitcoind**:



```shell
# bitcoind
btc_network = "regtest"
btc_rpc_user = <your-user>
btc_rpc_password = <your-password>
```



Perhatikan bahwa di sini, nama pengguna dan kata sandi harus ditulis **dengan tanda petik**. Menggunakan contoh sebelumnya :



```shell
btc_rpc_user = "aniketh"
btc_rpc_password = "strongpassword"
```



Setelah ini selesai, Anda seharusnya siap untuk meluncurkan Watchtower. Karena kita berjalan pada **regtest**, kemungkinan tidak ada blok yang ditambang pada jaringan uji Bitcoin ketika Watchtower pertama kali tersambung (jika ada, berarti ada yang salah). Watchtower membangun cache internal dari 100 blok terakhir dari **bitcoind**; jadi, pada saat pertama kali dijalankan, Anda mungkin akan mendapatkan kesalahan berikut ini:



```shell
ERROR [teosd] Not enough blocks to start the tower (required: 100). Mine at least 100 more
```



Karena kita menggunakan **regtest**, kita dapat memblokir Miner dengan mengeluarkan perintah RPC, tanpa harus menunggu penundaan rata-rata 10 menit seperti yang terlihat pada jaringan lain (seperti Mainnet atau Testnet). Lihat bantuan **bitcoin-cli** untuk detail cara melakukan blok Miner.



![Image](assets/fr/01.webp)



Itu saja: Anda telah berhasil menjalankan Watchtower. Selamat. 🎉




## 3 - Mengkonfigurasi Watchtower pada Umbrel



Pada Umbrel, menghubungkan ke Watchtower untuk melindungi node Lightning Anda sangatlah mudah, karena semuanya dilakukan melalui Interface grafis. Setelah menghubungkan dari jarak jauh ke node Anda, buka aplikasi "**Lightning Node**".



![Image](assets/fr/02.webp)



Klik pada tiga titik kecil di kanan atas Interface, kemudian pilih "**Advanced Settings**".



![Image](assets/fr/03.webp)



Pada menu "**Watchtower**", tersedia dua opsi:





- Layanan Watchtower**: opsi ini memungkinkan Anda mengoperasikan Watchtower, yaitu layanan yang memonitor saluran node lain untuk mendeteksi upaya penipuan. Jika terjadi pelanggaran, Watchtower Anda akan menerbitkan transaksi pada Blockchain, sehingga pengguna dapat memulihkan dana mereka yang terkunci. Setelah diaktifkan, URI Watchtower Anda akan muncul dan dapat dikomunikasikan ke node lain sehingga mereka dapat menambahkannya ke klien Watchtower mereka;





- Watchtower Client**: opsi ini memungkinkan Anda terhubung ke menara pengawas eksternal untuk melindungi saluran Anda sendiri. Setelah diaktifkan, Anda dapat menambahkan layanan Watchtower ke mana node Anda akan mengirimkan informasi yang diperlukan tentang salurannya. Menara pengawas ini kemudian akan memantau status mereka dan melakukan intervensi jika terjadi percobaan penipuan.



Prioritas bagi Anda tentu saja adalah mengaktifkan *Watchtower Client* untuk melindungi node Anda, tetapi saya juga menyarankan agar Anda mengaktifkan *Watchtower Service* untuk berkontribusi pada keamanan pengguna lain.



![Image](assets/fr/04.webp)



Kemudian klik pada tombol Green "**Save and Restart Node**". LND Anda akan dimulai ulang.



Pada menu yang sama, Anda juga akan menemukan URI layanan Watchtower Anda jika Anda telah mengaktifkannya. Anda juga dapat menambahkan URI Watchtower eksternal untuk melindungi saluran Anda. Klik "**TAMBAH**" untuk mengonfirmasi.



![Image](assets/fr/05.webp)



Ada beberapa Menara Pengawal yang tersedia secara online. Sebagai contoh, [LN+ dan Voltage menawarkan Watchtower altruistik] (https://lightningnetwork.plus/Watchtower) yang dapat Anda sambungkan:



```
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



![Image](assets/fr/06.webp)



Pilihan lainnya adalah dengan Exchange URI Watchtower Anda dengan sesama pengguna bitcoin, sehingga masing-masing melindungi node lainnya.



Saya juga menyarankan agar Anda menyiapkan beberapa Menara Pengawal untuk mengurangi risiko jika salah satu dari Menara Pengawal tersebut tidak tersedia.



Terakhir, Anda dapat menyesuaikan parameter "**Tingkat Biaya Sapuan Klien Watchtower**". Ini menentukan tingkat biaya maksimum yang bersedia Anda bayarkan untuk transaksi hukuman siaran Watchtower yang akan disertakan dalam blok. Pastikan Anda menetapkan nilai yang cukup tinggi, disesuaikan dengan jumlah yang dikunci di saluran Anda.