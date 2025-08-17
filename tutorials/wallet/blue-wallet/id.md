---
name: Blue Wallet

description: Portofolio Bitcoin yang Sangat Sederhana dan Kuat
---
![cover](assets/cover.webp)



Memulai pakai Bitcoin sering keliatan kayak tantangan besar, apalagi buat orang yang masih skeptis soal gampang nggaknya dipakai. Karena itu, penting banget nemuin alat yang pas biar Bitcoin makin mudah dipakai, bukan cuma jadi tempat nyimpen nilai, tapi juga bener-bener bisa dipakai sebagai alat tukar.



Dalam tutorial ini kita akan melihat Blue Wallet, Bitcoin Wallet yang sederhana namun sangat efektif yang memungkinkanmu untuk mengelola bitcoin secara pribadi dan juga untuk membuat koperasi manajemen berdasarkan [Multisig] (https://planb.network/resources/glossary/multisig) (jangan khawatir, kita akan kembali ke sana).



![Vidéo tutoriel Blue Wallet](https://www.youtube.com/watch?v=UCAtFgkdJtM)



## Memulai dengan Blue Wallet



BlueWallet itu open-source, Bitcoin wallet self-custody yang bikin kamu bisa ngendaliin sendiri bitcoinnya. Aplikasi ini tersedia di Android maupun iOS. Di tutorial ini aku bakal bahas versi Android, tapi semua langkahnya juga berlaku buat iOS.



![download](assets/fr/01.webp)



⚠️ Pastikan kamu download aplikasi BlueWallet dari platform resmi biar terjamin keasliannya dan bitcoin kamu tetap aman dari kebocoran atau peretasan.



Setelah aplikasi terpasang, kamu bisa bikin wallet baru dan nyimpen 12 kata pemulihan, atau impor Bitcoin wallet yang udah ada. Pastikan kamu bikin cadangan kata kunci dengan benar supaya nggak kehilangan akses ke bitcoin kamu.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Dengan BlueWallet, kamu bisa bikin portofolio Bitcoin yang terpisah dan fokus. Misalnya, satu wallet khusus buat tabungan dan satu lagi buat pengeluaran harian, semuanya tetap ada dalam satu aplikasi yang sama.



![home](assets/fr/02.webp)



## Jenis portofolio



Dalam Blue Wallet, kamu akan menemukan dua tipe portofolio Bitcoin asli.



### Portofolio Bitcoin



Jika kamu terbiasa dengan portofolio Bitcoin lainnya seperti Phoenix atau Aqua, kamu nggak akan merasa asing dengan portofolio Interface dengan portofolio Bitcoin Blue Wallet.



https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf


https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

Bitcoin Wallet berwarna biru mewakili Wallet standar dalam ekosistem Bitcoin. Kamu dapat membelanjakan bitcoin selama kamu memiliki kata pemulihan yang akan memberikan tanda tangan yang valid di jaringan untuk mengautentikasi bahwa kamu memiliki bitcoin.



Untuk membuat portofolio Bitcoin, klik tombol **Tambah sekarang**, masukkan nama portofolio kamu dan pilih tipe Bitcoin.



![bitcoin-wallet](assets/fr/03.webp)



Ketika kamu mengklik pratinjau Bitcoin Wallet , kamu bakal dapat melihat riwayat transaksi, mengirim dan menerima bitcoin.



⚠️ Semua transaksi di Bitcoin Wallet berada di rantai utama protokol Bitcoin (Mainnet).





- Menerima bitcoin dengan Bitcoin Blue Wallet Wallet sangat intuitif. Di bagian bawah layar Anda, klik tombol **Terima**. Bagikan kode QR atau Bitcoin Address Anda kepada pengirim agar mereka dapat mengirimkan bitcoin ke kamu.



Kamu juga bisa mengonfigurasi jumlah yang telah ditentukan untuk menentukan jumlah Bitcoin yang ingin kamu terima.



![receive-bitcoin](assets/fr/04.webp)





- Pada tombol **Kirim**, kirimkan bitcoin ke Bitcoin Address, atur jumlah yang diinginkan dan validasi transaksi.



![send-bitcoin](assets/fr/05.webp)



Blue Wallet memungkinkan kamu mengonfigurasi parameter pengiriman Bitcoin sesuai keinginan.



Karena itu, kamu bisa pilih rasio biaya transaksi yang sesuai kalau pengin transaksi kamu cepat tervalidasi di Mempool dan masuk ke blok oleh para penambang. Tergantung rasio yang kamu pilih, penambang bakal memprioritaskan transaksi kamu lebih tinggi atau rendah. Pelajari lebih lanjut di tutorial Mempool Space.



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

![feerate](assets/fr/06.webp)





- Dengan Blue Wallet, kamu bisa menambahkan beberapa penerima ke satu pengiriman.



Saat kamu nambah Bitcoin Address penerima pertama, klik opsi Tambahkan Penerima, masukkan alamat Bitcoin, lalu atur jumlah yang mau dikirim ke penerima ini, dan seterusnya. BlueWallet bakal mengirim bitcoin ke beberapa penerima dalam satu aksi sekaligus.



![add-recipients](assets/fr/07.webp)



Kamu bisa menghapus satu atau semua penerima dengan mengeklik **Hapus Penerima** dan **Hapus Semua Penerima**.



![remove-recipient](assets/fr/08.webp)





- Biaya yang membengkak**: Apakah kamu pernah melakukan transaksi yang membutuhkan waktu lama untuk dikonfirmasi? Dengan mengaktifkan inflasi biaya, kamu dapat menambahkan biaya transaksi tambahan ke transaksi yang tertunda untuk mempercepat konfirmasinya.



![bumping](assets/fr/09.webp)



### Portofolio Multisig



Multisig (multi-tanda tangan) Wallet merupakan Wallet yang dibuat dari pengelompokan sejumlah (minimal 2) dompet Bitcoin. Pada jenis Wallet ini, tergantung pada konfigurasi dan metode yang dipilih, membelanjakan bitcoin menjadi sebuah tindakan kolektif dan kooperatif.



Di BlueWallet, kamu bisa bikin portofolio multi-sig buat asosiasi, keluarga, atau perusahaan kamu. Di bagian ini, kita bakal bahas semua aspek dari jenis portofolio khusus ini.


Tambahkan portofolio baru dan pilih tipe **Multisig Vault** untuk membuat portofolio multi-sig.



![multisig-vault](assets/fr/10.webp)



Tentukan konfigurasi m-de-n di organisasi multi-tanda tangan Anda dengan mengklik **Pengaturan Brankas**.



⚠️ Dalam konfigurasi m-of-n, **m** menunjukkan jumlah minimum tanda tangan yang diperlukan untuk menyetujui transaksi dan **n** jumlah portofolio dalam organisasi.



Pastikan kamu tentuin jumlah minimum tanda tangan (m) buat sebagian besar organisasi kamu. Misalnya, konfigurasi multi-signature 2-dari-3 artinya dua wallet dalam organisasi harus tanda tangan dulu sebelum transaksi bisa dijalankan.



❗Menetapkan konfigurasi m-of-n di mana n sama dengan m itu berisiko besar. Kalau salah satu anggota kehilangan akses ke wallet, kamu bakal kehilangan kemampuan buat membelanjakan bitcoin di wallet itu.



Berikut ini beberapa contoh konfigurasi optimal untuk memastikan keamanan dan aksesibilitas ke bitcoin:





- multi-signature 2-de-3.





- 5-de-7 multi-signature.



![vault-settings](assets/fr/11.webp)



Ikuti praktik terbaik dengan memilih format P2WSH.



❗ **[P2WSH] (https://planb.network/resources/glossary/p2wsh) atau Pay to Witness Script Hash** Ini adalah metode penguncian yang mengamankan bitcoin keluar (output) dari transaksi kamu ke hash dari skrip khusus yang dibuat oleh BlueWallet. Keuntungan utama dari metode ini adalah mengurangi ukuran data transaksi dan secara otomatis bikin biaya transaksi lebih rendah.



Bikin atau impor setiap portofolio **n** sesuai konfigurasi kamu. Di tutorial ini, kita bakal pakai konfigurasi multi-signature 2-dari-3. Pastikan kamu nyimpen kata pemulihan untuk tiap portofolio satu per satu.



![vault-keys](assets/fr/12.webp)





- Menerima bitcoin



Pada halaman Multisig Wallet, kamu akan menemukan riwayat transaksi dan tombol Terima dan Kirim.



Menerima bitcoin dalam Wallet multi-tanda tangan adalah proses yang sama seperti ketika kamu menggunakan Bitcoin Wallet standar.





- Kirim bitcoin** :



Dengan mengelola wallet multi-signature, membelanjakan bitcoin jadi tindakan gabungan, baik dengan orang lain atau dengan wallet kedua milik kamu sendiri. Tanda tangan tunggal dari wallet kamu nggak cukup lagi. Ini nambah lapisan keamanan buat bitcoin kamu, karena orang jahat nggak bakal bisa membelanjakannya meskipun dia punya salah satu private key kamu.



Seperti portofolio Bitcoin standar Blue Wallet, kamu bisa menentukan beberapa penerima dalam opsi **Tambahkan penerima**.



Saat memvalidasi transaksi kamu, kamu memerlukan tanda tangan kedua untuk menyetujui pembelanjaan bitcoin. Ingat, kita menggunakan konfigurasi multi-tanda tangan 2-de-3.



Penandatangan Wallet kedua, jika dia juga seorang pengguna, dapat menandatangani transaksi meskipun dia tidak terhubung ke Internet (tidak ada Wi-Fi, tidak ada data seluler) dengan memindai kode QR dari [transaksi yang ditandatangani sebagian] (https://planb.network/resources/glossary/psbt) yang baru saja Anda buat.



![mutisig-send](assets/fr/13.webp)





- Melangkah lebih jauh dengan portofolio Multi signature**:



Pada Interface dari Wallet multi-tanda tangan kamu, klik tombol **Kelola tombol**.



Dengan melupakan salah satu kata pemulihan dari salah satu portofolio penandatangan (**Lupakan seed ini...**), kamu memberi tahu Blue Wallet untuk menghapus cadangan kata-kata ini dari memorinya. Oleh karena itu, kamu akan membuat cadangan eksternal.



![revoke-key](assets/fr/14.webp)



Dengan melakukan tindakan ini, kamu hanya menyimpan kunci publik yang terkait dengan kata pemulihan ini.



⚠️ Dengan hanya menyimpan kunci publik (XPUB), kamu dapat menambahkan tingkat keamanan ekstra pada konfigurasi 2-dari-3 tanda tangan ganda. Memang, menyimpan semua kata pemulihan di satu tempat saat ponsel diserang bisa merugikan. Penyerang yang memiliki akses ke hanya satu **VAULT** (kata kunci) yang Anda gunakan untuk menandatangani transaksi, tidak akan dapat mencuri bitcoin (minimal 02 tanda tangan yang dibutuhkan) karena kunci publik tidak dapat digunakan untuk menandatangani transaksi.



## Lebih banyak opsi dengan Blue Wallet



### Meningkatkan keamanan akses portofolio



Dalam Pengaturan, opsi **Keamanan** memungkinkanmu menentukan penggunaan sidik jari untuk melakukan transaksi, mengekspor, atau menghapus Wallet. Hal ini akan mengautentikasi orang yang menggunakan smartphonemu.



![biometry](assets/fr/15.webp)



## Aktifkan Lightning Network



Lightning Network tidak lagi didukung secara asli dalam aplikasi Blue Wallet.



Dalam Pengaturan > **Pengaturan Lightning**, kamu dapat secara manual mengaitkan Lightning Wallet ketika menjalankan node Lightning Network Daemon (LND). Instal Hub LND, lalu kaitkan Wallet dengan memasukkan tautan yang dihasilkan oleh Hub.



![ln](assets/fr/16.webp)



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

https://planb.network/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Sekarang kamu udah selesai tur BlueWallet, siap pakai Bitcoin dengan gampang dan powerful. Aku saranin kamu ambil langkah berikutnya, cari tahu gimana cara nerima pembayaran Bitcoin di toko kamu, berkat kekuatan Lightning.



https://planb.network/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06
