---
term: Erlay
definition: Protokoll som förbättrar effektiviteten för vidareländning av transaktioner för att minska bandbreddsförbrukningen.
---

Föreslaget nätverksprotokoll för att förbättra effektiviteten i att vidarebefordra obekräftade transaktioner mellan Bitcoin-noder.


För närvarande sprids varje transaktion via ett system där varje nod sänder ut den transaktion som den känner till till alla sina kollegor. Problemet är att detta leder till en hel del redundans och bandbreddsanvändning för dubbletter. Många transaktionsutsändningar är onödiga, eftersom mottagaren redan känner till dessa transaktioner och varje nod bara behöver känna till varje transaktion en gång. Erlay föreslår att man som standard begränsar antalet peers som en nod direkt skickar transaktioner till som den känner till till 8, och att man sedan använder en avstämningsprocess baserad på minisketch-biblioteket för att dela saknade transaktioner på ett mer effektivt sätt.


Erlay skulle minska bandbreddsförbrukningen med cirka 40%, vilket skulle göra Full node-driften mer tillgänglig för användare med begränsade internetanslutningar och därmed främja en bättre decentralisering av nätverket. Det här protokollet skulle också bibehålla en nästan konstant bandbreddsförbrukning när antalet anslutningar ökar. Detta innebär att det skulle bli mycket enklare för nodoperatörer att acceptera ett mycket stort antal anslutningar från sina kollegor, vilket skulle förbättra säkerheten i Bitcoin-nätverket genom att minska risken för partitionering, oavsett om den är avsiktlig eller oavsiktlig. Dessutom skulle Erlay göra det svårare att fastställa ursprungsnoden för en transaktion, vilket skulle öka konfidentialiteten för användare av noder som inte drivs under Tor.


Erlay föreslås i BIP330.