---
name: Ledger Flex
description: Sette opp og bruke Ledger Flex
---
![cover](assets/cover.webp)

En maskinvarelommebok er en elektronisk enhet som er dedikert til å administrere og sikre de private nøklene til en Bitcoin-lommebok. I motsetning til programvarelommebøker (eller hot wallets) som er installert på generelle maskiner som ofte er koblet til Internett, gjør maskinvarelommebøker det mulig å isolere de private nøklene fysisk, noe som reduserer risikoen for hacking og tyveri.

Hovedmålet med en maskinvarelommebok er å minimere enhetens funksjonalitet for å redusere angrepsflaten. Mindre angrepsflate betyr også færre potensielle angrepsvektorer, dvs. færre svake punkter i systemet som angripere kan utnytte for å få tilgang til bitcoins.

Det anbefales å bruke en maskinvarelommebok for å sikre bitcoinsene dine, spesielt hvis du har betydelige beløp, enten i absolutt verdi eller som en andel av de totale eiendelene dine.

Maskinvare-lommebøker brukes i kombinasjon med programvare for lommebokadministrasjon på en datamaskin eller smarttelefon. Programvaren administrerer opprettelsen av transaksjoner, men den kryptografiske signaturen som er nødvendig for å validere transaksjonene, utføres kun i maskinvarelommeboken. Dette betyr at de private nøklene aldri blir eksponert for et potensielt sårbart miljø.

Maskinvare-lommebøker tilbyr dobbel beskyttelse for brukeren: På den ene siden sikrer de bitcoinsene dine mot eksterne angrep ved å holde de private nøklene offline, og på den andre siden tilbyr de generelt bedre fysisk motstand mot forsøk på å trekke ut nøklene. Og det er nettopp ut fra disse to sikkerhetskriteriene at man kan bedømme og rangere de forskjellige modellene som er tilgjengelige på markedet.

I denne veiledningen foreslår jeg å oppdage en av disse løsningene: **Ledger Flex**.

![LEDGER FLEX](assets/notext/01.webp)

## Introduksjon til hovedbok Flex

Ledger Flex er en maskinvarelommebok produsert av det franske selskapet Ledger, som markedsføres til en pris på 249 €.

![LEDGER FLEX](assets/notext/02.webp)

Den har en stor E Ink-berøringsskjerm, en svart-hvitt-skjermteknologi. Dette er den samme teknologien som brukes i elektroniske lesere. E Ink-skjermen gir en klar og lesbar skjerm, selv i sterkt sollys, og bruker svært lite energi, eller ingen i det hele tatt når skjermen er statisk. Det fungerer ved hjelp av mikrokapsler som inneholder svarte og hvite pigmentpartikler. Når en elektrisk ladning tilføres, flytter de svarte eller hvite partiklene seg til overflaten av skjermen, slik at det kan dannes tekst eller bilder.

Ledger Flex er utstyrt med en CC EAL6+-sertifisert "secure element"-brikke, som gir deg avansert beskyttelse mot fysiske angrep på maskinvaren. Skjermen styres direkte av denne brikken. Et vanlig kritikkpunkt er at koden for denne brikken ikke er åpen kildekode, noe som krever en viss grad av tillit til integriteten til denne komponenten. Dette elementet blir imidlertid revidert av uavhengige eksperter.

Når det gjelder bruk, tilbyr Ledger Flex flere tilkoblingsmuligheter: Bluetooth, USB-C og NFC. Den store skjermen gjør det enkelt å verifisere transaksjonsdetaljene dine. Ledger skiller seg også ut fra konkurrentene med sin raske adopsjon av nye Bitcoin-funksjoner, som for eksempel Miniscript.

Etter å ha testet den, er jeg imponert over kvaliteten på produktet. Brukeropplevelsen er utmerket, og enheten er intuitiv. Det er en utmerket maskinvarelommebok. Imidlertid har den to store ulemper etter min mening: manglende evne til å verifisere chipens kode og selvfølgelig prisen, som er betydelig høyere enn konkurrentene. Til sammenligning selges den mest avanserte modellen fra Foundation til 199 dollar, Coinkites til 219,99 dollar, mens den nyeste Trezor, som også er utstyrt med en stor berøringsskjerm, tilbys til 169 €.

## Hvordan kjøpe en Ledger Flex?

Ledger Flex er tilgjengelig for kjøp [på den offisielle nettsiden](https://shop.ledger.com/pages/ledger-flex). Hvis du vil kjøpe den i en fysisk butikk, kan du også finne [listen over sertifiserte forhandlere](https://www.ledger.com/reseller) på Ledgers nettsted.

## Forutsetninger

Når du har mottatt Ledger Flex, er det første trinnet å undersøke emballasjen for å forsikre deg om at den ikke har vært åpnet.

![LEDGER FLEX](assets/notext/03.webp)

Ledger-emballasjen skal inneholde to forseglingsstrimler. Hvis disse stripene mangler eller er skadet, kan det tyde på at maskinvarelommeboken har blitt kompromittert og kanskje ikke er ekte.

![LEDGER FLEX](assets/notext/04.webp)

Når du åpner esken, bør du finne følgende elementer i den:

- The Ledger Flex;
- En USB-C-kabel;
- En brukerhåndbok;
- Kort for å skrive ned huskereglene dine.
![LEDGER FLEX](assets/notext/05.webp)

For denne opplæringen trenger du to programvarer: Ledger Live for å initialisere Ledger Flex, og Sparrow Wallet for å administrere Bitcoin-lommeboken din. Last ned [Ledger Live] (https://www.ledger.com/ledger-live) og [Sparrow Wallet] (https://sparrowwallet.com/download/) fra deres offisielle nettsider.

![LEDGER FLEX](assets/notext/06.webp)

Vi vil snart tilby en veiledning om hvordan du kan verifisere ektheten og integriteten til programvaren du laster ned. Jeg anbefaler på det sterkeste å gjøre det her for Ledger Live og Sparrow.

## Hvordan initialiserer jeg en Ledger Flex med Ledger Live?

Slå på Ledger Flex ved å trykke på høyre sideknapp i noen sekunder.

![LEDGER FLEX](assets/notext/07.webp)

Bla gjennom de ulike introduksjonssidene.

![LEDGER FLEX](assets/notext/08.webp)

Velg alternativet "*Sett opp uten Ledger Live*", og klikk deretter på knappen "*Skipp Ledger Live*".

![LEDGER FLEX](assets/notext/09.webp)

Du blir deretter bedt om å velge et navn for hovedboken. Klikk på "*Sett navn*", og skriv deretter inn det navnet du ønsker.

![LEDGER FLEX](assets/notext/10.webp)

Velg PIN-koden for enheten din, som skal brukes til å låse opp hovedboken. Dette er derfor en beskyttelse mot uautorisert fysisk tilgang. Denne PIN-koden spiller ingen rolle i utledningen av lommebokens kryptografiske nøkler. Selv uten tilgang til denne PIN-koden vil du derfor kunne få tilgang til bitcoinsene dine igjen ved hjelp av den 24 ord lange minnefrasen din.

Det anbefales å velge en 8-sifret PIN-kode, så tilfeldig som mulig. Sørg også for å lagre denne koden på et annet sted enn der Ledger Flex er lagret (for eksempel i en passordbehandler).

![LEDGER FLEX](assets/notext/11.webp)

Tast inn PIN-koden en gang til for å bekrefte den.

![LEDGER FLEX](assets/notext/12.webp)

Du vil deretter bli bedt om å velge mellom å gjenopprette en eksisterende lommebok eller opprette en ny. I denne veiledningen skal vi opprette en ny lommebok fra bunnen av, så velg alternativet "*Set up as a new Ledger*" for å generere en ny minnefrase.

![LEDGER FLEX](assets/notext/13.webp)

Flex vil gi deg instruksjoner om hvordan du skal håndtere restitusjonsfrasen din.

**Denne huskeregelen gir fullstendig og ubegrenset tilgang til alle bitcoinsene dine**. Alle som er i besittelse av denne frasen kan stjele pengene dine, selv uten fysisk tilgang til hovedboken din. Frasen på 24 ord gjør det mulig å gjenopprette tilgangen til bitcoinsene dine i tilfelle tap, tyveri eller skade på din Ledger Flex. Det er derfor svært viktig å lagre og oppbevare den på et sikkert sted.

Du kan skrive det ned på papparket som følger med hovedboken, eller for ekstra sikkerhet anbefaler jeg at du graverer det inn på et medium av rustfritt stål for å beskytte mot brann, oversvømmelse eller kollaps.

Du kan bla gjennom disse instruksjonene og hoppe over sider ved å trykke på skjermen.

![LEDGER FLEX](assets/notext/14.webp)

Hovedboken vil lage minnefrasen din ved hjelp av en tilfeldig tallgenerator. Forsikre deg om at du ikke blir observert under denne operasjonen. Skriv ned ordene du får fra Ledger på det fysiske mediet du ønsker. Avhengig av sikkerhetsstrategien din, kan du vurdere å lage flere fullstendige fysiske kopier av frasen (men viktigst av alt, ikke del den opp). Det er viktig å holde ordene nummererte og i sekvensiell rekkefølge.

***Du bør selvsagt aldri dele disse ordene på internett, i motsetning til hva jeg gjør i denne veiledningen. Dette eksemplet på en lommebok vil kun bli brukt på Testnet, og vil bli slettet ved slutten av opplæringen ***

![LEDGER FLEX](assets/notext/15.webp)

Klikk på knappen "*Neste*" for å gå videre til neste ordgruppe. Når alle ordene er notert, klikker du på knappen "*Done*" for å gå videre til neste trinn.

![LEDGER FLEX](assets/notext/16.webp)

Klikk på knappen "*Start bekreftelse*", og velg deretter ordene fra huskesetningen i riktig rekkefølge for å bekrefte at du har notert dem riktig. Fortsett denne prosedyren til det 24. ordet.

![LEDGER FLEX](assets/notext/17.webp)

Hvis frasen du bekrefter, stemmer nøyaktig overens med den som Flex ga deg i forrige trinn, kan du fortsette. Hvis ikke, betyr det at den fysiske sikkerhetskopien av minnefrasen er feil, og at du må starte prosessen på nytt.

![LEDGER FLEX](assets/notext/18.webp)

Og der har du det, frøet ditt er riktig opprettet på din Ledger Flex. Før vi fortsetter med å opprette en ny Bitcoin-lommebok fra dette frøet, la oss utforske enhetsinnstillingene sammen.

## Hvordan endrer du innstillingene i hovedboken?

Du låser og låser opp hovedboken ved å trykke på sideknappen. Du vil da bli bedt om å taste inn PIN-koden du har angitt i forrige trinn.

![LEDGER FLEX](assets/notext/19.webp)

Du får tilgang til innstillingene ved å klikke på tannhjulsymbolet nederst til venstre på enheten.

![LEDGER FLEX](assets/notext/20.webp)

I menyen "*Navn*" kan du endre navnet på hovedboken.

![LEDGER FLEX](assets/notext/21.webp)

I "*Om denne hovedboken*" finner du informasjon om din Flex.

![LEDGER FLEX](assets/notext/22.webp)

I menyen "*Låseskjerm*" har du mulighet til å endre bildet som vises på låseskjermen ved å velge "*Tilpass låseskjermbilde*". Takket være enhetens E Ink-skjermteknologi er det mulig å holde skjermen konstant på uten å bruke batteri. E Ink-skjermer bruker ikke energi til å opprettholde et statisk bilde. De bruker imidlertid energi når skjermbildet endres.

I undermenyen "*Autolås*" kan du konfigurere og aktivere automatisk låsing av hovedboken etter en bestemt periode med inaktivitet.

![LEDGER FLEX](assets/notext/23.webp)

I menyen "*Lyder*" kan du slå lydene til Flex på eller av. Og i menyen "Language" kan du endre språket på skjermen.

![LEDGER FLEX](assets/notext/24.webp)

Ved å klikke på pilen til høyre får du tilgang til andre innstillinger. "*Endre PIN-kode*" gir deg mulighet til å endre PIN-koden din.

![LEDGER FLEX](assets/notext/25.webp)

I menyene "*Bluetooth*" og "*NFC*" kan du administrere denne kommunikasjonen.

![LEDGER FLEX](assets/notext/26.webp)

I "*Battery*" kan du blant annet stille inn en automatisk avslutning av hovedboken.

![LEDGER FLEX](assets/notext/27.webp)

I delen "*Avansert*" får du tilgang til mer sofistikerte sikkerhetsinnstillinger. Det anbefales å ha alternativet "*PIN shuffle*" aktivert for å forbedre sikkerheten. Det er også i denne menyen du kan konfigurere en BIP39-passordfrase.

![LEDGER FLEX](assets/notext/28.webp)

Passordfrasen er et valgfritt passord som, kombinert med gjenopprettingsfrasen, gir et ekstra sikkerhetslag for lommeboken din.

For øyeblikket genereres lommeboken din fra en mnemonisk frase som består av 24 ord. Denne gjenopprettingsfrasen er svært viktig, ettersom den lar deg gjenopprette alle nøklene i lommeboken din i tilfelle tap. Den utgjør imidlertid et enkelt feilpunkt (SPOF). Hvis den blir kompromittert, er bitcoinsene i fare. Det er her passordfrasen kommer inn i bildet. Det er et valgfritt passord, som du kan velge vilkårlig, som legges til den mnemoniske frasen for å styrke lommebokens sikkerhet.

Passordfrasen må ikke forveksles med PIN-koden. Den spiller en rolle i utledningen av de kryptografiske nøklene dine. Den fungerer sammen med den mnemoniske frasen, og modifiserer frøet som nøklene genereres ut fra. Selv om noen skulle få tak i 24-ordsfrasen din, kan de ikke få tilgang til pengene dine uten passordfrasen. Ved å bruke en passordfrase oppretter du i praksis en ny lommebok med egne nøkler. Hvis du endrer (selv bare litt) på passordfrasen, vil det generere en annen lommebok.

Passordfrasen er et veldig kraftig verktøy for å øke sikkerheten til bitcoinsene dine. Det er imidlertid svært viktig å forstå hvordan det fungerer før du implementerer det, for å unngå å miste tilgangen til lommeboken din. Jeg vil forklare hvordan du bruker passordfrasen i en annen dedikert veiledning.

![LEDGER FLEX](assets/notext/29.webp)

Til slutt, på den siste innstillingssiden, kan du tilbakestille hovedboken din. Du bør kun tilbakestille hovedboken hvis du er sikker på at den ikke inneholder noen nøkler som sikrer bitcoins, da du kan miste tilgangen til pengene dine permanent.

![LEDGER FLEX](assets/notext/30.webp)

## Hvordan installerer jeg Bitcoin-applikasjonen?

Start med å starte Ledger Live-programvaren på datamaskinen, og koble deretter til og lås opp Ledger Flex.

![LEDGER FLEX](assets/notext/31.webp)

I Ledger Live går du til menyen "*My Ledger*". Du vil bli bedt om å autorisere tilgang til Flex.

![LEDGER FLEX](assets/notext/32.webp)

Valider tilgangen i hovedboken ved å klikke på knappen "*Allow*".

![LEDGER FLEX](assets/notext/33.webp)

Hvis fastvaren til din Ledger Flex ikke er oppdatert, vil Ledger Live automatisk tilby deg å oppdatere den. Hvis det er aktuelt, klikker du på "*Oppdater fastvare*" og deretter på "*Installer oppdatering*" for å starte installasjonen.

![LEDGER FLEX](assets/notext/34.webp)

Klikk på "*Install*"-knappen på Ledger, og vent deretter under installasjonen.

![LEDGER FLEX](assets/notext/35.webp)

Fastvaren til din Ledger Flex er nå oppdatert.

![LEDGER FLEX](assets/notext/36.webp)

Hvis du ønsker det, kan du endre bakgrunnsbildet på låseskjermen til Ledger Flex. Dette gjør du ved å klikke på "*Legg til >*".

![LEDGER FLEX](assets/notext/37.webp)

Klikk på knappen "*Last opp fra datamaskinen*" og velg bakgrunnsbilde fra bildene dine.

![LEDGER FLEX](assets/notext/38.webp)

Du kan beskjære bildet ditt.

![LEDGER FLEX](assets/notext/39.webp)

Velg en kontrast blant de ulike alternativene, og klikk deretter på "*Bekreft kontrast*".

![LEDGER FLEX](assets/notext/40.webp)

Klikk på "*Last inn bilde*"-knappen på Flex.

![LEDGER FLEX](assets/notext/41.webp)

Hvis du er fornøyd med bildet, klikker du på "*Keep*" for å angi det som bakgrunnsbilde på låseskjermen.

![LEDGER FLEX](assets/notext/42.webp)

Til slutt vil vi legge til Bitcoin-applikasjonen. For å gjøre dette, på Ledger Live, klikker du på "*Install*" -knappen ved siden av "*Bitcoin (BTC)*".

![LEDGER FLEX](assets/notext/43.webp)

Programmet installeres på Flex-enheten din.

![LEDGER FLEX](assets/notext/44.webp)

Fra nå av trenger du ikke lenger Ledger Live-programvaren for å administrere lommeboken din regelmessig. Du kan gå tilbake til den av og til for å oppdatere fastvaren når nye versjoner er tilgjengelige. For alt annet vil vi bruke Sparrow Wallet, som er et mye mer omfattende verktøy for effektiv administrasjon av en Bitcoin-lommebok.

## Hvordan setter jeg opp en ny Bitcoin-lommebok med Sparrow?

Åpne Sparrow Wallet og hopp over introduksjonssidene for å komme til startskjermen. Kontroller at du er riktig koblet til en node ved å se på bryteren nederst til høyre på skjermen.

![LEDGER FLEX](assets/notext/45.webp)

Jeg anbefaler på det sterkeste å bruke din egen Bitcoin-node. I denne veiledningen bruker jeg en offentlig node (gul) fordi jeg er på testnettet, men for normal bruk er det bedre å velge en lokal Bitcoin Core (grønn) eller en Electrum-server som er koblet til en ekstern node (blå).

Klikk på "*File*"-menyen og deretter på "*New Wallet*".

![LEDGER FLEX](assets/notext/46.webp)

Velg et navn for denne lommeboken, og klikk deretter på "*Create Wallet*".

![LEDGER FLEX](assets/notext/47.webp)

I rullegardinmenyen "*Script Type*" velger du hvilken type skript som skal brukes til å sikre bitcoinsene dine. Jeg anbefaler at du velger "*Taproot*", eller hvis det ikke er tilgjengelig, "*Native SegWit*".

![LEDGER FLEX](assets/notext/48.webp)

Klikk på knappen "*Connected Hardware Wallet*".

![LEDGER FLEX](assets/notext/49.webp)

Koble Ledger Flex til datamaskinen, lås den opp med PIN-koden din, og åpne deretter "*Bitcoin*"-applikasjonen. I denne veiledningen bruker jeg applikasjonen "*Bitcoin Testnet*", men fremgangsmåten er den samme for hovednettet.

![LEDGER FLEX](assets/notext/50.webp)

På Sparrow klikker du på "*Scan*"-knappen.

![LEDGER FLEX](assets/notext/51.webp)

Klikk deretter på "*Importer nøkkellager*".

![LEDGER FLEX](assets/notext/52.webp)

Du kan nå se detaljene for lommeboken din, inkludert den utvidede offentlige nøkkelen til den første kontoen din. Klikk på "*Apply*"-knappen for å fullføre opprettelsen av lommeboken.

![LEDGER FLEX](assets/notext/53.webp)

Velg et sterkt passord for å sikre tilgangen til Sparrow Wallet. Dette passordet vil sikre tilgangen til lommebokdataene dine på Sparrow, noe som bidrar til å beskytte dine offentlige nøkler, adresser, etiketter og transaksjonshistorikk mot uautorisert tilgang.

Jeg anbefaler deg å lagre dette passordet i en passordbehandler, slik at du ikke glemmer det.

![LEDGER FLEX](assets/notext/54.webp)

Og der har du det, lommeboken din er nå opprettet!

![LEDGER FLEX](assets/notext/55.webp)

Før du mottar dine første bitcoins i lommeboken din, anbefaler jeg deg på det sterkeste å utføre en gjenopprettingstest. Noter ned en referanseinformasjon, for eksempel xpub, og tilbakestill deretter Ledger Flex mens lommeboken fortsatt er tom. Prøv deretter å gjenopprette lommeboken på Ledger ved hjelp av papirsikkerhetskopiene dine. Sjekk at xpuben som genereres etter gjenopprettingen, stemmer overens med den du først noterte. Hvis dette er tilfelle, kan du være sikker på at papirbackupene dine er pålitelige.

## Hvordan motta bitcoins med Ledger Flex?

Klikk på fanen "*Mottak*".

![LEDGER FLEX](assets/notext/56.webp)

Koble Ledger Flex til datamaskinen, lås den opp med PIN-koden din, og åpne deretter "*Bitcoin*"-applikasjonen.

![LEDGER FLEX](assets/notext/57.webp)

Før du bruker adressen fra Sparrow Wallet, må du verifisere den på Ledger Flex-skjermen. På denne måten kan du bekrefte at adressen som vises på Sparrow ikke er falsk, og at Ledger faktisk har den private nøkkelen som er nødvendig for å bruke bitcoins som er sikret med denne adressen senere.

For å utføre denne verifiseringen klikker du på knappen "*Vis adresse*".

![LEDGER FLEX](assets/notext/58.webp)

Kontroller at adressen som vises på Ledger Flex, stemmer overens med den som er angitt i Sparrow Wallet. Det anbefales også å utføre denne verifiseringen rett før du gir adressen din til avsenderen, for å være sikker på at den er gyldig.

![LEDGER FLEX](assets/notext/59.webp)

Du kan legge til en "*Label*" for å beskrive kilden til bitcoinsene som skal sikres med denne adressen. Dette er en god praksis som hjelper deg med å administrere UTXO-ene dine bedre.

![LEDGER FLEX](assets/notext/60.webp)

Hvis du vil ha mer informasjon om merking, anbefaler jeg deg også å ta en titt på denne andre veiledningen:

https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52
Du kan deretter bruke denne adressen til å motta bitcoins.

![LEDGER FLEX](assets/notext/61.webp)

## Hvordan sende bitcoins med Ledger Flex?

Nå som du har mottatt de første satsene i lommeboken din sikret med Flex, kan du også bruke dem! Koble Ledger til datamaskinen, lås den opp, start Sparrow Wallet, og gå deretter til "*Send*"-fanen for å opprette en ny transaksjon.

![LEDGER FLEX](assets/notext/62.webp)

Hvis du vil gjøre "*myntkontroll*", det vil si spesifikt velge hvilke UTXOer som skal brukes i transaksjonen, går du til "*UTXOer*"-fanen. Velg UTXO-ene du ønsker å bruke, og klikk deretter på "*Send Selected*". Du blir omdirigert til samme skjermbilde som i "*Send*"-fanen, men med UTXO-ene du allerede har valgt for transaksjonen.

![LEDGER FLEX](assets/notext/63.webp)

Skriv inn destinasjonsadressen. Du kan også legge inn flere adresser ved å klikke på knappen "*+ Legg til*".

![LEDGER FLEX](assets/notext/64.webp)

Noter en "*Label*" for å huske formålet med denne utgiften.

![LEDGER FLEX](assets/notext/65.webp)

Velg beløpet som skal sendes til denne adressen.

![LEDGER FLEX](assets/notext/66.webp)

Juster gebyrsatsen for transaksjonen din i henhold til gjeldende marked.

![LEDGER FLEX](assets/notext/67.webp)

Kontroller at alle innstillingene for transaksjonen er riktige, og klikk deretter på "*Opprett transaksjon*".

![LEDGER FLEX](assets/notext/68.webp)

Hvis du er fornøyd med alt, klikker du på "*Finalize Transaction for Signing*".

![LEDGER FLEX](assets/notext/69.webp)

Klikk på "*Signer*".

![LEDGER FLEX](assets/notext/70.webp)

Klikk på "*Signer*" ved siden av din Ledger Flex.

![LEDGER FLEX](assets/notext/71.webp)

Kontroller transaksjonsinnstillingene på Flex-skjermen, inkludert mottakerens mottaksadresse, det sendte beløpet og gebyrbeløpet.

![LEDGER FLEX](assets/notext/72.webp)

For å signere holder du fingeren på "*Hold for å signere*"-knappen.

![LEDGER FLEX](assets/notext/73.webp)

Transaksjonen din er nå signert. Klikk på "*Broadcast Transaction*" for å kringkaste den på Bitcoin-nettverket.

![LEDGER FLEX](assets/notext/74.webp)

Du finner den under fanen "*Transaksjoner*" i Sparrow Wallet.

![LEDGER FLEX](assets/notext/75.webp)

Gratulerer, du har nå lært deg den grunnleggende bruken av Ledger Flex med Sparrow Wallet! I en fremtidig veiledning vil vi se hvordan du bruker Ledger Flex med Liana for å utnytte Miniscript.

Hvis du fant denne opplæringen nyttig, vil jeg sette pris på en tommel opp nedenfor. Del gjerne denne artikkelen på dine sosiale nettverk. Tusen takk skal du ha!