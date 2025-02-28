---
term: FORLENGET NØKKEL

---
En sekvens av tegn som kombinerer en nøkkel (offentlig eller privat), den tilhørende kjedekoden og en rekke metadata. En utvidet nøkkel samler alle elementene som er nødvendige for å utlede underordnede nøkler, i én enkelt identifikator. De brukes i deterministiske og hierarkiske lommebøker og kan være av to typer: en utvidet offentlig nøkkel (som brukes til å utlede underordnede offentlige nøkler) eller en utvidet privat nøkkel (som brukes til å utlede både underordnede private og offentlige nøkler). En utvidet nøkkel inneholder dermed flere forskjellige data, beskrevet i BIP32, i følgende rekkefølge:


- Prefikset: `prv` og `pub` er HRP (Human Readable Part) som indikerer om det er en utvidet privat nøkkel (`prv`) eller en utvidet offentlig nøkkel (`pub`). Den første bokstaven i prefikset angir versjonen av den utvidede nøkkelen: `x` for Legacy eller SegWit V1 på Bitcoin, `t` for Legacy eller SegWit V1 på Bitcoin Testnet, `y` for Nested SegWit på Bitcoin, `u` for Nested SegWit på Bitcoin Testnet, `z` for SegWit V0 på Bitcoin, `v` for SegWit V0 på Bitcoin Testnet.
- Dybden, som angir antall avledninger fra hovednøkkelen for å nå den utvidede nøkkelen;
- Det overordnede fingeravtrykket. Dette representerer de første 4 byte av `HASH160` av den overordnede offentlige nøkkelen;
- Indeksen. Dette er nummeret til paret blant søsknene som den utvidede nøkkelen er avledet fra;
- Kjedekoden;
- En utfyllingsbyte hvis det er en privat nøkkel `0x00`;
- Den private eller offentlige nøkkelen;
- En sjekksum. Den representerer de første 4 byte av `HASH256` av resten av den utvidede nøkkelen.

I praksis brukes den utvidede offentlige nøkkelen til å generere mottakeradresser og til å observere transaksjonene til en konto uten å eksponere de tilhørende private nøklene. Dette kan for eksempel gjøre det mulig å opprette en såkalt "watch-only"-lommebok. Det er imidlertid viktig å merke seg at den utvidede offentlige nøkkelen er sensitiv informasjon for brukerens personvern, ettersom avsløring av den kan gjøre det mulig for tredjeparter å spore transaksjoner og se saldoen på den tilknyttede kontoen.