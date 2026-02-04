---
term: P2P TRANSPORT V2
definition: Nieuwe versie van het Bitcoin P2P-protocol met versleuteling om de privacy te verbeteren.
---

Nieuwe versie van het Bitcoin P2P transportprotocol met opportunistische versleuteling om de privacy en veiligheid van de communicatie tussen knooppunten te verbeteren. Deze verbetering beoogt Address verschillende problemen met de basisversie van het P2P protocol, met name door de uitgewisselde gegevens ononderscheidbaar te maken voor een passieve waarnemer (zoals een internet service provider), waardoor de risico's van censuur en aanvallen worden verminderd door de detectie van specifieke patronen in datapakketten.


De geïmplementeerde versleuteling bevat geen authenticatie om geen onnodige complexiteit toe te voegen en om de toestemmingsvrije aard van de netwerkverbinding niet in gevaar te brengen. Dit nieuwe P2P transportprotocol biedt niettemin betere beveiliging tegen passieve aanvallen en maakt actieve aanvallen aanzienlijk kostbaarder en detecteerbaarder (met name MITM-aanvallen). De introductie van een pseudo-willekeurige gegevensstroom bemoeilijkt de taak voor aanvallers die communicatie willen censureren of manipuleren.


De P2P Transport V2 is als optie opgenomen (standaard uitgeschakeld) in versie 26.0 van Bitcoin core, ingezet in december 2023. Het kan worden geactiveerd met de `v2transport=1` optie in het configuratiebestand.