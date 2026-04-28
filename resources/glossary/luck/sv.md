---
term: Luck
definition: Indikator som mäter prestandan hos en miningpool jämfört med teoretiska förväntningar.
---

En indikator som används i Mining-pooler för att mäta en pools prestanda i förhållande till dess teoretiska förväntningar. Som namnet antyder utvärderar den poolens tur när det gäller att hitta ett block. Lyckan beräknas genom att jämföra det antal andelar som teoretiskt behövs för att hitta ett giltigt block, baserat på den aktuella svårighetsgraden i Bitcoin, med det faktiska antalet andelar som producerats för att hitta det blocket. Ett lägre antal andelar än förväntat tyder på tur, medan ett högre antal andelar tyder på otur.


Genom att korrelera svårighetsgraden på Bitcoin med antalet aktier som produceras varje sekund och svårighetsgraden för varje aktie kan poolen beräkna antalet aktier som teoretiskt sett krävs för att hitta ett giltigt block. Anta till exempel att det teoretiskt sett krävs 100 000 andelar för att en pool ska hitta ett block. Om poolen faktiskt producerar 200.000 innan den hittar ett block, är dess tur 50%:


```text
100,000 / 200,000 = 0.5 = 50%
```


Omvänt, om denna pool hittade ett giltigt block efter att bara ha producerat 50 000 aktier, är dess tur 200%:


```text
100,000 / 50,000 = 2 = 200%
```


Luck är en indikator som bara kan uppdateras efter att ett block har upptäckts av poolen, vilket gör den till en statisk indikator som uppdateras regelbundet.