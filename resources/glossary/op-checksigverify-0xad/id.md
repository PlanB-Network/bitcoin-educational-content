---
term: OP_CHECKSIGVERIFY (0XAD)

---
Melakukan operasi yang sama dengan `OP_CHECKSIG`, tetapi jika verifikasi tanda tangan gagal, skrip akan segera berhenti dengan kesalahan dan transaksi menjadi tidak valid. Jika verifikasi berhasil, skrip akan berlanjut tanpa memasukkan nilai `1` (true) ke dalam stack. Singkatnya, `OP_CHECKSIGVERIFY` melakukan operasi `OP_CHECKSIG` diikuti oleh `OP_VERIFY`. Opcode ini dimodifikasi dalam Tapscript untuk memverifikasi tanda tangan Schnorr.