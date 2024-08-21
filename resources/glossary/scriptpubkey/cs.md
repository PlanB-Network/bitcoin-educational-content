---
term: SCRIPTPUBKEY
---

Skript umístěný v výstupní části Bitcoinové transakce, který definuje podmínky, za kterých lze přidružený UTXO utratit. Tento skript tak zabezpečuje bitcoiny. Ve své nejběžnější formě obsahuje `scriptPubKey` podmínku, která vyžaduje, aby následující transakce poskytla důkaz o vlastnictví soukromého klíče odpovídajícího určené Bitcoinové adrese. To je často dosaženo skriptem, který vyžaduje podpis odpovídající veřejnému klíči spojenému s adresou použitou k zabezpečení těchto prostředků. Když transakce pokusí použít tento UTXO jako vstup, musí poskytnout `scriptSig`, který, jakmile je zkombinován se `scriptPubKey`, splní stanovené podmínky a produkuje platný skript.

Například, zde je klasický P2PKH `scriptPubKey`:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <adresa> OP_EQUALVERIFY OP_CHECKSIG
```

Odpovídající `scriptSig` by byl:

```text
<podpis> <veřejný klíč>
```

![](../../dictionnaire/assets/35.png)

> ► *Tento skript je také někdy označován jako "zamykací skript" v angličtině.*