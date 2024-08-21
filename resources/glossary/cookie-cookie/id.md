---
term: COOKIE (.COOKIE)
---

File yang digunakan untuk autentikasi RPC (*Remote Procedure Call*) di Bitcoin Core. Ketika bitcoind dimulai, ia menghasilkan cookie autentikasi unik dan menyimpannya dalam file ini. Klien atau skrip yang ingin berinteraksi dengan bitcoind melalui antarmuka RPC dapat menggunakan cookie ini untuk autentikasi secara aman. Mekanisme ini memungkinkan komunikasi yang aman antara bitcoind dan aplikasi eksternal (seperti perangkat lunak dompet, misalnya), tanpa memerlukan pengelolaan manual nama pengguna dan kata sandi. File `.cookie` dihasilkan ulang setiap kali bitcoind di-restart dan dihapus saat shutdown.