---
name: Rencana warisan Bitcoin
description: Cara mentransfer bitcoin ke orang yang Anda cintai
---

![cover](assets/cover.webp)



Pengiriman bitcoin merupakan tantangan teknis utama yang diabaikan oleh banyak pemegangnya. Tidak seperti aset perbankan tradisional, di mana lembaga keuangan dapat mengirimkan dana kepada pemilik yang sah, Bitcoin bekerja tanpa perantara. Orang yang Anda cintai tidak akan pernah bisa mengakses dana Anda tanpa informasi teknis yang diperlukan, terlepas dari keabsahan hukumnya.



Tutorial ini memandu Anda dalam membuat rencana warisan teknis. Anda akan mempelajari cara kerja mekanisme on-chain untuk transmisi otomatis, cara mendokumentasikan konfigurasi Anda, dan cara memilih solusi yang tepat untuk memastikan bahwa warisan Bitcoin Anda tetap dapat diakses oleh orang yang Anda cintai.



## Mengapa rencana warisan teknis sangat penting



Bitcoin didasarkan pada prinsip kriptografi yang mendasar: siapapun yang memegang kunci pribadi akan mengontrol dana. Kedaulatan ini menjadi kerentanan utama ketika pemegangnya menghilang tanpa mengirimkan informasi yang diperlukan.



Rencana warisan Bitcoin harus memenuhi dua tujuan yang tampaknya bertentangan: mengizinkan orang yang Anda cintai untuk mengakses dana Anda ketika saatnya tiba, sambil mencegah orang lain mengaksesnya sebelum waktunya. Keseimbangan yang rumit ini bergantung pada kemampuan pemrograman asli Bitcoin.



Kompleksitas teknis menambah lapisan kesulitan ekstra. Ahli waris Anda harus memanipulasi konsep-konsep seperti frasa pemulihan, deskriptor portofolio, atau jalur turunan. Tanpa persiapan yang memadai, bahkan ahli waris yang berniat baik pun berisiko melakukan kesalahan yang tidak dapat diubah.



## Cara kerja pewarisan on-chain



Bitcoin menggunakan bahasa skripnya untuk mengkodekan kondisi pengeluaran secara langsung dalam transaksi. Pewarisan on-chain mengeksploitasi kemampuan pemrograman ini untuk membuat jalur pemulihan alternatif yang diaktifkan secara otomatis.



### Kunci waktu



Timelock adalah mekanisme dasar dari pewarisan Bitcoin. Mekanisme ini memungkinkan dana dikunci hingga kondisi waktu tertentu terpenuhi.



**CLTV (CheckLockTimeVerify)**: Pengunci waktu absolut ini memeriksa bahwa waktu tertentu (tanggal atau tinggi blok) telah tercapai sebelum mengesahkan pengeluaran. Sebagai contoh, "dana ini hanya dapat dibelanjakan setelah blok 900000" atau "setelah 1 Januari 2026". Keuntungan dari CLTV adalah memungkinkan penundaan yang lama (beberapa tahun), tetapi tanggalnya tetap dan berlaku sama untuk semua UTXO dalam portofolio. Untuk mempertahankan kendali atas dana Anda, Anda harus membuat portofolio baru secara berkala dengan tanggal kedaluwarsa yang diperpanjang dan mentransfer dana Anda ke portofolio tersebut.



**CSV (CheckSequenceVerify)**: Pengunci waktu relatif ini memverifikasi bahwa sejumlah blok telah berlalu sejak UTXO dibuat. Sebagai contoh, "dana ini hanya dapat digunakan 52560 blok (~1 tahun) setelah diterima". Keuntungan dari CSV adalah setiap UTXO memiliki penghitungnya sendiri-sendiri. Setiap kali Anda melakukan transaksi, UTXO yang baru dibuat akan mengatur ulang batas waktunya sendiri. Namun, batas teknis 65535 blok (maksimum ~15 bulan) membatasi jangka waktu yang memungkinkan. Pendekatan ini lebih alami untuk penggunaan sehari-hari, karena aktivitas normal Anda secara otomatis memundurkan tenggat waktu.



### Beberapa jalur pengeluaran



Portofolio warisan menggabungkan beberapa jalur pengeluaran di setiap alamat:





- Jalur utama** : Pemilik dapat membelanjakan dananya kapan saja dengan kunci utamanya, tanpa batasan waktu.
- Jalur pemulihan **: Satu atau beberapa kunci alternatif dapat menghabiskan dana hanya setelah waktu yang ditetapkan berlalu.



Setiap transaksi yang dilakukan oleh pemilik akan "menyegarkan" UTXO, menciptakan output baru dengan pengunci waktu ulang. Mekanisme ini memastikan bahwa selama pemiliknya tetap aktif, jalur pemulihan tidak akan pernah aktif.



### Miniscript dan Taproot



**Miniscript** adalah bahasa terstruktur yang dikembangkan oleh Andrew Poelstra, Pieter Wuille, dan Sanket Kanjalkar yang memudahkan untuk menulis dan menganalisis skrip Bitcoin yang kompleks. Bahasa ini memungkinkan Anda untuk membuat kondisi pengeluaran yang dapat dibaca dan diverifikasi, yang sangat penting untuk konfigurasi pewarisan yang melibatkan beberapa kunci dan pengatur waktu.



**Taproot** (diaktifkan pada November 2021) secara signifikan meningkatkan pewarisan on-chain. Berkat struktur pohonnya (MAST), hanya kondisi pembelanjaan yang digunakan yang terungkap di blockchain. Jika pemilik membelanjakan dananya secara normal, kondisi pewarisan tetap tidak terlihat. Kerahasiaan ini juga mengurangi biaya transaksi untuk jalur yang kompleks.



## Pentingnya deskriptor secara kritis



Untuk portofolio lama, frasa pemulihan (seed) tidak cukup untuk memulihkan akses ke dana. Deskripsi **deskriptor** menjadi elemen penting.



Deskriptor adalah sebuah string yang secara lengkap menjelaskan struktur portofolio: public key yang terlibat, kondisi pengeluaran, jalur derivasi, dan timelock yang dikonfigurasi. Berikut adalah contoh yang disederhanakan:



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



**Tanpa deskriptor, bahkan dengan semua frasa pemulihan, ahli waris Anda tidak akan dapat membangun kembali portofolio.** Portofolio standar hanya dapat dipulihkan dari seed karena mengikuti jalur penurunan standar (BIP44, BIP84). Portofolio lama, di sisi lain, menggunakan skrip khusus yang tidak dapat ditebak. Cadangan deskriptor (atau file konfigurasi yang diekspor oleh perangkat lunak Anda) harus menyertai frasa pemulihan dalam rencana warisan Anda.



## Komponen dokumenter dari rencana warisan



Di luar mekanisme teknis, rencana warisan yang efektif bertumpu pada tiga pilar dokumentasi.



### Surat warisan



Surat pribadi ini merupakan pintu masuk ke rencana Anda. Ditulis untuk ahli waris Anda, surat ini menjelaskan konteks dan tindakan pencegahan yang harus diambil.



Surat Anda harus menyertakan aturan keselamatan secara eksplisit:




- Jangan terburu-buru, luangkan waktu untuk belajar sebelum memindahkan dana
- Jangan pernah menyampaikan frasa pemulihan yang lengkap kepada satu orang saja
- Jangan pernah memasukkan frasa pemulihan ke dalam program perangkat lunak atau komputer yang tidak diverifikasi
- Waspadai penipuan dan orang yang menawarkan bantuan yang tidak diminta
- Mintalah saran dari setidaknya dua orang yang Anda percayai sebelum mengambil keputusan apa pun



Surat ini juga berisi detail kontak notaris Anda dan lokasi surat wasiat Anda. Surat ini tidak boleh berisi frasa atau kata sandi pemulihan.



### Direktori kontak tepercaya



Tidak ada ahli waris yang harus menghadapi pemulihan bitcoin sendirian. Direktori ini berisi daftar orang-orang yang dapat memberikan bantuan teknis atau hukum.



Untuk setiap kontak, catatlah: nama lengkap, hubungan dengan Anda, peran dalam rencana tersebut, tingkat kepercayaan, keahlian Bitcoin, dan detail kontak lengkap. Aturan dasarnya: ahli waris Anda harus selalu berkonsultasi dengan setidaknya dua orang yang berbeda sebelum mengambil keputusan penting.



### Persediaan aset Bitcoin



Bagian ini memetakan semua bitcoin Anda dengan informasi teknis yang diperlukan untuk memulihkannya.



Untuk setiap portofolio, dokumentasikan :




- Jenis portofolio**: perangkat keras, perangkat lunak, konfigurasi (single-sig, multisig, warisan)
- Lokasi perangkat**: lokasi fisik perangkat keras wallet
- Descriptor/lokasi file konfigurasi**: penting untuk portofolio tingkat lanjut
- Lokasi frasa pemulihan**: terpisah dari deskriptor
- Kode akses**: tempat penyimpanan PIN dan kata sandi
- Penundaan yang dikonfigurasi**: saat jalur pemulihan diaktifkan



## Solusi teknis yang tersedia



Beberapa paket perangkat lunak mengimplementasikan mekanisme pewarisan on-chain. Masing-masing memiliki karakteristik teknisnya sendiri.



### Liana



Liana adalah perangkat lunak desktop (Linux, macOS, Windows) yang menggunakan Miniscript untuk membuat portofolio dengan jalur pemulihan berjangka waktu. Proyek ini dikembangkan oleh Wizardsardine, yang didirikan bersama oleh Antoine Poinsot (kontributor Bitcoin Core).



**Arsitektur teknis**: Liana membuat portofolio P2WSH (asli SegWit) secara default, dengan dukungan Taproot yang tersedia tergantung pada kompatibilitas perangkat keras wallet Anda. Arsitektur ini didasarkan pada jalur utama dan satu atau lebih jalur pemulihan. Deskriptor yang dihasilkan mengkodekan semua kondisi dan harus disimpan.



**Kunci waktu yang digunakan**: Liana menggunakan penguncian waktu relatif (CSV), terbatas pada 65535 blok (~15 bulan). Untuk mempertahankan kontrol, Anda harus melakukan transaksi penyegaran sebelum kunci waktu berakhir.



**Integrasi perangkat keras wallet**: BitBox02, Blockstream Jade, Coldcard, Ledger, Specter DIY, dan perangkat lain kompatibel untuk menandatangani transaksi.



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

### Bitcoin Keeper



Bitcoin Keeper adalah aplikasi seluler (iOS, Android) yang menggabungkan multisig dan kunci waktu melalui "Brankas yang Disempurnakan". Pendekatan seluler dengan panduan terintegrasi membuatnya dapat diakses oleh pengguna yang kurang teknis.



**Arsitektur teknis**: Enhanced Vaults menggunakan Miniscript untuk membuat konfigurasi multisig di mana kunci tambahan diaktifkan setelah penundaan yang ditentukan. Kunci Warisan menambah kuorum yang ada, sedangkan Kunci Darurat dapat melewati multisig sepenuhnya.



**Kunci waktu yang digunakan**: Bitcoin Keeper menggunakan penguncian waktu absolut (CLTV), yang memungkinkan waktu tunggu lebih dari 15 bulan. Tanggal aktivasi ditetapkan pada saat pembuatan wallet dan berlaku untuk semua UTXO. Aplikasi ini menggabungkan fungsi "revaulting" yang secara otomatis mengelola penyegaran: pengguna cukup mengikuti langkah-langkah yang dipandu, tanpa harus membuat wallet baru secara manual.



**Fitur tambahan**: Dokumen warisan yang terintegrasi, Dompet Canary untuk mendeteksi kompromi kunci, dan pengingat penyegaran.



https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-7f2a160b-10b6-4cc5-8820-514ee2eb1599

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

### Warisan



Heritage adalah sebuah aplikasi desktop yang menggunakan skrip Taproot untuk mengkodekan kondisi warisan. Penggunaan Taproot menawarkan kerahasiaan yang lebih baik, karena jalur yang tidak digunakan tetap tidak terlihat di blockchain.



**Arsitektur teknis**: Setiap alamat Warisan mengintegrasikan jalur utama dan jalur alternatif untuk setiap ahli waris, dengan jangka waktu yang progresif. Struktur hirarkis memungkinkan untuk menentukan cadangan pribadi pada 6 bulan dan ahli waris keluarga pada 12-15 bulan.



**Mode penggunaan**: Versi yang berdiri sendiri dengan node Anda sendiri (gratis) atau layanan terkelola yang menambahkan pengingat dan pemberitahuan kepada ahli waris (0,05%/tahun).



https://planb.academy/tutorials/wallet/desktop/heritage-0549701f-2619-4037-ad05-44982be73ef4

## Proses pemulihan ahli waris



Memahami proses pemulihan akan membantu Anda menyiapkan rencana yang efektif. Berikut adalah langkah-langkah teknis yang perlu diikuti oleh ahli waris.



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




- Memeriksa keaslian perangkat lunak yang diunduh** (checksum, tanda tangan)
- Jangan pernah membagikan frasa pemulihan Anda** dengan siapa pun yang menawarkan bantuan
- Konsultasikan dengan setidaknya dua orang yang Anda percayai** sebelum melakukan pemulihan
- Mentransfer dana ke portofolio sederhana** yang ia kendalikan sepenuhnya setelah pemulihan



## Praktik terbaik



### Pemisahan informasi



Jangan pernah menyimpan semua informasi di satu tempat. Deskriptor harus dipisahkan dari frasa pemulihan, yang pada gilirannya dipisahkan dari kode PIN. Distribusi ini mempersulit akses bagi penyerang, namun tetap dapat diperoleh kembali oleh ahli waris Anda yang sah.



### Tes pemulihan



Sebelum menyetorkan dana yang signifikan, uji seluruh proses pemulihan dengan jumlah yang kecil. Pastikan Anda dapat memulihkan portofolio dari deskriptor dan frasa pemulihan pada perangkat kosong. Dokumentasikan langkah-langkah tersebut untuk ahli waris Anda.



### Pemeliharaan kunci waktu



Rencanakan untuk menyegarkan timelock Anda sebelum masa berlakunya habis. Untuk timelock 12 bulan, lakukan transaksi setiap 9-10 bulan. Perangkat lunak biasanya menawarkan pengingat atau fungsi penyegaran otomatis.



### Pembaruan rencana



Konfigurasi Bitcoin Anda berkembang. Setiap perubahan signifikan (portofolio baru, modifikasi tenggat waktu, penambahan pewaris) harus tercermin dalam dokumentasi Anda. Tetapkan rutinitas tinjauan tahunan.



## Memilih pendekatan Anda



Pilihan di antara berbagai solusi yang berbeda tergantung pada profil teknis dan kebutuhan spesifik Anda.



**Liana** cocok untuk pengguna desktop yang lebih memilih perangkat lunak open source dengan kontrol penuh melalui node mereka sendiri. Konfigurasi tetap dapat diakses berkat antarmuka yang dipandu. Penguncian waktu relatif (CSV) menyederhanakan pemeliharaan, karena aktivitas normal Anda secara otomatis memundurkan tenggat waktu. Batasan: penundaan maksimum sekitar 15 bulan (65535 blok).



**Bitcoin Keeper** menargetkan pengguna seluler yang mencari antarmuka yang intuitif dengan dokumen penyerta yang terintegrasi. Aplikasi ini menawarkan dua jenis kunci khusus: Kunci Warisan (yang menambah kuorum) dan Kunci Darurat (yang melewatinya sepenuhnya). Penguncian waktu absolut (CLTV) memungkinkan waktu tunggu lebih dari 15 bulan, dengan fungsi penyegaran ulang yang menyederhanakan penyegaran. Paket Diamond Hands membuka fitur-fitur lama yang canggih.



**Warisan** ditujukan untuk pengguna teknis yang menghargai kerahasiaan Taproot dan pewarisan hirarkis dengan penundaan progresif. Struktur pohon Taproot menyembunyikan kondisi pewarisan selama transaksi normal, hanya mengungkapkan kondisi yang digunakan selama pemulihan.



Ketiga solusi tersebut memiliki satu kesamaan: mereka memerlukan penyegaran secara berkala untuk mencegah aktivasi jalur pemulihan yang terlalu dini. Kendala ini adalah harga dan jaminan dari warisan on-chain yang tidak terpercaya. Jadwalkan pengingat rutin dan jadikan pemeliharaan ini sebagai bagian dari rutinitas manajemen Bitcoin Anda.



## Kesimpulan



Paket warisan Bitcoin teknis menggabungkan mekanisme kriptografi (kunci waktu, Miniscript, Taproot) dengan dokumentasi yang ketat. Dompet tingkat lanjut memungkinkan Anda untuk mengirimkan bitcoin Anda secara otomatis setelah periode tidak aktif, tanpa campur tangan pihak ketiga.



Elemen-elemen penting yang harus diwariskan kepada ahli waris Anda adalah: deskriptor atau file konfigurasi, frasa pemulihannya, instruksi pemulihan yang mendetail, dan rincian kontak orang yang kompeten yang dapat membantu mereka.



Mulailah dengan memilih solusi teknis yang sesuai dengan profil Anda, mengujinya dengan jumlah yang kecil, kemudian mendokumentasikan keseluruhannya dalam rencana yang terstruktur. Kompleksitas awal menjamin bahwa aset Bitcoin Anda akan diteruskan dengan penuh keyakinan.



## Sumber daya



### Templat rencana warisan





- [Template Rencana Warisan Bitcoin (PDF)](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/resources/bet/seed-management-tools/assets/Bitcoin-Inheritance-Plan-Template.pdf) - Template Dokumentasi Plan ₿ Network



### Referensi teknis





- [BIP-65 : OP_CHECKLOCKTIMEVERIFY] (https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki) - Spesifikasi kunci waktu absolut (CLTV)
- [BIP-112: OP_CHECKSEQUENCEVERIFY] (https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki) - Spesifikasi kunci waktu relatif (CSV)
- [Referensi Naskah Mini](https://bitcoin.sipa.be/miniscript/) - Dokumentasi Naskah Mini Resmi oleh Pieter Wuille



### Situs web solusi resmi





- [Liana Wallet](https://wizardsardine.com/liana/) - Wizardsardine
- [Bitcoin Keeper] (https://bitcoinkeeper.app/) - Bithyve
- [Heritage Wallet] (https://btc-heritage.com/) - Crypto7