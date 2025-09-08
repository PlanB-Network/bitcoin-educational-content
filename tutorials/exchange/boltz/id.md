---
name: Boltz
description: Tukar-menukar di antara lapisan Bitcoin yang berbeda dengan tetap mempertahankan kontrol.
---


![cover](assets/cover.webp)



Sejak diluncurkan pada tahun 2009, sistem uang elektronik peer-to-peer Bitcoin telah berkembang secara eksponensial, memberikan solusi yang saat ini memungkinkannya menjadi sistem yang dapat kita gunakan secara instan dalam kegiatan sehari-hari, terutama melalui Lightning Network.



Namun, masalah utama tetap ada di antara lapisan protokol Bitcoin: interoperabilitas yang lancar. Untuk memanfaatkan potensi penuh Bitcoin, sangat penting untuk menemukan solusi yang memungkinkan transaksi antara berbagai lapisan protokol. Kebutuhan ini memunculkan Boltz pada tahun 2019, sebuah jembatan yang menghubungkan beberapa lapisan Bitcoin.



## Apa itu Boltz?



[Boltz] (https://boltz.Exchange) adalah platform non-kustodian yang ideal bagi siapa saja yang ingin bertransaksi di antara berbagai lapisan protokol Bitcoin:




- on chain**: Rantai utama Bitcoin di mana transaksi dikonfirmasi rata-rata setiap 10 menit, biaya transaksi sering kali tinggi, yang belum tentu memenuhi kebutuhan pengguna;
- Lightning Network**: Hamparan Bitcoin untuk pembayaran instan dengan biaya rendah, memungkinkan Bitcoin digunakan untuk pembayaran harian;
- Liquid Network**: hamparan untuk Bitcoin yang dibuat oleh Blockstream, memungkinkan Confidential Transactions yang cepat dan penggunaan instrumen keuangan berbasis Bitcoin lainnya;
- RootStock**: Solusi untuk mengembangkan kontrak pintar berdasarkan protokol Bitcoin.



![layers](assets/fr/01.webp)



Interoperabilitas di antara berbagai lapisan ini sangat penting, karena memberikan fleksibilitas yang dibutuhkan pengguna untuk memanfaatkan semua yang ditawarkan ekosistem Bitcoin.



Boltz menggunakan pertukaran atom. Teknologi ini memungkinkan bitcoin untuk dipertukarkan antara 2 lapisan (misalnya BTC onchain di Exchange untuk BTC di Lightning) secara langsung antara dua pihak, tanpa perlu kepercayaan dan tanpa perlu perantara. Pertukaran ini disebut "atomik" karena hanya dapat menghasilkan dua hasil:




- Jika Exchange berhasil dan kedua peserta telah menukarkan BTC mereka secara efektif;
- Jika Exchange gagal, dan kedua peserta pergi dengan BTC asli mereka.



Dengan cara ini, Anda memiliki hak kepemilikan permanen atas bitcoin Anda, dan Exchange tidak didasarkan pada kepercayaan apa pun terhadap pihak lawan: baik Exchange berhasil atau gagal, tetapi tidak ada pihak yang dapat mencuri dana pihak lain.



Exchange atom bekerja dengan kontrak pintar [HTLC] (https://planb.network/resources/glossary/htlc) (*Hashed Timelock Contract*). Pada jenis Contract ini, jumlahnya "dikunci" dalam saluran dua arah dan ada batasan waktu yang diberlakukan, sehingga jika transaksi tidak diselesaikan dalam waktu tertentu, saldo akan kembali ke deposan. Ini adalah mekanisme yang digunakan oleh platform Boltz.



## Pertukaran pertama Anda dengan Boltz



Boltz adalah platform web non-depositori yang tidak memerlukan informasi pribadi dari Anda. Boltz memiliki Interface yang minimalis dan lancar yang memungkinkan Anda untuk memulai perdagangan dalam waktu kurang dari satu menit.



![boltz](assets/fr/02.webp)



Setelah berada di platform, Anda dapat membuat pertukaran atom di antara berbagai lapisan ekosistem Bitcoin.



![home](assets/fr/03.webp)



Anda akan melihat jumlah minimum dan maksimum satoshi (unit terkecil Bitcoin) yang dapat Anda perdagangkan melalui Boltz, termasuk biaya jaringan dan persentase yang dikenakan oleh Boltz antara 0,1% dan 0,5%.



![fees](assets/fr/04.webp)



Kemudian pilih Layer dari mana Anda ingin membuat Exchange atom, dan pilih Layer di mana Anda ingin menerima bitcoin.



![couches](assets/fr/05.webp)



Dalam tutorial ini, kita akan berfokus pada atom Exchange dari Layer utama hingga Lightning Network.



Anda bisa mengonfigurasi unit dasar untuk bursa Anda dengan memilih di antara opsi-opsi :




- BTC ;
- Sats.



![unités](assets/fr/06.webp)



Setelah Anda menyelesaikan konfigurasi dasar Anda, masukkan jumlah Exchange atomik Anda, kemudian buat Lightning Invoice untuk jumlah yang setara, atau cukup masukkan LNURL Anda.



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.network/tutorials/wallet/mobile/blitz-wallet-794bdac4-1af4-49d5-9ea5-abb8228ca196

![swap](assets/fr/07.webp)



Untuk berjaga-jaga, silakan periksa parameter Exchange atomik Anda untuk mengekspor kunci cadangan yang ditautkan ke Exchange Anda.



Pada ikon **Pengaturan**, unduh kunci cadangan dan simpan file dengan tepat.



![settings](assets/fr/08.webp)



![rescue-key](assets/fr/09.webp)



File ini berisi 12 kata kunci portofolio yang terkait dengan bursa atom Anda.



Kemudian klik tombol **Buat atom Exchange** dan lanjutkan dengan pembayaran sejumlah yang ditunjukkan.



![payment](assets/fr/10.webp)



https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

https://planb.network/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

Setelah pembayaran Anda dilakukan dan dikonfirmasi, Anda akan secara otomatis menerima jumlah yang setara pada Lightning Wallet Anda.



Pada menu **Refund**, cari riwayat Exchange atomik Anda untuk mengidentifikasi Exchange yang ingin Anda kembalikan dananya. Anda juga bisa mengimpor riwayat penukaran yang pernah Anda lakukan di perangkat lain, misalnya, menggunakan file kunci cadangan yang terkait dengan penukaran tersebut.



![refund](assets/fr/11.webp)



Pada menu **History**, Anda dapat mengunduh riwayat yang lebih detail dari bursa yang terkait dengan kunci penyelamatan Anda dengan mengeklik tombol **Backup**.



![backup](assets/fr/12.webp)



⚠️ Mohon untuk tidak membocorkan file ini, karena file ini berisi semua informasi yang terkait dengan transaksi Anda dan kunci cadangan yang terkait dengan transaksi ini.



Boltz menawarkan kepada Anda tingkat kerahasiaan yang tinggi berkat aksesnya melalui tautan `.onion` pada jaringan Tor. Jadikan pertukaran atom benar-benar anonim dengan memilih menu **Onion**, setelah mengaktifkan penjelajahan Tor pada peramban Anda.



![onion](assets/fr/13.webp)



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

Sekarang Anda sudah tidak asing lagi dengan Boltz, platform Exchange yang unik yang memungkinkan interoperabilitas antara berbagai lapisan ekosistem Bitcoin.