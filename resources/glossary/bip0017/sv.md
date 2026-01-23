---
term: BIP0017
definition: Alternativt förslag till P2SH som introducerade opkoden OP_CHECKHASHVERIFY, men som i slutändan inte antogs till förmån för BIP16.
---

Förslag av Luke Dashjr som konkurrerade med BIP12 och BIP16. BIP17 introducerade en ny opcode, `OP_CHECKHASHVERIFY`, utformad för att möjliggöra verifiering av ett skript som finns i `scriptSig` mot dess Hash som finns i `scriptPubKey` innan pengarna låses upp. BIP16 (P2SH) föredrogs slutligen framför BIP17 (CHV) efter en period av intensiva debatter.