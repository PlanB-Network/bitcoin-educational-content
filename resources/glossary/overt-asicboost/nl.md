---
term: OPEN ASICBOOST
---

De open en transparante versie van AsicBoost. AsicBoost is een algoritmische optimalisatietechniek die gebruikt wordt in Bitcoin Mining. Mijnwerkers die de Overt versie gebruiken, manipuleren het `nVersion` veld van het kandidaat-blok en gebruiken deze modificatie als een extra Nonce. Deze methode laat het eigenlijke `Nonce` veld van het blok onveranderd tijdens elke hashing poging, waardoor de berekeningen die nodig zijn voor elke SHA256 verminderd worden, door sommige gegevens hetzelfde te houden tussen de pogingen. Deze versie is publiekelijk detecteerbaar en verbergt zijn wijzigingen niet voor de rest van het netwerk, in tegenstelling tot de geheime versie van AsicBoost.