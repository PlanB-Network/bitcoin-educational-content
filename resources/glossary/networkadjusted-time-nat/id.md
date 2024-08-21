---
term: NETWORK-ADJUSTED TIME (NAT)
---

Estimasi waktu universal yang ditetapkan pada jam dari node jaringan. Setiap node menghitung NAT-nya dengan mengambil median dari perbedaan waktu antara jam lokalnya (UTC) dan jam dari node yang terhubung dengannya, kemudian menambahkan jam lokalnya ke median dari perbedaan-perbedaan ini, hingga maksimum 70 menit. Waktu yang disesuaikan jaringan ini oleh karena itu adalah median dari waktu node yang dihitung secara lokal oleh setiap node. Bingkai acuan ini kemudian digunakan untuk memverifikasi validitas dari timestamp blok. Memang, agar sebuah blok diterima oleh sebuah node, timestamp-nya harus berada di antara MTP (median waktu dari 11 blok yang ditambang terakhir) dan NAT ditambah 2 jam:

```text
MTP < Valid Timestamp < (NAT + 2h)
```