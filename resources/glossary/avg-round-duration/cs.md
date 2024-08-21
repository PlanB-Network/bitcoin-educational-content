---
term: PRŮMĚRNÁ DOBA KOLO
---

Průměrná doba kola je ukazatel používaný k odhadu času, který je potřebný těžebnímu poolu k nalezení bloku, na základě obtížnosti sítě a hashrate poolu. Vypočítá se tak, že se vezme počet akcií (shares), které se očekávají pro nalezení bloku, a vydělí se hashrate poolu. Například, pokud má těžební pool 200 těžařů a každý z nich generuje průměrně 4 akcie za sekundu, celkový výpočetní výkon poolu je 800 akcií za sekundu:

```text
200 * 4 = 800
```

Předpokládáme-li, že průměrně je potřeba 1 milion akcií k nalezení platného bloku, *Prům. Doba Kola* poolu by byla 1 250 sekund, nebo přibližně 21 minut:

```text
1,000,000 / 800 = 1,250
```

V praktickém smyslu to znamená, že průměrně by měl těžební pool nalézt blok každých 21 minut nebo tak nějak. Tento ukazatel se mění s každou změnou hashrate poolu: zvýšení hashrate snižuje *Prům. Doba Kola*, zatímco její snížení ji prodlužuje. Bude se také měnit s každým periodickým přizpůsobením cíle obtížnosti Bitcoinu (každých 2016 bloků). Toto měření nebere v úvahu bloky nalezené jinými pooly a soustředí se výhradně na vnitřní výkon studovaného poolu.