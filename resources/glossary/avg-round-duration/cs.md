---
term: AVG. DÉLKA TRVÁNÍ KOLA

---
Průměrná doba trvání kola je ukazatel, který se používá k odhadu doby, za kterou těžební pool nalezne blok, a to na základě obtížnosti sítě a hashrate poolu. Vypočítá se tak, že se vezme počet podílů očekávaných k nalezení bloku a vydělí se hashrate poolu. Pokud má například těžební pool 200 těžařů a každý z nich vygeneruje v průměru 4 akcie za sekundu, je celkový výpočetní výkon poolu 800 akcií za sekundu:

```text
200 * 4 = 800
```

Za předpokladu, že k nalezení platného bloku je v průměru potřeba 1 milion akcií, je *Avg. Doba trvání kola* by byla 1 250 sekund, tedy přibližně 21 minut:

```text
1,000,000 / 800 = 1,250
```

V praxi to znamená, že těžební pool by měl najít blok v průměru každých přibližně 21 minut. Tento ukazatel kolísá se změnami v hashrate poolu: zvýšení hashrate snižuje *Avg. Round Duration*, zatímco jeho snížení ho prodlužuje. Bude také kolísat s každou pravidelnou úpravou cíle obtížnosti bitcoinu (každých 2016 bloků). Toto měřítko nebere v úvahu bloky nalezené jinými pooly a zaměřuje se výhradně na interní výkonnost zkoumaného poolu.