---
term: OP_CHECKHASHVERIFY (CHV)

---
Sebuah _opcode_ baru yang diusulkan pada tahun 2012 di BIP17 oleh Luke Dashjr yang akan menawarkan fungsi yang sama dengan `OP_EVAL` atau P2SH. _Opcode_ ini dimaksudkan untuk meng-_hash_ akhir dari `scriptSig`, membandingkan hasilnya dengan bagian atas _stack_, dan membuat transaksi menjadi tidak valid jika kedua _hash_ tersebut tidak cocok. _Opcode_ ini tidak pernah diimplementasikan.
