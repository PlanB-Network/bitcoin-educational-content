---
name: Electrum
description: Panduan lengkap Electrum, dari pemula hingga mahir
---

![cover](assets/cover.webp)

Di bawah ini terdapat beberapa sumber deskripsi untuk Electrum:

- [X](https://twitter.com/ElectrumWallet)
- [Electrum website](https://electrum.org/)
- [Electrum documentation](https://electrum.readthedocs.io/)

> "Saya harus mengatakan, ketika saya menemukan panduan ini saya terkejut. Selamat untuk Arman the Parman atas ini. Akan sangat disayangkan jika tidak dihosting di sini dan diterjemahkan ke sebanyak mungkin bahasa. Sungguh, beri tip pada orang itu." Rogzy

Postingan asli:

![Electrum Desktop Wallet (Mac / Linux) - unduh, verifikasi, sambungkan ke node Anda.](https://youtu.be/wHmQNcRWdHM)

![Melakukan transaksi Bitcoin dengan Electrum](https://youtu.be/-d_Zd7VcAfQ)

## Mengapa Electrum?

Ini panduan lengkap cara pakai Electrum Bitcoin Wallet, termasuk solusi buat semua jebakan dan keanehan yang mungkin kamu temui—semua ini aku susun berdasarkan pengalaman pribadi selama beberapa tahun pakai Electrum dan ngajarin orang lain soal keamanan dan privasi di dunia Bitcoin.

Electrum bukan dompet Bitcoin yang cocok buat orang yang pengen segalanya serba gampang atau cuma mau main di level pemula. Sebaliknya, dompet ini emang didesain buat orang yang udah paham atau pengen naik level jadi pengguna “power user”.

Buat Bitcoiner baru, Electrum ini bisa jadi pilihan oke asal ada pengguna yang lebih berpengalaman yang bisa bantu ngarahin dan nunjukin jalannya. Tapi kalau kamu mau belajar sendiri pun tetap aman kok—selama kamu sabar, luangin waktu, dan nyobainnya dulu di lingkungan yang aman (testing), cuma pake sedikit sats di awal. Panduan ini dibuat buat membantu proses itu. Tapi lebih dari itu, panduan ini juga cocok banget dijadiin referensi buat siapa pun yang pengen ngerti Electrum lebih dalam.

> Peringatan: Panduan ini cukup panjang dan padat. Nggak perlu maksa buat ngerjain semuanya dalam sehari. Lebih baik simpan aja dulu, lalu pelajari sedikit demi sedikit seiring waktu.

## Mengunduh Electrum

Idealnya, kamu pakai komputer khusus cuma buat urusan Bitcoin—semacam "komputer Bitcoin" pribadi (aku juga punya panduannya di sini: [https://armantheparman.com/mint/], dan bisa kamu temuin juga di bagian privasi). Tapi nggak apa-apa kok kalau di awal kamu mau coba-coba dulu pakai komputer biasa, asal jumlah Bitcoinnya kecil. Soalnya, siapa yang tahu berapa banyak malware yang mungkin udah numpuk di laptop kamu selama bertahun-tahun? Kamu nggak mau kan dompet Bitcoin kamu terekspos sama ancaman-ancaman kayak gitu?

Dapatkan Electrum dari https://electrum.org/.

Klik tab Unduh di bagian atas.

Klik tautan unduhan yang sesuai dengan komputer kamu. Kalau kamu pakai Linux atau Mac, kamu bisa menggunakan versi Python (ditandai dengan lingkaran merah). Untuk pengguna Linux yang memiliki komputer dengan chip Intel atau AMD, kamu juga bisa pilih AppImage (lingkaran hijau), yang fungsinya mirip seperti file eksekusi di Windows. Kalau kamu pakai Raspberry Pi, karena prosesornya ARM, kamu hanya bisa menggunakan versi Python (lingkaran merah), meskipun sistem operasinya juga Linux. Sementara itu, lingkaran biru ditujukan untuk pengguna Windows, dan lingkaran hitam untuk pengguna Mac.

![image](assets/1.webp)

## Memverifikasi Electrum

Tujuan dari proses "verifikasi" saat mengunduh adalah untuk memastikan tidak ada satu bit pun data yang berubah. Ini penting agar kamu nggak tanpa sadar menjalankan versi software yang sudah diretas dan bisa membahayakan. Tapi, kalau kamu cuma mau latihan dan belum menyimpan Bitcoin beneran, kamu bisa lewati proses ini dulu—asal pastikan kamu nggak pakai dompet itu untuk menyimpan dana serius.

Nanti, kalau kamu sudah siap pakai Electrum untuk menyimpan Bitcoin sungguhan, hapus dulu salinan lamamu dan mulai dari awal lagi—kali ini pastikan kamu memverifikasi unduhannya.

Untuk melakukan verifikasi ini, kita pakai alat kriptografi kunci publik dan privat yang disebut gpg. Panduan lengkapnya bisa kamu baca di sini: [https://armantheparman.com/gpg/]. Alat gpg biasanya sudah tersedia di semua sistem operasi Linux. Untuk pengguna Mac dan Windows, kamu bisa cek link tersebut juga untuk cara download dan instalasinya.

Selain mengunduh perangkat lunak Electrum, demi keamanan kamu juga perlu mengunduh TANDA TANGAN digital dari perangkat lunak itu. Tanda tangan ini sebenarnya adalah rangkaian teks—yang isinya angka-angka terenkripsi—yang dibuat oleh si pengembang menggunakan kunci gpg privat miliknya. Dengan bantuan program gpg, kita bisa "mengujinya" atau memverifikasi tanda tangan tersebut dengan mencocokkannya terhadap kunci publik si pengembang (yang berasal dari kunci privat tadi, dan bisa diakses siapa pun). Proses ini akan membandingkan tanda tangan digital dengan file unduhan untuk memastikan bahwa file yang kamu dapat benar-benar asli dan belum dimodifikasi.

Dengan kata lain, dengan tiga input (tanda tangan, kunci publik, dan file data), kita mendapatkan output benar atau salah untuk mengonfirmasi bahwa file tersebut tidak telah diubah.

Untuk mendapatkan tanda tangan, klik pada link yang sesuai dengan file yang kamu unduh (lihat panah berwarna):

![image](assets/2.webp)

Saat kamu mengklik link, file-nya bisa langsung terunduh ke folder unduhan, atau justru terbuka di browser. Kalau terbuka di browser, kamu perlu menyimpannya secara manual—caranya klik kanan lalu pilih “Simpan sebagai”. Perlu dicatat, tergantung sistem operasi atau browser yang kamu pakai, kadang kamu harus klik kanan di area kosong (bukan di teksnya) supaya opsi itu muncul.

Setelah file diunduh, tampilannya akan seperti ini. Kamu akan melihat ada beberapa tanda tangan—itu artinya file tersebut telah ditandatangani oleh beberapa orang yang berbeda. Kamu bisa memilih untuk memverifikasi semuanya, atau cukup salah satunya saja. Di panduan ini, saya akan tunjukkan cara memverifikasi tanda tangan milik pengembang saja.

![image](assets/3.webp)

Selanjutnya, kamu perlu mendapatkan kunci publik milik ThomasV—dia adalah pengembang utama Electrum. Kunci ini bisa kamu dapatkan langsung dari dia, lewat akun Keybase-nya, dari GitHub, melalui orang lain, dari keyserver, atau dari situs resmi Electrum.

Mendapatkan kunci publik dari situs web Electrum sebenarnya adalah cara yang paling tidak aman. Soalnya, kalau kita sedang memverifikasi apakah situs itu aman atau tidak, justru jadi kontradiktif kalau kita mengambil kunci publik dari sana—karena kunci publiknya bisa saja palsu kalau situsnya memang sudah disusupi.

Untuk sekarang, supaya tetap sederhana, saya akan tunjukkan cara mendapatkan kunci publiknya dari situs web Electrum. Tapi ingat, cara ini bukan yang paling aman—jadi tetap waspada. Sebagai perbandingan, kamu juga bisa cek salinan kunci yang sama di GitHub lewat tautan ini: https://github.com/spesmilo/electrum/blob/master/pubkeys/ThomasV.asc.

Scroll sedikit ke bawah halaman sampai kamu menemukan link menuju kunci publik ThomasV, yang ditandai dengan lingkaran merah di bawah ini. Klik link tersebut untuk mengunduh, atau jika tampilannya langsung terbuka sebagai teks di browser, klik kanan dan pilih “Simpan sebagai” untuk menyimpan file-nya.

![image](assets/4.webp)

Sekarang kamu sudah punya tiga file baru, yang kemungkinan semuanya ada di folder unduhan. Sebenarnya tidak masalah di mana file-file itu disimpan, tapi akan jauh lebih praktis kalau kamu memindahkannya ke dalam satu folder yang sama—biar proses selanjutnya jadi lebih mudah dan rapi.

Ketiga file tersebut:

1. Unduhan Electrum
2. File tanda tangan (biasanya memiliki nama file yang sama dengan unduhan Electrum dengan tambahan “.asc”)
3. Kunci publik ThomasV.

Buka terminal di Mac atau Linux, atau command prompt (CMD) di Windows.

Sekarang, navigasikan ke folder Downloads (atau ke mana pun kamu menyimpan ketiga file tadi). Kalau kamu belum familiar dengan istilah “navigasi ke direktori”, kamu bisa pelajari dulu lewat video singkat ini untuk Linux/Mac: https://www.youtube.com/watch?v=AO0jzD1hpXc, dan ini untuk Windows: https://www.youtube.com/watch?v=9zMWXD-xoxc. Jangan lupa, kalau kamu pakai Linux, nama direktori itu peka terhadap huruf besar dan kecil—jadi pastikan penulisannya benar.
Di terminal, ketik ini untuk mengimpor kunci publik ThomasV ke dalam "keyring" komputermu (keyring adalah konsep abstrak - sebenarnya hanya sebuah file di komputermu):
```bash
gpg --import ThomasV.asc
```

Pastikan nama file sesuai dengan yang telah kamu unduh. Perhatikan juga bahwa itu adalah tanda strip ganda bukan strip tunggal. Catat juga ada spasi sebelum dan setelah "--import". Kemudian tekan <enter>.

Kalau prosesnya berjalan lancar, file seharusnya berhasil diimpor. Tapi kalau muncul error, kemungkinan besar kamu tidak berada di direktori tempat file itu sebenarnya disimpan.

Untuk memastikan lokasi kamu saat ini di Mac atau Linux, ketik pwd. Ini akan menunjukkan direktori aktifmu sekarang. Lalu untuk melihat daftar file yang ada di situ, ketik ls.

Kalau semuanya benar, kamu seharusnya bisa melihat file teks bernama ThomasV.asc muncul di daftar, mungkin bersama file lainnya.

Kemudian kita menjalankan perintah untuk memverifikasi tanda tangan.

```bash
gpg --verify Electrum-4.1.5.tar.gz.asc Electrum-4.1.5.tar.gz
```

Perhatikan ada 4 "elemen" di sini, masing-masing dipisahkan oleh spasi. Saya telah menandai teks secara bergantian untuk membantu Anda melihat. Keempat elemen tersebut adalah:

1. program gpg
2. opsi --verify
3. nama file dari tanda tangan
4. nama file dari program

Yang menarik, terkadang Anda bisa meninggalkan elemen ke-4 dan komputer menebak apa yang Anda maksud. Saya tidak yakin, tetapi saya percaya ini hanya berfungsi jika nama file hanya berbeda oleh "asc" di akhir.

Jangan hanya menyalin nama file yang telah kita tunjukkan di sini - pastikan mereka cocok dengan nama file apa yang kamu miliki di sistem kamu.

Tekan <enter> untuk menjalankan perintah. Kalau berhasil, kamu akan melihat tulisan “good signature from ThomasV” sebagai tanda verifikasi sukses. Mungkin akan muncul beberapa pesan error—itu wajar, karena kita belum punya kunci publik dari orang lain yang juga ikut menandatangani file tersebut (sistem tanda tangan gabungan dalam satu file ini bisa saja berubah di versi mendatang). Selain itu, akan ada peringatan di bagian bawah yang bisa kamu abaikan. Peringatan itu cuma bilang kalau kamu belum secara eksplisit menyatakan bahwa kamu “memercayai” kunci publik milik ThomasV—dan itu tidak jadi masalah untuk sekarang.

Sekarang kita memiliki salinan Electrum yang telah diverifikasi dan aman untuk digunakan.

## Menjalankan Electrum

### Menjalankan Electrum jika menggunakan Python

Kalau kamu mengunduh versi Python, inilah cara membuatnya bekerja. Kamu akan melihat di halaman unduhan ini:

![image](assets/5.webp)

Untuk Linux, ide yang baik untuk pertama-tama memperbarui sistem Anda:

```bash
sudo apt-get update
sudo apt-get upgrade
```

Salin teks kuning yang disorot, tempelkan ke terminal, dan tekan <enter>. Kamu akan diminta kata sandimu, mungkin konfirmasi untuk melanjutkan, dan setelahnya, proses menginstal file-file tersebut ("dependencies") dimulai.

Setelah itu, kamu juga perlu mengekstrak file zip yang tadi kamu unduh ke folder pilihanmu. Ini bisa kamu lakukan lewat antarmuka grafis (tinggal klik kanan lalu pilih "Extract"), atau lewat baris perintah menggunakan perintah yang ditandai warna pink—ingat, nama file kamu bisa saja berbeda tergantung versi yang diunduh. Perlu diingat juga, yang kita verifikasi sebelumnya adalah file zip-nya, bukan folder hasil ekstraknya. Jadi pastikan kamu mengekstrak dari file zip yang sudah diverifikasi tadi.

Ada opsi untuk "menginstal" menggunakan program PIP, tetapi ini tidak perlu, dan menambahkan langkah ekstra serta instalasi file. Cukup jalankan program menggunakan terminal untuk melewati semua itu.

Langkah-langkahnya (Linux) adalah:

1. navigasikan ke direktori tempat file-file diekstrak
2. ketik: ./run_electrum

Di Mac, langkah-langkahnya sama tetapi Anda mungkin perlu menginstal Python3 terlebih dahulu, dan gunakan perintah ini untuk menjalankan:

```bash
```bash
python3 ./run_electrum
```

Setelah Electrum berjalan, jendela terminal akan tetap terbuka. Jika Anda menutupnya, program Electrum akan berhenti. Cukup minimalkan saat menggunakan Electrum.

### Menjalankan Electrum dengan Appimage

Langkah ini memang sedikit lebih mudah dibanding instalasi biasa, tapi tetap nggak semudah menjalankan file executable di Windows. Tergantung pada versi Linux yang kamu pakai, kadang file AppImage secara default tidak diizinkan untuk dieksekusi karena sistem belum memberikan izin. Nah, kita perlu mengubah pengaturannya dulu. Kalau AppImage-mu sudah bisa dijalankan, kamu bisa lewati langkah ini. Tapi kalau belum, navigasikan dulu ke folder tempat file AppImage itu berada lewat terminal, lalu jalankan perintah berikut:

```bash
sudo chmod ug+x Electrum-4.1.5-x86_64.AppImage
```

“sudo” memberikan hak superuser; “chmod” adalah perintah untuk mengubah mode, mengubah siapa yang dapat membaca, menulis, atau mengeksekusi; “ug+x” berarti kita sedang memodifikasi pengguna dan grup untuk mengizinkan eksekusi.

Sesuaikan nama file agar cocok dengan versi Anda.

Kemudian, Electrum akan berjalan dengan mengklik dua kali ikon Appimage.

### Menjalankan Electrum dengan Mac

Cukup klik dua kali file yang diunduh (itu adalah “drive”). Sebuah jendela akan terbuka. Seret ikon Electrum di jendela ke desktopmu, atau ke mana pun kamu ingin menyimpan program tersebut. Setelah itu, kamu dapat “mengeluarkan” drive, dan menghapus drive (file yang diunduh).

Untuk menjalankan program, cukup klik dua kali. Anda mungkin mendapatkan beberapa kesalahan spesifik Mac yang perlu dilewati.

### Menjalankan Electrum dengan Windows

Meskipun saya paling tidak suka Windows, ini adalah metode paling sederhana. Cukup klik dua kali file executable untuk menjalankan.

## Mulai dengan dompet dummy

Ketika kamu pertama kali memuat Electrum, sebuah jendela akan terbuka seperti ini:

![image](assets/6.webp)

Kita akan memilih servermu secara manual nanti, tetapi untuk sekarang, biarkan default dan auto-connect.

Selanjutnya, buatlah dompet dummy—ingat, jangan pernah memasukkan dana sungguhan ke dalam dompet ini. Tujuan dari dompet dummy adalah untuk sekadar mencoba-coba dan memastikan semua fitur di aplikasi berjalan lancar sebelum kamu benar-benar memuat dompet aslimu.

Kita sedang berusaha mencegah risiko privasi bocor secara nggak sengaja dari dompet utama. Jadi selama kamu masih dalam tahap latihan, dompet yang kamu buat bisa dianggap sebagai dompet dummy.

Kamu bisa membiarkan nama dompet tetap sebagai “default_wallet”, atau menggantinya sesuai keinginan, lalu klik Next. Nantinya, kalau kamu punya beberapa dompet, kamu bisa memilih dan membukanya di tahap ini dengan mengklik tombol “Choose…” terlebih dahulu.

![image](assets/7.webp)

Pilih “Standard wallet” dan <Next>:

![image](assets/8.webp)

Kemudian, pilih “I already have a seed”. Saya tidak ingin terbiasa membuat seed Electrum, karena menggunakan protokolnya sendiri yang tidak kompatibel dengan dompet lain – inilah mengapa kita tidak mengklik “new seed”.

![image](assets/9.webp)

Pergi ke https://iancoleman.io/bip39/ dan buat seed dummy. Pertama, ubah jumlah kata menjadi 12 (yang merupakan praktik umum), lalu klik “generate” dan salin kata-kata di kotak ke clipboard Anda.

![image](assets/10.webp)

Kemudian tempelkan kata-kata ke dalam Electrum. Berikut adalah contohnya:

![image](assets/11.webp)

Electrum akan mencari kata-kata yang cocok dengan protokolnya sendiri. Kita harus melewati itu. Klik opsi, dan pilih BIP39 Seed:

![image](assets/12.webp)
Setelah itu, seed yang kamu masukkan akan dianggap valid. (Sebelumnya, Electrum menganggap seed-nya tidak valid karena masih menunggu format seed milik Electrum sendiri.) Sebelum kamu lanjut ke langkah berikutnya, perhatikan baik-baik tulisan “Checksum OK”. Ini penting banget—terutama nanti kalau kamu pakai dompet sungguhan—karena tulisan itu menandakan bahwa seed yang kamu masukkan benar dan valid. Kalau kamu melihat peringatan di bagian bawah layar, nggak usah panik—itu cuma keluhan dari pengembang Electrum tentang standar BIP39. Mereka sering menganggap standar lain itu “FUD” dan merasa bahwa sistem mereka (yang memang tidak kompatibel dengan banyak dompet lain) lebih unggul. Tapi untuk saat ini, kamu bisa abaikan saja.

> Sedikit penyimpangan sebentar untuk membahas peringatan penting. Tujuan dari checksum adalah untuk memastikan kamu tidak salah ketik saat memasukkan seed. Jadi begini: kata terakhir dari seed (biasanya kata ke-12) adalah hasil checksum—ia dihitung secara matematis dari 11 kata sebelumnya. Kalau kamu salah ketik satu huruf atau satu kata saja di awal, maka kata terakhir tidak akan cocok secara matematis, dan dompet akan memperingatkan kamu. Tapi hati-hati, ini tidak berarti seed itu tidak bisa digunakan untuk membuat dompet Bitcoin yang berfungsi. Justru itu masalahnya: bayangkan kamu bikin dompet dengan seed yang salah ketik, lalu kamu isi dengan Bitcoin. Suatu hari kamu coba pulihkan dompet itu, tapi kamu lupa bahwa dulu pernah salah ketik—hasilnya kamu malah pulihkan dompet yang berbeda, dan dana kamu bisa hilang selamanya. Sayangnya, Electrum tidak memaksa kamu berhenti kalau seed yang kamu masukkan tidak lolos checksum. Ini sangat berbahaya, jadi kamu sendiri yang harus ekstra hati-hati. Dompet lain biasanya akan langsung menghentikan kamu jika seed salah—dan itu jauh lebih aman. Inilah salah satu alasan kenapa saya bilang Electrum adalah dompet yang bagus, tapi hanya setelah kamu benar-benar paham cara menggunakannya. Pengembang Electrum seharusnya memperbaiki hal ini, tapi sampai saat itu, tanggung jawabnya ada di tangan kamu.

Perlu kamu tahu, kalau kamu ingin menambahkan passphrase tambahan untuk memperkuat keamanan dompet, pilihan itu tersedia di jendela opsi ini—letaknya ada di bagian paling atas. Jadi jangan sampai kelewat kalau kamu memang berniat menggunakannya.

Setelah kamu klik OK, kamu akan dibawa kembali ke layar tempat kamu mengetik frasa seed tadi.

Kalau sebelumnya kamu memilih untuk menambahkan passphrase, jangan bingung—passphrase tidak dimasukkan bersama dengan kata-kata seed. Permintaan untuk mengetik passphrase-nya akan muncul setelah langkah ini.

Kalau kamu tidak memilih untuk menambahkan passphrase, maka layar berikutnya yang akan muncul adalah pengaturan lanjutan—berisi opsi tipe skrip dompet dan jalur derivasi. Kamu bisa pelajari lebih dalam soal itu di sini: https://armantheparman.com/public-and-private-keys/.

Tapi untuk sekarang, cukup biarkan pengaturannya tetap default dan lanjutkan saja ke langkah berikutnya.

![image](assets/13.webp)

> Sebagai tambahan informasi: pilihan pertama di jendela ini memungkinkan kamu memilih jenis alamat Bitcoin—bisa legacy (yang diawali “1”), P2SH (diawali “3”), atau Bech32/Native Segwit (yang mulai dengan “bc1q”). Sampai panduan ini ditulis, Electrum belum mendukung jenis alamat Taproot (yang biasanya dimulai dengan “bc1p”). Pilihan kedua memungkinkan kamu mengatur jalur derivasi, tapi sebaiknya jangan diubah dulu, apalagi kalau kamu belum ngerti fungsinya. Banyak orang bilang penting untuk mencatat jalur ini supaya kalau suatu saat perlu memulihkan dompet, kamu bisa akses lagi dengan benar. Tapi kalau kamu biarkan tetap default, biasanya sudah cukup aman—jadi nggak perlu khawatir, meskipun tetap bagus kalau kamu mencatatnya.

Setelah itu, kamu akan diminta untuk membuat password. Jangan bingung, ini beda dengan passphrase. Password digunakan untuk mengunci file dompet di komputer kamu, sedangkan passphrase adalah bagian dari proses pembentukan kunci pribadi. Karena ini cuma dompet latihan, kamu bisa lewati bagian ini dan lanjut tanpa mengisi password.

![image](assets/14.webp)
Setelah itu, akan muncul pop-up yang memberi tahu kalau ada versi baru dari Electrum—saran saya, pilih saja “tidak” dulu. Setelah itu, dompet akan selesai dibuat dan siap dipakai, tapi ingat, ini cuma dompet latihan yang nantinya akan dihapus.
![image](assets/15.webp)

Ada beberapa hal yang saya sarankan untuk kamu lakukan demi menyiapkan lingkungan software dengan benar—cukup dilakukan sekali saja di awal.

### Ubah unit menjadi BTC

Buka menu di bagian atas, lalu pilih Alat → Preferensi Electrum. Di tab Umum, ubah "unit dasar" menjadi BTC supaya lebih familiar. Setelah itu, aktifkan tab Alamat dan Koin dengan cara masuk ke menu Tampilan, lalu klik “Tampilkan Alamat” dan lanjutkan dengan “Tampilkan Koin”.

### Aktifkan Oneserver

Secara default, Electrum terhubung ke node acak. Ini juga terhubung ke banyak node sekunder lainnya. Saya tidak yakin data apa yang ditukar dengan node sekunder tersebut, tetapi kita tidak ingin itu terjadi, demi privasi. Bahkan jika Anda menentukan node, misalnya node Anda sendiri, node lainnya juga akan terhubung, dan saya tidak yakin informasi apa yang dibagikan. Bagaimanapun, mudah untuk mencegahnya. Sebelum saya menunjukkan cara menentukan node Anda sendiri, kami akan memaksa Electrum untuk hanya terhubung ke satu server pada satu waktu.

> Sebenarnya ada cara untuk melakukan ini lewat baris perintah dengan menambahkan opsi "oneserver", tapi saya tidak menyarankan metode itu. Sebagai gantinya, saya akan tunjukkan cara lain yang menurut saya lebih simpel untuk jangka panjang dan juga lebih aman karena kecil kemungkinan kamu tanpa sengaja tersambung ke node lain.

Alasan kenapa kita pakai dompet palsu dulu adalah karena kalau kita langsung pakai dompet asli yang berisi bitcoin beneran, maka saat pertama kali dibuka, Electrum bisa aja langsung nyambung ke node acak—meskipun kita udah pilih “atur server secara manual” sebelumnya. Entah kenapa, dia tetap bisa terhubung ke node-node lain di latar belakang (ya, ini salah satu hal yang seharusnya dibenahi oleh pengembang Electrum). Kalau dompet kita menyimpan informasi pribadi, ini bisa jadi masalah besar.

Kita juga nggak bisa langsung melakukan langkah-langkah selanjutnya tanpa lebih dulu memuat semacam dompet, karena file konfigurasi yang akan kita edit nantinya baru terbentuk dan bisa diakses setelah ada dompet yang dibuka.

**Tutup Electrum (PENTING, jika kamu tidak melakukan ini, perubahan berikut yang kamu buat akan terhapus).**

### File Konfigurasi LINUX/MAC

Buka terminal di Linux atau Mac (instruksi Windows nanti):

Secara default, kamu akan langsung berada di folder home. Dari situ, lanjutkan dengan masuk ke folder pengaturan Electrum yang tersembunyi—ini bukan folder tempat aplikasinya, tapi tempat di mana semua data konfigurasi Electrum disimpan.

```bash
cd .electrum
```

Perhatikan titik sebelum "electrum" yang menunjukkan ini adalah folder tersembunyi.

Cara lain untuk sampai ke sana adalah mengetik:

```bash
cd ~/.electrum
```

di mana "~" mewakili jalur direktori home Anda. Anda dapat melihat jalur lengkap direktori saat ini dengan perintah "pwd".

Setelah berada di direktori ".electrum", ketik "nano config" dan tekan <enter>.

Sebuah editor teks akan terbuka (disebut nano) dengan file konfigurasi terbuka. Mouse tidak banyak berfungsi di sini. Gunakan tombol panah untuk sampai ke baris yang mengatakan:

```json
"oneserver": false,
```

Ubah "false" menjadi "true"; dan jangan mengganggu sintaksnya (jangan menghapus koma atau titik koma).

Tekan <ctrl> x, untuk keluar, kemudian "y" untuk menyimpan, kemudian <enter> yang mengonfirmasi perubahan tanpa mengedit nama file.
Sekarang jalankan Electrum lagi. Kemudian klik lingkaran di pojok kanan bawah, yang akan membuka pengaturan jaringan. Lalu, dekat bagian atas di tab overview, Anda akan melihat "terhubung ke 1 node" - ini menunjukkan keberhasilan.
Tepat di bawah itu, kamu akan melihat sebuah bidang teks dan alamat server ada di sana. Anda saat ini terhubung ke node acak tersebut. Lebih lanjut tentang menghubungkan ke sebuah node di bagian selanjutnya.

### Berkas Konfigurasi Windows

Berkas konfigurasi Windows sedikit lebih sulit untuk ditemukan. Direktorinya adalah: `C:/Users/Parman/AppData/Roaming/Electrum`

Tentu saja, Anda harus mengganti "Parman" dengan nama pengguna komputer Anda sendiri.

Di folder tersebut Anda akan menemukan berkas konfigurasi. Buka dengan editor teks dan edit baris:

```json
"oneserver": false,
```

Ubah "false" menjadi "true"; jangan mengganggu sintaksnya (jangan menghapus koma atau titik koma).

Kemudian simpan berkas dan keluar.

## Menghubungkan Electrum ke sebuah node

Selanjutnya, kita ingin menghubungkan dompet dummy kita ke node pilihan kita. Jika Anda belum siap untuk menjalankan sebuah node, Anda dapat melakukan salah satu dari berikut ini:

1. Terhubung ke node pribadi teman (memerlukan Tor)
2. Terhubung ke node perusahaan terpercaya
3. Terhubung ke node acak (tidak disarankan).

Ngomong-ngomong, berikut adalah instruksi untuk menjalankan node-mu sendiri, dan ini adalah alasan mengapa kamu harus melakukannya. (semua tutorial di bagian Node atau di kursus gratis kami)

### Terhubung ke node teman melalui Tor (Panduan segera hadir.)

### Terhubung ke node perusahaan terpercaya

Alasan kenapa langkah ini penting adalah karena suatu saat kamu mungkin perlu mengakses blockchain, tapi nggak punya node sendiri yang aktif, atau nggak bisa pinjam node milik teman. Jadi, ini semacam langkah cadangan biar kamu tetap bisa jalan meski dalam kondisi darurat.

Sekarang mari kita hubungkan Electrum ke node Bitaroo. Mereka mengklaim tidak mengumpulkan data apa pun, dan sebagai exchange khusus Bitcoin yang dijalankan oleh Bitcoiner sejati, tingkat kepercayaannya jauh lebih tinggi. Memang masih ada sedikit elemen kepercayaan di sini, tapi itu jauh lebih aman dibanding terhubung ke node acak yang bisa saja dimiliki perusahaan pengawasan.

Dapatkan ke Pengaturan Jaringan dengan mengklik lingkaran di bagian kanan bawah jendela Dompet (merah menunjukkan tidak terhubung, hijau menunjukkan terhubung, dan biru menunjukkan terhubung melalui Tor).

![image](assets/16.webp)

Begitu kamu klik ikon lingkaran di pojok kanan bawah, akan muncul jendela pop-up. Karena sebelumnya kita sudah atur Electrum supaya hanya terhubung ke satu server, maka dompetmu akan menampilkan status “terhubung ke 1 node”.

Hilangkan tanda centang pada kotak "pilih server secara otomatis", lalu di Bidang Server, ketik detail Bitaroo seperti yang ditunjukkan:

![image](assets/17.webp)

Tutup jendela, dan sekarang kita seharusnya terhubung ke node Bitaroo. Untuk mengonfirmasi, lingkaran harus berwarna hijau. Klik lagi dan periksa bahwa detail server tidak berubah kembali ke node acak.

### Terhubung ke node-mu sendiri

Kalau kamu sudah punya node sendiri, itu langkah yang bagus. Tapi kalau yang kamu punya baru sebatas Bitcoin Core saja, tanpa Electrum Server, maka kamu belum bisa menghubungkan dompet Electrum ke node tersebut.

> Catatan penting: Electrum Server dan Electrum Wallet itu dua hal yang berbeda. Server adalah perangkat lunak tambahan yang dibutuhkan supaya dompet Electrum bisa terhubung dan berkomunikasi dengan blockchain Bitcoin. Kenapa harus ada pemisahan seperti ini, saya juga kurang tahu pasti—mungkin tujuannya biar performa lebih cepat, tapi bisa saja alasan sebenarnya berbeda.
Kalau kamu menjalankan node Bitcoin pakai software seperti MyNode (yang saya rekomendasikan untuk pemula), Raspiblitz (cocok saat kamu mulai lebih mahir), atau Umbrel (jujur aja, saya belum bisa rekomendasikan karena saya sering nemu masalah), kamu bisa langsung hubungkan dompet Electrum-mu dengan cukup memasukkan alamat IP dari komputer atau Raspberry Pi yang menjalankan node itu, ditambah titik dua dan angka 50002. Contohnya seperti: 192.168.1.10:50002. Nanti saya juga akan tunjukkan gimana cara cari alamat IP node kamu.

Buka pengaturan Jaringan (klik lingkaran hijau atau merah di pojok kanan bawah). Hilangkan tanda centang pada kotak "pilih server secara otomatis", kemudian masukkan alamat IP Anda seperti yang telah saya lakukan, alamat IP Anda akan berbeda, tetapi titik dua dan "50002" harus sama.

Tutup jendela, dan sekarang kita seharusnya terhubung ke node yang kamu punya. Untuk mengonfirmasi, klik lingkaran lagi dan periksa bahwa detail server tidak berubah kembali ke node acak.

Terkadang, meskipun melakukan segalanya dengan benar, tampaknya itu menolak untuk terhubung. Berikut adalah hal-hal yang dapat dicoba...

- Upgrade ke versi Electrum yang lebih baru, dan perangkat lunak node Anda
- Coba hapus folder cache di direktori ".electrum"
- Coba ubah port dari 50002 menjadi 50001 di pengaturan jaringan
- Gunakan panduan ini untuk terhubung menggunakan Tor sebagai alternatif (https://armantheparman.com/tor/)
- Reinstall Electrum Server di node

## MENEMUKAN ALAMAT IP NODE ANDA

Alamat IP memang bukan sesuatu yang biasa diketahui atau digunakan oleh pengguna pada umumnya. Dari pengalaman saya membantu banyak orang menyiapkan node dan menghubungkannya ke dompet, salah satu kendala paling umum justru ada di langkah sederhana ini—menemukan alamat IP dari node mereka.

Untuk MyNode, kamu bisa mengetik di jendela browser: `mynode.local`

Kadang, alamat seperti “mynode.local” nggak langsung bisa diakses (dan pastikan juga kamu nggak ngetiknya di kolom pencarian Google). Supaya browser mengenali itu sebagai alamat web dan bukan kata kunci pencarian, tambahkan http:// di depannya, jadi jadi http://mynode.local. Kalau itu tetap nggak berhasil, coba versi dengan “s” di depannya: https://mynode.local.

Langkah ini akan mengarahkan kamu ke antarmuka perangkat node-mu. Setelah masuk, cari dan klik bagian pengaturan—di sana biasanya ada tampilan seperti yang saya lingkari biru di gambar sebelumnya. Di layar itu, kamu bisa menemukan alamat IP dari perangkat node-mu.

Halaman ini akan dimuat dan kamu akan melihat alamat IP node (lingkaran "biru")

Kemudian, di masa depan, kamu dapat mengetik 192.168.0.150, atau http://192.168.0.150 ke dalam browsermu.

Untuk Raspiblitz (ketika tidak menghubungkan layar), Anda memerlukan metode berbeda (yang juga berfungsi untuk MyNode):

Login ke halaman web router kamu – di sini kita akan menemukan alamat IP dari semua perangkat yang terhubung. Halaman web router akan berupa alamat IP yang kamu masukkan ke dalam browser web. Tampilannya seperti ini:

    http://192.168.0.1

Kalau kamu butuh login ke router, coba cek dulu manual pengguna atau lihat stiker yang biasanya ditempel di bagian bawah atau belakang router—di situ sering ada info login. Kalau nggak ketemu juga, kamu bisa coba kredensial default yang umum dipakai: nama pengguna “admin” dan kata sandi “password”.

Jika sudah berhasil login, kamu akan melihat perangkat yang terhubung dan dari nama-nama mereka, mungkin jelas mana yang node milikmu. Alamat IP akan ada di sana.
### Jika dua metode pertama gagal, metode terakhir akan berhasil tetapi itu melelahkan:
Pertama, temukan alamat IP dari perangkat apa pun di jaringan Anda (komputer saat ini sudah cukup).

Di Mac, kamu akan menemukannya di preferensi Jaringan:

![image](assets/21.webp)

Kami tertarik pada 4 elemen pertama (192.168.0), bukan elemen ke-4, "166" yang Anda lihat di gambar (milik Anda akan berbeda).

Untuk Linux, gunakan baris perintah:

```bash
ifconfig | grep inet
```

Garis vertikal itu adalah simbol "pipe" dan kamu akan menemukannya di bawah tombol <delete>. Disitu, akan terlihat beberapa output dan sebuah alamat IP. (Abaikan 127.0.0.1 itu bukan itu, dan abaikan netmask)

Untuk Windows, buka prompt perintah (cmd) dan ketik:

```bash
ipconfig/all
```

dan tekan Enter. Alamat IP dapat ditemukan di output.

Itu bagian mudahnya. Sekarang masuk ke bagian yang agak tricky: menemukan alamat IP node-mu. Kita harus mencarinya secara manual, atau istilah kasarnya, "brute-force". Misalnya, kalau alamat IP komputer kamu dimulai dengan 192.168.0.xxx, maka node kamu kemungkinan besar juga pakai awalan yang sama. Jadi, kamu bisa coba buka browser dan ketik alamat seperti https://192.168.0.2, lalu coba naikkan angkanya satu per satu (192.168.0.3, 192.168.0.4, dan seterusnya) sampai kamu menemukan tampilan antarmuka node-mu.

Nomor IP terkecil yang mungkin kamu coba adalah 2, karena `0` biasanya dipakai untuk menunjuk semua perangkat dalam jaringan, dan `1` biasanya sudah dipakai oleh router. Nomor tertingginya adalah `255`, yang secara teknis adalah angka maksimum dari 1 byte (karena 255 = 11111111 dalam biner). Jadi rentang alamat IP yang bisa kamu “brute-force” coba adalah dari `192.168.x.2` sampai `192.168.x.255`, tergantung subnet jaringanmu.

Lakukan pencarian alamat IP satu per satu, naikkan angkanya perlahan sampai maksimal 255. Nanti kamu akan menemukan satu alamat yang ketika dibuka di browser akan menampilkan halaman MyNode atau RaspiBlitz kamu. Nah, begitu halaman itu muncul, berarti kamu sudah menemukan alamat IP node-mu. Alamat inilah yang nanti harus kamu masukkan ke pengaturan jaringan di Electrum agar bisa terhubung langsung ke node milikmu sendiri.

Ini akan terlihat seperti ini (pastikan kamu menyertakan titik dua dan nomor setelahnya):

![image](assets/22.webp)

> Penting untuk kamu pahami bahwa alamat IP ini bersifat internal, hanya berlaku di dalam jaringan rumahmu. Jadi orang dari luar internet nggak bisa mengaksesnya. Anggap saja ini seperti nomor ekstensi di kantor—misalnya kamu tekan 101 untuk menelepon meja bagian keuangan. Sama halnya, alamat IP ini hanya membantu perangkat-perangkat dalam jaringan yang sama saling menemukan dan berkomunikasi. Jadi nggak perlu khawatir, alamat ini nggak sensitif dan nggak membahayakan privasi.

## Hapus dompet palsu

Sekarang setelah Electrum berhasil terhubung ke satu node saja (dan bukan acak node di jaringan), mulai sekarang ia akan selalu dimuat dengan cara ini secara default. Langkah selanjutnya: hapus dompet palsu yang tadi kamu buat. Caranya, buka menu File lalu pilih Delete. Ini penting banget, apalagi kalau kamu tanpa sengaja sempat mengirim dana ke dompet ini—karena dompet tadi dibuat hanya untuk latihan, tanpa prosedur keamanan yang layak, jadi jangan pernah menyimpannya untuk penggunaan sungguhan.

## Buat dompet latihan

Setelah kamu menghapus dompet palsu tadi, sekarang saatnya mulai dari awal lagi dan buat dompet baru—caranya sama seperti sebelumnya. Tapi kali ini, tulislah seed phrase-nya (kata-kata benih) dan simpan dengan benar-benar aman. Ini bukan lagi sesi latihan, jadi jangan cuma copy-paste ke komputer atau foto pakai HP. Gunakan metode yang aman, seperti menulis di kertas tahan air atau logam, dan simpan di tempat yang tidak mudah diakses orang lain. Ingat, siapa pun yang punya akses ke seed ini bisa mengambil seluruh isi dompetmu.

Ini adalah langkah bijak: gunakan dompet latihan tanpa hardware wallet lebih dulu agar kamu bisa belajar memahami cara kerja Electrum tanpa ribet. Kirimkan hanya sedikit bitcoin ke dompet ini—anggap saja ini uang yang siap hilang demi belajar. Setelah kamu terbiasa dan paham cara menggunakannya dengan benar, barulah lanjut ke tahap berikutnya: menghubungkan Electrum ke hardware wallet untuk tingkat keamanan yang jauh lebih tinggi.

Di dompet baru yang dibuat, kamu akan melihat daftar alamat. Yang hijau disebut "alamat penerima". Mereka adalah produk dari 3 hal:

- Seed phrase
- Frasa sandi
- Jalur derivasi

Dompet baru yang kamu buat akan otomatis memiliki daftar alamat penerima Bitcoin—jumlahnya sangat banyak, bahkan mencapai lebih dari 4,3 miliar! Semua alamat itu bisa direkonstruksi ulang kapan saja, selama kamu punya seed phrase, passphrase (jika ada), dan jalur derivasinya. Electrum sendiri hanya menampilkan 20 alamat pertama secara default, dan akan menampilkan lebih banyak jika kamu mulai menggunakannya. Kalau kamu ingin memahami lebih dalam soal bagaimana kunci privat bekerja di balik layar, kamu bisa cek panduan khusus tentang itu.
![image](assets/23.webp)

Ini sangat berbeda dengan beberapa dompet lain yang hanya menampilkan 1 alamat pada satu waktu.

Karena kamu memasukkan seed phrase saat membuat dompet ini, Electrum secara otomatis menghasilkan kunci privat untuk setiap alamat yang dibuat dalam dompet itu. Artinya, kamu punya kendali penuh atas dana yang masuk ke alamat-alamat tersebut, dan kamu bisa dengan bebas mengirimkannya kapan saja—Electrum sudah memiliki semua yang dibutuhkan untuk menandatangani transaksi.

Perhatikan juga bahwa beberapa alamat dalam dompetmu ditandai dengan warna kuning—ini disebut “alamat kembalian”. Alamat-alamat ini berasal dari jalur matematika yang berbeda, tapi masih bagian dari dompetmu dan bisa ada hingga 4,3 miliar juga. Mereka dipakai secara otomatis saat kamu melakukan transaksi. Misalnya, kalau kamu kirim 0,5 BTC ke seseorang dari saldo 1,5 BTC, maka sisa 1,0 BTC akan dikirim balik ke dompetmu—bukan ke alamat awal, tapi ke salah satu alamat kembalian kuning ini. Kalau tidak, sisa uangmu bisa hilang ke penambang! Kalau kamu penasaran soal bagaimana sistem ini bekerja di balik layar (terutama tentang UTXO), kamu bisa baca lebih dalam lewat panduan ini: https://armantheparman.com/utxo/.

Langkah selanjutnya, buka kembali situs Ian Colman yang digunakan untuk mengelola seed phrase, lalu masukkan seed yang sudah kamu punya (jangan buat seed baru). Setelah kamu tempelkan seed-nya, kamu akan lihat informasi di bagian bawah halaman—termasuk kunci privat dan kunci publik—akan otomatis berubah. Semua informasi ini dihitung berdasarkan data yang kamu masukkan di bagian atas halaman, seperti seed phrase, jalur derivasi, dan tipe alamat.

> Ingat baik-baik: jangan pernah memasukkan seed phrase dompet Bitcoin asli kamu ke komputer—terutama kalau komputer itu dipakai sehari-hari dan berisiko terinfeksi malware. Seed itu kunci utama ke seluruh saldo Bitcoin-mu, dan kalau sampai dicuri, nggak ada cara untuk mengembalikannya. Tapi karena kita lagi latihan dan hanya pakai dompet dummy (tanpa dana asli), nggak masalah untuk sekarang. Tetap waspada, karena kebiasaan kecil ini bisa menentukan keamanan keuanganmu di masa depan.

Scroll ke bawah dan ubah jalur derivasi menjadi BIP84 (segwit) untuk mencocokkan dompet Electrum kamu dengan mengklik tab BIP84.

![image](assets/24.webp)

Di bawah itu, kamu akan melihat kunci privat ekstensi akun dan kunci publik ekstensi akun:

![image](assets/25.webp)

Pergi ke Electrum, dan bandingkan bahwa mereka cocok. Ada menu di bagian atas, dompet --> informasi:

![image](assets/26.webp)

Ini muncul:

![image](assets/27.webp)

Perhatikan kedua kunci publik cocok.

Selanjutnya, bandingkan alamat-alamatnya. Kembali ke situs Ian Coleman dan gulir ke bawah:

![image](assets/28.webp)

Perhatikan mereka cocok dengan alamat-alamat di Electrum.

Sekarang kita akan memeriksa alamat-alamat kembalian. Gulir sedikit ke atas ke jalur derivasi dan ubah 0 terakhir menjadi 1:

![image](assets/29.webp)

Sekarang scroll ke bawah dan bandingkan alamat-alamatnya cocok dengan alamat-alamat kuning di Electrum

Mengapa kita melakukan semua ini?

Intinya, kita menggunakan dua program berbeda untuk memproses seed phrase yang sama, lalu kita bandingkan hasilnya—apakah alamat, kunci privat, atau xpub yang dihasilkan cocok semua. Ini penting karena kalau dua software yang terpisah menghasilkan output identik, maka kemungkinan besar datanya benar dan tidak dimanipulasi oleh malware tersembunyi. Cara ini membantu mengurangi risiko “disabotase diam-diam” oleh perangkat lunak palsu.

Langkah selanjutnya adalah menerima tes kecil dan menghabiskannya dalam dompet dari satu alamat ke alamat lain.

## Menguji Wallet (Belajar Cara Menggunakannya)

Di bagian ini, saya akan menunjukkan langkah-langkah untuk menerima sejumlah kecil Bitcoin (UTXO) ke dalam dompet dummy kita, lalu mengirimkannya kembali ke alamat lain dalam dompet yang sama. Karena jumlahnya sangat kecil, kita tidak akan khawatir jika hilang—tujuan utamanya hanya untuk latihan, agar kamu bisa memahami alur transaksi secara nyata tanpa risiko.

Ini memiliki sejumlah tujuan.

- Ini akan membuktikan bahwa Anda memiliki kekuatan untuk menghabiskan koin di dompet baru.
- Ini akan mendemonstrasikan cara menggunakan perangkat lunak Electrum untuk melakukan pengeluaran (dan beberapa fitur), sebelum kita menambahkan kompleksitas ekstra untuk keamanan (menggunakan dompet perangkat keras atau komputer yang tidak terhubung ke internet)
- Ini akan memperkuat ide bahwa Anda memiliki banyak alamat untuk dipilih untuk menerima dan menghabiskan, dalam dompet yang sama.
Buka dompet Electrum uji Anda dan klik tab Alamat, kemudian klik kanan pada alamat pertama dan pilih Salin –> Alamat:
![image](assets/30.webp)

Alamat sekarang berada dalam memori komputermu.

Sekarang buka akun di bursa tempat kamu punya sedikit Bitcoin—dan mari kita tarik sejumlah kecil, misalnya 50.000 sats, ke alamat dompet dummy yang sudah kamu buat tadi. Di sini saya akan pakai Coinbase sebagai contoh, karena memang banyak orang yang pakai. Walaupun begitu, secara pribadi saya kurang suka Coinbase karena mereka dianggap berseberangan dengan prinsip dasar Bitcoin. Tapi demi latihan, kita anggap ini sekadar contoh teknis.

Masuk, dan klik tombol Kirim/Terima, yang per hari ini berada di pojok kanan atas halaman web.

![image](assets/31.webp)

Saya jelas tidak memiliki dana dengan Coinbase, tetapi bayangkan saja ada dana di sini dan ikuti langkah berikut: Tempelkan alamat dari Electrum di bidang “Ke” seperti yang telah saya lakukan. Anda juga perlu memilih jumlah (saya sarankan sekitar 50.000 sats atau sejenisnya). Jangan memasukkan "pesan opsional" – Coinbase sudah mengumpulkan cukup banyak data Anda (dan menjualnya), tidak perlu membantu mereka. Akhirnya, klik “Lanjutkan”. Setelah itu saya tidak tahu pop-up apa lagi yang akan Anda dapatkan, Anda sendiri yang menentukan, tetapi metodenya serupa untuk semua bursa.

![image](assets/32.webp)

Tergantung pada exchange atau bursa, Anda mungkin melihat sats di dompet Anda segera, atau beberapa penundaan jam/hari.

Perlu kamu tahu, Electrum akan langsung menampilkan koin sebagai "diterima" begitu transaksi masuk ke mempool—yaitu daftar transaksi yang menunggu untuk dimasukkan ke dalam blok oleh para penambang. Jadi, meskipun koin belum benar-benar tercatat di blockchain (alias belum terkonfirmasi), kamu tetap bisa melihatnya muncul di dompet. Setelah transaksi benar-benar masuk ke blok, statusnya akan berubah menjadi "terkonfirmasi", artinya dana tersebut sudah resmi aman di jaringan..

Sekarang setelah ada UTXO (koin yang belum terpakai) di dalam dompet, kita bisa mulai memberi label pada koin tersebut. Label ini bersifat pribadi dan hanya terlihat oleh kita di komputer yang sedang kita gunakan—tidak akan muncul di blockchain atau buku besar publik. Electrum menyimpan semua label ini secara lokal. Jika suatu saat kamu pindah ke komputer lain tapi masih menggunakan dompet yang sama, kamu bisa memindahkan file label ini agar semua catatan tetap utuh dan sinkron.

### Membuat label untuk UTXO

Saya sedang mencoba menerima donasi ke dompet uji ini. Terima kasih kepada @Sathoarder yang sudah langsung mengirimkan UTXO sebesar 10.000 sats, dan juga kepada seseorang yang anonim yang ikut menyumbang 5.000 sats ke alamat yang sama. Kalau kamu perhatikan, total saldo di alamat pertama sekarang jadi 15.000 sats, dengan dua transaksi yang tercatat di kolom paling kanan. Tapi lihat juga bagian bawah aplikasi: 10.000 sats sudah terkonfirmasi di blockchain, sedangkan 5.000 sats lainnya masih tertahan di mempool, jadi belum dianggap final.

![image](assets/33.webp)

Sekarang, kalau kita buka tab Koin di Electrum, kita akan melihat dua entri UTXO alias “koin yang diterima”. Keduanya berasal dari alamat yang sama, tapi masing-masing mewakili transaksi yang berbeda—yang satu sudah dikonfirmasi, satunya belum..

![image](assets/34.webp)

Kalau kamu kembali ke tab Alamat, coba klik dua kali di kolom “Label” di samping salah satu alamat. Kamu bisa langsung mengetikkan teks apa pun sebagai label—misalnya untuk mencatat siapa yang mengirim, atau dari mana dana itu berasal—lalu tekan <enter> untuk menyimpannya.

![image](assets/35.webp)

Memberi label pada koin yang masuk ke dompetmu itu penting agar kamu bisa tahu asal-usul setiap koin—apakah koin itu bebas dari KYC (Know Your Customer) atau justru bisa dilacak balik ke identitasmu, serta untuk membantu kamu menghitung pajak kalau suatu saat harus menjualnya. Sebaiknya jangan gabungkan banyak koin ke dalam satu alamat, karena bisa bikin pelacakan dan privasi jadi lebih rumit. Tapi kalau kamu tetap memilih cara itu, kamu bisa kasih label satu per satu berdasarkan transaksinya, bukan cuma alamatnya. Caranya bukan di tab "Coins" (padahal itu yang paling logis), tapi kamu harus buka tab "Riwayat", cari transaksinya, dan kasih label di sana. Nanti label itu bakal muncul juga di tab "Coins". Perlu dicatat juga, label yang dibuat di riwayat akan menggantikan label dari alamatnya. Dan supaya data label ini nggak hilang, kamu bisa simpan dengan cara ekspor lewat menu Wallet → Labels → Export.

Selanjutnya, kita akan mengirim koin dari alamat pertama ke alamat kedua. Klik kanan pada alamat pertama lalu pilih “habiskan dari”. Meskipun di contoh ini langkah ini tidak benar-benar diperlukan, bayangkan saja kalau kita punya banyak koin tersebar di berbagai alamat—fitur ini sangat berguna untuk memastikan kita hanya menggunakan koin tertentu saja. Kalau ingin memilih beberapa alamat sekaligus, kamu bisa klik kiri sambil menahan tombol Command (atau Ctrl di Windows), lalu klik kanan dan pilih “habiskan dari”.

![image](assets/36.webp)

Setelah kamu melakukan langkah tersebut, akan muncul bar berwarna hijau di bagian bawah jendela dompet yang menunjukkan berapa banyak koin yang sudah kamu pilih dan berapa total saldo yang tersedia untuk dibelanjakan.

Kita memang bisa memilih satu koin (UTXO) dari sebuah alamat dan membiarkan koin lainnya tidak digunakan, tapi ini sangat tidak disarankan. Ketika Anda membelanjakan sebagian dari koin di suatu alamat, tanda tangan digital milikmu membocorkan informasi kriptografis yang dapat digunakan untuk melemahkan keamanan alamat tersebut. Itu sebabnya, secara praktik terbaik, sebaiknya habiskan semua koin dari satu alamat sekaligus, lalu kirim kembalian ke alamat baru yang masih belum digunakan. Ini juga alasan mengapa menyimpan banyak koin di satu alamat bukan ide yang bagus—selain menurunkan privasi, ini juga berisiko dan bisa membuat biaya transaksi menjadi lebih mahal jika ingin memindahkan semuanya nanti. Namun, jika kamu tetap ingin tahu caranya, bisa langsung membuka tab “Coins” (Koin), lalu pilih UTXO tertentu dari daftar, klik kanan, dan pilih “Spend”. Tapi ingat, ini hanya untuk tujuan pembelajaran—jangan gunakan cara ini untuk transaksi sungguhan.

![image](assets/37.webp)

Sekarang, kita memiliki dua koin yang dipilih untuk dihabiskan. Selanjutnya, kita memutuskan kemana mengirimkannya. Mari kita kirim ke alamat kedua. Kita perlu menyalin alamat seperti ini:

![image](assets/38.webp)

Kemudian pergi ke tab "Kirim", dan tempel alamat kedua di bidang "bayar ke". Tidak perlu menambahkan deskripsi; Kamu bisa, tetapi dapat melakukannya nanti dengan mengedit label. Untuk jumlahnya, pilih "Max" untuk menghabiskan semua koin yang kita pilih. Kemudian klik "Bayar", dan kemudian klik tombol "lanjutan" pada pop-up yang muncul.

![image](assets/39.webp)

Selalu klik "lanjutan" pada tahap ini agar kita bisa mendapatkan kontrol yang lebih baik dan memeriksa secara tepat apa yang ada dalam transaksi. Berikut adalah transaksinya:

![image](assets/40.webp)

Kita melihat dua kotak/jendela putih internal. Yang atas adalah jendela input (koin mana yang dihabiskan), dan yang bawah adalah output (kemana koin itu pergi).

Perhatikan, status (kiri atas) adalah "belum ditandatangani" untuk saat ini. "Jumlah yang dikirim" adalah 0 karena koin sedang ditransfer dalam dompet. Biayanya adalah 481 sats. Perhatikan bahwa jika itu adalah 480 sats, nol terakhir akan dihilangkan, seperti ini, 0.0000048 dan bagi mata yang lelah, ini bisa terlihat seperti 48 sats – berhati-hatilah (sesuatu yang seharusnya diperbaiki oleh pengembang Electrum).
Ukuran transaksi merujuk pada ukuran data dalam byte, bukan jumlah bitcoin. "Ganti dengan biaya" diaktifkan secara default, dan ini memungkinkanmu untuk mengirim ulang transaksi dengan biaya yang lebih tinggi jika diperlukan. LockTime memungkinkan kita untuk menyesuaikan kapan transaksi tersebut valid - Saya belum mencoba itu, tetapi menyarankan agar tidak menggunakannya kecuali Anda benar-benar memahami apa yang kau lakukan dan telah berlatih dengan jumlah kecil.

Di bagian bawah, kita memiliki beberapa alat penyesuaian biaya penambangan yang canggih. Yang perlu kita lakukan untuk transfer internal adalah mengaturnya ke biaya minimum 1 sat/byte. Cukup ketikkan angka tersebut secara manual di kolom Target fee. Untuk memeriksa biaya yang sesuai untuk pembayaran eksternal, kamu dapat berkonsultasi dengan https://mempool.space untuk melihat seberapa sibuk mempool tersebut, dan beberapa biaya yang disarankan ditampilkan.

![image](assets/41.webp)

Saya telah memilih 1 sat/byte.

Di jendela input, kita melihat dua entri. Yang pertama adalah donasi 5000 sat. Kita lihat di sebelah kiri hash transaksinya (yang bisa kita cari di blockchain). Di sebelahnya, ada "21" - ini menunjukkan bahwa itu adalah output yang diberi label 21 dalam transaksi tersebut (sebenarnya output ke-22 karena yang pertama diberi label nol).

Hal yang perlu diperhatikan di sini: UTXO hanya ada di dalam sebuah transaksi. Untuk menghabiskan UTXO kita harus merujuknya, dan memasukkan referensi tersebut ke dalam input dari transaksi baru. Output kemudian menjadi UTXO baru dan UTXO lama menjadi STXO (Spent transaction output).

Baris kedua adalah donasi 10.000 sat. Ada "0" di sebelah hash transaksi dari mana asalnya karena itu adalah output pertama (dan mungkin satu-satunya) untuk transaksi tersebut.

Di jendela bawah, kita melihat alamat kita. Perhatikan total bitcoin dari input tidak cukup cocok dengan total output. Perbedaannya menjadi milik penambang. Penambang melihat perbedaan dalam semua transaksi di blok yang sedang dicoba ditambang, dan menambahkan angka tersebut ke dalam hadiahnya. (Biaya penambangan dengan cara ini sepenuhnya terputus dari rantai transaksi dan memulai kehidupan baru).

Jika kita menyesuaikan biaya penambangan, nilai output akan secara otomatis berubah.

> Penting untuk diperhatikan di sini: Perhatikan warna alamat di jendela transaksi. Ingat bahwa alamat hijau terdaftar di tab alamatmu. Jika sebuah alamat disorot hijau (atau kuning) di jendela transaksi, maka Electrum telah mengenali alamat tersebut sebagai miliknya. Jika alamat tidak memiliki sorotan, maka itu adalah alamat eksternal (eksternal ke dompet yang saat ini terbuka), dan kamu harus memeriksanya dengan lebih hati-hati.

Setelah memeriksa semua dalam transaksi dan senang dengan koin mana yang dibelanjakan, dan kemana koin tersebut akan pergi, Anda dapat klik "finalise."

![image](assets/42.webp)

Setelah klik "finalise", kamu tidak dapat lagi melakukan pengeditan - Jika perlu, kamu harus menutup ini dan memulai lagi. Perhatikan tombol "finalise" telah berubah menjadi "export", dan tombol baru muncul: "save", "combine", "sign" dan "broadcast". Tombol "broadcast" tidak aktif karena transaksi belum ditandatangani dan sehingga tidak valid pada tahap ini.

Setelah klik sign, jika kamu memiliki password untuk dompet Anda akan diminta untuk itu, dan kemudian status (kanan atas) akan berubah dari "Unsigned" menjadi "Signed". Kemudian tombol "Broadcast" akan tersedia.
Setelah menyiarkan, kamu dapat menutup jendela transaksi. Jika pergi ke tab alamat, kamu akan melihat alamat pertama kosong, dan alamat kedua memiliki 1 UTXO.
Catatan: Kita akan melihat semua perubahan ini bahkan sebelum transaksi ditambang ke dalam blok, atau "dikonfirmasi". Ini karena Electrum memperbarui saldo/transaksi berdasarkan tidak hanya data blockchain, tetapi juga data mempool. Tidak semua dompet melakukan ini.

Satu hal yang perlu diperhatikan adalah bahwa alih-alih menyiarkan, kita dapat menyimpan transaksi untuk nanti. Transaksi dapat disimpan baik dalam keadaan belum ditandatangani maupun sudah ditandatangani.

Klik tombol "export" (paradoksnya, JANGAN klik tombol "save"), dan kamu akan melihat beberapa opsi. Transaksi dikodekan dengan teks, dan oleh karena itu dapat disimpan dalam beberapa cara.

![image](assets/43.webp)

Menyimpan ke kode QR sangat menarik. Jika Anda memilih ini, sebuah QR akan muncul:

![image](assets/44.webp)

Anda kemudian dapat mengambil foto kode QR tersebut. Ada beberapa hal yang dapat Anda lakukan dengan ini, tetapi untuk sekarang, mari kita katakan Anda memuatnya kembali ke dalam dompet nanti. Anda dapat menutup Electrum, memuat dompet lagi, dan pergi ke menu Tools:

![image](assets/45.webp)

Ini akan memuat kamera komputer Anda. Anda kemudian menunjukkan kamera foto kode QR di ponsel Anda, dan ini akan memuat transaksi kembali, persis seperti Anda tinggalkan.

Tidak intuitif bagaimana cara memuat transaksi yang disimpan, jadi perhatikan khusus. Memuat transaksi bukanlah "tool" tetapi opsi tersebut tersembunyi di menu tools (hal lain yang harus diperbaiki oleh pengembang Electrum).

Proses serupa dimungkinkan dengan transaksi yang disimpan sebagai file. Cobalah berlatih dengan salah satu metode, dalam dompet yang sama. Saya tidak akan membahasnya di sini tetapi kamu dapat menggunakan fitur ini untuk memindahkan transaksi antara dompet yang sama di komputer yang berbeda, antara dompet multisignature, dan ke dan dari dompet hardware. Berikut adalah beberapa instruksi.

Ketika Anda mengklik tombol “save” setelah membuat transaksi, sebenarnya Anda tidak sedang menyimpan file teks atau dokumen biasa. Yang dilakukan Electrum adalah menyimpan transaksi tersebut sebagai proposed transaction (pembayaran yang diajukan) secara lokal di komputer Anda. Artinya, Electrum akan menganggap transaksi itu seperti sudah “dalam proses”, meskipun belum benar-benar dikirim ke jaringan Bitcoin. Jika Anda melakukannya tanpa sengaja, transaksi itu akan muncul di daftar riwayat dengan ikon kecil bergambar komputer. Jangan panik—Anda bisa menghapusnya dengan klik kanan pada transaksi tersebut dan memilih “delete”. Ini tidak akan menghapus bitcoin Anda. Electrum hanya akan “melupakan” bahwa transaksi itu pernah dibuat dan secara otomatis memperbarui saldo, menampilkan kembali sats Anda di tempat yang seharusnya.

### Alamat Perubahan

Alamat perubahan itu menarik. kamu perlu memahami UTXO untuk memahami penjelasan ini. Jika kamu menghabiskan ke alamat jumlah yang lebih kecil dari UTXO, maka bitcoin yang tersisa akan pergi ke penambang kecuali output perubahan ditentukan.

Kamu mungkin memiliki UTXO bitcoin 6.15 dan ingin menghabiskan 0.15 bitcoin untuk mendonasikan kepada beberapa pengunjuk rasa yang tertindas oleh pemerintah "demokratis" tirani di suatu tempat di dunia. Kemudian, kamu akan mengambil 6.15 bitcoin (menggunakan fungsi "spend from" di Electrum), dan memasukkannya dalam sebuah transaksi.

Kamu akan menempelkan alamat para pengunjuk rasa di kolom "pay to", mungkin kamu akan menulis "EndTheFed & WEF" di kolom "description", lalu masukkan jumlahnya 0.15 bitcoin dan klik "pay", kemudian pilih "advanced".
Di layar transaksi, untuk jendela input, kamu akan melihat UTXO bitcoin sebesar 6.15. Di jendela output, akan terlihat satu alamat tanpa sorotan (alamat para pengunjuk rasa) dengan 0.15 bitcoin di sampingnya. Lalu, ada satu alamat berwarna kuning dengan jumlah sedikit kurang dari 6.0 bitcoin. Itu adalah alamat kembalian yang secara otomatis dipilih oleh dompet dari daftar alamat kembalian miliknya sendiri. Alamat kembalian digunakan agar koin yang tersisa tidak masuk ke alamat penerima, yang mungkin akan digunakan lagi oleh orang lain atau untuk keperluan faktur. Ini penting agar tidak mengacaukan sistem dan menjaga privasi tetap terjaga.
Perhatikan bahwa saat Anda menyesuaikan biaya penambangan, jumlah output kembalian akan secara otomatis menyesuaikan, bukan jumlah pembayaran.

### Perubahan manual atau bayar ke banyak

Ini adalah fitur yang sangat menarik dari Electrum. Cara mengaksesnya seperti ini.

![image](assets/46.webp)

Anda kemudian dapat memasukkan beberapa tujuan untuk saldo UTXO yang akan dibelanjakan, seperti ini:

![image](assets/47.webp)

Tempel alamatnya, ketik koma, lalu spasi, lalu jumlahnya, lalu <enter>, lalu lakukan lagi. JANGAN MEMASUKKAN JUMLAH DALAM JENDELA “JUMLAH” – Electrum akan mengisi total di sini saat kamu mengetik jumlah individu di jendela “Bayar ke”.

Ini memungkinkanmu untuk secara manual menentukan kemana kembalian pergi (misalnya alamat tertentu di dompetmu, atau dompet lain), atau kamu dapat membayar banyak orang sekaligus. Jika totalnya tidak cukup tinggi untuk mencocokkan ukuran UTXO, Electrum masih akan membuat output kembalian tambahan untukmu.

Fitur Bayar ke Banyak juga memungkinkan kemungkinan untuk membuat "PayJoins" atau "CoinJoins" punyamu sendiri – di luar cakupan artikel ini, tetapi saya memiliki panduan di sini. (https://armantheparman.com/cj/)

## Dompet

Saya ingin mendemonstrasikan Dompet Hanya Menonton menggunakan Electrum. Untuk melakukan itu, saya perlu pertama-tama mendefinisikan “dompet”. Ada dua cara “dompet” digunakan dalam Bitcoin:

- Tipe A, “dompet” – merujuk pada perangkat lunak yang menunjukkan alamat dan saldo Anda, misalnya Electrum, Blue Wallet, Sparrow Wallet, dll.

- Tipe B, “dompet” – merujuk pada kumpulan alamat unik yang terkait dengan kombinasi dari seed_phrase/passphrase/derivation_path kita. Ada 8,6 miliar alamat dalam setiap dompet (4,3 miliar alamat penerima, dan 4,3 miliar alamat kembalian). Jika Anda mengubah sesuatu dalam seed phrase, passphrase, atau derivation path, Anda mendapatkan dompet yang belum digunakan dengan 8,6 miliar alamat kosong baru, dan semua unik.

Tipe mana yang dimaksud seseorang saat menggunakan kata “dompet” jelas dalam konteks.

## Dompet Hanya Menonton – sebuah latihan

Dompet hanya menonton adalah dompet yang tidak menyimpan kunci privat, sehingga tidak bisa mengirim Bitcoin, tapi tetap bisa melihat saldo, melacak transaksi, dan menerima pembayaran. Anda bisa membuatnya di Electrum dengan memilih opsi "watch-only" dan memasukkan kunci publik atau alamat. Dompet ini berguna untuk memantau dana tanpa risiko pencurian, dan akan lebih relevan saat kita membahas dompet perangkat keras nanti.
Kita akan membuat dompet reguler dummy, kali ini dengan sedikit tambahan kompleksitas berupa passphrase, lalu kita buat dompet hanya-menonton dari sana. Anda bisa mengikuti langkah-langkah persis seperti saya, atau buat versi Anda sendiri—ingat, ini hanya latihan, jadi dompetnya akan dibuang dan jangan digunakan untuk menyimpan dana sungguhan. Langkah pertama: buka situs web Ian Coleman dan hasilkan seed 12 kata.
Perhatikan 12 kata acak di tangkapan layar di bawah ini, dan bahwa saya telah memasukkan passphrase di bidang passphrase:

PASSPHRASE: “Craig Wright adalah pembohong dan penipu dan layak berada di penjara. Juga, Ross Ulbricht seharusnya dibebaskan dari penjara segera.”

Passphrase dapat terdiri hingga 100 karakter, dan sebaiknya tidak terlalu pendek maupun membingungkan. Gunakan kombinasi kata yang mudah Anda ingat, hindari huruf besar dan simbol agar lebih mudah diingat dan mengurangi stres jika suatu saat Anda perlu mengingatnya tanpa mencatat.

![image](assets/48.webp)

Selanjutnya, di Electrum, pergi ke menu file–>new/restore. Ketik nama unik untuk membuat dompet baru dan klik “next”.

![image](assets/49.webp)

Langkah selanjutnya Anda seharusnya sudah familiar, jadi saya akan mencantumkannya tanpa gambar:

- Standard wallet
- I already have a seed
- Salin dan tempel 12 kata di kotak, atau ketik secara manual.
- Klik opsi dan pilih BIP39, dan juga klik tanda centang passphrase (“extend this seed with custom words”)
- Masukkan passphrase Anda persis seperti yang Anda lakukan di halaman Ian Coleman
- Biarkan semantik skrip default dan jalur derivasi
- Tidak perlu menambahkan password (mengunci dompet)

Sekarang kembali ke situs Ian Coleman, ke bagian “derivation path”, dan klik tab “BIP 84” untuk memilih semantik skrip yang sama seperti default di Electrum (Native Segwit).

![image](assets/50.webp)

Kunci privat dan publik yang diperluas ada tepat di bawah, dan mereka berubah ketika Anda membuat perubahan pada jalur derivasi (atau apa pun yang lebih tinggi di halaman).

![image](assets/51.webp)

Kamu juga akan melihat “BIP32 extended private/public” keys – ini untuk diabaikan untuk saat ini.

Kunci privat diperluas memungkinkan regenerasi penuh dompet beserta kemampuan mengakses dan membelanjakan dana, sedangkan kunci publik diperluas hanya memungkinkan pembuatan dompet versi pengamat—tanpa akses untuk membelanjakan dana. Meski Electrum bisa menghasilkan seluruh alamat dari kunci publik diperluas, kunci privat tetap tak tersedia, jadi transaksi keluar tak dapat dilakukan. Sekarang, mari kita praktikkan untuk memperjelas hal ini.

Salin “account extended public key” ke clipboard.

Kemudian pergi ke Electrum, biarkan dompet yang kita buat terbuka, dan pergi ke file–>new/restore. Proses membuat dompet sedikit berbeda dari sebelumnya:

- Standard wallet
- Use a master key
- Tempel kunci publik diperluas di kotak dan lanjutkan
- Tidak perlu memasukkan passphrase; itu sudah bagian dari kunci publik diperluas
- Tidak perlu memasukkan semantik skrip dan jalur derivasi
- Tidak perlu menambahkan password (mengunci dompet)

Dompet hanya pengamat adalah jenis dompet yang memungkinkan pengguna memantau saldo dan aktivitas transaksi tanpa memiliki akses untuk membelanjakan dana, karena tidak menyimpan kunci privat. Dompet ini berguna untuk mengecek aktivitas dompet utama dari perangkat terpisah, mempermudah akuntansi atau audit, dan menerima dana secara aman tanpa risiko pencurian aset.

Salah satu alasan, dan bukan alasan utama, adalah dapat mengamati dompet dan saldo milikmu di komputer tanpa mengungkapkan kunci privatmu kepada malware apa pun di komputer tersebut.

Alasan lainnya adalah hal tersebut DIPERLUKAN untuk melakukan pembayaran jika Anda memilih untuk menyimpan kunci privat Anda di luar komputer; saya akan menjelaskan:

> Dompet perangkat keras (HWW) diciptakan agar sebuah perangkat dapat menyimpan kunci privat Anda secara aman (dikunci dengan PIN), tidak pernah mengungkapkan kunci ke komputer (bahkan ketika terhubung ke komputer melalui kabel), dan perangkat itu sendiri tidak dapat terhubung ke internet. Perangkat seperti itu tidak dapat melakukan transaksi sendiri karena semua transaksi bitcoin dimulai dengan merujuk pada UTXO(s) di blockchain (yang ada pada node). Sebuah dompet harus menentukan ID transaksi dimana UTXO berada, dan output mana dari transaksi yang akan digunakan. Hanya setelah menentukan input, baru transaksi baru dapat dibuat, apalagi ditandatangani. Dompet perangkat keras tidak dapat membuat transaksi karena mereka tidak memiliki akses ke UTXO apa pun – mereka tidak terhubung ke apa pun! Kunci publik yang diperluas biasanya diambil dari HWW, dan alamat kemudian ditampilkan di komputer – banyak orang akan familiar dengan perangkat lunak Ledger atau Trezor Suite yang menampilkan alamat dan saldo di komputer mereka – ini adalah dompet pengawas. Program-program ini dapat membuat transaksi, tetapi tidak dapat menandatangani. Mereka hanya dapat membuat transaksi ditandatangani oleh HWW yang terhubung dengan mereka. HWW mengambil transaksi yang baru dibuat dari dompet pengawas, menandatanganinya, dan kemudian mengirimkannya kembali ke komputer untuk disiarkan ke node. HWW tidak dapat menyiarkan sendiri, dompet pengawasnya yang melakukan itu. Dengan cara ini, kedua dompet (dompet kunci publik di komputer, dan dompet kunci privat di HWW) bekerja sama untuk menghasilkan, menandatangani, dan menyiarkan, sambil memastikan kunci privat tetap terisolasi dan jauh dari perangkat yang terhubung ke internet.

## Transaksi Bitcoin yang Ditandatangani Sebagian (PSBTs)

Mungkin untuk sebuah transaksi dibuat dan disimpan ke dalam file, kemudian dimuat ulang, ditandatangani, disimpan, dimuat ulang lagi, dan kemudian akhirnya disiarkan – saya tidak mengatakan siapa pun perlu melakukan ini; ini hanya sesuatu yang mungkin.

Sekarang pertimbangkan dompet multisignature 3 dari 5 – 5 kunci privat menciptakan sebuah dompet, dan 3 diperlukan untuk sepenuhnya menandatangani sebuah transaksi (Lihat di sini untuk mempelajari lebih lanjut tentang kunci dompet multisignature). Mungkin untuk memiliki 5 komputer yang berbeda masing-masing dengan salah satu dari lima kunci privat.

Komputer satu dapat menghasilkan transaksi dan menandatanganinya. Kemudian dapat menyimpannya ke file, dan mengirimkannya melalui email ke Komputer 2. Komputer 2 kemudian dapat menandatangani, dan berpotensi menyimpan file ke kode QR, dan mentransmisikan QR melalui panggilan Zoom ke Komputer 3 di sisi lain dunia. Komputer 3 dapat menangkap QR, memuat transaksi ke dalam electrum, dan menandatangani transaksi. Setelah 2 tanda tangan pertama, transaksi tersebut adalah PSBT (transaksi bitcoin yang ditandatangani sebagian). Setelah tanda tangan ketiga, transaksi menjadi sepenuhnya ditandatangani dan valid, siap untuk disiarkan.

Untuk mempelajari lebih lanjut tentang PSBTs, lihat panduan ini. (https://armantheparman.com/psbt/)

## Menggunakan Dompet Perangkat Keras dengan Electrum

Saya memiliki panduan tentang menggunakan dompet perangkat keras pada umumnya, yang menurut saya akan penting bagi orang-orang yang baru mengenal HWWs, untuk dibaca. (https://armantheparman.com/using-hwws/)
Anda juga akan menemukan panduan tentang berbagai merek HWW yang terhubung ke Sparrow Bitcoin Wallet di sini. (https://armantheparman.com/hwws/)
Ini akan menjadi panduan pertama saya yang menunjukkan cara menggunakan dompet perangkat keras dengan Electrum - Saya akan menggunakan dompet perangkat keras ColdCard untuk mendemonstrasikannya. Ini bukan dimaksudkan sebagai panduan terperinci tentang ColdCard secara spesifik, panduan itu ada di sini. Saya hanya menunjukkan poin-poin spesifik Electrum. (https://armantheparman.com/cc/)

### Menghubungkan melalui kartu micro SD (air-gapped)

Sebelum menghubungkan dompet nyata Anda melalui ColdCard, saya harap Anda telah melalui langkah-langkah sebelumnya untuk memuat dompet dummy Electrum dan mengatur parameter jaringan.

Kemudian, pada ColdCard, masukkan kartu SD. Saya asumsikan Anda sudah membuat seed Anda. Jika Anda mengakses dompet dengan passphrase, terapkan sekarang. Gulir ke bawah dan pilih menu Advanced/Tools –>Export Wallet –> Electrum Wallet.

Anda dapat menggulir ke bawah dan membaca pesannya. Ini selalu menawarkan Anda untuk memilih “1” untuk memasukkan nomor akun yang bukan nol (sesuatu yang merupakan bagian dari jalur derivasi), tetapi jika Anda mengikuti saran saya, Anda tidak mengutak-atik jalur derivasi default sehingga Anda tidak akan ingin nomor akun yang bukan nol; cukup tekan tanda centang untuk melanjutkan.

Kemudian pilih semantik skrip. Kebanyakan orang akan memilih “Native Segwit”.

Ini akan mengatakan “File dompet Electrum ditulis”, dan akan menampilkan nama file. Buat catatan mental tentang itu.

Kemudian keluarkan kartu micro SD dan masukkan ke dalam komputer dengan Electrum.

Beberapa sistem operasi akan secara otomatis membuka penjelajah file ketika Anda memasukkan microSD. Banyak orang akan melihat file dompet baru dan mengklik dua kali, dan bertanya-tanya mengapa itu tidak berfungsi. Ini bukan desain yang bagus. Anda sebenarnya harus mengabaikan penjelajah file (tutup), dan membuka file dompet menggunakan Electrum:

Buka Electrum. Jika sudah terbuka dengan dompet lain, pilih file –> baru. Kita mencari jendela ini:

![image](assets/52.webp)

Ini triknya, tidak intuitif. Klik “pilih”. Kemudian navigasikan sistem file pada kartu microSD dan temukan file dompet dan bukalah.

Sekarang Anda telah membuka dompet pengawasan yang sesuai dengan dompet perangkat keras Anda. Bagus.

### Menghubungkan melalui kabel USB.

Cara ini seharusnya lebih mudah, tetapi untuk komputer Linux, ini jauh lebih sulit. Sesuatu yang disebut “Udev rules” perlu diperbarui. Begini caranya (panduan terperinci https://armantheparman.com/gpg-articles/ ), dan secara singkat:

Ini adalah ide yang baik untuk memastikan sistem sudah terbaru. Kemudian:

```bash
sudo apt-get install libusb-1.0-0-dev libudev-dev
```

kemudian...

```bash
python3 -m pip install ckcc-protocol
```

Jika Anda mendapatkan kesalahan pastikan pip terinstal. Anda dapat memeriksanya dengan (pip –version), dan Anda dapat menginstalnya dengan (sudo apt install python3-pip)

Buat atau modifikasi, file, /etc/udev/rules.d/

Seperti ini:

```bash
sudo nano /etc/udev/rules.d
```

Sebuah editor teks akan terbuka. Salin teks dari sini dan tempelkan ke dalam file rules.d, simpan dan keluar.

![image](assets/53.webp)

Kemudian jalankan perintah-perintah ini satu demi satu:

```bash
sudo groupadd plugdev
sudo usermod -aG plugdev $(whoami)
sudo udevadm control –reload-rules && sudo udevadm trigger
```
Jika kamu mendapatkan pesan "group plugdev" sudah ada, itu tidak masalah, lanjutkan saja. Setelah perintah kedua, kamu tidak akan mendapatkan umpan balik/balasan, langsung saja lanjutkan ke perintah ketiga.
Kamu mungkin perlu memutuskan dan kemudian menyambungkan kembali ColdCard ke komputer.

Jika setelah semua ini masih tidak dapat menyambungkan ColdCard, saya akan mencoba memperbarui firmware (panduan segera, tapi untuk saat ini, Anda dapat menemukan instruksi di situs web produsen).

Selanjutnya, buat dompet baru:

- Dompet standar
- Gunakan perangkat keras
- Ini akan memindai dan mendeteksi ColdCard milikmu. Lanjutkan.
- Pilih semantik skrip dan jalur derivasi
- Putuskan apakah file dompet harus dienkripsi (disarankan)

### Transaksi menggunakan ColdCard

Dengan kabel terhubung, transaksi menjadi mudah. Menandatangani transaksi akan lancar.

Jika menggunakan perangkat dalam cara yang terisolasi dari jaringan, kamu harus secara manual memindahkan transaksi yang disimpan antar perangkat menggunakan kartu microSD. Ada beberapa trik.

Setelah membuat transaksi dan menyelesaikannya, kamu perlu mengklik tombol ekspor di sudut kiri bawah. Anda akan melihat "simpan ke file" yang secara kontraintuitif, bukan yang kita inginkan. Sebenarnya, kamu harus terlebih dahulu pergi ke opsi menu terakhir yang mengatakan "untuk dompet perangkat keras", dan kemudian, dari dalam pilihan itu, temukan "simpan ke file" lainnya dan pilih itu. Kemudian simpan file ke microSD, keluarkan kartu dan masukkan ke ColdCard. Ingat bahwa Anda mungkin perlu menerapkan passphrase untuk memilih dompet yang benar. Layar akan mengatakan siap untuk menandatangani. Klik tanda centang, periksa transaksi, dan lanjutkan dengan mengonfirmasi dengan tanda centang. Setelah selesai, keluarkan kartu, dan masukkan kembali ke komputer.

Kemudian kita perlu membuka transaksi menggunakan electrum. Fungsinya tersembunyi di menu alat –> muat transaksi. Navigasikan sistem file dan temukan file tersebut. Akan ada tiga file setiap kali kamu menandatangani. File asli yang disimpan oleh Watching Wallet, dan dua yang dibuat oleh ColdCard (saya tidak tahu mengapa ini terjadi). Satu akan mengatakan "ditandatangani" dan satu akan mengatakan "final". Ini tidak intuitif tetapi yang "ditandatangani" tidak berguna, kita perlu membuka transaksi "final".

Setelah termuat, kamu dapat mengklik "siarkan" dan pembayaran akan dilakukan.

## Memperbarui Electrum dan Direktori Tersembunyi ".electrum"

Electrum berada di komputermu di dua tempat. Ada aplikasinya sendiri, dan ada folder konfigurasi tersembunyi. Folder tersebut berada di tempat yang berbeda tergantung pada sistem operasi komputermu:

Windows:

> C:/Users/nama_pengguna_di_sini/AppData/Roaming/Electrum

Mac:

> /Users/nama_pengguna_di_sini/.electrum

Linux:

> /home/nama_pengguna_di_sini/.electrum

Perhatikan bahwa “.” sebelum “electrum” di Linux dan Mac – itu menunjukkan direktori tersebut tersembunyi. Juga, perhatikan bahwa direktori ini hanya dibuat (secara otomatis) setelah menjalankan Electrum untuk pertama kalinya. Arahan berisi file konfigurasi electrum dan juga direktori yang menyimpan dompet yang telah Anda simpan.

Jika perlu menghapus program Electrum dari komputermu, direktori tersembunyi akan tetap ada, kecuali jika secara aktif menghapus itu juga.
Untuk meningkatkan Electrum, kita mengikuti prosedur yang sama seperti yang saya jelaskan di awal untuk mengunduh dan memverifikasi. Anda kemudian akan memiliki dua salinan program di komputer Anda, dan Anda dapat menjalankan salah satu dari mereka – setiap program akan mengakses folder electrum tersembunyi yang sama untuk konfigurasi dan akses dompetnya. Semua hal yang kita simpan, seperti unit dasar, node default untuk terhubung, preferensi lainnya, dan akses ke dompet, akan tetap ada karena semua itu disimpan di folder tersebut.

### Memindahkan Electrum dan Dompet ke komputer lain

Untuk melakukan ini, kita dapat menyalin file program ke drive USB, dan juga menyalin direktori .electrum. Kemudian salin atau pindahkan ke komputer baru. Nah, kita tidak perlu memverifikasi program lagi. Tapi pastikan untuk menyalin direktori .electrum ke lokasi default (ingat untuk menyalinnya SEBELUM menjalankan Electrum untuk pertama kalinya di komputer tersebut, jika tidak, folder .electrum default yang kosong akan terisi, dan kamu mungkin akan bingung).

## Label

Seperti yang saya jelaskan sebelumnya, pada tab alamat, ada kolom label. kamu dapat mengklik dua kali di sana dan memasukkan catatan untuk dirimu sendiri (hanya di komputer milikmu, tidak publik, dan tidak di blockchain).

![image](assets/54.webp)

Ketika memindahkan dompet Electrum milikmu ke komputer lain, kamu mungkin tidak ingin kehilangan semua catatan ini. Kamu dapat mencadangkannya ke file menggunakan menu, dompet–> label –> ekspor, dan kemudian di komputer baru, gunakan dompet–>label–>impor.

## Tips:

Jika kalian merasa sumber daya ini berguna, dan ingin mendukung apa yang kami lakukan untuk Bitcoin, bisa menyumbangkan beberapa sats di sini:

Alamat Lightning Statis: dandysack84@walletofsatoshi.com
https://armantheparman.com/electrum/
