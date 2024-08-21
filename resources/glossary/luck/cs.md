---
term: LUCK
---

Indikátor používaný v těžebních poolech k měření výkonnosti poolu ve vztahu k jeho teoretickým očekáváním. Jak název napovídá, hodnotí štěstí poolu při hledání bloku. Štěstí (Luck) se vypočítá porovnáním počtu akcií (shares), které jsou teoreticky potřebné k nalezení platného bloku, na základě aktuální obtížnosti Bitcoinu, s aktuálním počtem akcií vyprodukovaných k nalezení tohoto bloku. Počet akcií nižší než očekávaný značí dobré štěstí, zatímco vyšší počet značí špatné štěstí.

Korelujíc obtížnost na Bitcoinu s jeho počtem akcií produkovaných každou sekundu a obtížností každé akcie, může pool vypočítat počet akcií, které jsou teoreticky nutné k nalezení platného bloku. Předpokládejme například, že teoreticky je potřeba 100 000 akcií, aby pool našel blok. Pokud pool skutečně produkuje 200 000 akcií před nalezením bloku, jeho štěstí je 50%:

```text
100,000 / 200,000 = 0.5 = 50%
```

Naopak, pokud tento pool najde platný blok po vyprodukovaní pouze 50 000 akcií, pak je jeho štěstí 200%:

```text
100,000 / 50,000 = 2 = 200%
```

Štěstí je indikátor, který lze aktualizovat pouze po objevení bloku poolem, což z něj činí statický indikátor, který se aktualizuje periodicky.