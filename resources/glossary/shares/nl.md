---
term: Shares
definition: Indicator die de bijdrage van een individuele miner binnen een miningpool kwantificeert.
---

In de context van Mining-pools is een aandeel een indicator die wordt gebruikt om de bijdrage van een individuele Miner binnen de pool te kwantificeren. Deze maat dient als basis voor de berekening van de beloning die de pool aan elke Miner herverdeelt. Elk aandeel komt overeen met een Hash die voldoet aan een moeilijkheidsdoel dat lager is dan dat van het Bitcoin netwerk.


Om dit met een analogie uit te leggen, neem een 20-zijdige dobbelsteen. Op Bitcoin, stel dat de Proof of Work vereist dat je een getal lager dan 3 gooit om een blok te valideren (dat wil zeggen, een resultaat van 1 of 2 behalen). Stel je nu voor dat binnen een Mining pool, de moeilijkheidsdoelstelling voor een aandeel op 10 staat. Dus voor een individuele Miner in de pool telt elke dobbelsteenworp met een resultaat lager dan 10 als een geldig aandeel. Deze aandelen worden dan door de Miner naar de pool gestuurd, om hun beloning op te eisen, zelfs als ze niet overeenkomen met een geldig resultaat voor een blok op Bitcoin.


Voor elke berekende Hash kan een individuele Miner in een pool drie verschillende scenario's tegenkomen:


- Als de Hash waarde groter of gelijk is aan het ingestelde moeilijkheidsdoel van de pool voor een aandeel, dan heeft deze Hash geen nut. De Miner verandert dan zijn Nonce om een nieuwe Hash te proberen: `Hash > share > block`.
- Als de Hash lager is dan het moeilijkheidsdoel van het aandeel, maar groter dan of gelijk aan het moeilijkheidsdoel van Bitcoin, dan vormt deze Hash een geldig aandeel dat echter niet voldoende is om een blok te valideren. De Miner kan deze Hash naar hun pool sturen om de beloning op te eisen die bij het aandeel hoort: `aandeel > Hash > blok`.
- Als de Hash lager is dan de moeilijkheidsdoelstelling van het Bitcoin netwerk, wordt het beschouwd als zowel een geldig aandeel als een geldig blok. De Miner zendt deze Hash naar hun pool, die zich haast om het uit te zenden op het Bitcoin netwerk. Deze Hash wordt ook geteld als een geldige share voor de Miner: `share > bloc > Hash`.





Dit deelsysteem wordt gebruikt om het werk te schatten dat door elke individuele Miner binnen een pool is gedaan, zonder dat alle hashes die door een Miner zijn gegenereerd individueel opnieuw berekend moeten worden, wat volledig inefficiënt zou zijn voor de pool.


Mining pools passen de moeilijkheidsgraad van de aandelen aan om de verificatielast in balans te brengen en zorgen ervoor dat elke Miner, klein of groot, ongeveer elke paar seconden aandelen indient. Dit maakt een nauwkeurige berekening van de Hashrate van elke Miner mogelijk en de verdeling van beloningen volgens de gekozen berekeningsmethode voor compensatie (PPS, PPLNS, TIDES...).


