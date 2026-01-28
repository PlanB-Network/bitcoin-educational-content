---
term: OP_EQUALVERIFY (0X88)
definition: Combineert OP_EQUAL en OP_VERIFY, waardoor de transactie ongeldig wordt als de waarden verschillen.
---

Combineert de functies van `OP_EQUAL` en `OP_VERIFY`. Het controleert eerst de gelijkheid van de bovenste twee waarden op de stack en vereist dan dat het resultaat niet nul is, anders is de transactie ongeldig. `OP_EQUALVERIFY` wordt vooral gebruikt in Address verificatiescripts.