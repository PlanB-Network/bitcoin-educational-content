---
term: Invoice LIGHTNING
---

Blixtsnabb betalningsbegäran som genereras av mottagaren och som innehåller all information som behövs för att slutföra transaktionen.


En Invoice Lightning innehåller betalningsdestinationen i form av mottagarnodens publika nyckel, men också ett LN-prefix, beloppet, en förfallotid, Hash för den hemlighet som används i HTLC och andra metadata, varav en del är valfria, t.ex. routningsalternativ. Dessa fakturor definieras av BOLT11-standarden. När en Invoice Lightning har betalats kan den inte återanvändas.


> ► *På franska skulle vi kunna översätta "Invoice" med "facture", men vi använder i allmänhet den engelska termen även på franska*