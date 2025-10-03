---
name: Minibits Wallet
description: Panduan untuk Minibits Wallet
---

![cover](assets/cover.webp)


Dalam tutorial ini, saya akan memandu Anda dalam menyiapkan Minibits Wallet untuk menggunakan ecash. Teknologi pembayaran yang berfokus pada privasi yang kuat yang bekerja bersama Bitcoin. Minibits adalah ecash dan Lightning Wallet yang memungkinkan transfer nilai secara instan, murah, dan privat, sehingga sangat ideal untuk transaksi sehari-hari yang mengutamakan privasi.


Sebelum kita membahas tentang Minibits, mari kita buat pemahaman yang jelas tentang apa itu ecash dan apa yang bukan. Banyak orang yang mengacaukan ecash dengan teknologi Bitcoin atau Blockchain, tetapi pada dasarnya keduanya merupakan konsep yang berbeda.


Ecash BUKAN Bitcoin. Ecash tidak menggantikan kustodian mandiri Bitcoin Wallet Anda, melainkan melengkapinya. Ecash BUKAN Blockchain dan TIDAK hidup di Ledger publik mana pun. Menariknya, ecash BUKAN merupakan teknologi baru - ecash sebenarnya sudah ada sebelum web di seluruh dunia, dengan konsep yang dikembangkan pada tahun 1980-an dan 1990-an.


Apa itu ecash: sangat pribadi (transaksi tidak meninggalkan riwayat yang dapat dilacak), peer-to-peer (transfer langsung tanpa perantara), dan berfungsi sebagai instrumen pembawa digital (jika Anda memilikinya, Anda yang mengendalikannya). Keuntungan utamanya adalah ecash DAPAT digunakan secara offline-baik pengirim maupun penerima dapat terputus dari internet selama transaksi berlangsung. Ecash DAPAT dicetak oleh satu pihak atau oleh federasi entitas tepercaya, dan merupakan teknologi pelengkap yang sempurna untuk Bitcoin, menangani transaksi kecil yang sering terjadi sementara Bitcoin berfungsi sebagai penyelesaian Layer.


Harap diperhatikan bahwa pengaturan Minibits ini merupakan `solusi kustodian`, yang berarti Anda mempercayai operator Mint untuk mengelola dana Anda. Hal ini menimbulkan risiko spesifik yang harus Anda pahami sebelum melanjutkan.


Proyek menampilkan disclaimer penting ini:


- Wallet ini hanya boleh digunakan untuk tujuan penelitian.
- Wallet adalah versi beta dengan fungsionalitas yang belum lengkap dan bug yang diketahui dan tidak diketahui.
- Jangan menggunakannya dengan uang tunai dalam jumlah besar.
- Uang elektronik yang disimpan dalam Wallet dikeluarkan oleh mint
- anda mempercayai mint untuk mendukungnya dengan Bitcoin sampai Anda mentransfer kepemilikan Anda ke Bitcoin lightning Wallet.
- Protokol Cashu yang diimplementasikan oleh Wallet belum mendapatkan tinjauan atau pengujian yang ekstensif.


Perlakukan Minibits seperti Wallet sehari-hari, bukan rekening tabungan, dan jangan pernah menyimpan nilai yang signifikan di sini.


## 1️⃣ Menyiapkan Wallet Anda


Untuk memulai, kunjungi [Situs Web Minibits](https://www.minibits.cash/) di mana Anda akan menemukan opsi pengunduhan untuk semua platform utama. Pengguna iOS dapat mengunduh dari [App Store](https://testflight.apple.com/join/defJQgTD), sementara pengguna iOS Uni Eropa memiliki opsi tambahan untuk menginstal dari [Freedom Store](https://freedomstore.io/). Pengguna Android bisa mendapatkan aplikasi ini dari [Google Play Store](https://play.google.com/store/apps/details?id=com.minibits_wallet) atau mengunduh file APK langsung dari halaman [GitHub Releases](https://github.com/minibits-cash/minibits_wallet/releases).


Saat menginstal Minibits, Anda akan melihat layar pengantar yang menjelaskan konsep dasarnya-Anda dapat membaca semua ini atau melewatinya jika Anda sudah terbiasa dengan teknologinya. Setelah Anda menyelesaikan langkah-langkah awal ini, Anda akan diminta untuk memilih:


- `Mengerti, bawa saya ke Wallet` untuk pengguna baru atau
- `Pulihkan Wallet yang hilang` jika Anda memulihkan dari cadangan.


![image](assets/en/01.webp)

Setelah menyelesaikan penyiapan awal, Anda akan masuk ke Layar Utama, yang memiliki beberapa Elements penting yang perlu diperhatikan. ① Ikon profil di sudut atas akan membawa Anda ke halaman profil di mana Anda bisa mengakses Minibits Wallet Address dan memilih opsi `batch receive`. ② Di tengah layar, Anda akan melihat Mint yang dapat Anda gunakan, dengan mint Minibits yang dipilih secara default. ③ Baris tindakan di bawah ini menyediakan opsi untuk mengirim pembayaran tunai atau kilat, memindai kode QR, dan menerima pembayaran. ④ Terakhir, bilah navigasi bagian bawah berisi pintasan ke layar Beranda, Riwayat Transaksi, Kontak, dan Pengaturan.


![image](assets/en/02.webp)


## 2️⃣ Mengelola permen


Secara default, mint Minibits diaktifkan ketika Anda memulai aplikasi. Namun, salah satu kekuatan ecash adalah kemampuannya untuk menggunakan beberapa mint untuk meningkatkan desentralisasi dan keamanan. Untuk menambahkan mint lain, buka `Pengaturan`, lalu pilih `Kelola mint`, dan terakhir ketuk `Tambahkan mint`.


(Bitcoinmints.com) menyediakan daftar lengkap mint yang tersedia dengan peringkat pengguna untuk membantu Anda memilih opsi yang memiliki reputasi baik. Menggunakan beberapa mint mengurangi risiko Anda. Jika satu mint mengalami masalah, dana Anda di mint lain tetap dapat diakses.


![image](assets/en/04.webp)


## 3️⃣ Membuat Cadangan


Pencadangan bisa dibilang merupakan langkah yang paling penting dalam keseluruhan proses penyiapan. Untuk mengakses opsi Pencadangan, navigasikan ke `Pengaturan`-> `Pencadangan` Di sini Anda akan menemukan dua opsi penting:

1. 'Frasa seed Anda' yang berisi '12 kata' yang memungkinkan Anda untuk memulihkan saldo ecash Anda jika perangkat hilang. Frasa seed ini adalah kunci utama Anda untuk semua ecash di semua koin yang telah Anda tambahkan. Tuliskan pada media fisik (kertas atau logam) dan simpan dengan aman di beberapa lokasi. Jangan pernah menyimpan frasa seed Anda secara digital di tempat yang dapat membahayakan. Pertimbangkan untuk mengunjungi [tutorial] (https://planb.network/en/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270) ini untuk mengetahui praktik terbaik dalam melindungi Wallet Anda.

2. `Backup Wallet` yang berisi string backup yang panjang.


**Perhatian**: Anda masih memerlukan frasa seed saat menggunakan cadangan ini untuk memulihkan Wallet Anda.


![image](assets/en/05.webp)


## 4️⃣ Buat Minibits Wallet Address


Selanjutnya arahkan ke `Kontak` di bagian bawah dan sesuaikan `Minibits Wallet Address` khusus Anda dengan mengetuk `Ubah` -> `Ubah Wallet Address`. Masukkan Address yang Anda inginkan dan periksa ketersediaannya.


![image](assets/en/07.webp)


Setelah mengatur Address, Anda akan diminta untuk memberikan sedikit `Donasi` untuk mendukung proyek ini. Meskipun ini opsional, saya sangat menyarankan untuk mempertimbangkannya jika Anda berencana untuk menggunakan layanan ini secara teratur. Proyek sumber terbuka seperti Minibits mengandalkan dukungan komunitas untuk melanjutkan pengembangan dan pemeliharaan. Bahkan kontribusi kecil pun dapat membantu memastikan keberlangsungan proyek ini.


![image](assets/en/08.webp)


## 5️⃣ Pengaturan Nostr


Jika Anda ingin memberi tip kepada orang yang Anda ikuti di Nostr, Anda bisa `Tambahkan kunci npub Anda` dengan memilih `Kontak` lalu `Publik`. Hal ini akan menghubungkan Minibits Wallet Anda ke jaringan sosial Nostr, sehingga memungkinkan pemberian tip tanpa hambatan.


Anda juga memiliki opsi untuk `Menggunakan profil Anda sendiri` dengan masuk ke `Pengaturan` dan kemudian `Privasi` untuk mengimpor Nostr Address dan kunci Anda sendiri. Namun, perlu diketahui bahwa dengan melakukan hal ini, Wallet Anda akan berhenti berkomunikasi dengan server minibits.cash Nostr dan LNURL Address, yang akan menonaktifkan fitur-fitur lightning Address untuk menerima zaps dan pembayaran.


![image](assets/en/09.webp)


## 6️⃣ Menerima dana


Untuk menerima dana pertama kali, Anda perlu mengisi ulang Wallet Anda melalui Invoice kilat. Prosesnya sangat mudah: ketuk `Topup`, masukkan `Jumlah` yang ingin Anda tambahkan, tambahkan `Memo`, lalu ketuk `Buat Invoice`. Anda kemudian harus membayar Invoice ini menggunakan Lightning Wallet lainnya, ini akan mengubah pembayaran Lightning Bitcoin menjadi token ecash di dalam Minibits Wallet Anda.


![image](assets/en/10.webp)


## 7️⃣ Kirim dana


Setelah Anda mendanai Wallet, Anda bisa mengirim dana dengan dua cara berbeda.


### Kirim ecash


Opsi pertama adalah mengirim uang tunai secara langsung. Ketuk `Kirim`, lalu pilih `Kirim uang tunai`, masukkan `Jumlah`, dan ketuk `Buat token.` Ini akan menghasilkan kode QR generate yang bisa Anda bagikan kepada penerima atau mereka pindai secara langsung dengan perangkat mereka. Penerima akan melihat token muncul di Wallet mereka hampir seketika, tanpa biaya Blockchain atau penundaan konfirmasi.


![image](assets/en/11.webp)


### Bayar dengan Lightning


Pilihan kedua adalah membayar melalui Lightning. Ketuk `Kirim`, lalu pilih `Bayar dengan Lightning`. Anda dapat memilih dari `kontak` Nostr Anda (jika Anda telah menghubungkan npub Anda), atau memasukkan/menempelkan kode pembayaran Lightning Address, Invoice, atau LNURL dengan menggunakan opsi `Tempel` atau `pindai`. Setelah `Mengkonfirmasi` penerima, Anda akan diminta untuk memasukkan `Jumlah yang Harus Dibayar`, menambahkan memo secara opsional, lalu ketuk `Konfirmasi` diikuti dengan `Bayar sekarang` untuk menyelesaikan transaksi Lightning.


![image](assets/en/12.webp)


## 8️⃣ Membuat koneksi NWC


Fitur hebat lainnya dari Minibits adalah kemampuan untuk membuat koneksi `Nostr Wallet Connect (NWC), yang memungkinkan aplikasi lain untuk meminta pembayaran dari Wallet Anda tanpa mengekspos kunci pribadi Anda.


Untuk mengaturnya, buka `Settings (Pengaturan), lalu pilih `Nostr Wallet Connect (Sambungan Nostr Wallet), dan ketuk `Addend connection (Tambah koneksi). Beri nama koneksi Anda dengan nama yang deskriptif untuk mengidentifikasi aplikasi dan akun pengguna yang terkait. Tetapkan batas maksimal harian yang wajar untuk mengontrol jumlah yang dapat digunakan melalui koneksi ini, lalu ketuk `Save` untuk menyelesaikan pengaturan.


Fitur ini sangat berguna untuk layanan seperti Nostr Clients di mana Anda ingin mengaktifkan pemberian tip otomatis tanpa perlu menyetujui setiap transaksi secara manual.


![image](assets/en/12.webp)


## 🎯 Kesimpulan


Minibits menyediakan pintu masuk yang dapat diakses ke dunia ecash, menawarkan pembayaran yang berfokus pada privasi yang melengkapi kepemilikan Bitcoin Anda. Ingatlah untuk selalu menyimpan cadangan yang tepat, pertimbangkan untuk menggunakan beberapa mint untuk redundansi, dan hanya menyimpan jumlah yang sesuai dalam solusi kustodian ini.


Untuk sumber daya tambahan, lihat repositori GitHub Minibits, situs web resmi, dan saluran Telegram mereka di mana komunitas secara aktif mendiskusikan perkembangan dan memecahkan masalah


- [Github](https://github.com/minibits-cash/minibits_wallet)
- [Situs web](https://www.minibits.cash/)
- [Telegram](https://t.me/MinibitsWallet)


Ekosistem ecash masih terus berkembang, tetapi alat seperti Minibits membuat teknologi privasi yang kuat ini semakin mudah diakses oleh pengguna sehari-hari.