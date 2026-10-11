---
name: SeedSigner
description: Perangkat keras wallet yang dibuat sendiri, tanpa status, terjangkau, dan sepenuhnya air gapped
---

![cover](assets/cover.webp)



SeedSigner adalah hardware wallet Bitcoin sumber terbuka yang bisa kamu rakit sendiri menggunakan komponen elektronik umum yang murah. Berbeda dengan produk komersial seperti Ledger, Coldcard atau Trezor, ini bukan perangkat siap pakai yang diproduksi perusahaan: ini adalah proyek komunitas yang memungkinkan siapa pun merakit perangkatnya sendiri dan mengendalikan setiap tahapannya.

SeedSigner dirancang agar 100% ***air-gapped***: tidak pernah terhubung ke internet, tidak memiliki Wi-Fi atau Bluetooth (pada Raspberry Pi Zero v1.3), dan tidak pernah tersambung ke komputer untuk bertukar data. Komunikasi dilakukan sepenuhnya melalui pertukaran kode QR. Secara praktis, software manajemen wallet kamu, seperti Sparrow Wallet, menampilkan transaksi yang akan ditandatangani dalam bentuk kode QR; kamu memindainya dengan kamera SeedSigner, lalu perangkat menandatangani transaksi menggunakan private key yang disimpan sementara di RAM. Terakhir, perangkat ini menghasilkan kode QR berisi transaksi yang sudah ditandatangani, lalu kamu memindainya dengan software untuk menyiarkannya ke jaringan Bitcoin.


![Image](assets/fr/001.webp)



SeedSigner juga tidak memiliki status. Artinya, perangkat ini tidak menyimpan seed atau private key kamu secara permanen, berbeda dengan hardware wallet lain. Setiap kali kamu me-reboot, memorinya benar-benar kosong, kecuali kalau kamu mengatur perangkat untuk menyimpan preferensi di kartu microSD. Jadi, kamu perlu memasukkan kembali seed setiap kali menggunakannya. Cara paling praktis adalah menyimpannya dalam bentuk kode QR yang bisa kamu pindai saat boot menggunakan kamera SeedSigner. Model operasi ini sangat mengurangi permukaan serangan: bahkan jika pencuri mengambil perangkat kamu, dia tidak akan menemukan informasi apa pun di dalamnya karena secara default selalu kosong.

Opsi lain untuk menyimpan seed dan menggunakannya dengan SeedSigner adalah memakai kartu pintar *SeedKeeper* bersama pembaca yang kompatibel. Ini memberimu *Secure Element* yang kuat untuk menyimpan seed, sambil tetap menggunakan layar SeedSigner untuk menandatangani transaksi. Namun konfigurasi khusus ini dibahas dalam tutorial terpisah. Di sini, kita fokus pada penggunaan dasar SeedSigner:

https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

Proyek SeedSigner punya posisi penting dalam ekosistem Bitcoin karena memberi siapa pun, di mana pun, akses ke keamanan tingkat lanjut untuk melindungi bitcoin mereka. Keunggulan utamanya ada pada aksesibilitas: hardware yang dibutuhkan bisa dibeli dengan harga kurang dari $50. Selain itu, orang yang tinggal di negara dengan pembatasan ketat tetap bisa merakit hardware wallet sendiri dari komponen komputer standar yang mudah ditemukan dan umumnya tidak terlalu terdampak regulasi.

Bahkan di luar konteks tersebut, SeedSigner tetap menarik: proyek ini bersifat sumber terbuka, bekerja tanpa batas negara dan sepenuhnya ***air-gapped***, serta mengurangi vektor serangan yang berkaitan dengan rantai pasokan hardware wallet kamu.

## 1. Peralatan yang diperlukan

Untuk merakit SeedSigner, kamu memerlukan komponen berikut:



- Raspberry Pi Nol
    - Versi 1.3 direkomendasikan, karena tidak memiliki Wi-Fi maupun Bluetooth, sehingga memastikan isolasi yang lengkap.
 - Versi W dan v2 juga kompatibel, tetapi menyertakan chip Wi-Fi/Bluetooth. Oleh karena itu, disarankan untuk menonaktifkannya secara fisik dengan melepaskan modul radio dari kartu. Pengoperasiannya relatif sederhana, tetapi membutuhkan ketelitian (tang halus cukup untuk Zero W, sedangkan untuk v2 diperlukan pena panas untuk melepaskan pelat logam yang menyembunyikan modul). Aku tidak akan membahas secara rinci dalam tutorial ini, tetapi kamu akan menemukan semua instruksi dalam dokumen ini: *[Menonaktifkan WiFi/Bluetooth dengan perangkat keras](https://github.com/DesobedienteTecnologico/rpi_disable_wifi_and_bt_by_hardware)*.
 - Harap diperhatikan: beberapa model Raspberry Pi Zero dijual tanpa pin GPIO yang sudah disolder. Kamu bisa membeli versi dengan pin terintegrasi secara langsung (solusi paling sederhana), atau membeli pin secara terpisah dan menyoldernya sendiri (solusi yang lebih kompleks).
 - Jangan lupa menyertakan catu daya micro-USB.



![Image](assets/fr/002.webp)





- Layar Waveshare 1,3 inci (240×240 piksel)** (dalam bahasa Prancis)
    - Sangat penting untuk memilih model khusus ini: ada layar lain yang serupa, tetapi dengan resolusi yang berbeda. Tanpa definisi 240×240 px, layar tidak akan dapat digunakan.
    - Layarnya dilengkapi tiga tombol dan joystick mini untuk antarmuka pengguna.



![Image](assets/fr/003.webp)





- Kamera yang kompatibel dengan Raspberry Pi Zero**
    - Opsi 1: kamera standar dengan alas emas lebar (periksa kompatibilitasnya dengan housing kamu).
    - Opsi 2: kamera "*Zero*" yang lebih ringkas, yang didesain khusus untuk Pi Zero.



![Image](assets/fr/004.webp)





- Kartu MicroSD**
    - Kapasitas yang disarankan: antara 4 dan 32 GB.





- Housing (opsional tetapi disarankan)** (opsional tetapi disarankan)** (opsional tetapi disarankan)** (opsional tetapi disarankan)**)
    - Melindungi perangkat dan membuatnya mudah digunakan.
    - Model yang paling populer adalah "*Orange Pill Case*", yang mana [file STL sumber terbuka tersedia untuk pencetakan 3D](https://github.com/SeedSigner/seedsigner/tree/dev/enclosureshttps://github.com/SeedSigner/seedsigner/tree/dev/enclosures).
    - Kotak juga tersedia dari [pengecer independen yang terhubung dengan proyek](https://seedsigner.com/hardware/).



![Image](assets/fr/005.webp)



Kamu bisa membeli komponen-komponen ini secara terpisah atau, untuk lebih mudahnya, pilihlah paket yang sudah jadi yang sudah termasuk semua perangkat keras yang diperlukan. Secara pribadi, aku memesan paket saya [di situs Perancis ini](https://bitcoinbazar.fr/), tetapi Anda juga akan menemukan daftar vendor untuk setiap wilayah di dunia pada [halaman perangkat keras proyek SeedSigner](https://seedsigner.com/hardware/). Jika kamu lebih suka membeli komponen secara terpisah, komponen-komponen tersebut tersedia di platform e-commerce utama atau di toko-toko spesialis.



## 2. Mempersiapkan perangkat lunak



Setelah menyiapkan perangkat keras, kamu perlu menyiapkan kartu microSD dengan menginstal sistem SeedSigner di dalamnya. Untuk melakukan ini, buka komputer pribadi kamu sehari-hari, dan colokkan microSD yang ditujukan untuk SeedSigner.



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



Terminal akan memberitahukan kamu bahwa sebuah kunci telah diimpor atau diperbarui. Selanjutnya, jalankan perintah verifikasi pada file tanda tangan (ingatlah untuk memodifikasi perintah sesuai dengan versi Anda, di sini `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/008.webp)



Jika semuanya sudah benar, keluarannya akan menampilkan `Good signature`. Artinya, file `.sha256.txt` memang ditandatangani oleh key yang baru saja kamu impor dan tanda tangannya valid. Abaikan pesan peringatan `WARNING: This key is not certified with a trusted signature`: ini normal, karena sekarang tanggung jawab ada di kamu untuk memastikan bahwa key tersebut benar milik proyek SeedSigner.



Untuk melakukan hal ini, bandingkan 16 karakter terakhir dari sidik jari yang ditampilkan dengan yang tersedia di [Keybase.io/SeedSigner](https://keybase.io/seedsigner), di [Twitter resmi](https://twitter.com/SeedSigner/status/1530555252373704707), atau di file yang dipublikasikan di [SeedSigner.com](https://seedsigner.com/keybase.txt). Jika pengidentifikasi ini sama persis, kamu dapat yakin bahwa kuncinya memang berasal dari proyek tersebut. Jika ragu, segera hentikan dan mintalah bantuan kepada komunitas SeedSigner (Telegram, X, GitHub...).



Ketika kunci telah divalidasi, kamu dapat memeriksa bahwa gambar yang diunduh belum dimodifikasi (ingatlah untuk memodifikasi perintah sesuai dengan versi kamu, di sini `0.8.6.`):



```
shasum -a 256 --ignore-missing --check seedsigner.0.8.6.sha256.txt
```



![Image](assets/fr/009.webp)





- Di Linux, perintah ini sudah tersedia secara bawaan.
- Peringatan: versi macOS sebelum `Big Sur (11)` tidak mengenali opsi `--ignore-missing`. Dalam kasus ini, hapus opsi tersebut dan abaikan peringatan tentang file yang hilang.

Hasil yang diharapkan adalah `OK` di samping file `.img`. Ini memastikan bahwa image yang kamu unduh identik dengan yang dipublikasikan oleh proyek dan belum dimodifikasi.

### 2.3 Verifikasi Windows

Di Windows, prosedurnya mirip tetapi perintahnya berbeda. Mulai dengan menginstal [Gpg4win](https://www.gpg4win.org/) lalu buka aplikasi *Kleopatra*. Impor public key proyek SeedSigner dari URL Keybase berikut:




```
https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/010.webp)



Selanjutnya, buka PowerShell di folder tempat file yang telah diunduh berada (`Shift` + klik kanan > `Buka PowerShell di sini`). Jalankan perintah berikut untuk memeriksa tanda tangan manifes (ingatlah untuk memodifikasi perintah sesuai dengan versi kamu, di sini `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/011.webp)



Jika semuanya sudah benar, keluarannya akan berbunyi `Tanda tangan yang baik`. Ini berarti bahwa file `.sha256.txt` telah ditandatangani oleh kunci yang baru saja kamu impor, dan tanda tangan tersebut valid. Abaikan pesan peringatan `WARNING: This key is not certified with a trusted signature`: ini normal, karena sekarang terserah kamu untuk memeriksa apakah kunci yang digunakan adalah milik proyek SeedSigner.



Untuk melakukan hal ini, bandingkan 16 karakter terakhir dari sidik jari yang ditampilkan dengan yang tersedia di [Keybase.io/SeedSigner](https://keybase.io/seedsigner), di [Twitter resmi](https://twitter.com/SeedSigner/status/1530555252373704707), atau di file yang dipublikasikan di [SeedSigner.com](https://seedsigner.com/keybase.txt). Jika pengidentifikasi ini sama persis, kamu dapat yakin bahwa kuncinya memang berasal dari proyek tersebut. Jika ragu, segera hentikan dan mintalah bantuan kepada komunitas SeedSigner (Telegram, X, GitHub...).



Setelah kunci divalidasi, kamu perlu memeriksa bahwa file gambar belum rusak. Untuk melakukan hal ini, gunakan perintah berikut ini di PowerShell:



```
CertUtil -hashfile seedsigner_os.0.8.6.[your-Pi-model].img SHA256
```



Contoh untuk Raspberry Pi Zero 2 (ingatlah untuk memodifikasi perintah sesuai dengan versi kamu, di sini `0.8.6.`):



```
CertUtil -hashfile seedsigner_os.0.8.6.pi02w.img SHA256
```



![Image](assets/fr/012.webp)



PowerShell kemudian menghitung hash SHA256 dari file gambar kamu. Bandingkan hash ini dengan nilai yang sesuai di `seedsigner.0.8.6.sha256.txt`.




- Jika kedua nilai tersebut sama persis, pemeriksaan berhasil dan kamu dapat melanjutkan.
- Jika berbeda, berarti file tersebut rusak atau rusak. Jangan gunakan file tersebut, dan mulai mengunduh lagi.



![Image](assets/fr/013.webp)



Verifikasi yang berhasil menjamin bahwa berkas `.img` Anda adalah asli (ditandatangani oleh SeedSigner) dan tidak diubah (tidak dimodifikasi). kamu dapat melanjutkan ke langkah berikutnya dengan aman.



### 2.4. Mem-flash gambar



Jika kamu belum memilikinya, unduh perangkat lunak [Balena Etcher](https://etcher.balena.io/), kemudian :




- Masukkan kartu microSD ke dalam komputer kamu.
- Luncurkan Etcher.
- Pilih file `.img` yang telah diunduh dan diverifikasi.
- Pilih kartu microSD sebagai target.
- Klik `Flash!`.



![Image](assets/fr/014.webp)



Tunggu sampai proses selesai: kartu microSD kamu sekarang siap digunakan. Saatnya masuk ke tahap perakitan!

## 3. Perakitan SeedSigner

Setelah kartu microSD siap dan sudah di-flash dengan software SeedSigner, kamu bisa lanjut ke perakitan akhir. Kerjakan dengan pelan dan hati-hati, karena beberapa bagiannya cukup rapuh, terutama layar, kamera, dan pin GPIO.

### 3.1 Mempersiapkan casing

Pertama, buka casing. Pastikan casing bersih dan tidak ada sisa cetakan 3D yang menghalangi pengunci internal. Perhatikan:

- Posisi kamera, yaitu lubang kecil berbentuk lingkaran di bagian depan.
- Bukaan untuk layar.
- Celah untuk port micro-USB dan slot microSD pada Raspberry Pi Zero.

### 3.2 Memasang kamera

Cari konektor pita kamera pada Raspberry Pi Zero. Letaknya berupa strip hitam tipis di sisi board yang bisa diangkat sedikit untuk membukanya. Angkat dengan hati-hati tanpa dipaksa, cukup dimiringkan beberapa milimeter saja.

![Image](assets/fr/015.webp)



Masukkan penutup kamera. Bagian berwarna cokelat/tembaga harus menghadap ke bawah. Pastikan konektor terpasang dengan kuat pada konektor, tanpa terpuntir.



![Image](assets/fr/016.webp)



Tutup bilah hitam untuk mengunci taplak meja (kamu akan mendengar bunyi klik). Periksa dengan hati-hati, apakah taplak meja tetap di tempatnya dan tidak bergerak.



![Image](assets/fr/017.webp)



Selanjutnya, pasang modul kamera ke lubang yang sesuai pada casing. Tergantung model casing yang kamu pakai, modul ini bisa langsung terpasang atau perlu sedikit perekat agar tetap di tempatnya. Pastikan lensa benar-benar sejajar dan menghadap ke luar.

### 3.3 Menginstal Raspberry Pi Zero

Jika kamu menggunakan casing, masukkan board Raspberry Pi Zero ke dalamnya. Sejajarkan port dengan hati-hati ke lubang yang tersedia.

Lalu letakkan layar Waveshare di atas Raspberry Pi Zero. Pin GPIO pada Pi harus sejajar dengan konektor female di layar. Tekan layar secara perlahan ke pin dengan tekanan merata di setiap sisi agar pin tidak bengkok.


![Image](assets/fr/018.webp)



Jika kamu memiliki casing, selesaikan perakitan dengan menambahkan panel depan dan joystick.



Terakhir, masukkan kartu microSD yang berisi perangkat lunak yang telah di-flash ke dalam slot yang terpasang di tepi Raspberry Pi Zero. Pastikan kartu tersebut terkunci pada tempatnya.



### 3.4 Memulai pertama kali



Sambungkan kabel daya micro-USB ke port khusus. Tunggu sekitar satu menit. Logo SeedSigner akan muncul, diikuti dengan layar beranda.



![Image](assets/fr/019.webp)



Untuk memulainya, periksa apakah berbagai komponen berfungsi dengan baik dengan masuk ke menu `Settings > I/O test`.



![Image](assets/fr/020.webp)



Uji semua tombol dan pastikan tombol-tombol tersebut merespons dengan benar. Kemudian klik tombol `KEY1` untuk memeriksa apakah kamera berfungsi seperti yang diharapkan. Ini akan mengambil gambar.



![Image](assets/fr/021.webp)



### 3.5 Penyesuaian kamera



Tergantung pada cara kamu memasang SeedSigner, kamera mungkin menampilkan gambar yang terbalik. Untuk mengoreksi hal ini, buka `Pengaturan > Tingkat Lanjut > Rotasi kamera` dan pilih rotasi 180° jika perlu.



![Image](assets/fr/022.webp)



Jika nanti kamu mengubah orientasi kamera atau ingin menyesuaikan pengaturan lain, seperti bahasa antarmuka, kamu perlu mengaktifkan persistensi pengaturan di microSD. Kalau tidak, semua pengaturan akan kembali ke default setiap kali kamu reboot, karena Raspberry Pi Zero tidak memiliki memori persisten.


Untuk melakukannya, buka menu `Settings > Persistent settings (Pengaturan > Pengaturan persisten), lalu pilih `Enabled (Diaktifkan).



![Image](assets/fr/023.webp)



Jika semuanya sudah berfungsi dengan baik, SeedSigner kamu sekarang siap digunakan!

## 4. Pengaturan SeedSigner

Sebelum membuat Bitcoin wallet, kita konfigurasikan dulu SeedSigner. Karena berjalan di Raspberry Pi Zero tanpa memori persisten, pengaturannya tidak akan tersimpan otomatis kecuali kamu menyimpannya di kartu microSD. Jadi pastikan opsi ini sudah kamu aktifkan, kalau tidak semua pengaturan akan hilang saat reboot, lihat langkah 3.5.

### 4.1 Akses menu pengaturan

Nyalakan SeedSigner dan tunggu sampai layar utama muncul. Gunakan joystick untuk masuk ke opsi `Settings`, lalu konfirmasi dengan menekan tombol tengah. Sekarang kamu berada di menu pengaturan utama.


![Image](assets/fr/024.webp)



### 4.2 Memilih perangkat lunak manajemen portofolio



Kemudian akses menu `Perangkat lunak koordinator`.



![Image](assets/fr/025.webp)



`Koordinator` mengacu pada software manajemen wallet yang akan digunakan SeedSigner untuk berkomunikasi melalui kode QR. Software ini terpasang di komputer atau smartphone kamu. Fungsinya untuk mengelola bitcoin kamu, tetapi tanpa pernah memiliki akses ke private key. SeedSigner tetap menjadi satu-satunya perangkat yang bisa menandatangani transaksi.

Versi firmware saat ini mendukung beberapa software: Sparrow, Specter, BlueWallet, Nunchuk, dan Keeper. Dalam contoh ini, aku menggunakan **Sparrow Wallet**, yang sangat aku rekomendasikan karena sederhana dan fiturnya lengkap.

Kalau kamu belum tahu cara menginstalnya, kamu bisa mengikuti tutorial berikut:

https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Tinggal pilih software yang kamu gunakan dari menu.



![Image](assets/fr/026.webp)



### 4.3 Tampilan unit dan jumlah



Dalam menu `Denomination Display`, kamu dapat memilih unit yang digunakan untuk menampilkan jumlah:




- `BTC`
- mBTC` (mili-bitcoin, atau 0,001 BTC)
- gW-15 (satoshi, atau 1/100.000.000 BTC)



Unit **sats** pada umumnya adalah yang paling praktis untuk jumlah kecil.



![Image](assets/fr/027.webp)



### 4.4 Pengaturan lanjutan



Sekarang masuk ke menu `Advanced`. Di sini Anda akan menemukan beberapa opsi yang berguna:




- jaringan gW-17`: untuk dimodifikasi hanya jika Anda ingin menggunakan SeedSigner pada Testnet.
- qR code density`: menyesuaikan jumlah informasi yang terkandung dalam setiap kode QR. Anda dapat membiarkan nilai default, kecuali jika kamu merasa kesulitan untuk membaca saat memindai.
- ekspor `Xpub`: mengaktifkan atau menonaktifkan ekspor kunci publik yang diperluas (`xpub`, `ypub`, `zpub`) ke perangkat lunak manajemen portofolio melalui kode QR (fungsi yang akan kita gunakan nanti, jadi biarkan diaktifkan untuk saat ini).
- `Jenis skrip`: mendefinisikan jenis skrip yang diperbolehkan untuk mengunci bitcoin. Kamu tidak perlu memodifikasi parameter ini, karena tipe skrip akan disetel secara langsung ke Sparrow. Di sini, hanya skrip yang diizinkan untuk dimanipulasi oleh SeedSigner yang diperhatikan.



### 4.5 Pemilihan bahasa



Terakhir, dalam menu `Language`, kamu dapat mengubah bahasa antarmuka sesuai preferensi Anda.



![Image](assets/fr/028.webp)



## 5. Membuat dan menyimpan seed



Seed atau seedphrase menjadi fondasi wallet Bitcoin kamu. Dari sinilah private key dan alamat diturunkan, sekaligus menjadi akses ke dana kamu. SeedSigner menyediakan beberapa metode untuk membuatnya, yang akan kita bahas di bagian ini.

Sebelum mulai, ada beberapa hal penting yang perlu kamu ingat:

- Frasa ini memberi akses penuh dan tanpa batas ke semua bitcoin kamu. Siapa pun yang memilikinya bisa mencuri dana kamu, bahkan tanpa akses fisik ke SeedSigner;
- Biasanya, frasa 12 kata digunakan untuk memulihkan wallet jika hardware wallet hilang atau dicuri. Namun karena SeedSigner adalah perangkat *stateless*, ia tidak pernah menyimpan seed kamu. Jadi cadangan fisik bukan sekadar backup, tetapi **satu-satunya cara untuk menggunakan wallet kamu**. Jika cadangan ini hilang, bitcoin kamu juga hilang permanen. Karena itu, buat cadangan dengan sangat hati-hati, di beberapa media dan simpan di tempat yang aman;
- Jika kamu masih baru, aku sangat menyarankan kamu membaca tutorial berikut agar benar-benar paham risiko dalam mengelola seedphrase:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.1 Mengakses alat bantu pembuatan seed



Dari layar beranda SeedSigner, buka menu `Tools`.



![Image](assets/fr/029.webp)



Sekarang kamu akan membuat seed. Seed adalah angka acak berukuran besar. Semakin acak proses pembuatannya, semakin tinggi tingkat keamanannya. SeedSigner menawarkan dua metode untuk melakukannya:

- `Camera`: seed dihasilkan dari noise visual sebuah foto. Kamu mengambil gambar lingkungan acak, seperti objek, lanskap, wajah, dan variasi pikselnya digunakan sebagai entropi untuk generate seed. Metode ini cepat, tetapi tidak bisa direproduksi.
- `Dice Rolls`: kamu melempar dadu untuk menghasilkan entropi yang dibutuhkan. Metode ini lebih lama, tetapi bisa direproduksi dan diverifikasi. Jika kamu memilih metode ini, ikuti panduan di tutorial berikut, tidak perlu menghitung checksum karena SeedSigner akan melakukannya:

https://planb.academy/tutorials/wallet/backup/generate-mnemonic-phrase-47507d90-e6af-4cac-b01b-01a14d7a8228

### 5.2 Membuat seed dengan foto

Jika kamu memilih metode foto, klik `New seed` dengan ikon kamera, ambil gambar lalu konfirmasi. Setelah itu pilih panjang seedphrase kamu, 12 atau 24 kata, yang akan ditampilkan di layar untuk kamu simpan. Langkah berikutnya sama seperti di bagian 5.3.

### 5.3 Membuat seed dengan dadu

Dalam tutorial ini, kita menggunakan metode **Dice Rolls**. Klik `New seed` dengan ikon dadu.


![Image](assets/fr/030.webp)



Kemudian pilih panjang frasa mnemonik Anda. 12 kata sudah menawarkan tingkat keamanan yang memadai, jadi ini adalah pilihan yang saya rekomendasikan.



![Image](assets/fr/031.webp)



Lempar dadu kamu lalu masukkan angka yang muncul menggunakan kursor. Tekan tombol tengah untuk mengonfirmasi setiap input. Jika kamu salah memasukkan angka, kamu bisa kembali dan memperbaikinya. Gunakan beberapa dadu berbeda untuk mengurangi risiko dadu yang tidak seimbang. Pastikan tidak ada yang mengawasi kamu selama proses ini.


![Image](assets/fr/032.webp)



Setelah kamu memasukkan 50 lemparan, SeedSigner akan menghasilkan kalimat Anda. **Ikuti instruksi dalam tutorial ini dengan seksama jika Anda baru memulai:**



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.4 Menampilkan dan menyimpan seed



Tuliskan kata-kata seedphrase kamu dengan hati-hati pada penyangga fisik yang sesuai (kertas atau logam).



![Image](assets/fr/033.webp)



### 5.5 Memeriksa cadangan



Untuk menghindari kesalahan pencadangan, SeedSigner meminta kamu untuk memverifikasi pencadangan Anda. Klik pada `Verifikasi`.



![Image](assets/fr/034.webp)



Kemudian masukkan kata yang diminta sesuai dengan urutannya dalam kalimat. Sebagai contoh, di sini kamu harus memilih kata ketiga dalam kalimat saya.



![Image](assets/fr/035.webp)



Kalau kamu membuat kesalahan, SeedSigner akan memberi tahu kamu dan kamu harus mulai lagi dari awal. Pastikan kamu mencatat seedphrase kamu saat sudah ditampilkan. Langkah verifikasi ini memastikan bahwa cadangan kamu benar dan lengkap. Setelah berhasil divalidasi, layar akan menampilkan `Backup Verified`.



![Image](assets/fr/036.webp)



Untuk uji pemulihan yang lebih lengkap, kamu bisa mengikuti tutorial berikut:

https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 5.6 Memahami konsep “perangkat tanpa status”

SeedSigner adalah perangkat tanpa memori permanen. Artinya, seed kamu tidak pernah disimpan di perangkat (berbeda dengan Ledger, Trezor, atau Coldcard). Saat kamu mematikan perangkat, seed langsung hilang dari RAM. Ketika dinyalakan lagi, SeedSigner kembali dalam kondisi kosong: kamu harus memasukkan seed lagi untuk bisa menandatangani transaksi.

Model ini memberi perlindungan penting. Walaupun SeedSigner berbasis Raspberry Pi Zero yang tidak punya perlindungan fisik seperti *Secure Element*, tidak ada data sensitif yang tersimpan. Jadi meskipun perangkat secara fisik dikompromikan, penyerang tidak bisa mengekstrak private key atau mengakses bitcoin kamu.

Di sisi lain, arsitektur ini berarti kamu punya tanggung jawab lebih besar: tanpa cadangan, dana kamu pasti hilang. Karena itu aku sarankan **cadangan ganda**. Kamu sudah punya frasa pemulihan sebagai cadangan utama jangka panjang yang disimpan di tempat aman. Sekarang kita buat salinannya dalam bentuk **kode QR**.

Setiap kali kamu memakai SeedSigner, kamu memindai kode QR itu dengan kamera perangkat agar seed kamu dimuat sementara ke memori saat menandatangani transaksi. Cadangan kedua ini untuk penggunaan sehari-hari, tapi tetap harus dijaga dengan hati-hati: siapa pun yang punya kode QR itu bisa mengakses bitcoin kamu.

Aku juga menyarankan menyimpan kode QR dan seedphrase di dua lokasi terpisah supaya tidak hilang bersamaan kalau terjadi sesuatu.

Alternatif yang lebih canggih dan aman adalah memakai SeedSigner bersama **SeedKeeper**, yang menyimpan seed di dalam secure element. Untuk detailnya, lihat tutorial ini:

https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

### 5.7 Menulis fingerprint master key

Setelah verifikasi selesai, SeedSigner akan menampilkan fingerprint dari master key wallet kamu. Fingerprint ini mengidentifikasi wallet kamu dan memastikan kamu memakai seed yang benar di masa depan. Fingerprint ini tidak mengungkap apa pun tentang private key, jadi aman disimpan secara digital. Pastikan kamu menyimpan salinannya dan jangan sampai hilang.


![Image](assets/fr/037.webp)



Pada tahap ini kamu juga bisa menambahkan **passphrase BIP39** untuk memperkuat keamanan wallet kamu. Bergantung pada strategi pencadangan yang kamu pakai, opsi ini bisa bermanfaat, tetapi juga punya risiko: kalau kamu kehilangan passphrase, akses ke bitcoin kamu juga hilang permanen.

https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Kalau kamu belum familiar dengan konsep passphrase, aku sarankan membaca tutorial lengkap tentang topik ini:



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

![Image](assets/fr/038.webp)



### 5.8 Menyimpan seed dalam format QR (*SeedQR*)



SeedSigner memungkinkan kamu mengonversi seed menjadi kode QR kertas yang disebut *SeedQR*. Metode ini mempermudah pemuatan ulang wallet karena kamu tidak perlu mengetik ulang setiap kata secara manual.

Untuk melakukannya, kamu butuh kertas kosong atau media QR logam yang sesuai dengan panjang seedphrase kamu. Kalau kamu membeli paket lengkap SeedSigner, biasanya template sudah disertakan. Kalau tidak, kamu bisa mengunduh dan mencetaknya, atau menyalinnya dengan tangan, melalui tautan berikut:



- [Format 12 kata](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)
- [Format 24 kata](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_29x29.pdf)
- [Format ringkas 12 kata](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_21x21.pdf)
- [Format ringkas 24 kata](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)



Dari layar seed, pilih `Backup Seed`.



![Image](assets/fr/039.webp)



Kemudian pilih `Export as SeedQR`.



![Image](assets/fr/040.webp)



Kemudian, pilih format yang diinginkan (normal atau compact) menurut templat kertas yang tersedia.



![Image](assets/fr/041.webp)



Klik `Mulai` untuk mulai membuat *SeedQR*. SeedSigner kemudian akan menampilkan serangkaian kisi-kisi (A1, A2, B1, dll.), masing-masing sesuai dengan bagian dari kode.



![Image](assets/fr/042.webp)



Dengan hati-hati mereproduksi setiap titik hitam pada lembar penyimpanan, lalu gunakan joystick untuk beralih ke blok berikutnya. Luangkan waktu Anda: ketidaksejajaran yang sederhana dapat membuat kode QR tidak dapat digunakan.



Beberapa tips:




- Mulailah dengan pensil agar kamu bisa memperbaiki kesalahan, kemudian kembali menggunakan pena hitam yang halus setelah Anda selesai;
- Satu titik yang terpusat dengan baik di tengah-tengah kotak, itulah yang kamu perlukan, tidak perlu mengisinya secara penuh.



![Image](assets/fr/043.webp)



Kemudian klik `Konfirmasi SeedQR`, dan pindai kode QR kamu untuk memeriksa apakah kode tersebut berfungsi dengan benar.



![Image](assets/fr/044.webp)



Jika pesan `Sukses` ditampilkan, *SeedQR* kamu valid: Anda dapat melanjutkan ke langkah berikutnya.



![Image](assets/fr/045.webp)



**Simpan lembar ini sama ketatnya seperti kamu menyimpan seedphrase. Siapa pun yang punya kode QR ini bisa merekonstruksi private key kamu dan mencuri bitcoin kamu.**

Selamat, wallet Bitcoin kamu sekarang sudah aktif! Sekarang kita impor komponen publiknya ke **Sparrow Wallet** supaya lebih mudah dikelola.

## 6. Impor wallet ke Sparrow

Setelah SeedSigner kamu siap dan seed sudah dibuat serta disimpan dengan benar, langkah berikutnya adalah menghubungkan wallet ini ke software manajemen seperti Sparrow Wallet. Seed kamu akan tetap offline, karena yang dikirim ke Sparrow hanya bagian publiknya saja. Ini memungkinkan software menampilkan alamat, transaksi, dan membuat transaksi baru tanpa bisa mengakses dana secara langsung. Untuk membelanjakan bitcoin, SeedSigner tetap harus menandatangani transaksi yang sudah disiapkan oleh Sparrow.

### 6.1 Mempersiapkan penandatangan seed

Masukkan microSD yang berisi sistem operasi, nyalakan SeedSigner, lalu muat seed yang sudah kamu buat dari kode QR cadangan. Di layar utama, pilih `Scan`, lalu pindai SeedQR kamu dengan kamera SeedSigner.


![Image](assets/fr/046.webp)



Periksa apakah sidik jari pada kunci utama kamu cocok dengan sidik jari pada wallet. Jika kamu menggunakan passphrase, masukkan sidik jari pada tahap ini.



![Image](assets/fr/047.webp)



Ini akan membawa kamu ke menu untuk portofolio, dalam kasusku, bernama `d4149b27`. Jika kamu kembali ke layar beranda, pilih `Seeds`, lalu pilih cetakan yang sesuai dengan portofolio kamu. Kemudian klik `Export Xpub`.



![Image](assets/fr/048.webp)



Pilih jenis portofolio. Dalam kasus kami, ini adalah portofolio tunggal: pilih `Single Sig`.



![Image](assets/fr/049.webp)



Berikutnya adalah pilihan standar skrip. Yang terbaru dan paling ekonomis dari segi biaya transaksi adalah `Taproot`. Oleh karena itu, aku menyarankanmu untuk memilih standar ini.



![Image](assets/fr/050.webp)



Sebuah pesan peringatan akan muncul. Ini normal: extended public key (`xpub`) ini memungkinkan kamu melihat semua alamat yang diturunkan dari seed kamu (di akun pertama). Key ini tidak memberi izin untuk membelanjakan dana, tetapi mengungkap struktur wallet kamu. Kalau bocor, dampaknya ke privasi, bukan ke keamanan dana: orang bisa melihat aktivitas kamu, tapi tidak bisa membelanjakan bitcoin kamu.

Klik `I Understand`, lalu `Export Xpub` jika kamu sudah yakin dengan informasi yang ditampilkan.

SeedSigner kemudian akan menghasilkan xpub dalam bentuk kode QR dinamis yang berisi semua data yang diperlukan untuk mengelola wallet kamu di Sparrow Wallet.


![Image](assets/fr/051.webp)



Kamu bisa menggunakan joystick untuk mengatur kecerahan layar supaya kode QR lebih mudah dipindai.

### 6.2 Mengimpor wallet baru ke Sparrow Wallet

Pastikan kamu sudah menginstal Sparrow Wallet di komputer kamu. Kalau belum tahu cara mengunduh, memverifikasi, dan menginstalnya dengan benar, kamu bisa lihat tutorial lengkap berikut:

https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Di komputer, buka Sparrow Wallet lalu pada menu bar klik `File → Import Wallet`.

![Image](assets/fr/052.webp)



Gulir ke bawah ke `SeedSigner`, lalu pilih `Scan...`. Webcam kamu akan terbuka: pindai kode QR dinamis yang ditampilkan pada layar SeedSigner Anda.



![Image](assets/fr/053.webp)



Beri nama wallet kamu, lalu klik `Create Wallet`. Sparrow kemudian akan meminta kamu membuat password untuk mengunci akses lokal ke wallet ini.

Pilih password yang kuat, karena password ini melindungi akses ke data wallet kamu di Sparrow, seperti public key, alamat, label, dan riwayat transaksi. Password ini tidak diperlukan untuk memulihkan wallet di kemudian hari: yang kamu butuhkan hanyalah seedphrase kamu dan, kalau ada, passphrase kamu.

Aku sarankan kamu menyimpan password ini di password manager supaya tidak hilang.


![Image](assets/fr/054.webp)



Sekarang keystore kamu telah berhasil diimpor.



![Image](assets/fr/055.webp)



Lalu periksa apakah `master fingerprint` yang ditampilkan di Sparrow cocok dengan yang sudah kamu catat sebelumnya di SeedSigner.

Kalau sudah cocok, berarti SeedSigner dan Sparrow Wallet kamu sudah terhubung dengan aman. Sparrow berfungsi sebagai antarmuka untuk mengelola wallet, sementara SeedSigner tetap menjadi satu-satunya perangkat yang bisa menandatangani transaksi. Sekarang kamu sudah siap menerima dan mengirim bitcoin dengan konfigurasi yang benar-benar tetap offline.


## 7. Menerima dan mengirim bitcoin



SeedSigner dan Sparrow Wallet kamu sekarang telah dikonfigurasikan untuk bekerja bersama. Pada bagian terakhir ini, kita akan melihat bagaimana cara menerima dan mengirim bitcoin menggunakan konfigurasi ini.



### 7.1 Menerima bitcoin



#### 7.1.1 Membuat alamat penerimaan



Pada komputer kamu, buka Sparrow Wallet dan buka kunci SeedSigner wallet menggunakan kata sandi. Pastikan perangkat lunak terhubung ke server (lekukan di kanan bawah). Pada bilah sisi, klik pada `Terima`.



![Image](assets/fr/056.webp)



Alamat Bitcoin baru sekarang ditampilkan. Kamu akan melihat:

- Alamat dalam bentuk teks (biasanya dimulai dengan `bc1p...` kalau kamu pakai P2TR seperti yang aku contohkan),
- Kode QR yang sesuai,
- Kolom `Label` untuk melacak transaksi kamu.

Aku sangat menyarankan kamu menambahkan label pada setiap penerimaan bitcoin di wallet kamu. Ini memudahkan kamu mengidentifikasi asal setiap UTXO dan membantu menjaga privasi dengan lebih baik. Untuk belajar lebih dalam soal topik penting ini, kamu bisa lihat pelatihan khusus di Plan ₿ Academy:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Untuk menambahkan label, cukup masukkan nama di bidang `Label`, lalu konfirmasikan.



Sebagai contoh:



```txt
Label : Sale of the Raspberry Pi Zero
```



Alamat kamu sekarang dikaitkan dengan label ini di semua bagian Sparrow.



![Image](assets/fr/057.webp)



#### 7.1.2 Verifikasi Address pada SeedSigner


Sebelum kamu membagikan alamat penerima, pastikan dulu bahwa alamat itu memang berasal dari seed kamu. Langkah ini memastikan SeedSigner tetap bisa menandatangani transaksi yang terkait dengan alamat tersebut. Ini juga melindungi kamu dari potensi serangan ketika Sparrow menampilkan alamat palsu.

Ingat, Sparrow berjalan di komputer yang bukan lingkungan aman dan punya permukaan serangan lebih besar dibandingkan SeedSigner yang benar-benar terisolasi. Jadi jangan langsung percaya alamat yang muncul di Sparrow sebelum kamu memverifikasinya lewat hardware wallet kamu sendiri.

Pada Sparrow, klik pada kode QR alamat untuk memperbesarnya: kode tersebut akan ditampilkan dalam layar penuh.



![Image](assets/fr/058.webp)



Pada SeedSigner kamu, dari menu utama, pilih `Pindai`. Pindai kode QR yang ditampilkan di layar komputer, lalu pilih seed yang sesuai dengan wallet kamu (dalam kasus saya, sidik jari `d4149b27`).



![Image](assets/fr/059.webp)



Jika alamat yang dipindai cocok dengan alamat yang berasal dari seed kamu, layar SeedSigner akan menampilkan pesan: `Address Terverifikasi`.



![Image](assets/fr/060.webp)



Hal ini mengonfirmasi bahwa alamat tersebut adalah milik wallet dan kamu bisa menerima bitcoin darinya.



#### 7.1.3 Penerimaan dana



Sekarang kamu dapat menyampaikan alamat ini (dalam bentuk teks atau kode QR) kepada orang atau departemen yang perlu mengirimi kamu satss. Setelah transaksi disiarkan di jaringan, transaksi tersebut akan muncul di tab `Transactions` pada Sparrow Wallet.



![Image](assets/fr/061.webp)



### 7.2 Kirim bitcoin



Mengirim bitcoin dengan SeedSigner adalah proses 3 langkah:




- Pembuatan transaksi di Sparrow ;
- Tanda tangan transaksi pada SeedSigner ;
- Distribusi akhir transaksi melalui Sparrow.



Semua pertukaran antara kedua perangkat dilakukan secara eksklusif menggunakan kode QR.



#### 7.2.1 Membuat transaksi di Sparrow



Pada Sparrow Wallet, kamu dapat mengklik tab `Send` pada bilah sisi kiri. Namun demikian, saya lebih suka menggunakan tab `UTXOs`, yang memungkinkan kamu mempraktikkan "*Coin Control*". Metode ini memberi kamu kendali yang tepat atas UTXO yang digunakan, sehingga kamu bisa mengendalikan informasi yang kamu ungkapkan selama transaksi.



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



Nyalakan SeedSigner kamu dan pindai SeedQR untuk membuka wallet kamu, seperti biasa. Dari layar utama, pilih `Scan`, lalu pindai kode QR yang ditampilkan di Sparrow.


![Image](assets/fr/066.webp)



Kemudian pilih seed yang sesuai dengan portofolio kamu.



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



Transaksi kamu sekarang telah dikirim ke jaringan Bitcoin. Kamu dapat mengikuti perkembangannya di tab `Transaksi` pada Sparrow Wallet.



![Image](assets/fr/073.webp)



Sekarang kamu telah menguasai dasar-dasar penggunaan SeedSigner. Untuk memperdalam pengetahuan kamu dan menjelajahi penggunaan yang lebih lanjut, aku mengajakmu untuk membaca tutorial berikut ini:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

**[Anda juga dapat mendukung pengembangan proyek sumber terbuka SeedSigner dengan memberikan donasi dalam bentuk bitcoin!](https://seedsigner.com/donate/)**




*Kredit: beberapa gambar dalam tutorial ini berasal dari [situs web resmi proyek SeedSigner](https://seedsigner.com/) dan [repositori GitHub](https://github.com/SeedSigner/seedsigner).*
