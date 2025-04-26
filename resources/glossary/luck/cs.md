---
term: LUCK

---
Ukazatel používaný v těžebních poolech k měření výkonnosti poolu vzhledem k jeho teoretickým očekáváním. Jak název napovídá, hodnotí štěstí poolu při hledání bloku. Štěstí se vypočítá porovnáním počtu podílů teoreticky potřebných k nalezení platného bloku na základě aktuální obtížnosti bitcoinu a skutečného počtu podílů, které byly k nalezení tohoto bloku vyrobeny. Nižší počet podílů, než se očekávalo, znamená štěstí, zatímco vyšší počet podílů znamená smůlu.

Korelací obtížnosti bitcoinu s počtem jeho akcií vyrobených každou sekundu a obtížností každé akcie může pool vypočítat počet akcií, které jsou teoreticky nutné k nalezení platného bloku. Předpokládejme například, že teoreticky je potřeba 100 000 akcií, aby pool našel blok. Pokud pool před nalezením bloku skutečně vyprodukuje 200 000 akcií, jeho štěstí je 50%:

```text
100,000 / 200,000 = 0.5 = 50%
```

Naopak, pokud tento pool našel platný blok po vyprodukování pouhých 50 000 akcií, pak je jeho štěstí 200%:

```text
100,000 / 50,000 = 2 = 200%
```

Štěstí je ukazatel, který lze aktualizovat pouze po objevení bloku fondem, takže se jedná o statický ukazatel, který je pravidelně aktualizován.