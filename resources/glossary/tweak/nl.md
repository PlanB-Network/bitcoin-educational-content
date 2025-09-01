---
term: TWEAK
---

In cryptografie is het "tweaken" van een openbare sleutel het wijzigen ervan met behulp van een additieve waarde die een "tweak" wordt genoemd, zodat de sleutel bruikbaar blijft met kennis van zowel de originele privésleutel als de tweak. Technisch gezien is een tweak een scalaire waarde die wordt toegevoegd aan de originele openbare sleutel. Als $P$ de openbare sleutel is en $t$ de aanpassing, dan wordt de aangepaste openbare sleutel :


$$
P' = P + tG
$$


Waarbij $G$ de generator van de gebruikte elliptische curve is. Deze bewerking produceert een nieuwe openbare sleutel die is afgeleid van het origineel, met behoud van bepaalde cryptografische eigenschappen die het gebruik ervan mogelijk maken. Deze methode wordt bijvoorbeeld gebruikt voor Taproot (P2TR) adressen, om uitgaven mogelijk te maken door ofwel een Schnorr handtekening te presenteren op de traditionele manier, of door te voldoen aan één van de voorwaarden in een Merkle Tree, ook bekend als een "MAST".