---
name: Portal
description: Mengkonfigurasi dan menggunakan Portal dompet perangkat keras TwentyTwo-Devices
---
![cover](assets/cover.webp)

Portal adalah dompet perangkat keras Bitcoin yang dibuat oleh TwentyTwo Devices, perusahaan yang fokus mengembangkan dompet perangkat keras open-source untuk para pengguna Bitcoin. Perusahaan ini didirikan oleh Alekos Filini, pencipta proyek Magical Bitcoin ([selanjutnya dinamakan BDK] (https://github.com/bitcoindevkit)) dan pernah bekerja untuk Blockstream dan BHB Network, TwentyTwo Devices yang kini berfokus pada kebebasan pengguna, kesederhanaan, dan keamanan.

Yang membuat Portal berbeda dari dompet perangkat keras lain di pasaran adalah integrasinya yang langsung dengan smartphone. Dompet ini bisa berfungsi tanpa kabel atau baterai, karena menggunakan teknologi NFC untuk menyalakan dirinya sendiri dan berkomunikasi dengan dompet seluler yang kompatibel. Desainnya yang elegan dibuat agar nyaman digunakan. Bagian bundarnya ditempatkan di belakang smartphone untuk menampilkan layar tempat kamu bisa memeriksa detail transaksi sebelum menandatanganinya dengan tombol khusus.

![Image](assets/fr/01.webp)

Portal sepenuhnya open-source, dibangun dengan firmware yang ditulis dalam bahasa Rust dan memanfaatkan BDK (Bitcoin Dev Kit) untuk mengelola kunci dan transaksi. Portal ini dijual dengan harga €89 [di situs web resminya] (https://store.twenty-two.xyz/products/portal-hardware-wallet).

Saat artikel ini ditulis, Portal kompatibel dengan aplikasi Nunchuk dan Bitcoin Keeper. Dalam tutorial ini, kita akan mengonfigurasinya menggunakan Nunchuk.

## Membuka kemasan

Ketika Anda menerima Portal Anda, periksa apakah kotak dan label yang menyegelnya dalam kondisi baik. Di dalamnya, Anda akan menemukan Portal Anda di dalam kantong tertutup.

Pastikan segelnya masih utuh supaya kantongnya belum dibuka. Nomor unik yang tercetak dengan huruf besar di kantong harus sama dengan nomor yang tertulis dengan warna hitam di bawah segel biru, nomor pada label kotak, dan nomor yang muncul di layar saat pertama kali kamu menyalakannya.

![Image](assets/fr/02.webp)

## Instalasi Nunchuk

Untuk mengelola dompet yang dihosting di Portal, kita akan menggunakan aplikasi Nunchuk. Unduh aplikasi ini dari [Google Play Store](https://play.google.com/store/apps/details?id=io.nunchuk.android), [App Store](https://apps.apple.com/us/app/nunchuk-bitcoin-wallet/id1563190073) atau secara langsung melalui [file `.apk`](https://github.com/nunchuk-io/nunchuk-android/releases).

![Image](assets/fr/03.webp)

Kalau kamu menggunakan Nunchuk untuk pertama kali, aplikasi ini akan meminta kamu membuat akun. Untuk tutorial ini, kamu nggak perlu membuat akun. Pilih *Lanjutkan sebagai tamu* untuk melanjutkan tanpa akun.

![Image](assets/fr/04.webp)

## Konfigurasi portal

Pada layar beranda Nunchuk, klik logo "*NFC*" di bagian atas layar.

![Image](assets/fr/05.webp)

Letakkan Portal di bagian belakang ponsel kamu untuk menyalakannya.

![Image](assets/fr/06.webp)

Nunchuk akan mengenali Portal kamu. Kemudian klik "*Lanjutkan*".

![Image](assets/fr/07.webp)

Untuk membuat portofolio baru, pilih "*Generate seed on Portal*" lalu klik "*Lanjutkan*".

![Image](assets/fr/08.webp)

Kamu bisa memilih antara frasa mnemonik 12 atau 24 kata. Keamanan kedua opsi ini serupa, jadi pilih saja yang paling mudah disimpan, yaitu 12 kata.

![Image](assets/fr/09.webp)

Kamu kemudian akan diminta membuat kata sandi. Kata sandi ini digunakan untuk membuka kunci Portal dan melindungi dari akses fisik yang tidak sah. Kata sandi tidak berpengaruh pada proses penurunan kunci kriptografi dompet kamu, jadi meski tanpa kata sandi, frasa mnemonik 12 atau 24 kata tetap memungkinkan kamu mengakses bitcoin. Disarankan memilih kata sandi yang acak dan cukup panjang, serta menyimpannya terpisah dari tempat Portal disimpan, misalnya di pengelola kata sandi.

![Image](assets/fr/10.webp)

Portal akan menampilkan frasa mnemonik 12 kata. Frasa ini memberi kamu akses penuh ke semua bitcoin kamu. Siapa pun yang memiliki frasa ini bisa mencuri dana kamu, bahkan tanpa harus memegang Portal secara fisik.

Frasa 12 kata ini juga digunakan untuk memulihkan akses ke bitcoin jika Portal hilang, dicuri, atau rusak. Karena itu, sangat penting untuk menyimpannya dengan hati-hati di tempat yang aman.

Kamu bisa menuliskannya di selembar kertas, atau untuk keamanan ekstra, aku sarankan mengukirnya di dasar baja tahan karat agar terlindung dari kebakaran, banjir, atau kerusakan.

Untuk info lebih lanjut tentang cara menyimpan dan mengelola frasa mnemonik dengan benar, aku sangat merekomendasikan mengikuti tutorial lainnya, terutama kalau kamu pemula.

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Tentu saja, kamu tidak boleh membagikan kata-kata ini di internet, seperti yang aku lakukan dalam tutorial ini. Portofolio contoh ini hanya akan digunakan di Testnet dan akan dihapus di akhir tutorial.

Tekan tombol pada Portal dengan kuat untuk beralih ke kata berikutnya. Pastikan kamu meletakkan seluruh jari kamu pada tombol dan menahan tekanan selama beberapa detik, sehingga interaksi terdeteksi dengan benar.

![Image](assets/fr/11.webp)

Portal kamu akan mengonfirmasi kata sandi yang kamu masukkan di Nunchuk.

![Image](assets/fr/12.webp)

Sekarang kamu telah selesai mengonfigurasi Portal dan membuat frasa mnemonik Anda!

![Image](assets/fr/13.webp)

## Konfigurasi dompet Bitcoin

Pada Nunchuk, klik "*Lanjutkan*", sambil tetap memegang Portal di bagian belakang ponselmu.

![Image](assets/fr/14.webp)

Dalam tutorial ini, aku akan menyiapkan portofolio single-sig, jadi aku memilih opsi ini.

![Image](assets/fr/15.webp)

Gunakan akun default, yaitu akun pertama di dompet (nomor 0). Nunchuk kemudian akan meminta kamu untuk mengonfirmasi kata sandi Portal agar bisa membukanya.

![Image](assets/fr/16.webp)

Di Portal, konfirmasikan ekspor xpub kamu ke Nunchuk. Hal ini memungkinkan kamu mengelola dompet dari ponsel pintar, tetapi tidak bisa membelanjakan bitcoin tanpa Portal. Tekan tombol untuk mengonfirmasi.

Perhatikan bahwa jalur derivasi yang ditunjukkan dalam kasus kamu akan berbeda dengan kasus saya, karena tutorial ini dilakukan di Testnet.

![Image](assets/fr/17.webp)

Beri nama portofolio milikmu, misalnya "*Portal*", lalu klik "*Lanjutkan*".

![Image](assets/fr/18.webp)

Nunchuk kemudian menampilkan Deskriptor kamu. Sebaiknya kamu membuat cadangan. Walaupun Deskriptor tidak mengizinkan kamu membelanjakan bitcoin, Deskriptor memungkinkan kamu melacak jalur turunan kunci dari frasa mnemonik kamu jika perlu memulihkan dompet. Simpan di tempat yang aman, karena meski kebocorannya tidak menimbulkan masalah keamanan, itu tetap masalah kerahasiaan.

Klik "*Selesai*".

![Image](assets/fr/19.webp)

Sekarang kamu perlu membuat kunci publik untuk dompet Bitcoin kamu. Untuk melakukannya, klik tombol "Buat dompet baru".

![Image](assets/fr/20.webp)

Klik sekali lagi pada "Buat dompet baru". Lalu pilih opsi "Buat dompet baru menggunakan kunci yang ada".

![Image](assets/fr/21.webp)

Pilih nama untuk portofolio kamu dan klik "*Lanjutkan*".

![Image](assets/fr/22.webp)

Pilih Portal kamu sebagai perangkat penandatanganan untuk set kunci baru ini, lalu klik "*Lanjutkan*".

![Image](assets/fr/23.webp)

Jika semuanya sudah sesuai dengan keinginan Anda, validasi kreasi tersebut.

![Image](assets/fr/24.webp)

Kamu kemudian bisa menyimpan file konfigurasi dompet. File ini hanya berisi kunci publik, jadi meski seseorang mengaksesnya, mereka tidak bisa mencuri bitcoin kamu. Namun, mereka bisa melacak semua transaksi kamu. Jadi, file ini hanya menimbulkan risiko terhadap privasi. Dalam beberapa kasus, file ini bisa sangat berguna untuk memulihkan dompet.

![Image](assets/fr/25.webp)

Dan hanya itu saja yang bisa dilakukan!

![Image](assets/fr/26.webp)

## Bagaimana cara menerima bitcoin dengan Portal?

Untuk menerima bitcoin, pilih dompetmu.

![Image](assets/fr/27.webp)

Sebelum menggunakan alamat yang dibuat, periksa pada layar Portal. Untuk melakukannya, klik "*Terima*".

![Image](assets/fr/28.webp)

Klik pada tiga titik, lalu pilih "*Verifikasi alamat melalui PORTAL*". Kemudian masukkan kata sandi.

![Image](assets/fr/29.webp)

Posisikan Portal di bagian belakang ponsel-mu, lalu konfirmasikan dengan menekan tombol.

![Image](assets/fr/30.webp)

Pastikan alamat yang ditampilkan di Portal sesuai dengan alamat di Nunchuk kamu, lalu konfirmasikan dengan menekan tombol sekali lagi. Jika alamatnya sama, kamu bisa memberikan alamat ini kepada pembayar.

![Image](assets/fr/31.webp)

Setelah transaksi pembayar disiarkan, kamu akan melihatnya muncul di dompet milikmu.

![Image](assets/fr/32.webp)

Klik pada "*Lihat sudut*".

![Image](assets/fr/33.webp)

Pilih UTXO barumu.

![Image](assets/fr/34.webp)

Klik tanda "*+*" di sebelah "*Tags*" untuk menambahkan tag ke UTXO milikumu. Ini adalah praktik yang baik, karena membantumu mengingat dari mana asal koin milikmu dan mengoptimalkan privasimu saat membelanjakan di masa mendatang.

![Image](assets/fr/35.webp)

Pilih tag yang sudah ada atau buat tag baru, lalu klik "*Save*". Anda juga bisa membuat "*collections*" untuk mengatur komponen milkmu dengan cara yang lebih terstruktur.

![Image](assets/fr/36.webp)

## Bagaimana cara mengirim bitcoin menggunakan Portal?

Setelah kamu memiliki bitcoin di dalam wallet, kamu juga bisa mengirimkannya. Untuk melakukannya, klik dompet pilihanmu.

![Image](assets/fr/37.webp)

Klik tombol "*Kirim*".

![Image](assets/fr/38.webp)

Pilih jumlah yang akan dikirim, lalu klik "*Lanjutkan*".

![Image](assets/fr/39.webp)

Tambahkan "*catatan*" pada transaksi Anda di masa mendatang untuk mengingatkan kamu tentang tujuannya.

![Image](assets/fr/40.webp)

Kemudian masukkan alamat penerima di bidang yang tersedia. Kamu juga dapat memindai alamat yang dikodekan sebagai kode QR dengan mengeklik ikon di bagian kanan atas layar. Kemudian klik tombol "*Buat Transaksi*".

![Image](assets/fr/41.webp)

Periksa detail transaksi Anda, lalu klik tombol "*Tanda Tangan*" di samping Portalmu, dan masukkan kata sandimu.

![Image](assets/fr/42.webp)

Letakkan Portal di bagian belakang ponsel kamu. Periksa apakah alamat penerima dan jumlahnya sudah benar. Jika sudah, tekan tombol untuk melanjutkan.

![Image](assets/fr/43.webp)

Periksa apakah biaya transaksi sudah benar, lalu tekan tombol lagi untuk menandatangani transaksimu.

![Image](assets/fr/44.webp)

Transaksi kamu telah ditandatangani. Kamu bisa memeriksa detailnya sekali terakhir di Nunchuk, lalu klik tombol "Siarkan transaksi" untuk mengirimnya ke jaringan Bitcoin.

![Image](assets/fr/45.webp)

Sekarang kamu sedang menunggu konfirmasi.

![Image](assets/fr/46.webp)

Selamat, sekarang kamu sudah bisa menggunakan Portal! Kalau kamu merasa tutorial ini bermanfaat, aku akan sangat berterima kasih jika kamu memberikan jempol hijau di bawah ini. Jangan ragu untuk membagikan artikel ini di jejaring sosial kamu. Terima kasih banyak!

Untuk mempelajari lebih lanjut, lihat kursus pelatihan lengkap kami tentang cara kerja portofolio HD:

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f
