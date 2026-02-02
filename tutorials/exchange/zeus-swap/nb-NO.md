---
name: Zeus Swap
description: Ikke-frihetsberøvende Exchange-tjeneste mellom On-Chain og Lightning Network bitcoins
---

![cover](assets/cover.webp)



Bitcoin-økosystemet er todelt: Hovednettverket (On-Chain) tilbyr maksimal sikkerhet, mens Lightning Network muliggjør umiddelbare transaksjoner. Denne to-Layer-arkitekturen skaper en praktisk utfordring: Hvordan kan midler overføres effektivt mellom disse to lagene uten sentraliserte mellomledd?



Problemet er konkret: Du mottar en Lightning-betaling, men ønsker å oppbevare den i Cold-lagring, eller omvendt, du har On-Chain-bitcoins, men trenger Lightning-likviditet. Tradisjonelle løsninger innebærer manuell åpning/lukking av Lightning-kanaler (kostbart og teknisk) eller sentraliserte plattformer som krever KYC.



Zeus Swap løser dette problemet med en automatisert Exchange-tjeneste uten frihetsberøvelse. Tjenesten er utviklet av Zeus LSP, og lar deg konvertere On-Chain bitcoins til Lightning satoshis i begge retninger, uten å overlate pengene dine til en mellommann. Prosessen bruker atomkontrakter (HTLC) som garanterer at Exchange enten fullføres eller kanselleres.



Innovasjonen ligger i enkelheten: bare noen få klikk for en Exchange som bevarer din økonomiske suverenitet, uten krav til registrering eller KYC.



## Hva er Zeus Swap?



Zeus Swap er en Exchange-likviditetstjeneste utviklet av Zeus LSP, som muliggjør atombytter mellom hovednettverket Bitcoin og Lightning Network. Det er en teknisk infrastruktur som bruker undersjøiske bytter og omvendte bytter for å legge til rette for toveiskonvertering mellom On-Chain BTC og Lightning-satoshier, samtidig som operasjonens ikke-frihetsberøvende karakter opprettholdes.



### Teknisk arkitektur



Zeus Swap bruker Boltz' åpen kildekode Bitcoin/Lightning atomic swap-teknologi. Protokollen bruker Hash Time Locked Contracts (HTLC): kontrakter som låser midler med to frigjøringsbetingelser (avsløring av en kryptografisk hemmelighet eller tidsutløp).



For et ubåtbytte (On-Chain → Lightning) sender brukeren bitcoins til en Address som inkorporerer Hash til en Lightning Invoice. Zeus LSP låser opp disse midlene kun ved å betale den tilsvarende Invoice, og avslører forhåndsbildet som automatisk låser opp bitcoinsene. Denne mekanismen garanterer atomicitet.



For et reversert bytte (Lightning → On-Chain) betaler brukeren en Lightning Invoice fra Zeus LSP, som avslører et forhåndsbilde som muliggjør frigjøring av en forberedt Bitcoin-transaksjon til destinasjonen Address.



Hvis du vil vite mer om hvordan Lightning Network fungerer, kan du ta en titt på vårt eget kurs :



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### Forretningsmodell



Zeus LSP fungerer som market maker og opprettholder On-Chain og Lightning-likviditet for å honorere swapper. For swapper bruker Zeus et variabelt gebyr (vanligvis 0,1 % til 0,5 % avhengig av retning og betingelser) pluss Bitcoins Mining-gebyr, som vises transparent før validering.



Som Lightning Service Provider optimaliserer Zeus kostnadene takket være sin ekspertise innen on-demand kanalåpning, effektiv ruting og skreddersydde likviditetsløsninger.



### Integrering



Zeus Wallet integrerer tjenesten, noe som gjør det mulig å bytte uten å forlate Interface Bitcoin/Lightning. Dette eliminerer friksjonen ved å kopiere og lime inn mellom applikasjoner.



Det uavhengige Interface-nettverket forblir tilgjengelig for alle lommebøker, noe som garanterer maksimal fleksibilitet i bruken.



## Hovedfunksjoner



### Toveis bytter



Zeus Swap tilbyr to typer Exchange:



**U-båtbytter (On-Chain → Lyn)**: Tilfør Lyn-likviditet fra Bitcoin-reservene dine, nyttig for å mate en mobil Wallet- eller Lyn-node uten å åpne kanaler manuelt.



**Reverse swaps (Lightning → On-Chain)**: konverter Lightning-satoshier til On-Chain bitcoins for langtidslagring, og unngå kostbare kanalstengninger.



### Brukergrensesnitt



**Interface web** (swaps.zeuslsp.com): forenklet opplevelse uten registrering, veiledet prosess med sanntidsvisning av avgifter og status.



**Zeus Wallet-integrasjon**: direkte bytter fra applikasjonen, automatisk håndtering av fakturaer og adresser, noe som eliminerer håndteringsfeil.



### Sikkerhet og restitusjon



Hvert bytte genererer en unik Contract med uforanderlige parametere: Hash Lightning, timeout, refusjon Address. I tilfelle feil, automatisk gjenoppretting via Address, uavhengig av Zeus LSP.



**Zeus Swaps Rescue Key**: Under et On-Chain → Lightning-bytte genererer Zeus automatisk en universell gjenopprettingsnøkkel som erstatter de gamle individuelle refusjonsfilene. Denne unike nøkkelen fungerer på alle enheter og for alle bytter som opprettes med den. Det er viktig å laste ned og lagre denne nøkkelen på et sikkert sted for å kunne gjenopprette pengene dine i tilfelle et bytte mislykkes.



### Optimalisering av nettverket



Zeus Swap justerer automatisk utløpstider og Mining-avgifter i henhold til nettverksforholdene. Zeus-brukere drar nytte av avanserte alternativer: valg av LSP, tilpassede forsinkelser, kompatibilitet med andre tjenester (Boltz).



## Installasjon og bruk



### Metoder for tilgang



**Interface web** (swaps.zeuslsp.com): Universell løsning som er kompatibel med alle lommebøker, ingen installasjon er nødvendig, ideell for sporadisk bruk.



**Zeus-appen** (iOS/Android): integrert opplevelse som kombinerer Wallet og bytter, egnet for vanlige brukere.



Se vår Zeus-veiledning for å lære mer om denne komplette Wallet :



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

### Nettkonfigurasjon



**On-Chain → Lightning**: Prosessen begynner med å konfigurere byttet på Interface web Zeus Swap. Brukeren kan bruke pilen mellom feltene On-Chain og Lightning for å reversere retningen på byttet.



![Interface de création de swap](assets/fr/01.webp)



*Interface Zeus Swap: beløpsvalg (Sats 50 000 → Sats 49 648 etter avgifter) med transparent visning av nettverksavgifter (Sats 302) og Zeus-tjeneste (Sats 50).*



Under prosessen tilbyr Zeus deg å laste ned den universelle gjenopprettingsnøkkelen :



![Téléchargement de la Zeus Swaps Rescue Key](assets/fr/02.webp)



*Nedlastingsdialog for Zeus Swaps Rescue Key - en universalnøkkel som erstatter de gamle individuelle refusjonsfilene*



Hvis du allerede har en nøkkel, kan du sjekke den i Zeus:



![Vérification de la clé existante](assets/fr/03.webp)



*Interface for å sjekke gyldigheten til en eksisterende Zeus Swaps Rescue Key*



Når den er konfigurert, genererer Zeus Bitcoin-depotet Address og viser instruksjonene :



![Adresse de dépôt et instructions](assets/fr/04.webp)



*Side for fullføring av bytte: QR-kode og Bitcoin Address for sending av 50 000 Satss, med påminnelse om 24-timers utløpsdato*



Deretter venter byttet på bekreftelse fra Bitcoin:



![Attente de confirmation](assets/fr/05.webp)



*Status "Transaksjon i Mempool" - venter på bekreftelse fra Bitcoin for å fullføre byttet*



Når dette er bekreftet, fullføres byttet automatisk:



![Swap réussi](assets/fr/06.webp)



*Bekreftelse på suksess: 49 648 Sats mottatt på Lightning etter fradrag av nettverks- og serviceavgifter*



### Bruke Zeus-appen



**Lightning → On-Chain**: Zeus-applikasjonen tilbyr en integrert opplevelse for reverserte bytter (Lightning til Bitcoin).



![Navigation vers les swaps dans Zeus](assets/fr/07.webp)



*Zeus' hovedskjermbilde viser saldoen til Lightning (69 851 Sats) og On-Chain (38 018 Sats), tilgang til bytter via sidemenyen*



![Configuration du swap reverse](assets/fr/08.webp)



*Interface opprettelse av omvendt bytte: 50 000 Sats Lightning → 49 220 Sats On-Chain, med nettverksavgifter (530 Sats) og service (250 Sats) tydelig vist. Brukere kan enten manuelt legge inn en Bitcoin som mottar Address, eller generate automatisk fra Wallet Zeus via "generate On-Chain Address"-knappen*



![Finalisation du swap mobile](assets/fr/09.webp)



*Avslutningsskjermbilder: Lightning Invoice-betalingsskjermbilde med "BETAL DENNE Invoice", bekreftelse på vellykket Lightning-betaling på 9,96 sekunder, og saldooppstilling med 49 162 Sats som venter på bekreftelse*



### Overvåkning og sikkerhet



Hvert bytte har en unik identifikator med sporing i sanntid. Full fremdriftsvisning, automatiske varsler for utløpsdatoer. Automatiske ladeanbefalinger i henhold til nettverksforholdene.



## Fordeler og begrensninger



### Fordeler





- Enkelhet**: Bytt med noen få klikk kontra manuell kanalmanipulering
- Ikke-frihetsberøvende**: ingen KYC, ingen konto, midler blir aldri overlatt til en tredjepart
- Åpenhet**: gebyrene vises eksplisitt før validering (0,1 % til 0,5 % + minimumsbeløp avhengig av brukertester - sjekk gjeldende gebyrer ved hver byttehandel)
- Mobilintegrasjon**: opprinnelig opplevelse i Zeus Wallet



### Begrensninger





- Utløpstider**: maksimalt 24-48 timer, mislykkes hvis Bitcoin ikke bekreftes i tide
- Beløpsgrenser**: minimum 25 000 Sats, Zeus LSP-likviditet variabel i henhold til betingelser
- Sporer On-Chain**: HTLC-skript som potensielt kan identifiseres ved hjelp av Blockchain-analyse
- Bekreftelse kreves**: minimum 10 minutter for Bitcoin-validering



## Beste praksis



### Tidspunkt og kostnader





- Hold øye med Mempool.space i perioder med lite trafikk
- Foretrekker helger og utenom rushtiden for å redusere Mining-kostnadene
- Beregn lønnsomhet: små beløp vs. direkte kanalåpning



### Sikkerhet





- Sjekk Bitcoin-adressene nøye (anbefales å kopiere og lime inn)
- Sikkerhetskopier Zeus Swaps Rescue Key**: Last ned og oppbevar gjenopprettingsnøkkelen på et trygt sted
- Dokument: Contract ID, refusjon Address, utløpsdato
- Bruk passende Mining-avgifter for rettidig bekreftelse



### Strategi for bruk





- Balansere On-Chain/Lightning-likviditeten slik at den passer til dine behov
- Zeus Swap for engangsjusteringer, direktekanaler for permanente behov



## Sammenligning med andre byttetjenester



### Zeus Swap vs Boltz Exchange



Zeus Swap bruker Boltz' backend-teknologi, men gjør noen avgjørende forbedringer:



**Zeus Swap-fordeler** :




- Interface unified**: innebygd integrering i Zeus Wallet vs Interface webteknikk Boltz
- WebSocket API**: oppdateringer i sanntid vs. manuell polling
- Automatisert administrasjon**: automatisk fakturering og Address-administrasjon
- Mobilstøtte**: Optimalisering kun for smarttelefoner vs. datamaskiner
- Swagger-dokumentasjon**: komplett REST API for utviklere



**Boltz er fortsatt fordelaktig** for total uavhengighet og bruk med alle Bitcoin/Lightning-oppsett.



Zeus Swap forvandler velprøvd Boltz-teknologi til en vanlig brukeropplevelse, som kan sammenlignes med forskjellen mellom en rå protokoll og et brukervennlig program.



### Zeus Swap vs Phoenix/Breez (integrerte bytter)



Phoenix og Breez integrerer transparente byttefunksjoner som skjuler den tekniske kompleksiteten for sluttbrukeren. Phoenix bruker et automatisk inn-/utbyttesystem der brukeren ikke eksplisitt skiller mellom Bitcoin-lag: Han "sender til en Bitcoin Address", og programmet håndterer byttet i bakgrunnen.



Denne ultraforenklede tilnærmingen passer perfekt for nybegynnere, men begrenser forståelsen og kontrollen over operasjonene. Zeus Swap har en mer pedagogisk filosofi: Brukerne forstår at de bytter mellom to forskjellige lag, og utvikler gradvis sin forståelse av økosystemet to-Layer Bitcoin.



## Detaljert sammenligning av gebyrer og grenser (2024)



⚠️ **Advarsel**: Gebyrene kan variere over tid, avhengig av markedsforhold og tjenesteoppdateringer. Sjekk alltid gebyrene som vises i Interface før du validerer et bytte.




| Tjeneste | Submarine Swap (BTC→LN) | Reverse Swap (LN→BTC) | Minimumsbeløp |
| ------------- | ----------------------- | --------------------- | --------------- |
| **Zeus Swap** | ~0.1% + mininggebyr | 0.5% + mininggebyr | 25 000 sats |
| **Boltz** | 0.2% + mininggebyr | 0.5% + mininggebyr | 50 000 sats |
| **Phoenix** | Kun mininggebyr | 0.4% fast | 10 000 sats |
| **Breez** | 0.25% + nettverksgebyr | 0.5% + mininggebyr | 50 000 sats |

Zeus Swap tilbyr en balanse mellom brukervennlighet og teknisk kontroll: mer tilgjengelig enn Boltz, mer fleksibel enn Phoenix/Breez, med en streng, ikke-frihetsberøvende tilnærming.



## Konklusjon



Zeus Swap representerer en betydelig innovasjon i Bitcoin-økosystemet, og løser på en elegant måte utfordringen med interoperabilitet mellom hovednettverket og Lightning Network. Ved å kombinere den kryptografiske robustheten til atomiske bytter med en tilgjengelig brukeropplevelse, demokratiserer denne tjenesten Bitcoin dual-Layer-administrasjon uten å gå på akkord med prinsippene for økonomisk suverenitet.



Zeus Swaps ikke-forvaringsarkitektur, som er arvet fra den velprøvde Boltz-teknologien, sikrer at midlene dine forblir under din eksklusive kontroll gjennom hele bytteprosessen. Denne tilnærmingen respekterer ånden i Bitcoin, samtidig som den tilbyr den brukervennligheten som kreves for å bli tatt i bruk. Åpen prising og fravær av KYC-prosesser forsterker dette unike verdiforslaget.



For den moderne Bitcoin-brukeren er Zeus Swap et strategisk verktøy for å optimalisere fordelingen av likviditet i henhold til behov: On-Chain sikker lagring for langsiktig sparing, lyntilgjengelighet for daglig forbruk og mikrotransaksjoner. Denne fleksibiliteten forvandler Bitcoin-styring fra en teknisk begrensning til et konkurransefortrinn.



Den fremtidige utviklingen av Zeus Swap, støttet av det erfarne Zeus LSP-teamet og Boltz' åpen kildekode-fellesskap, lover fortsatte forbedringer når det gjelder kostnader, behandlingstider og brukeropplevelse. Denne tjenesten er en del av den bredere trenden mot modning av Bitcoin-infrastrukturen, der teknisk raffinement blir gjennomsiktig for sluttbrukeren.



## Ressurser



### Offisiell dokumentasjon




- [Zeus Swap - Nettportal](https://swaps.zeuslsp.com)
- [Zeus Wallet - Mobilapplikasjon](https://zeusln.app)
- [Blog Zeus - Kunngjøringer og veiledninger](https://blog.zeusln.com)
- [Zeus teknisk dokumentasjon](https://docs.zeusln.app)



### Fellesskap og støtte




- [Twitter Zeus (@zeusln)](https://twitter.com/zeusln)
- [Telegram Zeus](https://t.me/ZeusLN)
- [GitHub Zeus](https://github.com/ZeusLN)