---
term: OP_CHECKMULTISIGVERIFY (0XAF)
---

Combineert een `OP_CHECKMULTISIG` en een `OP_VERIFY`. Het neemt meerdere handtekeningen en publieke sleutels om te verifiëren dat `M` van de `N` handtekeningen geldig zijn, net zoals `OP_CHECKMULTISIG` doet. Dan, net als `OP_VERIFY`, als de verificatie mislukt, stopt het script onmiddellijk met een foutmelding. Als de verificatie succesvol is, gaat het script verder zonder een waarde op de stack te zetten. Deze opcode is verwijderd in Tapscript.