---
term: SERANGAN ULANG
---

Dalam konteks Bitcoin, serangan replay terjadi ketika sebuah transaksi yang valid pada satu Blockchain direproduksi secara jahat pada Blockchain lain yang memiliki riwayat transaksi yang sama. Dengan kata lain, sebuah transaksi yang disiarkan pada satu saluran dapat direplikasi pada saluran lain tanpa persetujuan dari pengirim transaksi pertama.


Mari kita ambil contoh hipotetis Hard Fork dari Bitcoin, yang dinamai "*BitcoinBis*". Jika Anda melakukan pembayaran dalam bitcoin untuk membeli baguette dari tukang roti di Blockchain Bitcoin yang asli, tukang roti yang sama dapat memutar ulang transaksi yang sah tersebut di *BitcoinBis* untuk mendapatkan jumlah yang sama dalam mata uang digital di Fork ini, tanpa tindakan apa pun dari Anda.


Jenis serangan ini hanya dapat terjadi pada kasus percabangan Blockchain dengan 2 rantai independen yang bertahan dari waktu ke waktu. Biasanya, ini akan terjadi pada Hard Fork. Agar serangan replay dapat dilakukan, 2 blockchain harus memiliki riwayat yang sama, dan transaksi yang diduplikasi harus menggunakan input UTXO yang dibuat dari transaksi sebelumnya yang terjadi sebelum kedua chain terpecah, atau dari transaksi sebelumnya yang telah diulang dalam serangan replay sebelumnya.


Secara umum, dalam komputasi, serangan replay terdiri dari mencegat dan menggunakan kembali data yang valid untuk menipu sebuah sistem dengan mengulang transmisi asli. Hal ini terkadang dapat menyebabkan pencurian identitas pada jaringan.


> ► *Dalam kasus serangan replay pada transaksi Bitcoin, ini kadang-kadang disebut sebagai "transaksi replay". 