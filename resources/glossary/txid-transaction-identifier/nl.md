---
term: txid (TRANSACTIE-IDENTIFICATIECODE)
---

Een uniek identificatienummer geassocieerd met elke Bitcoin transactie. Deze wordt gegenereerd door de `SHA256d` Hash van de transactiegegevens te berekenen. De txid dient als referentie om een specifieke transactie binnen de Blockchain te vinden. Het wordt ook gebruikt om te verwijzen naar een UTXO, die in wezen de aaneenschakeling is van een txid van een vorige transactie en de index van de aangewezen uitvoer (ook "vout" genoemd). Voor transacties van na SegWit houdt de txid geen rekening meer met de transactiegetuige, wat de vervormbaarheid elimineert.