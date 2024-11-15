---
name: Peer-to-Peer Bitcoin Kjøp og Salgsløsning
goal: Utforske ikke-KYC Bitcoin kjøp og salgsløsninger
objectives:
  - Forstå de forskjellige typene KYC, deres risikoer og fordeler
  - Forstå fordelene med peer-to-peer kjøp
  - Implementere løsningen som passer dine behov
  - Forbedre håndteringen av dine UTXOer (KYC og ikke-KYC)
---

# En Reise inn i Verden av Ikke-KYC

Pierre tilbyr oss dette kurset som dykker ned i de forskjellige eksisterende løsningene for kjøp og salg av bitcoins peer-to-peer. Peer-to-peer kjøp er helt lovlig og tillater større anonymitet, faktisk er disse løsningene ikke KYC. KYC (Know Your Customer) er en markedsreguleringsregel (AMF) som innebærer å be om identifikasjon fra kunder som ønsker å kjøpe eller selge bitcoin. Disse reglene har som mål å forhindre hvitvasking av penger, finansiering av terrorisme og skatteunndragelse. Til tross for de betydelige konsekvensene for brukeren, har KYC som mål å forsvare og beskytte brukeren, selv om det ofte observeres å ha motsatt effekt.

Vi vil derfor utforske de forskjellige typene KYC (den fullstendige KYC-typen som i Frankrike, KYC Light-typen som i Sveits, og ikke-KYC-typen som peer-to-peer). Pierre vil presentere mer enn 6 løsninger, så du vil ha all informasjonen som trengs for å oppdage hvilken som passer deg. Hvis du leter etter en KYC-løsning, merk at de er inkludert i BTC 102-kurset.

+++

# Introduksjon
<partId>9aa6ddfd-a257-549f-bb23-f77f1ca5d330</partId>

## Forklaring & Type KYC
<chapterId>13d18e82-0c50-5a7f-97d8-39cf5b4ef085</chapterId>

### Introduksjon

![introduksjon av Rogzy](https://youtu.be/3AHeKLTK7Sg)

### Forklaring

![forklaring av KYC-typer](https://youtu.be/kDhXoPU1KtM)

KYC, for "Know Your Customer," er en regulatorisk standard som krever innsamling av privat informasjon fra klienter, som deres fysiske adresse, identifikasjon eller bankutskrifter. Denne praksisen er vanlig på meglerplattformer, som kan be om en komplett KYC, inkludert detaljert informasjon som et ID, et foto, bevis på bosted, lønnsslipper, osv.
Det primære målet med KYC (Know Your Customer) er å bekjempe hvitvasking av penger, finansiering av terrorisme og skatteunndragelse. Det er en lov implementert av AMF (Autorité des marchés financiers), det regulatoriske organet for det franske markedet. Imidlertid fører anvendelsen av KYC til sentraliseringen av høysensitive databaser som inneholder brukernes personlige informasjon. Denne informasjonen, som har en viss verdi, kan selges til ondsinnede enheter.
Videre ber ofte børsplattformer om en overdreven mengde personlig informasjon, og setter dermed brukerne i fare og øker samsvarskostnadene. Disse regulatoriske kostnadene kan avskrekke franske bedrifter og skade deres internasjonale konkurranseevne.

Det er tre typer KYC, inkludert full KYC, som krever en komplett og regulert innsamling av informasjon for å få tilgang til tjenesten. I Sveits tillater et alternativ kalt "KYC light" kjøp og salg av bitcoins uten å oppgi en ID, så lenge kjøpesummen ikke overstiger 1000 euro per dag. Løsninger som Relay muliggjør bruk av denne metoden.
I denne sammenhengen kan sveitsiske myndigheter få tilgang til bankinformasjon for å etterforske personer som anses som risikable. Leveringsadressene til bitcoins er også sporbare gjennom banksystemet. KYC light anses generelt som enklere og mindre kostbart enn det franske systemet.
I Frankrike krever kjøp av bitcoins på nett at man sender penger til en tredjepart, via SEPA-overføring eller Paypal. For de som prioriterer anonymitet, sikkerhet og personvern, er det også tilgjengelige løsninger for å kjøpe bitcoins kontant. For små volumer er kjøp av bitcoins kontant et enkelt og lovlig alternativ.
For å kunne selge daglig PLT på 100 euro av bitcoin til alle, er regulering av AMF (Autorité des Marchés Financiers) nødvendig. I Frankrike gjelder denne reguleringen hovedsakelig for enkeltpersoner som utfører betydelige volumer av transaksjoner. De to andre metodene for å kjøpe bitcoin inkluderer bruk av minibanker og utveksling blant venner. Minibanker er regulert og krever ID for transaksjoner over 500 euro. Utveksling blant venner tilbyr på den andre siden en mer diskret eksponering for bitcoin.

Disse regulatoriske tiltakene er på plass for å motvirke finansiering av terrorisme, skatteunndragelse og hvitvasking av penger. Bitcoin, som en fullstendig sporbar database, gjør hvitvasking av penger spesielt vanskelig. Bruken av Bitcoin av kriminelle kan spores, noe som gjør Bitcoin til et ineffektivt verktøy for hvitvasking av penger.
Det er viktig å merke seg at denne opplæringen presenterer ulike alternativer, samt verktøy som kan brukes til enten ondsinnede eller ikke-ondsinnete formål. I tillegg tilbyr den forklaringer på hvordan ordrebøker fungerer mellom skapere (ordreleverandører) og mottakere (ordremottakere).

Det er også viktig å merke seg at informasjonen som presenteres her ikke støtter noen spesiell løsning. Det er rett og slett for å presentere de tilgjengelige alternativene for en bedre forståelse av emnet. For eventuelle ytterligere spørsmål om Bitcoin, kan du gjerne konsultere nettressurser som www.discoverbitcoin.com.

## Sammenligning av Peer-to-Peer Kjøps- og Salgsløsninger
<chapterId>aad2dccb-0d2c-5533-859b-372b0f10d1ca</chapterId>

![sammenligning av p2p kjøps- og salgsløsninger](https://youtu.be/HiwSjN04Mz0)

P2P-løsninger for å kjøpe Bitcoin: Bisq, RoboSat, LNP2PBot, Peach, og HodlHodl

Å kjøpe Bitcoin på en peer-to-peer (P2P) basis er et foretrukket alternativ for investorer som ønsker å unngå sentraliserte utvekslingsplattformer. Denne delen av kurset undersøker forskjellige P2P-løsninger som er tilgjengelige, inkludert Bisq, RoboSat, LNP2PBot, Peach, og HodlHodl.
Sammenligning av fordelene og ulempene ved forskjellige løsninger

Hver P2P-løsning har sine egne fordeler og ulemper. Nedenfor er en oversikt over de viktigste funksjonene til hver løsning.

### Bisq

[Bisq](https://bisq.network/) er en ikke-forvaringsbasert P2P-løsning som har et DAO (Desentralisert Autonom Organisasjon) system og bruker multisig for tvisteløsning. Koden er åpen kilde, noe som bidrar til robustheten og beskyttelsen av brukerens personvern.

| Fordeler                                      | Ulemper                                                                                                       |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| - P2P, ikke-forvaring, multisig, DAO-løsning | - Applikasjonen er ganske tung og ikke veldig brukervennlig, tilgjengelig bare på datamaskiner                           |
| - Robust og sikker                        | - Begrensningene på kjøp og salg samt kontohåndtering med signaturer har en dobbeltkantet aspekt. |
| - Åpen kilde                                 |                                                                                                                     |

### RoboSat

[RoboSat](https://learn.robosats.com/) er en enkel å bruke, rask løsning som opererer under TOR og krever ikke en konto. Den er åpen kilde og bruker Lightning Network for raske transaksjoner.

| Fordeler                                                    | Ulemper                                                                  |
| - Enkel å bruke                                        | - Protokollen er skjør med kun én koordinator                              |
| - Lave transaksjonsgebyrer                             | - Krever teknisk kunnskap og forståelse for personvern |
| - Bruker Lightning Network for raske transaksjoner | - Umbrell-applikasjonen lar deg administrere din egen klientinstans        |

### LNP2PBot

[LNP2PBot](https://lnp2pbot.com/) er tilgjengelig via Telegram for kjøp av Bitcoin uten KYC. Den tilbyr raske transaksjoner gjennom Lightning Network og lave gebyrer.

| Fordeler                                                            | Ulemper                                                             |
| ------------------------------------------------------------------ | ------------------------------------------------------------------- |
| - Tilgjengelig via Telegram                                        | - Mindre robust og sikker enn andre løsninger                       |
| - Hastighet gjennom Lightning Network                              | - Tregere og mindre brukervennlig enn Robosat                       |
| - Lave transaksjonsgebyrer                                          | - Kan kobles til brukerens Telegram-identitet                       |
| - Intern tvisteløsning                                              | - Mangel på likviditet og skjørhet i applikasjonen                  |
| - Tilbyr fellesskap for å redusere tillitsproblemer                 | - Tillit må plasseres i LNP2Pbot for tvisteløsning                  |

### Peach

[Peach](https://peachbitcoin.com/) er en mobilapplikasjon dedikert til handel med Bitcoin. Den skiller seg ut med sin enkelhet, uten krav om å opprette en konto for å operere. Handler er raske, selv uten Lightning Network. I tillegg akselererer telefonvarsler transaksjonsprosessen.

| Fordeler                                                            | Ulemper                                                                                                                     |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------- |
| - Forenklet bruk: ingen kontooppretting er nødvendig.              | - Sikkerhet og robusthet: ved å være knyttet til et selskap, har Peach potensielle svakheter når det gjelder sikkerhet.    |
| - Transaksjonshastighet: utvekslinger er raske.                    | - Fravær av Lightning Network: denne teknologien, som tillater raskere Bitcoin-transaksjoner, brukes ikke av Peach.        |
| - Varsler: de akselererer transaksjonsprosessen.                    |                                                                                                                             |

### HodlHodl

[HodlHodl](https://hodlhodl.com/) er en ikke-forvaringsløsning for Bitcoin-utveksling. Den tilbyr mange fordeler som høy likviditet, muligheten for private handler, et henvisningssystem, samt kontoer med handelshistorikk og et vurderingssystem. Imidlertid er handler knyttet til brukerens e-postadresse og digitale identitet, lagret hos HodlHodl. Videre er kildekoden til HodlHodl ikke åpen for offentligheten, og applikasjonen kan ikke brukes med Tor.

| Fordeler                                                                                                                     | Ulemper                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| - Ikke-forvaring: brukeren forblir i besittelse av sine private nøkler.                                                      | - Lagring av personlig informasjon: brukerens e-postadresse og digitale identitet lagres av HodlHodl.                    |
| - Likviditet: HodlHodl tilbyr et bredt spekter av utvekslingsmuligheter.                                                     | - Lukket kildekode: koden til HodlHodl er ikke åpen for offentligheten.                                                   |
| - Private handelsalternativer: brukeren kan velge hvem de vil handle med. | - Inkompatibilitet med Tor: HodlHodl kan ikke brukes med dette personvern-fokuserte nettverket. |
| - Henvisningssystem: HodlHodl belønner muntlig anbefaling. | - Mulighet for tvungen KYC: i visse situasjoner kan HodlHodl kreve identifikasjonsinformasjon for å hente midler. |
| - Handelshistorikk og vurderingssystem: disse funksjonene tillater vurdering av påliteligheten til andre brukere. | |

## Konklusjon om P2P-løsninger
<chapterId>c904985a-78dd-593e-a9c4-bfd1208d10c3</chapterId>
Oppsummert har hver P2P-løsning sine fordeler og ulemper. Bisq anses som den mest robuste og sikre, men mindre tilgjengelig. RoboSat er åpen kildekode, men mindre robust enn Bisq. LNP2PBot er mindre robust og sikker enn de andre løsningene, tregere og mindre brukervennlig enn RoboSat, men mer så enn Bisq. Peach er den enkleste og raskeste appen for å kjøpe Bitcoin uten KYC, men den er støttet av et selskap, derfor svakheter når det gjelder sikkerhet og robusthet. HodlHodl er et protokoll administrert av et selskap og er lukket kildekode, derfor har den svakheter når det gjelder sikkerhet og robusthet, og er litt mer komplisert enn Peach.
Den gode gamle kontant betaling ansikt til ansikt forblir alltid en løsning, for små beløp.
I tillegg til P2P-løsninger, finnes det andre alternativer for kryptovalutaveksling. kycnot.me tilbyr tjenester som VPN, VPS, SMS, osv. Bitrefil lar deg kjøpe gavekort. Hver løsning på [kycnotme](https://kycnot.me/) er presentert med sine fordeler og ulemper.

# Veiledninger om P2P kjøp/salgsløsninger
<partId>582cee39-f6d0-5fb8-906f-b3e4c9f36fa5</partId>

## Robosats
<chapterId>1f1bd705-fcb3-5e32-8aa7-9ba184488326</chapterId>

![robosats](https://tube.nuagelibre.fr/videos/watch/1978a2e0-64a0-4437-9229-7614cdf5bf61?start=0s)

[RoboSat](https://learn.robosats.com/) er et åpen kildekode-prosjekt utviklet av Reckless Satoshi for å privat utveksle Bitcoins mot nasjonale valutaer. Det forenkler peer-to-peer-opplevelsen og bruker Lightning-fakturaer for å minimere behovet for oppbevaring og tillit. For å bruke det, trenger vi Tor, et anonymt kommunikasjonsnettverk.

Det første du må gjøre er å laste ned Tor. Du kan finne det på GitHub eller direkte på den offisielle nettsiden på følgende adresse: tor.org/download.
Når Tor er lastet ned og installert:
- Trykk "Koble til" for å etablere forbindelsen.
- Gå til [Robosats løk-adresse](http://robosats6tkf3eva7x2voqso3a5wcorsnw34jveyxfqi2fu7oyheasid.onion/).
- Kopier tokenet for å lagre identiteten din.

Her er stegene for å kjøpe bitcoins med Robosats:

- Sjekk ordreboken, du kan filtrere etter valuta og betalingsmetode - for eksempel, kjøp bitcoin i euro med Revolut.
- Før du kjøper, sjekk tilbudets utløpstid, prisen i euro, og premien (du kan også filtrere tilbud etter premie).
- Velg helst et tilbud med en aktiv bruker og en premie lavere enn gjennomsnittet.
- Verifiser ordresammendraget med beløpet, betalingsmetoden, premien, ordre-ID og utløpstid.
- Du kan motta dine satoshis på en bitcoin-adresse med bytte-ut avgifter (fra LN til BTC-onchain) på omtrent 1% (du kan endre on-chain mining-avgifter).
- Alternativt, opprett en faktura med en LN-lommebok fra denne [listen](https://learn.robosats.com/docs/wallets/) og kopier fakturaen på Robosats.
- Kontakt selgeren via kryptert chat for å diskutere fiat-betaling.

Nå la oss se på stegene for å selge bitcoins på Robosats:

- Tilpass tilbudet ditt ved å velge betalingsmetode, premie, utløpsvarighet, osv.
- Størrelsen på Fidelity Bond er tilsvarende sikkerhetsdepositumet på BISQ. Sett 15% eller 10% sikkerhetsdepositum for å oppmuntre til rettferdig spill fra den andre parten.
- Lås satoshisene for å bekrefte opprettelsen av ordren og unngå spam.
- Hvis noen aksepterer ditt salgstilbud, diskuter med jevnaldrende for å fortsette med fiat-betalingen. Når betalingen er gjort, er handelen fullført, og de solgte satoshisene er dine!

## BISQ: En peer-to-peer kjøpsløsning
<chapterId>28b010ce-0e9b-5f20-a622-fa64629b2d88</chapterId>

[Bisq](https://bisq.network/) er en desentralisert utvekslingsplattform for digitale eiendeler, primært Bitcoin. Den tillater direkte, sikre og private transaksjoner mellom brukere over hele verden uten behov for en mellommann.

🚨 Vær forsiktig når du bruker Bisq, da det er en avansert løsning. Det er kanskje ikke egnet for nybegynnere. Sørg for at du har litt erfaring og forståelse før du starter. 🚨

Vi vil se nærmere på denne løsningen, her er opplæringsvideoene:
For de mer erfarne, her er en kortfattet guide som raskt skisserer de essensielle stegene:

1. Last ned og installer: Besøk Bisq-nettstedet og last ned applikasjonen. Installer den på systemet ditt.
2. Sett opp betalingsmetode: Åpne applikasjonen og gå til "Konto". Legg til detaljene for betalingsmetoden din.
3. Fyll opp din Bisq-lommebok: Klikk på "Fond" og deretter "Motta fond" for å få din Bisq-adresse. Send Bitcoins til denne adressen.
4. Gjør en transaksjon: Klikk på "Kjøp/Selg" og velg ønsket transaksjon. Følg instruksjonene for å fullføre transaksjonen.
5. Bekreft mottak: Når du har mottatt betalingen, bekreft den i Bisq-applikasjonen. Dette frigjør Bitcoin fra depot.

Husk alltid å sjekke alle detaljene i transaksjonene dine og kun håndtere med pålitelige parter.

Her er nå en komplett guide som vil lede deg gjennom alle stegene for å bruke Bisq.

BISQ er et desentralisert og sikkert nettverk som respekterer ditt privatliv. Faktisk er det ikke-forvaring, noe som betyr at du alltid eier dine midler. Videre bruker BISQ en token, BSQ, som lar deg betale lavere transaksjonsgebyrer og oppmuntrer din deltakelse i DAO (Desentralisert Autonom Organisasjon). For å beskytte selgere i Bitcoin-fiat-transaksjoner, har BISQ implementert et system med signaturer og konto begrensninger. Som kjøper, må du skaffe en signert konto for å øke kjøpsgrensen din. Signaturen er også en måte å verifisere handelshistorikken til handelsmenn, og dermed sikre sikkerheten til transaksjonene.

For å installere Bisq og sikkerhetskopiere dataene dine, følg disse enkle stegene:

- Gå til bisc.network-siden for å laste ned programvaren (Skjermbilde av nedlastingssiden)
- Verifiser integriteten til programvaren ved hjelp av verktøy som de tilbudt av Loïc Morel for Windows-brukere.
- Når installasjonsprogrammet er verifisert, start BISQ, gi de nødvendige tillatelsene, og aksepter bruksvilkårene. (Skjermbilde av bruksvilkårene)
- BISQ vil koble seg til Bitcoin-nettverket og seg selv via Tor, noe som kan ta litt tid.
- Sett opp din betalingskonto og lag sikkerhetskopier av din SID (Secure Identifier) av lommeboken din for å forhindre tap eller tyveri. (Skjermbilde av oppsettssiden for konto)
- Sett også opp et passord for å kryptere informasjonen din.
Avhengig av operativsystemet ditt, vil BISQ-data bli lagret på forskjellige steder. Du kan finne dem i "Data Directory"-mappen. Vær forsiktig, hvis du sletter denne mappen, vil all din BISQ-data gå tapt. For å gjenopprette dataene dine gjennom en sikkerhetskopi:
- Kopier sikkerhetskopimappen til 'bruker/application support/BISQ'-plasseringen.
- Gi sikkerhetskopimappen navnet 'BISQ'.
- Start BISQ på nytt, og alle dataene dine skal være gjenopprettet.

Før du begynner å kjøpe eller selge Bitcoin på BISQ, er det avgjørende å sette opp betalingskontoen din. For eksempel kan du opprette en konto i din nasjonale valuta, som en SEPA-konto, en REVOLUT-konto, eller en PAYPAL-konto. For å sette opp din REVOLUT-konto:

- Legg til en konto og velg REVOLUT fra listen over alternativer. (Skjermbilde av listen over kontoalternativer)
- Du kan velge forskjellige valutaer: euro, pund sterling, amerikanske dollar, eller sveitsiske franc.
- Maksimal transaksjonsvarighet er én dag, og kjøpsgrensen er 0.25 Bitcoin.
- Bruk ditt personlige REVOLUT-kontonavn for å unngå forvirring.
- Sørg for å signere kontoene dine og etablere kjøpsgrenser for mer sikkerhet.

For å kjøpe Bitcoin på BISQ:

- Gå til "Kjøp"-seksjonen hvor du kan velge fra forskjellige markeder. (Skjermbilde av "Kjøp"-seksjonen)
- For å dra nytte av reduserte gebyrer, anbefaler vi å kjøpe BSQ, som du kan kjøpe med Bitcoin.
- Du kan velge fra forskjellige tilbud basert på pris, mengde, betalingsmetode, osv.
- For å kjøpe BSQ, først sett inn Bitcoin i lommeboken din.
- Velg et tilbud med lav premie og en liten mengde for å kjøpe BSQ.
- BISQ verifiserer gyldigheten av tilbudet og peer-tilkoblingen.
- Hvis selgeren ikke er tilkoblet, velg en annen.
- Sjekk tilbudet og aksepter en 5% premie.
- Bekreft gebyrene og BSQ-utvekslingen, og vent deretter på transaksjonsbekreftelsen for å kjøpe Bitcoins med BSQ.

For å selge Bitcoin på BISQ:

- Opprett et nytt tilbud i "Selg"-fanen. (Skjermbilde av "Selg"-fanen)
- Du kan velge å sette antall Bitcoins til salgs eller beløpet i euro du ønsker å motta.
- Du kan sette en premie som en prosentandel over markedsprisen.
- Du kan opprette et salgsområde eller la valget være opp til kjøperen.
- Du kan også sette en pris for å stoppe tilbudet.
- Velg minimumsinnskuddsbeløpet og transaksjonsgebyrene.
- Finansier ordren ved å sette inn Bitcoinsene som skal selges, beløpet for sikkerhetsinnskuddet, og gebyrene.
- Når du har opprettet tilbudet, vent på at en kjøper skal dukke opp.
Når kjøperen har gjort transaksjonsinnskuddet på BISQ, blir Bitcoins automatisk sendt til kjøperen, og du mottar pengene. Kontoen verifiseres og signeres etter en transaksjon med en signert konto.
## LNP2PBOT
<chapterId>e3b61150-90e3-5ab4-bc12-4a05879321f5</chapterId>

![LNp2pbot tutorial](https://tube.nuagelibre.fr/videos/watch/57ed232d-6149-4267-be38-92b0f32800f7)

[Telegram](https://telegram.org/) er en meldingsplattform som, med hjelp av botten [Lnp2pbot](https://lnp2pbot.com/), lar deg kjøpe og selge bitcoins raskt og enkelt. Slik gjør du det:

For å kjøpe Bitcoins via LNP2PBOT på Telegram, følg disse trinnene:
- Start med å gå til Lnp2pbot sin Twitter-konto og klikk på lenken i bioen. (Skjermbilde av botens Twitter-konto og lenken i bioen)
- I Telegram, bruk kommandoene "/buy" eller "/sell" for å legge ut kjøps- eller salgsordrer. (Skjermbilde av bruk av kommandoene "/buy" eller "/sell")
- Gå til P2P Lightning-kanalen for å finne kjøps- og salgstilbud som passer dine kriterier. (Skjermbilde av P2P Lightning-kanalen)
- Opprett et kjøpstilbud ved hjelp av Lnp2pbot og kommandoen "/buy".
- Velg valutaen du foretrekker, angi mengden, prisen (med et påslag om ønskelig), og velg betalingsmetoden din.
- Vent til en potensiell selger kontakter deg.

For å selge Bitcoins via Revolut, her er hva du trenger å gjøre:

- Klikk på 'sell Satoshi' for å åpne en varsling på LNP2PBot. (Skjermbilde av 'sell Satoshi'-alternativet)
- Motta en Lightning-faktura for å betale for å selge Satoshis. (Skjermbilde av Lightning-fakturaen)
- Vent på at kjøperen sender en faktura med satoshis for å motta betalingene.
- Etablere direkte kontakt med kjøperen via Telegram for å avtale betalingsmetoden og utveksle nødvendig informasjon.
- Valider transaksjonen med en merknad.

Hvis du ønsker å kjøpe Bitcoins ved å sende en LN-faktura, følg disse trinnene:

- Kopier fakturaen og send den til botten for å kjøpe Satoshi.
- Ta kontakt med selgeren for å fullføre kjøpet av bitcoins.
- I tilfelle av et problem, foreslå å vente eller forsøke en avbrytelse.
- Avbryt tilbudet og se etter et nytt om nødvendig.
- Velg et tilbud som aksepterer øyeblikkelige CPAs for kjøp av Satoshi.
- Send fakturaen og vent på selgerens betalingsbekreftelse.
- Når betalingen er gjort, send bekreftelsen til botten.
- Vent på valideringen av mottak av euro og sending av satoshis fra selgeren.
Ved å bruke disse metodene, kan du kjøpe og selge bitcoins på Telegram på en sikker måte.

## Peach Bitcoin
<chapterId>05e328c4-1003-586e-85c3-65109e3486e1</chapterId>

nettsted: https://peachbitcoin.com/

Vi tar en detaljert titt på denne løsningen i BTC 205 tilbudt av @pivi\_, her er opplæringsvideoene:

![peach](https://youtu.be/ziwhv9KqVkM)

[Peach](https://peachbitcoin.com/) er en sveitsisk mobilapplikasjon som tillater kjøp og salg av bitcoins peer-to-peer. Denne brukervennlige løsningen tilbyr et intuitivt grensesnitt, ideelt for kryptovalutatransaksjoner.

Grensesnittet til Peach-applikasjonen består av fire faner: kjøp, selg, historikk og innstillinger. (Skjermbilde av applikasjonsgrensesnittet)
Å kjøpe bitcoins på Peach er forenklet. For å starte trenger du å opprette et tilbud. Dette er mulig ved å få tilgang til "kjøp"-fanen. (Skjermbilde av "kjøp"-fanen)
Deretter kan du bla gjennom de tilgjengelige tilbudene ved å sveipe til du finner det som passer deg. De aksepterte betalingsmetodene er varierte, inkludert bankoverføring, online lommebok, gavekort og lokal mulighet. (Skjermbilde av tilgjengelige betalingsmetoder)
Når du har valgt et tilbud, kan du diskutere med selgeren via chatten integrert i applikasjonen. (Skjermbilde av applikasjonens chat)
Etter betalingen, bekreftet av selgeren, er transaksjonen fullført. Bitcoinsene sendes deretter til kjøperen, som mottar en varsling som bekrefter mottak av midler. (Skjermbilde av varslingen om mottak av bitcoins)
Peach er en ikke-forvaringsapplikasjon, noe som betyr at bitcoinene forblir i din besittelse gjennom hele prosessen. Eventuelle potensielle tvister håndteres imidlertid sentralt. Derfor er det avgjørende å sikkerhetskopiere transaksjonsrelatert informasjon og din personlige informasjon ved hjelp av Sikkerhetskopieringsfunksjonen. (Skjermbilde av Sikkerhetskopieringsfunksjonen) Ettersom Peach fortsatt er i betaversjon, kan noen feil oppstå. Det anbefales å verifisere all informasjon før du avslutter en transaksjon.
Oppsummert tilbyr Peach mobilapplikasjonen en tilgjengelig løsning for kjøp og salg av bitcoins peer-to-peer. Sikker og optimal bruk av Peach er nøkkelen til vellykkede transaksjoner.

## Hold Hodl
<chapterId>2c285751-ae9f-54af-8b28-c7c0beac7b43</chapterId>
[HodlHodl](https://hodlhodl.com/) er en desentralisert Bitcoin-markedsplass som prioriterer brukerkontroll og sikkerhet. I motsetning til tradisjonelle børser, opererer den på en peer-to-peer-modell, som tillater direkte utvekslinger mellom brukere. Takket være sitt multisignatur-escrow-system, sikrer Hodl Hodl sikkerheten til midler under transaksjoner. Plattformen støtter også ulike betalingsmetoder og tilbyr handelsalternativer som Kontrakter for Forskjell (CFD).
![hodlhodl tutorial](https://youtu.be/BDH9jE7kpD8)

I denne veiledningen forklarer vi hvordan du kjøper og selger bitcoins peer-to-peer på HodlHodl-plattformen.

Før du begynner å bruke HodlHodl-plattformen, er noen forberedende trinn nødvendige:

- Åpne HodlHodl-nettstedet.
- Opprett en konto ved hjelp av en e-postadresse for å holde en historikk over transaksjonene dine.
- Les sikkerhetsguiden nøye før du begynner å handle.
- Merk at plattformen ikke er åpen kildekode og beholder noe av din personlige informasjon.

Her er prosessen du følger for å gjøre et kjøp på HodlHodl-plattformen:

- Bruk filterfunksjonen for å finne tilbud som passer deg.
- Klikk på tilbudet som interesserer deg.
- Fyll inn de nødvendige feltene for å akseptere kontrakten.
- I vårt eksempel brukte vi Revolut som betalingsmetode.

Oppsett av multisig-kontrakten for transaksjonen gjøres som følger på HodlHodl:

- Når tilbudet er akseptert, gjør betalingen via den valgte metoden (Revolut i vårt tilfelle).
- Opprett en multisig-kontrakt ved å generere et passord.
- Vent på at bitcoinene blir deponert på multisig-adressen.
- Velg antall bekreftelser for kontrakten.
- Gjør betalingen av det avtalte beløpet til selgeren og bekreft det på HodlHodl.
- Vær tålmodig ettersom deponeringstiden kan være lang, avhengig av banken som brukes.
- Vent på selgerens bekreftelse før du frigjør bitcoinene etter kjøpet.

Å opprette et salgs- eller kjøpstilbud for bitcoins på HodlHodl går som følger:

- På HodlHodl-nettstedet, angi frigjøringsadressen for kjøpstilbud.
- Angi mengde, pris og betalingsmetode.
- Du kan også legge til valgfrie funksjoner som transaksjonsgrenser eller en tittel for tilbudet.
- Når tilbudet er opprettet, kan du se, redigere, duplisere eller slette det som du ønsker.

## Bonus: Side Shift.AI
<chapterId>bd1f0844-af1e-53da-9518-b3b22f802276</chapterId>

![SideShift AI](https://youtu.be/xG8Wc1Ti5b8)
Her er en kort veiledning om bruk av [SideShift AI](https://sideshift.ai/), et veldig praktisk verktøy for å konvertere shitcoins til bitcoin. Det er det ideelle verktøyet for de som har stengt alle sine personlige børser. Det er ikke nødvendig med et ordresystem, og likviditet er tilgjengelig. Vær imidlertid oppmerksom på at det er et gebyr på 2,5 % per transaksjon. Hvis du har kjøpt kryptovalutaer på en KYC-måte, anbefales det å bruke Monero for å konvertere disse kryptovalutaene til bitcoin. Monero tilbyr overlegen personvern sammenlignet med Bitcoin. For økt sikkerhet anbefales også CoinJoin-operasjonen. CoinJoin blander transaksjonene dine med de til andre brukere for å komplisere sporingen av transaksjonene dine.

Jeg vil også introdusere deg for et åpen kildekode-verktøy for kjøp og salg av bitcoins. Dette verktøyet lar deg velge fra mange blokkjeder. Du trenger bare å oppgi din Bitcoin-adresse og velge beløpet du ønsker å sende. Det er ikke nødvendig å opprette en konto eller koble lommeboken din til verktøyet. Du kan bruke en fast kurs for å sende eller motta et spesifikt beløp. I tillegg tillater dette verktøyet også salg av bitcoins i bytte mot USDC.

### Støtt Oss

Dette kurset, samt alt innholdet som er tilgjengelig på dette universitetet, har blitt tilbudt deg gratis av vårt fellesskap. For å støtte oss, kan du dele det med andre, bli medlem av universitetet, og til og med bidra til utviklingen via GitHub. På vegne av hele teamet, takk!

### Vurder Opplæringen

Et vurderingssystem for opplæringen vil snart bli integrert i denne nye E-læringsplattformen! I mellomtiden, tusen takk for at du fulgte kurset, og hvis du likte det, tenk på å dele det med de rundt deg.

# For å Gå Videre
<partId>28194543-78b5-5f98-852a-2fc76439ddde</partId>

## Intervju med Steph fra Peach Bitcoin
<chapterId>76ed1f17-1d0b-5c0f-8726-91ab4e2e2955</chapterId>

![intervju med Steph](https://youtu.be/LRGKD8qNSXw)

Her er et sammendrag av intervjuet:

Peach Bitcoin er en ikke-forvarings mobilapplikasjon, som muliggjør kjøp og salg av Bitcoin på en peer-to-peer-måte. For øyeblikket inkluderer Pitch Bitcoin-teamet, basert i Sveits, åtte medlemmer og streber etter å utvikle applikasjonen til også å fungere som en lommebok. Den unike modellen til Pitch Bitcoin er basert på en sentralisert bedriftsstruktur, samtidig som den opprettholder en desentralisert kjøp- og salgsprotokoll. I tillegg tilbyr applikasjonen et alternativ for kontanttransaksjoner under personlige møter.
En av de viktigste fordelene med Pitch Bitcoin er sikkerhetsnivået det tilbyr brukerne. Escrow-systemet med multisignatur og tidsbegrensning er designet for å håndtere konflikter og sikre sikkerheten til transaksjonene. Dessuten har Pitch Bitcoin prioritert tilgang til multisignaturmidlene, noe som gjør det mulig å overføre bitcoins til kjøperen i tilfelle ondsinnet oppførsel fra selgerens side. Selskapet planlegger å integrere alle europeiske valutaer samt andre betalingsmetoder når det lanseres i åpen beta i januar.

Idéen til Pitch Bitcoin ble født fra grunnleggerens personlige erfaring i Bitcoin-industrien. Etter å ha oppdaget Bitcoin i 2017 og deltatt på flere meetups og konferanser, ble hun en Bitcoin-maksimalist og så muligheten til å skape en plattform for Bitcoiners for å møtes og gjennomføre kontanttransaksjoner. I tillegg inkluderer applikasjonen kryptert chat for kommunikasjon med andre brukere, og bevarer dermed brukerens anonymitet.
For øyeblikket utvikler Pitch Bitcoin flere funksjoner for å lette arbeidet for selgere, inkludert opprettelsen av et API for selgere, en plattform for store selgere, og integreringen av BTC Pay Server for å automatisere overføringer. Applikasjonen vil bli lansert i åpen beta i januar 2023.
For å konkludere, understreker grunnleggeren av Pitch Bitcoin viktigheten av konkurranse i Bitcoin-økosystemet, ettersom det som er bra for Bitcoin er gunstig for alle. Hun oppfordrer også til mangfold og inkludering i Bitcoin-industrien og videre.

## Intervju med Pierre
<chapterId>4e4ba218-01ec-5f3a-bc49-c148bb22ee61</chapterId>

![intervju med Pierre](https://youtu.be/COoezuJncm8)

Her er et sammendrag av intervjuet:
Dette intervjuet avslutter Bitcoin 205-kurset, som tar for seg temaet løsninger for kjøp av Bitcoin peer-to-peer. Organisert av Pierre, har dette kurset som mål å utdanne det fransktalende publikummet om de tekniske løsningene for peer-to-peer Bitcoin-kjøp, et område som har blitt neglisjert til nå. Takket være fremskrittene som er gjort, er det nå mulig å kjøpe og bruke Bitcoin samtidig som man bevarer sitt privatliv, selv med bare en telefon og Telegram-appen.

En av metodene som blir fremhevet er bruken av CoinJoin med Samourai for å forbedre sikkerheten. Denne løsningen minimerer risikoene forbundet med sentraliserte enheter som holder personlig informasjon om Bitcoin-brukere. Det anbefales å kjøpe Bitcoins non-KYC, en metode som styrker anonymiteten. Videre tilbyr noen utvekslingsplattformer som Kraken lavere uttaksgebyrer enn andre, i tråd med Bitcoin-prinsippene.
Bisq, Robosat, og Peach presenteres som demokratiske løsninger for Bitcoin-handel. Peach, spesielt, er fremhevet for sin enkel tilgang som en mobilapplikasjon. Det er imidlertid utfordringer å ta tak i, inkludert reguleringen av kryptovalutaer og behovet for å respektere visse grenser for å unngå overdreven regulering.

Bruken av Bitcoin-ATMer diskuteres også; disse representerer en økonomisk metode for å skaffe non-KYC bitcoins. Avhengig av lokale reguleringer, kan disse ATMene installeres hjemme eller på offentlige steder og kan brukes til å tilby bitcoins til nære eller for betalinger i barer.

Opplæringen understreker viktigheten av utdanningens rolle i forståelsen av Bitcoin. Det antydes at Bitcoin kan tilby en løsning i tilfelle av resesjon eller hyperinflasjon, og at det er viktig å øke bevisstheten om dens potensial før det er for sent. Videre fremheves det at separasjonen av stat og penger er like essensiell som separasjonen av stat og religion.

Til slutt presenteres Bitcoin som en desentralisert valuta som krever offentlig utdanning og et åpent sinn for å bli fullt ut forstått og utnyttet. Opplæringen har som mål å hjelpe deltakerne med å forstå de ulike peer-to-peer kjøpsløsningene og å bruke disse verktøyene for å forbedre deres anonymitet og sikkerhet når de bruker Bitcoin.

## Evaluer dette kurset
<chapterId>a6410a99-adfc-50fd-a004-8048be620c8a</chapterId>
<isCourseReview>true</isCourseReview>

## Avsluttende eksamen
<chapterId>38d03a01-ae5f-5c21-acd4-42f18b20c2b4</chapterId>
<isCourseExam>true</isCourseExam>

## Bonusartikkel om personvern
<chapterId>9f1aa75a-3031-58b2-9d4a-11a5c4197302</chapterId>

En flott [artikkel](https://decouvrebitcoin.fr/tribune-sur-le-kyc-et-lidentification-des-bitcoins-onchain/) av Loïc Morel om KYC og identifikasjon
Denne grundige artikkelen utforsker utfordringene og løsningene for å bevare personvernet ved anskaffelse og bruk av bitcoins. Loïc dekonstruerer noen vanlige misforståelser om KYC (Know Your Customer) identifikasjon, detaljerer risikoene forbundet med denne prosessen, og tilbyr teknikker for å opprettholde anonymiteten til transaksjoner. Det er et must-read for de som ser etter å forstå nyansene av personvern i Bitcoin-verdenen, og for å lære hvordan man bruker verktøy som CoinJoin, Stonewall, og PayJoin for å skjule sporing av transaksjoner og dermed beskytte sitt personvern.