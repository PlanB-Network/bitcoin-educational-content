---
name: Mullvad VPN
description: Mengatur VPN yang dibayar dengan bitcoin
---
![cover](assets/cover.webp)

VPN ("*Virtual Private Network*") adalah layanan yang membangun koneksi aman dan terenkripsi antara perangkat Anda seperti ponsel atau komputer dengan server jarak jauh yang dikelola oleh penyedia VPN.

Secara teknis, ketika Anda terhubung ke VPN, lalu lintas internet Anda akan dialihkan melalui sambungan terenkripsi menuju server VPN. Proses ini mempersulit pihak ketiga, seperti Penyedia Layanan Internet (ISP) atau pihak-pihak berbahaya, untuk mencegat atau membaca data Anda. Server VPN kemudian bertindak sebagai perantara yang menghubungkan Anda ke layanan yang ingin Anda gunakan. Server tersebut akan menetapkan alamat IP baru untuk koneksi Anda, yang membantu menyembunyikan alamat IP asli Anda dari situs-situs yang Anda kunjungi. Namun, perlu diingat, bertentangan dengan apa yang mungkin disarankan oleh beberapa iklan online, menggunakan VPN tidak membuat Anda sepenuhnya anonim saat menjelajah internet. Hal ini karena Anda perlu menaruh kepercayaan pada penyedia VPN yang dapat melihat seluruh lalu lintas Anda.

![MULLVAD VPN](assets/fr/01.webp)

Penggunaan VPN memiliki banyak manfaat. Pertama, layanan ini melindungi privasi aktivitas daring Anda dari Penyedia Layanan Internet (ISP) atau pemerintah, dengan catatan bahwa penyedia VPN tidak membagikan informasi Anda. Kedua, VPN mengamankan data Anda, terutama saat Anda terhubung ke jaringan Wi-Fi publik yang rentan terhadap serangan MITM (man-in-the-middle). Ketiga, dengan menyembunyikan alamat IP Anda, VPN memungkinkan Anda mengatasi pembatasan geografis dan sensor, sehingga Anda dapat mengakses konten yang mungkin tidak tersedia atau diblokir di wilayah Anda.

Seperti yang dapat Anda lihat, VPN mengalihkan risiko pengamatan lalu lintas ke penyedia VPN. Oleh karena itu, saat memilih penyedia VPN, penting untuk mempertimbangkan data pribadi yang diminta saat pendaftaran. Jika penyedia meminta informasi seperti nomor telepon, alamat email, detail kartu bank, atau bahkan alamat pos Anda, risiko identitas Anda terkait dengan lalu lintas Anda akan meningkat. Apabila terjadi kebocoran pada penyedia atau penyitaan hukum, akan mudah untuk menghubungkan lalu lintas Anda dengan data pribadi Anda. Oleh karena itu, disarankan untuk memilih penyedia yang tidak memerlukan informasi pribadi apa pun dan menerima pembayaran anonim, seperti dengan Bitcoin.

Dalam tutorial ini, saya akan memperkenalkan solusi VPN yang sederhana, efisien, harga terjangkau, dan tidak memerlukan informasi pribadi untuk penggunaannya.

## Pengenalan Mullvad VPN

Mullvad VPN adalah layanan asal Swedia yang sangat menonjol karena komitmennya terhadap privasi pengguna. Berbeda dengan penyedia VPN pada umumnya, Mullvad tidak memerlukan data pribadi saat pendaftaran. Anda tidak perlu memberikan alamat email, nomor telepon, atau nama; sebagai gantinya, Mullvad akan memberikan Anda nomor akun anonim yang digunakan untuk pembayaran dan akses layanan. Selain itu, Mullvad mengklaim tidak menyimpan log aktivitas apa pun yang melewati server mereka.
![MULLVAD VPN](assets/notext/02.webp)

Untuk pembayaran, tidak wajib memberikan informasi kartu kredit karena Mullvad menerima pembayaran Bitcoin (khusus onchain di situs resmi mereka, namun ada metode tidak resmi untuk membayar melalui Lightning). Mereka juga menerima pembayaran tunai melalui pos.

Mullvad VPN juga berbeda dari yang lain karena transparansi dan keamanannya. Perangkat lunak mereka bersifat open-source, dan mereka secara rutin menjalani audit keamanan independen untuk menilai aplikasi dan infrastruktur mereka, yang hasilnya [dipublikasikan di situs web mereka](https://mullvad.net/fr/blog/tag/audits). Perusahaan di balik Mullvad berlokasi di Swedia, negara yang terkenal dengan undang-undang privasi yang ketat. Mereka secara eksklusif menggunakan server yang di-hosting sendiri, sehingga menghilangkan risiko terkait penggunaan layanan cloud pihak ketiga, seperti hyperscaler AWS, Google Cloud, atau Microsoft Azure.

Dalam hal fitur, Mullvad menawarkan semua yang diharapkan dari klien VPN yang baik, termasuk kill switch yang melindungi lalu lintas Anda jika VPN terputus, opsi untuk menonaktifkan VPN untuk aplikasi tertentu, dan kemampuan untuk mengarahkan lalu lintas Anda melalui beberapa server VPN.

Tentu saja, kualitas layanan ini sejalan dengan biaya, namun harga yang wajar sering kali menjadi indikator kualitas dan kejujuran. Ini dapat menandakan bahwa perusahaan memiliki model bisnis tanpa perlu menjual data pribadi Anda kepada pihak ketiga. Mullvad VPN menawarkan tarif tetap 5 euro per bulan, yang dapat digunakan pada hingga 5 perangkat berbeda.
![MULLVAD VPN](assets/notext/03.webp)

Berbeda dengan penyedia VPN umumnya, Mullvad menerapkan model pembelian waktu akses ke layanan, bukan langganan otomatis yang berulang. Anda cukup melakukan pembayaran satu kali dalam Bitcoin untuk durasi yang dipilih. Contohnya, jika Anda membeli akses selama satu tahun, Anda dapat menggunakan layanan tersebut untuk periode itu. Setelahnya, Anda perlu kembali ke situs web Mullvad untuk memperbarui waktu akses.
Dibandingkan dengan IVPN, penyedia VPN berkualitas tinggi lainnya, Mullvad sedikit lebih ekonomis. Misalnya, bahkan saat memilih pembelian tiga tahun dengan IVPN, biaya bulanan mencapai sekitar €5,40. Namun, IVPN memang menawarkan beberapa layanan tambahan dan juga memiliki paket yang lebih murah daripada Mullvad (paket Standard), tetapi ini terbatas hanya untuk 2 perangkat dan tidak menyertakan protokol "multi-hop."
Saya juga melakukan beberapa uji kecepatan informal untuk membandingkan IVPN dan Mullvad. Meskipun IVPN menunjukkan sedikit keunggulan dalam hal performa, kecepatan di Mullvad masih sangat memuaskan. Dibandingkan dengan penyedia VPN umum, IVPN dan Mullvad terbukti setidaknya sama efisiennya, bahkan lebih unggul dalam beberapa kasus.

## Bagaimana cara menginstal Mullvad VPN di komputer?

Kunjungi [situs resmi Mullvad](https://mullvad.net/en/download/) dan klik pada menu "*Downloads*".
![MULLVAD VPN](assets/notext/04.webp)

Untuk pengguna Windows atau macOS, unduh perangkat lunak langsung dari situs tersebut dan ikuti instruksi yang diberikan oleh panduan (wizard) pengaturan untuk menyelesaikan instalasi.
![MULLVAD VPN](assets/notext/05.webp)

Untuk pengguna Linux, Anda dapat menemukan instruksi khusus untuk distribusi Anda di bagian ["*Linux*"](https://mullvad.net/en/download/vpn/linux).
![MULLVAD VPN](assets/notext/06.webp)

Setelah instalasi selesai, Anda perlu memasukkan ID akun Anda. Kami akan menunjukkan cara memperolehnya di bagian-bagian selanjutnya dari tutorial ini.

## Bagaimana cara menginstal Mullvad VPN di smartphone?

Unduh Mullvad VPN dari toko aplikasi Anda, baik itu [AppStore](https://apps.apple.com/us/app/mullvad-vpn/id1488466513) untuk pengguna iOS, [Google Play Store](https://play.google.com/store/apps/details?id=net.mullvad.mullvadvpn) untuk Android, atau [F-Droid](https://f-droid.org/packages/net.mullvad.mullvadvpn/). Jika Anda menggunakan Android, Anda juga memiliki opsi untuk mengunduh file `.apk` langsung dari [situs Mullvad](https://mullvad.net/en/download/vpn/android).
![MULLVAD VPN](assets/notext/07.webp)

Pada penggunaan pertama aplikasi, Anda akan keluar. Anda perlu memasukkan ID akun Anda untuk mengaktifkan layanan.
![MULLVAD VPN](assets/notext/08.webp)

Sekarang, mari kita lanjutkan ke aktivasi Mullvad di perangkat Anda.

## Bagaimana cara membayar dan mengaktifkan Mullvad VPN?

Kunjungi [situs resmi Mullvad](https://mullvad.net/) dan klik tombol "*Get Started*".
![MULLVAD VPN](assets/notext/09.webp)

Klik pada tombol "*Generate account number*".
![MULLVAD VPN](assets/notext/10.webp)

Mullvad akan membuat akun Anda. Anda tidak perlu memberikan informasi pribadi apa pun. Hanya nomor akun Anda yang akan memungkinkan Anda untuk masuk. Ini berfungsi mirip dengan kunci akses. Simpan di tempat yang aman seperti pengelola kata sandi Anda, misalnya. Anda juga dapat membuat salinan di kertas.
![MULLVAD VPN](assets/notext/11.webp)

Kemudian klik pada tombol "*Add time to your account*".
![MULLVAD VPN](assets/notext/12.webp)

Anda kemudian akan tiba di halaman login untuk akun Anda. Masukkan nomor akun Anda kemudian klik tombol "*Log in*".
![MULLVAD VPN](assets/notext/13.webp)

Pilih metode pembayaran Anda. Saya merekomendasikan pembayaran menggunakan Bitcoin, karena Anda akan mendapatkan diskon 10%, yang menurunkan biaya menjadi €4,50 per bulan. Jika Anda lebih memilih untuk membayar melalui Lightning, saya akan menyediakan metode alternatif di bagian selanjutnya.
![MULLVAD VPN](assets/notext/14.webp)

Klik tombol "*Create a one-time payment address*".
![MULLVAD VPN](assets/notext/15.webp)

Kemudian bayarlah dengan dompet Bitcoin Anda jumlah yang tertera ke alamat penerima yang diberikan kepada Anda.
![MULLVAD VPN](assets/notext/16.webp)

Mungkin perlu beberapa menit sebelum situs mendeteksi pembayaran Anda, setelah transaksi dikonfirmasi. Setelah pembayaran terdeteksi oleh Mullvad, durasi langganan Anda akan muncul di kiri atas halaman, menggantikan tulisan "*No time left*".
![MULLVAD VPN](assets/notext/17.webp)

Anda kemudian dapat memasukkan nomor akun Anda pada perangkat lunak untuk mengaktifkan VPN.
![MULLVAD VPN](assets/notext/18.webp)

Untuk mengaktifkan VPN di aplikasi seluler Anda, prosesnya persis sama. Anda hanya perlu memasukkan nomor akun Anda.
![MULLVAD VPN](assets/notext/19.webp)

## Bagaimana cara membayar Mullvad VPN dengan Lightning?

Seperti yang telah Anda pahami, Mullvad belum menerima pembayaran melalui Lightning Network. Namun, berkat rekomendasi dari [Lounès](https://x.com/louneskmt), saya menemukan sebuah layanan tidak resmi yang memungkinkan Anda untuk mengatasi keterbatasan ini. Layanan ini, yang tersedia di [vpn.sovereign.engineering](https://vpn.sovereign.engineering/), menerima pembayaran Anda melalui Lightning dan sebagai gantinya akan menyediakan paket Mullvad yang valid untuk Anda.
![MULLVAD VPN](assets/notext/20.webp)

Anda memiliki 2 opsi berbeda di situs ini: Anda dapat memercayai pengelola situs dan langsung memasukkan nomor akun Anda. Setelah itu, klik tombol "*Log in*" agar paket Mullvad Anda otomatis tervalidasi. Atau, Anda bisa mengeklik tombol "*Heck yeah!*" untuk membeli Voucher menggunakan Lightning, yang nantinya dapat Anda gunakan di situs resmi Mullvad untuk mendapatkan paket Anda.
![MULLVAD VPN](assets/notext/21.webp) 

Dalam kedua kasus tersebut, Anda kemudian akan diminta untuk memilih durasi paket Anda. Anda dapat memilih antara 6 bulan dan 1 tahun.
![MULLVAD VPN](assets/notext/22.webp)

Kemudian klik tombol "*Top-up with Lightning*".
![MULLVAD VPN](assets/notext/23.webp)

Untuk menyelesaikan pembelian, bayar faktur dengan dompet Lightning Anda.
![MULLVAD VPN](assets/notext/24.webp) 

Jika Anda memilih untuk membeli Voucher, di situs Mullvad, pilih "*Voucher*" di antara metode pembayaran yang tersedia di akun Anda. Kemudian, masukkan nomor Voucher yang Anda terima dari situs vpn.sovereign.engineering di kolom yang ditentukan.
![MULLVAD VPN](assets/notext/25.webp) 

## Bagaimana cara menggunakan dan mengkonfigurasi Mullvad VPN?
Kini, setelah Anda memiliki akun yang aktif dan telah memasukkan nomor akun Anda di perangkat lunak atau aplikasi Mullvad, Anda dapat sepenuhnya menikmati layanan VPN Anda.
![MULLVAD VPN](assets/notext/26.webp)

Untuk memutuskan koneksi dari VPN, cukup klik tombol "*Disconnect*".
![MULLVAD VPN](assets/notext/27.webp)

Panah merah kecil di sebelah tombol "*Disconnect*" memungkinkan Anda untuk mengganti server tanpa mengubah lokasi saat ini.
![MULLVAD VPN](assets/notext/28.webp)

Jika Anda ingin mengganti kota untuk server VPN Anda, klik pada "*Switch location*" untuk memilih lokasi baru.
![MULLVAD VPN](assets/notext/29.webp)

Di bagian atas layar, Anda akan melihat nama panggilan perangkat Anda serta durasi sisa paket Anda.
![MULLVAD VPN](assets/notext/30.webp)

Dengan mengklik pada ikon orang kecil, Anda akan mengakses informasi detail tentang akun Anda.
![MULLVAD VPN](assets/notext/31.webp)

Untuk mengakses pengaturan, klik ikon roda gigi.
![MULLVAD VPN](assets/notext/32.webp)

Di menu "*User interface settings*" (Pengaturan antarmuka pengguna), Anda dapat menyesuaikan pengaturan perangkat lunak Anda, termasuk bahasa antarmuka dan pola pengaturan pada sistem Anda.
![MULLVAD VPN](assets/notext/33.webp)

Di menu "*VPN settings*" (pengaturan VPN), Anda akan menemukan berbagai opsi terkait VPN Anda. Saya menyarankan untuk mengaktifkan opsi "Launch app on start-up" (luncurkan aplikasi saat startup) dan "Auto-connect" (sambungkan otomatis) agar koneksi VPN Anda otomatis aktif saat perangkat Anda menyala.
![MULLVAD VPN](assets/notext/34.webp)

Di submenu "*DNS content blockers*", Anda memiliki opsi untuk menyaring dan memblokir permintaan DNS ke situs web berbahaya, iklan, atau yang tidak diinginkan.
![MULLVAD VPN](assets/notext/35.webp)

Akhirnya, menu "*Split tunneling*" memungkinkan Anda untuk memilih aplikasi tertentu di perangkat Anda yang lalu lintas internetnya tidak akan dialihkan melalui VPN.
![MULLVAD VPN](assets/notext/36.webp)

Untuk mendapatkan gambaran umum akun tentang Mullvad Anda dan mengelola berbagai perangkat yang terhubung, Anda dapat mengeklik menu "*Devices*" (Perangkat) di situs web.
![MULLVAD VPN](assets/notext/37.webp)

Dan dengan ini, sekarang Anda sudah siap untuk menikmati Mullvad VPN sepenuhnya. Jika Anda tertarik untuk menemukan penyedia VPN lain yang mirip dengan Mullvad, baik dari segi fitur maupun harga, saya juga merekomendasikan untuk melihat tutorial kami tentang IVPN:

https://planb.network/tutorials/computer-security/communication/ivpn-5a0cd5df-29f1-4382-a817-975a96646e68
