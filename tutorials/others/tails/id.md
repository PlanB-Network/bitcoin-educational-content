---
name: Tails

description: Menginstal Tails pada kunci USB
---

![image](assets/cover.webp)

Sistem operasi portabel dan amnesia yang melindungi Anda dari pengawasan dan sensor.

## Mengapa memiliki kunci USB dengan Tails terinstal?

Tails (https://tails.boum.org/) adalah cara termudah untuk memiliki komputer aman yang selalu tersedia kapan saja, yang tidak akan meninggalkan jejak apa pun pada komputer yang Anda gunakan bersamanya.

Untuk menggunakan Tails, matikan komputer yang Anda miliki akses kepadanya (di rumah orang tua Anda, di rumah teman Anda, di kafe internet...) dan mulailah dengan kunci USB Tails Anda sebagai gantinya dari Windows, macOS, atau Linux.

Setelah itu, Anda akan memiliki lingkungan kerja dan komunikasi yang independen dari sistem operasi biasa dan tidak pernah menggunakan hard drive.

Tails tidak pernah menulis ke hard drive dan hanya menggunakan RAM komputer untuk berfungsi. Memori ini sepenuhnya dihapus ketika Tails dimatikan, sehingga menghilangkan semua jejak yang mungkin ada.

## Beberapa kasus penggunaan konkret

Untuk memberi Anda ide konkret tentang manfaat selalu memiliki kunci USB dengan Tails, berikut adalah daftar kecil yang tidak lengkap yang disusun oleh tim Agora256:

- Terhubung ke Internet dan Tor secara tidak disensor dan anonim untuk menjelajahi situs web tanpa meninggalkan jejak;
- Membuka PDF dari situs web yang mencurigakan;
- Menguji cadangan kunci pribadi Bitcoin Anda dengan dompet Electrum;
- Menggunakan paket office (LibreOffice) dan bekerja di komputer yang bukan milik Anda;
- Mengambil langkah pertama Anda dalam lingkungan Linux untuk belajar cara meninggalkan dunia Microsoft dan Apple.

## Bagaimana cara mempercayai Tails?

Selalu ada elemen kepercayaan dalam menggunakan perangkat lunak, tetapi itu tidak harus buta. Alat seperti Tails harus berusaha untuk memberikan penggunanya sarana untuk dapat dipercaya. Untuk Tails, ini berarti:

- Kode sumber publik: https://gitlab.tails.boum.org/;
- Proyek berbasis pada proyek terkemuka: Tor dan Debian;
- Unduhan yang dapat diverifikasi dan direproduksi;
- Rekomendasi oleh berbagai individu dan organisasi.

## Panduan Instalasi dan Penggunaan

Tujuan dari panduan instalasi ini adalah untuk memandu Anda melalui setiap langkah instalasi. Kami tidak akan mendeskripsikan tindakan yang harus diambil lebih dari panduan resmi, tetapi kami akan menunjukkan Anda arah yang benar sambil memberi Anda tips dan trik.

Untuk alasan pengalaman praktis, tips ini akan difokuskan pada platform macOS dan Linux.
🛠️
Sebelum memulai prosedur ini, pastikan Anda memiliki kunci USB dengan kecepatan baca minimal 150 MB/s dan kapasitas minimal 8 GB, idealnya USB 3.0.

Prasyarat:

- 1 kunci USB, hanya untuk Tails, dengan kapasitas minimal 8 GB
- Komputer yang terhubung ke Internet dengan Linux, macOS, (atau Windows)
- Sekitar satu jam waktu luang, tergantung pada kecepatan koneksi Internet Anda, termasuk ½ jam untuk instalasi (file 1.3 GB untuk diunduh)

## Langkah 1: Unduh Tails dari komputer Anda

![image](assets/1.webp)

> 🔗 Bagian Tails resmi: https://tails.boum.org/install/linux/index.fr.html#download

Mengunduh file instalasi dengan ekstensi .img mungkin memakan waktu tergantung pada kecepatan unduh Internet Anda, jadi rencanakan terlebih dahulu. Dengan koneksi modern dan efisien, ini akan memakan waktu kurang dari 5 menit.

Simpan file dalam folder yang diketahui, seperti Downloads, karena ini akan diperlukan untuk langkah selanjutnya.

## Langkah 2: Verifikasi unduhan Anda

![image](assets/2.webp)
🔗 Bagian Resmi Tails: https://tails.boum.org/install/linux/index.fr.html#verify
Memverifikasi unduhan memastikan bahwa itu dikeluarkan oleh pengembang Tails dan tidak telah rusak atau dicegat selama unduhan.

Memungkinkan untuk memverifikasi secara manual bahwa file yang baru saja Anda unduh adalah yang diharapkan menggunakan PGP, tetapi tanpa pengetahuan lanjutan, verifikasi ini menawarkan tingkat keamanan yang sama dengan verifikasi JavaScript di halaman unduhan, sambil menjadi jauh lebih rumit dan rentan terhadap kesalahan.

Untuk memverifikasi file, gunakan tombol "Pilih unduhan Anda..." yang disediakan di bagian resmi!

## Langkah 3: Pasang Tails pada kunci USB Anda

![image](assets/3.webp)

> 🔗 Bagian Resmi Tails:
>
> - Linux: https://tails.boum.org/install/linux/index.fr.html#install
> - macOS: https://tails.boum.org/install/mac/index.fr.html#etcher dan https://tails.boum.org/install/mac/index.fr.html#install

Langkah ini untuk memasang Tails pada kunci USB Anda adalah yang paling sulit dalam seluruh panduan, terutama jika Anda belum pernah melakukannya sebelumnya. Poin terpenting adalah memilih prosedur yang benar di bagian resmi untuk sistem operasi Anda: Linux atau macOS.

Setelah alat-alat dipasang dan dipersiapkan seperti yang direkomendasikan, file dengan ekstensi .img dapat disalin ke kunci Anda (menghapus semua data yang ada) untuk membuatnya "dapat di-boot" secara independen.

Semoga berhasil! dan sampai jumpa di langkah 4.

## Langkah 4: Mulai ulang pada kunci USB Tails Anda

![image](assets/4.webp)

> 🔗 Bagian Resmi Tails: https://tails.boum.org/install/linux/index.en.html#restart
> Saatnya untuk memulai salah satu komputer Anda menggunakan stik USB baru Anda. Masukkan ke salah satu port USB-nya dan mulai ulang!

> 💡 Kebanyakan komputer tidak secara otomatis boot dari stik USB Tails, tetapi Anda dapat menekan tombol menu boot untuk menampilkan daftar perangkat yang mungkin untuk boot dari.

Untuk menentukan tombol apa yang harus Anda tekan untuk memastikan bahwa Anda memiliki menu boot yang memungkinkan Anda memilih stik USB daripada hard drive biasa Anda, berikut adalah daftar tidak lengkap berdasarkan produsen:

| Produsen     | Tombol          |
| ------------ | ---------------- |
| Acer         | F12, F9, F2, Esc |
| Apple        | Option           |
| Asus         | Esc              |
| Clevo        | F7               |
| Dell         | F12              |
| Fujitsu      | F12, Esc         |
| HP           | F9               |
| Huawei       | F12              |
| Intel        | F10              |
| Lenovo       | F12              |
| MSI          | F11              |
| Samsung      | Esc, F12, F2     |
| Sony         | F11, Esc, F10    |
| Toshiba      | F12              |
| lainnya...   | F12, Esc         |

Setelah stik USB dipilih, Anda seharusnya melihat layar boot baru ini, yang merupakan tanda yang sangat baik, jadi biarkan komputer terus boot...

![image](assets/5.webp)

## Langkah 5: Selamat Datang di Tails!

![image](assets/6.webp)

> 🔗 Bagian Resmi Tails: https://tails.boum.org/install/linux/index.en.html#tails

Satu atau dua menit setelah boot loader dan layar pemuatan, Layar Sambutan muncul.

![image](assets/7.webp)

Di Layar Sambutan, pilih bahasa Anda dan tata letak keyboard di bagian Bahasa & Wilayah. Klik pada Mulai Tails.

![image](assets/8.webp)
Jika komputer Anda tidak terhubung ke jaringan Anda secara kabel, silakan merujuk ke instruksi resmi Tails untuk membantu Anda terhubung ke jaringan Anda tanpa Wi-Fi (bagian "Test your Wi-Fi").
Setelah terhubung ke jaringan lokal, muncul wizard Koneksi Tor untuk membantu Anda terhubung ke jaringan Tor.

![image](assets/9.webp)

Anda dapat mulai menjelajah secara anonim, jelajahi opsi dan perangkat lunak yang termasuk dalam Tails. Nikmati diri Anda, Anda memiliki banyak ruang untuk kesalahan, karena tidak ada yang dimodifikasi di stick USB... Restart berikutnya Anda akan melupakan semua pengalaman Anda!

## Dalam panduan masa depan...

Setelah Anda bereksperimen sedikit lebih banyak dengan stick USB Tails Anda sendiri, kami akan menjelajahi topik lanjutan lainnya dalam artikel lain, seperti:

> Memperbarui kunci dengan versi terbaru dari Tails; Mengonfigurasi dan menggunakan penyimpanan persisten; Memasang perangkat lunak tambahan.
> Sampai saat itu, seperti biasa, jika Anda memiliki pertanyaan, jangan ragu untuk membagikannya dengan komunitas Agora256. Kita belajar bersama untuk menjadi lebih baik esok hari daripada hari ini!