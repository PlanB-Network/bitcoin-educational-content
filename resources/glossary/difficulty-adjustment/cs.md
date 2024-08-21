---
term: ÚPRAVA OBTÍŽNOSTI
---

Úprava obtížnosti je periodický proces, který předefinuje cílovou obtížnost pro mechanismus důkazu práce (těžbu) na Bitcoinu. Tato událost nastává každých 2016 bloků (přibližně každé dva týdny). Slouží k zvýšení nebo snížení faktoru obtížnosti (také nazývaného cílová obtížnost), v závislosti na tom, jak rychle byly poslední 2016 bloků nalezeny. Úprava má za cíl udržet stabilní a předvídatelnou rychlost produkce bloků, s frekvencí jednoho bloku každých 10 minut, navzdory variacím v výpočetním výkonu nasazeném těžaři. Změna obtížnosti během úpravy je omezena na faktor 4. Formule, kterou uzly provádějí pro výpočet nového cíle, je následující:
$$N = A \cdot \left(\frac{T}{1,209,600}\right)$$
&nbsp;
Kde:
* $N$: Nový cíl;
* $A$: Starý cíl posledních 2016 bloků;
* $T$: Celkový skutečný čas posledních 2016 bloků ve vteřinách;
* $1,209,600$: Cílový čas ve vteřinách pro produkci 2016 bloků s 10minutovým intervalem mezi každým.

> ► *Ve francouzštině se termín "reciblage" někdy také používá pro označení úpravy. V angličtině se tomu říká "Difficulty Adjustment".*