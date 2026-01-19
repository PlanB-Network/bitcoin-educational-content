---
name: Bull Bitcoin Wallet
description: Ketahui cara menggunakan Wallet Bull Bitcoin
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=6b0xTB2sE8E)


*Video tutorial dari BTC Sessions ini memandu Anda melalui proses pengaturan dan penggunaan Bull Bitcoin Wallet!


Panduan ini memandu Anda melalui instalasi, konfigurasi, dan penggunaan Bull Bitcoin Wallet. Anda akan belajar mengirim dan menerima dana pada jaringan Bitcoin On-Chain, Liquid, dan Lightning, serta cara memindahkan Bitcoin di antara jaringan-jaringan tersebut. Fitur wallet yang luas menjadikannya alat yang kuat dan lengkap untuk mengelola Bitcoin Anda. Mari kita mulai.


## Pendahuluan


Bull Bitcoin Wallet, yang dikembangkan oleh [Bull Bitcoin](https://www.bullbitcoin.com/), merupakan sebuah **self-custodial** Bitcoin wallet, yang berarti Anda memiliki kontrol penuh atas kunci pribadi Anda dan juga dana Anda, tanpa bergantung pada pihak ketiga. Bersifat open-source dan berakar pada filosofi Cypherpunk, Wallet ini menggabungkan kesederhanaan, kerahasiaan, dan fitur-fitur canggih seperti pertukaran lintas jaringan dan dukungan PayJoin. Ini memungkinkan Anda untuk mengelola bitcoin Anda di tiga jaringan: **Bitcoin onchain**, **Liquid** dan **Lightning**, masing-masing disesuaikan dengan penggunaan tertentu. Di [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49), Anda dapat melihat topik terkini dan perkembangan yang akan datang. Karena proyek ini 100% open-source dan "dibangun untuk umum", Anda juga dapat mengirimkan saran dan bug yang Anda temui. Meskipun beberapa dompet sekarang mendukung beberapa jaringan, Bull Bitcoin Wallet menonjol dengan mengintegrasikan fitur privasi secara mendalam di semua jaringan, menjadikannya alat yang ampuh untuk mengelola Bitcoin Anda di semua jaringan utama


## 1️⃣ Prasyarat


Sebelum Anda mulai menggunakan **Bull Bitcoin Wallet**, pastikan Anda memiliki item berikut ini:



- Smartphone yang Kompatibel**: Perangkat **iOS** (iPhone atau iPad) atau **Android**
- Koneksi internet
- Media cadangan yang aman**: Tuliskan **frase pemulihan** (12 kata) di atas kertas atau logam dan simpan di tempat yang aman.
- Pengetahuan dasar**: Pemahaman minimum mengenai konsep Bitcoin (alamat, transaksi, biaya) sangat berguna, meskipun tutorial ini menjelaskan setiap langkah untuk pemula.


## 2️⃣ Instalasi


Anda dapat menginstal aplikasi melalui:



- [Apple App Store](https://apps.apple.com/app/bull-bitcoin/id6743380972)[ ](https://apps.apple.com/us/app/bitchat-mesh/id6748219622) (untuk perangkat iOS)
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&hl=en) (untuk perangkat Android)


Pengguna Android juga memiliki opsi alternatif:



- Unduh APK langsung dari halaman [Rilis GitHub](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) atau
- Instal melalui [Zapstore] yang kompatibel dengan Nostr (https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqtxxmmd9e382mrvvf5hgcm0d9hzumt0vf5kcegnah0ap)


Setelah menginstal aplikasi, ikuti layar selamat datang untuk mengonfigurasi akun Anda.


## 3️⃣ Konfigurasi awal


Pada saat membuka, Anda akan diminta untuk memilih opsi berikut ini:



- `Create New Wallet`
- `Pulihkan Wallet` dan
- 'Opsi Lanjutan'


Mari kita mulai dengan mengetuk `Pilihan Lanjutan`.


Di sini, kita dapat mengonfigurasi pengaturan lanjutan sebelum membuat atau memulihkan wallet:


1. Aktifkan `Tor proxy` untuk merutekan lalu lintas melalui jaringan Tor.

1. [Aplikasi Orbot](https://orbot.app/en/) perlu diinstal dan dijalankan sebelum mengaktifkan

2. Tor Proxy hanya berlaku untuk Bitcoin (bukan Liquid) dan dapat mengakibatkan koneksi yang lebih lambat.

2. Menyiapkan `Custom Electrum Server`, atau

3. Sesuaikan pengaturan `Pulihkan Banteng`. Kita akan mempelajari lebih lanjut mengenai [Recover Bull](https://recoverbull.com/) nanti.


Setelah melakukan semua penyesuaian opsional, ketuk `Selesai`. Jika Anda ingin menggunakan kembali Wallet yang sudah ada, klik `Pulihkan Wallet` dan isi 12 kata frasa pemulihan Anda.


Jika tidak, klik `Buat Wallet Baru`.


![image](assets/en/01.webp)


## 4️⃣ Layar Utama


Sebelum kita menyelam lebih dalam, mari kita lihat `Layar Utama` untuk mendapatkan orientasi:



- 'ikhtisar transaksi' dan 'menu pengaturan' terletak di bagian atas.
- `Saldo yang Tersedia` memiliki opsi privasi yang dapat `diaktifkan atau dinonaktifkan`.
- Akses `Bitcoin Bull Exchange` untuk `Beli, Jual, atau Bayar` (ini tergantung pada yurisdiksi dan mungkin memerlukan KYC).
- 'Transfer' dana antar dompet
- `Secure Bitcoin` sama dengan Onchain Bitcoin Wallet
- pembayaran instan melalui Lightning- / Liquid Network *(Catatan: Bull Bitcoin Wallet memungkinkan pembayaran dilakukan dan diterima melalui Lightning. Dana yang diterima melalui Lightning disimpan di jaringan [*Liquid](https://liquid.net/) (dalam Pembayaran Instan Wallet) berkat pertukaran otomatis melalui [*pertukaran Boltz](https://boltz.exchange/). Hal ini memberikan Anda kemampuan untuk berinteraksi dengan Lightning tanpa harus mengelola saluran likuiditas, namun tetap berada dalam penyimpanan sendiri)
- `Kirim` dan `Terima` dana


![image](assets/en/02.webp)


Pertama, mari kita buat beberapa konfigurasi penting dan mulai dengan `Backup`.


## 5️⃣ Cadangan


Untuk memulai proses pencadangan, ketuk `ikon roda gigi (⚙)` di sudut kanan atas aplikasi dan pilih `Cadangan Wallet`. Anda akan dihadapkan pada dua metode untuk mengamankan wallet Anda: `Bankur Terenkripsi` dan `Cadangan Fisik`. Mari kita jelajahi masing-masing.


![image](assets/en/03.webp)


### Cadangan Fisik


Sentuh `Cadangan Fisik` untuk melihat daftar 12 kata yang mewakili pemulihan atau frasa seed Anda. Harap pertimbangkan yang berikut ini:



- Tuliskan 'frasa pemulihan' Anda dengan sangat hati-hati. Tuliskan di atas kertas atau logam dan simpan di tempat yang aman (brankas, lokasi offline). Frasa ini merupakan satu-satunya cara untuk mengakses bitcoin Anda jika perangkat Anda hilang atau aplikasi dihapus.
- Penting juga untuk diperhatikan bahwa siapa pun yang memiliki frasa ini dapat mencuri semua bitcoin Anda. Jangan pernah menyimpannya secara digital:
- Tidak ada tangkapan layar
- Tidak ada cadangan awan, email, atau pesan
- Tidak ada salin/tempel (risiko menyimpan ke clipboard)


![image](assets/en/25.webp)


Layar berikutnya akan meminta Anda untuk meletakkan kata dalam urutan yang benar untuk memastikan bahwa Anda mendapatkan frasa seed yang benar. Anda akan mendapatkan konfirmasi ketika tes selesai dan berhasil.


! **Poin ini sangat penting**. Untuk bantuan lebih lanjut:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### Brankas terenkripsi


Ada juga opsi pencadangan terenkripsi dan anonim di awan. Tapi bukankah kami telah menyebutkan di paragraf terakhir bahwa cadangan awan berisiko dan harus dihindari? Namun, tim Bull Bitcoin telah mengembangkan cara yang cerdas untuk membuat prosesnya aman. Inilah cara kerjanya:


`Recoverbull` adalah protokol pencadangan yang menyederhanakan pengamanan Bitcoin wallet Anda dengan membagi pencadangan menjadi dua bagian. Pertama, file cadangan wallet Anda dienkripsi di perangkat Anda menggunakan kunci enkripsi yang kuat. Anda dapat menyimpan file terenkripsi ini di mana pun Anda inginkan, seperti Google Drive atau perangkat Anda. Kedua, kunci enkripsi yang diperlukan untuk membuka kunci file disimpan oleh Server Kunci Recoverbull. Untuk memulihkan wallet Anda, Anda memerlukan file cadangan terenkripsi dan kunci, yang Anda akses dengan PIN atau kata sandi Anda. Desain ini memastikan bahwa cadangan awan Anda saja tidak berguna dan server kunci saja tidak berguna tanpa file cadangan khusus Anda. Hal ini membuat dana Anda tetap aman meskipun salah satu bagiannya terganggu.


Anggap saja ini seperti brankas. File cadangan terenkripsi adalah *boks*, yang bisa Anda simpan di mana saja (seperti Google Drive). PIN Pemulihan Anda adalah *kunci*, yang disimpan secara terpisah oleh Server Kunci Recoverbull. Seorang pencuri perlu mendapatkan kotak khusus Anda dan kunci khusus Anda untuk membukanya. Desain ini memastikan bahwa meskipun seseorang mendapatkan file cadangan Anda, tidak ada gunanya tanpa kunci dari server, dan kunci server tidak berguna tanpa file cadangan unik Anda.


Pelajari lebih lanjut tentang protokol cadangan `Recoverbull` wallet [di sini](https://recoverbull.com/).


Ketuk `Bank terenkripsi` lalu `Lanjutkan` untuk mengonfirmasi penggunaan Server Default. Sambungan akan dialihkan melalui Jaringan `Tor` untuk memastikan privasi dan anonimitas.


**Memahami PIN Anda**



- pIN Buka Kunci Aplikasi`**:** PIN opsional yang ditetapkan di `Pengaturan > PIN Keamanan` untuk mengunci aplikasi pada ponsel Anda.
- pIN Pemulihan: ** PIN wajib yang dibuat selama proses pencadangan `Encrypted Vault`, yang digunakan untuk mendekripsi file cadangan selama pemulihan.


Ini adalah dua PIN yang terpisah. Jangan lupa PIN Pemulihan Anda, karena PIN ini sangat penting untuk memulihkan wallet Anda."


**Pengaturan PIN Pemulihan:**



- Anda harus membuat PIN atau Kata Sandi untuk memulihkan akses ke wallet.
- PIN / Kata Sandi harus terdiri dari minimal 6 digit (misalnya, hindari urutan sederhana seperti 123456, yang tidak diterima).
- Tanpa PIN ini, pemulihan wallet tidak mungkin dilakukan.


Selanjutnya, pilih penyedia brankas:



- `Google Drive` atau
- 'lokasi khusus' (misalnya perangkat Anda)


![image](assets/en/04.webp)


Sekarang, simpan `file cadangan`. Selanjutnya, ketuk `Test Recovery`, pilih file cadangan atau vault yang disimpan, lalu ketuk `Decrypt Vault`. Masukkan `PIN` atau `Kata Sandi` Anda. Jika semuanya berhasil, layar `Test selesai dengan sukses` akan muncul.


### Label Impor / Ekspor


Sekarang setelah kita membuat Cadangan, mari kita lihat `Label`.  Bull Bitcoin wallet meningkatkan privasi dan pengaturan dengan memungkinkan pengguna untuk membuat label khusus untuk alamat penerima dan transaksi mereka. Label-label ini membantu Anda mengkategorikan dana Anda, karena transaksi yang dikirim ke alamat berlabel akan mewarisi label tersebut, dan Anda juga dapat memberi label pada transaksi keluar untuk melacak perubahannya. wallet sepenuhnya mendukung standar [BIP-329](https://bip329.org/), yang berarti Anda dapat mengekspor semua label ke file dan mengimpornya ke wallet lainnya. Fitur ini memastikan Anda dapat mencadangkan riwayat transaksi dan kategorisasi dengan lancar, atau memigrasikannya di antara berbagai contoh wallet, tanpa kehilangan organisasi yang telah disesuaikan.


![image](assets/en/05.webp)


## 6️⃣ Pengaturan


Setelah cadangan utama Anda aman, mari jelajahi fitur-fitur lain yang tersedia dalam pengaturan.


### A - Mengamankan akses


Untuk mengamankan aplikasi, buka `Pengaturan` dan pilih `Kode PIN Keamanan` untuk memilih Kode PIN. Buat PIN yang kuat untuk mengunci akses ke wallet Anda. Meskipun langkah ini bersifat opsional, namun sangat disarankan untuk mencegah akses yang tidak sah jika ada orang lain yang menggunakan telepon Anda.


![image](assets/en/06.webp)


### B - Koneksi ke simpul pribadi (opsional)


Wallet BullBitcoin terhubung ke server Electrum secara default: server pertama dikelola oleh Bull Bitcoin dan server sekunder dari Blockstream, yang keduanya dianggap tidak menyimpan log, sehingga mengurangi risiko pelacakan.


Untuk kerahasiaan yang lebih baik, Anda dapat menyambungkan aplikasi ke node Bitcoin Anda sendiri melalui server Electrum. Untuk melakukannya, ketuk `Pengaturan` > `Pengaturan Bitcoin` > `Pengaturan Electrum Server`, lalu ketuk `+ Tambah Server Khusus` untuk memasukkan alamat dan kredensial server Anda.


![image](assets/en/07.webp)


### C - Mata Uang


Saldo yang tersedia ditampilkan di layar utama dalam `sats` dan `USD`. Untuk mengubahnya, buka `Pengaturan` > `Mata Uang`. Di sana, Anda dapat beralih antara `sats/BTC` dan memilih `mata uang fiat default`.


![image](assets/en/08.webp)


### D - Pengaturan Bitcoin


Menu `Pengaturan Bitcoin` menawarkan akses mendalam ke konfigurasi dan data inti wallet Anda. Di sini, Anda dapat memeriksa detail mendasar dari `Secure Bitcoin` dan `Dompet pembayaran instan`, memberikan Anda transparansi dan kontrol penuh. Fitur-fitur utama dalam menu ini meliputi:



- Detail Wallet:** Buka Secure Bitcoin atau Pembayaran Instan wallet Anda untuk melihat informasi spesifik.
- Sidik Jari Wallet:** Pengenal unik untuk wallet Anda.
- Kunci Publik (Pubkey):** Kunci yang digunakan untuk generate alamat penerima Bitcoin Anda.
- Descriptor:** Ringkasan teknis struktur wallet Anda.
- Jalur Turunan:** Jalur khusus yang digunakan untuk generate semua alamat dari kunci privat utama Anda.
- Address Lihat:** Mengakses daftar alamat penerima yang tidak terpakai dan mengubah alamat (segera hadir)


Selain itu, Anda memiliki opsi untuk:



- pengaturan `Aktifkan Transfer Otomatis` untuk mengatur saldo wallet instan maksimum, yang kemudian akan ditransfer secara otomatis ke bitcoin wallet yang aman.
- Impor dompet Generik melalui Frasa `Mnemonic` atau impor `hanya untuk jam tangan`
- Hubungkan `Dompet perangkat keras`: perangkat yang didukung saat ini adalah ColdcardQ, SeedSigner, Spectre, Krux, Blockstream Jade, dan Foundation Passport


## 7️⃣ Bull Bitcoin Exchange


Langsung dari wallet, Anda memiliki akses ke [Bull Bitcoin exchange](https://www.bullbitcoin.com/), sehingga Anda dapat membeli, menjual, dan membayar Bitcoin tanpa harus meninggalkan aplikasi. Integrasi ini memberikan solusi yang nyaman untuk mengelola kebutuhan Bitcoin Anda. Perlu diketahui bahwa akses ke bursa dan layanannya mungkin dibatasi berdasarkan yurisdiksi Anda, dan menyelesaikan verifikasi Kenali Pelanggan Anda (KYC) mungkin diperlukan untuk mematuhi standar peraturan dan menggunakan fitur lengkap platform.


Untuk memulai, ketuk `Exchange` di sudut kanan bawah, lalu `Daftar` atau `Masuk` ke akun Anda.


Pertukaran ini menawarkan [fitur] berikut ini (https://www.bullbitcoin.com/):



- Beli Bitcoin dengan penitipan mandiri dari rekening bank Anda
- Non-kustodian
- Individu atau perusahaan
- Penarikan instan
- Tidak ada biaya tersembunyi
- Lightning Network tersedia
- Tidak ada batasan transaksi
- Opsi beli berulang


![image](assets/en/09.webp)


Untuk mempelajari lebih lanjut, silakan kunjungi tutorial ini:


https://planb.academy/en/tutorials/exchange/centralized/bull-bitcoin-europe-0ccf713e-efcd-44ec-8205-211f49ac7d53

## 8️⃣ Menerima dana


Menerima dana dengan **Bull Bitcoin Wallet** sangat mudah dan fleksibel, mendukung tiga jaringan berbeda yang disesuaikan untuk berbagai kasus penggunaan:



- Jaringan `Bitcoin (onchain)` untuk penyimpanan jangka panjang yang aman.
- Jaringan `Liquid` untuk transaksi yang cepat dan lebih rahasia.
- Jaringan `Lightning` untuk pembayaran instan dan berbiaya rendah.


Aplikasi ini secara otomatis membuat alamat atau faktur yang sesuai berdasarkan jaringan yang Anda pilih. Berikut ini adalah cara melanjutkan untuk setiap jaringan.


### Menerima melalui Onchain (jaringan Bitcoin)


Untuk menerima dana on-chain, Anda dapat memilih `Secure Bitcoin Wallet` dari layar Utama dan ketuk `Terima`, atau ketuk tombol `Terima` utama lalu pilih `Jaringan Bitcoin`.


Anda memiliki dua mode utama untuk menghasilkan alamat penerimaan:


**Mode Default (URI dengan parameter masukan tambahan)


Secara default, wallet menghasilkan [BIP21 URI](https://bips.dev/21/). Ini adalah format standar yang mengemas lebih banyak informasi daripada alamat sederhana, termasuk jumlah, catatan pribadi, dan parameter PayJoin untuk meningkatkan privasi. URI komprehensif ini dikodekan ke dalam kode QR dan tersedia untuk disalin. Formatnya terlihat seperti ini: `bitcoin:<alamat>?<parameter1>=<nilai1>&<parameter2>=<nilai2>`.



- Parameter Masukan Tambahan:**
    - Jumlah:** Tentukan jumlah yang diminta dalam BTC, sats, atau mata uang fiat.
    - Pesan:** Tambahkan catatan pribadi yang akan terlihat oleh pengirim.
    - PayJoin:** Aktifkan opsi ini untuk meningkatkan privasi dengan menggabungkan input dari pengirim dan penerima dalam transaksi.


Contoh URI:


```
bitcoin:bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54xxxxx?amount=0.0005&message=Tip+for+tutorial&pj=HTTPS%3A%2F%2FPAYJO.IN%2F78UH9WZUP8KKJ%23RK1Q2H30FASCU9WW09DQY2LK0K8P2DPRJ99V72CA78ACQAEL675QYTMQ+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1L0LYV6G
```


*Catatan Penting: Harap jangan mengirimkan dana ke alamat yang tertera dalam tutorial ini, karena wallet akan dihapus*


![image](assets/en/10.webp)


** Opsi Salin atau pindai Address saja yang diaktifkan


Dengan opsi `Salin atau pindai Address saja` yang diaktifkan, aplikasi ini menghasilkan alamat Bitcoin sederhana dalam format SegWit (bech32).


Contoh:


```javascript
bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54x3g56
```


Meskipun Anda memasukkan jumlah atau catatan, keduanya tidak akan disertakan dalam kode QR atau alamat yang disalin.


![image](assets/en/11.webp)


### Menerima melalui Liquid Network


Anda dapat menerima pembayaran pada Liquid Network. Setelah berada di layar `Terima`, Anda memiliki dua opsi yang sama untuk membuat permintaan pembayaran:


**1. Address sederhana:** Salin `alamat Liquid standar. Ini adalah pengenal unik untuk wallet Anda di jaringan Liquid dan tidak menyertakan jumlah atau pesan tertentu.


Contoh Address:


```javascript
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7xxxxxxx
```


**2. Permintaan Pembayaran Terperinci (URI):** Untuk permintaan yang lebih terstruktur, Anda dapat menentukan jumlah dan catatan pribadi. Informasi ini secara otomatis dikodekan ke dalam URI yang dapat dibagikan dan kode QR yang sesuai.



- Jumlah:** Anda dapat mengatur jumlah dalam Bitcoin (BTC), Satoshi (Sats), atau mata uang fiat.
- Catatan:** Tambahkan pesan pribadi untuk mengidentifikasi transaksi.


**Contoh URI:**


```javascript
liquidnetwork:lq1qqdhgs7w537nun55a5sdy4gxkd08pclk3d7v4qz36sy4xp0cq6gvl52fcfv7kdgkgzmfycrud0zsygqgyjclycckpasxxxxxx?amount=0.00001&message=Test&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```


Untuk menyelesaikan transaksi, berikan pengirim `alamat` atau `URI`. Anda dapat melakukan ini dengan menyalinnya ke clipboard Anda atau dengan meminta mereka memindai kode QR langsung dari layar Anda.


![image](assets/en/12.webp)


### Menerima melalui Lightning



Bull Bitcoin Wallet juga memungkinkan Anda untuk mengirim dan menerima pembayaran melalui Lightning Network. Fitur utamanya adalah dana yang diterima melalui Lightning secara otomatis ditukar dan disimpan di `Liquid Network` dalam `Pembayaran Instan Wallet`. Layanan ini didukung oleh `Boltz`. Desain ini memungkinkan Anda untuk menikmati kecepatan dan biaya rendah Lightning tanpa kerumitan dalam mengelola saluran likuiditas, sambil tetap mempertahankan kustodian penuh atas dana Anda. Meskipun pendekatan hibrida ini bersifat kustodian mandiri dan menghindari kerumitan dalam mengelola saluran, pendekatan ini memperkenalkan layanan pihak ketiga (Boltz), biaya swap yang kecil, dan ketergantungan pada federasi fungsionaris Liquid Network sebagai pemegang kunci, yang berbeda dengan Lightning wallet non-kustodian tradisional di mana Anda mengelola saluran Anda sendiri. Anda dapat mempelajari lebih lanjut tentang Liquid dan model tata kelola di sana di sini:


https://planb.academy/en/courses/e17ee350-41d4-49fa-b270-29e4d26d22f8/overview-of-liquid-architecture-and-governance-model-17650c4b-cd1f-4bc6-b490-708f92dc9306


- Batasan:** Batas
    - Jumlah Minimum:** Diperlukan jumlah faktur minimum. Silakan periksa aplikasi untuk mengetahui batas saat ini
    - Biaya:** Anda, sebagai penerima, bertanggung jawab atas biaya penukaran yang kecil. Biaya ini dipotong dari jumlah yang ditransfer pengirim dan dapat berubah sewaktu-waktu
- Manfaat:** Manfaat
    - Kustodian Mandiri:** Dana Anda selalu berada di bawah kendali Anda, diamankan di jaringan Liquid.
    - Hindari Biaya On-Chain yang Tinggi:** Dengan menggunakan Lightning dan menyimpan di Liquid, Anda melewati biaya on-chain yang terkait dengan pembukaan saluran Lightning tradisional. Anda dapat memilih untuk memindahkan dana ke saluran on-chain nanti, ketika jumlah yang terakumulasi sesuai dengan biaya.
    - Tip:** Untuk transaksi yang paling hemat biaya antara dua pengguna Bull Bitcoin, gunakan **jaringan Liquid secara langsung** untuk menghindari biaya swap Lightning sepenuhnya.


Untuk menerima pembayaran, Anda harus generate sebuah `Faktur Kilat`:


1. `Masukkan Jumlah`:** Tentukan jumlah yang ingin Anda terima dalam Bitcoin (BTC), Satoshi (Sats), atau mata uang fiat.

2. `Tambahkan Catatan` **(Opsional):** Sertakan memo atau catatan. Catatan ini akan disematkan pada faktur dan ditampilkan dalam riwayat transaksi Anda setelah pembayaran selesai, sehingga lebih mudah diidentifikasi.

3. `Validitas Invoice`:** Faktur Lightning sensitif terhadap waktu dan akan kedaluwarsa setelah **12 jam**. Jika tidak dibayar dalam jangka waktu tersebut, faktur tersebut menjadi tidak berlaku, dan Anda harus membuat generate yang baru.


Berikan faktur kepada pengirim dengan menyalinnya ke papan klip Anda atau dengan membiarkan mereka memindai kode QR yang ditampilkan di layar Anda.


![image](assets/en/13.webp)


## 9️⃣ Mengirim dana


Anda dapat mengakses layar kirim langsung dari halaman beranda atau dari dalam dompet Anda. Bull Bitcoin Wallet menyederhanakan proses dengan secara otomatis mendeteksi jaringan tujuan-`Bitcoin`, `Liquid`, atau `Lightning`-berdasarkan alamat atau faktur yang Anda masukkan, baik yang ditempelkan atau dipindai melalui kode QR.


### Transmisi On-Chain melalui Jaringan Bitcoin


Mengirim dana on-chain berarti transaksi Anda dicatat langsung di blockchain Bitcoin. Metode ini paling baik untuk transfer dalam jumlah besar atau transfer yang tidak sensitif terhadap waktu. Untuk memulai, Anda dapat mengetuk `Tombol Kirim` di sebelah kanan bawah, dan memindai atau memasukkan `alamat standar Bitcoin`.


Jika alamat yang Anda berikan tidak mencantumkan jumlah tertentu, Anda akan diminta untuk mengisi detailnya pada layar kirim. Anda bisa menentukan jumlah dalam unit yang Anda inginkan, seperti BTC, satoshi, atau mata uang fiat yang setara. Anda juga memiliki opsi untuk menambahkan catatan pribadi, yang merupakan memo pribadi untuk referensi Anda sendiri untuk membantu Anda mengidentifikasi transaksi nanti. Catatan ini tidak akan dibagikan dengan penerima.


Sebaliknya, jika permintaan pembayaran yang Anda pindai atau tempelkan sudah berisi semua rincian yang diperlukan, seperti URI BIP21 dengan jumlah yang sudah ditentukan sebelumnya, wallet akan melewati layar entri data dan membawa Anda langsung ke layar konfirmasi untuk mengesahkan pembayaran.


![image](assets/en/14.webp)


Sebelum transaksi Anda disiarkan, Anda akan dihadapkan pada layar konfirmasi. Sangat penting untuk meluangkan waktu sejenak dan meninjau setiap parameter dengan cermat, dengan memperhatikan alamat penerima, jumlah yang dikirim, dan biaya jaringan. Layar ini juga menyediakan alat bantu yang berguna untuk menyesuaikan transaksi Anda.


Anda dapat mengontrol biaya dengan dua cara utama. Metode pertama adalah memilih kecepatan transaksi yang diinginkan, seperti rendah, sedang, atau tinggi, dan wallet akan secara otomatis menghitung biaya yang sesuai untuk Anda. Metode kedua memungkinkan kontrol yang lebih tepat dengan memungkinkan Anda menetapkan biaya tertentu, baik sebagai total absolut dalam satoshi atau sebagai tarif relatif per byte, yang kemudian memberikan estimasi waktu konfirmasi.


Untuk pengguna tingkat lanjut, wallet menawarkan beberapa pengaturan untuk menyempurnakan transaksi. `Replace-by-Fee` (RBF) diaktifkan secara default, yang merupakan fitur berharga yang memungkinkan Anda untuk mempercepat transaksi jika macet di mempool dengan menyiarkan ulang dengan biaya yang lebih tinggi. Anda juga dapat secara manual memilih `Unspent Transaction Outputs` (UTXO) yang mana yang akan dibelanjakan. Ini adalah alat yang ampuh untuk konsolidasi UTXO, sebuah strategi di mana Anda menggabungkan beberapa input kecil menjadi satu input yang lebih besar. Meskipun hal ini mungkin akan membebani biaya lebih besar untuk transaksi saat ini, namun secara signifikan dapat mengurangi biaya untuk transaksi di masa depan, terutama jika biaya jaringan diperkirakan akan meningkat.


![image](assets/en/15.webp)


PayJoin secara otomatis dicoba ketika Anda memindai permintaan pembayaran penerima (URI BIP21) yang menyertakan parameter `pj=`. Jika Anda hanya menempelkan alamat biasa tanpa parameter tambahan, fitur ini tidak akan diaktifkan. Metode kolaboratif ini meningkatkan privasi dengan menggabungkan input dari pengirim dan penerima, mematahkan heuristik kepemilikan-input yang umum dan memungkinkan penskalaan yang lebih baik serta penghematan biaya dalam beberapa situasi.


### Mengirim ke Liquid Network


Liquid Network dirancang untuk transaksi yang cepat dan rahasia dengan biaya minimal. Ketika Anda mengirim dana melalui Liquid, dana tersebut akan ditarik dari `Pembayaran Instan Wallet`. Prosesnya sangat mudah: Anda cukup memasukkan atau memindai `alamat Liquid` penerima.


Jika alamat tidak menentukan jumlah, Anda akan diminta untuk memberikannya pada layar kirim. Anda bisa memasukkan jumlah dalam BTC, satoshi, atau fiat. Keuntungan utama Liquid adalah ambang batas minimumnya yang rendah. Seperti halnya transaksi on-chain, Anda dapat menambahkan catatan pribadi opsional untuk catatan Anda sendiri. Jika permintaan pembayaran sudah termasuk jumlah, wallet akan langsung menuju ke layar konfirmasi.


Pada layar konfirmasi untuk transaksi Liquid, Anda akan meninjau detailnya. Biayanya sangat rendah dan dihitung berdasarkan kompleksitas transaksi. Biasanya sekitar 0,1 sat/vB, yang untuk transaksi sederhana hanya sebesar 20-40 satoshi (misalnya, 26 satoshi pada 21 Desember 2025).


![image](assets/en/16.webp)


### Mengirim ke Lightning Network


Anda dapat memindai Lightning Address (mis. `runningbitcoin@rizful.com`) yang memungkinkan Anda untuk mengatur jumlah dan catatan opsional untuk penerima, atau memindai faktur dengan jumlah yang telah ditentukan sebelumnya, yang akan membawa Anda langsung ke layar konfirmasi.


*Harap diperhatikan bahwa jumlah minimum dan biaya berlaku.*


Bull Bitcoin Wallet mengirimkan pembayaran Lightning dengan menarik dana dari `Pembayaran Instan Wallet` (pada Liquid) dan menukarnya melalui `Boltz`. Pendekatan hibrida ini sepenuhnya bersifat kustodian mandiri dan menghindari biaya on-chain yang tinggi untuk mengelola saluran Lightning khusus, tetapi memerlukan pembayaran `biaya pertukaran`. Untuk biaya terendah, kirim langsung ke alamat Liquid penerima jika mereka juga menggunakan Bull Bitcoin wallet.


## 🔟 Mentransfer Dana Antar Dompet Anda


Bull Bitcoin memungkinkan Anda untuk memindahkan Bitcoin Anda antara `Bitcoin Aman` wallet dan `Pembayaran Instan Wallet` pada Liquid Network atau ke `Wallet eksternal`. Untuk melakukan transfer, cukup buka bagian `Transfer`, pilih dompet sumber dan tujuan, masukkan jumlah yang ingin Anda pindahkan, dan konfirmasikan transaksi.


![image](assets/en/17.webp)


## 1️⃣1️⃣ Memulihkan Bull Bitcoin Wallet Anda


Bagian ini menjelaskan cara mendapatkan kembali akses ke dana Bull Bitcoin Wallet Anda jika Anda kehilangan perangkat, menghapus aplikasi, atau hanya perlu beralih ke yang baru. Seperti yang telah dijelaskan, ada dua metode utama untuk pemulihan: menggunakan metode `Recoverbull` yang unik dan menggunakan frasa standar `BIP39 seed`.


### Metode 1: Recoverbull


Rekap: Cadangan Wallet dienkripsi secara lokal. File yang dienkripsi dapat disimpan di penyimpanan cloud, atau di perangkat lain. Kunci enkripsi disimpan oleh Server Kunci Recoverbull. Keduanya disimpan terpisah dan harus digabungkan untuk memulihkan wallet.


Untuk memulai, saya akan menghapus Wallet dengan semua dana di dalamnya dan menginstal ulang wallet. Kita akan mendarat di `Layar Selamat Datang` lagi. Kali ini, pilih opsi `Pulihkan Wallet`. Kemudian, navigasikan ke metode `Vault Terenkripsi`, konfirmasikan menggunakan `Server Kunci Default`, dan pilih lokasi atau `Penyedia Vault` di mana Anda menyimpan file cadangan.


![image](assets/en/18.webp)


Ini menyatakan bahwa vault berhasil diimpor. Tekan tombol `Dekripsi Brankas` dan masukkan `PIN`. Layar berikutnya akan menampilkan `saldo` dan `jumlah transaksi` Anda yang telah dipulihkan.


![image](assets/en/19.webp)


### Metode 2: Frasa Benih


Metode ini menggunakan frasa pemulihan utama wallet Anda, daftar 12 kata standar yang berfungsi sebagai cadangan utama untuk dana Anda. Ini adalah cara yang paling universal untuk memulihkan Bitcoin wallet, karena tidak terikat pada layanan atau server tertentu. Selama Anda memiliki frasa ini, Anda dapat memulihkan wallet Anda pada perangkat apa pun yang kompatibel, bahkan tanpa akses ke Server Kunci Bull Bitcoin.


Dari layar Selamat Datang, pilih `Pulihkan Wallet`. Kali ini, pilih metode `Physical backup`. Aplikasi akan menampilkan kisi-kisi kata. Pilih dengan hati-hati setiap kata dari frasa seed yang terdiri dari 12 kata dalam urutan yang benar. Teliti, karena satu kesalahan saja akan menghasilkan wallet yang salah.


## 1️⃣2️⃣ Menghubungkan Hardware Wallet


Untuk tingkat keamanan tertinggi, banyak pengguna Bitcoin memilih untuk menyimpan dana mereka dalam `penyimpanan dingin`. Ini berarti menyimpan `kunci pribadi` yang mengontrol Bitcoin Anda pada perangkat yang tidak pernah terhubung ke internet. Sebuah `perangkat keras wallet` (atau perangkat Penandatanganan) adalah perangkat fisik khusus yang dirancang untuk tujuan ini. Perangkat ini berfungsi seperti brankas digital untuk kunci Anda, memastikan kunci tersebut tidak pernah terpapar pada potensi ancaman dari komputer atau ponsel pintar online.


Dengan menghubungkan perangkat keras wallet ke aplikasi Bull Bitcoin, Anda mendapatkan yang terbaik dari kedua dunia: keamanan tanpa kompromi dari cold storage untuk private key Anda, dikombinasikan dengan fitur-fitur yang kuat dan antarmuka yang mudah digunakan dari Bull Bitcoin wallet untuk melihat saldo dan mengelola transaksi. Pada bab terakhir ini, kami akan menunjukkan kepada Anda cara menghubungkan perangkat keras wallet, seperti [Coldcard Q](https://coldcard.com/q), ke Bull Bitcoin wallet Anda. Tutorial ini tidak akan membahas pengaturan Coldcard Q secara mendalam; Anda dapat mempelajarinya di sini:


https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

### Mengimpor Wallet


![image](assets/en/26.webp)


Pertama, dari menu utama pada Coldcard Q Anda, pilih `Export Wallet`, lalu pilih `Bull Wallet`. Coldcard Anda akan menghasilkan kode QR generate.


![image](assets/en/20.webp)


Buka Bull Bitcoin Wallet dan navigasikan ke `Pengaturan` > `Pengaturan Bitcoin` > `Import wallet` dan pilih `Coldcard Q` pada ponsel Anda dan ketuk `Buka kamera` untuk memindai kode QR untuk mengimpor kunci publik perangkat keras wallet.


![image](assets/en/21.webp)


### Menerima dengan Coldcard Q


Untuk menerima Bitcoin menggunakan Coldcard Q yang terhubung, Anda tidak perlu menghubungkan perangkat secara fisik ke ponsel Anda. Bull Bitcoin Wallet telah mengimpor kunci publik yang diperlukan, sehingga dapat mengalamatkan generate dengan sendirinya.


1. Ketuk perangkat penandatanganan Coldcard Q yang diimpor dan pilih `Terima`.

2. Aplikasi akan secara otomatis menampilkan alamat Bitcoin yang baru dari wallet Coldcard Anda.

3. Gunakan alamat ini untuk menerima dana. Bitcoin akan diamankan secara langsung ke kunci perangkat keras wallet, meskipun perangkat sedang offline selama proses berlangsung.


![image](assets/en/22.webp)


### Mengirim dengan Coldcard Q


Mengirim Bitcoin dengan Coldcard Q Anda memerlukan konfirmasi fisik untuk mengesahkan transaksi apa pun. Meskipun aplikasi Bull Wallet digunakan untuk membuat transaksi, tanda tangan akhir hanya dapat dibuat pada perangkat keras wallet itu sendiri.


Untuk memulai, buka `Coldcard Q` wallet Anda dan ketuk `Kirim`. Kemudian, `buka kamera` untuk memindai kode QR alamat penerima. Setelah memindai, masukkan `jumlah` yang ingin Anda kirimkan dan sesuaikan `prioritas biaya` sesuai kebutuhan.


Untuk opsi lainnya, Anda dapat melihat di bawah Pengaturan Lanjutan. Di sini Anda akan menemukan opsi `Ganti dengan Biaya` (RBF), yang diaktifkan secara default dan memungkinkan Anda untuk mempercepat transaksi yang macet nanti. Anda juga memiliki opsi `Coin Control`, yang memungkinkan Anda memilih secara manual UTXO tertentu yang ingin Anda belanjakan.


Setelah Anda meninjau semua detail, ketuk `Tampilkan PSBT` untuk menyiapkan transaksi.


![image](assets/en/23.webp)


Tekan tombol `Pindai` pada Coldcard Q Anda dan gunakan kameranya untuk memindai kode QR yang ditampilkan pada ponsel Anda. Layar Coldcard kemudian akan menampilkan semua detail transaksi. Verifikasi jumlah, alamat penerima, dan alamat perubahan Anda dengan cermat. Jika semuanya sudah benar, tekan tombol `Enter` pada Coldcard Q untuk menandatangani transaksi. Selanjutnya, kode QR dari transaksi yang telah ditandatangani akan muncul di layar.


![image](assets/en/24.webp)


Pada Bull wallet, ketuk `Selesai`, lalu ketuk tombol `Kamera` untuk memindai kode QR dari `transaksi yang ditandatangani` dari Coldcard Q. Bull Wallet sekarang akan menampilkan layar ringkasan transaksi yang ditandatangani. Tinjau untuk terakhir kalinya, lalu ketuk `Siarkan` Transaksi. Ini akan menyelesaikan proses dengan mengirimkan transaksi ke jaringan Bitcoin, dan dana Anda akan segera dikirim.


## 🎯 Kesimpulan


Sekarang Anda telah menyelesaikan perjalanan Anda melalui Bull Bitcoin Wallet. Aplikasi ini menempatkan alat privasi dan keamanan yang kuat tepat di ujung jari Anda, membuat fitur-fitur canggih mudah digunakan. Aplikasi ini membantu Anda tetap privat dengan fitur-fitur seperti `PayJoin`, yang menyembunyikan transaksi Anda di blockchain, dan `Integrasi Tor`, yang menyembunyikan aktivitas jaringan Anda dari pengintai. Bagi mereka yang menginginkan kontrol penuh, Anda dapat terhubung ke `node Bitcoin pribadi Anda` untuk berhenti bergantung pada server pihak ketiga, dan menggunakan `Hardware wallet` untuk menjaga agar kunci pribadi Anda benar-benar offline dan aman. Dengan opsi pencadangan cerdas dan dukungan tanpa batas untuk Bitcoin, Liquid, dan Lightning, Bull Bitcoin Wallet adalah pilihan yang kuat dan lengkap bagi siapa saja yang serius untuk menjaga dana mereka tetap privat, aman, dan sepenuhnya berada di bawah kendali mereka sendiri.


## 📚 Sumber Daya Bull Wallet


[Github](https://github.com/SatoshiPortal/bullbitcoin-mobile) | [Situs web](https://www.bullbitcoin.com/) | [Recoverbull](https://recoverbull.com/)