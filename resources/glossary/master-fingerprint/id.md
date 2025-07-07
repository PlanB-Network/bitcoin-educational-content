---
term: MASTER FINGERPRINT

---
Sidik jari 4-byte (32-bit) dari kunci pribadi utama dalam dompet _Hierarchical Deterministic_ (HD). Sidik jari ini didapatkan dengan menghitung _hash_ `SHA256` dari kunci pribadi utama, diikuti dengan hash `RIPEMD160`, sebuah proses yang disebut sebagai `HASH160` pada Bitcoin. _Master Fingerprint_ digunakan untuk mengidentifikasi sebuah dompet HD, secara independen dari jalur derivasinya, tetapi dengan mempertimbangkan ada atau tidaknya kata sandi. Ini merupakan informasi ringkas yang memungkinkan untuk merujuk pada asal dari sekumpulan kunci, tanpa mengungkapkan informasi sensitif mengenai dompet yang bersangkutan.
