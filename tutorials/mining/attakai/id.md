---
name: Attakaï

description: Transformasi S9 menjadi pemanas rumah
---

![cover](assets/cover.webp)

## Attakaï - penambangan rumahan kini mungkin dan dapat diakses!

Inisiatif "Attakaï" mengeksplorasi penambangan Bitcoin dengan memanfaatkan panas yang dihasilkan. Panduan ini menawarkan solusi agar penambang bisa digunakan sebagai radiator di rumah, sehingga memberi kenyamanan tambahan sekaligus penghematan energi. Bitcoin secara otomatis menyesuaikan tingkat kesulitan penambangan dan memberi hadiah kepada penambang atas kerja mereka. Namun, konsentrasi hashrate bisa menimbulkan risiko terhadap netralitas jaringan. "Attakaï" menyediakan panduan praktis untuk memodifikasi penambang dengan biaya terjangkau, sehingga kamu bisa menekan tagihan listrik dan tetap mendapatkan hadiah berupa sats tanpa KYC.

## Pendahuluan

"Attakaï", yang berarti "suhu ideal" dalam bahasa Jepang, adalah nama sebuah inisiatif yang bertujuan mengenalkan penambangan Bitcoin melalui pemanfaatan ulang panas yang dihasilkan, yang diluncurkan oleh @ajelexBTC dan @BlobOnChain bersama Découvre Bitcoin. Panduan retrofit ASIC ini akan menjadi dasar untuk mempelajari lebih jauh tentang penambangan, cara kerjanya, perkembangan sejarah terkini, serta ekonomi yang melandasinya.

### Mengapa menggunakan kembali panas dari ASIC?

Penting untuk memahami hubungan antara energi dan produksi panas dalam sistem listrik.

Untuk investasi 1 kW energi listrik, sebuah radiator listrik menghasilkan 1 kW panas, tidak lebih dan tidak kurang. Radiator modern juga tidak lebih efisien dibandingkan radiator tradisional. Keunggulan mereka terletak pada kemampuan mendistribusikan panas secara terus-menerus dan merata di dalam ruangan, sehingga memberi kenyamanan lebih dibandingkan radiator tradisional yang bekerja bergantian antara daya pemanasan tinggi dan tanpa pemanasan sama sekali, yang akhirnya menimbulkan fluktuasi suhu secara rutin dan rasa tidak nyaman.

Sebuah komputer, atau lebih luas lagi sebuah papan elektronik, sebenarnya tidak mengonsumsi energi untuk melakukan perhitungan; energi dibutuhkan agar arus listrik dapat mengalir melalui komponennya supaya perangkat bisa berfungsi. Konsumsi energi muncul dari resistansi listrik pada komponen, yang menimbulkan rugi daya dan menghasilkan panas, yang dikenal sebagai efek Joule.

Beberapa perusahaan kemudian muncul dengan ide untuk menggabungkan kebutuhan daya komputasi dan kebutuhan pemanasan melalui konsep radiator server. Gagasannya adalah mendistribusikan server perusahaan ke dalam unit-unit kecil yang bisa ditempatkan di rumah atau kantor. Namun, ide ini menghadapi sejumlah kendala. Kebutuhan server tidak selalu sejalan dengan kebutuhan pemanasan, dan perusahaan tidak bisa menggunakan kapasitas komputasi server mereka secara fleksibel. Selain itu, ada keterbatasan bandwidth yang bisa dimiliki oleh individu. Semua hambatan ini membuat perusahaan sulit menjadikan instalasi mahal semacam ini menguntungkan atau menyediakan layanan server online yang stabil tanpa dukungan pusat data yang mampu mengambil alih saat pemanasan tidak dibutuhkan.

> "Panas dari komputer kamu tidak terbuang kalau kamu memang perlu memanaskan rumah. Jika kamu menggunakan pemanas listrik di tempat tinggalmu, maka panas dari komputer kamu sama sekali tidak terbuang. Biayanya juga sama saja ketika kamu menghasilkan panas ini lewat komputer. Jika kamu memiliki sistem pemanasan yang lebih murah daripada listrik, maka pemborosannya hanya sebatas selisih biayanya. Jika sedang musim panas dan kamu memakai pendingin udara, maka pemborosannya menjadi dua kali lipat.
> Penambangan Bitcoin harus dilakukan di tempat yang lebih murah. Mungkin itu ada di tempat yang iklimnya dingin dan di mana pemanasan adalah listrik, di mana penambangan menjadi gratis."
> Satoshi Nakamoto - 8 Agustus 2010
Bitcoin dan sistem bukti kerja (proof of work) nya menonjol karena secara otomatis menyesuaikan kesulitan penambangan berdasarkan jumlah komputasi yang dilakukan oleh seluruh jaringan, jumlah ini disebut hashrate dan dinyatakan dalam hash per detik. Saat ini diperkirakan sebesar 280 Exahash per detik, atau 280 miliar miliar hash per detik. Hashrate ini mewakili pekerjaan dan oleh karena itu jumlah energi yang digunakan. Semakin tinggi hashrate, semakin tinggi pula kesulitan yang meningkat, dan sebaliknya. Dengan demikian, seorang penambang Bitcoin dapat diaktifkan atau dinonaktifkan kapan saja tanpa ada dampak pada jaringan, tidak seperti radiator/server yang perlu tetap stabil untuk menawarkan layanannya. Penambang diberi hadiah untuk pekerjaan yang dilakukan relatif terhadap pekerjaan orang lain, tidak peduli seberapa kecil partisipasi ini mungkin.

Ringkasnya, sebuah radiator listrik dan penambang Bitcoin keduanya menghasilkan 1 kW panas untuk 1 kW listrik yang dikonsumsi. Namun, penambang juga menerima bitcoin sebagai hadiah. Terlepas dari harga listrik, harga bitcoin, atau persaingan aktivitas penambangan di jaringan Bitcoin, secara ekonomis lebih menguntungkan untuk memanaskan dengan penambang daripada radiator listrik.


### Nilai Tambah untuk Bitcoin

Kami tidak akan membahas detail operasi penambangan di sini, karena sumber belajar sudah tersedia di akademi jika kamu membutuhkannya. Yang penting untuk dipahami adalah bagaimana penambangan berkontribusi pada desentralisasi Bitcoin. Berbagai teknologi yang sudah ada digabungkan secara cerdas untuk mewujudkan konsensus Nakamoto. Konsensus ini secara ekonomi memberi hadiah kepada aktor jujur atas partisipasi mereka dalam operasi jaringan Bitcoin, sekaligus mencegah aktor yang tidak jujur. Ini adalah salah satu poin kunci yang membuat jaringan ini bisa terus bertahan dalam jangka panjang.

Aktor jujur, yaitu mereka yang menambang sesuai aturan, semuanya saling bersaing untuk mendapatkan porsi terbesar dari hadiah dalam memproduksi blok baru. Insentif ekonomi ini secara alami mendorong terjadinya sentralisasi, karena perusahaan memilih untuk berspesialisasi dalam aktivitas yang menguntungkan ini dengan menekan biaya melalui ekonomi skala. Para pelaku industri ini berada pada posisi yang lebih menguntungkan untuk membeli dan merawat mesin, serta menegosiasikan tarif listrik dalam skala besar.

> "Pada awalnya, sebagian besar pengguna akan menjalankan node jaringan, tetapi seiring jaringan berkembang melebihi titik tertentu, itu akan semakin banyak ditinggalkan kepada spesialis dengan ladang server dari perangkat keras khusus. Sebuah ladang server hanya perlu menjalankan satu node di jaringan dan sisanya dari LAN terhubung dengan satu node itu." - Satoshi Nakamoto - 2 November 2008

Entitas tertentu menguasai persentase yang cukup besar dari total hashrate melalui ladang penambangan berskala besar. Kita bisa melihat contohnya pada gelombang dingin yang terjadi baru-baru ini di Amerika Serikat, ketika sebagian besar hashrate dimatikan untuk mengalihkan energi ke rumah tangga yang mengalami lonjakan kebutuhan listrik. Selama beberapa hari, para penambang secara ekonomi terdorong untuk mematikan ladang mereka, dan kondisi cuaca ekstrem ini pun terlihat jelas pada kurva hashrate Bitcoin.

Situasi seperti ini bisa menjadi problematik dan menimbulkan risiko serius terhadap netralitas jaringan. Seorang aktor yang menguasai lebih dari 51% hashrate akan lebih mudah menyensor transaksi jika mereka menginginkannya. Karena itu, penting untuk mendistribusikan hashrate ke sebanyak mungkin aktor, bukan terkonsentrasi pada entitas terpusat yang lebih mudah disita oleh pemerintah, misalnya.

**Jika penambang tersebar di ribuan, atau bahkan jutaan, rumah tangga di seluruh dunia, menjadi sangat rumit bagi sebuah negara untuk mengambil kendali atas mereka.**
Di pabrik, penambang tidak cocok digunakan sebagai radiator dalam perumahan, karena dua masalah utama: kebisingan berlebih dan kurangnya penyesuaian. Namun, masalah ini dapat dengan mudah diatasi melalui modifikasi sederhana yang dilakukan pada perangkat keras dan perangkat lunak, memungkinkan untuk penambang yang jauh lebih tenang yang dapat dikonfigurasi dan diotomatisasi seperti pemanas listrik modern.
**Attakaï adalah inisiatif pendidikan yang mengajarkan kita cara meretrofit Antminer S9 dengan cara yang paling hemat biaya.**

Ini adalah kesempatan yang sangat baik untuk belajar dengan praktik. Selain mengurangi tagihan listrik, kamu akan dihadiahi sats KYC gratis untuk partisipasimu.

## Bab 1: Panduan Membeli ASIC Bekas

Dalam bagian ini, kami akan membahas praktik terbaik untuk membeli Bitmain Antminer S9 bekas, mesin yang akan menjadi dasar dari tutorial retrofit radiator ini. Panduan ini juga berlaku untuk model ASIC lainnya, karena ini merupakan panduan umum untuk membeli perangkat keras penambangan bekas.

Antminer S9 adalah perangkat yang ditawarkan oleh Bitmain sejak Mei 2016. Mesin ini mengonsumsi daya listrik sebesar 1323 W dan menghasilkan 13,5 TH/s. Meskipun sering dianggap sudah tua, perangkat ini tetap menjadi pilihan yang sangat baik untuk mulai menambang. Karena diproduksi dalam jumlah besar, suku cadangnya mudah ditemukan dan tersedia melimpah di banyak wilayah di dunia. Biasanya, perangkat ini bisa diperoleh secara peer-to-peer di situs seperti eBay atau LeBonCoin, karena penjual profesional umumnya sudah tidak menawarkannya lagi akibat kurang kompetitif dibandingkan mesin yang lebih baru. Antminer S9 memang kurang efisien dibandingkan ASIC seperti Antminer S19 yang diperkenalkan sejak Maret 2020, tetapi justru hal ini membuatnya menjadi perangkat keras bekas yang lebih terjangkau dan lebih cocok untuk modifikasi yang akan kami lakukan.

Antminer S9 tersedia dalam beberapa varian (i, j) yang membawa sedikit modifikasi pada perangkat keras generasi pertamanya. Kami tidak menilai hal ini sebagai faktor yang perlu memengaruhi keputusan pembelian kamu, karena panduan ini dapat diterapkan pada semua varian tersebut.

Harga ASIC sangat bervariasi dan bergantung pada banyak faktor, seperti harga Bitcoin, tingkat kesulitan jaringan, efisiensi mesin, dan biaya listrik. Karena itu, cukup sulit untuk memberikan perkiraan harga yang benar-benar akurat untuk mesin bekas. Pada Februari 2023, harga yang umum dijumpai di Prancis berada di kisaran €100 hingga €200, meskipun angka ini dapat berubah dengan cepat.

![image](assets/fr/001.webp)

Antminer S9 terdiri dari bagian-bagian berikut:

- 3 hashboard di mana chip yang menghasilkan kekuatan hashing berada

![image](assets/fr/002.webp)

- Sebuah papan kontrol yang mencakup slot untuk kartu SD, port Ethernet, dan konektor untuk hashboard dan kipas. Ini adalah otak dari ASIC kamu.
  ![image](assets/fr/003.webp)

- 3 kabel data yang menghubungkan hashboard ke papan kontrol.

![image](assets/fr/004.webp)

- Pasokan daya yang beroperasi pada 220V dan dapat dicolokkan seperti peralatan rumah tangga biasa.

![image](assets/fr/005.webp)

- 2 kipas 120mm.

![image](assets/fr/006.webp)

- Sebuah kabel laki-laki C13.

![image](assets/fr/007.webp)
Saat membeli mesin bekas, penting untuk memastikan semua bagiannya lengkap dan berfungsi dengan baik. Saat proses transaksi, kamu sebaiknya meminta penjual untuk menyalakan mesin guna memverifikasi bahwa semuanya berjalan normal. Pastikan perangkat bisa menyala dengan benar, lalu periksa konektivitas internet dengan menghubungkan kabel Ethernet dan mengakses antarmuka Bitmain melalui browser web pada jaringan lokal yang sama. Kamu bisa menemukan alamat IP perangkat ini dengan masuk ke antarmuka router internet dan mencari daftar perangkat yang terhubung. Alamat IP tersebut biasanya memiliki format seperti berikut: 192.168.x.x
![image](assets/fr/008.webp)

Selain itu, pastikan kredensial default masih berfungsi (username: root, password: root). Jika kredensial default tersebut tidak bisa digunakan, kamu perlu melakukan reset pada mesin.

![image](assets/fr/009.webp)

Setelah terhubung, kamu seharusnya bisa melihat status setiap hashboard di dashboard. Jika penambang terhubung ke sebuah pool, kamu seharusnya melihat semua hashboard berfungsi dengan baik. Perlu dicatat bahwa penambang menghasilkan suara yang cukup bising, dan ini adalah hal yang normal. Pastikan juga semua kipas berfungsi dengan semestinya.

Selanjutnya, kamu bisa menghapus konfigurasi mining pool milik pemilik sebelumnya untuk menyiapkan pool kamu sendiri nanti. Jika diperlukan, kamu juga dapat memeriksa hashboard dengan membongkar mesin. Namun, langkah ini lebih rumit, memakan lebih banyak waktu, dan membutuhkan beberapa alat. Jika kamu ingin melanjutkan dengan pembongkaran tersebut, kamu bisa merujuk ke bagian selanjutnya dari tutorial ini yang menjelaskan caranya secara rinci. Penting juga untuk diketahui bahwa penambang cenderung mengumpulkan banyak debu dan membutuhkan perawatan rutin. Dengan membongkar mesin, kamu bisa melihat langsung akumulasi debu serta kualitas perawatan sebelumnya.

Setelah meninjau semua poin ini, kamu bisa membeli mesin dengan tingkat kepercayaan yang lebih tinggi. Jika masih ragu, hubungi komunitas, dan jika kamu membutuhkan peralatan untuk menyelesaikan tutorial ini, jangan ragu untuk mengirimkan pesan kepada kami.
Untuk merangkum panduan ini dalam satu kalimat: **"Jangan percaya, verifikasi."**

## Bab 2: Panduan Pembelian untuk Bagian Modifikasi

![image](assets/fr/010.webp)

### Bagaimana mengubah Antminer S9 kamu menjadi pemanas yang senyap dan terhubung?

Jika kamu memiliki Antminer S9, Anda mungkin tahu betapa keras dan besar ukurannya. Namun, dimungkinkan untuk mengubahnya menjadi pemanas yang senyap dan terhubung dengan mengikuti beberapa langkah sederhana. Dalam artikel ini, kami akan memperkenalkan peralatan yang diperlukan untuk melakukan modifikasi, sementara artikel selanjutnya akan menjelaskan secara detail langkah-langkah yang harus diikuti untuk melakukan perubahan ini.

### 1. Ganti kipas

Kipas asli dari Antminer S9 terlalu keras untuk digunakan sebagai pemanas. Solusinya adalah menggantinya dengan kipas yang lebih senyap. Tim kami telah menguji beberapa model dari merek Noctua dan memilih Noctua NF-A14 iPPC-2000 PWM sebagai kompromi terbaik. Pastikan untuk memilih versi 12V dari kipas. Kipas 140mm ini dapat menghasilkan hingga 1300W panas sambil mempertahankan tingkat kebisingan teoritis sebesar 31 dB. Untuk memasang kipas 140mm ini, kamu akan membutuhkan adaptor 140mm ke 120mm, yang dapat ditemukan di toko DécouvreBitcoin. Kami juga akan menambahkan gril pelindung 140mm.

![image](assets/fr/010.webp)
![image](assets/fr/011.webp)
![image](assets/fr/012.webp)
Kipas c juga cukup berisik dan perlu diganti. Kami merekomendasikan Noctua NF-A6x25 PWM. Perhatikan bahwa konektor dari kipas Noctua tidak sama dengan yang asli, jadi kamu akan memerlukan adaptor konektor untuk menghubungkannya. Dua seharusnya cukup. Lagi, pastikan untuk memilih versi 12V dari kipas tersebut.
![image](assets/fr/013.webp)
![image](assets/fr/014.webp)

### 2. Tambahkan jembatan WIFI/Ethernet

Alih-alih menggunakan kabel Ethernet, kamu bisa menghubungkan Antminer kamu ke WIFI dengan menambahkan jembatan WIFI/Ethernet. Kami memilih vonets vap11g-300 karena perangkat ini memudahkan kamu mengambil sinyal WIFI dari router internet dan meneruskannya ke Antminer melalui Ethernet tanpa membuat subnet tambahan. Jika kamu memiliki keahlian kelistrikan, kamu juga bisa langsung mengambil daya dari power supply Antminer tanpa perlu menambahkan charger USB. Untuk melakukan ini, kamu akan membutuhkan jack betina 5.5mm x 2.1mm.

![image](assets/fr/015.webp)
![image](assets/fr/016.webp)

### 3. Opsional: Tambahkan colokan pintar

Jika kamu ingin menyalakan atau mematikan Antminer kamu dari smartphone sekaligus memantau konsumsi dayanya, kamu bisa menambahkan colokan pintar. Kami telah menguji colokan ANTELA versi 16A yang kompatibel dengan aplikasi Smart Life. Colokan pintar ini memungkinkan kamu memeriksa konsumsi daya harian dan bulanan, serta terhubung langsung ke router internet kamu melalui WIFI.

![image](assets/fr/017.webp)

> Daftar peralatan dan tautan
>
> - 2X adaptor 3D ukuran 140mm ke 120mm
> - 2X NF-A14 iPPC-2000 PWM [tautan](https://www.amazon.fr/Noctua-nf-polarized-A14-industrialppc-PWM-2000/dp/B00KESSUDW/ref=sr_1_2?__mk_fr_FR=ÅMÅŽÕÑ&crid=JCNLC31F3ECM&keywords=NF-A14+iPPC-2000+PWM&qid=1676819936&sprefix=nf-a14+ippc-2000+pwm%2Caps%2C114&sr=8-2)
> - 2X gril kipas 140mm [tautan](https://www.amazon.fr/dp/B06XD4FTSQ?psc=1&ref=ppx_yo2ov_dt_b_product_details)
> - Noctua NF-A6x25 PWM [tautan](https://www.amazon.fr/Noctua-nf-a6-25-PWM-Ventilateur-Marron/dp/B00VXTANZ4/ref=sr_1_1_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=3T313ABZA5EDE&keywords=Noctua+NF-A6x25+PWM&qid=1676819329&sprefix=noctua+nf-a6x25+pwm%2Caps%2C71&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1&smid=A38F5RZ72I2JQ)
- Gula elektrik 2.5mm2 [link](https://www.amazon.fr/Legrand-LEG98433-Borne-raccordement-Nylbloc/dp/B00BBHXLYS/ref=sr_1_3?__mk_fr_FR=ÅMÅŽÕÑ&crid=25IRJD7A0YN2A&keywords=sucre%2Belectrique%2B2mm2&qid=1676820815&sprefix=sucre%2Belectrique%2B2mm2%2Caps%2C84&sr=8-3&th=1)
- Vonets VAP11G-300 https://www.amazon.fr/Vonets-VAP11G-300-Bridge-convertit-Ethernet/dp/B014SK2H6W/ref=sr_1_3_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=13Q33UHRKCKG5&keywords=vonet&qid=1676819146&s=electronics&sprefix=vonet%2Celectronics%2C98&sr=1-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1
- Opsional: colokan pintar ANTELA https://www.amazon.fr/dp/B09YYMVXJZ/ref=twister_B0B5X46QLW?_encoding=UTF8&psc=1

## Bab 3 - TUTORIAL: Bagaimana Cara Mengubah Miner Menjadi Pemanas?

![image](assets/fr/039.webp)

Jika kamu adalah seorang DIYer yang terampil dan ingin mengubah miner menjadi pemanas, tutorial ini memang dibuat untuk kamu. Kami ingin mengingatkan bahwa memodifikasi perangkat elektronik dapat menimbulkan risiko listrik dan kebakaran. Karena itu, sangat penting untuk mengambil semua tindakan pencegahan yang diperlukan agar terhindar dari kerusakan atau cedera.

Dari pabrik, miner sebenarnya tidak cocok digunakan sebagai radiator di rumah karena terlalu bising dan tidak bisa diatur. Namun, dengan beberapa modifikasi sederhana, masalah ini bisa diatasi.

> PERINGATAN: Sangat penting untuk telah menginstal Braiins OS+ pada miner kamu atau perangkat lunak lain yang dapat mengurangi kinerja mesin. Langkah ini sangat penting karena, untuk mengurangi kebisingan, kami akan memasang kipas yang kurang kuat yang dapat menghilangkan panas lebih sedikit.

### Bahan yang Diperlukan

- 2 buah adaptor 3D 140mm ke 120mm
- 2 kipas Noctua NF-A14 iPPC-2000 PWM
- 2 gril kipas 140mm
- 1 kipas Noctua NF-A6x25 PWM
- Gula elektrik 2.5mm2
- Vonets VAP11G-300
- Opsional: colokan pintar ANTELA

### Mengganti Kipas

Kami akan mulai dengan mengganti kipas catu daya.

> PERINGATAN: Pertama dan terutama, sebelum memulai, pastikan kamu telah mencabut miner kamu untuk menghindari risiko tersengat listrik.

![image](assets/fr/040.webp)

Kami akan mulai dengan mengganti kipas catu daya.

Pertama, lepaskan 6 sekrup di sisi casing yang menahannya tertutup. Setelah sekrup dilepas, buka casing dengan hati-hati untuk mengeluarkan penutup plastik yang melindungi komponen.

![image](assets/fr/041.webp)
![image](assets/fr/042.webp)
Selanjutnya, saatnya melepas kipas bawaan dengan hati-hati agar tidak merusak komponen lainnya. Untuk melakukannya, lepaskan sekrup yang menahan kipas lalu perlahan kupas lem putih yang mengelilingi konektor. Penting untuk bekerja dengan sangat hati-hati agar tidak merusak kabel atau konektor.

Setelah kipas bawaan dilepas, kamu akan menyadari bahwa konektor kipas Noctua yang baru tidak cocok dengan konektor kipas lama. Kipas baru memang memiliki 3 kabel, termasuk kabel kuning yang memungkinkan kontrol kecepatan. Namun, pada kasus spesifik ini, kabel tersebut tidak akan digunakan. Untuk menghubungkan kipas baru, sebenarnya disarankan menggunakan adaptor khusus, tetapi perlu dicatat bahwa adaptor ini terkadang sulit ditemukan.

Jika kamu tidak memiliki adaptor tersebut, kamu tetap bisa melanjutkan dengan menghubungkan kipas baru menggunakan klem kabel. Untuk melakukan ini, kamu perlu memotong kabel pada kipas lama dan kipas baru.

Pada kipas baru, gunakan pemotong dan potong dengan hati-hati bagian luar selubung utama sepanjang sekitar 1 cm, tanpa memotong selubung kabel di bawahnya.

Kemudian, dengan menarik selubung utama ke bawah, potong selubung kabel merah dan hitam dengan cara yang sama seperti sebelumnya. Setelah itu, potong kabel kuning hingga rata.

Pada kipas lama, proses memotong selubung utama lebih sulit dilakukan tanpa merusak selubung kabel merah dan hitam. Untuk mengatasinya, kami menggunakan jarum yang diselipkan di antara selubung utama dan kabel merah serta hitam.

Setelah kabel merah dan hitam terlihat, potong selubungnya dengan hati-hati agar tidak merusak kabel listrik di dalamnya.

Selanjutnya, sambungkan kabel menggunakan klem kabel, kabel hitam dengan hitam dan kabel merah dengan merah. Kamu juga bisa menambahkan isolasi listrik untuk keamanan tambahan.

Setelah sambungan selesai, saatnya memasang kipas Noctua yang baru menggunakan grille dan sekrup lama. Sekrup baru yang disertakan di dalam kotak akan digunakan kembali nanti. Pastikan kipas dipasang dengan orientasi yang benar. Kamu akan melihat tanda panah di salah satu sisi kipas yang menunjukkan arah aliran udara. Sangat penting untuk memasang kipas sehingga panah ini mengarah ke dalam casing. Terakhir, sambungkan kembali kipas tersebut.

> Opsional: Jika kamu ahli dalam kelistrikan, kamu dapat langsung menambahkan konektor jack perempuan 5.5mm ke output daya 12V, yang akan memungkinkan kamu untuk langsung memberi daya pada jembatan Wi-Fi Vonet. Namun, jika kamu tidak yakin dengan kemampuan listrik kamu, lebih baik menggunakan konektor USB dengan pengisi daya smartphone untuk menghindari risiko hubungan pendek atau kerusakan listrik.

Setelah sambungan dibuat, pastikan untuk meletakkan penutup plastik di atas casing plastik dan bukan di dalamnya.
Akhirnya, pasang kembali penutup casing dan kencangkan 6 sekrup di sisi-sisinya untuk menahan semuanya dengan aman di tempatnya. Dan sekarang, casing catu daya kamu telah dilengkapi dengan kipas baru.
### Penggantian 2 kipas utama

- Pertama, cabut kipas dan lepaskan sekrupnya.
   ![image](assets/fr/058.webp)

- Konektor kipas Noctua baru tidak cocok dengan yang asli, tapi jangan panik! Keluarkan cutter kamu dan potong dengan hati-hati tab plastik kecil agar konektor pas sempurna dengan penambang kamu.

![image](assets/fr/059.webp)
![image](assets/fr/060.webp)

- Saatnya memasang bagian 3D!
   Pasang di kedua sisi penambang menggunakan sekrup yang kamu lepas dari kipas. Kencangkan sampai kepala sekrup masuk ke dalam bagian 3D dan tertahan dengan aman di tempatnya. Berhati-hatilah untuk tidak mengencangkan terlalu kuat, karena kamu bisa merusak bagian tersebut dan salah satu sekrup mungkin menyentuh kapasitor! Kemudian potong dengan hati-hati tab plastik kecil agar konektor pas sempurna dengan penambang kamu.

![image](assets/fr/061.webp)

- Sekarang mari kita lanjutkan ke kipas.
   Pasang ke bagian 3D menggunakan sekrup yang disediakan dalam kotak. Perhatikan arah aliran udara, panah di sisi kipas akan menunjukkan arah yang harus diikuti. Mulai dari sisi port Ethernet ke sisi lain. Lihat foto di bawah ini.

![image](assets/fr/062.webp)
![image](assets/fr/063.webp)
![image](assets/fr/064.webp)

- Langkah terakhir: colokkan kipas dan pasang gril di atas dengan sekrup yang tidak digunakan dari kotak kipas. Kamu hanya memiliki 4, tapi 2 per gril di sudut berlawanan sudah cukup. Kamu juga bisa mencari sekrup serupa lainnya di toko perangkat keras jika diperlukan.

![image](assets/fr/065.webp)
'![image](assets/fr/066.webp)

Sambil menunggu bisa menawarkan casing yang lebih menarik untuk pemanas baru, kamu dapat mengikat casing dan catu daya bersama-sama dengan tali kabel elektrik.

![image](assets/fr/067.webp)

Dan untuk sentuhan akhir, sambungkan jembatan Vonet ke port Ethernet pada catu dayanya. Jika kamu belum melakukannya, kamu dapat mengikuti tutorial ini untuk mengatur jembatan kamu.

![image](assets/fr/068.webp)

Dan sekarang, selamat! kamu baru saja mengganti seluruh bagian mekanis penambangmu. Kamu sekarang seharusnya mendengar suara yang jauh lebih sedikit.

## Bab 4 - Modifikasi Perangkat Lunak - Mereset Antminer S9

**Seri artikel yang diusulkan oleh BlobOnChain & Ajelex - 15/02/2023**

### Reset melalui tombol "Reset"

Metode ini bisa diterapkan dalam waktu sekitar 10 menit setelah penambang dinyalakan.

Setelah penambang berjalan selama 2 menit, tekan tombol "Reset" selama 5 detik lalu lepaskan. Penambang akan kembali ke pengaturan pabrik dalam waktu sekitar 4 menit dan akan melakukan restart secara otomatis tanpa perlu dimatikan.

![image](assets/fr/018.webp)

Restore via web side

Masuk ke antarmuka pengguna penambang kamua, klik pada "Upgrade" >> "Perform a reset", kemudian klik "OK" di jendela pop-up.

### Sistem operasi asli
Untuk bagian ini, kita akan mengasumsikan bahwa mesin dalam kondisi berfungsi, sedang berjalan, dan sistem operasi aslinya sudah terinstal. Kita akan melihat secara singkat antarmuka dari sistem operasi bawaan yang ditawarkan oleh Bitmain.
Pertama, sambungkan ke mesin kamu melalui jaringan lokal kamu:

![image](assets/fr/019.webp)

Setelah berada di halaman login, kamu perlu login ke ASIC menggunakan kredensial default:

- username: root
- password: root

(Bagaimana cara mereset jika password default tidak berfungsi?)

Sistem operasi utama relatif dasar. Dengan 4 tab: Sistem, Konfigurasi Penambang, Status Penambang, Jaringan. Di tab Konfigurasi Penambang, kamu dapat mengatur hingga 3 kolam penambangan.

![image](assets/fr/020.webp)

Di tab Status Penambang, kamu dapat mengamati berbagai informasi tentang operasi langsung dari ASIC. Hashrate yang dinyatakan dalam GH/s, informasi lebih detail tentang kolam, serta detail tentang status setiap hashboard dan kecepatan kipas dalam rotasi/menit.

![image](assets/fr/021.webp)

### Braiins OS+

Sekarang, kita akan mempelajari perangkat lunak untuk ASIC Braiins OS+ (https://braiins.com/os/plus). Perangkat lunak ini dikembangkan oleh perusahaan Braiins (https://braiins.com/), yang merupakan perusahaan induk dari kolam penambangan Braiins Pool (https://braiins.com/pool). Kolam penambangan ini saat ini memiliki 4,39% dari hashrate global (https://mempool.space/fr/mining/pool/slushpool) pada saat penulisan ini. Perusahaan yang berbasis di Praha ini sebelumnya dikenal sebagai Slushpool dan merupakan kolam penambangan pertama yang dimulai pada November 2010. Saat ini, perusahaan, dengan berbagai aktivitasnya, menawarkan alat studi profitabilitas untuk penambangan (https://insights.braiins.com/en), solusi manajemen pertambangan bersama dengan aktivitas kolamnya, dan perangkat lunak optimasi untuk ASIC. Ini juga menawarkan penambangan menggunakan protokol Stratum V2 baru (https://braiins.com/bitcoin-mining-stack-upgrade).

Kita akan mempelajari lebih detail operasi perangkat Bitmain, yang saat ini adalah model yang hanya kompatibel:

- S19, S19 Pro, S19j, S19j Pro, T19,

- 17, S17 Pro, S17+, S17e, T17, T17+, T17e & S9 [i, j]

Perangkat lunak Braiins OS dapat dengan mudah diinstal pada semua mesin yang disebutkan di atas. Ini memungkinkan kontrol yang jauh lebih presisi atas sebuah mesin dengan menyediakan fitur overclocking dan underclocking. Perangkat lunak ini juga memungkinkan penyetelan frekuensi setiap chip secara lebih detail melalui fitur optimasi otomatis yang disebut autotuning. Karena setiap chip hashing sedikit berbeda akibat proses manufaktur, perangkat lunak ini menguji frekuensi optimal untuk masing-masing chip guna mencapai efisiensi maksimum dalam satuan W/THs. Perangkat lunak ini mengklaim mampu mencapai kinerja hingga 25% lebih tinggi dibandingkan konfigurasi asli. Berdasarkan pengukuran kami, angka tersebut memang memungkinkan untuk dicapai.

## Instalasi Braiins OS+

Ada beberapa cara untuk menginstal Braiins OS+ pada ASIC. Kamu bisa lihat ke panduan ini serta dokumentasi resmi dari Braiins dan tutorial video.
Menginstal Braiins OS+ langsung pada memori Antminer

Pelajari cara mudah menginstal Braiins OS+ langsung pada memori Antminer kamu menggunakan BOS toolbox, menggantikan sistem operasi asli, melalui langkah-langkah rinci di bawah ini. Jika Anda ingin menjaga OS asli secara paralel, kamu dapat menginstal Braiins OS+ pada kartu SD.
- Nyalakan Antminer Anda dan hubungkan ke kotak internet kamu.
- Unduh BOS toolbox Windows / Linux.
- Ekstrak file yang diunduh dan buka file bos-toolbox.bat, pilih bahasa, dan setelah beberapa saat Anda akan melihat jendela ini:
   ![image](assets/fr/022.webp)

- BOS toolbox akan memudahkan Anda untuk menemukan alamat IP Antminer kamu dan menginstal Braiins OS+. Jika kamu sudah mengetahui alamat IP mesin kamu, Anda dapat langsung ke langkah 8. Jika tidak, pergi ke tab pemindaian.

![image](assets/fr/023.webp)

- Biasanya, pada jaringan rumah, rentang alamat IP adalah antara 192.168.1.1 dan 192.168.1.255, jadi masukkan "192.168.1.0/24" di bidang rentang IP. Jika jaringan kamu berbeda, silakan ubah alamat-alamat ini. Kemudian klik "Mulai".

- Perhatian, jika Antminer memiliki kata sandi, deteksi tidak akan berfungsi. Jika itu masalahnya, solusi termudah adalah melakukan reset pabrik.

- Kamu seharusnya bisa melihat semua Antminer di jaringan, di sini alamat IP adalah 192.168.1.37.

![image](assets/fr/024.webp)

- Klik pada Kembali, kemudian pergi ke tab instalasi, masukkan alamat IP yang sebelumnya ditemukan di bidang Miner(s) dan "admin" (atau "root") di bidang Kata Sandi, yang merupakan kata sandi default, kemudian klik "Mulai".
   Jika instalasi tidak berhasil dengan "admin" atau "root" sebagai kata sandi, mungkin perlu melakukan reset pabrik dan coba lagi.

![image](assets/fr/025.webp)

- Setelah beberapa saat, Antminer kamu akan restart dan kamu akan dapat mengakses antarmuka Braiins OS+ di alamat IP yang bersangkutan, di sini 192.168.1.37, langsung di bilah alamat browser Anda. Nama pengguna default adalah "root" dan tidak ada kata sandi default.
   Menginstal Braiins OS+ pada kartu SD

![image](assets/fr/026.webp)

![image](assets/fr/027.webp)

Metode kedua menggunakan antarmuka asli Antminer kamu. Metode ini berfungsi untuk mesin dengan sistem operasi yang berasal dari sebelum tahun 2019.

### Antarmuka Antminer

- Unduh sistem operasi baru yang akan diinstal di sini.
- Seperti pada bagian sebelumnya, sambungkan ke mesin kamu melalui jaringan lokal.
- Pergi ke tab Sistem dan kemudian Upgrade.
- Muat file yang kamu unduh dan flash gambar tersebut.

![image](assets/fr/028.webp)

### Kartu Micro SD

Metode kedua memungkinkan Anda menggunakan kartu micro SD. Metode ini hanya berfungsi dengan mesin dengan sistem operasi yang berasal dari setelah tahun 2019.

- Unduh sistem operasi baru yang akan diinstal di sini.

- Flash gambar yang diunduh ke kartu micro SD. Untuk ini, kamu dapat menggunakan Etcher. Sekadar menyalin file ke kartu micro SD tidak akan berhasil.
- Jika kamu memiliki Antminer S9 dan variasinya (S9i, S9j), kamu perlu menyesuaikan jumper untuk memaksa ASIC kamu boot dari file di kartu micro SD daripada NAND. Kalau kamu memiliki model yang berbeda, kamu bisa melanjutkan ke bagian 4. Jumper terletak di papan kontrol di bagian atas ASIC, dekat dengan port Ethernet. Kamu perlu melepasnya dengan menggesernya ke belakang. Setelah posisi jumper dimodifikasi seperti yang ditunjukkan pada gambar di bawah BOOT FROM SD, kamu dapat memasukkan kembali papan kontrol dan menyambungkan kembali S9.
![image](assets/fr/029.webp)

![image](assets/fr/030.webp)

- Masukkan kartu micro SD ke dalam ASIC.
- Start ASIC. Jika versi instalasi otomatis digunakan, sistem operasi baru akan terinstal secara otomatis. Instalasi selesai ketika kedua LED menyala bersamaan. Kamu bisa merestart ASIC dan melepas kartu micro SD. Jika versi lain yang diunduh, kamu perlu membiarkan kartu micro SD tetap berada di dalam ASIC.

Untuk informasi lebih lanjut tentang instalasi, kamu dapat mengunjungi bagian ini di situs web Braiins.

## Antarmuka

Kamu perlu terhubung ke ASIC milikmu dengan cara yang serupa. Menggunakan alamat IP lokal perangkat kamu di jaringan melalui browser.

Kredensial default sama dengan sistem operasi asli.

- username: root
- password: root

Kamu kemudian akan disambut oleh Dashboard Brains OS+.

### Dashboard

![image](assets/fr/031.webp)

Di halaman pertama ini, kamu dapat mengamati kinerja mesin Anda secara real-time.

- Tiga grafik real-time yang menunjukkan suhu, hashrate, dan status keseluruhan mesin kamu.
- Di sebelah kanan, hashrate nyata, suhu chip rata-rata, efisiensi estimasi dalam W/THs, dan konsumsi daya.
- Di bawah, kecepatan kipas dalam persentase dari kecepatan maksimum dan jumlah rotasi per menit.

![image](assets/fr/032.webp)

- Lebih lanjut ke bawah, kamu akan menemukan tampilan detil dari setiap hashboard. Suhu rata-rata papan dan chip yang terkandung, tegangan, dan frekuensi.
- Detail tentang kolam penambangan aktif di Pools.
- Status autotuning di Tuner Status.
- Di sebelah kanan, detail tentang saham yang ditransmisikan ke kolam.

### Konfigurasi

![image](assets/fr/033.webp)

### Sistem

![image](assets/fr/034.webp)

### Aksi Cepat

![image](assets/fr/035.webp)

## Konfigurasi pool
Seseorang bisa membayangkan mining pool seperti sebuah koperasi pertanian. Para petani menggabungkan hasil produksi mereka untuk mengurangi variabilitas pasokan dan permintaan, sehingga mendapatkan pendapatan yang lebih stabil untuk operasional mereka. Mining pool bekerja dengan cara yang sama, dan “bahan mentah” yang digabungkan adalah hash. Pada praktiknya, menemukan satu hash yang valid memungkinkan pembuatan sebuah blok dan dengan demikian memenangkan coinbase atau hadiah, yang saat ini sebesar 3.125 BTC ditambah biaya transaksi yang disertakan di dalam blok. Jika kamu menambang secara solo, kamu hanya akan menerima hadiah ketika berhasil menemukan sebuah blok. Dengan harus bersaing melawan semua penambang lain di dunia, peluangmu untuk memenangkan lotere besar ini sangat kecil, sementara kamu tetap harus menanggung biaya penggunaan penambang tanpa jaminan hasil.

Mining pool mengatasi masalah ini dengan menggabungkan daya komputasi dari banyak, bahkan ribuan, penambang dan membagikan hadiah berdasarkan persentase kontribusi masing-masing terhadap hashrate pool ketika sebuah blok ditemukan. Untuk memvisualisasikan peluang menambang sebuah blok secara solo, kamu bisa menggunakan alat ini. Dengan memasukkan data dari Antminer S9, kita bisa melihat bahwa peluang menemukan hash yang memungkinkan pembuatan blok adalah 1 banding 24.777.849 untuk setiap blok, atau 1 banding 172.068 per hari. Secara rata-rata, dengan asumsi hashrate dan tingkat kesulitan konstan, dibutuhkan sekitar 471 tahun untuk menemukan satu blok. Namun, karena segala sesuatu dalam Bitcoin bersifat probabilistik, terkadang ada juga penambang solo yang berhasil dan mendapatkan hadiah karena berani mengambil risiko ini, seperti pada kasus “Solo Bitcoin Miner Solves Block With Hash Rate of Just 10 TH/s, Beating Extremely Unlikely Odds” yang dilaporkan oleh Decrypt.

Kalau kamu suka berjudi, kamu bisa saja mencobanya, tetapi panduan ini tidak akan berfokus ke arah tersebut. Sebaliknya, kami akan berkonsentrasi pada mining pool yang paling sesuai dengan kebutuhan kita untuk membangun sistem pemanas.

Hal-hal yang perlu dipertimbangkan saat memilih mining pool antara lain adalah cara pembagian hadiah, yang bisa berbeda-beda, serta jumlah minimum sebelum hadiah bisa ditarik ke alamat kamu. Sebagai contoh, Braiins, yang menawarkan perangkat lunak yang kita bahas di sini, juga memiliki mining pool sendiri. Pool ini menggunakan sistem hadiah yang disebut “Score”, yang mendorong penambang untuk menambang dalam jangka waktu lama. Partisipasi mempertimbangkan faktor durasi aktivitas yang dinyatakan sebagai “scoring hashrate”. Dalam kasus kita, di mana sistem pemanas diharapkan bisa dinyalakan hanya beberapa menit saja, model hadiah ini kurang ideal. Kita lebih memilih sistem hadiah yang memberikan imbalan yang sama untuk setiap partisipasi.

Selain itu, jumlah penarikan minimum di Braiins Pool adalah 100.000 sats dan dilakukan secara on-chain. Artinya, sebagian sats akan terpotong biaya transaksi, dan sebagian hadiah bisa tertahan jika kamu tidak menambang cukup lama selama musim dingin.

Model hadiah yang menurut kami lebih menarik adalah PPS, singkatan dari “pay per share”. Dengan model ini, penambang menerima hadiah untuk setiap share yang valid. Ada juga varian lain, yaitu FPPS (Full Pay Per Share), yang tidak hanya membagikan hadiah coinbase tetapi juga biaya transaksi yang masuk ke dalam blok. Mining pool yang kami rekomendasikan untuk menggabungkan penambangan dan pemanasan adalah Linecoin Pool dengan model FPPS dan Nicehash dengan model PPS.

- Nicehash: Keuntungan dari Nicehash adalah penarikan dapat dilakukan menggunakan Lightning dengan biaya minimal. Selain itu, jumlah penarikan minimum adalah 2000 sats. Kerugiannya adalah Nicehash menggunakan hashrate-nya untuk blockchain yang paling menguntungkan, tanpa benar-benar memberikan kontrol kepada pengguna, jadi mungkin tidak necessarily berpartisipasi dalam hashrate Bitcoin.
- Linecoin: Keunggulan Linecoin terletak pada jumlah fitur yang ditawarkan, seperti dashboard yang detail, kemampuan untuk melakukan penarikan dengan Paynym (BIP 47) untuk perlindungan privasi yang lebih baik, dan integrasi bot Telegram serta otomatisasi yang dapat dikonfigurasi langsung di aplikasi seluler. Pool ini hanya menambang blok Bitcoin, tetapi jumlah minimum untuk penarikan tetap tinggi pada 100.000 sats. Kami akan mengulas antarmuka salah satu pool ini lebih detail dalam artikel mendatang.
Untuk mengonfigurasi pool di Braiins OS+, Anda perlu membuat akun di salah satu pool pilihan kamu. Di sini kami akan mengambil contoh Linecoin:

![image](assets/fr/036.webp)

Setelah akun kamu dibuat, klik pada Connect To Pool

Kemudian salin alamat Stratum serta nama pengguna kamu:

![image](assets/fr/037.webp)

Kamu sekarang dapat kembali ke antarmuka Braiins OS+ untuk memasukkan kredensial ini. Untuk kata sandi, kamu dapat meninggalkan kolom tersebut kosong.

![image](assets/fr/038.webp)

### Overclocking dan Underclocking

Overclocking dan autotuning keduanya melibatkan penyesuaian frekuensi pada kartu hashing untuk meningkatkan kinerja ASIC. Perbedaannya terletak pada kompleksitas pengaturan frekuensi ini.

**Overclocking** adalah penyesuaian sederhana yang melibatkan peningkatan frekuensi pada kartu hashing untuk meningkatkan hash rate mesin. Underclocking, di sisi lain, melibatkan penurunan frekuensi jam dari sirkuit terintegrasi di bawah frekuensi nominalnya. Dengan mengurangi frekuensi jam ASIC melalui underclocking, panas yang dihasilkan oleh perangkat keras juga berkurang. Ini memungkinkan penurunan kecepatan kipas yang diperlukan untuk mendinginkan ASIC, karena mereka tidak harus bekerja keras untuk menjaga suhu yang sesuai. Dengan mengurangi kecepatan kipas, kebisingan yang dihasilkan oleh ASIC juga berkurang. Ini bisa sangat berguna bagi pengguna yang menggunakan ASIC di rumah dan ingin meminimalkan gangguan kebisingan yang disebabkan oleh perangkat keras penambangan.

Penting untuk dicatat bahwa underclocking dapat mengakibatkan penurunan kinerja ASIC, sehingga penting untuk menemukan keseimbangan yang baik antara kinerja dan kebisingan.

Braiins OS+ mendukung overclocking, underclocking ASIC, dan autotuning. Ini memungkinkan pengguna untuk menyesuaikan frekuensi jam perangkat keras mereka secara fleksibel untuk memaksimalkan kinerja atau menghemat energi sesuai dengan preferensi mereka.

### Autotuning

Sebelum 2018, penambang memiliki dua cara utama untuk mendapatkan keuntungan dari aktivitas mereka: menemukan listrik dengan harga yang wajar dan membeli perangkat keras yang lebih efisien. Namun, pada tahun 2018, muncul sebuah terobosan baru di bidang perangkat lunak dan firmware penambangan yang dikenal sebagai AsicBoost. Teknik ini memungkinkan penambang menurunkan biaya sekitar 13% dengan memodifikasi firmware yang berjalan di perangkat mereka.

Saat ini, ada kemajuan baru di sektor perangkat lunak dan firmware penambangan yang disebut autotuning, yang menawarkan keuntungan lebih besar dibandingkan AsicBoost. ASIC terdiri dari banyak chip komputer kecil yang melakukan hashing. Chip-chip ini terbuat dari silikon, elemen yang sama yang banyak digunakan dalam semikonduktor dan komponen mikroelektronik lainnya. Poin penting yang perlu dipahami di sini adalah bahwa tidak semua chip silikon identik, setiap chip bisa memiliki sedikit perbedaan pada karakteristik listriknya. Produsen perangkat keras memahami hal ini dan merilis spesifikasi kinerja mesin penambangan berdasarkan batas bawah toleransi mereka. Dengan kata lain, produsen mengetahui frekuensi optimal untuk chip rata-rata, lalu menerapkan frekuensi tersebut secara seragam ke semua chip di dalam mesin.

Pendekatan ini menetapkan batas atas pada hashrate yang bisa dicapai oleh sebuah mesin. Autotuning adalah proses di mana sebuah algoritma mengevaluasi frekuensi optimal untuk setiap chip hashing secara individual, alih-alih memperlakukan seluruh mesin sebagai satu kesatuan. Artinya, chip dengan kualitas lebih tinggi yang mampu menghasilkan lebih banyak hash per detik akan dijalankan pada frekuensi yang lebih tinggi, sementara chip dengan kualitas lebih rendah akan dijalankan pada frekuensi yang lebih rendah. Autotuning tingkat chip pada dasarnya adalah cara untuk mengoptimalkan kinerja sebuah ASIC melalui perangkat lunak dan firmware yang berjalan di atasnya.

Hasil akhirnya adalah hashrate yang lebih tinggi per watt listrik, yang berarti margin keuntungan yang lebih besar bagi penambang. Alasan mengapa mesin tidak dikirimkan langsung dengan jenis perangkat lunak ini adalah karena variasi antar mesin dianggap tidak diinginkan. Pelanggan ingin tahu secara pasti apa yang mereka dapatkan, sehingga menjual produk dengan kinerja yang tidak konsisten dan sulit diprediksi dari satu mesin ke mesin lain merupakan hal yang berisiko bagi produsen. Selain itu, autotuning tingkat chip membutuhkan sumber daya pengembangan yang besar karena implementasinya cukup kompleks. Produsen sendiri sudah menghabiskan banyak sumber daya untuk mengembangkan firmware bawaan mereka. Meski begitu, ada solusi perangkat lunak yang memungkinkan autotuning, seperti Braiins OS+, yang dapat meningkatkan kinerja ASIC hingga sekitar 20%.

> Panduan dibuat oleh DecouvreBitcoin, info lebih lanjut tentang MINAGE 201 - kredit untuk Jim dan Ajelex'


