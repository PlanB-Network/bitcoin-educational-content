---
name: Ntopng
description: Pantau jaringan Anda dengan ntopng
---
![cover](assets/cover.webp)

___

*Tutorial ini didasarkan pada konten asli oleh Florian Duchemin yang dipublikasikan di [IT-Connect](https://www.it-connect.fr/). Lisensi [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Perubahan mungkin telah dilakukan pada teks asli.*

___

## I. Presentasi

**Untuk memeriksa kelancaran jaringan, mendapatkan gambaran jelas tentang penggunaan, atau untuk statistik performa, pemantauan aliran jaringan adalah bagian penting dari jaringan perusahaan**. Hal ini membantu mengantisipasi perubahan pada infrastruktur dan membantu memastikan kualitas penggunaan bagi pengguna (juga dikenal sebagai QoE atau _Quality of Experience_, berbeda dengan QoS).

Untuk melakukan ini, ada banyak teknik dan perangkat lunak/protokol yang tersedia. Netflow, misalnya, yang dikembangkan oleh Cisco, dapat digunakan untuk mengambil statistik aliran IP dari sebuah interface, tetapi penggunaannya terbatas pada peralatan yang kompatibel.

Itulah mengapa dalam tutorial ini saya akan memperkenalkan **Ntop** dan menunjukkan cara menggunakannya di infrastruktur Anda untuk mengawasi penggunaan jaringan Anda.

Ntop adalah perangkat lunak open source yang dapat dipasang di komputer Linux mana pun. Perangkat lunak ini gratis dan dapat mengumpulkan data berikut:

- Pemanfaatan bandwidth
- Klien utama
- Tujuan utama
- Protokol yang digunakan
- Aplikasi yang digunakan
- Port yang digunakan
- Dll.

Sekarang berganti nama menjadi **Ntopng (New Generation)**, yang menawarkan banyak fungsi dasar secara gratis. Versi komersial juga tersedia, memungkinkan ekspor peringatan yang dikonfigurasi ke perangkat lunak tipe SIEM, atau lalu lintas untuk difilter dengan aturan yang ditentukan langsung dari probe.

## II. Prasyarat

Pemasangan probe Ntop berbeda-beda sesuai dengan peralatan dan lingkungan. Jadi, di sini saya tidak akan memberikan panduan langkah demi langkah, tetapi akan menguraikan berbagai kemungkinannya.

### A. Mode on-board

Jika Anda memiliki firewall pfSense, OPNSense, atau Endian dalam produksi, atau bahkan workstation Linux dengan NFTables, kabar baik! Anda dapat memasang Ntopng secara langsung dan mulai memantau interface Anda.

Keuntungan dari teknik ini adalah tidak memerlukan perangkat keras tambahan. Di sisi lain, ini meningkatkan pemanfaatan sumber daya, jadi pastikan Anda memiliki perangkat keras yang memadai atau VM dengan ukuran yang cukup (minimal 2 core dan 2GB RAM).

### B. Mode TAP / SPAN

TAP adalah perangkat jaringan yang menduplikasi lalu lintas yang melewatinya dan mengirimkannya ke perangkat lain. Keuntungan dari perangkat ini adalah tidak memerlukan modifikasi pada infrastruktur yang ada, dan dapat ditempatkan di mana saja untuk memantau bagian jaringan tertentu, atau antara core switch dan edge router untuk menganalisis lalu lintas ke/dari Internet.

Kerugian besar dari jenis peralatan ini adalah biayanya. Dalam jaringan Gigabit saat ini, TAP pasif tidak dapat menangkap lalu lintas jaringan dengan benar, jadi Anda memerlukan perangkat aktif yang biayanya sekitar €200 (minimal).

Mode **SPAN**, juga dikenal sebagai **port mirroring**, digunakan oleh switch untuk meneruskan lalu lintas dari satu port ke port lainnya. Ini sejauh ini metode favorit saya, karena mudah diatur dan, seperti TAP, memungkinkan Anda untuk memantau sebagian atau seluruh jaringan sesuai keinginan. Namun, ada dua kelemahan: switch harus mengintegrasikan fungsi ini, dan penggunaannya dapat meningkatkan beban prosesor pada switch.

### C. Mode router

Sangat mungkin untuk memasang router di bawah Linux dan memasang ntopng di atasnya. Satu-satunya kelemahan dari metode ini adalah bahwa metode akan memodifikasi jaringan Anda, baik pengalamatan internalnya, maupun pengalamatan antara router "asli" Anda dan router yang Anda tambahkan.

Catatan: bagi pembaca artikel [Membuat router Wifi dengan Raspberry Pi dan RaspAP](https://www.it-connect.fr/creer-un-routeur-wifi-avec-un-raspberry-pi-et-raspap/), sangat mungkin untuk memasang Ntopng pada Rpi Anda untuk mendapatkan statistik yang akurat!


### D. Mode Bridge



Alternatif yang menarik adalah dengan menggunakan **sebuah mesin Linux dalam mode jembatan** yang ditempatkan di antara dua buah peralatan, hal ini memungkinkan semua trafik untuk ditangkap tanpa harus mengintervensi konfigurasi infrastruktur atau peralatannya. Karena mesin lama dapat melakukan pekerjaan itu, biaya dari metode ini juga bisa menarik. Perhatikan bahwa agar optimal, perangkat harus memiliki tiga kartu jaringan, dua dalam mode bridge, satu untuk mengakses Interface dan SSH. Bisa saja menggunakan hanya dua kartu, tetapi lalu lintas administrasi perangkat juga akan ditangkap...

Alternatif yang menarik adalah menggunakan **komputer Linux dalam mode bridge**. Ditempatkan di antara dua peralatan, ini memungkinkan semua lalu lintas ditangkap tanpa harus mengintervensi konfigurasi infrastruktur atau peralatannya. Karena perangkat lama bisa melakukan pekerjaan ini, biaya metode ini juga bisa menarik. Perhatikan bahwa agar optimal, perangkat harus memiliki tiga kartu jaringan, dua dalam mode bridge, satu untuk mengakses interface dan SSH. Sangat mungkin untuk menggunakan hanya dua kartu, tetapi lalu lintas administrasi perangkat juga akan ditangkap...

Jadi, **mode terakhir inilah yang akan saya gunakan**. Untuk alasan praktis, saya akan menggunakan  virtual machines untuk demonstrasi, tetapi metodenya tetap sama untuk penggunaan pada mesin fisik.

## III. Persiapan probe dengan jembatan Interface

Untuk probe, saya memilih komputer **Debian 11** dengan instalasi minimal.

Langkah pertama, selalu sama, perbarui file:

```
apt-get update && apt-get upgrade
```

Kemudian instal paket **bridge-utils**, yang akan memungkinkan kita untuk membuat bridge:

```
apt-get install bridge-utils
```

Setelah terinstal, hal pertama yang perlu diperhatikan adalah nama kartu jaringan kita saat ini. Pada Debian, nama ini dapat memiliki beberapa bentuk, dan kita akan membutuhkannya untuk konfigurasi.

Perintah **ip add** yang sederhana akan mengembalikan output dengan informasi ini:

![Image](assets/fr/016.webp)

Di sini, saya melihat 3 interface:

- **Lo**: Ini adalah interface loopback; sebuah interface virtual yang "melingkar" di atas peralatan itu sendiri. Pada dasarnya, interface ini, yang alamatnya adalah 127.0.0.1 (meskipun alamat apa pun dalam rentang 127.0.0.0/8 akan berfungsi, karena rentang ini dicadangkan untuk tujuan ini) digunakan untuk menghubungi peralatan itu sendiri. Jika Anda telah memasang situs web di workstation Anda (menggunakan WAMPP, misalnya), Anda mungkin pernah menggunakan alamat "*localhost*" di satu waktu untuk menampilkan situs yang di-host pada mesin Anda sendiri. Nama host ini diasosiasikan dengan alamat 127.0.0.1 dan karenanya dengan interface loopback.
- **ens33**: Ini adalah interface pertama saya, yang menerima alamat di sini dari DHCP saya.
- **ens36**: Interface kedua saya.

Sekarang setelah saya memiliki semua informasi, saya dapat memodifikasi file */etc/network/interfaces* untuk membuat bridge saya. Inilah tampilannya saat ini (mungkin berbeda):

```
# File ini menjelaskan interfaces jaringan yang tersedia dalam sistem Anda
# dan cara mengaktifkannya. Untuk informasi lebih lanjut, lihat interfaces(5).

source /etc/network/interfaces.d/*

# Interface jaringan loopback
auto lo
iface lo inet loopback

# Interface jaringan utama
allow-hotplug ens33
iface ens33 inet dhcp
# This is an autoconfigured IPv6 interface
iface ens33 inet6 auto
```

Bagian pertama berkaitan dengan Interface loopback saya, yang tidak akan saya bahas, diikuti oleh Interface ens33. Modifikasi-modifikasinya melibatkan penambahan Interface kedua saya (ens36) dan mengonfigurasi bridge dengan kedua interface ini.


```
# Interface jaringan utama
auto ens33
iface ens33 inet manual

# Interface jaringan sekunder
auto ens36
iface ens36 inet manual
```

Berikut ini beberapa penjelasan mengenai perubahan awal ini:

- **auto Interface**: akan secara otomatis "memulai" Interface saat sistem dinyalakan.
- **iface Interface inet manual**: untuk menggunakan Interface tanpa alamat IP. Sama seperti kata kunci "static" untuk mendefinisikan alamat IP statis atau "dhcp" untuk menggunakan pengalamatan dinamis.

Modifikasi terus berlanjut:

```
# Bridge interface
auto br0
iface br0 inet static
address 192.168.1.23
netmask 255.255.255.0
gateway 192.168.1.1
bridge_ports ens33 ens36
bridge_stp off
```

Di sini sekali lagi, beberapa penjelasan:

- **iface br0 inet static**: di sini saya telah mendefinisikan Interface bridge saya (br0) dengan alamat statis.
- **address, netmask, gateway**: informasi pengalamatan standar.
- **bridge_ports**: interface-interface yang akan disertakan dalam bridge.
- **bridge_stp**: protokol Spanning Tree digunakan saat menghubungkan switch untuk mendeteksi tautan yang berlebihan dan menghindari loop. Karena bridge dapat disisipkan di antara dua jalur jaringan, itu bisa menjadi sumber loop, maka ada kemungkinan untuk mengaktifkan protokol ini. Saya tidak membutuhkannya di sini, jadi saya menonaktifkannya.

Simpan perubahan dan mulai ulang jaringan:

```
systemctl restart networking
```

Untuk memeriksa perubahannya, tampilkan kembali hasil dari perintah **ip** add:

![Image](assets/fr/021.webp)

**Anda dapat melihat dengan jelas Interface baru saya "*br0*" dengan alamat IP yang telah saya tetapkan.** Selain itu, Anda juga dapat melihat bahwa dua interface fisik saya memang berstatus "UP", tetapi tidak memiliki alamat IP.

## IV. Menginstalasi NtopNG

Setelah probe kita dapat melakukan sniffing lalu lintas antara jaringan saya dan router, yang tersisa hanyalah memasang Ntopng. Untuk melakukannya, pertama-tama modifikasi file _/etc/apt/sources.list_ dan tambahkan **contrib** di akhir setiap baris yang dimulai dengan **deb** atau **deb-src**.

Secara default, sumber paket hanya berisi paket-paket yang sesuai dengan DFSG (_Debian Free Software Guidelines_), yang diidentifikasi dengan kata kunci **main**. Anda juga bisa menambahkan sumber-sumber ini:

- **contrib**: paket yang berisi perangkat lunak yang sesuai dengan DFSG, tetapi menggunakan dependensi yang bukan merupakan bagian dari cabang **main**.
- **non-free**: berisi paket yang tidak sesuai dengan DFSG.

Contoh baris di /etc/apt/sources.list:

```
deb http://deb.debian.org/debian/ bullseye main
```

Jadi, saya hanya akan menambahkan kata **contrib** pada baris seperti ini.

Langkah-langkah selanjutnya terdapat pada situs [NtopNG](https://packages.ntop.org/apt/) di mana, untuk Debian 11, Anda perlu menambahkan sumber Ntop untuk instalasi di masa mendatang. Penambahan ini dilakukan secara otomatis dengan menggunakan file :

```
wget https://packages.ntop.org/apt/bullseye/all/apt-ntop.deb
apt install ./apt-ntop.deb
```

Kemudian, tibalah pada tahap pemasangan yang sesungguhnya:

```
apt-get clean all
apt-get update
apt-get install ntopng
```

Perintah pertama akan menghapus cache dari manajer paket apt. Perintah kedua akan memperbarui daftar paket dan perintah ketiga akan menginstal NtopNG.

Setelah instalasi, perangkat lunak **NtopNG langsung tersedia di port 3000 pada mesin Debian**. Jadi bagi saya, ini adalah `http://192.168.1.23:3000`

![Image](assets/fr/022.webp)

Halaman beranda NtopNG

Login dan kata sandi default ditampilkan, jadi Anda tinggal memasukkannya!

## V. Menggunakan NtopNG

Saat Anda pertama kali masuk, hal pertama yang akan diminta untuk dilakukan adalah mengubah kata sandi admin default dan bahasa. Sayangnya, bahasa Prancis bukan salah satunya.


Anda kemudian tiba di dasboar:

![Image](assets/fr/023.webp)

Dasboar NtopNG



Jangan terbiasa dengan yang satu ini! Jika Anda melihat kotak kuning di bagian atas layar, Anda akan melihat kalimat: "*Lisensi akan berakhir pada 04:57*". Secara default, instalasi akan meluncurkan uji coba versi lengkap NtopNG, tetapi untuk waktu yang (sangat) terbatas. Setelah "hitungan mundur" ini tercapai, versi *community* diaktifkan dan dasbor berubah:

Jangan terganggu dengan yang ini! Jika Anda melihat kotak kuning di bagian atas layar, Anda akan melihat kalimat: "_Lisensi berakhir dalam 04:57_". Secara default, instalasi meluncurkan versi uji coba dari versi lengkap Ntopng, tetapi untuk waktu yang (sangat) terbatas. Setelah "hitungan mundur" ini tercapai, versi *community* diaktifkan dan dasbor berubah.

![Image](assets/fr/024.webp)

Dasbor *community* NtopNG yang baru

Hal pertama yang harus dilakukan adalah **memeriksa apakah interface yang benar sedang dalam posisi siap berkomunikasi**. Di sudut kiri atas, daftar drop-down interface yang tersedia memungkinkan Anda memilih interface yang kita tentukan di sini: br0.

![Image](assets/fr/025.webp)

Pilihan Interface

Window baru menampilkan "Top Flaw Talkers", yaitu perangkat yang paling banyak berkomunikasi. Di sini saya hanya memiliki dua stasiun yang muncul:

![Image](assets/fr/026.webp)

**Host sumber muncul di sebelah kiri, tujuan di sebelah kanan**. Ini memungkinkan Anda untuk memvisualisasikan penggunaan total bandwidth oleh setiap host, dan mendapatkan gambaran keseluruhan tentang lalu lintas jaringan. Itu tidak buruk, tapi kita bisa melangkah lebih jauh...

Jika saya mengklik "*Hosts*", misalnya, saya mendapatkan grafik yang menunjukkan konsumsi daya kirim dan terima dari setiap host di jaringan saya. Di sini, misalnya, saya dapat melihat bahwa 192.168.1.37 sendiri menyumbang 80% dari trafik saya.

![Image](assets/fr/027.webp)

Jika saya mengeklik IP Address dari host yang bersangkutan, saya diarahkan ke halaman ringkasan:

![Image](assets/fr/028.webp)

Saya dapat melihat, misalnya, bahwa itu adalah mesin VMWare (dengan mengenali YES dari alamat MAC saya), bahwa itu disebut DESKTOP-GHEBGV1 (jadi pastinya host Windows) DAN saya memiliki **statistik pada paket yang diterima dan dikirim, serta jumlah data.**

Anda juga akan melihat menu baru di bagian atas ringkasan ini. Saya sarankan Anda mengklik "**Apps**" untuk melihat apa yang mendorong begitu banyak lalu lintas:

![Image](assets/fr/017.webp)

Ha, sepertinya kita mendapatkan jawabannya! Pada grafik di sebelah kiri, **kita melihat bahwa 76,6% dari lalu lintasnya berasal dari... Windows Update**, jadi host ini sedang mengunduh pembaruan!

NtopNG menggunakan teknologi yang disebut DPI untuk *Deep Packet Inspection*, yang memungkinkannya untuk mengkategorikan setiap aliran jaringan dan mendefinisikan aplikasi (atau kelompok aplikasi) di belakangnya.

Untuk mendemonstrasikannya, saya memutar video YouTube pada host saya:

![Image](assets/fr/018.webp)

**Lalu lintas tersebut segera dikenali dan dikategorikan!**

Catatan: Untuk alasan yang jelas, perangkat lunak semacam ini dapat menimbulkan masalah privasi, jadi berhati-hatilah untuk menggunakannya dalam kondisi yang tepat. Perhatikan juga bahwa dimungkinkan untuk **menyamarkan hasil**, opsi tersebut dapat ditemukan di **Settings > Preferences > Misc** dan disebut "**Mask Host IP Address**".

## VI. Deteksi & peringatan

NtopNG juga mampu mengeluarkan peringatan keamanan pada feed tertentu. Peringatan ini dapat ditemukan di menu **Alerts**, di panel sebelah kiri. Di sini, misalnya, saya memiliki total 2851 peringatan, yang dibagi menjadi beberapa tingkat keparahan: Notice, Warning, dan Error.

![Image](assets/fr/019.webp)

Mari kita lihat peringatan dengan tingkat krusial tinggi, saya punya 17 di antaranya!

Mengklik angka ini akan menampilkan detail peringatan. Tidak ada yang mengkhawatirkan di sini, ini adalah positif palsu, di mana pengunduhan pembaruan dikategorikan sebagai transfer file biner dalam aliran HTTP, yang memang bisa berarti sebuah serangan.

![Image](assets/fr/020.webp)

Namun, karena saya menggunakan versi gratis, saya tidak bisa mengecualikan domain atau host yang menjadi sumber peringatan, jadi Anda harus terus mengawasinya agar tidak melewatkan sesuatu yang lebih mengkhawatirkan. NtopNG akan memberikan peringatan generate jika ada file :

Namun, karena saya menggunakan versi gratis, saya tidak dapat mengecualikan domain atau host yang menjadi sumber peringatan, jadi Anda harus terus mengawasinya untuk menghindari hilangnya sesuatu yang jauh lebih mengkhawatirkan. NtopNG akan menghasilkan peringatan jika terjadi:

- Pengunduhan file biner melalui HTTP
- Lalu lintas DNS yang mencurigakan
- Penggunaan port non-standar
- Deteksi SQL injection
- Cross-Site Scripting (XSS)
- Dll.

## VII. Kesimpulan

Dalam tutorial ini, kita telah melihat **cara mengatur sebuah probe dengan NtopNG** yang memungkinkan kita untuk **menganalisis lalu lintas jaringan kita** untuk memvisualisasikan penggunaan protokol dan okupansi setiap host, serta mendeteksi lalu lintas yang mencurigakan.

Sayangnya, saya tidak dapat meliput semua fitur dan kemungkinan dalam artikel ini, tetapi silakan jelajahi!

Solusi ini dapat diimplementasikan secara permanen di dalam infrastruktur perusahaan. NtopNG juga dapat mengekspor hasil ke database InfluxDB, memungkinkan Anda untuk membuat dasbor Anda sendiri dengan aplikasi pihak ketiga seperti Graphana.
