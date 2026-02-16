---
name: Ocean Mining

description: Pengenalan tentang Ocean Mining
---

![signup](assets/cover.webp)

**Mei 2024**

Ocean Mining adalah pool penambangan yang cukup unik. Di sini, tidak diperlukan akun, alamat email, atau kata sandi. Sama seperti Bitcoin, semuanya transparan, pseudonim, dan kontributor dapat memilih dari empat template blok yang berbeda.

### Sistem Kompensasi

Sistem kompensasi Ocean disebut TIDES, “Transparent Index of Distinct Extended Shares”. Sistem ini mencatat pekerjaan yang diberikan oleh para penambang, yang dikenal sebagai “shares”. Pool menghitung persentase “shares” untuk setiap kontributor, lalu menambahkan alamat Bitcoin mereka ke dalam template blok pool sebagai penerima persentase dari hadiah blok tersebut.

Template blok diperbarui sekitar setiap 10 detik untuk memperhitungkan transaksi baru yang paling menguntungkan dan untuk menyesuaikan distribusi hadiah blok jika diperlukan.

![signup](assets/rem.webp)

Apakah mesin kamu terhubung atau tidak saat pool menambang blok baru tidak menjadi masalah. Pekerjaan yang sudah diserahkan akan disimpan untuk delapan blok berikutnya yang ditemukan oleh pool.

Menyimpan pekerjaan untuk delapan blok, alih-alih mereset penghitung ke nol setiap kali blok baru ditambang, berarti kompensasi kamu baru akan mencapai 100% setelah pool menemukan delapan blok sejak kamu mulai berkontribusi. Ini juga berarti kamu akan tetap menerima kompensasi untuk delapan blok meskipun kamu berhenti berkontribusi ke pool.

Mekanisme ini meratakan kompensasi dan mencegah “pool hopping”, yaitu praktik berpindah-pindah pool secara rutin tergantung pada pool mana yang paling berpeluang menemukan blok berikutnya.

### Penarikan

Operasi Ocean Mining memungkinkan para kontributornya untuk memperoleh bitcoin “bersih”, yaitu bitcoin yang langsung dihasilkan dari hadiah blok.

Berbeda dengan sebagian besar pool lainnya, Ocean tidak menerima bitcoin yang baru ditambang; alamat kontributor langsung diintegrasikan ke dalam template blok.

Untuk saat ini, jumlah minimum agar benar-benar bisa mendapatkan manfaat dari bitcoin bersih adalah 1.048.576 sats. Dengan setiap blok yang ditambang oleh pool, porsi “shares” kamu harus memberikan hak atas lebih dari 1.048.576 sats agar dapat langsung dibayarkan kepadamu dari hadiah blok. Jika tidak, sats kamu akan disimpan oleh Ocean sampai total hadiahmu melebihi jumlah tersebut.

Semua bitcoin yang sementara disimpan oleh Ocean berada di alamat ini: [37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n, semuanya dapat diverifikasi di TimeChain.](https://mempool.space/address/37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n)
Juga dimungkinkan untuk menarik sats melalui Lightning menggunakan BOLT12. Kita akan melihat cara mengaturnya.

### Biaya Pool

Biaya berkisar dari 0% hingga 2% tergantung pada template blok yang dipilih.

## Transparansi Ocean

### Data Kontributor

![signup](assets/1.webp)

Semua informasi tentang kolam transparan, termasuk semua data pengguna. Untuk memahami poin ini, mari kita ambil contoh:

[Di dashboard Ocean](https://ocean.xyz/dashboard), Anda memiliki banyak informasi seperti hashrate selama enam bulan terakhir, jumlah peserta di pool, total jumlah bitcoin yang ditambang, dll.

Kita akan fokus pada bagian "Kontributor". Kamu dapat melihat daftar semua kontributor dengan hashrate rata-rata mereka selama tiga jam terakhir serta persentase **"shares"** dan **"hash"** relatif terhadap sisanya di pool.
**"Shares %"** adalah persentase pekerjaan yang disediakan oleh kontributor dalam jendela delapan blok terakhir dibandingkan dengan sisanya di kolam.
**"Hash %"** adalah persentase rata-rata hashrate yang disediakan oleh kontributor selama tiga jam terakhir dibandingkan dengan sisanya di pool.

![signup](assets/2.webp)

Pool akan melihat bahwa "Kontributor" diidentifikasi dengan alamat Bitcoin. Kamu bisa mengklik salah satu alamat ini untuk detail lebih lanjut.

Jika kita mengambil yang pertama, yang memiliki hashrate tertinggi [1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ](https://ocean.xyz/stats/1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ), Kamu dapat melihat semua detail tentang pengguna ini: hashrate, jumlah bitcoin yang ditambang, dengan blok mana, dan bahkan detail dari setiap mesin mereka (ASICs). Namun, mereka tetap anonim, seperti pada Bitcoin.

### Template Blok

Di kiri atas pada dashboard, kamu bisa melihat “Blok Selanjutnya”. Di halaman ini, ada empat template blok yang berbeda. Ocean memungkinkan setiap kontributor untuk memilih template blok yang ingin mereka dukung. Pilihan ini tidak berdampak langsung pada kompensasi kamu. Ketika pool menambang sebuah blok, semua kontributor tetap dikompensasi tanpa memandang template yang mereka pilih. Fitur ini hanya memberi kebebasan bagi setiap orang untuk “memilih” template blok yang paling sesuai dengan preferensi mereka.

![signup](assets/3.webp)

**CORE:** Biaya 2%, ini adalah template Bitcoin Core klasik tanpa filter, seperti tertulis di halaman mereka "Termasuk transaksi dan mayoritas spam"

**CORE+ANTISPAM:** Biaya 0%, Bitcoin Core dengan filter terhadap transaksi tertentu seperti Ordinals "Termasuk transaksi dan membatasi spam"

**OCEAN:** Biaya 0%, Bitcoin Knot "Hanya termasuk transaksi dan data yang cukup kecil"

**DATA-FREE:** Biaya 0%, Bitcoin Knot "Hanya termasuk transaksi tanpa data sembarangan"

### Perbedaan antara Bitcoin Core dan Bitcoin Knot
Bitcoin Core adalah perangkat lunak yang memungkinkan sekitar 99% node Bitcoin di seluruh dunia untuk beroperasi. Bitcoin adalah sebuah protokol, yang berarti bahwa, seperti Internet yang memiliki beberapa browser, bisa ada beberapa perangkat lunak berbeda yang beroperasi secara berdampingan pada TimeChain yang sama. Namun, karena kekhawatiran soal kompatibilitas dan untuk membatasi risiko bug yang dapat meninggalkan jejak permanen di TimeChain, hampir semua pengembang Bitcoin bekerja pada Bitcoin Core.

Bitcoin Knots adalah fork dari Bitcoin Core, yang berarti ia membagikan sebagian besar basis kode yang sama, sehingga risiko bug sangat dibatasi. Fork ini dibuat oleh Luke Dashjr, yang ingin menerapkan aturan yang lebih restriktif dibandingkan Bitcoin Core tanpa menciptakan hard fork. Saat ini, Bitcoin Core dan Bitcoin Knots dapat berkoeksistensi berkat konsensus Nakamoto.

## Menambahkan Pekerja

Untuk menambahkan pekerja, mulailah dengan memilih template blok kamu. Pilihan ini akan menentukan URL pool yang harus dimasukkan pada penambang Anda (ASICs).

- **CORE**: `stratum+tcp://core.mine.ocean.xyz:3202`
- **CORE+ANTISPAM**: `stratum+tcp://ordis.mine.ocean.xyz:3303`
- **OCEAN**: `stratum+tcp://mine.ocean.xyz:3334`
- **DATA-FREE**: `stratum+tcp://datafree.mine.ocean.xyz:3404`

Selanjutnya, untuk bidang pengguna, masukkan alamat Bitcoin yang kamu miliki. Berikut adalah daftar jenis alamat yang kompatibel:
- **P2PKH** (Tipe alamat asli. Dimulai dengan “1”)
- **P2SH** (Multisignature atau P2SH-Segwit. Dimulai dengan “3”)
- **Bech32** (Segwit. Dimulai dengan “bc”.)
- **Bech32m** (Taproot. Dimulai dengan “bc”. Lebih panjang dari Bech32.)

Jika kamu memiliki beberapa penambang, kamu bisa memasukkan alamat yang sama untuk semuanya sehingga hash rate mereka digabungkan dan ditampilkan sebagai satu penambang. Kamu juga bisa membedakan masing-masing dengan menambahkan nama yang berbeda. Untuk melakukannya, cukup tambahkan “.namapenambang” setelah alamat Bitcoin.

Akhirnya, untuk kolom kata sandi, gunakan `x`.

**Contoh:**
Jika kamu memilih template **OCEAN**, alamat Bitcoin Anda adalah `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv` dan kamu ingin menamai penambang Anda “Brrrr”, maka kamu perlu memasukkan informasi berikut di antarmuka penambang Anda:

- **URL**: `stratum+tcp://mine.ocean.xyz:3334`
- **USER**: `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr`
- **PASSWORD**: `x`

Beberapa menit setelah memulai penambangan, Anda akan dapat melihat data Anda di situs Ocean dengan mencari alamat Anda.

### Ikhtisar Dashboard
- **Saham dalam Jendela Hadiah**: Data ini menunjukkan jumlah saham, pekerjaan yang kamu kirim ke kolam dalam jendela 8 blok terakhir yang ditambang oleh pool.
- **Perkiraan Hadiah dalam Jendela**: Perkiraan jumlah satoshi yang akan kamu peroleh dengan pekerjaan yang sudah dilakukan. Ini tidak memperhitungkan biaya transaksi, hanya coinbase, bitcoin baru yang dikeluarkan oleh jaringan.
- **Perkiraan Pendapatan Blok Berikutnya**: Perkiraan jumlah satoshi yang diperoleh jika blok ditambang sekarang. Ingat, jika nilai ini kurang dari 1,048,576 satoshi, kamu tidak akan langsung menerima satoshi ke alamat kamu. Mereka akan dikirim ke alamat Ocean sampai pendapatan kamu melebihi ambang batas ini.

Di bawah ini, kamu memiliki grafik yang menampilkan riwayat hash rate kamu hingga 6 bulan.

![signup](assets/4.webp)

Di sini, kamu memiliki rata-rata hash rate dalam berbagai skala waktu, dari 60 detik hingga 24 jam, serta riwayat blok yang ditambang oleh pool untuk kamu yang telah berkontribusi dan diberi hadiah.

![signup](assets/5.webp)

Kamu memiliki opsi untuk mengekspor file CSV dari riwayat ini dengan tombol **Download CSV**.

![signup](assets/6.webp)

Di bagian berikutnya, kamu akan melihat daftar semua penambang yang sudah kamu hubungkan ke pool menggunakan alamat ini. Di sana, kamu bisa melihat hash rate masing-masing penambang, serta jumlah satoshi yang mereka terima secara individual atas pekerjaan yang mereka lakukan.

![signup](assets/7.webp)

Kamu dapat mengklik pada **Nickname** dari penambang mana pun. Kemudian kamu akan memiliki semua informasi yang baru saja kita lihat, tetapi secara spesifik untuk penambang tersebut.

Dan di bagian bawah halaman, ada beberapa informasi tambahan yang menampilkan riwayat pembayaran ke alamat kamu, jumlah satoshi yang sudah kamu tambang tetapi belum dibayarkan, serta total satoshi yang telah kamu tambang.

![signup](assets/8.webp)

Di sini, kamu bisa melihat bahwa pada kotak **Estimated Time Until Minimum Payout**, tertulis Lightning karena kami sudah menyiapkan penawaran BOLT12.

### Menyiapkan Penarikan Lightning
Seperti yang kamu pahami, Ocean bertujuan untuk memaksimalkan transparansi dan meminimalkan penyimpanan (menyimpan satoshi atas nama kamu).
Itulah mengapa, untuk penarikan Lightning, diperlukan penggunaan **BOLT12 offers**. Ini adalah cara baru melakukan pembayaran di jaringan Lightning yang mulai muncul pada tahun 2024 dan memungkinkan beberapa hal:
- Ini adalah tautan pembayaran yang dapat digunakan kembali, memungkinkan pembayaran otomatis dan, tidak seperti alamat Lightning, BOLT12 bersifat non-custodial.
- Ini juga merupakan metode pembayaran yang memberikan bukti bahwa pembayaran telah dilakukan, yang tidak terjadi pada LNURLs.
- Sangat penting, ini dapat digunakan bersama dengan tanda tangan Bitcoin untuk membuktikan bahwa kamu adalah pemegang alamat BTC dan penawaran BOLT12.

Sampai hari ini (Mei 2024), masih sedikit solusi yang tersedia untuk menggunakan metode ini. Dalam contoh ini, kami akan menggunakan server Start9 dengan Core Lightning. Ketika alat lain, seperti Phoenix Wallet misalnya, sudah mengintegrasikan penawaran BOLT12, tutorial ini akan tetap relevan. Pastikan kamu memiliki saluran terbuka dengan likuiditas masuk, jika tidak pembayaran tidak akan berhasil.

Mulailah dengan pergi ke dashboard kamu di situs Ocean dengan memasukkan alamat BTC milikmu, lalu klik pada tab **Configuration**.

![signup](assets/9.webp)

Kami akan menyalin teks **Description**, di sini:
`OCEAN Payouts for bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`

Sekarang pergi ke antarmuka Core Lightning kamu di server Start9 kamu (atau dompet mana pun yang mampu menyediakan penawaran BOLT12).

![signup](assets/10.webp)

Klik pada **Receive**.

Periksa **Offer**, lalu tempelkan teks yang sebelumnya disalin ke dalam bidang **Description** dan biarkan bidang **Amount** kosong.

![signup](assets/11.webp)

Klik pada **Generate Offer**.

![signup](assets/12.webp)

Kamu telah menghasilkan tautan pembayaran yang dapat digunakan kembali dan bersifat permanen, yang tidak memerlukan server pusat seperti pada alamat Lightning. Salin tautan tersebut, lalu kembali ke halaman Ocean.

Di bidang **Lightning BOLT12 Offer**, tempelkan tautan pembayaran dan biarkan bidang **Block Height** pada nilai defaultnya. Klik pada **GENERATE**.

![signup](assets/13.webp)

Agar Ocean bisa memastikan bahwa tautan pembayaran ini benar-benar milik kamu tanpa menggunakan sistem akun, kamu perlu menandatangani pesan yang baru saja dihasilkan menggunakan private key yang sesuai dengan alamat Bitcoin yang kamu gunakan. Ada banyak solusi yang tersedia untuk menandatangani pesan dengan private key kamu. Dalam tutorial ini, kami akan menggunakan BlueWallet sebagai contoh, tetapi metodenya sama untuk semua wallet.

![signup](assets/14.webp)

Dengan asumsi private key kamu berada di BlueWallet (kamu juga bisa melakukan hal yang sama dengan hardware wallet), klik dompet yang bersangkutan.

![signup](assets/15.webp)

Kemudian pada **…** di pojok kanan atas.

![signup](assets/15bis.webp)

Dan **Sign/Verify Message**.

![signup](assets/16.webp)

Di jendela ini, kamu memiliki tiga bidang: **Address**, **Signature**, dan **Message**.

Di bidang **Address**, masukkan alamat Bitcoin kamu. Jika kita kembali ke contoh kita, itu adalah alamat: `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`.

Biarkan bidang **Signature** kosong.
Dan tempelkan pesan yang dihasilkan ke dalam kolom **Pesan** di halaman Ocean: `{"height":845900,"lightning_bolt12":"lno1pg7y7s69g98zq5rp09hh2arnypnx7u3qvf3nzufjv4jrs7ncwyuxu6n3wdaxu6msxank5wp5dcc8samv89j8qv3jx36kscfjvempvggz84uzkn26vyzq8y2mr2s8fv0j76wesq43dz72kqrk33nl2tk9j45s"}`Klik pada **Sign**.

Ini akan menghasilkan tanda tangan kriptografis yang membuktikan kamu adalah pemilik alamat `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`, dan tanda tangan ini unik berkat pesan yang disediakan oleh Ocean, yang dihasilkan dari tautan pembayaran BOLT12.

![signup](assets/17.webp)

Salin tanda tangan tersebut dan tempelkan pada halaman Ocean, kemudian klik **CONFIRM**.

![signup](assets/18.webp)

Kamu akan melihat pesan konfirmasi.

![signup](assets/19.webp)

Sekarang pergi ke tab **My Stats**. Informasi tambahan ditampilkan di bagian atas dengan tautan pembayaran BOLT12 yang sebelumnya kamu hasilkan dengan Core Lightning di Start9.

![signup](assets/20.webp)
