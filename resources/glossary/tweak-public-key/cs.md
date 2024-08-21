---
term: TWEAK (VEŘEJNÝ KLÍČ)
---

V oblasti kryptografie "tweaking" (úprava) veřejného klíče zahrnuje modifikaci tohoto klíče použitím přídavné hodnoty nazývané "tweak" (úprava), tak aby byl stále použitelný s vědomím původního soukromého klíče a úpravy. Technicky je úprava skalární hodnota, která je přidána k původnímu veřejnému klíči. Pokud je $P$ veřejný klíč a $t$ je úprava, upravený veřejný klíč se stává:

$$
P' = P + tG
$$

Kde $G$ je generátor eliptické křivky použité. Tato operace umožňuje získání nového veřejného klíče odvozeného z původního klíče, přičemž si zachovává určité kryptografické vlastnosti, které jej činí použitelným. Například, tato metoda je používána pro adresy Taproot (P2TR) k umožnění výdajů buď prezentací Schnorr podpisu tradičním způsobem nebo splněním jedné z podmínek uvedených v Merkleově stromu, také nazývaném "MAST".

![](../../dictionnaire/assets/26.png)