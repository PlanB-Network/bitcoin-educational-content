---
name: Tor Browser
description: Bagaimana cara menggunakan Tor Browser?
---
![cover](assets/cover.webp)

Seperti namanya, browser adalah perangkat lunak yang digunakan untuk menjelajahi Internet. Ini berfungsi sebagai gerbang antara mesin pengguna dan web, menerjemahkan kode situs web menjadi halaman yang interaktif dan dapat dibaca. Pilihan browser Anda sangat penting, karena tidak hanya mempengaruhi pengalaman browsing Anda tetapi juga keamanan dan privasi online Anda.

Berhati-hatilah untuk tidak mengacaukan browser dengan mesin pencari. Browser adalah perangkat lunak yang Anda gunakan untuk mengakses Internet (seperti Chrome atau Firefox), sementara mesin pencari adalah layanan, seperti Google atau Bing, misalnya, yang membantu Anda menemukan informasi secara online.

Hari ini, Google Chrome adalah browser yang paling banyak digunakan. Ini menyumbang sekitar 65% dari pasar global pada tahun 2024. Chrome dihargai karena kecepatan dan performanya, tetapi tidak selalu menjadi pilihan terbaik untuk semua orang, terutama jika privasi adalah prioritas bagi Anda. Chrome milik Google, sebuah perusahaan yang dikenal mengumpulkan dan menganalisis jumlah data yang besar dari penggunanya. Dan memang, browser buatan mereka adalah inti dari strategi pengawasan mereka. Perangkat lunak ini adalah komponen sentral dalam sebagian besar interaksi online Anda. Menguasai pengumpulan data pada browser Anda adalah isu penting bagi Google.
![TOR BROWSER](assets/notext/01.webp)
*Sumber: [gs.statcounter.com](https://gs.statcounter.com/browser-market-share)*

Ada beberapa keluarga besar browser, masing-masing berbasis pada mesin rendering tertentu. Browser seperti Google Chrome, Microsoft Edge, Brave, Opera, atau Vivaldi semuanya didirikan pada Chromium browser, versi Chrome yang ringan dan open-source yang dikembangkan oleh Google. Semua browser ini menggunakan mesin rendering Blink, yang merupakan fork dari WebKit, yang sendiri berasal dari KHTML. Dominasi Chromium di pasar membuat browser yang berasal darinya secara khusus efisien, karena pengembang web cenderung mengoptimalkan situs mereka terutama untuk Blink.

Safari, browser Apple, menggunakan WebKit, yang juga berasal dari KHTML.

Di sisi lain, browser seperti Mozilla Firefox, LibreWolf, dan Tor Browser mengandalkan Gecko, mesin rendering yang berbeda, asli dari browser Netscape.

Memilih browser yang tepat tergantung pada kebutuhan Anda. Tetapi jika Anda setidaknya peduli dengan privasi Anda, dan oleh karena itu keamanan Anda, saya merekomendasikan menggunakan Firefox untuk penggunaan umum dan Tor Browser untuk privasi yang lebih lagi. Dalam tutorial ini, saya akan menunjukkan kepada Anda cara mudah untuk memulai dengan Tor Browser.
![TOR BROWSER](assets/notext/02.webp)

## Pengenalan ke Tor Browser

Tor Browser adalah browser yang dirancang khusus untuk navigasi Internet yang aman dan seprivasi mungkin. Browser ini berbasis pada Firefox, dan oleh karena itu pada mesin rendering Gecko.
Tor Browser menggunakan jaringan Tor untuk mengenkripsi dan merutekan lalu lintas Anda melalui beberapa server relay sebelum mentransmisikannya ke tujuan. Proses perutean berlapis-lapis ini, yang dikenal sebagai "*onion routing*," membantu menyembunyikan alamat IP asli Anda, membuatnya sulit untuk mengidentifikasi lokasi dan aktivitas online Anda. Namun, browsing secara alami lebih lambat dibandingkan dengan browser standar yang tidak menggunakan jaringan Tor, karena bersifat tidak langsung.
Berbeda dengan browser lain, Tor Browser mengintegrasikan fitur khusus untuk mencegah pelacakan aktivitas online Anda, seperti mengisolasi setiap situs web yang dikunjungi dan secara otomatis menghapus cookies dan riwayat setelah ditutup. Ini juga dirancang untuk meminimalkan risiko fingerprinting, dengan membuat semua pengguna tampak serupa sebisa mungkin ke situs yang dikunjungi.
Anda dapat dengan baik menggunakan Tor Browser untuk mengakses situs web standar (`.com`, `.org`, dll.). Dalam kasus ini, lalu lintas Anda dianonimkan dengan melewati beberapa node Tor sebelum mencapai node keluar yang berkomunikasi dengan situs akhir di clearnet.
![TOR BROWSER](assets/notext/03.webp)
Anda juga dapat menggunakan Tor Browser untuk mengakses layanan tersembunyi (alamat yang berakhir dengan `.onion`). Dalam skenario ini, seluruh lalu lintas tetap berada dalam jaringan Tor, tanpa node keluar, memastikan privasi total baik untuk pengguna maupun server tujuan. Mode operasi ini terutama digunakan untuk mengakses apa yang terkadang disebut sebagai "*dark web*," bagian dari Internet yang tidak terindeks oleh mesin pencari tradisional.
![TOR BROWSER](assets/notext/04.webp)

## Apa perbedaan antara jaringan Tor dan browser Tor?

Jaringan Tor dan browser Tor adalah dua hal yang berbeda yang tidak boleh disamakan, tetapi keduanya saling melengkapi. Jaringan Tor adalah infrastruktur global dari server relay, dioperasikan oleh pengguna, yang menganonimkan lalu lintas Internet dengan melewatinya melalui beberapa node sebelum mengarahkannya ke tujuan akhirnya. Ini adalah routing bawang yang terkenal.

Di sisi lain, browser Tor adalah browser khusus yang dirancang untuk memudahkan akses ke jaringan ini secara sederhana. Secara default, ia mengintegrasikan semua pengaturan yang diperlukan untuk terhubung ke jaringan Tor dan menggunakan versi modifikasi dari Firefox untuk menyediakan pengalaman browsing yang familiar sambil memaksimalkan privasi dan keamanan.

Jaringan Tor tidak hanya digunakan oleh browser Tor. Ini dapat digunakan oleh berbagai perangkat lunak dan aplikasi untuk mengamankan komunikasi mereka. Misalnya, dimungkinkan untuk mengaktifkan komunikasi melalui jaringan Tor pada node Bitcoin Anda untuk menyembunyikan alamat IP Anda dari pengguna lain dan mencegah pengawasan lalu lintas terkait Bitcoin Anda oleh penyedia layanan internet Anda.
Untuk merangkum, jaringan Tor adalah infrastruktur yang menyediakan privasi dalam browsing internet kita, dan browser Tor adalah perangkat lunak yang memungkinkan kita menggunakan jaringan ini sebagai bagian dari browsing web kita.

## Bagaimana cara menginstal Tor Browser?

Tor Browser tersedia untuk Windows, Linux, dan macOS untuk komputer, serta untuk Android pada smartphone. Untuk menginstal Tor Browser di komputer Anda, kunjungi [situs web resmi Proyek Tor](https://www.torproject.org/).
![TOR BROWSER](assets/notext/05.webp)
Klik pada tombol "*Download Tor Browser*".
![TOR BROWSER](assets/notext/06.webp)
Pilih versi yang sesuai untuk sistem operasi Anda.
![TOR BROWSER](assets/notext/07.webp)
Klik pada file eksekusi untuk memulai instalasi, lalu pilih bahasa Anda.
![TOR BROWSER](assets/notext/08.webp)
Pilih folder tempat perangkat lunak akan diinstal, lalu klik pada tombol "*Install*".
![TOR BROWSER](assets/notext/09.webp)
Tunggu hingga instalasi selesai.
![TOR BROWSER](assets/notext/10.webp)
Akhirnya, klik pada tombol "*Finish*".
![TOR BROWSER](assets/notext/11.webp)

## Bagaimana cara menggunakan Tor Browser?

Tor Browser digunakan seperti browser standar.
![TOR BROWSER](assets/notext/12.webp)
Pada peluncuran pertama, browser menampilkan halaman yang mengundang Anda untuk terhubung ke jaringan Tor. Cukup klik pada tombol "*Connect*" untuk membangun koneksi.
![TOR BROWSER](assets/notext/13.webp)
Jika Anda ingin perangkat lunak secara otomatis terhubung ke jaringan Tor dalam penggunaan Anda di masa depan, centang opsi "*Always connect automatically*".
![TOR BROWSER](assets/notext/14.webp)
Setelah terhubung ke jaringan Tor, Anda akan tiba di halaman utama.
Untuk melakukan pencarian di Internet, cukup masukkan kueri Anda di bilah pencarian dan tekan tombol "*enter*".
Kemudian, Anda akan mendapatkan hasil dari mesin pencari Anda sama seperti dengan browser lain.
Opsi "*Onionize*" pada DuckDuckGo memungkinkan Anda menggunakan mesin pencari melalui layanan tersembunyinya di jaringan Tor, dengan mengakses alamat `.onion`-nya.

## Bagaimana cara mengkonfigurasi Tor Browser?

Di bagian atas layar browser Anda, Anda akan menemukan opsi untuk mengimpor favorit Anda. Ini memungkinkan Anda untuk secara otomatis mengintegrasikan bookmark dari browser lama Anda ke dalam Tor Browser.
Anda juga memiliki opsi untuk menambahkan bookmark baru dengan mengklik ikon bintang yang terletak di pojok kanan atas halaman web yang Anda kunjungi.
Di menu di sebelah kanan, Anda dapat mengakses berbagai opsi.
Tombol "*New identity*" memungkinkan Anda untuk mengubah identitas Tor Anda. Secara spesifik, ini memungkinkan Anda untuk memulai sesi pengguna baru di Tor, yang berarti mengubah alamat IP Anda dan mereset cookie serta sesi yang terbuka.
Menu "*Bookmarks*" memungkinkan Anda untuk mengelola bookmark Anda.
"*History*" memberi Anda akses ke riwayat penjelajahan Anda jika Anda telah mengaktifkannya di pengaturan.
Menu "*Add-ons and themes*" memungkinkan Anda untuk menyesuaikan tampilan browser Anda atau menambahkan ekstensi. Karena Tor Browser berbasis pada Mozilla Firefox, Anda dapat menggunakan tema dan ekstensi yang tersedia untuk Firefox.
Akhirnya, tombol "*Settings*" memberi Anda akses ke pengaturan browser Anda.
Di tab "*General*" dari pengaturan, ada berbagai opsi yang memungkinkan Anda untuk menyesuaikan antarmuka pengguna Tor Browser.
Di tab "*Home*", Anda dapat memilih untuk mengubah halaman default yang ditampilkan saat membuka Tor Browser dan saat membuka tab baru.
Di tab "*Search*", Anda dapat memilih mesin pencari. Tor Browser secara default menggunakan DuckDuckGo, mesin pencari yang berfokus pada perlindungan privasi pengguna, tetapi Anda juga dapat memilih Google atau Startpage, misalnya.
Anda juga dapat mengatur pintasan di mesin pencari Anda.
Misalnya, Anda dapat mengetik "*@wikipedia*" diikuti oleh istilah pencarian Anda, seperti "*Bitcoin*", ke dalam bilah pencarian browser.
Fitur ini kemudian melakukan pencarian untuk istilah Anda langsung di situs Wikipedia.
Anda dapat dengan demikian mengatur pintasan kustom lainnya untuk situs yang berbeda.

Selanjutnya, di tab "*Privacy & Security*", Anda akan menemukan semua pengaturan yang terkait dengan privasi dan keamanan.
Anda memiliki opsi untuk menyimpan atau menghapus riwayat penjelajahan Anda.
![TOR BROWSER](assets/notext/34.webp) Anda juga dapat mengelola izin akses yang Anda berikan kepada berbagai situs web.
![TOR BROWSER](assets/notext/35.webp)
Untuk keselamatan umum browser Anda, mode "*Lebih Aman*" dan "*Paling Aman*" memungkinkan Anda untuk menyesuaikan fungsionalitas web dan skrip yang dieksekusi oleh situs yang Anda kunjungi. Ini meminimalkan risiko eksploitasi kerentanan, tetapi ini juga akan mempengaruhi tampilan dan interaktivitas situs sebagai imbalannya. ![TOR BROWSER](assets/notext/36.webp) Anda akan menemukan opsi keamanan lainnya, termasuk pemblokir konten berbahaya dan mode hanya-HTTPS, yang memastikan bahwa koneksi dengan situs selalu menghormati protokol ini. ![TOR BROWSER](assets/notext/37.webp) Akhirnya, di tab "*Koneksi*", Anda akan menemukan semua pengaturan yang terkait dengan menghubungkan ke jaringan Tor. Di sinilah Anda dapat mengonfigurasi jembatan untuk mengakses Tor dari wilayah di mana aksesnya mungkin disensor. ![TOR BROWSER](assets/notext/38.webp) Dan itulah, Anda sekarang siap untuk menjelajahi Internet dengan cara yang lebih aman dan lebih pribadi! Jika privasi online adalah topik yang menarik bagi Anda, saya juga merekomendasikan untuk menemukan tutorial lain ini tentang Mullvad VPN:

https://planb.network/tutorials/others/general/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8