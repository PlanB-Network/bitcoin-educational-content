---
name: Sats.mobi
description: Wallet (kustodian) dalam jangkauan Telegram
---
![cover](assets/cover.webp)

tutorial ini ditulis oleh_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)

# Sats.Mobi

SatsMobi adalah Wallet yang berjalan di Telegram, yang memiliki semua fungsi Wallet Lightning Network (kustodian) dan menawarkan, sebagai tambahan, sejumlah fitur yang sangat menyenangkan. Ini berasal dari Fork dari LightningTipBot, yang sekarang sudah tidak diproduksi lagi, mewarisi semua fitur-fiturnya sambil menambahkan fitur-fitur terbaru, membuatnya lebih modern. Dari LNTipBot, Sats.Mobi juga menelusuri filosofi open source. Wallet sebenarnya dapat dikonfigurasi dan dikelola sendiri dengan mengkloningnya dari [repositori] ini (https://github.com/massmux/SatsMobiBot).

Sebaliknya, jika Anda lebih suka menggunakannya dengan cara yang sederhana, cukup mulai obrolan di Telegram dan Anda akan menemukan bahwa itu adalah bot.

# Pengaturan

Dari bilah pencarian Telegram, cari "satsmobi" dan tautan ke [bot] (@SatsMobiBot) akan muncul.

**Perhatian**: Jika Anda tidak yakin dengan pencarian melalui Telegram, akses bot dengan aman menggunakan [tautan] berikut ini (https://t.me/SatsMobiBot)

![image](assets/it/01.webp)

Anda hanya perlu menekan _START_ untuk memulainya

![image](assets/it/02.webp)

Untuk menjelajahi Wallet, Anda dapat memilih _Menu_ di sudut kiri bawah.

![image](assets/it/03.webp)

Pilihlah _/help_ di antara perintah-perintah utama.

![image](assets/it/04.webp)

Sats.Mobi menyambut kami dengan menampilkan sebuah pesan, berisi daftar semua fitur utama. Pada saat startup, bot juga telah membuat LN Address, yang ditautkan ke pegangan yang dipilih pada Telegram (yang unik secara default). Perintah untuk mengirim dan menerima Sats dengan Wallet ini terlihat, serta fungsi-fungsi lain yang akan kita lihat nanti. Menarik juga untuk melihat menu _/advanced_ segera

![image](assets/it/05.webp)

Ternyata Sats.Mobi juga telah menciptakan LN Address anonim, yang dapat digunakan untuk mendapatkan privasi. Bot ini bekerja dengan perintah: cukup klik pada kata yang sesuai, atau ketik garis miring "/" pada bilah pesan, diikuti dengan perintah yang ingin Anda jalankan. Meskipun Wallet baru saja dibuat, pilihlah, misalnya, _/transactions_

![cimageover](assets/it/06.webp)

Perintah ini menunjukkan daftar transaksi terakhir, dalam hal ini nol.

![image](assets/it/07.webp)

# Menerima Sats

Perintah untuk membuat Invoice dan menerima Sats adalah _/invoice_. Sats.Mobi secara eksklusif menggunakan Satoshi, unit terkecil di Bitcon; oleh karena itu, untuk membuat Invoice, Anda perlu menulis jumlah dalam Sats di bilah pesan dan kemudian mengirimkannya dalam obrolan dengan bot.

![image](assets/it/08.webp)

Dalam contoh berikut ini, jumlah 210 Sats dipilih untuk diterima.

![cover](assets/it/09.webp)

Setelah beberapa saat menunggu Invoice disiapkan, Wallet tersedia dalam bentuk teks dan kode QR. Dengan membayar Invoice, Wallet akan menampilkan saldo. Jika karena suatu hal jumlah totalnya tidak sesuai, tulis _/balance_ dan tekan tombol `kirim`.

![image](assets/it/10.webp)

# Kirim Sats

Meskipun Satss adalah aset tak ternilai yang tidak boleh dipisahkan secara dangkal, Sats.Mobi membuat bagian ini menarik, melakukan beberapa tes singkat (yaitu, beberapa transaksi uji) tidak akan menjadi masalah.

## Membayar Invoice

Cara termudah untuk membayar Invoice adalah dengan menyalin string pesan `lnbc1xxxxx` dan menempelkannya ke dalam bilah pesan setelah mengetikkan perintah _/pay_. **Sintaks yang benar** adalah dengan menyisakan spasi setelah perintah.

![image](assets/it/11.webp)

Wallet mengirimkan pesan yang meminta konfirmasi. Dengan mengklik _Bayar_, Invoice telah dibayar.

![image](assets/it/12.webp)

Sats.Mobi dapat mengandalkan node Lightning yang efisien dan terhubung dengan baik, jarang sekali pembayaran gagal karena selalu dapat menemukan perutean yang benar.

## Bayar dengan nyaman dari ponsel

Beralih ke Telegram, Sats.Mobi juga tersedia di ponsel. Fungsi yang paling nyaman untuk pembayaran seluler adalah membingkai kode QR, tetapi Wallet ini tidak memiliki fungsi ini, karena ini bukan aplikasi yang berdiri sendiri, tetapi terkandung dalam aplikasi sosial. Oleh karena itu, Sats.Mobi diprogram untuk membuat pengalaman seluler semudah mungkin: aplikasi ini dapat memecahkan kode gambar, seperti foto yang diambil dari kode QR Invoice yang ingin Anda bayar.

Misalnya, kita ingin membayar Invoice sebesar 50 Sats.

![image](assets/it/20.webp)

Ketika ini ditunjukkan kepada kami, kami dapat mengambil gambar kode QR yang relevan.

![image](assets/it/21.webp)

Kami kemudian membuka Telegram di ponsel dan, dalam obrolan dengan Sats.Mobi, lampirkan foto yang baru saja kami ambil ke kode QR

![cover](assets/it/22.webp)

Setelah dipilih, kami mengirimkannya ke bot:

![image](assets/it/23.webp)

Sats.Mobi menerjemahkan foto dan **menyajikan permintaan pembayaran** dengan segera, dengan deskripsi yang benar. Obrolan meminta konfirmasi, untuk melanjutkan, Anda harus menekan _/bayar_

![image](assets/it/24.webp)

Kami menunggu beberapa saat agar pembayaran dapat diproses.

![image](assets/it/25.webp)

Invoice x 50 Sats dibayar, hasil yang dicapai tanpa menggunakan kamera dan fungsi pemindaian built-in.

## Sats.Mobi di Grup Telegram

![image](assets/it/27.webp)

Dari semua fitur yang membuat LNTipBot terkenal dan yang dibawa kembali oleh Sats.Mobi ke Telegram, ada satu fitur yang membuat pengalaman anggota dalam grup menjadi menyenangkan dan interaktif.

Pemilik dapat mengundang bot untuk bergabung dalam obrolan grup dan kemudian menunjuk Sats.Mobi sebagai admin. Sejak saat itu, kesenangan dimulai, karena anggota dapat mulai memberi penghargaan kepada pengguna lain atas kontribusi mereka dalam grup.


- _/tip_ menambahkan tip dengan merespons sebuah pesan;
- _/send_ mengirim dana dengan menentukan LN Address atau pegangan Telegram sebagai penerima;
- _/faucet_ (di menu _/advanced_) memungkinkan Anda untuk membuat satu set kiat yang dapat dikumpulkan oleh anggota grup tercepat dengan mengeklik _/collect_;
- _/tipjar_ (di menu _/advanced_) membuat jenis distribusi lain yang dapat dikirim ke pengguna dalam grup.

Masing-masing perintah ini memiliki sintaksnya sendiri, yang dijelaskan dalam menu perintah utama.

Bagaimana jika kita bukan pemilik grup? Tidak masalah: cukup minta pendiri untuk mengundang Sats.Mobi, tambahkan dia sebagai admin, dan selesai!

# Tempat Penjualan (POS)

Saat memulai Sats.Mobi untuk pertama kalinya, bot juga membuat fitur lain untuk pengguna: **POS**. "Perangkat" ini diaktifkan oleh pengguna dengan perintah _/pos_ atau dengan mengklik tombol yang relevan dari konsol di sudut kanan bawah. Faktanya, POS adalah aplikasi web, yang terbuka sebagai pop-up di obrolan Telegram

![image](assets/it/14.webp)

Interface membawa pegangan pribadi Telegram di sudut kiri atas dan digunakan dengan mudah seperti menggunakan semua POS: dengan mengetikkan jumlah pada keypad. Sekarang misalkan kita ingin mengumpulkan 21 sen untuk sebuah layanan. Mengetahui bahwa Sats.Mobi secara native hanya menangani Satss, tidak mudah untuk melakukan konversi di kepala Anda. Sebagai gantinya, POS menampilkan euro sebagai unit akun sambil menunjukkan padanannya dalam Satoshi.

![image](assets/it/15.webp)

Mengklik _/OK_ akan memunculkan Invoice yang dapat ditunjukkan kepada pelanggan melalui kode QR, atau yang dapat dikirim sebagai string melalui pesan instan, sehingga dapat dibayar

![image](assets/it/16.webp)

![image](assets/it/17.webp)

Tentu saja, POS juga tersedia di ponsel dengan memanggilnya dengan cara yang sama seperti yang ditunjukkan di atas.

![image](assets/it/18.webp)

Ini juga menampilkan dirinya sendiri yang dapat dilihat dengan baik dari layar ponsel:

![image](assets/it/19.webp)

# Fitur tambahan

Ada fitur-fitur lain yang melengkapi penawaran Wallet Sats.Mobi, yang, seperti yang telah kita lihat, memperluas konsep Wallet di luar operasi penerimaan dan pengiriman pembayaran:


- _/nostr_: untuk menghubungkan Wallet ke Nostr penggunanya untuk menerima zaps;
- _/cashback_: menunjukkan kode yang dapat Anda tunjukkan kepada pedagang untuk mendapatkan cashback atas suatu pengeluaran;
- _/buy_: memulai wizard di dalam bot, yang memungkinkan Anda untuk membeli Sats dengan harga euro:
- _/activatecard_: untuk meminta aktivasi kartu debit NFC, yang dapat dimuat ulang melalui Wallet Sats.Mobi dan yang notifikasi dapat diaktifkan;
- _/link_: membuat tautan untuk Wallet Zeus atau Wallet Biru Anda sendiri, yang dapat Anda gunakan sebagai kendali jarak jauh Wallet ini.

# Kesimpulan

Sats.Mobi merupakan Wallet yang menyenangkan dan asyik untuk digunakan, mengembalikan pengalaman menggunakan LNTipBot dengan menggunakan fitur yang lebih canggih dari LNBits. Namun, penting untuk diingat bahwa **ini adalah layanan kustodian**. Oleh karena itu, layanan ini hanya digunakan untuk kustodian beberapa Satss; layanan ini bukan merupakan prinsipal Wallet untuk dana Lightning Network-nya sendiri. Ada juga batas kapasitas yang melekat sebesar 500.000 Satss, batas yang tidak disarankan untuk dilampaui.

Jika Anda mencari Wallet Lightning Network non-kustodian, Anda harus mencari produk lain.

---
### Dokumentasi


- [Github](https://github.com/massmux/SatsMobiBot)
- Daftar putar demo [video] (https://www.youtube.com/results?search_query=Sats.mobi)