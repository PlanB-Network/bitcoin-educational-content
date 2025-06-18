---
term: MÅLSETTING
---

I deterministiske og hierarkiske (HD) porteføljer representerer formålet, definert av BIP43, et spesifikt avledningsnivå. Denne indeksen, som ligger på første dybde i avledningstreet (`m / purpose' /`), identifiserer avledningsstandarden som porteføljen har tatt i bruk, for å gjøre det lettere å oppnå kompatibilitet mellom ulike porteføljeadministrasjonsprogrammer. For SegWit-adresser (BIP84) er for eksempel formålet angitt som `/84'/`. Denne metoden gjør det mulig å organisere nøkler effektivt mellom ulike Address-typer innenfor en enkelt HD-portefølje. Standardindeksene som brukes er :




- For P2PKH: `44'` ;
- For P2WPKH-innleiret i P2SH: `49'` ;
- For P2WPKH: `84'` ;
- For P2TR: `86``.