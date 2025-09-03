---
name: Tails

description: Menginstal Tails pada flash drive USB
---

![image](assets/cover.webp)

Sistem operasi portabel dan amnesik yang melindungi Anda dari pengawasan dan sensor.

## Mengapa kita harus memiliki Flash Drive dengan Tails terinstal?

Tails (https://tails.boum.org/) adalah cara termudah untuk selalu memiliki komputer aman yang siap digunakan kapan saja, yang tidak akan meninggalkan jejak apa pun di komputer yang Anda gunakan.

Untuk menggunakan Tails, matikan komputer yang Anda akses (di rumah orang tua, di rumah teman, di kafe internet...) lalu nyalakan dengan flash drive USB Tails Anda, bukan dengan Windows, macOS, atau Linux.

Setelah itu, Anda akan memiliki lingkungan kerja dan komunikasi yang mandiri dari sistem operasi biasa, dan tidak membutuhkan hard drive.

Tails tidak pernah menulis ke hard drive dan hanya memakai RAM komputer untuk berfungsi. Memori ini sepenuhnya terhapus saat Tails dimatikan, sehingga menghilangkan semua jejak yang mungkin ada.

## Beberapa kasus penggunaan konkret

Untuk memberi Anda gambaran nyata tentang manfaat memiliki flash drive USB berisi Tails, berikut adalah daftar singkat dan tidak lengkap yang disusun oleh tim Agora256:

- Terhubung ke Internet dan Tor secara tanpa sensor dan anonim untuk menjelajahi situs web tanpa meninggalkan jejak;
- Membuka PDF dari situs web yang mencurigakan;
- Menguji cadangan kunci pribadi Bitcoin Anda dengan dompet Electrum;
- Menggunakan paket office (LibreOffice) dan bekerja di komputer yang bukan milik Anda;
- Mengambil langkah pertama Anda dalam lingkungan Linux untuk belajar cara meninggalkan dunia Microsoft dan Apple.

## Bagaimana cara mempercayai Tails?

Selalu ada elemen kepercayaan dalam menggunakan perangkat lunak, tetapi itu tidak harus buta. Aplikasi seperti Tails harus berupaya untuk memberikan penggunanya sarana untuk dapat dipercaya. Untuk Tails, ini berarti:

- Kode sumber publik: https://gitlab.tails.boum.org/;
- Proyek berbasis pada proyek terkemuka: Tor dan Debian;
- Unduhan yang dapat diverifikasi dan direproduksi;
- Rekomendasi oleh berbagai individu dan organisasi.

## Panduan Instalasi dan Penggunaan

Tujuan dari panduan instalasi ini adalah untuk memandu Anda melalui setiap langkah instalasi. Kami tidak akan menjelaskan tindakan lebih dari panduan resmi, namun kami akan mengarahkan Anda ke arah yang benar sambil memberikan tips dan trik.

Untuk alasan pengalaman praktis, tips ini akan difokuskan pada platform macOS dan Linux. 
🛠️ Sebelum memulai prosedur ini, pastikan Anda memiliki Flash Drive dengan kecepatan baca minimal 150 MB/s dan kapasitas minimal 8 GB, idealnya USB 3.0.

Prasyarat:

- 1 Flash Drive, hanya untuk Tails, dengan kapasitas minimal 8 GB
- Komputer yang terhubung ke Internet dengan Linux, macOS, (atau Windows)
- Waktu luang sekitar satu jam, tergantung pada kecepatan koneksi internet Anda, termasuk 30 menit untuk instalasi (file berukuran 1,3 GB untuk diunduh)

## Langkah 1: Unduh Tails dari komputer Anda

![image](assets/1.webp)
🔗 Instruksi dari Tails resmi: https://tails.boum.org/install/linux/index.fr.html#download

Mengunduh file instalasi dengan ekstensi .img mungkin memerlukan waktu, tergantung pada kecepatan internet Anda, jadi rencanakanlah dengan baik. Dengan koneksi modern dan efisien, proses ini akan memakan waktu kurang dari 5 menit.

Simpan file dalam folder yang mudah dicari, seperti Downloads, karena ini akan diperlukan untuk langkah selanjutnya.

## Langkah 2: Verifikasi unduhan Anda

![image](assets/2.webp)
🔗 Instruksi dari Tails Resmi: https://tails.boum.org/install/linux/index.fr.html#verify

Memverifikasi unduhan memastikan bahwa file tersebut benar-benar dikeluarkan oleh pengembang Tails dan tidak rusak atau disadap selama proses pengunduhan.

Hal yang memungkinkan Anda untuk memverifikasi file yang baru saja Anda unduh secara manual menggunakan PGP. Namun, tanpa pengetahuan tingkat lanjut, verifikasi ini menawarkan tingkat keamanan yang sama dengan verifikasi JavaScript di halaman unduhan, tetapi jauh lebih rumit dan rentan terhadap kesalahan.

Untuk memverifikasi file, gunakan tombol "Select your download / Pilih unduhan Anda..." yang disediakan di bagian resmi!

## Langkah 3: Pasang Tails pada flash drive USB Anda

![image](assets/3.webp)
🔗 Instruksi dari Resmi Tails:
- Linux: https://tails.boum.org/install/linux/index.fr.html#install
- macOS: https://tails.boum.org/install/mac/index.fr.html#etcher dan https://tails.boum.org/install/mac/index.fr.html#install

Langkah instalasi Tails pada flash drive USB Anda adalah bagian tersulit dalam seluruh panduan ini, terutama jika Anda belum pernah melakukannya sebelumnya. Poin terpenting adalah memilih prosedur yang tepat di bagian resmi sesuai dengan sistem operasi Anda: Linux atau macOS.

Setelah alat-alat terinstal dan siap sesuai rekomendasi, file dengan ekstensi .img dapat disalin ke flash drive Anda (ini akan menghapus semua data yang ada) untuk menjadikannya "bootable" secara mandiri.

Semoga berhasil! dan sampai jumpa di langkah 4.

## Langkah 4: Mulai ulang pada flash drive USB Tails Anda

![image](assets/4.webp)
🔗 Instruksi dari Tails  Resmi: https://tails.boum.org/install/linux/index.en.html#restart

Sekarang saatnya menyalakan salah satu komputer Anda menggunakan flash drive USB baru Anda. Masukkan ke salah satu port USB-nya, lalu mulai ulang komputer Anda!

**Catatan💡** Kebanyakan komputer tidak otomatis melakukan boot dari flash drive USB Tails. Anda mungkin perlu menekan tombol menu boot untuk menampilkan daftar perangkat yang bisa digunakan untuk boot.

Untuk mengetahui tombol apa yang harus Anda tekan agar menu boot muncul dan Anda bisa memilih flash drive USB daripada hard drive biasa Anda, berikut adalah daftar singkat berdasarkan produsen:

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

Setelah flash drive USB terpilih, Anda akan melihat layar boot baru ini. Ini adalah pertanda yang sangat baik, jadi biarkan komputer terus melakukan boot...
![image](assets/5.webp)

## Langkah 5: Selamat Datang di Tails!

![image](assets/6.webp)
🔗 Instruksi dari Tails  Resmi: https://tails.boum.org/install/linux/index.en.html#tails

Satu atau dua menit setelah proses boot loader dan layar pemuatan, Layar "Selamat datang" akan muncul.
![image](assets/7.webp)

Di Layar "Selamat datang", pilih bahasa Anda dan tata letak keyboard di bagian Bahasa & Wilayah. Klik pada Mulai Tails.
![image](assets/8.webp)

Jika komputer Anda tidak terhubung ke jaringan melalui kabel, silakan lihat instruksi resmi Tails untuk membantu Anda terhubung ke jaringan dengan Wi-Fi (lihat bagian "Test your Wi-Fi").

Setelah terhubung ke jaringan lokal, muncul wizard Koneksi Tor untuk membantu Anda terhubung ke jaringan Tor.
![image](assets/9.webp)

Anda bisa mulai menjelajah secara anonim, menjelajahi opsi dan perangkat lunak yang disertakan dalam Tails. Nikmati saja, Anda punya banyak ruang untuk membuat kesalahan, karena tidak ada yang diubah di flash drive USB... Restart Anda berikutnya akan melupakan semua pengalaman Anda!

## Dalam panduan masa depan...

Setelah Anda bereksperimen lebih jauh dengan flash drive USB Tails Anda sendiri, kita akan membahas topik yang lebih lanjut dalam artikel lain, seperti:
> Memperbarui flash drive USB dengan **versi terbaru dari Tails**;
> Mengonfigurasi dan menggunakan **penyimpanan persisten**(HDD atau SSD);
> Memasang **perangkat lunak tambahan**.

Sampai saat itu, seperti biasa, jika Anda memiliki pertanyaan, jangan ragu untuk membagikannya dengan komunitas Agora256. Kita belajar bersama untuk menjadi lebih baik di masa depan!
