---
name: Attakaï

description: mengubah S9 menjadi sistem pemanas rumah
---

![cover](assets/cover.webp)

# Attakai - membuat penambangan di rumah menjadi mungkin dan mudah diakses!

Inisiatif "Attakaï" mengeksplorasi penambangan Bitcoin menggunakan panas yang dihasilkan. Panduan ini menawarkan solusi untuk membuat penambang cocok digunakan sebagai radiator di rumah, memberikan lebih banyak kenyamanan dan penghematan energi. Bitcoin secara otomatis menyesuaikan kesulitan penambangan dan memberi hadiah kepada penambang atas kerja mereka. Namun, konsentrasi hashrate dapat menimbulkan risiko terhadap netralitas jaringan. "Attakaï" menyediakan panduan praktis untuk memodifikasi penambang secara ekonomis, memungkinkan peserta untuk mengurangi tagihan listrik mereka dan mendapatkan hadiah dengan sats tanpa KYC.

## Pendahuluan

"Attakaï," yang berarti "suhu ideal" dalam bahasa Jepang, adalah nama dari inisiatif yang bertujuan untuk menemukan penambangan bitcoin melalui penggunaan kembali panas yang diluncurkan oleh @ajelexBTC dan @BlobOnChain dengan Découvre Bitcoin. Panduan retrofit ASIC ini akan dijadikan dasar untuk mempelajari lebih lanjut tentang penambangan, operasinya, sejarah terkini, dan ekonomi yang mendasarinya.

### Mengapa menggunakan kembali panas dari ASIC?

Penting untuk memahami hubungan antara energi dan produksi panas dalam sistem listrik.

Untuk investasi 1 kW energi listrik, sebuah radiator listrik menghasilkan 1 kW panas, tidak lebih dan tidak kurang. Radiator baru tidak lebih efisien daripada radiator tradisional. Keuntungan mereka terletak pada kemampuan mereka untuk mendistribusikan panas secara kontinu dan merata di sebuah ruangan, memberikan lebih banyak kenyamanan dibandingkan dengan radiator tradisional yang bergantian antara daya pemanasan tinggi dan tidak ada pemanasan, sehingga menghasilkan variasi suhu reguler dan ketidaknyamanan.

Sebuah komputer, atau lebih luas sebuah papan elektronik, tidak mengonsumsi energi untuk melakukan perhitungan; ia hanya memerlukan energi untuk mengalir melalui komponennya agar dapat berfungsi. Konsumsi energi disebabkan oleh resistansi listrik dari komponen, yang menghasilkan kerugian dan dengan demikian menghasilkan panas, yang dikenal sebagai efek Joule.
Beberapa perusahaan telah datang dengan ide untuk menggabungkan kebutuhan akan daya komputasi dan kebutuhan pemanasan melalui radiator/server. Ide ini adalah mendistribusikan server perusahaan menjadi unit-unit kecil yang dapat ditempatkan di rumah atau kantor. Namun, ide ini menemui beberapa masalah. Kebutuhan akan server tidak terkait dengan kebutuhan akan pemanasan, dan perusahaan tidak dapat menggunakan kapasitas komputasi server mereka secara fleksibel. Ada juga batasan pada bandwidth yang dapat dimiliki individu. Semua kendala ini mencegah perusahaan dari membuat instalasi mahal ini menguntungkan atau menyediakan penawaran server online yang stabil tanpa pusat data yang mampu mengambil alih ketika pemanasan tidak diperlukan.

> "Panas dari komputer Anda tidak terbuang jika Anda perlu memanaskan rumah Anda. Jika Anda menggunakan pemanasan listrik di tempat Anda tinggal, maka panas dari komputer Anda tidak terbuang. Biayanya sama jika Anda menghasilkan panas ini dengan komputer Anda. Jika Anda memiliki sistem pemanasan yang lebih murah daripada listrik, maka pemborosan hanya pada perbedaan biaya. Jika musim panas dan Anda menggunakan pendingin udara, maka itu ganda.
> Penambangan Bitcoin harus dilakukan di tempat yang lebih murah. Mungkin itu akan di tempat yang iklimnya dingin dan di mana pemanasan adalah listrik, di mana penambangan menjadi gratis."
> Satoshi Nakamoto - 8 Agustus 2010
Bitcoin dan sistem bukti kerja (proof of work) nya menonjol karena secara otomatis menyesuaikan kesulitan penambangan berdasarkan jumlah komputasi yang dilakukan oleh seluruh jaringan, jumlah ini disebut hashrate dan dinyatakan dalam hash per detik. Saat ini diperkirakan sebesar 280 Exahash per detik, atau 280 miliar miliar hash per detik. Hashrate ini mewakili pekerjaan dan oleh karena itu jumlah energi yang digunakan. Semakin tinggi hashrate, semakin tinggi pula kesulitan yang meningkat, dan sebaliknya. Dengan demikian, seorang penambang Bitcoin dapat diaktifkan atau dinonaktifkan kapan saja tanpa ada dampak pada jaringan, tidak seperti radiator/server yang perlu tetap stabil untuk menawarkan layanannya. Penambang diberi hadiah untuk pekerjaan yang dilakukan relatif terhadap pekerjaan orang lain, tidak peduli seberapa kecil partisipasi ini mungkin.

Ringkasnya, sebuah radiator listrik dan penambang Bitcoin keduanya menghasilkan 1 kW panas untuk 1 kW listrik yang dikonsumsi. Namun, penambang juga menerima bitcoin sebagai hadiah. Terlepas dari harga listrik, harga bitcoin, atau persaingan aktivitas penambangan di jaringan Bitcoin, secara ekonomis lebih menguntungkan untuk memanaskan dengan penambang daripada radiator listrik.

![Presentasi Video](https://youtu.be/gKoh44UCSnE)

### Nilai Tambah untuk Bitcoin

Kami tidak akan membahas detail operasi penambangan di sini (sumber daya tersedia di akademi jika diperlukan). Yang penting untuk dipahami adalah bagaimana penambangan berkontribusi pada desentralisasi Bitcoin. Beberapa teknologi yang ada telah digabungkan secara cerdik untuk mewujudkan konsensus Nakamoto. Konsensus ini secara ekonomi memberi hadiah kepada aktor jujur atas partisipasi mereka dalam operasi jaringan Bitcoin, sambil mencegah aktor tidak jujur. Ini adalah salah satu poin kunci yang memungkinkan jaringan untuk eksis secara berkelanjutan.

Aktor jujur, mereka yang menambang sesuai dengan aturan, semuanya bersaing satu sama lain untuk memperoleh bagian terbesar dari hadiah untuk memproduksi blok baru. Insentif ekonomi ini secara alami mengarah pada bentuk sentralisasi karena perusahaan memilih untuk berspesialisasi dalam aktivitas menguntungkan ini dengan mengurangi biaya mereka melalui ekonomi skala. Aktor industri ini memiliki posisi yang menguntungkan untuk membeli dan memelihara mesin, serta menegosiasikan tarif listrik secara grosir.

> "Pada awalnya, sebagian besar pengguna akan menjalankan node jaringan, tetapi seiring jaringan berkembang melebihi titik tertentu, itu akan semakin banyak ditinggalkan kepada spesialis dengan ladang server dari perangkat keras khusus. Sebuah ladang server hanya perlu menjalankan satu node di jaringan dan sisanya dari LAN terhubung dengan satu node itu." - Satoshi Nakamoto - 2 November 2008

Entitas tertentu memegang persentase yang cukup besar dari total hashrate di ladang penambangan besar. Kita dapat mengamati gelombang dingin baru-baru ini di Amerika Serikat di mana sebagian besar hashrate dimatikan untuk mengalihkan energi ke rumah tangga yang membutuhkan listrik secara luar biasa. Selama beberapa hari, penambang secara ekonomi diberi insentif untuk mematikan ladang mereka, dan dengan demikian kita dapat melihat cuaca luar biasa ini pada kurva hashrate Bitcoin.

Masalah ini bisa menjadi problematik dan menimbulkan risiko signifikan terhadap netralitas jaringan. Seorang aktor yang memiliki lebih dari 51% hashrate bisa lebih mudah menyensor transaksi jika mereka menginginkannya. Itulah mengapa penting untuk mendistribusikan hashrate di antara banyak aktor daripada entitas terpusat yang bisa lebih mudah disita oleh pemerintah, misalnya.

**Jika penambang tersebar di ribuan, atau bahkan jutaan, rumah tangga di seluruh dunia, menjadi sangat rumit bagi sebuah negara untuk mengambil kendali atas mereka.**
Di pabrik, penambang tidak cocok digunakan sebagai radiator dalam perumahan, karena dua masalah utama: kebisingan berlebih dan kurangnya penyesuaian. Namun, masalah ini dapat dengan mudah diatasi melalui modifikasi sederhana yang dilakukan pada perangkat keras dan perangkat lunak, memungkinkan untuk penambang yang jauh lebih tenang yang dapat dikonfigurasi dan diotomatisasi seperti pemanas listrik modern.
**Attakaï adalah inisiatif pendidikan yang mengajarkan Anda cara meretrofit Antminer S9 dengan cara yang paling hemat biaya.**

Ini adalah kesempatan yang sangat baik untuk belajar dengan praktik. Selain mengurangi tagihan listrik Anda, Anda akan dihadiahi sats KYC gratis untuk partisipasi Anda.

## Bab 1: Panduan Membeli ASIC Bekas

Dalam bagian ini, kami akan membahas praktik terbaik untuk membeli Bitmain Antminer S9 bekas, mesin yang akan menjadi dasar tutorial retrofit radiator ini. Panduan ini juga berlaku untuk model ASIC lainnya karena ini adalah panduan umum untuk membeli perangkat keras penambangan bekas.

Antminer S9 adalah perangkat yang ditawarkan oleh Bitmain sejak Mei 2016. Ini mengonsumsi 1323W listrik dan menghasilkan 13.5 TH/s. Meskipun dianggap lama, ini tetap menjadi pilihan yang sangat baik untuk memulai penambangan. Karena diproduksi dalam jumlah besar, mudah untuk menemukan suku cadang yang berlimpah di banyak wilayah di dunia. Umumnya dapat diperoleh secara peer-to-peer di situs seperti Ebay atau LeBonCoin, karena penjual profesional tidak lagi menawarkannya karena kurang kompetitif dibandingkan dengan mesin yang lebih baru. Ini kurang efisien dibandingkan dengan ASIC seperti Antminer S19, yang diperkenalkan sejak Maret 2020, tetapi ini membuatnya menjadi perangkat keras bekas yang terjangkau dan lebih cocok untuk modifikasi yang akan kami lakukan.

Antminer S9 hadir dalam beberapa varian (i, j) yang membawa modifikasi kecil pada perangkat keras generasi pertama. Kami tidak percaya bahwa ini harus mempengaruhi keputusan pembelian Anda, dan panduan ini akan berfungsi untuk semua varian ini.

Harga ASIC bervariasi tergantung pada banyak faktor seperti harga bitcoin, kesulitan jaringan, efisiensi mesin, dan biaya listrik. Oleh karena itu, sulit untuk memberikan perkiraan yang akurat untuk membeli mesin bekas. Pada Februari 2023, harga yang diharapkan di Prancis umumnya berkisar antara €100 dan €200, tetapi harga ini dapat berubah dengan cepat.

![image](assets/guide-achat/1.webp)

Antminer S9 terdiri dari bagian-bagian berikut:

- 3 hashboard di mana chip yang menghasilkan kekuatan hashing berada

![image](assets/guide-achat/2.webp)

- Sebuah papan kontrol yang mencakup slot untuk kartu SD, port Ethernet, dan konektor untuk hashboard dan kipas. Ini adalah otak dari ASIC Anda.
  ![image](assets/guide-achat/3.webp)

- 3 kabel data yang menghubungkan hashboard ke papan kontrol.

![image](assets/guide-achat/4.webp)

- Pasokan daya yang beroperasi pada 220V dan dapat dicolokkan seperti peralatan rumah tangga biasa.

![image](assets/guide-achat/5.webp)

- 2 kipas 120mm.

![image](assets/guide-achat/6.webp)

- Sebuah kabel laki-laki C13.

![image](assets/guide-achat/7.webp)
Saat membeli mesin bekas, penting untuk memeriksa bahwa semua bagian termasuk dan berfungsi. Selama pertukaran, Anda harus meminta penjual untuk menyalakan mesin untuk memverifikasi fungsinya dengan benar. Penting untuk memeriksa bahwa perangkat menyala dengan benar, lalu periksa konektivitas internet dengan menghubungkan kabel Ethernet dan mengakses antarmuka koneksi Bitmain melalui browser web di jaringan lokal yang sama. Anda dapat menemukan alamat IP ini dengan terhubung ke antarmuka router internet Anda dan mencari perangkat yang terhubung. Alamat ini harus memiliki format berikut: 192.168.x.x
![image](assets/guide-achat/8.webp)

Juga, periksa bahwa kredensial default berfungsi (username: root, password: root). Jika kredensial default tidak berfungsi, Anda perlu melakukan reset mesin.

![image](assets/guide-achat/9.webp)

Setelah terhubung, Anda seharusnya dapat melihat status setiap hashboard di dashboard. Jika penambang terhubung ke sebuah pool, Anda seharusnya melihat semua hashboard berfungsi. Penting untuk dicatat bahwa penambang membuat banyak kebisingan, yang merupakan hal normal. Juga, pastikan kipas berfungsi dengan baik.

Anda kemudian dapat menghapus mining pool pemilik sebelumnya untuk menyiapkan milik Anda sendiri nanti. Jika diinginkan, Anda juga dapat memeriksa hashboard dengan membongkar mesin. Namun, langkah ini lebih kompleks dan membutuhkan lebih banyak waktu serta beberapa alat. Jika Anda ingin melanjutkan dengan pembongkaran ini, Anda dapat merujuk ke bagian selanjutnya dari tutorial ini yang menjelaskan cara melakukannya. Penting untuk dicatat bahwa penambang mengumpulkan banyak debu dan memerlukan perawatan rutin. Anda dapat mengamati akumulasi debu ini dan kualitas perawatan dengan membongkar mesin.
Setelah meninjau semua poin ini, Anda dapat membeli mesin Anda dengan tingkat kepercayaan yang tinggi. Jika ragu, hubungi komunitas, dan jika Anda membutuhkan peralatan untuk menyelesaikan tutorial ini, jangan ragu untuk mengirimkan kami pesan.
Untuk merangkum panduan ini dalam satu kalimat: **"Jangan percaya, verifikasi."**

## Bab 2: Panduan Pembelian untuk Bagian Modifikasi

![image](assets/piece/1.webp)

### Bagaimana mengubah Antminer S9 Anda menjadi pemanas yang senyap dan terhubung?

Jika Anda memiliki Antminer S9, Anda mungkin tahu betapa keras dan besar ukurannya. Namun, dimungkinkan untuk mengubahnya menjadi pemanas yang senyap dan terhubung dengan mengikuti beberapa langkah sederhana. Dalam artikel ini, kami akan memperkenalkan peralatan yang diperlukan untuk melakukan modifikasi, sementara artikel selanjutnya akan menjelaskan secara detail langkah-langkah yang harus diikuti untuk melakukan perubahan ini.

### 1. Ganti kipas

Kipas asli dari Antminer S9 terlalu keras untuk digunakan sebagai pemanas. Solusinya adalah menggantinya dengan kipas yang lebih senyap. Tim kami telah menguji beberapa model dari merek Noctua dan memilih Noctua NF-A14 iPPC-2000 PWM sebagai kompromi terbaik. Pastikan untuk memilih versi 12V dari kipas. Kipas 140mm ini dapat menghasilkan hingga 1300W panas sambil mempertahankan tingkat kebisingan teoritis sebesar 31 dB. Untuk memasang kipas 140mm ini, Anda akan membutuhkan adaptor 140mm ke 120mm, yang dapat Anda temukan di toko DécouvreBitcoin. Kami juga akan menambahkan gril pelindung 140mm.

![image](assets/piece/1.webp)
![image](assets/piece/2.webp)
![image](assets/piece/3.webp)
Kipas catu daya juga cukup berisik dan perlu diganti. Kami merekomendasikan Noctua NF-A6x25 PWM. Perhatikan bahwa konektor dari kipas Noctua tidak sama dengan yang asli, jadi Anda akan memerlukan adaptor konektor untuk menghubungkannya. Dua seharusnya cukup. Lagi, pastikan untuk memilih versi 12V dari kipas tersebut.
![image](assets/piece/4.webp)
![image](assets/piece/5.webp)

### 2. Tambahkan jembatan WIFI/Ethernet

Alih-alih menggunakan kabel Ethernet, Anda dapat menghubungkan Antminer Anda ke WIFI dengan menambahkan jembatan WIFI/Ethernet. Kami telah memilih vonets vap11g-300 karena dengan mudah memungkinkan Anda untuk mengambil sinyal WIFI dari kotak Internet Anda dan mentransmisikannya ke Antminer Anda melalui Ethernet tanpa menciptakan subnet. Jika Anda memiliki keahlian listrik, Anda dapat memberi daya langsung dengan catu daya Antminer tanpa perlu menambahkan pengisi daya USB. Untuk ini, Anda akan memerlukan jack betina 5.5mmx2.1mm.

![image](assets/piece/6.webp)
![image](assets/piece/7.webp)

### 3. Opsional: Tambahkan colokan pintar

Jika Anda ingin menyalakan/mematikan Antminer Anda dari smartphone dan memantau konsumsi dayanya, Anda dapat menambahkan colokan pintar. Kami telah menguji colokan ANTELA dalam versi 16A, kompatibel dengan aplikasi smartlife. Colokan pintar ini memungkinkan Anda untuk memeriksa konsumsi daya harian dan bulanan dan terhubung langsung ke kotak Internet Anda melalui WIFI.
![image](assets/piece/8.webp)

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

![image](assets/hardware/0.webp)

Jika Anda adalah seorang DIYer yang terampil dan ingin mengubah miner menjadi pemanas, tutorial ini adalah untuk Anda. Kami ingin memperingatkan Anda bahwa memodifikasi perangkat elektronik dapat menimbulkan risiko listrik dan kebakaran. Sangat penting untuk mengambil semua tindakan pencegahan yang diperlukan untuk menghindari kerusakan atau cedera.
Dari pabrik, miner sebenarnya tidak dapat digunakan sebagai radiator di rumah karena terlalu bising dan tidak dapat diatur. Namun, dimungkinkan untuk melakukan modifikasi sederhana untuk mengatasi masalah ini.

> PERINGATAN: Sangat penting untuk telah menginstal Braiins OS+ pada miner Anda atau perangkat lunak lain yang dapat mengurangi kinerja mesin Anda. Langkah ini sangat penting karena, untuk mengurangi kebisingan, kami akan memasang kipas yang kurang kuat yang dapat menghilangkan panas lebih sedikit.

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

> PERINGATAN: Pertama dan terutama, sebelum memulai, pastikan Anda telah mencabut miner Anda untuk menghindari risiko tersengat listrik.

![image](assets/hardware/1.webp)

Kami akan mulai dengan mengganti kipas catu daya.

Pertama, lepaskan 6 sekrup di sisi casing yang menahannya tertutup. Setelah sekrup dilepas, buka casing dengan hati-hati untuk mengeluarkan penutup plastik yang melindungi komponen.

![image](assets/hardware/2.webp)
![image](assets/hardware/3.webp)
Selanjutnya, saatnya untuk melepas kipas asli, dengan berhati-hati agar tidak merusak komponen lainnya. Untuk melakukan ini, lepaskan sekrup yang menahannya dan perlahan kupas lem putih yang mengelilingi konektor. Sangat penting untuk berproses dengan hati-hati untuk menghindari kerusakan pada kabel atau konektor.

Setelah kipas asli dilepas, Anda akan menyadari bahwa konektor kipas Noctua baru tidak cocok dengan kipas asli. Memang, kipas baru memiliki 3 kabel, termasuk kabel kuning yang memungkinkan kontrol kecepatan. Namun, kabel ini tidak akan digunakan dalam kasus spesifik ini. Untuk menghubungkan kipas baru, disarankan untuk menggunakan adaptor khusus. Namun, penting untuk dicatat bahwa adaptor ini terkadang sulit ditemukan.

Jika Anda tidak memiliki adaptor ini, Anda masih dapat melanjutkan untuk menghubungkan kipas baru menggunakan klem kabel. Untuk melakukan ini, Anda perlu memotong kabel kipas lama dan baru.

Pada kipas baru, gunakan pemotong dan dengan hati-hati potong kontur selubung utama sepanjang 1cm tanpa memotong selubung kabel di bawahnya.

Kemudian, dengan menarik selubung utama ke bawah, potong selubung kabel merah dan hitam dengan cara yang sama seperti sebelumnya. Dan potong kabel kuning rata.

Pada kipas lama, lebih sulit untuk memotong selubung utama tanpa merusak selubung kabel merah dan hitam. Untuk ini, kami menggunakan jarum yang kami selipkan antara selubung utama dan kabel merah dan hitam.

Setelah kabel merah dan hitam terpapar, potong selubungnya dengan hati-hati untuk menghindari kerusakan pada kabel listrik.

Kemudian, sambungkan kabel dengan klem kabel, kabel hitam dengan hitam dan kabel merah dengan merah. Anda juga dapat menambahkan isolasi listrik.

Setelah sambungan dibuat, saatnya untuk memasang kipas Noctua baru dengan grille dan sekrup lama, sekrup baru yang ada di kotak akan digunakan lagi nanti. Pastikan untuk meletakkannya dengan orientasi yang benar. Anda akan melihat sebuah panah di satu sisi kipas, menunjukkan arah aliran udara. Sangat penting untuk meletakkan kipas sehingga panah ini mengarah ke dalam casing. Kemudian, sambungkan kembali kipas.

> Opsional: Jika Anda terampil dalam listrik, Anda dapat langsung menambahkan konektor jack perempuan 5.5mm ke output daya 12V, yang akan memungkinkan Anda untuk langsung memberi daya pada jembatan Wi-Fi Vonet. Namun, jika Anda tidak yakin dengan kemampuan listrik Anda, lebih baik menggunakan konektor USB dengan pengisi daya smartphone untuk menghindari risiko hubungan pendek atau kerusakan listrik.

Setelah sambungan dibuat, pastikan untuk meletakkan penutup plastik di atas casing plastik dan bukan di dalamnya.
Akhirnya, pasang kembali penutup casing dan kencangkan 6 sekrup di sisi-sisinya untuk menahan semuanya dengan aman di tempatnya. Dan sekarang, casing catu daya Anda telah dilengkapi dengan kipas baru.
### Penggantian 2 kipas utama

1. Pertama, cabut kipas dan lepaskan sekrupnya.
   ![image](assets/hardware/19.webp)

2. Konektor kipas Noctua baru tidak cocok dengan yang asli, tapi jangan panik! Keluarkan cutter Anda dan potong dengan hati-hati tab plastik kecil agar konektor pas sempurna dengan penambang Anda.

![image](assets/hardware/20.webp)
![image](assets/hardware/21.webp)

3. Saatnya memasang bagian 3D!
   Pasang di kedua sisi penambang menggunakan sekrup yang Anda lepas dari kipas. Kencangkan sampai kepala sekrup masuk ke dalam bagian 3D dan tertahan dengan aman di tempatnya. Berhati-hatilah untuk tidak mengencangkan terlalu kuat, karena Anda bisa merusak bagian tersebut dan salah satu sekrup mungkin menyentuh kapasitor! Kemudian potong dengan hati-hati tab plastik kecil agar konektor pas sempurna dengan penambang Anda.

![image](assets/hardware/22.webp)

4. Sekarang mari kita lanjutkan ke kipas.
   Pasang ke bagian 3D menggunakan sekrup yang disediakan dalam kotak. Perhatikan arah aliran udara, panah di sisi kipas akan menunjukkan arah yang harus diikuti. Mulai dari sisi port Ethernet ke sisi lain. Lihat foto di bawah ini.

![image](assets/hardware/23.webp)
![image](assets/hardware/24.webp)
![image](assets/hardware/25.webp)

5. Langkah terakhir: colokkan kipas dan pasang gril di atas dengan sekrup yang tidak digunakan dari kotak kipas. Anda hanya memiliki 4, tapi 2 per gril di sudut berlawanan sudah cukup. Anda juga bisa mencari sekrup serupa lainnya di toko perangkat keras jika diperlukan.

![image](assets/hardware/26.webp)
'![image](assets/hardware/27.webp)

Sambil menunggu bisa menawarkan casing yang lebih menarik untuk pemanas baru Anda, Anda dapat mengikat casing dan catu daya bersama-sama dengan tali kabel elektrik.

![image](assets/hardware/28.webp)

Dan untuk sentuhan akhir, sambungkan jembatan Vonet ke port Ethernet pada catu dayanya. Jika Anda belum melakukannya, Anda dapat mengikuti tutorial ini untuk mengatur jembatan Anda.

![image](assets/hardware/29.webp)

Dan sekarang, selamat! Anda baru saja mengganti seluruh bagian mekanis penambang Anda. Anda sekarang seharusnya mendengar suara yang jauh lebih sedikit.

## Bab 4 - Modifikasi Perangkat Lunak - Mereset Antminer S9

**Seri artikel yang diusulkan oleh BlobOnChain & Ajelex - 15/02/2023**

### Reset melalui tombol "Reset"

Metode ini dapat diterapkan dalam 10 menit setelah memulai penambang.

Setelah menyalakan penambang selama 2 menit, tekan tombol "Reset" selama 5 detik, kemudian lepaskan. Penambang akan dikembalikan ke pengaturan pabrik dalam waktu 4 menit dan akan secara otomatis restart (tidak perlu mematikannya).

![image](assets/software/1.webp)

Restore via web side

Masuk ke antarmuka pengguna penambang Anda, klik pada "Upgrade" >> "Perform a reset", kemudian klik "OK" di jendela pop-up.

### Sistem operasi asli
Untuk bagian ini, kita akan mengasumsikan bahwa mesin sedang berfungsi, berjalan, dan sistem operasi aslinya telah terinstal. Kita akan melihat secara singkat antarmuka dari sistem operasi asli yang ditawarkan oleh Bitmain.
Pertama, sambungkan ke mesin Anda melalui jaringan lokal Anda:

![image](assets/software/2.webp)

Setelah berada di halaman login, Anda perlu login ke ASIC menggunakan kredensial default:

- username: root
- password: root

(Bagaimana cara mereset jika password default tidak berfungsi?)

Sistem operasi utama relatif dasar. Dengan 4 tab: Sistem, Konfigurasi Penambang, Status Penambang, Jaringan. Di tab Konfigurasi Penambang, Anda dapat mengonfigurasi hingga 3 kolam penambangan.

![image](assets/software/3.webp)

Di tab Status Penambang, Anda dapat mengamati berbagai informasi tentang operasi langsung dari ASIC. Hashrate yang dinyatakan dalam GH/s, informasi lebih detail tentang kolam, serta detail tentang status setiap hashboard dan kecepatan kipas dalam rotasi/menit.

![image](assets/software/4.webp)

### Braiins OS+

Sekarang, kita akan mempelajari perangkat lunak untuk ASIC Braiins OS+ (https://braiins.com/os/plus). Perangkat lunak ini dikembangkan oleh perusahaan Braiins (https://braiins.com/), yang merupakan perusahaan induk dari kolam penambangan Braiins Pool (https://braiins.com/pool). Kolam penambangan ini saat ini memiliki 4,39% dari hashrate global (https://mempool.space/fr/mining/pool/slushpool) pada saat penulisan ini. Perusahaan yang berbasis di Praha ini sebelumnya dikenal sebagai Slushpool dan merupakan kolam penambangan pertama yang dimulai pada November 2010. Saat ini, perusahaan, dengan berbagai aktivitasnya, menawarkan alat studi profitabilitas untuk penambangan (https://insights.braiins.com/en), solusi manajemen pertambangan bersama dengan aktivitas kolamnya, dan perangkat lunak optimasi untuk ASIC. Ini juga menawarkan penambangan menggunakan protokol Stratum V2 baru (https://braiins.com/bitcoin-mining-stack-upgrade).

Kita akan mempelajari lebih detail operasi perangkat Bitmain, yang saat ini adalah model yang hanya kompatibel:

- S19, S19 Pro, S19j, S19j Pro, T19,

- 17, S17 Pro, S17+, S17e, T17, T17+, T17e & S9 [i, j]

Perangkat lunak Braiins OS dapat dengan mudah diinstal pada semua mesin yang disebutkan di atas. Ini akan memungkinkan kontrol yang lebih presisi dari sebuah mesin dengan memungkinkan overclocking atau underclocking. Ini juga memungkinkan penyetelan halus frekuensi setiap chip melalui fitur optimasi otomatis yang disebut autotuning. Karena setiap chip hashing sedikit berbeda karena proses pembuatannya, perangkat lunak menguji frekuensi optimal untuk setiap chip untuk mencapai efisiensi maksimum (W/THs). Perangkat lunak mengklaim dapat mencapai kinerja yang bisa 25% lebih tinggi dari aslinya. Menurut pengukuran kami, dimungkinkan untuk mencapai angka-angka tersebut.

## Instalasi Braiins OS+

Ada beberapa cara untuk menginstal Braiins OS+ pada ASIC. Anda dapat merujuk ke panduan ini serta dokumentasi resmi dari Braiins dan tutorial video.
Menginstal Braiins OS+ langsung pada memori Antminer

Pelajari cara mudah menginstal Braiins OS+ langsung pada memori Antminer Anda menggunakan BOS toolbox, menggantikan sistem operasi asli, melalui langkah-langkah rinci di bawah ini. Jika Anda ingin menjaga OS asli secara paralel, Anda dapat menginstal Braiins OS+ pada kartu SD.
1. Nyalakan Antminer Anda dan hubungkan ke kotak internet Anda.
2. Unduh BOS toolbox Windows / Linux.
3. Ekstrak file yang diunduh dan buka file bos-toolbox.bat, pilih bahasa, dan setelah beberapa saat Anda akan melihat jendela ini:
   ![image](assets/software/5.webp)

4. BOS toolbox akan memudahkan Anda untuk menemukan alamat IP Antminer Anda dan menginstal Braiins OS+. Jika Anda sudah mengetahui alamat IP mesin Anda, Anda dapat langsung ke langkah 8. Jika tidak, pergi ke tab pemindaian.

![image](assets/software/6.webp)

5. Biasanya, pada jaringan rumah, rentang alamat IP adalah antara 192.168.1.1 dan 192.168.1.255, jadi masukkan "192.168.1.0/24" di bidang rentang IP. Jika jaringan Anda berbeda, silakan ubah alamat-alamat ini. Kemudian klik "Mulai".

6. Perhatian, jika Antminer memiliki kata sandi, deteksi tidak akan berfungsi. Jika itu masalahnya, solusi termudah adalah melakukan reset pabrik.

7. Anda seharusnya dapat melihat semua Antminer di jaringan Anda, di sini alamat IP adalah 192.168.1.37.

![image](assets/software/7.webp)

8. Klik pada Kembali, kemudian pergi ke tab instalasi, masukkan alamat IP yang sebelumnya ditemukan di bidang Miner(s) dan "admin" (atau "root") di bidang Kata Sandi, yang merupakan kata sandi default, kemudian klik "Mulai".
   Jika instalasi tidak berhasil dengan "admin" atau "root" sebagai kata sandi, mungkin perlu melakukan reset pabrik dan coba lagi.

![image](assets/software/8.webp)

9. Setelah beberapa saat, Antminer Anda akan restart dan Anda akan dapat mengakses antarmuka Braiins OS+ di alamat IP yang bersangkutan, di sini 192.168.1.37, langsung di bilah alamat browser Anda. Nama pengguna default adalah "root" dan tidak ada kata sandi default.
   Menginstal Braiins OS+ pada kartu SD

![image](assets/software/9.webp)

![image](assets/software/10.webp)

Metode kedua menggunakan antarmuka asli Antminer Anda. Metode ini berfungsi untuk mesin dengan sistem operasi yang berasal dari sebelum tahun 2019.

### Antarmuka Antminer

1. Unduh sistem operasi baru yang akan diinstal di sini.
2. Seperti pada bagian sebelumnya, sambungkan ke mesin Anda melalui jaringan lokal Anda.
3. Pergi ke tab Sistem dan kemudian Upgrade.
4. Muat file yang Anda unduh dan flash gambar tersebut.

![image](assets/software/11.webp)

### Kartu Micro SD

Metode kedua memungkinkan Anda menggunakan kartu micro SD. Metode ini hanya berfungsi dengan mesin dengan sistem operasi yang berasal dari setelah tahun 2019.

1. Unduh sistem operasi baru yang akan diinstal di sini.

2. Flash gambar yang diunduh ke kartu micro SD. Untuk ini, Anda dapat menggunakan Etcher. Sekadar menyalin file ke kartu micro SD tidak akan berhasil.
3. Jika Anda memiliki Antminer S9 dan variasinya (S9i, S9j), Anda perlu menyesuaikan jumper untuk memaksa ASIC Anda boot dari file di kartu micro SD daripada NAND. Jika Anda memiliki model yang berbeda, Anda dapat melanjutkan ke bagian 4. Jumper terletak di papan kontrol di bagian atas ASIC, dekat dengan port Ethernet. Anda perlu melepasnya dengan menggesernya ke belakang. Setelah posisi jumper dimodifikasi seperti yang ditunjukkan pada gambar di bawah BOOT FROM SD, Anda dapat memasukkan kembali papan kontrol dan menyambungkan kembali S9.
![image](assets/software/12.webp)

![image](assets/software/13.webp)

4. Masukkan kartu micro SD ke dalam ASIC.
5. Start ASIC. Jika versi instalasi otomatis digunakan, sistem operasi baru akan terinstal secara otomatis. Instalasi selesai ketika kedua LED menyala bersamaan. Anda dapat merestart ASIC dan melepas kartu micro SD. Jika versi lain yang diunduh, Anda perlu membiarkan kartu micro SD tetap berada di dalam ASIC.

Untuk informasi lebih lanjut tentang instalasi, Anda dapat mengunjungi bagian ini di situs web Braiins.

## Antarmuka

Anda perlu terhubung ke ASIC Anda dengan cara yang serupa. Menggunakan alamat IP lokal perangkat Anda di jaringan melalui browser.

Kredensial default sama dengan sistem operasi asli.

- username: root
- password: root

Anda kemudian akan disambut oleh Dashboard Brains OS+.

### Dashboard

![image](assets/software/14.webp)

Di halaman pertama ini, Anda dapat mengamati kinerja mesin Anda secara real-time.

- Tiga grafik real-time yang menunjukkan suhu, hashrate, dan status keseluruhan mesin Anda.
- Di sebelah kanan, hashrate nyata, suhu chip rata-rata, efisiensi estimasi dalam W/THs, dan konsumsi daya.
- Di bawah, kecepatan kipas dalam persentase dari kecepatan maksimum dan jumlah rotasi per menit.

![image](assets/software/15.webp)

- Lebih lanjut ke bawah, Anda akan menemukan tampilan detil dari setiap hashboard. Suhu rata-rata papan dan chip yang terkandung, tegangan, dan frekuensi.
- Detail tentang kolam penambangan aktif di Pools.
- Status autotuning di Tuner Status.
- Di sebelah kanan, detail tentang saham yang ditransmisikan ke kolam.

### Konfigurasi

![image](assets/software/16.webp)

### Sistem

![image](assets/software/17.webp)

### Aksi Cepat

![image](assets/software/18.webp)

Mengonfigurasi sebuah kolam
Seseorang dapat membayangkan kolam penambangan seperti sebuah koperasi pertanian. Para petani menggabungkan produksi mereka bersama-sama untuk mengurangi varians pasokan dan permintaan dan dengan demikian memperoleh pendapatan yang lebih stabil untuk operasi mereka. Kolam penambangan bekerja dengan cara yang sama, dan bahan mentah yang digabungkan bersama adalah hash. Faktanya, penemuan satu hash yang valid memungkinkan pembuatan sebuah blok dan dengan demikian memenangkan coinbase atau hadiah, saat ini 6.25 BTC ditambah biaya transaksi yang termasuk dalam blok. Jika Anda menambang sendirian, Anda hanya akan diberi hadiah ketika Anda menemukan sebuah blok. Berada dalam persaingan melawan semua penambang lain di planet ini, Anda akan memiliki peluang yang sangat kecil untuk memenangkan lotere besar ini dan Anda masih harus membayar biaya yang terkait dengan penggunaan penambang Anda tanpa jaminan keberhasilan. Kolam penambangan mengatasi masalah ini dengan menggabungkan kekuatan komputasi dari beberapa (ribuan) penambang dan membagikan hadiah mereka berdasarkan persentase partisipasi dalam hashrate kolam ketika sebuah blok ditemukan. Untuk memvisualisasikan peluang Anda menambang sebuah blok sendirian, Anda dapat menggunakan alat ini. Dengan memasukkan informasi dari Antminer S9, kita dapat melihat bahwa peluang menemukan hash yang memungkinkan pembuatan blok adalah 1 dalam 24,777,849 untuk setiap blok atau 1 dalam 172,068 per hari. Rata-rata (dengan hashrate dan kesulitan yang konstan), akan memakan waktu 471 tahun untuk menemukan sebuah blok.
Namun, karena segala sesuatu dalam Bitcoin adalah probabilitas, terkadang terjadi bahwa penambang solo diberi hadiah karena mengambil risiko ini: Solo Bitcoin Miner Solves Block With Hash Rate of Just 10 TH/s, Beating Extremely Unlikely Odds – Decrypt

Jika Anda suka berjudi, Anda dapat mencobanya, tetapi panduan kami tidak akan fokus ke arah itu. Sebaliknya, kami akan berkonsentrasi pada kolam penambangan yang paling sesuai dengan kebutuhan kami untuk membuat sistem pemanas.
Pertimbangan yang harus dimiliki ketika memilih kolam penambangan adalah operasi dari hadiah kolam, yang bisa berbeda, serta jumlah minimum sebelum dapat menarik hadiah ke alamat. Sebagai contoh, Braiins, yang menawarkan perangkat lunak yang kami bicarakan di sini, juga menawarkan sebuah kolam. Kolam ini memiliki sistem hadiah yang disebut "Score" yang mendorong penambang untuk menambang untuk jangka waktu yang lama. Partisipasi mencakup faktor waktu aktivitas yang dinyatakan dengan "scoring hashrate". Dalam kasus kami, di mana kami ingin sistem pemanas yang dapat dinyalakan hanya untuk beberapa menit, ini bukan sistem hadiah yang ideal. Kami lebih memilih sistem hadiah yang memberi kami hadiah yang sama untuk setiap partisipasi. Selain itu, jumlah penarikan minimum untuk Braiins Pool adalah 100,000 sats dan On-Chain. Jadi kami kehilangan beberapa sats dalam biaya transaksi dan sebagian hadiah kami dapat terkunci jika kami tidak menambang cukup selama musim dingin.

Model hadiah yang menarik bagi kami adalah PPS, yang berarti "bayar-per-bagian". Ini berarti bahwa penambang akan menerima hadiah untuk setiap bagian yang valid. Ada juga varian dari sistem ini, FPPS (Full Pay Per Share), yang tidak hanya membagi hadiah coinbase, tetapi juga biaya transaksi yang termasuk dalam blok. Kolam penambangan yang kami rekomendasikan untuk menghubungkan penambangan/pemanasan Anda adalah Linecoin Pool (FPPS) dan Nicehash (PPS).

- Nicehash: Keuntungan dari Nicehash adalah penarikan dapat dilakukan menggunakan Lightning dengan biaya minimal. Selain itu, jumlah penarikan minimum adalah 2000 sats. Kerugiannya adalah Nicehash menggunakan hashrate-nya untuk blockchain yang paling menguntungkan, tanpa benar-benar memberikan kontrol kepada pengguna, jadi mungkin tidak necessarily berpartisipasi dalam hashrate Bitcoin.
- Linecoin: Keunggulan Linecoin terletak pada jumlah fitur yang ditawarkan, seperti dashboard yang detail, kemampuan untuk melakukan penarikan dengan Paynym (BIP 47) untuk perlindungan privasi yang lebih baik, dan integrasi bot Telegram serta otomatisasi yang dapat dikonfigurasi langsung di aplikasi seluler. Pool ini hanya menambang blok Bitcoin, tetapi jumlah minimum untuk penarikan tetap tinggi pada 100.000 sats. Kami akan mengulas antarmuka salah satu pool ini lebih detail dalam artikel mendatang.
Untuk mengonfigurasi pool di Braiins OS+, Anda perlu membuat akun di salah satu pool pilihan Anda. Di sini kami akan mengambil contoh Linecoin:

![image](assets/software/19.webp)

Setelah akun Anda dibuat, klik pada Connect To Pool

Kemudian salin alamat Stratum serta nama pengguna Anda:

![image](assets/software/20.webp)

Anda sekarang dapat kembali ke antarmuka Braiins OS+ untuk memasukkan kredensial ini. Untuk kata sandi, Anda dapat meninggalkan kolom tersebut kosong.

![image](assets/software/21.webp)

### Overclocking dan Underclocking

Overclocking dan autotuning keduanya melibatkan penyesuaian frekuensi pada kartu hashing untuk meningkatkan kinerja ASIC. Perbedaannya terletak pada kompleksitas pengaturan frekuensi ini.

**Overclocking** adalah penyesuaian sederhana yang melibatkan peningkatan frekuensi pada kartu hashing untuk meningkatkan hash rate mesin. Underclocking, di sisi lain, melibatkan penurunan frekuensi jam dari sirkuit terintegrasi di bawah frekuensi nominalnya. Dengan mengurangi frekuensi jam ASIC melalui underclocking, panas yang dihasilkan oleh perangkat keras juga berkurang. Ini memungkinkan penurunan kecepatan kipas yang diperlukan untuk mendinginkan ASIC, karena mereka tidak harus bekerja keras untuk menjaga suhu yang sesuai. Dengan mengurangi kecepatan kipas, kebisingan yang dihasilkan oleh ASIC juga berkurang. Ini bisa sangat berguna bagi pengguna yang menggunakan ASIC di rumah dan ingin meminimalkan gangguan kebisingan yang disebabkan oleh perangkat keras penambangan.

Penting untuk dicatat bahwa underclocking dapat mengakibatkan penurunan kinerja ASIC, sehingga penting untuk menemukan keseimbangan yang baik antara kinerja dan kebisingan.

Braiins OS+ mendukung overclocking, underclocking ASIC, dan autotuning. Ini memungkinkan pengguna untuk menyesuaikan frekuensi jam perangkat keras mereka secara fleksibel untuk memaksimalkan kinerja atau menghemat energi sesuai dengan preferensi mereka.

### Autotuning

Sebelum 2018, penambang memiliki dua cara untuk mendapatkan keuntungan dalam aktivitas mereka: menemukan listrik dengan harga yang wajar dan membeli perangkat keras yang lebih efisien. Namun, pada tahun 2018, sebuah kemajuan baru ditemukan di bidang perangkat lunak dan firmware penambangan, yang disebut AsicBoost. Teknik ini memungkinkan penambang untuk mengurangi biaya mereka sekitar 13% dengan memodifikasi firmware yang berjalan pada perangkat mereka.
Hari ini, ada kemajuan baru dalam sektor perangkat lunak dan firmware penambangan yang disebut autotuning, yang menawarkan keuntungan yang lebih besar daripada AsicBoost. ASIC terdiri dari banyak chip komputer kecil yang melakukan hashing. Chip-chip ini terbuat dari silikon, elemen yang sama yang banyak digunakan dalam semikonduktor dan komponen mikroelektronik lainnya. Pemahaman kunci di sini adalah tidak semua chip silikon identik - setiap satu dapat sedikit bervariasi dalam sifat listriknya. Produsen perangkat keras mengetahui hal ini dan menerbitkan spesifikasi kinerja mesin penambangan mereka berdasarkan batas bawah toleransi mereka. Dengan kata lain, produsen mengetahui frekuensi yang paling baik untuk chip rata-rata dan mereka menggunakan frekuensi ini secara seragam untuk semua chip dalam mesin.
Ini menetapkan batas atas pada tingkat hash yang dapat dimiliki oleh sebuah mesin. Autotuning adalah proses di mana algoritma mengevaluasi frekuensi optimal untuk hashing chip demi chip, alih-alih memperlakukan seluruh mesin sebagai satu kesatuan. Ini berarti bahwa chip berkualitas lebih tinggi yang dapat melakukan lebih banyak hash per detik akan mendapatkan frekuensi yang lebih tinggi, dan chip berkualitas lebih rendah yang dapat melakukan relatif lebih sedikit hash akan mendapatkan frekuensi yang lebih rendah. Autotuning tingkat chip pada dasarnya adalah cara untuk mengoptimalkan kinerja sebuah ASIC melalui perangkat lunak dan firmware yang berjalan di atasnya.

Hasil akhirnya adalah tingkat hash yang lebih tinggi per watt listrik, yang berarti margin keuntungan yang lebih besar untuk penambang. Alasan mengapa mesin tidak didistribusikan dengan jenis perangkat lunak ini adalah karena variansi mesin tidak diinginkan, karena pelanggan ingin tahu persis apa yang mereka dapatkan, dan oleh karena itu, merupakan ide buruk bagi produsen untuk menjual produk yang tidak memiliki kinerja yang konsisten dan dapat diprediksi dari satu mesin ke mesin lainnya. Selain itu, autotuning tingkat chip memerlukan sumber daya pengembangan yang cukup besar, karena kompleks untuk diimplementasikan. Produsen sudah menghabiskan banyak sumber daya untuk mengembangkan firmware mereka sendiri. Ada solusi perangkat lunak yang memungkinkan untuk autotuning, seperti Braiins OS+. Selain meningkatkan kinerja ASIC hingga 20%.

> Panduan dibuat oleh DecouvreBitcoin, info lebih lanjut tentang MINAGE 201 - kredit untuk Jim dan Ajelex'