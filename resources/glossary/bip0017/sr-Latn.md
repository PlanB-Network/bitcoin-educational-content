---
term: BIP0017
definition: Alternativni predlog za P2SH koji je uvodio opcode OP_CHECKHASHVERIFY, na kraju nije usvojen u korist BIP16.
---

Predlog Luke Dashjr-a koji je konkurisao sa BIP12 i BIP16. BIP17 je uveo novi opcode, `OP_CHECKHASHVERIFY`, dizajniran da omogući verifikaciju skripta prisutnog u `scriptSig` u odnosu na njegov Hash prisutan u `scriptPubKey` pre otključavanja sredstava. BIP16 (P2SH) je na kraju bio preferiran u odnosu na BIP17 (CHV) nakon perioda intenzivnih debata.