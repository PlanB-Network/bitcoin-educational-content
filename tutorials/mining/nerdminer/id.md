---
name: Nerdminer
description: Mulai menambang bitcoin dengan peluang menang mendekati 0
---

![cover](assets/cover.webp)

## Konfigurasi NerdMiner v2 Anda

Dalam tutorial ini, kami akan memandu kamu melalui langkah-langkah yang diperlukan untuk menyiapkan NerdMiner_v2, yang merupakan perangkat keras (ESP-32 S3) yang didedikasikan untuk penambangan bitcoin.
Tentu saja, kekuatan komputasi dari perangkat seperti ini tidak dapat bersaing dengan ASIC dari penambang amatir atau profesional. Namun, NerdMiner adalah alat edukasi yang sempurna untuk membuat penambangan bitcoin menjadi nyata. Dan siapa tahu, dengan (banyak) keberuntungan, kamu mungkin menemukan blok dan hadiah yang bisa didapatkan. Bagi yang penasaran, kita akan melihat di bagian [Estimasi probabilitas menang](#estimation-de-la-probabilite-de-gain). Dalam hal konsumsi daya, NerdMiner mengonsumsi 0.5W; untuk perbandingan, lampu LED rata-rata mengonsumsi 20 kali lebih banyak.

Sebelum melalui berbagai langkah, mari kita daftar peralatan yang diperlukan untuk membuatnya:

- sebuah [Lilygo T-display S3](https://lilygo.cc/products/t-display-s3)
- sebuah [sumber daya USB-C](https://amzn.eu/d/gIOot90)
- sebuah casing 3D: jika kamu memiliki printer 3D, kamu dapat mengunduh [file 3D](https://www.printables.com/model/501547-nerdminer-v2-click-case-w-buttons) jika tidak, kamu dapat membelinya di [toko online Silexperience](https://silexperience.company.site/NerdMiner_V2-p544379757).
- sebuah PC dengan Chrome Browser terinstal
- sebuah koneksi internet
- sebuah alamat bitcoin

kamu juga dapat membeli kit NerdMiner yang sudah dirakit dari beberapa penjual seperti:

- [DécouvreBitcoin](https://shop.decouvrebitcoin.com/products/nerd-miner?_pos=1&_psq=nerd&_ss=e&_v=1.0)
- [BitMaker](https://bitronics.store/shop/)

Pertama, kita akan melihat cara mem-flash perangkat lunak ke ESP-32 S3, dan kemudian kita akan melihat cara merestartnya untuk mengubah jaringan wifi. Langkah-langkah ini untuk pengguna Windows, jika kamu menggunakan sistem operasi Linux, silakan lakukan [langkah awal](#etapes-preliminaires-pour-utilisateurs-linux) untuk memungkinkan pengenalan ESP-32 S3 oleh sistem kamu.

## Instalasi perangkat lunak NerdMiner_v2

Instalasi perangkat lunak sangat disederhanakan berkat penggunaan webflasher.

### Langkah 1: Persiapan webflasher

Pertama, kamu perlu mengunjungi [NM2 flasher online](https://bitmaker-hub.github.io/diyflasher/).

Kemudian pilih firmware yang sesuai dengan ESP-32 kamu. Kebanyakan waktu itu adalah default: T-Display S3. Kemudian klik pada "Flash".

> ⚠️ Penting bagi kamu untuk menggunakan browser Chrome - karena secara default, memungkinkan penggunaan flash dan akses ke port USB Anda.

![](assets/webflasher.webp)

### Langkah 2: Menghubungkan ESP-32

Setelah webflasher diluncurkan, sebuah jendela pop-up akan terbuka yang menampilkan berbagai port USB yang dikenali oleh browser.
Kamu kemudian bisa menghubungkan ESP32 kamu, dan sebuah port baru akan muncul (dalam contoh ini, port tersebut adalah ttyACM0), lalu pilih port tersebut dan klik "connect".
![](assets/flasher-port-serial.webp)

Perangkat lunak kemudian akan diunduh ke ESP32 Anda dalam hitungan detik.

![](assets/NM2-sucessfully-installed.webp)

### Langkah 3: Konfigurasi NerdMiner

Konfigurasi NerdMiner kamu dilakukan melalui smartphone atau komputer.
Aktifkan WiFi lalu sambungkan ke jaringan lokal NerdMinerAP. Jika kamu menggunakan smartphone, portal konfigurasi akan terbuka secara otomatis. Jika tidak, ketik alamat 192.168.4.1 di browser.
Kemudian pilih "Configure WiFi".

Sekarang kamu bisa mengonfigurasi NerdMiner kamu.
Pertama, mulai dengan terhubung ke jaringan WiFi kamu dengan memilih nama jaringan dan memasukkan kata sandi yang sesuai.

Selanjutnya, kamu bisa memilih kolam penambangan yang ingin kamu ikuti. Dalam industri penambangan Bitcoin, memang sudah umum untuk menggabungkan kekuatan komputasi guna meningkatkan peluang menemukan sebuah blok, dengan imbalan pembagian hadiah secara proporsional berdasarkan hashrate yang disumbangkan.
Untuk NerdMiner, kamu bisa memilih untuk terhubung ke salah satu kolam berikut:

| URL Kolam         | Port  | URL                        | Status                                   |
| ----------------- | ----- | -------------------------- | ---------------------------------------- |
| public-pool.io    | 21496 | https://web.public-pool.io | Kolam Solo dan sumber terbuka default    |
| pool.nerdminer.io | 3333  | https://nerdminer.io       | Dipelihara oleh CHMEX                    |
| pool.vkbit.com    | 3333  | https://vkbit.com/         | Dipelihara oleh djerfy                   |

Setelah Anda memilih kolam kamu, kamu perlu memasukkan alamat bitcoin Anda untuk menerima hadiah jika (secara luar biasa) sebuah blok ditemukan.

Juga, pilih zona waktu kamu agar NerdMiner dapat menampilkan waktu dengan benar.
Kamu sekarang dapat klik pada "save".

![](assets/wifi-configuration.webp)

Selamat, kamu sekarang menjadi bagian dari jaringan penambangan Bitcoin!

### Operasi NerdMiner

Perangkat lunak NerdMinerv2 memiliki 3 layar berbeda, yang dapat kamu akses dengan mengklik tombol atas di sisi kanan layar kamu:

- Layar utama memberikan akses ke statistik NerdMiner kamu.
- Layar kedua memberikan akses ke waktu, hashrate kamu, harga bitcoin, dan tinggi blok.
- Layar ketiga memberikan akses ke statistik tentang jaringan penambangan bitcoin global.
  ![](assets/NM2-screens.webp)

Jika kamu ingin me-reboot NerdMiner kamu, misalnya untuk mengubah jaringan WiFi, kamu perlu menekan tombol atas selama 5 detik.

Menekan tombol bawah sekali akan mematikan NerdMiner kamu. Mengklik dua kali akan memutar orientasi layar.

#### Langkah awal untuk pengguna Linux

Berikut adalah langkah-langkah agar Chrome dapat mendeteksi port serial kamu di Linux.

1. Identifikasi port yang terkait:

- Hubungkan ESP-32 kamu ke komputer.
- Buka terminal.
- Masukkan perintah berikut untuk mencantumkan semua port:
  - `dmesg | grep tty`
  - atau `ls /dev/tty*`
- Untuk memastikan portnya, kamu dapat melanjutkan dengan eliminasi dengan mengulangi perintah tanpa ESP-32 terhubung.

2. Ubah izin dari port yang terkait:
- Secara default, akses ke port serial mungkin memerlukan izin root, jadi kita akan membuatnya tersedia dengan menambahkan pengguna Anda ke grup `dialout`.
  - `sudo usermod -a -G dialout NAMA_PENGGUNA_ANDA`, ganti `NAMA_PENGGUNA_ANDA` dengan nama pengguna kamu.
  - kemudian log out dan log in kembali sebagai pengguna ini, atau restart sistem untuk memastikan perubahan grup berlaku.

Sekarang ESP-32 kamu dikenali oleh sistem, Anda bisa kembali ke [langkah pertama](#etape-1-preparation-du-webflasher) untuk instalasi perangkat lunak.

### Kesimpulan

Dan itulah! NerdMiner_v2 Anda sekarang dikonfigurasi dan siap digunakan.

Selamat menambang dan semoga keberuntungan berpihak pada Anda!

#### Mengestimasi probabilitas memenangkan

Mari bersenang-senang mengestimasi probabilitas memenangkan hadiah blok. Estimasi ini bersifat kasar dan hanya bertujuan untuk mendapatkan orde besaran dari probabilitas tersebut.
Kolam yang bisa dihubungkan oleh NerdMiner hanyalah "kolam penambangan solo", yang berarti kolam ini tidak memutualisasikan hashrate dari semua penambang yang terhubung, melainkan hanya bertindak sebagai koordinator.
Sekarang mari kita asumsikan bahwa NerdMiner kita memiliki hashrate sekitar 45 kH/s.

Dengan mengetahui bahwa total hashrate jaringan sekitar 450 EH/s (atau 4.5 x 10^20 hash per detik), kita dapat memperkirakan bahwa probabilitas untuk menemukan blok berikutnya adalah 1 banding 100 juta miliar, sesuatu yang sangat, sangat, sangat tidak mungkin terjadi. Jadi, selain menjadi alat edukasi dan objek rasa ingin tahu, NerdMiner juga dapat berfungsi sebagai tiket lotere dalam penambangan Bitcoin dengan konsumsi listrik marginal sekitar 0.5 W, meskipun seperti yang baru saja kita lihat, probabilitas untuk menang sangatlah rendah. Namun, kenapa tidak mencoba peruntungan kamu?

#### Informasi Tambahan

Berikut adalah beberapa tautan jika kamu ingin membaca lebih lanjut tentang subjek ini:

- [Halaman proyek NerdMiner_v2](http://github.com/BitMaker-hub/NerdMiner_v2)
- [Dokumentasi lengkap NerdMiners](https://docs.bitwater.ch/nerd-miner-v2/)
