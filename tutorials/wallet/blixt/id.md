---
name: Blixt

description: Dompet Node LN Seluler
---

![presentasi](assets/blixt_intro_en.webp)

## Node BTC/Lightning yang kuat di saku Anda, di mana pun Anda berada

Saya ingin memperkenalkan Anda kepada node dan dompet seluler BTC/LN yang baru dan kuat – Blixt. Nama ini berasal dari bahasa Swedia dan berarti "petir".
Jika Anda belum pernah menggunakan Bitcoin Lightning Network, sebelum Anda mulai, silakan baca [analogi penjelasan sederhana tentang Lightning Network (LN)](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport).

## ASPEK PENTING:

### 1. Blixt adalah node pribadi, BUKAN node perutean! Ingat itu.

Artinya, semua saluran LN di Blixt akan tidak diumumkan ke grafik LN (yang disebut saluran pribadi). Artinya, NODE INI TIDAK AKAN MELAKUKAN PERUTEAN pembayaran orang lain melalui node Blixt. [Baca lebih lanjut tentang saluran pribadi dan publik di sini](https://voltage.cloud/blog/lightning-network-faq/what-are-the-differences-between-public-and-private-channels/).

Node seluler Blixt BUKAN untuk perutean, saya ulangi. Terutama untuk dapat mengelola saluran LN Anda sendiri dan melakukan pembayaran LN Anda secara pribadi, kapan pun Anda membutuhkannya.

Node seluler Blixt, perlu online dan sinkron HANYA SEBELUM Anda akan melakukan transaksi Anda. Itulah mengapa Anda akan melihat ikon di atas yang menunjukkan status sinkronisasi. Ini hanya membutuhkan beberapa saat, tergantung berapa lama Anda membiarkannya offline dan menyinkronkan kembali grafik LN.

### 2. Blixt menggunakan LND (aezeed) sebagai backend dompet, jadi jangan mencoba mengimpor jenis dompet bitcoin lain ke dalamnya.

[Di sini Anda memiliki penjelasan tentang jenis-jenis dompet](https://coldbit.com/what-types-of-mnemonic-seeds-are-used-in-bitcoin/). Jadi jika sebelumnya Anda memiliki node LND, Anda dapat mengimpor seed dan backup.channels ke dalam Blixt, [seperti yang dijelaskan dalam panduan ini](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario).

### 3. Link penting Blixt (silakan bookmark mereka):

- [Repositori Github Blixt](https://github.com/hsjoberg/blixt-wallet) | [Rilis Github](https://github.com/hsjoberg/blixt-wallet/releases) (unduh file apk langsung)
- [Halaman Fitur Blixt](https://blixtwallet.github.io/features) - menjelaskan satu per satu setiap fitur dan fungsionalitas.
- [Halaman FAQ Blixt](https://blixtwallet.github.io/faq) - Daftar Q&A dan pemecahan masalah Blixt
- [Halaman Panduan Blixt](https://blixtwallet.github.io/guides) - demo, tutorial video, panduan ekstra dan kasus penggunaan untuk Blixt
- [Selebaran A4 yang dapat dicetak](https://github.com/BlixtWallet/blixtwallet.github.io/tree/master/assets/flyer) dengan langkah-langkah pertama menggunakan Blixt, dalam berbagai bahasa.
- Blixt juga menawarkan demo fungsional penuh langsung di [situs webnya](https://blixtwallet.com) atau di versi web khusus [web version](https://blixt-wallet-git-master-hsjoberg.vercel.app/), untuk memiliki pengalaman penuh menguji, sebelum mulai menggunakan Blixt di dunia nyata.
- [Halaman crowdfunding Geyser](https://geyser.fund/project/blixt) - donasikan sats sesuka Anda untuk mendukung proyek
- [Grup dukungan Telegram](https://t.me/blixtwallet)
# Fitur utama yang tersedia

## Neutrino Node

Secara default, Blixt terhubung ke server Blixt untuk menyinkronkan blok dan indeks dengan Neutrino (mode SPV untuk Verifikasi Pembayaran yang Disederhanakan), tetapi pengguna juga dapat terhubung ke node mereka sendiri. Menakjubkan melihat bahwa menyinkronkan node SPV membutuhkan waktu kurang dari 5 menit, dalam kasus saya di Android 11, untuk siap menggunakan dompet node penuh (on-chain dan LN).

## Node Non-Custodial Lengkap

Pengguna dapat mengelola saluran mereka sendiri dengan antarmuka yang mudah digunakan dan dengan informasi yang cukup ditampilkan untuk memiliki pengalaman yang baik. Di menu laci kiri atas, Anda dapat pergi ke saluran Lightning untuk mulai membuka dengan node lain, sesuai keinginan Anda. Jangan lupa untuk mengaktifkan Tor di pengaturan. Ini jauh lebih baik untuk privasi dan juga karena sebagai node seluler, jika Anda sering mengganti koneksi internet / IP clearnet, rekan-rekan Anda mungkin terganggu. Dengan URI node Tor, Anda akan selalu memiliki pengenal pribadi yang sama terlepas dari lokasi / IP Anda.

## Backup/Restore Node LND

Fitur yang kuat, mudah dikelola, dan berguna adalah memulihkan node LND yang mati lainnya, hanya dengan daftar seed 24 kata dan file channels.backup.

> [Berikut adalah panduan tentang cara memulihkan node Umbrel yang mati di Blixt dalam kasus SHTF.](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario)

Pengguna juga memiliki opsi untuk menyimpan backup saluran Blixt ke Google Drive dan/atau penyimpanan lokal di perangkat seluler mereka sendiri (untuk kemudian dipindahkan ke tempat yang aman, jauh dari ponsel Anda).

Proses pemulihan cukup sederhana: masukkan seed 24 kata, tambahkan file backup (sebelumnya disalin ke memori seluler), dan klik restore. Ini akan memakan waktu untuk menyinkronkan dan memindai semua blok untuk transaksi masa lalu Anda. Saluran akan ditutup secara otomatis dan dana dikembalikan ke dompet on-chain Anda (lihat menu laci kiri atas - on-chain).

> Jika sebelumnya Anda memiliki saluran terbuka dengan node lama Anda di belakang Tor, Anda harus terlebih dahulu mengaktifkan opsi Tor (dan memulai ulang aplikasi) dari pengaturan menu. Dengan cara ini, prosedur penutupan tidak akan gagal dan/atau opsi penutupan paksa tidak akan digunakan.

Ingat untuk membackup saluran LN Anda setelah membuka dan/atau menutup saluran. Hanya butuh beberapa detik untuk aman. Nanti, Anda dapat memindahkan file backup ke tempat yang aman jauh dari perangkat seluler Anda.
Untuk menguji seed Anda dalam skenario pemulihan, sebelum menambahkan dana, cukup gunakan seed 24 kata (aezeed) yang sama di BlueWallet. Jika alamat BTC yang dihasilkan sama di Blixt, Anda siap untuk melanjutkan. Tidak perlu menggunakan BlueWallet setelah itu, Anda dapat menghapus dompet yang diuji untuk pemulihan.

## Tor Terintegrasi

Setelah Anda mengaktifkannya, aplikasi akan memulai ulang di belakang jaringan Tor. Dari titik ini, Anda dapat melihat di pengaturan menu ID node Anda dengan alamat bawang, sehingga node lain dapat membuka saluran ke node seluler Blixt kecil Anda. Atau katakanlah Anda memiliki node Anda sendiri di rumah dan Anda ingin memiliki saluran kecil dengan node seluler Blixt Anda. Kombinasi yang sempurna.

## Dunder LSP - Penyedia Layanan Likuiditas

Fitur sederhana dan fantastis yang menawarkan pengguna baru kemampuan untuk mulai menerima BTC di Jaringan Lightning segera, tanpa perlu menyetor dana on-chain dan kemudian membuka saluran LN.
Untuk pengguna baru, ini adalah kabar baik karena mereka seharusnya dapat memulai dari awal, langsung di LN. Untuk melakukan ini, cukup buat faktur LN dari layar utama pada tombol "terima", masukkan jumlah, deskripsi, dll., dan bayar dari dompet lain. Blixt akan membuka saluran hingga 400k sats per transaksi yang diterima. Anda dapat membuka beberapa saluran jika perlu.
Sebuah kasus yang menarik dan berguna adalah sebagai berikut: katakanlah jumlah pertama yang Anda terima adalah 200k. Blixt akan membuka saluran 400k sats dengan sudah 200k (minus biaya pembukaan) di sisi Anda, tetapi karena Anda masih memiliki 200k "ruang" tersedia, Anda dapat menerima lebih banyak. Jadi pembayaran berikutnya, katakanlah 100k, akan tiba langsung melalui saluran ini, tanpa biaya tambahan, dan Anda masih memiliki 100k ruang untuk menerima lebih banyak.

Tetapi jika Anda memilih untuk menerima, katakanlah, 300k untuk pembayaran ketiga, itu akan membuat saluran 400k baru lainnya dan mendorong 300k ini ke sisi Anda.

Jika ada terlalu banyak permintaan, node Blixt dapat menyesuaikan kapasitas saluran selama pembukaan.

## Pembukaan Saluran Otomatis

Di pengaturan, pengguna dapat mengaktifkan opsi ini dan memiliki layanan otomatis yang membuka saluran dengan node dan rute terbaik berdasarkan saldo yang tersedia di dompet on-chain aplikasi Blixt. Ini adalah fitur yang bermanfaat bagi pengguna baru yang tidak yakin node mana yang harus dibuka salurannya dan/atau bagaimana membuka saluran LN. Ini seperti autopilot untuk LN.

> Ingat: opsi ini digunakan hanya sekali, ketika Anda membuat dompet Blixt baru Anda, dan diaktifkan secara default. Jadi jika pengguna baru memindai kode QR on-chain di layar utama dan menyetor sats pertama mereka ke alamat tersebut, Blixt akan secara otomatis membuka saluran dengan sats tersebut, dengan node publik Blixt.

## Layanan Likuiditas Masuk

Fitur yang didedikasikan untuk pedagang yang membutuhkan lebih banyak likuiditas MASUK, mudah digunakan. Untuk melakukan ini, cukup pilih salah satu penyedia likuiditas dari daftar, bayar jumlah yang Anda inginkan untuk saluran tersebut, dan berikan ID node Anda, dan dari sana, saluran akan terbuka ke node Blixt Anda.

## Daftar Kontak

Fitur berguna jika Anda ingin memiliki daftar penerima yang tahan lama dengan siapa Anda berdagang sebagian besar waktu. Daftar ini dapat terdiri dari LNURLs, alamat Lightning, atau informasi pembayaran/tagihan statis di masa depan. Untuk saat ini, daftar ini tidak dapat disimpan di luar aplikasi, tetapi ada rencana untuk memiliki opsi untuk mengekspornya.

## LNURL dan Alamat Lightning

Dukungan penuh LNURL. Anda dapat membayar ke LNURL, LN-auth, permintaan LN-chan dengan LNURL.
Anda dapat mengirim ke alamat LN apa pun dan juga menambahkannya ke daftar kontak Anda.
Juga mulai dengan versi 0.6.9 tersedia untuk menerima ke alamat LN Anda sendiri *@blixtwallet.com* jenis, melalui fitur [Blixt Lightning Box](https://github.com/hsjoberg/lightning-box).

## Keysend

Fitur yang sangat kuat yang dimiliki sedikit dompet seluler. Anda dapat mengirim/mendorong dana langsung melalui saluran atau ditujukan ke node lain, menambahkan pesan jika perlu. Seperti obrolan rahasia melalui LN. Fitur ini sangat berguna untuk menampilkan pesan di papan reklame Amboss.space ([di sini adalah panduan tentang papan reklame Amboss ini](https://darthcoin.substack.com/p/amboss-billboard-amazing-tool)).

## Penandatanganan Pesan
Alat yang sangat berguna untuk menandatangani pesan dengan kunci privat node Blixt Anda, pesan autentikasi, dan sebagainya. Sangat sedikit dompet mobile yang memiliki fitur ini, hampir tidak ada.

## Pembayaran Multi-Saluran - Pembayaran Multi-Jalur (MPP)

Fitur berguna untuk pembayaran LN, memungkinkan Anda membagi pembayaran LN menjadi beberapa bagian, melintasi beberapa saluran. Ini adalah cara yang baik untuk menyeimbangkan likuiditas di jaringan dan meningkatkan privasi.

## Lightning Browser

Serangkaian layanan pihak ketiga dengan LN, disusun dalam browser yang sederhana, mudah diakses, dan ramah pengguna. Ini juga cara yang baik untuk mempromosikan bisnis yang menerima BTC di LN. Ini adalah fitur yang akan dikembangkan lebih lanjut di masa depan. Untuk saat ini, tidak berfungsi di belakang Tor, jadi menjelajahi aplikasi ini akan dalam keadaan terbuka (clearnet).

## Log Explorers

Ini adalah alat yang kuat untuk memeriksa log LND dan status node Anda secara umum. Ada opsi untuk menyimpan file log. Sangat berguna untuk memiliki log ini di tangan jika Anda memerlukan bantuan pengembang dalam mengidentifikasi masalah tertentu.

## Keamanan

Anda dapat mengatur di pengaturan aplikasi, untuk keamanan dompet/node Anda yang lebih besar, kemungkinan untuk memulai aplikasi dengan kode PIN dan/atau sidik jari.

## Dompet On-chain

Fitur ini sedikit tersembunyi, di menu laci di kiri atas. Karena tidak sering digunakan oleh pengguna LN, tidak terlihat di layar utama. Tapi tidak apa-apa, Anda dapat memilikinya di dompet terpisah di mana Anda dapat mengelola alamat dan melihat log transaksi, dengan mengimpor seed Anda di Sparrow misalnya. Mungkin di masa depan, dompet Blixt juga akan mencakup fitur untuk mengelola UTxO. Tapi untuk saat ini, HANYA gunakan dompet on-chain ini untuk membuka atau menutup saluran di LN.

## Fitur Khusus

- Dengan versi 0.6.9 diperkenalkan "mode persisten" yang memungkinkan pengguna menjalankan Blixt sebagai node LN yang selalu online, menjaga layanan LND tetap hidup dan dompet LN siap menerima/mengirim kapan saja.
- Saluran Taproot Sederhana - memungkinkan pembukaan saluran Taproot untuk privasi lebih dan fitur lanjutan
- Saluran konfirmasi nol dengan Blixt Dunder LSP
- Speedloader ("sinkronisasi saluran LN") - Ini berarti semua saluran akan disinkronkan dengan cepat saat startup, untuk pencarian jalur yang lebih baik. Meskipun sedikit mengganggu bahwa Anda harus melihat layar sinkronisasi di awal, ini akan memastikan bahwa dompet mengetahui tentang semua saluran dan pembayaran akan lebih cepat dan lebih dapat diandalkan.
- Diterjemahkan dalam 25+ bahasa!

## "Easter Eggs"

Ya, dalam aplikasi Blixt, ada beberapa fitur tersembunyi, hal-hal kecil yang membuat aplikasi menjadi menarik, mengaktifkan aksi dan respons yang menyenangkan/menarik.
Petunjuk: coba klik dua kali pada logo Blixt di laci 🙂 Saya akan membiarkan Anda menemukan sisanya.

# Panduan Langkah demi Langkah Memulai dengan Blixt

> Sebagai pengguna LN baru, jika Anda mulai menggunakan Node LN Blixt, Anda pertama-tama perlu tahu apa itu Lightning Network dan bagaimana cara kerjanya, setidaknya pada level dasar. [Di sini kami menyusun daftar sumber daya sederhana tentang Lightning Network](https://blixtwallet.github.io/faq#what-is-ln). Silakan baca terlebih dahulu.”

Menjalankan node LN penuh di perangkat mobile bukanlah tugas yang mudah dan bisa memakan ruang (min 600MB) dan memori. Kami merekomendasikan untuk memiliki perangkat mobile yang baik, terupdate dan menggunakan setidaknya OS Android 11.

Saat Anda membuka Blixt, layar “Selamat Datang” akan memberi Anda beberapa opsi:

![Demo Blixt 01](assets/blixt_t01.webp)
Di sudut kanan atas, Anda akan melihat 3 titik yang mengaktifkan menu dengan:
- "enable Tor" - pengguna dapat memulai dengan jaringan Tor, khususnya jika ingin mengembalikan node LND lama yang berjalan dengan peer Tor saja.

- "Set Bitcoin node" - jika pengguna ingin terhubung langsung ke node miliknya sendiri, untuk menyinkronkan blok melalui Neutrino, dapat melakukannya langsung dari layar sambutan. Opsi ini juga baik dalam kasus koneksi internet Anda atau Tor, tidak stabil untuk terhubung ke node bitcoin default (node.blixtwallet.com).

## Langkah Pertama - Buat dompet baru

Jika Anda memilih untuk "membuat dompet baru", Anda akan langsung dialihkan ke layar utama Blixt Wallet.

Ini adalah "kokpit" Anda dan juga adalah "Main LN Wallet", jadi perhatikan, ini hanya akan menunjukkan saldo dompet LN Anda. Dompet onchain ditampilkan secara terpisah (lihat C).

![Demo Blixt 02](assets/blixt_t02.webp)

A - Ikon indikator sinkronisasi blok Blixt. Ini adalah hal terpenting untuk node LN: untuk disinkronkan dengan jaringan. Jika ikon itu masih ada dan bekerja, berarti node Anda BELUM SIAP! Jadi bersabarlah, khususnya untuk sinkronisasi awal pertama. Ini bisa memakan waktu hingga 6-8 menit, tergantung pada perangkat dan koneksi internet Anda.

Anda bisa mengkliknya dan melihat status sinkronisasi:

![Demo Blixt 03](assets/blixt_t03.webp)

Anda juga bisa mengklik tombol "Show LND Log" (A) jika Anda ingin melihat dan membaca lebih banyak detail teknis dari log LND, secara real time. Sangat berguna untuk debug dan belajar lebih banyak tentang cara kerja LN.

B - Di sini Anda dapat mengakses semua Pengaturan Blixt, dan banyak! Blixt menawarkan banyak fitur dan opsi kaya untuk mengelola node LN Anda seperti seorang profesional. Semua opsi tersebut dijelaskan secara detail di [“Halaman Fitur Blixt - Menu Opsi”](https://blixtwallet.github.io/features#blixt-options).

C - Di sini Anda memiliki menu "Magic Drawer", juga dijelaskan secara detail di sini. Di sini adalah "Onchain Wallet" (B), Saluran Petir (C), Kontak, Ikon status Saluran (A), Keysend (D).

![Demo Blixt 04](assets/blixt_t04.webp)

D - Adalah menu bantuan, dengan tautan ke halaman FAQ / Panduan, kontak pengembang, halaman Github dan grup dukungan Telegram.

E - Menunjukkan alamat BTC pertama Anda, di mana Anda dapat menyetor sats percobaan pertama Anda. INI OPSIONAL! Jika Anda menyetor langsung ke alamat tersebut, membuka saluran LN menuju Node Blixt. Artinya Anda akan melihat sats yang Anda setor, masuk ke transaksi onchain lainnya (tx), untuk membuka saluran LN tersebut. Anda dapat memeriksanya di dompet onchain Blixt (lihat poin C), dengan mengklik menu TX di kanan atas.

![Demo Blixt 05](assets/blixt_t05.webp)

Seperti yang Anda lihat di Log Transaksi Onchain, langkah-langkahnya sangat detail menunjukkan kemana sats itu pergi (setoran, buka, tutup saluran)

> REKOMENDASI: Setelah menguji beberapa situasi, kami sampai pada kesimpulan bahwa lebih efisien untuk membuka saluran antara 1 dan 5 M sats. Saluran yang lebih kecil cenderung cepat habis dan membayar % biaya yang lebih tinggi dibandingkan dengan saluran yang lebih besar.
F - Tunjukkan saldo utama dompet Lightning Anda. Ini BUKAN saldo total dompet Blixt Anda, ini hanya mewakili sats yang Anda miliki di Saluran Lightning, yang tersedia untuk dikirim. Seperti yang telah diindikasikan sebelumnya, dompet onchain terpisah. Ingatlah aspek ini. Dompet onchain terpisah karena alasan penting: itu digunakan terutama untuk membuka/menutup saluran LN.

Ok, sekarang Anda telah menyetorkan beberapa sats ke alamat onchain yang ditampilkan di layar utama. Disarankan ketika Anda melakukan itu, untuk menjaga aplikasi Blixt Anda online dan aktif untuk sementara waktu, sampai transaksi BTC diambil oleh para penambang ke dalam blok pertama.

Setelah itu bisa memakan waktu hingga 20-30 menit sampai benar-benar dikonfirmasi dan saluran terbuka dan Anda akan melihatnya di Magic Drawer - Saluran Lightning sebagai aktif. Juga titik berwarna kecil di atas laci, jika hijau akan menunjukkan bahwa saluran LN Anda online dan siap digunakan untuk mengirim sats melalui LN.

Alamat dan pesan selamat datang yang ditampilkan akan menghilang. Tidak perlu lagi untuk membuka saluran otomatis sekarang. Anda juga dapat menonaktifkan opsi di menu Pengaturan.

Saatnya untuk melanjutkan, menguji fitur dan opsi lain untuk membuka saluran LN.

Sekarang, mari kita buka saluran lain dengan peer node lain. Komunitas Blixt menyusun [daftar node baik untuk mulai menggunakan dengan Blixt.](https://github.com/hsjoberg/blixt-wallet/issues/1033)

### Prosedur untuk membuka saluran LN normal yang tidak diumumkan (pribadi) di node mobile Blixt Anda

Ini sangat sederhana, hanya memerlukan beberapa langkah dan sedikit kesabaran:
- Pergi ke [daftar Komunitas Blixt](https://github.com/hsjoberg/blixt-wallet/issues/1033) dari peer yang baik
- Pilih node dan klik pada judul link namanya, itu akan membuka halaman Ambossnya
- Klik untuk menampilkan kode QR untuk alamat URI node

![Demo Blixt 06](assets/blixt_t06.webp)

Sekarang, buka Blixt dan pergi ke laci atas - Saluran Lightning dan klik pada tombol “+”

![Demo Blixt 07](assets/blixt_t07.webp)

Sekarang, klik pada (A) kamera untuk memindai kode QR dari halaman Amboss dan detail node akan diisi. Tambahkan jumlah sats untuk saluran yang Anda inginkan dan kemudian pilih tarif biaya untuk tx. Anda dapat meninggalkannya otomatis (B) untuk konfirmasi lebih cepat atau menyesuaikannya secara manual dengan menggeser tombol. Anda juga dapat menekan lama angka dan mengeditnya sesuai keinginan Anda.

Jangan memasang kurang dari 1 sat/vbyte! Biasanya lebih baik untuk [mengkonsultasikan biaya mempool](https://mempool.space/) sebelum membuka saluran dan memilih biaya yang nyaman.

Selesai, sekarang cukup klik pada tombol “buka saluran” dan tunggu 3 konfirmasi, yang biasanya memakan waktu 30 menit (1 blok kira-kira setiap 10 menit).

Setelah dikonfirmasi, Anda akan melihat saluran aktif di bagian “Saluran Lightning” Anda.

## Langkah Kedua - Dapatkan lebih banyak Likuiditas Masuk

Ok, jadi sekarang kita memiliki saluran LN dengan hanya likuiditas KELUAR. Itu berarti kita hanya bisa MENGIRIM, kita masih tidak bisa MENERIMA sats melalui LN. Mengapa? Apakah Anda membaca panduan yang ditunjukkan di awal? Tidak? Kembali dan baca mereka. Sangat penting untuk memahami bagaimana saluran LN bekerja.

![Demo Blixt 08](assets/blixt_t08.webp)
Seperti yang Anda lihat dalam contoh ini, saluran yang dibuka dengan deposit pertama, tidak memiliki likuiditas MASUK ("Dapat menerima") yang banyak tetapi memiliki banyak likuiditas KELUAR ("Dapat mengirim").
Jadi, apa opsi yang Anda miliki, jika Anda ingin menerima lebih banyak sats melalui LN?
- Habiskan beberapa sats dari saluran yang ada. Ya, LN adalah jaringan pembayaran Bitcoin, yang digunakan terutama untuk menghabiskan sats Anda lebih cepat, lebih murah, pribadi, dan mudah. LN BUKAN cara untuk hodling, untuk itu Anda memiliki dompet onchain.
- Tukar beberapa sats, kembali ke dompet onchain Anda, menggunakan layanan tukar selam. Dengan cara ini Anda tidak menghabiskan sats Anda, tetapi mengembalikannya ke dompet onchain Anda sendiri. Di sini Anda dapat melihat secara detail beberapa metode, di [Halaman Panduan Blixt](https://blixtwallet.github.io/guides).
- Buka saluran MASUK dari penyedia LSP mana pun. Berikut adalah demo video tentang [cara menggunakan LNBig LSP untuk membuka saluran masuk](https://blixtwallet.github.io/assets/images/blixt-lnbig.mp4). Artinya, Anda akan membayar biaya kecil untuk saluran KOSONG (di sisi Anda) dan Anda akan dapat menerima lebih banyak sats ke dalam saluran tersebut. Jika Anda seorang pedagang yang menerima lebih dari menghabiskan, itu adalah opsi yang baik. Juga jika Anda membeli sats melalui LN, menggunakan Robosats atau pertukaran LN lainnya.
- Buka saluran Dunder, dengan node Blixt atau penyedia LSP Dunder lainnya. Saluran Dunder adalah cara sederhana untuk mendapatkan beberapa likuiditas MASUK, tetapi pada saat yang sama Anda menyetor beberapa sats ke dalam saluran tersebut. Juga bagus karena akan membuka saluran dengan [UTXO](https://en.bitcoin.it/wiki/UTXO) yang bukan dari dompet Blixt Anda. Itu menambahkan privasi.
Juga bagus karena, jika Anda tidak memiliki sats di dompet onchain, untuk membuka saluran LN normal, tetapi Anda memilikinya di dompet LN lain, Anda bisa saja membayar dari dompet lain tersebut melalui LN pembukaan dan deposit (di sisi Anda) dari saluran Dunder tersebut. [Lebih banyak detail bagaimana Dunder bekerja dan cara menjalankan server Anda sendiri di sini.](https://github.com/hsjoberg/dunder-lsp)

![Demo Blixt 09](assets/blixt_t09.webp)

Berikut adalah langkah-langkah cara mengaktifkan pembukaan saluran Dunder:
- Pergi ke Pengaturan, di bagian “Eksperimen” aktifkan kotak untuk “Aktifkan Dunder LSP”.
- Setelah Anda melakukan itu, kembali ke bagian atas ke “Bagian Jaringan Kilat” dan Anda akan melihat bahwa muncul opsi “Setel Server Dunder LSP”. Di sana, secara default diatur “https://dunder.blixtwallet.com” tetapi Anda dapat mengubahnya dengan alamat penyedia Dunder LSP lainnya. [Berikut adalah daftar komunitas Blixt](https://github.com/hsjoberg/blixt-wallet/issues/1033) dengan node yang dapat menyediakan saluran LSP Dudner untuk Blixt Anda.
- Sekarang Anda dapat pergi ke layar utama dan klik pada tombol “Terima”. Kemudian ikuti prosedur ini dijelaskan [dalam panduan ini](https://blixtwallet.github.io/guides#guide-lsp).

OK, jadi setelah saluran Dunder dikonfirmasi (akan memakan waktu beberapa menit) Anda akan berakhir dengan memiliki 2 saluran LN: satu dibuka awalnya dengan autopilot (saluran A) dan satu dengan lebih banyak likuiditas masuk, dibuka dengan Dunder (saluran B).
![Demo Blixt 10](assets/blixt_t10.webp)
Bagus, sekarang Anda sudah siap untuk mengirim dan menerima cukup banyak satoshi melalui LN!

## Langkah Ketiga - Prosedur Pemulihan Node

Sekarang, mari kita bahas tentang cara memulihkan dompet Blixt atau node LND yang crash. Ini sedikit lebih teknis, tapi tolong perhatikan. Ini tidak terlalu sulit.

> PENGINGAT: Di masa lalu saya menulis panduan khusus dengan beberapa opsi [cara memulihkan node LND yang crash](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario), di mana saya juga menyebutkan metode menggunakan Blixt sebagai proses pemulihan cepat, menggunakan seed + file channel.backup dari node LND Anda yang mati. Saya juga menulis panduan tentang cara memulihkan node Blixt Anda atau memigrasikan Blixt Anda ke perangkat lain, [di sini](https://blixtwallet.github.io/faq#blixt-restore).

![Demo Blixt 11](assets/blixt_t11.webp)

Tapi mari kita jelaskan dalam langkah-langkah sederhana proses ini. Seperti yang Anda lihat pada gambar di atas, ada 2 hal yang harus Anda lakukan untuk memulihkan node Blixt/LND sebelumnya Anda:
- kotak atas adalah tempat Anda harus mengisi dengan semua 24 kata dari seed Anda (node lama / mati)
- di bawah ada dua opsi tombol untuk memasukkan / mengunggah file channel.backup, yang sebelumnya disimpan dari node Blixt/LND lama Anda. Ini bisa dari file lokal (Anda mengunggahnya ke perangkat Anda sebelumnya) atau bisa dari lokasi remote Google Drive / iCloud. Blixt memiliki opsi ini untuk menyimpan backup saluran Anda langsung ke Google / iCloud Drive. Lihat lebih banyak detail di [Halaman Fitur Blixt](https://blixtwallet.github.io/features#blixt-options).

Tidak lupa untuk disebutkan, jika sebelumnya Anda tidak memiliki saluran LN yang terbuka, tidak perlu mengunggah file channel.backup. Cukup masukkan seed 24 kata dan tekan tombol pemulihan.

Jangan lupa untuk mengaktifkan Tor, dari menu titik 3 di atas, seperti yang kami jelaskan dalam bab "Langkah Pertama" dari panduan ini. Itu adalah kasus ketika Anda HANYA memiliki peer Tor dan tidak bisa dihubungi melalui clearnet (domain/IP). Jika tidak, itu tidak perlu.

Fitur berguna lainnya adalah untuk menetapkan node Bitcoin tertentu dari menu atas tersebut. Secara default, ia sinkron blok dari node.blixtwallet.com (mode neutrino) tetapi Anda dapat menetapkan node Bitcoin lain yang menyediakan sinkronisasi neutrino.

Jadi, setelah Anda mengisi opsi tersebut, dan menekan tombol pemulihan, Blixt akan mulai pertama kali menyinkronkan blok melalui Neutrino seperti yang kami jelaskan dalam bab "Langkah Pertama" dari panduan ini. Jadi, bersabarlah dan perhatikan proses pemulihan di layar utama, dengan mengklik pada ikon sinkronisasi.

![Demo Blixt 12](assets/blixt_t12.webp)

Seperti yang Anda lihat dalam contoh ini, itu menunjukkan bahwa blok bitcoin telah disinkronkan 100% (A) dan proses pemulihan sedang berlangsung (B). Itu berarti saluran LN yang sebelumnya Anda miliki, akan ditutup dan dana dipulihkan ke dompet onchain Blixt Anda.

Proses ini membutuhkan waktu! Jadi, tolong bersabar dan coba untuk menjaga Blixt Anda aktif dan online. Sinkronisasi awal bisa memakan waktu hingga 6-8 menit dan menutup saluran bisa memakan waktu hingga 10-15 menit. Jadi, sebaiknya perangkat Anda terisi daya dengan baik.
Setelah proses ini dimulai, Anda dapat memeriksa di Magic Drawer - Lightning Channels, status dari setiap saluran Anda sebelumnya, menunjukkan bahwa mereka dalam status "pending to close". Setelah setiap saluran ditutup, Anda dapat melihat tx penutupan di dompet onchain (lihat Magic Drawer - Onchain), dan membuka log menu tx.
![Demo Blixt 13](assets/blixt_t13.webp)

Juga akan baik untuk memeriksa dan menambahkan jika tidak ada, rekan-rekan sebelumnya yang Anda miliki di node LN lama Anda. Jadi, pergi ke menu Pengaturan, ke bawah ke "Lightning Network" dan masuk ke opsi "Show Lightning Peers".

![Demo Blixt 14](assets/blixt_t14.webp)

Di dalam bagian ini, Anda akan melihat rekan-rekan yang terhubung pada saat itu dan Anda dapat menambahkan lebih banyak, lebih baik menambahkan mereka yang sebelumnya memiliki saluran. Cukup pergi ke halaman Amboss, cari alias node rekan Anda atau nodeID dan pindai URI node mereka.

![Demo Blixt 15](assets/blixt_t15.webp)

Seperti yang Anda lihat di gambar di atas, ada 3 aspek:

A - mewakili alamat URI node clearnet (domain/IP)

B - mewakili alamat URI node Tor onion (.onion)

C - adalah kode QR untuk dipindai dengan kamera Blixt Anda atau tombol salin.

Alamat URI node ini harus Anda tambahkan ke dalam daftar rekan Anda. Jadi, perhatikan bahwa tidak cukup hanya nama alias node atau nodeID.

Sekarang Anda dapat pergi ke Magic Drawer (menu kiri atas) - Lightning Channels, dan Anda dapat melihat pada ketinggian blok kematangan dana akan dikembalikan ke alamat onchain Anda.

![Demo Blixt 16](assets/blixt_t16.webp)

Nomor blok 764272 adalah saat dana akan dapat digunakan di alamat bitcoin onchain Anda. Dan itu bisa memakan waktu hingga 144 blok dari blok konfirmasi pertama sampai dana dilepaskan. Jadi, periksa itu di [mempool](https://mempool.space/).

Dan itu saja. Cukup tunggu dengan sabar sampai semua saluran ditutup dan dana kembali ke dompet onchain Anda.

## Langkah Keempat - Kustomisasi

Bab ini tentang kustomisasi dan lebih mengenal Node Blixt Anda. Saya tidak akan mendeskripsikan semua fitur yang tersedia, terlalu banyak dan sudah dijelaskan di [Halaman Fitur Blixt](https://blixtwallet.github.io/features).

Tetapi saya akan menunjukkan beberapa di antaranya yang diperlukan untuk melanjutkan menggunakan Blixt Anda dan memiliki pengalaman yang hebat.

### A - Nama (NameDesc)

![Demo Blixt 17](assets/blixt_t17.webp)

[NameDesc](https://github.com/lightning/blips/blob/master/blip-0011.md) adalah standar untuk menyampaikan "nama penerima" dalam faktur BOLT11.

Ini bisa berupa nama apa saja dan dapat diubah kapan saja.

Opsi ini sangat berguna dalam berbagai kasus, ketika Anda ingin mengirim nama bersama dengan deskripsi faktur, sehingga penerima dapat memiliki petunjuk dari siapa mereka menerima sats tersebut. Ini sepenuhnya opsional dan juga di layar pembayaran, pengguna harus menandai kotak yang menunjukkan untuk mengirim nama alias.

Berikut adalah contoh bagaimana tampilan saat Anda menggunakan [chat.blixtwallet.com](https://chat.blixtwallet.com/)

![Demo Blixt 18](assets/blixt_t18.webp)

Ini adalah contoh lain mengirim ke aplikasi dompet lain yang mendukung NameDesc:

![Demo Blixt 19](assets/blixt_t19.webp)

### B - Backup Saluran LN dan kata-kata benih

Ini adalah fitur yang sangat penting!
Setelah membuka atau menutup sebuah saluran LN, Anda harus melakukan pencadangan. Ini bisa dilakukan secara manual dengan menyimpan sebuah file kecil di perangkat lokal (biasanya di folder unduhan) atau menggunakan akun Google Drive atau iCloud.
![Demo Blixt 20](assets/blixt_t20.webp)

Pergi ke Pengaturan Blixt - bagian Dompet. Di sana Anda memiliki opsi untuk menyimpan semua data penting untuk dompet Blixt Anda:
- “Show mnemonic” - akan menampilkan 24 kata kunci untuk ditulis
- “Remove mnemonic from device” - ini opsional dan gunakan hanya jika Anda benar-benar ingin menghapus kata-kata kunci dari perangkat Anda. Ini TIDAK akan menghapus dompet Anda, hanya kata kuncinya. Tetapi waspadalah! Tidak ada cara untuk memulihkannya jika Anda tidak menuliskannya terlebih dahulu.
- “Export channel backup” - opsi ini akan menyimpan sebuah file kecil di perangkat lokal Anda, biasanya ke dalam folder “unduhan”, dari mana Anda dapat mengambilnya dan memindahkannya keluar dari perangkat Anda, untuk penyimpanan yang aman.
- “Verify channel backup” - ini adalah opsi yang baik jika Anda menggunakan Google Drive atau iCloud untuk memeriksa integritas pencadangan yang dilakukan secara remote.
- “Google drive channel backup” - akan menyimpan file cadangan ke Google Drive pribadi Anda. File tersebut dienkripsi dan disimpan dalam repositori terpisah dari file google biasa Anda. Jadi tidak ada kekhawatiran bahwa file tersebut dapat dibaca oleh siapa pun. Bagaimanapun, file tersebut sama sekali tidak berguna tanpa kata-kata kunci, jadi tidak ada yang bisa mengambil dana Anda hanya dari file tersebut.

Saya akan merekomendasikan untuk bagian ini sebagai berikut:
- gunakan manajer kata sandi untuk menyimpan kata kunci dan file cadangan Anda dengan aman. [KeePass](https://keepass.info/) atau Bitwarden sangat bagus untuk itu dan dapat digunakan di multiplatform dan self hosted atau offline.
- LAKUKAN PENCADANGAN SETIAP KALI Anda membuka atau menutup saluran. File tersebut diperbarui dengan info saluran. Tidak perlu melakukannya setelah setiap transaksi yang Anda lakukan di LN. Cadangan saluran tidak menyimpan info tersebut, hanya menyimpan status saluran.

![Demo Blixt 21](assets/blixt_t21.webp)

## Kesimpulan

OK, masih banyak fitur menakjubkan lainnya yang ditawarkan Blixt, saya akan membiarkan Anda menemukannya satu per satu dan bersenang-senang.

Aplikasi ini benar-benar diremehkan, terutama karena tidak didukung oleh pendanaan VC, didorong oleh komunitas, dibangun dengan cinta dan gairah untuk Bitcoin dan Lightning Network.

Node LN seluler ini, Blixt adalah alat yang sangat kuat di tangan banyak pengguna, jika mereka tahu cara menggunakannya dengan baik. Bayangkan saja, Anda berjalan di seluruh dunia dengan node LN di saku Anda sendiri dan tidak ada yang akan tahu.

Dan tidak berbicara tentang semua fitur kaya lainnya yang datang dengan, yang sangat sedikit atau tidak ada aplikasi dompet lain yang bisa menawarkan.

Saya harap Anda menikmati menggunakannya. Secara pribadi, saya menyukainya dan sangat berguna bagi saya (lihat di sini sebuah kasus penggunaan di mana dompet ini adalah alat yang hebat).

SELAMAT BITCOIN LIGHTNING!

Semoga ₿ITCOIN Bersama Anda!

> DISCLAIMER: Saya tidak dibayar atau didukung dengan cara apa pun oleh pengembang aplikasi ini. Saya menulis panduan ini karena saya melihat bahwa minat pada aplikasi dompet ini meningkat dan pengguna baru masih tidak mengerti bagaimana memulainya. Juga untuk membantu Hampus (dev utama) dengan dokumentasi tentang menggunakan dompet node ini. Saya tidak memiliki kepentingan lain dalam mempromosikan aplikasi LN ini, selain mendorong adopsi Bitcoin dan LN. Ini adalah satu-satunya cara!