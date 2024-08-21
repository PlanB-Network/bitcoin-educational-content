---
term: SCRIPTSIG
---

Prvek v Bitcoinové transakci umístěný ve vstupech. `scriptSig` poskytuje nezbytná data k splnění podmínek nastavených `scriptPubKey` předchozí transakce, ze které jsou prostředky utraceny. Hraje tedy doplňující roli k `scriptPubKey`. Typicky `scriptSig` obsahuje digitální podpis a veřejný klíč. Podpis je generován vlastníkem bitcoinů pomocí jejich soukromého klíče a dokazuje, že mají oprávnění utratit UTXO. V tomto případě `scriptSig` demonstruje, že držitel vstupu vlastní soukromý klíč odpovídající veřejnému klíči spojenému s adresou specifikovanou v `scriptPubKey` předchozí odchozí transakce.

Když je transakce ověřena, data z `scriptSig` jsou provedena v odpovídajícím `scriptPubKey`. Pokud je výsledek platný, znamená to, že podmínky pro utrácení prostředků byly splněny. Pokud všechny vstupy transakce poskytují `scriptSig`, který validuje jejich `scriptPubKey`, transakce je platná a může být přidána do bloku pro provedení.

Například, zde je klasický P2PKH `scriptSig`:

```text
<signature> <public key>
```

Odpovídající `scriptPubKey` by byl:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```

![](../../dictionnaire/assets/35.png)

> ► *`scriptSig` je také někdy nazýván "odemčovací skript" v angličtině.*