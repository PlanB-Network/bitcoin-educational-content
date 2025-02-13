---
name: Liana
description: Menyiapkan dan menggunakan dompet di Liana
---
![cover](assets/cover.webp)

Dalam tutorial ini, kami akan menjelaskan langkah demi langkah cara menggunakan aplikasi Liana di komputer. Di antaranya, Anda akan mempelajari cara menyiapkan rencana suksesi otomatis, menerima dan mengirim bitcoin dalam situasi normal, dan mengambil dana dari portofolio yang ada setelah periode tertentu.

Pada bulan Januari 2025, dompet perangkat keras yang kompatibel dengan Liana adalah: BitBox02, Blockstream Jade, Blockstream Jade Plus, COLDCARD MK4, COLDCARD Q, Ledger Nano S, Ledger Nano S Plus, Ledger Nano X, Ledger Flex, Specter DIY.

Jika Anda ingin memulihkan dana dari dompet Liana yang sudah ada, baca presentasi di bawah ini dan langsung ke bagian "Memulihkan bitcoin".

## Memperkenalkan perangkat lunak Liana

Liana adalah paket perangkat lunak sumber terbuka yang dirancang untuk pembuatan dan pengelolaan portofolio tingkat lanjut, terutama sebagai bagian dari sistem pewarisan otomatis atau mekanisme pencadangan yang kuat. Proyek ini telah dikembangkan sejak tahun 2022 oleh Wizardsardine, sebuah perusahaan yang didirikan bersama oleh Kévin Loaec dan Antoine Poinsot. Di situs web resminya, Liana disajikan sebagai "portofolio sederhana untuk kurasi pribadi, dengan fungsi pemulihan dan pewarisan". Perangkat lunak ini berjalan di komputer - Linux, MacOS, Windows - dan kode sumbernya (terbuka) tersedia [di GitHub](https://github.com/wizardsardine/liana).

Liana dibangun di atas kemampuan pemrograman Bitcoin untuk membuat sebuah dompet yang canggih. Secara khusus, ia memanfaatkan kunci waktu (*timelock*), yang mengizinkan dana untuk dibelanjakan hanya setelah periode waktu tertentu berlalu, dan yang terlibat dalam pemulihan Bitcoin. Dompet Liana terdiri dari beberapa jalur pengeluaran:


- Jalur pengeluaran utama yang selalu tersedia;
- Setidaknya satu jalur pemulihan, yang dapat diakses setelah waktu tertentu.

Diagram di bawah ini mengilustrasikan pengoperasian portofolio dengan dua jalur pengeluaran:

![Schéma explicatif](assets/fr/01.webp)

Operasi ini memungkinkan Anda untuk mengatur berbagai konfigurasi, termasuk :


- Rencana suksesi (atau warisan), yang memungkinkan ahli waris untuk mendapatkan kembali dana jika pengguna meninggal dunia. Untuk informasi lebih lanjut mengenai hal ini, kami sarankan untuk membaca [bagian 4] (https://planb.network/courses/btc102/233c88d3-2e8e-5eba-ac06-efe67a209038) dari kursus BTC102.
- Cadangan yang diperkuat dengan waktu pemulihan, memberikan pengguna kemungkinan untuk menggunakan dompetnya tanpa harus menyimpan frasa rahasia yang sesuai dan berisiko dicuri, selama pencurian misalnya.
- Jaring pengaman untuk orang-orang yang baru memulai dengan Bitcoin: mereka akan mengelola dompet mereka sendiri, dan "wali" mereka (kerabat, misalnya) akan memiliki hak untuk mendapatkan kembali dana mereka setelah jangka waktu tertentu.
- Skema tanda tangan multi-pihak (*multisig*) dengan persyaratan yang berkurang dari waktu ke waktu, untuk mengatasi hilangnya satu atau lebih peserta, seperti mitra perusahaan.

Kekuatan besar Liana adalah bahwa ia memperkenalkan cara standar untuk menjamin pemulihan dana jika terjadi kehilangan kunci utama, yang digunakan untuk pengeluaran saat ini. Ini merupakan inovasi besar untuk penyimpanan dana yang bersih, yang penuh dengan risiko, terutama jika Anda tidak memiliki informasi yang memadai tentang masalah ini. Oleh karena itu, Liana dapat mendorong pengguna yang paling menghindari risiko sekalipun untuk berhenti menggunakan kustodian (seperti platform pertukaran) untuk menyimpan dana mereka dan mendapatkan kembali kepemilikan atas uang mereka, sesuai dengan etos cypherpunk Bitcoin.

Tentu saja, Liana memiliki kekurangan. Yang pertama adalah Anda harus memperbarui dompet Anda secara teratur dengan melakukan transaksi di blockchain Bitcoin. Ini bisa jadi merepotkan (tergantung seberapa sering Anda menggunakan perangkat lunak ini) dan mahal (tergantung pada tingkat biaya pada saat itu), tetapi ini adalah harga yang harus Anda bayar untuk keamanan ekstra.

Poin negatif kedua mungkin kerahasiaan. Ketika Anda melibatkan orang lain dalam konfigurasi, orang tersebut mengetahui semua alamat Anda dan oleh karena itu dapat memantau aktivitas Anda. Namun, ini tidak akan menjadi masalah jika Anda memilih cadangan yang diperkuat, atau untuk rencana suksesi di mana pewaris Anda tidak memiliki pengetahuan langsung tentang detail portofolio.

## Persiapan

Dalam tutorial ini, kita akan menyiapkan rencana suksesi. Kita akan menggunakan :


- Buku Besar Nano S Plus, untuk pengeluaran sehari-hari;

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

- Blockstream Jade, digunakan untuk memulihkan dana;

https://planb.network/tutorials/wallet/hardware/jade-7d62bf0c-f460-4e68-9635-af9b731dabc3

- Dua media penyimpanan (stik USB) untuk menyimpan deskriptor portofolio;
- Surat suksesi, yang berisi instruksi untuk memulihkan dana;
- Kantong tertutup bernomor, untuk memastikan bahwa perangkat pemulihan (Jade) belum pernah digunakan.

## Instalasi dan konfigurasi

Kunjungi situs web resmi Wizardsardine dan unduh Liana di https://wizardsardine.com/liana/. Anda juga dapat mengunduh versi terbaru [dari repositori GitHub] (https://github.com/wizardsardine/liana/releases), di mana Anda dapat memeriksa keaslian perangkat lunak. Versi yang digunakan dalam tutorial ini adalah 0.9.

![Télécharger Liana](assets/fr/02.webp)

Untuk mengetahui cara memverifikasi keaslian dan integritas perangkat lunak secara manual sebelum instalasi, kami sarankan Anda membaca tutorial ini:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Instal perangkat lunak pada komputer Anda dan luncurkan. Pilih opsi "*Buat dompet Liana baru*" untuk mengonfigurasi dompet Anda.

![Accueil Liana](assets/fr/03.webp)

Pilih jenis portofolio Anda. Jika Anda ingin menyiapkan pencadangan yang disempurnakan dengan waktu pemulihan, Anda bisa memilih opsi "*Buat sendiri*" dan memilih skema default. Ini akan bekerja dengan cara yang hampir sama, kecuali bahwa Anda tidak perlu mempertahankan frasa pemulihan dompet perangkat keras.

Di sini kami mengabaikan kasus *Multisig yang diperluas*, yang mengatur konfigurasi yang lebih kompleks.

Untuk keperluan tutorial ini, kita akan menggunakan warisan sederhana.

![Choisir type de portefeuille](assets/fr/04.webp)

Berikut ini penjelasan singkatnya.

![Rapide explication](assets/fr/05.webp)

Setelah Anda membaca penjelasannya, Anda akan dapat mengatur kunci dompet Liana Anda. Ini adalah langkah yang sangat penting, karena ini menentukan karakteristik pembelanjaan akun Anda.

![Configurer clés](assets/fr/06.webp)

Pertama-tama, dalam menu "Pengaturan Lanjutan", Anda dapat menentukan "tipe deskriptor", yaitu cara penulisan kontrak pada chain. Anda dapat memilih di antara dua jenis: P2WSH (SegWit) atau Taproot. Dalam kedua kasus tersebut, semantik dari ketentuan pembelanjaan akan sama. Meskipun P2WSH membuat kontrak lebih mudah dipahami, Taproot lebih unggul karena menyembunyikan kondisi yang tidak terpakai dan menghemat biaya selama pengambilan.

Pilihan ini bersifat opsional: jika ragu, biarkan opsi default (P2WSH pada versi 0.9, tetapi ini dapat berubah).

![Choisir le type de descripteur](assets/fr/07.webp)

Selanjutnya, konfigurasikan kunci utama Anda (*kunci utama*). Kunci ini (atau lebih tepatnya, set kunci ini) akan digunakan untuk pengeluaran dana saat ini, yang tidak tunduk pada kondisi waktu apa pun. Dengan mengklik "*Set*", Anda dapat memilih *perangkat penandatanganan* yang sesuai. Dalam kasus kami, kami telah memilih dompet perangkat keras Ledger Nano S Plus.

Otorisasi berbagi kunci publik yang diperluas dari perangkat. Beri nama kunci ini dengan nama yang berarti (dalam hal ini, "Nano S+"). Perhatikan bahwa semua aplikasi yang terinstal di perangkat akan terus berfungsi secara normal.

![Configurer clé principale](assets/fr/08.webp)

Selanjutnya, atur penundaan pengembalian, yaitu waktu setelah dana dapat dibelanjakan oleh *kunci warisan*. Penundaan ini ditentukan dalam bentuk blok, dengan setiap blok dipisahkan oleh rata-rata 10 menit. Kisarannya bisa dari 10 menit (1 blok) hingga sekitar 15 bulan (65.535 blok). Batas atas ini merupakan batasan protokol Bitcoin, karena waktu penguncian dikodekan pada 16 bit.

Kecuali dalam kondisi khusus, pilihlah waktu tunggu terpanjang: 15 bulan atau 65.535 blok. Ini akan menghemat biaya. Namun, kami menyarankan agar Anda melakukan prosedur pembaruan (dijelaskan di bagian "Memperbarui portofolio") setahun sekali, selalu pada waktu yang sama, untuk "meritualkan" praktik ini dan menghindari lupa.

Di sini, kami telah menyiapkan waktu pemulihan selama satu jam (6 blok) untuk melakukan pengujian.

![Configurer temps de verrouillage](assets/fr/09.webp)

Terakhir, siapkan kunci harta Anda. Kunci ini (atau lebih tepatnya, kumpulan kunci) akan digunakan untuk memulihkan dana jika Anda hilang. Klik "*Set*", pilih perangkat penandatanganan dan validasi pembagian kunci publik yang diperluas di dalamnya.

Untuk tutorial ini, kami memilih Jade. Berikan nama yang menarik pada kunci tersebut (di sini "Jade"). Seperti pada perangkat pertama, akun konvensional akan terus berfungsi.

![Configurer clé de succession](assets/fr/10.webp)

Setelah semua tindakan ini selesai, periksa apakah semuanya sudah sesuai dan klik "*Lanjutkan*" untuk mengonfirmasi pilihan Anda.

![Confirmer clés](assets/fr/11.webp)

Langkah selanjutnya adalah menyimpan deskriptor portofolio Anda. Ini adalah informasi yang Anda perlukan untuk menemukan dana di akun Anda. Berlawanan dengan frasa mnemonik, deskriptor tidak mengizinkan Anda untuk membelanjakan dana, jadi mengungkapkannya hanya akan menimbulkan masalah kerahasiaan (orang tersebut akan mengetahui semua transaksi Anda).

Simpan dua salinan deskriptor pada media elektronik, seperti stik USB. Pastikan Anda juga mencetak dua salinan di atas kertas, sehingga Anda dapat mengaksesnya jika terjadi kerusakan pada media elektronik. Setiap cadangan harus dikaitkan dengan perangkat tanda tangan.

![Sauvegarder descripteur](assets/fr/12.webp)

Deskriptor kami (yang dianalisis di akhir tutorial) adalah sebagai berikut:

```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```

Langkah terakhir dalam konfigurasi portofolio awal adalah memverifikasi deskriptor di setiap portofolio perangkat keras yang berfungsi sebagai perangkat tanda tangan.

![Enregistrer descripteur](assets/fr/13.webp)

Lakukan hal yang sama untuk setiap perangkat penandatanganan. Anda perlu memeriksa dan mengonfirmasi bahwa deskriptor telah ditambahkan ke setiap portofolio perangkat keras.

![Enregistrer descripteur Nano S Plus](assets/fr/14.webp)

Informasi dompet Anda sudah terdaftar, dan yang tersisa hanyalah mengonfigurasi bagaimana Anda ingin terhubung ke jaringan Bitcoin. Anda bisa memilih untuk menggunakan node Anda sendiri (lokal atau jarak jauh) atau menggunakan infrastruktur WizardSardine. Pada kasus terakhir, Anda perlu menautkan alamat email ke dompet Anda, yang akan memungkinkan Anda untuk mengambil deskriptor. WizardSardine akan memiliki akses ke semua transaksi Anda. Oleh karena itu, opsi pertama disarankan.

![Sélectionner connexion réseau](assets/fr/15.webp)

Kami telah memilih untuk menggunakan node kami sendiri. Anda dapat menggunakan node yang sudah ada, atau memasang *pruned node* pada mesin Anda. Jika Anda tidak memiliki akses ke node lain, instal node Anda sendiri pada mesin Anda, yang akan memakan waktu (dalam beberapa hari).

![Choisir type de nœud](assets/fr/16.webp)

Untuk tutorial ini, kami menggunakan server Electrum (publik) yang sudah ada. Namun, berhati-hatilah! Server ini memiliki akses ke semua aktivitas kita dengan dompet Liana. Jadi, gunakanlah node Anda sendiri jika Anda ingin melindungi privasi Anda.

![Connexion serveur Electrum public](assets/fr/17.webp)

Setelah konfigurasi node selesai, layar utama akan terbuka, menampilkan dompet Liana yang baru saja Anda buat.

Manfaatkan kesempatan ini untuk menyimpan unit pemulihan di tempat yang aman. Unit ini harus disimpan di lokasi yang strategis, sehingga dapat ditemukan oleh ahli waris Anda jika Anda meninggal dunia.

Untuk keamanan tambahan, Anda dapat menempatkan komponen yang digunakan untuk pemulihan di dalam kantong tertutup (*kantong anti rusak*) dan menuliskan nomor serinya di suatu tempat. Hal ini akan memastikan bahwa tidak ada orang yang mengaksesnya, dan perangkat Anda tetap valid.

Dalam contoh kami, kami telah menyusun elemen-elemen berikut ini:


- Blockstream Jade sebagai perangkat khas untuk perkebunan;
- Kabel USB untuk menghubungkan dan mengisi ulang daya perangkat;
- Cadangan kertas dari kalimat jika terjadi kegagalan fungsi atau kerusakan pada perangkat (perhatikan bahwa medianya juga dapat berupa logam, dan oleh karena itu terlindung dari elemen, seperti halnya dengan kapsul Cryptosteel, misalnya);
- Kunci USB yang berisi deskriptor portofolio ;
- Cadangan kertas deskriptor, jika terjadi kegagalan fungsi atau kerusakan pada kunci USB (cadangan ini belum difoto di sini);
- Surat suksesi yang menjelaskan langkah-langkah yang harus diambil untuk memulihkan dana.

![Éléments de récupération](assets/fr/18.webp)

Dan kami menempatkan barang-barang ini di bawah segel!

![Sachet scellé récupération](assets/fr/19.webp)

## Penerimaan dana

Layar utama Liana menampilkan saldo Anda dan transaksi (lampau dan saat ini) yang terkait dengan portofolio Anda. Dalam kasus kami, saldonya nol, dan ini normal.

![Écran principal](assets/fr/20.webp)

Untuk menerima dana, buka tab "*Terima*" dan klik "*Buat alamat*". Alamat baru akan muncul di layar Anda. Alamat ini lebih panjang dari alamat portofolio konvensional: alamat ini adalah alamat yang terhubung dengan kontrak yang berdiri sendiri (P2WSH atau Taproot).

![Générer nouvelle adresse](assets/fr/21.webp)

Anda perlu memverifikasi alamat ini pada portofolio perangkat keras Anda dengan mengeklik "*Verifikasi pada perangkat keras*".

![Vérifier adresse portefeuille matériel](assets/fr/22.webp)

Setelah dana terkirim, transaksi akan muncul di layar utama (pertama sebagai belum dikonfirmasi, kemudian sebagai dikonfirmasi). Di sini, kami telah mengirim 50.000 satoshi (lebih dari $50 pada saat transfer) untuk pengujian ini. Sudah jelas bahwa jumlah yang ditransfer dalam kasus Anda harus lebih besar dari nilai ini, karena adanya biaya transaksi.

![Vérifier solde](assets/fr/23.webp)

Anda dapat memeriksa status kedaluwarsa dana Anda dengan membuka tab "*Coins*". Tab ini menunjukkan kepada Anda berbagai koin (UTXO) yang ada di dompet Anda. Di sini, kita dapat melihat bahwa koin 50.000 satoshi yang dibuat oleh transaksi kita akan kedaluwarsa pada hari yang sama (dalam waktu satu jam).

![Obtenir informations pièce](assets/fr/24.webp)

Untuk lebih memahami model representasi UTXO yang digunakan dalam Bitcoin, Anda dapat membaca bagian pertama dari kursus tentang kerahasiaan dalam Bitcoin yang ditulis oleh Loïc Morel :

https://planb.network/courses/btc204
## Pengeluaran saat ini

Pengeluaran saat ini adalah situasi normal untuk menggunakan Liana. Mengirim bitcoin dengan kunci utama berfungsi seperti pada semua dompet Bitcoin klasik seperti Electrum atau Sparrow.

Untuk melakukan pembayaran, buka tab "*Kirim*" dan masukkan informasi penting: alamat BTC penerima, jumlah yang akan dikirim, dan tarif yang diinginkan. Deskripsi (disimpan secara lokal) juga dapat ditambahkan untuk kenyamanan Anda. Dalam contoh kami, kami mengirim 10.000 satoshi ke Bob tertentu, dengan tarif biaya 4 sat/ov, atau $ 0,67 pada saat transaksi.

Liana juga menawarkan "kontrol koin": Anda dapat menentukan koin (UTXO) mana yang ingin Anda belanjakan. Di sini, kami memilih koin 50.000 satoshi yang telah dibuat sebelumnya.

![Envoyer fonds clé principale](assets/fr/25.webp)

Kemudian tandatangani transaksi dengan perangkat tanda tangan Anda yang terhubung dengan kunci utama dengan mengklik "*Tanda Tangan*". Anda harus memverifikasi dan mengonfirmasi transaksi pada dompet perangkat keras Anda. Di sini, kami menggunakan Nano S Plus untuk menandatangani transaksi.

![Signer transaction clé principale](assets/fr/26.webp)

Terakhir, siarkan transaksi melalui jaringan dengan mengklik "*Broadcast*". Harap diperhatikan bahwa pengiriman dana akan mengatur ulang waktu pemulihan untuk koin yang digunakan.

![Diffuser transaction clé principale](assets/fr/27.webp)

Transaksi akan muncul di layar utama dan saldo Anda akan diperbarui.

![Solde après dépense](assets/fr/28.webp)

## Pembaruan portofolio

Seperti yang telah dijelaskan di atas, dompet Liana mengharuskan Anda untuk memperbarui dana Anda secara teratur dengan melakukan transaksi pada blockchain. Jika Anda tidak melakukannya, dana Anda dapat dipulihkan oleh ahli waris Anda (atau oleh perangkat kedua Anda dalam kasus cadangan yang disempurnakan). Situasi ini tidak terlalu berbahaya, tetapi hal ini mengalahkan tujuan dari pengaturan mekanisme ini: untuk tetap memegang kendali atas bitcoin Anda tanpa bantuan pihak ketiga yang tepercaya, dan juga mendapatkan keuntungan dari sebuah jaring pengaman.

Sebuah peringatan akan ditampilkan sebelum dana Anda (atau sebagian dari dana tersebut) kedaluwarsa dan dapat digunakan oleh kunci pemulihan. Ini akan menunjukkan bahwa "jalur pemulihan" Anda (*jalur pemulihan*) akan segera tersedia. Mengingat singkatnya waktu pemulihan kami (satu jam), pesan ini ditampilkan secara langsung dalam kasus kami.

![Avertissement chemin récupération](assets/fr/29.webp)

Ketika tenggat waktu mendekati, sebuah tombol akan muncul dan meminta Anda untuk memperbarui dana yang bersangkutan.

![Actualiser pièces depuis l'écran principal](assets/fr/30.webp)

Untuk memperbarui koin Anda, buka tab "*Koin*" dan klik "*Refresh koin*" di kotak koin yang sesuai. Jika Anda memiliki beberapa koin, Anda harus menyegarkannya satu per satu, dan dalam interval yang relatif singkat, untuk alasan kerahasiaan. Untuk menekan biaya, Anda bisa mengkonsolidasikan dana Anda dengan mengirimkan seluruh portofolio ke alamat penerima yang baru, namun hal ini akan mempengaruhi kerahasiaan Anda.

![Actualiser pièce](assets/fr/31.webp)

Tentukan tarif biaya yang diinginkan untuk transaksi tersebut. Karena ini adalah transfer ke diri Anda sendiri, Anda dapat menetapkan tarif biaya yang cukup rendah, terutama jika Anda melakukannya beberapa hari sebelum masa berlaku habis.

![Transfert à soi-même](assets/fr/32.webp)

Transaksi (berlabel "*transfer mandiri*") hanya akan terlihat di tab "*Transaksi*".

![Transactions après auto-transfert](assets/fr/33.webp)

Setelah dikonfirmasi, koin Anda aman! Anda bisa tenang sampai tanggal kedaluwarsa berikutnya.

## Pemulihan Bitcoin

Ketika memulihkan dana dari portofolio Liana, Anda mungkin dihadapkan pada salah satu dari dua situasi. Anda mungkin memiliki akses ke komputer tempat perangkat lunak diinstal, dalam hal ini yang harus Anda lakukan adalah membukanya (yang akan terjadi pada kasus model pencadangan yang disempurnakan). Namun, Anda mungkin tidak memiliki akses ke komputer ini, jadi kita akan mulai dari awal di sini. Perhatikan bahwa prosedur pemulihannya sama pada kedua kasus tersebut.

Untuk memulai, unduh Liana dari [situs web resmi Wizardsardine] (https://wizardsardine.com/liana/), atau dari [repositori GitHub] (https://github.com/wizardsardine/liana/releases), di mana Anda dapat memeriksa keaslian perangkat lunak. Instal perangkat lunak dan jalankan. Versi yang digunakan dalam kasus kami adalah 0.9, jadi tampilannya mungkin sudah berubah. Pada layar selamat datang, pilih opsi "Tambahkan dompet Liana yang sudah ada".

![Ajouter portefeuille existant](assets/fr/34.webp)

Konfigurasikan bagaimana Anda ingin terhubung ke jaringan. Anda bisa memilih untuk menggunakan node Anda sendiri (lokal atau jarak jauh) atau menggunakan infrastruktur WizardSardine. Dalam kasus terakhir, Anda akan membutuhkan alamat email yang digunakan oleh pembuat portofolio, sehingga dana dapat ditemukan secara otomatis. Jika Anda tidak memiliki informasi ini, pilih opsi pertama.

![Sélectionner connexion réseau](assets/fr/35.webp)

Jika Anda menggunakan node Anda sendiri, impor deskriptor portofolio. Ini adalah deskripsi teknis akun, yang memungkinkan Anda untuk mengambil dana yang tersimpan di dalamnya. Dalam kasus kami, ini adalah informasi berikut:

```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```

![Importer descripteur](assets/fr/36.webp)

Liana kemudian meminta Anda untuk memasukkan frasa mnemonik. Jika Anda memiliki perangkat tanda tangan yang berfungsi (dompet perangkat keras), lewati bagian ini. Jika perangkat Anda hilang atau rusak, tetapi Anda memiliki 12 atau 24 kata yang sesuai, Anda masih bisa menggunakan opsi ini. Untuk berjaga-jaga (jika jumlah yang akan dipulihkan cukup besar), kami tetap menyarankan anda untuk mendapatkan dompet perangkat keras yang baru dan menggunakan mnemonik untuk memulihkan kunci-kunci di dalamnya.

Dalam kasus kami, kami menggunakan dompet perangkat keras Blockstream Jade sebagai perangkat pemulihan dan memilih untuk melewatkan ("*Skip*") langkah ini.

![Passer phrase mnémotechnique](assets/fr/37.webp)

Periksa dan simpan deskriptor di perangkat tanda tangan Anda dengan memilihnya di layar. Jika dompet perangkat keras Anda tidak muncul, periksa apakah perangkat tersebut terhubung dan tidak terkunci. Periksa dan konfirmasikan bahwa informasi ini telah ditambahkan ke perangkat Anda.

![Enregistrer descripteur sur l'appareil de récupération](assets/fr/38.webp)

Konfigurasikan node Anda. Anda dapat menggunakan node yang sudah ada atau menginstal *pruned node* pada mesin Anda. Dalam kasus kami, kami menggunakan node yang sudah ada.

![Choisir type de nœud](assets/fr/39.webp)

Untuk tutorial ini, kami menggunakan server Electrum publik. Akan tetapi, server ini memiliki akses ke semua aktivitas kita dengan dompet Liana. Jika Anda ingin melindungi privasi Anda, Anda sebaiknya menggunakan node Anda sendiri.

![Connexion serveur Electrum public](assets/fr/17.webp)

Setelah Anda menyiapkan node, Anda akan dibawa ke layar dompet utama, di mana Anda bisa melihat saldo dan transaksi sebelumnya yang ditautkan ke akun tersebut. Anda juga dapat melihat apakah dana dapat diambil. Di sini, kita melihat bahwa koin dapat diambil.

![Accueil Liana récupération](assets/fr/40.webp)

Untuk memulihkan dana dalam portofolio, buka Pengaturan ("*Pengaturan*") di bagian kiri bawah dan klik "*Pemulihan*".

![Récupération dans paramètres](assets/fr/41.webp)

Keluarkan koin ke dalam dompet dengan mencentang kotak yang sesuai. Tunjukkan alamat BTC yang ingin Anda kirimkan dana, serta tarif biaya transaksi. Kemudian klik "*Selanjutnya*".

![Récupération des pièces](assets/fr/42.webp)

Tanda tangani transaksi dengan mengeklik "*Tanda tangani*" dan validasi transaksi pada dompet perangkat keras Anda.

![Signer transaction clé de récupération](assets/fr/43.webp)

Kemudian, siarkan melalui jaringan dengan mengeklik "*Broadcast*".

![Diffuser transaction clé de récupération](assets/fr/44.webp)

Transaksi akan muncul di layar utama. Setelah dikonfirmasi, pemulihan selesai!

![Écran principal après récupération](assets/fr/45.webp)

## Video

Jika Anda ingin tahu lebih banyak tentang Liana, ada beberapa konten video yang akan memberi Anda gambaran yang lebih jelas tentang cara kerjanya. Berikut ini adalah video presentasi Liana bersama Kévin Loaec dan Antoine Poinsot :

![Vidéo de présentation avec Kévin Loaec et Antoine Poinsot](https://youtu.be/siuLmQo1lM8)

Dan berikut ini adalah tutorial tentang cara menggunakan Liana, dengan Antoine Poinsot :

![Vidéo-tutoriel avec Antoine Poinsot](https://youtu.be/JrG4WMVPZDQ)

Manipulasi yang ditunjukkan dalam gambar terakhir, serupa dengan yang disajikan dalam tutorial ini.

## Bonus: analisis deskriptor

Deskriptor adalah string karakter yang dapat dibaca manusia yang secara lengkap menjelaskan serangkaian alamat. Deskriptor menggabungkan sejumlah informasi penting untuk mengambil bagian-bagian (UTXO) dari portofolio tingkat lanjut. Cara penulisan deskriptor didasarkan pada [Miniscript syntax] (https://bitbox.swiss/blog/understanding-bitcoin-miniscript-part-2/), bahasa skrip yang dikembangkan oleh Andrew Poelstra, Pieter Wuille, dan Sanket Kanjalkar pada tahun 2019.

Untuk lebih memahami mengapa string karakter ini penting, mari kita analisis deskriptor dalam contoh kita, yaitu :

```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```

Informasi berikut ini dapat diekstrak dari deskriptor ini:


- `wsh` (kependekan dari *witness script hash*): Ini adalah jenis keluaran transaksional yang dibuat. Jika kita memilih untuk menggunakan Taproot, pengenalnya adalah `tr`.
- `atau_d`: Ini adalah operator logika yang menunjukkan bahwa *salah satu dari dua* kondisi berikut ini harus dipenuhi agar pengeluaran dapat diterima (`_d` menunjukkan sintaks tertentu).
- `pk` (kependekan dari *public key*): Operator ini memeriksa tanda tangan yang diberikan terhadap kunci publik berikut, dan memberikan jawaban sebagai Boolean (TRUE atau FALSE).
- `[3689a8e7/48'/0'/0'/2']`: Elemen ini termasuk *sidik jari* dari kunci utama untuk dompet perangkat keras utama (dalam hal ini Nano S Plus), dan jalur turunan ke kunci pribadi yang diperluas yang ditautkan (yang darinya semua kunci pribadi lainnya diturunkan).
- `xpub6FKY ... WQa`: Ini adalah kunci publik yang diperluas yang ditautkan ke portofolio perangkat keras utama (di sini Nano S Plus)
- `/<0;1>/*`: Ini adalah jalur derivasi untuk mendapatkan kunci dan alamat sederhana: `0` untuk penerimaan, `1` untuk operasi internal (*change*), dengan "wildcard" (`*`) yang memungkinkan derivasi berurutan dari beberapa alamat dengan cara yang dapat dikonfigurasi, mirip dengan manajemen "gap limit" pada perangkat lunak portofolio klasik.
- dan_v`: Ini adalah operator logika yang mengindikasikan bahwa *dua kondisi berikut* harus dipenuhi agar pengeluaran dapat diterima (`_v` mengindikasikan sintaks tertentu).
- `v:pkh` (kependekan dari *verifikasi: hash kunci publik*): Operator ini memverifikasi tanda tangan dan kunci publik yang diberikan terhadap hash kunci publik (*hash*) yang mengikutinya. Pada dasarnya, ini adalah pemeriksaan yang sama dengan skrip P2PKH dan P2WPKH.
- `[42e629dd/48'/0'/0'/2']`: Ini adalah elemen yang sama seperti di atas (terdiri dari jejak dan jalur turunan), kecuali bahwa jejak kunci utama portofolio pemulihan perangkat keras (dalam hal ini Jade) diindikasikan.
- `xpub6DpQ ... WQd`: Ini adalah kunci publik yang diperluas yang terhubung ke dompet pemulihan perangkat keras (di sini adalah Jade).
- `older(6)` : Operator ini memeriksa bahwa output transaksi yang dibuat harus memiliki usia yang benar-benar lebih besar dari 6 blok agar dapat digunakan.

Item data terakhir (`8alrve5h`) adalah checksum deskriptor, dan berhubungan dengan pengenal portofolio.

Skrip yang dibuat oleh portofolio ini akan berbentuk sebagai berikut:

```plaintext
<primary_key> CHECKSIG IFDUP NOTIF DUP HASH160 <recovery_key_hash> EQUALVERIFY CHECKSIGVERIFY <locktime> CHECKSEQUENCEVERIFY ENDIF
```

Karena keamanan dompet Bitcoin Anda juga bergantung pada pemahaman Anda tentang cara kerjanya, saya sarankan Anda mempelajari mekanisme dompet deterministik dan hirarkis secara mendalam dengan mengikuti kursus pelatihan gratis di Plan ₿ Network:

https://planb.network/courses/cyp201