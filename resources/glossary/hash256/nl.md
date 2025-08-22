---
term: HASH256
---

Cryptografische functie gebruikt voor verschillende toepassingen op Bitcoin. Hierbij wordt de SHA256-functie twee keer toegepast op de invoergegevens. Het bericht wordt één keer door SHA256 gehaald en het resultaat van deze bewerking wordt gebruikt als invoer voor een tweede keer door SHA256. De uitvoer van deze functie is daarom 256 bits.


$${HASH256}(x) = \text{SHA256}(\text{SHA256}(x))$$