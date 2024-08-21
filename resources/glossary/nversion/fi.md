---
termi: NVERSION
---

`nVersion`-kenttä Bitcoin-siirrossa käytetään ilmaisemaan käytössä olevan siirtomuodon version. Se mahdollistaa verkon erottaa eri aikakausien siirtomuotojen kehitykset toisistaan ja soveltaa vastaavia sääntöjä. Tällä kentällä ei ole vaikutusta konsensus-sääntöihin. Tämä tarkoittaa, että mihin tahansa arvoon, joka on annettu tälle kentälle, ei johda siirron mitätöintiin. Kuitenkin `nVersion`-kentällä on standardisointisääntöjä, jotka tällä hetkellä hyväksyvät vain arvot `1` ja `2`. Toistaiseksi tämä kenttä on hyödyllinen vain `nSequence`-kentän aktivoinnissa.