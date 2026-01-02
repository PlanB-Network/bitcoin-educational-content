---
name: BitcoinVoucherBot P2P
description: Cara Membeli dan Menjual Bitcoin P2P dengan BitcoinVoucherBot
---

![image](assets/cover.webp)



Kita masih mendengar tentang BitcoinVoucherBot, bot Telegram yang dibuat untuk membeli Bitcoin tanpa [KYC] (https://planb.academy/resources/glossary/kyc-know-your-customer) melalui transfer bank SEPA. Sayangnya, per November 2025, BitcoinVoucherBot dalam bentuknya yang tersentralisasi tidak lagi tersedia sebagai layanan tanpa KYC.



Dalam panduan ini, kita akan melihat bagaimana cara kerja implementasi baru yang memungkinkan pengguna untuk membeli dan menjual Bitcoin secara langsung di pasar P2P (Peer-To-Peer) yang baru, sehingga tidak ada KYC. Untuk melawan pembatasan baru yang semakin mengancam kebebasan digital dan privasi, para pengembang menciptakan ekstensi ini, memberikan pengguna kemampuan untuk membeli dan menjual Bitcoin dengan tingkat anonimitas yang tinggi melalui P2P (Peer-To-Peer). Mari kita lihat bersama bagaimana cara kerja metode pertukaran baru ini.



Untuk menggunakan layanan ini, Anda harus melakukan transfer melalui Lightning Network. Jadi, pastikan Anda memiliki wallet yang mendukung protokol ini dan memungkinkan Anda untuk menggunakan "LNURL" atau "Lightning Address" untuk menerima dan mengirim dana.



Di antara dompet yang didukung yang dapat kami temukan:





- [Sats.Mobi] (https://planb.academy/tutorials/wallet/mobile/satsmobi-ea04e1cd-609a-4ea8-9c61-f9de1fe3a1fb) (Bot Telegram) (Penitipan)
- [Wallet Dari Satoshi] (https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7) (Kustodian dengan pertukaran ke Non-Kustodian)
- [Breez](https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06) (Non-custodial)



Atau setiap wallet yang memiliki "Lightning Address" dan menghasilkan faktur Bolt11. Dompet yang menggunakan generate sebagai faktur Bolt12 saat ini tidak didukung. Untuk info lebih lanjut, lihat definisi [Bolt] (https://planb.academy/resources/glossary/bolt).



Untuk tutorial ini, mengingat kemudahan penggunaannya yang langsung dapat digunakan, kita akan menggunakan Wallet of Satoshi.



**Perhatian**: Wallet of Satoshi, meskipun populer di kalangan pemula, bersifat kustodian, dengan kontrol terbatas atas dana; gunakan hanya untuk sementara, segera transfer ke non-kustodian untuk kedaulatan penuh. Pada Oktober 2025, ini mencakup mode kustodian mandiri yang stabil di seluruh dunia di iOS / Android (perbarui aplikasinya), dengan kunci pribadi otonom, beralih di antara mode, alamat Lightning khusus, dan cadangan 12 kata seed. Namun, ini tetap menjadi solusi sementara hingga konsolidasi, lebih memilih wallet non-kustodian yang matang untuk manajemen jangka panjang.



Bagus sekali! Sekarang kita bisa memulai perjalanan kita, yang akan memandu Anda langkah demi langkah dalam membuat akun, mengelola kecocokan pembelian dan penjualan, dan menggunakan area terbatas Anda.



## Wallet dan Pendaftaran



Pertama, jika Anda belum menginstalnya di ponsel cerdas Anda, unduh Wallet of Satoshi.





- [Google Play](https://play.google.com/store/apps/details?id=com.livingroomofsatoshi.wallet&pli=1)
- [App Store](https://apps.apple.com/au/app/wallet-of-satoshi/id1438599608)



![image](assets/it/01.webp)



Jika Anda belum pernah menggunakan Wallet of Satoshi dan ingin memahami cara kerjanya, saya sarankan Anda mengikuti tutorial ini agar Anda dapat mengaktifkannya dengan benar dan mencadangkannya dengan aman.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Setelah wallet Anda siap, Anda dapat mulai mengirimkan sejumlah kecil sats. Perlu diingat bahwa, untuk menyelesaikan pendaftaran platform P2P (Peer-To-Peer) Anda, Anda akan diminta untuk mengirimkan 1000 sats sebagai tindakan kontrol: ini untuk menciptakan penghalang terhadap serangan jenis phantom match (scam), mencegah siapa pun untuk mendaftar tanpa filter spam.



![image](assets/it/02.webp)



Sekarang kita bisa membuka platform P2P (Peer-To-Peer) untuk melanjutkan pendaftaran. Anda dapat masuk dari PC desktop atau browser di ponsel pintar, melalui Telegram BitcoinVoucherBot atau melalui tautan .onion untuk memberikan tingkat privasi yang lebih tinggi.



jika Anda memilih untuk menggunakan tautan Tor .onion, saya juga merekomendasikan "Tor Browser". Jika Anda belum mengetahuinya, Anda bisa mempelajari lebih lanjut di tautan ini:



https://planb.academy/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

Sekarang pilihlah bagaimana Anda ingin menjangkau platform ini.





- [BitcoinVoucherBot] (https://t.me/BitcoinVoucherBot?start=55360009) (Telegram)
- [Desktop PC / Smartphone Browser](https://p2p.bitcoinvoucher.bot/?ref=55360009)
- [Tor .Onion] (http://umembxtpokml6fkogemcfnpyt3qqvyw6u3hnvwinevo3gvoe6j7vfyad.onion/?ref=55360009)



Anda akan diarahkan ke halaman utama.



tekan "Dapatkan Pemula" untuk segera memulai



![image](assets/it/03.webp)



Pada layar berikutnya, Anda harus memilih kata sandi dan memasukkannya (kotak A), kemudian mengulanginya (kotak B). Saya sarankan agar Anda segera menyimpan kata sandi ini ke media cadangan, yang bisa disimpan di perangkat digital yang aman, seperti "Bitwarden":



https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

atau menyimpan kata sandi Anda pada media kertas (**peringatan**: ini bukan solusi yang baik, namun tidak apa-apa jika dimaksudkan sebagai solusi sementara).



Centang kotak verifikasi di mana Anda menyatakan bahwa Anda bukan robot (kotak C). Harap diperhatikan Jangan aktifkan enkripsi RSA kecuali Anda tahu persis apa itu enkripsi RSA dan bagaimana cara kerjanya. Anda tidak perlu melakukan apa pun pada tahap ini. Klik pada "Buat Avatar" ("Generate Avatar") (kotak D).



![image](assets/it/04.webp)



Sekarang Anda harus membayar 1000 sats untuk menyelesaikan pendaftaran.



1. Mulai dari atas, pertama-tama lihat "ID Avatar" Anda yang dibuat secara acak dan sangat penting Simpan dengan hati-hati, seperti yang saya sarankan untuk Anda lakukan dengan kata sandi.


2. Anda kemudian harus memasukkan "Lightning Address" Anda pada kolom di bawah ini. Ini akan memungkinkan Anda untuk menerima pembayaran jika Anda membeli Bitcoin, atau mendapatkan pengembalian dana. Jika Anda menggunakan Wallet Dari Satoshi, Anda akan dapat menyalin Address Anda dengan mengklik terima.


3. Centang kotak verifikasi di mana Anda menyatakan bahwa Anda bukan robot.


4. Lakukan pembayaran sebesar 1000 sats untuk mendapatkan akses ke area terlarang Anda. Jika Anda tidak dapat membingkainya, klik dengan mouse Anda (di PC) atau ketuk dengan jari Anda (di Browser/Smartphone Telegram) untuk menyalin alamat yang perlu Anda tempelkan ke dalam Wallet of Satoshi dan selesaikan pembayaran faktur.



![image](assets/it/05.webp)



Ini adalah LNURL Address Anda.



![image](assets/it/06.webp)



Selamat!!! Anda telah membuat Avatar Anda secara permanen dan Anda dapat melihat ringkasannya di sini. Sekali lagi, saya sarankan agar Anda menyimpan Avatar dan kata sandi Anda dengan hati-hati, seperti yang saya sarankan sebelumnya.



Klik `I've saved my credentials, continue` (diterjemahkan menjadi: "Saya telah menyimpan kredensial saya, lanjutkan")



![image](assets/it/07.webp)



Anda sekarang berada di jantung platform, di mana Anda dapat melihat semua pertandingan perdagangan dengan detailnya. Untuk tampilan yang lebih jelas, di bawah ini Anda akan melihat gambar yang melekat pada situs web dari komputer desktop.





- "Jenis" ("Type") menentukan apakah ini adalah penjualan "Jual" ("sell") atau pembelian "beli" ("buy")
- "Jumlah" ("Amount"): menunjukkan berapa banyak sats yang dijual pengguna jika kecocokan berjenis "Jual", atau berapa banyak Bitcoin yang ingin dibeli pengguna jika kecocokan berjenis "Beli".
- "Harga BTC dengan Margin" ("Harga BTC dengan Margin"): menunjukkan harga dengan mempertimbangkan margin yang diterapkan di atas nilai yang ditandai.
- "Margin" ("Margin") adalah persentase yang diterapkan pada harga pasar, Dengan tanda minus (-) Anda mendapatkan diskon dari harga pasar, Dengan tanda plus (+) premium diterapkan pada harga pasar.
- "Metode" ("Metode") menunjukkan dengan metode mana pengguna lebih suka dibayar.
- "Creator" adalah avatar unik yang digunakan oleh pengguna di platform.
- "Rep" (Reputasi) Tingkat reputasi pengguna berkisar dari -5 tidak dapat diandalkan hingga +5 sangat dapat diandalkan.
- "Status" ("Status"): menunjukkan status pertandingan. Pada contoh tangkapan layar, semua pertandingan tampak "Open" ("Terbuka").
- "Expiration" ("Kadaluarsa"): menunjukkan berapa lama waktu yang tersisa sebelum pertandingan berakhir dan dibatalkan jika tidak dipilih oleh siapa pun.



![image](assets/it/08.webp)



Di bagian kanan atas, klik Avatar Anda untuk mengakses profil Anda.



![image](assets/it/09.webp)



Di sini Anda dapat melihat nama Avatar, ID Pengguna, tanggal pembuatan, dan reputasi Anda, yang akan mencerminkan secara positif atau negatif perilaku Anda dalam negosiasi.



![image](assets/it/10.webp)



Pada bagian Pengaturan, Anda dapat melihat "Lightning Address," yang dimasukkan pada saat pendaftaran, dan mengubahnya jika perlu. Anda juga memiliki opsi untuk membuat Kunci Publik, yang seperti yang disebutkan harus diatur hanya jika Anda memiliki keterampilan yang sesuai. Kunci ini digunakan untuk mengenkripsi pesan yang akan Anda pertukarkan dengan mitra Anda langsung dari komputer Anda.



Fitur Notifikasi Telegram sangat direkomendasikan. Dengan mengaktifkannya, kode QR akan muncul untuk Anda bingkai dengan aplikasi Telegram: dengan cara ini Anda akan menerima notifikasi waktu nyata tentang semua tindakan yang terkait dengan pertandingan Anda, langsung di obrolan bot di Telegram.



![image](assets/it/11.webp)



Terakhir, Anda akan menemukan bagian rujukan Anda, dengan penghasilan yang dihasilkan oleh pengguna yang Anda undang. Dari sini Anda dapat menggunakan tombol untuk membagikan tautan atau kode QR Anda dan, sedikit lebih jauh ke bawah, melihat daftar kecocokan untuk melacak reputasi Anda bersama dengan skor yang sesuai.



![image](assets/it/12.webp)



## Buat pesanan untuk Membeli Bitcoin



Masuk ke Marketplace: dari bilah navigasi utama, klik simbol keranjang "Marketplace" ("Pasar") untuk membuka buku pesanan. kemudian mulai pesanan baru: tekan tombol "Pesanan Baru" ("New Order") untuk memulai proses.



![image](assets/it/13.webp)





- Mengatur detail pesanan:
- Pilih opsi "Beli Bitcoin" ("Beli Bitcoin").
- Masukkan jumlah sats yang Anda inginkan.
- Tentukan margin harga (antara -20% dan +20% dari nilai pasar).
- Pilih metode pembayaran (SEPA Instan, dll.).
- Menunjukkan mata uang pilihan.
- Konfirmasi Pesanan: klik "Buat Pesanan" ("Konfirmasi Pesanan") untuk melanjutkan ke tahap pengajuan.



![image](assets/it/14.webp)



Diperlukan deposit: deposit sebesar 10% dari jumlah total, ditambah biaya layanan, diperlukan untuk mengaktifkan pesanan.




- Pembayaran deposit: ketika pesanan dibuat, sistem secara otomatis menghasilkan faktur Lightning. Deposit hanya bersifat sementara dan akan dikembalikan ketika pesanan selesai.
- Fitur utama:
- Uang jaminan: 10% dari nilai pesanan.
- Biaya layanan: biaya untuk menggunakan platform.
- Batas waktu: Anda memiliki waktu 5 menit untuk melakukan pembayaran, jika tidak, transaksi akan kedaluwarsa.



![image](assets/it/15.webp)



Setelah pembayaran berhasil, order akan muncul di buku dan dapat dilihat oleh semua pengguna, yang dapat memilih dan menerimanya. Untuk membuat order jual, yang perlu Anda lakukan adalah mengklik "Jual Bitcoin" ("Jual Bitcoin"), masukkan jumlah satoshi yang ingin Anda jual, tentukan margin, pilih metode pembayaran dan mata uang, lalu lanjutkan dengan deposit 10% sebagai uang jaminan. Setelah selesai, match Anda akan terlihat di daftar.



![image](assets/it/16.webp)



## Cara menerima pesanan



1. Penjual dapat melihat daftar semua pesanan yang tersedia di buku.


2. Periksa detailnya: setiap pesanan menunjukkan informasi seperti:




  - Jumlah Bitcoin,
  - Margin harga,
  - Metode pembayaran,
  - Reputasi pengguna.



![image](assets/it/17.webp)



3. Klik pada pesanan untuk membuka lembar lengkap dengan semua informasi.


4. Tekan "Jual Bitcoin" ("Jual Bitcoin") untuk menerima proposal.



![image](assets/it/18.webp)



## Setoran yang diperlukan oleh penjual



Ketika pesanan diterima, sistem akan membuat faktur pembayaran. Setoran sudah termasuk:



- Jumlah total pesanan,



- komisi layanan.



Pembayaran deposit harus dilakukan dalam batas waktu yang ditentukan, jika tidak, transaksi tidak akan dikonfirmasi.



![image](assets/it/19.webp)



## Mengirim instruksi pembayaran



Setelah deposit dilakukan, transaksi akan muncul di dasbor pribadi penjual, yang harus memberikan detail kepada pembeli untuk menyelesaikan pembayaran dalam mata uang fiat.



1. Penjual menampilkan transaksi aktif di panel mereka.


2. Klik "Kirim Instruksi Pembayaran."


3. Masukkan semua informasi yang diperlukan untuk pembayaran fiat (IBAN, penerima, alamat, alasan pembayaran, dll.).


4. Klik "Kirim Pesan" ("Send Message") untuk mengirimkan data kepada pembeli.



![image](assets/it/20.webp)



## Prosedur pembayaran



Pembeli menerima, dalam obrolan platform, pesan dengan semua data yang diperlukan untuk melakukan pembayaran dalam mata uang fiat:




- Detail bank: IBAN dengan nama dan alamat pemegang rekening penjual.
- Jumlah yang tepat: jumlah fiat yang tepat untuk ditransfer.
- Penyebab/keterangan: teks yang akan disertakan dalam transaksi.
- Batas waktu: batas waktu untuk menyelesaikan pembayaran.



Transfer dilakukan di luar sistem P2P dan harus dilakukan melalui lembaga perbankan.



⚠️ **Catatan penting:** konfirmasi pada platform harus dilakukan hanya setelah Anda benar-benar mengatur transfer atau pembayaran fiat melalui bank Anda.



![image](assets/it/21.webp)



## Konfirmasi fiat pembayaran



Langkah ini sangat penting bagi pembeli dan harus dilakukan hanya setelah memverifikasi bahwa pembayaran benar-benar telah dikirim.



1. Menerima data: pembeli telah menerima instruksi pembayaran dari penjual.


2. Eksekusi pembayaran: transfer fiat diatur dari rekening bank seseorang.


3. Verifikasi: periksa apakah operasi telah diproses dengan benar.


4. Konfirmasi di platform: klik "Konfirmasi pembayaran fiat" ("Konfirmasi pembayaran fiat") di halaman jual beli.


Tombol "Konfirmasi Pembayaran fiat" muncul di bagian transaksi dan hanya boleh digunakan setelah memverifikasi bahwa pembayaran memang telah terkirim.



![image](assets/it/22.webp)



Langkah terakhir dalam proses ini adalah penjual mengonfirmasi penerimaan pembayaran fiat, setelah itu satss dilepaskan ke pembeli.



![image](assets/it/23.webp)



## Kesimpulan



Dengan harapan, tutorial ini akan membantu Anda untuk menggunakan metode baru untuk memperdagangkan Bitcoin atau bahkan hanya membelinya, baik untuk penyimpanan nilai Anda sendiri atau untuk mulai melakukan pembayaran harian. Namun, ini tetap menjadi pintu untuk dijelajahi untuk menghadapi apa yang akan terjadi di dunia digital kita.



Jerat yang dijalankan oleh badan-badan yang mengendalikan kita semakin ketat, untuk melahirkan Internet yang semakin terkendali. Dengan membeli P2P, Anda akan menyimpan pembelian Anda dalam anonimitas total, tidak meninggalkan jejak dan tidak ada dampak lanjutan dari pihak ketiga.