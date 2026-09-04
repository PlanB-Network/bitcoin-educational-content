---
name: Liana
description: Menyiapkan dan menggunakan dompet di Liana
---
![cover](assets/cover.webp)

Dalam tutorial ini, aku akan menjelaskan langkah demi langkah cara menggunakan aplikasi Liana di komputer. Di antaranya, kamu akan mempelajari cara menyiapkan rencana suksesi otomatis, menerima dan mengirim bitcoin dalam situasi normal, dan mengambil dana dari portofolio yang ada setelah periode tertentu.

Pada bulan Januari 2025, dompet perangkat keras yang kompatibel dengan Liana adalah: BitBox02, Blockstream Jade, Blockstream Jade Plus, COLDCARD MK4, COLDCARD Q, Ledger Nano S, Ledger Nano S Plus, Ledger Nano X, Ledger Flex, Specter DIY.

Jika kamu ingin memulihkan dana dari dompet Liana yang sudah ada, baca presentasi di bawah ini dan langsung ke bagian "Memulihkan bitcoin".

## Memperkenalkan perangkat lunak Liana

Liana adalah paket perangkat lunak sumber terbuka yang dirancang untuk pembuatan dan pengelolaan portofolio tingkat lanjut, terutama sebagai bagian dari sistem pewarisan otomatis atau mekanisme pencadangan yang kuat. Proyek ini telah dikembangkan sejak tahun 2022 oleh Wizardsardine, sebuah perusahaan yang didirikan bersama oleh Kévin Loaec dan Antoine Poinsot. Di situs web resminya, Liana disajikan sebagai "portofolio sederhana untuk kurasi pribadi, dengan fungsi pemulihan dan pewarisan". Perangkat lunak ini berjalan di komputer - Linux, MacOS, Windows - dan kode sumbernya (terbuka) tersedia [di GitHub](https://github.com/wizardsardine/liana).

Liana dibangun di atas kemampuan pemrograman Bitcoin untuk membuat sebuah dompet yang canggih. Secara khusus, ia memanfaatkan kunci waktu (*timelock*), yang mengizinkan dana untuk dibelanjakan hanya setelah periode waktu tertentu berlalu, dan yang terlibat dalam pemulihan Bitcoin. Dompet Liana terdiri dari beberapa jalur pengeluaran:

- Jalur pengeluaran utama yang selalu tersedia;
- Setidaknya satu jalur pemulihan, yang dapat diakses setelah waktu tertentu.

Diagram di bawah ini mengilustrasikan pengoperasian portofolio dengan dua jalur pengeluaran:


![Schéma explicatif](assets/fr/01.webp)

Operasi ini memungkinkanmu untuk mengatur berbagai konfigurasi, termasuk :


- Rencana suksesi (atau warisan), yang memungkinkan ahli waris untuk mendapatkan kembali dana jika pengguna meninggal dunia. Untuk informasi lebih lanjut mengenai hal ini, kami sarankan untuk membaca [bagian 4](https://planb.academy/courses/f3e3843d-1a1d-450c-96d6-d7232158b81f/233c88d3-2e8e-5eba-ac06-efe67a209038) dari kursus BTC102.
- Cadangan yang diperkuat dengan waktu pemulihan, memberikan pengguna kemungkinan untuk menggunakan dompetnya tanpa harus menyimpan seedphrase yang sesuai dan berisiko dicuri, misalnya saat terjadi pencurian.  
- Jaring pengaman untuk orang-orang yang baru memulai dengan Bitcoin: mereka akan mengelola dompet mereka sendiri, dan "wali" mereka (kerabat, misalnya) akan memiliki hak untuk mendapatkan kembali dana mereka setelah jangka waktu tertentu.  
- Skema tanda tangan multi-pihak (*multisig*) dengan persyaratan yang berkurang dari waktu ke waktu, untuk mengatasi hilangnya satu atau lebih peserta, seperti mitra perusahaan.  

Kekuatan besar Liana adalah bahwa ia memperkenalkan cara standar untuk menjamin pemulihan dana jika terjadi kehilangan kunci utama, yang digunakan untuk pengeluaran saat ini. Ini merupakan inovasi besar untuk penyimpanan dana yang bersih, yang penuh dengan risiko, terutama jika kamu tidak memiliki informasi yang memadai tentang masalah ini. Oleh karena itu, Liana dapat mendorong pengguna yang paling menghindari risiko sekalipun untuk berhenti menggunakan kustodian (seperti platform pertukaran) untuk menyimpan dana mereka dan mendapatkan kembali kepemilikan atas uang mereka, sesuai dengan etos cypherpunk Bitcoin.

Tentu saja, Liana memiliki kekurangan. Yang pertama adalah kamu harus memperbarui dompet secara teratur dengan melakukan transaksi di blockchain Bitcoin. Ini bisa jadi merepotkan (tergantung seberapa sering kamu menggunakan perangkat lunak ini) dan mahal (tergantung pada tingkat biaya pada saat itu), tetapi ini adalah harga yang harus dibayar untuk keamanan ekstra.

Poin negatif kedua mungkin kerahasiaan. Ketika kamu melibatkan orang lain dalam konfigurasi, orang tersebut mengetahui semua alamatmu dan oleh karena itu dapat memantau aktivitasmu. Namun, ini tidak akan menjadi masalah jika kamu memilih cadangan yang diperkuat, atau untuk rencana suksesi di mana pewarismu tidak memiliki pengetahuan langsung tentang detail portofolio.

## Persiapan

Dalam tutorial ini, kita akan menyiapkan rencana suksesi. Kita akan menggunakan:

- Ledger Nano S Plus, untuk pengeluaran sehari-hari;  
https://planb.academy/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

- Blockstream Jade, digunakan untuk memulihkan dana;  
https://planb.academy/tutorials/wallet/hardware/jade-7d62bf0c-f460-4e68-9635-af9b731dabc3

- Dua media penyimpanan (stik USB) untuk menyimpan deskriptor portofolio;  
- Surat suksesi, yang berisi instruksi untuk memulihkan dana;  
- Kantong tertutup bernomor, untuk memastikan bahwa perangkat pemulihan (Jade) belum pernah digunakan.


## Instalasi dan konfigurasi

Kunjungi situs web resmi Wizardsardine dan unduh Liana di https://wizardsardine.com/liana/. Anda juga dapat mengunduh versi terbaru [dari repositori GitHub](https://github.com/wizardsardine/liana/releases), di mana kamu dapat memeriksa keaslian perangkat lunak. Versi yang digunakan dalam tutorial ini adalah 0.9.

![Télécharger Liana](assets/fr/02.webp)

Untuk mengetahui cara memverifikasi keaslian dan integritas perangkat lunak secara manual sebelum instalasi, kami sarankan kamu membaca tutorial ini:

https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Instal perangkat lunak pada komputermu dan luncurkan. Pilih opsi "*Buat dompet Liana baru*" untuk mengonfigurasi dompetmu.

![Accueil Liana](assets/fr/03.webp)

Pilih jenis portofolio kamu. Jika kamu ingin menyiapkan pencadangan yang disempurnakan dengan waktu pemulihan, kamu bisa memilih opsi "*Buat sendiri*" dan memilih skema default. Ini akan bekerja dengan cara yang hampir sama, kecuali kamu tidak perlu mempertahankan seedphrase dompet perangkat keras.

Di sini kita mengabaikan kasus *Multisig yang diperluas*, yang mengatur konfigurasi yang lebih kompleks.

Untuk keperluan tutorial ini, kita akan menggunakan warisan sederhana.

![Choisir type de portefeuille](assets/fr/04.webp)

Berikut ini penjelasan singkatnya.

![Rapide explication](assets/fr/05.webp)

Setelah kamu membaca penjelasannya, kamu akan dapat mengatur kunci dompet Liana-mu. Ini adalah langkah yang sangat penting, karena menentukan karakteristik pengeluaran akunmu.

![Configurer clés](assets/fr/06.webp)

Pertama-tama, dalam menu "Pengaturan Lanjutan", kamu dapat menentukan "tipe deskriptor", yaitu cara penulisan kontrak pada chain. Kamu dapat memilih di antara dua jenis: P2WSH (SegWit) atau Taproot. Dalam kedua kasus tersebut, semantik dari ketentuan pengeluaran akan sama. Meskipun P2WSH membuat kontrak lebih mudah dipahami, Taproot lebih unggul karena menyembunyikan kondisi yang tidak terpakai dan menghemat biaya selama pengambilan.

Pilihan ini bersifat opsional: jika ragu, biarkan opsi default (P2WSH pada versi 0.9, tetapi ini dapat berubah).

![Choisir le type de descripteur](assets/fr/07.webp)

Selanjutnya, konfigurasikan kunci utama kamu (*kunci utama*). Kunci ini (atau lebih tepatnya, set kunci ini) akan digunakan untuk pengeluaran dana saat ini, yang tidak tunduk pada kondisi waktu apa pun. Dengan mengklik "*Set*", kamu dapat memilih *perangkat penandatanganan* yang sesuai. Dalam kasus kita, kita telah memilih dompet perangkat keras Ledger Nano S Plus.

Otorisasi berbagi kunci publik yang diperluas dari perangkat. Beri nama kunci ini dengan nama yang berarti (dalam hal ini, "Nano S+"). Perhatikan bahwa semua aplikasi yang terinstal di perangkat akan terus berfungsi secara normal.

![Configurer clé principale](assets/fr/08.webp)

Selanjutnya, atur penundaan pengembalian, yaitu waktu setelah dana dapat dibelanjakan oleh *kunci warisan*. Penundaan ini ditentukan dalam bentuk blok, dengan setiap blok dipisahkan oleh rata-rata 10 menit. Kisarannya bisa dari 10 menit (1 blok) hingga sekitar 15 bulan (65.535 blok). Batas atas ini merupakan batasan protokol Bitcoin, karena waktu penguncian dikodekan pada 16 bit.

Kecuali dalam kondisi khusus, pilihlah waktu tunggu terpanjang: 15 bulan atau 65.535 blok. Ini akan menghemat biaya. Namun, kami menyarankan agar kamu melakukan prosedur pembaruan (dijelaskan di bagian "Memperbarui portofolio") setahun sekali, selalu pada waktu yang sama, untuk "meritualkan" praktik ini dan menghindari lupa.

Di sini, kita telah menyiapkan waktu pemulihan selama satu jam (6 blok) untuk melakukan pengujian.

![Configurer temps de verrouillage](assets/fr/09.webp)

Terakhir, siapkan kunci harta kamu. Kunci ini (atau lebih tepatnya, kumpulan kunci) akan digunakan untuk memulihkan dana jika kamu hilang. Klik "*Set*", pilih perangkat penandatanganan dan validasi pembagian kunci publik yang diperluas di dalamnya.

Untuk tutorial ini, kita memilih Jade. Berikan nama yang menarik pada kunci tersebut (di sini "Jade"). Seperti pada perangkat pertama, akun konvensional akan terus berfungsi.

![Configurer clé de succession](assets/fr/10.webp)

Setelah semua tindakan ini selesai, periksa apakah semuanya sudah sesuai dan klik "*Lanjutkan*" untuk mengonfirmasi pilihan kamu.

![Confirmer clés](assets/fr/11.webp)

Langkah selanjutnya adalah menyimpan deskriptor portofolio kamu. Ini adalah informasi yang kamu perlukan untuk menemukan dana di akunmu. Berlawanan dengan seedphrase, deskriptor tidak mengizinkan kamu untuk membelanjakan dana, jadi mengungkapkannya hanya akan menimbulkan masalah kerahasiaan (orang tersebut akan mengetahui semua transaksi kamu).

Simpan dua salinan deskriptor pada media elektronik, seperti stik USB. Pastikan kamu juga mencetak dua salinan di atas kertas, sehingga dapat mengaksesnya jika terjadi kerusakan pada media elektronik. Setiap cadangan harus dikaitkan dengan perangkat penandatanganan.


![Sauvegarder descripteur](assets/fr/12.webp)

Deskriptor kami (yang dianalisis di akhir tutorial) adalah sebagai berikut:

```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```

Langkah terakhir dalam konfigurasi portofolio awal adalah memverifikasi deskriptor di setiap portofolio perangkat keras yang berfungsi sebagai perangkat tanda tangan.

![Enregistrer descripteur](assets/fr/13.webp)

Lakukan hal yang sama untuk setiap perangkat penandatanganan. Kamu perlu memeriksa dan mengonfirmasi bahwa deskriptor telah ditambahkan ke setiap portofolio perangkat keras.

![Enregistrer descripteur Nano S Plus](assets/fr/14.webp)

Informasi dompet kamu sudah terdaftar, dan yang tersisa hanyalah mengonfigurasi bagaimana kamu ingin terhubung ke jaringan Bitcoin. Kamu bisa memilih untuk menggunakan node sendiri (lokal atau jarak jauh) atau menggunakan infrastruktur WizardSardine. Pada kasus terakhir, kamu perlu menautkan alamat email ke dompetmu, yang akan memungkinkan kamu untuk mengambil deskriptor. WizardSardine akan memiliki akses ke semua transaksi kamu. Oleh karena itu, opsi pertama disarankan.

![Sélectionner connexion réseau](assets/fr/15.webp)

Kami telah memilih untuk menggunakan node kami sendiri. Kamu dapat menggunakan node yang sudah ada, atau memasang *pruned node* pada mesinmu. Jika kamu tidak memiliki akses ke node lain, instal node sendiri pada mesinmu, yang akan memakan waktu (dalam beberapa hari).

![Choisir type de nœud](assets/fr/16.webp)

Untuk tutorial ini, kami menggunakan server Electrum (publik) yang sudah ada. Namun, berhati-hatilah! Server ini memiliki akses ke semua aktivitas kita dengan dompet Liana. Jadi, gunakanlah node Anda sendiri jika kamu ingin melindungi privasi kamu.

![Connexion serveur Electrum public](assets/fr/17.webp)

Setelah konfigurasi node selesai, layar utama akan terbuka, menampilkan dompet Liana yang baru saja kamu buat.

Manfaatkan kesempatan ini untuk menyimpan unit pemulihan di tempat yang aman. Unit ini harus disimpan di lokasi yang strategis, sehingga dapat ditemukan oleh ahli warismu jika kamu meninggal dunia.

Untuk keamanan tambahan, kamu dapat menempatkan komponen yang digunakan untuk pemulihan di dalam kantong tertutup (*kantong anti rusak*) dan menuliskan nomor serinya di suatu tempat. Hal ini akan memastikan bahwa tidak ada orang yang mengaksesnya, dan perangkatmu tetap valid.

Dalam contoh kami, kami telah menyusun elemen-elemen berikut ini:

- Blockstream Jade sebagai perangkat khas untuk pemulihan;  
- Kabel USB untuk menghubungkan dan mengisi ulang daya perangkat;  
- Cadangan kertas dari seedphrase jika terjadi kegagalan fungsi atau kerusakan pada perangkat (perhatikan bahwa medianya juga dapat berupa logam, dan oleh karena itu terlindung dari elemen, seperti halnya dengan kapsul Cryptosteel, misalnya);  
- Kunci USB yang berisi deskriptor portofolio;  
- Cadangan kertas deskriptor, jika terjadi kegagalan fungsi atau kerusakan pada kunci USB (cadangan ini belum difoto di sini);  
- Surat suksesi yang menjelaskan langkah-langkah yang harus diambil untuk memulihkan dana.


![Éléments de récupération](assets/fr/18.webp)

Dan kami menempatkan barang-barang ini di bawah segel!

![Sachet scellé récupération](assets/fr/19.webp)

## Penerimaan dana

Layar utama Liana menampilkan saldo kamu dan transaksi (lampau dan saat ini) yang terkait dengan portofolio kamu. Dalam kasus kami, saldonya nol, dan ini normal.

![Écran principal](assets/fr/20.webp)

Untuk menerima dana, buka tab "*Terima*" dan klik "*Buat alamat*". Alamat baru akan muncul di layar kamu. Alamat ini lebih panjang dari alamat portofolio konvensional: alamat ini adalah alamat yang terhubung dengan kontrak yang berdiri sendiri (P2WSH atau Taproot).

![Générer nouvelle adresse](assets/fr/21.webp)

Kamu perlu memverifikasi alamat ini pada portofolio perangkat keras milikmu dengan mengeklik "*Verifikasi pada perangkat keras*".

![Vérifier adresse portefeuille matériel](assets/fr/22.webp)

Setelah dana terkirim, transaksi akan muncul di layar utama (pertama sebagai belum dikonfirmasi, kemudian sebagai dikonfirmasi). Di sini, kami telah mengirim 50.000 satoshi (lebih dari $50 pada saat transfer) untuk pengujian ini. Sudah jelas bahwa jumlah yang ditransfer dalam kasusmu harus lebih besar dari nilai ini, karena adanya biaya transaksi.

![Vérifier solde](assets/fr/23.webp)

Kamu dapat memeriksa status kedaluwarsa dana kamu dengan membuka tab "*Coins*". Tab ini menunjukkan berbagai koin (UTXO) yang ada di dompetmu. Di sini, kita dapat melihat bahwa koin 50.000 satoshi yang dibuat oleh transaksi kita akan kedaluwarsa pada hari yang sama (dalam waktu satu jam).

![Obtenir informations pièce](assets/fr/24.webp)

Untuk lebih memahami model representasi UTXO yang digunakan dalam Bitcoin, kamu dapat membaca bagian pertama dari kursus tentang kerahasiaan dalam Bitcoin yang ditulis oleh Loïc Morel :

https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Pengeluaran saat ini

Pengeluaran saat ini adalah situasi normal untuk menggunakan Liana. Mengirim bitcoin dengan kunci utama berfungsi seperti pada semua dompet Bitcoin klasik seperti Electrum atau Sparrow.

Untuk melakukan pembayaran, buka tab "*Kirim*" dan masukkan informasi penting: alamat BTC penerima, jumlah yang akan dikirim, dan tarif yang diinginkan. Deskripsi (disimpan secara lokal) juga dapat ditambahkan untuk kenyamananmu. Dalam contoh kami, kami mengirim 10.000 satoshi ke Bob tertentu, dengan tarif biaya 4 sat/ov, atau $0,67 pada saat transaksi.

Liana juga menawarkan "kontrol koin": kamu dapat menentukan koin (UTXO) mana yang ingin kamu belanjakan. Di sini, kita memilih koin 50.000 satoshi yang telah dibuat sebelumnya.


![Envoyer fonds clé principale](assets/fr/25.webp)

Kemudian tandatangani transaksi dengan perangkat penandatanganan kamu yang terhubung dengan kunci utama dengan mengklik "*Tanda Tangan*". Kamu harus memverifikasi dan mengonfirmasi transaksi pada dompet perangkat kerasmu. Di sini, kita menggunakan Nano S Plus untuk menandatangani transaksi.

![Signer transaction clé principale](assets/fr/26.webp)

Terakhir, siarkan transaksi melalui jaringan dengan mengklik "*Broadcast*". Harap diperhatikan bahwa pengiriman dana akan mengatur ulang waktu pemulihan untuk koin yang digunakan.

![Diffuser transaction clé principale](assets/fr/27.webp)

Transaksi akan muncul di layar utama dan saldo kamu akan diperbarui.

![Solde après dépense](assets/fr/28.webp)

## Pembaruan portofolio

Seperti yang telah dijelaskan di atas, dompet Liana mengharuskan kamu untuk memperbarui dana secara teratur dengan melakukan transaksi pada blockchain. Jika tidak dilakukan, dana kamu dapat dipulihkan oleh ahli warismu (atau oleh perangkat kedua kamu dalam kasus cadangan yang disempurnakan). Situasi ini tidak terlalu berbahaya, tetapi hal ini mengalahkan tujuan dari pengaturan mekanisme ini: untuk tetap memegang kendali atas bitcoin tanpa bantuan pihak ketiga yang tepercaya, dan juga mendapatkan keuntungan dari sebuah jaring pengaman.

Sebuah peringatan akan ditampilkan sebelum dana kamu (atau sebagian dari dana tersebut) kedaluwarsa dan dapat digunakan oleh kunci pemulihan. Ini akan menunjukkan bahwa "jalur pemulihan" kamu (*jalur pemulihan*) akan segera tersedia. Mengingat singkatnya waktu pemulihan kami (satu jam), pesan ini ditampilkan secara langsung dalam kasus kami.

![Avertissement chemin récupération](assets/fr/29.webp)

Ketika tenggat waktu mendekati, sebuah tombol akan muncul dan meminta kamu untuk memperbarui dana yang bersangkutan.

![Actualiser pièces depuis l'écran principal](assets/fr/30.webp)

Untuk memperbarui koin kamu, buka tab "*Koin*" dan klik "*Refresh koin*" di kotak koin yang sesuai. Jika kamu memiliki beberapa koin, kamu harus menyegarkannya satu per satu, dan dalam interval yang relatif singkat, untuk alasan kerahasiaan. Untuk menekan biaya, kamu bisa mengkonsolidasikan dana dengan mengirimkan seluruh portofolio ke alamat penerima yang baru, namun hal ini akan mempengaruhi kerahasiaanmu.

![Actualiser pièce](assets/fr/31.webp)

Tentukan tarif biaya yang diinginkan untuk transaksi tersebut. Karena ini adalah transfer ke diri sendiri, kamu dapat menetapkan tarif biaya yang cukup rendah, terutama jika melakukannya beberapa hari sebelum masa berlaku habis.

![Transfert à soi-même](assets/fr/32.webp)

Transaksi (berlabel "*transfer mandiri*") hanya akan terlihat di tab "*Transaksi*".

![Transactions après auto-transfert](assets/fr/33.webp)

Setelah dikonfirmasi, koin milikmu aman! Kamu bisa tenang sampai tanggal kedaluwarsa berikutnya.

## Pemulihan Bitcoin

Ketika memulihkan dana dari portofolio Liana, kamu mungkin dihadapkan pada salah satu dari dua situasi. Kamu mungkin memiliki akses ke komputer tempat perangkat lunak diinstal, dalam hal ini yang harus dilakukan adalah membukanya (yang akan terjadi pada kasus model pencadangan yang disempurnakan). Namun, kamu mungkin tidak memiliki akses ke komputer ini, jadi kita akan mulai dari awal di sini. Perhatikan bahwa prosedur pemulihannya sama pada kedua kasus tersebut.

Untuk memulai, unduh Liana dari [situs web resmi Wizardsardine](https://wizardsardine.com/liana/), atau dari [repositori GitHub](https://github.com/wizardsardine/liana/releases), di mana kamu dapat memeriksa keaslian perangkat lunak. Instal perangkat lunak dan jalankan. Versi yang digunakan dalam kasus kami adalah 0.9, jadi tampilannya mungkin sudah berubah. Pada layar selamat datang, pilih opsi "Tambahkan dompet Liana yang sudah ada".

![Ajouter portefeuille existant](assets/fr/34.webp)

Konfigurasikan bagaimana kamu ingin terhubung ke jaringan. Kamu bisa memilih untuk menggunakan node sendiri (lokal atau jarak jauh) atau menggunakan infrastruktur WizardSardine. Dalam kasus terakhir, kamu akan membutuhkan alamat email yang digunakan oleh pembuat portofolio, sehingga dana dapat ditemukan secara otomatis. Jika kamu tidak memiliki informasi ini, pilih opsi pertama.

![Sélectionner connexion réseau](assets/fr/35.webp)

Jika kamu menggunakan node milikmu sendiri, impor deskriptor portofolio. Ini adalah deskripsi teknis akun, yang memungkinkan Anda untuk mengambil dana yang tersimpan di dalamnya. Dalam kasus kami, ini adalah informasi berikut:

```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```

![Importer descripteur](assets/fr/36.webp)

Liana kemudian meminta kamu untuk memasukkan seedphrase. Jika kamu memiliki perangkat penandatanganan yang berfungsi (dompet perangkat keras), lewati bagian ini. Jika perangkatmu hilang atau rusak, tetapi kamu memiliki 12 atau 24 kata yang sesuai, kamu masih bisa menggunakan opsi ini. Untuk berjaga-jaga (jika jumlah yang akan dipulihkan cukup besar), kami tetap menyarankan untuk mendapatkan dompet perangkat keras yang baru dan menggunakan seedphrase untuk memulihkan kunci-kunci di dalamnya.

Dalam kasus kami, kami menggunakan dompet perangkat keras Blockstream Jade sebagai perangkat pemulihan dan memilih untuk melewatkan ("*Skip*") langkah ini.

![Passer phrase mnémotechnique](assets/fr/37.webp)

Periksa dan simpan deskriptor di perangkat penandatanganan kamu dengan memilihnya di layar. Jika dompet perangkat kerasmu tidak muncul, periksa apakah perangkat tersebut terhubung dan tidak terkunci. Periksa dan konfirmasikan bahwa informasi ini telah ditambahkan ke perangkatmu.


![Enregistrer descripteur sur l'appareil de récupération](assets/fr/38.webp)

Konfigurasikan node kamu. Kamu dapat menggunakan node yang sudah ada atau menginstal *pruned node* pada mesinmu. Dalam kasus kami, kami menggunakan node yang sudah ada.

![Choisir type de nœud](assets/fr/39.webp)

Untuk tutorial ini, kami menggunakan server Electrum publik. Akan tetapi, server ini memiliki akses ke semua aktivitas kita dengan dompet Liana. Jika kamu ingin melindungi privasimu, sebaiknya gunakan node sendiri.

![Connexion serveur Electrum public](assets/fr/17.webp)

Setelah kamu menyiapkan node, kamu akan dibawa ke layar dompet utama, di mana kamu bisa melihat saldo dan transaksi sebelumnya yang ditautkan ke akun tersebut. Kamu juga dapat melihat apakah dana dapat diambil. Di sini, kita melihat bahwa koin dapat diambil.

![Accueil Liana récupération](assets/fr/40.webp)

Untuk memulihkan dana dalam portofolio, buka Pengaturan ("*Pengaturan*") di bagian kiri bawah dan klik "*Pemulihan*".

![Récupération dans paramètres](assets/fr/41.webp)

Keluarkan koin ke dalam dompet dengan mencentang kotak yang sesuai. Tunjukkan alamat BTC yang ingin kamu kirimkan dana, serta tarif biaya transaksi. Kemudian klik "*Selanjutnya*".

![Récupération des pièces](assets/fr/42.webp)

Tanda tangani transaksi dengan mengeklik "*Tanda tangani*" dan validasi transaksi pada dompet perangkat keras milikmu.

![Signer transaction clé de récupération](assets/fr/43.webp)

Kemudian, siarkan melalui jaringan dengan mengeklik "*Broadcast*".

![Diffuser transaction clé de récupération](assets/fr/44.webp)

Transaksi akan muncul di layar utama. Setelah dikonfirmasi, pemulihan selesai!

![Écran principal après récupération](assets/fr/45.webp)

## Bonus: analisis deskriptor

Deskriptor adalah string karakter yang dapat dibaca manusia yang secara lengkap menjelaskan serangkaian alamat. Deskriptor menggabungkan sejumlah informasi penting untuk mengambil bagian-bagian (UTXO) dari portofolio tingkat lanjut. Cara penulisan deskriptor didasarkan pada [Miniscript syntax](https://bitbox.swiss/blog/understanding-bitcoin-miniscript-part-2/), bahasa skrip yang dikembangkan oleh Andrew Poelstra, Pieter Wuille, dan Sanket Kanjalkar pada tahun 2019.

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

Karena keamanan dompet Bitcoin kamu juga bergantung pada pemahamanmu tentang cara kerjanya, aku sarankan kamu mempelajari mekanisme dompet deterministik dan hierarkis secara mendalam dengan mengikuti kursus pelatihan gratis di Plan ₿ Academy:

https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f
