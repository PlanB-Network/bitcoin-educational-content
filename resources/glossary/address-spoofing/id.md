---
term: Address spoofing

definition: Serangan di mana aktor jahat membuat alamat yang sangat mirip dengan alamat korban untuk menipu mereka dan mengalihkan pembayaran mereka.
---

Serangan di mana aktor jahat membuat alamat (atau aspek pembayaran lainnya) yang sangat mirip dengan milik korban. Tujuannya adalah untuk mengelabui pengguna agar menyalin alamat yang salah ini selama transaksi, yang mengakibatkan bitcoin terkirim ke pihak penjahat dan bukan ke tujuan yang sebenarnya.


Penyerang mengeksploitasi situasi mendesak pengguna untuk menyalin alamat yang salah jika dia melakukan transaksi tanpa memeriksa keakuratannya. Pada umumnya, untuk mengimplementasikan serangan ini, penyerang melakukan pembayaran dengan jumlah yang kecil ke dompet korban untuk mengintegrasikan alamat palsu ke dalam riwayat transaksinya. Serangan ini lebih sering digunakan pada saat transaksi _altcoin_, dimana penggunaan ulang alamat penerima yang sama sudah menjadi praktik umum, tidak seperti Bitcoin, dimana penggunaan alamat kosong untuk setiap transaksi merupakan praktik yang lebih umum. Akan tetapi, pengguna Bitcoin masih bisa terkena serangan ini.



Metode lain untuk menampilkan alamat yang salah kepada korban adalah penggunaan perangkat lunak pengelolaan dompet palsu yang meniru perangkat lunak sah, atau pengubahan alamat ketika sebuah mesin telah dikompromikan, antara saat alamat tersebut disalin dan saat transaksi dibangun. Hal ini kadang-kadang disebut sebagai '"*address swapping*"'.



Untuk melindungi diri Anda dari berbagai metode serangan ini, penting untuk memeriksa beberapa karakter alamat, terutama _checksum_ (di bagian akhir), pada layar perangkat dompet sebelum menandatangani transaksi.



Serangan ini juga kadang-kadang disebut sebagai '"*address poisoning*"'.
