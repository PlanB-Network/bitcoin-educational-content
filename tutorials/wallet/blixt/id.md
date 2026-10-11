---
name: Blixt Wallet
description: Bagaimana cara mulai menggunakan node LN yang kuat di ponsel kamu?
---
![cover](assets/cover.webp)


Panduan ini didedikasikan untuk semua pengguna baru yang ingin mulai menggunakan Bitcoin Lightning Network (LN) dengan sumber terbuka GRATIS, dengan cara NON-KUSTODIAL.


Menggunakan [Blixt Wallet](https://blixtwallet.com/), sebuah node LN penuh di ponsel Anda, di mana pun Anda berada.


Jika kamu belum pernah menggunakan Bitcoin Lightning Network, sebelum memulai, [silakan baca analogi penjelasan sederhana tentang Lightning Network (LN)](https://darth-coin.github.io/beginner/LN-airport-analogy-en.html).


## ASPEK-ASPEK PENTING:



- Blixt adalah sebuah node privat, BUKAN node perutean! Ingat ini: semua saluran LN di Blixt akan diumumkan ke grafik LN sebagai saluran pribadi. Artinya, NODE INI TIDAK AKAN MELAKUKAN ROUTING pembayaran orang lain melalui node Blixt. Node Blixt ini BUKAN untuk perutean, aku ulangi. Node ini terutama untuk mengelola saluran LN-mu sendiri dan melakukan pembayaran LN secara pribadi, kapan pun kamu membutuhkannya. Node Blixt ini harus online dan disinkronkan HANYA SEBELUM kamu melakukan transaksi. Itu sebabnya kamu akan melihat ikon di atas yang menunjukkan status sinkronisasi. Proses ini hanya membutuhkan beberapa saat, tergantung berapa lama kamu menyimpannya secara offline.




- Blixt menggunakan LND (aezeed) sebagai backend Wallet, jadi jangan coba-coba mengimpor jenis dompet Bitcoin lainnya ke dalamnya. [Di sini telah menjelaskan jenis-jenis Wallet Mnemonic](https://coldbit.com/what-types-of-Mnemonic-seeds-are-used-in-Bitcoin/). Dan berikut ini adalah [daftar yang lebih lengkap dari semua jenis wallet](https://walletsrecovery.org/). Jadi, jika sebelumnya kamu memiliki node LND, kamu dapat mengimpor seed dan backup.channels ke dalam Blixt, [seperti yang dijelaskan dalam panduan ini](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html).



- Di akhir panduan ini, kamu akan menemukan bagian khusus yang berisi ["tips dan trik"](https://darth-coin.github.io/wallets/getting-started-blixt-Wallet-en.html#tips)



- Tautan penting Blixt - lihat di bagian akhir panduan ini, silakan tandai.


---

## Blixt - Kontak Pertama


Jadi... Ibu Darth memutuskan untuk mulai menggunakan LN dengan Blixt. Keputusan keras, tapi bijaksana. Blixt hanya untuk orang-orang pintar dan mereka yang benar-benar ingin belajar lebih banyak, penggunaan LN yang mendalam.


![blixt](assets/en/01.webp)


Darth memperingatkan ibunya:


"*Ibu, jika Anda mulai menggunakan Blixt LN Node, Anda harus terlebih dahulu mengetahui apa itu Lightning Network dan bagaimana cara kerjanya, setidaknya pada tingkat dasar. [Di sini saya mengumpulkan daftar sumber daya sederhana tentang Lightning Network](https://blixtwallet.github.io/faq#what-is-LN). Silakan baca terlebih dahulu.*"


Ibu Darth membaca sumber-sumber yang ada dan melakukan langkah pertama: memasang Blixt pada perangkat Android barunya. Blixt juga tersedia untuk iOS dan macOS (desktop), tapi itu bukan untuk Ibu Darth... Meskipun begitu, disarankan menggunakan versi Android yang lebih baru, setidaknya 9 atau 10, untuk kompatibilitas dan pengalaman yang lebih baik. Menjalankan node LN secara penuh di perangkat seluler bukanlah hal yang mudah dan bisa memakan banyak ruang (min 600MB) serta memori.


Setelah kamu membuka Blixt, layar "Selamat Datang" akan memberi kamu beberapa opsi:


![blixt](assets/en/02.webp)


Di sudut kanan atas, Anda akan melihat 3 titik yang mengaktifkan menu:



- "aktifkan Tor" - pengguna dapat memulai dengan jaringan Tor, secara khusus jika ingin memulihkan node LND lama yang berjalan dengan rekan-rekan Tor saja.
- "Set Bitcoin node" - jika pengguna ingin terhubung ke node-nya sendiri secara langsung, untuk menyinkronkan blok melalui Neutrino, dapat melakukannya langsung dari layar selamat datang. Opsi ini juga bagus jika koneksi internet atau Tor Anda tidak begitu stabil untuk terhubung ke node Bitcoin default (node.blixtwallet.com).
- Dalam waktu dekat akan ditambahkan bahasa di sana, sehingga pengguna dapat langsung memulai dengan bahasa yang nyaman. Jika kamu ingin berkontribusi pada proyek open source ini dengan menerjemahkan ke bahasa lain, [silakan bergabung di sini](https://explore.transifex.com/blixt-Wallet/blixt-Wallet/).


### OPSI A - Buat Wallet baru


Jika kamu memilih "membuat Wallet baru", kamu akan langsung diarahkan ke layar utama Blixt Wallet.


Ini adalah "kokpit"-mu dan juga merupakan "LN Wallet Utama", jadi perhatikan, ini hanya menampilkan saldo LN Wallet-mu. Wallet onchain ditampilkan secara terpisah (lihat C).


![blixt](assets/en/03.webp)


A - Ikon indikator sinkronisasi blok Blixt. Ini adalah hal paling penting untuk node LN: memastikan node tersinkronisasi dengan jaringan. Jika ikon tersebut masih bergerak, berarti node-mu BELUM SIAP! Jadi bersabarlah, terutama saat sinkronisasi awal. Proses ini bisa memakan waktu 6-8 menit, tergantung perangkat dan koneksi internetmu.



Kamu bisa mengekliknya dan melihat status sinkronisasi:


![blixt](assets/en/04.webp)


Kamu juga bisa mengklik tombol "Tampilkan Log LND" (A) jika ingin melihat dan membaca lebih banyak detail teknis dari log LND secara real time. Ini sangat berguna untuk melakukan debug dan mempelajari lebih dalam cara kerja LN.



B - Di sini kamu dapat mengakses semua Pengaturan Blixt, dan banyak sekali! Blixt menawarkan banyak fitur dan opsi yang kaya untuk mengelola node LN Anda seperti seorang profesional. Semua opsi tersebut dijelaskan secara rinci di "[Halaman Fitur Blixt](https://blixtwallet.github.io/features#blixt-options) - Menu Opsi".


C - Di sini kamu memiliki menu "Laci Ajaib", [juga dijelaskan secara rinci di sini](https://blixtwallet.github.io/features#blixt-drawer). Di sini terdapat "Onchain Wallet" (B), Saluran Lightning (C), Kontak, ikon status Saluran (A), Keysend (D).


![blixt](assets/en/05.webp)


D - Adalah menu bantuan, dengan tautan ke halaman FAQ/Panduan, kontak pengembang, halaman Github, dan grup dukungan Telegram.


E - Tunjukkan BTC Address pertamamu, tempat kamu bisa menyetor Sats pengujian pertama. INI OPSIONAL! Jika kamu menyetor langsung ke Address tersebut, berarti kamu membuka saluran LN menuju Blixt Node. Artinya, Sats yang kamu setorkan akan masuk ke transaksi onchain (tx) lain untuk membuka saluran LN itu. Kamu bisa memeriksanya di Blixt onchain Wallet (lihat poin C) dengan mengklik menu TX di kanan atas.



![blixt](assets/en/06.webp)


Seperti yang dapat kamu lihat di Log Transaksi Onchain, langkah-langkahnya sangat terperinci yang menunjukkan ke mana arah Sats (deposit, buka, tutup saluran).


REKOMENDASI:


Setelah menguji beberapa situasi, kami menyimpulkan bahwa jauh lebih efisien membuka saluran antara 1 hingga 5 M Sats. Saluran yang lebih kecil cenderung cepat habis dan membayar biaya lebih tinggi dibandingkan saluran yang lebih besar.


F - Menunjukkan saldo Lightning Wallet utama-mu. Ini BUKAN total saldo Blixt Wallet, hanya mewakili Sats yang kamu miliki di Lightning Channels, yang tersedia untuk dikirim. Seperti disebut sebelumnya, Onchain Wallet terpisah. Ingat ini: Onchain Wallet terpisah karena alasan penting, terutama digunakan untuk membuka/menutup saluran LN.


Baiklah, sekarang Ibu Darth telah menyetorkan sejumlah Sats ke onchain Address yang ditampilkan di layar utama. Disarankan saat melakukan ini, biarkan aplikasi Blixt tetap online dan aktif untuk sementara, sampai BTC tx dimasukkan penambang ke dalam blok pertama.


Setelah itu, proses konfirmasi bisa memakan waktu 20-30 menit sampai saluran terbuka sepenuhnya dan kamu akan melihatnya di Laci Ajaib - Saluran Petir sebagai aktif. Titik kecil berwarna di atas laci, jika Green, menunjukkan bahwa saluran LN-mu sedang online dan siap digunakan untuk mengirim Sats melalui LN.


Address dan pesan selamat datang yang ditampilkan akan hilang. Tidak perlu lagi membuka saluran otomatis sekarang. Kamu juga bisa menonaktifkan opsi ini di menu Pengaturan.



Saatnya untuk melanjutkan, menguji fitur dan opsi lain untuk membuka saluran LN.


Sekarang, mari kita buka saluran lain dengan peer node lain. Komunitas Blixt menempatkan togheter [daftar node yang baik untuk mulai digunakan dengan Blixt](https://github.com/hsjoberg/blixt-Wallet/issues/1033).


**Prosedur untuk membuka saluran LN di Blixt**


Ini sangat sederhana, hanya perlu beberapa langkah dan sedikit kesabaran:



- Masuk ke daftar rekan kerja [Komunitas Blixt](https://github.com/hsjoberg/blixt-Wallet/issues/1033)
- Pilih simpul dan klik tautan judul namanya, simpul tersebut akan membuka halaman Amboss
- Klik untuk menampilkan kode QR untuk node URI Address


![blixt](assets/en/07.webp)


Buka Blixt dan pergi ke laci atas - Saluran Lightning dan klik tombol "+"


![blixt](assets/en/08.webp)


Sekarang, klik (A) kamera untuk memindai kode QR dari halaman Amboss dan detail node akan terisi. Tambahkan jumlah Sats untuk saluran yang kamu inginkan, lalu pilih tarif biaya untuk tx. Kamu bisa membiarkannya otomatis (B) untuk konfirmasi lebih cepat atau menyesuaikannya secara manual dengan menggeser tombol. Kamu juga bisa menekan lama angka dan mengeditnya sesuka hati.


Jangan memasang kurang dari 1 sat/vbyte! Biasanya lebih baik untuk berkonsultasi dengan [biaya Mempool](https://Mempool.space/) sebelum membuka saluran dan memilih biaya yang sesuai.


Selesai, sekarang tinggal klik tombol "buka saluran" dan tunggu 3 konfirmasi, yang biasanya memakan waktu 30 menit (1 blok kira-kira setiap 10 menit).


Setelah dikonfirmasi, Anda akan melihat saluran yang aktif di bagian "Saluran Lightning".


---

## Blixt - Kontak Kedua


Baiklah, sekarang kita memiliki saluran LN dengan likuiditas yang hanya OUTBOUND. Itu berarti kita hanya dapat MENGIRIM, kita masih tidak dapat MENERIMA Sats melalui LN.


![blixt](assets/en/09.webp)


Kenapa? Apakah kamu sudah membaca panduan yang ditunjukkan di awal? Tidak? Kembalilah dan bacalah. Sangat penting untuk memahami cara kerja saluran LN.


![blixt](assets/en/10.webp)


Seperti yang terlihat pada contoh ini, saluran yang dibuka dengan setoran pertama tidak memiliki terlalu banyak likuiditas INBOUND ("Dapat menerima") tetapi memiliki banyak likuiditas OUTBOUND ("Dapat mengirim").


Jadi, opsi apa yang kamu miliki jika ingin menerima lebih banyak Sats melalui LN?


- Habiskan beberapa Sats dari saluran yang ada. Ya, LN adalah jaringan pembayaran Bitcoin, yang digunakan terutama untuk membelanjakan Sats-mu dengan lebih cepat, lebih murah, privat, dan mudah. LN BUKAN tempat untuk hodling; untuk itu, kamu punya onchain Wallet.


- Tukar beberapa Sats kembali ke onchain Wallet-mu menggunakan layanan submarine swap. Dengan cara ini, kamu tidak kehilangan Sats-mu, tetapi mengembalikannya ke onchain Wallet sendiri.
 Di sini Anda dapat melihat secara detail beberapa metode, di [Halaman Panduan Blixt](https://blixtwallet.github.io/guides).



- Buka saluran INBOUND dari penyedia LSP mana pun. Berikut ini adalah demo video tentang cara menggunakan LNBig LSP untuk membuka saluran inbound. Itu berarti, Anda akan membayar sedikit biaya untuk saluran KOSONG (di sisi Anda) dan Anda akan dapat menerima lebih banyak Sats ke dalam saluran tersebut. Jika Anda adalah pedagang yang menerima lebih banyak daripada membelanjakan, itu adalah pilihan yang bagus. Juga jika Anda membeli Sats di atas LN, menggunakan Robosats atau LN Exchange lainnya.



- Buka saluran Dunder, dengan node Blixt atau penyedia LSP Dunder lainnya. Saluran Dunder adalah cara sederhana untuk mendapatkan likuiditas INBOUND, tetapi pada saat yang sama kamu menyetor sejumlah Sats ke dalam saluran tersebut. Hal ini juga bagus karena akan membuka saluran dengan [UTXO](https://en.Bitcoin.it/wiki/UTXO) yang bukan berasal dari Blixt Wallet kamu. Hal ini akan menambah privasi. Juga bagus karena, jika kamu tidak memiliki Sats ke dalam onchain Wallet, untuk membuka saluran LN normal, tetapi anda memilikinya ke dalam LN Wallet lainnya, kamu dapat membayar dari Wallet lainnya melalui LN pembukaan dan deposit (di sisi kamu) saluran Dunder tersebut. [Lebih detail cara kerja Dunder dan cara menjalankan server Anda sendiri di sini](https://github.com/hsjoberg/dunder-lsp).


![blixt](assets/en/11.webp)


Berikut adalah langkah-langkah untuk mengaktifkan pembukaan saluran Dunder:



- Buka Pengaturan, di bagian "Eksperimen" aktifkan kotak untuk "Aktifkan Dunder LSP".
- Setelah kamu melakukannya, kembali ke bagian "Lightning Network" dan kamu akan melihat opsi "Set Dunder LSP Server". Di sana, secara default diatur "https://dunder.blixtwallet.com" tetapi Anda dapat mengubahnya dengan penyedia LSP Dunder lainnya Address. [Berikut adalah daftar komunitas Blixt](https://github.com/hsjoberg/blixt-Wallet/issues/1033) dengan node yang dapat menyediakan saluran LSP Dudner untuk Blixt Anda.
- Sekarang kamu dapat masuk ke layar utama dan klik tombol "Terima". Kemudian ikuti prosedur ini [dijelaskan dalam panduan ini](https://blixtwallet.github.io/guides#guide-lsp).


Oke, jadi setelah saluran Dunder dikonfirmasi (akan memakan waktu beberapa menit) Anda akan mendapatkan 2 saluran LN: satu saluran yang dibuka dengan autopilot (saluran A) dan satu saluran dengan likuiditas yang lebih banyak, dibuka dengan Dunder (saluran B).


![blixt](assets/en/12.webp)


Bagus, sekarang kamu sudah siap untuk mengirim dan menerima cukup banyak Sats melalui LN!


SELAMAT DATANG LIGHTNING Bitcoin!


---

## Blixt - Kontak Ketiga


Ingat, pada bab satu "Kontak Pertama" ada 2 pilihan di layar Selamat Datang:


- [Opsi A](https://darth-coin.github.io/wallets/getting-started-blixt-Wallet-en.html#option-a) - Buat Wallet baru
- Opsi B - Pulihkan Wallet


Jadi sekarang mari kita bahas tentang cara memulihkan Blixt Wallet atau node LND yang rusak. Ini sedikit lebih teknis, tetapi mohon diperhatikan. Bukankah itu Hard.


### OPSI B - Kembalikan Wallet


Di masa lalu saya menulis panduan khusus tentang [cara memulihkan node Umbrel yang rusak](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html), di mana saya juga menyebutkan metode menggunakan Blixt sebagai proses pemulihan cepat, menggunakan file seed + channel.backup dari Umbrel.


Saya juga menulis panduan cara memulihkan node Blixt atau memigrasi Blixt kamu ke perangkat lain, [di sini](https://blixtwallet.github.io/faq#blixt-restore).


![blixt](assets/en/13.webp)


Namun, mari kita jelaskan secara sederhana proses ini. Seperti yang dapat kamu lihat pada gambar di atas, ada 2 hal yang harus kamu lakukan untuk memulihkan node Blixt/LND sebelumnya:



- Kotak teratas adalah tempat kamu harus mengisi semua 24 kata dari seed-mu (node lama / mati).  
- Di bagian bawah terdapat dua tombol untuk memasukkan/mengunggah file channel.backup, yang sebelumnya disimpan dari node Blixt/LND lamamu. Bisa dari berkas lokal (yang sudah diunggah ke perangkatmu sebelumnya) atau dari lokasi jarak jauh seperti Google Drive / iCloud. Blixt menyediakan opsi ini untuk menyimpan cadangan saluran-mu langsung ke Google Drive / iCloud.
Lihat detail lebih lanjut di [Halaman Fitur Blixt](https://blixtwallet.github.io/features#blixt-options).


Namun, jika sebelumnya kamu tidak punya saluran LN yang terbuka, tidak perlu mengunggah file channels.backup. Cukup masukkan 24 kata seed-mu dan tekan tombol restore.


Jangan lupa mengaktifkan Tor dari menu 3 titik di atas, seperti yang dijelaskan di bagian Opsi A. Ini diperlukan hanya jika kamu HANYA memiliki rekan Tor dan tidak bisa dihubungi melalui clearnet (domain/IP). Selain itu, tidak perlu.


Fitur lain yang berguna adalah mengatur node Bitcoin tertentu dari menu atas. Secara default, Blixt menyinkronkan blok dari node.blixtwallet.com (mode Neutrino), tetapi kamu bisa mengatur node Bitcoin lain yang menyediakan sinkronisasi Neutrino.


Setelah mengisi opsi-opsi tersebut dan menekan tombol restore, Blixt akan mulai menyinkronkan blok-blok melalui Neutrino seperti dijelaskan di bab Kontak Pertama. Bersabarlah dan perhatikan proses pemulihan di layar utama dengan mengklik ikon sinkronisasi.



![blixt](assets/en/14.webp)


Seperti yang terlihat pada contoh ini, blok Bitcoin telah tersinkronisasi 100% (A) dan proses pemulihan sedang berjalan (B). Artinya, saluran LN yang kamu miliki sebelumnya akan ditutup dan dananya akan dipulihkan ke dalam onchain Blixt Wallet-mu.


Proses ini membutuhkan waktu, jadi bersabarlah dan pastikan Blixt tetap aktif dan online. Sinkronisasi awal bisa memakan waktu 6-8 menit, dan penutupan saluran bisa memakan waktu 10-15 menit. Sebaiknya isi daya perangkat dengan baik.


Setelah proses dimulai, kamu bisa memeriksa status masing-masing saluran lamamu di Laci Ajaib - Saluran Petir, yang menunjukkan status "menunggu penutupan". Setelah setiap saluran ditutup, kamu bisa melihat tx penutupan di onchain Wallet (lihat Laci Ajaib - Onchain) dan membuka log menu tx.



![blixt](assets/en/15.webp)


Juga akan lebih baik untuk memeriksa dan menambahkan jika tidak ada, relay-relay kamu sebelumnya yang kamu miliki di node LN lama. Jadi pergi ke menu Pengaturan, ke "Lightning Network" dan masuk ke opsi "Tampilkan Rekan Petir".


![blixt](assets/en/16.webp)


Di dalam bagian ini Anda akan melihat peer yang terhubung dengan kamu pada saat itu dan dapat menambahkan lebih banyak lagi, lebih baik menambahkan yang sudah kamu miliki salurannya sebelumnya. Cukup buka [halaman Amboss](https://amboss.space/), cari node peer alias atau nodeID kamu dan pindai URI node mereka.


![blixt](assets/en/17.webp)


Seperti yang terlihat pada gambar di atas, ada 3 aspek:


A - mewakili node clearnet Address URI (domain/IP)  


B - mewakili node bawang Tor Address URI (.onion)  


C - adalah kode QR untuk dipindai dengan kamera Blixt-mu atau tombol salin.


URI node Address ini harus ditambahkan ke daftar peer-mu. Jadi, hanya mengetahui nama alias node atau nodeID saja tidak cukup.


Sekarang kamu bisa pergi ke Magic Drawer (menu kiri atas) - Lightning Channels, dan melihat pada tingkat blok jatuh tempo kapan dana akan dikembalikan ke onchain Address-mu.



![blixt](assets/en/18.webp)


Nomor blok 764272 adalah saat dana akan dapat digunakan di Bitcoin onchain Address kamu. Dan itu bisa memakan waktu hingga 144 blok dari blok konfirmasi pertama hingga dirilis. [Jadi, periksa di Mempool](https://Mempool.space/).


Dan hanya itu saja. Tunggu saja dengan sabar hingga semua saluran ditutup dan dana kembali ke onchain Wallet kamu.


👉 **Metode pemulihan rahasia :**


Ada metode lain untuk memulihkan node Blixt LND-mu tanpa menutup saluran. Namun, metode ini tersembunyi bagi pengguna pemula, karena HANYA untuk mereka yang tahu apa yang mereka lakukan.


Jika kamu perlu memigrasikan node Blixt yang sudah ada (masih berfungsi) ke perangkat baru tanpa menutup saluran LN, lakukan langkah-langkah berikut:


- Asumsikan kamu sudah menyimpan Blixt Wallet seed (24 kata aezeed).  
- Di perangkat lama, buka "Pengaturan" → bagian debug → "Compact LND database". Langkah ini opsional tapi disarankan jika ingin ukuran file channel.db lebih kecil. Ukurannya biasanya cukup besar tergantung aktivitas node-mu. Ini akan memulai ulang Blixt dan memadatkan ukuran file db.  
- Setelah restart, buka "Pengaturan" dan ubah nama alias reguler-mu menjadi "Hampus". Ini akan mengaktifkan opsi tersembunyi, hanya untuk pengguna tingkat lanjut.  
- Pergi ke bagian "Debug" dan kamu akan melihat opsi baru "Ekspor file channel.db". PERINGATAN! Setelah ekspor, node Blixt LN di perangkat lama akan dinonaktifkan dan seluruh basis data node (channel.db) siap diimpor ke perangkat baru.  
- File db ini akan tersimpan di folder yang ditentukan di perangkat lama (Dokumen atau Unduhan). Dari sana, pindahkan ke perangkat baru menggunakan misalnya [aplikasi LocalSend FOSS](https://github.com/localsend/localsend) untuk mentransfer file langsung antar perangkat.  
- Saat ini, Blixt lama HARUS tetap ditutup. JANGAN DIBUKA LAGI!  
- Setelah mentransfer file channel.db ke perangkat baru, mulai instalasi baru Blixt dan pilih "Restore Wallet" di layar pertama.  
- Pada tombol "Pilih file SCB", tekan lama (JANGAN klik biasa!) untuk memilih file channel.db yang kamu simpan secara lokal di perangkat baru. Jika hanya ditekan sekali, secara default akan menggunakan file SCB (dengan menutup saluran) dan tidak bisa digunakan untuk pencadangan saluran langsung.  
- Masukkan 24 kata seed-mu lalu klik "Pulihkan".  
- Kamu akan melihat Blixt mulai menyinkronkan dengan Neutrino. Kamu juga bisa memantau log sinkronisasi.  
- INGAT! Pastikan Blixt tetap terbuka sepanjang fase ini! Jangan biarkan masuk mode tidur atau menutup layar aplikasi, karena akan mengganggu sinkronisasi awal dan kamu harus mengulangnya. Tunggu dengan sabar, proses ini hanya memakan beberapa menit.  
- Setelah sinkronisasi blok awal selesai, Blixt akan memindai alamat Wallet-mu sebelumnya dan saluran akan kembali online, hidup, dan sehat.  
- Sayangnya, riwayat pembayaran dan kontak sebelumnya tidak bisa dikembalikan (belum), tapi itu tidak terlalu penting.

SELESAI! Sekarang kamu memiliki node Blixt LN yang sepenuhnya dipulihkan. Cara ini juga bekerja dengan cadangan LND lain (Umbrel, Raspiblitz, dll) jika file channel.db disimpan dengan benar sebelumnya. Jadi Blixt benar-benar bisa menyimpan node LND yang mati.



---

## Blixt - Kontak Keempat


Bab ini adalah tentang kustomisasi dan mengenal Blixt Node dengan lebih baik. Aku tidak akan menjelaskan semua fitur yang tersedia, karena terlalu banyak dan sudah dijelaskan di [Halaman Fitur Blixt](https://blixtwallet.github.io/features).


Tetapi aku akan menunjukkan beberapa hal yang diperlukan untuk terus menggunakan Blixt dan mendapatkan pengalaman yang luar biasa.


### A - Nama (NameDesc)


![blixt](assets/en/19.webp)


[NamDesc](https://github.com/lightning/blips/blob/master/blip-0011.md) adalah standar untuk menyampaikan "nama penerima" dalam faktur BOLT11.


Ini bisa berupa nama apa saja dan dapat diubah kapan saja.


Opsi ini sangat berguna dalam berbagai situasi, misalnya ketika kamu ingin mengirim nama bersama deskripsi Invoice, sehingga penerima memiliki petunjuk tentang siapa yang menerima Sats. Ini sepenuhnya opsional, dan pada layar pembayaran, pengguna harus mencentang kotak untuk mengirim nama alias.


Berikut ini adalah contoh tampilan yang akan muncul ketika kamu menggunakan [chat.blixtwallet.com](https://chat.blixtwallet.com/)


![blixt](assets/en/20.webp)


Ini adalah contoh lain pengiriman ke aplikasi Wallet lain yang mendukung NameDesc:


![blixt](assets/en/21.webp)


### B - Kotak Petir


Dimulai dengan v0.6.9-420 yang baru [baru-baru ini diumumkan](https://github.com/hsjoberg/blixt-Wallet/releases/tag/v0.6.9-420), Blixt memperkenalkan fitur baru yang kuat untuk Lightning Address di Blixt.


Fitur baru ini bersifat opsional dan TIDAK AKTIF secara default!


Saat ini, LN Box default dijalankan oleh server Blixt dan menawarkan @blixtwallet.com LN Address. Namun, SIAPAPUN yang memiliki node publik LND dapat menjalankan server Lightning Box sendiri dan menawarkan LN Address untuk domain dan penyimpanan mereka sendiri.


Sekarang, server Blixt hanya meneruskan pembayaran yang dikirim ke alamat LN @blixtwallet.com ke pengguna Blixt yang sudah mengatur LN Address mereka. Pengguna harus menempatkan node Blixt Wallet dalam "mode persisten" untuk menerima pembayaran ke alamat LN @blixtwallet.com.


Lihat dalam catatan rilis video demo tentang cara mengatur LN Address kamu di Blixt.


LN Address yang diimplementasikan ke dalam aplikasi Blixt Wallet ini, seperti chatting melalui LN, instan dan menyenangkan, juga mendukung [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (menambahkan nama alias ke pembayaran). Kamu dapat menambahkan dalam daftar kontak semua alamat LN biasa yang sering kamu gunakan dan siap sedia untuk mengobrol. Sekarang Blixt dapat dianggap sebagai aplikasi obrolan LN yang lengkap 😂😂.


Fitur lain yang berguna adalah dukungan penuh terhadap LUD-18 (yang juga didukung oleh [Stacker.News](https://stacker.news/r/DarthCoin) dan yang lainnya).


![blixt](assets/en/22.webp)


Seperti yang terlihat pada tangkapan layar di atas, pengiriman dari akun Stacker News menampilkan logo + LN Address + pesan dengan baik. Hal yang sama berlaku untuk pengiriman dari Blixt: kamu bisa melampirkan Blixt LN Address-mu, cukup menambahkan nama alias (yang sebelumnya diatur di pengaturan Blixt), atau bahkan keduanya.


Opsi dari LUD-18 ini dapat berguna juga untuk layanan berlangganan, di mana pengguna dapat mengirimkan alias tertentu (BUKAN nama alias node atau nama asli kamu!) dan berdasarkan hal tersebut Anda dapat didaftarkan atau menerima kembali pesan tertentu atau apa pun. Melampirkan nama alias ([LUD-18](https://github.com/lnurl/luds/blob/luds/18.md)) + komentar ([LUD-12](https://github.com/lnurl/luds/blob/luds/12.md)) pada pembayaran LN dapat memiliki beberapa kasus penggunaan!


Berikut ini adalah kode untuk [Lightning Box](https://github.com/hsjoberg/lightning-box) jika Anda menjalankannya untuk Anda sendiri, untuk keluarga dan teman kamu, di node kamu sendiri.


Di sini kamu juga dapat menjalankan [LSP Dunder server](https://github.com/hsjoberg/dunder-lsp) untuk node seluler Blixt dan menawarkan likuiditas untuk pengguna Blixt jika kamu memiliki node LN publik yang baik (hanya berfungsi dengan LND).


### C - Cadangan Saluran LN dan kata seed


Ini adalah fitur yang sangat penting!


Setelah membuka atau menutup saluran LN, kamu harus melakukan pencadangan. Hal ini dapat dilakukan secara manual dengan menyimpan file kecil di perangkat lokal (biasanya folder unduhan) atau menggunakan akun Google Drive atau iCloud.


![blixt](assets/en/23.webp)


Buka bagian Pengaturan Blixt - Wallet. Di sana kamu memiliki opsi untuk menyimpan semua data penting untuk Blixt Wallet:



- "Tampilkan Mnemonic" - akan menampilkan 24 kata seed untuk dituliskan.  
- "Hapus Mnemonic dari perangkat" - opsional, gunakan hanya jika benar-benar ingin menghapus kata seed dari perangkat. Ini TIDAK akan menghapus Wallet-mu, hanya seed. Perlu diingat, tidak ada cara untuk memulihkannya jika kamu belum menuliskannya terlebih dahulu.  
- "Export channel backup" - opsi ini akan menyimpan file kecil di perangkat lokal, biasanya di folder "download", dari mana kamu bisa memindahkannya ke luar perangkat untuk disimpan dengan aman.  
- "Verifikasi cadangan saluran" - opsi ini berguna jika kamu menggunakan Google Drive atau iCloud, untuk memeriksa integritas cadangan yang dilakukan dari jarak jauh.  
- "Cadangan saluran Google Drive" - akan menyimpan file cadangan ke Google Drive pribadimu. File ini dienkripsi dan disimpan di lokasi terpisah dari file Google biasa, sehingga aman dan tidak bisa dibaca orang lain. Bagaimanapun, file ini sama sekali tidak berguna tanpa kata-kata seed, jadi tidak ada yang bisa mengambil dana hanya dari file tersebut.


Rekomendasi untuk bagian ini:


- Gunakan pengelola kata sandi untuk menyimpan seed dan file cadangan dengan aman. KeePass atau Bitwarden sangat bagus untuk itu, bisa digunakan multiplatform dan di-host sendiri atau offline.  
- LAKUKAN CADANGAN SETIAP KALI kamu membuka atau menutup saluran. File tersebut akan diperbarui dengan info saluran. Kamu tidak perlu melakukannya setelah setiap transaksi LN. Pencadangan saluran tidak menyimpan info transaksi, hanya status saluran.



![blixt](assets/en/24.webp)


---

## Blixt - Kiat dan Trik


### KASUS 1 - MASALAH SINKRONISASI


"_Blixt-ku tidak tersinkronisasi... Blixt-ku tidak menunjukkan saldo... Blixt-ku tidak bisa membuka saluran... Aku mencoba memulihkannya di perangkat lain... dll."


Semua masalah ini biasanya muncul karena PERANGKAT-MU TIDAK TERSINKRONISASI DENGAN BENAR. Perlu dipahami hal penting ini: Blixt adalah node LND seluler yang menggunakan Neutrino untuk menyinkronkan dan membaca blok.




- Berikut ini penjelasan yang tidak terlalu teknis dari [Majalah Bitcoin](https://bitcoinmagazine.com/technical/why-Bitcoin-wallets-need-block-filters)
- Berikut ini adalah sumber daya teknis lebih lanjut dari [Bitcoin Optech](https://bitcoinops.org/en/topics/compact-block-filters/)
- Berikut ini adalah bagaimana kamu dapat mengaktifkan Neutrino di node rumah Anda sendiri dan melayani filter blok untuk node seluler Anda, dari [Docs Lightning Engineering](https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core)


PERINGATAN: Menggunakan Neutrino melalui clearnet benar-benar aman. IP atau xpub-mu tidak akan bocor. Kamu hanya membaca blok dari node jarak jauh dengan Neutrino. Sisanya semua dilakukan di perangkat lokalmu.


Jadi, TIDAK PERLU menggunakan Tor. Tor akan menambah latensi secara signifikan pada proses sinkronisasi dan membuat Blixt-mu sangat tidak stabil. Jika benar-benar ingin menggunakan Tor, pastikan kamu paham apa yang dilakukan, memiliki koneksi yang baik, dan bersabar. Hal yang sama berlaku untuk VPN—perhatikan latensi tambahan yang ditimbulkan oleh VPN.


Kamu bisa menguji latensi server Neutrino dengan melakukan ping, dari PC atau ponselmu.


![blixt](assets/en/25.webp)


Ini adalah ping biasa ke server Neutrino europe.blixtwallet.com, yang menunjukkan koneksi sangat bagus dengan waktu respons rata-rata 50ms dan TTL 51. Waktu respons bisa bervariasi, tapi tidak terlalu banyak. TTL harus stabil.


Jika nilai ini lebih tinggi dari 100-150ms, proses sinkronisasi bisa macet atau, lebih buruk lagi, saluranmu bisa tertutup oleh peer. Jangan abaikan hal ini.


Tanpa sinkronisasi yang tepat, kamu tidak akan melihat saldo yang benar, dan saluran LN-mu tidak akan online atau beroperasi. Tidak peduli seberapa tinggi kecepatan unduh-mu, yang penting adalah waktu respons dan TTL (Time To Live).


Hal ini umum terjadi pada pengguna di kawasan Amerika Latin. Aku tidak tahu persis apa yang terjadi, tapi kalian memiliki koneksi dengan ping lebih dari 200ms, yang bisa mengganggu sinkronisasi.


Jadi, apa solusi untuk para pengguna yang putus asa ini?



- Berhenti menggunakan Blixt dengan Tor. Sama sekali tidak berguna.  
- Kamu bisa menggunakan VPN, tapi pilih dengan bijak dan selalu pantau ping-mu. Gunakan yang lebih dekat dengan lokasi geografismu. Ingat, jarak lebih jauh berarti waktu respons (ms) lebih tinggi.  
- Pilih dengan bijak peer Neutrino-mu. Berikut adalah daftar server Neutrino publik yang terkenal:



```txt
For US region
btcd1.lnolymp.us | btcd2.lnolymp.us
btcd-mainnet.lightning.computer
swest.blixtwallet.com (Seattle)
node.eldamar.icu
noad.sathoarder.com
bb1.breez.technology | bb2.breez.technology
neutrino.shock.network
For EU region
europe.blixtwallet.com (Germany)
For Asia region
sg.lnolymp.us
asia.blixtwallet.com
```


Cara lain adalah dengan memilih salah satu dari daftar node yang mengumumkan "filter ringkas" (BIP157/neutrino) - [Halaman Bitnodes Filter Neutrino](https://bitnodes.io/nodes/?q=NODE_COMPACT_FILTERS). Pilih salah satu yang lebih dekat dengan lokasi geografis kamu.


Cara lain (cara terbaik) adalah terhubung ke node komunitas lokal, yang dikelola oleh teman atau grup yang kamu kenal, dan menawarkan koneksi Neutrino. (https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core) Node mereka tidak akan terpengaruh sama sekali; mereka hanya membutuhkan koneksi yang stabil dan bersifat publik.


Ada kebutuhan akan lebih banyak server Neutrino di wilayah LATAM untuk sinkronisasi yang lebih baik dan cepat. Jadi, atur diri sendiri dengan komunitas Bitcoin lokalmu dan putuskan siapa dan di mana yang menjalankan Bitcoin Core + Neutrino untuk penggunaanmu. IP publik saja sudah cukup. Jika tidak memiliki akses ke IP publik, kamu bisa menggunakan IP VPS dan membuat terowongan WireGuard ke node rumahmu. Dengan begitu, semua trafik diarahkan ke IP VPS lokal tanpa mengungkapkan informasi pribadi tentang node rumahmu.



### KASUS 2 - TIDAK PERNAH MENYELESAIKAN SINKRONISASI


"_Blixt saya memiliki koneksi yang baik dengan server neutrino namun mengalami kendala dalam sinkronisasi._"


#### Server Waktu


Kadang-kadang orang menggunakan perangkat lama atau yang tidak terhubung dengan benar ke server waktu. Neutrino akan melakukan sinkronisasi dengan baik hingga mencapai blok aktual yang tidak sesuai dengan waktu lokal. Kamu akan melihat di log Blixt LND kesalahan seperti "stempel waktu blok jauh di masa depan" atau hal terkait "header tidak lulus pemeriksaan kewarasan".


Perbaikan cepat: atur waktu dan tanggal yang tepat untuk perangkat kamu dan mulai ulang Blixt.


#### Ruang kecil pada perangkat


Terkadang, dengan menggunakan perangkat lama atau dengan ruang penyimpanan kecil, node bisa mencapai batas dan macet. Semakin sering kamu menggunakan node LND seluler ini, file Neutrino dan file channel.db akan semakin besar.


Perbaikan cepat: Buka Opsi Blixt → Bagian Debug → pilih "Hentikan LND dan hapus file Neutrino". Ini akan memulai ulang aplikasi dan memulai sinkronisasi baru. Kadang-kadang, perbaikan cepat ini juga bisa memperbaiki data yang rusak. Perlu diingat, proses ini memakan waktu 1-3 menit untuk sinkronisasi ulang sepenuhnya. Proses ini TIDAK menghapus dana atau saluran yang ada, tetapi setelah sinkronisasi ulang bisa memicu pemindaian ulang alamat Bitcoin-mu, yang mungkin memakan waktu lebih lama.


Langkah selanjutnya adalah memeriksa berapa banyak data yang masih digunakan. Kamu bisa melihatnya di info Aplikasi Android → Data. Jika masih lebih besar dari 400-500MB, kamu bisa memadatkan file LND. Caranya: buka Opsi Blixt → Bagian Debug → pilih "Compact DB LND". Mulai ulang aplikasi Blixt jika tidak berjalan otomatis. Pemadatan terjadi saat startup dan hanya sekali. Sekarang kamu akan melihat penggunaan data Blixt lebih sedikit.


#### Mode persisten


Terkadang orang tidak membuka Blixt dalam waktu lama, sehingga sinkronisasi memakan waktu lebih lama. Namun, mereka berharap bisa langsung tersinkronisasi saat membukanya.


Harap bersabar, dan perhatikan roda pemintalan di bagian atas. Opsional, kamu bisa pergi ke Opsi → Lihat Info Node dan memeriksa apakah tersinkronisasi ke rantai dan grafik, ditandai sebagai "true". Tanpa tanda "true", kamu tidak bisa menggunakan Blixt dengan benar, tidak bisa melihat saldo dengan tepat, saluran LN tidak akan online, dan kamu tidak bisa melakukan pembayaran.


Perbaikan cepat: Ada opsi ampuh untuk "menghidupkan" node Blixt-mu. Pergi ke Opsi → Eksperimen → pilih "Aktifkan Mode Persisten". Ini akan memulai ulang Blixt dan menempatkan layanan LND dalam mode persisten, alias selalu aktif dan menjaga sinkronisasi tetap online, bahkan jika kamu beralih ke aplikasi lain atau hanya menutup Blixt (bukan menutup paksa atau mematikan tugas). Kamu bisa mempertahankannya sepanjang hari jika koneksi stabil dan perlu menggunakan Blixt beberapa kali. Aplikasi ini tidak akan menghabiskan banyak baterai.



### KASUS 3 - SAYA INGIN BERMIGRASI KE PERANGKAT LAIN


Oke, tentang skenario ini saya menulis panduan ekstensif di [halaman FAQ](https://blixtwallet.github.io/faq#blixt-restore): dengan 2 pilihan, cepat (menutup saluran secara kooperatif sebelum migrasi) dan lambat (menutup saluran secara paksa karena perangkat lama mati).


Tetapi, aku ingin menegaskan kembali di sini, beberapa aspek penting dan menambahkan prosedur "rahasia" yang baru.


PENGINGAT:



- Selalu lakukan pencadangan status saluran (SCB) setelah kamu membuka atau menutup saluran. Hanya perlu beberapa detik untuk melakukannya.
- Jangan menyimpan file SCB yang lama, agar tidak bingung dan mengembalikannya. Sama sekali tidak berguna dan dapat memicu prosedur penalti jika kamu melihatnya. Selalu gunakan versi terakhir dari file SCB jika Anda melanjutkan untuk memulihkan.
- Simpan file SCB (berupa teks terenkripsi dengan ekstensi .bin) dari perangkat Anda, di tempat yang aman. Anda dapat menggunakan [LocalSend](https://github.com/localsend/localsend) untuk memindahkan file ini ke PC atau perangkat lain.
- Simpan juga seed dari Blixt Wallet Anda di tempat yang aman, misalnya pengelola kata sandi offline / USB terenkripsi.


Metode rahasia: Cara memigrasi node Blixt tanpa menutup saluran yang ada. Untuk ini, kamu perlu membaca dengan seksama bagian sebelumnya "Kontak Ketiga" dalam panduan ini tentang "Pulihkan Wallet".


Prosedur ini BUKAN UNTUK NOOB, ini hanya untuk pengguna tingkat lanjut! Itu sebabnya tidak terbuka secara luas dan aku sarankan untuk melakukannya hanya dengan bantuan dari pengembang Blixt atau dukungan. Tolong jangan abaikan saran ini.


### KASUS 4 - REKAN APA YANG DIGUNAKAN UNTUK MEMBUKA SALURAN?


Seperti yang saya tulis di [halaman panduan Blixt](https://blixtwallet.github.io/guides) ada banyak cara untuk membuka saluran dengan mobile LND ini. Tetapi beberapa aspek penting ingin saya ingatkan di sini:



- terbuka dengan node LSP yang terkenal dan dengan relay-relay yang dijamin oleh komunitas. [Lihat di sini daftarnya](https://github.com/hsjoberg/blixt-Wallet/issues/1033)
- Jangan membuka saluran dengan node Tor acak. Mereka tidak berguna dan hanya akan menyebabkan masalah saat melakukan pembayaran. Tidak peduli seberapa "handal" temanmu menjalankan node Tor yang buruk di hutan, itu tidak akan memberimu rute terbaik untuk node pribadi seluler. Kamu tidak membuka saluran hanya karena seseorang temanmu; ini bukan Facebook! Buka saluran untuk rute yang bagus, biaya rendah, dan ketersediaan tinggi.  
- Tidak perlu membuka banyak saluran kecil; cukup 2-3 atau maksimal 4, tapi dengan jumlah Sats yang cukup. Jangan membuka saluran kecil, itu sama sekali tidak berguna. Saluran di bawah 200k Sats untuk ponsel hampir tidak berguna.  
- Ingat LSP yang menawarkan saluran masuk dan saluran JIT (Just-In-Time). Ini sangat berguna karena kamu tidak perlu menggunakan UTXO-mu; kamu bisa membayar pembukaan saluran dengan dana yang sudah ada di dompet LN lain, menumpuknya, dan menyiapkannya untuk membuka saluran yang lebih besar. Gunakan saluran JIT sesuai kebutuhanmu.
 [Saya telah menjelaskan dalam panduan ini](https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) lebih banyak opsi untuk peer untuk node pribadi seperti Blixt. Juga [di sini, di panduan ini yang diposting di SN](https://stacker.news/items/679242/r/DarthCoin) saya menjelaskan cara mengelola likuiditas mobile node pribadi.


---

## Kesimpulan


Oke, ada banyak fitur luar biasa lain yang ditawarkan Blixt; aku akan membiarkanmu menemukannya satu per satu dan bersenang-senanglah.


Aplikasi ini benar-benar diremehkan, terutama karena tidak didukung pendanaan VC mana pun. Ini digerakkan oleh komunitas, dibangun dengan cinta dan semangat untuk Bitcoin dan Lightning Network.


Node LN mobile ini, Blixt, adalah alat yang sangat kuat di tangan banyak pengguna, jika mereka tahu cara menggunakannya dengan baik. Bayangkan saja, kamu berjalan keliling dunia membawa node LN di saku, dan tidak ada yang akan mengetahuinya.


Belum lagi semua fitur kaya lainnya yang menyertainya, yang hanya sedikit atau bahkan tidak ada yang bisa ditawarkan oleh aplikasi Wallet lain.


Sementara itu, berikut ini adalah semua tautan tentang Bitcoin Lightning Node yang menakjubkan ini:




- [Halaman Resmi Blixt](https://blixtwallet.com/)
- [Halaman Github Blixt](https://github.com/hsjoberg/blixt-Wallet/)
- [Halaman Fitur Blixt](https://blixtwallet.github.io/features) - menjelaskan satu per satu setiap fitur dan fungsionalitas.
- [Halaman FAQ Blixt](https://blixtwallet.github.io/faq) - Daftar tanya jawab dan pemecahan masalah Blixt
- [Halaman Panduan Blixt](https://blixtwallet.github.io/guides) - demo, tutorial video, panduan tambahan, dan kasus penggunaan untuk Blixt
- Unduh: [Android Play Store](https://play.google.com/store/apps/details?id=com.blixtwallet) | [iOS](https://testflight.apple.com/join/EXvGhRzS) | [Unduhan langsung APK](https://github.com/hsjoberg/blixt-Wallet/releases)
- [Grup Telegram untuk dukungan langsung](https://t.me/blixtwallet)
- [Twitter](https://twitter.com/BlixtWallet)
- [Halaman crowdfunding Geyser](https://geyser.fund/project/blixt) - donasikan Sats sesuai keinginan Anda untuk mendukung proyek ini
- [LNURL Chat Blixt](https://chat.blixtwallet.com/) - obrolan LN anonim
- [Blixt presentation - promo video](https://lightning.video/06fdf68f99e246a6ec6ba1470677b9e632faaad4aa0ca9773c38714b682a4ac1)
- [Blixt Girls Calendar](https://lightning.video/eeb744202ad3f14c18bf6d719970ebd9c53f0f13b79c94d299c6be623fba64b6) - video promo (Anda dapat menguji penggunaan pertama LN)
- [Selebaran A4 yang dapat dicetak dengan langkah pertama menggunakan Blixt, dalam berbagai bahasa](https://github.com/BlixtWallet/blixtwallet.github.io/tree/master/assets/flyer).
- [Blixt juga menawarkan demo fungsional penuh](https://blixt-Wallet-git-master-hsjoberg.vercel.app/) langsung di situs webnya atau di web versi khusus, untuk mendapatkan pengujian pengalaman penuh, sebelum mulai menggunakan di dunia nyata.


---
**PERHATIAN:**


*Saya tidak dibayar atau didukung dengan cara apa pun oleh pengembang aplikasi ini. Saya menulis panduan ini karena saya melihat minat terhadap aplikasi Wallet ini semakin meningkat dan pengguna baru masih belum mengerti bagaimana cara memulainya. Juga untuk membantu Hampus (pengembang utama) dengan dokumentasi tentang penggunaan node Wallet.*


*Saya tidak memiliki kepentingan lain dalam mempromosikan aplikasi LN ini, selain mendorong adopsi Bitcoin dan LN. Ini adalah satu-satunya cara!*


---
