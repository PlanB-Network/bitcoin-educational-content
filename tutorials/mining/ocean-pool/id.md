---
name: Ocean Mining

description: Pengenalan tentang Penambangan Lautan
---

![signup](assets/cover.webp)

**Mei 2024**

Ocean Mining adalah kolam penambangan yang cukup unik. Di sini, tidak diperlukan akun, alamat email, atau kata sandi. Sama seperti Bitcoin, semuanya transparan, pseudonim, dan kontributor dapat memilih dari empat template blok yang berbeda.

### Sistem Kompensasi

Sistem kompensasi dari Ocean disebut TIDES, "Transparent Index of Distinct Extended Shares". Sistem ini mencatat pekerjaan yang disediakan oleh para penambang, yang dikenal sebagai "shares". Kolam menghitung persentase "shares" untuk setiap kontributor, kemudian menambahkan alamat Bitcoin mereka ke dalam template blok kolam sebagai penerima persentase dari hadiah blok tersebut.

Template blok diperbarui sekitar setiap 10 detik untuk memperhitungkan transaksi baru yang paling menguntungkan dan untuk mengubah distribusi hadiah blok jika diperlukan.

![signup](assets/rem.webp)

Apakah mesin Anda terhubung atau tidak pada saat kolam menambang blok baru tidak masalah. Pekerjaan yang sudah diserahkan disimpan untuk delapan blok berikutnya yang ditemukan oleh kolam.

Menyimpan pekerjaan untuk delapan blok alih-alih mereset penghitung ke nol dengan setiap blok baru yang ditambang berarti kompensasi Anda hanya akan 100% setelah kolam menemukan delapan blok setelah Anda mulai berkontribusi. Ini juga berarti bahwa Anda akan terus dikompensasi untuk delapan blok jika Anda berhenti berkontribusi ke kolam.

Mekanisme ini meratakan kompensasi dan mencegah "pool hopping", yang melibatkan beralih kolam secara teratur tergantung pada mana yang paling mungkin menemukan blok berikutnya.

### Penarikan

Operasi Ocean Mining memungkinkan kontributornya untuk memulihkan bitcoin "bersih", yang berarti bitcoin yang langsung dikeluarkan oleh hadiah blok.

Tidak seperti sebagian besar kolam lainnya, Ocean tidak menerima bitcoin yang baru ditambang; alamat kontributor langsung diintegrasikan ke dalam template blok.

Untuk saat ini, jumlah minimum untuk benar-benar mendapatkan manfaat dari bitcoin bersih adalah 1,048,576 sats. Dengan setiap blok yang ditambang oleh kolam, bagian "shares" Anda harus memberi Anda hak lebih dari 1,048,576 sats agar mereka dapat langsung dibayar kepada Anda oleh hadiah blok.
Jika tidak, sats Anda akan disimpan oleh Ocean sampai total hadiah Anda melebihi jumlah ini.

Semua bitcoin yang sementara disimpan oleh Ocean berada di alamat ini: [37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n, semuanya dapat diverifikasi di TimeChain.](https://mempool.space/address/37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n)
Juga dimungkinkan untuk menarik sats Anda melalui Lightning menggunakan BOLT12. Kita akan melihat cara mengaturnya.

### Biaya Kolam

Biaya berkisar dari 0% hingga 2% tergantung pada template blok yang dipilih.

## Transparansi Ocean

### Data Kontributor

![signup](assets/1.webp)

Semua informasi tentang kolam transparan, termasuk semua data pengguna. Untuk memahami poin ini, mari kita ambil contoh:

[Di dashboard Ocean](https://ocean.xyz/dashboard), Anda memiliki banyak informasi seperti hashrate selama enam bulan terakhir, jumlah peserta di kolam, total jumlah bitcoin yang ditambang, dll.

Kita akan fokus pada bagian "Kontributor". Anda dapat melihat daftar semua kontributor dengan hashrate rata-rata mereka selama tiga jam terakhir serta persentase **"shares"** dan **"hash"** relatif terhadap sisanya di kolam.
**"Shares %"** adalah persentase pekerjaan yang disediakan oleh kontributor dalam jendela delapan blok terakhir dibandingkan dengan sisanya di kolam.
**"Hash %"** adalah persentase rata-rata hashrate yang disediakan oleh kontributor selama tiga jam terakhir dibandingkan dengan sisanya di kolam.

![signup](assets/2.webp)

Anda akan melihat bahwa "Kontributor" diidentifikasi dengan alamat Bitcoin. Anda dapat mengklik salah satu alamat ini untuk detail lebih lanjut.

Jika kita mengambil yang pertama, yang memiliki hashrate tertinggi [1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ](https://ocean.xyz/stats/1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ), Anda dapat melihat semua detail tentang pengguna ini: hashrate, jumlah bitcoin yang ditambang, dengan blok mana, dan bahkan detail dari setiap mesin mereka (ASICs). Namun, mereka tetap anonim, seperti pada Bitcoin.

### Template Blok

Di kiri atas pada dashboard, Anda memiliki "Blok Selanjutnya". Di halaman ini, ada empat template blok yang berbeda. Ocean memungkinkan setiap kontributor untuk memilih template blok yang ingin mereka dukung. Ini tidak memiliki dampak langsung pada kompensasi Anda. Ketika kolam menambang sebuah blok, semua kontributor dikompensasi terlepas dari template yang mereka pilih. Ini hanya memungkinkan semua orang untuk "memilih" template blok yang cocok untuk mereka.

![signup](assets/3.webp)

**CORE:** Biaya 2%, ini adalah template Bitcoin Core klasik tanpa filter, seperti tertulis di halaman mereka "Termasuk transaksi dan mayoritas spam"

**CORE+ANTISPAM:** Biaya 0%, Bitcoin Core dengan filter terhadap transaksi tertentu seperti Ordinals "Termasuk transaksi dan membatasi spam"

**OCEAN:** Biaya 0%, Bitcoin Knot "Hanya termasuk transaksi dan data yang cukup kecil"

**DATA-FREE:** Biaya 0%, Bitcoin Knot "Hanya termasuk transaksi tanpa data sembarangan"

### Perbedaan antara Bitcoin Core dan Bitcoin Knot
Bitcoin Core adalah perangkat lunak yang memungkinkan sekitar 99% node Bitcoin di seluruh dunia untuk beroperasi. Bitcoin adalah protokol, yang berarti bahwa, seperti Internet, di mana ada beberapa browser, bisa ada beberapa program perangkat lunak yang berbeda yang koeksistensi pada TimeChain yang sama. Namun, karena kekhawatiran akan kompatibilitas dan untuk membatasi risiko bug yang akan meninggalkan jejak tak terhapus pada TimeChain, hampir semua pengembang Bitcoin bekerja pada Bitcoin Core. Bitcoin Knots adalah fork dari Bitcoin Core, yang berarti ia membagikan sebagian besar kode mereka, sangat membatasi risiko bug. Fork ini dibuat oleh Luke Dashjr, yang ingin menerapkan aturan yang lebih restriktif daripada Bitcoin Core tanpa menciptakan hard fork. Sekarang, Bitcoin Core dan Bitcoin Knots koeksistensi berkat konsensus Nakamoto.

## Menambahkan Pekerja

Untuk menambahkan pekerja, mulailah dengan memilih template blok Anda. Pilihan ini akan menentukan URL kolam yang harus dimasukkan pada penambang Anda (ASICs).

- **CORE**: `stratum+tcp://core.mine.ocean.xyz:3202`
- **CORE+ANTISPAM**: `stratum+tcp://ordis.mine.ocean.xyz:3303`
- **OCEAN**: `stratum+tcp://mine.ocean.xyz:3334`
- **DATA-FREE**: `stratum+tcp://datafree.mine.ocean.xyz:3404`

Selanjutnya, untuk bidang pengguna, masukkan alamat Bitcoin yang Anda miliki. Berikut adalah daftar jenis alamat yang kompatibel:
- **P2PKH** (Tipe alamat asli. Dimulai dengan “1”)
- **P2SH** (Multisignature atau P2SH-Segwit. Dimulai dengan “3”)
- **Bech32** (Segwit. Dimulai dengan “bc”.)
- **Bech32m** (Taproot. Dimulai dengan “bc”. Lebih panjang dari Bech32.)

Jika Anda memiliki beberapa penambang, Anda dapat memasukkan alamat yang sama untuk semua penambang sehingga hash rate mereka digabungkan dan muncul sebagai satu penambang. Anda juga dapat membedakan mereka dengan menambahkan nama yang berbeda untuk masing-masing. Untuk melakukan ini, cukup tambahkan “.namapenambang” setelah alamat Bitcoin.

Akhirnya, untuk kolom kata sandi, gunakan `x`.

**Contoh:**
Jika Anda memilih template **OCEAN**, alamat Bitcoin Anda adalah `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv` dan Anda ingin menamai penambang Anda “Brrrr”, maka Anda perlu memasukkan informasi berikut di antarmuka penambang Anda:

- **URL**: `stratum+tcp://mine.ocean.xyz:3334`
- **USER**: `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr`
- **PASSWORD**: `x`

Beberapa menit setelah memulai penambangan, Anda akan dapat melihat data Anda di situs Ocean dengan mencari alamat Anda.

### Ikhtisar Dashboard
- **Saham dalam Jendela Hadiah**: Data ini menunjukkan jumlah saham, pekerjaan yang Anda kirim ke kolam dalam jendela 8 blok terakhir yang ditambang oleh kolam.
- **Perkiraan Hadiah dalam Jendela**: Perkiraan jumlah satoshi yang akan Anda peroleh dengan pekerjaan yang sudah dilakukan. Ini tidak memperhitungkan biaya transaksi, hanya coinbase, bitcoin baru yang dikeluarkan oleh jaringan.
- **Perkiraan Pendapatan Blok Berikutnya**: Perkiraan jumlah satoshi yang diperoleh jika blok ditambang sekarang. Ingat, jika nilai ini kurang dari 1,048,576 satoshi, Anda tidak akan langsung menerima satoshi ke alamat Anda. Mereka akan dikirim ke alamat Ocean sampai pendapatan Anda melebihi ambang batas ini.

Di bawah ini, Anda memiliki grafik yang menampilkan riwayat hash rate Anda hingga 6 bulan.

![signup](assets/4.webp)

Di sini, Anda memiliki rata-rata hash rate Anda dalam berbagai skala waktu, dari 60 detik hingga 24 jam, serta riwayat blok yang ditambang oleh kolam untuk yang Anda telah berkontribusi dan diberi hadiah.

![signup](assets/5.webp)

Anda memiliki opsi untuk mengekspor file CSV dari riwayat ini dengan tombol **Download CSV**.

![signup](assets/6.webp)

Di bagian berikutnya, Anda memiliki daftar semua penambang yang telah Anda hubungkan ke kolam dengan alamat ini. Anda memiliki, tentu saja, hash rate individu mereka, tetapi juga jumlah satoshi yang mereka terima secara individu untuk pekerjaan mereka.

![signup](assets/7.webp)

Anda dapat mengklik pada **Nickname** dari penambang mana pun. Anda kemudian akan memiliki semua informasi yang baru saja kita lihat, tetapi secara spesifik untuk penambang tersebut.

Dan di bagian bawah halaman, beberapa informasi tambahan di mana Anda dapat melihat riwayat pembayaran pada alamat Anda, satoshi yang telah Anda tambang tetapi belum dibayar, dan total satoshi yang telah Anda tambang.

![signup](assets/8.webp)

Di sini, Anda dapat melihat bahwa dalam kotak **Estimated Time Until Minimum Payout**, tertulis Lightning karena kami telah menyiapkan penawaran BOLT12.

### Menyiapkan Penarikan Lightning
Seperti yang Anda pahami, Ocean bertujuan untuk memaksimalkan transparansi dan meminimalkan penyimpanan (menyimpan satoshi Anda atas nama Anda).
Itulah mengapa, untuk penarikan Lightning, diperlukan penggunaan **BOLT12 offers**. Ini adalah cara baru melakukan pembayaran di jaringan Lightning yang mulai muncul pada tahun 2024 dan memungkinkan beberapa hal:
- Ini adalah tautan pembayaran yang dapat digunakan kembali, memungkinkan pembayaran otomatis dan, tidak seperti alamat Lightning, BOLT12 bersifat non-custodial.
- Ini juga merupakan metode pembayaran yang memberikan bukti bahwa pembayaran telah dilakukan, yang tidak terjadi pada LNURLs.
- Sangat penting, ini dapat digunakan bersama dengan tanda tangan Bitcoin untuk membuktikan bahwa Anda adalah pemegang alamat BTC dan penawaran BOLT12.

Sampai hari ini (Mei 2024), sedikit solusi yang ada untuk menggunakan metode ini. Dalam contoh ini, kami akan menggunakan server Start9 dengan Core Lightning. Ketika alat lain, seperti Phoenix Wallet misalnya, telah mengintegrasikan penawaran BOLT12, tutorial ini akan tetap berlaku. Pastikan Anda memiliki saluran terbuka dengan likuiditas masuk, jika tidak pembayaran tidak akan berhasil.

Mulailah dengan pergi ke dashboard Anda di situs Ocean dengan memasukkan alamat BTC Anda, lalu klik pada tab **Configuration**.

![signup](assets/9.webp)

Kami akan menyalin teks **Description**, di sini:
`OCEAN Payouts for bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`

Sekarang pergi ke antarmuka Core Lightning Anda di server Start9 Anda (atau dompet mana pun yang mampu menyediakan penawaran BOLT12).

![signup](assets/10.webp)

Klik pada **Receive**.

Periksa **Offer**, lalu tempelkan teks yang sebelumnya disalin ke dalam bidang **Description** dan biarkan bidang **Amount** kosong.

![signup](assets/11.webp)

Klik pada **Generate Offer**.

![signup](assets/12.webp)

Anda telah menghasilkan tautan pembayaran yang dapat digunakan kembali dan permanen yang tidak memerlukan server pusat seperti halnya dengan alamat Lightning. Salin tautan tersebut lalu kembali ke halaman Ocean.

Di bidang **Lightning BOLT12 Offer**, tempelkan tautan pembayaran dan biarkan bidang **Block Height** pada nilai defaultnya. Klik pada **GENERATE**.

![signup](assets/13.webp)

Agar Ocean dapat memastikan bahwa tautan pembayaran ini memang milik Anda tanpa menggunakan sistem akun, Anda perlu menandatangani pesan yang baru saja dihasilkan dengan kunci privat Anda yang sesuai dengan alamat Bitcoin yang Anda gunakan. Banyak solusi yang ada untuk menandatangani pesan dengan kunci privat Anda. Dalam tutorial ini, kami akan mengambil contoh BlueWallet, tetapi metodenya sama untuk semua dompet.

![signup](assets/14.webp)

Dengan asumsi kunci privat Anda berada di BlueWallet (Anda dapat melakukan hal yang sama dengan dompet perangkat keras), klik pada dompet yang bersangkutan.

![signup](assets/15.webp)

Kemudian pada **…** di pojok kanan atas.

![signup](assets/15bis.webp)

Dan **Sign/Verify Message**.

![signup](assets/16.webp)

Di jendela ini, Anda memiliki tiga bidang: **Address**, **Signature**, dan **Message**.

Di bidang **Address**, masukkan alamat Bitcoin Anda. Jika kita kembali ke contoh kita, itu adalah alamat: `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`.

Biarkan bidang **Signature** kosong.
Dan tempelkan pesan yang dihasilkan ke dalam kolom **Pesan** di halaman Ocean: `{"height":845900,"lightning_bolt12":"lno1pg7y7s69g98zq5rp09hh2arnypnx7u3qvf3nzufjv4jrs7ncwyuxu6n3wdaxu6msxank5wp5dcc8samv89j8qv3jx36kscfjvempvggz84uzkn26vyzq8y2mr2s8fv0j76wesq43dz72kqrk33nl2tk9j45s"}`Klik pada **Sign**.

Ini akan menghasilkan tanda tangan kriptografis yang membuktikan Anda adalah pemilik alamat `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`, dan tanda tangan ini unik berkat pesan yang disediakan oleh Ocean, yang dihasilkan dari tautan pembayaran BOLT12.

![signup](assets/17.webp)

Salin tanda tangan tersebut dan tempelkan pada halaman Ocean, kemudian klik **CONFIRM**.

![signup](assets/18.webp)

Anda seharusnya melihat pesan konfirmasi.

![signup](assets/19.webp)

Sekarang pergi ke tab **My Stats**. Informasi tambahan ditampilkan di bagian atas dengan tautan pembayaran BOLT12 yang sebelumnya Anda hasilkan dengan Core Lightning di Start9.

![signup](assets/20.webp)