---
term: SEED (BITCOIN)

---
V kontextu Bitcoinu je seed 512bitová hodnota, která se používá k odvození všech soukromých a veřejných klíčů přidružených k peněžence HD (Hierarchical Deterministic). Technicky vzato je seed jiná hodnota než fráze pro obnovení (nebo mnemotechnická fráze). Fráze, která se obvykle skládá z 12 nebo 24 slov, je generována pseudonáhodným způsobem ze zdroje entropie a doplněna kontrolním součtem. Tato fráze usnadňuje zálohování člověku tím, že poskytuje textovou reprezentaci hodnoty v základu peněženky.

Pro získání skutečného seedu je obnovovací fráze, případně doplněná volitelnou přístupovou frází, zpracována algoritmem PBKDF2 (*Password-Based Key Derivation Function 2*). Výsledkem tohoto výpočtu je 512bitový seed. Právě tento seed se používá k deterministickému generování hlavního klíče a poté celé sady klíčů pro peněženku HD v souladu s BIP32.

![](../../dictionnaire/assets/31.webp)

> *V běžném jazyce však většina bitcoinářů mluví o mnemotechnické frázi, když hovoří o "seedu", a nikoli o mezistavu derivace, který leží mezi mnemotechnickou frází a hlavním klíčem.*