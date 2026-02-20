---
term: Stamps
definition: Protocol waarmee afbeeldingsgegevens in de Bitcoin-blockchain kunnen worden ingebed via P2MS-transacties.
---

Een protocol dat de integratie van geformatteerde afbeeldingsgegevens rechtstreeks op de Bitcoin Blockchain mogelijk maakt via onbewerkte transacties met meerdere handtekeningen (P2MS). Stamps codeert de binaire inhoud van een afbeelding in base 64 en voegt deze toe aan de sleutels van een 1/3 P2MS. Eén sleutel is echt en wordt gebruikt om het geld uit te geven, terwijl de andere twee dummy-sleutels zijn (de bijbehorende privésleutel is onbekend) die de gegevens opslaan. Door de gegevens direct als publieke sleutels te coderen in plaats van `OP_RETURN` uitgangen te gebruiken, zijn afbeeldingen die zijn opgeslagen met het Stamps protocol bijzonder werkintensief voor de knooppunten. Deze methode creëert met name meerdere UTXO's, wat de grootte van de UTXO set vergroot en problemen oplevert voor volle nodes.