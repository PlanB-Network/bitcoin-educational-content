---
name: Jaringan IP dari teori ke praktik
goal: Kuasai dasar-dasar jaringan IP untuk mengonfigurasi dan memecahkan masalah dengan lebih baik.
objectives: 


  - Memahami arsitektur dan pengoperasian protokol TCP/IP
  - Menjelaskan perbedaan, keuntungan dan kendala IPv4 dan IPv6
  - Mengidentifikasi dan membedakan berbagai jenis IP Address
  - Mengkonfigurasi dan memverifikasi pengalamatan IP pada sistem Unix/Linux
  - Gunakan alat bantu diagnostik utama untuk menganalisis dan memecahkan masalah jaringan


---

# Keterampilan Penting untuk Menavigasi Dunia IP


Selami jantung dunia IP dan bekali diri Anda dengan pengetahuan untuk memahami dan mengelola jaringan Anda secara efisien. Dalam kursus ini, Anda akan mempelajari semua yang perlu Anda ketahui tentang jaringan komputer dengan cara yang jelas dan praktis.


Anda akan mempelajari cara kerja jaringan dan pengalamatan IP, cara membedakan antara IPv4 dan IPv6, cara mengidentifikasi dan menggunakan kategori Address yang berbeda, dan cara memahami pentingnya protokol TCP/IP serta hubungan yang dibentuknya antara alamat IP, alamat fisik, dan nama DNS.


NET 302 ditujukan terutama untuk siswa, pengguna Linux atau hanya mereka yang ingin tahu yang ingin memahami dasar-dasar jaringan dan memperkuat otonomi mereka dalam mengelola, memecahkan masalah dan mengoptimalkan infrastruktur.


Bergabunglah bersama kami dan ubah pengetahuan Anda menjadi keahlian operasional yang nyata!


___


Kursus NET 302 ini merupakan adaptasi dari kursus *Dasar-Dasar Jaringan: TCP/IP, IPv4 dan IPv6*, yang ditulis dalam bahasa Prancis oleh Philippe Pierre dan diterbitkan di [IT-Connect](https://www.it-connect.fr/cours/les-bases-du-reseau-tcpip-ipv4-et-ipv6/), di bawah lisensi Creative Commons Attribution-NonCommercial 4.0 International ([CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)).



Perubahan substansial telah dilakukan pada versi asli oleh Loïc Morel: teks telah sepenuhnya ditulis ulang, diperluas, dan diperkaya untuk memberikan konten yang diperbarui dan mendalam, sambil mempertahankan semangat pendidikan dari karya asli Philippe Pierre. Diagram-diagramnya juga telah direvisi.


+++


# Pendahuluan


<partId>a52b996d-1e23-470f-a9df-7ad88790099a</partId>



## Gambaran umum kursus


<chapterId>9f238ecd-c9bb-4886-a205-2beba609fb13</chapterId>


Kursus ini memberikan pengenalan lengkap tentang dasar-dasar jaringan IP. Kursus ini disusun menjadi empat bagian utama, masing-masing mencakup aspek penting untuk memahami, mengonfigurasi, dan mendiagnosis masalah dalam jaringan komputer.


### Protokol TCP/IP


Pada bagian pertama ini, kita akan meletakkan dasar dengan menjelajahi konsep jaringan dan sejarah protokol TCP/IP. Kita akan mempelajari komponen-komponen utamanya: IP, TCP, bersama dengan tinjauan singkat tentang protokol QoS IPv5. Kita juga akan membahas primitif layanan untuk lebih memahami logika data Exchange.


### Pengalamatan IPv4


Kemudian kita akan beralih ke modul yang didedikasikan untuk pengalamatan IPv4. Kamu akan belajar bagaimana IPv4 digunakan dalam praktiknya, jenis-jenis Address yang berbeda (privat, publik, broadcast, dan lain-lain), peran fundamental DNS, serta cara kerja alamat Ethernet dan protokol ARP. Kamu juga akan menemukan NAT (Network Address Translation) dan dasar-dasar konfigurasi jaringan.


### Pengalamatan IPv6


Bagian ketiga berfokus pada pengalamatan IPv6, yang diperlukan untuk mengatasi keterbatasan IPv4. Kita akan membahas standar dan definisinya, Address Assignment dalam jaringan lokal, manajemen blok Address dan hubungan antara IPv6 dan DNS.


### Alat diagnostik jaringan


Terakhir, kami akan menyimpulkan dengan presentasi alat diagnostik jaringan utama. Alat-alat ini akan memungkinkan Anda untuk menganalisis, mengontrol, dan memecahkan masalah kerusakan. Bagian ini akan disusun berdasarkan lapisan: Akses Jaringan, Jaringan, Transportasi dan lapisan atas.


Di akhir kursus ini, Anda akan memiliki pengetahuan dasar untuk mengelola infrastruktur jaringan secara efisien dan mendiagnosis potensi masalah.


Siap terjun ke dunia jaringan komputer? Mari kita mulai!


**CATATAN**: Deskripsi ini didasarkan pada sistem GNU/Linux CentOS 7. Namun, konfigurasi jaringan sebagian besar sama ketika membandingkan sistem Debian dengan sistem CentOS. Jadi, kami tidak akan membuat perbedaan apa pun. Jika ada, kami akan mengawalinya dengan logo tertentu.


**NB **: Jika Anda menemukan istilah yang tidak dikenal selama kursus, silakan baca [daftar istilah](https://planb.network/resources/glossary) untuk mendapatkan definisi.



# Protokol TCP/IP


<partId>53fd4b73-cdf1-4865-ba29-1ac8ec3e9e9a</partId>



## Apa yang dimaksud dengan jaringan?


<chapterId>7370904f-f8f5-4ad4-a63a-5931d94c3b3b</chapterId>



Dalam modul pertama ini, kita akan membahas secara mendalam protokol TCP/IP, yang merupakan landasan komunikasi digital modern. Kita akan membahas asal-usulnya, prinsip-prinsip dasarnya, dan sistem pengalamatan yang digunakannya, yang sangat penting untuk memastikan aliran informasi di antara perangkat yang terhubung.


Kami juga akan merinci komponen utama yang menyusun model ini, dan menjelaskan bagaimana komponen-komponen tersebut berinteraksi untuk membentuk jaringan yang operasional, dapat diandalkan, dan dapat diskalakan. Tetapi pertama-tama, penting untuk kembali ke konsep jaringan.


Secara etimologis, jaringan mengacu pada sekumpulan titik yang terhubung satu sama lain, membentuk struktur yang saling berhubungan. Dalam telekomunikasi dan komputasi, definisi ini diterjemahkan ke dalam sekelompok perangkat (komputer, router, sakelar, titik akses, dll.) yang mampu bertukar data melalui media fisik atau nirkabel. Dengan demikian, sebuah jaringan memungkinkan aliran informasi yang terus menerus atau terputus-putus, tergantung pada kebutuhan, protokol yang digunakan, dan sifat arsitektur yang digunakan.


Seiring berjalannya waktu, beberapa topologi klasik telah dikembangkan untuk memenuhi kebutuhan yang berbeda dalam hal biaya, kinerja, ketahanan, dan kemudahan pemeliharaan. Ini termasuk:


- jaringan cincin,
- jaringan pohon,
- jaringan bus,
- jaringan bintang,
- jaringan mesh.



### Jaringan dering


Dalam topologi cincin, perangkat terhubung dalam loop tertutup: setiap stasiun terhubung ke stasiun berikutnya, dan stasiun terakhir terhubung kembali ke stasiun pertama. Dalam pengaturan ini, setiap perangkat bertindak sebagai relai, meneruskan data ke sambungan berikutnya. Tergantung pada jenis jaringan, informasi dapat beredar dalam satu arah saja, atau keduanya.


Keuntungan dari pengaturan ini terletak pada kesederhanaan pemasangan kabel, dan tidak adanya ketergantungan pada peralatan pusat. Namun, kelangsungan seluruh jaringan tergantung pada kesehatan masing-masing elemen: kegagalan satu stasiun dapat mengganggu seluruh sistem komunikasi. Inilah sebabnya mengapa mekanisme redundansi atau bypass sering diterapkan.



![Image](assets/fr/001.webp)



### Jaringan pohon


Jaringan pohon, atau topologi hirarkis, dimodelkan setelah struktur pohon keluarga. Jaringan ini terdiri dari tingkatan-tingkatan yang berurutan: simpul akar di bagian atas terhubung ke beberapa simpul di tingkat yang lebih rendah, yang dapat terhubung ke simpul lain, dan seterusnya.


Tata letak hirarkis ini bekerja dengan sangat baik untuk jaringan besar yang membutuhkan pembagian tanggung jawab yang jelas dan manajemen yang tersegmentasi. Namun, ini juga membuat jaringan rentan terhadap kegagalan node tingkat yang lebih tinggi: kehilangan root atau cabang utama dapat memutus seluruh bagian infrastruktur.



![Image](assets/fr/002.webp)



### Jaringan bus


Dalam topologi bus, semua perangkat berbagi media transmisi yang sama, biasanya saluran koaksial atau serat optik. Setiap unit terhubung secara pasif, artinya tidak secara aktif mengubah sinyal, dan dapat mengirim atau menerima data melalui saluran bersama ini.


Keuntungan utama topologi bus adalah biaya pemasangan yang rendah, berkat pemasangan kabel yang disederhanakan.  Namun, dalam implementasi berbasis koaksial yang lebih lama (Ethernet 10BASE2/10BASE5), memutus atau kehilangan satu stasiun dapat mengganggu atau bahkan menghentikan semua lalu lintas, karena kontinuitas listrik bus dan impedansi pemutusan tidak lagi dipertahankan. Memiliki satu media fisik juga merupakan kelemahan yang kritis: kerusakan atau gangguan apa pun akan menghentikan komunikasi untuk seluruh jaringan.



![Image](assets/fr/003.webp)



### Jaringan bintang


Topologi bintang, juga dikenal sebagai "hub dan spoke", adalah yang paling umum saat ini, terutama di jaringan Ethernet rumah dan kantor. Di sini, semua perangkat terhubung ke satu perangkat pusat.


Tata letak ini memudahkan pengelolaan dan pemeliharaan: jika satu perangkat periferal gagal, seluruh jaringan tidak akan terpengaruh. Kelemahannya adalah perangkat pusat merupakan titik kegagalan tunggal: jika gagal, komunikasi akan terhenti di mana-mana. Kualitas kabel dan panjang sambungan juga harus dipertimbangkan dengan cermat untuk mempertahankan kinerja yang baik.



![Image](assets/fr/004.webp)



**Catatan**: masih ada jaringan yang diatur dalam topologi linear, seperti bus, di mana peralatan dihubungkan satu demi satu. Solusi ini, meskipun murah untuk diterapkan, memiliki kelemahan utama yaitu satu kali putus akan mengisolasi beberapa host, membagi jaringan menjadi beberapa bagian yang independen.


### Jaringan jala


Jaringan mesh dirancang untuk redundansi maksimum: setiap perangkat terhubung langsung ke setiap perangkat lainnya. Hal ini memastikan kelangsungan layanan meskipun beberapa tautan atau perangkat gagal, karena lalu lintas dapat dialihkan melalui jalur alternatif.


Pengorbanannya adalah jumlah sambungan yang harus dibuat meningkat dengan cepat seiring dengan jumlah terminal. Untuk titik sambungan `N`, diperlukan sambungan terpisah sebanyak `N × (N-1) / 2`, membuat topologi ini mahal dan rumit untuk diterapkan. Oleh karena itu, topologi ini digunakan terutama di jaringan kritis yang membutuhkan ketersediaan yang sangat tinggi, seperti bagian tertentu dari Internet atau sistem industri yang sensitif.



![Image](assets/fr/005.webp)



Variasi lain yang ada, seperti jaringan grid atau hypercube, yang dirancang untuk kebutuhan khusus dalam komputasi terdistribusi atau pemrosesan paralel.


Dalam skala global, Internet adalah interkoneksi besar-besaran dari jaringan yang menggunakan beragam topologi, yang disatukan oleh pengalamatan umum (IPv4 dan IPv6) dan kumpulan protokol standar yang ditetapkan oleh IETF (*Internet Engineering Task Force*). Keragaman ini berarti Internet tidak mengikuti satu topologi tunggal: strukturnya fleksibel, dapat diukur dan tidak bergantung pada skema pengalamatan logis yang membuatnya dapat digunakan.



## Asal-usul TCP/IP


<chapterId>266b6864-8789-48d7-bc85-001cb9f1651f</chapterId>



Asal-usul protokol TCP terletak pada **ARPA** (*Advanced Research Projects Agency*, berganti nama menjadi "DARPA" pada tahun 1972), yang meluncurkan proyek **ARPANET** pada tahun 1966. Segmen ARPANET pertama beroperasi pada bulan Oktober 1969, menghubungkan universitas UCLA dan Stanford. Tujuannya adalah untuk menghubungkan pusat-pusat penelitian melalui jaringan packet-switched yang dapat menjaga komunikasi tetap berjalan bahkan jika terjadi kegagalan infrastruktur parsial.


Sebagai bagian dari dinamika ini, ARPA mendanai Universitas Berkeley untuk mengintegrasikan protokol TCP/IP pertama ke dalam sistem BSD Unix. Hal ini memainkan peran penting dalam menyebarkan dan menstandarkan protokol, pertama di dunia akademis, dan kemudian di industri.


**Catatan**: pada saat itu, para ilmuwan komputer belum memiliki Linux (yang baru muncul pada awal tahun 1990-an), atau Minix, sistem pendidikan yang dirancang oleh Andrew Tanenbaum.  Pilihan utamanya adalah Unix, atau, kadang-kadang, mainframe berpemilik seperti OpenVMS. Berkat fleksibilitas dan keterbukaannya, Unix berperan penting dalam menyebarkan konsep jaringan yang pertama.


Sebenarnya, TCP/IP bukanlah protokol tunggal, melainkan sebuah rangkaian protokol yang dibangun di sekitar TCP dan IP. Protokol ini menjadi terkenal karena menyediakan pemrograman standar Interface untuk bertukar data antar mesin pada jaringan yang sama. Interface ini, berdasarkan pada primitif yang disebut "soket", memungkinkan untuk membuat koneksi yang andal dan fleksibel sambil mengintegrasikan protokol aplikasi yang penting.


Oleh karena itu, ARPANET merupakan fondasi historis dari Internet saat ini. Memang, Internet adalah jaringan global yang didasarkan pada prinsip pengalihan paket, di mana informasi beredar menggunakan seperangkat protokol standar yang memastikan kompatibilitas dan interoperabilitas antara sistem yang heterogen. Arsitektur terbuka ini telah memungkinkan pengembangan dan penyebaran layanan dan aplikasi yang tak terhitung jumlahnya, termasuk:


- email,
- world Wide Web (www),
- transfer dan berbagi file...


Tata kelola dan evolusi protokol-protokol ini diawasi oleh ***Internet Architecture Board*** (IAB).

Organisasi ini mengkoordinasikan arahan teknis melalui dua struktur utama:


- IRTF** (_Internet Research Task Force_), yang melakukan penelitian jangka panjang tentang evolusi dan peningkatan protokol.
- IETF** (_Internet Engineering Task Force_), yang mengembangkan, menstandarkan, dan mendokumentasikan protokol operasional yang digunakan di Internet


Distribusi sumber daya jaringan (rentang IP Address, nomor sistem otonom, nama domain akar, dll.) dikoordinasikan secara internasional oleh **IANA/ICANN**. Manajemen operasional bergantung pada: **RIR** (*Regional Internet Registries*): **RIPE NCC** (Eropa, Timur Tengah, Asia Tengah), **ARIN**, **APNIC**, **LACNIC**, dan **AFRINIC**.


Semua spesifikasi protokol TCP/IP dicatat dalam dokumen yang disebut **RFC** (_Request For Comments_), yang berfungsi sebagai referensi teknis yang otoritatif. RFC terus diperbarui dan diberi nomor untuk mencerminkan evolusi yang sedang berlangsung dari rangkaian protokol.


Tumpukan TCP/IP sering direpresentasikan sebagai tumpukan empat lapisan fungsional, yang sering dibandingkan dengan model **OSI** (_Open Systems Interconnection_) tujuh-Layer yang dikembangkan oleh **ISO** (_International Standards Organization_), yang berfungsi sebagai referensi konseptual untuk jaringan.


Empat lapisan model TCP/IP adalah:


- nETWORK ACCESS Layer, yang menyediakan tautan fisik dan protokol kontrol akses media;
- iNTERNET Layer, yang menangani perutean dan pengalamatan IP;
- tRANSPORT Layer, yang menjamin keandalan dan pengelolaan aliran data menggunakan protokol seperti TCP atau UDP;
- aPLIKASI Layer, yang mengelompokkan protokol pengguna dan perangkat lunak seperti HTTP, FTP, SMTP, dan DNS.



![Image](assets/fr/006.webp)



Saat ini, versi IP yang paling banyak digunakan adalah IPv4, tetapi ruang 32-bit Address memiliki keterbatasan yang jelas. Hal ini mendorong terciptanya IPv6, yang menggunakan pengalamatan 128-bit dan menawarkan kapasitas yang hampir tak terbatas: penting untuk mendukung pertumbuhan eksplosif perangkat yang terhubung dan memenuhi tantangan Internet of Things, mobilitas, dan keamanan.


Setiap Layer dari tumpukan TCP/IP menyediakan layanan spesifik, sehingga memungkinkan untuk memenuhi kebutuhan jaringan yang berbeda secara modular: transmisi fisik, pengalamatan logis, integritas data, dan layanan tingkat aplikasi.


| Device example    | Description                                                                               | 	TCP/IP layer |
| ---------------------- | ----------------------------------------------------------------------------------------- | ----------------------- |
| Web server            | Application services closest to end users                                      | Application             |
| Gateway or proxy    | 	Encodes, encrypts, compresses useful data                                              | Application             |
| Session switch | Establishes sessions between applications                                               | Application             |
| Firewall or L4 router | Establishes, maintains, and terminates sessions between endpoint devices                  | Transport               |
| Router                | Globally addresses interfaces and determines optimal paths through a network | Network                  |
| Switch   | Locally addresses interfaces and forwards traffic via MAC                            | Network Access         |
| Network Interface Card (NIC)     | Signal encoding, cabling, connectors, physical specifications                        | Network Access         |

https://planb.network/tutorials/computer-security/communication/pi-hole-46a735c5-8af3-4cc3-a2c2-1d4f6a7dc428

https://planb.network/tutorials/computer-security/operating-system/opnsense-90c2785d-a0d7-4981-be8d-d290bbeb8263

https://planb.network/tutorials/computer-security/operating-system/pfsense-24eea96a-2fdc-42a6-a77b-89bc29149864

## Protokol QoS IPv5


<chapterId>570ded19-be61-4005-844e-9490570a6455</chapterId>



Header dari paket IP adalah struktur data yang penting, dibagi menjadi beberapa bidang, masing-masing dengan peran khusus untuk memastikan paket dikirim dan diproses dengan benar saat mereka berjalan melalui jaringan. Bidang-bidang ini termasuk IP Address tujuan (diperlukan untuk merutekan paket ke penerima yang dituju), panjang header yang ditunjukkan oleh bidang IHL (*Internet Header Length*), total panjang paket yang dicatat dalam bidang *Total Length*, informasi kontrol dan verifikasi, dan parameter lain untuk mengelola aliran dan kualitas komunikasi.


Bidang pertama dalam header disebut Versi. Nilai 4-bit ini menentukan versi protokol IP mana yang diikuti oleh paket. Ini penting karena memberi tahu setiap router atau perangkat perantara bagaimana menafsirkan dan menangani data yang dienkapsulasi.


**Catatan**: Pengelolaan dan penetapan versi protokol IP berada di bawah tanggung jawab **IANA**. Sebuah field 4-bit memungkinkan 16 kombinasi biner (nilai 0 hingga 15). Hingga saat ini, penetapannya adalah sebagai berikut:



| Version Number | Protocol   | Version Description         | Reference               |
| -------------- | ---------- | --------------------------- | ----------------------- |
| 0–1            | Reserved   | Reserved                    |                         |
| 2–3            | Unassigned | Unassigned                  |                         |
| 4              | IP         | Internet Protocol           | RFC 791                 |
| **5**          | **ST**     | **ST Datagram mode**        | **RFC 1190** / RFC 1819 |
| 6              | IPv6       | Internet Protocol version 6 | RFC 8200                |
| 7              | TP/IX      | The Next Internet           | RFC 1475                |
| 8              | PIP        | The P Internet Protocol     | RFC 1621                |
| 9              | TUBA       | Tuba                        | RFC 1347                |
| 10–14          | Unassigned | Unassigned                  |                         |
| 15             | Reserved   | Reserved                    |                         |

Di antaranya adalah IPv5, yang meskipun tidak banyak diketahui oleh publik, namun sebenarnya sudah ada sejak dulu sebagai ST (_Stream Protocol_). Dikembangkan pada tahun 1980-an, IPv5 dirancang untuk memenuhi kebutuhan yang berkembang pada saat itu: menyediakan "_Quality of Service_" (QoS) untuk aliran data tertentu yang membutuhkan transmisi yang stabil dan berkelanjutan, seperti Voice over IP atau aliran multimedia. Tujuannya adalah untuk menjamin bandwidth dan prioritas end-to-end, sebuah konsep yang mirip dengan apa yang ditawarkan RSVP (_Resource Reservation Protocol_) saat ini untuk memesan sumber daya jaringan secara dinamis pada router modern.


Namun, IPv5 masih bersifat eksperimental dan diimplementasikan hanya pada sejumlah kecil perangkat jaringan. Adopsi yang terbatas, dikombinasikan dengan kebutuhan yang berkembang pesat akan lebih banyak ruang Address, membuat para perancang Internet langsung beralih dari IPv4 ke IPv6. Hal ini dilakukan untuk menghindari keterbatasan Address dari IPv4 dan risiko kebingungan atau ketidakcocokan dengan spesifikasi eksperimental IPv5.


Meskipun IPv5 tidak pernah digunakan secara luas, IPv5 memainkan peran penting dalam membentuk pemikiran awal tentang QoS dan manajemen lalu lintas. Saat ini, IPv5 lebih merupakan penanda sejarah daripada sebuah standar yang berfungsi.


**Pengingat** - Protokol adalah seperangkat aturan komunikasi: struktur data, algoritme, format paket, dan konvensi yang memungkinkan perangkat yang berbeda untuk Exchange informasi dengan andal dan dapat dimengerti. Layanan adalah implementasi konkret dari protokol melalui program tertentu (klien, server) yang mengikuti aturan-aturan ini dan membuat fungsionalitas tersedia bagi pengguna dan aplikasi.


Sekarang kita dapat melihat lebih dekat pada struktur dan operasi protokol IP, fondasi penting dari semua komunikasi jaringan.



## Protokol IP


<chapterId>758fddbd-b652-4c18-bd1e-d038bd2e4d05</chapterId>



### Definisi dan informasi umum


Protokol IP, atau "***Internet Protocol***", adalah tulang punggung model TCP/IP. Protokol ini membawa paket data dari satu host ke host lainnya dalam jaringan, baik lokal maupun di seluruh dunia. Protokol ini memiliki dua peran utama: mengelola pengalamatan logis perangkat, dan memastikan paket dirutekan melintasi jaringan yang sering kali heterogen dan saling terhubung.


Pada tingkat fisik, transmisi bergantung pada antarmuka perangkat keras untuk membuat koneksi point-to-point antar node. Namun, protokol IP-lah yang memungkinkan komunikasi ujung ke ujung, memberikan setiap paket informasi yang dibutuhkan untuk menavigasi melalui beberapa jalur yang memungkinkan ke tujuannya.


Tiga konfigurasi jaringan Elements menentukan bagaimana sebuah paket dikirim dalam perjalanannya:


- IP Address**: mengidentifikasi host tujuan secara unik dalam jaringan.
- Subnet mask**: menentukan bagian mana dari Address yang mengidentifikasi jaringan dan bagian mana yang mengidentifikasi host, memungkinkan pembagian logis ke dalam subnet.
- Gateway**: menunjukkan router perantara yang harus dilewati paket untuk mencapai jaringan eksternal atau segmen lain dari jaringan lokal.


Di Internet, data tidak mengalir sebagai satu aliran yang terus menerus, tetapi dikirim sebagai **datagram**: blok data yang independen, masing-masing dienkapsulasi dengan semua informasi yang diperlukan untuk pengiriman. Ini adalah prinsip **paket switching**, di mana informasi dipecah menjadi unit-unit mandiri yang dapat mengambil jalur yang berbeda untuk mencapai penerima yang sama.


Selain muatan (*payload*), setiap datagram IP berisi header terstruktur dengan bidang-bidang seperti Address tujuan, Address sumber, jenis layanan, nomor versi protokol, dan informasi kontrol lain yang diperlukan untuk mengelola transmisi.


Ukuran maksimum teoretis dari datagram IP adalah **65.536 oktet**, sebuah batas yang ditetapkan oleh bidang panjang total dalam header. Dalam praktiknya, ukuran ini jarang tercapai, karena jaringan fisik yang membawa paket (Ethernet, Wi-Fi, serat optik...) biasanya memberlakukan batas yang lebih ketat yang dikenal sebagai **MTU** (_Maximum Transmission Unit_). Jika sebuah datagram melebihi MTU dari sambungan fisik, datagram tersebut harus dipecah menjadi paket-paket yang lebih kecil, masing-masing dikirim secara terpisah dan disatukan kembali pada saat kedatangan.


Kemampuan beradaptasi ini membuat IP menjadi protokol yang kuat dan fleksibel, yang mampu beroperasi di berbagai macam teknologi yang mendasarinya sambil mempertahankan kompatibilitas universal antara sistem dan jaringan yang heterogen.



### Fragmentasi datagram IP


Ketika sebuah datagram IP perlu melewati jaringan yang kapasitas transmisinya lebih kecil dari datagram itu sendiri, datagram tersebut harus dipecah-pecah agar dapat berjalan tanpa masalah. Batas ukuran fisik ini disebut **MTU** (Maximum Transmission Unit): ukuran frame terbesar yang dapat melewati jaringan tertentu tanpa terpecah.


Setiap teknologi jaringan memberlakukan MTU-nya sendiri, yang ditentukan oleh karakteristik perangkat keras dan protokolnya. Nilai yang umum meliputi:


- ARPANET**: 1000 byte
- Ethernet**: 1500 byte
- FDDI**: 4470 byte


Ketika sebuah datagram melebihi MTU segmen jaringan yang harus dilewati, peralatan perutean akan membaginya menjadi **fragmen** yang lebih kecil yang sesuai dengan batas tersebut. Hal ini biasanya terjadi ketika berpindah dari jaringan dengan MTU tinggi ke jaringan dengan kapasitas yang lebih rendah. Sebagai contoh, sebuah datagram yang berasal dari jaringan FDDI mungkin perlu dipecah-pecah sebelum dikirim melalui segmen Ethernet.



![Image](assets/fr/008.webp)



Proses fragmentasi bekerja seperti ini:


- Router memecah datagram menjadi beberapa fragmen yang tidak lebih besar dari MTU jaringan target.
- Ukuran setiap fragmen adalah kelipatan 8 byte, karena protokol IP menggunakan unit ini untuk menyandikan offset pemasangan ulang.
- Setiap fragmen mendapatkan header IP-nya sendiri, yang berisi informasi yang diperlukan oleh penerima akhir untuk menyusunnya kembali dalam urutan yang benar.


Setelah terfragmentasi, potongan-potongan tersebut bergerak secara independen melalui jaringan. Mereka mungkin mengambil rute yang berbeda, tergantung pada tabel perutean, beban tautan, atau pemadaman. Tidak ada jaminan bahwa mereka akan tiba sesuai dengan urutan pengirimannya.


Pada saat kedatangan, mesin penerima menangani **pemasangan kembali**. Dengan menggunakan informasi dalam header (pengenal bersama, offset, dan flag fragmentasi), mesin ini menempatkan kembali fragmen dalam urutan yang benar untuk merekonstruksi datagram asli sebelum mentransmisikannya ke Layer berikutnya. Jika satu fragmen saja hilang atau rusak, seluruh datagram biasanya dibuang, tanpa setiap fragmen, hasilnya tidak akan lengkap atau tidak dapat digunakan.


Meskipun efektif, fragmentasi dan reassembly memiliki kekurangan: pemrosesan ekstra untuk router dan host, dan kemungkinan kehilangan paket yang lebih tinggi, yang dapat meningkatkan transmisi ulang. Itulah mengapa manajemen MTU yang cermat dan pengoptimalan ukuran paket penting untuk komunikasi IP yang lancar dan efisien.



### Enkapsulasi data


Untuk memastikan bahwa data dirutekan dengan benar melalui lapisan-lapisan model TCP/IP, proses **enkapsulasi** memainkan peran kunci. Pada setiap tahap ketika pesan berjalan dari aplikasi pengirim ke mesin penerima, informasi tambahan, yang dikenal sebagai header, ditambahkan. Header ini memberikan perangkat perantara dan lapisan perangkat lunak instruksi yang mereka butuhkan untuk memproses, mengirim, dan, jika perlu, menyusun kembali data.


Ketika sebuah pesan dikirim, pesan tersebut melewati empat lapisan tumpukan TCP/IP. Pada setiap Layer, header baru ditambahkan di depan data yang ada: setiap header berisi metadata spesifik, seperti alamat logis atau fisik, port komunikasi, nomor urut, bendera kontrol kesalahan, dan informasi apa pun yang diperlukan untuk mengelola transmisi dan perutean.


Oleh karena itu, penularan mengikuti proses yang terstruktur:


- Aplikasi Layer membuat **pesan** awal, yang berisi data mentah.
- Transport Layer merangkumnya ke dalam **segmen**, menambahkan port sumber dan tujuan, nomor urut, dan mekanisme kontrol aliran.
- Internet Layer menambahkan header IP pada segmen tersebut untuk membentuk **datagram**, menentukan alamat IP sumber dan tujuan.
- Network Access Layer membungkus datagram ke dalam **frame**, menambahkan alamat MAC dan kode pemeriksaan integritas (CRC).



![Image](assets/fr/009.webp)



Proses enkapsulasi ini memastikan integritas dan ketertelusuran data, dan juga kemampuan beradaptasi: ketika berpindah dari satu jaringan ke jaringan lain, header memberikan informasi yang diperlukan perangkat untuk memilih rute, memeriksa validitas, atau melakukan fragmentasi jika perlu.


Setelah tiba, prosesnya dibalik: mesin penerima mendapatkan frame di Network Access Layer, yang membaca dan menghapus header yang sesuai. Datagram kemudian diteruskan ke Internet Layer, yang membaca header IP dan menghapusnya secara bergantian untuk mengirimkan segmen ke Transport Layer. Transport Layer memproses header transport, memeriksa integritas aliran, dan akhirnya mengirimkan **pesan** ke aplikasi target dalam keadaan aslinya.



![Image](assets/fr/010.webp)



Transformasi data pada setiap Layer dapat diringkas sebagai:


- Pesan**: blok informasi di Aplikasi Layer.
- Segmen**: unit data setelah dienkapsulasi oleh Transport Layer.
- Datagram**: formulir yang diambil setelah penambahan header IP oleh Internet Layer.
- Frame**: blok akhir yang siap untuk ditransmisikan melalui media fisik oleh Network Access Layer.



![Image](assets/fr/011.webp)



Proses ini, yang sangat penting untuk keandalan dan universalitas komunikasi Internet, memastikan bahwa setiap bagian data, tidak peduli seberapa terfragmentasi atau rumitnya, dapat diangkut dari ujung ke ujung namun tetap dapat dipahami dan digunakan oleh mesin penerima.



### Pengalamatan IP


Bahkan dengan pengalihan paket, fragmentasi, dan enkapsulasi, jaringan masih tidak dapat berfungsi tanpa sistem pengalamatan yang andal. Untuk memastikan bahwa setiap paket data mencapai penerima yang tepat, Internet Layer menggunakan pengenal unik: **IP Address**.

Pada IPv4, IP Address dikodekan pada **32 bit** dan ditulis sebagai empat angka desimal yang dipisahkan oleh titik-titik, dalam format N1.N2.N3.N4 yang sudah tidak asing lagi (misalnya: 192.168.1.12).


IP Address memiliki dua bagian:


- _netid_**: mengidentifikasi jaringan tempat host berada
- _hostid_**: mengidentifikasi host tertentu dalam jaringan tersebut

Pemisahan ini memungkinkan Internet global terstruktur secara logis ke dalam banyak jaringan yang saling terhubung.


Secara historis, sistem IPv4 bergantung pada skema berbasis kelas, diberi label dari A hingga E, yang mendefinisikan kisaran Address dan tujuan penggunaannya. Setiap kelas mengalokasikan sejumlah bit ke _netid_ dan _hostid_, yang secara langsung mempengaruhi jumlah jaringan dan host yang mungkin.



| **Class** | **IPv4 Address Range**            | **Usage**                    |
| --------- | --------------------------------- | ---------------------------- |
| A         | 1.x.x.x to 126.x.x.x              | Unicast addresses            |
|           | (127.x.x.x reserved for loopback) | Local loopback               |
| B         | 128.0.x.x to 191.255.x.x          | Unicast addresses            |
| C         | 192.0.0.x to 223.255.255.x        | Unicast addresses            |
| D         | 224.0.0.0 to 239.255.255.255      | IP Multicast                 |
| E         | 240.0.0.0 to 255.255.255.255      | Reserved for experimentation |

Tidak semua nilai yang mungkin dapat ditetapkan ke host. Sebagai contoh, dalam **kelas C** Address, byte terakhir menawarkan 8 bit (256 nilai). Tetapi dua di antaranya dicadangkan:


- 0: mengidentifikasi jaringan itu sendiri
- 255: adalah **broadcast** Address, digunakan untuk mengirim paket ke semua host dalam jaringan sekaligus.

Ini menyisakan 254 alamat yang dapat digunakan untuk perangkat.


Jumlah alamat yang tersedia sangat bervariasi di antara kelas-kelas: dari jaringan publik yang besar di kelas A, jaringan perusahaan di kelas B, hingga jaringan lokal yang lebih kecil di kelas C.



![Image](assets/fr/013.webp)



Beberapa rentang Address dicadangkan untuk penggunaan pribadi dan tidak pernah dirutekan secara langsung di Internet. Ini dikenal sebagai **alamat pribadi**, dan digunakan di dalam organisasi, bisnis, atau rumah, dan memerlukan terjemahan Address, biasanya NAT (*Network Address Translation*), untuk menjangkau Internet publik. Ini adalah:


- Kelas A**: dari 10.0.0.0 hingga 10.255.255.255
- Kelas B**: dari 172.16.0.0 hingga 172.31.255.255
- Kelas C**: dari 192.168.0.0 hingga 192.168.255.255


Ketika perangkat dengan Address pribadi mengakses Internet, router atau gateway yang mendukung NAT akan menggantikannya dengan Address publik yang valid.


Contoh: Jika sebuah host memiliki Address **192.168.7.5**, kita dapat menyimpulkan:


- 192.168.7.0: jaringan Address
- 192.168.7.1: sering kali merupakan router lokal
- 192.168.7.5: tuan rumah itu sendiri


Kasus khusus lainnya adalah **127.0.0.1**, yang dikenal sebagai "***loopback***".

Pada sistem Linux, ini dikaitkan dengan Interface **lo**. Address ini memungkinkan mesin untuk melakukan Address sendiri untuk pengujian atau diagnostik lokal, tanpa melalui Interface fisik. Seluruh rentang **127.0.0.0/8** dicadangkan untuk tujuan ini.


Untuk mengoptimalkan penggunaan Address dan mendesain jaringan yang kompleks, **subnetmask** (_netmask_) sangat penting. Topeng biner ini memisahkan _netid_ dari _hostid_ dalam IP Address.

Setiap kelas memiliki topeng default:


- 255.0.0.0** untuk kelas A,
- 255.255.0.0** untuk kelas B,
- 255.255.255.0** untuk kelas C.


Desain jaringan yang baik mengikuti aturan dasar: perangkat yang harus berkomunikasi secara langsung harus berada dalam jaringan atau subnet yang sama. Untuk menyegmentasikan jaringan, kita menggunakan subnetting, membagi jaringan menjadi subnet yang lebih kecil dengan menggunakan mask yang lebih spesifik.


Contoh subnetting:

Jaringan **kelas C**: 192.168.1.0/24 dengan mask default 255.255.255.0.

Kami menginginkan 4 subnet yang masing-masing terdiri dari 60 host.


**Langkah 1**: Jumlah alamat yang dibutuhkan per subnet = 60 + 2 alamat yang dicadangkan (jaringan + broadcast) = 62.


**Langkah 2**: Temukan pangkat terdekat dari 2 ≥ 62. -> 2⁶ = 64.


**Langkah 3: Sesuaikan mask. Pertahankan bit _netid_ dan simpan bit _hostid_ yang diperlukan. Kita mendapatkan sebuah mask biner yang, setelah dikonversi, akan menghasilkan **255.255.255.192**.


```
11111111 11111111 11111111 11000000
```


**Langkah 4**: Hitung rentang Address untuk setiap subnet, dengan memvariasikan bit yang dicadangkan untuk host.



| Subnet ID (bits) | Subnet Address   | Subnet Mask     | Address Range                 | Broadcast Address |
| ---------------- | ---------------- | --------------- | ----------------------------- | ----------------- |
| 00               | 192.168.1.0/26   | 255.255.255.192 | 192.168.1.1 – 192.168.1.62    | 192.168.1.63      |
| 01               | 192.168.1.64/26  | 255.255.255.192 | 192.168.1.65 – 192.168.1.126  | 192.168.1.127     |
| 10               | 192.168.1.128/26 | 255.255.255.192 | 192.168.1.129 – 192.168.1.190 | 192.168.1.191     |
| 11               | 192.168.1.192/26 | 255.255.255.192 | 192.168.1.193 – 192.168.1.254 | 192.168.1.255     |


**Langkah 5**: Ini menciptakan empat subjaringan, masing-masing mendukung hingga 62 mesin, sambil menjaga skema pengalamatan keseluruhan tetap efisien. Bagian _hostid_ dibagi menjadi bagian _subnetid_ dan bagian host.



![Image](assets/fr/016.webp)



Prinsip dasar subnetting ini tetap sangat diperlukan dalam rekayasa jaringan modern, yang memungkinkan alokasi IP yang tepat, kontrol lalu lintas yang lebih baik, isolasi segmen yang kuat, dan manajemen jaringan yang dapat diskalakan.



### Pengalamatan CIDR


Pada awal tahun 1990-an, ketika Internet menyebar dengan cepat melalui bisnis dan organisasi, sistem pengalamatan IP tradisional berdasarkan kelas (A, B, C) mulai menunjukkan batasannya.

Strukturnya yang kaku menyebabkan pemborosan alamat IP yang signifikan dan membuat tabel routing menjadi semakin besar, kompleks, dan sulit untuk dipelihara.

Untuk mengatasi masalah ini, sebuah metode yang lebih fleksibel dan efisien diperkenalkan: **CIDR** (Perutean Antar Domain Tanpa Kelas). CIDR secara bertahap menjadi standar, sebagian besar menggantikan sistem berbasis kelas yang lama.


Ide inti di balik CIDR adalah kemampuan untuk mengelompokkan beberapa jaringan yang berdekatan, terutama blok Kelas C, ke dalam satu unit logis yang disebut **supernet** (_supernet_). Dengan agregasi ini, satu entri dalam tabel perutean dapat mewakili beberapa subjaringan, mengurangi jumlah rute yang perlu ditangani router dan meningkatkan kinerjanya.


Meskipun jaringan Kelas C pada awalnya memiliki kebutuhan terbesar untuk agregasi karena kapasitasnya yang lebih kecil, prinsip ini juga telah diterapkan pada jaringan Kelas B dan, secara teori, bahkan jaringan Kelas A, meskipun jaringan Kelas A tidak terlalu terpengaruh karena rentang Address yang besar.


Dengan CIDR, konsep kelas tetap menghilang. Ruang Address diperlakukan sebagai rentang kontinu yang dapat dibagi atau digabungkan sesuai kebutuhan. Blok CIDR didefinisikan menggunakan subnet mask yang tidak terbatas pada default kelas A, B, atau C. Sebuah blok CIDR dapat mewakili satu jaringan atau sekumpulan subjaringan yang bersebelahan yang berbagi awalan yang sama.


Blok CIDR ditulis dalam format "Address/prefix", di mana angka setelah garis miring menunjukkan berapa banyak bit yang membentuk bagian jaringan. Sebagai contoh, /17 berarti bahwa 17 bit pertama mengidentifikasi jaringan, sedangkan 15 bit sisanya mengidentifikasi host.


Contoh:

Blok /17 berisi 2^(32-17) alamat sehingga 2^15 = 32.768 alamat total. Dengan mengurangi dua alamat yang dicadangkan (jaringan dan broadcast) akan menyisakan 32.766 alamat host yang dapat digunakan. Hal ini memungkinkan administrator jaringan untuk mengatur ukuran subnet mereka secara tepat agar sesuai dengan kebutuhan dunia nyata, menghindari pemborosan yang tidak perlu.


Agar ukuran CIDR lebih mudah dipahami, berikut ini adalah tabel awalan umum dan subnet mask yang setara serta alamat yang dapat digunakan:


| CIDR Prefix | Available Host Bits | Subnet Mask     | Usable Host Addresses         |
| ----------- | ------------------- | --------------- | ----------------------------- |
| /8          | 24                  | 255.0.0.0       | 2^24 - 2 = 16,777,214         |
| /12         | 20                  | 255.240.0.0     | 2^20 - 2 = 1,048,574          |
| /16         | 16                  | 255.255.0.0     | 2^16 - 2 = 65,534             |
| /20         | 12                  | 255.255.240.0   | 2^12 - 2 = 4,094              |
| /24         | 8                   | 255.255.255.0   | 2^8 - 2 = 254                 |
| /26         | 6                   | 255.255.255.192 | 2^6 - 2 = 62                  |
| /27         | 5                   | 255.255.255.224 | 2^5 - 2 = 30                  |
| /28         | 4                   | 255.255.255.240 | 2^4 - 2 = 14                  |
| /29         | 3                   | 255.255.255.248 | 2^3 - 2 = 6                   |
| /30         | 2                   | 255.255.255.252 | 2^2 - 2 = 2                   |
| /31         | 1                   | 255.255.255.254 | 2^1 = 2 (point-to-point only) |
| /32         | 0                   | 255.255.255.255 | 1 (host address only)         |


**CATATAN**: Secara historis, RFC 950 tidak menganjurkan penggunaan subnet nol, terutama untuk menghindari kebingungan dalam perutean.  Pembatasan ini menjadi usang dengan RFC 1878, yang sepenuhnya mengizinkan penggunaannya. Batasan yang lama sebagian besar disebabkan oleh ketidakcocokan dengan perangkat keras yang lebih tua yang tidak dapat menangani CIDR dengan benar. Peralatan modern tidak memiliki masalah seperti itu.


Sebagai contoh, subnet **1.0.0.0** dengan subnet mask **255.255.0.0** yang tadinya rancu dengan pengenal jaringan kelas A, sekarang sudah valid dan dapat digunakan.


**TIP**: untuk penghitungan subnet yang bebas dari kesalahan dan konversi alamat ke notasi CIDR dengan cepat, ada alat bantu praktis seperti ***ipcalc***. "Kalkulator jaringan" ini dengan jelas menunjukkan rincian Address, rentang yang tersedia, dan mask yang terkait, ideal untuk administrator dan siswa yang mempelajari CIDR.


```shell
sudo apt install ipcalc
```


https://planb.network/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d

## Protokol TCP


<chapterId>860bf7d5-a502-4d10-a12c-9827f6c2d393</chapterId>



Protokol **TCP** (_Transmission Control Protocol_) memainkan peran sentral dalam TRANSPORT Layer model TCP/IP. Protokol ini bertindak sebagai jembatan antara aplikasi dan Internet Layer, memastikan transfer data yang andal antara dua mesin yang berjauhan.

Sementara protokol IP hanya mengirimkan paket tanpa menjamin pengiriman atau urutan, TCP memastikan integritas dan konsistensi aliran data, mengirimkannya tanpa kehilangan, dalam urutan yang benar, dan tanpa duplikat.


Tanggung jawab utama TCP meliputi:


- Menyusun ulang segmen yang diterima;
- Memantau aliran data untuk menghindari kemacetan;
- Memisahkan atau menyusun kembali blok data ke dalam unit (segmen) yang sesuai;
- Mengelola pembentukan dan pemutusan koneksi antara kedua ujung komunikasi.


TCP adalah protokol yang berorientasi pada koneksi, yang berarti protokol ini mengatur hubungan yang eksplisit dan berkelanjutan antara klien dan server. Untuk melakukan hal ini, TCP menggunakan **nomor urut** dan **pengakuan**: untuk setiap segmen yang dikirim, sebuah pengenal unik diberikan sehingga mesin penerima dapat memeriksa urutan dan integritas data. Penerima kemudian mengembalikan segmen pengakuan dengan **back flag** yang diset ke 1, mengonfirmasi penerimaan dan menunjukkan nomor urut yang diharapkan berikutnya.



![Image](assets/fr/018.webp)



Untuk meningkatkan keandalan, TCP menggunakan pengatur waktu: setelah sebuah segmen dikirim, hitungan mundur dimulai. Jika sebuah acknowledgement tidak sampai dalam periode waktu yang ditentukan, pengirim akan secara otomatis mentransmisikan ulang segmen tersebut, dengan asumsi bahwa segmen tersebut hilang dalam perjalanan. Mekanisme pengiriman ulang otomatis ini mengimbangi kerugian yang melekat pada jaringan IP, yang dapat terjadi dalam kasus kemacetan, kesalahan rute, atau kegagalan perangkat keras.



![Image](assets/fr/019.webp)



TCP mampu mendeteksi dan menangani duplikat. Jika segmen yang ditransmisikan ulang tiba tetapi yang asli juga muncul, penerima menggunakan nomor urut untuk mengidentifikasi duplikat dan hanya menyimpan salinan yang benar, sehingga menghilangkan ambiguitas.


Agar proses ini dapat berjalan, kedua mesin harus memiliki pemahaman yang sama tentang nomor urut awal mereka. Hal ini dipastikan dengan mengikuti prosedur koneksi yang ketat: di satu sisi, **server** mendengarkan pada port tertentu, menunggu permintaan masuk (mode pasif); di sisi lain, **klien** secara aktif memulai koneksi dengan mengirimkan permintaan ke server pada port layanan yang sama.


**CATATAN**: "Port" adalah pengenal numerik (dari 0 hingga 65.535) yang ditetapkan untuk aplikasi jaringan pada komputer. Port ini digunakan untuk membedakan beberapa layanan yang berjalan secara bersamaan pada IP Address yang sama. Ketika klien mengirim data, klien menentukan nomor port sehingga sistem operasi server tahu program mana yang harus menerimanya (misalnya 80 untuk HTTP, 443 untuk HTTPS, 25 untuk SMTP). Port bertindak seperti pintu khusus, mengarahkan lalu lintas masuk dan keluar, mencegah kebingungan antara layanan, dan memungkinkan kontrol akses yang halus melalui firewall atau aturan penyaringan.


Sinkronisasi urutan Exchange didasarkan pada mekanisme **"*jabat tangan tiga arah*" yang terkenal, mirip dengan cara dua orang saling menyapa untuk menjalin kontak. Fase inisialisasi ini, yang memastikan keandalan TCP, berlangsung dalam 3 tahap:

1. **SYN:** Klien mengirimkan segmen sinkronisasi awal (**SYN**) dengan set flag yang sesuai dan nomor urut awal (misalnya, C);

2. **SYN-ACK:** Server penerima merespons dengan segmen pengakuan (**SYN-ACK**), server ini mengakui nomor urut klien dan memberikan nomor urut awalnya sendiri;

3. **ACK:** Klien mengirimkan pengakuan akhir (**ACK**) yang mengonfirmasi penerimaan nomor urut server, menyelesaikan sinkronisasi. Bendera SYN sekarang dinonaktifkan dan bendera ACK tetap disetel untuk mengindikasikan bahwa koneksi telah dibuat.



![Image](assets/fr/020.webp)



Protokol Exchange ini memastikan bahwa kedua belah pihak berbagi basis penomoran yang sama sebelum mentransmisikan data muatan. Setelah sinkronisasi ini selesai, sesi dibuka: segmen sekarang dapat berjalan di kedua arah, masing-masing diakui pada saat diterima, memastikan keandalan aliran data yang maksimal.


Jabat tangan tiga arah ini hanya menyangkut pembentukan koneksi. Untuk penutupan, TCP menggunakan *jabat tangan empat arah*: FIN → ACK → FIN → ACK, yang menjamin bahwa tidak ada segmen dalam perjalanan yang hilang sebelum koneksi benar-benar dilepaskan.


Meskipun dirancang untuk ketahanan dan keandalan, proses ini juga menimbulkan kerentanan yang dapat dieksploitasi. Sebagai contoh, serangan seperti **IP Spoofing** bertujuan untuk mem-bypass atau merusak hubungan kepercayaan ini dengan menyamar sebagai mesin yang sah melalui nomor urut yang dipalsukan, menciptakan celah yang memungkinkan intersepsi atau manipulasi aliran data.


Untuk membatasi risiko pembajakan sinkronisasi urutan dan untuk mengatur beban jaringan, protokol TCP menggunakan teknik manajemen aliran yang dikenal sebagai "**_Sliding Window_**". Sistem ini mengatur berapa banyak data yang dapat dikirim tanpa memerlukan pengakuan langsung untuk setiap segmen, sehingga mengurangi beban berlebih yang tidak perlu pada jaringan sekaligus mempertahankan keandalan yang baik.


Secara praktis, jendela geser mendefinisikan rentang nomor urut yang dapat beredar secara bebas antara pengirim dan penerima tanpa setiap segmen diakui. Saat pengakuan diterima oleh sistem pengirim, jendela "bergeser": jendela bergeser ke kanan sehingga memberi ruang bagi segmen baru untuk dikirim. Ukuran jendela ini (sangat penting untuk mengoptimalkan throughput sambil menghindari kemacetan) ditentukan dalam bidang "*Window*" pada header TCP.


**Contoh**: jika nomor urut awal adalah 3 dan jendela meluas ke urutan 5, segmen bernomor 3 hingga 5 dapat dikirim tanpa menunggu pengakuan individu.



![Image](assets/fr/021.webp)



Ukuran jendela geser tidak tetap; jendela ini menyesuaikan secara dinamis dengan kondisi jaringan dan kapasitas pemrosesan penerima.  Jika penerima dapat menangani volume data yang lebih besar, penerima akan mengindikasikan hal ini melalui bidang Jendela, dan meminta pengirim untuk memperluas jendelanya. Sebaliknya, jika terjadi kelebihan beban atau risiko kejenuhan, penerima dapat meminta pengurangan, pengirim akan menunggu sampai jendela bergerak maju untuk mengirim segmen tambahan.


Protokol ini menyediakan prosedur simetris untuk menutup koneksi TCP untuk memastikan penutupan yang bersih dan teratur. Salah satu mesin dapat memulai penutupan dengan mengirimkan segmen dengan flag **FIN** yang diset ke 1, yang menandakan niatnya untuk mengakhiri komunikasi. Kemudian menunggu sampai semua segmen dalam perjalanan telah diterima dan mengabaikan data lebih lanjut.


Setelah menerima segmen ini, mesin lain akan mengirimkan pengakuan, yang juga ditandai dengan bendera FIN. Kemudian menyelesaikan pengiriman data yang tersisa sebelum memberi tahu aplikasi lokal bahwa sambungan telah ditutup. Konfirmasi ganda ini memastikan pematian yang teratur dan meminimalkan risiko kehilangan data.


Manajemen yang tepat ini, yang menggabungkan perutean fleksibel IP dengan kontrol ketat TCP, sering diilustrasikan dengan diagram yang membandingkan kecepatan protokol IP (yang bekerja berdasarkan **"upaya terbaik", tanpa jaminan pengiriman) dengan keandalan protokol TCP (yang mengelola transmisi melalui pengakuan dan urutan yang dinegosiasikan).



![Image](assets/fr/022.webp)



Namun, dalam beberapa kasus, keandalan mutlak bukanlah prioritas: kecepatan dan kesederhanaan. Hal ini berlaku untuk aplikasi seperti live streaming atau VoIP, yang dapat mentoleransi beberapa kehilangan paket tanpa mempengaruhi pengalaman pengguna secara serius. Dalam kasus seperti itu, **UDP** (_User Datagram Protocol_) lebih disukai.


UDP beroperasi dengan prinsip yang secara fundamental berbeda dari TCP: UDP bersifat **connectionless**, yang berarti tidak ada hubungan yang dibuat antara pengirim dan penerima. Ketika sebuah mesin mengirimkan paket melalui UDP, paket tersebut dikirimkan satu arah; penerima tidak mengirimkan acknowledgement, dan pengirim tidak memiliki konfirmasi bahwa pesan telah sampai. Header UDP sengaja dibuat minimal, hanya berisi port sumber, port tujuan, panjang segmen, dan checksum, tanpa mekanisme pengakuan atau kontrol status. Seperti biasa, alamat IP dibawa oleh header IP yang mendasarinya.


Analogi yang umum adalah bahwa TCP seperti **panggilan telepon**, di mana sebuah sirkuit dibuat, diikuti dan dikontrol selama percakapan berlangsung. Sementara itu, protokol UDP seperti **mengirim surat**, di mana pengirim memasukkan surat ke dalam kotak surat tanpa bukti pengiriman atau umpan balik yang sistematis.


Saling melengkapi antara TCP dan UDP memungkinkan jaringan modern untuk beradaptasi dengan berbagai kebutuhan, memilih keandalan maksimum atau memprioritaskan kecepatan, tergantung pada aplikasinya.



## Primitif layanan


<chapterId>4480afb7-e950-4ccb-88fa-d132f9dc3479</chapterId>



### Arsitektur berlapis dan organisasi Exchange


Seperti yang telah kita lihat, **layanan** adalah implementasi konkret dari protokol yang telah kami jelaskan sejauh ini. Meskipun model TCP/IP berbeda dengan model **OSI**, model ini mengadopsi pendekatan berlapis yang sama: setiap Layer dirancang untuk menjalankan fungsi tertentu dan menyediakan **layanan** kepada Layer yang berada tepat di atasnya, sehingga menghasilkan arsitektur yang modular, kuat, dan mudah dipelihara.


Setiap Layer dibangun di atas kemampuan yang ada di bawahnya, dan pada gilirannya menyediakan Layer di atasnya dengan Interface yang konsisten untuk mengelola data. Dalam arsitektur ini, setiap Layer memiliki **struktur data** sendiri, yang ditentukan secara hati-hati untuk memastikan kompatibilitas yang sempurna dengan lapisan lainnya. Kompatibilitas ini sangat penting untuk komunikasi yang lancar, andal, dan jelas dari satu titik akhir ke titik lainnya.


Ada dua aspek utama yang mengatur pertukaran ini:


- Aspek vertikal**: hubungan antara satu Layer dengan Layer di atas atau di bawahnya (dari Layer N ke Layer N+1, dan sebaliknya).



![Image](assets/fr/023.webp)




- Aspek horizontal**: interaksi antara aplikasi jarak jauh, yaitu dialog antara **klien** dan **server**, di kedua arah.



![Image](assets/fr/024.webp)



Arsitektur berlapis mengikuti prinsip bahwa setiap Layer hanya memproses informasi dalam cakupannya: struktur data, header, dan mekanisme kontrol bervariasi dari satu Layer ke Layer lainnya, tetapi bersama-sama mereka membentuk sistem yang koheren, memastikan data secara bertahap dialihkan ke tujuan akhirnya.


**Pengingat**: Terminologi khusus digunakan untuk menjelaskan unit data yang dipertukarkan antar lapisan:


- pesan** untuk Aplikasi Layer,
- segmen** untuk Transport Layer (TCP),
- datagram** untuk Internet Layer (IP),
- frame** untuk Akses Jaringan Layer.


Tabel di bawah ini meringkas istilah-istilah untuk konteks TCP dan UDP:


| TCP/IP Layer         | Unit Name (TCP) | Unit Name (UDP) |
|----------------------|------------------|------------------|
| Application Layer    | Stream           | Message          |
| Transport Layer      | Segment          | Packet           |
| Internet Layer       | Datagram         | Datagram         |
| Network Access Layer | Frame            | Frame            |

### Primitif layanan dan unit data


Inti dari sistem ini adalah **service primitives**, yang bertindak sebagai antarmuka komunikasi. Primitif ini berfungsi seperti meja layanan, mendengarkan **port** khusus yang dipesan dan memungkinkan proses untuk membangun, memelihara, dan mengakhiri koneksi jaringan dengan cara yang terkendali. Sementara protokol mengatur format dan transmisi data di seluruh jaringan, **layanan dan primitifnya** yang menyediakan hubungan vertikal antara lapisan.


Dengan menggabungkan aspek horizontal (komunikasi antara aplikasi terdistribusi) dengan aspek vertikal (interaksi internal antar lapisan), model TCP/IP memberikan arsitektur yang lengkap dan terukur. Tumpang tindihnya kedua perspektif ini memberikan gambaran yang jelas tentang bagaimana data dipertukarkan dalam komunikasi jaringan yang terstruktur.



![Image](assets/fr/026.webp)



### Ringkasan bagian


Pada bagian utama pertama ini, kami menjelajahi arsitektur inti yang mengatur konfigurasi dan pengoperasian jaringan yang terhubung ke Internet saat ini. Arsitektur ini didasarkan pada model **four-Layer**, yang terinspirasi oleh model OSI, dan dibangun di sekitar rangkaian protokol **TCP/IP**, yang merupakan tulang punggung komunikasi modern. Kami melihat bahwa TCP, dengan pendekatan yang berorientasi pada koneksi, memastikan transfer yang andal, sementara UDP, lebih ringan dan lebih cepat, lebih disukai ketika kecepatan lebih penting daripada keandalan.


Fungsi yang tepat dari model ini bergantung pada implementasi protokol melalui **layanan primitif**. Hal ini memastikan hubungan antar lapisan, sehingga memungkinkan pemrosesan data disesuaikan dengan kebutuhan spesifik dari setiap tingkat, dari transportasi ke aplikasi, termasuk akses Internet dan jaringan. Pendekatan modular ini membuat sistem menjadi fleksibel dan kuat.


Pengalamatan IP adalah landasan lain dari infrastruktur ini. Setiap perangkat yang terhubung diidentifikasi dengan **IP Address yang unik**, yang diambil dari ruang Address yang diorganisasikan ke dalam **kelas** (dari A hingga E). Beberapa alamat ini dicadangkan untuk tujuan khusus, seperti loopback lokal atau multicast, sementara yang lain, yang dikenal sebagai "alamat privat", tidak dialihkan melalui Internet tanpa terjemahan (NAT). Klasifikasi ini memungkinkan organisasi jaringan yang logis dan hirarkis.


Kami juga memeriksa konsep **subnetworks**, yang memungkinkan untuk membagi segmen jaringan untuk mengelola sumber daya IP dengan lebih baik dan mengoptimalkan aliran data. Meskipun pembagian manual menggunakan subnet mask tetap menjadi prinsip penting, sebagian besar telah dimodernisasi berkat **CIDR** (_Routing Antar Domain Tanpa Kelas_). Metode ini telah mengubah manajemen Address dengan memungkinkan alokasi rentang IP yang lebih fleksibel dan rasional, sekaligus mengurangi ukuran tabel perutean.


Dengan menguasai konsep-konsep ini - lapisan, protokol, primitif layanan, pengalamatan dan subnetting - Anda akan mendapatkan dasar yang kuat untuk memahami cara kerja teknis jaringan modern, dan untuk mengonfigurasi infrastruktur jaringan secara efisien untuk memenuhi kebutuhan saat ini.


Pada bagian berikutnya, kita akan melihat lebih dekat pada pengalamatan IPv4.



# Pengalamatan IPv4


<partId>83f3c3e5-378c-440f-a095-df210842efde</partId>



## Menggunakan IPv4


<chapterId>79e4dd18-446a-435b-9f25-c88a00f8bec6</chapterId>



Pada bagian ini, kita akan membahas lebih dalam dan melihat bagaimana alamat **IPv4** diimplementasikan dalam jaringan dunia nyata. Kami akan menguraikan formatnya, logika di baliknya, dan bagaimana alamat-alamat tersebut terhubung dengan Elements jaringan utama lainnya seperti **nama DNS**, **alamat MAC**, **subjaringan**, dan **teknik penerjemahan**.


IP Address adalah pengenal numerik unik yang ditetapkan untuk setiap **jaringan Interface** pada perangkat. Hal ini memungkinkan untuk menemukan perangkat ini dalam jaringan dan menjangkaunya untuk mengirimkan data. Sebagai contoh, router, server, workstation, printer jaringan, atau bahkan kamera pengintai memiliki setidaknya satu IP Address sendiri. IP Address memungkinkan **routing**, yaitu memindahkan paket dari titik A ke titik B, meskipun secara fisik berjauhan.


Alamat IP dapat ditetapkan dengan dua cara utama:


- Statis**: Diatur secara manual pada perangkat.
- Dinamis**: Ditetapkan secara otomatis sesuai permintaan oleh server DHCP (_Dynamic Host Configuration Protocol_). DHCP menyederhanakan manajemen jaringan, sehingga tidak memerlukan konfigurasi manual dan memungkinkan kontrol yang tepat melalui reservasi dan durasi sewa.


*alamat *IPv4** ditulis dalam format **32-bit** yang dibagi menjadi **empat byte**. Setiap byte berisi 8 bit dan mewakili angka desimal dari 0 hingga 255. Keempat byte dipisahkan oleh titik-titik untuk membentuk notasi yang jelas dan mudah dibaca.


contoh: Address 172.16.254.1_



![Image](assets/fr/027.webp)



Setiap bit dalam byte memiliki nilai (atau "bobot"): bit sebelah kiri (bit yang paling signifikan) bernilai 128, 64 berikutnya, lalu 32, 16, 8, 4, 2, dan 1 untuk bit sebelah kanan (bit yang paling tidak signifikan). Dengan cara ini, penulisan biner dikonversi ke desimal dengan penambahan sederhana dari bobot yang ditetapkan.


Tabel di bawah ini mengilustrasikan korespondensi ini:



| Binary Code | Activated Bit Values          | Decimal Value |
|-------------|-------------------------------|---------------|
| 00000000    | 0                             | 0             |
| 00000001    | 1                             | 1             |
| 00000011    | 1 + 2                         | 3             |
| 00000111    | 1 + 2 + 4                     | 7             |
| 00001111    | 1 + 2 + 4 + 8                 | 15            |
| 00011111    | 1 + 2 + 4 + 8 + 16            | 31            |
| 00111111    | 1 + 2 + 4 + 8 + 16 + 32       | 63            |
| 01111111    | 1 + 2 + 4 + 8 + 16 + 32 + 64  | 127           |
| 11111111    | 1 + 2 + 4 + 8 + 16 + 32 + 64 + 128 | 255      |

Untuk mengonversi biner ke desimal, tambahkan bobot bit yang ditetapkan ke 1.


| Binary     | Decimal Value |
| ---------- | ------------- |
| `10101100` | 172           |
| `00010000` | 16            |
| `11111110` | 254           |
| `00000001` | 1             |

IP Address mengidentifikasi satu **jaringan Interface**, bukan seluruh perangkat. Router multi-port atau firewall memiliki beberapa antarmuka, masing-masing dengan IP Address-nya sendiri. Satu Interface bahkan dapat memiliki beberapa alamat IP (misalnya, untuk melayani beberapa jaringan atau layanan virtual).


Setiap paket IP berisi dua alamat IP dalam headernya:


- Sumber Address (**pengirim**)
- Tujuan Address (**penerima**)

Router membaca alamat-alamat ini untuk mengetahui jalur terbaik untuk mengirim paket hingga mencapai tujuan. Tanpa aturan pengalamatan yang ketat, lalu lintas jaringan tidak dapat dirutekan dengan benar dan interkoneksi global jaringan tidak mungkin dilakukan.


IPv4 Address memiliki dua bagian:


- NetID**: mengidentifikasi jaringan
- HostID**: mengidentifikasi perangkat di dalam jaringan tersebut

Subnet mask** menentukan di mana NetID berakhir dan HostID dimulai, menentukan berapa banyak bit yang dimiliki oleh masing-masing bagian. Semakin panjang NetID, semakin besar jumlah subnet yang mungkin, tetapi jumlah host per subnet berkurang.


Pada awalnya, jaringan IPv4 dibagi menjadi lima **kelas**: (A, B, C, D, dan E). Setiap kelas berhubungan dengan rentang NetID tertentu dan mendefinisikan perincian yang tetap:


- Kelas A: jaringan yang sangat besar dengan jumlah host yang banyak
- Kelas B: jaringan berukuran sedang
- Kelas C: jaringan kecil
- Kelas D: alamat yang dicadangkan untuk multicasting (_multicast_)
- Kelas E: alamat eksperimental, tidak digunakan untuk pengalamatan konvensional



| Class | Leading Bits | First Byte Range | Default Subnet Mask | Purpose                          |
| ----- | ------------ | ---------------- | ------------------- | -------------------------------- |
| A     | 0            | 0 – 127          | 255.0.0.0           | Very large networks              |
| B     | 10           | 128 – 191        | 255.255.0.0         | Medium-sized networks            |
| C     | 110          | 192 – 223        | 255.255.255.0       | Small networks                   |
| D     | 1110         | 224 – 239        | N/A                 | Multicast addresses              |
| E     | 1111         | 240 – 255        | N/A                 | Experimental (not publicly used) |

Alamat Khusus:


- Jaringan Address**: Mengidentifikasi jaringan itu sendiri (digunakan dalam tabel perutean).
- Menyiarkan Address**: Mengirimkan data ke semua perangkat dalam subnet sekaligus (semua bit HostID diatur ke 1).


Rentang berikut ini dicadangkan untuk penggunaan internal:


- 10.0.0.0/8** (Kelas Privat A)
- 127.0.0.0/8** (loopback lokal atau _loopback_)
- 172.16.0.0 hingga 172.31.255.255** (Kelas B pribadi)
- 192.168.0.0 hingga 192.168.255.255** (Kelas C pribadi)


Alamat **127.0.0.1** dan, secara umum, seluruh rentang 127.0.0.0/8 digunakan untuk pengujian internal: permintaan apa pun yang dikirim ke alamat tersebut tidak pernah meninggalkan mesin. Hal ini berguna untuk memeriksa apakah layanan jaringan lokal bekerja tanpa melibatkan jaringan yang lebih luas.


Untuk memanfaatkan ruang Address dengan lebih baik, administrator sering membagi jaringan ke dalam **subnet** menggunakan subnet mask atau notasi **CIDR** (_Routing Antar Domain Tanpa Kelas_). CIDR memungkinkan manajemen yang lebih tepat dan membantu menghindari pemborosan alamat. Saat ini, CIDR sangat penting untuk menyempurnakan rentang IP dan mengurangi ukuran tabel perutean.


Dalam jaringan modern, pengalamatan IP biasanya dipasangkan dengan pengenal lain:



- nama domain** yang terdaftar dalam **DNS** (Sistem Nama Domain): Sistem ini mengaitkan IP numerik Address dengan nama yang mudah diingat.
- MAC Address**: pengenal fisik yang terukir pada kartu jaringan, digunakan untuk transportasi lokal (_Ethernet_). Ketika paket IP perlu ditransmisikan secara fisik, tabel ARP mencocokkan IP Address dengan MAC Address tujuan.


Untuk mengatasi kekurangan IPv4 Address dan untuk menambahkan keamanan Layer, jaringan sering menggunakan terjemahan Address (_NAT_). NAT memungkinkan banyak perangkat pribadi untuk berbagi satu IP publik Address ketika mengakses Internet.


**Catatan**: Alat bantu OS online dan built-in, seperti [kalkulator Grenoble CRIC](http://cric.grenoble.cnrs.fr/Administrateurs/Outils/CalculMasque/), membuat penghitungan subnet dan mask menjadi lebih mudah.

Utilitas ini membantu merencanakan pemisahan jaringan secara efisien.


Kesimpulannya, broadcast Address tetap merupakan fungsi praktis untuk mengirim pesan yang sama ke semua perangkat yang terhubung ke sebuah segmen: hal ini dicapai dengan mengatur semua bit pada bagian HostID ke 1 sehingga semua host menjadi sasaran.



## Berbagai jenis IPv4 Address yang berbeda


<chapterId>2adfad24-a90d-45b5-b808-3d2f6598bebf</chapterId>



Alamat IPv4 terbagi dalam dua kategori utama: alamat publik, yang dapat diakses secara langsung di Internet, dan alamat privat, yang ditujukan untuk penggunaan internal dalam jaringan lokal.


IPv4 Address publik bersifat unik secara global dan dapat dirutekan di Internet. IPv4 publik diberikan oleh otoritas resmi dan diperlukan untuk layanan yang berhadapan dengan publik seperti situs web, server email, atau infrastruktur cloud.

Keunikan alamat-alamat ini di seluruh dunia sangat penting untuk menghindari konflik atau tabrakan perutean.


IANA (Otoritas Penugasan Nomor Internet), yang beroperasi di bawah **ICANN** (Perusahaan Internet untuk Nama dan Nomor yang Ditugaskan), mengelola distribusi rentang IP ini. Secara konkret, IANA membagi ruang IPv4 menjadi 256 blok dengan ukuran /8, menurut notasi CIDR. Setiap blok mewakili lebih dari 16,7 juta alamat (2³² / 2⁸).


Blok Address unicast ini dipercayakan oleh IANA kepada **Regional Internet Registries** (RIR). RIR ini bertanggung jawab untuk mendistribusikan kembali alamat di tingkat regional, sesuai dengan kebutuhan nyata dari penyedia akses, perusahaan, atau administrasi. Ruang unicast Address terbentang dari blok **1/8 hingga 223/8**, dengan bagian yang dicadangkan untuk penggunaan khusus (penelitian, dokumentasi, pengujian), atau dialokasikan secara langsung ke jaringan atau RIR untuk didistribusikan kembali.


Untuk memeriksa siapa yang memiliki IP publik Address, Anda bisa melihat basis data RIR dengan menggunakan perintah **whois**, atau dengan menggunakan antarmuka web yang disediakan oleh masing-masing registri. Alat-alat ini dapat digunakan untuk melacak Address kembali ke organisasi atau penyedia yang mendeklarasikannya.


Sebaliknya, ada alamat IPv4 pribadi, sebuah respons praktis terhadap kekurangan alamat publik. Alamat-alamat ini, yang tidak dapat dirutekan di Internet, dicadangkan untuk lingkungan lokal: jaringan perusahaan, LAN rumah, pusat data, atau cluster komputasi. Alamat ini tidak unik di seluruh dunia: banyak jaringan pribadi dapat menggunakan kembali rentang IP yang sama tanpa gangguan, selama mereka tetap terisolasi atau menggunakan perangkat penerjemah jaringan Address untuk mengakses internet.


Untuk mengizinkan perangkat dengan IP Address pribadi mengakses Internet, jaringan menggunakan NAT (Network Address Translation). NAT bekerja dengan secara dinamis mengganti Address pribadi dengan Address publik, sehingga memungkinkan lusinan (atau bahkan ratusan) perangkat untuk berbagi satu IP Address publik. Metode ini mengoptimalkan penggunaan ruang IPv4 dan juga menambahkan keamanan Layer dengan menyembunyikan struktur jaringan internal.


Kategori khusus lainnya adalah alamat **tidak ditentukan**. Notasi IPv4 **0.0.0.0** atau versi IPv6 **::/128** berarti "tidak ada Address tertentu". Address seperti itu tidak valid sebagai tujuan Address jaringan, tetapi dapat digunakan secara lokal oleh host untuk menunjukkan "semua antarmuka" atau "belum ada Address yang ditetapkan". Hal ini biasa terjadi pada DHCP dinamis Assignment atau untuk mendengarkan semua antarmuka server.


IPv6 juga mendukung pengalamatan privat, tetapi standar umumnya merekomendasikan pengalamatan publik untuk menghindari penumpukan beberapa lapisan NAT. Alamat **site-local** (_site-local_) dari blok **fec0::/10** sudah tidak digunakan lagi oleh **RFC 3879** untuk alasan konsistensi dan keamanan. Mereka digantikan dengan **Alamat Lokal Unik** (_ULA_) yang terletak di blok **fc00::/7**. ULA memungkinkan pembuatan jaringan IPv6 pribadi dengan perutean internal yang bersih, menggunakan pengenal 40-bit yang dibuat secara acak untuk memastikan keunikan lokal.


Habisnya IPv4 secara resmi dikonfirmasi pada tahun 2011. Untuk memperpanjang masa pakainya, komunitas Internet mengadopsi beberapa strategi:


- Migrasi bertahap ke **IPv6**
- Penggunaan **NAT** secara luas
- Kebijakan alokasi yang lebih ketat dari RIR, yang membutuhkan justifikasi dan manajemen kebutuhan Address yang tepat
- Pemulihan blok Address yang tidak terpakai atau dikembalikan secara sukarela oleh perusahaan


Langkah-langkah ini menunjukkan bahwa pengalamatan IP bukan hanya merupakan tantangan teknis, tetapi juga masalah tata kelola global, yang merupakan pusat dari ekspansi Internet yang sedang berlangsung.



## DNS, sebuah direktori Address


<chapterId>511244ec-ba43-44ac-b4c3-b41579a15cff</chapterId>



Jujur saja, manusia tidak pandai menghafal deretan angka yang panjang, baik dalam bentuk biner maupun desimal. Tantangan ini menjadi lebih besar lagi dengan alamat IP, yang bisa jadi rumit dan satu IP Address terkadang bisa menyembunyikan beberapa alamat, terutama ketika teknik seperti NAT atau hosting virtual terlibat.


Untuk mempermudah, Aplikasi Layer menggunakan sistem yang menghubungkan IP Address ke nama yang logis dan dapat dibaca manusia. Ini adalah peran **DNS** (*Domain Name System*), sebuah direktori besar, hirarkis, dan terdistribusi yang mencocokkan nama domain yang dapat dibaca dengan alamat IP. Sistem ini didasarkan pada seperangkat protokol dan layanan. Perangkat lunak server DNS yang paling banyak digunakan adalah **BIND** (_Berkeley Internet Name Domain_), sebuah paket perangkat lunak sumber terbuka yang menjadi referensi sebagian besar infrastruktur DNS Internet.


Ide inti di balik DNS adalah sederhana: untuk semua layanan yang terhubung, baik situs web, server email, atau layanan jaringan lainnya, ada catatan yang memetakan nama domain ke satu atau beberapa alamat IP. Ini bekerja dalam dua arah:


- Resolusi maju: menerjemahkan nama menjadi IP Address.
- Resolusi terbalik: menemukan nama domain yang terkait dengan IP Address yang diberikan.

Hal ini membuat pengalamatan jaringan dapat digunakan oleh manusia sekaligus menjaga ketepatan yang dibutuhkan router untuk memindahkan data dengan benar.


Nama domain selalu terstruktur secara hierarkis, dengan setiap tingkat dipisahkan oleh sebuah titik: nama lengkapnya disebut **FQDN** (_Fully Qualified Domain Name_). Bagian paling kanan adalah **TLD** (_Top Level Domain_) seperti `.com`, `.org`, atau `.fr`. Bagian paling kiri menunjukkan host, yaitu mesin atau layanan tertentu yang terhubung ke IP Address.


Sistem DNS dirancang sebagai **pohon zona**. Sebuah **zona** adalah bagian dari ruang nama domain yang dikelola oleh server DNS tertentu. Satu zona dapat berisi beberapa **subdomain**, yang dapat didelegasikan ke zona lain yang dikelola oleh server yang berbeda. Administrator bertanggung jawab untuk mengelola zona mereka: menangani pembaruan, pendelegasian, dan manajemen secara keseluruhan.


Struktur ini memungkinkan tidak hanya untuk menunjuk ke domain utama (misalnya `example.com`), tetapi juga menyempurnakan catatan untuk masing-masing host (`www`, `mail`, `ftp`, dan lain-lain). Pada masa awal jaringan, pemetaan ini ditangani dengan file statis seperti (`/etc/hosts` pada sistem Unix), tetapi metode seperti itu dengan cepat menjadi tidak praktis untuk Internet yang berkembang pesat dan saling terhubung.


Penting untuk dipahami bahwa server DNS hanya dapat melayani cakupan yang terbatas. Sebagai contoh, server DNS internal perusahaan mungkin tidak dapat diakses secara langsung dari Internet. Jika DNS ini tidak dikonfigurasi untuk meneruskan kueri, atau tidak memiliki hubungan tepercaya dengan server lain, beberapa kueri akan gagal: baik nama maupun IP Address tidak dapat diselesaikan di luar zona yang ditentukan.


DNS juga berperan dalam perutean email. Sebagai contoh, catatan **MX** (_Mail Exchange_) menentukan server email yang bertanggung jawab untuk menerima email untuk domain tertentu. Catatan ini menentukan prioritas (faktor pembobotan) dan solusi failover. File zona server DNS harus berisi record **SOA** (_Start Of Authority_), yang menunjuk server sebagai sumber informasi resmi untuk zona tersebut.


Berkat struktur hirarkis dan terdistribusi, DNS tetap menjadi landasan Internet, memungkinkan pengguna untuk mengakses layanan melalui nama domain yang jelas dan mudah diingat, bukannya alamat IP yang panjang dan teknis.


Pada bab berikutnya, kita akan menjelajahi konsep mendasar lainnya: **Alamat Ethernet, juga dikenal sebagai alamat MAC, yang memastikan pengiriman data pada Layer fisik jaringan lokal.



## Menemukan alamat Ethernet dan ARP


<chapterId>d02109f6-9bf9-4261-a8f9-e1aa4398b949</chapterId>



### Definisi


Agar protokol perutean data dapat bekerja dengan andal dan konsisten, ada satu komponen kunci yang sangat penting. Sebagai manusia, kita dapat dengan mudah mengenali sebuah mesin dari IP Address atau dari namanya yang diambil melalui DNS. Namun, sebuah mesin harus dapat mengenali perangkat tujuan dengan jelas untuk mengirimkan paket. Untuk melakukan hal ini, mesin bergantung pada pengenal perangkat keras tertentu, yang secara langsung digunakan oleh jaringan Interface: MAC Address (_Media Access Control_).


**Catatan**: Ini tidak ada hubungannya dengan "Address fisik" dalam arsitektur memori. Dalam komputasi, memori fisik Address mengacu pada lokasi tertentu pada bus memori, berlawanan dengan Address virtual yang dikelola oleh sistem operasi. Sebaliknya, MAC Address hanya berhubungan dengan perangkat keras jaringan.


MAC Address diberikan secara permanen dan unik oleh produsen tempat peralatan tersebut diproduksi. MAC Address dengan tegas mengidentifikasi kartu jaringan apakah itu komputer, ponsel cerdas, printer, atau perangkat lain yang terhubung. Tidak seperti IP Address, yang dapat berubah secara dinamis (melalui server DHCP atau konfigurasi manual), MAC Address biasanya tetap sama selama masa pakai perangkat, kecuali jika sengaja diubah.


Setiap jaringan Interface, berkabel atau nirkabel, memiliki MAC Address sendiri. Address ini digunakan dalam tautan data Layer (Layer 2 model OSI) untuk memasukkan dan mengelola perangkat keras Address dalam setiap frame jaringan yang dipertukarkan. Hal ini kadang-kadang disebut sebagai alamat Ethernet atau UAA (Alamat yang Diatur Secara Universal). Dibakukan dengan panjang 48 bit, atau 6 byte, ditulis dalam notasi heksadesimal, umumnya dalam bentuk byte yang dipisahkan dengan `:` atau `-`.


Sebagai contoh: `5A:BC:17:A2:AF:15`


Dalam struktur ini, tiga byte pertama mengidentifikasi produsen kartu jaringan: ini dikenal sebagai **OUI** (*Organisationally Unique Identifier*). Awalan ini, yang ditetapkan oleh IEEE, juga digunakan dalam skema pengalamatan perangkat keras lainnya, seperti Bluetooth dan LLDP, untuk menjamin keunikan di seluruh dunia.


### Mengubah MAC Address (MAC Spoofing)


Secara teori, MAC Address dirancang untuk tetap tetap, tetapi ada beberapa cara untuk memodifikasinya, terutama untuk memenuhi kebutuhan tertentu atau untuk menghindari kendala tertentu. Operasi ini, yang sering disebut sebagai _spoofing MAC_, melibatkan penggantian perangkat keras asli Address dengan nilai yang berbeda, yang ditentukan pada tingkat perangkat lunak. Beberapa sistem operasi memfasilitasi modifikasi ini, terutama ketika Ethernet Address yang sebenarnya tidak secara langsung digunakan oleh driver.


Alasan untuk perubahan tersebut bervariasi. Bisa jadi karena kebutuhan aplikasi tertentu yang memerlukan Ethernet Address tertentu agar dapat berfungsi dengan baik, atau untuk menyelesaikan konflik alamat yang sama antara dua perangkat yang berbagi jaringan lokal yang sama.


Mengubah MAC Address juga dapat dimotivasi oleh pertimbangan privasi: dengan menyembunyikan pengenal unik yang terukir pada kartu, pengguna mengurangi kemungkinan perangkat mereka dilacak oleh jaringan atau layanan pengawasan. Namun, praktik ini bukannya tanpa konsekuensi. Mengganti MAC Address dapat mengganggu perangkat penyaringan tertentu, atau mengharuskan firewall dikonfigurasi ulang untuk mengesahkan perangkat keras yang baru.


Beberapa jaringan, khususnya Wi-Fi, menggunakan penyaringan MAC Address untuk mengizinkan hanya perangkat dengan alamat yang disetujui. Meskipun hal ini menambah tingkat kontrol dasar, namun tidak aman dengan sendirinya. Seorang penyerang dapat menangkap MAC Address yang valid yang sudah diotorisasi di jaringan dan mengkloningnya untuk menerobos pembatasan. Untuk alasan ini, penyaringan MAC harus selalu dikombinasikan dengan langkah-langkah keamanan yang lebih kuat.


### Korespondensi MAC/IP


Agar jaringan lokal dapat bekerja secara efisien, harus ada pemetaan yang jelas antara alamat fisik (alamat MAC) dan alamat logis (alamat IP). Tanpa hubungan ini, sebuah komputer mungkin mengetahui IP Address dari sebuah tujuan tetapi tidak akan tahu bagaimana cara mengirim data secara fisik ke tujuan tersebut di jaringan lokal.

Pemetaan ini ditangani secara otomatis oleh ARP (_Address Resolution Protocol_).


Dalam praktiknya, ketika pengguna ingin mengetahui MAC Address yang sesuai dengan IP Address tertentu, pengguna dapat menggunakan utilitas `arp`. Alat ini memeriksa tabel ARP lokal mesin untuk menampilkan kecocokan yang diketahui antara alamat IP dan alamat MAC pada jaringan lokal. Dengan cara ini, memungkinkan untuk memverifikasi hubungan yang efektif antara lapisan logis dan fisik dengan cepat.


Contoh praktis: jika Anda ingin memeriksa kartu jaringan mana yang sesuai dengan IP Address `192.168.1.5`, gunakan perintah berikut:


```bash
arp –a 192.168.1.5
```


Output akan menampilkan Address fisik (MAC) yang terkait, sifat input (statis atau dinamis) dan Interface yang bersangkutan.


```
Interface: 192.168.1.5 --- 0x5
IP Address            MAC Address                Type
192.168.1.5           00:54:BC:17:14:6E          D
```


Penting untuk diingat bahwa MAC Address dan IP Address adalah dua pengidentifikasi yang sama sekali berbeda, namun saling melengkapi. MAC Address diukir secara unik pada setiap jaringan Interface oleh produsen dan digunakan untuk mengidentifikasi perangkat secara fisik pada jaringan lokal. IP Address, di sisi lain, adalah Address logis yang ditetapkan secara dinamis atau statis, yang memungkinkan mesin untuk bergabung dengan jaringan IP dan paket Exchange di luar jaringan lokalnya.



- Contoh visual dari MAC Address:


![Image](assets/fr/032.webp)




- Contoh visual dari IP Address:


![Image](assets/fr/027.webp)



Dalam lingkungan perusahaan, kedua tingkat pengalamatan ini tidak dapat berfungsi secara terpisah. Misalnya, ketika server DHCP secara otomatis menetapkan IP Address, MAC Address peralatan digunakan sebagai titik awal. Komputer mengirimkan permintaan siaran DHCP yang berisi MAC Address sehingga server dapat menetapkan IP Address yang tersedia ke perangkat yang benar. Tanpa identifikasi perangkat keras ini, server DHCP tidak akan tahu ke perangkat mana Address akan dikirimkan.


Oleh karena itu, protokol ARP sangat penting: protokol ini menyediakan hubungan antara alamat IP dan alamat fisik, sehingga memungkinkan mesin untuk menerjemahkan tujuan logis menjadi tujuan fisik yang sebenarnya. Ketika sebuah komputer perlu mengirim paket ke mesin di jaringan yang sama, komputer pertama-tama akan melihat tabel ARP untuk memeriksa apakah MAC Address penerima sudah diketahui. Jika belum, komputer akan menyiarkan permintaan ARP ke semua host di jaringan lokal. Mesin yang mengenali IP Address target dalam permintaan ini merespons dengan menentukan MAC Address-nya. Pengirim kemudian menulis pasangan IP/MAC ini ke cache ARP-nya, untuk menghindari pengulangan operasi setiap kali permintaan dikirim.


Tabel ARP ini bertindak sebagai direktori pemetaan mini, yang secara dinamis diupdate dengan cara yang sama seperti DNS yang mengasosiasikan nama domain dengan alamat IP. Tanpa ARP, tidak ada Exchange lokal yang dapat digunakan, karena sambungan data Layer perlu mengetahui MAC Address agar dapat mengenkapsulasi frame Ethernet dengan benar.


Sebaliknya, protokol RARP (_Reverse Address Resolution Protocol_) dirancang untuk situasi yang berlawanan: memungkinkan mesin yang hanya mengetahui MAC Address untuk menemukan IP Address-nya. Hal ini biasa terjadi pada workstation lama yang tidak memiliki disk Hard lokal, yang harus melakukan booting melalui jaringan dan meminta IP Address. RARP akhirnya digantikan oleh **BOOTP** dan kemudian **DHCP**, yang lebih fleksibel dan otomatis.


Protokol asosiasi ini memainkan peran penting dalam perutean. Router pada dasarnya adalah mesin dengan beberapa antarmuka jaringan, yang menghubungkan segmen yang berbeda. Ketika router menerima sebuah frame, router memprosesnya untuk mengekstrak datagram IP dan memeriksa header IP untuk menentukan tujuan. Jika tujuan berada di jaringan yang terhubung langsung, datagram dikirim langsung setelah memperbarui header. Jika tujuan berada di jaringan lain, router akan melihat tabel routing untuk mengidentifikasi jalur terbaik, atau _next hop_, ke tujuan.


Hal ini memecah rute menjadi beberapa segmen yang lebih pendek dan lebih mudah dikelola. Setiap router perantara hanya mengetahui langkah berikutnya, tidak harus tujuan akhir.


**Pengingat:** Pengiriman langsung terjadi ketika pengirim dan penerima berada pada jaringan fisik yang sama. Jika tidak, pengiriman tidak langsung dan melewati satu atau beberapa router.


Tabel perutean, yang dikelola secara manual (perutean statis) atau dinamis (perutean dinamis), berisi informasi yang diperlukan untuk memutuskan rute mana yang akan diambil. Dalam jaringan kecil, konfigurasi statis sudah cukup. Dalam infrastruktur yang lebih besar, perutean dinamis sangat penting untuk secara otomatis menyesuaikan rute ketika topologi berubah atau sebuah sambungan terputus.


Tabel perutean bertindak sebagai tabel pemetaan antara alamat IP target dan gateway berikutnya. Tabel ini biasanya menyimpan pengenal jaringan (_network ID_) daripada setiap host Address, yang sangat mengurangi ukurannya.


| Destination Address | Next-Hop Router Address | Interface |
| ------------------- | ----------------------- | --------- |

Dengan menggunakan entri ini, router dapat dengan cepat menentukan melalui Interface mana dan ke node mana setiap datagram harus dikirim. Dikombinasikan dengan ARP untuk menyelesaikan alamat MAC yang cocok, hal ini memastikan transfer data yang efisien dan dapat diandalkan di seluruh jaringan.


Terakhir, protokol perutean dinamis mencakup standar seperti RIP (_Routing Information Protocol_), berdasarkan algoritma jarak, dan OSPF (_Open Shortest Path First_), yang menghitung jalur terpendek dalam topologi yang kompleks. Protokol-protokol ini secara terus-menerus diperbarui Exchange untuk mengoptimalkan rute, mengurangi biaya transmisi, dan meningkatkan ketahanan terhadap pemadaman atau kemacetan.



## NAT: Address Terjemahan


<chapterId>4f984d5d-f2e0-4faf-b703-ff315f32cef4</chapterId>



### Definisi


Network Address Translation_ (NAT) adalah sebuah teknik yang dikembangkan untuk mengatasi penipisan alamat IPv4 yang tersedia secara bertahap. Dirancang sebagai solusi sementara sebelum adopsi IPv6 secara luas, NAT memungkinkan perusahaan dan individu untuk terus menghubungkan sejumlah besar mesin sementara hanya menggunakan satu set alamat IP publik yang terbatas.


**Pengingat penting:** Perpindahan dari IPv4 ke IPv6 secara teoritis memecahkan masalah kelelahan dengan memperluas ruang Address dari 32 bit ke 128 bit, menyediakan jumlah alamat yang hampir tidak terbatas (2^128). Namun dalam praktiknya, transisi ini masih belum selesai, dan NAT masih digunakan secara luas hingga saat ini.


Prinsip di balik NAT sederhana namun sangat efektif: alih-alih menetapkan IP publik Address yang unik untuk setiap perangkat di jaringan internal, satu Address yang dapat dirutekan (atau sekumpulan kecil alamat) digunakan untuk semua perangkat pribadi. Gateway NAT, yang sering diintegrasikan ke dalam router atau firewall, kemudian secara dinamis menerjemahkan IP internal Address bersama dengan informasi yang diperlukan untuk merutekan trafik dengan benar ke dunia luar, dan memastikan bahwa respons dikembalikan ke pengirim asli.


Pendekatan ini memiliki manfaat langsung: menyembunyikan arsitektur jaringan internal sepenuhnya. Bagi pengamat luar, semua permintaan dari workstation, server atau printer tampak berasal dari identitas publik yang sama. Alamat privat, biasanya diambil dari rentang yang telah dipesan (misalnya 192.168.x.x atau 10.x.x.x), tetap tidak terlihat dari Internet.


Selain mengatasi kelangkaan IPv4, NAT juga memperkuat keamanan dengan menciptakan penghalang logis pertama antara jaringan internal dan publik. Komunikasi masuk yang tidak diminta secara alami diblokir, karena hanya koneksi yang dimulai dari dalam jaringan yang mendapatkan manfaat dari terjemahan yang diperlukan untuk menerima tanggapan.



![Image](assets/fr/035.webp)



### Jenis terjemahan


NAT dapat diimplementasikan dengan berbagai cara untuk memenuhi kebutuhan tertentu. Dua mode operasi utama adalah terjemahan statis dan terjemahan dinamis.


**Terjemahan statis** menciptakan pemetaan tetap antara IP Address pribadi dan IP Address publik. Setiap mesin internal terhubung secara permanen ke Address publik khusus. Sebagai contoh, perangkat internal yang dikonfigurasi sebagai 192.168.20.1 dapat dihubungkan dengan Address yang dapat dirutekan 157.54.130.1. Ketika sebuah paket keluar meninggalkan jaringan lokal, router mengganti Address sumber paket dengan Address publik, dan melakukan operasi sebaliknya untuk lalu lintas yang masuk. Terjemahan dua arah ini transparan bagi pengguna.


**Peringatan:** Meskipun metode ini mengisolasi jaringan internal, metode ini tidak mengatasi kekurangan alamat IP publik, karena Anda masih membutuhkan alamat publik sebanyak mesin yang akan diekspos. Oleh karena itu, penerjemahan statis terutama digunakan ketika sumber daya internal tertentu harus tetap dapat dijangkau dari luar (server web, server email...).


*di sisi lain, *Dynamic translation**, menggunakan kumpulan alamat IP publik. Ketika sebuah host internal memulai koneksi, router untuk sementara memberikan salah satu alamat publik ini ke Address pribadi host selama durasi sesi. Sambungan ini bersifat 1-ke-1, tetapi sementara: setelah sambungan berakhir, Address publik tersedia untuk perangkat lain. Oleh karena itu, NAT dinamis mengurangi jumlah alamat publik yang diperlukan ketika tidak semua mesin online pada saat yang sama, tetapi masih membutuhkan blok alamat eksternal setidaknya sebesar jumlah maksimum koneksi simultan.


**Port translation** (PAT), juga dikenal sebagai *NAT overload* atau *IP masquerading*, melangkah lebih jauh: semua perangkat pribadi berbagi satu IP publik Address (atau jumlah yang sangat kecil). Untuk membedakan sesi, gateway memodifikasi tidak hanya Address sumber, tetapi juga port sumber. Gateway menyimpan tabel yang menghubungkan setiap pasangan *(private Address, private port)* ke pasangan *(public Address, public port)* yang unik. Bentuk NAT ini digunakan di hampir semua router rumah, memungkinkan lusinan perangkat (komputer, ponsel pintar, benda-benda yang terhubung, dll.) untuk berbagi IP publik Address yang sama, sambil mempertahankan komunikasi yang lancar.


Oleh karena itu, NAT memperpanjang umur IPv4, sambil menambahkan Layer yang berharga dalam hal segmentasi dan keamanan. Namun, seiring dengan pertumbuhan adopsi IPv6 dan ruang Address yang luas menjadi lebih banyak digunakan, peran NAT kemungkinan akan menurun, meskipun untuk tujuan kompatibilitas dan kontrol, NAT masih akan digunakan di beberapa lingkungan untuk menyegmentasi dan menyaring lalu lintas.


### Implementasi NAT


Untuk memastikan pengoperasian terjemahan Address yang tepat, router atau gateway NAT harus menyimpan catatan akurat tentang pemetaan yang dibuat antara setiap Address pribadi di jaringan internal dan Address publik yang digunakannya untuk berkomunikasi dengan dunia luar. Informasi ini disimpan dalam apa yang dikenal sebagai "tabel terjemahan NAT", yang memainkan peran sentral dalam mengelola lalu lintas jaringan.


Setiap entri dalam tabel ini menghubungkan setidaknya satu pasangan: IP internal Address dari mesin pengirim dan IP eksternal Address yang akan diekspos di Internet. Ketika sebuah paket dari jaringan privat dikirim ke tujuan publik, router NAT mencegat frame, menganalisis header IP dan TCP/UDP, kemudian mengganti sumber privat Address dengan Address publik gateway. Pada jalur balik, gateway yang sama menangkap paket yang masuk, memeriksa tabel pemetaan dan melakukan operasi sebaliknya untuk mengarahkan aliran ke IP internal asli Address.


Prinsip penerjemahan dinamis ini bergantung pada manajemen tabel yang tepat: setiap entri tetap valid selama ada trafik yang aktif untuk membenarkannya. Setelah periode tidak aktif yang dapat dikonfigurasi, entri akan dihapus dan dapat digunakan kembali untuk koneksi baru.


contoh tabel terjemahan NAT yang disederhanakan:_


| Internal IP   | External IP    | Duration (sec) | Reusable? |
| ------------- | -------------- | -------------- | --------- |
| 10.101.10.20  | 193.48.100.174 | 1,200          | no        |
| 10.100.54.251 | 193.48.101.8   | 3,601          | yes       |
| 10.100.0.89   | 193.48.100.46  | 0              | no        |

Dalam contoh ini, jika tidak ada paket yang melewati entri kedua dalam waktu lebih dari satu jam (3.600 detik), maka akan ditandai sebagai dapat digunakan kembali. Sebaliknya, durasi nol menunjukkan komunikasi aktif, dengan pemetaan terkunci.


Meskipun NAT beroperasi secara transparan untuk sebagian besar penggunaan umum (penjelajahan web, email, transfer file, dll.), NAT dapat menciptakan tantangan tambahan untuk aplikasi jaringan tertentu. Beberapa teknologi mengandalkan pertukaran alamat IP atau port secara eksplisit di dalam muatan paket. Setelah melewati gateway NAT, informasi ini menjadi tidak konsisten.


Contoh umum dari keterbatasan meliputi:


- Protokol peer-to-peer (P2P), yang memerlukan koneksi langsung antar perangkat, terhalang oleh penghalang NAT, karena semua mesin internal berbagi IP eksternal Address yang sama dan tidak dapat dijangkau secara langsung tanpa konfigurasi khusus (seperti *port forwarding* atau UPnP);
- Protokol IPSec, yang digunakan untuk mengamankan komunikasi jaringan, mengenkripsi header paket. Karena NAT harus memodifikasi header ini untuk mengganti alamat IP, enkripsi membuat hal ini tidak mungkin dilakukan tanpa mekanisme adaptasi seperti NAT-T (*NAT Traversal*);
- Protokol X Window, yang memungkinkan tampilan jarak jauh dari aplikasi grafis pada Unix/Linux, bekerja dengan cara server X secara aktif mengirimkan koneksi TCP ke klien. Pembalikan arah koneksi yang biasa terjadi ini dapat diblokir oleh NAT.


Secara umum, protokol apa pun yang secara eksplisit menyertakan IP internal Address dalam muatan paket akan terpengaruh, karena Address tersebut tidak lagi cocok dengan Address yang nyata dan dapat dilihat di internet setelah diterjemahkan.


**Catatan penting:** Untuk Address masalah ini, beberapa router NAT menawarkan _Deep Packet Inspection_ (DPI) atau _Protocol Helpers_, yang memeriksa isi paket untuk mengidentifikasi dan secara dinamis mengganti alamat atau nomor port di dalam data aplikasi. Hal ini membutuhkan pengetahuan mendalam tentang format protokol, dan dapat menciptakan kerentanan keamanan atau meningkatkan penggunaan sumber daya.


**Perhatian:** Meskipun NAT membantu menyembunyikan jaringan internal dan mengontrol trafik yang masuk, NAT bukanlah pengganti firewall khusus. Penerjemahan saja bukanlah penghalang keamanan yang lengkap: harus selalu dilengkapi dengan aturan penyaringan yang jelas untuk memblokir trafik yang tidak diminta atau tidak diinginkan.


untuk mengilustrasikan bagaimana hal ini bekerja dalam praktiknya, pertimbangkan contoh berikut:_



![Image](assets/fr/037.webp)



Dalam skenario ini, workstation internal dapat mengakses server web internal hanya dengan memanggil URL `http://192.168.1.20:80`. Menentukan port adalah opsional di sini, karena `80` adalah port HTTP standar, sebaliknya, jika permintaan dimulai dari luar, pengguna akan memasukkan Address publik `http://85.152.44.14:80`. Router NAT menerima permintaan, berkonsultasi dengan tabel pemetaannya, dan secara otomatis menerjemahkan Address publik menjadi privat, mengarahkan koneksi ke `http://192.168.1.20:80`.


Prinsip yang sama berlaku untuk server lain yang diotorisasi untuk menerima koneksi internet, seperti server Extranet (sirkuit biru pada diagram).


**Catatan praktis:** Dalam lingkungan tervirtualisasi, antarmuka jaringan yang disebut _virbrX_ (untuk _Virtual Bridge X_) biasanya digunakan. Jembatan virtual ini, yang disediakan secara khusus oleh perpustakaan libvirt atau hypervisor Xen, menghubungkan jaringan internal virtual mesin tamu ke jaringan fisik sambil menerapkan NAT. Mereka umumnya dikonfigurasi melalui skrip di `/etc/sysconfig/network-scripts/`, seperti yang ditunjukkan di bawah ini untuk `virbr0`:


```ini
NAME=""
BOOTPROTO=none
MACADDR=""
TYPE=Bridge
DEVICE=virbr0
NETMASK=255.255.255.0
MTU=""
BROADCAST=192.168.0.255
IPADDR=192.168.0.1
NETWORK=192.168.0.0
ONBOOT=yes
```


Setelah jembatan virtual terpasang, Anda perlu mengaktifkan perutean IP dan mengonfigurasi penerjemahan port dengan `iptables`:


```shell
echo 1 > /proc/sys/net/ipv4/ip_forward
```


```shell
iptables -t nat -A POSTROUTING -o <WAN> -s 192.168.0.0/24 -j MASQUERADE
```


Dengan konfigurasi ini, lalu lintas keluar dialihkan dan terjemahan NAT diterapkan, sehingga mesin virtual dapat berkomunikasi dengan dunia luar tanpa secara langsung mengekspos alamat IP internalnya.


Pada bab berikutnya, kita akan melihat secara rinci konfigurasi IP Address di Linux, yang mencakup metode sederhana dan lanjutan yang cocok untuk konteks administrasi yang berbeda.



https://planb.network/tutorials/computer-security/communication/pi-hole-46a735c5-8af3-4cc3-a2c2-1d4f6a7dc428

https://planb.network/tutorials/computer-security/operating-system/opnsense-90c2785d-a0d7-4981-be8d-d290bbeb8263

https://planb.network/tutorials/computer-security/operating-system/pfsense-24eea96a-2fdc-42a6-a77b-89bc29149864


## Bagaimana cara mengkonfigurasi jaringan dengan `ip`?


<chapterId>8ba7e946-d2a0-4841-8d54-e85ba96baa25</chapterId>



### Konfigurasi standar


Setelah membahas dasar-dasar teoritis jaringan dan memahami bagaimana alamat IP, mask, routing, dan penerjemahan bekerja bersama-sama, sekarang saatnya untuk beralih ke konfigurasi praktis. Pada GNU/Linux, pengaturan jaringan sekarang ditangani dengan perintah **`ip`** (paket _iproute2_), yang menggantikan `ifconfig` yang lebih lama.


`ip` memungkinkan Anda menetapkan atau mengubah IP Address, mengubah mask, memulai atau menghentikan Interface, atau memeriksa statusnya kapan saja.


**TIP:** untuk menampilkan semua antarmuka (aktif atau tidak): `ip addr show`


Contoh: menetapkan Address statis dan mengaktifkan Interface


Tambahkan Address `192.168.1.2/24` ke Interface `eth0`:


```shell
ip addr add 192.168.1.2/24 dev eth0
```


Aktifkan Interface:


```shell
ip link set dev eth0 up
```


Nonaktifkan Interface yang sama:


```shell
ip link set dev eth0 down
```


Menampilkan status Interface tertentu:


```shell
ip addr show dev eth2
```


**Tip praktis:** Dengan `ip`, menambahkan Address tambahan ke Interface tidak lagi memerlukan akhiran `:1`. Cukup tambahkan baris `ip addr add ...` lainnya:


```shell
ip addr add 172.18.2.39/24 dev eth2
```


### Skrip aktivasi: ifup / ifdown


Utilitas `ifup` dan `ifdown` membaca berkas konfigurasi statis dari `/etc/sysconfig/network-scripts/` (pada RHEL, CentOS, Rocky Linux, AlmaLinux...) atau `/etc/network/interfaces/` (pada Debian/Ubuntu) untuk menaik-turunkan antarmuka secara bersih.


```shell
ifup eth1
ifdown eth2
```


File konfigurasi (seperti RHEL):


- /etc/sysconfig/network**: pengaturan global (JARINGAN, NAMA HOST, GERBANG...).
- ifcfg-**: pengaturan khusus untuk setiap Interface.


Contoh statis (ifcfg-eth0):


```ini
DEVICE=eth0
BOOTPROTO=none
ONBOOT=yes
IPADDR=192.168.2.5
NETMASK=255.255.255.0
GATEWAY=192.168.2.1
```


Contoh DHCP:


```ini
DEVICE=eth0
BOOTPROTO=dhcp
ONBOOT=yes
```


Struktur modular ini masih berlaku dan dapat dengan mudah diotomatisasi pada sistem saat ini.


### Konfigurasi lanjutan: ikatan


Dalam lingkungan profesional, tujuannya adalah untuk menjamin kontinuitas layanan dan/atau untuk menggabungkan bandwidth. *Mekanisme bonding* (atau *teaming* dengan _teamd_) memenuhi kebutuhan ini: beberapa antarmuka fisik berfungsi sebagai Interface logis tunggal, sering disebut `bond0` atau `team0`.



![Image](assets/fr/039.webp)



Prasyarat:


- Muatkan modul `bonding` (atau gunakan `teamd`) ;
- Memiliki setidaknya dua antarmuka fisik yang tersedia.


#### Berbagai metode ikatan yang umum:


|Mode|Name|Principle|
|---|---|---|
|0|balance-rr|Round-robin, cyclic distribution of frames|
|1|active-backup|Single active interface with hot failover |
|2|balance-xor|Selection based on XOR of src/dst MAC addresses|
|3|broadcast|Broadcast simultaneously on all interfaces   |
|4|802.3ad (LACP)|Standardized dynamic aggregation; requires compatible switch|
|5|tlb (Transmit Load Balancing)|Balancing based on transmit load|
|6|alb (Adaptive Load Balancing)|Adaptive balancing; also balances receive via ARP|

#### Menyiapkan dengan `tautan ip



- Menonaktifkan antarmuka fisik:


```shell
ip link set eth0 down
ip link set eth1 down
```



- Menciptakan Interface yang terikat:


```shell
ip link add bond0 type bond mode balance-alb
```



- Mengonfigurasi opsi setelah pembuatan


```shell
ip link set bond0 type bond miimon 100
```



- Menetapkan alamat MAC dan IP:


```shell
ip link set dev bond0 address 00:17:56:BC:02:3A
ip addr add 192.168.2.3/24 dev bond0
ip route add default via 192.168.2.1
```



- Memasang antarmuka slave:


```shell
ip link set eth0 master bond0
ip link set eth1 master bond0
```



- Bawa semuanya kembali:


```shell
ip link set bond0 up
ip link set eth0 up
ip link set eth1 up
```


**Tip:** untuk melepaskan budak tanpa melepas ikatan: `ip link set eth1 nomaster`


#### Konfigurasi permanen (seperti RHEL)


Buat tiga file di `/etc/sysconfig/network-scripts`:


_ifcfg-bond0_


```ini
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=none
IPADDR=192.168.2.3
NETMASK=255.255.255.0
BROADCAST=192.168.2.255
GATEWAY=192.168.2.1
BONDING_OPTS="mode=balance-alb miimon=100"
```


_ifcfg-eth0_


```ini
DEVICE=eth0
ONBOOT=yes
MASTER=bond0
SLAVE=yes
```


_ifcfg-eth1_


```ini
DEVICE=eth1
ONBOOT=yes
MASTER=bond0
SLAVE=yes
```


Kalau begitu:


```shell
systemctl restart network
```


#### IP tambahan Address (alias modern)


Dengan `ip`, Anda dapat dengan mudah menambahkan Address kedua ke perangkat yang sama:


```shell
ip addr add 192.168.1.2/24 dev eth0
```


Untuk membuat alias ini tetap ada setelah reboot, tambahkan blok `IPADDR2=...` / `PREFIX2=...` yang kedua pada `ifcfg-eth0`, atau buat sambungan *NetworkManager* yang baru melalui `nmcli`.


Berkat `ip` dan perintah terkait (`ip link`, `ip addr`, `ip route`), konfigurasi jaringan menjadi lebih konsisten, dapat dituliskan, dan jelas. Ikatan adalah komponen kunci dari arsitektur ketersediaan tinggi, dan menetapkan beberapa alamat ke satu Interface menjadi jauh lebih sederhana.


Di bab berikutnya, kita akan melihat secara spesifik dan implementasi pengalamatan IPv6.


# Pengalamatan IPv6


<partId>9b1d87f1-2a68-496e-b5dd-76cf74fb8cde</partId>


## IPv6: Standar dan definisi


<chapterId>d1f16f0a-1104-460d-8d67-f725665f8e3f</chapterId>



Sekarang kita beralih ke generasi pengalamatan IP berikutnya: protokol IPv6, yang awalnya dikenal sebagai IPng (_IP Next Generation_). Dirancang untuk mengatasi keterbatasan struktural IPv4, protokol ini memperkenalkan arsitektur pengalamatan yang diperluas, serta berbagai pengoptimalan teknis.


Motivasi di balik adopsi IPv6 sangat beragam, dan Address merupakan kebutuhan penting untuk evolusi Internet. Pertama, peran IPv6 adalah untuk mendukung pertumbuhan eksponensial dalam jumlah perangkat yang terhubung (sebuah tujuan yang tidak dapat dicapai dengan ruang Address yang terbatas pada IPv4). Kedua, protokol ini bertujuan untuk mengurangi ukuran tabel routing, membuat pertukaran menjadi lebih efisien dan mengurangi beban kerja router dalam jangka panjang.


IPv6 juga berusaha untuk menyederhanakan aspek-aspek tertentu dalam penanganan paket, meningkatkan aliran datagram dan mengoptimalkan kecepatan transfer antar jaringan. Dari sudut pandang keamanan, header AH/ESP dari protokol *IPsec* disertakan dalam spesifikasi dasar, dan semua node IPv6 harus dapat mendukungnya (RFC 6434). Namun, penggunaannya tetap opsional: terserah administrator untuk mengaktifkannya tergantung pada konteksnya.


Tujuan lainnya termasuk penanganan yang lebih tepat untuk jenis layanan, terutama untuk memastikan kualitas yang lebih baik untuk aplikasi real-time (VoIP, konferensi video, dll). IPv6 juga dirancang untuk memungkinkan manajemen mobilitas yang lebih fleksibel: sebuah perangkat dapat mengubah titik akses tanpa mengubah Address-nya dengan cara yang dapat dilihat oleh rekan-rekannya.


Terakhir, IPv6 dirancang untuk hidup berdampingan dengan protokol lama. Meskipun tidak secara langsung kompatibel dengan IPv4, IPv6 tetap dapat dioperasikan sepenuhnya dengan protokol yang lebih tinggi seperti TCP, UDP, ICMPv6, dan DNS, serta protokol perutean seperti OSPF dan BGP, tergantung pada penyesuaian tertentu. Untuk manajemen multicast, IPv6 menggunakan protokol MLD (*Multicast Listener Discovery*), yang secara fungsional setara dengan IGMP di lingkungan IPv4.


### Aturan notasi


Salah satu perubahan yang paling signifikan dalam IPv6 adalah format IP Address itu sendiri. Untuk mengatasi kekurangan alamat IPv4 yang kronis, panjang Address telah ditingkatkan dari 32 bit menjadi 128 bit, jadi 16 byte. Secara teori, ini menghasilkan ruang Address yang mungkin sebesar:


$$3.4 \kali 10^{38}$$


Hal ini memastikan kapasitas yang hampir tidak terbatas untuk semua peralatan saat ini dan masa depan.


Alamat IPv6 ditulis dengan cara yang sangat berbeda dengan notasi desimal bertitik yang biasa digunakan. IPv6 Address terdiri dari delapan kelompok 16-bit, ditulis dalam heksadesimal dan dipisahkan dengan titik dua `:`.


Sebagai contoh:


```
1987:0c02:0000:84c2:0000:0000:cf2a:9077
```


Untuk menyederhanakan notasi, angka nol di depan pada setiap kelompok dapat dihilangkan. Contoh di atas kemudian menjadi:


```
1987:c02:0:84c2:0:0:cf2a:9077
```


Selain itu, satu urutan kontinu grup nol dapat diganti dengan ::, yang semakin memperpendek Address:


```
1987:c02:0:84c2::cf2a:9077
```


**Peringatan:** Aturan ini sangat ketat: hanya satu urutan angka nol yang berurutan yang dapat diganti dengan `::`. Jika Address berisi beberapa urutan angka nol, hanya angka nol terpanjang yang dipadatkan. Hal ini memastikan keunikan dan keterbacaan.


**Detail penting:** Karakter `:` yang digunakan untuk memisahkan blok heksadesimal dapat menyebabkan ambiguitas pada URL, karena `:` juga digunakan untuk mengindikasikan port layanan. Untuk menghindari kebingungan, alamat IPv6 dalam URL harus diapit oleh tanda kurung siku `[ ]`.


Contoh akses HTTP ke port tertentu untuk Address `2002:400:2A41:378::34A2:36`:


```
http://[2002:400:2A41:378::34A2:36]:8080
```


Ketika merepresentasikan IPv4 Address dalam konteks IPv6, Anda dapat menggunakan notasi campuran dalam bentuk desimal bertitik, diawali dengan `::`:


```
::192.168.1.5
```


Kompatibilitas ini membantu memudahkan transisi antara kedua protokol dengan memungkinkan blok IPv4 dimasukkan ke dalam ruang IPv6 Address.


**Catatan:** Untuk menstandarkan cara penulisan alamat, RFC 5952 mendefinisikan format kanonik dengan aturan singkatan untuk menghindari beberapa representasi dari Address yang sama. Mengikuti rekomendasi ini membantu mengurangi salah tafsir dan memastikan konfigurasi jaringan yang konsisten.


### Tipe IPv6 Address


IPv6 berbeda dari pendahulunya melalui berbagai macam kategori Address, masing-masing dirancang untuk penggunaan tertentu, sekaligus memungkinkan perutean yang fleksibel dan manajemen jaringan. Seperti halnya IPv4, alamat dapat bersifat global, lokal, dicadangkan, atau khusus untuk mekanisme transisi tertentu.


IPv6 Address yang tidak ditentukan diwakili oleh `::` atau, secara lebih eksplisit, `::0.0.0.0`. Bentuk khusus ini digunakan selama akuisisi Address, atau sebagai nilai default untuk menunjukkan ketiadaan Address.



| IPv6 Address Prefix | Description                                 |
| ------------------- | ------------------------------------------- |
|::/8                | Reserved addresses                          |
| 2000::/3            | Unicast addresses, routable on the Internet |
| fc00::/7            | Unique local addresses (1)                  |
| fe80::/10           | Link-local addresses                        |
| ff00::/8            | Multicast addresses                         |

(1): *Pada LAN pribadi, awalan `fd00::/8` lebih disukai untuk menetapkan alamat internal yang tidak dapat dirutekan di Internet*


#### Alamat yang dicadangkan


Rentang IPv6 tertentu secara eksplisit dicadangkan dan tidak boleh digunakan sebagai alamat global. Alamat-alamat tersebut memiliki tujuan teknis tertentu:


- `::/128`**: Address yang tidak ditentukan, tidak pernah ditetapkan secara permanen ke perangkat, tetapi digunakan sebagai sumber Address oleh mesin yang menunggu konfigurasi.
- `::1/128`**: _loopback_ Address, setara dengan `127.0.0.1` di IPv4, yang memungkinkan mesin untuk melakukan Address itu sendiri.
- `64:ff9b::/96`**: Dicadangkan untuk penerjemah protokol untuk mengaktifkan interkoneksi IPv4/IPv6, seperti yang didefinisikan dalam RFC 6052.
- `::ffff:0:0/96`**: blok kompatibilitas untuk merepresentasikan IPv4 Address dalam struktur IPv6 tertentu, yang sering digunakan secara internal oleh aplikasi.


Blok-blok ini menjamin interoperabilitas dan memfasilitasi migrasi antara dua versi protokol.


#### Alamat unicast global


Alamat unicast global merupakan sebagian besar ruang IPv6 yang dapat dirutekan secara publik, yang mewakili sekitar 1/8 ruang Address. Sejak tahun 1999, IANA telah mengalokasikan blok-blok ini, seperti awalan `2001::/16`, dalam blok CIDR (dari `/23` hingga `/12`) ke registri regional, yang kemudian mendistribusikannya ke penyedia dan organisasi.


Beberapa rentang memiliki penggunaan khusus yang terdokumentasi:


- `2001:2::/48`**: Dicadangkan untuk pengujian performa dan interoperabilitas (RFC 5180).
- `2001:db8::/32`**: Dicadangkan untuk dokumentasi dan contoh (RFC 3849).
- `2002::/16`**: Digunakan untuk mekanisme 6to4, yang memungkinkan lalu lintas IPv6 melintasi infrastruktur IPv4 (berguna selama fase transisi antara dua protokol).


**Catatan:** sebagian besar alamat global tetap tidak digunakan, berfungsi sebagai cadangan untuk pertumbuhan Internet di masa depan.


#### Alamat lokal unik (ULA)


Alamat lokal yang unik (`fc00::/7`) adalah alamat IPv6 yang setara dengan alamat privat IPv4 (RFC1918). Alamat ini memungkinkan pembuatan jaringan internal yang terisolasi tanpa risiko konflik dengan pengalamatan publik. Dalam praktiknya, awalan yang efektif adalah `fd00::/8`, dengan bit ke-8 diset ke 1 untuk menunjukkan penggunaan lokal. Setiap blok ULA memiliki pengenal acak semu 40-bit, sehingga meminimalkan tabrakan Address ketika menghubungkan jaringan privat yang terpisah.


#### Tautkan alamat lokal


Alamat link-lokal (`fe80::/64`) digunakan secara eksklusif untuk komunikasi dalam segmen Layer 2 yang sama (VLAN atau sakelar yang sama). Alamat-alamat ini tidak pernah dirutekan di luar sambungan lokal. Setiap jaringan Interface secara otomatis menghasilkan link-lokal Address, yang sering kali berasal dari MAC Address menggunakan skema EUI-64.


**Fitur khusus**: mesin yang sama dapat menggunakan link-lokal Address yang sama pada beberapa antarmuka, tetapi Interface harus ditentukan saat berkomunikasi untuk menghindari ambiguitas.


#### Alamat multicast


Pada IPv6, broadcast telah digantikan oleh multicast, sebuah cara yang lebih efisien untuk mengirimkan paket ke sekelompok penerima yang ditentukan. Rentang multicast diawali dengan `ff00::/8`. Ini termasuk alamat seperti `ff02::1`, yang menargetkan semua node pada sambungan lokal. Meskipun nyaman, Address ini tidak lagi direkomendasikan untuk aplikasi, karena dapat melakukan siaran yang tidak terkendali.


Penggunaan multicast yang umum adalah _Neighbor Discovery Protocol_ (NDP), yang menggantikan ARP di IPv6. NDP menggunakan alamat multicast tertentu, seperti `ff02::1:ff00:0/104`, untuk secara otomatis menemukan host lain yang tersambung ke sambungan yang sama.


Dengan menggabungkan tipe Address ini, IPv6 menyediakan satu set opsi lengkap untuk memenuhi kebutuhan perutean global, komunikasi lokal, migrasi IPv4/IPv6, dan konfigurasi perangkat otomatis, sekaligus meningkatkan efisiensi transmisi.


### Lingkup Address


Cakupan IPv6 Address mendefinisikan domain yang tepat di mana IPv6 itu valid dan unik. Memahami konsep ini adalah kunci untuk menguasai perutean paket dan organisasi logis jaringan IPv6. Alamat IPv6 umumnya dikelompokkan ke dalam tiga kategori utama berdasarkan cakupan dan penggunaannya: unicast, anycast, dan multicast.


*alamat *Unicast** adalah yang paling umum dan mencakup beberapa subtipe yang berbeda.

Ini termasuk _loopback_ (`::1`) Address, yang cakupannya terbatas pada host yang menggunakannya, dan yang digunakan untuk menguji tumpukan jaringan secara internal tanpa mengirim lalu lintas melalui jaringan fisik.

Lalu ada alamat link-lokal (_link-local_), yang cakupannya terbatas pada satu segmen jaringan: alamat ini digunakan untuk komunikasi langsung antara perangkat pada sambungan fisik atau logis yang sama (mis. sakelar tunggal atau VLAN).

Terakhir, alamat lokal yang unik (_ULA_, untuk _Unique Local Addresses_) bersifat internal untuk jaringan privat. Alamat-alamat ini dapat dirutekan di antara beberapa segmen privat tetapi tidak pernah terlihat di Internet.


Secara konseptual, alamat IPv6 sering direpresentasikan sebagai struktur biner di mana bagian pertama (64 bit pertama) mengidentifikasi awalan jaringan, dan bagian kedua (juga 64 bit) secara unik mengidentifikasi Interface perangkat di jaringan tersebut. Pembagian ini membuat konfigurasi otomatis Address lebih mudah melalui mekanisme seperti SLAAC (_Stateless Address Autoconfiguration_), yang memungkinkan mesin secara otomatis membuat Address yang stabil berdasarkan MAC Address atau pengenal acak semu.


| Field     | Prefix | L | Global ID | Subnet | Interface ID |
|-----------|--------|---|-----------|--------|---------------|
| Bits      | 7      | 1 | 40        | 16     | 64            |

Arsitektur IPv6 mengikuti model perutean global hirarkis dari Internet saat ini. Partisi awalan memungkinkan pendaftar regional dan operator jaringan untuk mengelola alokasi Address dengan cara yang terdesentralisasi, sekaligus memastikan keunikan global. Dalam kerangka kerja ini, host yang sama dapat secara bersamaan memegang Address unicast global untuk komunikasi internet dan Address link-lokal untuk interaksi lokal, misalnya dengan lingkungan terdekat atau untuk pesan penemuan router.


| Field     | Prefix | Zero | Interface ID |
|-----------|--------|------|--------------|
| Bits      | 10     | 54   | 64           |

**Alamat anycast mewakili konsep perantara yang dibangun di atas model unicast tetapi dapat berperilaku seperti multicast dalam kasus-kasus tertentu. Address anycast pada dasarnya adalah Address unicast yang ditugaskan ke beberapa antarmuka yang didistribusikan melalui node jaringan yang berbeda. Ketika sebuah paket dikirim ke anycast Address, protokol IPv6 bertujuan untuk mengirimkannya ke salah satu host yang berbagi Address tersebut, biasanya yang paling dekat dalam hal topologi perutean. Pendekatan ini mengoptimalkan kecepatan pemrosesan permintaan dan meningkatkan ketahanan layanan terdistribusi. Contoh klasiknya adalah server DNS root, di mana pengalamatan anycast secara otomatis mengarahkan kueri ke titik terdekat.



| Field     | Prefix | Subnet | Interface ID |
|-----------|--------|--------|--------------|
| Bits      | 48     | 16     | 64           |

Pada IPv6, **alamat multicast** menggantikan mekanisme broadcast, yang dianggap terlalu mahal dan tidak cocok untuk jaringan berskala global. Multicast Address mengidentifikasi sekelompok antarmuka, biasanya di beberapa host, yang ingin menerima paket yang sama secara bersamaan.

Setiap multicast Address menyertakan bidang _scope_ 4-bit khusus, yang mendefinisikan batas geografis atau batas logis siaran:


- Lingkup `1` berarti paket hanya untuk perangkat lokal.
- Cakupan `2` membatasi paket pada sambungan lokal: semua perangkat pada segmen fisik atau virtual yang sama dapat menerimanya.
- Cakupan `5` memperluas jangkauan ke suatu lokasi, biasanya seluruh jaringan perusahaan.
- Cakupan `8` memperluas jangkauan ke sebuah organisasi, memungkinkan pengiriman ke semua subnet dari entitas yang sama.
- Lingkup `e` (14 dalam heksadesimal) menunjukkan jangkauan global, membuat grup multicast dapat diakses dari mana saja di Internet jika infrastruktur perutean mendukung.


Struktur multicast IPv6 Address meliputi:


- bidang _Flag_ (4 bit) menentukan apakah grup bersifat permanen atau sementara,
- bidang _Scope_ (4 bit) mendefinisikan ruang lingkup,
- bidang identifikasi (112 bit) yang mengidentifikasi nomor grup multicast.


| Field      | Prefix | Flags | Scope | Group ID |
|------------|--------|--------|--------|----------|
| Bits       | 8      | 4      | 4      | 112      |

Contoh terkenal dari multicast IPv6 yang sedang bekerja adalah _Neighbor Discovery Protocol_ (NDP). Daripada menggunakan ARP seperti pada IPv4, NDP bergantung pada alamat multicast seperti `ff02::1:ff00:0/104` untuk menyiarkan permintaan penemuan tetangga, yang hanya menargetkan host yang relevan pada sambungan yang sama.


Dengan mendefinisikan cakupan Address secara tepat, IPv6 mengatur bagaimana aliran data dikirim, diterima, dan dirutekan. Perincian ini membuat protokol ini lebih fleksibel dan efisien untuk mengelola komunikasi lokal dan global, sekaligus menghindari kerugian dari penyiaran umum.


## Address Assignment dalam jaringan lokal


<chapterId>4c9c3e52-59bc-499a-af0a-6dd369a9e029</chapterId>


Pada bab ini, kita akan melihat salah satu aspek yang paling praktis dari penerapan IPv6: memberikan alamat IP ke host pada jaringan lokal. Arsitektur IPv6 telah dirancang untuk fleksibilitas, memungkinkan setiap perangkat untuk generate Address sendiri secara otomatis, sementara masih memungkinkan konfigurasi manual sepenuhnya bila diperlukan.


Jaringan lokal IPv6 secara sistematis membagi Address menjadi dua bagian:


- 64 bit pertama mewakili awalan subnet, biasanya disediakan oleh router atau otoritas Address;
- 64 bit sisanya digunakan oleh host untuk mengidentifikasi dirinya secara unik pada segmen tersebut.

Model ini sangat menyederhanakan agregasi rute dan manajemen blok Address.


Dua pendekatan utama digunakan untuk menetapkan alamat ke perangkat:


- Konfigurasi manual, di mana administrator menentukan setiap Interface secara tepat Address;
- Konfigurasi otomatis, di mana perangkat generate atau mendapatkan alamatnya sendiri secara dinamis.


Dalam konfigurasi manual, administrator menetapkan IPv6 Address secara lengkap ke setiap Interface. Nilai-nilai tertentu tetap dicadangkan:


- `::/128`: Address yang tidak ditentukan, tidak pernah ditetapkan secara permanen;
- `::1/128`: loopback Address (_loopback_), setara dengan IPv4: `127.0.0.1`.


Tidak seperti IPv4, tidak ada konsep _broadcast_; kombinasi "semua nol" atau "semua satu" di bagian host tidak memiliki arti khusus.

Konfigurasi manual masih berguna dalam lingkungan yang terkendali, tetapi menjadi sulit untuk dipertahankan dalam skala besar.


Untuk konfigurasi otomatis, ada beberapa metode yang tersedia:


- Protokol **NDP** (_Neighbor Discovery Protocol_), yang ditentukan oleh RFC4862, memungkinkan konfigurasi otomatis tanpa status. Dalam mode ini, host menerima awalan jaringan dari router lokal, dan melengkapi Address itu sendiri dengan pengenal berdasarkan MAC Address. Metode ini mudah digunakan, dan tidak memerlukan server pusat.
- Implementasi seperti yang ada di Windows dapat generate bagian host secara semu untuk meningkatkan privasi dengan menghindari pemaparan langsung MAC Address. Mengungkapkan MAC Address dalam paket IPv6 dapat menimbulkan masalah privasi, karena memungkinkan pelacakan perangkat di jaringan yang berbeda.
- Protokol DHCPv6: Didefinisikan dalam RFC3315 dan mirip dengan DHCP yang digunakan untuk IPv4, protokol ini memungkinkan konfigurasi yang lebih terkontrol dan terpusat, termasuk manajemen penyewaan, opsi tambahan (DNS, MTU...), dan registrasi basis data. DHCPv6 dapat beroperasi sendiri atau bersama konfigurasi tanpa nama untuk menyediakan parameter tambahan tanpa menetapkan IP Address itu sendiri.


**Catatan penting:** Dalam metode berbasis MAC, MAC Address dikonversi ke pengenal 64-bit menggunakan format EUI-64. Mekanisme ini menyisipkan byte `FF:FE` di tengah-tengah MAC Address asli (dalam 48 bit), dan membalikkan bit ke-7 untuk mengindikasikan keunikan global. Hasilnya adalah pengenal Interface yang stabil, yang digunakan pada IPv6 Address secara penuh.


Berikut ini contoh cara mengubah MAC Address menjadi EUI-64:


![Image](assets/fr/045.webp)



Namun, karena meningkatnya kekhawatiran akan pelacakan perangkat, sistem operasi modern (terutama Linux, Windows 10+, macOS, Android) sekarang mengaktifkan ekstensi privasi secara default. Ekstensi ini menggunakan pengenal Interface yang dibuat secara acak yang diperbarui secara berkala untuk koneksi keluar, sambil mempertahankan pengenal yang stabil untuk komunikasi internal (seperti DNS atau DHCPv6).


Seperti halnya DHCP pada IPv4, alamat IPv6 yang ditetapkan secara otomatis dapat memiliki dua masa pakai, yang ditentukan oleh router atau server DHCPv6:


- Masa pakai yang diinginkan*: setelah periode ini, Address tetap berlaku, tetapi tidak lagi digunakan untuk memulai sambungan baru;
- Masa pakai yang valid*: ketika waktu ini berakhir, Address akan sepenuhnya dihapus dari konfigurasi Interface.


Sistem ini memungkinkan untuk mengelola perubahan jaringan secara dinamis, misalnya, memastikan transisi yang mulus dari satu ISP ke ISP lainnya. Dengan memperbarui awalan yang diumumkan oleh router dan menyesuaikan catatan DNS secara paralel, migrasi IPv6 dapat dilakukan tanpa gangguan layanan yang nyata.


**Tip:** Penggunaan gabungan Address dan siklus hidup DNS memungkinkan untuk mengimplementasikan strategi transisi bertahap, di mana koneksi baru berpindah ke topologi baru, sementara koneksi yang sudah ada terus berlanjut hingga akhir alami.


Singkatnya, IPv6 menawarkan berbagai fleksibilitas untuk Address Assignment: konfigurasi manual, konfigurasi otomatis tanpa negara atau stateful, DHCPv6, atau pembuatan secara acak. Setiap pendekatan memiliki kelebihan dan keterbatasannya masing-masing, dan dapat diadaptasi sesuai dengan tingkat kontrol yang diperlukan, ukuran jaringan, atau kebutuhan privasi.


## Menetapkan blok IPv6 Address


<chapterId>45cce866-1b58-4888-b3fe-15c922180839</chapterId>


### Distribusi Address


Skema alokasi IPv6 Address telah disusun untuk memenuhi dua tujuan: menjamin keunikan Address global, dan untuk memungkinkan hierarki logis yang mendukung agregasi dan penyederhanaan tabel perutean.

Seperti halnya IPv4, *Internet Assigned Numbers Authority* (IANA) berada di puncak hirarki ini. IANA mengelola ruang unicast Address global dan mendelegasikan blok Address ke lima registri Internet regional (_RIR_).


Kelima RIR yang ada saat ini adalah:


- ARIN (Amerika Utara),
- RIPE NCC (Eropa, Timur Tengah, Asia Tengah),
- APNIC (Asia-Pasifik),
- AFRINIC (Afrika),
- LACNIC (Amerika Latin dan Karibia).


IANA mengalokasikan blok IPv6 dengan ukuran yang berbeda-beda untuk setiap RIR, umumnya antara /23 dan /12. Pendekatan ini menawarkan fleksibilitas sekaligus memastikan skalabilitas jangka panjang. RIR kemudian mendistribusikan kembali blok-blok ini kepada Penyedia Layanan Internet (ISP), perusahaan besar, dan institusi publik.


Sejak tahun 2006, setiap RIR telah menerima satu blok IPv6 /12 dari IANA, sebuah ukuran tetap yang dirancang untuk memastikan cadangan yang stabil dan cukup besar untuk pertumbuhan di masa depan. RIR biasanya membagi ini menjadi blok /23, /26 atau /29. ISP paling sering menerima /32 blok, meskipun ukuran ini dapat bervariasi tergantung pada ukuran dan wilayah geografis ISP. Mereka biasanya mengalokasikan /48 blok untuk pelanggan. Setiap /48 menyediakan 65.536 subnet /64 yang berbeda (kapasitas yang sangat besar dibandingkan dengan IPv4).


**Catatan penting:** Sebuah blok /32 berisi tepat 65.536 sub-blok /48. Ini berarti bahwa setiap ISP dapat melayani puluhan ribu pelanggan tanpa menghabiskan alokasi mereka. Berkat /48, setiap pelanggan akan memiliki ruang yang sangat besar untuk menyusun jaringan internalnya sendiri dengan sebanyak mungkin segmen /64 yang diinginkan.


Hirarki alokasi umumnya terlihat seperti ini:


| IANA | RIR | LIR | Customer | Subnet | Interface |
|------|-----|-----|----------|--------|-----------|
|  3   | 20  |  9  |    16    |   16   |     64    |

Dengan banyaknya alamat ini, NAT (*Network Address Translation*), yang dulunya sangat penting dalam IPv4 untuk mengatasi kekurangan Address, tidak lagi diperlukan. Setiap host dapat memiliki Address publik yang unik dan dapat dirutekan secara global, sehingga menyederhanakan konektivitas ujung ke ujung dan membuat protokol seperti IPSec, VoIP, atau sambungan masuk menjadi lebih mudah digunakan.


Untuk memeriksa organisasi mana yang memiliki IPv6 Address, Anda bisa menggunakan perintah `whois` untuk menanyakan basis data RIR publik. Transparansi ini memungkinkan untuk mengidentifikasi organisasi yang memiliki awalan, yang dapat berguna untuk tujuan jaringan, analisis atau keamanan.


### Pengalamatan PA vs PI


Awalnya, model alokasi IPv6 hanya didasarkan pada blok PA (*Provider Aggregatable*), yang berarti terhubung ke ISP. Dalam model ini, sebuah organisasi menerima awalan dari ISP-nya, yang berarti bahwa mengganti penyedia memerlukan penomoran ulang seluruh infrastruktur.


Meskipun fitur konfigurasi otomatis IPv6 dan masa pakai Address membuat penomoran ulang menjadi lebih mudah, namun tetap saja tidak nyaman bagi organisasi dengan infrastruktur penting atau koneksi beberapa penyedia untuk kebutuhan redundansi.


Sejak tahun 2009, kebijakan alokasi telah mengizinkan blok PI (*Provider Independent*). Blok ini (umumnya berukuran /48) dialokasikan langsung ke perusahaan atau institusi oleh RIR, secara independen dari ISP mana pun. Model ini sangat cocok untuk organisasi yang melakukan *multihoming*, (artinya terhubung ke beberapa operator secara bersamaan). Sebagai contoh, di Eropa, RIPE-512 menguraikan kebijakan untuk alokasi PI.


### Notasi subnet mask


Seperti pada IPv4, IPv6 menggunakan CIDR (*Classless Inter-Domain Routing*). Ini terdiri dari indikasi jumlah bit yang membentuk awalan setelah Address, menggunakan karakter `/`.


Perhatikan contoh berikut ini:


```
2001:db8:1:1a0::/59
```


Ini berarti bahwa 59 bit pertama ditetapkan dan mengidentifikasi jaringan. Semua bit yang tersisa (di sini 69 bit) dapat digunakan untuk mengidentifikasi subnet atau host.


Dengan demikian, notasi ini mencakup alamat dari `2001:db8:1:1a0:0:0:0:0` hingga `2001:db8:1:1bf:ffff:ffff:ffff:ffff`.


Oleh karena itu, blok ini mencakup satu set 8 /64 subnet, masing-masing mampu meng-host sejumlah besar perangkat.


Notasi CIDR memungkinkan perencanaan ruang Address yang tepat, dari jaringan skala besar hingga pengaturan di rumah dan lingkungan tervirtualisasi, dan mendorong agregasi rute, mengurangi beban router dan meningkatkan skalabilitas.


### Paket dan header IPv6


Format paket IPv6 berbeda dengan IPv4 karena lebih sederhana dan lebih dapat diperluas. Datagram IPv6 selalu dimulai dengan header ukuran tetap sebesar 40 byte yang berisi semua informasi perutean yang penting. Pendekatan yang ramping ini, dibandingkan dengan panjang variabel header IPv4 (dari 20 hingga 60 byte), memungkinkan pemrosesan paket yang lebih cepat dan lebih efisien oleh router.


Namun, IPv6 tidak menghilangkan fungsionalitas: alih-alih mengintegrasikan banyak bidang opsional di header utama, IPv6 memperkenalkan sistem header ekstensi, yang ditempatkan segera setelah header dasar. Header opsional ini memungkinkan untuk menambahkan data atau instruksi khusus untuk fungsi tertentu, tanpa membebani paket biasa.


Beberapa tajuk ekstensi mengikuti struktur tetap, sementara yang lain dapat menampung sejumlah opsi yang bervariasi. Opsi-opsi ini dikodekan sebagai kembar tiga `{Type, Length, Value}`:


- Kolom "Jenis" (1 byte) menunjukkan sifat opsi;
- Dua bit pertama dari "Type" menentukan apa yang harus dilakukan router jika opsi tidak dikenali:
 - Abaikan pilihan tersebut dan lanjutkan perawatan,
 - Jatuhkan datagram,
 - Jatuhkan dan kirimkan kesalahan ICMP ke sumbernya.
 - Jatuhkan datagram tanpa pemberitahuan (dalam kasus paket multicast).
- Bidang "Panjang" (1 byte) menentukan ukuran bidang "Nilai", dari 0 hingga 255 byte;
- Bidang "Nilai" berisi data yang terkait dengan opsi.


Berikut ini adalah ikhtisar berbagai jenis header ekstensi yang didefinisikan oleh IPv6.


#### Tajuk Hop-by-Hop


Header ini, jika ada, selalu ditempatkan segera setelah header dasar. Header ini berisi informasi yang harus diproses oleh setiap router di sepanjang jalur paket, tidak seperti kebanyakan header lainnya, yang biasanya hanya ditangani oleh node tujuan. Penggunaan yang umum termasuk menandakan parameter global atau meminta langkah pemrosesan tertentu saat paket berjalan melalui jaringan.


![Image](assets/fr/047.webp)


#### Header perutean


Header perutean menentukan daftar alamat perantara yang harus dilewati oleh paket. Ada dua mode perutean utama:


- Perutean yang ketat: jalur yang tepat telah ditentukan sebelumnya
- Perutean longgar: hanya langkah wajib tertentu yang ditentukan.


Empat bidang pertama dari header rooting ini adalah:


- Header Berikutnya**: mengidentifikasi jenis header berikutnya;
- Jenis Routing**: menentukan metode routing (biasanya `0`);
- Segmen kiri**: jumlah segmen yang tersisa untuk dilintasi;
- Address [n]**: daftar alamat perantara.


Kolom "Segmen Tersisa" dimulai dengan jumlah total segmen yang tersisa dan dikurangi satu pada setiap hop.


![Image](assets/fr/048.webp)


#### Tajuk fragmentasi


Dalam IPv6, hanya host sumber yang diizinkan untuk memecah datagram, tidak seperti IPv4 di mana router juga dapat melakukannya. Semua node IPv6 harus dapat menangani paket minimal 1280 byte. Jika router menemukan paket yang lebih besar dari MTU link berikutnya, router akan mengirimkan pesan *ICMPv6 Packet Too Big* kembali ke sumber, yang kemudian menyesuaikan ukuran transmisinya.


Header fragmentasi berisi bidang-bidang berikut ini:


- Identifikasi**: pengidentifikasi datagram unik untuk pemasangan kembali.
- Fragment Offset**: posisi fragmen di dalam datagram asli.
- Bendera M**: mengindikasikan apakah ada fragmen lain yang mengikuti.


![Image](assets/fr/049.webp)


#### Header otentikasi (AH)


Header ini dirancang untuk mengamankan komunikasi dengan memverifikasi keaslian pengirim dan integritas data. Header ini biasanya digunakan dengan protokol IPsec. Dengan menggunakan kode autentikasi, penerima dapat mengonfirmasi bahwa pesan tersebut benar-benar berasal dari pengirim yang diharapkan dan belum diubah dalam perjalanan.


Jika terjadi upaya modifikasi yang curang, kode otentikasi tidak akan cocok lagi, dan datagram dapat ditolak. Mekanisme ini juga melindungi dari serangan pengulangan dengan mendeteksi duplikasi yang tidak sah.


![Image](assets/fr/050.webp)


#### Tajuk Opsi Tujuan


Header ini hanya ditujukan untuk penerima akhir datagram. Header ini dapat digunakan untuk menambahkan opsi atau metadata khusus untuk aplikasi, tanpa diperhitungkan oleh router perantara.


Pada awalnya, tidak ada opsi seperti itu yang didefinisikan dalam protokol. Namun, header ini diperkenalkan ketika IPv6 dirancang, untuk memungkinkan ekstensi di masa depan ditambahkan tanpa mengubah struktur paket secara keseluruhan. Opsi null, misalnya, hanya digunakan untuk mengisikan header dengan kelipatan 8 byte untuk tujuan penyelarasan memori.


![Image](assets/fr/051.webp)


Desain paket IPv6 dibangun di atas pemisahan yang jelas antara header dasar minimal dan header ekstensi modular. Arsitektur ini memastikan kinerja pemrosesan standar dan fleksibilitas yang diperlukan untuk mengembangkan protokol dan mengintegrasikan keamanan, perutean yang kompleks, atau mekanisme kualitas layanan, sambil mempertahankan kompatibilitas dengan infrastruktur di masa depan.


## Hubungan antara IPv6 dan DNS


<chapterId>421eacb8-b80b-4aee-910f-e069ed805f00</chapterId>


Dalam jaringan modern, DNS (*Domain Name System*) menerjemahkan nama domain menjadi alamat IP yang dapat digunakan oleh mesin. Dengan diperkenalkannya IPv6, DNS harus beradaptasi untuk mendukung alamat 128-bit sambil mempertahankan kompatibilitas dengan IPv4. Koeksistensi ini sangat penting dalam lingkungan dual-stack, di mana kedua versi IP beroperasi secara bersamaan.


### Catatan DNS khusus IPv6


Untuk mengaitkan nama domain dengan IPv6 Address, DNS menggunakan record AAAA (*quad-A*), yang serupa dengan record "A" untuk alamat IPv4. Rekor AAAA secara eksplisit memetakan nama domain ke IPv6 Address.

Contoh:


```shell
ipv6.mydmn.org.         IN      AAAA    2001:66c:2a8:22::c100:68b
```


Catatan ini menunjukkan bahwa domain `ipv6.mydmn.org` diselesaikan ke IPv6 Address `2001:66c:2a8:22::c100:68b`. Dimungkinkan, dan bahkan disarankan untuk kompatibilitas maksimum, untuk mengaitkan nama domain yang sama dengan beberapa alamat IP, baik IPv4 (melalui catatan A) atau IPv6 (melalui catatan AAAA). Hal ini memungkinkan pelanggan yang kompatibel dengan IPv6 untuk lebih memilih IPv6, sekaligus memastikan klien yang hanya menggunakan IPv4 tetap didukung.


Selain itu, DNS mendukung resolusi terbalik, yang berarti DNS dapat mencari nama domain yang terkait dengan IP Address yang diberikan. Dalam kasus IPv6, operasi ini menggunakan catatan PTR yang ditempatkan di zona `ip6.arpa`. Zona ini secara khusus disediakan untuk resolusi balik IPv6. Untuk IPv4, ini adalah zona `in-addr.arpa`.


### Resolusi terbalik


Resolusi balik IPv6 Address mengikuti proses yang ketat:

1) Perluas Address ke dalam notasi heksadesimal penuh (16 byte, yaitu 32 digit heksadesimal).

Contoh:


```shell
2001:66c:2a8:22::c100:68b
```


Menjadi:


```shell
2001:066c:02a8:0022:0000:0000:c100:068b
```


2) Balikkan urutan setiap digit heksadesimal (nibble), pisahkan dengan titik-titik dan tambahkan `ip6.arpa`:


```shell
b.8.6.0.0.0.1.c.0.0.0.0.0.0.0.0.2.2.0.0.8.a.2.0.c.6.6.0.1.0.0.2.ip6.arpa  IN PTR  ipv6.mydmn.org
```


Struktur ini memastikan pencarian balik yang terstandardisasi dan unik di ruang IPv6 Address.


**Harap diperhatikan**: Kueri DNS dapat melalui IPv4 atau IPv6. Protokol transport yang digunakan tidak berpengaruh pada jenis catatan yang dikembalikan.

Sebagai contoh:


- Klien yang tersambung melalui IPv6 dapat meminta catatan IPv4.
- Klien yang tersambung melalui IPv4 dapat meminta catatan IPv6.

Server DNS hanya merespons dengan catatan yang dimilikinya, terlepas dari protokol transport kueri.


Ketika nama host dipetakan ke IPv4 dan IPv6, pilihan Address mana yang akan digunakan diatur oleh RFC 6724, yang mendefinisikan algoritme pemilihan Address berdasarkan faktor-faktor seperti preferensi awalan, cakupan, dan jangkauan. Secara default, IPv6 umumnya lebih disukai kecuali jika diganti oleh konfigurasi sistem atau jaringan.


**Pengingat penting**: ketika menyematkan IPv6 Address dalam URL (*Uniform Resource Locator*), IPv6 Address harus diapit oleh tanda kurung siku (`[]`). Hal ini untuk menghindari kebingungan antara tanda titik dua (`:`) di dalam IPv6 Address dan tanda titik dua yang memisahkan nama host dengan port dalam URL.


Contoh yang valid:


```shell
http://[2001:db8::1]:8080
```


Hal ini memastikan bahwa URL diproses dengan benar oleh browser dan server web.


Oleh karena itu, mengintegrasikan IPv6 ke dalam sistem DNS bergantung pada jenis record baru, metode yang ketat untuk resolusi terbalik, dan aturan pemilihan dan pemformatan yang tepat untuk memastikan kompatibilitas dan konsistensi perutean.


### Ringkasan bagian


Pada bagian ini, kami menjelajahi prinsip-prinsip dasar pengalamatan IPv6. Kami mulai dengan memeriksa struktur IPv6 Address: panjang 128-bit, notasi heksadesimal, dan aturan penyederhanaan yang digunakan untuk memperpendek urutan angka nol yang berulang. Desain ini memungkinkan IPv6 untuk mengatasi keterbatasan ruang Address IPv4, sekaligus menjamin skalabilitas dan hirarki yang efisien.


Kami kemudian melihat berbagai kategori alamat IPv6: unicast, anycast, dan multicast, yang merinci cakupan, penggunaan umum, dan representasinya dalam ruang Address.


Selanjutnya, kami meninjau metode pemberian alamat IPv6 dalam jaringan lokal, baik dengan konfigurasi manual, melalui protokol DHCPv6, atau menggunakan mekanisme konfigurasi otomatis tanpa kewarganegaraan seperti yang ditawarkan oleh NDP. Pendekatan-pendekatan ini memungkinkan perangkat untuk secara otomatis mendapatkan Address mereka sendiri dari awalan yang disediakan dan MAC Address (melalui EUI-64), sekaligus menawarkan fleksibilitas dalam hal manajemen dan privasi seumur hidup.


Kami juga telah merinci bagaimana blok Address dialokasikan, mulai dari IANA, yang mendistribusikannya ke lima RIR (*Registered Internet Regions*), dan kemudian ke ISP, yang mendistribusikannya kembali ke pelanggan mereka sebagai subnet (biasanya di /48, yang memungkinkan subnet 65536 /64). Perbedaan antara blok _Provider Aggregatable_ (PA) dan _Provider Independent_ (PI) membantu mengelola skenario _multihoming_ atau pergantian penyedia.


Kami melihat bahwa DNS telah beradaptasi dengan IPv6 dengan diperkenalkannya catatan AAAA, dan bahwa mekanisme resolusi balik sekarang bergantung pada zona `ip6.arpa`. Yang penting, DNS tetap independen dari protokol transport yang digunakan (IPv4 atau IPv6), memastikan interoperabilitas yang mulus dalam lingkungan dual-stack.


Oleh karena itu, IPv6 bukan hanya peningkatan tambahan atas IPv4, tetapi juga merupakan desain ulang sistem pengalamatan yang lengkap, yang dibuat untuk memenuhi tantangan Internet global saat ini dan di masa depan.


Di bagian akhir dari kursus NET 302 ini, kita akan beralih ke praktik dan fokus pada alat diagnostik jaringan.



# Alat diagnostik jaringan


<partId>368a5c6f-ec48-4b28-970f-3a770788ad37</partId>


## Alat Akses Jaringan Layer


<chapterId>1d25a21d-6900-4fbe-a438-e06c8afb9e02</chapterId>


Pada bab pertama dari bagian terakhir tentang diagnostik jaringan ini, kami fokus pada alat untuk menganalisis akses jaringan Layer model TCP/IP. Layer ini bertanggung jawab untuk komunikasi langsung antara perangkat pada jaringan fisik yang sama, khususnya melalui penggunaan alamat MAC dan antarmuka jaringan fisik seperti kartu Ethernet atau antarmuka Wi-Fi.


Tujuannya di sini adalah untuk menyediakan alat bantu praktis bagi para administrator untuk memeriksa, menguji, dan mengoptimalkan Layer yang penting untuk konektivitas tingkat rendah. Alat-alat ini dapat digunakan untuk memverifikasi pengoperasian antarmuka yang tepat, memecahkan masalah konfigurasi kartu jaringan, atau mendeteksi anomali seperti tabrakan, kehilangan paket, atau kesalahan tautan.


### Utilitas lingkungan IP/MAC


#### alat `Arp`


Salah satu alat diagnostik tertua pada Network Access Layer adalah perintah `arp`. Meskipun semakin digantikan oleh alternatif modern seperti `ip neigh` (yang akan segera kita temukan). `Arp` masih ada di banyak sistem untuk melihat atau memanipulasi cache ARP (*Address Resolution Protocol*). Cache ini menyimpan pemetaan antara alamat IP dan alamat MAC yang dikenal secara lokal pada mesin. Dengan kata lain, ini memungkinkan Anda untuk menentukan Address fisik (MAC) mana yang sesuai dengan Address IP yang diberikan pada jaringan lokal.


Dalam praktiknya, ketika sebuah host ingin mengirim paket ke IP Address dalam subnet yang sama, host tersebut harus terlebih dahulu mengetahui MAC Address mesin target. Pemetaan ini ditangani oleh ARP, yang menyiarkan permintaan pada jaringan lokal dan menerima balasan yang berisi MAC Address yang sesuai. Hasil ini kemudian disimpan sementara di tabel lokal yang disebut "ARP cache", untuk menghindari pengulangan permintaan untuk setiap paket baru.


Untuk melihat isi cache dan memeriksa entri yang saat ini diketahui oleh mesin, gunakan:


```bash
arp -a
```


Perintah ini mencantumkan semua pemetaan IP/MAC yang terdaftar secara lokal, di semua antarmuka. Setiap baris menyediakan nama host (jika dapat diselesaikan), IP Address, MAC Address yang sesuai, dan Interface di mana pemetaan diamati.


Untuk memfilter tampilan ke IP Address tertentu, cukup tentukan saja:


```bash
arp -a 192.168.1.5
```


Hal ini memudahkan untuk memeriksa apakah IP Address tertentu ada dalam cache, yang dapat membantu mendiagnosis kegagalan komunikasi antara dua host pada jaringan yang sama.


Demikian juga, untuk menampilkan hanya entri ARP yang terkait dengan jaringan tertentu Interface (misalnya kartu Ethernet bernama `eth0`), Anda dapat menggunakan:


```bash
arp -a -i eth0
```


Hal ini sangat berguna dalam lingkungan multi-Interface (kabel, nirkabel, VPN, dll.), di mana satu host mungkin memiliki beberapa adapter jaringan.


Perintah `arp` tidak terbatas pada penggunaan hanya-baca. Perintah ini juga dapat digunakan untuk mengedit cache ARP secara manual, sebuah fitur yang sangat berharga dalam skenario pemecahan masalah tingkat lanjut tertentu atau ketika mensimulasikan kondisi tertentu. Misalnya, Anda dapat menambahkan pemetaan IP/MAC secara manual:


```bash
arp -s 192.168.1.7 00:17:BC:56:4F:25 -i eth2
```


Perintah ini membuat entri statis dalam tabel ARP lokal, mengaitkan IP Address `192.168.1.7` dengan MAC Address `00:17:BC:56:4F:25` pada Interface `eth2` Jika tidak ada Interface yang ditetapkan, sistem secara otomatis menggunakan yang pertama kali digunakan.


Anda juga dapat menghapus entri dari cache ARP, baik untuk memperbaiki kesalahan atau memaksa penemuan kembali:


```bash
arp -d 192.168.1.7
```


Hal ini akan menghapus entri, memastikan bahwa upaya komunikasi berikutnya akan memicu permintaan ARP yang baru.


**CATATAN**: Opsi hapus juga menerima nama Interface, sehingga Anda dapat menargetkan penghapusan entri tertentu secara lebih tepat.


Secara ringkas, alat `arp` menyediakan diagnostik tingkat rendah, khususnya berguna dalam jaringan lokal di mana masalah konektivitas sering kali dapat ditelusuri kembali ke resolusi Address yang salah atau usang. Namun, pada sistem terbaru, terutama dengan distribusi Linux modern, alat ini semakin digantikan oleh perintah `ip neigh`, dari toolset `iproute2`, yang menawarkan fungsionalitas yang sama dalam kerangka kerja yang lebih terpadu.


#### alat `Ip tetangga`


Pada sistem modern, khususnya distribusi Linux terbaru, perintah `ip neigh` adalah alat yang digunakan untuk memeriksa dan mengelola pemetaan antara alamat IP dan MAC. Perintah ini adalah bagian dari rangkaian `iproute2`, yang secara bertahap menggantikan alat yang lebih tua seperti `arp`, menyediakan kerangka kerja yang lebih konsisten dan fleksibel untuk diagnostik pada sambungan data Layer.


Perintah `ip neigh` menanyakan cache tetangga IP lokal, yang setara dengan cache ARP untuk IPv4 dan cache NDP (_Neighbor Discovery Protocol_) untuk IPv6. Cache ini menyimpan hubungan yang diketahui antara alamat IP (v4 atau v6) dan alamat MAC, bersama dengan statusnya (valid, tertunda, kadaluarsa...).


Perintah dasar untuk menampilkan cache adalah:


```bash
ip neigh
```


Ini menghasilkan daftar entri, yang menunjukkan IP tujuan Address, jaringan yang relevan Interface, MAC Address yang terkait (jika tersedia), dan status entri (mis. `DAPAT DIJANGKAU`, `TUNDA`, `TUNDA`, `GAGAL`...).


Contoh keluaran:


```bash
192.168.1.5 dev eth0 lladdr 00:17:BC:56:4F:25 REACHABLE
```


Baris ini menunjukkan bahwa mesin mengetahui pemetaan yang valid antara IP Address `192.168.1.5` dan MAC Address `00:17:BC:56:4F:25` melalui Interface `eth0`.


Anda juga dapat memfilter entri berdasarkan kriteria seperti IP Address, Interface, atau negara bagian. Misalnya, untuk menanyakan hanya Address `192.168.1.7`:


```bash
ip neigh show 192.168.1.7
```


Atau untuk menampilkan semua entri untuk Interface `eth1`:


```bash
ip neigh show dev eth1
```


Selain konsultasi, `ip neigh` juga dapat digunakan untuk mengedit cache secara manual. Misalnya, untuk menambahkan entri statis:


```bash
ip neigh add 192.168.1.7 lladdr 00:17:BC:56:4F:25 dev eth1 nud permanent
```


Ini secara permanen mengaitkan IP Address `192.168.1.7` dengan MAC Address yang ditentukan pada Interface `eth1`. Opsi `nud permanent` (untuk _Deteksi Ketidakterjangkauan Tetangga_) memastikan bahwa entri tidak akan secara otomatis dibatalkan.


Sebaliknya, untuk menghapus entri cache:


```bash
ip neigh del 192.168.1.7 dev eth1
```


Hal ini memaksa sistem untuk menyelesaikan kembali pemetaan pada saat berikutnya berkomunikasi dengan Address tersebut.


**CATATAN**: Alat `ip neigh` berfungsi untuk IPv4 dan IPv6. Untuk IPv4, alat ini berinteraksi dengan ARP; untuk IPv6, alat ini berinteraksi dengan NDP. Hal ini memberikan pendekatan yang terpadu dan konsisten untuk mengelola hubungan IP/MAC di seluruh keluarga protokol, menjadikan `ip neigh` sebagai standar modern untuk manajemen tetangga pada sistem Linux.


### Alat analisis paket


Untuk menganalisis secara menyeluruh apa yang terjadi pada jaringan komputer, administrator memerlukan alat yang dapat menangkap paket yang dipertukarkan di antara mesin. Dua utilitas yang menonjol sebagai tolok ukur: `tcpdump` dan `Wireshark`. Alat-alat ini sangat penting untuk mendiagnosa perilaku abnormal, mengaudit pertukaran protokol, atau mempelajari keamanan jaringan dengan memeriksa isi frame.


#### `ttcpdump`: analisis baris perintah


`tcpdump` adalah alat baris perintah yang sangat kuat yang dirancang untuk menangkap dan menampilkan paket yang berjalan melalui jaringan Interface. Alat ini beroperasi secara real time, dan berkat desainnya yang ringan, dapat digunakan pada sistem tanpa Interface grafis atau dengan sumber daya yang terbatas. Alat ini bergantung pada pustaka `libpcap`, yang menyediakan fungsi penangkapan tingkat rendah yang tidak bergantung pada perangkat keras.


Penggunaan umum `tcpdump` adalah untuk memonitor aktivitas jaringan dari sebuah mesin atau segmen jaringan, menyaring paket sesuai dengan kriteria tertentu. Hasilnya dapat dialihkan ke sebuah file, sehingga trafik dapat diarsipkan untuk analisis nanti atau diputar ulang di alat lain, seperti Wireshark.


Sintaks perintah umum adalah:


```bash
tcpdump -w <file.cap> -i <interface> -s <snapshot_length> -n <filters>
```



- `-w` menulis paket yang ditangkap ke file dalam format `libpcap` (ekstensi `.cap` atau `.pcap`);
- `-i` menentukan jaringan Interface yang akan dimonitor (mis. `eth0`, `wlan0`);
- `-s` menetapkan jumlah maksimum data yang ditangkap per paket. Menentukan `0` akan menangkap semua paket;
- `-n` menonaktifkan DNS dan resolusi nama layanan, sehingga meningkatkan kinerja.


Filter ekspresi di akhir perintah memungkinkan Anda membatasi tangkapan pada sebagian lalu lintas. Anda dapat menggabungkan kata kunci `host`, `port`, `src`, `dst`, dll., untuk mempersempit pilihan.


Contoh: untuk menangkap paket HTTP (port 80) ke atau dari server `192.168.25.24`, dan menyimpannya dalam file `fichier.cap`:


```bash
tcpdump -w fichier.cap -i eth0 -s 0 -n port 80 and host 192.168.25.24
```


File yang dihasilkan nantinya dapat dianalisis dalam alat bantu grafis atau diputar ulang pada sistem lain.


#### Wireshark: analisis visual tingkat lanjut


Wireshark, yang sebelumnya dikenal sebagai *Ethereal*, adalah program analisis jaringan yang lengkap dengan grafis Interface. Tidak seperti `tcpdump`, program ini menyediakan visualisasi paket yang terstruktur dan mendetail, termasuk pembedahan protokol, grafik aliran, statistik trafik, dan filter interaktif. Program ini juga bergantung pada `libpcap`, yang berarti program ini dapat membuka dan memproses file tangkapan yang dihasilkan oleh `tcpdump`.


Wireshark tersedia pada banyak sistem operasi, termasuk Linux dan Windows. Menginstalnya memerlukan hak administrator untuk mengakses antarmuka penangkapan. Setelah diluncurkan, Anda dapat memilih jaringan Interface dari menu *Capture*. Mengklik *Start* akan memulai perekaman paket secara real-time. Tampilan dibagi menjadi tiga panel:


- daftar bingkai yang ditangkap ;
- detail yang diterjemahkan protokol,
- data heksadesimal mentah.



![Image](assets/fr/052.webp)



Wireshark unggul dalam skenario di mana Anda perlu mengamati perilaku protokol yang kompleks, merekonstruksi dialog aplikasi (seperti sesi HTTP atau DNS), atau mempelajari waktu respons layanan. Wireshark juga mendukung filter tampilan yang sangat spesifik dengan menggunakan sintaks khusus (berbeda dengan `tcpdump`) untuk memfokuskan hanya pada paket-paket yang relevan.


#### Alat pelengkap


Penting untuk dicatat bahwa `tcpdump` dan Wireshark tidak dapat dipertukarkan: masing-masing memiliki kekuatannya sendiri. `tcpdump` lebih cocok untuk lingkungan baris perintah, skrip otomatis, dan intervensi server jarak jauh, sementara Wireshark ideal untuk analisis lalu lintas yang mendetail, interaktif, dan edukatif.


Kedua alat ini dapat digabungkan: tangkapan dapat dilakukan pada sistem jarak jauh dengan `tcpdump`, kemudian file `.cap` ditransfer untuk dianalisis dengan Wireshark pada mesin lokal. Pendekatan ini banyak digunakan dalam praktik.


### Alat analisis Interface


Pada Network Access Layer, sering kali diperlukan untuk menanyakan dan mengonfigurasi antarmuka jaringan fisik untuk mendiagnosis kerusakan, mengoptimalkan kinerja, atau memverifikasi integritas koneksi. Salah satu alat yang paling kuat yang tersedia di Linux untuk tujuan ini adalah `ethtool`, sebuah utilitas baris perintah yang tidak hanya menyediakan informasi teknis terperinci tentang Ethernet Interface, tetapi juga memungkinkan Anda untuk menyesuaikan beberapa parameter secara real time.


#### Lihat spesifikasi Interface


Fitur inti dari `ethtool` adalah kemampuannya untuk menanyakan Interface dan menampilkan karakteristik saat ini. Hal ini memungkinkan Anda untuk memeriksanya:


- kecepatan tautan (misalnya 100 Mbit/dtk, 1 Gbit/dtk, atau 10 Gbit/dtk);
- mode negosiasi (setengah dupleks atau dupleks penuh);
- apakah negosiasi otomatis diaktifkan;
- jenis port (tembaga, serat, dll.);
- status tautan (aktif atau tidak) ;
- dukungan untuk fitur-fitur canggih seperti *Wake-on-LAN*.


Informasi ini sangat berguna untuk mendiagnosis masalah yang berkaitan dengan konektivitas fisik atau pengaturan negosiasi yang tidak sesuai antara kartu jaringan host dan peralatan yang terhubung dengannya (sakelar, router, dll.).


Untuk mendapatkan informasi ini, cukup jalankan:


```bash
ethtool enp0s3
```


Perintah ini menghasilkan laporan terperinci tentang `enp0s3` Interface, sebuah konvensi penamaan yang umum pada sistem berbasis CentOS atau RHEL.



![Image](assets/fr/053.webp)



#### Memodifikasi parameter Interface secara dinamis


`ethtool` tidak terbatas pada pengamatan: ini juga memungkinkan Anda untuk menyesuaikan parameter Interface tertentu tanpa me-reboot mesin. Hal ini memungkinkan, misalnya, untuk memaksakan kecepatan tautan tertentu atau mengaktifkan fitur sesuai dengan kebutuhan jaringan lokal.


Opsi `-s` digunakan untuk mengonfigurasi parameter secara dinamis, misalnya:


- kecepatan tautan (`speed`), ditetapkan secara eksplisit (misalnya 1000 untuk 1 Gbit/dtk);
- mode dupleks (`duplex`), baik `setengah` atau `penuh`;
- mengaktifkan atau menonaktifkan negosiasi otomatis (`autoneg`);
- mengaktifkan *Wake-on-LAN* (`wol`);
- jenis port.


Contoh 1: aktifkan negosiasi otomatis pada Interface:


```bash
ethtool -s enp0s3 autoneg on
```


Contoh 2: aktifkan fitur *Wake-on-LAN* (untuk mengaktifkan mesin dari jarak jauh melalui paket ajaib):


```bash
ethtool -s enp0s3 wol p
```


Dalam contoh ini, opsi `p` menetapkan bahwa pengaktifan akan terjadi segera setelah paket *Wake-on-LAN* terdeteksi. Pengaturan ini sering digunakan di lingkungan perusahaan untuk melakukan pembaruan semalam atau pemeliharaan jarak jauh.


#### Instalasi alat


Penting untuk dicatat bahwa `ethtool` tidak selalu terinstal secara default. Pada distribusi Red Hat/CentOS, alat ini dapat diinstal dengan perintah:


```bash
yum install -y ethtool
```


Pada Debian dan Ubuntu, perintah yang setara adalah:


```bash
sudo apt install ethtool
```


**PERINGATAN **: dalam semua perintah `ethtool`, nama jaringan Interface harus ditentukan segera setelah opsi (sebagai `-s`). Kesalahan sintaks dalam penempatan parameter akan membuat perintah menjadi tidak valid atau tidak efektif.



## Alat Jaringan Layer


<chapterId>d2c5bf35-4284-4af8-8e8b-049c696a511b</chapterId>


### Alat analisis lalu lintas


Dalam diagnostik jaringan, perintah `ping` tetap menjadi salah satu alat yang paling sederhana namun paling kuat untuk menguji konektivitas antara dua mesin. Perintah ini memeriksa apakah host jarak jauh dapat dijangkau pada waktu tertentu, sekaligus memberikan informasi tentang latensi, stabilitas sambungan, dan resolusi DNS.


Perintah `ping` bergantung pada protokol ICMP (*Internet Control Message Protocol*). Saat pengguna mengirim permintaan `ping`, sistem akan mengirimkan paket ICMP "Echo Request" ke IP Address atau nama host. Jika mesin target sedang online dan jalur jaringannya valid, mesin tersebut akan merespons dengan paket ICMP "Echo Reply". Mekanisme sederhana ini dapat digunakan untuk mengukur latensi dan mendeteksi masalah konektivitas atau resolusi nama.


Contoh perintah klasik:


```bash
ping 172.17.18.19
```


Respons yang khas:


```bash
mydmn.org (172.17.18.19): 56 data bytes
64 bytes from 172.17.18.19: icmp_seq=0 ttl=56 time=7.7 ms
64 bytes from 172.17.18.19: icmp_seq=1 ttl=56 time=6.0 ms
64 bytes from 172.17.18.19: icmp_seq=2 ttl=56 time=5.5 ms
```


Pada contoh ini, resolusi nama telah dilakukan secara otomatis: domain `mydmn.org` diasosiasikan dengan IP Address `172.17.18.19`, yang mengonfirmasikan bahwa resolusi DNS bekerja dengan benar. Perintah ini juga memberikan rincian teknis seperti:


- nomor urut iCMP (`icmp_seq`), berguna untuk memeriksa urutan respons;
- TTL (*Time-To-Live*), yang mengindikasikan jumlah hop yang tersisa sebelum paket dibuang;
- waktu pulang-pergi/tunda (`waktu`), dinyatakan dalam milidetik, yang memberikan perkiraan latensi tautan.


#### Analisis yang lebih rinci tentang parameter ICMP


TTL adalah bidang yang sangat penting dalam protokol IP. Setiap datagram diinisialisasi dengan nilai TTL oleh pengirim (biasanya 64, 128 atau 255). Setiap router di sepanjang jalur akan mengurangi nilai ini sebesar 1. Jika TTL mencapai 0 sebelum mencapai tujuannya, paket akan dibuang dan kesalahan ICMP akan dikembalikan ke pengirim. Mekanisme ini mencegah perulangan perutean yang tak terbatas.


Waktu propagasi (*tundaan/waktu pulang-pergi*) mengukur penundaan paket untuk meninggalkan pengirim, mencapai target, dan kembali. Dalam praktiknya, penundaan di bawah 200 ms dianggap dapat diterima untuk sambungan yang stabil. Penundaan yang sangat tinggi dapat mengindikasikan kepadatan jaringan, perutean yang tidak efisien, atau kualitas sambungan yang buruk.


#### Penggunaan `ping` tingkat lanjut


`ping` menyediakan opsi untuk menyempurnakan pengujian dan mengamati perilaku jaringan tertentu.


Untuk mengirim permintaan broadcast, Anda dapat menggunakan opsi `-b` untuk menargetkan semua host pada subnet:

```bash
ping -b 192.168.1.255
```


Ini berguna di jaringan lokal untuk mendeteksi host yang aktif dengan cepat atau menguji bagaimana jaringan menangani permintaan broadcast. Namun, dalam banyak pengaturan, router dan firewall memblokir ping broadcast untuk mencegah serangan amplifikasi.


Anda juga dapat menentukan interval khusus di antara permintaan dengan opsi `-i` (default: 1 detik):


```bash
ping -i 0.2 -c 10 192.168.1.7
```


Ini mengirimkan 10 permintaan ICMP pada interval 0,2 detik. Pengujian tersebut berguna untuk mendeteksi fluktuasi latensi dalam waktu singkat atau untuk memberikan tekanan ringan pada sambungan untuk mengevaluasi stabilitasnya.


### Alat analisis tabel perutean


Perintah `ip route`, bagian dari paket `iproute2`, adalah alat yang direkomendasikan dan alat standar pada sistem Linux modern untuk memeriksa dan mengelola tabel perutean IP kernel. Perintah ini menggantikan perintah `route` yang sudah usang, menawarkan sintaks yang lebih jelas, konsistensi yang lebih baik, dan dukungan yang lebih luas untuk fitur-fitur modern (IPv6, beberapa tabel, ruang nama, dll.).


#### Menampilkan tabel perutean


Untuk menampilkan tabel perutean saat ini:


```bash
ip route show
```


Output ini berisi daftar semua rute yang diketahui oleh kernel, yaitu jalur yang dilalui oleh paket-paket yang keluar tergantung pada tujuannya.


Contoh keluaran:


```bash
default via 192.168.1.1 dev eth0 proto dhcp metric 100
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.100
```


Setiap garis mewakili sebuah rute. Kolom-kolom utama meliputi:


- default**: rute default, digunakan ketika tidak ada rute yang lebih spesifik yang cocok.
- via**: gerbang yang digunakan untuk mencapai tujuan.
- dev**: jaringan Interface yang digunakan.
- proto**: bagaimana rute dibuat (manual, DHCP, kernel, dll).
- metrik**: biaya rute, digunakan untuk memprioritaskan beberapa jalur yang memungkinkan.
- scope**: cakupan rute (misalnya `link` untuk rute yang terhubung secara langsung).
- src**: IP sumber Address yang digunakan untuk paket keluar pada Interface ini.


#### Menambah dan menghapus rute


Anda juga dapat memodifikasi tabel perutean secara dinamis, misalnya dengan menambah atau menghapus rute statis.


Menambahkan rute statis:


```bash
ip route add 192.168.1.0/24 via 192.168.1.1 dev eth0
```


Ini mengkonfigurasi rute ke jaringan `192.168.1.0/24`, melalui gateway `192.168.1.1` pada Interface `eth0`.


Hapus rute ini:


```bash
ip route del 192.168.1.0/24
```


Perintah ini menghapus rute yang telah ditentukan sebelumnya.


#### Perintah yang berguna


Berikut ini beberapa varian yang berguna untuk analisis atau skrip:


- `ip -4 route`: menampilkan rute IPv4 saja;
- `ip -6 route`: hanya menampilkan rute IPv6;
- `ip tabel daftar rute utama`: menampilkan tabel perutean utama (nilai default);
- `ip route get <Address>`: tunjukkan Interface dan gateway mana yang akan digunakan oleh paket ke Address yang diberikan.


Contoh:


```bash
ip route get 8.8.8.8
```


Ini menampilkan rute yang tepat yang akan diambil paket untuk mencapai `8.8.8.8`.


### Alat penelusuran


Salah satu alat yang paling efektif untuk menganalisis rute yang diambil oleh paket IP antara host sumber dan tujuan target adalah perintah `traceroute`. Perintah ini menunjukkan, langkah demi langkah, jalur yang dilalui oleh paket dan mengidentifikasi router perantara yang dilaluinya. Jika terjadi kerusakan sambungan jaringan atau pemutusan layanan, `traceroute` membantu menentukan lokasi masalah dengan tepat.


Seperti halnya perintah `ping`, target dapat ditentukan dengan nama domain yang memenuhi syarat (FQDN) atau dengan IP Address-nya. Sebagai contoh:


```bash
traceroute mydmn.org
```


#### Prinsip operasi


`traceroute` bergantung pada bidang TTL (*Time To Live*) di header paket IP. Seperti yang dijelaskan sebelumnya, bidang ini adalah penghitung yang dikurangi oleh setiap router di sepanjang jalur. Ketika TTL mencapai nol, paket dibuang, dan router mengembalikan pesan ICMP "Waktu Terlampaui" ke pengirim. Mekanisme ini mencegah loop tak terbatas jika terjadi salah rute.


`traceroute` memanfaatkan perilaku ini untuk memetakan router antara pengirim dan penerima:


- Pertama-tama router mengirimkan serangkaian paket UDP (biasanya tiga), dengan TTL 1. Router pertama menemukan TTL 0 sehingga ia membuang paket dan kemudian membalas dengan pesan ICMP, yang mengungkapkan IP Address dan waktu respons.
- Selanjutnya, ia mengirimkan serangkaian paket lain dengan TTL 2, mengungkapkan router kedua.
- Proses ini berulang hingga tujuan tercapai, di mana pada saat itu host merespons dengan pesan ICMP Port Unreachable, yang mengindikasikan bahwa titik akhir telah tercapai.


Secara default, `traceroute` menggunakan paket UDP yang dikirim ke port yang tidak digunakan (biasanya dimulai dari 33434), tetapi juga dapat dikonfigurasi untuk menggunakan ICMP (seperti `ping`) atau bahkan TCP, tergantung pada sistem atau varian perintah.


Contoh keluaran:


```bash
traceroute to www.google.fr (216.58.210.35), 64 hops max, 52 byte packets

1  par81-024.ff.avast.com (62.210.189.205)   25.107 ms  24.235 ms  24.383 ms
2  62-210-189-1.rev.poneytelecom.eu (62.210.189.1)  27.341 ms  27.119 ms  28.184 ms
3  a9k1-45x-s43-1.dc3.poneytelecom.eu (195.154.1.92)  25.910 ms  25.040 ms  25.558 ms
4  72.14.218.182 (72.14.218.182)  36.234 ms  39.907 ms  38.130 ms
5  108.170.244.177 (108.170.244.177)  25.880 ms
108.170.244.240 (108.170.244.240)  25.791 ms
108.170.244.177 (108.170.244.177)  26.449 ms
6  216.239.62.143 (216.239.62.143)  26.491 ms
216.239.43.157 (216.239.43.157)  26.414 ms
216.239.62.139 (216.239.62.139)  26.400 ms
...
9  108.170.246.161 (108.170.246.161)  33.174 ms
108.170.246.129 (108.170.246.129)  34.342 ms
108.170.246.161 (108.170.246.161)  33.707 ms
10  108.170.232.105 (108.170.232.105)  33.845 ms  33.846 ms
108.170.232.103 (108.170.232.103)  34.206 ms
11  lhr25s11-in-f35.1e100.net (216.58.210.35)  34.094 ms  33.353 ms  33.718 ms
```


Setiap baris berhubungan dengan router yang dilalui, dengan hingga tiga pengukuran waktu (dalam milidetik) yang mengindikasikan latensi perjalanan pulang pergi ke router tersebut. Nilai-nilai ini membantu menilai kinerja setiap segmen jaringan.


#### Interpretasi hasil


Jika router tidak merespons atau memfilter pesan ICMP, tanda bintang `*` akan ditampilkan sebagai pengganti waktu respons. Hal ini mungkin mengindikasikan:


- firewall yang memblokir balasan ICMP,
- perangkat yang dikonfigurasi untuk tidak merespons, atau
- masalah konektivitas sementara di sepanjang jalur.


Dengan demikian, `traceroute` tidak hanya mengidentifikasi rute yang diambil, tetapi juga menyoroti titik-titik latensi atau gangguan yang tidak normal.


Pada beberapa sistem, perintah `tracepath` yang setara dapat digunakan, yang tidak memerlukan hak akses root. Untuk IPv6, gunakan `traceroute6` atau `tracepath6`.


Contoh untuk penelusuran IPv6:


```bash
traceroute6 ipv6.google.com
```


### Alat untuk memeriksa koneksi aktif


Untuk mendiagnosis koneksi jaringan yang aktif dan memonitor aktivitas jaringan pada sistem Linux, perintah `ss` (kependekan dari _socket statistics_) adalah alat referensi modern. Bagian dari paket `iproute2`, alat ini menggantikan `netstat` yang sudah tidak digunakan lagi, menawarkan kinerja yang lebih baik dan hasil yang lebih akurat.


`ss` menampilkan koneksi TCP dan UDP yang aktif, port pendengar, alamat lokal dan jarak jauh, status koneksi, dan proses yang terkait.


#### Penggunaan umum


Bila dijalankan tanpa opsi, perintah `ss` akan menampilkan koneksi TCP yang aktif. Sintaks dasar:


```bash
ss [options]
```


Beberapa opsi umum untuk menyempurnakan analisis:


- `-t`: hanya menampilkan koneksi TCP;
- `-u`: hanya menampilkan koneksi UDP;
- `-l`: hanya menampilkan soket pendengaran;
- `-n`: menonaktifkan resolusi nama (IP mentah dan nomor port);
- `-p`: menampilkan setiap soket yang terkait dengan proses (PID dan nama program),
- `-a`: menampilkan semua sambungan, termasuk sambungan yang tidak aktif,
- `-s`: menampilkan statistik soket tingkat tinggi.


#### Studi kasus


Untuk menampilkan semua koneksi aktif yang menggunakan TCP port 80 (HTTP):


```bash
ss -ant | grep ':80'
```


Ini menunjukkan koneksi TCP aktif yang melibatkan port 80. Status seperti `DENGAR`, `TETAP`, `TUNGGU` menunjukkan status saat ini dari setiap Exchange.


Contoh keluaran:

```
ESTAB 0 0 192.168.1.10:54321  93.184.216.34:80
```


Untuk menampilkan semua koneksi jaringan dengan proses yang terkait:


```bash
ss -tulnp
```


Untuk mendapatkan ringkasan penggunaan soket secara keseluruhan:

```bash
ss -s
```


Untuk memfilter koneksi UDP saja:

```bash
ss -unp
```


Perintah-perintah ini sangat berguna untuk mendeteksi koneksi yang mencurigakan, port mendengarkan yang tidak terduga, atau memantau aktivitas layanan tertentu.


## Transportasi dan alat Layer teratas


<chapterId>bce47931-930e-4288-b0fd-666c9a1066b5</chapterId>


### Alat bantu kueri DNS


Pada lapisan atas model TCP/IP, terutama pada Aplikasi Layer, penting untuk memahami cara kerja resolusi nama. Alat bantu kueri DNS memungkinkan Anda memeriksa apakah nama domain dikaitkan dengan benar dengan IP Address, dan juga membantu mendiagnosis masalah server DNS seperti kesalahan konfigurasi, penundaan propagasi, atau tidak tersedianya. Alat-alat ini sangat penting bagi administrator jaringan atau pengguna yang menginginkan pemahaman yang lebih dalam tentang pertukaran DNS dalam lingkungan IP.


#### Perintah `nslookup`


Alat kueri DNS yang paling sederhana adalah `nslookup`. Alat ini mengirimkan kueri ke server DNS dan mengembalikan IP Address yang terkait dengan nama domain (atau sebaliknya). Secara default, alat ini menanyakan server DNS yang dikonfigurasi sistem, tetapi Anda juga dapat menentukan server secara langsung dalam perintah.


Contoh pencarian langsung:

```bash
nslookup mydmn.org
```


Menanyakan server DNS tertentu:

```bash
nslookup mydmn.org 192.6.23.4
```


Permintaan tersebut meminta server DNS di `192.6.23.4` untuk menyelesaikan nama `mydmn.org`. Hal ini sangat berguna untuk memeriksa apakah server DNS tertentu mengenali nama domain atau untuk memverifikasi bahwa server tersebut berfungsi dengan baik.


#### Perintah `dig`


`dig` (*Domain Information Groper*) adalah alat yang lebih modern, lengkap, dan fleksibel daripada `nslookup`. Alat ini mendukung kueri yang rumit dan menyediakan informasi rinci tentang proses resolusi, hierarki server yang terlibat, jenis catatan yang dikembalikan (A, AAAA, MX, TXT, dll.), dan kesalahan yang ditemui.


Contoh kueri dasar:

```bash
dig mydmn.org
```


Menanyakan server DNS tertentu:

```bash
dig @192.6.23.4 mydmn.org
```


Perintah ini memeriksa ketersediaan record DNS pada server tertentu.

Salah satu keunggulan utama `dig` adalah bahwa ia menampilkan detail respons DNS, sehingga sangat berguna untuk mendiagnosis kesalahan konfigurasi.


#### Konfigurasi manual untuk penyelesai DNS


Kadang-kadang perlu untuk mengganti server DNS yang digunakan secara lokal, misalnya, dalam lingkungan pengujian atau untuk memaksa penggunaan server tertentu. Hal ini dapat dilakukan dengan mengedit file `/etc/resolv.conf`, yang mendefinisikan pengaturan resolusi DNS sistem.


Contoh konfigurasi:


```bash
vi /etc/resolv.conf

search mydmn.org
nameserver 192.168.1.10
nameserver 192.168.1.11
```



- Bidang `pencarian` menentukan domain untuk ditambahkan secara otomatis ketika menyelesaikan nama pendek.
- Entri `nameserver` menentukan server DNS yang akan digunakan, dalam urutan prioritas.


Pada banyak distribusi modern (terutama yang menggunakan `systemd-resolved`), perubahan pada `/etc/resolv.conf` bersifat sementara dan dapat ditimpa pada saat reboot atau koneksi ulang jaringan. Metode yang lebih permanen termasuk menggunakan `resolvconf`, `systemd-resolved`, atau memodifikasi konfigurasi *NetworkManager*.


#### Perintah `host`


Alat DNS lain yang sederhana namun efektif adalah `host`. Alat ini mengubah nama domain menjadi alamat IP (atau sebaliknya) dan dapat membantu mendiagnosis kegagalan atau kesalahan konfigurasi DNS pada jaringan Interface.


Contoh:

```bash
host mydmn.org
```


Pencarian terbalik:

```bash
host 192.6.23.4
```


`host` sangat berguna untuk pemeriksaan cepat, terutama ketika digunakan dalam skrip baris perintah.


Permintaan yang berulang-ulang atau intensif ke server DNS pihak ketiga tanpa izin dapat ditafsirkan sebagai upaya penyusupan atau aktivitas berbahaya. Jika digunakan secara tidak benar, atau terhadap jaringan yang tidak Anda kendalikan, perintah-perintah ini dapat menyerupai pemindaian pengintaian, yang sering kali merupakan langkah pertama dalam serangan. Selalu batasi penggunaannya pada lingkungan yang Anda kelola atau di mana Anda memiliki otorisasi eksplisit.


### Alat Pemindaian Jaringan


Saat memantau atau mengamankan jaringan lokal atau area luas, sangat penting untuk mengidentifikasi perangkat yang aktif dan layanan yang mereka ekspos. Inilah yang dilakukan oleh alat `nmap` (*Network Mapper*).


https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

#### Memperkenalkan `nmap`


`nmap` memungkinkan pemindaian yang ditargetkan pada satu atau beberapa host untuk mendeteksi port yang terbuka, layanan yang tersedia (HTTP, SSH, DNS, dll.), dan terkadang bahkan jenis sistem operasi yang digunakan. Berkat banyak pilihannya, `nmap` memberikan gambaran umum yang tepat tentang permukaan eksposur jaringan, yang sangat penting selama audit atau fase pengerasan manajemen infrastruktur.


Sama seperti perintah `host`, `nmap` tidak boleh digunakan pada jaringan atau infrastruktur yang bukan milik Anda, atau tanpa otorisasi eksplisit. Pemindaian port yang tidak sah dapat ditandai sebagai upaya pengintaian yang berbahaya, sering kali terdeteksi oleh sistem keamanan (firewall, IDS/IPS), dan bahkan dapat menyebabkan konsekuensi hukum.


#### Penggunaan dasar


Untuk memindai host tertentu dan melihat port yang terbuka:

```bash
nmap 192.168.0.1
```


Perintah ini memindai 1000 port yang paling umum pada host `192.168.0.1` dan menampilkan layanan yang diakses dan protokol yang digunakan. Jika resolusi DNS dikonfigurasi, Anda juga dapat menggunakan nama host sebagai pengganti IP Address.


#### Pemindaian jaringan lengkap


Salah satu keunggulan `nmap` adalah kemampuannya untuk memindai seluruh rentang alamat dengan satu perintah. Hal ini memudahkan, misalnya, untuk menginventarisir semua mesin yang aktif di jaringan dengan cepat:


```bash
nmap 192.168.0.0/24
```


Dalam kasus ini, semua host dalam rentang `192.168.0.0` hingga `192.168.0.255` akan ditanyakan. Untuk setiap IP Address, hasilnya mencantumkan daftar port yang terbuka, statusnya (terbuka, difilter, dll.), dan, jika memungkinkan, nama layanan yang sesuai.



![Image](assets/fr/055.webp)



Seorang administrator dapat mengandalkan `nmap` untuk beberapa tugas:


- Mendeteksi host yang aktif**: mengidentifikasi mesin mana yang merespons dalam sebuah subnet;
- Inventaris layanan**: memastikan hanya port yang diperlukan yang dapat diakses (prinsip hak istimewa yang paling sedikit);
- Pemeriksaan kepatuhan**: bandingkan port terbuka dengan kebijakan keamanan organisasi;
- Pencegahan kerentanan**: temukan layanan yang tidak aman atau ketinggalan zaman yang berjalan di mesin-mesin penting.


https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

### Alat interogasi proses


Untuk analisis mendalam tentang proses aktif dan file yang terbuka, khususnya dalam konteks jaringan, administrator Linux sering menggunakan perintah `lsof` (*List Open Files*). Terlepas dari namanya, `lsof` tidak terbatas pada file tradisional: pada sistem UNIX, segala sesuatu dianggap sebagai file, termasuk soket jaringan, perangkat, dan saluran komunikasi.


Oleh karena itu, alat ini menyediakan tampilan penampang sistem dengan menghubungkan proses aktif, port jaringan yang terbuka, file yang diakses, dan pengguna yang terlibat.


#### Analisis jaringan dengan `lsof`


Opsi `-i` membatasi output untuk koneksi jaringan (TCP, UDP, IPv4, atau IPv6). Hal ini memudahkan untuk melihat proses mana yang berkomunikasi melalui jaringan:


```bash
lsof -i
```


Perintah ini mencantumkan semua proses yang sedang berjalan menggunakan soket jaringan, menunjukkan port yang digunakan, protokol (TCP/UDP), status koneksi, serta PID dan pengguna yang terkait.


#### Pemfilteran berdasarkan IP Address atau port


Anda dapat mempersempit pencarian dengan menentukan IP Address dan port, untuk mengisolasi aliran jaringan tertentu. Misalnya, untuk memeriksa sesi SMTP (port 25) dengan host tertentu:


```bash
lsof -n -i @192.168.2.1:25
```


Ini hanya akan menampilkan koneksi jaringan yang aktif dengan host `192.168.2.1` pada port 25, yang berguna untuk mendiagnosis aktivitas yang mencurigakan atau masalah aliran SMTP.


#### Pelacakan akses perangkat


Kelebihan lain dari `lsof` adalah melacak file khusus seperti partisi disk. Sebagai contoh, untuk memeriksa proses mana yang telah membuka file pada `/dev/sda1`:


```bash
lsof /dev/sda1
```


Hal ini berguna ketika upaya pelepasan gagal karena perangkat masih digunakan, atau ketika menyelidiki aplikasi mana yang mengakses partisi.


#### Analisis silang: proses dan jaringan


Opsi dapat digabungkan untuk mendapatkan wawasan yang tepat. Misalnya, untuk melihat semua port jaringan yang dibuka oleh proses dengan PID 1521:


```bash
lsof -i -a -p 1521
```


Opsi `-a` memotong kriteria (`-i` dan `-p`), membatasi output hanya pada koneksi jaringan dari proses tersebut.


#### Pelacakan multi-pengguna


`lsof` juga dapat digunakan untuk menganalisis aktivitas oleh pengguna tertentu, membuat daftar semua file yang telah mereka buka, yang secara opsional disaring oleh PID:


```bash
lsof -p 1521 -u 500,phil
```


Ini menunjukkan file atau koneksi jaringan yang digunakan oleh pengguna `phil` atau UID 500, terbatas pada proses 1521.


### Ringkasan Bagian


Pada bagian terakhir ini, kami telah menjelajahi berbagai alat yang sangat diperlukan untuk mendiagnosis, menganalisis, dan mengelola jaringan komputer. Terstruktur di sekitar lapisan model TCP/IP, studi ini tidak hanya menjelaskan cara kerja komunikasi jaringan, tetapi juga menetapkan metodologi yang ketat untuk mengidentifikasi, mengisolasi, dan menyelesaikan masalah potensial.


Alat-alat ini memberikan administrator seperangkat tuas teknis yang koheren untuk memantau kesehatan jaringan, menganalisis lalu lintas, mengaudit koneksi, dan dengan cepat mengintervensi peralatan atau layanan yang rusak.


#### Akses Jaringan Layer


Alat yang memberikan visibilitas langsung ke antarmuka dan bingkai:


- arp / ip neigh**: memeriksa dan memodifikasi cache ARP/NDP untuk memeriksa atau mengoreksi asosiasi IP-MAC;
- tcpdump**: penangkapan paket baris perintah, dapat difilter dan diekspor;
- Wireshark**: analisis paket grafis dengan penguraian protokol yang mendalam;
- ethtool**: menanyakan dan menyesuaikan parameter fisik kartu Ethernet (kecepatan, dupleks, WoL, dll.).


#### Jaringan Layer


Alat untuk menilai konektivitas IP, perutean, dan lalu lintas paket:


- ping**: menguji daya jangkau dan mengukur latensi dengan ICMP;
- ip route**: memeriksa dan memodifikasi tabel perutean untuk mengontrol jalur paket;
- traceroute**: identifikasi router hop-by-hop di sepanjang rute ke suatu tujuan;
- ss**: inventaris terperinci dari soket TCP/UDP dan proses yang terkait (penerus netstat).


#### Lapisan Transportasi dan Aplikasi


Alat untuk mendiagnosis layanan dan proses:


- nslookup / dig / host**: Kueri DNS untuk memvalidasi resolusi nama dan menganalisis catatan;
- nmap**: jelajahi port terbuka dan layanan yang terbuka untuk menilai permukaan serangan;
- lsof**: daftar file dan soket yang dibuka oleh proses, menghubungkan sistem dan aktivitas jaringan.


Menguasai alat-alat ini, masing-masing selaras dengan tahap tertentu dari model TCP/IP, memungkinkan pendekatan metodis: mulai dari Layer fisik, bergerak melalui perutean, dan hingga layanan aplikasi. Rangkaian keahlian ini melengkapi administrator untuk mendiagnosis, mengamankan, dan mengoptimalkan infrastruktur mereka, memastikan kinerja dan ketersediaan jaringan.


# Bagian akhir


<partId>09d5393c-63bc-42fc-bf79-c65e380211bd</partId>


## Ulasan & Peringkat


<chapterId>114c33c0-9831-4d74-affd-f5d37adc53c3</chapterId>


<isCourseReview>true</isCourseReview>

## Ujian akhir


<chapterId>b99e005e-8dd0-4fa4-b302-f940c27a30ac</chapterId>


<isCourseExam>true</isCourseExam>

## Kesimpulan


<chapterId>3b449814-78f3-41c0-8138-0a04f3682719</chapterId>


<isCourseConclusion>true</isCourseConclusion>