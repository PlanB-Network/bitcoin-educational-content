---
term: PBKDF2

---
`PBKDF2` adalah singkatan dari *Password-Based Key Derivation Function 2*, yang merupakan sebuah metode untuk membuat kunci kriptografi dari kata sandi dengan menggunakan sebuah fungsi turunan. Metode ini membutuhkan masukan berupa kata sandi, _salt_ kriptografi, dan secara berulang-ulang menerapkan fungsi yang telah ditentukan sebelumnya (biasanya berupa fungsi _hash_ seperti `SHA256` atau `HMAC`) pada data tersebut. Proses ini diulang berkali-kali untuk menghasilkan kunci kriptografi.

Dalam konteks Bitcoin, `PBKDF2` digunakan bersama dengan fungsi `HMAC-SHA512` untuk membuat _seed_ dari sebuah dompet deterministik dan hirarkis (_seed_) dari sebuah frasa pemulihan yang terdiri dari 12 atau 24 kata. _Salt_ kriptografi yang digunakan dalam kasus ini adalah frasa sandi BIP39, dan jumlah iterasi adalah `2048`.
