---
term: IP_ASN.MAP

---
File yang digunakan dalam Bitcoin Core untuk menyimpan ASMAP, yang meningkatkan _bucketing_ (atau pengelompokan) alamat IP dengan mengandalkan _Autonomous System Numbers_ (ASN). Alih-alih mengelompokkan koneksi keluar berdasarkan awalan jaringan IP (/16), file ini memungkinkan untuk mendiversifikasi koneksi dengan membuat peta pengalamatan IP ke ASN, yang merupakan pengidentifikasi unik untuk setiap jaringan di Internet. Konsepnya adalah untuk meningkatkan keamanan dan topologi jaringan Bitcoin dengan mendiversifikasi koneksi untuk melindungi dari serangan tertentu (terutama serangan Erebus).
