---
term: OP_NUMEQUALVERIFY (0X9D)
definition: Combineert OP_NUMEQUAL en OP_VERIFY, mislukt als de numerieke waarden verschillen.
---

Combineert de bewerkingen `OP_NUMEQUAL` en `OP_VERIFY`. Het vergelijkt numeriek de twee bovenste Elements op de stack. Als de waarden gelijk zijn, verwijdert `OP_NUMEQUALVERIFY` het ware resultaat van de stack en gaat verder met de uitvoering van het script. Als de waarden niet gelijk zijn, is het resultaat onwaar en mislukt het script onmiddellijk.