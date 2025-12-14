---
name: Sparrow Wallet
description: Cara menginstal, mengatur, dan menggunakan Sparrow Wallet
---
![cover](assets/cover.webp)

Sparrow Wallet adalah alat open-source buatan Craig Raw yang membantu pengguna mengelola Bitcoin mereka dengan aman dan efisien. Wallet ini populer di kalangan Bitcoiner karena kemudahan penggunaan dan fitur-fiturnya yang mendalam.

Ada dua cara untuk menggunakan Sparrow:


- Seperti hot wallet pada umumnya, kunci pribadi tersimpan langsung di komputermu.
- Sebagai pengelola cold wallet, Sparrow bisa dipakai bareng hardware wallet — di mana kunci privat disimpan langsung di perangkat keras seperti Ledger atau Trezor. Dalam mode ini, Sparrow cuma ngatur info wallet publik: melacak saldo, bikin alamat baru, dan nyusun transaksi. Tapi, biar transaksi itu sah, tetap butuh tanda tangan dari hardware wallet. Karena itulah, Sparrow bisa jadi pengganti aplikasi bawaan kayak Ledger Live atau Trezor Suite.

Sparrow mendukung dompet single-sig (tanda tangan tunggal) maupun multi-sig (multi tanda tangan), dan bisa dipakai buat ngatur banyak wallet sekaligus dengan lancar. Misalnya, kamu bisa pakai satu wallet yang terhubung ke Ledger, satu lagi ke Trezor, plus hot wallet yang langsung di komputer kamu — semua bisa dikontrol bareng dari Sparrow.

Sparrow juga punya fitur coin control yang canggih, jadi kamu bisa pilih sendiri UTXO (kepingan saldo Bitcoin) mana yang mau dipakai saat kirim transaksi. Fitur ini bikin kamu bisa jaga privasi lebih baik dan ngatur strategi pengiriman dengan lebih rapi.

Soal koneksi, Sparrow ngasih fleksibilitas penuh — kamu bisa hubungkan langsung ke node Bitcoin milikmu sendiri, entah itu lewat server Electrum jarak jauh atau langsung pakai Bitcoin Core. Kalau belum punya node pribadi, kamu juga bisa pakai node publik. Semua koneksi jarak jauh bakal lewat jaringan Tor, jadi tetap aman dan privat.

## Cara Install Sparrow Wallet

Buka [halaman unduhan resmi Sparrow Wallet] (https://sparrowwallet.com/download/) dan pilih versi perangkat lunak yang sesuai dengan sistem operasi Anda.

![Image](assets/fr/01.webp)

Sebelum install, penting banget buat cek dulu apakah file Sparrow-nya asli dan nggak diubah-ubah. Ini buat jaga-jaga dari risiko software palsu atau malware. Kalau kamu belum tahu caranya, tenang aja — ada panduan lengkapnya di sini:

https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Begitu Sparrow udah terinstal, kamu bisa langsung lewatin layar pembuka dan lanjut ke bagian pengaturan koneksi.

![Image](assets/fr/02.webp)

## Menghubungkan ke jaringan Bitcoin

Supaya bisa terhubung ke jaringan Bitcoin dan ngirim transaksi, Sparrow perlu nyambung dulu ke node Bitcoin. Ada tiga cara utama buat nyambungin Sparrow ke node:


- 🟡 Pakai node publik, Kalau kamu belum punya node sendiri, kamu bisa pakai simpul publik alias node pihak ketiga yang terbuka untuk umum. Ini cara paling cepat buat mulai pakai Sparrow tanpa ribet. Tapi perlu diingat, node yang kamu pakai bisa ngintip semua transaksi yang kamu lihat atau kirim — jadi privasimu bisa bocor. Memegang kunci sendiri itu penting, tapi punya node sendiri jauh lebih mantap. Jadi, pilihan ini cocok buat pemula yang baru mulai, asal kamu sadar risikonya ya.
- 🟢 Sambung ke node bitcoin core. Kalau kamu udah punya node Bitcoin Core sendiri, kamu bisa sambungin langsung ke Sparrow. Bisa secara lokal (kalau Bitcoin Core-nya ada di komputer yang sama), atau jarak jauh kalau node-nya jalan di perangkat lain. Cara ini lebih aman dan lebih privat karena kamu nggak perlu bergantung ke pihak ketiga — semua data langsung dari node milikmu sendiri.
- 🔵 Kalau node Bitcoin kamu udah dilengkapi Electrs (biasanya udah ada di solusi all-in-one kayak Umbrel atau Start9), kamu bisa sambungin Sparrow dari jarak jauh lewat server Electrum itu. Cara ini cocok buat kamu yang punya node sendiri di perangkat terpisah, tapi tetap pengen akses Sparrow dari laptop atau komputer lain. Lebih fleksibel, tetap privat.

**Lebih baik pakai koneksi ke Electrs atau langsung ke Bitcoin Core di node kamu sendiri. Dengan begitu, kamu nggak perlu terlalu ngandelin pihak ketiga, dan privasimu juga lebih terjaga.**

### Terhubung ke node publik 🟡

Menghubungkan ke node publik sangat sederhana. Klik pada tab "*Public Server*".

![Image](assets/fr/03.webp)

Pilih node dari daftar dropdown yang muncul.

![Image](assets/fr/04.webp)

Kemudian klik "*Test Connection*".

![Image](assets/fr/05.webp)

Kalau udah tersambung, Sparrow bakal nunjukin tanda centang kuning di pojok kanan bawah. Itu artinya kamu lagi terhubung ke node publik.

![Image](assets/fr/06.webp)

### Menghubungkan ke Bitcoin Core 🟢

Metode kedua buat nyambung ke node Bitcoin adalah lewat Bitcoin Core. Kalau Bitcoin Core-nya terpasang di komputer yang sama, Sparrow bakal otomatis autentikasi pakai cookie file. Tapi kalau Bitcoin Core-nya jalan di mesin lain (jarak jauh), kamu perlu masukin password yang udah kamu atur di file bitcoin.conf.

Perlu dicatat, kalau kamu pakai Bitcoin Core versi pruned (yang dipangkas), kamu nggak bisa pulihkan wallet yang punya transaksi sebelum blok-blok lama yang udah dibuang. Tapi tenang, kalau kamu bikin wallet baru langsung di Sparrow, hal ini nggak masalah kok — transaksi baru tetap bakal kelihatan meskipun node-nya pruned.

Buat mengatur node Bitcoin Core, kamu bisa ikutin salah satu tutorial di bawah ini — pilih aja yang sesuai sama sistem operasi yang kamu pakai:

https://planb.academy/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

Pada Sparrow, buka tab "*Bitcoin Core*".

![Image](assets/fr/07.webp)

**Dengan Bitcoin Core lokal:**

Kalau Bitcoin Core udah terpasang di komputermu, cari file bitcoin.conf di folder data Bitcoin.
Kalau file itu belum ada, nggak apa-apa — kamu bisa bikin sendiri.

Cukup buka editor teks (kayak Notepad di Windows), lalu masukin baris berikut ini:

```ini
server=1
```

Kemudian simpan perubahannya.

Kamu juga bisa ngaktifin ini lewat tampilan antarmuka Bitcoin Core (Bitcoin-QT).
Caranya: buka menu "Settings" > "Options...", lalu centang pilihan "Enable RPC server".

Jangan lupa untuk memulai ulang perangkat lunak setelah melakukan perubahan ini.

![Image](assets/fr/08.webp)

Setelah itu, balik lagi ke Sparrow Wallet dan masukin jalur (path) ke file cookie kamu.
File ini biasanya ada di folder yang sama dengan bitcoin.conf, tapi letaknya bisa beda-beda tergantung sistem operasi yang kamu pakai:

| **macOS** | ~/Perpustakaan/Dukungan Aplikasi/Bitcoin |

| ----------- | ------------------------------------- |

| **Windows** | %APPDATA%\Bitcoin |

| **Linux** | ~/.Bitcoin |

![Image](assets/fr/09.webp)

Biarkan parameter lain sebagai default, URL `127.0.0.1` dan port `8332`, lalu klik "*Test Connection*".

![Image](assets/fr/10.webp)

Kalau sambungan berhasil, bakal muncul tanda centang hijau di pojok kanan bawah. Itu tandanya Sparrow udah terhubung ke node Bitcoin Core kamu.

![Image](assets/fr/11.webp)

**dengan remote Bitcoin Core: Dengan remote Bitcoin Core:**

Kalau Bitcoin Core-nya ada di komputer lain tapi masih dalam jaringan yang sama, kamu tetap bisa sambungin ke Sparrow.
Pertama, cari file bitcoin.conf di folder data Bitcoin. Kalau belum ada, kamu bisa bikin sendiri.

Buka file itu pakai editor teks (kayak Notepad), lalu tambahkan baris berikut ini:

```ini
server=1
```

Setelah mengedit file, pastikan Anda menyimpannya dalam folder yang sesuai untuk sistem operasi Anda:

| **macOS** | ~/Perpustakaan/Dukungan Aplikasi/Bitcoin |

| ----------- | ------------------------------------- |

| **Windows** | %APPDATA%\Bitcoin |

| **Linux** | ~/.Bitcoin |

Kamu juga bisa ngelakuin ini lewat tampilan antarmuka Bitcoin Core (Bitcoin-QT).
Cukup buka menu "Settings", lalu pilih "Options...", dan centang kotak "Enable RPC server".

Kalau file bitcoin.conf belum ada, gampang kok — kamu bisa langsung bikin dari sini juga dengan klik "Open Configuration File". Nanti bakal otomatis bikin file-nya, dan kamu tinggal isi sesuai kebutuhan.

![Image](assets/fr/12.webp)

Temukan IP Address dari mesin yang menghosting Bitcoin Core di jaringan lokal Anda. Untuk melakukan ini, Anda dapat menggunakan alat seperti [Angry IP Scanner] (https://angryip.org/). Mari kita asumsikan, untuk kepentingan argumen, bahwa IP Address dari node Anda adalah `192.168.1.18`.

Dalam berkas `Bitcoin.conf`, tambahkan baris berikut, atur `rpcbind=192.168.1.18` untuk mencocokkan IP Address node Anda.

```ini
[main]
rpcbind=127.0.0.1
rpcbind=192.168.1.18
rpcallowip=127.0.0.1
rpcallowip=192.168.1.0/24
```

![Image](assets/fr/13.webp)

Pada berkas `Bitcoin.conf`, tambahkan nama pengguna dan kata sandi untuk sambungan jarak jauh. Pastikan untuk mengganti `loic` dengan nama pengguna dan `my_password` dengan kata sandi yang kuat:

```ini
rpcuser=loic
rpcpassword=my_password
```

![Image](assets/fr/14.webp)

Setelah memodifikasi dan menyimpan file, mulai ulang perangkat lunak Bitcoin-QT.

Sekarang balik lagi ke Sparrow Wallet.
Buka tab "User / Pass", lalu masukin username dan password yang tadi udah kamu atur di file bitcoin.conf.

Biarkan pengaturan lainnya tetap default:

URL: 127.0.0.1
Port: 8332

Kalau udah, klik tombol "Test Connection" buat ngecek apakah Sparrow berhasil nyambung ke node kamu.

![Image](assets/fr/15.webp)

Kalau koneksi berhasil, bakal muncul tanda centang hijau di pojok kanan bawah. Itu tandanya Sparrow udah berhasil nyambung ke node Bitcoin Core kamu.

![Image](assets/fr/16.webp)

### Menghubungkan ke server Electrum 🔵

Opsi terakhir buat nyambungin Sparrow adalah lewat server Electrum jarak jauh.
Metode ini cocok banget kalau kamu mau akses node dari perangkat lain lewat jaringan Tor. Sparrow bisa manfaatin indeks dari Electrs, jadi lacak transaksi dan saldo jadi jauh lebih cepat. Ini ideal banget buat kamu yang pakai solusi node-in-a-box kayak Umbrel atau Start9, karena Electrs bisa diinstal cuma dengan sekali klik aja.

Untuk melakukan ini, dapatkan Tor `.onion' Address dari server Electrum Anda. Dengan Umbrel, misalnya, Anda akan menemukannya di aplikasi Electrs.

![Image](assets/fr/17.webp)

Pada Sparrow Wallet, akses tab "*Private Electrum*".

![Image](assets/fr/18.webp)

Masukkan Tor Address Anda di tempat yang disediakan. Pengaturan lainnya bisa tetap default. Kemudian klik "*Test Connection*".

![Image](assets/fr/19.webp)

Kalau koneksi udah berhasil, kamu bisa tutup jendela pengaturannya.
Nanti bakal muncul tanda centang biru di pojok kanan bawah — itu tandanya Sparrow udah terhubung ke server Electrum kamu.

![Image](assets/fr/20.webp)

## Bikin Hot Wallet Pertamamu

Setelah Sparrow berhasil dikonfigurasi dan terhubung ke jaringan Bitcoin, sekarang waktunya bikin wallet pertamamu.
Di bagian ini, kita bakal bikin Hot Wallet, yaitu wallet yang nyimpen kunci privat langsung di komputer kamu. Karena komputer itu perangkat yang kompleks dan selalu terhubung ke internet, artinya permukaan serangannya cukup besar. Jadi, Hot Wallet sebaiknya cuma dipakai buat nyimpen jumlah Bitcoin yang kecil — kayak buat transaksi sehari-hari atau testing. Kalau kamu mau nyimpen Bitcoin dalam jumlah besar, lebih aman pakai wallet yang terhubung ke Hardware Wallet.
Kalau itu yang kamu butuhkan, kamu bisa langsung loncat ke bagian selanjutnya.

Untuk membuat Hot Wallet, dari layar beranda Sparrow Wallet, klik tab "*File*" dan kemudian "*New Wallet*".

![Image](assets/fr/21.webp)

Masukkan nama untuk portofolio Anda dan klik "*Buat Wallet*".

![Image](assets/fr/22.webp)

Di bagian atas tampilan, kamu bisa pilih mau bikin wallet tipe Single Signature atau Multi Signature.
Tepat di bawahnya, ada pilihan jenis script buat ngunci UTXO kamu. Supaya lebih up-to-date dan efisien, aku saranin pakai standar terbaru: Taproot (P2TR).

![Image](assets/fr/23.webp)

Kemudian klik "*Software Wallet Baru atau Impor*".

![Image](assets/fr/24.webp)

Pilih standar BIP39, karena ini yang paling umum dan didukung hampir semua software Bitcoin.
Setelah itu, pilih panjang recovery phrase (kata sandi pemulihan) kamu. Sekarang ini, 12 kata udah cukup aman, dan lebih gampang disimpan atau dihafal dibanding 24 kata.

![Image](assets/fr/25.webp)

Klik tombol "Generate New" buat bikin recovery phrase wallet kamu.
Frasa ini penting banget — dia ngasih akses penuh ke semua Bitcoin yang kamu simpan.
Siapa pun yang punya frasa ini bisa ambil semua dana kamu, bahkan tanpa perlu nyentuh komputer kamu.
Jadi pastikan kamu nyimpen frasa ini di tempat yang aman, offline, dan jangan pernah kasih ke siapa pun.

Frasa 12 kata ini bisa ngembaliin akses ke Bitcoin kamu kalau sewaktu-waktu komputer rusak, hilang, atau dicuri.
Makanya, penting banget buat nyimpen frasa ini dengan hati-hati dan di tempat yang aman — idealnya offline, nggak difoto, dan nggak disimpan di cloud.

Kamu bisa nulis frasa ini di kertas, atau kalau mau lebih aman, ukir di lempengan baja tahan karat.
Cara ini bakal bantu lindungi frasa kamu dari risiko kayak kebakaran, banjir, atau kerusakan fisik lainnya. Media penyimpanannya bisa disesuaikan sama strategi keamanan kamu.
Tapi kalau kamu pakai Sparrow ini cuma buat Hot Wallet dengan jumlah Bitcoin yang nggak terlalu besar, ditulis di kertas aja udah cukup kok — asal disimpan dengan baik dan nggak mudah diakses orang lain.

Kalau kamu masih baru dan pengen belajar lebih dalam soal cara nyimpen dan ngelola frasa mnemonic dengan benar, aku saranin banget buat cek tutorial lanjutan lainnya. Info ini penting banget, apalagi buat pemula, supaya kamu nggak kehilangan akses ke Bitcoin kamu di masa depan.

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/26.webp)

**Jelas ya, frasa 12 kata ini nggak boleh dibagikan di internet — beda sama yang aku lakukan di tutorial ini.**
Wallet ini cuma contoh, dan cuma dipakai di Testnet (bukan jaringan Bitcoin asli).
Nanti juga bakal dihapus setelah tutorial selesai. Jadi ingat, jangan pernah bagikan frasa wallet asli kamu ke siapa pun, apalagi online.

Kamu juga bisa nambahin passphrase BIP39 dengan centang kotak “Use passphrase”.
Fitur ini bisa bikin wallet kamu jauh lebih aman, tapi hati-hati — kalau kamu nggak ngerti cara kerjanya, risikonya bisa besar. Makanya, aku saranin banget buat baca dulu penjelasan singkat tentang teori di balik passphrase ini sebelum kamu pakai.

https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Setelah kamu nyimpen frasa mnemonic dan passphrase (kalau ada) ke media fisik, klik tombol "Konfirmasi Pencadangan".
Tombol ini menandai kalau kamu udah siap lanjut dan frasanya udah benar-benar kamu amankan.

![Image](assets/fr/27.webp)

Sekarang, masukin lagi 12 kata recovery kamu buat memastikan semuanya udah disimpan dengan benar.
Kalau udah cocok semua, klik tombol "Create Keystore" buat lanjut ke tahap berikutnya.

![Image](assets/fr/28.webp)

Kemudian klik "*Import Keystore*" untuk mengimpor kunci portofolio dari frasa Mnemonic.

![Image](assets/fr/29.webp)

Klik "*Apply*" untuk menyelesaikan pembuatan portofolio.

![Image](assets/fr/30.webp)

Sekarang, buat password yang kuat untuk ngamanin akses ke wallet kamu di Sparrow.
Biar nggak lupa, sebaiknya simpan password ini di password manager yang aman. Perlu kamu tahu, password ini nggak memengaruhi frasa pemulihan (mnemonic) kamu. Password ini cuma dipakai buat buka wallet di Sparrow.
Artinya, meskipun kamu lupa password ini, kamu masih bisa akses Bitcoin kamu pakai frasa 12 kata tadi — lewat aplikasi lain yang juga mendukung BIP39.

![Image](assets/fr/31.webp)

Hot Wallet kamu sekarang udah jadi!
Kalau kamu nggak mau sambungin ke Hardware Wallet, kamu bisa langsung lanjut ke bagian "Menerima Bitcoin" di tutorial ini.

## Mengelola portofolio Cold

Cara kedua pakai Sparrow Wallet adalah dengan nyambungin ke Hardware Wallet sebagai pengelola portofolio.
Dalam mode ini, private key kamu tetap aman tersimpan di hardware wallet, dan Sparrow cuma akses info publiknya aja — kayak saldo, alamat, dan transaksi. Pendekatan ini jauh lebih aman dibandingkan Hot Wallet, karena private key disimpan di perangkat khusus (biasanya pakai chip keamanan), yang nggak terhubung ke internet. Artinya, risiko diretas jauh lebih kecil dibanding kalau disimpan di komputer biasa.

Ada dua cara utama untuk menghubungkan Hardware Wallet ke Sparrow:


- Dengan kabel, biasanya digunakan dengan model entry-level seperti Trezor Safe 3 atau Ledger Nano S Plus;
- Dalam mode Air-Gap, yaitu tanpa koneksi kabel langsung, melalui kartu MicroSD atau kode QR Exchange.

Sparrow mendukung semua metode komunikasi ini dan kompatibel dengan sebagian besar dompet perangkat keras yang ada di pasaran.

Di tutorial ini, aku bakal pakai Ledger Nano S yang disambung pakai kabel.
Tapi tenang aja, langkah-langkahnya kurang lebih sama kalau kamu pakai mode air-gap (nggak langsung nyambung ke komputer). Kalau kamu pakai hardware wallet lain, kamu bisa cek panduan khususnya di situs Plan ₿ Academy — di sana ada tutorial lengkap buat berbagai jenis device.

Sebelum mulai, pastikan wallet kamu udah dikonfigurasi di hardware wallet-nya.
Kalau kamu pakai koneksi kabel, cukup colokkan perangkat ke komputer pakai kabelnya.

Untuk mengimpor apa yang disebut "*Keystore*" (informasi publik yang diperlukan untuk mengelola portofolio) ke dalam Sparrow Wallet, klik pada tab "*File*", kemudian "*New Wallet*".

![Image](assets/fr/32.webp)

Beri nama portofolio Anda dan klik "*Buat Wallet*". Saya menyarankan Anda untuk memasukkan nama Hardware Wallet Anda untuk mengidentifikasinya dengan mudah nanti.

![Image](assets/fr/33.webp)

Di bagian atas tampilan, pilih jenis wallet yang mau kamu buat: Single Signature atau Multi Signature.
Untuk contoh kali ini, kita bakal pakai yang Single Signature dulu, alias cukup satu tanda tangan buat validasi transaksi.

Tepat di bawahnya, kamu bisa pilih jenis script buat ngunci UTXO (saldo Bitcoin kamu).
Kalau hardware wallet kamu mendukung, aku saranin pakai Taproot (P2TR) — ini standar terbaru yang lebih hemat biaya dan lebih ramah privasi.

![Image](assets/fr/34.webp)

Selanjutnya, langkahnya bakal sedikit beda tergantung kamu pakai metode koneksi yang mana.
Kalau kamu pakai mode Air-Gap (nggak nyambung langsung ke komputer), pilih opsi “Airgapped Hardware Wallet” di Sparrow.
Setelah itu, ikuti petunjuk sesuai dengan jenis perangkat yang kamu pakai — biasanya ada langkah scan QR, file PSBT, atau microSD, tergantung hardware wallet-nya.

![Image](assets/fr/35.webp)

Kalau kamu pakai koneksi kabel (seperti yang aku lakukan di tutorial ini), pilih opsi “Connected Hardware Wallet” di Sparrow.

![Image](assets/fr/36.webp)

Klik tombol "Scan" supaya Sparrow bisa mendeteksi hardware wallet kamu.
Pastikan perangkat udah dicolokkan dan nggak terkunci.
Untuk beberapa model kayak Ledger, kamu juga perlu buka dulu aplikasi Bitcoin di perangkatnya biar bisa terdeteksi dengan benar.

![Image](assets/fr/37.webp)

Pilih "*Import Keystore*".

![Image](assets/fr/38.webp)

Klik "*Apply*" untuk menyelesaikan pembuatan portofolio.

![Image](assets/fr/39.webp)

Sekarang, buat password yang kuat buat ngamanin akses ke Sparrow Wallet kamu.
Password ini bakal ngelindungin data seperti alamat, riwayat transaksi, dan kunci publik.
Biar nggak lupa, sebaiknya simpan di password manager yang aman.
Tapi perlu diingat: password ini nggak dipakai buat akses ke Bitcoin kamu secara langsung.
Bahkan tanpa password ini, kamu masih bisa pulihin wallet-mu pakai frasa Mnemonic lewat aplikasi lain yang support BIP39.

![Image](assets/fr/40.webp)

Sekarang portofolio kamu udah berhasil dikonfigurasi di Sparrow! 

![Image](assets/fr/41.webp)

## Menerima bitcoin

Setelah Wallet diatur di Sparrow, kamu bisa menerima bitcoin. Cukup akses menu "*Terima*".

![Image](assets/fr/42.webp)

Sparrow akan menampilkan Address pertama yang tidak terpakai dalam Wallet Anda. Anda bisa menambahkan "*Label*" ke Address ini untuk mengingatkan Anda tentang asal usul satoshi ini di kemudian hari.

![Image](assets/fr/43.webp)

Kalau kamu pakai Hot Wallet, alamat Bitcoin yang ditampilkan bisa langsung dipakai — tinggal salin atau scan kode QR-nya.
Kamu bisa kirim Bitcoin ke alamat ini tanpa perlu langkah tambahan.

Kalau kamu pakai Hardware Wallet, penting banget buat selalu cek alamatnya langsung di layar perangkat sebelum dipakai.
Kalau pakai koneksi kabel, sambungkan dan buka kunci hardware wallet kamu dulu.
Lalu, di Sparrow, klik tombol “Display Address”.
Pastikan alamat yang muncul di perangkat sama persis dengan yang ditampilkan di Sparrow. Ini buat mastiin kamu nggak kena tipu atau dialihkan ke alamat palsu.

![Image](assets/fr/44.webp)

Kalau kamu pakai Hardware Wallet yang air-gap (nggak nyambung langsung ke komputer), cara verifikasi alamatnya bisa beda-beda tergantung jenis perangkat.
Untuk langkah-langkah pastinya, kamu bisa cek tutorial khusus dari Plan ₿ Academy yang sesuai dengan model hardware wallet kamu.

Begitu pengirim udah menyelesaikan transaksinya, kamu bakal lihat transaksinya muncul di tab "Transaksi".
Kamu bisa klik transaksi itu buat lihat detail lengkapnya — kayak jumlah, status konfirmasi, dan juga TXID (ID transaksinya).


![Image](assets/fr/45.webp)

Di tab "Alamat", kamu bisa lihat daftar semua alamat wallet kamu.
Di situ kelihatan mana aja yang udah pernah dipakai, dan apakah udah kamu kasih label atau belum.
Alamat "Terima" adalah alamat yang ditampilkan waktu kamu klik tombol "Terima". Ini dipakai buat nerima pembayaran masuk.
Alamat "Change" dipakai secara otomatis waktu kamu kirim Bitcoin. Ini buat nyimpen “kembalian” dari UTXO yang nggak kepakai semua — semacam sisa saldo dari transaksi kamu.

![Image](assets/fr/46.webp)

Tab "UTXOs" nunjukin semua potongan Bitcoin (UTXO) yang kamu punya.
Setiap UTXO itu semacam fragmen saldo dari transaksi sebelumnya, dan bisa kamu lihat jumlahnya satu per satu.
Kamu juga bisa lihat label yang udah kamu kasih buat tiap UTXO — ini ngebantu banget buat ngelacak asal-usul dana atau tujuan penggunaannya.

![Image](assets/fr/47.webp)

## Kirim bitcoin

Sekarang kamu udah punya beberapa satoshi di wallet, kamu juga bisa coba kirim sebagian.
Memang ada beberapa cara buat kirim Bitcoin, tapi aku saranin pakai menu "UTXOs" biar kamu punya kontrol penuh atas koin mana yang mau dipakai (ini yang disebut coin control).
Kalau kamu masih pemula dan pengen yang simpel, pakai menu "Kirim" juga nggak masalah — tinggal masukin alamat tujuan dan jumlahnya aja.

![Image](assets/fr/48.webp)

Pilih UTXO yang mau kamu pakai buat transaksi, lalu klik "Kirim Terpilih".
Cara ini bikin kamu bisa milih sumber dana paling pas dari saldo-saldo kecil (UTXO) yang kamu punya — bisa disesuaiin sama tujuan pengeluaran dan label yang udah kamu kasih sebelumnya. Ini juga bantu ningkatin privasi saat bayar.
Cuma pastikan ya, jumlah UTXO yang kamu pilih harus lebih besar dari jumlah yang mau kamu kirim.

![Image](assets/fr/49.webp)

Masukkan alamat tujuan di kolom "Bayar ke".
Kalau kamu punya QR code, bisa juga langsung scan pakai webcam — tinggal klik ikon kamera di samping kolom itu.
Mau kirim ke lebih dari satu alamat dalam satu transaksi? Tinggal klik tombol “+Tambah” buat nambah baris penerima lainnya.

![Image](assets/fr/50.webp)

Tambahin label di transaksimu biar kamu ingat ini transaksi buat apa.
Misalnya: “Kirim ke wallet cold storage” atau “Bayar kopi via Lightning”.
Label ini juga bakal otomatis nempel ke UTXO hasil transaksinya, jadi bakal kebaca terus ke depannya.
Kalau ini transaksi ke atau dari exchange, kasih label nama exchangenya juga ya — ini bantu banget buat tracking portofolio nanti.

![Image](assets/fr/51.webp)

Masukkan jumlah yang akan dikirim ke Address ini.

![Image](assets/fr/52.webp)

Sesuaikan tingkat biaya sesuai dengan kondisi pasar saat ini. Kamu dapat melakukannya dengan memasukkan nilai biaya yang pasti atau dengan menyesuaikan tarif biaya dengan penggeser.

![Image](assets/fr/53.webp)

Di bagian bawah tampilan, kamu bisa pilih antara mode “Efficiency” atau “Privacy” buat transaksi kamu.
Efficiency cocok buat transaksi biasa — hemat ruang, cepat, dan biaya rendah.
Privacy (kalau tersedia) bakal bikin struktur transaksi kamu jadi mirip CoinJoin kecil — disebut Stonewall. Ini bantu banget ningkatin privasi karena bikin analisis blockchain jadi lebih ribet.
Tapi di contoh ini, karena aku cuma punya satu UTXO, opsi Privacy nggak muncul.
Kalau kamu punya lebih banyak UTXO, fitur ini bisa kamu manfaatin.

![Image](assets/fr/54.webp)

Sparrow bakal nampilin diagram ringkasan transaksi — di situ kamu bisa lihat input, output, dan fee-nya.
Perlu dicatat: biaya transaksi itu bukan bagian dari output, walaupun di diagram keliatannya begitu. Itu cuma visual bantu aja.
Kalau semuanya udah sesuai dan kamu puas, tinggal klik tombol “Buat Transaksi” buat lanjut ke langkah berikutnya.

![Image](assets/fr/55.webp)

Setelah itu, kamu bakal dibawa ke halaman yang nunjukin detail lengkap dari transaksi kamu.
Luangkan waktu sebentar buat periksa semua elemennya — mulai dari alamat tujuan, jumlah, sampai fee-nya.
Kalau semuanya udah oke, klik tombol “Finalisasi Transaksi untuk Penandatanganan” buat masuk ke tahap tanda tangan.

![Image](assets/fr/56.webp)

Sangat penting untuk mempertahankan Sighash default.
Untuk tahu kenapa ini penting, kamu bisa cek kursus pelatihan ini — di situ aku jelasin semua yang perlu kamu tahu soal Sighash:

https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

Di layar berikutnya, opsi yang muncul bisa beda-beda tergantung jenis Wallet yang kamu pakai:


- Untuk Hardware Wallet Air-Gap, klik "Show QR" untuk menampilkan PSBT yang dapat kamu tandatangani dengan perangkatmu, lalu muat PSBT yang telah ditandatangani ke dalam Sparrow menggunakan "Scan QR". Opsi "Save Transaction" bekerja dengan cara yang sama, tetapi dengan penukaran pada microSD;
- Kalau pakai Hot Wallet, kamu tinggal klik "Sign" lalu masukin kata sandi Wallet kamu buat tandatangan.
- Kalau pakai Hardware Wallet yang pakai kabel, klik juga "*Sign*" buat ngirim transaksi yang belum ditandatangani ke perangkat kamu.

![Image](assets/fr/57.webp)

Di Hardware Wallet kamu, cek dulu alamat penerima, jumlah yang mau dikirim, dan biayanya. Kalau semuanya udah oke, tinggal lanjut tanda tangan.

Setelah transaksi ditandatangani, nanti bakal muncul lagi di Sparrow, siap buat dikirim ke jaringan Bitcoin dan masuk ke blok berikutnya. Kalau semuanya udah bener, tinggal klik "Broadcast Transaction".

![Image](assets/fr/58.webp)

Transaksi kamu sekarang udah dikirim dan lagi menunggu konfirmasi.

![Image](assets/fr/59.webp)

## Mengelola dan mengonfigurasi portofolio di Sparrow

Pada tab "*Settings*", kamu akan menemukan informasi rinci mengenai portofoliomu, misalnya, :


- Jenis portofolio (single-sig atau multi-sig);
- Jenis skrip yang digunakan ;
- Nama yang sudah kamu tetapkan ke portofolio ;
- Jejak kunci utama;
- Jalur pintas ;
- Kunci publik akun yang diperpanjang.

![Image](assets/fr/60.webp)

Tombol "Export" bisa kamu pakai buat nyimpen info portofolio, jadi nanti bisa dipakai di software lain tanpa kehilangan pengaturan yang udah kamu atur di Sparrow.

Tombol "Tambah Akun" memungkinkan kamu nambahin akun baru ke portofolio. Tiap akun punya set alamatnya sendiri. Fitur ini berguna banget misalnya kalau kamu mau pisahin akun pribadi dan bisnis, tapi tetap pakai satu frasa Mnemonic.

Tombol "Advanced" ngasih kamu akses ke pengaturan lanjutan, kayak ngatur cara Sparrow nyari alamat atau ganti kata sandi portofolio.

![Image](assets/fr/61.webp)

Waktu kamu nutup Sparrow Wallet, dompetnya bakal ngunci otomatis. Pas kamu buka lagi, bakal muncul jendela yang minta kamu masukin kata sandi buat buka kuncinya.

![Image](assets/fr/62.webp)

Kalau jendela itu nggak muncul, atau kamu mau buka portofolio lain di Sparrow, klik tab "File" lalu pilih "Open Wallet".

![Image](assets/fr/63.webp)

Ini bakal ngebuka File Manager ke folder tempat Sparrow nyimpen dompet-dompet kamu. Tinggal pilih Wallet yang mau dibuka, lalu masukin kata sandinya.

![Image](assets/fr/64.webp)

Di menu "File" bagian "Settings", kamu bisa nemuin pengaturan koneksi jaringan Bitcoin yang udah dibahas sebelumnya. Di situ juga kamu bisa ngatur hal-hal lain kayak satuan yang dipakai, mata uang fiat buat konversi, dan sumber data yang dipakai.

![Image](assets/fr/65.webp)

Tab "Lihat" nyediain opsi buat kustomisasi tampilan dan akses ke beberapa perintah penting, kayak "Refresh Wallet" yang bisa nyegerin pencarian transaksi di portofolio kamu.

![Image](assets/fr/66.webp)

Tab "Tools" ngumpulin beberapa alat bantu canggih, di antaranya:


- "*Tanda Tangan/Verifikasi Pesan*" memungkinkanmu untuk membuktikan kepemilikan Address yang diterima atau memverifikasi tanda tangan.
- "*Kirim Ke Banyak*" menawarkan Interface yang disederhanakan untuk melakukan transaksi ke beberapa alamat penerima sekaligus, yang nyaman untuk pengeluaran batch.
- "*Sweep Private Key*" memungkinkanmu untuk mengambil bitcoin yang diamankan dengan private key sederhana dan mentransfernya ke Sparrow Wallet. Ini bisa sangat berguna bagi mereka yang memiliki bitcoin yang berasal dari awal tahun 2010, sebelum era dompet HD.
- "Verifikasi Unduhan" memverifikasi integritas dan keaslian perangkat lunak yang diunduh sebelum menginstalnya pada perangkatmu.
- "*Restart In*" memungkinkanmu untuk beralih ke dompetmu di jaringan Testnet atau Signet. Ini dapat berguna jika kamu ingin mengakses jaringan uji coba dengan koin yang tidak memiliki nilai.

![Image](assets/fr/67.webp)

Sekarang Kamu sudah mengetahui semua tentang perangkat lunak Sparrow Wallet, alat yang sangat baik untuk mengelola portofolio Bitcoin milikmu setiap hari.

Jika kamu merasa tutorial ini bermanfaat, kami akan sangat berterima kasih jika kamu memberikan jempol Green di bawah ini. Jangan ragu untuk membagikannya di media sosial. Terima kasih banyak!

Kami juga merekomendasikan tutorial lain yang menjelaskan cara mengonfigurasi Hardware Wallet COLDCARD Q dengan Sparrow Wallet:

https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3