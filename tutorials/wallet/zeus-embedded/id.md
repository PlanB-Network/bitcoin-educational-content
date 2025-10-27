---
name: Zeus Embedded
description: Cara menggunakan Lightning Zeus Embedded Wallet
---
![cover-zeus-embedded](assets/cover.webp)

ZEUS pada awalnya adalah aplikasi seluler untuk manajemen jarak jauh dari node petir, memungkinkanmu untuk mengontrol node yang diinstal pada server jarak jauh

Tetapi aplikasi ini juga memiliki fitur "Node tertanam".

**Aspek aplikasi inilah yang akan kita jelajahi dalam tutorial ini. Hal ini memungkinkan siapa saja untuk memiliki node petir mereka sendiri di ponsel, tanpa perlu server khusus, dengan cara yang sama seperti ACINQ menawarkan petir Wallet yang luar biasa, Phoenix.

https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

Sebagai pengingat, Lightning adalah jaringan yang berjalan paralel dengan Bitcoin dan memungkinkan kamu menukar bitcoin tanpa harus melakukan transaksi on-chain secara langsung. Hasilnya, transaksi bisa berlangsung hampir seketika tanpa perlu menunggu sekitar 10 menit untuk memvalidasi satu blok. Ini sangat berguna saat kamu ingin membayar pedagang di dunia nyata. Selain itu, Lightning juga menawarkan tingkat privasi yang jauh lebih tinggi dibanding jaringan Bitcoin.

**Zeus "Integrated" ditujukan untuk para pengguna Bitcoin yang ingin memaksimalkan privasi dan otonomi mereka.

Singkatnya, ini adalah ponsel wallet impian para cypherpunk. Meskipun masih dalam tahap awal (versi alfa) dan masih ada beberapa bug, fiturnya sangat banyak, dan jelas akan menarik bagi para pemberani di antara kita yang menginginkan kontrol dan kebebasan maksimal.

Di sisi lain, menurutku, saat ini wallet ini belum cocok untuk pemula yang belum terbiasa dengan Bitcoin dan hanya ingin cara mudah untuk mengirim atau menerima satoshi. Meski begitu, hal ini bisa berubah nanti, karena fitur penitipan melalui protokol Cashu (Chaumian Ecash) sedang dikembangkan untuk memudahkan para pemula.


## Instal aplikasi

Kunjungi [situs web proyek] (https://zeusln.com/) untuk mengunduh aplikasi untuk OS ponsel cerdas kamu:

![image](assets/fr/01.webp)

![image](assets/fr/02.webp)

## Pembuatan portofolio

Setelah aplikasi dimulai, klik tombol "Quick Start" untuk mulai membuat Wallet.

![image](assets/fr/03.webp)

Serangkaian layar inisialisasi akan muncul. Tunggu sebentar, lalu biarkan beberapa menit sampai node tersinkronisasi 100% melalui Neutrino.

Proses ini mungkin memakan waktu beberapa menit. Sebagai catatan, Neutrino adalah cara bagi wallet seluler untuk mengakses data blockchain Bitcoin tanpa harus menjalankan full node.

![image](assets/fr/04.webp)

Setelah beberapa saat, kamu sudah siap untuk mulai menggunakan wallet.

![image](assets/fr/05.webp)

## Penyiapan aplikasi

Siap? Nggak juga, karena jelas para pengguna Zeus, sesuai dengan namanya, menavigasi wallet mereka dengan gaya dan penuh wibawa. Jadi, kita perlu mengganti avatarnya.

Klik avatar kamu di pojok kanan atas layar:

![image](assets/fr/06.webp)

Klik pada roda gigi, lalu pada tanda plus "+" :

![image](assets/fr/07.webp)

Pilih foto Zeus yang paling bagus untuk mewakili Wallet ini dan klik "PILIH GAMBAR" di bagian bawah layar, lalu kembali dengan mengklik tanda panah di kanan atas.

![image](assets/fr/08.webp)

Terakhir, beri nama panggilan untuk wallet kamu, lalu klik "SAVE Wallet CONFIG" supaya perubahan tersimpan. Setelah itu, klik panah kembali di pojok kiri atas untuk kembali ke layar beranda.

![image](assets/fr/09.webp)

Kali ini kita benar-benar bisa memulai.

![image](assets/fr/10.webp)

### Biometrik

Untuk melindungi akses ke wallet, kamu bisa menambahkan PIN atau kata sandi, dan juga mengaktifkan biometrik.

Untuk melakukannya, buka menu utama wallet dengan mengetuk tiga garis horizontal di pojok kiri atas.

![image](assets/fr/11.webp)

Pilih "Pengaturan", lalu "Keamanan", dan terakhir "Atur/Ganti PIN".

![image](assets/fr/12.webp)

Buat PIN kamu, konfirmasikan, lalu aktifkan biometrik dengan menekan tombol "Biometrik" yang tersedia. Setelah itu, kembali ke menu utama dengan mengetuk panah di pojok kiri atas.

![image](assets/fr/13.webp)


### Simpan frasa Mnemonic

Setelah kembali ke menu utama, klik "Cadangkan Wallet", lalu baca peringatan yang menjelaskan bahwa kehilangan 24 kata yang akan kamu terima sama artinya dengan kehilangan akses ke dana kamu, dan siapa pun yang memiliki kata-kata ini selain kamu bisa mengakses dana tersebut. Jangan pernah memberikannya kepada siapa pun.

Pilih "SAYA MENGERTI" di bagian bawah layar. Lalu klik setiap kata dari 24 kata tersebut untuk menampilkannya, dan catat dengan hati-hati.

Kamu bisa menuliskannya di atas kertas, atau untuk keamanan tambahan, mengukirnya di baja tahan karat agar terlindungi dari kebakaran, banjir, atau kerusakan lainnya. Pilihan media untuk menyimpan seedphrase tergantung strategi keamanan kamu, tetapi jika menggunakan Zeus sebagai portofolio pengeluaran dengan jumlah sedang, kertas sudah cukup.

Untuk informasi lebih lengkap tentang cara menyimpan dan mengelola seedphrase dengan benar, aku sangat menyarankan mengikuti tutorial lain, terutama jika kamu masih pemula.

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![image](assets/fr/14.webp)

Setelah selesai, klik "SAYA SUDAH MENCADANG 24 KATA SAYA" di bagian bawah layar, lalu kita akan kembali ke layar beranda, siap untuk menerima bitcoin pertama kamu.

## Opsi 1 - Menerima bitcoin On-Chain & membuka saluran Lightning

**Zeus Embedded** terutama dirancang sebagai simpul petir tertanam, tetapi juga dapat digunakan sebagai Wallet On-Chain.

Untuk menerima bitcoin On-Chain, klik tombol "On-Chain" lalu "Terima".

Terakhir, pindai kode QR atau salin Bitcoin Address untuk menyetor dana.

![image](assets/fr/15.webp)

Setelah dana dikonfirmasi dan dikreditkan ke wallet kamu, kamu bisa menggunakannya untuk membuka Lightning channel. Saluran Lightning ini adalah pintu masuk ke Lightning Network, yang memungkinkan kamu menukar bitcoin dengan cara yang lebih cepat dan lebih privat.

- Untuk melakukannya, klik "PINDAHKAN DANA On-Chain KE LIGHTNING"

Di layar berikutnya, kamu akan diminta membuka saluran bekerja sama dengan "Olympus by Zeus", LSP (Lightning Service Provider) yang direkomendasikan oleh wallet.

Untuk tutorial ini, kita akan memilih opsi ini demi kemudahan, meski sebenarnya kamu bisa membuka saluran dengan node mana pun di jaringan.

Bahkan, memungkinkan membuka beberapa saluran dalam satu transaksi dengan memilih "OPEN ADDITIONAL CHANNEL", tapi kita akan membahas itu di versi "lanjutan" dari tutorial Zeus Embedded.

- Selanjutnya, pilih jumlah yang ingin kamu dedikasikan untuk saluran ini. Dalam contoh kita, semua dana on-chain akan digunakan, jadi aktifkan tombol "Gunakan semua dana yang memungkinkan".

- Terakhir, klik tombol "OPEN CHANNEL" di bagian bawah layar.
  
![image](assets/fr/16.webp)

Dalam hitungan detik, saluran sudah terbentuk dan kita siap melakukan transaksi Lightning pertama. Di layar beranda, kamu akan melihat ikon jam kecil di samping saldo wallet. Ini menandakan bahwa kita masih harus menunggu 3 konfirmasi on-chain sebelum saluran benar-benar aktif.

![image](assets/fr/17.webp)

Setelah 3 kali konfirmasi, kami melihat bahwa saldo kami sekarang dikreditkan ke sisipan Lightning.

![image](assets/fr/18.webp)

Hal kecil yang perlu diperhatikan: ketika kita membuka menu di bagian bawah layar untuk mengecek status saluran Lightning, akan terlihat bahwa sebagian kecil saldo tidak bisa dibelanjakan. Misalnya, kita hanya bisa menggunakan 208.253 satoshi, bukan 210.370 satoshi yang ada. Ini normal karena memang bagian ini khusus untuk protokol Lightning.

Perlu dicatat juga, mitra kita, Olympus, berhak menutup saluran atas kebijakannya sendiri, misalnya jika saluran tidak digunakan. Untuk memastikan saluran tetap aktif, kita harus membayar LSP (Lightning Service Provider), seperti yang akan kita bahas di paragraf berikutnya melalui cara kedua membuka saluran.


## Kirim bitcoin melalui Lightning

Sekarang kita sudah menyiapkan saluran kita dan menjalankannya, mari kita lihat bagaimana kita dapat menggunakannya untuk membayar petir Invoice (Invoice).

Untuk melakukan ini, klik tombol "Lightning", kemudian "Send".

![image](assets/fr/19.webp)

Pada layar berikutnya, salin Invoice kamu ke dalam kolom khusus, atau pindai dengan mengeklik ikon di kanan atas. Terakhir, geser tombol "Geser untuk Membayar" ke kanan untuk membayar.

![image](assets/fr/20.webp)

Tunggu beberapa detik dan Invoice akan meluncur, dan satoshi kamu akan melaju dengan kecepatan cahaya.

![image](assets/fr/21.webp)

Zeus juga memungkinkan kamu menambahkan catatan untuk mendenominasi pembayaran, atau melihat rute yang ditempuh satoshi sebelum sampai ke tujuan (beserta biaya yang dikenakan oleh semua node perantara). Inilah jenis fungsionalitas yang membuat kami menyukai wallet ini.

![image](assets/fr/22.webp)


Perhatikan bahwa tidak seperti Wallet seperti [Phoenix]([Plan ₿ Network - Phoenix](https://planb.network/fr/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf)), Dengan Zeus, rute dihitung secara lokal dan tidak didelegasikan ke pihak ketiga (ACINQ dalam kasus Phoenix). Jadi, hanya kamu yang mengetahui penerima pembayaran. Memang ada sedikit pengorbanan efisiensi (pembayaran bisa memakan waktu lebih lama), tapi keuntungan privasinya jauh lebih besar.

Dengan mengetuk panah kecil di bagian bawah layar beranda, kamu juga bisa melihat riwayat pembayaran. Di sini terlihat dalam warna hijau, 212.121 sats diterima secara on-chain, lalu warna merah menunjukkan 211.756 sats yang digunakan untuk membuka saluran, dan 121.212 sats digunakan untuk membayar Lightning invoice.

![image](assets/fr/23.webp)


## Opsi 2 - Menerima bitcoin secara langsung di Lightning

Daripada membuka saluran secara manual seperti yang baru saja kita lakukan, kamu bisa menerima dana langsung melalui Lightning, bahkan tanpa saluran yang sudah ada sebelumnya, dengan menggunakan Olympus, Zeus LSP.

- Untuk melakukannya, klik tombol "Lightning" di layar beranda, lalu pilih "Receive".
- Setelah itu, masukkan jumlah yang ingin kamu terima di kotak "Jumlah" dan tekan tombol "BUAT Invoice" di bagian bawah layar.

![image](assets/fr/24.webp)

Layar berikutnya menampilkan invoice yang harus dibayar untuk menerima satoshi. Kita diberitahu bahwa LSP akan menahan 10.000 sats jika pembayaran dilakukan melalui Lightning. Nanti kita akan lihat bagaimana biaya ini dibenarkan untuk membuka saluran.

Bayar invoice atau minta orang lain untuk membayarnya, dan saluran akan terbuka secara otomatis, namun dikurangi 10.000 sats sesuai kesepakatan.

![image](assets/fr/25.webp)

Sekarang kita memiliki dua saluran Lightning, yang statusnya bisa diperiksa dengan mengetuk tombol yang ditunjukkan panah putih di bagian bawah layar beranda.

Kamu bisa melihat bahwa, berbeda dengan saluran yang dibuka dari dana on-chain, saluran yang dibuka langsung melalui Lightning tidak menampilkan peringatan.

Karena kamu telah membayar untuk menyiapkan saluran ini, Lightning Service Provider (LSP) berjanji memelihara saluran selama 3 bulan dan menyediakan "likuiditas masuk" untukmu. Pada saluran paling bawah, terlihat kapasitas penerimaan sebesar 96.383 sats. Artinya, LSP mengikat modal agar kamu bisa menerima pembayaran langsung begitu saluran dibuka.

Jadi, 10.000 sats yang dibayarkan mencakup biaya pembukaan saluran (transaksi on-chain), jaminan pemeliharaan saluran selama 3 bulan, dan penguncian modal.

![image](assets/fr/26.webp)

Selamat, sekarang kamu siap menggunakan Zeus Embedded, wallet seluler Lightning dengan fitur paling canggih di pasaran.

Untuk mempelajari lebih lanjut tentang cara kerja teknis Lightning Network, kamu bisa mengikuti pelatihan Plan ₿ Network gratis yang luar biasa dari Fanis Michalakis:

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
