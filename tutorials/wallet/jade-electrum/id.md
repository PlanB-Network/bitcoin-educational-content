---
name: Jade - Electrum
description: Cara menggunakan Jade atau Jade Plus Anda dengan Electrum (desktop)
---

![cover](assets/cover.webp)



panduan ini diambil dari pelajaran [Lokakarya Bitcoin](https://officinebitcoin.it/lezioni/jadeele/index.html)_



Tutorial ini dibuat dengan Jade Classic, tetapi pengoperasiannya juga berlaku bagi kamu yang memiliki Jade Plus.



Setelah menginisialisasi Jade, kamu bisa mulai menggunakannya dan untuk melakukannya pilih tampilan wallet.



Jade adalah perangkat yang dapat digunakan dengan beberapa wallet, atau aplikasi pendamping seperti yang dijelaskan Blockstream di situsnya.



Dalam tutorial ini, kamu akan melihat langkah-langkah untuk menggunakan Electrum Wallet melalui koneksi kabel USB.



## Transfer kunci publik



Ambil dan nyalakan Jade yang sudah kamu inisialisasi. Segera setelah kamu menyalakannya, tampilannya akan terlihat seperti ini:




![img](assets/en/32.webp)



Jika kamu memilih _Unlock Jade_, kamu akan masuk ke menu di mana kamu harus memilih cara menghubungkan perangkat kamu ke aplikasi pendamping.



Dengan Electrum, kamu hanya bisa menghubungkan Jade melalui USB, jadi pilih metode ini.



Luncurkan Electrum, yang akan menampilkan opsi default untuk membuka wallet yang terakhir digunakan.



Jika ini pertama kalinya kamu menghubungkan Jade ke Electrum, pilih _Buat Dompet Baru_ lalu _Selesai_.


![img](assets/en/34.webp)



Nama wallet.



![img](assets/en/35.webp)



Pilih Wallet Standar.



![img](assets/en/36.webp)



Apabila memilih keystore, sangat penting untuk memilih _Use a hardware device_.



![img](assets/en/37.webp)



Electrum mulai memindai perangkat keras.



![img](assets/en/38.webp)



Dengan menghubungkan USB ke komputer (sudah terhubung pada sisi USB C ke Jade), hardware wallet akan muncul di hadapan kamu dalam mode terkunci. Buka kunci Jade dengan memasukkan enam digit PIN yang ditetapkan selama penyiapan.




![img](assets/en/39.webp)



Perangkat keras yang tidak terkunci, Electrum mendeteksi Jade. Lanjutkan dengan mengklik _Next_.



![img](assets/en/40.webp)



Pada titik ini Electrum memintamu untuk mengatur skrip kebijakan: pilih _Native Segwit_.



![img](assets/en/41.webp)



Fase transfer kunci publik dari wallet dari Jade ke tampilan Electrum dimulai.



Ketika ekspor kunci publik selesai, prosesnya selesai.



Watch-only sudah siap dan Electrum memperingatkan penyelesaian dengan layar berikut ini.



![img](assets/en/42.webp)



Wallet benar-benar dibuat dan kamu bisa mulai menjelajahinya: kamu dapat melihat _addresses_, _wallet information_, dan yang paling penting kamu dapat melihat di pojok kanan bawah indikasi bahwa ini adalah perangkat Blockstream. Titik hijau di sebelah logo Blockstream menunjukkan bahwa perangkat telah dihidupkan dan terhubung dengan benar ke jaringan lokal.



![img](assets/en/43.webp)



## Transaksi penerimaan dan pengeluaran



Dari menu _Receive_ pada Electrum, generate lalu catat sebuah `scriptPubKey` (alamat) untuk menerima dana. Selalu mulai dengan jumlah kecil dan lakukan uji coba penerimaan+pengeluaran.



![img](assets/en/44.webp)



Setelah menerima sats, Kamu dapat memeriksa kedatangannya di menu _History_.



![img](assets/en/45.webp)



![img](assets/en/46.webp)



Setelah transaksi dikonfirmasi, kamu dapat membelanjakan UTXO ini dan menyelesaikan tes.



Biaya yang dikeluarkan dilakukan dengan menggunakan Jade untuk penandatanganan.



Buka menu _Send_ pada Electrum, tempelkan scriptPubKey, dan periksa dengan baik.



![img](assets/en/47.webp)



Setelah selesai, tekan _Bayar_.



Jendela transaksi akan terbuka, di mana penting untuk menetapkan biaya transaksi yang benar. Setelah kamu menyelesaikan semua pengaturan, klik _Preview_ di sudut kanan bawah.



![img](assets/en/48.webp)



Jendela transaksi menunjukkan beberapa detail penting, pertama dan terutama status: `Tidak Ditandatangani`.



Pada tahap ini kamu juga dapat melihat perintah _Sign_, yang harus kamu klik untuk membubuhkan tanda tangan dengan Jade.



![img](assets/en/49.webp)



Sekarang, dimulailah fase komunikasi antara layar wallet dan hardware wallet, di mana Electrum memperingatkan kamu untuk mengikuti petunjuk pada hardware wallet yang sudah dinyalakan dan siap untuk menandatangani.



![img](assets/en/50.webp)



**Namun, pertama-tama, kamu sebaiknya memverifikasi apa yang kamu tandatangani: semua parameter transaksi yang baru saja kamu siapkan juga muncul di Jade dan kamu dapat memverifikasi semuanya.**



![img](assets/en/51.webp)



Untuk melanjutkan, pastikan kamu selalu menempatkan kursor pada tanda panah `→` yang mengarah ke langkah berikutnya dan jangan pernah pada tanda `X` kecuali jika kamu ingin mengakhiri operasi tanpa menyelesaikannya.



Bagian verifikasi diakhiri dengan tampilan biaya. Pada tahap ini, konfirmasi sama dengan membubuhkan tanda tangan kamu.


![img](assets/en/52.webp)



Untuk sesaat, Jade memproses operasi, setelah selesai, Jade kembali ke menu beranda.



![img](assets/en/53.webp)



Pada Electrum, kamu dapat melihat status transaksi, yang telah berubah dari `Tidak Ditandatangani` menjadi `Tanda Tangan` dan sekarang kamu dapat menyebarkannya dengan mengeklik _Broadcast_.



![img](assets/en/54.webp)



wallet, dengan demikian diuji, dapat digunakan untuk menerima UTXO yang dimaksudkan untuk penyimpanan yang aman.



![img](assets/en/55.webp)



Panduan ini adalah contoh cara menggunakan Jade kamu, yang terhubung melalui USB, ke wallet khusus. Electrum adalah contoh klasik, tetapi kamu mungkin lebih memilih perangkat lunak wallet lainnya. Jade mengekspor kunci publik ke banyak wallet lain: temukan fungsi serupa yang kamu baca dalam tutorial ini untuk memandu kamu dan menemukan cara menggunakannya di aplikasi pendamping favorit kamu.
