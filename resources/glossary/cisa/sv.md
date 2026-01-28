---
term: CISA
definition: Tekniskt förslag för att kombinera signaturerna från alla ingångar i en transaktion till en enda, vilket minskar storlek och avgifter.
---

Akronym för "Cross-Input Signature Aggregation". Detta är ett tekniskt förslag som är utformat för att optimera storleken på Bitcoin-transaktioner genom att minska antalet signaturer som krävs för att validera dem.


För närvarande, på Bitcoin, måste varje input i en transaktion ha en individuell signatur innan den kan konsumeras. Detta bevisar att ägaren till UTXO i fråga har godkänt transaktionen. Med CISA är målet att kombinera signaturerna för alla inmatningar till en enda transaktion till en enda signatur som täcker alla inmatningar. Detta skulle göra det möjligt att minska storleken på transaktioner med många ingångar och därmed också minska deras kostnader. Detta skulle vara särskilt användbart för dem som utför coinjoins eller konsolideringar, samtidigt som fler transaktioner skulle kunna bekräftas på Bitcoin utan att blockstorlekar eller intervall ändras. CISA är baserat på Schnorr-protokollet, som möjliggör linjär aggregering av signaturer. Detta innebär att en enda signatur kan bevisa innehav av flera oberoende nycklar.


Att implementera CISA på Bitcoin är dock mycket komplicerat, eftersom det kräver genomgripande förändringar i hur skript fungerar. För närvarande görs skriptverifiering på Bitcoin input för input. Att gå över till en modell där en hel transaktion kontrolleras på en gång, som föreslås av CISA, är långt ifrån en trivial förändring.