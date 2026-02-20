---
name: Cashu.me
description: Panduan Cashu.me untuk menggunakan ecash
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=LIPw1c74LBU)


*Berikut ini adalah video tutorial dari BTC Sessions, sebuah panduan video yang memandu Anda tentang cara mengatur dan menggunakan Cashu.me Bitcoin Wallet, yang memberikan Anda akses ke transaksi Bitcoin yang sederhana, murah, dan privat - tanpa memerlukan toko aplikasi!


Dalam tutorial ini kita akan menjelajahi Cashu.me, sebuah Wallet berbasis browser untuk pembayaran Bitcoin pribadi menggunakan ecash Chaumian. Sebelum kita membahasnya, mari kita lihat pengenalan singkat tentang ecash dan cara kerjanya.


## Pengantar tentang ecash


Bayangkan memiliki uang tunai digital yang berfungsi persis seperti uang kertas di saku Anda - privat, instan, dan dapat digunakan secara peer-to-peer tanpa perantara. Itulah yang dimungkinkan oleh ecash: sebuah pendekatan pembayaran digital yang mengembalikan privasi uang fisik ke dunia digital. Tidak seperti onchain-Bitcoin, yang mencatat setiap transaksi pada Ledger publik yang dapat dilihat oleh siapa saja, ecash menciptakan token pribadi yang mewakili nilai Bitcoin yang sebenarnya sambil menjaga kerahasiaan kebiasaan belanja Anda.


Bayangkan ecash sebagai instrumen pembawa digital yang disimpan di perangkat Anda - jika Anda memegangnya, Anda memilikinya, seperti halnya uang tunai. Token ini diterbitkan oleh layanan tepercaya yang disebut `Mints` yang menyimpan cadangan Bitcoin yang mendasarinya. Ketika Anda menggunakan ecash, Anda tidak menyiarkan transaksi Anda ke seluruh jaringan. Sebaliknya, Anda menukarkan token pribadi secara langsung dengan orang lain, menciptakan pengalaman pembayaran yang lebih terasa seperti memberikan uang tunai kepada seseorang daripada melakukan pembayaran digital tradisional.


Cashu adalah protokol ecash Chaumian yang gratis dan bersumber terbuka yang dibuat untuk Bitcoin. Teknologi ini dibangun berdasarkan penelitian kriptografi perintis David Chaum pada tahun 1980-an, menggunakan `tanda tangan buta` untuk memastikan privasi. Ketika Anda menerima token ecash, mint akan menandatanganinya tanpa mengetahui ke mana token tersebut akan dibelanjakan - sebuah fitur penting yang mencegah pelacakan transaksi. Yang terpenting, ecash tidak menggantikan Bitcoin; ecash melengkapinya dengan mengatasi beberapa masalah kritis yang muncul dari persyaratan arsitektur Bitcoin. Ecash memberikan privasi yang ditawarkan oleh uang tunai fisik (yang tidak dimiliki oleh Ledger yang transparan) dan memungkinkan transaksi mikro instan tanpa biaya Blockchain atau penundaan konfirmasi.


Ecash terintegrasi secara mulus dengan Lightning Network. Anda menggunakan Lightning untuk menyetor Bitcoin ke dalam mint (mengubah nilai Bitcoin Anda menjadi token ecash) dan untuk menariknya nanti (mengubah token kembali menjadi saldo Lightning yang dapat dibelanjakan). Bersama-sama, keduanya membentuk kombinasi yang kuat: Bitcoin menyediakan penyelesaian yang aman Layer, Lightning memungkinkan transaksi yang cepat dan interoperabilitas jaringan, dan ecash menambahkan privasi Layer yang membuat pembayaran digital terasa lebih privat.


## Cashu.me


Cashu.me adalah sebuah `Progressive Web App (PWA) yang mengimplementasikan protokol Cashu - sebuah implementasi spesifik dari Chaumian ecash yang dirancang untuk Bitcoin. Sebagai sebuah PWA, aplikasi ini bekerja secara langsung di browser Anda tanpa memerlukan instalasi dari toko aplikasi, meskipun Anda dapat `menginstal` aplikasi ini ke perangkat Anda untuk akses yang lebih mudah. Pendekatan berbasis web ini memastikan kompatibilitas yang luas di seluruh sistem operasi dengan tetap menjaga keamanan melalui protokol kriptografi dan bukan pembatasan platform.


## 🎉 Fitur Utama


Mari selami fitur-fiturnya dan jelajahi apa yang ditawarkan Cashu.me:



- Ecash Chaumian di Lightning**: Menggunakan tanda tangan buta sehingga mint tidak dapat melacak saldo pengguna atau riwayat transaksi
- Penyimpanan token secara mandiri**: Anda mengontrol token ecash secara lokal dengan frasa seed Anda
- Cadangan frasa seed**: frasa pemulihan 12 kata untuk pemulihan Wallet
- Kemandirian mint**: Dapat digunakan dengan beberapa mint independen-Anda tidak terkunci pada satu penyedia saja
- Transaksi instan dan gratis**: Dalam mint yang sama, pembayaran diselesaikan dalam hitungan detik tanpa biaya
- Arsitektur yang menjaga privasi**: Mint tidak dapat melihat siapa yang bertransaksi dengan siapa
- Pembayaran non-tunai secara offline**: Mengirim/menerima token melalui protokol transmisi lokal, seperti NFC, kode QR, Bluetooth, dll. tanpa koneksi internet
- Temukan mint ecash melalui Nostr**: Temukan dan verifikasi mint tepercaya melalui protokol Nostr
- Tukar uang elektronik antar mint**: Semua uang logam menggunakan Lightning yang berarti Anda bisa mentransfer nilai di antara keduanya.
- Kendalikan Wallet Anda dari jarak jauh dengan Nostr Wallet Connect (NWC)**: Hubungkan ke aplikasi lain seperti Nostr Client dan mulai melakukan zapping melalui NWC


Pengorbanan yang sangat penting adalah `kepercayaan`: meskipun Anda mengontrol token itu sendiri, Anda harus mempercayai mint untuk menyimpan cadangan Bitcoin yang mendasarinya. Seperti yang dinyatakan dalam dokumentasi Cashu:


> ... Mint menjalankan infrastruktur Lightning dan menyimpan satoshi untuk para pengguna ecash mint. Pengguna harus mempercayai mint untuk melakukan Redeem pada ecash mereka ketika mereka ingin menukarkannya ke Lightning.

- Dokumentasi Cashu, [Pertanyaan Umum tentang Keamanan dan Privasi](https://docs.cashu.space/faq#general-safety-and-privacy-questions)


Hal ini menjadikan ecash sebagai solusi kustodian untuk Bitcoin itu sendiri, meskipun Anda tetap memegang kendali penuh atas token.


## 1️⃣ Pengaturan Awal


① Mulailah dengan mengunjungi [Wallet.cashu.me](https://Wallet.cashu.me) di browser Anda. Karena Cashu.me adalah `PWA`, Anda tidak perlu mengunduhnya dari toko aplikasi, cukup buka situsnya secara langsung di browser Anda. Untuk akses yang lebih mudah, Anda dapat menginstalnya secara opsional ke layar beranda perangkat Anda.


② Untuk memasang PWA, ketuk tombol menu ⋮ pada browser Anda dan pilih `Tambahkan ke Layar Utama`. Setelah terinstal, tutup tab browser dan luncurkan Cashu.me dari layar beranda perangkat Anda. Pada layar pembuka, ketuk `Next` untuk melanjutkan.


③ Keamanan sangat penting. Simpan frasa seed Anda dengan aman di pengelola kata sandi atau, lebih baik lagi, tulis di atas kertas. Frasa pemulihan yang terdiri dari 12 kata ini adalah satu-satunya cara untuk memulihkan dana jika Anda kehilangan akses ke perangkat ini. Ketuk ikon 👁️ untuk menampilkan frasa seed Anda, tuliskan 12 kata secara berurutan, lalu centang kotak yang bertuliskan `Saya telah menuliskannya`. Ketuk `Selanjutnya` untuk melanjutkan, dan centang kotak untuk mengonfirmasi bahwa Anda menerima `syarat` pada layar berikut.


![image](assets/en/01.webp)


Setelah menyelesaikan penyiapan, Anda harus terhubung ke `Mint`. Ketuk `TAMBAH MINT` diikuti dengan `TEMUKAN MINT` untuk melihat mint yang direkomendasikan oleh komunitas Nostr. Untuk verifikasi tambahan, Anda dapat meninjau peringkat mint di [bitcoinmints.com](bitcoinmints.com).


Selanjutnya ketuk `Klik untuk menelusuri permen` untuk melihat daftar lengkapnya. Pilih permen dengan menyalin URL-nya, tempelkan ke dalam bidang URL, dan beri nama yang mudah dikenali. Untuk contoh ini, kita akan menggunakan:


URL: `https://mint.minibits.cash/Bitcoin`

Nama: `Minibits`


![image](assets/en/02.webp)


Ketuk `TAMBAH MINT` untuk menyelesaikan proses. Pada layar konfirmasi, verifikasi bahwa Anda mempercayai operator mint ini, lalu ketuk `TAMBAH MINT` lagi. Mint Minibits sekarang akan muncul di Layar Utama Anda. Setelah Wallet Anda siap, Anda harus mendanainya sebelum melakukan transaksi.


![image](assets/en/03.webp)


## 2️⃣ Mendanai Wallet Anda


Cashu.me menawarkan dua metode berbeda untuk mendanai Wallet Anda. Ketika Anda mengetuk `Terima` di Layar Utama, Anda akan melihat opsi untuk menerima dana melalui `TUNAI` atau melalui `KILAT.` Mari jelajahi kedua opsi tersebut.


![image](assets/en/04.webp)


### Pendanaan melalui LIGHTNING


Opsi pertama adalah mendanai Wallet melalui Lightning Invoice. pilih mint jika Anda telah menambahkan mint yang berbeda dan tentukan `jumlah (Sats)` yang ingin Anda terima. Kemudian ketuk `BUAT Invoice.` Sekarang Anda akan mendapatkan QR-Code yang dapat Anda pindai dengan Lightning Wallet atau Anda dapat dengan mudah `Salin` Invoice dan tempelkan ke Wallet lainnya untuk membayar dan mendanai cashu.me Wallet Anda.


![image](assets/en/05.webp)


### Menerima uang tunai


Metode ecash memungkinkan Anda menerima token secara langsung dari ecash Wallet lain. Mulailah dengan mengetuk tombol `Terima`, dan pilih opsi `ECASH`. Anda bisa `Paste` atau `Scan` atau menggunakan `NFC` untuk mengirimkan Cashu token dari Wallet lain. Jika Anda memilih untuk menempelkan, masukkan string token yang telah Anda salin dari Wallet lain, maka `Jumlah` dan `Mint` akan secara otomatis ditampilkan. Tekan `TERIMA` untuk menyelesaikan transaksi, dan Sats akan muncul di Wallet Anda. Perhatikan bahwa saldo Anda sekarang terdistribusi ke beberapa mint. Sebagai contoh, Anda mungkin memiliki 1.000 Sats di `Mint` Minibits dan 1.000 Sats tambahan di `Mint` Coinos. Pemisahan di berbagai mint ini merupakan aspek penting dari arsitektur Cashu.


![image](assets/en/06.webp)


### Bertukar Antar Mint


Jika Anda tidak lagi mempercayai mint tertentu yang telah Anda tambahkan, cashu.me menawarkan fitur untuk `Swap` dana dari satu mint ke mint lainnya. Buka tab mint dan gulir ke bawah hingga Anda melihat `Multimint Swaps`. Pilih mint `DARI` dan `KEPADA` dari menu tarik-turun dan masukkan jumlah yang ingin Anda transfer. Tekan `SWAP` untuk memindahkan token di antara beberapa mint. Ini akan dieksekusi melalui transaksi Lightning, jadi Anda harus menyisakan ruang untuk potensi biaya Lightning. Dalam contoh saya, 1 sat sudah cukup.


![image](assets/en/07.webp)


## 3️⃣ Mengirim dana


Untuk mengirim Sats, Cashu.me menyediakan dua opsi. Untuk mengirim melalui `tunai` atau melalui `kilat`. Mari kita lihat kedua opsi tersebut.


### Mengirim melalui Lightning


Untuk mengirim melalui Lightning, ikuti langkah-langkah berikut:


1. Ketuk `KIRIM` pada Layar Utama dan pilih `Petir`

2. Aplikasi akan meminta Anda untuk memasukkan `Lightning Invoice` atau `-Address`. Anda dapat menempelkan Invoice/Address secara langsung, atau menggunakan opsi pindai kode QR untuk menangkapnya secara visual, lalu mengonfirmasi dengan `ENTER`

3. Pilih Mint dari mana Anda ingin membayar menggunakan kolom Dropdown dan ketuk `PAY` untuk mengonfirmasi. **Catatan**: ada juga pilihan untuk menggunakan `Multinut` di bawah `Pengaturan` -> `Pengujian` yang memungkinkan Anda untuk membayar faktur dari beberapa mint sekaligus.

4. Setelah berhasil, Anda akan melihat konfirmasi pembayaran dan jumlah yang dipotong dari saldo Anda.


![image](assets/en/08.webp)


### Mengirim melalui ecash


Mengirim uang elektronik juga sangat mudah.


1. Ketuk `KIRIM` dan kali ini pilih opsi `TUNAI`.

2. `Pilih mint` dan masukkan `Jumlah` yang ingin Anda kirimkan di Sats dan ketuk `KIRIM` untuk mengonfirmasi

3. Hal ini akan menciptakan `Kode QR Animasi` yang dapat Anda sesuaikan dengan menyesuaikan parameter Kecepatan dan Ukuran. Siapa pun dapat memindai Kode QR ini ke Redeem atau Sats dengan segera, atau Anda dapat mengetuk COPY untuk mengirim string token ke orang lain melalui saluran alternatif seperti Bluetooth, NFC, atau pesan standar.

4. Saya membuka Wallet yang lain. Rekatkan dari clipboard dan pilih `Receive ecash` di Wallet lainnya.


![image](assets/en/09.webp)


## 4️⃣ Fitur Tambahan


Di luar fungsionalitas pengiriman dan penerimaan inti, Cashu.me menawarkan fitur-fitur tambahan yang kuat yang meningkatkan pengalaman Bitcoin Anda dalam ekosistem Nostr.


### Nostr Wallet Connect


Nostr Wallet Connect (`NWC`) mengubah cara Anda berinteraksi dengan aplikasi Nostr dengan menciptakan koneksi tanpa batas antara Wallet dan aplikasi sosial. Protokol ini memungkinkan aplikasi seperti [Damus](https://damus.io/) atau [Primal](https://primal.net/home) untuk meminta pembayaran secara langsung melalui relay Nostr tanpa mengharuskan Anda meninggalkan aplikasi.


Untuk mengatur `NWC` di Cashu.me:


1. Buka `Pengaturan` di menu Hamburger kiri atas

2. Gulir ke Bagian `NOSTR Wallet CONNECT` dan ketuk Tombol `Enable`

3. Anda kemudian akan menetapkan tunjangan untuk menetapkan jumlah maksimum yang dapat dibelanjakan oleh aplikasi dari Wallet Anda.

4. Setelah dikonfigurasi, Anda dapat menyalin string koneksi dan menempelkannya ke klien Nostr apa pun yang mendukung `NWC`, sehingga memungkinkan fungsionalitas zapping dan tipping secara instan.


![image](assets/en/10.webp)


### Lightning Address via npub.cash


Cashu.me terintegrasi dengan [npub.cash](https://npub.cash/) untuk menyediakan Anda dengan Lightning Address yang bekerja secara mulus dengan protokol Nostr. Di sini Anda dapat mendaftar dan mengklaim nama pengguna Anda dengan memberikan `nsec` Nostr Anda, yang berharga 5.000 Sats dan mendukung proyek npub.cash, atau Anda dapat menggunakan kunci publik Nostr apa pun (`npub`) tanpa registrasi.


Pertama, masuk ke `Pengaturan` dan ketuk `Aktifkan` Lightning Address dengan npub.cash. Ini akan membuat generate npub.cash Address menggunakan string `npub` yang berasal dari frasa Wallet seed Anda secara default.


Atau, kunjungi [halaman web ini](https://npub.cash/username) untuk mengklaim nama pengguna khusus menggunakan Nostr `nsec` Anda sendiri, yang memberi Anda Lightning Address yang dipersonalisasi seperti username@npub.cash.


![image](assets/en/11.webp)


## 🎯 Kesimpulan


Cashu.me memberikan pembayaran Bitcoin pribadi yang berfungsi seperti uang tunai fisik - secara instan dan peer-to-peer tanpa mengekspos riwayat transaksi Anda. Saya pribadi menghargai arsitektur PWA-nya karena beroperasi bebas dari batasan toko aplikasi. Dengan menggabungkan keamanan Bitcoin, kecepatan Lightning, dan privasi ecash, Wallet menawarkan kasus penggunaan yang dapat meningkatkan adopsi Bitcoin sehari-hari.


Meskipun Anda memiliki kontrol penuh atas token ecash Anda melalui penyimpanan mandiri, ingatlah bahwa mint bertindak sebagai pihak ketiga tepercaya yang memegang cadangan Bitcoin yang mendasarinya. Kemampuan untuk menggunakan beberapa mint dan menukar di antaranya memberikan fleksibilitas sekaligus menjaga privasi.


Berkat fitur-fitur seperti alamat NWC dan npub.cash, Cashu.me merupakan opsi Wallet yang menarik bagi para klien sosial yang menghargai privasi dan kedaulatan atas pembatasan kebijakan teknologi besar.


## 📚 Sumber Daya


[https://github.com/cashubtc/cashu.me](https://github.com/cashubtc/cashu.me)


[https://github.com/cashubtc](https://github.com/cashubtc)


[https://github.com/cashubtc/awesome-cashu](https://github.com/cashubtc/awesome-cashu)


[https://cashu.space/](https://cashu.space/)