---
term: NLOCKTIME
---

Sebuah bidang tersemat dalam transaksi yang menetapkan kondisi berbasis waktu sebelum transaksi tersebut tidak dapat ditambahkan ke dalam blok yang valid. Parameter ini memungkinkan penentuan waktu yang tepat (timestamp Unix) atau jumlah blok tertentu sebagai kondisi agar transaksi dianggap valid. Dengan demikian, ini adalah timelock absolut (bukan relatif). `nLockTime` mempengaruhi seluruh transaksi dan secara efektif memungkinkan verifikasi waktu, sedangkan opcode `OP_CHECKLOCKTIMEVERIFY` hanya memungkinkan perbandingan nilai teratas dari stack dengan nilai `nLockTime`.