---
term: SERANGAN REPLAY
---

Dalam konteks Bitcoin, serangan _replay_ terjadi ketika sebuah transaksi yang valid pada satu _blockchain_ direproduksi secara jahat pada _blockchain_ lain yang memiliki riwayat transaksi yang sama. Dengan kata lain, sebuah transaksi yang disiarkan pada satu saluran dapat direplikasi pada saluran lain tanpa persetujuan dari pengirim transaksi pertama.


Mari kita ambil contoh hipotetis _Hard Fork_ dari Bitcoin, yang dinamai "*BitcoinBis*". Jika Anda melakukan pembayaran dalam bitcoin untuk membeli _baguette_ dari tukang roti di _blockchain_ Bitcoin yang asli, tukang roti yang sama dapat memutar ulang transaksi yang sah tersebut di *BitcoinBis* untuk mendapatkan jumlah yang sama dalam mata uang digital di _Fork_ ini, tanpa tindakan apa pun dari Anda.


Jenis serangan ini hanya dapat terjadi pada kasus percabangan _blockchain_ dengan 2 rantai independen yang bertahan dari waktu ke waktu. Biasanya, ini akan terjadi pada _Hard Fork_. Agar serangan _replay_ dapat dilakukan, 2 _blockchain_ harus memiliki riwayat yang sama, dan transaksi yang diduplikasi harus menggunakan input UTXO yang dibuat dari transaksi sebelumnya yang terjadi sebelum kedua rantai terpecah, atau dari transaksi sebelumnya yang telah diulang dalam serangan _replay_ sebelumnya.


Secara umum, dalam komputasi, serangan _replay_ terdiri dari pencegatan dan penggunaan kembali data yang valid untuk menipu sebuah sistem dengan mengulang transmisi asli. Hal ini terkadang dapat menyebabkan pencurian identitas pada jaringan.
