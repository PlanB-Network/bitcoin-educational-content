---
term: BIP0017
definition: Alternatief voorstel voor P2SH dat de opcode OP_CHECKHASHVERIFY introduceerde, uiteindelijk niet aangenomen ten gunste van BIP16.
---

Voorstel van Luke Dashjr dat concurreerde met BIP12 en BIP16. BIP17 introduceerde een nieuwe opcode, `OP_CHECKHASHVERIFY`, ontworpen om de verificatie van een script aanwezig in de `scriptSig` tegen zijn Hash aanwezig in de `scriptPubKey` mogelijk te maken alvorens de fondsen te ontgrendelen. BIP16 (P2SH) kreeg uiteindelijk de voorkeur boven BIP17 (CHV) na een periode van intensieve debatten.