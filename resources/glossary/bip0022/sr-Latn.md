---
term: BIP0022
definition: Standard JSON-RPC getblocktemplate koji omogućava softveru za rudarenje da komunicira sa punim čvorovima radi izgradnje blokova.
---

BIP predložen 2012. od strane Luke Dashjr koji uvodi standardizovani JSON-RPC metod za eksterne Mining interfejse, nazvan "getblocktemplate". Sa povećanjem težine Mining, razvila se upotreba specijalizovanog eksternog softvera za proizvodnju Proof of Work. Ovaj BIP predlaže zajednički standard komunikacije za šablon bloka između punih čvorova i softvera specijalizovanog za Mining. Ovaj metod uključuje slanje cele strukture bloka, umesto samo zaglavlja, kako bi se omogućilo Miner da ga prilagodi.