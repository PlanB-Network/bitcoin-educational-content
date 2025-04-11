---
term: NVERSION

---
Feltet `nVersion` i en Bitcoin-transaksjon brukes til å angi hvilken versjon av transaksjonsformatet som brukes. Det gjør det mulig for nettverket å skille mellom ulike versjoner av transaksjonsformatet over tid og å bruke de tilsvarende reglene. Dette feltet har ingen innvirkning på konsensusreglene. Det betyr at en hvilken som helst verdi i dette feltet ikke fører til at transaksjonen blir ugyldiggjort. Feltet `nVersion` har imidlertid standardiseringsregler som for øyeblikket bare godtar verdiene `1` og `2`. Inntil videre er dette feltet bare nyttig for aktivering av feltet `nSequence`.