---
term: seed NODEN
---

Statische lijst van publieke Bitcoin knooppunten, direct geïntegreerd in de broncode van Bitcoin core (`Bitcoin/src/chainparamsseeds.h`). Deze lijst dient als verbindingspunten voor nieuwe Bitcoin knooppunten die zich bij het netwerk aansluiten, maar wordt alleen gebruikt als de DNS seeds geen antwoord geven binnen 60 seconden na hun verzoek. In dit geval zal het nieuwe Bitcoin knooppunt verbinding maken met deze seed knooppunten om een eerste verbinding met het netwerk te maken en IP adressen van andere knooppunten op te vragen. Het uiteindelijke doel is om de benodigde informatie te verkrijgen om de Initial Block Download (IBD) uit te voeren en te synchroniseren met de keten die het meeste werk heeft geaccumuleerd. De lijst van seed knooppunten bevat bijna 1000 knooppunten, geïdentificeerd in overeenstemming met de standaard vastgelegd door BIP155. seed knooppunten vertegenwoordigen dus de derde methode van verbinding met het netwerk voor een Bitcoin knooppunt, na het mogelijke gebruik van het `peers.dat` bestand, aangemaakt door het knooppunt zelf, en het aanvragen van DNS seeds.


> opmerking: seed knooppunten moeten niet verward worden met "DNS seeds", die de tweede methode zijn om verbindingen tot stand te brengen