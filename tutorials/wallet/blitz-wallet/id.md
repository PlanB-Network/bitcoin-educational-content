---
name: Blitz Wallet
description: Dompet Bitcoin paling sederhana.
---

![cover](assets/cover.webp)

Pengalaman pengguna adalah salah satu faktor penentu saat memilih dompet Bitcoin. Dalam tutorial ini, kami memperkenalkan Blitz Wallet, sebuah dompet yang menempatkan kesederhanaan sebagai inti pendekatannya: berkat integrasi protokol **Spark**, Blitz menawarkan salah satu dompet Bitcoin paling sederhana dan paling lengkap di pasaran, dengan pembayaran instan dan tanpa pengelolaan teknis.

## Apa itu Blitz Wallet?

Blitz Wallet adalah dompet Bitcoin **self-custodial** dan **open source**, yang mengutamakan kedaulatan Anda serta pengalaman pengguna yang lancar dan intuitif.

[Blitz Wallet](https://blitz-wallet.com/) adalah aplikasi mobile yang tersedia di Android (Play Store) dan iOS (App Store).

Berbeda dengan dompet Lightning tradisional yang mengharuskan Anda mengelola channel pembayaran dan likuiditas masuk, Blitz Wallet mengandalkan **protokol Spark** untuk menghilangkan kerumitan teknis tersebut. Hasilnya: pembayaran instan sejak satoshi pertama diterima, tanpa konfigurasi awal apa pun. Tujuan Blitz adalah membuat pembayaran bitcoin semudah aplikasi pembayaran biasa, tanpa pernah mengorbankan self-custody dana Anda.

Blitz Wallet juga mendukung **alamat yang mudah dibaca** dalam format `pengguna@domain.com` (melalui LNURL), sehingga mengirim bitcoin semudah mengirim e-mail, tanpa harus berurusan dengan invoice panjang atau QR code untuk setiap transaksi.

## Memahami Protokol Spark

Sebelum masuk ke praktik, ada baiknya memahami teknologi yang menjalankan Blitz Wallet di balik layar: **protokol Spark**.

### Apa itu Spark?

Spark adalah protokol lapisan atas open source yang dibangun di atas Bitcoin, dikembangkan oleh tim Lightspark. Protokol ini memungkinkan transaksi instan dengan biaya rendah, sambil tetap menjaga self-custody bitcoin Anda.

Berbeda dengan Lightning Network yang mengandalkan **channel pembayaran** antara dua pihak, Spark menggunakan teknologi yang disebut **statechain** (rantai status). Prinsip dasarnya adalah sebagai berikut: alih-alih memindahkan bitcoin di blockchain untuk setiap transaksi, Spark mentransfer **hak pengeluaran** dari satu pengguna ke pengguna lain, tanpa perpindahan on-chain.

### Bagaimana cara kerjanya?

Untuk memahami Spark secara intuitif, bayangkan bahwa membelanjakan bitcoin di Spark memerlukan penyelesaian puzzle dua keping:
- Satu keping dipegang oleh pengguna (misalnya, Alice).
- Keping lainnya dipegang oleh sekelompok operator yang disebut **Spark Entity (SE)**.

Hanya kombinasi dari dua keping yang cocok yang dapat membelanjakan bitcoin.

Ketika Alice ingin mengirim bitcoinnya ke Bob, inilah yang terjadi: puzzle baru dibuat bersama antara Bob dan SE. Puzzle tetap memiliki bentuk yang sama, tetapi keping-keping yang menyusunnya berubah. Sekarang, keping Bob yang cocok dengan keping SE. Keping lama Alice menjadi tidak dapat digunakan, karena SE telah menghancurkan keping yang sesuai dengannya. Kepemilikan bitcoin telah berpindah tangan, **tanpa transaksi apa pun di blockchain**.

Bob kemudian dapat mengulangi proses yang sama untuk mengirim bitcoin ini ke Carol, dan seterusnya. Setiap transfer bekerja dengan mengganti keping puzzle, bukan dengan perpindahan dana on-chain.

### Mengapa ini aman?

Pertanyaan yang wajar muncul: apa yang terjadi jika SE tidak benar-benar menghancurkan keping lamanya?

Spark Entity bukanlah entitas tunggal: ini adalah sekelompok operator independen. Keping SE tidak pernah dipegang oleh satu operator saja. Penggantian puzzle memerlukan kerja sama dari beberapa operator. Cukup **satu operator yang jujur** dalam sebuah transfer untuk mencegah pengaktifan kembali puzzle lama. Tidak ada operator tunggal yang dapat secara diam-diam menyimpan puzzle lama yang aktif atau membuatnya kembali di kemudian hari.

Selain itu, Spark memiliki mekanisme penarikan sepihak: Anda selalu dapat mengambil kembali bitcoin Anda secara on-chain tanpa kerja sama dari SE. Mekanisme cadangan ini merupakan bagian integral dari arsitektur Spark, dan menjamin bahwa Anda tidak pernah bergantung pada jaringan untuk mengakses dana Anda.

### Spark vs Lightning Network

Spark dan Lightning tidak bersaing: mereka **saling melengkapi**. Blitz Wallet mengintegrasikan keduanya, sehingga Anda dapat menikmati keunggulan masing-masing.

|                               | **Spark**                    | **Lightning Network**   |
| ----------------------------- | ---------------------------- | ----------------------- |
| **Teknologi**                 | Statechains (rantai status)  | Channel pembayaran      |
| **Pengelolaan channel**       | Tidak diperlukan             | Diperlukan              |
| **Likuiditas masuk**          | Tidak diperlukan             | Diperlukan              |
| **Transaksi instan**          | Ya                           | Ya                      |
| **Self-custody**              | Ya                           | Ya                      |
| **Kompatibilitas Lightning**  | Ya (melalui atomic swaps)    | Natif                   |

Lightning Network tetap merupakan protokol yang sangat baik untuk pembayaran instan, tetapi ia memiliki kendala teknis (pengelolaan channel, likuiditas masuk, node yang harus online...) yang dapat menjadi hambatan bagi pemula. Spark menghilangkan kendala tersebut sambil tetap kompatibel dengan Lightning.

## Instalasi dan Konfigurasi

Dalam tutorial ini, kami menggunakan versi Android dari Blitz Wallet, tetapi semua proses yang dijelaskan di bawah ini juga berlaku untuk iOS.

![installation](assets/fr/01.webp)

Karena Blitz Wallet adalah dompet self-custody, Anda memiliki pilihan antara **membuat dompet baru** atau **mengimpor frasa pemulihan** (12 atau 24 kata) dari dompet yang sudah ada.

Di sini, kami memilih untuk membuat dompet baru. Temukan di bawah ini rekomendasi kami tentang pencadangan frasa pemulihan Anda:

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

❗ **PENTING**: 12 atau 24 kata pemulihan ini adalah **satu-satunya kunci akses ke bitcoin Anda**. Blitz adalah dompet self-custodial: baik Blitz maupun Spark tidak memiliki akses ke frasa pemulihan atau dana Anda. Jika Anda kehilangan kata-kata ini, Anda akan kehilangan akses ke bitcoin Anda secara permanen. Jangan bagikan kepada siapa pun: siapa pun yang memilikinya dapat membelanjakan bitcoin Anda.

Selanjutnya, buat **kode PIN** untuk mengamankan akses ke dompet Anda.

![setup-wallet](assets/fr/02.webp)

## Memulai dengan Blitz

Melakukan transaksi dengan Blitz lebih intuitif dibandingkan kebanyakan dompet Bitcoin lainnya. Antarmukanya minimalis dan berpusat pada tiga tindakan utama: kirim, pindai, dan terima.

### Menerima bitcoin

Untuk menerima bitcoin di dompet Blitz Anda, klik ikon **"Panah bawah"** (↓), masukkan jumlah dalam satoshi yang ingin Anda terima, tambahkan deskripsi opsional, lalu dompet akan menghasilkan invoice yang dapat Anda bagikan kepada pengirim.

⚠️ **CATATAN**: Satoshi (atau "sat") adalah unit terkecil dari bitcoin: **1 bitcoin = 100.000.000 satoshi**.

Salah satu keunikan Blitz Wallet adalah dukungannya terhadap beberapa jaringan dan protokol dalam ekosistem Bitcoin:

- **Lightning Network**: Salah satu lapisan atas Bitcoin yang memungkinkan pembayaran mikro secara instan dengan biaya sangat rendah. Ideal untuk jumlah kecil dalam penggunaan sehari-hari.

- **Bitcoin (on-chain)**: Blockchain utama dari protokol Bitcoin, cocok untuk transaksi dengan jumlah lebih besar di mana keamanan maksimal dan finalitas menjadi prioritas.

- **Liquid Network**: Sebuah sidechain (rantai paralel) dari Bitcoin yang dikembangkan oleh Blockstream, yang memungkinkan transaksi cepat dan rahasia menggunakan Liquid Bitcoin (L-BTC).

https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

Secara default, Blitz menghasilkan invoice Lightning, tetapi Anda dapat memilih jaringan tempat Anda ingin menerima satoshi dengan mengklik tombol **"Choose format"** (Pilih format).

![receive-sats](assets/fr/03.webp)

### Membuat Kontak

Blitz Wallet menyederhanakan pengiriman bitcoin secara berulang melalui sistem kontaknya.

Di menu **Contacts**, Anda dapat menyimpan nama pengguna Blitz atau alamat Lightning (LNURL) yang sering Anda gunakan untuk bertransaksi.

Dengan demikian, Anda dapat mengirim satoshi ke alamat-alamat tersebut dalam beberapa klik, tanpa harus memindai QR code atau memasukkan alamat secara manual setiap kali.

### Mengirim bitcoin

Selain metode klasik pengiriman bitcoin (memindai QR code, memasukkan alamat secara manual), Blitz menawarkan beberapa opsi praktis:

- **Dari gambar** (*From Image*): Impor QR code dari galeri foto Anda.
- **Dari clipboard** (*From Clipboard*): Tempel alamat atau invoice yang telah disalin sebelumnya.
- **Input manual** (*Manual Input*): Masukkan langsung alamat Bitcoin, invoice Lightning, atau alamat yang mudah dibaca (misalnya `pengguna@walletofsatoshi.com`).
- **Dari kontak Anda**: Pilih penerima yang sudah tersimpan untuk mengirim dalam beberapa klik.

Di menu **Wallet**, klik tombol **"Panah atas"** (↑), pilih metode pengiriman Anda, masukkan jumlah yang akan dikirim, tambahkan deskripsi, dan konfirmasi transaksi.

Jumlah minimum untuk melakukan pengiriman saat ini adalah **1.000 satoshi**.

![send-bitcoin](assets/fr/05.webp)

## Toko Blitz

Di luar operasi transfer bitcoin, Blitz Wallet mengintegrasikan toko tempat Anda dapat membelanjakan bitcoin untuk membeli layanan digital langsung dari aplikasi.

Dari menu utama, klik tab **Store** untuk mengakses toko. Anda juga akan menemukan akses ke platform **Bitrefill** yang memungkinkan Anda membeli kartu hadiah dari ribuan merchant di seluruh dunia, langsung dengan bitcoin.

- **Kecerdasan buatan**: Akses model AI generatif terbaru (Claude 3.5 Sonnet, GPT-4o, GPT-4o-mini, Gemini Flash 1.5) dan bayar kredit Anda langsung dalam satoshi. Tersedia beberapa paket sesuai kebutuhan Anda (Casual, Pro, Power).

![ia-credits](assets/fr/06.webp)

- **SMS anonim**: Kirim dan terima SMS ke seluruh dunia tanpa mengungkapkan nomor telepon pribadi Anda. Layanan ini ditagih dalam satoshi untuk setiap pesan yang dikirim.

![sms-credit](assets/fr/07.webp)

- **VPN WireGuard**: Lindungi privasi online Anda dengan berlangganan VPN WireGuard (mingguan, bulanan, atau triwulanan), yang dapat dibayar dengan bitcoin langsung dari toko Blitz. Anda hanya perlu mengunduh aplikasi klien WireGuard di perangkat Anda untuk mulai menggunakannya.

![wireguard](assets/fr/08.webp)

https://planb.academy/tutorials/exchange/centralized/bitrefill-8c588412-1bfc-465b-9bca-e647a647fbc1

## Blitz Wallet di Balik Layar: Mendalami Lebih Jauh

Di balik kemudahan penggunaan Blitz Wallet tersembunyi arsitektur teknis yang dirancang dengan baik, menggabungkan beberapa lapisan ekosistem Bitcoin.

### Distribusi Saldo Anda

Blitz Wallet mengelola saldo Anda secara transparan dengan mendistribusikan dana Anda di antara berbagai protokol sesuai kebutuhan. Ketika saldo Anda kurang dari 500.000 satoshi, Blitz menggunakan **Liquid Network** dan atomic swaps untuk memberikan pengalaman yang lancar dan memungkinkan transaksi di Lightning Network bahkan dengan jumlah kecil.

Pendekatan ini menjamin kemudahan bagi pengguna baru, tanpa perlu memahami mekanisme yang mendasarinya. Anda dapat melihat distribusi saldo Anda di antara berbagai lapisan di menu **Pengaturan > Balance Info**.

![balance](assets/fr/09.webp)

### Mode Lightning (opsional)

Secara default, Blitz Wallet menggunakan Liquid Network dan protokol Spark untuk memberikan pengalaman yang lancar tanpa konfigurasi teknis. Namun, Blitz memberi Anda opsi untuk mengaktifkan **mode Lightning** yang akan secara otomatis membuka channel pembayaran ketika Anda mencapai saldo **500.000 satoshi** (0,005 BTC).

Untuk mengaktifkan mode Lightning, buka **Pengaturan**, lalu di bagian **Pengaturan Teknis**, klik opsi **Node Info**.

![enable-lightning](assets/fr/10.webp)

Berkat protokol Spark, aktivasi ini bersifat **opsional**: Spark sudah memungkinkan pembayaran yang kompatibel dengan Lightning tanpa perlu membuka channel atau mengelola likuiditas masuk. Mode Lightning natif tetap berguna bagi pengguna tingkat lanjut yang ingin memiliki node Lightning mereka sendiri yang terintegrasi dalam aplikasi.

### Point of Sale (PoS)

Blitz Wallet mengintegrasikan fitur **point of sale** yang memungkinkan merchant menerima pembayaran bitcoin langsung dari aplikasi.

Di menu **Pengaturan > Point-of-sale**, Anda dapat mengkonfigurasi:

- Identitas unik toko Anda
- Mata uang fiat lokal untuk menampilkan harga
- Instruksi untuk karyawan Anda
- Opsi tip untuk pelanggan Anda

Pelanggan Anda hanya perlu memindai QR code yang dihasilkan untuk melakukan pembayaran bitcoin secara instan.

![pos](assets/fr/11.webp)

https://planb.academy/tutorials/wallet/mobile/speed-wallet-8715e454-1720-4a7f-8c1d-3da02cf67312

Sumber yang digunakan untuk menulis tutorial ini:
- Blog [Breez](https://breez.technology/) Technology: [*Spark Explained Like You're Five*](https://blog.breez.technology/spark-explained-like-youre-five-8d554aad18d0).
