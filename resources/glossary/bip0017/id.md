---
term: BIP0017

definition: Proposal alternatif untuk P2SH yang memperkenalkan opcode OP_CHECKHASHVERIFY, yang akhirnya tidak diadopsi demi BIP16.
---
Proposal oleh Luke Dashjr yang bersaing dengan BIP12 dan BIP16. BIP17 memperkenalkan sebuah opcode baru, `OP_CHECKHASHVERIFY`, yang didesain untuk memungkinkan verifikasi sebuah skrip yang terdapat pada `scriptSig` dengan _hash_ yang terdapat pada `scriptPubKey` sebelum mengakses Bitcoin. Setelah melalui perdebatan sengit, BIP16 (P2SH) pada akhirnya lebih disukai daripada BIP17 (CHV).
