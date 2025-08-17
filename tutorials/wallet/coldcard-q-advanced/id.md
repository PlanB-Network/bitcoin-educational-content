---
name: KARTU KOLEKSI Q - Advanced
description: Menggunakan opsi lanjutan COLDCARD Q
---
![cover](assets/cover.webp)

Dalam tutorial sebelumnya, kita sudah membahas konfigurasi awal COLDCARD Q dan fungsi-fungsi dasarnya untuk pemula. Jika kamu baru saja menerima COLDCARD Q dan belum mengaturnya, aku sarankan kamu memulai dengan tutorial tersebut sebelum melanjutkan di sini:

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

Tutorial baru ini didedikasikan untuk opsi lanjutan COLDCARD Q, yang dirancang untuk pengguna tingkat lanjut dan paranoid. Faktanya, COLDCARD dibedakan dari hardware wallet lainnya karena memiliki banyak fitur keamanan yang canggih. Tentu saja, kamu tidak harus menggunakan semua opsi ini. Pilih saja yang sesuai dengan strategi keamanan kamu.

**Peringatan**, Penggunaan yang tidak tepat dari beberapa opsi lanjutan ini dapat mengakibatkan hilangnya bitcoin kamu atau rusaknya hardware wallet kamu. Oleh karena itu, aku sangat menyarankan agar kamu membaca saran dan penjelasan untuk setiap opsi dengan seksama.

Sebelum memulai, pastikan kamu memiliki akses ke cadangan fisik seed phrase 12 atau 24 kata, dan periksa validitasnya melalui menu berikut: Tingkat Lanjut/Peralatan > Zona Bahaya > Fungsi Seed > Lihat Seed Words.

![CCQ](assets/fr/01.webp)

## Kata sandi BIP39

Jika kamu tidak tahu apa itu passphrase BIP39, atau jika kamu belum sepenuhnya paham bagaimana cara kerjanya, aku sangat menyarankan kamu melihat tutorial ini terlebih dahulu, yang mencakup dasar-dasar teori yang diperlukan untuk memahami risiko yang terkait dengan penggunaan passphrase:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Ingatlah bahwa setelah kamu membuat passphrase di wallet kamu, mnemonic saja tidak akan cukup untuk mendapatkan kembali akses ke bitcoin kamu. Kamu akan membutuhkan mnemonic dan passphrase. Selain itu, kamu harus memasukkan passphrase setiap kali membuka kunci COLDCARD Q. Hal ini akan meningkatkan keamanan, karena akses fisik ke COLDCARD dan pengetahuan tentang PIN tidak cukup tanpa passphrase.

Di COLDCARD, kamu memiliki dua opsi untuk mengelola passphrase kamu:

1. **Entri klasik:** Kamu memasukkan passphrase secara manual setiap kali menggunakan hardware wallet kamu, seperti yang biasa dilakukan dengan hardware wallet lainnya. COLDCARD Q mempermudah tugas ini dengan keyboard lengkap.

2. **Anda dapat memilih untuk mengenkripsi kata sandi dan menyimpannya pada kartu microSD.** Dalam hal ini, kamu harus memasukkan microSD ke dalam COLDCARD Q setiap kali menggunakannya. Perlu diperhatikan bahwa microSD ini hanya akan bekerja pada COLDCARD Q kamu dan bukan merupakan backup. Oleh karena itu, sangat penting bagi kamu untuk menyimpan salinan passphrase kamu pada media fisik, seperti kertas atau logam.

Untuk mengatur kata sandi BIP39, akses menu "*Kata Sandi*".

![CCQ](assets/fr/02.webp)

Masukkan kata sandimu menggunakan keyboard. Pastikan untuk memilih kata sandi yang kuat (panjang dan acak) dan buat cadangan fisik.

![CCQ](assets/fr/03.webp)

Setelah Anda menetapkan kata sandi, COLDCARD Q akan menampilkan sidik jari kunci utama dompet baru yang terkait dengan kata sandi ini. Pastikan untuk menyimpan sidik jari ini. Ketika kamu memasukkan kembali kata sandi saat menggunakan perangkat di masa mendatang, kamu dapat memeriksa apakah sidik jari yang ditampilkan sesuai dengan yang disimpan. Pemeriksaan ini memastikan bahwa kamu tidak membuat kesalahan saat memasukkan kata sandi.

![CCQ](assets/fr/04.webp)

Sekarang kamu dapat menekan "*ENTER*" untuk menerapkan kata sandi ini ke frasa mnemonik kamu dan mengaktifkan dompet yang baru. Jika kamu lebih suka menyimpan kata sandi ini di microSD, masukkan kartu ke dalam slot yang sesuai dan tekan "*1*".

![CCQ](assets/fr/05.webp)

Kata sandi sekarang telah diterapkan. Jejak kunci muncul di layar beranda dan di bagian atas layar.

![CCQ](assets/fr/06.webp)

Setiap kali kamu membuka kunci COLDCARD Q, kamu harus mengakses menu "*Passphrase*" dan memasukkan kata sandi dengan cara yang sama seperti di atas, untuk menerapkannya pada mnemonik yang tersimpan di perangkat dan mengakses dompet Bitcoin yang benar.

![CCQ](assets/fr/07.webp)

Jika kamu telah menyimpan kata sandi pada kartu microSD, setiap kali kamu menggunakannya, masukkan ke dalam COLDCARD dan akses menu "*Kata Sandi*". COLDCARD kamu akan memuat kata sandi secara langsung dari microSD, jadi kamu tidak perlu memasukkannya secara manual. Klik pada "*Kembalikan Tersimpan*".

![CCQ](assets/fr/08.webp)

Periksa apakah panjang dan huruf pertama dari kata sandi yang dimuat sudah benar.

![CCQ](assets/fr/09.webp)

Konfirmasikan bahwa sidik jari yang ditampilkan sesuai dengan sidik jari yang ada di dompet kamu dan klik "*Restore*".

![CCQ](assets/fr/10.webp)

Perlu diingat bahwa menggunakan kata sandi berarti kamu harus mengimpor satu set kunci baru yang berasal dari kombinasi frasa mnemonik dan kata sandi kamu ke dalam perangkat lunak manajemen dompetmu (seperti Sparrow Wallet). Untuk melakukannya, ikuti langkah "*Konfigurasi dompet baru di Sparrow*" di tutorial lainnya:

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

## Opsi membuka kunci

COLDCARD juga punya keuntungan dari beberapa opsi untuk proses membuka kunci perangkat. Mari kita lihat lebih lanjut opsi-opsi lanjutan ini.

### Trik PIN

Trick PIN adalah kode PIN sekunder yang berbeda dari PIN yang ditetapkan saat konfigurasi awal perangkat. Kode ini digunakan untuk memicu tindakan tertentu yang sudah dikonfigurasi sebelumnya begitu dimasukkan saat COLDCARD dinyalakan. Kamu bisa mengonfigurasi beberapa Trick PIN, masing-masing terkait dengan tindakan yang berbeda. Fitur ini memungkinkan kamu menyesuaikan COLDCARD dengan strategi keamanan pribadi kamu. Fitur ini sangat berguna dalam situasi pemaksaan fisik, seperti saat perampokan (biasanya disebut dalam komunitas Bitcoin sebagai "serangan kunci Inggris").

Untuk mengaktifkan Trick PIN dan mengaitkannya dengan suatu tindakan, akses menu `Pengaturan > Pengaturan Login > Trick PIN`.

![CCQ](assets/fr/11.webp)

Pilih "*Tambahkan Trik Baru*".

![CCQ](assets/fr/12.webp)

Tetapkan kode PIN yang akan dikaitkan dengan tindakan dan ingatlah untuk menyimpannya.

![CCQ](assets/fr/13.webp)

Kemudian pilih tindakan yang akan dilakukan secara otomatis setiap kali kamu memasukkan PIN Trik ini. Berikut adalah daftar tindakan yang tersedia untuk PIN:


- "*Brick Self*: Tindakan ini akan menghancurkan kedua chip COLDCARD Q jika Trick PIN dimasukkan, sehingga perangkat sama sekali tidak dapat digunakan. Maka tidak mungkin untuk dijual kembali, digunakan kembali atau bahkan dikembalikan ke Coinkite. Perangkat akan menjadi tidak dapat digunakan lagi. Fitur ini dapat digunakan jika terjadi perampokan untuk meyakinkan penyerang bahwa ia tidak akan pernah bisa mengakses bitcoin milikmu. **Harap diperhatikan**: tanpa cadangan fisik dari frasa mnemonik dan kata sandi, bitcoin-mu akan hilang secara permanen.

![CCQ](assets/fr/14.webp)


- "*Hapus Seed*": Menu ini menawarkan beberapa tindakan untuk menghapus seed, yaitu mengatur ulang COLDCARD tanpa menghancurkannya. Tidak seperti opsi "*Brick Self*", opsi ini memungkinkan untuk mengkonfigurasi ulang perangkat dengan menggunakan cadangan frasa mnemonik. Akan tetapi, tanpa cadangan ini, bitcoin-mu akan hilang. Berikut adalah opsi yang tersedia:
 - "*Hapus & Boot Ulang*: Menghapus seed dan me-reboot COLDCARD tanpa menampilkan informasi apa pun di layar.
 - "*Silent Wipe*": Menghapus seed secara diam-diam, dan membuka kunci COLDCARD pada dompet palsu secara acak seolah-olah tidak terjadi apa-apa.
 - "*Seka -> Dompet*": Menghapus seed secara diam-diam dan membuka COLDCARD pada dompet sekunder yang sudah diatur sebelumnya, yang dirancang sebagai umpan. Dompet ini mungkin berisi sebagian kecil dari tabungan bitcoin Anda untuk memuaskan penyerang.
 - "*Katakanlah Dihapus, Berhenti*": Menghapus seed dan menampilkan pesan `Seed terhapus, Berhenti` di layar.

![CCQ](assets/fr/15.webp)


- "*Dompet Paksa*": Dengan tindakan ini, kode Trick PIN akan membuka wallet yang berasal dari seed menggunakan BIP85. Wallet sekunder ini bisa digunakan sebagai umpan untuk menenangkan penyerang. COLDCARD bertindak seolah-olah itu adalah wallet yang sebenarnya, tetapi tanpa PIN utama (beda dengan Trick PIN), penyerang tidak akan pernah bisa mengakses wallet yang asli. Strategi ini dirancang untuk membuat orang percaya bahwa wallet yang terhubung dengan Trick PIN adalah satu-satunya yang ada.
- 
![CCQ](assets/fr/16.webp)


- "* Hitung Mundur Masuk*": Menu ini mengelompokkan tindakan dengan hitungan mundur sebelum dijalankan. **Peringatan**, beberapa di antaranya dapat merusak perangkat atau mengakibatkan hilangnya bitcoin. Berikut adalah sub-tindakan yang tersedia:
 - "*Hapus & Hitung Mundur*: Menghapus seed dari memori COLDCARD, lalu memulai hitungan mundur satu jam. Tanpa menyimpan mnemonik atau kata sandi Anda, bitcoin akan hilang. Opsi ini didesain untuk mengelabui penyerang agar berpikir bahwa perangkat akan terbuka di akhir hitungan mundur, padahal sebenarnya perangkat akan disetel ulang ke pengaturan pabrik.
 - "* Hitung Mundur & Batu Bata*": Memulai hitungan mundur satu jam, di mana pada akhirnya COLDCARD akan menghancurkan dua chip amannya, membuatnya tidak dapat digunakan secara permanen. Tanpa cadangan, bitcoin-mu akan hilang. Tindakan ini dirancang untuk mengelabui penyerang, yang mengira bahwa ia sedang menunggu untuk membuka kunci, padahal sebenarnya perangkat akan hancur dengan sendirinya.
 - "*Hanya Hitung Mundur* : Memicu hitungan mundur satu jam sederhana, setelah itu COLDCARD akan dimulai ulang tanpa tindakan lebih lanjut. Seed tidak dihapus dan perangkat tetap utuh. Berhati-hatilah untuk tidak mengacaukan tindakan ini dengan opsi "*Login Countdown*", yang akan dibahas pada bagian berikut, yang menambahkan hitungan mundur ke PIN utama sambil memberikan akses ke dompet yang sebenarnya.

![CCQ](assets/fr/17.webp)


- "*Tampak Kosong*": Tindakan ini membuat COLDCARD terlihat kosong, memberikan kesan bahwa seed telah dihapus. Pada kenyataannya, tidak ada yang terjadi dan seed tetap utuh. Ini mensimulasikan COLDCARD yang tidak terpakai atau direset.

![CCQ](assets/fr/18.webp)


- "*Hanya Reboot*: Ketika PIN Trik digunakan, COLDCARD hanya melakukan boot ulang. Tidak ada tindakan lain yang dilakukan.

![CCQ](assets/fr/19.webp)


- "*Mode Delta*": Tindakan yang kompleks ini, ditujukan untuk pengguna berpengalaman, dirancang untuk menghadapi serangan pemaksaan yang sangat canggih, baik dari pihak negara maupun kerabat yang memiliki informasi rahasia. Ketika Delta Mode diaktifkan, COLDCARD memberikan akses ke wallet yang asli, memungkinkan penyerang menavigasi dan memverifikasi bahwa itu adalah wallet yang benar. Namun, tanda tangan transaksi diblokir, sehingga mencegah transfer bitcoin. Selain itu, akses ke mnemonic dinonaktifkan dan setiap upaya untuk mengambilnya akan mengakibatkan penghapusan. Untuk meningkatkan kredibilitas, Trick PIN yang digunakan dengan Delta Mode harus memiliki awalan yang sama dengan PIN asli (untuk menampilkan kata-kata anti-phishing yang sama), tetapi akhiran harus berbeda.

![CCQ](assets/fr/20.webp)

Setelah kamu memilih tindakan, konfirmasikan pilihanmu.

![CCQ](assets/fr/21.webp)

kemudian kamu melihat semua PIN Trik yang dikonfigurasi di menu khusus.

![CCQ](assets/fr/22.webp)

Dengan memilih Trick PIN yang ada, kamu bisa memeriksa tindakan terkait. Kamu juga dapat menyembunyikannya dengan "*Sembunyikan Trick*", sehingga tidak terlihat di menu Trick PIN. Kamu dapat menghapusnya dengan mengklik "*Hapus Trick*", atau mengubah kode PIN sambil mempertahankan tindakan terkait dengan "*Ubah PIN*".

![CCQ](assets/fr/23.webp)

Opsi "*Tambahkan Jika Salah*", tersedia di menu "*Tipu PIN*", memungkinkan kamu mengonfigurasi tindakan tertentu yang secara otomatis dipicu setelah sejumlah percobaan yang salah untuk memasukkan kode PIN utama. Jumlah percobaan yang diizinkan dapat diatur selama konfigurasi.

### Tombol Acak

Opsi Tombol Acak memungkinkan kamu untuk mengacak angka yang ditampilkan pada tombol keypad saat memasukkan kode PIN. Fitur ini melindungi kerahasiaan kode PIN-mu, bahkan jika terjadi pengawasan oleh orang atau kamera.

Untuk mengaktifkan opsi ini, akses menu `Pengaturan > Pengaturan Login > Tombol Acak`.

![CCQ](assets/fr/24.webp)

Pilih opsi "*Scramble Keys*".

![CCQ](assets/fr/25.webp)

Mulai sekarang, ketika kamu membuka kunci COLDCARD Q, tombol pada keypad akan diberi nomor baru secara acak setiap kali digunakan.

![CCQ](assets/fr/26.webp)

### Hitung Mundur Masuk

Opsi ini memungkinkan kamu menerapkan hitungan mundur sistematis setiap kali mencoba membuka kunci COLDCARD. Opsi ini bisa diintegrasikan ke dalam strategi keamanan kamu dengan menunda akses ke perangkat jika terjadi pencurian, atau dengan memberlakukan penundaan sebelum menandatangani transaksi, misalnya untuk melindungi diri jika terjadi perampokan. Namun, hitungan mundur ini berlaku untuk semua penggunaan kamu, termasuk saat menggunakan COLDCARD secara sah, yang berarti kamu juga harus bersabar. Berhati-hatilah untuk tidak mengacaukan pilihan ini dengan tindakan "*Just Countdown*", yang hanya aktif ketika Trick PIN tertentu digunakan.

Untuk mengonfigurasi opsi ini, akses menu `Pengaturan > Pengaturan Login > Hitung Mundur Login`.

![CCQ](assets/fr/27.webp)

Pilih waktu hitung mundur. Misalnya, jika kamu memilih 1 jam, kamu harus menunggu 1 jam untuk setiap upaya membuka kunci COLDCARD Q.

![CCQ](assets/fr/28.webp)

Setiap kali kamu membuka kunci, kamu akan diminta untuk memasukkan kode PIN.

![CCQ](assets/fr/29.webp)

Kemudian, tunggu waktu yang ditetapkan oleh hitungan mundur.

![CCQ](assets/fr/30.webp)

Di akhir hitungan mundur, kamu harus memasukkan PIN lagi untuk mengakses perangkat.

![CCQ](assets/fr/31.webp)

### Masuk Kalkulator

Opsi ini memungkinkan kamu untuk menyamarkan COLDCARD kamu sebagai kalkulator saat membuka kunci. Untuk mengaktifkan fitur ini, akses menu `Pengaturan > Pengaturan Masuk > Masuk Kalkulator`.

![CCQ](assets/fr/32.webp)

Aktifkan opsi dengan memilihnya.

![CCQ](assets/fr/33.webp)

Mulai sekarang, setiap kali perangkat dihidupkan, kalkulator yang berfungsi dengan perintah dasar akan ditampilkan.

![CCQ](assets/fr/34.webp)

Sebagai contoh, kamu dapat menghitung hash SHA256 dari "*Rencana B Network*".

![CCQ](assets/fr/35.webp)

Untuk membuka kunci COLDCARD dari mode kalkulator, mulailah dengan memasukkan awalan kode PIN kamu diikuti dengan tanda hubung. Sebagai contoh, jika kode PIN kamu adalah `00-00` (kode ini lemah dan hanya contoh, jadi pilihlah kode PIN yang kuat), ketik `00-`. COLDCARD kemudian akan menampilkan dua kata anti-phishing Anda.

![CCQ](assets/fr/36.webp)

Kemudian masukkan kode PIN lengkap kamu, dipisahkan dengan spasi atau tanda hubung, misalnya: `00 00`.

![CCQ](assets/fr/37.webp)

COLDCARD kemudian akan keluar dari mode kalkulator dan membuka kunci secara normal.

## Menghancurkan COLDCARD Anda dengan bersih

Jika kamu berencana membuang COLDCARD Q kamu, misalnya karena sekarang menggunakan hardware wallet lain, penting untuk menghancurkan perangkat dengan benar. Hal ini bertujuan memastikan tidak ada informasi terkait wallet kamu yang bisa dipulihkan oleh pihak ketiga.

Terdapat tiga tingkat penghancuran informasi, tergantung kebutuhan kamu. Sebelum memulai, pastikan wallet kamu sudah diimpor ke hardware wallet lain, kamu memiliki akses ke semua dana kamu, dan yang terpenting, kamu memiliki seed phrase dan passphrase apa pun, yang keduanya berfungsi. Tanpa backup wallet, penghancuran COLDCARD kamu akan mengakibatkan hilangnya bitcoin.

Tingkat penghancuran pertama terdiri dari hanya menghapus seed. Opsi ini menghapus frasa mnemonik dari memori COLDCARD, namun tetap membiarkan perangkat tetap berfungsi. Ini sangat ideal jika kamu ingin menggunakan COLDCARD Q lagi di kemudian hari. Untuk menghapus seed dari memori, akses menu `Tingkat Lanjut/Peralatan > Zona Bahaya > Fungsi Seed > Hancurkan Seed`.

![CCQ](assets/fr/38.webp)

Tingkat penghancuran kedua terdiri dari penonaktifan permanen dua secure element COLDCARD melalui software. Tindakan ini membuat perangkat tidak bisa digunakan sama sekali. Kamu tidak akan bisa menjualnya lagi, menggunakannya kembali, atau mengembalikannya ke Coinkite: perangkat ini akan dihancurkan secara permanen. Untuk melanjutkan, ikuti langkah-langkah yang dijelaskan di bagian sebelumnya mengenai "*Brick Me*" Kemudian masukkan PIN ini dengan sengaja saat membuka kunci COLDCARD.

Tingkat ketiga melibatkan penghancuran fisik komponen aman COLDCARD Q milikmu. Seperti sebelumnya, hal ini akan membuat perangkat tidak dapat digunakan lagi. Untuk melakukannya, gunakan bor untuk membuat lubang pada dua chip di sisi kanan atas perangkat (setelah dibalik), dekat dengan tulisan "*SHOOT HERE*".

**Tindakan pencegahan penting**:


- Untuk menghindari risiko sengatan listrik, keluarkan baterai dari perangkat dan cabut dari stopkontak sebelum menangani.
- Tunggu beberapa menit setelah mematikan unit sebelum memulai pengeboran.
- Kenakan sarung tangan berinsulasi dan kacamata pengaman untuk memastikan keselamatan Anda.

![CCQ](assets/fr/39.webp)

Setelah chip dilubangi, jangan coba-coba menyambungkan kembali COLDCARD Q.

Selamat, kamu sekarang sudah menguasai opsi lanjutan COLDCARD Q!

Jika kamu merasa tutorial ini bermanfaat, aku akan sangat berterima kasih jika kamu memberikan tanda jempol hijau di bawah ini. Jangan ragu untuk membagikan tutorial ini di media sosial. Terima kasih banyak!

Aku juga merekomendasikan tutorial lain ini, di mana kita membahas penggunaan pesaing langsung untuk CCQ, Ledger Flex :

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a
