---
term: RÅ TRANSAKTION
---

En Bitcoin-transaktion som är byggd och signerad, existerar i sin binära form. En rå transaktion (*raw TX*) är den slutliga representationen av en transaktion, strax innan den sänds ut i nätverket. Denna transaktion innehåller all nödvändig information för att kunna inkluderas i ett block:


- Versionen;
- Flaggan;
- Ingångarna;
- Utgångarna;
- Låsningstiden;
- Vittnet.


Det som kallas en "*råtransaktion*" representerar rådata som passerar genom SHA256 Hash-funktionen två gånger för att generate transaktionens txid. Dessa data används sedan i blockets Merkle Tree för att integrera transaktionen i Blockchain.


> ► *Detta begrepp kallas ibland också "Serialized Transaction". På franska kan dessa termer översättas med "transaction brute" respektive "transaction sérialisée"*