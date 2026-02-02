---
term: Atomic swap
definition: Een uitwisseling van cryptocurrencies tussen twee partijen zonder vertrouwde intermediair, waarbij de uitwisseling volledig slaagt of volledig wordt geannuleerd.
---

Technologie die de directe Exchange van cryptocurrencies tussen twee partijen mogelijk maakt, zonder dat er vertrouwen nodig is en zonder tussenpersoon. Deze uitwisselingen worden "atomair" genoemd omdat ze slechts twee resultaten kunnen opleveren:


- Ofwel is de Exchange succesvol en hebben beide deelnemers hun cryptocurrencies effectief uitgewisseld;
- Of de Exchange mislukt, en beide deelnemers vertrekken met hun oorspronkelijke cryptocurrencies.


Atomic Swaps kunnen worden uitgevoerd met dezelfde cryptocurrency, in welk geval het ook een "*coinswap*" wordt genoemd, of tussen verschillende cryptocurrencies. Historisch gezien vertrouwden ze op "Hash Time-Locked Contracts" (HTLC), een tijdvergrendelingssysteem dat de voltooiing of volledige annulering van de Exchange garandeert, waardoor de integriteit van de fondsen van de betrokken partijen behouden blijft. Deze methode vereiste protocollen die zowel scripts als tijdsloten aankonden. De laatste jaren is de trend echter verschoven naar het gebruik van *Adaptor Signatures*. Deze tweede benadering heeft het voordeel dat er geen scripts meer nodig zijn, waardoor de operationele kosten dalen. Het andere grote voordeel is dat het niet nodig is om identieke hashing te gebruiken voor beide delen van de transactie, wat helpt om te voorkomen dat er een verband tussen beide wordt onthuld.