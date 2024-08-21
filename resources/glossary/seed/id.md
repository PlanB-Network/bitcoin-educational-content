---
term: SEED
---

Dalam konteks spesifik dompet Bitcoin deterministik hierarkis, seed adalah potongan informasi 512-bit yang berasal dari keacakan. Ini digunakan untuk menghasilkan secara deterministik dan hierarkis sebuah set kunci privat, dan kunci publik yang bersesuaian, untuk sebuah dompet Bitcoin. Seed sering kali disalahartikan dengan frasa pemulihan itu sendiri. Namun, ini adalah informasi yang berbeda. Seed diperoleh dengan menerapkan fungsi `PBKDF2` pada frasa mnemonik dan passphrase potensial apa pun.

Seed ditemukan dengan pengenalan BIP32, yang mendefinisikan dasar-dasar dompet deterministik hierarkis. Dalam standar ini, seed adalah 128 bit. Ini memungkinkan untuk derivasi semua kunci dalam dompet dari satu potongan informasi, tidak seperti dompet JBOK (*Just a Bunch Of Keys*), yang memerlukan backup baru untuk setiap kunci yang dihasilkan. BIP39 kemudian memperkenalkan pengkodean seed ini untuk menyederhanakan pembacaannya oleh manusia. Pengkodean ini dilakukan dalam bentuk frasa, yang umumnya disebut sebagai frasa mnemonik atau frasa pemulihan. Standar ini membantu menghindari kesalahan dalam backup seed, terutama melalui penggunaan checksum.

Secara lebih umum, dalam kriptografi, seed adalah potongan data acak yang digunakan sebagai titik awal untuk menghasilkan kunci kriptografi, enkripsi, atau urutan pseudo-acak. Kualitas dan keamanan banyak proses kriptografi bergantung pada keacakan dan kerahasiaan seed.

> ► *Terjemahan bahasa Inggris dari "graine" adalah "seed". Dalam bahasa Prancis, banyak yang langsung menggunakan kata bahasa Inggris untuk merujuk pada seed.*