---
term: (VEŘEJNÝ KLÍČ)

---
V oblasti kryptografie "vylepšování" veřejného klíče spočívá v úpravě tohoto klíče pomocí přídavné hodnoty zvané "tweak" tak, aby zůstal použitelný se znalostí původního soukromého klíče a tweaku. Technicky vzato je tweak skalární hodnota, která se přidává k původnímu veřejnému klíči. Pokud $P$ je veřejný klíč a $t$ je tweak, vznikne tweakovaný veřejný klíč:

$$
P' = P + tG
$$

Kde $G$ je generátor použité eliptické křivky. Tato operace umožňuje získat nový veřejný klíč odvozený od původního klíče při zachování určitých kryptografických vlastností, které umožňují jeho použití. Tato metoda se používá například u adres Taproot (P2TR), které umožňují utrácení buď předložením Schnorrova podpisu tradičním způsobem, nebo splněním jedné z podmínek uvedených v Merklově stromu, nazývaném také "MAST".

![](../../dictionnaire/assets/26.webp)