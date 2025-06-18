---
name: Sparrow Wallet
description: Menginstal, mengonfigurasi, dan menggunakan Sparrow Wallet
---
![cover](assets/cover.webp)

Sparrow Wallet adalah perangkat lunak manajemen portofolio Bitcoin yang dikembangkan oleh Craig Raw. Perangkat lunak sumber terbuka ini dihargai oleh para bitcoiners karena banyak fitur dan Interface yang intuitif.

Ada dua cara untuk menggunakan Sparrow:


- Seperti Hot Wallet, di mana kunci pribadi Anda disimpan di PC Anda.
- Sebagai manajer Cold Wallet, dimana kunci pribadi disimpan pada Hardware Wallet. Dalam mode ini, Sparrow hanya memanipulasi informasi Wallet publik, melacak dana, menghasilkan alamat, dan membuat transaksi, tetapi tanda tangan Hardware Wallet diperlukan untuk membuat transaksi ini valid. Oleh karena itu, Sparrow dapat menggantikan aplikasi seperti Ledger Live atau Trezor Suite.

Sparrow mendukung dompet dengan tanda tangan tunggal dan multi tanda tangan, dan memungkinkan manajemen yang lancar untuk beberapa dompet. Sebagai contoh, Anda dapat secara bersamaan mengontrol satu Wallet yang terhubung ke Ledger, satu lagi ke Trezor, dan juga memiliki Hot Wallet.

Perangkat lunak ini juga menawarkan fitur kontrol koin yang canggih, memungkinkan Anda untuk memilih dengan tepat UTXO mana yang akan digunakan dalam transaksi Anda untuk mengoptimalkan kerahasiaan Anda.

Dalam hal koneksi, Sparrow memungkinkan Anda terhubung ke node Bitcoin Anda sendiri, baik dari jarak jauh melalui Server Electrum, atau dengan Bitcoin Core. Anda juga dapat menggunakan node publik jika Anda belum memiliki node sendiri. Sambungan jarak jauh dibuat melalui Tor.

## Pasang Sparrow Wallet

Buka [halaman unduhan resmi Sparrow Wallet] (https://sparrowwallet.com/download/) dan pilih versi perangkat lunak yang sesuai dengan sistem operasi Anda.

![Image](assets/fr/01.webp)

Penting untuk memeriksa integritas dan keaslian perangkat lunak sebelum menginstalnya. Jika Anda tidak tahu cara melakukannya, Anda bisa menemukan tutorial lengkapnya di sini:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Setelah Sparrow terinstal, Anda bisa melewatkan layar penjelasan awal dan langsung menuju ke layar manajemen koneksi.

![Image](assets/fr/02.webp)

## Menghubungkan ke jaringan Bitcoin

Untuk berinteraksi dengan jaringan Bitcoin dan menyiarkan transaksi Anda, Sparrow harus terhubung ke node Bitcoin. Ada tiga cara utama untuk membuat koneksi ini:


- 🟡 Menggunakan simpul publik, yaitu menyambung ke simpul pihak ketiga yang mengizinkan koneksi tersebut. Jika Anda tidak memiliki node Bitcoin Anda sendiri, opsi ini memungkinkan Anda untuk memulai Sparrow dengan cepat. Akan tetapi, node yang Anda sambungkan akan melihat semua transaksi Anda, yang dapat membahayakan kerahasiaan Anda. Memiliki kontrol atas kunci Anda sangat penting, tetapi memiliki node Anda sendiri bahkan lebih baik. Jadi, gunakan opsi ini hanya jika Anda baru memulai, dengan tetap menyadari risiko privasi Anda.
- 🟢 Menghubungkan ke node Bitcoin Core. Jika Anda memiliki node Bitcoin Core Anda sendiri, Anda dapat menyambungkannya ke Sparrow Wallet, baik secara lokal jika Bitcoin Core diinstal pada mesin yang sama, atau dari jarak jauh.
- 🔵 Koneksi melalui server Electrum. Jika node Bitcoin Anda dilengkapi dengan Electrs, seperti halnya dengan solusi node-in-a-box seperti Umbrel atau Start9, Anda dapat menyambungkannya dari jarak jauh dari Sparrow.

**Lebih baik menggunakan koneksi melalui Electrs atau Bitcoin Core pada node Anda sendiri untuk mengurangi kebutuhan untuk mempercayai pihak ketiga dan mengoptimalkan kerahasiaan Anda**

### Terhubung ke simpul publik 🟡

Menghubungkan ke node publik sangat sederhana. Klik pada tab "*Public Server*".

![Image](assets/fr/03.webp)

Pilih simpul dari daftar tarik-turun.

![Image](assets/fr/04.webp)

Kemudian klik "*Test Connection*".

![Image](assets/fr/05.webp)

Setelah terhubung, Sparrow Wallet akan menampilkan tanda centang kuning di sudut kanan bawah Interface untuk mengindikasikan bahwa Anda terhubung ke simpul publik.

![Image](assets/fr/06.webp)

### Menghubungkan ke Bitcoin Core 🟢

Metode kedua untuk menyambung ke node Bitcoin adalah dengan menghubungkan Sparrow ke Bitcoin Core. Jika Bitcoin Core diinstal pada mesin yang sama, autentikasi akan dilakukan melalui file cookie. Jika Bitcoin Core berada di mesin jarak jauh, Anda harus menggunakan kata sandi yang ditetapkan dalam file `Bitcoin.conf`.

Harap diperhatikan bahwa jika Anda menggunakan Bitcoin Core node yang dipangkas, Anda tidak akan dapat memulihkan Wallet yang berisi transaksi sebelum blok yang disimpan secara lokal. Akan tetapi, untuk Wallet baru yang dibuat di Sparrow, hal ini tidak akan menjadi masalah: transaksi baru Anda akan terlihat, bahkan dengan node yang dipangkas.

Untuk mengonfigurasi node Bitcoin Core, Anda dapat membaca salah satu tutorial berikut, tergantung pada sistem operasi Anda:

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

Pada Sparrow, buka tab "*Bitcoin Core*".

![Image](assets/fr/07.webp)

**Dengan Bitcoin Core lokal:**

Jika Bitcoin Core terinstal di komputer Anda, cari file `Bitcoin.conf` di antara file perangkat lunak. Jika file ini tidak ada, Anda dapat membuatnya. Buka file tersebut dengan editor teks dan masukkan baris berikut:

```ini
server=1
```

Kemudian simpan perubahan Anda.

Anda juga dapat melakukan ini melalui grafik Bitcoin-QT's Interface dengan menavigasi ke "*Settings*" > "*Options...*" dan mengaktifkan opsi "*Enable RPC server*".

Jangan lupa untuk memulai ulang perangkat lunak setelah melakukan perubahan ini.

![Image](assets/fr/08.webp)

Kemudian kembali ke Sparrow Wallet dan masukkan jalur ke file cookie Anda, biasanya terletak di folder yang sama dengan `Bitcoin.conf`, tergantung pada sistem operasi Anda:

| **macOS** | ~/Perpustakaan/Dukungan Aplikasi/Bitcoin |

| ----------- | ------------------------------------- |

| **Windows** | %APPDATA%\Bitcoin |

| **Linux** | ~/.Bitcoin |

![Image](assets/fr/09.webp)

Biarkan parameter lain sebagai default, URL `127.0.0.1` dan port `8332`, lalu klik "*Test Connection*".

![Image](assets/fr/10.webp)

Sambungan telah dibuat. Tanda centang Green akan muncul di sudut kanan bawah untuk menunjukkan bahwa Anda terhubung ke node Bitcoin Core.

![Image](assets/fr/11.webp)

*dengan remote Bitcoin Core: ** Dengan remote Bitcoin Core:**

Jika Bitcoin Core diinstal pada mesin lain yang terhubung ke jaringan yang sama, pertama-tama cari file `Bitcoin.conf` di antara file perangkat lunak. Jika file ini belum ada, Anda dapat membuatnya. Buka file ini dengan editor teks dan tambahkan baris berikut:

```ini
server=1
```

Setelah mengedit file, pastikan Anda menyimpannya dalam folder yang sesuai untuk sistem operasi Anda:

| **macOS** | ~/Perpustakaan/Dukungan Aplikasi/Bitcoin |

| ----------- | ------------------------------------- |

| **Windows** | %APPDATA%\Bitcoin |

| **Linux** | ~/.Bitcoin |

Operasi ini juga dapat dilakukan melalui Bitcoin-QT Interface grafis Interface. Buka menu "*Settings*", kemudian "*Options...*", dan aktifkan opsi "*Enable RPC server*" dengan mencentang kotak yang sesuai. Jika file `Bitcoin.conf` tidak ada, Anda dapat membuatnya langsung dari Interface ini dengan mengklik "*Open Configuration File*".

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

Sekarang Anda dapat kembali ke Sparrow Wallet. Buka tab "*User / Pass*". Masukkan nama pengguna dan kata sandi yang Anda konfigurasikan dalam file `Bitcoin.conf`. Biarkan parameter lainnya sebagai default, yaitu URL `127.0.0.1` dan port `8332`. Kemudian klik "*Test Connection*".

![Image](assets/fr/15.webp)

Sambungan telah dibuat. Tanda centang Green akan muncul di sudut kanan bawah untuk mengindikasikan bahwa Anda tersambung ke node Bitcoin Core.

![Image](assets/fr/16.webp)

### Menghubungkan ke server Electrum 🔵

Opsi terakhir untuk menyambung adalah dengan menggunakan server Electrum jarak jauh. Metode ini memungkinkan Anda terhubung ke node Anda melalui Tor dari perangkat lain, dan memanfaatkan pengindeks untuk menelusuri portofolio Anda di Sparrow dengan lebih cepat. Metode ini sangat cocok jika Anda memiliki solusi node-in-a-box seperti Umbrel atau Start9, yang memungkinkan Anda untuk menginstal Electrs dengan satu klik.

Untuk melakukan ini, dapatkan Tor `.onion' Address dari server Electrum Anda. Dengan Umbrel, misalnya, Anda akan menemukannya di aplikasi Electrs.

![Image](assets/fr/17.webp)

Pada Sparrow Wallet, akses tab "*Private Electrum*".

![Image](assets/fr/18.webp)

Masukkan Tor Address Anda di tempat yang disediakan. Pengaturan lainnya bisa tetap default. Kemudian klik "*Test Connection*".

![Image](assets/fr/19.webp)

Koneksi telah dikonfirmasi. Jika Anda menutup jendela ini, tanda centang biru akan muncul di sudut kanan bawah, yang menunjukkan bahwa Anda terhubung ke server Electrum.

![Image](assets/fr/20.webp)

## Buat portofolio yang hangat

Setelah Sparrow Wallet dikonfigurasikan untuk berkomunikasi dengan jaringan Bitcoin, Anda siap untuk membuat Wallet pertama Anda. Bagian ini memandu Anda untuk membuat Hot Wallet, yaitu Wallet yang kunci pribadinya disimpan di komputer Anda. Karena komputer anda merupakan mesin yang kompleks dan terhubung ke Internet, maka komputer anda memiliki permukaan serangan yang sangat besar. Oleh karena itu, Hot Wallet sebaiknya hanya digunakan untuk menyimpan bitcoin dalam jumlah yang terbatas. Untuk menyimpan jumlah yang lebih besar, pilihlah Wallet yang aman dengan Hardware Wallet. Jika ini yang Anda cari, Anda dapat langsung melanjutkan ke bagian selanjutnya.

Untuk membuat Hot Wallet, dari layar beranda Sparrow Wallet, klik tab "*File*" dan kemudian "*New Wallet*".

![Image](assets/fr/21.webp)

Masukkan nama untuk portofolio Anda dan klik "*Buat Wallet*".

![Image](assets/fr/22.webp)

Di bagian atas Interface, Anda dapat memilih apakah akan membuat portofolio "*Single Signature*" atau "*Multi Signature*". Tepat di bawahnya, pilih jenis skrip untuk mengunci UTXO Anda. Saya sarankan Anda menggunakan standar terbaru: "*Taproot (P2TR)*".

![Image](assets/fr/23.webp)

Kemudian klik "*Software Wallet Baru atau Impor*".

![Image](assets/fr/24.webp)

Pilih standar BIP39, karena standar ini didukung oleh hampir semua perangkat lunak portofolio Bitcoin. Selanjutnya, pilih panjang frasa pemulihan Anda. Saat ini, frasa 12 kata sudah cukup, karena keduanya menawarkan keamanan yang serupa, tetapi frasa 12 kata lebih sederhana untuk disimpan.

![Image](assets/fr/25.webp)

Klik tombol "*generate New*" untuk meng-generate frasa Wallet Anda. Frasa ini memberikan akses penuh dan tidak terbatas ke semua bitcoin Anda. Siapa pun yang memiliki frasa ini dapat mencuri dana Anda, bahkan tanpa akses fisik ke komputer Anda.

Frasa 12 kata ini mengembalikan akses ke bitcoin Anda jika terjadi kehilangan, pencurian, atau kerusakan pada komputer Anda. Oleh karena itu, sangat penting untuk menyimpannya dengan hati-hati dan menyimpannya di tempat yang aman.

Anda bisa menuliskannya di atas kertas atau, untuk keamanan tambahan, mengukirnya di atas baja tahan karat untuk melindunginya dari api, banjir atau keruntuhan. Pilihan media untuk Mnemonic Anda akan tergantung pada strategi keamanan Anda, tetapi jika Anda menggunakan Sparrow sebagai Wallet yang berisi uang hangat dalam jumlah sedang, kertas sudah cukup.

Untuk informasi lebih lanjut mengenai cara yang tepat untuk menyimpan dan mengelola frasa Mnemonic Anda, saya sangat merekomendasikan untuk mengikuti tutorial lainnya, khususnya jika Anda seorang pemula:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/26.webp)

**Jelas, Anda tidak boleh membagikan kata-kata ini di Internet, seperti yang saya lakukan dalam tutorial ini. Contoh Wallet ini hanya akan digunakan pada Testnet dan akan dihapus pada akhir tutorial.**

Anda juga dapat memilih untuk menambahkan passphrase BIP39 dengan mengklik kotak "*Use passphrase*". Peringatan: menggunakan passphrase bisa sangat berguna, tetapi jika Anda tidak memahami cara kerjanya, ini bisa sangat berisiko. Itulah mengapa saya sangat menyarankan Anda untuk membaca artikel teori singkat tentang subjek ini:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Setelah Anda menyimpan Mnemonic dan passphrase Anda ke media fisik, klik "*Konfirmasi Pencadangan*".

![Image](assets/fr/27.webp)

Masukkan kembali 12 kata Anda untuk mengonfirmasi bahwa kata tersebut telah disimpan dengan benar, lalu klik "*Buat Toko Kunci*".

![Image](assets/fr/28.webp)

Kemudian klik "*Import Keystore*" untuk mengimpor kunci portofolio Anda dari frasa Mnemonic.

![Image](assets/fr/29.webp)

Klik "*Apply*" untuk menyelesaikan pembuatan portofolio.

![Image](assets/fr/30.webp)

Tetapkan kata sandi yang kuat untuk mengamankan akses ke portofolio Sparrow Anda. Sebaiknya simpan kata sandi ini di dalam pengelola kata sandi, agar Anda tidak lupa. Perhatikan bahwa kata sandi ini tidak berperan dalam penurunan kunci Anda. Kata sandi ini hanya digunakan untuk mengakses Wallet Anda melalui Sparrow Wallet. Jadi, bahkan tanpa kata sandi ini, frasa Mnemonic Anda sudah cukup untuk mengakses bitcoin Anda dari aplikasi yang kompatibel dengan BIP39.

![Image](assets/fr/31.webp)

Hot Wallet Anda sekarang sudah dibuat. Anda bisa langsung ke bagian *Menerima Bitcoin* pada tutorial ini jika Anda tidak berencana menggunakan Hardware Wallet dengan Sparrow.

## Mengelola portofolio Cold

Cara kedua untuk menggunakan Sparrow Wallet adalah dengan mengaturnya sebagai manajer portofolio dengan Hardware Wallet. Dalam konfigurasi ini, private key dari Bitcoin Wallet anda tetap berada secara eksklusif pada Hardware Wallet, sedangkan Sparrow hanya mengakses informasi publik. Pendekatan ini menawarkan tingkat keamanan yang lebih tinggi dibandingkan dengan dompet Hot yang telah dibahas di atas, karena private key disimpan pada perangkat khusus, seringkali dengan sebuah chip yang aman, yang tidak terhubung ke Internet dan oleh karena itu memberikan permukaan serangan yang lebih kecil dibandingkan dengan komputer biasa.

Ada dua cara utama untuk menghubungkan Hardware Wallet Anda ke Sparrow:


- Dengan kabel, biasanya digunakan dengan model entry-level seperti Trezor Safe 3 atau Ledger Nano S Plus;
- Dalam mode Air-Gap, yaitu tanpa koneksi kabel langsung, melalui kartu MicroSD atau kode QR Exchange.

Sparrow mendukung semua metode komunikasi ini dan kompatibel dengan sebagian besar dompet perangkat keras yang ada di pasaran.

Untuk tutorial ini, saya akan menggunakan Ledger Nano S dengan kabel, tetapi prosedurnya serupa dalam mode Air-Gap. Anda akan menemukan detail khusus untuk Hardware Wallet Anda dalam tutorial khusus pada Plan ₿ Network.

Sebelum memulai, pastikan Wallet sudah dikonfigurasikan pada Hardware Wallet Anda. Jika Anda menggunakan koneksi kabel, sambungkan ke komputer melalui kabel.

Untuk mengimpor apa yang disebut "*Keystore*" (informasi publik yang diperlukan untuk mengelola portofolio) ke dalam Sparrow Wallet, klik pada tab "*File*", kemudian "*New Wallet*".

![Image](assets/fr/32.webp)

Beri nama portofolio Anda dan klik "*Buat Wallet*". Saya menyarankan Anda untuk memasukkan nama Hardware Wallet Anda untuk mengidentifikasinya dengan mudah nanti.

![Image](assets/fr/33.webp)

Pada bagian atas Interface, pilih antara portofolio "*Single Signature*" atau "*Multi Signature*". Untuk contoh kita, kita akan mengonfigurasi portofolio tanda tangan tunggal.

Tepat di bawah, pilih jenis skrip untuk mengunci UTXO Anda. Jika Hardware Wallet Anda mendukungnya, saya sarankan Anda memilih "*Taproot (P2TR)*".

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