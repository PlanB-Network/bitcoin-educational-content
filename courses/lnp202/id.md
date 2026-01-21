---
name: Menyiapkan simpul Lightning pertama Anda
goal: Memahami, memasang, mengonfigurasi, dan menggunakan simpul Lightning
objectives: 


  - Memahami peran dan tujuan dari simpul Lightning.
  - Identifikasi berbagai solusi perangkat lunak yang tersedia.
  - Memasang dan mengkonfigurasi simpul Lightning (LND).
  - Menghubungkan akun pengeluaran.
  - Ketahui risiko penggunaan simpul Lightning.


---

# Langkah pertama Anda menuju otonomi di Lightning



Anda sudah mendapatkan sats pertama Anda, mengamankan dana penyimpanan mandiri Anda, dan menggunakan node Bitcoin untuk berdaulat dalam penggunaan on-chain Anda. Langkah selanjutnya adalah mendapatkan otonomi yang sama di Lightning: itulah tujuan kursus ini.



LNP202 ditujukan untuk pengguna tingkat menengah, dan memandu Anda langkah demi langkah melalui penerapan node Lightning pertama Anda, tanpa keahlian teknis tingkat lanjut.



Anda akan mempelajari cara memasang LND pada Umbrel, membuka dan mengelola saluran Anda, mengawasi node Anda, dan menghubungkan wallet seluler, sehingga Anda dapat menikmati pengalaman yang sebanding dengan wallet kustodian, sambil mempertahankan kendali penuh atas dana Anda.



+++


# Pendahuluan


<partId>5e77c17a-0853-4f36-a988-1b4a956f49e4</partId>



## Gambaran umum kursus


<chapterId>e0871abf-af6d-4221-9389-1a996aea9b79</chapterId>



LNP202 adalah kursus praktis yang dirancang untuk membuat Anda mandiri di Lightning dengan mengoperasikan node Anda sendiri. Tujuannya sederhana: mulai dengan node Bitcoin yang sudah ada, terapkan LND pada Umbrel, amankan dengan benar, buka dan kelola saluran pertama Anda, lalu gunakan node Anda setiap hari dari wallet seluler. Kursus ini mengasumsikan bahwa Anda telah mengambil BTC 202, karena saya mengasumsikan bahwa node Bitcoin Anda di Umbrel sudah siap dan tersinkronisasi. Kita tidak akan membahas kembali cara menyiapkan node Bitcoin di sini.



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

Untuk pemahaman yang lebih baik mengenai mekanika internal Lightning, kursus LNP 201 juga sangat direkomendasikan, meskipun bukan merupakan prasyarat untuk kursus ini:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Di bagian pertama kursus LNP202 ini, kita akan melihat apa sebenarnya Lightning node itu, apa bedanya dengan wallet yang sederhana, dan mengapa mengoperasikan node pribadi adalah satu-satunya cara untuk menggunakan Lightning tanpa mendelegasikan sats Anda ke pihak ketiga yang tepercaya. Bagian ini diakhiri dengan pilihan strategis: solusi mana yang tepat untuk Anda, mulai dari pendekatan yang paling sederhana hingga node Lightning klasik, yang akan kita terapkan dalam kursus ini.



Di Bagian 2 kursus ini, Anda akan menginstal LND di Umbrel, kemudian menerapkan elemen-elemen yang mencegah kesalahan yang paling merugikan: strategi pencadangan yang realistis dan perlindungan terhadap kecurangan melalui menara pengawas. Setelah dasar-dasar ini siap, Anda akan membuka saluran pertama Anda, sehingga Anda bisa mulai membayar di Lightning dengan infrastruktur Anda sendiri.



Jadi, Anda tahu: dalam kursus LNP202 ini, kita akan menyiapkan node Lightning dalam mode plug-and-play melalui Umbrel, daripada pendekatan baris perintah klasik, agar cocok untuk pengguna tingkat menengah. Jika Anda lebih suka instalasi baris perintah, saya sarankan Anda mengikuti tutorial di bawah ini. Kursus Lightning lain yang lebih canggih dan berorientasi pada baris perintah juga sedang dipersiapkan.



https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Bagian 3 kemudian akan membawa Anda dari node yang berfungsi ke node yang Anda tahu cara mengendalikannya. Anda akan mulai dengan menentukan profil operator node Lightning Anda (konsumen, pedagang, atau router), kemudian memahami paket perangkat lunak manajemen yang lengkap, untuk melacak saluran Anda dan bertindak dengan bersih pada topologi Anda. Terakhir, Anda akan membahas poin Lightning yang sangat penting: cara mendapatkan likuiditas masuk, baik melalui solusi berbayar atau kooperatif.



Bagian 4 akan berfokus pada penggunaan sehari-hari. Anda akan menyiapkan koneksi antara node Anda dan pelanggan seluler, sehingga Anda dapat membayar dan menagih hanya dari ponsel cerdas Anda, tanpa melepaskan hak asuh. Kita akan melihat pendekatan jaringan melalui *Tailscale*, kemudian pendekatan protokol melalui *Nostr Wallet Connect*, dengan kelebihan dan kekurangannya masing-masing. Kursus ini akan diakhiri dengan bab terakhir yang akan memberi Anda kebiasaan yang tepat untuk mempertahankan self-custody Anda, baik secara operasional maupun pedagogis.



Jika Anda mengikuti kursus LNP202 ini dengan urutan yang benar, pada akhirnya Anda akan memiliki konfigurasi yang lengkap untuk node Lightning Anda, fungsional untuk penggunaan sehari-hari dan, yang terpenting, terkendali.




## Memahami simpul petir


<chapterId>8275dfd8-7a72-48cc-bf7f-bc2a46063003</chapterId>



Sebelum meluncurkan node Anda sendiri, bab ini mengulas secara singkat teori dasar di balik Lightning Network. Memang penting untuk memahami mekanisme yang terlibat, karena ini akan memungkinkan Anda untuk mengidentifikasi risiko dan mengadopsi praktik-praktik yang baik untuk membatasinya. Namun, saya tidak akan membahasnya secara rinci di sini, karena ini bukan tujuan utama dari kursus ini. Jika Anda ingin mempelajari subjek ini lebih dalam, saya sangat menyarankan Anda untuk membaca kursus LNP 201 dari Fanis Michalakis, yang merupakan referensi di bidang ini:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### Apakah yang dimaksud dengan simpul petir?



Mari kita kembali ke dasar: sebelum mendefinisikan apa itu node, kita perlu memahami apa itu Lightning Network. Ini adalah protokol lapisan atas, yang dibangun di atas Bitcoin, yang dirancang untuk memungkinkan transaksi offchain BTC yang cepat (dengan penyelesaian yang hampir instan) dan umumnya tidak mahal. "Offchain" berarti bahwa transaksi yang dilakukan di Lightning tidak dimaksudkan untuk muncul di blockchain Bitcoin utama. Lightning juga merupakan respons parsial terhadap peningkatan penggunaan Bitcoin dan kemacetan onchain, yang meningkatkan kekhawatiran tentang skalabilitas sistem.



Untuk beroperasi, Lightning bergantung pada pembukaan saluran pembayaran antara peserta, di mana transaksi dapat dilakukan hampir secara instan, seringkali dengan biaya minimal, tanpa perlu mendaftarkannya satu per satu di blockchain Bitcoin. Saluran ini dapat tetap terbuka untuk waktu yang sangat lama, membutuhkan transaksi onchain hanya ketika dibuka dan ditutup.



Sebuah node Lightning adalah peserta dalam jaringan Lightning, membuka saluran dan melakukan pembayaran dengan node lain. Secara konkret, Lightning node adalah sebuah perangkat lunak yang berjalan di komputer dan mengimplementasikan protokol Lightning Network. Contohnya termasuk LND, Core Lightning atau Eclair. Peran utama perangkat lunak ini adalah untuk:




- terhubung ke node Bitcoin untuk mendapatkan informasi dari blockchain utama;
- membuat dan mengelola saluran pembayaran dua arah dengan node lain;
- bertukar pesan dengan seluruh jaringan Lightning.



![Image](assets/fr/001.webp)



### Node vs. Lightning Wallet: perbedaan penting



Pada Bitcoin (onchain), "*wallet*" mengacu pada perangkat lunak yang mengelola kunci pribadi Anda, menghitung saldo Anda dari UTXO dan membangun transaksi Anda. wallet ini dapat didasarkan pada node Bitcoin Anda sendiri atau node orang lain, tetapi saat ini, peran node dan peran onchain wallet jelas berbeda.



Pada Lightning, lebih sulit untuk menggunakan kembali kosakata semacam ini tanpa menimbulkan kebingungan. Istilah "*Lightning wallet*" agak kabur, karena pada kenyataannya, tidak ada yang namanya Lightning wallet yang benar-benar mandiri, kecuali jika didasarkan pada suatu node. Oleh karena itu, hanya ada dua situasi yang memungkinkan:



- Untuk memiliki Lightning node yang sebenarnya (yaitu non-kustodian): perangkat lunak yang Anda gunakan (misalnya aplikasi seluler seperti Phoenix atau contoh LND di Umbrel) sebenarnya menjalankan sebuah node, dan Anda benar-benar memegang kunci untuk mengambil bitcoin Anda. Dalam kasus ini, "*Lightning wallet*" Anda sebenarnya hanyalah sebuah antarmuka pengguna di atas node Lightning, baik yang tertanam maupun yang jarak jauh.



- Untuk menggunakan layanan kustodian: Anda menggunakan aplikasi yang menunjukkan kepada Anda saldo di sats di Lightning, tetapi di latar belakang, dana berada di node penyedia (mis. Wallet of Satoshi). Anda tidak memiliki kunci atau kendali atas saluran tersebut. Saldo Anda hanyalah entri akuntansi dalam basis data perusahaan. Hal ini sebanding dengan meninggalkan bitcoin Anda di platform bursa, dengan semua risiko yang terkait. Dalam hal ini, "*Lightning wallet*" Anda hanyalah sebuah akses ke akun yang dikelola oleh operator yang, pada gilirannya, menjalankan simpul Lightning yang sebenarnya.



Jadi, tidak ada yang di antara keduanya pada Lightning: Anda memiliki node (bahkan yang tertanam) sehingga Anda berada dalam hak milik sendiri, atau tidak, sehingga perusahaan memiliki sats Anda. Tetapi seperti yang akan kita lihat di bab-bab berikutnya, kedua penggunaan ini terkadang sulit dibedakan. Sebagai contoh, Phoenix adalah aplikasi seluler yang menyematkan simpul Lightning yang sebenarnya, tetapi pengguna belum tentu menyadarinya, karena kerumitan penuh operasinya hampir seluruhnya tersembunyi.



### Pengingat tentang cara kerja Lightning Network



Pada bagian ini, saya akan memberi Anda pengingat singkat tentang cara kerja Lightning. Sekali lagi, jika Anda ingin mendapatkan presentasi yang lebih mendalam mengenai konsep teoretis, saya mengundang Anda untuk melihat kursus khusus LNP 201.



#### Saluran pembayaran: buka, perbarui, dan tutup



Inti dari jaringan Lightning didasarkan pada saluran pembayaran dua arah. Sebuah saluran dapat dibuka (yaitu dibuat), diperbarui saat transaksi Lightning terjadi, dan kemudian ditutup. Dari sudut pandang onchain, sebuah saluran tidak lebih dari sebuah output multisignature 2/2.



![Image](assets/fr/002.webp)



Dari sudut pandang Lightning, ini adalah saluran pembayaran dengan likuiditas yang dibagi antara dua peserta.



![Image](assets/fr/003.webp)





- Membuka saluran:**



Dua node memutuskan untuk membuka saluran. Salah satu dari mereka melakukan transaksi bitcoin dalam transaksi onchain yang disebut *transaksi pendanaan*. Transaksi ini menghasilkan output berdasarkan skrip multisignature 2-of-2, yang berarti bahwa pengeluaran dana ini pada Bitcoin membutuhkan tanda tangan dari kedua node di dalam channel. Sebelum mengeluarkan transaksi ini, pihak yang menyediakan dana meminta pihak lain untuk menandatangani *transaksi penarikan*, yang tidak dikeluarkan onchain, tetapi memungkinkannya untuk memulihkan dananya jika terjadi masalah.



![Image](assets/fr/004.webp)





- Transaksi Commitment:** Transaksi Commitment:**



Status saluran (yaitu distribusi sats antara A dan B) diwakili oleh *commitment transaction*, yang diketahui oleh kedua node tetapi tidak segera disiarkan di blockchain. Transaksi ini menjelaskan bagaimana mendistribusikan kembali dana saluran pada blockchain sesuai dengan pembayaran yang dilakukan pada Lightning.



Dengan setiap pembayaran Lightning, kedua node menandatangani state baru yang menggantikan state sebelumnya. Status lama dicabut berkat mekanisme kunci pencabutan: jika salah satu peserta mencoba menyiarkan status lama, peserta lainnya dapat memulihkan jumlah penuh dana sebagai penalti.



Ide yang penting di sini adalah selalu ada transaksi Bitcoin yang ditandatangani, tidak disiarkan pada rantai, yang disimpan oleh node, dan yang memungkinkan pendistribusian ulang sats satu sama lain sesuai dengan pembayaran yang dilakukan pada Lightning Network.



![Image](assets/fr/005.webp)





- Penutupan saluran:**



Sebuah channel dapat ditutup dengan bersih melalui penutupan kooperatif, ketika kedua belah pihak menyetujui kondisi akhir channel, atau secara sepihak (penutupan paksa) jika salah satu partisipan berhenti bekerja sama atau tidak dapat dihubungi. Dalam semua kasus, penutupan mengambil bentuk transaksi onchain yang menghabiskan output 2/2 dan mendistribusikan dana di antara para peserta sesuai dengan status terakhir yang valid dari saluran.



![Image](assets/fr/006.webp)



Dengan demikian, Lightning berfungsi sebagai lapisan sekunder yang berlabuh di Bitcoin: hanya peristiwa tertentu (pembukaan dan penutupan saluran) yang muncul di blockchain utama. Pembayaran perantara tetap berada di luar rantai.



Sebelum melangkah lebih jauh, berikut ini adalah dua konsep penting untuk memahami cara mengelola saluran Lightning:




- Liquidity*: jumlah sats yang tersedia pada satu sisi saluran;
- Kapasitas *kapasitas*: ini adalah jumlah total yang terkunci dalam output multisig 2/2, yaitu jumlah likuiditas di kedua sisi saluran.



#### Jaringan saluran dan likuiditas



Saluran tidak hanya untuk pembayaran antara dua node: saluran merupakan bagian dari jaringan global saluran yang saling terhubung. Node Anda dapat merutekan pembayaran untuk pengguna lain melalui salurannya sendiri, dan Anda dapat mengirim sats ke node Lightning yang tidak memiliki saluran langsung dengan Anda, selama jalur yang valid dapat ditemukan di antara dua node Anda.



Setiap node mengetahui, melalui protokol gosip, peta jaringan ini: saluran mana yang ada, node mana yang terhubung dengan saluran dua arah, dan kapasitas mana yang dipublikasikan. Untuk mengirim pembayaran ke penerima tanpa saluran langsung, node Anda menghitung rute yang terdiri dari beberapa lompatan: node Anda → node X → node Y → node penerima. Pada setiap lompatan, pembayaran melewati saluran yang harus memiliki likuiditas yang cukup ke arah pembayaran.



![Image](assets/fr/007.webp)



Oleh karena itu, likuiditas saluran tidak simetris: satu sisi mungkin terisi penuh, sementara sisi lainnya hampir kosong. Mengelola likuiditas ini, yaitu mengetahui di mana sats berada dan ke arah mana mereka dapat mengalir, adalah salah satu aspek terpenting dalam mengoperasikan simpul Lightning. Kita akan membahasnya secara lebih rinci dalam bab-bab praktis yang akan datang.



#### HTLC: mengangkut pembayaran tanpa dirampok



Untuk memungkinkan pembayaran melewati node perantara tanpa memerlukan kepercayaan, Lightning menggunakan kontrak pintar yang disebut *HTLC* (*Hashed Time-Locked Contracts*). Secara sederhana, HTLC membuat transfer dana bergantung pada pengungkapan rahasia, dan menggabungkan batasan waktu untuk melindungi pengirim jika terjadi kegagalan transaksi. Oleh karena itu, setiap pembayaran tunduk pada presentasi pra-gambar (rahasia yang hash-nya sesuai dengan nilai yang disepakati). Jika penerima akhir memberikan pra-citra ini, dia dapat mengklaim dana, yang pada gilirannya memungkinkan setiap simpul perantara untuk memulihkan dananya sendiri.



![Image](assets/fr/008.webp)



Saya tidak akan menjelaskan detail teknis tentang cara kerja HTLC, karena tidak penting untuk tujuan kursus ini. Anda akan menemukan penjelasan mendalam dalam kursus teori LNP 201. Ingatlah bahwa HTLC memungkinkan pertukaran atomik: transfer selesai dan tidak ada yang dirugikan dalam perutean, atau gagal dan setiap peserta mendapatkan kembali dana awalnya. Tidak ada jalan tengah.



### Implementasi simpul Lightning utama



Seperti halnya Bitcoin, ada beberapa implementasi protokol Lightning. Sejumlah tim independen sedang mengembangkan versi mereka sendiri, yang semuanya dapat dioperasikan karena mengikuti spesifikasi yang sama (BOLT). Berikut ini adalah implementasi utama yang digunakan saat ini.



#### LND (*Lightning Network Daemon*)



LND adalah implementasi lengkap protokol Lightning, yang ditulis dalam bahasa Go dan dikembangkan oleh Lightning Labs.



![Image](assets/fr/009.webp)



#### Petir Inti (*CLN*)



Core Lightning (sebelumnya *C-Lightning*) adalah implementasi yang dikembangkan oleh Blockstream. Ditulis dalam bahasa C, dengan beberapa komponen dalam Rust.



![Image](assets/fr/010.webp)



#### Eclair



Eclair adalah implementasi yang ditulis dalam Scala dan dikembangkan oleh perusahaan Prancis ACINQ. ACINQ mengoperasikan salah satu node perutean paling penting dalam jaringan Lightning dengan Eclair, dan menggunakan implementasi ini sebagai dasar perangkat lunak untuk produknya sendiri, seperti aplikasi Phoenix.



![Image](assets/fr/011.webp)



#### LDK (*Lightning Development Kit*)



LDK (*Lightning Development Kit*) adalah kit pengembangan Rust, yang dikelola oleh Spiral (Block, ex-Square). Ini bukan daemon yang siap pakai seperti LND atau CLN, tetapi sebuah perpustakaan untuk pengembang yang ingin mengintegrasikan Lightning secara langsung ke dalam aplikasi mereka.



![Image](assets/fr/012.webp)



Dalam kursus LNP202 ini, kami akan berkonsentrasi terutama pada LND: implementasi yang paling sering digunakan dalam solusi siap pakai untuk pelanggan swasta, seperti Umbrel.



Sekian pengingat singkat tentang cara kerja Lightning. Sekali lagi, jika ada konsep yang tidak Anda pahami, atau jika Anda ingin mempelajari lebih dalam sebelum mempraktikkannya, kursus Fanis Michalakis adalah referensi penting tentang subjek ini:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


## Mengapa menjalankan simpul Lightning Anda sendiri?


<chapterId>421db24e-511c-41ed-ad68-69b0662042ea</chapterId>



Menjawab pertanyaan ini cukup sederhana, karena pertanyaan ini bersifat retoris: tanpa simpul Anda sendiri, Anda tidak lagi benar-benar menggunakan Lightning, tetapi hanya ilusi Lightning di seluruh infrastruktur perusahaan.



Menggunakan kustodian Lightning wallet berarti bahwa bitcoin secara teknis adalah milik perusahaan yang mengoperasikan node tersebut. Anda tidak memegang kunci privat, dan Anda tidak mengontrol salurannya. Saldo wallet Anda hanyalah sebuah baris dalam basis data penyedia layanan. Situasi ini tentu saja sangat nyaman bagi pemula, dan pengalaman pengguna sering kali berubah-ubah, tetapi pertanyaan mendasarnya adalah: apa keuntungan menggunakan Bitcoin dan Lightning jika Anda akhirnya melepaskan aspek-aspek yang membedakannya dari mata uang tradisional dan bank?



Dua proposisi nilai utama Bitcoin adalah kedaulatan moneter (tidak lagi bergantung pada otoritas pusat untuk menerbitkan dan menyimpan) dan resistensi terhadap sensor (ketidakmungkinan bagi pihak ketiga untuk mencegah atau memfilter pembayaran). Sistem kustodian di Lightning bertentangan dengan kedua tujuan ini: Anda tidak dapat memeriksa pasokan uang internal platform, dan menurut definisi, operator yang memegang semua dana dan semua saluran dapat menyensor, menunda, memprioritaskan, atau memblokir pembayaran Anda. Dalam kondisi seperti ini, kita bisa bertanya pada diri sendiri, **apa gunanya menggunakan bitcoin melalui Lightning jika akan mereproduksi pola kepercayaan dan ketergantungan yang sama dengan sistem mata uang negara tradisional**.



> Yang dibutuhkan adalah sistem pembayaran elektronik berdasarkan bukti kriptografi dan bukannya kepercayaan, yang memungkinkan dua pihak yang bersedia untuk bertransaksi secara langsung satu sama lain tanpa memerlukan pihak ketiga yang terpercaya.
*Satoshi Nakamoto, Bitcoin Kertas Putih


Di samping filosofi, kerugian yang lebih konkret untuk Anda adalah sebagai berikut. Pertama, Anda tidak memiliki cara untuk memverifikasi bahwa perusahaan tersebut benar-benar memiliki bitcoin yang sesuai dengan saldo yang ditampilkan. Perusahaan tersebut mungkin beroperasi dengan cadangan pecahan, diretas, bangkrut, atau hilang begitu saja. Dalam kasus ini, Anda hanyalah kreditur biasa, tanpa jaminan nyata bahwa Anda akan mendapatkan uang Anda kembali.



Kedua, perusahaan tunduk pada risiko regulasi: perintah, pembekuan dana, permintaan untuk memblokir pengguna atau transaksi, pengawasan yang diperkuat, atau bahkan pelarangan aktivitas di yurisdiksi tertentu. Setiap kendala yang membebani penyedia layanan secara otomatis tercermin pada Anda.



Dalam hal kerahasiaan, situasinya tidak lebih baik. Operator kustodian melihat semua aliran Anda: jumlah, frekuensi, penerima, saldo, kebiasaan belanja. Dikombinasikan dengan informasi yang disediakan oleh aplikasi dan mungkin analisis rantai yang mendasari Bitcoin, informasi ini dapat memberikan profil yang sangat tepat dari aktivitas keuangan Anda. Sekali lagi, hal ini sangat jauh dari tujuan Bitcoin untuk mengurangi pemantauan keuangan.



Kabar baiknya adalah bahwa saat ini, mengoperasikan simpul Lightning Anda sendiri tidak lagi menjadi milik para ahli teknis, seperti yang terjadi pada akhir tahun 2010. Solusi yang relatif sederhana tersedia untuk pengguna rumahan, yang akan kami jelaskan secara rinci dalam bab berikutnya.




## Memilih solusi yang tepat untuk pekerjaan


<chapterId>615870e3-741d-4ec1-875d-a483e70f39d4</chapterId>



Saat ini, Anda dapat memiliki pengalaman pengguna yang sangat mirip dengan pengalaman kustodian Lightning wallet, namun tetap berada dalam kustodian mandiri. Tujuan dari bab ini adalah untuk membantu Anda memilih jalur yang paling sesuai dengan profil Anda.



### Opsi 1: Jangan gunakan Lightning secara langsung



Solusi pertama adalah dengan tidak menggunakan Lightning secara native, tetapi menggunakan Bitcoin atau Liquid wallet yang menyematkan pertukaran atom. Sebagai contoh, aplikasi Aqua atau Bull Bitcoin Wallet menggunakan metode ini, dengan memungkinkan Anda untuk membayar faktur Lightning tanpa mengoperasikan node Lightning sendiri, namun tetap berada di dalam tahanan sendiri.



Prinsipnya sangat mudah: dana Anda tetap berada di Bitcoin, baik on-chain atau di Liquid, dan Anda mengaksesnya melalui wallet di mana Anda memegang kuncinya dengan cara tradisional. Ketika Anda memindai faktur Lightning, wallet Anda akan memulai transaksi (on-chain atau Liquid) ke layanan pertukaran atom. Layanan ini kemudian mengelola pembayaran Lightning melalui simpulnya sendiri, menggunakan bitcoin yang Anda berikan kepada on-chain atau melalui Liquid. Hasilnya, Anda tidak perlu menangani saluran Lightning sendiri, namun Anda masih dapat menyelesaikan faktur Lightning dengan lancar.



![Image](assets/fr/013.webp)



Keuntungan utama dari pendekatan ini, dibandingkan dengan kustodian Lightning wallet konvensional, adalah Anda tetap memiliki 100% dana Anda setiap saat. Bitcoin berada di onchain atau Liquid wallet Anda, dengan frasa mnemonik Anda sendiri. Bahkan selama pertukaran, Anda tetap memiliki dana Anda, karena pertukarannya bersifat atomik. Sistem ini bergantung pada mekanisme kriptografi yang memastikan hanya ada dua kemungkinan hasil: swap berhasil sepenuhnya, atau gagal dan layanan tidak dapat mengambil dana Anda.



Sebagian besar portofolio yang menawarkan jenis fungsionalitas ini mengandalkan [Boltz] (https://boltz.exchange/) untuk bagian teknis swap.



Solusi ini juga menawarkan keuntungan yang menarik dalam hal kerahasiaan, terutama ketika digabungkan dengan Liquid. Untuk pemula, solusi ini juga sangat mudah diatur dan disimpan: frasa mnemonik klasik, tidak ada saluran, tidak ada likuiditas untuk menyeimbangkan...



Di sisi lain, pendekatan ini memiliki keterbatasan. Pertama, pendekatan ini tidak dapat diandalkan: Anda bergantung pada ketersediaan dan niat baik layanan swap. Jika layanan ini tidak lagi ingin memproses akun Anda, atau berhenti beroperasi, Anda tidak bisa lagi membayar faktur Lightning melalui layanan ini. Kemudian ada biaya yang tidak sedikit: Anda membayar biaya transaksi onchain atau Liquid, dan komisi layanan swap. Selain itu, jika biaya onchain meningkat tajam, maka akan menjadi sangat mahal untuk menggunakan Lightning.



Jadi, untuk penggunaan sesekali, ini masih dapat diterima, tetapi untuk pengguna Lightning yang sangat aktif, lebih baik melakukan segala sesuatunya dengan simpul Lightning yang sebenarnya.



### Opsi 2: Node Petir di dalam pesawat



Kategori solusi kedua didasarkan pada node Lightning yang tertanam langsung dalam aplikasi seluler. Phoenix Wallet memelopori model ini dan tetap menjadi tolok ukur. Saat ini, proyek-proyek lain menawarkan pendekatan yang sebanding, seperti Zeus (dalam mode tertanam) atau BitKit.



Idenya sederhana: aplikasi ini benar-benar menjalankan node Lightning, tetapi semua operasi yang rumit ditangani secara otomatis di latar belakang. Anda memiliki antarmuka "*Lightning wallet*" dengan frasa mnemonik untuk pencadangan, Anda melihat saldo dan membayar faktur, tetapi Anda tidak mengelola saluran, likuiditas, atau sebagian besar parameter.



![Image](assets/fr/014.webp)



Solusi ini selalu bersifat kustodian mandiri. Kunci yang mengontrol dana adalah generated dan disimpan di ponsel Anda, dan pencadangan melalui mekanisme seed atau yang setara. Anda tidak hanya memiliki akun dengan penyedia layanan, Anda benar-benar memiliki bitcoin yang terkunci di saluran yang menjadi milik Anda dan tidak dapat dicuri.



Keuntungan dari node on-board LN sangat banyak:




- sangat mudah dipasang dan digunakan;
- pengalaman pengguna yang hampir sama dengan Lightning wallet kustodian, tetapi dengan kustodian mandiri;
- tidak ada pengelolaan saluran atau likuiditas secara manual;
- pencadangan yang relatif sederhana.



Tetapi wallet yang tertanam ini juga memiliki keterbatasan yang signifikan. Pertama, dalam hal kerahasiaan, operator layanan (misalnya ACINQ dalam kasus Phoenix) memiliki pandangan yang cukup rinci tentang arus yang melewati node Anda: jumlah, frekuensi, penerima, meskipun hal ini akan meningkat, terutama dengan adopsi bertahap *Trampoline Nodes*. Kedua, anda sangat bergantung pada operator ini sebagai rekan Lightning utama anda. Jika node ACINQ tidak tersedia (dalam kasus Phoenix), jika perusahaan berada di bawah tekanan peraturan atau mengubah model bisnisnya, pengalaman pengguna Anda mungkin akan sangat terdegradasi, atau bahkan terganggu.



Akhirnya, kesederhanaan ini ada harganya. Layanan node LN yang tertanam umumnya membebankan biaya tertentu untuk deposit, penarikan atau operasi manajemen saluran tertentu. Menurut pendapat saya, model ini masuk akal dalam hal layanan yang ditawarkan, tetapi untuk penggunaan intensif, ini bisa jauh lebih mahal daripada node Lightning konvensional yang dikelola dengan baik.



### Opsi 3: simpul Lightning klasik



Solusi ketiga, yang akan kita bahas secara lebih mendalam dalam kursus LNP202 ini, adalah mengoperasikan node Lightning konvensional pada server atau perangkat khusus.



Yang saya maksud dengan "klasik" adalah Anda menginstal dan mengonfigurasi implementasi Lightning (mis. LND) sendiri di atas node Bitcoin Anda sendiri. Anda memilih rekan-rekan Anda, membuka saluran Anda, mengelola likuiditas masuk dan keluar, dan mengatur kebijakan biaya perutean Anda.



Dalam hal kedaulatan, ini adalah solusi terbaik. Anda tidak lagi bergantung pada perusahaan tertentu untuk saluran atau pembayaran Anda: jika peer menyensor Anda atau menutup saluran, Anda dapat membuka saluran lain dengan node yang berbeda. Jika sebuah layanan menghilang, sats Anda tetap berada di saluran yang Anda kendalikan, dan Anda dapat memulangkannya ke dalam rantai. Anda juga dapat mengoptimalkan biaya jangka panjang Anda: setelah saluran Anda diatur dan dikelola dengan benar, biaya pembayaran secara keseluruhan dapat menjadi sangat rendah.



Dalam hal kerahasiaan, Anda jelas tunduk pada keterbatasan model Lightning sendiri, tetapi Anda tidak menyerahkan seluruh bisnis Anda ke satu operator.



Sebaliknya, menyiapkan simpul Lightning klasik jelas lebih rumit: Anda harus menginstal, mengonfigurasi, memelihara, memantau pembaruan, memahami logika saluran dan kebijakan pengisian daya, mengelola saluran dan arus kas, dan sebagainya. Kesalahan konfigurasi, pencadangan yang ceroboh, atau manajemen yang ceroboh dapat dengan mudah menyebabkan hilangnya sats. Node juga harus berjalan terus menerus.



Inilah jalan yang saya sarankan untuk Anda ikuti dalam kursus ini, menemani Anda di setiap langkah untuk membatasi risiko dan menyusun pendekatan Anda.



### Solusi yang mana untuk profil pengguna yang mana?



Untuk memilih solusi yang tepat untuk profil pengguna Lightning Anda, Anda perlu mempertimbangkan dua faktor: seberapa sering Anda menggunakan Lightning, dan selera Anda untuk manajemen teknis.



Jika Anda tidak melakukan banyak pembayaran Lightning sesekali, tetapi masih ingin dapat menyelesaikan faktur LN dari ponsel Anda dari waktu ke waktu, tanpa melepaskan hak asuh sendiri: Bitcoin atau Liquid wallet dengan fungsionalitas swap mungkin merupakan pilihan terbaik. Anda tetap memiliki kepemilikan dana Anda, tidak mengelola node, dan menerima biaya yang sedikit lebih tinggi sebagai imbalan untuk kesederhanaan.



https://planb.academy/tutorials/wallet/mobile/bull-bitcoin-2c72127c-a228-4f50-b833-c6183d56aaf6

https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

Jika Anda menggunakan Lightning secara teratur dan menginginkan manfaat dari node yang sebenarnya, tetapi tidak ingin menghabiskan waktu untuk mengelola saluran, biaya, atau infrastruktur, node Lightning yang tertanam di ponsel adalah solusi yang baik. Anda tetap memiliki hak asuh atas dana Anda, UX tetap sangat mudah diakses, dan semua kerumitan disembunyikan, dengan harga ketergantungan yang nyata pada operator.



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

https://planb.academy/tutorials/wallet/mobile/bitkit-a7224674-85c4-4045-9baf-37018d89550c

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

Jika Anda adalah pengguna tingkat menengah atau mahir, bersedia menginvestasikan waktu untuk memahami dan mengelola infrastruktur Anda, dan menginginkan kontrol maksimum atas saluran, likuiditas, dan biaya Anda: node Lightning berbasis server klasik adalah cara yang tepat. Ini adalah solusi yang paling menuntut, tetapi juga yang paling konsisten dengan ide kedaulatan Bitcoin.




# Membuat simpul Lightning pertama Anda


<partId>b6db225e-61ab-437a-bccb-33d07503da15</partId>



## Memasang LND dengan Umbrel


<chapterId>a0014bf3-1bd3-4311-b15b-5ef2354ec744</chapterId>



Sekarang setelah kita meninjau dasar-dasar Lightning dan solusi yang tersedia, sekarang saatnya untuk mulai bekerja. Untuk mengikuti kursus ini, Anda memerlukan node Bitcoin yang disinkronkan ke Umbrel. Kursus pelatihan LNP202 ini adalah kelanjutan dari BTC 202; jika Anda belum memiliki node Bitcoin, saya mengundang Anda untuk mengikuti kursus pelatihan ini sebelum kembali ke sini setelah node Anda disinkronkan. Saya sangat menyarankan agar Anda berkonsultasi dengan kursus ini, karena saya tidak akan menjelaskan secara rinci tentang pengoperasian, konfigurasi, dan langkah-langkah keamanannya.



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

Pada bab pertama ini, kita akan melihat cara menginstal LND pada Umbrel Anda. Cara kerja Umbrel membuat langkah ini sangat sederhana, karena yang harus Anda lakukan hanyalah menginstal aplikasi.



Dari halaman beranda, buka `App Store` di bagian bawah antarmuka.



![Image](assets/fr/015.webp)



Pada bilah pencarian, masukkan `Lightning Node`, lalu klik aplikasi.



![Image](assets/fr/016.webp)



Kemudian klik tombol `Instal` untuk meluncurkan instalasi.



![Image](assets/fr/017.webp)



Dari halaman beranda, klik aplikasi untuk membukanya, lalu pilih `Setup a new node`.



![Image](assets/fr/018.webp)



Anda diberikan frasa mnemonik 24 kata. Simpan di tempat yang aman. Kita akan melihat lebih detail di bab berikutnya tentang cara mendapatkan kembali akses ke node Lightning Anda (ini adalah proses yang jauh lebih rumit daripada Bitcoin wallet yang sederhana), tetapi ingatlah untuk saat ini bahwa frasa ini memainkan peran penting dan harus disimpan dengan sangat hati-hati.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Simpan frasa ini dengan cara yang sama seperti frasa mnemonik konvensional: pada media fisik (kertas atau logam) yang disimpan di lokasi yang aman, lalu klik tombol `NEXT`.



![Image](assets/fr/019.webp)



Kemudian masukkan kata-kata dari kalimat Anda untuk memeriksa apakah Anda telah menuliskannya dengan benar.



![Image](assets/fr/020.webp)



Sebuah pesan peringatan akan mengingatkan Anda bahwa aplikasi ini masih dalam versi beta dan Lightning Network masih merupakan teknologi eksperimental. Yang jelas, jangan pernah memberikan sejumlah uang ke simpul Lightning Anda jika Anda tidak siap untuk kehilangannya.



Anda kemudian akan tiba di antarmuka utama Lightning node Anda. Di sebelah kiri, Anda akan menemukan onchain Bitcoin dan wallet yang dihosting di node Anda. Ini adalah generated dari frasa 24 kata yang baru saja Anda simpan.



Di bagian tengah, Anda akan menemukan Lightning wallet Anda. Ini sebenarnya mewakili uang tunai keluar Anda, yaitu bitcoin yang Anda miliki di dalam saluran Lightning Anda.



Di sebelah kanan, Anda akan melihat beberapa informasi penting tentang node Anda:




- Jumlah koneksi dan saluran terbuka;
- Total arus kas keluar Anda, yaitu jumlah yang secara teoritis dapat Anda belanjakan untuk Lightning;
- Total likuiditas yang masuk, yaitu apa yang secara teoritis dapat Anda terima di Lightning.



![Image](assets/fr/021.webp)



Mari kita mulai dengan menyesuaikan node kita. Klik pada tiga titik kecil di bagian kanan atas antarmuka, lalu pada `Pengaturan Lanjutan`. Pada submenu `Personalisasi`, Anda dapat menentukan nama publik untuk node Anda (hindari menggunakan nama asli Anda) dan memilih warnanya.



![Image](assets/fr/046.webp)



Kemudian klik tombol hijau `SIMPAN DAN MULAI ULANG` untuk memulai ulang simpul Anda dan menerapkan perubahan ini.



Lightning node Anda sekarang siap untuk membuka saluran pertamanya untuk melakukan pembayaran. Tapi pertama-tama, mari kita lihat cara melindungi sats Anda!



## Menyimpan simpul Lightning Anda


<chapterId>638fa75d-62af-4bf3-ab4a-b7d10ea75815</chapterId>



Sebelum mengirimkan sats pertama Anda ke node Anda, penting untuk memahami cara kerja pencadangannya dan apa saja risiko yang terkait. Tidak seperti portofolio onchain Bitcoin yang sederhana, mencadangkan node Lightning cukup rumit: strategi yang salah dapat menyebabkan hilangnya dana Anda secara permanen. Dalam bab ini, kita akan melihat apa saja yang benar-benar perlu dicadangkan, dan bagaimana Umbrel menangani proses ini dengan LND.



Dalam kursus ini, kita akan menggunakan implementasi LND (*Lightning Network Daemon*). Meskipun prinsip-prinsipnya serupa pada implementasi lainnya, file dan prosedur pemulihan yang akan saya bicarakan khusus untuk LND.



### Apa yang harus saya simpan di simpul Lightning?



Pada simpul Lightning, tidak cukup hanya dengan menyimpan seed dan berharap semuanya akan kembali normal. Beberapa elemen memainkan peran yang berbeda, jadi penting untuk membedakannya.



#### seed (*aezeed*)



Apabila Anda menginisialisasi LND, Anda akan menerima seed yang terdiri dari 24 kata. Ini adalah format khusus LND yang disebut "*aezeed*". Ini bukanlah seed BIP39 yang klasik, meskipun terlihat sangat mirip. Dari seed ini, LND mendapatkan private key dari onchain wallet Anda yang terkait dengan node Lightning, yaitu alamat tempat Anda dapat menerima atau mengembalikan bitcoin setelah penutupan channel.



![Image](assets/fr/019.webp)



Oleh karena itu, seed ini dapat digunakan untuk membuat ulang onchain wallet yang terkait dengan node Anda, dan untuk mengambil dana yang telah dipulangkan ke onchain (mis. setelah penutupan saluran). Di sisi lain, seed saja tidak cukup untuk memulihkan channel Lightning Anda yang masih terbuka, karena tidak berisi informasi yang diperlukan tentang status channel Anda.



#### Basis data saluran (`channel.db`)



LND menyimpan status detail saluran Anda dalam database bernama `channel.db`. Basis data ini berisi:




- daftar saluran terbuka Anda;
- rekan-rekan Anda dan tanda pengenal mereka;
- gW-155 terakhir untuk setiap channel (status berurutan yang mendefinisikan siapa yang memiliki apa dalam channel dan memungkinkan dana onchain untuk dipulihkan jika terjadi masalah);
- informasi yang diperlukan untuk menghukum rekan kerja yang mencoba menyiarkan laporan lama.



Masalah dengan basis data ini adalah bahwa ia terus berubah: setiap pembayaran, setiap perutean, setiap pembukaan atau penutupan saluran mengubah isinya. Inilah sebabnya mengapa cadangan konvensional (misalnya salinan periodik dari `channel.db` anda) berbahaya. Jika anda mengembalikan versi `channel.db` yang terlalu lama dan memasang kembali node dengan status usang ini, rekan-rekan anda dapat menganggap bahwa anda menyiarkan status saluran yang lama. Dalam kasus ini, protokol menyediakan penalti: rekan anda dapat memulihkan jumlah penuh dana saluran, seolah-olah anda telah mencoba untuk menipu.



Dalam praktiknya, `channel.db` bukanlah media cadangan. Ini adalah status hidup dari node Anda. Satu-satunya situasi yang masuk akal untuk menggunakannya untuk memulihkan simpul Anda adalah ketika Anda memulihkan basis data ini secara langsung dari mesin yang baru saja mengalami kegagalan (mis. disk yang masih dapat dibaca). Dalam kasus ini, Anda memulihkan status terbaru dan dapat memulai ulang LND pada mesin lain berdasarkan basis data ini, dengan aman karena mengetahui bahwa status ini sudah semutakhir mungkin, karena mesin yang lama sudah tidak berjalan. Situasi lain di mana metode ini dapat berfungsi sebagai cadangan yang relevan adalah dalam konfigurasi dua disk, dengan salinan permanen yang dinamis dari satu disk ke disk lainnya. Namun, jenis pengaturan ini lebih rumit untuk diimplementasikan.



Tetapi membuat salinan `channel.db` secara berkala dan menyimpannya sebagai cadangan untuk dipulihkan di kemudian hari adalah ide yang sangat buruk: pada hari Anda menggunakannya, Anda berisiko menghukum diri sendiri dan kehilangan semua sats Anda.



#### Cadangan Saluran Statis (SCB)



Untuk memungkinkan pemulihan bencana, LND telah memperkenalkan mekanisme *Static Channel Backup* (SCB). Ini adalah file khusus, sering disebut `channel.backup`, yang berisi informasi statis tentang saluran Anda: siapa rekan-rekan Anda, cara menghubungi mereka dan apa saluran Anda.



File ini tidak berisi status saluran yang terperinci atau riwayat pembaruan. File ini tidak memungkinkan Anda untuk membuka kembali saluran dalam kondisi yang sama persis seperti sebelumnya, atau untuk terus mengoperasikan node Lightning ini. Sebaliknya, perannya adalah bertindak sebagai titik jangkar untuk meminta rekan-rekan Anda untuk membantu Anda menutup semua saluran Anda dengan bersih, dan dengan demikian menerima onchain sats Anda, pada kunci yang dapat Anda ambil berkat seed. Jadi, tidak seperti file `channel.db`, yang dimodifikasi dengan setiap pembayaran atau perutean, file SCB hanya diperbarui ketika saluran dibuka atau ditutup.



Ketika memulihkan melalui SCB, prosesnya adalah sebagai berikut:




- Anda memulihkan seed (*aezeed*) Anda, yang membuat ulang onchain wallet Anda yang terkait dengan node Lightning;
- Anda memberikan LND dengan SCB terbaru Anda;
- LND menggunakan SCB untuk menemukan daftar rekan-rekan Anda dan saluran yang Anda miliki bersama mereka;
- Ia akan menghubungi setiap peer, memberitahu mereka bahwa Anda telah mengalami kehilangan data dan meminta mereka untuk "menutup paksa" channel Anda dengan mereka, sehingga Anda dapat memulihkan bagian onchain Anda.



Idenya adalah rekan-rekan Anda, yang mengetahui bahwa Anda melaporkan kehilangan data, akan menyiarkan commitment transaction terakhir mereka dan menutup saluran paksa. Setelah transaksi ini dikonfirmasi, dana Anda akan muncul kembali di portofolio onchain Anda (terhubung ke seed).



Namun, mekanisme pemulihan ini tidak sempurna. Pertama, mekanisme ini tidak benar-benar memulihkan simpul Lightning Anda, karena semua saluran akan ditutup. Anda kemudian harus membangun simpul Lightning baru dari awal. Kedua, protokol ini tidak menjamin pemulihan 100%, meskipun protokol ini sangat meningkatkan peluang untuk memulihkan saldo onchain Anda jika terjadi masalah. Memang, protokol pemulihan ini bergantung pada kerja sama dan ketersediaan rekan-rekan Anda: jika salah satu dari mereka sedang offline, kehilangan datanya sendiri, atau menolak untuk bekerja sama, dana Anda mungkin akan tetap diblokir, atau bahkan hilang secara permanen. Itulah mengapa penting untuk tidak membiarkan saluran tetap terbuka di node Lightning Anda dengan rekan-rekan yang tidak dapat dijangkau untuk waktu yang lama. Jika Anda mengalami kehilangan data pada saat itu dan peer tersebut tetap tidak dapat dijangkau, pemulihan melalui SCB tidak mungkin dilakukan, dan dana Anda akan tetap hilang sampai peer tersebut kembali online (mungkin selamanya).



Singkatnya, strategi cadangan Lightning yang baik pada LND bertumpu pada tiga pilar:




- seed (*aezeed*) Anda, untuk lapisan onchain;
- Pencadangan SCB otomatis yang andal;
- Manajemen saluran yang baik dengan memilih rekan-rekan yang dapat diandalkan dan secara preventif menutup saluran yang sering kali tidak dapat dijangkau.



### Bagaimana Umbrel mengelola cadangan node LND Anda?



Umbrel menawarkan mekanisme pencadangan yang disederhanakan untuk node LND, tepatnya berdasarkan SCB. Idenya adalah untuk menyelamatkan Anda dari kesulitan memanipulasi file ini sendiri, membuat cadangan dan mengotomatiskan prosesnya sejauh mungkin.



Ketika Anda membuat node pada Umbrel, Anda akan menerima seed yang memiliki peran ganda:




- ini mendapatkan Bitcoin onchain wallet Anda yang terkait dengan simpul Lightning Anda;
- digunakan untuk mendapatkan pengenal cadangan dan kunci enkripsi yang digunakan untuk cadangan SCB jarak jauh.



Berkat mekanisme ini, Umbrel secara otomatis membuat cadangan terenkripsi dari SCB Anda dan menyimpannya di server melalui Tor. SCB disimpan secara terenkripsi, berkat kunci yang berasal dari seed Anda. Jadi, jika terjadi kehilangan data, yang harus Anda lakukan adalah membuat ulang Bitcoin dan Lightning node pada Umbrel, pada mesin yang sama atau yang lain, kemudian masukkan seed Anda. Anda kemudian akan dapat mengambil status SCB terbaru dari server Umbrel, mendekripsinya, dan memulai proses pemulihan dana Anda.



Cadangan ini dienkripsi secara lokal oleh node Anda sebelum dikirim, yang menjamin kerahasiaan data Anda: Umbrel tidak dapat membaca isi dari SCB. Transmisi dilakukan melalui Tor, yang mencegah alamat IP Anda bocor. Terlebih lagi, Umbrel Anda menambahkan noise pada lalu lintas (padding acak dan backup palsu yang dikirim pada interval yang tidak teratur) untuk mencegah server menyimpulkan dengan tepat ketika Anda membuka atau menutup saluran.



Keuntungan utama dari metode ini adalah metode ini sangat menyederhanakan pencadangan node Lightning Anda: Anda hanya perlu mencadangkan seed Anda satu kali selama inisialisasi node. Hal ini memang memiliki beberapa risiko, karena ini hanya merupakan pencadangan SCB, tetapi untuk jumlah yang wajar, ini merupakan kompromi yang dapat diterima.



### Praktik terbaik untuk membatasi risiko kerugian



Bahkan dengan cadangan Umbrel, beberapa praktik sederhana yang baik dapat sangat mengurangi risiko kehilangan sats:





- Pantau ketersediaan rekan-rekan Anda:



Jika sebuah saluran penting sering dihubungkan dengan peer yang tidak dapat dijangkau atau tidak stabil, akan lebih aman jika anda menutupnya dengan bersih ketika node anda masih bekerja. Kerja sama preventif atau penutupan paksa akan menghilangkan potensi sumber masalah jika terjadi pemulihan SCB.





- Hindari memusatkan terlalu banyak likuiditas pada rekan-rekan yang tidak dikenal:



Semakin besar saluran yang dimiliki rekan Anda, semakin penting untuk dapat diandalkan. Pilihlah node yang serius, terhubung dengan baik, dan aktif, sehingga pemulihan di masa depan melalui SCB dapat berjalan dengan lancar.





- Lengkapi Umbrel dengan cadangan lokal:



Selain pencadangan otomatis Umbrel, Anda juga dapat menyimpan salinan terenkripsi dari berkas SCB (`channel.backup`) pada media eksternal dan memperbaruinya secara berkala. Idealnya, Anda harus memperbaruinya setiap kali Anda membuka atau menutup saluran. Hal ini memberi Anda solusi pencadangan jika, karena alasan apa pun, layanan pencadangan otomatis Umbrel tidak tersedia.





- Mengelola seed Anda dengan cara yang benar



seed Umbrel Anda tidak hanya memulihkan wallet onchain Anda, tetapi juga mendapatkan kunci enkripsi untuk cadangan. Oleh karena itu, penyerang yang memiliki akses ke sana dapat melakukan pemulihan dan mentransfer dana Anda ke wallet miliknya, bahkan tanpa memiliki akses fisik ke node Anda.



Jadi, jika Anda perlu memulihkan node Anda tetapi tidak lagi memiliki seed, Anda tidak akan dapat memulihkan apa pun: semua sats Anda akan hilang. Jadi, sangat penting untuk menyimpan seed Anda dengan sangat hati-hati, hanya pada media fisik (kertas atau logam), dan menyimpannya di tempat yang aman. Untuk informasi lebih lanjut mengenai cara mengelola seed, silakan baca tutorial ini:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### Bagaimana cara menyimpan node Lightning saya di Umbrel?



Sekarang setelah Anda memahami bagaimana teori ini bekerja, mari kita masuk ke hal-hal yang lebih detail. Dari aplikasi Lightning Node Anda (yang sebenarnya adalah LND), klik pada tiga titik kecil di sudut kanan atas.



![Image](assets/fr/022.webp)



Ada tiga elemen yang menarik di sini untuk cadangan:




- Pastikan bahwa opsi `Pencadangan otomatis` diaktifkan. Ini akan secara otomatis mengirimkan SCB terenkripsi Anda ke server Umbrel.
- Anda kemudian dapat memilih apakah akan mengirim melalui Tor atau clearnet, dengan menggunakan opsi `Backup over Tor`. Seperti yang telah dijelaskan pada bagian sebelumnya, saya sangat menyarankan Anda untuk menggunakan Tor untuk menjaga kerahasiaan Anda.
- Terakhir, terdapat tombol `Unduh file cadangan saluran`, yang memungkinkan Anda mengunduh file `channel.backup`, yaitu cuplikan terenkripsi dari SCB Anda, ke komputer Anda. Hal ini memungkinkan Anda untuk membuat cadangan lokal tambahan dari waktu ke waktu, selain yang secara otomatis dikirim ke server Umbrel.



Sekarang Anda sudah mengetahui cara melindungi Lightning node sats Anda dari kehilangan data. Di bab berikutnya, kita akan melihat cara mengamankan node Anda dari upaya kecurangan.




## Watchtower: peran dan pengaturan


<chapterId>e6c654dd-26c5-4e4d-8d11-a215bac37812</chapterId>



Dalam Lightning, setiap saluran didasarkan pada urutan status yang berurutan, yang diwakili oleh commitment transaction yang tidak dipublikasikan. Dengan setiap pembayaran atau perutean Lightning, 2 peserta dalam saluran membangun sepasang commitment transaction baru, yang mencerminkan distribusi dana saat ini di saluran tersebut. commitment transaction yang lama menjadi usang.



Jika salah satu pihak mempublikasikan status yang sudah kedaluwarsa, pihak lain berhak untuk memberikan sanksi dan mengembalikan seluruh dana saluran tersebut. Pada bab ini, kita akan melihat secara singkat bagaimana mekanisme ini bekerja, dan kemudian menjelaskan bagaimana cara menyiapkan menara pengawas: sebuah sistem untuk melindungi simpul Lightning Anda dari kemungkinan upaya kecurangan.



### Memahami cara kerja menara pengawas


Pada saat tertentu, setiap pihak dalam saluran memiliki commitment transaction yang, jika diterbitkan, akan memungkinkan mereka untuk menutup saluran dan memulihkan bagian dana mereka. Proses ini dikenal sebagai *pemblokiran paksa*. Tetapi jika mereka mencoba untuk menerbitkan commitment transaction yang lebih tua, sesuai dengan kondisi saluran sebelumnya yang memiliki lebih banyak sats, maka transaksi ini akan dianggap sebagai upaya kecurangan. Dalam kasus ini, pihak lawan dapat menggunakan kunci pencabutan yang terkait dengan status yang lebih lama ini untuk memulihkan jumlah penuh dana di dalam channel, sementara pihak yang curang diblokir sementara oleh timelock.


Sistem ini berarti bahwa menerbitkan status lama, yaitu mencoba melakukan kecurangan, sangat berisiko: jika pihak lain melihat transaksi ini di mempool atau di blockchain sebelum timelock berakhir, mereka dapat menggunakan kunci pencabutan dan memulihkan semua dana. **Oleh karena itu, keamanan Lightning channel Anda bergantung pada kemampuan Anda untuk mendeteksi upaya kecurangan dalam jangka waktu yang ditentukan oleh timelock**.



#### Mengapa menara pengawas diperlukan?



Mekanisme penalti hanya berlaku jika pihak yang dirugikan mampu:




- memantau setiap blok Bitcoin baru untuk melihat apakah saluran commitment transaction telah diterbitkan;
- menentukan apakah transaksi ini sesuai dengan status terakhir yang valid atau status yang dicabut;
- dalam hal status dicabut, untuk menyiarkan transaksi legal tepat waktu, menggunakan kunci pencabutan untuk memulihkan semua dana sebelum kunci waktu berakhir.



![Image](assets/fr/023.webp)



Dalam skenario yang ideal, node Lightning Anda online 24/7, disinkronkan dan terus memantau blockchain. Karena alasan ini, ia dapat mendeteksi upaya kecurangan dan bereaksi. Namun dalam praktiknya, Lightning node pribadi dapat mati, terutama jika terjadi pemadaman listrik yang berkepanjangan atau kegagalan koneksi internet.



Justru selama periode waktu henti inilah risiko menjadi nyata: jika rekan yang tidak jujur menerbitkan status lama saat node Anda offline, dan timelock habis tanpa reaksi apa pun dari Anda, kecurangan menjadi efektif. Anda kehilangan sebagian atau seluruh dana Anda di dalam channel.



Watchtower diperkenalkan untuk mengurangi risiko ini. Menara pengawas adalah sebuah layanan eksternal yang memonitor blockchain atas nama Anda, memindai kemungkinan publikasi status lama di salah satu saluran Anda, dan, jika perlu, secara otomatis menyiarkan transaksi penalti atas nama Anda. Jadi, meskipun node Lightning Anda tetap offline untuk waktu yang lama, selama menara pengawas yang Anda gunakan masih beroperasi, ia akan dapat melindungi dana Anda dengan memantau setiap upaya kecurangan dan menerapkan penalti yang sesuai, segera setelah ia mendeteksinya.



#### Bagaimana menara pengawas beroperasi



Menara pengawas dirancang untuk meminimalkan informasi yang dipelajarinya tentang saluran Anda, sekaligus memberinya sarana untuk bertindak jika terjadi masalah:




- Untuk setiap status saluran baru dengan peer, node Anda menyiapkan transaksi penalti potensial sebelumnya. Jika terjadi kecurangan peer ini, transaksi ini akan memungkinkan Anda untuk memulihkan semua dana di dalam channel;
- Node Anda kemudian mengenkripsi transaksi penalti ini menggunakan TXID dari commitment transaction yang sesuai (yang akan digunakan jika si penipu mencoba melakukan kecurangan). Selama tidak ada penutupan yang terjadi, menara pengawas tidak dapat mendekripsi transaksi ini, karena tidak sepenuhnya mengetahui TXID dari transaksi kecurangan;
- Node Anda mengirimkan sebuah paket kepada menara pengawas yang berisi transaksi penalti terenkripsi dan setengah TXID dari transaksi kecurangan yang mungkin terjadi.



Karena TXID yang dikirimkan ke menara pengawas tidak lengkap, menara pengawas tidak dapat mendekripsi transaksi keadilan. Akan tetapi, menara pengawas dapat memonitor blockchain untuk mencari TXID yang cocok dengan bagian yang dimilikinya. Jika ia mendeteksi transaksi seperti itu, maka ia akan mencoba menggunakan TXID lengkap dari transaksi tersebut untuk mendekripsi transaksi penalti Anda. Jika dekripsi berhasil, ia akan mengetahui bahwa ini adalah upaya kecurangan dan segera menerbitkan transaksi penalti untuk Anda.



![Image](assets/fr/024.webp)



Oleh karena itu, menara pengawas tidak memiliki visibilitas terhadap detail saluran Anda: baik identitas rekan-rekan Anda, maupun saldo, maupun struktur transaksi. Menara pengawas hanya melihat paket yang dienkripsi. Satu-satunya informasi yang dapat disimpulkannya adalah kecepatan pembaruan saluran Anda, karena ia menerima paket untuk setiap status baru, tetapi tidak dapat mengetahui isinya. Jika terjadi kecurangan, ia pasti akan menemukan informasi saluran dengan mendekripsi transaksi penalti, tetapi setidaknya sats anda akan terselamatkan.



Mekanisme ini didasarkan pada sebuah kompromi: Anda mendelegasikan kemampuan untuk mempublikasikan transaksi penalti yang telah ditandatangani sebelumnya kepada menara pengawas, tetapi transaksi ini tetap tidak dapat dilihat oleh menara pengawas sampai beberapa kecurangan terjadi. Menara pengawas tidak dapat mengubah penerima atau mengalihkan dana, karena menara pengawas hanya memiliki transaksi yang telah ditandatangani, dengan output yang dibekukan untuk Anda. Menara pengawas juga tidak dapat mengetahui detail saluran dalam penutupan paksa atau kooperatif yang sah, karena TXID-nya tidak cocok. Di sisi lain, Menara Pengawal tetap menjadi pihak ketiga yang paling tidak terpercaya: Anda harus mengandalkannya untuk online dan menyiarkan transaksi keadilan Anda dengan benar ketika Anda membutuhkannya.



#### Menjadi menara pengawas



Secara teori, setiap node Lightning dapat bertindak sebagai menara pengawas untuk node lain (jika mereka menggunakan implementasi yang sama, misalnya LND), sementara itu sendiri dilindungi oleh node lain yang memainkan peran ini untuknya. Pada bagian praktis berikut ini, saya akan menunjukkan kepada Anda cara mengatur mekanisme sederhana ini pada LND Anda di bawah Umbrel.


Sebagai konsekuensinya, strategi yang menarik mungkin adalah dengan bersepakat dengan teman-teman bitcoiner yang terpercaya untuk bertindak sebagai menara pengawas satu sama lain. Anda memantau saluran mereka, dan mereka memantau saluran Anda.



### Temukan menara pengawas altruistik



Jika Anda tidak mengenal siapa pun di sekitar Anda yang dapat menyediakan layanan menara pengawas, ada sejumlah menara pengawas publik yang bersifat altruistik yang dapat Anda hubungkan. Contohnya, dalam kursus LNP202 ini, saya sarankan Anda terhubung ke layanan menara pengawas yang ditawarkan bersama oleh LN+ dan Voltage, yang merupakan menara pengawas untuk LND.


Di sini Anda memiliki detail login:



- Via Tor:


```txt
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



- Melalui clearnet:


```txt
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@34.216.52.158:9911
```

Untuk berterima kasih kepada mereka yang telah menyediakan layanan menara pengawas gratis ini, [Anda dapat memberikan donasi melalui Lightning](https://lightningnetwork.plus/donation).


Sekarang kita menggunakan layanan menara pengawas altruistik, mari kita lihat bagaimana mengkonfigurasinya pada node LND di bawah Umbrel.


### Menyiapkan menara pengawas


Dari aplikasi `Lightning Node`, klik pada tiga titik di kanan atas antarmuka, kemudian pilih `Advanced Settings`.


![Image](assets/fr/025.webp)


Kemudian buka menu `Watchtower`.


![Image](assets/fr/026.webp)



Aktifkan opsi `Klien Watchtower`, lalu klik tombol `SELAMATKAN DAN MULAI ULANG NODE`. Tunggu hingga LND dimulai ulang.


![Image](assets/fr/027.webp)


Setelah restart selesai, kembali ke menu yang sama dan masukkan ID menara pengawas altruistik pilihan Anda pada kolom yang tersedia. Kemudian klik tombol `TAMBAH` untuk mengonfirmasi. Anda juga dapat menyesuaikan parameter `Tingkat Biaya Sapuan Klien Watchtower`: ini adalah tingkat biaya yang bersedia Anda bayarkan untuk transaksi keadilan yang disiarkan oleh menara pengawas. Anda tidak perlu memilih tarif yang terlalu tinggi, tetapi Anda juga harus menghindari tarif yang terlalu rendah, jika tidak, transaksi legal tidak akan dikonfirmasi tepat waktu.


Mulai ulang node Anda menggunakan tombol `SELAMATKAN DAN MULAI ULANG NODE` untuk menerapkan perubahan ini.


![Image](assets/fr/028.webp)



Jika Anda kembali ke menu yang sama, Anda akan melihat bahwa node Lightning Anda sekarang dilindungi oleh menara pengawas yang baru saja Anda tambahkan.



![Image](assets/fr/029.webp)



Sebuah menara pengawas altruistik pada umumnya sudah cukup, terutama jika Anda tidak menaruh uang dalam jumlah besar pada node Lightning Anda dan jika Anda mengelola node Anda dengan baik (jangan biarkan terlalu lama). Untuk keamanan yang lebih baik lagi, Anda juga bisa menambahkan beberapa dengan mengulangi proses yang sama.



## Buka saluran Lightning pertama Anda


<chapterId>00642af7-8f3d-4a25-96d7-34e85de7bd5d</chapterId>



Jika Anda sudah sampai sejauh ini, Anda sudah tahu bahwa node Lightning tanpa saluran seperti wallet yang kosong: ada, tetapi tidak berguna. Untuk dapat mengirim atau menerima pembayaran, node Anda harus terhubung ke setidaknya satu node lain di jaringan Lightning melalui saluran. Di masa depan, kami sangat menyarankan untuk membuka beberapa saluran, untuk alasan ketahanan dan efisiensi perutean. Pada bab-bab berikutnya, kita juga akan melihat bagaimana cara mengelola aset likuid Anda, mengoptimalkan topologi saluran Anda, dan menggunakan alat yang lebih canggih daripada antarmuka LND dasar pada Umbrel.



Tetapi dalam bab pengantar ini, tujuannya hanya untuk memahami cara memilih peer Lightning yang baik, di mana menemukan informasi yang Anda perlukan untuk memilih peer Anda, dan akhirnya cara membuka saluran pertama Anda melalui antarmuka dasar LND.



### Bagaimana cara memilih rekan Lightning yang baik?



Ketika Anda membuka saluran, Anda harus memilih peer: node Lightning lain yang akan terhubung langsung dengan node Anda, melalui saluran. Pilihan peer ini penting, karena akan berdampak langsung pada:




- kemudahan bagi pembayaran Anda untuk menemukan jalannya;
- keandalan saluran Anda dari waktu ke waktu;
- biaya perutean Anda.



Tidak ada yang namanya pasangan yang sempurna untuk semua orang, tetapi ada sejumlah kriteria yang dapat diandalkan untuk mengidentifikasi kandidat yang baik.



#### 1. Konektivitas simpul



Peer yang baik adalah node yang terhubung dengan baik ke jaringan Lightning. Ini berarti tidak hanya memiliki sejumlah besar saluran (meskipun ini dapat menjadi indikator), tetapi di atas semua itu terhubung ke node lain yang dapat diandalkan dan menempati posisi yang cukup sentral dalam grafik jaringan.



Simpul yang terhubung dengan baik meningkatkan peluang Anda untuk menemukan rute yang efisien ke sebagian besar tujuan pembayaran. Hal ini juga mengurangi jumlah simpul perantara yang dibutuhkan, sehingga menekan biaya.



Sebaliknya, membuka saluran pertama Anda ke node yang terisolasi atau terhubung dengan lemah dapat membatasi kemungkinan Anda: Anda akan dapat membayar peer ini, tetapi akan jauh lebih sulit untuk membayar sisa jaringan.



#### 2. Kapitalisasi dan kapasitas saluran



Peer yang baik juga merupakan simpul yang memiliki kapitalisasi yang memadai. Hal ini ditunjukkan oleh total kapasitas salurannya (jumlah sats yang dikomitmenkan untuk semua salurannya) dan kapasitas saluran rata-rata (sering kali lebih baik memiliki beberapa saluran yang bermodal besar daripada banyak saluran kecil).



Sebuah node dengan kapasitas yang tidak masuk akal, atau yang semua salurannya kecil, tidak akan dapat merutekan pembayaran dengan jumlah besar, yang mengakibatkan kegagalan perutean untuk Anda.



#### 3. Kebijakan pengeluaran



Setiap node menetapkan biaya routingnya sendiri (`biaya dasar` dan `tarif biaya`). Peer yang baik tidak akan mengenakan biaya yang terlalu tinggi untuk saluran strategis. Untuk saluran pertama, yang terbaik adalah memilih node dengan biaya yang agak moderat, agar tidak menghambat pembayaran Anda sendiri.



Ingatlah bahwa biaya perutean Anda sendiri juga memengaruhi cara orang lain memandang Anda sebagai rekan: simpul yang terus-menerus mengubah biayanya atau membebankan biaya yang tidak masuk akal jarang dihargai.



#### 4. Stabilitas dan senioritas



Stabilitas peer adalah kriteria yang sangat penting. Node yang baik memiliki waktu aktif yang tinggi (sangat jarang offline), menjaga salurannya tetap terbuka untuk waktu yang lama dan tidak terus-menerus membuka/menutup saluran tanpa alasan.



Saluran yang lama dan masih aktif merupakan sinyal yang baik: mereka menunjukkan bahwa hubungan tersebut menguntungkan bagi peer, bahwa node tersebut mengetahui cara mengelola modalnya dan tidak menutup setiap saat, sehingga Anda tidak perlu terus membayar biaya onchain untuk menutup dan membuka kembali.



Sebaliknya, rekan yang sering offline, atau yang dengan cepat menutup saluran, dapat menjadi sumber masalah bagi Anda, dan biaya tambahan untuk membuka saluran baru.



Bahkan dengan kriteria ini, Anda tidak akan membuat pilihan yang sempurna pada kali pertama. Itu normal: kualitas sesungguhnya dari suatu produk terungkap dari penggunaannya. Jadi, ini penting untuk dilakukan:




- memantau aktivitas saluran (volume yang dirutekan, ketersediaan, dll.);
- menutup saluran yang tidak memiliki tujuan atau yang rekan-rekannya terlalu sering offline;
- mengalokasikan kembali modal Anda ke rekan-rekan yang lebih baik dari waktu ke waktu.



Idenya adalah untuk tidak membuka dan menutup saluran setiap hari (yang akan menjadi mahal dalam biaya onchain), tetapi secara bertahap mengembangkan topologi Anda untuk menyatu pada satu set peer yang dapat diandalkan dan terhubung dengan baik yang kompatibel dengan kebutuhan Anda.



### Bagaimana cara menemukan rekan sejawat?



Untuk menerapkan kriteria ini, Anda memerlukan alat yang menyediakan visibilitas jaringan Lightning. Ada beberapa penjelajah dan layanan yang tersedia untuk melakukan ini. Di antara penjelajah Lightning yang paling terkenal adalah [1ML] (https://1ml.com/) dan [Amboss] (https://amboss.space/).



https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017

https://planb.academy/tutorials/node/lightning-network/1ml-37ada2ab-7a24-4473-87fd-007cb7640e7b

Di sini, bagaimanapun, saya sarankan Anda menggunakan [alat Lightning Terminal dari Lightning Labs](https://terminal.lightning.engineering/), yang menyediakan peringkat (memang berdasarkan kriteria yang sebagian subyektif) dari node Lightning yang dianggap paling relevan untuk membuka saluran.



![Image](assets/fr/030.webp)



Masalah dengan node Lightning yang sangat besar di bagian atas peringkat ini adalah sebagian besar tidak menerima pembukaan saluran di bawah jumlah yang sangat tinggi. Banyak juga yang menerapkan kebijakan manajemen peer yang ketat, yang dapat menyebabkan saluran Anda ditutup. Di sisi lain, node-node ini umumnya tidak membutuhkan likuiditas yang masuk, mengingat jumlah koneksinya.



Oleh karena itu, saya menyarankan Anda untuk bekerja dengan cara menuruni peringkat untuk menemukan simpul yang terhubung dengan baik, dapat diandalkan, dan cukup sentral dalam grafik jaringan, tanpa menjadi terlalu besar. Sebagai contoh, di sini saya telah mengidentifikasi simpul Lightning di stacker.news, yang terhubung dengan sangat baik, memiliki kapasitas tinggi dan menempati posisi sentral dalam grafik jaringan.



![Image](assets/fr/031.webp)



Pendekatan lain yang menarik adalah dengan membuka saluran ke simpul yang membutuhkan likuiditas masuk, seperti pedagang yang Anda kenal, asosiasi, atau komunitas. Strategi ini memiliki tiga keuntungan:




- Karena entitas yang dipilih membutuhkan likuiditas yang masuk, maka secara logis akan lebih sedikit insentif untuk menutup saluran Anda tanpa alasan;
- Aktivitas ekonominya meningkatkan peluang untuk melakukan routing pada saluran ini, dan oleh karena itu mengumpulkan sejumlah biaya;
- Anda membantu ekosistem dan memberikan kontribusi yang berharga bagi para pengguna bitcoin lainnya.



Setelah Anda mengidentifikasi simpul yang relevan, Anda dapat mengambil ID Simpulnya. Ini hanyalah gabungan dari kunci publik simpul, pemisah `@`, alamat IP atau Tor, dan port yang digunakan. ID ini mudah diakses dari profil node pada penjelajah Lightning mana pun.



### Buka saluran pertama Anda melalui LND



Sekarang kita telah mengidentifikasi node yang akan digunakan untuk membuka saluran pertama kita, kita membutuhkan sats untuk menguncinya. Untuk melakukan ini, Anda perlu memberi makan Bitcoin pada rantai wallet yang terkait dengan LND Anda.



Dari antarmuka utama LND, cari `Bitcoin Wallet` Anda, lalu klik tombol `Deposit`. Alamat penerima onchain adalah generated: kirimkan sats ke alamat tersebut. Jumlah yang perlu Anda transfer tergantung pada kapasitas yang ingin Anda alokasikan ke saluran pertama Anda, tetapi perlu diingat bahwa Anda perlu mengirim sedikit lebih banyak dari kapasitas yang ditargetkan. Sebagai contoh, jika Anda ingin membuka saluran 500.000 sats, jangan mengirim 500.000 sats secara tepat, tetapi jumlah yang lebih tinggi.



![Image](assets/fr/032.webp)



Setelah transaksi disiarkan, transaksi akan muncul di antarmuka. Tunggu konfirmasi sebelum membuka saluran. Anda akan melihat panah hijau di sebelahnya ketika sudah dikonfirmasi.



![Image](assets/fr/033.webp)



Gulir ke bawah ke antarmuka utama, lalu klik `+ OPEN CHANNEL`.



![Image](assets/fr/034.webp)



Masukkan `Node ID` dari node yang ingin Anda gunakan untuk membuka saluran, tunjukkan jumlah yang ingin Anda kunci, lalu sesuaikan biaya transaksi pembukaan sesuai dengan kondisi pasar biaya onchain. Tentu saja, pastikan Anda memiliki dana yang cukup dalam portofolio onchain LND Anda sebelumnya.



Setelah semua parameter ditetapkan, klik tombol `BUKA SALURAN`.



![Image](assets/fr/035.webp)



Tunggu hingga transaksi pembukaan dikonfirmasi di blockchain. Saluran pertama Anda sekarang secara resmi beroperasi: selamat!



Anda dapat melihat bahwa, untuk saat ini, 100% likuiditas saluran ada di pihak saya: itu normal, karena sayalah yang membuka saluran tersebut. Seiring dengan perkembangan pembayaran dan perutean, distribusi ini akan berubah, tetapi kapasitas total saluran akan selalu tetap sama.



![Image](assets/fr/036.webp)



Sekarang setelah Anda memiliki saluran, Anda bisa melakukan pembayaran Lightning pertama Anda, asalkan node yang dipilih terhubung dengan benar ke jaringan. Tentu saja, di bab selanjutnya kita akan melihat cara menyiapkan metode yang lebih nyaman untuk membayar faktur Lightning dari ponsel Anda. Tetapi untuk saat ini, mari kita coba melakukan pembayaran pertama secara langsung dari LND ke Umbrel.



Untuk melakukan ini, di bagian `Lightning Wallet`, klik tombol `KIRIM`, lalu tempelkan faktur yang akan diatur.



![Image](assets/fr/037.webp)



Jumlah faktur akan ditampilkan. Konfirmasikan pembayaran dengan mengeklik tombol `KIRIM`.



![Image](assets/fr/038.webp)



Jika rute yang valid ditemukan, pembayaran Lightning pertama Anda akan berhasil.



![Image](assets/fr/039.webp)



Jika kita melihat distribusi likuiditas dalam saluran, kita melihat bahwa rekan saya sekarang memiliki 5.002 sats di sisinya. Ini sesuai dengan 5.000 sats dari pembayaran yang baru saja saya lakukan, yang dia alihkan ke node penerima. Tambahan 2 sats mewakili biaya routing yang saya bayarkan, karena penerima menerima 5.000 sats dengan tepat.



![Image](assets/fr/040.webp)



Untuk meningkatkan keandalan pembayaran kita, tentu saja kita perlu membuka saluran lain. Bergantung pada tujuan kita, kita juga perlu menemukan cara untuk menyediakan likuiditas yang masuk sehingga kita dapat menerima pembayaran di Lightning. Ini akan menjadi topik bahasan di bagian selanjutnya.



# Mengelola simpul Lightning Anda


<partId>e27c3e1e-487b-4414-ad6b-d67bdb91c7c5</partId>



## Tentukan profil operator node Anda


<chapterId>d3b2e163-50f6-4d1d-a5fc-8fd177dfac76</chapterId>



Setelah Lightning node Anda aktif dan berjalan, langkah selanjutnya adalah menentukan profil trader Anda. Ini adalah pilihan yang penting, karena ini menentukan strategi pembukaan saluran Anda, jenis rekan yang Anda sukai, dan cara Anda mengelola likuiditas.



Di Lightning, agar ini berfungsi, Anda membutuhkan likuiditas ke arah yang benar. Likuiditas keluar sesuai dengan kemampuan Anda untuk membayar (sats tersedia di sisi saluran Anda). Likuiditas yang masuk sesuai dengan kapasitas Anda untuk menerima (sats tersedia di sisi rekan-rekan Anda). Dengan kata lain, profil Anda bermuara pada pertanyaan sederhana: sebagian besar waktu, apakah sats Anda meninggalkan node Anda, atau memasukinya?



### Konsumen



Ini adalah profil sebagian besar pengguna. Anda menggunakan node Anda untuk melakukan pembayaran Lightning: untuk membeli barang dan jasa, membayar tagihan, mengirim tip - singkatnya, untuk menggunakan Lightning sebagai alat pembayaran yang cepat. Di sisi lain, Anda menerima sedikit dari Lightning, atau hanya sedikit, misalnya beberapa donasi, pengembalian uang antar teman, atau beberapa pembayaran mikro.



Profil ini adalah yang paling mudah dikelola, karena kebutuhan utama Anda adalah mampu membayar. Secara praktis, ini berarti Anda membutuhkan likuiditas keluar. Setelah Anda membuka satu atau beberapa saluran dengan ukuran yang tepat ke node yang stabil dan terhubung dengan baik, pembayaran keluar Anda akan secara otomatis memindahkan likuiditas ke sisi lain saluran Anda. Pergerakan inilah yang secara alami menciptakan jumlah likuiditas yang masuk secara wajar. Hasilnya, meskipun Anda tidak ingin menerima secara teratur, Anda masih dapat menerima dari waktu ke waktu tanpa menerapkan strategi yang rumit. Jadi, Anda tidak perlu khawatir dengan likuiditas yang masuk.



Dalam kursus LNP202 ini, kita akan fokus pada profil operator node "konsumen" ini, karena ini adalah profil yang sesuai dengan hampir semua pengguna Bitcoin di Lightning.



### Pengecer



Pedagang, di satu sisi, adalah kebalikan dari konsumen. Di sini, tujuan utamanya bukan untuk membayar, tetapi untuk menagih. Sebuah bisnis, penyedia layanan, toko online, atau tempat penjualan yang menerima Lightning akan menerima banyak pembayaran masuk, dan melakukan pembayaran keluar yang relatif sedikit dari node ini.



Profil ini lebih menuntut, karena pembayaran yang ditolak di Lightning berpotensi menimbulkan penjualan yang hilang. Oleh karena itu, prioritasnya adalah likuiditas masuk. Jika node Anda tidak memiliki cukup inbound, pelanggan Anda akan melihat pembayaran mereka gagal, bahkan jika mereka memiliki dana, hanya karena tidak ada rute untuk mengalirkan likuiditas ke arah yang benar.



Tantangan utama bagi pedagang juga datang dari evolusi alami saluran. Jika yang Anda lakukan hanyalah menerima, saluran Anda secara bertahap akan terisi di sisi Anda. Jadi, Anda memerlukan mekanisme untuk mempertahankan dan memperbarui likuiditas yang masuk.



Namun, ada kasus yang lebih sederhana: profil konsumen/pengusaha campuran. Jika Anda mengumpulkan di Lightning, tetapi juga membelanjakan di Lightning (pengeluaran bisnis, pembayaran kepada pemasok, atau bahkan pengeluaran pribadi), maka pembayaran keluar Anda secara alami akan menciptakan pembayaran masuk. Manajemen menjadi lebih lancar, karena arus saling mengimbangi, dan Anda tidak perlu menggunakan mekanisme buatan yang dirancang semata-mata untuk mendapatkan kembali likuiditas masuk.



### Router



Router adalah profil yang spesifik. Ia tidak menggunakan simpul Lightning untuk membayar atau mengumpulkan, tetapi untuk merutekan pembayaran orang lain dan mengumpulkan biaya. Tujuannya adalah untuk menjadi rute yang berguna, dapat diandalkan, dan kompetitif secara ekonomi di dalam grafik Lightning.



Sejujurnya, menjadi router di Lightning adalah bisnis yang lebih kompleks daripada yang terlihat, dan profitabilitas sulit dicapai. Pertama-tama, membuka dan menutup saluran mahal dalam biaya onchain. Untuk merutekan secara efisien, Anda sering kali harus menyesuaikan topologi, menguji, menutup saluran yang berkinerja buruk, membuka saluran baru, dan menyeimbangkan kembali likuiditas Anda secara teratur. Kedua, persaingan sangat ketat: node yang besar dan mapan secara alami menangkap sebagian besar lalu lintas, dan sulit untuk mendapatkan pijakan tanpa mengikat modal yang signifikan di saluran yang berukuran besar.



Ada juga persyaratan operasional yang tinggi. Sebuah simpul perutean harus sangat stabil, dipantau, dicadangkan dengan benar, dan dikelola dengan ketat. Anda harus memantau kinerja saluran, menyesuaikan kebijakan biaya, menjaga likuiditas yang seimbang, mengelola rekan kerja, dan dengan cepat menyelesaikan masalah teknis. Tingkat keterlibatan ini bisa menarik sebagai hobi teknis atau sebagai kontribusi terhadap infrastruktur, tetapi jika tujuan Anda hanya untuk menggunakan Lightning dengan cara yang berdaulat, masuk ke dalam perutean untuk menghasilkan uang jarang relevan. Itulah mengapa kursus ini tidak membahas profil ini secara mendalam.



### Posisikan diri Anda dengan jelas sebelum melangkah lebih jauh



Jika Anda sesuai dengan profil konsumen, prioritas Anda adalah untuk dapat membayar dengan andal dengan manajemen yang sederhana. Jika Anda seorang pedagang, prioritas Anda adalah untuk menguangkan tanpa kegagalan, yang menyiratkan strategi akuisisi likuiditas masuk. Jika Anda mempertimbangkan perutean, Anda perlu mendekatinya sebagai aktivitas yang menuntut, tidak pasti secara ekonomi, dan memakan waktu.



Mendefinisikan profil ini sekarang akan membantu Anda menghindari jebakan klasik: menerapkan strategi saluran yang dirancang untuk pedagang atau router, padahal Anda hanyalah pengguna yang ingin membayar.



## Menggunakan pengelola simpul Lightning


<chapterId>02eb4c09-d14b-4ff0-8b04-b90de3307d34</chapterId>



Pada bagian sebelumnya dari kursus pelatihan LNP202 ini, kami menggunakan antarmuka dasar dari aplikasi `Lightning Node` pada Umbrel. Antarmuka ini cukup untuk operasi yang penting (memeriksa saldo, melihat distribusi uang tunai, membuka dan menutup saluran), tetapi dengan sengaja dibuat sangat sederhana. Kesederhanaan ini membatasi pilihan yang tersedia dan tidak memberikan akses ke banyak fitur canggih dari node LND Anda. Untuk alasan ini, kita sekarang akan menggunakan perangkat lunak manajemen node Lightning lain yang lebih komprehensif.



Perangkat lunak tambahan ini hanya akan menjadi antarmuka manajemen pelengkap untuk node Anda. Ini berarti Anda dapat terus menggunakan antarmuka `Lightning Node` secara paralel, dan bahkan menggunakan beberapa antarmuka yang berbeda jika Anda mau. Ini hanyalah cara yang berbeda untuk berinteraksi dengan Lightning node yang sama.



Di antara program perangkat lunak yang paling terkenal adalah:




- [Alby Hub] (https://albyhub.com/);
- [Ride The Lightning](https://www.ridethelightning.info/);
- [ThunderHub] (https://thunderhub.io/).



Ketiganya merupakan solusi yang baik. Jika mau, Anda bisa menguji ketiganya dengan simpul Anda sebelum memilih salah satu yang paling cocok untuk Anda. Secara pribadi, saya menggunakan ThunderHub karena kebiasaan dan karena kelihatannya lebih lengkap daripada yang lain. Ini adalah alat yang akan saya sajikan dalam kursus pelatihan ini, tetapi Anda juga dapat memilih salah satu dari dua alternatif lainnya. Kami memiliki tutorial khusus untuk masing-masing program ini pada Plan ₿ Academy.



https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

https://planb.academy/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

### Pasang ThunderHub



Semua program ini dapat diinstal dengan sangat mudah dari App Store Umbrel. Seperti yang saya katakan, kita akan menggunakan ThunderHub di sini, tetapi jika Anda ingin menguji yang lain nanti, prosedurnya akan serupa.



![Image](assets/fr/041.webp)



Umbrel memberi Anda kata sandi default untuk mengakses ThunderHub. Salinlah: Anda akan membutuhkannya segera. Ingatlah juga untuk menyimpannya di pengelola kata sandi Anda, karena Anda akan diminta untuk memasukkannya setiap kali Anda membuka perangkat lunak.



![Image](assets/fr/042.webp)



Klik `Login`, lalu tempelkan kata sandi yang diberikan oleh Umbrel untuk masuk.



![Image](assets/fr/043.webp)



Anda kemudian akan dibawa ke halaman beranda ThunderHub, yang menampilkan informasi utama tentang node Lightning Anda.



![Image](assets/fr/044.webp)



Untuk memulainya, saya sarankan Anda mengaktifkan autentikasi dua faktor (2FA). Dalam pengaturan, cukup klik `Aktifkan` di samping `Aktifkan 2FA`, lalu ikuti proses seperti biasa.



![Image](assets/fr/045.webp)



### Gunakan ThunderHub



ThunderHub relatif mudah dipelajari. Semua menu dapat diakses dari kolom sebelah kiri antarmuka. Sebagai rangkuman, berikut ini adalah fungsi masing-masing menu:




- beranda: ikhtisar simpul, saldo, dan tindakan cepat;
- dasbor: dasbor yang dapat disesuaikan dengan widget dan metrik;
- rekan: melihat dan mengelola koneksi ke node Lightning lainnya;
- saluran: manajemen saluran lengkap (likuiditas, biaya, penutupan, dll.);
- rebalance": alat untuk menyeimbangkan kembali saluran melalui pembayaran melingkar;
- transaksi: riwayat pembayaran Lightning yang dikirim dan diterima;
- forwards`: statistik perutean dan biaya generated oleh node Anda;
- 'Rantai': Portofolio onchain Bitcoin (UTXO dan transaksi);
- integrasi gW-201 untuk pemantauan dan pencadangan;
- `Tools`: alat bantu tingkat lanjut (cadangan, laporan, makaroni, tanda tangan, dll.);
- swap: Lightning/onchain swap melalui Boltz;
- `Statistik`: statistik keseluruhan dan kinerja node Lightning Anda.



Dengan serangkaian fungsi ini, Anda memiliki semua alat yang Anda perlukan untuk mengelola node Lightning secara efisien. Tidaklah penting untuk menguasai setiap opsi secara mendetail dengan segera: kita akan menjelajahinya secara bertahap di sepanjang kursus ini. Namun, jika Anda ingin memahami perangkat lunak ini secara lebih mendalam, lihat tutorial ThunderHub kami:



https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

Menu yang paling kami minati di sini adalah `Channels`. Menu ini menawarkan tampilan terperinci dari semua saluran di node Anda, dengan distribusi likuiditasnya. Secara khusus, Anda dapat melihat saluran mana yang terbuka di `Open`, yang menunggu untuk dibuka atau ditutup di `Pending`, dan yang sudah ditutup di `Closed`.



![Image](assets/fr/047.webp)



Untuk saluran tertentu, Anda dapat mengklik nama peer atau ID saluran untuk membuka halaman Amboss dan mendapatkan informasi lebih lanjut. Anda juga dapat mengklik ikon pensil untuk memodifikasi parameter saluran, termasuk kebijakan biaya yang diterapkan pada saluran tersebut jika node Anda merutekan pembayaran ke node peer Anda.



![Image](assets/fr/048.webp)



Jika Anda menggunakan node Lightning Anda terutama sebagai "konsumen", Anda tidak perlu mengubah muatan ini: Anda dapat mempertahankan nilai default. Di sisi lain, jika Anda ingin lebih memahami cara kerja routing charge pada Lightning, saya merekomendasikan pelatihan LNP 201, dan khususnya bab 4.1:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Dengan mengklik tanda silang kecil di samping sebuah peer, Anda dapat memulai penutupan sebuah channel. Jika Anda melihat, misalnya, bahwa sebuah peer sering tidak aktif, mungkin sebaiknya Anda menutup channel tersebut untuk mengalokasikan kembali modal Anda ke peer yang lebih dapat diandalkan.



Anda kemudian memiliki dua pilihan. Yang pertama, dan selalu lebih baik, adalah penutupan kooperatif. Dengan mengonfirmasi tindakan ini, node Anda meminta rekan Anda untuk menutup saluran secara bersama-sama. Jika dia menerimanya, Anda dapat menyiarkan transaksi penutupan onchain dan mendapatkan kembali bagian dana Anda. Keuntungan dari metode ini adalah Anda memilih biaya onchain untuk transaksi tersebut, sehingga menghindari biaya yang tidak perlu, dan dana dipulihkan dengan lebih cepat, tanpa adanya penguncian waktu.



![Image](assets/fr/049.webp)



Opsi kedua adalah penutupan paksa. Dalam hal ini, Anda tidak meminta persetujuan rekan dan langsung menyiarkan commitment transaction terakhir yang Anda miliki. Saya tidak akan merekomendasikan metode ini kecuali sebagai pilihan terakhir, misalnya jika rekan secara sistematis menolak penutupan kooperatif atau tidak lagi merespons. Penutupan paksa memiliki dua kelemahan utama: biayanya sering kali sangat tinggi, karena telah ditetapkan sebelumnya untuk mengantisipasi kenaikan biaya onchain, dan ada penundaan dalam memulihkan dana, karena diblokir oleh kunci waktu. Penguncian waktu ini memberikan waktu bagi rekan Anda untuk bereaksi jika terjadi upaya kecurangan (yang jelas tidak terjadi di sini, tetapi Anda masih harus menunggu).



![Image](assets/fr/050.webp)



Terakhir, untuk membuka saluran baru, masuk ke menu `Home` dan klik `Buka Saluran` di bagian `Liquidity`. Anda kemudian akan dapat memasukkan ID node yang dipilih, kapasitas saluran, biaya perutean Lightning yang diinginkan, dan biaya onchain untuk transaksi pembukaan.



![Image](assets/fr/051.webp)



Ini adalah tindakan utama yang harus Anda lakukan pada ThunderHub. Kita akan menemukan fitur-fitur lainnya sambil belajar dalam kursus LNP202 ini.



## Memperoleh likuiditas yang masuk


<chapterId>b740c656-a897-4d95-af4b-116b718447cd</chapterId>



Seperti yang Anda lihat, memiliki likuiditas keluar untuk melakukan pembayaran di Lightning tidak terlalu rumit. Cukup buka saluran atas inisiatif Anda sendiri ke node lain dan mulailah mengirim sats. Di sisi lain, memiliki likuiditas masuk untuk menerima pembayaran di Lightning lebih rumit, karena Anda membutuhkan node lain untuk membuka saluran untuk Anda, atau Anda perlu memindahkan likuiditas sendiri dengan melakukan pembayaran.



Jika Anda mengadopsi profil "konsumen", umumnya tidak perlu khawatir tentang likuiditas yang masuk. Penggunaan node Lightning Anda akan lebih banyak berorientasi pada pembayaran, bukan pada uang tunai. Dengan hanya melakukan beberapa pembayaran Lightning, Anda akan secara alami menciptakan likuiditas yang masuk dari waktu ke waktu.



Di sisi lain, jika Anda memiliki profil "pedagang", situasinya terbalik: Anda terutama akan mengumpulkan pembayaran dan melakukan sedikit pembayaran. Jadi, Anda tidak bisa hanya mengandalkan pembayaran Anda sendiri untuk likuiditas yang masuk. Oleh karena itu, node Lightning lain perlu membuka saluran ke node Anda. Tetapi bagaimana hal ini dapat dicapai? Bagaimana Anda membuat operator lain mengikat modal untuk Anda? Itulah yang akan kita bahas dalam bab ini.



### Membeli likuiditas masuk



Seperti yang Anda duga, cara paling efektif untuk membuat seseorang bertindak adalah dengan membayar mereka. Untuk likuiditas yang masuk ke node Lightning Anda, prinsipnya sama persis. Cara paling sederhana untuk mendapatkan saluran ke node Anda adalah dengan membayar layanan dan ikatan modal yang terlibat.



Jika Anda adalah sebuah bisnis atau peritel, pendekatan ini berarti Anda dapat dengan cepat mendapatkan saluran yang dapat diandalkan untuk mengumpulkan pembayaran dari pelanggan Anda tanpa hambatan.



Ada banyak cara untuk membeli likuiditas masuk. Salah satu yang saya gunakan dan rekomendasikan secara pribadi adalah platform Amboss (https://magma.amboss.tech/). Ini sangat mudah digunakan, membuka salurannya cepat dan tarifnya umumnya masuk akal. Magma bekerja seperti pasar dengan pembuat dan penerima, tetapi versi 2 telah sangat menyederhanakan pengalamannya: cukup buat permintaan, bayar harga melalui Lightning, dan Magma secara otomatis mencocokkannya dengan penawaran terbaik yang tersedia. Setelah enam konfirmasi onchain, saluran Anda dengan likuiditas yang masuk sudah aktif dan berjalan. Begini cara kerjanya:



Kunjungi [situs web Magma](https://magma.amboss.tech/buy), di bagian `Beli Saluran`.



![Image](assets/fr/052.webp)



Jika Anda mau, Anda dapat membuat akun untuk melacak pembelian Anda, tetapi ini tidak wajib. Jika Anda tidak membuat akun, Magma hanya akan memberi Anda ID sesi, yang akan memungkinkan Anda untuk mengambil pembelian Anda di kemudian hari.



Setelah berada di situs, isi informasi yang diperlukan untuk membeli likuiditas. Pilih `Satu Kali` untuk pembelian satu kali, lalu masukkan jumlah yang ingin Anda bayarkan untuk likuiditas yang masuk. Semakin tinggi jumlah yang dibayarkan, semakin besar kapasitas saluran yang dibuka ke node Anda. Perkiraan kapasitas saluran muncul di bawah ini: ini adalah perkiraan, karena jumlah akhir akan bergantung pada penawaran terbaik yang ditemukan oleh Magma, yang terkadang lebih tinggi, terkadang lebih rendah.



![Image](assets/fr/053.webp)



Kemudian masukkan ID node Anda. Anda dapat menemukannya, misalnya, di menu `Node ID` pada aplikasi `Lightning Node` di Umbrel.



![Image](assets/fr/054.webp)



Setelah semua informasi telah diisi, klik tombol `Tinjau & buka order`.



![Image](assets/fr/055.webp)



Jika Anda belum membuat akun, Magma akan memberi Anda kunci sesi dan file cadangan. Simpan kedua hal ini di tempat yang aman, karena keduanya akan memungkinkan Anda untuk mengambil pesanan di kemudian hari, atau melacak statusnya jika terjadi masalah. Setelah Anda menyimpan file, klik tombol `Bayar dengan Kilat`.



![Image](assets/fr/056.webp)



Magma kemudian akan mengirimkan faktur Lightning untuk jumlah yang telah Anda pilih. Anda harus membayarnya. Jika Anda sudah memiliki saluran pada node Lightning Anda, Anda dapat membayar langsung dari node tersebut, atau menggunakan Lightning wallet eksternal lainnya.



![Image](assets/fr/057.webp)



Setelah pembayaran dilakukan, transaksi akan muncul sebagai transaksi yang sedang diproses di antarmuka Magma.



![Image](assets/fr/058.webp)



Setelah beberapa menit, permintaan akan diproses: saluran dengan sats akan dibuka ke node Lightning Anda. Setelah transaksi pembukaan dikonfirmasi di dalam blockchain, Anda akan memiliki akses ke likuiditas yang masuk.



![Image](assets/fr/059.webp)



Magma juga terintegrasi langsung ke dalam ThunderHub. Pada tab `Home`, gulir ke bawah ke bagian `Liquidity` dan klik `Buy Inbound Liquidity`. Anda tinggal memasukkan jumlah yang diinginkan dan mengonfirmasi. Anda tidak perlu membayar faktur apa pun secara manual, karena ThunderHub secara otomatis menangani pembayaran dari node Anda.



![Image](assets/fr/060.webp)



Jika Anda adalah seorang pedagang, jenis layanan ini sangat cocok, karena memungkinkan Anda untuk dengan cepat mendapatkan likuiditas masuk dalam jumlah besar dari node yang dapat diandalkan, menjamin bahwa pelanggan Anda dapat membayar Anda tanpa kesulitan. Di sisi lain, jika Anda seorang individu, atau jika Anda tidak ingin membayar likuiditas yang masuk, ada juga solusi gratis. Mari kita lihat.



### Likuiditas masuk koperasi



Jika Anda bukan seorang pedagang, tetapi masih membutuhkan likuiditas masuk (misalnya, untuk mem-priming node Anda pada saat start-up, sementara Anda menunggu beberapa pembayaran dilakukan), Anda tidak perlu membayarnya. Salah satu solusi yang saya sukai adalah bekerja sama dengan operator node lain yang juga membutuhkan likuiditas masuk, untuk membuka saluran Lightning satu sama lain. Dengan cara ini, membuka saluran memberi Anda likuiditas keluar, sementara pada saat yang sama memberi Anda likuiditas masuk, tanpa biaya (biaya modulo onchain untuk pembukaan).



Tentu saja, Anda dapat mengaturnya secara langsung dengan sesama pengguna bitcoin. Namun, ada sebuah platform yang didedikasikan untuk jenis pembukaan melingkar seperti ini: [Lightning Network +] (https://lightningnetwork.plus/). Prinsipnya adalah tidak membuka dua saluran antara orang yang sama, tetapi mengatur pembukaan melingkar yang melibatkan minimal tiga peserta, atau bahkan lebih.



Mari kita ambil contoh untuk memahami cara kerja Lightning Network +:




- Seorang operator node, bernama `A`, menerbitkan pengumuman yang menyatakan bahwa dia ingin membuka saluran 1 juta sats dengan dua orang lainnya;
- Iklan akan tetap aktif hingga ada peserta baru yang ditambahkan;
- Kemudian, dua operator, `B` dan `C`, bergabung dengan pengumuman simpul `A`. Segitiga sekarang telah selesai, dan fase pembukaan dapat dimulai.
- Node `A` membuka saluran ke node `B`;
- Node `B` membuka saluran ke node `C`;
- Node `C` membuka saluran ke node `A`.



Pada akhir operasi, setiap node memiliki 1 juta sats likuiditas keluar dan 1 juta sats likuiditas masuk. Skema ini dapat diperluas menjadi empat atau lima peserta.



Tentu saja, tidak ada mekanisme teknis untuk menjamin bahwa peserta akan benar-benar membuka saluran yang telah mereka buat. Itulah mengapa platform ini telah menyiapkan sistem reputasi, berdasarkan ulasan positif ketika operator memenuhi komitmen mereka. Dan dalam skenario terburuk, jika Anda menemukan seseorang yang tidak bekerja sama, Anda tidak akan kehilangan uang: Anda hanya akan kehilangan kesempatan untuk mendapatkan likuiditas yang masuk.



Solusi ini sangat cocok untuk profil "konsumen", karena memungkinkan Anda untuk mendapatkan likuiditas yang masuk secara gratis, sambil menghubungkan node Anda ke operator kecil lainnya. Di sisi lain, jika Anda adalah seorang pedagang, pendekatan ini umumnya tidak relevan: setiap sat likuiditas yang masuk membutuhkan pemblokiran sat likuiditas yang keluar, dan kebutuhan Anda yang besar akan likuiditas yang masuk akan melibatkan pengikatan modal yang terlalu besar.



Untuk menggunakan Lightning Network+, Anda memiliki dua pilihan: menggunakan aplikasi yang terintegrasi ke dalam Umbrel, atau menggunakan situs web klasik dan membuat akun dengan masuk dari node Anda. Saya merekomendasikan yang terakhir, karena aplikasi terintegrasi tidak menawarkan berbagai fungsi yang tersedia.



Buka situs web [Lightning Network +] (https://lightningnetwork.plus/) dan klik tombol `Login` di bagian kanan atas antarmuka.



![Image](assets/fr/061.webp)



Untuk mengautentikasi diri Anda, Anda perlu menandatangani pesan yang disediakan menggunakan kunci pribadi Lightning node Anda. Dengan ThunderHub, operasi ini sangat sederhana. Mulailah dengan menyalin pesan yang ditampilkan oleh LN+.



![Image](assets/fr/062.webp)



Pada ThunderHub, buka tab `Tools`, lalu klik tombol `Sign` di bagian `Messages`.



![Image](assets/fr/063.webp)



Rekatkan pesan autentikasi yang disediakan oleh LN+, lalu klik `Tanda tangani`.



![Image](assets/fr/064.webp)



ThunderHub kemudian menandatangani pesan ini menggunakan kunci privat node Anda. Salin tanda tangan generated.



![Image](assets/fr/065.webp)



Rekatkan tanda tangan ini ke dalam bidang yang sesuai di situs LN+, lalu klik `Masuk`.



![Image](assets/fr/066.webp)



Anda sekarang terhubung ke LN+ dengan node Lightning Anda. Proses ini memungkinkan LN+ untuk memverifikasi bahwa Anda adalah pemilik sah dari node yang Anda klaim di platform mereka.



![Image](assets/fr/067.webp)



Jika mau, Anda dapat mempersonalisasi profil LN+ Anda, misalnya dengan menambahkan biografi singkat.



Untuk berpartisipasi dalam pembukaan saluran sirkit pertama Anda, buka menu `Swaps` di bagian atas antarmuka. Di sini Anda akan menemukan semua swap yang tersedia saat ini, tergantung pada karakteristik node Anda.



![Image](assets/fr/068.webp)



Untuk bergabung dengan penawaran swap yang ada, cukup klik dan daftar. Namun, pada LN+, pembuat swap dapat memberlakukan persyaratan tertentu pada peserta, seperti jumlah saluran minimum atau kapasitas total node minimum. Oleh karena itu mungkin saja, terutama di masa-masa awal, hanya sedikit penawaran yang tersedia untuk node Anda. Dalam kasus saya, meskipun beberapa saluran sudah terbuka, tidak ada penawaran yang tersedia untuk node saya. Jadi saya membuat swap saya sendiri, dan Anda dapat melakukan hal yang sama jika Anda berada dalam situasi yang sama.



Klik `Mulai Liquidity Swap`, lalu masukkan parameter penawaran Anda:




- Pilih jumlah total peserta (3, 4 atau 5);
- Tunjukkan jumlah saluran yang akan dibuka (pastikan Anda memiliki setidaknya jumlah ini di onchain wallet Anda);
- Tentukan waktu buka saluran. Ini adalah periode di mana para peserta setuju untuk tidak menutupnya;
- Di sebelah kanan, Anda dapat menetapkan batasan untuk peserta: jumlah saluran minimum, kapasitas total minimum, dan jenis koneksi yang diterima.



Setelah semua parameter ditetapkan, klik tombol `Start Liquidity Swap`.



![Image](assets/fr/069.webp)



Penawaran swap Anda sekarang telah dibuat. Sekarang yang harus Anda lakukan adalah menunggu operator node lain mendaftar. Jika persyaratan Anda tidak terlalu ketat, ini tidak akan memakan waktu lama. Ingatlah untuk memantau status swap Anda dalam beberapa jam atau hari berikutnya.



![Image](assets/fr/070.webp)



Semua tempat pertukaran telah diambil: sekarang kita beralih ke tahap pembukaan saluran. Setiap peserta dapat melihat, dari antarmuka LN+-nya, pada node mana dia harus membuka saluran Lightning.



![Image](assets/fr/084.webp)



Di sisi Anda, buka saluran menggunakan Node ID yang disediakan oleh LN+ dan perhatikan jumlah yang ditunjukkan. Seperti yang telah kita lihat di bab-bab sebelumnya, Anda dapat melakukan ini baik melalui ThunderHub, dengan manajer node Lightning lain, atau langsung dari antarmuka aplikasi Lightning Node dasar.



![Image](assets/fr/085.webp)



Setelah pembukaan diluncurkan, Anda dapat melihatnya muncul di bagian saluran yang menunggu. Dalam kasus saya, ini adalah saluran dengan simpul `Plebian_fr`.



![Image](assets/fr/086.webp)



Anda kemudian dapat kembali ke LN+ untuk mengonfirmasi bahwa Anda telah memulai pembukaan saluran. Cukup klik tombol `Pembukaan Saluran Dimulai`.



![Image](assets/fr/087.webp)



Ketika semua peserta lain juga telah membuka saluran yang telah mereka ikuti, jangan lupa untuk memberikan ulasan positif kepada mereka.



![Image](assets/fr/088.webp)



Jika terjadi kesulitan atau penundaan, Anda dapat menghubungi rekan-rekan Anda secara langsung melalui bagian komentar di bagian bawah halaman.



![Image](assets/fr/089.webp)



Beberapa peserta mungkin ingin menyeimbangkan kembali saluran melingkar sejak awal, dengan melakukan pembayaran kepada diri mereka sendiri. Hal ini memastikan distribusi uang tunai yang seimbang di setiap saluran. Jika Anda berada dalam profil "konsumen", hal ini tidak penting, tetapi Anda bisa melakukan penyeimbangan ulang ini sendiri jika Anda mau, atau untuk sementara waktu menetapkan biaya saluran Anda ke nol untuk memudahkan rekan yang ingin melakukannya. Terkadang tidak ada yang mau melakukannya.



![Image](assets/fr/090.webp)




# Melepaskan potensi simpul Lightning Anda


<partId>8dcc24b1-6eb9-4a5f-a56b-8a823e5ac0fd</partId>



## Hubungkan wallet seluler melalui Tailscale


<chapterId>5fefb222-3f50-4f9d-a170-2ea628be4437</chapterId>



Selesai, Anda sekarang memiliki node Lightning yang terhubung dengan baik, dengan likuiditas yang masuk dan keluar. Jadi, Anda sudah siap untuk menggunakan node Lightning Anda dalam kehidupan nyata. Hingga saat ini, kami selalu menggunakan antarmuka langsung pada Umbrel, baik aplikasi `Lightning Node` atau antarmuka `ThunderHub`. Alat-alat ini berfungsi untuk mengirim dan menerima pembayaran, tetapi jelas tidak dioptimalkan untuk pembayaran Lightning sehari-hari. Antarmuka ini dirancang untuk digunakan pada komputer, tidak praktis pada ponsel cerdas, dan juga membutuhkan koneksi ke jaringan yang sama untuk berfungsi dengan baik (meskipun secara teknis memungkinkan untuk terhubung dari jarak jauh melalui Tor).



Dalam praktiknya, apa yang kita cari sebagai pengguna bitcoin adalah antarmuka Lightning wallet klasik pada ponsel pintar: kemampuan untuk memindai faktur melalui kode QR, dan antarmuka sederhana untuk membayar dan menguangkan sats. Inilah yang akan kita terapkan dalam bab ini dan bab berikutnya. Ide umumnya adalah memiliki aplikasi Lightning wallet seluler di ponsel cerdas Anda, yang dapat digunakan dari mana saja (bukan hanya jaringan lokal Anda) tetapi, di latar belakang, bergantung pada node Lightning Anda sendiri untuk mengirim dan menerima pembayaran.



### Apa saja solusi untuk menghubungkan pelanggan seluler?



Saat ini, ada beberapa cara untuk melakukan hal ini, baik dari segi aplikasi seluler dan jenis koneksi antara node Anda dan aplikasi ini. Tiga mode koneksi utama adalah:




- melalui ***Tor***;
- melalui VPN ***Tailscale***;
- melalui ***Nostr Wallet Connect***.



Beberapa tahun yang lalu, saya pernah terhubung melalui ***Tor***, tetapi saya segera berhenti: jumlah kegagalan dan penundaan komunikasi terlalu besar. Secara teori, cara ini berhasil, tetapi dalam praktiknya, pengalaman pengguna sangat buruk. Oleh karena itu, saya tidak menyarankan pendekatan ini.



Alternatif yang kemudian saya adopsi adalah menggunakan VPN ***Tailscale*** untuk memastikan komunikasi antara aplikasi seluler dan node. Solusi ini bekerja dengan sangat baik: bahkan pada jaringan seluler dengan kecepatan rendah, pembayaran saya selalu berjalan tanpa kesulitan. Ini adalah metode yang akan saya perkenalkan pertama kali dalam bab ini, dengan aplikasi Zeus.



Pada bab berikutnya, kita akan melihat solusi lain yang lebih baru, yang juga bekerja dengan sangat baik: ***Nostr Wallet Connect***. Kali ini, kami akan menggunakan aplikasi Alby Go untuk memberikan Anda sebuah alternatif, meskipun Zeus juga kompatibel dengan NWC jika Anda menginginkannya.



### Menginstalasi dan mengkonfigurasi Tailscale



Untuk metode pertama ini, kita membutuhkan Tailscale. Ini adalah solusi VPN berdasarkan WireGuard, yang memungkinkan Anda untuk menghubungkan perangkat yang tersebar di Internet dengan aman, sambil secara otomatis mengelola enkripsi, autentikasi, dan pelintasan NAT. Sederhananya, ini seolah-olah semua perangkat Anda terhubung ke LAN yang sama dengan router Anda, meskipun mereka bisa berada di mana saja di Internet.



Untuk menggunakannya, pertama-tama buatlah akun. Buka situs web Tailscale, lalu klik tombol `Mulai`.



![Image](assets/fr/071.webp)



Kemudian pilih penyedia identitas untuk akun Tailscale Anda. Secara pribadi, saya menggunakan salah satu akun GitHub saya untuk masuk.



![Image](assets/fr/072.webp)



Setelah Anda masuk, Anda akan ditanyai beberapa pertanyaan tentang penggunaan Anda. Jawablah dengan singkat untuk melanjutkan.



![Image](assets/fr/073.webp)



Tailscale kemudian menawarkan untuk menginstal klien pada mesin Anda. Untuk saat ini, bukan itu yang kami minati: langsung saja ke Umbrel dan instal aplikasi Tailscale dari App Store.



![Image](assets/fr/074.webp)



Ketika aplikasi terbuka, klik `Log In`, lalu ikuti proses autentikasi, menggunakan metode yang sama seperti saat Anda membuat akun.



![Image](assets/fr/075.webp)



Klik `Hubungkan` untuk mengonfirmasi. Umbrel Anda sekarang tersambung ke jaringan VPN Anda.



![Image](assets/fr/076.webp)



Kemudian unduh aplikasi Tailscale ke ponsel cerdas Anda dan masuk menggunakan akun yang sama. Harap diperhatikan: di Android, tidak mungkin menggunakan dua VPN secara bersamaan. Agar Tailscale bisa berfungsi, Anda harus menonaktifkan VPN lain yang sedang aktif. Terlebih lagi, setiap kali Anda ingin menggunakan node Lightning Anda melalui Zeus, Anda harus mengaktifkan VPN Tailscale, jika tidak, koneksi tidak akan terbentuk.



![Image](assets/fr/077.webp)



Pada situs Tailscale, setelah setidaknya dua klien terhubung, Anda dapat mengakses konsol administrasi dengan daftar semua perangkat Anda yang terhubung ke jaringan dan alamat IP Tailscale.



![Image](assets/fr/078.webp)



### Hubungkan Zeus



Instal aplikasi Zeus pada ponsel Anda. Ketika terbuka, pilih `Penyiapan Lanjutan`, lalu `Buat atau sambungkan wallet`.



![Image](assets/fr/079.webp)



Pada bagian `Antarmuka Wallet`, pilih `LND (REST)`. Kemudian masukkan alamat Tailscale dari Umbrel Anda, yang dapat Anda temukan dari dasbor Tailscale atau langsung di aplikasi Tailscale pada Umbrel. Untuk port, masukkan `8080`.



![Image](assets/fr/080.webp)



Zeus kemudian meminta Anda untuk memberikan `Macaroon`. Ini adalah otorisasi token yang memungkinkan Anda untuk secara tepat mendefinisikan hak yang diberikan kepada aplikasi (dalam hal ini Zeus) untuk berinteraksi dengan node Lightning Anda. Dimungkinkan untuk generate macaroon dari ThunderHub, di menu `Tools`, sub-menu `Bakery`, tetapi untuk tujuan ini, cara termudah adalah dengan mengambilnya langsung dari aplikasi `Lightning Node`.



Klik pada tiga titik kecil di kanan atas antarmuka, lalu pada `Connect Wallet`. Pilih `REST (Jaringan Lokal)`. Anda kemudian akan dapat menyalin macaroon dengan hak yang sesuai.



![Image](assets/fr/081.webp)



Rekatkan ke bidang yang sesuai di Zeus, lalu klik tombol `SELAMATKAN KONFIGURASI DOMPET`.



![Image](assets/fr/082.webp)



Anda sekarang dapat mengakses node Lightning Anda dari aplikasi Zeus. Ini berarti Anda dapat membuat faktur generate untuk menerima pembayaran secara langsung di node Lightning Anda dari ponsel cerdas Anda, dan juga membayar faktur Lightning di mana pun Anda berada.



![Image](assets/fr/083.webp)



Tip: Tailscale tidak terbatas untuk menggunakan node Lightning Anda dari jarak jauh. Ini memungkinkan Anda mengakses semua alat Umbrel Anda dari perangkat lunak lain, bahkan dari jarak jauh. Sebagai contoh, Anda dapat menggunakan alamat IP Tailscale dari Umbrel Anda untuk menghubungkan node Bitcoin Anda (melalui Electrs atau Fulcrum) ke Sparrow Wallet, tanpa melalui Tor. Sekali lagi, ini menghindari kelambatan yang melekat pada Tor. Cukup instal klien Tailscale pada komputer Anda dan hubungkan ke jaringan Anda.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

Di bab berikutnya, kita akan melihat cara lain yang sama efektifnya untuk menghubungkan klien seluler ke node Lightning Anda: Nostr Wallet Connect. Kita akan menggunakan aplikasi yang berbeda dari Zeus (walaupun Zeus juga kompatibel dengan NWC), yaitu Alby Go.



## Hubungkan wallet seluler melalui NWC


<chapterId>f5c97e43-e66e-4ba3-bcc9-fee1a04fc7f4</chapterId>



Jika Anda tidak yakin dengan koneksi Tailscale, atau jika mengelola VPN ganda tampaknya terlalu merepotkan, bab ini menyarankan cara lain menggunakan klien seluler jarak jauh untuk membayar dan menerima sats melalui simpul Lightning Anda: ***Nostr Wallet Connect***.



Untuk contoh ini, kita akan menggunakan aplikasi seluler Alby Go, yang didesain dengan sangat baik dan sangat mudah dipelajari. Meskipun demikian, Anda juga dapat menggunakan Zeus atau aplikasi seluler lain yang kompatibel dengan NWC. Anda akan menemukan daftar aplikasi yang kompatibel di [repositori GitHub `awesome-nwc`] (https://github.com/getAlby/awesome-nwc).



### Bagaimana cara kerja Nostr Wallet Connect?



Nostr Wallet Connect adalah protokol standar yang memungkinkan aplikasi atau situs web untuk memicu tindakan pada node Lightning jarak jauh, tanpa membuat koneksi jaringan langsung ke node tersebut (tidak ada API LND yang terekspos, tidak ada VPN, tidak ada layanan `.onion`...). NWC mendefinisikan bagaimana sebuah aplikasi merumuskan suatu maksud (misalnya `pay_intece`) dan menerima hasilnya.



Cara kerjanya cukup sederhana. Anda menginisialisasi sesi dengan memindai kode QR atau melalui deeplink `nostr+walletconnect:`. String ini berisi parameter sesi dan rahasia otorisasi. Kemudian, ketika aplikasi ingin membayar, aplikasi akan menserialisasikan permintaan, mengenkripsinya, dan menerbitkannya sebagai peristiwa pada relai Nostr. Node membaca peristiwa pada relai, mendekripsinya, memeriksa apakah penulis memiliki otorisasi untuk sesi ini, mengeksekusi pembayaran, kemudian mengembalikan respons terenkripsi (sukses dengan gambar awal, atau kesalahan). Relai hanya bertindak sebagai perantara transportasi: tidak dapat membaca konten, tetapi dapat mengamati waktu dan frekuensi permintaan.



Dibandingkan dengan koneksi melalui Tailscale atau Tor, keuntungan utama dari NWC adalah node Anda tidak dapat dijangkau secara langsung dari luar. Hal ini sangat menyederhanakan penggunaan seluler: node Anda tidak perlu menerima koneksi yang masuk, hanya perlu berkomunikasi dengan relay. Di sisi lain, Anda memperkenalkan ketergantungan fungsional pada relai Nostr: jika mereka tidak tersedia, pengalaman menurun. Selain itu, meskipun pesan dienkripsi, relai dapat mengamati tingkat metadata aktivitas tertentu.



Perbedaan dalam model keamanan juga penting. Dengan Tailscale atau Tor, Anda membuka akses langsung ke simpul Anda (melalui API dari LND) yang dilindungi oleh rahasia yang sangat sensitif. Ini sangat kuat, karena Anda dapat mengatur segalanya, tetapi juga merupakan permukaan serangan lapisan bawah. Dengan NWC, akses lebih aplikatif: Anda mendelegasikan sesi token yang hanya mengotorisasi tindakan tertentu.



### Pasang Alby Hub pada node Lightning Anda



Sebelumnya, ada aplikasi yang secara khusus didedikasikan untuk koneksi NWC di App Store Umbrel, tetapi sayangnya aplikasi ini sudah tidak tersedia lagi. Sekarang Anda harus menggunakan Alby Hub untuk membuat koneksi jenis ini. Untuk melakukan ini, mulailah dengan menginstal aplikasi Alby Hub langsung dari toko.



![Image](assets/fr/091.webp)



Saat membuka, lewati layar pengantar, lalu klik tombol `Mulai (LND)`. Penting untuk memeriksa apakah tertulis `LND`, bukan `LDK`, dalam tanda kurung. Jika `LND` muncul, ini berarti bahwa Alby Hub telah mendeteksi dengan benar node Lightning yang ada dan akan mengkonfigurasi dirinya sendiri sebagai antarmuka untuknya. Sebaliknya, jika `LDK` yang ditampilkan, ini menunjukkan bahwa Alby Hub belum mendeteksi node Anda dan akan membuat node baru, yang bukan merupakan tujuan di sini.



![Image](assets/fr/092.webp)



Anda kemudian akan diminta untuk membuat akun Alby. Untuk penggunaan yang terbatas pada NWC, hal ini tidak perlu dilakukan, tetapi Anda mungkin ingin melakukannya jika Anda ingin memanfaatkan layanan khusus Alby. Jika tidak, klik `Mungkin nanti` untuk melanjutkan.



![Image](assets/fr/093.webp)



Kemudian pilih kata sandi yang kuat dan unik. Ini akan melindungi akses ke Alby Hub pada node Anda. Ingatlah untuk menyimpannya di pengelola kata sandi Anda.



![Image](assets/fr/094.webp)



Ini membawa Anda ke antarmuka Alby Hub. Anda tidak perlu melalui seluruh proses konfigurasi, kecuali jika Anda ingin menggunakannya sebagai pengelola utama node Lightning Anda. Seperti yang kita lihat sebelumnya, Alby Hub sebenarnya dapat menggantikan penggunaan ThunderHub untuk administrasi node Anda. Jika Anda ingin mengetahui lebih lanjut tentang opsi Alby Hub, lihat tutorial khusus kami:



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Buka menu `Koneksi`.



![Image](assets/fr/095.webp)



Di sini Anda dapat melihat semua aplikasi yang dapat terhubung ke node Lightning Anda melalui NWC. Ini termasuk Zeus, yang sudah disebutkan di bab sebelumnya. Di sini, kita akan menggunakan Alby Go. Klik pada Alby Go, kemudian pada tombol `Hubungkan ke Alby Go` untuk memulai proses koneksi.



![Image](assets/fr/096.webp)



### Memasang dan menghubungkan Alby Go



Pada ponsel cerdas Anda, instal aplikasi Alby Go:




- [Google Play Store](https://play.google.com/store/apps/details?id=com.getalby.mobile);
- [Apple App Store](https://apps.apple.com/us/app/alby-go/id6471335774);
- [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq3jhml5fvklgnq9fxpete767txn9zfzqdkc0sxfptmnchfrexje7qqfxxmmd9enk2arpd338jtndda3xjmr9pzj5tk).



Di Alby Hub, konfigurasikan hak yang ingin Anda berikan pada aplikasi Alby Go pada node Lightning Anda. Anda dapat, misalnya, menetapkan batas pengeluaran per periode, tanggal kedaluwarsa untuk tautan NWC, atau memberikan kontrol penuh. Setelah Anda mengatur parameter, klik tombol `Next`.



![Image](assets/fr/097.webp)



Alby Hub kemudian generate kode QR untuk membuat koneksi NWC antara node Lightning Anda dan Alby Go.



![Image](assets/fr/098.webp)



Pada aplikasi Alby Go, saat pertama kali dibuka, klik `Hubungkan Wallet`, lalu pindai kode QR yang disediakan oleh Alby Hub.



![Image](assets/fr/099.webp)



Pilih nama untuk mengidentifikasi wallet ini. Anda sekarang memiliki akses jarak jauh ke node Lightning Anda melalui Alby Go. Anda dapat membuat faktur generate untuk menerima sats di node Anda, atau mengatur faktur Lightning secara langsung dengannya.



![Image](assets/fr/100.webp)



Sebagai contoh, saya mengirim 1543 sats dari antarmuka Alby Go.



![Image](assets/fr/101.webp)



Jika saya membuka antarmuka dasar node Lightning saya di Umbrel, saya dapat melihat bahwa pembayaran ini memang telah dilakukan oleh node saya.



![Image](assets/fr/102.webp)



Sekarang Anda tahu cara mudah menggunakan node Lightning Anda dari mana saja.



## Otonomi yang tahan lama pada Lightning


<chapterId>691a0942-b46d-482a-8fbc-fe19b3814992</chapterId>



Sekarang kita telah sampai pada akhir kursus ini. Anda sekarang memiliki dasar-dasar yang Anda butuhkan untuk menggunakan Lightning Network dengan cara yang berdaulat: Anda memahami peran nyata dari sebuah node, trade-off dari pendekatan yang berbeda, dan Anda telah menyiapkan instance LND di Umbrel dengan strategi pencadangan dan perlindungan yang konsisten. Anda juga telah membuka saluran pertama Anda, mempelajari cara mengelola likuiditas, untuk membuat pembayaran Anda dapat diandalkan setiap hari.



Dari sudut pandang operasional, node Anda sekarang harus memasuki ritme pemeliharaan. Hal utama adalah memantaunya (waktu aktif, sinkronisasi, status saluran, kegagalan pembayaran, dll.), Menerapkan pembaruan yang ditawarkan oleh Umbrel ketika versi stabil tersedia, dan secara berkala memeriksa apakah cadangan dan konfigurasi menara pengawas Anda masih aktif.



Dalam hal saluran, gunakan pendekatan pragmatis: pertahankan yang berguna bagi Anda, tutup saluran yang tidak aktif secara permanen atau terkait dengan rekan-rekan yang tidak stabil, dan secara bertahap alokasikan kembali modal Anda ke arah topologi yang lebih kuat.



**Salah satu jebakan yang paling umum pada tahap ini adalah mengalokasikan terlalu banyak modal ke node Lightning Anda. Ingatlah bahwa Lightning node Anda jauh lebih tidak aman daripada perangkat keras wallet, dan bahwa ketersediaan dana yang dikomitmenkan ke saluran Anda bergantung pada mekanisme cadangan yang tetap tidak sempurna. Oleh karena itu, sangat penting untuk menjaga jumlah yang masuk akal, yang dapat Anda tanggung jika terjadi masalah, dan selalu simpan sebagian besar sats Anda pada perangkat keras onchain wallet.



Mengenai alat, saya sarankan agar Anda tetap ingin tahu dan memperhatikan perkembangan baru. Dalam sesi pelatihan ini, kami menemukan beberapa di antaranya, baik untuk mengelola node Anda, konektivitasnya, atau penggunaan jarak jauh untuk melakukan pembayaran. Namun, Lightning adalah bidang yang sangat dinamis. Setiap tahun, alat baru dan relevan muncul, dan banyak aplikasi baru juga muncul di Umbrel. Dengan mengikuti perkembangan baru ini, Anda dapat menemukan solusi yang lebih kuat atau lebih praktis daripada yang disajikan dalam kursus ini.



Dari sisi pendidikan, jika Anda belum melakukannya, saya sangat menyarankan Anda untuk mengambil kursus teori LNP 201 dari Fanis Michalakis, yang didedikasikan untuk pengoperasian Lightning Network. Ini akan membantu Anda lebih memahami manipulasi yang dilakukan dalam kursus LNP202 ini, dan memberi Anda kepercayaan diri yang lebih besar dalam pengelolaan node Anda sehari-hari.



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Dengan nada yang berbeda, tetapi sama pentingnya dengan perjalanan bitcoin Anda, saya juga merekomendasikan kursus luar biasa dari Ludovic Lars tentang sejarah penciptaan Bitcoin.



https://planb.academy/courses/a51c7ceb-e079-4ac3-bf69-6700b985a082

Tetapi sebelum melanjutkan, Anda dapat menulis ulasan tentang kursus LNP202 ini dan, tentu saja, mengambil ijazah untuk mengonfirmasi bahwa Anda telah memahami semua isinya.



# Bagian akhir


<partId>683c998f-ba0a-4ffb-a7e8-4cd8369cb9b3</partId>



## Ulasan & Peringkat


<chapterId>aec048c7-7130-425d-8eca-9cd7f90c27f3</chapterId>



<isCourseReview>true</isCourseReview>

## Ujian akhir


<chapterId>3951ccbb-14a3-4322-b81b-8dd2a6da19cb</chapterId>



<isCourseExam>true</isCourseExam>

## Kesimpulan


<chapterId>30cd6309-5139-40d9-8927-92de0f76414a</chapterId>



<isCourseConclusion>true</isCourseConclusion>