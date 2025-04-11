---
term: KODE PEMBAYARAN YANG DAPAT DIGUNAKAN KEMBALI

---
Dalam BIP47, kode pembayaran yang dapat digunakan kembali adalah sebuah pengenal statis yang dihasilkan dari dompet Bitcoin yang memungkinkan untuk melakukan transaksi notifikasi dan mendapatkan alamat yang unik. Hal ini untuk menghindari penggunaan ulang alamat, yang menyebabkan hilangnya privasi, tanpa harus secara manual mendapatkan dan mengirimkan alamat baru yang tidak terpakai untuk setiap pembayaran. Pada BIP47, kode pembayaran yang dapat digunakan kembali dibuat sebagai berikut:


- Byte 0 sesuai dengan versi;
- Byte 1 adalah bidang bit untuk menambahkan informasi dalam kasus penggunaan tertentu;
- Byte 2 menunjukkan paritas `y` dari kunci publik;
- Dari byte 3 hingga byte 34, Anda akan menemukan nilai `x` dari kunci publik;
- Dari byte 35 hingga byte 66, terdapat kode rantai yang terkait dengan kunci publik;
- Dari byte 67 hingga byte 79, tidak ada padding.

Bagian yang Dapat Dibaca Manusia (HRP) biasanya ditambahkan di awal kode pembayaran dan checksum di bagian akhir, dan kemudian dikodekan dalam base58. Dengan demikian, konstruksi kode pembayaran sangat mirip dengan kunci yang diperluas. Berikut ini adalah kode pembayaran BIP47 saya sendiri dalam base58 sebagai contoh:

```text
PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qD
udE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5
```

Dalam implementasi PayNym pada BIP47, kode pembayaran juga dapat diekspresikan dalam bentuk pengenal yang terkait dengan gambar robot. Ini milik saya, sebagai contoh:

```text
+throbbingpond8B1
```

Penggunaan kode pembayaran dengan implementasi PayNym saat ini tersedia di Sparrow Wallet di PC dan Samourai Wallet di ponsel.