---
term: PŘIZPŮSOBENÍ OBTÍŽNOSTI

---
Úprava obtížnosti je periodický proces, který nově definuje cíl obtížnosti pro mechanismus důkazu práce (těžby) v bitcoinech. K této události dochází každých 2016 bloků (přibližně každé dva týdny). Slouží ke zvýšení nebo snížení faktoru obtížnosti (nazývaného také cíl obtížnosti) v závislosti na tom, jak rychle byly nalezeny poslední bloky z roku 2016. Cílem úpravy je udržet stabilní a předvídatelnou míru produkce bloků s frekvencí jeden blok každých 10 minut, a to i přes výkyvy ve výpočetním výkonu nasazeném těžaři. Změna obtížnosti během úpravy je omezena na faktor 4. Vzorec prováděný uzly pro výpočet nového cíle je následující:

$$N = A \cdot \left(\frac{T}{1,209,600}\right)$$

&nbsp;

Kde:


- $N$: Nový cíl;
- $A$: Starý cíl posledních bloků z roku 2016;
- $T$: Celkový skutečný čas posledních 2016 bloků v sekundách;
- $1,209,600$: Cílová doba v sekundách pro vytvoření 2016 bloků s intervalem 10 minut mezi jednotlivými bloky.

> ► Ve francouzštině se někdy pro úpravu používá také výraz "reciblage". V angličtině se označuje jako "Difficulty Adjustment "*