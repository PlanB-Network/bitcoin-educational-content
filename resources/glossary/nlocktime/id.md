---
term: NLOCKTIME

---
Bidang yang disematkan dalam transaksi yang menetapkan kondisi berbasis waktu sebelum transaksi tidak dapat ditambahkan ke blok yang valid. Parameter ini memungkinkan untuk menentukan waktu yang tepat (stempel waktu Unix) atau jumlah blok tertentu sebagai syarat agar transaksi dianggap sah. Dengan demikian, hal ini merupakan penguncian waktu yang absolut (bukan relatif). `nLockTime` mempengaruhi seluruh transaksi dan secara efektif memungkinkan verifikasi waktu, sedangkan _opcode_ `OP_CHECKLOCKTIMEVERIFY` hanya memungkinkan untuk membandingkan nilai teratas dari tumpukan dengan nilai `nLockTime`.
