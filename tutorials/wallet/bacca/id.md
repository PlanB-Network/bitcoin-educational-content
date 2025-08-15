---
name: Bacca
description: Mengkonfigurasi Buku Besar tanpa perangkat lunak Ledger Live
---
![cover](assets/cover.webp)

Jika kamu menggunakan Ledger, kemungkinan besar kamu akan melewati proses melalui perangkat lunak Ledger Live, setidaknya saat konfigurasi awal perangkat, untuk memeriksa keasliannya dan menginstal aplikasi Bitcoin di dalamnya. Namun, setelah konfigurasi awal ini, banyak pengguna Bitcoin lebih memilih beralih ke perangkat lunak manajemen dompet khusus seperti Sparrow atau Liana ketimbang Ledger Live. Ledger memang memproduksi dompet perangkat keras yang sangat bagus, bahkan cepat mengadopsi fitur-fitur terbaru Bitcoin. Tetapi, perangkat lunak mereka belum tentu sesuai dengan kebutuhan spesifik para bitcoiner. Ledger Live justru memuat banyak fitur yang dirancang untuk altcoin, sementara opsi khusus untuk pengelolaan dompet Bitcoin masih terbatas. Sayangnya, Sparrow dan Liana (untuk saat ini) belum memungkinkan kamu menginstal aplikasi Bitcoin di Ledger.

Untuk melewati keharusan menggunakan Ledger Live saat konfigurasi awal Ledger, kamu bisa memakai alat bernama Bacca (atau “Penginstal Ledger”). Perangkat lunak ini memungkinkan kamu menginstal dan memperbarui aplikasi Bitcoin, memverifikasi keaslian Ledger, dan bahkan memperbarui firmware perangkat. Bacca dibuat oleh Antoine Poinsot (alias Darosior), pengembang Bitcoin Core di Chaincode Labs sekaligus salah satu pendiri Revault dan Liana. (https://wizardsardine.com/), dan Pythcoiner.

Dalam tutorial ini, aku akan menunjukkan kepada kamu cara menggunakan alat ini, sehingga kamu bisa melakukannya tanpa perangkat lunak Ledger Live selamanya, sambil tetap menikmati perangkat Ledger. Alat ini bisa digunakan di semua jenis perangkat.: Nano S Classic, Nano S Plus, Nano X, Flex, dan Stax.

---
*Harap diperhatikan bahwa alat ini cukup baru, dan pengembangnya menyatakan bahwa alat ini masih **dalam tahap pengujian**. Mereka merekomendasikan untuk menggunakannya hanya untuk tujuan pengujian, dan bukan untuk perangkat yang dimaksudkan untuk menampung dompet Bitcoin yang sebenarnya, meskipun hal itu memungkinkan untuk dilakukan. Dalam hal ini, aku menyarankanmu untuk mengikuti rekomendasi dari pengembang alat ini, yang ditentukan [pada README repositori GitHub mereka](https://github.com/darosior/ledger_installer).*

---
## Prasyarat

Pada komputer kamu, kamu akan membutuhkan dua alat untuk menggunakan Bacca:


- Git ;
- Karat.

Jika kamu sudah menginstalnya, kamu bisa melewati langkah ini.

**Linux:**

ada distribusi Linux, Git biasanya sudah terinstal. Untuk mengecek apakah Git sudah ada di sistem kamu, kamu bisa mengetik perintah berikut di terminal :

```bash
git --version
```

Jika kamu belum menginstal Git di sistemmu, berikut adalah perintah untuk menginstalnya di Debian :

```bash
sudo apt install git
```

Terakhir, untuk menginstal setup Rust kamu, gunakan perintah :

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

**Jendela:**

Untuk menginstal Git, kunjungi [situs web resmi proyek](https://git-scm.com/). Unduh perangkat lunak dan ikuti petunjuk pemasangan.

![BACCA](assets/fr/01.webp)

Lanjutkan dengan cara yang sama untuk menginstal Rust dari [situs web resmi](https://www.rust-lang.org/tools/install).

![BACCA](assets/fr/02.webp)

**MacOS:**

Jika Git belum terinstal di sistem , buka terminal dan jalankan perintah berikut untuk menginstalnya:

```bash
git --version
```

Jika Git tidak terinstal di sistem, sebuah jendela akan terbuka dan menawarkanmu untuk menginstal Xcode, yang di dalamnya termasuk Git. Cukup ikuti petunjuk di layar untuk melanjutkan penginstalan.

Untuk menginstal Rust, jalankan perintah berikut:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

## Instalasi Bacca

Buka terminal, lalu masuk ke folder tempat kamu ingin menyimpan perangkat lunak, dan jalankan perintah berikut:

```bash
git clone https://github.com/darosior/ledger_installer.git
```

Masuk ke direktori tempat perangkat lunak berada:

```bash
cd ledger_installer
```

Kemudian gunakan Cargo untuk mengkompilasi proyek dan menjalankan GUI Bacca:

```bash
cargo run -p ledger_manager_gui
```

Anda sekarang memiliki akses ke antarmuka perangkat lunak.

![BACCA](assets/fr/03.webp)

## Mengonfigurasi Ledger

Sebelum memulai, kalau Ledger kamu masih baru, pastikan sudah mengatur kode PIN dan menyimpan frasa pemulihan. Kamu nggak perlu Ledger Live untuk langkah awal ini. Cukup sambungkan Ledger lewat kabel USB untuk menyalakannya. Kalau kamu masih ragu bagaimana melakukan kedua langkah ini, kamu bisa merujuk ke tutorial awal khusus untuk model Ledger kamu:

https://planb.network/tutorials/wallet/hardware/ledger-c6fc7d82-91e7-4c74-bad7-cbff7fea7a88

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

## Menggunakan Bacca

Sambungkan Ledger kamu ke komputer dan buka kuncinya dengan kode PIN yang sudah kamu atur. Bacca akan otomatis mendeteksi Ledger kamu.

![BACCA](assets/fr/04.webp)

Untuk memastikan keaslian Ledger kamu, klik tombol "Cek". Kamu perlu mengonfirmasi koneksi di perangkat Ledger untuk melanjutkan.

![BACCA](assets/fr/05.webp)

Bacca akan memberi tahu kamu kalau Ledger kamu asli. Kalau tidak, itu berarti perangkat mungkin telah disusupi atau palsu. Dalam kasus ini, hentikan penggunaannya segera.

![BACCA](assets/fr/06.webp)

Pada menu "*Apps*", kamu dapat melihat daftar aplikasi yang telah terinstal pada Ledger milikmu.

![BACCA](assets/fr/07.webp)

Untuk menginstal aplikasi Bitcoin, klik "*Instal*", kemudian otorisasi instalasi pada Ledger yang kamu punya.

![BACCA](assets/fr/08.webp)

Aplikasi sudah terinstal dengan baik.

![BACCA](assets/fr/09.webp)

Jika kamu belum menginstal aplikasi versi terbaru, Bacca akan menampilkan tombol "*Update*" dan bukannya "*Latest*". Cukup klik tombol ini untuk memperbarui aplikasi.

![BACCA](assets/fr/10.webp)

Setelah Ledger kamu dikonfigurasi dengan benar dan aplikasi Bitcoin-nya versi terbaru, kamu siap mengimpor dan menggunakan dompet kamu di software manajemen seperti Sparrow atau Liana, tanpa perlu lewat Ledger Live!

Kalau kamu merasa tutorial ini bermanfaat, aku bakal sangat berterima kasih kalau kamu kasih jempol hijau di bawah ini. Jangan ragu juga untuk membagikan artikel ini di media sosial kamu. Terima kasih banyak!

Aku juga menyarankan kamu untuk melihat tutorial tentang GnuPG ini, yang menjelaskan cara memeriksa integritas dan keaslian software sebelum menginstalnya. Ini adalah praktik penting, apalagi saat menginstal software manajemen dompet seperti Liana atau Sparrow:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

