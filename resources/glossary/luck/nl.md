---
term: Luck
definition: Indicator die de prestaties van een mining pool meet in vergelijking met theoretische verwachtingen.
---

Een indicator die gebruikt wordt in Mining pools om de prestatie van een pool te meten ten opzichte van de theoretische verwachtingen. Zoals de naam al zegt, evalueert het het geluk van de pool bij het vinden van een blok. Geluk wordt berekend door het aantal aandelen dat theoretisch nodig is om een geldig blok te vinden, gebaseerd op de huidige moeilijkheidsgraad van Bitcoin, te vergelijken met het werkelijke aantal aandelen dat geproduceerd werd om dat blok te vinden. Een lager aantal aandelen dan verwacht wijst op veel geluk, terwijl een hoger aantal wijst op pech.


Door de moeilijkheid op Bitcoin te correleren met het aantal aandelen dat elke seconde geproduceerd wordt en de moeilijkheid van elk aandeel, kan de pool het aantal aandelen berekenen dat theoretisch nodig is om een geldig blok te vinden. Stel bijvoorbeeld dat een pool theoretisch 100.000 aandelen nodig heeft om een blok te vinden. Als de pool daadwerkelijk 200.000 aandelen produceert voordat hij een blok vindt, dan heeft hij 50% geluk:


```text
100,000 / 200,000 = 0.5 = 50%
```


Omgekeerd, als deze pool een geldig blok vond na slechts 50.000 aandelen te hebben geproduceerd, dan is zijn geluk 200%:


```text
100,000 / 50,000 = 2 = 200%
```


Geluk is een indicator die alleen kan worden bijgewerkt nadat een blok is ontdekt door de pool, waardoor het een statische indicator is die periodiek wordt bijgewerkt.