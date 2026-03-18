---
name: ArkadeOS
description: Panduan lengkap untuk portofolio Arkade dan Protokol Ark
---

![cover](assets/cover.webp)



Jaringan Bitcoin menghadapi tantangan besar: skalabilitas. Meskipun lapisan utama (lapisan 1) menawarkan keamanan dan desentralisasi yang tak tertandingi, lapisan ini hanya dapat menangani sejumlah transaksi per detik. Lightning Network telah muncul sebagai solusi lapisan kedua (lapisan 2) yang menjanjikan, memungkinkan pembayaran yang cepat dan murah. Akan tetapi, Lightning memiliki kendala tersendiri: manajemen saluran, kebutuhan likuiditas yang masuk, dan kerumitan teknis yang dapat menunda pengguna baru.



Ini adalah latar belakang **Ark**, protokol layer 2 baru yang dirancang untuk menawarkan pengalaman pengguna yang disederhanakan tanpa mengorbankan kedaulatan. **ArkadeOS** (atau Arkade) adalah implementasi besar pertama dari protokol ini, yang menawarkan portofolio Bitcoin generasi berikutnya.



Tutorial ini akan memandu Anda memasuki dunia Arkade. Kita akan menjelajahi cara kerja protokol Ark, cara menginstal dan mengonfigurasi Arkade wallet, dan cara menggunakannya untuk mengirim dan menerima bitcoin secara instan, secara rahasia, dan tanpa gesekan Lightning Network yang biasa terjadi.



## Memahami protokol Ark



Sebelum mendalami penggunaan Arkade, penting untuk memahami konsep utama protokol Ark yang menggerakkannya. Ark bukanlah sebuah blockchain yang terpisah, tetapi sebuah mekanisme koordinasi yang cerdas di atas Bitcoin.



### Konsep VTXO


Inti dari Ark adalah **VTXO** (Virtual UTXO). VTXO adalah UTXO yang belum dipublikasikan pada blockchain Bitcoin: ia berada di luar rantai utama (off-chain) tetapi didukung oleh transaksi yang telah ditandatangani sebelumnya pada blockchain.



Tidak seperti saldo di bursa terpusat, VTXO benar-benar milik Anda. Anda memiliki bukti kriptografi yang memungkinkan Anda, kapan saja, untuk mengklaim bitcoin asli yang sesuai di blockchain, bahkan jika server Ark menghilang. VTXO memungkinkan Anda untuk mentransfer nilai secara instan antar pengguna tanpa menunggu konfirmasi blok.



### Peran ASP (Penyedia Layanan Bahtera)


Protokol Ark beroperasi pada model klien-server. Server disebut **ASP** (Penyedia Layanan Ark). ASP berperan sebagai konduktor:




- Ini menyediakan likuiditas yang diperlukan untuk jaringan.
- Ini mengoordinasikan transaksi antar pengguna.
- Ini mengatur "putaran" penyelesaian pada blockchain.



Sangat penting untuk dicatat bahwa ASP adalah **non-kustodian**. ASP tidak pernah menyimpan kunci pribadi Anda, dan juga tidak dapat mencuri dana Anda. Perannya murni bersifat teknis dan logistik. Jika ASP menyensor transaksi Anda atau mengalami kegagalan, Anda selalu dapat memulihkan dana Anda melalui prosedur keluar sepihak.



### Putaran dan privasi


Transaksi di Ark diselesaikan dalam batch yang disebut **Rounds**. Secara berkala (misalnya setiap beberapa detik), ASP mengumpulkan semua transaksi yang tertunda dan menambatkannya di blockchain Bitcoin dalam satu transaksi yang dioptimalkan.


Mekanisme ini menawarkan dua keuntungan utama:




- Skalabilitas**: Satu transaksi on-chain dapat memvalidasi ribuan pembayaran off-chain, sehingga secara drastis mengurangi biaya bagi pengguna.
- Kerahasiaan**: Setiap putaran bertindak sebagai **CoinJoin**. Dana dari semua peserta dicampur ke dalam kumpulan umum sebelum didistribusikan kembali dalam bentuk VTXO baru. Hal ini memutus hubungan antara pengirim dan penerima, sehingga sangat sulit, bahkan mustahil, bagi pengamat luar untuk melacak pembayaran.



## Presentasi ArkadeOS



ArkadeOS adalah aplikasi konkret yang membuat protokol Ark tersedia untuk masyarakat umum. Dikembangkan oleh Ark Labs, ini adalah ekosistem lengkap yang terdiri dari portofolio (Wallet), server (Operator), dan alat pengembang.



Untuk pengguna akhir, Arkade mengambil bentuk web yang elegan dan intuitif wallet (PWA - Progressive Web App). Ini menyembunyikan kompleksitas kriptografi VTXO dan putaran di balik antarmuka yang sudah dikenal. Dengan Arkade, Anda memiliki alamat untuk menerima, tombol untuk mengirim, dan riwayat transaksi, seperti halnya wallet klasik, tetapi dengan kekuatan kesegeraan dan kerahasiaan Ark.



## Instalasi dan konfigurasi



Karena Arkade adalah Aplikasi Web Progresif, aplikasi ini sangat mudah dipasang, dan tidak harus melibatkan toko aplikasi tradisional.



### Akses dan pemasangan


Anda dapat mengakses Arkade secara langsung dari peramban web modern apa pun (Chrome, Safari, Brave) di komputer atau ponsel.





- Kunjungi situs web resmi aplikasi ini: **[arkade.money](https://arkade.money)**.



![arkade homepage](assets/fr/01.webp)



Anda akan disambut oleh serangkaian layar pengantar yang memperkenalkan Anda pada konsep-konsep utama Arkade: ekosistem baru untuk Bitcoin, pentingnya penyimpanan sendiri, dan manfaat transaksi batch.



![arkade onboarding](assets/fr/02.webp)





- Di Android (Chrome/Brave)** : Tekan menu browser (tiga titik) dan pilih "Instal aplikasi" atau "Tambahkan ke layar beranda".
- Pada iOS (Safari)**: Tekan tombol berbagi (kotak dengan panah ke atas) dan pilih "Di layar beranda".



Setelah terinstal, Arkade diluncurkan seperti aplikasi asli, layar penuh dan tanpa bilah alamat.



### Pembuatan portofolio


Saat pertama kali diluncurkan, Anda akan diminta untuk mengonfigurasi portofolio Anda.





- Klik **"Buat Wallet Baru "**.



![create wallet](assets/fr/03.webp)





- wallet dibuat secara instan. Tidak seperti dompet Bitcoin tradisional, **Arkade tidak menggunakan frasa pemulihan 12 atau 24 kata**. Sebagai gantinya, Arkade secara otomatis membuat **kunci pribadi** dalam format Nostr (nsec), yang akan digunakan untuk mencadangkan dan memulihkan wallet Anda. Ingatlah untuk segera menyimpan kunci ini (lihat bagian selanjutnya).





- Anda akan melihat layar "Your new wallet is live!", yang mengonfirmasi bahwa wallet Anda telah siap digunakan. Klik **"GO TO WALLET "** untuk mengakses antarmuka utama.



Begitu masuk ke wallet, Anda akan dibawa ke antarmuka utama Arkade. Di sini Anda akan menemukan saldo Anda, tombol untuk mengirim dan menerima dana, dan tab "Aplikasi" yang memberikan akses ke aplikasi terintegrasi seperti Boltz (bursa Lightning), LendaSat dan LendaSwap (layanan pinjaman), dan Fuji Money (aset sintetis).



![wallet interface](assets/fr/04.webp)



### Koneksi ke ASP


Secara default, portofolio secara otomatis dikonfigurasikan untuk terhubung ke ASP resmi Arkade Labs. Anda dapat memeriksa server mana yang terhubung dengan membuka **Pengaturan** > **Tentang** di mana Anda akan melihat alamat server (saat ini `https://arkade.computer`).



Pada versi Arkade saat ini (Beta), tidak memungkinkan untuk memodifikasi server ASP secara manual. Aplikasi ini secara otomatis terhubung ke ASP resmi Arkade Labs. Di masa depan, pengguna mungkin dapat memilih di antara ASP yang berbeda sesuai dengan preferensi mereka, tetapi fitur ini belum tersedia.



### Mencadangkan kunci pribadi Anda


**Arkade menggunakan kunci pribadi dalam format Nostr (nsec) sebagai metode pencadangan dan pemulihan. Untuk mencadangkan kunci pribadi Anda:





- Buka **Pengaturan** dari layar utama.
- Pilih **"Pencadangan dan privasi "**.
- Anda akan melihat **kunci pribadi** Anda ditampilkan dalam format `nsec...`. Rangkaian karakter yang panjang ini adalah satu-satunya cara untuk memulihkan wallet anda.
- Tekan **"COPY NSEC TO CLIPBOARD "** untuk menyalin kunci pribadi Anda.
- Simpan kunci ini di tempat yang aman**: tulis di kertas, simpan di pengelola kata sandi yang aman, atau gunakan metode pencadangan lain yang sesuai untuk Anda.
- Arkade juga menawarkan opsi **"Aktifkan cadangan Nostr "**. Fitur ini menggunakan protokol Nostr (jaringan terdesentralisasi) untuk secara otomatis mencadangkan data tertentu dari wallet Anda dalam bentuk terenkripsi ke relay Nostr. Hal ini memfasilitasi sinkronisasi antara beberapa perangkat dan menawarkan pemulihan status wallet Anda yang lebih sederhana.



**Penting**: Cadangan nostr adalah fitur **kenyamanan** saja. Mereka tidak menggantikan cadangan kunci nsec Anda. Relai nostr tidak menjamin penyimpanan data secara permanen. Kunci pribadi nsec anda tetap menjadi satu-satunya cara yang dijamin untuk memulihkan dana anda.



![backup private key](assets/fr/05.webp)




## Menggunakan Arkade



Setelah Anda menyiapkan wallet Anda, Anda siap untuk menjelajahi kemampuan Arkade. Antarmuka dirancang untuk menyatukan berbagai jenis pembayaran Bitcoin (On-chain, Lightning, Ark) dengan mulus.



### Menerima dana



Untuk mendanai portofolio Anda, tekan **"Terima "**. Arkade menawarkan tiga metode penerimaan:





- Pembayaran Ark**: Jika pengirim juga menggunakan Arkade, bagikan alamat Ark Anda untuk transfer instan, rahasia, dan hampir gratis.
- Setoran on-chain (Boarding)**: Gunakan alamat Bitcoin (`bc1p...`) untuk menerima dari wallet klasik atau bursa. Tunggu konfirmasi (~10 menit) sebelum dana dikonversi menjadi VTXO.
- Pertukaran petir**: Buat faktur Lightning dan bayar dari wallet Lightning eksternal. Dana tiba seketika melalui swap otomatis.



![receive amount](assets/fr/06.webp)



Layar tanda terima menampilkan semua opsi yang tersedia: Kode QR, alamat Ark, alamat Bitcoin (BIP21), dan faktur Lightning. Untuk pembayaran Lightning, biarkan aplikasi tetap terbuka selama transaksi berlangsung.



![receive confirmation](assets/fr/07.webp)



### Mengirim dana



Untuk mengirim dana, tekan **"Kirim "** dan tempelkan alamat penerima atau pindai kode QR. Arkade secara otomatis mendeteksi jenis pembayaran yang diperlukan:





- Pembayaran Ark**: Ke alamat Ark, transfer bersifat instan, pribadi, dan hampir gratis (0 biaya SATS). Penerima tidak perlu online.
- Pembayaran Lightning**: Pindai faktur Lightning (`lnbc...`) dan Arkade akan secara otomatis melakukan penukaran. ASP membayar faktur untuk Anda dan mendebit saldo Arkade Anda.
- Pembayaran on-chain**: Menuju alamat klasik Bitcoin (`bc1q... ` atau `bc1p... `), Arkade memulai "Output Kolaboratif" yang akan disertakan dalam putaran on-chain berikutnya.



Periksa detail pada layar "Tanda tangani transaksi", lalu konfirmasikan dengan **"TAP TO SIGN "**.



![send payment](assets/fr/08.webp)



**Batasan saat ini (Beta) **: VTXO yang dibuat kurang dari 24 jam yang lalu tidak dapat digunakan untuk output on-chain. Jika Anda mengalami kesalahan, harap tunggu sampai VTXO Anda "matang".



*kerahasiaan keluaran *on-chain**: Contoh di bawah ini menunjukkan sebuah [transaksi keluaran Ark di mempool.space](https://mempool.space/fr/tx/153a70384d1c8a183c0e408e29b0a11820fd71a8bd5b4b00b12bc9b7f9decacb). Kami mengamati sebuah input terdistribusi ke 4 output yang berbeda, seperti CoinJoin. Untuk pengamat eksternal, tidak mungkin untuk menentukan jumlah yang mana milik pengguna yang mana.



![transaction ark mempool](assets/fr/11.webp)



## Fitur lanjutan



### Manajemen kedaluwarsa VTXO


Fitur teknis dari protokol Ark adalah bahwa VTXO memiliki masa pakai yang terbatas. Batasan waktu ini melekat pada desain protokol. Waktu kedaluwarsa dapat dikonfigurasi oleh setiap server ASP; pada ASP resmi Arkade Labs, periode ini sekitar **4 minggu (≈30 hari)**.



**Batasan ini memungkinkan server Ark untuk mengelola likuiditas secara efisien dan membersihkan VTXO dari pengguna yang tidak aktif. Setelah kedaluwarsa, server Ark secara teknis dapat mengklaim dana yang tersisa di pohon VTXO.



**Agar VTXO Anda tetap aktif, VTXO harus "disegarkan" sebelum masa berlakunya habis. Penyegaran terdiri dari berpartisipasi dalam "putaran" baru di mana VTXO Anda yang hampir kedaluwarsa ditukar dengan VTXO baru dengan masa berlaku penuh (≈30 hari di Arkade Labs ASP).



Portofolio Arkade mengelola proses ini secara otomatis: aplikasi secara konstan memantau status VTXO Anda dan secara otomatis menyegarkannya beberapa hari sebelum masa berlakunya habis. Selama Anda membuka aplikasi Anda secara teratur (setidaknya seminggu sekali), VTXO Anda akan secara otomatis tetap aktif.



**Jika Anda tidak membuka portofolio Anda selama lebih dari 4 minggu, VTXO Anda akan kedaluwarsa. Namun, Anda tidak kehilangan dana Anda: Anda tetap memiliki opsi untuk memulihkannya melalui **keluar sepihak** (lihat bagian selanjutnya). Prosedur ini lebih mahal dan lebih lambat, tetapi memastikan bahwa dana Anda tetap dapat dipulihkan.



Kebutuhan untuk membuka aplikasi secara teratur membuat Arkade menjadi **"Hot Wallet"** yang dirancang untuk penggunaan sehari-hari, bukan brankas untuk penyimpanan jangka panjang. Untuk menyimpan bitcoin tanpa menggunakannya dalam jangka waktu yang lama, pilihlah perangkat keras wallet yang dingin.



**Memeriksa status VTXO Anda**: Anda dapat memantau status VTXO Anda di **Pengaturan** > **Tingkat Lanjut**. Lihat "Perpanjangan Berikutnya" untuk melihat kapan perpanjangan otomatis berikutnya akan dilakukan, dan "Koin Virtual" untuk melihat daftar terperinci semua VTXO Anda dengan tanggal kedaluwarsanya.



![vtxo management](assets/fr/09.webp)



### Sortie Unilatérale (Keluar Sepihak)



Keluar secara sepihak adalah **jaminan kriptografi fundamental** protokol Ark yang memastikan Anda mendapatkan dana Anda kembali, bahkan jika ASP menghilang, menyensor transaksi Anda, atau menolak untuk bekerja sama. Secara teknis, VTXO Anda adalah **transaksi Bitcoin yang telah ditandatangani sebelumnya** yang Anda miliki. Dalam keadaan darurat, Anda dapat menyiarkan transaksi ini di blockchain Bitcoin untuk memulihkan dana Anda tanpa izin siapa pun.



**Bagaimana cara kerjanya? Prosesnya berlangsung dalam dua tahap. Pertama, **Pembukaan**: Anda secara berurutan menyiarkan transaksi yang sudah ditandatangani sebelumnya yang membentuk VTXO Anda di pohon transaksi. Kemudian **Finalisasi**: setelah penguncian waktu berakhir (biasanya 24 jam), Anda mengumpulkan bitcoin Anda dari alamat standar.



**Status saat ini di Arkade**: Pada versi Beta, belum ada tombol atau antarmuka pengguna yang sederhana untuk output satu sisi. Fungsionalitas ini saat ini membutuhkan penggunaan Arkade SDK dan pengetahuan teknis pemrograman TypeScript.



**Meskipun prosedur tidak dapat diakses dengan satu sentuhan tombol, jaminan kriptografi tetap ada. VTXO Anda berisi transaksi yang telah ditandatangani sebelumnya yang secara sah menjadi milik Anda. Jaminan teknis inilah yang membuat Ark menjadi protokol **non-kustodian**: bahkan dalam skenario terburuk sekalipun, dana Anda tetap dapat dipulihkan secara teknis. Antarmuka yang disederhanakan mungkin akan ditambahkan dalam versi Arkade yang akan datang.



## Keuntungan dan keterbatasan



Untuk menempatkan Arkade dalam konteks yang tepat, mari kita rangkum kekuatan dan kelemahannya saat ini.



### Sorotan




- Pengalaman Pengguna (UX)**: Tidak ada manajemen saluran, kapasitas yang masuk atau cadangan saluran yang rumit seperti pada Lightning. Cukup instal dan gunakan.
- Privasi**: Arsitektur CoinJoin standar menawarkan tingkat anonimitas yang jauh lebih tinggi daripada transaksi on-chain atau Lightning standar.
- Interoperabilitas**: Bayar kode QR Bitcoin apa pun (On-chain atau Lightning) dari satu antarmuka.



### Kendala




- Protokol muda**: Ark adalah teknologi yang sangat baru. Bug mungkin saja ada. Disarankan untuk tidak menggunakan Ark untuk menyimpan sejumlah uang yang kehilangannya akan sangat penting.
- Ketergantungan ASP**: Meskipun non-kustodian, sistem ini bergantung pada ketersediaan ASP untuk kelancarannya. Jika ASP offline, Anda tidak dapat lagi bertransaksi secara instan (hanya mengeluarkan dana on-chain Anda).
- Hanya Hot Wallet saja**: Kebutuhan untuk membuka aplikasi secara teratur untuk menyegarkan VTXO tidak cocok untuk penyimpanan dingin (Cold Storage).



## Perbandingan: Arkade vs Lightning vs Cashu



Untuk lebih memahami posisi Arkade, mari kita bandingkan dengan dua solusi skalabilitas utama lainnya.




| Kriteria | Arkade (Ark) | Lightning Network | Cashu (E-cash) |
| :--- | :--- | :--- | :--- |
| **Model** | UTXO bersama dikoordinasikan oleh server (ASP) | Jaringan P2P saluran pembayaran | Token buta yang diterbitkan oleh bank (Mint) |
| **Kustodi** | **Non-custodial** (Anda memegang kunci) | **Non-custodial** (Anda memegang kunci) | **Custodial** (Mint memegang dana) |
| **Privasi** | **Tinggi** (CoinJoin asli, buta bagi publik) | **Sedang** (Onion routing, tapi saluran terlihat) | **Sangat Tinggi** (Buta bahkan bagi Mint) |
| **Skalabilitas** | Luar Biasa (Batching masif on-chain) | Luar Biasa (Transaksi tanpa batas off-chain) | Luar Biasa (Tanda tangan server sederhana) |
| **Pengalaman** | Sederhana (mirip wallet on-chain) | Kompleks (manajemen saluran, likuiditas) | Sangat sederhana (seperti uang tunai digital) |
| **Risiko utama** | Ketersediaan ASP & Kedaluwarsa | Manajemen saluran & Backup | Kepercayaan pada Mint (risiko pencurian) |

**Arkade** adalah kompromi yang ideal: kesederhanaan dan kerahasiaan Cashu, tetapi dengan kedaulatan (non-kustodian) Lightning.



## Dukungan & Bantuan



Jika Anda mengalami masalah atau memiliki pertanyaan saat menggunakan Arkade, aplikasi ini menawarkan beberapa opsi dukungan:





- Buka **Pengaturan** > **Dukungan**.
- Anda akan menemukan beberapa opsi:
  - Dukungan pelanggan**: Dapatkan bantuan untuk portofolio Anda, laporkan bug, atau ajukan pertanyaan.
  - Obrolan Aman**: Percakapan Anda aman dan pribadi, dengan riwayat yang disimpan di antara sesi.
  - Laporan Bug**: Laporkan masalah yang Anda temui, termasuk langkah-langkah untuk mengatasinya.
  - Lacak Kemajuan**: Lacak tiket dan percakapan dukungan Anda setiap saat.



![support](assets/fr/10.webp)



Tim Arkade juga aktif di Telegram melalui saluran @arkade_os untuk mendapatkan dukungan dan peluang integrasi.



## Catatan penting: Aplikasi dalam versi Beta



**⚠️ Arkade saat ini dalam versi Beta Publik pada mainnet Bitcoin**. Meskipun aplikasi ini berfungsi dengan bitcoin asli, penting untuk mengambil tindakan pencegahan tertentu.



### Rekomendasi untuk digunakan




- Gunakan dalam jumlah kecil**: Hindari menyimpan uang dalam jumlah besar di Arkade. Gunakan wallet ini untuk pengeluaran sehari-hari Anda dan simpan tabungan Anda pada perangkat keras wallet yang dingin.
- Kemungkinan adanya bug dan keterbatasan**: Seperti halnya aplikasi lain yang sedang dalam pengembangan aktif, Arkade mungkin memiliki bug atau perilaku yang tidak diharapkan. Laporkan masalah apa pun melalui dukungan terintegrasi.
- Evolusi yang cepat**: Aplikasi dan protokol terus ditingkatkan. Beberapa fitur dapat berubah atau ditambahkan dalam versi mendatang.



### Keterbatasan yang diketahui saat ini




- penundaan 24 jam pada VTXO**: VTXO yang baru dibuat tidak dapat langsung digunakan untuk output on-chain.
- ASP yang unik**: Belum memungkinkan untuk mengubah server ASP dalam aplikasi.
- Keluaran teknis sepihak**: Belum ada antarmuka yang disederhanakan untuk output unilateral (memerlukan SDK).



Tim Arkade Labs secara aktif bekerja untuk melonggarkan batasan ini di versi mendatang.



## Kesimpulan



ArkadeOS merupakan terobosan besar dalam ekosistem Bitcoin. Dengan mengimplementasikan protokol Ark, ini membuktikan bahwa kesederhanaan penggunaan dapat direkonsiliasi dengan prinsip-prinsip dasar Bitcoin: jangan percaya, verifikasi.



Meskipun masih dalam tahap awal, Arkade menawarkan sekilas gambaran menarik tentang bagaimana masa depan pembayaran Bitcoin: instan, privat, dan dapat diakses oleh semua orang tanpa prasyarat teknis. Ini adalah alat yang sempurna untuk pengeluaran harian Anda, melengkapi solusi tabungan Anda yang aman (Cold Wallet).



Kami mendorong Anda untuk menguji Arkade dengan jumlah kecil untuk menemukan protokol baru ini untuk diri Anda sendiri. Ekosistem ini berkembang dengan cepat, dan Arkade berada di garis depan dalam inovasi ini.



## Sumber daya



Untuk mengetahui lebih lanjut, bacalah sumber daya resmi:





- Situs web Arkade**: [arkadeos.com](https://arkadeos.com)
- Dokumentasi**: [docs.arkadeos.com](https://docs.arkadeos.com)
- Protokol Ark**: [ark-protocol.org](https://ark-protocol.org)
- Kode Sumber** : [GitHub Arkade](https://github.com/arkade-os)