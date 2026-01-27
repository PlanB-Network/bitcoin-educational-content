---
name: 1ML
description: Pelajari cara menggunakan penjelajah 1ML untuk memahami dan menganalisis jaringan Lightning Bitcoin.
---
![cover](assets/cover.webp)



## Pendahuluan



Lightning Network adalah solusi pembayaran cepat dan berbiaya rendah yang dibangun di atas Bitcoin, yang memungkinkan transaksi instan dan aman. Mengamati jaringan ini sangat penting untuk memahami cara kerjanya, topologinya, dan keadaan node yang membentuknya. Lightning explorer, seperti 1ML, digunakan untuk memvisualisasikan data publik jaringan, termasuk node aktif, saluran terbuka, dan kapasitas yang tersedia, memberikan gambaran umum yang berharga bagi pengguna, pengembang, dan operator node.



## Akses 1ML dan pahami halaman beranda



Untuk mengakses 1ML, cukup buka peramban web Anda dan ketik [https://1ml.com](https://1ml.com). Ini akan membawa Anda ke halaman beranda, yang berfungsi sebagai dasbor global Lightning Network.



![capture](assets/fr/03.webp)



Halaman ini menampilkan beberapa statistik penting di bagian atas layar, termasuk :





- Jumlah total node aktif** di jaringan, yaitu komputer yang terlibat dalam pengiriman dan penerimaan pembayaran Lightning.
- Jumlah **saluran terbuka**, yang sesuai dengan koneksi antara node-node yang memungkinkan transfer dana.
- Kapasitas jaringan **total**, dinyatakan dalam bitcoin (BTC), yang menunjukkan jumlah kapasitas semua saluran publik.



Angka-angka ini diperbarui secara berkala untuk mencerminkan kondisi jaringan saat ini. Angka-angka tersebut memberikan gambaran tentang ukuran, pertumbuhan dan ketangguhannya.



![capture](assets/fr/04.webp)



Tepat di bawah, halaman ini menawarkan daftar dengan peringkat:





- Node yang paling banyak terhubung**, yang memiliki saluran paling terbuka ke node lain.
- Kapasitas **tertinggi** pada node, menunjukkan node mana yang dapat mentransfer jumlah terbesar.
- Saluran yang paling penting dalam hal kapasitas.



Filter juga dapat digunakan untuk menyaring daftar ini berdasarkan lokasi geografis atau kriteria lainnya.



Halaman ini merupakan titik awal yang ideal untuk menjelajahi Lightning Network dan memahami topologi umumnya.



![capture](assets/fr/05.webp)



![capture](assets/fr/06.webp)



## Menjelajahi simpul petir



Untuk menjelajahi sebuah node di 1ML, mulailah dengan menggunakan bilah pencarian di bagian atas halaman. Anda dapat memasukkan **Node ID**, yaitu pengenal unik node, atau **alias**, yang merupakan nama yang lebih mudah diingat.



Setelah pencarian selesai, klik pada simpul yang sesuai untuk mengakses halaman detailnya.



![capture](assets/fr/07.webp)



Pada halaman ini, beberapa informasi penting ditampilkan:





- Node ID**: pengenal unik ini adalah serangkaian karakter panjang yang memungkinkan node diidentifikasi secara tepat di seluruh jaringan.



![capture](assets/fr/08.webp)





- Alias**: ini adalah nama yang dipilih oleh pemilik simpul untuk mewakilinya secara publik.



![capture](assets/fr/09.webp)





- Jumlah saluran menunjukkan berapa banyak koneksi yang terbuka pada node tersebut dengan node lainnya, sedangkan kapasitas total menunjukkan jumlah bitcoin yang tersedia pada saluran-saluran tersebut. Sebuah node dengan jumlah saluran yang banyak dan kapasitas yang tinggi biasanya terhubung dengan baik dan mampu mentransfer uang dalam jumlah besar dengan cepat ke seluruh jaringan.



![capture](assets/fr/10.webp)





- Waktu aktif, atau ketersediaan, mengukur berapa lama sebuah node tetap aktif dan dapat diakses secara online, yang mencerminkan keandalannya. Di sisi lain, **umur** node, menunjukkan berapa lama node tersebut telah ada di jaringan, yang mencerminkan stabilitas dan pengalamannya dalam Lightning Network.



![capture](assets/fr/11.webp)



Data ini membantu Anda memahami pentingnya dan keandalan sebuah node di Lightning Network. Sebagai contoh, sebuah node dengan jumlah saluran yang besar, kapasitas tinggi, dan waktu aktif yang tinggi sering kali menjadi pemain utama dalam jaringan.



## Menjelajahi saluran petir



### Apa yang dimaksud dengan saluran Lightning?



Saluran Lightning adalah koneksi langsung antara dua node jaringan. Hal ini memungkinkan kedua node ini untuk bertukar pembayaran instan dan berbiaya rendah tanpa melalui rantai utama Bitcoin untuk setiap transaksi. Saluran adalah fondasi yang membuat Lightning Network cepat dan dapat diskalakan.



### Baca informasi saluran di 1ML



Pada 1ML, setiap saluran memiliki halaman atau lembar deskripsi sendiri yang berisi sejumlah data penting:



Dari halaman simpul, Anda dapat mengakses daftar salurannya. Dengan mengklik sebuah saluran, 1ML menampilkan halaman khusus dengan beberapa informasi penting.



![capture](assets/fr/12.webp)



![capture](assets/fr/13.webp)



Data utama yang terlihat adalah sebagai berikut:





- Node mitra**: setiap saluran menghubungkan dua node. 1ML menampilkan pengenal dan alias masing-masing.



![capture](assets/fr/14.webp)





- Kapasitas saluran**: ini adalah jumlah total bitcoin yang terkunci di saluran ini. Kapasitas ini mewakili batas maksimum pembayaran yang dapat transit melalui saluran ini.



![capture](assets/fr/15.webp)





- Usia saluran**: menunjukkan berapa lama saluran tersebut telah terbuka. Saluran yang lama sering kali merupakan tanda hubungan yang stabil antara dua node.



![capture](assets/fr/16.webp)



### Batas visibilitas saluran



Penting untuk dipahami bahwa 1ML hanya menampilkan **sebagian** dari Lightning Network. Penjelajah hanya menampilkan **saluran publik**, yaitu saluran yang telah diumumkan di jaringan. Saluran privat, yang sering digunakan untuk alasan kerahasiaan atau strategi, tidak terlihat. Selain itu, 1ML tidak menunjukkan distribusi dana yang tepat di setiap sisi saluran, atau pembayaran yang dilakukan, atau likuiditas yang sebenarnya tersedia pada saat tertentu. Oleh karena itu, informasi yang ditampilkan dapat digunakan untuk menganalisis **struktur umum jaringan**, tetapi bukan aktivitas keuangan yang sebenarnya atau status likuiditas yang terperinci.



## Jelajahi Lightning Network berdasarkan lokasi



### Simpul berdasarkan negara dan wilayah



1ML memungkinkan Anda untuk menjelajahi Lightning Network menurut **perincian geografis**. Dari halaman beranda atau melalui bagian khusus, Anda dapat menampilkan node berdasarkan negara atau wilayah. Fitur ini didasarkan pada informasi lokasi yang dinyatakan oleh operator node.


Pada bilah navigasi, Anda akan melihat tautan **Lokasi**. Pada halaman tersebut, node dikelompokkan berdasarkan benua, negara, dan kota.



![capture](assets/fr/17.webp)



Dengan memilih sebuah negara, 1ML menampilkan daftar node yang terkait, bersama dengan statistik agregat seperti jumlah node dan total kapasitas yang terlihat untuk area geografis tersebut.



#### Apa yang dikatakan tentang adopsi lokal





- Adopsi teknologi**: Sejumlah besar node di suatu wilayah menunjukkan bahwa pengguna, perusahaan, atau layanan Bitcoin secara aktif mengadopsi Lightning Network. Hal ini menunjukkan kematangan teknologi dan kemauan untuk memanfaatkan manfaat Lightning (transaksi cepat, biaya lebih rendah).
- Ekosistem ekonomi** : Keberadaan node yang padat juga dapat menandakan tatanan ekonomi lokal di sekitar Bitcoin: pedagang yang menerima Lightning, perusahaan rintisan yang mengembangkan alat, acara komunitas, dll.
- Keamanan dan ketahanan**: Distribusi geografis yang beragam meningkatkan ketahanan jaringan dalam menghadapi pemadaman atau pembatasan lokal. Semakin banyak node yang tersebar, semakin terdesentralisasi dan sulit untuk menyensor jaringan.
- Kebijakan dan peraturan**: Beberapa negara mungkin melihat adopsi yang lebih cepat berkat kerangka kerja peraturan yang mendukung atau komunitas yang proaktif. Sebaliknya, di daerah di mana peraturannya ketat atau tidak bersahabat, jumlah node akan lebih rendah.



#### Batasan data geografis



Namun, perlu diingat bahwa geolokasi node Lightning memiliki keterbatasan dan bias:





- Perkiraan lokasi IP**: 1ML umumnya menggunakan alamat IP publik dari node untuk memperkirakan lokasinya. Namun, metode ini dapat terdistorsi oleh penggunaan VPN, server cloud (AWS, Google Cloud), atau hosting di negara yang berbeda dengan domisili pemilik node yang sebenarnya.
- Node virtual**: Beberapa operator meng-host node mereka di server jarak jauh untuk alasan keandalan dan ketersediaan, yang dapat memberikan kesan lokasi fisik yang salah.
- Mobilitas pengguna**: Operator node dapat mengubah lokasi, memindahkan infrastrukturnya, atau membuka beberapa node di wilayah yang berbeda, sehingga pembacaan data menjadi lebih kompleks.
- Tidak terlihatnya node pribadi**: Beberapa node tidak mempublikasikan alamat IP mereka atau menggunakan metode untuk menyembunyikan lokasi mereka, membuat geolokasi tidak mungkin dilakukan.



## kasus penggunaan beton 1ML



### Memahami topologi jaringan



1ML memungkinkan Anda untuk memvisualisasikan **struktur umum Lightning Network**. Dengan mengamati koneksi antar node, jumlah saluran dan kapasitas keseluruhan, dimungkinkan untuk memahami bagaimana jaringan diorganisir, node mana yang memainkan peran sentral dan bagaimana arus pembayaran secara teoritis dapat beredar.



Pemahaman ini sangat penting jika kita ingin memahami cara kerja Lightning Network, dan tidak hanya untuk penggunaan portofolio.



### Mengidentifikasi simpul-simpul penting



Berkat peringkat yang ditawarkan oleh 1ML (node yang paling terhubung, kapasitas tertinggi, usia), memungkinkan untuk mengidentifikasi node yang menempati tempat penting dalam jaringan. Node-node ini sering kali berfungsi sebagai gerbang utama untuk pembayaran Lightning.



![capture](assets/fr/18.webp)



### Memeriksa visibilitas publik dari sebuah node



Untuk operator node, 1ML memungkinkan Anda untuk memeriksa apakah node Anda diiklankan secara publik di Lightning Network. Jika sebuah node muncul di 1ML, ini berarti node tersebut dapat dilihat dan diakses oleh node lain untuk membuka saluran publik.


Hal ini dapat berguna untuk mendiagnosis masalah visibilitas atau konektivitas.



### Menyaksikan Lightning Network berevolusi dari waktu ke waktu



Dengan membandingkan statistik global selama periode yang berbeda, 1ML memungkinkan kita untuk mengamati evolusi Lightning Network: peningkatan atau penurunan jumlah node, variasi kapasitas total atau perubahan distribusi geografis.


Pengamatan ini menawarkan perspektif yang menarik tentang pertumbuhan, kematangan, dan tren Lightning Network.



## praktik terbaik dan batasan 1ML



### Data publik ≠ realitas yang lengkap



1ML hanya didasarkan pada data **yang diumumkan secara publik** pada Lightning Network. Ini berarti bahwa alat ini hanya menunjukkan sebagian dari kenyataan. Banyak saluran mungkin bersifat pribadi, beberapa node mungkin tidak diiklankan, dan likuiditas aktual yang tersedia di saluran tidak terlihat. Oleh karena itu, penting untuk menggunakan 1ML sebagai alat analisis global, bukan sebagai representasi lengkap dari jaringan.



### Privasi dan Petir



Lightning Network telah dirancang dengan fokus yang kuat pada **privasi pembayaran**. Transaksi individu tidak terlihat di 1ML, dan saldo saluran yang tepat tidak dipublikasikan. Keterbatasan ini bukanlah kesalahan dari penjelajah, tetapi merupakan fitur mendasar dari Lightning Network, yang dirancang untuk melindungi privasi pengguna.



### Jangan langsung mengambil kesimpulan



Sebuah node dengan kapasitas tinggi atau banyak saluran tidak selalu lebih "handal" atau "efisien" dalam semua kasus. Demikian pula, penurunan sementara dalam kapasitas jaringan secara keseluruhan tidak selalu berarti masalah struktural. Angka-angka harus selalu ditafsirkan dengan melihat ke belakang dan dimasukkan ke dalam konteks.



### Saling melengkapi dengan alat lain



1ML adalah titik awal yang sangat baik untuk menjelajahi Lightning Network, tetapi paling baik digunakan bersama dengan alat lain seperti portofolio Lightning, antarmuka manajemen node, dan penjelajah lainnya. Pendekatan ini memberikan pandangan yang lebih lengkap dan bernuansa tentang jaringan.



## opsi koneksi 1ML (fungsionalitas lanjutan)



1ML menawarkan opsi **log-in / membuat akun**, dapat dilihat di situs, tetapi ini **tidak diperlukan** untuk melihat data Lightning Network. Semua fitur yang dibahas sejauh ini dalam tutorial ini tersedia **tanpa akun**.



Koneksi ini ditujukan terutama untuk **operator simpul petir**. Secara khusus, fitur ini memungkinkan sebuah simpul dikaitkan dengan akun 1ML untuk mengelola informasi publik tertentu, seperti presentasi simpul, tautan kontak, dan metadata lainnya. Fitur ini dirancang untuk meningkatkan visibilitas dan identifikasi sebuah node di dalam penjelajah.



Penting untuk dicatat bahwa 1ML **bukan layanan kustodian**. Pembuatan akun tidak memberikan akses ke dana, saluran, atau pembayaran node. Akun ini hanya berfungsi untuk berinteraksi dengan penjelajah dari sudut pandang deklaratif dan informatif.



Dalam konteks mempelajari atau menemukan Lightning Network, opsi ini dapat dianggap sebagai **opsional** dan dicadangkan untuk penggunaan yang lebih lanjut.



## Kesimpulan



1ML adalah alat yang berharga untuk mengamati dan memahami Lightning Network dari data publiknya. Alat ini memungkinkan Anda menjelajahi struktur jaringan, menganalisis node dan saluran, serta melacak evolusi keseluruhan adopsi Lightning Network dari waktu ke waktu. Tanpa memerlukan akun atau penanganan dana, 1ML menawarkan gerbang yang dapat diakses oleh siapa saja yang ingin memperdalam pemahaman mereka tentang cara kerja Lightning.


Jika Anda ingin melangkah lebih jauh dengan Lightning Network, saya merekomendasikan kursus Pengantar Lightning Network yang lengkap:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb