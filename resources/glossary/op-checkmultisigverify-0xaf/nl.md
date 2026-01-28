---
term: OP_CHECKMULTISIGVERIFY (0XAF)
definition: Combineert OP_CHECKMULTISIG en OP_VERIFY, waarbij het script stopt als de verificatie mislukt.
---

Combineert een `OP_CHECKMULTISIG` en een `OP_VERIFY`. Het neemt meerdere handtekeningen en publieke sleutels om te verifiëren dat `M` van de `N` handtekeningen geldig zijn, net zoals `OP_CHECKMULTISIG` doet. Dan, net als `OP_VERIFY`, als de verificatie mislukt, stopt het script onmiddellijk met een foutmelding. Als de verificatie succesvol is, gaat het script verder zonder een waarde op de stack te zetten. Deze opcode is verwijderd in Tapscript.