---
term: ADDR

---
Pesan jaringan yang sebelumnya digunakan pada Bitcoin untuk mengomunikasikan alamat node yang menerima koneksi yang masuk. Format lama ini, yang terbatas pada 128 bit per alamat, hanya cocok untuk alamat IPv6, IPv4, dan Tor versi 2. Dengan hadirnya protokol baru seperti Tor V3 dan kebutuhan akan skalabilitas yang lebih baik untuk protokol jaringan di masa depan, format `addr` digantikan oleh `addrv2`, yang diperkenalkan di BIP155.