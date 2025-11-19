---
term: UITPUNT
---

Een unieke verwijzing naar een niet-uitgevoerde transactie-uitgang (UTXO). Het bestaat uit twee Elements:


- `txid`: de identifier van de transactie die de uitvoer heeft aangemaakt;
- `vout`: de index van de uitvoer in de transactie.


De combinatie van deze twee Elements identificeert precies een UTXO. Bijvoorbeeld, als een transactie een `txid` heeft van `abc...123` en de uitvoerindex is `0`, dan wordt het uitvoerpunt genoteerd als:


```text
abc...123:0
```


Het outpoint wordt gebruikt in de input (`vin`) van een nieuwe transactie om aan te geven welke UTXO wordt uitgegeven.


> ► *De term "outpoint" wordt vaak synoniem gebruikt met "UTXO."*