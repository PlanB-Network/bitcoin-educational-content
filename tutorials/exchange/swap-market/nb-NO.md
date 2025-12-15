---
name: SwapMarket
description: Bitcoin og Lightning swap-tjenester aggregator
---

![cover](assets/cover.webp)



Overføring av midler mellom Bitcoin on-chain og Lightning Network krever vanligvis enten manuell åpning av Lightning-kanaler (teknisk og kostbart), eller bruk av sentraliserte swapplattformer med KYC. SwapMarket tilbyr et alternativ: tillitsløse atom-swapper via konkurransedyktige leverandører, uten KYC.



Innovasjon: Selv om leverandørene er mellommenn, garanterer HTLC (*Hash Time Locked Contracts*) matematisk at midlene dine forblir under din kontroll. Samlingen av flere leverandører (Boltz, ZEUS Swaps, Eldamar, Middle Way) skaper priskonkurranse. Interface web åpen kildekode, selv-hosting.



## Hva er SwapMarket?



SwapMarket er en åpen kildekode-aggregator som ble lansert i 2024, og fungerer som en sammenligner av Bitcoin/Lightning-swapleverandører. Brukeren sammenligner umiddelbart betingelser (gebyrer, likviditet, grenser) og velger den optimale leverandøren.



### Teknisk arkitektur



**Frontend på klientsiden**: 100 % klientsideapplikasjon (fork Boltz Web App) som ligger på GitHub Pages. Koden kjører i nettleseren uten backend-server. Historikk lagres lokalt (informasjonskapsler/cache). Offentlig og reviderbar kildekode.



**Provideroppdagelse** : Hardkodet liste i `src/configs/mainnet.ts`. Nye leverandører legges til via Pull Request eller e-post.



**Uavhengige backends**: Hver leverandør driver sin egen Boltz-backend. Grensesnittet spør API-ene i sanntid for å sammenligne tilbud umiddelbart.



**HTLC Atomiske bytter**: Hash Time Locked Contracts garanterer atomicitet: enten gjennomføres swappen, eller så får hver av partene tilbake sine midler. Motpartsrisiko er matematisk eliminert.



### Filosofi



SwapMarket reduserer sentralisering ved å skape konkurranse mellom leverandører om gebyrer og likviditet. Ingen KYC, åpen kildekode som kan hostes selv, flere uavhengige operatører for å unngå single points of failure.



## Hovedfunksjoner



### Leverandørens markedsplass



Grensesnittet viser alle aktive leverandører: navn på leverandør, gebyrer (prosent og/eller faste), minimums-/maksimumsbeløp som er tilgjengelige, og hvilke swaptyper som støttes. Programmet spør direkte etter API-ene til hver leverandør som er referert til i konfigurasjonsfilen, for å hente inn tilbud i sanntid. Konkurransen mellom leverandørene garanterer optimale priser, vanligvis rundt 0,5 % for standard swapper.



### Toveis bytter



**Bytt inn (on-chain → Lightning)**: Konverter on-chain BTC-er til Lightning-satoshier. Bruksområde: drive en mobil wallet Lightning, skaffe innkommende kapasitet på en node eller ha øyeblikkelig likviditet.



**Bytt ut (Lightning → on-chain)**: Konverter Lightning-satoshier til on-chain BTC. Brukssak: Tøm en wallet Lightning til fryselager eller rebalansere likviditet mellom lagene.



### Sikkerhet og restitusjon



**Trustless atombytter**: HTLC garanterer at enten utvekslingen fullføres i sin helhet, eller at hver part får tilbake sin innsats. Motpartsrisiko er matematisk eliminert.



**Tilbakebetalingsmekanisme**: Hver swap har en tidslås. Hvis byttet mislykkes, refunderes midlene automatisk etter utløpet. Brukeren beholder alltid muligheten til å kreve tilbake sine bitcoins.



**Gjenopprettingsnøkler**: SwapMarket lar deg eksportere gjenopprettingsnøkler for pågående bytter. Hvis det skulle oppstå et problem, kan disse nøklene brukes til å fullføre eller avbryte et bytte fra en hvilken som helst enhet.



## Installasjon og tilgang



### Interface web



SwapMarket krever ingen installasjon. Tilgang skjer via nettleseren ved å besøke https://swapmarket.github.io. For maksimal konfidensialitet, bruk Brave, Firefox med antisporingsutvidelser eller LibreWolf. Tor Browser anbefales for anonymitet på nettet.



Ingen registrering, e-post eller identitetsbekreftelse kreves.



### Selv-hosting (valgfritt)



For tekniske brukere som ikke ønsker å være avhengige av det offisielle GitHub Pages-domenet, kan SwapMarket kjøres lokalt :



**Via npm** :


```
git clone https://github.com/SwapMarket/swapmarket.github.io.git
cd swapmarket.github.io
npm install
npm run dev
```



**Via Docker** :


```
docker run -p 3000:80 ghcr.io/swapmarket/swapmarket:latest
```



Applikasjonen vil være tilgjengelig på `http://localhost:3000`. Selvhosting garanterer full kontroll over grensesnittet, eliminerer risikoen for sensur av det offisielle domenet og gjør det mulig å kontrollere kildekoden før den kjøres.



### Opprinnelig konfigurasjon



**Wallet Lightning**: Forsikre deg om at du har en operativ wallet Lightning (Phoenix, Zeus, BlueWallet osv.). For innbytte vil du generate en Lightning-faktura. For utskiftninger betaler du en Lightning-faktura.



**Wallet on-chain**: For innbytte trenger du en wallet Bitcoin on-chain for å sende penger. For utvekslinger må du forberede en Bitcoin-mottakeradresse.



**Valgfri konfigurasjon**: SwapMarket lagrer byttehistorikk og preferanser i informasjonskapsler i nettleseren. Ingen kontoopprettelse kreves.



## Tilgang til innstillinger og Rescue Key



Før du foretar dine første bytter, anbefaler vi på det sterkeste at du laster ned din **Rescue Key**. Med denne nødnøkkelen kan du få tilbake pengene dine hvis du skulle få et teknisk problem eller miste tilgangen til enheten din.



### Tilgangsparametere



Fra SwapMarkets hovedside klikker du på tannhjulikonet (⚙️) øverst til høyre i grensesnittet, ved siden av bytteskjemaet.



![Accès aux paramètres](assets/fr/01.webp)



### Sideinnstillinger



Innstillinger-siden åpnes og viser flere konfigurasjonsalternativer:





- Pålydende**: Valg mellom BTC eller sats
- Desimalseparator**: Desimalseparator (, eller .)
- Lyd-/leservarsler**: Lyd- og nettleservarsler
- Redningsnøkkel** : Last ned gjenopprettingsnøkkelen
- Logger**: Vis, last ned eller slett logger



![Page Settings](assets/fr/02.webp)



### Last ned Rescue Key



Klikk på **Last ned**-knappen ved siden av "Rescue Key".



**Viktige punkter** :




- Redningsnøkkelen er en **nødnøkkel** som fungerer for alle fremtidige bytter
- Oppbevar denne nøkkelen på et **sikkert og permanent** sted (passordbehandler, digital safe)
- I tilfelle et bytteproblem (tidsavbrudd, teknisk feil), kan du med denne nøkkelen gjenopprette pengene dine



## Opprette et bytte trinn for trinn



### Bytte ut: Lyn → Bitcoin



Dette første eksempelet viser hvordan du konverterer Lightning-satoshier til on-chain bitcoins.



**Trinn 1: Bytt konfigurasjon



Fra hovedsiden velger du bytteskjemaet :




- LIGHTNING** (øvre felt): Skriv inn beløpet du ønsker å sende i sats Lightning (eksempel: 30 000 sats)
- BITCOIN** (nedre felt): Beløpet du vil motta vises automatisk etter at avgiftene er trukket fra (eksempel: 29 320 sats)



I det nederste feltet limer du inn **mottaker Bitcoin-adressen** der du ønsker å motta pengene. Sjekk denne adressen nøye.



Standard leverandør er vanligvis Boltz Exchange. Nettverksavgifter og leverandøravgifter vises tydelig.



![Configuration swap-out](assets/fr/03.webp)



**Trinn 2: Valg av leverandør**



Klikk på rullegardinmenyen for leverandør (standard: "Boltz Exchange") for å vise alle tilgjengelige likviditetsleverandører.



Et modalvindu åpnes og viser en sammenligningstabell:




- Status**: Green-indikator hvis leverandøren er aktiv
- Alias**: Navn på leverandør (Boltz Exchange, Middle Way, Eldamar, ZEUS Swaps)
- Gebyr**: Gebyr som påløper av leverandøren (vanligvis mellom 0,49 % og 0,5 %)
- Maks bytte**: Maksimalt beløp som aksepteres for en swap



Sammenlign gebyrer og maksimumsbeløp, og velg deretter den leverandøren du ønsker.



**Vær oppmerksom på dette**: Grensesnittet for valg av leverandør viser ikke **minimumsbeløp** for hver leverandør. Denne informasjonen vises bare i grensesnittet for oppretting av bytter, etter at en leverandør er valgt. Minimums- og maksimumsbeløp kan variere fra leverandør til leverandør, og kan endres over tid. **Sjekk alltid disse grensene når du gjør byttet**: Hvis beløpet du ønsker å bytte ligger utenfor grensene til en leverandør, kan du velge en annen leverandør som passer bedre for transaksjonen din.



![Sélection du provider](assets/fr/04.webp)



**Trinn 3: Opprettelse av bytte og betaling med Lightning**



Klikk på den gule **"CREATE ATOMIC SWAP"**-knappen. SwapMarket vil generate sende deg en **Lightning-faktura** (BOLT11) som du kan betale fra din wallet Lightning.



Siden viser :




- Bytte-ID**: Unik bytteidentifikator (eksempel: J4ymFIMVR6Hm)
- Status**: "swap.created" (bytte opprettet, venter på betaling)
- QR-kode**: Skann den med din wallet Lightning
- Invoice Lightning**: Tegnstreng som begynner med "lnbc" (eksempel: lnbc300u1p50whiv...gn5dk2szgqkvfkzc)



Betal denne fakturaen fra din wallet Lightning (Phoenix, Zeus, BlueWallet osv.). Det nøyaktige beløpet som skal betales vises (eksempel: 30 000 sats).



![Paiement Lightning](assets/fr/05.webp)



**Trinn 4: Bekreftelse og aksept**



Når Lightning-betalingen er bekreftet, mottar SwapMarket betalingen umiddelbart, og leverandøren sender Bitcoin-transaksjonen til adressen din.



Status endres til **"invoice.settled"** (faktura betalt), og en bekreftelsesmelding vises.



Dine on-chain bitcoins vil være tilgjengelige så snart transaksjonen er bekreftet (vanligvis noen minutter til noen timer, avhengig av mining-gebyrene som er valgt av leverandøren).



![Confirmation swap-out](assets/fr/06.webp)



Du kan klikke på **"OPEN CLAIM TRANSACTION"** for å se Bitcoin-transaksjonen i en blockchain-nettleser.



### Innbytte: Bitcoin → Lightning



Dette andre eksempelet viser hvordan du konverterer on-chain bitcoins til Lightning-satoshier.



**Trinn 1: Bytt konfigurasjon



Fra hovedsiden velger du bytteskjemaet :




- BITCOIN** (øvre felt): Skriv inn beløpet du ønsker å sende i sats Bitcoin (eksempel: 63 400 sats)
- LIGHTNING** (nederste felt): Beløpet du vil motta vises automatisk etter at gebyrene er trukket fra (eksempel: 62 884 sats)



I det nederste feltet limer du inn en Lightning**-faktura (BOLT11) generert fra wallet Lightning, eller bruk LNURL-adressen din hvis wallet støtter det.



![Configuration swap-in](assets/fr/07.webp)



**Trinn 2: Kontroll av redningsnøkkel**



Når du har klikket på **"CREATE ATOMIC SWAP"**, vises et modalvindu der du blir bedt om å bekrefte Rescue Key.



![Modal Rescue Key](assets/fr/08.webp)



**Boltz Rescue Key**: Ettersom du allerede har lastet opp gjenopprettingsnøkkelen din under den første konfigurasjonen (se forrige avsnitt), klikker du på knappen **"VERIFY EXISTING KEY"** for å importere nøkkelen du har lagret.



Velg den tidligere nedlastede Rescue Key-filen. Etter vellykket verifisering går grensesnittet automatisk videre til neste trinn.



**Trinn 3: Bitcoin** innskuddsadresse



SwapMarket genererer nå en **unik Bitcoin-adresse** som inneholder HTLC-kontrakten som er knyttet til Lynfakturaen din.



Siden viser :




- Bytte-ID**: Unik identifikator (eksempel: 1kGmB6JyGqU4)
- Status**: "invoice.set" (faktura satt, venter på betaling Bitcoin)
- QR-kode**: Bitcoin depotadresse
- Bitcoin**-adresse: Begynner vanligvis med "bc1p..." (eksempel: bc1p5mvtwxapjkds...9d4n9f)
- Advarsel i gult** : "Sørg for at transaksjonen bekreftes innen ~24 timer etter at dette byttet er opprettet!"



Denne perioden på ~24 timer er **timeout** for HTLC-kontrakten. Hvis Bitcoin-transaksjonen ikke bekreftes innen denne tidsrammen, vil byttet mislykkes, og du må bruke Rescue Key for å få tilbake pengene dine.



![Adresse de dépôt Bitcoin](assets/fr/09.webp)



Du kan kopiere adressen ved å klikke på **"ADRESSE"**-knappen, eller skanne QR-koden direkte fra din wallet on-chain.



**Trinn 4: Sende bitcoins**



Fra din wallet Bitcoin on-chain sender du **nøyaktig** det angitte beløpet (f.eks. 63 400 sats) til den genererte adressen.



**Viktig**: Bruk passende mining-avgifter for å garantere rask bekreftelse. Hvis gebyret er for lavt og transaksjonen blir liggende i mempool utover tidsavbruddet (~24 timer), vil byttet mislykkes.



Når transaksjonen er sendt, oppdager SwapMarket at den ligger i mempoolen og viser :




- Status** : "transaction.mempool
- Melding**: "Transaksjonen er i mempool - Venter på bekreftelse for å fullføre byttet"



![Transaction en mempool](assets/fr/10.webp)



**Trinn 5: Bekreftelse og mottak av lyn**



Så snart Bitcoin-transaksjonen mottar sin første bekreftelse, betaler leverandøren automatisk Lightning-fakturaen din. Du mottar satoshiene umiddelbart på din wallet Lightning.



Statusen endres til **"transaction.claim.pending"**, og deretter vises en bekreftelsesmelding:



![Confirmation swap-in](assets/fr/11.webp)



Lynsatoshiene dine er umiddelbart tilgjengelige i wallet.



## Fordeler og begrensninger



### Fordeler



**Ratekonkurranse**: Samlingen av tilbydere skaper en naturlig konkurranse som trekker gebyrene ned (0,49 % til 0,5 %).



**Konfidensialitet**: Ingen KYC, 100 % grensesnitt på klientsiden (ingen overføring av personopplysninger), kompatibel med Tor-nettleseren.



**Ikke-forvaring**: HTLC garanterer matematisk eksklusiv kontroll over midlene dine. Enten lykkes byttet, eller så får du tilbake bitcoinsene dine.



**Selv-hosting med åpen kildekode**: offentlig kode som kan revideres og distribueres lokalt for maksimal motstand mot sensur.



### Begrensninger



**Begrenset likviditet**: Begrenset antall aktive leverandører (Boltz, Eldamar, MiddleWay avhengig av periode). Maksimumsbeløp kan være begrenset.



**Utløpstid**: Tidsavbrudd fra 24 til 48 timer. Hvis on-chain-transaksjonen ikke bekreftes før utløp, kreves manuell gjenoppretting.



**Interface sentralisering**: Selv om det offisielle grensesnittet kan hostes selv, ligger det på GitHub Pages. Hvis GitHub sensurerer repoen, vil tilgang via swapmarket.github.io bli blokkert (løsning: selvhosting).



**on-chain-spor**: HTLC-skript kan potensielt identifiseres ved hjelp av avansert blokkjedeanalyse.



## Beste praksis



### Sikker konfigurasjon



**Last ned redningsnøkkelen din**: Før du gjør dine første bytter, må du laste ned redningsnøkkelen din fra Innstillinger (se den dedikerte delen ovenfor). Denne unike nøkkelen vil fungere for alle fremtidige bytter, slik at du kan få tilbake pengene dine hvis det skulle oppstå et problem.



**Bruk Tor-nettleseren**: For maksimal konfidensialitet, få tilgang til SwapMarket via Tor Browser for å skjule din IP-adresse.



**Vurder selvhosting**: For tekniske brukere som kjører sin egen SwapMarket-forekomst, slipper man å være avhengig av det offisielle GitHub Pages-domenet.



### Optimalisering av bytte



**Hold et øye med mempoolen**: Sjekk mempool.space før et innbytte. Velg tider med lav aktivitet for å minimere mining-kostnadene.



**Sjekk adresser**: Ved utveksling må du kontrollere mottaksadressen din nøye. Bruk kopier og lim inn, og sjekk de første 5 og de siste 5 tegnene.



**Test med små mengder**: Begynn med den minste tillatte mengden (25 000 til 50 000 sats). Øk gradvis når du har mestret prosessen.



**Dokumenter byttene dine**: Noter ID, innløsningsadresse og utløpsdato for hver swap. Denne informasjonen gjør det enklere å spore og gjenopprette swapene i tilfelle tekniske problemer.



### Strategi for bruk



**Balanser kontantstrømmen din**: Bruk SwapMarket til å justere fordelingen mellom on-chain (sparing, langsiktig sikkerhet) og Lightning (daglige utgifter, øyeblikkelige betalinger) i henhold til dine reelle behov.



**Beregn lønnsomhet**: For permanente Lightning-likviditetsbehov kan du sammenligne den kumulative kostnaden ved gjentatte swapper med å åpne en Lightning-kanal direkte. SwapMarket utmerker seg for engangsjusteringer, ikke nødvendigvis for store, regelmessige strømmer.



## SwapMarket vs Boltz: Hva er forskjellen?



### Boltz: Teknologi vs. service



**Boltz er åpen kildekode-teknologien** (`boltz-backend` på GitHub) som implementerer atombytter via HTLC mellom Bitcoin, Lightning og Liquid.



**Kritisk punkt**: Alle SwapMarket-leverandører (Boltz Exchange, ZEUS Swaps, Eldamar, Middle Way) bruker sin egen instans av Boltz backend. Den underliggende teknologien er derfor identisk. En sårbarhet i Boltz-backenden vil potensielt påvirke alle tilbydere, men systemets åpne kildekode gjør det mulig for fellesskapsrevisjon.



**Boltz Exchange** er en enkelt tjeneste som drives av Boltz-teamet, mens **SwapMarket** samler flere leverandører som alle bruker Boltz-teknologi, noe som skaper et konkurransedyktig prismiljø.



Se veiledningene Boltz og Zeus Swap for mer informasjon:



https://planb.academy/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

https://planb.academy/tutorials/exchange/centralized/zeus-swap-b6732907-b5d8-43ea-85e3-9dcd6e6abe47

### Viktige forskjeller



| Aspekt       | Boltz Exchange       | SwapMarket                           |
| ------------ | -------------------- | ------------------------------------ |
| Natur         | Unik tjeneste        | Multi-leverandør-aggregator          |
| Leverandører  | Kun Boltz            | Boltz, ZEUS, Eldamar, Middle Way     |
| Konkurranse   | Faste priser         | Fri konkurranse                      |
| Grensesnitt   | boltz.exchange       | swapmarket.github.io (selv-hostbar)   |
| Sikkerhet     | Non-custodial (HTLC) | Non-custodial (HTLC)                 |

**Fordeler med SwapMarket**: Priskonkurranse, diversifisering av backend-instanser, sammenligning i sanntid.



**Teknologiske alternativer** (ikke kompatible med SwapMarket): Lightning Loop (Lightning Labs), Muun Wallet, NLoop, Breez Wallet. Disse løsningene bruker sine egne implementeringer av undervannsbytter.



**Anbefaling**: Bruk Boltz Exchange for enkelhetens skyld eller SwapMarket for å optimalisere kostnadene gjennom konkurranse. Begge er like sikre (HTLC er ikke frihetsberøvende).



## Konklusjon



SwapMarket legger til rette for Bitcoin/Lightning-børser ved å samle flere leverandører i ett enkelt grensesnitt. HTLC-arkitekturen garanterer at byttene ikke er frihetsberøvende, fraværet av KYC bevarer konfidensialiteten, og den selv-hostbare koden med åpen kildekode forsterker motstanden mot sensur.



Konkurransen mellom leverandørene forbedrer prisene og mangedobler kildene til likviditet. SwapMarket er et praktisk verktøy for å optimalisere tolagshåndtering (on-chain-besparelser, Lightning-utgifter), samtidig som det ivaretar finansiell suverenitet og konfidensialitet.



## Ressurser



### Offisiell dokumentasjon




- [SwapMarket - Webapplikasjon](https://swapmarket.github.io)
- [GitHub SwapMarket] (https://github.com/SwapMarket/swapmarket.github.io)
- [Teknisk dokumentasjon] (https://docs.boltz.exchange/)
- [Guide til selvhosting] (https://github.com/SwapMarket/swapmarket.github.io/blob/main/README.md)



### Relaterte prosjekter




- [Boltz Exchange](https://boltz.exchange) - Original atombyttetjeneste
- [ZEUS Swaps](https://zeusln.com) - Leverandør av lynbytteavtaler