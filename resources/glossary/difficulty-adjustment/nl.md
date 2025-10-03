---
term: MOEILIJKHEIDSGRAAD AANPASSEN
---

Moeilijkheidsaanpassing is een periodiek proces dat de moeilijkheidsdoelstelling voor het Proof of Work mechanisme (Mining) op Bitcoin herdefinieert. Deze gebeurtenis vindt om de 2016 blokken plaats (ongeveer om de twee weken). Het dient om de moeilijkheidsfactor (ook wel de moeilijkheidsdoelstelling genoemd) te verhogen of te verlagen, afhankelijk van hoe snel de laatste 2016-blokken werden gevonden. De aanpassing heeft als doel om een stabiele en voorspelbare blokproductiesnelheid te behouden, met een frequentie van één blok elke 10 minuten, ondanks variaties in de rekenkracht ingezet door miners. De verandering in moeilijkheid tijdens de aanpassing is beperkt tot een factor 4. De formule die door de nodes wordt uitgevoerd om het nieuwe doel te berekenen is als volgt:

$$N = A \dot \left(\frac{T}{1.209.600}}right)$$


Waar:


- $N$: Het nieuwe doel;
- $A$: Het oude doel van de laatste 2016 blokken;
- $T$: De totale werkelijke tijd van de laatste 2016 blokken in seconden;
- $1,209,600$: De doeltijd in seconden om 2016 blokken te produceren met een interval van 10 minuten tussen elke blok.


> in het Frans wordt de term "reciblage" soms ook gebruikt om aanpassing aan te duiden. In het Engels wordt het "Difficulty Adjustment" genoemd.