---
term: OP_CHECKMULTISIGVERIFY (0XAF)

---
Menggabungkan `OP_CHECKMULTISIG` dan `OP_VERIFY`. Dibutuhkan beberapa tanda tangan dan kunci publik untuk memverifikasi bahwa tanda tangan `M` dari tanda tangan `N` valid, seperti halnya `OP_CHECKMULTISIG`. Kemudian, seperti `OP_VERIFY`, jika verifikasi gagal, skrip akan segera berhenti dengan sebuah kesalahan. Jika verifikasi berhasil, skrip akan berlanjut tanpa memasukkan nilai apa pun ke dalam _stack_. _Opcode_ ini telah dihapus di Tapscript.
