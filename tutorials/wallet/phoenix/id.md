---
name: Phoenix
description: Menginstal dan menggunakan Phoenix Wallet
---
![cover](assets/cover.webp)

Phoenix adalah dompet sekaligus node Lightning non-kustodian yang dikembangkan oleh ACINQ, perusahaan asal Prancis yang fokus pada solusi perangkat lunak berbasis Lightning. Berbeda dengan dompet Lightning kustodian seperti Wallet of Satoshi, di mana bitcoin kamu dipegang pihak ketiga, Phoenix bikin kamu bisa pegang kendali penuh atas kunci pribadimu sendiri.

Phoenix bekerja sebagai node Lightning asli yang langsung tertanam di ponselmu, dan secara otomatis membuka saluran dengan node Lightning ACINQ. Aplikasi ini dibangun di atas Lightning-KMP, sebuah implementasi lintas platform Lightning Network berbasis Kotlin yang dioptimalkan untuk dompet seluler. Nggak seperti solusi node Lightning lain, Phoenix jauh lebih simpel dalam pengelolaannya. Kamu nggak perlu ribet buka atau tutup saluran, jalankan node Bitcoin, atau ngurus likuiditas di Lightning Network. Semua urusan teknis itu ditangani Phoenix di belakang layar.

Aplikasi ini ngasih kombinasi antara kemudahan dompet Lightning seluler dengan keamanan dan kedaulatan node Lightning pribadimu sendiri. Phoenix bikin kamu bisa pakai Lightning Network dengan aman, efisien, dan mandiri, sambil tetap dapet pengalaman pengguna yang mulus dan gampang dipahami.

Sebagai gantinya, ada biaya tertentu yang berlaku:


- Setiap kali kirim lewat Lightning, ada biaya 0,4% dari jumlah transaksi ditambah 4 sats.
- Kalau butuh "uang muka" untuk bisa menerima lewat Lightning, akan dikenakan biaya 1% dari jumlah yang diterima.
- Setiap kali buka saluran baru, ada biaya 1000 sats.

Menurutku, Phoenix adalah solusi tengah yang keren banget antara dompet Lightning kustodian dan pengelolaan manual node Lightning. Aplikasi ini cocok dipakai baik oleh pemula maupun pengguna tingkat lanjut yang nggak mau ribet ngurus detail teknis LND atau Core Lightning sendiri. Yuk, kita pelajari bareng gimana cara pakainya!

![Image](assets/fr/01.webp)

## Instal aplikasi

Buka toko aplikasimu dan instal Phoenix :


- Di [Google Play Store](https://play.google.com/store/apps/details?id=fr.acinq.phoenix.mainnet);
- Di [App Store](https://apps.apple.com/fr/app/phoenix-wallet/id1544097028?l=en-GB).

![Image](assets/fr/02.webp)

Kamu juga bisa menginstal aplikasi [dengan file apk di repositori GitHub mereka] (https://github.com/ACINQ/phoenix/releases).

![Image](assets/fr/03.webp)

## Pembuatan portofolio

Setelah aplikasi dimulai, klik tombol "*Next*" untuk melewatkan presentasi, kemudian "*Start*".

![Image](assets/fr/04.webp)

Pilih "*Buat dompet baru*".

![Image](assets/fr/05.webp)

Dan itu saja, dompet dan node Lightning sekarang sudah dibuat.

![Image](assets/fr/06.webp)

## Menyimpan frasa mnemonik

Sebelum mulai, kita perlu menyimpan seed phrase atau frasa pemulihan 12 kata. Frasa ini ngasih akses penuh dan tanpa batas ke semua bitcoin kamu. Siapa pun yang punya seed phrase ini bisa mencuri dana kamu, bahkan tanpa harus pegang ponselmu.

Seed phrase 12 kata ini juga jadi kunci buat balikin akses ke bitcoin kalau ponselmu hilang, dicuri, atau rusak. Karena itu, penting banget buat nyimpennya dengan hati-hati di tempat yang aman.

Kamu bisa tulis di kertas atau, kalau mau lebih aman lagi, ukir di baja tahan karat supaya tahan dari kebakaran, banjir, atau kerusakan fisik lainnya. Media penyimpanan seed phrase ini tergantung strategi keamananmu, tapi kalau kamu pakai Phoenix cuma buat dompet sehari-hari dengan jumlah kecil, kertas aja udah cukup.

Kalau mau tau lebih detail soal cara nyimpen dan ngatur seed phrase dengan benar, aku sangat nyaranin kamu ikutin tutorial lain, apalagi kalau kamu masih pemula:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Klik pada pesan yang ditampilkan di bagian atas interface "*Save your wallet...*".

![Image](assets/fr/07.webp)

Kemudian klik "*Save my wallet*".

![Image](assets/fr/08.webp)

Kemudian klik "*Lihat kunci saya*" dan simpan frasa mnemonikmu pada media fisik.

![Image](assets/fr/09.webp)

Centang dua kotak di bagian bawah interface untuk mengonfirmasi bahwa pencadangan telah berhasil diselesaikan.

![Image](assets/fr/10.webp)

## Penyiapan aplikasi

Sebelum melakukan transaksi pertama, kamu bisa atur pengaturan dengan ngeklik ikon roda gigi di pojok kiri bawah tampilan aplikasi.

![Image](assets/fr/11.webp)

Di menu Display, kamu bisa pilih tema aplikasi, denominasi yang dipakai buat bitcoin, dan mata uang fiat lokalmu.

![Image](assets/fr/12.webp)

Di menu "*Pilihan Pembayaran*", kamu bakal nemuin berbagai pengaturan lanjutan buat pembayaran Lightning. Kamu bisa biarin aja pakai pengaturan default.

![Image](assets/fr/13.webp)

Di "*Manajemen saluran*", tetapkan biaya maksimum yang siap kamu bayar saat membuka saluran Lightning.

![Image](assets/fr/14.webp)

Di menu "*Access Control,*" aku sangat nyaranin kamu buat ngaktifin sistem autentikasi supaya akses ke aplikasi di ponselmu lebih aman. Ini bakal mencegah orang lain yang bisa buka ponselmu yang nggak terkunci buat masuk ke Phoenix dan nyuri bitcoin kamu.

![Image](assets/fr/15.webp)

Pada menu "*Electrum server*", jika kamu memiliki server Electrs, kamu bisa menghubungkannya untuk menyiarkan transaksimu.

![Image](assets/fr/16.webp)

Buat ningkatin privasi koneksimu, aktifin opsi koneksi lewat Tor di menu "*Tor.* Walaupun pakai Tor bisa bikin pembayaran agak sedikit lebih lambat dan butuh aplikasi Phoenix tetap kebuka di latar depan saat nerima, tapi fitur ini bakal ningkatin privasi kamu secara signifikan.

![Image](assets/fr/17.webp)

## Menerima bitcoin secara on-chain

Waktu pertama kali dipakai, kamu bisa isi dompet Phoenix dengan dana on-chain. Kamu juga bisa lakuin deposit pertama langsung lewat Lightning (lihat bagian berikutnya). Tapi di kedua cara itu, bakal ada biaya tambahan buat buka saluran pertamamu.

Klik pada tombol "*Terima*".

![Image](assets/fr/18.webp)

Geser kode QR ke kiri buat nampilin alamat penerimaan Bitcoin. Kirim jumlah yang mau kamu depositin ke alamat itu supaya masuk ke Phoenix.

![Image](assets/fr/19.webp)

Jumlah yang kamu terima lewat on-chain bakal pertama kali muncul sebagai tertunda di bawah saldo dompetmu. Dana baru bisa dipakai setelah dapet 3 konfirmasi.

![Image](assets/fr/20.webp)

Begitu dana udah masuk, Phoenix bakal otomatis buka saluran Lightning buat kamu. Setelah itu, kamu bisa langsung kirim dan nerima bitcoin lewat Lightning Network.

![Image](assets/fr/21.webp)

## Menerima bitcoin melalui Lightning

Untuk menerima satelit melalui Lightning Network, klik tombol "*Receive*".

![Image](assets/fr/22.webp)

Phoenix bakal bikin faktur Lightning. Kamu bisa scan faktur itu atau kirim ke orang yang mau transfer pembayaran ke kamu.

![Image](assets/fr/23.webp)

Dengan ngeklik tombol "*Edit*", kamu bisa nambahin deskripsi yang bakal keliatan sama si pengirim di faktur, dan juga nentuin jumlah pasti yang harus mereka kirim.

![Image](assets/fr/24.webp)

Faktur klasik yang tadi disebut cuma bisa dipakai sekali aja. Kalau mau opsi pembayaran yang bisa dipakai berulang kali, kamu bisa pakai kode QR yang bisa digunakan terus, yaitu penawaran **BOLT12.**

![Image](assets/fr/25.webp)

Begitu faktur atau penawaran BOLT12 dibayar, transaksinya bakal langsung muncul di dompet Lightning kamu.

![Image](assets/fr/26.webp)

## Kirim bitcoin melalui Lightning

Sekarang setelah kamu punya saldo sats di Phoenix, kamu udah siap buat ngelakuin pembayaran lewat Lightning Network. Mulai aja dengan ngeklik tombol Kirim.

![Image](assets/fr/27.webp)

Ada beberapa opsi yang bisa kamu pilih. Dengan ngeklik Pindai kode QR, kamu bisa scan faktur Lightning, penawaran BOLT12, atau bahkan alamat penerima buat pembayaran on-chain.

![Image](assets/fr/28.webp)

Kamu juga bisa masukin informasi itu secara manual lewat keyboard di kolom bagian atas tampilan, atau masukin alamat Lightning (BOLT12 atau LNURL). Selain itu, kamu bisa langsung tempel informasi dengan tombol "*Paste.*"
![Image](assets/fr/29.webp)

Di contoh ini, aku udah scan faktur sebesar 10.000 sat. Buat ngelakuin pembayaran, cukup klik Bayar.

![Image](assets/fr/30.webp)

Transaksi selesai.

![Image](assets/fr/31.webp)

Selamat, sekarang kamu udah tau cara ngatur dan pake Phoenix. Kalau kamu ngerasa tutorial ini bermanfaat, aku bakal seneng banget kalau kamu kasih jempol hijau di bawah. Jangan ragu juga buat share artikel ini di media sosialmu. Makasih banyak udah baca!

Kalau mau lanjut lebih jauh, coba deh lihat tutorial tentang Alby Hub, solusi inovatif dan gampang dipake buat ngejalanin node Lightning kamu sendiri:

https://planb.network/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Dan kalau kamu pengen ngerti lebih dalam soal cara kerja teknis Lightning Network, kamu bisa ikutin pelatihan gratis yang keren banget dari Fanis Michalakis di Plan ₿ Network:

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
