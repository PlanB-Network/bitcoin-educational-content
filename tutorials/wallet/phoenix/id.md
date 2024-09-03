---
name: Phoenix

description: Mengatur dompet Phoenix Anda
---

![phoenix](assets/cover.webp)

## Pendahuluan

Phoenix adalah dompet lightning non-custodial yang dibuat oleh Acinq, tim di balik implementasi Lightning Eclair.

Perlu diingat bahwa Phoenix adalah aplikasi mobile yang berfokus pada pembayaran Lightning, namun masih mendukung pembayaran on-chain, melalui swap terintegrasi. Ini berarti setiap deposit on-chain ke Phoenix, akan langsung ditukar menjadi saluran Lightning.

Juga jika Anda ingin mengirim ke alamat on-chain, Phoenix akan melakukan swap secara internal dari saluran LN Anda ke tujuan on-chain. Harap sadar, semua swap ini memiliki biaya, karena melibatkan biaya on-chain.

Di bawah ini dalam bagian "Panduan Memulai" kami akan membahas proses pengaturan dan juga menjelaskan lebih lanjut tentang cara mengelola likuiditas lightning dengan Phoenix.

## Sumber Daya Penting
- Halaman web resmi Phoenix - [https://phoenix.acinq.co](https://phoenix.acinq.co)
- Halaman Dokumentasi / FAQ - [https://phoenix.acinq.co/faq](https://phoenix.acinq.co/faq)
- [Halaman Github](https://github.com/ACINQ/phoenix/) | [Halaman Rilis Github](https://github.com/ACINQ/phoenix/releases) (unduh apk langsung)
- [Dukungan dan diskusi](https://github.com/ACINQ/phoenix/discussions)
- [Blog Acinq](https://acinq.co/blog) - pengumuman

## Video Tutorial

![Phoenix: Tutorial Dompet Bitcoin Lightning](https://youtu.be/cbtAmevYpdM?si=zctujxtI0hI-jKpC)

## Panduan Memulai

Berikut adalah panduan langkah demi langkah cara memulai dengan Phoenix, pengaturan, melakukan/menerima pembayaran, mengelola likuiditas, proses cadangan/pemulihan.

### Unduh & Pengaturan
Anda dapat mengunduh dan menginstal Phoenix dari: [App Store](https://apps.apple.com/us/app/phoenix-wallet/id1544097028) | [Google Play Store](https://play.google.com/store/apps/details?id=fr.acinq.phoenix.mainnet) | [Unduh apk langsung](https://github.com/ACINQ/phoenix/releases)

Ikuti instruksi mulai dari layar Selamat Datang, langkah demi langkah.

![](assets/screenshot2.webp)

Anda akan diinformasikan tentang pembuatan saluran lightning secara otomatis.
Mulai dengan v2.0 adalah peningkatan besar yang membawa "splicing" ke Phoenix:
- saluran dinamis tunggal,
- tidak ada lagi biaya 1% pada likuiditas masuk
- prediktabilitas dan kontrol yang lebih baik
- swap tanpa kepercayaan

Periksa [postingan blog Phoenix](https://acinq.co/blog/phoenix-splicing-update) untuk detail lebih lanjut, terutama model biaya baru.

![](assets/screenshot3.webp)

### Panduan cepat likuiditas

Jadi, begitu Anda menerima/menyetor sats ke dalam dompet ini, secara otomatis akan membuka saluran dengan node ACINQ. Biasanya ukuran saluran akan sedikit lebih besar dari jumlah yang Anda setorkan. Jadi Anda akan selalu memiliki saluran baru untuk setiap setoran, kecuali ketika Anda belum sepenuhnya menguras saluran dan Anda menerima pembayaran yang lebih kecil, itu akan diisi ulang.

Untuk likuiditas Lightning Phoenix kami akan menyarankan skenario berikut:

Dengan versi baru v0.2.0 fitur LN baru splicing. Itu berarti dari sekarang Anda tidak perlu lagi berurusan dengan banyak saluran kecil baru untuk setiap pembayaran yang diterima.

Jika tidak ada cukup likuiditas masuk, Phoenix akan meningkatkan ukuran saluran awal Anda, tetapi itu masih akan menyiratkan biaya onchain. Anda dapat mengatur biaya tersebut bagaimanapun dalam pengaturan Phoenix, opsi pembayaran dan biaya.
Jadi, kami menyarankan untuk mulai menggunakan Phoenix dengan saluran yang besar, seperti 1-3-5M sats. Biaya komitmen Anda akan tidak signifikan dibandingkan dengan ukuran saluran dan tidak akan terlalu mempengaruhi Anda. Juga, daripada membayar 4-5 kali (atau berapapun kali Anda menyetor jumlah kecil) biaya minimal 3000 sats untuk setiap setoran, Anda hanya akan membayar sekali biaya pembukaan saluran.
Jika Anda mulai menghabiskan dari saluran tersebut, jangan habiskan semuanya, karena Phoenix akan menutupnya.

Jika Anda meninggalkan beberapa sats di saluran dan melakukan pengisian ulang dari dompet LN lain / sumber setoran lain, kami memiliki dua situasi untuk dipertimbangkan:
- dengan jumlah setoran baru yang lebih besar dari kapasitas saluran Anda, Phoenix akan mengubah ukuran saluran dan Anda akan membayar biaya tambahan.
- dengan jumlah setoran baru yang lebih rendah dari kapasitas saluran Anda, tidak akan ada biaya yang terlibat.

Jadi, coba ukur kapasitas saluran awal Anda sesuai dengan kebutuhan pribadi Anda untuk pengeluaran. Menghabiskan dan mengganti dalam batas saluran tidak akan menimbulkan biaya lagi dan pengalaman menggunakan aplikasi dompet ini akan lancar.

### Cadangan
Di layar berikut Anda akan diberitahu bahwa aplikasi Phoenix akan menghasilkan frasa benih sebagai cadangan untuk dompet Anda. Nanti kata-kata benih ini HARUS disimpan di tempat yang aman!

![](assets/screenshot4.webp)

Layar berikut menunjukkan jika Anda ingin membuat dompet baru atau mengembalikan dompet sebelumnya, dari frasa benih.

![](assets/screenshot5.webp)

Setelah dompet baru dibuat, Anda akan diberitahu bahwa Anda harus melakukan cadangan dari frasa benih. Klik tombol "Backup wallet".

![](assets/screenshot6.webp)

Anda akan diberitahu bahwa kata-kata dari benih ini sangat penting dan sensitif dan Anda harus menjaga mereka tetap pribadi.

![](assets/screenshot7.webp)

Kata-kata benih ini HARUS Anda simpan ke tempat yang aman, seperti manajer kata sandi ([KeePass](https://keepass.info/) atau [Bitwarden](https://bitwarden.com/)), menyimpan database dari manajer kata sandi ini ke dalam USB terenkripsi offline untuk keselamatan total.

![](assets/screenshot8.webp)

### Menerima pembayaran

Sebelum Anda mulai menerima, silakan baca bab di atas "Panduan Likuiditas Cepat".

Jadi sekarang, Anda siap untuk menerima sats ke dalam dompet Phoenix Anda!

![](assets/screenshot9.webp)

Untuk menerima pembayaran, di Phoenix Anda memiliki opsi berikut:
- dengan menggunakan kode QR yang ditampilkan, mewakili faktur Lightning "kosong"
- dengan mengedit faktur Lightning (lihat tombol edit di bawah kode QR), di mana Anda dapat menambahkan jumlah sats, menambahkan komentar yang ditampilkan kepada pembayar
- dengan menggunakan / memindai kode QR LNURL-withdraw
- dengan menghasilkan alamat Bitcoin on-chain dari dompet Phoenix Anda. Ingat bahwa pembayaran ini akan "dikonversi" menjadi saluran Lightning baru (jika Anda belum membuka satu) atau mengubah ukuran saluran Lightning yang ada.

![](assets/screenshot10.webp)

Layar yang ditampilkan untuk mengedit faktur Lightning baru dan menghasilkan kode QR baru untuk itu:

![](assets/screenshot11.webp)

Ini adalah layar di mana Anda dapat menghasilkan alamat BTC on-chain dan diberitahu bahwa pembayaran ke alamat ini akan "dikonversi" menjadi likuiditas lightning dan melibatkan beberapa biaya.

![](assets/screenshot12.webp)

Setelah pembayaran selesai, akan ditampilkan layar konfirmasi, semua selesai!

![](assets/screenshot13.webp)
Anda dapat menambahkan catatan pribadi pada setiap pembayaran yang diterima. Catatan ini tidak disimpan di tempat lain, hanya disimpan di perangkat Anda. Jika Anda mengembalikan dompet Phoenix Anda, catatan ini tidak akan dikembalikan. Ini adalah fitur yang berguna untuk melacak pembayaran yang dikirim dan diterima.
![](assets/screenshot14.webp)

### Mengirim Pembayaran

Untuk mengirim pembayaran adalah proses yang cukup sederhana, cukup klik tombol di layar utama "Kirim"

![](assets/screenshot15.webp)

Anda akan diminta untuk mengizinkan aplikasi Phoenix mengakses kamera perangkat, agar dapat memindai kode QR.

![](assets/screenshot16.webp)

Di layar pembayaran, Anda memiliki 3 opsi:
- memindai kode QR dari faktur penerima Lightning / LNURL
- memasukkan secara manual (tempel), masukan Alamat Lightning atau kode LNURL-pay
- memuat gambar QR dari disk lokal

![](assets/screenshot17.webp)

Seperti yang Anda lihat di layar ini, permintaan pembayaran telah dipindai dan detailnya sudah terisi. Anda hanya perlu menekan tombol "Bayar".

![](assets/screenshot18.webp)

Setelah pembayaran dikirim dan dikonfirmasi, akan ditampilkan layar konfirmasi dengan detail singkat pembayaran, termasuk biaya yang dibayar. Jika Anda ingin melihat lebih banyak detail pembayaran, klik tombol "Detail".

![](assets/screenshot19.webp)

Di layar detail, Anda dapat melihat detail teknis pembayaran, termasuk: hash pembayaran dan permintaan, preimage, node tujuan, dan durasi. Terkadang detail ini berguna untuk melacak pembayaran, debug atau mengidentifikasi dengan penerima pembayaran tertentu.

![](assets/screenshot20.webp)

### Pengaturan

Di menu Pengaturan, tidak terlalu banyak yang harus dilakukan, Phoenix mengutamakan kesederhanaan. Namun, satu aspek penting di sini adalah menu untuk mengelola saluran pembayaran dan biaya, di mana Anda dapat menetapkan tingkat biaya yang diinginkan. Ingatlah bahwa dalam lingkungan mempool dengan biaya tinggi Anda sebaiknya tidak menggunakan biaya yang sangat rendah, jika tidak pembayaran Anda dan pembukaan saluran akan terganggu dan/atau gagal.

Opsi lain di menu Pengaturan:
- Tampilan - untuk beralih ke tema warna yang berbeda
- Server Electrum - untuk memeriksa status server Electrum yang Anda terhubung atau menentukan satu
- Tor - jika Anda ingin menggunakan Phoenix di belakang jaringan Tor
- Pengaturan akses aplikasi - menetapkan izin untuk Phoenix ke layanan perangkat tertentu
- Frase pemulihan - jika Anda ingin memeriksa kata-kata benih dan/atau membuat cadangan baru
- Daftar saluran - menampilkan status saluran Lightning Anda dan likuiditas (masuk/keluar) yang tersedia
- Log - menampilkan log debugging
- Tutup semua saluran - Opsi berbahaya yang harus digunakan HANYA jika Anda ingin menutup node Phoenix Anda secara permanen dan memulihkan dana ke alamat onchain Anda. Alamat tersebut nantinya dapat diambil menggunakan dompet Electrum, menggunakan frase benih Phoenix Anda.

![](assets/screenshot21.webp)

### Atur Ulang

Jika Anda berada dalam situasi bahwa aplikasi Phoneix Anda mengalami masalah (tidak melakukan pembayaran, tidak terhubung ke server Electrum, tidak dapat menerima pembayaran) atau Anda hanya ingin memindahkannya ke perangkat lain, Anda HARUS memastikan dua aspek:
- memiliki cadangan frase benih Anda
- hentikan aplikasi di perangkat Anda - pergi ke detail aplikasi dan paksa hentikan layanan
- copot pemasangannya dari perangkat lama jika Anda ingin memindahkannya ke yang baru
- JANGAN menjalankan dompet Phoenix yang sama di beberapa perangkat!

![](assets/screenshot22.webp)

Setelah Anda menginstal ulang atau memasangnya di perangkat baru, klik tombol "Pulihkan" dan ikuti instruksinya

![](assets/screenshot23.webp)
Anda tidak dapat menggunakan jenis benih lain, yang dihasilkan dari aplikasi dompet lain. [Lihat lebih banyak detail di sini](https://walletsrecovery.org/) tentang jenis dompet lain dan jenis benih serta jalur derivasi mereka. Tidak semua kompatibel!
![](assets/screenshot24.webp)

Anda harus memasukkan kata-kata benih yang telah disimpan sebelumnya, satu per satu, dalam urutan yang spesifik. Setelah Anda selesai memasukkan 12 kata, klik tombol "Impor" dan selesai.

![](assets/screenshot25.webp)

Dalam beberapa saat Anda akan melihat saldo sebelumnya Anda ditampilkan. Juga, Anda akan mendapatkan peringatan untuk membuat cadangan benih Anda. Anda bisa langsung pergi ke menu dan pilih "Saya telah menyimpan cadangan" jika Anda sudah melakukannya.

![](assets/screenshot26.webp)

Selesai! Selamat menikmati Lightning!