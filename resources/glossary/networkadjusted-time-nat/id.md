---
term: WAKTU YANG DISESUAIKAN DENGAN JARINGAN (NAT)

---
Estimasi waktu universal yang dibuat berdasarkan jam dari node jaringan. Setiap node menghitung NAT-nya dengan mengambil median dari perbedaan waktu antara jam lokalnya (UTC) dan node yang terhubung dengannya, kemudian menambahkan jam lokalnya ke median perbedaan ini, hingga maksimum 70 menit. Oleh karena itu, waktu yang disesuaikan dengan jaringan adalah median dari waktu node yang dihitung secara lokal oleh setiap node. Kerangka referensi ini kemudian digunakan untuk memverifikasi validitas stempel waktu blok. Memang, agar sebuah blok dapat diterima oleh sebuah node, stempel waktunya harus berada di antara MTP (waktu rata-rata dari 11 blok terakhir yang ditambang) dan NAT ditambah 2 jam:

```text
MTP < Valid Timestamp < (NAT + 2h)
```