---
name: Sparrow Wallet
description: Menginstal, mengonfigurasi, dan menggunakan Sparrow Wallet
---
![cover](assets/cover.webp)

Sparrow Wallet adalah perangkat lunak manajemen portofolio Bitcoin yang dikembangkan oleh Craig Raw. Perangkat lunak sumber terbuka ini dihargai oleh para bitcoiners karena banyak fitur dan Interface yang intuitif.

Ada dua cara untuk menggunakan Sparrow:


- Seperti hot wallet, di mana private key kamu disimpan di komputer kamu.
- Sebagai pengelola cold wallet, di mana private key disimpan di hardware wallet. Dalam mode ini, Sparrow hanya mengelola informasi publik dari wallet, melacak saldo, membuat alamat, dan menyiapkan transaksi. Namun, tanda tangan dari hardware wallet tetap dibutuhkan agar transaksi tersebut valid. Karena itu, Sparrow bisa menggantikan aplikasi seperti Ledger Live atau Trezor Suite.

Sparrow mendukung wallet dengan single-signature maupun multisignature, dan memungkinkan kamu mengelola beberapa wallet sekaligus dengan mudah. Misalnya, kamu bisa mengontrol satu wallet yang terhubung ke Ledger, satu lagi ke Trezor, dan juga punya hot wallet di saat yang sama.

Software ini juga menawarkan fitur coin control yang canggih, memungkinkan kamu memilih dengan tepat UTXO mana yang mau dipakai dalam transaksi untuk mengoptimalkan privasi kamu.

Untuk koneksi, Sparrow memungkinkan kamu terhubung ke node Bitcoin milikmu sendiri, baik dari jarak jauh lewat server Electrum maupun langsung dengan Bitcoin Core. Kamu juga bisa pakai node publik kalau belum punya node sendiri. Koneksi jarak jauh dilakukan lewat Tor.

## Pasang Sparrow Wallet

Buka [halaman unduhan resmi Sparrow Wallet] (https://sparrowwallet.com/download/) dan pilih versi perangkat lunak yang sesuai dengan sistem operasi kamu.

![Image](assets/fr/01.webp)

Penting untuk memeriksa integritas dan keaslian software sebelum menginstalnya. Kalau kamu belum tahu caranya, kamu bisa menemukan tutorial lengkapnya di sini:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Setelah Sparrow terinstal, kamu bisa melewatkan layar penjelasan awal dan langsung menuju ke layar manajemen koneksi.

![Image](assets/fr/02.webp)

## Menghubungkan ke jaringan Bitcoin

Untuk berinteraksi dengan jaringan Bitcoin dan menyiarkan transaksi kamu, Sparrow harus terhubung ke node Bitcoin. Ada tiga cara utama untuk membuat koneksi ini:


- 🟡 Menggunakan node publik, yaitu terhubung ke node milik pihak ketiga yang membuka koneksi untuk umum. Kalau kamu belum punya node Bitcoin sendiri, opsi ini memungkinkan kamu untuk mulai menggunakan Sparrow dengan cepat. Tapi, node yang kamu sambungkan akan bisa melihat semua transaksi kamu, yang bisa mengurangi privasi kamu. Mengontrol private key itu penting, tapi punya node sendiri jauh lebih baik. Jadi, pakai opsi ini hanya saat kamu baru mulai, sambil tetap sadar akan risiko privasinya.
- 🟢 Menghubungkan ke node Bitcoin Core. Kalau kamu punya node Bitcoin Core sendiri, kamu bisa menyambungkannya ke Sparrow Wallet, baik secara lokal kalau Bitcoin Core terpasang di komputer yang sama, atau dari jarak jauh.
- 🔵 Koneksi melalui server Electrum. Jika node Bitcoin Anda dilengkapi dengan Electrs, seperti halnya dengan solusi node-in-a-box seperti Umbrel atau Start9, kamu bisa menyambungkannya dari jarak jauh dari Sparrow.

**Lebih baik menggunakan koneksi melalui Electrs atau Bitcoin Core pada node milikmu sendiri untuk mengurangi kebutuhan untuk mempercayai pihak ketiga dan mengoptimalkan kerahasiaan Anda**

### Terhubung ke simpul publik 🟡

Menghubungkan ke node publik sangat sederhana. Klik pada tab "*Public Server*".

![Image](assets/fr/03.webp)

Pilih node dari daftar tarik-turun.

![Image](assets/fr/04.webp)

Kemudian klik "*Test Connection*".

![Image](assets/fr/05.webp)

Setelah terhubung, Sparrow Wallet akan menampilkan tanda centang kuning di pojok kanan bawah antarmuka untuk menunjukkan bahwa kamu terhubung ke node publik.

![Image](assets/fr/06.webp)

### Menghubungkan ke Bitcoin Core 🟢

Metode kedua untuk terhubung ke node Bitcoin adalah dengan menghubungkan Sparrow ke Bitcoin Core. Kalau Bitcoin Core terpasang di komputer yang sama, proses autentikasi akan dilakukan lewat file cookie. Tapi kalau Bitcoin Core ada di komputer lain, kamu perlu menggunakan password yang sudah ditetapkan di file `bitcoin.conf`.

Perlu diingat, kalau kamu memakai node Bitcoin Core yang dipangkas (pruned), kamu nggak akan bisa memulihkan wallet yang punya transaksi sebelum blok-blok yang tersimpan secara lokal. Tapi untuk wallet baru yang dibuat langsung di Sparrow, hal ini nggak jadi masalah, karena transaksi barumu tetap akan terlihat, bahkan dengan pruned node.

Untuk mengonfigurasi node Bitcoin Core, Anda dapat membaca salah satu tutorial berikut, tergantung pada sistem operasi Anda:

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

Pada Sparrow, buka tab "*Bitcoin Core*".

![Image](assets/fr/07.webp)

**Dengan Bitcoin Core lokal:**

Jika Bitcoin Core terinstal di komputer kamu, cari file `Bitcoin.conf` di antara file perangkat lunak. Kalau file ini tidak ada, kamu bisa membuatnya. Buka file tersebut dengan editor teks dan masukkan baris berikut:

```ini
server=1
```

Kemudian simpan perubahan bisa.

Kamu juga bisa  melakukan ini melalui grafik Bitcoin-QT's Interface dengan menavigasi ke "*Settings*" > "*Options...*" dan mengaktifkan opsi "*Enable RPC server*".

Jangan lupa untuk memulai ulang perangkat lunak setelah melakukan perubahan ini.

![Image](assets/fr/08.webp)

Kemudian kembali ke Sparrow Wallet dan masukkan jalur ke file cookie, biasanya terletak di folder yang sama dengan `Bitcoin.conf`, tergantung pada sistem operasi kamu:

| **macOS** | ~/Perpustakaan/Dukungan Aplikasi/Bitcoin |

| ----------- | ------------------------------------- |

| **Windows** | %APPDATA%\Bitcoin |

| **Linux** | ~/.Bitcoin |

![Image](assets/fr/09.webp)

Biarkan parameter lain sebagai default, URL `127.0.0.1` dan port `8332`, lalu klik "*Test Connection*".

![Image](assets/fr/10.webp)

Sambungan telah dibuat. Tanda centang Green akan muncul di sudut kanan bawah untuk menunjukkan bahwa kamu terhubung ke node Bitcoin Core.

![Image](assets/fr/11.webp)

*dengan remote Bitcoin Core: ** Dengan remote Bitcoin Core:**

Jika Bitcoin Core diinstal pada mesin lain yang terhubung ke jaringan yang sama, pertama-tama cari file `Bitcoin.conf` di antara file perangkat lunak. Jika file ini belum ada, kamu dapat membuatnya. Buka file ini dengan editor teks dan tambahkan baris berikut:

```ini
server=1
```

Setelah mengedit file, pastikan kamu menyimpannya dalam folder yang sesuai untuk sistem operasi Anda:

| **macOS** | ~/Perpustakaan/Dukungan Aplikasi/Bitcoin |

| ----------- | ------------------------------------- |

| **Windows** | %APPDATA%\Bitcoin |

| **Linux** | ~/.Bitcoin |

Operasi ini juga dapat dilakukan melalui Bitcoin-QT Interface grafis Interface. Buka menu "*Settings*", kemudian "*Options...*", dan aktifkan opsi "*Enable RPC server*" dengan mencentang kotak yang sesuai. Jika file `Bitcoin.conf` tidak ada, kamu bisa membuatnya langsung dari Interface ini dengan mengklik "*Open Configuration File*".

![Image](assets/fr/12.webp)

Temukan IP Address dari mesin yang menghosting Bitcoin Core di jaringan lokal. Untuk melakukan ini, kamu bisa menggunakan alat seperti [Angry IP Scanner] (https://angryip.org/). Mari kita asumsikan, untuk kepentingan argumen, bahwa IP Address dari node adalah `192.168.1.18`.

Dalam berkas `Bitcoin.conf`, tambahkan baris berikut, atur `rpcbind=192.168.1.18` untuk mencocokkan IP Address node kamu.

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

Sekarang kamu bisa kembali ke Sparrow Wallet. Buka tab "*User / Pass*". Masukkan nama pengguna dan kata sandi yang kamu konfigurasikan dalam file `Bitcoin.conf`. Biarkan parameter lainnya sebagai default, yaitu URL `127.0.0.1` dan port `8332`. Kemudian klik "*Test Connection*".

![Image](assets/fr/15.webp)

Sambungan telah dibuat. Tanda centang Green akan muncul di sudut kanan bawah untuk mengindikasikan bahwa Anda tersambung ke node Bitcoin Core.

![Image](assets/fr/16.webp)

### Menghubungkan ke server Electrum 🔵

Opsi terakhir untuk menyambung adalah dengan menggunakan server Electrum jarak jauh. Metode ini memungkinkan kamu terhubung ke node milikmu melalui Tor dari perangkat lain, dan memanfaatkan pengindeks untuk menelusuri portofolio kamu di Sparrow dengan lebih cepat. Metode ini sangat cocok jika Anda memiliki solusi node-in-a-box seperti Umbrel atau Start9, yang memungkinkan kamu untuk menginstal Electrs dengan satu klik.

Untuk melakukan ini, dapatkan Tor `.onion' Address dari server Electrum milikmu. Dengan Umbrel, misalnya, kamu akan menemukannya di aplikasi Electrs.

![Image](assets/fr/17.webp)

Pada Sparrow Wallet, akses tab "*Private Electrum*".

![Image](assets/fr/18.webp)

Masukkan Tor Address kamu di tempat yang disediakan. Pengaturan lainnya bisa tetap default. Kemudian klik "*Test Connection*".

![Image](assets/fr/19.webp)

Koneksi telah dikonfirmasi. Kalau kamu menutup jendela ini, tanda centang biru akan muncul di sudut kanan bawah, yang menunjukkan bahwa kamu terhubung ke server Electrum.

![Image](assets/fr/20.webp)

## Buat portofolio yang hangat

Setelah Sparrow Wallet dikonfigurasi untuk terhubung ke jaringan Bitcoin, kamu siap membuat wallet pertamamu. Di bagian ini, kamu akan belajar cara membuat hot wallet, yaitu wallet yang private key-nya disimpan di komputer kamu. Karena komputer adalah perangkat yang kompleks dan terhubung ke internet, permukaan serangannya sangat besar. Karena itu, hot wallet sebaiknya hanya dipakai untuk menyimpan bitcoin dalam jumlah kecil. Untuk jumlah yang lebih besar, pilih wallet yang lebih aman dengan hardware wallet. Kalau itu yang kamu butuhkan, kamu bisa langsung lanjut ke bagian berikutnya.

Untuk membuat Hot Wallet, dari layar beranda Sparrow Wallet, klik tab "*File*" dan kemudian "*New Wallet*".

![Image](assets/fr/21.webp)

Masukkan nama untuk portofolio kamu dan klik "*Buat Wallet*".

![Image](assets/fr/22.webp)

Di bagian atas Interface, kamu bisa memilih apakah akan membuat portofolio "*Single Signature*" atau "*Multi Signature*". Tepat di bawahnya, pilih jenis skrip untuk mengunci UTXO kamu. Aku sarankan kamu menggunakan standar terbaru: "*Taproot (P2TR)*".

![Image](assets/fr/23.webp)

Kemudian klik "*Software Wallet Baru atau Impor*".

![Image](assets/fr/24.webp)

Pilih standar BIP39, karena standar ini didukung oleh hampir semua perangkat lunak portofolio Bitcoin. Selanjutnya, pilih panjang frasa pemulihan kamu. Saat ini, frasa 12 kata sudah cukup, karena keduanya menawarkan keamanan yang serupa, tetapi frasa 12 kata lebih sederhana untuk disimpan.

![Image](assets/fr/25.webp)

Klik tombol “*Generate New*” untuk membuat seedphrase wallet kamu. Seedphrase ini memberi akses penuh dan tak terbatas ke semua bitcoin milikmu. Siapa pun yang punya seedphrase ini bisa mencuri danamu, bahkan tanpa menyentuh komputermu.

Seedphrase berisi 12 kata ini bisa memulihkan akses ke bitcoin kamu jika komputer hilang, dicuri, atau rusak. Karena itu, sangat penting untuk menyimpannya dengan hati-hati dan menaruhnya di tempat yang aman.

Kamu bisa menuliskannya di atas kertas, atau kalau mau keamanan ekstra, ukir di pelat baja tahan karat supaya tahan terhadap api, banjir, atau keruntuhan. Pilihan medianya tergantung pada strategi keamanan kamu, tapi kalau Sparrow kamu dipakai sebagai hot wallet dengan jumlah dana sedang, kertas sudah cukup.

Untuk info lebih lanjut tentang cara yang benar menyimpan dan mengelola seedphrase, aku sangat menyarankan kamu mengikuti tutorial lain kami, terutama kalau kamu masih pemula:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/26.webp)

**Jelas, kamu dilarang membagikan kata-kata ini di Internet, seperti yang aku lakukan dalam tutorial ini. Contoh Wallet ini hanya akan digunakan pada Testnet dan akan dihapus pada akhir tutorial.**

Kamu juga bisa menambahkan passphrase BIP39 dengan mengklik kotak “Use passphrase”. Peringatan: penggunaan passphrase bisa sangat berguna, tapi kalau kamu belum benar-benar paham cara kerjanya, ini bisa sangat berisiko. Karena itu, aku sangat menyarankan kamu membaca artikel teori singkat tentang topik ini:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Setelah kamu menyimpan Mnemonic dan passphrase ke media fisik, klik "*Konfirmasi Pencadangan*".

![Image](assets/fr/27.webp)

Masukkan kembali 12 kata kamu untuk mengonfirmasi bahwa kata tersebut telah disimpan dengan benar, lalu klik "*Buat Toko Kunci*".

![Image](assets/fr/28.webp)

Kemudian klik "*Import Keystore*" untuk mengimpor kunci portofolio Anda dari seedphrase.

![Image](assets/fr/29.webp)

Klik "*Apply*" untuk menyelesaikan pembuatan portofolio.

![Image](assets/fr/30.webp)

Buat password yang kuat untuk mengamankan akses ke wallet kamu di Sparrow. Sebaiknya simpan password ini di pengelola kata sandi supaya kamu nggak lupa. Perlu diingat, password ini tidak berperan dalam penurunan key-mu. Password ini hanya digunakan untuk membuka wallet kamu di Sparrow Wallet. Jadi, bahkan tanpa password ini, seedphrase kamu sudah cukup untuk mengakses bitcoin dari aplikasi lain yang kompatibel dengan BIP39.

![Image](assets/fr/31.webp)

Hot Wallet kamu sekarang sudah dibuat. Kamu bisa langsung ke bagian *Menerima Bitcoin* pada tutorial ini jika kamu tidak berencana menggunakan Hardware Wallet dengan Sparrow.

## Mengelola portofolio Cold

Cara kedua untuk menggunakan Sparrow Wallet adalah mengaturnya sebagai pengelola portofolio yang terhubung ke hardware wallet. Dalam konfigurasi ini, private key wallet Bitcoin kamu tersimpan secara eksklusif di hardware wallet, sementara Sparrow hanya mengakses informasi publik. Pendekatan ini memberi tingkat keamanan lebih tinggi dibandingkan hot wallet, karena private key disimpan di perangkat khusus, seringkali dengan chip yang aman, yang tidak terhubung ke internet sehingga permukaan serangannya jauh lebih kecil daripada komputer biasa.

Ada dua cara utama untuk menghubungkan Hardware Wallet kamu ke Sparrow:


- Dengan kabel, biasanya digunakan dengan model entry-level seperti Trezor Safe 3 atau Ledger Nano S Plus;
- Dalam mode Air-Gap, yaitu tanpa koneksi kabel langsung, melalui kartu MicroSD atau kode QR Exchange.

Sparrow mendukung semua metode komunikasi ini dan kompatibel dengan hampir semua hardware wallet yang ada di pasaran.

Dalam tutorial ini, aku akan menggunakan Ledger Nano S dengan koneksi kabel, tapi langkah-langkahnya hampir sama kalau kamu memakai mode air-gapped. Kamu bisa menemukan panduan khusus untuk hardware wallet milikmu di tutorial terpisah di Plan ₿ Network.

Sebelum mulai, pastikan wallet sudah dikonfigurasi di hardware wallet kamu. Kalau kamu memakai koneksi kabel, sambungkan perangkatmu ke komputer terlebih dahulu.

Untuk mengimpor apa yang disebut "*Keystore*" (informasi publik yang diperlukan untuk mengelola portofolio) ke dalam Sparrow Wallet, klik pada tab "*File*", kemudian "*New Wallet*".

![Image](assets/fr/32.webp)

Beri nama portofolio kamu dan klik "*Buat Wallet*". Aku menyarankanmu untuk memasukkan nama Hardware Wallet kamu untuk mengidentifikasinya dengan mudah nanti.

![Image](assets/fr/33.webp)

Pada bagian atas Interface, pilih antara portofolio "*Single Signature*" atau "*Multi Signature*". Untuk contoh kita, kita akan mengonfigurasi portofolio tanda tangan tunggal.

Tepat di bawah, pilih jenis skrip untuk mengunci UTXO kamu. Jika Hardware Wallet kamu mendukungnya, aku sarankan kamu memilih "*Taproot (P2TR)*".

![Image](assets/fr/34.webp)

Selanjutnya, prosedurnya berbeda menurut metode koneksi kamu. Kalau kamu menggunakan metode Celah Udara, pilih "*Airgapped Hardware Wallet*". Kemudian ikuti petunjuk khusus untuk perangkat kamu.

![Image](assets/fr/35.webp)

Kalau kamu menggunakan koneksi kabel, seperti dalam kasus saya, pilih "*Connected Hardware Wallet*".

![Image](assets/fr/36.webp)

Klik "*Scan*" untuk meminta Sparrow mendeteksi perangkat kamu. Pastikan perangkat sudah dicolokkan dan tidak terkunci. Untuk beberapa model, seperti Ledger, kamu harus membuka aplikasi "*Bitcoin*" untuk mengaktifkan pendeteksian.

![Image](assets/fr/37.webp)

Pilih "*Import Keystore*".

![Image](assets/fr/38.webp)

Klik "*Apply*" untuk menyelesaikan pembuatan portofolio.

![Image](assets/fr/39.webp)

Buat password yang kuat untuk mengamankan akses ke Sparrow Wallet kamu. Password ini akan melindungi public key, alamat, dan riwayat transaksimu. Disarankan untuk menyimpannya di pengelola kata sandi agar tidak lupa. Perlu diingat, password ini tidak berperan dalam penurunan key-mu. Bahkan tanpa password ini, kamu tetap bisa memulihkan akses ke bitcoin dengan seedphrase melalui software yang kompatibel dengan BIP39.

![Image](assets/fr/40.webp)

Portofolio manajemen kamu sekarang dikonfigurasikan di Sparrow.

![Image](assets/fr/41.webp)

## Menerima bitcoin

Setelah Wallet kamu diatur di Sparrow, kamu bisa menerima bitcoin. Cukup akses menu "*Terima*".

![Image](assets/fr/42.webp)

Sparrow akan menampilkan Address pertama yang tidak terpakai dalam Wallet. Anda bisa menambahkan "*Label*" ke Address ini untuk mengingatkan Anda tentang asal usul satoshi ini di kemudian hari.

![Image](assets/fr/43.webp)

Kalau kamu menggunakan hot wallet, address yang ditampilkan bisa langsung dipakai, baik dengan menyalinnya maupun memindai kode QR-nya.

Kalau kamu menggunakan hardware wallet, sangat penting untuk memverifikasi address di layar perangkat sebelum digunakan. Untuk perangkat berkabel, sambungkan dan buka kunci hardware wallet kamu, lalu di Sparrow klik “Display Address”. Pastikan address yang muncul di layar hardware wallet sama persis dengan yang ditampilkan di Sparrow.

![Image](assets/fr/44.webp)

Untuk pengguna Hardware Wallet Air-Gap, verifikasi Address bervariasi menurut model perangkat. Lihat tutorial khusus Plan ₿ Network untuk mendapatkan instruksi yang tepat.

Setelah transaksi disiarkan oleh pembayar, kamu akan melihatnya muncul di tab "*Transaksi*". Kamu dapat mengkliknya untuk detail lebih lanjut, seperti txid.

![Image](assets/fr/45.webp)

Di tab “*Alamat*”, kamu akan menemukan daftar semua address penerimaan milikmu. Kamu bisa melihat apakah address-address itu sudah pernah digunakan dan apakah label sudah ditambahkan. Address “*Terima*” adalah address yang ditampilkan Sparrow saat kamu mengklik “*Terima*” dan digunakan untuk menerima pembayaran masuk. Sementara address “*Change*” dipakai dalam transaksi sebagai tempat kembalian dari UTXO kamu yang tidak terpakai.

![Image](assets/fr/46.webp)

Tab “*UTXOs*” menampilkan semua UTXO milikmu, yaitu potongan Bitcoin yang kamu punya. Kamu bisa melihat jumlah tiap UTXO beserta label yang terpasang padanya.

![Image](assets/fr/47.webp)

## Kirim bitcoin

Sekarang setelah kamu punya beberapa satoshi di wallet kamu, kamu juga bisa mengirim sebagian darinya. Meskipun ada beberapa cara untuk melakukannya, aku menyarankan kamu menggunakan menu “*UTXOs*” agar bisa mengontrol dengan lebih presisi koin mana yang ingin kamu belanjakan (*coin control*), daripada langsung lewat menu “*Kirim*”. Tapi kalau kamu masih pemula, menu “*Kirim*” juga sudah cukup mudah digunakan.

![Image](assets/fr/48.webp)

Pilih UTXO yang ingin kamu gunakan sebagai input untuk transaksi ini, lalu klik “Kirim Terpilih”. Cara ini memungkinkan kamu memilih sumber koin yang paling sesuai dari daftar UTXO milikmu, berdasarkan kebutuhan pengeluaran dan label yang sudah kamu buat saat menerimanya, sehingga bisa mengoptimalkan privasi pembayaranmu. Pastikan jumlah UTXO yang kamu pilih lebih besar dari jumlah yang ingin kamu kirim.

![Image](assets/fr/49.webp)

Masukkan Address penerima di kolom "*Bayar ke*". Kamu juga dapat memindai Address dengan webcam dengan mengklik ikon kamera. Tombol "*+Tambah*" memungkinkanmu membayar ke beberapa alamat dalam satu transaksi.

![Image](assets/fr/50.webp)

Tambahkan label pada transaksimu untuk membantumu mengingat tujuannya. Label ini juga akan otomatis dikaitkan dengan address kembalianmu nanti.

![Image](assets/fr/51.webp)

Masukkan jumlah yang akan dikirim ke Address ini.

![Image](assets/fr/52.webp)

Sesuaikan tingkat biaya sesuai dengan kondisi pasar saat ini. Kamu dapat melakukannya dengan memasukkan nilai biaya absolut atau dengan menyesuaikan tarif biaya dengan penggeser.

![Image](assets/fr/53.webp)

Di bagian bawah antarmuka, kamu bisa memilih antara “Efficiency” dan “Privacy”. Dalam contoh ini, opsi “Privacy” tidak tersedia karena aku hanya punya satu UTXO di wallet ini. “Efficiency” digunakan untuk transaksi biasa, sedangkan “Privacy” adalah jenis transaksi Stonewall, struktur transaksi yang meningkatkan privasimu dengan meniru mini-CoinJoin, sehingga membuat *chain analysis* jadi lebih sulit.

![Image](assets/fr/54.webp)

Sparrow menampilkan diagram ringkasan yang menunjukkan input, output, dan biaya transaksi kamu (perhatikan bahwa biaya sebenarnya bukanlah output, berlawanan dengan apa yang ditunjukkan oleh diagram ini). Kalau kamu puas dengan semuanya, klik "*Buat Transaksi*".

![Image](assets/fr/55.webp)

Kamu akan dibawa ke halaman yang merinci Elements dari transaksi kamu. Periksa apakah semua informasi sudah benar, lalu klik "*Finalisasi Transaksi untuk Penandatanganan*".

![Image](assets/fr/56.webp)

Sangat penting untuk mempertahankan Sighash default. Untuk memahami alasannya, lihatlah kursus pelatihan ini, di mana saya menjelaskan semua yang perlu kamu ketahui tentang Sighash:

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

Pada layar berikutnya, opsi bervariasi menurut tipe Wallet yang Anda gunakan:


- Untuk Hardware Wallet Air-Gap, klik "*Show QR*" untuk menampilkan PSBT yang dapat kamu tandatangani dengan perangkat kamu, lalu muat PSBT yang telah ditandatangani ke dalam Sparrow menggunakan "*Scan QR*". Opsi "*Save Transaction*" bekerja dengan cara yang sama, tetapi dengan penukaran pada microSD;
- Untuk Hot Wallet, cukup klik "*Sign*" dan masukkan kata sandi Wallet untuk menandatangani;
- Untuk Hardware Wallet berkabel, klik juga "*Sign*" untuk mengirim transaksi yang belum ditandatangani ke perangkat Anda.

![Image](assets/fr/57.webp)

Pada Hardware Wallet Anda, periksa Address penerima, jumlah yang dikirim, dan biaya. Jika semuanya sudah benar, lanjutkan dengan tanda tangan.

Setelah transaksi ditandatangani, transaksi tersebut akan muncul kembali di Sparrow, siap untuk disiarkan di jaringan Bitcoin untuk dimasukkan ke dalam blok berikutnya. Jika semuanya sudah benar, klik "*Broadcast Transaction*".

![Image](assets/fr/58.webp)

Sekarang transaksi kamu disiarkan dan menunggu konfirmasi.

![Image](assets/fr/59.webp)

## Mengelola dan mengonfigurasi portofolio di Sparrow

Pada tab "*Settings*", kamu akan menemukan informasi rinci mengenai portofolio milikmu, misalnya, :


- Jenis portofolio (single-sig atau multi-sig);
- Jenis skrip yang digunakan ;
- Nama yang sudah kamu tetapkan ke portofolio ;
- Jejak kunci utama;
- Jalur pintas ;
- Kunci publik akun yang diperpanjang.

![Image](assets/fr/60.webp)

Tombol "*Export*" memungkinkan kamu untuk mengekspor informasi portofolio kamu sehingga kamu dapat menggunakannya di perangkat lunak lain sambil mempertahankan informasi yang telah diatur di Sparrow.

Tombol "*Tambah Akun*" memungkinkan kamu menambahkan akun tambahan ke portofolio kamu. Sebuah akun berhubungan dengan seperangkat alamat kotak masuk yang terpisah. Fitur ini dapat berguna, misalnya, jika kamu ingin memisahkan akun pribadi dan akun bisnis, dengan satu frasa Mnemonic.

Tombol "*Advanced*" memberikan akses ke pengaturan lanjutan, seperti menyesuaikan pencarian Address Sparrow dan mengubah kata sandi portofolio.

![Image](assets/fr/61.webp)

Ketika kamu menutup Sparrow Wallet, Wallet kamu akan terkunci secara otomatis. Saat berikutnya kamu membuka perangkat lunak, sebuah jendela akan meminta kamu untuk membuka kunci Wallet dengan kata sandinya.

![Image](assets/fr/62.webp)

Jika jendela ini tidak terbuka, atau kalau kamu ingin membuka portofolio lain di Sparrow, klik tab "*File*" dan pilih "*Open Wallet*".

![Image](assets/fr/63.webp)

Ini akan membuka File Manager Anda ke folder tempat Sparrow menyimpan dompet kamu. Cukup pilih Wallet yang ingin kamu buka dan masukkan kata sandi untuk membukanya.

![Image](assets/fr/64.webp)

Pada menu "*File*" di bawah "*Settings*", kamu akan menemukan parameter koneksi jaringan Bitcoin yang telah dieksplorasi pada bagian sebelumnya. Kamu juga bisa menyesuaikan berbagai parameter seperti unit yang digunakan, mata uang fiat untuk konversi, dan sumber informasi.

![Image](assets/fr/65.webp)

Tab "*Lihat*" menawarkan opsi kustomisasi dan akses ke beberapa perintah yang berguna, seperti "*Refresh Wallet*", yang menyegarkan pencarian transaksi untuk portofolio kamu.

![Image](assets/fr/66.webp)

Tab "*Tools*" mengelompokkan beberapa alat bantu canggih, termasuk :


- "*Tanda Tangan/Verifikasi Pesan*" memungkinkan kamu untuk membuktikan kepemilikan Address yang diterima atau memverifikasi tanda tangan.
- "*Kirim Ke Banyak*" menawarkan Interface yang disederhanakan untuk melakukan transaksi ke beberapa alamat penerima sekaligus, yang nyaman untuk pengeluaran batch.
- "*Sweep Private Key*" memungkinkan kamu untuk mengambil bitcoin yang diamankan dengan private key sederhana dan mentransfernya ke Sparrow Wallet kamu. Ini bisa sangat berguna bagi mereka yang memiliki bitcoin yang berasal dari awal tahun 2010, sebelum era dompet HD.
- "Verifikasi Unduhan" memverifikasi integritas dan keaslian perangkat lunak yang diunduh sebelum menginstalnya pada perangkat kamu.
- "*Restart In*" memungkinkan Anda untuk beralih ke dompet Anda di jaringan Testnet atau Signet. Ini dapat berguna kalau kamu ingin mengakses jaringan uji coba dengan koin yang tidak memiliki nilai.

![Image](assets/fr/67.webp)

Sekarang kamu sudah tahu semua tentang Sparrow Wallet, alat yang luar biasa untuk mengelola portofolio Bitcoin kamu sehari-hari.

Kalau kamu merasa tutorial ini bermanfaat, aku akan sangat berterima kasih kalau kamu mau memberikan jempol hijau di bawah ini. Jangan ragu untuk membagikannya di media sosial kamu. Terima kasih banyak!

Aku juga merekomendasikan kamu tutorial lain yang menjelaskan cara mengonfigurasi Hardware Wallet COLDCARD Q dengan Sparrow Wallet:

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3
