---
term: BIP113
---

Zavedl změnu ve výpočtu všech operací s časovým zámkem (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` a `OP_CHECKSEQUENCEVERIFY`). Specifikuje, že pro hodnocení platnosti časových zámků musí být nyní porovnávány s MTP (*Median Time Past*, medián času posledních 11 bloků), což je medián časových razítek posledních 11 bloků. Dříve bylo používáno pouze časové razítko předchozího bloku. Tato metoda činí systém předvídatelnějším a zabraňuje manipulaci s časovým referencem těžaři. BIP113 byl zaveden prostřednictvím měkké vidlice (soft fork) 4. července 2016 společně s BIP68 a BIP112, aktivován poprvé použitím metody BIP9.