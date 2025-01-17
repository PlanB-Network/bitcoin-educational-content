---
name: RoninDojo

description: Memasang dan menggunakan node Bitcoin RoninDojo Anda.
---
***PERINGATAN:** Menyusul penangkapan pendiri Samourai Wallet dan penyitaan server mereka pada 24 April, beberapa fitur RoninDojo, seperti Whirlpool, tidak lagi beroperasi. Namun, ada kemungkinan alat-alat ini dapat dipulihkan atau diluncurkan kembali dengan cara yang berbeda dalam beberapa minggu mendatang. Selain itu, karena kode RoninDojo dihosting di GitLab Samourai, yang juga disita, saat ini tidak mungkin untuk mengunduh kode secara remote. Tim RoninDojo kemungkinan sedang bekerja untuk menerbitkan ulang kode tersebut.*

_Kami mengikuti perkembangan kasus ini serta perkembangan terkait alat-alat yang terkait. Tenang saja, kami akan memperbarui tutorial ini seiring dengan tersedianya informasi baru._

_Tutorial ini disediakan hanya untuk tujuan pendidikan dan informasi. Kami tidak mendukung atau mendorong penggunaan alat-alat ini untuk tujuan kriminal. Tanggung jawab setiap pengguna untuk mematuhi hukum di yurisdiksi mereka._

_Tutorial ini didedikasikan untuk pemasangan RoninDojo v1. Untuk memanfaatkan peningkatan dan fitur terbaru, saya sangat merekomendasikan untuk mengkonsultasikan tutorial kami yang didedikasikan untuk pemasangan langsung RoninDojo v2 pada Raspberry Pi Anda:_ https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8

---

Menjalankan dan menggunakan node Anda sendiri adalah esensial untuk benar-benar berpartisipasi dalam jaringan Bitcoin. Meskipun menjalankan node Bitcoin tidak memberikan manfaat finansial kepada pengguna, ini memungkinkan mereka untuk menjaga privasi, bertindak secara independen, dan memiliki kontrol atas kepercayaan mereka dalam jaringan.

Dalam artikel ini, kita akan melihat secara detail RoninDojo, solusi hebat untuk menjalankan node Bitcoin Anda sendiri.

### Daftar Isi:

- Apa itu RoninDojo?
- Perangkat keras apa yang harus dipilih?
- Bagaimana cara memasang RoninDojo?
- Bagaimana cara menggunakan RoninDojo?
- Kesimpulan

Jika Anda tidak familiar dengan cara kerja node Bitcoin dan perannya, saya merekomendasikan untuk memulai dengan membaca artikel ini: Node Bitcoin - Bagian 1/2: Konsep Teknis.

![Samourai](assets/1.webp)

## Apa itu RoninDojo?

Dojo adalah server node Bitcoin penuh yang dikembangkan oleh tim Samourai Wallet. Anda dapat dengan bebas memasangnya di mesin apa pun.

RoninDojo adalah asisten pemasangan dan alat administrasi untuk Dojo dan berbagai alat lainnya. RoninDojo mengambil implementasi asli dari Dojo dan menambahkan banyak alat lain ke dalamnya, sambil juga membuat pemasangan dan pengelolaan menjadi lebih mudah.

Mereka juga menawarkan perangkat keras "plug-and-play", RoninDojo Tanto, dengan RoninDojo yang telah dipasang sebelumnya pada mesin yang dirakit oleh tim mereka. Tanto adalah solusi berbayar, cocok untuk mereka yang tidak ingin "mengotori tangan".

Kode untuk RoninDojo bersifat open-source, jadi juga mungkin untuk memasang solusi ini pada perangkat keras Anda sendiri. Opsi ini hemat biaya tetapi membutuhkan sedikit lebih banyak manipulasi, yang akan kita lakukan dalam artikel ini.

RoninDojo adalah Dojo, jadi ini memungkinkan integrasi Whirlpool CLI yang mudah ke dalam node Bitcoin Anda untuk memiliki pengalaman CoinJoin terbaik. Dengan Whirlpool CLI, tidak hanya Anda dapat membiarkan bitcoin Anda remix 24/7 tanpa perlu menjaga komputer pribadi Anda tetap menyala, tetapi Anda juga dapat sangat meningkatkan privasi Anda.
RoninDojo mengintegrasikan banyak alat lain yang bergantung pada Dojo Anda, seperti kalkulator Boltzmann, yang menentukan tingkat privasi sebuah transaksi, server Electrum untuk menghubungkan dompet Bitcoin Anda yang berbeda ke node Anda, atau server Mempool untuk mengamati transaksi Anda secara pribadi. Dibandingkan dengan solusi node lain seperti Umbrel, yang telah saya perkenalkan kepada Anda dalam artikel ini, RoninDojo sangat fokus pada solusi dan alat "On Chain" yang mengoptimalkan privasi pengguna. Oleh karena itu, RoninDojo tidak memungkinkan interaksi dengan Lightning Network.

RoninDojo menawarkan lebih sedikit alat dibandingkan dengan Umbrel, tetapi beberapa fitur esensial untuk seorang Bitcoiner yang ada di Ronin sangat stabil.

Jadi, jika Anda tidak memerlukan semua fitur dari server Umbrel dan hanya ingin node yang sederhana dan stabil dengan beberapa alat esensial seperti Whirlpool atau Mempool, maka RoninDojo mungkin adalah solusi yang baik untuk Anda.

Menurut saya, fokus pengembangan Umbrel sangat pada Lightning Network dan alat yang serbaguna. Ini masih merupakan node Bitcoin, tetapi tujuannya adalah untuk menjadikannya mini-server multitugas. Sebaliknya, fokus pengembangan RoninDojo lebih selaras dengan tim di Samourai Wallet dan berfokus pada alat esensial untuk seorang Bitcoiner, memungkinkan untuk kemandirian penuh dan pengelolaan privasi yang dioptimalkan pada Bitcoin.

Harap dicatat bahwa pengaturan node RoninDojo sedikit lebih kompleks daripada node Umbrel.

Sekarang setelah kita dapat menggambarkan RoninDojo, mari kita lihat bagaimana cara mengatur node ini bersama-sama.

## Perangkat keras apa yang harus dipilih?

Untuk memilih mesin yang menjadi host dan menjalankan RoninDojo, Anda memiliki beberapa pilihan.

Seperti yang dijelaskan sebelumnya, pilihan termudah adalah memesan Tanto, mesin plug-and-play yang dirancang khusus untuk tujuan ini. Untuk memesan milik Anda, kunjungi di sini: [link](https://shop.ronindojo.io/product-category/nodes/).

Karena tim RoninDojo memproduksi kode sumber terbuka, juga dimungkinkan untuk mengimplementasikan RoninDojo pada mesin lain. Anda dapat menemukan versi terbaru dari wizard instalasi di halaman ini: [link](https://ronindojo.io/en/downloads.html), dan versi terbaru dari kode di halaman ini: [link](https://code.samourai.io/ronindojo/RoninDojo).

Secara pribadi, saya menginstalnya pada Raspberry Pi 4 8GB dan semuanya berfungsi dengan sempurna.

Namun, harap dicatat bahwa tim RoninDojo menunjukkan bahwa sering kali ada masalah dengan casing dan adaptor SSD. Oleh karena itu, tidak disarankan untuk menggunakan casing dengan kabel untuk SSD mesin Anda. Sebaliknya, lebih disukai untuk menggunakan kartu ekspansi penyimpanan yang dirancang khusus untuk motherboard Anda, seperti ini: Kartu Ekspansi Penyimpanan Raspberry Pi 4.

Berikut adalah contoh cara mengatur node RoninDojo Anda sendiri:

- Raspberry Pi 4.
- Casing dengan kipas.
- Kartu ekspansi penyimpanan yang kompatibel.
- Kabel daya.
- Kartu micro SD industri berkapasitas 16GB atau lebih.
- SSD berkapasitas 1TB atau lebih besar.
- Kabel Ethernet RJ45, kategori 8 disarankan.

## Bagaimana Cara Menginstal RoninDojo?

### Langkah 1: Persiapkan kartu micro SD yang dapat di-boot.

Setelah Anda merakit mesin Anda, Anda dapat mulai menginstal RoninDojo. Untuk melakukan ini, mulailah dengan membuat kartu micro SD yang dapat di-boot dengan membakar gambar disk yang sesuai ke dalamnya.

Masukkan kartu micro SD Anda ke dalam komputer pribadi Anda, kemudian kunjungi situs web resmi RoninDojo untuk mengunduh gambar disk RoninOS: https://ronindojo.io/en/downloads.html.
Unduh gambar disk yang sesuai dengan perangkat keras Anda. Dalam kasus saya, saya mengunduh gambar "MANJARO-ARM-RONINOS-RPI4-22.03.IMG.XZ":
![Unduh gambar disk RoninOS](assets/2.webp)

Setelah gambar diunduh, verifikasi integritasnya menggunakan file .SHA256 yang sesuai. Saya akan menjelaskan secara detail cara melakukan ini dalam artikel ini: Bagaimana cara memverifikasi integritas perangkat lunak Bitcoin di Windows?

Instruksi spesifik untuk memverifikasi integritas RoninOS juga tersedia di halaman ini: https://wiki.ronindojo.io/en/extras/verify.

Untuk membakar gambar ini ke kartu micro SD Anda, Anda dapat menggunakan perangkat lunak seperti Balena Etcher, yang dapat Anda unduh di sini: https://www.balena.io/etcher/.

Untuk melakukan ini, pilih gambar di Etcher dan flash ke kartu micro SD:

![Membakar gambar disk dengan Etcher](assets/3.webp)

Setelah operasi selesai, Anda dapat memasukkan kartu micro SD yang dapat di-boot ke dalam Raspberry Pi dan menghidupkan mesin.

### Langkah 2: Konfigurasi RoninOS.

RoninOS adalah sistem operasi dari node RoninDojo Anda. Ini adalah versi modifikasi dari Manjaro, distribusi Linux. Setelah memulai mesin Anda dan menunggu beberapa menit, Anda dapat mulai mengonfigurasinya.

Untuk terhubung secara remote ke sana, Anda perlu menemukan alamat IP dari mesin RoninDojo Anda. Untuk melakukan ini, Anda dapat, misalnya, terhubung ke panel administrasi kotak internet Anda, atau Anda juga dapat mengunduh perangkat lunak seperti https://angryip.org/ untuk memindai jaringan lokal Anda dan menemukan IP mesin.

Setelah Anda menemukan IP, Anda dapat mengambil kendali mesin Anda dari komputer lain yang terhubung ke jaringan lokal yang sama menggunakan SSH.

Dari komputer yang menjalankan macOS atau Linux, cukup buka terminal. Dari komputer yang menjalankan Windows, Anda dapat menggunakan alat khusus seperti Putty atau langsung menggunakan Windows PowerShell.

Setelah terminal terbuka, ketik perintah berikut:

> ssh root@192.168.?.?

Cukup ganti tanda tanya dengan IP RoninDojo yang sebelumnya Anda temukan.
Tip: Di Shell, klik kanan untuk menempelkan item.

Selanjutnya, Anda akan tiba di panel kontrol Manjaro. Pilih tata letak keyboard yang benar menggunakan panah untuk mengubah target dalam daftar dropdown.

![Konfigurasi Keyboard Manjaro](assets/4.webp)

Pilih nama pengguna dan kata sandi untuk sesi Anda. Gunakan kata sandi yang kuat dan buat cadangan yang aman. Anda dapat secara opsional menggunakan kata sandi yang lemah selama instalasi, dan nanti dengan mudah mengubahnya dengan "menyalin-menempelkannya" ke RoninUI. Ini akan memungkinkan Anda menggunakan kata sandi yang sangat kuat tanpa menghabiskan terlalu banyak waktu mengetiknya secara manual selama pengaturan Manjaro.

![Konfigurasi Nama Pengguna Manjaro](assets/5.webp)

Selanjutnya, Anda juga akan diminta untuk memilih kata sandi root. Untuk kata sandi root, masukkan kata sandi yang kuat langsung. Anda tidak akan dapat mengubahnya dari RoninUI. Juga, ingat untuk mencadangkan kata sandi root ini dengan aman.

Kemudian masukkan lokasi dan zona waktu Anda.

![Konfigurasi Zona Waktu Manjaro](assets/6.webp)

![Konfigurasi Lokasi Manjaro](assets/7.webp)

Selanjutnya, pilih nama host.

![Konfigurasi Nama Host Manjaro](assets/8.webp)

Akhirnya, verifikasi informasi konfigurasi Manjaro dan konfirmasi.

![Verifikasi Informasi Konfigurasi ManjaroOS](assets/9.webp)

### Langkah 3: Unduh RoninDojo.
Konfigurasi awal RoninOS akan dilakukan. Setelah selesai, seperti yang ditunjukkan pada tangkapan layar di atas, mesin akan restart. Tunggu beberapa saat, kemudian masukkan perintah berikut untuk terhubung kembali ke mesin RoninDojo Anda:
> ssh username@192.168.?.?

Cukup ganti "username" dengan nama pengguna yang sebelumnya Anda pilih, dan ganti tanda tanya dengan IP dari RoninDojo Anda.

Kemudian masukkan kata sandi pengguna Anda.

Di terminal, akan terlihat seperti ini:

![SSH Connection to RoninOS](assets/10.webp)

Anda sekarang terhubung ke mesin Anda, yang saat ini hanya memiliki RoninOS. Sekarang Anda perlu menginstal RoninDojo di atasnya.

Unduh versi terbaru RoninDojo dengan memasukkan perintah berikut:

> git clone https://code.samourai.io/ronindojo/RoninDojo

Pengunduhan akan cepat. Di terminal, Anda akan melihat ini:

![Cloning RoninDojo](assets/11.webp)

Tunggu hingga pengunduhan selesai, kemudian instal dan akses antarmuka pengguna RoninDojo menggunakan perintah berikut:

> ~/RoninDojo/ronin

Anda akan diminta untuk memasukkan kata sandi pengguna Anda:

![Bitcoin Node Password Verification](assets/12.webp)

Perintah ini hanya diperlukan saat pertama kali Anda mengakses RoninDojo Anda. Setelah itu, untuk mengakses RoninCLI melalui SSH, Anda hanya perlu memasukkan perintah [SSH username@192.168.?.?] dengan mengganti "username" dengan nama pengguna Anda dan memasukkan alamat IP node Anda. Anda akan diminta kata sandi pengguna Anda.

Selanjutnya, Anda akan melihat animasi yang luar biasa ini:

![RoninCLI launch animation](assets/13.webp)

Kemudian Anda akan tiba di antarmuka pengguna CLI RoninDojo.

### Langkah 4: Instal RoninDojo.

Dari menu utama, navigasikan ke menu "System" menggunakan tombol panah pada keyboard Anda. Tekan tombol enter untuk mengonfirmasi pilihan Anda.

![RoninCLI navigation menu to System](assets/14.webp)

Kemudian pergi ke menu "System Setup & Install".

![RoninCLI navigation menu to RoninDojo system installation](assets/15.webp)

Akhirnya, centang "System Setup" dan "Install RoninDojo" menggunakan spasi bar, kemudian pilih "Accept" untuk memulai instalasi.

![RoninDojo installation confirmation](assets/16.webp)

Biarkan proses instalasi berjalan dengan tenang. Dalam kasus saya, itu memakan waktu sekitar 2 jam. Biarkan terminal Anda tetap terbuka selama proses tersebut.

Sesekali periksa terminal Anda, karena Anda akan diminta untuk menekan tombol pada tahap tertentu dari instalasi, seperti di sini misalnya:

![RoninDojo installation in progress](assets/17.webp)

Di akhir instalasi, Anda akan melihat berbagai kontainer mulai berjalan:

![Node container startup](assets/18.webp)

Kemudian node Anda akan restart. Terhubung lagi ke RoninCLI untuk langkah selanjutnya.

![Bitcoin node restart](assets/19.webp)

### Langkah 5: Unduh rantai proof-of-work dan akses RoninUI.

Setelah instalasi selesai, node Anda akan mulai mengunduh rantai Bitcoin proof-of-work. Ini disebut Initial Block Download (IBD). Biasanya memakan waktu antara 2 hingga 14 hari tergantung pada koneksi internet dan perangkat Anda.

Anda dapat melacak kemajuan unduhan rantai dengan mengakses antarmuka web RoninUI.

Untuk mengaksesnya dari jaringan lokal, ketikkan berikut ini di bilah alamat browser Anda:

- Langsung masukkan alamat IP mesin Anda (192.168.?.?)

- Atau masukkan: ronindojo.local
Ingat untuk menonaktifkan VPN Anda jika Anda menggunakannya.
### Kemungkinan Masalah

Jika Anda tidak dapat terhubung ke RoninUI dari browser Anda, periksa fungsi aplikasi dari Terminal Anda yang terhubung ke node Anda melalui SSH. Sambungkan ke menu utama dengan mengikuti langkah sebelumnya:

- Ketik: SSH username@192.168.?.? ganti dengan kredensial Anda.

- Masukkan password pengguna Anda.

Setelah berada di menu utama, pergi ke:

> RoninUI > Restart

Jika aplikasi berhasil di-restart, masalahnya ada pada koneksi dari browser Anda. Periksa bahwa Anda tidak menggunakan VPN dan pastikan Anda terhubung ke jaringan yang sama dengan node Anda.

Jika restart menghasilkan kesalahan, coba perbarui sistem operasi dan kemudian instal ulang RoninUI. Untuk memperbarui OS:

> System > Software Updates > Update Operating System

Setelah pembaruan dan restart selesai, sambungkan kembali ke node Anda melalui SSH dan instal ulang RoninUI:

> RoninUI > Re-install

Setelah mengunduh RoninUI lagi, coba sambungkan ke RoninUI melalui browser Anda.

> Tip: Jika Anda secara tidak sengaja keluar dari RoninCLI dan menemukan diri Anda di terminal Manjaro, cukup masukkan perintah "ronin" untuk langsung kembali ke menu utama RoninCLI.

### Web log in

Anda juga dapat masuk ke antarmuka web RoninUI dari jaringan mana pun menggunakan Tor. Untuk melakukan ini, ambil alamat Tor dari RoninUI Anda dari RoninCLI:

> Credentials > Ronin UI

Ambil alamat Tor yang berakhir dengan .onion dan kemudian masuk ke Ronin UI dengan memasukkan alamat ini di browser Tor Anda. Berhati-hatilah untuk tidak membocorkan berbagai kredensial Anda, karena ini adalah informasi sensitif.

![Antarmuka login web RoninUI](assets/20.webp)

Setelah masuk, Anda akan diminta password pengguna Anda. Ini adalah password yang sama yang Anda gunakan untuk masuk melalui SSH.

![Panel manajemen antarmuka web RoninUI](assets/21.webp)

Kita dapat melihat kemajuan dari IBD (Initial Block Download) di sini. Bersabarlah, Anda sedang mengambil semua transaksi yang dilakukan di Bitcoin sejak 3 Januari 2009.

Setelah mengunduh seluruh blockchain, indexer akan mengkompakkan database. Operasi ini memakan waktu sekitar 12 jam. Anda juga dapat melacak kemajuannya di bawah "Indexer" di RoninUI.

Node RoninDojo Anda akan sepenuhnya fungsional setelah ini:

![Indexer disinkronkan pada node fungsional 100%](assets/22.webp)

Jika Anda ingin mengubah password pengguna menjadi yang lebih kuat, Anda dapat melakukannya sekarang dari tab "Settings". Di RoninDojo, tidak ada lapisan keamanan tambahan, jadi saya sarankan memilih password yang benar-benar kuat dan menjaga backup-nya.

## Bagaimana cara menggunakan RoninDojo?

Setelah rantai diunduh dan dikompakkan, Anda dapat mulai menikmati layanan yang ditawarkan oleh node RoninDojo baru Anda. Mari kita lihat cara menggunakannya.

### Menghubungkan perangkat lunak dompet ke electrs.

Utilitas pertama dari node baru Anda yang telah terinstal dan tersinkronisasi akan menjadi untuk menyiarkan transaksi Anda ke jaringan Bitcoin. Oleh karena itu, Anda kemungkinan ingin menghubungkan berbagai perangkat lunak manajemen dompet Anda ke node tersebut.

Anda dapat melakukan ini menggunakan Electrum Rust Server (electrs). Aplikasi ini biasanya sudah terpasang di node RoninDojo Anda. Jika tidak, Anda dapat menginstalnya secara manual dari antarmuka RoninCLI.

Cukup pergi ke:

> Applications > Manage Applications > Install Electrum Server

Untuk mendapatkan alamat Tor dari Electrum Server Anda, dari menu RoninCLI, pergi ke:

> Credentials > Electrs
Anda hanya perlu memasukkan tautan .onion ke dalam perangkat lunak dompet Anda. Sebagai contoh, di Sparrow Wallet, pergi ke tab:
> File > Preferences > Server

Di tipe server, pilih "Private Electrum", kemudian masukkan alamat Tor dari Electrum Server Anda di kolom yang sesuai. Akhirnya, klik pada "Test Connection" untuk menguji dan menyimpan koneksi Anda.

![Antarmuka koneksi Sparrow Wallet ke electrs](assets/23.webp)

### Menghubungkan perangkat lunak dompet ke Samourai Dojo.

Alih-alih menggunakan Electrs, Anda juga dapat menggunakan Samourai Dojo untuk menghubungkan dompet perangkat lunak yang kompatibel ke node RoninDojo Anda. Sebagai contoh, Samourai Wallet menawarkan opsi ini.

Untuk melakukan ini, cukup pindai kode QR koneksi Dojo Anda. Untuk mengaksesnya dari RoninUI, klik pada tab "Dashboard" dan kemudian pada tombol "Manage" di kotak Dojo Anda. Anda kemudian akan dapat melihat kode QR koneksi untuk Dojo dan BTC-RPC Explorer Anda. Untuk menampilkannya, klik pada "Display values".

![Mengambil kode QR koneksi ke Dojo](assets/24.webp)

Untuk menghubungkan Samourai Wallet Anda ke Dojo, Anda perlu memindai kode QR ini selama instalasi aplikasi:

![Menghubungkan ke Dojo dari aplikasi Samourai Wallet](assets/25.webp)

### Menggunakan Mempool Explorer Anda sendiri.

Sebuah alat penting bagi pengguna Bitcoin, explorer memungkinkan Anda untuk memeriksa berbagai informasi tentang rantai Bitcoin. Dengan Mempool, misalnya, Anda dapat memeriksa secara real-time biaya yang diterapkan oleh pengguna lain untuk menyesuaikan biaya Anda sesuai kebutuhan. Anda juga dapat memeriksa status konfirmasi salah satu transaksi Anda atau melihat saldo sebuah alamat.

Alat explorer ini dapat membuka Anda pada risiko privasi dan mengharuskan Anda untuk mempercayai basis data pihak ketiga. Ketika Anda menggunakan alat online ini tanpa melalui node Anda sendiri:

- Anda berisiko membocorkan informasi tentang dompet Anda.

- Anda mempercayai pengelola situs web untuk rantai proof-of-work yang mereka host.

Untuk menghindari risiko ini, Anda dapat menggunakan instance Mempool Anda sendiri di node Anda melalui jaringan Tor. Dengan solusi ini, tidak hanya Anda menjaga privasi saat menggunakan layanan, tetapi Anda juga tidak perlu lagi mempercayai penyedia karena Anda menanyakan basis data Anda sendiri.

Untuk melakukan ini, mulailah dengan menginstal Mempool Space Visualizer dari RoninCLI:

> Applications > Manage Applications > Install Mempool Space Visualizer

Setelah terinstal, ambil tautan ke Mempool Anda. Alamat Tor akan memungkinkan Anda untuk mengaksesnya dari jaringan mana pun. Demikian pula, kita ambil tautan ini melalui RoninCLI:

> Credentials > Mempool

![Mengambil alamat Tor Mempool](assets/26.webp)

Cukup masukkan alamat Tor Mempool Anda di browser Tor untuk menikmati instance Mempool Anda sendiri, berdasarkan data Anda sendiri. Saya merekomendasikan menambahkan alamat Tor ini ke favorit Anda untuk akses yang lebih cepat. Anda juga dapat membuat pintasan di desktop Anda.

![Antarmuka Mempool Space](assets/27.webp)

Jika Anda belum memiliki browser Tor, Anda dapat mengunduhnya di sini: https://www.torproject.org/download/

Anda juga dapat mengaksesnya dari smartphone Anda dengan menginstal Tor Browser dan memasukkan alamat yang sama. Dari mana saja, Anda dapat melihat keadaan rantai Bitcoin menggunakan node Anda sendiri.

### Menggunakan Whirlpool CLI.

Node RoninDojo Anda juga mencakup WhirlpoolCLI, antarmuka baris perintah jarak jauh untuk mengotomatiskan campuran Whirlpool.
Ketika Anda melakukan CoinJoin dengan implementasi Whirlpool, aplikasi yang Anda gunakan harus tetap terbuka agar dapat mengeksekusi campuran dan remix. Proses ini bisa menjadi melelahkan bagi pengguna yang ingin memiliki set anon yang tinggi, karena perangkat yang menghosting aplikasi dengan Whirlpool harus selalu menyala. Dalam praktiknya, ini berarti jika Anda ingin melibatkan UTXO Anda dalam remix 24/7, Anda perlu menjaga komputer pribadi atau telepon Anda selalu menyala dengan aplikasi terbuka.

Salah satu solusi untuk kendala ini adalah menggunakan WhirlpoolCLI pada mesin yang dimaksudkan untuk selalu menyala, seperti node Bitcoin. Dengan ini, UTXO kita dapat diremix 24/7 tanpa perlu menjaga mesin lain selain node Bitcoin kita berjalan.

WhirlpoolCLI digunakan bersama WhirlpoolGUI, antarmuka grafis yang diinstal pada komputer pribadi untuk pengelolaan Coinjoin yang mudah. Saya akan menjelaskan secara detail cara mengatur Whirlpool CLI dengan dojo Anda sendiri dalam artikel ini: [link](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=dans%20cette%20partie.-,Tutoriel%20%3A%20Whirpool%20CLI%20sur%20Dojo%20et%20Whirlpool%20GUI.,-Si%20vous%20souhaitez).

Untuk mempelajari lebih lanjut tentang Coinjoin secara umum, saya menjelaskan semuanya dalam artikel ini: [link](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin).

### Menggunakan Whirlpool Stat Tool.

Setelah melakukan CoinJoins dengan Whirlpool, Anda mungkin ingin mengetahui tingkat privasi sebenarnya dari UTXO campuran Anda. Whirlpool Stat Tool memungkinkan Anda untuk dengan mudah melakukan ini. Dengan alat ini, Anda dapat menghitung skor prospektif dan skor retrospektif dari UTXO campuran Anda. Untuk mempelajari lebih lanjut tentang menghitung Anon Sets ini dan bagaimana mereka bekerja, saya sarankan membaca bagian ini: [link](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment).

Alat ini sudah terpasang di RoninDojo Anda. Untuk saat ini, hanya tersedia dari RoninCLI. Untuk meluncurkannya dari menu utama, pergi ke:

> Samourai Toolkit > Whirlpool Stat Tool

Instruksi penggunaan akan muncul. Setelah selesai, tekan tombol apa saja untuk mengakses baris perintah:

![Whirlpool Stats Tool software home](assets/28.webp)

Terminal akan ditampilkan:

> wst#/tmp>

Untuk keluar dari antarmuka ini dan kembali ke menu RoninCLI, cukup masukkan perintah:

> quit

Untuk memulai, kita akan mengatur proxy pada Tor agar dapat mengekstrak data OXT dengan privasi penuh. Masukkan perintah:

> socks5 127.0.0.1:9050

Kemudian unduh data dari kolam yang berisi transaksi Anda:

> download 0001
>
> Ganti 0001 dengan kode denominasi kolam yang menarik bagi Anda.

Kode denominasi adalah sebagai berikut pada WST:

- Kolam 0.5 bitcoin: 05

- Kolam 0.05 bitcoin: 005

- Kolam 0.01 bitcoin: 001

- Kolam 0.001 bitcoin: 0001
![Mengunduh data dari kolam 0001 dari OXT](assets/29.webp)
Setelah data diunduh, muatlah dengan perintah:

> load 0001
>
> Gantilah 0001 dengan kode denominasi kolam yang Anda minati.

![Memuat data dari kolam 0001](assets/30.webp)
Biarkan proses pemuatan berlangsung, ini mungkin memakan waktu beberapa menit. Setelah memuat data, ketik perintah skor diikuti oleh TXID (identifikasi transaksi) Anda untuk mendapatkan Anon Sets-nya:

> score TXID
>
> Gantilah TXID dengan identifikasi transaksi Anda.

![Mencetak skor prospektif dan retrospektif dari TXID yang diberikan](assets/31.webp)

WST kemudian akan menampilkan skor retrospektif (metrik yang melihat ke belakang) diikuti oleh skor prospektif (metrik yang melihat ke depan). Selain skor dari Anon Sets, WST juga menyediakan Anda dengan tingkat difusi output Anda dalam kolam berdasarkan anon set.

Harap dicatat bahwa skor prospektif dari UTXO Anda dihitung berdasarkan TXID dari campuran awal Anda, bukan campuran terakhir Anda. Sebaliknya, skor retrospektif dari UTXO dihitung berdasarkan TXID dari siklus terakhir.

Sekali lagi, jika Anda tidak memahami konsep-konsep Anon Sets ini, saya merekomendasikan membaca bagian ini dari artikel saya tentang Coinjoin di mana saya menjelaskan semuanya secara detail dengan diagram: [https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment)

### Menggunakan kalkulator Boltzmann.

Kalkulator Boltzmann adalah alat yang memungkinkan Anda untuk dengan mudah menghitung berbagai metrik lanjutan pada transaksi Bitcoin, termasuk tingkat entropinya. Semua data ini akan memungkinkan Anda untuk mengkuantifikasi tingkat privasi dari sebuah transaksi dan mendeteksi kesalahan potensial. Alat ini sudah terpasang sebelumnya pada node RoninDojo Anda.

Untuk mengaksesnya dari RoninCLI, sambungkan melalui SSH, kemudian pergi ke menu:

> Samourai Toolkit > Kalkulator Boltzmann

Sebelum menjelaskan cara menggunakannya di RoninDojo, saya akan menjelaskan apa yang diwakili oleh metrik ini, bagaimana mereka dihitung, dan untuk apa mereka digunakan.

Indikator ini dapat digunakan untuk transaksi Bitcoin apa pun, tetapi mereka sangat menarik untuk mempelajari kualitas dari transaksi Coinjoin.

1. Indikator pertama yang dihitung oleh perangkat lunak ini adalah jumlah kombinasi yang mungkin. Ini dicatat pada kalkulator sebagai "nb combinations". Mengingat nilai dari UTXO-UTXO, indikator ini mewakili jumlah pemetaan yang mungkin dari input ke output.

> Jika Anda tidak familiar dengan istilah "UTXO", saya merekomendasikan membaca artikel singkat ini: Mekanisme transaksi Bitcoin: UTXO, input, dan output.

Dengan kata lain, indikator ini mewakili jumlah interpretasi yang mungkin untuk sebuah transaksi tertentu. Sebagai contoh, struktur Coinjoin Whirlpool 5x5 akan memiliki jumlah kombinasi yang mungkin sama dengan 1496:

![Skema transaksi Coinjoin di kycp.org](assets/32.webp)

Kredit: KYCP
2. Indikator kedua yang dihitung adalah entropi sebuah transaksi. Mengingat jumlah kombinasi yang mungkin sangat tinggi untuk sebuah transaksi, seseorang dapat memilih untuk menggunakan entropi sebagai gantinya. Entropi mewakili logaritma biner dari jumlah kombinasi yang mungkin. Rumusnya adalah sebagai berikut:
- E: entropi dari transaksi.
- C: jumlah kombinasi yang mungkin untuk transaksi.

> E = log2(C)

Dalam matematika, logaritma biner (basis 2) adalah fungsi invers dari fungsi pangkat 2. Dengan kata lain, logaritma biner dari x adalah pangkat yang harus dinaikkan angka 2 untuk mendapatkan nilai x.

Dengan demikian:

> E = log2(C)
> C = 2^E

Indikator ini dinyatakan dalam bit. Sebagai contoh, berikut adalah perhitungan entropi dari transaksi Whirlpool 5x5 Coinjoin, dengan jumlah kombinasi yang mungkin sebelumnya disebutkan sama dengan 1496:

> C = 1496
>
> E = log2(1496)
>
> E = 10.5469 bit

Oleh karena itu, transaksi Coinjoin ini memiliki entropi sebesar 10.5469 bit, yang sangat baik.

Semakin tinggi indikator ini, semakin banyak interpretasi yang berbeda dari transaksi tersebut, dan oleh karena itu transaksi tersebut semakin rahasia.

Mari kita ambil contoh lain. Berikut adalah transaksi "klasik" yang memiliki satu input dan dua output:

![Skema transaksi Bitcoin di oxt.me](assets/34.webp)

Kredit: OXT

Transaksi ini hanya memiliki satu interpretasi yang mungkin:

> [(inp 0) > (Outp 0 ; Outp 1)]

Jadi entropinya akan sama dengan 0:

> C = 1
>
> E = log2(C)
>
> E = 0

3. Indikator ketiga yang dikembalikan oleh kalkulator Boltzmann adalah efisiensi dari Tx yang disebut "Efisiensi Dompet". Indikator ini sederhananya memungkinkan membandingkan transaksi input dengan transaksi terbaik yang mungkin dalam konfigurasi yang sama.

Kita sekarang akan memperkenalkan konsep entropi maksimum, yang mewakili entropi tertinggi yang dapat dicapai untuk struktur transaksi tertentu. Sebagai contoh, struktur Whirlpool 5x5 Coinjoin akan memiliki entropi maksimum sebesar 10.5469. Indikator efisiensi membandingkan entropi maksimum ini dengan entropi aktual dari transaksi input. Rumusnya adalah sebagai berikut:

- ER: Entropi aktual yang dinyatakan dalam bit.
- EM: Entropi maksimum dengan struktur yang sama yang dinyatakan dalam bit.
- Ef: Efisiensi yang dinyatakan dalam bit.

> Ef = ER - EM
>
> Ef = 10.5469 - 10.5469
>
> Ef = 0 bit

Indikator ini juga dinyatakan sebagai persentase, sehingga rumusnya menjadi:

- CR: Jumlah kombinasi yang mungkin aktual.
- CM: Jumlah kombinasi yang mungkin maksimum dengan struktur yang sama.
- Ef: Efisiensi yang dinyatakan sebagai persentase.

> Ef = CR/CM
>
> Ef = 1496/1496
>
> Ef = 100%

Efisiensi 100% berarti transaksi ini memiliki privasi tertinggi yang mungkin relatif terhadap strukturnya.

4. Indikator keempat yang dihitung adalah kepadatan entropi. Ini memungkinkan kita untuk menghubungkan entropi dengan setiap input atau output. Indikator ini dapat digunakan untuk membandingkan efisiensi antar transaksi dengan ukuran yang berbeda.

Perhitungannya sangat sederhana: kita membagi entropi transaksi dengan jumlah input dan output yang ada. Sebagai contoh, untuk Whirlpool 5x5 Coinjoin, kita akan memiliki:

    ED: Kepadatan entropi yang dinyatakan dalam bit.
    E: Entropi transaksi yang dinyatakan dalam bit.
    T: Jumlah total input dan output dalam transaksi.

T = 5 + 5 = 10
ED = E / TED = 10.5469 / 10
ED = 1.054 bit

Informasi kelima yang disediakan oleh kalkulator Boltzmann adalah tabel probabilitas tautan antara input dan output. Tabel ini hanya memberikan Anda probabilitas (skor Boltzmann) bahwa input tertentu sesuai dengan output tertentu.

Jika kita mengambil contoh kita dengan Whirlpool Coinjoin, tabel probabilitasnya akan seperti ini:

| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
|---------|----------|----------|----------|----------|----------|
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |

Di sini kita dapat melihat bahwa setiap input memiliki probabilitas yang sama untuk terhubung dengan setiap output.

Namun, jika kita mengambil contoh transaksi dengan satu input dan dua output, itu akan terlihat seperti ini:

| Input | Output 0 | Output 1 |
| ----- | -------- | -------- |
| 0     | 100%     | 100%     |

Dalam contoh ini, kita dapat melihat bahwa probabilitas setiap output berasal dari input 0 adalah 100%.

Semakin rendah probabilitas ini, semakin tinggi tingkat kerahasiaan.

6. Informasi keenam yang dihitung adalah jumlah tautan deterministik. Rasio tautan deterministik juga akan disediakan. Indikator ini menyoroti jumlah tautan antara input dan output dari transaksi yang diberikan yang memiliki probabilitas 100%, artinya mereka tidak dapat disangkal.

Rasio menunjukkan jumlah tautan deterministik dalam transaksi dibandingkan dengan jumlah total tautan.

Misalnya, transaksi Coinjoin Whirlpool tidak memiliki tautan deterministik antara input dan output. Indikatornya akan nol dan rasionya juga 0%.

Namun, untuk transaksi kedua yang diteliti (1 input dan 2 output), indikatornya adalah 2 dan rasionya adalah 100%.

Oleh karena itu, jika indikator ini nol, itu menunjukkan kerahasiaan yang baik.

Sekarang setelah kita telah mempelajari indikatornya, mari kita lihat cara menghitungnya menggunakan perangkat lunak ini. Dari RoninCLI, pergi ke menu:

> Samourai Toolkit > Boltzmann Calculator

![Halaman utama perangkat lunak Boltzmann Calculator](assets/35.webp)

Setelah perangkat lunak diluncurkan, masukkan ID transaksi yang ingin Anda pelajari. Anda dapat memasukkan beberapa transaksi sekaligus dengan memisahkannya dengan koma, kemudian tekan enter:

![Masukkan TXID untuk dipelajari pada Boltzmann Calculator](assets/36.webp)

Kalkulator kemudian akan mengembalikan semua indikator yang telah kita lihat sebelumnya:

![Cetakan data Boltzmann Calculator untuk TXID ini](assets/37.webp)

Ketik perintah "Quit" untuk keluar dari perangkat lunak dan kembali ke menu RoninCLI.

Untuk mempelajari lebih lanjut tentang kalkulator Boltzmann, saya merekomendasikan membaca artikel-artikel ini:

- https://medium.com/@laurentmt/memperkenalkan-boltzmann-85930984a159

- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf
### Menghubungkan Bisq.
Bisq adalah platform pertukaran peer-to-peer yang memungkinkan Anda untuk membeli dan menjual bitcoin. Platform ini digunakan dengan perangkat lunak desktop yang berjalan di Tor dan memungkinkan Anda untuk bertukar bitcoin tanpa perlu menyediakan identitas Anda.
Bisq mengamankan pertukaran peer-to-peer melalui sistem multi-tanda tangan 2/2. Anda dapat menggunakan perangkat lunak ini dengan node RoninDojo Anda sendiri untuk mengoptimalkan privasi pertukaran Anda dan mempercayai data dari blockchain node Anda sendiri.

Untuk mengunduh perangkat lunak Bisq, kunjungi situs web resmi mereka: https://bisq.network/

Untuk memulai dengan perangkat lunak, saya merekomendasikan membaca halaman ini: https://bisq.network/getting-started/

Untuk mengambil tautan koneksi dari RoninDojo Anda, Anda perlu terhubung ke RoninCLI melalui SSH. Kemudian pergi ke menu:

> Aplikasi > Kelola Aplikasi

Masukkan kata sandi Anda, kemudian centang kotak dengan tombol spasi:

> [ ] Aktifkan Koneksi Bisq

Konfirmasi pilihan Anda. Biarkan node Anda terinstal, kemudian ambil alamat Tor V3 dari:

> Kredensial > Bitcoind

Salin alamat di bawah "Bitcoin Daemon".

Anda juga dapat mengambil alamat Tor V3 Bitcoind Anda dari antarmuka RoninUI dengan hanya mengklik "Kelola" di kotak "Bitcoin Core" pada "Dashboard":

![Ambil alamat TorV3 Bitcoin Daemon di RoninUI](assets/38.webp)

Untuk menghubungkan node Anda dari Bisq, pergi ke menu:

> Pengaturan > Info Jaringan

![Akses antarmuka koneksi node dari perangkat lunak Bisq](assets/39.webp)

Klik pada gelembung "Gunakan custom Bitcoin Core nodes". Kemudian masukkan alamat Bitcoin TorV3 Anda di kotak yang ditentukan, dengan ".onion" tetapi tanpa "http://".

![Kotak untuk memasukkan alamat TorV3 node Anda di perangkat lunak Bisq](assets/40.webp)

Restart perangkat lunak Bisq. Node Anda sekarang terhubung ke Bisq Anda.

### Fitur lainnya.

Node RoninDojo Anda juga mencakup fitur dasar lainnya. Anda memiliki kemampuan untuk memindai informasi spesifik untuk memastikan bahwa itu diperhitungkan.

Misalnya, terkadang mungkin bahwa dompet Anda yang terhubung ke RoninDojo tidak menemukan bitcoin yang menjadi milik Anda. Saldo adalah 0 meskipun Anda yakin bahwa Anda memiliki bitcoin di dompet ini. Ada banyak penyebab yang mungkin perlu dipertimbangkan, termasuk kesalahan dalam jalur derivasi, dan di antaranya, juga mungkin bahwa node Anda tidak mengamati alamat Anda.

Untuk memperbaikinya, Anda dapat memeriksa bahwa node Anda melacak xpub Anda dengan "alat xpub". Untuk mengaksesnya dari RoninUI, pergi ke menu:

> Pemeliharaan > Alat XPUB

Masukkan xpub yang bermasalah dan klik "Periksa" untuk memverifikasi informasi ini.

![Alat XPUB dari RoninUI](assets/41.webp)

Jika xpub Anda dilacak oleh node, Anda akan melihat ini muncul:

![Hasil Alat XPUB menunjukkan analisis yang berhasil](assets/42.webp)

Periksa bahwa semua transaksi muncul dengan benar. Juga, verifikasi bahwa jenis derivasi cocok dengan dompet Anda. Di sini kita dapat melihat bahwa node menginterpretasikan xpub ini sebagai derivasi BIP44. Jika jenis derivasi ini tidak cocok dengan dompet Anda, klik tombol "Ketik Ulang", kemudian pilih BIP44/BIP49/BIP84 sesuai pilihan Anda:

![Ubah jenis derivasi xpub yang diteliti dari RoninUI](assets/43.webp)

Jika xpub Anda tidak dilacak oleh node Anda, Anda akan melihat layar ini yang mengundang Anda untuk mengimpor:
![Impor xpub dengan Alat XPUB pada RoninUI](assets/44.webp)
Anda juga dapat menggunakan alat pemeliharaan lainnya:

- Alat Transaksi: Memungkinkan Anda untuk mengamati detail dari transaksi tertentu.
- Alat Alamat: Memungkinkan Anda untuk memverifikasi bahwa alamat tertentu sedang dilacak oleh Dojo Anda.
- Pemindaian Ulang Blok: Memaksa node Anda untuk memindai ulang rentang blok yang dipilih.

Anda juga akan menemukan alat "Push Tx" pada RoninUI. Ini memungkinkan Anda untuk menyiarkan transaksi yang telah ditandatangani ke jaringan Bitcoin. Ini harus dimasukkan dalam format heksadesimal:

![Alat untuk menyiarkan transaksi yang telah ditandatangani dari RoninUI](assets/45.webp)

## Kesimpulan.

Kita telah melihat bagaimana cara menginstal dan memulai dengan alat yang luar biasa ini, yaitu RoninDojo. Ini adalah pilihan yang sangat baik untuk menjalankan node Bitcoin Anda sendiri. Ini adalah solusi yang stabil yang mengintegrasikan dan memperbarui semua alat esensial untuk seorang Bitcoiner.

Jika menggunakan terminal tidak membuat Anda takut dan jika Anda tidak memerlukan alat yang terkait dengan Jaringan Lightning, maka RoninDojo mungkin menarik bagi Anda.

Jika bisa, pertimbangkan untuk mendonasikan kepada pengembang yang secara bebas memproduksi perangkat lunak sumber terbuka ini untuk Anda: https://donate.ronindojo.io/

Untuk mempelajari lebih lanjut tentang RoninDojo, saya merekomendasikan untuk memeriksa tautan di sumber daya eksternal saya di bawah ini.

### Bacaan lebih lanjut:

- Memahami dan menggunakan CoinJoin pada Bitcoin.
- Fungsi hash - kutipan dari ebook Bitcoin Démocratisé 1.
- Semua yang perlu Anda ketahui tentang Bitcoin Passphrase.

### Sumber daya eksternal:

- https://ronindojo.io/index.html
- https://wiki.ronindojo.io/en/home
- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf
- https://medium.com/@laurentmt/memperkenalkan-boltzmann-85930984a159
- https://en.wikipedia.org/wiki/Boltzmann_formula
- https://wiki.ronindojo.io/en/setup/bisq
- https://bisq.network/
