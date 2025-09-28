---
name: GrapheneOS

description: Sistem operasi seluler yang berfokus pada keamanan dan privasi berbasis Android
---

![cover](assets/cover.webp)
> [GrapheneOS](https://grapheneos.org/) adalah sistem operasi seluler open source nirlaba yang dirancang untuk memberikan tingkat privasi dan keamanan yang tinggi sambil tetap sepenuhnya kompatibel dengan aplikasi Android.

GrapheneOS, yang awalnya didirikan pada tahun 2014 sebagai 'CopperheadOS', berbasis pada Kode Android tradisional (AOSP), namun dengan banyak perubahan dan peningkatan yang bertujuan untuk meningkatkan privasi dan keamanan pengguna. GrapheneOS memberikan kontrol kepada pengguna atas telepon mereka, bukan kepada perusahaan teknologi besar.

![video](https://youtu.be/VnumtalYLFI)

### Sommaire:

- Pengantar
- Persiapan
- Instalasi
- Alternatif Aplikasi
- Kekurangan
- Info Berguna

*Tutorial ini merupakan adaptasi dari konten asli yang diterbitkan oleh [BitcoinQnA di Bitcoiner.Guide di bawah lisensi MIT](https://github.com/BitcoinQnA/Bitcoiner.Guide/blob/main/grapheneos.md), yang sepenuhnya berhak atas penghargaan untuk penulisan awal.*

## Mengapa menggunakan GrapheneOS?

Ponsel modern adalah perangkat pelacak dan pengumpul data seharga $500-$1000. Setiap aspek kehidupan kita berjalan melaluinya, dan sayangnya banyak dari data ini dibagikan kepada pihak ketiga dalam satu bentuk atau lainnya.

Ponsel modern adalah perangkat pelacak dan pengumpul data seharga $500-$1000. Setiap aspek kehidupan kita berjalan melaluinya, dan sayangnya sebagian besar data ini dibagikan kepada pihak ketiga dalam satu atau lain bentuk. GrapheneOS dibuat khusus untuk mengurangi pembagian data ini dan meningkatkan keamanan perangkat Anda dari metode-metode serangan berbahaya. Tidak ada yang namanya akun GrapheneOS. Anda tidak memerlukannya untuk mengunduh aplikasi atau berinteraksi dengan OS. Sederhananya, Anda bukanlah produknya.

GrapheneOS memberikan keamanan tambahan pada pengunaan Android Anda melalui beberapa prinsip inti yang sederhana.

1. **Pengurangan serangan awal** - Menghapus kode yang tidak perlu (atau bloatware).
2. **Pencegahan paparan kerentanan** - Memungkinkan pengguna memiliki kendali yang cukup untuk memilih kelonggaran yang nyaman bagi mereka.
3. **Pembatasan sandbox** -GrapheneOS memperkuat sandbox Android yang ada, lebih lanjut mengunci kemampuan setiap aplikasi untuk berkomunikasi dengan bagian lain dari ponsel Anda.

Pelajari lebih lanjut tentang detail teknis semua fitur GrapheneOS [di sini](https://grapheneos.org/features).

### Mempermudah Transisi

Jika Anda sudah bertahun-tahun tenggelam dalam ekosistem Google atau Apple, gagasan kehilangan semua kenyamanan itu dalam semalam bisa jadi menakutkan. Namun, dengan melakukan instalasi aplikasi dengan cermat (akan dibahas nanti), sebagian besar kesulitan yang diperkirakan ini bisa dikurangi atau dihilangkan.

Sebagus apa pun alternatif yang bermunculan, gagasan tentang perubahan semacam itu masih bisa membuat keengganan. Jika Anda menemukan diri dalam situasi ini, saran terbaik saya adalah menggunakan perangkat GrapheneOS baru Anda secara paralel dengan ponsel lama Anda untuk sementara waktu. Dari sana, Anda bisa perlahan-lahan melepaskan diri dari 2-3 aplikasi per minggu hingga Anda menyadari hanya menggunakan perangkat GrapheneOS Anda.

Jika Anda mengambil pendekatan ini, bersikaplah tegas pada diri sendiri dan hentikan ketergantungan Anda pada alternatif yang memantau data secepat mungkin. Kita sebagai manusia cenderung malas dan sering memilih jalan termudah. Ingatlah mengapa Anda membuat keputusan untuk beralih sejak awal.

**Alih-alih membayar dengan data pribadi Anda, Anda memilih untuk membayar dengan waktu Anda, dan terkadang dengan uang hasil jerih payah Anda (tergantung pada aplikasi alternatif yang Anda instal).**

## Memulai

GrapheneOS saat ini hanya diproduksi untuk _(agak ironis)_ lini ponsel [Google Pixel](https://grapheneos.org/faq#supported-devices). Namun, ini bukan tanpa alasan yang kuat. Ponsel Pixel menawarkan keamanan berbasis hardware terbaik untuk melengkapi upaya penguatan OS. Ini mencakup hal-hal seperti isolasi komponen spesifik dan verified boot.

### Memilih perangkat

Saat memilih ponsel Pixel yang ingin Anda instal GrapheneOS, pastikan Anda memeriksa berapa lama perangkat tersebut akan terus mendapatkan [pembaruan keamanan](https://support.google.com/pixelphone/answer/4457705?hl=en#zippy=%2Cpixel-xl-a-a-g-a-g) standar.

Pada saat penulisan ini, Pixel 6a adalah model termurah yang tersedia dengan dukungan jangka panjang yang baik, dijamin hingga Juli 2027. Jika Anda memilih model ini, pembukaan kunci OEM tidak akan berfungsi dengan versi OS bawaan dari pabrik. Anda perlu memperbaruinya ke rilis Juni 2022 atau yang lebih baru melalui pembaruan over-the-air. Setelah diperbarui, Anda juga perlu melakukan factory reset perangkat untuk memperbaiki pembukaan kunci OEM. Semua model lain yang tidak terkunci operator akan siap untuk GrapheneOS langsung dari kotak.

Saat memilih perangkat, Anda juga ingin memastikan membeli versi yang tidak terkunci (unlocked). Operator tertentu seperti Verizon mengirimkan unit mereka yang bootloader-nya terkunci, yang sepenuhnya mencegah proses selanjutnya.

### Memasang GrapheneOS

GrapheneOS [web installer](https://grapheneos.org/install/web) membuat seluruh proses menjadi sangat mudah, dan bisa diselesaikan oleh siapa saja dalam waktu kurang dari 10 menit.
Instruksi berikut adalah versi ringkas yang diambil dari tautan di atas.

Yang Anda butuhkan adalah:
- Ponsel Pixel
- Kabel USB untuk menghubungkan telepon ke komputer Anda
- Komputer untuk menjalankan browser web (browser berbasis Chromium: Chrome, Edge, Brave, dll.)

1. Langkah pertama adalah pergi ke **Settings** > **About phone** dan ketuk berulang kali nomor build sampai Anda melihat **'Developer Mode'** diaktifkan.
2. Selanjutnya pergi ke **Settings** > **System** > **Developer Options** dan aktifkan **'OEM Unlocking'**.
3. Sekarang reboot perangkat dan tahan tombol volume bawah saat telepon sedang menyala kembali.
4. Hubungkan telepon ke laptop Anda dan jika diminta otorisasi, izinkan koneksi.
5. Di halaman web installer, klik 'Unlock the bootloader'.
6. Anda kemudian akan melihat opsi ponsel berubah. Gunakan tombol volume untuk mengubah seleksi menjadi `unlock` dan tekan tombol power untuk menerima.
7. Selanjutnya klik unduh rilisan di halaman web installer.
8. Setelah sepenuhnya diunduh, lanjutkan ke langkah berikutnya dan klik 'Flash release'. Ini akan memakan waktu satu atau dua menit dan Anda tidak perlu menyentuh ponsel sama sekali.
9. Akhirnya, lanjutkan ke langkah berikutnya dari web installer dan klik **Lock Bootloader**. Anda perlu mengubah seleksi dan konfirmasi dengan tombol power dengan cara yang sama seperti yang Anda lakukan sebelumnya dalam proses.
10. Ketika Anda melihat kata `Start`, konfirmasi ini dengan tombol power dan perangkat akan boot ke sistem operasi baru Anda tanpa Google.
    
![image](assets/fr/2.webp)

Layar awal GrapheneOS

_Anda mungkin juga ingin mengambil langkah ekstra, opsional tetapi direkomendasikan, yaitu memverifikasi instalasi melalui aplikasi Auditor. Anda akan membutuhkan ponsel Android terpisah yang sudah terinstal aplikasi tersebut untuk menyelesaikan langkah ini. Instruksi lengkap untuk ini dapat ditemukan [di sini](https://attestation.app/tutorial)._

![video](https://www.youtube.com/embed/L1KZWjZVnAw)

Video ini menjelaskan langkah-langkah sederhana di atas

Jika langkah-langkah sederhana tersebut terasa terlalu sulit, Anda bisa mempertimbangkan untuk membeli Pixel dengan perangkat lunak GrapheneOS yang sudah [terinstal sebelumnya](https://ronindojo.io/en/roninmobile). Namun, perlu diingat bahwa Anda memberikan sedikit kepercayaan kepada penyedia tersebut.

### Aplikasi yang Terpasang Sebelumnya

Sekarang setelah pengaturan selesai, Anda mungkin menyadari betapa minimalisnya GrapheneOS saat pertama kali diinstal. Secara default, Anda akan memiliki aplikasi-aplikasi berikut yang terpasang:

![image](assets/fr/3.webp)

Aplikasi bawaan

Dua nama yang mungkin belum Anda kenal adalah 'Auditor' dan 'Vanadium'.
- Aplikasi [Auditor](https://play.google.com/store/apps/details?id=app.attestation.auditor) menggunakan fitur keamanan berbasis perangkat keras (hardware-based security features) untuk memvalidasi identitas sebuah perangkat, serta keaslian dan integritas sistem operasinya. Aplikasi ini akan memverifikasi bahwa perangkat menjalankan sistem operasi bawaan (stock operating system) dengan bootloader yang terkunci, dan bahwa tidak ada manipulasi atau perubahan yang terjadi pada sistem operasi.
- [Vanadium](https://github.com/GrapheneOS/Vanadium) adalah varian dari browser web Chromium yang diperkuat untuk privasi dan keamanan.

## Kustomisasi

Pengaturan ponsel adalah hal yang personal, tetapi berikut adalah beberapa item pertama yang saya ubah ketika menginstal GrapheneOS untuk membuat diri saya merasa lebih nyaman.

### Mengatur wallpaper dan memperbarui tema

Menuju ke Pengaturan > Wallpaper dan Gaya (Wallpaper and Style). Dari sini saya:
- Memperbarui latar belakang layar utama dan layar kunci dengan gambar yang diunduh dari web.
- Memilih warna aksen yang digunakan di seluruh UI.
- Mengaktifkan tema Gelap.

### Menampilkan persentase baterai

Menuju ke **Settings / Pengaturan** > **Battery / Baterai**, kemudian aktifkan **Show battery percentage / Tampilkan persentase baterai** di bilah status.

### Mengimpor kontak

**Dari ponsel Android lain** - Menuju ke aplikasi Kontak dan cari opsi Ekspor ke VCF.

**Dari iOS** - Gunakan aplikasi seperti Export Contacts dan pilih opsi ekspor 'vCard' untuk membuat file VCF. Setelah Anda memiliki file VCF tersebut, Anda bisa memindahkannya ke perangkat GrapheneOS Anda menggunakan opsi penyimpanan eksternal seperti kartu microSD atau USB drive. Jika Anda tidak memiliki salah satu dari itu, Anda bisa memilih untuk membagikan melalui salah satu dari banyak aplikasi yang tercantum di bawah ini.

![image](assets/fr/4.webp)

Layar utama yang dipersonalisasi

## Aplikasi Alternatif

Agar ponsel Anda bisa berfungsi dengan baik, Anda pasti ingin menginstal beberapa aplikasi! Pilihan yang akan saya sertakan di sini karena saya telah menggunakannya sendiri secara pribadi, atau karena sangat direkomendasikan oleh komunitas privasi yang lebih luas. Ada banyak alternatif bagus lainnya yang tidak disebutkan, dan [Awesome Privacy](https://awesome-privacy.xyz) menawarkan daftar aplikasi penjaga privasi yang sangat lengkap untuk semua jenis perangkat.

Hanya karena aplikasi tersebut Perangkat Lunak Bebas dan Open Source (FOSS), bukan berarti aplikasi tersebut bebas dari potensi kebocoran privasi. Gunakan [Exodus](https://reports.exodus-privacy.eu.org/en/) untuk melihat bagaimana kinerja aplikasi pilihan Anda terhadap audit privasi mereka.

### F-Droid

[F-Droid](https://f-droid.org/) adalah katalog aplikasi FOSS (Perangkat Lunak Bebas dan Open Source) yang dapat diinstal untuk Android. Aplikasi ini memudahkan penelusuran, instalasi, dan pembaruan aplikasi di perangkat Anda. Perlu disebutkan bahwa pembaruan melalui F-Droid terkadang bisa lebih lambat dibandingkan dengan toko aplikasi lain. Ini terutama bergantung pada apakah aplikasi ditemukan melalui repositori utama F-Droid atau repositori khusus.

Untuk menginstal F-Droid cukup menuju ke situs web mereka melalui browser di ponsel GrapheneOS Anda dan ketuk unduh. Ini akan mengunduh file `.apk`. Kemudian Anda akan diminta apakah Anda ingin menginstal aplikasi tersebut.

Selain aplikasi yang ditemukan di repositori default F-Droid, banyak proyek open source juga yang memiliki host repositori mereka sendiri yang dapat ditambahkan di pengaturan aplikasi F-Droid. Jika ini terjadi, proyek yang bersangkutan akan memandu Anda melalui langkah-langkah yang sangat sederhana yang diperlukan untuk mencapai ini di situs web mereka.

![image](assets/fr/5.webp)

Layar utama F-Droid

https://planb.network/tutorials/computer-security/data/f-droid-2cd1aae5-7028-4c04-8fbe-95aeaf278ef4

### Aurora Store
[Aurora Store](https://auroraoss.com/) adalah versi FOSS dari Google Play Store. Aurora memiliki tampilan dan nuansa yang sangat mirip dengan Play Store tradisional dan memungkinkan Anda untuk mengunduh dan memperbarui aplikasi apa pun yang biasanya Anda temukan melalui opsi Google.

Fitur utama dari Aurora adalah login anonim. Ini berarti Anda dapat mengunduh aplikasi favorit Anda yang tidak tersedia melalui F-Droid atau APK langsung, tanpa harus login ke akun Google Anda.

Sebelum Anda bergegas menjadikan ini sebagai opsi instalasi default Anda, ingatlah bahwa banyak aplikasi yang kita coba hindari diinstal dari Play Store. Hanya karena mereka dapat diakses dari Aurora tidak mengubah fakta bahwa beberapa mungkin memiliki fitur pelacakan yang tertanam. Tidak selalu mungkin, tetapi kapan pun Anda bisa, carilah alternatif F-Droid sebelum mengunduh melalui Aurora.

Sebelum Anda terburu-buru menjadikan ini opsi instalasi default, ingatlah bahwa banyak aplikasi yang ingin kita hindari dulunya diinstal dari Play Store. Hanya karena aplikasi-aplikasi tersebut dapat diakses dari Aurora, tidak mengubah fakta bahwa beberapa di antaranya mungkin memiliki fitur pelacak yang tertanam. Meskipun tidak selalu memungkinkan, kapan pun Anda bisa, carilah alternatif F-Droid sebelum mengunduh melalui Aurora.

Untuk menginstal Aurora, cukup cari 'Aurora Store' di F-Droid.

Aurora juga memiliki beberapa potensi vektor serangan, karena "akun anonim" sebenarnya dibuat dan dikendalikan oleh Aurora. Mereka secara teori dapat menyajikan pembaruan berbahaya atau mendorong aplikasi ke ponsel Anda, meskipun Anda tetap harus menerima perintah instalasi di perangkat. Aurora juga terkadang memiliki masalah dengan aplikasi yang tidak muncul karena kesalahan pembacaan wilayah dan perangkat. Hal ini biasanya bisa diatasi dengan langkah-langkah di bawah ini.

**Tips Penting** - Terkadang Aurora Store akan mengalami pembatasan kecepatan (rate limiting) yang membatasi kemampuan Anda untuk mencari dan menginstal aplikasi. Untuk mengatasinya, buka **Settings / Pengaturan** > **Apps / Aplikasi** > **Aurora** > **Open by default / Buka secara default**, lalu tambahkan domain `play.google.com`. Sekarang, setiap kali Anda membuka situs web produk atau layanan yang memiliki tautan 'Download via Play Store / Unduh via Play Store'', mengetuk tautan tersebut akan membuka aplikasi di dalam Aurora untuk Anda unduh.

![image](assets/fr/6.webp)

Layar beranda Aurora Store

https://planb.network/tutorials/computer-security/data/aurora-store-b3345da7-1ed1-407e-a9ae-a1c7f0ba9967

### Unduhan APK

Aplikasi di Android juga dapat diunduh dan diinstal melalui file `.apk`. Ini adalah alternatif yang bagus yang tidak memerlukan toko aplikasi pihak ketiga sama sekali; cukup unduh file langsung dari situs web proyek atau layanan, atau repositori GitHub mereka.

Kekurangan dari cara ini adalah Anda tidak mendapatkan pembaruan otomatis, jadi Anda perlu memantau saluran komunikasi layanan tersebut untuk mengetahui rilis baru. Namun, ada proyek hebat bernama Obtainium yang bertujuan untuk mengatasi masalah ini. [Obtainium](https://github.com/ImranR98/Obtainium) memungkinkan Anda untuk menginstal dan memperbarui aplikasi open source langsung dari halaman rilis mereka, dan menerima notifikasi saat rilis baru tersedia.

![image](assets/fr/7.webp)

Layar Utama Obtanium

### Web Apps

Untuk situasi di mana Anda mungkin ingin sesekali menggunakan suatu layanan dan tidak ingin mengunduh aplikasi native, Anda cukup mengakses versi web-nya. Banyak situs web saat ini juga menawarkan dukungan Progressive Web App (PWA). Ini adalah di mana Anda dapat menandai (bookmark) situs web tertentu (misalnya Twitter.com) ke layar utama ponsel Anda. Kemudian, ketika Anda mengetuk ikon tersebut, ia akan terbuka sebagai aplikasi layar penuh tanpa gangguan biasa yang datang dengan pengalaman browser pada umumnya. Anda bisa melihat contoh tampilannya di bawah.

Untuk mencapai ini di Vanadium, browser native GrapheneOS, cukup navigasikan ke situs web pilihan, ketuk tiga titik vertikal di sudut kanan atas layar, lalu ketuk **'Add to Home Screen' (Tambahkan ke Layar Utama)**.

Satu-satunya kekurangan dari cara ini adalah karena ini hanyalah halaman web yang ditandai, Anda tidak akan mendapatkan bentuk notifikasi apa pun. Meskipun beberapa orang mungkin melihatnya sebagai hal yang positif!

![image](assets/fr/8.webp)

Twitter PWA

### Web Browser

Anda tidak akan kesulitan dengan aplikasi bawaan, Vanadium. Aplikasi ini berfungsi identik dengan browser seluler lain yang pernah saya coba, dan saya belum pernah mengalami masalah kompatibilitas.

Untuk saat-saat ketika Anda perlu mengakses situs `.onion` asli Tor, Anda bisa mengunduh APK Tor Browser langsung dari [situs web mereka](https://www.torproject.org/download/#android) atau melalui F-Droid.

### VPN

Untuk melindungi aktivitas online Anda dari penyedia layanan internet (ISP) yang mungkin memata-matai, aplikasi Jaringan Pribadi Virtual (VPN) adalah pilihan yang baik. Sebuah VPN mengirimkan lalu lintas internet Anda melalui terowongan terenkripsi ke alamat IP bersama yang dikendalikan oleh penyedia layanan VPN untuk memastikan aktivitas perangkat Anda tidak dapat dikaitkan dengan Anda.

Berikut dua opsi yang diakui yang memungkinkan Anda membayar layanan dengan Bitcoin tanpa memberikan informasi pribadi apa pun. Keduanya tersedia di F-Droid.

https://planb.network/tutorials/computer-security/communication/ivpn-5a0cd5df-29f1-4382-a817-975a96646e68

https://planb.network/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8

### Pesan

Dalam beberapa tahun terakhir, solusi pesan terenkripsi menjadi sangat banyak. Namun, masalahnya tetap sama: Anda mungkin memiliki opsi terbaik dan paling pribadi yang terinstal di ponsel Anda, tetapi jika tidak ada kontak Anda yang menggunakannya, apa gunanya?

Kebanyakan orang yang tidak tertarik pada ruang privasi kemungkinan besar menggunakan WhatsApp atau iMessage. Yang pertama dapat diunduh melalui Aurora Store, tetapi yang terakhir (iMessage) tidak akan berfungsi di GrapheneOS (tentu saja!).

- [Signal](https://signal.org/) adalah salah satu messenger terenkripsi end-to-end (E2EE) yang lebih populer, yang memiliki rekam jejak kuat dan fitur yang banyak. Signal memerlukan nomor telepon untuk pendaftaran, jadi jika Anda berencana untuk mengobrol dengan orang-orang yang Anda tidak ingin mereka tahu nomor telepon Anda, mungkin carilah beberapa alternatif. Signal harus diunduh melalui Aurora Store.
- [Simplex](https://f-droid.org/en/packages/chat.simplex.app/) adalah messenger E2EE yang relatif baru. Ia tidak memiliki ID pengguna, tidak memerlukan nomor telepon atau informasi pribadi. Orang dapat menemukan Anda dengan memindai kode QR pribadi Anda atau dengan mengunjungi tautan unik Anda. Simplex juga memungkinkan pengguna tingkat lanjut untuk menjalankan server mereka sendiri guna mengurangi ketergantungan pada entitas terpusat. Simplex tidak memiliki aplikasi desktop, sehingga mungkin tidak cocok jika penggunaan multi-perangkat adalah prioritas Anda. Simplex untuk Android tersedia melalui F-Droid.
- [Threema](https://threema.ch/en/faq/libre_installation) menawarkan pengalaman yang mirip dengan Simplex, tetapi sudah ada lebih lama dan sebagai hasilnya, terasa sedikit lebih "sempurna". Threema tidak gratis, lisensi seumur hidup berharga $4.99 dan dapat dibeli dengan Bitcoin. Threema menawarkan aplikasi web dan aplikasi desktop. Aplikasi Android tersedia melalui F-Droid.
- [Telegram FOSS](https://f-droid.org/en/packages/org.telegram.messenger/) adalah fork FOSS tidak resmi dari aplikasi Telegram resmi untuk Android. Telegram memiliki 'obrolan rahasia' E2EE, tetapi opsi default-nya tidak pribadi. Telegram FOSS dapat diunduh dari F-Droid.

![image](assets/fr/9.webp)

Kiri: Threema Kanan: Simplex

https://planb.network/tutorials/computer-security/communication/signal-8dfb5572-6962-4f1c-bfa5-3192da4e9a4e

https://planb.network/tutorials/computer-security/communication/telegram-09ab3cf3-7625-4267-97a1-24e59a9e5943

https://planb.network/tutorials/computer-security/communication/tox-027bc897-8c98-4265-b85b-e78b7ab607f3

https://planb.network/tutorials/computer-security/communication/simplex-chat-7a1efa11-4d0a-49c4-92aa-e18bf22c22b9

https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74

### Media
- [Spotube](https://f-droid.org/packages/oss.krtirtho.spotube/) adalah aplikasi Spotify lintas platform yang tidak memerlukan akun Premium. Spotube tersedia melalui F-Droid.
- [ViMusic](https://f-droid.org/en/packages/it.vfsfitvnm.vimusic/) adalah aplikasi fantastis untuk streaming musik apa pun dari YouTube Music secara gratis. ViMusic tersedia dari F-Droid.
- [Newpipe](https://f-droid.org/packages/org.schabi.newpipe/) menawarkan pengalaman YouTube tanpa iklan yang mengganggu dan izin yang meragukan. Dengan NewPipe Anda dapat berlangganan saluran, mendengarkan di latar belakang, dan bahkan mengunduh untuk ditonton secara offline. NewPipe dapat diakses melalui F-Droid.
- [AntennaPod](https://f-droid.org/packages/de.danoeh.antennapod/) adalah pemutar podcast yang memungkinkan Anda untuk berlangganan dan mengelola semua acara favorit Anda. AntennaPod tersedia melalui F-Droid.

![image](assets/fr/11.webp)

Kiri: Spotube
Kanan: ViMusic

### Peta

Jika Anda ingin bantuan suara saat mengemudi dan menggunakan aplikasi peta di GrapheneOS, Anda perlu menginstal [RHVoice](https://rhvoice.org/installation/) dan [mengonfigurasinya](https://discuss.grapheneos.org/d/2488-organic-maps-app-voice-instructions-are-not-available).

- [Magic Earth](https://www.magicearth.com/) adalah alternatif peta yang mendukung navigasi belokan demi belokan, peta 3D dan offline. Magic Earth dapat diunduh dari Aurora Store.
- [Organic Maps]((https://f-droid.org/en/packages/app.organicmaps/)) merupakan alternatif aplikasi peta yang dirancang bagi para pelancong, wisatawan, pendaki, dan pesepeda. Aplikasi ini dikembangkan berdasarkan data OpenStreetMap yang dihimpun dari kontribusi komunitas (crowd-sourced). Organic Maps adalah turunan (fork) open-source dari aplikasi Maps.me (yang sebelumnya dikenal sebagai MapsWithMe). Aplikasi ini mendukung seluruh fiturnya tanpa memerlukan koneksi internet aktif dan tersedia untuk diunduh melalui F-Droid.
- [OsmAnd](https://f-droid.org/en/packages/net.osmand.plus/) adalah alternatif peta lain yang mendukung semua fitur yang disebutkan di atas.

![image](assets/fr/13.webp)

Kiri: Magic Earth
Kanan: Organic Maps

### Email

- [Proton Mail](https://proton.me/mail) menawarkan layanan email pribadi gratis yang mendukung E2EE yang diaudit. Proton juga menawarkan versi berbayar yang mendukung domain khusus dan [aliasing](https://proton.me/support/creating-aliases). Proton Mail dapat diunduh sebagai APK langsung atau melalui Aurora.
- [Tutanota](https://tutanota.com/) menawarkan fitur yang sama dengan Proton Mail, termasuk layanan berbayar opsional dan dapat diunduh sebagai APK langsung atau melalui F-Droid.
- [K-9 Mail](https://f-droid.org/en/packages/com.fsck.k9/) adalah aplikasi email open source yang bekerja dengan hampir sama seperti penyedia email. Mendukung beberapa akun, kotak masuk terpadu, dan standar enkripsi OpenPGP.

![image](assets/fr/15.webp)

Kiri: Proton Mail
Kanan: Tutanota

### Produktivitas

- [Syncthing](https://f-droid.org/packages/com.nutomic.syncthingandroid/) adalah program sinkronisasi file. Aplikasi ini menyinkronkan file antara dua atau lebih perangkat secara real-time, terlindungi dengan aman dari pihak yang mengintai. Data Anda sepenuhnya milik Anda, dan Anda berhak memilih di mana data itu disimpan, apakah dibagikan dengan pihak ketiga, dan bagaimana data itu ditransmisikan melalui internet. Syncthing tersedia melalui F-Droid.
- [KDE Connect](https://f-droid.org/packages/org.kde.kdeconnect_tp/) menghubungkan semua perangkat Anda agar dapat berkomunikasi dengan mudah satu sama lain saat terhubung ke jaringan rumah Anda. Aplikasi ini memudahkan pengiriman file, foto, dan data clipboard antar semua perangkat Anda (bahkan di iOS!). KDE Connect dapat diunduh dari F-Droid.
- [Notesnook](https://f-droid.org/en/packages/com.streetwriters.notesnook/) adalah aplikasi catatan terenkripsi end-to-end (E2EE) untuk menyinkronkan ide dan daftar tugas Anda di seluruh perangkat. Paket gratisnya seharusnya mencukupi untuk sebagian besar kebutuhan penggunaan pribadi. Notesnook tersedia di F-Droid.
- [Standard Notes](https://f-droid.org/en/packages/com.standardnotes/) sangat mirip dengan Notesnook, tetapi memerlukan paket berbayar untuk dapat menggunakan seluruh fiturnya. Standard Notes tersedia melalui F-Droid.
- [Anysoft Keyboard](https://f-droid.org/packages/com.menny.android.anysoftkeyboard/) adalah aplikasi papan ketik (keyboard) yang memungkinkan Anda menyesuaikan hampir semua hal terkait pengalaman mengetik di ponsel Anda. Aplikasi ini dapat diunduh melalui F-Droid.
- [GBoard](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin&hl=en&gl=US) adalah aplikasi keyboard bawaan dari Google. Menurut pengalaman saya, GBoard menawarkan pengalaman mengetik dan menggeser terbaik. Jika Anda mengunduh aplikasi ini, pastikan Anda sepenuhnya menonaktifkan semua izin terkait jaringan. Dapat diunduh melalui Aurora.

![image](assets/fr/17.webp)

Kiri: Notesnook
Kanan: KDE Connect

### Gaya Hidup

- [Geometric Weather](https://f-droid.org/en/packages/wangdaye.com.geometricweather/) adalah aplikasi cuaca Open Source yang dirancang dengan indah dan tersedia melalui F-Droid. Ini juga mendukung berbagai ukuran widget sehingga Anda dapat melihat cuaca di lokasi pilihan Anda langsung dari layar utama Anda.
- [Translate You](https://f-droid.org/packages/com.bnyro.translate/) adalah aplikasi penerjemahan Open Source dan menjaga privasi yang mendukung lebih dari 200 bahasa. Translate You tersedia melalui F-Droid.
- [Proton Calendar](https://proton.me/calendar/download) adalah E2EE yang mudah digunakan dan berinteraksi dengan mulus dengan akun email Proton Anda. Proton Calendar dapat diunduh sebagai APK atau melalui toko Aurora.
- [PassAndroid](https://f-droid.org/en/packages/org.ligi.passandroid/) adalah aplikasi yang dirancang untuk menampilkan dan menyimpan berbagai jenis tiket digital, seperti boarding pass, kupon, tiket bioskop, dan kartu keanggotaan. Cukup unduh file `pkpass` atau `espass` yang relevan, lalu buka dengan aplikasi ini. PassAndroid tersedia melalui F-Droid.

![image](assets/fr/19.webp)

Kiri: Geometric Weather
Kanan: Proton Calendar

### Keamanan/Privasi

- [Bitwarden](https://mobileapp.bitwarden.com/fdroid/) menyediakan solusi pengelola kata sandi terenkripsi end-to-end (E2EE) lintas platform secara gratis untuk semua perangkat Anda. Layanan berbayar mereka memungkinkan Anda mengintegrasikan kode otentikasi dua faktor (2FA) langsung ke dalam aplikasi. Bagian server Bitwarden dapat di-hosting sendiri (self-hosted), dan aplikasi Android-nya tersedia melalui F-Droid.
- [Proton Pass](https://proton.me/pass/download) menawarkan layanan gratis serupa dengan Bitwarden, tetapi pelanggan [Proton Unlimited](https://proton.me/pricing) dapat mengakses fitur-fitur lanjutan tambahan. Proton Pass tersedia melalui APK atau Aurora.
- [FreeOTP](https://f-droid.org/packages/org.fedorahosted.freeotp/) adalah aplikasi autentikasi dua faktor untuk sistem yang menggunakan protokol kata sandi sekali pakai. Token dapat dengan mudah ditambahkan dengan memindai kode QR. FreeOTP tersedia melalui F-Droid.
- [Aegis](https://f-droid.org/en/packages/com.beemdevelopment.aegis/) adalah aplikasi gratis, aman, dan Open Source untuk Android untuk mengelola token verifikasi 2-langkah untuk layanan online Anda. Aegis tersedia melalui F-Droid.
- [Cryptomator](https://f-droid.org/en/packages/org.cryptomator.lite/) adalah layanan berbayar, lintas platform yang mengenkripsi data Anda secara lokal sehingga Anda dapat dengan aman mengunggahnya ke layanan cloud favorit Anda. Cryptomator dapat diunduh melalui F-Droid.

![image](assets/fr/21.webp)

Kiri: Proton Pass
Kanan: Bitwarden

https://planb.network/tutorials/computer-security/authentication/ente-auth-1928e65a-3b43-40f3-9efd-457ee2d79bb9

https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

https://planb.network/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc

https://planb.network/tutorials/computer-security/data/cryptomator-84e52c76-2253-49fe-81da-e05e90c28d0d

### Solusi Cloud

- [Proton Drive](https://proton.me/drive/download) adalah solusi cloud E2EE berbayar untuk membackup dan menyimpan semua file Anda. Saat penulisan ini, mereka baru saja mengumumkan aplikasi desktop Windows, tetapi pengguna Mac dan Linux harus terus menggunakan versi web untuk sinkronisasi dari komputer mereka (untuk saat ini). Aplikasi Android tersedia sebagai APK atau melalui Aurora.
- [Skiff](https://skiff.com/download) juga menawarkan penyimpanan cloud E2EE berbayar dan sarana kolaborasi file. Mereka menawarkan Aplikasi desktop Mac dan Windows (serta aplikasi web) dan Aplikasi Android mereka harus diunduh dari Aurora.
- [Nextcloud](https://f-droid.org/en/packages/com.nextcloud.client/) menawarkan solusi berbasis cloud dengan fitur lengkap untuk kolaborasi, sinkronisasi antar perangkat, dan penyimpanan file. Pengguna yang lebih mahir dapat memilih untuk melakukan self-host perangkat lunak gratis dan open source (FOSS) mereka sendiri pada perangkat keras apa pun yang diinginkan. Aplikasi Android-nya dapat diunduh melalui F-Droid.
- [Cryptpad](https://cryptpad.fr/) menawarkan alternatif berbasis web, E2EE, gratis untuk Google Docs.

![image](assets/fr/23.webp)

Proton Drive

https://planb.network/tutorials/computer-security/data/proton-drive-03cbe49f-6ddc-491f-8786-bc20d98ebb16

## Kekurangan

Alternatif Open Source dan yang menjaga privasi dari aplikasi raksasa teknologi yang telah Anda biasa gunakan kini sangat banyak, dan beberapa di antaranya bahkan seringkali lebih baik dibandingkan alternatif closed source yang sarat spyware.

Namun, ketika beralih ke GrapheneOS, ada beberapa kenyamanan yang harus Anda relakan karena tidak ada alternatifnya. Ini termasuk:
- **Apple CarPlay/Android Auto** - Anda harus tetap menggunakan Bluetooth, USB, atau Aux yang baik dan lama.
- **Apple/Google Pay** - Hampir semua orang tetap membawa dompet mereka!
- **Aplikasi perbankan** - Bukan berarti aplikasi ini tidak berfungsi sama sekali. Beberapa di antaranya berfungsi sempurna. Yang lain hanya berfungsi jika Google Play Services diaktifkan (baca lebih lanjut di bawah), dan ada pula yang sama sekali tidak berfungsi. Periksa laporan mengenai bank Anda [di sini](https://privsec.dev/posts/android/banking-applications-compatibility-with-grapheneos/) untuk melihat status terkini. Jangan khawatir jika bank Anda termasuk dalam daftar yang tidak berfungsi; ingatlah bahwa Anda selalu dapat menyimpan URL-nya sebagai aplikasi web di layar utama ponsel Anda.
- **Push Notifications** - Sebagian besar aplikasi yang mengirimkan pembaruan saat Anda tidak menggunakan aplikasi tersebut dilakukan melalui Google Play Services. Layanan ini tidak terinstal secara default di GrapheneOS. Jadi, jika Anda tidak langsung menerima notifikasi saat teman mengirim email, kemungkinan besar inilah alasannya. Kabar baiknya adalah beberapa aplikasi yang disebutkan di atas telah mengimplementasikan koneksi latar belakang mereka sendiri untuk secara berkala memeriksa pembaruan dan kemudian memberikan notifikasi yang diperlukan.

### Sandboxed Google Play

**Perlu diperhatikan:** GrapheneOS memiliki lapisan kompatibilitas yang memungkinkan Anda menginstal dan menggunakan rilis resmi Google Play di sandbox aplikasi standar. Google Play sama sekali tidak mendapatkan akses atau hak istimewa khusus di GrapheneOS, berbeda dengan sistem lain yang bisa melewati sandbox aplikasi dan mendapatkan akses istimewa dalam jumlah besar.

Jika Anda merasa tidak bisa hidup tanpa notifikasi otomatis (push  notification ) untuk aplikasi favorit Anda atau aplikasi tertentu "tidak berguna" tanpa Layanan Google Play, GrapheneOS memungkinkan Anda [menginstal](https://grapheneos.org/usage#sandboxed-google-play-installation) layanan ini dalam lingkungan yang sepenuhnya terisolasi. Setelah terinstal, layanan ini tidak memerlukan akun Google untuk berfungsi, dan setiap izinnya dapat dikontrol dengan ketat.

Sebelum Anda terburu-buru menginstalnya di hari pertama, saya sangat menyarankan Anda untuk melihat seberapa jauh Anda bisa bertahan tanpanya. Anda mungkin akan terkejut betapa banyak aplikasi yang berfungsi normal tanpa layanan tersebut.

Jika Anda tetap ingin menginstalnya, cukup ketuk aplikasi 'Apps' yang sudah terinstal, lalu pilih 'Google Play Services'. Pertimbangkan untuk menginstalnya bersama aplikasi yang kurang menjaga privasi yang tidak bisa Anda tinggalkan, di dalam profil pengguna yang sama sekali terpisah. Ini akan memberikan lapisan pemisahan ekstra dari bagian lain ponsel Anda.

![image](assets/fr/24.webp)

Layar instalasi Layanan Play

### Profil

GrapheneOS memungkinkan Anda memiliki pengalaman ponsel yang terpisah, di dalam ponsel Anda sendiri. Profil tambahan ini dapat menginstal aplikasi dan layanan mereka sendiri, serta tidak dapat mengakses file atau data apa pun dari akun pemilik utama. Jika Anda hanya memiliki satu atau dua aplikasi yang "wajib ada" dan memerlukan Play Services, namun jarang digunakan, menginstal aplikasi tersebut bersama Play Services dalam profil terpisah mungkin merupakan ide bagus untuk semakin memperkuat implikasi privasi kecil sekalipun yang mungkin timbul akibat menjalankannya di profil pemilik.

Anda dapat membaca lebih lanjut tentang kasus penggunaan ini [di sini](https://discuss.grapheneos.org/d/168-ideas-for-user-profiles/2).

Jika Anda memutuskan untuk menambahkan profil terpisah sesuai kebutuhan Anda, aplikasi [Insular](https://f-droid.org/en/packages/com.oasisfeng.island.fdroid/) mungkin akan sangat berguna. Insular memungkinkan Anda untuk dengan mudah menggandakan aplikasi yang sudah ada ke profil baru tanpa perlu melalui rute instalasi tradisional yang dibahas sebelumnya dalam panduan ini. Selain itu, Insular juga memungkinkan Anda untuk dengan cepat 'membekukan' aplikasi-aplikasi tersebut untuk menonaktifkan sepenuhnya semua layanan latar belakang aplikasi dari berjalan.

![image](assets/fr/24.webp)

Layar manajemen profil pengguna

### e-SIM

Jika Anda ingin meningkatkan privasi ponsel Anda ke tingkat berikutnya dan memiliki layanan seluler yang terlepas dari identitas dunia nyata Anda, eSIM mungkin cocok untuk Anda. eSIM adalah SIM virtual yang bisa Anda beli online dan tambahkan ke ponsel Anda melalui kode QR. Perusahaan yang menawarkan layanan semacam ini dan dapat dibayar secara anonim dengan Bitcoin antara lain [Silent.Link](https://silent.link/) dan [Bitrefill](https://www.bitrefill.com/gb/en/esims/).

Namun, eSIM tidak boleh dianggap sebagai solusi lengkap untuk privasi ponsel. Mereka bisa menjadi alat yang berguna di tangan yang tepat, tetapi silakan lakukan riset Anda mengenai [tradeoff](https://grapheneos.org/faq#cellular-tracking) penggunaan jenis layanan seluler apa pun jika tujuan Anda adalah untuk sepenuhnya "lepas dari jaringan" (off grid).

Layanan Play yang terisolasi harus diinstal untuk penyediaan eSIM di GrapheneOS.

## Cadangan

Setelah Anda selesai menyiapkan ponsel Pixel "bebas Google" Anda, ada baiknya Anda membuat cadangan. Cadangan ini akan memungkinkan Anda mengembalikan ponsel ke kondisi yang sama persis jika ponsel hilang atau dicuri.

Anda dapat memilih untuk menyimpan file cadangan ke media penyimpanan eksternal mana pun, atau ke solusi cloud yang di-hosting sendiri seperti Nextcloud. Meskipun demikian, beberapa pengguna melaporkan tingkat keberhasilan yang bervariasi dengan opsi terakhir ini.

Untuk membuat cadangan pertama Anda:

1. Buka **Settings  / Pengaturan** > **System / Sistem** > **Back Up / Cadangan**, kemudian tulis kode pemulihan 12 kata Anda. Kode ini diperlukan untuk mendekripsi file cadangan pada suatu saat nanti. Kehilangan kode, kehilangan akses ke cadangan ponsel Anda.
2. Selanjutnya pilih lokasi penyimpanan Anda. Saya akan merekomendasikan drive USB eksternal atau Kartu microSD industrial.
3. Pilih data yang akan dicadangkan. Jika ruang penyimpanan pada media yang Anda tentukan mencukupi, saya sarankan untuk memilih semuanya.
4. Ketuk tiga titik di kanan atas, dan pilih **Backup now / Cadangkan sekarang**.

![gambar](assets/fr/26.webp)

Layar Cadangan

Ingatlah, jika Anda membuat cadangan offline ke media penyimpanan eksternal, penting untuk melakukan langkah ini secara rutin. Ini akan memastikan pembaruan penting terbaru pada ponsel Anda tidak hilang jika terjadi hal terburuk.

![video](https://www.youtube.com/embed/eyWmcItzisk)

Video yang menjelaskan proses cadangan

## Kesimpulan

Dalam beberapa tahun terakhir, perangkat lunak GrapheneOS telah berkembang pesat. Kini lebih stabil dan kompatibel dari sebelumnya. Ditambah dengan ekosistem aplikasi Open Source dan penjaga privasi yang berkembang pesat, GrapheneOS menjadi alternatif yang benar-benar layak untuk Stock Android atau iOS, bahkan untuk orang "normal" seperti Anda!

Pelanggaran data dan pengawasan massal (dragnet surveillance) sudah menjadi hal yang umum di dunia saat ini sehingga hampir tidak lagi menjadi berita utama. Terserah pada Anda untuk melindungi diri sendiri. Akan ada penyesuaian dan pengorbanan yang harus dilakukan, tetapi mengurangi eksposur Anda terhadap pelanggaran semacam itu tidak sesulit yang Anda kira.

Saya harap panduan ini dapat membantu perjalanan Anda. Jika Anda merasa panduan ini bermanfaat dan ingin mendukung pekerjaan saya, silakan pertimbangkan untuk mengirimkan donasi.

Jika Anda adalah pengguna GrapheneOS yang sudah ada, atau menjadi salah satunya karena panduan ini, pertimbangkan untuk [berdonasi](https://grapheneos.org/donate) guna mendukung pekerjaan penting mereka.

### Pelajari lebih lanjut

GrapheneOS adalah sebuah "lubang kelinci" (rabbit hole) yang bisa dengan mudah membuat siapa pun menghabiskan waktu berminggu-minggu untuk mendalaminya. Ada begitu banyak yang bisa Anda pelajari dan utak-atik untuk menyesuaikan pengalaman dengan kebutuhan dan model ancaman Anda. Berikut adalah beberapa tautan di mana Anda dapat melanjutkan perjalanan Anda:

- [Panduan Penggunaan Resmi GrapheneOS](https://grapheneos.org/usage) - Situs Web Resmi
- [Forum GrapheneOS](https://discuss.grapheneos.org/) - Situs Web Resmi
- [Kelas Master Pengaturan GrapheneOS](https://www.youtube.com/watch?app=desktop&v=GLJyD9MJgIQ) - Video oleh 'The Privacy Wayfinder'
- [Podcast Umum GrapheneOS](https://www.youtube.com/watch?app=desktop&v=UCPX0mFFRNA) - Podcast oleh 'Watchman Privacy'

*Tutorial ini merupakan adaptasi dari konten asli yang diterbitkan oleh [BitcoinQnA di Bitcoiner.Guide di bawah lisensi MIT](https://github.com/BitcoinQnA/Bitcoiner.Guide/blob/main/grapheneos.md), yang sepenuhnya berhak atas penghargaan untuk penulisan awal.*


