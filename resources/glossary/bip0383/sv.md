---
term: BIP0383
definition: multi()- och sortedmulti()-funktioner för att beskriva multisig-skript i deskriptorer.
---

Introducerar funktionerna `multi(NUM, KEY, ..., KEY)` och `sortedmulti(NUM, KEY, ..., KEY)` för deskriptorer. Dessa funktioner gör det möjligt att beskriva multisignaturskript i deskriptorerna, där `sortedmulti` sorterar de publika nycklarna i lexikografisk ordning för att säkerställa kompatibilitet vid import. BIP383 implementerades tillsammans med alla andra deskriptorrelaterade BIP:er (utom BIP386) i version 0.17 av Bitcoin Core.