---
name: Jade Plus - Sparrow
description: Konfigurasi lanjutan Jade Plus dengan Dompet Sparrow
---
![cover](assets/cover.webp)

Jade Plus adalah hardware wallet khusus Bitcoin yang dirancang oleh Blockstream. Wallet ini merupakan penerus Jade klasik, dengan peningkatan perangkat lunak, lebih banyak opsi, dan ergonomi yang didesain ulang untuk penggunaan yang lebih intuitif. Versi baru ini menawarkan layar LCD 1,9 inci yang luar biasa, dengan gamut warna lebih luas dari pendahulunya. Tombol dan navigasi menu juga telah dioptimalkan.

Jade Plus dapat digunakan dalam beberapa cara: melalui koneksi kabel USB-C, dalam mode "*Air-Gap*" dengan kartu micro SD (memerlukan adaptor), melalui Bluetooth, atau bahkan dengan menukarkan kode QR berkat kamera terintegrasi. Hardware wallet ini bertenaga baterai.

Wallet ini tersedia mulai dari $149,99 dalam versi hitam dasar, dan harganya bisa naik hingga $20 untuk versi "*Genesis Grey*" atau "*Lunar Silver*". Oleh karena itu, Jade Plus adalah pilihan menarik, dengan fungsi canggih yang sebanding dengan hardware wallet kelas atas seperti Coldcard Q atau Passport V2, tetapi dengan harga cukup rendah, mendekati model kelas menengah.


![JADE-PLUS-SPARROW](assets/fr/01.webp)

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

Dalam tutorial ini, kita akan menyiapkan konfigurasi lanjutan Jade Plus dengan perangkat lunak Sparrow Wallet desktop dalam mode kode QR. Konfigurasi ini sangat ideal untuk pengguna tingkat menengah atau berpengalaman. Jika kamu mencari pendekatan yang lebih sederhana untuk pemula, aku menyarankanmu melihat tutorial ini, di mana kita menggunakan Jade Plus dengan Green Wallet melalui koneksi Bluetooth:

https://planb.academy/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0

## Model keamanan Jade Plus

Jade Plus menggunakan model keamanan berdasarkan "elemen aman virtual", yang diwujudkan oleh "blind oracle". Secara konkret, mekanisme ini menggabungkan PIN yang dipilih pengguna, sebuah rahasia yang disimpan di Jade, dan sebuah rahasia yang dipegang oleh oracle (server yang dikelola Blockstream) untuk membuat kunci AES-256 yang didistribusikan ke dua entitas. Selama inisiasi, pertukaran ECDH mengamankan komunikasi dengan oracle dan mengenkripsi seed pada hardware wallet. Secara praktis, ketika kamu ingin mengakses seed untuk menandatangani transaksi, kamu membutuhkan akses ke:


- Perangkat Jade Plus itu sendiri
- PIN untuk membuka kunci perangkat
- Rahasia yang disimpan di oracle

Keuntungan utama dari pendekatan ini adalah tidak adanya satu titik kegagalan pada tingkat hardware, karena jika penyerang mendapatkan akses ke Jade kamu, mengekstraksi kunci membutuhkan kompromi secara bersamaan dengan Jade dan oracle. Model ini juga sepenuhnya open-source, sehingga menghindari keterbatasan yang biasanya terkait dengan penggunaan elemen keamanan fisik, seperti yang digunakan pada Ledger.

Kerugian dari sistem ini adalah penggunaan Jade Plus bergantung pada oracle yang dikelola Blockstream. Jika oracle ini tidak dapat diakses, maka tidak mungkin lagi menggunakan hardware wallet secara langsung dengan PIN. Namun, ini tidak berarti bitcoin kamu hilang, karena bitcoin tersebut masih bisa dipulihkan dengan menggunakan seed, yang dapat kamu masukkan di Jade Plus dalam mode "*stateless*". Untuk mengurangi ketergantungan ini, kamu juga bisa mengonfigurasi dan mengelola server oracle sendiri.


Pilihan lain untuk mengelola seed kamu adalah dengan tidak mendaftarkannya pada Jade Plus. Dalam hal ini, Jade hanya menjadi perangkat tanda tangan saja. Selama inisialisasi, selain menyimpan seed biasa berupa kata-kata, kamu juga bisa menyimpannya sebagai kode QR yang dibuat sendiri. Dengan cara ini, setiap kali kamu menggunakan wallet, kamu dapat mengimpor seed menggunakan kamera Jade. Ini bisa menjadi opsi menarik untuk pengguna tingkat lanjut, tergantung pada strategi keamanan kamu, tetapi kamu harus berhati-hati dalam menyimpan dan melindungi seed, karena meskipun dalam bentuk kode QR, ini memungkinkan siapa saja untuk mencuri dana kamu. Kita akan melihat opsi ini dalam tutorial ini, tetapi tidak wajib.

## Membuka kemasan Jade Plus

Ketika kamu menerima Jade Plus, periksa apakah kotak dan segelnya dalam kondisi baik untuk memastikan paket kamu belum dibuka.

![JADE-PLUS-SPARROW](assets/fr/02.webp)

Di dalam kotak kamu akan menemukan :


- Le Jade Plus
- Kabel USB-C
- Kartu untuk merekam seed kamu sebagai kata-kata atau sebagai "*CompactSeedQR*"
- Beberapa petunjuk penggunaan
- Sebuah kabel
- Beberapa stiker


![JADE-PLUS-SPARROW](assets/fr/03.webp)

Di dalam kotak kamu akan menemukan :


- Le Jade Plus
- Kabel USB-C
- Kartu untuk merekam seed kamu sebagai kata-kata atau sebagai "*CompactSeedQR*"
- Beberapa petunjuk penggunaan
- Sebuah kabel
- Beberapa stiker


![JADE-PLUS-SPARROW](assets/fr/04.webp)

## Menyiapkan dompet Bitcoin baru

Klik pada tombol mulai.

![JADE-PLUS-SPARROW](assets/fr/05.webp)

Klik "*Setup Jade*".

![JADE-PLUS-SPARROW](assets/fr/06.webp)

Pilih "Pengaturan Lanjutan".

![Image](assets/fr/07.webp)

Kemudian klik "*Buat Dompet Baru*" untuk membuat seed baru. Kamu bisa memilih antara seed 12 atau 24 kata. Keamanan wallet kamu tetap setara dengan kedua opsi tersebut, jadi mungkin lebih mudah memilih opsi yang paling sederhana untuk disimpan, yaitu 12 kata.

![Image](assets/fr/08.webp)

Klik tombol "*Lanjutkan*" untuk menampilkan frasa pemulihan baru kamu.

![Image](assets/fr/09.webp)

Jade Plus kamu akan menampilkan seed 12 kata. **Seed ini memberikan kamu akses penuh dan tidak terbatas ke semua bitcoin kamu. Siapa pun yang memiliki seed ini dapat mencuri dana kamu, bahkan tanpa akses fisik ke Jade Plus. Seed 12 kata ini akan mengembalikan akses ke bitcoin kamu jika terjadi kehilangan, pencurian, atau kerusakan pada Jade. Oleh karena itu, sangat penting untuk menyimpannya dengan hati-hati dan di lokasi yang aman.**

Kamu bisa menuliskannya pada karton yang disertakan dalam kotak, atau untuk keamanan tambahan, saya sarankan mengukirnya pada dasar baja tahan karat agar terlindungi dari kebakaran, banjir, atau keruntuhan.

![Image](assets/fr/10.webp)

Untuk informasi lebih lanjut mengenai cara yang tepat untuk menyimpan dan mengelola seed kamu, saya sangat merekomendasikan mengikuti tutorial lainnya, khususnya jika kamu pemula:

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Tentu saja, kamu tidak boleh membagikan kata-kata ini di Internet, seperti yang saya lakukan dalam tutorial ini. Portofolio contoh ini hanya akan digunakan di Testnet dan akan dihapus di akhir tutorial.

Klik panah di sebelah kanan layar untuk menampilkan kata-kata berikut.

![Image](assets/fr/11.webp)

Setelah kamu menyimpan seed, Jade Plus akan meminta kamu untuk mengonfirmasinya. Pilih kata yang benar sesuai urutannya menggunakan tombol di bagian atas perangkat, dan klik tombol tengah untuk beralih ke kata berikutnya.

![Image](assets/fr/12.webp)

Kamu kemudian memiliki 2 opsi. Seperti yang dijelaskan pada bagian pendahuluan, kamu bisa memilih untuk menyimpan seed secara langsung di perangkat dan menggunakan sistem proteksi "*Virtual Secure Element*" dari Blockstream untuk mengakses wallet kamu (Opsi 1), atau menyimpan seed dalam bentuk kode QR dan memindainya setiap kali digunakan (Opsi 2).

Untuk Opsi 1, pilih "*Tidak*", dan untuk Opsi 2, pilih "*Ya*".


![Image](assets/fr/13.webp)

### Opsi 1: Buka Kunci PIN QR

Jika kamu telah memilih Opsi 1 (CompactSeedQR: "*No*"), kamu akan langsung dibawa ke pilihan metode koneksi. Dalam tutorial ini, kita ingin menggunakan perangkat dalam mode Air-Gapped melalui pertukaran kode QR, jadi pilih "*QR*".

![Image](assets/fr/27.webp)

Klik "*Lanjutkan*".

![Image](assets/fr/28.webp)

Kode PIN digunakan untuk membuka kunci Jade kamu dan menawarkan perlindungan terhadap akses fisik yang tidak sah. Kode PIN ini tidak terlibat dalam derivasi kunci kriptografi wallet kamu. Jadi, bahkan tanpa akses ke kode PIN ini, dengan memiliki seed 12 kata, kamu masih bisa memperoleh kembali akses ke bitcoin kamu. Kami menyarankan memilih kode PIN yang seacak mungkin. Selain itu, pastikan menyimpan kode ini di tempat terpisah dari tempat penyimpanan Jade, misalnya di pengelola kata sandi.

Pilih kode PIN 6 digit pada Jade kamu, menggunakan tombol kiri dan kanan untuk menggulir angka, dan tombol tengah untuk mengonfirmasi setiap angka.


![Image](assets/fr/29.webp)

Konfirmasikan PIN kamu untuk kedua kalinya.

![Image](assets/fr/30.webp)

Seperti yang dijelaskan pada bagian pendahuluan, seed kamu disimpan secara terenkripsi di Jade Plus. Untuk mendekripsinya, kamu harus menyediakan file:


- Kode PIN yang valid (yang baru saja kita siapkan)
- Rahasia oracle yang dikelola Blockstream

Dalam tutorial lanjutan ini, kita akan menggunakan Sparrow Wallet untuk mengelola wallet Bitcoin kita. Namun, tidak seperti perangkat lunak Green Wallet dari Blockstream, Sparrow tidak memiliki akses ke oracle di server Blockstream. Oleh karena itu, kita akan menggunakan situs web Blockstream untuk mengambil rahasia oracle setiap kali membuka kunci Jade Plus.

Kunjungi https://jadefw.blockstream.com/pinqr/index.html

Klik "*Mulai Buka Kunci QR*".

![Image](assets/fr/31.webp)

Klik "*Selesai*", karena kamu telah memilih PIN kamu di Jade Plus.

![Image](assets/fr/32.webp)

Gunakan kamera komputer kamu untuk memindai kode QR yang ditampilkan pada layar Jade kamu.

![Image](assets/fr/33.webp)

Konfirmasikan pada Jade kamu untuk mengakses layar berikutnya.

![Image](assets/fr/34.webp)

Pindai kode QR yang sekarang terlihat di situs web untuk mendapatkan rahasia oracle.

![Image](assets/fr/35.webp)

Sekarang portofolio kamu telah dibuat, kamu dapat melanjutkan ke langkah berikutnya dan melewatkan sub-bagian "*Opsi 2: CompactSeedQR*".

![Image](assets/fr/36.webp)

Setiap kali kamu memulai, klik "*QR Mode*".

![Image](assets/fr/37.webp)

Pilih "*Kunci PIN QR*".

![Image](assets/fr/38.webp)

Masukkan kode PIN kamu.

![Image](assets/fr/39.webp)

Kemudian buka [situs web Blockstream](https://jadefw.blockstream.com/pinqr/qrpin.html) untuk menukar kode QR dengan oracle.

![Image](assets/fr/40.webp)

Jade kamu sekarang tidak terkunci.

![Image](assets/fr/41.webp)

### Opsi 2: CompactSeedQR

Jika kamu telah memilih Opsi 2 (CompactSeedQR: "*Ya*"), klik "*Ya*" sekali lagi.

![Image](assets/fr/14.webp)

Klik "*Mulai*".

![Image](assets/fr/15.webp)

Kamu dapat menggunakan basis kode QR yang disediakan dalam kotak Jade Plus. Pilih kotak yang sesuai, tergantung pada apakah Anda memilih kalimat 12 atau 24 kata. Kamu juga dapat [mencetak template dari situs web Blockstream](https://help.blockstream.com/hc/article_attachments/41928319071769).

Jade Plus kamu akan menampilkan setiap zona kode QR kamu.

![Image](assets/fr/16.webp)

Gunakan pena untuk mewarnai kotak-kotak tersebut dan mereproduksi seed kamu sebagai kode QR. Lakukan dengan tepat agar kamera Jade Plus dapat memindainya nanti. Gunakan tanda panah untuk berpindah ke area berikutnya.

![Image](assets/fr/17.webp)

Setelah selesai, klik "*Selesai*".

![Image](assets/fr/18.webp)

Pindai kode QR buatan tangan kamu dengan Jade Plus untuk memeriksa keabsahannya.

![Image](assets/fr/19.webp)

Jika cadangan kertas kamu sudah benar, klik "*Lanjutkan*".

![Image](assets/fr/20.webp)

Dalam tutorial ini, kita akan menggunakan mode koneksi berdasarkan pemindaian kode QR secara eksklusif, jadi pilih "*QR*".

![Image](assets/fr/21.webp)

Kamu juga bisa memilih untuk menambahkan PIN sebagai tambahan pada cadangan CompactSeedQR kamu, seperti pada Opsi 1. Ini menawarkan dua cara untuk mengakses wallet kamu: baik melalui PIN dan sistem "Virtual Secure Element" Blockstream, atau melalui CompactSeedQR.

Jika kamu memilih opsi PIN ganda, pilih "*PIN*" dan ikuti langkah yang sama seperti pada Opsi 1 untuk mengatur kode PIN kamu.

Jika kamu lebih suka melanjutkan dengan CompactSeedQR saja, pilih "*SeedQR*".


![Image](assets/fr/22.webp)

Setelah portofolio kamu selesai dibuat, kamu dapat melanjutkan ke langkah berikutnya.

![Image](assets/fr/23.webp)

Setiap kali kamu memulai, klik tombol "*QR Mode*", lalu "*Scan SeedQR*".

![Image](assets/fr/24.webp)

Gunakan kamera perangkat untuk memindai benih yang kamu simpan sebagai kode QR.

![Image](assets/fr/25.webp)

Jade kamu sekarang tidak terkunci.

![Image](assets/fr/26.webp)

## Menambahkan kata sandi BIP39

Kata sandi BIP39 adalah kata sandi opsional yang bisa kamu pilih secara bebas, dan ditambahkan ke seed kamu untuk memperkuat keamanan wallet. Dengan mengaktifkan fitur ini, akses ke wallet Bitcoin kamu akan membutuhkan seed dan kata sandi. Tanpa keduanya, mustahil memulihkan wallet.

Sebelum mengonfigurasi opsi ini pada Jade Plus kamu, sangat disarankan membaca artikel ini untuk memahami sepenuhnya operasi teoritis dari kata sandi dan menghindari kesalahan yang dapat menyebabkan hilangnya bitcoin kamu:

https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Dengan Jade kamu masih terkunci (kata sandi hanya dapat dimasukkan ketika perangkat tidak dibuka), akses menu "*Options*".


![Image](assets/fr/42.webp)

Pilih "*Seedphrase BIP39*".

![Image](assets/fr/43.webp)

Pada opsi "*Frequency*", kamu bisa memilih apakah Jade Plus akan meminta kamu memasukkan kata sandi setiap kali dijalankan:


- "*Disabled*" menonaktifkan penggunaan kata sandi
- "*Next Login Only*" akan mengharuskan kamu kembali ke menu ini untuk mengaktifkan permintaan kata sandi pada saat memulai berikutnya. Opsi ini memungkinkan kamu untuk tidak mengungkapkan penggunaannya
- "*Selalu Tanyakan*" membuat Jade secara sistematis meminta kata sandi setiap kali memulai, sehingga mengungkapkan bahwa wallet kamu dilindungi oleh kata sandi

Pilih opsi yang sesuai dengan strategi keamanan kamu. Secara pribadi, saya memilih "*Selalu Tanyakan*" sebagai contoh.


![Image](assets/fr/44.webp)

Kamu kemudian bisa memilih di antara dua metode untuk memasukkan kata sandi kamu:


- "*Manual*": Papan ketik virtual memungkinkan kamu memasukkan huruf (besar dan kecil), angka, dan simbol, karakter demi karakter. Ini adalah metode standar untuk semua hardware wallet
- "*Daftar Kata*": Metode khusus yang dirancang Blockstream untuk Jade, yang mempercepat pemasukan kata sandi dan meningkatkan entropinya. Selama input, sistem menyarankan kata-kata dari daftar BIP39, sehingga membuka kunci menjadi lebih mudah. Metode ini secara otomatis menghasilkan kalimat dengan menggabungkan kata-kata yang dipilih, dipisahkan oleh spasi (contoh: `kemampuan meninggalkan mampu`)

Secara pribadi, aku menyarankan menggunakan metode pertama, karena ini adalah standar yang akan kamu temukan pada semua dukungan wallet lainnya.


![Image](assets/fr/45.webp)

Kamu kemudian bisa kembali ke layar beranda dan membuka kunci wallet kamu seperti biasa, baik menggunakan kode PIN atau CompactSeedQR (seperti yang terlihat di atas). Kamu akan diminta memasukkan kata sandi kamu.

![Image](assets/fr/46.webp)

Masukkan pada keyboard Jade, dan pastikan membuat satu atau beberapa cadangan pada media fisik (kertas atau logam). Sebagai contoh, saya menggunakan kata sandi yang sangat lemah, tetapi kamu harus memilih kata sandi acak yang kuat yang mencakup semua jenis karakter dan cukup panjang (seperti kata sandi yang kuat).

![Image](assets/fr/47.webp)

Jika kata sandi kamu valid, konfirmasikan.

![Image](assets/fr/48.webp)

Harap diperhatikan bahwa kata sandi BIP39 peka terhadap huruf besar-kecil dan kesalahan pengetikan. Jika kamu memasukkan kata sandi yang sedikit berbeda dari yang dikonfigurasikan awalnya, Jade tidak akan melaporkan kesalahan, tetapi akan menghasilkan satu set kunci kriptografi lain yang tidak sama dengan kunci kriptografi di wallet awal kamu.

Oleh karena itu, sangat penting, saat mengonfigurasi, untuk mencatat sidik jari kunci utama kamu, yang dapat ditemukan di sudut kanan bawah layar. Misalnya, dengan kata sandi `Plan ₿ Academy`, sidik jari kunci utama saya adalah `3AD1AE65`.


![Image](assets/fr/49.webp)

Setiap kali kamu membuka kunci Jade dengan kata sandi, periksa apakah sidik jari sama dengan yang kamu catat saat konfigurasi. Jika ya, kata sandi kamu sudah benar dan kamu mengakses wallet Bitcoin yang tepat. Jika tidak, kamu menggunakan wallet yang salah dan perlu mencoba lagi. Berhati-hatilah agar tidak melakukan kesalahan input.

Sebelum kamu menerima bitcoin pertama di wallet kamu, **saya sangat menyarankan melakukan tes pemulihan kosong**. Catat beberapa informasi referensi, seperti xpub atau alamat penerima pertama, kemudian hapus wallet kamu di Jade Plus saat masih kosong (`Options -> Device -> Factory Reset`). Setelah itu, coba pulihkan wallet menggunakan cadangan kertas dari seed dan kata sandi yang ada. Periksa apakah informasi yang dihasilkan setelah pemulihan sesuai dengan yang kamu catat sebelumnya. Jika sesuai, kamu bisa yakin bahwa cadangan kertas kamu dapat diandalkan. Untuk mengetahui lebih lanjut tentang cara melakukan pemulihan tes, lihat tutorial lainnya:

https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Mengonfigurasi dompet di Dompet Sparrow

Dalam tutorial ini, saya menyajikan penggunaan tingkat lanjut Jade Plus menggunakan Sparrow Wallet. Namun, hardware wallet ini kompatibel dengan banyak program lain, seperti Liana, Nunchuk, Spectre, Green, dan Keeper. Kompatibilitas ini bervariasi tergantung pada metode koneksi: USB, Bluetooth, atau kode QR (lihat tabel di bagian pendahuluan untuk detailnya).

Mulailah dengan mengunduh dan menginstal Sparrow Wallet [dari situs web resmi](https://sparrowwallet.com/) di komputer kamu, jika kamu belum melakukannya.

![Image](assets/fr/50.webp)

Pastikan untuk memeriksa keaslian dan integritas perangkat lunak sebelum instalasi. Jika kamu tidak tahu cara melakukannya, silakan baca tutorial ini:

https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Setelah Sparrow Wallet terbuka, klik tab "*File*", lalu "*Dompet Baru*".

![Image](assets/fr/51.webp)

Beri nama dompet kamu, lalu klik "*Buat Dompet*".

![Image](assets/fr/52.webp)

Pilih "*Dompet Perangkat Keras yang Terisi Penuh*".

![Image](assets/fr/53.webp)

Klik "*Pindai...*" di samping opsi "*Jade*".

![Image](assets/fr/54.webp)

Buka kunci Jade Plus kamu dan, jika kamu menggunakannya, masukkan kata sandi kamu. Kemudian masuk ke menu "*Options*", pilih "*Wallet*", dan klik "*Export Xpub*".

![Image](assets/fr/55.webp)

Jade kamu akan menampilkan Keystore kamu melalui beberapa kode QR. Pindai kode-kode tersebut pada mesin menggunakan Sparrow.

![Image](assets/fr/56.webp)

Sekarang kamu akan melihat xpub dan sidik jari kunci utama, yang seharusnya cocok dengan yang ada di Jade Plus. Klik pada "*Terapkan*".

![Image](assets/fr/57.webp)

Tetapkan kata sandi yang kuat untuk mengamankan akses ke Sparrow Wallet kamu. Kata sandi ini akan melindungi kunci publik, alamat, label, dan riwayat transaksi kamu dari akses yang tidak sah. Sebaiknya simpan kata sandi ini di pengelola kata sandi agar kamu tidak lupa.

![Image](assets/fr/58.webp)

Portofolio kamu sekarang telah dikonfigurasi dengan benar di Sparrow.

![Image](assets/fr/59.webp)

## Menerima bitcoin

Setelah Jade Plus kamu dikonfigurasi, kamu siap menerima satoshi pertama di wallet Bitcoin baru kamu. Untuk melakukannya, di Sparrow, klik menu "*Receive*".

![Image](assets/fr/60.webp)

Sparrow akan menampilkan alamat penerimaan kosong pertama dalam portofolio kamu.

![Image](assets/fr/61.webp)

Sebelum menggunakannya, mari periksa di layar Jade Plus untuk memastikan wallet tersebut milik wallet Bitcoin kita. Di Jade, klik "*Scan QR*", lalu pindai kode QR dari alamat yang ditampilkan di Sparrow.

![Image](assets/fr/62.webp)

Periksa apakah alamat yang ditampilkan di layar Jade kamu sesuai dengan yang ditampilkan di Sparrow Wallet. Jika sesuai, klik tanda centang untuk melanjutkan.

![Image](assets/fr/63.webp)

Hardware wallet kamu kemudian akan mengonfirmasi bahwa alamat ini adalah bagian dari wallet kamu dan menyimpan kunci privat yang terkait.

![Image](assets/fr/64.webp)

Jika alamat tersebut divalidasi oleh Jade kamu, kamu bisa menggunakannya untuk menerima bitcoin. Ketika transaksi disiarkan di jaringan, transaksi tersebut akan muncul di Sparrow. Tunggu hingga kamu menerima konfirmasi yang cukup untuk menganggap transaksi tersebut sudah pasti.

![Image](assets/fr/65.webp)

## Kirim bitcoin

Sekarang setelah kamu memiliki beberapa satoshi di wallet kamu, kamu juga bisa mengirim sebagian. Untuk melakukannya, klik menu "*UTXOs*".

![Image](assets/fr/66.webp)

Pilih UTXO yang ingin kamu gunakan sebagai input untuk transaksi ini, lalu klik "*Kirim Terpilih*".

![Image](assets/fr/67.webp)

Masukkan alamat penerima, label untuk mengingatkan kamu tentang tujuan transaksi dan jumlah yang ingin Anda kirim ke alamat ini.

![Image](assets/fr/68.webp)

Sesuaikan tarif biaya sesuai dengan kondisi pasar saat ini, lalu klik "*Buat Transaksi*".

![Image](assets/fr/69.webp)

Pastikan semua parameter transaksi sudah benar, lalu klik "*Finalisasi Transaksi untuk Penandatanganan*".

![Image](assets/fr/70.webp)

Klik "*Show QR*" untuk menampilkan PSBT (*Partially Signed Bitcoin Transaction*). Sparrow telah membuat transaksi, tetapi belum memiliki tanda tangan untuk membuka kunci bitcoin yang digunakan dalam input. Tanda tangan ini hanya dapat dilakukan oleh Jade Plus, yang menyimpan seed kamu dan memberikan akses ke kunci privat yang diperlukan untuk menandatangani transaksi.

![Image](assets/fr/71.webp)

Di Jade Plus kamu, klik "*Scan QR*" untuk memindai PSBT yang ditampilkan di Sparrow.

![Image](assets/fr/72.webp)

Konfirmasikan bahwa alamat pengiriman dan jumlah yang dikirim sudah benar, lalu klik tanda panah untuk memvalidasi.

![Image](assets/fr/73.webp)

Pastikan jumlah biaya sesuai dengan yang kamu pilih, lalu klik ikon centang di sudut kiri atas antarmuka untuk menandatangani transaksi.

![Image](assets/fr/74.webp)

Pada Sparrow Wallet, klik "*Scan QR*" dan pindai kode QR yang ditampilkan pada Jade kamu.

![Image](assets/fr/75.webp)

Transaksi yang kamu tandatangani sekarang siap untuk disiarkan di jaringan Bitcoin dan dimasukkan ke dalam blok oleh penambang. Jika semuanya sudah benar, klik "*Siarkan Transaksi*".

![Image](assets/fr/76.webp)

Transaksi kamu telah disiarkan dan menunggu konfirmasi.

![Image](assets/fr/77.webp)

Selamat, sekarang kamu sudah tahu cara mengatur dan menggunakan Jade Plus dalam mode QR. Jika kamu merasa tutorial ini bermanfaat, saya akan berterima kasih jika kamu memberikan jempol hijau di bawah ini. Jangan ragu untuk membagikan artikel ini di jejaring sosial kamu. Terima kasih telah berbagi!

Untuk melangkah lebih jauh, saya merekomendasikan tutorial lain tentang Jade Plus, di mana kita mengonfigurasinya melalui Bluetooth dengan aplikasi seluler Green:

https://planb.academy/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0
