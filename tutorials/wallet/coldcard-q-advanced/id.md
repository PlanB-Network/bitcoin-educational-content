---
name: KARTU KOLEKSI Q - Lanjutan
description: Menggunakan opsi lanjutan COLDCARD Q
---
![cover](assets/cover.webp)

Dalam tutorial sebelumnya, kita sudah membahas konfigurasi awal COLDCARD Q dan fungsi-fungsi dasarnya untuk pemula. Jika Anda baru saja menerima COLDCARD Q dan belum mengaturnya, saya sarankan Anda memulai dengan tutorial tersebut sebelum melanjutkan di sini:

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3
Tutorial baru ini didedikasikan untuk opsi lanjutan COLDCARD Q, yang dirancang untuk pengguna tingkat lanjut dan paranoid. Faktanya, COLDCARD dibedakan dari dompet perangkat keras lainnya karena memiliki banyak fitur keamanan yang canggih. Tentu saja, Anda tidak harus menggunakan semua opsi ini. Pilih saja yang sesuai dengan strategi keamanan Anda.

**Peringatan**, penggunaan yang tidak tepat dari beberapa opsi lanjutan ini dapat mengakibatkan hilangnya bitcoin Anda atau rusaknya dompet perangkat keras Anda. Oleh karena itu, saya sangat menyarankan agar Anda membaca saran dan penjelasan untuk setiap opsi dengan seksama.

Sebelum memulai, pastikan Anda memiliki akses ke cadangan fisik frasa mnemonik 12 atau 24 kata, dan periksa validitasnya melalui menu berikut: `Tingkat Lanjut/Peralatan > Zona Bahaya > Fungsi Benih > Lihat Kata Benih`.

![CCQ](assets/fr/01.webp)

## Kata sandi BIP39

Jika Anda tidak tahu apa itu kata sandi BIP39, atau jika Anda tidak sepenuhnya paham bagaimana cara kerjanya, saya sangat menyarankan agar Anda melihat tutorial ini terlebih dahulu, yang mencakup dasar-dasar teori yang diperlukan untuk memahami risiko yang terkait dengan penggunaan kata sandi:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
Ingatlah bahwa setelah Anda membuat kata sandi di dompet Anda, mnemonic Anda saja tidak akan cukup untuk mendapatkan kembali akses ke bitcoin Anda. Anda akan membutuhkan mnemonic dan kata sandi. Selain itu, Anda harus memasukkan kata sandi setiap kali membuka kunci COLDCARD Q. Hal ini akan meningkatkan keamanan dengan membuat akses fisik ke COLDCARD dan pengetahuan tentang PIN tidak cukup tanpa kata sandi.

Pada COLDCARD, Anda memiliki dua opsi untuk mengelola kata sandi Anda:

1. **Entri klasik:** Anda memasukkan kata sandi secara manual setiap kali Anda menggunakan dompet perangkat keras Anda, seperti yang Anda lakukan dengan dompet perangkat keras lainnya. COLDCARD Q menyederhanakan tugas ini dengan keyboard yang lengkap.

2. **Anda dapat memilih untuk mengenkripsi kata sandi dan menyimpannya pada kartu microSD. Dalam hal ini, Anda harus memasukkan microSD ke dalam COLDCARD Q setiap kali menggunakannya. Harap diperhatikan bahwa microSD ini hanya akan bekerja pada COLDCARD Q Anda dan bukan merupakan cadangan. Oleh karena itu, sangat penting bagi Anda untuk menyimpan salinan kata sandi Anda pada media fisik, seperti kertas atau logam.

Untuk mengatur kata sandi BIP39 Anda, akses menu "*Kata Sandi*".

![CCQ](assets/fr/02.webp)

Masukkan kata sandi Anda menggunakan keyboard. Pastikan untuk memilih kata sandi yang kuat (panjang dan acak) dan buat cadangan fisik.

![CCQ](assets/fr/03.webp)

Setelah Anda menetapkan kata sandi, COLDCARD Q akan menampilkan sidik jari kunci utama dompet baru yang terkait dengan kata sandi ini. Pastikan untuk menyimpan sidik jari ini. Ketika Anda memasukkan kembali kata sandi saat menggunakan perangkat Anda di masa mendatang, Anda akan dapat memeriksa apakah sidik jari yang ditampilkan sesuai dengan yang Anda simpan. Pemeriksaan ini memastikan bahwa Anda tidak membuat kesalahan saat memasukkan kata sandi.

![CCQ](assets/fr/04.webp)

Sekarang Anda dapat menekan "*ENTER*" untuk menerapkan kata sandi ini ke frasa mnemonik Anda dan mengaktifkan dompet yang baru. Jika Anda lebih suka menyimpan kata sandi ini di microSD, masukkan kartu ke dalam slot yang sesuai dan tekan "*1*".

![CCQ](assets/fr/05.webp)

Kata sandi Anda sekarang telah diterapkan. Jejak kunci muncul di layar beranda dan di bagian atas layar.

![CCQ](assets/fr/06.webp)

Setiap kali Anda membuka kunci COLDCARD Q, Anda harus mengakses menu "*Passphrase*" dan memasukkan kata sandi dengan cara yang sama seperti di atas, untuk menerapkannya pada mnemonik yang tersimpan di perangkat dan mengakses dompet Bitcoin yang benar.

![CCQ](assets/fr/07.webp)

Jika Anda telah menyimpan kata sandi pada kartu microSD, setiap kali Anda menggunakannya, masukkan ke dalam COLDCARD dan akses menu "*Kata Sandi*". COLDCARD Anda akan memuat kata sandi secara langsung dari microSD, jadi Anda tidak perlu memasukkannya secara manual. Klik pada "*Kembalikan Tersimpan*".

![CCQ](assets/fr/08.webp)

Periksa apakah panjang dan huruf pertama dari kata sandi yang dimuat sudah benar.

![CCQ](assets/fr/09.webp)

Konfirmasikan bahwa sidik jari yang ditampilkan sesuai dengan sidik jari yang ada di dompet Anda dan klik "*Restore*".

![CCQ](assets/fr/10.webp)

Perlu diingat bahwa menggunakan kata sandi berarti anda harus mengimpor satu set kunci baru yang berasal dari kombinasi frasa mnemonik dan kata sandi anda ke dalam perangkat lunak manajemen dompet anda (seperti Sparrow Wallet). Untuk melakukannya, ikuti langkah "*Konfigurasi dompet baru di Sparrow*" di tutorial lainnya:

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3
## Opsi membuka kunci

COLDCARD juga mendapatkan keuntungan dari sejumlah opsi untuk proses membuka kunci perangkat. Mari cari tahu lebih lanjut tentang opsi-opsi tingkat lanjut ini.

### Trik PIN

Trick PIN adalah kode PIN sekunder yang berbeda dari kode PIN yang ditetapkan saat konfigurasi perangkat awal. Kode ini digunakan untuk memicu tindakan tertentu yang telah dikonfigurasi sebelumnya segera setelah dimasukkan saat COLDCARD dihidupkan. Anda dapat mengonfigurasi beberapa Trick PIN, masing-masing terkait dengan tindakan yang berbeda. Fitur-fitur ini memungkinkan Anda untuk menyesuaikan COLDCARD dengan strategi keamanan pribadi Anda. Fitur ini sangat berguna dalam kasus-kasus pemaksaan fisik, seperti pada saat perampokan (biasanya disebut dalam komunitas Bitcoin sebagai "serangan kunci inggris").

Untuk mengaktifkan Trick PIN dan mengaitkannya dengan suatu tindakan, akses menu `Pengaturan > Pengaturan Login > Trick PIN`.

![CCQ](assets/fr/11.webp)

Pilih "*Tambahkan Trik Baru*".

![CCQ](assets/fr/12.webp)

Tetapkan kode PIN yang akan dikaitkan dengan tindakan dan ingatlah untuk menyimpannya.

![CCQ](assets/fr/13.webp)

Kemudian pilih tindakan yang akan dilakukan secara otomatis setiap kali Anda memasukkan PIN Trik ini. Berikut adalah daftar tindakan yang tersedia untuk PIN:


- "*Brick Self*: Tindakan ini akan menghancurkan kedua chip COLDCARD Q jika Trick PIN dimasukkan, sehingga perangkat sama sekali tidak dapat digunakan. Maka tidak mungkin untuk dijual kembali, digunakan kembali atau bahkan dikembalikan ke Coinkite. Perangkat akan menjadi tidak dapat digunakan lagi. Fitur ini dapat digunakan jika terjadi perampokan untuk meyakinkan penyerang bahwa ia tidak akan pernah bisa mengakses bitcoin Anda. **Harap diperhatikan**: tanpa cadangan fisik dari frasa mnemonik dan kata sandi Anda, bitcoin Anda akan hilang secara permanen.

![CCQ](assets/fr/14.webp)


- "*Hapus Benih*": Menu ini menawarkan beberapa tindakan untuk menghapus seed, yaitu mengatur ulang COLDCARD tanpa menghancurkannya. Tidak seperti opsi "*Brick Self*", opsi ini memungkinkan untuk mengkonfigurasi ulang perangkat dengan menggunakan cadangan frasa mnemonik Anda. Akan tetapi, tanpa cadangan ini, bitcoin Anda akan hilang. Berikut adalah opsi yang tersedia:
 - "*Hapus & Boot Ulang*: Menghapus seed dan me-reboot COLDCARD tanpa menampilkan informasi apa pun di layar.
 - "*Silent Wipe*": Menghapus seed secara diam-diam, dan membuka kunci COLDCARD pada dompet palsu secara acak seolah-olah tidak terjadi apa-apa.
 - "*Seka -> Dompet*": Menghapus seed secara diam-diam dan membuka COLDCARD pada dompet sekunder yang sudah dikonfigurasikan sebelumnya, yang dirancang sebagai umpan. Dompet ini mungkin berisi sebagian kecil dari tabungan bitcoin Anda untuk memuaskan penyerang.
 - "*Katakanlah Dihapus, Berhenti*": Menghapus benih dan menampilkan pesan `Benih terhapus, Berhenti` di layar.

![CCQ](assets/fr/15.webp)


- "*Dompet Paksa*": Dengan tindakan ini, kode Trick PIN akan membuka dompet yang berasal dari seed menggunakan BIP85. Dompet sekunder ini dapat digunakan sebagai umpan untuk memuaskan penyerang. COLDCARD bertindak seolah-olah sebagai dompet yang sebenarnya, tetapi tanpa PIN utama (berbeda dengan Trick PIN), penyerang tidak akan pernah dapat mengakses dompet yang sebenarnya. Strategi ini didesain untuk membuat orang percaya bahwa dompet yang terhubung dengan Trick PIN adalah satu-satunya yang ada.

![CCQ](assets/fr/16.webp)


- "* Hitung Mundur Masuk*": Menu ini mengelompokkan tindakan dengan hitungan mundur sebelum dijalankan. **Peringatan**, beberapa di antaranya dapat merusak perangkat Anda atau mengakibatkan hilangnya bitcoin Anda. Berikut adalah sub-tindakan yang tersedia:
 - "*Hapus & Hitung Mundur*: Menghapus seed dari memori COLDCARD, lalu memulai hitungan mundur satu jam. Tanpa menyimpan mnemonik atau kata sandi Anda, bitcoin Anda akan hilang. Opsi ini didesain untuk mengelabui penyerang agar berpikir bahwa perangkat akan terbuka di akhir hitungan mundur, padahal sebenarnya perangkat akan disetel ulang ke pengaturan pabrik.
 - "* Hitung Mundur & Batu Bata*": Memulai hitungan mundur satu jam, di mana pada akhirnya COLDCARD akan menghancurkan dua chip amannya, membuatnya tidak dapat digunakan secara permanen. Tanpa cadangan, bitcoin Anda akan hilang. Tindakan ini dirancang untuk mengelabui penyerang, yang mengira bahwa ia sedang menunggu untuk membuka kunci, padahal sebenarnya perangkat akan hancur dengan sendirinya.
 - "*Hanya Hitung Mundur* : Memicu hitungan mundur satu jam sederhana, setelah itu COLDCARD akan dimulai ulang tanpa tindakan lebih lanjut. Benih tidak dihapus dan perangkat tetap utuh. Berhati-hatilah untuk tidak mengacaukan tindakan ini dengan opsi "*Login Countdown*", yang akan dibahas pada bagian berikut, yang menambahkan hitungan mundur ke PIN utama sambil memberikan akses ke dompet yang sebenarnya.

![CCQ](assets/fr/17.webp)


- "*Tampak Kosong*": Tindakan ini membuat COLDCARD terlihat kosong, memberikan kesan bahwa seed telah dihapus. Pada kenyataannya, tidak ada yang terjadi dan seed tetap utuh. Ini mensimulasikan COLDCARD yang tidak terpakai atau direset.

![CCQ](assets/fr/18.webp)


- "*Hanya Reboot*: Ketika PIN Trik digunakan, COLDCARD hanya melakukan boot ulang. Tidak ada tindakan lain yang dilakukan.

![CCQ](assets/fr/19.webp)


- "*Mode Delta*": Tindakan yang rumit ini, diperuntukkan bagi pengguna yang berpengalaman, dirancang untuk melawan serangan pemaksaan yang sangat canggih, baik dari negara atau kerabat yang memiliki informasi rahasia. Ketika Delta Mode diaktifkan, COLDCARD menyediakan akses ke dompet yang sebenarnya, memungkinkan penyerang untuk menavigasi dan memverifikasi bahwa itu adalah dompet yang benar. Akan tetapi, tanda tangan transaksi diblokir, sehingga mencegah transfer bitcoin. Sebagai tambahan, akses ke frase mnemonic dinonaktifkan dan setiap usaha untuk mengambilnya akan mengakibatkan penghapusan. Untuk meningkatkan kredibilitas, Trick PIN yang digunakan dengan Delta Mode harus memiliki awalan yang sama dengan PIN asli (untuk menampilkan kata-kata anti-phishing yang sama), tetapi akhiran harus berbeda.

![CCQ](assets/fr/20.webp)

Setelah Anda memilih tindakan, konfirmasikan pilihan Anda.

![CCQ](assets/fr/21.webp)

Anda kemudian dapat melihat semua PIN Trik yang dikonfigurasi di menu khusus.

![CCQ](assets/fr/22.webp)

Dengan memilih Trick PIN yang ada, Anda dapat memeriksa tindakan terkait. Anda juga dapat menyembunyikannya dengan "*Sembunyikan Trick*", sehingga tidak terlihat di menu Trick PIN. Anda dapat menghapusnya dengan mengklik "*Hapus Trick*", atau mengubah kode PIN sambil mempertahankan tindakan terkait dengan "*Ubah PIN*".

![CCQ](assets/fr/23.webp)

Opsi "*Tambahkan Jika Salah*", tersedia di menu "*Tipu PIN*", memungkinkan Anda mengonfigurasi tindakan tertentu yang secara otomatis dipicu setelah sejumlah percobaan yang salah untuk memasukkan kode PIN utama. Jumlah percobaan yang diizinkan dapat diatur selama konfigurasi.

### Tombol Acak

Opsi Tombol Acak memungkinkan Anda untuk mengacak angka yang ditampilkan pada tombol keypad saat memasukkan kode PIN. Fitur ini melindungi kerahasiaan kode PIN Anda, bahkan jika terjadi pengawasan oleh orang atau kamera.

Untuk mengaktifkan opsi ini, akses menu `Pengaturan > Pengaturan Login > Tombol Acak`.

![CCQ](assets/fr/24.webp)

Pilih opsi "*Scramble Keys*".

![CCQ](assets/fr/25.webp)

Mulai sekarang, ketika Anda membuka kunci COLDCARD Q, tombol pada keypad akan diberi nomor baru secara acak setiap kali Anda menggunakannya.

![CCQ](assets/fr/26.webp)

### Hitung Mundur Masuk

Opsi ini memungkinkan Anda untuk menerapkan hitungan mundur sistematis setiap kali Anda mencoba membuka kunci COLDCARD. Opsi ini dapat diintegrasikan ke dalam strategi keamanan Anda dengan menunda akses ke perangkat jika terjadi pencurian, atau dengan memberlakukan penundaan sebelum menandatangani transaksi, misalnya untuk melindungi diri Anda sendiri jika terjadi perampokan. Namun, hitungan mundur ini berlaku untuk semua penggunaan Anda, termasuk saat Anda menggunakan COLDCARD secara sah, yang juga mengharuskan Anda untuk bersabar. Berhati-hatilah untuk tidak mengacaukan pilihan ini dengan tindakan "*Just Countdown*", yang hanya diaktifkan ketika Trick PIN tertentu digunakan.

Untuk mengonfigurasi opsi ini, akses menu `Pengaturan > Pengaturan Login > Hitung Mundur Login`.

![CCQ](assets/fr/27.webp)

Pilih waktu hitung mundur. Misalnya, jika Anda memilih 1 jam, Anda harus menunggu 1 jam untuk setiap upaya membuka kunci COLDCARD Q.

![CCQ](assets/fr/28.webp)

Setiap kali Anda membuka kunci, Anda akan diminta untuk memasukkan kode PIN.

![CCQ](assets/fr/29.webp)

Kemudian, tunggu waktu yang ditetapkan oleh hitungan mundur.

![CCQ](assets/fr/30.webp)

Di akhir hitungan mundur, Anda harus memasukkan PIN lagi untuk mengakses perangkat.

![CCQ](assets/fr/31.webp)

### Masuk Kalkulator

Opsi ini memungkinkan Anda untuk menyamarkan COLDCARD Anda sebagai kalkulator saat membuka kunci. Untuk mengaktifkan fitur ini, akses menu `Pengaturan > Pengaturan Masuk > Masuk Kalkulator`.

![CCQ](assets/fr/32.webp)

Aktifkan opsi dengan memilihnya.

![CCQ](assets/fr/33.webp)

Mulai sekarang, setiap kali perangkat dihidupkan, kalkulator yang berfungsi dengan perintah dasar akan ditampilkan.

![CCQ](assets/fr/34.webp)

Sebagai contoh, Anda dapat menghitung hash SHA256 dari "*Rencana B Network*".

![CCQ](assets/fr/35.webp)

Untuk membuka kunci COLDCARD dari mode kalkulator, mulailah dengan memasukkan awalan kode PIN Anda diikuti dengan tanda hubung. Sebagai contoh, jika kode PIN Anda adalah `00-00` (kode ini lemah dan hanya contoh, jadi pilihlah kode PIN yang kuat), ketik `00-`. COLDCARD kemudian akan menampilkan dua kata anti-phishing Anda.

![CCQ](assets/fr/36.webp)

Kemudian masukkan kode PIN lengkap Anda, dipisahkan dengan spasi atau tanda hubung, misalnya: `00 00`.

![CCQ](assets/fr/37.webp)

COLDCARD kemudian akan keluar dari mode kalkulator dan membuka kunci secara normal.

## Menghancurkan COLDCARD Anda dengan bersih

Jika Anda berencana untuk membuang COLDCARD Q Anda, misalnya karena Anda sekarang menggunakan dompet perangkat keras lain, penting untuk menghancurkan perangkat dengan benar. Hal ini untuk memastikan bahwa tidak ada informasi yang berkaitan dengan dompet Anda yang dapat dipulihkan oleh pihak ketiga.

Terdapat tiga tingkat penghancuran informasi, tergantung pada kebutuhan Anda. Sebelum memulai, pastikan bahwa dompet Anda sudah diimpor ke dompet perangkat keras lain, Anda memiliki akses ke semua dana Anda dan, yang terpenting, Anda memiliki frasa mnemonik dan kata sandi apa pun, yang keduanya berfungsi. Tanpa cadangan dompet, kehancuran COLDCARD Anda akan mengakibatkan hilangnya bitcoin Anda.

Tingkat penghancuran pertama terdiri dari hanya menghapus benih. Opsi ini menghapus frasa mnemonik Anda dari memori COLDCARD, namun tetap membiarkan perangkat tetap berfungsi. Ini sangat ideal jika Anda ingin menggunakan COLDCARD Q lagi di kemudian hari. Untuk menghapus seed dari memori, akses menu `Tingkat Lanjut/Peralatan > Zona Bahaya > Fungsi Seed > Hancurkan Seed`.

![CCQ](assets/fr/38.webp)

Tingkat penghancuran kedua terdiri dari penonaktifan secara permanen dua chip aman COLDCARD melalui perangkat lunak. Tindakan ini membuat perangkat tidak dapat digunakan sama sekali. Anda tidak akan bisa menjualnya kembali, menggunakannya kembali atau mengembalikannya ke Coinkite: perangkat ini akan dihancurkan secara permanen. Untuk melanjutkan, ikuti langkah-langkah yang dijelaskan di bagian sebelumnya mengenai "*Brick Me*" Kemudian masukkan PIN ini dengan sengaja saat membuka kunci COLDCARD.

Tingkat ketiga melibatkan penghancuran fisik komponen aman COLDCARD Q Anda. Seperti sebelumnya, hal ini akan membuat perangkat tidak dapat digunakan lagi. Untuk melakukannya, gunakan bor untuk membuat lubang pada dua chip di sisi kanan atas perangkat (setelah dibalik), dekat dengan tulisan "*SHOOT HERE*".

**Tindakan pencegahan penting**:


- Untuk menghindari risiko sengatan listrik, keluarkan baterai dari perangkat dan cabut dari stopkontak sebelum menangani.
- Tunggu beberapa menit setelah mematikan unit sebelum memulai pengeboran.
- Kenakan sarung tangan berinsulasi dan kacamata pengaman untuk memastikan keselamatan Anda.

![CCQ](assets/fr/39.webp)

Setelah chip dilubangi, jangan coba-coba menyambungkan kembali COLDCARD Q.

Selamat, Anda sekarang sudah menguasai opsi lanjutan COLDCARD Q!

Jika Anda merasa tutorial ini bermanfaat, saya akan sangat berterima kasih jika Anda memberikan tanda jempol hijau di bawah ini. Jangan ragu untuk membagikan tutorial ini di jejaring sosial Anda. Terima kasih banyak!

Saya juga merekomendasikan tutorial lain ini, di mana kita membahas penggunaan pesaing langsung untuk CCQ, Ledger Flex :

https://planb.network/fr/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a