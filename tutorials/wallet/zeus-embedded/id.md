---
name: Zeus Embedded
description: Cara menggunakan Lightning Zeus Embedded Wallet
---
![cover-zeus-embedded](assets/cover.webp)



ZEUS pada awalnya adalah aplikasi seluler untuk manajemen jarak jauh dari node Lightning, memungkinkan kamu mengontrol node yang diinstal di server jarak jauh.


Tetapi aplikasi ini juga memiliki fitur "Node tertanam".


**Aspek aplikasi inilah yang akan kita jelajahi dalam tutorial ini.** Fitur ini memungkinkan siapa pun memiliki node Lightning sendiri langsung di ponsel, tanpa perlu server khusus, dengan cara yang sama seperti ACINQ menawarkan Lightning Wallet yang luar biasa, Phoenix.


https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf


**Sebagai pengingat, Lightning adalah jaringan yang beroperasi secara paralel dengan Bitcoin, yang memungkinkan bitcoin ditransaksikan tanpa harus melakukan transaksi on-chain secara sistematis. Hasilnya adalah transaksi yang hampir seketika, tanpa perlu menunggu 10 menit untuk memvalidasi sebuah blok. Hal ini sangat berguna saat membayar pedagang di dunia fisik. Selain itu, Lightning menawarkan tingkat privasi yang sangat tinggi yang tidak dimiliki oleh jaringan Bitcoin.**


**Zeus "Integrated"** ditujukan bagi pengguna Bitcoin yang ingin memaksimalkan privasi dan otonomi mereka.


Singkatnya, ini adalah mobile Wallet impian para cypherpunk. Meskipun masih dalam tahap awal, yaitu versi alfa, dan masih terdapat beberapa bug, fitur-fiturnya sudah sangat banyak, dan tidak diragukan lagi ini akan menyenangkan para pemberani di antara kita yang menginginkan kontrol dan pilihan maksimum.


Di sisi lain, menurutku saat ini fitur ini belum cocok untuk pemula yang belum terbiasa dengan Bitcoin dan hanya ingin cara sederhana untuk mengirim atau menerima satoshi. Namun, hal ini bisa saja berubah di masa mendatang, karena fitur kustodial melalui protokol Cashu, yaitu Chaumian Ecash, sedang diimplementasikan untuk para pemula...



## Instal aplikasi



Kunjungi [situs web proyek](https://zeusln.com/) untuk mengunduh aplikasi untuk OS ponsel cerdas Anda:



![image](assets/fr/01.webp)



![image](assets/fr/02.webp)



## Pembuatan portofolio



Setelah aplikasi dimulai, klik tombol "Quick Start" untuk mulai membuat Wallet.



![image](assets/fr/03.webp)





Serangkaian layar inisialisasi kemudian akan muncul. Tunggu beberapa saat, lalu biarkan beberapa menit sampai node tersinkronisasi 100% melalui Neutrino.


Proses ini bisa memakan waktu beberapa menit. Sebagai informasi, Neutrino adalah cara bagi wallet seluler untuk mengakses informasi blockchain Bitcoin tanpa perlu menjalankan full node.



![image](assets/fr/04.webp)





Setelah beberapa saat, kamu siap untuk pergi.



![image](assets/fr/05.webp)




## Penyiapan aplikasi



Tentu saja belum, karena sudah jelas bahwa pengguna Zeus, sesuai namanya, menavigasi Wallet-nya dengan penuh kelas dan gaya. Jadi kita harus mengganti avatarnya.


Klik avatar kamu di sudut kanan atas layar:



![image](assets/fr/06.webp)





Klik pada roda gigi, lalu pada tanda plus "+" :



![image](assets/fr/07.webp)





Pilih foto Zeus yang paling indah untuk mewakili Wallet ini dan klik "PILIH GAMBAR" di bagian bawah layar, lalu kembali dengan mengklik tanda panah di kanan atas.



![image](assets/fr/08.webp)





Terakhir, berikan nama panggilan pada Wallet kamu dan klik "SAVE Wallet CONFIG" agar perubahan dapat diterapkan. Terakhir, klik panah belakang di sudut kiri atas untuk kembali ke layar beranda.



![image](assets/fr/09.webp)





Kali ini kita benar-benar bisa memulai.



![image](assets/fr/10.webp)



### Biometrik



Untuk melindungi akses ke Wallet, kamu dapat menambahkan PIN/kata sandi dan mengaktifkan biometrik.



Untuk melakukan ini, buka menu utama Wallet dengan mengeklik garis horizontal di kiri atas.



![image](assets/fr/11.webp)





Pilih "Pengaturan", lalu "Keamanan", dan terakhir "Atur/Ganti PIN".



![image](assets/fr/12.webp)





Buat PIN kamu, konfirmasikan, dan aktifkan biometrik dengan menekan tombol "Biometrik" yang sesuai.  Kembali ke menu utama, dengan menggunakan tanda panah di kiri atas.



![image](assets/fr/13.webp)




### Simpan seedphrase


Setelah kamu kembali ke menu utama, klik "Cadangkan Wallet", lalu baca teks peringatan yang menjelaskan bahwa kehilangan 24 kata yang akan kamu terima sama artinya dengan kehilangan akses ke dana kamu, dan siapa pun yang memiliki kata-kata tersebut selain kamu bisa mengakses dana kamu. Jangan pernah memberikannya kepada siapa pun.


Pilih "SAYA MENGERTI" di bagian bawah layar. Lalu klik masing-masing dari 24 kata untuk menampilkannya, dan catat dengan cermat.


Kamu bisa menuliskannya di atas kertas, atau untuk keamanan tambahan, mengukirnya di atas baja tahan karat agar terlindung dari kebakaran, banjir, atau keruntuhan. Pilihan media untuk seedphrase kamu akan bergantung pada strategi keamananmu, tetapi jika kamu menggunakan Zeus sebagai wallet pengeluaran dengan jumlah sedang, kertas sudah cukup.


Untuk informasi lebih lanjut tentang cara yang tepat menyimpan dan mengelola seedphrase kamu, aku sangat merekomendasikan mengikuti tutorial lainnya, terutama jika kamu seorang pemula:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![image](assets/fr/14.webp)



Setelah selesai, klik "SAYA SUDAH MENCADANGKAN 24 KATA SAYA" di bagian bawah layar, dan kita akan kembali ke layar beranda, siap menerima bitcoin pertama kita.


## Opsi 1 - Menerima bitcoin on-chain & membuka channel Lightning


**Zeus Embedded** pada dasarnya dirancang sebagai node Lightning tertanam, tetapi juga bisa digunakan sebagai wallet on-chain.


Untuk menerima bitcoin on-chain, klik tombol "On-Chain" lalu "Terima".


Terakhir, pindai kode QR atau salin Bitcoin address untuk menyetor dana.


![image](assets/fr/15.webp)





Setelah dana dikonfirmasi dan masuk ke wallet kamu, kamu bisa menggunakannya untuk membuka **Lightning channel**. Channel Lightning ini adalah gerbang kamu ke Lightning Network, yang memungkinkan kamu melakukan exchange bitcoin dengan cara yang lebih privat dan cepat.


- Untuk melakukannya, klik "PINDAHKAN DANA On-Chain KE LIGHTNING"


Pada layar berikutnya, kamu akan diminta membuka channel dengan **"Olympus by Zeus"**, yaitu LSP, Lightning Service Provider, yang direkomendasikan oleh wallet.


Untuk tutorial ini, kita akan memilih opsi tersebut demi kemudahan, tetapi kamu juga bisa membuka channel dengan node mana pun di jaringan.


Bahkan, kamu bisa membuka beberapa channel dalam satu transaksi dengan memilih "OPEN ADDITIONAL CHANNEL". *Tetapi kita akan membahasnya dalam versi "lanjutan" dari tutorial* **Zeus Embedded**.


- Selanjutnya, pilih jumlah yang ingin kamu alokasikan untuk channel ini. Dalam contoh kita, semua dana on-chain akan digunakan, jadi kita aktifkan tombol "Gunakan semua dana yang memungkinkan".


- Terakhir, tekan tombol "OPEN CHANNEL" di bagian bawah layar.



![image](assets/fr/16.webp)





Dalam hitungan detik, channel sudah terbentuk dan kita siap melakukan transaksi Lightning pertama. Di layar beranda, kamu bisa melihat ikon jam kecil di sebelah saldo wallet. Ini karena kita masih harus menunggu 3 konfirmasi on-chain sebelum channel benar-benar bisa digunakan.


![image](assets/fr/17.webp)





Setelah 3 kali konfirmasi, kami melihat bahwa saldo kami sekarang dikreditkan ke sisipan Lightning.



![image](assets/fr/18.webp)



Hal kecil yang perlu diperhatikan: saat kamu mengklik menu di bagian bawah layar untuk melihat status channel Lightning, kamu akan melihat bahwa sebagian kecil saldo tidak tersedia untuk dibelanjakan. Kamu hanya bisa membelanjakan 208253 satoshi, bukan 210370 satoshi yang kamu miliki. Ini normal dan memang bagian dari mekanisme protokol Lightning.


Terakhir, perlu dicatat bahwa mitra kita, Olympus, berhak menutup channel atas kebijakannya sendiri jika channel tersebut tidak digunakan, misalnya. Untuk memastikan channel tetap dipertahankan, kita harus membayar LSP, Lightning Service Provider, seperti yang akan kita lihat di paragraf berikutnya melalui metode kedua untuk membuka channel.



## Kirim bitcoin melalui Lightning



Sekarang kita sudah menyiapkan saluran kita dan menjalankannya, mari kita lihat bagaimana kita dapat menggunakannya untuk membayar petir Invoice (Invoice).



Untuk melakukan ini, klik tombol "Lightning", kemudian "Send".



![image](assets/fr/19.webp)





Pada layar berikutnya, salin Invoice kamu ke dalam kolom khusus, atau pindai dengan mengeklik ikon di kanan atas. Terakhir, geser tombol "Geser untuk Membayar" ke kanan untuk membayar.



![image](assets/fr/20.webp)






Tunggu beberapa detik dan Invoice akan meluncur, dan satoshi kamu akan melaju dengan kecepatan cahaya.



![image](assets/fr/21.webp)





Zeus kemudian memungkinkan kamu menambahkan catatan untuk memberi keterangan pada pembayaranmu, atau melihat rute yang ditempuh satoshi sebelum mencapai tujuan, termasuk biaya yang dikenakan oleh setiap node perantara. Inilah jenis fungsionalitas yang kita sukai dari wallet seperti ini.


![image](assets/fr/22.webp)



Perhatikan bahwa tidak seperti Wallet seperti [Phoenix]([Plan ₿ Academy - Phoenix](https://planb.academy/fr/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf)), dengan Zeus rute dihitung secara lokal dan tidak didelegasikan ke pihak ketiga (ACINQ dalam kasus Phoenix). Jadi, kamu adalah satu-satunya yang mengetahui penerima pembayaran. Kita memang sedikit kehilangan efisiensi, karena pembayaran membutuhkan waktu lebih lama untuk selesai, tetapi sebagai gantinya kita mendapat peningkatan privasi yang signifikan.


Dengan mengklik panah kecil di bagian bawah layar beranda, kamu juga bisa melihat riwayat pembayaran. Di sini terlihat dalam warna hijau 212.121 sats yang diterima secara on-chain, lalu dalam warna merah 211.756 sats yang digunakan untuk membuka channel, kemudian 121.212 satoshi yang dipakai untuk membayar Lightning invoice.


![image](assets/fr/23.webp)





## Opsi 2 - Menerima bitcoin secara langsung di Lightning



Alih-alih membuka channel secara manual seperti yang baru saja kita lihat, kamu juga bisa menerima dana langsung melalui Lightning, bahkan tanpa channel yang sudah ada sebelumnya, dengan menggunakan Olympus, LSP milik Zeus.


- Untuk melakukannya, klik tombol "Lightning" di layar beranda, lalu pilih "Receive".
- Kemudian masukkan jumlah yang ingin kamu terima di kolom "Jumlah" dan tekan tombol "BUAT Invoice" di bagian bawah layar.


![image](assets/fr/24.webp)





Layar berikutnya menampilkan Lightning invoice yang harus dibayar agar kamu bisa menerima satoshi. Kamu akan diberi tahu bahwa LSP akan menahan 10.000 sats jika pembayaran dilakukan melalui Lightning. Nanti kita akan melihat bagaimana biaya pembukaan channel ini dijustifikasi.


Bayar invoice tersebut atau minta orang lain membayarnya, dan channel akan terbuka secara otomatis, dengan potongan 10.000 sats sesuai ketentuan.


![image](assets/fr/25.webp)





Sekarang kita berada di depan 2 channel Lightning, yang statusnya bisa kamu periksa dengan menekan tombol yang ditunjukkan oleh panah putih di bagian bawah layar beranda.


Kita bisa melihat bahwa, berbeda dengan channel yang dibuka dari saldo on-chain, channel yang dibuka langsung melalui Lightning tidak menampilkan peringatan.


Karena kamu sudah membayar untuk menyiapkan channel ini, Lightning Service Provider, LSP, berkomitmen untuk memeliharanya selama 3 bulan, serta menyediakan "inbound liquidity" untuk kamu. Pada channel paling bawah, kamu bisa melihat bahwa kapasitas penerimaan adalah 96383 satoshi. Artinya, LSP telah mengunci modal agar kamu bisa langsung menerima pembayaran setelah channel dibuka.


Jadi, biaya 10.000 satoshi yang dibayarkan mencakup biaya pembukaan channel, yaitu transaksi Bitcoin on-chain, jaminan pemeliharaan channel selama 3 bulan, serta penguncian modal.


![image](assets/fr/26.webp)





Selamat, sekarang kamu sudah siap menggunakan Zeus Embedded, wallet Lightning seluler dengan fitur paling canggih yang ada saat ini.


Untuk memahami lebih dalam tentang cara kerja teknis Lightning Network, kamu bisa mengikuti pelatihan gratis luar biasa dari Fanis Michalakis di Plan ₿ Academy:

https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
