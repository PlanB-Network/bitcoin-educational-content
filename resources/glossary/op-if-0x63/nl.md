---
term: OP_IF (0X63)
---

Voert het volgende deel van het script uit als de waarde bovenaan de stack niet nul is (true). Als de waarde nul is (false), worden deze bewerkingen overgeslagen en wordt direct overgegaan naar de bewerkingen na `OP_ELSE`, als deze aanwezig is. `OP_IF` maakt het mogelijk om een voorwaardelijke controlestructuur te starten binnen een script. Het bepaalt de controlestroom in een script op basis van een voorwaarde die wordt gegeven op het moment dat de transactie wordt uitgevoerd. `OP_IF` wordt samen met `OP_ELSE` en `OP_ENDIF` op de volgende manier gebruikt:


```text
<condition>
OP_IF
<operations if the condition is true>
OP_ELSE
<operations if the condition is false>
OP_ENDIF
```