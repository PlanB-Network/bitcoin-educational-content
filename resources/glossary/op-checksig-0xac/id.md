---
term: OP_CHECKSIG (0XAC)
---

Memverifikasi keabsahan sebuah tanda tangan terhadap kunci publik yang diberikan. Ini mengambil dua elemen teratas dari tumpukan: tanda tangan dan kunci publik, dan mengevaluasi apakah tanda tangan tersebut benar untuk hash transaksi dan kunci publik yang ditentukan. Jika verifikasi berhasil, ini mendorong nilai `1` (benar) ke dalam tumpukan, jika tidak maka `0` (salah). Opcode ini dimodifikasi dalam Tapscript untuk memverifikasi tanda tangan Schnorr.