---
term: BIP0017

definition: Alternativer Vorschlag zu P2SH, der den Opcode OP_CHECKHASHVERIFY einführte, aber letztendlich zugunsten von BIP16 abgelehnt wurde.
---
Vorschlag von Luke Dashjr, der mit BIP12 und BIP16 konkurrierte. BIP17 führte einen neuen Opcode ein, `OP_CHECKHASHVERIFY`, der die Verifizierung eines Skripts im `scriptSig` gegen seinen Hash im `scriptPubKey` ermöglichen sollte, bevor die Mittel freigeschaltet wurden. BIP16 (P2SH) wurde schließlich nach intensiven Debatten gegenüber BIP17 (CHV) bevorzugt.