---
term: BLOCKS/REV*.DAT

---
Navn på filene i Bitcoin Core som lagrer informasjonen som trengs for å potensielt reversere endringene som er gjort i UTXO-settet av tidligere tilførte blokker. Hver fil identifiseres med et unikt nummer som er det samme som blk*.dat-filen den tilsvarer. Rev*.dat-filene inneholder reverseringsdataene som tilsvarer blokkene som er lagret i blk*.dat-filene. Disse dataene er i hovedsak en liste over alle UTXO-ene som er brukt som innganger i en blokk. Disse reverseringsfilene gjør det mulig for noden å gå tilbake til en tidligere tilstand i tilfelle en omorganisering av blokkjeden fører til at tidligere validerte blokker blir forkastet.