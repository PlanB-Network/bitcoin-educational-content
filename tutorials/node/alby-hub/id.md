---
name: Alby Hub
description: Bagaimana cara mudah meluncurkan simpul Lightning Anda sendiri?
---
![cover](assets/cover.webp)

Alby Hub adalah perangkat lunak terbaru dari Alby, perusahaan di balik ekstensi web Lightning yang populer. Alby Hub adalah antarmuka yang mudah digunakan untuk mengelola node Lightning.

Dalam tutorial ini, kita akan melihat berbagai cara menggunakan Alby Hub untuk mengelola node Lightning Anda sendiri, dan cara menghubungkannya ke Alby Go, aplikasi seluler Alby. Ini akan memungkinkan Anda untuk menggunakan sats Anda saat bepergian sambil menjadi otonom dalam pengelolaan node Anda.

![ALBY HUB](assets/fr/01.webp)

## Apa yang dimaksud dengan Alby Hub?

Pada tahun 2024, Alby menandai pergeseran strategis. Selama bertahun-tahun, mereka telah menawarkan berbagai alat yang terkait dengan Bitcoin dan Lightning Network, termasuk ekstensi Alby yang ikonik, yang memungkinkan Anda untuk mengoperasikan dompet Lightning, kustodian atau lainnya. Namun, pada tahun 2025, mereka berencana untuk menghentikan layanan dompet kustodian bersama mereka dan fokus secara eksklusif pada solusi kustodian mandiri. Alby Hub akan menjadi alat andalan baru dalam ekosistem Alby. Perangkat lunak ini memungkinkan pengguna untuk dengan mudah mengelola node Lightning mereka sendiri, sambil mempertahankan kepemilikan kunci mereka (self-custody).

Alby Hub adalah alat yang sangat mudah beradaptasi. Alat ini dapat memenuhi kebutuhan pengguna pemula dan pengguna tingkat lanjut. Para pemula akan menggunakannya untuk mengoperasikan sendiri node Lightning sungguhan dengan mudah, tanpa harus berurusan dengan kerumitan yang mendasarinya. Untuk pengguna yang lebih berpengalaman, Alby Hub dapat digunakan sebagai antarmuka lengkap untuk manajemen tingkat lanjut dari node Lightning yang ada.

Tergantung pada kebutuhan Anda, Alby Hub tersedia dalam 4 konfigurasi:


- Alby Hub Cloud: ** Awan Alby

Ideal untuk pemula, opsi pertama ini adalah opsi cloud Alby. Opsi ini memungkinkan Anda untuk menggunakan node Lightning secara langsung di server yang dikelola Alby, yang dapat diakses melalui antarmuka Alby Hub Anda. Meskipun Alby mengelola server, Anda tetap memiliki kedaulatan atas dana Anda, karena kunci Anda dienkripsi menggunakan kata sandi yang hanya diketahui oleh Anda. Akan tetapi, kunci Anda harus tetap didekripsi dalam RAM agar node dapat beroperasi, yang secara teoritis membuat mereka berisiko jika seseorang secara fisik mengakses server. Ini adalah kompromi yang menarik untuk pemula, tetapi penting untuk menyadari risikonya.

Keuntungan utama dari opsi ini adalah Anda mendapatkan node Lightning yang aktif dan berjalan 24/7, tanpa harus mengelola hosting sendiri. Terlebih lagi, pencadangan node Lightning Anda disederhanakan dan diotomatisasi, dibandingkan dengan opsi hosting mandiri yang mengharuskan Anda mengelola sendiri pencadangan saluran.

Alby menawarkan layanan ini seharga 21.000 sat per bulan (harga Desember 2024, bisa berubah, [periksa harga mereka] (https://albyhub.com/#pricing)). Biaya ini secara otomatis dipotong dari node Anda melalui faktur Lightning yang dikeluarkan oleh Alby. Hal ini dilakukan melalui koneksi NWC yang mengonfigurasi node Anda untuk secara otomatis membayar faktur Alby yang terkait dengan langganan Anda.


- Alby Hub dengan simpul yang sudah ada :**

Jika Anda sudah memiliki node yang dihosting, misalnya pada Umbrel atau Start9, Alby Hub dapat digunakan sebagai antarmuka manajemen tingkat lanjut, dengan cara yang sama seperti ThunderHub atau RTL.


- Alby Hub lokal :** Lokal

Anda juga dapat menginstal Alby Hub dan node Anda langsung di PC Anda, meskipun opsi ini kurang praktis, karena PC Anda harus tetap aktif setiap saat untuk mengakses node Lightning dari jarak jauh. Namun, alternatif ini mungkin cocok untuk kebutuhan spesifik Anda.


- Alby Hub di server pribadi :**

Untuk pengguna tingkat lanjut, Alby Hub dapat digunakan pada server pribadi dengan perintah sederhana. Opsi ini tidak tercakup dalam tutorial ini, tetapi Anda dapat menemukan instruksi khusus [di GitHub Alby](https://github.com/getAlby/hub?tab=readme-ov-file#docker).

Tutorial ini berfokus terutama pada antarmuka, yang akan sama, apa pun opsi yang dipilih. Kita juga akan melihat cara menggunakan Alby Hub dengan opsi cloud berbayar, lalu dengan opsi node-in-box (Umbrel atau Start9).

![ALBY HUB](assets/fr/02.webp)

Untuk instalasi lokal pada PC Anda, [unduh dan instal perangkat lunak sesuai dengan sistem operasi Anda](https://github.com/getAlby/hub/releases), kemudian ikuti petunjuk yang sama pada antarmuka.

![ALBY HUB](assets/fr/03.webp)

## Membuat akun Alby

Langkah pertama adalah membuat akun Alby. Meskipun hal ini tidak penting untuk menggunakan Alby Hub, namun Anda dapat memanfaatkan sepenuhnya opsi yang tersedia, termasuk kemungkinan mendapatkan alamat Lightning.

Kunjungi [situs web resmi Alby] (https://getalby.com/) dan klik tombol "*Buat Akun*".

![ALBY HUB](assets/fr/04.webp)

Masukkan nama panggilan dan alamat email, lalu klik "*Daftar*". Alamat email ini akan digunakan untuk masuk ke akun Anda nanti.

![ALBY HUB](assets/fr/05.webp)

Masukkan kode verifikasi yang Anda terima melalui email.

![ALBY HUB](assets/fr/06.webp)

Setelah masuk ke akun online Anda, klik tombol "*Lanjutkan*".

![ALBY HUB](assets/fr/07.webp)

Klik "*Lanjutkan*" sekali lagi.

![ALBY HUB](assets/fr/08.webp)

## Opsi hosting awan

Anda kemudian harus memilih antara opsi hosting mandiri, di mana Anda meng-host node Lightning pada perangkat keras Anda sendiri, atau opsi berbayar menggunakan awan Alby. Saya akan mulai dengan menjelaskan cara melanjutkan dengan opsi Cloud (perhatikan bahwa ini adalah opsi berbayar, lihat detailnya di bagian sebelumnya).

Klik "*Upgrade*".

![ALBY HUB](assets/fr/09.webp)

Konfirmasikan dengan mengklik "*Langganan Sekarang*".

![ALBY HUB](assets/fr/10.webp)

Klik "*Luncurkan Alby Hub*".

![ALBY HUB](assets/fr/11.webp)

Tunggu beberapa saat sementara node Anda dibuat.

![ALBY HUB](assets/fr/12.webp)

Dan selesai, Alby Hub Anda sekarang sudah terkonfigurasi. Di bagian selanjutnya, saya akan menunjukkan kepada Anda cara menginstal Alby Hub pada node yang sudah ada. Jika Anda tidak perlu, Anda bisa langsung ke bagian berikutnya untuk mengonfigurasi node Anda.

![ALBY HUB](assets/fr/13.webp)

## Opsi hosting mandiri

Jika Anda lebih suka menggunakan Alby Hub sebagai antarmuka untuk node Lightning Anda yang sudah ada, Anda memiliki beberapa opsi: menginstalnya di server, secara lokal di komputer Anda, atau melalui node-in-box (Umbrel atau Start9). Menggunakan Alby Hub dalam konfigurasi ini tidak dipungut biaya. Kita akan berkonsentrasi pada opsi node-in-box, karena menurut saya opsi server, tanpa akses fisik, memiliki risiko yang sama dengan versi cloud, dan instalasi lokal pada PC sering kali tidak cocok.

Untuk mengatur ini pada Umbrel (langkah-langkah untuk Start9 sama), Anda harus terlebih dahulu memiliki simpul LND yang sudah dikonfigurasi.

Masuk ke antarmuka Umbrel Anda dan buka toko aplikasi.

![ALBY HUB](assets/fr/14.webp)

Cari aplikasi "*Alby Hub*".

![ALBY HUB](assets/fr/15.webp)

Instal di node Anda.

![ALBY HUB](assets/fr/16.webp)

Antarmuka Alby Hub Anda sekarang sudah siap. Anda dapat mengikuti tutorial selanjutnya seolah-olah Anda menggunakan antarmuka cloud, tetapi tanpa opsi versi berbayar. Terlebih lagi, tidak seperti versi cloud, kunci Anda disimpan secara lokal di node Anda, bukan di server Alby.

![ALBY HUB](assets/fr/17.webp)

## Meluncurkan Alby Hub

Klik tombol "*Mulai*".

![ALBY HUB](assets/fr/18.webp)

Alby Hub kemudian akan meminta Anda untuk memilih kata sandi. Kata sandi ini sangat penting, karena akan digunakan untuk mengenkripsi dompet Anda. Pada versi cloud berbayar, kunci Anda disimpan di server Alby, dienkripsi dengan kata sandi yang hanya Anda yang tahu, kemudian didekripsi dan disimpan hanya di RAM untuk menandatangani transaksi bila diperlukan.

Oleh karena itu, sangat penting untuk memilih kata sandi yang kuat. Siapa pun yang memiliki kata sandi ini berpotensi mendapatkan akses ke node Anda. Pastikan Anda juga membuat satu atau beberapa salinan kata sandi ini pada selembar kertas, atau lebih baik lagi, pada sepotong logam untuk keamanan tambahan. **Jika Anda kehilangan kata sandi ini, maka tidak mungkin untuk memulihkan akses ke bitcoin Anda**, karena Alby tidak memiliki cara untuk meresetnya. Hilangnya kata sandi ini berarti hilangnya bitcoin Anda.

Setelah Anda memilih dan menyimpan kata sandi dengan hati-hati, klik "*Buat Kata Sandi*".

![ALBY HUB](assets/fr/19.webp)

Anda sekarang memiliki akses ke simpul Lightning Anda.

![ALBY HUB](assets/fr/20.webp)

Tindakan pertama yang harus dilakukan adalah menyimpan frasa pemulihan Anda, yang darinya kunci Anda berasal. Frasa ini memungkinkan Anda untuk memulihkan akses ke dompet onchain Anda dan, dengan status terbaru dari saluran Anda, sats Anda di Lightning. Untuk melakukan ini, klik "*Settings*".

![ALBY HUB](assets/fr/21.webp)

Lalu buka tab "*Cadangan*". Masukkan kata sandi Anda untuk mengaksesnya.

![ALBY HUB](assets/fr/22.webp)

Anda kemudian akan memiliki akses ke frasa pemulihan 12 kata Anda. Buatlah satu atau beberapa salinan fisik dari frasa ini di atas kertas atau logam, dan simpan di tempat yang aman.

![ALBY HUB](assets/fr/23.webp)

Setelah Anda menyimpan frasa, centang kotak untuk mengonfirmasi bahwa Anda telah menyimpannya dan klik "*Lanjutkan*".

![ALBY HUB](assets/fr/24.webp)

## Bagaimana cara memulihkan akses ke bitcoin saya?

Sebelum mengirim dana ke node Anda, penting untuk memahami cara memulihkannya jika terjadi masalah, serta informasi apa saja yang diperlukan untuk pemulihan ini. Prosesnya bervariasi sesuai dengan sifat dana yang akan dipulihkan dan mode hosting node Anda.

Untuk pengguna cloud berbayar, pemulihan lengkap bitcoin Anda memerlukan tiga elemen penting:


- Ungkapan pemulihan Anda;
- Kata sandi Anda (kata sandi yang digunakan untuk node Anda);
- Akses ke akun Alby Anda, untuk mengambil status terbaru dari saluran Lightning Anda.

Ketiadaan salah satu dari ketiga informasi ini akan membuat Anda tidak dapat memulihkan bitcoin Anda secara penuh.

Bagi mereka yang meng-host node mereka sendiri, proses pemulihan identik dengan proses pemulihan untuk node Lightning mana pun. Anda akan membutuhkan :


- Ungkapan pemulihan Anda;
- Status terbaru dari saluran Lightning Anda. Untuk mengamankan informasi ini, Umbrel menawarkan [opsi](https://github.com/getumbrel/umbrel/blob/2b266036f62a1594aa60a8a3be30cfb8656e755f/scripts/backup/README.md) untuk mengenkripsinya dan menyimpannya secara dinamis dan anonim melalui Tor.

## Beli saluran Lightning pertama Anda

Anda sekarang dapat mengikuti instruksi yang diberikan oleh Alby Hub. Klik pada tombol untuk membuka saluran pertama Anda untuk uang masuk.

![ALBY HUB](assets/fr/25.webp)

Pilih "*Saluran Terbuka*". Jika Anda tidak berniat untuk menjadi simpul perutean dan tidak secara khusus membutuhkannya, saya sarankan Anda memilih saluran pribadi.

![ALBY HUB](assets/fr/26.webp)

Alby Hub akan membuat faktur untuk Anda bayar. Pembayaran ini mencakup biaya transaksi yang diperlukan untuk membuka saluran Anda, serta biaya layanan LSP (*Lightning Service Provider*) yang akan membuka saluran ke node Anda, sehingga Anda dapat menerima pembayaran dengan segera.

![ALBY HUB](assets/fr/27.webp)

Setelah faktur dibayar dan transaksi dikonfirmasi, saluran Lightning pertama Anda telah dibuat.

![ALBY HUB](assets/fr/28.webp)

Pada tab "*Node*", Anda dapat melihat bahwa Anda sekarang memiliki uang masuk, yang memungkinkan Anda untuk menerima pembayaran melalui Lightning.

![ALBY HUB](assets/fr/29.webp)

Untuk menerima pembayaran, klik tab "*Dompet*" lalu "*Terima*".

![ALBY HUB](assets/fr/30.webp)

Masukkan jumlah dan tambahkan deskripsi jika perlu, lalu klik "*Buat Faktur*".

![ALBY HUB](assets/fr/31.webp)

Saya menerima pembayaran pertama saya sebesar 120.000 sat.

![ALBY HUB](assets/fr/32.webp)

Dengan kembali ke tab "*Dompet*", Anda dapat memeriksa saldo dompet Anda. Perhatikan bahwa Alby Hub secara otomatis menyisihkan 354 sat ketika Anda melakukan pembayaran pertama. Untuk setiap saluran Lightning yang Anda buka setelahnya, Alby Hub akan secara otomatis menyisihkan cadangan yang setara dengan 1% dari kapasitas saluran. Cadangan ini merupakan langkah keamanan yang memungkinkan node Anda untuk memulihkan dana saluran jika terjadi upaya penipuan oleh rekan Anda. Itulah sebabnya, meskipun saya telah mengirim 120.000 satelit, hanya 119.646 satelit yang ditampilkan di saldo saya.

![ALBY HUB](assets/fr/33.webp)

## Menyimpan bitcoin di rantai

Jika Anda ingin memiliki uang tunai keluar untuk melakukan pembayaran, Anda juga dapat membuka saluran sendiri. Untuk melakukan ini, Anda memerlukan bitcoin onchain di dompet Anda.

Dari tab "*Node*", klik "*Deposit*".

![ALBY HUB](assets/fr/34.webp)

Kirim bitcoin ke alamat yang ditampilkan. Alamat ini berasal dari frasa pemulihan yang Anda simpan sebelumnya.

![ALBY HUB](assets/fr/35.webp)

Saya telah mengirim 72.000 satoshi. Mereka sekarang terlihat di "*Saldo Tabungan*", yang mencakup semua dana yang saya miliki di chain, dan bukan di Lightning.

![ALBY HUB](assets/fr/36.webp)

## Buka saluran Lightning

Setelah Anda memiliki dana onchain, Anda dapat membuka channel Lightning baru. Disarankan untuk membuka beberapa channel, dengan jumlah yang cukup untuk memastikan bahwa Anda selalu dapat melakukan pembayaran tanpa kendala. Sebagian besar LSP (*Lightning Service Provider*) membutuhkan minimal 150.000 sat untuk membuka saluran dengan Anda.

Pada tab "*Node*", klik "*Open Channel*".

![ALBY HUB](assets/fr/37.webp)

Pilih ukuran channel Anda. Saya sarankan agar Anda tidak membuka saluran yang terlalu kecil, mengingat ini adalah node Lightning dan mesin yang menghosting kunci Anda tidak menawarkan tingkat keamanan yang sama dengan dompet perangkat keras. Jadi berhati-hatilah dengan jumlah yang Anda pilih untuk diblokir.

![ALBY HUB](assets/fr/38.webp)

Di menu "*Opsi Lanjutan*", Anda dapat memilih LSP mana yang akan digunakan untuk membuka saluran Anda, atau secara manual memasukkan simpul Lightning lain.

![ALBY HUB](assets/fr/39.webp)

Kemudian klik "*Buka Saluran*".

![ALBY HUB](assets/fr/40.webp)

Tunggu sementara saluran Anda dikonfirmasi di rantai.

![ALBY HUB](assets/fr/41.webp)

Saluran baru Anda sekarang akan muncul di tab "*Node*".

![ALBY HUB](assets/fr/42.webp)

## Menghubungkan aplikasi pengeluaran

Sekarang setelah Anda memiliki node Lightning yang berfungsi, Anda bisa menggunakannya untuk menerima dan membelanjakan satoshi setiap hari. Meskipun antarmuka web Alby Hub berguna untuk mengelola node Anda, namun tidak ideal untuk melakukan transaksi cepat saat bepergian. Untuk itu, kita akan menggunakan aplikasi dompet Lightning yang terinstal di ponsel pintar kita.

Dalam tutorial ini, saya sarankan Anda memilih Alby Go, yang sangat mudah digunakan, tetapi Anda juga dapat menggunakan aplikasi lain yang kompatibel seperti Zeus.

![ALBY HUB](assets/fr/43.webp)

Untuk menginstal Alby Go, buka toko aplikasi perangkat Anda:


- [Untuk Android](https://play.google.com/store/apps/details?id=com.getalby.mobile);
- [Untuk Apple](https://apps.apple.com/us/app/alby-go/id6471335774).

![ALBY HUB](assets/fr/44.webp)

Pengguna Android juga dapat menginstal aplikasi ini melalui file `.apk` [tersedia di GitHub Alby](https://github.com/getAlby/go/releases).

![ALBY HUB](assets/fr/45.webp)

Ketika aplikasi diluncurkan, klik "*Hubungkan Dompet*".

![ALBY HUB](assets/fr/46.webp)

Di Alby Hub Anda, di bawah tab "*Koneksi*", klik "*Tambah Koneksi*".

![ALBY HUB](assets/fr/47.webp)

Beri nama koneksi ini untuk mengidentifikasinya dengan mudah di Hub Anda, dan pilih izin yang ingin Anda berikan ke aplikasi. Dalam kasus saya, saya memilih "*Akses Penuh*" untuk mendapatkan akses penuh ke dana Lightning node saya dari ponsel cerdas saya, tetapi Anda juga bisa membatasi akses dengan anggaran maksimum, memilih fitur yang diizinkan, atau menetapkan tanggal kedaluwarsa untuk izin ini. Setelah dikonfigurasi, klik "*Next*".

![ALBY HUB](assets/fr/48.webp)

Alby Hub kemudian akan menghasilkan sebuah rahasia untuk membuat koneksi.

![ALBY HUB](assets/fr/49.webp)

Kembali ke aplikasi Alby Go, pindai kode QR atau tempelkan rahasianya.

![ALBY HUB](assets/fr/50.webp)

Klik "Selesai*".

![ALBY HUB](assets/fr/51.webp)

Anda sekarang memiliki akses jarak jauh ke node Lightning Anda dari ponsel cerdas Anda, membuatnya mudah untuk mengirim dan menerima satelit saat bepergian setiap hari.

![ALBY HUB](assets/fr/52.webp)

Jika perlu, Anda dapat mengelola izin untuk koneksi ini secara langsung di Alby Hub dengan mengkliknya.

![ALBY HUB](assets/fr/53.webp)

Untuk menerima sats, cukup klik "*Terima*".

![ALBY HUB](assets/fr/54.webp)

Ubah jumlah dan deskripsi faktur dengan mengklik "*Faktur*".

![ALBY HUB](assets/fr/55.webp)

Tagih faktur untuk menerima sat.

![ALBY HUB](assets/fr/56.webp)

Untuk mengirim sat, klik "*Kirim*".

![ALBY HUB](assets/fr/57.webp)

Pindai faktur yang ingin Anda bayar.

![ALBY HUB](assets/fr/58.webp)

Kemudian klik "*Bayar*".

![ALBY HUB](assets/fr/59.webp)

Transaksi Anda telah dikonfirmasi.

![ALBY HUB](assets/fr/60.webp)

Dengan mengeklik tanda panah kecil, Anda dapat mengakses riwayat transaksi Anda.

![ALBY HUB](assets/fr/61.webp)

Transaksi ini juga dapat dilihat di Alby Hub Anda.

![ALBY HUB](assets/fr/62.webp)

## Menyesuaikan alamat Lightning Anda

Alby menawarkan opsi alamat Lightning. Ini memungkinkan Anda untuk menerima pembayaran di node Anda tanpa harus membuat faktur secara manual setiap kali. Secara default, Alby memberikan Anda alamat Lightning, tetapi Anda bisa menyesuaikannya. Masuk ke akun online Alby Anda, klik nama Anda di sudut kanan atas, lalu pilih "*Pengaturan*".

![ALBY HUB](assets/fr/63.webp)

Navigasikan ke menu "*Lightning Address*".

![ALBY HUB](assets/fr/64.webp)

Ubah alamat Anda, lalu konfirmasikan dengan mengklik "*Perbarui alamat lightning Anda*".

![ALBY HUB](assets/fr/65.webp)

Harap diperhatikan bahwa setelah alamat Anda diubah, alamat tersebut tidak lagi menjadi milik Anda. Jadi, pastikan Anda tidak akan pernah mengirim sat lagi ke alamat tersebut.

Dan itu saja, Anda sekarang tahu cara menggunakan Lightning dengan node Anda sendiri menggunakan alat Alby Hub. Jika Anda merasa tutorial ini bermanfaat, saya akan sangat berterima kasih jika Anda memberikan jempol hijau di bawah ini. Jangan ragu untuk membagikan artikel ini di jejaring sosial Anda. Terima kasih banyak!

Untuk memahami secara detail semua mekanisme Lightning yang telah kami manipulasi dalam tutorial ini, saya sangat menyarankan Anda untuk menemukan pelatihan gratis kami tentang subjek ini :

https://planb.network/courses/lnp201