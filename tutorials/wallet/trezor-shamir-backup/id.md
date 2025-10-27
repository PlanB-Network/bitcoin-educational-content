---
name: Cadangan Trezor Shamir
description: Frasa Mnemonic satu-bagi dan multi-bagi di Trezor
---
![cover](assets/cover.webp)

*Kredit gambar: [Trezor.io](https://trezor.io/)*

## Opsi pencadangan baru di Trezor

Sejak tahun 2023, Trezor mulai menawarkan format pencadangan baru yang disebut **Cadangan Satu Bagian (Single Share Backup),** yang secara bertahap menggantikan metode klasik berbasis BIP39 yang umum digunakan di banyak wallet. Berbeda dari seedphrase 12 atau 24 kata tradisional, format baru ini memakai frasa 20 kata tunggal yang berasal dari standar buatan SatoshiLabs, yaitu SLIP39. Tujuannya adalah untuk meningkatkan ketahanan dan keterbacaan cadangan, sambil memungkinkan migrasi yang lebih mudah ke model pencadangan terdistribusi.

Model terdistribusi ini disebut **Cadangan Multi-Bagian (Shamir Backup).** Prinsip dasarnya sama, tetapi alih-alih menghasilkan satu seedphrase, model ini membaginya menjadi beberapa fragmen yang disebut share. Setiap share sendiri merupakan frasa Mnemonic yang valid. Untuk memulihkan wallet, sejumlah share tertentu (sesuai dengan ambang batas atau threshold) perlu digabungkan kembali. Misalnya, dalam skema 3 dari 5, kamu bisa memulihkan wallet dengan 3 share dari total 5 share.

Perlu kamu tahu, sistem cadangan terdistribusi milik Trezor ini berbeda dari dompet Multisig. Untuk membelanjakan Bitcoin-mu, kamu hanya perlu hardware wallet Trezor saja. Hanya satu tanda tangan yang dibutuhkan. Mekanisme distribusi ini berlaku di level seedphrase (cadangan), bukan di level transaksi.

![Image](assets/fr/01.webp)

Sistem ini mengatasi masalah single point of failure pada seedphrase tanpa menimbulkan kerumitan seperti pada pengelolaan Multisig atau penggunaan passphrase BIP39. Proses pemulihan kini tidak lagi bergantung pada satu informasi tunggal, melainkan beberapa bagian informasi, dengan keunggulan tambahan berupa toleransi kehilangan berkat sistem ambang batas.

Kamu yang sebelumnya membuat wallet dengan Cadangan Satu Bagian (Single Share Backup) bisa beralih ke Cadangan Multi-Bagian (Multi-Share Backup) kapan saja tanpa perlu memindahkan isi wallet. Alamat dan akun penerima akan tetap sama. Sistem Multi-Share hanya memengaruhi bagian cadangan, sementara seluruh isi wallet lainnya tetap tidak berubah.

Multi-Share Backup tersedia di **Trezor Model T, Safe 3, dan Safe 5.** Fitur ini tidak didukung oleh Trezor Model One.

**Catatan penting:** Sistem Multi-Share Trezor aman secara kriptografis karena menggunakan skema Shamir’s Secret Sharing untuk proses distribusi. Sangat disarankan agar kamu tidak mencoba membuat sistem serupa secara manual, misalnya dengan membagi seedphrase klasik sendiri. Itu adalah praktik berisiko tinggi yang bisa menyebabkan pencurian atau kehilangan Bitcoin kamu. Seedphrase klasik harus selalu disimpan utuh.


## Berbagi Rahasia Shamir di SLIP39

Mekanisme kriptografi yang digunakan pada cadangan Multi-Share Trezor didasarkan pada Shamir’s Secret Sharing Scheme (SSSS). Prinsip kerjanya begini: informasi rahasia (dalam hal ini seed dari wallet) diubah menjadi sebuah polinomial matematika. Dari polinomial tersebut, beberapa titik dihitung—masing-masing titik ini menjadi satu share. Untuk memulihkan rahasia aslinya, dilakukan proses interpolasi polinomial dengan mengumpulkan jumlah share minimum sesuai ambang batas (threshold).

Tidak ada informasi rahasia yang bisa disimpulkan dari jumlah share di bawah ambang batas, sehingga keamanan informasi rahasia tetap terjaga secara teoretis. Dengan kata lain, bahkan jika penyerang memiliki kekuatan komputasi tanpa batas, mereka tetap tidak akan bisa menebak seed selama ambang batas belum terpenuhi.

SLIP39 menggunakan skema ini untuk mendistribusikan wallet seed. Setiap share terdiri dari 20 kata yang berasal dari daftar berisi 1024 kata, berbeda dengan daftar kata yang digunakan pada BIP39.

## Menyiapkan Cadangan Multi-share pada Trezor

Ketika membuat portofolio di Trezor, kamu memiliki tiga opsi berbeda:

- Gunakan frasa klasik BIP39 Mnemonic yang terdiri dari 12 atau 24 kata;
- Gunakan frasa Mnemonic satu saham (SLIP39);
- Konfigurasikan beberapa frasa Mnemonic dalam Multi-share (SLIP39).

Kalau kamu memilih seedphrase Single-Share SLIP39, kamu bisa meningkatkan ke Multi-Share nanti tanpa perlu mengatur ulang wallet-mu. Tapi kalau kamu memulai dengan wallet klasik BIP39 (frasa 12 atau 24 kata), kamu tidak bisa langsung mengonversinya ke Multi-Share. Kamu harus membuat wallet Multi-Share baru dari awal dan memindahkan dana dari wallet lama ke yang baru lewat satu atau beberapa transaksi Bitcoin. Proses ini lebih rumit dan bisa memakan biaya tambahan. Kalau kamu berencana melakukan migrasi seperti ini, disarankan untuk membeli hardware wallet Trezor baru agar kamu tidak perlu memasukkan seedphrase ke dalam perangkat lunak wallet mana pun.

Dalam tutorial ini, kita akan mulai dengan cara mengatur Multi-Share saat membuat wallet baru. Setelah itu, di bagian berikutnya, kita akan bahas cara mengonversi Single-Share menjadi Multi-Share pada wallet yang sudah ada.

Kalau kamu butuh panduan tentang cara menyiapkan perangkat Trezor dari awal, kami juga punya tutorial lengkap untuk setiap model Trezor:

https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

### Pada portofolio baru

Sekarang kamu telah menyelesaikan konfigurasi awal Trezor kamu dan siap untuk membuat portofolio. Di Trezor Suite, klik tombol "*Buat Wallet baru*".

![Image](assets/fr/02.webp)

Pilih opsi "*Cadangan Multi-Bagi*", lalu klik "*Buat Wallet*".

![Image](assets/fr/03.webp)

Terima persyaratan penggunaan di Trezor kamu dan konfirmasikan pembuatan portofolio.

![Image](assets/fr/04.webp)

Di Trezor Suite, klik "*Lanjutkan pencadangan*".

![Image](assets/fr/05.webp)

Baca instruksi dengan cermat, konfirmasikan, lalu klik "*Buat cadangan Wallet*".

![Image](assets/fr/06.webp)

Untuk informasi lebih lanjut tentang cara yang benar menyimpan dan mengelola seedphrase-mu, aku sangat menyarankan kamu untuk mengikuti tutorial lainnya, terutama jika kamu masih pemula:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Pada Trezor, pilih jumlah total saham yang ingin Anda konfigurasi. Konfigurasi yang paling umum adalah 2-de-3 dan 3-de-5. Untuk contoh ini, saya akan membuat 2-de-3, jadi saya akan memilih 3 bagian. Setiap bagian akan mewakili frasa Mnemonic yang terdiri dari 20 kata.

*Untuk pengguna Safe 5, meskipun layar akan mengatakan "*Ketuk untuk melanjutkan*", kamu harus menggeser ke atas untuk mengonfirmasi

![Image](assets/fr/07.webp)

Kemudian, konfirmasikan ambang batasnya, yaitu jumlah share yang dibutuhkan untuk memulihkan akses ke wallet dan Bitcoin yang tersimpan di dalamnya..

![Image](assets/fr/08.webp)

Trezor akan membuat beberapa share kamu (seedphrase) menggunakan generator angka acak. Pastikan kamu tidak diawasi selama proses ini. Tuliskan kata-kata yang muncul di layar ke media fisik pilihanmu. Penting untuk menomori kata-kata itu dan menjaga urutannya.

Aku sarankan kamu mencatat setiap share di media terpisah dan menyimpannya dengan hati-hati agar tidak beberapa share bisa diakses di tempat yang sama. Sebagai contoh, untuk konfigurasi 2-dari-3 seperti milikku, salah satu opsi adalah menyimpan satu salinan di rumah, satu lagi di rumah teman tepercaya, dan yang terakhir di brankas bank. Pilihan lokasi penyimpanan tergantung pada strategi keamanan pribadimu.

Kamu bisa melihat di bagian atas layar share mana yang sedang kamu lihat.

Tentu saja, kamu tidak boleh membagikan kata-kata ini di Internet, jangan lakukan itu seperti yang aku contohkan dalam tutorial ini. Wallet contoh ini hanya akan digunakan pada Testnet dan akan dihapus pada akhir tutorial.**_

![Image](assets/fr/09.webp)

Untuk berpindah ke kata berikutnya, klik bagian bawah layar. Kamu bisa kembali ke kata sebelumnya dengan menggeser ke bawah. Setelah semua kata selesai kamu tulis, tahan jari di layar untuk lanjut ke bagian berikutnya, lalu ulangi langkah yang sama.

![Image](assets/fr/10.webp)

Di akhir setiap proses pencatatan share, kamu akan diminta memilih beberapa kata dari seedphrase-mu untuk memastikan bahwa kamu sudah menuliskannya dengan benar.

![Image](assets/fr/11.webp)

Selesai! Kamu sudah berhasil mencadangkan wallet-mu menggunakan opsi Multi-Share. Sekarang kamu bisa melanjutkan ke langkah konfigurasi berikutnya.

### Pada portofolio saham tunggal yang sudah ada

Kalau kamu sudah punya Trezor Wallet dengan cadangan Single-Share (frasa SLIP39 Mnemonic, bukan frasa BIP39 klasik) dan ingin meningkatkan ketersediaan serta keamanan cadangan wallet-mu, kamu bisa mengatur sistem Multi-Share tanpa perlu mentransfer Bitcoin-mu.

Untuk melakukannya, hubungkan dan buka kunci hardware wallet-mu. Lalu di Trezor Suite, buka menu Pengaturan.

![Image](assets/fr/12.webp)

Buka tab "*Perangkat*".

![Image](assets/fr/13.webp)

Kemudian klik "*Buat Cadangan Multi-share*".

![Image](assets/fr/14.webp)

Baca petunjuknya, lalu klik "*Buat Cadangan Multi-share*".

![Image](assets/fr/15.webp)

Selanjutnya, kamu akan diminta memasukkan seedphrase kamu yang sekarang (Single-Share) langsung di layar Trezor. Pilih jumlah kata yang sesuai, biasanya 20 kata secara default.

![Image](assets/fr/16.webp)

Kemudian gunakan keyboard di layar Trezor untuk memasukkan setiap kata dari frasa Mnemonic kamu saat ini.

![Image](assets/fr/17.webp)

Anda kemudian dapat memilih konfigurasi Cadangan Multi-share Anda dengan mengikuti petunjuk yang disediakan di bagian sebelumnya.

![Image](assets/fr/18.webp)

Setelah kamu membuat Cadangan Multi-Share, kamu perlu memutuskan apa yang akan dilakukan dengan seedphrase Single-Share lamamu. Karena wallet Bitcoin-nya tetap sama, frasa tunggal itu masih bisa digunakan untuk mengakses wallet-mu. Pilihan ini tergantung pada strategi keamanan pribadimu, tapi secara umum disarankan untuk menghancurkan frasa tunggal tersebut agar tidak ada lagi satu titik kegagalan — sesuai tujuan utama dari sistem Multi-Share. Jika kamu memutuskan untuk menghancurkannya, pastikan dilakukan dengan aman, karena frasa itu masih memberi akses penuh ke Bitcoin-mu.

Selamat! Sekarang kamu sudah memahami cara kerja Single-Share dan Multi-Share Backup pada hardware wallet Trezor. Kalau kamu ingin meningkatkan keamanan wallet-mu ke tingkat berikutnya, lihat juga tutorial tentang BIP39 passphrase berikut ini:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Kalau kamu merasa tutorial ini bermanfaat, aku bakal sangat berterima kasih kalau kamu mau kasih jempol hijau di bawah ini. Jangan ragu juga buat membagikan artikel ini ke media sosialmu. Terima kasih banyak!

## Sumber daya tambahan





- [SLIP-0039: Pembagian Rahasia Shamir untuk Kode Mnemonic] (https://github.com/satoshilabs/slips/blob/master/slip-0039.md);
- [Multi-share Backup di Trezor](https://trezor.io/learn/a/multi-share-backup-on-trezor);
- [Wikipedia: Shamir's secret sharing](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing).
