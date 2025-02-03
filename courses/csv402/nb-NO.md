---
name: RGB-protokollen, fra teori til praksis
goal: Tilegne seg ferdighetene som trengs for å forstå og bruke RGB
objectives: 

  - Forstå de grunnleggende konseptene i RGB-protokollen
  - Beherske prinsippene for validering på klientsiden og Bitcoin-forpliktelser
  - Lær hvordan du oppretter, administrerer og overfører RGB-kontrakter
  - Slik bruker du en RGB-kompatibel Lightning-node

---
# Oppdage RGB-protokollen

Dyk ned i RGB-verdenen, en protokoll som er utformet for å implementere og håndheve digitale rettigheter i form av kontrakter og eiendeler, basert på konsensusreglene og driften av Bitcoin-blokkjeden. Dette omfattende kurset guider deg gjennom det tekniske og praktiske grunnlaget for RGB, fra konseptene "Client-side Validation" og "Single-use Seals" til implementering av avanserte smartkontrakter.

Gjennom et strukturert, trinnvis program vil du oppdage mekanismene for validering på klientsiden, deterministiske forpliktelser på Bitcoin og interaksjonsmønstre mellom brukere. Lær hvordan du oppretter, administrerer og overfører RGB-tokens på Bitcoin eller Lightning Network.

Enten du er utvikler, Bitcoin-entusiast eller bare nysgjerrig på å lære mer om denne teknologien, vil dette kurset gi deg verktøyene og kunnskapen du trenger for å mestre RGB og bygge innovative løsninger på Bitcoin.

Kurset er basert på et direktesendt seminar i regi av Fulgur'Ventures, med tre anerkjente lærere og RGB-eksperter som undervisere.

+++
# Innledning

<partId>c6f7a70f-d894-595f-8c0a-b54759778839</partId>

## Presentasjon av kurset

<chapterId>cf2f087b-6c6b-5037-8f98-94fc9f1d7f46</chapterId>

Hei alle sammen, og velkommen til dette kurset dedikert til RGB, et klientsidevalidert smartkontraktsystem som kjører på Bitcoin og Lightning Network. Strukturen i dette kurset er utformet for å muliggjøre en grundig utforskning av dette komplekse emnet. Slik er kurset organisert:

**Seksjon 1: Teori

Den første delen er dedikert til de teoretiske konseptene som trengs for å forstå det grunnleggende ved validering på klientsiden og RGB. Som du vil oppdage i dette kurset, introduserer RGB en rekke tekniske konsepter som vanligvis ikke brukes i Bitcoin. I denne delen finner du også en ordliste med definisjoner av alle begreper som er spesifikke for RGB-protokollen.

**Seksjon 2: Øvelse

Den andre delen fokuserer på anvendelsen av de teoretiske konseptene i del 1. Vi lærer hvordan man lager og manipulerer RGB-kontrakter. Vi skal også se hvordan man programmerer med disse verktøyene. Disse to første delene presenteres av Maxim Orlovsky.

**Seksjon 3: Bruksområder

Den siste delen ledes av andre foredragsholdere som presenterer konkrete RGB-baserte bruksområder, for å belyse reelle brukstilfeller.

---
Dette kurset sprang opprinnelig ut av en to ukers bootcamp for avansert utvikling i Viareggio i Toscana, arrangert av [Fulgur'Ventures] (https://fulgur.ventures/). Den første uken, som fokuserte på Rust og SDK-er, finner du i dette andre kurset:

https://planb.network/courses/lnp402
I dette kurset fokuserer vi på den andre uken av bootcampen, som fokuserer på RGB.

**Uke 1 - LNP402:**

![RGB-Bitcoin](assets/fr/001.webp)

**Uke 2 - Nåværende opplæring CSV402:**

![RGB-Bitcoin](assets/fr/002.webp)

Tusen takk til arrangørene av disse live-kursene og til de tre lærerne som deltok:


- Maxim Orlovskij: *Ex Tenebrae sententia sapiens dominabitur astris. Cypher, AI, robotikk, transhumanisme. Skaperen av RGB, Prime, Radiant og lnp_bp, mycitadel_io & cyphernet_io* ;
- Hunter Trujilo: *Utvikler, Rust, Bitcoin, Lightning, RGB* ;
- Federico Tenga: *Jeg gjør mitt for å gjøre verden til en cypherpunk-dystopi. Jobber for tiden med RGB hos Bitfinex*.

Den skriftlige versjonen av dette kurset ble utarbeidet ved hjelp av to hovedressurser:


- Videoer av Maxim Orlovsky, Hunter Trujilo og Frederico Tengas seminar på Lightning Bootcamp ;
- RGB-dokumentasjonen, hvis produksjon ble sponset av [Bitfinex] (https://www.bitfinex.com/).

# RGB i teorien

<partId>80e797ee-3f33-599f-ab82-e82eeee08219</partId>

## Introduksjon til distribuerte databehandlingskonsepter

<chapterId>f52f8af5-5d7c-588b-b56d-99b97176204b</chapterId>

![video](https://youtu.be/AF2XbifPGXM)

RGB er en protokoll som er utviklet for å anvende og håndheve digitale rettigheter (i form av kontrakter og eiendeler) på en skalerbar og konfidensiell måte, basert på konsensusreglene og -operasjonene i Bitcoin-blokkjeden. Målet med dette første kapittelet er å presentere de grunnleggende konseptene og terminologien rundt RGB-protokollen, og spesielt fremheve de nære koblingene til grunnleggende distribuerte databehandlingskonsepter som validering på klientsiden og engangsforseglinger.

I dette kapittelet utforsker vi det grunnleggende ved **distribuerte konsensussystemer** og ser hvordan RGB passer inn i denne familien av teknologier. Vi introduserer også hovedprinsippene som hjelper oss å forstå hvorfor RGB har som mål å være utvidbar og uavhengig av Bitcoins egen konsensusmekanisme, samtidig som vi støtter oss på den når det er nødvendig.

### Innledning

Distribuert databehandling, en spesifikk gren av informatikken, studerer protokollene som brukes til å sirkulere og behandle informasjon i et nettverk av noder. Til sammen utgjør disse nodene og protokollreglene det som kalles et distribuert system. Blant de viktigste egenskapene som kjennetegner et slikt system, er :


- Muligheten for uavhengig verifisering og validering** av visse data fra hver node;
- Nodenes mulighet til å konstruere (avhengig av protokollen) en fullstendig eller delvis oversikt over informasjonen. Disse visningene er det distribuerte systemets **tilstander**;
- Den **kronologiske rekkefølgen** av operasjoner, slik at data er tidsstemplet på en pålitelig måte og det er enighet om hendelsesforløpet (sekvensen av tilstander).

Begrepet **konsensus** i et distribuert system dekker særlig to aspekter:


- Anerkjennelse av gyldigheten** av tilstandsendringer (i henhold til protokollregler);
- Avtalen om rekkefølgen** på disse tilstandsendringene, som gjør det umulig å omskrive eller reversere validerte operasjoner i ettertid (dette er også kjent i Bitcoin som "double-spend protection").

Den første funksjonelle, tillatelsesfrie implementeringen av en distribuert konsensusmekanisme ble introdusert av Satoshi Nakamoto med Bitcoin, takket være den kombinerte bruken av en blockchain-datastruktur og en Proof-of-Work (PoW)-algoritme. I dette systemet avhenger troverdigheten til blokkhistorikken av datakraften som nodene (utvinnerne) bruker på den. Bitcoin er derfor et viktig og historisk eksempel på et distribuert konsensussystem som er åpent for alle (*permissionless*).

I en verden av blokkjeder og distribuert databehandling kan vi skille mellom to grunnleggende paradigmer: ***blokkjeder*** i tradisjonell forstand, og ***statskanaler***, der Lightning Network er det beste eksemplet i produksjon. Blokkjeden er definert som et register over kronologisk ordnede hendelser, replikert ved konsensus i et åpent, tillatelsesfritt nettverk. State channels, derimot, er peer-to-peer-kanaler som gjør det mulig for to (eller flere) deltakere å opprettholde en oppdatert tilstand utenfor kjeden, og som kun bruker blokkjeden når de åpner og lukker disse kanalene.

I forbindelse med Bitcoin er du uten tvil kjent med prinsippene for utvinning, desentralisering og endelighet av transaksjoner på blokkjeden, samt hvordan betalingskanaler fungerer. Med RGB introduserer vi et nytt paradigme kalt **Validering på klientsiden**, som i motsetning til blockchain eller Lightning består i lokal (klientsiden) lagring og validering av tilstandsovergangene til en smartkontrakt. Dette skiller seg også fra andre "DeFi-teknikker" (_rollups_, _plasma_, _ARK_ osv.), ved at Client-side Validation er avhengig av blokkjeden for å forhindre dobbeltbruk og for å ha et tidsstemplingssystem, samtidig som registeret over tilstander og overganger utenfor kjeden bare oppbevares hos de berørte deltakerne.

![RGB-Bitcoin](assets/fr/003.webp)

Senere introduserer vi også et viktig begrep: begrepet "**stash**", som refererer til settet med data på klientsiden som kreves for å bevare statusen til en kontrakt, ettersom disse dataene ikke replikeres globalt over hele nettverket. Til slutt ser vi på begrunnelsen bak RGB, en protokoll som drar nytte av validering på klientsiden, og hvorfor den utfyller eksisterende tilnærminger (blokkjede og tilstandskanaler).

### Trilemmaer i distribuert databehandling

For å forstå hvordan validering på klientsiden og RGB løser problemer som ikke er løst av blockchain og Lightning, la oss oppdage tre store "trilemmaer" innen distribuert databehandling:


- Skalerbarhet, desentralisering, personvern** ;
- CAP**-teoremet (konsistens, tilgjengelighet, partisjonstoleranse) ;
- CIA**-trilemmaet (konfidensialitet, integritet og tilgjengelighet).

#### 1. Skalerbarhet, desentralisering og konfidensialitet


- Blockchain (Bitcoin)**

Blockchain er svært desentralisert, men ikke veldig skalerbar. Dessuten er konfidensialiteten begrenset, siden alt ligger i et globalt, offentlig register. Vi kan prøve å forbedre konfidensialiteten med nullkunnskapsteknologier (konfidensielle transaksjoner, mimblewimble-ordninger osv.), men den offentlige kjeden kan ikke skjule transaksjonsgrafen.


- Lyn/statskanaler**

Statlige kanaler (som Lightning Network) er mer skalerbare og mer private enn blokkjeder, ettersom transaksjonene foregår utenfor kjeden. Plikten til å offentliggjøre visse elementer (finansieringstransaksjoner, nettverkstopologi) og overvåking av nettverkstrafikken kan imidlertid delvis gå på bekostning av konfidensialiteten. Desentraliseringen lider også under dette: ruting er kontantintensivt, og store noder kan bli sentraliseringspunkter. Det er nettopp dette fenomenet vi begynner å se på Lightning.


- Validering på klientsiden (RGB)**

Dette nye paradigmet er enda mer skalerbart og mer konfidensielt, fordi vi ikke bare kan integrere proof-of-knowledge-teknikker med null-avsløring, men det finnes heller ingen global transaksjonsgraf, siden ingen har hele registeret. På den annen side innebærer det også et visst kompromiss med desentraliseringen: Utstederen av en smartkontrakt kan ha en sentral rolle (som en "kontraktsutsteder" i Ethereum). I motsetning til blokkjeder lagrer og validerer du med Client-side Validation bare de kontraktene du er interessert i, noe som forbedrer skalerbarheten ved at du ikke trenger å laste ned og verifisere alle eksisterende tilstander.

![RGB-Bitcoin](assets/fr/004.webp)

#### 2. CAP-teoremet (konsistens, tilgjengelighet, partisjonstoleranse)

CAP-teoremet understreker at det er umulig for et distribuert system å tilfredsstille konsistens (*Konsistens*), tilgjengelighet (*Tilgjengelighet*) og partisjonstoleranse (*Partisjonstoleranse*) på samme tid.


- Blockchain**

Blokkjeden favoriserer konsistens og tilgjengelighet, men fungerer ikke så godt med nettverkspartisjonering: Hvis du ikke kan se en blokk, kan du ikke handle og ha samme oversikt som hele nettverket.


- Lyn** (på fransk)

Et system med tilstandskanaler har tilgjengelighet og partisjoneringstoleranse (siden to noder kan forbli koblet til hverandre selv om nettverket er fragmentert), men den generelle konsistensen avhenger av åpning og lukking av kanaler i blokkjeden.


- Validering på klientsiden (RGB)**

Et system som RGB tilbyr konsistens (hver deltaker validerer sine data lokalt, uten tvetydighet) og partisjoneringstoleranse (du beholder dataene dine autonomt), men garanterer ikke global tilgjengelighet (alle må sørge for at de har de relevante delene av historikken, og noen deltakere kan la være å publisere noe eller slutte å dele visse typer informasjon).

![RGB-Bitcoin](assets/fr/005.webp)

#### 3. CIA-trilemmaet (konfidensialitet, integritet og tilgjengelighet)

Dette trilemmaet minner oss om at konfidensialitet, integritet og tilgjengelighet ikke kan optimaliseres samtidig. Blockchain, Lightning og Client-side Validation faller ulikt inn i denne balansen. Tanken er at ingen enkeltstående systemer kan levere alt; det er nødvendig å kombinere flere tilnærminger (blockchain-tidsstempling, Lightnings synkrone tilnærming og lokal validering med RGB) for å få en sammenhengende pakke som gir gode garantier i hver dimensjon.

![RGB-Bitcoin](assets/fr/006.webp)

### Blokkjedens rolle og begrepet sharding

Blokkjeden (i dette tilfellet Bitcoin) fungerer først og fremst som en _tidsstemplingsmekanisme_ og beskyttelse mot dobbeltbruk. I stedet for å sette inn de komplette dataene til en smart kontrakt eller et desentralisert system, inkluderer vi ganske enkelt **kryptografiske forpliktelser** (_commitments_) til transaksjoner (i betydningen validering på klientsiden, som vi kaller "tilstandsoverganger"). Dermed :


- Vi frigjør blokkjeden fra en stor mengde data og logikk;
- Hver bruker lagrer bare den historikken som er nødvendig for sin egen del av kontrakten (sin "*shard*"), i stedet for å replikere den globale tilstanden.

Sharding er et konsept som har sin opprinnelse i distribuerte databaser (f.eks. MySQL for sosiale nettverk som Facebook eller Twitter). For å løse problemet med datavolum og synkroniseringsforsinkelser segmenteres databasen i _shards_ (USA, Europa, Asia osv.). Hvert segment er lokalt konsistent og bare delvis synkronisert med de andre.

For smartkontrakter av RGB-typen deler vi opp i henhold til selve kontraktene. Hver kontrakt er en uavhengig _deling_. Hvis du for eksempel bare har USDT-tokens, trenger du ikke å lagre eller validere hele historikken til et annet token som USDC. På Bitcoin gjør ikke blokkjeden _sharding_: du har et globalt sett med UTXO-er. Med validering på klientsiden beholder hver deltaker bare de kontraktsdataene den har eller bruker.

Vi kan derfor se for oss økosystemet på følgende måte:


- Blokkjeden (Bitcoin)** som et fundament som sikrer fullstendig replikering av et minimumsregister og fungerer som et tidsstemplingslag;
- Lightning Network** for raske, konfidensielle transaksjoner, fortsatt basert på sikkerheten og det endelige oppgjøret i Bitcoin-blokkjeden;
- RGB og Client-side Validation** for å legge til mer kompleks smartkontraktslogikk, uten å rote til blokkjeden eller miste konfidensialiteten.

![RGB-Bitcoin](assets/fr/007.webp)

Disse tre elementene danner en trekantet helhet, i stedet for en lineær stabel med "lag 2", "lag 3" og så videre. Lightning kan kobles direkte til Bitcoin, eller knyttes til Bitcoin-transaksjoner som inneholder RGB-data. På samme måte kan en "BiFi"-bruk (finans på Bitcoin) settes sammen med blokkjeden, med Lightning og med RGB i henhold til behov for konfidensialitet, skalerbarhet eller kontraktslogikk.

![RGB-Bitcoin](assets/fr/008.webp)

### Begrepet tilstandsoverganger

I ethvert distribuert system er målet med valideringsmekanismen å kunne **bestemme gyldigheten og den kronologiske rekkefølgen av tilstandsendringer**. Målet er å verifisere at protokollreglene er overholdt, og å bevise at disse tilstandsendringene følger etter hverandre i en endelig, uangripelig rekkefølge.

For å forstå hvordan denne valideringen fungerer i forbindelse med **Bitcoin** og, mer generelt, for å forstå filosofien bak validering på klientsiden, la oss først ta en titt tilbake på mekanismene i Bitcoin-blokkjeden, før vi ser hvordan validering på klientsiden skiller seg fra dem og hvilke optimaliseringer den muliggjør.

![RGB-Bitcoin](assets/fr/009.webp)

Når det gjelder Bitcoin-blokkjeden, er transaksjonsvalidering basert på en enkel regel:


- Alle nettverksnoder laster ned hver blokk og transaksjon;
- De validerer disse transaksjonene for å verifisere at UTXO-settet (alle ubrukte utganger) har utviklet seg riktig;
- De lagrer disse dataene (i form av blokker) slik at historikken kan spilles av på nytt ved behov.

![RGB-Bitcoin](assets/fr/010.webp)

Denne modellen har imidlertid to store ulemper:


- Skalerbarhet**: Siden hver node må behandle, verifisere og arkivere alles transaksjoner, er det en åpenbar grense for transaksjonskapasiteten, særlig knyttet til den maksimale blokkstørrelsen (1 MB i gjennomsnitt i løpet av 10 minutter for Bitcoin, unntatt informasjonskapsler);
- Personvern**: Alt sendes og lagres offentlig (beløp, destinasjonsadresser osv.), noe som begrenser konfidensialiteten i utvekslingene.

![RGB-Bitcoin](assets/fr/012.webp)

I praksis fungerer denne modellen for Bitcoin som et basislag (lag 1), men den kan bli utilstrekkelig for mer komplekse bruksområder som samtidig krever høy transaksjonsgjennomstrømning og en viss grad av konfidensialitet.

Validering på klientsiden er basert på den motsatte ideen: I stedet for å kreve at hele nettverket validerer og lagrer alle transaksjoner, validerer hver enkelt deltaker (klient) bare den delen av historikken som angår ham eller henne:


- Når en person mottar en eiendel (eller annen digital eiendom), trenger han eller hun bare å kjenne til og verifisere kjeden av operasjoner (tilstandsoverganger) som førte til eiendelen, og bevise dens legitimitet;
- Denne sekvensen av operasjoner, fra ***Genesis*** (den første utstedelsen) til den siste transaksjonen, utgjør en acyklisk rettet graf (DAG) eller shard, dvs. en brøkdel av den samlede historikken.

![RGB-Bitcoin](assets/fr/013.webp)

Samtidig er validering på klientsiden avhengig av begrepet ***commitment***, slik at resten av nettverket (eller mer presist, det underliggende laget, for eksempel Bitcoin) kan låse inn den endelige tilstanden uten å se detaljene i disse dataene.

En *commitment* er en kryptografisk forpliktelse, vanligvis en _hash_ (for eksempel SHA-256) som settes inn i en Bitcoin-transaksjon, som beviser at private data er inkludert, uten å avsløre disse dataene.

Takket være disse _forpliktelsene_ kan vi bevise:


- Eksistensen av informasjon (siden den er lagret i en hash) ;
- Anterioriteten til denne informasjonen (fordi den er forankret og tidsstemplet i blokkjeden, med en dato og blokkrekkefølge).

Det nøyaktige innholdet avsløres imidlertid ikke, slik at det forblir konfidensielt.

Slik fungerer en RGB-tilstandsovergang helt konkret:


- Du forbereder en ny tilstandsovergang (f.eks. overføring av en RGB-token);
- Du genererer en kryptografisk forpliktelse til denne overgangen og setter den inn i en Bitcoin-transaksjon (disse forpliktelsene kalles "*anchors*" i RGB-protokollen);
- Motparten (mottakeren) henter historikken på kundesiden som er knyttet til denne eiendelen, og validerer end-to-end-konsistens, fra smartkontraktens tilblivelse til overgangen du overfører til den.

![RGB-Bitcoin](assets/fr/014.webp)

Validering på klientsiden gir to store fordeler:


- Skalerbarhet:**

Forpliktelsene (*commitments*) som inngår i blokkjeden, er små (i størrelsesorden noen titalls byte). Dette sikrer at blokkplassen ikke blir mettet, ettersom det bare er hashen som trenger å inkluderes. Det gjør det også mulig å utvikle protokollen utenfor kjeden, ettersom hver bruker bare trenger å lagre sitt eget historiefragment (sin _stash_).


- Personvern :**

Transaksjonene i seg selv (dvs. deres detaljerte innhold) publiseres ikke i kjeden. Det er bare fingeravtrykkene deres (*hash*) som er det. Dermed forblir beløp, adresser og kontraktslogikk private, og mottakeren kan lokalt verifisere gyldigheten av sin shard ved å inspisere alle tidligere transaksjoner. Det er ingen grunn til at mottakeren skal offentliggjøre disse dataene, bortsett fra i tilfelle en tvist eller dersom det kreves bevis.

I et system som RGB kan flere tilstandsoverganger fra ulike kontrakter (eller ulike aktiva) aggregeres til én enkelt Bitcoin-transaksjon via en enkelt _commitment_. Denne mekanismen etablerer en deterministisk, tidsstemplet kobling mellom transaksjonen i kjeden og dataene utenfor kjeden (de validerte overgangene på klientsiden), og gjør det mulig å registrere flere shards samtidig i ett enkelt ankerpunkt, noe som reduserer kostnadene og fotavtrykket i kjeden ytterligere.

Når denne Bitcoin-transaksjonen valideres, "låses" tilstanden til de underliggende kontraktene permanent, siden det blir umulig å endre hashen som allerede er innskrevet i blokkjeden.

![RGB-Bitcoin](assets/fr/015.webp)

### Stash-konseptet

En **stash** er et sett med data på klientsiden som en deltaker absolutt må beholde for å opprettholde integriteten og historikken til en RGB-smartkontrakt. I motsetning til en Lightning-kanal, der visse tilstander kan rekonstrueres lokalt fra delt informasjon, blir ikke RGB-kontraktens stash replikert andre steder: Hvis du mister den, vil ingen kunne gjenopprette den til deg, ettersom du er ansvarlig for din del av historikken. Derfor er det viktig å ta i bruk et system med pålitelige sikkerhetskopieringsprosedyrer i RGB.

![RGB-Bitcoin](assets/fr/016.webp)

### Single-use Seal: opprinnelse og drift

Når man aksepterer en eiendel, for eksempel en valuta, er to garantier avgjørende:


- Autentisiteten til den mottatte varen;
- Det unike med den mottatte varen, for å unngå dobbeltutgifter.

For fysiske eiendeler, som en pengeseddel, er fysisk tilstedeværelse nok til å bevise at den ikke har blitt duplisert. I den digitale verdenen, der eiendelene er rent informasjonsbaserte, er denne verifiseringen imidlertid mer kompleks, ettersom informasjon lett kan mangfoldiggjøres og dupliseres.

Som vi så tidligere, kan vi sikre ektheten til et RGB-token ved at avsenderen avslører historikken over tilstandsoverganger. Ved å ha tilgang til alle transaksjoner siden den første transaksjonen, kan vi bekrefte tokenets autentisitet. Dette prinsippet ligner på Bitcoin, der myntenes historikk kan spores tilbake til den opprinnelige Coinbase-transaksjonen for å verifisere gyldigheten. Men i motsetning til Bitcoin er denne historikken over tilstandsoverganger i RGB privat og oppbevares på klientsiden.

For å forhindre dobbeltbruk av RGB-tokens bruker vi en mekanisme som kalles "**Single-use Seal**". Dette systemet sikrer at hver token ikke kan brukes en gang til.

Single-use Seals er kryptografiske primitiver, foreslått i 2016 av Peter Todd, som er beslektet med fysiske segl: Når et segl har blitt plassert på en beholder, er det umulig å åpne eller endre den uten å bryte seglet på en irreversibel måte.

![RGB-Bitcoin](assets/fr/018.webp)

Denne tilnærmingen, overført til den digitale verden, gjør det mulig å bevise at en sekvens av hendelser faktisk har funnet sted, og at den ikke lenger kan endres i ettertid. Single-use Seals går dermed lenger enn den enkle logikken med `hash + tidsstempel`, og legger til begrepet om et segl som kan lukkes **bare én gang**.

![RGB-Bitcoin](assets/fr/017.webp)

For at Single-use Seals skal fungere, trenger du et medium som kan bevise eksistensen eller fraværet av en publikasjon, og som er vanskelig (om ikke umulig) å forfalske når informasjonen først har blitt spredt. En **blokkjede** (som Bitcoin) kan fylle denne rollen, og det samme kan for eksempel en papiravis med offentlig opplag. Ideen er som følger:


- Vi ønsker å bevise at en viss forpliktelse på en melding `h(m)` er blitt publisert til et publikum uten å avsløre innholdet i meldingen `m` ;
- Vi ønsker å bevise at ingen annen konkurrerende `h(m')` -forpliktelse har blitt publisert i stedet for `h(m)` ;
- Vi ønsker også å kunne kontrollere at meldingen `m` eksisterer før en bestemt dato.

En blokkjede egner seg ideelt til denne rollen: Så snart en transaksjon er inkludert i en blokk, har hele nettverket det samme ufalsifiserbare beviset på dens eksistens og innhold (i hvert fall delvis, siden _forpliktelsen_ kan skjule detaljene samtidig som den beviser meldingens ekthet).

Et single-use seal kan derfor ses på som et formelt løfte om å publisere en melding (som fremdeles er ukjent på dette stadiet) én og bare én gang, på en måte som kan verifiseres av alle interesserte parter.

I motsetning til enkle _commitments_ (hash) eller tidsstempler, som vitner om en eksistensdato, gir et single-use-segl en ekstra garanti for at **ingen alternativ forpliktelse** kan eksistere samtidig: Du kan ikke lukke det samme seglet to ganger, eller forsøke å erstatte den forseglede meldingen.

Følgende sammenligning hjelper deg med å forstå dette prinsippet:


- Kryptografisk forpliktelse (hash)**: Med en hash-funksjon kan du forplikte deg til et stykke data (et tall) ved å publisere dets hash. Dataene forblir hemmelige inntil du avslører forhåndsbildet, men du kan bevise at du kjente til dem på forhånd;
- Tidsstempel (blokkjede)**: Ved å sette inn denne hashen i blokkjeden beviser vi også at vi kjente til den på et bestemt tidspunkt (da den ble inkludert i en blokk);
- Engangsforsegling**: Med engangsplomber går vi et skritt videre ved å gjøre forpliktelsen unik. Med en enkelt hash kan du opprette flere motstridende forpliktelser parallelt (problemet med legen som kunngjør "*Det er en gutt*" til familien og "*Det er en jente*" i sin personlige dagbok). Single-use Seal eliminerer denne muligheten ved å koble forpliktelsen til et bevis på publisering, for eksempel Bitcoin-blokkjeden, slik at et forbruk av UTXO definitivt forsegler forpliktelsen. Når UTXO er brukt, kan de samme UTXO ikke brukes på nytt for å erstatte forpliktelsen.

| Engangsforseglinger | Tidsstempler | Enkel forpliktelse (digest/hash) | Engangsforseglinger | Tidsstempler

| -------------------------------------------------------------------------------- | ------------------------------- | ---------- | ---------------- |

offentliggjøring av forpliktelsen avslører ikke budskapet | Ja | Ja | Ja | Ja | Ja

bevis på dato for forpliktelse / eksistens av melding før en bestemt dato | Umulig | Mulig | Mulig | Mulig | Mulig

| Bevis for at det ikke finnes noen annen alternativ forpliktelse Umulig | Mulig |

Single-use Seals fungerer i tre hovedfaser:

**Seal Definition :**


- Alice definerer på forhånd reglene for publisering av seglet (når, hvor og hvordan meldingen skal publiseres);
- Bob aksepterer eller anerkjenner disse vilkårene.

![RGB-Bitcoin](assets/fr/021.webp)

**Seal Closing :**


- Ved kjøretid lukker Alice seglet ved å publisere den faktiske meldingen (vanligvis i form av en _commitment_, f.eks. en hash);
- Det gir også et **vitne** (kryptografisk bevis) som viser at forseglingen er lukket og ugjenkallelig.

![RGB-Bitcoin](assets/fr/019.webp)

**Seal Verification :**


- Når forseglingen er lukket, kan Bob ikke lenger åpne den: Han kan bare kontrollere at den er lukket;
- Bob samler inn seglet, **vitnet** og meldingen (eller forpliktelsen hans) for å sikre at alt stemmer overens, og at det ikke finnes konkurrerende segl eller ulike versjoner.

Prosessen kan oppsummeres som følger:

```txt
# Défini par Alice, validé ou accepté par Bob
seal <- Define()
# Fermeture du sceau par Alice avec le message
witness <- Close(seal, message)
# Vérification par Bob
bool <- Verify(seal, witness, message)
```

Validering på klientsiden går imidlertid ett skritt videre: Hvis selve definisjonen av et segl forblir utenfor blokkjeden, er det (i teorien) mulig for noen å bestride eksistensen eller legitimiteten til det aktuelle seglet. For å løse dette problemet brukes en kjede av sammenlåsende engangsforseglinger:


- Hvert lukket segl inneholder definisjonen av det følgende seglet;
- Vi registrerer disse avslutningene (med deres _commitments_) i blokkjeden (i en Bitcoin-transaksjon);
- Ethvert forsøk på å endre et tidligere segl vil dermed være i strid med historien som er innebygd i Bitcoin.

Det er nettopp dette RGB-systemet gjør:


- Publiserte meldinger er _forpliktelser_ til validerte data på klientsiden;
- Forseglingsdefinisjonen er knyttet til en Bitcoin UTXO ;
- Forseglingen lukkes når denne UTXO-en er brukt opp eller når en ny utgang krediteres den samme forpliktelsen;
- Transaksjonskjeden som bruker disse UTXO-ene, tilsvarer beviset på publisering: hver overgang eller endring av tilstand på RGB er dermed forankret i Bitcoin.

For å oppsummere:


- Forseglingsdefinisjonen_ er UTXO-en du har tenkt å forsegle en fremtidig forpliktelse med;
- _seal closing_ skjer når du bruker denne UTXO-en og oppretter en transaksjon som inneholder forpliktelsen;
- _vitnet_ er selve transaksjonen, som beviser at du har lukket seglet med dette innholdet;
- Du kan ikke bevise at et segl ikke har blitt lukket (du kan ikke være helt sikker på at en UTXO ikke allerede har blitt brukt eller ikke vil bli brukt i en blokk du ikke har sett ennå), men du kan bevise at det faktisk har blitt lukket.

Denne unikheten er viktig for validering på klientsiden: Når du validerer en tilstandsovergang, kontrollerer du at den tilsvarer en unik UTXO, som ikke tidligere er brukt i en konkurrerende forpliktelse. Det er dette som garanterer at det ikke forekommer dobbeltbruk i smartkontrakter utenfor kjeden.

### Flere forpliktelser og røtter

En RGB-smartkontrakt kan ha behov for å bruke flere Single-use Seals (flere UTXO-er) samtidig. I tillegg kan en enkelt Bitcoin-transaksjon referere til flere forskjellige kontrakter, som hver forsegler sin egen tilstandsovergang. Dette krever en **multi-commitment**-mekanisme for å bevise, deterministisk og entydig, at ingen av forpliktelsene eksisterer i duplikat. Det er her begrepet **anchor** kommer inn i bildet i RGB: en spesiell struktur som kobler en Bitcoin-transaksjon og en eller flere forpliktelser på klientsiden (tilstandsoverganger), som hver potensielt tilhører en annen kontrakt. Vi skal se nærmere på dette konseptet i neste kapittel.

![RGB-Bitcoin](assets/fr/023.webp)

To av prosjektets viktigste GitHub-arkiver (under LNPBP-organisasjonen) samler de grunnleggende implementeringene av disse konseptene som ble studert i det første kapittelet:


- klient_side_validering** : Inneholder Rust-primitiver for lokal validering ;
- single_use_seals**: Implementerer logikken for å definere og lukke disse forseglingene på en sikker måte.

![RGB-Bitcoin](assets/fr/020.webp)

Merk at disse programvarebrikkene er Bitcoin-agnostiske; i teorien kan de brukes på et hvilket som helst annet medium for bevis for publisering (et annet register, en journal osv.). I praksis er RGB avhengig av Bitcoin for sin robusthet og brede konsensus.

![RGB-Bitcoin](assets/fr/021.webp)

### Spørsmål fra publikum

#### Mot mer utbredt bruk av engangsplomber

Peter Todd skapte også _Open Timestamps_-protokollen, og Single-use Seal-konseptet er en naturlig forlengelse av disse ideene. Utover RGB kan man se for seg andre bruksområder, for eksempel konstruksjon av _sidekjeder_ uten å ty til _merge mining_ eller drivechain-relaterte forslag som BIP300. Alle systemer som krever en enkelt forpliktelse, kan i prinsippet utnytte denne kryptografiske primitiven. I dag er RGB den første store fullskala-implementeringen.

#### Problemer med datatilgjengelighet

Siden hver bruker lagrer sin egen del av historikken ved validering på klientsiden, er det ikke garantert at dataene er tilgjengelige globalt. Hvis en kontraktsutsteder holder tilbake eller tilbakekaller visse opplysninger, kan du være uvitende om den faktiske utviklingen av tilbudet. I noen tilfeller (for eksempel stablecoins) forventes det at utstederen opprettholder offentlige data for å bevise volumet i omløp, men det er ingen teknisk forpliktelse til å gjøre det. Det er derfor mulig å utforme bevisst ugjennomsiktige kontrakter med ubegrenset tilbud, noe som reiser spørsmål om tillit.

#### Deling og kontraktsisolering

Hver kontrakt representerer en isolert _shard_: USDT og USDC trenger for eksempel ikke å dele historikken sin. Atombytter er fortsatt mulig, men dette innebærer ikke sammenslåing av registrene deres. Alt gjøres ved hjelp av kryptografisk forpliktelse, uten å avsløre hele historikkgrafen til hver deltaker.

### Konklusjon

Vi har sett hvor konseptet med validering på klientsiden passer inn i blockchain og _statskanaler_, hvordan det reagerer på distribuerte databehandlingstrilemmaer, og hvordan det utnytter Bitcoin blockchain unikt for å unngå dobbeltbruk og for * tidsstempling*. Ideen er basert på begrepet **Single-use Seal**, som gjør det mulig å opprette unike forpliktelser som du ikke kan bruke på nytt etter eget ønske. På denne måten laster hver deltaker bare opp den historikken som er strengt nødvendig, noe som øker skalerbarheten og konfidensialiteten til smartkontrakter, samtidig som sikkerheten til Bitcoin beholdes som et bakteppe.

Det neste trinnet vil være å forklare mer detaljert hvordan denne Single-use Seal-mekanismen brukes i Bitcoin (via UTXO-er), hvordan ankere opprettes og valideres, og deretter hvordan komplette smartkontrakter bygges i RGB. Vi vil spesielt se på spørsmålet om flere forpliktelser, den tekniske utfordringen med å bevise at en Bitcoin-transaksjon samtidig forsegler flere tilstandsoverganger i forskjellige kontrakter, uten å introdusere sårbarheter eller doble forpliktelser.

Før du dykker inn i de mer tekniske detaljene i det andre kapittelet, kan du gjerne lese nøkkeldefinisjonene på nytt (validering på klientsiden, Single-use Seal, ankere osv.) og huske på den overordnede logikken: Vi ønsker å forene styrkene til Bitcoin-blokkjeden (sikkerhet, desentralisering, tidsstempling) med styrkene til off-chain-løsninger (hastighet, konfidensialitet, skalerbarhet), og det er nettopp dette RGB og validering på klientsiden prøver å oppnå.

## Forpliktelseslaget

<chapterId>cc2fe85a-9cc7-5b8c-a00a-c0a867241061</chapterId>

![video](https://youtu.be/FS6PDprWl5Q)

I dette kapittelet skal vi se på implementeringen av validering på klientsiden og engangsforseglinger i Bitcoin-blokkjeden. Vi presenterer hovedprinsippene for RGBs **commitment-lag** (lag 1), med særlig fokus på **TxO2**-ordningen, som RGB bruker for å definere og lukke et segl i en Bitcoin-transaksjon. Deretter vil vi diskutere to viktige punkter som ennå ikke har blitt dekket i detalj:


- De _deterministiske Bitcoin-forpliktelsene_;
- Forpliktelser med flere protokoller.

Det er kombinasjonen av disse konseptene som gjør det mulig for oss å legge flere systemer eller kontrakter oppå én UTXO og dermed én blokkjede.

Det er viktig å huske at de kryptografiske operasjonene som er beskrevet, i absolutte termer kan brukes på andre blokkjeder eller publiseringsmedier, men Bitcoins egenskaper (i form av desentralisering, motstand mot sensur og åpenhet for alle) gjør det til det ideelle grunnlaget for å utvikle avansert programmerbarhet som den som kreves av **RGB**.

### Forpliktelsesordninger i Bitcoin og RGBs bruk av dem

Som vi så i kursets første kapittel, er Single-use Seals et generelt konsept: Vi lover å inkludere en forpliktelse (_commitment_) på et bestemt sted i en transaksjon, og dette stedet fungerer som et segl som vi lukker på en melding. På Bitcoin-blokkjeden er det imidlertid flere alternativer for å velge hvor denne _forpliktelsen_ skal plasseres.

For å forstå logikken, la oss huske det grunnleggende prinsippet: For å lukke en _single-use seal_, bruker vi det forseglede området ved å sette inn _commitment_ på en gitt melding. I Bitcoin kan dette gjøres på flere måter:


- Bruk en offentlig nøkkel eller adresse**

Vi kan bestemme at en bestemt offentlig nøkkel eller adresse er _single-use seal_. Så snart denne nøkkelen eller adressen dukker opp i kjeden i en transaksjon, betyr det at forseglingen er lukket med en bestemt melding.


- Bruk en Bitcoin**-transaksjonsutgang

Dette betyr at en _engangsforsegling_ er definert som et nøyaktig _utgangspunkt_ (et TXID + utgangsnummerpar). Så snart dette _utgangspunktet_ er brukt opp, er forseglingen lukket.

Under arbeidet med RGB identifiserte vi minst fire ulike måter å implementere disse seglene på Bitcoin:


- Definer forseglingen via en offentlig nøkkel, og lukk den i en _output_ ;
- Definer forseglingen med et _outpoint_ og lukk den med en _output_ ;
- Definer forseglingen via verdien av en offentlig nøkkel, og lukk den i en _input_ ;
- Definer forseglingen via et _outpoint_, og lukk den i et _input_.

| Forseglingsdefinisjon | Forseglingslukking | Ytterligere krav | Hovedapplikasjon | Mulige engasjementsordninger

| ------------- | ------------------------- | --------------------- | ----------------------------------------------------------------- | ---------------------------- | ------------------------------ |

p2(W)PKH | Ingen for øyeblikket | Keytweak, taptweak, opret | P2(W)PKH | Ingen for øyeblikket

| TxO2 | Transaksjonsutgang | Transaksjonsutgang | Krever deterministiske forpliktelser på Bitcoin | RGBv1 (universal) | Keytweak, tapret, opret |

| PkI | Offentlig nøkkelverdi | Transaksjonsoppføring | Kun Taproot og ikke kompatibel med eldre lommebøker | Bitcoin-baserte identiteter | Sigtweak, witweak

| TxO1 | Transaksjonsutgang | Transaksjonsinngang | Kun Taproot og ikke kompatibel med eldre lommebøker | Ingen for øyeblikket | Sigtweak, witweak |

Vi skal ikke gå i detalj om hver av disse konfigurasjonene, ettersom vi i RGB har valgt å bruke **et _utpunkt_ som definisjon av forseglingen**, og å plassere _commitment_ i utgangen av transaksjonen som bruker dette _utpunktet_. Vi kan derfor introdusere følgende begreper for fortsettelsen:


- "Seal-definisjon"** : Et gitt _utgangspunkt_ (identifisert av TXID + utgangsnr.) ;
- "Seal closing"**: Transaksjonen som bruker dette _outpoint_, der en _commitment_ legges til en melding.

Dette skjemaet er valgt fordi det er kompatibelt med RGB-arkitektur, men andre konfigurasjoner kan være nyttige for ulike bruksområder.

"O2" i "TxO2" minner oss om at både definisjon og avslutning er basert på bruk (eller opprettelse) av en transaksjonsutgang.

### Eksempel på TxO2-diagram

Som en påminnelse: Å definere et _engangsforsegling_ krever ikke nødvendigvis publisering av en transaksjon i kjeden. Det holder for eksempel at Alice allerede har en ubrukt UTXO. Hun kan bestemme seg: "Dette _utgangspunktet_ (som allerede eksisterer) er nå mitt segl". Hun noterer dette lokalt (_klientsiden_), og inntil denne UTXO-en er brukt, anses forseglingen som åpen.

![RGB-Bitcoin](assets/fr/024.webp)

Den dagen den ønsker å lukke seglet (for å signalisere en hendelse, eller for å forankre en bestemt melding), bruker den denne UTXO-en i en ny transaksjon (denne transaksjonen kalles ofte "_vitnetransaksjonen_" (ikke relatert til _segwit_, det er bare den betegnelsen vi gir den). Denne nye transaksjonen vil inneholde _commitment_ til meldingen.

![RGB-Bitcoin](assets/fr/025.webp)

Merk at i dette eksemplet :


- Ingen andre enn Bob (eller de personene som Alice velger å avsløre det fullstendige beviset for) vil vite at en bestemt melding er skjult i denne transaksjonen;
- Alle kan se at _outpoint_ er brukt, men det er bare Bob som har beviset på at meldingen faktisk er forankret i transaksjonen.

For å illustrere dette TxO2-opplegget kan vi bruke et _single-use seal_ som en mekanisme for å tilbakekalle en PGP-nøkkel. I stedet for å publisere et tilbakekallingssertifikat på servere, kan Alice si: "Denne Bitcoin-utgangen, hvis den blir brukt, betyr at PGP-nøkkelen min er tilbakekalt".

Alice har derfor en spesifikk UTXO, som en bestemt tilstand eller data (som bare hun kjenner til) er knyttet til lokalt (på klientsiden).

Alice informerer Bob om at hvis denne UTXO-en blir brukt, vil en bestemt hendelse anses å ha inntruffet. Fra utsiden ser vi bare en Bitcoin-transaksjon, men Bob vet at denne utgiften har en skjult mening.

![RGB-Bitcoin](assets/fr/026.webp)

Når Alice bruker denne UTXO-en, lukker hun seglet på en melding som indikerer hennes nye nøkkel, eller rett og slett tilbakekallingen av den gamle. På denne måten vil alle som overvåker kjeden se at UTXO-en er brukt, men bare de som har det fulle beviset, vil vite at det nettopp er tilbakekallingen av PGP-nøkkelen.

![RGB-Bitcoin](assets/fr/027.webp)

For at Bob eller andre involverte skal kunne sjekke den skjulte meldingen, må Alice gi ham informasjon utenfor kjeden.

![RGB-Bitcoin](assets/fr/028.webp)

Alice må derfor gi Bob :


- Selve meldingen (for eksempel den nye PGP-nøkkelen) ;
- Kryptografisk bevis på at meldingen var involvert i transaksjonen (kjent som _extra transaction proof_ eller _anchor_).

![RGB-Bitcoin](assets/fr/029.webp)

Tredjeparter har ikke denne informasjonen. De ser bare at en UTXO har blitt brukt. Konfidensialiteten er derfor sikret.

La oss oppsummere prosessen i to transaksjoner for å tydeliggjøre strukturen:


- Transaksjon 1**: Denne inneholder _forseglingsdefinisjonen_, dvs. det _utgangspunktet_ som skal fungere som forsegling.

![RGB-Bitcoin](assets/fr/031.webp)


- Transaksjon 2**: Bruker dette _outpoint_. Dette lukker forseglingen og setter inn _commitment_ på meldingen i samme transaksjon.

![RGB-Bitcoin](assets/fr/033.webp)

Vi kaller derfor den andre transaksjonen for "_vitnetransaksjonen_".

For å illustrere dette fra en annen vinkel, kan vi representere to lag:


- Det øverste laget (blokkjeden, offentlig)**: Alle ser transaksjonen og vet at et _outpoint_ har blitt brukt;
- Det nedre laget (klientsiden, privat)**: Bare Alice (eller personen det gjelder) vet at denne utgiften tilsvarer den og den meldingen, via det kryptografiske beviset og meldingen hun oppbevarer lokalt.

![RGB-Bitcoin](assets/fr/034.webp)

Men når seglet skal lukkes, oppstår spørsmålet om hvor _forpliktelsen_ skal settes inn

I forrige avsnitt nevnte vi kort hvordan valideringsmodellen på klientsiden kan brukes på RGB og andre systemer. Her tar vi for oss **deterministiske Bitcoin-forpliktelser** og hvordan de kan integreres i en transaksjon. Tanken er å forstå hvorfor vi prøver å sette inn en enkelt forpliktelse i _vitnetransaksjonen_, og fremfor alt hvordan vi kan sikre at det ikke kan være andre uoppdagede konkurrerende forpliktelser.

### Forpliktelsessteder i en transaksjon

Når du gir noen bevis på at en bestemt melding er innebygd i en transaksjon, må du kunne garantere at det ikke finnes en annen form for forpliktelse (en annen, skjult melding) i den samme transaksjonen som ikke har blitt avslørt for deg. For at validering på klientsiden skal forbli robust, trenger du en **deterministisk** mekanisme for å plassere en enkelt _commitment_ i transaksjonen som lukker _single-use seal_.

I _vitnetransaksjonen_ brukes den berømte UTXO (eller _forseglingsdefinisjonen_), og denne utgiften tilsvarer lukkingen av forseglingen. Teknisk sett vet vi at hvert outpoint bare kan brukes én gang. Det er nettopp dette som underbygger Bitcoins motstand mot dobbeltbruk. Men utgiftstransaksjonen kan ha flere _innganger_, flere _utganger_ eller være sammensatt på en kompleks måte (coinjoins, Lightning-kanaler osv.). Vi må derfor definere tydelig hvor vi skal sette inn _commitment_ i denne strukturen, entydig og enhetlig.

Uansett metode (PkO, TxO2 osv.) kan _forpliktelsen_ settes inn :


- I en Input** via :
    - Sigtweak** (modifiserer `r`-komponenten i ECDSA-signaturen, i likhet med "Sign-to-contract"-prinsippet) ;
    - Witweak** (transaksjonens _segregerte vitne_-data er endret).
- I en Output** via :
    - Keytweak** (mottakerens offentlige nøkkel "tweakes" med meldingen) ;
    - Opret** (meldingen plasseres i en ikke-forbrukbar utgang `OP_RETURN`) ;
    - Tapret** (eller _Taptweak_), som baserer seg på taproot for å sette inn forpliktelser i skriptdelen av en taproot-nøkkel, og dermed endre den offentlige nøkkelen på en deterministisk måte.

![RGB-Bitcoin](assets/fr/035.webp)

Her er detaljene for hver metode:

![RGB-Bitcoin](assets/fr/038.webp)

***Sig tweak (sign-to-contract) :***

En tidligere metode gikk ut på å utnytte den tilfeldige delen av en signatur (ECDSA eller Schnorr) til å legge inn _forpliktelsen_: Dette er teknikken som kalles "**Sign-to-contract**". Du erstatter den tilfeldig genererte noncen med en hash som inneholder dataene. På denne måten avslører signaturen implisitt forpliktelsen din, uten at det tar ekstra plass i transaksjonen. Denne tilnærmingen har en rekke fordeler:


- Ingen overbelastning i kjeden (du bruker samme sted som den grunnleggende noncen);
- I teorien kan dette være ganske diskret, ettersom noncen i utgangspunktet er et tilfeldig datum.

Det har imidlertid dukket opp to store ulemper:


- Multisig før Taproot: Når du har flere signatarer, må du bestemme hvilken signatur som skal bære _forpliktelsen_. Signaturene kan ha ulik rekkefølge, og hvis en signatar nekter, mister du kontrollen over utfallet av _commitment_;
- MuSig og delt nonce: Med Schnorr multisig (*MuSig*) er nonce-generering en flerpartsalgoritme, og det blir praktisk talt umulig å justere noncen individuelt.

I praksis er **sig tweak ** heller ikke veldig kompatibel med eksisterende maskinvare (maskinvare lommebøker) og formater (Lightning, etc.). Så denne gode ideen er vanskelig å sette ut i praksis.

***Nøkkeljustering (betal-til-kontrakt): ***

**Nøkkeltilpasningen** tar opp det historiske konseptet _pay-to-contract_. Vi tar den offentlige nøkkelen `X` og justerer den ved å legge til verdien `H(melding)`. Hvis `X = x * G` og `h = H(melding)`, blir den nye nøkkelen `X' = X + h * G`. Denne endrede nøkkelen skjuler forpliktelsen til `meldingen`. Innehaveren av den opprinnelige private nøkkelen kan, ved å legge `h` til sin private nøkkel `x`, bevise at han har nøkkelen til å bruke utdataene. I teorien er dette elegant, fordi :


- _commitment_ legges inn uten å legge til flere felt;
- Du lagrer ikke ytterligere data i kjeden.

I praksis støter vi imidlertid på følgende problemer:


- Lommebøker gjenkjenner ikke lenger den offentlige standardnøkkelen, siden den har blitt "justert", slik at de ikke enkelt kan knytte UTXO til den vanlige nøkkelen din;
- Maskinvare-lommebøker er ikke utformet for å signere med en nøkkel som ikke er avledet fra deres standardavledning;
- Du må tilpasse skriptene, beskrivelsene osv.

I RGB-sammenheng var denne veien planlagt frem til 2021, men det viste seg å være for komplisert å få det til å fungere med dagens standarder og infrastruktur.

***Vitnejustering :***

En annen idé, som visse protokoller som _inscriptions Ordinals_ har satt ut i livet, er å plassere dataene direkte i `vitne`-delen av transaksjonen (derav uttrykket "witness tweak"). Denne metoden :


- Gjør engasjementet umiddelbart synlig (du limer bokstavelig talt inn rådata i vitnet);
- Kan være gjenstand for sensur (utvinnere eller noder kan nekte å videresende hvis den er for stor eller har andre vilkårlige egenskaper);
- Opptar plass i blokkene, stikk i strid med RGBs mål om diskresjon og letthet.

I tillegg er vitne designet for å kunne beskjæres i visse sammenhenger, noe som kan gjøre det mer komplisert å ha robuste bevis.

***Open-return (opret) :***

En `OP_RETURN` er veldig enkel i sin virkemåte, og lar deg lagre en hash eller en melding i et spesielt felt i transaksjonen. Men det er umiddelbart synlig: alle ser at det er en _commitment_ i transaksjonen, og den kan sensureres eller forkastes, i tillegg til å legge til ekstra output. Siden dette øker gjennomsiktigheten og størrelsen, anses det som mindre tilfredsstillende med tanke på en løsning for validering på klientsiden.

```txt
34-byte_Opret_Commitment =
OP_RETURN   OP_PUSHBYTE_32   <mpc::Commitment>
|_________| |______________| |_________________|
1-byte       1-byte         32 bytes
```

### Tapret

Det siste alternativet er bruk av **Taproot** (introdusert med BIP341) med *Tapret*-ordningen. *Tapret* er en mer kompleks form for deterministisk forpliktelse, som gir forbedringer når det gjelder fotavtrykk på blokkjeden og konfidensialitet for kontraktsoperasjoner. Hovedideen er å skjule forpliktelsen i `Script Path Spend`-delen av en [taproot-transaksjon] (https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki).

![RGB-Bitcoin](assets/fr/036.webp)

Før vi beskriver hvordan forpliktelsen settes inn i en taproot-transaksjon, skal vi se på den **nøyaktige formen** på forpliktelsen, som **imperativt** må tilsvare en 64-byte streng [konstruert](https://github.com/BP-WG/bp-core/blob/master/dbc/src/tapret/mod.rs#L179-L196) på følgende måte:

```txt
64-byte_Tapret_Commitment =
OP_RESERVED ...  ... .. OP_RESERVED   OP_RETURN   OP_PUSHBYTE_33  <mpc::Commitment>  <Nonce>
|___________________________________| |_________| |______________| |_______________|  |______|
OP_RESERVED x 29 times = 29 bytes      1 byte         1 byte          32 bytes        1 byte
|________________________________________________________________| |_________________________|
TAPRET_SCRIPT_COMMITMENT_PREFIX = 31 bytes                    MPC commitment + NONCE = 33 bytes
```


- De 29 byte `OP_RESERVED`, etterfulgt av `OP_RETURN`, og deretter `OP_PUSHBYTE_33`, utgjør den 31 byte store _prefiks_delen;
- Deretter kommer en 32-byte _commitment_ (vanligvis Merkle-roten fra **MPC**), som vi legger til 1 byte med **Nonce** (totalt 33 byte for denne andre delen).

Metoden `Tapret` på 64 byte ser altså ut som en `Opret` som vi har prefikset 29 byte med `OP_RESERVED` og lagt til en ekstra byte som en nonce.

For å opprettholde fleksibiliteten når det gjelder implementering, konfidensialitet og skalering, tar Tapret-ordningen hensyn til ulike brukstilfeller, avhengig av kravene:


- Unik innlemmelse av en Tapret-forpliktelse i en Taproot-transaksjon uten en allerede eksisterende Script Path-struktur;
- Integrering av en Tapret-forpliktelse i en Taproot-transaksjon som allerede er utstyrt med en Script Path.

La oss se nærmere på hvert av disse to scenariene.

#### Tapret-innlemmelse uten eksisterende Script Path

I dette første tilfellet tar vi utgangspunkt i en taproot-utgangsnøkkel (*Taproot Output Key*) `Q` som bare inneholder den interne offentlige nøkkelen `P` *(Internal Key*), uten noen tilknyttet skriptbane (*Script Path*) :

![RGB-Bitcoin](assets/fr/047.webp)


- p: den interne offentlige nøkkelen for _Key Path Spend_.
- `G`: det genererende punktet til den elliptiske kurven [secp256k1](https://en.bitcoin.it/wiki/Secp256k1).
- t = tH_TWEAK(P)` er tweak-faktoren, beregnet via en _tagged hash_ (f.eks. `SHA-256(SHA-256(TapTweak) || P)`), i henhold til [BIP86] (https://github.com/bitcoin/bips/blob/master/bip-0086.mediawiki#address-derivation). Dette beviser at det ikke finnes noe skjult skript.

For å inkludere en **Tapret**-forpliktelse må du legge til et **Script Path Spend** med et **unikt script**, på følgende måte:

![RGB-Bitcoin](assets/fr/048.webp)


- t = tH_TWEAK(P || Script_root)` blir da den nye justeringsfaktoren, inkludert **Script_root**.
- `Script_root = tH_BRANCH(64-byte_Tapret_Commitment)` representerer roten til dette **skriptet**, som ganske enkelt er en hash av typen `SHA-256(SHA-256(TapBranch) || 64-byte_Tapret_Commitment)`.

Beviset for inkludering og entydighet i taproot-treet koker her ned til den eneste interne offentlige nøkkelen `P`.

#### Tapret-integrering i en allerede eksisterende skriptbane

Det andre scenariet gjelder en mer kompleks `Q` taproot**-utgang, som allerede inneholder flere skript. Vi har for eksempel et tre med tre skript:

![RGB-Bitcoin](assets/fr/049.webp)


- tH_LEAF(x)` angir den normaliserte taggede hashfunksjonen til et bladskript.
- a, B, C` representerer skript som allerede er inkludert i taproot-strukturen.

For å legge til Tapret-forpliktelsen må vi sette inn et *ikke-forbrukbart skript* på første nivå i treet, og flytte de eksisterende skriptene ett nivå ned. Visuelt blir treet :

![RGB-Bitcoin](assets/fr/050.webp)


- tHABC` representerer den taggede hashen til toppnivågrupperingen `A, B, C`.
- tHT` representerer hashen til skriptet som tilsvarer `Tapret` på 64 byte.

I henhold til taproot-reglene må hver gren/blad kombineres i henhold til en leksikografisk hash-rekkefølge. Det finnes to mulige tilfeller:


- `tHT` > `tHABC`: Tapret-forpliktelsen flyttes til høyre i treet. Unikhetsbeviset trenger bare `tHABC` og `P` ;
- tHT` < `tHABC`**: Tapret-forpliktelsen er plassert til venstre. For å bevise at det ikke finnes noen annen Tapret-forpliktelse til høyre, må `tHAB` og `tHC` avsløres for å vise at det ikke finnes noen annen slik skrift.

Visuelt eksempel for det første tilfellet (`tHABC < tHT`):

![RGB-Bitcoin](assets/fr/051.webp)

Eksempel for det andre tilfellet (`tHABC > tHT`):

![RGB-Bitcoin](assets/fr/052.webp)

#### Optimalisering med nonce

For å forbedre konfidensialiteten kan vi "mine" (et mer nøyaktig begrep ville vært "bruteforcing") verdien av `<Nonce>` (den siste byten av 64-byte `Tapret`) i et forsøk på å oppnå en hash `tHT` slik at `tHABC < tHT`. I dette tilfellet er forpliktelsen plassert til høyre, slik at brukeren slipper å avsløre hele innholdet i eksisterende skript for å bevise at Tapret er unikt.

Oppsummert tilbyr `Tapret` en diskret og deterministisk måte å innlemme en forpliktelse i en taproot-transaksjon, samtidig som kravet om unikhet og entydighet, som er avgjørende for RGBs validering på klientsiden og logikk for single-use seal, blir respektert.

#### Gyldige utganger

For RGB-forpliktelsestransaksjoner er hovedkravet for et gyldig Bitcoin-forpliktelsesskjema som følger: Transaksjonen (*vitnetransaksjon*) må beviselig inneholde en enkelt forpliktelse. Dette kravet gjør det umulig å konstruere en alternativ historikk for validerte data på klientsiden innenfor samme transaksjon. Dette betyr at meldingen som _single-use seal_ lukkes rundt, er unik.

For å oppfylle dette prinsippet, og uavhengig av antall utganger i en transaksjon, krever vi at **en og bare én utgang** kan inneholde en forpliktelse (*commitment*). For hver av de anvendte ordningene (*Opret* eller *Tapret*) er de eneste gyldige utgangene som kan inneholde en RGB _commitment_ :


- Den første utdataen `OP_RETURN` (hvis den finnes) for *Opret*-ordningen;
- Den første taproot-utdataen (hvis den finnes) for *Tapret*-ordningen.

Merk at det er fullt mulig for en transaksjon å inneholde en enkelt `Opret`-forpliktelse og en enkelt `Tapret`-forpliktelse i to separate utganger. Takket være Seal Definitions deterministiske natur tilsvarer disse to forpliktelsene to forskjellige datastykker som er validert på klientsiden.

### Analyse og praktiske valg i RGB

Da vi startet RGB, gikk vi gjennom alle disse metodene for å finne ut hvor og hvordan vi skulle plassere en _commitment_ i en transaksjon på en deterministisk måte. Vi definerte noen kriterier:


- Kompatibilitet med ulike scenarier (f.eks. multisig, Lightning, maskinvarelommebøker osv.);
- Innvirkning på plass i kjeden ;
- Vanskelig implementering og vedlikehold ;
- Konfidensialitet og motstand mot sensur.

| Trace- og on-chain-dimensjonering | Dimensjonering på klientsiden | Porteføljeintegrasjon | Maskinvarekompatibilitet | Lightning-kompatibilitet | Taproot-kompatibilitet

| --------------------------------------------------- | ------------------------ | ------------------ | ----------------------------- | ------------------------ | ----------------------- | --------------------- |

| Keytweak (deterministisk P2C) | 🟢 | 🟡 | 🔴 | 🟠 | 🔴 BOLT, 🔴 Bifrost | 🟠 Taproot, 🟢 MuSig | 🔴 🟢 Taproot, 🟢 MuSig

| Sigtweak (deterministisk S2C) | 🟢 | 🟢 | 🟠 | 🔴 | 🔴 BOLT, 🔴 Bifrost | 🟠 Taproot, 🔴 MuSig |

| Opret (OP_RETURN) | 🔴 | 🟢 | 🟢 | 🟢 | 🟠 | 🔴 BOLT, 🟠 Bifrost | - | |

tapret-algoritme: øverste venstre node | 🟠 | 🔴 | 🟠 | 🟢 | 🔴 BOLT, 🟢 Bifrost | 🟢 Taproot, 🟢 MuSig | 🟢 Bifrost | 🟢 Taproot, 🟢 MuSig

tapret-algoritme #4: hvilken som helst node + bevis | 🟢 | 🟢 | 🟠 | 🟢 | 🔴 BOLT, 🟢 Bifrost | 🟢 Taproot, 🟢 MuSig | 🔴 BOLT, 🟢 Bifrost | 🟢 Taproot, 🟢 MuSig

| Deterministisk forpliktelsesordning | Standard | Kostnad i kjeden | Størrelse på bevis på kundesiden | Standard

| ------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |

| Nøkkelvekking (deterministisk P2C) | LNPBP-1, 2 | 0 byte | 33 byte (uvektet nøkkel) |

sigtweak (deterministisk S2C) | WIP (LNPBP-39) | 0 byte | 0 byte | 0 byte | Sigtweak (deterministisk S2C) | WIP (LNPBP-39)

| Opret (OP_RETURN) | - | 36 (v)bytes (TxOut additional) | 0 bytes | | 36 (v)bytes (TxOut additional) | 0 bytes |

| Tapret-algoritme: øverste venstre node | LNPBP-6 | 32 byte i vitne (8 vbytes) på en hvilken som helst n-av-m multisig og bruk per skriptsti | 0 byte på taproot-skript uten skript ~270 byte i et enkelt skripttilfelle, ~128 byte hvis mer enn ett skript |

| Tapret-algoritme nr. 4: hvilken som helst node + bevis på unikhet | LNPBP-6 | 32 byte i vitnet (8 vbytes) for enkeltskript-tilfeller, 0 byte i vitnet i de fleste andre tilfeller | 0 byte på taproot-skript uten skript, 65 byte til Taptree har et dusin skript |

| Lag | Kostnad på kjeden (byte/vbyte) | Kostnad på kjeden (byte/vbyte) | Kostnad på kjeden (byte/vbyte) | Kostnad på kjeden (byte/vbyte) | Kostnad på kjeden (byte/vbyte) | Kostnad på klientsiden (byte) | Kostnad på klientsiden (byte) | Kostnad på klientsiden (byte) | Kostnad på klientsiden (byte) | Kostnad på klientsiden (byte) | Kostnad på klientsiden (byte) | Kostnad på klientsiden (byte) | Kostnad

| ------------------------------ | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ------------------------ | ------------------------ | ------------------------ | ------------------------ | ------------------------ |

| **Type** | **Tapret** | **Tapret #4** | **Keytweak** | **Sigtweak** | **Opret** | **Tapret** | **Tapret #4** | **Keytweak** | **Sigtweak** | **Opret** | **Tapret** | **Tapret #4** | **Keytweak** | **Sigtweak** | **Opret** |

| Single-sig | 0 | 0 | 0 | 0 | 0 | 32 | 0 | 0 | 0 | 32 | 0? | 0 | 0 |

| MuSig (n-av-n) | 0 | 0 | 0 | 0 | 32 | 0 | 0 | 0 | 32 | ? > 0 | 0 |

| Multi-sig 2-av-3 | 32/8 | 32/8 eller 0 | 0 n/a | 32 | ~270 | 65 | 32 | n/a | 0 |

| Multi-sig 3-av-5 | 32/8 | 32/8 eller 0 | 0 n/a | 32 | ~340 | 65 | 32 | n/a | 0 |

| Multi-sig 2-av-3 med tidsavbrudd | 32/8 | 0 | 0 n/a | 32 | 64 | 65 | 32 | n/a | 0 | 0

lag | Kostnad på kjeden (vbytes) | Kostnad på kjeden (vbytes) | Kostnad på kjeden (vbytes) | Kostnad på klientsiden (byte) | Kostnad på klientsiden (byte) | Kostnad på klientsiden (byte) | Kostnad på klientsiden (byte) | Kostnad på klientsiden (byte)

| -------------------------------- | ---------------------- | ---------------------- | ---------------------- | ------------------------ | ------------------------ |

| **Type** | **Base** | **Tapret #2** | **Tapret #4** | **Tapret #2** | **Tapret #4** | **Tapret #4** | **Tapret #2** | **Tapret #4** | **Tapret #4

| MuSig (n-av-n) | 16,5 | 0 | 0 | 0 | 0 | 0 | 0 | 0

| FROST (n-av-m) | ? | 0 | 0 | 0 | 0 |

| Multi_a (n-av-m) | 1+16n+8m | 8 | 8 | 33 * m | 65 | 8

| MuSig-gren / Multi_a (n-av-m) | 1+16n+8n+8xlog(n) | 8 | 0 | 64 | 65 |

| Med tidsavbrudd (n-av-m) | 1+16n+8n+8xlog(n) | 8 | 0 | 64 | 65 |

| Metode | Konfidensialitet og skalerbarhet | Interoperabilitet | Kompatibilitet | Portabilitet | Kompleksitet | Kompleksitet

| ----------------------------------------- | ------------------------------ | ---------------- | ------------- | ----------- | ---------- |

| Keytweak (deterministisk P2C) | 🟢 | 🔴 | 🔴 | 🟡 | 🟡 | 🟡 |

sigtweak (deterministisk S2C) | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 |

| Opret (OP_RETURN) | 🔴 | 🟠 | 🔴 | 🟢 | 🟢 | 🟢 |

| Algo Tapret: øverste venstre node | 🟠 | 🟢 | 🔴 | 🟠 | 🔴 | 🟠 |

| Algo Tapret #4: Enhver node + bevis | 🟢 | 🟢 | 🟢 | 🟠 | 🔴 | |

I løpet av studien ble det klart at ingen av forpliktelsesordningene var fullt ut kompatible med den nåværende Lightning-standarden (som ikke bruker Taproot, _muSig2_ eller ytterligere _commitment_-støtte). Det arbeides med å endre Lightnings kanalkonstruksjon (*BiFrost*) for å gjøre det mulig å legge inn RGB-forpliktelser. Dette er et annet område der vi må gjennomgå transaksjonsstrukturen, nøklene og måten kanaloppdateringer signeres på.

Analysen viste at andre metoder (key tweak, sig tweak, witness tweak osv.) faktisk ga andre former for komplikasjoner:


- Enten har vi et stort volum i kjeden;
- Enten er det en radikal inkompatibilitet med den eksisterende lommebokkoden;
- Enten er løsningen ikke levedyktig i ikke-samarbeidende multisig.

For RGB er det særlig to metoder som skiller seg ut: ***Opret*** og ***Tapret***, begge klassifisert som "Transaction Output", og kompatible med TxO2-modusen som brukes av protokollen.

### Multiprotokollforpliktelser - MPC

I denne delen ser vi på hvordan **RGB** håndterer aggregering av flere kontrakter (eller, mer presist, deres _overgangsbunter_) innenfor en enkelt forpliktelse (*commitment*) registrert i en Bitcoin-transaksjon via et deterministisk skjema (i henhold til `Opret` eller `Tapret`). For å oppnå dette skjer merkeliseringen av de ulike kontraktene i en struktur som kalles **MPC Tree** (_Multi Protocol Commitment Tree_). I dette avsnittet skal vi se på konstruksjonen av dette MPC-treet, hvordan man får tak i roten, og hvordan flere kontrakter kan dele den samme transaksjonen på en konfidensiell og entydig måte.

Multi Protocol Commitment (MPC) er utviklet for å dekke to behov:


- Konstruksjonen av `mpc::Commitment`-hash: denne vil bli inkludert i Bitcoin-blokkjeden i henhold til en `Opret`- eller `Tapret`-ordning, og må gjenspeile alle tilstandsendringene som skal valideres;
- Samtidig lagring av flere kontrakter i én enkelt _commitment_, slik at separate oppdateringer på flere eiendeler eller RGB-kontrakter kan håndteres i én enkelt Bitcoin-transaksjon.

Konkret tilhører hver _transition bundle_ en bestemt kontrakt. All denne informasjonen settes inn i et **MPC-tre**, hvis rot (`mpc::Root`) deretter hashes igjen for å gi `mpc::Commitment`. Det er denne siste hashen som plasseres i Bitcoin-transaksjonen (_vitnetransaksjon_), i henhold til den deterministiske metoden som er valgt.

![RGB-Bitcoin](assets/fr/042.webp)

#### MPC Root Hash

Verdien som faktisk skrives på kjeden (i `Opret` eller `Tapret`) kalles `mpc::Commitment`. Denne beregnes i form av [BIP-341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki), i henhold til formelen :

```txt
mpc::Commitment = SHA-256(SHA-256(mpc_tag) || SHA-256(mpc_tag) || depth || cofactor || mpc::Root )
```

hvor :


- `mpc_tag` er en tag: `urn:ubideco:mpc:commitment#2024-01-31`, valgt i henhold til [RGB tagging conventions] (https://github.com/RGB-WG/rgb-core/blob/master/doc/Commitments.md);
- `depth` (1 byte) angir dybden på *MPC-treet* ;
- cofactor` (16 bits, i Little Endian) er en parameter som brukes for å sikre at posisjonene som tildeles hver kontrakt i treet, er unike;
- `mpc::Root` er roten til *MPC Tree*, beregnet i henhold til prosessen som beskrives i neste avsnitt.

![RGB-Bitcoin](assets/fr/044.webp)

#### MPC Trekonstruksjon

For å bygge dette MPC-treet må vi sørge for at hver kontrakt tilsvarer en unik bladposisjon. Anta at vi har :


- c` kontrakter som skal inkluderes, indeksert av `i` i `i = {0,1,...,C-1}` ;
- For hver kontrakt `c_i` har vi en identifikator `ContractId(i) = c_i`.

Deretter konstruerer vi et tre med bredde `w` og dybde `d` slik at `2^d = w`, med `w > C`, slik at hver kontrakt kan plasseres i et eget _blad_. Posisjonen `pos(c_i)` til hver kontrakt i treet er bestemt av :

```txt
pos(c_i) = c_i mod (w - cofactor)
```

hvor `kofaktor` er et heltall som øker sannsynligheten for å få forskjellige posisjoner for hver kontrakt. I praksis følger konstruksjonen en iterativ prosess:


- Vi starter med en minimumsdybde (`d=3` for å skjule det nøyaktige antallet kontrakter);
- Vi prøver forskjellige "kofaktorer" (opp til "w/2", eller maksimalt 500 av ytelseshensyn);
- Hvis vi ikke klarer å plassere alle kontraktene uten kollisjon, inkrementerer vi `d` og begynner på nytt.

Målet er å unngå trær som er for høye, samtidig som risikoen for kollisjon holdes på et minimum. Merk at kollisjonsfenomenet følger en tilfeldig fordelingslogikk, knyttet til [Anniversary Paradox] (https://en.wikipedia.org/wiki/Birthday_problem).

#### Bebodde blader

Når `C` distinkte posisjoner `pos(c_i)` er oppnådd for kontrakter `i = {0,1,...,C-1}`, fylles hvert ark med en hashfunksjon (*tagged hash*):

```txt
tH_MPC_LEAF(c_i) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x10 || c_i || BundleId(c_i))
```

hvor :


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, er alltid valgt i henhold til Merkle-konvensjonene for RGB ;
- `0x10` identifiserer et _kontraktsblad_ ;
- `c_i` er kontraktsidentifikatoren på 32 byte (utledet fra Genesis-hash);
- bundleId(c_i)` er en 32-byte hash som beskriver settet med `State Transitions` i forhold til `c_i` (samlet i en *Transition Bundle*).

#### Ubebodde blader

De resterende bladene, som ikke er tilordnet en kontrakt (dvs. `w - C` -bladene), fylles med en "dummy"-verdi (_entropiblad_) :

```txt
tH_MPC_LEAF(j) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x11 || entropy || j )
```

hvor :


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, er alltid valgt i henhold til Merkle-konvensjonene for RGB ;
- `0x11` betegner et _entropiblad_ ;
- `entropi` er en tilfeldig verdi på 64 byte, valgt av den som bygger treet;
- `j` er posisjonen (i 32 bits Little Endian) til dette bladet i treet.

#### MPC-noder

Etter å ha generert `w`-bladene (bebodde eller ikke), går vi videre til merkelisering. Eventuelle interne noder hashes på følgende måte:

```txt
tH_MPC_BRANCH(tH1 || tH2) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || b || d || w || tH1 || tH2)
```

hvor :


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, er alltid valgt i henhold til Merkle-konvensjonene for RGB ;
- b` er _forgreningsfaktoren_ (8 bits). Oftest er `b=0x02` fordi treet er binært og komplett;
- d` er dybden på noden i treet;
- `w` er treets bredde (i 256-biters Little Endian binær);
- tH1` og `tH2` er hashene til de underordnede nodene (eller bladene), som allerede er beregnet som vist ovenfor.

Ved å fortsette på denne måten får vi roten `mpc::Root`. Deretter kan vi beregne `mpc::Commitment` (som forklart ovenfor) og sette den inn i kjeden.

For å illustrere dette, la oss tenke oss et eksempel der `C=3` (tre kontrakter). Deres posisjoner antas å være `pos(c_0)=7`, `pos(c_1)=4`, `pos(c_2)=2`. De andre bladene (posisjon 0, 1, 3, 5, 6) er _entropiblader_. Diagrammet nedenfor viser rekkefølgen av hasher til roten med :


- `BUNDLE_i` som representerer `BundleId(c_i)` ;
- `tH_MPC_LEAF(A)` og så videre, som representerer blader (noen for kontrakter, andre for entropi) ;
- Hver gren `tH_MPC_BRANCH(...)` kombinerer hashene til sine to barn.

Det endelige resultatet er **mpc::Root**, og deretter `mpc::Commitment`.

![RGB-Bitcoin](assets/fr/053.webp)

#### Kontroll av MPC-akselen

Når en kontrollør ønsker å sikre at en `c_i`-kontrakt (og dens `BundleId`) er inkludert i den endelige `mpc::Commitment`, mottar han ganske enkelt et Merkle-bevis. Dette beviset angir nodene som trengs for å spore bladene (i dette tilfellet `c_i`'s _kontraktblad_) tilbake til roten. Det er ikke nødvendig å avsløre hele *MPC-treet*: dette beskytter konfidensialiteten til andre kontrakter.

I eksempelet trenger en `c_2`-verifikator bare en mellomliggende hash (`tH_MPC_LEAF(D)`), to `tH_MPC_BRANCH(...)`, `pos(c_2)`-posisjonsbeviset og `cofactor`-verdien. Den kan deretter rekonstruere roten lokalt, deretter beregne `mpc::Commitment` på nytt og sammenligne den med den som er skrevet i Bitcoin-transaksjonen (i `Opret` eller `Tapret`).

![RGB-Bitcoin](assets/fr/054.webp)

Denne mekanismen sikrer at :


- Status i forhold til `c_2` er faktisk inkludert i den samlede informasjonsblokken (klientsiden);
- Ingen kan bygge en alternativ historikk med den samme transaksjonen, fordi _commitment_ i kjeden peker til en enkelt MPC-rot.

#### Sammendrag av MPC-strukturen

Multi Protocol Commitment* (MPC) er prinsippet som gjør det mulig for RGB å samle flere kontrakter i én enkelt Bitcoin-transaksjon, samtidig som forpliktelsenes unikhet og konfidensialitet overfor andre deltakere opprettholdes. Takket være den deterministiske konstruksjonen av treet tildeles hver kontrakt en unik posisjon, og tilstedeværelsen av "dummy"-blader (*Entropy Leaves*) maskerer delvis det totale antallet kontrakter som deltar i transaksjonen.

Hele Merkle-treet lagres aldri på klienten. Vi genererer ganske enkelt en _Merkle-sti_ for hver kontrakt som skal overføres til mottakeren (som deretter kan validere forpliktelsen). I noen tilfeller kan du ha flere aktiva som har gått gjennom samme UTXO. Da kan du slå sammen flere _Merkle-stier_ til en såkalt _multiprotokollforpliktelsesblokk_, slik at du unngår å duplisere for mye data.

Hvert _Merkle-bevis_ er derfor lett, spesielt ettersom treets dybde ikke vil overstige 32 i RGB. Det finnes også et begrep om "Merkle-blokk", som inneholder mer informasjon (tverrsnitt, entropi osv.), og som er nyttig for å kombinere eller separere flere grener.

Det er derfor det tok så lang tid å ferdigstille RGB. Vi hadde den overordnede visjonen fra 2019: å legge alt på klientsiden og sirkulere tokens utenfor kjeden. Men for detaljer som sharding for flere kontrakter, strukturen til Merkle-treet, hvordan man håndterer kollisjoner og sammenslåingsbevis ... alt dette krevde iterasjoner.

### Ankere: en global samling

I forlengelsen av konstruksjonen av våre forpliktelser (`Opret` eller `Tapret`) og vår MPC (*Multi Protocol Commitment*), må vi ta for oss begrepet **Anchor** i RGB-protokollen. Et anker er en validert struktur på klientsiden som samler elementene som trengs for å verifisere at en Bitcoin-forpliktelse faktisk inneholder spesifikk kontraktsinformasjon. Med andre ord oppsummerer et anker alle dataene som trengs for å validere _forpliktelsene_ beskrevet ovenfor.

Et anker består av tre ordnede felt:


- `Txid`
- `MPC Proof`
- ekstra transaksjonsbevis - ETP

Hvert av disse feltene spiller en rolle i valideringsprosessen, enten det dreier seg om å rekonstruere den underliggende Bitcoin-transaksjonen eller å bevise eksistensen av en skjult forpliktelse (spesielt i tilfellet `Tapret`).

#### TxId

Txid-feltet tilsvarer 32-byte-identifikatoren til Bitcoin-transaksjonen som inneholder `Opret`- eller `Tapret`-forpliktelsen.

I teorien ville det være mulig å finne dette `Txid` ved å spore kjeden av tilstandsoverganger som i seg selv peker til hver vitnetransaksjon, i tråd med logikken til Single-use Seals. Men for å forenkle og fremskynde verifiseringen inkluderes dette `Txid` ganske enkelt i ankeret, slik at validatoren slipper å gå tilbake gjennom hele historikken utenfor kjeden.

#### MPC Proof

Det andre feltet, `MPC Proof`, refererer til beviset på at denne kontrakten (f.eks. `c_i`) er inkludert i _Multi Protocol Commitment_. Det er en kombinasjon av :


- `pos_i`, posisjonen til denne kontrakten i MPC-treet;
- cofactor`, verdien som er definert for å løse posisjonskollisjoner;
- `Merkle Proof`, dvs. settet med noder og hasher som brukes til å rekonstruere MPC-roten og verifisere at kontraktsidentifikatoren og dens `Transition Bundle` er forpliktet til roten.

Denne mekanismen ble beskrevet i forrige avsnitt om oppbygging av *MPC-treet*, der hver kontrakt får et unikt blad takket være :

```txt
pos(c_i) = c_i mod (w - cofactor)
```

Deretter brukes et deterministisk merkeliseringsskjema til å aggregere alle bladene (kontrakter + entropi). Til slutt gjør `MPC Proof` det mulig å rekonstruere roten lokalt og sammenligne den med `mpc::Commitment` som er inkludert i kjeden.

#### Ekstra transaksjonsbevis - ETP

Det tredje feltet, **ETP**, avhenger av hvilken type forpliktelse som brukes. Hvis forpliktelsen er av typen `Opret`, er det ikke nødvendig med ytterligere bevis. Validatoren inspiserer den første `OP_RETURN`-utgangen fra transaksjonen og finner `mpc::Commitment` direkte der.

**Hvis forpliktelsen er av typen `Tapret`**, må det leveres et tilleggsbevis kalt *Extra Transaction Proof - ETP*. Det inneholder :


- Den interne offentlige nøkkelen (`P`) til taproot-utdataene som *commitment* er innebygd i;
- Partnernodene til `Script Path Spend` (når Tapret *commitment* settes inn i et skript), for å bevise den nøyaktige plasseringen av dette skriptet i taproot-treet:
 - Hvis `Tapret` *commitment* er på den høyre grenen, avslører vi den venstre noden (f.eks. `tHABC`),
 - Hvis `Tapret` *forpliktelsen* er på venstre side, må du avsløre 2 noder (f.eks. `tHAB` og `tHC`) for å bevise at ingen annen *forpliktelse* er til stede på høyre side.
- Nonce kan brukes til å "mine" den beste konfigurasjonen, slik at *commitment* kan plasseres til høyre i treet (bevisoptimalisering).

Dette tilleggsbeviset er viktig fordi `Tapret`-forpliktelsen, i motsetning til `Opret`, er integrert i strukturen til et taproot-skript, noe som krever at man avslører en del av taproot-treet for å kunne validere plasseringen av *forpliktelsen*.

![RGB-Bitcoin](assets/fr/045.webp)

**Anchors ** innkapsler derfor all informasjonen som kreves for å validere en Bitcoin-forpliktelse i sammenheng med RGB. De indikerer både den relevante transaksjonen (`Txid`) og beviset på kontraktsposisjonering (`MPC Proof`), samtidig som de administrerer tilleggsbeviset (`ETP`) i tilfelle `Tapret`. På denne måten beskytter et anker integriteten og unikheten til tilstanden utenfor kjeden ved å sikre at den samme transaksjonen ikke kan tolkes på nytt for andre kontraktsdata.

### Konklusjon

I dette kapittelet går vi gjennom :


- Hvordan bruke Single-use Seals-konseptet i Bitcoin (spesielt via et _outpoint_);
- De ulike metodene for å sette inn en _commitment_ i en transaksjon på en deterministisk måte (Sig tweak, Key tweak, witness tweak, op_return, Taproot/Tapret) ;
- Årsakene til at RGB fokuserer på Tapret-forpliktelser ;
- Håndtering av flere kontrakter via _multiprotokollforpliktelser_, avgjørende hvis du ikke ønsker å eksponere en hel stat eller andre kontrakter når du vil bevise et bestemt poeng;
- Vi har også sett hvilken rolle _Anchors_ spiller, som samler alt sammen (transaksjons-TXID, Merkle-trebevis og Taproot-bevis) i én enkelt pakke.

I praksis er den tekniske implementasjonen delt mellom flere dedikerte Rust _crates_ (i _client_side_validation_, _commit-verify_, _bp_core_ osv.). De grunnleggende begrepene er der:

![RGB-Bitcoin](assets/fr/046.webp)

I neste kapittel skal vi se på den rene off-chain-komponenten i RGB, nemlig kontraktslogikken. Vi skal se hvordan RGB-kontrakter, organisert som delvis replikerte _finite state-maskiner_, oppnår mye høyere uttrykksfullhet enn Bitcoin-skript, samtidig som konfidensialiteten til dataene deres bevares.

## Introduksjon til smartkontrakter og deres tilstander

<chapterId>04a9569f-3563-5382-bf53-0c7069343ba0</chapterId>

![video](https://youtu.be/tmAVdyXGmj4)

I dette og neste kapittel skal vi se nærmere på begrepet **smart kontrakt** i RGB-miljøet og utforske de ulike måtene disse kontraktene kan definere og utvikle sin *tilstand* på. Vi skal se hvorfor RGB-arkitekturen, ved hjelp av den ordnede sekvensen av Single-use Seals, gjør det mulig å utføre ulike typer ***kontraktsoperasjoner*** på en skalerbar måte og uten å gå gjennom et sentralisert register. Vi skal også se på den grunnleggende rollen som ***Forretningslogikk*** spiller i utviklingen av kontraktstilstanden.

### Smartkontrakter og digitale ihendehaverrettigheter

RGBs mål er å tilby en infrastruktur for implementering av smartkontrakter på Bitcoin. Med "smartkontrakt" mener vi en avtale mellom flere parter som håndheves automatisk og beregningsmessig, uten menneskelig inngripen for å håndheve klausulene. Med andre ord håndheves kontraktens lov av programvaren, ikke av en betrodd tredjepart.

Denne automatiseringen reiser spørsmålet om desentralisering: Hvordan kan vi frigjøre oss fra et sentralisert register (f.eks. en sentral plattform eller database) for å administrere eierskap og kontraktsoppfyllelse? Den opprinnelige ideen, som RGB har tatt opp, er å gå tilbake til en eierform kjent som "ihendehaverinstrumenter". Historisk sett ble visse verdipapirer (obligasjoner, aksjer osv.) utstedt i ihendehaverform, slik at alle som fysisk hadde dokumentet i sin besittelse, kunne håndheve sine rettigheter.

![RGB-Bitcoin](assets/fr/055.webp)

RGB overfører dette konseptet til den digitale verden: Rettigheter (og forpliktelser) er innkapslet i data som manipuleres utenfor kjeden, og statusen til disse dataene valideres av deltakerne selv. Dette gir på forhånd en mye større grad av konfidensialitet og uavhengighet enn andre tilnærminger basert på offentlige registre.

### Introduksjon til Smart Contract RGB-status

En smartkontrakt i RGB kan sees på som en tilstandsmaskin, definert av :


- En **State**, dvs. et sett med informasjon som gjenspeiler kontraktens nåværende konfigurasjon;
- En **forretningslogikk** (sett med regler) som beskriver under hvilke betingelser og av hvem tilstanden kan endres.

![RGB-Bitcoin](assets/fr/056.webp)

Det er viktig å forstå at disse kontraktene ikke er begrenset til enkel overføring av tokens. De kan omfatte et bredt spekter av bruksområder: fra tradisjonelle eiendeler (tokens, aksjer, obligasjoner) til mer komplekse mekanikker (bruksrettigheter, kommersielle vilkår osv.). I motsetning til andre blokkjeder, der kontraktskoden er tilgjengelig og kan kjøres av alle, avgrenser RGBs tilnærming tilgangen til og kunnskapen om kontrakten til deltakerne ("***kontraktsdeltakere***"). Det finnes flere roller:


- Utstederen** eller skaperen av kontrakten, som definerer kontraktens Genesis og de opprinnelige variablene;
- Parter med rettigheter** (*eierskap*) eller andre håndhevingsmuligheter ;
- Observatører**, som potensielt er begrenset til å se visse opplysninger, men som ikke kan utløse endringer.

Denne rolledelingen bidrar til sensurresistens ved å sikre at kun autoriserte personer kan samhandle med kontraktsstaten. Det gir også RGB muligheten til å skalere horisontalt: De fleste valideringer skjer utenfor blokkjeden, og bare kryptografiske ankere (*forpliktelsene*) er innskrevet på Bitcoin.

### Status og forretningslogikk i RGB

Rent praktisk tar kontraktens **forretningslogikk** form av regler og skript, definert i det RGB kaller et **skjema**. Skjemaet koder for :


- Statlig struktur (hvilke felt er offentlige? Hvilke felt eies av hvilke parter?
- Gyldighetsbetingelser (hva må sjekkes før en tilstandsoppdatering godkjennes?) ;
- Fullmakter (hvem kan sette i gang en *State Transition*? Hvem kan bare observere?).

Samtidig er **Kontraktsstaten** ofte delt inn i to komponenter:


- En **Global State**: offentlig del, potensielt observerbar av alle (avhengig av konfigurasjon);
- Owned States**: private deler, tildelt spesifikt til eiere via UTXO-er som det refereres til i kontraktslogikken.

Som vi skal se i de neste kapitlene, må enhver statusoppdatering (*Contract Operation*) forankres til en Bitcoin _commitment_ (via `Opret` eller `Tapret`) og overholde *Business Logic*-skript for å anses som gyldig.

### Kontraktsoperasjoner: statens tilblivelse og utvikling

I RGB-universet er en ***Kontraktsoperasjon*** enhver hendelse som endrer kontrakten fra en **gammel tilstand** til en **ny tilstand**. Disse operasjonene følger følgende logikk:


- Vi tar til etterretning den nåværende statusen for kontrakten;
- Vi bruker regelen eller operasjonen (en ***State Transition***, en ***Genesis*** hvis det er den aller første tilstanden, eller en ***State Extension*** hvis det finnes en offentlig *valens* som skal utløses på nytt);
- Vi forankrer endringen via en ny _commitment_ på blokkjeden, lukker en _single-use seal_ og oppretter en annen ;
- De berørte rettighetshaverne validerer lokalt (*klientsiden*) at overgangen er i samsvar med *skjemaet* og at den tilhørende Bitcoin-transaksjonen er registrert i kjeden.

![RGB-Bitcoin](assets/fr/057.webp)

Sluttresultatet er en oppdatert kontrakt, nå med en annen tilstand. Denne overgangen krever ikke at hele Bitcoin-nettverket er opptatt av detaljene, siden bare et lite kryptografisk fingeravtrykk (_commitment_) blir registrert i blokkjeden. Sekvensen av Single-use Seals forhindrer dobbeltbruk eller dobbeltbruk av staten.

### Operasjonskjeden: fra Genesis til Terminal State

For å sette dette i perspektiv starter en RGB-smartkontrakt med en **Genesis**, den aller første tilstanden. Deretter følger ulike kontraktsoperasjoner etter hverandre og danner en DAG (*Directed Acyclic Graph*) av operasjoner:


- Hver overgang er basert på en tidligere tilstand (eller flere, i tilfelle konvergerende overganger);
- Den kronologiske rekkefølgen garanteres ved at hver overgang inkluderes i et Bitcoin-anker, tidsstemplet og uforanderlig takket være konsensus gjennom Proof-of-Work ;
- Når det ikke pågår flere operasjoner, nås en **Terminaltilstand**: kontraktens siste og fullstendige tilstand.

![RGB-Bitcoin](assets/fr/012.webp)

Denne DAG-topologien (i stedet for en enkel lineær kjede) gjenspeiler muligheten for at ulike deler av kontrakten kan utvikles parallelt, så lenge de ikke er i strid med hverandre. RGB sørger da for å unngå eventuelle uoverensstemmelser ved å verifisere hver enkelt deltaker på *klientsiden*.

### Sammendrag

Smartkontrakter i RGB introduserer en modell for digitale ihendehaverinstrumenter, desentralisert, men forankret i Bitcoin for tidsstempling og garanti for rekkefølgen på transaksjoner. Automatisert utførelse av disse kontraktene er basert på :


- En **Kontraktstatus*, som angir kontraktens nåværende konfigurasjon (rettigheter, saldoer, variabler osv.);
- En **forretningslogikk** (*Schema*) som definerer hvilke overganger som er tillatt og hvordan de skal valideres;
- Contract Operations**, som oppdaterer denne tilstanden trinn for trinn, takket være forpliktelser forankret i Bitcoin-transaksjoner.

I neste kapittel vil vi gå nærmere inn på den konkrete representasjonen av disse ***tilstandene*** og ***tilstandsovergangene*** på off-chain-nivå, og hvordan de forholder seg til UTXO-ene og single-use-seglene som er innebygd i Bitcoin. Dette vil være en mulighet til å se hvordan RGBs interne mekanikk, basert på validering på klientsiden, klarer å opprettholde konsistensen i smartkontrakter samtidig som datakonfidensialiteten bevares.

## RGB-kontraktsoperasjoner

<chapterId>78c44e88-50c4-5ec4-befe-456c1a9f080b</chapterId>

![video](https://youtu.be/lUTjeuM0oTA)

I dette kapittelet skal vi se på hvordan operasjoner i smartkontrakter og tilstandsoverganger fungerer, igjen innenfor RGB-protokollen. Målet er også å forstå hvordan flere deltakere samarbeider om å overføre eierskapet til en eiendel.

### Tilstandsoverganger og deres mekanikk

Det generelle prinsippet er fortsatt validering på klientsiden, der tilstandsdata oppbevares av eieren og valideres av mottakeren. Det spesielle med RGB er imidlertid at Bob, som mottaker, ber Alice om å innlemme visse opplysninger i kontraktsdataene for å få reell kontroll over den mottatte eiendelen, via en skjult referanse til en av sine UTXO-er.

For å illustrere prosessen med en *State Transition* (som er en av de grunnleggende ***Contract Operations*** i RGB), kan vi ta et steg-for-steg-eksempel på en overføring av eiendeler mellom Alice og Bob:

**Utgangssituasjon:**

Alice har en ***stash RGB*** med lokalt validerte data (*klientsiden*). Dette lageret refererer til en av hennes UTXOer på Bitcoin. Dette betyr at en _seal-definisjon_ i disse dataene peker til en UTXO som tilhører Alice. Tanken er å gjøre det mulig for henne å overføre visse digitale rettigheter knyttet til en eiendel (f.eks. RGB-tokens) til Bob.

![RGB-Bitcoin](assets/fr/058.webp)

**Bob har også UTXOer :**

Bob, derimot, har minst én egen UTXO, uten noen direkte kobling til Alices. Hvis Bob ikke har noen UTXO, er det likevel mulig å overføre til ham ved hjelp av selve *vitnetransaksjonen*: Resultatet av denne transaksjonen vil da inkludere forpliktelsen (_commitment_) og implisitt knytte eierskapet til den nye kontrakten til Bob.

![RGB-Bitcoin](assets/fr/059.webp)

**Konstruksjon av den nye eiendommen (*Ny tilstand*) :**

Bob sender Alice informasjon kodet i form av en ***faktura*** (vi vil gå nærmere inn på fakturakonstruksjon i senere kapitler), og ber henne om å opprette en ny tilstand som er i samsvar med kontraktens regler. Denne tilstanden vil inneholde en ny *seal-definisjon* som peker til en av Bobs UTXO-er. På denne måten får Bob eierskap til eiendelene som er definert i denne nye tilstanden, for eksempel en viss mengde RGB-tokens.

![RGB-Bitcoin](assets/fr/060.webp)

**Forberedelse av prøvetransaksjonen:**

Alice oppretter deretter en Bitcoin-transaksjon som bruker UTXO-en som ble referert til i det forrige seglet (den som legitimerte henne som innehaver). I utdataene fra denne transaksjonen settes det inn en *forpliktelse* (via `Opret` eller `Tapret`) for å forankre den nye RGB-tilstanden. Forpliktelsene `Opret` eller `Tapret` er avledet fra et *MPC-tre* (som vi har sett i tidligere kapitler), som kan aggregere flere overganger fra forskjellige kontrakter.

**Overføring av *Sending* til Bob:**

Før transaksjonen sendes ut, sender Alice en ***Consignment*** til Bob som inneholder alle nødvendige data på *klientsiden* (hans *stash*) og den nye tilstandsinformasjonen i Bobs favør. På dette tidspunktet bruker Bob RGB-konsensusreglene:


- Den validerer alle RGB-dataene i *Consignment*, inkludert den nye statusen som gir den eierskap til eiendelen;
- Ved hjelp av *Anchors* som er inkludert i *Consignment*, verifiserer den kronologien til vitnetransaksjonene (fra Genesis til den siste overgangen) og validerer de tilsvarende forpliktelsene i blokkjeden.

**Overgangen er fullført:**

Hvis Bob er fornøyd, kan han gi sin godkjenning (for eksempel ved å signere *forsendelsen*). Alice kan deretter kringkaste den forberedte prøvetransaksjonen. Når dette er bekreftet, lukkes forseglingen som Alice tidligere hadde, og eierskapet formaliseres av Bob. Sikkerheten mot dobbeltbruk er basert på samme mekanisme som i Bitcoin: UTXO-en er brukt opp, noe som beviser at Alice ikke lenger kan gjenbruke den.

![RGB-Bitcoin](assets/fr/061.webp)

Den nye tilstanden refererer nå til Bobs UTXO, noe som gir Bob eierskapet som Alice tidligere hadde. Bitcoin-utgangen der RGB-dataene er forankret, blir det ugjenkallelige beviset på overføringen av eierskapet.

Et eksempel på en minimal DAG (*Directed Acyclic Graph*) bestående av to kontraktsoperasjoner (en **Genesis** og deretter en ***State Transition***) kan illustrere hvordan RGB-staten (*klientsiden*-laget, i rødt) kobles til Bitcoin-blokkjeden (*Commitment*-laget, i oransje).

![RGB-Bitcoin](assets/fr/062.webp)

Den viser at en Genesis definerer en forsegling (*forseglingsdefinisjon*), deretter lukker en *State Transition* denne forseglingen for å opprette en ny i en annen UTXO.

I denne sammenhengen vil vi minne om noen begreper:


- En ***Oppgave*** kombinerer :
    - En ***Seal-definisjon*** (som peker mot en UTXO);
    - Owned States**, dvs. data knyttet til eierskap (for eksempel antall tokens som er overført).
- En **Global State** samler kontraktens generelle egenskaper, som er synlig for alle, og sikrer global konsistens i utviklingen.

State Transitions**, som ble beskrevet i forrige kapittel, er den viktigste formen for kontraktsoperasjoner. De refererer til én eller flere tidligere tilstander (fra Genesis eller en annen tilstandsovergang) og oppdaterer dem til en ny tilstand.

![RGB-Bitcoin](assets/fr/063.webp)

Dette diagrammet viser hvordan flere segl kan lukkes i en *State Transition Bundle* i en enkelt eksempeltransaksjon, samtidig som nye segl åpnes. Et interessant trekk ved RGB-protokollen er dens evne til å skalere: Flere overganger kan aggregeres til en Transition Bundle, der hver aggregering er knyttet til et distinkt blad i *MPC-treet* (en unik bundle-identifikator). Takket være *Deterministic Bitcoin Commitment* (DBC)-mekanismen settes hele meldingen inn i en `Tapret`- eller `Opret`-utgang, samtidig som den lukker tidligere forseglinger og eventuelt definerer nye. Anchor* fungerer som en direkte kobling mellom forpliktelsen som er lagret i blokkjeden og valideringsstrukturen på klientsiden (*klientsiden*).

I de følgende kapitlene skal vi se på alle komponentene og prosessene som er involvert i å bygge og validere en tilstandsovergang. De fleste av disse elementene er en del av RGB-konsensus, som er implementert i **RGB Core Library**.

### Overgangspakke

På RGB er det mulig å samle ulike tilstandsoverganger som tilhører samme kontrakt (dvs. som deler samme **ContractId**, avledet fra Genesis **OpId**). I det enkleste tilfellet, som mellom Alice og Bob i eksempelet ovenfor, inneholder en **Transition Bundle** bare én overgang. Men støtte for operasjoner med flere betalere (for eksempel coinjoins, Lightning Channel-åpninger osv.) betyr at flere brukere kan kombinere sine State Transitions i én enkelt pakke.

Når disse overgangene er samlet inn, forankres de (ved hjelp av MPC + DBC-mekanismen) i en enkelt Bitcoin-transaksjon:


- Hver tilstandsovergang hashes og grupperes i en overgangsbunt ;
- Overgangspakken blir selv hashet og satt inn i MPC-trebladet som tilsvarer denne kontrakten (en BundleId);
- MPC-treet kobles til slutt inn via `Opret` eller `Tapret` i vitnetransaksjonen, som dermed lukker de forbrukte forseglingene og definerer de nye forseglingene.

Teknisk sett er **BundleId** som settes inn i MPC-arket, hentet fra en tagget hash som brukes på den strenge serialiseringen av *InputMap*-feltet i bunten:

```txt
BundleId = SHA256( SHA256(bundle_tag) || SHA256(bundle_tag) || InputMap )
```

Der `bundle_tag = urn:lnp-bp:rgb:bundle#2024-02-03` for eksempel.

*InputMap* er en datastruktur som for hver inngang `i` i eksempeltransaksjonen viser referansen til *OpId* for den tilsvarende tilstandsovergangen. For eksempel

```txt
InputMap =
N               input_0    OpId(input_0)    input_1    OpId(input_1)   ...    input_N-1  OpId(input_N-1)
|____________________| |_________||______________| |_________||______________|       |__________||_______________|
16-bit Little Endian   32-bit LE   32-byte hash
|_________________________| |_________________________|  ...  |___________________________|
MapElement1                MapElement2                       MapElementN
```


- n er det totale antallet oppføringer i transaksjonen som refererer til en OPId;
- opId(input_j)` er operasjonsidentifikatoren til en av tilstandsovergangene som finnes i pakken.

Ved å referere til hver oppføring bare én gang og på en ordnet måte, unngår vi at det samme seglet brukes to ganger i to samtidige State Transitions.

### Generering av tilstand og aktiv tilstand

Statusoverganger kan derfor brukes til å overføre eierskapet til en eiendel fra én person til en annen. Dette er imidlertid ikke de eneste mulige operasjonene i RGB-protokollen. Protokollen definerer tre **Contract Operations** :


- Tilstandsovergang** ;
- Genesis** ;
- State Extension**.

Blant disse kalles **Genesis** og **State Extension** noen ganger for "*State Generation operations*", fordi de oppretter nye tilstander uten å lukke noen umiddelbart. Dette er et svært viktig poeng: **Genesis** og **State Extension** innebærer ikke at en forsegling lukkes. De definerer snarere et nytt segl, som deretter må brukes av en påfølgende **State Transition** for å bli virkelig validert i blokkjedehistorikken.

![RGB-Bitcoin](assets/fr/064.webp)

En kontrakts **Active State** defineres ofte som settet med de nyeste tilstandene som er resultatet av transaksjonshistorikken (DAG), som starter med Genesis og følger alle ankere i Bitcoin-blokkjeden. Eventuelle gamle tilstander som allerede er foreldet (dvs. knyttet til brukte UTXO-er), anses ikke lenger som aktive, men er fortsatt viktige for å kontrollere konsistensen i historikken.

### Genesis

Genesis er utgangspunktet for alle RGB-kontrakter. Den opprettes av kontraktutstederen og definerer de innledende parameterne, i samsvar med **Schema**. Når det gjelder et RGB-token, kan Genesis for eksempel spesifisere :


- Antall tokens som opprinnelig ble opprettet og eierne av disse;
- Totalt mulig emisjonstak ;
- Eventuelle regler for gjenutstedelse, og hvilke deltakere som er kvalifisert.

Som den første transaksjonen i kontrakten refererer ikke Genesis til noen tidligere tilstand, og den lukker heller ikke noe segl. For å vises i historikken og bli validert, må Genesis imidlertid **forbrukes** (lukkes) av en første tilstandsovergang (ofte en skanning/auto-spend-transaksjon til utstederen selv, eller den første distribusjonen til brukerne).

### State Extension

State Extensions** tilbyr en original funksjon for smartkontrakter. De gjør det mulig å innløse visse digitale rettigheter (*Valencies*) som er fastsatt i kontraktsdefinisjonen, uten å lukke forseglingen umiddelbart. Oftest gjelder dette :


- Distribuerte tokenutstedelser;
- Mekanismer for bytte av eiendeler ;
- Betingede gjenutgivelser (som kan omfatte ødeleggelse av andre eiendeler osv.).

Teknisk sett refererer en tilstandsutvidelse til en *Redeem* (en bestemt type RGB-inndata) som tilsvarer en *Valency* som er definert tidligere (for eksempel i Genesis eller en annen tilstandsovergang). Den definerer et nytt segl, som er tilgjengelig for personen eller tilstanden som drar nytte av det. For at dette seglet skal tre i kraft, må det brukes av en påfølgende tilstandsovergang.

![RGB-Bitcoin](assets/fr/065.webp)

For eksempel: Genesis oppretter en utstedelsesrett (*Valency*). Denne kan utøves av en autorisert aktør, som deretter bygger en State Extension :


- Det refererer til Valency (innløsning);
- Den oppretter en ny *assignment* (nye *Owned State*-data) som peker til en UTXO ;
- En fremtidig tilstandsovergang, utstedt av eieren av denne nye UTXO-en, vil faktisk overføre eller distribuere de nyutstedte tokens.

### Komponenter i en kontraktsoperasjon

Jeg vil nå ta en detaljert titt på hvert av elementene som inngår i en **Contract Operation** i RGB. En Contract Operation er en handling som endrer tilstanden til en kontrakt, og som valideres på klientsiden, på en deterministisk måte, av den legitime mottakeren. Vi skal se nærmere på hvordan en Contract Operation tar hensyn til kontraktens **gamle tilstand** (*Old State*) på den ene siden, og definisjonen av en **ny tilstand** (*New State*) på den andre siden.

```txt
+---------------------------------------------------------------------------------------------------------------------+
|  Contract Operation                                                                                                 |
|                                                                                                                     |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|  | Ffv |     | ContractId | SchemaId |      | TransitionType | ExtensionType |      | Testnet |     | AltLayers1 |  |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Metadata                                      |  | Global State                                               |  |
|  |                                               |  | +----------------------------------+                       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  | |          Structured Data            |       |  | | |  GlobalStateType  | |  Data  | |     ...     ...       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  |                                               |  | +----------------------------------+                       |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|                                                                                                                     +---------> OpId |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|  | Inputs                                        |  | Assignments                                                |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #1                                  | |  | | Assignment #1                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ + ---------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #2                                  | |  | | Assignment #2                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  |       ...           ...          ...          |  |     ...          ...             ...                       |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Redeems                                       |  | Valencies                                                  |  |
|  |                                               |  |                                                            |  |
|  | +------------------------------+              |  |                                                            |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
| OpId +--------------> PrevOpId | | ValencyType | |  ...   ...   |  |  | ValencyType |  | ValencyType |         ...              |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
|  | +------------------------------+              |  |                                                            |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------+
```

Hvis vi ser på diagrammet ovenfor, ser vi at en Contract Operation inneholder elementer som refererer til **New State** og andre som refererer til den oppdaterte **Old State**.

Elementene i den **Nye staten** er :


- Oppdrag**, der det er definert :
 - Definisjonen av **Seal**;
 - Den **eide staten**.
- Den **Globale staten**, som kan endres eller berikes ;
- Valencies**, eventuelt definert i en State Transition eller Genesis.

Den **gamle staten** refereres til via :


- Inputs**, som peker til *Assignments* av tidligere tilstandsoverganger (ikke til stede i Genesis);
- Redeems**, som refererer til tidligere definerte Valencies (kun i State Extensions).

I tillegg inneholder en kontraktsoperasjon mer generelle felt som er spesifikke for operasjonen:


- ffv` (*Fast-forward versjon*): heltall på 2 byte som angir kontraktsversjonen;
- transitionType` eller ExtensionType`: 16-biters heltall som angir overgangs- eller utvidelsestypen, i henhold til forretningslogikken;
- `ContractId`: 32-byte nummer som refererer til *OpId* for kontrakten Genesis. Inkludert i Transitions og Extensions, men ikke i Genesis ;
- schemaId: finnes bare i Genesis. Dette er en 32-byte hash som representerer kontraktens struktur (*Schema*);
- testnet`: Boolsk som angir om du er på Testnet- eller Mainnet-nettverket. Kun for Genesis;
- altlayers1`: variabel som identifiserer det alternative laget (sidekjede eller annet) som brukes til å forankre data i tillegg til Bitcoin. Bare til stede i Genesis ;
- metadata": felt som kan lagre midlertidig informasjon som er nyttig for å validere en kompleks kontrakt, men som ikke skal registreres i den endelige statushistorikken.

Til slutt komprimeres alle disse feltene ved hjelp av en tilpasset hashingprosess for å produsere et unikt fingeravtrykk, `OpId`. Denne `OpId`en integreres deretter i Transition Bundle, slik at den kan autentiseres og valideres i protokollen.

Hver *Contract Operation* identifiseres derfor av en 32-byte hash som heter `OpId`. Denne hashen beregnes ved hjelp av en SHA256-hash av alle elementene som inngår i operasjonen. Med andre ord har hver *Contract Operation* sin egen kryptografiske forpliktelse, som inneholder alle dataene som trengs for å verifisere autentisiteten og konsistensen til operasjonen.

En RGB-kontrakt identifiseres deretter med en `ContractId`, som er avledet fra Genesis `OpId` (siden det ikke finnes noen operasjon før Genesis). Konkret tar vi Genesis `OpId`, snur byte-rekkefølgen og bruker en Base58-koding. Denne kodingen gjør `ContractId` enklere å håndtere og gjenkjenne.

### Metoder og regler for statusoppdatering

**Contract State** representerer det settet med informasjon som RGB-protokollen må spore for en gitt kontrakt. Den består av :


- En enkelt global tilstand**: Dette er den offentlige, globale delen av kontrakten, som er synlig for alle;
- En eller flere Owned States**: Hver Owned State er knyttet til et unikt segl (og dermed en UTXO på Bitcoin). Det skilles mellom :
    - De **offentlig** eide statene,
    - De **private** eide statene.

![RGB-Bitcoin](assets/fr/066.webp)

Den *Globale tilstanden* er direkte inkludert i *Kontraktsoperasjonen* som en enkelt blokk. De *Owned States* er definert i hver *Assignment*, sammen med *Seal Definition*.

En viktig egenskap ved RGB er måten Global State og Owned States modifiseres på. Det finnes generelt to typer atferd:


- Foranderlig**: Når et tilstandselement er beskrevet som foranderlig, erstatter hver ny operasjon den forrige tilstanden med en ny tilstand. De gamle dataene anses da som foreldet;
- Akkumulerende**: Når et tilstandselement er definert som akkumulerende, legger hver ny operasjon til ny informasjon til den forrige tilstanden, uten å overskrive den. Resultatet er en slags akkumulert historikk.

Hvis et tilstandselement i kontrakten ikke er definert som muterbart eller kumulativt, vil dette elementet forbli tomt ved senere operasjoner (det finnes med andre ord ingen nye versjoner for dette feltet). Det er kontraktsskjemaet (dvs. den kodede forretningslogikken) som avgjør om en tilstand (Global eller Owned) er muterbar, kumulativ eller fast. Når Genesis er definert, kan disse egenskapene bare endres hvis kontrakten selv tillater det, for eksempel via en spesifikk State Extension.

Tabellen nedenfor illustrerer hvordan hver type kontraktsoperasjon kan manipulere (eller ikke manipulere) den globale tilstanden og den eide tilstanden:

| Genesis | State Extension | State Transition | State Transition

| ---------------------------- | :-----: | :-------------: | :--------------: |

| **Legg til global tilstand** | + | - | + | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

| n/a | - | + | **Mutasjon av global tilstand** | - | + | | | **Mutasjon av global tilstand

| **Legg til eid tilstand** | + | - | + | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

| **Mutasjon av eid tilstand** | n/a | Nei | + | | | **Mutasjon av eid tilstand

| **Legg til valenser** | + | + | + | + | + | | + | | | +

**`+`** : handling mulig hvis kontraktens skjema tillater det.

**`-``**: Operasjonen må bekreftes av en påfølgende tilstandsovergang (tilstandsutvidelsen alene lukker ikke engangsforseglingen).

I tillegg kan det skilles mellom det tidsmessige omfanget og oppdateringsrettighetene for hver type data i tabellen nedenfor:

metadata | Global State | Owned State | Global State | Owned State

| ------------------------------- | ---------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |

| Definert for en enkelt kontraktsoperasjon | Definert globalt for kontrakten | Definert for hvert segl (*Assignment*) | Definert for en enkelt kontraktsoperasjon | Definert globalt for kontrakten | Definert for hvert segl (*Assignment*) | Definert for hvert segl (*Assignment*) | Definert for hver kontrakt

| Ikke-aktualiserbar (flyktige data) | Transaksjon utstedt av aktører (utsteder osv.) | Avhenger av den rettmessige innehaveren av seglet (den som kan bruke det i en påfølgende transaksjon) | Ikke-aktualiserbar (flyktige data) | Avhenger av den rettmessige innehaveren av seglet (den som kan bruke det i en påfølgende transaksjon)

| Tilstanden er definert før operasjonen (av *Seal Definition* fra forrige operasjon) | Tilstanden er etablert ved slutten av operasjonen | Tilstanden er etablert ved slutten av operasjonen | Tilstanden er definert før operasjonen (av *Seal Definition* fra forrige operasjon) | Tilstanden er etablert ved slutten av operasjonen | Tilstanden er definert før operasjonen (av *Seal Definition* fra forrige operasjon)

### Global stat

Global State beskrives ofte som "ingen eier, alle vet". Den inneholder generell informasjon om kontrakten, som er offentlig synlig. I en kontrakt som utsteder tokener, kan den for eksempel inneholde :


- Tickeren (symbolsk forkortelse av tokenet): `ticker` ;
- Tokenets fulle navn: `name` ;
- Presisjon (antall desimaler): `presisjon` ;
- Opprinnelig tilbud (og/eller maksimal token-grense): `issuedSupply` ;
- Utstedelsesdato: `opprettet` ;
- Juridiske data eller annen offentlig informasjon: `data`.

Denne globale tilstanden kan plasseres på offentlige ressurser (nettsteder, IPFS, Nostr, Torrent osv.) og distribueres til samfunnet. Det økonomiske insentivet (behovet for å oppbevare og overføre disse tokens osv.) gjør det naturlig for kontraktsbrukere å vedlikeholde og spre disse dataene selv.

### Oppgaver

*Assignment* er den grunnleggende strukturen for å definere :


- Seglet (*Seal Definition*), som peker til en bestemt UTXO;
- *Owned State*, dvs. egenskapen eller dataene som er knyttet til dette seglet.

En *Assignment* kan ses på som en analog til en Bitcoin-transaksjon, men med mer fleksibilitet. Her ligger logikken i eiendomsoverføringen: *Assignment* knytter en bestemt type eiendel eller rettighet (`AssignmentType`) til et segl. Den som har den private nøkkelen til UTXO-en som er knyttet til dette seglet (eller den som kan bruke denne UTXO-en), anses som eier av denne *Owned State*.

En av RGBs store styrker ligger i muligheten til å avsløre (*reveal*) eller skjule (*conceal*) feltene *Seal Definition* og *Owned State* etter eget ønske. Dette gir en kraftig kombinasjon av konfidensialitet og selektivitet. Du kan for eksempel bevise at en overgang er gyldig uten å avsløre alle dataene, ved å gi den avslørte versjonen til personen som skal validere den, mens tredjeparter bare ser den skjulte versjonen (en hash). I praksis beregnes alltid `OpId` for en overgang ut fra de *skjulte* dataene.

![RGB-Bitcoin](assets/fr/067.webp)

#### Definisjon av segl

*Seal-definisjonen*, i sin åpenbare form, har fire grunnleggende felt: `txptr`, `vout`, `blinding` og `method` :


- txptr**: dette er en referanse til en UTXO på Bitcoin :
    - Når det gjelder en **Genesis-forsegling**, peker den direkte til en eksisterende UTXO (den som er knyttet til Genesis);
    - I tilfellet med en **Graph seal** kan vi ha :
        - En enkel `txid`, hvis den peker til en bestemt UTXO,
        - Eller en `WitnessTx`, som angir en selvreferanse: seglet peker til selve transaksjonen. Dette er spesielt nyttig når ingen ekstern UTXO er tilgjengelig, for eksempel i Lightning channel opening-transaksjoner, eller hvis mottakeren ikke har noen UTXO.
- vout** : utgangsnummeret til transaksjonen angitt av `txptr`. Kun til stede for en standard Graph seal (ikke for `WitnessTx`);
- blinding**: et tilfeldig tall på 8 byte, for å styrke konfidensialiteten og forhindre forsøk på å manipulere UTXO-ens identitet;
- method** : angir hvilken forankringsmetode som brukes (`Tapret` eller `Opret`).

Den *skjulte* formen av forseglingsdefinisjonen er en SHA256-hash (tagget) av sammenkjedningen av disse fire feltene, med en tagg som er spesifikk for RGB.

![RGB-Bitcoin](assets/fr/068.webp)

#### Eide stater

Den andre komponenten i *Assignment* er Owned State. I motsetning til Global State kan den eksistere i offentlig eller privat form:


- Offentlig eid stat**: Alle kjenner dataene som er knyttet til seglet. For eksempel et offentlig bilde;
- Private Owned State**: Dataene er skjult, kun kjent for eieren (og eventuelt validatoren om nødvendig). For eksempel antall tokens som innehas.

RGB definerer fire mulige tilstandstyper (*StateTypes*) for en Owned State:


- Deklarativ**: inneholder ingen numeriske data, bare en deklarativ rettighet (f.eks. stemmerett). Den skjulte og den avslørte formen er identiske;
- Fungible**: representerer en fungibel mengde (som poletter). I åpen form har vi `beløp` og `blinding`. I skjult form har vi en enkelt *Pedersen-forpliktelse* som skjuler beløpet og blinding;
- Structured**: lagrer strukturerte data (opptil 64 kB). I åpen form er det datablobben. I skjult form er det en tagget hash av denne blobben:

```txt
SHA-256(SHA-256(tag_data) || SHA-256(tag_data) || blob)
```

Med for eksempel :

```txt
tag_data = urn:lnp-bp:rgb:state-data#2024-02-12
```


- Attachments**: kobler en fil (lyd, bilde, binær osv.) til Owned State, og lagrer filhash `file_hash`, MIME-typen `media type` og et kryptografisk salt `salt`. Selve filen ligger et annet sted. I skjult form er den en hash tagget med de tre foregående dataelementene:

```txt
SHA-256(SHA-256(tag_attachment) || SHA-256(tag_attachment) || file_hash || media_type || salt)
```

Med for eksempel :

```txt
tag_attachment = urn:rgb:state-attach#2024-02-12
```

For å oppsummere, her er de fire mulige tilstandstypene i offentlig og skjult form:

```txt
State                      Concealed form                              Revealed form
+---------------------------------------------------------------------------------------------------------
+--------------------------------------------------------------------------------+
|                                                                                |
Declarative        |                              < void >                                          |
|                                                                                |
+--------------------------------------------------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------+ +----------+       |
Fungible           | | Pedersen Commitement | | <========== |         | Amount | | Blinding |       |
| +----------------------+ |             |         +--------+ +----------+       |
+--------------------------+             +---------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------------------+        |
Structured         | |     Tagged Hash      | | <========== |         |     Data Blob      |        |
| +----------------------+ |             |         +--------------------+        |
+--------------------------+             +---------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             | +-----------+ +------------+ +------+ |
Attachments        | |     Tagged Hash      | | <========== | | File Hash | | Media Type | | Salt | |
| +----------------------+ |             | +-----------+ +------------+ +------+ |
+--------------------------+             +---------------------------------------+
```

| **Deklarativ** | **Fungibel** | **Strukturert** | **Bilag** | **Bilag

| --------------------- | -------------- | ------------------------------------ | ----------------------------- | ---------------------------- |

| Ingen | 64-biters heltall med eller uten fortegn | Alle strenge datatyper | Alle filer | Alle filer

| Info type** | Ingen | Signerte eller usignerte | Strenge typer | MIME-type | MIME-type

| Pedersen-forpliktelse | Hashing med blinding | Hashet fil-ID

størrelsesbegrensninger** | N/A | 256 byte | Opptil 64 KB | Opptil ~500 Gb | | 256 byte

### Innganger

Inngangene til en *kontraktsoperasjon* refererer til de *oppdragene* som blir brukt i denne nye operasjonen. En Inngang indikerer :


- prevOpId` : identifikatoren (`OpId`) for den forrige operasjonen der *Assignment* befant seg;
- assignmentType` : typen *Assignment* (for eksempel `assetOwner` for et token) ;
- `Index`: indeksen til *Assignment* i listen som er knyttet til forrige `OpId`, bestemt etter en leksikografisk sortering av de skjulte selene.

Inputs vises aldri i Genesis, siden det ikke finnes noen tidligere Assignments. De vises heller ikke i State Extensions (fordi State Extensions ikke lukker segl, men omdefinerer nye segl basert på Valencies).

Når vi har Owned States av typen `Fungible`, kontrollerer valideringslogikken (via AluVM-skriptet som følger med i skjemaet) at summene er konsistente: summen av innkommende tokens (*Inputs*) må være lik summen av utgående tokens (i de nye *Assignments*).

### Metadata

Feltet **Metadata** kan være på opptil 64 KiB og brukes til å inkludere midlertidige data som er nyttige for validering, men som ikke er integrert i kontraktens permanente tilstand. For eksempel kan mellomliggende beregningsvariabler for komplekse skript lagres her. Denne plassen er ikke ment å lagres i den globale historikken, og derfor er den ikke omfattet av Owned States eller Global State.

### Valenser

Valencies** er en original RGB-protokollmekanisme. De finnes i Genesis, State Transitions eller State Extensions. De representerer numeriske rettigheter som kan aktiveres av en tilstandsutvidelse (via *Redeems*), og deretter fullføres av en påfølgende overgang. Hver Valency identifiseres av en `ValencyType` (16 bits). Semantikken (gjenutstedelsesrett, tokenbytte, brennrett osv.) er definert i skjemaet.

Konkret kan vi tenke oss en Genesis som definerer en "rett til å utstede på nytt"-valens. En tilstandsutvidelse vil konsumere den (*Redeem*) hvis visse betingelser er oppfylt, for å introdusere en ny mengde tokens. Deretter kan en tilstandsovergang som utgår fra innehaveren av seglet som er opprettet på denne måten, overføre disse nye pollettene.

### Innløser

Redeems er valensens ekvivalent til innganger for Assignments. De vises bare i tilstandsutvidelser, ettersom det er her en tidligere definert valens aktiveres. En Redeem består av to felt:


- `PrevOpId` : `OpId` for operasjonen der Valency ble spesifisert;
- `ValencyType`: den typen Valency du ønsker å aktivere (hver `ValencyType` kan bare brukes én gang av State Extension).

Eksempel: En Redeem kan tilsvare en CoinSwap-kjøring, avhengig av hva som ble kodet i Valency.

### RGB-statuskarakteristikker

Vi skal nå ta en titt på flere grunnleggende tilstandskarakteristikker i RGB. Spesielt skal vi se på :


- **Strict Type System**, som pålegger en presis og typet organisering av data;
- Viktigheten av å skille mellom **validering** og **eierskap** ;
- Systemet **konsensus-evolusjon** i RGB, som inkluderer begrepene *fast-forward* og *push-back*.

Husk som alltid at alt som har med kontraktsstatus å gjøre, valideres på klientsiden i henhold til konsensusregler som er fastsatt i protokollen, og hvis ultimate kryptografiske referanse er forankret i Bitcoin-transaksjoner.

#### Strengt typesystem

RGB bruker et *Strict Type System* og en deterministisk serialiseringsmodus (*Strict Encoding*). Denne organiseringen er utformet for å garantere perfekt reproduserbarhet og presisjon i definisjon, håndtering og validering av kontraktsdata.

I mange programmeringsmiljøer (JSON, YAML ...) kan datastrukturen være fleksibel, til og med for permissiv. I RGB, derimot, er strukturen og typene for hvert felt definert med eksplisitte begrensninger. For eksempel :


- Hver variabel har en bestemt type (for eksempel et 8-bits usignert heltall `u8`, eller et 16-bits signert heltall, osv;)
- Typer kan være sammensatte (nestede typer). Dette betyr at du kan definere en type basert på andre typer (f.eks. en aggregert type som inneholder et `u8`-felt, et `bool`-felt osv;)
- Samlinger kan også spesifiseres: lister (*list*), sett (*set*) eller ordbøker (*map*), med en deterministisk rekkefølge;
- Hvert felt er avgrenset (*nedre grense* / *øvre grense*). Vi setter også grenser for antall elementer i samlinger (containment);
- Data er bytejustert, og serialiseringen er strengt definert og entydig.

Takket være denne strenge kodingsprotokollen :


- Rekkefølgen på feltene er alltid den samme, uavhengig av hvilken implementering eller hvilket programmeringsspråk som brukes;
- Hashene som beregnes på samme datasett, er derfor reproduserbare og identiske (strengt deterministiske *commitments*);
- Grenser forhindrer ukontrollert vekst i datastørrelsen (f.eks. for mange felt);
- Denne formen for koding forenkler kryptografisk verifisering, ettersom hver deltaker vet nøyaktig hvordan dataene skal serialiseres og hashes.

I praksis kompileres strukturen (*Schema*) og den resulterende koden (*Grensesnitt* og tilhørende logikk). Et beskrivende språk brukes til å definere kontrakten (typer, felt, regler) og generere et strengt binært format. Når det er kompilert, er resultatet :


- En *Memory Layout* for hvert felt;
- Semantiske identifikatorer (som angir om endring av et variabelnavn har innvirkning på logikken, selv om minnestrukturen forblir den samme).

Det strenge typesystemet muliggjør også nøyaktig overvåking av endringer: Enhver endring i strukturen (til og med en endring av feltnavn) kan oppdages og føre til en endring i det samlede fotavtrykket.

Til slutt produserer hver kompilering et fingeravtrykk, en kryptografisk identifikator som bekrefter den nøyaktige versjonen av koden (data, regler, validering). For eksempel kan en identifikator av formen :

```txt
BEiLYE-am9WhTW1-oK8cpvw4-FEMtzMrf-mKocuGZn-qWK6YF#ginger-parking-nirvana
```

Dette gjør det mulig å håndtere konsensus eller implementeringsoppdateringer, samtidig som man sikrer detaljert sporbarhet av versjonene som brukes i nettverket.

For å forhindre at tilstanden til en RGB-kontrakt blir for tungvint å validere på klientsiden, er det innført en konsensusregel som pålegger en maksimal størrelse på `2^16` byte (64 Kio) for alle data som er involvert i valideringsberegninger. Dette gjelder for hver variabel eller struktur: ikke mer enn 65536 byte, eller tilsvarende i tall (32768 16-biters heltall osv.). Dette gjelder også for samlinger (lister, sett, kart), som ikke kan overstige `2^16` elementer.

Denne grensen garanterer :


- Kontrollerer den maksimale størrelsen på data som skal manipuleres under en tilstandsovergang;
- Kompatibilitet med den virtuelle maskinen (*AluVM*) som brukes til å kjøre valideringsskript.

#### Validering != Eierskapsparadigmet

En av RGBs viktigste innovasjoner er det strenge skillet mellom to konsepter:


- Validering**: kontroll av at en tilstandsovergang overholder kontraktens regler (forretningslogikk, historikk osv.);
- **Eierskapet** (eierskap eller kontroll): det faktum at man eier Bitcoin UTXO som gjør det mulig å bruke (eller stenge) engangsforseglingen, og dermed kan tilstandsovergangen finne sted.

Validering** finner sted på nivå med RGB-programvarestakken (biblioteker, *commitments*-protokoll osv.). Dens rolle er å sikre at kontraktens interne regler (beløp, tillatelser osv.) overholdes. Observatører eller andre deltakere kan også validere datahistorikken.

Eierskap**, derimot, er helt avhengig av Bitcoins sikkerhet. Å eie den private nøkkelen til en UTXO betyr å kontrollere muligheten til å starte en ny overgang (lukke Single-use Seal). Så selv om noen kan se eller validere dataene, kan de ikke endre tilstanden hvis de ikke eier den aktuelle UTXO-en.

![RGB-Bitcoin](assets/fr/069.webp)

Denne tilnærmingen begrenser de klassiske sårbarhetene som oppstår i mer komplekse blokkjeder (der all koden i en smartkontrakt er offentlig og kan endres av hvem som helst, noe som noen ganger har ført til hacking). På RGB kan en angriper ikke bare interagere med tilstanden i kjeden, ettersom retten til å handle på tilstanden (*eierskap*) er beskyttet av Bitcoin-laget.

Dessuten gjør denne frikoblingen at RGB kan integreres naturlig med Lightning Network. Lightning-kanaler kan brukes til å engasjere og flytte RGB-ressurser uten å engasjere *forpliktelser* i kjeden hver gang. Vi skal se nærmere på denne integreringen av RGB i Lightning i senere kapitler av kurset.

#### Konsensus om utviklingen i RGB

I tillegg til semantisk kodeversjonering inneholder RGB et system for utvikling eller oppdatering av en kontrakts konsensusregler over tid. Det finnes to hovedformer for evolusjon:


- Spol frem**
- Push-back** (på fransk)

En fast-forward oppstår når en tidligere ugyldig regel blir gyldig. For eksempel, hvis kontrakten utvikler seg til å tillate en ny type `AssignmentType` eller et nytt felt :


- Dette kan ikke sammenlignes med en klassisk blockchain hardfork, ettersom RGB fungerer i validering på klientsiden og ikke påvirker den generelle kompatibiliteten til blockchain ;
- I praksis angis denne typen endringer ved hjelp av feltet `Ffv` (*fast-forward version*) i kontraktsoperasjonen;
- Nåværende innehavere blir ikke skadelidende: deres status forblir gyldig;
- Nye mottakere (eller nye brukere) må derimot oppdatere programvaren (lommeboken) slik at den kjenner igjen de nye reglene.

En push-back betyr at en tidligere gyldig regel blir ugyldig. Det er derfor en "herding" av reglene, men strengt tatt ikke en softfork:


- Eksisterende innehavere kan bli påvirket (de kan få eiendeler som blir foreldet eller ugyldige i den nye versjonen);
- Vi kan tenke oss at vi faktisk lager en ny protokoll: Den som tar i bruk den nye regelen, går bort fra den gamle;
- Utstederen kan bestemme seg for å utstede aktiva på nytt i den nye protokollen, noe som tvinger brukerne til å ha to separate lommebøker (én for den gamle og én for den nye protokollen) hvis de ønsker å administrere begge versjonene.

I dette kapittelet om RGB-kontraktsoperasjoner har vi utforsket de grunnleggende prinsippene som ligger til grunn for denne protokollen. Som du sikkert har lagt merke til, krever RGB-protokollens iboende kompleksitet bruk av mange tekniske termer. I neste kapittel vil jeg derfor gi deg en ordliste som oppsummerer alle konseptene som er dekket i denne første teoretiske delen, med definisjoner av alle tekniske termer knyttet til RGB. I neste avsnitt tar vi en praktisk titt på definisjonen og implementeringen av RGB-kontrakter.

## RGB-ordliste

<chapterId>545e16a4-3cca-44a3-9fd5-dbc5868abf97</chapterId>

Denne korte ordlisten med viktige tekniske termer som brukes i RGB-verdenen (i alfabetisk rekkefølge), er nyttig hvis du har behov for å komme tilbake til den. Dette kapittelet er ikke nødvendig hvis du allerede har forstått alt vi har gjennomgått i den første delen.

#### AluVM

Forkortelsen AluVM står for "_Algorithmic logic unit Virtual Machine_", en registerbasert virtuell maskin utviklet for validering av smartkontrakter og distribuert databehandling. Den brukes (men er ikke utelukkende reservert) for validering av RGB-kontrakter. Skript eller operasjoner som inngår i en RGB-kontrakt kan dermed utføres i AluVM-miljøet.

For ytterligere informasjon: [AluVMs offisielle nettside](https://www.aluvm.org/)

#### Anker

Et anker representerer et sett med data på klientsiden som brukes til å bevise at en unik _commitment_ er inkludert i en transaksjon. I RGB-protokollen består et anker av følgende elementer:


- Bitcoin-transaksjonsidentifikatoren (TXID) for **vitnetransaksjonen** ;
- **Multi Protocol Commitment (MPC)** ;
- Den **Deterministiske Bitcoin-forpliktelsen (DBC)**;
- **Ekstra transaksjonsbevis (ETP)** hvis forpliktelsesmekanismen **Tapret** brukes (se avsnittet om denne modellen).

Et anker tjener derfor til å etablere en verifiserbar kobling mellom en spesifikk Bitcoin-transaksjon og private data som er validert av RGB-protokollen. Det garanterer at disse dataene faktisk er inkludert i blokkjeden, uten at det nøyaktige innholdet er offentlig eksponert.

#### Oppdrag

I RGBs logikk tilsvarer et Assignment en transaksjonsutgang som endrer, oppdaterer eller oppretter visse egenskaper i en kontrakts tilstand. Et Assignment består av to elementer:


- A **Seal Definition** (referanse til en spesifikk UTXO) ;
- En **Owned State** (data som beskriver staten som er knyttet til denne nye eieren).

En tildeling indikerer derfor at en del av tilstanden (for eksempel en eiendel) nå er allokert til en bestemt innehaver, identifisert via et engangsforsegling knyttet til en UTXO.

#### Forretningslogikk

Forretningslogikken samler alle regler og interne operasjoner i en kontrakt, beskrevet av dens **skjema** (dvs. selve kontraktens struktur). Den dikterer hvordan kontraktens tilstand kan utvikle seg, og under hvilke betingelser.

#### Validering på klientsiden

Validering på klientsiden refererer til prosessen der hver part (klient) verifiserer et sett med data som utveksles privat, i henhold til reglene i en protokoll. I RGBs tilfelle er disse utvekslede dataene gruppert sammen i det som kalles **sendinger**. I motsetning til Bitcoin-protokollen, som krever at alle transaksjoner publiseres i kjeden, tillater RGB at kun _commitments_ (forankret i Bitcoin) lagres offentlig, mens den essensielle kontraktsinformasjonen (overganger, attesteringer, bevis) forblir utenfor kjeden, og kun deles mellom de berørte brukerne.

#### Engasjement

En forpliktelse (i kryptografisk forstand) er et matematisk objekt, betegnet `C`, som er avledet deterministisk fra en operasjon på strukturerte data `m` (meldingen) og en tilfeldig verdi `r`. Vi skriver :

$$
C = \text{commit}(m, r)
$$

Denne mekanismen består av to hovedoperasjoner:


- Commit**: En kryptografisk funksjon brukes på en melding `m` og et tilfeldig tall `r` for å produsere `C` ;
- Verify**: Vi bruker `C`, `m`-meldingen og `r`-verdien til å kontrollere at denne forpliktelsen er korrekt. Funksjonen returnerer `True` eller `False`.

En forpliktelse må respektere to egenskaper:


- Binding**: Det må være umulig å finne to forskjellige meldinger som produserer samme `C` :

$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$

Som for eksempel :

$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$


- Skjult**: Kunnskap om `C` må ikke avsløre innholdet i `m`.

I RGB-protokollen er en forpliktelse inkludert i en Bitcoin-transaksjon for å bevise eksistensen av en viss informasjon på et gitt tidspunkt, uten å avsløre selve informasjonen.

#### Forsendelse

En **Sending** grupperer dataene som utveksles mellom partene, med forbehold om validering på klientsiden i RGB. Det finnes to hovedkategorier av forsendelser:


- Contract Consignment**: leveres av *utsteder* (kontraktsutsteder), og inneholder initialiseringsinformasjon som Schema, Genesis, grensesnitt og grensesnittimplementering.
- Transfer Consignment**: leveres av den betalende parten (*betaler*). Den inneholder hele historikken for tilstandsoverganger som fører frem til den endelige forsendelsen (dvs. den endelige tilstanden som betaleren mottar).

Disse forsendelsene registreres ikke offentlig i blokkjeden, men utveksles direkte mellom de berørte partene via den kommunikasjonskanalen de selv velger.

#### Kontrakt

En kontrakt er et sett med rettigheter som utøves digitalt mellom flere aktører via RGB-protokollen. Den har en aktiv tilstand og en forretningslogikk, definert av et skjema, som spesifiserer hvilke operasjoner som er autoriserte (overføringer, utvidelser osv.). Kontraktens tilstand og dens gyldighetsregler er uttrykt i skjemaet. Kontrakten utvikler seg til enhver tid bare i samsvar med det som er tillatt i henhold til dette skjemaet og valideringsskript (kjørt for eksempel i AluVM).

#### Kontraktsdrift

En kontraktsoperasjon er en oppdatering av kontraktsstatus som utføres i henhold til skjemaregler. Følgende operasjoner finnes i RGB:


- Tilstandsovergang** ;
- Genesis** ;
- State Extension**.

Hver operasjon endrer tilstanden ved å legge til eller erstatte bestemte data (Global State, Owned State...).

#### Kontraktsdeltaker

En kontraktsdeltaker er en aktør som tar del i operasjoner knyttet til kontrakten. I RGB skilles det mellom :


- Utstederen av kontrakten, som skaper Genesis (kontraktens opprinnelse);
- Kontraktspartene, dvs. innehaverne av rettigheter til kontraktstilstanden;
- Offentlige parter, som kan bygge statlige utvidelser hvis kontrakten tilbyr Valencies som er tilgjengelig for allmennheten.

#### Kontraktsrettigheter

Kontraktsrettigheter refererer til de ulike rettighetene som kan utøves av de involverte i en RGB-kontrakt. De faller inn i flere kategorier:


- Eierskapsrettigheter**, knyttet til eierskapet til en bestemt UTXO (via en _Seal Definition_);
- Utøvende rettigheter**, dvs. muligheten til å bygge en eller flere overganger (State Transitions) i samsvar med Schema ;
- Offentlige rettigheter**, når skjemaet autoriserer visse offentlige bruksområder, for eksempel opprettelse av en State Extension via innløsning av en Valency.

#### Kontraktsstat

Kontraktsstatus tilsvarer den nåværende tilstanden til en kontrakt på et gitt tidspunkt. Den kan bestå av både offentlige og private data, som gjenspeiler kontraktens tilstand. RGB skiller mellom :


- **Global State**, som omfatter kontraktens offentlige egenskaper (satt opp i Genesis eller lagt til via autoriserte oppdateringer);
- Owned States**, som tilhører bestemte eiere, identifisert ved UTXO-en.

#### Deterministisk Bitcoin-forpliktelse - DBC

Deterministic Bitcoin Commitment (DBC) er et sett med regler som brukes til å påviselig og unikt registrere en _commitment_ i en Bitcoin-transaksjon. I RGB-protokollen finnes det to hovedformer av DBC:


- Opret**
- Tapret**

Disse mekanismene definerer nøyaktig hvordan _forpliktelsen_ er kodet i utdataene eller strukturen til en Bitcoin-transaksjon, for å sikre at denne forpliktelsen er deterministisk sporbar og verifiserbar.

#### Directed Acyclic Graph - DAG

En DAG (eller *Acyclic Guided Graph*) er en syklusfri graf, noe som muliggjør topologisk planlegging. Blokkjeder, som _shards_ av RGB-kontrakter, kan representeres av DAG-er.

For ytterligere informasjon: [Directed Acyclic Graph] (https://en.wikipedia.org/wiki/Directed_acyclic_graph)

#### Gravering

Gravering er en valgfri datastreng som etterfølgende eiere av en kontrakt kan legge inn i kontraktshistorikken. Denne funksjonen finnes for eksempel i **RGB21**-grensesnittet, og gjør det mulig å legge til minneverdig eller beskrivende informasjon i kontraktshistorikken.

#### Ekstra transaksjonsbevis - ETP

ETP (*Extra Transaction Proof*) er den delen av Anchor som inneholder tilleggsdataene som kreves for å validere en **Tapret** *commitment* (i forbindelse med _taproot_). Det inkluderer blant annet taproot-skriptets interne offentlige nøkkel (_internal PubKey_) og informasjon som er spesifikk for _Script Path Spend_.

#### Genesis

Genesis refererer til datasettet, styrt av et skjema, som utgjør den opprinnelige tilstanden til enhver kontrakt i RGB. Det kan sammenlignes med Bitcoins _Genesis Block_-konsept, eller med Coinbase-transaksjonskonseptet, men her på _klientsiden_ og RGB-token-nivå.

#### Global stat

Den globale tilstanden er settet med offentlige egenskaper som inngår i kontraktstilstanden. Den er definert ved Genesis og kan, avhengig av kontraktsreglene, oppdateres ved autoriserte overganger. I motsetning til Owned States tilhører ikke Global State en bestemt enhet; den er nærmere et offentlig register i kontrakten.

#### Grensesnitt

Grensesnittet er det settet med instruksjoner som brukes til å dekode binærdataene som er kompilert i et skjema eller i kontraktsoperasjoner og deres tilstander, for å gjøre dem lesbare for brukeren eller lommeboken hans. Det fungerer som et tolkningslag.

#### Implementering av grensesnitt

Grensesnittimplementering er settet med deklarasjoner som knytter et **grensesnitt** til et **skjema**. Den muliggjør den semantiske oversettelsen som utføres av selve grensesnittet, slik at rådataene i en kontrakt kan forstås av brukeren eller den involverte programvaren (lommebøkene).

#### Faktura

En faktura har form av en URL kodet i [base58] (https://en.wikipedia.org/wiki/Binary-to-text_encoding#Base58), som inneholder dataene som er nødvendige for å opprette en **State Transition** (av betaleren). Med andre ord er det en faktura som gjør det mulig for motparten (*betaleren*) å opprette den tilsvarende overgangen for å overføre eiendelen eller oppdatere kontraktens tilstand.

#### Lightning Network

Lightning Network er et desentralisert nettverk av betalingskanaler (eller _statskanaler_) på Bitcoin, som består av 2/2 lommebøker med flere signaturer. Det muliggjør raske, rimelige _off-chain_-transaksjoner, samtidig som det baserer seg på Bitcoins lag 1 for voldgift (eller stenging) når det er nødvendig.

Hvis du vil ha mer informasjon om hvordan Lightning fungerer, anbefaler jeg at du tar dette andre kurset:

https://planb.network/courses/lnp201
#### Multiprotokollforpliktelse - MPC

Multi Protocol Commitment (MPC) refererer til Merkle-tre-strukturen som brukes i RGB for å inkludere flere **Transition Bundles** fra ulike kontrakter i en enkelt Bitcoin-transaksjon. Tanken er å gruppere flere forpliktelser (som potensielt tilsvarer ulike kontrakter eller ulike aktiva) i ett enkelt ankerpunkt for å optimalisere opptaket av blokkplass.

#### Eid stat

En Owned State er den delen av en Contract State som er omsluttet av en Assignment og knyttet til en bestemt innehaver (via et Single-use Seal som peker til en UTXO). Dette representerer for eksempel en digital eiendel eller en spesifikk kontraktsmessig rettighet som er tildelt denne personen.

#### Eierskap

Eierskap refererer til muligheten til å kontrollere og bruke en UTXO som er referert til av en forseglingsdefinisjon. Når en Owned State er knyttet til en UTXO, har eieren av denne UTXO-en potensielt rett til å overføre eller utvikle den tilknyttede staten, i henhold til kontraktens regler.

#### Delvis signert Bitcoin-transaksjon - PSBT

En PSBT (_Partially Signed Bitcoin Transaction_) er en Bitcoin-transaksjon som ennå ikke er fullstendig signert. Den kan deles mellom flere enheter, som hver kan legge til eller verifisere visse elementer (signaturer, skript ...), til transaksjonen anses å være klar for distribusjon i kjeden.

For ytterligere informasjon: [BIP-0174](https://github.com/bitcoin/bips/blob/master/bip-0174.mediawiki)

#### Pedersens engasjement

En Pedersen-forpliktelse er en type kryptografisk forpliktelse som har den egenskapen at den er **homorfisk** med hensyn til addisjonsoperasjonen. Dette betyr at det er mulig å validere summen av to forpliktelser uten å avsløre de individuelle verdiene.

Formelt sett, hvis :

$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$

da :

$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$

Denne egenskapen er for eksempel nyttig for å skjule hvor mange tokens som er utvekslet, samtidig som det er mulig å verifisere totalsummen.

Ytterligere informasjon: [Pedersen commitment](https://link.springer.com/chapter/10.1007/3-540-46766-1_9)

#### Innløs

I en tilstandsutvidelse refererer en Redeem til handlingen med å gjenvinne (eller utnytte) en tidligere erklært **Valency**. Ettersom en valens er en offentlig rettighet, gjør Redeem det mulig for en autorisert deltaker å gjøre krav på en spesifikk kontraktstilstandsutvidelse.

#### Skjema

Et skjema i RGB er et deklarativt stykke kode som beskriver settet med variabler, regler og forretningslogikk (*Forretningslogikk*) som styrer driften av en kontrakt. Skjemaet definerer tilstandsstrukturen, hvilke typer overganger som er tillatt, og valideringsbetingelsene.

#### Definisjon av segl

Seal Definition er den delen av en Assignment som knytter _forpliktelsen_ til en UTXO som eies av den nye innehaveren. Med andre ord angir den hvor betingelsen er lokalisert (i hvilken UTXO), og fastslår eierskapet til en eiendel eller rettighet.

#### Splint

En Shard representerer en gren i DAG for tilstandsovergangshistorikken til en RGB-kontrakt. Med andre ord er det en sammenhengende delmengde av kontraktens samlede historikk, som for eksempel tilsvarer sekvensen av overganger som kreves for å bevise gyldigheten til en gitt eiendel siden _Genesis_.

#### Tetning for engangsbruk

Et engangsforsegling er et kryptografisk løfte om forpliktelse til et ennå ukjent budskap, som bare vil bli avslørt én gang i fremtiden og som må være kjent av alle medlemmer av et bestemt publikum. Målet er å forhindre at det opprettes flere konkurrerende forpliktelser for det samme seglet.

#### Stash

Stash er det settet med data på klientsiden som en bruker lagrer for en eller flere RGB-kontrakter, for valideringsformål (*Validering på klientsiden*). Dette inkluderer overgangshistorikk, forsendelser, gyldighetsbevis osv. Hver innehaver beholder bare de delene av historikken de trenger (*shards*).

#### State Extension

En tilstandsutvidelse er en kontraktsoperasjon som brukes til å utløse tilstandsoppdateringer ved å innløse tidligere erklærte **Valencies**. For å være effektiv må en tilstandsutvidelse avsluttes med en tilstandsovergang (som oppdaterer kontraktens endelige tilstand).

#### Overgang mellom tilstander

Statusovergang er en operasjon som endrer statusen til en RGB-kontrakt til en ny status. Den kan endre data om global tilstand og/eller egen tilstand. I praksis blir hver overgang verifisert av Schema-regler og forankret i Bitcoin-blokkjeden via en _commitment_.

#### Taproot

Refererer til Bitcoins Segwit v1-transaksjonsformat, introdusert av [BIP341] (https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki) og [BIP342] (https://github.com/bitcoin/bips/blob/master/bip-0342.mediawiki). Taproot forbedrer konfidensialiteten og fleksibiliteten til skript, særlig ved å gjøre transaksjoner mer kompakte og vanskeligere å skille fra hverandre.

#### Terminal Consignment - Sluttpunkt for sending

Terminalforsendelsen (eller _Consignment Endpoint_) er en *overførselsforsendelse* som inneholder kontraktens endelige tilstand, inkludert tilstandsovergangen som er opprettet fra mottakerens faktura (*betalingsmottaker*). Det er derfor sluttpunktet for en overføring, med de nødvendige dataene for å bevise at eierskap eller tilstand er overført.

#### Overgangspakke

En Transition Bundle er et sett med RGB State Transitions (som tilhører samme kontrakt) som alle er involvert i den samme ***vitnetransaksjonen*** Bitcoin. Dette gjør det mulig å samle flere oppdateringer eller overføringer i ett enkelt anker i kjeden.

#### UTXO

En Bitcoin UTXO (*Unspent Transaction Output*) er definert av hashen til en transaksjon og utgangsindeksen (*vout*). Det kalles også noen ganger et _outpoint_. I RGB-protokollen muliggjør en referanse til en UTXO (via en **Seal Definition**) plasseringen av **Owned State**, dvs. eiendommen som holdes på blokkjeden.

#### Valens

En Valency er en offentlig rettighet som ikke krever statlig lagring som sådan, men som kan innløses via en **State Extension**. Det er derfor en form for mulighet som er åpen for alle (eller visse aktører), deklarert i kontraktslogikken, for å gjennomføre en bestemt utvidelse på et senere tidspunkt.

#### Vitnetransaksjon

Vitnetransaksjonen er Bitcoin-transaksjonen som lukker engangsforseglingen rundt en melding som inneholder en Multi Protocol Commitment (MPC). Denne transaksjonen bruker en UTXO eller oppretter en, for å forsegle forpliktelsen knyttet til RGB-protokollen. Den fungerer som et bevis i kjeden på at tilstanden har blitt satt på et bestemt tidspunkt.

# Programmering på RGB

<partId>148a7436-d079-56d9-be08-aaa4c14c6b3a</partId>

## Implementering av RGB-kontrakter

<chapterId>8333ea5f-51c7-5dd5-b1d7-47d491e58e51</chapterId>

![video](https://youtu.be/Uo1UoxiImsI)

I dette kapittelet skal vi se nærmere på hvordan en RGB-kontrakt defineres og implementeres. Vi skal se hva komponentene i en RGB-kontrakt er, hvilke roller de har, og hvordan de er bygget opp.

### Komponentene i en RGB-kontrakt

Så langt har vi allerede diskutert **Genesis**, som representerer utgangspunktet for en kontrakt, og vi har sett hvordan den passer inn i logikken til en *Contract Operation* og protokollens tilstand. Den fullstendige definisjonen av en RGB-kontrakt er imidlertid ikke begrenset til Genesis alene: Den omfatter tre komplementære komponenter som til sammen utgjør kjernen i implementeringen.

Den første komponenten kalles **Schema**. Dette er en fil som beskriver den grunnleggende strukturen og forretningslogikken (*forretningslogikken*) i kontrakten. Den spesifiserer datatypene som brukes, valideringsreglene, de tillatte operasjonene (f.eks. utstedelse av første token, overføringer, spesielle betingelser osv.) - kort sagt det generelle rammeverket som dikterer hvordan kontrakten fungerer.

Den andre komponenten er **Grensesnittet**. Den fokuserer på hvordan brukerne (og dermed porteføljeprogramvaren) skal samhandle med kontrakten. Den beskriver semantikken, dvs. den lesbare representasjonen av de ulike feltene og handlingene. Mens skjemaet definerer hvordan kontrakten fungerer rent teknisk, definerer grensesnittet hvordan disse funksjonene skal presenteres og eksponeres: metodenavn, datavisning osv.

Den tredje komponenten er **Grensesnittimplementeringen**, som utfyller de to foregående ved å fungere som en slags bro mellom skjemaet og grensesnittet. Med andre ord knytter den semantikken som uttrykkes i grensesnittet, til de underliggende reglene som er definert i skjemaet. Det er denne implementasjonen som for eksempel håndterer konverteringen mellom en parameter som er lagt inn i lommeboken, og den binære strukturen som protokollen pålegger, eller kompileringen av valideringsregler i maskinspråk.

Denne modulariteten er et interessant trekk ved RGB, ettersom den gjør det mulig for ulike grupper av utviklere å jobbe separat med disse aspektene (*Schema*, *Grensesnitt*, *Implementering*), så lenge de følger protokollens konsensusregler.

For å oppsummere består hver kontrakt av :


- Genesis**, som er kontraktens opprinnelige tilstand (og kan sammenlignes med en spesiell transaksjon som definerer det første eierskapet til en eiendel, en rettighet eller andre parameteriserbare data);
- Schema**, som beskriver kontraktens forretningslogikk (datatyper, valideringsregler osv.);
- Interface**, som gir et semantisk lag for både lommebøker og menneskelige brukere, og som tydeliggjør lesing og gjennomføring av transaksjoner;
- Implementation**-grensesnittet, som bygger bro mellom forretningslogikk og presentasjon, for å sikre at kontraktsdefinisjonen stemmer overens med brukeropplevelsen.

![RGB-Bitcoin](assets/fr/070.webp)

Det er viktig å merke seg at for at en lommebok skal kunne administrere en RGB-eiendel (det være seg en fungibel token eller en rettighet av noe slag), må den ha alle disse elementene samlet: *Schema*, *Grensesnitt*, *Grensesnittsimplementering* og *Genesis*. Dette overføres via en ***kontraktsforsendelse***, dvs. en datapakke som inneholder alt som trengs for å validere kontrakten på klientsiden.

For å klargjøre disse begrepene, følger her en oppsummeringstabell som sammenligner komponentene i en RGB-kontrakt med begreper som allerede er kjent enten i objektorientert programmering (OOP) eller i Ethereums økosystem:

| RGB-kontraktskomponent | Betydning | OOP-ekvivalent | Ethereum-ekvivalent | OOP-ekvivalent

| ---------------------------- | --------------------------------------- | -------------------------------------------------- | ---------------------------------- |

| Klassekonstruktør | Kontraktskonstruktør | Kontraktens opprinnelige tilstand

| Klasse | Kontraktens forretningslogikk

| Kontraktsemantikk | Grensesnitt (Java) / egenskap (Rust) / protokoll (Swift) | ERC-standard | ERC

| Application Binary Interface (ABI) | Impl (Rust) / Implements (Java) | Mapping av semantikk og logikk

Den venstre kolonnen viser elementene som er spesifikke for RGB-protokollen. Den midterste kolonnen viser den konkrete funksjonen til hver komponent. I kolonnen "OOP-ekvivalent" finner vi den tilsvarende termen i objektorientert programmering:


- **Genesis** spiller en rolle som ligner på rollen til en *Class-konstruktør*: det er her kontraktens tilstand initialiseres;
- Et **Schema** er beskrivelsen av en klasse, det vil si definisjonen av dens egenskaper, metoder og underliggende logikk;
- **Interface** tilsvarer *interfaces* (Java), *traits* (Rust) eller *protocols* (Swift): Dette er de offentlige definisjonene av funksjoner, hendelser, felt ... ;
- Grensesnittimplementering** tilsvarer *Impl* i Rust eller *Implements* i Java, der vi spesifiserer hvordan koden faktisk skal utføre metodene som er annonsert i grensesnittet.

I Ethereum-sammenheng er Genesis nærmere *kontraktskonstruktøren*, Schema er kontraktsdefinisjonen, Interface er en standard som ERC-20 eller ERC-721, og Interface Implementation er ABI (*Application Binary Interface*), som spesifiserer formatet for interaksjon med kontrakten.

Fordelen med RGBs modularitet ligger også i det faktum at ulike interessenter kan skrive for eksempel sin egen grensesnittimplementering, så lenge de respekterer logikken i *Schema* og semantikken i *Grensesnitt*. Dermed kan en utsteder utvikle en ny, mer brukervennlig front-end (grensesnitt) uten å endre logikken i kontrakten, eller omvendt, man kan utvide skjemaet for å legge til funksjonalitet, og levere en ny versjon av den tilpassede grensesnittimplementeringen, mens de gamle implementeringene fortsatt vil være gyldige for grunnleggende funksjonalitet.

Når vi kompilerer en ny kontrakt, genererer vi en Genesis (det første trinnet i utstedelsen eller distribusjonen av eiendelen), samt dens komponenter (skjema, grensesnitt, grensesnittimplementering). Etter dette er kontrakten fullt operativ og kan spres til lommebøker og brukere. Denne metoden, der Genesis kombineres med disse tre komponentene, garanterer en høy grad av tilpasning (hver kontrakt kan ha sin egen logikk), desentralisering (alle kan bidra til en gitt komponent) og sikkerhet (validering forblir strengt definert av protokollen, uten å være avhengig av vilkårlig kode i kjeden, slik det ofte er tilfelle på andre blokkjeder).

Jeg vil nå se nærmere på hver av disse komponentene: **Skjemaet**, **Grensesnittet** og **Grensesnittimplementeringen**.

### Skjema

I forrige avsnitt så vi at en kontrakt i RGB-økosystemet består av flere elementer: Genesis, som etablerer den opprinnelige tilstanden, og flere andre komplementære komponenter. Formålet med skjemaet er å deklarativt beskrive all forretningslogikken i kontrakten, det vil si datastrukturen, typene som brukes, de tillatte operasjonene og betingelsene for disse. Det er derfor et svært viktig element for å gjøre en kontrakt operativ på klientsiden, siden hver deltaker (for eksempel en lommebok) må kontrollere at tilstandsovergangene den mottar, er i samsvar med logikken som er definert i skjemaet.

Et skjema kan sammenlignes med en "klasse" i objektorientert programmering (OOP). Generelt sett fungerer det som en modell som definerer komponentene i en kontrakt, for eksempel :


- De forskjellige typene Owned States og Assignments ;
- Valencies, dvs. spesielle rettigheter som kan utløses (*innløses*) for visse operasjoner;
- Globale tilstandsfelt, som beskriver globale, offentlige og delte egenskaper ved kontrakten;
- Genesis-strukturen (den aller første operasjonen som aktiverer kontrakten) ;
- Tillatte former for tilstandsoverganger og tilstandsutvidelser, og hvordan disse operasjonene kan endre ;
- Metadata knyttet til hver operasjon, for å lagre midlertidig informasjon eller tilleggsinformasjon;
- Regler som bestemmer hvordan interne kontraktsdata kan utvikle seg (for eksempel om et felt er muterbart eller kumulativt);
- Sekvenser av operasjoner som anses som gyldige: for eksempel en rekkefølge av overganger som skal respekteres, eller et sett med logiske betingelser som skal oppfylles.

![RGB-Bitcoin](assets/fr/071.webp)

Når *utstederen* av en eiendel på RGB publiserer en kontrakt, oppgir den Genesis og Schemaet som er knyttet til den. Brukere eller lommebøker som ønsker å samhandle med aktivumet, henter dette skjemaet for å forstå logikken bak kontrakten, og for å kunne verifisere senere at overgangene de skal delta i, er legitime.

Det første trinnet for alle som mottar informasjon om en RGB-eiendel (f.eks. en tokenoverføring), er å validere denne informasjonen mot skjemaet. Dette innebærer å bruke skjemakompileringen til å :


- Kontroller at Owned States, Assignments og andre elementer er riktig definert, og at de overholder de pålagte typene (det såkalte *strict type system*);
- Kontroller at overgangsreglene (valideringsskript) er oppfylt. Disse skriptene kan kjøres via AluVM, som er til stede på klientsiden og er ansvarlig for å validere konsistensen i forretningslogikken (overføringsbeløp, spesielle betingelser osv.).

I praksis er ikke Schema kjørbar kode, slik man kan se i blokkjeder som lagrer kode i kjeden (EVM på Ethereum). Tvert imot skiller RGB forretningslogikk (deklarativ) fra kjørbar kode på blokkjeden (som er begrenset til kryptografiske ankere). Dermed bestemmer skjemaet reglene, men anvendelsen av disse reglene skjer utenfor blokkjeden, hos hver deltaker, i henhold til prinsippet om validering på klientsiden.

Et skjema må kompileres før det kan brukes av RGB-applikasjoner. Denne kompileringen produserer en binær fil (f.eks. `.rgb`) eller en kryptert binær fil (`.rgba`). Når lommeboken importerer denne filen, vet den at :


- Hvordan hver datatype (heltall, strukturer, matriser ...) ser ut takket være det strenge typesystemet ;
- Hvordan Genesis bør struktureres (for å forstå initialisering av aktiva);
- De ulike typene operasjoner (State Transitions, State Extensions) og hvordan de kan modifisere tilstanden ;
- Skriptreglene (introdusert i skjemaet) som AluVM-motoren vil bruke for å kontrollere gyldigheten av operasjoner.

Som forklart i tidligere kapitler gir *strict type system* oss et stabilt, deterministisk kodingsformat: Alle variabler, enten det er Owned States, Global States eller Valencies, er beskrevet nøyaktig (størrelse, nedre og øvre grenser om nødvendig, signert eller usignert type osv.) Det er også mulig å definere nestede strukturer, for eksempel for å støtte komplekse brukstilfeller.

Eventuelt kan skjemaet referere til en rot `SchemaId`, noe som gjør det enklere å gjenbruke en eksisterende grunnstruktur (en mal). På denne måten kan du utvikle en kontrakt eller lage variasjoner (f.eks. en ny type token) fra en allerede utprøvd mal. Denne modulariteten gjør at man ikke trenger å gjenskape hele kontrakter, og bidrar til standardisering av beste praksis.

Et annet viktig poeng er at logikken for tilstandsutvikling (overføringer, oppdateringer osv.) er beskrevet i skjemaet i form av skript, regler og betingelser. Så hvis kontraktsdesigneren ønsker å autorisere en ny utstedelse eller pålegge en brennmekanisme (ødeleggelse av tokens), kan han spesifisere de tilsvarende skriptene for AluVM i valideringsdelen av skjemaet.

#### Forskjellen fra programmerbare blokkjeder i kjeden

I motsetning til systemer som Ethereum, der smartkontraktkoden (den kjørbare koden) er skrevet inn i selve blokkjeden, lagrer RGB kontrakten (dens logikk) utenfor kjeden, i form av et kompilert deklarativt dokument. Dette innebærer at :


- Det finnes ingen Turing-komplett VM som kjører i hver eneste node i Bitcoin-nettverket. Reglene i en RGB-kontrakt kjøres ikke på blokkjeden, men i hver bruker som ønsker å validere en tilstand;
- Kontraktsdata forurenser ikke blokkjeden: bare kryptografiske bevis (*forpliktelser*) er innebygd i Bitcoin-transaksjoner (via `Tapret` eller `Opret`);
- Schemaet kan oppdateres eller avvises (*fast-forward*, *push-back*, osv.), uten at det krever en gaffel i Bitcoin-blokkjeden. Lommebøker trenger bare å importere det nye skjemaet og tilpasse seg konsensusendringene.

#### Bruk av utsteder og brukere

Når en *utsteder* skaper en eiendel (for eksempel en ikke-inflasjonær fungibel token), forbereder den :


- Et skjema som beskriver reglene for utslipp, overføring osv;
- En Genesis tilpasset dette skjemaet (med totalt antall utstedte tokens, identiteten til den opprinnelige eieren, eventuelle spesielle valenser for gjenutstedelse osv.)

Deretter gjør den det kompilerte skjemaet (en `.rgb`-fil) tilgjengelig for brukerne, slik at alle som mottar en overføring av dette tokenet, kan kontrollere konsistensen av operasjonen lokalt. Uten dette skjemaet vil en bruker ikke kunne tolke statusdataene eller kontrollere at de er i samsvar med kontraktsreglene.

Så når en ny lommebok ønsker å støtte en eiendel, trenger den bare å integrere det relevante skjemaet. Denne mekanismen gjør det mulig å legge til kompatibilitet med nye RGB-aktivatyper uten å endre lommebokens programvarebase på en invasiv måte: Alt som kreves er å importere det binære skjemaet og forstå strukturen.

Skjemaet definerer forretningslogikken i RGB. Det viser evolusjonsreglene for en kontrakt, strukturen til dataene (Owned States, Global State, Valencies) og de tilknyttede valideringsskriptene (som kan kjøres av AluVM). Takket være dette deklarative dokumentet er definisjonen av en kontrakt (kompilert fil) klart adskilt fra den faktiske utførelsen av reglene (klientsiden). Denne frakoblingen gir RGB stor fleksibilitet, noe som muliggjør et bredt spekter av brukstilfeller (fungible tokens, NFT, mer sofistikerte kontrakter), samtidig som man unngår kompleksiteten og feilene som er typiske for programmerbare blokkjeder på kjeden.

#### Eksempel på skjema

La oss ta en titt på et konkret eksempel på et skjema for en RGB-kontrakt. Dette er et utdrag i Rust fra filen `nia.rs` (initialer for "*Non-Inflatable Assets*"), som definerer en modell for fungible tokens som ikke kan utstedes på nytt utover deres opprinnelige forsyning (en ikke-inflasjonær eiendel). Denne typen tokens kan i RGB-universet sees på som ekvivalenten til ERC20 i Ethereum, dvs. fungible tokens som respekterer visse grunnleggende regler (f.eks. for overføringer, initialisering av forsyninger osv.).

Før vi går inn i koden, er det verdt å minne om den generelle strukturen i et RGB-skjema. Det er en rekke erklæringer som rammer inn :


- En mulig `SchemaId` som angir bruk av et annet grunnskjema som mal;
- De **Globale statene** og **Eide stater** (med sine strenge typer) ;
- Eventuelle valenser** (hvis noen);
- **Operasjonene** (Genesis, tilstandsoverganger, tilstandsutvidelser) som kan referere til disse tilstandene og valensene;
- **Strict Type System** brukes til å beskrive og validere data;
- Valideringsskript** (kjørt via AluVM).

![RGB-Bitcoin](assets/fr/072.webp)

Koden nedenfor viser den fullstendige definisjonen av Rust Schema. Vi kommenterer den del for del, ved å følge annotasjonene (1) til (9) nedenfor:

```rust
// ===== PART 1: Function Header and SubSchema =====
fn nia_schema() -> SubSchema {
// definitions of libraries and variables
// ===== PART 2: General Properties (ffv, subset_of, type_system) =====
Schema {
ffv: zero!(),
subset_of: None,
type_system: types.type_system(),
// ===== PART 3: Global States =====
global_types: tiny_bmap! {
GS_NOMINAL => GlobalStateSchema::once(types.get("RGBContract.DivisibleAssetSpec")),
GS_DATA => GlobalStateSchema::once(types.get("RGBContract.ContractData")),
GS_TIMESTAMP => GlobalStateSchema::once(types.get("RGBContract.Timestamp")),
GS_ISSUED_SUPPLY => GlobalStateSchema::once(types.get("RGBContract.Amount")),
},
// ===== PART 4: Owned Types =====
owned_types: tiny_bmap! {
OS_ASSET => StateSchema::Fungible(FungibleType::Unsigned64Bit),
},
// ===== PART 5: Valencies =====
valency_types: none!(),
// ===== PART 6: Genesis: Initial Operations =====
genesis: GenesisSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: tiny_bmap! {
GS_NOMINAL => Occurrences::Once,
GS_DATA => Occurrences::Once,
GS_TIMESTAMP => Occurrences::Once,
GS_ISSUED_SUPPLY => Occurrences::Once,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
},
// ===== PART 7: Extensions =====
extensions: none!(),
// ===== PART 8: Transitions: TS_TRANSFER =====
transitions: tiny_bmap! {
TS_TRANSFER => TransitionSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: none!(),
inputs: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
}
},
// ===== PART 9: Script AluVM and Entry Points =====
script: Script::AluVM(AluScript {
libs: confined_bmap! { alu_id => alu_lib },
entry_points: confined_bmap! {
EntryPoint::ValidateGenesis => LibSite::with(FN_GENESIS_OFFSET, alu_id),
EntryPoint::ValidateTransition(TS_TRANSFER) => LibSite::with(FN_TRANSFER_OFFSET, alu_id),
},
}),
}
}
```


- (1) - Funksjonsoverskrift og underskjema**

Funksjonen `nia_schema()` returnerer et `SubSchema`, noe som indikerer at dette skjemaet delvis kan arve fra et mer generisk skjema. I RGB-økosystemet gjør denne fleksibiliteten det mulig å gjenbruke visse standardelementer i et hovedskjema, og deretter definere regler som er spesifikke for den aktuelle kontrakten. Her velger vi å ikke aktivere arv, siden `subset_of` vil være `None`.


- (2) - Generelle egenskaper: ffv, subset_of, type_system**

Egenskapen `ffv` tilsvarer den *hurtige* versjonen av kontrakten. En verdi på `zero!()` her indikerer at vi er på versjon 0 eller den første versjonen av dette skjemaet. Hvis du senere ønsker å legge til nye funksjoner (ny type operasjon osv.), kan du øke denne versjonen for å indikere en konsensusendring.

Egenskapen `subset_of: None`-egenskapen bekrefter fraværet av arv. Feltet `type_system` refererer til det strenge typesystemet som allerede er definert i biblioteket `types`. Denne linjen indikerer at alle data som brukes av kontrakten, bruker den strenge serialiseringsimplementeringen som tilbys av det aktuelle biblioteket.


- (3) - Globale stater

I blokken `global_types` deklarerer vi fire elementer. Vi bruker nøkkelen, for eksempel `GS_NOMINAL` eller `GS_ISSUED_SUPPLY`, til å referere til dem senere:


- `GS_NOMINAL` refererer til en `DivisibleAssetSpec`-type, som beskriver ulike felt i det opprettede tokenet (fullt navn, ticker, presisjon ...);
- `GS_DATA` representerer generelle data, for eksempel en ansvarsfraskrivelse, metadata eller annen tekst;
- `GS_TIMESTAMP` refererer til en utstedelsesdato;
- `GS_ISSUED_SUPPLY` angir det totale tilbudet, dvs. det maksimale antallet tokens som kan opprettes.

Nøkkelordet `once(...)` betyr at hvert av disse feltene bare kan vises én gang.


- (4) - Eide typer

I `owned_types` deklarerer vi `OS_ASSET`, som beskriver en fungibel tilstand. Vi bruker `StateSchema::Fungible(FungibleType::Unsigned64Bit)`, noe som indikerer at mengden eiendeler (tokens) er lagret som et 64-bit unsigned heltall. Dermed vil enhver transaksjon sende en viss mengde enheter av dette tokenet, som vil bli validert i henhold til denne strengt typede numeriske strukturen.


- (5) - Valencies**

Vi angir `valency_types: none!()`, noe som betyr at det ikke finnes noen valenser i dette skjemaet, med andre ord ingen spesielle eller ekstra rettigheter (som reissue, betinget brenning osv.). Hvis et skjema inneholdt slike, ville de blitt deklarert i denne delen.


- (6) - Genesis: første operasjoner

Her kommer vi inn i den delen som erklærer Contract Operations. Genesis er beskrevet av :


- Fraværet av `metadata` (feltet `metadata: Ty::<SemId>::UNIT.id(None)`) ;
- Globale tilstander som må være til stede én gang hver (`Once`);
- En Assignments-liste der `OS_ASSET` må vises `OnceOrMore`. Dette betyr at Genesis krever minst én `OS_ASSET`-tildeling (en opprinnelig holder);
- Ingen valens : `valens: none!()`.

Slik begrenser vi definisjonen av den første tokenutstedelsen: Vi må deklarere den utstedte forsyningen (`GS_ISSUED_SUPPLY`), pluss minst én innehaver (en Owned State av typen `OS_ASSET`).


- (7) - Utvidelser

Feltet `extensions: none!()` indikerer at det ikke er planlagt noen tilstandsutvidelse i denne kontrakten. Dette betyr at det ikke finnes noen operasjon for å innløse en digital rettighet (Valency) eller for å utføre en tilstandsutvidelse før en Transition. Alt gjøres via Genesis eller State Transitions.


- (8) - Overganger: TS_TRANSFER

I `transitions` definerer vi operasjonstypen `TS_TRANSFER`. Vi forklarer at :


- Den har ingen metadata;
- Den endrer ikke den globale tilstanden (som allerede er definert i Genesis);
- Den tar én eller flere `OS_ASSETs` som inndata. Dette betyr at den må bruke eksisterende Owned States;
- Den oppretter (`assignments`) minst én ny `OS_ASSET` (med andre ord, mottakeren eller mottakerne mottar tokens) ;
- Det genererer ingen ny Valency.

Dette modellerer oppførselen til en grunnleggende overføring, som forbruker tokens på en UTXO, deretter oppretter nye Owned States til fordel for mottakerne, og dermed bevarer likheten i det totale beløpet mellom innganger og utganger.


- (9) - AluVM-skript og inngangspunkter** (på fransk)

Til slutt deklarerer vi et AluVM-skript (`Script::AluVM(AluScript { ... })`). Dette skriptet inneholder :


- Ett eller flere eksterne biblioteker (`libs`) som skal brukes under valideringen;
- Inngangspunkter som peker til funksjonsoffset i AluVM-koden, som tilsvarer validering av Genesis (`ValidateGenesis`) og hver deklarerte Transition (`ValidateTransition(TS_TRANSFER)`).

Denne valideringskoden er ansvarlig for å bruke forretningslogikk. Den vil for eksempel sjekke :


- At `GS_ISSUED_SUPPLY` ikke overskrides under Genesis ;
- At summen av `input` (tokens brukt) er lik summen av `assignments` (tokens mottatt) for `TS_TRANSFER`.

Hvis disse reglene ikke overholdes, vil overgangen bli ansett som ugyldig.

Dette eksemplet på et "*Non Inflatable Fungible Asset*"-skjema gir oss en bedre forståelse av strukturen til en enkel RGB-fungibel tokenkontrakt. Vi kan tydelig se skillet mellom databeskrivelse (Global og Owned States), operasjonsdeklarasjon (Genesis, Transitions, Extensions) og valideringsimplementering (AluVM-skript). Takket være denne modellen oppfører et token seg som et klassisk fungibelt token, men forblir validert på klientsiden og er ikke avhengig av infrastrukturen i kjeden for å utføre koden. Bare kryptografiske forpliktelser er forankret i Bitcoin-blokkjeden.

### Grensesnitt

Grensesnittet er det laget som skal gjøre en kontrakt lesbar og manipulerbar, både av brukere (menneskelig lesing) og av porteføljer (programvarelesing). Grensesnittet spiller derfor en rolle som kan sammenlignes med et grensesnitt i et objektorientert programmeringsspråk (Java, Rust trait osv.), ved at det eksponerer og tydeliggjør den funksjonelle strukturen i en kontrakt, uten nødvendigvis å avsløre de interne detaljene i forretningslogikken.

I motsetning til Schema, som er rent deklarativt og kompilert til en binær fil som er vanskelig å bruke som den er, gir Interface de lesenøklene som trengs for å :


- Oppgi og beskriv de globale statene og eierstatene som inngår i kontrakten;
- Få tilgang til navnene og verdiene i hvert felt, slik at de kan vises (f.eks. for et token, finn ut tickeren, maksimumsbeløpet osv.);
- Tolke og konstruere kontraktsoperasjoner (Genesis, State Transition eller State Extension) ved å knytte data til forståelige navn (f.eks. utføre en overføring ved å spesifisere "beløp" i stedet for en binær identifikator).

![RGB-Bitcoin](assets/fr/073.webp)

Takket være grensesnittet kan du for eksempel skrive kode i en lommebok som, i stedet for å manipulere felter, manipulerer etiketter som "antall tokens", "asset name" osv. direkte. På denne måten blir det mer intuitivt å administrere en kontrakt. På denne måten blir kontraktshåndteringen mer intuitiv.

#### Generell drift

Denne metoden har mange fordeler:


- Standardisering:**

Samme type kontrakt kan støttes av et standardgrensesnitt som deles mellom flere lommebokimplementeringer. Dette forenkler kompatibilitet og gjenbruk av kode.


- Tydelig skille mellom skjema og grensesnitt:**

I RGB-design er Schema (forretningslogikk) og Grensesnitt (presentasjon og manipulering) to uavhengige enheter. Utviklerne som skriver kontraktslogikken, kan konsentrere seg om skjemaet uten å bekymre seg for ergonomi eller datarepresentasjon, mens et annet team (eller det samme teamet, men på en annen tidslinje) kan utvikle grensesnittet.


- Fleksibel utvikling:**

Grensesnittet kan endres eller legges til etter at aktivumet er utstedt, uten at selve kontrakten må endres. Dette er en stor forskjell fra andre smartkontraktsystemer i kjeden, der grensesnittet (ofte blandet med kjøringskoden) er frosset fast i blokkjeden.


- Mulighet for flere grensesnitt

Den samme kontrakten kan eksponeres gjennom ulike grensesnitt tilpasset ulike behov: et enkelt grensesnitt for sluttbrukeren, et mer avansert for utstederen som trenger å håndtere komplekse konfigurasjonsoperasjoner. Lommeboken kan deretter velge hvilket grensesnitt som skal importeres, avhengig av hva den skal brukes til.

![RGB-Bitcoin](assets/fr/074.webp)

I praksis, når lommeboken henter en RGB-kontrakt (via en `.rgb`- eller `.rgba`-fil), importerer den også det tilhørende grensesnittet, som også er kompilert. Ved kjøretid kan lommeboken for eksempel :


- Bla gjennom listen over stater og les navnene deres, for å vise Ticker, Initial Amount, Issue Date osv. i brukergrensesnittet, i stedet for en uleselig numerisk identifikator;
- Bygg en operasjon (for eksempel en overføring) ved hjelp av eksplisitte parameternavn: I stedet for å skrive `oppdrag { OS_ASSET => 1 }`, kan den tilby brukeren et "Beløp"-felt i et skjema, og oversette denne informasjonen til de strengt typede feltene som forventes av kontrakten.

#### Forskjellen fra Ethereum og andre systemer

I Ethereum er grensesnittet (beskrevet via ABI, *Application Binary Interface*) vanligvis avledet fra lagret kode i kjeden (smartkontrakten). Det kan være kostbart eller komplisert å endre en spesifikk del av grensesnittet uten å røre selve kontrakten. RGB er imidlertid basert på en logikk helt utenfor kjeden, med data forankret i *commitments* på Bitcoin. Dette designet gjør det mulig å endre grensesnittet (eller implementeringen av det) uten å påvirke den grunnleggende sikkerheten til kontrakten, ettersom valideringen av forretningsreglene forblir i skjemaet og den refererte AluVM-koden.

#### Sammenstilling av grensesnitt

Som med Schema defineres grensesnittet i kildekode (ofte i Rust) og kompileres til en `.rgb`- eller `.rgba`-fil. Denne binære filen inneholder all informasjonen som kreves av lommeboken for å :


- Identifiser felt etter navn ;
- Knytt hvert felt (og dets verdi) til den strenge systemtypen som er definert i kontrakten;
- Kjenn til de ulike operasjonene som er tillatt, og hvordan du bygger dem.

Når grensesnittet er importert, kan lommeboken vise kontrakten på riktig måte og foreslå interaksjoner for brukeren.

### Grensesnitt standardisert av LNP/BP-foreningen

I RGB-økosystemet brukes et grensesnitt til å gi dataene og operasjonene i en kontrakt en lesbar og manipulerbar betydning. Grensesnittet utfyller dermed skjemaet, som beskriver forretningslogikken internt (strenge typer, valideringsskript osv.). I dette avsnittet tar vi en titt på standardgrensesnittene som er utviklet av LNP/BP-foreningen for vanlige kontraktstyper (fungible tokens, NFT osv.).

Som en påminnelse er tanken at hvert grensesnitt beskriver hvordan man viser og manipulerer en kontrakt på lommeboksiden, med tydelige navn på feltene (for eksempel `spec`, `ticker`, `issuedSupply`...) og en definisjon av mulige operasjoner (for eksempel `Transfer`, `Burn`, `Rename`...). Flere grensesnitt er allerede operative, men det vil komme flere og flere i fremtiden.

#### Noen grensesnitt som er klare til bruk

**RGB20** er grensesnittet for fungible eiendeler, som kan sammenlignes med Ethereums ERC20-standard. Den går imidlertid et skritt videre og tilbyr mer omfattende funksjonalitet:


- For eksempel muligheten til å endre navn på eiendelen (endring av *ticker* eller fullt navn) etter at den er utstedt, eller til å justere presisjonen (*aksjesplitter*);
- Den kan også beskrive mekanismer for sekundær gjenutstedelse (begrenset eller ubegrenset) og for brenning og deretter erstatning, for å gi utstederen tillatelse til å ødelegge og deretter gjenskape eiendeler under visse betingelser;

RGB20-grensesnittet kan for eksempel kobles til **Non-Inflatable Asset (NIA)-ordningen**, som pålegger en ikke-oppblåsbar startforsyning, eller til andre mer avanserte ordninger etter behov.

**RGB21** gjelder kontrakter av NFT-typen, eller mer generelt alt unikt digitalt innhold, for eksempel representasjon av digitale medier (bilder, musikk osv.). I tillegg til å beskrive utstedelse og overføring av en enkelt eiendel, inkluderer den funksjoner som :


- Integrert støtte for direkte inkludering av en fil (opptil 16 MB) i kontrakten (for henting på klientsiden);
- Muligheten for eieren til å legge inn en "*inngravering*" i historikken for å bevise tidligere eierskap av en NFT.

**RGB25** er en hybridstandard som kombinerer fungible og ikke-fungible aspekter. Den er utformet for delvis fungible eiendeler, for eksempel tokenisering av eiendom, der du ønsker å dele opp en eiendom samtidig som du beholder en kobling til en enkelt rotaktivitet (med andre ord har du fungible deler av et hus som er koblet til et ikke-fungibelt hus). Teknisk sett kan dette grensesnittet kobles til **Collectible Fungible Asset* (CFA)**-skjemaet, som tar hensyn til oppsplitting samtidig som det opprinnelige aktivumet spores.

#### Grensesnitt under utvikling

Andre grensesnitt er planlagt for mer spesialiserte bruksområder, men er ennå ikke tilgjengelige:


- RGB22**, dedikert til digitale identiteter, for å administrere identifikatorer og kjedeprofiler i RGB-økosystemet;
- RGB23**, for avansert tidsstempling, som bruker noen av ideene fra *Opentimestamps*, men med sporbarhetsfunksjoner;
- RGB24**, som tar sikte på et desentralisert domenenavnsystem (DNS) tilsvarende *Ethereum Name Service* ;
- RGB26**, utviklet for å administrere DAO-er (*Decentralized Autonomous Organization*) i et mer komplekst format (styring, stemmegivning osv.);
- RGB30**, som er svært lik RGB20, men med det spesielle at den tar hensyn til desentralisert opprinnelig utstedelse og bruker State Extensions. Dette vil bli brukt for eiendeler som utstedes på nytt av flere enheter, eller som er underlagt finere betingelser.

Avhengig av hvilken dato du konsulterer dette kurset, kan det selvsagt hende at disse grensesnittene allerede er operative og tilgjengelige.

#### Eksempel på grensesnitt

Denne Rust-kodebiten viser et [RGB20](https://github.com/RGB-WG/rgb-std/blob/master/src/interface/rgb20.rs)-grensesnitt (fungible asset). Denne koden er hentet fra filen `rgb20.rs` i standard RGB-biblioteket. La oss ta en titt på den for å forstå strukturen til et grensesnitt og hvordan det bygger bro mellom forretningslogikken (definert i skjemaet) på den ene siden og funksjonalitetene som eksponeres for lommebøker og brukere på den andre siden.

```rust
// ...
fn rgb20() -> Iface {
let types = StandardTypes::with(rgb20_stl());
Iface {
version: VerNo::V1,
name: tn!("RGB20"),
global_state: tiny_bmap! {
fname!("spec") => GlobalIface::required(types.get("RGBContract.DivisibleAssetSpec")),
fname!("data") => GlobalIface::required(types.get("RGBContract.ContractData")),
fname!("created") => GlobalIface::required(types.get("RGBContract.Timestamp")),
fname!("issuedSupply") => GlobalIface::one_or_many(types.get("RGBContract.Amount")),
fname!("burnedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
fname!("replacedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
},
assignments: tiny_bmap! {
fname!("inflationAllowance") => AssignIface::public(OwnedIface::Amount, Req::NoneOrMore),
fname!("updateRight") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnEpoch") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnRight") => AssignIface::public(OwnedIface::Rights, Req::NoneOrMore),
fname!("assetOwner") => AssignIface::private(OwnedIface::Amount, Req::NoneOrMore),
},
valencies: none!(),
genesis: GenesisIface {
metadata: Some(types.get("RGBContract.IssueMeta")),
global: tiny_bmap! {
fname!("spec") => ArgSpec::required(),
fname!("data") => ArgSpec::required(),
fname!("created") => ArgSpec::required(),
fname!("issuedSupply") => ArgSpec::required(),
},
assignments: tiny_bmap! {
fname!("assetOwner") => ArgSpec::many(),
fname!("inflationAllowance") => ArgSpec::many(),
fname!("updateRight") => ArgSpec::optional(),
fname!("burnEpoch") => ArgSpec::optional(),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_RESERVES
},
},
transitions: tiny_bmap! {
tn!("Transfer") => TransitionIface {
optional: false,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("previous") => ArgSpec::from_non_empty("assetOwner"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_non_empty("assetOwner"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Issue") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.IssueMeta")),
globals: tiny_bmap! {
fname!("issuedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_non_empty("inflationAllowance"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_many("inflationAllowance"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
ISSUE_EXCEEDS_ALLOWANCE,
INSUFFICIENT_RESERVES
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("OpenEpoch") => TransitionIface {
optional: true,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnEpoch"),
},
assignments: tiny_bmap! {
fname!("next") => ArgSpec::from_optional("burnEpoch"),
fname!("burnRight") => ArgSpec::required()
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("burnRight")),
},
tn!("Burn") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("burnedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: None,
},
tn!("Replace") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("replacedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS,
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Rename") => TransitionIface {
optional: true,
metadata: None,
globals: tiny_bmap! {
fname!("new") => ArgSpec::from_required("spec"),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("updateRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("updateRight"),
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("future")),
},
},
extensions: none!(),
error_type: types.get("RGB20.Error"),
default_operation: Some(tn!("Transfer")),
type_system: types.type_system(),
}
}
```

I dette grensesnittet ser vi likheter med skjemastrukturen: Vi finner en erklæring av Global State, Owned States, Contract Operations (Genesis og Transitions), samt feilhåndtering. Men grensesnittet fokuserer på presentasjonen og manipuleringen av disse elementene for en lommebok eller en hvilken som helst annen applikasjon.

Forskjellen fra Schema ligger i typenes natur. Schema bruker strenge typer (for eksempel `FungibleType::Unsigned64Bit`) og mer tekniske identifikatorer. Interface bruker feltnavn, makroer (`fname!()`, `tn!()`) og referanser til argumentklasser (`ArgSpec`, `OwnedIface::Rights`...). Målet her er å lette den funksjonelle forståelsen og organiseringen av elementer for lommeboken.

I tillegg kan grensesnittet introdusere ytterligere funksjonalitet til det grunnleggende skjemaet (f.eks. administrasjon av en `burnEpoch`-rettighet), så lenge dette forblir i samsvar med den endelige validerte logikken på klientsiden. AluVM-"skript"-delen i skjemaet vil sikre kryptografisk validitet, mens grensesnittet beskriver hvordan brukeren (eller lommeboken) samhandler med disse tilstandene og overgangene.

#### Global tilstand og oppgaver

I `global_state`-seksjonen finner vi felt som `spec` (asset description), `data`, `created`, `issuedSupply`, `burnedSupply`, `replacedSupply`. Dette er felt som lommeboken kan lese og presentere. For eksempel


- `spec` viser tokenkonfigurasjonen;
- `issuedSupply` eller `burnedSupply` gir oss det totale antallet tokens som er utstedt eller brent, osv.

I delen `assignments` definerer vi ulike roller eller rettigheter. For eksempel


- `assetOwner` tilsvarer beholdningen av tokens (det er den fungible *Owned State*) ;
- `burnRight` tilsvarer muligheten til å brenne tokens ;
- updateRight` tilsvarer retten til å gi nytt navn til eiendelen.

Nøkkelordet `public` eller `private` (f.eks. `AssignIface::public(...)`) angir om disse tilstandene er synlige (`public`) eller konfidensielle (`private`). Når det gjelder `Req::NoneOrMore`, `Req::Optional`, indikerer de den forventede forekomsten.

#### Genesis og overganger

Genesis-delen beskriver hvordan eiendelen initialiseres:


- Feltene `spec`, `data`, `created`, `issuedSupply` er obligatoriske (`ArgSpec::required()`) ;
- Tildelinger som `assetOwner` kan finnes i flere kopier (`ArgSpec::many()`), slik at tokens kan distribueres til flere opprinnelige innehavere;
- Felt som `inflationAllowance` eller `burnEpoch` kan (eller kan ikke) være inkludert i Genesis.

For hver overgang (`Transfer`, `Issue`, `Burn`...) definerer grensesnittet hvilke felter operasjonen forventer som input, hvilke felter operasjonen vil produsere som output, og eventuelle feil som kan oppstå. For eksempel

**Transition :**


- Inndata : `previous` → må være en `assetOwner` ;
- Tildelinger : `beneficiary` → blir en ny `assetOwner` ;
- Feil: `NON_EQUAL_AMOUNTS` (lommeboken vil dermed kunne håndtere tilfeller der inngangssummen ikke samsvarer med utgangssummen).

**Transition `Issue` :**


- Valgfritt (`optional: true`), ettersom ekstra utslipp ikke nødvendigvis aktiveres;
- Inndata: `used` → en `inflationAllowance`, dvs. tillatelse til å legge til flere tokens ;
- Tildelinger: `beneficiary` (nye tokens mottatt) og `future` (gjenværende `inflationAllowance`) ;
- Mulige feil: `SUPPLY_MISMATCH`, `ISSUE_EXCEEDS_ALLOWANCE`, osv.

**Brenn overgang :**


- Innganger : `used` → a `burnRight` ;
- Globaler : `burnedSupply` kreves ;
- Oppgaver: `future` → en mulig fortsettelse av `burnRight` hvis vi ikke har brent alt ;
- Feil: `SUPPLY_MISMATCH`, `INVALID_PROOF`, `INSUFFICIENT_COVERAGE`.

Hver operasjon er derfor beskrevet på en måte som er lesbar for en lommebok. Dette gjør det mulig å vise et grafisk grensesnitt der brukeren tydelig kan se: "Du har rett til å brenne. Vil du brenne et visst beløp? Koden vet at den skal fylle ut et `burnedSupply`-felt og sjekke at `burnRight` er gyldig.

For å oppsummere er det viktig å huske på at et grensesnitt, uansett hvor komplett det er, ikke i seg selv definerer kontraktens interne logikk. Kjernen i arbeidet gjøres av **Schema**, som inkluderer strenge typer, Genesis-struktur, overganger og så videre. Grensesnittet eksponerer ganske enkelt disse elementene på en mer intuitiv og navngitt måte, slik at de kan brukes i en applikasjon.

Takket være RGBs modularitet kan grensesnittet oppgraderes (for eksempel ved å legge til en `Rename`-overgang, korrigere visningen av et felt osv.) uten å måtte skrive om hele kontrakten. Brukerne av dette grensesnittet kan da dra umiddelbar nytte av disse forbedringene så snart de oppdaterer filen `.rgb` eller `.rgba`.

Men når du har deklarert et grensesnitt, må du koble det til det tilhørende skjemaet. Dette gjøres via ***Interface Implementation***, som spesifiserer hvordan hvert navngitte felt (for eksempel `fname!("assetOwner")`) skal mappes til den strenge ID-en (for eksempel `OS_ASSET`) som er definert i Schemaet. Dette sikrer for eksempel at når en lommebok manipulerer et `burnRight`-felt, er dette den tilstanden som i skjemaet beskriver muligheten til å brenne tokens.

### Implementering av grensesnitt

I RGB-arkitekturen har vi sett at hver komponent (skjema, grensesnitt osv.) kan utvikles og kompileres uavhengig av hverandre. Det er likevel ett uunnværlig element som knytter disse ulike byggeklossene sammen: ***Grensesnittimplementeringen***. Det er dette som eksplisitt tilordner identifikatorene eller feltene som er definert i skjemaet (på forretningslogikksiden) til navnene som er deklarert i grensesnittet (på presentasjons- og brukerinteraksjonssiden). Når en lommebok laster inn en kontrakt, kan den dermed forstå nøyaktig hvilket felt som tilsvarer hva, og hvordan en operasjon som er navngitt i grensesnittet, forholder seg til logikken i skjemaet.

Et viktig poeng er at grensesnittimplementeringen ikke nødvendigvis er ment å eksponere alle skjemafunksjoner eller alle grensesnittfelter: den kan begrenses til en delmengde. I praksis gjør dette det mulig å begrense eller filtrere visse aspekter av skjemaet. Du kan for eksempel ha et skjema med fire typer operasjoner, men et implementasjonsgrensesnitt som bare tilordner to av dem i en gitt kontekst. Omvendt, hvis et grensesnitt foreslår flere endepunkter, kan vi velge å ikke implementere dem her.

Her er et klassisk eksempel på grensesnittimplementering, der vi knytter et *Non-Inflatable Asset* (NIA)-skjema til RGB20-grensesnittet:

```rust
fn nia_rgb20() -> IfaceImpl {
let schema = nia_schema();
let iface = Rgb20::iface();
IfaceImpl {
version: VerNo::V1,
schema_id: schema.schema_id(),
iface_id: iface.iface_id(),
script: none!(),
global_state: tiny_bset! {
NamedField::with(GS_NOMINAL, fname!("spec")),
NamedField::with(GS_DATA, fname!("data")),
NamedField::with(GS_TIMESTAMP, fname!("created")),
NamedField::with(GS_ISSUED_SUPPLY, fname!("issuedSupply")),
},
assignments: tiny_bset! {
NamedField::with(OS_ASSET, fname!("assetOwner")),
},
valencies: none!(),
transitions: tiny_bset! {
NamedType::with(TS_TRANSFER, tn!("Transfer")),
},
extensions: none!(),
}
}
```

I dette implementasjonsgrensesnittet :


- Vi refererer eksplisitt til skjemaet, via `nia_schema()`, og grensesnittet, via `Rgb20::iface()`. Anropene `schema.schema_id()` og `iface.iface_id()` brukes til å forankre grensesnittimplementeringen på kompileringssiden (dette knytter sammen de kryptografiske identifikatorene til disse to komponentene);
- Det opprettes en mapping mellom skjemaelementer og grensesnittelementer. For eksempel kobles feltet `GS_NOMINAL` i skjemaet til strengen `"spec"` på grensesnittsiden (`NamedField::with(GS_NOMINAL, fname!("spec"))`). Vi gjør det samme for operasjoner, for eksempel `TS_TRANSFER`, som vi kobler til `"Transfer"` i grensesnittet... ;
- Vi kan se at det ikke finnes noen valenser (`valencies: none!()`) eller utvidelser (`extensions: none!()`), noe som gjenspeiler det faktum at denne NIA-kontrakten ikke bruker disse funksjonene.

Resultatet etter kompilering er en separat `.rgb`- eller `.rgba`-fil, som skal importeres til lommeboken i tillegg til skjemaet og grensesnittet. Dermed vet programvaren hvordan man konkret kobler denne NIA-kontrakten (hvis logikk er beskrevet av skjemaet) til "RGB20"-grensesnittet (som gir menneskelige navn og en interaksjonsmodus for fungible tokens), og bruker denne grensesnittimplementeringen som en gateway mellom de to.

#### Hvorfor separat grensesnittimplementering?

Separasjon øker fleksibiliteten. Et enkelt skjema kan ha flere forskjellige grensesnittimplementasjoner, som hver kartlegger ulike funksjoner. I tillegg kan selve grensesnittimplementeringen utvikles eller skrives om uten at det kreves endringer i verken skjemaet eller grensesnittet. På denne måten beholdes RGBs prinsipp om modularitet: Hver komponent (skjema, grensesnitt, grensesnittimplementasjon) kan versjoneres og oppdateres uavhengig av hverandre, så lenge protokollens kompatibilitetsregler overholdes (samme identifikatorer, konsistens i typer osv.).

Når lommeboken laster inn en kontrakt, må den i praksis :


- Last inn det kompilerte **skjemaet** (for å kjenne strukturen i forretningslogikken) ;
- Last inn kompilert **Grensesnitt** (for å forstå navn og operasjoner på brukersiden) ;
- Last inn kompilert **Grensesnitt-implementering** (for å koble skjemalogikk til grensesnittnavn, operasjon for operasjon, felt for felt).

Denne modulære arkitekturen muliggjør bruksscenarioer som :


- Begrens visse operasjoner for visse brukere: tilby et delvis implementeringsgrensesnitt som bare gir tilgang til grunnleggende overføringer, uten å tilby for eksempel brenne- eller oppdateringsfunksjoner;
- Endringspresentasjon: Utform en grensesnittimplementasjon som gir nytt navn til et felt i grensesnittet eller tilordner det på en annen måte, uten å endre grunnlaget for kontrakten;
- Støtte for flere ordninger: En lommebok kan laste inn flere grensesnittimplementasjoner for samme grensesnittype for å håndtere ulike ordninger (ulike tokenlogikker), forutsatt at strukturen er kompatibel.

I neste kapittel skal vi se nærmere på hvordan en kontraktsoverføring fungerer, og hvordan RGB-fakturaer genereres.

## Overføring av kontrakter

<chapterId>f043a307-d420-5752-b0d7-ebfd845802c0</chapterId>

![video](https://youtu.be/sVoKIi-1XbY)

I dette kapittelet skal vi analysere prosessen med en kontraktsoverføring i RGB-økosystemet. For å illustrere dette tar vi en titt på Alice og Bob, våre vanlige hovedpersoner, som ønsker å bytte en RGB-aktiva. Vi skal også vise noen kommandoutdrag fra kommandolinjeverktøyet `rgb`, for å se hvordan det fungerer i praksis.

### Forståelse av RGB-kontraktsoverføring

La oss ta et eksempel på en overføring mellom Alice og Bob. I dette eksempelet antar vi at Bob akkurat har begynt å bruke RGB, mens Alice allerede har RGB-aktiva i lommeboken sin. Vi skal se hvordan Bob setter opp miljøet sitt, importerer den relevante kontrakten, deretter ber om en overføring fra Alice, og til slutt hvordan Alice utfører den faktiske transaksjonen på Bitcoin-blokkjeden.

#### 1) Installere RGB-lommeboken

Først og fremst må Bob installere en RGB-lommebok, dvs. programvare som er kompatibel med protokollen. Denne inneholder ingen kontrakter i utgangspunktet. Bob trenger også :


- En Bitcoin-lommebok for å administrere UTXO-ene dine;
- En tilkobling til en Bitcoin-node (eller til en Electrum-server), slik at du kan identifisere UTXO-ene dine og spre transaksjonene dine i nettverket.

Som en påminnelse, **Owned States** i RGB refererer til Bitcoin UTXOs. Vi må derfor alltid kunne administrere og bruke UTXO-er i en Bitcoin-transaksjon som inneholder kryptografiske forpliktelser (`Tapret` eller `Opret`) som peker på RGB-data.

#### 2) Innhenting av kontraktsinformasjon

Bob må deretter hente ut de kontraktsdataene han er interessert i. Disse dataene kan sirkulere via en hvilken som helst kanal: nettside, e-post, meldingsprogram... I praksis grupperes de sammen i en ***sending***, dvs. en liten datapakke som inneholder :


- **Genesis**, som definerer kontraktens opprinnelige tilstand;
- **Schema**, som beskriver forretningslogikken (strenge typer, valideringsskript osv.);
- Grensesnittet **Interface**, som definerer presentasjonslaget (feltnavn, tilgjengelige operasjoner);
- Grensesnittsimplementeringen**, som konkret knytter skjemaet til grensesnittet.

![RGB-Bitcoin](assets/fr/075.webp)

Den totale størrelsen er ofte i størrelsesorden noen få kilobyte, ettersom hver komponent som regel veier mindre enn 200 byte. Det kan også være mulig å kringkaste denne forsendelsen i Base58, via sensurresistente kanaler (som for eksempel Nostr eller via Lightning Network), eller som en QR-kode.

#### 3) Import og validering av kontrakter

Når Bob har mottatt forsendelsen, importerer han den til RGB-lommeboken sin. Denne vil da :


- Kontroller at Genesis og Schema er gyldige;
- Innlastingsgrensesnitt og implementering av grensesnitt ;
- Oppdater datalageret på klientsiden.

Bob kan nå se eiendelen i lommeboken sin (selv om han ikke eier den ennå) og forstå hvilke felt som er tilgjengelige, hvilke operasjoner som er mulige... Deretter må han kontakte en person som faktisk eier eiendelen som skal overføres. I vårt eksempel er dette Alice.

Prosessen med å finne ut hvem som har en bestemt RGB-eiendel, ligner på å finne en Bitcoin-betaler. Detaljene i denne forbindelsen avhenger av bruken (markedsplasser, private chattekanaler, fakturering, salg av varer og tjenester, lønn ...).

#### 4) Utstedelse av faktura

For å starte overføringen av en RGB-eiendel må Bob først utstede en faktura. Denne fakturaen brukes til å :


- Fortell Alice hvilken type operasjon som skal utføres (for eksempel en `Transfer` fra et RGB20-grensesnitt);
- Gi Alice Bobs *forseglingsdefinisjon* (dvs. UTXO-en der han ønsker å motta eiendelen);
- Angi mengden virkestoff som kreves (f.eks. 100 enheter).

Bob bruker `rgb`-verktøyet på kommandolinjen. Anta at han vil ha 100 enheter av en token med kjent `ContractId`, ønsker å stole på `Tapret`, og spesifiserer UTXO (`456e3..dfe1:0`):

```bash
bob$ rgb invoice RGB20 100 <ContractId> tapret1st:456e3..dfe1:0
```

Vi skal se nærmere på strukturen til RGB-fakturaer i slutten av dette kapittelet.

#### 5) Fakturaoverføring

Den genererte fakturaen (f.eks. som URL: `rgb:2WBcas9.../RGB20/100+utxob:...`) inneholder all informasjonen Alice trenger for å forberede overføringen. Som med forsendelsen kan den kodes kompakt (Base58 eller et annet format) og sendes via et meldingsprogram, e-post, Nostr...

![RGB-Bitcoin](assets/fr/076.webp)

#### 6) Transaksjonsforberedelser på Alice-siden

Alice mottar fakturaen fra Bob. I RGB-lommeboken sin har hun en stash som inneholder eiendelen som skal overføres. For å bruke UTXO-en som inneholder eiendelen, må hun først generere en PSBT (*Partially Signed Bitcoin Transaction*), dvs. en ufullstendig Bitcoin-transaksjon, ved hjelp av UTXO-en hun har:

```bash
alice$ wallet construct tx.psbt
```

Denne basistransaksjonen (foreløpig usignert) vil bli brukt til å forankre den kryptografiske forpliktelsen knyttet til overføringen til Bob. Alices UTXO vil dermed bli brukt, og i utdataene vil vi plassere `Tapret`- eller `Opret`-forpliktelsen for Bob.

#### 7) Generering av overføringsforsendelse

Deretter bygger Alice ***terminalforsendelsen*** (noen ganger kalt "overføringssending") via kommandoen :

```bash
alice$ rgb transfer tx.psbt <invoice> consignment.rgb
```

Denne nye filen `consignment.rgb` inneholder :


- Den komplette historikken over State Transitions som kreves for å validere eiendelen frem til i dag (siden Genesis);
- Den nye tilstandsovergangen som overfører aktiva fra Alice til Bob, i henhold til fakturaen Bob har utstedt;
- Den ufullstendige Bitcoin-transaksjonen (*vitnetransaksjon*) (`tx.psbt`), som bruker Alices Single-use Seal, modifisert for å inkludere den kryptografiske forpliktelsen til Bob.

På dette stadiet er transaksjonen ennå ikke kringkastet på Bitcoin-nettverket. Forsendelsen er større enn en enkel forsendelse, ettersom den inkluderer hele historikken (*beviskjeden*) for å bevise eiendelens legitimitet.

#### 8) Bob kontrollerer og aksepterer forsendelsen

Alice overfører denne **terminalforsendelsen** til Bob. Bob vil da :


- Kontroller gyldigheten av tilstandsovergangen (sørg for at historikken er konsistent, at kontraktsreglene overholdes osv;)
- Legg den til ditt lokale lager;
- Eventuelt generere en signatur (`sig:...`) på forsendelsen, for å bevise at den har blitt undersøkt og godkjent (noen ganger kalt en "*payslip*").

```bash
bob$ rgb accept consignment.rgb
sig:DbwzvSu4BZU81jEpE9FVZ3xjcyuTKWWy2gmdnaxtACrS
```

![RGB-Bitcoin](assets/fr/077.webp)

#### 9) Alternativ: Bob sender bekreftelse tilbake til Alice (*betalingsslipp*)

Hvis Bob ønsker det, kan han sende denne signaturen tilbake til Alice. Dette indikerer:


- At den anerkjenner overgangen som gyldig;
- At han samtykker til at Bitcoin-transaksjonen sendes.

Dette er ikke obligatorisk, men det kan gi Alice en forsikring om at det ikke vil oppstå senere tvister om overføringen.

#### 10) Alice signerer og publiserer transaksjonen

Alice kan da :


- Sjekk Bobs signatur (`rgb check <sig>`) ;
- Signer *vitnetransaksjonen* som fortsatt er en PSBT (`wallet sign`) ;
- Publiser vitnetransaksjonen på Bitcoin-nettverket (`-publish`).

```bash
alice$ rgb check <sig>
alice$ wallet sign —publish tx.psbt
```

![RGB-Bitcoin](assets/fr/078.webp)

Når transaksjonen er bekreftet, markerer den at overføringen er fullført. Bob blir den nye eieren av eiendelen: Han har nå en Owned State som peker til UTXO-en han kontrollerer, noe som bevises av forpliktelsen i transaksjonen.

For å oppsummere, her er den komplette overføringsprosessen:

![RGB-Bitcoin](assets/fr/079.webp)

### Fordeler med RGB-overføringer


- Konfidensialitet** :

Bare Alice og Bob har tilgang til alle data om tilstandsoverganger. De utveksler denne informasjonen utenfor blokkjeden, via forsendelser. De kryptografiske forpliktelsene i Bitcoin-transaksjonen avslører ikke typen eiendel eller beløpet, noe som garanterer langt større konfidensialitet enn andre token-systemer i kjeden.


- Validering på kundesiden** :

Bob kan sjekke konsistensen av overføringen ved å sammenligne *forsendelsen* med *forankringene* i Bitcoin-blokkjeden. Han trenger ikke tredjepartsvalidering. Alice trenger ikke å publisere hele historikken på blokkjeden, noe som reduserer belastningen på basisprotokollen og forbedrer konfidensialiteten.


- Forenklet atomicitet** :

Komplekse utvekslinger (atombytter mellom BTC og en RGB-aktiva, for eksempel) kan utføres i én enkelt transaksjon, slik at man unngår behovet for HTLC- eller PTLC-skript. Hvis avtalen ikke kringkastes, kan alle gjenbruke UTXO-ene sine på andre måter.

### Oppsummeringsdiagram for overføring

Før vi ser nærmere på fakturaene, kan du se et oversiktsdiagram over den overordnede flyten i en RGB-overføring:


- Bob installerer en RGB-lommebok og får den første kontraktsforsendelsen;
- Bob utsteder en faktura der UTXO oppgir hvor eiendelen skal mottas;
- Alice mottar fakturaen, oppretter PSBT og genererer terminalforsendelsen;
- Bob aksepterer den, sjekker, legger dataene til lageret sitt og signerer (*betalingsslipp*) om nødvendig;
- Alice publiserer transaksjonen på Bitcoin-nettverket;
- Bekreftelse av transaksjonen gjør overføringen offisiell.

![RGB-Bitcoin](assets/fr/080.webp)

Overføringen illustrerer all kraften og fleksibiliteten i RGB-protokollen: en privat utveksling, validert på klientsiden, minimalt og diskret forankret i Bitcoin-blokkjeden, og som beholder det beste av protokollens sikkerhet (ingen risiko for dobbeltbruk). Dette gjør RGB til et lovende økosystem for verdioverføringer som er mer konfidensielle og skalerbare enn programmerbare blokkjeder i kjeden.

### Fakturaer RGB

I denne delen forklarer vi i detalj hvordan **fakturaer** fungerer i RGB-økosystemet, og hvordan de gjør det mulig å utføre operasjoner (spesielt overføringer) med en kontrakt. Først ser vi på identifikatorene som brukes, deretter på hvordan de kodes, og til slutt på strukturen til en faktura uttrykt som en URL (et format som er praktisk nok til bruk i lommebøker).

#### Identifikatorer og koding

Det er definert en unik identifikator for hvert av de følgende elementene:


- En RGB-kontrakt;
- Skjemaet (forretningslogikken) ;
- Grensesnitt og implementering av grensesnitt ;
- Dens eiendeler (tokens, NFT osv.),

Denne entydigheten er svært viktig, ettersom hver komponent i systemet må kunne skilles fra hverandre. En kontrakt X må for eksempel ikke kunne forveksles med en annen kontrakt Y, og to forskjellige grensesnitt (RGB20 vs. RGB21, for eksempel) må ha forskjellige identifikatorer.

For å gjøre disse identifikatorene både effektive (liten størrelse) og lesbare, bruker vi :


- Base58-koding, som unngår bruk av forvirrende tegn (f.eks. `0` og bokstaven `O`) og gir relativt korte strenger;
- Et prefiks som angir identifikatorens art, vanligvis i form av `rgb:` eller et lignende URN.

For eksempel kan en `ContractId` representeres av noe sånt som :

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```

Prefikset `rgb:` bekrefter at dette er en RGB-identifikator, og ikke en HTTP-lenke eller annen protokoll. Takket være dette prefikset kan lommebøker tolke strengen riktig.

#### Segmentering av identifikatorer

RGB-identifikatorer er ofte ganske lange, ettersom den underliggende (kryptografiske) sikkerheten kan kreve felt på 256 bit eller mer. For å gjøre det enklere for mennesker å lese og verifisere disse strengene, deler vi dem opp i flere blokker atskilt med en bindestrek (`-`). I stedet for å ha en lang, uavbrutt streng med tegn, deler vi den altså opp i kortere blokker. Denne praksisen er vanlig for kredittkort eller telefonnumre, og den gjelder også her for å gjøre det enklere å verifisere. En bruker eller partner kan for eksempel få beskjed om dette: "*Sjekk at den tredje blokken er `9GEgnyMj7`*", i stedet for å måtte sammenligne alt på én gang. Den siste blokken brukes ofte som en **kontrollsum**, for å ha et system for å oppdage feil eller skrivefeil.

Som et eksempel kan en `ContractId` i base58-kodet og segmentert være :

```txt
2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```

Hver av strekene deler strengen inn i seksjoner. Dette påvirker ikke semantikken i koden, bare presentasjonen av den.

#### Bruke nettadresser for fakturaer

En RGB-faktura presenteres som en URL. Det betyr at den kan klikkes på eller skannes (som en QR-kode), og en lommebok kan tolke den direkte for å gjennomføre en transaksjon. Denne enkle interaksjonen skiller seg fra andre systemer der man må kopiere og lime inn ulike data i ulike felt i programvaren.

En faktura for en fungibel token (f.eks. en RGB20-token) kan se slik ut:

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

La oss analysere denne URL-en:


- `rgb:`** (prefiks): angir en lenke som påkaller RGB-protokollen (tilsvarende `http:` eller `bitcoin:` i andre sammenhenger);
- `2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX`**: representerer `ContractId` for tokenet du ønsker å manipulere;
- `/RGB20/100`**: indikerer at `RGB20`-grensesnittet brukes, og at 100 enheter av ressursen er forespurt. Syntaksen er `/Interface/amount` ;
- `+utxob:`**: angir at informasjon om UTXO-mottakeren (eller, mer presist, definisjonen av Single-use Seal) legges til;
- `egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb`**: Dette er den *blindede* UTXO-en (eller forseglingsdefinisjonen). Bob har med andre ord maskert sin nøyaktige UTXO, slik at avsenderen (Alice) ikke vet hva den nøyaktige adressen er. Hun vet bare at det finnes et gyldig segl som refererer til en UTXO som kontrolleres av Bob.

Det faktum at alt er samlet i én URL gjør livet enklere for brukeren: Et enkelt klikk eller skanning i lommeboken, og operasjonen er klar til å utføres.

Man kan tenke seg systemer der en enkel ticker (f.eks. `USDT`) brukes i stedet for `ContractId`. Dette ville imidlertid skape store problemer med tillit og sikkerhet: En ticker er ikke en unik referanse (flere kontrakter kunne hevde å hete `USDT`). Med RGB ønsker vi en unik, entydig kryptografisk identifikator. Derfor har vi valgt en 256-biters streng, kodet i base58 og segmentert. Brukeren vet at han manipulerer nettopp den kontrakten som har ID-en `2WBcas9-yjz...` og ikke noen annen.

#### Ytterligere URL-parametere

Du kan også legge til flere parametere i URL-en, på samme måte som med HTTP, for eksempel :

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb?sig=6kzbKKffP6xftkxn9UP8gWqiC41W16wYKE5CYaVhmEve
```


- `?sig=...`: representerer for eksempel en signatur knyttet til fakturaen, som noen lommebøker kan verifisere;
- Hvis en lommebok ikke administrerer denne signaturen, ignorerer den ganske enkelt denne parameteren.

La oss ta tilfellet med en NFT via RGB21-grensesnittet. Vi kan for eksempel ha :

```txt
rgb:7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK/RGB21/DbwzvSu-4BZU81jEp-E9FVZ3xj-cyuTKWWy-2gmdnaxt-ACrS+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Her ser vi :


- `rgb:`**: URL-prefiks ;
- `7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK`**: Kontrakts-ID (NFT) ;
- rGB21**: grensesnitt for ikke-soppbare eiendeler (NFT) ;
- `DbwzvSu-4BZU81jEp-...`**: en eksplisitt referanse til den unike delen av NFT-en, for eksempel en hash av datablobben (media, metadata ...) ;
- `+utxob:egXsFnw-...`**: forseglingsdefinisjonen.

Tanken er den samme: Overfør en unik lenke som lommeboken kan tolke, og som tydelig identifiserer den unike eiendelen som skal overføres.

#### Andre operasjoner via URL

RGB-URL-er brukes ikke bare til å be om en overføring. De kan også kode mer avanserte operasjoner, for eksempel utstedelse av nye tokens (*issuance*). For eksempel:

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/issue/100000+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Her finner vi :


- `rgb:` : protokoll ;
- `2WBcas9-...`: Kontrakt-ID ;
- `/RGB20/issue/100000`: indikerer at du ønsker å påkalle "*Issue*"-overgangen for å opprette ytterligere 100 000 tokens;
- `+utxob:`: definisjonen av seglet.

Lommeboken kan for eksempel se slik ut "Jeg har blitt bedt om å utføre en `utstedelse`-operasjon fra `RGB20`-grensesnittet, på den og den kontrakten, for 100 000 enheter, til fordel for den og den engangsforseglingen*."

Nå som vi har sett på hovedelementene i RGB-programmering, skal jeg ta deg gjennom neste kapittel om hvordan du utarbeider en RGB-kontrakt.

## Utarbeidelse av smartkontrakter

<chapterId>0e0a645c-0049-588d-8965-b8c536590cc9</chapterId>

![video](https://youtu.be/GRwS-NvWF3I)

I dette kapittelet går vi steg for steg gjennom hvordan du skriver en kontrakt ved hjelp av kommandolinjeverktøyet `rgb`. Målet er å vise hvordan du installerer og manipulerer CLI, kompilerer et **skjema**, importerer **grensesnittet** og **grensesnittsimplementeringen**, og deretter utsteder (*issue*) en ressurs. Vi ser også på den underliggende logikken, inkludert kompilering og tilstandsvalidering. Ved slutten av dette kapittelet bør du være i stand til å reprodusere prosessen og opprette dine egne RGB-kontrakter.

Som en påminnelse er den interne logikken i RGB basert på Rust-biblioteker som du som utvikler kan importere til prosjektene dine for å håndtere valideringsdelen på klientsiden. I tillegg jobber LNP/BP Association-teamet med bindinger for andre språk, men dette er ennå ikke ferdigstilt. I tillegg utvikler andre enheter som Bitfinex sine egne integrasjonsstabler (vi vil snakke om disse i de to siste kapitlene i kurset). Inntil videre er derfor `rgb` CLI den offisielle referansen, selv om den fortsatt er relativt upolert.

### Installasjon og presentasjon av rgb-verktøyet

Hovedkommandoen heter ganske enkelt `rgb`. Den er designet for å minne om `git`, med et sett underkommandoer for å manipulere kontrakter, påkalle dem, utstede eiendeler og så videre. Bitcoin Wallet er for øyeblikket ikke integrert, men vil bli det i en nært forestående versjon (0.11). Denne neste versjonen vil gjøre det mulig for brukere å opprette og administrere lommebøker (via deskriptorer) direkte fra `rgb`, inkludert PSBT-generering, kompatibilitet med ekstern maskinvare (f.eks. en maskinvarelommebok) for signering, og interoperabilitet med programvare som Sparrow. Dette vil forenkle hele utstedelses- og overføringsscenarioet.

#### Installasjon via Cargo

Vi installerer verktøyet i Rust med :

```bash
cargo install rgb-contracts --all-features
```

(Merk: Kassen heter `rgb-contracts`, og den installerte kommandoen vil hete `rgb`. Hvis det allerede eksisterte en crate med navnet `rgb`, kan det ha vært en kollisjon, derav navnet)

Installasjonen kompilerer et stort antall avhengigheter (f.eks. kommandoanalyse, Electrum-integrasjon, håndtering av nullkunnskapsbevis osv.)

Når installasjonen er fullført, vil :

```bash
rgb
```

Ved å kjøre `rgb` (uten argumenter) vises en liste over tilgjengelige underkommandoer, for eksempel `grensesnitt`, `skjema`, `import`, `eksport`, `utstedelse`, `faktura`, `overføring` osv. Du kan endre den lokale lagringskatalogen (et lager som inneholder alle logger, skjemaer og implementasjoner), velge nettverk (testnet, mainnet) eller konfigurere Electrum-serveren din.

![RGB-Bitcoin](assets/fr/081.webp)

#### Første oversikt over kontroller

Når du kjører følgende kommando, vil du se at et `RGB20`-grensesnitt allerede er integrert som standard:

```bash
rgb interfaces
```

Hvis dette grensesnittet ikke er integrert, kloner du :

```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```

Kompilere den:

```bash
cargo run
```

Importer deretter grensesnittet du ønsker:

```bash
rgb import interfaces/RGB20.rgb
```

![RGB-Bitcoin](assets/fr/082.webp)

På den annen side får vi beskjed om at det ennå ikke er importert noe skjema til programvaren. Det finnes heller ingen kontrakt i lageret. For å se den, kjør kommandoen :

```bash
rgb schemata
```

Deretter kan du klone repositoryet for å hente ut bestemte skjemaer:

```bash
git clone https://github.com/RGB-WG/rgb-schemata
```

![RGB-Bitcoin](assets/fr/083.webp)

I katalogen `src/` inneholder dette depotet flere Rust-filer (for eksempel `nia.rs`) som definerer skjemaer (NIA for "*Non Inflatable Asset*", UDA for "*Unique Digital Asset*" osv.) For å kompilere kan du deretter kjøre :

```bash
cd rgb-schemata
cargo run
```

Dette genererer flere `.rgb`- og `.rgba`-filer som svarer til de kompilerte skjemaene. Du finner for eksempel `NonInflatableAsset.rgb`.

#### Import av skjema og grensesnittimplementering

Du kan nå importere skjemaet til `rgb` :

```bash
rgb import schemata/NonInflatableAssets.rgb
```

![RGB-Bitcoin](assets/fr/084.webp)

Dette legger det til i det lokale lageret. Hvis vi kjører følgende kommando, ser vi at skjemaet nå vises:

```bash
rgb schemata
```

### Opprettelse av kontrakt (utstedelse)

Det finnes to måter å opprette en ny ressurs på:


- Enten bruker vi et skript eller kode i Rust som bygger en kontrakt ved å fylle ut skjemafelter (global tilstand, Owned States osv.) og produserer en `.rgb`- eller `.rgba`-fil;
- Eller bruk underkommandoen `issue` direkte, med en YAML-fil (eller TOML) som beskriver tokenets egenskaper.

Du finner eksempler i Rust i mappen `examples`, som illustrerer hvordan du bygger en `ContractBuilder`, fyller inn `global state` (asset name, ticker, supply, date, etc.), definerer Owned State (hvilken UTXO den er tilordnet), og deretter kompilerer alt dette til en *contract consignment* som du kan eksportere, validere og importere til et stash.

Den andre måten er å redigere en YAML-fil manuelt for å tilpasse `ticker`, `name`, `supply`, og så videre. Anta at filen heter `RGB20-demo.yaml`. Du kan spesifisere :


- `spec`: ticker, navn, presisjon ;
- `terms`: et felt for juridiske merknader ;
- `issuedSupply` : mengden token som er utstedt;
- `assignments`: angir engangsforseglingen (*forseglingsdefinisjon*) og mengden som er låst opp.

Her er et eksempel på en YAML-fil som kan opprettes:

```yaml
interface: RGB20Fixed
globals:
spec:
ticker: PBN
name: Plan B Network
details: "Pay attention: the asset has no value"
precision: 2
terms:
text: >
SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
media: ~
issuedSupply: 100000000
assignments:
assetOwner:
seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
amount: 100000000 # this is 1 million (we have two digits for cents)
```

![RGB-Bitcoin](assets/fr/085.webp)

Deretter kjører du bare kommandoen :

```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```

![RGB-Bitcoin](assets/fr/086.webp)

I mitt tilfelle er den unike skjemaidentifikatoren (som skal være omsluttet av enkle anførselstegn) `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k`, og jeg har ikke lagt inn noen utsteder. Så bestillingen min er :

```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```

Hvis du ikke kjenner skjema-ID-en, kan du kjøre kommandoen :

```bash
rgb schemata
```

CLI svarer at en ny kontrakt er utstedt og lagt til i lageret. Hvis vi skriver inn følgende kommando, ser vi at det nå finnes en ekstra kontrakt som tilsvarer den som nettopp ble utstedt:

```bash
rgb contracts
```

![RGB-Bitcoin](assets/fr/087.webp)

Deretter viser den neste kommandoen de globale tilstandene (navn, ticker, forsyning ...) og listen over Owned States, dvs. allokeringer (for eksempel 1 million `PBN`-tokens definert i UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`).

```bash
rgb state '<ContractId>'
```

![RGB-Bitcoin](assets/fr/088.webp)

### Eksport, import og validering

Hvis du vil dele kontrakten med andre brukere, kan den eksporteres fra lageret til en :

```bash
rgb export '<ContractId>' myContractPBN.rgb
```

![RGB-Bitcoin](assets/fr/089.webp)

Filen `myContractPBN.rgb` kan sendes videre til en annen bruker, som kan legge den til sin stash med kommandoen :

```bash
rgb import myContractPBN.rgb
```

Ved import, hvis det er en enkel *kontraktsforsendelse*, får vi meldingen "`Importing consignment rgb`". Hvis det er en større *statovergangsforsendelse*, vil kommandoen være annerledes (`rgb accept`).

Du kan også bruke den lokale valideringsfunksjonen for å sikre gyldighet. Du kan for eksempel kjøre :

```bash
rgb validate myContract.rgb
```

#### Bruk, verifisering og visning av lagerbeholdning

Som en påminnelse er lageret en lokal beholdning av skjemaer, grensesnitt, implementasjoner og kontrakter (Genesis + overganger). Hver gang du kjører "import", legger du til et element i lageret. Dette lageret kan vises i detalj med kommandoen :

```bash
rgb dump
```

![RGB-Bitcoin](assets/fr/090.webp)

Dette vil generere en mappe med informasjon om hele lageret.

### Overføring og PSBT

For å gjennomføre en overføring må du manipulere en lokal Bitcoin-lommebok for å administrere `Tapret`- eller `Opret`-forpliktelsene.

#### Generer en faktura

I de fleste tilfeller foregår interaksjonen mellom deltakerne i en kontrakt (f.eks. Alice og Bob) ved at det genereres en faktura. Hvis Alice vil at Bob skal utføre noe (en tokenoverføring, en reutstedelse, en handling i en DAO osv.), oppretter Alice en faktura som beskriver instruksjonene hennes til Bob. Så vi har :


- Alice** (utstederen av fakturaen) ;
- Bob** (som mottar og utfører fakturaen).

I motsetning til andre økosystemer er en RGB-faktura ikke begrenset til betalingsbegrepet. Den kan inneholde en hvilken som helst forespørsel knyttet til kontrakten: tilbakekalle en nøkkel, stemme, opprette en gravering (*gravering*) på en NFT osv. Den tilsvarende operasjonen kan beskrives i kontraktsgrensesnittet. Den tilsvarende operasjonen kan beskrives i kontraktsgrensesnittet.

Følgende kommando genererer en RGB-faktura:

```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```

Med :


- `$CONTRACT`: Kontraktsidentifikator (*ContractId*) ;
- `$INTERFACE`: grensesnittet som skal brukes (f.eks. `RGB20`) ;
- `$ACTION`: navnet på operasjonen som er angitt i grensesnittet (for en enkel fungibel tokenoverføring kan dette være "Transfer"). Hvis grensesnittet allerede har en standardhandling, trenger du ikke å oppgi den igjen her;
- `$STATE`: statusdataene som skal overføres (for eksempel en mengde tokens hvis en fungibel token overføres);
- `$SEAL`: mottakerens (Alices) engangsforsegling, dvs. en eksplisitt referanse til en UTXO. Bob vil bruke denne informasjonen til å lage vitnetransaksjonen, og den tilsvarende utdataen vil da tilhøre Alice (i *blindet UTXO* eller ukryptert form).

For eksempel med følgende kommandoer

```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```

CLI vil generere en faktura som :

```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```

Den kan sendes til Bob via en hvilken som helst kanal (tekst, QR-kode osv.).

#### Foreta en overføring

For å overføre fra denne fakturaen :


- Bob (som har tokens i sin stash) har en Bitcoin-lommebok. Han må forberede en Bitcoin-transaksjon (i form av en PSBT, f.eks. `tx.psbt`) som bruker UTXOene der de nødvendige RGB-tokens befinner seg, pluss én UTXO for valuta (veksling);
- Bob utfører følgende kommando:

```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```


- Dette genererer en `consignment.rgb`-fil som inneholder :
 - Overgangshistorikken beviser for Alice at symbolene er ekte;
 - Den nye overgangen som overfører tokens til Alice's Single-use Seal ;
 - En vitnetransaksjon (usignert).
- Bob sender denne `consignment.rgb`-filen til Alice (via e-post, en delingsserver eller en RGB-RPC-protokoll, Storm, etc.);
- Alice mottar `consignment.rgb` og aksepterer det i sin egen stash :

```bash
alice$ rgb accept consignment.rgb
```


- CLI kontrollerer gyldigheten av overgangen og legger den til i Alices lager. Hvis den er ugyldig, mislykkes kommandoen med en detaljert feilmelding. Hvis ikke, lykkes den, og rapporterer at eksempeltransaksjonen ennå ikke har blitt kringkastet på Bitcoin-nettverket (Bob venter på grønt lys fra Alice);
- Som bekreftelse returnerer kommandoen `accept` en signatur (*betalingsslipp*) som Alice kan sende til Bob for å vise ham at hun har godkjent *forsendelsen* ;
- Bob kan deretter signere og publisere (`--publisere`) sin Bitcoin-transaksjon:

```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```


- Så snart denne transaksjonen er bekreftet i kjeden, anses eierskapet til eiendelen som overført til Alice. Alices lommebok, som overvåker transaksjonens utvinning, ser den nye Owned State dukke opp i sin stash.

I neste kapittel skal vi se nærmere på integreringen av RGB i Lightning Network.

## RGB på Lightning-nettverket

<chapterId>0962980a-8f94-5d0f-9cd0-43d7f884a01d</chapterId>

![video](https://youtu.be/mqCupTlDbA0)

I dette kapittelet foreslår jeg å undersøke hvordan RGB kan brukes i Lightning Network til å integrere og flytte RGB-aktiva (tokens, NFT-er osv.) via betalingskanaler utenfor kjeden.

Den grunnleggende ideen er at RGB-tilstandsovergangen (*State Transition*) kan overføres til en Bitcoin-transaksjon, som i sin tur kan forbli utenfor kjeden til Lightning-kanalen er stengt. Så hver gang kanalen oppdateres, kan en ny RGB-statusovergang inkorporeres i den nye transaksjonen, som deretter ugyldiggjør den gamle overgangen. På denne måten kan Lightning-kanaler brukes til å overføre RGB-eiendeler, og de kan rutes på samme måte som konvensjonelle Lightning-betalinger.

### Opprettelse og finansiering av kanaler

For å opprette en Lightning-kanal som inneholder RGB-ressurser, trenger vi to elementer:


- Bitcoin-finansiering for å opprette kanalens 2/2 multisig (kanalens grunnleggende UTXO);
- RGB-finansiering, som sender ressurser til samme multisig.

I Bitcoin-termer må finansieringstransaksjonen eksistere for å definere UTXO-referansen, selv om den bare inneholder en liten mengde sats (det er bare et spørsmål om at hver utgang i fremtidige forpliktelsestransaksjoner likevel forblir over støvgrensen). Alice kan for eksempel bestemme seg for å levere 10 000 sats og 500 USDT (utstedt som en RGB-aktiva). I finansieringstransaksjonen legger vi til en forpliktelse (`Opret` eller `Tapret`) som forankrer RGB-tilstandsovergangen.

![RGB-Bitcoin](assets/fr/091.webp)

Når finansieringstransaksjonen er klargjort (men ennå ikke kringkastet), opprettes forpliktelsestransaksjoner slik at hver av partene kan stenge kanalen ensidig når som helst. Disse transaksjonene ligner Lightnings klassiske forpliktelsestransaksjoner, bortsett fra at vi legger til en ekstra utgang som inneholder RGB-ankeret (OP_RETURN eller Taproot) som er knyttet til den nye tilstandsovergangen.

RGB-tilstandsovergangen flytter deretter aktivaene fra 2/2 multisig av finansieringen til utgangene av forpliktelsestransaksjonen. Fordelen med denne prosessen er at sikkerheten i RGB-tilstanden samsvarer nøyaktig med Lightnings straffemekanikk: Hvis Bob sender ut en gammel kanaltilstand, kan Alice straffe ham og bruke utdataene for å få tilbake både satsene og RGB-tokens. Insentivet er derfor enda sterkere enn i en Lightning-kanal uten RGB-aktiva, siden en angriper ikke bare kan miste satsene, men også kanalens RGB-aktiva.

En forpliktelsestransaksjon signert av Alice og sendt til Bob vil derfor se slik ut:

![RGB-Bitcoin](assets/fr/092.webp)

Og den medfølgende forpliktelsestransaksjonen, signert av Bob og sendt til Alice, vil se slik ut:

![RGB-Bitcoin](assets/fr/093.webp)

### Kanaloppdatering

Når det skjer en betaling mellom to kanaldeltakere (eller de ønsker å endre aktivaallokeringen), oppretter de et nytt par forpliktelsestransaksjoner. Beløpet i sats på hver utgang kan forbli uendret eller ikke, avhengig av implementeringen, siden hovedrollen er å muliggjøre konstruksjon av gyldige UTXO-er. På den annen side må OP_RETURN-utgangen (eller Taproot-utgangen) modifiseres slik at den inneholder det nye RGB-ankeret, som representerer den nye fordelingen av aktiva i kanalen.

Hvis Alice for eksempel overfører 30 USDT til Bob i kanalen, vil den nye tilstandsovergangen gjenspeile en saldo på 400 USDT for Alice og 100 USDT for Bob. Commit-transaksjonen legges til (eller endres av) OP_RETURN/Taproot-ankeret for å inkludere denne overgangen. Merk at fra RGBs synspunkt forblir inngangen til overgangen den opprinnelige multisig (der aktiva i kjeden faktisk allokeres frem til kanalen lukkes). Det er bare RGB-utdataene (allokeringene) som endres, avhengig av hvilken omfordeling som besluttes.

Forpliktelsestransaksjonen er signert av Alice og klar til å distribueres av Bob :

![RGB-Bitcoin](assets/fr/094.webp)

Forpliktelsestransaksjonen er signert av Bob og klar til å distribueres av Alice :

![RGB-Bitcoin](assets/fr/095.webp)

### HTLC-styring

I virkeligheten gjør Lightning Network det mulig å dirigere betalinger via flere kanaler ved hjelp av HTLC-er (*Hashed Time-Locked Contracts*). Det er det samme med RGB: For hver betaling som går gjennom kanalen, legges det til en HTLC-utgang til den forpliktende transaksjonen, og en RGB-tildeling knyttet til denne HTLC-en. Dermed får den som bruker HTLC-utgangen (takket være hemmeligheten eller etter utløpet av tidslåsen) tilbake både satsene og de tilknyttede RGB-eiendelene. På den annen side må du selvsagt ha nok penger på veien i form av både sats- og RGB-eiendeler.

![RGB-Bitcoin](assets/fr/096.webp)

Driften av RGB på Lightning må derfor vurderes parallelt med driften av selve Lightning-nettverket. Hvis du ønsker å fordype deg i dette emnet, anbefaler jeg at du tar en titt på dette andre omfattende kurset:

https://planb.network/courses/lnp201
### RGB-kodekart

Før jeg går videre til neste avsnitt, vil jeg til slutt gi deg en oversikt over koden som brukes i RGB. Protokollen er basert på et sett med Rust-biblioteker og spesifikasjoner med åpen kildekode. Her er en oversikt over de viktigste repositoriene og crates:

![RGB-Bitcoin](assets/fr/097.webp)

#### Validering på klientsiden


- Repository**: [klient_side_validering](https://github.com/LNP-BP/client_side_validation)
- Kasser** : [klientsidevalidering](https://crates.io/crates/client_side_validation), [single_use_seals](https://crates.io/crates/single_use_seals)

Håndtering av validering utenfor kjeden og logikk for engangsplomber.

#### Deterministiske Bitcoin-forpliktelser (DBC)


- Repository**: [bp-core](https://github.com/BP-WG/bp-core)
- Kasse**: [bp-dbc](https://crates.io/crates/bp-dbc)

Håndtering av deterministisk forankring i Bitcoin-transaksjoner (Tapret, OP_RETURN osv.).

#### Multiprotokollforpliktelse (MPC)


- Repository**: [klient_side_validering](https://github.com/LNP-BP/client_side_validation)
- Kasse** : [commit_verify](https://crates.io/crates/commit_verify)

Flere engasjementskombinasjoner og integrering med ulike protokoller.

#### Strenge typer og streng koding


- Spesifikasjoner**: [nettsted strict-types.org] (https://www.strict-types.org/)
- Repositorier**: [strict-types](https://github.com/strict-types/strict-types), [strict-encoding](https://github.com/strict-types/strict-encoding)
- Kasser** : [strict_types](https://crates.io/crates/strict_types), [strict_encoding](https://crates.io/crates/strict_encoding)

Det strenge typingssystemet og den deterministiske serialiseringen som brukes for validering på klientsiden.

#### RGB-kjerne


- Repository**: [rgb-core](https://github.com/RGB-WG/rgb-core)
- Kasse**: [rgb-core](https://crates.io/crates/rgb-core)

Kjernen i protokollen, som omfatter hovedlogikken i RGB-valideringen.

#### RGB standardbibliotek og lommebok


- Repository**: [rgb-std](https://github.com/RGB-WG/rgb-std)
- Kasse** : [rgb-std](https://crates.io/crates/rgb-std)

Standardimplementeringer, stash- og lommebokadministrasjon.

#### RGB CLI


- Repository**: [rgb](https://github.com/RGB-WG/rgb)
- Kasser**: [rgb-cli](https://crates.io/crates/rgb-cli), [rgb-wallet](https://crates.io/crates/rgb-wallet)

`rgb` CLI og crate wallet, for kommandolinjemanipulering av kontrakter.

#### RGB-skjema


- Repository**: [rgb-schemata](https://github.com/RGB-WG/rgb-schemata/)

Inneholder eksempler på skjemaer (NIA, UDA osv.) og implementeringer av disse.

#### ALuVM


- Info** : [aluvm.org](https://www.aluvm.org/)
- Repositorier**: [aluvm-spec](https://github.com/AluVM/aluvm-spec), [alure](https://github.com/AluVM/alure)
- Kasser**: [aluvm](https://crates.io/crates/aluvm), [aluasm](https://crates.io/crates/aluasm)

Registerbasert virtuell maskin som brukes til å kjøre valideringsskript.

#### Bitcoin-protokollen - BP


- Repositorier** : [bp-core](https://github.com/BP-WG/bp-core), [bp-std](https://github.com/BP-WG/bp-std), [bp-wallet](https://github.com/BP-WG/bp-wallet)

Tillegg for å støtte Bitcoin-protokollen (transaksjoner, omgåelser osv.).

#### Allestedsnærværende deterministisk databehandling - UBIDECO


- Repository**: [UBIDECO](https://github.com/UBIDECO)

Økosystem knyttet til deterministisk utvikling med åpen kildekode.

# Bygger på RGB

<partId>3b4b0d66-0c1b-505a-b5ca-4b2e57dd73c2</partId>

## DIBA og Bitmask-prosjektet

<chapterId>dc92a5e8-ed93-5a3f-bcd0-d433932842f4</chapterId>

![video](https://youtu.be/nbUtV8GOR_U)

Denne siste delen av kurset er basert på presentasjoner holdt av ulike foredragsholdere på RGB-bootcampen. Her finner du uttalelser og refleksjoner om RGB og dets økosystem, samt presentasjoner av verktøy og prosjekter basert på protokollen. Dette første kapittelet er moderert av Hunter Beast, og de to neste av Frederico Tenga.

### Fra JavaScript til Rust, og inn i Bitcoin-økosystemet

Til å begynne med jobbet Hunter Beast hovedsakelig i JavaScript. Så oppdaget han **Rust**, hvis syntaks til å begynne med virket lite tiltalende og frustrerende. Men etter hvert begynte han å sette pris på kraften i språket, kontrollen over minnet (*heap* og *stack*), samt sikkerheten og ytelsen som følger med. Han understreker at Rust er et utmerket treningsgrunnlag for å få en grundig forståelse av hvordan en datamaskin fungerer.

Hunter Beast forteller om sin bakgrunn i ulike prosjekter i *altcoin*-økosystemet, som Ethereum (med Solidity, TypeScript osv.), og senere Filecoin. Han forklarer at han i utgangspunktet var imponert over noen av protokollene, men endte opp med å bli desillusjonert av de fleste av dem, ikke minst på grunn av deres tokenomikk. Han fordømmer de tvilsomme økonomiske insentivene, den inflatoriske opprettelsen av tokens som utvanner investorer, og det potensielt utnyttende aspektet ved disse prosjektene. Så han endte opp med å innta en **Bitcoin-maksimalist**-holdning, ikke minst fordi noen mennesker åpnet øynene hans for Bitcoins sunnere økonomiske mekanismer, og for robustheten i dette systemet.

### Det attraktive med RGB og å bygge på lag

Det som definitivt overbeviste ham om Bitcoins relevans, var oppdagelsen av RGB og konseptet med lag. Han mener at eksisterende funksjonalitet på andre blokkjeder kan reproduseres på høyere lag, over Bitcoin, uten å endre den grunnleggende protokollen.

I februar 2022 begynte han i **DIBA** for å jobbe spesifikt med RGB, og spesielt med lommeboken **Bitmask**. På den tiden var Bitmask fortsatt i versjon 0.01 og kjørte RGB i versjon 0.4, kun for håndtering av enkelttokens. Han bemerker at dette var mindre selvforvaringsorientert enn i dag, ettersom logikken delvis var serverbasert. Siden den gang har arkitekturen utviklet seg i retning av denne modellen, noe bitcoinere setter stor pris på.

### Grunnlaget for RGB-protokollen

**RGB**-protokollen er den nyeste og mest avanserte utførelsen av _fargede mynter_-konseptet, som ble utforsket allerede rundt 2012-2013. På den tiden var det flere team som ønsket å knytte ulike bitcoinverdier til UTXO-er, noe som førte til flere spredte implementeringer. Mangelen på standardisering og den lave etterspørselen på den tiden hindret disse løsningene i å få varig fotfeste.

I dag skiller RGB seg ut med sin konseptuelle robusthet og enhetlige spesifikasjoner via LNP/BP-forbindelsen. Prinsippet er basert på validering på klientsiden. Bitcoin-blokkjeden lagrer bare kryptografiske forpliktelser (_commitments_, via Taproot eller OP_RETURN), mens mesteparten av dataene (kontraktsdefinisjoner, overføringshistorikk osv.) lagres av de berørte brukerne. På denne måten fordeles lagringsbelastningen og konfidensialiteten til utvekslingene forsterkes, uten å tynge blokkjeden. Denne tilnærmingen gjør det mulig å opprette fungible eiendeler (**RGB20**-standarden) eller unike eiendeler (**RGB21**-standarden), innenfor et modulært og skalerbart rammeverk.

### Token-funksjonen (RGB20) og unike eiendeler (RGB21)

Med **RGB20** definerer vi et fungibelt token på Bitcoin. Utstederen velger en _forsyning_, en _presisjon_, og oppretter en _kontrakt_ der han deretter kan foreta overføringer. Hver overføring refereres til en Bitcoin UTXO, som fungerer som en *Single-use Seal*. Denne logikken sikrer at brukeren ikke kan bruke den samme eiendelen to ganger, siden bare den personen som er i stand til å bruke UTXO-en, faktisk har nøkkelen til å oppdatere tilstanden til kontrakten på klientsiden.

**RGB21** retter seg mot unike ressurser (eller "NFT"). Eiendelen har et tilbud på 1, og kan knyttes til metadata (bildefil, lyd osv.) som beskrives via et bestemt felt. I motsetning til NFT-er på offentlige blokkjeder kan data og deres MIME-identifikatorer forbli private og distribueres peer-to-peer etter eierens skjønn.

### Bitmask-løsningen: en lommebok for RGB

For å utnytte RGBs muligheter i praksis har **DIBA**-prosjektet utviklet en lommebok kalt [Bitmask] (https://bitmask.app/). Tanken er å tilby et Taproot-basert verktøy som ikke er depotbasert, og som er tilgjengelig som en webapplikasjon eller nettleserutvidelse. Bitmask håndterer både RGB20- og RGB21-aktiva og integrerer ulike sikkerhetsmekanismer:


- Kjernekoden er skrevet i Rust, og deretter kompilert i WebAssembly for å kjøre i et JavaScript-miljø (React);
- Nøklene genereres lokalt, og lagres deretter kryptert lokalt;
- Tilstandsdata (stash) lagres i minnet, serialiseres og krypteres via **Carbonado**-biblioteket, som utfører komprimering, feilretting, kryptering og strømverifisering ved hjelp av Blake3.

Takket være denne arkitekturen foregår alle aktivatransaksjoner på klientsiden. Fra utsiden er Bitcoin-transaksjonen ikke noe annet enn en klassisk Taproot-utgiftstransaksjon, som ingen vil mistenke at også bærer en overføring av fungible tokens eller NFT-er. Fraværet av overbelastning i kjeden (ingen offentlig lagrede metadata) garanterer en viss grad av diskresjon og gjør det lettere å motstå mulige sensurforsøk.

### Sikkerhet og distribuert arkitektur

Ettersom RGB-protokollen krever at hver deltaker beholder sin transaksjonshistorikk (for å bevise gyldigheten av overføringene den mottar), oppstår spørsmålet om lagring. Bitmask foreslår å serialisere dette lageret lokalt, og deretter sende det til flere servere eller skyer (valgfritt). Dataene forblir kryptert av brukeren via **Carbonado**, slik at en server ikke kan lese dem. I tilfelle delvis korrupsjon kan feilkorreksjonslaget rekonstruere innholdet.

Bruken av CRDT (_Conflict-free replicated data type_) gjør det mulig å slå sammen ulike versjoner av lageret hvis de avviker fra hverandre. Alle står fritt til å lagre disse dataene der de ønsker, ettersom ingen enkelt node inneholder all informasjon knyttet til ressursen. Dette gjenspeiler *Client-side Validation*-filosofien, der hver eier er ansvarlig for å lagre bevis på gyldigheten til RGB-aktivaen sin.

### Mot et bredere økosystem: markedsplass, interoperabilitet og nye funksjoner

Selskapet bak Bitmask begrenser seg ikke til å utvikle en lommebok. DIBA har til hensikt å utvikle :


- En **markedsplass** for utveksling av tokens, særlig i **RGB21**-form;
- Kompatibilitet med andre lommebøker (for eksempel *Iris Wallet*);
- Teknikker for batching** av overføringer, dvs. muligheten for å inkludere flere påfølgende RGB-overføringer i én enkelt transaksjon.

Samtidig jobber vi med **WebBTC** eller **WebLN** (standarder som gjør det mulig for nettsteder å be lommeboken om å signere Bitcoin- eller Lightning-transaksjoner), samt med muligheten til å "teleburnere" Ordinals-oppføringer (hvis vi ønsker å repatriere Ordinals til et mer diskret og fleksibelt RGB-format).

### Konklusjon

Hele prosessen viser hvordan RGB-økosystemet kan distribueres og gjøres tilgjengelig for sluttbrukere gjennom robuste tekniske løsninger. Overgangen fra et altcoin-perspektiv til en mer Bitcoin-sentrisk visjon, kombinert med oppdagelsen av * Client-side Validation *, illustrerer en ganske logisk vei: vi forstår at det er mulig å implementere forskjellige funksjoner (fungible tokens, NFT, smarte kontrakter ...) uten å gafle blockchain, ganske enkelt ved å dra nytte av kryptografiske forpliktelser på Taproot-transaksjoner eller OP_RETURNs.

Lommeboken **Bitmask** er en del av denne tilnærmingen: på blockchain-siden er alt du ser en vanlig Bitcoin-transaksjon; på brukersiden manipulerer du et webgrensesnitt der du oppretter, bytter og lagrer alle slags eiendeler utenfor kjeden. Denne modellen skiller tydelig den monetære infrastrukturen (Bitcoin) fra utstedelses- og overføringslogikken (RGB), samtidig som den sikrer et høyt konfidensialitetsnivå og bedre skalerbarhet.

## Bitfinex' arbeid med RGB

<chapterId>d4d80e07-5eac-5b29-a93a-123180e97047</chapterId>

![vidéo](https://youtu.be/5iAhsgCSL3U)

I dette kapittelet, som er basert på en presentasjon av Frederico Tenga, ser vi på et sett med verktøy og prosjekter som er opprettet av Bitfinex-teamet dedikert til RGB, med sikte på å fremme fremveksten av et rikt og mangfoldig økosystem rundt denne protokollen. Teamets opprinnelige mål er ikke å lansere et spesifikt kommersielt produkt, men snarere å tilby programvarebyggesteiner, bidra til selve RGB-protokollen og foreslå konkrete implementeringsreferanser, for eksempel en mobil lommebok (* Iris Wallet*) eller en RGB-kompatibel Lightning-node.

### Bakgrunn og mål

Siden rundt 2022 har Bitfinex RGB-teamet konsentrert seg om å utvikle teknologistakken som gjør det mulig å utnytte og teste RGB på en effektiv måte. Flere bidrag har blitt gitt:


- Deltakelse i kildekode- og protokollspesifikasjoner, inkludert skriving av forbedringsforslag, feilretting osv;
- Verktøy for utviklere som forenkler integreringen av RGB i applikasjonene deres;
- Utforming av en mobil lommebok med navnet [Iris] (https://iriswallet.com/) for å eksperimentere og illustrere beste praksis for bruk av RGB ;
- Opprettelse av en tilpasset Lightning-node som kan håndtere kanaler med RGB-ressurser;
- Støtte andre team som bygger løsninger på RGB, for å oppmuntre til mangfold og et sterkt økosystem.

Denne tilnærmingen tar sikte på å dekke hele behovskjeden: fra lavnivåbiblioteket (*[RGBlib](https://github.com/RGB-Tools/rgb-lib)*), som gjør det mulig å implementere en lommebok, til produksjonsaspektet (en Lightning-node, en lommebok for Android osv.).

### RGBlib-biblioteket: forenkler utviklingen av RGB-applikasjoner

Et viktig poeng i demokratiseringen av RGB-lommebøker og -applikasjoner er å gjøre tilgjengelig en abstraksjon som er enkel nok til at utviklere ikke trenger å lære seg alt om protokollens interne logikk. Dette er nettopp målet med **RGBlib**, skrevet i Rust.

RGBlib fungerer som en bro mellom de svært fleksible (men til tider komplekse) kravene til RGB som vi har studert i de foregående kapitlene, og de konkrete behovene til en applikasjonsutvikler. Med andre ord kan en lommebok (eller tjeneste) som ønsker å administrere tokenoverføringer, utstedelse av aktiva, verifisering osv., stole på RGBlib uten å kjenne til alle kryptografiske detaljer eller alle RGB-parametere som kan tilpasses.

Bokhandelen tilbyr :


- Nøkkelferdige funksjoner for utstedelse (_utstedelse_) av eiendeler (fungible eller ikke);
- Muligheten til å overføre (sende/motta) eiendeler ved å manipulere enkle objekter (adresser, beløp, UTXO-er osv.);
- En mekanisme for lagring og innlasting av statusinformasjonen (*konsigneringer*) som kreves for validering på klientsiden.

RGBlib er derfor avhengig av komplekse begreper som er spesifikke for RGB (validering på klientsiden, Tapret/Opret-ankre), men innkapsler dem slik at den endelige applikasjonen ikke trenger å omprogrammere alt eller ta risikable beslutninger. I tillegg er RGBlib allerede bundet i flere språk (Kotlin og Python), noe som åpner for bruksområder utover et enkelt Rust-univers.

### Iris Wallet: et eksempel på en RGB-lommebok på Android

For å bevise effektiviteten til RGBlib har Bitfinex-teamet utviklet **Iris Wallet**, utelukkende på Android på dette stadiet. Det er en mobil lommebok som illustrerer en brukeropplevelse som ligner på en vanlig Bitcoin-lommebok: du kan utstede en eiendel, sende den, motta den og se historikken, samtidig som du forblir på en selvforvaringsmodell.

Iris har en rekke interessante funksjoner:

**Bruk av en Electrum-server:**

Som enhver lommebok trenger Iris å vite om transaksjonsbekreftelser på blokkjeden. I stedet for å bygge inn en komplett node, bruker Iris som standard en Electrum-server som vedlikeholdes av Bitfinex-teamet. Brukere kan imidlertid konfigurere sin egen server eller en annen tredjepartstjeneste. På denne måten kan Bitcoin-transaksjoner valideres og informasjon hentes (indeksering) på en modulær måte.

**RGB-proxy-serveren:**

I motsetning til Bitcoin krever RGB utveksling av metadata utenfor kjeden (*consignments*) mellom avsender og mottaker. For å forenkle denne prosessen tilbyr Iris en løsning der kommunikasjonen foregår via en proxy-server. Mottakerlommeboken genererer en *faktura* som nevner hvor avsenderen skal sende dataene på *klientsiden*. Som standard peker URL-en til en proxy som Bitfinex-teamet er vert for, men du kan endre denne proxyen (eller være vert for din egen). Tanken er å gå tilbake til en kjent brukeropplevelse der mottakeren viser en QR-kode, og avsenderen skanner denne koden for transaksjonen, uten noen komplekse tilleggsmanipulasjoner.

**Kontinuerlig sikkerhetskopiering:**

I en ren Bitcoin-sammenheng er det vanligvis tilstrekkelig å ta sikkerhetskopi av seed (selv om vi i disse dager anbefaler å ta sikkerhetskopi av seed og deskriptorer i stedet). Med RGB er ikke dette nok: Du må også ta vare på den lokale historikken (*sendinger*) som beviser at du virkelig eier en RGB-eiendel. Hver gang du mottar en kvittering, lagrer enheten nye data, noe som er avgjørende for senere utgifter. Iris administrerer automatisk en kryptert sikkerhetskopi i brukerens Google Disk. Dette krever ingen spesiell tillit til Google, ettersom sikkerhetskopien er kryptert, og mer robuste alternativer (for eksempel en personlig server) er planlagt for fremtiden for å unngå enhver risiko for sensur eller sletting av en tredjepartsoperatør.

**Andre funksjoner:**


- Opprett en kran for raskt å teste eller distribuere tokens for eksperimentering eller markedsføring;
- Et sertifiseringssystem (for øyeblikket sentralisert) for å skille et legitimt token fra et falskt som kopierer en berømt ticker. I fremtiden kan denne sertifiseringen bli mer desentralisert (via DNS eller andre mekanismer).

Alt i alt tilbyr Iris en brukeropplevelse som ligger nær en klassisk Bitcoin-lommebok, og maskerer den ekstra kompleksiteten (stash management, *consignment*-historikk osv.) takket være RGBlib og bruk av en proxy-server.

### Proxy-server og brukeropplevelse

Proxy-serveren som ble introdusert ovenfor, fortjener å bli beskrevet i detalj, ettersom den er nøkkelen til en smidig brukeropplevelse. I stedet for at avsenderen manuelt må overføre *forsendelsene* til mottakeren, foregår RGB-transaksjonen i bakgrunnen via en :


- Mottakeren genererer en *faktura* (som blant annet inneholder proxy-adressen);
- Avsenderen sender (via en HTTP-forespørsel) et overgangsprosjekt (*oppdraget*) til proxyen ;
- Mottakeren henter dette prosjektet og utfører valideringen på *klientsiden* lokalt;
- Mottakeren publiserer deretter, via proxyen, aksept (eller eventuelt avvisning) av tilstandsovergangen ;
- Avsenderen kan se valideringsstatusen og, hvis den aksepteres, sende Bitcoin-transaksjonen som fullfører overføringen.

På denne måten oppfører lommeboken seg nesten som en vanlig lommebok. Brukeren er uvitende om alle mellomtrinnene. Riktignok er den nåværende proxyen verken kryptert eller autentisert (noe som gir bekymringer om konfidensialitet og integritet), men disse forbedringene er mulige i senere versjoner. Proxy-konseptet er fortsatt ekstremt nyttig for å gjenskape "jeg sender en QR-kode, du skanner for å betale"-opplevelsen.

### RGB-integrering på Lightning Network

Et annet hovedfokus i Bitfinex-teamets arbeid er å gjøre Lightning-nettverket kompatibelt med RGB-aktiva. Målet er å muliggjøre Lightning-kanaler i USDT (eller andre token), og å dra nytte av de samme fordelene som bitcoin på Lightning (nesten øyeblikkelige transaksjoner, ruting osv.). Konkret innebærer dette å opprette en Lightning-node som er modifisert til :


- Åpne en kanal ved å plassere ikke bare satoshier, men også en eller flere RGB-ressurser i finansieringen UTXO multisig ;
- Generer Lightning-forpliktelsestransaksjoner (Bitcoin-siden) ledsaget av tilsvarende RGB-tilstandsoverganger. Hver gang kanalen oppdateres, omdefinerer en RGB-overgang aktivadistribusjonen i Lightning-utgangene;
- Muliggjør ensidig stenging, der eiendelen hentes i en eksklusiv UTXO, i samsvar med Lightning Network-regler (HTLC, tidslås, straff osv.).

Denne løsningen, kalt "**RGB Lightning Node**", bruker LDK (*Lightning Dev Kit*) som base, og legger til mekanismene som trengs for å injisere RGB-tokens i kanalene. Lightning-forpliktelser beholder den klassiske strukturen (punkterbare utganger, tidslås ...), og i tillegg forankres en RGB-tilstandsovergang (via `Opret` eller `Tapret`). For brukeren åpner dette veien til Lightning-kanaler i stablecoins eller i andre aktiva som sendes ut via RGB.

### DEX-potensial og innvirkning på Bitcoin

Når flere aktiva forvaltes via Lightning, blir det mulig å tenke seg en **atomisk børs** på én enkelt Lightning-rutebane, med samme logikk for hemmeligheter og tidslås. Bruker A har for eksempel bitcoin på én Lightning-kanal, og bruker B har USDT RGB på en annen Lightning-kanal. De kan bygge en sti mellom de to kanalene og samtidig bytte BTC mot USDT, uten behov for tillit. Dette er ikke noe annet enn et **atomisk bytte** som foregår i flere hopp, noe som gjør at eksterne deltakere nesten ikke legger merke til at de foretar en handel, ikke bare en ruting. Denne tilnærmingen tilbyr :


- Svært lav ventetid, ettersom alt forblir utenfor kjeden på Lightning.
- En overlegen **privatliv**: ingen vet at det er en handel, og ikke en normal ruting ;
- Unngå frontrunning, et tilbakevendende problem for DEX på kjeden ;
- Reduserte kostnader (du betaler ikke blokkplass, bare avgifter for lynruting).

Vi kan da se for oss et økosystem der Lightning-noder tilbyr byttepriser (ved å tilby likviditet). Hver node kan, hvis den ønsker det, spille rollen som _markedsprodusent_ og kjøpe og selge ulike aktiva på Lightning. Disse utsiktene til en _layer-2_ DEX forsterker ideen om at det ikke er nødvendig å forke eller bruke tredjeparts blokkjeder for å oppnå desentraliserte aktivabørser.

Virkningen på Bitcoin kan være positiv: Lightnings infrastruktur (noder, kanaler og tjenester) vil bli mer fullt utnyttet takket være volumene som genereres av disse *stablecoins*, derivater og andre tokens. Forhandlere som er interessert i USDT-betalinger på Lightning, vil mekanisk oppdage BTC-betalinger på Lightning (administrert av den samme stakken). Vedlikehold og finansiering av Lightning Network-infrastrukturen kan også dra nytte av multiplikasjonen av disse ikke-BTC-strømmene, noe som indirekte vil komme Bitcoin-brukere til gode.

### Konklusjon og ressurser

Bitfinex-teamet dedikert til RGB illustrerer gjennom sitt arbeid mangfoldet av hva som kan gjøres på toppen av protokollen. På den ene siden er det RGBlib, et bibliotek som letter utformingen av lommebøker og applikasjoner. På den andre siden har vi Iris Wallet, en praktisk demonstrasjon på Android av et pent sluttbrukergrensesnitt. Til slutt viser integrasjonen av RGB med Lightning at stablecoin-kanaler er mulig, og åpner veien for en potensiell desentralisert DEX på Lightning.

Denne tilnærmingen er i stor grad eksperimentell og fortsetter å utvikle seg: RGBlib-biblioteket blir forbedret underveis, Iris Wallet får jevnlige forbedringer, og den dedikerte Lightning-noden er ennå ikke en vanlig Lightning-klient.

For de som ønsker å lære mer eller bidra, finnes det flere ressurser tilgjengelig, blant annet :


- [GitHub RGB Tools repositories] (https://github.com/RGB-Tools);
- [Et informasjonsnettsted dedikert til Iris Wallet] (https://iriswallet.com/) for å teste lommeboken på Android.

I neste kapittel skal vi se nærmere på hvordan du starter en RGB Lightning-node.

## RLN - RGB Lightning Node

<chapterId>ecaabe32-20ba-5f8c-8ca1-a3f095792958</chapterId>

![vidéo](https://youtu.be/piQQH4Q2nr0)

I dette siste kapittelet tar Frederico Tenga deg steg for steg gjennom oppsettet av en Lightning RGB-node i et Regtest-miljø, og viser deg hvordan du oppretter RGB-tokens på den. Ved å starte to separate noder kan du også se hvordan du åpner en Lightning-kanal mellom dem og utveksler RGB-aktiva.

Denne videoen fungerer som en veiledning, på samme måte som i et tidligere kapittel, men denne gangen fokuserer vi spesielt på Lightning!

Hovedressursen for denne videoen er Github-arkivet [RGB Lightning Node] (https://github.com/RGB-Tools/rgb-lightning-node), som gjør det enkelt for deg å starte denne konfigurasjonen i Regtest.

### Utplassering av en RGB-kompatibel Lightning-node

Prosessen tar opp i seg og omsetter i praksis alle konseptene som er gjennomgått i de foregående kapitlene:


- Ideen om at **UTXO ** blokkert på en 2/2 multisig av en lynkanal kan motta ikke bare bitcoins, men også være en engangsforsegling av RGB-eiendeler (fungible eller ikke) ;
- I hver Lightning-transaksjon legges det til en utgang (`Tapret` eller `Opret`) som er dedikert til å forankre RGB-tilstandsovergangen;
- Den tilhørende infrastrukturen (bitcoind/indexer/proxy) for å validere Bitcoin-transaksjoner og utveksle *klient-side*-data.

### Vi introduserer rgb-lightning-node

**`rgb-lightning-node`**-prosjektet er en Rust-demon basert på en `rust-lightning` (LDK)-gaffel som er modifisert for å ta hensyn til eksistensen av RGB-ressurser i en kanal. Når en kanal åpnes, kan tilstedeværelsen av ressurser spesifiseres, og hver gang kanaltilstanden oppdateres, opprettes en RGB-overgang som gjenspeiler fordelingen av ressursen i Lightning-utgangene. Dette muliggjør :


- Åpne Lightning-kanaler i USDT, for eksempel;
- Rute disse tokens gjennom nettverket, forutsatt at rutingsstiene har tilstrekkelig likviditet;
- Utnytt Lightnings straffe- og tidslås-logikk uten endringer: RGB-overgangen forankres ganske enkelt i en ekstra utgang fra forpliktelsestransaksjonen.

Koden er fortsatt på alfa-stadiet: Vi anbefaler at du bare bruker den i **regtest** eller på **testnet**.

### Installasjon av noder

For å kompilere og installere `rgb-lightning-node`-binærfilen, starter vi med å klone repositoryet og dets undermoduler, og deretter kjører vi :

```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```

![RGB-Bitcoin](assets/fr/098.webp)


- Alternativet `--recurse-submodules` kloner også de nødvendige underenhetene (inkludert den modifiserte versjonen av `rust-lightning`);
- Alternativet `--shallow-submodules` begrenser dybden på klonen for å gjøre nedlastingen raskere, samtidig som det gir tilgang til viktige commits.

Kjør følgende kommando fra prosjektroten for å kompilere og installere binærfilen :

```bash
cargo install --locked --debug --path .
```

![RGB-Bitcoin](assets/fr/099.webp)


- `--locked` sikrer at versjonen av avhengighetene overholdes strengt;
- `--debug` er ikke obligatorisk, men kan hjelpe deg med å fokusere (du kan bruke `--release` hvis du foretrekker det);
- `--path .` forteller `cargo install` å installere fra den aktuelle katalogen.

På slutten av denne kommandoen vil en kjørbar `rgb-lightning-node` være tilgjengelig i din `$CARGO_HOME/bin/`. Sørg for at denne stien ligger i `$PATH`, slik at du kan starte kommandoen fra en hvilken som helst katalog.

### Krav til ytelse

For å fungere krever `rgb-lightning-node` daemon tilstedeværelse og konfigurasjon av :


- En `bitcoind`**-node

Hver RLN-instans må kommunisere med `bitcoind` for å kringkaste og overvåke sine transaksjoner i kjeden. Autentisering (innlogging/passord) og URL (host/port) må oppgis til daemon.


- En indekseringsenhet** (Electrum eller Esplora)

Dæmonen må kunne liste opp og utforske transaksjoner i kjeden, spesielt for å finne UTXO-en som en eiendel er forankret på. Du må spesifisere URL-adressen til Electrum-serveren eller Esplora.


- En RGB**-proxy

Som vi har sett i tidligere kapitler, er **proxy-serveren** en komponent (valgfri, men sterkt anbefalt) som forenkler utvekslingen av *sendinger* mellom Lightning-motparter. Også her må en URL angis.

ID-er og URL-er legges inn når demonen _låses opp_ via API-et. Mer om dette senere.

### Regtest-lansering

For enkel bruk finnes det et `regtest.sh`-skript som automatisk starter et sett med tjenester via Docker: `bitcoind`, `electrs` (indekser), `rgb-proxy-server`.

![RGB-Bitcoin](assets/fr/100.webp)

Dette gjør at du kan starte et lokalt, isolert og forhåndskonfigurert miljø. Den oppretter og ødelegger containere og datakataloger ved hver omstart. Vi begynner med å starte :

```bash
./regtest.sh start
```

Dette skriptet vil :


- Opprett en `docker/`-katalog for å lagre ;
- Kjør `bitcoind` i regtest, samt indekseren `electrs` og `rgb-proxy-serveren` ;
- Vent til alt er klart til bruk.

![RGB-Bitcoin](assets/fr/101.webp)

Nå skal vi starte flere RLN-noder. I separate skall kjører du for eksempel (for å starte 3 RLN-noder) :

```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```

![RGB-Bitcoin](assets/fr/102.webp)


- Parameteren `--network regtest` indikerer bruk av regtest-konfigurasjonen;
- `--daemon-listening-port` angir hvilken REST-port Lightning-noden skal lytte etter API-anrop på (JSON);
- `--ldk-peer-listening-port` angir hvilken Lightning p2p-port det skal lyttes på;
- `dataldk0/`, `dataldk1/` er stiene til lagringskatalogene (hver node lagrer informasjonen sin separat).

Du kan også kjøre kommandoer på RLN-nodene dine fra nettleseren:

```url
https://rgb-tools.github.io/rgb-lightning-node/
```

For at en node skal kunne åpne en kanal, må den først ha bitcoins på en adresse som er generert med følgende kommando (for node nr. 1, for eksempel):

```bash
curl -X POST http://localhost:3001/address
```

Svaret vil gi deg en adresse.

![RGB-Bitcoin](assets/fr/103.webp)

På `bitcoind` Regtest skal vi utvinne noen bitcoins. Kjør :

```bash
./regtest.sh mine 101
```

![RGB-Bitcoin](assets/fr/104.webp)

Send pengene til nodeadressen som er generert ovenfor:

```bash
./regtest.sh sendtoaddress <address> <amount>
```

![RGB-Bitcoin](assets/fr/105.webp)

Deretter utvinner du en blokk for å bekrefte transaksjonen:

```bash
./regtest.sh mine 1
```

![RGB-Bitcoin](assets/fr/106.webp)

### Testnet-lansering (uten Docker)

Hvis du vil teste et mer realistisk scenario, kan du starte 3 RLN-noder på Testnet i stedet for i Regtest, som peker mot offentlige tjenester :

```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```

Hvis ingen konfigurasjon blir funnet, vil daemon som standard prøve å bruke :


- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332`
- indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-rpc`

Med innlogging :


- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `passord`

Du kan også tilpasse disse elementene via API-et `init`/`unlock`.

### Utstedelse av en RGB-token

For å utstede et token begynner vi med å lage "fargeleggbare" UTXO-er:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```

![RGB-Bitcoin](assets/fr/107.webp)

Du kan selvfølgelig tilpasse bestillingen. For å bekrefte transaksjonen, utvinner vi en :

```bash
./regtest.sh mine 1
```

Vi kan nå opprette en RGB-ressurs. Kommandoen avhenger av hvilken type eiendel du ønsker å opprette og dens parametere. Her oppretter jeg et NIA-token (*Non Inflatable Asset*) ved navn "PBN" med en forsyning på 1000 enheter. Med `precision` kan du definere delbarheten til enhetene.

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "PBN",
"name": "Plan B Network",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```

![RGB-Bitcoin](assets/fr/108.webp)

Svaret inneholder ID-en til den nyopprettede ressursen. Husk å notere denne identifikatoren. I mitt tilfelle er den :

```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```

![RGB-Bitcoin](assets/fr/109.webp)

Deretter kan du overføre den videre i kjeden, eller allokere den i en Lightning-kanal. Det er akkurat det vi skal gjøre i neste avsnitt.

### Åpne en kanal og overføre en RGB-ressurs

Du må først koble noden din til en motpart i Lightning-nettverket ved hjelp av kommandoen `/connectpeer`. I mitt eksempel kontrollerer jeg begge nodene. Derfor henter jeg den offentlige nøkkelen til min andre Lightning-node med denne kommandoen:

```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```

Kommandoen returnerer den offentlige nøkkelen til min node nr. 2 :

```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```

![RGB-Bitcoin](assets/fr/110.webp)

Deretter åpner vi kanalen ved å spesifisere den relevante ressursen (`PBN`). Med kommandoen `/openchannel` kan du definere størrelsen på kanalen i satoshis og velge om du vil inkludere RGB-aktivet. Det kommer an på hva du ønsker å lage, men i mitt tilfelle er kommandoen :

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```

Finn ut mer her:


- `peer_pubkey_and_opt_addr`: Identifikatoren til motparten vi ønsker å koble oss til (den offentlige nøkkelen vi fant tidligere);
- `kapasitet_sat`: Total kanalkapasitet i satoshis ;
- `push_msat`: Beløp i millisatoshis som overføres til motparten når kanalen åpnes (her overfører jeg 10 000 sats med en gang, slik at han kan foreta en RGB-overføring senere);
- `asset_amount`: Mengde RGB-ressurser som skal bindes til kanalen ;
- `asset_id` : Unik identifikator for RGB-aktiva som er involvert i kanalen;
- `offentlig`: Angir om kanalen skal gjøres offentlig for ruting i nettverket.

![RGB-Bitcoin](assets/fr/111.webp)

For å bekrefte transaksjonen utvinnes 6 blokker:

```bash
./regtest.sh mine 6
```

![RGB-Bitcoin](assets/fr/112.webp)

Lightning-kanalen er nå åpen og inneholder også 500 `PBN`-tokens på node nr. 1 sin side. Hvis node nr. 2 ønsker å motta `PBN`-tokens, må den generere en faktura. Slik gjør du det:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```

Med :


- `amt_msat`: Fakturabeløp i millisatoshis (minimum 3000 sats) ;
- `expiry_sec` : Fakturaens utløpstid i sekunder ;
- `asset_id` : Identifikator for RGB-eiendelen som er knyttet til fakturaen ;
- `aktivum_beløp`: Beløpet for RGB-eiendelen som skal overføres med denne fakturaen.

Som svar får du en RGB-faktura (som beskrevet i de foregående kapitlene):

```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```

![RGB-Bitcoin](assets/fr/113.webp)

Vi vil nå betale denne fakturaen fra den første noden, som har de nødvendige kontantene med `PBN`-tokenet:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```

![RGB-Bitcoin](assets/fr/114.webp)

Betaling har blitt utført. Dette kan bekreftes ved å utføre kommandoen :

```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```

![RGB-Bitcoin](assets/fr/115.webp)

Slik distribuerer du en Lightning-node som er modifisert for å transportere RGB-ressurser. Denne demonstrasjonen er basert på :


- Et regtest-miljø (via `./regtest.sh`) eller testnet ;
- En Lightning-node (`rgb-lightning-node`) basert på en `bitcoind`, en indekserer og en `rgb-proxy-server` ;
- En serie JSON REST API-er for åpning/lukking av kanaler, utstedelse av tokens, overføring av eiendeler via Lightning osv.

Takket være denne prosessen :


- Lightning Engagement-transaksjoner inkluderer en ekstra utgang (OP_RETURN eller Taproot) med forankring av en RGB-overgang;
- Overføringer gjøres på nøyaktig samme måte som tradisjonelle Lightning-betalinger, men med tillegg av et RGB-token;
- Flere RLN-noder kan kobles sammen for å rute og eksperimentere med betalinger på tvers av flere noder, forutsatt at det er tilstrekkelig likviditet i både bitcoins og aktivumet RGB på stien.

Prosjektet er fortsatt i alfa-stadiet. Det anbefales derfor på det sterkeste at du begrenser deg til testmiljøer (regtest, testnet).

Mulighetene som åpnes av denne LN-RGB-kompatibiliteten er betydelige: stablecoins på Lightning, DEX layer-2, overføring av fungible tokens eller NFT-er til svært lave kostnader ... De foregående kapitlene har skissert den konseptuelle arkitekturen og valideringslogikken. Nå har du en praktisk oversikt over hvordan du kan få en slik node opp og gå, for fremtidig utvikling eller testing.

# Konklusjon

<partId>b0baebfc-d146-5938-849a-f835fafb386f</partId>


## Anmeldelser og rangeringer

<chapterId>0217e8b0-942a-5fee-bd91-9a866551eff3</chapterId>

<isCourseReview>true</isCourseReview>

## Konklusjon

<chapterId>0309536d-c336-56a0-869e-a8395ed8d9ae</chapterId>

<isCourseConclusion>true</isCourseConclusion>
