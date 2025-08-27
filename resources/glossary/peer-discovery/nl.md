---
term: PEER ONTDEKKEN
---

Het proces waarbij knooppunten in het Bitcoin netwerk verbinding maken met andere knooppunten om informatie te verkrijgen. Wanneer een Bitcoin knooppunt voor het eerst wordt gestart, heeft het geen informatie over andere knooppunten in het netwerk. Toch moet het verbindingen tot stand brengen om te synchroniseren met de Blockchain die het meeste werk heeft. Er worden verschillende mechanismen gebruikt om deze peers te ontdekken, in volgorde van prioriteit:


- Het knooppunt begint met het raadplegen van zijn lokale `peers.dat` bestand, dat informatie bevat over knooppunten waarmee het eerder heeft gecommuniceerd. Als het knooppunt nieuw is, is dit bestand leeg en gaat het proces naar de volgende stap;
- Bij afwezigheid van informatie in het `peers.dat` bestand (wat normaal is voor een nieuw gelanceerd knooppunt), voert het knooppunt DNS queries uit naar de DNS seeds. Deze servers geven een lijst met IP-adressen van vermoedelijk actieve knooppunten om verbindingen tot stand te brengen. De adressen van de DNS seeds zijn hard gecodeerd in de Bitcoin core code. Deze stap is meestal voldoende om de ontdekking van peers te voltooien;
- Als de DNS seeds niet binnen 60 seconden reageren, kan het knooppunt zich wenden tot de seed knooppunten. Dit zijn openbare Bitcoin knooppunten die zijn opgenomen in een statische lijst van bijna duizend entries die direct in de broncode van Bitcoin core is geïntegreerd. Het nieuwe knooppunt zal deze lijst gebruiken om een eerste verbinding met het netwerk tot stand te brengen en IP-adressen van andere knooppunten te verkrijgen;
- In het zeer onwaarschijnlijke geval dat alle voorgaande methoden falen, heeft de beheerder van het knooppunt altijd de mogelijkheid om handmatig IP-adressen van knooppunten toe te voegen om een eerste verbinding tot stand te brengen.