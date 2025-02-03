---
term: BIP113

---
Zavedena změna ve výpočtu všech operací časového zámku (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` a `OP_CHECKSEQUENCEVERIFY`). Určuje, že pro vyhodnocení platnosti časových zámků se nyní musí porovnat s MTP (*Median Time Past*), což je medián časových značek posledních 11 bloků. Dříve se používala pouze časová značka předchozího bloku. Díky této metodě je systém předvídatelnější a zabraňuje manipulaci těžařů s referenčním časem. BIP113 byl zaveden prostřednictvím soft forku 4. července 2016 spolu s BIP68 a BIP112, které byly poprvé aktivovány pomocí metody BIP9.