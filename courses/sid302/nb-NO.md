---
name: Liquid Bootcamp Essentials
goal: Få en omfattende forståelse av Liquid Network- og Elements-prosjektet, og lær hvordan du kan implementere avanserte løsninger innen konfidensielle transaksjoner, tokenisering og desentralisert nettverksarkitektur.
objectives: 

  - Forstå det grunnleggende i Liquid-arkitekturen og dens forhold til Bitcoin.
  - Lær deg å konfigurere og betjene Liquid-noder ved hjelp av Elements-programvaren.
  - Utforsk bruken av konfidensielle transaksjoner og utstedelse av eiendeler på Liquid Network.
  - Forstå de forretningsmessige og tekniske aspektene ved Liquid for anvendelser i kapitalmarkedene.

---

# Introduksjon til Liquid-nettverket


Bli med på en utdanningsreise som er utformet for å gi en dyp forståelse av Liquid Network og Elements-prosjektet. Denne bootcampen kombinerer teori og praksis for å lære deg de tekniske, arkitektoniske og forretningsmessige grunnprinsippene som er nødvendige for å implementere og utnytte Liquids muligheter. Fra konfidensielle transaksjoner til økosystemdesign - dette kurset er ideelt for deg som ønsker å utvide kunnskapen din om avanserte verktøy i Bitcoin-økosystemet.


Med presentasjoner fra bransjeeksperter dekker kurset emner som Liquid-arkitektur, tokeniseringsapplikasjoner, tekniske konsepter i Elements og innovative brukstilfeller som Breez SDK. Kurset er designet for å være tilgjengelig for nybegynnere og viderekomne brukere, men gir også verdi for erfarne utviklere som ønsker å mestre Liquid som en plattform for å optimalisere prosjektene sine.

+++

# Innledning


<partId>9f8a83d5-27e0-4e6d-af12-6cd6eb667291</partId>


## Kursoversikt


<chapterId>3192ee7d-255b-4c4f-ba18-e08c5ab98577</chapterId>


Velkommen til Liquid Bootcamp, et omfattende kurs som er utviklet for å gi deg kunnskapen og ferdighetene du trenger for å utnytte Liquid Network- og Elements-prosjektet på en effektiv måte. Dette kurset gir en omfattende utforskning av Liquids særegne funksjoner, inkludert Confidential Transactions, utstedelse av aktiva og den fødererte nettverksarkitekturen, samtidig som det introduserer de grunnleggende konseptene i Elements, programvaren som driver Liquid.


Gjennom hele bootcampen vil du utforske de praktiske bruksområdene til Liquid Network, fra å sette opp og drive noder til å forstå bruken av Bitcoin i kapitalmarkeder og tokenisering. Med presentasjoner fra bransjeeksperter vil du også få innsikt i avanserte emner som HTLC-er, Breez SDK og Blockstream AMP-prosjektet.


Denne bootcampen ble opprinnelig gjennomført som et personlig arrangement, etter en strukturert plan (som vist på bildet) designet for live-økter. I denne kurstilpasningen er imidlertid innholdet omorganisert for å passe bedre til et nettbasert format og gjøre det lettere for studentene å forstå. Den nye rekkefølgen sikrer en logisk progresjon fra grunnleggende konsepter til mer avanserte og tekniske emner, og maksimerer dermed læringsopplevelsen.


Denne reisen er strukturert for å imøtekomme deltakere med varierende ekspertisenivå, og tilbyr en blanding av teoretisk kunnskap og praktisk erfaring. Ved slutten av denne bootcampen vil du ha en solid forståelse av Liquids arkitektur, integrasjonen med Bitcoin og hvordan du kan bruke de innovative funksjonene til å bygge og optimalisere finansielle løsninger.


Dykk ned i Liquid-sidekjedens verden og utløs dens fulle potensial akkurat nå!

# Grunnleggende


<partId>6dd86449-c0f7-4e51-9252-5f135cf019df</partId>


## Liquid Arkitektur


<chapterId>4bca9c70-d54d-4e9a-b2db-17c3a6fa655b</chapterId>


:::video id=ff6899d2-b47f-4c3d-983d-3bd66d2be59d:::

### Liquid Network Arkitektur og konsensusmodell


Liquid Network er en føderert sidekjede bygget på Elements-kodebasen, designet for å utvide Bitcoins muligheter samtidig som den baserer seg på dens grunnleggende sikkerhet. I motsetning til Bitcoins Proof-of-Work, opererer Liquid på en føderert konsensusmodell. Nettverket vedlikeholdes av en globalt distribuert gruppe av medlemmer, inkludert børser, trading desks og infrastrukturleverandører. Fra denne gruppen velges femten "funksjonærer" ut til å fungere som blokkunderskrivere.


Disse funksjonærene produserer blokker på en deterministisk måte, med en ny blokk generert hvert minutt. Denne presise timingen står i kontrast til Bitcoins probabilistiske ti-minutters intervaller. For at en blokk skal være gyldig, må den være signert av minst 11 av de 15 funksjonærene (en terskel på to tredjedeler pluss én). Denne mekanismen gir Liquid "to-blokk-finalitet", noe som betyr at når en transaksjon har fått to bekreftelser (omtrent to minutter), er det matematisk umulig å reorganisere kjeden. Denne hastigheten og sikkerheten er avgjørende for arbitrasje, automatisert handel og raske oppgjør mellom børser.


Føderasjonen er dynamisk. Gjennom Dynamic Federation (Dynafed)-protokollen kan nettverket rotere funksjonærer eller oppdatere parametere uten at det kreves en hard fork. Dette gjør at systemet kan utvikle seg og skifte ut maskinvare eller medlemmer sømløst, samtidig som det opprettholder kontinuerlig drift.


### Confidential Transactions og kapitalforvaltning


Et av de viktigste kjennetegnene ved Liquid er at den støtter Confidential Transactions (CT) og flere aktiva. I Bitcoin-hovedkjeden er alle transaksjonsdetaljer - avsender, mottaker og beløp - offentlige. I Liquid bruker CT kryptografiske forpliktelser til å skjule aktivatypen og beløpet fra den offentlige hovedboken, samtidig som nettverket kan verifisere at transaksjonen er gyldig (dvs. at det ikke har forekommet inflasjon). Bare deltakerne som har blindingnøklene, kan se de spesifikke verdiene, noe som gir et nivå av kommersielt personvern som er avgjørende for institusjoner som flytter store posisjoner.


Liquid behandler alle eiendeler som "innfødte" borgere av blokkjeden. Dette inkluderer Liquid Bitcoin (LBTC), stablecoins som USDT og sikkerhetstokener. Utstedelse av en eiendel krever ikke komplekse smartkontrakter; det er en grunnleggende funksjon i protokollen.


#### Regulerte eiendeler og AMP

For eiendeler som krever samsvar, for eksempel sikkerhetstokener, bruker Liquid Blockstream Asset Management Platform (AMP). Dette introduserer et autorisert lag der transaksjoner krever en ekstra signatur fra en autorisasjonsserver. Dette gjør det mulig for utstedere å håndheve regler - for eksempel hvitelisting eller KYC-krav - på et detaljert nivå, og kombinerer effektiviteten til en blokkjede med de regulatoriske kontrollene i tradisjonell finans.


### Toveis Peg- og sikkerhetsinfrastruktur


Forbindelsen mellom Liquid og Bitcoin opprettholdes gjennom en toveis peg. For å "pegge inn" sender en bruker Bitcoin til en generert adresse på mainchain. Disse midlene er låst i 102 bekreftelser (ca. 17 timer) for å eliminere risikoen for omorganisering. Når det er bekreftet, blir en tilsvarende mengde LBTC preget på Liquid-sidekjeden.


"Peg-out"-prosessen gjør det mulig for brukere å løse inn LBTC mot Bitcoin. Dette krever brenning av LBTC og en kryptografisk autorisasjon fra føderasjonen. For å forhindre tyveri er peg-outs strengt kontrollert av Peg-out Authorization Keys (PAKs) som holdes av føderasjonsmedlemmer. I tillegg kan midler byttes umiddelbart via tredjepartsleverandører som SideSwap, noe som omgår oppgjørsforsinkelsen og gir raskere likviditet.


#### Maskinvare-sikkerhetsmoduler (HSM)

Sikkerheten håndheves strengt gjennom maskinvare. Funksjonærene oppbevarer ikke private nøkler på standardservere, men bruker i stedet maskinvaresikkerhetsmoduler (HSM-er). Disse enhetene er adskilt fra logikken på vertsserveren og er programmert med strenge regler. En HSM vil for eksempel nekte å signere en blokk hvis høyden ikke er større enn den forrige, noe som forhindrer omskriving av historikk. Denne "kontradiktoriske" sikkerhetsmodellen forutsetter at vertsserveren kan bli kompromittert, slik at nøklene forblir sikre selv om den fysiske lokasjonen blir brutt opp.


## Grunnleggende om Elements


<chapterId>1e9cfbed-108e-4067-afb9-4cf950cb43d3</chapterId>


:::video id=5652dcb2-4303-484c-8be5-d98063b39c1c:::

### Elements: Grunnlaget for Liquid


Elements er en åpen kildekode-blokkjedeplattform som er avledet fra Bitcoin Core-kodebasen. Den utvider Bitcoins funksjonalitet ved å muliggjøre sidekjedeuavhengige blokkjeder som kan overføre eiendeler til og fra Bitcoin. Mens Bitcoin Core driver Bitcoin-nettverket, er Elements programvaremotoren bak Liquid Network og andre tilpassede sidekjeder.


Forholdet er enkelt: Liquid er en spesifikk "instans" av en Elements-sidekjede, konfigurert for produksjonsbruk med en føderert konsensusmodell. Utviklere som er kjent med Bitcoin, vil finne Elements intuitiv, ettersom den beholder det samme RPC-grensesnittet (Remote Procedure Call) og kommandolinjestrukturen (`elements-cli`, `elements-d`, `elements-qt`). Den viktigste forskjellen ligger i konfigurasjonen: Ved å sette `chain=liquidv1` kobles en node til hovednettverket Liquid, mens `chain=elementsregtest` spinner opp et lokalt regresjonstestmiljø der utviklere kan generate blokker umiddelbart og teste uten eksterne avhengigheter.


#### Utstedelse av eiendeler

Et av de fremtredende trekkene ved Elements er utstedelse av egne aktiva. I motsetning til Ethereum, der tokens er komplekse smartkontrakter, er aktiva i Elements førsteklasses borgere som opprettes via en enkel RPC-kommando (`issueasset`).


- Unike identifikatorer:** Hver eiendel får en unik 64-tegns heksadesimal ID.
- Reissuance Tokens:** Utstedere kan eventuelt opprette reissuance tokens, som gir innehaveren rett til å utstede flere av eiendelen senere (nyttig for stablecoins eller security tokens).
- Asset Registry:** Siden hex-ID-er ikke kan leses av mennesker, tilordner Blockstream Asset Registry disse ID-ene til navn og tickere (f.eks. "USDT"), på samme måte som en DNS for eiendeler.


### Personvern via Confidential Transactions


Elements adresserer en av de primære begrensningene ved offentlige blokkjeder: mangelen på kommersielt personvern. På Bitcoin er alle transaksjonsbeløp synlige for hele verden. Elements introduserer **Confidential Transactions (CT)**, som kryptografisk skjuler beløpet og aktivatypen, samtidig som nettverket kan verifisere transaksjonens gyldighet.


Dette oppnås ved hjelp av **Pedersen Commitments** og **Range Proofs**.


- Pedersen Commitments** erstatter det synlige beløpet med en kryptografisk forpliktelse. På grunn av homomorfisk kryptering kan validatorer kontrollere at *Input Commitments = Output Commitments + Fees* uten å se de faktiske verdiene.
- Range Proofs** hindrer en bruker i å skape penger ut av løse luften (f.eks. ved å bruke negative tall) ved å bevise matematisk at den skjulte verdien er et positivt heltall innenfor et gyldig område.


For en utenforstående observatør viser en konfidensiell transaksjon gyldige inn- og utdata, men skjuler *hva* som sendes og *hvor mye*. Det er bare avsenderen og mottakeren (som har blendingsnøklene) som kan se klartekstdataene.


### Utvikling og arbeidsflyt for RPC


Samhandling med en Elements-node skjer primært gjennom JSON-RPC-grensesnittet. Dette gjør det mulig for applikasjoner skrevet i Python, JavaScript eller Go å kommunisere med blokkjeden.



- Oppsett:** En utvikler starter vanligvis i "regtest"-modus. Dette gjør det mulig å generere blokker umiddelbart (`generateblock`) for å bekrefte transaksjoner umiddelbart, uten å måtte bruke 1 minutt på å generere blokker i det aktive nettverket.
- Kommandoer:** Standard Bitcoin-kommandoer som `getblockchaininfo` er tilgjengelige, sammen med Elements-spesifikke kommandoer som `dumpblindingkey` (for revisjon av CT-er) eller `pegin` (for å flytte BTC inn i sidekjeden).
- Aliaser:** For å administrere flere noder (f.eks. en "sender" og en "mottaker" for testing) bruker utviklere ofte skallaliaser som `e1-cli` og `e2-cli`, som peker til forskjellige datakataloger og simulerer et peer-to-peer-nettverk på én enkelt maskin.


Denne arkitekturen gjør det mulig for utviklere å bygge sofistikerte finansapplikasjoner - for eksempel verdipapirplattformer eller private betalingsgatewayer - ved hjelp av de robuste og velkjente verktøyene i Bitcoin-økosystemet.


## Tilkobling av Bitcoin-lag


<chapterId>3ff2df4a-8995-4d5e-9b8a-cd114880e666</chapterId>


:::video id=31368c02-b979-44d7-b217-ceed96c7ca5c:::

### Infrastruktur på tvers av Layer og HTLC-er


Bitcoin-økosystemet har utviklet seg til en flerlagsarkitektur, med Mainchain som sørger for oppgjør, Lightning som tilbyr hastighet, og Liquid som muliggjør avanserte aktivafunksjoner. Å flytte verdier mellom disse lagene uten sentraliserte mellomledd krever en tillitsløs kryptografisk primitivitet: Hash Time Locked Contract (HTLC).


En HTLC skaper en betinget betalingskanal som kobler sammen uavhengige systemer på atomisk vis. Den fungerer gjennom to primære begrensninger: en **hash-lås** og en **tidslås**.


- Hash Lock:** Midler kan brukes umiddelbart hvis mottakeren avslører et hemmelig "forhåndsbilde" som samsvarer med en bestemt kryptografisk hash.
- Tidslåsen:** Hvis mottakeren ikke avslører hemmeligheten innen en bestemt tidsramme (blokkhøyde), kan den opprinnelige avsenderen kreve pengene tilbake.


Denne strukturen med to veier sørger for sikkerhet. I en utveksling på tvers av lagene brukes den samme hashlåsen i begge nettverkene. Når mottakeren avslører hemmeligheten for å kreve penger på det ene laget (f.eks. Liquid), blir hemmeligheten synlig for avsenderen, som deretter kan bruke den til å kreve tilsvarende penger på det andre laget (f.eks. Lightning). Denne kryptografiske bindingen garanterer at byttet enten fullføres for begge parter eller mislykkes for begge, noe som eliminerer risikoen for at den ene parten mister midler mens den andre vinner dem.


### Taproot og MuSig2-oppgradering


Eldre HTLC-er (SegWit v0) fungerte bra, men hadde personvern- og effektivitetsulemper. De krevde publisering av hele skriptlogikken on-chain, noe som gjorde byttetransaksjoner lett identifiserbare for blockchain-analytikere og dyrere på grunn av datastørrelsen. Introduksjonen av Taproot (SegWit v1) og MuSig2-protokollen har revolusjonert denne arkitekturen.


Taproot gir mulighet for **nøkkelaggregering** via MuSig2. I stedet for å avsløre et komplekst skript med flere offentlige nøkler, lar MuSig2 byttedeltakerne kombinere nøklene sine til én samlet offentlig nøkkel.


- Samarbeidende "Key Path":** Hvis begge parter er enige om byttet (den "lykkelige veien"), signerer de transaksjonen sammen. For nettverket ser dette identisk ut som en standard betaling med én signatur. Den bruker minimalt med blokkplass og avslører absolutt ingen informasjon om byttebetingelsene.
- Hvis en av partene ikke svarer eller er ondsinnet, avsløres det underliggende skriptet (som inneholder hash-/tidslåsene) først da. Dette er organisert i et Merkle-tre, slik at den ærlige parten bare kan avsløre den spesifikke grenen som trengs for å få tilbake penger, mens resten av kontraktslogikken holdes skjult.


### Praktisk implementering: Liquid-Lightning Swaps


I praksis muliggjør disse protokollene sømløs utveksling mellom Bitcoin-lagene. Et typisk Liquid-til-Lightning-bytte begynner med at en kunde ber om et bytte fra en tjenesteleverandør. Kunden oppgir en Lightning-faktura, og leverandøren låser den tilsvarende Liquid Bitcoin (L-BTC) til en Taproot-aktivert HTLC-adresse.


Atomariteten håndheves når betalingen gjøres opp. For å gjøre krav på L-BTC må tjenesteleverandøren ha preimage. De får dette preimage bare når de betaler kundens Lightning-faktura. I det øyeblikket Lightning-betalingen er fullført, avsløres forhåndsbildet, slik at leverandøren kan låse opp Liquid-midlene.


#### Wallet-abstraksjon og UTXO-administrasjon

For sluttbrukerne er denne kompleksiteten helt abstrahert. Moderne lommebøker som Aqua håndterer nøkkelgenerering, fakturaskaping og signeringsprosesser i bakgrunnen. Brukeren "betaler" ganske enkelt en Lightning-faktura ved hjelp av Liquid-saldoen. Bak kulissene administrerer tjenesten UTXO-konsolidering, og feier med jevne mellomrom små, uavhentede eller refunderte utganger for å opprettholde wallet-effektiviteten og minimere gebyrpåvirkningen i perioder med høy trafikk.


## Liquid Network Oversikt


<chapterId>1968db03-2364-46c0-9670-9e9844289ca1</chapterId>


:::video id=0bac0a62-90f2-41da-ac7c-330c0604bc61:::

### Liquid Network Arkitektur og konsensus


Liquid Network fungerer som en føderert sidekjede bygget på **Elements**-kodebasen. Mens Elements - en fork av Bitcoin Core - leverer programvaregrunnlaget, er Liquid implementeringen av produksjonsnettverket. I motsetning til Bitcoins Proof-of-Work, som er avhengig av konkurrerende mining, bruker Liquid en **Føderert konsensus**-modell.


Nettverket vedlikeholdes av femten globalt distribuerte "funksjonærer" Disse enhetene driver spesialiserte servere som utfører to viktige oppgaver:

1.  **Blokkproduksjon:** Funksjonærene bytter på å lage blokker i en deterministisk round-robin-plan, som genererer en ny blokk nøyaktig hvert minutt.

2.  **Blokksignering:** For at en blokk skal være gyldig, må den være signert av minst 11 av de 15 funksjonærene.


Denne 11 av 15-terskelen sikrer at nettverket tåler at opptil fire noder svikter uten å stoppe. Den største fordelen med denne avveiningen er **deterministisk endelighet**. Mens Bitcoin opererer med sannsynligheter, oppnår Liquid oppgjørssikkerhet etter to blokker (ca. to minutter). Når en blokk har en enkelt bekreftelse på toppen, kan ikke kjeden reorganiseres, noe som gjør den svært effektiv for arbitrasje og raske oppgjør.


### Confidential Transactions og innfødte eiendeler


Liquids definerende funksjon er standard bruk av **Confidential Transactions (CT)**. På Bitcoin mainchain er avsender, mottaker og beløp offentlige. Liquid forbedrer dette ved å blinde beløpet og eiendelstypen kryptografisk, mens avsender- og mottakeradressene forblir synlige for verifisering.


For å sikre at en bruker ikke kan skrive ut penger (f.eks. ved å sende negative beløp), bruker Liquid **Pedersen Commitments** og **Range Proofs**. Disse kryptografiske primitivene gjør det mulig for nettverket å verifisere at *Input = Output + Fees* og at alle verdier er positive heltall, uten å avsløre de spesifikke tallene til den offentlige hovedboken. Bare deltakerne som har blindingsnøklene, kan se de dekrypterte dataene.


#### Utstedelse av eiendeler

Liquid behandler alle aktiva som "native" Enten det er Liquid Bitcoin (L-BTC), en stablecoin som USDT eller et verdipapir token, deler de alle den samme arkitekturen. Utstedelse av en eiendel krever ingen smartkontrakter - bare et enkelt RPC-anrop.


- Uregulerte eiendeler:** Kan utstedes uten tillatelse av hvem som helst.
- Regulerte eiendeler:** Ved å bruke Blockstream Asset Management Platform (AMP) kan utstedere håndheve regler for etterlevelse (som KYC/AML) ved å kreve en ny signatur fra en autorisasjonsserver før en eiendel kan flyttes.


### Den toveis pinnen og dynamisk føderasjon


Broen mellom Bitcoin og Liquid er **Two-Way Peg**. Den lar brukerne flytte BTC til sidekjeden (Peg-in) og tilbake til mainchain (Peg-out).


**Peg-in-prosessen:**

Dette er uten tillatelse. En bruker sender BTC til en føderasjonskontrollert adresse. For å beskytte mot omorganiseringer av Bitcoin-blokkjeden må disse midlene vente på **102 bekreftelser** (ca. 17 timer) før tilsvarende L-BTC utstedes på sidekjeden.


**Peg-out-prosessen:**

For å gå tilbake til Bitcoin brennes L-BTC. For å forhindre tyveri av de underliggende Bitcoin-reservene er peg-outs imidlertid ikke helautomatiske. De krever autorisasjon fra et medlem som innehar en **Peg-Out Authorization Key (PAK)**. Selve Bitcoin-midlene er sikret i en wallet med 11 av 15 multisignaturer, med nøkler i maskinvaresikkerhetsmoduler (HSM-er) som er luftgapet fra funksjonærenes hovedservere.


**Dynamisk føderasjon (Dynafed):**

For å sikre lang levetid bruker Liquid Dynafed, en protokoll som gjør det mulig for nettverket å rotere funksjonærer eller oppdatere parametere uten en hard fork. Hvis en funksjonær må byttes ut, sender nettverket ut en overgangstransaksjon. Etter en overlappingsperiode på to uker tar den nye konfigurasjonen over, slik at føderasjonen kan utvikle seg sømløst og samtidig opprettholde kontinuerlig oppetid.


## Økosystem og kapitalmarkeder


<chapterId>5f4c0e50-b435-4b6c-b8b7-c55cc1a35431</chapterId>


:::video id=07e0b82f-2d60-4eb3-9b5d-2ccb7ad06e8a:::

### Liquid Network: Forretningsstrategi og økosystem


Liquid er mer enn en teknisk sidekjede; det er et forretningsfokusert infrastrukturlag som er utviklet for å håndtere de komplekse kravene i kapitalmarkedene som Bitcoin mainchain ikke kan støtte effektivt. Mens Lightning Network er optimalisert for høyfrekvente betalinger med lav verdi, er Liquid rettet mot overføringer med høy verdi, utstedelse av aktiva og oppgjør mellom børser.


Økosystemet drives av **Liquid Federation**, et konsortium bestående av ca. 73 selskaper, inkludert børser, trading desks og infrastrukturleverandører. Denne samarbeidsmodellen gjenspeiler tradisjonelle finansielle clearinghus, men opererer med større åpenhet og betydelig kortere oppgjørstid (2 minutter mot T+2 dager).


### Tokenisering av eiendeler i den virkelige verden (RWA)


Kjerneforretningen for Liquid er "Tokenization" - å representere verdier i den virkelige verden (aksjer, obligasjoner, mining-kontrakter) som digitale tokens på blokkjeden. Dette gir tre primære fordeler:

1.  **Globale markeder døgnet rundt:** Fjerning av banktider og geografiske begrensninger.

2.  **Driftseffektivitet:** Eliminering av avstemmingsfeil ved hjelp av en delt, uforanderlig hovedbok.

3.  **Atomoppgjør:** Reduserer motpartsrisiko ved å sikre at levering skjer samtidig med betaling.


#### Regulerte eiendeler og AMP

De fleste institusjonelle aktiva kan ikke handles uten tillatelse på grunn av juridiske krav. Asset Management Platform (AMP)** er den tekniske standarden som håndhever disse reglene.


- Hvitelisting:** Utstedere kan begrense beholdning og handel til KYC-verifiserte adresser.
- Multisig Control:** Samsvarstiltak (som å fryse stjålne midler eller utstede tapte tokens på nytt) administreres via multisignaturautorisasjon, noe som sikrer at ingen enkeltansatt kan handle ensidig.


Denne infrastrukturen er i drift i dag. Plattformer som **Stalker** tilbyr ende-til-ende-tokeniseringstjenester i Europa, mens **Sideswap** fungerer som en desentralisert børs og wallet uten depot, noe som muliggjør peer-to-peer-handel med eiendeler som **Blockstream Mining Note (BMN)** og tokeniserte MicroStrategy-aksjer (CMSTR).


### Suksess i den virkelige verden: Casestudien av Mayfell


Det mest overbevisende beviset på Liquids nytteverdi kommer fra **Mayfell** i Mexico. I et marked der tradisjonell finansiering baserer seg på gjeldsbrev på papir - som er utsatt for tap, svindel og treg behandling - flyttet Mayfell hele infrastrukturen til Liquid.



- Omfang:** Over 25 000 gjeldsbrev utstedt, til en verdi av mer enn 1,5 milliarder dollar.
- Personvern:** Ved hjelp av Liquids Confidential Transactions er lånebeløpene kun synlige for utlåner og låntaker, noe som ivaretar forretningshemmeligheter samtidig som revisorer kan verifisere hovedbokens integritet.
- Effekt:** Ved å koble långivere som ikke er banker, til globale kapitalmarkeder via blokkjeden, reduserte Mayfell kostnadene og utvidet tilgangen til kreditt for meksikanske små og mellomstore bedrifter, noe som viser at Liquids verdiforslag strekker seg langt utover spekulativ handel.


### Strategisk posisjonering i forhold til andre kjeder


Liquid konkurrerer i et overfylt marked av tokeniseringsplattformer (Ethereum, Solana osv.), men det har klare strategiske fordeler:


- Regulatorisk klarhet:** Liquid bruker Bitcoin (L-BTC) som sin opprinnelige eiendel. Den har ikke en forhåndsutvunnet token eller en ICO, slik at man unngår risikoen for "uregistrert sikkerhet" som plager andre L1-blokkjeder.
- Stabilitet:** I motsetning til Ethereums kontomodell, der mislykkede transaksjoner fortsatt koster gassavgifter, er Liquids UTXO-modell deterministisk og pålitelig for virksomhetskritiske finansielle data.
- Personvern:** Standard konfidensialitet er et krav for de fleste finansinstitusjoner, en funksjon Liquid tilbyr naturlig som offentlige kjeder sliter med å implementere uten komplekse tilleggsprogrammer.


For utviklere gir dette økosystemet en klar mulighet: å bygge verktøyene (dashbord, lommebøker, compliance-integrasjoner) som bygger bro mellom tradisjonell finans og Bitcoins sikre oppgjørslag.


## Blockstream AMP


<chapterId>4f21a0a7-0dc0-44cf-8a3a-d9e2f8a3f05f</chapterId>


:::video id=f00822b4-dc1a-46ff-adfc-ff7c97a0024d:::

### Blockstream AMP: Tillatt kontroll av aktiva på Liquid


Blockstream AMP (Asset Management Platform) fungerer som et kritisk infrastrukturlag på Liquid Network, designet spesielt for utstedere av regulerte digitale verdipapirer og stablecoins. Mens Liquid gir et tillatelsesfritt basislag med utstedelse av egne aktiva, krever regulerte enheter ofte streng overvåking og samsvarsfunksjoner. AMP bygger bro over dette gapet ved å introdusere et kontrollag med tillatelse over spesifikke aktiva uten å ofre personvernfordelene ved Liquids Confidential Transactions.


Plattformens kjerneverdi hviler på to primære egenskaper: omfattende utstedersynlighet og transaksjonsautorisasjon. I motsetning til standard Liquid-aktiva der beløp og typer er blinded for alle andre enn deltakerne, gjør AMPaktiva det mulig for utstederen å opprettholde et fullstendig unblinded-revisjonsspor. Denne gjennomsiktigheten er avgjørende for lovpålagt rapportering og interne revisjoner. Videre håndhever AMP en streng autorisasjonsmodell gjennom en medsigneringsmekanisme. Hver overføring av en AMP-aktiva krever en signatur fra AMP-serveren. Dette gjør det mulig for utstedere å håndheve komplekse regler off-chain - for eksempel frysing av kontoer, hvitelisting av akkrediterte investorer eller innføring av overføringsgrenser - som i praksis fungerer som en sentralisert portvokter i et desentralisert nettverk.


#### Operasjonelle avveininger

Denne arkitekturen innebærer spesifikke avveininger. Systemet er avhengig av AMP-serverens tilgjengelighet; hvis serveren fungerer som medunderskriver og går offline, stanser likviditeten i aktivaene. I tillegg må investorene akseptere at utstederen har fullt innsyn i beholdningene deres, samtidig som personvernet mellom brukerne opprettholdes. Denne modellen er ideell for kompatible sikkerhetstokener, men uegnet for sensurresistente kryptovalutaer.


### Arkitekturutvikling og integrasjonsveier


AMP-økosystemet er i ferd med å gå fra sin første iterasjon til en mer fleksibel og interoperabel "versjon 2"-arkitektur. Det gamle systemet krevde at utstedere opprettholdt fullt synkroniserte Elements-noder og tvang utviklere til å stole på den monolittiske Green SDK-en. Selv om dette var funksjonelt, skapte det høye tekniske inngangsbarrierer og begrensede wallet-valg.


Neste generasjons arkitektur forenkler disse kravene fundamentalt ved å flytte kompleksiteten til serveren. I denne nye modellen håndterer AMP-serveren det tunge arbeidet med transaksjonskonstruksjon, UTXO-valg og gebyrberegning. Den presenterer utstederen med en delvis signert Elements-transaksjon (PSET) som bare krever en signatur. Denne "smart server, dum wallet"-tilnærmingen eliminerer behovet for at utstedere kjører fulle noder, og gjør det mulig å bruke maskinvarelommebøker og standard oppsett med flere signaturer for finansforvaltning.


For utviklere betyr denne utviklingen at de beveger seg bort fra proprietære SDK-er og over til standard deskriptorer og PSET-arbeidsflyter. Lommebøker kan nå registrere multisignaturbeskrivelser hos AMP-serveren for å etablere autorisasjonsrettigheter. Dette tilpasser AMP-utviklingen til bredere Bitcoin wallet-standarder, noe som gjør integrasjon tilgjengelig for alle applikasjoner som kan håndtere PSBT/PSET-formater. Utviklere som bygger i dag, oppfordres til å bruke verktøy som Liquid Wallet Kit (LWK), som støtter disse moderne, deskriptorbaserte arkitekturene og sørger for at applikasjonene deres er fremtidssikret for de nye AMP-standardene.


### Liquid Wallet-økosystemet og konfidensialitet


Å bygge applikasjoner på Liquid krever at man navigerer i en mer kompleks stabel enn standard Bitcoin-utvikling på grunn av funksjoner som native assets og Confidential Transactions. Økosystemet støttes av en lagdelt arkitektur: biblioteker på lavt nivå, som `secp256k1-zkp`, håndterer kryptografiske primitiver, mens verktøysett på høyere nivå håndterer wallet-logikk.


Historisk sett har Green Development Kit (GDK) vært en omfattende, men rigid løsning. Det moderne alternativet er Liquid Wallet Kit (LWK), som tilbyr en modulær tilnærming. LWK deler opp problemene i separate kasser - som håndterer deskriptorer, signering og maskinvarekommunikasjon uavhengig av hverandre - noe som gir utviklere fleksibilitet til å bygge skreddersydde løsninger uten å måtte forholde seg til et monolittisk bibliotek.


#### Håndtering av Confidential Transactions

Den største utfordringen i dette økosystemet er å håndtere blindingens livssyklus. I Liquid krypteres transaksjonsutdata ved hjelp av ECDH-nøkkelutveksling (Elliptic Curve Diffie-Hellman). En avsender bruker mottakerens offentlige nøkkel til å kryptere beløp og typer, noe som genererer et rekkeviddebevis som verifiserer transaksjonens gyldighet uten å avsløre verdier.


For at en wallet skal fungere, må den lykkes med å reversere denne prosessen. Når en wallet oppdager en innkommende transaksjon, forsøker den å oppheve blindingen av utdataene ved hjelp av sin private blindingsnøkkel. Hvis den delte hemmeligheten stemmer overens, kan wallet dekryptere verdien og legge den til brukerens saldo. Denne prosessen er beregningsintensiv og krever presis styring av blindingfaktorer for å sikre at transaksjonene er matematisk balanserte, en kompleksitet som verktøy som LWK har som mål å abstrahere bort for utvikleren.


# Teknisk


<partId>53629f58-b9e0-4a10-8ab2-d51b047414f8</partId>

<chapterId>f1fdf2b0-4b6a-4ba7-812c-7586dcb36713</chapterId>


## Breez SDK - Nodeless


<chapterId>fb77442c-3d1e-427e-b2f5-16668ce4c643</chapterId>


:::video id=1a6289b5-fdae-4320-b5b1-41925150108c:::

### Introduksjon til Breez Liquid SDK


Breez Liquid SDK er et selvforvaltende verktøysett med åpen kildekode som er utviklet for å bygge bro mellom Liquid Network og det bredere Bitcoin-økosystemet. Dets primære oppgave er å abstrahere kompleksiteten i Lightning Network-nodeadministrasjon og atombytter, slik at utviklere kan bygge friksjonsfrie finansielle applikasjoner.


Kjernelogikken er bygget med en "mobile first"-filosofi og er skrevet i Rust for ytelse og sikkerhet, men den bruker UniFFI (Unified Foreign Function Interface) for å tilby native bindinger for Kotlin, Swift, Python, C#, Dart og Flutter. Dette sikrer at utviklere kan integrere Bitcoin-funksjonalitet i sitt foretrukne miljø uten å måtte håndtere kryptografiske operasjoner på lavt nivå.


**Transaksjonstyper som støttes:**

SDK opererer med Liquid som sin "hjemmebase" Den utmerker seg med tre spesifikke operasjoner:

1.  **Liquid-til-Liquid:** Direkte on-chain-overføringer.

2.  **Liquid-til-Lightning:** Betaling av Lightning-fakturaer ved bruk av Liquid-midler.

3.  **Liquid-til-Bitcoin:** Bytte av midler direkte til Bitcoin mainchain.


*Merk: SDK-en støtter ikke direkte Lightning-til-Lightning- eller Bitcoin-til-Bitcoin-transaksjoner. Det er utelukkende et Liquid-sentrisk verktøy


### Betalingsarkitekturer: Submarine swapper


For å oppnå interoperabilitet mellom Liquid, Lightning og Bitcoin uten sentraliserte depotmottakere, baserer Breez seg på **Submarine Swaps**. Dette er atomoperasjoner der en transaksjon enten fullføres på begge nettverkene eller mislykkes på begge, noe som sikrer at midler aldri går tapt i transitt.


#### Lynsending (ubåtbytte)

Når en bruker betaler en Lightning-faktura, sender SDK-en en "lock-up"-transaksjon på Liquid Network. Dette setter i praksis midlene i sperret konto. Bytteleverandøren (Boltz) oppdager dette, betaler Lightning-fakturaen og bruker deretter betalingsbildet (den kryptografiske kvitteringen) til å kreve de låste Liquid-midlene.


#### Lynmottak (omvendt ubåtbytte)

Mottak av Lightning er den omvendte prosessen. Brukeren genererer en faktura, og swap-leverandøren låser midler på Lightning Network. SDK overvåker denne prosessen via WebSockets. Når låsen er bekreftet, utfører SDK-en automatisk en kravtransaksjon for å flytte tilsvarende midler til brukerens Liquid wallet.


#### Tverrkjedet Bitcoin

For Liquid-til-Bitcoin-overføringer bruker arkitekturen en "dual-swap"-mekanisme. Lock-up-transaksjoner skjer på begge kjedene samtidig. Avsenderen gjør krav på midler på Bitcoin, mens mottakeren gjør krav på midler på Liquid. Dette muliggjør tillitsløs brobygging uten å være avhengig av federated peg-outs eller sentraliserte sentraler.


### Utvikler Interface og automatisert administrasjon


Breez SDK forenkler utvikleropplevelsen ved å kondensere komplekse finansielle strømmer til en standardisert tretrinnsprosess: **Koble til, forberede og utføre**.


1.  **Connect:** Initialiserer wallet, synkroniserer med blokkjeden ved hjelp av Liquid Wallet Kit (LWK), og oppretter WebSocket-tilkoblinger for sanntidsovervåking.

2.  **Forberede:** Før du setter inn penger, beregner og returnerer dette trinnet alle tilknyttede nettverksgebyrer og byttekostnader, slik at brukergrensesnittet kan presentere en tydelig totalsum for brukeren.

3.  **Dette trinnet konstruerer transaksjonen, sender den og setter i gang byttet.


#### Automatiserte sikkerhetsmekanismer

En av SDK-enes mest kritiske funksjoner er **Automated Refund Management**. I tilfelle nettverksfeil eller en ikke-samarbeidsvillig motpart, kan midler teoretisk sett bli sittende fast i en tidslåst kontrakt. SDK-en abstraherer gjenopprettingslogikken fullstendig. Den overvåker statusen til hver swap; hvis en swap mislykkes eller tidsavbrytes, konstruerer og sender SDK-en automatisk refusjonstransaksjonen for å returnere midler til brukerens wallet.


I tillegg håndterer SDK **Metadata Resolution**. Den slår sammen off-chain-byttedata (levert av Boltz-bytteprogrammet) med on-chain-transaksjonshistorikk. Dette sikrer at brukerens transaksjonshistorikk er lesbar for mennesker, og viser fakturadetaljer og betalingskontekst i stedet for bare rå heksadesimale transaksjonshashes.


# Siste del


<partId>7ec65e6b-6e63-41b6-92ea-6a13bc77c3ff</partId>


## Anmeldelser og rangeringer


<chapterId>e5f6348c-e207-40ae-8fef-6a068a6bf741</chapterId>


<isCourseReview>true</isCourseReview>

## Avsluttende eksamen


<chapterId>b13c4aa8-ced6-11f0-8515-afd3f381a001</chapterId>

<isCourseExam>true</isCourseExam>

## Konklusjon


<chapterId>e30a5587-d74b-4360-87fb-bbf3de1b0ba8</chapterId>

<isCourseConclusion>true</isCourseConclusion>