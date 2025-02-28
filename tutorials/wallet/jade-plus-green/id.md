---
name: Jade Plus - Hijau
description: Konfigurasikan Jade Plus dengan mudah dengan Green
---
![cover](assets/cover.webp)

Jade Plus adalah dompet perangkat keras khusus Bitcoin yang dirancang oleh Blockstream. Dompet ini merupakan penerus Jade klasik, dengan peningkatan perangkat lunak, lebih banyak opsi, dan ergonomi yang didesain ulang untuk penggunaan yang lebih intuitif. Versi baru ini menawarkan layar LCD 1,9 inci yang luar biasa, dengan gamut warna yang lebih luas dari pendahulunya. Tombol dan navigasi menu juga telah dioptimalkan.

Jade Plus dapat digunakan dalam beberapa cara: melalui koneksi kabel USB-C, dalam mode "*Air-Gap*" dengan kartu micro SD (memerlukan adaptor), melalui Bluetooth atau bahkan dengan menukarkan kode QR berkat kamera yang terintegrasi. Dompet perangkat keras ini bertenaga baterai.

Dompet ini tersedia mulai dari $149,99 dalam versi hitam dasar, dan harganya bisa naik hingga $20 untuk versi "*Genesis Grey*" atau "*Lunar Silver*". Oleh karena itu, Jade Plus adalah pilihan yang menarik, dengan fungsi canggih yang sebanding dengan dompet perangkat keras kelas atas seperti Coldcard Q atau Passport V2, tetapi dengan harga yang cukup rendah, mendekati model kelas menengah.

![JADE-PLUS-GREEN](assets/fr/01.webp)

Jade Plus kompatibel dengan sebagian besar perangkat lunak manajemen portofolio. Berikut ini adalah ringkasan kompatibilitas pada saat penulisan (Januari 2025):

| Desktop | Seluler | USB | Bluetooth | QR | JadeLink | Perangkat lunak manajemen

| ------------------- | ------- | ------ | --- | ----------- | --- | -------- |

| Blockstream Hijau | 🟢 | 🟢 | 🟢 | 🟢 (Seluler) | 🟢 | 🔴 |

liana | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 |

burung pipit | 🟢 | 🔴 | 🟢 | 🔴 | 🟢 | 🟢 | 🟢 |

nunchuk | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 |

| Momok | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 |

| BlueWallet | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 |

electrum | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 |

| Penjaga Gawang | 🔴 | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 |

Dalam tutorial ini, kita akan mengatur dan menggunakan Jade Plus dengan aplikasi seluler Green Wallet Blockstream melalui koneksi Bluetooth. Pengaturan ini sangat ideal untuk pemula. Jika Anda mencari pendekatan yang lebih canggih, saya sarankan Anda melihat tutorial ini di mana kita menggunakan Jade Plus dengan Sparrow Wallet dalam mode kode QR:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262
## Model keamanan Jade Plus

Jade Plus menggunakan model keamanan berdasarkan "elemen aman virtual", yang diwujudkan oleh "blind oracle". Secara konkret, mekanisme ini menggabungkan PIN yang dipilih oleh pengguna, sebuah rahasia yang disimpan di Jade dan sebuah rahasia yang dipegang oleh oracle (server yang dikelola oleh Blockstream), untuk membuat kunci AES-256 yang didistribusikan ke dua entitas. Selama inisiasi, pertukaran ECDH mengamankan komunikasi dengan oracle, dan mengenkripsi frasa pemulihan pada dompet perangkat keras. Secara praktis, ketika Anda ingin mengakses seed untuk menandatangani transaksi, Anda membutuhkan akses ke :


- Ke perangkat Jade Plus itu sendiri;
- Ke PIN untuk membuka kunci perangkat ;
- Dan untuk rahasia peramal.

Keuntungan utama dari pendekatan ini adalah tidak adanya satu titik kegagalan pada tingkat perangkat keras, karena jika penyerang mendapatkan akses ke Jade Anda, mengekstraksi kunci membutuhkan kompromi secara bersamaan dengan Jade dan oracle. Model ini juga berarti bahwa Jade Plus sepenuhnya bersifat open-source, menghindari kendala yang terkait dengan penggunaan elemen keamanan fisik yang sebenarnya, seperti yang digunakan pada Ledger, misalnya.

Kerugian dari sistem ini adalah penggunaan Jade Plus bergantung pada oracle yang dikelola oleh Blockstream. Jika oracle ini tidak dapat diakses, maka tidak mungkin lagi untuk menggunakan dompet perangkat keras secara langsung dengan PIN. Akan tetapi, ini tidak berarti bahwa bitcoin Anda hilang, karena bitcoin tersebut masih dapat dipulihkan dengan menggunakan frasa pemulihan Anda, yang dapat Anda masukkan di Jade Plus dalam mode "*stateless*". Untuk mengatasi ketergantungan ini, Anda juga bisa mengonfigurasi dan mengelola server oracle Anda sendiri.

## Membuka kemasan Jade Plus

Ketika Anda menerima Jade Plus, periksa apakah kotak dan segelnya dalam kondisi baik untuk memastikan bahwa paket Anda belum dibuka.

![JADE-PLUS-GREEN](assets/fr/02.webp)

Di dalam kotak Anda akan menemukan :


- Le Jade Plus;
- Kabel USB-C;
- Kartu untuk merekam frasa mnemonik Anda sebagai kata-kata atau sebagai "*CompactSeedQR*";
- Beberapa petunjuk penggunaan ;
- Sebuah kabel;
- Beberapa stiker.

![JADE-PLUS-GREEN](assets/fr/03.webp)

Perangkat ini memiliki 4 tombol navigasi:


- Tombol di kanan bawah menyalakan Jade;
- Tombol besar pada bagian depan perangkat digunakan untuk memilih item;
- Dua tombol kecil di bagian atas memungkinkan Anda menavigasi ke kiri dan ke kanan;
- Anda juga dapat memilih item dengan mengklik secara bersamaan pada dua tombol di bagian atas perangkat.

![JADE-PLUS-GREEN](assets/fr/04.webp)

## Menyiapkan dompet Bitcoin baru

Klik pada tombol mulai.

![JADE-PLUS-GREEN](assets/fr/05.webp)

Klik "*Setup Jade*".

![JADE-PLUS-GREEN](assets/fr/06.webp)

Pilih "Begin Setup" (Mulai Penyiapan). Opsi "*Advanced Setup*" melakukan hal yang sama, tetapi dengan akses ke pengaturan lanjutan.

![JADE-PLUS-GREEN](assets/fr/07.webp)

Kemudian klik "*Buat Dompet Baru*" untuk menghasilkan seed baru.

![JADE-PLUS-GREEN](assets/fr/08.webp)

Klik tombol "*Lanjutkan*" untuk menampilkan frasa pemulihan baru Anda.

![JADE-PLUS-GREEN](assets/fr/09.webp)

Jade Plus Anda akan menampilkan frasa mnemonik 12 kata. **Mnemonik ini memberikan Anda akses penuh dan tidak terbatas ke semua bitcoin Anda. Siapa pun yang memiliki frasa ini dapat mencuri dana Anda, bahkan tanpa akses fisik ke Jade Plus Anda. Frasa 12 kata ini akan mengembalikan akses ke bitcoin Anda jika terjadi kehilangan, pencurian, atau kerusakan pada Jade Anda. Oleh karena itu, sangat penting untuk menyimpannya dengan hati-hati dan menyimpannya di lokasi yang aman.

Anda bisa menuliskannya pada karton yang disertakan dalam kotak, atau untuk keamanan tambahan, saya sarankan untuk mengukirnya pada dasar baja tahan karat untuk melindunginya dari kebakaran, banjir atau keruntuhan.

![JADE-PLUS-GREEN](assets/fr/10.webp)

Untuk informasi lebih lanjut mengenai cara yang tepat untuk menyimpan dan mengelola frasa mnemonik Anda, saya sangat merekomendasikan untuk mengikuti tutorial lainnya, khususnya jika Anda seorang pemula:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
***Tentu saja, Anda tidak boleh membagikan kata-kata ini di Internet, seperti yang saya lakukan dalam tutorial ini. Portofolio contoh ini hanya akan digunakan di Testnet dan akan dihapus di akhir tutorial

Klik panah di sebelah kanan layar untuk menampilkan kata-kata berikut.

![JADE-PLUS-GREEN](assets/fr/11.webp)

Setelah Anda menyimpan frasa, Jade Plus akan meminta Anda untuk mengonfirmasinya. Pilih kata yang benar sesuai dengan urutannya menggunakan tombol di bagian atas perangkat, dan klik tombol tengah untuk beralih ke kata berikutnya.

![JADE-PLUS-GREEN](assets/fr/12.webp)

## Menghubungkan Jade Plus ke Green Wallet

Dalam tutorial ini, kita akan menggunakan aplikasi Green Wallet untuk mengelola dompet yang dihosting di Jade Plus. Metode ini sangat cocok untuk pemula. Jika Anda ingin mengelola dompet Bitcoin Anda secara lebih detail, Anda juga bisa menggunakan Sparrow Wallet, yang akan kita bahas dalam tutorial terpisah:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262
Untuk petunjuk tentang cara menginstal dan menyiapkan aplikasi Blockstream Green, silakan lihat bagian pertama dari tutorial ini:

https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143
Setelah berada di aplikasi Blockstream Green, klik tombol "*Konfigurasi portofolio baru*".

![JADE-PLUS-GREEN](assets/fr/13.webp)

Pilih "*Pada Dompet Perangkat Keras*".

![JADE-PLUS-GREEN](assets/fr/14.webp)

Aktifkan Bluetooth pada smartphone Anda, kemudian klik tombol "*Hubungkan Jade Anda*".

![JADE-PLUS-GREEN](assets/fr/15.webp)

Mengesahkan aplikasi Green untuk mengakses koneksi Bluetooth.

![JADE-PLUS-GREEN](assets/fr/16.webp)

Aplikasi sedang mencari Jade Plus Anda.

![JADE-PLUS-GREEN](assets/fr/17.webp)

Pada Jade Plus, klik menu "*Bluetooth*".

![JADE-PLUS-GREEN](assets/fr/18.webp)

Pilih perangkat Anda pada aplikasi Hijau.

![JADE-PLUS-GREEN](assets/fr/19.webp)

Konfirmasikan kode pemasangan pada Jade Plus Anda.

![JADE-PLUS-GREEN](assets/fr/20.webp)

Green menawarkan Anda sebuah tes untuk memastikan bahwa batu giok Anda asli. Klik pada tombol untuk melakukannya.

![JADE-PLUS-GREEN](assets/fr/21.webp)

Konfirmasikan pada Jade.

![JADE-PLUS-GREEN](assets/fr/22.webp)

Warna hijau mengonfirmasi bahwa perangkat Anda asli.

![JADE-PLUS-GREEN](assets/fr/23.webp)

## Mengatur kode PIN

Klik tombol "*Lanjutkan*" untuk memilih kode PIN Jade Anda.

![JADE-PLUS-GREEN](assets/fr/24.webp)

Kode PIN membuka kunci Giok Anda. Oleh karena itu, kode ini merupakan perlindungan terhadap akses fisik yang tidak sah. Kode PIN ini tidak terlibat dalam proses derivasi kunci kriptografi dompet Anda. Jadi, bahkan tanpa akses ke kode PIN ini, dengan memiliki frasa mnemonik 12 kata, Anda dapat memperoleh kembali akses ke bitcoin Anda. Kami menyarankan untuk memilih kode PIN yang seacak mungkin. Dan pastikan untuk menyimpan kode ini di lokasi yang terpisah dari tempat penyimpanan Jade Anda (misalnya, di pengelola kata sandi).

Pilih kode PIN 6 digit pada Jade Anda, dengan menggunakan tombol kanan dan kiri untuk menggulir angka, dan tombol tengah untuk mengonfirmasi entri angka.

![JADE-PLUS-GREEN](assets/fr/25.webp)

Konfirmasikan PIN Anda untuk kedua kalinya.

![JADE-PLUS-GREEN](assets/fr/26.webp)

Dompet bitcoin Anda telah dibuat.

![JADE-PLUS-GREEN](assets/fr/27.webp)

## Membuat akun Bitcoin

Sekarang Anda harus membuat akun dalam portofolio Anda. Klik tombol "*Buat akun*".

![JADE-PLUS-GREEN](assets/fr/28.webp)

Pilih "*Standard*" jika Anda ingin membuat portofolio single-sig klasik.

![JADE-PLUS-GREEN](assets/fr/29.webp)

Untuk informasi lebih lanjut tentang opsi "*2FA*", Anda dapat mengikuti tutorial lainnya:

https://planb.network/tutorials/wallet/mobile/blockstream-green-2FA-37397d5c-5c27-44ad-a27a-c9ceac8c9df9
Akun Anda telah dibuat.

![JADE-PLUS-GREEN](assets/fr/30.webp)

Jika Anda ingin mempersonalisasi portofolio Green Anda, klik pada tiga titik kecil di kanan atas.

![JADE-PLUS-GREEN](assets/fr/31.webp)

Opsi "*Rename*" memungkinkan Anda menyesuaikan nama portofolio Anda, yang sangat berguna jika Anda mengelola beberapa portofolio pada aplikasi yang sama. Menu "*Unit*" memungkinkan Anda mengubah unit dasar portofolio Anda. Sebagai contoh, Anda bisa memilih untuk menampilkannya dalam satuan satoshi daripada bitcoin. Terakhir, menu "*Parameter*" memberikan Anda akses ke opsi-opsi lain. Di sini, misalnya, Anda akan menemukan kunci publik yang diperluas dan deskriptornya, yang berguna jika Anda berencana untuk membuat dompet khusus jam tangan dari Jade Anda.

![JADE-PLUS-GREEN](assets/fr/32.webp)

Untuk menyambungkan kembali ke Jade Anda setelah mematikannya, tekan tombol on/off di bagian bawah perangkat. Pada aplikasi Hijau, pilih perangkat Anda dari halaman beranda:

![JADE-PLUS-GREEN](assets/fr/33.webp)

Kemudian masukkan kode PIN pada Jade Anda, dan Anda akan terhubung kembali.

![JADE-PLUS-GREEN](assets/fr/34.webp)

Jade Anda dibuka kuncinya melalui "elemen aman virtual" Blockstream (lihat bagian pertama tutorial ini). Hal ini memerlukan koneksi Bluetooth dengan aplikasi Green. Jika Anda mengalami kesulitan dengan koneksi Bluetooth saat membuka kunci, coba pisahkan dan hubungkan kembali kedua perangkat. Jika masalah masih berlanjut, Anda masih dapat membuka kunci Jade Anda dengan memilih opsi "*QR Scan*" dan mengikuti petunjuk yang tersedia [di situs web Blockstream] (https://jadefw.blockstream.com/pinqr/index.html).

Sebelum Anda menerima bitcoin pertama Anda di dompet Anda, **Saya sangat menyarankan Anda untuk melakukan tes pemulihan kosong**. Catatlah beberapa informasi referensi, seperti xpub atau alamat penerima pertama Anda, kemudian hapus wallet Anda di aplikasi Green dan di Jade Plus ketika masih kosong (`Options -> Device -> Factory Reset`). Kemudian coba pulihkan dompet Anda menggunakan cadangan kertas dari frasa mnemonik. Periksa apakah informasi cookie yang dihasilkan setelah pemulihan sesuai dengan yang Anda tuliskan sebelumnya. Jika sesuai, Anda dapat yakin bahwa cadangan kertas Anda dapat diandalkan. Untuk mengetahui lebih lanjut mengenai cara melakukan pemulihan uji coba, silakan baca tutorial lainnya:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895
## Menerima bitcoin

Setelah dompet Bitcoin Anda siap, Anda siap untuk menerima satoshi pertama Anda! Cukup klik tombol "*Terima*" pada aplikasi berwarna hijau.

![JADE-PLUS-GREEN](assets/fr/35.webp)

Warna hijau menampilkan alamat penerimaan, tetapi sebelum menggunakannya, sangat penting untuk memeriksanya di Jade untuk mengonfirmasi bahwa alamat tersebut benar-benar milik portofolio kami. Untuk melakukannya, klik tombol "*Verify on device*".

![JADE-PLUS-GREEN](assets/fr/36.webp)

Periksa pada Jade bahwa alamatnya sama dengan yang ada di Green, lalu klik tombol untuk mengonfirmasi.

![JADE-PLUS-GREEN](assets/fr/37.webp)

Sekarang Anda bisa membagikan alamat tersebut kepada pembayar untuk menerima bitcoin di dompet Anda. Ketika transaksi disiarkan di jaringan, transaksi tersebut akan muncul di dompet Anda. Tunggu hingga Anda menerima konfirmasi yang cukup untuk menganggap transaksi tersebut sudah pasti.

![JADE-PLUS-GREEN](assets/fr/38.webp)

## Kirim bitcoin

Dengan bitcoin di dompet Anda, Anda sekarang juga dapat mengirim bitcoin. Klik "*Kirim*".

![JADE-PLUS-GREEN](assets/fr/39.webp)

Pada halaman berikutnya, masukkan alamat penerima. Anda dapat memasukkannya secara manual atau memindai kode QR.

![JADE-PLUS-GREEN](assets/fr/40.webp)

Pilih jumlah pembayaran.

![JADE-PLUS-GREEN](assets/fr/41.webp)

Di bagian bawah layar, Anda dapat memilih tarif biaya untuk transaksi ini. Anda dapat memilih untuk mengikuti rekomendasi aplikasi atau menyesuaikan biaya Anda. Semakin tinggi biaya dalam kaitannya dengan transaksi tertunda lainnya, semakin cepat transaksi Anda akan diproses. Untuk informasi pasar biaya, silakan kunjungi [Mempool.space] (https://mempool.space/) di bagian "*Biaya Transaksi*".

![JADE-PLUS-GREEN](assets/fr/42.webp)

Klik "*Selanjutnya*" untuk mengakses layar ringkasan transaksi. Periksa apakah alamat, jumlah, dan biaya sudah benar.

![JADE-PLUS-GREEN](assets/fr/43.webp)

Jika semua berjalan lancar, geser tombol hijau di bagian bawah layar ke kanan untuk menandatangani dan menyiarkan transaksi di jaringan Bitcoin.

![JADE-PLUS-GREEN](assets/fr/44.webp)

Anda sekarang diminta untuk mengonfirmasi transaksi di Jade.

![JADE-PLUS-GREEN](assets/fr/45.webp)

Pastikan alamat penerima sudah benar. Klik tanda centang untuk mengonfirmasi.

![JADE-PLUS-GREEN](assets/fr/46.webp)

Periksa apakah jumlah tagihan sudah benar, lalu validasi.

![JADE-PLUS-GREEN](assets/fr/47.webp)

Transaksi Anda telah ditandatangani dan disiarkan dari Green.

![JADE-PLUS-GREEN](assets/fr/48.webp)

Selamat, sekarang Anda sudah mengetahui cara mengatur dan menggunakan Jade Plus dengan aplikasi seluler Blockstream Green, melalui koneksi Bluetooth. Jika Anda merasa tutorial ini bermanfaat, saya akan berterima kasih jika Anda memberikan jempol hijau di bawah ini. Jangan ragu untuk membagikan artikel ini di jejaring sosial Anda. Terima kasih telah berbagi!

Untuk melangkah lebih jauh, saya merekomendasikan tutorial tentang Jade Plus ini, di mana kita mengonfigurasikannya dengan perangkat lunak Sparrow Wallet dalam mode QR. Anda juga akan mempelajari cara menggunakan pengaturan lanjutan dari dompet perangkat keras Anda:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262