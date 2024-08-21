---
term: SCRIPTPUBKEY
---

Skript, mis asub Bitcoini tehingu väljundiosas ja määratleb tingimused, mille alusel seotud UTXO-d saab kulutada. See skript seega turvab bitcoine. Kõige levinumas vormis sisaldab `scriptPubKey` tingimust, mis nõuab järgmiselt tehingult tõestust eraõiguse olemasolu kohta, mis vastab määratud Bitcoini aadressile. See saavutatakse sageli skripti abil, mis nõuab allkirja, mis vastab aadressiga seotud avalikule võtmele, mida kasutati nende vahendite turvamiseks. Kui tehing üritab seda UTXO-d sisendina kasutada, peab see esitama `scriptSig`, mis ühendatuna `scriptPubKey`-ga, vastab seatud tingimustele ja toodab kehtiva skripti.

Näiteks, siin on klassikaline P2PKH `scriptPubKey`:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <aadress> OP_EQUALVERIFY OP_CHECKSIG
```

Vastav `scriptSig` oleks:

```text
<allkiri> <avalik võti>
```

![](../../dictionnaire/assets/35.png)

> ► *Seda skripti nimetatakse inglise keeles mõnikord ka "lukustusskriptiks".*