---
name: Minibits Wallet
description: Panduan untuk Minibits Wallet
---

![cover](assets/cover.webp)


Dalam tutorial ini, aku akan memandu kamu menyiapkan Minibits Wallet untuk menggunakan ecash. Teknologi pembayaran yang berfokus pada privasi kuat ini bekerja bersama Bitcoin. Minibits adalah ecash dan Lightning Wallet yang memungkinkan transfer nilai secara instan, murah, dan privat, sehingga sangat ideal untuk transaksi sehari-hari yang mengutamakan privasi.

Sebelum kita membahas Minibits, mari kita pahami dengan jelas apa itu ecash dan apa yang bukan. Banyak orang sering mencampurkan ecash dengan teknologi Bitcoin atau Blockchain, padahal keduanya pada dasarnya adalah konsep yang berbeda.

Ecash BUKAN Bitcoin. Ecash tidak menggantikan Wallet Bitcoin kustodian mandiri milikmu, tetapi melengkapinya. Ecash BUKAN Blockchain dan TIDAK hidup di Ledger publik mana pun. Menariknya, ecash BUKAN teknologi baru, ecash sebenarnya sudah ada sebelum web mendunia, dengan konsep yang dikembangkan pada tahun 1980-an dan 1990-an.

Apa itu ecash: sangat privat (transaksi tidak meninggalkan riwayat yang dapat dilacak), peer-to-peer (transfer langsung tanpa perantara), dan berfungsi sebagai instrumen pembawa digital (jika kamu memilikinya, kamu yang mengendalikannya). Keuntungan utamanya adalah ecash DAPAT digunakan secara offline, baik pengirim maupun penerima dapat terputus dari internet selama transaksi berlangsung. Ecash DAPAT diterbitkan oleh satu pihak atau oleh federasi entitas tepercaya, dan merupakan teknologi pelengkap yang sempurna untuk Bitcoin, menangani transaksi kecil yang sering terjadi sementara Bitcoin berfungsi sebagai layer penyelesaian.

Harap diperhatikan bahwa pengaturan Minibits ini merupakan `solusi kustodian`, yang berarti kamu mempercayai operator Mint untuk mengelola dana kamu. Hal ini menimbulkan risiko spesifik yang harus kamu pahami sebelum melanjutkan.

Proyek menampilkan disclaimer penting ini:

- Wallet ini hanya boleh digunakan untuk tujuan penelitian.
- Wallet ini adalah versi beta dengan fungsionalitas yang belum lengkap serta bug yang diketahui maupun yang belum diketahui.
- Jangan menggunakannya dengan uang tunai dalam jumlah besar.
- Uang elektronik yang disimpan di Wallet diterbitkan oleh mint.
- Kamu mempercayai mint untuk mendukungnya dengan Bitcoin sampai kamu mentransfer kepemilikanmu ke Lightning Wallet Bitcoin.
- Protokol Cashu yang diimplementasikan oleh Wallet belum mendapatkan tinjauan atau pengujian yang ekstensif.

Perlakukan Minibits seperti Wallet sehari-hari, bukan rekening tabungan, dan jangan pernah menyimpan nilai yang signifikan di sini.



## 1️⃣ Menyiapkan Wallet Anda


Untuk memulai, kunjungi [Situs Web Minibits](https://www.minibits.cash/) di mana kamu akan menemukan opsi pengunduhan untuk semua platform utama. Pengguna iOS dapat mengunduh dari [App Store](https://testflight.apple.com/join/defJQgTD), sementara pengguna iOS Uni Eropa memiliki opsi tambahan untuk menginstal dari [Freedom Store](https://freedomstore.io/). Pengguna Android bisa mendapatkan aplikasi ini dari [Google Play Store](https://play.google.com/store/apps/details?id=com.minibits_wallet) atau mengunduh file APK langsung dari halaman [GitHub Releases](https://github.com/minibits-cash/minibits_wallet/releases).


Saat menginstal Minibits, kamu akan melihat layar pengantar yang menjelaskan konsep dasarnya. Kamu bisa membaca semuanya atau melewatinya jika sudah terbiasa dengan teknologinya. Setelah menyelesaikan langkah-langkah awal ini, kamu akan diminta untuk memilih:

- `Mengerti, bawa saya ke Wallet` untuk pengguna baru, atau
- `Pulihkan Wallet yang hilang` jika kamu memulihkan dari cadangan.



![image](assets/en/01.webp)

Setelah menyelesaikan penyiapan awal, kamu akan masuk ke Layar Utama, yang memiliki beberapa elemen penting yang perlu diperhatikan. ① Ikon profil di sudut atas akan membawamu ke halaman profil, tempat kamu bisa mengakses Minibits Wallet Address dan memilih opsi `batch receive`. ② Di tengah layar, kamu akan melihat mint yang dapat kamu gunakan, dengan mint Minibits dipilih secara default. ③ Baris tindakan di bawahnya menyediakan opsi untuk mengirim pembayaran tunai atau Lightning, memindai kode QR, dan menerima pembayaran. ④ Terakhir, bilah navigasi bagian bawah berisi pintasan ke layar Beranda, Riwayat Transaksi, Kontak, dan Pengaturan.


![image](assets/en/02.webp)


## 2️⃣ Mengelola permen


Secara default, mint Minibits diaktifkan saat kamu pertama kali membuka aplikasi. Namun, salah satu kekuatan ecash adalah kemampuannya menggunakan beberapa mint untuk meningkatkan desentralisasi dan keamanan. Untuk menambahkan mint lain, buka `Pengaturan`, lalu pilih `Kelola mint`, dan terakhir ketuk `Tambahkan mint`.


(Bitcoinmints.com) menyediakan daftar lengkap mint yang tersedia beserta peringkat pengguna untuk membantu kamu memilih opsi yang memiliki reputasi baik. Menggunakan beberapa mint dapat mengurangi risiko. Jika satu mint mengalami masalah, dana kamu di mint lain tetap bisa diakses.


![image](assets/en/04.webp)


## 3️⃣ Membuat Cadangan


Pencadangan bisa dibilang merupakan langkah yang paling penting dalam keseluruhan proses penyiapan. Untuk mengakses opsi Pencadangan, navigasikan ke `Pengaturan`-> `Pencadangan` Di sini Anda akan menemukan dua opsi penting:

1. 'Seedphrase kamu' yang berisi '12 kata' memungkinkan kamu memulihkan saldo ecash jika perangkat hilang. Seedphrase ini adalah kunci utama untuk semua ecash di semua koin yang sudah kamu tambahkan. Tuliskan di media fisik (kertas atau logam) dan simpan dengan aman di beberapa lokasi. Jangan pernah menyimpan seedphrase kamu secara digital di tempat yang bisa membahayakan.
 Pertimbangkan untuk mengunjungi [tutorial](https://planb.academy/en/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270) ini untuk mengetahui praktik terbaik dalam melindungi Wallet kamu.

2. `Backup Wallet` yang berisi string backup yang panjang.


**Perhatian**: Kamu tetap memerlukan seedphrase saat menggunakan cadangan ini untuk memulihkan Wallet kamu.


![image](assets/en/05.webp)


## 4️⃣ Buat Minibits Wallet Address


Selanjutnya arahkan ke `Kontak` di bagian bawah dan sesuaikan `Minibits Wallet Address` khusus kamu dengan mengetuk `Ubah` -> `Ubah Wallet Address`. Masukkan Address yang kamu inginkan dan periksa ketersediaannya.


![image](assets/en/07.webp)


Setelah mengatur Address, kamu akan diminta memberikan sedikit `Donasi` untuk mendukung proyek ini. Meskipun opsional, aku sangat menyarankan untuk mempertimbangkannya jika kamu berencana menggunakan layanan ini secara teratur. Proyek open source seperti Minibits mengandalkan dukungan komunitas untuk melanjutkan pengembangan dan pemeliharaan. Bahkan kontribusi kecil pun bisa membantu memastikan keberlangsungan proyek ini.


![image](assets/en/08.webp)


## 5️⃣ Pengaturan Nostr


Jika kamu ingin memberi tip kepada orang yang kamu ikuti di Nostr, kamu bisa `Tambahkan kunci npub kamu` dengan memilih `Kontak` lalu `Publik`. Ini akan menghubungkan Minibits Wallet kamu ke jaringan sosial Nostr, sehingga memungkinkan pemberian tip tanpa hambatan.

Kamu juga punya opsi untuk `Menggunakan profil kamu sendiri` dengan masuk ke `Pengaturan` lalu `Privasi` untuk mengimpor Nostr Address dan kunci milikmu sendiri. Namun, perlu diketahui bahwa dengan melakukan ini, Wallet kamu akan berhenti berkomunikasi dengan server minibits.cash Nostr dan LNURL Address, sehingga fitur Lightning Address untuk menerima zaps dan pembayaran akan dinonaktifkan.


![image](assets/en/09.webp)


## 6️⃣ Menerima dana


Untuk menerima dana pertama kali, kamu perlu mengisi ulang Wallet melalui Invoice Lightning. Prosesnya sangat mudah: ketuk `Topup`, masukkan `Jumlah` yang ingin kamu tambahkan, tambahkan `Memo`, lalu ketuk `Buat Invoice`. Setelah itu, kamu perlu membayar Invoice ini menggunakan Lightning Wallet lain. Proses ini akan mengubah pembayaran Lightning Bitcoin menjadi token ecash di dalam Minibits Wallet kamu.


![image](assets/en/10.webp)


## 7️⃣ Kirim dana


Setelah kamu mendanai Wallet, kamu bisa mengirim dana dengan dua cara berbeda.


### Kirim ecash


Opsi pertama adalah mengirim uang tunai secara langsung. Ketuk `Kirim`, lalu pilih `Kirim uang tunai`, masukkan `Jumlah`, dan ketuk `Buat token`. Ini akan menghasilkan kode QR yang bisa kamu bagikan kepada penerima atau mereka pindai langsung dengan perangkat mereka. Penerima akan melihat token muncul di Wallet mereka hampir seketika, tanpa biaya Blockchain atau penundaan konfirmasi.


![image](assets/en/11.webp)


### Bayar dengan Lightning


Pilihan kedua adalah membayar melalui Lightning. Ketuk `Kirim`, lalu pilih `Bayar dengan Lightning`. Kamu bisa memilih dari `kontak` Nostr kamu (jika sudah menghubungkan npub), atau memasukkan/menempelkan kode pembayaran Lightning Address, Invoice, atau LNURL menggunakan opsi `Tempel` atau `Pindai`. Setelah `Mengonfirmasi` penerima, kamu akan diminta memasukkan `Jumlah yang Harus Dibayar`, menambahkan memo secara opsional, lalu ketuk `Konfirmasi` diikuti dengan `Bayar sekarang` untuk menyelesaikan transaksi Lightning.


![image](assets/en/12.webp)


## 8️⃣ Membuat koneksi NWC


Fitur hebat lainnya dari Minibits adalah kemampuan untuk membuat koneksi `Nostr Wallet Connect (NWC)`, yang memungkinkan aplikasi lain meminta pembayaran dari Wallet kamu tanpa mengekspos kunci privat.

Untuk mengaturnya, buka `Settings (Pengaturan)`, lalu pilih `Nostr Wallet Connect (Sambungan Nostr Wallet)`, dan ketuk `Add new connection (Tambah koneksi)`. Beri nama koneksi kamu dengan nama yang deskriptif untuk mengidentifikasi aplikasi dan akun pengguna yang terkait. Tetapkan batas maksimal harian yang wajar untuk mengontrol jumlah yang dapat digunakan melalui koneksi ini, lalu ketuk `Save` untuk menyelesaikan pengaturan.

Fitur ini sangat berguna untuk layanan seperti Nostr Clients, di mana kamu ingin mengaktifkan pemberian tip otomatis tanpa perlu menyetujui setiap transaksi secara manual.



![image](assets/en/12.webp)


## 🎯 Kesimpulan


Minibits menyediakan pintu masuk yang mudah diakses ke dunia ecash, menawarkan pembayaran yang berfokus pada privasi yang melengkapi kepemilikan Bitcoin kamu. Ingat untuk selalu menyimpan cadangan dengan benar, pertimbangkan menggunakan beberapa mint untuk redundansi, dan hanya menyimpan jumlah yang wajar dalam solusi kustodian ini.

Untuk sumber daya tambahan, lihat repositori GitHub Minibits, situs web resmi, dan saluran Telegram mereka, tempat komunitas aktif berdiskusi mengenai perkembangan dan membantu memecahkan masalah.



- [Github](https://github.com/minibits-cash/minibits_wallet)
- [Situs web](https://www.minibits.cash/)
- [Telegram](https://t.me/MinibitsWallet)


Ekosistem ecash masih terus berkembang, tetapi alat seperti Minibits membuat teknologi privasi yang kuat ini semakin mudah diakses oleh pengguna sehari-hari.
