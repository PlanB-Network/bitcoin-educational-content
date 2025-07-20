---
term: SEED
---

Dalam konteks spesifik portofolio deterministik hirarkis Bitcoin, sebuah _seed_ adalah sebuah informasi 512-bit yang berasal dari sebuah peristiwa acak. Ini digunakan untuk secara deterministik dan hirarkis melakukan generasi satu set kunci privat, dan kunci publik yang bersangkutan, untuk portofolio Bitcoin. _Seed_ sering kali dikacaukan dengan frasa pemulihan itu sendiri padahal keduanya bukanlah hal yang sama. _Seed_ didapatkan dengan menerapkan fungsi `PBKDF2` pada frasa _mnemonic_ dan _passphrase_.


_Seed_ diciptakan dengan BIP32, yang mendefinisikan dasar-dasar portofolio deterministik hirarkis. Dalam standar ini, seed berukuran 128 bit. Hal ini memungkinkan semua kunci dalam portofolio berasal dari satu informasi, tidak seperti portofolio JBOK (*Just a Bunch Of Keys*), yang membutuhkan cadangan baru untuk setiap kunci yang dihasilkan. BIP39 kemudian mengusulkan pengkodean _seed_ ini, untuk menyederhanakan pembacaannya oleh manusia. Pengkodean ini berbentuk sebuah frasa, yang secara umum disebut sebagai frasa _mnemonic_ atau frasa pemulihan. Standar ini menghindari kesalahan ketika menyimpan _seed_, khususnya berkat penggunaan _checksum_.


Di luar konteks Bitcoin, dalam kriptografi secara umum, _seed_ adalah nilai awal yang digunakan untuk kunci kriptografi untuk generasi kunci, atau lebih luas lagi, semua jenis data yang dihasilkan oleh generator bilangan _pseudo-random_. Nilai awal ini haruslah acak dan tidak dapat diprediksi untuk menjamin keamanan sistem kriptografi. Memang, _seed_ memperkenalkan entropi ke dalam sistem, tetapi proses pembangkitan yang mengikutinya bersifat deterministik.


> ► *Dalam bahasa umum, mayoritas pengguna bitcoin mengacu pada frasa mnemonic ketika mereka berbicara tentang "seed", dan bukan pada kondisi turunan antara yang berada di antara frasa mnemonic dan kunci utama*
