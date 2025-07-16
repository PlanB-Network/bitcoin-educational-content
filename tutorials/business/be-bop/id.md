---
name: be-BOP
description: Panduan praktis untuk memonetisasi bisnis Anda dengan be-BOP
---

![cover-bebop](assets/cover.webp)



**be-BOP** adalah platform e-commerce yang dirancang untuk pengusaha yang ingin berjualan secara online dan offline, dengan otonomi penuh, sambil menerima pembayaran dalam Bitcoin, melalui rekening bank dan Tunai. Solusi ini juga berguna untuk semua jenis organisasi yang ingin mengumpulkan donasi atau memonetisasi berbagai aktivitasnya.



Solusinya sederhana, ringan, dan mandiri. Solusi ini memungkinkan pembuatan toko online, bahkan di lingkungan di mana layanan keuangan tradisional terbatas atau tidak ada. Memang, **be-BOP** telah dirancang untuk beroperasi secara efisien dengan atau tanpa akses ke bank, menggunakan Bitcoin sebagai infrastruktur pembayaran.



Dalam tutorial ini, kami akan memandu Anda langkah demi langkah melalui :





- Buat toko online pertama Anda dengan **be-BOP**
- Personalisasi etalase dan produk Anda
- Mengonfigurasi metode pembayaran yang tersedia
- Pahami praktik terbaik untuk berjualan online secara efektif dengan **be-BOP**



Tutorial ini tidak membutuhkan keterampilan teknis tingkat lanjut. Tutorial ini ditujukan untuk para pengembang serta pengrajin, pedagang, koperasi, atau pengusaha yang ingin memulai perdagangan digital dengan cara yang berdaulat dan tangguh.



## Prasyarat untuk menginstal be-BOP di server Anda sendiri



Sebelum Anda mulai menginstal be-BOP, pastikan Anda memiliki infrastruktur teknis berikut ini. Elements ini sangat penting agar platform dapat berfungsi dengan baik:



### Penyimpanan yang kompatibel dengan S3



be-BOP menggunakan sistem penyimpanan untuk mengelola file (seperti gambar produk). Hal ini memerlukan akses ke layanan S3, seperti file :





- [MinIO] (https://min.io/) dihosting sendiri
- Amazon S3 (AWS)
- Penyimpanan Objek Scaleway



Anda perlu mengonfigurasi bucket dan memberikan informasi berikut:





- S3_BUCKET**: nama bucket
- S3_ENDPOINT_URL**: tautan akses ke layanan S3 Anda
- S3_KEY_ID** dan S3_KEY_SECRET: kode akses Anda
- S3_REGION**: wilayah layanan S3 Anda



### Basis data MongoDB dalam mode ReplicaSet



be-BOP menggunakan MongoDB untuk menyimpan data toko, pengguna, produk, dan data lainnya.



Anda memiliki dua pilihan:





- Instal MongoDB secara lokal dengan mode **ReplicaSet diaktifkan**
- Gunakan layanan online seperti **MongoDB Atlas**



Anda akan membutuhkan variabel-variabel berikut ini:





- MONGODB_URL**: koneksi basis data Address
- MONGODB_DB**: nama database



## Lingkungan Node.js



be-BOP bekerja dengan Node.js. Pastikan Anda memiliki **Node.js** versi 18 atau lebih tinggi dan **Corepack** diaktifkan (diperlukan untuk mengelola manajer paket seperti pnpm). Perintah yang harus dijalankan adalah `corepack enable`



### Git LFS terinstal



Beberapa sumber daya (seperti gambar besar) dikelola melalui Git LFS (Penyimpanan File Besar). Pastikan Anda telah menginstal Git LFS di komputer Anda dengan perintah `git lfs install`. Setelah prasyarat ini tersedia, Anda siap untuk melanjutkan ke langkah berikutnya: mengunduh dan mengonfigurasi be-BOP.



**Catatan:** Panduan teknis untuk penerapan perangkat lunak tersedia dalam tutorial terpisah.



## Membuat akun Super-Admin



Saat pertama kali be-BOP diluncurkan, akun **Super Admin** akan dibuat. Akun ini memiliki semua otorisasi yang diperlukan untuk mengelola fungsi back-office. Untuk membuat akun, ikuti langkah-langkah berikut:





- Buka `yourresiteweb/admin/login`
- Buat akun super-admin dengan login dan kata sandi yang aman



Akun ini akan memberi Anda akses ke semua fungsi back-office. Setelah dibuat, Anda bisa masuk dengan memasukkan nama pengguna dan kata sandi.



![login](assets/fr/001.webp)



## Konfigurasi dan keamanan Back-Office



Sebelum mengonfigurasi koneksi back-office Interface, Anda perlu membuat Hash yang unik. Hal ini memberikan perlindungan terhadap aktor jahat yang mencoba mencuri tautan koneksi ke admin Interface Anda.



Untuk membuat Hash, buka `/admin/Settings`. Pada bagian yang didedikasikan untuk keamanan (misalnya "Admin Hash"), tentukan sebuah string unik (Hash). Setelah terdaftar, URL back-office akan dimodifikasi (misalnya `/admin-yourhash/login`) untuk membatasi akses ke orang yang tidak berwenang.



![hash-login](assets/fr/002.webp)



2.2. Mengaktifkan mode pemeliharaan (jika perlu)



Masih di /admin/Settings, (Settings > General melalui grafik Interface) centang opsi "aktifkan mode pemeliharaan" di bagian bawah halaman.



![maintenance-mode](assets/fr/003.webp)



Jika diperlukan, Anda bisa menentukan daftar alamat IPv4 resmi (dipisahkan dengan koma) untuk memungkinkan akses ke front office selama pemeliharaan. Back office tetap dapat diakses oleh administrator.



![ip-bebop](assets/fr/004.webp)



## Pengaturan komunikasi



Untuk memungkinkan be-BOP mengirim pemberitahuan (misalnya untuk pesanan, pendaftaran atau pesan sistem), Anda perlu mengonfigurasi setidaknya satu metode komunikasi. Tersedia dua pilihan: email (SMTP) atau Nostr.



### Konfigurasi SMTP (email)



be-BOP dapat mengirim email melalui server SMTP. Anda akan membutuhkan kredensial SMTP yang valid, yang biasanya disediakan oleh layanan email (misalnya Mailgun, Gmail, dll.).



Inilah yang perlu Anda ketahui:



SMTP_HOST: Server SMTP Address (mis. smtp.mailgun.org)



SMTP_PORT: port yang akan digunakan (biasanya 587 atau 465)



SMTP_USER: nama pengguna Anda (biasanya email Address)



SMTP_PASSWORD: kata sandi atau kunci API Anda



SMTP_FROM: email Address yang akan muncul sebagai pengirim




### Konfigurasi Nostr



be-BOP memungkinkan Anda untuk mengirim pemberitahuan melalui protokol Nostr, sebuah infrastruktur pengiriman pesan yang terdesentralisasi. Untuk melakukan ini, Anda perlu melakukan generate atau Supply kunci privat Nostr (NSEC). Anda dapat generate kunci ini secara langsung melalui Interface be-BOP, pada bagian yang didedikasikan untuk Nostr. Ketika Elements ini dikonfigurasi dengan benar, be-BOP akan dapat secara otomatis mengirim pesan dan peringatan kepada pengguna Anda.



## Metode pembayaran yang kompatibel



be-BOP kompatibel dengan beberapa solusi pembayaran, sehingga Anda dapat menawarkan fleksibilitas yang lebih besar kepada pelanggan. Inilah yang Anda perlukan untuk mengatur metode pembayaran yang paling sesuai untuk Anda.



### Bitcoin Onchain



be-BOP memungkinkan Anda menerima pembayaran Bitcoin secara langsung pada Blockchain (On-Chain), secara sederhana dan aman.



**Langkah-langkah konfigurasi:**





- Buka menu **Pengaturan Pembayaran**
- Klik **Bitcoin Nodeless** untuk mengakses parameter pembayaran On-Chain.
- Lengkapi kolom-kolom berikut ini:



| Champ                  | Description                                               | Exemple à utiliser                              |
|------------------------|-----------------------------------------------------------|--------------------------------------------------|
| **BIP Standard**       | Le type d’adressage utilisé                               | BIP84 (pour les adresses au format bech32 commençant par `bc1`) |
| **Clé publique étendue** | Votre Zpub (ou Xpub selon le portefeuille utilisé)        | `zpub...` (extrait de votre portefeuille Bitcoin) |
| **Derivation Index**   | L’index de départ pour la génération des adresses         | `1`                                              |
| **Mempool URL**        | L’URL du service mempool utilisé pour suivre les transactions | `https://mempool.space`                         |

![payment-nodeless](assets/fr/005.webp)



**Tip:** Untuk mendapatkan kunci publik yang diperluas (Zpub), Anda dapat melihat pengaturan lanjutan Bitcoin Wallet Anda (Sparrow wallet, BlueWallet, Spectre, dll.). Pastikan Wallet Anda **bukan hanya-baca** jika Anda ingin menggunakan riwayat transaksi.



### Lightning Network



be-BOP juga dapat menerima pembayaran Bitcoin instan berkat Lightning Network. Saat ini tersedia dua opsi konfigurasi:



** Phoenixd**



Buka menu `Pengaturan Pembayaran`, klik `Phoenixd`



![phoenixd](assets/fr/006.webp)



Anda kemudian harus memasukkan kata sandi atau autentikasi token** yang menghubungkan Anda ke instance Phoenixd Anda, sebuah backend yang dikembangkan oleh Acinq yang memungkinkan Anda mengelola pembayaran Lightning dengan node Anda sendiri, tetapi tanpa kerumitan dalam mengelola saluran pembayaran.



**Swiss Bitcoin Pay**



Jika Anda tidak ingin mengelola node Lightning sendiri, **Swiss Bitcoin Pay** adalah solusi siap pakai dan mudah dikonfigurasi yang ideal untuk mulai menerima pembayaran Lightning tanpa infrastruktur yang rumit.



Langkah-langkah konfigurasi :





- Di menu "Pengaturan Pembayaran", klik `Swiss Bitcoin Pay`
- Masuk ke akun Swiss Bitcoin Pay Anda (atau buat akun baru jika Anda belum memilikinya).
- Masukkan Kunci API yang disediakan oleh Swiss Bitcoin Pay, lalu klik "Simpan"



Setelah diatur, be-BOP akan secara otomatis membuat faktur generate Lightning untuk pelanggan Anda, dan Anda akan menerima pembayaran langsung ke akun Swiss Bitcoin Pay Anda. Solusi ini ideal bagi pengguna yang ingin menghindari kerumitan teknis dari simpul pribadi sekaligus menerima pembayaran yang cepat dan murah.



![swissbtcpay](assets/fr/007.webp)



### PayPal



Selain Bitcoin, be-BOP juga memungkinkan Anda menerima pembayaran tunai melalui PayPal, sebuah solusi internasional yang terkenal dan banyak digunakan.



Langkah-langkah konfigurasi :





- Masuk ke menu `Pengaturan Pembayaran`
- Klik `PayPal
- Di akun Paypal Anda (bagian pengembang), masukkan `ID Klien` dan `Rahasia`
- Pilih mata uang pilihan Anda (misalnya **USD**, **EUR**, **XOF**, dll.)
- Klik `simpan



![paypal](assets/fr/008.webp)



**Catatan:** Anda harus memiliki rekening bisnis PayPal untuk mendapatkan pengenal ini. Anda dapat memperolehnya melalui portal [pengembang] (https://developer.paypal.com)



### Rangkuman



Perangkat lunak ini sekarang mengintegrasikan solusi pembayaran **SumUp**, sehingga Anda dapat menerima pembayaran kartu kredit dengan mudah, aman dan efisien. Untuk mendapatkan manfaat dari fungsi ini, diperlukan konfigurasi awal. Berikut ini adalah langkah-langkah yang harus diikuti, yang diberi nomor untuk implementasi yang jelas dan progresif:





- Mulailah dengan memasukkan **API Key** Anda, sebuah kunci rahasia yang diberikan oleh SumUp ketika Anda membuat akun pengembang. Kunci ini akan membuat koneksi yang aman antara akun SumUp Anda dan perangkat lunak.
- Isi kolom `Kode Pedagang` dengan kode unik yang mengidentifikasi bisnis Anda dalam platform SumUp. Kode ini penting untuk mengaitkan transaksi dengan bisnis Anda.
- Pada kolom `Mata Uang`, pilih mata uang utama yang Anda gunakan untuk transaksi (misalnya **EUR**, **USD**, **CDF**, dsb.).
- Setelah semua kolom diisi dengan benar, klik tombol `Save` untuk menyimpan pengaturan Anda. Sistem kemudian akan membuat tautan dengan akun SumUp Anda, dan perangkat lunak Anda akan siap menerima pembayaran.



![payment-sumup](assets/fr/009.webp)



Setelah konfigurasi ini, integrasi **SumUp** akan aktif dan beroperasi, sehingga Anda dapat dengan cepat mencairkan dan melacak transaksi Anda langsung dari perangkat lunak.



### Stripe



be-BOP juga menawarkan integrasi penuh dengan **Stripe**, salah satu platform pembayaran online yang paling populer. Stripe memungkinkan Anda untuk menerima pembayaran online melalui kartu kredit, Wallet digital, dan beberapa metode pembayaran lainnya. Berikut ini cara mengaktifkannya:





- Masukkan **kunci rahasia** yang disediakan di dasbor Stripe.
- Lengkapi kolom **Kunci Publik**, yang juga disediakan oleh Stripe.
- Pilih **mata uang utama**.
- Simpan konfigurasi, lalu klik `Save`.



![payment-stripe](assets/fr/010.webp)



⚠️ **Harap diperhatikan:** Penting untuk mengetahui rezim PPN yang berlaku untuk aktivitas Anda (mis.: penjualan dengan PPN di negara penjual, pembebasan berdasarkan justifikasi, atau penjualan dengan tarif PPN di negara pembeli) agar dapat mengonfigurasi opsi faktur dengan benar di **be-BOP**.



## Konfigurasi mata uang



**be-BOP** menawarkan manajemen mata uang tingkat lanjut dan disesuaikan dengan lingkungan multi-mata uang dan persyaratan akuntansi yang spesifik. Untuk memastikan konsistensi dalam operasi dan pelaporan keuangan, sangat penting untuk mengonfigurasi mata uang yang berbeda yang digunakan dalam sistem dengan benar. Berikut adalah langkah-langkah yang harus diikuti untuk konfigurasi ini:





- Pilih **mata uang utama** (`Mata uang utama`)
- Pilih `Mata uang sekunder
- Tentukan **mata uang referensi** (`Mata uang referensi harga`)
- Tunjukkan `Mata uang akuntansi



Setelah semua mata uang dikonfigurasikan dengan benar, perangkat lunak ini memastikan konversi otomatis dan akurat untuk transaksi multi-mata uang, dengan tetap menjaga konsistensi akuntansi yang ketat.



![settings-currencies](assets/fr/011.webp)



## Konfigurasi akses pemulihan melalui email atau Nostr



Masih di `/admin/settings`, melalui modul **ARM**, pastikan bahwa akun super-admin menyertakan **email Address** atau **recovery pub**, sehingga memudahkan prosedur jika Anda lupa kata sandi.



![settings-users](assets/fr/012.webp)



## Pengaturan bahasa



Perangkat lunak ini menawarkan kemampuan multibahasa untuk beradaptasi dengan audiens internasional dan meningkatkan pengalaman pengguna. Untuk mengaktifkan fungsionalitas multibahasa, penting untuk mengonfigurasi bahasa yang tersedia dan menentukan **bahasa default**.



![settings-languages](assets/fr/13.webp)



## Interface dan konfigurasi Identitas di be-BOP



**be-BOP** menyediakan semua peralatan yang dibutuhkan oleh para desainer untuk mendesain situs web. Langkah pertama adalah membuka bagian `/Admin > Merch > Layout` dalam pengaturan. Mulailah dengan mengonfigurasi **Top Bar**, **Navbar** dan **Footer**.



### Le Top Bar



Konfigurasi **Top Bar** memungkinkan Anda mempersonalisasi identitas visual perangkat lunak Anda dengan menampilkan informasi utama langsung dari baris pertama Interface. Hal ini memperkuat pengenalan merek dan memberikan konteks yang jelas bagi pengguna.



#### Langkah-langkah konfigurasi :





- Pada bidang `Nama merek`, masukkan nama perusahaan, organisasi, atau produk Anda. Nama ini akan muncul di bagian atas Interface dan akan mewakili identitas visual utama Anda.
- Tunjukkan judul situs web**: judul yang dipilih harus meringkas tujuan platform. Judul ini dapat muncul di header atau di tab browser.
- Tambahkan deskripsi situs web**: ini adalah tempat Anda memasukkan deskripsi singkat tentang inisiatif Anda. Deskripsi ini membantu mengontekstualisasikan alat ini bagi pengguna dan juga dapat digunakan untuk tujuan SEO.



Setelah informasi ini dimasukkan, **Top Bar** akan menampilkan presentasi yang jelas, profesional, dan koheren tentang solusi Anda.



#### Tautan di Bilah Atas



Bagian `Tautan` pada Bilah Atas memungkinkan Anda menambahkan pintasan ke halaman penting dalam aplikasi atau situs eksternal. Tautan ini ditampilkan secara langsung di Bilah Atas, menawarkan akses cepat dan terstruktur kepada pengguna Anda.



#### Langkah-langkah konfigurasi :





- Masukkan nama tautan (Teks)**: pada bidang `Teks`, masukkan nama atau label tautan yang akan ditampilkan (misalnya Beranda, Kontak, Bantuan...).
- Tunjukkan tautan Address (Url)**: di bidang `Url`, masukkan Address lengkap dari halaman target (internal atau eksternal).
- Tambahkan tautan lain jika perlu**: setiap baris konfigurasi memungkinkan Anda menambahkan tautan tambahan menggunakan bidang `Text` dan `Url`.
- Simpan tautan**: setelah semua tautan dimasukkan, klik tombol "Tambahkan tautan bilah atas" untuk menyimpannya.



Konfigurasi ini memungkinkan Anda untuk menawarkan navigasi yang jelas, lancar dan mudah diakses melalui berbagai bagian situs web Anda atau ke sumber daya pelengkap.



![settings-topbar](assets/fr/014.webp)



### La Nav Bar



Bagian **Navbar** memungkinkan Anda mengonfigurasi menu navigasi utama be-BOP Anda, biasanya terletak di samping atau atas Interface. Menu ini memandu pengguna ke berbagai halaman dan fungsi aplikasi. Konfigurasi tautan sederhana dan intuitif. Inilah cara kerjanya:





- Masukkan nama tautan (`Teks`)**: pada baris konfigurasi, mulai dengan mengisi bidang `Teks`. Ini sesuai dengan nama tautan yang ditampilkan pada bilah navigasi (contoh: *Dashboard*, *Pengguna*, *Pengaturan*...).
- Masukkan tautan Address (`Url`)**: di samping bidang `Teks`, Anda akan menemukan bidang `Url`. Di bidang ini, masukkan Address halaman yang akan dialihkan oleh tautan. Ini bisa berupa rute internal atau tautan ke halaman eksternal.
- Tambahkan beberapa tautan jika diperlukan**: di bawah baris pertama, bidang `Teks` dan `Url` baru tersedia untuk menambahkan sebanyak mungkin tautan yang diperlukan. Setiap baris mewakili tautan navigasi tambahan.
- Simpan tautan**: setelah Anda memasukkan semua Elements, klik tombol `Tambahkan tautan bilah navigasi` untuk menyimpan dan menampilkan hasilnya di bilah navigasi.



Konfigurasi ini memungkinkan penataan akses yang efisien ke berbagai bagian perangkat lunak, meningkatkan ergonomi dan pengalaman pengguna.



![navbar](assets/fr/015.webp)



### Footer



Bagian **Footer** memungkinkan Anda menyesuaikan footer perangkat lunak Anda, menambahkan informasi atau tautan yang berguna. Sebelum mengonfigurasi tautan, mulailah dengan mengaktifkan opsi tertentu:





- Mengaktifkan tampilan label "Didukung oleh be-BOP "**: aktifkan tombol `Display Powered by be-BOP` untuk menampilkan label ini di bagian footer.
- Masukkan nama tautan (`Teks`)**: isi bidang `Teks`, yang sesuai dengan kata-kata tautan di footer (contoh: *Terms*, *Privasi*, *Kontak*...).
- Tunjukkan tautan Address (`Url`)**: di bidang `Url`, masukkan Address halaman target (internal atau eksternal).
- Tambahkan lebih banyak tautan jika diperlukan**: gunakan baris tambahan untuk membuat sebanyak mungkin tautan yang Anda inginkan.
- Simpan tautan**: klik tombol "Tambahkan tautan footer" untuk menyimpan tautan.



![footer](assets/fr/016.webp)



### Personalisasi visual



**⚠️ Jangan lupa untuk mengatur logo untuk tema terang dan gelap, serta favicon, melalui** `Admin > Merch > Pictures`.



Berikut ini adalah cara menyesuaikan tampilan dan nuansa situs Anda:



#### Buka bagian Gambar



Menu `Admin` > `Merch` > `Gambar`.



#### Menambahkan gambar baru



Klik pada `Gambar Baru`.



#### Pilih file lokal



Klik `Pilih File`, lalu pilih gambar dari disk Hard Anda.



#### Pilih file yang akan diimpor



Klik dua kali pada gambar yang akan diimpor (logo terang, logo gelap, atau favicon).



#### Penamaan gambar



Isi bidang `Nama gambar`.



#### Tambahkan gambar



Klik `Tambah` untuk menyelesaikan impor.



![pictures](assets/fr/017.webp)



### Pengaturan Identitas Penjual



#### Pengaturan identitas



Dapat diakses melalui `Admin > Identitas` (atau `Pengaturan > Identitas`), bagian ini memungkinkan Anda untuk mengonfigurasi informasi administratif dan hukum perusahaan Anda.



#### Informasi hukum





- Nama bisnis**: nama resmi perusahaan.
- ID Bisnis**: pengenal resmi atau nomor registrasi (RCCM, SIRET...).



#### Bisnis Address





- Jalan**: pos Address (jalan, nomor...).
- Negara**: negara.
- Negara bagian**: provinsi atau wilayah.
- Kota**: kota.
- Kode pos**: kode pos.



#### Informasi kontak





- Email**: email profesional Address.
- Telepon**: nomor telepon perusahaan.



#### Rekening bank





- Nama pemegang rekening**: nama pemegang rekening.
- Pemegang rekening Address**: Address milik pemegang rekening.
- IBAN**: Nomor Rekening Bank Internasional.
- BIC**: Kode SWIFT/BIC.



![bank-account](assets/fr/019.webp)



#### Penagihan





- Klik `Isi dengan informasi toko utama` untuk mengisi data.
- Informasi penerbit paling kanan atas**: kolom untuk informasi hukum/pajak yang terlihat pada faktur.
- Klik `Update` untuk menyimpan perubahan.



**Catatan:** Anda juga dapat memasukkan informasi tambahan untuk ditampilkan pada Invoice, sesuai dengan kebutuhan Anda.



![vat](assets/fr/019.webp)



![issuer-info](assets/fr/020.webp)



#### Toko fisik Address



Bagi mereka yang memiliki toko fisik, tambahkan Address lengkap secara spesifik di `Admin > Pengaturan > Identitas` atau bagian khusus. Hal ini akan memungkinkannya untuk ditampilkan pada dokumen resmi dan di catatan kaki jika perlu.



![seller-id](assets/fr/021.webp)



## Manajemen Produk



### Menciptakan produk baru



Buka `Admin > Merch > Produk` untuk menambah atau mengubah produk. Isi kolom berikut ini:



#### Informasi dasar





- Nama Produk**: nama produk (contoh: *Kaos BOP edisi terbatas*).
- Siput**: Pengenal URL tanpa spasi (misalnya `tshirt-bop-edition-limitee`).
- Alias** *(opsional)*: berguna untuk penambahan cepat ke keranjang melalui bidang khusus.



![product-config](assets/fr/028.webp)



#### Harga





- Jumlah Harga**: harga produk (mis. `25.00`).
- Mata Uang Harga**: mata uang (EUR, USD, BTC, dll.).
- Produk khusus **:
  - ini adalah produk gratis.
  - ini adalah produk bayar sesuai keinginan Anda.



#### Pilihan produk





- Produk tunggal (`standalone`)**: hanya satu tambahan yang dapat dilakukan per pesanan (mis. donasi, tiket masuk).
- Produk dengan variasi**:
  - Jangan centang `Standalone`.
  - Centang `Produk memiliki variasi ringan (tidak ada perbedaan stok)`.
  - Menambahkan :
    - Nama** (mis. *Ukuran*),
    - Nilai** (contoh: S, M, L, XL),
    - Perbedaan harga** jika ada (contoh: `+2 USD` untuk XL).



![product-details](assets/fr/029.webp)



## Manajemen stok



### Opsi lanjutan saat membuat produk (Stok, Pengiriman, Tiket, dll.)



#### Produk dengan stok terbatas



Jika produk Anda tidak tersedia dalam jumlah yang tidak terbatas, centang `Produk memiliki stok terbatas`. Ini akan mengaktifkan pelacakan otomatis untuk jumlah yang tersisa. Setelah kotak ini dicentang, sebuah kolom akan muncul untuk menunjukkan **stok yang tersedia**.



Sistem mengelola :





- Stok yang dipesan** → produk dalam keranjang yang belum dibayar
- Stok terjual** → produk yang sudah dibeli



**Waktu pemesanan keranjang**: Ketika pelanggan menambahkan produk ke keranjangnya, produk tersebut "dipesan" untuk waktu yang terbatas. Anda dapat mengubah waktu ini di: `Admin > Konfigurasi > Reservasi keranjang` (nilai dalam menit)



#### Produk yang akan dikirim?



Centang `Produk memiliki komponen fisik yang akan dikirim ke Address pelanggan`. Ini berguna untuk semua produk yang akan dikirim secara fisik (buku, kaos, dll.)



#### Opsi lainnya





- Tiket**: centang jika produk tersebut adalah tiket untuk suatu acara
- Pemesanan**: periksa apakah ini adalah slot reservasi (mis.: sesi, janji temu)



![product-options](assets/fr/030.webp)



### Pengaturan Tindakan (bawah)



Bagian ini menentukan **di mana** dan **bagaimana** produk dapat dilihat dan dibeli:



| Plateforme        | Produit visible | Ajoutable au panier |
|-------------------|------------------|----------------------|
| Eshop (site public)        | ✔️              | ✔️                  |
| Retail POS (point de vente)| ✔️              | ✔️                  |
| Google Shopping            | ✔️              | ✔️                  |
| Nostr-bot (vente via bot)  | ✔️              | ✔️                  |

Centang hanya saluran yang ingin Anda gunakan.



## Pembuatan dan penyesuaian halaman dan widget CMS



### Halaman CMS wajib



Buka `Admin > Merch > CMS`. Anda akan melihat daftar halaman yang sudah ada dan dapat menambahkan halaman baru dengan **Tambahkan halaman CMS**.



Halaman CMS penting untuk :





- Informasikan kepada pengunjung Anda (misalnya ketentuan penggunaan)
- Mematuhi hukum (misalnya kebijakan privasi)
- Jelaskan fitur toko tertentu (mis. pengumpulan IP, PPN 0%)



Anda dapat menambahkan halaman lain sesuai kebutuhan:





- Tentang kami / Siapa kami
- Dukung kami / Donasi
- PERTANYAAN YANG SERING DIAJUKAN
- Kontak
- dll.



**Tip: Klik setiap tautan atau ikon untuk mengubah **konten**, **judul**, atau **kemunculan SEO** dari setiap halaman.



### Tata letak dan grafik Elements



Pergi ke : `Admin > Merch > Tata Letak`. Anda dapat menyesuaikan visual Elements situs Anda:



![product-options](assets/fr/032.webp)



#### Bilah Atas





- Mengubah atau menghapus tautan (misal: HOME, TENTANG KAMI,...)
- Navigasi di antara bagian utama situs



#### Navbar (bilah navigasi utama)





- Hadir di area abu-abu di bawah bilah atas
- Berisi akses cepat ke : `Konfigurasi`, `Pengaturan Pembayaran`, `Transaksi`, `Manajemen Simpul`, `Widget`, dll.
- Hanya untuk direksi



#### Footer





- Dapat diedit dari `Admin > Merch > Tata Letak`
- Berisi: informasi kontak, tautan berguna, pemberitahuan hukum ...



#### Menyesuaikan visual



Pergi ke: `Admin > Merch > Gambar`



Anda bisa :





- Mengubah **logo utama**
- Memodifikasi atau menambahkan tata letak **gambar**



#### Deskripsi situs



Juga dapat dimodifikasi di `Pictures`, ini memungkinkan Anda untuk menampilkan **ringkasan atau slogan** di header atau footer, tergantung pada temanya.



**Catatan:** Hal ini memungkinkan Anda untuk menyesuaikan tampilan dengan identitas merek Anda (pendidikan, komersial atau komunitas).



### Mengintegrasikan widget ke dalam halaman CMS



Widget** memperkaya halaman CMS Anda dengan Elements yang dinamis atau visual.



#### Pembuatan widget



Pergi ke: `Admin > Widget`



Contoh widget yang tersedia:





- Tantangan**: tantangan atau misi
- Tag**: kategori atau kata kunci
- Penggeser**: korsel gambar
- Spesifikasi **: Tabel spesifikasi
- Formulir**: formulir (kontak, umpan balik, dll.)
- Hitung Mundur**: pengatur waktu
- Galeri**: galeri gambar
- Papan Peringkat**: peringkat pengguna



![widgets](assets/fr/033.webp)



#### Integrasi ke halaman CMS



Gunakan **kode pendek** dalam konten halaman CMS Anda:



| Objectif                 | Balise à insérer                      |
|--------------------------|---------------------------------------|
| Afficher un produit      | `[Product=slug?display=img-1]`        |
| Afficher une image       | `[Picture=slug width=100 height=100 fit=contain]` |
| Intégrer un slider       | `[Slider=slug?autoplay=3000]`         |
| Ajouter un challenge     | `[Challenge=slug]`                    |
| Ajouter un compte à rebours | `[Countdown=slug]`                 |
| Intégrer un formulaire   | `[Form=slug]`                         |

**Parameter saat ini** :





- `slug`: pengenal widget yang unik
- `display=img-1`: gambar khusus produk
- `lebar`, `tinggi`, `cocok`: dimensi dan gaya gambar
- autoplay=3000`: waktu dalam ms antara dua slide



**Keuntungan**:





- Mudah disisipkan (salin dan tempel)
- Dinamis: modifikasi apa pun pada widget secara otomatis tercermin
- Tidak diperlukan pengembang



## Manajemen dan pelaporan pesanan



### Pelacakan pesanan



Untuk melihat dan mengelola pesanan sebelumnya, buka: `Admin > Transaksi > Pesanan`



Di sini Anda akan menemukan **daftar lengkap pesanan** yang ditempatkan di situs Anda.



![orders](assets/fr/034.webp)



#### Visualisasi dan pencarian



Interface memungkinkan Anda untuk mencari dan memfilter pesanan menurut beberapa kriteria:





- nomor pesanan: nomor pesanan
- alias produk: pengenal atau nama produk
- cara pembayaran": metode pembayaran yang digunakan (kartu, kripto, dll.)
- `Email`: email pelanggan



Filter ini memfasilitasi pencarian cepat dan manajemen yang ditargetkan.



#### Rincian setiap pesanan



Dengan mengklik pesanan, Anda dapat mengakses file lengkap yang berisi file :





- Produk yang dipesan
- Informasi pelanggan
- Pengiriman Address (jika ada)
- Catatan apa pun yang terkait dengan pesanan



#### Tindakan yang mungkin dilakukan pada pesanan



Anda bisa :





- Konfirmasi pesanan (jika tertunda)
- Membatalkan pesanan (jika terjadi masalah atau permintaan pelanggan)
- Tambahkan **label** (untuk organisasi internal)
- Konsultasikan / tambahkan **catatan internal**



**Catatan:** Bagian ini sangat penting untuk logistik dan hubungan pelanggan yang baik.



### Pelaporan dan ekspor



Untuk mengakses statistik penjualan dan pembayaran :


administrator > Pengaturan > Pelaporan



![reporting](assets/fr/035.webp)



Di sini Anda akan menemukan gambaran umum bisnis Anda, dalam bentuk **laporan bulanan dan tahunan**.



#### Isi laporan



Laporan-laporan tersebut dibagi menjadi beberapa bagian:





- Detail Pesanan**: jumlah pesanan, status (dikonfirmasi, dibatalkan, tertunda), evolusi
- Detail Produk**: produk yang dijual, jumlah, produk populer
- Detail Pembayaran**: jumlah yang terkumpul, rincian berdasarkan metode pembayaran



#### Ekspor data



Tiap bagian menyertakan tombol **Export CSV**, yang memungkinkan Anda untuk :





- Unduh data dalam format CSV
- Buka di Excel, Google Spreadsheet, dll.
- Pengarsipan untuk penggunaan administrasi atau akuntansi
- Menggunakannya untuk laporan internal



**Catatan:** ideal untuk pelacakan kinerja, akuntansi, dan presentasi.



## Konfigurasi Pesan Nostr (opsional)



![nostr-config](assets/fr/036.webp)



Platform ini mendukung protokol **Nostr** untuk fungsi-fungsi canggih tertentu:





- Pemberitahuan terdesentralisasi
- Masuk tanpa kata sandi
- Pemberian cahaya Interface



### Membuat dan menambahkan kunci pribadi Nostr



Pergi ke :


admin > Manajemen Simpul > Nostr





- Klik **Buat nsec** jika Anda tidak memilikinya.
- Sistem ini dapat melakukan generate secara otomatis.
- Sebagai alternatif, Anda dapat menggunakan kunci yang sudah ada (misalnya dari Damus atau Amethyst).



Berikutnya:





- Salin kunci `nsec`
- Tambahkan ke file `.env.local` (atau `.env`) Anda: ```env NOSTR_PRIVATE_KEY = YourNsecIciKey



### Fitur yang diaktifkan dengan Nostr



Setelah dikonfigurasi, beberapa fungsi tersedia:



**Pemberitahuan melalui Nostr**





- Mengirim peringatan untuk pesanan, pembayaran, atau peristiwa sistem
- Untuk administrator atau pengguna



*pemberian cahaya *Interface**





- Dapat diakses melalui klien Nostr
- Memungkinkan manajemen yang cepat dan ramah seluler



**Koneksi tanpa kata sandi**





- Masuk dengan tautan aman (dikirim melalui Nostr)
- Keamanan dan kelancaran pengguna yang lebih baik



## Kustomisasi desain dan tema



Untuk menyesuaikan tampilan toko Anda dengan piagam grafis Anda, buka: `Admin > Merch > Tema`



Di sini Anda akan menemukan semua opsi untuk **membuat** dan **mengkonfigurasi** tema khusus.



### Membuat tema



![theme](assets/fr/037.webp)



Ketika membuat atau memodifikasi tema, Anda dapat menentukan file :





- Warna**: untuk tombol, latar belakang, teks, tautan, dll.
- Font**: pilihan jenis huruf untuk judul, paragraf, menu
- Gaya grafis**: batas, margin, spasi, bentuk blok



### Bagian yang dapat disesuaikan



Setiap bagian dari situs ini dapat disesuaikan secara independen:





- Header**: bilah navigasi atas
- Tubuh**: konten utama
- Footer**: bagian bawah halaman



**Catatan:** Perincian ini memastikan konsistensi antara visual situs dan identitas merek Anda.



### Aktivasi tema



Setelah tema dikonfigurasi :





- Klik **Simpan**
- Aktifkan sebagai **tema utama** toko



**Catatan:** tema aktif adalah tema yang akan terlihat oleh pengunjung.



## Mengonfigurasi templat email



Platform ini memungkinkan Anda mempersonalisasi email yang dikirim secara otomatis ke pengguna. Pergi ke: `Admin > Pengaturan > Templat`



![emails-templates](assets/fr/038.webp)



### Membuat / mengedit templat



Setiap email (konfirmasi pesanan, kata sandi yang terlupa, dll.) memiliki :





- Subjek**: subjek email (misalnya "Pesanan Anda telah divalidasi")
- Badan HTML**: Konten HTML yang ditampilkan dalam email



**Catatan:** Anda bisa menyisipkan teks, gambar, tautan, dll., sesuai kebutuhan.



### Menggunakan variabel dinamis



Untuk membuat email dinamis, sisipkan variabel seperti :





- `{orderNumber}}` : diganti dengan nomor pesanan yang sebenarnya
- `{invoiceLink}}` : tautan ke Invoice
- `{websiteLink}}`: URL situs web Anda



**Catatan:** tag ini secara otomatis diganti ketika dikirim.



### Kiat tingkat lanjut





- Buat email yang **responsif** agar mudah dibaca di perangkat seluler
- Menambahkan **tombol tindakan** (bayar, unduh, lacak pesanan)
- Uji email Anda dengan mengirimkannya ke diri Anda sendiri sebelum dipublikasikan



## Mengonfigurasi tag dan widget tertentu



### Manajemen tag



Tag dapat digunakan untuk menyusun dan memperkaya konten Anda. Untuk mengaksesnya: `Admin > Widget > Tag`



![tags-config](assets/fr/039.webp)



### Membuat tag



Lengkapi kolom-kolom berikut ini:





- Nama Tag**: nama tag yang ditampilkan
- Siput**: pengenal unik (tanpa spasi atau aksen)
- Tag Family**: mengelompokkan tag berdasarkan kategori



![targsconfig](assets/fr/040.webp)



#### Keluarga yang tersedia :





- pencipta`: penulis atau produser
- pengecer: tenaga penjualan atau tempat penjualan
- `Temporal`: periode atau tanggal
- acara: acara terkait



### Bidang opsional



Bidang-bidang ini dapat digunakan untuk memperkaya tag seolah-olah itu adalah halaman konten:





- Judul
- Subtitle
- Konten pendek**
- Konten lengkap** (dalam bahasa Prancis)
- CTA** (tombol tindakan)



### Menggunakan tag



Tag dapat berupa :





- Dialokasikan ke produk
- Diintegrasikan ke dalam halaman CMS dengan sebuah tag: [Tag = siput? display = var-1]



## Konfigurasi file yang dapat diunduh



Untuk menawarkan dokumen yang dapat diunduh kepada pelanggan Anda: `Admin > Merch > File`



### Menambahkan file



1. Klik **File baru**


2. Menginformasikan :




   - Nama file** (mis. *Panduan instalasi*)
   - File untuk diunggah** (PDF, gambar, Word...)



**Catatan:** setelah ditambahkan, platform secara otomatis menghasilkan **tautan permanen**.



### Menggunakan tautan



Tautan ini kemudian dapat disisipkan ke dalam file :





- Halaman CMS** (sebagai tautan teks atau tombol)
- Klien **email** (melalui templat)
- Lembar produk** (mis. unduhan manual)



Sangat ideal untuk menyediakan *panduan pengguna, panduan teknis, lembar produk...* tanpa perlu hosting eksternal.



## Nostr-bot



Platform ini menawarkan integrasi tingkat lanjut dengan protokol **Nostr**, melalui bot otomatis.



Buka: Manajemen simpul > Nostr



### Fitur utama



#### Manajemen relai





- Menambah atau menghapus **relay** yang digunakan oleh bot
- Mengoptimalkan **jangkauan** dan **keandalan** pesan terkirim



#### Pesan perkenalan otomatis





- Mengaktifkan pesan otomatis pada **interaksi pengguna pertama**
- Ideal untuk :
  - Mempresentasikan layanan Anda
  - Kirim tautan yang berguna (misalnya FAQ, kontak, pesanan)



#### Sertifikasi `npub Anda





- Tambahkan **logo** dan **nama publik**
- Tautan ke **domain web yang telah diverifikasi**
- Meningkatkan kredibilitas dan pengakuan identitas Nostr Anda



### Kasus penggunaan Nostr-bot





- Mengirimkan **konfirmasi pesanan** kepada Anda
- Tanggapan otomatis terhadap **peristiwa (misalnya pesanan baru)**
- Menciptakan **interaksi pelanggan yang terdesentralisasi**



## Membebani label terjemahan secara berlebihan



be-BOP multibahasa (FR, EN, ES...), tetapi Anda dapat menyesuaikan terjemahan dengan kebutuhan Anda.



Untuk melakukan ini, buka: `Pengaturan > Bahasa`



### Memuat dan mengedit



File terjemahan dalam bentuk JSON. Anda dapat :





- Unduh** file bahasa
- Memodifikasi** teks yang ada
- Tambahkan** terjemahan Anda sendiri



Tautan ke file asli :


[https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations](https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations)



**Contoh:** mengganti `Tambahkan ke keranjang` dengan `Ajouter au panier` atau `Acheter`.



## Kerja Sama Tim & Mesin Kasir (POS)



### Manajemen pengguna dan hak akses



#### Menciptakan peran



Pergi ke: `Admin > Pengaturan > ARM`



Klik **Buat peran** untuk membuat peran (misalnya `Super Admin`, `POS`, `Pemeriksa tiket`).



Setiap peran berisi :





- akses tulis**: akses tulis
- akses baca**: akses baca
- akses terlarang**: bagian interdites



#### Pembuatan pengguna



Dalam menu yang sama `Admin > Settings > ARM`, tambahkan pengguna dengan nama :





- masuk
- alias
- pemulihan email
- (opsional) `recovery npub` untuk koneksi melalui Nostr



Menetapkan peran yang telah ditentukan sebelumnya.



![pos-users](assets/fr/045.webp)



Pengguna hanya-baca** akan melihat menu dalam *italic* dan tidak dapat mengubah konten.



## Konfigurasi Point of Sale (POS)



### Menetapkan peran POS



Untuk memberi pengguna akses ke POS, tetapkan peran `Point of Sale (POS)` di `Admin > Konfigurasi > ARM`



Dia dapat terhubung melalui URL yang aman: `/pos` atau `/pos/touch`



### Fitur khusus POS



Be-BOP menawarkan Interface yang didedikasikan untuk penjualan fisik (toko, acara, dll.).



#### Penambahan cepat melalui alias



Dalam `/cart`, sebuah bidang memungkinkan Anda untuk menambahkan produk:





- Dengan memindai **kode batang** (ISBN, EAN13)
- Dengan memasukkan **alias produk** secara manual



**Catatan:** produk secara otomatis ditambahkan ke keranjang.



#### Cara pembayaran



Dukungan POS:





- Spesies
- Kartu kredit
- Lightning Network (kripto)
- Lainnya sesuai dengan konfigurasi



Tersedia dua opsi lanjutan:





- Pembebasan PPN**: berlaku berdasarkan justifikasi (LSM, orang asing...)
- Diskon hadiah**: diskon luar biasa dengan komentar wajib



#### Tampilan sisi klien



URL `/pos/session` ditujukan untuk **layar sekunder** (HDMI, tablet...):



Poster:





- Produk dalam proses
- Jumlah total
- Metode pembayaran
- Diskon berlaku



**Catatan:** pelanggan mengikuti pesanan secara langsung, sementara penjual mencatatnya di `/pos`.



### Ringkasan POS



| Fonction                         | Description                                             |
|----------------------------------|---------------------------------------------------------|
| Rôle POS                         | Assigné via ARM                                         |
| Interface principale             | `/pos` ou `/pos/touch`                                 |
| Affichage client (écran 2)       | `/pos/session`                                         |
| Paiement                         | Espèces, carte, Lightning, etc.                         |
| Ajout produit                    | Alias ou scan code-barres                              |
| Remises / TVA                    | Sur justification managériale obligatoire              |


Terima kasih telah mengikuti tutorial ini dengan saksama.