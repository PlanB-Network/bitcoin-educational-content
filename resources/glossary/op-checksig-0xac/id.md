---
term: OP_CHECKSIG (0XAC)

---
Memverifikasi keabsahan tanda tangan terhadap kunci publik yang diberikan. Proses ini mengambil dua elemen teratas dari tumpukan: tanda tangan dan kunci publik, dan mengevaluasi apakah tanda tangan tersebut benar untuk hash transaksi dan kunci publik yang ditentukan. Jika verifikasi berhasil, maka ia akan memasukkan nilai `1` (benar) ke dalam stack, jika tidak, maka `0` (salah). Opcode ini dimodifikasi dalam Tapscript untuk memverifikasi tanda tangan Schnorr.