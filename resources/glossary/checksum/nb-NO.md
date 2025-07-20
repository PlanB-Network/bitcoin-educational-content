---
term: CHECKSUM
---

Sjekksummen er en verdi som beregnes ut fra et datasett, og som brukes til å verifisere integriteten og gyldigheten til dataene under overføring eller lagring. Sjekksumalgoritmer er utviklet for å oppdage utilsiktede feil eller utilsiktede endringer av data, for eksempel overføringsfeil eller filkorrupsjon. Det finnes ulike typer sjekksumalgoritmer, for eksempel paritetssjekker, modulære sjekksummer, kryptografiske Hash-funksjoner eller BCH-koder (*Bose, Ray-Chaudhuri og Hocquenghem*).


På Bitcoin brukes sjekksummer på applikasjonsnivå for å sikre integriteten til mottaksadresser. En kontrollsum beregnes ut fra nyttelasten til en brukers Address, og legges deretter til Address for å oppdage eventuelle feil i inndataene. En sjekksum finnes også i gjenopprettingsfraser (mnemonics).


> det er vanlig å bruke det engelske begrepet "checksum" direkte på fransk