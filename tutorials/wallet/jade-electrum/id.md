---
name: Giok - Electrum
description: Cara menggunakan Jade atau Jade Plus Anda dengan Electrum (desktop)
---

![cover](assets/cover.webp)



panduan ini diambil dari pelajaran [Lokakarya Bitcoin] (https://officinebitcoin.it/lezioni/jadeele/index.html)_



Tutorial ini dibuat dengan Jade Classic, tetapi pengoperasiannya juga berlaku bagi mereka yang memiliki Jade Plus.



Setelah menginisialisasi Jade, Anda bisa mulai menggunakannya dan-untuk melakukannya-pilih tampilan wallet.



Jade adalah perangkat yang dapat digunakan dengan beberapa wallet, atau aplikasi pendamping seperti yang ditentukan Blockstream di situsnya.



Dalam tutorial ini, Anda akan melihat langkah-langkah untuk menggunakan Electrum Wallet, melalui koneksi kabel USB.



## Transfer kunci publik



Ambil dan nyalakan Jade yang sudah Anda inisialisasi. Segera setelah Anda menyalakannya, tampilannya akan terlihat seperti ini:




![img](assets/en/32.webp)



Jika Anda memilih _Unlock Jade_, Anda akan mendapatkan menu di mana Anda harus memilih cara menghubungkan perangkat Anda ke aplikasi pendamping.



Dengan Electrum, Anda hanya dapat menghubungkan Jade melalui USB, jadi pilihlah metode ini.



Luncurkan Electrum, yang akan membuka usulan sebagai opsi default untuk membuka wallet yang terakhir digunakan.



Jika ini adalah pertama kalinya Anda menghubungkan Jade ke Electrum, pilih _Buat Dompet Baru_ lalu _Selesai_.



![img](assets/en/34.webp)



Nama wallet.



![img](assets/en/35.webp)



Pilih Wallet Standar.



![img](assets/en/36.webp)



Apabila memilih keystore, sangat penting untuk memilih _Use a hardware device_.



![img](assets/en/37.webp)



Electrum mulai memindai perangkat keras.



![img](assets/en/38.webp)



Dengan menghubungkan USB ke komputer (sudah terhubung pada sisi USB C ke Jade), perangkat keras wallet akan muncul di hadapan Anda dalam mode kunci. Jade membuka kunci dengan memasukkan enam digit PIN yang ditetapkan selama penyiapan.




![img](assets/en/39.webp)



Perangkat keras yang tidak terkunci, Electrum mendeteksi Giok. Lanjutkan dengan mengklik _Next_.



![img](assets/en/40.webp)



Pada titik ini Electrum meminta Anda untuk mengatur skrip kebijakan: pilih _Native Segwit_.



![img](assets/en/41.webp)



Fase transfer kunci publik dari wallet dari Jade ke tampilan Electrum dimulai.



Ketika ekspor kunci publik selesai, prosesnya selesai.



Watch-only sudah siap dan Electrum memperingatkan penyelesaian dengan layar berikut ini.



![img](assets/en/42.webp)



wallet benar-benar dibuat dan Anda dapat mulai menjelajahinya: Anda dapat melihat _addresses_, _wallet information_, dan-yang paling penting-Anda dapat melihat di pojok kanan bawah indikasi bahwa ini adalah perangkat Blockstream. Titik hijau di sebelah logo Blockstream menunjukkan bahwa perangkat telah dihidupkan dan terhubung dengan benar ke jaringan lokal.



![img](assets/en/43.webp)



## Transaksi penerimaan dan pengeluaran



Dari menu _Receive_ pada Electrum, generate, tuliskan sebuah `scriptPubKey` (alamat) untuk menerima dana. Selalu mulai dengan jumlah yang kecil dan lakukan uji coba penerimaan+pengeluaran.



![img](assets/en/44.webp)



Setelah menerima satss, Anda dapat memeriksa kedatangannya di menu _History_.



![img](assets/en/45.webp)



![img](assets/en/46.webp)



Setelah transaksi dikonfirmasi, Anda dapat membelanjakan UTXO ini dan menyelesaikan tes.



Biaya yang dikeluarkan adalah dengan menggunakan Jade untuk penandatanganan.



Buka menu _Send_ pada Electrum, tempelkan scriptPubKey, dan periksa dengan baik.



![img](assets/en/47.webp)



Setelah selesai, tekan _Bayar_.



Jendela transaksi akan terbuka, di mana penting untuk menetapkan biaya transaksi yang benar. Setelah Anda menyelesaikan semua pengaturan, klik _Preview_ di sudut kanan bawah.



![img](assets/en/48.webp)



Jendela transaksi menunjukkan beberapa detail penting, pertama dan terutama status: `Tidak Ditandatangani`.



Pada tahap ini Anda juga dapat melihat perintah _Sign_, yang harus Anda klik untuk membubuhkan tanda tangan dengan Jade.



![img](assets/en/49.webp)



Sekarang, dimulailah fase komunikasi antara layar wallet dan perangkat keras, di mana Electrum memperingatkan Anda untuk mengikuti petunjuk pada perangkat keras, dihidupkan dan siap untuk menandatangani.



![img](assets/en/50.webp)



**Namun, pertama-tama, Anda sebaiknya memverifikasi apa yang Anda tandatangani: semua parameter transaksi yang baru saja Anda siapkan, juga muncul di Jade** dan Anda dapat memverifikasi semuanya.



![img](assets/en/51.webp)



Untuk melanjutkan, pastikan Anda selalu menempatkan kursor pada tanda panah `→` yang mengarah ke langkah berikutnya dan jangan pernah pada tanda `X` kecuali jika Anda ingin mengakhiri operasi tanpa menyelesaikannya.



Bagian verifikasi diakhiri dengan tampilan biaya. Pada tahap ini, konfirmasi sama dengan membubuhkan tanda tangan Anda.



![img](assets/en/52.webp)



Untuk sesaat, Jade memproses operasi, setelah selesai, Jade kembali ke menu beranda.



![img](assets/en/53.webp)



Pada Electrum, Anda dapat melihat status transaksi, yang telah berubah dari `Tidak Ditandatangani` menjadi `Tanda Tangan` dan sekarang Anda dapat menyebarkannya dengan mengeklik _Broadcast_.



![img](assets/en/54.webp)



wallet, dengan demikian diuji, dapat digunakan untuk menerima UTXO yang dimaksudkan untuk penyimpanan yang aman.



![img](assets/en/55.webp)



Panduan ini adalah contoh cara menggunakan Jade Anda, yang terhubung melalui USB, ke jam tangan khusus wallet. Electrum adalah contoh klasik, tetapi Anda mungkin lebih memilih perangkat lunak wallet lainnya. Jade mengekspor kunci publik ke banyak dompet lain: temukan fungsi serupa yang Anda baca dalam tutorial ini, untuk memandu Anda dan menemukan cara menggunakannya di aplikasi pendamping favorit Anda.