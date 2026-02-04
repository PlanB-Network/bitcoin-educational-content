---
term: Herbruikbare betalingscode
definition: Statische identifier van BIP47 die de afleiding van unieke adressen mogelijk maakt zonder adreshergebruik.
---

In BIP47 is een herbruikbare betaalcode een statische identifier die wordt gegenereerd uit een Bitcoin Wallet die een meldingstransactie en de afleiding van unieke adressen mogelijk maakt. Dit voorkomt hergebruik van adressen, wat leidt tot verlies van privacy, zonder dat voor elke betaling handmatig nieuwe, ongebruikte adressen moeten worden afgeleid en verzonden. In BIP47 worden herbruikbare betalingscodes als volgt opgebouwd:


- Byte 0 komt overeen met de versie;
- Byte 1 is een bitveld voor het toevoegen van informatie in geval van specifiek gebruik;
- Byte 2 geeft de pariteit van de `y` van de openbare sleutel aan;
- Van byte 3 tot byte 34 vind je de `x` waarde van de publieke sleutel;
- Van byte 35 tot byte 66 is er de chain code geassocieerd met de publieke sleutel;
- Van byte 67 tot byte 79 is er nul opvulling.


Een Human-Readable Part (HRP) wordt over het algemeen toegevoegd aan het begin van de betalingscode en een controlesom aan het einde, waarna de code wordt gecodeerd in base58. De opbouw van een betaalcode is dus vergelijkbaar met die van een uitgebreide sleutel. Hier is bijvoorbeeld mijn eigen BIP47 betalingscode in base58:


```text
PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qD
udE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5
```


In de PayNym-implementatie van BIP47 kunnen betaalcodes ook worden uitgedrukt in de vorm van identifiers die zijn gekoppeld aan de afbeelding van een robot. Hier is de mijne, bijvoorbeeld:


```text
+throbbingpond8B1
```


Het gebruik van betaalcodes met de PayNym-implementatie is momenteel beschikbaar op Sparrow wallet op PC en op Samourai Wallet op mobiel.