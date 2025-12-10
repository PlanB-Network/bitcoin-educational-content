---
name: LN Markets
description: Platform perdagangan Bitcoin pada Lightning Network
---

![cover](assets/cover.webp)



LN Markets adalah platform perdagangan Bitcoin asli Lightning pertama yang benar-benar asli Lightning, memungkinkan Anda untuk memperdagangkan turunan Bitcoin dengan leverage langsung dari wallet Lightning Anda, tanpa KYC, penyelesaian instan, dan penyimpanan minimal. Diluncurkan pada tahun 2020, platform ini menghilangkan hambatan pertukaran tradisional: tidak ada verifikasi identitas, tidak ada setoran yang diblokir, tidak perlu menunggu konfirmasi blockchain. wallet Lightning Anda menjadi akun trading Anda.



## Apa itu LN Markets?



LN Markets menawarkan **Futures** (kontrak perpetual dengan leverage hingga 100×) dan **Options** (Call/Put dengan risiko terbatas pada premi yang dibayarkan). Platform ini berfungsi sebagai lapisan agregasi likuiditas yang mengkonsolidasikan beberapa tempat perdagangan untuk eksekusi tanpa selip yang optimal. Dana Anda hanya terkunci selama durasi posisi aktif Anda, bukan berhari-hari atau berminggu-minggu seperti pada akun kustodian tradisional.



### Produk perdagangan yang tersedia



**Kontrak Berjangka (Kontrak Abadi)**



Kontrak abadi adalah kontrak berjangka tanpa tanggal kedaluwarsa, memungkinkan Anda untuk berspekulasi pada tren harga Bitcoin dengan leverage. LN Markets menawarkan dua mode manajemen margin:



**Mode terisolasi**: Setiap posisi memiliki margin tersendiri. Hanya dana yang dialokasikan untuk posisi spesifik ini yang berisiko. Jika posisi mencapai harga likuidasi, **hanya posisi ini yang dilikuidasi**, posisi Anda yang lain dan saldo yang tersisa tidak terpengaruh. Ideal untuk membatasi risiko per trade secara ketat.



**Mode Silang (Cross Margin)**: Margin dibagi di antara semua posisi terbuka Anda. Saldo total akun Anda berfungsi sebagai jaminan untuk semua posisi Anda. Jika suatu posisi mengalami kerugian, sistem akan menarik seluruh saldo yang tersedia untuk menghindari likuidasi. **Risiko**: jika saldo total Anda habis, semua posisi Anda mungkin dilikuidasi secara bersamaan. Direkomendasikan hanya untuk trader berpengalaman yang ingin memaksimalkan efisiensi modal.



**Manajemen posisi** :





- Posisi long**: Anda bertaruh pada kenaikan BTC/USD. Jika harga naik, Anda menang; jika harga turun, Anda kalah. **Contoh**: Bitcoin pada $100.000, Anda membuka posisi Long dengan 10.000 sats dan leverage 10×. Jika Bitcoin naik menjadi $105.000 (+5%), posisi Anda akan mendapatkan 50% (5% × 10), yaitu ~5.000 keuntungan sats. Jika Bitcoin turun menjadi $95.000 (-5%), Anda kehilangan 50%, yaitu kerugian ~5.000 sats.





- Posisi pendek**: Anda bertaruh pada penurunan BTC/USD. Jika harga turun, Anda menang; jika harga naik, Anda kalah. **Contoh**: Bitcoin pada $100.000, Anda membuka posisi short dengan 10.000 sats dan leverage 10×. Jika Bitcoin turun ke $95.000 (-5%), Anda menang 50%, yaitu ~5.000 sats. Jika Bitcoin naik menjadi $105.000 (+5%), Anda kalah 50%.



Leverage (hingga 100×) memperkuat keuntungan dan kerugian secara proporsional. Mekanisme **funding rate** (biaya berkala setiap 8 jam) menyeimbangkan posisi long dan short. Anda dapat mengelola hingga 100 posisi berjangka secara bersamaan.



** Pilihan**



Opsi adalah seperti **tiket lotere dengan tanggal kedaluwarsa**. Anda membayar premi untuk bertaruh pada arah harga Bitcoin. **Keuntungan utama**: Anda tidak akan pernah kehilangan lebih dari premi yang dibayarkan, tidak ada likuidasi yang mungkin terjadi.





- Opsi Panggilan (taruhan bullish)**: Anda bertaruh bahwa Bitcoin akan naik di atas harga kesepakatan sebelum kedaluwarsa. Anda menang jika harga naik, kerugian terbatas pada premi jika harga turun.





- Opsi Put (taruhan bearish)**: Anda bertaruh bahwa Bitcoin akan jatuh di bawah harga kesepakatan. Anda menang jika harga turun, kerugian terbatas pada premi jika harga naik.





- Straddle (taruhan volatilitas)**: Anda membeli Call DAN Put secara bersamaan. Anda menang jika Bitcoin membuat pergerakan besar ke arah mana pun, Anda kehilangan kedua premi jika harga tetap stabil.



Batas: 50 posisi simultan. Ideal untuk memulai trading dengan leverage tanpa takut likuidasi.



**sats ↔ sUSD**: Segera konversikan satoshi Anda menjadi dolar sintetis (sUSD) untuk melindungi diri Anda dari volatilitas, atau sebaliknya untuk mendapatkan eksposur Bitcoin.



## Akses platform dan pembuatan akun



### Pergi ke LN Markets



Buka [lnmarkets.com](https://lnmarkets.com) dan klik "Buka Aplikasi".



![Page d'accueil LN Markets](assets/fr/01.webp)



### Buat akun Anda



Layar selamat datang menawarkan beberapa metode koneksi:



![Méthodes de connexion](assets/fr/02.webp)



**Opsi tersedia**:


1. **Mendaftar dengan Lightning wallet** (disarankan): LNURL-auth dengan Phoenix, Breez, Zeus atau BlueWallet


2. **Daftar dengan email**: akun klasik (membatasi pengalaman Lightning)


3. **Alby** atau **Ledger**: ekstensi browser



### Koneksi melalui Lightning (LNURL-auth)



Klik "Daftarkan diri Anda dengan Lightning wallet". Pindai kode QR dengan Lightning wallet Anda:



![QR code LNURL-auth](assets/fr/03.webp)



wallet Anda secara otomatis menandatangani permintaan kriptografi dan akun Anda dibuat secara instan, tanpa email atau kata sandi. Keamanan yang kuat dan anonimitas total.



### Konfigurasi awal



![Configuration post-connexion](assets/fr/04.webp)



**Parameter yang tersedia** :




- Nama pengguna**: sesuaikan nama pengguna Anda
- Penarikan otomatis**: aktifkan penarikan otomatis ke wallet Anda setelah penutupan perdagangan
- Autentikasi Dua Faktor**: keamanan yang ditingkatkan dengan 2FA
- Dokumentasi**: mengakses sumber daya resmi



## Tur Interface



Antarmuka LN Markets disusun ke dalam beberapa bagian yang dapat diakses dari menu samping:



### Dasbor



![Dashboard](assets/fr/06.webp)



Menampilkan kinerja Anda berdasarkan jenis produk (Futures Cross, Futures Isolated, Options) dengan P&L, volume yang diperdagangkan, dan Address Lightning pribadi Anda (mis. `pivi@lnmarkets.com`).



### Profil



![Profil trader](assets/fr/07.webp)



Statistik terperinci: jumlah perdagangan, jenis pedagang (SCALPER, dll.), durasi posisi rata-rata, rincian Long/Short, tingkat kemenangan, rata-rata (jumlah, margin, leverage), dan struktur biaya progresif sesuai dengan volume.



### Perdagangan



![Historique des trades](assets/fr/08.webp)



Tab Perdagangan menampilkan riwayat lengkap posisi Anda, dengan semua metrik penting: tanggal pembuatan, arah (Long/Short), ukuran posisi (kuantitas), margin yang dikomitmenkan, harga masuk dan keluar, laba/rugi yang direalisasikan (P&L), dan biaya perdagangan. Anda dapat memfilter berdasarkan jenis produk (futures/opsi) dan mengekspor data Anda untuk analisis eksternal atau akuntansi.



### Pengaturan



![Paramètres de la plateforme](assets/fr/05.webp)



Tab Pengaturan menawarkan dua tab: **Akun** dan **Interface**.



*tab *Akun**:



Manajemen akun dengan bidang yang dapat diedit :




- Nama pengguna**: ubah nama pengguna Anda (mis. "pivi") dengan tombol "Perbarui"
- Email**: tambahkan/edit alamat email Anda
- Alamat bitcoin deposit**: alamat bitcoin yang dapat Anda gunakan untuk menyetor dana on-chain.



**Tiga sakelar konfigurasi**:




- Tampil di papan peringkat**: pilih apakah akan muncul di papan peringkat publik atau tidak
- Gunakan alamat Taproot**: gunakan alamat Bitcoin Taproot untuk setoran/penarikan on-chain
- Aktifkan penarikan otomatis**: aktifkan penarikan otomatis ke wallet Lightning Anda setelah penutupan perdagangan



**Migrasi akun**: Bagian yang memungkinkan Anda untuk memigrasikan akun Lightning Anda ke autentikasi email/kata sandi klasik.



*manajemen *Session**: tombol "Hapus sesi dan data lokal" untuk memutuskan sambungan dan membersihkan data browser lokal.



*tab *Interface**:



Sesuaikan pengalaman pengguna dengan tujuh sakelar:




- Lewati konfirmasi order**: menonaktifkan modal konfirmasi sebelum eksekusi perdagangan (perdagangan cepat)
- Tampilkan keterangan alat**: menampilkan keterangan alat saat mengarahkan kursor ke elemen
- Mode Privat (menyembunyikan data sensitif)**: menyembunyikan jumlah dan data sensitif di antarmuka (mode privasi)
- Tampilkan PL bersih di profil**: tampilkan laba/rugi bersih di profil publik Anda
- Gunakan ikon satuan**: menampilkan ikon untuk satuan mata uang (sats, $)
- Aktifkan notifikasi suara**: aktifkan notifikasi suara untuk peristiwa trading
- Aktifkan pemberitahuan desktop**: mengaktifkan pemberitahuan desktop sistem operasi



### Wallet



![Wallet](assets/fr/09.webp)



Saldo Bitcoin dan Sintetis USD dengan riwayat setoran, penarikan, transfer silang, swap, pendanaan, dan manajemen alamat on chain.



### API



![API V3](assets/fr/10.webp)



LN Markets menawarkan API REST (V2 dan V3) yang lengkap untuk mengotomatiskan trading Anda sepenuhnya melalui skrip atau bot. Anda dapat membuat kunci API dengan izin yang dapat disesuaikan (hanya-baca, perdagangan, penarikan) langsung dari antarmuka. TypeScript dan Python SDK resmi tersedia untuk integrasi yang mudah. Dokumentasi lengkap API V3 tersedia di [api.lnmarkets.com/v3] (https://api.lnmarkets.com/v3).



## Setoran dana pertama



Klik "Deposit". Ada tiga metode yang tersedia:



![Modal de dépôt](assets/fr/11.webp)



1. **LNURL**: pindai kode QR dengan wallet Lightning Anda


2. **Invoice**: masukkan jumlah lalu pindai faktur Lightning


3. ** On-Chain **: depot Bitcoin on chain



## Perdagangan dalam praktik



### Trade Futures Long: bertaruh pada sisi atas



Dari Dasbor, klik "Futures" lalu "Terisolasi". Klik **"Beli "** untuk membuka posisi Long.



![Interface Futures Long](assets/fr/12.webp)



Klik ikon **kalkulator** di sebelah tombol "Beli" untuk menampilkan kalkulator posisi:



![Calculateur de position Long](assets/fr/13.webp)



**Contoh konkret**:




- Jumlah**: $100 (ukuran posisi)
- Margin Perdagangan**: 12.336 sats (margin komitmen)
- Pengungkit**: 7.73× (setiap variasi 1% BTC = 7,73% dari modal Anda)
- Harga masuk** : $104,863.5
- Likuidasi**: $92.852 (harga likuidasi otomatis yang kritis)
- Harga keluar**: $110.000 (untuk perhitungan keuntungan)
- PL** : 4.492 sats (keuntungan jika keluar pada harga $110.000)



**Skenario** :




- Kenaikan +4,9%** ($110.000): keuntungan +4.492 sats (+36,4%)
- Netral** ($104.863): -185 sats (hanya biaya)
- Turun -11,5%** ($92.852): total likuidasi (-100%)



Klik tombol "Beli" untuk mengonfirmasi jual beli. **Dua kasus yang mungkin terjadi** :





- Jika Anda memiliki likuiditas** yang cukup di akun Anda: modal konfirmasi akan ditampilkan secara langsung (gambar di bawah). Klik "Ya" untuk mengeksekusi trade secara instan.



![Confirmation trade Long](assets/fr/14.webp)





- Jika Anda tidak memiliki cukup uang tunai**: kode QR Lightning akan ditampilkan. Pindai kode tersebut dengan wallet Lightning Anda untuk membayar margin yang diperlukan. Perdagangan terbuka secara otomatis setelah menerima pembayaran



### Perdagangan Futures Short: bertaruh pada sisi negatifnya



Klik **"Jual "** untuk membuka posisi Short (Anda menang jika harga turun). Buka kalkulator dengan ikon kalkulator untuk mengatur posisi Anda:



![Calculateur de position Short](assets/fr/15.webp)



Klik "Jual" untuk mengonfirmasi. Sedangkan untuk Long, **dua kemungkinan kasus**:





- Jika Anda memiliki cukup uang tunai**: mode konfirmasi langsung, klik "Ya"
- Jika Anda tidak memiliki cukup uang tunai**: kode QR Lightning akan ditampilkan (gambar di bawah). Pindai kode tersebut dengan wallet Lightning Anda untuk membayar margin yang diperlukan:



![Paiement Lightning pour Short](assets/fr/16.webp)



Setelah pembayaran Lightning diterima, posisi Short Anda akan terbuka secara otomatis. Anda bisa mengaturnya dari antarmuka trading.



#### Menutup posisi



Untuk menutup posisi Anda (Long atau Short), klik **silang kecil di pojok kanan bawah** pada antarmuka manajemen:



![Interface de clôture](assets/fr/17.webp)



Dialog konfirmasi ditampilkan untuk mengonfirmasi penutupan transaksi:



![Confirmation clôture](assets/fr/18.webp)



Modal menampilkan P&L (laba atau rugi) Anda saat ini. Klik "Ya" untuk menutup. Saldo akan langsung ditambahkan (untung) atau dikurangkan (rugi) dari Wallet Anda melalui Lightning.



### Opsi Perdagangan Panggilan: hak bersyarat untuk membeli



Opsi menawarkan **risiko terbatas** pada premi yang dibayarkan, tanpa kemungkinan likuidasi. Call memberi Anda hak (bukan kewajiban) untuk membeli Bitcoin pada harga kesepakatan sebelum kedaluwarsa. Tidak seperti kontrak berjangka, Anda tidak akan pernah kehilangan lebih dari premi yang diinvestasikan.



Dari Dasbor, klik "Opsi", lalu pilih tab "Panggilan".



![Interface Options Call](assets/fr/19.webp)



Konfigurasikan perdagangan Anda dengan parameter berikut:




- Kuantitas**: 100 dolar AS (ukuran kontrak Anda)
- Kadaluarsa** : 2025-11-15 (tanggal kedaluwarsa)
- Mogok**: $96.000 (harga target)



Bidang lainnya dihitung secara otomatis:




- Margin**: 1.045 sats (premi yang harus dibayar, investasi Anda)
- Titik impas**: $96.923 (harga untuk memulihkan saham Anda)
- Delta**: 40 (sensitivitas harga Bitcoin)



**Bagaimana cara menghitung kemenangan Anda?



Keuntungan Anda bergantung pada harga Bitcoin pada saat kedaluwarsa. Rumus: **(Harga BTC - Strike) × ukuran Contract - Premium yang dibayarkan**.



**Contoh konkret**:





- Bitcoin dengan harga $96.000** (harga saat ini): Nilai intrinsik = $0. **Kerugian: -1,045 sats** (Anda kehilangan premi)





- Bitcoin dengan harga $97.000**: Nilai intrinsik = (97.000 - 96.000) × 0,00105 BTC = $1,05. Dikonversi ke sats ≈ 2.175 sats. **Keuntungan: 2,175 - 1,045 = +1,130 sats** (keuntungan +108%)





- Bitcoin dengan harga $98.000**: nilai intrinsik = $2.000 ≈ 3.224 sats. **Keuntungan: +2.179 sats** (keuntungan +208%)





- Bitcoin dengan harga $100.000**: nilai intrinsik = $4.000 ≈ 5.263 sats. **Keuntungan: +4.218 sats** (keuntungan +403%)





- Bitcoin di bawah $96.000**: Opsi berakhir tanpa nilai. **Kerugian terbatas: -1.045 sats**, tidak ada likuidasi



Klik "Beli Panggilan". Kotak dialog konfirmasi akan muncul:



![Confirmation Call option](assets/fr/20.webp)



Klik "Beli Panggilan" sekali lagi untuk mengonfirmasi. Opsi akan muncul di "Running Options". Pada saat kedaluwarsa, LN Markets secara otomatis menghitung nilai intrinsik dan menyesuaikan keuntungan/kerugian Anda.



**Catatan tentang Opsi Put** : Pengoperasiannya identik dengan panggilan, tetapi secara terbalik. Dengan Put, Anda bertaruh pada harga Bitcoin akan **turun**. Jika Bitcoin jatuh di bawah harga kesepakatan Anda, Anda menang; jika tetap di atas, Anda hanya kehilangan premi yang dibayarkan. Perhitungan keuntungan mengikuti logika yang sama: **(Strike - harga BTC) × ukuran Contract - Premi yang dibayarkan**.



### Penarikan dana kilat



Klik "Tarik":



![Modal de retrait](assets/fr/21.webp)



**Metode** : LNURL, Invoice, Lightning Address, On-Chain.



*prosedur *Invoice**:


1. Buat faktur Lightning dari wallet Anda


2. Salin faktur (dimulai dengan `lnbc...`)


3. Rekatkan ke dalam bidang LN Markets


4. Konfirmasi penarikan dana


5. wallet Anda dikreditkan dalam 1-3 detik



Tidak ada biaya penarikan Lightning, hanya biaya perutean minimal (<0,1% dalam praktiknya).



## Risiko dan praktik terbaik



**Risiko utama** :




- Likuidasi total**: leverage tinggi dapat menghapus 100% margin dalam hitungan menit
- Layanan eksperimental**: fase alfa, ketidakpastian teknologi
- Risiko mitra pengimbang**: platform tetap menjadi mitra pengimbang tunggal



**Praktik terbaik** :



1. **Manajemen modal**: terapkan strategi manajemen risiko yang disesuaikan dengan profil Anda. Misalnya: alokasikan 5% dari total aset Anda untuk perdagangan dengan leverage, kemudian risikokan maksimum 1% dari modal ini per perdagangan (misalnya: aset 1 BTC → 5 juta sats untuk diperdagangkan → risiko maksimum 50 ribu sats per posisi)



2. **Stop-loss sistematis**: konfigurasikan stop-loss untuk membatasi kerugian Anda per trade. Dengan aturan risiko 1%, misalnya, bahkan 10 trade yang merugi secara beruntun hanya mewakili 10% dari modal trading Anda



3. **Mulai dari yang kecil**: uji coba terlebih dahulu dengan beberapa ribu dolar untuk memahami mekanismenya sebelum menerapkan strategi manajemen modal Anda



4. **Tarik keuntungan Anda secara teratur**: amankan keuntungan Anda di wallet utama Anda, hanya menyisakan modal perdagangan aktif di platform



5. **Waspadai leverage**: hindari leverage >20× kecuali jika Anda sepenuhnya menyadari risiko likuidasi



**Biaya**: tidak ada biaya deposit/penarikan Lightning, spread ~0,1% per perdagangan (turun menjadi 0,06% tergantung volume).



## Keuntungan dan keterbatasan



**Keuntungan**:




- Non-kustodian (kontrol total tidak termasuk periode perdagangan)
- Bebas KYC (anonimitas melalui Lightning/Nostr)
- Penyelesaian instan (setoran/penarikan dalam hitungan detik)
- Eksekusi tanpa selip dengan agregasi likuiditas
- Dukungan API publik dan Nostr



**Keterbatasan** :




- Layanan alfa (kemungkinan evolusi)
- Likuiditas lebih rendah dari Binance/Deribit
- Dilarang untuk penduduk AS



## Kesimpulan



LN Markets mewujudkan evolusi besar dari perdagangan Bitcoin dengan mengintegrasikan Lightning Network secara native untuk memberikan kontrol kembali kepada pengguna. Bagi para pengguna bitcoin yang ingin berspekulasi tanpa mengorbankan kedaulatan mereka, ini adalah alternatif unik untuk bursa terpusat tradisional.



Platform ini terus berkembang dengan perdagangan berjangka linier USDT dan perdagangan non-kustodian melalui Discreet Log Contracts (DLC) yang sedang dikembangkan. Dengan menerapkan praktik manajemen risiko yang baik (jumlah kecil, stop-loss, penarikan reguler), LN Markets menjadi alat yang ampuh untuk mengeksplorasi leverage Bitcoin secara bertanggung jawab.



Mulailah dari yang kecil, uji coba dengan beberapa ribu satss, dan secara bertahap jelajahi batas Lightning Network yang baru ini. Selamat berdagang berdaulat ⚡️!



## Sumber daya





- [Situs web resmi LN Markets](https://lnmarkets.com)
- [Dokumentasi](https://docs.lnmarkets.com)