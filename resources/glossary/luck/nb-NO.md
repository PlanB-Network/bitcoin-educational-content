---
term: LYKKE

---
En indikator som brukes i utvinningspooler for å måle poolens ytelse i forhold til de teoretiske forventningene. Som navnet antyder, evaluerer den poolens flaks med å finne en blokk. Flaks beregnes ved å sammenligne antallet aksjer som teoretisk sett trengs for å finne en gyldig blokk, basert på Bitcoins nåværende vanskelighetsgrad, med det faktiske antallet aksjer som produseres for å finne den aktuelle blokken. Et lavere antall aksjer enn forventet indikerer flaks, mens et høyere antall indikerer uflaks.

Ved å korrelere vanskelighetsgraden på Bitcoin med antall aksjer som produseres hvert sekund og vanskelighetsgraden til hver aksje, kan poolen beregne hvor mange aksjer som teoretisk sett er nødvendig for å finne en gyldig blokk. Anta for eksempel at det i teorien tar 100 000 aksjer for en pool å finne en blokk. Hvis bassenget faktisk produserer 200 000 før det finner en blokk, har det 50 % flaks:

```text
100,000 / 200,000 = 0.5 = 50%
```

Hvis dette utvalget derimot fant en gyldig blokk etter bare å ha produsert 50 000 aksjer, er lykken 200 %:

```text
100,000 / 50,000 = 2 = 200%
```

Luck er en indikator som bare kan oppdateres etter at en blokk er oppdaget av poolen, noe som gjør den til en statisk indikator som oppdateres med jevne mellomrom.