---
name: Sparrow Wallet
description: Cara menginstal, mengatur, dan menggunakan Sparrow Wallet.
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

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

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

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

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

*dengan remote Bitcoin Core: ** Dengan remote Bitcoin Core:**

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

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/26.webp)

**Jelas ya, frasa 12 kata ini nggak boleh dibagikan di internet — beda sama yang aku lakukan di tutorial ini.
Wallet ini cuma contoh, dan cuma dipakai di Testnet (bukan jaringan Bitcoin asli).
Nanti juga bakal dihapus setelah tutorial selesai. Jadi ingat, jangan pernah bagikan frasa wallet asli kamu ke siapa pun, apalagi online.**

Kamu juga bisa nambahin passphrase BIP39 dengan centang kotak “Use passphrase”.
Fitur ini bisa bikin wallet kamu jauh lebih aman, tapi hati-hati — kalau kamu nggak ngerti cara kerjanya, risikonya bisa besar. Makanya, aku saranin banget buat baca dulu penjelasan singkat tentang teori di balik passphrase ini sebelum kamu pakai.

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

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
Tapi tenang aja, langkah-langkahnya kurang lebih sama kalau kamu pakai mode air-gap (nggak langsung nyambung ke komputer). Kalau kamu pakai hardware wallet lain, kamu bisa cek panduan khususnya di situs Plan ₿ Network — di sana ada tutorial lengkap buat berbagai jenis device.

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

Selanjutnya, prosedurnya berbeda menurut metode koneksi Anda. Jika Anda menggunakan metode Celah Udara, pilih "*Airgapped Hardware Wallet*". Kemudian ikuti petunjuk khusus untuk perangkat Anda.

![Image](assets/fr/35.webp)

Jika Anda menggunakan koneksi kabel, seperti dalam kasus saya, pilih "*Connected Hardware Wallet*".

![Image](assets/fr/36.webp)

Klik "*Scan*" untuk meminta Sparrow mendeteksi perangkat Anda. Pastikan perangkat sudah dicolokkan dan tidak terkunci. Untuk beberapa model, seperti Ledger, Anda harus membuka aplikasi "*Bitcoin*" untuk mengaktifkan pendeteksian.

![Image](assets/fr/37.webp)

Pilih "*Import Keystore*".

![Image](assets/fr/38.webp)

Klik "*Apply*" untuk menyelesaikan pembuatan portofolio.

![Image](assets/fr/39.webp)

Tetapkan kata sandi yang kuat untuk mengamankan akses ke Sparrow Wallet Anda. Kata sandi ini akan melindungi kunci publik, alamat, dan riwayat transaksi Anda. Kami sarankan anda menyimpannya dalam sebuah pengelola kata sandi. Perhatikan bahwa kata sandi ini tidak berperan dalam penurunan kunci Anda. Bahkan tanpa kata sandi ini, Anda dapat memulihkan akses ke bitcoin Anda dengan Mnemonic melalui perangkat lunak yang kompatibel dengan BIP39.

![Image](assets/fr/40.webp)

Portofolio manajemen Anda sekarang dikonfigurasikan di Sparrow.

![Image](assets/fr/41.webp)

## Menerima bitcoin

Setelah Wallet Anda diatur di Sparrow, Anda bisa menerima bitcoin. Cukup akses menu "*Terima*".

![Image](assets/fr/42.webp)

Sparrow akan menampilkan Address pertama yang tidak terpakai dalam Wallet Anda. Anda bisa menambahkan "*Label*" ke Address ini untuk mengingatkan Anda tentang asal usul satoshi ini di kemudian hari.

![Image](assets/fr/43.webp)

Jika Anda menggunakan Hot Wallet, Address yang ditampilkan dapat langsung digunakan, baik dengan menyalinnya atau dengan memindai kode QR terkait.

Jika Anda menggunakan Hardware Wallet, sangat penting untuk memeriksa Address pada layar perangkat sebelum menggunakannya. Untuk perangkat berkabel, hubungkan dan buka kunci Hardware Wallet Anda, kemudian di Sparrow, klik "*Display Address*". Pastikan Address yang ditampilkan pada Hardware Wallet Anda sesuai dengan yang ditampilkan pada Sparrow.

![Image](assets/fr/44.webp)

Untuk pengguna Hardware Wallet Air-Gap, verifikasi Address bervariasi menurut model perangkat. Lihat tutorial khusus Plan ₿ Network untuk mendapatkan instruksi yang tepat.

Setelah transaksi disiarkan oleh pembayar, Anda akan melihatnya muncul di tab "*Transaksi*". Anda dapat mengkliknya untuk detail lebih lanjut, seperti txid.

![Image](assets/fr/45.webp)

Pada tab "*Alamat*", Anda akan menemukan daftar semua alamat kotak masuk Anda. Anda dapat melihat apakah alamat-alamat tersebut telah digunakan dan apakah label telah ditambahkan. *Alamat "*Terima*" adalah alamat yang ditampilkan Sparrow ketika Anda mengklik "*Terima*" dan ditujukan untuk pembayaran yang masuk. Alamat "*Change*" digunakan untuk Exchange dalam transaksi Anda, yaitu untuk mengembalikan bagian yang tidak terpakai dari UTXO Anda yang masuk.

![Image](assets/fr/46.webp)

Tab "*UTXOs*" menunjukkan kepada Anda semua UTXO Anda, yaitu fragmen Bitcoin yang Anda pegang. Anda dapat melihat jumlah setiap UTXO dan label yang terkait.

![Image](assets/fr/47.webp)

## Kirim bitcoin

Sekarang setelah Anda memiliki beberapa satoshi di Wallet Anda, Anda juga memiliki opsi untuk mengirim beberapa. Meskipun ada beberapa cara untuk melakukan ini, saya sarankan Anda menggunakan menu "*UTXOs*" untuk kontrol yang lebih tepat terhadap koin yang Anda belanjakan (*kontrol koin*), daripada langsung ke menu "*Kirim*" (meskipun menu yang terakhir ini mungkin sudah cukup untuk Anda jika Anda seorang pemula).

![Image](assets/fr/48.webp)

Pilih UTXO yang ingin Anda gunakan sebagai input untuk transaksi ini, lalu klik "*Kirim Terpilih*". Pendekatan ini memungkinkan Anda untuk memilih sumber yang paling tepat di antara UTXO Anda, sesuai dengan pengeluaran Anda dan label yang diterapkan saat diterima, untuk mengoptimalkan kerahasiaan pembayaran Anda. Pastikan jumlah UTXO yang dipilih lebih besar dari jumlah yang ingin Anda kirim.

![Image](assets/fr/49.webp)

Masukkan Address penerima di kolom "*Bayar ke*". Anda juga dapat memindai Address dengan webcam dengan mengklik ikon kamera. Tombol "*+Tambah*" memungkinkan Anda membayar ke beberapa alamat dalam satu transaksi.

![Image](assets/fr/50.webp)

Tambahkan label pada transaksi Anda untuk mengingatkan Anda tentang tujuannya. Label ini juga akan dikaitkan dengan Exchange Anda nantinya.

![Image](assets/fr/51.webp)

Masukkan jumlah yang akan dikirim ke Address ini.

![Image](assets/fr/52.webp)

Sesuaikan tingkat biaya sesuai dengan kondisi pasar saat ini. Anda dapat melakukannya dengan memasukkan nilai biaya absolut atau dengan menyesuaikan tarif biaya dengan penggeser.

![Image](assets/fr/53.webp)

Pada bagian bawah Interface, Anda dapat memilih antara "*Efficiency*" dan "*Privacy*". Dalam kasus saya, opsi "*Privacy*" tidak tersedia, karena saya hanya memiliki satu UTXO dalam portofolio ini. "*Efficiency*" berhubungan dengan transaksi klasik, sedangkan "*Privacy*" adalah transaksi tipe Stonewall, struktur transaksi yang memperkuat kerahasiaan Anda dengan mensimulasikan mini-CoinJoin, yang membuat analisis rantai menjadi lebih kompleks.

![Image](assets/fr/54.webp)

Sparrow menampilkan diagram ringkasan yang menunjukkan input, output, dan biaya transaksi Anda (perhatikan bahwa biaya sebenarnya bukanlah output, berlawanan dengan apa yang ditunjukkan oleh diagram ini). Jika Anda puas dengan semuanya, klik "*Buat Transaksi*".

![Image](assets/fr/55.webp)

Anda akan dibawa ke halaman yang merinci Elements dari transaksi Anda. Periksa apakah semua informasi sudah benar, lalu klik "*Finalisasi Transaksi untuk Penandatanganan*".

![Image](assets/fr/56.webp)

Sangat penting untuk mempertahankan Sighash default. Untuk memahami alasannya, lihatlah kursus pelatihan ini, di mana saya menjelaskan semua yang perlu Anda ketahui tentang Sighash:

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

Pada layar berikutnya, opsi bervariasi menurut tipe Wallet yang Anda gunakan:


- Untuk Hardware Wallet Air-Gap, klik "*Show QR*" untuk menampilkan PSBT yang dapat Anda tandatangani dengan perangkat Anda, lalu muat PSBT yang telah ditandatangani ke dalam Sparrow menggunakan "*Scan QR*". Opsi "*Save Transaction*" bekerja dengan cara yang sama, tetapi dengan penukaran pada microSD;
- Untuk Hot Wallet, cukup klik "*Sign*" dan masukkan kata sandi Wallet untuk menandatangani;
- Untuk Hardware Wallet berkabel, klik juga "*Sign*" untuk mengirim transaksi yang belum ditandatangani ke perangkat Anda.

![Image](assets/fr/57.webp)

Pada Hardware Wallet Anda, periksa Address penerima, jumlah yang dikirim, dan biaya. Jika semuanya sudah benar, lanjutkan dengan tanda tangan.

Setelah transaksi ditandatangani, transaksi tersebut akan muncul kembali di Sparrow, siap untuk disiarkan di jaringan Bitcoin untuk dimasukkan ke dalam blok berikutnya. Jika semuanya sudah benar, klik "*Broadcast Transaction*".

![Image](assets/fr/58.webp)

Transaksi Anda sekarang disiarkan dan menunggu konfirmasi.

![Image](assets/fr/59.webp)

## Mengelola dan mengonfigurasi portofolio di Sparrow

Pada tab "*Settings*", Anda akan menemukan informasi rinci mengenai portofolio Anda, misalnya, :


- Jenis portofolio (single-sig atau multi-sig);
- Jenis skrip yang digunakan ;
- Nama yang sudah Anda tetapkan ke portofolio ;
- Jejak kunci utama;
- Jalur pintas ;
- Kunci publik akun yang diperpanjang.

![Image](assets/fr/60.webp)

Tombol "*Export*" memungkinkan Anda untuk mengekspor informasi portofolio Anda sehingga Anda dapat menggunakannya di perangkat lunak lain sambil mempertahankan informasi yang telah diatur di Sparrow.

Tombol "*Tambah Akun*" memungkinkan Anda menambahkan akun tambahan ke portofolio Anda. Sebuah akun berhubungan dengan seperangkat alamat kotak masuk yang terpisah. Fitur ini dapat berguna, misalnya, jika Anda ingin memisahkan akun pribadi dan akun bisnis, dengan satu frasa Mnemonic.

Tombol "*Advanced*" memberikan akses ke pengaturan lanjutan, seperti menyesuaikan pencarian Address Sparrow dan mengubah kata sandi portofolio.

![Image](assets/fr/61.webp)

Ketika Anda menutup Sparrow Wallet, Wallet Anda akan terkunci secara otomatis. Saat berikutnya Anda membuka perangkat lunak, sebuah jendela akan meminta Anda untuk membuka kunci Wallet dengan kata sandinya.

![Image](assets/fr/62.webp)

Jika jendela ini tidak terbuka, atau jika Anda ingin membuka portofolio lain di Sparrow, klik tab "*File*" dan pilih "*Open Wallet*".

![Image](assets/fr/63.webp)

Ini akan membuka File Manager Anda ke folder tempat Sparrow menyimpan dompet Anda. Cukup pilih Wallet yang ingin Anda buka dan masukkan kata sandi untuk membukanya.

![Image](assets/fr/64.webp)

Pada menu "*File*" di bawah "*Settings*", Anda akan menemukan parameter koneksi jaringan Bitcoin yang telah dieksplorasi pada bagian sebelumnya. Anda juga dapat menyesuaikan berbagai parameter seperti unit yang digunakan, mata uang fiat untuk konversi, dan sumber informasi.

![Image](assets/fr/65.webp)

Tab "*Lihat*" menawarkan opsi kustomisasi dan akses ke beberapa perintah yang berguna, seperti "*Refresh Wallet*", yang menyegarkan pencarian transaksi untuk portofolio Anda.

![Image](assets/fr/66.webp)

Tab "*Tools*" mengelompokkan beberapa alat bantu canggih, termasuk :


- "*Tanda Tangan/Verifikasi Pesan*" memungkinkan Anda untuk membuktikan kepemilikan Address yang diterima atau memverifikasi tanda tangan.
- "*Kirim Ke Banyak*" menawarkan Interface yang disederhanakan untuk melakukan transaksi ke beberapa alamat penerima sekaligus, yang nyaman untuk pengeluaran batch.
- "*Sweep Private Key*" memungkinkan Anda untuk mengambil bitcoin yang diamankan dengan private key sederhana dan mentransfernya ke Sparrow Wallet Anda. Ini bisa sangat berguna bagi mereka yang memiliki bitcoin yang berasal dari awal tahun 2010, sebelum era dompet HD.
- "Verifikasi Unduhan" memverifikasi integritas dan keaslian perangkat lunak yang diunduh sebelum menginstalnya pada perangkat Anda.
- "*Restart In*" memungkinkan Anda untuk beralih ke dompet Anda di jaringan Testnet atau Signet. Ini dapat berguna jika Anda ingin mengakses jaringan uji coba dengan koin yang tidak memiliki nilai.

![Image](assets/fr/67.webp)

Sekarang Anda sudah mengetahui semua tentang perangkat lunak Sparrow Wallet, alat yang sangat baik untuk mengelola portofolio Bitcoin Anda setiap hari.

Jika Anda merasa tutorial ini bermanfaat, saya akan sangat berterima kasih jika Anda memberikan jempol Green di bawah ini. Jangan ragu untuk membagikannya di jejaring sosial Anda. Terima kasih banyak!

Saya juga merekomendasikan tutorial lain yang menjelaskan cara mengonfigurasi Hardware Wallet COLDCARD Q dengan Sparrow Wallet:

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3
