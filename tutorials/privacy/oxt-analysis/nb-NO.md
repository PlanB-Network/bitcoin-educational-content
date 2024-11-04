---
name: OXT - Chain Analysis
description: Bli kjent med grunnleggende om kjedeanalyse på Bitcoin
---
![cover](assets/cover.webp)

***ADVARSEL:** Etter arrestasjonen av grunnleggerne av Samourai Wallet og beslagleggelsen av deres servere den 24. april, **er nettsiden OXT.me for øyeblikket utilgjengelig**. Det er likevel mulig at dette verktøyet kan bli relansert i de kommende ukene. I mellomtiden kan du fortsatt dra nytte av denne opplæringen for å forstå grunnleggende om kjedeanalyse på Bitcoin. Alle heuristikker og mønstre som presenteres her, forblir anvendelige på Bitcoin-transaksjoner. Selv om disse verktøyene er mindre optimaliserte enn OXT, kan du midlertidig bruke [Mempool.space](https://mempool.space/) eller [Bitcoin Explorer](https://bitcoinexplorer.org/) for å sette de teoretiske konseptene i denne artikkelen ut i praksis.*

_Vi følger nøye med på utviklingen av denne saken samt utviklingen angående de tilknyttede verktøyene. Vær trygg på at vi vil oppdatere denne opplæringen så snart ny informasjon blir tilgjengelig._

_Denne opplæringen er gitt kun for utdannings- og informasjonsformål. Vi støtter eller oppfordrer ikke til bruk av disse verktøyene til kriminelle formål. Det er hver brukers ansvar å overholde lovene i sin jurisdiksjon._

---

I denne artikkelen vil du lære de essensielle teoretiske grunnlagene som trengs for å begynne med grunnleggende kjedeanalyser på Bitcoin, og viktigere, for å forstå hvordan de som observerer deg opererer. Selv om denne artikkelen ikke er en praktisk opplæring i OXT-verktøyet (et emne vi vil dekke i en fremtidig opplæring), samler den et sett med avgjørende kunnskap for bruken av det. For hver modell, metrikk og indikator som presenteres, er det gitt en lenke til en eksempeltransaksjon på OXT, som vil tillate deg å bedre forstå bruken av den og å øve deg parallelt med lesingen.

## Introduksjon
En av pengenes funksjoner er å løse problemet med dobbel sammentreff av ønsker. I et system basert på byttehandel krever gjennomføringen av en utveksling ikke bare å finne en person som tilbyr en vare som møter mitt behov, men også å tilby dem en vare av tilsvarende verdi som tilfredsstiller deres eget behov. Å finne denne balansen viser seg å være kompleks. Derfor tyr vi til penger, som lar oss flytte verdi både i rom og tid.

For at penger skal løse dette problemet, er det essensielt at parten som tilbyr en vare eller tjeneste er overbevist om sin evne til å bruke den summen senere. Dermed vil enhver rasjonell person som er villig til å akseptere et pengebeløp, enten det er digitalt eller fysisk, sørge for at det oppfyller to grunnleggende kriterier:
- Mynten må være intakt og autentisk;
- og den må ikke være dobbeltbrukt.

Hvis vi bruker fysisk penger, er det den første egenskapen som er mest kompleks å fastslå. I forskjellige perioder i historien har integriteten til metallmynter ofte blitt påvirket av praksiser som klipping eller boring. For eksempel, i det gamle Roma, var det vanlig for borgere å skrape kantene på gullmynter for å samle litt edelmetall, samtidig som de beholdt dem for fremtidige transaksjoner. Dette er spesielt grunnen til at riller senere ble stemplet på kanten av mynter. Autentisitet er også en vanskelig egenskap å verifisere på et fysisk penge-medium. I dag er teknikker for å bekjempe forfalskning stadig mer komplekse, noe som tvinger handelsmenn til å investere i dyre verifikasjonssystemer.

På den annen side, på grunn av deres natur, er dobbeltbruk ikke et problem for fysiske valutaer. Hvis jeg gir deg en €10 seddel, forlater den uopprettelig min besittelse for å gå inn i din, og utelukker dermed enhver mulighet for flere utgifter av de monetære enhetene den representerer.
For digital valuta er utfordringen annerledes. Å sikre autentisiteten og integriteten til en mynt er ofte enklere, men å sikre fraværet av dobbeltutgifter er mer komplekst. Hver digital vare er i bunn og grunn informasjon. I motsetning til fysiske varer, deler ikke informasjon seg under utvekslinger, men sprer seg ved å multiplisere. For eksempel, hvis jeg sender deg et dokument via e-post, blir det deretter duplisert. På din ende, kan du ikke verifisere med sikkerhet at jeg har slettet det originale dokumentet.

Den eneste måten å unngå denne dupliseringen av en digital vare på, er å være klar over alle utvekslingene i systemet. På denne måten kan man vite hvem som eier hva og oppdatere alles kontoer basert på transaksjonene som er gjort. Dette er det som gjøres, for eksempel, med bokførte penger. Når du betaler €10 til en handelsmann med kredittkort, noterer banken denne utvekslingen og oppdaterer hovedboken.

På Bitcoin, blir forebyggingen av dobbeltutgifter gjort på samme måte. Det søkes å bekrefte fraværet av en transaksjon som allerede har brukt myntene i spørsmålet. Hvis disse aldri har blitt brukt, da kan vi være sikre på at ingen dobbeltutgifter vil forekomme. Dette er den berømte setningen fra Satoshi Nakamoto i White Paper: "*Den eneste måten å bekrefte fraværet av en transaksjon på, er å være klar over alle transaksjoner.*"

I motsetning til bankmodellen, på Bitcoin, ønsker vi ikke å måtte stole på en sentral enhet. Derfor må alle brukere kunne bekrefte dette fraværet av dobbeltutgifter, uten å stole på en tredjepart. Således må alle være klar over alle Bitcoin-transaksjoner.

Det er nettopp denne offentlige spredningen av informasjon som kompliserer beskyttelsen av personvern på Bitcoin. I det tradisjonelle banksystemet, i teorien, er det bare finansinstitusjonen som er klar over transaksjonene som er gjort. Imidlertid, på Bitcoin, er alle brukere informert om alle transaksjoner, via deres respektive noder.

På grunn av denne begrensningen på spredning, skiller Bitcoins personvernmodell seg fra den i banksystemet. I sistnevnte er transaksjoner assosiert med brukerens identitet, men informasjonsflyten er kuttet av mellom den betrodde tredjeparten og offentligheten. Med andre ord, din bankmann vet at du kjøper baguetten din hver morgen på det lokale bakeriet, men din nabo er ikke klar over alle disse transaksjonene. I tilfellet med Bitcoin, siden informasjonsflyten ikke kan brytes mellom transaksjoner og det offentlige domenet, stoler personvernmodellen på å skille brukerens identitet fra transaksjonene selv.
![analyse](assets/en/1.webp)
*Diagram inspirert av Satoshi Nakamotos i White Paper: Bitcoin: A Peer-to-Peer Electronic Cash System, seksjon 10 "Privacy".*
Siden Bitcoin-transaksjoner gjøres offentlige, blir det mulig å etablere koblinger mellom dem for å utlede informasjon om de involverte partene. Denne aktiviteten utgjør til og med en spesialitet i seg selv, vanligvis kalt "kjedeanalyse". I denne artikkelen inviterer jeg deg til å utforske grunnleggende om kjedeanalyse for å forstå hvordan dine bitcoins blir sporet.

Flertallet av selskaper som spesialiserer seg på kjedeanalyse opererer som svarte bokser, og avslører ikke sine metodologier. Derfor er det vanskelig å få informasjon om denne praksisen. For skrivingen av denne artikkelen, stolte jeg hovedsakelig på de få åpne ressursene som er tilgjengelige:
- Hoveddelen av artikkelen min er hentet fra serien av fire artikler kalt: [Understanding Bitcoin Privacy with OXT](https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923), produsert av Samourai Wallet i 2021;
- Jeg brukte også ulike rapporter fra [OXT Research](https://medium.com/oxt-research), samt deres gratis kjedeanalyseverktøy;
- Mer generelt kommer kunnskapen min fra de forskjellige tweetene og innholdet fra [@LaurentMT](https://twitter.com/LaurentMT) og [@ErgoBTC](https://twitter.com/ErgoBTC);- Jeg ble også inspirert av [Space Kek #19](https://podcasters.spotify.com/pod/show/decouvrebitcoin/episodes/SpaceKek-19---Analyse-de-chane--anonsets-et-entropie-e1vfuji) der jeg deltok sammen med [@louneskmt](https://twitter.com/louneskmt), [@TheoPantamis](https://twitter.com/TheoPantamis), [@Sosthene___](https://twitter.com/Sosthene___), og [@LaurentMT](https://twitter.com/LaurentMT).

Jeg vil gjerne takke deres forfattere, utviklere og produsenter. Uten deres ulike innhold og programvare, ville denne artikkelen ikke eksistert. Jeg takker også anmelderne som nøye korrigerte denne teksten og velsignet meg med deres ekspertise:
- [Gilles Cadignan](https://twitter.com/gillesCadignan);
- [Ludovic Lars](https://twitter.com/lugaxker) ([https://viresinnumeris.fr/](https://viresinnumeris.fr/)).

*Til din informasjon, jeg har lagt til et teknisk miniglossar på slutten av artikkelen for å definere visse termer. Hvis du ser et ord du ikke forstår med en asterisk, er definisjonen nederst på siden.*

## Hva er kjedeanalyse?
Kjedeanalyse er en praksis som omfatter alle metoder for å spore Bitcoin-flyt på blokkjeden. Generelt sett stoler kjedeanalyse på å observere karakteristikker i prøver av tidligere transaksjoner. Deretter involverer det å identifisere disse samme karakteristikkene i en transaksjon som man ønsker å analysere og dedusere plausible tolkninger. Denne problemløsningsmetoden, basert på en praktisk tilnærming for å finne en tilstrekkelig god løsning, er det som kalles en heuristikk.

For å forenkle, kjedeanalyse gjøres i to hovedtrinn:
1. Identifikasjonen av kjente karakteristikker;
2. Deduksjonen av hypoteser.

Ett av målene med kjedeanalyse er å gruppere ulike aktiviteter på Bitcoin for å bestemme unikheten til brukeren som utførte dem. Etterfølgende vil det være mulig å forsøke å koble denne bunten av aktiviteter til en reell identitet.

Husk min introduksjon. Jeg forklarte hvorfor Bitcoins personvernmodell opprinnelig støttet seg på å skille brukerens identitet fra deres transaksjoner. Det ville derfor være fristende å tenke at kjedeanalyse er unødvendig, siden selv om man klarer å gruppere on-chain aktiviteter, kan de ikke assosieres med en reell identitet. Teoretisk sett er denne uttalelsen nøyaktig. Kryptografiske nøkkelpar brukes til å etablere betingelser på UTXOene. I sin essens avslører disse nøkkelparene ingen informasjon om identiteten til deres innehavere. Så selv om man lykkes i å gruppere aktiviteter assosiert med forskjellige nøkkelpar, forteller dette oss ingenting om enheten bak disse aktivitetene.
Men i praksis er virkeligheten mye mer kompleks. Det finnes en mengde atferder som risikerer å koble en ekte identitet til en aktivitet på kjeden. I analyse kalles dette et inngangspunkt, og det finnes mange av dem. Det mest vanlige er selvfølgelig KYC (Know Your Customer). Hvis du tar ut dine bitcoins fra en regulert plattform til en av dine personlige mottaksadresser, så er det noen som kan koble din identitet til denne adressen. Mer generelt kan et inngangspunkt være enhver form for interaksjon mellom ditt virkelige liv og en Bitcoin-transaksjon. For eksempel, hvis du publiserer en mottaksadresse på dine sosiale nettverk, kan dette være et inngangspunkt for analyse. Hvis du gjør en betaling i bitcoins til din baker, kan de assosiere ditt ansikt (som er en del av din identitet) med en Bitcoin-adresse. Disse inngangspunktene er nesten uunngåelige når man bruker Bitcoin. Selv om man kan forsøke å begrense deres omfang, vil de forbli til stede. Derfor er det avgjørende å kombinere metoder som tar sikte på å bevare ditt personvern. Selv om det å opprettholde en akseptabel separasjon mellom din virkelige identitet og dine transaksjoner er en prisverdig tilnærming, er det fortsatt utilstrekkelig. Faktisk, hvis alle dine aktiviteter på kjeden kan grupperes sammen, så kan selv det minste inngangspunktet kompromittere det eneste laget av personvern du hadde etablert.

Derfor er det også nødvendig å håndtere kjedeanalyse i vår bruk av Bitcoin. Ved å gjøre dette, kan vi minimere aggregeringen av våre aktiviteter og begrense innvirkningen av et inngangspunkt på vårt personvern. Nøyaktig, for å bedre motvirke kjedeanalyse, hva er en bedre tilnærming enn å gjøre seg kjent med metodene som brukes i kjedeanalyse? Hvis du vil vite hvordan du kan forbedre ditt personvern på Bitcoin, må du forstå disse metodene. Dette vil tillate deg å bedre forstå teknikker som [Coinjoin](https://planb.network/en/tutorials/privacy/coinjoin-samourai-wallet) eller [Payjoin](https://planb.network/en/tutorials/privacy/payjoin), og å redusere feilene du kanskje gjør.

I dette kan vi trekke en analogi med kryptografi og kryptoanalyse. En god kryptograf er først og fremst en god kryptoanalytiker. For å forestille seg en ny krypteringsalgoritme, må man vite hvilke angrep den vil møte, og også studere hvorfor tidligere algoritmer ble brutt. Samme prinsipp gjelder for personvern på Bitcoin. Å forstå metodene for kjedeanalyse er nøkkelen til å beskytte mot det. Derfor tilbyr jeg deg denne artikkelen.

Det er avgjørende å forstå at kjedeanalyse ikke er en eksakt vitenskap. Den stoler på heuristikker avledet fra tidligere observasjoner eller logiske tolkninger. Disse reglene tillater ganske pålitelige resultater, men aldri med absolutt presisjon. Med andre ord, kjedeanalyse innebærer alltid en dimensjon av sannsynlighet i de konklusjonene som trekkes. Vi kan estimere med mer eller mindre sikkerhet at to adresser tilhører samme enhet, men total sikkerhet vil alltid være utenfor rekkevidde.

Hele målet med kjedeanalyse ligger nettopp i aggregeringen av ulike heuristikker for å minimere risikoen for feil. Det er på en måte en akkumulering av bevis som lar oss komme nærmere virkeligheten.

Disse berømte heuristikkene kan grupperes inn i forskjellige kategorier som vi vil detaljere sammen:
- Transaksjonsmønstre (eller transaksjonsmodeller);
- Interne heuristikker til transaksjonen;
- Eksterne heuristikker til transaksjonen.

Det er verdt å merke seg at de to første heuristikkene på Bitcoin ble formulert av Satoshi Nakamoto selv. Han diskuterer dem i del 10 av White Paper. Som vi vil se senere, er det interessant å observere at disse to heuristikkene fortsatt opprettholder en preeminens i kjedeanalyse i dag. Disse er:
- den Felles Inngangs-Eierskap Heuristikken (CIOH);
- og adresse gjenbruk.
La oss utforske sammen de observerbare kjennetegnene og tolkningene som kan trekkes for å gjennomføre en analyse.
## Transaksjonsmønstre (eller transaksjonsmodeller)
Et transaksjonsmønster er rett og slett en typisk transaksjonsmodell som kan finnes på blockchain, hvis tolkning sannsynligvis er kjent. Når vi studerer mønstre, vil vi fokusere på en enkelt transaksjon som vi vil analysere på et høyt nivå. Med andre ord, vi vil bare se på antall innganger og utganger, uten å dvele ved dens mer spesifikke detaljer eller dens miljø. Fra den observerte modellen vil vi kunne tolke transaksjonens natur. Vi vil deretter se etter kjennetegn ved dens struktur og utlede en tolkning.

### Den enkle sendingen (eller enkel betaling)
Denne modellen kjennetegnes av forbruket av en eller flere UTXOer som inngang og produksjonen av to UTXOer som utgang.

![analyse](assets/en/2.webp)

Tolkningen av denne modellen er at vi er i nærvær av en sende- eller betalingstransaksjon. Brukeren har forbrukt sine egne UTXOer som inngang for å tilfredsstille i utgang en betalings-UTXO og en veksel-UTXO (veksel som kommer tilbake til samme bruker). Vi vet derfor at den observerte brukeren sannsynligvis ikke lenger er i besittelse av en av de to UTXOene i utgang (betalingsen), men fortsatt er i besittelse av den andre UTXOen (vekselen).

På dette tidspunktet er det umulig for oss å spesifisere hvilken utgang som representerer hvilken UTXO, siden det ikke er målet med denne modellen. Vi vil kunne gjøre dette ved å stole på heuristikkene som vi vil studere i den følgende delen. På dette stadiet er vårt mål begrenset til å identifisere naturen til transaksjonen i spørsmål, som i dette tilfellet er en enkel sending.

For eksempel, her er en Bitcoin-transaksjon som adopterer mønsteret for enkel sending:
### Sweep ("sweep" på engelsk)
Denne modellen kjennetegnes av forbruket av en enkelt UTXO som inngang og produksjonen av en enkelt UTXO som utgang.

![analyse](assets/en/3.webp)

Tolkningen av denne modellen er at vi er i nærvær av en selvoverføring. Brukeren har overført sine bitcoins til seg selv, til en annen adresse de eier. Siden det ikke er noen endring i transaksjonen, er det svært usannsynlig at vi har med en betaling å gjøre. Vi vet da at den observerte brukeren sannsynligvis fortsatt er i besittelse av denne UTXOen.

For eksempel, her er en Bitcoin-transaksjon som adopterer sweep-mønsteret:
[35f1072a0fda5ae106efb4fda871ab40e1f8023c6c47f396441ad4b995ea693d](https://mempool.space/tx/35f1072a0fda5ae106efb4fda871ab40e1f8023c6c47f396441ad4b995ea693d)

Men, denne typen mønster kan også avsløre en selvoverføring til en konto på en børs (kryptovalutabørsplattform). Det vil være studiet av kjente adresser og konteksten til transaksjonen som vil tillate oss å vite om det er en sweep til en selvforvaltet lommebok eller et uttak til en plattform.

### Konsolidering
Denne modellen kjennetegnes av forbruket av flere UTXOer som inngang og produksjonen av en enkelt UTXO som utgang.

![analyse](assets/en/4.webp)
Tolkningen av denne modellen er at vi er i nærvær av en konsolidering. Dette er en vanlig praksis blant Bitcoin-brukere, med mål om å slå sammen flere UTXOer i forventning om en mulig økning i transaksjonsgebyrer. Ved å utføre denne operasjonen i en periode når gebyrene er lave, er det mulig å spare på fremtidige gebyrer.
Vi kan utlede at brukeren bak denne transaksjonen sannsynligvis var i besittelse av alle UTXOene på inngangen og fortsatt er i besittelse av UTXOen på utgangen. Derfor er det sikkert en selvoverføring.

Akkurat som med feiingen, kan denne typen mønster også avsløre en selvoverføring til en børskonto. Det vil være studiet av kjente adresser og konteksten til transaksjonen som vil tillate oss å vite om det er en konsolidering til en selvforvaltet lommebok eller et uttak til en plattform.

For eksempel, her er en Bitcoin-transaksjon som adopterer konsolideringsmønsteret:
[77c16914211e237a9bd51a7ce0b1a7368631caed515fe51b081d220590589e94](https://mempool.space/tx/77c16914211e237a9bd51a7ce0b1a7368631caed515fe51b081d220590589e94)
### Modellen for Batch-utgifter
Denne modellen kjennetegnes av forbruket av noen få UTXOer som inngang (ofte bare én) og produksjonen av mange UTXOer som utgang.

![analyse](assets/en/5.webp)

Tolkningen av denne modellen er at vi er i nærvær av en batch-utgift. Dette er en praksis som sannsynligvis avslører betydelig økonomisk aktivitet, som for eksempel en børs. Batch-utgifter lar disse enhetene spare på gebyrer ved å kombinere sine utgifter i en enkelt transaksjon.

Vi kan utlede at UTXO-inngangen kommer fra et selskap med betydelig økonomisk aktivitet og at UTXO-utgangene vil dispergere. Noen vil tilhøre selskapets kunder. Andre kan gå mot partnerbedrifter. Til slutt vil det sikkert være en endring som returnerer til det utstedende selskapet.

For eksempel, her er en Bitcoin-transaksjon som adopterer mønsteret for batch-utgifter:
[8a7288758b6e5d550897beedd13c70bcbaba8709af01a7dbcc1f574b89176b43](https://mempool.space/tx/8a7288758b6e5d550897beedd13c70bcbaba8709af01a7dbcc1f574b89176b43)

### Protokollspesifikke Transaksjoner
Blant transaksjonsmønstrene kan vi også identifisere modeller som avslører bruken av en spesifikk protokoll. For eksempel vil Whirlpool coinjoins ha en lett gjenkjennelig struktur som gjør det mulig å skille dem fra andre klassiske transaksjoner.

![analyse](assets/en/6.webp)

Analysen av dette mønsteret antyder at vi sannsynligvis er i nærvær av en samarbeidstransaksjon. Det er også mulig å observere en coinjoin. Hvis denne siste hypotesen viser seg å være nøyaktig, kan antallet utganger gi oss et omtrentlig estimat av antall deltakere.

For eksempel, her er en Bitcoin-transaksjon som adopterer mønsteret for samarbeidstransaksjonstypen coinjoin:
[00601af905bede31086d9b1b79ee8399bd60c97e9c5bba197bdebeee028b9bea](https://mempool.space/tx/00601af905bede31086d9b1b79ee8399bd60c97e9c5bba197bdebeee028b9bea)
Det finnes mange andre protokoller som har sine egne spesifikke strukturer. Dermed kan vi skille mellom transaksjoner av Wabisabi-typen eller Stamps-transaksjoner, for eksempel.
## Intern Transaksjonsheuristikk
En intern heuristikk er en spesifikk egenskap identifisert innenfor en transaksjon selv, uten behov for å undersøke dens miljø, som lar oss gjøre deduksjoner. I motsetning til mønstre som fokuserer på den overordnede strukturen av transaksjonen, er interne heuristikker basert på settet av uttrekkbare data. Dette inkluderer:
- Mengdene av forskjellige UTXOer både innkommende og utgående;
- Alt relatert til skript: mottaksadresser, versjonering, låsetider...

Generelt lar denne typen heuristikk oss identifisere endringen i en spesifikk transaksjon. Ved å gjøre dette kan vi deretter fortsette å spore en enhet over flere forskjellige transaksjoner.

Jeg minner igjen om at disse heuristikkene ikke er absolutt presise. Tatt individuelt, tillater de oss bare å identifisere plausible scenarioer. Det er akkumuleringen av flere heuristikker som bidrar til å redusere usikkerhet, uten å noen gang fullstendig eliminere den.

### Interne Likhetstrekk
Denne heuristikken involverer å studere likhetene mellom inngangene og utgangene av samme transaksjon. Hvis samme egenskap observeres på inngangene og på bare en av utgangene av transaksjonen, da er det sannsynlig at denne utgangen utgjør endringen.

Det mest åpenbare kjennetegnet er gjenbruk av en mottaksadresse i samme transaksjon.

![analyse](assets/en/7.webp)

Denne heuristikken etterlater lite rom for tvil. Med mindre deres private nøkkel har blitt kompromittert, avslører samme mottaksadresse uunngåelig aktiviteten til en enkelt bruker. Tolkingen som følger er at endringen av transaksjonen er utgangen med samme adresse som inngangen. Dette lar oss fortsette å spore individet fra denne endringen.

For eksempel, her er en transaksjon hvor denne heuristikken sannsynligvis kan anvendes:
[54364146665bfc453a55eae4bfb8fdf7c721d02cb96aadc480c8b16bdeb8d6d0](https://mempool.space/tx/54364146665bfc453a55eae4bfb8fdf7c721d02cb96aadc480c8b16bdeb8d6d0)

Disse likhetene mellom innganger og utganger stopper ikke ved gjenbruk av adresse. Enhver likhet i bruk av skript kan tillate anvendelse av en heuristikk. For eksempel, noen ganger kan samme versjonering mellom en inngang og en av utgangene av transaksjonen observeres.

![analyse](assets/en/8.webp)
I dette diagrammet kan vi se at inngang nummer 0 låser opp et P2WPKH-skript (SegWit V0 som starter med "bc1q"). Utgang nummer 0 bruker samme type skript. Imidlertid bruker utgang nummer 1 et P2TR-skript (SegWit V1 som starter med "bc1p"). Tolkingen av denne egenskapen er at det er sannsynlig at adressen med samme versjonering som inngangen er endringsadressen. Den ville derfor fortsatt tilhøre samme bruker.
Her er en transaksjon hvor denne heuristikken sannsynligvis kan anvendes:
[db07516288771ce5d0a06b275962ec4af1b74500739f168e5800cbcb0e9dd578](https://mempool.space/tx/db07516288771ce5d0a06b275962ec4af1b74500739f168e5800cbcb0e9dd578)
I denne transaksjonen kan vi se at inngangsnummer 0 og utgangsnummer 1 bruker P2WPKH-skript (SegWit V0), mens utgangsnummer 0 bruker en annen skripttype, P2PKH (Legacy).
### Betalinger med Runde Tall
En annen intern heuristikk som kan hjelpe oss med å identifisere vekselen, er den med runde tall. Generelt, når vi står overfor et enkelt betalingsmønster (1 inngang og 2 utganger), hvis en av utgangene bruker et rundt beløp, så representerer det betalingen.

![analyse](assets/en/9.webp)

Ved prosess av eliminering, hvis en utgang representerer betalingen, representerer den andre vekselen. Derfor kan vi tolke at det er sannsynlig at brukeren i inngangen fortsatt besitter utgangen som er identifisert som vekselen.

Det bør bemerkes at denne heuristikken ikke alltid er anvendelig, siden flertallet av betalinger fortsatt gjøres i fiatvalutaenheter. Faktisk, når en handelsmann i Frankrike aksepterer bitcoin, viser de generelt ikke stabile priser i sats. De ville heller foretrekke en konvertering mellom prisen i euro og beløpet i bitcoins som skal betales. Derfor bør det ikke være et rundt tall i transaksjonsutgangen. Likevel kunne en analytiker forsøke å utføre denne konverteringen med tanke på vekslingskursen som var gjeldende da transaksjonen ble kringkastet på nettverket.

Hvis bitcoin en dag blir den foretrukne regnskapsenheten i våre utvekslinger, kunne denne heuristikken bli enda mer nyttig for analyse.

For eksempel, her er en transaksjon hvor denne heuristikken sannsynligvis kan anvendes:
### Det Store Forbruket

Når en tilstrekkelig stor forskjell blir oppdaget mellom to transaksjonsutganger i en enkel betalingsmodell, kan det estimeres at den større utgangen sannsynligvis er vekselen.

![analyse](assets/en/10.webp)

Denne heuristikken om den største utgangen er sannsynligvis den mest upresise av alle. Hvis identifisert alene, er den ganske svak. Imidlertid kan denne egenskapen kombineres med andre heuristikker for å redusere usikkerheten i vår tolkning.

For eksempel, hvis vi undersøker en transaksjon som har en utgang med et rundt beløp og en annen utgang med et større beløp, tillater den felles anvendelsen av heuristikken for runde betalinger og den om den største utgangen oss å redusere vårt usikkerhetsnivå.

For eksempel, her er en transaksjon hvor denne heuristikken sannsynligvis kan anvendes:
[b79d8f8e4756d34bbb26c659ab88314c220834c7a8b781c047a3916b56d14dcf](https://mempool.space/tx/b79d8f8e4756d34bbb26c659ab88314c220834c7a8b781c047a3916b56d14dcf)

## Eksterne Heuristikker til Transaksjonen
Studiet av eksterne heuristikker er analysen av likheter, mønstre og karakteristikker av visse elementer som ikke er iboende til selve transaksjonen. Med andre ord, hvis vi tidligere begrenset oss til å utnytte elementer som er iboende til transaksjonen med interne heuristikker, utvider vi nå vårt analysefelt til transaksjonens miljø takket være eksterne heuristikker.

### Gjenbruk av Adresse
Dette er en av de mest kjente heuristikkene blant Bitcoinere. Gjenbruk av adresse gjør det mulig å etablere en kobling mellom forskjellige transaksjoner og forskjellige UTXOer. Det observeres når en Bitcoin mottaksadresse brukes flere ganger.

Tolkningen av gjenbruk av adresse er at alle UTXOene låst på denne adressen tilhører (eller har tilhørt) samme enhet. Denne heuristikken gir lite rom for usikkerhet. Når den er identifisert, har tolkningen som følger en stor sjanse for å korrespondere med virkeligheten.
Som forklart i introduksjonen, ble denne heuristikken oppdaget av Satoshi Nakamoto selv. I White Paper nevner han spesifikt en løsning for å forhindre brukere fra å produsere den, som rett og slett er å bruke en ny adresse for hver ny transaksjon: "*Som en ekstra brannmur, kunne et nytt par med nøkler brukes for hver transaksjon for å holde dem ulinket til en felles eier.*"
For eksempel, her er en adresse gjenbrukt over flere transaksjoner:
[bc1qqtmeu0eyvem9a85l3sghuhral8tk0ar7m4a0a0](https://mempool.space/address/bc1qqtmeu0eyvem9a85l3sghuhral8tk0ar7m4a0a0)

### Likheten mellom Skript og Lommebokavtrykk
Utover gjenbruk av adresser, er det mange andre heuristikker som kan koble handlinger til samme lommebok eller til en klynge av adresser.

For det første kan en analytiker bruke likheter i skriptbruk. For eksempel kan visse minoritetsskript som multisig være lettere å oppdage enn SegWit V0-skript. Jo større gruppen vi gjemmer oss i, jo vanskeligere er det å oppdage oss. Dette er spesielt grunnen til at, på Coinjoin Whirlpool-protokollen, bruker alle deltakere nøyaktig samme type skript.

Mer generelt kan en analytiker også fokusere på de karakteristiske avtrykkene av en lommebok. Disse er spesifikke prosesser for en bruk som man kan søke å identifisere for å utnytte dem som sporingheuristikker. Med andre ord, hvis man observerer en akkumulering av de samme interne karakteristikkene på transaksjoner tilskrevet den sporede enheten, kan man forsøke å identifisere disse samme karakteristikkene på andre transaksjoner.

For eksempel kan det identifiseres at den sporede brukeren systematisk sender sitt veksel til P2TR*-adresser (bc1p…). Hvis denne prosessen gjentas, kan den brukes som en heuristikk for fortsettelsen av vår analyse. Andre avtrykk kan også brukes, som rekkefølgen av UTXOene, plasseringen av vekselen i utgangene, signaliseringen av RBF (Replace-by-Fee), eller til og med, versjonsnummeret og locktime.
Som [@LaurentMT](https://twitter.com/LaurentMT) spesifiserer i [Space Kek #19](https://podcasters.spotify.com/pod/show/decouvrebitcoin/episodes/SpaceKek-19---Analyse-de-chane--anonsets-et-entropie-e1vfuji) (en frankofon podcast), øker nytten av lommebokavtrykk i kjedeanalyse betydelig over tid. Faktisk, det økende antallet skripttyper og den stadig gradvise utrullingen av disse nye funksjonene av lommebokprogramvare aksentuerer forskjellene. Det skjer til og med at man kan nøyaktig identifisere programvaren brukt av den sporede enheten. Derfor er det viktig å forstå at studiet av et lommeboks avtrykk er spesielt relevant for nylige transaksjoner, mer så enn for de som ble initiert tidlig i 2010-årene.
For å oppsummere, kan et avtrykk være enhver spesifikk praksis, utført automatisk av lommeboken eller manuelt av brukeren, som kan finnes på andre transaksjoner for å assistere i vår analyse.

### CIOH
CIOH, for "Common Input Ownership Heuristic," som kunne oversettes som "heuristikken for felles eierskap av inndata" eller "medforbruk-heuristikken," er en heuristikk som sier at når en transaksjon har flere inndata, kommer disse sannsynligvis alle fra en enkelt enhet. Følgelig er deres eierskap felles.
For å anvende CIOH, observerer man først en transaksjon som har flere innganger. Dette kan være to innganger, så vel som tretti innganger. Når denne egenskapen er oppdaget, sjekker man om transaksjonen ikke passer inn i et kjent mønster. For eksempel, hvis den har 5 innganger med omtrent samme beløp og 5 utganger med nøyaktig samme beløp, vet vi at det er strukturen til en Coinjoin Whirlpool. Derfor kan ikke CIOH anvendes.
Men, hvis transaksjonen ikke passer inn i noe kjent mønster for samarbeidstransaksjon, da kan det tolkes at alle inngangene sannsynligvis kommer fra samme enhet. Dette kan være svært nyttig for å utvide en allerede kjent klynge eller for å fortsette sporingen.

![analyse](assets/en/11.webp)

CIOH ble oppdaget av Satoshi Nakamoto. Han diskuterer det i del 10 av White Paper: "*[...] lenken er uunngåelig med transaksjoner med flere innganger, som nødvendigvis avslører at deres innganger var eid av samme eier. Risikoen er at hvis eieren av en nøkkel blir avslørt, kan lenkene avsløre andre transaksjoner som tilhørte samme eier.*"
Det er spesielt fascinerende å merke seg at Satoshi Nakamoto, selv før den offisielle lanseringen av Bitcoin, allerede hadde identifisert de to hovedpersonvernsvakhetene for brukere, nemlig CIOH og adresse gjenbruk. Slik forutseenhet er ganske bemerkelsesverdig, ettersom disse to heuristikkene forblir, selv i dag, de mest nyttige i kjedeanalyse.

### Off-chain Data
Åpenbart er ikke kjedeanalyse begrenset til on-chain data. Enhver data fra en tidligere analyse eller tilgjengelig på Internett kan også brukes til å forfine en analyse.

For eksempel, hvis det observeres at de sporede transaksjonene systematisk kringkastes fra samme Bitcoin-node og dens IP-adresse kan identifiseres, kan det være mulig å oppdage andre transaksjoner fra samme enhet.

Analytikeren har også muligheten til å stole på analyser som tidligere er gjort åpen kildekode, eller på sine egne tidligere analyser. Kanskje man finner en utgang som peker på en klynge av adresser som allerede hadde blitt identifisert. Noen ganger er det også mulig å stole på utganger som peker til en børs, adressene til disse plattformene er generelt kjent.

På samme måte kan man utføre en analyse ved eliminering. For eksempel, hvis man under analysen av en transaksjon med to utganger, en av dem er knyttet til en kjent, men distinkt klynge av adresser fra enheten som spores, da kan det tolkes at den andre utgangen sannsynligvis representerer vekslingen.

Kjedeanalyse inkluderer også en del av OSINT (Open Source Intelligence) som er litt mer generalist med internett-søk. Dette er grunnen til at det frarådes å poste mottaksadresser direkte på sosiale medier eller på en nettside, enten under et pseudonym eller ikke.

### Temporale Modeller
Man tenker kanskje ikke umiddelbart på det, men visse menneskelige atferder er gjenkjennelige on-chain. Det mest nyttige i en studie er ditt søvnmønster! Ja, når du sover, sender du antageligvis ikke Bitcoin-transaksjoner. Siden du generelt sover på omtrent samme timer, er det vanlig å bruke temporale analyser i on-chain analyse. Det innebærer ganske enkelt å registrere tidspunktene som en gitt enhets transaksjoner blir kringkastet til Bitcoin-nettverket. Å analysere disse temporale mønstrene lar oss utlede mange informasjonsbiter.
Først og fremst kan en temporal analyse noen ganger identifisere naturen til enheten som spores. Hvis man observerer at transaksjoner kringkastes konsekvent over 24 timer, kan dette indikere en sterk økonomisk aktivitet. Entiteten bak disse transaksjonene er sannsynligvis en bedrift, potensielt internasjonal, og kanskje med automatiserte prosedyrer internt.
For eksempel, jeg hadde gjenkjent dette mønsteret for noen uker siden mens jeg analyserte en transaksjon som ved en feiltakelse hadde allokert 19 bitcoins i gebyrer. En enkel tidsanalyse hadde tillatt meg å anta at vi hadde med en automatisert tjeneste å gjøre, og derfor sannsynligvis en stor enhet som en børs: https://twitter.com/Loic_Pandul/status/1701127409712452072
Faktisk, noen dager senere, ble det oppdaget at midlene tilhørte PayPal, via Paxos-børsen.

På den annen side, hvis man ser at det tidsmessige mønsteret er ganske spredt over 16 spesifikke timer, da kan det estimeres at vi har med en individuell bruker å gjøre, eller kanskje en lokal bedrift avhengig av volumene som er utvekslet.

Utover naturen til den observerte enheten, kan det tidsmessige mønsteret også gi oss en omtrentlig lokasjon av brukeren. Vi kan dermed korrelere andre transaksjoner, og bruke tidsstempelet til disse som en ytterligere heuristikk som kan legges til vår analyse.

For eksempel, på adressen som ble gjenbrukt flere ganger som jeg tidligere nevnte, kan man observere at transaksjonene, enten innkommende eller utgående, er konsentrert over et 13-timers intervall.
![analyse](assets/notext/12.webp)
*Kreditt: OXT*

Dette intervallet samsvarer sannsynligvis med Europa, Afrika, eller Midtøsten. Derfor kan det tolkes at brukeren bak disse transaksjonene bor der.

I et annet register, er det også en tidsanalyse av denne typen som tillot hypotesen at Satoshi Nakamoto ikke opererte fra Japan, men faktisk fra USA: [https://medium.com/@insearchofsatoshi/the-time-zones-of-satoshi-nakamoto-aa40f035178f](https://medium.com/@insearchofsatoshi/the-time-zones-of-satoshi-nakamoto-aa40f035178f)

### Analysen av Volumer
En annen ekstern heuristikk som kan brukes er analysen av handelsvolumer. Basert på mengdene til stede i hver transaksjon tilskrevet en enhet, kan denne informasjonen brukes som en ytterligere heuristikk for resten av analysen.
Denne heuristikken er åpenbart ganske svak, men den kan hjelpe med å redusere usikkerhet når den legges til andre heuristikker.

## Hvordan beskytte deg mot kjedeanalyse?
Som en Bitcoin-bruker, har du rett til å beskytte ditt privatliv. Dette stammer fra dine naturlige rettigheter til å eie og disponere over deg selv, som er iboende i hver enkelt, uavhengig av enhver lovgivningsmessig begrensning.

Denne naturlige retten til å beskytte ens privatliv er også omgjort til et krav-rett, nedfelt i Artikkel 12 i Verdenserklæringen om menneskerettigheter, som sier at "*Ingen skal utsettes for vilkårlig innblanding i sitt privatliv, familie, hjem eller korrespondanse, ei heller angrep på sin ære og omdømme. Enhver har rett til lovens beskyttelse mot slik innblanding eller angrep.*".

Imidlertid består kjernen i virksomheten til selskaper som spesialiserer seg på kjedeanalyse nettopp av å trenge inn i din private sfære, og dermed kompromittere konfidensialiteten til din korrespondanse. Mens man kunne håpe at, i samsvar med det nevnte krav-rett, ville stater ivrig forsvare vårt privatliv, ikke bare forsømmer de å gjøre det, men de finansierer også i stor grad finansieringen av disse analysefirmaene. Det ville også være forgjeves å håpe på støtte fra sektorforeninger, som ser ut til å være villige til å gjøre alle innrømmelser i møte med lovgiveren.

De facto eksisterer ikke dette krav-rettet til privatliv på Bitcoin. Det er derfor opp til deg, brukeren, å hevde din naturlige rett og beskytte konfidensialiteten til din korrespondanse. Dette innebærer å ta i bruk ulike teknikker og brukerpraksiser, som vil tillate deg å forhindre eller lure heuristikkene som brukes for kjedeanalyse.

### Unngå å falle inn i heuristikker
Først og fremst, før man vurderer mer radikale metoder, er det tilrådelig å begrense vår eksponering for heuristikkene som brukes for kjedeanalyse så mye som mulig. Som nevnt tidligere, er de to mest kraftfulle heuristikkene adressebruk på nytt og COINJOIN.
Det grunnleggende prinsippet for å sikre ditt personvern på Bitcoin ligger i å bruke en ny, ren adresse for hver innkommende transaksjon til lommeboken din. Adressebruk på nytt er virkelig den største trusselen mot konfidensialitet på Bitcoin.
For en individuell bruker er det veldig enkelt å generere en ny adresse for hver innkommende betaling. Moderne lommebøker gjør dette automatisk så snart du klikker på "Motta". Så, hvis du legger selv den minste vekt på personvernet til transaksjonene dine, representerer bruk av ferske adresser det absolutte minimum. Hvis du noen gang trenger et statisk kontaktpunkt på internett, i stedet for å sette en mottaksadresse, kan du bruke løsninger [som PayNym som implementerer BIP47](https://planb.network/en/tutorials/privacy/paynym-bip47).
Videre, hvis du ønsker å handle mot kjedeanalyse, unngå å slå sammen UTXOer ved inngangen av en transaksjon. Minst, hvis du virkelig trenger å slå sammen, foretrekk UTXOer som har samme kilde. Denne anbefalingen innebærer å ha god styring av dine UTXOer. Når du kjøper dine bitcoins, foretrekk overføringer som involverer store beløp for å maksimere antall betalinger du kan gjøre uten å måtte slå sammen. Jeg råder deg også til å merke dine UTXOer i programvaren din for å identifisere deres opprinnelse og unngå sammenslåing fra distinkte kilder.

Mer generelt, for alle andre heuristikker, trenger du å kjenne dem for å prøve å ikke falle inn i dem:
- Ikke bruk minoritetsskript. Foretrekk SegWit V0 eller muligens SegWit V1;
- Ikke gjør betalinger i runde tall. For eksempel, hvis du trenger å sende 100k sats til en venn, send dem 114,486 sats. De vil kjøpe deg en drink i retur;
- Prøv å ikke alltid ha en endring som er mye større enn betalingsutgangen;
- Ikke post dine mottaksadresser på sosiale medier;
- Bruk din egen node under Tor for å kringkaste dine transaksjoner;
- Prøv å ikke alltid kringkaste dine Bitcoin-transaksjoner på samme tid…

### Bruk av personvernsverktøy
Du kan også ty til metoder som gjør din bruk av Bitcoin tvetydig for å forhindre eller lure kjedeanalyse.

Den mest populære teknikken er sikkert Coinjoin, en samarbeidstransaksjonsstruktur som mobiliserer flere UTXOer av samme beløp. Målet her er å bryte deterministiske lenker, og dermed forhindre analyser fra nåtiden til fortiden og fra fortiden til nåtiden. Coinjoin tillater plausibel benektelse ved å skjule dine mynter innenfor en stor gruppe av uatskillelige mynter. Hvis du vil lære mer om Coinjoin, både teknisk og praktisk, foreslår jeg at du leser disse andre artiklene og veiledningene:
- [COINJOIN - SAMOURAI WALLET](https://planb.network/en/tutorials/privacy/coinjoin-samourai-wallet);
- [COINJOIN - SPARROW WALLET](https://planb.network/en/tutorials/privacy/coinjoin-sparrow-wallet);
- [WHIRLPOOL STATS TOOLS - ANONSETS](https://planb.network/en/tutorials/privacy/wst-anonsets).
![analyse](assets/en/13.webp)

CoinJoin er et utmerket verktøy for å skape plausibel benektelse for mynter, men det er ikke optimalisert for alle brukerens personvernbehov. Spesifikt, CoinJoin ble ikke designet for å bli et betalingsverktøy. Det er veldig rigid om beløpene som utveksles for å perfeksjonere produksjonen av plausibel benektelse. Siden man ikke kan fritt velge mengden av transaksjonsutganger, kan ikke CoinJoin brukes til å gjøre betalinger i bitcoins.
For eksempel, forestill deg at jeg ønsker å betale for min baguette med bitcoins mens jeg optimaliserer mitt personvern. Gitt umuligheten av å velge mengden av den resulterende UTXO fra CoinJoin, ville jeg finne meg selv ute av stand til å justere mengden av mitt forbruk til prisen satt av bakeren. Derfor viser CoinJoin seg å være utilstrekkelig for betalingstransaksjoner.
Andre verktøy har blitt utviklet for å møte personvernsbehov i mer spesifikke bruksområder. For eksempel har vi [PayJoin](https://planb.network/en/tutorials/privacy/payjoin), en slags mini-CoinJoin, som involverer kun to deltakere og er basert på en struktur som tillater betaling.

Det unike med PayJoin ligger i dens evne til å produsere en transaksjon som ser vanlig ut, mens den faktisk er en mini-CoinJoin mellom to brukere. I denne strukturen deltar mottakeren av transaksjonen blant inndataene sammen med den faktiske avsenderen. Således setter mottakeren inn en betaling til seg selv innenfor transaksjonen som letter den faktiske betalingen.

For eksempel, hvis du kjøper en baguette fra bakeren din for 6,000 sats fra en UTXO på 10,000 sats, og du ønsker å gjøre en PayJoin, vil bakeren din legge til en UTXO på 15,000 sats som tilhører dem som en inndata til din opprinnelige transaksjon, som de vil fullstendig gjenvinne som en utdata, for å lure heuristikkene:

![analyse](assets/en/14.webp)

Transaksjonsgebyrer er neglisjert for å forenkle forståelsen av ordningen.

Målene med PayJoin er todelt. For det første, sikter den til å lure en ekstern observatør ved å skape en avledning gjennom COH. Faktisk, når en analytiker observerer denne transaksjonen, vil de tro at de kan anvende COH, og dermed anta en felles eierskap av de forskjellige inndataene. I virkeligheten er denne antagelsen feil, ettersom en inndata tilhører avsenderen, mens den andre er eid av mottakeren. Derfor korrumperer PayJoin kjedeanalyse ved å lede analytikeren ned feil sti.
Det andre målet med PayJoin er å lure analytikeren om det faktiske beløpet av transaksjonen, takket være den spesifikke strukturen av dens utdata. Således faller PayJoin innenfor feltet av steganografi. Det tillater det virkelige beløpet av transaksjonen å bli skjult innenfor en bedragersk transaksjon.

Faktisk, hvis vi gjenbesøker vårt eksempel på å bruke PayJoin for å kjøpe en baguette, kan en ekstern observatør tro at vi har å gjøre med en betaling på 4,000 sats eller 21,000 sats. I virkeligheten er betalingen for baguetten 6,000 sats: 21,000 - 15,000 = 6,000. Den virkelige verdien av betalingen er derfor skjult innenfor en falsk betaling som fungerer som en avledning for kjedeanalyse.

Utover PayJoin og CoinJoin, finnes det mange andre Bitcoin transaksjonsstrukturer som enten blokkerer kjedeanalyse eller bedrar den. Blant disse, kunne jeg nevne [Stonewall](https://planb.network/en/tutorials/privacy/stonewall) og [StonewallX2](https://planb.network/en/tutorials/privacy/stonewall-x2) transaksjoner, som tillater enten å lage en fleksibel mini Coinjoin eller å imitere en fleksibel mini Coinjoin. Det finnes også [Ricochet](https://planb.network/en/tutorials/privacy/ricochet) transaksjoner som simulerer en endring av eierskap av bitcoins ved å gjøre en mengde falske overføringer til seg selv.

Alle disse verktøyene er tilgjengelige på Samourai Wallet på mobil, og Sparrow Wallet på PC. Hvis du ønsker å lære mer om disse spesifikke transaksjonsstrukturene, råder jeg deg til å oppdage mine veiledninger:
- [PAYJOIN](https://planb.network/en/tutorials/privacy/payjoin);
- [PAYJOIN - SAMOURAI WALLET](https://planb.network/en/tutorials/privacy/payjoin-samourai-wallet);
- [PAYJOIN - SPARROW WALLET](https://planb.network/en/tutorials/privacy/payjoin-sparrow-wallet);
- [STONEWALL](https://planb.network/en/tutorials/privacy/stonewall);
- [STONEWALL X2](https://planb.network/en/tutorials/privacy/stonewall-x2);
- [RICOCHET](https://planb.network/en/tutorials/privacy/ricochet).

## Konklusjon
Kjedeanalyse er en praksis som involverer å forsøke å spore flyten av bitcoins på kjeden. For å gjøre dette, ser analytikere etter mønstre og karakteristikker for å trekke mer eller mindre plausible hypoteser og tolkninger.

Nøyaktigheten av disse heuristikkene varierer: noen gir en høyere grad av sikkerhet enn andre, men ingen kan hevde å være ufeilbarlige. Imidlertid kan akkumuleringen av flere konvergerende heuristikker redusere denne iboende tvilen, selv om det forblir umulig å fullstendig eliminere den.
Vi kan kategorisere disse metodene i tre distinkte hovedkategorier:
- Mønstre, fokusert på den generelle strukturen til hver transaksjon;
- Interne heuristikker, som tillater en uttømmende undersøkelse av alle detaljene i en transaksjon, uten å utvide til dens kontekst;
- Eksterne heuristikker, som omfatter analysen av transaksjonen i sitt miljø, samt eventuelle eksterne data som kan gi innsikt.

Som en Bitcoin-bruker, er det essensielt å mestre de grunnleggende prinsippene for kjedeanalyse for effektivt å motvirke den og dermed beskytte ditt personvern.

## Teknisk Mini-Glossar:
**P2PKH:** akronym for Pay to Public Key Hash. Det er en standard skriptmodell brukt for å etablere betingelser for utgifter på en UTXO. Den tillater låsing av bitcoins på en hash av en offentlig nøkkel, det vil si, på en mottakeradresse. Dette skriptet er assosiert med Legacy-standarden og ble introdusert i de første versjonene av Bitcoin av Satoshi Nakamoto. I motsetning til P2PK, hvor den offentlige nøkkelen eksplisitt er inkludert i skriptet, bruker P2PKH et kryptografisk avtrykk av den offentlige nøkkelen, med noe metadata, også kalt en "mottakeradresse". Dette skriptet inkluderer RIPEMD160-hashen av SHA256 av den offentlige nøkkelen og stipulerer at for å få tilgang til midlene, må mottakeren oppgi en offentlig nøkkel som matcher denne hashen, samt en gyldig digital signatur generert fra den tilhørende private nøkkelen. P2PKH-adresser er kodet ved hjelp av Base58Check-formatet, som gir dem motstand mot typografiske feil gjennom bruk av en kontrollsum. Disse adressene starter alltid med tallet 1.
**P2TR:** akronym for Pay to Taproot ("betal til roten"). Det er en standard skriptmodell brukt for å etablere betingelser for bruk av en UTXO. P2TR ble introdusert med implementeringen av Taproot i november 2021. Det benytter Schnorr-protokollen for å aggregere kryptografiske nøkler, samt Merkle-trær for alternative skript, kjent som MAST (Merkelized Alternative Script Tree). I motsetning til tradisjonelle transaksjoner hvor betingelser for bruk er offentlig eksponert (noen ganger ved mottak, noen ganger ved bruk), tillater P2TR skjuling av komplekse skript bak en enkelt tilsynelatende offentlig nøkkel. Teknisk sett låser et P2TR-skript bitcoins på en unik Schnorr offentlig nøkkel, betegnet som K. Imidlertid er denne K-nøkkelen faktisk en aggregat av en offentlig nøkkel P og en offentlig nøkkel M, sistnevnte blir beregnet fra Merkle-roten av en liste over ScriptPubKeys. Nøkkelaggregering utføres ved hjelp av Schnorr-signaturprotokollen. Bitcoins låst med et P2TR-skript kan brukes på to distinkte måter: enten ved å publisere en signatur for den offentlige nøkkelen P, eller ved å oppfylle ett av skriptene inneholdt i Merkle-treet. Det første alternativet kalles "nøkkelsti" og det andre "skriptsti." Således tillater P2TR brukere å sende bitcoins enten til en offentlig nøkkel eller til flere skript etter eget valg. En annen fordel med dette skriptet er at, selv om det er flere måter å bruke en P2TR-utgang på, trenger bare den som brukes å bli avslørt ved bruk, slik at de ubrukte alternativene forblir private. For eksempel, takket være Schnorr nøkkelaggregering, kan den offentlige nøkkelen P selv være en aggregert nøkkel, potensielt representere en multisig. P2TR er en versjon 1 SegWit-utgang, noe som betyr at signaturer for P2TR-innganger lagres i vitnet til en transaksjon, og ikke i ScriptSig. P2TR-adresser bruker Bech32m-koding og starter med bc1p.

**P2WPKH:** Akronym for Pay to Witness Public Key Hash. Det er en standard skriptmodell brukt for å etablere betingelser for bruk av en UTXO. P2WPKH ble introdusert med implementeringen av SegWit i august 2017. Dette skriptet er likt P2PKH (Pay to Public Key Hash), ved at det også låser bitcoins basert på hashen av en offentlig nøkkel, det vil si en mottaksadresse. Forskjellen ligger i hvordan signaturer og skript er inkludert i transaksjonen. I tilfellet med P2WPKH, er informasjonen om signaturskriptet (ScriptSig) flyttet fra den tradisjonelle transaksjonsstrukturen til en egen seksjon kalt Witness. Denne flyttingen er en funksjon av SegWit (Segregated Witness)-oppdateringen. Denne teknikken har fordelen av å redusere størrelsen på transaksjonsdata i hoveddelen, samtidig som den nødvendige skriptinformasjonen for validering beholdes i en egen seksjon. Følgelig er P2WPKH-transaksjoner generelt mindre kostbare med hensyn til gebyrer sammenlignet med Legacy-transaksjoner. P2WPKH-adresser er skrevet ved hjelp av Bech32-koding, noe som bidrar til en mer kortfattet og mindre feilutsatt skriving takket være BCH-kontrollsummen. Disse adressene starter alltid med bc1q, noe som gjør dem lett å skille fra Legacy mottaksadresser. P2WPKH er en versjon 0 SegWit-utgang.
**UTXO:** Akronym for Ubrukt Transaksjonsutgang. En UTXO er en transaksjonsutgang som ennå ikke har blitt brukt eller anvendt som inngang for en ny transaksjon. UTXOer representerer andelen av bitcoins som en bruker eier og som for øyeblikket er tilgjengelige for å bli brukt. Hver UTXO er assosiert med et spesifikt utgangsskript, som definerer de nødvendige betingelsene for å bruke bitcoinene. Transaksjoner i Bitcoin forbruker disse UTXOene som innganger og skaper nye UTXOer som utganger. UTXO-modellen er grunnleggende for Bitcoin, ettersom den tillater enkel verifisering av at transaksjoner ikke forsøker å bruke bitcoins som ikke eksisterer eller allerede har blitt brukt. I bunn og grunn er en UTXO et stykke Bitcoin.