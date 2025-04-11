---
term: HMAC-SHA512

---
`HMAC-SHA512` adalah singkatan dari "Kode Otentikasi Pesan Berbasis Hash - Algoritma Hash Aman 512". Ini adalah algoritma kriptografi yang digunakan untuk memverifikasi integritas dan keaslian pesan yang dipertukarkan antara dua pihak. Algoritma ini menggabungkan fungsi hash kriptografi `SHA512` dengan kunci rahasia bersama untuk menghasilkan Kode Autentikasi Pesan (MAC) yang unik untuk setiap pesan.

Dalam konteks Bitcoin, penggunaan alami dari `HMAC-SHA512` sedikit diturunkan. Algoritma ini digunakan dalam proses derivasi deterministik dan hirarkis dari pohon kunci kriptografi dompet. `HMAC-SHA512` secara khusus digunakan untuk berpindah dari seed ke kunci utama, dan kemudian untuk setiap turunan dari pasangan induk ke pasangan anak. Algoritma ini juga ditemukan di dalam algoritma turunan lainnya yang bernama `PBKDF2`, yang digunakan untuk berpindah dari frasa pemulihan dan frasa sandi ke seed.