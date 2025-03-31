---
name: Linux Mint

description: Menyiapkan komputer untuk transaksi bitcoin
---

![image](assets/cover.webp)

## Apa yang salah jika Anda menggunakan komputer biasa?

Saat melakukan transaksi Bitcoin, idealnya komputer Anda tidak terinfeksi malware. Tentu saja.

Jika Anda menyimpan frasa seed Bitcoin Anda (biasanya 12 atau 24 kata) di luar komputer dengan perangkat penandatanganan (misalnya dompet perangkat keras - tujuan utamanya), maka Anda mungkin berpikir tidak terlalu penting untuk memiliki komputer yang "bersih" - ini tidak benar.

Komputer yang terinfeksi malware dapat membaca alamat Bitcoin Anda, memaparkan saldo Anda kepada penyerang - mereka tidak dapat mengambil bitcoin hanya dengan mengetahui alamatnya, tetapi mereka dapat melihat berapa banyak yang Anda miliki, dan menghitung dari situ apakah Anda target yang layak. Mereka juga mungkin dapat mengetahui di mana Anda tinggal, misalnya, dan mengambil kuku atau anak-anak Anda untuk membuat Anda membayar tebusan.

## Apa solusinya?

Saya mendorong kebanyakan pengguna Bitcoin untuk menggunakan komputer khusus bebas malware (dengan akses internet) untuk melakukan transaksi Bitcoin. Saya menyarankan orang menggunakan sistem operasi open-source seperti Linux Mint, tetapi gunakan Windows atau Mac jika Anda harus - itu lebih baik daripada menggunakan komputer biasa yang sering digunakan yang pasti memiliki malware tersembunyi di dalamnya.

Salah satu hambatan yang dihadapi orang adalah menginstal sistem operasi baru pada komputer tersebut. Panduan ini untuk membantu dengan itu.

Ada banyak varietas Linux dan saya telah mencoba beberapa. Rekomendasi saya untuk pengguna Bitcoin adalah Linux Mint, karena mudah diinstal, sangat cepat (terutama saat bootup dan shutdown), tidak berat (setiap perangkat lunak tambahan adalah risiko), dan jarang crash pada saya atau berperilaku aneh (dibandingkan dengan versi lain seperti Ubuntu dan Debian).

Beberapa mungkin sangat resisten terhadap sistem operasi baru, lebih memilih Windows atau Mac OS. Saya mengerti, tetapi sistem operasi Windows dan Apple bersifat closed source, jadi kita harus mempercayai apa yang mereka lakukan; Saya tidak berpikir itu kebijakan yang baik, tetapi tidak semua-atau-tidak sama sekali. Saya lebih suka orang menggunakan komputer Windows atau Mac OS yang baru diinstal daripada komputer yang sering digunakan (dengan siapa tahu malware apa yang telah terakumulasi di dalamnya). Satu langkah lebih baik adalah menggunakan komputer Linux yang baru diinstal, yang akan saya demonstrasikan.

Jika Anda gugup menggunakan Linux karena ketidakdiketahuiannya, itu alami, tetapi begitu juga menghabiskan waktu untuk belajar. Banyak informasi tersedia secara online. Berikut adalah video pendek yang sangat saya rekomendasikan yang memperkenalkan dasar-dasar baris perintah.
Pilih komputer

Saya akan mulai dengan apa yang saya pikir adalah opsi terbaik. Kemudian saya akan memberikan pendapat saya tentang alternatifnya.

Opsi ideal:

Rekomendasi saya, jika Anda mampu membelinya, dan jika ukuran tumpukan bitcoin Anda membenarkannya, adalah mendapatkan laptop entry-level baru. Model paling dasar yang dibangun saat ini cukup baik untuk menangani apa yang akan digunakan. Spesifikasi prosesor dan RAM tidak relevan, karena semuanya akan cukup baik.

Hindari:

- Kombinasi tablet apa pun, termasuk Surface Pro
- Chromebook – sering kali kapasitas penyimpanannya terlalu rendah
- Komputer apa pun dengan drive eMMC; Jika memiliki drive SSD, itu sempurna
- Mac – mereka mahal, dan perangkat kerasnya tidak cocok dengan sistem operasi Linux menurut pengalaman saya
- Apa pun yang direnovasi atau bekas (meskipun bukan penghentian kesepakatan mutlak)

Sebagai gantinya, carilah laptop Windows 11 (Saat ini Windows 11 adalah rilis terbaru. Kita akan menghilangkan perangkat lunak itu, jangan khawatir.). Saya mencari di amazon.com untuk "Laptop Windows 11" dan menemukan contoh yang baik ini:
Harga dari yang di atas ini bagus. Spesifikasinya cukup memadai. Ini memiliki kamera terintegrasi yang bisa kita gunakan untuk transaksi PSBT kode QR (jika tidak, Anda harus membeli kamera USB untuk melakukan itu). Jangan khawatir tentang fakta bahwa ini bukan merek yang terkenal (harganya murah). Jika Anda ingin merek yang lebih baik, itu akan menelan biaya, misalnya:

Beberapa yang lebih murah hanya memiliki ruang penyimpanan 64Gb; Saya belum menguji laptop dengan penyimpanan sekecil itu - mungkin OK untuk memiliki 64Gb, tapi mungkin sedikit berisiko.

## Opsi Lain – Tails

Tails adalah sistem operasi yang boot dari USB thumb drive, dan sementara mengambil alih perangkat keras dari komputer apapun. Ini hanya menggunakan koneksi Tor, jadi Anda harus nyaman menggunakan Tor. Tidak ada data yang Anda tulis ke memori selama sesi Anda disimpan ke drive (dimulai segar setiap kali) kecuali Anda mengubah pengaturan dan membuat opsi penyimpanan permanen (di USB thumb drive) – yang Anda kunci dengan kata sandi.

Ini bukan pilihan yang buruk dan gratis, tapi sedikit kaku untuk tujuan kita. Memasang perangkat lunak baru di dalamnya bukanlah hal yang mudah. Satu fitur bagus adalah bahwa itu datang dengan Electrum, tapi kekurangannya adalah bahwa Anda tidak menginstalnya sendiri. Pastikan USB drive yang Anda gunakan setidaknya 8Gb.

Fleksibilitas Anda berkurang jika Anda menggunakan Tails. Anda mungkin tidak akan bisa mengikuti berbagai panduan untuk mengatur apa yang Anda butuhkan dan membuatnya bekerja dengan benar. Misalnya, jika Anda mengikuti panduan saya untuk menginstal Bitcoin Core, ada modifikasi yang diperlukan untuk membuatnya bekerja. Saya tidak berpikir saya akan membuat panduan khusus Tails, jadi Anda perlu membangun keterampilan Anda dan melakukannya sendiri.

Saya juga tidak yakin seberapa baik dompet perangkat keras akan berinteraksi dengan OS ini.

Setelah mengatakan semua ini, komputer Tails untuk transaksi Bitcoin adalah opsi tambahan yang bagus, dan pasti akan membantu keterampilan privasi keseluruhan Anda untuk belajar menggunakan Tails.

## Opsi Lain – Boot OS Langsung

Ini sangat mirip dengan Tails, kecuali sistem operasinya tidak didedikasikan untuk privasi. Cara dasar untuk menggunakan ini adalah dengan mem-flash USB drive dengan sistem operasi Linux pilihan Anda dan membuat komputer boot dari itu alih-alih drive internal. Cara melakukan ini dijelaskan nanti.

Keuntungannya adalah Anda kurang dibatasi dan segala sesuatu akan bekerja tanpa tweak lanjutan.

Saya tidak yakin seberapa baik sistem seperti itu mengisolasi malware di komputer yang ada dari USB boot drive yang Anda gunakan yang menyimpan sistem operasi baru. Mungkin melakukan pekerjaan dengan baik dan mungkin tidak sebaik Tails. Karena saya tidak tahu, preferensi saya adalah laptop khusus.
Opsi Lain – Laptop atau komputer desktop bekas Anda

Menggunakan komputer bekas bukanlah ide yang ideal, terutama karena saya tidak mengetahui kerja dari malware yang canggih, atau jika menghapus drive cukup untuk menyingkirkan itu. Mungkin iya tapi saya tidak ingin meremehkan seberapa cerdik hacker jahat bisa. Anda bisa memutuskan, saya tidak ingin berkomitmen.

Jika Anda memilih untuk menggunakan desktop lama alih-alih laptop lama, ini akan baik-baik saja, kecuali itu akan secara permanen mengambil ruang untuk transaksi bitcoin Anda yang mungkin jarang; Anda seharusnya tidak menggunakannya untuk hal lain. Sedangkan dengan laptop, Anda bisa saja menyimpannya, dan bahkan menyembunyikannya untuk keamanan ekstra.

## Menginstal Linux Mint di komputer apa pun
Berikut adalah instruksi untuk menghapus sistem operasi apa pun dari laptop baru Anda dan menginstal Linux Mint, tetapi Anda dapat menyesuaikannya untuk menginstal hampir semua versi Linux di hampir semua komputer.
Kita akan menggunakan komputer apa pun untuk mem-flash sistem operasi ke sebuah perangkat memori jenis apa pun. Tidak masalah perangkat memori apa, selama itu kompatibel dengan port USB, dan saya sarankan minimal 16Gb.

Dapatkan salah satu dari benda ini:

![image](assets/3.webp)

Atau Anda bisa menggunakan sesuatu seperti ini:

![image](assets/4.webp)

Selanjutnya, navigasikan ke linuxmint.com

![image](assets/5.webp)

Arahkan mouse ke menu Download di bagian atas, lalu klik tautan, “Linux Mint 20.3” atau versi terbaru yang direkomendasikan pada saat Anda melakukan ini.

![image](assets/6.webp)

Akan ada beberapa “rasa” yang bisa dipilih. Ikuti “Cinnamon” untuk mengikuti panduan ini. Klik tombol Download.

![image](assets/7.webp)

Di halaman berikutnya, Anda dapat menggulir ke bawah untuk melihat mirror (Mirror adalah berbagai server yang menyimpan salinan file yang kita inginkan). Anda dapat memverifikasi unduhan menggunakan SHA256 dan gpg (disarankan), tetapi saya akan melewatkan menjelaskan itu di sini karena saya sudah menulis panduan tentang ini.

![image](assets/8.webp)

Pilih mirror yang paling dekat dengan Anda dan klik tautannya (teks hijau di kolom mirror). File akan mulai diunduh – versi yang saya unduh adalah 2.1 gigabyte.

Setelah diunduh, Anda dapat mem-flash file ke perangkat memori portabel dan membuatnya bootable. Cara termudah adalah menggunakan Balena Etcher. Unduh dan instal jika Anda belum memilikinya.

Kemudian jalankan:

![image](assets/9.webp)

Klik flash from file, dan pilih file LinuxMint yang Anda unduh.

Kemudian klik Select target. Pastikan perangkat memori terpasang dan pastikan Anda memilih drive yang benar, jika tidak Anda mungkin menghancurkan isi drive yang salah!

Setelah itu, pilih Flash! Anda mungkin perlu memasukkan kata sandi Anda. Ketika selesai, drive kemungkinan tidak akan bisa dibaca oleh komputer Windows atau Mac Anda karena telah diubah menjadi perangkat Linux. Cukup cabut.
Menyiapkan komputer tujuan

Nyalakan laptop baru, dan saat sedang menyala, tahan tombol BIOS. Ini biasanya F2, tetapi bisa juga F1, F8, F10, F11, F12 atau Delete. Coba satu per satu sampai Anda mendapatkannya, atau cari di internet untuk model komputer Anda dan ajukan pertanyaan yang tepat.

Misalnya “BIOS key Dell laptops”.

Setiap komputer akan memiliki menu BIOS yang berbeda. Jelajahi dan temukan menu mana yang memungkinkan Anda untuk mengonfigurasi urutan boot. Untuk tujuan kita, kita ingin komputer mencoba boot dari perangkat yang terhubung ke USB (jika ada yang terhubung), sebelum mencoba boot dari hard drive internal (jika tidak Windows akan dimuat). Setelah Anda mengatur itu, Anda mungkin perlu menyimpan sebelum keluar atau mungkin disimpan secara otomatis.

Reboot komputer dan seharusnya akan dimuat dari perangkat memori USB. Kita sekarang dapat menginstal Linux di drive internal dan Windows akan dihapus untuk selamanya.

Ketika Anda sampai ke layar berikut, pilih “OEM install (untuk produsen)”. Jika Anda malah memilih “Start Linux Mint”, Anda akan mendapatkan sesi Linux Mint yang dimuat dari perangkat memori, tetapi setelah Anda mematikan komputer, tidak ada informasi Anda yang disimpan – ini pada dasarnya sesi sementara sehingga Anda dapat mencobanya.
Anda akan dibawa melalui wizard grafis yang akan mengajukan sejumlah pertanyaan yang seharusnya mudah dijawab. Salah satunya adalah pengaturan Bahasa, yang lain adalah koneksi jaringan internet rumah Anda dan kata sandi. Jika diminta untuk menginstal perangkat lunak tambahan, tolak. Ketika Anda sampai pada pertanyaan tentang jenis instalasi, beberapa orang mungkin ragu-ragu - Anda perlu memilih "Hapus disk dan instal Linux Mint". Juga, jangan mengenkripsi drive dan jangan pilih LVM.

Anda akhirnya akan sampai ke desktop. Pada titik ini, Anda belum selesai. Anda sebenarnya bertindak sebagai produsen (yaitu, seseorang yang membangun komputer dan menyiapkan Linux untuk pelanggan). Anda perlu mengklik dua kali ikon desktop, "Instal Linux Mint", untuk menyelesaikannya.

Ingat untuk mengeluarkan memory stick, dan kemudian reboot. Setelah reboot, Anda akan menggunakan sistem operasi untuk pertama kalinya sebagai pengguna baru. Selamat.

Salah satu hal pertama yang harus dilakukan (dan dilakukan secara teratur), adalah menjaga sistem agar tetap terbaru.

Buka aplikasi Terminal, dan ketikkan berikut ini:

```bash
sudo apt-get update
```

tekan <enter>, konfirmasi pilihan Anda, dan kemudian perintah ini:

```bash
sudo apt-get upgrade
```

tekan <enter> dan konfirmasi pilihan Anda.

Biarkan ia melakukan tugasnya, ini bisa memakan waktu beberapa menit.

Selanjutnya, saya suka menginstal Tor (sensitif huruf besar-kecil):

```bash
sudo apt-get install tor
```

> _TAMBAHAN: Anda juga dapat menjalankan boot Linux Mint dari “OEM install” (Pastikan Anda terhubung ke internet, jika tidak Anda bisa mendapatkan kesalahan). Jika Anda melakukan ini, nanti Anda perlu mengklik ikon “kirim ke pengguna akhir” yang seharusnya ada di desktop. Kemudian Anda reboot dan memulai sistem operasi seolah-olah Anda membuka komputer untuk pertama kalinya._

Panduan ini menjelaskan mengapa Anda mungkin memerlukan komputer khusus untuk transaksi Bitcoin, dan bagaimana menginstal sistem operasi Linux Mint yang baru di dalamnya.