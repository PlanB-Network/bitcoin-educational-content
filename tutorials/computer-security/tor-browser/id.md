---
name: Tor Browser
description: Bagaimana cara menggunakan Tor Browser?
---
![cover](assets/cover.webp)

Seperti namanya, browser adalah perangkat lunak yang digunakan untuk menjelajahi Internet. Browser ini berfungsi sebagai gerbang penghubung antara perangkat pengguna dan lingkungan web, dengan menerjemahkan kode situs web menjadi halaman-halaman yang interaktif dan mudah dibaca. Oleh karena itu, pemilihan browser memiliki pengaruh yang tinggi, mengingat dampaknya yang tidak hanya memengaruhi pengalaman penjelajahan Anda, tetapi juga keamanan dan privasi online Anda.

Penting untuk membedakan secara cermat antara browser dan mesin pencari. Browser merupakan perangkat lunak yang Anda gunakan untuk mengakses Internet (seperti Google Chrome atau Mozilla Firefox), sementara mesin pencari adalah layanan, seperti Google atau Bing, yang bertujuan membantu Anda menemukan informasi secara online.

Saat ini, Google Chrome merupakan browser yang paling banyak digunakan. Pada tahun 2024, pangsa pasar globalnya mencapai sekitar 65%. Meskipun Chrome sangat dihargai karena kecepatan dan performanya, ia tidak selalu menjadi pilihan terbaik bagi setiap orang, terutama jika privasi merupakan prioritas utama. Chrome adalah produk dari Google, sebuah perusahaan yang reputasinya dikenal dalam mengumpulkan dan menganalisis data pengguna yang sangat besar. Memang, browser internal mereka merupakan inti dari strategi pengawasan data Google. Mengingat perangkat lunak ini merupakan komponen sentral dalam sebagian besar interaksi online Anda, penguasaan terhadap pengumpulan data melalui browser menjadi isu penting bagi Google.
![TOR BROWSER](assets/notext/01.webp)
*Sumber: [gs.statcounter.com](https://gs.statcounter.com/browser-market-share)*

Ada beberapa keluarga besar browser, yang masing-masing didasarkan pada mesin rendering tertentu. Browser seperti Google Chrome, Microsoft Edge, Brave, Opera, atau Vivaldi, semuanya dibangun di atas browser Chromium, versi Chrome yang ringan dan open-source yang dikembangkan oleh Google. Semua browser ini menggunakan mesin rendering Blink, yang merupakan fork dari WebKit, yang berasal dari KHTML. Dominasi Chromium di pasar membuat browser yang berasal darinya menjadi sangat efisien, karena pengembang web cenderung mengoptimalkan situs mereka terutama untuk Blink.

Safari, browser Apple, menggunakan WebKit, yang juga berasal dari KHTML.

Di sisi lain, browser seperti Mozilla Firefox, LibreWolf, dan Tor Browser mengandalkan Gecko, mesin rendering yang berbeda, asli dari browser Netscape.

Memilih browser yang tepat tergantung pada kebutuhan Anda. Tetapi jika Anda setidaknya peduli dengan privasi Anda, dan oleh karena itu keamanan Anda, saya merekomendasikan untuk menggunakan Firefox untuk penggunaan umum dan Tor Browser untuk privasi yang lebih tinggi. Dalam tutorial ini, saya akan menunjukkan kepada Anda cara mudah untuk memulai dengan Tor Browser.
![TOR BROWSER](assets/notext/02.webp)

## Pengenalan ke Tor Browser

Tor Browser adalah browser yang dirancang khusus untuk navigasi internet yang aman dan seprivasi mungkin. Browser ini berbasis pada Firefox, dan karenanya menggunakan mesin rendering Gecko. Tor Browser memanfaatkan jaringan Tor untuk mengenkripsi dan mengarahkan lalu lintas Anda melalui beberapa server relai sebelum mentransmisikannya ke tujuan. Proses perutean berlapis-lapis ini, yang dikenal sebagai "*onion routing*, berfungsi untuk menyembunyikan alamat IP asli Anda, sehingga menyulitkan identifikasi lokasi dan aktivitas online Anda. Namun, konsekuensinya adalah penjelajahan menjadi lebih lambat dibandingkan dengan browser umum yang tidak menggunakan jaringan Tor, karena prosesnya bersifat tidak langsung.

Berbeda dengan browser lain, Tor Browser mengintegrasikan fitur khusus untuk mencegah pelacakan aktivitas online Anda, seperti mengisolasi setiap situs web yang dikunjungi dan secara otomatis menghapus cookies serta riwayat penjelajahan saat ditutup. Browser ini juga dirancang untuk meminimalkan risiko fingerprinting, dengan membuat semua pengguna tampak semirip mungkin bagi situs-situs yang dikunjungi.

Anda dapat dengan baik menggunakan Tor Browser untuk mengakses situs web standar (`.com`, `.org`, dll.). Dalam kasus ini, lalu lintas Anda dianonimkan dengan melewati beberapa node Tor sebelum mencapai node keluar yang berkomunikasi dengan situs akhir di clearnet.
![TOR BROWSER](assets/notext/03.webp)

Anda juga dapat menggunakan Tor Browser untuk mengakses layanan tersembunyi (alamat yang berakhiran `.onion`). Dalam skenario ini, semua lalu lintas tetap berada di dalam jaringan Tor, tanpa node keluar, memastikan privasi total bagi pengguna dan server tujuan. Mode operasi ini terutama digunakan untuk mengakses apa yang kadang-kadang disebut "*dark web*", bagian dari Internet yang tidak diindeks oleh mesin pencari tradisional.
![TOR BROWSER](assets/notext/04.webp)

## Apa Perbedaan Antara Jaringan Tor dan Browser Tor?

Jaringan Tor dan browser Tor adalah dua entitas yang berbeda namun saling melengkapi, dan penting untuk tidak salah kaprah. Jaringan Tor adalah sebuah infrastruktur global yang terdiri dari server relai. Server-server ini dioperasikan oleh para pengguna, dan fungsinya adalah menganonimkan lalu lintas internet dengan melewatkannya melalui beberapa node (titik) sebelum diarahkan ke tujuan akhirnya. Inilah yang dikenal sebagai "_onion routing_" yang terkenal itu.

Di sisi lain, browser Tor adalah browser khusus yang dirancang untuk memfasilitasi akses ke jaringan ini secara yang sederhana. Browser ini secara bawaan mengintegrasikan semua pengaturan yang diperlukan untuk terhubung ke jaringan Tor dan menggunakan versi Firefox yang telah dimodifikasi untuk memberikan pengalaman menjelajah yang familiar sekaligus memaksimalkan privasi dan keamanan.

Jaringan Tor tidak hanya digunakan oleh browser Tor. Jaringan ini dapat dimanfaatkan oleh berbagai perangkat lunak dan aplikasi untuk mengamankan komunikasi mereka. Misalnya, dimungkinkan untuk mengaktifkan komunikasi melalui jaringan Tor pada node Bitcoin Anda untuk menyembunyikan alamat IP Anda dari pengguna lain dan mencegah pengawasan lalu lintas terkait Bitcoin Anda oleh penyedia layanan internet Anda. Singkatnya, Jaringan Tor adalah infrastruktur yang menyediakan privasi dalam penjelajahan internet kita, dan browser Tor adalah perangkat lunak yang memungkinkan kita menggunakan jaringan ini sebagai bagian dari penjelajahan web kita.

## Bagaimana cara menginstal Tor Browser?

Tor Browser tersedia untuk Windows, Linux, dan macOS untuk komputer, serta untuk Android pada smartphone. Untuk menginstal Tor Browser di komputer Anda, kunjungi [situs web resmi Proyek Tor](https://www.torproject.org/).
![TOR BROWSER](assets/notext/05.webp)

Klik pada tombol "*Download Tor Browser / Unduh Tor Browser*".
![TOR BROWSER](assets/notext/06.webp)

Pilih versi yang sesuai untuk sistem operasi Anda.
![TOR BROWSER](assets/notext/07.webp)

Klik pada file eksekusi untuk memulai instalasi, lalu pilih bahasa Anda.
![TOR BROWSER](assets/notext/08.webp)

Pilih folder tempat perangkat lunak akan diinstal, lalu klik pada tombol "*Install*".
![TOR BROWSER](assets/notext/09.webp)

Tunggu hingga instalasi selesai.
![TOR BROWSER](assets/notext/10.webp)

Akhirnya, klik pada tombol "*Finish / Selesai*".
![TOR BROWSER](assets/notext/11.webp)

## Bagaimana cara menggunakan Tor Browser?

Tor Browser digunakan seperti browser standar.
![TOR BROWSER](assets/notext/12.webp)

Pada peluncuran pertama, browser menampilkan halaman yang mengundang Anda untuk terhubung ke jaringan Tor. Cukup klik pada tombol "*Connect / Hubungkan*" untuk membangun koneksi.
![TOR BROWSER](assets/notext/13.webp)

Jika Anda ingin perangkat lunak secara otomatis terhubung ke jaringan Tor dalam penggunaan Anda di masa depan, centang opsi "*Always connect automatically /  Selalu terhubung otomatis*".
![TOR BROWSER](assets/notext/14.webp)

Setelah terhubung ke jaringan Tor, Anda akan tiba di halaman utama.
![TOR BROWSER](assets/notext/15.webp)

Untuk melakukan pencarian di Internet, cukup masukkan kueri Anda di kolom pencarian dan tekan tombol "*enter*".
![TOR BROWSER](assets/notext/16.webp)

Kemudian, Anda akan mendapatkan hasil dari mesin pencari Anda sama seperti dengan browser lain.
![TOR BROWSER](assets/notext/17.webp)

Opsi "*Onionize*" pada DuckDuckGo memungkinkan Anda menggunakan mesin pencari melalui layanan tersembunyinya di jaringan Tor, dengan mengakses alamat `.onion`-nya.
![TOR BROWSER](assets/notext/18.webp)

## Bagaimana cara mengkonfigurasi Tor Browser?

Di bagian atas layar browser Anda, Anda akan menemukan opsi untuk mengimpor favorit Anda. Ini memungkinkan Anda untuk secara otomatis mengintegrasikan bookmark dari browser lama Anda ke dalam Tor Browser.
![TOR BROWSER](assets/notext/19.webp)

Anda juga memiliki opsi untuk menambahkan bookmark baru dengan mengklik ikon bintang yang terletak di pojok kanan atas halaman web yang Anda kunjungi.
![TOR BROWSER](assets/notext/20.webp)

Di menu di sebelah kanan, Anda dapat mengakses berbagai opsi.
![TOR BROWSER](assets/notext/21.webp)

Tombol "*New identity / Pengenal baru*" memungkinkan Anda untuk mengubah identitas Tor Anda. Secara khusus, ini memungkinkan Anda untuk memulai sesi pengguna baru di Tor, yang berarti mengubah alamat IP Anda dan mereset cookie serta sesi yang terbuka.
![TOR BROWSER](assets/notext/22.webp)

Menu "*Bookmarks*" memungkinkan Anda untuk mengelola bookmark Anda.
![TOR BROWSER](assets/notext/23.webp)

"*History / Riwayat*" memberi Anda akses ke riwayat penjelajahan Anda jika Anda telah mengaktifkannya di pengaturan.
![TOR BROWSER](assets/notext/24.webp)

Menu "*Add-ons and themes / Ekstensi dan tema*" memungkinkan Anda untuk menyesuaikan tampilan browser Anda atau menambahkan ekstensi. Karena Tor Browser berbasis pada Mozilla Firefox, Anda dapat menggunakan tema dan ekstensi yang tersedia untuk Firefox.
![TOR BROWSER](assets/notext/25.webp)

Akhirnya, tombol "*Settings / Pengaturan*" memberi Anda akses ke pengaturan browser Anda.
![TOR BROWSER](assets/notext/26.webp)

Di tab "*General / Umum*" dari pengaturan, ada berbagai opsi yang memungkinkan Anda untuk menyesuaikan antarmuka pengguna Tor Browser.
![TOR BROWSER](assets/notext/27.webp)

Di tab "*Home / Beranda*", Anda dapat memilih untuk mengubah halaman default yang ditampilkan saat membuka Tor Browser dan saat membuka tab baru.
![TOR BROWSER](assets/notext/28.webp)

Di tab "*Search /  Pencarian*", Anda dapat memilih mesin pencari. Tor Browser secara default menggunakan DuckDuckGo, mesin pencari yang berfokus pada perlindungan privasi pengguna, tetapi Anda juga dapat memilih Google atau Startpage, misalnya.
![TOR BROWSER](assets/notext/29.webp)

Anda juga dapat mengatur pintasan di mesin pencari Anda.
![TOR BROWSER](assets/notext/30.webp)

Misalnya, Anda dapat mengetik "*@wikipedia*" diikuti oleh istilah pencarian Anda, seperti "*Bitcoin*", ke dalam kolom pencarian browser.
![TOR BROWSER](assets/notext/31.webp)

Fitur ini kemudian melakukan pencarian untuk istilah Anda langsung di situs Wikipedia.
![TOR BROWSER](assets/notext/32.webp)

Anda dapat dengan demikian mengatur pintasan kustom lainnya untuk situs yang berbeda.

Selanjutnya, di tab "*Privacy & Security / Privasi dan keamanan*", Anda akan menemukan semua pengaturan yang terkait dengan privasi dan keamanan.
![TOR BROWSER](assets/notext/33.webp)
Anda memiliki opsi untuk menyimpan atau menghapus riwayat penjelajahan Anda.
![TOR BROWSER](assets/notext/34.webp)
Anda juga dapat mengelola izin akses yang Anda berikan kepada berbagai situs web.
![TOR BROWSER](assets/notext/35.webp)

Untuk keamanan umum browser Anda, mode "*Lebih Aman*" dan "*Paling Aman*" memungkinkan Anda untuk menyesuaikan fungsionalitas web dan skrip yang dieksekusi oleh situs yang Anda kunjungi. Ini meminimalkan risiko eksploitasi kerentanan, tetapi ini juga akan mempengaruhi tampilan dan interaktivitas situs sebagai gantinya.
![TOR BROWSER](assets/notext/36.webp)

Anda akan menemukan opsi keamanan lainnya, termasuk pemblokir konten berbahaya dan mode HTTPS-saja, yang memastikan koneksi ke situs selalu mematuhi protokol ini secara konsisten.
![TOR BROWSER](assets/notext/37.webp)

Terakhir, di tab "*Koneksi / Connection*", Anda akan menemukan semua pengaturan yang berkaitan dengan koneksi ke jaringan Tor. Di sinilah Anda dapat mengonfigurasi jembatan untuk mengakses Tor dari wilayah yang aksesnya mungkin disensor.
![TOR BROWSER](assets/notext/38.webp)

Dan itulah, Anda sekarang siap untuk menjelajahi Internet dengan cara yang lebih aman dan lebih pribadi! Jika privasi online adalah topik yang menarik bagi Anda, saya juga merekomendasikan untuk menemukan tutorial lain tentang Mullvad VPN:

https://planb.network/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8
