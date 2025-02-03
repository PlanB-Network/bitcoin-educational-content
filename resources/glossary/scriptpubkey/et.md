---
term: SCRIPTPUBKEY

---
Bitcoini tehingu väljundosas asuv skript, mis määratleb tingimused, mille alusel saab seotud UTXO-d kulutada. See skript kindlustab seega bitcoinid. Kõige tavalisemal kujul sisaldab `scriptPubKey` tingimust, mis nõuab, et järgmine tehing tõendaks kindlaksmääratud Bitcoini aadressile vastava privaatvõtme olemasolu. See saavutatakse sageli skripti abil, mis nõuab allkirja, mis vastab nende vahendite tagamiseks kasutatud aadressiga seotud avalikule võtmele. Kui tehing üritab seda UTXOd kasutada sisendina, peab ta esitama `scriptSig`, mis koos `scriptPubKey`ga vastab seatud tingimustele ja annab kehtiva skripti.

Näiteks siin on klassikaline P2PKH `scriptPubKey`:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```

Vastav `scriptSig` oleks:

```text
<signature> <public key>
```

![](../../dictionnaire/assets/35.webp)

> ► *Seda kirjaviisi nimetatakse inglise keeles mõnikord ka "locking script"