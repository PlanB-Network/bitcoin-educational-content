---
term: BIP0017

definition: Alternativt forslag til P2SH som introduserte opkoden OP_CHECKHASHVERIFY, men som til slutt ikke ble valgt til fordel for BIP16.
---
Forslag av Luke Dashjr som konkurrerte med BIP12 og BIP16. BIP17 introduserte en ny opcode, `OP_CHECKHASHVERIFY`, som skal gjøre det mulig å verifisere et skript i `scriptSig` mot dets hash i `scriptPubKey` før midlene låses opp. BIP16 (P2SH) ble til slutt foretrukket fremfor BIP17 (CHV) etter en periode med intense debatter.