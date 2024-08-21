---
term: OP_CHECKSIGVERIFY (0XAD)
---

Melakukan operasi yang sama dengan `OP_CHECKSIG`, tetapi jika verifikasi tanda tangan gagal, skrip langsung berhenti dengan kesalahan dan transaksi menjadi tidak valid. Jika verifikasi berhasil, skrip berlanjut tanpa mendorong nilai `1` (benar) ke dalam tumpukan. Secara ringkas, `OP_CHECKSIGVERIFY` melakukan operasi `OP_CHECKSIG` diikuti oleh `OP_VERIFY`. Opcode ini dimodifikasi dalam Tapscript untuk memverifikasi tanda tangan Schnorr.