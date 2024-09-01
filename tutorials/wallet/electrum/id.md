---
name: Electrum

description: Panduan Lengkap Electrum, dari pemula hingga mahir
---

![cover](assets/cover.webp)

Deskripsi untuk Electrum

https://twitter.com/ElectrumWallet
https://electrum.org/
https://electrum.readthedocs.io/

> "Saya harus mengatakan, ketika saya menemukan panduan ini saya terkejut. Selamat untuk Arman the Parman atas ini. Akan sangat disayangkan jika tidak dihosting di sini dan diterjemahkan ke sebanyak mungkin bahasa. Sungguh, beri tip pada orang itu." Rogzy

Postingan asli:

![Electrum Desktop Wallet (Mac / Linux) - unduh, verifikasi, sambungkan ke node Anda.](https://youtu.be/wHmQNcRWdHM)

![Melakukan transaksi Bitcoin dengan Electrum](https://youtu.be/-d_Zd7VcAfQ)

## Mengapa Electrum?

Ini adalah panduan terperinci tentang cara menggunakan Electrum Bitcoin Wallet, dengan solusi untuk semua jebakan dan keanehannya - sesuatu yang saya kembangkan setelah beberapa tahun penggunaan, dan mengajar siswa tentang keamanan/privasi Bitcoin. Electrum bukanlah dompet Bitcoin terbaik bagi orang yang ingin menjaga segalanya semudah mungkin, dan lebih memilih untuk tetap pada level pemula. Sebaliknya, ini untuk orang yang adalah, atau bercita-cita menjadi, pengguna "power".

Untuk Bitcoiner baru, ini sangat baik hanya jika di bawah pengawasan pengguna berpengalaman untuk menunjukkan jalan. Jika belajar menggunakannya sendiri, itu akan aman asalkan mereka meluangkan waktu dan menggunakannya dalam lingkungan pengujian dengan hanya sejumlah kecil sats pada awalnya. Panduan ini mendukung upaya tersebut, tetapi ini juga merupakan referensi yang baik untuk siapa saja.

> Peringatan: Panduan ini besar. Jangan mencoba melakukan semua ini dalam satu hari. Lebih baik untuk menyimpan panduan dan mengikisnya dari waktu ke waktu.

## Mengunduh Electrum

Idealnya, gunakan komputer Bitcoin khusus untuk transaksi Bitcoin Anda (Panduan saya untuk ini https://armantheparman.com/mint/) _(JUGA tersedia di bagian privasi)_. Tidak masalah untuk berlatih dengan jumlah kecil pada komputer "kotor" ketika Anda pertama kali belajar (siapa tahu berapa banyak malware tersembunyi yang telah terakumulasi di komputer reguler Anda selama bertahun-tahun - Anda tidak ingin memaparkan dompet Bitcoin Anda kepada mereka).

Dapatkan Electrum dari https://electrum.org/.

Klik tab Unduh di bagian atas.

Klik pada tautan unduhan yang sesuai dengan komputer Anda. Komputer Linux atau Mac dapat menggunakan tautan Python (lingkaran merah). Komputer Linux dengan chip Intel atau AMD dapat menggunakan Appimage (lingkaran hijau; ini seperti file eksekusi Windows). Perangkat Raspberry Pi memiliki mikroprosesor ARM dan hanya dapat menggunakan versi Python (lingkaran merah), bukan Appimage, meskipun Pi menjalankan Linux. Lingkaran biru untuk Windows dan lingkaran hitam untuk Mac.

![image](assets/1.webp)

## Memverifikasi Electrum

Tujuan dari "memverifikasi" unduhan adalah untuk memastikan tidak satu bit data pun yang telah diubah. Ini mencegah Anda menggunakan versi perangkat lunak "diretas" yang berbahaya. Tidak masalah untuk melewatkan ini asalkan Anda hanya menggunakan salinan yang diunduh untuk berlatih, yaitu jangan gunakan dompet yang menyimpan uang serius. Kemudian, setelah Anda siap menggunakan Electrum untuk dana nyata Anda, Anda harus menghapus salinan Anda dan memulai dari awal, kali ini memverifikasi unduhan Anda.
Untuk melakukan ini, kami menggunakan alat kriptografi kunci publik/privat – gpg, yang telah kami tulis panduannya di sini (https://armantheparman.com/gpg/). Alat gpg tersedia di semua sistem operasi Linux. Untuk Mac dan Windows, lihat link gpg untuk instruksi pengunduhan.

Selain mengunduh perangkat lunak Electrum, untuk keamanan, Anda juga memerlukan TANDA TANGAN digital dari perangkat lunak tersebut. Ini adalah rangkaian teks (sebenarnya adalah angka yang dikodekan menggunakan teks) yang dihasilkan oleh pengembang dengan kunci gpg PRIVAT-nya. Menggunakan program gpg, kita kemudian dapat "menguji" TANDA TANGAN tersebut terhadap kunci PUBLIK-nya (dibuat dari kunci privat pengembang) yang dapat diakses oleh semua orang, dibandingkan dengan FILE unduhan.

Dengan kata lain, dengan tiga input (tanda tangan, kunci publik, dan file data), kita mendapatkan output benar atau salah untuk mengonfirmasi bahwa file tersebut tidak telah diubah.

Untuk mendapatkan tanda tangan, klik pada link yang sesuai dengan file yang Anda unduh (lihat panah berwarna):

![image](assets/2.webp)

Mengklik link mungkin secara otomatis mengunduh file ke folder unduhan Anda, atau mungkin terbuka di browser. Jika terbuka di browser, Anda perlu menyimpan file tersebut. Anda dapat klik kanan dan pilih "simpan sebagai". Tergantung pada sistem operasi atau browser, Anda mungkin perlu klik kanan pada area ruang putih, bukan teksnya.

Berikut adalah tampilan teks yang diunduh. Anda dapat melihat ada beberapa tanda tangan – ini adalah tanda tangan oleh orang yang berbeda. Anda dapat memverifikasi masing-masing atau salah satunya. Saya akan menunjukkan kepada Anda cara memverifikasi hanya tanda tangan pengembang.

![image](assets/3.webp)

Selanjutnya, Anda perlu mendapatkan kunci publik ThomasV – dia adalah pengembang utama. Anda bisa mendapatkannya langsung dari dia, akun Keybase-nya, Github, atau orang lain, dari keyserver, atau dari situs web Electrum.

Mendapatkannya dari situs web Electrum sebenarnya adalah cara yang paling tidak aman, karena jika situs web ini berbahaya (hal yang sedang kita periksa) mengapa kita mendapatkan kunci publik dari sana (kunci publik bisa palsu)?

Untuk menjaga agar hal ini sederhana untuk sekarang, saya akan menunjukkan kepada Anda cara mendapatkannya dari situs web tersebut, tetapi ingatlah hal ini. Berikut adalah salinannya (https://github.com/spesmilo/electrum/blob/master/pubkeys/ThomasV.asc ) di GitHub yang dapat Anda bandingkan.

Gulir ke bawah halaman sedikit untuk menemukan link ke kunci publik ThomasV (lingkaran merah di bawah). Klik dan unduh, atau jika membuka beberapa teks di browser, klik kanan untuk menyimpan.

![image](assets/4.webp)

Anda sekarang memiliki 3 file baru, mungkin semuanya ada di folder unduhan. Tidak masalah di mana mereka berada, tetapi prosesnya menjadi lebih mudah jika Anda menaruh semuanya dalam folder yang sama.

Ketiga file tersebut:

1. Unduhan Electrum
2. File tanda tangan (biasanya memiliki nama file yang sama dengan unduhan Electrum dengan tambahan “.asc”)
3. Kunci publik ThomasV.

Buka terminal di Mac atau Linux, atau command prompt (CMD) di Windows.

Navigasikan ke direktori Downloads (atau di mana pun Anda menaruh ketiga file tersebut). Jika Anda tidak tahu apa maksudnya, pelajari dari video singkat ini untuk Linux/Mac (https://www.youtube.com/watch?v=AO0jzD1hpXc) dan ini untuk Windows (https://www.youtube.com/watch?v=9zMWXD-xoxc). Ingat bahwa pada komputer Linux, nama direktori peka terhadap huruf besar-kecil.
Di terminal, ketik ini untuk mengimpor kunci publik ThomasV ke dalam "keyring" komputer Anda (keyring adalah konsep abstrak - sebenarnya hanya sebuah file di komputer Anda):
```bash
gpg --import ThomasV.asc
```

Pastikan nama file sesuai dengan yang telah Anda unduh. Perhatikan juga bahwa itu adalah tanda strip ganda bukan strip tunggal. Catat juga ada spasi sebelum dan setelah "--import". Kemudian tekan <enter>.

File seharusnya terimpor. Jika Anda mendapatkan kesalahan, periksa apakah Anda berada di direktori tempat file tersebut benar-benar ada. Untuk memeriksa direktori mana Anda berada (di Mac atau Linux), ketik pwd. Untuk melihat file apa saja yang ada di direktori tempat Anda berada (di Mac atau Linux), ketik ls. Anda seharusnya melihat file teks "ThomasV.asc" terdaftar, mungkin di antara file lainnya.

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

Jangan hanya menyalin nama file yang telah saya tunjukkan di sini - pastikan mereka cocok dengan nama file apa yang Anda miliki di sistem Anda.

Tekan <enter> untuk menjalankan perintah. Anda seharusnya melihat "good signature from ThomasV" untuk menunjukkan keberhasilan. Akan ada beberapa kesalahan karena kita tidak memiliki kunci publik untuk tanda tangan orang lain yang terkandung dalam file tanda tangan (sistem menggabungkan tanda tangan dalam satu file mungkin berubah dalam versi selanjutnya). Juga, ada peringatan di bagian bawah yang bisa kita abaikan (ini memberi tahu kita bahwa kita belum secara eksplisit memberitahu komputer bahwa kita mempercayai kunci publik ThomasV).

Sekarang kita memiliki salinan Electrum yang telah diverifikasi dan aman untuk digunakan.

## Menjalankan Electrum

### Menjalankan Electrum jika menggunakan Python

Jika Anda mengunduh versi Python, inilah cara membuatnya bekerja. Anda akan melihat di halaman unduhan ini:

![image](assets/5.webp)

Untuk Linux, ide yang baik untuk pertama-tama memperbarui sistem Anda:

```bash
sudo apt-get update
sudo apt-get upgrade
```

Salin teks kuning yang disorot, tempelkan ke terminal, dan tekan <enter>. Anda akan diminta kata sandi Anda, mungkin konfirmasi untuk melanjutkan, dan kemudian itu akan menginstal file-file tersebut ("dependencies").

Anda juga perlu mengekstrak file yang dikompres ke direktori pilihan Anda. Anda dapat melakukan ini dengan antarmuka pengguna grafis, atau dari baris perintah (perintah yang disorot pink) - ingat nama file Anda mungkin berbeda. (Perhatikan bahwa ketika kita memverifikasi unduhan di bagian sebelumnya, itu adalah file zip yang kita verifikasi, bukan direktori yang diekstrak.)

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

Ini sedikit lebih mudah, tapi tidak se-mudah file executable Windows. Tergantung pada versi Linux yang Anda gunakan, secara default, file Appimage mungkin memiliki atribut yang diset sehingga eksekusi tidak diizinkan oleh sistem. Kita harus mengubah ini. Jika Appimage Anda berfungsi, Anda dapat melewati langkah ini. Navigasikan ke tempat file berada, menggunakan terminal, lalu jalankan perintah ini:

```bash
sudo chmod ug+x Electrum-4.1.5-x86_64.AppImage
```

“sudo” memberikan hak superuser; “chmod” adalah perintah untuk mengubah mode, mengubah siapa yang dapat membaca, menulis, atau mengeksekusi; “ug+x” berarti kita sedang memodifikasi pengguna dan grup untuk mengizinkan eksekusi.

Sesuaikan nama file agar cocok dengan versi Anda.

Kemudian, Electrum akan berjalan dengan mengklik dua kali ikon Appimage.

### Menjalankan Electrum dengan Mac

Cukup klik dua kali file yang diunduh (itu adalah “drive”). Sebuah jendela akan terbuka. Seret ikon Electrum di jendela ke desktop Anda, atau ke mana pun Anda ingin menyimpan program tersebut. Anda kemudian dapat “mengeluarkan” drive, dan menghapus drive (file yang diunduh).

Untuk menjalankan program, cukup klik dua kali. Anda mungkin mendapatkan beberapa kesalahan spesifik Mac yang perlu dilewati.

### Menjalankan Electrum dengan Windows

Meskipun saya paling tidak suka Windows, ini adalah metode paling sederhana. Cukup klik dua kali file executable untuk menjalankan.

## Mulai dengan dompet dummy

Ketika Anda pertama kali memuat Electrum, sebuah jendela akan terbuka seperti ini:

![image](assets/6.webp)

Kita akan memilih server Anda secara manual nanti, tetapi untuk sekarang, biarkan default dan auto-connect.

Selanjutnya, buat dompet dummy – jangan pernah memasukkan dana ke dalam dompet ini. Tujuan dari dompet dummy ini adalah untuk melanjutkan melalui perangkat lunak dan memastikan semuanya berfungsi dengan baik sebelum Anda memuat dompet asli Anda. Kita mencoba menghindari secara tidak sengaja memberikan privasi dengan dompet asli. Jika Anda hanya berlatih, dompet yang Anda buat dapat dianggap sebagai dompet dummy.

Anda dapat membiarkan nama sebagai “default_wallet” atau mengubahnya sesuai yang Anda suka, dan klik next. Nanti, jika Anda memiliki beberapa dompet, Anda dapat menemukan dan membukanya pada tahap ini dengan pertama kali mengklik “Choose…”

![image](assets/7.webp)

Pilih “Standard wallet” dan <Next>:

![image](assets/8.webp)

Kemudian, pilih “I already have a seed”. Saya tidak ingin Anda terbiasa membuat seed Electrum, karena menggunakan protokolnya sendiri yang tidak kompatibel dengan dompet lain – inilah mengapa kita tidak mengklik “new seed”.

![image](assets/9.webp)

Pergi ke https://iancoleman.io/bip39/ dan buat seed dummy. Pertama, ubah jumlah kata menjadi 12 (yang merupakan praktik umum), lalu klik “generate” dan salin kata-kata di kotak ke clipboard Anda.

![image](assets/10.webp)

Kemudian tempelkan kata-kata ke dalam Electrum. Berikut adalah contohnya:

![image](assets/11.webp)

Electrum akan mencari kata-kata yang cocok dengan protokolnya sendiri. Kita harus melewati itu. Klik opsi, dan pilih BIP39 Seed:

![image](assets/12.webp)
Benih kemudian menjadi valid. (Sebelum melakukan ini, Electrum mengharapkan sebuah benih Electrum sehingga benih ini dianggap tidak valid). Sebelum Anda klik lanjut, perhatikan teks yang mengatakan "Checksum OK". Ini penting (untuk dompet nyata yang mungkin Anda gunakan nanti) bahwa Anda melihat ini sebelum melanjutkan, karena ini mengonfirmasi validitas benih yang Anda masukkan. Peringatan di dekat bagian bawah dapat diabaikan, itu adalah keluhan pengembang Electrum tentang BIP39 dan klaim "FUD" mereka bahwa versi mereka (yang tidak kompatibel dengan dompet lain) lebih unggul.

> Sebuah penyimpangan cepat untuk peringatan penting. Tujuan dari checksum adalah untuk memastikan Anda memasukkan benih Anda tanpa kesalahan ketik. Checksum adalah bagian akhir dari benih (kata ke-12 menjadi kata checksum) yang secara matematis ditentukan oleh bagian awal dari benih (11 kata). Jika Anda mengetik sesuatu yang salah di awal, kata checksum tidak akan cocok secara matematis, dan perangkat lunak dompet akan memberi tahu Anda dengan peringatan. Ini tidak berarti bahwa benih tidak dapat digunakan untuk membuat Dompet Bitcoin yang fungsional. Bayangkan membuat dompet dengan kesalahan ketik, memuat dompet dengan bitcoin, kemudian suatu hari Anda mungkin perlu mengembalikan dompet, tetapi ketika Anda melakukannya, Anda tidak mereproduksi kesalahan ketik - Anda akan mengembalikan dompet yang salah! Sangat berbahaya bahwa Electrum akan membiarkan Anda melanjutkan membuat dompet jika checksum Anda tidak valid, jadi diingatkan, itu tanggung jawab Anda untuk memastikan. Dompet lain tidak akan membiarkan Anda melanjutkan, yang jauh lebih aman. Ini adalah salah satu hal yang saya maksud ketika saya mengatakan Electrum baik untuk digunakan, setelah Anda belajar menggunakannya dengan benar (pengembang Electrum harus memperbaiki ini).

Perhatikan bahwa jika Anda ingin menambahkan passphrase, kesempatan untuk memilih itu ada di jendela opsi ini, tepat di bagian atas.

Setelah mengklik OK, Anda akan dibawa kembali ke tempat Anda mengetik frasa benih. Jika Anda memilih opsi passphrase, Anda TIDAK memasukkannya dengan kata-kata benih (permintaan untuk itu datang selanjutnya).

Jika Anda tidak meminta passphrase, Anda akan melihat layar ini selanjutnya - lebih banyak opsi untuk tipe skrip dompet Anda dan jalur derivasi yang dapat Anda pelajari di sini (https://armantheparman.com/public-and-private-keys/), tetapi cukup biarkan default dan lanjutkan.

![image](assets/13.webp)

> Untuk info tambahan: Opsi pertama memungkinkan Anda memilih antara legacy (alamat yang dimulai dengan “1”), pay-to-script-hash (alamat yang dimulai dengan “3”), atau bech32/native segwit (alamat yang dimulai dengan “bc1q”). Saat penulisan, Electrum belum mendukung taproot (alamat yang dimulai dengan “bc1p”). Opsi kedua di jendela ini memungkinkan Anda untuk memodifikasi jalur derivasi. Saya sarankan Anda tidak pernah memodifikasinya, terutama sebelum memahami apa artinya. Orang akan menekankan pentingnya menuliskan jalur derivasi sehingga Anda dapat memulihkan dompet Anda jika diperlukan, tetapi jika Anda meninggalkannya sebagai default, Anda mungkin akan baik-baik saja, jadi jangan panik - tetapi masih merupakan praktik yang baik untuk menuliskan jalur derivasi.

Selanjutnya, Anda akan diberi opsi untuk menambahkan PASSWORD. Ini tidak boleh disamakan dengan “PASSPHRASE”. Password mengunci file di komputer Anda. Passphrase adalah bagian dari pembuatan kunci pribadi. Karena ini adalah dompet palsu, Anda dapat meninggalkan password kosong dan melanjutkan.

![image](assets/14.webp)
Anda akan mendapatkan pop-up tentang notifikasi versi baru (Saya sarankan Anda memilih tidak). Dompet tersebut kemudian akan menghasilkan dirinya sendiri dan siap digunakan (tetapi ingat, dompet ini ditujukan untuk dihapus, ini hanya dompet palsu).
![image](assets/15.webp)

Ada beberapa hal yang saya sarankan Anda lakukan untuk menyiapkan lingkungan perangkat lunak (hanya diperlukan sekali):

### Ubah unit menjadi BTC

Pergi ke menu atas, alat –> preferensi electrum, dan di sana di bawah tab umum, Anda akan menemukan opsi untuk mengubah "unit dasar" menjadi BTC.
Aktifkan tab Alamat dan Koin

Pergi ke menu atas, tampilan, dan pilih "tampilkan alamat". Kemudian kembali ke tampilan dan pilih "tampilkan koin".

### Aktifkan Oneserver

Secara default, Electrum terhubung ke node acak. Ini juga terhubung ke banyak node sekunder lainnya. Saya tidak yakin data apa yang ditukar dengan node sekunder tersebut, tetapi kita tidak ingin itu terjadi, demi privasi. Bahkan jika Anda menentukan node, misalnya node Anda sendiri, node lainnya juga akan terhubung, dan saya tidak yakin informasi apa yang dibagikan. Bagaimanapun, mudah untuk mencegahnya. Sebelum saya menunjukkan cara menentukan node Anda sendiri, kami akan memaksa Electrum untuk hanya terhubung ke satu server pada satu waktu.

> Ada cara untuk melakukan ini dengan menentukan "oneserver" dari baris perintah, tetapi saya tidak menyarankan cara ini. Saya akan menunjukkan alternatif yang menurut saya lebih mudah dalam jangka panjang, dan lebih mungkin tidak membiarkan Anda secara tidak sengaja terhubung ke node lain.

Alasan kami menggunakan dompet palsu adalah jika kami telah memuat dompet nyata kami, dengan bitcoin nyata kami, kami akan telah terhubung secara tidak sengaja ke node acak sekarang (bahkan jika kami memilih "atur server secara manual" di awal, itu masih terhubung ke node sekunder lainnya karena alasan tertentu (hei pengembang Electrum, Anda harus memperbaiki ini). Jika dompet kami bersifat pribadi, ini akan menjadi bencana.

Kami juga tidak dapat melakukan langkah-langkah yang akan saya tunjukkan di bawah ini tanpa terlebih dahulu memuat beberapa jenis dompet. (Kami akan mengedit file konfigurasi yang hanya terisi dan siap untuk diedit setelah dompet dimuat).

**Tutup Electrum (PENTING, jika Anda tidak melakukan ini, perubahan berikut yang Anda buat akan terhapus).**

### File Konfigurasi LINUX/MAC

Buka terminal di Linux atau Mac (instruksi Windows nanti):

Anda seharusnya secara otomatis berada di folder home. Dari sana, navigasikan ke folder pengaturan electrum tersembunyi (ini berbeda dengan tempat aplikasi berada).

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
Tepat di bawah itu, Anda akan melihat sebuah bidang teks dan alamat server ada di sana. Anda saat ini terhubung ke node acak tersebut. Lebih lanjut tentang menghubungkan ke sebuah node di bagian selanjutnya.

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

Ngomong-ngomong, berikut adalah instruksi untuk menjalankan node Anda sendiri, dan ini adalah alasan mengapa Anda harus melakukannya. (semua tutorial di bagian Node atau di kursus gratis kami)

### Terhubung ke node teman melalui Tor (Panduan segera hadir.)

### Terhubung ke node perusahaan terpercaya

Alasan untuk melakukan ini adalah jika Anda harus mengakses blockchain dan Anda tidak memiliki node Anda sendiri yang tersedia (atau node teman).

Mari terhubung ke node Bitaroo - Kami diberitahu bahwa mereka tidak mengumpulkan data. Mereka adalah pertukaran Bitcoin Only, dijalankan oleh seorang Bitcoiner yang bersemangat. Terhubung dengan mereka melibatkan sedikit kepercayaan, tetapi itu lebih baik daripada terhubung ke node acak, yang bisa jadi adalah perusahaan pengawasan.

Dapatkan ke Pengaturan Jaringan dengan mengklik lingkaran di bagian kanan bawah jendela Dompet (merah menunjukkan tidak terhubung, hijau menunjukkan terhubung, dan biru menunjukkan terhubung melalui Tor).

![image](assets/16.webp)

Setelah Anda mengklik ikon lingkaran, sebuah jendela pop-up akan muncul: Dompet Anda akan menunjukkan "terhubung ke 1 node" karena kita telah memaksa itu sebelumnya.

Hilangkan tanda centang pada kotak "pilih server secara otomatis", lalu di Bidang Server, ketik detail Bitaroo seperti yang ditunjukkan:

![image](assets/17.webp)

Tutup jendela, dan sekarang kita seharusnya terhubung ke node Bitaroo. Untuk mengonfirmasi, lingkaran harus berwarna hijau. Klik lagi dan periksa bahwa detail server tidak berubah kembali ke node acak.

### Terhubung ke node Anda sendiri

Jika Anda memiliki node Anda sendiri itu bagus. Jika Anda hanya memiliki Bitcoin Core, dan bukan Electrum SERVER juga, Anda belum akan dapat menghubungkan Electrum WALLET ke node Anda.

> Catatan: Electrum Server dan Electrum Wallet adalah hal yang berbeda. Server adalah perangkat lunak yang diperlukan agar Electrum Wallet dapat berkomunikasi dengan blockchain Bitcoin - Saya tidak tahu mengapa ini dirancang seperti itu - mungkin untuk kecepatan tetapi saya bisa salah.
Jika Anda menjalankan paket perangkat lunak node seperti MyNode (yang saya rekomendasikan untuk pemula), Raspiblitz (direkomendasikan saat Anda menjadi lebih mahir), atau Umbrel (saya pribadi belum merekomendasikannya karena saya mengalami terlalu banyak masalah), maka Anda akan dapat menghubungkan dompet Anda hanya dengan memasukkan alamat IP dari komputer (Raspberry Pi) yang menjalankan node, ditambah dengan titik dua, dan 50002, seperti yang ditunjukkan pada gambar di bagian sebelumnya. (Lebih lanjut saya akan menunjukkan cara menemukan alamat IP node Anda).

Buka pengaturan Jaringan (klik lingkaran hijau atau merah di pojok kanan bawah). Hilangkan tanda centang pada kotak "pilih server secara otomatis", kemudian masukkan alamat IP Anda seperti yang telah saya lakukan, alamat IP Anda akan berbeda, tetapi titik dua dan "50002" harus sama.

Tutup jendela, dan sekarang kita seharusnya terhubung ke node Anda. Untuk mengonfirmasi, klik lingkaran lagi dan periksa bahwa detail server tidak berubah kembali ke node acak.

Terkadang, meskipun melakukan segalanya dengan benar, tampaknya itu menolak untuk terhubung. Berikut adalah hal-hal yang dapat dicoba...

- Upgrade ke versi Electrum yang lebih baru, dan perangkat lunak node Anda
- Coba hapus folder cache di direktori ".electrum"
- Coba ubah port dari 50002 menjadi 50001 di pengaturan jaringan
- Gunakan panduan ini untuk terhubung menggunakan Tor sebagai alternatif (https://armantheparman.com/tor/)
- Reinstall Electrum Server di node

## MENEMUKAN ALAMAT IP NODE ANDA

Alamat IP bukanlah sesuatu yang biasanya diketahui dan digunakan oleh pengguna reguler. Saya telah membantu banyak orang menjalankan node, dan kemudian menghubungkan dompet mereka ke node – sebuah hambatan yang sering tampaknya adalah menemukan alamat IP-nya.

Untuk MyNode, Anda dapat mengetik di jendela browser: `mynode.local`

Terkadang, “mynode.local” tidak berfungsi (pastikan Anda tidak mengetiknya di bilah pencarian Google. Untuk memaksa bilah navigasi mengenali teks Anda sebagai alamat dan bukan pencarian, awali teks dengan `http://` seperti ini: `http://mynode.local`. Jika itu tidak berhasil, coba dengan "s", seperti ini: `https://mynode.local`.

Ini akan mengakses perangkat, dan Anda dapat mengklik tautan pengaturan (lihat "lingkaran" biru saya di bawah) untuk menampilkan layar ini di mana alamat IP terletak:

Halaman ini akan dimuat dan Anda akan melihat alamat IP node (lingkaran "biru")

Kemudian, di masa depan, Anda dapat mengetik 192.168.0.150, atau http://192.168.0.150 ke dalam browser Anda.

Untuk Raspiblitz (ketika tidak menghubungkan layar), Anda memerlukan metode berbeda (yang juga berfungsi untuk MyNode):

Login ke halaman web router Anda – di sini kita akan menemukan alamat IP dari semua perangkat yang terhubung. Halaman web router akan berupa alamat IP yang Anda masukkan ke dalam browser web. Tampilan saya adalah:

    http://192.168.0.1

Untuk mendapatkan kredensial login ke router, Anda dapat mencarinya di manual pengguna atau terkadang bahkan pada stiker di router itu sendiri. Cari nama pengguna dan kata sandi. Jika Anda tidak dapat menemukannya, coba User: “admin” Password: “password”

Jika Anda berhasil login, Anda akan melihat perangkat yang terhubung dan dari nama-nama mereka, mungkin jelas mana yang node Anda. Alamat IP akan ada di sana.
### Jika dua metode pertama gagal, metode terakhir akan berhasil tetapi itu melelahkan:
Pertama, temukan alamat IP dari perangkat apa pun di jaringan Anda (komputer saat ini sudah cukup).

Di Mac, Anda akan menemukannya di preferensi Jaringan:

![image](assets/21.webp)

Kami tertarik pada 4 elemen pertama (192.168.0), bukan elemen ke-4, "166" yang Anda lihat di gambar (milik Anda akan berbeda).

Untuk Linux, gunakan baris perintah:

```bash
ifconfig | grep inet
```

Garis vertikal itu adalah simbol "pipe" dan Anda akan menemukannya di bawah tombol <delete>. Anda akan melihat beberapa output dan sebuah alamat IP. (Abaikan 127.0.0.1 itu bukan itu, dan abaikan netmask)

Untuk Windows, buka prompt perintah (cmd) dan ketik:

```bash
ipconfig/all
```

dan tekan Enter. Alamat IP dapat ditemukan di output.

Itu adalah bagian yang mudah. Bagian yang sulit sekarang adalah menemukan alamat IP node Anda – kita perlu menebak secara brute-force. Misalkan misalnya alamat IP komputer Anda dimulai dengan 192.168.0.xxx, maka untuk node Anda, di browser, coba: `https://192.168.0.2`

Nomor terkecil yang mungkin adalah 2 (0 berarti perangkat apa pun, dan 1 milik router) dan yang tertinggi, saya percaya adalah 255 (ini kebetulan adalah 11111111 dalam biner, angka terbesar yang dipegang oleh 1 byte).

Satu per satu, bekerja jalan Anda naik menuju 255. Akhirnya, Anda akan berhenti pada nomor yang benar yang memuat halaman MyNode Anda (atau halaman RaspiBlitz). Kemudian Anda akan tahu nomor apa yang harus dimasukkan dalam pengaturan jaringan Electrum Anda untuk terhubung ke node Anda.

Ini akan terlihat seperti ini (pastikan Anda menyertakan titik dua dan nomor setelahnya):

![image](assets/22.webp)

> Penting untuk diketahui bahwa alamat IP ini adalah INTERNAL untuk jaringan rumah Anda. Tidak ada orang di luar yang bisa melihatnya dan mereka tidak sensitif. Mereka seperti ekstensi telepon dalam organisasi besar yang mengarahkan Anda ke telepon yang berbeda.

## Hapus dompet palsu

Sekarang kita telah berhasil terhubung ke satu dan hanya satu node. Inilah cara Electrum akan dimuat secara default dari sekarang. Anda sekarang harus menghapus dompet palsu (Menu: file –> delete), jika Anda secara tidak sengaja mengirim dana ke dompet tidak aman ini (Ini tidak aman karena kita tidak membuatnya dengan cara yang aman).

## Buat dompet latihan

Setelah menghapus dompet palsu, mulai lagi dan buat yang baru, dengan cara yang sama, hanya kali ini, tulis kata-kata benih dan simpan dengan cukup aman.

Ini adalah ide yang baik untuk belajar bagaimana Electrum bekerja dengan dompet latihan ini, tanpa dompet keras yang merepotkan (diperlukan untuk keamanan tinggi). Hanya masukkan sejumlah kecil bitcoin ke dalam dompet ini – Anggap Anda akan kehilangan uang ini. Setelah mahir, kemudian pelajari cara menggunakan Electrum dengan dompet keras.

Di dompet baru yang Anda buat, Anda akan melihat daftar alamat. Yang hijau disebut "alamat penerima". Mereka adalah produk dari 3 hal:

- Frasa benih
- Frasa sandi
- Jalur derivasi

Dompet baru Anda memiliki satu set alamat penerima yang dapat secara matematis dan dapat direproduksi dibuat oleh dompet perangkat lunak apa pun yang memiliki benih, frasa sandi, dan jalur derivasi. Ada 4,3 miliar dari mereka! Lebih dari yang Anda butuhkan. Electrum hanya menunjukkan 20 pertama, dan kemudian lebih banyak saat Anda menggunakan yang pertama.
Informasi lebih lanjut tentang kunci privat Bitcoin dapat ditemukan dalam panduan ini.
![image](assets/23.webp)

Ini sangat berbeda dengan beberapa dompet lain yang hanya menampilkan 1 alamat pada satu waktu.

Karena Anda memasukkan frasa benih saat membuat dompet ini, Electrum memiliki kunci privat untuk setiap alamat, dan memungkinkan untuk melakukan pengeluaran dari alamat-alamat tersebut.

Perhatikan juga bahwa ada alamat-alamat kuning, yang disebut "alamat-alamat kembalian" – Ini hanyalah satu set alamat lain dari cabang matematika yang berbeda (ada 4,3 miliar lagi dari ini). Dompet menggunakan alamat-alamat ini untuk secara otomatis mengirimkan dana berlebih kembali ke dalam dompet sebagai kembalian. Misalnya, jika Anda mengambil 1,5 bitcoin dan menghabiskan 0,5 untuk pedagang, sisa 1,0 perlu ditempatkan di suatu tempat. Dompet Anda akan menghabiskannya ke alamat kembalian kuning kosong berikutnya – jika tidak, itu akan pergi ke penambang! Untuk informasi lebih lanjut tentang ini (UTXOs) lihat panduan ini. (https://armantheparman.com/utxo/)

Selanjutnya, kembali ke situs kunci privat Ian Colman dan masukkan benih (alih-alih menghasilkan satu). Anda akan melihat di bawah bahwa informasi kunci privat dan publik berubah; semuanya bergantung pada hal-hal di atas di halaman.

> Ingat, Anda seharusnya "tidak pernah" memasukkan benih pada komputer untuk dompet Bitcoin Anda yang sebenarnya – malware dapat mencurinya. Kita hanya menggunakan dompet latihan, untuk tujuan belajar, jadi tidak apa-apa untuk sekarang.

Gulir ke bawah dan ubah jalur derivasi menjadi BIP84 (segwit) untuk mencocokkan dompet Electrum Anda dengan mengklik tab BIP84.

![image](assets/24.webp)

Di bawah itu, Anda akan melihat kunci privat ekstensi akun dan kunci publik ekstensi akun:

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

Sekarang gulir ke bawah dan bandingkan alamat-alamatnya cocok dengan alamat-alamat kuning di Electrum

Mengapa kita melakukan semua ini?

Kita mengambil kata-kata benih dan memasukkannya melalui dua program perangkat lunak independen yang berbeda untuk memastikan mereka memberi kita informasi yang sama. Ini secara signifikan mengurangi risiko bahwa kode jahat bersembunyi di dalam dan memberi kita kunci privat atau publik palsu, atau alamat-alamat.

Langkah selanjutnya adalah menerima tes kecil dan menghabiskannya dalam dompet dari satu alamat ke alamat lain.

## Menguji Dompet (Belajar menggunakannya)

Di sini saya akan menunjukkan kepada Anda cara menerima UTXO ke dompet Anda dan kemudian memindahkannya (menghabiskannya) ke alamat lain dalam dompet. Ini adalah jumlah yang sangat kecil yang tidak akan kita keberatan kehilangan.

Ini memiliki sejumlah tujuan.

- Ini akan membuktikan bahwa Anda memiliki kekuatan untuk menghabiskan koin di dompet baru.
- Ini akan mendemonstrasikan cara menggunakan perangkat lunak Electrum untuk melakukan pengeluaran (dan beberapa fitur), sebelum kita menambahkan kompleksitas ekstra untuk keamanan (menggunakan dompet perangkat keras atau komputer yang tidak terhubung ke internet)
- Ini akan memperkuat ide bahwa Anda memiliki banyak alamat untuk dipilih untuk menerima dan menghabiskan, dalam dompet yang sama.
Buka dompet Electrum uji Anda dan klik tab Alamat, kemudian klik kanan pada alamat pertama dan pilih Salin –> Alamat:
![image](assets/30.webp)

Alamat sekarang berada dalam memori komputer Anda.

Sekarang pergi ke bursa tempat Anda memiliki beberapa bitcoin, dan mari kita tarik sejumlah kecil ke alamat ini, katakanlah 50.000 sats. Saya akan menggunakan Coinbase sebagai contoh karena ini adalah bursa yang paling sering digunakan, meskipun mereka adalah musuh dari Bitcoin, dan saya merasa jijik untuk masuk ke akun lama yang terlantar untuk tujuan ini.

Masuk, dan klik tombol Kirim/Terima, yang per hari ini berada di pojok kanan atas halaman web.

![image](assets/31.webp)

Saya jelas tidak memiliki dana dengan Coinbase, tetapi bayangkan saja ada dana di sini dan ikuti langkah berikut: Tempelkan alamat dari Electrum di bidang “Ke” seperti yang telah saya lakukan. Anda juga perlu memilih jumlah (saya sarankan sekitar 50.000 sats atau sejenisnya). Jangan memasukkan "pesan opsional" – Coinbase sudah mengumpulkan cukup banyak data Anda (dan menjualnya), tidak perlu membantu mereka. Akhirnya, klik “Lanjutkan”. Setelah itu saya tidak tahu pop-up apa lagi yang akan Anda dapatkan, Anda sendiri yang menentukan, tetapi metodenya serupa untuk semua bursa.

![image](assets/32.webp)

Tergantung pada bursa, Anda mungkin melihat sats di dompet Anda segera, atau beberapa penundaan jam/hari.

Perhatikan bahwa Electrum akan menunjukkan Anda menerima koin bahkan jika mereka belum dikonfirmasi di blockchain. Koin yang Anda miliki dibaca dari daftar tunggu Node Bitcoin, atau “mempool”. Ketika masuk ke blok, Anda akan melihat dana sebagai terkonfirmasi.

Sekarang setelah kita memiliki UTXO di dompet kita, kita harus memberi label padanya. Hanya kita yang bisa melihat label ini, ini tidak ada hubungannya dengan buku besar publik. Semua Label Electrum kita hanya terlihat di komputer yang kita gunakan. Kita sebenarnya bisa menyimpan file dan menggunakannya untuk mengembalikan semua label kita ke komputer lain yang menjalankan dompet yang sama.

### Membuat label untuk UTXO

Saya membutuhkan donasi ke dompet uji ini, terima kasih kepada @Sathoarder yang telah memberi saya UTXO langsung (10.000 sats), dan orang lain (anon) menyumbang ke alamat yang sama (5000 sats). Perhatikan ada 15.000 sats di saldo alamat pertama, dan total 2 transaksi (kolom paling kanan). Di bagian bawah, Saldo adalah 10.000 sats terkonfirmasi, dan 5.000 sats lainnya belum terkonfirmasi (masih di mempool).

![image](assets/33.webp)

Sekarang, jika kita menuju ke tab Koin, kita bisa melihat dua “koin yang diterima” atau UTXO. Keduanya berada di alamat yang sama.

![image](assets/34.webp)

Kembali ke tab alamat, jika Anda mengklik dua kali pada area “label” di sebelah alamat, Anda akan dapat memasukkan beberapa teks, kemudian tekan <enter> untuk menyimpan:

![image](assets/35.webp)

Ini adalah praktik yang baik sehingga Anda dapat melacak dari mana koin Anda berasal, apakah mereka bebas dari KYC atau tidak, dan berapa biaya setiap UTXO untuk Anda (dalam kasus Anda perlu menjual dan menghitung pajak yang akan diambil dari Anda oleh pemerintah Anda).
Idealnya, Anda seharusnya menghindari mengumpulkan banyak koin dalam satu alamat yang sama. Jika Anda memutuskan untuk melakukannya (sebaiknya tidak), Anda dapat memberi label pada setiap koin alih-alih memberi label yang sama pada semuanya dengan menggunakan metode alamat. Anda sebenarnya tidak bisa pergi ke tab "koin" dan mengedit label di sana (tidak, itu akan terlalu intuitif!). Anda harus pergi ke tab Riwayat, temukan transaksi, beri label pada itu, dan kemudian Anda akan melihat label di bagian koin. Semua label yang Anda lihat di bagian koin berasal dari label Alamat ATAU label riwayat, tetapi label riwayat apa pun menggantikan label alamat apa pun. Untuk mencadangkan label Anda ke dalam file, Anda dapat mengekspornya dari menu di atas, dompet–>label–>ekspor.

Selanjutnya, mari kita habiskan koin dari alamat pertama ke alamat kedua. Klik kanan pada alamat pertama dan pilih "habiskan dari" (Ini sebenarnya tidak perlu dalam skenario ini, tetapi bayangkan kita memiliki banyak koin di banyak alamat; dengan menggunakan fitur ini, kita dapat memaksa dompet untuk hanya menghabiskan koin yang kita inginkan. Jika kita ingin memilih beberapa koin di beberapa alamat, kita dapat memilih alamat dengan klik kiri sambil menahan tombol perintah, kemudian klik kanan, dan pilih "habiskan dari":

![image](assets/36.webp)

Setelah Anda melakukan itu, akan ada bar hijau di bagian bawah jendela dompet yang menunjukkan jumlah koin yang telah Anda pilih dan total yang tersedia untuk dihabiskan.

Anda juga dapat menghabiskan koin individu dalam satu alamat dan mengecualikan yang lain di alamat yang sama, tetapi ini tidak disarankan karena Anda meninggalkan koin di alamat yang telah dilemahkan secara kriptografis karena pengeluaran salah satu koin (alasan lain untuk tidak menaruh banyak koin dalam satu alamat, selain alasan privasi, adalah bahwa mengingat Anda seharusnya menghabiskan semuanya jika Anda menghabiskan satu, ini menjadi mahal secara tidak perlu). Begini cara memilih satu koin dari alamat bersama, tetapi jangan lakukan itu:

![image](assets/37.webp)

Sekarang, kita memiliki dua koin yang dipilih untuk dihabiskan. Selanjutnya, kita memutuskan kemana mengirimkannya. Mari kita kirim ke alamat kedua. Kita perlu menyalin alamat seperti ini:

![image](assets/38.webp)

Kemudian pergi ke tab "Kirim", dan tempel alamat kedua di bidang "bayar ke". Tidak perlu menambahkan deskripsi; Anda bisa, tetapi Anda dapat melakukannya nanti dengan mengedit label. Untuk jumlahnya, pilih "Max" untuk menghabiskan semua koin yang kita pilih. Kemudian klik "Bayar", dan kemudian klik tombol "lanjutan" pada pop-up yang muncul.

![image](assets/39.webp)

Selalu klik "lanjutan" pada tahap ini agar kita bisa mendapatkan kontrol yang lebih baik dan memeriksa secara tepat apa yang ada dalam transaksi. Berikut adalah transaksinya:

![image](assets/40.webp)

Kita melihat dua kotak/jendela putih internal. Yang atas adalah jendela input (koin mana yang dihabiskan), dan yang bawah adalah output (kemana koin itu pergi).

Perhatikan, status (kiri atas) adalah "belum ditandatangani" untuk saat ini. "Jumlah yang dikirim" adalah 0 karena koin sedang ditransfer dalam dompet. Biayanya adalah 481 sats. Perhatikan bahwa jika itu adalah 480 sats, nol terakhir akan dihilangkan, seperti ini, 0.0000048 dan bagi mata yang lelah, ini bisa terlihat seperti 48 sats – berhati-hatilah (sesuatu yang seharusnya diperbaiki oleh pengembang Electrum).
Ukuran transaksi merujuk pada ukuran data dalam byte, bukan jumlah bitcoin. "Ganti dengan biaya" diaktifkan secara default, dan ini memungkinkan Anda untuk mengirim ulang transaksi dengan biaya yang lebih tinggi jika diperlukan. LockTime memungkinkan Anda untuk menyesuaikan kapan transaksi tersebut valid - Saya belum mencoba itu, tetapi menyarankan agar tidak menggunakannya kecuali Anda benar-benar memahami apa yang Anda lakukan dan telah berlatih dengan jumlah kecil.

Di bagian bawah, kita memiliki beberapa alat penyesuaian biaya penambangan yang canggih. Yang perlu Anda lakukan untuk transfer internal adalah mengaturnya ke biaya minimum 1 sat/byte. Cukup ketikkan angka tersebut secara manual di kolom Target fee. Untuk memeriksa biaya yang sesuai untuk pembayaran eksternal, Anda dapat berkonsultasi dengan https://mempool.space untuk melihat seberapa sibuk mempool tersebut, dan beberapa biaya yang disarankan ditampilkan.

![image](assets/41.webp)

Saya telah memilih 1 sat/byte.

Di jendela input, kita melihat dua entri. Yang pertama adalah donasi 5000 sat. Kita lihat di sebelah kiri hash transaksinya (yang bisa kita cari di blockchain). Di sebelahnya, ada "21" - ini menunjukkan bahwa itu adalah output yang diberi label 21 dalam transaksi tersebut (sebenarnya output ke-22 karena yang pertama diberi label nol).

Hal yang perlu diperhatikan di sini: UTXO hanya ada di dalam sebuah transaksi. Untuk menghabiskan UTXO kita harus merujuknya, dan memasukkan referensi tersebut ke dalam input dari transaksi baru. Output kemudian menjadi UTXO baru dan UTXO lama menjadi STXO (Spent transaction output).

Baris kedua adalah donasi 10.000 sat. Ada "0" di sebelah hash transaksi dari mana asalnya karena itu adalah output pertama (dan mungkin satu-satunya) untuk transaksi tersebut.

Di jendela bawah, kita melihat alamat kita. Perhatikan total bitcoin dari input tidak cukup cocok dengan total output. Perbedaannya menjadi milik penambang. Penambang melihat perbedaan dalam semua transaksi di blok yang sedang dicoba ditambang, dan menambahkan angka tersebut ke dalam hadiahnya. (Biaya penambangan dengan cara ini sepenuhnya terputus dari rantai transaksi dan memulai kehidupan baru).

Jika kita menyesuaikan biaya penambangan, nilai output akan secara otomatis berubah.

> Penting untuk diperhatikan di sini: Perhatikan warna alamat di jendela transaksi. Ingat bahwa alamat hijau terdaftar di tab alamat Anda. Jika sebuah alamat disorot hijau (atau kuning) di jendela transaksi, maka Electrum telah mengenali alamat tersebut sebagai miliknya. Jika alamat tidak memiliki sorotan, maka itu adalah alamat eksternal (eksternal ke dompet yang saat ini terbuka), dan Anda harus memeriksanya dengan lebih hati-hati.

Setelah Anda memeriksa semua dalam transaksi dan yakin Anda senang dengan koin mana yang Anda belanjakan, dan kemana koin tersebut akan pergi, Anda dapat klik "finalise."

![image](assets/42.webp)

Setelah Anda klik "finalise", Anda tidak dapat lagi melakukan pengeditan - Jika Anda perlu, Anda harus menutup ini dan memulai lagi. Perhatikan tombol "finalise" telah berubah menjadi "export", dan tombol baru muncul: "save", "combine", "sign" dan "broadcast". Tombol "broadcast" tidak aktif karena transaksi belum ditandatangani dan sehingga tidak valid pada tahap ini.

Setelah Anda klik sign, jika Anda memiliki password untuk dompet Anda akan diminta untuk itu, dan kemudian status (kanan atas) akan berubah dari "Unsigned" menjadi "Signed". Kemudian tombol "Broadcast" akan tersedia.
Setelah Anda menyiarkan, Anda dapat menutup jendela transaksi. Jika Anda pergi ke tab alamat, Anda akan melihat alamat pertama kosong, dan alamat kedua memiliki 1 UTXO.
Catatan: Anda akan melihat semua perubahan ini bahkan sebelum transaksi ditambang ke dalam blok, atau "dikonfirmasi". Ini karena Electrum memperbarui saldo/transaksi berdasarkan tidak hanya data blockchain, tetapi juga data mempool. Tidak semua dompet melakukan ini.

Satu hal yang perlu diperhatikan adalah bahwa alih-alih menyiarkan, kita dapat menyimpan transaksi untuk nanti. Transaksi dapat disimpan baik dalam keadaan belum ditandatangani maupun sudah ditandatangani.

Klik tombol "export" (paradoksnya, JANGAN klik tombol "save"), dan Anda akan melihat beberapa opsi. Transaksi dikodekan dengan teks, dan oleh karena itu dapat disimpan dalam beberapa cara.

![image](assets/43.webp)

Menyimpan ke kode QR sangat menarik. Jika Anda memilih ini, sebuah QR akan muncul:

![image](assets/44.webp)

Anda kemudian dapat mengambil foto kode QR tersebut. Ada beberapa hal yang dapat Anda lakukan dengan ini, tetapi untuk sekarang, mari kita katakan Anda memuatnya kembali ke dalam dompet nanti. Anda dapat menutup Electrum, memuat dompet lagi, dan pergi ke menu Tools:

![image](assets/45.webp)

Ini akan memuat kamera komputer Anda. Anda kemudian menunjukkan kamera foto kode QR di ponsel Anda, dan ini akan memuat transaksi kembali, persis seperti Anda tinggalkan.

Tidak intuitif bagaimana cara memuat transaksi yang disimpan, jadi perhatikan khusus. Memuat transaksi bukanlah "tool" tetapi opsi tersebut tersembunyi di menu tools (hal lain yang harus diperbaiki oleh pengembang Electrum).

Proses serupa dimungkinkan dengan transaksi yang disimpan sebagai file. Cobalah berlatih dengan salah satu metode, dalam dompet yang sama. Saya tidak akan membahasnya di sini tetapi Anda dapat menggunakan fitur ini untuk memindahkan transaksi antara dompet yang sama di komputer yang berbeda, antara dompet multisignature, dan ke dan dari dompet hardware. Berikut adalah beberapa instruksi.

Sekarang, kembali ke tombol "save" – ini bukan cara untuk menyimpan teks transaksi. Yang sebenarnya dilakukan adalah memberitahu dompet Electrum untuk mengenali transaksi ini di komputer lokal sebagai pembayaran yang diajukan. Jika Anda melakukannya secara tidak sengaja, Anda akan melihat transaksi dengan ikon komputer kecil. Anda dapat klik kanan dan menghapus transaksi – jangan khawatir, Anda tidak dapat menghapus bitcoin dengan cara ini. Electrum kemudian akan melupakan bahwa transaksi ini pernah terjadi, dan akan "mengembalikan" sats kembali dan menampilkan sats di lokasi yang benar di mana mereka sebenarnya ada.

### Alamat Perubahan

Alamat perubahan itu menarik. Anda perlu memahami UTXO untuk memahami penjelasan ini. Jika Anda menghabiskan ke alamat jumlah yang lebih kecil dari UTXO, maka bitcoin yang tersisa akan pergi ke penambang kecuali output perubahan ditentukan.

Anda mungkin memiliki UTXO bitcoin 6.15 dan ingin menghabiskan 0.15 bitcoin untuk mendonasikan kepada beberapa pengunjuk rasa yang tertindas oleh pemerintah "demokratis" tirani di suatu tempat di dunia. Anda kemudian akan mengambil 6.15 bitcoin (menggunakan fungsi "spend from" di Electrum), dan memasukkannya dalam sebuah transaksi.

Anda akan menempelkan alamat para pengunjuk rasa di bidang "pay to", mungkin Anda akan menempatkan "EndTheFed & WEF" di bidang "description", dan untuk jumlahnya, Anda akan memasukkan 0.15 bitcoin dan klik "pay", lalu "advanced".
Di layar transaksi, untuk jendela input, Anda akan melihat UTXO bitcoin sebesar 6.15. Untuk jendela output, Anda akan melihat sebuah alamat tanpa penyorotan (ini adalah alamat para pengunjuk rasa) dengan 0.15 bitcoin di sampingnya. Anda juga akan melihat alamat berwarna kuning dengan jumlah bitcoin sedikit kurang dari 6.0. Ini adalah alamat kembalian yang secara otomatis dipilih oleh dompet dari salah satu alamat kembalian kuning miliknya. Tujuan dari alamat kembalian adalah agar dompet dapat menaruh koin kembalian di dalamnya tanpa mengacaukan ketersediaan alamat penerima yang mungkin Anda rencanakan untuk digunakan, atau telah mengirimkan faktur untuknya. Jika mereka akan digunakan nanti oleh pelanggan, misalnya, Anda tidak ingin dompet Anda secara otomatis menggunakannya dan mengisinya. Ini berantakan dan buruk untuk privasi.
Perhatikan bahwa saat Anda menyesuaikan biaya penambangan, jumlah output kembalian akan secara otomatis menyesuaikan, bukan jumlah pembayaran.

### Perubahan manual atau bayar ke banyak

Ini adalah fitur yang sangat menarik dari Electrum. Anda mengaksesnya seperti ini.

![image](assets/46.webp)

Anda kemudian dapat memasukkan beberapa tujuan untuk saldo UTXO yang Anda belanjakan, seperti ini:

![image](assets/47.webp)

Tempel alamatnya, ketik koma, lalu spasi, lalu jumlahnya, lalu <enter>, lalu lakukan lagi. JANGAN MEMASUKKAN JUMLAH DALAM JENDELA “JUMLAH” – Electrum akan mengisi total di sini saat Anda mengetik jumlah individu di jendela “Bayar ke”.

Ini memungkinkan Anda untuk secara manual menentukan kemana kembalian pergi (misalnya alamat tertentu di dompet Anda, atau dompet lain), atau Anda dapat membayar banyak orang sekaligus. Jika total Anda tidak cukup tinggi untuk mencocokkan ukuran UTXO, Electrum masih akan membuat output kembalian tambahan untuk Anda.

Fitur Bayar ke Banyak juga memungkinkan kemungkinan untuk membuat "PayJoins" atau "CoinJoins" Anda sendiri – di luar cakupan artikel ini, tetapi saya memiliki panduan di sini. (https://armantheparman.com/cj/)

## Dompet

Saya ingin mendemonstrasikan Dompet Hanya Menonton menggunakan Electrum. Untuk melakukan itu, saya perlu pertama-tama mendefinisikan “dompet”. Ada dua cara “dompet” digunakan dalam Bitcoin:

- Tipe A, “dompet” – merujuk pada perangkat lunak yang menunjukkan alamat dan saldo Anda, misalnya Electrum, Blue Wallet, Sparrow Wallet, dll.

- Tipe B, “dompet” – merujuk pada kumpulan alamat unik yang terkait dengan kombinasi dari seed_phrase/passphrase/derivation_path kita. Ada 8,6 miliar alamat dalam setiap dompet (4,3 miliar alamat penerima, dan 4,3 miliar alamat kembalian). Jika Anda mengubah sesuatu dalam seed phrase, passphrase, atau derivation path, Anda mendapatkan dompet yang belum digunakan dengan 8,6 miliar alamat kosong baru, dan semua unik.

Tipe mana yang dimaksud seseorang saat menggunakan kata “dompet” jelas dalam konteks.

## Dompet Hanya Menonton – sebuah latihan

Tidak sepenuhnya jelas apa guna dompet hanya menonton, tetapi saya akan mulai dengan menjelaskan apa itu, bagaimana membuat satu untuk latihan, dan kemudian kita akan kembali ke tujuannya nanti saat saya menjelaskan lebih lanjut tentang dompet perangkat keras. (Untuk ulasan mendalam tentang cara menggunakan dompet perangkat keras, dan berbagai merek spesifik, lihat di sini.)
Kita akan membuat dompet reguler dummy (kali ini menambahkan sedikit lebih kompleksitas dengan passphrase), dan kemudian dompet pengamatannya. Jika Anda mau, Anda bisa menyalin yang saya buat persis, atau membuat milik Anda sendiri – dompet ini akan dibuang; jangan benar-benar menggunakannya. Mulailah dengan menghasilkan seed 12 kata menggunakan situs web Ian Coleman.
Perhatikan 12 kata acak di tangkapan layar di bawah ini, dan bahwa saya telah memasukkan passphrase di bidang passphrase:

PASSPHRASE: “Craig Wright adalah pembohong dan penipu dan layak berada di penjara. Juga, Ross Ulbricht seharusnya dibebaskan dari penjara segera.”

Passphrase bisa sampai 100 karakter panjangnya, dan idealnya harus tidak ambigu dan tidak terlalu pendek – Yang saya gunakan hanya untuk bersenang-senang – Saya umumnya menyarankan menghindari huruf besar dan simbol hanya untuk mengurangi stres Anda dalam mencoba kombinasi jika Anda pernah memiliki masalah dengan mengingat passphrase Anda.

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

Anda juga akan melihat “BIP32 extended private/public” keys – ini untuk diabaikan untuk saat ini.

Kunci privat diperluas akun dapat digunakan untuk sepenuhnya meregenerasi dompet Anda. Kunci publik diperluas akun, bagaimanapun, hanya dapat menghasilkan versi terbatas dari dompet yang sama (dompet pengamat) – Jika Anda memasukkan kunci ini di Electrum, itu masih akan menghasilkan semua 8,6 miliar alamat yang akan dihasilkan oleh seed atau kunci privat diperluas, tetapi tidak akan ada kunci privat yang tersedia untuk Electrum, jadi tidak ada pengeluaran yang mungkin. Mari kita lakukan sekarang untuk menunjukkan poinnya:

Salin “account extended public key” ke clipboard.

Kemudian pergi ke Electrum, biarkan dompet yang kita buat terbuka, dan pergi ke file–>new/restore. Proses membuat dompet sedikit berbeda dari sebelumnya:

- Standard wallet
- Use a master key
- Tempel kunci publik diperluas di kotak dan lanjutkan
- Tidak perlu memasukkan passphrase; itu sudah bagian dari kunci publik diperluas
- Tidak perlu memasukkan semantik skrip dan jalur derivasi
- Tidak perlu menambahkan password (mengunci dompet)

Ketika dompet dimuat, Anda seharusnya memperhatikan bahwa alamat yang sama persis dimuat seperti sebelumnya ketika seed dimasukkan. Anda juga seharusnya memperhatikan di bagian atas di bilah judul, tertulis “watching wallet”. Dompet ini dapat menunjukkan kepada Anda alamat Anda, dan saldo (dengan memeriksa saldo melalui node), tetapi Anda tidak dapat MENANDATANGANI transaksi (karena dompet pengamat tidak memiliki kunci privat).
Lalu apa gunanya?

Salah satu alasan, dan bukan alasan utama, adalah Anda dapat mengamati dompet dan saldo Anda di komputer tanpa mengungkapkan kunci privat Anda kepada malware apa pun di komputer tersebut.

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
Jika Anda mendapatkan pesan "group plugdev" sudah ada, itu tidak masalah, lanjutkan saja. Setelah perintah kedua, Anda tidak akan mendapatkan umpan balik/balasan, langsung saja lanjutkan ke perintah ketiga.
Anda mungkin perlu memutuskan dan kemudian menyambungkan kembali ColdCard ke komputer.

Jika setelah semua ini Anda masih tidak dapat menyambungkan ColdCard, saya akan mencoba memperbarui firmware (panduan segera, tapi untuk saat ini, Anda dapat menemukan instruksi di situs web produsen).

Selanjutnya, buat dompet baru:

- Dompet standar
- Gunakan perangkat keras
- Ini akan memindai dan mendeteksi ColdCard Anda. Lanjutkan.
- Pilih semantik skrip dan jalur derivasi
- Putuskan apakah file dompet harus dienkripsi (disarankan)

### Transaksi menggunakan ColdCard

Dengan kabel terhubung, transaksi menjadi mudah. Menandatangani transaksi akan lancar.

Jika menggunakan perangkat dalam cara yang terisolasi dari jaringan, Anda harus secara manual memindahkan transaksi yang disimpan antar perangkat menggunakan kartu microSD. Ada beberapa trik.

Setelah membuat transaksi dan menyelesaikannya, Anda perlu mengklik tombol ekspor di sudut kiri bawah. Anda akan melihat "simpan ke file" yang secara kontraintuitif, bukan yang kita inginkan. Anda sebenarnya harus terlebih dahulu pergi ke opsi menu terakhir yang mengatakan "untuk dompet perangkat keras", dan kemudian, dari dalam pilihan itu, temukan "simpan ke file" lainnya dan pilih itu. Kemudian simpan file ke microSD, keluarkan kartu dan masukkan ke ColdCard. Ingat bahwa Anda mungkin perlu menerapkan passphrase untuk memilih dompet yang benar. Layar akan mengatakan siap untuk menandatangani. Klik tanda centang, periksa transaksi, dan lanjutkan dengan mengonfirmasi dengan tanda centang. Setelah selesai, keluarkan kartu, dan masukkan kembali ke komputer.

Kemudian kita perlu membuka transaksi menggunakan electrum. Fungsinya tersembunyi di menu alat –> muat transaksi. Navigasikan sistem file dan temukan file tersebut. Akan ada tiga file setiap kali Anda menandatangani. File asli yang disimpan oleh Watching Wallet, dan dua yang dibuat oleh ColdCard (saya tidak tahu mengapa ini terjadi). Satu akan mengatakan "ditandatangani" dan satu akan mengatakan "final". Ini tidak intuitif tetapi yang "ditandatangani" tidak berguna, kita perlu membuka transaksi "final".

Setelah Anda memuat itu, Anda dapat mengklik "siarkan" dan pembayaran akan dilakukan.

## Memperbarui Electrum dan Direktori Tersembunyi ".electrum"

Electrum berada di komputer Anda di dua tempat. Ada aplikasinya sendiri, dan ada folder konfigurasi tersembunyi. Folder tersebut berada di tempat yang berbeda tergantung pada sistem operasi Anda:

Windows:

> C:/Users/nama_pengguna_anda_di_sini/AppData/Roaming/Electrum

Mac:

> /Users/nama_pengguna_anda_di_sini/.electrum

Linux:

> /home/nama_pengguna_anda_di_sini/.electrum

Perhatikan bahwa “.” sebelum “electrum” di Linux dan Mac – itu menunjukkan direktori tersebut tersembunyi. Juga, perhatikan bahwa direktori ini hanya dibuat (secara otomatis) setelah Anda menjalankan Electrum untuk pertama kalinya. Direktori berisi file konfigurasi electrum dan juga direktori yang menyimpan dompet yang telah Anda simpan.

Jika Anda menghapus program Electrum dari komputer Anda, direktori tersembunyi akan tetap ada, kecuali Anda secara aktif menghapus itu juga.
Untuk meningkatkan Electrum, Anda mengikuti prosedur yang sama seperti yang saya jelaskan di awal untuk mengunduh dan memverifikasi. Anda kemudian akan memiliki dua salinan program di komputer Anda, dan Anda dapat menjalankan salah satu dari mereka – setiap program akan mengakses folder electrum tersembunyi yang sama untuk konfigurasi dan akses dompetnya. Semua hal yang kita simpan, seperti unit dasar, node default untuk terhubung, preferensi lainnya, dan akses ke dompet, akan tetap ada karena semua itu disimpan di folder tersebut.
### Memindahkan Electrum dan Dompet Anda ke komputer lain

Untuk melakukan ini, Anda dapat menyalin file program ke drive USB, dan juga menyalin direktori .electrum. Kemudian salin atau pindahkan ke komputer baru. Anda tidak perlu memverifikasi program lagi. Pastikan untuk menyalin direktori .electrum ke lokasi default (ingat untuk menyalinnya SEBELUM menjalankan Electrum untuk pertama kalinya di komputer tersebut, jika tidak, folder .electrum default yang kosong akan terisi, dan Anda mungkin akan bingung).

## Label

Seperti yang saya jelaskan sebelumnya, pada tab alamat, ada kolom label. Anda dapat mengklik dua kali di sana dan memasukkan catatan untuk diri Anda sendiri (hanya di komputer Anda, tidak publik, dan tidak di blockchain).

![image](assets/54.webp)

Ketika memindahkan dompet Electrum Anda ke komputer lain, Anda mungkin tidak ingin kehilangan semua catatan ini. Anda dapat mencadangkannya ke file menggunakan menu, dompet–> label –> ekspor, dan kemudian di komputer baru, gunakan dompet–>label–>impor.

## Tips:

Jika Anda merasa sumber daya ini berguna, dan Anda ingin mendukung apa yang saya lakukan untuk Bitcoin, Anda dapat menyumbangkan beberapa sats di sini:

Alamat Lightning Statis: dandysack84@walletofsatoshi.com
https://armantheparman.com/electrum/