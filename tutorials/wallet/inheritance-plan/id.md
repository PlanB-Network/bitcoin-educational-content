---
name: Rencana warisan Bitcoin
description: Cara mentransfer bitcoin ke orang yang kamu cintai
---

![cover](assets/cover.webp)



Pengiriman bitcoin adalah tantangan teknis utama yang sering diabaikan banyak pemegangnya. Tidak seperti aset perbankan tradisional, di mana lembaga keuangan bisa mengirimkan dana kepada pemilik yang sah, Bitcoin beroperasi tanpa perantara. Orang yang kamu cintai tidak akan pernah bisa mengakses dana kamu tanpa informasi teknis yang diperlukan, terlepas dari keabsahan hukumnya.



Tutorial ini memandu kamu untuk membuat rencana warisan teknis. Kamu akan mempelajari bagaimana mekanisme on-chain bekerja untuk transmisi otomatis, bagaimana mendokumentasikan konfigurasi kamu, dan bagaimana memilih solusi yang tepat agar warisan Bitcoin kamu tetap bisa diakses oleh orang yang kamu cintai.



## Mengapa rencana warisan teknis sangat penting



Bitcoin didasarkan pada prinsip kriptografi yang mendasar: siapa pun yang memegang kunci privat mengendalikan dana. Kedaulatan ini justru menjadi kerentanan utama ketika pemegangnya menghilang tanpa mewariskan informasi yang diperlukan.



Rencana warisan Bitcoin harus memenuhi dua tujuan yang tampak bertentangan: memungkinkan orang yang kamu cintai mengakses dana kamu pada waktunya, sambil mencegah pihak lain mengaksesnya sebelum waktunya. Keseimbangan yang rumit ini bergantung pada kemampuan pemrograman bawaan Bitcoin.



Kompleksitas teknis menambah lapisan kesulitan tersendiri. Ahli waris kamu harus memahami konsep seperti seedphrase, deskriptor wallet, atau jalur derivasi. Tanpa persiapan yang memadai, bahkan ahli waris yang berniat baik pun berisiko melakukan kesalahan yang tidak bisa dibatalkan.




## Cara kerja pewarisan on-chain



Bitcoin menggunakan bahasa skripnya untuk mengkodekan kondisi pengeluaran secara langsung dalam transaksi. Pewarisan on-chain mengeksploitasi kemampuan pemrograman ini untuk membuat jalur pemulihan alternatif yang diaktifkan secara otomatis.



### Kunci waktu



Timelock adalah mekanisme dasar dalam pewarisan Bitcoin. Mekanisme ini memungkinkan dana dikunci sampai kondisi waktu tertentu terpenuhi.



**CLTV (CheckLockTimeVerify)**: Timelock absolut ini memeriksa bahwa waktu tertentu, baik berupa tanggal maupun tinggi blok, sudah tercapai sebelum pengeluaran disahkan. Contohnya, "dana ini hanya bisa dibelanjakan setelah blok 900000" atau "setelah 1 Januari 2026". Keunggulan CLTV adalah memungkinkan penundaan jangka panjang hingga beberapa tahun, tetapi tanggalnya bersifat tetap dan berlaku sama untuk semua UTXO dalam wallet. Untuk tetap mempertahankan kendali atas dana kamu, kamu perlu membuat wallet baru secara berkala dengan tanggal kedaluwarsa yang diperpanjang lalu memindahkan dana ke wallet tersebut.



**CSV (CheckSequenceVerify)**: Timelock relatif ini memverifikasi bahwa sejumlah blok telah berlalu sejak UTXO dibuat. Contohnya, "dana ini hanya bisa digunakan 52560 blok sekitar 1 tahun setelah diterima". Keunggulan CSV adalah setiap UTXO memiliki penghitungnya sendiri. Setiap kali kamu melakukan transaksi, UTXO baru yang tercipta akan mengatur ulang batas waktunya. Namun, batas teknis 65535 blok dengan maksimum sekitar 15 bulan membatasi jangka waktu yang bisa diterapkan. Pendekatan ini terasa lebih alami untuk penggunaan sehari-hari, karena aktivitas normal kamu secara otomatis memundurkan tenggat waktu.



### Beberapa jalur pengeluaran



Portofolio warisan menggabungkan beberapa jalur pengeluaran di setiap alamat:





- Jalur utama** : Pemilik dapat membelanjakan dananya kapan saja dengan kunci utamanya, tanpa batasan waktu.
- Jalur pemulihan **: Satu atau beberapa kunci alternatif dapat menghabiskan dana hanya setelah waktu yang ditetapkan berlalu.



Setiap transaksi yang dilakukan oleh pemilik akan "menyegarkan" UTXO, menciptakan output baru dengan pengunci waktu ulang. Mekanisme ini memastikan bahwa selama pemiliknya tetap aktif, jalur pemulihan tidak akan pernah aktif.



### Miniscript dan Taproot



**Miniscript** adalah bahasa terstruktur yang dikembangkan oleh Andrew Poelstra, Pieter Wuille, dan Sanket Kanjalkar untuk mempermudah penulisan dan analisis skrip Bitcoin yang kompleks. Bahasa ini memungkinkan kamu membuat kondisi pengeluaran yang mudah dibaca dan diverifikasi, yang sangat penting untuk konfigurasi pewarisan yang melibatkan beberapa kunci dan timelock.



**Taproot** (diaktifkan pada November 2021) secara signifikan meningkatkan mekanisme pewarisan on-chain. Berkat struktur pohonnya yang dikenal sebagai MAST, hanya kondisi pembelanjaan yang benar-benar digunakan yang akan terungkap di blockchain. Jika pemilik membelanjakan dananya secara normal, kondisi pewarisan tetap tersembunyi. Privasi ini juga membantu mengurangi biaya transaksi untuk jalur skrip yang kompleks.


## Pentingnya deskriptor secara kritis



Untuk wallet modern, seedphrase saja tidak cukup untuk memulihkan akses ke dana. **Deskriptor** menjadi elemen yang sangat penting.



Deskriptor adalah sebuah string yang sepenuhnya menjelaskan struktur wallet: public key yang terlibat, kondisi pengeluaran, jalur derivasi, serta timelock yang dikonfigurasi. Berikut contoh yang disederhanakan:



```
wsh(or_d(pk([fingerprint/path]xpub...),and_v(v:pkh([fingerprint/path]xpub...),older(52560))))
```



Deskriptor ini mengatakan: "baik kunci utama dapat langsung digunakan, atau kunci pemulihan dapat digunakan setelah 52560 blok".



Mari kita bongkar contoh ini:




- `wsh()` : Skrip Saksi Hash, menunjukkan jenis alamat (P2WSH)
- or_d()`: kondisi "atau" dengan cabang default
- pk([sidik jari/path]xpub...)`: Kunci publik utama dengan sidik jari dan jalur turunannya
- and_v()`: "dan" kondisi yang menggabungkan kunci pemulihan dengan kunci waktu
- `lebih tua (52560) `: Kunci waktu relatif dari 52560 blok



**Tanpa deskriptor, bahkan dengan semua seedphrase, ahli waris kamu tidak akan bisa membangun kembali wallet tersebut.** Wallet standar bisa dipulihkan hanya dari seedphrase karena mengikuti jalur derivasi standar seperti BIP44 atau BIP84. Wallet lama, sebaliknya, menggunakan skrip khusus yang tidak bisa ditebak begitu saja. Cadangan deskriptor, atau file konfigurasi yang diekspor dari software kamu, harus disertakan bersama seedphrase dalam rencana warisan kamu.



## Komponen dokumenter dari rencana warisan



Di luar mekanisme teknis, rencana warisan yang efektif bertumpu pada tiga pilar dokumentasi.



### Surat warisan



Surat pribadi ini menjadi pintu masuk ke rencana kamu. Ditujukan untuk ahli waris kamu, surat ini menjelaskan konteks serta langkah-langkah pencegahan yang harus diperhatikan.



Surat kamu harus secara eksplisit memuat aturan keselamatan berikut:



- Jangan terburu-buru, luangkan waktu untuk belajar sebelum memindahkan dana
- Jangan pernah memberikan seedphrase lengkap kepada satu orang saja
- Jangan pernah memasukkan seedphrase ke dalam software atau komputer yang tidak terverifikasi
- Waspadai penipuan dan orang yang menawarkan bantuan tanpa diminta
- Mintalah saran dari setidaknya dua orang yang kamu percaya sebelum mengambil keputusan apa pun



Surat ini juga memuat detail kontak notaris kamu dan lokasi surat wasiat kamu. Surat ini tidak boleh berisi seedphrase atau kata sandi apa pun.


### Direktori kontak tepercaya



Tidak ada ahli waris yang seharusnya menghadapi proses pemulihan bitcoin sendirian. Direktori ini berisi daftar orang-orang yang bisa memberikan bantuan teknis atau hukum.



Untuk setiap kontak, catat: nama lengkap, hubungan dengan kamu, peran dalam rencana tersebut, tingkat kepercayaan, keahlian di bidang Bitcoin, serta detail kontak lengkap. Aturan dasarnya: ahli waris kamu harus selalu berkonsultasi dengan setidaknya dua orang yang berbeda sebelum mengambil keputusan penting.



### Persediaan aset Bitcoin



Bagian ini memetakan semua bitcoin kamu dengan informasi teknis yang diperlukan untuk memulihkannya.



Untuk setiap portofolio, dokumentasikan :




- Jenis portofolio**: perangkat keras, perangkat lunak, konfigurasi (single-sig, multisig, warisan)
- Lokasi perangkat**: lokasi fisik perangkat keras wallet
- Descriptor/lokasi file konfigurasi**: penting untuk portofolio tingkat lanjut
- Lokasi backup phrase**: terpisah dari deskriptor
- Kode akses**: tempat penyimpanan PIN dan kata sandi
- Penundaan yang dikonfigurasi**: saat jalur pemulihan diaktifkan



## Solusi teknis yang tersedia



Beberapa paket perangkat lunak mengimplementasikan mekanisme pewarisan on-chain. Masing-masing memiliki karakteristik teknisnya sendiri.



### Liana



Liana adalah software desktop untuk Linux, macOS, dan Windows yang menggunakan Miniscript untuk membuat wallet dengan jalur pemulihan berbasis waktu. Proyek ini dikembangkan oleh Wizardsardine, yang didirikan bersama oleh Antoine Poinsot, seorang kontributor Bitcoin Core.



**Arsitektur teknis**: Secara default, Liana membuat wallet P2WSH asli SegWit, dengan dukungan Taproot yang tersedia tergantung pada kompatibilitas hardware wallet kamu. Arsitekturnya didasarkan pada satu jalur utama dan satu atau lebih jalur pemulihan. Deskriptor yang dihasilkan mengodekan seluruh kondisi tersebut dan wajib disimpan dengan aman.



**Timelock yang digunakan**: Liana menggunakan timelock relatif CSV, yang dibatasi hingga 65535 blok sekitar 15 bulan. Untuk tetap mempertahankan kontrol, kamu harus melakukan transaksi penyegaran sebelum batas waktu ini berakhir.



**Integrasi hardware wallet**: BitBox02, Blockstream Jade, Coldcard, Ledger, Specter DIY, serta perangkat lain kompatibel untuk menandatangani transaksi.



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

### Bitcoin Keeper



Bitcoin Keeper adalah aplikasi seluler untuk iOS dan Android yang menggabungkan multisig dan timelock melalui fitur "Brankas yang Disempurnakan". Pendekatan berbasis mobile dengan panduan terintegrasi membuatnya lebih mudah diakses oleh pengguna yang kurang teknis.



**Arsitektur teknis**: Enhanced Vaults menggunakan Miniscript untuk membuat konfigurasi multisig di mana kunci tambahan akan aktif setelah penundaan yang ditentukan. Kunci Warisan menambah kuorum yang sudah ada, sementara Kunci Darurat bisa melewati multisig sepenuhnya.



**Timelock yang digunakan**: Bitcoin Keeper menggunakan timelock absolut CLTV, yang memungkinkan masa tunggu lebih dari 15 bulan. Tanggal aktivasi ditetapkan saat wallet dibuat dan berlaku untuk semua UTXO. Aplikasi ini juga menyertakan fungsi "revaulting" yang secara otomatis mengelola penyegaran: kamu cukup mengikuti langkah-langkah yang dipandu tanpa perlu membuat wallet baru secara manual.



**Fitur tambahan**: Dokumen warisan yang terintegrasi, Dompet Canary untuk mendeteksi kompromi kunci, dan pengingat penyegaran.



https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-7f2a160b-10b6-4cc5-8820-514ee2eb1599

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

### Warisan



Heritage adalah aplikasi desktop yang menggunakan skrip Taproot untuk mengodekan kondisi pewarisan. Penggunaan Taproot memberikan privasi yang lebih baik, karena jalur yang tidak digunakan tetap tersembunyi di blockchain.



**Arsitektur teknis**: Setiap alamat Heritage mengintegrasikan jalur utama dan jalur alternatif untuk masing-masing ahli waris, dengan jangka waktu yang progresif. Struktur hierarkis ini memungkinkan kamu menetapkan cadangan pribadi pada 6 bulan dan ahli waris keluarga pada 12 hingga 15 bulan.



**Mode penggunaan**: Tersedia versi mandiri dengan node kamu sendiri yang gratis, atau layanan terkelola yang menambahkan pengingat serta notifikasi kepada ahli waris dengan biaya 0,05% per tahun.



https://planb.academy/tutorials/wallet/desktop/heritage-0549701f-2619-4037-ad05-44982be73ef4

## Proses pemulihan ahli waris



Memahami proses pemulihan akan membantu kamu menyiapkan rencana yang efektif. Berikut adalah langkah-langkah teknis yang perlu diikuti oleh ahli waris.



### Persyaratan pemulihan



Ahli waris membutuhkan :


1. **File deskriptor atau konfigurasi** dari portofolio asli (format JSON atau teks, tergantung pada perangkat lunaknya)


2. **Frasa pemulihannya** (frasa yang terkait dengan kunci warisannya, biasanya 12 atau 24 kata)


3. **Perangkat lunak yang kompatibel** (Liana, Bitcoin Keeper, Heritage, atau Sparrow/Specter untuk deskriptor standar)


4. **Sambungan ke node Bitcoin** untuk memeriksa status penguncian waktu dan menyiarkan transaksi



### Langkah-langkah pemulihan



1. **Instal perangkat lunak** pada perangkat yang aman dan konfigurasikan koneksi ke jaringan Bitcoin (simpul pribadi atau server Electrum)


2. **Impor deskriptor** untuk merekonstruksi struktur portofolio. Perangkat lunak akan secara otomatis generate semua alamat yang digunakan


3. **Kembalikan kunci warisan** dari frasa pemulihan. Perangkat lunak akan memeriksa apakah kunci ini sesuai dengan salah satu kunci yang diotorisasi dalam deskriptor


4. **Sinkronisasi portofolio** untuk menemukan semua UTXO dan kondisi pengeluarannya


5. **Periksa masa berlaku timelock **: perangkat lunak akan menunjukkan untuk setiap UTXO apakah jalur pemulihan aktif


6. **Buat transaksi pemulihan** ke alamat yang hanya dikendalikan oleh ahli waris (idealnya satu wallet baru)


7. **Menandatangani dan menyiarkan transaksi di jaringan Bitcoin



Jika penguncian waktu belum berakhir, ahli waris harus menunggu. Perangkat lunak akan menampilkan tanggal atau blok yang memungkinkan untuk pemulihan. Selama masa tunggu ini, dana tetap aman di blockchain.



### Hal-hal yang perlu diperhatikan untuk ahli waris



Ahli waris harus memberi perhatian khusus pada :




- Memeriksa keaslian software yang diunduh** (checksum, tanda tangan)
- Jangan pernah membagikan seedphrase kamu** kepada siapa pun yang menawarkan bantuan
- Berkonsultasi dengan setidaknya dua orang yang kamu percaya** sebelum melakukan pemulihan
- Memindahkan dana ke wallet sederhana** yang sepenuhnya dia kendalikan setelah pemulihan




## Praktik terbaik



### Pemisahan informasi



Jangan pernah menyimpan semua informasi di satu tempat. Deskriptor harus dipisahkan dari frasa pemulihan, yang pada gilirannya dipisahkan dari kode PIN. Distribusi ini mempersulit akses bagi penyerang, namun tetap dapat diperoleh kembali oleh ahli waris Anda yang sah.



### Tes pemulihan



Sebelum menyetorkan dana yang signifikan, uji seluruh proses pemulihan dengan jumlah yang kecil. Pastikan kamu dapat memulihkan portofolio dari deskriptor dan frasa pemulihan pada perangkat kosong. Dokumentasikan langkah-langkah tersebut untuk ahli waris.



### Pemeliharaan kunci waktu



Rencanakan untuk menyegarkan timelock kamu sebelum masa berlakunya habis. Untuk timelock 12 bulan, lakukan transaksi setiap 9-10 bulan. Perangkat lunak biasanya menawarkan pengingat atau fungsi penyegaran otomatis.



### Pembaruan rencana



Konfigurasi Bitcoin kamu akan terus berkembang. Setiap perubahan signifikan seperti wallet baru, perubahan tenggat waktu, atau penambahan ahli waris harus tercermin dalam dokumentasi kamu. Tetapkan rutinitas peninjauan tahunan.



## Memilih pendekatan Anda



Pilihan di antara berbagai solusi ini bergantung pada profil teknis dan kebutuhan spesifik kamu.



**Liana** cocok untuk pengguna desktop yang lebih memilih software open source dengan kontrol penuh melalui node mereka sendiri. Konfigurasinya tetap mudah diakses berkat antarmuka yang dipandu. Timelock relatif CSV menyederhanakan pemeliharaan, karena aktivitas normal kamu secara otomatis memundurkan tenggat waktu. Batasannya adalah penundaan maksimum sekitar 15 bulan dengan 65535 blok.



**Bitcoin Keeper** ditujukan bagi pengguna seluler yang mencari antarmuka intuitif dengan dokumentasi pendamping yang terintegrasi. Aplikasi ini menawarkan dua jenis kunci khusus: Kunci Warisan yang menambah kuorum dan Kunci Darurat yang dapat melewatinya sepenuhnya. Timelock absolut CLTV memungkinkan masa tunggu lebih dari 15 bulan, dengan fungsi penyegaran ulang yang mempermudah proses refresh. Paket Diamond Hands membuka fitur vault tingkat lanjut.



**Heritage** dirancang untuk pengguna teknis yang menghargai privasi Taproot dan pewarisan hierarkis dengan penundaan progresif. Struktur pohon Taproot menyembunyikan kondisi pewarisan selama transaksi normal, dan hanya mengungkapkan kondisi yang benar-benar digunakan saat pemulihan.



Ketiga solusi ini memiliki satu kesamaan: semuanya memerlukan penyegaran berkala untuk mencegah aktivasi jalur pemulihan terlalu cepat. Konsekuensi ini adalah harga sekaligus jaminan dari mekanisme pewarisan on-chain tanpa pihak ketiga tepercaya. Jadwalkan pengingat rutin dan jadikan pemeliharaan ini sebagai bagian dari rutinitas manajemen Bitc



## Kesimpulan



Paket warisan Bitcoin yang bersifat teknis menggabungkan mekanisme kriptografi seperti timelock, Miniscript, dan Taproot dengan dokumentasi yang disiplin. Wallet tingkat lanjut memungkinkan kamu mewariskan bitcoin secara otomatis setelah periode tidak aktif, tanpa campur tangan pihak ketiga.



Elemen penting yang harus diwariskan kepada ahli waris kamu meliputi: deskriptor atau file konfigurasi, seedphrase, instruksi pemulihan yang rinci, serta detail kontak orang yang kompeten untuk membantu mereka.



Mulailah dengan memilih solusi teknis yang sesuai dengan profil kamu, uji dengan jumlah kecil, lalu dokumentasikan seluruhnya dalam rencana yang terstruktur. Kompleksitas di awal menjadi jaminan bahwa aset Bitcoin kamu bisa diwariskan dengan penuh keyakinan.



## Sumber daya



### Templat rencana warisan





- [Template Rencana Warisan Bitcoin (PDF)](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/resources/bet/seed-management-tools/assets/Bitcoin-Inheritance-Plan-Template.pdf) - Template Dokumentasi Plan ₿ Academy



### Referensi teknis





- [BIP-65 : OP_CHECKLOCKTIMEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki) - Spesifikasi kunci waktu absolut (CLTV)
- [BIP-112: OP_CHECKSEQUENCEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki) - Spesifikasi kunci waktu relatif (CSV)
- [Referensi Naskah Mini](https://bitcoin.sipa.be/miniscript/) - Dokumentasi Naskah Mini Resmi oleh Pieter Wuille



### Situs web solusi resmi





- [Liana Wallet](https://wizardsardine.com/liana/) - Wizardsardine
- [Bitcoin Keeper](https://bitcoinkeeper.app/) - Bithyve
- [Heritage Wallet](https://btc-heritage.com/) - Crypto7
