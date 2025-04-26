---
term: BIAYA TRANSAKSI

---
Biaya transaksi merupakan jumlah yang bertujuan untuk memberikan kompensasi kepada para penambang atas partisipasi mereka dalam mekanisme proof of work. Biaya ini mendorong para penambang untuk memasukkan transaksi ke dalam blok yang mereka buat. Biaya ini dihasilkan dari selisih antara jumlah total input dan jumlah total output dalam sebuah transaksi:

```text
fees = inputs - outputs
```

Biaya ini dinyatakan dalam `sats/vBytes`, yang berarti bahwa biaya tidak bergantung pada jumlah bitcoin yang dikirim, tetapi pada berat transaksi. Biaya ini dipilih secara bebas oleh pengirim transaksi dan menentukan kecepatan penyertaannya ke dalam blok melalui mekanisme lelang. Sebagai contoh, katakanlah saya melakukan transaksi dengan input sebesar `100.000 satoshi`, output sebesar `40.000 satoshi`, dan output lainnya sebesar `58.500 satoshi`. Total dari semua output tersebut adalah `98.500 sat`. Biaya yang dialokasikan untuk transaksi ini adalah `1.500 sat`. Penambang yang menyertakan transaksi saya dapat membuat `1.500 sats` dalam transaksi coinbase mereka dengan imbalan `1.500 sats` yang tidak saya dapatkan dalam output saya.

Transaksi dengan biaya yang lebih tinggi, relatif terhadap ukurannya, diperlakukan sebagai prioritas oleh para penambang, yang dapat mempercepat proses konfirmasi. Sebaliknya, transaksi dengan biaya yang lebih rendah dapat ditunda selama periode kepadatan yang tinggi. Perlu dicatat bahwa biaya transaksi Bitcoin berbeda dengan subsidi blok, yang merupakan insentif tambahan untuk penambang. Imbalan blok terdiri dari bitcoin baru yang dibuat dengan setiap blok yang ditambang (subsidi blok), dan juga biaya transaksi yang terkumpul. Walaupun subsidi blok akan berkurang seiring waktu karena batas total pasokan bitcoin, biaya transaksi akan terus memainkan peran penting dalam mendorong para penambang untuk berpartisipasi.

Pada tingkat protokol, tidak ada yang menghalangi pengguna untuk memasukkan transaksi tanpa biaya ke dalam blok. Pada kenyataannya, jenis transaksi tanpa biaya ini merupakan hal yang luar biasa. Secara default, node Bitcoin tidak meneruskan transaksi dengan biaya yang lebih rendah dari `1 sat/vBytes`. Jika ada beberapa transaksi tanpa biaya yang lolos, hal ini dikarenakan transaksi tersebut diintegrasikan secara langsung oleh penambang yang menang, tanpa melalui jaringan node. Sebagai contoh, transaksi berikut ini tidak termasuk biaya:

```text
fd456524104a6674693c29946543f8a0befccce5a352bda55ec8559fc630f5f3
```

Dalam contoh khusus ini, ini merupakan sebuah transaksi yang diprakarsai oleh direktur dari pool penambangan F2Pool. Sebagai pengguna biasa, batas bawah saat ini adalah `1 sat/vBytes`.

Penting juga untuk mempertimbangkan batas pembersihan. Selama periode kepadatan tinggi, mempool node akan membersihkan transaksi yang tertunda di bawah ambang batas tertentu, untuk menghormati batas RAM yang dialokasikan. Batas ini dapat dipilih secara bebas oleh pengguna, tetapi banyak yang membiarkan nilai default Bitcoin Core pada 300 MB. Ini dapat dimodifikasi dalam file `bitcoin.conf` dengan parameter `maxmempool`.

> ► *Dalam bahasa Inggris, kami menyebutnya sebagai "biaya transaksi".*