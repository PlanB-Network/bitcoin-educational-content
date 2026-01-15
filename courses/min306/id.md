---
name: Penguasaan Bitaxe Open Source Mining
goal: Kuasai ekosistem Bitaxe yang lengkap, mulai dari perakitan perangkat keras hingga kustomisasi tingkat lanjut dan pengoptimalan kinerja
objectives: 

  - Memahami filosofi perangkat keras open source Bitcoin mining
  - Membangun perangkat Bitaxe mining dari awal
  - Mengkonfigurasi dan mengoptimalkan perangkat lunak mining termasuk AxeOS dan Public Pool
  - Menerapkan pengoptimalan kinerja tingkat lanjut termasuk overclocking dan benchmarking

---

# Panduan Bitaxe Mining Anda


Selamat datang di kursus Bitaxe yang komprehensif, di mana Anda akan menguasai perangkat keras Bitcoin mining open source revolusioner yang mendemokratisasi akses ke teknologi mining. Kursus ini akan membawa Anda dari memahami dasar filosofis mining yang terdesentralisasi hingga kustomisasi perangkat keras tingkat lanjut dan teknik pengoptimalan kinerja.


Proyek Bitaxe mewakili pergeseran paradigma dalam Bitcoin mining, mematahkan monopoli produsen ASIC yang berpemilik dengan menyediakan desain, firmware, dan perangkat lunak yang sepenuhnya terbuka. Melalui bab-bab praktik ini, Anda akan mendapatkan keterampilan praktis dalam perakitan perangkat keras, konfigurasi perangkat lunak, desain PCB, dan pengoptimalan kinerja.


Tidak diperlukan pengalaman mining sebelumnya, meskipun pengetahuan elektronik dasar dan keakraban dengan GitHub akan sangat membantu. Kursus ini akan mengubah Anda dari seorang pengamat yang ingin tahu menjadi pembuat dan kontributor Bitaxe yang cakap.


+++


# Pendahuluan


<partId>6b3cd9f0-0063-40f0-a7bb-00a48f330d88</partId>


## Gambaran umum kursus


<chapterId>1fac9579-0e1c-48e3-9bc5-e7a2960018c8</chapterId>


Selamat datang di kursus MIN 306 _**Penguasaan Bitaxe Open Source Mining**_, sebuah perjalanan komprehensif ke dunia Bitaxe mining. Kursus ini dirancang untuk mereka yang ingin memahami, membangun, dan mengoptimalkan perangkat keras Bitaxe mining mereka sendiri sambil menjelajahi dasar-dasar filosofis dan teknis yang membuat proyek ini unik dalam ekosistem Bitcoin.


### Memahami Bitaxe


Bagian pertama meletakkan dasar-dasar penting: Anda akan menemukan asal-usul proyek Bitaxe, evolusinya, dan nilai-nilai desentralisasi dan transparansi yang mendefinisikannya. Anda akan mempelajari apa itu Bitaxe, perbedaannya dengan ASIC, dan di mana menemukan sumber daya komunitas untuk memperdalam pengetahuan Anda. Bagian ini memberikan konteks yang diperlukan untuk memahami mengapa Bitaxe mewakili titik balik dalam sejarah Bitcoin mining.


### Perangkat Lunak dan Operasi


Bagian kedua berfokus pada lingkungan perangkat lunak, dengan presentasi terperinci tentang *AxeOS*: sistem operasi sumber terbuka yang dirancang khusus untuk perangkat Bitaxe. Anda akan mempelajari fitur-fitur utamanya dan cara mengonfigurasi serta berinteraksi dengan perangkat Anda untuk memulai pengoperasian mining pertama Anda.


### Komunitas dan Kolaborasi


Bagian ketiga menyoroti aspek kolaboratif dari proyek ini. Anda akan menjelajahi filosofi sumber terbuka yang diterapkan pada pengembangan perangkat keras dan perangkat lunak Bitaxe. Melalui latihan praktis, Anda akan belajar cara berkontribusi langsung ke kode sumber, dan Anda juga akan menemukan _Public Pool_, sebuah platform komunitas untuk menggabungkan kekuatan komputasi. Anda juga akan belajar cara menginstalnya pada node Umbrel untuk integrasi lokal dan berdaulat.


### Perakitan dan Pemecahan Masalah Perangkat Keras


Pada bagian keempat, Anda akan mempelajari perangkat keras itu sendiri. Anda akan belajar cara mengidentifikasi alat yang diperlukan untuk merakit Bitaxe, memperbaiki masalah penyolderan, dan melakukan diagnostik lengkap menggunakan *AxeOS* dan alat USB. Bagian ini menekankan pada praktik langsung dan pemahaman mendalam tentang bagaimana komponen perangkat keras dan perangkat lunak berinteraksi.


### Kustomisasi Tingkat Lanjut


Bagian kelima didedikasikan untuk kustomisasi. Anda akan belajar cara memodifikasi PCB (papan sirkuit tercetak), membuat file pabrik, dan menggunakan _Bitaxe Web Flasher_. Bagian ini ditujukan bagi mereka yang ingin melampaui perakitan sederhana dan benar-benar mendesain versi khusus perangkat mereka sendiri.


### Optimalisasi Kinerja


Terakhir, bagian keenam mencakup teknik optimasi tingkat lanjut. Anda akan mempelajari cara melakukan benchmarking Bitaxe Anda untuk mengevaluasi kinerjanya dan cara meng-overclock-nya secara efisien. Keterampilan ini akan membantu Anda mendapatkan hasil maksimal dari perangkat keras Anda sambil menghormati keterbatasan fisiknya.


Seperti setiap kursus di Plan ₿ Academy, bagian akhir mencakup evaluasi yang dirancang untuk memperkuat pengetahuan Anda.


Selami petualangan teknis ini - masa depan Bitcoin mining ada di tangan Anda!


# Memahami Bitaxe

<partId>ba1cb4ea-6a77-54fd-916c-57285c8c2418</partId>


## Sejarah

<chapterId>73d928e5-72f0-5c17-a7a6-8b6ece7f9a30</chapterId>

:::video id=67d2529a-b7cb-4804-b02c-e56c12c9e66e:::

Proyek Bitaxe mewakili perubahan terobosan dalam pengembangan perangkat keras Bitcoin mining, yang membawa prinsip-prinsip sumber terbuka ke industri yang didominasi oleh solusi berpemilik. Seri edukasi ini mengeksplorasi sejarah komprehensif, inovasi teknis, dan evolusi Bitaxe yang digerakkan oleh komunitas, memberikan wawasan tentang bagaimana visi seorang insinyur bertransformasi menjadi ekosistem perangkat keras mining yang terdesentralisasi yang berkembang pesat. Dengan memeriksa asal-usul, tantangan, dan pencapaian proyek, kami memperoleh pemahaman yang berharga tentang kompleksitas teknis pengembangan ASIC dan kekuatan kolaborasi sumber terbuka di ruang Bitcoin.


### Kisah Asal Mula: Dari Penemuan Jalur Sutra hingga Visi Mining Surya


Skot, pendiri Bitaxe, memulai perjalanannya ke Bitcoin di sebuah pesta kampus di mana ia pertama kali mengetahui tentang Bitcoin melalui seseorang yang membeli barang di Silk Road. Paparan awal terhadap Bitcoin dengan harga sekitar $20 per koin memicu rasa ingin tahu yang kemudian berkembang menjadi proyek mining yang revolusioner. Landasan teknis untuk pekerjaannya di masa depan dibangun selama masa kuliahnya, di mana ia memiliki akses ke sumber daya FPGA yang luas di laboratorium. Bekerja bersama supervisornya, Skot mulai bereksperimen dengan bitstream FPGA open source untuk Bitcoin mining, awalnya dengan tujuan sederhana yaitu mining yang cukup untuk membeli pizza untuk kantor mereka.


Transisi dari eksperimen akademis ke pengembangan yang serius terjadi beberapa tahun kemudian ketika Skot mengerjakan gerbang bertenaga surya untuk pengumpulan data jarak jauh di Afrika. Pengalaman profesional dengan sistem tenaga surya ini memicu kesadaran bahwa ASIC Bitcoin mining, yang pada dasarnya merupakan perangkat DC tegangan rendah, akan berpasangan dengan sempurna dengan panel surya. Konsep ini tampak alami dan elegan. Namun, ketika Skot mulai meneliti solusi yang ada, ia menemukan kesenjangan yang signifikan di pasar: tidak seperti masa-masa awal Bitcoin mining ketika desain FPGA tersedia secara terbuka, kemunculan ASIC telah menggerakkan industri ke arah solusi yang sepenuhnya eksklusif dan bersumber tertutup.


Kurangnya perangkat keras open source mining menjadi penyebab frustrasi bagi Skot, terutama karena latar belakangnya dalam pengembangan perangkat lunak open source dan keyakinannya bahwa sifat open source Bitcoin harus diperluas ke infrastruktur mining. Keselarasan filosofis dengan prinsip-prinsip open source ini, dikombinasikan dengan tantangan teknis untuk merekayasa ulang desain ASIC yang dipatenkan, menyiapkan panggung untuk apa yang akan menjadi proyek Bitaxe. Visi awalnya sangat ambisius namun praktis: menciptakan penambang Bitcoin bertenaga surya yang dapat beroperasi secara independen tanpa memerlukan komputer terpisah untuk kontrol, sehingga cocok untuk digunakan di lokasi-lokasi terpencil di bawah panel surya.


### Tantangan Teknis dan Terobosan Rekayasa Terbalik


Pengembangan Bitaxe membutuhkan penanganan kendala teknis yang substansial, terutama berpusat pada kurangnya dokumentasi chip ASIC Bitmain. Pendekatan Skot terhadap tantangan ini menunjukkan tekad dan kecerdikan yang diperlukan untuk rekayasa balik yang sukses. Tanpa akses ke lembar data resmi atau spesifikasi teknis, ia terpaksa memeriksa chip di bawah mikroskop, mengukur jarak pin dengan kaliper, dan bahkan memindai chip untuk menentukan persyaratan footprint yang tepat. Proses yang melelahkan ini menghasilkan beberapa prototipe yang gagal, dengan dua iterasi pertama "penambang harian" gagal berfungsi dengan baik karena perhitungan footprint yang salah.


Terobosan datang dengan iterasi ketiga pada bulan Mei 2022, ketika Skot berhasil menciptakan desain dua chip yang berfungsi menggunakan chip BM1387 yang diambil dari unit Antminer S9. Pencapaian ini menandai lahirnya nama Bitaxe, yang terinspirasi dari konsep beliung untuk Bitcoin mining. Keberhasilan desain ini memvalidasi pendekatan reverse engineering dan menunjukkan bahwa pengembang independen dapat membuat perangkat keras mining yang fungsional tanpa dukungan pabrikan. Namun, tantangan teknis yang dihadapi tidak hanya pada antarmuka chip tetapi juga desain catu daya yang rumit, karena ASIC memerlukan pengaturan tegangan yang tepat pada arus tinggi, sering beroperasi pada tegangan serendah 0,6 volt sambil menarik arus listrik yang signifikan.


Pengembangan firmware menghadirkan lapisan kerumitan lain, karena proyek ini memerlukan pembuatan perangkat lunak mining yang dapat berjalan langsung pada mikrokontroler ESP32 daripada mengandalkan komputer eksternal yang menjalankan perangkat lunak seperti CGMiner. Pendekatan mandiri ini sangat penting untuk visi Skot tentang unit mining yang dapat digunakan secara mandiri. Kombinasi rekayasa balik perangkat keras dan pengembangan firmware tertanam menciptakan tantangan teknis yang komprehensif yang membutuhkan keahlian di berbagai disiplin ilmu, mulai dari teknik kelistrikan dan desain PCB hingga pemrograman tertanam dan protokol jaringan.


### Pembentukan Komunitas dan Kolaborasi Open Source


Transformasi Bitaxe dari proyek tunggal menjadi inisiatif komunitas yang berkembang merupakan salah satu aspek yang paling signifikan dari keberhasilannya. Awalnya, upaya Skot untuk menarik minat generate melalui forum Bitcoin dan media sosial hanya mendapat sedikit tanggapan dan terkadang skeptis. Terobosan datang ketika anggota komunitas seperti SirVapesAlot menyadari potensi open source mining dan mendirikan server Open Source Miners United (OSMU) Discord. Platform ini menyediakan lingkungan kolaboratif yang diperlukan agar proyek dapat berkembang, menarik kontributor dari berbagai latar belakang yang memiliki minat yang sama dalam mendemokratisasi teknologi Bitcoin mining.


Model pengembangan berbasis komunitas terbukti sangat efektif, dengan kontributor utama seperti Johnny9 dan Ben yang muncul untuk mengatasi tantangan teknis tertentu. Keahlian Johnny9 dalam pengembangan firmware memecahkan masalah implementasi perangkat lunak yang kritis, sementara keahlian pengembangan front-end Ben menciptakan dasbor AxeOS yang intuitif yang menyederhanakan konfigurasi dan pemantauan perangkat. Kontribusi tambahan Ben termasuk membangun kemampuan manufaktur dan menciptakan Public Pool, sebuah pool mining open source yang dioptimalkan untuk perangkat Bitaxe. Pendekatan kolaboratif ini menunjukkan bagaimana prinsip-prinsip open source dapat mempercepat pengembangan melebihi apa yang dapat dicapai oleh kontributor individu mana pun.


Komunitas OSMU juga memupuk lingkungan yang inklusif di mana para pendatang baru dapat belajar dan berkontribusi terlepas dari keahlian teknis awal mereka. Perjalanan Ben sendiri dari seorang pemula dalam menyolder hingga menjadi seorang produsen besar merupakan contoh dari pendekatan yang ramah terhadap pengembangan keterampilan. Komitmen komunitas terhadap pendidikan dan dukungan timbal balik menciptakan siklus yang baik di mana anggota yang berpengalaman membimbing pendatang baru, yang kemudian menjadi kontributor. Model ini terbukti penting untuk meningkatkan skala proyek di luar lingkup aslinya dan membangun ekosistem yang berkelanjutan untuk inovasi dan pertumbuhan yang berkelanjutan.


### Visi Desentralisasi Mining dan Dampak di Masa Depan


Visi jangka panjang Skot untuk Bitaxe jauh melampaui pembuatan perangkat mining lainnya: Bitaxe merupakan transformasi fundamental dari lanskap Bitcoin. Tujuan ambisius untuk memproduksi satu juta penambang satu terahash akan menciptakan kekuatan mining yang terdistribusi, yang mewakili langkah signifikan menuju desentralisasi mining. Visi ini menjawab kekhawatiran kritis tentang sentralisasi mining, di mana kumpulan besar dan operasi industri berpotensi tunduk pada tekanan pemerintah atau penangkapan peraturan. Dengan mendistribusikan daya mining ke penambang rumahan yang tak terhitung jumlahnya, jaringan menjadi lebih tangguh dan selaras dengan prinsip-prinsip desentralisasi Bitcoin.


Model ekonomi yang mendukung visi ini bergantung pada karakteristik unik mining rumahan, di mana biaya infrastruktur pada dasarnya nol dan penambang dapat beroperasi dengan pengawasan yang minimal. Tidak seperti operasi mining industri yang membutuhkan investasi modal besar-besaran dalam fasilitas, infrastruktur listrik, dan sistem pendingin, penambang rumahan cukup mencolokkan perangkat ke outlet listrik yang ada dan koneksi internet. Pendekatan ini secara teoritis dapat menghasilkan tingkat hash yang signifikan secara online tanpa hambatan masuk tradisional yang menjadi ciri operasi mining skala besar.


Keberhasilan proyek ini telah mulai mempengaruhi ekosistem Bitcoin mining yang lebih luas, dengan potensi untuk menginspirasi produsen lain untuk merangkul model pengembangan open source. Kelayakan finansial yang ditunjukkan oleh produsen Bitaxe membuktikan bahwa perangkat keras open source dapat sukses secara komersial dengan tetap menjaga transparansi dan keterlibatan komunitas. Karena proyek ini terus berkembang dengan integrasi chip baru, desain yang lebih baik, dan kemitraan manufaktur yang diperluas, proyek ini berfungsi sebagai bukti konsep bagaimana Bitcoin mining dapat kembali ke akarnya yang terdesentralisasi sembari merangkul teknologi ASIC yang modern. Tujuan utamanya lebih dari sekadar distribusi tingkat hash untuk memasukkan dampak pendidikan, membawa lebih banyak orang ke dalam kontak langsung dengan proses Bitcoin yang mendasar dari mining dan menumbuhkan pemahaman yang lebih dalam tentang model keamanan jaringan.


## Apa yang dimaksud dengan Bitaxe?

<chapterId>6a56af56-35ce-51af-999b-4bc7305e6464</chapterId>

:::video id=12b26c7a-74b1-4ea9-afc0-e3ef90cf5837:::

### Gambaran Umum dan Kemampuan Perangkat Keras


Ekosistem Bitaxe mencakup beberapa iterasi perangkat keras, masing-masing dirancang untuk mengoptimalkan berbagai aspek pengalaman mining dengan tetap mempertahankan filosofi inti dari aksesibilitas sumber terbuka. Perangkat ini tidak hanya berfungsi sebagai perangkat keras mining yang fungsional, tetapi juga sebagai alat edukasi yang memungkinkan pengguna untuk memahami hubungan yang rumit antara chip ASIC, mikrokontroler, dan proses Bitcoin mining. Memahami filosofi desain dan implementasi teknis Bitaxe memberikan wawasan berharga tentang bagaimana perangkat keras mining modern beroperasi di tingkat komponen dan sistem.



### Bitaxe Max, Implementasi Generasi Pertama


Bitaxe Max merupakan implementasi dasar dari konsep Bitaxe, memanfaatkan chip BM1397 ASIC yang awalnya dikembangkan oleh Bitmain untuk seri S17 mining mereka. Integrasi chip ini menunjukkan bagaimana perangkat keras sumber terbuka dapat menggunakan kembali teknologi ASIC yang ada untuk menciptakan solusi mining yang dapat diakses. Bitaxe Max memberikan perkiraan kecepatan hash antara 300 hingga 400 gigahash per detik, memposisikannya sebagai platform mining edukasi dan eksperimental daripada solusi skala komersial.


Integrasi chip BM1397 ke dalam Bitaxe Max memerlukan pertimbangan yang cermat terhadap manajemen daya, kontrol termal, dan protokol komunikasi. Desain papan mengakomodasi persyaratan khusus ASIC ini sekaligus menyediakan sirkuit pendukung yang diperlukan untuk operasi yang stabil. Implementasi ini menunjukkan bagaimana pengembangan perangkat keras sumber terbuka dapat memanfaatkan teknologi semikonduktor yang ada untuk menciptakan aplikasi baru dan peluang pembelajaran dalam komunitas mining.


### Bitaxe Ultra, Teknologi Chip Canggih


Bitaxe Ultra merupakan evolusi dari platform Bitaxe, yang menggabungkan chip BM1366 ASIC yang lebih canggih dari seri S19 Bitmain. Teknologi chip yang lebih baru ini membawa peningkatan efisiensi dan karakteristik kinerja pada platform Bitaxe dengan tetap mempertahankan filosofi desain dasar yang sama. Peningkatan ke chip BM1366 menunjukkan kemampuan beradaptasi platform dan komitmen komunitas untuk menggabungkan kemajuan teknologi ke dalam solusi mining open-source.


Transisi dari chip BM1397 ke BM1366 memerlukan modifikasi pada sistem pengiriman daya, manajemen termal, dan algoritme kontrol board. Perubahan ini menggambarkan sifat pengembangan perangkat keras yang berulang-ulang dan pentingnya menjaga kompatibilitas sambil meningkatkan kinerja. Implementasi Bitaxe Ultra memberi pengguna akses ke teknologi ASIC yang lebih baru sambil mempertahankan sifat edukatif dan eksperimental dari platform ini.


### Mikrokontroler dan Sistem Komunikasi


Di jantung setiap perangkat Bitaxe terdapat mikrokontroler ESP yang berfungsi sebagai antarmuka utama antara pengguna dan chip ASIC. Mikrokontroler ini menjalankan perangkat lunak khusus yang dikembangkan oleh komunitas Open Source Miners United (OSMU), yang memungkinkan kontrol yang tepat atas parameter operasi ASIC. Komunikasi antara mikrokontroler dan ASIC terjadi melalui jalur komunikasi serial yang dirancang dengan hati-hati yang diukir langsung ke papan sirkuit tercetak sebagai jejak yang terlihat.


Peran mikrokontroler lebih dari sekadar kontrol ASIC sederhana: mikrokontroler ini mencakup manajemen daya, pemantauan suhu, dan fungsi antarmuka pengguna. Melalui layar tampilan terintegrasi, pengguna dapat memantau parameter operasional yang penting seperti suhu, tingkat hash, alamat IP, dan statistik mining yang relevan lainnya. Sistem umpan balik waktu nyata ini memberikan wawasan berharga ke dalam kinerja perangkat dan membantu pengguna mengoptimalkan operasi mining mereka sambil mempelajari perilaku perangkat keras yang mendasarinya.


### Pertimbangan Manajemen Daya dan Keamanan


Platform Bitaxe beroperasi dengan persyaratan daya 5 volt yang ketat, sehingga pemilihan catu daya yang tepat sangat penting untuk masa pakai dan keamanan perangkat. Sistem manajemen daya pada papan Bitaxe mencakup sirkuit canggih yang dirancang untuk mengatur pengiriman tegangan ke chip ASIC sambil memantau konsumsi daya di berbagai mode operasional. Kemampuan manajemen daya ini memungkinkan perangkat beroperasi secara efisien di berbagai frekuensi dan tegangan internal, biasanya mengkonsumsi antara 5 hingga 25 watt tergantung pada konfigurasi.


Memahami kebutuhan daya menjadi sangat penting ketika mempertimbangkan bahwa aplikasi tegangan yang salah dapat merusak perangkat secara permanen. Hubungan antara frekuensi, voltase, konsumsi daya, dan laju hash menunjukkan prinsip-prinsip dasar operasi ASIC yang berlaku di semua perangkat keras mining. Pengguna dapat bereksperimen dengan pengaturan daya yang berbeda untuk memahami pertukaran efisiensi yang melekat pada operasi mining, mendapatkan pengalaman praktis dengan konsep yang berlaku untuk implementasi mining skala yang lebih besar.


### Fokus dan Partisipasi Jaringan Mining Solo


Platform Bitaxe secara khusus menargetkan aplikasi mining solo, di mana penambang individu mencoba untuk memecahkan blok Bitcoin secara mandiri daripada berpartisipasi dalam kumpulan mining yang besar. Walaupun tingkat hash perangkat Bitaxe membuat penemuan blok yang sukses secara statistik tidak mungkin terjadi, pendekatan ini memiliki tujuan pendidikan dan filosofis yang penting dalam komunitas Bitcoin. Solo mining dengan perangkat Bitaxe membantu pengguna memahami mekanisme dasar sistem Bitcoin sambil berkontribusi pada desentralisasi jaringan.


Penekanan pada mining solo mencerminkan komitmen komunitas OSMU untuk mendorong partisipasi individu dalam model keamanan Bitcoin. Dengan menyediakan perangkat keras yang dapat diakses yang dapat beroperasi secara independen, platform Bitaxe memungkinkan pengguna untuk menjalankan operasi mining mereka sendiri tanpa bergantung pada infrastruktur pool. Pendekatan ini mendorong pemahaman yang lebih dalam mengenai mekanisme konsensus Bitcoin sekaligus mendukung sifat desentralisasi jaringan melalui peningkatan keragaman penambang.


### Evolusi Perangkat Keras dan Peningkatan Produksi


Platform Bitaxe terus berkembang melalui umpan balik dari komunitas dan optimalisasi produksi, dengan versi yang lebih baru yang menggabungkan peningkatan yang meningkatkan kemampuan produksi dan pengalaman pengguna. Pembaruan versi biasanya berfokus pada efisiensi produksi daripada perubahan kinerja yang mendasar, memastikan bahwa pengguna yang ada tidak menghadapi tekanan keusangan. Fitur-fitur seperti transisi dari konektor micro-USB ke USB-C dan sistem koneksi daya yang lebih baik mencerminkan perhatian komunitas terhadap peningkatan kegunaan praktis.


Pendekatan evolusioner ini menunjukkan manfaat pengembangan perangkat keras sumber terbuka, di mana masukan dari komunitas mendorong peningkatan bertahap yang bermanfaat bagi semua pengguna. Filosofi "jika ada hash, maka ada hash" menekankan fokus platform pada fungsionalitas daripada peningkatan yang konstan, mendorong pengguna untuk memelihara dan mengoperasikan perangkat mereka daripada mengejar versi terbaru. Pendekatan ini mendukung praktik perangkat keras yang berkelanjutan dengan tetap mempertahankan nilai edukasi Bitaxe.


## Di mana saya dapat mempelajari lebih lanjut?

<chapterId>706f2fff-fa1c-5d8e-b14c-ece6e42c016f</chapterId>

:::video id=90088397-3a16-485f-bbd2-89cdbb844e4a:::

Proyek Bitaxe merupakan inisiatif open-source mining yang komprehensif yang melampaui satu perangkat. Memahami di mana menemukan informasi yang dapat diandalkan, sumber daya teknis, dan dukungan komunitas sangat penting bagi siapa saja yang ingin terlibat dalam ekosistem ini. Bab ini memberikan panduan lengkap untuk platform dan sumber daya penting yang menjadi fondasi komunitas Bitaxe dan Open Source Miners United (OSMU).


### Bitaxe.org, Pusat Informasi


Situs web Bitaxe.org berfungsi sebagai pintu gerbang utama untuk semua informasi dan sumber daya yang berhubungan dengan proyek. Platform terpusat ini berfungsi sebagai titik referensi pertama Anda kapan pun Anda perlu mempelajari perangkat Bitaxe atau menjelajahi proyek-proyek lain dalam komunitas OSMU. Desain situs web ini memprioritaskan aksesibilitas dan pengaturan, menyajikan pengunjung dengan tautan yang dikurasi dengan cermat yang menghubungkan ke berbagai sumber daya khusus di seluruh ekosistem.


Pentingnya pusat pusat ini tidak dapat dilebih-lebihkan, karena menghilangkan kebingungan yang sering menyertai proyek-proyek sumber terbuka yang terdesentralisasi. Daripada mencari melalui berbagai platform atau mengandalkan informasi yang mungkin sudah ketinggalan zaman dari sumber yang tidak resmi, pengguna dapat mempercayai Bitaxe.org untuk menyediakan tautan terkini dan terverifikasi ke semua sumber daya penting. Pendekatan ini memastikan bahwa baik pendatang baru maupun anggota komunitas yang berpengalaman dapat secara efisien menemukan informasi spesifik yang mereka butuhkan untuk proyek mereka.


### Sumber Daya Teknis dan Materi Pengembangan


Repositori file desain perangkat keras di GitHub merupakan salah satu sumber daya yang paling berharga bagi siapa saja yang tertarik untuk memahami atau membangun perangkat Bitaxe. Repositori publik ini berisi dokumentasi komprehensif yang mencakup setiap aspek proses desain perangkat keras, mulai dari konsep awal hingga spesifikasi manufaktur akhir. Repositori ini mencakup gambar-gambar terperinci, tujuan proyek, deskripsi fitur, dan penjelasan komponen internal yang memberikan kedalaman teknis dan panduan praktis.


Bagi mereka yang tertarik untuk membuat perangkat mereka sendiri, repositori ini menyertakan file dokumentasi khusus seperti building.md, yang memberikan petunjuk langkah demi langkah untuk seluruh proses produksi. Dokumentasi ini mencakup alat perangkat lunak yang diperlukan untuk desain PCB, prosedur untuk mengirim file ke produsen, dan langkah-langkah yang terlibat dalam menerima dan memvalidasi PCB yang diproduksi. Tingkat detail ini memastikan bahwa individu atau organisasi kecil dapat berhasil menavigasi proses produksi tanpa pengalaman yang luas sebelumnya dalam produksi perangkat keras.


Repositori ESP-Miner berfungsi sebagai lokasi pusat untuk semua kode dan dokumentasi yang berhubungan dengan firmware. Repositori GitHub ini berisi setiap baris kode yang ditulis untuk firmware Bitaxe, bersama dengan dokumentasi lengkap yang menjelaskan persyaratan sistem, spesifikasi perangkat keras, dan opsi konfigurasi. Struktur repositori dirancang untuk mengakomodasi pengguna yang lebih memilih file biner yang sudah dikompilasi dan pengembang yang ingin membangun firmware dari kode sumber.


Dokumentasi dalam repositori ini mencakup bagian yang mendetail mengenai persyaratan perangkat keras, opsi pra-konfigurasi, dan nilai yang direkomendasikan untuk berbagai pengaturan. Informasi ini terbukti sangat berharga bagi pengguna yang ingin menyesuaikan perangkat mereka atau memecahkan masalah tertentu. Selain itu, repositori ini juga menyertakan informasi tentang perkembangan terbaru, seperti integrasi Raspberry Pi, untuk memastikan bahwa dokumentasi tetap mutakhir dengan evolusi proyek yang sedang berlangsung.


### Alat Manajemen dan Pemeliharaan Perangkat


Flasher web Bitaxe merupakan solusi praktis untuk pemeliharaan dan pembaruan perangkat. Alat berbasis web ini memungkinkan pengguna untuk melakukan flash firmware ke perangkat mereka tanpa memerlukan perangkat lunak khusus atau prosedur baris perintah yang rumit. Flasher ini mendukung berbagai varian perangkat, termasuk Bitaxe Ultra dengan berbagai versi port dan model Bitaxe Max yang lebih lama. Pengguna dapat memilih antara memperbarui firmware yang ada melalui antarmuka web atau melakukan reset lengkap dari pabrik menggunakan koneksi USB.


Alat ini menjawab salah satu tantangan paling umum yang dihadapi oleh para penggemar perangkat keras: memelihara dan memperbarui firmware perangkat. Dengan menyediakan antarmuka web yang mudah digunakan, flasher ini menghilangkan banyak hambatan teknis yang mungkin menghalangi pengguna untuk selalu memperbarui perangkat mereka dengan rilis firmware terbaru. Desain alat ini memprioritaskan kesederhanaan sekaligus mempertahankan fleksibilitas yang diperlukan untuk berbagai konfigurasi perangkat dan skenario pembaruan.


### Platform Komunitas dan Saluran Komunikasi


Server Discord merupakan jantung dari interaksi dan dukungan komunitas secara real-time dalam ekosistem Bitaxe. Organisasi server mencerminkan minat dan kebutuhan anggota komunitas yang beragam, dengan saluran yang terstruktur dengan cermat yang memfasilitasi diskusi terfokus pada topik tertentu. Anggota baru akan menghadapi proses verifikasi yang mengharuskan mereka membaca dan menerima peraturan komunitas, memastikan bahwa semua peserta memahami harapan untuk interaksi yang saling menghormati dan produktif.


Struktur saluran server mencakup area diskusi umum yang mencakup topik-topik seperti integrasi tenaga surya, kumpulan mining, dan diskusi terkait Bitcoin. Bagian yang lebih khusus berfokus pada perangkat tertentu, termasuk saluran khusus untuk varian Bitaxe Ultra, Hex, dan Supra. Saluran firmware menyediakan ruang yang terfokus untuk diskusi teknis tentang pengembangan perangkat lunak dan pemecahan masalah, sementara saluran rilis resmi memastikan bahwa anggota komunitas menerima pemberitahuan tepat waktu tentang perkembangan baru.


Situs ini juga dilengkapi dengan area pelanggan yang memberikan manfaat tambahan bagi anggota komunitas yang memilih untuk mendukung proyek ini secara finansial. Pendekatan berjenjang ini memungkinkan komunitas untuk menawarkan layanan yang lebih baik dengan tetap mempertahankan akses terbuka ke informasi penting dan saluran dukungan. Saluran bantuan berfungsi sebagai ruang khusus untuk pemecahan masalah dan bantuan teknis, memastikan bahwa pengguna dapat menerima dukungan yang cepat ketika menghadapi kesulitan.



Wiki Open Source Miners United (osmu.wiki) menyediakan dokumentasi komprehensif yang melengkapi diskusi real-time yang terjadi di Discord. Tidak seperti platform berbasis obrolan, wiki ini menawarkan dokumentasi yang terstruktur dan dapat dicari yang mencakup semua aspek proyek Bitaxe dan inisiatif terkait. Cara pengorganisasiannya mencerminkan struktur proyek, dengan bagian khusus untuk seri perangkat yang berbeda dan panduan penyiapan yang komprehensif.


Sifat sumber terbuka wiki memungkinkan anggota komunitas untuk berkontribusi secara langsung pada dokumentasi. Pengguna dapat mengedit halaman, mengirimkan koreksi, dan menambahkan informasi baru melalui integrasi GitHub, memastikan bahwa basis pengetahuan tetap mutakhir dan transparan. Pendekatan kolaboratif ini memanfaatkan keahlian kolektif komunitas sambil mempertahankan kontrol kualitas melalui proses peninjauan untuk perubahan yang diajukan.


Wiki mencakup sumber daya praktis seperti panduan penyiapan PDF yang menyediakan petunjuk langkah demi langkah untuk konfigurasi dan penggunaan perangkat. Panduan ini berfungsi sebagai referensi berharga bagi pengguna baru dan anggota komunitas berpengalaman yang membutuhkan akses cepat ke prosedur atau detail konfigurasi tertentu.


### Informasi Pembelian dan Vendor


Daftar resmi Bitaxe memenuhi kebutuhan penting dalam komunitas perangkat keras sumber terbuka: mengidentifikasi vendor yang dapat dipercaya dan menghindari penjual yang curang. Daftar yang telah dikurasi ini mencakup pengecer dan produsen terverifikasi yang memenuhi kriteria khusus untuk keabsahan dan dukungan komunitas. Setiap daftar mencakup tautan langsung ke situs web vendor, informasi regional, dan deskripsi perusahaan yang membantu pengguna membuat keputusan pembelian yang tepat.


Yang penting, daftar tersebut menunjukkan apakah setiap vendor berkontribusi kembali kepada komunitas OSMU, baik secara finansial maupun melalui bentuk dukungan lainnya. Transparansi ini membantu anggota komunitas untuk memahami vendor mana yang secara aktif mendukung pengembangan dan keberlanjutan proyek. Daftar ini juga berfungsi sebagai tindakan perlindungan terhadap penipuan umum, seperti pre-order tidak sah untuk produk yang belum dirilis, yang secara historis menyebabkan masalah dalam komunitas.


Penekanan pada tautan non-afiliasi menunjukkan komitmen komunitas untuk memberikan rekomendasi vendor yang tidak bias. Pengguna dapat mempercayai bahwa rekomendasi yang diberikan didasarkan pada legitimasi vendor dan kontribusi komunitas, bukan insentif finansial, sehingga memastikan bahwa keputusan pembelian mendukung kebutuhan individu dan keberlanjutan komunitas.



# Perangkat Lunak dan Operasi

<partId>04b302a9-42ba-5ad4-834c-6979950c2948</partId>


## Apa itu AxeOS?

<chapterId>a0cdf10d-e007-58e2-a17b-b588fd393b5e</chapterId>

:::video id=de7bcbf2-f9ac-4057-ad40-29dc223b4798:::

AxeOS adalah firmware dan antarmuka web untuk perangkat Bitaxe mining, yang memberikan kontrol penuh dan kemampuan pemantauan kepada pengguna melalui dasbor berbasis browser yang intuitif. Sistem ini mengubah tugas manajemen ASIC yang rumit menjadi pengalaman yang mudah diakses, memungkinkan penambang untuk memantau kinerja, menyesuaikan pengaturan, dan mengelola beberapa perangkat dari satu antarmuka. Memahami AxeOS sangat penting untuk memaksimalkan potensi perangkat Bitaxe Anda dan mempertahankan operasi mining yang optimal.


### Ikhtisar Dasbor dan Metrik Inti


Dasbor AxeOS berfungsi sebagai jendela utama Anda ke dalam kinerja perangkat Bitaxe Anda, menyajikan metrik mining yang penting dalam format waktu nyata yang terorganisir. Ketika Anda menavigasi ke alamat IP perangkat Bitaxe Anda, Anda akan segera disajikan dengan empat indikator kinerja utama yang menentukan kondisi operasi mining Anda saat ini. Tampilan laju hash menunjukkan kecepatan komputasi aktual yang dihasilkan chip ASIC Anda saat memproses template blok saat ini, memberikan umpan balik langsung pada fungsionalitas inti perangkat Anda.


Berdekatan dengan tingkat hash, penghitung saham melacak setiap solusi valid yang dikirimkan perangkat Bitaxe Anda ke kumpulan mining, bertambah dengan setiap pengiriman yang berhasil dan berfungsi sebagai ukuran langsung dari kontribusi perangkat Anda terhadap upaya mining. Metrik efisiensi memberikan wawasan penting tentang kinerja daya perangkat Anda dengan menghitung rasio tingkat hash terhadap konsumsi daya, sehingga membantu Anda mengoptimalkan profitabilitas operasi Anda. Indikator tingkat kesulitan terbaik menyimpan catatan tingkat kesulitan tertinggi yang pernah ditemukan perangkat Anda, mempertahankan pencapaian ini bahkan melalui reboot dan pembaruan, hanya mengatur ulang ketika Anda melakukan flash pabrik secara lengkap.


Sistem menu dasbor yang dapat diperluas, dikontrol oleh tombol sakelar, menyediakan akses ke semua fungsionalitas AxeOS dengan tetap mempertahankan antarmuka yang bersih. Grafik hash rate langsung merupakan salah satu fitur yang paling berharga, menampilkan data kinerja waktu nyata yang menjadi lebih akurat dan informatif semakin lama Anda mempertahankan sesi Anda. Bagian daya, panas, dan kinerja menyediakan pemantauan komprehensif terhadap status operasional perangkat Anda, termasuk peringatan tegangan input yang memperingatkan Anda akan potensi masalah catu daya sambil memastikan pengoperasian yang berkelanjutan dalam parameter yang aman.


### Pemantauan Lanjutan dan Informasi Sistem


Kemampuan pemantauan AxeOS jauh melampaui pelacakan tingkat hash dasar, memberikan wawasan terperinci tentang setiap aspek operasi perangkat Bitaxe Anda. Bagian daya menampilkan konsumsi daya yang dihitung yang berasal dari sirkuit terintegrasi onboard, pengukuran tegangan input dari koneksi catu daya Anda, dan level tegangan ASIC yang diminta. Ketika terjadi penurunan tegangan, AxeOS segera menampilkan notifikasi peringatan, meskipun ini biasanya tidak mempengaruhi operasi mining dan hanya menunjukkan peluang optimalisasi catu daya.


Pemantauan suhu berfokus pada manajemen termal chip ASIC, dengan pembacaan yang diambil dari lokasi strategis pada perangkat untuk memberikan data termal yang akurat dengan offset yang sesuai untuk akurasi tingkat chip. Tampilan frekuensi dan tegangan menawarkan umpan balik waktu nyata pada parameter penyetelan ASIC Anda, dengan tegangan terukur yang mewakili pembacaan paling akurat yang tersedia, yang diambil langsung di lokasi chip ASIC. Ketepatan ini memungkinkan penyetelan parameter kinerja dengan tetap mempertahankan kondisi pengoperasian yang aman.


Bagian status koneksi memberikan visibilitas langsung ke dalam konfigurasi pool mining Anda, menampilkan URL strata saat ini, port, dan identifikasi pengguna. Untuk perangkat yang terhubung ke kolam renang umum, AxeOS menghasilkan tautan cepat yang nyaman yang membawa Anda langsung ke antarmuka web kolam renang Anda, di mana Anda dapat mengakses statistik terperinci, daftar perangkat, dan data kinerja historis. Integrasi ini menyederhanakan proses pemantauan dengan menghubungkan informasi tingkat perangkat dan tingkat kolam renang dalam alur kerja yang mulus.


### Manajemen Kawanan dan Kontrol Multi-Perangkat


Fungsionalitas Swarm merupakan solusi AxeOS untuk kerumitan dalam mengelola beberapa perangkat Bitaxe di seluruh jaringan, sehingga tidak perlu lagi mengingat dan menavigasi ke banyak alamat IP. Sistem manajemen terpusat ini memungkinkan Anda untuk menambahkan perangkat hanya dengan memasukkan alamat IP mereka, secara otomatis mendeteksi penambang Bitaxe yang aktif dan menggabungkannya ke dalam dasbor kontrol terpadu. Setelah dikonfigurasi, Swarm memberikan kontrol yang komprehensif atas seluruh operasi mining Anda dari satu antarmuka.


Melalui antarmuka Swarm, Anda dapat melakukan tugas-tugas manajemen penting di beberapa perangkat secara bersamaan atau satu per satu, termasuk perubahan konfigurasi pool, restart perangkat, penyesuaian frekuensi, dan pemantauan kinerja. Pendekatan terpusat ini secara signifikan mengurangi biaya administrasi dalam mengelola operasi mining yang besar sekaligus memastikan konfigurasi yang konsisten di semua perangkat. Sistem ini mempertahankan identitas perangkat individu sambil memberikan kemampuan manajemen kolektif, mencapai keseimbangan optimal antara kontrol granular dan efisiensi operasional.


Dasbor Swarm menampilkan setiap perangkat yang dikelola dengan status saat ini, metrik kinerja, dan kontrol akses cepat, sehingga memungkinkan respons yang cepat terhadap masalah kinerja atau perubahan konfigurasi. Fungsionalitas ini terbukti sangat berharga bagi para penambang yang mengoperasikan beberapa perangkat di lokasi yang berbeda atau mereka yang sering menyesuaikan parameter mining berdasarkan kondisi pasar atau kinerja pool.


### Manajemen Konfigurasi dan Pengaturan Sistem


Bagian Pengaturan dari AxeOS menyediakan kontrol yang komprehensif atas setiap aspek yang dapat dikonfigurasi dari perangkat Bitaxe Anda, mulai dari konektivitas jaringan hingga parameter mining dan optimalisasi perangkat keras. Konfigurasi jaringan dimulai dengan pengaturan Wi-Fi, di mana Anda menentukan nama jaringan dan kata sandi Anda, dengan AxeOS merekomendasikan nama jaringan satu kata tanpa spasi untuk memastikan konektivitas yang andal. Sistem ini menangani proses konfigurasi nirkabel yang lengkap, memungkinkan manajemen jarak jauh dan kemampuan pemantauan.


Konfigurasi Mining berpusat pada pengaturan strata, di mana Anda menentukan URL pool mining yang Anda pilih tanpa awalan protokol atau nomor port, yang ditangani dalam bidang terpisah. Bidang pengguna strata mengakomodasi berbagai persyaratan pool, mendukung alamat Bitcoin untuk mining tunggal dan sistem nama pengguna untuk pool mining, dengan kemampuan untuk menambahkan pengidentifikasi perangkat untuk operasi multi-perangkat. Fungsionalitas kata sandi strata yang baru-baru ini ditambahkan mendukung pool yang membutuhkan autentikasi, meskipun sebagian besar pool publik beroperasi tanpa persyaratan ini.


Pengoptimalan perangkat keras melalui penyesuaian frekuensi dan tegangan inti merupakan kemampuan penyetelan kinerja AxeOS yang paling kuat. Tergantung pada versi perangkat dan browser Anda, pengaturan ini dapat muncul sebagai menu tarik-turun dengan konfigurasi yang telah ditetapkan atau sebagai bidang terbuka yang memungkinkan nilai khusus. Pengaturan default frekuensi 485 MHz dan tegangan inti 1200 mV memberikan operasi yang stabil untuk pengujian awal, sementara pengguna tingkat lanjut dapat mengoptimalkan parameter ini untuk kinerja atau efisiensi maksimum berdasarkan persyaratan khusus dan kondisi operasi mereka.


### Pemeliharaan Sistem dan Fitur Lanjutan


AxeOS mencakup kemampuan pemeliharaan sistem yang canggih yang dirancang untuk menjaga perangkat Bitaxe Anda tetap beroperasi pada kinerja puncak sambil memberikan informasi diagnostik untuk pemecahan masalah dan pengoptimalan. Sistem pembaruan menyederhanakan manajemen firmware dengan menampilkan rilis terbaru yang tersedia secara langsung di antarmuka dan menyediakan tautan unduhan langsung ke file firmware resmi. Integrasi ini menghilangkan kebutuhan untuk menavigasi repositori GitHub secara manual atau mengelola unduhan file, menyederhanakan proses pembaruan menjadi beberapa klik.


Antarmuka pembaruan menerima file firmware dengan nama yang tepat, khususnya esp-miner.bin dan www.bin, untuk memastikan kompatibilitas dan mencegah kesalahan instalasi. Bagi pengguna yang mengalami kesulitan dengan proses pembaruan standar, AxeOS menyediakan referensi untuk prosedur flash pabrik yang komprehensif yang dapat mengembalikan perangkat ke fungsi aslinya. Pendekatan ganda ini mengakomodasi pembaruan rutin dan skenario pemulihan.


Sistem pencatatan memberikan wawasan waktu nyata ke dalam operasi perangkat, menampilkan informasi terperinci tentang model chip ASIC, waktu aktif sistem, status konektivitas Wi-Fi, memori yang tersedia, versi firmware, dan revisi board. Log ini terbukti sangat berharga bagi pengembang dan pengguna tingkat lanjut yang ingin memahami perilaku perangkat, mendiagnosis masalah, atau mengoptimalkan kinerja. Penampil log waktu nyata menyajikan data operasional langsung, termasuk pemrosesan nonce, perhitungan kesulitan, dan parameter pengiriman mining, menawarkan visibilitas yang belum pernah terjadi sebelumnya ke dalam proses mining itu sendiri.


Fitur sistem tambahan termasuk kontrol orientasi layar untuk perangkat yang digunakan dalam penutup khusus, inversi polaritas kipas untuk konfigurasi pendinginan khusus, dan kontrol kipas otomatis yang menyesuaikan pendinginan berdasarkan suhu ASIC. Kontrol kecepatan kipas manual memberikan manajemen pendinginan yang tepat ketika sistem otomatis tidak memenuhi persyaratan tertentu. Semua perubahan konfigurasi memerlukan penyimpanan dan restart perangkat agar dapat diterapkan, memastikan operasi yang stabil dan mencegah status konfigurasi parsial yang dapat memengaruhi kinerja mining.



# Komunitas dan Kolaborasi

<partId>eed1ce48-6752-5744-91f7-91e4e20ff6b2</partId>


## Ikhtisar Kontribusi Sumber Terbuka

<chapterId>715d026e-cebc-536e-a34e-728f5653b999</chapterId>

:::video id=7298ba19-28d2-4a7c-ac0b-44ad0c4770cf:::

### GitHub dan Perannya dalam Pengembangan Perangkat Lunak


GitHub mewakili perubahan mendasar dalam cara proyek pengembangan perangkat lunak dikelola dan dibagikan di seluruh komunitas pemrograman global. Sebagai platform berbasis cloud yang menjadi tuan rumah proyek pengembangan perangkat lunak menggunakan Git, sistem kontrol versi terdistribusi, GitHub memungkinkan para pengembang untuk berkolaborasi dengan lancar dalam proyek tanpa memandang lokasi fisik mereka. Platform ini berfungsi sebagai alat teknis dan jaringan sosial bagi para programmer, memungkinkan mereka untuk melacak perubahan, menggabungkan pembaruan, memelihara berbagai versi kode mereka, dan berkontribusi pada inisiatif sumber terbuka seperti proyek BitX dari Open Source Miners United.


Kekuatan GitHub terletak pada kemampuannya untuk menyederhanakan proses pengembangan kolaboratif yang kompleks. Ketika beberapa pengembang mengerjakan proyek yang sama, GitHub menyediakan infrastruktur untuk mengelola kontribusi, meninjau perubahan, menangani masalah proyek, dan memelihara dokumentasi yang komprehensif. Pendekatan kolaboratif ini telah menjadikan GitHub sebagai komponen penting dalam alur kerja pengembangan perangkat lunak modern, yang mengubah cara pengembang individu dan organisasi besar dalam melakukan pendekatan terhadap manajemen proyek dan berbagi kode.


### Menavigasi GitHub Interface dan Struktur Repositori


Memahami antarmuka GitHub dimulai dengan mengenali elemen-elemen kunci yang membentuk halaman repositori. Bilah navigasi bagian atas berisi beberapa bagian penting termasuk Kode, Masalah, Permintaan Tarik, Diskusi, Tindakan, Proyek, Keamanan, dan Wawasan. Setiap bagian memiliki tujuan tertentu dalam ekosistem manajemen proyek, dengan bagian Code menampilkan file dan folder aktual yang membentuk proyek.


Struktur repositori itu sendiri mencerminkan pendekatan organisasi pengelola proyek. Beberapa repositori hanya berisi satu berkas, mungkin sebuah skrip shell sederhana, sementara yang lain seperti proyek perangkat keras BitX berisi banyak berkas yang diorganisasikan ke dalam direktori dan subdirektori. Nama repositori muncul dengan jelas dan berfungsi sebagai pengenal dan deskripsi singkat tentang tujuan proyek. Elemen interaktif yang penting termasuk tombol Watch untuk menerima pemberitahuan tentang pembaruan repositori, tombol Fork untuk membuat salinan pribadi repositori, dan tombol Star yang berfungsi sebagai sistem pengesahan komunitas yang mirip dengan fitur "jempol".


Bagian Tentang menyediakan informasi proyek yang penting dalam format yang ringkas, termasuk deskripsi satu baris, informasi lisensi, dan detail proyek utama. Untuk proyek BitX, bagian ini mengidentifikasikannya sebagai "perangkat keras penambang open source ASIC Bitcoin" dan menentukan lisensi GPL 3.0. Memahami lisensi sangat penting karena GitHub beroperasi sebagai platform sumber terbuka di mana repositori publik dapat diakses oleh seluruh komunitas, tetapi kontennya hanya dapat digunakan dan didistribusikan sesuai dengan aturan kepatuhan masing-masing lisensi.


### Bekerja dengan Cabang dan Versi Proyek


Konsep cabang merupakan salah satu fitur GitHub yang paling kuat untuk mengelola berbagai versi dan jalur pengembangan dalam satu proyek. Cabang pada dasarnya membuat salinan atau versi modifikasi dari basis kode utama, yang memungkinkan pengembang untuk mengerjakan fitur-fitur tertentu, perbaikan bug, atau perubahan eksperimental tanpa memengaruhi jalur pengembangan utama. Cabang utama biasanya berfungsi sebagai versi default dan paling stabil dari proyek, sementara cabang tambahan mengakomodasi iterasi yang berbeda, fase pengujian, atau varian produk yang sama sekali berbeda.


Dalam proyek perangkat keras BitX, terdapat beberapa cabang untuk mengelola versi dan konfigurasi perangkat keras yang berbeda. Sebagai contoh, cabang Ultra v2 berisi file khusus untuk iterasi perangkat keras tersebut, sedangkan cabang Super 401 berfokus pada implementasi yang menggunakan chip S21 ASIC untuk meningkatkan efisiensi. Setiap cabang mungkin memiliki beberapa komit di depan atau di belakang cabang utama, yang menunjukkan sejauh mana perubahan dan aktivitas pengembangan. Ketika memeriksa cabang yang berbeda, pengguna akan melihat struktur file, dokumentasi, dan bahkan representasi visual yang sama sekali berbeda, yang mencerminkan persyaratan dan spesifikasi unik dari setiap varian perangkat keras.


Sistem cabang mencegah kebingungan di antara kontributor dan pengguna dengan memisahkan jalur pengembangan yang berbeda secara jelas. Daripada mencampur fitur eksperimental dengan rilis stabil, atau menggabungkan versi perangkat keras yang berbeda di satu lokasi, cabang memberikan pemisahan yang jelas sambil mempertahankan kemampuan untuk menggabungkan perubahan yang berhasil kembali ke jalur pengembangan utama jika diperlukan. Pendekatan organisasi ini memastikan bahwa pengguna dapat dengan mudah menemukan versi spesifik yang mereka butuhkan sementara pengembang dapat mengerjakan perbaikan tanpa mengganggu proyek utama.


### Berkontribusi Melalui Isu


Bagian Masalah berfungsi sebagai saluran komunikasi utama antara pengguna dan pengelola proyek untuk melaporkan masalah, menyarankan perbaikan, dan mendokumentasikan bug. Namun, sangat penting untuk memahami bahwa bagian Masalah dirancang khusus untuk masalah teknis yang sah, bukan pertanyaan umum atau permintaan dukungan. Ketika pengguna menemukan kerusakan aktual, perilaku tak terduga, atau mengidentifikasi potensi perbaikan, membuat masalah yang terdokumentasi dengan baik akan membantu seluruh komunitas dengan memberikan perhatian pada masalah yang dapat memengaruhi banyak pengguna.


Pelaporan masalah yang efektif membutuhkan dokumentasi masalah yang mendetail, termasuk keadaan yang menyebabkan masalah tersebut, langkah-langkah untuk mereproduksi masalah, dan detail teknis yang relevan. Proyek BitX mendemonstrasikan prinsip ini melalui berbagai masalah tertutup yang menunjukkan proses penyelesaiannya, mulai dari identifikasi masalah awal melalui diskusi komunitas hingga penyelesaian akhir. Beberapa masalah menghasilkan perbaikan perangkat keras, seperti penambahan lubang pemasangan untuk meningkatkan opsi pendinginan, sementara yang lain dapat diselesaikan melalui pendidikan pengguna atau pembaruan perangkat lunak.


Perbedaan antara Isu dan Diskusi penting untuk menjaga interaksi komunitas yang terorganisir. Sementara Isu berfokus pada masalah teknis tertentu, bagian Diskusi menyediakan lingkungan seperti forum untuk pertanyaan, ide, dan keterlibatan komunitas secara umum. Meskipun server Discord telah menjadi saluran komunikasi utama untuk komunitas BitX, bagian Diskusi GitHub tetap tersedia untuk percakapan yang lebih formal atau dapat dicari yang mendapat manfaat dari dokumentasi permanen dan referensi yang mudah.


### Memahami Pull Request


Pull request merupakan mekanisme yang digunakan kontributor eksternal untuk mengusulkan perubahan pada repositori proyek. Ketika seseorang mengidentifikasi peningkatan, perbaikan bug, atau fitur baru yang akan bermanfaat bagi proyek, mereka dapat membuat pull request untuk mengirimkan perubahan mereka untuk ditinjau dan potensi integrasi ke dalam basis kode utama. Proses ini memastikan bahwa semua modifikasi telah ditinjau sebelum menjadi bagian dari proyek resmi, menjaga kualitas kode dan koherensi proyek sambil memungkinkan kontribusi komunitas.


Alur kerja pull request biasanya dimulai ketika seorang kontributor melakukan fork pada repositori, membuat salinannya sendiri di mana mereka dapat melakukan perubahan, dan kemudian mengirimkan perubahan tersebut kembali ke proyek asli melalui pull request. Pengelola proyek kemudian dapat meninjau perubahan yang diusulkan, mendiskusikan modifikasi dengan kontributor, dan pada akhirnya memutuskan apakah akan menggabungkan perubahan tersebut ke dalam proyek utama. Proses peninjauan kolaboratif ini membantu menjaga standar proyek sekaligus mendorong partisipasi dan peningkatan komunitas.


Memahami tag dan rilis menambahkan lapisan lain pada manajemen proyek dan kontrol versi. Tag berfungsi sebagai penanda dalam garis waktu pengembangan, mengidentifikasi titik-titik tertentu yang mewakili versi atau pencapaian tertentu. Dalam proyek perangkat keras seperti BitX, tag sering kali berhubungan dengan nomor model atau revisi perangkat keras tertentu, memberikan titik referensi yang jelas bagi pengguna yang mencari versi tertentu. Rilis, yang lebih umum digunakan dalam proyek perangkat lunak, mewakili distribusi formal dari fitur-fitur yang telah selesai dan perbaikan bug, sering kali disertai dengan catatan rilis yang terperinci dan paket yang dapat diunduh.


Ekosistem GitHub menciptakan lingkungan yang komprehensif untuk kolaborasi sumber terbuka yang jauh melampaui berbagi file sederhana. Dengan memahami berbagai komponen ini dan penggunaannya yang tepat, kontributor dapat berpartisipasi secara efektif dalam proyek, membantu meningkatkan desain perangkat lunak dan perangkat keras, serta mendapatkan manfaat dari pengetahuan dan upaya kolektif komunitas pengembangan global. Baik melaporkan masalah, menyarankan perbaikan, atau menyumbangkan kode, GitHub menyediakan alat dan struktur yang diperlukan untuk kolaborasi yang berarti di dunia sumber terbuka.


## Kontribusi Sumber Terbuka Secara Langsung

<chapterId>84d033f5-7182-584f-b1a5-697172bc7a1c</chapterId>

:::video id=7d318fd0-6f0b-422a-9f30-2c470b56951d:::

Dengan membangun fondasi untuk membuat isu dan mengeksplorasi proyek open source, bab ini berfokus pada aspek praktis dalam memberikan kontribusi langsung melalui pull request dan manajemen repositori. Memahami cara mengelola repositori fork, membuat perubahan, dan mengirimkan pull request merupakan keahlian yang sangat penting bagi setiap pengembang yang ingin berkontribusi secara bermakna pada proyek open source, baik itu pengembangan perangkat lunak maupun desain perangkat keras.


Proses kontribusi perubahan kode mengikuti alur kerja standar yang memastikan integritas proyek sekaligus memungkinkan pengembangan kolaboratif. Alur kerja ini melibatkan pembuatan salinan repositori proyek Anda sendiri, melakukan modifikasi dalam lingkungan yang terkendali, dan kemudian mengusulkan perubahan tersebut kembali ke proyek asli melalui proses peninjauan formal. Meskipun contoh-contoh dalam bab ini berfokus pada kontribusi perangkat lunak, prinsip dan prosedur yang sama juga berlaku untuk proyek perangkat keras yang melibatkan desain PCB, skema, dan dokumentasi teknis lainnya.


### Memahami Forks dan Struktur Repositori


Dasar dari berkontribusi pada proyek sumber terbuka dimulai dengan membuat fork, yang berfungsi sebagai salinan pribadi Anda dari repositori asli. Ketika Anda menavigasi ke repositori GitHub dan mengklik tombol "fork", Anda membuat salinan independen di bawah akun GitHub Anda sendiri yang mempertahankan koneksi yang jelas ke sumber aslinya. Repositori bercabang ini muncul di akun Anda dengan indikasi yang jelas tentang asalnya, menampilkan teks seperti "bercabang dari [pemilik-asli]/[nama-repositori]" di bawah judul repositori.


Repositori bercabang Anda beroperasi secara independen dari yang asli, memungkinkan Anda untuk membuat perubahan tanpa memengaruhi proyek utama. Namun, repositori cabang tetap mengetahui pembaruan pada repositori asli melalui fitur sinkronisasi GitHub. Ketika repositori asli menerima pembaruan yang tidak dimiliki oleh fork Anda, GitHub menampilkan informasi status seperti "Cabang ini adalah X yang berkomitmen di belakang" atau "X yang berkomitmen di depan," yang memberikan visibilitas yang jelas ke dalam hubungan antara fork dan repositori hulu. Anda dapat menyinkronkan fork Anda dengan repositori asli kapan saja dengan mengklik tombol "Sinkronkan fork", yang menarik perubahan terbaru dari sumber hulu.


Hubungan antara fork dan repositori asli menjadi sangat penting ketika Anda mulai membuat perubahan. Ketika Anda mengimplementasikan modifikasi dan mengomitnya ke fork Anda, GitHub melacak perbedaan ini dan menampilkannya sebagai komit di depan repositori asli. Sistem pelacakan ini memungkinkan proses pull request, di mana Anda dapat mengusulkan perubahan Anda untuk dimasukkan ke dalam proyek utama sambil mempertahankan riwayat yang jelas tentang apa yang telah dimodifikasi.


### Menyiapkan Lingkungan Pengembangan Anda


Menciptakan lingkungan pengembangan yang efektif membutuhkan perhatian yang cermat terhadap alat pengembangan umum dan persyaratan khusus proyek. Visual Studio Code berfungsi sebagai lingkungan pengembangan terintegrasi (IDE) yang sangat baik untuk sebagian besar kontribusi sumber terbuka, menyediakan fitur-fitur penting untuk pengeditan kode, integrasi kontrol versi, dan manajemen proyek. Komponen penting pertama melibatkan pemasangan dan konfigurasi ekstensi Git, yang memungkinkan integrasi tanpa batas dengan repositori GitHub langsung dari lingkungan pengembangan Anda.


Versi modern Visual Studio Code biasanya menyertakan dukungan Git secara default, tetapi Anda harus melakukan autentikasi dengan akun GitHub untuk mengaktifkan fungsionalitas penuh. Proses autentikasi ini melibatkan masuk ke GitHub melalui IDE, yang kemudian memungkinkan Anda untuk mengkloning repositori, melakukan perubahan, dan mendorong pembaruan langsung dari lingkungan pengembangan Anda. Integrasi GitHub muncul sebagai ikon di bilah sisi kiri, menyediakan akses ke kloning repositori, manajemen cabang, dan fitur sinkronisasi tanpa memerlukan operasi baris perintah.


Untuk proyek yang melibatkan sistem tertanam atau platform perangkat keras tertentu, alat tambahan menjadi penting. Ekstensi ESP-IDF merupakan komponen penting untuk proyek yang menargetkan mikrokontroler ESP32, yang membutuhkan kompatibilitas versi tertentu untuk memastikan fungsionalitas yang tepat. Proses instalasi melibatkan pemilihan versi ESP-IDF yang sesuai, mengkonfigurasi jalur alat, dan menyiapkan lingkungan wadah pengembangan. Versi 5.1.3 saat ini mewakili konfigurasi yang direkomendasikan untuk banyak proyek berbasis ESP32, meskipun persyaratan ini dapat berkembang saat proyek memperbarui dependensi dan rantai alat mereka.


### Membuat Perubahan dan Mengelola Komitmen


Setelah lingkungan pengembangan Anda dikonfigurasi dengan benar, proses membuat kontribusi yang berarti dimulai dengan mengunduh atau mengkloning repositori bercabang Anda ke mesin lokal Anda. Anda dapat melakukannya dengan mengunduh file ZIP dari konten repositori atau dengan menggunakan fungsionalitas kloning terintegrasi Visual Studio Code, yang menyediakan alur kerja yang lebih efisien untuk pengembangan yang sedang berlangsung. Proses kloning membuat salinan lokal repositori Anda yang tetap tersinkronisasi dengan GitHub fork, memungkinkan Anda untuk bekerja secara offline dengan tetap mempertahankan kemampuan kontrol versi.


Ketika bekerja dengan repositori lokal, Anda mendapatkan akses ke struktur proyek yang lengkap, termasuk file kode sumber, file konfigurasi, dokumentasi, dan file desain perangkat keras. Sebagian besar proyek firmware menggunakan bahasa pemrograman seperti C untuk fungsionalitas inti, dengan komponen tambahan yang ditulis dalam TypeScript untuk antarmuka pengguna atau Java untuk utilitas tertentu. Memahami struktur proyek membantu Anda mengidentifikasi file yang sesuai untuk dimodifikasi dan memastikan bahwa perubahan yang Anda lakukan selaras dengan pola arsitektur dan standar pengkodean proyek.


Proses komit merupakan aspek fundamental dari kontrol versi yang membutuhkan perhatian yang cermat terhadap akurasi teknis dan kejelasan komunikasi. Sebelum melakukan perubahan apa pun, Anda harus benar-benar memahami kode yang ada dan menguji modifikasi apa pun di lingkungan lokal Anda. Aturan utama dari kontribusi open source menekankan untuk tidak pernah mempublikasikan kode yang belum teruji, karena hal ini dapat menyebabkan bug atau kerentanan keamanan yang mempengaruhi seluruh komunitas proyek. Selain itu, Anda tidak boleh memberikan informasi sensitif seperti kata sandi, token API, atau kredensial pribadi ke repositori publik, karena informasi ini dapat diakses secara permanen oleh siapa pun yang memiliki akses ke repositori.


### Membuat dan Mengelola Pull Request


Puncak dari upaya kontribusi Anda adalah membuat pull request, yang berfungsi sebagai proposal formal untuk menggabungkan perubahan Anda ke dalam repositori proyek asli. Proses ini dimulai di GitHub fork Anda, di mana Anda dapat meninjau perbedaan antara repositori Anda dan sumber hulu. Antarmuka GitHub dengan jelas menampilkan jumlah komit di depan atau di belakang, memberikan visibilitas langsung ke dalam cakupan perubahan yang Anda usulkan. Sebelum membuat pull request, Anda harus memastikan fork Anda disinkronkan dengan perubahan hulu terbaru untuk meminimalkan potensi konflik.


Membuat pull request yang efektif membutuhkan lebih dari sekadar mengirimkan perubahan kode Anda. Deskripsi pull request berfungsi sebagai kesempatan Anda untuk mengomunikasikan tujuan, ruang lingkup, dan dampak modifikasi Anda kepada pengelola dan komunitas proyek. Deskripsi yang ditulis dengan baik menjelaskan masalah apa yang diatasi oleh perubahan Anda, bagaimana Anda mengimplementasikan solusinya, dan implikasi potensial untuk bagian lain dari proyek. Dokumentasi ini menjadi sangat penting untuk perubahan kompleks yang mungkin tidak langsung terlihat dengan melihat perbedaan kode saja.


Proses peninjauan merupakan aspek kolaboratif dari pengembangan open source di mana pengelola proyek dan kontributor berpengalaman mengevaluasi perubahan yang Anda ajukan. Anda dapat meminta peninjau khusus yang memiliki keahlian di bidang yang dipengaruhi oleh perubahan Anda, memastikan bahwa anggota komunitas yang berpengetahuan luas memeriksa pekerjaan Anda. Proses peninjauan dapat melibatkan beberapa iterasi, dengan peninjau memberikan umpan balik, meminta modifikasi, atau meminta pengujian tambahan. Proses penyempurnaan kolaboratif ini membantu menjaga kualitas kode sambil memberikan kesempatan belajar yang berharga bagi kontributor di semua tingkat pengalaman.


Memahami bahwa tidak semua pull request akan diterima akan membantu menetapkan ekspektasi yang tepat untuk proses kontribusi. Pengelola proyek dapat menolak pull request karena berbagai alasan, termasuk ketidaksesuaian dengan tujuan proyek, pengujian yang tidak memadai, atau adanya solusi alternatif yang sudah dikembangkan. Daripada melihat penolakan sebagai kegagalan, hal ini harus dianggap sebagai kesempatan untuk belajar dari umpan balik, memperbaiki pendekatan, dan berpotensi menyumbangkan solusi alternatif yang lebih baik untuk memenuhi kebutuhan proyek. Komunitas open source tumbuh subur dalam proses berulang dari proposal, tinjauan, dan penyempurnaan yang pada akhirnya mendorong proyek ke depan melalui upaya kolektif dan keahlian bersama.



## Apa itu Kolam Renang Umum?

<chapterId>b461bf94-4a90-5bb8-ba3f-976d5d57be0d</chapterId>


:::video id=d4652496-1ed4-4415-8048-0b6871b9ed51:::

Public Pool mewakili pendekatan revolusioner untuk Bitcoin mining yang mengatasi banyak masalah yang dimiliki oleh para penambang dengan pool mining tradisional. Sebagai pool Bitcoin mining solo yang sepenuhnya open-source, Public Pool secara fundamental mengubah model distribusi reward yang selama ini digunakan oleh para penambang. Tidak seperti pool mining konvensional di mana para peserta berbagi reward ketika ada penambang di pool tersebut yang menemukan sebuah blok, Public Pool beroperasi dengan prinsip solo mining di mana penambang individu mempertahankan 100% dari reward blok mereka ketika mereka berhasil menambang sebuah blok.


Fitur yang paling menarik dari Public Pool adalah struktur tanpa biaya. Ketika penambang berhasil menemukan sebuah blok menggunakan Public Pool, mereka akan menerima reward blok secara utuh beserta seluruh biaya transaksi yang terkait, tanpa potongan biaya operasional pool. Hal ini sangat berbeda dengan pool mining tradisional yang biasanya mengenakan biaya mulai dari 1-3% dari reward mining. Model tanpa biaya ini membuat Public Pool sangat menarik bagi para penambang yang ingin memaksimalkan potensi keuntungan mereka dengan tetap memegang kendali penuh atas operasi mining mereka.


Untuk memahami posisi unik Public Pool, penting untuk memahami perbedaan mendasar antara solo mining dan pooled mining. mining solo yang sebenarnya berarti Anda menambang secara mandiri dan menerima upah blok penuh (saat ini 3,125 BTC + biaya) jika Anda menemukan blok, tetapi probabilitasnya sebanding dengan tingkat hash Anda dibandingkan dengan seluruh jaringan - menciptakan varians ekstrem yang dapat berlangsung selama berbulan-bulan atau bertahun-tahun di antara upah. Pool tradisional menggabungkan kekuatan hash untuk menemukan blok lebih sering, mendistribusikan reward secara proporsional dan memberikan pendapatan yang stabil dan dapat diprediksi. Untuk penambang dengan modal yang signifikan yang diinvestasikan dalam perangkat keras dan biaya operasional, mining solo murni biasanya tidak praktis terlepas dari keuntungan filosofisnya - variansnya membuat hampir tidak mungkin untuk menutupi biaya listrik dan memulihkan investasi. Realitas ekonomi ini berarti sebagian besar penambang akan memilih mining gabungan untuk alasan keuangan praktis. Public Pool beroperasi sebagai pool mining tunggal, yang berarti Anda masih menghadapi varians mining tunggal (Anda hanya mendapatkan imbalan ketika Anda menemukan blok secara pribadi), tetapi Anda mendapatkan keuntungan dari infrastruktur pool dan operasi tanpa biaya yang transparan.


### Keuntungan Open Source dan Implementasi Teknis


Komitmen Public Pool terhadap pengembangan sumber terbuka memberikan para penambang transparansi dan kontrol yang belum pernah ada sebelumnya terhadap operasi mining mereka. Seluruh basis kode tersedia di GitHub, memungkinkan para penambang untuk memeriksa dengan tepat bagaimana perangkat lunak beroperasi, memodifikasinya sesuai dengan kebutuhan mereka, dan bahkan berkontribusi pada pengembangannya. Transparansi ini menjawab kekhawatiran yang signifikan dalam komunitas mining mengenai konfigurasi dan praktik yang tidak diketahui dari pool mining tradisional.


Arsitektur perangkat lunak mencakup fungsionalitas inti pool mining dan repositori antarmuka pengguna yang terpisah, yang keduanya tersedia secara bebas untuk diunduh dan dimodifikasi. Penambang dapat menjalankan Public Pool dalam berbagai konfigurasi, termasuk kontainer Docker, membuatnya dapat beradaptasi dengan pengaturan perangkat keras dan preferensi teknis yang berbeda. Dokumentasi komprehensif yang disediakan di repositori GitHub menawarkan panduan instalasi yang mendetail, opsi konfigurasi, dan instruksi modifikasi, sehingga dapat diakses oleh para penambang dengan berbagai tingkat keahlian teknis.


Menghubungkan ke Public Pool membutuhkan konfigurasi minimal dibandingkan dengan pengaturan mining tradisional. Para penambang hanya perlu mengonfigurasi perangkat mining mereka dengan detail koneksi Stratum dan memberikan alamat Bitcoin mereka sebagai nama pengguna. Nama pekerja opsional dapat ditambahkan setelah pemisah titik untuk tujuan organisasi.


### Fitur Komunitas dan Model Keberlanjutan


Public Pool menggabungkan beberapa fitur inovatif yang memperkuat komunitas Bitcoin mining sambil mempertahankan operasi tanpa biaya. Platform ini menampilkan statistik yang komprehensif termasuk total hash rate dari penambang yang terhubung, yang biasanya berkisar antara 1 hingga 2 PetaHash per detik pada tahun 2024 dan sekitar 40 PH/detik pada bulan November 2025, dan memberikan informasi terperinci tentang perangkat mining yang terhubung. Yang paling penting adalah penekanan platform pada perangkat keras mining open-source, dengan perangkat yang ditandai dengan bintang yang menunjukkan desain open-source sepenuhnya, lengkap dengan tautan ke repositori GitHub masing-masing.


Keberlanjutan operasi tanpa biaya Public Pool bergantung pada kemitraan program afiliasi yang kreatif dengan vendor perangkat keras mining. Ketika para penambang membeli peralatan dari perusahaan mitra dengan menggunakan kode diskon "SOLO", lima puluh persen dari pendapatan afiliasi akan mendukung biaya operasional Public Pool, sementara lima puluh persen sisanya akan didistribusikan sebagai hadiah bagi para penambang yang mencapai tingkat kesulitan tertinggi setiap bulannya. Model ini menciptakan hubungan simbiosis mutualisme di mana para penambang mendapatkan diskon untuk pembelian peralatan, vendor mendapatkan pelanggan, dan Public Pool mempertahankan operasinya tanpa memungut biaya langsung.


### Filosofi Desentralisasi dan Praktik Terbaik


Meskipun Public Pool menawarkan alternatif yang sangat baik untuk pool mining tradisional, penting untuk memahami perannya dalam konteks desentralisasi Bitcoin yang lebih luas. Platform ini berfungsi sebagai batu loncatan menuju tujuan akhir penambang individu yang mengoperasikan pool mining mereka sendiri. Menjalankan pool mining Anda sendiri merupakan tingkat desentralisasi tertinggi, karena menghilangkan ketergantungan pada infrastruktur atau perangkat lunak pihak ketiga, terlepas dari seberapa transparan atau bermaksud baik pihak ketiga tersebut.


Sifat Public Pool yang open-source menjadikannya sebagai platform pembelajaran yang ideal bagi para penambang yang ingin memahami operasi pool sebelum mengimplementasikan solusi mereka sendiri. Ketersediaan panduan instalasi untuk berbagai sistem operasi dan dokumentasi yang komprehensif memberikan para penambang pengetahuan yang dibutuhkan untuk bertransisi dari penggunaan Public Pool ke pengoperasian infrastruktur mining mereka sendiri. Aspek edukasi ini selaras dengan prinsip-prinsip fundamental Bitcoin tentang kedaulatan dan desentralisasi, memberdayakan para penambang individu untuk mengambil kendali penuh atas operasi mining mereka sambil berkontribusi pada keamanan dan desentralisasi jaringan Bitcoin secara keseluruhan.


Antarmuka pengguna platform ini memberikan penambang kemampuan pemantauan yang terperinci, termasuk status pekerja, statistik tingkat hash, dan metrik kinerja. Fitur-fitur ini membantu para penambang mengoptimalkan operasi mereka sambil mempelajari prinsip-prinsip manajemen pool yang nantinya dapat mereka terapkan pada implementasi pool mining mereka sendiri.


## Cara memasang Public-Pool di Umbrel

<chapterId>7f6d0307-7715-5581-89ea-f13cf8754f9a</chapterId>


:::video id=3a4fe0a9-bbf5-458a-8ec1-52c3b83afd87:::

Menjalankan kolam renang Bitcoin mining Anda sendiri di rumah menjadi semakin mudah diakses dengan perangkat keras modern dan solusi perangkat lunak yang disederhanakan. Bab ini membahas implementasi praktis dari kolam renang umum berbasis rumah menggunakan perangkat keras PC mini yang terjangkau dan perangkat lunak manajemen node yang disederhanakan. Pada akhir panduan ini, Anda akan memahami persyaratan perangkat keras, proses penyiapan perangkat lunak, dan konfigurasi dasar yang diperlukan untuk membangun infrastruktur kolam renang mining Anda sendiri.


### Persyaratan dan Pengaturan Perangkat Keras


Fondasi dari setiap pengaturan pool mining di rumah dimulai dengan memilih perangkat keras yang sesuai yang menyeimbangkan kinerja, biaya, dan efisiensi energi. PC mini merupakan solusi ideal untuk aplikasi ini, menawarkan daya pemrosesan yang cukup sekaligus mempertahankan jejak yang ringkas dan konsumsi daya yang wajar. Konfigurasi yang disarankan mencakup prosesor Intel N100, yang menyediakan sumber daya komputasi yang memadai untuk operasi pool, dipasangkan dengan setidaknya satu terabyte penyimpanan NVMe untuk mengakomodasi blockchain Bitcoin dan data terkait.


Persyaratan penyimpanan sangat penting karena menjalankan pool mining memerlukan pemeliharaan node Bitcoin yang tersinkronisasi sepenuhnya. Drive NVMe satu terabyte memastikan operasi baca/tulis yang cepat, yang penting untuk sinkronisasi blockchain dan pemrosesan transaksi yang sedang berlangsung. Selain itu, alokasi RAM yang memadai mendukung kelancaran operasi sistem operasi Linux yang mendasari dan perangkat lunak manajemen node yang akan mengoordinasikan aktivitas pool.


### Arsitektur Perangkat Lunak dan Manajemen Node


Tumpukan perangkat lunak untuk kumpulan mining rumahan dibangun di atas fondasi Linux, memberikan stabilitas dan keamanan yang diperlukan untuk operasi Bitcoin. Di atas sistem dasar ini, perangkat lunak manajemen node khusus seperti Umbrel menciptakan antarmuka yang intuitif untuk mengelola infrastruktur Bitcoin. Pendekatan ini mengabstraksikan banyak kerumitan yang secara tradisional terkait dengan menjalankan node Bitcoin, membuat operasi pool dapat diakses oleh pengguna tanpa latar belakang teknis yang luas.


Umbrel berfungsi sebagai platform manajemen node yang komprehensif yang menangani instalasi, sinkronisasi, dan pemeliharaan Bitcoin Core yang sedang berlangsung melalui antarmuka berbasis web. Model toko aplikasi platform ini memungkinkan pemasangan layanan tambahan yang mudah, termasuk perangkat lunak kumpulan mining, melalui operasi tunjuk-dan-klik yang sederhana. Arsitektur ini memastikan bahwa pengguna dapat fokus pada operasi pool daripada administrasi sistem, sambil tetap mempertahankan kontrol penuh atas infrastruktur Bitcoin mereka.


### Instalasi dan Konfigurasi Kolam Renang Umum


Menginstal perangkat lunak kolam renang umum melalui platform Umbrel menunjukkan sifat ramping dari penyebaran infrastruktur Bitcoin modern. Prosesnya dimulai dengan mengakses toko aplikasi Umbrel melalui antarmuka web, di mana pencarian sederhana untuk "kolam renang umum" akan menampilkan perangkat lunak kolam renang mining yang tersedia. Instalasi hanya membutuhkan beberapa klik: memilih aplikasi, mengonfirmasi instalasi, dan menunggu proses penyiapan otomatis selesai.


Proses instalasi secara otomatis mengkonfigurasi koneksi yang diperlukan antara perangkat lunak pool publik dan node Bitcoin yang mendasarinya. Integrasi ini memastikan bahwa pool dapat memvalidasi transaksi, membuat template blok, dan mendistribusikan pekerjaan ke penambang yang terhubung tanpa memerlukan konfigurasi manual dari parameter jaringan yang kompleks. Setelah instalasi selesai, antarmuka pool dapat langsung diakses melalui jaringan lokal, memberikan kemampuan pemantauan dan manajemen secara real-time.


### Menghubungkan Penambang dan Pertimbangan Jaringan


Menghubungkan perangkat keras mining ke pool yang baru saja dibuat membutuhkan konfigurasi pengaturan pool penambang untuk mengarahkan ke infrastruktur lokal Anda. Hal ini melibatkan penggantian alamat pool default dengan alamat IP lokal Anda dan nomor port yang sesuai yang ditetapkan selama instalasi pool publik. Perubahan konfigurasi akan mengalihkan upaya komputasi perangkat keras mining Anda dari pool eksternal ke infrastruktur berbasis rumah Anda, sehingga Anda dapat mempertahankan kontrol penuh atas operasi mining dan potensi reward.


Konfigurasi jaringan memainkan peran penting dalam aksesibilitas dan fungsionalitas pool. Pengaturan jaringan lokal biasanya melibatkan pengalamatan IP standar, tetapi pengguna dapat menemukan variasi dalam resolusi DNS tergantung pada konfigurasi router mereka. Beberapa router menyediakan layanan DNS lokal yang membuat nama yang ramah untuk layanan lokal, sementara yang lain memerlukan akses alamat IP langsung. Untuk akses yang lebih luas di luar jaringan lokal, konfigurasi port forwarding pada router mungkin diperlukan, meskipun hal ini menimbulkan pertimbangan keamanan tambahan yang memerlukan evaluasi yang cermat terhadap risiko dan manfaat yang terkait.


Keberhasilan pembentukan pool mining rumahan merupakan langkah signifikan menuju infrastruktur Bitcoin yang terdesentralisasi, yang memberikan nilai edukasi dan kemampuan mining yang praktis sambil mempertahankan kendali penuh atas operasi Bitcoin Anda.


# Perakitan dan Pemecahan Masalah Perangkat Keras

<partId>f6987088-5ba4-52e2-b2d0-aa122080940c</partId>


## Alat apa yang digunakan?

<chapterId>733935b5-0171-5a22-838c-e192df6f7ccf</chapterId>


:::video id=bddd0e47-7b43-4685-ba2e-bf3a8ff653c9:::

Dalam dunia penyolderan perangkat pemasangan permukaan (SMD), terutama ketika bekerja dengan proyek Bitaxe, memiliki peralatan yang tepat membuat perbedaan antara frustrasi dan kesuksesan. Panduan komprehensif ini mencakup peralatan penting yang diperlukan untuk menangani proyek penyolderan SMD secara efektif, mulai dari perkakas tangan dasar hingga peralatan khusus yang akan meningkatkan kemampuan penyolderan Anda.


Jika Anda ingin merujuk ke beberapa dokumentasi tentang skema, periksa [repo GitHub](https://github.com/skot/bitaxe-doc/tree/main).


### Perkakas Tangan Dasar dan Instrumen Presisi


Dasar dari setiap penyolderan SMD dimulai dengan pinset berkualitas, yang berfungsi sebagai alat penempatan komponen utama Anda. Dua jenis pinset terbukti paling berharga dalam pekerjaan ini: pinset berujung lurus standar dan pinset dengan sedikit lengkungan di ujungnya. Variasi ujung lurus menangani sebagian besar komponen SMD yang ditemukan dalam kit Bitaxe pada umumnya, sedangkan pinset dengan ujung bengkok lebih unggul ketika bekerja dengan komponen yang sangat kecil yang memerlukan pemosisian yang tepat. Alat-alat ini sering kali disertakan dengan kit perbaikan, seperti set iFixit yang dirancang untuk perbaikan ponsel, sehingga mudah diakses oleh sebagian besar penggemar.


Melengkapi pinset, gunting yang bagus menjadi sangat diperlukan untuk memotong pita listrik, yang memiliki banyak fungsi dalam proyek elektronik. Selotip listrik menyediakan isolasi penting untuk kabel dan komponen, dan memiliki selotip berkualitas yang sudah tersedia akan menyederhanakan proses penyolderan. Persediaan dasar ini dapat diperoleh dari toko perangkat keras atau pengecer online tanpa memerlukan pemasok elektronik khusus.


### Aplikasi dan Manajemen Pasta Solder


Penerapan pasta solder merupakan salah satu aspek paling penting dari penyolderan SMD, dan alat yang tepat membuat proses ini akurat dan menyenangkan. Jarum suntik kecil dan tidak tajam yang diisi dengan pasta solder memberikan kontrol yang luar biasa atas penempatan pasta. Metode ini memungkinkan aplikasi yang tepat dari jumlah pasta solder yang tepat yang dibutuhkan untuk setiap sambungan, dan kebanyakan orang dengan cepat mengembangkan teknik yang tepat untuk mengontrol tekanan dan laju aliran melalui praktik langsung.


Pilihan pasta solder itu sendiri secara signifikan berdampak pada keberhasilan penyolderan. ChipQuik TS391SNL50 menonjol sebagai pasta solder yang luar biasa untuk proyek Bitaxe dan pekerjaan SMD umum. Pasta ini mempertahankan konsistensi dan karakteristik peleburan yang tepat, menghindari masalah yang terkait dengan alternatif yang lebih murah yang memiliki titik leleh yang terlalu rendah. Pasta solder berkualitas rendah dapat menimbulkan masalah di mana sambungan yang sebelumnya disolder menjadi cair kembali saat memanaskan area yang berdekatan, yang menyebabkan perpindahan komponen dan koneksi yang buruk. Meskipun pasta solder berkualitas mewakili investasi awal yang lebih tinggi, hasil yang lebih baik dan berkurangnya rasa frustrasi membenarkan biaya yang dikeluarkan.


### Alat Bantu Pemecahan Masalah dan Pembersihan


Bahkan para penyolder yang berpengalaman pun mengalami masalah yang memerlukan koreksi, sehingga peralatan pematrian sangat penting untuk toolkit yang lengkap. Peralatan pematrian, pada dasarnya adalah alat vakum yang dipanaskan, menghilangkan kelebihan solder dan mengoreksi sambungan yang tidak terhubung di antara pin komponen. Alat-alat ini bekerja paling efektif bila dikombinasikan dengan fluks, yang meningkatkan aliran solder dan membantu proses pematrian bekerja lebih efisien.


Fluks tersedia dalam berbagai bentuk, termasuk jenis padat dan cair, dan memiliki banyak tujuan selain bantuan pematrian. Ketika pasta solder mulai kehilangan keefektifannya selama sesi kerja yang lama, menerapkan fluks tambahan akan mengembalikan karakteristik aliran yang tepat dan memastikan koneksi yang andal. Alat seperti sendok kecil, yang sering ditemukan dalam kit perbaikan presisi, memfasilitasi aplikasi fluks yang akurat ke area tertentu tanpa mencemari komponen di sekitarnya.


Pembersihan papan merupakan langkah terakhir dalam pekerjaan berkualitas profesional, yang membutuhkan alkohol isopropanol dan sikat pembersih khusus. Sikat gigi bekas dapat digunakan dengan sempurna untuk tujuan ini, dan botol pemerasan yang berisi isopropanol memungkinkan aplikasi larutan pembersih yang terkontrol. Kombinasi ini menghilangkan residu fluks dan sisa-sisa pasta, sehingga papan terlihat bersih dan profesional yang juga memudahkan pemeriksaan sambungan solder.


### Peralatan Khusus dan Peralatan Canggih


Untuk proyek yang melibatkan sirkuit terpadu yang kompleks, khususnya ASIC, stensil mengubah proses penyolderan dari penempatan tangan yang membosankan menjadi aplikasi pasta yang efisien dan akurat. Templat yang dipotong secara presisi ini memastikan ketebalan dan penempatan pasta yang konsisten, secara dramatis mengurangi waktu yang diperlukan untuk komponen yang kompleks sekaligus meningkatkan keandalan. Investasi dalam stensil berkualitas membayar dividen dalam penghematan waktu dan hasil yang lebih baik.


Manajemen termal menjadi sangat penting ketika bekerja dengan komponen daya, membuat pasta termal atau pelumas termal menjadi persediaan yang penting. Bahan-bahan ini memastikan perpindahan panas yang tepat antara heat sink dan sirkuit terpadu, mencegah kerusakan termal dan memastikan pengoperasian yang andal. Bahan antarmuka termal berkualitas merupakan investasi kecil yang melindungi komponen yang jauh lebih mahal.


Inti dari pengaturan penyolderan SMD adalah stasiun pengerjaan ulang udara panas, yang menyediakan panas terkontrol yang diperlukan untuk pekerjaan pemasangan di permukaan. Meskipun stasiun anggaran dalam kisaran $ 30-50 dapat berkinerja memadai, mereka sering kali tidak memiliki keandalan dan ketepatan peralatan kelas atas. Stasiun tingkat pemula ini biasanya beroperasi secara efektif pada suhu 355°C dan mencakup pengurangan suhu otomatis ketika alat genggam dikembalikan ke dudukannya. Namun, keandalannya tidak konsisten, dengan beberapa unit yang mengalami kerusakan sebelum waktunya. Untuk pekerjaan yang serius, berinvestasi pada peralatan berkualitas lebih tinggi dari pemasok elektronik khusus akan memberikan nilai jangka panjang yang lebih baik melalui peningkatan keandalan dan kontrol suhu yang lebih tepat.


Kombinasi alat ini menciptakan kemampuan penyolderan SMD lengkap yang jauh melampaui proyek Bitaxe hingga pekerjaan elektronik umum. Memahami peran masing-masing alat dan memilih peralatan berkualitas yang sesuai dengan tingkat keahlian dan persyaratan proyek Anda memastikan hasil yang sukses dan pengalaman menyolder yang menyenangkan.



## Memperbaiki masalah solder

<chapterId>96663744-b4f7-5154-930f-a68ba7954603</chapterId>


:::video id=9286c0dc-acd6-44d9-b34e-59cfb2da9748:::


Kit transceiver Bitaxe menghadirkan tantangan unik selama perakitan yang memerlukan perhatian yang cermat terhadap orientasi komponen, pencegahan jembatan solder, dan manajemen panas yang tepat. Memahami masalah umum ini dan solusinya sangat penting untuk konstruksi kit yang sukses dan menghindari kerusakan komponen yang mahal. Bab ini membahas masalah penyolderan yang paling sering dijumpai selama perakitan Bitaxe dan memberikan teknik praktis untuk mengidentifikasi dan mengatasinya.


### Orientasi dan Identifikasi Komponen


Orientasi komponen yang tepat merupakan salah satu aspek yang paling penting dalam perakitan Bitaxe yang sukses, khususnya dengan MOSFET Q1 dan Q2. Komponen-komponen ini memiliki penanda orientasi khas yang harus diperhatikan dengan cermat selama pemasangan. Setiap MOSFET berisi tanda titik kecil yang sesuai dengan pengaturan pad tertentu pada papan sirkuit. Kunci untuk orientasi yang benar terletak pada pemahaman struktur fisik komponen ini, yang memiliki empat pin yang disusun dengan satu pad besar dan tiga pad kecil yang tidak memiliki koneksi ke pad besar.


Apabila memasang Q1 dan Q2, periksa komponen dan papan sirkuit secara cermat. Tata letak papan dengan jelas menunjukkan orientasi yang diinginkan melalui konfigurasi pad, dengan empat pin diposisikan agar sesuai dengan struktur MOSFET. Sebelum menyolder komponen besar apa pun, selalu verifikasi orientasi dengan membandingkan penanda fisik komponen dengan susunan pad papan. Langkah verifikasi sederhana ini mencegah frustrasi karena harus mematahkan dan memasang kembali komponen yang salah orientasi.


Konsekuensi dari orientasi yang salah lebih dari sekadar masalah fungsionalitas. MOSFET yang salah orientasi dapat menyebabkan kerusakan sirkuit yang sulit didiagnosis dan mungkin memerlukan penggantian komponen secara menyeluruh. Meluangkan waktu untuk memverifikasi orientasi sebelum menerapkan panas memastikan operasi sirkuit yang tepat dan mencegah pemecahan masalah yang tidak perlu di kemudian hari dalam proses perakitan.


### Mengelola Jembatan Solder dan Solder Berlebih


Jembatan solder merupakan tantangan umum lainnya dalam perakitan Bitaxe, terutama di sekitar komponen bernada halus seperti U10. Sambungan yang tidak diinginkan antara pin yang berdekatan ini dapat menyebabkan kerusakan sirkuit dan memerlukan teknik pelepasan yang hati-hati. Pendekatan yang paling efektif adalah dengan menggunakan sumbu pematrian, bahan jalinan tembaga yang menyerap kelebihan solder ketika dipanaskan. Teknik ini membutuhkan kesabaran dan pemilihan alat yang tepat untuk menghindari kerusakan komponen yang sensitif.


Saat menangani jembatan solder pada sirkuit terpadu, gunakan penahan PCB atau penjepit yang diartikulasikan untuk menahan komponen dengan aman saat bekerja. Terapkan panas yang lembut pada area yang terkena dan tarik sumbu pematrian dengan hati-hati pada sambungan yang dijembatani. Jalinan tembaga secara alami menyerap kelebihan solder, memisahkan sambungan yang tidak diinginkan. Proses ini mungkin memerlukan beberapa kali percobaan, tetapi ketekunan akan menghasilkan sambungan yang bersih dan terpisah dengan benar.


Pencegahan tetap merupakan pendekatan terbaik untuk manajemen jembatan solder. Menggunakan pasta solder dalam jumlah yang tepat dan mempertahankan kontrol tangan yang stabil selama penempatan komponen secara signifikan mengurangi pembentukan jembatan. Ketika jembatan terjadi, segera atasi daripada berharap jembatan tidak akan mempengaruhi operasi sirkuit. Bahkan jembatan yang tampaknya kecil dapat menyebabkan masalah fungsionalitas yang signifikan yang sulit didiagnosis setelah papan dirakit sepenuhnya.


### Komponen Penting dan Pertimbangan Khusus


Konverter buck U9 perlu mendapat perhatian khusus karena perannya yang sangat penting dalam mengubah 5 volt menjadi 1,2 volt untuk chip ASIC. Komponen ini menghadirkan tantangan unik karena lima koneksi kecil dan kecenderungan kegagalan. Pemasangan yang tepat membutuhkan aplikasi pasta solder yang tepat dan manajemen panas yang cermat. Pasta solder yang tidak mencukupi di bawah U9 dapat mengakibatkan koneksi yang buruk yang mencegah konversi tegangan yang tepat, sementara pasta yang berlebihan dapat membuat jembatan yang menyebabkan kerusakan sirkuit.


U9 menghasilkan tanda tangan audio yang khas ketika mengalami masalah jembatan solder, menghasilkan suara frekuensi tinggi yang berbeda dari pengoperasian ASIC yang normal. Teknik diagnostik pendengaran ini dapat membantu mengidentifikasi masalah, meskipun memerlukan pendengaran frekuensi tinggi yang baik untuk mendeteksi. Jika diagnosis audio tidak memungkinkan, inspeksi visual menjadi penting. Periksa semua koneksi dengan hati-hati, cari jembatan atau cakupan solder yang tidak memadai.


Jika U9 gagal menghasilkan output 1,2 volt yang diperlukan meskipun terlihat disolder dengan benar, pertimbangkan pasta solder yang tidak mencukupi sebagai penyebabnya. Lepaskan komponen, oleskan sedikit pasta solder tambahan, dan pasang kembali. Dalam kasus di mana masing-masing pin tidak memiliki cakupan solder yang memadai, oleskan sedikit pasta solder dengan hati-hati ke lokasi tertentu dengan menggunakan pinset. Pasta solder secara alami akan mengalir di bawah komponen saat dipanaskan, menciptakan sambungan yang tepat melalui aksi kapiler.


### Manajemen Panas dan Perlindungan Komponen


Manajemen panas yang tepat melindungi komponen sensitif dari kerusakan termal sekaligus memastikan sambungan solder yang andal. Komponen seperti osilator kristal Y1 dan U1 sangat sensitif terhadap paparan panas dalam waktu lama dan memerlukan kontrol suhu yang cermat. Pertahankan suhu besi solder pada 350 derajat Celcius, tetapi minimalkan waktu aplikasi panas untuk mencegah kerusakan komponen. Teknik penyolderan yang cepat dan efisien melindungi komponen sensitif ini sekaligus menghasilkan koneksi yang andal.


Chip ASIC memerlukan teknik penanganan khusus karena struktur pin yang kompleks dan sensitivitasnya terhadap tekanan mekanis. Saat menggunakan stensil untuk aplikasi pasta solder, pastikan cakupan yang merata di semua pin untuk mencegah penempatan komponen yang tidak rata. Jika pasta solder yang berlebihan menyebabkan ASIC tidak terpasang dengan rata, biarkan rakitan mendingin sepenuhnya sebelum melakukan koreksi. Berikan tekanan lembut hanya pada tepi komponen yang berlabel, jangan pernah ke area cetakan tengah, saat memanaskan ulang untuk mendapatkan posisi yang tepat.


Komponen U8 menghadirkan tantangan unik karena banyaknya pin dan potensi kabel yang tertekuk. Apabila pin tertekuk selama penanganan, gunakan penahan PCB atau penjepit artikulasi untuk mengamankan komponen dan luruskan pin yang terpengaruh dengan hati-hati. Bekerjalah secara perlahan dan sabar untuk menghindari putusnya kabel yang halus. Memahami bahwa kelompok pin tertentu pada U8 terhubung secara internal dapat menyederhanakan pemecahan masalah, karena jembatan di antara pin tertentu ini tidak memengaruhi operasi sirkuit. Namun, jembatan antara pin lain memerlukan pelepasan yang hati-hati untuk memastikan fungsionalitas yang tepat.


## Cara men-debug Bitaxe Anda menggunakan AxeOS

<chapterId>603f5c0d-4b7c-51e1-9bad-318a8b8e9db7</chapterId>

:::video id=d23d748b-510e-4748-9617-b875da757031:::

Ketika bekerja dengan perangkat Bitaxe mining, kegagalan perangkat keras dapat muncul dalam berbagai cara yang mungkin tidak langsung terlihat. Memahami cara mendiagnosis masalah ini secara sistematis menggunakan sistem operasi AxeOS dapat menghemat waktu yang signifikan dan mencegah penggantian komponen yang tidak perlu. Bab ini membahas teknik diagnostik dan metodologi pemecahan masalah yang digunakan oleh teknisi berpengalaman untuk mengidentifikasi masalah perangkat keras tertentu melalui analisis perangkat lunak.


### Memahami Indikator Konsumsi Daya


Indikator diagnostik pertama dan paling penting dalam AxeOS adalah pemantauan konsumsi daya. Perangkat Bitaxe normal, termasuk model Bitaxe Ultra dan Bitaxe Supra, biasanya mengkonsumsi antara 10 hingga 17 watt selama pengoperasian standar. Pengukuran dasar ini berfungsi sebagai indikator kesehatan utama Anda untuk seluruh sistem. Ketika konsumsi daya turun secara signifikan di bawah kisaran ini, terutama di bawah 3 watt, hal ini menandakan adanya masalah mendasar pada chip ASIC atau sirkuit pendukungnya.


Skenario konsumsi daya yang rendah memerlukan perhatian segera karena mengindikasikan bahwa chip mining sama sekali tidak berfungsi atau beroperasi dalam kondisi yang sangat menurun. Pengukuran ini sendiri dapat membantu Anda dengan cepat membedakan antara masalah kinerja dan kegagalan perangkat keras sepenuhnya. Pembacaan daya di AxeOS memberikan umpan balik waktu nyata yang memungkinkan Anda untuk memantau keefektifan upaya perbaikan yang Anda lakukan pada perangkat.


### Menganalisis Pengukuran Tegangan ASIC


Fitur pengukuran tegangan ASIC di AxeOS memberikan informasi diagnostik penting yang membantu menentukan dengan tepat sifat masalah perangkat keras. Saat memeriksa pembacaan tegangan, Anda perlu memahami hubungan antara tegangan yang diukur dan tegangan yang diminta untuk mendiagnosis masalah dengan benar. Sistem menampilkan tegangan yang dikirim ke chip ASIC dan tegangan yang diminta oleh chip dari sistem manajemen daya.


Apabila Anda mengamati pengukuran tegangan ASIC tepat 1,2 volt yang dikombinasikan dengan konsumsi daya di bawah 3 watt, kombinasi spesifik ini mengindikasikan masalah penyolderan pada chip ASIC atau ASIC yang gagal total. Pembacaan tegangan ini menunjukkan bahwa daya mencapai lokasi chip, tetapi chip itu sendiri tidak berfungsi dengan baik. Pemeriksaan fisik die ASIC dapat menunjukkan adanya retakan atau kerusakan lain yang terlihat yang dapat menjelaskan pola perilaku ini.


Skenario diagnostik yang berbeda muncul ketika Anda melihat konsumsi daya yang rendah dipasangkan dengan pembacaan tegangan yang diminta sangat rendah, seperti 100 milivolt atau 0,5 volt. Pola ini menunjukkan bahwa chip ASIC tidak menerima suplai tegangan yang memadai, yang biasanya menunjukkan masalah pada komponen konverter buck U9. Konverter buck bertanggung jawab untuk menyediakan regulasi tegangan yang tepat yang dibutuhkan chip ASIC untuk pengoperasian yang tepat.


### Menafsirkan Data Log dan Komunikasi ASIC


Sistem pencatatan AxeOS memberikan wawasan yang berharga mengenai apakah chip ASIC Anda berkomunikasi dengan sistem kontrol. Ketika Anda mengakses log melalui fungsi "tampilkan log", keberadaan entri "hasil ASIC" menegaskan bahwa chip tidak hanya diberi daya tetapi juga secara aktif memproses pekerjaan dan mengembalikan hasil. Komunikasi ini menunjukkan bahwa ASIC disolder dengan benar dan mempertahankan koneksinya ke sirkuit kontrol.


Tidak adanya hasil ASIC dalam log, khususnya ketika dikombinasikan dengan gejala lain, membantu mempersempit masalah ke komponen tertentu atau masalah koneksi. Pendekatan diagnostik ini memungkinkan Anda untuk membedakan antara chip yang sama sekali tidak responsif dan chip yang mungkin memiliki masalah koneksi yang terputus-putus. Analisis log menjadi sangat berharga ketika memecahkan masalah yang kompleks di mana beberapa gejala mungkin menunjukkan akar penyebab yang berbeda.


### Pendekatan Pemecahan Masalah yang Sistematis


Ketika mendiagnosis masalah perangkat keras Bitaxe, mengikuti pendekatan sistematis mencegah pengabaian masalah kritis dan memastikan proses perbaikan yang efisien. Mulailah dengan mendokumentasikan konsumsi daya dan pembacaan voltase, kemudian hubungkan pengukuran ini dengan data log untuk membangun gambaran lengkap tentang perilaku sistem. Pendekatan metodis ini membantu mengidentifikasi apakah masalah berasal dari chip ASIC itu sendiri, sistem pengiriman daya, atau jalur komunikasi antar komponen.


Untuk kasus-kasus di mana konverter buck U9 tampaknya menjadi masalah, pemeriksaan fisik dan kemungkinan penyolderan ulang mungkin diperlukan. Komponen U9 sangat rentan terhadap masalah penyolderan, terutama dalam situasi perakitan pertama kali. Ketika masalah regulasi tegangan dicurigai, menggunakan multimeter untuk memverifikasi bahwa 1,2 volt benar-benar ada pada pin ASIC memberikan konfirmasi yang pasti tentang masalah pengiriman daya. Jika tegangan ada pada pin tetapi ASIC masih tidak berfungsi, dan pemeriksaan fisik menunjukkan tidak ada kerusakan, mengganti chip ASIC menjadi langkah logis berikutnya. Jika masalah masih berlanjut bahkan setelah penggantian ASIC, komponen U2, yang menggerakkan chip ASIC, mungkin memerlukan perhatian sebagai elemen terakhir dalam urutan pemecahan masalah.


## Bagaimana cara men-debug menggunakan USB?

<chapterId>f3182763-e1ef-5460-8bc0-f2ea53e3a410</chapterId>


:::video id=fe1b4b48-5f8a-4fd7-9417-ca03a36bce9f:::


Ketika memecahkan masalah perangkat Bitaxe mining, memiliki akses langsung ke sistem pencatatan internal perangkat akan memberikan wawasan yang tak ternilai yang tidak dapat ditawarkan oleh antarmuka berbasis web. Bab ini membahas cara membuat koneksi serial USB langsung ke perangkat Bitaxe Anda menggunakan kerangka kerja ESP-IDF, yang memungkinkan pemantauan log sistem, urutan booting, dan pesan kesalahan secara real-time. Pendekatan debugging ini sangat penting ketika menangani perangkat yang sering mengalami reboot atau kegagalan perangkat keras, karena dapat menangkap semua informasi diagnostik yang mungkin hilang selama restart sistem.


Proses debugging memerlukan Visual Studio Code dengan ekstensi ESP-IDF, meskipun IDE apa pun yang kompatibel dapat digunakan. Metode ini dapat digunakan pada semua varian Bitaxe yang memiliki port USB, termasuk Bitaxe Ultra 204 dan model lainnya dalam seri ini. Koneksi serial langsung melewati potensi keterbatasan antarmuka web dan menyediakan akses tanpa filter ke informasi status internal perangkat.


### Menyiapkan Komunikasi Serial


Membangun komunikasi dengan perangkat Bitaxe Anda dimulai dengan menghubungkan kabel USB dan membuka terminal ESP-IDF dalam lingkungan pengembangan Anda. Perintah `idf.py monitor` memulai proses koneksi, secara otomatis memindai port COM yang tersedia untuk membuat komunikasi UART dengan chip ESP32 pada perangkat Bitaxe Anda. Sistem biasanya melakukan siklus melalui port yang tersedia (COM3, COM4, COM16, dll.) sampai menemukan koneksi yang benar.


Setelah tersambung, terminal akan menampilkan urutan booting lengkap dan log operasional yang sedang berlangsung. Proses koneksi awal mungkin memerlukan waktu beberapa saat karena sistem mengidentifikasi port komunikasi yang benar. Jika deteksi port otomatis gagal, Anda dapat menentukan port COM secara manual melalui antarmuka pemilihan port IDE. Saluran komunikasi langsung ini tetap aktif selama perangkat beroperasi, sehingga memberikan akses berkelanjutan ke diagnostik sistem dan metrik kinerja.


### Menafsirkan Urutan Booting dan Log Operasi Normal


Urutan booting memberikan informasi penting tentang konfigurasi perangkat keras dan proses inisialisasi perangkat Bitaxe Anda. Log pengaktifan normal dimulai dengan informasi versi ESP-IDF, diikuti dengan pesan "Selamat datang di Bitaxe. Hack the planet" yang mengonfirmasi pemuatan firmware yang berhasil. Sistem kemudian menampilkan konfigurasi frekuensi ASIC, identifikasi model perangkat, dan detail versi board.


Perangkat yang berfungsi dengan baik akan menunjukkan inisialisasi I2C yang berhasil dan pengaturan tegangan ASIC yang diatur ke 1,2 volt. Log menampilkan informasi status GPIO dan urutan inisialisasi Wi-Fi, diikuti dengan konfigurasi server DHCP dan penetapan alamat IP. Salah satu indikator yang paling penting adalah pesan deteksi chip ASIC, yang seharusnya melaporkan "terdeteksi satu chip ASIC" untuk perangkat chip tunggal. Konfirmasi ini memvalidasi bahwa perangkat keras mining telah terhubung dengan benar dan berkomunikasi dengan pengontrol ESP32.


Log operasional mengungkapkan beberapa tugas bersamaan yang berjalan pada perangkat, termasuk komunikasi strata API, koordinasi tugas utama, manajemen tugas ASIC, dan pemrosesan tugas strata. Pengidentifikasi tugas yang berbeda ini membantu mengisolasi masalah pada komponen sistem tertentu. Operasi normal mencakup pembentukan koneksi pool, pesan penyesuaian kesulitan, antrian pekerjaan dan dequeuing, dan pelaporan pembuatan nonce. Operasi mining yang berhasil menampilkan hasil ASIC dengan perhitungan tingkat kesulitan dan mining mengirimkan konfirmasi ketika saham memenuhi ambang batas yang diperlukan.


### Mengidentifikasi Kegagalan Perangkat Keras dan Pola Kesalahan


Kegagalan perangkat keras termanifestasi dalam log melalui pola kesalahan tertentu yang menunjukkan komponen mana yang tidak berfungsi. Modus kegagalan yang paling umum adalah kesalahan komunikasi I2C dengan sirkuit terpadu tertentu pada papan Bitaxe. Sebagai contoh, kegagalan komunikasi DS4432U muncul sebagai pesan "ESP_ERROR_CHECK failed" dengan indikator waktu habis, yang menunjukkan masalah pengaturan tegangan atau masalah penyolderan yang mempengaruhi komponen U10 yang bertanggung jawab atas komunikasi tampilan.


Pesan kesalahan ini mencakup informasi debugging yang terperinci seperti file sumber tertentu (main_ds4432u.c), panggilan fungsi yang gagal, dan inti prosesor yang menangani tugas tersebut. Informasi penelusuran kembali memberikan konteks tambahan untuk pemecahan masalah tingkat lanjut. Pola kesalahan yang sama dapat terjadi pada chip kontrol suhu dan kipas EMC2101, masing-masing menghasilkan tanda tangan log yang berbeda yang membantu mengidentifikasi komponen yang gagal.


Masalah perangkat keras fisik sering kali muncul sebagai siklus kesalahan berulang yang diikuti dengan boot ulang sistem. Jika perangkat Anda mengeluarkan suara berisik selama pengoperasian, hal ini biasanya mengindikasikan masalah penyolderan seperti sambungan antar pin komponen atau sambungan solder yang tidak memadai. Meskipun masalah mekanis ini mungkin tidak selalu menjadi entri log spesifik generate, masalah ini menciptakan kondisi operasi yang tidak stabil yang bermanifestasi sebagai seringnya terjadi crash dan siklus restart pada output pemantauan.


### Strategi Pemecahan Masalah Tingkat Lanjut


Pemantauan serial memberikan beberapa keunggulan dibandingkan antarmuka debugging berbasis web, terutama untuk kegagalan intermiten atau perangkat yang sering mengalami reboot. Pengambilan log secara terus menerus memastikan bahwa tidak ada informasi diagnostik yang hilang selama restart sistem, tidak seperti antarmuka web yang mungkin kehilangan data selama peristiwa pemutusan sambungan. Kemampuan pencatatan yang komprehensif ini memungkinkan untuk mengidentifikasi pola kegagalan dan menghubungkan kondisi kesalahan tertentu dengan perangkat keras atau faktor lingkungan.


Saat menganalisis perangkat yang bermasalah, fokuslah pada urutan kejadian yang menyebabkan kegagalan daripada pesan kesalahan yang terisolasi. Komunikasi ASIC yang berhasil harus menunjukkan pemrosesan pekerjaan yang teratur, pembuatan nonce, dan siklus pengiriman berbagi. Hasil ASIC yang hilang dalam log menunjukkan kegagalan komunikasi antara ESP32 dan chip mining, yang sering kali disebabkan oleh masalah catu daya, jejak yang rusak, atau kegagalan komponen.


Untuk pemecahan masalah yang sistematis, dokumentasikan pola kesalahan dan kegagalan spesifik komponen sebelum mencari dukungan komunitas. Log kesalahan yang terperinci, termasuk pengidentifikasi chip dan mode kegagalan tertentu, memungkinkan pengguna yang berpengalaman untuk memberikan panduan perbaikan yang ditargetkan, seperti prosedur penggantian komponen atau koreksi penyolderan. Pendekatan metodis untuk debugging perangkat keras ini secara signifikan meningkatkan tingkat keberhasilan perbaikan dan mengurangi waktu pemecahan masalah untuk masalah yang kompleks.


# Kustomisasi Tingkat Lanjut

<partId>8d333102-ecb5-5f05-bfb5-03a27b2d0d70</partId>


## Memodifikasi PCB

<chapterId>ca08d2a4-2b34-575b-aecc-7482a03c190e</chapterId>


:::video id=30fb0010-f560-4e96-a05b-c21dc172746e:::

KiCad merupakan salah satu alat bantu sumber terbuka yang paling kuat yang tersedia untuk desain dan perutean papan sirkuit tercetak (PCB). Perangkat lunak kelas profesional ini memungkinkan para insinyur dan penghobi untuk membuat desain elektronik yang rumit dengan menempatkan komponen pada papan virtual dan merutekan jalur rumit yang menghubungkan komponen-komponen tersebut. Apa yang membuat KiCad sangat berharga untuk tujuan pendidikan dan pengembangan adalah sifat sumber terbuka yang lengkap, memungkinkan pengguna untuk memodifikasi, menyesuaikan, dan belajar dari desain yang ada tanpa batasan lisensi.


Proyek Bitaxe mencontohkan kekuatan pengembangan perangkat keras sumber terbuka, menyediakan desain PCB lengkap yang dapat diperiksa, dimodifikasi, dan disesuaikan oleh pengguna sesuai dengan kebutuhan spesifik mereka. Aksesibilitas ini menciptakan lingkungan pembelajaran yang sangat baik di mana siswa dan praktisi dapat menjelajahi desain PCB dunia nyata sambil mengembangkan pemahaman mereka tentang sistem elektronik. Kemampuan untuk menyesuaikan elemen visual seperti logo memberikan titik masuk yang mudah didekati bagi pengguna yang mungkin terintimidasi oleh kerumitan teknis desain elektronik.


### Menyiapkan Lingkungan KiCad Anda


Sebelum memulai pekerjaan kustomisasi, pengaturan yang tepat untuk lingkungan pengembangan Anda sangatlah penting. Repositori Bitaxe harus diunduh ke mesin lokal Anda, biasanya dilakukan melalui fungsionalitas pengunduhan ZIP GitHub. Repositori ini berisi semua file proyek yang diperlukan, termasuk file proyek KiCad, pustaka komponen, dan dokumentasi desain yang diperlukan untuk modifikasi yang berhasil.


Instalasi KiCad harus dilakukan dengan menggunakan distribusi resmi dari situs web KiCad, untuk memastikan kompatibilitas dengan file proyek dan akses ke fitur-fitur terbaru. Setelah repositori dan KiCad terinstal dengan benar, membuka proyek memerlukan navigasi ke file proyek Bitaxe Ultra KiCad di dalam struktur repositori yang telah diunduh. File proyek ini berfungsi sebagai pusat penghubung yang menghubungkan semua file desain, pustaka komponen, dan pengaturan konfigurasi yang terkait.


Tampilan awal desain PCB yang kompleks dapat tampak luar biasa, dengan banyak komponen, jejak, dan lapisan yang menciptakan lanskap visual yang padat. Namun, fungsionalitas penampil 3D KiCad menyediakan alat yang sangat berharga untuk memahami tata letak fisik dan hubungan spasial dalam desain. Perspektif tiga dimensi ini mengubah representasi skematik abstrak menjadi visualisasi realistis dari produk akhir yang diproduksi, membuatnya lebih mudah untuk memahami penempatan komponen dan estetika desain secara keseluruhan.


### Proses Kustomisasi Logo


Menyesuaikan logo pada desain PCB merupakan salah satu modifikasi yang paling mudah diakses oleh pengguna yang baru mengenal KiCad, yang membutuhkan pengetahuan teknis minimal sekaligus memberikan hasil visual langsung. Prosesnya dimulai dengan alat konverter gambar, yang mengubah file gambar standar menjadi format footprint yang kompatibel dengan perangkat lunak desain PCB. Proses konversi ini membutuhkan perhatian yang cermat terhadap parameter ukuran, biasanya diukur dalam milimeter untuk memastikan penskalaan yang tepat pada papan akhir yang diproduksi.


Alur kerja konverter gambar melibatkan beberapa langkah penting yang menentukan tampilan akhir dan penempatan logo kustom. Pemilihan gambar sumber harus memprioritaskan desain dengan kontras tinggi yang akan diterjemahkan dengan baik ke proses pencetakan silkscreen yang digunakan dalam pembuatan PCB. Spesifikasi ukuran menjadi sangat penting, karena logo harus cukup besar agar tetap terbaca setelah diproduksi tanpa mengganggu penempatan atau fungsionalitas komponen. Pilihan antara lapisan silkscreen depan dan belakang memengaruhi visibilitas dan pertimbangan manufaktur.


Manajemen footprint library merupakan aspek fundamental dari kustomisasi KiCad, yang mengharuskan pengguna untuk memahami bagaimana perangkat lunak ini mengatur dan mengakses elemen-elemen desain. Menambahkan logo kustom melibatkan pembuatan footprint library baru atau memodifikasi yang sudah ada, kemudian menautkan library ini dengan benar di dalam struktur proyek. Proses ini memastikan bahwa elemen kustom tetap dapat diakses di berbagai sesi desain dan dapat dengan mudah dibagikan dengan anggota tim atau kolaborator lain.


### Eksplorasi dan Pemahaman Desain Tingkat Lanjut


Di luar kustomisasi logo yang sederhana, KiCad menyediakan alat bantu yang kuat untuk mengeksplorasi dan memahami desain PCB yang kompleks. Sistem manajemen lapisan memungkinkan pengguna untuk secara selektif melihat berbagai aspek desain, mulai dari penempatan komponen dan perutean hingga spesifikasi manufaktur dan informasi perakitan. Pendekatan berlapis ini memungkinkan analisis terperinci dari elemen desain tertentu tanpa kekacauan visual dari komponen yang tidak terkait.


Analisis penelusuran jejak merupakan salah satu aspek yang paling mendidik dari eksplorasi PCB, yang mengungkapkan bagaimana koneksi listrik mengalir di antara komponen dan subsistem. Dengan mengikuti jejak individu atau kelompok sinyal terkait, pengguna dapat mengembangkan pemahaman tentang fungsionalitas sirkuit dan keputusan desain. Sebagai contoh, memeriksa jaringan distribusi daya mengungkapkan bagaimana regulasi tegangan dan komponen penyaringan bekerja bersama untuk memberikan daya yang bersih dan stabil ke komponen elektronik yang sensitif.


Hubungan antara desain skematik dan tata letak fisik menjadi jelas melalui pemeriksaan yang cermat terhadap penempatan komponen dan keputusan perutean. Memahami mengapa komponen tertentu diposisikan di lokasi tertentu, bagaimana pertimbangan termal memengaruhi keputusan tata letak, dan bagaimana persyaratan integritas sinyal mendorong pilihan perutean memberikan wawasan yang berharga ke dalam praktik desain PCB profesional. Pengetahuan ini terbukti sangat berharga bagi pengguna yang mengembangkan desain mereka sendiri atau memodifikasi desain yang sudah ada untuk aplikasi tertentu.


Alat bantu pemeriksaan dan verifikasi aturan desain KiCad yang komprehensif memastikan bahwa modifikasi menjaga kompatibilitas kelistrikan dan manufaktur. Sistem otomatis ini membantu mencegah kesalahan desain yang umum terjadi sekaligus mengedukasi pengguna tentang standar industri dan praktik terbaik. Integrasi visualisasi 3D dengan data desain kelistrikan menciptakan lingkungan pembelajaran yang kuat di mana konsep teoretis menjadi nyata melalui representasi visual dan eksplorasi interaktif.


## Bagaimana cara membuat file pabrik?

<chapterId>e9da631c-e6d1-50c1-bb59-bc8455c29d3e</chapterId>


:::video id=07f980bf-6052-4ed4-bf7b-75e8aba585df:::

Membangun firmware khusus untuk perangkat mining berbasis ESP membutuhkan perhatian yang cermat terhadap konfigurasi, ketergantungan, dan proses pembuatan yang tepat. Panduan komprehensif ini memandu Anda melalui proses lengkap pembuatan binari firmware standar dan file pabrik yang menyertakan pengaturan yang telah dikonfigurasi sebelumnya, sehingga penerapan menjadi lebih efisien dan mengurangi waktu penyiapan bagi pengguna akhir.


Harap diperhatikan bahwa bab ini cukup teknis dan dapat dibaca sekilas saja jika Anda ingin tahu lebih banyak.


### Menyiapkan Lingkungan Pengembangan


Untuk memulai pengembangan firmware ESP-Miner, Anda harus membuat lingkungan pengembangan yang tepat di Visual Studio Code, idealnya pada distribusi linux. Ekstensi ESP-IDF berfungsi sebagai landasan penyiapan ini, menyediakan alat yang diperlukan dan integrasi kerangka kerja untuk pengembangan ESP32. Ketika menginstal ekstensi ESP-IDF untuk pertama kalinya, pengguna akan menemukan panduan penyiapan yang memfasilitasi proses konfigurasi.


Pertimbangan penting dalam proses penyiapan adalah memilih versi ESP-IDF yang sesuai. Meskipun versi 5.1.3 sebelumnya direkomendasikan, pengalaman praktis telah mengungkapkan bahwa versi ini dapat menyebabkan masalah pembangunan yang mempersulit proses pengembangan. Pendekatan yang direkomendasikan sekarang adalah menggunakan ESP-IDF versi 5.3 Beta 1, yang telah terbukti dapat mengatasi masalah-masalah tersebut dan memastikan bahwa perangkat Bitaxe berfungsi dengan baik. Proses instalasi memerlukan pemilihan opsi instalasi Express dan secara khusus memilih versi 5.3 Beta 1 dari pilihan yang tersedia.


Penyiapan lingkungan pengembangan melampaui instalasi ESP-IDF untuk menyertakan konfigurasi terminal yang tepat. Visual Studio Code menyediakan beberapa metode untuk mengakses fungsionalitas ESP-IDF, termasuk opsi palet perintah untuk membuka terminal ESP-IDF atau menggunakan ikon terminal khusus yang terletak di antarmuka. Lingkungan terminal khusus ini memastikan bahwa semua perintah ESP-IDF berfungsi dengan benar dan menyediakan akses ke rantai alat yang lengkap.


### Mengkonfigurasi Pengaturan ESP-Miner


File konfigurasi merupakan inti dari proses kustomisasi ESP-Miner, yang berisi semua parameter penting yang menentukan bagaimana perangkat akan beroperasi di lingkungan targetnya. Konfigurasi ini mencakup pengaturan jaringan, koneksi pool mining, dan parameter khusus perangkat keras yang harus disesuaikan dengan skenario penerapan tertentu.


Konfigurasi jaringan merupakan komponen utama dari proses penyiapan, yang memerlukan spesifikasi kredensial Wi-Fi termasuk SSID dan kata sandi. Daripada menggunakan nilai placeholder seperti "test", konfigurasi produksi harus menyertakan kredensial jaringan yang sebenarnya yang akan digunakan perangkat dalam lingkungan operasionalnya. Konfigurasi ini juga mengakomodasi berbagai pengaturan pool mining, mendukung konfigurasi pool pribadi dengan alamat IP tertentu dan pool publik seperti public-pool.io dengan pengaturan port yang sesuai.


Parameter konfigurasi khusus Mining mencakup pengaturan pengguna strata, yang biasanya sesuai dengan alamat Bitcoin di mana hadiah mining harus diarahkan. Parameter perangkat keras tambahan seperti pengaturan frekuensi, konfigurasi voltase, dan spesifikasi tipe ASIC harus sesuai dengan platform perangkat keras target. Repositori GitHub menyediakan contoh pra-konfigurasi untuk varian perangkat keras yang berbeda, seperti konfigurasi BM1368 yang dirancang untuk perangkat Super dan pengaturan BM1366 untuk varian Ultra. Spesifikasi versi board, seperti mengatur versi port ke 401 untuk revisi perangkat keras yang lebih baru, memastikan kompatibilitas dengan karakteristik spesifik perangkat target.


### Membangun Web Interface dan Firmware Inti


Proyek ESP-Miner menggabungkan antarmuka web yang canggih yang memerlukan kompilasi terpisah sebelum proses pembuatan firmware utama dapat dimulai. Antarmuka web ini, yang disebut sebagai firmware AxeOS, menyediakan antarmuka manajemen yang komprehensif bagi pengguna untuk memantau dan mengendalikan perangkat mining mereka.


Proses pembuatan antarmuka web dimulai dengan menavigasi ke direktori server HTTP di dalam struktur repositori utama, khususnya subdirektori AxeOS. Lokasi ini berisi aplikasi web berbasis Node.js yang membutuhkan instalasi ketergantungan melalui perintah npm install. Sistem build mengasumsikan bahwa Node.js telah terinstal dengan benar pada sistem pengembangan, karena ini merupakan persyaratan mendasar untuk proses kompilasi antarmuka web.


Setelah instalasi ketergantungan, perintah npm run build mengkompilasi komponen antarmuka web, membuat file yang diperlukan yang akan disematkan ke dalam firmware ESP32. Proses kompilasi ini menghasilkan aset web yang dioptimalkan yang menyediakan fungsionalitas antarmuka pengguna sambil mempertahankan penggunaan memori yang efisien pada platform ESP32 yang terbatas. Keberhasilan penyelesaian langkah pembuatan ini sangat penting sebelum melanjutkan ke kompilasi firmware utama, karena firmware ESP-Miner menggabungkan komponen antarmuka web ini sebagai fungsionalitas integral.


### Membuat File Pabrik dengan Konfigurasi Tertanam


Pembuatan file pabrik merupakan strategi penerapan tingkat lanjut yang menyematkan pengaturan konfigurasi secara langsung ke dalam biner firmware, sehingga tidak memerlukan konfigurasi manual selama penyiapan perangkat. Pendekatan ini terbukti sangat berharga untuk penerapan skala besar atau situasi di mana konfigurasi yang konsisten di beberapa perangkat sangat penting.


Proses pembuatan file pabrik dimulai dengan membuat biner konfigurasi dari file konfigurasi CSV menggunakan alat penghasil partisi NVS ESP-IDF. Alat ini, yang terletak di dalam direktori komponen ESP-IDF di bawah nvs-flash/nvs-partition-generator, mengonversi konfigurasi yang dapat dibaca manusia ke dalam format biner yang sesuai untuk penyimpanan memori flash langsung. Skrip nvs-partition-gen.py memproses file config.csv dan menghasilkan file config.binary yang menargetkan ruang alamat memori 0x6000.


Perakitan akhir file pabrik menggunakan skrip penggabungan khusus yang menggabungkan binari firmware inti dengan data konfigurasi. Repositori ini menyediakan beberapa opsi penggabungan, termasuk skrip penggabungan standar untuk file pabrik dasar dan skrip penggabungan yang mencakup konfigurasi untuk file pabrik yang komprehensif. Skrip penggabungan dengan konfigurasi.sh membuat file pabrik yang menyertakan fungsionalitas firmware dan pengaturan yang telah dikonfigurasi sebelumnya, sehingga menghasilkan paket penerapan yang lengkap. Pendekatan ini memungkinkan pembuatan file pabrik khusus perangkat, seperti versi yang disesuaikan untuk perangkat Bitaxe Ultra dengan revisi papan tertentu, sambil mempertahankan fleksibilitas untuk file pabrik generik generate tanpa konfigurasi yang disematkan untuk skenario yang membutuhkan fleksibilitas pengaturan manual.


File pabrik yang telah selesai menyediakan tim penerapan dengan binari siap pakai yang mencakup semua komponen firmware yang diperlukan dan pengaturan konfigurasi, merampingkan proses penyediaan perangkat dan memastikan parameter operasional yang konsisten di seluruh perangkat mining yang digunakan.


## Bagaimana cara menggunakan Bitaxe Web Flasher?

<chapterId>8c3e2d4c-c038-53ec-93cb-cc30a29e4394</chapterId>


:::video id=291757b9-f459-48f6-8766-56387f907859:::

Penginstal Web Bitaxe mewakili pendekatan yang efisien untuk manajemen firmware untuk perangkat Bitaxe, memberikan pengguna beberapa opsi instalasi melalui antarmuka berbasis web. Alat yang komprehensif ini menghilangkan kerumitan yang biasanya terkait dengan pembaruan firmware dan instalasi baru, sehingga manajemen perangkat dapat diakses oleh pengguna terlepas dari keahlian teknis mereka. Memahami penggunaan penginstal yang tepat dari penginstal ini sangat penting untuk mempertahankan kinerja perangkat yang optimal dan menghindari jebakan umum yang dapat membuat perangkat tidak dapat dioperasikan untuk sementara waktu.


### Persyaratan Pengaksesan dan Kompatibilitas Peramban


Penginstal Web Bitaxe dapat diakses melalui URL khusus [https://bitaxeorg.github.io/bitaxe-web-flasher/](https://bitaxeorg.github.io/bitaxe-web-flasher/) (URL yang ditampilkan dalam video sekarang sudah tidak digunakan lagi), yang berfungsi sebagai pusat untuk semua aktivitas instalasi firmware. Namun, keberhasilan pengoperasian alat berbasis web ini memerlukan kompatibilitas browser, karena penginstal bergantung pada teknologi web tertentu yang tidak didukung secara universal di semua browser. Chrome merupakan peramban yang direkomendasikan sebagai peramban utama untuk penginstal, yang menyediakan kompatibilitas penuh dengan semua fitur dan fungsi. Sementara peramban berbasis Chromium lainnya mungkin menawarkan fungsionalitas yang serupa, alternatif populer seperti Brave dan Firefox tidak memiliki dukungan serial web API yang diperlukan, sehingga tidak kompatibel dengan operasi inti pemasang.


Keterbatasan browser ini berasal dari ketergantungan penginstal pada komunikasi serial langsung dengan perangkat Bitaxe melalui antarmuka web. Serial web API, yang memungkinkan komunikasi ini, masih merupakan standar web yang relatif baru yang belum mencapai adopsi browser secara universal. Pengguna yang mencoba mengakses penginstal melalui browser yang tidak didukung akan mengalami kegagalan koneksi dan ketidakmampuan untuk berkomunikasi dengan perangkat mereka, sehingga perlu beralih ke browser yang kompatibel sebelum melanjutkan aktivitas penginstalan.


### Persyaratan Daya dan Persiapan Perangkat


Perangkat Bitaxe memiliki kebutuhan daya yang berbeda tergantung pada model dan versinya, sehingga manajemen daya yang tepat sangat penting untuk keberhasilan penginstalan firmware. Perangkat yang menjalankan versi 204 atau di bawahnya dapat beroperasi hanya melalui daya USB, mengambil arus yang cukup dari komputer yang terhubung untuk mempertahankan operasi selama proses flashing. Pengaturan daya yang disederhanakan ini membuat versi sebelumnya sangat nyaman untuk pembaruan firmware, karena pengguna hanya perlu menyambungkan satu kabel USB untuk memulai proses instalasi.


Namun demikian, perangkat yang menjalankan versi 205 dan di atasnya memerlukan sumber daya eksternal selain koneksi USB, yang mencerminkan perubahan dalam konsumsi daya dan desain sirkuit dalam revisi perangkat keras yang lebih baru. Perangkat ini tidak dapat menarik daya yang memadai melalui USB saja, sehingga memerlukan koneksi ke catu daya standar selama penginstalan firmware. Kegagalan dalam menyediakan daya yang memadai untuk perangkat yang lebih baru ini akan mengakibatkan kegagalan penginstalan dan potensi kerusakan pada proses pembaruan firmware.


Proses koneksi fisik memerlukan pengaturan waktu dan manipulasi tombol yang spesifik untuk memastikan komunikasi yang tepat antara pemasang dan perangkat. Pengguna harus menekan dan menahan tombol boot pada perangkat Bitaxe mereka sebelum menghubungkan kabel USB-C ke komputer. Urutan ini menempatkan perangkat ke dalam mode bootloader, sehingga memungkinkan penginstal berkomunikasi langsung dengan penyimpanan firmware perangkat. Menghubungkan kabel USB sebelum menekan tombol boot akan menghasilkan operasi perangkat normal dan bukan mode bootloader yang diperlukan untuk instalasi firmware, sehingga penginstal tidak dapat membuat saluran komunikasi yang diperlukan.


### Opsi Instalasi dan Aplikasinya


Penginstal Web Bitaxe menyediakan empat pilihan instalasi yang berbeda, masing-masing dirancang untuk kasus penggunaan dan konfigurasi perangkat tertentu. Bitaxe Superboard versi 4.0.1 merupakan firmware terbaru untuk perangkat model Super, dengan versi 4.0.2 yang dijadwalkan untuk rilis di masa mendatang. Opsi ini mencakup varian pabrik dan pembaruan, memberikan fleksibilitas dalam pendekatan instalasi berdasarkan kebutuhan pengguna dan status perangkat.


Instalasi pabrik merupakan penggantian firmware lengkap yang mencerminkan proses manufaktur asli, termasuk prosedur uji mandiri komprehensif yang memverifikasi fungsionalitas perangkat di semua sistem. Ketika pengguna memilih penginstalan pabrik, penginstal melakukan penghapusan lengkap firmware dan data konfigurasi yang ada, menggantinya dengan penginstalan yang baru dan bersih, sama seperti yang akan diterapkan saat pembuatan. Proses ini mencakup pengujian mandiri otomatis yang memvalidasi operasi perangkat keras yang tepat, mengharuskan pengguna untuk melakukan boot ulang perangkat mereka setelah selesai sebelum operasi normal dapat dilanjutkan. Instalasi pabrik terbukti sangat berharga ketika perangkat mengalami masalah yang terus-menerus atau ketika pengguna ingin mengembalikan perangkat mereka ke spesifikasi asli pabrik.


Instalasi pembaruan memberikan pendekatan yang lebih konservatif, mempertahankan data konfigurasi yang ada sementara hanya memperbarui komponen firmware inti. Opsi ini terbukti ideal bagi pengguna yang telah menyesuaikan pengaturan perangkat mereka dan ingin mempertahankan konfigurasi pribadi mereka sambil memanfaatkan peningkatan firmware dan perbaikan bug. Proses pembaruan hanya menargetkan komponen firmware yang memerlukan modifikasi, sehingga pengaturan khusus pengguna, kredensial WiFi, dan alamat Bitcoin tetap utuh selama proses instalasi.


### Pertimbangan Instalasi Penting dan Perlindungan Data


Perbedaan antara instalasi pabrik dan pembaruan membawa implikasi yang signifikan untuk konfigurasi perangkat dan pelestarian data pengguna. Instalasi pabrik melakukan penghapusan perangkat secara menyeluruh, menghapus semua pengaturan yang dikonfigurasi pengguna termasuk kredensial WiFi, alamat Bitcoin, dan parameter perangkat yang dipersonalisasi. Setelah instalasi pabrik, pengguna harus menyambungkan kembali ke jaringan WiFi default perangkat dan mengkonfigurasi ulang semua pengaturan pribadi dari awal, yang pada dasarnya memperlakukan perangkat seolah-olah perangkat tersebut baru dari pabrik.


Instalasi pembaruan memerlukan perhatian yang cermat terhadap opsi hapus perangkat yang disajikan selama proses instalasi. Penginstal akan meminta pengguna dengan pertanyaan "Apakah Anda ingin menghapus perangkat sebelum menginstal Bitaxe Flasher?" disertai dengan peringatan bahwa semua data pada perangkat akan hilang. Pengguna yang melakukan instalasi pembaruan harus menolak opsi ini dengan mengklik "Next" daripada mengonfirmasi operasi penghapusan. Menerima opsi hapus selama instalasi pembaruan akan menghapus file konfigurasi perangkat, yang berpotensi membuat perangkat tidak berfungsi hingga konfigurasi yang tepat dipulihkan. Meskipun situasi ini tidak merusak perangkat secara permanen, namun hal ini akan menimbulkan komplikasi yang tidak perlu dan memerlukan langkah konfigurasi tambahan untuk mengembalikan pengoperasian normal.


Proses instalasi itu sendiri berjalan secara otomatis setelah pengguna menentukan pilihan dan mengonfirmasi pilihan mereka. Penginstal menangani semua aspek teknis transfer dan verifikasi firmware, menyediakan indikator kemajuan dan pembaruan status selama proses berlangsung. Pendekatan otomatis ini menghilangkan kebutuhan pengguna untuk memahami prosedur penginstalan firmware yang rumit sekaligus memastikan hasil yang andal dan konsisten di berbagai model perangkat dan versi firmware.


## Bagaimana cara membuat dan memesan PCB?

<chapterId>566f5e06-9ec9-55c0-84f6-101d6ca4c2ff</chapterId>


:::video id=9a56ad84-d9cf-4f85-ab98-301fb3101228:::

Bab ini berfokus pada proses praktis pembuatan file manufaktur dari proyek KiCad dan pemesanan PCB profesional dari produsen online. Dengan menggunakan proyek Bitaxe sebagai contoh, kita akan membahas alur kerja lengkap mulai dari pembuatan file hingga melakukan pemesanan dengan produsen PCB.


### Memahami Proses Pembuatan PCB


Perjalanan dari desain KiCad yang telah selesai ke PCB fisik melibatkan beberapa langkah penting yang menjembatani kesenjangan antara desain digital dan manufaktur fisik. Ketika bekerja dengan proyek yang rumit seperti Bitaxe, editor PCB di KiCad memberikan tampilan komprehensif dari desain Anda, menampilkan semua komponen dan interkoneksinya melalui jejak berwarna. Garis merah dan biru yang Anda lihat mewakili koneksi listrik antara sirkuit terintegrasi yang berbeda dan komponen pada papan. Fitur penampil 3D KiCad memungkinkan Anda memvisualisasikan bagaimana tampilan papan rakitan akhir, memberikan wawasan yang berharga tentang penempatan komponen dan potensi konflik mekanis.


Proses manufaktur memerlukan format file tertentu yang dapat ditafsirkan dan digunakan oleh produsen PCB untuk membuat papan Anda. File-file ini berisi informasi yang tepat tentang lapisan tembaga, lubang bor, penempatan komponen, dan spesifikasi manufaktur lainnya. Memahami alur kerja ini sangat penting, baik saat Anda bekerja dengan desain Bitaxe standar atau membuat modifikasi seperti menambahkan logo khusus, mengubah nilai komponen, atau menyesuaikan tata letak papan untuk memenuhi persyaratan tertentu.


### Menghasilkan File Gerber untuk Manufaktur


File Gerber berfungsi sebagai standar industri untuk mengomunikasikan informasi desain PCB kepada produsen. File-file ini berisi semua data yang diperlukan untuk membuat PCB Anda, termasuk pola lapisan tembaga, definisi topeng solder, dan lokasi lubang bor. Untuk membuka file-file ini di KiCad, buka editor PCB dan akses hasil fabrikasi melalui menu File. Perangkat lunak ini secara otomatis mengonfigurasi pengaturan yang sesuai untuk proses manufaktur standar, termasuk struktur direktori output yang tepat yang biasanya diatur sebagai "file manufaktur/gerber."


Proses pembuatan membuat beberapa file Gerber, masing-masing mewakili aspek yang berbeda dari desain PCB Anda. File-file ini bekerja sama untuk memberikan instruksi fabrikasi lengkap kepada produsen. Setelah dibuat, file-file ini harus dikompres menjadi arsip ZIP, karena ini adalah format standar yang diharapkan oleh sebagian besar produsen PCB. File ZIP berisi semua data manufaktur yang diperlukan dan memastikan bahwa tidak ada file yang hilang atau rusak selama proses pengunggahan ke situs web produsen.


Perlu dicatat bahwa banyak proyek sumber terbuka, termasuk Bitaxe, sering menyertakan file manufaktur yang sudah dibuat sebelumnya di repositori mereka. Namun, memahami cara generate file-file ini sendiri sangat penting ketika membuat modifikasi desain atau bekerja dengan versi board yang berbeda. Pengetahuan ini menjadi sangat berharga ketika menyesuaikan desain atau memecahkan masalah manufaktur.


### Memilih Produsen PCB dan Memahami Opsi


Lanskap manufaktur PCB menawarkan beberapa opsi terkemuka, dengan JLCPCB dan PCBWay menjadi salah satu pilihan paling populer bagi para penggemar dan profesional. Kedua produsen menyediakan layanan serupa dengan harga yang kompetitif dan kualitas yang dapat diandalkan, meskipun masing-masing memiliki keunggulan spesifik tergantung pada kebutuhan proyek Anda. JLCPCB sering kali menarik pengguna pertama kali dengan harga promosi dan antarmuka yang ramah pengguna, sementara PCBWay mungkin menawarkan opsi material yang berbeda atau layanan khusus.


Apabila mengunggah file Gerber Anda ke situs web produsen, sistem akan secara otomatis menganalisis desain Anda dan menyajikan berbagai opsi manufaktur. Pengaturan default yang disediakan oleh platform ini biasanya cocok untuk sebagian besar desain standar, dan secara umum disarankan untuk mempertahankan pengaturan ini kecuali Anda memiliki persyaratan khusus. Parameter utama meliputi ketebalan PCB, berat tembaga, permukaan akhir, dan jumlah minimum. Sebagian besar produsen mengharuskan pesanan minimum lima papan, yang sebenarnya bekerja dengan baik untuk proyek-proyek penghobi di mana memiliki papan cadangan atau berbagi dengan teman akan bermanfaat.


Pilihan warna merupakan salah satu dari sedikit pilihan estetika yang tersedia selama proses produksi. Meskipun hijau tetap menjadi pilihan tradisional dan paling hemat biaya, produsen biasanya menawarkan alternatif termasuk biru, merah, kuning, ungu, dan hitam. Pilihan warna murni estetika dan tidak memengaruhi kinerja listrik PCB Anda, meskipun beberapa warna mungkin memiliki sedikit implikasi biaya atau waktu produksi yang lebih lama.


### Pertimbangan Manufaktur Tingkat Lanjut dan Opsi Perakitan


Di luar fabrikasi PCB dasar, produsen modern menawarkan layanan tambahan yang secara signifikan dapat merampingkan penyelesaian proyek Anda. Stensil merupakan salah satu layanan tambahan yang paling berharga, terutama untuk desain dengan komponen nada halus seperti chip ASIC yang ditemukan dalam proyek Bitcoin mining. Stensil pada dasarnya adalah templat aluminium yang dipotong secara presisi dengan bukaan yang sesuai persis dengan lokasi bantalan solder pada PCB Anda. Alat ini memungkinkan aplikasi pasta solder yang konsisten dan akurat, secara dramatis meningkatkan kualitas perakitan dan mengurangi kemungkinan kesalahan penyolderan.


Pilihan stensil biasanya mencakup stensil tunggal dengan pola atas dan bawah, atau stensil terpisah untuk setiap sisi papan. Untuk sebagian besar proyek, stensil gabungan terbukti lebih nyaman dan hemat biaya. Ketebalan stensil dihitung dengan cermat untuk menyimpan jumlah pasta solder yang sesuai untuk jenis komponen dan ukuran pad tertentu. Menggunakan stensil mengubah apa yang bisa menjadi proses manual yang membosankan dan rawan kesalahan menjadi langkah perakitan yang cepat dan profesional.


Meskipun beberapa produsen menawarkan layanan perakitan parsial atau lengkap, opsi ini memerlukan pertimbangan yang cermat untuk proyek-proyek kompleks seperti Bitaxe. Ketersediaan komponen, implikasi biaya, dan nilai edukasi dari perakitan mandiri semuanya menjadi faktor dalam keputusan ini. Banyak komponen khusus yang diperlukan untuk proyek Bitcoin mining mungkin tidak tersedia melalui layanan perakitan PCB standar, sehingga pencarian komponen dan perakitan manual menjadi pendekatan yang lebih praktis. Episode mendatang dalam seri ini akan membahas strategi sumber komponen dan teknik perakitan untuk membantu Anda menyelesaikan proyek Bitaxe Anda dengan sukses dari PCB kosong menjadi perangkat fungsional.


Proses manufaktur dan perakitan merupakan jembatan penting antara desain digital dan implementasi fisik. Memahami alur kerja ini memberdayakan Anda untuk mengendalikan proyek Anda, mengurangi biaya, dan mendapatkan pengalaman langsung yang berharga dengan proses manufaktur profesional. Baik Anda membuat satu prototipe atau merencanakan produksi kecil, menguasai keterampilan ini membuka kemungkinan baru untuk mewujudkan desain elektronik Anda.


# Optimalisasi Kinerja

<partId>87b8790f-b7a9-5286-a7f8-328176ef7cb5</partId>


## Membandingkan Bitaxe Anda

<chapterId>7259a4b1-93c1-5956-87d3-baaee58115af</chapterId>


:::video id=2491a783-9750-4ea5-a40c-1d1d611784d5:::

Mengejar kinerja mining yang optimal membutuhkan pendekatan sistematis untuk konfigurasi perangkat keras yang menyeimbangkan hashrate, efisiensi, dan manajemen termal. Bitaxe menawarkan banyak parameter konfigurasi yang dapat memengaruhi kinerja secara signifikan, tetapi menguji setiap kombinasi pengaturan secara manual akan menjadi tidak praktis dan memakan waktu. Bab ini membahas cara memanfaatkan alat pembandingan otomatis untuk mengoptimalkan kinerja Bitaxe Anda secara ilmiah sambil mempertahankan kondisi pengoperasian yang aman.


### Memahami Metrik Kinerja Bitaxe dan Konfigurasi Dasar


Sebelum masuk ke dalam teknik pengoptimalan, sangat penting untuk memahami indikator kinerja utama yang menentukan efisiensi operasional Bitaxe Anda. Metrik utama meliputi hashrate yang diukur dalam terahash per detik, efisiensi daya yang dinyatakan dalam joule per terahash, frekuensi ASIC dalam megahertz, dan tegangan inti dalam volt. Bitaxe yang dikonfigurasi dengan baik dapat mencapai sekitar 1,1 terahash dengan efisiensi sekitar 17 joule per terahash, beroperasi pada 550 megahertz dengan tegangan ASIC terukur sebesar 1,14 volt. Angka-angka dasar ini memberikan titik acuan untuk memahami potensi peningkatan yang tersedia melalui optimasi sistematis.


Hubungan antara metrik ini sangat kompleks dan saling bergantung. Frekuensi yang lebih tinggi biasanya meningkatkan hashrate tetapi juga meningkatkan konsumsi daya dan panas. Demikian pula, penyesuaian voltase mempengaruhi kinerja dan karakteristik termal. Tantangannya terletak pada menemukan keseimbangan optimal yang memaksimalkan hashrate atau efisiensi sambil mempertahankan operasi yang stabil dalam batas suhu yang aman. Proses pengoptimalan ini membutuhkan pengujian metodis di berbagai kombinasi parameter, sehingga alat otomatis sangat berharga untuk mencapai hasil yang optimal.


### Arsitektur Alat Benchmark Bitaxe Hashrate


Alat [Bitaxe Hashrate Benchmark](https://github.com/mrv777/Bitaxe-Hashrate-Benchmark/) merupakan solusi canggih berbasis Python yang awalnya dikembangkan oleh WhiteCookie dan kemudian disempurnakan oleh mrv777. Alat sumber terbuka ini, yang didistribusikan di bawah lisensi GPLv3, mengotomatiskan proses kompleks pengujian beberapa kombinasi konfigurasi untuk mengidentifikasi pengaturan optimal untuk perangkat keras spesifik Anda. Kekuatan utama alat ini terletak pada pendekatan sistematisnya terhadap pengujian parameter, secara bertahap menyesuaikan pengaturan frekuensi dan voltase sambil terus memantau metrik kinerja dan kondisi termal.


Proses pembandingan biasanya membutuhkan waktu 30 hingga 40 menit untuk menyelesaikannya, di mana alat ini secara metodis menguji berbagai kombinasi pengaturan frekuensi dan voltase ASIC. Alat ini dimulai dengan pengaturan awal yang konservatif, biasanya dimulai dari 1,15 volt dan 500 megahertz, kemudian secara bertahap meningkatkan parameter ini sambil memantau hashrate, suhu, dan stabilitas. Yang penting, alat ini memprioritaskan pengoperasian yang aman di atas kinerja maksimum, secara otomatis mundur dari pengaturan yang menyebabkan pembentukan panas yang berlebihan atau ketidakstabilan. Pendekatan konservatif ini memastikan bahwa proses pengoptimalan tidak mengorbankan umur panjang atau keandalan perangkat keras.


### Persyaratan Pemasangan dan Pengaturan


Menerapkan alat Benchmark Bitaxe Hashrate memerlukan beberapa komponen perangkat lunak prasyarat pada komputer lokal Anda. Persyaratan utama termasuk Python untuk menjalankan skrip benchmarking, Git untuk manajemen repositori, dan secara opsional Visual Studio Code untuk meningkatkan kemampuan lingkungan pengembangan. Meskipun alat ini dapat dioperasikan dari antarmuka baris perintah, menggunakan lingkungan pengembangan terintegrasi seperti VS Code memberikan visibilitas yang lebih baik ke dalam proses pembandingan dan analisis hasil.


Proses instalasi mengikuti praktik pengembangan Python standar, dimulai dengan mengkloning repositori dari GitHub ke mesin lokal Anda. Setelah repositori diunduh, Anda harus membuat lingkungan virtual untuk mengisolasi ketergantungan alat ini dari instalasi Python sistem Anda. Isolasi ini mencegah potensi konflik dengan aplikasi Python lain dan memastikan operasi yang konsisten. Setelah mengaktifkan lingkungan virtual, Anda akan menginstal dependensi yang diperlukan menggunakan file persyaratan yang disediakan, yang secara otomatis mengonfigurasi semua pustaka dan modul yang diperlukan untuk pengoperasian alat yang tepat.


### Menjalankan Tolok Ukur dan Menafsirkan Hasil


Menjalankan benchmark membutuhkan eksekusi satu perintah Python yang menyertakan alamat IP Bitaxe Anda sebagai parameter. Alat ini secara otomatis terhubung ke antarmuka web penambang Anda dan memulai proses pengujian sistematis. Selama eksekusi, alat ini memberikan informasi logging terperinci yang menunjukkan iterasi pengujian saat ini, pengaturan voltase dan frekuensi yang diterapkan, hashrate yang dihasilkan, voltase input, pembacaan suhu, dan data termal dari komponen penting seperti konverter buck. Umpan balik waktu nyata ini memungkinkan Anda untuk memantau kemajuan pembandingan dan memahami bagaimana pengaturan yang berbeda memengaruhi kinerja penambang Anda.


Manajemen termal cerdas alat ini menjadi nyata ketika suhu mendekati ambang batas keamanan 66 derajat Celcius. Alih-alih mendorong melampaui batas pengoperasian yang aman, benchmark secara otomatis mengurangi pengaturan untuk menjaga stabilitas termal. Pendekatan konservatif ini memastikan bahwa proses pengoptimalan memprioritaskan keandalan perangkat keras jangka panjang di atas peningkatan performa jangka pendek. Setelah selesai, alat ini menghasilkan hasil yang komprehensif dalam format JSON, memberi peringkat lima konfigurasi teratas untuk hashrate maksimum dan efisiensi optimal. Hasil ini memberikan panduan yang jelas untuk memilih konfigurasi yang paling sesuai dengan prioritas operasional Anda, baik yang berfokus pada output maksimum atau efisiensi energi.


Alat pembandingan juga menawarkan opsi penyesuaian untuk pengguna tingkat lanjut yang ingin memodifikasi parameter pengujian. Argumen baris perintah memungkinkan Anda untuk menentukan voltase dan frekuensi awal khusus, sehingga memungkinkan pengoptimalan yang lebih bertarget untuk kasus penggunaan tertentu. Misalnya, jika Anda sudah mengetahui bahwa perangkat keras Anda berkinerja baik pada frekuensi yang lebih tinggi, Anda dapat memulai benchmark pada pengaturan yang lebih tinggi daripada memulai dari pengaturan default yang konservatif. Fleksibilitas ini membuat alat ini berharga bagi pengguna pemula yang mencari pengoptimalan otomatis dan penambang berpengalaman yang ingin menyempurnakan karakteristik kinerja tertentu.


## Lakukan overclock Bitaxe Anda

<chapterId>6b48c0c6-51c3-51a3-b317-850a374ae61e</chapterId>


:::video id=46c7a442-cd72-477c-8c91-b2c489ada1e6:::

Meng-overclock perangkat Bitaxe membutuhkan pertimbangan yang cermat terhadap batasan perangkat keras dan kebutuhan pendinginan. Meskipun banyak pengguna lebih memilih untuk melakukan underclock pada perangkat mereka untuk pengoperasian yang lebih tenang, memahami teknik overclocking yang tepat sangatlah penting bagi mereka yang mencari performa maksimum tanpa merusak perangkat keras mereka. Proses ini melibatkan peningkatan frekuensi dan kemungkinan menyesuaikan pengaturan voltase di luar spesifikasi pabrik, yang secara inheren meningkatkan panas dan tekanan pada komponen.


Dasar dari overclocking yang sukses terletak pada infrastruktur pendingin yang memadai. Sebelum mencoba modifikasi frekuensi, Anda harus memastikan Bitaxe Anda memiliki kemampuan pembuangan panas yang tepat. Bitaxe Gamma dengan heatsink dan kipas berkualitas menyediakan manajemen termal yang diperlukan untuk overclocking yang aman. Perangkat dengan heatsink kecil dan kipas yang tidak memadai tidak boleh di-overclock, karena kinerja pendinginan yang buruk akan menyebabkan pelambatan termal dan potensi kerusakan perangkat keras. Hubungan antara panas dan umur komponen sangat penting untuk dipahami-panas yang berlebihan menciptakan tekanan yang menurunkan komponen elektronik dari waktu ke waktu, sehingga secara signifikan mengurangi masa pakai perangkat Anda.


### Penempatan Heatsink yang Strategis


Komponen paling penting yang membutuhkan pendinginan tambahan adalah buck converter, sebuah komponen kecil berwarna hitam yang terletak di bagian belakang Bitaxe dekat koil besar. Perangkat ini mengubah catu daya 5V yang masuk menjadi tegangan yang sesuai untuk chip ASIC, biasanya sekitar 1,2V. Buck converter, yang sering disebut sebagai TPS, menghasilkan panas yang signifikan selama operasi dan merupakan hambatan termal yang membatasi potensi overclocking. Memasang heatsink berperekat kecil pada komponen ini tidak hanya memungkinkan ruang overclocking yang lebih tinggi tetapi juga meningkatkan efisiensi secara keseluruhan dengan mengurangi kerugian termal.


Penempatan heatsink tambahan dapat memberikan manfaat pada area papan dengan arus tinggi lainnya. Sirkuit pengaturan tegangan mengalami tekanan listrik yang cukup besar saat daya mengalir dari bagian input ke bawah melalui berbagai jalur board untuk memasok chip ASIC. Banyak overclocker berpengalaman memasang heatsink di bagian depan Bitaxe di area-area berarus tinggi ini untuk meningkatkan pembuangan panas lebih jauh. Meskipun tidak terlalu diperlukan untuk overclocking moderat, langkah pendinginan tambahan ini menjadi penting ketika mendorong frekuensi ke tingkat ekstrim.


### Pertimbangan dan Keterbatasan Sistem Pendingin


Kontroler ESP32, terlihat sebagai komponen keperakan pada papan, biasanya tidak memerlukan pendinginan tambahan. Komponen ini menghasilkan panas minimal secara independen dan hanya menjadi hangat karena transfer panas dari komponen di sekitarnya. Memasang heatsink di dekat ESP32 berpotensi mengganggu antena Wi-Fi yang berdekatan, menurunkan konektivitas nirkabel dan kualitas sinyal. Fokuskan upaya pendinginan pada komponen pengaturan daya dan area ASIC daripada sirkuit kontrol.


Konfigurasi kipas ganda menghadirkan peluang dan keterbatasan. Meskipun menambahkan kipas kedua untuk menghembuskan udara di bagian belakang Bitaxe dapat meningkatkan performa pendinginan, firmware perangkat hanya dapat mengontrol satu kipas dengan baik. Bitaxe memiliki dua header kipas tetapi hanya satu pengontrol kipas, yang berarti bahwa menghubungkan dua kipas akan membingungkan firmware karena menerima sinyal RPM yang saling bertentangan. Konfigurasi ini akan berfungsi tetapi dapat mengakibatkan perilaku kontrol kipas yang tidak dapat diprediksi.


### Penilaian Kinerja Dasar


Sebelum mencoba modifikasi overclocking, tetapkan metrik performa awal dengan menjalankan Bitaxe Anda pada pengaturan stock selama beberapa jam. Pantau temperatur ASIC, temperatur regulator tegangan, dan persentase kecepatan kipas melalui antarmuka web. Suhu pengoperasian yang optimal harus menjaga ASIC di bawah 60°C dan regulator tegangan di bawah 60°C dalam kondisi normal. Jika perangkat Anda sudah beroperasi di atas 65°C pada ASIC atau 70-80°C pada regulator tegangan pada pengaturan stok, perangkat keras pendingin tambahan wajib dipasang sebelum melanjutkan overclocking.


Pendekatan sistematis untuk peningkatan frekuensi melibatkan langkah-langkah bertahap menggunakan opsi frekuensi yang telah ditentukan sebelumnya dalam menu pengaturan. Mulailah dengan memilih langkah frekuensi berikutnya yang tersedia di atas pengaturan Anda saat ini sambil mempertahankan tegangan inti default. Pendekatan konservatif ini memungkinkan Anda untuk mengevaluasi dampak termal dan stabilitas sebelum membuat perubahan tambahan. Biarkan perangkat beroperasi pada setiap pengaturan frekuensi baru setidaknya selama 30 menit hingga satu jam, memantau tren suhu dan stabilitas laju hash selama periode evaluasi.


### Konfigurasi Khusus Tingkat Lanjut


Akses ke pengaturan frekuensi dan voltase khusus memerlukan pengaktifan antarmuka overclocking tingkat lanjut dengan menambahkan "?OC" pada URL antarmuka web perangkat. Hal ini akan membuka kolom input manual untuk kontrol frekuensi dan voltase yang tepat, disertai dengan peringatan yang sesuai tentang risiko pengoperasian di luar parameter yang dirancang. Antarmuka khusus memungkinkan penyetelan di luar langkah frekuensi standar, sehingga pengguna yang berpengalaman dapat mengoptimalkan kinerja untuk konfigurasi pendinginan spesifik mereka.


Ketika menggunakan pengaturan khusus, pertahankan ukuran kenaikan konservatif 10-15 MHz per langkah penyesuaian. Pendekatan metodis ini mencegah lonjakan panas yang tiba-tiba dan memungkinkan pengujian stabilitas yang tepat pada setiap tingkat frekuensi. Beberapa pengguna tingkat lanjut mencapai frekuensi sekitar 700 MHz dengan tegangan inti yang disesuaikan ke 1.175V atau nilai yang serupa, tetapi pengaturan ekstrem ini memerlukan modifikasi pendinginan yang ekstensif dan pemantauan yang cermat. Regulator tegangan dapat beroperasi pada suhu hingga 100°C tanpa kerusakan langsung, tetapi suhu yang lebih tinggi mengurangi efisiensi dan keandalan jangka panjang. Overclocking yang sukses membutuhkan kesabaran, pengujian sistematis, dan pemantauan terus menerus untuk mencapai peningkatan kinerja yang stabil sambil menjaga integritas perangkat keras.


# Bagian Akhir

<partId>33367393-17a7-58d4-8359-79fffc6221fb</partId>


## Evaluasi kursus ini

<chapterId>785f8b92-c8a6-5a65-aa39-e9753a7edf51</chapterId>

<isCourseReview>true</isCourseReview>

## Kesimpulan

<chapterId>758baee6-2404-56fb-b534-6a39e441ae29</chapterId>

<isCourseConclusion>true</isCourseConclusion>