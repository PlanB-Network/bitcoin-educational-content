---
term: SCRIPTSIG

---
Prvek v transakci Bitcoin umístěný ve vstupech. `scriptSig` poskytuje údaje nezbytné pro splnění podmínek stanovených `scriptPubKey` předchozí transakce, z níž jsou prostředky utráceny. Hraje tedy doplňkovou roli k `scriptPubKey`. Obvykle `scriptSig` obsahuje digitální podpis a veřejný klíč. Podpis generuje vlastník bitcoinů pomocí svého soukromého klíče a dokazuje, že má oprávnění utrácet UTXO. V tomto případě `scriptSig` prokazuje, že držitel vstupu vlastní soukromý klíč odpovídající veřejnému klíči spojenému s adresou uvedenou v `scriptPubKey` předchozí odchozí transakce.

Když je transakce ověřena, data z `scriptSig` se provedou v odpovídajícím `scriptPubKey`. Pokud je výsledek platný, znamená to, že byly splněny podmínky pro vydání prostředků. Pokud všechny vstupy transakce poskytují `scriptSig`, který ověřuje jejich `scriptPubKey`, je transakce platná a může být přidána do bloku k provedení.

Například zde je klasický P2PKH `scriptSig`:

```text
<signature> <public key>
```

Odpovídající `scriptPubKey` by byl:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```

![](../../dictionnaire/assets/35.webp)

> ► *SkriptSig` se někdy v angličtině nazývá také "odemykací skript".*