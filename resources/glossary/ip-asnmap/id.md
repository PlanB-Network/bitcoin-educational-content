---
term: IP_ASN.MAP

---
File yang digunakan dalam Bitcoin Core untuk menyimpan ASMAP, yang meningkatkan bucketing (yaitu pengelompokan) alamat IP dengan mengandalkan Autonomous System Numbers (ASN). Alih-alih mengelompokkan koneksi keluar berdasarkan awalan jaringan IP (/16), file ini memungkinkan untuk mendiversifikasi koneksi dengan membuat peta pengalamatan IP ke ASN, yang merupakan pengidentifikasi unik untuk setiap jaringan di Internet. Idenya adalah untuk meningkatkan keamanan dan topologi jaringan Bitcoin dengan mendiversifikasi koneksi untuk melindungi dari serangan tertentu (terutama serangan Erebus).