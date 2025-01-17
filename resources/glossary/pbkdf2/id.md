---
term: PBKDF2

---
`PBKDF2` adalah singkatan dari *Fungsi Derivasi Kunci Berbasis Kata Sandi 2*. Ini adalah sebuah metode untuk membuat kunci kriptografi dari kata sandi dengan menggunakan sebuah fungsi turunan. Metode ini membutuhkan masukan berupa kata sandi, garam kriptografi, dan secara berulang-ulang menerapkan fungsi yang telah ditentukan sebelumnya (biasanya berupa fungsi hash seperti `SHA256` atau `HMAC`) pada data tersebut. Proses ini diulang berkali-kali untuk menghasilkan kunci kriptografi.

Dalam konteks Bitcoin, `PBKDF2` digunakan bersama dengan fungsi `HMAC-SHA512` untuk membuat seed dari sebuah dompet deterministik dan hirarkis (seed) dari sebuah frasa pemulihan yang terdiri dari 12 atau 24 kata. Salt kriptografi yang digunakan dalam kasus ini adalah frasa sandi BIP39, dan jumlah iterasi adalah `2048`.