---
term: Addr

definition: Pesan jaringan Bitcoin lama yang memungkinkan mengkomunikasikan alamat IP node yang menerima koneksi. Digantikan oleh addrv2 (BIP155) untuk mendukung format alamat yang lebih panjang.
---
Pesan jaringan yang sebelumnya digunakan pada Bitcoin untuk mengomunikasikan alamat node yang menerima koneksi yang masuk. Format lama ini memiliki batasan 128 bit per alamat, dan hanya cocok untuk alamat IPv6, IPv4, dan Tor versi 2. Dengan hadirnya protokol baru seperti Tor V3 dan kebutuhan akan skalabilitas yang lebih baik untuk protokol jaringan di masa depan, format `addr` nantinya akan digantikan oleh `addrv2`, yang muncul dalam BIP155.
