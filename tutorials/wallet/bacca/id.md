---
name: Bacca
description: Mengkonfigurasi Buku Besar tanpa perangkat lunak Ledger Live
---
![cover](assets/cover.webp)

Jika Anda menggunakan Ledger, Anda mungkin menemukan bahwa Anda harus melalui perangkat lunak Ledger Live, setidaknya untuk konfigurasi perangkat awal, untuk memeriksa keasliannya dan menginstal aplikasi Bitcoin di dalamnya. Namun, setelah konfigurasi ini, banyak pengguna Bitcoin yang lebih memilih untuk menggunakan perangkat lunak manajemen dompet Bitcoin khusus seperti Sparrow atau Liana daripada Ledger Live. Meskipun Ledger memproduksi dompet perangkat keras yang sangat baik yang dengan cepat menyertakan fitur-fitur Bitcoin terbaru, perangkat lunak mereka belum tentu disesuaikan dengan kebutuhan spesifik para bitcoiners. Memang, Ledger Live menyertakan banyak fitur yang dirancang untuk altcoin, sementara opsi yang didedikasikan untuk manajemen dompet Bitcoin terbatas. Tetapi masalah dengan Sparrow dan Liana (untuk saat ini), adalah mereka tidak mengizinkan Anda untuk menginstal aplikasi Bitcoin di Ledger.

Untuk melewati kebutuhan untuk menggunakan Ledger Live selama konfigurasi awal Ledger Anda, Anda dapat menggunakan alat Bacca, (atau "Penginstal Ledger"). Perangkat lunak ini memungkinkan Anda untuk menginstal dan memperbarui aplikasi Bitcoin, memverifikasi keaslian Ledger Anda, dan bahkan memperbarui firmware perangkat. Bacca diciptakan oleh Antoine Poinsot (Darosior), pengembang Bitcoin Core di Chaincode Labs, salah satu pendiri Revault dan Liana (https://wizardsardine.com/), dan Pythcoiner.

Dalam tutorial ini, saya akan menunjukkan kepada Anda cara menggunakan alat ini, sehingga Anda dapat melakukannya tanpa perangkat lunak Ledger Live untuk selamanya, dan tetap menikmati perangkat Ledger. Alat ini dapat digunakan di semua perangkat: Nano S Classic, Nano S Plus, Nano X, Flex, dan Stax.

---
*Harap diperhatikan bahwa alat ini cukup baru, dan pengembangnya menyatakan bahwa alat ini masih **dalam tahap pengujian**. Mereka merekomendasikan untuk menggunakannya hanya untuk tujuan pengujian, dan bukan untuk perangkat yang dimaksudkan untuk menampung dompet Bitcoin yang sebenarnya, meskipun hal itu memungkinkan untuk dilakukan. Dalam hal ini, saya sarankan Anda untuk mengikuti rekomendasi dari pengembang alat ini, yang ditentukan [pada README repositori GitHub mereka](https://github.com/darosior/ledger_installer).*

---
## Prasyarat

Pada komputer Anda, Anda akan membutuhkan dua alat untuk menggunakan Bacca:


- Git ;
- Karat.

Jika Anda sudah menginstalnya, Anda dapat melewati langkah ini.

**Linux:**

Pada distribusi Linux, Git umumnya sudah terinstal. Untuk memeriksa apakah Git telah terinstal pada sistem Anda, Anda dapat mengetikkan perintah berikut di terminal :

```bash
git --version
```

Jika Anda belum menginstal Git di sistem Anda, berikut adalah perintah untuk menginstalnya di Debian :

```bash
sudo apt install git
```

Terakhir, untuk menginstal lingkungan pengembangan Rust Anda, gunakan perintah :

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

**Jendela:**

Untuk menginstal Git, kunjungi [situs web resmi proyek](https://git-scm.com/). Unduh perangkat lunak dan ikuti petunjuk pemasangan.

![BACCA](assets/fr/01.webp)

Lanjutkan dengan cara yang sama untuk menginstal Rust dari [situs web resmi](https://www.rust-lang.org/tools/install).

![BACCA](assets/fr/02.webp)

**MacOS:**

Jika Git belum terinstal di sistem Anda, buka terminal dan jalankan perintah berikut untuk menginstalnya:

```bash
git --version
```

Jika Git tidak terinstal di sistem Anda, sebuah jendela akan terbuka dan menawarkan Anda untuk menginstal Xcode, yang di dalamnya termasuk Git. Cukup ikuti petunjuk di layar untuk melanjutkan penginstalan.

Untuk menginstal Rust, jalankan perintah berikut:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

## Instalasi Bacca

Buka terminal dan buka folder tempat Anda ingin menyimpan perangkat lunak, lalu jalankan perintah berikut:

```bash
git clone https://github.com/darosior/ledger_installer.git
```

Navigasikan ke direktori perangkat lunak:

```bash
cd ledger_installer
```

Kemudian gunakan Cargo untuk mengkompilasi proyek dan menjalankan GUI Bacca:

```bash
cargo run -p ledger_manager_gui
```

Anda sekarang memiliki akses ke antarmuka perangkat lunak.

![BACCA](assets/fr/03.webp)

## Mengkonfigurasi Buku Besar

Sebelum memulai, jika Ledger Anda masih baru, pastikan Anda telah mengatur kode PIN dan menyimpan frasa pemulihan. Anda tidak memerlukan Ledger Live untuk langkah awal ini. Cukup sambungkan Ledger Anda melalui kabel USB untuk menyalakannya. Jika Anda tidak yakin bagaimana cara melanjutkan kedua langkah ini, Anda dapat merujuk ke awal tutorial khusus untuk model Anda:

https://planb.network/tutorials/wallet/hardware/ledger-c6fc7d82-91e7-4c74-bad7-cbff7fea7a88

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

## Menggunakan Bacca

Hubungkan Buku Besar Anda ke komputer Anda dan buka kuncinya menggunakan kode PIN yang telah Anda tetapkan. Bacca akan secara otomatis mendeteksi Ledger Anda.

![BACCA](assets/fr/04.webp)

Untuk mengonfirmasi keaslian Buku Besar Anda, klik tombol "*Cek*". Anda perlu mengesahkan koneksi pada perangkat Ledger Anda untuk melanjutkan.

![BACCA](assets/fr/05.webp)

Bacca kemudian akan memberi tahu Anda jika Ledger Anda asli. Jika tidak, ini mengindikasikan bahwa perangkat telah disusupi, atau perangkat tersebut palsu. Dalam hal ini, segera hentikan penggunaannya.

![BACCA](assets/fr/06.webp)

Pada menu "*Apps*", Anda dapat melihat daftar aplikasi yang telah terinstal pada Ledger Anda.

![BACCA](assets/fr/07.webp)

Untuk menginstal aplikasi Bitcoin, klik "*Instal*", kemudian otorisasi instalasi pada Ledger Anda.

![BACCA](assets/fr/08.webp)

Aplikasi sudah terinstal dengan baik.

![BACCA](assets/fr/09.webp)

Jika Anda belum menginstal aplikasi Bitcoin versi terbaru, Bacca akan menampilkan tombol "*Update*" dan bukannya "*Latest*". Cukup klik tombol ini untuk memperbarui aplikasi.

![BACCA](assets/fr/10.webp)

Setelah Ledger Anda dikonfigurasi dengan benar dengan versi terbaru aplikasi Bitcoin, Anda siap untuk mengimpor dan menggunakan dompet Anda pada perangkat lunak manajemen seperti Sparrow atau Liana, tanpa harus melalui Ledger Live!

Jika Anda merasa tutorial ini bermanfaat, saya akan sangat berterima kasih jika Anda memberikan jempol hijau di bawah ini. Jangan ragu untuk membagikan artikel ini di jejaring sosial Anda. Terima kasih banyak!

Saya juga menyarankan Anda untuk melihat tutorial tentang GnuPG ini, yang menjelaskan cara memeriksa integritas dan keaslian perangkat lunak Anda sebelum menginstalnya. Ini adalah praktik penting, terutama ketika menginstal perangkat lunak manajemen portofolio seperti Liana atau Sparrow :


https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

