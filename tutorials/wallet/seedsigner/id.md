---
name: SeedSigner
description: Perangkat keras wallet yang dibuat sendiri, tanpa status, terjangkau, dan sepenuhnya memiliki celah udara
---

![cover](assets/cover.webp)



SeedSigner adalah perangkat keras wallet Bitcoin sumber terbuka yang dapat dibuat sendiri oleh siapa saja dengan menggunakan komponen elektronik serba guna yang murah. Tidak seperti produk komersial seperti Ledger, Coldcard atau Trezor, ini bukanlah perangkat siap pakai yang diproduksi oleh perusahaan: ini adalah proyek komunitas yang memungkinkan siapa pun untuk membuat perangkat mereka sendiri, mengendalikan setiap langkah.



SeedSigner dirancang untuk menjadi 100% ***air-gapped***: tidak pernah terhubung ke Internet, tidak memiliki Wi-Fi atau Bluetooth (dalam kasus Raspberry Pi Zero v1.3) dan tidak pernah terhubung ke komputer untuk bertukar data. Komunikasi secara eksklusif melalui sistem pertukaran kode QR. Secara konkret, perangkat lunak manajemen portofolio Anda (seperti Sparrow Wallet) menampilkan transaksi yang akan ditandatangani dalam bentuk kode QR; Anda memindainya dengan kamera SeedSigner, kemudian perangkat menandatangani transaksi menggunakan kunci pribadi Anda yang disimpan sementara di RAM-nya. Terakhir, alat ini menghasilkan kode QR yang berisi transaksi yang telah ditandatangani, yang Anda pindai dengan perangkat lunak Anda untuk mengirimkannya ke jaringan Bitcoin.



![Image](assets/fr/001.webp)



SeedSigner juga tidak memiliki status. Dengan kata lain, ia tidak menyimpan seed atau kunci pribadi Anda secara permanen, tidak seperti dompet perangkat keras lainnya. Setiap kali Anda melakukan reboot, memorinya benar-benar kosong, kecuali jika Anda mengonfigurasi perangkat untuk menyimpan pengaturan Anda pada kartu microSD. Oleh karena itu, Anda harus memasukkan kembali seed Anda setiap kali Anda menggunakannya, metode yang paling praktis adalah menyimpannya dalam bentuk kode QR, yang akan dipindai pada saat memulai menggunakan kamera SeedSigner. Mode operasi ini sangat mengurangi permukaan serangan: bahkan jika pencuri mencuri perangkat Anda, dia tidak akan menemukan informasi apa pun di dalamnya, karena selalu kosong secara default.



Pilihan lain untuk menyimpan seed Anda dan menggunakannya dengan SeedSigner adalah dengan menggunakan kartu pintar *SeedKeeper* bersama dengan pembaca yang kompatibel. Hal ini memberikan Anda sebuah *Secure Element* yang sangat kuat untuk menyimpan seed Anda, sambil menggunakan layar SeedSigner untuk menandatangani transaksi. Tetapi konfigurasi khusus ini adalah subjek dari tutorial khusus lainnya. Di sini, kita akan berkonsentrasi pada penggunaan dasar SeedSigner:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

Proyek SeedSigner menempati tempat yang penting dalam ekosistem Bitcoin, karena menawarkan kepada semua orang, di mana pun di dunia, kemungkinan untuk mendapatkan keuntungan dari keamanan tingkat lanjut untuk melindungi bitcoin mereka. Keuntungan utamanya terletak pada aksesibilitasnya: perangkat keras yang dibutuhkan dapat dibeli dengan harga kurang dari $50. Terlebih lagi, ini memungkinkan orang-orang yang tinggal di negara-negara terbatas untuk membangun perangkat keras wallet mereka sendiri dari komponen komputer standar, yang mudah ditemukan dan tidak terlalu tunduk pada batasan peraturan.



Tetapi bahkan di luar konteks khusus ini, SeedSigner dapat menjadi opsi yang menarik untuk Anda: ini adalah sumber terbuka, bekerja tanpa batas negara dan tanpa celah udara, dan mengurangi vektor serangan yang terkait dengan rantai pasokan perangkat keras wallet Anda.



## 1. Peralatan yang diperlukan



Untuk membangun SeedSigner Anda, Anda memerlukan komponen-komponen berikut ini:





- Raspberry Pi Nol
    - Versi 1.3 direkomendasikan, karena tidak memiliki Wi-Fi maupun Bluetooth, sehingga memastikan isolasi yang lengkap.
 - Versi W dan v2 juga kompatibel, tetapi menyertakan chip Wi-Fi/Bluetooth. Oleh karena itu, disarankan untuk menonaktifkannya secara fisik dengan melepaskan modul radio dari kartu. Pengoperasiannya relatif sederhana, tetapi membutuhkan ketelitian (tang halus cukup untuk Zero W, sedangkan untuk v2 diperlukan pena panas untuk melepaskan pelat logam yang menyembunyikan modul). Saya tidak akan membahas secara rinci dalam tutorial ini, tetapi Anda akan menemukan semua instruksi dalam dokumen ini: *[Menonaktifkan WiFi/Bluetooth dengan perangkat keras](https://github.com/DesobedienteTecnologico/rpi_disable_wifi_and_bt_by_hardware)*.
 - Harap diperhatikan: beberapa model Raspberry Pi Zero dijual tanpa pin GPIO yang sudah disolder. Anda bisa membeli versi dengan pin terintegrasi secara langsung (solusi paling sederhana), atau membeli pin secara terpisah dan menyoldernya sendiri (solusi yang lebih kompleks).
 - Jangan lupa menyertakan catu daya micro-USB.



![Image](assets/fr/002.webp)





- Layar Waveshare 1,3 inci (240×240 piksel)** (dalam bahasa Prancis)
    - Sangat penting untuk memilih model khusus ini: ada layar lain yang serupa, tetapi dengan resolusi yang berbeda. Tanpa definisi 240×240 px, layar tidak akan dapat digunakan.
    - Layarnya dilengkapi tiga tombol dan joystick mini untuk antarmuka pengguna.



![Image](assets/fr/003.webp)





- Kamera yang kompatibel dengan Raspberry Pi Zero**
    - Opsi 1: kamera standar dengan alas emas lebar (periksa kompatibilitasnya dengan housing Anda).
    - Opsi 2: kamera "*Zero*" yang lebih ringkas, yang didesain khusus untuk Pi Zero.



![Image](assets/fr/004.webp)





- Kartu MicroSD**
    - Kapasitas yang disarankan: antara 4 dan 32 GB.





- Housing (opsional tetapi disarankan)** (opsional tetapi disarankan)** (opsional tetapi disarankan)** (opsional tetapi disarankan)**)
    - Melindungi perangkat dan membuatnya mudah digunakan.
    - Model yang paling populer adalah "*Orange Pill Case*", yang mana [file STL sumber terbuka tersedia untuk pencetakan 3D](https://github.com/SeedSigner/seedsigner/tree/dev/enclosureshttps://github.com/SeedSigner/seedsigner/tree/dev/enclosures).
    - Kotak juga tersedia dari [pengecer independen yang terhubung dengan proyek](https://seedsigner.com/hardware/).



![Image](assets/fr/005.webp)



Anda bisa membeli komponen-komponen ini secara terpisah atau, untuk lebih mudahnya, pilihlah paket yang sudah jadi yang sudah termasuk semua perangkat keras yang diperlukan. Secara pribadi, saya memesan paket saya [di situs Perancis ini](https://bitcoinbazar.fr/), tetapi Anda juga akan menemukan daftar vendor untuk setiap wilayah di dunia pada [halaman perangkat keras proyek SeedSigner](https://seedsigner.com/hardware/). Jika Anda lebih suka membeli komponen secara terpisah, komponen-komponen tersebut tersedia di platform e-commerce utama atau di toko-toko spesialis.



## 2. Mempersiapkan perangkat lunak



Setelah Anda menyiapkan perangkat keras, Anda perlu menyiapkan kartu microSD dengan menginstal sistem SeedSigner di dalamnya. Untuk melakukan ini, buka komputer pribadi Anda sehari-hari, dan colokkan microSD yang ditujukan untuk SeedSigner.



### 2.1. Unduh



Buka [repositori GitHub resmi proyek](https://github.com/SeedSigner/seedsigner/releases). Pada versi terbaru perangkat lunak, unduh file :




- Gambar `.img` yang sesuai dengan model Pi Anda.
- File `.sha256.txt`.
- File `.sha256.txt.sig`.



![Image](assets/fr/006.webp)



Sebelum memulai instalasi, mari kita periksa perangkat lunaknya.



### 2.2 Verifikasi di Linux dan macOS



Mulailah dengan mengimpor kunci publik resmi dari proyek SeedSigner langsung dari Keybase :



```
gpg --fetch-keys https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/007.webp)



Terminal akan memberitahukan Anda bahwa sebuah kunci telah diimpor atau diperbarui. Selanjutnya, jalankan perintah verifikasi pada file tanda tangan (ingatlah untuk memodifikasi perintah sesuai dengan versi Anda, di sini `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/008.webp)



Jika semuanya sudah benar, keluarannya akan berbunyi `Tanda tangan yang baik`. Ini berarti bahwa file `.sha256.txt` telah ditandatangani oleh kunci yang baru saja Anda impor, dan tanda tangan tersebut valid. Abaikan pesan peringatan `WARNING: This key is not certified with a trusted signature`: ini normal, karena sekarang terserah Anda untuk memeriksa apakah kunci yang digunakan adalah milik proyek SeedSigner.



Untuk melakukan hal ini, bandingkan 16 karakter terakhir dari sidik jari yang ditampilkan dengan yang tersedia di [Keybase.io/SeedSigner](https://keybase.io/seedsigner), di [Twitter resmi](https://twitter.com/SeedSigner/status/1530555252373704707), atau di file yang dipublikasikan di [SeedSigner.com](https://seedsigner.com/keybase.txt). Jika pengidentifikasi ini sama persis, Anda dapat yakin bahwa kuncinya memang berasal dari proyek tersebut. Jika ragu, segera hentikan dan mintalah bantuan kepada komunitas SeedSigner (Telegram, X, GitHub...).



Ketika kunci telah divalidasi, Anda dapat memeriksa bahwa gambar yang diunduh belum dimodifikasi (ingatlah untuk memodifikasi perintah sesuai dengan versi Anda, di sini `0.8.6.`):



```
shasum -a 256 --ignore-missing --check seedsigner.0.8.6.sha256.txt
```



![Image](assets/fr/009.webp)





- Pada Linux, perintah ini sudah tersedia secara bawaan.
- Peringatan: versi macOS sebelum `Big Sur (11)` tidak mengenali opsi `--abaikan-kehilangan`. Dalam kasus ini, hapus dan abaikan peringatan tentang file yang hilang.



Hasil yang diharapkan adalah `OK` di samping file `.img`. Ini mengonfirmasi bahwa gambar yang diunggah identik dengan gambar yang diterbitkan oleh proyek dan belum dimodifikasi.



### 2.3 Verifikasi Windows



Pada Windows, prosedurnya serupa tetapi perintahnya berbeda. Mulailah dengan menginstal [Gpg4win](https://www.gpg4win.org/) dan buka aplikasi *Kleopatra*. Impor kunci publik dari proyek SeedSigner dari URL Keybase :



```
https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/010.webp)



Selanjutnya, buka PowerShell di folder tempat file yang telah diunduh berada (`Shift` + klik kanan > `Buka PowerShell di sini`). Jalankan perintah berikut untuk memeriksa tanda tangan manifes (ingatlah untuk memodifikasi perintah sesuai dengan versi Anda, di sini `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/011.webp)



Jika semuanya sudah benar, keluarannya akan berbunyi `Tanda tangan yang baik`. Ini berarti bahwa file `.sha256.txt` telah ditandatangani oleh kunci yang baru saja Anda impor, dan tanda tangan tersebut valid. Abaikan pesan peringatan `WARNING: This key is not certified with a trusted signature`: ini normal, karena sekarang terserah Anda untuk memeriksa apakah kunci yang digunakan adalah milik proyek SeedSigner.



Untuk melakukan hal ini, bandingkan 16 karakter terakhir dari sidik jari yang ditampilkan dengan yang tersedia di [Keybase.io/SeedSigner](https://keybase.io/seedsigner), di [Twitter resmi](https://twitter.com/SeedSigner/status/1530555252373704707), atau di file yang dipublikasikan di [SeedSigner.com](https://seedsigner.com/keybase.txt). Jika pengidentifikasi ini sama persis, Anda dapat yakin bahwa kuncinya memang berasal dari proyek tersebut. Jika ragu, segera hentikan dan mintalah bantuan kepada komunitas SeedSigner (Telegram, X, GitHub...).



Setelah kunci divalidasi, Anda perlu memeriksa bahwa file gambar belum rusak. Untuk melakukan hal ini, gunakan perintah berikut ini di PowerShell:



```
CertUtil -hashfile seedsigner_os.0.8.6.[your-Pi-model].img SHA256
```



Contoh untuk Raspberry Pi Zero 2 (ingatlah untuk memodifikasi perintah sesuai dengan versi Anda, di sini `0.8.6.`):



```
CertUtil -hashfile seedsigner_os.0.8.6.pi02w.img SHA256
```



![Image](assets/fr/012.webp)



PowerShell kemudian menghitung hash SHA256 dari file gambar Anda. Bandingkan hash ini dengan nilai yang sesuai di `seedsigner.0.8.6.sha256.txt`.




- Jika kedua nilai tersebut sama persis, pemeriksaan berhasil dan Anda dapat melanjutkan.
- Jika berbeda, berarti file tersebut rusak atau rusak. Jangan gunakan file tersebut, dan mulai mengunduh lagi.



![Image](assets/fr/013.webp)



Verifikasi yang berhasil menjamin bahwa berkas `.img` Anda adalah asli (ditandatangani oleh SeedSigner) dan tidak diubah (tidak dimodifikasi). Anda dapat melanjutkan ke langkah berikutnya dengan aman.



### 2.4. Mem-flash gambar



Jika Anda belum memilikinya, unduh perangkat lunak [Balena Etcher](https://etcher.balena.io/), kemudian :




- Masukkan kartu microSD ke dalam komputer Anda.
- Luncurkan Etcher.
- Pilih file `.img` yang telah diunduh dan diverifikasi.
- Pilih kartu microSD sebagai target.
- Klik `Flash!`.



![Image](assets/fr/014.webp)



Tunggu sampai proses selesai: microSD Anda siap digunakan. Sekarang saatnya untuk perakitan!



## 3. Perakitan SeedSigner



Setelah kartu microSD Anda disiapkan dan di-flash dengan perangkat lunak SeedSigner, Anda dapat melanjutkan dengan perakitan akhir. Luangkan waktu Anda, karena beberapa bagiannya rapuh (terutama taplak meja, kamera dan pin GPIO).



### 3.1 Mempersiapkan rumah



Pertama-tama, buka casing Anda. Pastikan casing bersih dan tidak ada sisa plastik cetak 3D yang menghalangi pengencang internal. Perhatikan :




- Lokasi kamera (lubang melingkar kecil di depan).
- Bukaan untuk layar.
- Potongan untuk port micro-USB dan slot microSD Raspberry Pi Zero.



### 3.2 Pemasangan kamera



Temukan konektor pita kamera pada Raspberry Pi Zero: ini adalah strip hitam tipis di sisi papan, yang dapat diangkat sedikit untuk membuka. Angkatlah dengan hati-hati, tanpa memaksanya: hanya perlu dimiringkan beberapa milimeter.



![Image](assets/fr/015.webp)



Masukkan penutup kamera. Bagian berwarna cokelat/tembaga harus menghadap ke bawah. Pastikan konektor terpasang dengan kuat pada konektor, tanpa terpuntir.



![Image](assets/fr/016.webp)



Tutup bilah hitam untuk mengunci taplak meja (Anda akan mendengar bunyi klik). Periksa dengan hati-hati, apakah taplak meja tetap di tempatnya dan tidak bergerak.



![Image](assets/fr/017.webp)



Kemudian, tempatkan modul kamera di lubang yang sesuai pada housing. Tergantung pada modelnya, modul ini bisa langsung terpasang atau memerlukan strip perekat kecil untuk menahannya di tempatnya. Lensa harus disejajarkan secara sempurna, menghadap ke luar.



### 3.3 Menginstalasi Raspberry Pi Zero



Jika Anda menggunakan casing, masukkan papan Raspberry Pi Zero ke dalamnya. Sejajarkan port dengan hati-hati dengan lubang yang tersedia.



Kemudian posisikan layar Waveshare di atas Raspberry Pi Zero. Pin GPIO Pi harus sejajar dengan konektor perempuan layar. Tekan layar secara perlahan ke pin, berikan tekanan yang sama pada setiap sisi untuk menghindari pembengkokan.



![Image](assets/fr/018.webp)



Jika Anda memiliki casing, selesaikan perakitan dengan menambahkan panel depan dan joystick.



Terakhir, masukkan kartu microSD yang berisi perangkat lunak yang telah di-flash ke dalam slot yang terpasang di tepi Raspberry Pi Zero. Pastikan kartu tersebut terkunci pada tempatnya.



### 3.4 Memulai pertama kali



Sambungkan kabel daya micro-USB ke port khusus. Tunggu sekitar satu menit. Logo SeedSigner akan muncul, diikuti dengan layar beranda.



![Image](assets/fr/019.webp)



Untuk memulainya, periksa apakah berbagai komponen berfungsi dengan baik dengan masuk ke menu `Settings > I/O test`.



![Image](assets/fr/020.webp)



Uji semua tombol dan pastikan tombol-tombol tersebut merespons dengan benar. Kemudian klik tombol `KEY1` untuk memeriksa apakah kamera berfungsi seperti yang diharapkan. Ini akan mengambil gambar.



![Image](assets/fr/021.webp)



### 3.5 Penyesuaian kamera



Tergantung pada cara Anda memasang SeedSigner, kamera mungkin menampilkan gambar yang terbalik. Untuk mengoreksi hal ini, buka `Pengaturan > Tingkat Lanjut > Rotasi kamera` dan pilih rotasi 180° jika perlu.



![Image](assets/fr/022.webp)



Jika Anda telah mengubah orientasi kamera atau ingin mengubah pengaturan lain (seperti bahasa antarmuka) di kemudian hari, Anda harus mengaktifkan persistensi pengaturan pada microSD. Jika tidak, pengaturan Anda akan kembali ke default setiap kali Anda melakukan boot ulang, karena Raspberry Pi Zero tidak memiliki memori persisten.



Untuk melakukannya, buka menu `Settings > Persistent settings (Pengaturan > Pengaturan persisten), lalu pilih `Enabled (Diaktifkan).



![Image](assets/fr/023.webp)



Jika semuanya sudah berfungsi, SeedSigner Anda sekarang siap digunakan!



## 4. Pengaturan SeedSigner



Sebelum membuat Bitcoin wallet Anda, mari kita konfigurasikan SeedSigner. Karena berjalan pada Raspberry Pi Zero tanpa memori persisten, pengaturannya tidak tersimpan secara otomatis kecuali Anda menyimpannya pada kartu microSD. Jadi pastikan Anda telah mengaktifkan opsi ini, jika tidak, pengaturan ini akan hilang saat reboot (lihat langkah 3.5).



### 4.1 Akses menu parameter



Jalankan SeedSigner Anda dan tunggu hingga layar beranda muncul. Dengan menggunakan joystick, navigasikan ke opsi `Pengaturan`, lalu validasi dengan menekan tombol tengah. Anda sekarang masuk ke menu pengaturan utama.



![Image](assets/fr/024.webp)



### 4.2 Memilih perangkat lunak manajemen portofolio



Kemudian akses menu `Perangkat lunak koordinator`.



![Image](assets/fr/025.webp)



"Koordinator" mengacu pada perangkat lunak manajemen portofolio yang akan digunakan oleh SeedSigner Anda untuk berkomunikasi melalui kode QR. Perangkat lunak ini diinstal di komputer atau ponsel pintar Anda. Perangkat lunak ini akan memungkinkan Anda untuk mengelola bitcoin Anda, tetapi tanpa memiliki akses ke kunci pribadi Anda. SeedSigner tetap menjadi satu-satunya perangkat yang mampu menandatangani transaksi Anda.



Versi firmware saat ini mendukung beberapa program: Sparrow, Specter, BlueWallet, Nunchuk dan Keeper. Dalam kasus saya, saya menggunakan **Sparrow Wallet**, yang secara khusus saya rekomendasikan karena kesederhanaan dan fungsionalitasnya yang kaya.



Jika Anda tidak tahu cara menginstalnya, Anda dapat mengikuti tutorial ini:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Cukup pilih perangkat lunak pilihan Anda dari menu.



![Image](assets/fr/026.webp)



### 4.3 Tampilan unit dan jumlah



Dalam menu `Denomination Display`, Anda dapat memilih unit yang digunakan untuk menampilkan jumlah:




- `BTC`
- mBTC` (mili-bitcoin, atau 0,001 BTC)
- gW-15 (satoshi, atau 1/100.000.000 BTC)



Unit **sats** pada umumnya adalah yang paling praktis untuk jumlah kecil.



![Image](assets/fr/027.webp)



### 4.4 Pengaturan lanjutan



Sekarang masuk ke menu `Advanced`. Di sini Anda akan menemukan beberapa opsi yang berguna:




- jaringan gW-17`: untuk dimodifikasi hanya jika Anda ingin menggunakan SeedSigner pada Testnet.
- qR code density`: menyesuaikan jumlah informasi yang terkandung dalam setiap kode QR. Anda dapat membiarkan nilai default, kecuali jika Anda merasa kesulitan untuk membaca saat memindai.
- ekspor `Xpub`: mengaktifkan atau menonaktifkan ekspor kunci publik yang diperluas (`xpub`, `ypub`, `zpub`) ke perangkat lunak manajemen portofolio melalui kode QR (fungsi yang akan kita gunakan nanti, jadi biarkan diaktifkan untuk saat ini).
- `Jenis skrip`: mendefinisikan jenis skrip yang diperbolehkan untuk mengunci bitcoin Anda. Anda tidak perlu memodifikasi parameter ini, karena tipe skrip akan disetel secara langsung ke Sparrow. Di sini, hanya skrip yang diizinkan untuk dimanipulasi oleh SeedSigner yang diperhatikan.



### 4.5 Pemilihan bahasa



Terakhir, dalam menu `Language`, Anda dapat mengubah bahasa antarmuka sesuai preferensi Anda.



![Image](assets/fr/028.webp)



## 5. Membuat dan menyimpan seed



seed (atau frasa mnemonik) menjadi dasar portofolio Bitcoin Anda. Ia digunakan untuk mendapatkan private key dan alamat Anda, dan menyediakan akses ke dana Anda. SeedSigner menawarkan beberapa metode untuk membuatnya, yang akan kita bahas di bagian ini.



Sebelum kita mulai, ada beberapa pengingat penting:




- Frasa ini memberikan akses penuh dan tidak terbatas ke semua bitcoin Anda.** Siapa pun yang memiliki frasa ini dapat mencuri dana Anda, bahkan tanpa akses fisik ke SeedSigner Anda;
- Biasanya, frasa 12 kata digunakan untuk memulihkan wallet jika terjadi kehilangan atau pencurian perangkat keras wallet. Tetapi karena SeedSigner adalah perangkat *stateless*, ia tidak pernah mendaftarkan seed Anda. Jadi, cadangan fisik Anda bukan hanya salinan cadangan, tetapi **satu-satunya cara untuk menggunakan wallet Anda**. Jika Anda kehilangan cadangan ini, bitcoin Anda akan hilang secara permanen. Jadi, buatlah cadangan dengan hati-hati, di beberapa media dan di tempat yang aman;
- Jika Anda baru memulai, saya sangat menyarankan Anda untuk membaca tutorial ini untuk mendapatkan pemahaman yang mendetail mengenai risiko yang terlibat dalam mengelola frasa mnemonik:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.1 Mengakses alat bantu pembuatan seed



Dari layar beranda SeedSigner, buka menu `Tools`.



![Image](assets/fr/029.webp)



Sekarang Anda akan mendapatkan generate dan seed. seed adalah sebuah angka acak yang besar. Semakin acak angka tersebut dihasilkan, semakin aman. SeedSigner menawarkan dua cara untuk melakukan ini:




- kamera": seed dihasilkan dari noise visual foto. Anda mengambil gambar lingkungan acak (objek, lanskap, wajah, dll.) yang variasi pikselnya digunakan untuk entropi generate. Ini adalah metode yang cepat, tetapi tidak dapat direproduksi.
- "lemparan dadu": Anda melempar dadu untuk menciptakan entropi yang diperlukan. Metode ini lebih memakan waktu, tetapi dapat direproduksi dan oleh karena itu dapat diverifikasi. Jika Anda memilih metode ini, ikuti saran dalam tutorial ini (tidak perlu menghitung checksum di sini, SeedSigner yang akan melakukannya):



https://planb.academy/tutorials/wallet/backup/generate-mnemonic-phrase-47507d90-e6af-4cac-b01b-01a14d7a8228

### 5.2 Menciptakan seed dengan foto



Jika Anda memilih metode foto, klik `New seed` (dengan ikon kamera), ambil gambar dan validasi. Kemudian pilih panjang kalimat Anda (12 atau 24 kata), yang akan muncul di layar untuk disimpan. Langkah-langkah berikut ini sama dengan bagian 5.3.



### 5.3 Membuat seed dengan dadu



Dalam tutorial ini, kami menggunakan metode **Dice Rolls**. Klik `New seed` (dengan ikon dadu).



![Image](assets/fr/030.webp)



Kemudian pilih panjang frasa mnemonik Anda. 12 kata sudah menawarkan tingkat keamanan yang memadai, jadi ini adalah pilihan yang saya rekomendasikan.



![Image](assets/fr/031.webp)



Lempar dadu Anda dan masukkan angka yang dihasilkan dengan menggunakan kursor. Tekan tombol tengah untuk memvalidasi setiap entri. Jika Anda membuat kesalahan, Anda dapat kembali. Gunakan beberapa dadu yang berbeda untuk mengurangi pengaruh dadu yang tidak seimbang. Pastikan Anda tidak diawasi selama operasi ini.



![Image](assets/fr/032.webp)



Setelah Anda memasukkan 50 lemparan, SeedSigner akan menghasilkan kalimat Anda. **Ikuti instruksi dalam tutorial ini dengan seksama jika Anda baru memulai:**



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.4 Menampilkan dan menyimpan seed



Tuliskan kata-kata frasa mnemonik Anda dengan hati-hati pada penyangga fisik yang sesuai (kertas atau logam).



![Image](assets/fr/033.webp)



### 5.5 Memeriksa cadangan



Untuk menghindari kesalahan pencadangan, SeedSigner meminta Anda untuk memverifikasi pencadangan Anda. Klik pada `Verifikasi`.



![Image](assets/fr/034.webp)



Kemudian masukkan kata yang diminta sesuai dengan urutannya dalam kalimat. Sebagai contoh, di sini saya harus memilih kata ketiga dalam kalimat saya.



![Image](assets/fr/035.webp)



Jika Anda membuat kesalahan, SeedSigner akan memberi tahu Anda, dan Anda harus memulai dari awal lagi, pastikan untuk mencatat frasa mnemonik Anda ketika diberikan kepada Anda. Langkah verifikasi ini memastikan bahwa cadangan Anda sudah benar dan lengkap. Setelah divalidasi, layar akan menampilkan `Backup Verified`.



![Image](assets/fr/036.webp)



Untuk tes pemulihan yang lebih lengkap, ikuti tutorial ini:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 5.6 Memahami konsep "perangkat tanpa kewarganegaraan



SeedSigner adalah sebuah perangkat tanpa memori permanen. Ini berarti seed Anda tidak pernah disimpan di dalam perangkat (tidak seperti Ledger, Trezor, atau Coldcard, misalnya). Segera setelah Anda mematikan daya, seed akan menghilang sepenuhnya dari RAM. Ketika Anda menyalakannya kembali, SeedSigner kembali ke kondisi kosong: Anda harus memberikan seed Anda lagi, agar dapat menandatangani transaksi Anda.



Hal ini memberikan perlindungan yang penting. Tidak seperti dompet perangkat keras lainnya, SeedSigner didasarkan pada Raspberry Pi Zero, yang tidak memiliki perlindungan fisik, termasuk *Secure Element*. Tetapi karena tidak ada data sensitif yang disimpan, bahkan perangkat yang disusupi secara fisik tidak akan mengizinkan penyerang untuk mengekstrak kunci pribadi Anda atau membelanjakan bitcoin Anda.



Di sisi lain, arsitektur ini menyiratkan tanggung jawab tambahan: tanpa cadangan, dana Anda pasti hilang. Itulah mengapa saya merekomendasikan **cadangan ganda**. Anda sudah memiliki frasa pemulihan Anda: ini adalah cadangan jangka panjang utama Anda, untuk disimpan di tempat yang aman. Sekarang kita akan membuat salinan frasa ini dalam bentuk **kode QR**.



Setiap kali Anda menggunakan SeedSigner, Anda memindai kode QR ini dengan kamera perangkat sehingga perangkat ini akan memuat seed Anda untuk sementara waktu ke dalam memorinya saat Anda menandatangani transaksi Anda. Cadangan kedua ini, yang ditujukan untuk penggunaan sehari-hari, juga harus disimpan dengan sangat hati-hati: siapa pun yang memiliki kode QR ini memiliki akses penuh ke bitcoin Anda.


Saya juga menyarankan Anda untuk menyimpan kode QR dan frasa mnemonik Anda di dua lokasi terpisah, untuk menghindari kehilangan semuanya jika terjadi klaim.



Terakhir, alternatif yang lebih canggih dan aman adalah dengan menggunakan SeedSigner dengan **SeedKeeper**, yang menyimpan seed di dalam secure element. Untuk mengetahui lebih lanjut, lihat tutorial ini:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

### 5.7 Tulis sidik jari kunci master



Setelah verifikasi selesai, SeedSigner menampilkan sidik jari dari kunci utama wallet Anda. Sidik jari ini mengidentifikasi wallet Anda dan memastikan bahwa Anda menggunakan frasa pemulihan yang benar di masa mendatang. Sidik jari ini tidak mengungkapkan informasi apapun mengenai kunci pribadi Anda, sehingga Anda dapat menyimpannya dengan aman pada media digital. Pastikan Anda menyimpan salinan yang dapat diakses dan tidak pernah kehilangannya.



![Image](assets/fr/037.webp)



Pada tahap ini Anda juga dapat menambahkan **passphrase BIP39** untuk memperkuat keamanan wallet Anda. Bergantung pada strategi pencadangan Anda, opsi ini mungkin bermanfaat, tetapi juga memiliki risiko: jika Anda kehilangan passphrase, akses ke bitcoin Anda akan hilang secara permanen.



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Jika Anda belum terbiasa dengan konsep passphrase, saya mengundang Anda untuk membaca tutorial komprehensif tentang subjek ini:



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

![Image](assets/fr/038.webp)



### 5.8 Menyimpan seed dalam format QR (*SeedQR*)



SeedSigner memungkinkan Anda mengonversi seed Anda menjadi kode QR kertas, yang disebut *SeedQR*. Metode ini menyederhanakan pemuatan ulang wallet Anda, karena menghindari pengetikan ulang setiap kata secara manual.



Untuk melakukan ini, Anda memerlukan kertas kosong atau kode QR logam yang sesuai dengan panjang frasa mnemonik Anda. Jika Anda telah membeli paket lengkap untuk SeedSigner Anda, template biasanya disertakan. Jika tidak, Anda dapat mengunduh dan mencetaknya (atau mereproduksinya dengan tangan) di sini:




- [Format 12 kata](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)
- [Format 24 kata](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_29x29.pdf)
- [Format ringkas 12 kata](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_21x21.pdf)
- [Format ringkas 24 kata](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)



Dari layar seed Anda, pilih `Backup Seed`.



![Image](assets/fr/039.webp)



Kemudian pilih `Export as SeedQR`.



![Image](assets/fr/040.webp)



Kemudian, pilih format yang diinginkan (normal atau compact) menurut templat kertas yang tersedia.



![Image](assets/fr/041.webp)



Klik `Mulai` untuk mulai membuat *SeedQR*. SeedSigner kemudian akan menampilkan serangkaian kisi-kisi (A1, A2, B1, dll.), masing-masing sesuai dengan bagian dari kode.



![Image](assets/fr/042.webp)



Dengan hati-hati mereproduksi setiap titik hitam pada lembar penyimpanan Anda, lalu gunakan joystick untuk beralih ke blok berikutnya. Luangkan waktu Anda: ketidaksejajaran yang sederhana dapat membuat kode QR tidak dapat digunakan.



Beberapa tips:




- Mulailah dengan pensil agar Anda bisa memperbaiki kesalahan, kemudian kembali menggunakan pena hitam yang halus setelah Anda selesai;
- Satu titik yang terpusat dengan baik di tengah-tengah kotak, itulah yang Anda perlukan, tidak perlu mengisinya secara penuh.



![Image](assets/fr/043.webp)



Kemudian klik `Konfirmasi SeedQR`, dan pindai kode QR Anda untuk memeriksa apakah kode tersebut berfungsi dengan benar.



![Image](assets/fr/044.webp)



Jika pesan `Sukses` ditampilkan, *SeedQR* Anda valid: Anda dapat melanjutkan ke langkah berikutnya.



![Image](assets/fr/045.webp)



**Simpanlah lembar ini seketat frasa pemulihan Anda. Siapapun yang memiliki kode QR ini dapat merekonstruksi kunci pribadi Anda dan mencuri bitcoin Anda.**



Selamat, portofolio Bitcoin Anda sekarang sudah aktif dan berjalan! Sekarang kita akan mengimpor komponen publiknya ke **Sparrow Wallet** untuk mengelolanya dengan mudah.



## 6. Impor wallet ke Sparrow



Setelah SeedSigner Anda disiapkan dan seed Anda dibuat dan disimpan dengan benar, langkah selanjutnya adalah menautkan portofolio ini ke perangkat lunak manajemen seperti Sparrow Wallet. seed Anda akan selalu offline, karena hanya bagian publik dari portofolio Anda yang akan dikirimkan ke Sparrow. Hal ini akan memungkinkan perangkat lunak untuk menampilkan alamat, transaksi, dan membuat transaksi baru, tanpa perlu membelanjakan bitcoin Anda. Untuk membelanjakan bitcoin Anda, SeedSigner Anda harus selalu menandatangani transaksi yang disiapkan oleh Sparrow.



### 6.1 Mempersiapkan Penandatangan Benih



Masukkan microSD yang berisi sistem operasi, nyalakan SeedSigner Anda, lalu muat seed yang baru saja Anda buat dari kode QR cadangan. Pada layar Utama, pilih `Pindai`, lalu pindai SeedQR Anda dengan SeedSigner.



![Image](assets/fr/046.webp)



Periksa apakah sidik jari pada kunci utama Anda cocok dengan sidik jari pada wallet Anda. Jika Anda menggunakan passphrase, masukkan sidik jari pada tahap ini.



![Image](assets/fr/047.webp)



Ini akan membawa Anda ke menu untuk portofolio Anda, dalam kasus saya, bernama `d4149b27`. Jika Anda kembali ke layar beranda, pilih `Seeds`, lalu pilih cetakan yang sesuai dengan portofolio Anda. Kemudian klik `Export Xpub`.



![Image](assets/fr/048.webp)



Pilih jenis portofolio. Dalam kasus kami, ini adalah portofolio tunggal: pilih `Single Sig`.



![Image](assets/fr/049.webp)



Berikutnya adalah pilihan standar skrip. Yang terbaru dan paling ekonomis dari segi biaya transaksi adalah `Taproot`. Oleh karena itu, saya menyarankan Anda untuk memilih standar ini.



![Image](assets/fr/050.webp)



Sebuah pesan peringatan akan muncul. Ini adalah hal yang normal: kunci publik yang diperluas (`xpub`) ini memungkinkan Anda untuk melihat semua alamat yang berasal dari seed Anda (pada akun pertama). Kunci ini tidak mengizinkan Anda untuk membelanjakan dana Anda, tetapi kunci ini mengungkapkan struktur portofolio Anda. Jika bocor, maka akan menjadi masalah bagi privasi Anda, tetapi tidak bagi keamanan bitcoin Anda: kunci ini memungkinkan Anda untuk melihatnya, tetapi tidak untuk membelanjakannya.



Klik `Saya Mengerti`, lalu `Ekspor Xpub` jika Anda puas dengan informasi yang ditampilkan.



SeedSigner kemudian menghasilkan xpub Anda dalam bentuk kode QR dinamis yang berisi semua data yang Anda perlukan untuk mengelola portofolio Anda di Sparrow Wallet.



![Image](assets/fr/051.webp)



Anda dapat menggunakan joystick untuk menyesuaikan kecerahan layar agar pemindaian kode QR lebih mudah.



### 6.2 Mengimpor portofolio baru ke dalam Sparrow Wallet



Pastikan Anda sudah menginstal perangkat lunak Sparrow Wallet di komputer Anda. Jika Anda tidak tahu cara mengunduh, memeriksa, dan menginstalnya dengan benar, lihat tutorial lengkap kami tentang masalah ini:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Pada komputer Anda, buka Sparrow Wallet, kemudian pada bilah menu, klik `File → Import Wallet`.



![Image](assets/fr/052.webp)



Gulir ke bawah ke `SeedSigner`, lalu pilih `Scan...`. Webcam Anda akan terbuka: pindai kode QR dinamis yang ditampilkan pada layar SeedSigner Anda.



![Image](assets/fr/053.webp)



Tetapkan nama untuk portofolio Anda, lalu klik `Buat Wallet`. Sparrow kemudian akan meminta Anda untuk mengatur kata sandi untuk mengunci akses lokal ke wallet ini. Pilih kata sandi yang kuat: kata sandi ini akan melindungi akses ke data portofolio Anda di Sparrow (kunci publik, alamat, label, dan riwayat transaksi). Kata sandi ini tidak diperlukan untuk memulihkan portofolio di kemudian hari: hanya frasa mnemonik Anda (dan mungkin passphrase Anda) yang diperlukan untuk tujuan ini.



Saya sarankan Anda menyimpan kata sandi ini dalam pengelola kata sandi untuk menghindari kehilangannya.



![Image](assets/fr/054.webp)



Keystore Anda sekarang telah berhasil diimpor.



![Image](assets/fr/055.webp)



Kemudian periksa apakah `sidik jari master` yang ditampilkan di Sparrow cocok dengan yang sebelumnya dicatat di SeedSigner Anda.



SeedSigner dan Sparrow Wallet Anda sekarang terhubung dengan aman. Sparrow bertindak sebagai antarmuka manajemen yang lengkap, sementara SeedSigner tetap menjadi satu-satunya perangkat yang mampu menandatangani transaksi Anda. Anda sekarang siap untuk menerima dan mengirim bitcoin dalam konfigurasi yang benar-benar tanpa celah.



## 7. Menerima dan mengirim bitcoin



SeedSigner dan Sparrow Wallet Anda sekarang telah dikonfigurasikan untuk bekerja bersama. Pada bagian terakhir ini, kita akan melihat bagaimana cara menerima dan mengirim bitcoin menggunakan konfigurasi ini.



### 7.1 Menerima bitcoin



#### 7.1.1 Membuat alamat penerimaan



Pada komputer Anda, buka Sparrow Wallet dan buka kunci SeedSigner wallet menggunakan kata sandi Anda. Pastikan perangkat lunak terhubung ke server (lekukan di kanan bawah). Pada bilah sisi, klik pada `Terima`.



![Image](assets/fr/056.webp)



Alamat Bitcoin baru ditampilkan. Anda akan melihat :




- Alamat teks (dimulai dengan `bc1p... ` jika Anda menggunakan P2TR seperti yang saya gunakan),
- Kode QR yang sesuai,
- Kolom `Label` untuk melacak transaksi Anda.



Saya sangat menyarankan agar Anda menambahkan label pada setiap tanda terima bitcoin pada wallet Anda. Hal ini akan memudahkan Anda untuk mengidentifikasi asal usul setiap UTXO dan meningkatkan manajemen privasi Anda. Untuk mempelajari lebih dalam tentang topik penting ini, Anda bisa melihat pelatihan khusus di Plan ₿ Academy:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Untuk menambahkan label, cukup masukkan nama di bidang `Label`, lalu konfirmasikan.



Sebagai contoh:



```txt
Label : Sale of the Raspberry Pi Zero
```



Alamat Anda sekarang dikaitkan dengan label ini di semua bagian Sparrow.



![Image](assets/fr/057.webp)



#### 7.1.2 Verifikasi Address pada SeedSigner



Sebelum membagikan alamat penerima Anda, sangat penting untuk memeriksa bahwa alamat tersebut adalah milik seed Anda. Langkah ini memastikan bahwa SeedSigner Anda akan dapat menandatangani transaksi yang terkait dengan alamat ini. Langkah ini juga melindungi dari kemungkinan serangan dimana Sparrow menampilkan alamat palsu. Ingatlah bahwa Sparrow berjalan pada lingkungan yang tidak aman (komputer Anda), yang memiliki permukaan serangan yang jauh lebih besar dibandingkan dengan SeedSigner Anda, yang benar-benar terisolasi. Oleh karena itu, jangan pernah percaya begitu saja dengan alamat penerima yang ditampilkan di Sparrow sampai Anda memverifikasinya dengan perangkat keras wallet Anda.



Pada Sparrow, klik pada kode QR alamat untuk memperbesarnya: kode tersebut akan ditampilkan dalam layar penuh.



![Image](assets/fr/058.webp)



Pada SeedSigner Anda, dari menu utama, pilih `Pindai`. Pindai kode QR yang ditampilkan di layar komputer Anda, lalu pilih seed yang sesuai dengan wallet Anda (dalam kasus saya, sidik jari `d4149b27`).



![Image](assets/fr/059.webp)



Jika alamat yang dipindai cocok dengan alamat yang berasal dari seed Anda, layar SeedSigner akan menampilkan pesan: `Address Terverifikasi`.



![Image](assets/fr/060.webp)



Hal ini mengonfirmasi bahwa alamat tersebut adalah milik wallet Anda dan Anda bisa menerima bitcoin darinya.



#### 7.1.3 Penerimaan dana



Sekarang Anda dapat menyampaikan alamat ini (dalam bentuk teks atau kode QR) kepada orang atau departemen yang perlu mengirimi Anda satss. Setelah transaksi disiarkan di jaringan, transaksi tersebut akan muncul di tab `Transactions` pada Sparrow Wallet.



![Image](assets/fr/061.webp)



### 7.2 Kirim bitcoin



Mengirim bitcoin dengan SeedSigner adalah proses 3 langkah:




- Pembuatan transaksi di Sparrow ;
- Tanda tangan transaksi pada SeedSigner ;
- Distribusi akhir transaksi melalui Sparrow.



Semua pertukaran antara kedua perangkat dilakukan secara eksklusif menggunakan kode QR.



#### 7.2.1 Membuat transaksi di Sparrow



Pada Sparrow Wallet, Anda dapat mengklik tab `Send` pada bilah sisi kiri. Namun demikian, saya lebih suka menggunakan tab `UTXOs`, yang memungkinkan Anda mempraktikkan "*Coin Control*". Metode ini memberi Anda kendali yang tepat atas UTXO yang digunakan, sehingga Anda bisa mengendalikan informasi yang Anda ungkapkan selama transaksi.



Pada tab `UTXOs`, pilih koin yang ingin Anda belanjakan, lalu klik `Kirim Terpilih`.



![Image](assets/fr/062.webp)



Kemudian isi kolom transaksi:




- Di `Bayar ke`, tempelkan alamat penerima atau klik ikon kamera untuk memindai kode QR;
- Di `Label`, tambahkan label untuk melacak pengeluaran ini;
- Dalam `Jumlah`, masukkan jumlah yang akan dikirim;
- Terakhir, pilih tingkat biaya berdasarkan kondisi pasar saat ini (perkiraan tersedia di [mempool.space](https://mempool.space/)).



Setelah isian diisi, periksa informasinya dengan cermat, lalu klik `Buat Transaksi >>`.



![Image](assets/fr/063.webp)



Periksa detail transaksi untuk memastikan semuanya sudah benar, lalu klik `Finalisasi Transaksi untuk Penandatanganan`.



![Image](assets/fr/064.webp)



Transaksi sekarang sudah siap, tetapi belum ditandatangani. Untuk menampilkan [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/psbt) sebagai kode QR, klik `Tampilkan QR`.



![Image](assets/fr/065.webp)



#### 7.2.2 Menandatangani transaksi dengan Penandatangan Benih



Nyalakan SeedSigner Anda dan pindai SeedQR Anda untuk mengakses portofolio Anda, seperti biasa. Dari layar beranda, pilih `Pindai`, lalu pindai kode QR yang ditampilkan pada Sparrow.



![Image](assets/fr/066.webp)



Kemudian pilih seed yang sesuai dengan portofolio Anda.



![Image](assets/fr/067.webp)



SeedSigner secara otomatis mendeteksi bahwa ini adalah PSBT dan menampilkan ringkasan transaksi:




   - Jumlah yang dikirim,
   - Alamat keluaran,
   - Biaya transaksi terkait.



Klik `Tinjau Detail` dan periksa dengan cermat semua informasi secara langsung pada layar SeedSigner. Hal yang paling penting untuk diperiksa adalah jumlah yang dikirim, alamat penerima, dan jumlah biaya yang dikenakan.



![Image](assets/fr/068.webp)



Jika semuanya sudah benar, pilih `Approve PSBT` untuk menandatangani transaksi dengan menggunakan kunci privat yang sesuai.



![Image](assets/fr/069.webp)



Setelah ditandatangani, SeedSigner menghasilkan kode QR baru yang berisi transaksi yang telah ditandatangani, yang siap untuk dipindai oleh Sparrow.



![Image](assets/fr/070.webp)



#### 7.2.3 Menyiarkan transaksi dari Sparrow



Setelah transaksi valid, transaksi tersebut perlu disiarkan di jaringan Bitcoin, sehingga sampai ke penambang yang akan menambahkannya ke dalam blok.



Pada Sparrow, klik `QR Scan`.



![Image](assets/fr/071.webp)



Tunjukkan kode QR yang ditampilkan oleh SeedSigner Anda (kode dari transaksi yang ditandatangani) ke webcam. Sparrow akan memecahkan kode tanda tangan dan menampilkan detail transaksi secara lengkap. Lakukan pemeriksaan akhir bahwa semua informasi sudah benar, lalu klik Broadcast Transaction untuk menyiarkannya di jaringan Bitcoin.



![Image](assets/fr/072.webp)



Transaksi Anda sekarang telah dikirim ke jaringan Bitcoin. Anda dapat mengikuti perkembangannya di tab `Transaksi` pada Sparrow Wallet.



![Image](assets/fr/073.webp)



Anda sekarang telah menguasai dasar-dasar penggunaan SeedSigner. Untuk memperdalam pengetahuan Anda dan menjelajahi penggunaan yang lebih lanjut, saya mengundang Anda untuk membaca tutorial berikut ini:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

**[Anda juga dapat mendukung pengembangan proyek sumber terbuka SeedSigner dengan memberikan donasi dalam bentuk bitcoin!](https://seedsigner.com/donate/)**



*Kredit: beberapa gambar dalam tutorial ini berasal dari [situs web resmi proyek SeedSigner](https://seedsigner.com/) dan [repositori GitHub](https://github.com/SeedSigner/seedsigner).*