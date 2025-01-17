---
term: P2SH

---
P2SH står for *Pay to Script Hash*. Det er en standard skriptmodell som brukes til å etablere utgiftsbetingelser på en UTXO. I motsetning til P2PK- og P2PKH-skript, der utgiftsbetingelsene er forhåndsdefinert, gjør P2SH det mulig å integrere vilkårlige utgiftsbetingelser og tilleggsfunksjoner i et transaksjonsskript.

Teknisk sett inneholder `scriptPubKey` i en P2SH-transaksjon den kryptografiske hashen til en `redeemScript`, i stedet for eksplisitte utgiftsbetingelser. Denne hashen oppnås ved hjelp av en `SHA256`-hash. Når du sender bitcoins til en P2SH-adresse, avsløres ikke den underliggende `redeemScript`. Bare hashen er inkludert i transaksjonen. P2SH-adresser er kodet i `Base58Check` og starter med tallet `3`. Når mottakeren ønsker å bruke de mottatte bitcoinsene, må de oppgi en `redeemScript` som samsvarer med hashen i `scriptPubKey`, sammen med de nødvendige dataene for å oppfylle betingelsene i denne `redeemScript`. I et P2SH-skript med flere signaturer kan skriptet for eksempel kreve signaturer fra flere private nøkler.

Bruken av P2SH gir større fleksibilitet, ettersom det gjør det mulig å lage vilkårlige skript uten at avsenderen kjenner til detaljene. P2SH ble introdusert i 2012 med BIP16.