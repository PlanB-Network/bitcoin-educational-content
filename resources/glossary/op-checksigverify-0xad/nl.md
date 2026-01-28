---
term: OP_CHECKSIGVERIFY (0XAD)
definition: Combineert OP_CHECKSIG en OP_VERIFY, waarbij het script stopt als de handtekening ongeldig is.
---

Voert dezelfde operatie uit als `OP_CHECKSIG`, maar als de verificatie van de handtekening mislukt, stopt het script onmiddellijk met een foutmelding en is de transactie dus ongeldig. Als de verificatie slaagt, gaat het script verder zonder een `1` (true) waarde op de stack te zetten. Samengevat voert `OP_CHECKSIGVERIFY` de operatie `OP_CHECKSIG` gevolgd door `OP_VERIFY` uit. Deze opcode is aangepast in Tapscript om Schnorr-handtekeningen te verifiëren.