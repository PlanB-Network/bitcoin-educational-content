---
term: VIN
definition: Element i en Bitcoin-transaktion som anger källan för medlen via en referens till en tidigare UTXO.
---

Ett specifikt element i en Bitcoin-transaktion som anger källan till de medel som används för att tillfredsställa utgifterna. Varje `vin` hänvisar till en outnyttjad output (UTXO) från en tidigare transaktion. En transaktion kan innehålla flera inputs, som var och en identifieras genom en kombination av `txid` (identifieraren för den ursprungliga transaktionen) och `vout` (indexet för output i den transaktionen).


Varje `vin` innehåller följande information:


- gW-3: Identifieraren för den föregående transaktionen som innehåller den produktion som här används som input;
- `vout`: indexet för utdata i den föregående transaktionen;
- `scriptSig` eller `scriptWitness`: ett upplåsningsskript som tillhandahåller de uppgifter som krävs för att uppfylla de villkor som ställs av `scriptPubKey` för den tidigare transaktion vars medel används, vanligtvis genom att tillhandahålla en kryptografisk signatur;
- `nSequence`: ett specifikt fält som används för att ange hur denna ingång är tidslåst, liksom andra alternativ som RBF.