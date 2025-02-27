---
name: Jade Plus - Burung Gereja
description: Konfigurasi lanjutan Jade Plus dengan Dompet Sparrow
---
![cover](assets/cover.webp)

Jade Plus adalah dompet perangkat keras khusus Bitcoin yang dirancang oleh Blockstream. Dompet ini merupakan penerus Jade klasik, dengan peningkatan perangkat lunak, lebih banyak opsi, dan ergonomi yang didesain ulang untuk penggunaan yang lebih intuitif. Versi baru ini menawarkan layar LCD 1,9 inci yang luar biasa, dengan gamut warna yang lebih luas dari pendahulunya. Tombol dan navigasi menu juga telah dioptimalkan.

Jade Plus dapat digunakan dalam beberapa cara: melalui koneksi kabel USB-C, dalam mode "*Air-Gap*" dengan kartu micro SD (memerlukan adaptor), melalui Bluetooth atau bahkan dengan menukarkan kode QR berkat kamera yang terintegrasi. Dompet perangkat keras ini bertenaga baterai.

Dompet ini tersedia mulai dari $149,99 dalam versi hitam dasar, dan harganya bisa naik hingga $20 untuk versi "*Genesis Grey*" atau "*Lunar Silver*". Oleh karena itu, Jade Plus adalah pilihan yang menarik, dengan fungsi canggih yang sebanding dengan dompet perangkat keras kelas atas seperti Coldcard Q atau Passport V2, tetapi dengan harga yang cukup rendah, mendekati model kelas menengah.

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

Dalam tutorial ini, kita akan menyiapkan konfigurasi lanjutan Jade Plus dengan perangkat lunak Sparrow Wallet desktop dalam mode kode QR. Konfigurasi ini sangat ideal untuk pengguna tingkat menengah atau berpengalaman. Jika Anda mencari pendekatan yang lebih sederhana untuk pemula, saya sarankan Anda untuk melihat tutorial ini di mana kita menggunakan Jade Plus dengan Green Wallet melalui koneksi Bluetooth:

https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0
## Model keamanan Jade Plus

Jade Plus menggunakan model keamanan berdasarkan "elemen aman virtual", yang diwujudkan oleh "blind oracle". Secara konkret, mekanisme ini menggabungkan PIN yang dipilih oleh pengguna, sebuah rahasia yang disimpan di Jade dan sebuah rahasia yang dipegang oleh oracle (server yang dikelola oleh Blockstream), untuk membuat kunci AES-256 yang didistribusikan ke dua entitas. Selama inisiasi, pertukaran ECDH mengamankan komunikasi dengan oracle, dan mengenkripsi frasa pemulihan pada dompet perangkat keras. Secara praktis, ketika Anda ingin mengakses seed untuk menandatangani transaksi, Anda membutuhkan akses ke :


- Perangkat Jade Plus itu sendiri;
- Ke PIN untuk membuka kunci perangkat ;
- Dan untuk rahasia peramal.

Keuntungan utama dari pendekatan ini adalah tidak adanya satu titik kegagalan pada tingkat perangkat keras, karena jika penyerang mendapatkan akses ke Jade Anda, mengekstraksi kunci membutuhkan kompromi secara bersamaan dengan Jade dan oracle. Model ini juga berarti bahwa Jade Plus sepenuhnya bersifat open-source, menghindari kendala yang terkait dengan penggunaan elemen keamanan fisik yang sebenarnya, seperti yang digunakan pada Ledger, misalnya.

Kerugian dari sistem ini adalah penggunaan Jade Plus bergantung pada oracle yang dikelola oleh Blockstream. Jika oracle ini tidak dapat diakses, maka tidak mungkin lagi untuk menggunakan dompet perangkat keras secara langsung dengan PIN. Akan tetapi, ini tidak berarti bahwa bitcoin Anda hilang, karena bitcoin tersebut masih dapat dipulihkan dengan menggunakan frasa pemulihan Anda, yang dapat Anda masukkan di Jade Plus dalam mode "*stateless*". Untuk mengatasi ketergantungan ini, Anda juga bisa mengonfigurasi dan mengelola server oracle Anda sendiri.

Pilihan lain untuk mengelola seed Anda adalah dengan tidak mendaftarkannya pada Jade Plus. Dalam hal ini, Jade hanya menjadi perangkat tanda tangan saja. Selama inisialisasi, selain menyimpan frasa pemulihan yang biasa berupa kata-kata, Anda juga akan menyimpannya sebagai kode QR yang dibuat sendiri. Dengan cara ini, setiap kali Anda menggunakan dompet, Anda dapat mengimpor seed menggunakan kamera Jade. Ini bisa menjadi opsi yang menarik untuk pengguna tingkat lanjut, tergantung pada strategi keamanan Anda, tetapi Anda harus berhati-hati dalam menyimpan seed dan melindunginya, karena meskipun dalam bentuk kode QR, ini memungkinkan siapa saja untuk mencuri dana Anda. Kita akan melihat opsi ini dalam tutorial ini, tetapi tidak wajib.

## Membuka kemasan Jade Plus

Ketika Anda menerima Jade Plus, periksa apakah kotak dan segelnya dalam kondisi baik untuk memastikan bahwa paket Anda belum dibuka.

![JADE-PLUS-SPARROW](assets/fr/02.webp)

Di dalam kotak Anda akan menemukan :


- Le Jade Plus;
- Kabel USB-C;
- Kartu untuk merekam frasa mnemonik Anda sebagai kata-kata atau sebagai "*CompactSeedQR*";
- Beberapa petunjuk penggunaan ;
- Sebuah kabel;
- Beberapa stiker.

![JADE-PLUS-SPARROW](assets/fr/03.webp)

Perangkat ini memiliki 4 tombol navigasi:


- Tombol di kanan bawah menyalakan Jade;
- Tombol besar pada bagian depan perangkat digunakan untuk memilih item;
- Dua tombol kecil di bagian atas memungkinkan Anda menavigasi ke kiri dan ke kanan;
- Anda juga dapat memilih item dengan mengklik secara bersamaan pada dua tombol di bagian atas perangkat.

![JADE-PLUS-SPARROW](assets/fr/04.webp)

## Menyiapkan dompet Bitcoin baru

Klik pada tombol mulai.

![JADE-PLUS-SPARROW](assets/fr/05.webp)

Klik "*Setup Jade*".

![JADE-PLUS-SPARROW](assets/fr/06.webp)

Pilih "Pengaturan Lanjutan*".

![Image](assets/fr/07.webp)

Kemudian klik "*Buat Dompet Baru*" untuk membuat seed baru. Anda dapat memilih antara frasa mnemonik 12 atau 24 kata. Keamanan dompet Anda tetap setara dengan kedua opsi tersebut, jadi mungkin akan lebih mudah untuk memilih opsi yang paling sederhana untuk disimpan, yaitu 12 kata.

![Image](assets/fr/08.webp)

Klik tombol "*Lanjutkan*" untuk menampilkan frasa pemulihan baru Anda.

![Image](assets/fr/09.webp)

Jade Plus Anda akan menampilkan frasa mnemonik 12 kata. **Mnemonik ini memberikan Anda akses penuh dan tidak terbatas ke semua bitcoin Anda. Siapa pun yang memiliki frasa ini dapat mencuri dana Anda, bahkan tanpa akses fisik ke Jade Plus Anda. Frasa 12 kata ini akan mengembalikan akses ke bitcoin Anda jika terjadi kehilangan, pencurian, atau kerusakan pada Jade Anda. Oleh karena itu, sangat penting untuk menyimpannya dengan hati-hati dan menyimpannya di lokasi yang aman.

Anda bisa menuliskannya pada karton yang disertakan dalam kotak, atau untuk keamanan tambahan, saya sarankan untuk mengukirnya pada dasar baja tahan karat untuk melindunginya dari kebakaran, banjir atau keruntuhan.

![Image](assets/fr/10.webp)

Untuk informasi lebih lanjut mengenai cara yang tepat untuk menyimpan dan mengelola frasa mnemonik Anda, saya sangat merekomendasikan untuk mengikuti tutorial lainnya, khususnya jika Anda seorang pemula:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
tentu saja, Anda tidak boleh membagikan kata-kata ini di Internet, seperti yang saya lakukan dalam tutorial ini. Portofolio contoh ini hanya akan digunakan di Testnet dan akan dihapus di akhir tutorial.**_

Klik panah di sebelah kanan layar untuk menampilkan kata-kata berikut.

![Image](assets/fr/11.webp)

Setelah Anda menyimpan frasa, Jade Plus akan meminta Anda untuk mengonfirmasinya. Pilih kata yang benar sesuai dengan urutannya menggunakan tombol di bagian atas perangkat, dan klik tombol tengah untuk beralih ke kata berikutnya.

![Image](assets/fr/12.webp)

Anda kemudian memiliki 2 opsi. Seperti yang telah dijelaskan pada bagian pendahuluan, Anda dapat memilih untuk menyimpan seed Anda secara langsung di perangkat dan menggunakan sistem proteksi "*Virtual Secure Element*" dari Blockstream untuk mengakses dompet Anda (Opsi 1), atau menyimpan seed Anda dalam bentuk kode QR dan memindainya setiap kali Anda menggunakannya (Opsi 2).

Untuk Opsi 1, pilih "*Tidak*", dan untuk Opsi 2, pilih "*Ya*".

![Image](assets/fr/13.webp)

### Opsi 1: Buka Kunci PIN QR

Jika Anda telah memilih opsi 1 (CompactSeedQR: "*No*"), Anda akan langsung dibawa ke pilihan metode koneksi. Dalam tutorial ini, kami ingin menggunakan perangkat dalam mode Celah Udara melalui pertukaran kode QR, jadi pilih "*QR*".

![Image](assets/fr/27.webp)

Klik "*Lanjutkan*".

![Image](assets/fr/28.webp)

Kode PIN digunakan untuk membuka kunci Jade Anda dan menawarkan perlindungan terhadap akses fisik yang tidak sah. Kode PIN ini tidak terlibat dalam derivasi kunci kriptografi dompet Anda. Jadi, bahkan tanpa akses ke kode PIN ini, dengan memiliki frasa mnemonik 12 kata, Anda dapat memperoleh kembali akses ke bitcoin Anda. Kami menyarankan Anda untuk memilih kode PIN yang seacak mungkin. Selain itu, pastikan Anda menyimpan kode ini di tempat yang terpisah dari tempat penyimpanan Jade Anda, seperti di pengelola kata sandi.

Pilih kode PIN 6 digit pada Jade Anda, dengan menggunakan tombol kiri dan kanan untuk menggulir angka, dan tombol tengah untuk mengonfirmasi setiap angka.

![Image](assets/fr/29.webp)

Konfirmasikan PIN Anda untuk kedua kalinya.

![Image](assets/fr/30.webp)

Seperti yang telah dijelaskan pada bagian pendahuluan, seed Anda disimpan secara terenkripsi di Jade Plus. Untuk mendekripsinya, Anda harus menyediakan file :


- Kode PIN yang valid (yang baru saja kita siapkan);
- Rahasia oracle yang dikelola oleh Blockstream.

Dalam tutorial lanjutan ini, kita akan menggunakan Sparrow Wallet untuk mengelola dompet Bitcoin kita. Namun, tidak seperti perangkat lunak Green Wallet dari Blockstream, Sparrow tidak memiliki akses ke oracle di server Blockstream. Oleh karena itu, kita akan menggunakan situs web Blockstream untuk mengambil rahasia oracle setiap kali kita membuka kunci Jade Plus.

Kunjungi https://jadefw.blockstream.com/pinqr/index.html

Klik "*Mulai Buka Kunci QR*".

![Image](assets/fr/31.webp)

Klik "*Selesai*", karena Anda telah memilih PIN Anda di Jade Plus.

![Image](assets/fr/32.webp)

Gunakan kamera komputer Anda untuk memindai kode QR yang ditampilkan pada layar Jade Anda.

![Image](assets/fr/33.webp)

Konfirmasikan pada Jade Anda untuk mengakses layar berikutnya.

![Image](assets/fr/34.webp)

Pindai kode QR yang sekarang terlihat di situs web untuk mendapatkan rahasia oracle.

![Image](assets/fr/35.webp)

Sekarang portofolio Anda telah dibuat, Anda dapat melanjutkan ke langkah berikutnya dan melewatkan sub-bagian "*Opsi 2: CompactSeedQR*".

![Image](assets/fr/36.webp)

Setiap kali Anda memulai, klik "*QR Mode*".

![Image](assets/fr/37.webp)

Pilih "*Kunci PIN QR*".

![Image](assets/fr/38.webp)

Masukkan kode PIN Anda.

![Image](assets/fr/39.webp)

Kemudian buka [situs web Blockstream] (https://jadefw.blockstream.com/pinqr/qrpin.html) untuk menukar kode QR dengan oracle.

![Image](assets/fr/40.webp)

Giok Anda sekarang tidak terkunci.

![Image](assets/fr/41.webp)

### Opsi 2: CompactSeedQR

Jika Anda telah memilih opsi 2 (CompactSeedQR: "*Ya*"), klik "*Ya*" sekali lagi.

![Image](assets/fr/14.webp)

Klik "*Mulai*".

![Image](assets/fr/15.webp)

Anda dapat menggunakan basis kode QR yang disediakan dalam kotak Jade Plus. Pilih kotak yang sesuai, tergantung pada apakah Anda memilih kalimat 12 atau 24 kata. Anda juga dapat [mencetak template dari situs web Blockstream] (https://help.blockstream.com/hc/article_attachments/41928319071769).

Jade Plus Anda akan menampilkan setiap zona kode QR Anda.

![Image](assets/fr/16.webp)

Gunakan pena untuk mewarnai kotak-kotak tersebut dan mereproduksi benih Anda sebagai kode QR. Lakukan dengan tepat untuk memastikan bahwa kamera Jade Plus dapat memindainya nanti. Gunakan tanda panah untuk berpindah ke area berikutnya.

![Image](assets/fr/17.webp)

Setelah selesai, klik "*Selesai*".

![Image](assets/fr/18.webp)

Pindai kode QR buatan tangan Anda dengan Jade Plus untuk memeriksa keabsahannya.

![Image](assets/fr/19.webp)

Jika cadangan kertas Anda sudah benar, klik "*Lanjutkan*".

![Image](assets/fr/20.webp)

Dalam tutorial ini, kita akan menggunakan mode koneksi berdasarkan pemindaian kode QR secara eksklusif, jadi pilih "*QR*".

![Image](assets/fr/21.webp)

Anda juga dapat memilih untuk menambahkan PIN sebagai tambahan pada cadangan CompactSeedQR Anda, seperti pada opsi 1. Ini menawarkan dua cara untuk mengakses dompet Anda: baik melalui PIN dan sistem "Elemen Aman Virtual" Blockstream, atau melalui CompactSeedQR.

Jika Anda memilih opsi PIN ganda, pilih "*PIN*" dan ikuti langkah yang sama seperti pada opsi 1 untuk mengatur kode PIN Anda.

Jika Anda lebih suka melanjutkan dengan CompactSeedQR saja, pilih "*SeedQR*".

![Image](assets/fr/22.webp)

Setelah portofolio Anda selesai dibuat, Anda dapat melanjutkan ke langkah berikutnya.

![Image](assets/fr/23.webp)

Setiap kali Anda memulai, klik tombol "*QR Mode*", lalu "*Scan SeedQR*".

![Image](assets/fr/24.webp)

Gunakan kamera perangkat untuk memindai benih yang Anda simpan sebagai kode QR.

![Image](assets/fr/25.webp)

Giok Anda sekarang tidak terkunci.

![Image](assets/fr/26.webp)

## Menambahkan kata sandi BIP39

Kata sandi BIP39 adalah kata sandi opsional yang bisa Anda pilih secara bebas, dan ditambahkan ke frasa mnemonic Anda untuk memperkuat keamanan dompet. Dengan mengaktifkan fitur ini, akses ke dompet Bitcoin Anda akan membutuhkan kata kunci dan frasa sandi. Tanpa keduanya, mustahil untuk memulihkan dompet.

Sebelum mengonfigurasi opsi ini pada Jade Plus Anda, sangat disarankan agar Anda membaca artikel ini untuk memahami sepenuhnya operasi teoritis dari kata sandi dan menghindari kesalahan yang dapat menyebabkan hilangnya bitcoin Anda:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
Dengan Jade Anda masih terkunci (kata sandi hanya dapat dimasukkan ketika perangkat tidak dibuka), akses menu "*Options*".

![Image](assets/fr/42.webp)

Pilih "*Frasa Sandi BIP39*".

![Image](assets/fr/43.webp)

Pada opsi "*Frequency*", Anda dapat memilih apakah Jade Plus akan meminta Anda untuk memasukkan kata sandi setiap kali dijalankan:


- "*Disabled*" menonaktifkan penggunaan kata sandi;
- "*Next Login Only*" akan mengharuskan Anda untuk kembali ke menu ini untuk mengaktifkan permintaan kata sandi Anda pada saat memulai berikutnya. Opsi ini memungkinkan Anda untuk tidak mengungkapkan penggunaannya;
- "*Selalu Tanyakan*" menyebabkan Jade secara sistematis meminta kata sandi Anda setiap kali memulai, sehingga mengungkapkan bahwa dompet Anda dilindungi oleh kata sandi.

Pilih opsi yang sesuai dengan strategi keamanan Anda. Secara pribadi, saya memilih "*Selalu Tanyakan*" sebagai contoh.

![Image](assets/fr/44.webp)

Anda kemudian dapat memilih di antara dua metode untuk memasukkan kata sandi Anda:


- "*Manual*: Papan ketik virtual memungkinkan Anda memasukkan huruf (huruf besar dan kecil), angka, dan simbol, karakter demi karakter. Ini adalah metode standar untuk semua dompet perangkat keras;
- "*Daftar Kata*": Metode khusus yang dirancang oleh Blockstream untuk Jade, yang mempercepat pemasukan kata sandi dan meningkatkan entropinya. Selama input, sistem menyarankan kata-kata dari daftar BIP39, sehingga membuka kunci menjadi lebih mudah. Metode ini secara otomatis menghasilkan kalimat dengan menggabungkan kata-kata yang dipilih, dipisahkan oleh spasi (contoh: `kemampuan meninggalkan mampu`).

Secara pribadi, saya menyarankan Anda untuk menggunakan metode pertama, karena ini adalah standar yang akan Anda temukan pada semua dukungan portofolio lainnya.

![Image](assets/fr/45.webp)

Anda kemudian dapat kembali ke layar beranda dan membuka kunci dompet Anda seperti biasa, baik menggunakan kode PIN atau CompactSeedQR Anda (seperti yang terlihat di atas). Anda akan diminta untuk memasukkan kata sandi Anda.

![Image](assets/fr/46.webp)

Masukkan pada keyboard Jade, dan pastikan untuk membuat satu atau beberapa cadangan pada media fisik (kertas atau logam). Sebagai contoh, saya menggunakan kata sandi yang sangat lemah, tetapi Anda harus memilih kata sandi acak yang kuat yang mencakup semua jenis karakter dan cukup panjang (seperti kata sandi yang kuat).

![Image](assets/fr/47.webp)

Jika kata sandi Anda valid, konfirmasikan.

![Image](assets/fr/48.webp)

Harap diperhatikan bahwa kata sandi BIP39 peka terhadap huruf besar-kecil dan kesalahan pengetikan. Jika Anda memasukkan kata sandi yang sedikit berbeda dari yang dikonfigurasikan pada awalnya, Jade tidak akan melaporkan kesalahan tetapi akan mendapatkan satu set kunci kriptografi lain yang tidak sama dengan kunci kriptografi yang ada di portofolio awal Anda.

Oleh karena itu, penting sekali, ketika mengonfigurasi, untuk mencatat sidik jari kunci utama Anda, yang dapat ditemukan di sudut kanan bawah layar. Contohnya, dengan kata sandi `PBN`, sidik jari tombol utama saya adalah `3AD1AE65`.

![Image](assets/fr/49.webp)

Setiap kali Anda membuka kunci Jade dengan kata sandi, periksa apakah sidik jari sama dengan yang Anda masukkan saat konfigurasi. Jika ya, kata sandi Anda sudah benar dan Anda mengakses dompet Bitcoin yang tepat. Jika tidak, Anda menggunakan dompet yang salah dan perlu mencoba lagi, berhati-hatilah agar tidak membuat kesalahan input.

Sebelum Anda menerima bitcoin pertama Anda di dompet Anda, **Saya sangat menyarankan Anda untuk melakukan tes pemulihan kosong**. Catatlah beberapa informasi referensi, seperti xpub atau alamat penerima pertama Anda, kemudian hapus wallet Anda di Jade Plus ketika masih kosong (`Options -> Device -> Factory Reset`). Kemudian cobalah untuk memulihkan dompet Anda menggunakan cadangan kertas dari frasa mnemonik dan kata sandi apa pun. Periksa apakah informasi cookie yang dihasilkan setelah pemulihan sesuai dengan yang Anda tuliskan sebelumnya. Jika sesuai, Anda bisa yakin bahwa cadangan kertas Anda dapat diandalkan. Untuk mengetahui lebih lanjut tentang cara melakukan pemulihan tes, lihat tutorial lainnya:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895
## Mengonfigurasi dompet di Dompet Sparrow

Dalam tutorial ini, saya menyajikan penggunaan tingkat lanjut Jade Plus menggunakan Sparrow Wallet. Namun, dompet perangkat keras ini kompatibel dengan banyak program lain, seperti Liana, Nunchuk, Spectre, Green, dan Keeper. Kompatibilitas ini bervariasi dalam hal koneksi: USB, Bluetooth atau kode QR (lihat tabel di bagian pendahuluan untuk detailnya).

Mulailah dengan mengunduh dan menginstal Sparrow Wallet [dari situs web resmi] (https://sparrowwallet.com/) di komputer Anda, jika Anda belum melakukannya.

![Image](assets/fr/50.webp)

Pastikan untuk memeriksa keaslian dan integritas perangkat lunak sebelum instalasi. Jika Anda tidak tahu cara melakukannya, silakan baca tutorial ini:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Setelah Sparrow Wallet terbuka, klik tab "*File*", lalu "*Dompet Baru*".

![Image](assets/fr/51.webp)

Beri nama dompet Anda, lalu klik "*Buat Dompet*".

![Image](assets/fr/52.webp)

Pilih "*Dompet Perangkat Keras yang Terisi Penuh*".

![Image](assets/fr/53.webp)

Klik "*Pindai...*" di samping opsi "*Jade*".

![Image](assets/fr/54.webp)

Buka kunci Jade Plus Anda dan, jika Anda menggunakannya, masukkan kata sandi Anda. Kemudian masuk ke menu "*Options*", pilih "*Wallet*", dan klik "*Export Xpub*".

![Image](assets/fr/55.webp)

Jade Anda akan menampilkan Keystore Anda melalui beberapa kode QR. Pindai kode-kode tersebut pada mesin Anda menggunakan Sparrow.

![Image](assets/fr/56.webp)

Sekarang Anda akan melihat xpub dan sidik jari kunci utama Anda, yang seharusnya cocok dengan yang ada di Jade Plus. Klik pada "*Terapkan*".

![Image](assets/fr/57.webp)

Tetapkan kata sandi yang kuat untuk mengamankan akses ke Dompet Sparrow Anda. Kata sandi ini akan melindungi kunci publik, alamat, label, dan riwayat transaksi Anda dari akses yang tidak sah. Sebaiknya simpan kata sandi ini di pengelola kata sandi, agar Anda tidak lupa.

![Image](assets/fr/58.webp)

Portofolio Anda sekarang telah dikonfigurasi dengan benar di Sparrow.

![Image](assets/fr/59.webp)

## Menerima bitcoin

Setelah Jade Plus Anda dikonfigurasi, Anda siap untuk menerima satoshi pertama Anda di dompet Bitcoin baru Anda. Untuk melakukannya, pada Sparrow, klik menu "*Receive*".

![Image](assets/fr/60.webp)

Sparrow akan menampilkan alamat penerimaan kosong pertama dalam portofolio Anda.

![Image](assets/fr/61.webp)

Sebelum menggunakannya, mari kita periksa di layar Jade Plus untuk memastikan bahwa wallet tersebut adalah milik dompet Bitcoin kita. Pada Jade, klik "*Scan QR*", lalu pindai kode QR dari alamat yang ditampilkan di Sparrow.

![Image](assets/fr/62.webp)

Periksa apakah alamat yang ditampilkan di layar Jade Anda sesuai dengan yang ditampilkan di Sparrow Wallet. Jika sesuai, klik tanda centang untuk melanjutkan.

![Image](assets/fr/63.webp)

Dompet perangkat keras Anda kemudian akan mengonfirmasi bahwa alamat ini adalah bagian dari dompet Anda dan menyimpan kunci pribadi yang terkait.

![Image](assets/fr/64.webp)

Jika alamat tersebut divalidasi oleh Jade Anda, maka Anda bisa menggunakannya untuk menerima bitcoin. Ketika transaksi disiarkan di jaringan, transaksi tersebut akan muncul di Sparrow. Tunggu hingga Anda menerima konfirmasi yang cukup untuk menganggap transaksi tersebut sudah pasti.

![Image](assets/fr/65.webp)

## Kirim bitcoin

Sekarang setelah Anda memiliki beberapa sat di dompet Anda, Anda juga dapat mengirim beberapa. Untuk melakukannya, klik menu "*UTXOs*".

![Image](assets/fr/66.webp)

Pilih UTXO yang ingin Anda gunakan sebagai input untuk transaksi ini, lalu klik "*Kirim Terpilih*".

![Image](assets/fr/67.webp)

Masukkan alamat penerima, label untuk mengingatkan Anda tentang tujuan transaksi dan jumlah yang ingin Anda kirim ke alamat ini.

![Image](assets/fr/68.webp)

Sesuaikan tarif biaya sesuai dengan kondisi pasar saat ini, lalu klik "*Buat Transaksi*".

![Image](assets/fr/69.webp)

Pastikan semua parameter transaksi sudah benar, lalu klik "*Finalisasi Transaksi untuk Penandatanganan*".

![Image](assets/fr/70.webp)

Klik "*Show QR*" untuk menampilkan PSBT (*Transaksi Bitcoin yang Ditandatangani Sebagian*). Sparrow telah membuat transaksi, tetapi masih belum memiliki tanda tangan untuk membuka kunci bitcoin yang digunakan dalam input. Tanda tangan ini hanya dapat dilakukan oleh Jade Plus, yang menampung seed Anda dan memberikan akses ke private key yang diperlukan untuk menandatangani transaksi.

![Image](assets/fr/71.webp)

Pada Jade Plus Anda, klik "*Scan QR*" untuk memindai PSBT yang ditampilkan pada Sparrow.

![Image](assets/fr/72.webp)

Konfirmasikan bahwa alamat pengiriman dan jumlah yang dikirim sudah benar, lalu klik tanda panah untuk memvalidasi.

![Image](assets/fr/73.webp)

Pastikan jumlah biaya sesuai dengan yang Anda pilih, lalu klik ikon centang di sudut kiri atas antarmuka untuk menandatangani transaksi.

![Image](assets/fr/74.webp)

Pada Sparrow Wallet, klik "*Scan QR*" dan pindai kode QR yang ditampilkan pada Jade Anda.

![Image](assets/fr/75.webp)

Transaksi yang Anda tandatangani sekarang siap untuk disiarkan di jaringan Bitcoin dan dimasukkan ke dalam blok oleh penambang. Jika semuanya sudah benar, klik "*Siarkan Transaksi*".

![Image](assets/fr/76.webp)

Transaksi Anda telah disiarkan dan menunggu konfirmasi.

![Image](assets/fr/77.webp)

Selamat, sekarang Anda sudah tahu cara mengatur dan menggunakan Jade Plus dalam mode QR. Jika Anda merasa tutorial ini bermanfaat, saya akan berterima kasih jika Anda memberikan jempol hijau di bawah ini. Jangan ragu untuk membagikan artikel ini di jejaring sosial Anda. Terima kasih telah berbagi!

Untuk melangkah lebih jauh, saya merekomendasikan tutorial lain tentang Jade Plus, di mana kita mengonfigurasinya melalui Bluetooth dengan aplikasi seluler Green:

https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0