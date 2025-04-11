---
term: SCRIPTPUBKEY

---
Skript umístěný ve výstupní části bitcoinové transakce, který definuje podmínky, za nichž lze utratit přidružené UTXO. Tento skript tedy zajišťuje bitcoiny. Ve své nejběžnější podobě obsahuje `scriptPubKey` podmínku, která vyžaduje, aby následující transakce poskytla důkaz o vlastnictví soukromého klíče odpovídajícího zadané bitcoinové adrese. Toho je často dosaženo skriptem, který požaduje podpis odpovídající veřejnému klíči spojenému s adresou použitou k zajištění těchto prostředků. Když se transakce pokusí použít tento UTXO jako vstup, musí poskytnout `scriptSig`, který po spojení s `scriptPubKey` splňuje nastavené podmínky a vytváří platný skript.

Například zde je klasický P2PKH `scriptPubKey`:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```

Odpovídající `scriptSig` by byl:

```text
<signature> <public key>
```

![](../../dictionnaire/assets/35.webp)

> *Toto písmo se někdy v angličtině označuje také jako "locking script"