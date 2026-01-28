---
term: Outpoint
definition: Unik referens till en UTXO, bestående av txid och utgångsindex.
---

En unik referens till en outnyttjad transaktionsutgång (UTXO). Den består av två Elements:


- gW-2": Identifieraren för den transaktion som skapade utdata;
- `vout`: index för utdata i transaktionen.


Kombinationen av dessa två Elements identifierar exakt en UTXO. Till exempel, om en transaktion har en `txid` på `abc...123` och utgångsindex är `0`, kommer utpunkten att noteras som:


```text
abc...123:0
```


Outpoint används i inputs (`vin`) i en ny transaktion för att ange vilken UTXO som spenderas.


> ► *Termen "outpoint" används ofta synonymt med "UTXO"*