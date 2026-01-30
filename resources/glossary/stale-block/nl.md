---
term: Stale block
definition: Geldig blok dat echter buiten de hoofdketen valt wanneer twee miners tegelijkertijd een blok op dezelfde hoogte vinden.
---

Verwijst naar een blok zonder kinderen: een geldig blok, maar uitgesloten van de Bitcoin hoofdketen. Het doet zich voor wanneer twee miners binnen een korte tijd een geldig blok op dezelfde ketenhoogte vinden en dit uitzenden over het netwerk. Knooppunten kiezen uiteindelijk slechts één blok om in de keten op te nemen, volgens het principe van de keten met het meeste geaccumuleerde werk, waardoor de andere "verouderd" wordt. Het proces dat leidt tot de productie van een verouderd blok is als volgt:


- Twee miners vinden een geldig blok op dezelfde ketenhoogte binnen een kort tijdsinterval. Laten we ze `Blok A` en `Blok B` noemen;
- Elk zendt zijn blok uit naar het Bitcoin knooppuntennetwerk. Elk knooppunt heeft nu 2 blokken op dezelfde hoogte. Er zijn dus twee geldige ketens;
- Miners gaan door met het zoeken naar werkbewijzen voor de volgende blokken, maar om dit te doen moeten ze noodzakelijkerwijs slechts één blok kiezen tussen `Blok A` en `Blok B` waarop ze gaan mijnen;
- Een Miner vindt uiteindelijk een geldig blok boven `Blok B`. Laten we het `Blok B+1` noemen;
- Ze zenden `Blok B+1` uit naar de netwerkknooppunten;
- Aangezien de knooppunten de langste keten volgen (met het meeste geaccumuleerde werk), zullen ze inschatten dat de `keten B` de keten is die gevolgd moet worden;
- Ze zullen `Blok A` verlaten, dat niet langer deel uitmaakt van de hoofdketen. Het is dus een verouderd blok geworden.





