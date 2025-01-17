---
term: INDEKS (NOMOR KUNCI)

---
Dalam konteks HD wallet, indeks ini merujuk pada nomor urut yang diberikan kepada child key yang dihasilkan dari parent key. Indeks ini digunakan bersama dengan kunci induk dan kode rantai induk untuk mendapatkan kunci anak yang unik secara deterministik. Hal ini memungkinkan untuk organisasi yang terstruktur dan pembuatan beberapa pasangan kunci anak yang dapat direproduksi dari kunci induk yang sama. Ini adalah bilangan bulat 32-bit yang digunakan dalam fungsi penurunan `HMAC-SHA512`. Dengan demikian, angka ini membedakan kunci anak kandung dalam sebuah dompet HD.