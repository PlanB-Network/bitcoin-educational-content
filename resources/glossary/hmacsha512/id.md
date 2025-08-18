---
term: HMAC-SHA512

---
`HMAC-SHA512` adalah singkatan dari "_Hash-based Message Authentication Code - Secure Hash Algorithm 512_", dapat diterjemahkan ke bahasa Indonesia sebgai "Kode Otentikasi Pesan Berbasis Hash - Algoritma Hash Aman 512", yang merupakan algoritma kriptografi yang digunakan untuk memverifikasi integritas dan keaslian pesan yang dipertukarkan antara dua pihak. Algoritma ini menggabungkan fungsi _hash_ kriptografi `SHA512` dengan kunci rahasia bersama untuk menghasilkan Kode Otentikasi Pesan (_Message Authentication Code_) yang unik untuk setiap pesan.

Dalam konteks Bitcoin, terdapat sedikit turunan dari `HMAC-SHA512` yang digunakan. Algoritma ini digunakan dalam proses derivasi deterministik dan hirarkis dari pohon kunci kriptografi dompet. `HMAC-SHA512` secara khusus digunakan untuk berpindah dari _seed_ ke kunci utama, dan kemudian untuk setiap turunan dari pasangan induk ke pasangan anak. Algoritma ini juga ditemukan di dalam algoritma turunan lainnya yang bernama `PBKDF2`, yang digunakan untuk berpindah dari frasa pemulihan dan _passphrase_ ke _seed_.
