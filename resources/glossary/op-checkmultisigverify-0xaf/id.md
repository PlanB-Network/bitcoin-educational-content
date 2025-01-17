---
term: OP_CHECKMULTISIGVERIFY (0XAF)

---
Menggabungkan `OP_CHECKMULTISIG` dan `OP_VERIFY`. Dibutuhkan beberapa tanda tangan dan kunci publik untuk memverifikasi bahwa tanda tangan `M` dari tanda tangan `N` adalah valid, seperti halnya `OP_CHECKMULTISIG`. Kemudian, seperti `OP_VERIFY`, jika verifikasi gagal, skrip akan segera berhenti dengan sebuah kesalahan. Jika verifikasi berhasil, skrip akan berlanjut tanpa memasukkan nilai apa pun ke dalam stack. Opcode ini telah dihapus di Tapscript.