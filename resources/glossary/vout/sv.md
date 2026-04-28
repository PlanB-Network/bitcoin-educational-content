---
term: VOUT
definition: Element i en Bitcoin-transaktion som bestämmer destinationen för medlen med ett värde och ett låsskript.
---

Ett specifikt element i en Bitcoin-transaktion som bestämmer destinationen för de skickade medlen. En transaktion kan innehålla flera utgångar, var och en unikt identifierad genom kombinationen av transaktionsidentifieraren (`txid`) och ett index kallat `vout`. Detta index, som börjar på `0`, markerar utmatningens position i sekvensen av transaktionsutmatningar. Således kommer den första utgången att betecknas med `"vout": 0`, den andra med `"vout": 1`, och så vidare.


Varje `vout` innehåller i första hand två typer av information:


- det värde, uttryckt i bitcoins, som representerar det belopp som skickats;
- ett låsningsskript (`scriptPubKey`) som anger de villkor som krävs för att medlen ska kunna användas igen i en framtida transaktion.


Kombinationen av `txid` och `vout` för en specifik bit bildar vad som kallas en UTXO, till exempel:


```text
txid: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf
vout: 0
outpoint: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf:0
```