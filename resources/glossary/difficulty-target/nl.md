---
term: MOEILIJKHEIDSDOEL
---

De moeilijkheidsfactor, ook bekend als het moeilijkheidsdoel, is een parameter die gebruikt wordt in het consensusmechanisme van Proof of Work (Proof of Work, PoW) op Bitcoin. Het doel vertegenwoordigt een numerieke waarde die de moeilijkheidsgraad bepaalt voor mijnwerkers om een specifiek cryptografisch probleem op te lossen, Proof of Work genaamd, bij het creëren van een nieuw blok op Blockchain.


De moeilijkheidsdoelstelling is een instelbaar getal van 256 bits (64 bytes) dat een aanvaardbaarheidslimiet bepaalt voor het hashen van blokkoppen. Met andere woorden, om een blok geldig te laten zijn, moet de Hash van de header met `SHA256d` (dubbel `SHA256`) numeriek lager of gelijk zijn aan de moeilijkheidsdoelstelling. De Proof of Work bestaat uit het wijzigen van het `Nonce` veld van de blokkop of de Coinbase Transaction totdat de resulterende Hash lager is dan de doelwaarde.


Dit doel wordt om de 2016 blokken aangepast (ongeveer om de twee weken), tijdens een gebeurtenis die "aanpassing" heet De moeilijkheidsfactor wordt herberekend op basis van de tijd die het kostte om de vorige 2016-blokken te delven. Als de totale tijd minder dan twee weken is, neemt de moeilijkheidsgraad toe door het doel naar beneden aan te passen. Als de totale tijd meer dan twee weken is, neemt de moeilijkheidsgraad af door het doel naar boven bij te stellen. Het doel is om een gemiddelde Mining tijd van 10 minuten per blok aan te houden. Deze tijd tussen elk blok helpt om splitsingen van het Bitcoin netwerk te voorkomen, wat leidt tot verspilling van rekenkracht. De moeilijkheidsdoelstelling is te vinden in de kop van elk blok, in het `nBits` veld. Omdat dit veld gereduceerd is tot 32 bits en het doel eigenlijk 256 bits is, is het doel gecomprimeerd tot een minder precies wetenschappelijk formaat.


![](../../dictionnaire/assets/34.webp)


> *Het moeilijkheidsdoel wordt soms ook de "moeilijkheidsfactor" genoemd Bij uitbreiding kan ernaar verwezen worden met de codering in de blokkoppen met de term "nBits"*