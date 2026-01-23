---
term: Anonsets (anonimiteitssets)
definition: Indicatoren die de mate van privacy van een UTXO meten door het aantal onderscheidbare UTXO's in een set te tellen, typisch na een coinjoin.
---
Anonsets dienen als indicatoren om de mate van privacy van een specifieke UTXO te beoordelen. Meer specifiek meten zij het aantal niet-onderscheidbare UTXO’s binnen de verzameling die de onderzochte munt omvat. Aangezien een groep identieke UTXO’s vereist is, worden anonsets doorgaans berekend binnen een coinjoin-cyclus. Ze maken het mogelijk, indien nodig, de kwaliteit van coinjoins te beoordelen. Een anonset van grote omvang duidt op een hoger niveau van anonimiteit, omdat het moeilijk wordt om een specifieke UTXO binnen de verzameling te onderscheiden.

Er bestaan twee soorten anonsets: de forward anonset (forward-looking metrics); en de backward anonset (backward-looking metrics). De term "*score*" wordt soms ook gebruikt om anonsets aan te duiden.

De eerste geeft de grootte aan van de groep waarbinnen de bestudeerde UTXO aan de uitgang zich verbergt, gegeven de UTXO aan de ingang. Deze indicator maakt het mogelijk de weerstand van de privacy van de munt te meten tegen een analyse van verleden naar heden (van ingang naar uitgang). De tweede geeft het aantal mogelijke bronnen voor een bepaalde munt aan, gegeven de UTXO aan de uitgang. Deze indicator maakt het mogelijk de weerstand van de privacy van de munt te meten tegen een analyse van heden naar verleden (van uitgang naar ingang).
















