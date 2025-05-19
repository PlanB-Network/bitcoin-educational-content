---
term: GRAIN
---

Dalam konteks spesifik portofolio deterministik hirarkis Bitcoin, sebuah seed adalah sebuah informasi 512-bit yang berasal dari sebuah peristiwa acak. Ini digunakan untuk secara deterministik dan hirarkis generate satu set kunci privat, dan kunci publik yang sesuai, untuk portofolio Bitcoin. seed sering kali dikacaukan dengan frasa pemulihan itu sendiri. Akan tetapi, ini bukanlah hal yang sama. seed didapatkan dengan menerapkan fungsi `PBKDF2` pada frasa Mnemonic dan passphrase.


seed diciptakan dengan BIP32, yang mendefinisikan dasar-dasar portofolio deterministik hirarkis. Dalam standar ini, seed berukuran 128 bit. Hal ini memungkinkan semua kunci dalam portofolio berasal dari satu informasi, tidak seperti portofolio JBOK (*Just a Bunch Of Keys*), yang membutuhkan cadangan baru untuk setiap kunci yang dihasilkan. BIP39 kemudian mengusulkan pengkodean seed ini, untuk menyederhanakan pembacaannya oleh manusia. Pengkodean ini berbentuk sebuah frasa, yang secara umum disebut sebagai frasa Mnemonic atau frasa pemulihan. Standar ini menghindari kesalahan ketika menyimpan seed, khususnya berkat penggunaan checksum.


Di luar konteks Bitcoin, dalam kriptografi secara umum, seed adalah nilai awal yang digunakan untuk kunci kriptografi generate, atau lebih luas lagi, semua jenis data yang dihasilkan oleh generator bilangan acak semu. Nilai awal ini haruslah acak dan tidak dapat diprediksi untuk menjamin keamanan sistem kriptografi. Memang, seed memperkenalkan entropi ke dalam sistem, tetapi proses pembangkitan yang mengikutinya bersifat deterministik.


> ► *Dalam bahasa umum, mayoritas pengguna bitcoin mengacu pada frasa Mnemonic ketika mereka berbicara tentang "seed", dan bukan pada kondisi turunan antara yang berada di antara frasa Mnemonic dan kunci utama*