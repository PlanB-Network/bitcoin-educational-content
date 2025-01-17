---
term: P2WPKH

---
P2WPKH står for *Pay to Witness Public Key Hash*. Det er en standard skriptmodell som brukes til å etablere utgiftsbetingelser på en UTXO. P2WPKH ble introdusert med implementeringen av SegWit i august 2017.

Dette skriptet ligner på P2PKH (*Pay to Public Key Hash*), ettersom det også låser bitcoins basert på hashen til en offentlig nøkkel, det vil si en mottakeradresse. Forskjellen ligger i hvordan signaturer og skript inkluderes i transaksjonen. I P2WPKH flyttes informasjonen om signaturskriptet (`scriptSig`) fra den tradisjonelle transaksjonsstrukturen til en egen seksjon kalt `Witness`. Denne flyttingen er en del av SegWit-oppdateringen (*Segregated Witness*), som bidrar til å forhindre forfalskning av signaturer. P2WPKH-transaksjoner er generelt billigere i gebyrer sammenlignet med Legacy-transaksjoner, ettersom delen i vitnet koster mindre.

P2WPKH-adresser skrives ved hjelp av `Bech32`-koding med en kontrollsum i form av BCH-kode. Disse adressene starter alltid med `bc1q`. P2WPKH er en versjon 0 SegWit-utgang.