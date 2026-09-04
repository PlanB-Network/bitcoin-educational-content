---
name: Jade Plus - Green
description: Konfigurasikan Jade Plus dengan mudah dengan Green
---
![cover](assets/cover.webp)

Jade Plus adalah hardware wallet khusus Bitcoin yang dirancang oleh Blockstream. Wallet ini merupakan penerus Jade klasik, dengan peningkatan perangkat lunak, lebih banyak opsi, dan ergonomi yang didesain ulang untuk penggunaan yang lebih intuitif. Versi baru ini menawarkan layar LCD 1,9 inci yang luar biasa, dengan gamut warna lebih luas dari pendahulunya. Tombol dan navigasi menu juga telah dioptimalkan.

Jade Plus dapat digunakan dalam beberapa cara: melalui koneksi kabel USB-C, dalam mode "*Air-Gap*" dengan kartu micro SD (memerlukan adaptor), melalui Bluetooth, atau bahkan dengan menukarkan kode QR berkat kamera terintegrasi. Hardware wallet ini bertenaga baterai.

Wallet ini tersedia mulai dari $149,99 dalam versi hitam dasar, dan harganya bisa naik hingga $20 untuk versi "*Genesis Grey*" atau "*Lunar Silver*". Oleh karena itu, Jade Plus adalah pilihan menarik, dengan fungsi canggih yang sebanding dengan hardware wallet kelas atas seperti Coldcard Q atau Passport V2, tetapi dengan harga cukup rendah, mendekati model kelas menengah.


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

Dalam tutorial ini, kita akan mengatur dan menggunakan Jade Plus dengan aplikasi seluler Green Wallet Blockstream melalui koneksi Bluetooth. Pengaturan ini sangat ideal untuk pemula. Jika kamu mencari pendekatan yang lebih canggih, saya sarankan melihat tutorial ini di mana kita menggunakan Jade Plus dengan Sparrow Wallet dalam mode kode QR:

https://planb.academy/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

## Model keamanan Jade Plus

Jade Plus menggunakan model keamanan berdasarkan "elemen aman virtual", yang diwujudkan oleh "blind oracle". Secara konkret, mekanisme ini menggabungkan PIN yang dipilih pengguna, sebuah rahasia yang disimpan di Jade, dan sebuah rahasia yang dipegang oleh oracle (server yang dikelola Blockstream), untuk membuat kunci AES-256 yang didistribusikan ke dua entitas. Selama inisiasi, pertukaran ECDH mengamankan komunikasi dengan oracle, dan mengenkripsi seed pada hardware wallet. Secara praktis, ketika kamu ingin mengakses seed untuk menandatangani transaksi, kamu membutuhkan akses ke:


- Perangkat Jade Plus itu sendiri
- PIN untuk membuka kunci perangkat
- Oracle Secret

Keuntungan utama dari pendekatan ini adalah tidak adanya satu titik kegagalan pada tingkat hardware, karena jika penyerang mendapatkan akses ke Jade kamu, mengekstraksi kunci membutuhkan kompromi secara bersamaan dengan Jade dan oracle. Model ini juga berarti bahwa Jade Plus sepenuhnya open-source, menghindari kendala yang terkait dengan penggunaan elemen keamanan fisik yang sebenarnya, seperti yang digunakan pada Ledger, misalnya.


Kerugian dari sistem ini adalah penggunaan Jade Plus bergantung pada oracle yang dikelola Blockstream. Jika oracle ini tidak dapat diakses, maka tidak mungkin lagi menggunakan hardware wallet secara langsung dengan PIN. Namun, ini tidak berarti bitcoin kamu hilang, karena bitcoin tersebut masih bisa dipulihkan dengan menggunakan seed, yang dapat kamu masukkan di Jade Plus dalam mode "*stateless*". Untuk mengurangi ketergantungan ini, kamu juga bisa mengonfigurasi dan mengelola server oracle sendiri.

## Membuka kemasan Jade Plus

Ketika kamu menerima Jade Plus, periksa apakah kotak dan segelnya dalam kondisi baik untuk memastikan paket kamu belum dibuka.

![JADE-PLUS-GREEN](assets/fr/02.webp)

Di dalam kotak kamu akan menemukan :


- Le Jade Plus
- Kabel USB-C
- Kartu untuk merekam seed kamu sebagai kata-kata atau sebagai "*CompactSeedQR*"
- Beberapa petunjuk penggunaan
- Sebuah kabel
- Beberapa stiker


![JADE-PLUS-GREEN](assets/fr/03.webp)

Perangkat ini memiliki 4 tombol navigasi:


- Tombol di kanan bawah menyalakan Jade
- Tombol besar di bagian depan perangkat digunakan untuk memilih item
- Dua tombol kecil di bagian atas memungkinkan kamu menavigasi ke kiri dan ke kanan
- Kamu juga bisa memilih item dengan mengklik secara bersamaan kedua tombol di bagian atas perangkat

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

Klik tombol "*Lanjutkan*" untuk menampilkan frasa pemulihan baru kamu.

![JADE-PLUS-GREEN](assets/fr/09.webp)

Jade Plus kamu akan menampilkan seed 12 kata. **Seed ini memberikan kamu akses penuh dan tidak terbatas ke semua bitcoin kamu. Siapa pun yang memiliki seed ini dapat mencuri dana kamu, bahkan tanpa akses fisik ke Jade Plus. Seed 12 kata ini akan mengembalikan akses ke bitcoin kamu jika terjadi kehilangan, pencurian, atau kerusakan pada Jade. Oleh karena itu, sangat penting untuk menyimpannya dengan hati-hati dan di lokasi yang aman.**

Kamu bisa menuliskannya pada karton yang disertakan dalam kotak, atau untuk keamanan tambahan, saya sarankan mengukirnya pada dasar baja tahan karat agar terlindungi dari kebakaran, banjir, atau keruntuhan.

![JADE-PLUS-GREEN](assets/fr/10.webp)

Untuk informasi lebih lanjut mengenai cara yang tepat untuk menyimpan dan mengelola seed kamu, saya sangat merekomendasikan mengikuti tutorial lainnya, khususnya jika kamu pemula:

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Tentu saja, kamu tidak boleh membagikan kata-kata ini di Internet, seperti yang saya lakukan dalam tutorial ini. Portofolio contoh ini hanya akan digunakan di Testnet dan akan dihapus di akhir tutorial.**

Klik panah di sebelah kanan layar untuk menampilkan kata-kata berikut.


![JADE-PLUS-GREEN](assets/fr/11.webp)

Setelah kamu menyimpan seed, Jade Plus akan meminta kamu untuk mengonfirmasinya. Pilih kata yang benar sesuai urutannya menggunakan tombol di bagian atas perangkat, dan klik tombol tengah untuk beralih ke kata berikutnya.

![JADE-PLUS-GREEN](assets/fr/12.webp)

## Menghubungkan Jade Plus ke Green Wallet

Dalam tutorial ini, kita akan menggunakan aplikasi Green Wallet untuk mengelola wallet yang dihosting di Jade Plus. Metode ini sangat cocok untuk pemula. Jika kamu ingin mengelola wallet Bitcoin kamu secara lebih detail, kamu juga bisa menggunakan Sparrow Wallet, yang akan dibahas dalam tutorial terpisah:

https://planb.academy/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

Untuk petunjuk tentang cara menginstal dan menyiapkan aplikasi Blockstream Green, silakan lihat bagian pertama dari tutorial ini:

https://planb.academy/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

Setelah berada di aplikasi Blockstream Green, klik tombol "*Konfigurasi portofolio baru*".

![JADE-PLUS-GREEN](assets/fr/13.webp)

Pilih "*Pada Dompet Perangkat Keras*".

![JADE-PLUS-GREEN](assets/fr/14.webp)

Aktifkan Bluetooth pada smartphone kamu, kemudian klik tombol "*Hubungkan Jade Anda*".

![JADE-PLUS-GREEN](assets/fr/15.webp)

Mengesahkan aplikasi Green untuk mengakses koneksi Bluetooth.

![JADE-PLUS-GREEN](assets/fr/16.webp)

Aplikasi sedang mencari Jade Plus kamu.

![JADE-PLUS-GREEN](assets/fr/17.webp)

Pada Jade Plus, klik menu "*Bluetooth*".

![JADE-PLUS-GREEN](assets/fr/18.webp)

Pilih perangkat kamu pada aplikasi Hijau.

![JADE-PLUS-GREEN](assets/fr/19.webp)

Konfirmasikan kode pemasangan pada Jade Plus kamu.

![JADE-PLUS-GREEN](assets/fr/20.webp)

Green menawarkanmu sebuah tes untuk memastikan bahwa Jade milikmu asli. Klik pada tombol untuk melakukannya.

![JADE-PLUS-GREEN](assets/fr/21.webp)

Konfirmasikan pada Jade.

![JADE-PLUS-GREEN](assets/fr/22.webp)

Warna hijau mengonfirmasi bahwa perangkat kamu asli.

![JADE-PLUS-GREEN](assets/fr/23.webp)

## Mengatur kode PIN

Klik tombol "*Lanjutkan*" untuk memilih kode PIN Jade kamu.

![JADE-PLUS-GREEN](assets/fr/24.webp)

Kode PIN membuka kunci Jade kamu. Oleh karena itu, kode ini berfungsi sebagai perlindungan terhadap akses fisik yang tidak sah. Kode PIN ini tidak terlibat dalam proses derivasi kunci kriptografi wallet kamu. Jadi, bahkan tanpa akses ke kode PIN ini, dengan memiliki seed 12 kata, kamu masih bisa memperoleh kembali akses ke bitcoin kamu. Kami menyarankan memilih kode PIN yang seacak mungkin, dan pastikan menyimpannya di lokasi terpisah dari tempat penyimpanan Jade (misalnya, di pengelola kata sandi).

Pilih kode PIN 6 digit pada Jade kamu, menggunakan tombol kanan dan kiri untuk menggulir angka, dan tombol tengah untuk mengonfirmasi setiap entri angka.


![JADE-PLUS-GREEN](assets/fr/25.webp)

Konfirmasikan PIN kamu untuk kedua kalinya.

![JADE-PLUS-GREEN](assets/fr/26.webp)

Dompet bitcoin kamu telah dibuat.

![JADE-PLUS-GREEN](assets/fr/27.webp)

## Membuat akun Bitcoin

Sekarang kamu harus membuat akun dalam portofolio kamu. Klik tombol "*Buat akun*".

![JADE-PLUS-GREEN](assets/fr/28.webp)

Pilih "*Standard*" jika kamu ingin membuat portofolio single-sig klasik.

![JADE-PLUS-GREEN](assets/fr/29.webp)

Untuk informasi lebih lanjut tentang opsi "*2FA*", kamu dapat mengikuti tutorial lainnya:

https://planb.academy/tutorials/wallet/mobile/blockstream-green-2fa-37397d5c-5c27-44ad-a27a-c9ceac8c9df9

Akun Anda telah dibuat.

![JADE-PLUS-GREEN](assets/fr/30.webp)

Jika kamu ingin mempersonalisasi portofolio Green kamu, klik pada tiga titik kecil di kanan atas.

![JADE-PLUS-GREEN](assets/fr/31.webp)

Opsi "*Rename*" memungkinkan kamu menyesuaikan nama portofolio kamu, yang sangat berguna jika kamu mengelola beberapa portofolio pada aplikasi yang sama. Menu "*Unit*" memungkinkan kamu mengubah unit dasar portofolio. Misalnya, kamu bisa memilih menampilkannya dalam satuan satoshi daripada bitcoin. Terakhir, menu "*Parameter*" memberikan akses ke opsi-opsi lain. Di sini, misalnya, kamu akan menemukan kunci publik yang diperluas dan deskriptornya, yang berguna jika kamu berencana membuat wallet khusus dari Jade kamu.

![JADE-PLUS-GREEN](assets/fr/32.webp)

Untuk menyambungkan kembali ke Jade kamu setelah mematikannya, tekan tombol on/off di bagian bawah perangkat. Pada aplikasi Green, pilih perangkat kamu dari halaman beranda:

![JADE-PLUS-GREEN](assets/fr/33.webp)

Kemudian masukkan kode PIN pada Jade kamu, dan kamu akan terhubung kembali.

![JADE-PLUS-GREEN](assets/fr/34.webp)

Jade kamu dibuka kuncinya melalui "elemen aman virtual" Blockstream (lihat bagian pertama tutorial ini). Hal ini memerlukan koneksi Bluetooth dengan aplikasi Green. Jika kamu mengalami kesulitan dengan koneksi Bluetooth saat membuka kunci, coba pisahkan dan hubungkan kembali kedua perangkat. Jika masalah masih berlanjut, kamu masih bisa membuka kunci Jade dengan memilih opsi "*QR Scan*" dan mengikuti petunjuk yang tersedia [di situs web Blockstream](https://jadefw.blockstream.com/pinqr/index.html).

Sebelum kamu menerima bitcoin pertama di wallet kamu, **saya sangat menyarankan melakukan tes pemulihan kosong**. Catat beberapa informasi referensi, seperti xpub atau alamat penerima pertama, kemudian hapus wallet kamu di aplikasi Green dan di Jade Plus saat masih kosong (`Options -> Device -> Factory Reset`). Setelah itu, coba pulihkan wallet menggunakan cadangan kertas dari seed. Periksa apakah informasi yang dihasilkan setelah pemulihan sesuai dengan yang kamu catat sebelumnya. Jika sesuai, kamu bisa yakin bahwa cadangan kertas kamu dapat diandalkan. Untuk mengetahui lebih lanjut tentang cara melakukan pemulihan uji coba, silakan baca tutorial lainnya:

https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895


## Menerima bitcoin

Setelah wallet Bitcoin kamu siap, kamu siap untuk menerima satoshi pertama kamu! Cukup klik tombol "*Terima*" pada aplikasi Green.

![JADE-PLUS-GREEN](assets/fr/35.webp)

Warna hijau menampilkan alamat penerimaan, tetapi sebelum menggunakannya, sangat penting untuk memeriksanya di Jade untuk mengonfirmasi bahwa alamat tersebut benar-benar milik portofolio kami. Untuk melakukannya, klik tombol "*Verify on device*".

![JADE-PLUS-GREEN](assets/fr/36.webp)

Periksa pada Jade bahwa alamatnya sama dengan yang ada di Green, lalu klik tombol untuk mengonfirmasi.

![JADE-PLUS-GREEN](assets/fr/37.webp)

Sekarang kamu bisa membagikan alamat tersebut kepada pembayar untuk menerima bitcoin di wallet kamu. Ketika transaksi disiarkan di jaringan, transaksi akan muncul di wallet kamu. Tunggu hingga kamu menerima konfirmasi yang cukup untuk menganggap transaksi tersebut sudah pasti.

![JADE-PLUS-GREEN](assets/fr/38.webp)

## Kirim bitcoin

Dengan bitcoin di wallet kamu, kamu sekarang juga bisa mengirim bitcoin. Klik "*Kirim*".

![JADE-PLUS-GREEN](assets/fr/39.webp)

Pada halaman berikutnya, masukkan alamat penerima. Kamu bisa memasukkannya secara manual atau memindai kode QR.

![JADE-PLUS-GREEN](assets/fr/40.webp)

Pilih jumlah pembayaran.

![JADE-PLUS-GREEN](assets/fr/41.webp)

Di bagian bawah layar, kamu bisa memilih tarif biaya untuk transaksi ini. Kamu bisa mengikuti rekomendasi aplikasi atau menyesuaikan biaya sendiri. Semakin tinggi biaya dibanding transaksi lain yang tertunda, semakin cepat transaksi kamu akan diproses. Untuk informasi pasar biaya, silakan kunjungi [Mempool.space](https://mempool.space/) di bagian "*Biaya Transaksi*".

![JADE-PLUS-GREEN](assets/fr/42.webp)

Klik "*Selanjutnya*" untuk mengakses layar ringkasan transaksi. Periksa apakah alamat, jumlah, dan biaya sudah benar.

![JADE-PLUS-GREEN](assets/fr/43.webp)

Jika semua berjalan lancar, geser tombol hijau di bagian bawah layar ke kanan untuk menandatangani dan menyiarkan transaksi di jaringan Bitcoin.

![JADE-PLUS-GREEN](assets/fr/44.webp)

Kamu sekarang diminta untuk mengonfirmasi transaksi di Jade.

![JADE-PLUS-GREEN](assets/fr/45.webp)

Pastikan alamat penerima sudah benar. Klik tanda centang untuk mengonfirmasi.

![JADE-PLUS-GREEN](assets/fr/46.webp)

Periksa apakah jumlah tagihan sudah benar, lalu validasi.

![JADE-PLUS-GREEN](assets/fr/47.webp)

Transaksi Anda telah ditandatangani dan disiarkan dari Green.

![JADE-PLUS-GREEN](assets/fr/48.webp)

Selamat, sekarang kamu sudah mengetahui cara mengatur dan menggunakan Jade Plus dengan aplikasi seluler Blockstream Green melalui koneksi Bluetooth. Jika kamu merasa tutorial ini bermanfaat, saya akan berterima kasih jika kamu memberikan jempol hijau di bawah ini. Jangan ragu untuk membagikan artikel ini di jejaring sosial kamu. Terima kasih telah berbagi!

Untuk melangkah lebih jauh, saya merekomendasikan tutorial tentang Jade Plus ini, di mana kita mengonfigurasikannya dengan perangkat lunak Sparrow Wallet dalam mode QR. Kamu juga akan mempelajari cara menggunakan pengaturan lanjutan dari hardware wallet kamu:

https://planb.academy/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262



