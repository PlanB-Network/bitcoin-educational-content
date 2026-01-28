---
term: Invoice lightning
definition: Lightning-betalningsförfrågan som innehåller all information som behövs för att slutföra transaktionen.
---

Blixtsnabb betalningsbegäran som genereras av mottagaren och som innehåller all information som behövs för att slutföra transaktionen.


En Invoice Lightning innehåller betalningsdestinationen i form av mottagarnodens publika nyckel, men också ett LN-prefix, beloppet, en förfallotid, Hash för den hemlighet som används i HTLC och andra metadata, varav en del är valfria, t.ex. routningsalternativ. Dessa fakturor definieras av BOLT11-standarden. När en Invoice Lightning har betalats kan den inte återanvändas.


