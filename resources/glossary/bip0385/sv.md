---
term: BIP0385
definition: addr()- och raw()-funktioner för att beskriva utgångsskript efter adress eller i hexadecimal form i deskriptorer.
---

Introducerar deskriptorfunktionerna `addr(ADDR)` och `raw(HEX)`. Funktionen `addr(ADDR)` gör det möjligt att beskriva ett utdataskript med hjälp av en mottagande Address, medan funktionen `raw(HEX)` gör det möjligt att specificera ett utdataskript med hjälp av en rå hexadecimal representation av skriptet. BIP385 implementerades tillsammans med alla andra deskriptorrelaterade BIP:er (utom BIP386) i version 0.17 av Bitcoin Core.