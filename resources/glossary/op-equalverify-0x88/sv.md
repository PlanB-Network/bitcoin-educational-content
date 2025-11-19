---
term: OP_EQUALVERIFY (0X88)
---

Kombinerar funktionerna i `OP_EQUAL` och `OP_VERIFY`. Den kontrollerar först att de två översta värdena på stacken är lika, och kräver sedan att resultatet är ett annat än noll, annars är transaktionen ogiltig. `OP_EQUALVERIFY` används framför allt i Address:s verifieringsskript.