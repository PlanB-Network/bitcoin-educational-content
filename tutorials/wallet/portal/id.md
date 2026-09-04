---
name: Portal
description: Mengkonfigurasi dan menggunakan Portal dompet perangkat keras TwentyTwo-Devices
---
![cover](assets/cover.webp)

Portal adalah dompet perangkat keras Bitcoin yang didesain oleh TwentyTwo Devices, sebuah perusahaan yang mengkhususkan diri dalam pembuatan dompet perangkat keras sumber terbuka untuk para pengguna Bitcoin. Didirikan oleh Alekos Filini, pencipta proyek Magical Bitcoin ([selanjutnya dinamakan BDK](https://github.com/bitcoindevkit)) dan pernah bekerja untuk Blockstream dan BHB Network, TwentyTwo Devices bertujuan untuk fokus pada otonomi pengguna, kesederhanaan dan keamanan.

Yang membedakan Portal dari dompet perangkat keras lain di pasaran adalah integrasi aslinya dengan smartphone. Dompet ini bekerja tanpa kabel atau baterai. Ia menggunakan teknologi NFC untuk menyalakan dirinya sendiri dan berkomunikasi dengan dompet seluler apa pun yang kompatibel. Desainnya yang menarik dibuat untuk penggunaan yang ergonomis. Bagian bundar ditempatkan di belakang smartphone untuk menampilkan layar di mana kamu bisa memeriksa detail transaksi sebelum menandatanganinya dengan tombol khusus.


![Image](assets/fr/01.webp)

Sepenuhnya open-source, Portal didasarkan pada firmware yang ditulis dalam bahasa Rust dan menggunakan BDK (Bitcoin Dev Kit) untuk manajemen kunci dan transaksi. Portal ini dijual dengan harga €89 [di situs web resminya](https://store.twenty-two.xyz/products/portal-hardware-wallet).

Pada saat artikel ini ditulis, Portal ini kompatibel dengan aplikasi Nunchuk dan Bitcoin Keeper. Dalam tutorial ini, kita akan mengonfigurasinya dengan Nunchuk.

## Membuka kemasan

Ketika kamu menerima Portal, periksa apakah kotak dan label yang menyegelnya dalam kondisi baik. Di dalamnya, kamu akan menemukan Portal di dalam kantong tertutup.

Pastikan segelnya masih utuh untuk memastikan kantong belum dibuka. Nomor unik yang ditampilkan dalam huruf besar pada kantong harus sesuai dengan nomor yang tertulis dalam warna hitam di bawah segel biru, nomor yang tertera pada label kotak, dan nomor yang akan muncul di layar saat pertama kali menyalakannya.

![Image](assets/fr/02.webp)

## Instalasi Nunchuk

Untuk mengelola dompet yang dihosting di Portal, kita akan menggunakan aplikasi Nunchuk. Unduh aplikasi ini dari [Google Play Store](https://play.google.com/store/apps/details?id=io.nunchuk.android), [App Store](https://apps.apple.com/us/app/nunchuk-bitcoin-wallet/id1563190073) atau secara langsung melalui [file `.apk`](https://github.com/nunchuk-io/nunchuk-android/releases).

![Image](assets/fr/03.webp)

Jika kamu menggunakan Nunchuk untuk pertama kalinya, aplikasi ini akan meminta kamu membuat akun. Untuk keperluan tutorial ini, kamu tidak perlu membuat akun. Pilih "*Lanjutkan sebagai tamu*" untuk melanjutkan tanpa akun.

![Image](assets/fr/04.webp)

## Konfigurasi portal

Pada layar beranda Nunchuk, klik logo "*NFC*" di bagian atas layar.

![Image](assets/fr/05.webp)

Posisikan Portal kamu di bagian belakang ponsel cerdas kamu untuk mengaktifkannya.

![Image](assets/fr/06.webp)

Nunchuk akan mengenali Portal kamu. Kemudian klik "*Lanjutkan*".

![Image](assets/fr/07.webp)

Untuk membuat portofolio baru, pilih "*Generate seed on Portal*" lalu klik "*Lanjutkan*".

![Image](assets/fr/08.webp)

Kamu dapat memilih antara frasa mnemonik 12 atau 24 kata. Keamanan yang ditawarkan oleh kedua opsi ini serupa, jadi kamu bisa memilih yang paling mudah disimpan, yaitu 12 kata.

![Image](assets/fr/09.webp)

Kamu kemudian akan diminta untuk memilih kata sandi. Kata sandi ini akan membuka kunci Portal. Oleh karena itu, kata sandi memberikan perlindungan terhadap akses fisik yang tidak sah. Kata sandi ini tidak terlibat dalam proses penurunan kunci kriptografi dompet. Jadi, bahkan tanpa kata sandi ini, kepemilikan frasa mnemonik 12 atau 24 kata tetap memungkinkan kamu mendapatkan kembali akses ke bitcoin. Disarankan untuk memilih kata sandi yang seacak mungkin dan cukup panjang. Pastikan kamu menyimpan kata sandi ini di tempat yang terpisah dari tempat penyimpanan Portal (mis. di pengelola kata sandi).

![Image](assets/fr/10.webp)

Portal kamu akan menampilkan frasa mnemonik 12 kata. Frasa mnemonik ini memberi kamu akses penuh dan tidak terbatas ke semua bitcoin. Siapa pun yang memiliki frasa ini bisa mencuri dana kamu, bahkan tanpa akses fisik ke Portal.

Frasa 12 kata ini memulihkan akses ke bitcoin jika terjadi kehilangan, pencurian, atau kerusakan pada Portal. Oleh karena itu, sangat penting untuk menyimpannya dengan hati-hati dan di tempat yang aman.

Kamu bisa menuliskannya di selembar kertas, atau untuk keamanan tambahan, aku sarankan mengukirnya pada dasar baja tahan karat untuk melindunginya dari kebakaran, banjir, atau keruntuhan.

Untuk informasi lebih lanjut tentang cara yang tepat menyimpan dan mengelola frasa mnemonik, aku sangat merekomendasikan mengikuti tutorial lainnya, khususnya jika kamu seorang pemula:

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Tentu saja, kamu tidak boleh membagikan kata-kata ini di Internet, seperti yang aku lakukan dalam tutorial ini. Portofolio contoh ini hanya digunakan di Testnet dan akan dihapus di akhir tutorial.

Tekan tombol pada Portal dengan kuat untuk beralih ke kata berikutnya. Pastikan seluruh jari kamu menempel pada tombol dan tahan beberapa detik, agar interaksi terdeteksi dengan benar.

![Image](assets/fr/11.webp)

Portal kamu kemudian akan mengonfirmasi kata sandi yang kamu masukkan di Nunchuk.

![Image](assets/fr/12.webp)

Kamu sekarang telah selesai mengonfigurasi Portal dan membuat frasa mnemonik kamu!

![Image](assets/fr/13.webp)

## Konfigurasi dompet Bitcoin

Pada Nunchuk, klik "*Lanjutkan*", sambil tetap memegang Portal di bagian belakang ponsel kamu.

![Image](assets/fr/14.webp)

Dalam tutorial ini, aku akan menyiapkan portofolio single-sig, jadi aku memilih opsi ini.

![Image](assets/fr/15.webp)

Gunakan akun default, yaitu akun pertama di dompet (nomor 0). Nunchuk kemudian akan meminta kamu mengonfirmasi kata sandi Portal untuk membukanya.

![Image](assets/fr/16.webp)

Di Portal, konfirmasikan ekspor xpub ke Nunchuk. Ini memungkinkan kamu mengelola wallet dari ponsel pintar tanpa bisa membelanjakan bitcoin tanpa Portal. Tekan tombol untuk mengonfirmasi.

Perhatikan bahwa jalur derivasi yang ditampilkan dalam kasus kamu akan berbeda dengan kasusku, karena tutorial ini dilakukan di Testnet.


![Image](assets/fr/17.webp)

Beri nama portofolio kamu, misalnya "*Portal*", lalu klik "*Lanjutkan*".

![Image](assets/fr/18.webp)

Nunchuk kemudian menampilkan Descriptor kamu. Sebaiknya kamu membuat cadangan. Walaupun Descriptor tidak memungkinkan kamu membelanjakan bitcoin, ini memungkinkan kamu melacak jalur turunan dari kunci dari frasa mnemonik jika terjadi pemulihan dompet. Simpan di tempat yang aman, karena meskipun kebocorannya tidak menimbulkan masalah keamanan, hal ini tetap merupakan masalah kerahasiaan.


Klik "*Selesai*".

![Image](assets/fr/19.webp)

Sekarang kamu perlu membuat kunci publik untuk dompet Bitcoin Anda. Untuk melakukannya, klik tombol "*Buat dompet baru*".

![Image](assets/fr/20.webp)

Klik sekali lagi pada "*Buat dompet baru*". Kemudian pilih opsi "*Buat dompet baru menggunakan kunci yang ada*".

![Image](assets/fr/21.webp)

Pilih nama untuk portofolio kamu dan klik "*Lanjutkan*".

![Image](assets/fr/22.webp)

Pilih Portal kamu sebagai perangkat penandatanganan untuk set kunci baru ini, lalu klik "*Lanjutkan*".

![Image](assets/fr/23.webp)

Jika semuanya sudah sesuai dengan keinginan kamu, validasi kreasi tersebut.

![Image](assets/fr/24.webp)

Kamu kemudian dapat menyimpan file konfigurasi dompet. File ini hanya berisi kunci publik, yang berarti meskipun seseorang mengaksesnya, mereka tidak bisa mencuri bitcoin kamu. Namun, mereka akan bisa melacak semua transaksi kamu. Oleh karena itu, file ini hanya menimbulkan risiko terhadap privasi. Dalam beberapa kasus, file ini mungkin sangat diperlukan untuk memulihkan dompet.


![Image](assets/fr/25.webp)

Dan hanya itu saja yang bisa dilakukan!

![Image](assets/fr/26.webp)

## Bagaimana cara menerima bitcoin dengan Portal?

Untuk menerima bitcoin, pilih dompet kamu.

![Image](assets/fr/27.webp)

Sebelum menggunakan alamat yang dibuat, periksa pada layar Portal. Untuk melakukannya, klik "*Terima*".

![Image](assets/fr/28.webp)

Klik pada tiga titik, lalu pilih "*Verifikasi alamat melalui PORTAL*". Kemudian masukkan kata sandi kamu.

![Image](assets/fr/29.webp)

Posisikan Portal di bagian belakang ponsel kamu, lalu konfirmasikan dengan menekan tombol.

![Image](assets/fr/30.webp)

Pastikan alamat yang ditampilkan di Portal sesuai dengan alamat di Nunchuk, lalu konfirmasikan dengan menekan tombol sekali lagi. Jika alamatnya sama, kamu bisa memberikan alamat ini kepada pembayar.

![Image](assets/fr/31.webp)

Setelah transaksi pembayar disiarkan, kamu akan melihatnya muncul di dompet milikmu.

![Image](assets/fr/32.webp)

Klik pada "*Lihat sudut*".

![Image](assets/fr/33.webp)

Pilih UTXO baru kamu.

![Image](assets/fr/34.webp)

Klik tanda "*+*" di sebelah "*Tags*" untuk menambahkan tag ke UTXO kamu. Ini adalah praktik yang baik, karena membantu kamu mengingat dari mana asal koin dan mengoptimalkan privasi saat membelanjakan di masa mendatang.

![Image](assets/fr/35.webp)

Pilih tag yang sudah ada atau buat tag baru, lalu klik "*Save*". Kamu juga bisa membuat "*collections*" untuk mengatur komponen kamu dengan cara yang lebih terstruktur.

![Image](assets/fr/36.webp)

## Bagaimana cara mengirim bitcoin menggunakan Portal?

Setelah kamu memiliki bitcoin di dalam wallet, kamu juga bisa mengirimkannya. Untuk melakukannya, klik dompet pilihan kamu.

![Image](assets/fr/37.webp)

Klik tombol "*Kirim*".

![Image](assets/fr/38.webp)

Pilih jumlah yang akan dikirim, lalu klik "*Lanjutkan*".

![Image](assets/fr/39.webp)

Tambahkan "*catatan*" pada transaksi di masa mendatang untuk mengingatkan kamu tentang tujuannya.

![Image](assets/fr/40.webp)

Kemudian masukkan alamat penerima di bidang yang tersedia. Kamu juga bisa memindai alamat yang dikodekan sebagai kode QR dengan mengeklik ikon di bagian kanan atas layar. Setelah itu, klik tombol "*Buat Transaksi*".

![Image](assets/fr/41.webp)

Periksa detail transaksi kamu, lalu klik tombol "*Tanda Tangan*" di samping Portal, dan masukkan kata sandi kamu.

![Image](assets/fr/42.webp)

Letakkan Portal di bagian belakang ponsel kamu. Periksa apakah alamat penerima dan jumlahnya sudah benar. Jika sudah, tekan tombol untuk melanjutkan.

![Image](assets/fr/43.webp)

Periksa apakah biaya transaksi sudah benar, lalu tekan tombol lagi untuk menandatangani transaksi kamu.

![Image](assets/fr/44.webp)

Transaksi kamu telah ditandatangani. Kamu bisa memeriksa detailnya untuk terakhir kali di Nunchuk, lalu klik tombol "*Siarkan transaksi*" untuk menyiarkannya di jaringan Bitcoin.

![Image](assets/fr/45.webp)

Transaksi kamu sekarang sedang menunggu konfirmasi.

![Image](assets/fr/46.webp)

Selamat, kamu sekarang sudah bisa menggunakan Portal! Jika kamu merasa tutorial ini bermanfaat, aku akan sangat berterima kasih jika kamu memberikan tanda jempol hijau di bawah ini. Jangan ragu membagikan artikel ini di jejaring sosial. Terima kasih banyak!

Untuk mengetahui lebih lanjut, lihat kursus pelatihan lengkap kami mengenai cara kerja portofolio HD:


https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f
