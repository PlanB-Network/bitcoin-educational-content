---
name: Macadamia Wallet
description: Cashu mobile wallet untuk pembayaran BTC secara anonim dan instan
---

![cover](assets/cover.webp)



Macadamia Wallet adalah wallet mobile iOS yang mengimplementasikan protokol Cashu, sebuah sistem ecash Chaumian yang memungkinkan pembayaran Bitcoin yang sepenuhnya anonim. Berkat tanda tangan buta, tidak ada pengamat yang dapat menghubungkan simpanan Anda dengan pembelanjaan Anda, menawarkan kerahasiaan yang mirip dengan uang tunai fisik.



Dalam tutorial ini, kita akan melihat cara menginstal dan mengonfigurasi Macadamia, melakukan transaksi Cashu pertama Anda (Mint, Send, Receive, Melt), dan mengelola beberapa mint untuk mengamankan dana Anda.



## Apa itu Macadamia Wallet?



### Protokol Cashu



Cashu menggunakan tanda tangan buta yang ditemukan oleh David Chaum: Anda menyetorkan bitcoin ke server "mint", yang mengeluarkan token yang setara dengan satoshi. Mint menandatangani token-token ini tanpa melihat isinya, sehingga mustahil untuk menghubungkan token ke pengguna. Pertukarannya bersifat off-chain, peer-to-peer, dan benar-benar tidak jelas - bahkan mint tidak dapat melacak siapa yang membayar siapa.



Macadamia adalah sumber terbuka wallet iOS yang dikembangkan di Swift/SwiftUI. Ia bekerja tanpa akun atau KYC, token Anda disimpan secara lokal dan dilindungi oleh frasa seed. Kode dapat diaudit di GitHub dan token dapat dioperasikan dengan dompet Cashu lainnya (Minibits, Cashu.me).



### Model kustodian dan kompromi



**Penting**: Cashu beroperasi dengan model kustodian. Token adalah janji untuk membayar (IOU) yang didukung oleh cadangan Bitcoin milik mint. Jika mint menghilang, token Anda akan kehilangan nilainya. Ini adalah kompromi untuk kerahasiaan maksimum.



Gunakan Macadamia sebagai wallet fisik: dalam jumlah kecil saja. Sebarkan dana Anda ke beberapa mint untuk mengurangi risiko.



## Fitur utama



Macadamia mengimplementasikan empat operasi dasar dari protokol Cashu. **Mint** mengubah satoshi Anda menjadi token melalui faktur Lightning. **Send** memungkinkan Anda mengirim token secara gratis melalui kode QR atau tautan, sepenuhnya off-chain. **Receive** memungkinkan Anda menerima token atau faktur Lightning generate. **Melebur** membayar faktur Lightning dengan menghancurkan token Anda.



wallet mendukung pengelolaan beberapa mint secara bersamaan. Anda dapat menukar token di antara mint yang berbeda melalui Lightning.



## Platform yang didukung



Macadamia hanya tersedia di iOS 17 atau lebih tinggi untuk iPhone dan iPad. Aplikasi Swift/SwiftUI asli menawarkan integrasi optimal dengan ekosistem Apple.



Protokol Cashu menjamin interoperabilitas antar dompet. Anda bisa mengembalikan frasa seed Anda di aplikasi lain seperti Minibits di Android atau Nutstash di desktop.



Versi saat ini didistribusikan melalui TestFlight. Gunakan hanya dalam jumlah kecil dengan versi beta ini.



## Instalasi



Macadamia saat ini tersedia melalui TestFlight, program pengujian beta Apple. Berikut cara menginstalnya:



### Instalasi melalui TestFlight



**Langkah 1: Unduh TestFlight**



Jika Anda belum memiliki aplikasi TestFlight di perangkat Anda, cari "TestFlight" di App Store dan instal. TestFlight adalah aplikasi resmi Apple untuk menguji versi beta aplikasi iOS.



**Langkah 2: Bergabunglah dengan program beta Macadamia** (dalam bahasa Prancis)



Setelah TestFlight terinstal, ikuti tautan undangan dari iPhone atau iPad Anda: [https://testflight.apple.com/join/RMU6PaRu](https://testflight.apple.com/join/RMU6PaRu)



Tautan akan secara otomatis membuka TestFlight dan menawarkan Anda untuk menginstal Macadamia Wallet. Sentuh "Terima" lalu "Instal" untuk memulai pengunduhan. Aplikasi ini memiliki berat sekitar sepuluh megabyte dan hanya membutuhkan waktu beberapa detik untuk menginstal.



![Installation TestFlight](assets/fr/01.webp)



### Informasi penting tentang versi beta



Macadamia masih dalam tahap pengembangan aktif. Versi TestFlight sering diperbarui dan mungkin memperkenalkan fitur baru atau memperbaiki bug. Namun, seperti halnya versi beta lainnya, kegagalan fungsi dapat terjadi. **Kami sangat menyarankan agar Anda hanya menggunakan dalam jumlah kecil**, yang dapat hilang jika terjadi masalah teknis.



Macadamia tidak mengumpulkan data pengguna apa pun sesuai dengan kebijakan privasi yang ditampilkan. Pastikan untuk memeriksa bahwa pengembangnya adalah cypherbase UG saat menginstal.



## Konfigurasi awal



Saat pertama kali diluncurkan, Macadamia menghasilkan kalimat BIP-39 yang terdiri dari 12 kata. Tulislah di tempat yang aman - jangan pernah dijadikan tangkapan layar. Kata-kata ini memungkinkan Anda untuk membuat ulang wallet dan membelanjakan token Anda.



![Configuration initiale](assets/fr/02.webp)



Ikuti empat langkah: selamat datang, terima persyaratan, simpan kalimat seed, dan konfirmasi akhir.



![Interface principale](assets/fr/03.webp)



Setelah konfigurasi selesai, Macadamia menampilkan tiga tab utama. **Wallet** menampilkan saldo dan riwayat transaksi Anda. **Mints** memungkinkan Anda mengelola server Cashu Anda. **Settings** memberikan akses ke pengaturan dan frasa seed Anda.



![Ajout d'un mint](assets/fr/04.webp)



Sekarang Anda perlu mengonfigurasi mint, yaitu server Cashu yang akan menerbitkan token Anda. Buka tab "Mints", ketuk "Add new Mint URL", dan masukkan alamat mint yang Anda pilih (mis. mint.cubabitcoin.org). Kunjungi bitcoinmints.com atau cashu.space untuk melihat mint publik yang memiliki reputasi baik. Validasi hanya mint yang reputasinya telah Anda periksa, karena mereka akan memiliki hak asuh atas satoshi Anda.



## Penggunaan sehari-hari



### Pembuatan token baru (Mint)



Untuk memberi makan wallet Macadamia Anda dengan ecash, Anda perlu melakukan operasi "Mint" (untuk membuat token). Sentuh "Terima", lalu pilih opsi "Kilat". Masukkan jumlah yang diinginkan (misalnya 1000 sats), pilih mint yang akan digunakan, lalu generate faktur Lightning.



![Opération Mint](assets/fr/05.webp)



Bayar faktur Lightning yang dihasilkan dengan wallet biasa (Phoenix, Zeus, BlueWallet).



![Confirmation Mint](assets/fr/06.webp)



Token Cashu langsung muncul di saldo Anda setelah pembayaran.



### Kirim token



Untuk mengirim token Cashu ke pengguna lain, sentuh tombol "Kirim" di layar utama, lalu pilih "Ecash". Masukkan jumlah yang akan dikirim (misalnya 50 sats) dan tambahkan memo deskriptif jika diperlukan.



![Envoi Ecash](assets/fr/07.webp)



Bagikan kode QR atau teks yang dihasilkan melalui iMessage, Signal, atau Telegram. Penerima mengklaim dana secara instan dan gratis.



### Menerima token



Untuk menerima token Cashu yang dikirim oleh pengguna lain, sentuh "Terima" lalu pilih "Ecash". Pindai kode QR token atau tempelkan tautan token yang Anda terima.



![Réception Ecash](assets/fr/08.webp)



Sentuh "Redeem" untuk mengklaim token.



### Pembayaran Kilat (Meleleh)



Untuk membayar faktur Lightning dengan token Cashu Anda, sentuh "Kirim" lalu pilih "Lightning". Tempelkan faktur BOLT11 yang ingin Anda bayar.



![Paiement Lightning](assets/fr/11.webp)



Mint menghancurkan token Anda dan mengeksekusi pembayaran Lightning. Jadi, Anda bisa membayar layanan Lightning apa pun sambil menjaga anonimitas Anda.



### Tukar di antara permen



Ketika Anda menerima token dari mint yang belum Anda konfigurasikan, Macadamia menawarkan beberapa opsi untuk mengelola token ini.



![Swap inter-mints](assets/fr/09.webp)



Tambahkan mint baru atau tukar token ke mint yang sudah ada. Swap menggunakan Lightning sebagai jembatan untuk mentransfer dana Anda secara anonim.



### Manajemen multi-mint tingkat lanjut



Macadamia menawarkan alat canggih untuk mengelola beberapa mint secara bersamaan dan mengalokasikan dana Anda secara strategis.



![Gestion multi-mints](assets/fr/10.webp)



"Bagikan Dana" secara otomatis mendistribusikan saldo Anda berdasarkan persentase (misalnya 50/50). "Transfer" memungkinkan transfer manual antar mint untuk mendiversifikasi risiko Anda.



## Keuntungan dan keterbatasan



**Sorotan** :





- Kerahasiaan maksimum**: Transaksi yang tidak dapat dilacak, bahkan oleh mint. Tidak ada metadata blockchain, pertukaran peer-to-peer tanpa jejak.
- Cepat dan gratis**: Transfer instan gratis dalam sekejap, ideal untuk pembayaran mikro.
- Interoperabilitas**: token Cashu yang terstandarisasi untuk digunakan dengan dompet lain yang kompatibel (Minibits, Nutstash).
- Kesederhanaan**: Interface iOS native dapat diakses oleh pemula namun tetap dapat diaudit (open source).



**Kendala** :





- Model kustodian**: diperlukan kepercayaan mint. Jika mint menghilang, token Anda akan kehilangan nilainya.
- hanya untuk iOS**: Tidak ada versi Android/desktop. Interoperabilitas Cashu memungkinkan akses melalui dompet lain, tetapi pengalaman optimal tetap di iOS.
- Ketergantungan terhadap Mint**: Mint offline = tidak dapat melakukan transaksi yang membutuhkan intervensinya (Mint, Melt).
- Teknologi yang sedang berkembang**: Pengembangan aktif, kemungkinan bug, standar yang terus berkembang.



## Praktik terbaik





- Diversifikasi koin Anda**: Sebarkan chip Anda di beberapa mint terkemuka untuk mengurangi risiko.
- Jumlah batas**: Gunakan Macadamia sebagai wallet fisik untuk pembayaran harian, bukan sebagai brankas.
- Amankan seed** Anda: Simpan frasa 12 kata Anda di atas kertas di tempat yang aman. Lakukan uji coba pemulihan sesekali.
- Periksa mint**: Konsultasikan dengan cashu.space dan forum komunitas sebelum menambahkan mint. Pilihlah yang memiliki waktu aktif yang baik dan reputasi yang baik.
- VPN atau Tor**: Sembunyikan IP Anda dengan VPN/Tor untuk memaksimalkan privasi jaringan.
- Bergabunglah dengan komunitas**: Grup Telegram/Discord Cashu untuk mendapatkan informasi terbaru, rekomendasi mint, dan praktik terbaik.



## Kesimpulan



Macadamia Wallet membawa sifat-sifat uang tunai fisik ke Bitcoin digital. Dengan menggabungkan tanda tangan buta Chaum dan Lightning, ia menawarkan solusi elegan untuk kerahasiaan transaksi. Antarmuka iOS-nya yang asli membuat teknologi kriptografi yang canggih dapat diakses namun tetap open source dan dapat dioperasikan dengan ekosistem Cashu.



Model kustodian menuntut kewaspadaan dan praktik keamanan yang baik. Jika digunakan dengan benar, Macadamia menjadi alat yang sangat berharga untuk pembayaran sehari-hari yang membutuhkan anonimitas, melengkapi dompet non-kustodian untuk tabungan.



## Sumber daya



### Dokumentasi resmi




- Situs web resmi: [macadamia.cash](https://macadamia.cash)
- Pertanyaan Umum Macadamia: [macadamia.cash/faq](https://macadamia.cash/faq)
- Kode sumber GitHub: [github.com/zeugmaster/macadamia](https://github.com/zeugmaster/macadamia)



### Dokumentasi Cashu




- Dokumentasi teknis: [docs.cashu.space](https://docs.cashu.space)
- Daftar mint publik: [bitcoinmints.com](https://bitcoinmints.com)
- Situs web protokol resmi: [cashu.space](https://cashu.space)



### Komunitas




- Grup Telegram Cashu: [t.me/cashu_ecash](https://t.me/cashu_ecash)