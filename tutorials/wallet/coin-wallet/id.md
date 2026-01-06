---
name: Coin Wallet
description: Tutorial tentang Coin Wallet dan cara-cara untuk meningkatkan privasi dan keamanan
---

![cover](assets/cover.webp)


Tutorial ini mencakup [Coin Wallet](https://coin.space/) - kripto kustodian mandiri wallet untuk perangkat seluler, dan cara meningkatkan keamanan dan privasi saat menggunakan aplikasi wallet seluler.



## Tentang Coin Wallet


**Coin Wallet** adalah wallet sumber terbuka yang bersifat self-custodial/non-custodial yang dibuat oleh tim penggemar Bitcoin pada tahun 2015. Dimulai sebagai aplikasi web, diikuti oleh aplikasi iOS pada tahun 2017, dan aplikasi Android pada tahun 2020 - tersedia di Google Play, Samsung Galaxy Store, dan Huawei AppGallery.


Keunggulan utama:


- Arsitektur non-kustodian
- Sepenuhnya [kode sumber terbuka](https://github.com/CoinSpace/CoinSpace/blob/master/LICENSE)
- Desain yang sederhana dan bersih
- Berfokus pada tujuan utama - menyimpan mata uang kripto dengan aman, tanpa fitur yang tidak perlu
- Dukungan lintas platform: seluler (iOS & Android), desktop, web
- Dukungan RBF (Ganti-Berdasarkan-Biaya) - mempercepat transaksi yang macet kapan saja
- Perangkat keras 2FA dengan [YubiKey](https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/) / kunci FIDO2
- Dukungan Tor bawaan - rutekan semua lalu lintas melalui jaringan Tor untuk privasi maksimum



## 1️⃣ Menginstalasi Coin Wallet

Coin Wallet tersedia di semua platform utama.



- [iOS App Store](https://apps.apple.com/app/coin-wallet-bitcoin-crypto/id980719434)



- [Android Google Play](https://play.google.com/store/apps/details?id=com.coinspace.app)



- [Android (Galaxy Store)](https://galaxystore.samsung.com/detail/com.coinspace.app)



- [Android (Huawei AppGallery)](https://appgallery.huawei.com/app/C112183767)



- [Android (Uptodown)](https://coin-wallet.en.uptodown.com/android)



- [Android APK](https://coin.space/api/v3/download/android-apk/any)



- [Semua tautan rilis](https://github.com/CoinSpace/CoinSpace/releases)


Juga tersedia untuk desktop (Windows, Linux, macOS), sebagai aplikasi web dan melalui Tor.


![image](assets/en/01.webp)


## 2️⃣ Membuat Wallet dan Mengatur PIN


wallet dibuat menggunakan passphrase - urutan acak 12 kata yang dipisahkan oleh spasi, yang dihasilkan dari [daftar 2048 kata](https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts).

Coin Wallet mendukung 12, 15, 18, 21, atau 24 kata sandi yang diimpor dari dompet lain.


passphrase adalah bentuk yang dapat dibaca oleh manusia dari kunci pribadi utama. Ini harus disimpan dengan aman. passphrase adalah semua yang diperlukan untuk mengakses atau memulihkan wallet. Jika passphrase hilang, maka wallet dan semua dana akan hilang secara permanen. passphrase tidak boleh dibagikan. Coin Wallet tidak menyimpan kunci di server atau database mana pun.


**Apakah 12 kata passphrase aman?

Dengan 2048 kemungkinan kata per posisi, terdapat 2048¹² ≈ 10³⁹ kombinasi - memberikan keamanan ~128 bit, sebanding dengan kunci privat Bitcoin. Tingkat ini secara luas dianggap cukup.


![image](assets/en/02.webp)


Setelah passphrase dituliskan dan dikonfirmasi, aplikasi akan meminta Anda untuk menetapkan **4 digit PIN** untuk akses sehari-hari. Untuk menambah kenyamanan, Anda dapat mengaktifkan autentikasi biometrik (sidik jari atau pengenalan wajah) alih-alih menggunakan PIN.


![image](assets/en/03.webp)



Tidak ada akun, tidak ada pemulihan kunci, tidak ada pengaturan ulang passphrase, dan tidak ada pembalikan transaksi. Keamanan adalah tanggung jawab penuh pengguna.


Untuk praktik terbaik yang mendetail tentang cara menyimpan frasa mnemonik:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 3️⃣ Kata Sandi + PIN. Kapan dan Bagaimana Mereka Digunakan


**Kapan passphrase diperlukan?

Hanya dalam kasus yang jarang terjadi ini:


- Menyiapkan wallet pada perangkat baru
- Menginstal ulang aplikasi Coin Wallet
- Menghapus data aplikasi/peramban (Penyimpanan Lokal)
- Menghapus kunci perangkat keras dari akun
- Memasukkan PIN yang salah sebanyak tiga kali (aplikasi akan terkunci untuk keamanan)


Dalam penggunaan sehari-hari, PIN 4 digit sudah cukup untuk membuka kunci wallet.


**Kata Sandi + PIN: Cara Kerjanya**

passphrase adalah kunci privat master yang sebenarnya dan berfungsi pada perangkat apa pun.

Karena mengetik 12-24 kata setiap kali akan merepotkan, Coin Wallet menggunakan PIN 4 digit untuk akses cepat sehari-hari pada perangkat saat ini.

PIN sederhana saja tidak cukup aman untuk melindungi kunci utama secara langsung, sehingga tidak pernah digunakan untuk enkripsi. Sebaliknya:



- PIN dikirim ke server dan ditukar dengan kriptografi panjang token.
- token ini mendekripsi kunci master terenkripsi yang disimpan hanya pada perangkat.


Jika PIN dimasukkan secara salah sebanyak tiga kali, server akan menghapus token secara permanen. Kunci yang tersimpan secara lokal menjadi tidak dapat digunakan, dan satu-satunya cara untuk memulihkan wallet adalah dengan memasukkan passphrase yang asli.

Desain ini memberikan kenyamanan dan perlindungan jatuh yang kuat.



## 4️⃣ Menerima ₿itcoin - Jenis dan Privasi Address


Coin Wallet mendukung ketiga format alamat Bitcoin:



- Native SegWit (Bech32)** - dimulai dengan **bc1q** - biaya terendah, direkomendasikan
- SegWit bersarang (P2SH)** - dimulai dengan **3**
- Warisan (P2PKH)** - dimulai dengan **1**


![image](assets/en/04.webp)


**Mengapa alamat berubah setelah setiap deposit?

Hal ini disengaja dan melindungi privasi. Setiap kali koin diterima, Coin Wallet secara otomatis membuat alamat baru yang tidak terpakai. Jika alamat yang sama digunakan kembali (misalnya, untuk gaji bulanan), siapa pun dapat dengan mudah menjumlahkan semua transaksi yang masuk pada penjelajah blockchain dan mengetahui total pendapatan.


Alamat lama tetap berlaku selamanya - Anda masih bisa menerima email dari alamat tersebut - tetapi menggunakan alamat baru setiap kali adalah praktik terbaik privasi yang direkomendasikan.


**Cara menerima Bitcoin:**

1. Buka koin

2. Ketuk **Terima**

3. Pilih jenis alamat yang diinginkan (sebaiknya **bc1q** - `Native SegWit`)

4. Tunjukkan kode QR atau salin alamat dan kirimkan ke pembayar


**Opsional - Mecto (untuk pembayaran secara langsung):**

Pada layar Receive yang sama, terdapat tombol `Mecto`.

Saat Anda menyalakannya:


- Anda akan diminta untuk memasukkan **nickname** (nama panggilan)
- Lokasi Anda saat ini + alamat penerimaan untuk sementara dibagikan dengan pengguna Coin Wallet lainnya yang juga mengaktifkan Mecto
- Mereka dapat menemukan Anda di peta kecil dan mengirim koin tanpa mengetik atau memindai


Data hanya dapat dilihat oleh pengguna Mecto lainnya dan secara otomatis dihapus setelah 1 jam (atau segera setelah Anda mematikannya).

Mecto sepenuhnya opsional - tinggalkan saja jika Anda lebih suka privasi maksimum.


![image](assets/en/05.webp)


## 5️⃣ Mengirim ₿itcoin


Untuk mengirim Bitcoin:


1. Buka koin → ketuk **Kirim**

2. Rekatkan alamat atau pindai kode QR

3. Masukkan jumlah (atau ketuk **Max**)

4. Pilih kecepatan transaksi:


| Speed   | Approx. confirmation time | Fee level     |
|---------|---------------------------|---------------|
| **Slow**    | ~120 minutes              | Lowest
| **Default** | ~60 minutes               | Medium
| **Fast**    | ~20 minutes               | Higher

5. Konfirmasi dengan 4 digit PIN Anda → transaksi disiarkan


### Cara mempercepat transaksi ₿itcoin yang tertunda (RBF)


Jika Anda memilih biaya lambat dan transaksi macet:


1. Buka tab **History** (Riwayat)

2. Ketuk transaksi yang tertunda

3. Ketuk **Accelerate** (Ganti-Biaya)

4. Konfirmasi → transaksi akan disiarkan ulang dengan biaya yang lebih tinggi


Akselerasi RBF saat ini didukung untuk:

Bitcoin - Avalanche - Binance Smart Chain - Ethereum - Ethereum Classic - Polygon


Lebih lanjut tentang Replace-by-fee (RBF): https://bitcoinops.org/en/topics/replace-by-fee/


## 6️⃣ Mengekspor Kunci Pribadi


**Kapan Anda benar-benar membutuhkan kunci pribadi?

(99% pengguna tidak pernah melakukannya - 12 kata passphrase sudah cukup)


| Situation                                      | Why you need the private key                     |
|------------------------------------------------|--------------------------------------------------|
| Sweeping an old paper wallet                   | To move funds to your current wallet             |
| Importing into a hardware signer (e.g. Coldcard) | For offline signing                              |
| Emergency recovery (lost seed but app still open) | To rescue coins before the app is gone           |
| Using tools that don’t accept seed phrases     | Some watch-only or signing utilities             |

### Cara mengekspor kunci privat di Coin Wallet


1. Buka **Bitcoin (BTC)**

2. Gulir ke bagian bawah halaman - ketuk **Ekspor kunci pribadi**

3. Aplikasi ini menampilkan setiap alamat dengan saldo + kunci privatnya dalam format **WIF** (dimulai dengan 5, K, atau L) dan kode QR.


Hanya alamat yang tidak kosong yang muncul.


**Contoh kunci WIF**

`L2v1eK4i9j3k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k`


**Apa yang harus dilakukan selanjutnya (disarankan)**


- Buka Electrum, Sparrow, BlueWallet, atau perangkat keras apa pun wallet
- Impor/Sapu kunci pribadi
- Semua dana langsung berpindah ke alamat baru yang aman di bawah seed Anda saat ini


Jangan pernah menyimpan kunci pribadi secara digital dalam bentuk teks biasa. Setelah disapu, kunci ini dapat dihapus dengan aman.


Untuk panduan lengkap mengenai private key dan jalur derivasi: [Cara Bekerja dengan Private Key: Panduan Utama](https://coin.space/how-to-work-with-private-keys-the-ultimate-guide/)



## 7️⃣ Rincian Teknis - BIP39, BIP32 dan Jalur Turunan


Coin Wallet secara ketat mengikuti standar resmi Bitcoin yang digunakan oleh hampir semua dompet yang serius.


`BIP39` - bagaimana passphrase menjadi kunci pribadi utama


- Jumlah kata default: 12
- passphrase/kata sandi opsional: tidak ada ("")
- Entropi awal: 128 bit (12 kata) → 256 bit (24 kata)
- Implementasi sumber terbuka: https://github.com/paulmillr/scure-bip39
- Daftar kata: daftar bahasa Inggris standar yang terdiri dari 2048 kata
- Mendukung impor frasa 12, 15, 18, 21, dan 24 kata dari BIP39 wallet lainnya


`BIP32 + BIP44/BIP49/BIP84` - pembuatan semua alamat secara deterministik

Dari satu kunci utama, wallet dapat mengakses milyaran alamat dengan urutan yang ditentukan secara ketat. Inilah sebabnya mengapa 12 kata yang sama yang dimasukkan ke dalam Electrum, Sparrow, Trezor, Ledger, BlueWallet, dll. akan menunjukkan alamat dan saldo yang sama persis.


**Jalur derivasi yang digunakan dalam Coin Wallet untuk Bitcoin**


| Address type              | Standard | Derivation path       | Starts with | Comment                              |
|---------------------------|----------|-----------------------|-------------|--------------------------------------|
| Native SegWit (Bech32)    | BIP84    | `m/84'/0'/0'`         | bc1q…       | Modern format, lowest fees           |
| Nested SegWit (P2SH)      | BIP49    | `m/49'/0'/0'`         | 3…          | Compatibility wrapper for old services |
| Legacy (P2PKH)            | BIP44    | `m/44'/0'/0'`         | 1…          | Oldest format, highest fees          |

Di dalam setiap jalur:


- `/0` - rantai eksternal (alamat yang Anda tunjukkan untuk menerima pembayaran)
- `/1` - rantai internal (mengubah alamat yang digunakan oleh wallet itu sendiri)


Karena Coin Wallet mengikuti standar publik ini tanpa perubahan apa pun, dana Anda akan tetap dapat dipulihkan di wallet lain yang kompatibel bahkan dalam 10-20-30 tahun.


## 8️⃣ Meningkatkan Anonimitas dengan Tor


**Mengapa menggunakan Tor di Coin Wallet**

Tor menyembunyikan alamat IP asli Anda dari node Bitcoin, pertukaran, dan pengamat.

Semua lalu lintas (saldo, transaksi, swap) melewati jaringan Tor - tidak ada koneksi langsung, tidak ada kebocoran IP.

Hal ini diimplementasikan secara langsung di dalam kode sumber aplikasi (lihat [.env configuration](https://github.com/CoinSpace/CoinSpace/blob/master/web/.env#L31)).


Coin Wallet memiliki alamat .onion yang tersembunyi dan, sejak v6.6.3 (Desember 2024), **dukungan Tor bawaan langsung di aplikasi seluler**.


### Cara mengaktifkan Tor di Android & iOS


1. **Instal Orbot** - aplikasi resmi Tor Project (gratis)


   - Android → [Google Play](https://play.google.com/store/apps/details?id=org.torproject.android) / [F-Droid](https://orbot.app/en/)
   - iPhone / iPad → [App Store](https://apps.apple.com/us/app/orbot/id1609461599)


2. **Buka Orbot → ketuk Mulai**

Pilih **Coin Wallet** dari daftar sehingga hanya wallet yang menggunakan Tor (opsional, tetapi disarankan)

Tunggu hingga muncul tulisan **"Tersambung "** (10-30 detik)


3. **Buka Coin Wallet → Pengaturan → Jaringan**

Nyalakan **Gunakan Tor**


4. **Periksa status**

Ikon **bawang Tor berwarna ungu** muncul di bilah atas → semua lalu lintas sekarang dialihkan melalui Tor


![image](assets/en/06.webp)


Itu saja - ponsel Anda Coin Wallet sepenuhnya anonim.


Nikmati manajemen kripto pribadi!


## 📝 Kesimpulan


[Coin Wallet](https://coin.space/) - salah satu pelopor Bitcoin wallet yang sesungguhnya dengan sejarah pengembangan selama 10 tahun.

Ini sengaja dibuat sederhana dan tetap fokus pada misi utamanya: menyimpan mata uang kripto Anda dengan aman.

Tidak ada iklan, tidak ada umpan berita, tidak ada langganan, tidak ada fitur sosial, tidak ada gangguan - hanya wallet yang bersih, cepat, dan dapat menjaga diri sendiri yang melakukan apa yang seharusnya dilakukan.

Coin Wallet mengutamakan kesederhanaan dan keamanan - selalu dan akan selalu.


## 📖 Sumber Daya


https://coin.space/


https://support.coin.space/hc/en-us


https://en.bitcoin.it/wiki/Wallet


https://bitcoinops.org/


https://github.com/CoinSpace/CoinSpace/


https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/


https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts


https://github.com/paulmillr/scure-bip39