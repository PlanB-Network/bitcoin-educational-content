---
term: VOUT
definition: Onderdeel van een Bitcoin-transactie die de bestemming van het geld bepaalt met een waarde en een locking script.
---

Een specifiek element van een Bitcoin transactie dat de bestemming van het verzonden geld bepaalt. Een transactie kan meerdere uitgangen bevatten, elk uniek geïdentificeerd door de combinatie van de transactie identifier (`txid`) en een index genaamd `vout`. Deze index, beginnend bij `0`, markeert de positie van de uitgang in de reeks van transactie-uitgangen. Zo wordt de eerste uitvoer aangeduid met `"vout: 0`, de tweede met `"vout": 1`, enzovoort.


Elke `vout` bevat voornamelijk twee stukjes informatie:


- de waarde, uitgedrukt in bitcoins, die het verzonden bedrag vertegenwoordigt;
- een vergrendelingsscript (`scriptPubKey`) dat de voorwaarden bepaalt waaronder het geld opnieuw kan worden uitgegeven in een toekomstige transactie.


De combinatie van de `txid` en de `vout` van een specifiek stuk vormt wat bijvoorbeeld een UTXO wordt genoemd:


```text
txid: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf
vout: 0
outpoint: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf:0
```