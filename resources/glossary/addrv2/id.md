---
term: Addrv2

definition: Format pesan jaringan baru (BIP155) yang memungkinkan penyiaran alamat node Bitcoin. Mendukung alamat yang lebih panjang seperti Tor v3 atau I2P.
---
Perubahan yang diusulkan dalam BIP155 untuk pesan `addr` pada jaringan Bitcoin. Pesan `addr` digunakan untuk mengumumkan alamat _node_ yang menerima koneksi yang masuk, tetapi hanya terbatas untuk alamat 128-bit. Ukuran ini cukup untuk alamat IPv6, IPv4, dan Tor V2, tetapi tidak cukup untuk protokol lainnya. Versi terbaru `addrv2` dirancang untuk mendukung alamat yang lebih panjang, termasuk layanan tersembunyi Tor v3 256-bit, serta protokol jaringan lain seperti I2P atau protokol di masa depan.
