---
term: BIAYA TRANSAKSI
---

Biaya transaksi merupakan jumlah yang bertujuan untuk mengkompensasi para penambang atas partisipasi mereka dalam mekanisme proof of work. Biaya ini mendorong penambang untuk memasukkan transaksi dalam blok yang mereka buat. Biaya ini merupakan hasil dari perbedaan antara jumlah total input dan jumlah total output dalam sebuah transaksi:

```text
biaya = input - output
```

Biaya ini dinyatakan dalam `sats/vBytes`, artinya biaya tidak bergantung pada jumlah bitcoin yang dikirim, tetapi pada berat transaksi. Biaya ini dipilih secara bebas oleh pengirim transaksi dan menentukan kecepatan inklusi transaksi dalam blok melalui mekanisme lelang. Sebagai contoh, katakanlah saya melakukan transaksi dengan input `100,000 sats`, output `40,000 sats`, dan output lainnya `58,500 sats`. Total output adalah `98,500 sats`. Biaya yang dialokasikan untuk transaksi ini adalah `1,500 sats`. Penambang yang memasukkan transaksi saya dapat menciptakan `1,500 sats` dalam transaksi coinbase mereka sebagai imbalan untuk `1,500 sats` yang tidak saya dapatkan kembali dalam output saya.

Transaksi dengan biaya lebih tinggi, relatif terhadap ukurannya, dianggap sebagai prioritas oleh penambang, yang dapat mempercepat proses konfirmasi. Sebaliknya, transaksi dengan biaya lebih rendah mungkin mengalami penundaan selama periode kemacetan tinggi. Penting untuk dicatat bahwa biaya transaksi Bitcoin berbeda dari subsidi blok, yang merupakan insentif tambahan untuk penambang. Hadiah blok terdiri dari bitcoin baru yang diciptakan dengan setiap blok yang ditambang (subsidi blok), serta biaya transaksi yang dikumpulkan. Meskipun subsidi blok berkurang seiring waktu karena batas pasokan total bitcoin, biaya transaksi akan terus memainkan peran penting dalam mendorong penambang untuk berpartisipasi.

Di tingkat protokol, tidak ada yang mencegah pengguna untuk memasukkan transaksi tanpa biaya dalam sebuah blok. Dalam kenyataannya, jenis transaksi tanpa biaya ini adalah pengecualian. Secara default, node Bitcoin tidak meneruskan transaksi dengan biaya lebih rendah dari `1 sat/vBytes`. Jika beberapa transaksi tanpa biaya telah lolos, itu karena mereka langsung diintegrasikan oleh penambang pemenang, tanpa melewati jaringan node. Sebagai contoh, transaksi berikut ini tidak mencakup biaya:

```text
fd456524104a6674693c29946543f8a0befccce5a352bda55ec8559fc630f5f3
```

Dalam contoh spesifik ini, itu adalah transaksi yang diinisiasi oleh direktur kolam penambangan F2Pool. Sebagai pengguna reguler, batas bawah saat ini adalah `1 sat/vBytes`.
Juga perlu mempertimbangkan batasan penghapusan. Selama periode kemacetan tinggi, mempool dari node menghapus transaksi tertunda mereka di bawah ambang tertentu, untuk menghormati batas RAM yang dialokasikan. Batas ini dipilih secara bebas oleh pengguna, tetapi banyak yang meninggalkan nilai default Bitcoin Core di 300 MB. Ini dapat dimodifikasi dalam file `bitcoin.conf` dengan parameter `maxmempool`.
> ► *Dalam bahasa Inggris, kami menyebutnya "transaction fees".*