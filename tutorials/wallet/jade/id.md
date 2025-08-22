---
name: Jade

description: Cara menyiapkan perangkat JADE kamu
---

![image](assets/cover.webp)

## Video Tutorial

![video](https://www.youtube.com/watch?v=_U1jsTeqbTw)
Blockstream Jade - Mobile Bitcoin Hardware Wallet FULL TUTORIAL oleh BTCsession

## Panduan Penulisan Lengkap

![image](assets/cover2.webp)

### Prasyarat

1. Unduh versi terbaru Blockstream Green.

2. Pasang driver ini untuk memastikan Jade dikenali oleh komputermu.

### Pengaturan Desktop

![full guide](https://youtu.be/0fPVzsyL360)

Buka Blockstream Green, kemudian klik logo Blockstream di bawah Devices.

![image](assets/1.webp)

Hubungkan Jade ke desktop kamu dengan kabel USB yang sudah disediakan.

> Catatan: Kalau Jade nggak dikenali komputer kamu, pastikan kamu sudah mengunduh driver yang ada di panduan di sini.

Begitu Jade kamu muncul di Green, perbarui Jade dengan klik Check for updates lalu pilih versi firmware terbaru. Gunakan roda gulir atau toggle di Jade untuk konfirmasi dan lanjutkan pembaruan. Pastikan Jade kamu masih menampilkan tombol "*Initialize*", kalau nggak, kamu perlu menunggu sampai Jade selesai disiapkan dulu baru bisa memperbaruinya. Gunakan tombol kembali kalau perlu balik ke layar ini.

![image](assets/2.webp)

Setelah kamu memperbarui firmware Jade, pilih Setup Jade pada jaringan dan kebijakan keamanan yang mau kamu pakai.

> Tip: Kebijakan keamanan ada di bawah Type pada layar login yang ditunjukkan di bawah ini. Kalau kamu masih ragu mau pilih Singlesig atau Multisig Shield, silakan cek panduan kami di sini. (https://help.blockstream.com/hc/en-us/articles/4403642609433)

![image](assets/3.webp)

Selanjutnya, pilih buat dompet Baru lalu pilih 12 kata untuk menghasilkan frasa pemulihan kamu. Kalau kamu klik Advanced, bakal ada opsi frasa pemulihan 12 atau 24 kata.

![image](assets/4.webp)

Catat frasa pemulihan secara offline di kertas (atau pakai perangkat cadangan frasa pemulihan khusus buat keamanan ekstra). Setelah itu, gunakan roda atau toggle di bagian atas Jade kamu untuk memverifikasi frasa pemulihan. Langkah ini buat memastikan kamu udah nulisnya dengan benar.

![image](assets/5.webp)

Atur dan konfirmasi PIN enam digit kamu. PIN ini dipakai buat buka kunci Blockstream Jade setiap kali kamu login ke dompet.

![image](assets/6.webp)

Sekarang, pilih aja Go to Wallet di aplikasi desktop Green dan kamu bakal lihat dompet kamu terbuka di Blockstream Green. Blockstream Jade juga bakal nunjukin kalau statusnya sudah Siap! Sekarang kamu bisa langsung pakai Jade buat kirim dan terima transaksi Bitcoin.

![image](assets/7.webp)

Setelah kamu selesai pakai dompet, cabut Blockstream Jade dari perangkat. Lain kali kalau mau pakai dompet di Blockstream Jade lagi, cukup sambungkan ulang perangkat kamu dan ikuti petunjuknya.

sumber: https://help.blockstream.com/hc/en-us/articles/17478506300825

### Lampiran A - Memverifikasi file unduhan Green Wallet

Memverifikasi unduhan berarti memeriksa bahwa file yang Anda unduh tidak telah dimodifikasi sejak dirilis oleh pengembang.

Memverifikasi unduhan artinya memastikan file yang kamu unduh nggak diutak-atik sejak dirilis sama pengembang.

Kita bisa cek ini dengan memverifikasi tanda tangan (yang dibuat pakai kunci privat pengembang) bareng file unduhan dan kunci publik pengembang. Hasilnya harus TRUE waktu dicek pakai fungsi gpg --verify. Aku bakal tunjukin caranya sebentar lagi. Kalau kamu mau dalemin latar belakangnya, aku punya panduan ini.

Pertama, kita mendapatkan kunci tanda tangan:
Untuk Linux, buka terminal, dan jalankan perintah ini (kamu hanya perlu menyalin dan menempelkan teks, serta menyertakan tanda kutip):
```bash
gpg --keyserver keyserver.ubuntu.com --recv-keys "04BE BF2E 35A2 AF2F FDF1 FA5D E7F0 54AA 2E76 E792"
```

UUntuk Mac, caranya sama, cuma kamu perlu unduh dan install GPG Suite dulu.

Untuk Windows, juga sama, tapi kamu perlu unduh dan install GPG4Win terlebih dahulu.

Nanti kamu bakal dapat output yang bilang kalau kunci publik sudah berhasil diimpor.

![image](assets/9.webp)

Gambar ini punya atribut alt kosong; nama filenya image-3-1024x162.webp.

Selanjutnya, kita perlu ambil file yang berisi hash dari software. File ini ada di halaman GitHub Blockstream. Pertama, buka halaman informasinya di sini, lalu klik tautan "desktop". Itu bakal bawa kamu ke halaman rilis terbaru di GitHub, dan di sana kamu akan lihat tautan ke SHA256SUMS.asc, yaitu dokumen teks yang berisi hash yang diterbitkan Blockstream untuk program yang kita unduh.

![image](assets/10.webp)

GitHub:

![image](assets/11.webp)

Ini sebenarnya nggak wajib, tapi setelah aku simpan ke disk, aku ganti nama file "SHA256SUMS.asc" jadi "SHA256.txt" biar lebih gampang dibuka di Mac pakai editor teks.

Isi file itu kurang lebih kayak gini:

![image](assets/12.webp)

Teks yang kita cari ada di bagian atas. Tergantung file mana yang kamu unduh, nanti ada hash yang cocok untuk kita bandingkan.

Di bagian bawah dokumen ada tanda tangan yang dibuat untuk pesan di atas — jadi file ini sebenarnya dua dalam satu.

Urutannya nggak masalah, tapi sebelum ngecek hash, kita pastikan dulu kalau pesan hash asli itu memang belum diubah.

Sekarang buka terminal. Kamu harus ada di direktori tempat file SHA256SUMS.asc tadi diunduh. Kalau asumsinya kamu unduh ke folder Downloads, di Linux dan Mac masuk ke direktori itu dengan perintah (huruf besar-kecil harus sesuai):

```bash
cd Downloads
```

Tentu aja, kamu harus tekan <enter> setelah ngetik perintah itu. Kalau pakai Windows, buka CMD (Command Prompt) dan ketik perintah yang sama (cuma di Windows nggak sensitif huruf besar-kecil). Untuk Windows dan Mac, pastikan kamu udah unduh GPG4Win dan GPG Suite sesuai instruksi sebelumnya. Sementara di Linux, gpg biasanya udah langsung ada di sistem operasi.

Dari Terminal (atau CMD di Windows), ketik perintah ini:
```bash
gpg --verify SHA256SUMS.asc
```

Ejaan tepat nama file (yang ditandai merah) bisa aja beda tergantung kapan kamu ngunduhnya, jadi pastikan perintah sesuai sama nama file yang kamu punya. Kamu bakal dapat output seperti ini, dan abaikan aja peringatan soal tanda tangan yang dipercaya — itu cuma berarti kamu belum secara manual ngasih tahu komputer buat mempercayai kunci publik yang sebelumnya kita impor.

![image](assets/13.webp)

Gambar ini memiliki atribut alt yang kosong; nama filenya adalah image-4-1024x165.webp

Output ini nunjukin kalau tanda tangannya valid, jadi kita bisa yakin kunci privat dari "info@greenaddress.it" memang yang menandatangani data (laporan hash) itu. Sekarang kita perlu bikin hash dari file zip yang udah diunduh, lalu bandingin hasilnya dengan yang dipublikasikan. Di file SHA256SUMS.asc, memang ada teks kecil yang bilang "Hash: SHA512", tapi itu agak membingungkan karena isi file jelas berupa output SHA256, jadi bagian itu bisa diabaikan aja.

Untuk Mac dan Linux, buka terminal lalu arahkan ke folder tempat file zip diunduh (mungkin kamu perlu ketik cd Downloads lagi, kecuali terminalnya belum ditutup). Buat ngecek posisi kamu sekarang di direktori mana, cukup ketik pwd (print working directory). Kalau hal-hal ini masih terasa asing, ada baiknya tonton video singkat di YouTube dengan cari "cara menavigasi sistem file Linux/Mac/Windows".

Untuk meng-hash file, ketik ini:

```bash
shasum -a 256 BlockstreamGreen_MacOS_x86_64.zip
```

Kamu perlu pastiin dulu nama file kamu yang tepat, lalu ubah bagian teks berwarna biru di atas sesuai dengan nama file itu.

Nanti kamu bakal dapat output seperti ini (punyamu mungkin beda kalau filenya nggak sama persis dengan punyaku):

![image](assets/14.webp)

Selanjutnya, bandingin secara visual output hash dengan yang ada di file SHA256SUMS.asc. Kalau hasilnya cocok, berarti --> SUKSES! Selamat!

sumber: https://armantheparman.com/jade/

### Menggunakannya di Sparrow

Kalau kamu udah familiar pakai Sparrow, maka caranya sama aja seperti biasa:

> Catatan: prosesnya mirip dengan Specter, misalnya.

Unduh Sparrow lewat tautan yang disediakan di sini.

![image](assets/14.5.webp)

Klik Next untuk ikutin panduan pengaturan dan pelajari berbagai opsi koneksi.

![image](assets/15.webp)

Pilih server yang kamu mau, lalu pilih Create New Wallet.

![image](assets/16.webp)

Masukkan nama untuk dompet kamu, lalu klik Create Wallet.

![image](assets/17.webp)

Pilih kebijakan dan jenis skrip yang kamu mau, lalu pilih Connected Hardware Wallet.

> Catatan: Kalau sebelumnya kamu udah pakai Blockstream Jade sebagai dompet Singlesig di Blockstream Green dan mau lihat transaksinya di Sparrow, pastiin jenis skripnya sama dengan tipe akun yang nyimpen dana kamu di Green. Kamu juga perlu pastiin jalur derivasinya cocok.

![image](assets/18.webp)

Colokkan Blockstream Jade kamu, lalu klik Scan. Kamu bakal diminta masukin PIN di Jade.

> Tip: Sebelum sambungin Jade, pastiin aplikasi Blockstream Green nggak terbuka. Kalau Green terbuka, kadang bisa bikin Sparrow nggak deteksi Jade dengan benar..

![image](assets/19.webp)

Pilih Import Keystore untuk impor kunci publik dari akun default, atau klik panah untuk pilih jalur derivasi secara manual yang mau kamu pakai.

![image](assets/20.webp)

Setelah kunci yang diinginkan telah diimpor, klik Apply.

![image](assets/21.webp)

Anda sekarang telah berhasil mengatur dompet Anda dan Anda dapat mulai menerima, menyimpan, dan menghabiskan bitcoin Anda menggunakan Sparrow dan Blockstream Jade.

> Catatan: Kalau sebelumnya kamu pakai Jade dengan Blockstream Green sebagai dompet Multisig Shield, jangan berharap dompet Sparrow baru kamu nunjukin saldo yang sama — ini dompet yang berbeda. Buat akses dompet Multisig Shield kamu lagi, cukup sambungkan ulang Jade ke Blockstream Green.

![image](assets/22.webp)

sumber: https://help.blockstream.com/hc/en-us/articles/7559912660761-How-do-I-use-Blockstream-Jade-with-Sparrow-

### aplikasi green
Jika kamu lebih banyak menggunakan panduan mobile, kamu bisa menggunakannya dengan Blockstream Green
- Cara mengatur Blockstream Jade dengan Green | Blockstream Jade - https://youtu.be/7aacxnc6DHg

- Cara menerima bitcoin ke dompet Jade | Blockstream Jade - https://youtu.be/CVtcDdiPqLA
