---
name: Blixt Wallet
description: Bagaimana cara mulai menggunakan node LN yang kuat di ponsel Anda?
---
![cover](assets/cover.webp)


Panduan ini didedikasikan untuk semua pengguna baru yang ingin mulai menggunakan Bitcoin Lightning Network (LN) dengan sumber terbuka GRATIS, dengan cara NON-KUSTODIAL.


Menggunakan [Blixt Wallet](https://blixtwallet.com/), sebuah node LN penuh di ponsel Anda, di mana pun Anda berada.


Jika Anda belum pernah menggunakan Bitcoin Lightning Network, sebelum memulai, [silakan baca analogi penjelasan sederhana tentang Lightning Network (LN)](https://darth-coin.github.io/beginner/LN-airport-analogy-en.html).


## ASPEK-ASPEK PENTING:



- Blixt adalah sebuah simpul privat, BUKAN simpul perutean! Ingatlah itu: Itu berarti, semua saluran LN di Blixt akan diumumkan ke grafik LN (disebut saluran pribadi). Itu berarti, NODE INI TIDAK AKAN MELAKUKAN ROUTING pembayaran orang lain melalui node Blixt. Node Blixt ini BUKAN untuk perutean, saya ulangi. Ini terutama untuk dapat mengelola saluran LN Anda sendiri dan melakukan pembayaran LN Anda secara pribadi, kapan pun Anda butuhkan. Node Blixt ini harus online dan disinkronkan HANYA SEBELUM Anda akan melakukan transaksi. Itulah mengapa Anda akan melihat ikon di atas yang menunjukkan status sinkronisasi. Ini hanya membutuhkan beberapa saat, tergantung berapa lama Anda menyimpannya secara offline.



- Blixt menggunakan LND (aezeed) sebagai backend Wallet, jadi jangan coba-coba mengimpor jenis dompet Bitcoin lainnya ke dalamnya. [Di sini Anda telah menjelaskan jenis-jenis Wallet Mnemonic](https://coldbit.com/what-types-of-Mnemonic-seeds-are-used-in-Bitcoin/). Dan berikut ini adalah [daftar yang lebih lengkap dari semua jenis wallet](https://walletsrecovery.org/). Jadi, jika sebelumnya Anda memiliki node LND, Anda dapat mengimpor seed dan backup.channels ke dalam Blixt, [seperti yang dijelaskan dalam panduan ini](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html).



- Di akhir panduan ini, Anda akan menemukan bagian khusus yang berisi ["tips dan trik"](https://darth-coin.github.io/wallets/getting-started-blixt-Wallet-en.html#tips)



- Tautan penting Blixt - lihat di bagian akhir panduan ini, silakan tandai.


---

## Blixt - Kontak Pertama


Jadi... Ibu Darth memutuskan untuk mulai menggunakan LN dengan Blixt. Keputusan Hard, tapi bijaksana. Blixt hanya untuk orang-orang pintar dan mereka yang benar-benar ingin belajar lebih banyak, penggunaan LN yang mendalam.


![blixt](assets/en/01.webp)


Darth memperingatkan ibunya:


"*Ibu, jika Anda mulai menggunakan Blixt LN Node, Anda harus terlebih dahulu mengetahui apa itu Lightning Network dan bagaimana cara kerjanya, setidaknya pada tingkat dasar. [Di sini saya mengumpulkan daftar sumber daya sederhana tentang Lightning Network](https://blixtwallet.github.io/faq#what-is-LN). Silakan baca terlebih dahulu.*"


Ibu Darth membaca sumber-sumber yang ada dan melakukan langkah pertama: memasang Blixt pada perangkat Android barunya. Blixt juga tersedia untuk iOS dan macOS (desktop). Tetapi itu bukan untuk Darth's Mom... Meskipun demikian, disarankan untuk menggunakan versi Android yang lebih baru, setidaknya 9 atau 10 untuk kompatibilitas dan pengalaman yang lebih baik. Menjalankan node LN secara penuh pada perangkat seluler bukanlah tugas yang mudah dan dapat menghabiskan banyak ruang (min 600MB) dan memori.


Setelah Anda membuka Blixt, layar "Selamat Datang" akan memberi Anda beberapa opsi:


![blixt](assets/en/02.webp)


Di sudut kanan atas, Anda akan melihat 3 titik yang mengaktifkan menu:



- "aktifkan Tor" - pengguna dapat memulai dengan jaringan Tor, secara khusus jika ingin memulihkan node LND lama yang berjalan dengan rekan-rekan Tor saja.
- "Set Bitcoin node" - jika pengguna ingin terhubung ke node-nya sendiri secara langsung, untuk menyinkronkan blok melalui Neutrino, dapat melakukannya langsung dari layar selamat datang. Opsi ini juga bagus jika koneksi internet atau Tor Anda tidak begitu stabil untuk terhubung ke node Bitcoin default (node.blixtwallet.com).
- Dalam waktu dekat akan ditambahkan bahasa di sana, sehingga pengguna dapat langsung memulai dengan bahasa yang nyaman. Jika Anda ingin berkontribusi pada proyek open source ini dengan menerjemahkan ke bahasa lain, [silakan bergabung di sini](https://explore.transifex.com/blixt-Wallet/blixt-Wallet/).


### OPSI A - Buat Wallet baru


Jika Anda memilih untuk "membuat Wallet baru", Anda akan langsung diarahkan ke layar utama Blixt Wallet.


Ini adalah "kokpit" Anda dan juga merupakan "LN Wallet Utama", jadi harap diperhatikan, ini hanya akan menunjukkan kepada Anda saldo LN Wallet Anda. Wallet onchain ditampilkan secara terpisah (lihat C).


![blixt](assets/en/03.webp)


A - Ikon indikator sinkronisasi blok Blixt. Ini adalah hal yang paling penting untuk node LN: untuk disinkronkan dengan jaringan. Jika ikon tersebut masih berfungsi, berarti node Anda BELUM SIAP! Jadi bersabarlah, khususnya untuk sinkronisasi awal pertama. Ini bisa memakan waktu hingga 6-8 menit, tergantung pada perangkat dan koneksi internet Anda.


Anda bisa mengekliknya dan melihat status sinkronisasi:


![blixt](assets/en/04.webp)


Anda juga dapat mengklik tombol "Tampilkan Log LND" (A) jika Anda ingin melihat dan membaca lebih banyak detail teknis dari log LND, secara real time. Sangat berguna untuk melakukan debug dan mempelajari lebih lanjut cara kerja LN.


B - Di sini Anda dapat mengakses semua Pengaturan Blixt, dan banyak sekali! Blixt menawarkan banyak fitur dan opsi yang kaya untuk mengelola node LN Anda seperti seorang profesional. Semua opsi tersebut dijelaskan secara rinci di "[Halaman Fitur Blixt](https://blixtwallet.github.io/features#blixt-options) - Menu Opsi".


C - Di sini Anda memiliki menu "Laci Ajaib", [juga dijelaskan secara rinci di sini](https://blixtwallet.github.io/features#blixt-drawer). Di sini terdapat "Onchain Wallet" (B), Saluran Petir (C), Kontak, ikon status Saluran (A), Keysend (D).


![blixt](assets/en/05.webp)


D - Adalah menu bantuan, dengan tautan ke halaman FAQ/Panduan, kontak pengembang, halaman Github, dan grup dukungan Telegram.


E - Tunjukkan BTC Address pertama Anda, tempat Anda dapat menyetor Sats pengujian pertama Anda. INI OPSIONAL! Jika Anda menyetor langsung ke Address tersebut, berarti Anda membuka saluran LN menuju Blixt Node. Itu berarti Anda akan melihat Sats yang Anda setorkan, masuk ke transaksi onchain (tx) lain, untuk membuka saluran LN tersebut. Anda dapat memeriksanya di Blixt onchain Wallet (lihat poin C), dengan mengklik menu TX di kanan atas.


![blixt](assets/en/06.webp)


Seperti yang dapat Anda lihat di Log Transaksi Onchain, langkah-langkahnya sangat terperinci yang menunjukkan ke mana arah Sats (deposit, buka, tutup saluran).


REKOMENDASI:


Setelah menguji beberapa situasi, kami sampai pada kesimpulan bahwa jauh lebih efisien untuk membuka saluran antara 1 dan 5 M Sats. Saluran yang lebih kecil cenderung cepat habis dan membayar biaya yang lebih tinggi dibandingkan dengan saluran yang lebih besar.


F - Menunjukkan saldo Lightning Wallet utama Anda. Ini BUKAN total saldo Blixt Wallet Anda, ini hanya mewakili Sats yang Anda miliki di Lightning Channels, yang tersedia untuk dikirim. Seperti yang ditunjukkan sebelumnya, Onchain Wallet terpisah. Ingatlah aspek ini. Onchain Wallet terpisah karena alasan penting: digunakan terutama untuk membuka/menutup saluran LN.


Baiklah, sekarang Ibu Darth telah menyetorkan sejumlah Sats ke dalam onchain Address yang ditampilkan di layar utama. Disarankan ketika Anda melakukan hal tersebut, agar aplikasi Blixt Anda tetap online dan aktif untuk sementara waktu, hingga BTC tx diambil oleh para penambang ke dalam blok pertama.


Setelah itu dapat memakan waktu hingga 20-30 menit hingga sepenuhnya dikonfirmasi dan saluran terbuka dan Anda akan melihatnya di Laci Ajaib - Saluran Petir sebagai aktif. Titik kecil berwarna di atas laci, jika Green akan menunjukkan bahwa saluran LN Anda sedang online dan siap digunakan untuk mengirim Sats melalui LN.


Address dan pesan selamat datang yang ditampilkan akan menghilang. Tidak perlu lagi membuka saluran otomatis sekarang. Anda juga dapat menonaktifkan opsi ini di menu Pengaturan.


Saatnya untuk melanjutkan, menguji fitur dan opsi lain untuk membuka saluran LN.


Sekarang, mari kita buka saluran lain dengan peer node lain. Komunitas Blixt menempatkan togheter [daftar node yang baik untuk mulai digunakan dengan Blixt](https://github.com/hsjoberg/blixt-Wallet/issues/1033).


**Prosedur untuk membuka saluran LN di Blixt**


Ini sangat sederhana, hanya perlu beberapa langkah dan sedikit kesabaran:



- Masuk ke daftar rekan kerja [Komunitas Blixt](https://github.com/hsjoberg/blixt-Wallet/issues/1033)
- Pilih simpul dan klik tautan judul namanya, simpul tersebut akan membuka halaman Amboss
- Klik untuk menampilkan kode QR untuk node URI Address


![blixt](assets/en/07.webp)


Buka Blixt dan pergi ke laci atas - Saluran Petir dan klik tombol "+"


![blixt](assets/en/08.webp)


Sekarang, klik (A) kamera untuk memindai kode QR dari halaman Amboss dan detail node akan terisi. Tambahkan jumlah Sats untuk saluran yang Anda inginkan dan kemudian pilih tarif biaya untuk tx. Anda dapat membiarkannya otomatis (B) untuk konfirmasi yang lebih cepat atau menyesuaikannya secara manual dengan menggeser tombol. Anda juga dapat menekan lama angka dan mengeditnya sesuka Anda.


Jangan memasang kurang dari 1 sat/vbyte! Biasanya lebih baik untuk berkonsultasi dengan [biaya Mempool](https://Mempool.space/) sebelum membuka saluran dan memilih biaya yang sesuai.


Selesai, sekarang tinggal klik tombol "buka saluran" dan tunggu 3 konfirmasi, yang biasanya memakan waktu 30 menit (1 blok kira-kira setiap 10 menit).


Setelah dikonfirmasi, Anda akan melihat saluran yang aktif di bagian "Saluran Petir".


---

## Blixt - Kontak Kedua


Baiklah, sekarang kita memiliki saluran LN dengan likuiditas yang hanya OUTBOUND. Itu berarti kita hanya dapat MENGIRIM, kita masih tidak dapat MENERIMA Sats melalui LN.


![blixt](assets/en/09.webp)


Kenapa? Apakah Anda sudah membaca panduan yang ditunjukkan di awal? Tidak? Kembalilah dan bacalah. Sangat penting untuk memahami cara kerja saluran LN.


![blixt](assets/en/10.webp)


Seperti yang Anda lihat pada contoh ini, saluran yang dibuka dengan setoran pertama, tidak memiliki terlalu banyak likuiditas INBOUND ("Dapat menerima") tetapi memiliki banyak likuiditas OUTBOUND ("Dapat mengirim").


Jadi, opsi apa yang Anda miliki, jika Anda ingin menerima lebih banyak Sats daripada LN?



- Habiskan beberapa Sats dari saluran yang ada. Ya, LN adalah jaringan pembayaran dari Bitcoin, yang digunakan terutama untuk membelanjakan Sats Anda dengan lebih cepat, lebih murah, privat, dan mudah. LN BUKAN cara hodling, untuk itu Anda memiliki onchain Wallet.



- Tukar beberapa Sats, kembali ke dalam onchain Wallet Anda, dengan menggunakan layanan submarine swap. Dengan cara ini, Anda tidak menghabiskan Sats Anda, tetapi mengembalikannya ke onchain Wallet Anda sendiri. Di sini Anda dapat melihat secara detail beberapa metode, di [Halaman Panduan Blixt](https://blixtwallet.github.io/guides).



- Buka saluran INBOUND dari penyedia LSP mana pun. Berikut ini adalah demo video tentang cara menggunakan LNBig LSP untuk membuka saluran inbound. Itu berarti, Anda akan membayar sedikit biaya untuk saluran KOSONG (di sisi Anda) dan Anda akan dapat menerima lebih banyak Sats ke dalam saluran tersebut. Jika Anda adalah pedagang yang menerima lebih banyak daripada membelanjakan, itu adalah pilihan yang bagus. Juga jika Anda membeli Sats di atas LN, menggunakan Robosats atau LN Exchange lainnya.



- Buka saluran Dunder, dengan node Blixt atau penyedia LSP Dunder lainnya. Saluran Dunder adalah cara sederhana untuk mendapatkan likuiditas INBOUND, tetapi pada saat yang sama Anda menyetor sejumlah Sats ke dalam saluran tersebut. Hal ini juga bagus karena akan membuka saluran dengan [UTXO](https://en.Bitcoin.it/wiki/UTXO) yang bukan berasal dari Blixt Wallet Anda. Hal ini akan menambah privasi. Juga bagus karena, jika anda tidak memiliki Sats ke dalam onchain Wallet, untuk membuka saluran LN normal, tetapi anda memilikinya ke dalam LN Wallet lainnya, anda dapat membayar dari Wallet lainnya melalui LN pembukaan dan deposit (di sisi anda) saluran Dunder tersebut. [Lebih detail cara kerja Dunder dan cara menjalankan server Anda sendiri di sini](https://github.com/hsjoberg/dunder-lsp).


![blixt](assets/en/11.webp)


Berikut adalah langkah-langkah untuk mengaktifkan pembukaan saluran Dunder:



- Buka Pengaturan, di bagian "Eksperimen" aktifkan kotak untuk "Aktifkan Dunder LSP".
- Setelah Anda melakukannya, kembali ke bagian "Lightning Network" dan Anda akan melihat opsi "Set Dunder LSP Server". Di sana, secara default diatur "https://dunder.blixtwallet.com" tetapi Anda dapat mengubahnya dengan penyedia LSP Dunder lainnya Address. [Berikut adalah daftar komunitas Blixt](https://github.com/hsjoberg/blixt-Wallet/issues/1033) dengan node yang dapat menyediakan saluran LSP Dudner untuk Blixt Anda.
- Sekarang Anda dapat masuk ke layar utama dan klik tombol "Terima". Kemudian ikuti prosedur ini [dijelaskan dalam panduan ini](https://blixtwallet.github.io/guides#guide-lsp).


Oke, jadi setelah saluran Dunder dikonfirmasi (akan memakan waktu beberapa menit) Anda akan mendapatkan 2 saluran LN: satu saluran yang dibuka dengan autopilot (saluran A) dan satu saluran dengan likuiditas yang lebih banyak, dibuka dengan Dunder (saluran B).


![blixt](assets/en/12.webp)


Bagus, sekarang Anda sudah siap untuk mengirim dan menerima cukup banyak Sats melalui LN!


SELAMAT DATANG PETIR Bitcoin!


---

## Blixt - Kontak Ketiga


Ingat, pada bab satu "Kontak Pertama" ada 2 pilihan di layar Selamat Datang:


- [Opsi A](https://darth-coin.github.io/wallets/getting-started-blixt-Wallet-en.html#option-a) - Buat Wallet baru
- Opsi B - Pulihkan Wallet


Jadi sekarang mari kita bahas tentang cara memulihkan Blixt Wallet atau node LND yang rusak. Ini sedikit lebih teknis, tetapi mohon diperhatikan. Bukankah itu Hard.


### OPSI B - Kembalikan Wallet


Di masa lalu saya menulis panduan khusus tentang [cara memulihkan node Umbrel yang rusak](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html), di mana saya juga menyebutkan metode menggunakan Blixt sebagai proses pemulihan cepat, menggunakan file seed + channel.backup dari Umbrel.


Saya juga menulis panduan cara memulihkan node Blixt Anda atau memigrasi Blixt Anda ke perangkat lain, [di sini](https://blixtwallet.github.io/faq#blixt-restore).


![blixt](assets/en/13.webp)


Namun, mari kita jelaskan secara sederhana proses ini. Seperti yang dapat Anda lihat pada gambar di atas, ada 2 hal yang harus Anda lakukan untuk memulihkan node Blixt/LND sebelumnya:



- kotak teratas adalah tempat Anda harus mengisi dengan semua 24 kata dari seed Anda (simpul lama / mati)
- di bagian bawah terdapat dua pilihan tombol untuk memasukkan/mengunggah file channel.backup, yang sebelumnya disimpan dari node Blixt/LND Anda yang lama. Bisa dari berkas lokal (Anda mengunggahnya ke perangkat Anda sebelumnya) atau bisa juga dari lokasi jarak jauh Google drive / iCloud. Blixt memiliki opsi ini untuk menyimpan cadangan saluran Anda secara langsung ke dalam drive Google / iCloud. Lihat detail lebih lanjut di [Halaman Fitur Blixt](https://blixtwallet.github.io/features#blixt-options).


Namun demikian, jika sebelumnya Anda tidak mempunyai saluran LN yang terbuka, tidak perlu meng-upload file channels.backup. Cukup masukkan 24 kata seed dan tekan tombol restore.


Jangan lupa untuk mengaktifkan Tor, dari menu 3 titik teratas, seperti yang kami jelaskan di bagian Opsi A. Itu adalah kasus ketika Anda HANYA memiliki rekan Tor dan tidak dapat dihubungi melalui clearnet (domain/IP). Selain itu tidak perlu.


Fitur lain yang berguna adalah mengatur node Bitcoin tertentu dari menu atas tersebut. Secara default, ia menyinkronkan blok dari node.blixtwallet.com (mode neutrino), tetapi Anda dapat mengatur node Bitcoin lainnya yang menyediakan sinkronisasi neutrino.


Jadi, setelah Anda mengisi opsi-opsi tersebut, dan menekan tombol restore, Blixt akan mulai menyinkronkan blok-blok tersebut melalui Neutrino seperti yang telah kami jelaskan di bab Kontak Pertama. Jadi bersabarlah dan perhatikan proses pemulihan di layar utama, dengan mengklik ikon sinkronisasi.


![blixt](assets/en/14.webp)


Seperti yang dapat Anda lihat pada contoh ini, ini menunjukkan bahwa blok Bitcoin telah tersinkronisasi 100% (A) dan proses pemulihan sedang berjalan (B). Itu berarti saluran LN yang Anda miliki sebelumnya, akan ditutup dan dana akan dipulihkan ke dalam onchain Blixt Wallet Anda.


Proses ini membutuhkan waktu! Jadi harap bersabar dan usahakan agar Blixt Anda tetap aktif dan online. Sinkronisasi awal dapat memakan waktu hingga 6-8 menit dan penutupan saluran dapat memakan waktu hingga 10-15 menit. Jadi, sebaiknya Anda mengisi daya perangkat dengan baik.


Setelah proses ini dimulai, Anda dapat memeriksa di Laci Ajaib - Saluran Petir, status masing-masing saluran Anda sebelumnya, yang menunjukkan bahwa mereka dalam status "menunggu penutupan". Setelah setiap saluran ditutup, Anda dapat melihat tx penutupan di onchain Wallet (lihat Laci Ajaib - Onchain), dan membuka log menu tx.


![blixt](assets/en/15.webp)


Juga akan lebih baik untuk memeriksa dan menambahkan jika tidak ada, rekan-rekan Anda sebelumnya yang Anda miliki di node LN lama Anda. Jadi pergi ke menu Pengaturan, ke "Lightning Network" dan masuk ke opsi "Tampilkan Rekan Petir".


![blixt](assets/en/16.webp)


Di dalam bagian ini Anda akan melihat peer yang terhubung dengan Anda pada saat itu dan Anda dapat menambahkan lebih banyak lagi, lebih baik menambahkan yang sudah Anda miliki salurannya sebelumnya. Cukup buka [halaman Amboss](https://amboss.space/), cari node peer alias atau nodeID Anda dan pindai URI node mereka.


![blixt](assets/en/17.webp)


Seperti yang Anda lihat pada gambar di atas, terdapat 3 aspek:


A - mewakili simpul clearnet Address URI (domain/IP)


B - mewakili simpul bawang Tor Address URI (.onion)


C - adalah kode QR untuk dipindai dengan kamera Blixt Anda atau tombol salin.


URI node Address ini harus Anda tambahkan ke dalam daftar peer Anda. Jadi, perlu diketahui bahwa tidak cukup hanya nama alias simpul atau nodeID saja.


Sekarang Anda dapat pergi ke Magic Drawer (menu kiri atas) - Lightning Channels, dan Anda dapat melihat pada tingkat blok jatuh tempo mana dana akan dikembalikan ke dalam onchain Address Anda.


![blixt](assets/en/18.webp)


Nomor blok 764272 adalah saat dana akan dapat digunakan di Bitcoin onchain Address Anda. Dan itu bisa memakan waktu hingga 144 blok dari blok konfirmasi pertama hingga dirilis. [Jadi, periksa di Mempool](https://Mempool.space/).


Dan hanya itu saja. Tunggu saja dengan sabar hingga semua saluran ditutup dan dana kembali ke onchain Wallet Anda.


👉 **Metode pemulihan rahasia :**


Ada metode lain untuk memulihkan node Blixt LND Anda tanpa harus menutup saluran. Tetapi tersembunyi dari pengguna noob biasa, karena metode ini HANYA untuk mereka yang tahu apa yang mereka lakukan.


Jika Anda perlu memigrasikan node Blixt Anda yang sudah ada (yang masih berfungsi) ke perangkat baru, tanpa menutup saluran LN yang sudah ada, Anda harus melakukan langkah-langkah berikut:



- Kami berasumsi bahwa Anda telah menyimpan Blixt Wallet seed (24 kata aezeed)
- Pada perangkat lama, buka "Pengaturan" - bagian debug - "Compact LND database". Langkah ini opsional tetapi disarankan jika Anda menginginkan ukuran file channel.db yang lebih kecil. Biasanya cukup besar, tergantung aktivitas node Anda. Ini akan memulai ulang Blixt dan memadatkan ukuran file db.
- Setelah dimulai ulang, buka "Pengaturan" dan ubah nama alias reguler Anda menjadi "Hampus". Ini akan mengaktifkan opsi tersembunyi, hanya untuk pengguna tingkat lanjut.
- Pergi ke bagian "Debug" dan Anda akan melihat opsi baru "Ekspor file channel.db". PERINGATAN! Setelah Anda melakukan ekspor ini, node Blixt LN yang ada akan dinonaktifkan pada perangkat lama dan akan mengekspor seluruh basis data node (channel.db) yang siap untuk diimpor ke perangkat baru.
- File db ini akan disimpan ke dalam folder yang telah ditentukan di perangkat lama Anda (Dokumen atau Unduhan) dan dari sana Anda harus memindahkannya ke perangkat baru Anda. Anda bisa menggunakan misalnya [aplikasi LocalSend FOSS](https://github.com/localsend/localsend) untuk mentransfer file secara langsung antar perangkat.
- Pada saat ini Blixt lama Anda HARUS tetap ditutup. JANGAN DIBUKA LAGI!
- Setelah Anda mentransfer file channel.db ke perangkat baru, mulai instalasi baru Blixt dan pilih "Restore Wallet" di layar pertama.
- Pada tombol yang bertuliskan "Pilih file SCB" tekan lama (BUKAN klik saja!) dan Anda akan melihat pilihan untuk memilih file channel.db di mana Anda menyimpannya secara lokal di perangkat baru. Jika Anda hanya menekan tombol tersebut, maka secara default akan menggunakan file SCB (dengan menutup saluran), tidak dapat digunakan untuk pencadangan saluran siaran langsung.
- Masukkan 24 kata seed lalu klik "Pulihkan"
- Anda akan melihat bahwa Blixt akan mulai melakukan sinkronisasi dengan Neutrino. Anda juga dapat melihat log sinkronisasi.
- INGAT! Usahakan agar Blixt tetap terbuka sepanjang waktu pada fase ini! Jangan biarkan ia masuk ke mode tidur atau menutup layar aplikasi. Hal itu dapat mengganggu sinkronisasi awal dan Anda harus melakukannya lagi. Tunggu dengan sabar, tidak memakan waktu lebih dari beberapa menit.
- Setelah sinkronisasi blok awal selesai, ia akan segera memindai alamat Wallet Anda sebelumnya dan saluran Anda akan kembali online, hidup dan sehat.
- Sayangnya, riwayat pembayaran dan kontak sebelumnya tidak dapat (belum) dikembalikan. Tapi itu tidak terlalu penting.


Dan SELESAI! Sekarang Anda memiliki node Blixt LN yang telah dipulihkan sepenuhnya. Ini juga dapat bekerja dengan cadangan LND lainnya (Umbrel, Raspiblitz, dll) jika Anda menyimpan dengan benar file channel.db sebelumnya. Jadi Blixt benar-benar dapat menyimpan node LND yang mati.


---

## Blixt - Kontak Keempat


Bab ini adalah tentang kustomisasi dan mengenal Blixt Node dengan lebih baik. Saya tidak akan menjelaskan semua fitur yang tersedia, karena terlalu banyak dan sudah dijelaskan di [Halaman Fitur Blixt](https://blixtwallet.github.io/features).


Tetapi saya akan menunjukkan beberapa hal yang diperlukan untuk terus menggunakan Blixt Anda dan mendapatkan pengalaman yang luar biasa.


### A - Nama (NameDesc)


![blixt](assets/en/19.webp)


[NamDesc](https://github.com/lightning/blips/blob/master/blip-0011.md) adalah standar untuk menyampaikan "nama penerima" dalam faktur BOLT11.


Ini bisa berupa nama apa saja dan dapat diubah kapan saja.


Opsi ini sangat berguna dalam berbagai kasus, ketika Anda ingin mengirim nama bersama dengan deskripsi Invoice, sehingga penerima dapat memiliki petunjuk dari siapa yang menerima Sats tersebut. Ini sepenuhnya opsional dan juga pada layar pembayaran, pengguna harus mencentang kotak yang menunjukkan untuk mengirim nama alias.


Berikut ini adalah contoh tampilan yang akan muncul ketika Anda menggunakan [chat.blixtwallet.com](https://chat.blixtwallet.com/)


![blixt](assets/en/20.webp)


Ini adalah contoh lain pengiriman ke aplikasi Wallet lain yang mendukung NameDesc:


![blixt](assets/en/21.webp)


### B - Kotak Petir


Dimulai dengan v0.6.9-420 yang baru [baru-baru ini diumumkan](https://github.com/hsjoberg/blixt-Wallet/releases/tag/v0.6.9-420), Blixt memperkenalkan fitur baru yang kuat untuk Lightning Address di Blixt.


Fitur baru ini bersifat opsional, tidak AKTIF secara default!


Untuk saat ini, LN Box default dijalankan oleh server Blixt dan menawarkan @blixtwallet.com LN Address. Tetapi SIAPAPUN yang memiliki node publik LND dapat menjalankan server Lightning Box dan menawarkan LN Address untuk domainnya sendiri, penyimpanan sendiri.


Saat ini, server Blixt hanya meneruskan pembayaran yang dikirim ke alamat LN @blixtwallet.com ke pengguna Blixt yang mengatur LN Address mereka. Pengguna harus menempatkan node Blixt mereka Wallet dalam "mode persisten" untuk menerima pembayaran ini ke alamat LN @blixtwallet.com.


Lihat dalam catatan rilis video demo tentang cara mengatur LN Address Anda di Blixt.


LN Address yang diimplementasikan ke dalam aplikasi Blixt Wallet ini, seperti chatting melalui LN, instan dan menyenangkan, juga mendukung [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (menambahkan nama alias ke pembayaran). Anda dapat menambahkan dalam daftar kontak semua alamat LN biasa yang sering Anda gunakan dan siap sedia untuk mengobrol. Sekarang Blixt dapat dianggap sebagai aplikasi obrolan LN yang lengkap 😂😂.


Fitur lain yang berguna adalah dukungan penuh terhadap LUD-18 (yang juga didukung oleh [Stacker.News](https://stacker.news/r/DarthCoin) dan yang lainnya).


![blixt](assets/en/22.webp)


Seperti yang dapat Anda lihat pada tangkapan layar di atas, pengiriman dari akun Stacker News, menampilkan logo + LN Address + pesan dengan baik. Cara yang sama juga berlaku untuk mengirim dari Blixt, Anda dapat melampirkan Blixt LN Address Anda atau cukup menambahkan nama alias (yang sebelumnya diatur dalam pengaturan Blixt) atau bahkan keduanya.


Opsi dari LUD-18 ini dapat berguna juga untuk layanan berlangganan, di mana pengguna dapat mengirimkan alias tertentu (BUKAN nama alias node Anda atau nama asli Anda!) dan berdasarkan hal tersebut Anda dapat didaftarkan atau menerima kembali pesan tertentu atau apa pun. Melampirkan nama alias ([LUD-18](https://github.com/lnurl/luds/blob/luds/18.md)) + komentar ([LUD-12](https://github.com/lnurl/luds/blob/luds/12.md)) pada pembayaran LN dapat memiliki beberapa kasus penggunaan!


Berikut ini adalah kode untuk [Lightning Box](https://github.com/hsjoberg/lightning-box) jika Anda menjalankannya untuk Anda sendiri, untuk keluarga dan teman Anda, di node Anda sendiri.


Di sini Anda juga dapat menjalankan [LSP Dunder server](https://github.com/hsjoberg/dunder-lsp) untuk node seluler Blixt dan menawarkan likuiditas untuk pengguna Blixt jika Anda memiliki node LN publik yang baik (hanya berfungsi dengan LND).


### C - Cadangan Saluran LN dan kata seed


Ini adalah fitur yang sangat penting!


Setelah membuka atau menutup saluran LN, Anda harus melakukan pencadangan. Hal ini dapat dilakukan secara manual dengan menyimpan file kecil di perangkat lokal (biasanya folder unduhan) atau menggunakan akun Google Drive atau iCloud.


![blixt](assets/en/23.webp)


Buka bagian Pengaturan Blixt - Wallet. Di sana Anda memiliki opsi untuk menyimpan semua data penting untuk Blixt Wallet Anda:



- "Tampilkan Mnemonic" - akan menampilkan 24 kata seed untuk menuliskannya
- "Hapus Mnemonic dari perangkat" - ini opsional dan gunakan hanya jika Anda benar-benar ingin menghapus kata seed dari perangkat Anda. Ini TIDAK akan menghapus Wallet Anda, hanya seed. Namun perlu diketahui! Tidak ada cara untuk memulihkannya jika Anda tidak menuliskannya terlebih dahulu.
- "Export channel backup" - opsi ini akan menyimpan file kecil di perangkat lokal Anda, biasanya ke dalam folder "download", dari mana Anda dapat mengambilnya dan memindahkannya ke luar perangkat, untuk disimpan dengan aman.
- "Verifikasi cadangan saluran" - ini adalah opsi yang baik jika Anda menggunakan Google drive atau iCloud untuk memeriksa integritas cadangan yang dilakukan dari jarak jauh.
- " Cadangan saluran Google drive" - akan menyimpan file cadangan ke dalam Google drive pribadi Anda. File ini dienkripsi dan disimpan di tempat penyimpanan terpisah dari file google Anda yang biasa. Jadi tidak ada kekhawatiran yang dapat dibaca oleh siapa pun. Bagaimanapun juga file tersebut sama sekali tidak berguna tanpa kata-kata seed, jadi tidak ada yang bisa mengambil dana Anda hanya dari file tersebut.


Saya akan merekomendasikan untuk bagian ini yang berikut ini:



- gunakan pengelola kata sandi untuk menyimpan dengan aman seed dan file cadangan Anda. KeePass atau Bitwarden sangat bagus untuk itu dan bisa digunakan pada multiplatform dan di-host sendiri atau offline.
- LAKUKAN CADANGAN SETIAP KALI Anda membuka atau menutup saluran. File tersebut akan diperbarui dengan info saluran. Anda tidak perlu melakukannya setelah setiap transaksi yang Anda lakukan pada LN. Pencadangan saluran tidak menyimpan info tersebut, hanya menyimpan status saluran.


![blixt](assets/en/24.webp)


---

## Blixt - Kiat dan Trik


### KASUS 1 - MASALAH SINKRONISASI


"_Blixt saya tidak tersinkronisasi... Blixt saya tidak menunjukkan saldo... Blixt saya tidak dapat membuka saluran... Saya mencoba memulihkannya di perangkat lain... dll."


Semua masalah ini dimulai karena PERANGKAT ANDA TIDAK TERSINKRONISASI DENGAN BENAR. Harap pahami aspek penting ini: Blixt adalah node LND seluler, yang menggunakan Neutrino untuk menyinkronkan/membaca blok.



- Berikut ini penjelasan yang tidak terlalu teknis dari [Majalah Bitcoin](https://bitcoinmagazine.com/technical/why-Bitcoin-wallets-need-block-filters)
- Berikut ini adalah sumber daya teknis lebih lanjut dari [Bitcoin Optech](https://bitcoinops.org/en/topics/compact-block-filters/)
- Berikut ini adalah bagaimana Anda dapat mengaktifkan Neutrino di node rumah Anda sendiri dan melayani filter blok untuk node seluler Anda, dari [Docs Lightning Engineering](https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core)


PERINGATAN: Menggunakan Neutrino melalui clearnet benar-benar aman, IP atau xpub Anda tidak akan bocor. Anda hanya membaca blok dari node jarak jauh dengan neutrino. Itu saja. Sisanya dilakukan di perangkat lokal Anda.


Jadi TIDAK PERLU menggunakannya dengan Tor. Tor akan menambah latensi yang sangat besar pada proses sinkronisasi Anda dan akan membuat Blixt Anda menjadi sangat tidak stabil. Jika Anda benar-benar ingin menggunakan melalui Tor, pastikan apa yang Anda lakukan dan memiliki koneksi yang baik dan kesabaran. Kasus yang sama untuk menggunakan VPN. Berhati-hatilah dengan latensi yang diberikan pada Anda dari VPN tersebut.


Anda dapat menguji latensi server neutrino hanya dengan melakukan ping, dari PC atau ponsel Anda.


![blixt](assets/en/25.webp)


Ini adalah ping biasa ke server neutrino europe.blixtwallet.com, ini menunjukkan bahwa koneksi sangat bagus dengan waktu respons rata-rata 50ms dan TTL 51. Waktu respons dapat bervariasi tetapi tidak terlalu banyak. TTL harus stabil.


Jika nilai ini lebih tinggi dari 100-150ms maka proses sinkronisasi Anda akan macet atau lebih buruk lagi, dapat menyebabkan saluran tertutup oleh rekan-rekannya! Jangan abaikan aspek ini.


Tanpa sinkronisasi yang tepat, Anda juga tidak dapat melihat keseimbangan yang benar atau saluran LN Anda tidak akan online dan beroperasi. Tidak peduli berapa giga ultra terra mbps yang Anda miliki, kecepatan unduh TIDAK BERMASALAH. Yang penting adalah respons waktu dan TTL (waktu hidup).


Hal ini merupakan kasus yang umum terjadi pada pengguna di kawasan Amerika Latin. Saya tidak tahu apa yang terjadi di sana, tetapi kalian memiliki koneksi yang buruk dengan ping lebih dari 200ms yang dapat mengganggu sinkronisasi.


Jadi, apa solusi untuk para pengguna yang putus asa ini?



- berhenti menggunakan Blixt dengan Tor. Sama sekali tidak berguna
- anda bisa menggunakan VPN tetapi pilihlah dengan bijak dan pantau selalu pingnya. Gunakan salah satu yang lebih dekat dengan lokasi geografis Anda. Jarak berarti lebih banyak waktu respons ms, ingat.
- pilihlah dengan bijak rekan-rekan neutrino Anda, berikut adalah daftar server neutrino publik yang terkenal:


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


Cara lain adalah dengan memilih salah satu dari daftar node yang mengumumkan "filter ringkas" (BIP157/neutrino) - [Halaman Bitnodes Filter Neutrino](https://bitnodes.io/nodes/?q=NODE_COMPACT_FILTERS). Pilih salah satu yang lebih dekat dengan lokasi geografis Anda.


Cara lain (cara terbaik) adalah terhubung ke node komunitas lokal, yang dikelola oleh teman atau grup yang Anda kenal, dan menawarkan koneksi neutrino. (https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core) Simpul mereka tidak akan terpengaruh dengan cara apa pun, mereka hanya membutuhkan koneksi yang stabil dan bersifat publik.


Ada kebutuhan untuk lebih banyak server neutrino di wilayah LATAM, untuk sinkronisasi yang lebih baik dan cepat. Jadi, silakan atur diri Anda sendiri, dengan komunitas Bitcoin lokal Anda dan putuskan siapa dan di mana yang menjalankan Bitcoin Core + Neutrino untuk penggunaan Anda sendiri. Hanya dengan IP publik saja sudah cukup. Jika Anda tidak memiliki akses ke IP publik, Anda dapat menggunakan IP VPS dan membuat terowongan wireguard ke node rumah Anda. Dengan begitu Anda mengarahkan semua trafik ke IP VPS lokal Anda, tanpa mengungkapkan informasi pribadi apa pun tentang node rumah Anda.


### KASUS 2 - TIDAK PERNAH MENYELESAIKAN SINKRONISASI


"_Blixt saya memiliki koneksi yang baik dengan server neutrino namun mengalami kendala dalam sinkronisasi._"


#### Server Waktu


Kadang-kadang orang menggunakan berbagai perangkat lama atau tidak terhubung dengan benar ke server waktu. Neutrino melakukan sinkronisasi dengan baik hingga mencapai blok aktual yang tidak sesuai dengan waktu lokal yang sebenarnya. Anda akan melihat dalam log Blixt LND kesalahan yang mengatakan bahwa "stempel waktu blok jauh dari masa depan" atau sesuatu yang terkait dengan "header tidak lulus pemeriksaan kewarasan".


Perbaikan cepat: atur waktu dan tanggal yang tepat untuk perangkat Anda dan mulai ulang Blixt.


#### Ruang kecil pada perangkat


Terkadang dengan menggunakan perangkat lama, dengan ruang yang kecil, dapat mencapai batas ambang dan macet. Memang semakin banyak Anda menggunakan node LND seluler ini, file neutrino menjadi lebih besar dan juga file channel.db.


Perbaikan cepat: Buka Opsi Blixt - Bagian Debug - Pilih "hentikan LND dan hapus file neutrino". Ini akan memulai ulang aplikasi dan memulai sinkronisasi baru. Terkadang perbaikan cepat ini juga dapat memperbaiki data yang rusak. Perlu diingat bahwa ini akan memakan waktu, antara 1 hingga 3 menit untuk menyinkronkan ulang sepenuhnya. Proses ini TIDAK menghapus dana atau saluran yang ada, tetapi ya, setelah sinkronisasi ulang dapat memicu pemindaian ulang alamat Bitcoin Anda dan hal ini dapat memakan waktu lebih lama.


Langkah selanjutnya adalah memeriksa berapa banyak data yang masih terpakai. Anda bisa melihatnya di info Aplikasi Android - data. Jika masih lebih besar dari 400-500MB, Anda dapat memadatkan file LND. Jadi, buka Opsi Blixt - Bagian Debug - Pilih "Compact DB LND". Mulai ulang aplikasi Blixt jika tidak berjalan secara otomatis. Pemadatan terjadi saat startup dan hanya sekali. Sekarang Anda akan melihat bahwa data Blixt lebih sedikit digunakan.


#### Mode persisten


Terkadang orang tidak membuka Blixt dalam waktu yang lama, sehingga sinkronisasi menjadi terlalu lama. Tetapi mereka berharap untuk langsung disinkronkan saat membukanya.


Mohon bersabar, dan lihatlah roda pemintalan bagian atas. Opsional, Anda bisa pergi ke Opsi - Lihat Info Node dan lihat apakah disinkronkan ke rantai dan disinkronkan ke grafik yang ditandai sebagai "benar". Tanpa tanda "true", Anda tidak dapat menggunakan Blixt dengan benar, Anda tidak dapat melihat saldo dengan benar, Anda tidak dapat melihat saluran LN secara online, Anda tidak dapat melakukan pembayaran.


Perbaikan cepat: Ada opsi yang ampuh untuk "menghidupkan" node Blixt Anda. Pergi ke Opsi - Eksperimen - Pilih "Aktifkan Mode Persisten". Itu akan memulai ulang Blixt Anda dan akan menempatkan layanan LND dalam mode persisten, alias akan selalu aktif dan menjaga sinkronisasi Anda tetap online, bahkan jika Anda beralih ke aplikasi lain atau hanya menutup Blixt (bukan menutup paksa atau mematikan tugas). Anda bisa mempertahankannya seperti itu sepanjang hari jika koneksi Anda stabil dan Anda perlu menggunakan Blixt beberapa kali. Aplikasi ini tidak akan menghabiskan banyak baterai.


### KASUS 3 - SAYA INGIN BERMIGRASI KE PERANGKAT LAIN


Oke, tentang skenario ini saya menulis panduan ekstensif di [halaman FAQ](https://blixtwallet.github.io/faq#blixt-restore): dengan 2 pilihan, cepat (menutup saluran secara kooperatif sebelum migrasi) dan lambat (menutup saluran secara paksa karena perangkat lama mati).


Tetapi, saya ingin menegaskan kembali di sini, beberapa aspek penting dan menambahkan prosedur "rahasia" yang baru.


PENGINGAT:



- Selalu lakukan pencadangan status saluran (SCB) SETELAH Anda membuka atau menutup saluran. Hanya perlu beberapa detik untuk melakukannya.
- Jangan menyimpan file SCB yang lama, agar tidak bingung dan mengembalikannya. Sama sekali tidak berguna dan dapat memicu prosedur penalti jika Anda melihatnya. Selalu gunakan versi terakhir dari file SCB jika Anda melanjutkan untuk memulihkan.
- Simpan file SCB (berupa teks terenkripsi dengan ekstensi .bin) dari perangkat Anda, di tempat yang aman. Anda dapat menggunakan [LocalSend](https://github.com/localsend/localsend) untuk memindahkan file ini ke PC atau perangkat lain.
- Simpan juga seed dari Blixt Wallet Anda di tempat yang aman, misalnya pengelola kata sandi offline / USB terenkripsi.


Metode rahasia: Cara memigrasi node Blixt tanpa menutup saluran yang ada. Untuk ini, Anda perlu membaca dengan seksama bagian sebelumnya "Kontak Ketiga" dalam panduan ini tentang "Pulihkan Wallet".


Prosedur ini BUKAN UNTUK NOOB, ini hanya untuk pengguna tingkat lanjut! Itu sebabnya tidak terbuka secara luas dan saya sarankan untuk melakukannya hanya dengan bantuan dari pengembang Blixt atau dukungan saya. Tolong jangan abaikan saran ini.


### KASUS 4 - REKAN APA YANG DIGUNAKAN UNTUK MEMBUKA SALURAN?


Seperti yang saya tulis di [halaman panduan Blixt](https://blixtwallet.github.io/guides) ada banyak cara untuk membuka saluran dengan mobile LND ini. Tetapi beberapa aspek penting ingin saya ingatkan di sini:



- terbuka dengan simpul LSP yang terkenal dan dengan rekan-rekan yang dijamin oleh komunitas. [Lihat di sini daftarnya](https://github.com/hsjoberg/blixt-Wallet/issues/1033)
- jangan membuka dengan node Tor acak saja. Mereka tidak berharga dan Anda hanya akan mendapatkan masalah tidak dapat melakukan pembayaran. Tidak peduli seberapa baik teman Anda "pelari node" dengan node Tor yang buruk di hutan, itu tidak akan pernah memberi Anda rute terbaik untuk node pribadi seluler. Anda tidak membuka saluran dengan seseorang hanya karena dia teman Anda. Ini bukan Facebook! Anda membuka saluran untuk: rute yang bagus, biaya yang kecil, ketersediaan.
- tidak perlu membuka banyak sekali saluran kecil, 2-3 atau maksimal 4, tetapi dengan jumlah Sats yang baik. Jangan membuka saluran kecil, sama sekali tidak berguna. Lebih kecil dari 200k untuk ponsel tidak banyak gunanya.
- ingatlah LSP yang menawarkan saluran masuk dan saluran JIT (tepat pada waktunya). Hal ini sangat berguna karena Anda tidak perlu menggunakan UTXO Anda, Anda dapat membayar saluran pembuka dengan dana yang sudah Anda miliki di dompet LN lainnya, menumpuk dan mempersiapkannya untuk saluran yang lebih besar untuk dibuka. Anda harus menggunakan saluran JIT ini sesuai keinginan Anda. [Saya telah menjelaskan dalam panduan ini](https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) lebih banyak opsi untuk peer untuk node pribadi seperti Blixt. Juga [di sini, di panduan ini yang diposting di SN](https://stacker.news/items/679242/r/DarthCoin) saya menjelaskan cara mengelola likuiditas mobile node pribadi.


---

## Kesimpulan


Oke, ada banyak fitur luar biasa lainnya yang ditawarkan Blixt, saya akan membiarkan Anda menemukannya satu per satu dan bersenang-senanglah.


Aplikasi ini benar-benar diremehkan, terutama karena tidak didukung oleh pendanaan VC mana pun, digerakkan oleh komunitas, dibangun dengan cinta dan semangat untuk Bitcoin dan Lightning Network.


Node LN mobile ini, Blixt adalah alat yang sangat kuat di tangan banyak pengguna, jika mereka tahu cara menggunakannya dengan baik. Bayangkan saja, Anda berjalan keliling dunia dengan membawa node LN di saku Anda dan tidak ada yang akan mengetahuinya.


Dan belum lagi semua fitur kaya lainnya yang menyertainya, yang hanya sedikit atau bahkan tidak ada yang bisa ditawarkan oleh aplikasi Wallet lainnya.


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
**PENAFIAN:**


*Saya tidak dibayar atau didukung dengan cara apa pun oleh pengembang aplikasi ini. Saya menulis panduan ini karena saya melihat minat terhadap aplikasi Wallet ini semakin meningkat dan pengguna baru masih belum mengerti bagaimana cara memulainya. Juga untuk membantu Hampus (pengembang utama) dengan dokumentasi tentang penggunaan node Wallet.*


*Saya tidak memiliki kepentingan lain dalam mempromosikan aplikasi LN ini, selain mendorong adopsi Bitcoin dan LN. Ini adalah satu-satunya cara!*


---