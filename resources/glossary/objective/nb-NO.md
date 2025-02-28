---
term: MÅLSETTING

---
I deterministiske og hierarkiske (HD) lommebøker representerer formålet (eller _purpose_ på engelsk), definert av BIP43, et spesifikt avledningsnivå. Denne indeksen, som ligger på første dybde i avledningstreet (`m / purpose' /`), identifiserer avledningsstandarden som er vedtatt av lommeboken, for å lette kompatibiliteten mellom ulike lommebokadministrasjonsprogrammer. For eksempel, når det gjelder SegWit-adresser (BIP84), er målet angitt som `/84'/`. Denne metoden gjør det mulig å organisere nøkler på en effektiv måte mellom ulike typer adresser i samme HD-lommebok. Standardindeksene som brukes er


- For P2PKH: `44'`;
- For P2WPKH-nested-in-P2SH: `49'`;
- For P2WPKH: `84`;
- For P2TR: `86`.

![](../../dictionnaire/assets/20.webp)