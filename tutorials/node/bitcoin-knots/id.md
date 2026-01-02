---
name: Bitcoin Knots
description: Bagaimana cara menjalankan node dengan klien alternatif Bitcoin Knots
---
![cover](assets/cover.webp)

Bitcoin Knots adalah implementasi alternatif dari protokol Bitcoin yang berasal dari Bitcoin Core. Dikembangkan dan dikelola oleh Luke Dashjr, klien ini menawarkan beberapa fitur tambahan dan penyesuaian aturan pada Mempool, namun tetap kompatibel dengan node lain di jaringan. Bitcoin Knots mengintegrasikan Bitcoin Wallet, tetapi juga bisa digunakan sebagai node Bitcoin sederhana bersama dengan perangkat lunak wallet lainnya.

## Mengapa menggunakan Knot daripada Core?

Saat ini, Core adalah implementasi mayoritas dari protokol Bitcoin di jaringan. Protokol Bitcoin hanyalah sekumpulan aturan dan butuh perangkat lunak untuk menerapkannya. Mesin yang menjalankan perangkat lunak yang mengimplementasikan protokol Bitcoin disebut node, dan semua node ini bersama-sama membentuk jaringan Bitcoin.

Sepanjang sejarah Bitcoin, banyak klien yang berasal dari perangkat lunak awal yang dikembangkan oleh Satoshi Nakamoto telah muncul. Sampai sekarang (Maret 2025), Bitcoin Core adalah mayoritas dengan hampir 98% node di jaringan Bitcoin menggunakan klien ini.

Tapi ada juga perangkat lunak alternatif. Ini bukan node yang terhubung dengan Altcoin seperti Bitcoin Cash, tapi klien alternatif yang kompatibel dengan jaringan Bitcoin yang sebenarnya. Dari semuanya, Bitcoin Knots adalah yang paling terkenal dan saat ini mewakili sekitar 1,4% dari jaringan. Klien alternatif lainnya masih sangat sedikit.

![Image](assets/fr/01.webp)

Ada dua alasan utama untuk menggunakan klien alternatif seperti Knots daripada Core:


- **Teknis**: Klien-klien ini sering menawarkan opsi yang berbeda dibanding Core, terutama soal manajemen Mempool, dengan menentukan transaksi mana yang diterima dan disiarkan oleh node kamu.
- **Kebijakan**: Beberapa orang lebih suka menggunakan klien alternatif seperti Knots untuk alasan non-teknis, terutama untuk mendukung alternatif dari Core dan mengurangi monopoli Core. Jika Core mengalami masalah, akan sangat berguna punya klien alternatif yang solid dan terpelihara dengan baik, serta tahu cara menggunakannya. Ada juga yang memakai Knots sebagai bentuk protes karena sudah kehilangan kepercayaan pada pengembang Core atau tidak setuju dengan pengelolaan klien mayoritas.

## Bagaimana cara memasang Bitcoin Knot?

Kunjungi [situs web resmi Bitcoin Knot](https://bitcoinknots.org/#download) untuk mengunduh versi untuk sistem operasi Anda. Jangan lupa untuk mengunduh sidik jari dan tanda tangan untuk memverifikasi perangkat lunak. File-file ini juga tersedia [di repositori GitHub Bitcoin Knots](https://github.com/bitcoinknots/Bitcoin).

![Image](assets/fr/02.webp)

Sebelum menginstal perangkat lunak di komputer kamu, aku sangat menyarankan untuk memeriksa keaslian dan integritasnya. Kalau kamu belum tahu caranya, lihat tutorial lainnya ini:

https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Setelah perangkat lunak diverifikasi, instal perangkat lunak dengan mengikuti langkah-langkah yang ditunjukkan pada panel instalasi.

![Image](assets/fr/03.webp)

## Meluncurkan IBD

Pertama kali kamu menjalankan Bitcoin Knots, kamu bisa memilih direktori lokal tempat data node kamu (termasuk blockchain, set UTXO, dan parameter) akan disimpan.

![Image](assets/fr/04.webp)

Kamu juga bisa memilih untuk memangkas data blockchain agar hanya menyimpan blok terbaru. Opsi ini memungkinkan node kamu memeriksa setiap blok sepenuhnya dalam batas penyimpanan yang ditentukan, lalu secara bertahap menghapus blok yang paling lama. Kalau kamu punya ruang disk yang cukup (saat ini sekitar 650 GB dan terus bertambah), biarkan opsi ini tidak dicentang. Kalau ruang disk kamu terbatas, aktifkan pruning dan tentukan kapasitas maksimum yang diizinkan.

Perhatikan bahwa kalau node kamu di-prune dan kamu menggunakannya untuk menyinkronkan wallet yang dipulihkan, kamu tidak akan bisa mengambil transaksi yang lebih lama dari blok tertua yang tersimpan secara lokal.

![Image](assets/fr/05.webp)

Opsi lain yang tersedia adalah *Assume Valid.* Opsi ini mempercepat sinkronisasi awal dengan melewati verifikasi tanda tangan untuk transaksi yang ada di blok sebelum blok tertentu.

Tujuan *Assume Valid* adalah mempercepat sinkronisasi pertama node tanpa mengurangi keamanan secara signifikan, dengan mengasumsikan bahwa transaksi-transaksi tersebut sebelumnya sudah divalidasi secara luas oleh jaringan. Satu-satunya kompromi penting adalah node kamu tidak akan mendeteksi pencurian Bitcoin yang terjadi jauh sebelumnya, tetapi tetap menjamin keakuratan jumlah total bitcoin yang beredar. Node kamu akan memverifikasi semua tanda tangan transaksi setelah blok yang ditentukan. Pendekatan ini didasarkan pada asumsi bahwa transaksi yang sudah diterima jaringan sejak lama tanpa perselisihan kemungkinan besar valid.

Sebagai contoh, di sini Assume Valid diatur pada blok no. 855000 `00000000000000000000000233ea80aa10d38aa4486cd7033fffc2c4df556d0b9138`, yang diterbitkan pada 1 Agustus 2024. Selama IBD, node aku hanya akan mulai melakukan verifikasi tanda tangan penuh dari blok ini dan seterusnya.

![Image](assets/fr/06.webp)

Kemudian klik tombol *OK* untuk memulai Initial Block Download. Kamu harus sabar selama proses sinkronisasi awal. Jika kamu ingin melanjutkannya nanti, cukup tutup perangkat lunaknya dan matikan komputer. Sinkronisasi akan berlanjut tanpa masalah saat kamu membuka program lagi.

![Image](assets/fr/07.webp)

## Menyiapkan Simpul Bitcoin Anda

Klik tab "*Settings*", kemudian pilih "*Options*".

![Image](assets/fr/08.webp)

Pada tab "*Main*", kamu mengakses parameter utama node:


- "*Start...*" secara otomatis meluncurkan node ketika komputer kamu dinyalakan untuk segera memulai sinkronisasi;
- "*Prune...*" menyesuaikan batas penyimpanan jika kamu memilih untuk memangkas Blockchain ;
- "*Cache basis data...*" menetapkan jumlah maksimum RAM yang diizinkan untuk node kamu;
- Terakhir, aktifkan "*Enable RPC server*" jika kamu ingin menghubungkan node Bitcoin Knots kamu ke perangkat lunak portofolio lainnya, seperti Sparrow Wallet atau Liana misalnya.

![Image](assets/fr/09.webp)

Pada tab "*Wallet*", Kamu akan menemukan pengaturan untuk wallet terintegrasi yang bisa kamu buat nanti di Knots. Aku menyarankan agar kamu mengaktifkan RBF dan coin control. Kamu juga bisa menentukan jenis script yang akan digunakan.

![Image](assets/fr/10.webp)

Tab "*Network*" berisi parameter jaringan yang bisa kamu sesuaikan dengan kebutuhan spesifik kamu.

![Image](assets/fr/11.webp)

Tab "*Mempool*" memungkinkan kamu untuk mengonfigurasi *Memory Pool*, yaitu pengelolaan transaksi yang belum dikonfirmasi yang disimpan dalam memori, dan ukuran maksimum yang dialokasikan untuk fungsi ini (300 MB secara default).

![Image](assets/fr/12.webp)

Tab *Penyaringan spam* adalah fitur Bitcoin Knots. Di sini kamu akan menemukan beberapa pengaturan yang memungkinkan kamu memilih transaksi mana yang akan diterima atau ditolak untuk disiarkan. Tujuan utamanya adalah membatasi penggunaan tertentu yang dianggap marjinal di Bitcoin, terutama meta-protokol, untuk memerangi praktik tersebut sambil menghindari beban berlebih pada node kamu. Ini adalah pilihan yang bersifat politis dan bergantung pada visi pribadimu tentang Bitcoin.

Kamu juga akan menemukan parameter klasik seperti definisi ambang batas "*Dust*".

Tapi parameter ini hanya mempengaruhi aturan standardisasi. Node kamu akan tetap menerima transaksi yang belum dikonfirmasi selama transaksi itu termasuk dalam sebuah blok, supaya tetap kompatibel dengan node lain di jaringan Bitcoin. Pengaturan ini hanya mengubah cara node kamu memproses dan mendistribusikan transaksi yang belum dikonfirmasi ke rekan-rekan node. Dalam praktiknya, karena Knots adalah minoritas, aturan standarisasi di jaringan masih mengikuti default dari Bitcoin Core.

![Image](assets/fr/13.webp)

Tab "*Mining*" memungkinkanmu mengonfigurasi kemungkinan partisipasi node milikmu dalam Mining, kalau kamu ingin mengaktifkan fungsi ini.

![Image](assets/fr/14.webp)

Terakhir, tab "*Display*" menyangkut parameter yang berkaitan dengan grafik Interface, termasuk bahasa perangkat lunak.

![Image](assets/fr/15.webp)

## Membuat portofolio Bitcoin

Setelah sinkronisasi awal selesai, node Bitcoin Knots kamu sudah berfungsi penuh. Kamu sekarang bisa menghubungkan node ini ke perangkat lunak wallet lainnya, atau langsung memakai hot wallet bawaan. Untuk melanjutkan, klik tombol Buat *Wallet baru.*

![Image](assets/fr/16.webp)

Berikan nama pada Wallet kamu. Kamu juga dapat melindunginya dengan passphrase BIP39 dengan mengklik "*Enkripsi Wallet*". Setelah siap, klik tombol "*Create*".

![Image](assets/fr/17.webp)

Passphrase BIP39 adalah kata sandi opsional yang bisa kamu pilih selain seedphrase untuk meningkatkan keamanan wallet kamu. Sebelum mengonfigurasi fitur ini, aku sangat menyarankan kamu membaca artikel berikut yang menjelaskan secara detail cara kerja passphrase secara teori dan cara menghindari kesalahan yang bisa menyebabkan hilangnya bitcoin kamu secara permanen:

https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
Kalau kamu mengaktifkan passphrase, pilih yang kuat dan simpan dengan hati-hati di satu atau beberapa media fisik yang aman.

![Image](assets/fr/18.webp)

Portofolio Bitcoin kamu sekarang telah dibuat.

![Image](assets/fr/19.webp)

## Mencadangkan portofolio Bitcoin Anda

Bahkan sebelum kamu menerima bitcoin pertamamu, sangat penting untuk membuat backup wallet agar kamu bisa memulihkan dana jika komputer hilang atau rusak. Untuk melakukannya, klik pada tab "*File*" dan kemudian "*Backup Wallet*".

![Image](assets/fr/20.webp)

Operasi ini menghasilkan satu file yang bisa digunakan untuk memulihkan semua bitcoin kamu. Jadi berhati-hatilah dan simpan di media eksternal yang aman.

## Menerima bitcoin

Untuk menerima bitcoin langsung ke Knot Wallet kamu, klik tombol "*Terima*".

![Image](assets/fr/21.webp)

Tetapkan *Label* pada address kamu untuk memudahkan identifikasi tujuan dan mempermudah penggunaan coin control di masa depan. Kamu juga bisa menentukan jumlah yang akan diterima pada address ini, atau menambahkan pesan untuk pembayar. Setelah semuanya diatur, klik *Minta pembayaran.*

![Image](assets/fr/22.webp)

Bitcoin Knot kemudian menampilkan Address penerima, yang dapat kamu salin atau pindai dan kirimkan ke pembayar.

![Image](assets/fr/23.webp)

Setelah transaksi disiarkan, kamu dapat mengikuti statusnya secara langsung di menu "*Transactions*".

![Image](assets/fr/24.webp)

## Kirim bitcoin

Sekarang setelah kamu memiliki bitcoin di dalam Knots Wallet, kamu dapat mengirimkannya. Untuk melakukannya, klik tombol "*Kirim*".

![Image](assets/fr/25.webp)

Klik tombol "*Input...*" untuk memilih UTXO yang ingin kamu belanjakan dalam transaksi ini.

![Image](assets/fr/26.webp)

Masukkan Bitcoin Address penerima.

![Image](assets/fr/27.webp)

Tambahkan label untuk mengingat tujuan transaksi ini.

![Image](assets/fr/28.webp)

Masukkan jumlah yang ingin kamu kirim ke Address ini.

![Image](assets/fr/29.webp)

Klik tombol "*Pilih...*" untuk memilih tarif biaya yang sesuai untuk transaksi kamu, berdasarkan status jaringan saat ini.

![Image](assets/fr/30.webp)

Jika semuanya sudah sesuai dengan keinginan kamu, klik tombol "*Kirim*". Jika kamu menggunakan passphrase, kamu akan diminta untuk mengisinya pada tahap ini.

![Image](assets/fr/31.webp)

Periksa parameter transaksi kamu untuk terakhir kalinya, lalu jika semuanya sudah benar, klik tombol Kirim sekali lagi untuk menandatangani dan mendistribusikan transaksi kamu.

![Image](assets/fr/32.webp)

Transaksi kamu yang menunggu konfirmasi sekarang muncul di tab "*Transaksi*".

![Image](assets/fr/33.webp)

## Menghubungkan node Anda ke program lain

Bitcoin Knots yang terintegrasi dengan antarmuka untuk mengelola wallet kamu belum tentu yang paling intuitif, dan fungsinya masih cukup terbatas. Tapi kamu bisa menghubungkan node Bitcoin Knots kamu ke perangkat lunak manajemen wallet khusus untuk lebih mudah mengakses data blockchain dan menyiarkan transaksi.

Prosedurnya akan tergantung pada perangkat lunak yang kamu pakai, tapi ada dua skenario utama: Bitcoin Knots diinstal di komputer yang sama dengan perangkat lunak wallet, atau dijalankan di mesin terpisah.

### Dengan Bitcoin Knot lokal:

Kalau Bitcoin Knots terinstal di komputermu, cari file `bitcoin.conf` di antara file perangkat lunaknya. Kalau file ini belum ada, kamu bisa membuatnya. Buka file tersebut dengan editor teks dan masukkan baris berikut:

```ini
server=1
```

Kemudian simpan perubahan kamu.

Kamu juga dapat melakukan ini melalui grafik Bitcoin-QT Interface dengan menavigasi ke "*Pengaturan*" > "*Options...*" dan aktifkan opsi "*Enable RPC server*".

Jangan lupa untuk memulai ulang perangkat lunak setelah melakukan perubahan ini.

![Image](assets/fr/34.webp)

Lalu buka perangkat lunak manajemen wallet kamu (misalnya Sparrow Wallet atau Liana) dan masukkan path menuju file cookie kamu, yang biasanya ada di folder yang sama dengan `bitcoin.conf`, tergantung sistem operasi kamu:

|**macOS**|~/Perpustakaan/Dukungan Aplikasi/Bitcoin

|---|---|

|**Windows**|%APPDATA%\Bitcoin|

|**Linux**|~/.Bitcoin|

![Image](assets/fr/35.webp)

Biarkan parameter lain sebagai default, URL `127.0.0.1` dan port `8332`, lalu klik "*Test Connection*".

![Image](assets/fr/36.webp)

### Dengan Bitcoin Knot jarak jauh:

Kalau Bitcoin Knots diinstal di mesin lain yang terhubung ke jaringan yang sama, pertama cari file `bitcoin.conf` di antara file perangkat lunaknya. Kalau file ini belum ada, kamu bisa membuatnya. Buka file tersebut dengan editor teks dan tambahkan baris berikut:

```ini
server=1
```

Setelah mengedit file, pastikan kamu menyimpannya dalam folder yang sesuai untuk sistem operasi:

|**macOS**|~/Perpustakaan/Dukungan Aplikasi/Bitcoin

|---|---|

|**Windows**|%APPDATA%\Bitcoin|

|**Linux**|~/.Bitcoin|

Operasi ini juga bisa dilakukan lewat antarmuka grafik Bitcoin-QT. Buka menu Settings, lalu Options..., dan aktifkan Enable RPC server dengan mencentang kotaknya. Jika file bitcoin.conf belum ada, kamu bisa membuatnya langsung dari antarmuka ini dengan klik *Open Configuration File.*

![Image](assets/fr/37.webp)

Temukan IP Address dari mesin yang menghosting Bitcoin Knot di jaringan lokal Anda. Untuk melakukan ini, Anda dapat menggunakan alat seperti [Angry IP Scanner](https://angryip.org/). Mari kita asumsikan, untuk kepentingan argumen, bahwa IP Address dari node Anda adalah `192.168.1.18`.

Pada berkas `Bitcoin.conf`, tambahkan baris berikut, atur `rpcbind=192.168.1.18` untuk mencocokkan IP Address node.

```ini
[main]
rpcbind=127.0.0.1
rpcbind=192.168.1.18
rpcallowip=127.0.0.1
rpcallowip=192.168.1.0/24
```

![Image](assets/fr/38.webp)

Tambahkan juga nama pengguna dan kata sandi untuk sambungan jarak jauh ke file `Bitcoin.conf`. Pastikan untuk mengganti `loic` dengan nama pengguna dan `my_password` dengan kata sandi yang kuat:

```ini
rpcuser=loic
rpcpassword=my_password
```

![Image](assets/fr/39.webp)

Setelah memodifikasi dan menyimpan file, jalankan kembali Bitcoin Knots.

Sekarang kamu dapat membuka perangkat lunak manajemen portofolio (misalnya, Sparrow Wallet atau Liana). Pada Sparrow, buka tab "*User / Pass*". Masukkan nama pengguna dan kata sandi yang telah kamu konfigurasikan dalam file `Bitcoin.conf`. Biarkan parameter lainnya sebagai default, yaitu URL `127.0.0.1` dan port `8332`. Kemudian klik "*Test Connection*".

![Image](assets/fr/40.webp)

Sambungan sudah dibuat.

Sekarang kamu sudah tahu semua tentang implementasi alternatif Bitcoin Knots.

Kalau kamu merasa tutorial ini bermanfaat, aku akan sangat berterima kasih kalau kamu mau memberikan jempol hijau di bawah ini. Jangan ragu membagikannya di jejaring sosial kamu. Terima kasih banyak.

Aku juga merekomendasikan tutorial lain yang menjelaskan cara menyiapkan node Lightning kamu sendiri:

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a
