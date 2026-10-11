---
name: BIP-39 Passphrase Ledger
description: Bagaimana cara menambahkan passphrase ke dompet Ledger kamu?
---
![cover](assets/cover.webp)

Passphrase BIP39 adalah kata sandi opsional yang, ketika digabungkan dengan seedphrase-mu, memberikan lapisan keamanan tambahan untuk dompet Bitcoin deterministik dan hierarkis. Dalam tutorial ini, kita akan bersama-sama mengulas cara mengatur passphrase pada dompet Bitcoin amanmu di Ledger (terlepas dari modelnya).

Sebelum memulai tutorial ini, jika kamu tidak familiar dengan konsep passphrase, bagaimana cara kerjanya, dan implikasinya terhadap dompet Bitcoinmu, aku sangat merekomendasikan untuk berkonsultasi dengan artikel teoretis lain ini di mana aku menjelaskan semuanya:

https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

## Bagaimana fungsi passphrase pada Ledger?

Dengan perangkat Ledger, kamu memiliki dua opsi berbeda untuk mengonfigurasi passphrase pada dompetmu: opsi "*PIN-tied*" dan opsi "*temporary*".

Dengan opsi "*PIN-tied*", kamu mengaitkan passphrase dengan PIN kedua pada Ledger-mu. Ini berarti kamu akan memiliki 2 PIN: satu untuk mengakses dompet regulermu tanpa passphrase, dan yang lainnya untuk mengakses dompet kedua yang dilindungi oleh passphrase.

![PASSPHRASE BIP39](assets/notext/03.webp)

Pada dasarnya, bahkan dengan opsi passphrase yang terikat pada PIN kedua ini, passphrase-mu tetaplah passphrase-mu. Ini berarti jika kamu kehilangan Ledger dan ingin memulihkan bitcoinmu di perangkat atau perangkat lunak lain, kamu akan benar-benar membutuhkan frasa 24 kata dan **passphrase lengkap**. PIN yang terkait dengan passphrase hanya digunakan untuk mengaksesnya di Ledger saat ini, tetapi tidak berfungsi di Ledger lain atau perangkat lunak lain. Oleh karena itu, sangat penting untuk sepenuhnya mencadangkan passphrase pada media fisik. **Mengetahui PIN sekunder saja tidak cukup untuk mendapatkan kembali akses ke dompetmu**; ini hanya fitur kemudahan pada Ledger.

Opsi PIN kedua ini sangat menarik untuk menghadapi serangan fisik. Misalnya, jika seorang penyerang memaksa kamu untuk membuka kunci perangkat untuk mencuri dana, kamu dapat menggunakan PIN pertama untuk mengakses dompet umpan yang berisi sejumlah kecil bitcoin, sementara menjaga dana utama tetap aman di balik PIN kedua.

Selain itu, opsi ini menawarkan semua manfaat keamanan dari passphrase BIP39 tanpa kendala harus memasukkannya secara manual setiap kali menggunakan perangkat penandatanganan. Ini memungkinkan penggunaan passphrase panjang dan acak, sehingga memperkuat perlindungan terhadap serangan brute force, sambil menghindari kesulitan mengetiknya secara manual setiap kali pada tombol kecil perangkat.  

Opsi "*passphrase sementara*" tidak menyimpan passphrase pada perangkat. Setiap kali kamu ingin mengakses dompet terlindungi, kamu perlu memasukkan passphrase secara manual pada Ledger. Ini membuat penggunaan lebih merepotkan tetapi sedikit meningkatkan keamanan dengan tidak meninggalkan jejak passphrase pada perangkat. Segera setelah perangkat dimatikan, ia kembali ke keadaan default dan memerlukan entri baru dari passphrase lengkap untuk mengakses akun tersembunyi. Opsi "*passphrase sementara*" ini dengan demikian mirip dengan operasi dompet perangkat keras lainnya.

Dalam tutorial ini, aku akan menggunakan Ledger Flex sebagai contoh. Namun, jika kamu menggunakan model Ledger lain, prosesnya tetap sama. Untuk Ledger Stax, antarmukanya sama dengan Ledger Flex. Sedangkan untuk model Nano S, Nano S Plus, dan Nano X, meskipun antarmukanya berbeda, proses dan nama-nama menu tetap sama.  

**Perhatian:** Jika kamu sudah menerima bitcoin di Ledger sebelum mengaktifkan passphrase, kamu perlu mentransfernya melalui transaksi Bitcoin. Passphrase menghasilkan satu set kunci baru, sehingga menciptakan dompet yang sepenuhnya independen dari dompet awal. Saat menambahkan passphrase, kamu akan memiliki dompet baru yang kosong. Namun, ini tidak menghapus dompet pertama tanpa passphrase. Kamu masih bisa mengaksesnya, baik langsung melalui Ledger tanpa memasukkan passphrase atau melalui perangkat lunak lain menggunakan frasa 24 kata-mu.

Sebelum memulai tutorial ini, pastikan kamu sudah menginisialisasi Ledger dan menghasilkan seedphrase-mu. Jika ini belum terjadi dan Ledger-mu baru, ikuti tutorial khusus untuk modelmu yang tersedia di Plan ₿ Academy. Setelah langkah ini selesai, kamu dapat kembali ke tutorial ini.

https://planb.academy/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.academy/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4



## Bagaimana cara mengatur passphrase sementara dengan Ledger?

Di halaman utama Ledger kamu, klik pada roda gigi pengaturan.

![PASSPHRASE BIP39](assets/notext/04.webp)

Pilih menu "Advanced", kemudian "Set passphrase".

![PASSPHRASE BIP39](assets/notext/05.webp)

Ini adalah langkah di mana kamu dapat memilih antara opsi "linked to PIN" atau opsi "temporary" yang telah kita bahas di bagian sebelumnya. Di sini, aku akan menjelaskan cara mengatur passphrase sementara, jadi klik pada "Set temporary passphrase".

![PASSPHRASE BIP39](assets/notext/06.webp)
Kamu kemudian diminta untuk memasukkan passphrase-mu. Pilih passphrase yang kuat dan segera lanjutkan ke cadangan fisik, pada media seperti kertas atau logam. Dalam contoh ini, aku memilih passphrase: `fH3&kL@9mP#2sD5qR!82`. Setelah memasukkan passphrase-mu, klik tombol "*Continue*".
![PASSPHRASE BIP39](assets/notext/07.webp)

Verifikasi bahwa passphrase kamu cocok dengan yang telah kamu catat pada cadangan fisik kamu, kemudian klik tombol "*Yes, it's correct*" untuk mengonfirmasi.

![PASSPHRASE BIP39](assets/notext/08.webp)

Untuk menyelesaikan pembuatan passphrase kamu, masukkan kode PIN Ledger kamu. Mulai sekarang, setiap kali kamu ingin mengakses dompet kamu dengan passphrase di Ledger, kamu perlu mengikuti langkah-langkah yang sama seperti yang dijelaskan di sini.

![PASSPHRASE BIP39](assets/notext/09.webp)

Kamu sekarang dapat mengimpor set kunci publikmu di Sparrow Wallet untuk mengelola dompetmu. Di Sparrow, ini akan sesuai dengan dompet yang berbeda dari dompet awalmu tanpa passphrase.

Buka Sparrow Wallet. Pastikan perangkat lunak terhubung ke node, kemudian klik pada tab "*File*" dan pilih "*New Wallet*".


![PASSPHRASE BIP39](assets/notext/10.webp)

Pilih nama untuk dompetmu yang dilindungi oleh passphrase. Untuk contoh ini, aku memilih nama yang secara eksplisit menyertakan istilah "*passphrase*". Namun, jika kamu lebih suka menjaga kerahasiaan dompet ini di komputermu, kamu dapat memilih nama yang kurang sugestif.

![PASSPHRASE BIP39](assets/notext/11.webp)

Pilih jenis skrip untuk dompet kamu. Aku menyarankanmu untuk memilih "*Taproot*" atau alternatifnya "*Native SegWit*".

![PASSPHRASE BIP39](assets/notext/12.webp)
Hubungkan Ledger-mu ke komputer, kemudian klik pada "*Connected Hardware Wallet*". Pastikan kamu sudah memasukkan passphrase pada Ledger-mu. Jika belum, silakan kembali ke langkah sebelumnya untuk memasukkan passphrase-mu. Sebelum melanjutkan ke pemindaian, ingat juga untuk membuka aplikasi "*Bitcoin*" pada Ledger-mu.

Klik pada tombol "*Scan...*".

Klik pada "*Import Keystore*" di sebelah Ledger-mu.

Dompetmu yang dilindungi oleh passphrase sekarang telah dibuat di Sparrow. Untuk mengonfirmasi, klik pada tombol "*Apply*".

Pilih kata sandi yang kuat untuk mengamankan akses ke Sparrow Wallet. Kata sandi ini akan memastikan keamanan akses ke data dompetmu di Sparrow, yang membantu melindungi kunci publik, alamat, label, dan riwayat transaksi dari akses tidak sah. Aku menyarankan menyimpan kata sandi ini di pengelola kata sandi agar tidak lupa.

Dan sekarang, dompetmu telah dibuat! Di menu "*Settings*", Sparrow akan memberikanmu "*Master fingerprint*". Ini merupakan sidik jari dari kunci induk, yang digunakan sebagai dasar untuk menurunkan dompet. Aku sangat menyarankan untuk menyimpan salinan sidik jari ini. Dalam contohku, ini sesuai dengan: `281ee33a`.

Ingat apa yang disebutkan di bagian sebelumnya: kesalahan, meskipun kecil, dalam memasukkan passphrase-mu akan menghasilkan dompet baru yang sepenuhnya berbeda dengan kunci yang berbeda. Setiap kali perlu memastikan kamu mengakses dompet yang tepat dengan passphrase yang benar, periksa bahwa sidik jari kunci induk cocok dengan yang dicatat. Informasi ini, dengan sendirinya, tidak menimbulkan risiko terhadap keamanan dana atau privasi.

Sebelum menggunakan dompet dengan passphrase, aku sangat menyarankan melakukan tes pemulihan dry-run. Catat informasi referensi seperti xpub atau sidik jari kunci induk, kemudian reset Ledger-mu sementara dompet masih kosong. Selanjutnya, coba pulihkan dompet di Ledger menggunakan cadangan kertas dari frasa 24 kata dan passphrase. Periksa bahwa informasi yang dihasilkan setelah pemulihan cocok dengan yang dicatat awalnya. Jika demikian, kamu dapat yakin bahwa cadangan kertasmu dapat diandalkan.

## Bagaimana cara mengatur passphrase yang terkait dengan PIN pada Ledger?

Di halaman utama Ledger-mu, klik pada roda gigi pengaturan.

Pilih menu "*Advanced*", kemudian "*Set passphrase*".

Ini adalah langkah di mana kamu dapat memilih antara opsi "*linked to PIN*" atau "*temporary*" yang dibahas di bagian sebelumnya. Di sini, aku akan menjelaskan cara mengatur passphrase yang terkait dengan PIN, jadi klik pada "*Set passphrase and attach it to a new PIN*".

Kamu kemudian harus memilih kode PIN yang akan dikaitkan dengan passphrase-mu. Sama seperti kode PIN utama, disarankan memilih kode PIN 8 digit, sembarang mungkin. Juga, pastikan menyimpan kode ini di lokasi yang berbeda dari tempat Ledger Flex-mu disimpan.

Dalam kasus saya, kode PIN utama adalah `58293647` dan saya memilih `71425839` sebagai kode PIN sekunder yang terkait dengan passphrase.
![PASSPHRASE BIP39](assets/notext/22.webp)

Kamu kemudian diminta untuk memasukkan passphrase-mu. Pilih passphrase yang kuat dan segera lanjutkan ke cadangan fisik, pada media seperti kertas atau logam. Dalam contoh ini, aku memilih passphrase: `fH3&kL@9mP#2sD5qR!82`. Setelah memasukkan passphrase-mu, klik tombol "*Continue*".


![PASSPHRASE BIP39](assets/notext/23.webp)

Verifikasi bahwa passphrase-mu sesuai dengan yang telah dicatat pada cadangan fisik, kemudian klik tombol "*Yes, it's correct*" untuk mengonfirmasi.

![PASSPHRASE BIP39](assets/notext/24.webp)

Untuk menyelesaikan pembuatan passphrase kamu, masukkan kode PIN utama Ledger kamu (bukan yang terkait dengan passphrase).

![PASSPHRASE BIP39](assets/notext/25.webp)

Mulai sekarang, setiap kali kamu ingin mengakses dompet dengan passphrase di Ledger, kamu perlu memasukkan bukan kode PIN utama, melainkan kode PIN sekunder:
- Kode PIN utama (`58293647`) > dompet tanpa passphrase.
- Kode PIN sekunder (`71425839`) > dompet dengan passphrase.

Kamu sekarang dapat mengimpor set kunci publikmu di Sparrow Wallet untuk mengelola dompetmu. Di Sparrow, ini akan sesuai dengan dompet yang berbeda dari dompet awalmu tanpa passphrase.

Buka Sparrow Wallet. Pastikan perangkat lunak terhubung ke node, kemudian klik pada tab "*File*" dan pilih "*New Wallet*".

![PASSPHRASE BIP39](assets/notext/26.webp)

Pilih nama untuk dompetmu yang dilindungi oleh passphrase. Untuk contoh ini, aku memilih nama yang secara eksplisit menyertakan istilah "*passphrase*". Namun, jika kamu lebih suka menjaga kerahasiaan dompet ini di komputermu, kamu dapat memilih nama yang kurang sugestif.

![PASSPHRASE BIP39](assets/notext/27.webp)

Pilih tipe skrip untuk dompet kamu. Aku menyarankanmu untuk memilih "*Taproot*" atau, jika tidak tersedia, "*Native SegWit*".

![PASSPHRASE BIP39](assets/notext/28.webp)
Hubungkan Ledger-mu ke komputer, kemudian klik pada "*Connected Hardware Wallet*". Pastikan kamu sudah memiliki passphrase di Ledger-mu dengan membukanya menggunakan kode PIN sekunder. Jika tidak, restart Ledger-mu dan masukkan kode PIN yang terkait dengan passphrase. Sebelum melanjutkan ke pemindaian, ingat juga untuk membuka aplikasi "*Bitcoin*" di Ledger-mu.

![PASSPHRASE BIP39](assets/notext/29.webp)

Klik tombol "*Scan...*".

![PASSPHRASE BIP39](assets/notext/30.webp)

Klik pada "*Import Keystore*".

![PASSPHRASE BIP39](assets/notext/31.webp)

Dompet kamu yang dilindungi oleh passphrase sekarang telah dibuat di Sparrow. Untuk mengonfirmasi, klik tombol "*Apply*".

![PASSPHRASE BIP39](assets/notext/32.webp)

Pilih kata sandi yang kuat untuk mengamankan akses ke Sparrow Wallet. Kata sandi ini akan menjamin keamanan akses ke data dompetmu di Sparrow, yang membantu melindungi kunci publik, alamat, label, dan riwayat transaksi dari akses tidak sah.

Aku menyarankan menyimpan kata sandi ini di pengelola kata sandi agar tidak lupa.

![PASSPHRASE BIP39](assets/notext/33.webp)
Dan sekarang, dompetmu telah dibuat! Di menu "*Settings*", Sparrow akan memberikanmu "*Master fingerprint*". Ini merupakan sidik jari dari kunci indukmu, yang digunakan sebagai dasar dari turunan dompetmu. Aku sangat merekomendasikan untuk menyimpan salinan sidik jari ini. Dalam contohku, ini sesuai dengan: `281ee33a`.

![PASSPHRASE BIP39](assets/notext/34.webp)

Ingat apa yang telah disebutkan di bagian sebelumnya: kesalahan, meskipun kecil, dalam memasukkan passphrase-mu akan menghasilkan dompet baru yang sepenuhnya berbeda dengan kunci yang berbeda. Setiap kali perlu memastikan akses ke dompet yang benar dengan passphrase yang tepat, verifikasi bahwa sidik jari dari kunci induk cocok dengan yang telah dicatat. Informasi ini, dengan sendirinya, tidak menimbulkan risiko terhadap keamanan dana atau privasi.

Sebelum menggunakan dompet dengan passphrase, aku sangat menyarankan melakukan tes pemulihan tanpa risiko. Catat informasi referensi seperti xpub atau sidik jari dari kunci induk, kemudian reset Ledger-mu sementara dompet masih kosong. Selanjutnya, coba pulihkan dompet di Ledger menggunakan cadangan kertas dari frasa 24 kata dan passphrase. Periksa bahwa informasi yang dihasilkan setelah pemulihan cocok dengan apa yang awalnya dicatat. Jika demikian, kamu dapat yakin bahwa cadangan kertasmu dapat diandalkan.

Selamat, dompet Bitcoin-mu sekarang diamankan dengan passphrase! Jika kamu merasa tutorial ini bermanfaat, aku akan sangat menghargai jika kamu memberikan jempol ke atas di bawah ini. Jangan ragu untuk membagikan artikel ini di jaringan sosialmu. Terima kasih banyak!

Aku juga merekomendasikan memeriksa tutorial lengkap lainnya tentang cara menggunakan Ledger Flex-mu:


https://planb.academy/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a
