---
name: Byttemarkedet
description: Bitcoin og Lightning swap-tjenester aggregator
---

![cover](assets/cover.webp)



Overføring av midler mellom Bitcoin On-Chain og Lightning Network krever vanligvis enten manuell åpning av Lightning-kanaler (teknisk og kostbart), eller bruk av sentraliserte swap-plattformer med KYC. SwapMarket tilbyr et alternativ: Trustless atom-swapper via konkurransedyktige leverandører, uten KYC.



Innovasjon: Selv om leverandørene er mellommenn, garanterer HTLC (*Hash Time Locked Contracts*) matematisk at midlene dine forblir under din kontroll. Samlingen av flere leverandører (Boltz, ZEUS Swaps, Eldamar, Middle Way) skaper priskonkurranse. Interface web åpen kildekode, selv-hosting.



## Hva er SwapMarket?



SwapMarket er en aggregator med åpen kildekode som ble lansert i 2024, og fungerer som en sammenligner av Bitcoin/Lightning-swapleverandører. Brukeren sammenligner umiddelbart betingelser (gebyrer, likviditet, grenser) og velger den optimale leverandøren.



### Teknisk arkitektur



**Frontend på klientsiden**: 100 % klientsideapplikasjon (Fork Boltz Web App) hostet på GitHub Pages. Koden kjører i nettleseren uten backend-server. Historikk lagres lokalt (informasjonskapsler/cache). Offentlig og reviderbar kildekode.



**Tilbyderoppdagelse** : Hard-kodet liste i `src/configs/Mainnet.ts`. Nye leverandører legges til via Pull Request eller e-post.



**Uavhengige backends**: Hver leverandør driver sin egen Boltz-backend. Interface spør API-ene i sanntid for å sammenligne tilbud umiddelbart.



**HTLC Atomiske bytter**: Hash Time Locked Contracts garanterer atomicitet: enten gjennomføres swappen, eller så får hver av partene tilbake sine midler. Motpartsrisiko er matematisk eliminert.



### Filosofi



SwapMarket reduserer sentralisering ved å skape konkurranse mellom leverandører om gebyrer og likviditet. Ingen KYC, åpen kildekode som kan hostes selv, flere uavhengige operatører for å unngå single points of failure.



## Hovedfunksjoner



### Leverandørens markedsplass



Interface viser alle aktive leverandører: navn på leverandør, gebyrer (prosent og/eller faste), minimums-/maksimumsbeløp som er tilgjengelige, og hvilke swaptyper som støttes. Programmet spør direkte etter API-ene til hver leverandør som er referert til i konfigurasjonsfilen, for å hente inn tilbud i sanntid. Konkurransen mellom leverandørene garanterer optimale priser, vanligvis rundt 0,5 % for standard swapper.



### Toveis bytter



**Bytt inn (On-Chain → Lightning)**: Konverter On-Chain BTC-er til Lightning-satoshier. Bruksområde: drive en mobil Wallet Lightning, skaffe innkommende kapasitet på en node eller ha umiddelbar likviditet.



**Bytt ut (Lightning → On-Chain)**: Konverter Lightning-satoshier til On-Chain BTC. Brukssak: Dump Wallet Lightning til Cold-lagring eller rebalansering av likviditet mellom lagene.



### Sikkerhet og restitusjon



**Trustless Atombytteavtaler: HTLC garanterer at enten Exchange fullføres i sin helhet, eller at hver part får tilbake sin innsats. Motpartsrisiko er matematisk eliminert.



**Innløsningsmekanisme**: Hver swap har en utløpsdato (TIMELOCK). Hvis byttet mislykkes, refunderes midlene automatisk etter utløpet. Brukeren har alltid muligheten til å kreve tilbake bitcoinsene sine.



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



Applikasjonen vil være tilgjengelig på `http://localhost:3000`. Selvhosting garanterer total kontroll over Interface, eliminerer risikoen for sensur av det offisielle domenet og gjør det mulig å kontrollere kildekoden før den kjøres.



### Opprinnelig konfigurasjon



**Wallet Lightning**: Sørg for at du har en operativ Wallet Lightning (Phoenix, Zeus, BlueWallet osv.). For innbytte vil du generate en Lightning Invoice. For utskiftninger betaler du en Lightning Invoice.



**Wallet On-Chain**: For innbytte trenger du en Wallet Bitcoin On-Chain for å sende penger. For utvekslinger må du forberede en Bitcoin som mottar Address.



**Valgfri konfigurasjon**: SwapMarket lagrer byttehistorikk og preferanser i informasjonskapsler i nettleseren. Ingen kontoopprettelse kreves.



## Tilgang til innstillinger og Rescue Key



Før du foretar dine første bytter, anbefaler vi på det sterkeste at du laster ned din **Rescue Key**. Med denne nødnøkkelen kan du få tilbake pengene dine hvis du skulle få et teknisk problem eller miste tilgangen til enheten din.



### Tilgangsparametere



Fra SwapMarkets hovedside klikker du på tannhjulikonet (⚙️) øverst til høyre på Interface, ved siden av bytteskjemaet.



![Accès aux paramètres](assets/fr/01.webp)



### Sideinnstillinger



Innstillinger-siden åpnes og viser flere konfigurasjonsalternativer:





- Pålydende**: Valg mellom BTC eller Sats
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



Dette første eksempelet viser hvordan du konverterer Lightning-satoshier til On-Chain bitcoins.



**Trinn 1: Bytt konfigurasjon



Fra hovedsiden velger du bytteskjemaet :




- LIGHTNING** (øvre felt): Skriv inn beløpet du ønsker å sende i Sats Lightning (eksempel: 30 000 Sats)
- Bitcoin** (nederste felt): Beløpet du vil motta vises automatisk etter at avgiftene er trukket fra (eksempel: Sats 29 320)



I det nederste feltet limer du inn din **mottakende Bitcoin Address** der du ønsker å motta midlene. Kontroller denne Address nøye.



Standard leverandør er vanligvis Boltz Exchange. Nettverksavgifter og leverandøravgifter vises tydelig.



![Configuration swap-out](assets/fr/03.webp)



**Trinn 2: Valg av leverandør**



Klikk på rullegardinmenyen for leverandør (standard: "Boltz Exchange") for å vise alle tilgjengelige likviditetsleverandører.



Et modalvindu åpnes og viser en sammenligningstabell:




- Status**: Green-indikator hvis leverandøren er aktiv
- Alias**: Navn på leverandør (Boltz Exchange, Middle Way, Eldamar, ZEUS Swaps)
- Gebyr**: Gebyr som påløper fra leverandøren (vanligvis mellom 0,49 % og 0,5 %)
- Maks bytte**: Maksimalt beløp som aksepteres for en swap



Sammenlign gebyrer og maksimumsbeløp, og velg deretter den leverandøren du ønsker.



**Vær oppmerksom på dette**: Interface for valg av leverandør viser ikke **minimumsbeløp** for hver leverandør. Denne informasjonen vises kun i Interface for opprettelse av bytte, etter at en leverandør er valgt. Minimums- og maksimumsbeløp kan variere fra leverandør til leverandør, og kan endres over tid. **Sjekk alltid disse grensene når du gjør byttet**: Hvis beløpet du ønsker å bytte ligger utenfor grensene til en leverandør, kan du velge en annen leverandør som passer bedre for transaksjonen din.



![Sélection du provider](assets/fr/04.webp)



**Trinn 3: Opprettelse av bytte og betaling med Lightning**



Klikk på den gule **"CREATE ATOMIC SWAP"**-knappen. SwapMarket vil generate en **Lightning Invoice** (BOLT11) som du kan betale fra din Wallet Lightning.



Siden viser :




- Bytte-ID**: Unik bytteidentifikator (eksempel: J4ymFIMVR6Hm)
- Status**: "swap.created" (bytte opprettet, venter på betaling)
- QR-kode**: Skann den med din Wallet Lightning
- Invoice Lightning**: Tegnstreng som begynner med "lnbc" (eksempel: lnbc300u1p50whiv...gn5dk2szgqkvfkzc)



Betal denne Invoice fra din Wallet Lightning (Phoenix, Zeus, BlueWallet osv.). Det nøyaktige beløpet som skal betales vises (eksempel: 30 000 Sats).



![Paiement Lightning](assets/fr/05.webp)



**Trinn 4: Bekreftelse og aksept**



Når Lightning-betalingen er bekreftet, mottar SwapMarket umiddelbart betalingen din, og leverandøren sender Bitcoin-transaksjonen til din Address.



Statusen endres til **"Invoice.settled"** (Invoice betalt), og en bekreftelsesmelding vises.



Dine On-Chain bitcoins vil være tilgjengelige så snart transaksjonen er bekreftet (vanligvis i løpet av noen få minutter til noen få timer, avhengig av Mining-gebyrene som leverandøren har valgt).



![Confirmation swap-out](assets/fr/06.webp)



Du kan klikke på **"OPEN CLAIM TRANSACTION"** for å se Bitcoin-transaksjonen på en Blockchain explorer.



### Bytte inn: Bitcoin → Lightning



Dette andre eksempelet viser hvordan du konverterer On-Chain bitcoins til Lightning satoshis.



**Trinn 1: Bytt konfigurasjon



Fra hovedsiden velger du bytteskjemaet :




- Bitcoin** (øvre felt): Skriv inn beløpet du ønsker å sende i Sats Bitcoin (eksempel: 63 400 Sats)
- LIGHTNING** (nederste felt): Beløpet du vil motta vises automatisk etter at gebyrene er trukket fra (eksempel: 62 884 Sats)



I det nederste feltet limer du inn en Lightning** Invoice (BOLT11) generert fra din Wallet Lightning, eller du kan bruke LNURL Address hvis din Wallet støtter det.



![Configuration swap-in](assets/fr/07.webp)



**Trinn 2: Kontroll av redningsnøkkel**



Når du har klikket på **"CREATE ATOMIC SWAP"**, vises et modalvindu der du blir bedt om å bekrefte Rescue Key.



![Modal Rescue Key](assets/fr/08.webp)



**Boltz Rescue Key**: Ettersom du allerede har lastet opp gjenopprettingsnøkkelen din under den første konfigurasjonen (se forrige avsnitt), klikker du på knappen **"VERIFY EXISTING KEY"** for å importere nøkkelen du har lagret.



Velg den tidligere nedlastede Rescue Key-filen. Etter vellykket verifisering går Interface automatisk videre til neste trinn.



**Trinn 3: Bitcoin** innskudd Address



SwapMarket genererer nå en **unik Bitcoin Address** som inneholder HTLC Contract knyttet til din Lightning Invoice.



Siden viser :




- Bytte-ID**: Unik identifikator (eksempel: 1kGmB6JyGqU4)
- Status** : "Invoice.set" (Invoice er satt, venter på betaling Bitcoin)
- QR-kode**: Bitcoin depot Address
- Bitcoin** Address: Begynner vanligvis med "bc1p..." (eksempel: bc1p5mvtwxapjkds...9d4n9f)
- Advarsel i gult** : "Sørg for at transaksjonen bekreftes innen ~24 timer etter at dette byttet er opprettet!"



Denne perioden på ~24 timer er **timeout** for HTLC Contract. Hvis Bitcoin-transaksjonen ikke bekreftes innen denne tidsrammen, vil byttet mislykkes, og du må bruke Rescue Key for å få tilbake pengene dine.



![Adresse de dépôt Bitcoin](assets/fr/09.webp)



Du kan kopiere Address ved å klikke på **"Address"**-knappen, eller skanne QR-koden direkte fra din Wallet On-Chain.



**Trinn 4: Sende bitcoins**



Fra din Wallet Bitcoin On-Chain sender du **nøyaktig** det angitte beløpet (f.eks. 63 400 Sats) til den genererte Address.



**Viktig**: Bruk passende Mining-gebyrer for å garantere rask bekreftelse. Hvis gebyret er for lavt og transaksjonen blir værende i Mempool utover tidsavbruddet (~24 timer), vil byttet mislykkes.



Når transaksjonen er sendt, oppdager SwapMarket at den er i Mempool og viser :




- Status** : "transaction.Mempool"
- Melding**: "Transaksjonen er i Mempool - Venter på bekreftelse for å fullføre byttet"



![Transaction en mempool](assets/fr/10.webp)



**Trinn 5: Bekreftelse og mottak av lyn**



Så snart Bitcoin-transaksjonen får sin første bekreftelse, betaler leverandøren automatisk din Lightning Invoice. Du mottar satoshiene umiddelbart på din Wallet Lightning.



Statusen endres til **"transaction.claim.pending"**, og deretter vises en bekreftelsesmelding:



![Confirmation swap-in](assets/fr/11.webp)



Lynsatosjene dine er umiddelbart tilgjengelige i Wallet.



## Fordeler og begrensninger



### Fordeler



**Ratekonkurranse**: Samlingen av tilbydere skaper en naturlig konkurranse som trekker gebyrene ned (0,49 % til 0,5 %).



**Konfidensialitet**: Ingen KYC, Interface 100 % på klientsiden (ingen overføring av personopplysninger), kompatibel med Tor-nettleseren.



**Ikke-frihetsberøvende**: HTLC garanterer matematisk eksklusiv kontroll over midlene dine. Enten lykkes byttet, eller så får du tilbake bitcoinsene dine.



**Selv-hosting med åpen kildekode**: offentlig kode som kan revideres og distribueres lokalt for maksimal motstand mot sensur.



### Begrensninger



**Begrenset likviditet**: Begrenset antall aktive leverandører (Boltz, Eldamar, MiddleWay avhengig av periode). Maksimumsbeløp kan være begrenset.



**Utløpstid**: Tidsavbrudd fra 24 til 48 timer. Hvis On-Chain-transaksjonen ikke bekreftes før utløp, kreves manuell gjenoppretting.



**Interface-sentralisering**: Selv om den offisielle Interface kan hostes selv, ligger den på GitHub Pages. Hvis GitHub sensurerer repoen, vil tilgang via swapmarket.github.io bli blokkert (løsning: selvhosting).



**On-Chain-spor**: HTLC-skript kan potensielt identifiseres ved hjelp av avansert Blockchain-analyse.



## Beste praksis



### Sikker konfigurasjon



**Last ned redningsnøkkelen din**: Før du gjør dine første bytter, må du laste ned redningsnøkkelen din fra Innstillinger (se den dedikerte delen ovenfor). Denne unike nøkkelen vil fungere for alle fremtidige bytter, slik at du kan få tilbake pengene dine hvis det skulle oppstå et problem.



**Bruk Tor-nettleseren**: For maksimal konfidensialitet, få tilgang til SwapMarket via Tor Browser for å skjule din IP Address.



**Vurder selvhosting**: For tekniske brukere som kjører sin egen SwapMarket-forekomst, slipper man å være avhengig av det offisielle GitHub Pages-domenet.



### Optimalisering av bytte



**Hold et øye med Mempool**: Sjekk Mempool.space før et innbytte. Velg tidspunkter med lav aktivitet for å minimere Mining-kostnadene.



**Sjekk adresser**: For utskiftninger må du kontrollere mottakende Address nøye. Bruk kopier og lim inn og sjekk de første 5 og de siste 5 tegnene.



**Test med små mengder**: Begynn med den minste tillatte mengden (25 000 til 50 000 Sats). Øk gradvis når du har mestret prosessen.



**Dokumenter byttene dine**: Noter hver swaps ID, innløsnings-Address og utløpsdato. Denne informasjonen gjør det lettere å spore og gjenopprette swapene i tilfelle et teknisk problem.



### Strategi for bruk



**Balanser kontantstrømmen din**: Bruk SwapMarket til å justere fordelingen mellom On-Chain (sparing, langsiktig sikkerhet) og Lightning (daglige utgifter, umiddelbare betalinger) i henhold til dine reelle behov.



**Beregn lønnsomhet**: For permanente Lightning-likviditetsbehov kan du sammenligne den kumulative kostnaden ved gjentatte swapper med å åpne en Lightning-kanal direkte. SwapMarket utmerker seg for engangsjusteringer, ikke nødvendigvis for store, regelmessige strømmer.



## SwapMarket vs Boltz: Hva er forskjellen?



### Boltz: Teknologi vs. service



**Boltz er åpen kildekode-teknologien** (`boltz-backend` på GitHub) som implementerer atombytter via HTLC mellom Bitcoin, Lightning og Liquid.



**Kritisk punkt**: Alle SwapMarket-leverandører (Boltz Exchange, ZEUS Swaps, Eldamar, Middle Way) bruker sin egen instans av Boltz backend. Den underliggende teknologien er derfor identisk. En sårbarhet i Boltz-backenden vil potensielt påvirke alle tilbydere, men systemets åpne kildekode gjør det mulig for fellesskapsrevisjon.



**Boltz Exchange** er en enkelt tjeneste som drives av Boltz-teamet, mens **SwapMarket** samler flere leverandører som alle bruker Boltz-teknologi, noe som skaper et konkurransedyktig prismiljø.



Se veiledningene Boltz og Zeus Swap for mer informasjon:



https://planb.network/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

https://planb.network/tutorials/exchange/centralized/zeus-swap-b6732907-b5d8-43ea-85e3-9dcd6e6abe47

### Viktige forskjeller



| Aspect        | Boltz Exchange           | SwapMarket                                 |
| ------------- | ------------------------ | ------------------------------------------ |
| Nature        | Service unique           | Agrégateur multi-providers                 |
| Providers     | Boltz uniquement         | Boltz, ZEUS, Eldamar, Middle Way           |
| Compétition   | Tarifs fixes             | Compétition libre                          |
| Interface     | boltz.exchange           | swapmarket.github.io (self-hostable)       |
| Sécurité      | Non-custodial (HTLC)     | Non-custodial (HTLC)                       |

**Fordeler med SwapMarket**: Priskonkurranse, diversifisering av backend-instanser, sammenligning i sanntid.



**Teknologiske alternativer** (ikke kompatible med SwapMarket): Lightning Loop (Lightning Labs), Muun Wallet, NLoop, Breez Wallet. Disse løsningene bruker sine egne implementeringer av undervannsbytter.



**Anbefaling**: Bruk Boltz Exchange for enkelhetens skyld eller SwapMarket for å optimalisere kostnadene gjennom konkurranse. Begge er like sikre (HTLC er ikke frihetsberøvende).



## Konklusjon



SwapMarket legger til rette for Bitcoin/Lightning-børser ved å samle flere leverandører i én enkelt Interface. HTLC-arkitekturen garanterer at swapene ikke er frihetsberøvende, fraværet av KYC bevarer konfidensialiteten, og koden med åpen kildekode som kan hostes på egen hånd, styrker motstanden mot sensur.



Konkurransen mellom leverandørene forbedrer prisene og mangedobler kildene til likviditet. For å optimalisere to-Layer-styring (On-Chain-besparelser, Lightning-utgifter) er SwapMarket et praktisk verktøy som bevarer finansiell suverenitet og konfidensialitet.



## Ressurser



### Offisiell dokumentasjon




- [SwapMarket - Webapplikasjon](https://swapmarket.github.io)
- [GitHub SwapMarket] (https://github.com/SwapMarket/swapmarket.github.io)
- [Teknisk dokumentasjon] (https://docs.boltz.Exchange/)
- [Guide til selvhosting] (https://github.com/SwapMarket/swapmarket.github.io/blob/main/README.md)



### Relaterte prosjekter




- [Boltz Exchange](https://boltz.Exchange) - Original atombyttetjeneste
- [ZEUS Swaps](https://zeusln.com) - Leverandør av lynbytteavtaler