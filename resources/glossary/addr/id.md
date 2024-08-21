---
term: ADDR
---

Pesan jaringan yang dahulu digunakan pada Bitcoin untuk mengkomunikasikan alamat-alamat node yang menerima koneksi masuk. Format lama ini, yang terbatas pada 128 bit per alamat, hanya cocok untuk alamat IPv6, IPv4, dan versi 2 Tor. Dengan kedatangan protokol baru seperti Tor V3 dan kebutuhan akan skalabilitas yang lebih baik untuk protokol jaringan masa depan, format `addr` digantikan oleh `addrv2`, yang diperkenalkan dalam BIP155.