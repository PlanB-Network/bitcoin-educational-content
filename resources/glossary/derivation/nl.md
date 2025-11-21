---
term: DERIVATIE
---

Verwijst naar het proces van het genereren van kind sleutelparen uit een ouder sleutelpaar (private sleutel en publieke sleutel) en een chain code binnen een deterministische en hiërarchische (HD) Wallet. Dit proces maakt de segmentatie van takken mogelijk en de organisatie van een Wallet in verschillende niveaus met talrijke kind sleutelparen, die allemaal hersteld kunnen worden door alleen de basis herstelinformatie te kennen (de Mnemonic zin en een mogelijke passphrase). Om een kind sleutel af te leiden, wordt de `HMAC-SHA512` functie gebruikt met de ouder chain code en de aaneenschakeling van de ouder sleutel en een 32-bit index. Er zijn twee soorten afleidingen:


- Normale afleiding, waarbij de openbare sleutel van de ouder wordt gebruikt als basis voor de `HMAC-SHA512`-functie;
- Geharde afleiding, die de privésleutel van de ouder gebruikt als basis voor de `HMAC-SHA512`-functie;


Het resultaat van HMAC-SHA512 wordt in tweeën gedeeld: de eerste 256 bits worden de kindsleutel (privaat of publiek na verwerking door ECDSA) en de resterende 256 bits worden het chain code kind.