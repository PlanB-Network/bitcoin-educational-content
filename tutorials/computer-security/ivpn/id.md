---
name: IVPN
description: Mengatur VPN yang dibayar dengan bitcoin
---
![cover](assets/cover.webp)

VPN ("*Virtual Private Network*") adalah layanan yang membangun koneksi aman dan terenkripsi antara ponsel atau komputer Anda dengan server jarak jauh yang dikelola oleh penyedia VPN.

Secara teknis, ketika terhubung ke VPN, lalu lintas internet Anda akan dialihkan melalui sambungan terenkripsi ke server VPN. Proses ini mempersulit pihak ketiga, seperti Penyedia Layanan Internet (ISP) atau pihak yang berniat jahat, untuk mencegat atau membaca data Anda. Server VPN kemudian bertindak sebagai perantara yang terhubung ke layanan yang ingin Anda gunakan atas nama Anda. Ini akan memberikan alamat IP baru untuk koneksi Anda, yang membantu menyembunyikan alamat IP asli Anda dari situs yang Anda kunjungi. Namun, berbeda dengan apa yang mungkin disarankan oleh beberapa iklan online, penggunaan VPN tidak serta merta memungkinkan Anda menjelajahi internet secara anonim, karena hal ini membutuhkan bentuk kepercayaan pada penyedia VPN yang dapat melihat semua lalu lintas Anda.
![IVPN](assets/fr/01.webp)

Manfaat penggunaan VPN sangat banyak. Pertama, VPN menjaga privasi aktivitas online Anda dari Penyedia Layanan Internet (ISP) atau pemerintah, asalkan penyedia VPN tidak membagikan informasi Anda. Kedua, VPN mengamankan data Anda, terutama saat Anda terhubung ke jaringan Wi-Fi publik yang rentan terhadap serangan MITM (man-in-the-middle). Ketiga, dengan menyembunyikan alamat IP Anda, VPN memungkinkan Anda melewati pembatasan geografis dan sensor, untuk mengakses konten yang mungkin tidak tersedia atau diblokir di wilayah Anda.

Seperti yang Anda lihat, VPN mengalihkan risiko pengamatan lalu lintas ke penyedia VPN. Oleh karena itu, saat memilih penyedia VPN, penting untuk mempertimbangkan data pribadi yang diperlukan untuk pendaftaran. Jika penyedia meminta informasi seperti nomor telepon, alamat email, detail kartu bank, atau lebih buruk lagi, alamat pos Anda, risiko mengaitkan identitas Anda dengan lalu lintas Anda akan meningkat. Pada saat kasus kebocoran data penyedia atau penyitaan hukum, akan mudah untuk mengaitkan lalu lintas Anda dengan data pribadi Anda. Oleh karena itu, disarankan untuk memilih penyedia yang tidak memerlukan data pribadi apa pun dan menerima pembayaran anonim, seperti dengan Bitcoin.

Dalam tutorial ini, saya memperkenalkan solusi VPN yang sederhana, efisien, harga terjangkau, dan tidak memerlukan informasi pribadi untuk penggunaannya.

## Pengenalan ke IVPN

IVPN adalah layanan VPN yang dirancang khusus untuk pengguna yang mencari privasi. Berbeda dengan penyedia VPN populer yang sering dipromosikan di YouTube, IVPN menonjol karena transparansi, keamanan, dan penghormatan terhadap privasi.
Kebijakan privasi IVPN sangat ketat: tidak ada informasi pribadi yang diperlukan saat mendaftar. Anda dapat membuka akun tanpa memberikan alamat email, nama, atau nomor telepon. Untuk pembayaran, tidak perlu memasukkan detail kartu kredit, karena IVPN menerima pembayaran dalam Bitcoin (on-chain dan Lightning). Selain itu, IVPN mengklaim tidak menyimpan log aktivitas apa pun, yang berarti bahwa, secara teori, lalu lintas internet Anda tidak dicatat oleh perusahaan. 
IVPN juga [sepenuhnya open-source](https://github.com/ivpn), terkait perangkat lunak, aplikasi, dan bahkan situs web mereka, memungkinkan siapa pun untuk memverifikasi dan meninjau kode mereka. Mereka juga menjalani audit keamanan independen setiap tahun, yang hasilnya dipublikasikan di situs web mereka.

IVPN secara eksklusif menggunakan server yang dihosting sendiri, sehingga menghilangkan risiko yang terkait dengan penggunaan layanan cloud pihak ketiga, seperti AWS, Google Cloud, atau Microsoft Azure.

Layanan ini menawarkan berbagai fitur canggih, seperti multi-hop, yang mengarahkan lalu lintas melalui beberapa server yang terletak di yurisdiksi berbeda untuk meningkatkan anonimitas. IVPN juga mengintegrasikan pemblokir pelacak dan iklan, serta menawarkan opsi untuk memilih dari berbagai protokol VPN.

Tentu saja, kualitas layanan ini datang dengan biaya, tetapi harga yang sesuai sering kali menjadi indikator kualitas dan kejujuran. Ini bisa menandakan bahwa perusahaan memiliki model bisnis tanpa perlu menjual data pribadi. IVPN kemudian menawarkan 2 jenis paket: paket Standard, yang memungkinkan koneksi hingga 2 perangkat, dan paket Pro, yang memungkinkan hingga 7 koneksi dan mencakup protokol "Multi-hop" yang mengarahkan lalu lintas Anda melalui beberapa server.

Tidak seperti penyedia VPN pada umumnya, IVPN beroperasi dengan model pembelian waktu akses ke layanan, bukan langganan berulang. Anda membayar dalam Bitcoin sekali untuk durasi yang dipilih. Misalnya, jika Anda membeli akses satu tahun, Anda dapat menggunakan layanan tersebut untuk periode itu, setelah itu Anda harus kembali ke situs web IVPN untuk membeli waktu akses lagi.

[Tarif IVPN](https://www.ivpn.net/en/pricing/) bersifat progresif tergantung pada durasi akses yang dibeli. Berikut adalah harga untuk paket Standar:
- 1 minggu: $2
- 1 bulan: $6
- 1 tahun: $60
- 2 tahun: $100
- 3 tahun: $140

Dan untuk rencana Pro:
- 1 minggu: $4
- 1 bulan: $10
- 1 tahun: $100
- 2 tahun: $160
- 3 tahun: $220

## Bagaimana cara menginstal IVPN di komputer?
Unduh [versi terbaru dari perangkat lunak](https://www.ivpn.net/en/apps-windows/) untuk sistem operasi Anda, lalu lanjutkan dengan instalasi dengan mengikuti langkah-langkah di panduan instalasi (installation wizard).
![IVPN](assets/notext/02.webp)

Untuk pengguna Linux, merujuk pada instruksi khusus untuk distribusi Anda yang tersedia di [halaman ini](https://www.ivpn.net/en/apps-linux/).
![IVPN](assets/notext/03.webp)

Setelah instalasi selesai, Anda perlu memasukkan ID akun Anda. Kami akan menunjukkan cara mendapatkannya di bagian selanjutnya dari tutorial ini.
![IVPN](assets/notext/04.webp)

## Bagaimana cara menginstal IVPN di smartphone?

Unduh IVPN dari toko aplikasi Anda, baik itu [AppStore](https://apps.apple.com/us/app/ivpn-secure-vpn-for-privacy/id1193122683) untuk pengguna iOS, [Google Play Store](https://play.google.com/store/apps/details?id=net.ivpn.client) untuk Android, atau [F-Droid](https://f-droid.org/en/packages/net.ivpn.client). Jika Anda menggunakan Android, Anda juga memiliki opsi untuk mengunduh file `.apk` langsung dari [situs IVPN](https://www.ivpn.net/en/apps-android/)..

![IVPN](assets/notext/05.webp)

Saat pertama kali menggunakan aplikasi, Anda akan dalam keadaan logout. Anda perlu memasukkan ID akun Anda untuk mengaktifkan layanan ini.
![IVPN](assets/notext/06.webp)

Sekarang, mari kita lanjutkan ke aktivasi IVPN di perangkat Anda.

## Bagaimana cara membayar dan mengaktifkan IVPN?

Pergi ke situs web resmi IVPN [di halaman pembayaran](https://www.ivpn.net/en/pricing/).
![IVPN](assets/notext/07.webp)

Pilih paket yang paling sesuai dengan kebutuhan Anda. Untuk tutorial ini, kami akan memilih paket Standard, yang memungkinkan kami mengaktifkan VPN di komputer dan ponsel pintar kami, sebagai contoh.
![IVPN](assets/notext/08.webp)

IVPN kemudian akan membuat akun Anda. Anda tidak perlu memberikan data pribadi apa pun. ID akun Anda adalah satu-satunya yang akan memungkinkan Anda untuk masuk. Ini berfungsi semacam kunci akses. Simpanlah di tempat yang aman, seperti pengelola kata sandi Anda. Anda juga dapat membuat salinan cetak.
![IVPN](assets/notext/09.webp)

Di halaman yang sama, pilih durasi langganan Anda pada layanan tersebut.
![IVPN](assets/notext/10.webp)

Kemudian, pilih metode pembayaran Anda. Untuk bagian saya, saya akan melakukan pembayaran melalui Lightning Network, jadi saya mengeklik tombol "Bitcoin".
![IVPN](assets/notext/11.webp)

Pastikan semuanya sesuai dengan keinginan Anda, lalu klik tombol "Pay with Lightning".
![IVPN](assets/notext/12.webp)

Faktur Lightning akan disajikan kepada Anda di BTCPay Server mereka. Pindai kode QR dengan dompet Lightning Anda dan lanjutkan dengan pembayaran.
![IVPN](assets/notext/13.webp) 

Setelah faktur dibayar, klik pada tombol "*Return to IVPN"*".
![IVPN](assets/notext/14.webp)

Akun Anda kini akan muncul sebagai "*Active*", dan Anda dapat melihat tanggal hingga kapan akses VPN Anda berlaku. Setelah tanggal ini, Anda perlu memperbarui pembayaran Anda.
![IVPN](assets/notext/15.webp)

Untuk mengaktifkan koneksi Anda melalui IVPN di PC Anda, cukup salin ID akun Anda.
![IVPN](assets/notext/16.webp)

Dan tempelkan ke dalam perangkat lunak yang sebelumnya Anda unduh.
![IVPN](assets/notext/17.webp)

Kemudian klik pada tombol "*Login*".
![IVPN](assets/notext/18.webp)

Klik tanda centang untuk mengaktifkan koneksi VPN, dan sekarang, lalu lintas internet komputer Anda kini terenkripsi dan diarahkan melalui server IVPN.
![IVPN](assets/notext/19.webp)

Untuk smartphone Anda, prosedurnya identik. Tempelkan ID akun Anda atau pindai kode QR yang terhubung dengan akun IVPN Anda yang bisa diakses dari situs web. Setelah itu, klik tanda centang untuk membuat koneksi.
![IVPN](assets/notext/20.webp)

## Bagaimana cara menggunakan dan mengkonfigurasi IVPN?

Dalam hal penggunaan dan pengaturan, ini cukup sederhana. Dari antarmuka utama, Anda dapat mengaktifkan atau menonaktifkan koneksi hanya dengan menggunakan tanda centang.
![IVPN](assets/notext/21.webp)

Anda juga memiliki opsi untuk menjeda VPN Anda untuk durasi tertentu.
![IVPN](assets/notext/22.webp)

Dengan mengklik server yang sedang digunakan, Anda dapat memilih server lain dari daftar yang tersedia.
![IVPN](assets/notext/23.webp)

Anda juga bisa mengaktifkan atau menonaktifkan firewall terintegrasi serta fungsi anti-pelacak.
![IVPN](assets/notext/24.webp)

Untuk mengakses pengaturan tambahan, klik pada ikon pengaturan.
![IVPN](assets/notext/25.webp)

Pada tab "*Account*", Anda akan menemukan pengaturan yang terkait dengan akun Anda.
![IVPN](assets/notext/26.webp)

Pada tab "*General*", terdapat beberapa pengaturan klien. Saya menyarankan Anda untuk mencentang opsi "*Launch at login*" dan "*On launch*" di bagian "*Autoconnect*" untuk secara otomatis menyambungkan koneksi dengan VPN saat komputer Anda dimulai.
![IVPN](assets/notext/27.webp)

Pada tab "*Connection*", Anda akan menemukan berbagai opsi yang terkait dengan koneksi. Di sinilah Anda dapat mengubah protokol VPN yang digunakan.
![IVPN](assets/notext/28.webp)

Pada tab "*IVPN Firewall*" memungkinkan Anda mengaktifkan firewall secara sistematis saat komputer dinyalakan, memastikan tidak ada koneksi yang terjalin di luar VPN.
![IVPN](assets/notext/29.webp)

Pada tab "*Split Tunnel*" menawarkan kemungkinan untuk mengecualikan perangkat lunak tertentu dari koneksi VPN. Aplikasi yang ditambahkan di sini akan terus beroperasi dengan koneksi internet normal meskipun VPN diaktifkan.
![IVPN](assets/notext/30.webp)

Pada tab "*WiFi control*", Anda memiliki opsi untuk mengonfigurasi tindakan spesifik sesuai dengan jaringan yang Anda sambungkan. Misalnya, Anda dapat menetapkan jaringan rumah Anda sebagai "*Trusted*" dan mengonfigurasi VPN agar tidak aktif pada jaringan ini, tetapi otomatis aktif pada setiap jaringan WiFi lainnya.
![IVPN](assets/notext/31.webp)

Pada menu "*AntiTracker*", pilih profil pemblokiran untuk anti-pelacak Anda. Ini dirancang untuk memblokir iklan, malware, dan pelacak data dengan menghalangi permintaan ke layanan pelacakan saat Anda menjelajahi internet. Ini meningkatkan privasi Anda dengan mencegah perusahaan mengumpulkan dan menjual data penjelajahan Anda. "*Hardcore Mode*" juga tersedia untuk sepenuhnya memblokir semua domain milik Google dan Meta, serta semua layanan yang bergantung padanya.
![IVPN](assets/notext/32.webp)

Dan akhirnya! Kini Anda sudah siap untuk menikmati IVPN secara penuh. Jika Anda juga ingin meningkatkan keamanan akun online Anda dengan menggunakan pengelola kata sandi lokal, saya mengundang Anda untuk melihat tutorial kami tentang KeePass, sebuah solusi gratis dan open-source:

https://planb.network/tutorials/computer-security/authentication/keepass-f8073bb7-5b4a-4664-9246-228e307be246

Jika Anda tertarik untuk menemukan penyedia VPN lain yang serupa dengan IVPN, baik dalam hal fitur maupun harga, saya juga merekomendasikan untuk melihat tutorial kami tentang Mullvad:

https://planb.network/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8
