---
term: P2WSH

---
P2WSH står for *Pay to Witness Script Hash*. Det er en standard skriptmodell som brukes til å etablere utgiftsbetingelser på en UTXO. P2WSH ble introdusert med implementeringen av SegWit i august 2017.

Dette skriptet ligner på P2SH (*Pay to Public Script Hash*), ettersom det også låser bitcoins basert på hashen til et skript. Forskjellen ligger i hvordan signaturer og skript inkluderes i transaksjonen. For å bruke bitcoins på denne typen skript må mottakeren levere det opprinnelige skriptet, kalt `witnessScript` (tilsvarende `redeemScript`), sammen med de nødvendige signaturene. Denne mekanismen gjør det mulig å implementere mer sofistikerte bruksbetingelser, for eksempel multisig.

I P2WSH-sammenheng er informasjonen om signaturskriptet (`scriptWitness`, tilsvarende `scriptSig`) flyttet fra den tradisjonelle transaksjonsstrukturen til en egen seksjon kalt `Witness`. Denne flyttingen er en del av SegWit-oppdateringen (*Segregated Witness*), som bidrar til å forhindre forfalskning av signaturer. P2WSH-transaksjoner er generelt billigere i gebyrer sammenlignet med Legacy-transaksjoner, ettersom delen i vitnet koster mindre.

P2WSH-adresser skrives ved hjelp av `Bech32`-koding med en kontrollsum i form av BCH-kode. Disse adressene starter alltid med `bc1q`. P2WSH er en versjon 0 SegWit-utgang.