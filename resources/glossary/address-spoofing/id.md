---
term: Address SPOOFING
---

Serangan di mana aktor jahat membuat Address (atau pengenal pembayaran lainnya) yang sangat mirip dengan milik korban. Tujuannya adalah untuk mengelabui pengguna agar menyalin Address yang salah ini selama transaksi, yang mengakibatkan bitcoin dikirim ke penyerang dan bukan ke tujuan yang dimaksud.


Penyerang mengeksploitasi ketergesa-gesaan pengguna untuk menyalin Address yang salah jika dia melakukan transaksi tanpa memeriksa keakuratannya. Pada umumnya, untuk mengimplementasikan serangan ini, penyerang melakukan pembayaran dengan jumlah yang kecil ke Wallet korban untuk mengintegrasikan Address palsu ke dalam riwayat transaksinya. Serangan ini cenderung digunakan pada altcoin, dimana sudah menjadi praktik umum untuk menggunakan kembali alamat penerima yang sama, tidak seperti Bitcoin, dimana penggunaan alamat kosong untuk setiap transaksi merupakan praktik yang lebih luas. Akan tetapi, pengguna Bitcoin tidak kebal terhadap serangan ini.


Metode lain untuk menempatkan Address yang salah di depan korban adalah penggunaan perangkat lunak manajemen Wallet palsu yang meniru perangkat lunak yang sah, atau mengubah Address ketika mesin disusupi, antara waktu penyalinan dan waktu transaksi dibuat. Hal ini terkadang disebut sebagai "*penukaran Address*".


Untuk melindungi diri Anda dari berbagai metode serangan ini, penting untuk memeriksa beberapa karakter Address, terutama checksum (di bagian akhir), pada layar perangkat penandatanganan sebelum menandatangani transaksi.


> ► *Serangan ini juga kadang-kadang disebut sebagai Keracunan Address