---
name: Zeus Embedded
description: Cara menggunakan Lightning Zeus Embedded Wallet
---
![cover-zeus-embedded](assets/cover.webp)



ZEUS pada awalnya adalah aplikasi seluler untuk manajemen jarak jauh dari node petir, memungkinkan Anda untuk mengontrol node yang diinstal pada server jarak jauh


Tetapi aplikasi ini juga memiliki fitur "Node tertanam".



**Aspek aplikasi inilah yang akan kita jelajahi dalam tutorial ini.** Hal ini memungkinkan siapa saja untuk memiliki node petir mereka sendiri di ponsel, tanpa perlu server khusus, dengan cara yang sama seperti ACINQ menawarkan petir Wallet yang luar biasa, Phoenix.



https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

**Sebagai pengingat, Lightning adalah sebuah jaringan yang beroperasi secara paralel dengan Bitcoin, yang memungkinkan bitcoin untuk ditukarkan tanpa harus melakukan transaksi On-Chain secara sistematis. Hasilnya adalah transaksi yang hampir seketika, tanpa perlu menunggu 10 menit untuk memvalidasi sebuah blok. Hal ini sangat berguna ketika membayar pedagang di dunia fisik. Terlebih lagi, Lightning memberikan tingkat kerahasiaan yang luar biasa yang tidak dimiliki oleh jaringan Bitcoin.**



**Zeus "Integrated"** ditujukan untuk para pengguna Bitcoin yang ingin memaksimalkan privasi dan otonomi mereka.


Singkatnya, ini adalah ponsel Wallet impian para cypherpunks. Meskipun masih dalam tahap awal (versi alfa) dan masih terdapat beberapa bug, fitur-fiturnya sangat banyak, dan tidak diragukan lagi bahwa ini akan menyenangkan para pemberani di antara kita, yang menginginkan kontrol dan pilihan maksimum.



Di sisi lain, menurut saya, saat ini tidak cocok untuk pemula yang tidak terbiasa dengan Bitcoin dan hanya menginginkan cara yang sederhana untuk mengirim/menerima satoshi. Walaupun hal ini mungkin berubah di waktu mendatang, karena fitur penitipan melalui protokol Cashu (Chaumian Ecash) sedang diimplementasikan untuk para pemula...



## Instal aplikasi



Kunjungi [situs web proyek] (https://zeusln.com/) untuk mengunduh aplikasi untuk OS ponsel cerdas Anda:



![image](assets/fr/01.webp)



![image](assets/fr/02.webp)



## Pembuatan portofolio



Setelah aplikasi dimulai, klik tombol "Quick Start" untuk mulai membuat Wallet.



![image](assets/fr/03.webp)





Serangkaian layar inisialisasi kemudian muncul. Tunggu beberapa saat, lalu tunggu beberapa menit sampai node 100% tersinkronisasi melalui Neutrino.



Ini mungkin membutuhkan waktu beberapa menit. Sebagai informasi, neutrino adalah cara bagi dompet seluler untuk mengakses informasi Blockchain Bitcoin, tanpa perlu menjalankan Full node.



![image](assets/fr/04.webp)





Setelah beberapa saat, Anda siap untuk pergi.



![image](assets/fr/05.webp)




## Penyiapan aplikasi



Siap, tidak juga, karena sudah jelas bahwa pengguna Zeus yang sesuai dengan namanya menavigasi Wallet-nya dengan berkelas dan penuh gaya. Jadi kita harus mengubah avatarnya.



Klik avatar Anda di sudut kanan atas layar:



![image](assets/fr/06.webp)





Klik pada roda gigi, lalu pada tanda plus "+" :



![image](assets/fr/07.webp)





Pilih foto Zeus yang paling indah untuk mewakili Wallet ini dan klik "PILIH GAMBAR" di bagian bawah layar, lalu kembali dengan mengklik tanda panah di kanan atas.



![image](assets/fr/08.webp)





Terakhir, berikan nama panggilan pada Wallet Anda dan klik "SAVE Wallet CONFIG" agar perubahan dapat diterapkan. Terakhir, klik panah belakang di sudut kiri atas untuk kembali ke layar beranda.



![image](assets/fr/09.webp)





Kali ini kita benar-benar bisa memulai.



![image](assets/fr/10.webp)



### Biometrik



Untuk melindungi akses ke Wallet, Anda dapat menambahkan PIN/kata sandi dan mengaktifkan biometrik.



Untuk melakukan ini, buka menu utama Wallet dengan mengeklik garis horizontal di kiri atas.



![image](assets/fr/11.webp)





Pilih "Pengaturan", lalu "Keamanan", dan terakhir "Atur/Ganti PIN".



![image](assets/fr/12.webp)





Buat PIN Anda, konfirmasikan, dan aktifkan biometrik dengan menekan tombol "Biometrik" yang sesuai.  Kembali ke menu utama, dengan menggunakan tanda panah di kiri atas.



![image](assets/fr/13.webp)




### Simpan frasa Mnemonic



Setelah Anda kembali ke menu utama, klik "Cadangkan Wallet", lalu baca teks peringatan yang menginformasikan bahwa kehilangan 24 kata yang akan Anda terima sama saja dengan kehilangan akses ke dana Anda, dan siapa pun yang memiliki kata-kata ini selain Anda dapat mengakses dana Anda. Jangan pernah memberikannya kepada siapa pun.



Pilih "SAYA MENGERTI" di bagian bawah layar. Kemudian klik masing-masing dari 24 kata untuk memunculkannya, dan catat dengan cermat.



Anda bisa menuliskannya di atas kertas, atau mungkin, untuk keamanan tambahan, mengukirnya di atas baja tahan karat untuk melindunginya dari kebakaran, banjir, atau keruntuhan. Pilihan media untuk Mnemonic Anda akan bergantung pada strategi keamanan Anda, tetapi jika Anda menggunakan Zeus sebagai portofolio pengeluaran yang berisi jumlah sedang, kertas sudah cukup.



Untuk informasi lebih lanjut mengenai cara yang tepat untuk menyimpan dan mengelola frasa Mnemonic Anda, saya sangat merekomendasikan untuk mengikuti tutorial lainnya, khususnya jika Anda seorang pemula:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![image](assets/fr/14.webp)



Setelah selesai, klik "SAYA SUDAH MENCADANG 24 KATA SAYA" di bagian bawah layar, dan kita akan kembali ke layar beranda, siap untuk menerima bitcoin pertama kita.




## Opsi 1 - Menerima bitcoin On-Chain & membuka saluran Lightning



**Zeus Embedded** terutama dirancang sebagai simpul petir tertanam, tetapi juga dapat digunakan sebagai Wallet On-Chain.



Untuk menerima bitcoin On-Chain, klik tombol "On-Chain" lalu "Terima".


Terakhir, pindai kode QR atau salin Bitcoin Address untuk menyetor dana.



![image](assets/fr/15.webp)





Setelah dana dikonfirmasi dan dikreditkan ke Wallet Anda, Anda dapat menggunakannya untuk membuka **Lightning channel**. Saluran Lightning Anda adalah pintu gerbang ke Lightning Network, yang memungkinkan Anda untuk melakukan Exchange bitcoin dengan cara yang lebih rahasia dan cepat.





- Untuk melakukannya, klik "PINDAHKAN DANA On-Chain KE LIGHTNING"



Pada layar berikutnya, Anda diminta untuk membuka saluran yang bekerja sama dengan **"Olympus by Zeus "**, LSP (Lightning Service Provider) yang disukai oleh Wallet.


Untuk tutorial ini, kita akan memilih opsi ini demi kemudahan, tetapi sangat mungkin untuk membuka saluran dengan node apa pun di jaringan.


Bahkan dimungkinkan untuk membuka beberapa saluran dalam satu transaksi dengan memilih "OPEN ADDITIONAL CHANNEL". *Tetapi kita akan membahas hal ini dalam versi "lanjutan" dari tutorial* **Zeus Embedded**.





- Kemudian pilih jumlah yang ingin Anda dedikasikan untuk saluran ini. Dalam kasus kami, semua dana On-Chain kami akan digunakan, jadi kami mengaktifkan tombol "Gunakan semua dana yang memungkinkan".





- Terakhir, pilih tombol "OPEN CHANNEL" di bagian bawah layar.



![image](assets/fr/16.webp)





Dalam hitungan detik, saluran sudah terbentuk dan kami siap untuk melakukan transaksi Lightning pertama kami. Di layar beranda, kita bisa melihat jam kecil di sebelah saldo Wallet kita. Ini karena kita masih harus menunggu 3 konfirmasi On-Chain sebelum saluran benar-benar berfungsi.



![image](assets/fr/17.webp)





Setelah 3 kali konfirmasi, kami melihat bahwa saldo kami sekarang dikreditkan ke sisipan Lightning.



![image](assets/fr/18.webp)



Hal kecil yang perlu diperhatikan: ketika kita mengklik menu di bagian bawah layar untuk melihat status saluran petir kita, kita akan melihat bahwa sebagian kecil saldo kita tidak tersedia untuk dibelanjakan: kita hanya bisa membelanjakan 208253 satoshi, bukan 210370 satoshi yang kita miliki. Hal ini normal, karena ini khusus untuk protokol petir.



Terakhir, perlu dicatat bahwa mitra kami, Olympus, berhak untuk menutup saluran atas kebijakannya sendiri, jika saluran tersebut tidak digunakan, misalnya. Untuk memastikan bahwa saluran kita dipertahankan, kita harus membayar LSP (Penyedia Layanan Petir), seperti yang akan kita lihat di paragraf berikutnya, melalui cara ke-2 untuk membuka saluran.





## Kirim bitcoin melalui Lightning



Sekarang kita sudah menyiapkan saluran kita dan menjalankannya, mari kita lihat bagaimana kita dapat menggunakannya untuk membayar petir Invoice (Invoice).



Untuk melakukan ini, klik tombol "Lightning", kemudian "Send".



![image](assets/fr/19.webp)





Pada layar berikutnya, salin Invoice Anda ke dalam kolom khusus, atau pindai dengan mengeklik ikon di kanan atas. Terakhir, geser tombol "Geser untuk Membayar" ke kanan untuk membayar.



![image](assets/fr/20.webp)






Tunggu beberapa detik dan Invoice akan meluncur, dan satoshi Anda akan melaju dengan kecepatan cahaya.



![image](assets/fr/21.webp)





Zeus kemudian memungkinkan Anda untuk menambahkan catatan untuk mendenominasi pembayaran Anda, atau melihat rute yang diambil satoshi Anda sebelum mencapai tujuan (dan biaya yang dikenakan oleh semua node perantara). Ini adalah jenis fungsionalitas yang kami sukai dari Wallet.



![image](assets/fr/22.webp)



Perhatikan bahwa tidak seperti Wallet seperti [Phoenix]([Plan ₿ Network - Phoenix](https://planb.network/fr/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf)), dengan Zeus rute dihitung secara lokal dan tidak didelegasikan ke pihak ketiga (ACINQ dalam kasus Phoenix). Jadi, Anda adalah satu-satunya yang mengetahui penerima pembayaran. Kami kehilangan sedikit efisiensi (pembayaran membutuhkan waktu lebih lama untuk diselesaikan, tetapi kami mendapatkan banyak keuntungan dalam hal privasi).





Dengan mengklik panah kecil di bagian bawah layar beranda, Anda juga dapat melihat riwayat pembayaran kami. Di sini kita melihat dalam Green, 212.121 Sats yang diterima untuk On-Chain, kemudian warna merah masing-masing 211.756 Sats yang digunakan untuk membuka saluran kami, kemudian 121.212 satoshi yang digunakan untuk membayar petir Invoice.



![image](assets/fr/23.webp)





## Opsi 2 - Menerima bitcoin secara langsung di Lightning



Daripada membuka saluran secara manual, seperti yang baru saja kita lihat, dimungkinkan untuk menerima dana secara langsung melalui Lightning, bahkan tanpa saluran yang sudah ada sebelumnya, dengan menggunakan Olympus, Zeus LSP.




- Untuk melakukan ini, klik tombol "Lightning" pada layar beranda, kemudian pada "Receive".
- Kemudian pilih jumlah yang ingin Anda terima di kotak "Jumlah" dan pilih tombol "BUAT Invoice" di bagian bawah layar.



![image](assets/fr/24.webp)





Layar berikutnya menunjukkan Invoice yang harus dibayarkan untuk menerima satoshi. Kami diberitahu bahwa LSP akan menahan 10.000 Sats jika pembayaran dilakukan melalui Lightning. Kita akan lihat nanti bagaimana biaya pembukaan saluran ini dibenarkan.



Bayar Invoice atau minta orang lain untuk membayarnya, dan saluran akan dibuka secara otomatis, tetapi dikurangi 10.000 Sats sesuai kesepakatan.



![image](assets/fr/25.webp)





Kita sekarang berada di depan 2 saluran petir, yang statusnya dapat diperiksa dengan mengeklik tombol yang ditunjukkan oleh panah putih di bagian bawah layar beranda.



Kita dapat melihat bahwa, tidak seperti saluran yang dibuka dari skala On-Chain, saluran yang dibuka secara langsung melalui petir tidak menampilkan peringatan.


Karena Anda telah membayar untuk menyiapkan saluran ini, Penyedia Layanan Lightning (LSP) berjanji untuk memelihara saluran selama 3 bulan, dan menawarkan "likuiditas yang masuk" kepada Anda. Pada saluran paling bawah, Anda dapat melihat bahwa kapasitas penerimaan adalah 96383 satoshi. Oleh karena itu, LSP telah mengikat modal agar Anda dapat menerima pembayaran secara langsung setelah membuka saluran.



Jadi, 10.000 Satoshi dalam biaya yang dibayarkan mencakup: biaya pembukaan kanal (transaksi Bitcoin On-Chain, jaminan untuk memelihara kanal selama 3 bulan, dan penguncian modal).



![image](assets/fr/26.webp)





Selamat, Anda sekarang siap untuk menggunakan Zeus Embedded, sistem pencahayaan seluler Wallet dengan fitur paling canggih di pasaran.





Untuk mengetahui lebih lanjut tentang pengoperasian teknis Lightning Network, Anda dapat mengikuti pelatihan Plan ₿ Network gratis yang luar biasa dari Fanis Michalakis:



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb