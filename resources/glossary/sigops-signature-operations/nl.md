---
term: SIGOPS (HANDTEKENINGOPERATIES)
---

Verwijst naar de digitale handtekening operaties die nodig zijn om transacties te valideren. Elke Bitcoin transactie kan meerdere ingangen bevatten, die elk een of meer handtekeningen nodig hebben om als geldig beschouwd te worden. De verificatie van deze handtekeningen wordt gedaan door het gebruik van specifieke opcodes genaamd "sigops". Hieronder vallen specifiek `OP_CHECKSIG`, `OP_CHECKSIGVERIFY`, `OP_CHECKMULTISIG` en `OP_CHECKMULTISIGVERIFY`. Deze operaties leggen een bepaalde werklast op de netwerkknooppunten die ze moeten verifiëren. Om DoS aanvallen te voorkomen door het kunstmatig opdrijven van het aantal sigops, legt het protocol daarom een limiet op het aantal sigops dat per blok is toegestaan, om ervoor te zorgen dat de validatielast beheersbaar blijft voor de knooppunten. Deze limiet is momenteel ingesteld op een maximum van 80.000 sigops per blok. Om te tellen volgen de nodes deze regels:


In het `scriptPubKey` tellen `OP_CHECKSIG` en `OP_CHECKSIGVERIFY` voor 4 sigops. De opcodes `OP_CHECKMULTISIG` en `OP_CHECKMULTISIGVERIFY` tellen voor 80 sigops. Tijdens het tellen worden deze operaties namelijk met 4 vermenigvuldigd als ze geen deel uitmaken van een SegWit ingang (voor een P2WPKH zal het aantal sigops dus 1 zijn);


In de `redeemscript` tellen de opcodes `OP_CHECKSIG` en `OP_CHECKSIGVERIFY` ook als 4 sigops, `OP_CHECKMULTISIG` en `OP_CHECKMULTISIGVERIFY` tellen als `4n` als ze voorafgaan aan `OP_n`, of anders als 80 sigops;


Voor de `witnessScript` zijn `OP_CHECKSIG` en `OP_CHECKSIGVERIFY` 1 sigop waard, `OP_CHECKMULTISIG` en `OP_CHECKMULTISIGVERIFY` worden geteld als `n` als ze worden geïntroduceerd door `OP_n`, of anders 20 sigops;


In Taproot scripts worden sigops anders behandeld dan in traditionele scripts. In plaats van elke handtekeningoperatie direct te tellen, introduceert Taproot een sigops-budget voor elke transactie-invoer, dat evenredig is met de grootte van die invoer. Dit budget is 50 sigops plus de byte grootte van de getuige van de invoer. Elke handtekeningoperatie vermindert dit budget met 50. Als de uitvoering van een handtekeningoperatie het budget onder nul brengt, is het script ongeldig. Deze methode zorgt voor meer flexibiliteit in Taproot scripts, met behoud van bescherming tegen mogelijk misbruik gerelateerd aan sigops, door ze direct te koppelen aan het gewicht van de invoer. Taproot scripts zijn dus niet opgenomen in de 80.000 sigops per blok limiet.