---
term: Gemiddelde ronde duur
definition: Een indicator die de gemiddelde tijd schat die een mijngroep nodig heeft om een blok te vinden, op basis van zijn rekenkracht en netwerkmoeilijkheid.
---

De gemiddelde duur van een ronde is een indicator die gebruikt wordt om de tijd in te schatten die een Mining pool nodig heeft om een blok te vinden, gebaseerd op de moeilijkheidsgraad van het netwerk en de Hashrate van de pool. Het wordt berekend door het aantal aandelen te nemen dat verwacht wordt om een blok te vinden en dit te delen door de Hashrate van de pool. Als een Mining pool bijvoorbeeld 200 miners heeft, en elk genereert gemiddeld 4 aandelen per seconde, dan is de totale rekenkracht van de pool 800 aandelen per seconde:


```text
200 * 4 = 800
```


Ervan uitgaande dat het gemiddeld 1 miljoen aandelen kost om een geldig blok te vinden, zou de *Avg. Round Duration* 1.250 seconden zijn, of ongeveer 21 minuten:


```text
1,000,000 / 800 = 1,250
```


Praktisch gezien betekent dit dat de Mining pool gemiddeld elke 21 minuten een blok zou moeten vinden. Deze indicator fluctueert met veranderingen in de Hashrate van de pool: een toename in Hashrate verlaagt de *Avg. Round Duration*, terwijl een verlaging hem verlengt. Het zal ook fluctueren met elke periodieke aanpassing van het Bitcoin moeilijkheidsdoel (elke 2016 blokken). Deze meting houdt geen rekening met blokken die gevonden zijn door andere pools en richt zich alleen op de interne prestaties van de bestudeerde pool.