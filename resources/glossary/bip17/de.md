---
term: BIP17
---

Vorschlag von Luke Dashjr, der mit BIP12 und BIP16 konkurrierte. BIP17 führte einen neuen Opcode, `OP_CHECKHASHVERIFY`, ein, der dazu gedacht war, die Überprüfung eines Skripts, das im `scriptSig` vorhanden ist, gegen seinen Hash, der im `scriptPubKey` vorhanden ist, zu ermöglichen, bevor die Mittel freigegeben werden. BIP16 (P2SH) wurde letztendlich nach einer Zeit intensiver Debatten BIP17 (CHV) vorgezogen.