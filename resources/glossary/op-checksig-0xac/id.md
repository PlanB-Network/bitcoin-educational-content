---
term: OP_CHECKSIG (0XAC)

---
_Opcode_ untuk verifikasi keabsahan tanda tangan terhadap kunci publik yang diberikan. Proses ini mengambil dua elemen teratas dari _stack_: tanda tangan dan kunci publik, dan mengevaluasi apakah tanda tangan tersebut benar berhubungan dengan _hash_ transaksi dan kunci publik yang ditentukan. Jika verifikasi berhasil, maka ia akan memasukkan nilai `1` (benar) ke dalam _stack_, jika tidak, maka nilai `0` (salah) akan didorong ke dalam _stack_. Opcode ini dimodifikasi dalam Tapscript untuk memverifikasi tanda tangan Schnorr.
