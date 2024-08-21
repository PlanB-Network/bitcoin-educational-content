---
term: STONEWALL
---

Sebuah bentuk transaksi Bitcoin tertentu yang bertujuan untuk meningkatkan privasi pengguna selama melakukan pembayaran dengan meniru coinjoin antara dua orang, tanpa benar-benar menjadi satu. Memang, transaksi ini tidak bersifat kolaboratif. Seorang pengguna dapat membangunnya sendiri, hanya melibatkan UTXO milik mereka sendiri sebagai input. Oleh karena itu, Anda dapat membuat transaksi Stonewall untuk setiap kesempatan, tanpa perlu sinkronisasi dengan pengguna lain.

Operasi dari transaksi Stonewall adalah sebagai berikut: pada input transaksi, pengirim menggunakan 2 UTXO yang milik mereka. Transaksi kemudian menghasilkan 4 output, 2 di antaranya akan berjumlah sama persis. 2 lainnya akan merupakan kembalian. Di antara 2 output dengan jumlah yang sama, hanya satu yang sebenarnya akan pergi ke penerima pembayaran.

Dengan demikian, hanya ada 2 peran dalam transaksi Stonewall:
* Pengirim, yang melakukan pembayaran sebenarnya;
* Penerima, yang mungkin tidak menyadari sifat khusus dari transaksi dan hanya menunggu pembayaran dari pengirim.

![](../../dictionnaire/assets/33.png)
Transaksi Stonewall tersedia baik pada aplikasi Samourai Wallet maupun perangkat lunak Sparrow Wallet.

Struktur Stonewall menambahkan banyak entropi ke transaksi dan menyamarkan jejak untuk analisis rantai. Dari luar, transaksi seperti itu dapat diinterpretasikan sebagai coinjoin kecil antara dua orang. Namun pada kenyataannya, sama seperti transaksi Stonewall x2, ini adalah pembayaran. Metode ini dengan demikian menghasilkan ketidakpastian dalam analisis rantai, atau bahkan mengarah ke jejak palsu. Meskipun pengamat eksternal berhasil mengidentifikasi pola transaksi Stonewall, mereka tidak akan memiliki semua informasi. Mereka tidak akan dapat menentukan mana dari dua UTXO dengan jumlah yang sama yang sesuai dengan pembayaran. Lebih lanjut, mereka tidak akan dapat menentukan apakah dua UTXO pada input berasal dari dua orang yang berbeda atau jika mereka milik satu orang yang menggabungkannya. Poin terakhir ini disebabkan oleh fakta bahwa transaksi Stonewall x2 mengikuti pola yang sama persis dengan transaksi Stonewall. Dari luar dan tanpa informasi konteks tambahan, mustahil untuk membedakan transaksi Stonewall dari transaksi Stonewall x2. Namun, yang pertama bukanlah transaksi kolaboratif, sementara yang terakhir adalah. Ini menambahkan lebih banyak keraguan tentang pengeluaran ini.