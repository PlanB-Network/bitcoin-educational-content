---
name: Sats.mobi

description: Kustodian Wallet yang dapat diakses melalui Telegram
---

![cover](assets/cover.webp)


tutorial ini ditulis oleh_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)


## Sats.Mobi

SatsMobi adalah Wallet yang beroperasi di Telegram, menghadirkan semua fungsi Lightning Network (kustodian) Wallet, ditambah serangkaian fitur yang sangat menghibur. SatsMobi berasal dari fork LightningTipBot yang sekarang sudah tidak lagi dikembangkan, mewarisi semua fiturnya sambil menambahkan fitur-fitur terbaru, sehingga membuatnya lebih modern. Seperti LNTipBot, SatsMobi juga menganut filosofi sumber terbuka. Wallet dapat dikonfigurasi dan dikelola secara independen dengan mengkloningnya dari [repositori](https://github.com/massmux/SatsMobiBot) ini.


Jika kamu lebih suka menggunakannya secara sederhana, memulai obrolan di Telegram akan mengungkapkan bahwa itu adalah bot.


## Pengaturan

Dari bilah pencarian Telegram, cari "satsmobi" dan tautan ke [bot](@SatsMobiBot) akan muncul.


**Perhatian**: Jika kamu tidak yakin tentang pencarian melalui Telegram, akses bot dengan aman menggunakan [tautan] berikut ini (https://t.me/SatsMobiBot)


![image](assets/it/01.webp)


Yang perlu kamu lakukan untuk memulai adalah menekan _MULAI_


![image](assets/it/02.webp)


Untuk menjelajahi Wallet, kamu dapat memilih _Menu_ di bagian kiri bawah.


![image](assets/it/03.webp)


Sekarang pilihlah _/help_ di antara perintah-perintah utama.


![image](assets/it/04.webp)


SatsMobi menyambut kita dengan menampilkan sebuah pesan yang berisi daftar semua fungsi utama. Saat pertama kali dijalankan, bot juga membuat LN Address yang ditautkan ke username Telegram yang kamu pakai (unik secara default). Perintah untuk mengirim dan menerima Sats dengan Wallet ini langsung terlihat, begitu juga fungsi-fungsi lain yang akan kita bahas nanti. Menarik juga untuk melihat menu _/advanced_


![image](assets/it/05.webp)


Terlihat bahwa Sats.Mobi juga menciptakan LN Address anonim, yang digunakan untuk mendapatkan privasi. Bot ini bekerja dengan perintah: cukup klik pada kata yang sesuai, atau ketik garis miring "/" pada bilah pesan, diikuti dengan perintah yang ingin Anda jalankan. Meskipun Wallet baru saja dibuat, pilihlah misalnya _/transactions_


![image](assets/it/06.webp)


Perintah ini menampilkan daftar transaksi terakhir, dalam hal ini sama dengan nol.


![image](assets/it/07.webp)


## Menerima Sats

Perintah untuk membuat Invoice dan menerima Sats adalah _/invoice_. SatsMobi beroperasi secara eksklusif dalam Satoshi, unit terkecil dari Bitcoin; jadi untuk membuat Invoice, kamu cukup menuliskan jumlah dalam Sats di kolom pesan lalu mengirimkannya di obrolan dengan bot.

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


Saat digunakan di Telegram, SatsMobi juga bisa diakses lewat ponsel. Fungsi paling nyaman untuk membayar lewat ponsel biasanya adalah memindai kode QR, tetapi Wallet ini tidak memiliki fitur tersebut karena bukan aplikasi yang berdiri sendiri, melainkan berjalan di dalam jejaring sosial. Karena itu, SatsMobi diprogram untuk memaksimalkan pengalaman seluler: Wallet ini bisa membaca dan mendekode gambar, seperti foto kode QR Invoice yang ingin kamu bayar.

Misalnya, kamu ingin membayar Invoice sebesar 50 Sats.


![image](assets/it/20.webp)


Ketika ini ditunjukkan kepada kami, kami dapat mengambil foto kode QR terkait.


![image](assets/it/21.webp)


Kami kemudian membuka Telegram di ponsel dan, dalam obrolan dengan Sats.Mobi, lampirkan foto yang baru saja diambil dari kode QR


![cover](assets/it/22.webp)


Setelah dipilih, kami mengirimkannya ke bot:


![image](assets/it/23.webp)

Sats.Mobi menerjemahkan foto dan **segera menampilkan permintaan pembayaran**, dengan deskripsi yang benar. Obrolan akan meminta konfirmasi, untuk melanjutkan, kamu harus menekan _/bayar_

![image](assets/it/24.webp)


Mohon tunggu beberapa saat agar pembayaran dapat diproses.


![image](assets/it/25.webp)


Invoice seharga 50 Sats telah dibayar, hasil yang dicapai tanpa menggunakan kamera dan fungsi pemindaian terintegrasi.


### Sats.Mobi di Grup Telegram


![image](assets/it/27.webp)


Di antara fitur yang membuat LNTipBot terkenal dan kini dibawa oleh SatsMobi ke Telegram adalah fitur yang membuat pengalaman jadi seru dan interaktif bagi para anggota grup.

Pemilik grup bisa mengundang bot ke dalam obrolan lalu menetapkan SatsMobi sebagai admin. Sejak saat itu, keseruannya dimulai, karena para anggota bisa mulai memberi tip kepada pengguna lain atas kontribusi mereka di grup.


- _/tip_ menambahkan tip dengan membalas pesan;
- _/send_ mengirim dana dengan menentukan LN Address atau username Telegram sebagai penerima;
- _/faucet_ (di menu _/advanced_) memungkinkan pembuatan serangkaian tip yang bisa diklaim oleh anggota tercepat di grup dengan mengeklik _/collect_;
- _/tipjar_ (di menu _/advanced_) membuat jenis distribusi lain yang bisa dikirim ke pengguna dalam grup.


Masing-masing perintah ini memiliki sintaks tersendiri yang dijelaskan di menu perintah utama.

Dan kalau kamu bukan pemilik grup? Tidak masalah: cukup minta pendiri grup untuk mengundang SatsMobi, tambahkan sebagai admin grup, dan kamu sudah siap!


## Tempat Penjualan (POS)


Saat SatsMobi pertama kali diluncurkan, bot ini juga menghadirkan fitur lain untuk para pengguna: **POS**. "Perangkat" ini diaktifkan dengan perintah _/pos_ atau dengan mengeklik tombol terkait di konsol kanan bawah. Pada dasarnya, POS adalah aplikasi web yang terbuka sebagai pop-up di dalam obrolan Telegram.


![image](assets/it/14.webp)


Interface menampilkan username Telegram pribadimu di kiri atas dan digunakan dengan cara yang sama seperti POS pada umumnya: cukup ketik jumlahnya di keypad. Misalnya sekarang kamu ingin menagih 21 sen euro untuk sebuah layanan. Karena SatsMobi hanya mengelola Sats secara native, tidak mudah menghitung konversinya di kepala. Untuk mempermudah, POS menampilkan euro sebagai unit akun sekaligus menunjukkan padanannya dalam Satoshi.


![image](assets/it/15.webp)

Mengklik _/OK_ akan menampilkan Invoice yang dapat ditunjukkan kepada pelanggan melalui kode QR, atau yang dapat dikirim sebagai string melalui pesan instan, sehingga dapat dibayar.

![image](assets/it/16.webp)

![image](assets/it/17.webp)


Tentu saja, POS juga tersedia di ponsel, diakses dengan cara yang sama seperti yang ditunjukkan sebelumnya.


![image](assets/it/18.webp)


Ini juga ditampilkan dengan baik pada layar ponsel:


![image](assets/it/19.webp)


## Fitur Tambahan


Ada fitur lain yang melengkapi penawaran SatsMobi Wallet yang, seperti sudah kita lihat, memperluas konsep Wallet ini melampaui sekadar menerima dan mengirim pembayaran:


- _/nostr_: untuk menghubungkan Wallet ke akun Nostr kamu sendiri agar bisa menerima zap;
- _/cashback_: menampilkan kode yang bisa kamu tunjukkan ke pedagang untuk mendapatkan cashback atas pembelian;
- _/buy_: memulai prosedur terpandu di dalam bot yang memungkinkan kamu membeli Sats dengan harga euro;
- _/activatecard_: untuk meminta aktivasi kartu debit NFC yang bisa diisi ulang lewat SatsMobi Wallet dan notifikasinya bisa diaktifkan;
- _/link_: membuat tautan untuk Zeus atau BlueWallet milikmu sendiri yang bisa digunakan sebagai remote control untuk Wallet ini.


## Kesimpulan

SatsMobi adalah Wallet yang seru dan nyaman digunakan, menghidupkan kembali pengalaman LNTipBot dengan memanfaatkan fungsi yang lebih canggih dari LNBits. Namun, penting untuk diingat bahwa **ini adalah layanan kustodian**. Karena itu, sebaiknya kamu hanya menyimpan sedikit Sats di sini, bukan menjadikannya Wallet utama untuk dana Lightning Network kamu. Ada juga batas kapasitas bawaan sebesar 500.000 Sats, dan sebaiknya tidak melewati batas tersebut.

Kalau kamu mencari Lightning Network Wallet non-kustodian, sangat disarankan untuk mempertimbangkan produk lain.


---
### Dokumentasi


- [Github](https://github.com/massmux/SatsMobiBot)
- Daftar putar demo [video](https://www.youtube.com/results?search_query=Sats.mobi)
