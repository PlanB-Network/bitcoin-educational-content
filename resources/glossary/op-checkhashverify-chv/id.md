---
term: OP_CHECKHASHVERIFY (CHV)

---
Sebuah opcode baru yang diusulkan pada tahun 2012 di BIP17 oleh Luke Dashjr yang akan menawarkan fungsi yang sama dengan `OP_EVAL` atau P2SH. Opcode ini dimaksudkan untuk meng-hash akhir dari `scriptSig`, membandingkan hasilnya dengan bagian atas tumpukan, dan membuat transaksi menjadi tidak valid jika kedua hash tersebut tidak cocok. Opcode ini tidak pernah diimplementasikan.