---
term: Recursieve (covenant)
definition: Covenant die voorwaarden oplegt aan de huidige transactie en alle transacties die daarna volgen, voor onbepaalde tijd.
---

Een recursieve overeenkomst op Bitcoin is een type Smart contract dat niet alleen voorwaarden oplegt aan de huidige transactie, maar ook aan toekomstige transacties die de output van deze transactie uitgeven. Dit maakt het mogelijk om transactieketens te maken waarbij elke transactie zich moet houden aan bepaalde regels die gedefinieerd zijn door de eerste in de keten. Recursiviteit creëert een opeenvolging van transacties waarbij elke transactie de beperkingen erft van de oudertransactie. Dit zou complexe en langdurige controle mogelijk maken over hoe bitcoins kunnen worden uitgegeven, maar het zou ook risico's introduceren met betrekking tot bestedingsvrijheid en fungibiliteit.


Kortom, een niet-recursief convenant beperkt zich tot de transactie die onmiddellijk volgt op de transactie waarin de regels zijn vastgelegd. Omgekeerd heeft een recursief convenant de mogelijkheid om voor onbepaalde tijd specifieke voorwaarden op te leggen aan een Bitcoin. Transacties kunnen elkaar opvolgen, maar de Bitcoin in kwestie behoudt altijd de oorspronkelijke voorwaarden. Transacties kunnen elkaar opvolgen, maar de Bitcoin in kwestie behoudt altijd de oorspronkelijke voorwaarden die eraan verbonden waren. Technisch gezien ontstaat een niet-recursieve overeenkomst wanneer de `scriptPubKey` van een UTXO beperkingen oplegt aan de `scriptPubKey` van de uitvoer van een transactie die deze UTXO gebruikt. Een recursief convenant daarentegen ontstaat wanneer de `scriptPubKey` van een UTXO beperkingen definieert op de `scriptPubKey` van de uitvoer van een transactie die deze UTXO uitgeeft, en op alle `scriptPubKey`s die zullen volgen op de uitgave van deze UTXO.


Meer in het algemeen, in computers, is wat "recursiviteit" wordt genoemd de mogelijkheid van een functie om zichzelf aan te roepen, waardoor een soort lus ontstaat.