---
term: BENIH

---
Dalam konteks spesifik dompet Bitcoin deterministik hirarkis, sebuah seed adalah sebuah informasi berukuran 512-bit yang berasal dari keacakan. Seed digunakan untuk menghasilkan satu set kunci privat, dan kunci publik yang sesuai, secara deterministik dan hirarkis untuk sebuah dompet Bitcoin. Seed sering kali disalahartikan sebagai frasa pemulihan itu sendiri. Akan tetapi, ini adalah informasi yang berbeda. Seed didapatkan dengan menerapkan fungsi `PBKDF2` pada frasa mnemonik dan kata sandi potensial.

Seed diciptakan dengan diperkenalkannya BIP32, yang mendefinisikan dasar-dasar dompet deterministik hirarkis. Dalam standar ini, ukuran seed adalah 128 bit. Hal ini memungkinkan untuk mendapatkan semua kunci dalam sebuah dompet dari sebuah informasi, tidak seperti dompet JBOK (*Just a Bunch Of Keys*), yang membutuhkan cadangan baru untuk setiap kunci yang dihasilkan. BIP39 kemudian memperkenalkan sebuah pengkodean untuk menyederhanakan pembacaan oleh manusia. Pengkodean ini dilakukan dalam bentuk sebuah frase, yang biasa disebut sebagai frase mnemonik atau frase pemulihan. Standar ini membantu untuk menghindari kesalahan dalam pencadangan seed, terutama melalui penggunaan checksum.

Secara umum, dalam kriptografi, sebuah seed adalah sebuah data acak yang digunakan sebagai titik awal untuk menghasilkan kunci kriptografi, enkripsi, atau urutan acak semu. Kualitas dan keamanan dari banyak proses kriptografi bergantung pada keacakan dan kerahasiaan seed.

> ► *Terjemahan bahasa Inggris dari "graine" adalah "biji". Dalam bahasa Prancis, banyak yang secara langsung menggunakan kata bahasa Inggris untuk merujuk pada biji*