---
term: VIN
definition: Onderdeel van een Bitcoin-transactie die de bron van het geld specificeert via een verwijzing naar een vorige UTXO.
---

Een specifiek element van een Bitcoin transactie dat de bron van fondsen specificeert die worden gebruikt om aan de outputs te voldoen. Elke `vin` verwijst naar een onbestede output (UTXO) van een voorgaande transactie. Een transactie kan meerdere inputs bevatten, elk geïdentificeerd door een combinatie van de `txid` (de identificator van de oorspronkelijke transactie) en de `vout` (de index van de output in die transactie).


Elke `vin` bevat de volgende informatie:


- `txid`: de identifier van de vorige transactie met de uitvoer die hier als invoer wordt gebruikt;
- `vout`: de index van de uitvoer in de vorige transactie;
- `scriptSig` of `scriptWitness`: een ontgrendelingsscript dat de benodigde gegevens levert om te voldoen aan de voorwaarden gesteld door de `scriptPubKey` van de vorige transactie waarvan het geld wordt uitgegeven, meestal door het leveren van een cryptografische handtekening;
- `nSequence`: een specifiek veld dat wordt gebruikt om aan te geven hoe deze ingang in de tijd wordt vergrendeld, evenals andere opties zoals RBF.