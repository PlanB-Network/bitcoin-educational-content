---
name: GrapheneOS

description: Tutorial Graphene OS
---

> "[GrapheneOS](https://grapheneos.org/) adalah sistem operasi mobile yang fokus pada privasi dan keamanan dengan kompatibilitas aplikasi Android, dikembangkan sebagai proyek open source nirlaba."

GrapheneOS, yang awalnya didirikan pada tahun 2014 sebagai 'CopperheadOS', berbasis pada Kode Android tradisional (AOSP), namun dengan banyak perubahan dan peningkatan yang bertujuan untuk meningkatkan privasi dan keamanan pengguna. GrapheneOS memberikan kontrol kepada pengguna atas telepon mereka, bukan kepada perusahaan teknologi besar.

### Sommaire:

- Pengantar
- Persiapan
- Instalasi
- Alternatif Aplikasi
- Kekurangan
- Info Berguna

Panduan oleh https://github.com/BitcoinQnA/Bitcoiner.Guide/blob/main/grapheneos.md

## Mengapa menggunakan GrapheneOS?

Ponsel modern adalah perangkat pelacak dan pengumpul data seharga $500-$1000. Setiap aspek kehidupan kita berjalan melaluinya, dan sayangnya banyak dari data ini dibagikan kepada pihak ketiga dalam satu bentuk atau lainnya.
GrapheneOS dibangun khusus untuk mengurangi pembagian data ini dan meningkatkan keamanan perangkat Anda dari vektor serangan potensial. Tidak ada yang namanya akun GrapheneOS. Anda tidak memerlukannya untuk mengunduh aplikasi atau berinteraksi dengan OS. Singkatnya, Anda bukan produknya.

GrapheneOS memberikan keamanan tambahan pada pengalaman Android Anda melalui beberapa prinsip inti yang sederhana.

1. **Pengurangan permukaan serangan** - Menghapus kode yang tidak perlu (atau bloatware).
2. **Pencegahan paparan kerentanan** - Memungkinkan pengguna cukup granularitas untuk memilih kompromi yang mereka nyaman dengan.
3. **Pengurungan sandbox** - GrapheneOS memperkuat sandbox Android yang ada, lebih lanjut mengunci kemampuan setiap aplikasi untuk berkomunikasi dengan sisa telepon Anda.

Pelajari lebih lanjut tentang detail teknis dari set fitur GrapheneOS [di sini](https://grapheneos.org/features).

### Mempermudah Transisi

Jika Anda telah terjebak dalam ekosistem Google atau Apple selama bertahun-tahun, pemikiran kehilangan semua kemudahan itu dalam semalam bisa menjadi hal yang menakutkan. Namun, dengan beberapa keputusan pemasangan aplikasi yang dipertimbangkan dengan baik (dibahas nanti), banyak kesulitan yang diharapkan ini dapat dikurangi atau dihilangkan.

Sebagus apa pun alternatifnya menjadi, pemikiran tentang perubahan seperti itu masih bisa menimbulkan keberatan. Jika Anda menemukan diri Anda dalam situasi ini, saran terbaik saya adalah menjalankan perangkat GrapheneOS baru Anda bersamaan dengan telepon Anda yang ada untuk sementara waktu. Dari sana Anda dapat perlahan-lahan mengurangi ketergantungan Anda pada 2-3 aplikasi per minggu sampai Anda menemukan diri Anda hanya mencapai perangkat GrapheneOS Anda.

Jika Anda mengambil pendekatan ini, bersikaplah ketat dengan diri sendiri dan putuskan ketergantungan Anda pada alternatif yang diawasi secepat mungkin. Kita manusia adalah makhluk yang malas dan sering mengambil jalan dengan hambatan terkecil. Ingatlah mengapa Anda melakukan perubahan ini di tempat pertama.

**Alih-alih membayar dengan data pribadi Anda, Anda memilih untuk membayar dengan waktu Anda, dan terkadang uang Anda yang diperoleh dengan susah payah (tergantung pada aplikasi alternatif yang Anda instal).**

## Memulai

GrapheneOS saat ini hanya diproduksi untuk _(agak ironis)_ jajaran telepon [Google Pixel](https://grapheneos.org/faq#supported-devices). Ini tidak tanpa alasan yang baik. Pixel menawarkan keamanan berbasis perangkat keras terbaik untuk melengkapi pekerjaan yang dilakukan untuk menguatkan OS. Ini termasuk hal-hal seperti isolasi komponen spesifik dan boot yang diverifikasi.

### Memilih perangkat

Saat memilih Pixel yang ingin Anda instal GrapheneOS, pastikan Anda memeriksa berapa lama perangkat akan terus mendapatkan [pembaruan keamanan](https://support.google.com/pixelphone/answer/4457705?hl=en#zippy=%2Cpixel-xl-a-a-g-a-g) secara default.
Saat penulisan ini, Pixel 6a adalah model termurah yang tersedia dengan dukungan jangka panjang yang baik, dijamin hingga Juli 2027. Jika Anda memilih model ini, OEM unlocking tidak akan berfungsi dengan versi OS bawaan dari pabrik. Anda perlu memperbaruinya ke rilis Juni 2022 atau lebih baru melalui pembaruan over-the-air. Setelah Anda memperbaruinya, Anda juga perlu melakukan reset pabrik pada perangkat untuk memperbaiki OEM unlocking. Semua model lain yang tidak terkunci oleh operator akan siap untuk GrapheneOS langsung dari kotak.

Saat memilih perangkat, Anda juga ingin memastikan Anda membeli versi yang tidak terkunci. Beberapa operator seperti Verizon mengirimkan unit mereka yang terkunci bootloader yang sepenuhnya mencegah proses berikut.

### Memasang GrapheneOS

Pemasang web GrapheneOS [web installer](https://grapheneos.org/install/web) membuat seluruh proses menjadi sangat mudah, dan bisa diselesaikan oleh siapa saja dalam waktu kurang dari 10 menit.
Instruksi berikut adalah versi ringkas yang diambil dari tautan di atas.

Yang Anda butuhkan adalah:

- Pixel
- Kabel USB untuk menghubungkan telepon ke komputer Anda
- Komputer untuk menjalankan browser web (browser berbasis Chromium: Chrome, Edge, Brave, dll.)

1. Langkah pertama adalah pergi ke **Settings** > **About phone** dan ketuk berulang kali nomor build sampai Anda melihat **'Developer Mode'** diaktifkan.
2. Selanjutnya pergi ke **Settings** > **System** > **Developer Options** dan aktifkan **'OEM Unlocking'**.
3. Sekarang reboot perangkat dan tahan tombol volume bawah saat telepon sedang menyala kembali.
4. Hubungkan telepon ke laptop Anda dan jika diminta otorisasi, izinkan koneksi.
5. Di halaman web installer, klik 'Unlock the bootloader'.
6. Anda kemudian akan melihat opsi telepon berubah. Gunakan tombol volume untuk mengubah seleksi menjadi `unlock` dan gunakan tombol daya untuk menerima.
7. Selanjutnya klik unduh rilis di halaman web installer.
8. Setelah sepenuhnya diunduh, lanjutkan ke langkah berikutnya dan klik 'Flash release'. Ini akan memakan waktu satu atau dua menit dan Anda tidak perlu menyentuh telepon sama sekali.
9. Akhirnya, lanjutkan ke langkah berikutnya dari web installer dan klik **Lock Bootloader**. Anda perlu mengubah seleksi dan konfirmasi dengan tombol daya dengan cara yang sama seperti yang Anda lakukan sebelumnya dalam proses.
10. Ketika Anda melihat kata `Start`, konfirmasi ini dengan tombol daya dan perangkat akan boot ke sistem operasi baru Anda tanpa Google.

![image](assets/2.webp)

Layar awal GrapheneOS

_Setelah boot awal dan pengaturan, adalah praktik yang baik untuk menonaktifkan OEM unlocking dari Settings > System > Developer Options._

_Anda mungkin juga ingin mengambil langkah tambahan, opsional tapi disarankan untuk memverifikasi instalasi melalui aplikasi Auditor. Anda akan membutuhkan telepon Android terpisah dengan aplikasi terinstal untuk menyelesaikan langkah ini. Instruksi untuk ini dapat ditemukan [di sini](https://attestation.app/tutorial)._

![video](https://www.youtube.com/embed/L1KZWjZVnAw)

Video yang menjelaskan langkah-langkah sederhana di atas

Jika langkah-langkah sederhana tersebut terasa terlalu jauh, Anda bisa mempertimbangkan untuk membeli Pixel dengan perangkat lunak GrapheneOS [terpasang sebelumnya](https://ronindojo.io/en/roninmobile). Hanya perlu diingat bahwa Anda menaruh sedikit kepercayaan pada penyedia.

### Aplikasi yang Terpasang Sebelumnya

Sekarang setelah Anda siap, Anda mungkin memperhatikan betapa kosongnya GrapheneOS tampak pada pemasangan pertama. Secara default Anda akan memiliki aplikasi-aplikasi ini terpasang:

![image](assets/3.webp)

Aplikasi bawaan
Dua istilah yang mungkin belum Anda kenal adalah 'Auditor' dan 'Vanadium'.
- Aplikasi [Auditor](https://play.google.com/store/apps/details?id=app.attestation.auditor) menggunakan fitur keamanan berbasis perangkat keras untuk memvalidasi identitas suatu perangkat bersama dengan keaslian dan integritas sistem operasi. Aplikasi ini akan memverifikasi bahwa perangkat menjalankan sistem operasi bawaan dengan bootloader yang terkunci dan tidak ada manipulasi yang terjadi pada sistem operasi.
- [Vanadium](https://github.com/GrapheneOS/Vanadium) adalah varian dari peramban web Chromium yang diperkuat untuk privasi dan keamanan.

## Kustomisasi

Pengaturan telepon adalah hal yang personal, tetapi berikut adalah beberapa item pertama yang saya ubah ketika menginstal GrapheneOS untuk membuat diri saya merasa lebih nyaman.

### Mengatur wallpaper dan memperbarui tema

Menuju ke Pengaturan > Wallpaper dan Gaya. Dari sini saya:

- Memperbarui latar belakang layar utama dan layar kunci dengan gambar yang diunduh dari web.
- Memilih warna aksen yang digunakan di seluruh UI.
- Mengaktifkan tema Gelap.

### Menampilkan persentase baterai

Menuju ke **Pengaturan** > **Baterai**, kemudian aktifkan **Tampilkan persentase baterai** di bilah status.

### Mengimpor kontak

**Dari telepon Android lain** - Menuju ke aplikasi Kontak dan cari opsi Ekspor ke VCF.

**Dari iOS** - Gunakan aplikasi seperti Export Contact dan gunakan opsi ekspor 'vCard' untuk mengekspor file VCF.
Setelah Anda memiliki file VCF, Anda dapat mentransfernya ke perangkat GrapheneOS Anda dengan opsi penyimpanan eksternal seperti kartu microSD atau USB drive. Jika Anda tidak memiliki salah satu dari itu, Anda bisa memilih untuk berbagi melalui salah satu dari banyak aplikasi yang tercantum di bawah ini.

![image](assets/4.webp)

Layar utama yang dipersonalisasi

## Aplikasi Alternatif

Untuk membuat telepon Anda berguna, Anda akan ingin menginstal beberapa aplikasi! Opsi yang diikuti termasuk karena saya telah menggunakannya secara pribadi atau karena mereka menerima rekomendasi kuat dari komunitas privasi yang lebih luas. Ada banyak alternatif bagus lainnya yang tidak disebutkan, dan [Awesome Privacy](https://awesome-privacy.xyz) menawarkan daftar aplikasi yang menjaga privasi secara luas untuk semua jenis perangkat.

Hanya karena sebuah aplikasi adalah Perangkat Lunak Bebas dan Sumber Terbuka (FOSS) tidak berarti bebas dari potensi kebocoran privasi. Gunakan [Exodus](https://reports.exodus-privacy.eu.org/en/) untuk melihat bagaimana aplikasi pilihan Anda berkinerja terhadap audit privasi mereka.

### F-Droid

[F-Droid](https://f-droid.org/) adalah katalog yang dapat diinstal dari aplikasi FOSS untuk Android. Klien memudahkan untuk menjelajah, menginstal, dan memperbarui aplikasi di perangkat Anda. Penting untuk disebutkan bahwa pembaruan melalui F-Droid terkadang bisa lebih lambat dibandingkan dengan toko aplikasi lain. Ini terutama tergantung pada apakah aplikasi ditemukan melalui repositori utama F-Droid atau yang khusus.

Untuk menginstal F-Droid cukup menuju ke situs web mereka melalui browser di telepon GrapheneOS Anda dan ketuk unduh. Ini akan mengunduh file `.apk`. Kemudian Anda akan diminta apakah Anda ingin menginstal aplikasi tersebut.

Selain aplikasi yang ditemukan dalam repositori default di F-Droid, banyak proyek Sumber Terbuka juga akan menghosting repositori mereka sendiri yang dapat ditambahkan dalam pengaturan aplikasi F-Droid. Jika ini kasusnya, proyek yang bersangkutan akan memandu Anda melalui langkah-langkah yang sangat sederhana yang diperlukan untuk mencapai ini di situs web mereka.

![image](assets/5.webp)

Layar utama F-Droid

### Aurora Store
[Aurora Store](https://auroraoss.com/) adalah versi FOSS dari Google Play Store. Aurora memiliki tampilan dan nuansa yang sangat mirip dengan Play Store tradisional dan memungkinkan Anda untuk mengunduh dan memperbarui aplikasi apa pun yang biasanya Anda temukan melalui opsi Google.
Fitur utama dari Aurora adalah login anonim. Ini berarti Anda dapat mengunduh aplikasi favorit Anda yang tidak tersedia melalui F-Droid atau APK langsung, tanpa harus login ke akun Google Anda.

Sebelum Anda bergegas menjadikan ini sebagai opsi instalasi default Anda, ingatlah bahwa banyak aplikasi yang kita coba hindari diinstal dari Play Store. Hanya karena mereka dapat diakses dari Aurora tidak mengubah fakta bahwa beberapa mungkin memiliki fitur pelacakan yang tertanam. Tidak selalu mungkin, tetapi kapan pun Anda bisa, carilah alternatif F-Droid sebelum mengunduh melalui Aurora.

Untuk menginstal Aurora, cukup cari 'Aurora Store' di F-Droid.

Aurora juga memiliki beberapa vektor serangan potensial, karena "akun anonim" sebenarnya dibuat dan dikontrol oleh Aurora. Mereka bisa, secara teori, menyajikan pembaruan berbahaya atau mendorong aplikasi ke ponsel Anda, meskipun Anda masih harus menerima prompt instalasi di perangkat. Aurora juga terkadang memiliki beberapa masalah dengan aplikasi yang tidak muncul karena kesalahan baca region dan perangkat. Ini biasanya dapat diatasi dengan langkah-langkah di bawah ini.

**Tips teratas** - Terkadang Aurora Store akan mengalami pembatasan laju yang membatasi kemampuan Anda untuk mencari dan menginstal aplikasi. Untuk mengatasi ini, pergi ke **Pengaturan** > **Aplikasi** > **Aurora** > **Buka secara default**, kemudian tambahkan domain `play.google.com`. Sekarang, kapan pun Anda menavigasi ke situs web produk atau layanan yang memiliki tautan 'Unduh via Play Store', mengetuknya akan membuka aplikasi tersebut dalam Aurora untuk Anda unduh.

![image](assets/6.webp)

Layar beranda Aurora Store

### Unduhan APK

Aplikasi di Android juga dapat diunduh dan diinstal melalui file `.apk`. Ini adalah alternatif bagus yang tidak memerlukan toko aplikasi pihak ketiga, cukup unduh file langsung dari situs web proyek atau layanan atau repositori GitHub.

Kekurangan dari pendekatan ini adalah Anda tidak mendapatkan pembaruan otomatis, jadi Anda perlu memantau saluran komunikasi layanan tersebut untuk mengetahui rilis baru. Namun, ada proyek bagus yang disebut Obtanium yang bertujuan untuk memperbaiki ini. [Obtainium](https://github.com/ImranR98/Obtainium) memungkinkan Anda untuk menginstal dan memperbarui aplikasi Open-Source langsung dari halaman rilis mereka, dan menerima notifikasi ketika rilis baru tersedia.

![image](assets/7.webp)

Pratinjau Obtanium

### Web Apps

Untuk saat-saat di mana Anda mungkin ingin menggunakan layanan secara tidak sering dan tidak ingin mengunduh aplikasi asli, Anda dapat mengakses versi webnya. Banyak situs web saat ini juga menawarkan dukungan Progressive Web App (PWA). Di sini Anda dapat mem-bookmark situs web tertentu (misalnya Twitter.com) ke layar beranda ponsel Anda. Kemudian ketika Anda mengetuk ikonnya, itu terbuka sebagai aplikasi layar penuh tanpa gangguan biasa yang datang dengan pengalaman browser tipikal. Anda dapat melihat contoh bagaimana ini terlihat di bawah ini.

Untuk mencapai ini di Vanadium, browser asli GrapheneOS, cukup navigasikan ke situs web pilihan, ketuk tiga titik vertikal di sudut kanan atas layar dan kemudian ketuk **'Tambahkan ke Layar Beranda'**.

Satu-satunya kekurangan dari pendekatan ini adalah karena ini hanya halaman web yang dibookmark, Anda tidak akan mendapatkan bentuk notifikasi apa pun. Meskipun beberapa mungkin melihat itu sebagai hal positif!

![image](assets/8.webp)

Twitter PWA

### Web Browsers
Anda tidak akan salah pilih dengan opsi pra-paket, Vanadium. Aplikasi ini berperilaku identik dengan browser mobile lain yang pernah saya coba dan saya tidak pernah mengalami masalah kompatibilitas.

Untuk saat-saat ketika Anda perlu mengakses situs `.onion` asli Tor, Anda dapat mengunduh APK Tor Browser langsung dari [situs web mereka](https://www.torproject.org/download/#android) atau melalui F-Droid.

### VPN

Untuk melindungi aktivitas online Anda dari penyedia layanan internet (ISP) yang mengintip, aplikasi Jaringan Pribadi Virtual (VPN) adalah pilihan yang baik. VPN mengirimkan lalu lintas internet Anda dalam terowongan terenkripsi ke alamat IP bersama yang dikontrol oleh penyedia layanan VPN untuk memastikan aktivitas perangkat Anda tidak dapat dikaitkan dengan Anda.

Berikut adalah 3 opsi terhormat yang memungkinkan Anda membayar layanan dengan Bitcoin dan tanpa memberikan informasi pribadi apa pun. Semua 3 opsi tersedia melalui F-Droid.

- [Mullvad](https://f-droid.org/packages/net.mullvad.mullvadvpn/)
- [Proton](https://f-droid.org/en/packages/ch.protonvpn.android/)
- [iVPN](https://f-droid.org/en/packages/net.ivpn.client/)

### Pesan

Dalam beberapa tahun terakhir, solusi pesan terenkripsi telah menjadi berlimpah. Masalahnya tetap, Anda dapat memiliki opsi yang terbaik dan paling pribadi terinstal di ponsel Anda, tetapi jika Anda tidak memiliki kontak yang menggunakannya, apa gunanya?

Kebanyakan orang yang tidak tertarik dengan ruang privasi kemungkinan akan menggunakan WhatsApp atau iMessage. Yang pertama dapat diunduh melalui Aurora Store tetapi yang terakhir tidak akan berfungsi di GrapheneOS (tentu saja!).

- [Signal](https://signal.org/) adalah salah satu messenger terenkripsi ujung-ke-ujung (E2EE) yang lebih populer yang memiliki rekam jejak yang kuat dan fitur yang kaya. Signal memerlukan nomor telepon untuk mendaftar, jadi jika Anda berencana untuk mengobrol dengan orang-orang yang sebaiknya tidak mengetahui nomor telepon Anda, mungkin pertimbangkan beberapa alternatif. Signal harus diunduh melalui Aurora Store.
- [Simplex](https://f-droid.org/en/packages/chat.simplex.app/) adalah messenger E2EE yang cukup baru. Tidak memerlukan ID pengguna, tidak memerlukan nomor telepon atau informasi pribadi. Orang menemukan Anda dengan memindai kode QR pribadi Anda atau dengan mengunjungi tautan unik Anda. Simplex juga memungkinkan pengguna lanjutan untuk menjalankan server mereka sendiri untuk lebih mengurangi ketergantungan pada entitas terpusat. Simplex tidak memiliki klien desktop, jadi mungkin tidak cocok jika multi-perangkat ada dalam daftar prioritas Anda. Simplex untuk Android tersedia melalui F-Droid.
- [Threema](https://threema.ch/en/faq/libre_installation) menawarkan pengalaman serupa dengan Simplex, tetapi telah ada lebih lama dan sebagai hasilnya, terasa sedikit lebih terpolis. Threema tidak gratis, lisensi seumur hidup berharga $4.99 dan dapat dibeli dengan Bitcoin. Threema menawarkan klien web dan aplikasi desktop asli. Aplikasi Android tersedia melalui F-Droid.
- [Telegram FOSS](https://f-droid.org/en/packages/org.telegram.messenger/) adalah fork FOSS tidak resmi dari aplikasi Telegram resmi untuk Android. Telegram memiliki 'chat rahasia' E2EE, tetapi opsi default tidak pribadi. Telegram FOSS dapat diunduh dari F-Droid.

![image](assets/9.webp)
Kiri: Threema
Kanan: Simplex

### Media
- [Spotube](https://f-droid.org/packages/oss.krtirtho.spotube/) adalah klien Spotify lintas platform yang tidak memerlukan akun Premium. Spotube tersedia melalui F-Droid.
- [ViMusic](https://f-droid.org/en/packages/it.vfsfitvnm.vimusic/) adalah aplikasi fantastis untuk streaming musik apa pun dari YouTube Music secara gratis. ViMusic tersedia dari F-Droid.
- [Newpipe](https://f-droid.org/packages/org.schabi.newpipe/) menawarkan pengalaman YouTube tanpa iklan yang mengganggu dan izin yang meragukan. Dengan NewPipe Anda dapat berlangganan saluran, mendengarkan di latar belakang, dan bahkan mengunduh untuk ditonton secara offline. NewPipe dapat diakses melalui F-Droid.
- [AntennaPod](https://f-droid.org/packages/de.danoeh.antennapod/) adalah pemutar podcast yang memungkinkan Anda untuk berlangganan dan mengelola semua acara favorit Anda. AntennaPod tersedia melalui F-Droid.

![image](assets/11.webp)

Kiri: Spotube
Kanan: ViMusic

### Peta

Jika Anda ingin bantuan suara saat mengemudi dan menggunakan aplikasi peta di GrapheneOS, Anda perlu menginstal [RHVoice](https://rhvoice.org/installation/) dan [mengonfigurasinya](https://discuss.grapheneos.org/d/2488-organic-maps-app-voice-instructions-are-not-available).

- [Magic Earth](https://www.magicearth.com/) adalah alternatif peta yang mendukung navigasi belokan demi belokan, peta 3D dan offline. Magic Earth dapat diunduh dari Aurora Store.
- [Organic Maps](https://f-droid.org/en/packages/app.organicmaps/) adalah alternatif peta untuk pelancong, turis, pendaki, dan pesepeda berdasarkan data OpenStreetMap yang bersumber dari kerumunan. Ini adalah fork open-source yang berfokus pada privasi dari aplikasi Maps.me (sebelumnya dikenal sebagai MapsWithMe). Mendukung 100% fitur tanpa koneksi Internet aktif dan dapat diunduh dari F-Droid.
- [OsmAnd](https://f-droid.org/en/packages/net.osmand.plus/) adalah alternatif peta lain yang mendukung semua fitur yang disebutkan di atas.

![image](assets/13.webp)

Kiri: Magic Earth
Kanan: Organic Maps

### Email

- [Proton Mail](https://proton.me/mail) menawarkan layanan email pribadi gratis yang mendukung E2EE yang diaudit. Proton juga menawarkan versi berbayar yang mendukung domain kustom dan [aliasing](https://proton.me/support/creating-aliases). Proton Mail dapat diunduh sebagai APK langsung atau melalui Aurora.
- [Tutanota](https://tutanota.com/) menawarkan fitur yang sama dengan Proton Mail, termasuk layanan berbayar opsional dan dapat diunduh sebagai APK langsung atau melalui F-Droid.
- [K-9 Mail](https://f-droid.org/en/packages/com.fsck.k9/) adalah klien email open source yang bekerja dengan hampir setiap penyedia email. Mendukung beberapa akun, kotak masuk terpadu, dan standar enkripsi OpenPGP.

![image](assets/15.webp)

Kiri: Proton Mail
Kanan: Tutanota

### Produktivitas

- [Syncthing](https://f-droid.org/packages/com.nutomic.syncthingandroid/) adalah program sinkronisasi file. Ini menyinkronkan file antara dua atau lebih perangkat secara real-time, terlindungi dengan aman dari pandangan orang lain. Data Anda adalah milik Anda sendiri dan Anda berhak memilih di mana data tersebut disimpan, apakah dibagikan dengan pihak ketiga, dan bagaimana cara data tersebut ditransmisikan melalui internet. Syncthing tersedia melalui F-Droid.
- [KDE Connect](https://f-droid.org/packages/org.kde.kdeconnect_tp/) memungkinkan semua perangkat Anda untuk berkomunikasi satu sama lain dengan mudah ketika terhubung ke jaringan rumah Anda. Dengan mudah kirimkan file, foto, data clipboard ke semua perangkat Anda (bahkan di iOS!). KDE Connect dapat diunduh dari F-Droid.
- [Notesnook](https://f-droid.org/en/packages/com.streetwriters.notesnook/) adalah aplikasi catatan E2EE untuk menyinkronkan pikiran dan daftar tugas Anda di semua perangkat Anda. Paket gratis mereka seharusnya mencakup sebagian besar kasus penggunaan pribadi. Notesnook tersedia di F-Droid.
- [Standard Notes](https://f-droid.org/en/packages/com.standardnotes/) sangat mirip dengan Notesnook, tetapi memerlukan paket berbayar untuk mencocokkan set fiturnya. Standard Notes tersedia melalui F-Droid.
- [Anysoft Keyboard](https://f-droid.org/packages/com.menny.android.anysoftkeyboard/) adalah aplikasi keyboard yang memungkinkan Anda untuk menyesuaikan hampir semua hal yang dapat Anda pikirkan terkait pengalaman mengetik di ponsel Anda. Dapat diunduh melalui F-Droid.
- [GBoard](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin&hl=en&gl=US) adalah aplikasi keyboard default dari Google. Menurut pengalaman saya, ini menawarkan pengalaman mengetik dan menggeser terbaik. Jika Anda mengunduh aplikasi ini, pastikan Anda sepenuhnya menonaktifkan semua izin terkait jaringan. Dapat diunduh melalui Aurora.

![image](assets/17.webp)

Kiri: Notesnook
Kanan: KDE Connect

### Gaya Hidup

- [Geometric Weather](https://f-droid.org/en/packages/wangdaye.com.geometricweather/) adalah aplikasi cuaca Open Source yang dirancang dengan indah dan tersedia melalui F-Droid. Ini juga mendukung berbagai ukuran widget sehingga Anda dapat melihat cuaca di lokasi pilihan Anda langsung dari layar utama Anda.
- [Translate You](https://f-droid.org/packages/com.bnyro.translate/) adalah aplikasi penerjemahan Open Source dan menjaga privasi yang mendukung lebih dari 200 bahasa. Translate You tersedia melalui F-Droid.
- [Proton Calendar](https://proton.me/calendar/download) adalah E2EE yang mudah digunakan dan berinteraksi dengan mulus dengan akun email Proton Anda. Proton Calendar dapat diunduh sebagai APK atau melalui toko Aurora.
- [PassAndroid](https://f-droid.org/en/packages/org.ligi.passandroid/) adalah aplikasi untuk menampilkan dan menyimpan boarding pass, kupon, tiket bioskop dan kartu keanggotaan dll. Cukup unduh file `pkpass` atau `espass` yang relevan dan buka dengan aplikasi. PassAndroid tersedia melalui F-Droid.

![image](assets/19.webp)
Kiri: Geometric Weather
Kanan: Proton Calendar

### Keamanan/Privasi

- [Bitwarden](https://mobileapp.bitwarden.com/fdroid/) menawarkan solusi manajer kata sandi lintas platform E2EE gratis untuk semua perangkat Anda. Layanan berbayar mereka memungkinkan Anda untuk mengintegrasikan kode 2FA ke dalam aplikasi. Sisi server dari Bitwarden dapat di-host sendiri dan aplikasi Android tersedia melalui F-Droid.
- [Proton Pass](https://proton.me/pass/download) menawarkan layanan gratis serupa dengan Bitwarden, tetapi pelanggan [Proton Unlimited](https://proton.me/pricing) dapat mengakses fitur-fitur lanjutan tambahan. Proton Pass tersedia melalui APK atau Aurora.
- [FreeOTP](https://f-droid.org/packages/org.fedorahosted.freeotp/) adalah aplikasi autentikasi dua faktor untuk sistem yang menggunakan protokol kata sandi sekali pakai. Token dapat dengan mudah ditambahkan dengan memindai kode QR. FreeOTP tersedia melalui F-Droid.
- [Aegis](https://f-droid.org/en/packages/com.beemdevelopment.aegis/) adalah aplikasi gratis, aman, dan Open Source untuk Android untuk mengelola token verifikasi 2-langkah untuk layanan online Anda. Aegis tersedia melalui F-Droid.
- [Cryptomator](https://f-droid.org/en/packages/org.cryptomator.lite/) adalah layanan berbayar, lintas platform yang mengenkripsi data Anda secara lokal sehingga Anda dapat dengan aman mengunggahnya ke layanan cloud favorit Anda. Cryptomator dapat diunduh melalui F-Droid.

![image](assets/21.webp)
Kiri: Proton Pass
Kanan: Bitwarden

### Solusi Cloud

- [Proton Drive](https://proton.me/drive/download) adalah solusi cloud E2EE berbayar untuk membackup dan menyimpan semua file Anda. Saat penulisan ini, mereka baru saja mengumumkan klien desktop Windows, tetapi pengguna Mac dan Linux harus terus menggunakan versi web untuk sinkronisasi dari komputer mereka (untuk saat ini). Klien Android tersedia sebagai APK atau melalui Aurora.
- [Skiff](https://skiff.com/download) juga menawarkan penyimpanan cloud E2EE berbayar dan alat kolaborasi file. Mereka menawarkan klien desktop Mac dan Windows (serta aplikasi web) dan klien Android mereka harus diunduh dari Aurora.
- [Nextcloud](https://f-droid.org/en/packages/com.nextcloud.client/) menawarkan solusi berbasis cloud lengkap untuk kolaborasi, sinkronisasi lintas perangkat, dan penyimpanan file. Pengguna yang lebih maju dapat memilih untuk meng-host sendiri perangkat lunak Free and Open Source mereka di perangkat keras apa pun yang mereka suka. Klien Android dapat diunduh melalui F-Droid.
- [Cryptpad](https://cryptpad.fr/) menawarkan alternatif berbasis web, E2EE, gratis untuk Google Docs.

![image](assets/23.webp)

Proton Drive

## Kekurangan

Alternatif Open Source dan pelestarian privasi untuk aplikasi konglomerat teknologi yang telah Anda biasa gunakan banyak, dan beberapa di antaranya seringkali lebih baik daripada alternatif bersumber tertutup yang penuh dengan spyware.

Namun, ketika beralih ke GrapheneOS, ada beberapa kenyamanan yang harus Anda relakan karena tidak ada alternatifnya. Ini termasuk:

- **Apple CarPlay/Android Auto** - Anda harus tetap menggunakan Bluetooth, USB, atau Aux yang baik dan lama.
- **Apple/Google Pay** - Hampir semua orang tetap membawa dompet mereka!
- **Aplikasi perbankan** - Bukan berarti ini sama sekali tidak berfungsi. Beberapa berfungsi dengan sempurna. Yang lain hanya berfungsi dengan Google Play Services diaktifkan (baca lebih lanjut di bawah ini) dan yang lainnya sama sekali tidak berfungsi. Baca laporan tentang bank Anda [di sini](https://privsec.dev/posts/android/banking-applications-compatibility-with-grapheneos/) untuk melihat kondisi terkini. Jangan khawatir jika bank Anda termasuk dalam daftar yang tidak berfungsi, ingat Anda bisa menyimpan URL sebagai aplikasi web di layar beranda Anda.
- **Push Notifications** - Kebanyakan aplikasi yang mengirimkan pembaruan saat tidak menggunakan aplikasi tertentu akan melakukannya melalui Google Play Services. Ini tidak diinstal secara default dengan GrapheneOS, jadi jika Anda merasa tidak segera diberitahu ketika teman Anda mengirimkan email, inilah sebabnya. Kabar baiknya adalah beberapa aplikasi yang disebutkan di atas telah menerapkan koneksi latar belakang mereka sendiri untuk secara berkala memeriksa pembaruan dan kemudian memberi Anda notifikasi jika diperlukan.

### Sandboxed Google Play
GrapheneOS memiliki lapisan kompatibilitas yang memberikan opsi untuk menginstal dan menggunakan rilis resmi dari Google Play dalam kotak pasir aplikasi standar. Google Play tidak menerima akses atau hak istimewa khusus di GrapheneOS dibandingkan dengan menghindari kotak pasir aplikasi dan menerima sejumlah besar akses yang sangat berprivilegi.

Jika Anda merasa tidak bisa hidup tanpa notifikasi push untuk aplikasi favorit Anda atau aplikasi 'harus ada' tertentu tidak berguna tanpa Layanan Play, GrapheneOS memungkinkan Anda untuk [menginstal](https://grapheneos.org/usage#sandboxed-google-play-installation) layanan ini dalam lingkungan yang sepenuhnya terisolasi. Setelah terinstal, layanan ini tidak memerlukan akun Google untuk bekerja, dan izin setiap layanan dapat dikontrol secara ketat.

Sebelum Anda terburu-buru menginstal ini di hari pertama, saya mendesak Anda untuk melihat seberapa jauh Anda bisa tanpa mereka. Anda mungkin akan terkejut melihat betapa banyak aplikasi yang berfungsi dengan sempurna normal tanpa mereka.

Jika Anda ingin menginstalnya, cukup ketuk aplikasi 'Apps' yang telah terinstal sebelumnya diikuti oleh 'Google Play Services'. Pertimbangkan untuk menginstalnya bersama dengan aplikasi-aplikasi kurang privat yang tidak bisa Anda tinggalkan, dalam profil pengguna yang sepenuhnya terpisah untuk memberikan lapisan pemisahan ekstra dari sisanya di ponsel Anda.

![image](assets/24.webp)

Layar instalasi Layanan Play

### Profil

GrapheneOS memungkinkan Anda untuk memiliki pengalaman telepon yang terpisah, di dalam ponsel Anda. Profil tambahan dapat menginstal aplikasi dan layanan mereka sendiri dan tidak dapat mengakses file atau data dari akun pemilik.
Jika Anda hanya memiliki satu atau dua aplikasi 'harus ada' yang memerlukan Layanan Play, tetapi hanya digunakan sangat jarang, menginstal aplikasi tersebut bersama dengan Layanan Play dalam profil terpisah mungkin merupakan ide bagus untuk lebih meningkatkan privasi yang tersisa dengan menjalankannya dalam profil pemilik.

Anda dapat membaca lebih lanjut tentang penggunaan kasus ini [di sini](https://discuss.grapheneos.org/d/168-ideas-for-user-profiles/2).

Jika Anda memutuskan untuk menambahkan profil terpisah untuk sesuai dengan kasus penggunaan Anda, aplikasi [Insular](https://f-droid.org/en/packages/com.oasisfeng.island.fdroid/) mungkin berguna untuk Anda. Insular memungkinkan Anda untuk dengan mudah mengkloning aplikasi yang ada ke profil baru tanpa perlu melalui rute instalasi tradisional yang dibahas sebelumnya dalam panduan ini. Insular juga memungkinkan Anda untuk dengan cepat 'membekukan' aplikasi tersebut untuk menonaktifkan sepenuhnya semua layanan latar belakang aplikasi tersebut.

![image](assets/24.webp)

Layar manajemen profil pengguna

### e-SIM

Jika Anda ingin meningkatkan privasi telepon Anda ke level selanjutnya dan memiliki layanan seluler yang terpisah dari identitas dunia nyata Anda, eSIM mungkin cocok untuk Anda. eSIM adalah SIM virtual yang dapat Anda beli secara online dan tambahkan ke ponsel Anda melalui kode QR. Perusahaan yang menawarkan layanan seperti itu yang dapat dibayar secara anonim dengan Bitcoin termasuk [Silent.Link](https://silent.link/) dan [Bitrefill](https://www.bitrefill.com/gb/en/esims/).

eSIM tidak seharusnya dilihat sebagai solusi sempurna untuk privasi telepon. Mereka bisa menjadi alat yang berguna ketika di tangan yang tepat, tetapi silakan lakukan penelitian Anda tentang [tradeoff](https://grapheneos.org/faq#cellular-tracking) menggunakan jenis layanan seluler apa pun jika niat Anda adalah untuk benar-benar 'off grid'.

Layanan Play yang terisolasi harus diinstal untuk penyediaan eSIM di GrapheneOS.

## Cadangan
Setelah Anda menyelesaikan pengaturan ponsel Pixel baru Anda yang telah di-de-Google, ide yang baik adalah membuat cadangan diri Anda. Cadangan ini akan memungkinkan Anda untuk mengembalikan ponsel ke keadaan yang identik dalam kejadian jika Anda kehilangan ponsel Anda atau jika ponsel tersebut hilang/dicuri.
Anda dapat memilih untuk menyimpan file cadangan ke media penyimpanan eksternal apa pun, atau ke solusi cloud mandiri seperti Nextcloud, meskipun beberapa pengguna melaporkan tingkat keberhasilan yang bervariasi dengan opsi yang terakhir.

Untuk membuat cadangan pertama Anda:

1. Buka **Pengaturan** > **Sistem** > **Cadangan**, kemudian tulis kode pemulihan 12 kata Anda. Kode ini diperlukan untuk mendekripsi file cadangan pada tanggal nanti. Kehilangan kode, kehilangan akses ke cadangan ponsel Anda.
2. Selanjutnya pilih lokasi penyimpanan Anda. Saya akan merekomendasikan drive USB eksternal atau kartu microSD kelas industri.
3. Pilih data yang akan dicadangkan. Jika Anda memiliki ruang pada media penyimpanan yang ditentukan, saya menyarankan untuk memilih semuanya.
4. Ketuk tiga titik di kanan atas, dan pilih **Cadangkan sekarang**.

![gambar](assets/26.webp)

Layar Cadangan

Ingatlah jika Anda membuat cadangan offline ke media penyimpanan eksternal, masuk akal untuk menyelesaikan langkah ini secara teratur untuk memastikan setiap pembaruan penting terbaru pada ponsel Anda tidak hilang jika hal terburuk terjadi.

![video](https://www.youtube.com/embed/eyWmcItzisk)

Video yang menjelaskan proses cadangan

## Kesimpulan

Dalam beberapa tahun terakhir, perangkat lunak GrapheneOS telah berkembang secara signifikan. Ini lebih stabil dan kompatibel dari sebelumnya. Menggabungkan ini dengan ekosistem aplikasi Open Source dan pelestarian privasi yang berkembang, membuat GrapheneOS menjadi alternatif yang benar-benar layak untuk Android stok atau iOS, bahkan untuk orang 'normal' seperti Anda!

Pelanggaran data dan pengawasan jaringan begitu umum di dunia saat ini sehingga mereka hampir tidak membuat berita lagi. Terserah Anda untuk melindungi diri sendiri. Akan ada penyesuaian dan pengorbanan yang harus dilakukan di sepanjang jalan, tetapi mengurangi paparan Anda terhadap pelanggaran semacam itu tidaklah sesulit yang Anda pikirkan.

Saya berharap panduan ini dapat membantu Anda dalam perjalanan Anda. Jika Anda merasa panduan ini berguna dan ingin mendukung pekerjaan saya, silakan pertimbangkan untuk mengirimkan [donasi](/tips).

Jika Anda adalah pengguna GrapheneOS yang sudah ada, atau menjadi salah satunya sebagai hasil dari panduan ini, pertimbangkan untuk [berdonasi](https://grapheneos.org/donate) untuk mendukung pekerjaan penting mereka.

### Pelajari lebih lanjut

GrapheneOS adalah lubang kelinci yang bisa dengan mudah menghabiskan waktu berhari-hari untuk ditelusuri. Ada begitu banyak yang dapat Anda pelajari dan tinker dengan untuk menyesuaikan pengalaman sesuai dengan kebutuhan dan model ancaman Anda. Berikut adalah beberapa tautan di mana Anda dapat melanjutkan perjalanan Anda:

- [Panduan Penggunaan Resmi GrapheneOS](https://grapheneos.org/usage) - Situs Web Resmi
- [Forum GrapheneOS](https://discuss.grapheneos.org/) - Situs Web Resmi
- [Kelas Master Pengaturan GrapheneOS](https://www.youtube.com/watch?app=desktop&v=GLJyD9MJgIQ) - Video oleh 'The Privacy Wayfinder'
- [Podcast Umum GrapheneOS](https://www.youtube.com/watch?app=desktop&v=UCPX0mFFRNA) - Podcast oleh 'Watchman Privacy'

kredit penuh ke: https://github.com/BitcoinQnA/Bitcoiner.Guide/blob/main/grapheneos.md