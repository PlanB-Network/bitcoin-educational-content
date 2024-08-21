---
term: IP_ASN.MAP
---

File yang digunakan dalam Bitcoin Core untuk menyimpan ASMAP, yang meningkatkan pengelompokan (bucketing) alamat IP dengan mengandalkan Nomor Sistem Otonom (ASN). Alih-alih mengelompokkan koneksi keluar berdasarkan prefiks jaringan IP (/16), file ini memungkinkan untuk mendiversifikasi koneksi dengan menetapkan peta alamat IP ke ASN, yang merupakan pengenal unik untuk setiap jaringan di Internet. Ide ini bertujuan untuk meningkatkan keamanan dan topologi jaringan Bitcoin dengan mendiversifikasi koneksi untuk melindungi dari serangan tertentu (terutama serangan Erebus).