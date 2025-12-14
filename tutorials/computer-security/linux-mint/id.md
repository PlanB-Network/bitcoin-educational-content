---
name: Linux Mint

description: Menyiapkan komputer untuk transaksi bitcoin
---

![image](assets/cover.webp)

## Apa yang salah jika Anda menggunakan komputer biasa?

Saat melakukan transaksi Bitcoin, idealnya komputer Anda bebas dari malware. Tentu saja.

Meskipun Anda menyimpan seed phrase Bitcoin (umumnya terdiri dari 12 atau 24 kata) terpisah dari komputer dengan menggunakan perangkat penanda tangan (misalnya, dompet perangkat keras—yang merupakan fungsi utamanya), anggapan bahwa memiliki komputer "bersih" menjadi tidak terlalu penting adalah keliru.

Komputer yang terinfeksi malware dapat membaca alamat Bitcoin Anda, sehingga mengekspos saldo Anda kepada penyerang. Walaupun mereka tidak dapat mengambil Bitcoin hanya dengan mengetahui alamatnya, mereka dapat melihat jumlah kepemilikan Anda dan dari sana menilai apakah Anda merupakan target yang menguntungkan. Mereka mungkin dapat mengidentifikasi lokasi domisili Anda, dan menggunakan informasi tersebut untuk melakukan pemerasan, misalnya dengan mengancam keselamatan fisik atau anggota keluarga Anda demi mendapatkan tebusan.

## Apa solusinya?

Saya sangat menganjurkan sebagian besar Bitcoiner untuk menggunakan komputer khusus yang bebas malware (dengan akses internet) untuk melakukan transaksi Bitcoin. Saya menyarankan penggunaan sistem operasi open-source seperti Linux Mint, namun jika harus, gunakan Windows atau Mac – lebih baik daripada menggunakan komputer pribadi daripada yang sering dipakai bersama, yang hampir selalu memiliki malware tersembunyi di dalamnya.

Salah satu kendala yang dihadapi banyak orang adalah instalasi sistem operasi baru pada komputer tersebut. Panduan ini bertujuan untuk membantu mengatasi hal tersebut.

Terdapat banyak varian Linux, dan saya telah mencoba beberapa di antaranya. Rekomendasi saya bagi para Bitcoiner adalah Linux Mint, karena mudah diinstal, sangat cepat (terutama saat bootup dan shutdown), tidak berat (setiap perangkat lunak tambahan adalah risiko), dan jarang sekali mengalami crash atau berperilaku aneh (dibandingkan dengan versi lain seperti Ubuntu dan Debian).

Beberapa orang mungkin sangat enggan beralih ke sistem operasi baru, lebih memilih Windows atau macOS. Saya memahami hal tersebut, namun sistem operasi Windows dan Apple adalah sumber tertutup (closed source), sehingga kita harus memercayai apa yang mereka lakukan; saya tidak menganggap itu keputusan yang baik, tetapi bukan berarti ini adalah pilihan "semua atau tidak sama sekali". Saya jauh lebih memilih orang menggunakan komputer Windows atau macOS yang baru diinstal secara pribadi daripada komputer yang sering digunakan (dengan malware yang mungkin sudah menumpuk di dalamnya). Satu langkah lebih baik adalah menggunakan komputer Linux yang baru diinstal, yang akan saya demonstrasikan.

Jika Anda merasa cemas menggunakan Linux karena ketidakpahaman, itu wajar, tetapi meluangkan waktu untuk belajar juga merupakan hal yang wajar. Banyak sekali informasi yang tersedia secara online. Berikut adalah video singkat yang sangat saya rekomendasikan untuk memperkenalkan dasar-dasar command line.

Pilih komputer

Saya akan mulai dengan apa yang saya pikir adalah opsi terbaik. Kemudian saya akan memberikan pendapat saya tentang alternatifnya.

Opsi ideal:

Rekomendasi saya, jika Anda mampu, dan jika ukuran simpanan Bitcoin Anda mencukupi, adalah memilih laptop entry-level yang benar-benar baru. Model paling dasar yang dibuat saat ini sudah cukup untuk menangani apa yang akan digunakan. Spesifikasi prosesor dan RAM tidak terlalu berpengaruh, karena semuanya akan cukup baik.

Hindari:
- Kombinasi tablet apa pun, termasuk Surface Pro
- Chromebook – sering kali kapasitas penyimpanannya terlalu rendah
- Komputer apa pun dengan drive eMMC; Jika memiliki drive SSD, itu sempurna
- Mac – mereka mahal, dan perangkat kerasnya tidak cocok dengan sistem operasi Linux menurut pengalaman saya
- Apa pun yang diperbaharui (refurbished) atau bekas (2nd hand) (meskipun bukan penghalang mutlak)

Sebaliknya, carilah laptop Windows 11 (Saat ini Windows 11 adalah rilis terbaru. Kita akan menyingkirkan perangkat lunak itu, jangan khawatir.). Saya mencari di amazon.com untuk "Windows 11 Laptop" dan menemukan contoh yang baik ini:
![image](assets/1.webp)

Harga laptop yang di atas ini bagus. Spesifikasinya cukup memadai. Laptop ini memiliki kamera bawaan yang bisa kita gunakan untuk transaksi QR code PSBT (jika tidak ada, Anda perlu membeli kamera USB). Jangan khawatir jika mereknya kurang dikenal, karena harganya memang terjangkau. Jika Anda menginginkan merek yang lebih ternama, tentu biayanya akan lebih tinggi, contohnya:
![image](assets/2.webp)

Beberapa laptop dengan harga lebih murah hanya memiliki ruang penyimpanan 64GB. Saya belum menguji laptop dengan drive sekecil itu—mungkin OK hanya 64Gb, tapi mungkin cukup berisiko.

## Opsi Lain – Tails

Tails adalah sistem operasi yang dapat di-boot dari flash drive USB dan mengambil alih perangkat keras komputer mana pun secara sementara. Sistem ini hanya menggunakan koneksi Tor, jadi Anda harus merasa nyaman menggunakan Tor. Tidak ada data yang Anda tulis ke memori selama sesi akan disimpan ke drive (selalu mulai dari awal setiap kali) kecuali Anda mengubah pengaturan dan membuat opsi penyimpanan permanen (pada flash drive USB) – yang Anda kunci dengan kata sandi.

Ini bukan pilihan yang buruk dan gratis, tetapi sedikit kaku untuk tujuan kita. Menginstal perangkat lunak baru di dalamnya tidaklah mudah. Salah satu fitur bagusnya adalah sudah dilengkapi dengan Electrum, tetapi kekurangannya adalah Anda tidak menginstalnya sendiri. Pastikan flash drive USB yang Anda gunakan berkapasitas minimal 8 GB.

Fleksibilitas Anda berkurang jika Anda menggunakan Tails. Anda mungkin tidak dapat mengikuti berbagai panduan untuk menyiapkan apa yang Anda butuhkan dan membuatnya berfungsi dengan benar. Misalnya, jika Anda mengikuti panduan saya untuk menginstal Bitcoin Core, ada modifikasi yang diperlukan agar berfungsi. Saya rasa saya tidak akan membuat panduan khusus Tails, jadi Anda perlu membangun keterampilan dan melakukannya sendiri.

Saya juga tidak yakin seberapa baik dompet perangkat keras akan berinteraksi dengan OS ini.

Setelah mengatakan semua ini, komputer Tails untuk transaksi Bitcoin adalah opsi tambahan yang bagus, dan pasti akan membantu keterampilan privasi Anda secara keseluruhan untuk belajar menggunakan Tails.

## Opsi Lain – Boot OS Langsung

Ini sangat mirip dengan Tails, hanya saja sistem operasinya tidak didedikasikan untuk privasi. Cara dasar untuk menggunakannya adalah dengan mem-flash drive USB dengan sistem operasi Linux pilihan Anda, dan membuat komputer boot dari drive tersebut, bukan dari drive internal. Cara melakukannya akan dijelaskan nanti.

Keuntungannya adalah Anda kurang dibatasi dan segalanya akan berfungsi tanpa penyesuaian (tweak) tingkat lanjut.

Saya tidak yakin seberapa baik sistem semacam ini mengisolasi malware pada komputer yang ada dari drive boot USB yang Anda gunakan (yang berisi sistem operasi baru). Kemungkinan besar ini bekerja dengan baik, namun mungkin tidak sebaik Tails. Karena saya tidak yakin, preferensi saya adalah laptop khusus yang baru.

## Opsi Lain – Laptop atau komputer desktop bekas Anda

Menggunakan komputer bekas bukanlah ide yang ideal, terutama karena saya tidak mengetahui kerja dari malware yang canggih, atau jika menghapus drive cukup untuk menyingkirkan itu. Mungkin iya tapi saya tidak ingin meremehkan seberapa cerdik hacker jahat bisa. Anda bisa memutuskan, saya tidak ingin berkomitmen.
Menggunakan komputer bekas tidaklah ideal, terutama karena saya tidak memahami cara kerja malware canggih, juga apakah penghapusan (wiping) drive sudah cukup untuk menyingkirkannya. Kemungkinan besar cukup, tetapi saya tidak ingin meremehkan betapa cerdiknya para peretas jahat. Anda bisa memutuskan sendiri, saya tidak ingin melakukannya.

Jika Anda memilih untuk menggunakan komputer desktop lama daripada laptop lama, ini akan baik-baik saja, kecuali bahwa hal ini akan secara permanen memakan ruang untuk transaksi Bitcoin Anda yang mungkin jarang terjadi; Anda tidak boleh menggunakannya untuk hal lain. Sedangkan dengan laptop, Anda bisa menyimpannya, bahkan menyembunyikannya untuk keamanan ekstra.

## Menginstal Linux Mint di komputer apa pun

Instruksi ini bertujuan untuk menghapus sistem operasi apa pun dari laptop baru Anda dan menginstal Linux Mint, namun Anda dapat mengadaptasinya untuk menginstal hampir semua versi Linux pada hampir semua komputer.

Kita akan menggunakan komputer mana pun untuk mem-flash sistem operasi ke memory stick tertentu. Jenis memory stick tidak menjadi masalah, asalkan kompatibel dengan port USB, dan saya menyarankan kapasitas minimal 16GB.

Dapatkan salah satu dari benda ini:
![image](assets/3.webp)

Atau Anda bisa menggunakan sesuatu seperti ini:
![image](assets/4.webp)

Selanjutnya, menuju ke [linuxmint.com](https://linuxmint.com/)
![image](assets/5.webp)

Arahkan mouse ke menu Download di bagian atas, lalu klik tautan, “Linux Mint 20.3” atau versi terbaru yang direkomendasikan pada saat Anda melakukan ini.
![image](assets/6.webp)

Akan ada beberapa “rasa” yang bisa dipilih. Ikuti “Cinnamon” untuk mengikuti panduan ini. Klik tombol Download / Unduh.
![image](assets/7.webp)

Pada halaman berikutnya, Anda dapat bergeser ke bawah untuk melihat mirror (mirror adalah berbagai server yang menyimpan salinan file yang kita inginkan). Anda dapat memverifikasi unduhan menggunakan SHA256 dan gpg (disarankan), tetapi saya tidak akan menjelaskan hal itu di sini karena saya sudah menulis panduan tentangnya.
![image](assets/8.webp)

Pilih mirror yang paling dekat dengan Anda, lalu klik tautannya (teks hijau pada kolom mirror). File akan mulai diunduh (versi yang saya unduh berukuran 2,1 gigabyte).

Setelah terunduh, Anda dapat mem-flash file tersebut ke perangkat memori portabel dan menjadikannya bootable. Untuk melakukannya, cara termudah adalah menggunakan Balena Etcher. Unduh dan instal jika Anda belum memilikinya.

Kemudian jalankan:

![image](assets/9.webp)

Klik flash from file, dan pilih file LinuxMint yang Anda unduh.

Selanjutnya, klik Select target. Pastikan perangkat memori Anda sudah terpasang dan pastikan Anda memilih drive yang benar, jika tidak, Anda bisa merusak isi drive yang salah!

Setelah itu, pilih Flash! Anda mungkin perlu memasukkan kata sandi. Setelah selesai, drive tersebut kemungkinan besar tidak akan bisa dibaca oleh komputer Windows atau Mac Anda karena telah diubah menjadi perangkat Linux. Cukup cabut saja.

Menyiapkan komputer tujuan

Nyalakan laptop baru Anda, dan saat sedang booting, tekan dan tahan tombol BIOS. Biasanya ini adalah F2, tetapi bisa juga F1, F8, F10, F11, F12, atau Delete. Coba setiap tombol sampai berhasil, atau cari di internet model komputer Anda dan tanyakan pertanyaan yang tepat.

Contoh: "Tombol BIOS laptop Dell."

Setiap komputer akan memiliki menu BIOS yang berbeda. Jelajahi dan temukan menu mana yang memungkinkan Anda mengonfigurasi urutan boot. Untuk tujuan kita, kita ingin komputer mencoba boot dari perangkat yang terhubung via USB (jika ada yang terhubung), sebelum mencoba boot dari hard drive internal (jika tidak, Windows akan dimuat). Setelah Anda mengaturnya, Anda mungkin perlu menyimpan sebelum keluar atau mungkin tersimpan secara otomatis.

Reboot komputer dan seharusnya akan dimuat dari perangkat memori USB. Kita sekarang dapat menginstal Linux di drive internal dan Windows akan dihapus untuk selamanya.
Reboot komputer dan seharusnya akan memuat dari perangkat memori USB. Kita tidak dapat menginstal Linux di drive internal dan Windows akan dihapus secara permanen.

Ketika Anda mencapai layar berikut, pilih "OEM install (for manufacturers)". Jika Anda memilih "Start Linux Mint" sebagai gantinya, Anda akan mendapatkan sesi Linux Mint yang dimuat dari perangkat memori, tetapi setelah Anda mematikan komputer, tidak ada informasi Anda yang tersimpan – ini pada dasarnya adalah sesi sementara agar Anda bisa mencobanya.
![image](assets/10.webp)

Anda akan dipandu melalui wizard grafis yang akan mengajukan sejumlah pertanyaan yang seharusnya mudah dijawab. Salah satunya adalah pengaturan Bahasa, yang lain adalah koneksi jaringan internet rumah Anda dan kata sandi. Jika diminta untuk menginstal perangkat lunak tambahan, tolaklah. Ketika Anda sampai pada pertanyaan mengenai jenis instalasi, beberapa orang mungkin ragu—Anda perlu memilih "Erase disk and install Linux Mint" (Hapus disk dan instal Linux Mint). Selain itu, jangan enkripsi drive dan jangan pilih LVM.

Anda akhirnya akan sampai ke desktop. Pada titik ini, Anda belum sepenuhnya selesai. Anda sebenarnya bertindak sebagai produsen (yaitu seseorang yang membangun komputer dan menyiapkan Linux untuk pelanggan). Anda perlu mengeklik dua kali ikon desktop, "Install Linux Mint", untuk menyelesaikannya.
![image](assets/11.webp)

Ingat untuk mencabut memory stick, dan kemudian reboot. Setelah reboot, Anda akan menggunakan sistem operasi untuk pertama kalinya sebagai pengguna baru. Selamat.

Salah satu hal pertama yang perlu dilakukan (dan dilakukan secara teratur) adalah menjaga sistem tetap up-to-date.

Buka aplikasi Terminal, dan ketikkan berikut ini:

```bash
sudo apt-get update
```

tekan "Enter", konfirmasi pilihan Anda, dan kemudian ketik perintah ini:

```bash
sudo apt-get upgrade
```

tekan "Enter" dan konfirmasi pilihan Anda.

Biarkan perintah dijalankan, ini bisa memakan waktu beberapa menit.

Selanjutnya, saya suka menginstal Tor (sensitif huruf besar-kecil / case sensitive):

```bash
sudo apt-get install tor
```

> _TAMBAHAN: Anda juga dapat menjalankan boot Linux Mint dari "OEM install" (pastikan Anda terhubung ke internet, jika tidak, Anda bisa mendapatkan error). Jika Anda melakukan ini, Anda nanti perlu mengeklik ikon "ship to end user" yang seharusnya ada di desktop. Kemudian, Anda akan me-reboot dan memulai sistem operasi seolah-olah Anda membuka komputer untuk pertama kalinya._

Panduan ini menjelaskan mengapa Anda mungkin memerlukan komputer khusus untuk transaksi Bitcoin, dan bagaimana menginstal sistem operasi Linux Mint yang baru di dalamnya.
