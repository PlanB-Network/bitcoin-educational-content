---
term: Gossip
definition: P2P-protocol voor het verspreiden van informatie tussen nodes op een epidemische manier.
---

Gossip is een peer-to-peer (P2P) gedistribueerd algoritme voor het epidemisch verspreiden van informatie naar alle netwerkagenten. Voor Bitcoin, Lightning en andere gedistribueerde systemen maakt dit protocol het mogelijk om de Global State van knooppunten uit te wisselen en te synchroniseren in slechts enkele cycli. Elk knooppunt verspreidt informatie naar een of meer willekeurige of niet-willekeurige buren, die op hun beurt de informatie verspreiden naar andere buren, enzovoort, totdat een globaal gesynchroniseerde toestand is bereikt.


In Lightning is roddelen een communicatieprotocol tussen knooppunten om informatie te delen over de huidige toestand en topologie van het netwerk. Het roddelprotocol stelt knooppunten in staat om de dynamische status van betaalkanalen en andere knooppunten te kennen, om de routering van transacties over het netwerk te vergemakkelijken zonder dat er directe verbindingen tussen alle knooppunten nodig zijn.


