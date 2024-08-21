---
term: SEED (BITCOIN)
---

V kontextu Bitcoinu je seed 512bitová hodnota používaná k odvození všech soukromých a veřejných klíčů spojených s HD (Hierarchický Deterministický) peněženkou. Technicky je seed odlišná hodnota od obnovovací fráze (nebo mnemoniky). Tato fráze, která je typicky složena z 12 nebo 24 slov, je generována pseudo-náhodným způsobem ze zdroje entropie a doplněna kontrolním součtem. Tato fráze usnadňuje lidskou zálohu tím, že poskytuje textovou reprezentaci hodnoty na základě peněženky.

Pro získání skutečného seedu je obnovovací fráze, možná doprovázená volitelnou heslovou frází, zpracována prostřednictvím algoritmu PBKDF2 (*Password-Based Key Derivation Function 2*). Výsledkem tohoto výpočtu je 512bitový seed. Právě tento seed je použit k deterministickému generování hlavního klíče a poté celé sady klíčů pro HD peněženku v souladu s BIP32.

![](../../dictionnaire/assets/31.png)

> ► *Nicméně, v běžném jazyce většina bitcoinistů odkazuje na mnemonickou frázi, když mluví o "seedu," a nikoli na mezičlánek derivace, který leží mezi mnemonickou frází a hlavním klíčem.*