---
term: OP_CHECKMULTISIGVERIFY (0XAF)
---

Menggabungkan `OP_CHECKMULTISIG` dan `OP_VERIFY`. Ini memerlukan beberapa tanda tangan dan kunci publik untuk memverifikasi bahwa `M` dari `N` tanda tangan adalah valid, sama seperti yang dilakukan `OP_CHECKMULTISIG`. Kemudian, seperti `OP_VERIFY`, jika verifikasi gagal, skrip langsung berhenti dengan kesalahan. Jika verifikasi berhasil, skrip dilanjutkan tanpa mendorong nilai apa pun ke dalam tumpukan. Opcode ini dihapus dalam Tapscript.