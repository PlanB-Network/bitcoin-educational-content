---
term: CHECKSUM

---
En sjekksum er en beregnet verdi fra et datasett som brukes til å verifisere integriteten og gyldigheten til dataene under overføring eller lagring. Sjekksumalgoritmer er utviklet for å oppdage utilsiktede feil eller utilsiktede endringer av data, for eksempel overføringsfeil eller filkorrupsjon. Det finnes ulike typer sjekksumalgoritmer, for eksempel paritetssjekker, modulære sjekksummer, kryptografiske hashfunksjoner eller BCH-koder (*Bose, Ray-Chaudhuri og Hocquenghem*).

I Bitcoin brukes sjekksummer på applikasjonsnivå for å sikre integriteten til mottatte adresser. En sjekksum beregnes ut fra nyttelasten til en brukers adresse, og legges deretter til denne adressen for å oppdage mulige feil under oppføringen. En sjekksum finnes også i gjenopprettingsfraser (mnemonic).

> den engelske oversettelsen av "somme de contrôle" er "sjekksum". Det er allment akseptert å bruke begrepet "sjekksum" direkte på fransk