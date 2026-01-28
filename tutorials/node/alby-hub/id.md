---
name: Alby Hub
description: Bagaimana cara mudah meluncurkan simpul Lightning kamu sendiri?
---
![cover](assets/cover.webp)

Alby Hub adalah perangkat lunak open-source terbaru dari Alby, perusahaan di balik ekstensi web Lightning yang populer. Alby Hub adalah dompet dengan kendali sendiri yang paling mudah digunakan dengan node Lightning, dapat diakses dari mana saja untuk terintegrasi dengan banyak aplikasi. Alby Hub adalah antarmuka yang mudah digunakan untuk mengelola node Lightning.

Dalam tutorial ini, kita akan melihat berbagai cara menggunakan Alby Hub dan bagaimana menghubungkannya dengan Alby Go, aplikasi seluler Alby, atau Alby Browser Extension. Ini akan memungkinkan kamu menghabiskan sats kamu saat bepergian sambil tetap mandiri dalam mengelola node kamu.

![ALBY HUB](assets/fr/01.webp)

## Apa yang dimaksud dengan Alby Hub?

Alby Hub disiapkan untuk menjadi alat unggulan baru dalam ekosistem Alby. Perangkat lunak ini memungkinkan pengguna untuk dengan mudah mengelola dompet self-custodial mereka sendiri dengan node Lightning terintegrasi, sambil tetap mempertahankan kepemilikan kunci mereka sendiri (self-custody).

Alby Hub adalah alat yang sangat mudah beradaptasi. Alat ini bisa memenuhi kebutuhan pengguna pemula dan pengguna tingkat lanjut. Para pemula bisa menggunakannya untuk mengoperasikan node Lightning sungguhan dengan mudah, tanpa harus berurusan dengan kerumitan yang mendasarinya. Untuk pengguna yang lebih berpengalaman, Alby Hub bisa digunakan sebagai antarmuka lengkap untuk manajemen tingkat lanjut dari node Lightning yang sudah ada.

Tergantung pada kebutuhan kamu, Alby Hub tersedia dalam 4 konfigurasi:


- Alby Hub Cloud: **Awan Alby**

Ideal untuk pemula, opsi pertama ini adalah opsi cloud Alby. Ini memungkinkan kamu mengimplementasikan Hub langsung di server yang dikelola oleh Alby, dan bisa diakses melalui antarmuka Alby Hub kamu. Meskipun Alby mengelola server, kamu tetap memiliki kedaulatan atas dana kamu, karena kunci kamu dienkripsi menggunakan kata sandi yang hanya kamu yang tahu. Namun, kunci kamu harus tetap didekripsi di RAM agar node bisa beroperasi, yang secara teoritis mengeksposnya ke risiko jika seseorang mengakses server secara fisik. Ini adalah kompromi yang menarik untuk pemula, tapi penting untuk menyadari risikonya.

Keuntungan utama dari opsi ini adalah kamu mendapatkan node Lightning yang aktif dan berjalan 24/7 tanpa harus mengelola hosting sendiri. Selain itu, pencadangan node Lightning kamu disederhanakan dan diotomatisasi, dibandingkan dengan opsi hosting mandiri yang mengharuskan kamu mengelola sendiri pencadangan saluran.

Alby Cloud adalah layanan berbayar [Periksa harga mereka](https://albyhub.com/#pricing) untuk lebih jelasnya. BBiaya akan otomatis dipotong dari dompet kamu melalui faktur Lightning yang diterbitkan oleh Alby. Ini bekerja lewat koneksi NWC yang mengatur node kamu untuk membayar faktur langganan Alby secara otomatis.

- Alby Hub dengan node yang sudah ada :**

Jika kamu sudah memiliki node yang dihosting, misalnya di Umbrel atau Start9, Alby Hub bisa digunakan sebagai antarmuka manajemen tingkat lanjut, sama seperti ThunderHub atau RTL.


- Alby Hub lokal: **Lokal**

Kamu juga bisa menginstal Alby Hub langsung di PC, meskipun opsi ini kurang praktis karena PC harus selalu menyala agar node Lightning bisa diakses dari jarak jauh. Namun, cara ini mungkin cocok untuk kebutuhan spesifik kamu.


- Alby Hub di server pribadi :**

Untuk pengguna tingkat lanjut, Alby Hub bisa dijalankan di server pribadi dengan perintah sederhana. Opsi ini tidak dibahas dalam tutorial ini, tapi kamu bisa menemukan instruksi lengkapnya di sini. [di GitHub Alby](https://github.com/getAlby/hub?tab=readme-ov-file#docker).

Tutorial ini fokus terutama pada antarmuka, yang akan sama untuk semua opsi. Kita juga akan membahas cara menggunakan Alby Hub dengan opsi cloud berbayar, lalu dengan opsi node-in-box seperti Umbrel atau Start9.

![ALBY HUB](assets/fr/02.webp)

Untuk instalasi lokal pada PC, [unduh dan instal perangkat lunak sesuai dengan sistem operasi](https://github.com/getAlby/hub/releases), kemudian ikuti petunjuk yang sama pada antarmuka.

![ALBY HUB](assets/fr/03.webp)

## Membuat akun Alby

Langkah pertama adalah membuat akun Alby. Meskipun tidak wajib untuk menggunakan Alby Hub, akun ini memungkinkan kamu memanfaatkan semua opsi yang tersedia, termasuk mendapatkan alamat Lightning.

Kunjungi [situs web resmi Alby](https://getalby.com/) dan klik tombol "*Buat Akun*".

![ALBY HUB](assets/fr/04.webp)

Masukkan nama panggilan dan alamat email, lalu klik "*Daftar*". Alamat email ini akan digunakan untuk masuk ke akun nanti.

![ALBY HUB](assets/fr/05.webp)

Masukkan kode verifikasi yang kamu terima melalui email.

![ALBY HUB](assets/fr/06.webp)

Setelah masuk ke akun online, klik tombol "*Lanjutkan*".

![ALBY HUB](assets/fr/07.webp)

Klik "*Lanjutkan*" sekali lagi.

![ALBY HUB](assets/fr/08.webp)

## Opsi hosting awan

Selanjutnya, kamu harus memilih antara opsi self-hosted, di mana Alby Hub diinstal di perangkat sendiri, atau opsi premium. Aku akan mulai dengan menjelaskan cara menggunakan opsi Pro Cloud (ingat, ini adalah opsi berbayar, lihat detailnya di bagian sebelumnya).

Klik "*Upgrade*".

![ALBY HUB](assets/fr/09.webp)

Konfirmasikan dengan mengklik "*Langganan Sekarang*".

![ALBY HUB](assets/fr/10.webp)

Klik "*Luncurkan Alby Hub*".

![ALBY HUB](assets/fr/11.webp)

Tunggu beberapa saat sementara node kamu dibuat.

![ALBY HUB](assets/fr/12.webp)

Dan itu saja, Alby Hub kamu sekarang sudah dikonfigurasi. Di bagian berikutnya, aku akan tunjukkan cara menginstal Alby Hub di node yang sudah ada. Jika kamu belum punya node Lightning, kamu bisa langsung lanjut ke bagian berikut untuk mengonfigurasi Alby Hub di Alby Cloud.


![ALBY HUB](assets/fr/13.webp)

## Opsi hosting mandiri

Jika kamu lebih suka menggunakan Alby Hub sebagai antarmuka untuk node Lightning yang sudah ada, ada beberapa opsi: menginstalnya di server, secara lokal di komputer, atau melalui node-in-box seperti Umbrel atau Start9. Menggunakan Alby Hub dengan konfigurasi ini tidak dikenai biaya. Kita akan fokus pada opsi node-in-box, karena menurutku opsi server tanpa akses fisik punya risiko serupa dengan versi cloud, dan instalasi lokal di PC seringkali kurang praktis.

Untuk menyiapkannya di Umbrel (langkah-langkah untuk Start9 sama), kamu harus terlebih dahulu memiliki node LND yang sudah dikonfigurasi.

Masuk ke antarmuka Umbrel dan buka toko aplikasi.

![ALBY HUB](assets/fr/14.webp)

Cari aplikasi "*Alby Hub*".

![ALBY HUB](assets/fr/15.webp)

Instal di node kamu.

![ALBY HUB](assets/fr/16.webp)

Antarmuka Alby Hub kamu sekarang sudah siap. Kamu bisa mengikuti tutorial berikut seolah-olah menggunakan antarmuka cloud, tapi tanpa opsi berbayar. Selain itu, berbeda dengan versi cloud, kunci kamu disimpan secara lokal di node, bukan di server Alby.

![ALBY HUB](assets/fr/17.webp)

## Meluncurkan Alby Hub

Klik tombol "*Mulai*".

![ALBY HUB](assets/fr/18.webp)

Alby Hub kemudian akan meminta kamu memilih kata sandi. Kata sandi ini sangat penting karena digunakan untuk mengenkripsi dompet kamu. Pada versi cloud berbayar, kunci disimpan di server Alby, dienkripsi dengan kata sandi yang hanya kamu tahu, lalu didekripsi dan disimpan di RAM hanya saat diperlukan untuk menandatangani transaksi.

Karena itu, penting untuk memilih kata sandi yang kuat. Siapa pun yang memiliki kata sandi ini bisa berpotensi mengakses node kamu. Pastikan juga membuat satu atau lebih cadangan fisik dari kata sandi ini di kertas, atau lebih baik lagi, di logam untuk keamanan ekstra.

Setelah memilih dan menyimpan kata sandi dengan aman, klik *Buat Kata Sandi*.

![ALBY HUB](assets/fr/19.webp)

Sekarang kamu sudah memiliki akses ke node Lightning kamu.

![ALBY HUB](assets/fr/20.webp)

Langkah pertama adalah menyimpan seedphrase kamu, dari mana kunci kamu dibuat. Untuk melakukannya, klik "Pengaturan". Seedphrase ini memungkinkan kamu memulihkan akses ke dompet jika cadangan otomatis diaktifkan.

![ALBY HUB](assets/fr/21.webp)

Lalu buka tab "*Cadangan*". Masukkan kata sandi kamu untuk mengaksesnya.

![ALBY HUB](assets/fr/22.webp)

Kamu kemudian akan melihat seedphrase 12 kata kamu. Buat satu atau beberapa salinan fisik dari seedphrase ini di kertas atau logam, dan simpan di tempat yang aman.

![ALBY HUB](assets/fr/23.webp)

Setelah menyimpan seedphrase, centang kotak untuk mengonfirmasi bahwa kamu sudah menyimpannya, lalu klik "Lanjutkan".

![ALBY HUB](assets/fr/24.webp)

## Bagaimana cara memulihkan akses ke bitcoin saya?

Sebelum mengirimkan dana ke Alby Hub kamu, penting untuk memahami cara memulihkannya jika terjadi masalah, serta informasi apa yang dibutuhkan untuk pemulihan. Proses ini berbeda tergantung pada jenis dana dan mode hosting node kamu.

Untuk pengguna cloud berbayar, pemulihan penuh bitcoin membutuhkan tiga elemen penting:

- Seedphrase kamu;
- Akses ke akun Alby kamu untuk mengambil cadangan otomatis.

Jika salah satu dari dua informasi ini tidak tersedia, pemulihan bitcoin kamu menjadi tidak mungkin.

Bagi mereka yang menjalankan Alby Hub di perangkat mereka sendiri, proses pemulihan didokumentasikan [di sini](https://guides.getalby.com/user-guide/alby-account-and-browser-extension/alby-hub/backups-and-recover#alby-hub-self-hosted-with-an-alby-account).

Kalau kamu menginstal Alby Hub di node yang sudah ada, kamu perlu mengikuti proses pemulihan dari sistem operasi node tersebut. Misalnya: Umbrel menawarkan [opsi](https://github.com/getumbrel/umbrel/blob/2b266036f62a1594aa60a8a3be30cfb8656e755f/scripts/backup/README.md) untuk mengenkripsi status terbaru dari saluran Lightning kamu dan menyimpannya secara dinamis dan anonim melalui Tor. Perlu diingat, hanya cadangan otomatis dari Alby yang memungkinkan kamu memulihkan Hub sepenuhnya tanpa menutup saluran apa pun.

## Beli saluran Lightning pertama Anda

Sekarang kamu bisa mengikuti instruksi yang diberikan oleh Alby Hub. Klik tombol untuk membuka saluran pertama kamu agar bisa menerima dana.

![ALBY HUB](assets/fr/25.webp)

Pilih "*Saluran Terbuka*". Jika kamu tidak berniat menjadi node perutean dan tidak membutuhkannya secara khusus, aku sarankan memilih saluran pribadi.

![ALBY HUB](assets/fr/26.webp)

Alby Hub akan membuat faktur untuk kamu bayar. Pembayaran ini mencakup biaya transaksi untuk membuka saluran, serta biaya layanan LSP (*Lightning Service Provider*) yang akan membuka saluran ke node kamu, sehingga kamu bisa langsung menerima pembayaran.

![ALBY HUB](assets/fr/27.webp)

Setelah faktur dibayar dan transaksi dikonfirmasi, saluran Lightning pertama kamu sudah berhasil dibuat.

![ALBY HUB](assets/fr/28.webp)

Di tab "*Node*", kamu bisa melihat bahwa kamu sekarang memiliki dana masuk, yang memungkinkan menerima pembayaran lewat Lightning.

![ALBY HUB](assets/fr/29.webp)

Untuk menerima pembayaran, klik tab "*Dompet*" lalu "*Terima*".

![ALBY HUB](assets/fr/30.webp)

Masukkan jumlah dan tambahkan deskripsi jika perlu, lalu klik "*Buat Faktur*".

![ALBY HUB](assets/fr/31.webp)

Aku menerima pembayaran pertamaku sebesar 120.000 sat.

![ALBY HUB](assets/fr/32.webp)

Kembali ke tab "Dompet", kamu bisa memeriksa saldo dompet. Perlu diperhatikan, Alby Hub secara otomatis menyisihkan 354 sat saat pembayaran pertama dilakukan. Untuk setiap saluran Lightning berikutnya yang dibuka, Alby Hub akan otomatis menyisihkan cadangan sebesar 1% dari kapasitas saluran. Cadangan ini berfungsi sebagai langkah keamanan, memungkinkan node memulihkan dana saluran jika ada upaya penipuan dari rekan. Itulah sebabnya, meskipun aku mengirim 120.000 sat, saldo yang ditampilkan hanya 119.646 sat.

![ALBY HUB](assets/fr/33.webp)

## Menyimpan bitcoin di rantai

Jika kamu ingin memiliki dana keluar untuk melakukan pembayaran, kamu juga bisa membuka saluran sendiri. Untuk ini, kamu memerlukan bitcoin on-chain di dompet kamu.

Dari tab "*Node*", klik "*Deposit*".

![ALBY HUB](assets/fr/34.webp)

Kirim bitcoin ke alamat yang ditampilkan. Alamat ini berasal dari frasa pemulihan yang kamu simpan sebelumnya.

![ALBY HUB](assets/fr/35.webp)

Aku telah mengirim 72.000 satoshi. Sekarang terlihat di tab "Saldo Tabungan", yang mencakup semua dana on-chain yang kamu miliki, bukan di Lightning.

![ALBY HUB](assets/fr/36.webp)

## Buka saluran Lightning

Setelah memiliki dana on-chain, kamu bisa membuka saluran Lightning baru. Disarankan membuka beberapa saluran dengan jumlah yang cukup agar selalu bisa melakukan pembayaran tanpa kendala. Sebagian besar LSP (*Lightning Service Provider*) meminta minimal 150.000 sat untuk membuka saluran dengan kamu.

Pada tab "*Node*", klik "*Open Channel*".

![ALBY HUB](assets/fr/37.webp)

Pilih ukuran saluran kamu. Aku sarankan untuk tidak membuka saluran terlalu kecil, karena ini adalah node Lightning dan perangkat yang menyimpan kunci kamu tidak menawarkan tingkat keamanan seperti dompet perangkat keras. Jadi, berhati-hatilah dengan jumlah yang kamu pilih untuk diblokir.

![ALBY HUB](assets/fr/38.webp)

Di menu "*Opsi Lanjutan*", Kamu bisa memilih LSP yang akan digunakan untuk membuka saluran, atau memasukkan node Lightning lain secara manual.

![ALBY HUB](assets/fr/39.webp)

Kemudian klik "*Buka Saluran*".

![ALBY HUB](assets/fr/40.webp)

Tunggu sementara saluran kamu dikonfirmasi di rantai.

![ALBY HUB](assets/fr/41.webp)

Saluran baru kamu sekarang akan muncul di tab "*Node*".

![ALBY HUB](assets/fr/42.webp)

## Manajemen Node

Mengelola saluran Lightning lebih mudah dari yang kamu kira. Alby Hub memungkinkan kamu memindahkan sats antara saldo pengeluaran dan saldo on-chain, sehingga kamu bisa menambah kapasitas untuk membayar atau menerima pembayaran.

![ALBY HUB](assets/fr/66.webp)


## Menghubungkan aplikasi pengeluaran

Sekarang, setelah node Lightning kamu berfungsi, kamu bisa menggunakannya untuk menerima dan membelanjakan sats setiap hari. Meski antarmuka web Alby Hub berguna untuk mengelola node, ini kurang ideal untuk transaksi cepat saat bepergian. Untuk itu, kita akan menggunakan aplikasi dompet Lightning di ponsel.

Dalam tutorial ini, aku sarankan menggunakan Alby Go karena sangat mudah digunakan, tapi kamu juga bisa memakai aplikasi lain yang kompatibel, seperti Zeus.

![ALBY HUB](assets/fr/43.webp)

Untuk menginstal Alby Go, buka toko aplikasi di perangkat kamu:


- [Untuk Android](https://play.google.com/store/apps/details?id=com.getalby.mobile);
- [Untuk Apple](https://apps.apple.com/us/app/alby-go/id6471335774).

![ALBY HUB](assets/fr/44.webp)

Pengguna Android juga dapat menginstal aplikasi ini melalui file `.apk` [tersedia di GitHub Alby](https://github.com/getAlby/go/releases).

![ALBY HUB](assets/fr/45.webp)

Ketika aplikasi diluncurkan, klik "*Hubungkan Dompet*".

![ALBY HUB](assets/fr/46.webp)

Di Alby Hub kamu, di bawah App Store, temukan “Alby Go” dan klik “Connect”  
![ALBY HUB](assets/fr/47.webp)  
Klik “Connect with One-Tab Connections”. Ini akan memungkinkan kamu menghubungkan Alby Hub ke aplikasi lain yang menggunakan Alby Go hanya dengan satu klik. 

![ALBY HUB](assets/fr/48.webp)  

Alby Hub kemudian akan membuat kunci rahasia untuk membangun koneksi dengan Alby Go.

![ALBY HUB](assets/fr/49.webp)

Kembali ke aplikasi Alby Go, pindai kode QR atau tempelkan rahasianya.

![ALBY HUB](assets/fr/50.webp)

Klik "Selesai".

![ALBY HUB](assets/fr/51.webp)

Sekarang kamu punya akses jarak jauh ke node Lightning yang didukung Alby Hub lewat ponsel, sehingga lebih mudah mengirim dan menerima sats saat bepergian setiap hari.


![ALBY HUB](assets/fr/52.webp)

Jika perlu, kamu bisa mengelola izin untuk koneksi ini langsung di Alby Hub dengan mengkliknya.

![ALBY HUB](assets/fr/53.webp)

Untuk menerima sats, cukup klik "*Terima*".

![ALBY HUB](assets/fr/54.webp)

Ubah jumlah dan deskripsi faktur dengan mengklik "*Faktur*".

![ALBY HUB](assets/fr/55.webp)

Tagih faktur untuk menerima sat.

![ALBY HUB](assets/fr/56.webp)

Untuk mengirim sat, klik "*Kirim*".

![ALBY HUB](assets/fr/57.webp)

Pindai faktur yang ingin kamu bayar.

![ALBY HUB](assets/fr/58.webp)

Kemudian klik "*Bayar*".

![ALBY HUB](assets/fr/59.webp)

Transaksi kamu telah dikonfirmasi.

![ALBY HUB](assets/fr/60.webp)

Dengan mengklik tanda panah kecil, kamu bisa mengakses riwayat transaksi kamu..

![ALBY HUB](assets/fr/61.webp)

Transaksi ini juga dapat dilihat di Alby Hub milikmu.

![ALBY HUB](assets/fr/62.webp)

## Menyesuaikan alamat Lightning Anda

Alby menawarkan opsi alamat Lightning, sehingga kamu bisa menerima pembayaran di node tanpa membuat faktur secara manual setiap kali. Secara default, Alby memberi kamu alamat Lightning, tapi kamu bisa menyesuaikannya. Masuk ke akun Alby online, klik nama kamu di sudut kanan atas, lalu pilih "*Pengaturan*".

![ALBY HUB](assets/fr/63.webp)

Navigasikan ke menu "*Lightning Address*".

![ALBY HUB](assets/fr/64.webp)

Ubah alamat kamu, lalu konfirmasikan dengan mengklik "*Perbarui alamat lightning Anda*".

![ALBY HUB](assets/fr/65.webp)

Perlu diingat bahwa setelah alamat kamu diubah, alamat tersebut tidak lagi menjadi milikmu. Jadi, pastikan kamu tidak akan pernah mengirim sat lagi ke alamat tersebut.

Dan itu saja, sekarang kamu tahu cara menggunakan Lightning dengan node kamu sendiri menggunakan Alby Hub. Jika kamu merasa tutorial ini bermanfaat, aku akan sangat berterima kasih jika kamu memberi jempol hijau di bawah ini. Jangan ragu membagikan artikel ini di jejaring sosial kamu. Terima kasih banyak!

Untuk memahami secara detail semua mekanisme Lightning yang telah kami manipulasi dalam tutorial ini, aku sangat menyarankan kamu mengikuti pelatihan gratis kami tentang subjek ini :

https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
