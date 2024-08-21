---
term: KODE PEMBAYARAN YANG DAPAT DIGUNAKAN KEMBALI
---

Dalam BIP47, sebuah kode pembayaran yang dapat digunakan kembali adalah pengenal statis yang dihasilkan dari dompet Bitcoin yang memungkinkan untuk transaksi notifikasi dan derivasi alamat unik. Ini menghindari penggunaan kembali alamat, yang mengarah pada kehilangan privasi, tanpa harus secara manual menurunkan dan mentransmisikan alamat baru yang belum digunakan untuk setiap pembayaran. Dalam BIP47, kode pembayaran yang dapat digunakan kembali dibangun sebagai berikut:
* Byte 0 sesuai dengan versi;
* Byte 1 adalah bidang bit untuk menambahkan informasi dalam kasus penggunaan spesifik;
* Byte 2 menunjukkan paritas dari `y` dari kunci publik;
* Dari byte 3 sampai byte 34, Anda akan menemukan nilai `x` dari kunci publik;
* Dari byte 35 sampai byte 66, terdapat kode rantai yang terkait dengan kunci publik;
* Dari byte 67 sampai byte 79, terdapat padding nol.

Sebuah Bagian yang Dapat Dibaca Manusia (HRP) umumnya ditambahkan di awal kode pembayaran dan checksum di akhir, dan kemudian dikodekan dalam base58. Konstruksi kode pembayaran dengan demikian cukup mirip dengan itu dari kunci ekstensi. Berikut adalah kode pembayaran BIP47 saya sendiri dalam base58 sebagai contoh:

```text
PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qD
udE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5
```

Dalam implementasi PayNym dari BIP47, kode pembayaran juga dapat dinyatakan dalam bentuk pengenal yang terkait dengan gambar robot. Berikut adalah milik saya, sebagai contoh:

```text
+throbbingpond8B1
```

Penggunaan kode pembayaran dengan implementasi PayNym saat ini tersedia di Sparrow Wallet di PC dan di Samourai Wallet di mobile.