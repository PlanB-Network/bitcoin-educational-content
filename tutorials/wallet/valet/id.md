---
name: Valet Bitcoin
description: Valet membawa simpul Lightning non-kustodian ke dalam saku Anda
---

![cover_valet](assets/cover.webp)



## Pendahuluan


Valet adalah Bitcoin dan Lightning wallet yang ringan dan mandiri yang menawarkan proses orientasi yang mudah dan nyaman bagi pemula. Secara khusus dirancang untuk melayani komunitas Bitcoin dan ekonomi sirkular, terutama di daerah terpencil.


Ini adalah fork dari **Simple Bitcoin Wallet (SBW) **, dengan fitur saluran Hosted Lightning canggih yang disebut **Fiat Channels**, yang dirancang untuk memungkinkan siapa pun menerima pembayaran Lightning tanpa risiko volatilitas.


Valet saat ini hanya tersedia untuk perangkat Android, dan dapat diunduh dan diinstal dari beberapa toko aplikasi bersumber terbuka. Namun, Valet tidak tersedia di Google Play Store karena masalah privasi pengembang dan KYC.



## Unduh dan Instal Valet


Valet dapat diunduh sebagai file APK dari halaman GitHub Standard Sats. [Standard Sats] (https://standardsats.github.io/) adalah perusahaan yang mengembangkan Valet.


👉 Untuk mengunduh Valet, kunjungi [halaman GitHub] Standard Sats [https://github.com/standardsats/valet/releases], dan temukan rilis **terbaru** (Biasanya yang paling atas).


👉 Buka **Assets** dan klik pada file yang hanya berekstensi **.apk**. Pengunduhan Anda akan dimulai secara otomatis.


![Standard_Sats_GitHub_page_view](assets/en/001.webp)


👉 Setelah pengunduhan selesai, buka **Manajer file** > **Unduhan** pada perangkat Anda, dan pilih file apk Valet.


![Select_valet_apk](assets/en/002.webp)


👉 Instal, dan dalam beberapa detik, aplikasi Anda akan siap dan muncul di layar beranda.


![valet_icon_on_homescreen](assets/en/003.webp)


Sebagai alternatif, Anda juga dapat mengunduh Valet dari toko aplikasi **F-Droid**. Jika Anda tidak memiliki aplikasi F-Droid di perangkat Anda, Anda dapat mengunduh dan menginstalnya [di sini] (https://f-droid.org/en/).


👉 Pada layar beranda Anda, buka F-Droid dan cari **Valet**. Pilih opsi pertama dengan **ikon ungu dan putih** dari dua opsi yang akan muncul, dan klik **Unduh**.


![F-Droid_icon_on_homescreen](assets/en/004.webp)


![search_and_download_Valet](assets/en/005.webp)


👉 Setelah mengunduh, klik **Instal** dan ikuti petunjuk di layar. Setelah instalasi selesai, Anda dapat meluncurkan Valet dari F-Droid dengan mengeklik **Buka**, atau meluncurkannya dari layar beranda perangkat.



## Membuat Bitcoin Wallet


Anda dapat mengatur Bitcoin wallet di Valet dalam dua langkah sederhana.


👉 Luncurkan Valet dari layar beranda perangkat Anda atau dari aplikasi F-Droid. Layar penyiapan wallet akan muncul, dengan dua opsi: **Buat Wallet Baru** dan **Pulihkan Wallet yang sudah ada**.


👉 Pilih **Create New Wallet**, dan seketika itu juga, wallet baru akan dibuat, dan Anda akan diarahkan ke halaman beranda.


![set_up_a\_new_wallet](assets/en/006.webp)



## Cadangkan Frasa Benih Anda


👉 Pada halaman beranda wallet, klik **kartu Green** yang bertuliskan **"Ketuk untuk menyimpan frasa pemulihan wallet jika Anda kehilangan atau mengganti perangkat Anda "**


![seed_phrase_green_card](assets/en/007.webp)


👉 Satu set 12 kata dalam bahasa Inggris akan ditampilkan. Tulislah di atas kertas, dengan urutan 1 sampai 12, dan simpanlah dengan aman.


![the_seed_phrase](assets/en/008.webp)


### Perhatikan ⚠️:


Perhatikan elemen-elemen berikut ini:


- Seperti yang telah Anda ketahui, Valet adalah wallet kustodian mandiri, sehingga frasa seed Anda adalah satu-satunya akses untuk memulihkan Wallet Anda.
- Jika Anda kehilangan frasa seed Anda, Anda tidak akan **pernah** mendapatkan akses ke wallet Anda.
- Jika seseorang mendapatkan frasa seed Anda, mereka dapat mencuri semua Bitcoin Anda.


Jadi, Anda harus menuliskan frasa seed yang terdiri dari 12 kata dan menyimpannya di tempat yang aman. Anda tidak boleh mengambil tangkapan layar, menyimpannya sebagai draf di email Anda, atau menyimpannya di perangkat elektronik apa pun yang pernah terhubung ke internet.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

## Menerima dan Mengirim Bitcoin secara Valet


Valet adalah wallet kustodian mandiri dengan kemampuan on-chain dan Lightning Bitcoin. Ini berarti Anda dapat menerima dan mengirim Bitcoin dari Valet baik melalui **On-chain** atau melalui **Lightning Network**.


Namun, untuk dapat menerima atau mengirim Bitcoin melalui Lightning, Anda perlu menyiapkan saluran Lightning menggunakan on-chain Bitcoin Anda sebagai Liquidity. Atau Anda dapat membeli likuiditas saluran Lightning dari vendor.



## Menghasilkan Bitcoin Address On-chain


Untuk menerima Bitcoin hingga on-chain, Anda harus membuat alamat Bitcoin.


👉 Pada halaman beranda wallet, Anda akan melihat **Kartu Jingga** dan **Kartu Ungu**, masing-masing berlabel **Bitcoin** dan **Kilat**.


👉 Klik pada kartu berwarna oranye yang berlabel **Bitcoin**. Anda akan diarahkan ke layar yang menampilkan alamat Bitcoin.


![click_on_Bitcoin_card](assets/en/009.webp)


👉 Anda dapat **menyalin** alamat dan mengirimkannya kepada orang yang mengirimkan Bitcoin kepada Anda, atau klik tombol **berbagi** untuk mengirimkan kode QR kepada orang tersebut melalui media sosial atau saluran komunikasi lainnya.


👉 Anda juga dapat mengklik tombol **Edit** untuk mengatur jumlah Bitcoin yang harus dikirim ke alamat tersebut.


**Perhatian:** Seperti faktur, fitur edit sangat berguna dalam skenario di mana Anda mungkin ingin menerima jumlah Bitcoin tertentu ke suatu alamat pada suatu titik; namun, ini tidak berarti bahwa alamat tersebut tidak dapat menerima jumlah yang lebih tinggi atau lebih rendah.


klik **Lebih banyak alamat baru**, untuk menghasilkan alamat baru secara acak.


![generating_a\_bitcoin_add](assets/en/010.webp)


👉 Anda juga bisa membuat alamat on-chain Bitcoin dengan mengklik tombol **Terima** di bagian bawah halaman beranda wallet Anda. Kemudian pilih **Terima ke alamat bitcoin**, dan lanjutkan dengan proses yang sama seperti di atas.


![click_receieve_button](assets/en/011.webp)


![receive_to_bitcoin_address](assets/en/012.webp)



## Mengirim Bitcoin melalui On-chain


Mengirimkan Bitcoin dari Valet wallet melalui on-chain adalah tugas yang mudah.


👉 Di bagian bawah halaman beranda wallet Anda, klik tombol **Kirim**, masukkan alamat Bitcoin, atau klik **Pindai**, untuk memindai kode QR alamat, lalu klik **Ok**.


![click_send_button](assets/en/013.webp)


![enter_bitcoin_add](assets/en/014.webp)


👉 Masukkan jumlah Bitcoin yang ingin Anda kirim. Anda dapat memasukkan jumlah secara manual dalam Sats atau dalam mata uang Fiat, atau Anda dapat mengklik **Max** untuk menggunakan semua saldo on-chain Anda.


👉 Anda juga dapat menyesuaikan biaya yang ingin Anda bayarkan untuk transaksi tersebut dengan mengeklik kotak hijau kecil berlabel **biaya** lalu menggeser titik putih ke kanan atau ke kiri untuk menambah atau mengurangi biaya. Klik **Ok** untuk mengirim transaksi.


![enter_amount_and_fee_rate](assets/en/015.webp)



## Menyiapkan Saluran Lightning Network


Seperti disebutkan di atas, Valet adalah Bitcoin dan Lightning wallet kustodian mandiri; oleh karena itu, untuk dapat mengirim dan menerima Bitcoin melalui jaringan Lightning, Anda harus menyiapkan saluran Lightning terlebih dahulu, dengan mengikuti langkah-langkah berikut:


👉 Pada layar beranda, klik **kartu ungu** berlabel **Petir**. Anda akan dibawa ke halaman dengan opsi berikut ini:



- Pindai Node QR
- Beli di LNBIG.COM
- Beli di BITREFILL.COM
- Meminta sinkronisasi ulang grafik LN.


Ketika Anda memilih **Purchase from lnbig.com** atau **Purchase from bitrefill.com**, Anda akan diarahkan ke situs web perusahaan-perusahaan ini, di mana Anda dapat membeli likuiditas masuk dengan beberapa kapasitas. Abaikan opsi terakhir **Minta sinkronisasi ulang grafik LN** untuk saat ini.


Jadi pilihan pertama kita di sini adalah **Pindai QR Node**. Pada titik ini, Anda harus sudah memutuskan dan mendapatkan **kode QR** dari node yang ingin Anda buka salurannya. Anda dapat membuka saluran ke node publik mana pun yang Anda pilih. Lihat [1ML] (https://1ml.com/) atau [Amboss] (https://amboss.space/), pilih node publik yang Anda inginkan, dan pindai kode QR yang terkait dengan node yang Anda pilih.


![channel_opening_options](assets/en/016.webp)


👉 Anda akan secara otomatis diarahkan ke halaman berikutnya, di mana Anda harus mendanai saluran Anda. Sekali lagi, penggunaan jaringan Lightning kustodian mandiri mengharuskan Anda menggunakan Bitcoin untuk mendanai saluran. Ini berarti Anda harus memiliki Bitcoin di on-chain wallet Anda untuk mendanai saluran Lightning. Silakan lihat artikel ini oleh [Hacken] (https://hacken.io/discover/lightning-network/), untuk membaca lebih lanjut tentang jaringan Lightning.


![fund_channel](assets/en/017.webp)


👉 Masukkan **jumlah** Bitcoin yang ingin Anda danai untuk mendanai saluran tersebut, atau klik **Max** untuk menggunakan semua saldo on-chain Bitcoin Anda. Anda dapat menyesuaikan **biaya**, atau membiarkan pengaturan biaya default, dan klik **Ok**.


**Perhatian:** Jumlah yang Anda danai untuk mendanai saluran akan menjadi kapasitas saluran baru Anda (yaitu total volume Sats yang dapat ditransaksikan ke dan dari saluran tersebut)


Penting juga bagi Anda untuk menggunakan lebih dari **100.000 Sats** sebagai jumlah pendanaan saat membuka saluran. Hal ini karena banyak node Lightning membutuhkan kapasitas minimal 100.000 Sats untuk membuka saluran untuk mereka. Jadi, untuk menghindari coba-coba, cukup gunakan jumlah yang lebih tinggi dari kisaran tersebut.


![enter_funding_amount](assets/en/018.webp)


![funding_approval](assets/en/019.webp)


👉 Pada titik ini, ketika Anda memeriksa halaman beranda wallet Anda, Anda akan melihat bahwa jumlah pendanaan Anda sekarang telah dipindahkan dari **kartu Bitcoin** ke **kartu Lightning**. Pada riwayat transaksi Anda, Anda akan melihat transaksi pendanaan yang sedang diproses.


![channel_funding_processing](assets/en/020.webp)


👉 Jika Anda mengklik kartu Lightning, Anda akan melihat informasi yang menunjukkan bahwa saluran Lightning Anda terbuka. Anda juga akan melihat **transaksi pendanaan saluran** pada daftar transaksi Anda. Tunggu hingga transaksi pendanaan Anda dikonfirmasi pada blockchain, dan channel Lightning Anda akan siap.


![channel_opening](assets/en/021.webp)


👉 Segera setelah transaksi pendanaan dikonfirmasi, klik **Kartu Lightning** di halaman beranda Anda, dan Anda akan melihat informasi tentang saluran Lightning Anda sebagai berikut:



- Rangkaian angka acak yang dipisahkan oleh titik-titik:** Ini adalah alamat IP node. (IPV4 dan IPV6, masing-masing)
- KAPASITAS:** Ini adalah total volume Sats yang dapat dikirim dan diterima melalui saluran ini
- DAPAT MENGIRIM:** Ini adalah jumlah Sats yang dapat Anda kirim pada saat ini. Anda akan melihat bahwa angka ini hampir sama dengan **Kapasitas**. Ini karena Anda belum mengirimkan pembayaran apa pun melalui saluran tersebut.
- DAPAT MENERIMA:** Ini adalah jumlah Sats yang dapat Anda terima di saluran ini saat ini. (Jumlahnya tidak banyak pada saat ini karena untuk dapat menerima, Anda harus terlebih dahulu mengirimkan sejumlah Sats untuk membuat Liquidity yang masuk)
- DAPAT DIKEMBALIKAN:** Ini menampilkan jumlah yang dibayarkan kembali ke alamat on-chain Anda ketika Anda menutup saluran. Ini juga disebut sebagai **Saldo lokal saluran** Anda. Perhatikan bahwa jumlah ini hanya sedikit lebih kecil dari kapasitas saluran, dan ini karena ketika menutup saluran, anda harus membayar biaya untuk mempublikasikan transaksi penutupan pada blockchain, sama seperti yang anda lakukan ketika mendanai saluran. Jadi sistem telah mengurangi perkiraan jumlah terendah yang akan anda bayarkan)
- NILAI DALAM PENERBANGAN:** Ketika seseorang mengirimkan sejumlah sats ke saluran Anda, atau ketika Anda mencoba mengirimkan sejumlah sats ke seseorang, dan karena alasan apa pun, transaksi tertunda, hal itu sering ditampilkan di bidang ini.


![channel_info](assets/en/022.webp)


## Mengirim Sats Melalui Saluran Anda


Mengirim Sats melalui Lightning Network adalah tugas yang mudah.


👉 Di bagian bawah halaman beranda, klik **Kirim**, dan **tempel** faktur Lightning (Anda harus sudah menyalinnya) di bidang yang tersedia, atau klik **Pindai** untuk memindai kode QR faktur Lightning.


![click_send_or_scan](assets/en/023.webp)


Sebagian besar faktur Lightning dilengkapi dengan jumlah yang sudah dimasukkan sebelumnya untuk dibayar. Namun dalam beberapa kasus, faktur ini mungkin merupakan faktur terbuka yang mengharuskan Anda untuk mengisi jumlahnya.


👉 Masukkan jumlah dalam **Dolar** atau **Sats**, atau klik **Max**, untuk menggunakan semua saldo di saluran Lightning Anda, lalu klik **Ok**. Segera setelah jalur yang baik ditemukan, pembayaran Anda akan dikirim dan selesai dalam beberapa detik. Perhatikan halaman beranda untuk melihat apakah pembayaran telah selesai. Ini akan mendapatkan tanda centang hijau ketika telah selesai.


![enter_the_amount](assets/en/024.webp)


## Menerima Sats Melalui Saluran Anda


Menerima pembayaran di saluran Lightning Anda sangat bergantung pada apakah Anda memiliki likuiditas masuk Liquid atau tidak. Setelah membuka saluran, Anda tidak akan dapat menerima pembayaran hingga Anda setidaknya telah mengirim sejumlah Sats untuk **menciptakan likuiditas masuk** di ujung lain koneksi saluran. Untuk mengonfirmasi apakah Anda dapat menerima Sats dan jumlah Sats yang dapat Anda terima, centang kolom **Dapat Menerima** di informasi saluran Anda. Ini akan menunjukkan kepada Anda berapa banyak Sats yang Anda terima pada setiap titik waktu.


Sekarang, anggaplah Anda telah mengirimkan sejumlah Sats dari saluran Anda, Anda sekarang memiliki likuiditas masuk, dan dapat menerima Sats.


Untuk menerima di saluran Lightning, Anda harus membuat faktur. Tidak seperti Bitcoin on-chain, yang menggunakan alamat, jaringan Lightning menggunakan faktur. Ada dua rute untuk membuat faktur di Valet.


#### OPSI 1


👉 Di bagian bawah halaman beranda, klik **Terima**, pilih **Terima faktur Lightning**. Isi jumlah yang akan diterima di faktur, dan klik **Ok**. Salin faktur atau bagikan kode QR kepada pembayar.


![receive_to_channel](assets/en/025.webp)


![fill_invoice_amount](assets/en/026.webp)


![copy_invoice_or_share_QR](assets/en/027.webp)


#### OPSI 2


👉 Klik pada kartu Lightning berwarna ungu di halaman beranda wallet Anda. Ketuk di mana saja di saluran Anda, dan daftar pilihan akan muncul. Pilih **Terima ke saluran** dan masukkan jumlah yang Anda terima (baik dalam Sats atau dolar). Anda juga akan melihat berapa banyak Sats yang dapat Anda terima (kapasitas masuk) saat Anda mengisi faktur. Klik **Ok** dan salin faktur atau bagikan kode QR kepada pembayar.


![receive_to_channel](assets/en/028.webp)


**Perhatian:** Opsi pertama adalah opsi universal, yang berarti bahwa jika Anda memiliki lebih dari satu saluran aktif dan Anda menggunakan opsi pertama, sistem akan secara otomatis memilih salah satu saluran untuk menerima Sats.


Jadi, dalam skenario ini, pilihan kedua adalah yang terbaik untuk digunakan jika Anda ingin menerima Sats ke saluran tertentu.


### Opsi Pop-Up Saluran Anda Dijelaskan


Ketika Anda mengetuk saluran Anda, bidang opsi berikut ini akan ditampilkan:


![channel_pop_ups](assets/en/029.webp)


**BAGIKAN DETAIL SALURAN LIGHTNING:** Ini memungkinkan Anda untuk membagikan detail saluran Anda, seperti ID rekan jarak jauh, ID saluran lokal, transaksi Pendanaan, tanggal pembuatan, dll.


**MENUTUP SALURAN KE DOMPET:** Anda dapat menutup saluran petir Anda kapan pun Anda mau. Untuk menutup saluran Anda, sistem akan memeriksa saldo Bitcoin yang Anda miliki di sisi saluran Anda sendiri (ingat bidang **"Dapat Mengirim "**, juga dikenal sebagai saldo lokal Anda), dan mengirimkannya kembali kepada Anda. Di Valet, Anda dapat memilih ke mana Anda ingin Bitcoin tersebut dikirim ketika saluran ditutup. Jadi, **Tutup saluran ke wallet** adalah salah satu dari dua pilihan Anda.


klik opsi ini, dan pilih **Bitcoin**. Penutupan saluran akan dimulai, dan saldo Bitcoin saluran Anda akan dikirim kembali ke alamat on-chain wallet Anda.


![close_channel_to_wallet](assets/en/030.webp)


**TUTUP SALURAN KE ADDRESS:** Ini adalah opsi kedua untuk menutup saluran. Ketika Anda memilih opsi ini, Anda akan diminta untuk memasukkan alamat wallet ke mana saldo Bitcoin di saluran Anda akan dikirim. Harap diperhatikan bahwa pada opsi ini, Anda hanya dapat memindai kode QR dari alamat Bitcoin yang ingin Anda tutup salurannya. Saat ini, tidak ada opsi untuk menempelkan alamat secara manual.


👉 Klik opsi ini, pindai alamat Bitcoin, dan klik **Ok**. Penutupan saluran akan dimulai, dan saldo Lightning Bitcoin Anda akan dikirim ke alamat yang Anda pindai.


![scan_address_and_Ok](assets/en/031.webp)


**Menerima ke saluran:** Ini adalah hal yang sama seperti membuat faktur, tetapi dalam beberapa kasus, Anda mungkin memiliki lebih dari satu saluran, termasuk saluran Fiat (jenis saluran Lightning yang unik yang dapat diperoleh di Valet wallet). Jadi, jika Anda memiliki beberapa saluran yang terbuka, opsi ini memastikan bahwa Anda dapat menerima pembayaran ke saluran tertentu.


**ISI ULANG DARI SALURAN LAIN:** Opsi ini adalah fitur yang memungkinkan Anda mengisi ulang satu saluran dari saluran lain yang ada. Misalnya, jika Anda memiliki 2 saluran Lightning yang berbeda (A dan B), dan saldo Bitcoin pada saluran A telah habis, dengan opsi ini, Anda dapat dengan mudah dan otomatis mengisi ulang saldo saluran A dari saluran B.


**DIRECT NOT PRIVATE RECEIVE:** Ini juga merupakan opsi untuk membuat faktur untuk menerima pembayaran, tetapi ketika Anda menggunakan opsi ini, pengirim membayar Anda secara langsung. Ini berarti bahwa pembayaran tidak melewati node yang berbeda sebelum sampai ke tangan Anda, seperti halnya pembayaran Lightning biasa. Jadi, pada intinya, pengirim tahu bahwa Anda yang mereka bayar, mengetahui ID saluran Anda, dll. Opsi ini sering kali dapat digunakan ketika Anda menerima pembayaran dari sumber yang Anda percayai dan tidak perlu menjaga privasi Anda.


## Saluran yang Di-host dan Fiat


Seperti kebanyakan Bitcoin wallet lainnya, Valet adalah Bitcoin dan Lightning wallet yang sederhana dan ringan. Tetapi memiliki fitur Lightning yang unik yang membedakannya dari kebanyakan Bitcoin wallet lainnya. Fitur itu disebut **Hosted and Fiat Channels**.


Saluran Fiat adalah jenis implementasi Lightning yang memungkinkan kemudahan dalam proses orientasi dan penggunaan jaringan Lightning. Ini adalah solusi kustodian yang memungkinkan anonimitas penuh, seperti halnya saluran Lightning biasa. Teknologi saluran Fiat juga memungkinkan pembuatan turunan Bitcoin pada jaringan Lightning. Contohnya adalah dengan saluran Fiat, pedagang dapat menerima pembayaran Bitcoin dengan nilai stabil tanpa mengkhawatirkan volatilitas Bitcoin.


Implementasi saluran Fiat saat ini di Valet memungkinkan penciptaan mata uang Fiat sintetis yang stabil yang didukung oleh Sats. Ini menggunakan hubungan Host-Klien di mana Host adalah node Lightning yang menawarkan layanan ini, dan klien adalah pengguna Valet. Ini adalah solusi kustodian karena semua Sats berada di sisi Host; namun, pembuatan faktur, perutean tor, dan pembuatan gambar awal masih terjadi di sisi klien seperti pada saluran Lightning normal.


Membuka saluran Fiat membutuhkan proses yang sama dengan membuka saluran Lightning. Satu-satunya perbedaan yang signifikan adalah bahwa dalam kasus ini, klien (pengguna Valet) tidak perlu melakukan likuiditas on-chain untuk membuat kapasitas saluran. Host menetapkan kapasitas saluran dan merutekan semua pembayaran untuk klien.


👉 Untuk membuka saluran Fiat, klik **Kartu Petir** berwarna ungu di halaman beranda wallet Anda. Pilih **Pindai QR Node** (Pada titik ini, Anda harus telah mengidentifikasi Host yang ingin Anda buka salurannya, dan mendapatkan QR node tersebut. Contoh node Host yang dapat digunakan untuk membuka saluran Fiat adalah node SATM dengan Standard Sats.)


**Perhatian:** Penting untuk dicatat bahwa siapa pun dapat menjadi Host. Yang Anda perlukan hanyalah menjalankan node Lightning dengan **Pengaya saluran Fiat** dan **Layanan lindung nilai**. Fiat channel adalah proyek sumber terbuka oleh *Standard Sats*. Baca lebih lanjut tentang hal ini di [di sini] (https://github.com/standardsats/fiat-channels-rfc) dan [di sini] (https://standardsats.github.io/).


QR simpul SATM di bawah ini:


![SATM_node_QR](assets/en/032.webp)


👉 Setelah Anda memindai QR node, klik **Permintaan saluran fiat USD** atau **Permintaan saluran fiat EUR** (Ini adalah denominasi fiat yang akan digunakan untuk mengutip saldo Fiat Anda). Untuk saat ini, pilih USD, dan klik **OK**. Saluran akan terbuka secara otomatis, dan Anda dapat langsung menerima Sats. Anda lihat, sesederhana itu!!!


![choose_fiat_denomination](assets/en/033.webp)


![channel_confirmation_prompt](assets/en/034.webp)


👉 Masuk ke halaman beranda wallet Anda, Anda akan melihat kartu **hijau muda** berlabel **USD**, yang merupakan **channel Fiat** Anda.


![fiat_channel_card](assets/en/035.webp)


**Perhatian:** Ketika Anda menerima Sats di saluran Fiat, nilai fiat dari Sats yang Anda terima akan dikunci sebagai saldo yang stabil, sementara volume Sats mengambang dengan harga Bitcoin. Solusi ini dirancang terutama untuk pedagang yang ingin menerima Sats untuk pembayaran tetapi tidak ingin menghadapi tantangan volatilitas Bitcoin. Hal ini membantu mereka mempertahankan nilai yang stabil setiap saat, sambil tetap dapat bertransaksi di jaringan Lightning, menikmati jangkauan global dan penyelesaian cepat Bitcoin sebagai alat tukar di Lightning Network.


Ketika saluran Fiat Anda dibuat, berikut ini adalah bidang Nilai yang akan Anda lihat dan apa artinya masing-masing:


![fiat_channel_info](assets/en/036.webp)



- Rangkaian angka acak yang dipisahkan oleh titik-titik:** Ini adalah alamat IP node. (IPV4 dan IPV6, masing-masing)
- TARIF SERVER:** Ini adalah harga pasar Bitcoin di mana Host menawarkan layanan kepada Anda. Ini sering kali akan sedikit berbeda dari harga pasar yang berlaku, karena Host dapat menambahkan sedikit premi. Sepenuhnya tergantung pada Host untuk menentukan tarif ini; oleh karena itu, ini juga akan bervariasi dari satu Host ke Host lainnya.
- NILAI FIAT:** Ini adalah nilai fiat stabil yang terkunci dari setiap sat yang Anda terima di saluran ini. Ingat, seperti yang dijelaskan sebelumnya, setiap kali Anda menerima Sats di saluran Fiat Anda, nilai fiat dari Sats pada saat penerimaan segera dikunci sebagai nilai fiat stabil sintetis di bidang ini. Nilai **Saldo Fiat** Anda tidak berfluktuasi dengan harga pasar Bitcoin. Kapan pun Anda ingin melakukan pembayaran dari saluran ini, Anda hanya dapat mengirim Sats yang setara dengan saldo Fiat ini. Jadi, anggap saja ini sebagai mata uang fiat digital yang didukung oleh Sats.
- KAPASITAS:** Ini adalah total volume Sats yang dapat dikirim dan diterima melalui saluran ini. (Ini juga diatur oleh Host. Dan tidak seperti saluran Lightning biasa, kapasitas ini dapat disesuaikan oleh Host sesuai kebutuhan)
- DAPAT MENGIRIM:** Ini adalah volume Sats yang dapat Anda kirimkan pada setiap titik berdasarkan saldo fiat Anda. Ini sangat berbeda dengan apa yang Anda miliki di saluran Lightning normal, karena nilai ini mengambang dengan harga Bitcoin. Oleh karena itu, apa yang Anda lihat di sini adalah nilai Sats dari saldo Fiat Anda setiap saat berdasarkan **Server Rate**.
- DAPAT MENERIMA:** Ini adalah jumlah Sats yang dapat Anda terima ke saluran ini saat ini. Setelah Anda membuat saluran, nilai ini harus sama dengan kapasitas saluran.
- NILAI DALAM PENERBANGAN:** Ketika seseorang mengirimkan sejumlah sats ke saluran Anda, atau ketika Anda mencoba mengirimkan sejumlah sats kepada seseorang, dan karena alasan apa pun, transaksi tersebut tertunda, hal itu sering kali ditampilkan di bidang ini.


Berikut adalah hal-hal penting yang perlu diperhatikan tentang saluran Fiat:



- Tidak seperti saluran Lightning biasa, ketika Anda membuka saluran fiat, Anda dapat segera mulai menerima Sats, tetapi Anda tidak dapat mengirim. Anda hanya dapat mengirim Sats ketika Anda telah menerima Sats.
- Setiap saat, aset yang dikirim ke dan dari adalah Sats. Saldo Fiat hanyalah representasi IOU sintetis dari nilai Bitcoin yang diterima pada titik waktu tertentu. Jadi, ini bukanlah penciptaan token atau mata uang kripto baru.
- Saluran Fiat sebagian besar berguna untuk pedagang/bisnis yang skeptis tentang menerima pembayaran Bitcoin karena masalah volatilitas. Saluran ini juga berguna bagi perusahaan yang ingin membayar gaji pekerjanya dalam Bitcoin tanpa menanggung konsekuensi dari volatilitas Bitcoin, yang dapat membuat modal gaji mereka tidak stabil. Ini juga mungkin berguna bagi individu yang tinggal di daerah dengan penggunaan Bitcoin yang dominan, tetapi memiliki biaya hidup yang tetap.
- Perhatikan bahwa tidak ada bidang yang diberi label **DAPAT DIKEMBALIKAN**. Ini karena, secara teknis, Anda tidak dapat menutup saluran Fiat. Anda hanya dapat berhenti menggunakan saluran Fiat dengan menguras saldonya ke saluran Lightning normal Anda.


### Opsi Pop-Up Saluran Fiat Anda Dijelaskan


Ketika Anda mengetuk saluran Fiat Lightning Anda, bidang-bidang berikut ini akan ditampilkan:


![fiat_channel_pop_up](assets/en/037.webp)


**BAGIKAN RINCIAN SALURAN YANG DIHOST:** Ini memungkinkan Anda untuk membagikan rincian saluran Fiat Anda, seperti ID rekan jarak jauh, ID saluran lokal, tanggal pembuatan, dll.


**EXPORT CHANNEL STATE:** Ini memungkinkan Anda untuk mengekspor status saluran kapan saja. Hal ini biasanya berguna untuk memperbaiki kesalahan saluran, dan Host mungkin meminta Anda untuk membagikannya jika diperlukan.


**MENGURAS SALDO SALURAN:** Seperti yang telah disebutkan sebelumnya, Anda tidak dapat menutup saluran Fiat secara teknis, tetapi Anda dapat menguras saldo saluran Anda ke saluran Lightning normal yang ada. Hal ini secara otomatis memindahkan saldo Fiat yang setara dengan Sat ke saluran Lightning normal Anda.


**MENERIMA KE SALURAN:** Ini adalah hal yang sama seperti membuat faktur, tetapi dalam beberapa kasus, pengguna mungkin memiliki lebih dari satu saluran Fiat dengan Host yang berbeda, termasuk saluran Lightning normal. Jadi, jika pengguna memiliki beberapa saluran yang terbuka, opsi ini memastikan bahwa mereka dapat menerima pembayaran ke saluran tertentu.


**ISI ULANG DARI SALURAN LAIN:** Opsi ini merupakan fitur yang memungkinkan pengguna mengisi ulang satu saluran dari saluran lain yang ada. Jadi, dengan opsi ini, Anda dapat mengisi ulang saluran Fiat Anda dari saluran normal atau saluran Fiat lain yang Anda miliki, seperti halnya menguras.


**DIRECT NOT PRIVATE RECEIVE:** Ini juga merupakan opsi untuk membuat faktur untuk menerima pembayaran, tetapi ketika Anda menggunakan opsi ini, pengirim membayar Anda secara langsung. Ini berarti bahwa pembayaran tidak melewati node yang berbeda sebelum sampai ke tangan Anda. Jadi, pada intinya, pengirim tahu bahwa Anda yang mereka bayar, mengetahui ID saluran Anda, dll. Opsi ini sering kali dapat digunakan ketika Anda menerima pembayaran dari sumber yang Anda percayai dan tidak perlu menjaga privasi Anda.


## Pengaturan Valet:


Seperti setiap aplikasi lainnya, Valet memiliki pengaturan aplikasi yang dapat Anda sesuaikan dengan selera Anda. Anda dapat mengakses halaman pengaturan dari layar beranda.


👉 Pada layar beranda, klik ikon **Gear** yang terletak di sudut kanan atas layar untuk mengakses pengaturan. Di bawah ini adalah komponen-komponen dalam bagian pengaturan.


![settings_icon](assets/en/038.webp)


**Cadangan saluran lokal diaktifkan:** Jika ini dinyatakan **Disabled,** Anda harus mengaktifkannya karena ini adalah satu-satunya cara untuk memulihkan saluran Lightning normal jika Anda menghapus dan menginstal ulang Valet. Kami akan menjelaskan hal ini nanti. Jadi klik ini, dan berikan izin pada Valet untuk **penyimpanan media** Anda karena di situlah file cadangan disimpan.


![app_permissions](assets/en/039.webp)


![enable_media_access](assets/en/040.webp)


**TEMPAT MENYIMPAN CADANGAN LOKAL:** Selama Anda memberikan izin kepada Valet untuk penyimpanan Anda, bidang ini secara otomatis akan diatur untuk menyimpan cadangan lokal di folder **Unduhan**. Namun Anda dapat mengubahnya dengan mengklik di sini dan memilih folder pilihan Anda.


**MENGATUR DOMPET RANTAI** Ini agak teknis, dan Anda tidak perlu repot-repot melakukannya kecuali jika Anda cukup berpengalaman. Pengaturan default di sini sudah cukup baik.


**TAMBAHKAN DOMPET PERANGKAT KERAS:** Anda juga tidak perlu repot-repot melakukan hal ini, kecuali jika Anda memiliki perangkat keras wallet yang ingin Anda sambungkan dan pantau. Dengan pengaturan ini, Anda dapat memindai dan menghubungkan perangkat keras wallet Anda, seperti Trezor atau Kartu Cold, dan memantau aktivitasnya. Ini adalah fitur watch-only, yang berarti Anda tidak dapat melakukan transaksi pada Perangkat Keras wallet dari sini. Anda hanya dapat mengamati dan memantau aktivitas wallet, saldo, dll.


**SET CUSTOM ELECTRUM NODE:** Ini juga bersifat teknis, dan kecuali Anda cukup paham, Anda tidak perlu repot-repot melakukan hal ini. Pengaturan default sudah cukup baik.


**SATUAN BITCOIN:** Ini adalah bagaimana Anda ingin menampilkan saldo Bitcoin Anda. Opsi pertama menampilkan saldo Anda dalam istilah Satoshi, misalnya, 1.000.000 Sats, sedangkan opsi kedua menampilkannya dalam poin desimal BTC. Misalnya, 0.01BTC


**GUNAKAN AUTENTIKASI PIN** Jika Anda mencentang kotak ini, maka Anda harus menyiapkan PIN atau sidik jari yang harus Anda masukkan untuk masuk ke wallet, dan mengautentikasi transaksi.


**GUNAKAN KONEKSI TOR:** Jika Anda mencentang kotak ini, transaksi Anda akan dirutekan melalui jaringan Tor. Ini menambahkan lapisan privasi ekstra tetapi dapat mengakibatkan keterlambatan pembayaran, terutama untuk pembayaran Lightning.


**LIHAT BIP39 FRAGMEN PEMULIHAN:** Di sinilah Anda dapat mengakses frasa seed 12 kata untuk cadangan. Jadi, jika Anda tidak menuliskannya sebelumnya, atau Anda tidak dapat menemukan di mana Anda menuliskannya, selama Anda masih memiliki akses ke Wallet, Anda dapat menyalinnya dari sini.


**STATISTIK PENGGUNAAN:** Ini menunjukkan kepada Anda ringkasan semua transaksi dan aktivitas Anda sejak pembuatan wallet


![usage_stats](assets/en/041.webp)


## Wallet Pemulihan


Valet adalah wallet non-kustodian, jadi jika Anda kehilangan perangkat atau menghapus aplikasi wallet Anda, Anda perlu melakukan pemulihan wallet untuk mendapatkan kembali saluran Bitcoin dan Lightning Anda. Di awal tutorial ini, kami menyebutkan pentingnya menuliskan **12 kata seed frasa** Anda karena itu adalah kunci untuk memulihkan wallet Anda. Tidak ada perwakilan layanan pelanggan yang dapat membantu Anda kembali ke wallet Anda.


Ada dua alat penting yang diperlukan untuk memulihkan Valet wallet Anda, tergantung pada apakah Anda memiliki saluran Lightning yang aktif atau tidak. Untuk pengguna yang tidak memiliki saluran Lightning normal yang aktif, yang mereka perlukan hanyalah **12 kata frasa seed**, dengan mengikuti langkah-langkah sederhana di bawah ini:


👉 Instal aplikasi Valet baru, dan luncurkan/mulai aplikasi.


👉 Pilih **Kembalikan Wallet yang Sudah Ada**


![restore_existing_wallet](assets/en/042.webp)


👉 Pilih **Frasa pemulihan saja**.


![select_recovery_phrase](assets/en/043.webp)


👉 Masukkan frasa pemulihan 12 kata dan klik **OK**.


![input_12_words](assets/en/044.webp)


wallet Anda akan dipulihkan. Dalam kasus ini, hanya saldo on-chain Bitcoin Anda yang akan dipulihkan.


Namun, jika Anda memiliki saluran Lightning normal yang aktif dan Anda memulihkan wallet Anda hanya dengan frasa pemulihan, saluran Lightning Anda akan ditutup paksa, dan saldo Bitcoin yang Anda miliki di saluran tersebut akan secara otomatis dikirim ke saldo on-chain Anda.


Cara lain untuk memulihkan Valet wallet Anda, terutama jika Anda memiliki saluran Lightning normal yang terbuka sebelum Anda mencopot pemasangan Valet, adalah dengan **menggunakan file cadangan lokal yang tersimpan di perangkat Anda, di samping frasa seed 12 kata**. Jika Anda menggunakan keduanya, status saluran Lightning Anda akan dipulihkan, sehingga saluran Lightning Anda tidak akan ditutup paksa.


Berikut ini adalah langkah-langkahnya:


👉 Instal aplikasi Valet baru, dan luncurkan/mulai aplikasi.


👉 Pilih **Pulihkan Wallet yang Ada**.


👉 Pilih **Frase Cadangan + Pemulihan**.


![select_backup_and_recovery_seed](assets/en/045.webp)


👉 Pilih file Cadangan dari manajer file ponsel Anda. (File ini selalu disimpan di folder **Unduhan** secara default)


![local_backup_file_in_download_folder](assets/en/046.webp)


Setelah file cadangan yang benar dipilih, prompt yang mengonfirmasi bahwa **"File cadangan ada "** akan ditampilkan, dan kemudian akan meminta Anda untuk memasukkan frasa seed sebanyak 12 kata.


![enter_12_words](assets/en/047.webp)


👉 Masukkan frasa pemulihan 12 kata dan klik **OK**. Anda akan dibawa ke halaman beranda wallet Anda.


👉 Tunggu hingga sinkronisasi jaringan Bitcoin (**SYNC**), dan sinkronisasi node Lightning (**Sinkronisasi LN**) selesai, dan wallet Anda akan dipulihkan sepenuhnya, termasuk saluran Lightning Anda.


![LN_sync](assets/en/048.webp)


## Kesimpulan


Valet adalah solusi wallet yang menarik, dengan fitur-fitur yang membuatnya cocok untuk penerimaan pengguna baru. Valet juga memiliki saluran Fiat, teknologi yang tidak terlalu baru yang memastikan integrasi bisnis yang dijalankan dengan fiat pada standar Bitcoin.


Unduh Valet hari ini, dan cobalah !!! 🧡