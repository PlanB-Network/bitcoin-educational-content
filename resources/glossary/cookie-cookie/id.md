---
term: COOKIE (.COOKIE)

---
File yang digunakan untuk otentikasi RPC (*Remote Procedure Call*) di Bitcoin Core. Ketika bitcoind dimulai, ia akan menghasilkan cookie otentikasi yang unik dan menyimpannya di file ini. Klien atau skrip yang ingin berinteraksi dengan bitcoind melalui antarmuka RPC dapat menggunakan cookie ini untuk mengautentikasi dengan aman. Mekanisme ini memungkinkan komunikasi yang aman antara bitcoind dan aplikasi eksternal (seperti perangkat lunak dompet, misalnya), tanpa memerlukan pengelolaan nama pengguna dan kata sandi secara manual. File `.cookie` dibuat ulang pada setiap restart bitcoind dan dihapus setelah dimatikan.