---
term: MASTER FINGERPRINT
---

Sebuah sidik jari 4-byte (32-bit) dari kunci privat utama dalam sebuah dompet Hierarchical Deterministic (HD). Sidik jari ini diperoleh dengan menghitung hash `SHA256` dari kunci privat utama, diikuti oleh hash `RIPEMD160`, proses yang disebut sebagai `HASH160` pada Bitcoin. Master Fingerprint digunakan untuk mengidentifikasi sebuah dompet HD, terlepas dari jalur derivasi, namun mempertimbangkan keberadaan atau ketiadaan sebuah passphrase. Ini adalah informasi ringkas yang memungkinkan untuk merujuk asal dari sebuah set kunci, tanpa mengungkapkan informasi sensitif tentang dompet tersebut.