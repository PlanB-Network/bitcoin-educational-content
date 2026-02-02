---
term: Formbarhet (transaktion)
definition: Möjligheten att ändra strukturen på en transaktion utan att ändra dess effekt, men genom att ändra dess TXID.
---

Avser möjligheten att något modifiera strukturen i en Bitcoin-transaktion utan att ändra dess effekt, men samtidigt ändra transaktionsidentifieraren (*txid*). Denna egenskap kan utnyttjas på ett illvilligt sätt för att vilseleda intressenter om statusen för en transaktion och därmed orsaka problem som dubbla utgifter. Formbarheten möjliggjordes genom flexibiliteten hos den digitala signatur som användes. SegWit Soft Fork infördes framför allt för att förhindra att Bitcoin-transaktioner kunde manipuleras, vilket gjorde implementeringen av Lightning Network komplicerad. Detta uppnås genom att ta bort de manipulerbara uppgifterna från transaktionen från txid-beräkningen.


> även om det är sällsynt används ibland termen "mutabilitet" för att hänvisa till samma begrepp