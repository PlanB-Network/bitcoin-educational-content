---
name: Lightning Watchtower
description: Memahami dan menggunakan Watchtower pada simpul Lightning Anda
---
![cover](assets/cover.webp)



## Bagaimana cara kerja Watch Tower?



Bagian penting dari ekosistem Lightning Network, _Watchtower_ memberi tingkat perlindungan ekstra buat saluran Lightning kamu. Peran utamanya adalah memantau status saluran dan ikut turun tangan jika salah satu sisi saluran mencoba menipu sisi lainnya.


Bagaimana watchtower bisa tahu kalau sebuah saluran sudah disusupi? Watchtower menerima dari kliennya (salah satu pihak dalam saluran) info yang dibutuhkan untuk mengenali dan menangani pelanggaran dengan benar. Info ini mencakup rincian transaksi terakhir, status saluran saat ini, dan elements yang diperlukan untuk membuat transaksi penalti. Sebelum ngirim data ini ke watchtower, klien bisa mengenkripsinya untuk menjaga kerahasiaan. Jadi meskipun watchtower menerima data tersebut, watchtower nggak bisa mendekripsinya sampai pelanggaran benar terjadi. Mekanisme enkripsi ini melindungi privasi klien dan mencegah watchtower mendapatkan akses yang nggak sah ke informasi sensitif.


Dalam tutorial ini, kita akan mencermati 3 cara menggunakan **Watchtower**:




- pertama, metode baku klasik melalui LND,
- kemudian pendekatan lain dengan Eye of Satoshi,
- dan terakhir, konfigurasi sederhana Watchtower pada node Lightning Anda yang dihosting dengan Umbrel.



## 1 - Mengkonfigurasi Watchtower atau klien melalui LND



*Tutorial ini diambil dari [dokumentasi resmi LND](https://github.com/lightningnetwork/LND/blob/master/docs/Watchtower.md). Beberapa perubahan mungkin telah dilakukan pada versi aslinya



Sejak v0.7.0, `LND` mendukung eksekusi altruistic watchtower pribadi sebagai subsistem yang terintegrasi penuh di dalam LND. Watchtower memberi garis pertahanan kedua terhadap skenario pelanggaran yang berbahaya atau tidak sengaja ketika node klien sedang offline atau nggak bisa merespons saat pelanggaran terjadi, sehingga memberi tingkat keamanan yang lebih tinggi buat dana saluran.

Nggak seperti reward watchtower yang meminta sebagian dana saluran sebagai imbalan atas jasanya, altruist watchtower mengembalikan semua dana korban dengan hanya memotong biaya on chain tanpa mengambil komisi. Reward watchtower akan diaktifkan di versi berikutnya; fitur ini masih dalam tahap pengujian dan penyempurnaan.

Selain itu, `LND` sekarang bisa dikonfigurasikan untuk berfungsi sebagai watchtower client, yang menyimpan transaksi remediasi pelanggaran terenkripsi yang dikenal sebagai transaksi keadilan dari altruist watchtower lainnya. Watchtower menyimpan gumpalan terenkripsi berukuran tetap dan hanya bisa mendekripsi serta mempublikasikan transaksi keadilan setelah pihak yang melanggar menyiarkan status commitment yang sudah dicabut. Komunikasi klien ↔ watchtower terenkripsi dan diautentikasi menggunakan pasangan kunci sementara, yang membatasi kemampuan watchtower untuk melacak klien lewat kredensial jangka panjang.

Perlu kamu tahu kalau kita memilih untuk memakai rangkaian fitur terbatas dalam rilis ini yang sudah memberi peningkatan keamanan signifikan bagi pengguna `LND`. Banyak fitur watchtower lainnya sudah hampir selesai atau sudah sangat matang; kita akan terus merilisnya setelah pengujian dan begitu dianggap aman.

Catatan: untuk saat ini, watchtower hanya menyimpan output `to_local` dan `to_remote` dari commitment yang dicabut. Penyimpanan output HTLC akan digunakan di versi mendatang karena protokolnya bisa diperluas untuk menyertakan data tanda tangan tambahan di dalam gumpalan terenkripsi.



### Mengkonfigurasi Watchtower

Untuk menyiapkan watchtower, pengguna baris perintah perlu mengompilasi sub server opsional `watchtowerrpc`, yang memungkinkan interaksi dengan watchtower lewat gRPC atau `lncli`. Binari yang dipublikasikan sudah menyertakan sub server `watchtowerrpc` secara default.

Konfigurasi minimum untuk mengaktifkan watchtower adalah `Watchtower.active=1`.

Kamu bisa mengambil info konfigurasi watchtower kamu dengan `lncli tower info`:


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



Secara default, watchtower mendengarkan pada `:9911`, yang sesuai dengan port `9911` di semua antarmuka yang tersedia. Pengguna bisa menentukan antarmuka pendengar mereka sendiri lewat opsi --Watchtower.listen=. Kamu bisa mengecek konfigurasi kamu di bidang "listeners" pada `lncli tower info`. Kalau kamu mengalami masalah saat nyambung ke watchtower kamu, pastikan `<port>` sudah terbuka atau proxy kamu sudah dikonfigurasi dengan benar ke interface yang aktif.



#### Alamat IP eksternal



Pengguna juga dapat menentukan IP eksternal Watchtower Address(es) dengan `Watchtower.externalip=`, yang mengekspos URI lengkap Watchtower (pubkey@host:port) melalui RPC atau `lncli tower info`:



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911"
]
```



URI Watchtower dapat dikomunikasikan ke pelanggan untuk disambungkan dan digunakan dengan perintah ini:



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```


Kalau pelanggan Watchtower perlu mengaksesnya dari jarak jauh, pastikan untuk :




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



Catatan: kunci publik watchtower berbeda dari kunci publik node LND. Untuk saat ini, ini berfungsi sebagai soft whitelist, karena klien perlu mengetahui kunci publik watchtower untuk bisa memakainya sebagai cadangan sambil menunggu mekanisme whitelist yang lebih canggih. Aku menyarankan untuk tidak mengungkapkan kunci publik ini secara terbuka kecuali kalau kamu memang siap membuat watchtower kamu terekspos ke seluruh internet.



#### Direktori basis data Watchtower



Basis data Watchtower dapat dipindahkan dengan menggunakan opsi `Watchtower.towerdir=`. Perhatikan bahwa akhiran `/Bitcoin/Mainnet/Watchtower.db` akan ditambahkan ke jalur yang dipilih untuk mengisolasi basis data dengan string. Dengan demikian, pengaturan `Watchtower.towerdir=/path/to/towerdir` akan menghasilkan basis data di `/path/to/towerdir/Bitcoin/Mainnet/Watchtower.db`.



Di bawah Linux, misalnya, basis data default Watchtower terletak di :


`/home/$USER/.LND/data/Watchtower/Bitcoin/Mainnet/Watchtower.db`



### Mengkonfigurasi klien Watchtower



Untuk mengonfigurasi klien Watchtower, kamu memerlukan dua item:





- Aktifkan klien Watchtower dengan opsi `--wtclient.active`.



```shell
$  lnd --wtclient.active
```





- URI dari Watchtower yang masih aktif.



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



Kamu dapat mengonfigurasi beberapa menara pengawas dengan cara ini.



#### Tarif biaya untuk transaksi legal


Pengguna bisa secara opsional mengatur tarif biaya untuk transaksi keadilan lewat opsi `wtclient.sweep-fee-rate`, yang menerima nilai dalam sat per byte. Nilai defaultnya 10 sat per byte, tapi kamu bisa menetapkan tarif yang lebih tinggi supaya dapet prioritas lebih besar saat biaya jaringan sedang tinggi. Perubahan pada `sweep-fee-rate` akan berlaku untuk semua pembaruan baru setelah daemon dimulai ulang.



#### Pengawasan



Dengan perintah `lncli wtclient`, pengguna sekarang dapat berinteraksi langsung dengan klien Watchtower untuk mendapatkan atau memodifikasi informasi tentang semua watchtowers yang terdaftar.


Sebagai contoh, dengan `lncli wtclient tower`, kamu bisa melihat jumlah sesi yang saat ini dinegosiasikan dengan watchtower yang tadi kamu tambahkan dan mengetahui apakah dia sedang dipakai sebagai cadangan lewat bidang `active_session_candidate`.



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




## 2 - Memasang Eye of Satoshi kamu sendiri



*Tutorial ini sebagian diambil dari artikel di [Summer of Bitcoin Blog](https://blog.summerofbitcoin.org/). Modifikasi telah dilakukan terhadap versi aslinya*



Eye of Satoshi ([Rust-TEOS](https://github.com/talaia-labs/Rust-teos)) adalah Watchtower Lightning non-depositori, yang sesuai dengan [Bolt 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org). Terdiri dari dua komponen utama:





- teos**: termasuk baris perintah Interface (CLI) dan fitur-fitur server penting dari Watchtower. Dua binari - **teosd** dan **teos-CLI** - dihasilkan ketika _crate_ ini dikompilasi.





- teos-common**: mencakup fungsionalitas sisi server dan sisi klien yang digunakan bersama (berguna untuk membuat klien).



Untuk menjalankan Watchtower dengan benar, kamu perlu menjalankan **bitcoind** sebelum meluncurkan Watchtower dengan perintah **teosd**. Sebelum menjalankan kedua perintah ini, kamu perlu mengonfigurasi file **Bitcoin.conf**. Berikut ini cara melakukannya:





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





- regtest**: tidak diperlukan, tetapi berguna kalau kamu merencanakan pengembangan.



Nilai untuk **rpcuser** dan **rpcpassword** harus dipilih oleh kamu. Nilai-nilai tersebut harus ditulis tanpa tanda petik. Sebagai contoh:



```shell
rpcuser=aniketh
rpcpassword=strongpassword
```



Sekarang, kalau kamu menjalankan **bitcoind**, node akan mulai.





- Untuk bagian Watchtower, Anda harus terlebih dahulu menginstal **teos** dari sumbernya. Ikuti petunjuk yang diberikan dalam tautan ini.





- Setelah kamu berhasil menginstal **teos** di sistem kamu dan menjalankan tesnya, kamu bisa lanjut ke langkah terakhir yaitu menyiapkan berkas **teos.toml** di direktori pengguna teos. File ini harus ditempatkan dalam folder bernama **.teos** (ingat ada tanda titik) di dalam direktori home kamu. Misalnya, **/home/ /** **.teos** di Linux. Setelah lokasinya ditemukan, buat berkas **teos.toml** dan atur opsi opsinya sesuai perubahan yang sudah kamu lakukan di bitcoind.



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



Setelah ini selesai, kamu harusnya sudah siap untuk menjalankan watchtower. Karena kita berjalan di regtest, kemungkinan nggak ada blok yang ditambang di jaringan uji Bitcoin saat watchtower pertama kali tersambung. Kalau ada blok, berarti ada yang salah. Watchtower membangun cache internal dari 100 blok terakhir dari **bitcoind**, jadi saat pertama kali dijalankan kamu mungkin bakal melihat error seperti ini:



```shell
ERROR [teosd] Not enough blocks to start the tower (required: 100). Mine at least 100 more
```



Karena kita menggunakan **regtest**, kita dapat memblokir Miner dengan mengeluarkan perintah RPC, tanpa harus menunggu penundaan rata-rata 10 menit seperti yang terlihat pada jaringan lain (seperti Mainnet atau Testnet). Lihat bantuan **bitcoin-cli** untuk detail cara melakukan blok Miner.



![Image](assets/fr/01.webp)



Itu saja: kamu telah berhasil menjalankan Watchtower. Selamat. 🎉




## 3 - Mengkonfigurasi Watchtower pada Umbrel



Di Umbrel, menghubungkan ke watchtower untuk melindungi node Lightning kamu itu gampang banget karena semuanya dilakukan lewat antarmuka grafis. Setelah terhubung dari jarak jauh ke node kamu, buka aplikasi "**Lightning Node**".



![Image](assets/fr/02.webp)



Klik pada tiga titik kecil di kanan atas Interface, kemudian pilih "**Advanced Settings**".



![Image](assets/fr/03.webp)



Pada menu "**Watchtower**", tersedia dua opsi:





- **Watchtower Service:** opsi ini memungkinkan kamu mengoperasikan watchtower, yaitu layanan yang memantau saluran node lain untuk mendeteksi upaya penipuan. Kalau terjadi pelanggaran, watchtower kamu akan menerbitkan transaksi ke blockchain supaya pengguna bisa memulihkan dana mereka yang terkunci. Setelah diaktifkan, URI watchtower kamu akan muncul dan bisa dibagikan ke node lain supaya mereka bisa menambahkannya ke klien watchtower mereka.

- **Watchtower Client:** opsi ini memungkinkan kamu terhubung ke watchtower eksternal untuk melindungi saluran kamu sendiri. Setelah diaktifkan, kamu bisa menambahkan layanan watchtower tempat node kamu akan mengirim info yang diperlukan tentang salurannya. Watchtower tersebut lalu akan memantau statusnya dan bertindak kalau ada percobaan penipuan.

- Prioritas buat kamu tentu mengaktifkan Watchtower Client untuk melindungi node kamu, tapi aku juga menyarankan supaya kamu mengaktifkan Watchtower Service untuk berkontribusi pada keamanan pengguna lain.



![Image](assets/fr/04.webp)



Kemudian klik pada tombol Green "**Save and Restart Node**". LND Anda akan dimulai ulang.



Pada menu yang sama, kamu juga akan menemukan URI layanan Watchtower kamu jika Anda telah mengaktifkannya. kamu juga dapat menambahkan URI Watchtower eksternal untuk melindungi saluran Anda. Klik "**TAMBAH**" untuk mengonfirmasi.



![Image](assets/fr/05.webp)



Ada beberapa Menara Pengawal yang tersedia secara online. Sebagai contoh, [LN+ dan Voltage menawarkan Watchtower altruistik](https://lightningnetwork.plus/Watchtower) yang dapat Anda sambungkan:



```
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



![Image](assets/fr/06.webp)



Pilihan lainnya adalah saling bertukar URI watchtower dengan sesama pengguna Bitcoin supaya masing masing bisa saling melindungi node satu sama lain.

Aku juga menyarankan kamu menyiapkan beberapa watchtower untuk mengurangi risiko kalau salah satu watchtower sedang nggak tersedia.

Terakhir, kamu bisa menyesuaikan parameter **Tingkat Biaya Sweeping Klien Watchtower.** Ini menentukan tingkat biaya maksimum yang kamu bersedia bayar untuk transaksi penalti yang disiarkan watchtower supaya bisa masuk blok. Pastikan kamu menetapkan nilai yang cukup tinggi dan sesuai dengan jumlah dana yang terkunci di saluran kamu.
