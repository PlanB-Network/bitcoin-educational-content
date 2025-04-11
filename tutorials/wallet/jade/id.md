---
name: Jade

description: Cara menyiapkan perangkat JADE Anda
---

![image](assets/cover.webp)

## Video Tutorial

![video](https://www.youtube.com/watch?v=_U1jsTeqbTw)
Blockstream Jade - Mobile Bitcoin Hardware Wallet FULL TUTORIAL oleh BTCsession

## Panduan Penulisan Lengkap

![image](assets/cover2.webp)

### Prasyarat

1. Unduh versi terbaru dari Blockstream Green.

2. Pasang driver ini untuk memastikan Jade dikenali oleh komputer Anda.

### Pengaturan Desktop

![full guide](https://youtu.be/0fPVzsyL360)

Buka Blockstream Green, kemudian klik logo Blockstream di bawah Devices.

![image](assets/1.webp)

Hubungkan Jade ke desktop Anda menggunakan kabel USB yang disediakan.

> Catatan: Jika Jade tidak dikenali oleh komputer Anda, pastikan untuk mengunduh driver yang ditemukan dalam panduan di sini.

Setelah Jade Anda muncul di Green, perbarui Jade dengan mengklik Check for updates dan pilih versi firmware terbaru. Gunakan roda gulir atau toggle pada Jade untuk mengonfirmasi dan melanjutkan dengan pembaruan. Pastikan Jade Anda masih menampilkan tombol "Initialize", jika tidak, Anda harus menunggu setelah menyiapkan Jade untuk memperbaruinya. Gunakan tombol kembali untuk kembali ke layar ini jika perlu.

![image](assets/2.webp)

Setelah Anda memperbarui firmware Jade, pilih Setup Jade pada jaringan dan kebijakan keamanan yang ingin Anda gunakan.

> Tip: Kebijakan keamanan tercantum di bawah Type pada layar login yang ditunjukkan di bawah ini. Jika Anda tidak yakin apakah akan memilih Singlesig atau Multisig Shield, silakan tinjau panduan kami di sini. (https://help.blockstream.com/hc/en-us/articles/4403642609433)

![image](assets/3.webp)

Selanjutnya, pilih untuk membuat dompet Baru dan pilih 12 kata untuk menghasilkan frasa pemulihan Anda. Mengklik Advanced akan memberi Anda opsi frasa pemulihan 12 dan 24 kata.

![image](assets/4.webp)

Catat frasa pemulihan secara offline di atas kertas (atau dengan menggunakan perangkat cadangan frasa pemulihan khusus untuk keamanan ekstra). Kemudian, gunakan roda atau toggle di bagian atas Jade Anda untuk memverifikasi frasa pemulihan Anda. Langkah ini memastikan Anda telah menuliskannya dengan benar.

![image](assets/5.webp)

Tetapkan dan konfirmasi PIN enam digit Anda. Ini digunakan untuk membuka kunci Blockstream Jade setiap kali Anda login ke dompet Anda.

![image](assets/6.webp)

Sekarang, cukup pilih Go to Wallet pada aplikasi desktop Green dan Anda akan melihat dompet Anda terbuka di Blockstream Green. Blockstream Jade juga akan menunjukkan bahwa itu sudah Siap! Anda sekarang dapat menggunakan Jade Anda untuk mengirim dan menerima transaksi Bitcoin.

![image](assets/7.webp)

Setelah Anda selesai menggunakan dompet Anda, putuskan sambungan Blockstream Jade Anda dari perangkat. Kali berikutnya Anda ingin menggunakan dompet di Blockstream Jade, cukup hubungkan kembali perangkat Anda dan ikuti petunjuknya.

sumber: https://help.blockstream.com/hc/en-us/articles/17478506300825

### Lampiran A - Memverifikasi file unduhan Green Wallet

Memverifikasi unduhan berarti memeriksa bahwa file yang Anda unduh tidak telah dimodifikasi sejak dirilis oleh pengembang.

Kita melakukan ini dengan memeriksa bahwa tanda tangan (yang dihasilkan oleh kunci pribadi pengembang) bersama dengan file yang diunduh dan kunci publik pengembang menghasilkan hasil TRUE ketika melewati fungsi gpg –verify. Saya akan menunjukkan cara melakukannya selanjutnya. Jika Anda ingin mempelajari latar belakangnya, saya memiliki panduan ini dan ini.

Pertama, kita mendapatkan kunci tanda tangan:
Untuk Linux, buka terminal, dan jalankan perintah ini (Anda hanya perlu menyalin dan menempelkan teks, serta menyertakan tanda kutip):
```bash
gpg --keyserver keyserver.ubuntu.com --recv-keys "04BE BF2E 35A2 AF2F FDF1 FA5D E7F0 54AA 2E76 E792"
```

Untuk Mac, lakukan hal yang sama, kecuali Anda perlu mengunduh dan menginstal GPG Suite terlebih dahulu.

Untuk Windows, lakukan hal yang sama, kecuali Anda perlu mengunduh dan menginstal GPG4Win terlebih dahulu.

Anda akan mendapatkan output yang mengatakan kunci publik telah diimpor.

![image](assets/9.webp)

Gambar ini memiliki atribut alt yang kosong; nama filenya adalah image-3-1024x162.webp

Selanjutnya, kita perlu mendapatkan file yang berisi hash dari perangkat lunak. Ini disimpan di halaman GitHub Blockstream. Pertama, kunjungi halaman informasi mereka di sini, dan klik pada tautan untuk "desktop". Ini akan membawa Anda ke halaman rilis terbaru di GitHub dan di sana Anda akan melihat tautan ke file SHA256SUMS.asc, yang merupakan dokumen teks yang berisi hash yang diterbitkan Blockstream dari program yang kita unduh.

![image](assets/10.webp)

GitHub:

![image](assets/11.webp)

Ini tidak perlu, tetapi setelah menyimpan ke disk, saya mengganti nama "SHA256SUMS.asc" menjadi "SHA256.txt" untuk lebih mudah membuka file di Mac menggunakan editor teks. Ini adalah isi dari file tersebut:

![image](assets/12.webp)

Teks yang kita cari ada di bagian atas. Tergantung pada file mana yang kita unduh, ada output hash yang sesuai yang akan kita bandingkan nanti.

Bagian bawah dari dokumen berisi tanda tangan yang dibuat pada pesan di atas – ini adalah file dua dalam satu.

Urutannya tidak penting, tetapi sebelum memeriksa hash, kita akan memeriksa bahwa pesan hash asli (yaitu tidak telah diubah).

Buka terminal. Anda perlu berada di direktori yang benar di mana file SHA256SUMS.asc diunduh. Dengan asumsi Anda mengunduhnya ke direktori "Downloads", untuk Linux dan Mac, ubah ke direktori seperti ini (case sensitive):

```bash
cd Downloads
```

Tentu saja, Anda harus menekan <enter> setelah perintah ini. Untuk Windows, buka CMD (command prompt), dan ketik hal yang sama (meskipun tidak case sensitive).

Untuk Windows dan Mac, Anda perlu telah mengunduh GPG4Win dan GPG Suite, masing-masing, seperti yang diinstruksikan sebelumnya. Untuk Linux, gpg datang dengan Sistem Operasi. Dari Terminal (atau CMD untuk Windows), ketik perintah ini:

```bash
gpg --verify SHA256SUMS.asc
```

Ejaan tepat dari nama file (dalam merah) mungkin berbeda pada hari Anda mengambil file, jadi pastikan perintah cocok dengan nama file seperti yang diunduh. Anda seharusnya mendapatkan output ini, dan abaikan peringatan tentang tanda tangan yang dipercaya – itu hanya berarti Anda belum secara manual memberi tahu komputer bahwa Anda mempercayai kunci publik yang kita impor sebelumnya.

![image](assets/13.webp)

Gambar ini memiliki atribut alt yang kosong; nama filenya adalah image-4-1024x165.webp

Output ini mengonfirmasi tanda tangan itu baik, dan kita dapat yakin kunci pribadi dari "info@greenaddress.it" telah menandatangani data (laporan hash).
Sekarang kita harus meng-hash file zip yang telah diunduh dan membandingkan outputnya seperti yang dipublikasikan. Perhatikan bahwa dalam file SHA256SUMS.asc, ada sedikit teks yang mengatakan "Hash: SHA512" yang membuat saya bingung, karena file tersebut jelas memiliki output SHA256 di dalamnya, jadi saya akan mengabaikan itu.

Untuk Mac dan Linux, buka terminal, navigasikan ke tempat file zip diunduh (mungkin Anda perlu mengetik "cd Downloads" lagi, kecuali Anda belum menutup terminal sejak itu). Ngomong-ngomong, Anda selalu dapat memeriksa direktori mana Anda berada dengan mengetik PWD ("print working directory), dan jika ini semua asing, sangat berguna untuk menonton video YouTube singkat dengan mencari "cara menavigasi sistem file Linux/Mac/Windows".

Untuk meng-hash file, ketik ini:

```bash
shasum -a 256 BlockstreamGreen_MacOS_x86_64.zip
```

Anda harus memeriksa apa nama file Anda secara tepat, dan memodifikasi teks dalam biru di atas jika diperlukan.

Anda akan mendapatkan output seperti ini (milik Anda akan berbeda jika file berbeda dengan milik saya):

![image](assets/14.webp)

Selanjutnya, bandingkan secara visual output hash dengan apa yang ada di file SHA256SUMS.asc. Jika mereka cocok, maka --> SUKSES! Selamat.

sumber: https://armantheparman.com/jade/

### Menggunakannya di Sparrow

Jika Anda sudah tahu cara menggunakan Sparrow maka seperti biasa:

> Catatan: prosesnya sama dengan Specter misalnya

Unduh Sparrow menggunakan tautan yang disediakan di sini.

![image](assets/14.5.webp)

Klik Next untuk mengikuti panduan pengaturan untuk mempelajari tentang berbagai opsi koneksi.

![image](assets/15.webp)

Pilih server yang Anda inginkan kemudian pilih Create New Wallet.

![image](assets/16.webp)

Masukkan nama untuk dompet Anda dan klik Create Wallet.

![image](assets/17.webp)

Pilih kebijakan dan jenis skrip yang Anda inginkan kemudian pilih Connected Hardware Wallet.

> Catatan: Jika Anda sebelumnya telah menggunakan Blockstream Jade sebagai dompet Singlesig dengan Blockstream Green dan ingin melihat transaksi Anda di Sparrow, pastikan jenis skrip cocok dengan tipe akun yang berisi dana Anda di Green. Anda juga perlu agar jalur derivasi cocok.

![image](assets/18.webp)

Colokkan Blockstream Jade Anda dan klik Scan. Anda kemudian akan diminta untuk memasukkan PIN Anda di Jade.

> Tip: Sebelum menghubungkan Jade Anda, pastikan aplikasi Blockstream Green tidak terbuka. Jika Green terbuka, ini dapat menyebabkan masalah dengan deteksi Jade Anda dalam Sparrow.

![image](assets/19.webp)

Pilih Import Keystore untuk mengimpor kunci publik dari akun default, atau pilih panah untuk secara manual memilih jalur derivasi yang ingin Anda gunakan.

![image](assets/20.webp)

Setelah kunci yang diinginkan telah diimpor, klik Apply.

![image](assets/21.webp)

Anda sekarang telah berhasil mengatur dompet Anda dan Anda dapat mulai menerima, menyimpan, dan menghabiskan bitcoin Anda menggunakan Sparrow dan Blockstream Jade.

> Catatan: Jika Anda sebelumnya menggunakan Jade dengan Blockstream Green sebagai dompet Multisig Shield, Anda tidak seharusnya mengharapkan dompet Sparrow baru Anda menunjukkan saldo yang sama - ini adalah dompet yang berbeda. Untuk mengakses dompet Multisig Shield Anda lagi, cukup hubungkan kembali Jade Anda ke Blockstream Green.

![image](assets/22.webp)

sumber: https://help.blockstream.com/hc/en-us/articles/7559912660761-How-do-I-use-Blockstream-Jade-with-Sparrow-

### aplikasi green
Jika Anda lebih banyak menggunakan panduan mobile, Anda bisa menggunakannya dengan Blockstream Green
- Cara mengatur Blockstream Jade dengan Green | Blockstream Jade - https://youtu.be/7aacxnc6DHg

- Cara menerima bitcoin ke dompet Jade | Blockstream Jade - https://youtu.be/CVtcDdiPqLA