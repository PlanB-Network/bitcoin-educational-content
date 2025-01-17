---
term: DERIVASJON

---
Refererer til prosessen med å generere underordnede nøkkelpar fra et overordnet nøkkelpar (privat nøkkel og offentlig nøkkel) og en kjedekode i en deterministisk og hierarkisk (HD) lommebok. Denne prosessen gjør det mulig å segmentere forgreninger og organisere en lommebok i ulike nivåer med mange underordnede nøkkelpar, som alle kan gjenopprettes ved kun å kjenne til den grunnleggende gjenopprettingsinformasjonen (den mnemoniske frasen og en eventuell passordfrase). For å utlede en underordnet nøkkel brukes `HMAC-SHA512`-funksjonen med den overordnede kjedekoden og sammenkjedningen av den overordnede nøkkelen og en 32-biters indeks. Det finnes to typer avledninger:


- Normal avledning, som bruker den overordnede offentlige nøkkelen som grunnlag for `HMAC-SHA512`-funksjonen;
- Herdet avledning, som bruker den overordnede private nøkkelen som grunnlag for `HMAC-SHA512`-funksjonen;

Resultatet av HMAC-SHA512 deles i to: De første 256 bitene blir den underordnede nøkkelen (privat eller offentlig etter behandling gjennom ECDSA), og de resterende 256 bitene blir den underordnede kjedekoden.