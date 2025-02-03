---
term: AKSJER

---
I forbindelse med utvinningspooler er en andel en indikator som brukes til å kvantifisere den enkelte gruvearbeiderens bidrag i poolen. Dette målet brukes som grunnlag for å beregne belønningen som utvinningspoolen omfordeler til hver utvinner. Hver share tilsvarer en hash som tilfredsstiller et vanskelighetsmål som er lavere enn Bitcoin-nettverkets.

For å forklare med en analogi, tenk på en 20-sidig terning. Anta at beviset på arbeidet med Bitcoin krever at man slår et tall lavere enn 3 for å validere en blokk (det vil si å oppnå et resultat på 1 eller 2). Tenk deg nå at vanskelighetsgraden for en andel i en utvinningspool er satt til 10. For en individuell gruvearbeider i utvinningsfellesskapet teller dermed hvert terningkast som resulterer i et tall lavere enn 10, som en gyldig andel. Disse andelene sendes deretter til utvinnerne for å kreve belønning, selv om de ikke tilsvarer et gyldig resultat for en blokk på Bitcoin.

For hver hash som beregnes, kan en individuell utvinner i en sammenslutning møte tre ulike scenarier:


- Hvis hashverdien er større enn eller lik poolens fastsatte vanskelighetsmål for en andel, er denne hashen ubrukelig. Utvinneren endrer da nonce for å forsøke en ny hash: `hash > share > block`.
- Hvis hashen er lavere enn vanskelighetsmålet for andelen, men større enn eller lik vanskelighetsmålet for Bitcoin, utgjør denne hashen en gyldig andel som imidlertid ikke er tilstrekkelig for å validere en blokk. Utgraveren kan sende denne hashen til sin pool for å kreve belønningen som er knyttet til andelen: `andel > hash > blokk`.
- Hvis hashen er lavere enn Bitcoin-nettverkets vanskelighetsmål, anses den som både en gyldig andel og en gyldig blokk. Utvinneren overfører denne hashen til sin pool, som skynder seg å kringkaste den på Bitcoin-nettverket. Denne hashen regnes også som en gyldig share for utvinneren: `share > bloc > hash`.

![](../../dictionnaire/assets/32.webp)

Dette delesystemet brukes til å estimere arbeidet som utføres av hver enkelt utvinner i en pool, uten at alle hashene som genereres av en utvinner, må beregnes på nytt, noe som ville vært fullstendig ineffektivt for poolen.

Gruvebassenger justerer vanskelighetsgraden for aksjer for å balansere verifikasjonsbelastningen og sørge for at hver gruvearbeider, uansett om den er liten eller stor, sender inn aksjer med noen få sekunders mellomrom. Dette muliggjør en nøyaktig beregning av hver gruvearbeiders hashrate og fordelingen av belønninger i henhold til den valgte metoden for kompensasjonsberegning (PPS, PPLNS, TIDES...).

> på fransk kan "shares" oversettes med "del"