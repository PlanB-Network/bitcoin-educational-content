---
name: Sats.mobi

description: Kustodian Wallet yang dapat diakses melalui Telegram
---

![cover](assets/cover.webp)


tutorial ini ditulis oleh_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)


## Sats.Mobi

SatsMobi adalah Wallet yang beroperasi di Telegram, menampilkan semua fungsi Lightning Network (kustodian) Wallet, ditambah serangkaian fitur yang sangat menghibur. SatsMobi berasal dari Fork LightningTipBot yang sekarang sudah tidak diproduksi lagi, mewarisi semua fiturnya sambil menambahkan fitur-fitur terbaru, sehingga membuatnya lebih modern. Seperti LNTipBot, Sats.Mobi juga menganut filosofi sumber terbuka. Wallet dapat dikonfigurasi dan dikelola secara independen dengan mengkloningnya dari [repositori] ini (https://github.com/massmux/SatsMobiBot).


Jika Anda lebih suka menggunakannya secara sederhana, memulai obrolan di Telegram akan mengungkapkan bahwa itu adalah bot.


## Pengaturan

Dari bilah pencarian Telegram, cari "satsmobi" dan tautan ke [bot] (@SatsMobiBot) akan muncul.


**Perhatian**: Jika Anda tidak yakin tentang pencarian melalui Telegram, akses bot dengan aman menggunakan [tautan] berikut ini (https://t.me/SatsMobiBot)


![image](assets/it/01.webp)


Yang perlu Anda lakukan untuk memulai adalah menekan _MULAI_


![image](assets/it/02.webp)


Untuk menjelajahi Wallet, Anda dapat memilih _Menu_ di bagian kiri bawah.


![image](assets/it/03.webp)


Sekarang pilihlah _/help_ di antara perintah-perintah utama.


![image](assets/it/04.webp)


Sats.Mobi menyambut kami dengan menampilkan sebuah pesan, berisi daftar semua fungsi utama. Pada saat startup, bot juga membuat LN Address, yang ditautkan ke pegangan yang dipilih di Telegram (yang unik secara default). Perintah untuk mengirim dan menerima Sats dengan Wallet ini terlihat, serta fungsi-fungsi lain yang akan kita lihat nanti. Menarik juga untuk melihat menu _/advanced_


![image](assets/it/05.webp)


Terlihat bahwa Sats.Mobi juga menciptakan LN Address anonim, yang digunakan untuk mendapatkan privasi. Bot ini bekerja dengan perintah: cukup klik pada kata yang sesuai, atau ketik garis miring "/" pada bilah pesan, diikuti dengan perintah yang ingin Anda jalankan. Meskipun Wallet baru saja dibuat, pilihlah misalnya _/transactions_


![image](assets/it/06.webp)


Perintah ini menampilkan daftar transaksi terakhir, dalam hal ini sama dengan nol.


![image](assets/it/07.webp)


## Menerima Sats

Perintah untuk membuat Invoice dan menerima Sats adalah _/invoice_. Sats.Mobi beroperasi secara eksklusif di Satoshi, unit terkecil dari Bitcoin; oleh karena itu, untuk membuat Invoice, Anda perlu menulis jumlah dalam Sats di bilah pesan dan kemudian mengirimkannya dalam obrolan dengan bot.

![image](assets/it/08.webp)


Dalam contoh berikut, pilihan dibuat untuk menerima jumlah 210 Sats.


![cover](assets/it/09.webp)


Setelah beberapa saat menunggu Invoice disiapkan, maka akan muncul dalam bentuk teks dan kode QR. Membayar dengan Invoice, Wallet akan menampilkan saldo. Jika karena suatu alasan jumlah total tidak diperbarui, tulis _/balance_ dan tekan tombol `enter`.


![image](assets/it/10.webp)


## Mengirim Sats


Meskipun Sats adalah aset yang sangat berharga, yang tidak boleh dilepaskan begitu saja, Sats.Mobi membuat bagian ini menarik, melakukan beberapa tes singkat (yaitu, beberapa transaksi uji coba) tidak akan menjadi masalah.


### Membayar Invoice


Cara termudah untuk membayar Invoice adalah dengan menyalin string pesan `lnbc1xxxxx` dan menempelkannya ke dalam bilah pesan setelah mengetikkan perintah _/pay_. **Sintaks yang benar** mengharuskan adanya spasi setelah perintah.


![image](assets/it/11.webp)


Wallet akan mengirimkan pesan yang meminta konfirmasi. Dengan mengklik _Bayar_, Invoice dibayar.


![image](assets/it/12.webp)


Sats.Mobi dapat mengandalkan node Lightning yang efisien dan terhubung dengan baik, jarang sekali pembayaran gagal karena selalu berhasil menemukan perutean yang benar.


### Membayar dengan nyaman dari ponsel


Menjelajah di Telegram, Sats.Mobi juga tersedia di ponsel. Fungsi yang paling nyaman untuk membayar dengan ponsel adalah memindai kode QR, tetapi Wallet ini tidak memiliki fungsi tersebut, karena Wallet bukanlah aplikasi yang berdiri sendiri, melainkan terdapat dalam jejaring sosial. Oleh karena itu, Sats.Mobi diprogram untuk memfasilitasi pengalaman seluler semaksimal mungkin: aplikasi ini memang dapat memecahkan kode gambar, seperti foto yang diambil dari kode QR Invoice yang ingin Anda bayar.


Misalnya, Anda ingin membayar Invoice sebesar 50 Sats.


![image](assets/it/20.webp)


Ketika ini ditunjukkan kepada kami, kami dapat mengambil foto kode QR terkait.


![image](assets/it/21.webp)


Kami kemudian membuka Telegram di ponsel dan, dalam obrolan dengan Sats.Mobi, lampirkan foto yang baru saja diambil dari kode QR


![cover](assets/it/22.webp)


Setelah dipilih, kami mengirimkannya ke bot:


![image](assets/it/23.webp)

Sats.Mobi menerjemahkan foto dan **segera menampilkan permintaan pembayaran**, dengan deskripsi yang benar. Obrolan akan meminta konfirmasi, untuk melanjutkan, Anda harus menekan _/bayar_

![image](assets/it/24.webp)


Mohon tunggu beberapa saat agar pembayaran dapat diproses.


![image](assets/it/25.webp)


Invoice seharga 50 Sats telah dibayar, hasil yang dicapai tanpa menggunakan kamera dan fungsi pemindaian terintegrasi.


### Sats.Mobi di Grup Telegram


![image](assets/it/27.webp)


Di antara fitur-fitur yang membuat LNTipBot terkenal dan yang dibawa oleh Sats.Mobi ke Telegram, adalah fitur yang membuat pengalaman menjadi menyenangkan dan interaktif bagi para anggota di dalam grup.

Pemilik dapat mengundang bot untuk bergabung dengan obrolan grup dan kemudian menominasikan Sats.Mobi sebagai admin. Sejak saat itu, kesenangan dimulai, karena anggota dapat mulai memberi penghargaan kepada pengguna lain atas kontribusi mereka ke grup.


- _/tip_ menambahkan tip dengan membalas pesan;
- _/send_ mengirim dana dengan menentukan LN Address atau pegangan Telegram sebagai penerima;
- _/faucet_ (di menu _/advanced_) memungkinkan pembuatan serangkaian kiat yang dapat dikumpulkan oleh anggota tercepat dalam grup dengan mengeklik _/collect_;
- _/tipjar_ (di menu _/advanced_) membuat jenis distribusi lain yang dapat dikirim ke pengguna dalam grup.


Masing-masing perintah ini memiliki sintaks, yang dijelaskan dalam menu perintah utama.


Dan jika kita bukan pemilik grup? Tidak masalah: cukup minta pendiri grup untuk mengundang Sats.Mobi, tambahkan sebagai admin grup, dan Anda sudah siap!


## Tempat Penjualan (POS)


Ketika Sats.Mobi diluncurkan untuk pertama kalinya, bot juga menciptakan fitur lain untuk pengguna: **POS**. "Perangkat" ini diaktifkan oleh pengguna dengan perintah _/pos_ atau dengan mengklik tombol terkait dari konsol di kanan bawah. Faktanya, POS adalah aplikasi web, yang terbuka sebagai pop-up di obrolan Telegram


![image](assets/it/14.webp)


Interface menampilkan pegangan Telegram pribadi pengguna di kiri atas dan digunakan dengan cara yang sama seperti semua POS: dengan mengetikkan jumlah pada keypad. Anggaplah sekarang kita ingin mengumpulkan 21 sen euro untuk sebuah layanan. Mengetahui bahwa Sats.Mobi hanya mengelola Sats secara native, tidak mudah untuk melakukan konversi di kepala Anda. Sebaliknya, POS menampilkan euro sebagai unit akun, yang sekaligus menunjukkan padanannya dalam Satoshi.


![image](assets/it/15.webp)

Mengklik _/OK_ akan menampilkan Invoice yang dapat ditunjukkan kepada pelanggan melalui kode QR, atau yang dapat dikirim sebagai string melalui pesan instan, sehingga dapat dibayar.

![image](assets/it/16.webp)

![image](assets/it/17.webp)


Tentu saja, POS juga tersedia di ponsel, diakses dengan cara yang sama seperti yang ditunjukkan sebelumnya.


![image](assets/it/18.webp)


Ini juga ditampilkan dengan baik pada layar ponsel:


![image](assets/it/19.webp)


## Fitur Tambahan


Ada fitur lain yang melengkapi penawaran Sats.Mobi Wallet, yang, seperti yang telah kita lihat, memperluas konsep Wallet di luar operasi penerimaan dan pengiriman pembayaran:


- _/nostr_: untuk menghubungkan Wallet ke pengguna Nostr Anda sendiri untuk menerima zaps;
- _/cashback_: menunjukkan kode yang dapat ditunjukkan kepada pedagang untuk mendapatkan cashback atas pembelian;
- _/buy_: memulai prosedur yang dipandu di dalam bot, yang memungkinkan pembelian Sats dengan harga euro;
- _/activatecard_: untuk meminta aktivasi kartu debit NFC, yang dapat diisi ulang melalui Sats.Mobi Wallet dan yang dapat diaktifkan notifikasinya;
- _/link_: membuat tautan untuk Zeus atau Blue Wallet Anda sendiri, yang dapat digunakan sebagai remote control untuk Wallet ini.


## Kesimpulan

Sats.Mobi merupakan Wallet yang menyenangkan dan menyenangkan untuk digunakan, yang membawa kembali pengalaman menggunakan LNTipBot dengan menggunakan fungsi yang lebih canggih dari LNBits. Namun, penting untuk diingat bahwa **ini adalah layanan kustodian**. Oleh karena itu, layanan ini sebaiknya digunakan untuk menyimpan sedikit Sats, bukan sebagai Wallet utama untuk dana Lightning Network Anda. Ada juga batas kapasitas intrinsik, yaitu 500.000 Sats, batas yang disarankan untuk tidak dilampaui.


Jika Anda mencari dompet Lightning Network non-kustodian, sangat disarankan untuk melihat produk lain.


---
### Dokumentasi


- [Github](https://github.com/massmux/SatsMobiBot)
- Daftar putar demo [video] (https://www.youtube.com/results?search_query=Sats.mobi)