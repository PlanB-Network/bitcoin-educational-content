---
name: Nerdminer
description: Mulai menambang bitcoin dengan peluang menang mendekati 0
---

![cover](assets/cover.webp)

> Menyiapkan NerdMiner_v2 Anda

Dalam tutorial ini, kami akan memandu Anda melalui langkah-langkah yang diperlukan untuk menyiapkan NerdMiner_v2, yang merupakan perangkat keras (ESP-32 S3) yang didedikasikan untuk penambangan bitcoin.
Tentu saja, kekuatan komputasi dari perangkat seperti ini tidak dapat bersaing dengan ASIC dari penambang amatir atau profesional. Namun, NerdMiner adalah alat edukasi yang sempurna untuk membuat penambangan bitcoin menjadi nyata. Dan siapa tahu, dengan (banyak) keberuntungan, Anda mungkin menemukan blok dan hadiah yang menyertainya. Bagi yang penasaran, kita akan melihat di bagian [Estimasi probabilitas menang](#estimation-de-la-probabilite-de-gain). Dalam hal konsumsi daya, NerdMiner mengonsumsi 0.5W; untuk perbandingan, lampu LED rata-rata mengonsumsi 20 kali lebih banyak.

Sebelum melalui berbagai langkah, mari kita daftar peralatan yang diperlukan untuk membuatnya:

- sebuah [Lilygo T-display S3](https://lilygo.cc/products/t-display-s3)
- sebuah [sumber daya USB-C](https://amzn.eu/d/gIOot90)
- sebuah casing 3D: jika Anda memiliki printer 3D, Anda dapat mengunduh [file 3D](https://www.printables.com/model/501547-nerdminer-v2-click-case-w-buttons) jika tidak, Anda dapat membelinya di [toko online Silexperience](https://silexperience.company.site/NerdMiner_V2-p544379757).
- sebuah PC dengan Chrome Browser terinstal
- sebuah koneksi internet
- sebuah alamat bitcoin

Anda juga dapat membeli kit NerdMiner yang sudah dirakit dari beberapa penjual seperti:

- [DécouvreBitcoin](https://shop.decouvrebitcoin.com/products/nerd-miner?_pos=1&_psq=nerd&_ss=e&_v=1.0)
- [BitMaker](https://bitronics.store/shop/)

Pertama, kita akan melihat cara mem-flash perangkat lunak ke ESP-32 S3, dan kemudian kita akan melihat cara merestartnya untuk mengubah jaringan wifi. Langkah-langkah ini untuk pengguna Windows, jika Anda menggunakan sistem operasi Linux, silakan lakukan [langkah awal](#etapes-preliminaires-pour-utilisateurs-linux) untuk memungkinkan pengenalan ESP-32 S3 oleh sistem Anda.

# Instalasi perangkat lunak NerdMiner_v2

Instalasi perangkat lunak sangat disederhanakan berkat penggunaan webflasher.

## Langkah 1: Persiapan webflasher

Pertama, Anda perlu mengunjungi [NM2 flasher online](https://bitmaker-hub.github.io/diyflasher/).

Kemudian pilih firmware yang sesuai dengan ESP-32 Anda. Kebanyakan waktu itu adalah default: T-Display S3. Kemudian klik pada "Flash".

> ⚠️ Penting bagi Anda untuk menggunakan browser Chrome - karena secara default, memungkinkan penggunaan flash dan akses ke port USB Anda.

![](assets/webflasher.webp)

## Langkah 2: Menghubungkan ESP-32

Setelah webflasher diluncurkan, sebuah jendela pop-up akan terbuka menunjukkan berbagai port USB yang dikenali oleh browser.
Anda kemudian dapat menghubungkan ESP-32 Anda, dan sebuah port baru akan ditampilkan (dalam kasus ini, itu adalah port ttyACM0). Anda kemudian harus memilihnya dan klik pada "connect".
![](assets/flasher-port-serial.webp)

Perangkat lunak kemudian akan diunduh ke ESP32 Anda dalam hitungan detik.

![](assets/NM2-sucessfully-installed.webp)

## Langkah 3: Konfigurasi NerdMiner

Konfigurasi NerdMiner Anda akan dilakukan melalui smartphone atau komputer.
Aktifkan WiFi dan sambungkan ke jaringan lokal NerdMinerAP. Jika Anda menggunakan smartphone, portal konfigurasi akan terbuka secara otomatis. Jika tidak, ketik alamat 192.168.4.1 di browser.
Kemudian pilih "Configure WiFi".

Anda sekarang dapat mengonfigurasi NerdMiner Anda.
Pertama, mulailah dengan terhubung ke jaringan WiFi Anda dengan memilih nama jaringan Anda dan memasukkan kata sandi yang terkait.

Kemudian Anda dapat memilih kolam penambangan yang ingin Anda ikuti. Memang, dalam industri penambangan bitcoin, umum untuk menggabungkan kekuatan komputasi untuk meningkatkan peluang menemukan blok dengan imbalan berbagi hadiah secara proporsional dengan hashrate yang disediakan.
Untuk NerdMiners, Anda dapat memilih untuk terhubung ke salah satu kolam ini:

| URL Kolam         | Port  | URL                        | Status                                   |
| ----------------- | ----- | -------------------------- | ---------------------------------------- |
| public-pool.io    | 21496 | https://web.public-pool.io | Kolam Solo dan sumber terbuka default    |
| pool.nerdminer.io | 3333  | https://nerdminer.io       | Dipelihara oleh CHMEX                    |
| pool.vkbit.com    | 3333  | https://vkbit.com/         | Dipelihara oleh djerfy                   |

Setelah Anda memilih kolam Anda, Anda perlu memasukkan alamat bitcoin Anda untuk menerima hadiah jika (secara luar biasa) sebuah blok ditemukan.

Juga, pilih zona waktu Anda agar NerdMiner dapat menampilkan waktu dengan benar.
Anda sekarang dapat klik pada "save".

![](assets/wifi-configuration.webp)

Selamat, Anda sekarang menjadi bagian dari jaringan penambangan Bitcoin!

## Operasi NerdMiner

Perangkat lunak NerdMinerv2 memiliki 3 layar berbeda, yang dapat Anda akses dengan mengklik tombol atas di sisi kanan layar Anda:

- Layar utama memberikan akses ke statistik NerdMiner Anda.
- Layar kedua memberikan akses ke waktu, hashrate Anda, harga bitcoin, dan tinggi blok.
- Layar ketiga memberikan akses ke statistik tentang jaringan penambangan bitcoin global.
  ![](assets/NM2-screens.webp)

Jika Anda ingin me-reboot NerdMiner Anda, misalnya untuk mengubah jaringan WiFi, Anda perlu menekan tombol atas selama 5 detik.

Menekan tombol bawah sekali akan mematikan NerdMiner Anda. Mengklik dua kali akan memutar orientasi layar.

### Langkah awal untuk pengguna Linux

Berikut adalah langkah-langkah agar Chrome dapat mendeteksi port serial Anda di Linux.

1. Identifikasi port yang terkait:

- Hubungkan ESP-32 Anda ke komputer.
- Buka terminal.
- Masukkan perintah berikut untuk mencantumkan semua port:
  - `dmesg | grep tty`
  - atau `ls /dev/tty*`
- Untuk memastikan portnya, Anda dapat melanjutkan dengan eliminasi dengan mengulangi perintah tanpa ESP-32 terhubung.

2. Ubah izin dari port yang terkait:
- Secara default, akses ke port serial mungkin memerlukan izin root, jadi kita akan membuatnya tersedia dengan menambahkan pengguna Anda ke grup `dialout`.
  - `sudo usermod -a -G dialout NAMA_PENGGUNA_ANDA`, ganti `NAMA_PENGGUNA_ANDA` dengan nama pengguna Anda.
  - kemudian log out dan log in kembali sebagai pengguna ini, atau restart sistem untuk memastikan perubahan grup berlaku.

Sekarang ESP-32 Anda dikenali oleh sistem, Anda bisa kembali ke [langkah pertama](#etape-1-preparation-du-webflasher) untuk instalasi perangkat lunak.

## Kesimpulan

Dan itulah! NerdMiner_v2 Anda sekarang dikonfigurasi dan siap digunakan.

Selamat menambang dan semoga keberuntungan berpihak pada Anda!

### Mengestimasi probabilitas memenangkan

Mari bersenang-senang mengestimasi probabilitas memenangkan hadiah blok. Estimasi ini akan kasar dan hanya berusaha untuk mendapatkan besaran magnitudo dari probabilitas.
Kolam yang dapat NerdMiner terhubung hanya "kolam penambangan solo" yang berarti bahwa kolam tersebut tidak memutualisasikan hashrate dari semua penambang yang terhubung tetapi hanya bertindak sebagai koordinator.
Sekarang mari kita asumsikan bahwa NerdMiner kita memiliki hashrate sekitar 45kH/s.

Mengetahui bahwa total hashrate adalah sekitar 450 EH/s (atau 4.5 x 10^20 hash per detik), kita dapat mempertimbangkan bahwa probabilitas menemukan blok berikutnya adalah 1 dalam 100 juta miliar, yang sangat sangat sangat tidak mungkin terjadi. Jadi selain menjadi alat edukasi dan objek rasa ingin tahu, NerdMiner dapat berfungsi sebagai tiket lotere dalam penambangan bitcoin dengan biaya listrik marginal 0.5 W--meskipun seperti yang baru saja kita lihat probabilitas menangnya sangat rendah. Namun, mengapa tidak mencoba keberuntungan Anda?

### Informasi Tambahan

Berikut adalah beberapa tautan jika Anda ingin membaca lebih lanjut tentang subjek ini:

- [Halaman proyek NerdMiner_v2](http://github.com/BitMaker-hub/NerdMiner_v2)
- [Dokumentasi lengkap NerdMiners](https://docs.bitwater.ch/nerd-miner-v2/)