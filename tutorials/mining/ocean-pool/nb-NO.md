---
name: Ocean Mining

description: Introduksjon til Havgruvedrift
---

![signup](assets/cover.webp)

**Mai 2024**

Ocean Mining er en noe unik gruvepool. Her kreves ingen kontoer, ingen e-postadresser, ingen passord. Akkurat som med Bitcoin, er alt transparent, pseudonymt, og bidragsytere kan velge mellom fire forskjellige blokkmaler.

### Kompensasjonssystem

Kompensasjonssystemet til Ocean kalles TIDES, "Transparent Index of Distinct Extended Shares". Dette systemet registrerer arbeidet levert av gruvearbeiderne, kjent som "shares". Bassenget beregner prosentandelen av "shares" for hver bidragsyter, deretter legges deres Bitcoin-adresse inn i bassengets blokkmal som mottaker av denne prosentandelen av blokkbelønningen.

Blokkmalen oppdateres omtrent hvert 10. sekund for å ta hensyn til de mest lønnsomme nye transaksjonene og for å endre fordelingen av blokkbelønningen om nødvendig.

![signup](assets/rem.webp)

Om dine maskiner er tilkoblet eller ikke på tidspunktet bassenget miner en ny blokk spiller ingen rolle. Arbeidet som allerede er sendt inn, beholdes for de neste åtte blokkene funnet av bassenget.

Å beholde arbeidet for åtte blokker i stedet for å tilbakestille tellerne til null med hver nye blokk som mines, betyr at kompensasjonen din kun vil være 100% når bassenget har funnet åtte blokker etter at du begynte å bidra. Dette betyr også at du vil fortsette å bli kompensert for åtte blokker hvis du slutter å bidra til bassenget.

Denne mekanismen jevner ut kompensasjonen og motvirker "pool hopping", som innebærer å bytte bassenger regelmessig avhengig av hvilket som mest sannsynlig vil finne den neste blokken.

### Uttak

Driften av Ocean Mining tillater bidragsyterne å gjenopprette "rene" bitcoins, noe som betyr bitcoins som er direkte utstedt av blokkbelønningen.

I motsetning til flertallet av andre bassenger, mottar ikke Ocean de nyutvunne bitcoinene; bidragsyternes adresser er direkte integrert i blokkmalen.

For øyeblikket er det minste beløpet for å virkelig dra nytte av de rene bitcoinene 1,048,576 sats. Med hver blokk som mines av bassenget, må din andel av "shares" gi deg rett til mer enn 1,048,576 sats for at de skal betales direkte til deg av blokkbelønningen.
Ellers vil dine sats bli holdt av Ocean til dine totale belønninger overstiger dette beløpet.

Alle bitcoins som midlertidig holdes av Ocean er på denne adressen: [37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n, alt er verifiserbart på TimeChain.](https://mempool.space/address/37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n)
Det er også mulig å ta ut dine sats via Lightning ved bruk av BOLT12. Vi vil se hvordan dette settes opp.

### Bassengavgifter

Avgiftene varierer fra 0% til 2% avhengig av den valgte blokkmalen.

## Gjennomsiktigheten til Ocean

### Bidragsyterdata

![signup](assets/1.webp)

All informasjon om bassenget er transparent, inkludert alle brukerdata. For å forstå dette punktet, la oss ta et eksempel:

[På Ocean-dashboardet](https://ocean.xyz/dashboard) har du mange informasjonsbiter som hashraten over de siste seks månedene, antall deltakere i bassenget, det totale antallet bitcoins som er utvunnet, osv.

Vi vil fokusere på "Bidragsytere"-seksjonen. Du kan se listen over alle bidragsytere med deres gjennomsnittlige hashrate over de siste tre timene samt prosentandelen av **"shares"** og **"hash"** i forhold til resten av bassenget.
**"Shares %"** er prosentandelen av arbeidet levert av bidragsyteren i vinduet av de siste åtte blokkene sammenlignet med resten av bassenget.
**"Hash %"** er prosentandelen av gjennomsnittlig hashrate levert av bidragsyteren over de siste tre timene sammenlignet med resten av bassenget.

![signup](assets/2.webp)

Du vil legge merke til at "Bidragsytere" er identifisert ved en Bitcoin-adresse. Du kan klikke på noen av disse adressene for flere detaljer.

Hvis vi tar den første, den med høyest hashrate [1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ](https://ocean.xyz/stats/1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ), kan du se alle detaljene om denne brukeren: hashrate, antall bitcoins utvunnet, med hvilken blokk, og til og med detaljene om hver av deres maskiner (ASICs). Imidlertid forblir de anonyme, som på Bitcoin.

### Blokkmal

Øverst til venstre på dashbordet har du "Neste blokk". På denne siden er det fire forskjellige blokkmaler. Ocean tillater hver bidragsyter å velge blokkmalen de ønsker å støtte. Dette har ikke direkte innvirkning på kompensasjonen din. Når bassenget utvinner en blokk, blir alle bidragsytere kompensert uavhengig av malen de har valgt. Dette lar rett og slett alle "stemme" for blokkmalen som passer dem.

![signup](assets/3.webp)

**CORE:** Avgift 2%, dette er den klassiske Bitcoin Core-malen uten filter, som skrevet på deres side "Inkluderer transaksjoner og flertallet av spam"

**CORE+ANTISPAM:** Avgift 0%, Bitcoin Core med et filter mot visse transaksjoner som Ordinals "Inkluderer transaksjoner og begrenser spam"

**OCEAN:** Avgift 0%, Bitcoin Knot "Inkluderer kun transaksjoner og rimelig små data"

**DATA-FREE:** Avgift 0%, Bitcoin Knot "Inkluderer kun transaksjoner uten noen vilkårlige data"

### Forskjellen mellom Bitcoin Core og Bitcoin Knot
Bitcoin Core er programvaren som muliggjør omtrent 99% av Bitcoin-noder rundt om i verden for å operere. Bitcoin er et protokoll, noe som betyr at, akkurat som Internett, der det er flere nettlesere, kan det være flere forskjellige programvareprogrammer som samexisterer på samme TimeChain. Imidlertid, av hensyn til kompatibilitet og for å begrense risikoen for feil som ville etterlate uutslettelige spor på TimeChain, jobber nesten alle Bitcoin-utviklere på Bitcoin Core. Bitcoin Knots er en forgrening av Bitcoin Core, noe som betyr at den deler flertallet av deres kode, noe som sterkt begrenser risikoen for feil. Denne forgreningen ble opprettet av Luke Dashjr, som ønsket å anvende mer restriktive regler enn Bitcoin Core uten å skape en hard fork. Nå eksisterer Bitcoin Core og Bitcoin Knots takket være Nakamoto-konsensus.

## Legge til en Arbeider

For å legge til en arbeider, start med å velge din blokkmal. Dette valget vil bestemme basseng-URLen du skal angi på din miner (ASICs).

- **CORE**: `stratum+tcp://core.mine.ocean.xyz:3202`
- **CORE+ANTISPAM**: `stratum+tcp://ordis.mine.ocean.xyz:3303`
- **OCEAN**: `stratum+tcp://mine.ocean.xyz:3334`
- **DATA-FREE**: `stratum+tcp://datafree.mine.ocean.xyz:3404`

Deretter, for brukerfeltet, angi en Bitcoin-adresse du eier. Her er listen over kompatible adressetyper:
- **P2PKH** (Original adressetype. Begynner med “1”)
- **P2SH** (Multisignatur eller P2SH-Segwit. Starter med “3”)
- **Bech32** (Segwit. Starter med “bc”.)
- **Bech32m** (Taproot. Starter med “bc”. Lengre enn Bech32.)

Hvis du har flere minere, kan du angi samme adresse for alle slik at hash-ratene deres kombineres og vises som en enkelt miner. Du kan også skille dem ved å legge til et distinkt navn til hver. For å gjøre dette, legg ganske enkelt til “.arbeidernavn” etter Bitcoin-adressen.

Til slutt, for passordfeltet, bruk `x`.

**Eksempel:**
Hvis du velger **OCEAN**-malen, er Bitcoin-adressen din `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv` og du ønsker å navngi din miner “Brrrr”, da må du angi følgende informasjon i grensesnittet til din miner:

- **URL**: `stratum+tcp://mine.ocean.xyz:3334`
- **BRUKER**: `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr`
- **PASSORD**: `x`

Noen minutter etter at du har startet mining, vil du kunne se dataene dine på Ocean-nettstedet ved å søke etter adressen din.

### Oversikt over Dashboard
- **Andeler i Belønningsvindu**: Disse dataene indikerer antall andeler, arbeidet du har sendt til bassenget i vinduet for de siste 8 blokkene som er minet av bassenget.
- **Estimerte Belønninger i Vindu**: Estimat av antall sats du vil tjene med arbeidet som allerede er gjort. Dette tar ikke hensyn til transaksjonsgebyrer, men kun coinbase, de nye bitcoinene utstedt av nettverket.
- **Estimerte Inntekter Neste Blokk**: Estimat av antall sats tjent hvis en blokk blir minet nå. Husk, hvis denne verdien er mindre enn 1,048,576 sats, vil du ikke direkte motta satsene til adressen din. De vil bli sendt til Oceans adresse til dine inntekter overstiger denne terskelen.

Nedenfor har du et diagram som viser din hashrate-historikk opptil 6 måneder.

![signup](assets/4.webp)

Her har du din gjennomsnittlige hashrate over forskjellige tidsrammer, fra 60s til 24h, samt historikken til blokker minet av bassenget som du har bidratt til og blitt belønnet for.

![signup](assets/5.webp)

Du har muligheten til å eksportere en CSV-fil av denne historikken med **Last ned CSV**-knappen.

![signup](assets/6.webp)

I følgende seksjon har du en liste over alle minerne du har koblet til bassenget med denne adressen. Du har selvfølgelig deres individuelle hashrate, men også antall sats de individuelt har mottatt for sitt arbeid.

![signup](assets/7.webp)

Du kan klikke på **Kallenavn** til en hvilken som helst miner. Du vil da ha all informasjonen vi nettopp så, men spesifikt for den mineren.

Og nederst på siden, noe tilleggsinformasjon hvor du kan se historikken til utbetalinger på adressen din, satsene du har minet men ikke ennå blitt betalt, og totalt antall sats du har minet.

![signup](assets/8.webp)

Her kan du se at i **Estimert Tid Til Minimum Utbetaling**-boksen, står det skrevet Lightning fordi vi har satt opp et BOLT12-tilbud.

### Oppsett av Lightning Uttak
Som du har forstått, har Ocean som mål å maksimere gjennomsiktighet og minimere forvaring (å holde dine sats på dine vegne).
Derfor er det nødvendig å bruke **BOLT12 tilbud** for Lightning-uttak. Dette er en ny måte å gjøre en betaling på Lightning-nettverket som begynner å dukke opp i 2024 og tillater flere ting:
- Det er en gjenbrukbar betalingslenke, som tillater automatiske betalinger og, i motsetning til en Lightning-adresse, er BOLT12 ikke-forvaring.
- Det er også en betalingsmetode som gir bevis på at betalingen ble gjort, noe som ikke er tilfellet med LNURLs.
- Veldig viktig, den kan brukes i forbindelse med en Bitcoin-signatur for å bevise at du er både innehaveren av BTC-adressen og BOLT12-tilbudet.
Per i dag (mai 2024), finnes det få løsninger for å bruke denne metoden. I dette eksemplet vil vi bruke en Start9-server med Core Lightning. Når andre verktøy, som for eksempel Phoenix Wallet, har integrert BOLT12-tilbud, vil denne opplæringen fortsatt være aktuell. Sørg for at du har åpne kanaler med innkommende likviditet, ellers vil ikke betalinger fungere.

Start med å gå til dashbordet ditt på Ocean-nettstedet ved å angi din BTC-adresse, deretter klikk på **Configuration**-fanen.

![signup](assets/9.webp)

Vi vil kopiere **Description**-teksten, her:
`OCEAN Utbetalinger for bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`

Gå nå til Core Lightning-grensesnittet på din Start9-server (eller hvilken som helst lommebok som er i stand til å tilby et BOLT12-tilbud).

![signup](assets/10.webp)

Klikk på **Receive**.

Sjekk **Offer**, deretter lim inn den tidligere kopierte teksten i **Description**-feltet og la **Amount**-feltet stå tomt.

![signup](assets/11.webp)

Klikk på **Generate Offer**.

![signup](assets/12.webp)

Du har generert en gjenbrukbar og permanent betalingslenke som ikke krever en sentral server, som er tilfellet med Lightning-adresser. Kopier lenken og gå deretter tilbake til Ocean-siden.

I **Lightning BOLT12 Offer**-feltet, lim inn betalingslenken og la **Block Height**-feltet stå på sin standardverdi. Klikk på **GENERATE**.

![signup](assets/13.webp)

For at Ocean skal sikre at denne betalingslenken faktisk er din uten å bruke et kontosystem, må du signere meldingen som nettopp har blitt generert med din private nøkkel som tilsvarer Bitcoin-adressen du bruker. Mange løsninger eksisterer for å signere en melding med din private nøkkel. I denne opplæringen vil vi ta eksemplet med BlueWallet, men metoden er den samme for alle lommebøker.

![signup](assets/14.webp)

Forutsatt at din private nøkkel er i BlueWallet (du kan gjøre det samme med en maskinvarelommebok), klikk på den aktuelle lommeboken.

![signup](assets/15.webp)

Deretter på **…** øverst til høyre.

![signup](assets/15bis.webp)

Og **Sign/Verify Message**.

![signup](assets/16.webp)

I dette vinduet har du tre felt: **Address**, **Signature**, og **Message**.

I **Address**-feltet, skriv inn din Bitcoin-adresse. Hvis vi går tilbake til vårt eksempel, er det adressen: `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`.

La **Signature**-feltet stå tomt.
Og lim inn den genererte meldingen i **Melding**-feltet på Ocean sin side: `{"height":845900,"lightning_bolt12":"lno1pg7y7s69g98zq5rp09hh2arnypnx7u3qvf3nzufjv4jrs7ncwyuxu6n3wdaxu6msxank5wp5dcc8samv89j8qv3jx36kscfjvempvggz84uzkn26vyzq8y2mr2s8fv0j76wesq43dz72kqrk33nl2tk9j45s"}`Klikk på **Signer**.

Dette vil generere en kryptografisk signatur som beviser at du er eieren av adressen `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`, og denne signaturen er unik takket være meldingen som er levert av Ocean, generert fra BOLT12 betalingslenken.

![signup](assets/17.webp)

Kopier signaturen og lim den inn på Ocean sin side, deretter klikk på **BEKREFT**.

![signup](assets/18.webp)

Du bør se en bekreftelsesmelding.

![signup](assets/19.webp)

Nå gå til **Mine Statistikker**-fanen. Ytterligere informasjon vises øverst med BOLT12 betalingslenken du tidligere genererte med Core Lightning på Start9.

![signup](assets/20.webp)