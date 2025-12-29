---
name: 1ML
description: Lær hvordan du bruker 1ML-utforskeren til å forstå og analysere Bitcoins Lightning-nettverk.
---
![cover](assets/cover.webp)



## Innledning



Lightning Network er en rask og rimelig betalingsløsning som er bygget på toppen av Bitcoin, og som muliggjør umiddelbare og sikre transaksjoner. Det er viktig å observere dette nettverket for å forstå hvordan det fungerer, dets topologi og tilstanden til nodene som utgjør det. En Lightning explorer, som 1ML, brukes til å visualisere nettverkets offentlige data, inkludert aktive noder, åpne kanaler og tilgjengelig kapasitet, noe som gir en verdifull oversikt for brukere, utviklere og nodeoperatører.



## Få tilgang til 1ML og forstå startsiden



For å få tilgang til 1ML åpner du ganske enkelt nettleseren og skriver inn [https://1ml.com](https://1ml.com). Dette tar deg til hjemmesiden, som fungerer som Lightning Networks globale dashbord.



![capture](assets/fr/03.webp)



Denne siden viser flere viktige statistikker øverst på skjermen, blant annet :





- Det **totale antallet aktive noder** i nettverket, dvs. datamaskiner som er involvert i sending og mottak av Lyn-betalinger.
- Antall åpne kanaler**, som tilsvarer forbindelsene mellom disse nodene som muliggjør pengeoverføringer.
- Den **totale nettverkskapasiteten**, uttrykt i bitcoin (BTC), som angir summen av kapasiteten til alle offentlige kanaler.



Disse tallene oppdateres jevnlig for å gjenspeile nettverkets nåværende tilstand. De gir et inntrykk av nettverkets størrelse, vekst og robusthet.



![capture](assets/fr/04.webp)



Rett under siden finner du lister med rangeringer:





- De **mest tilkoblede nodene**, som har flest åpne kanaler til andre noder.
- Den **høyeste kapasiteten** på nodene, som angir hvilke noder som kan overføre de største mengdene.
- De viktigste kanalene når det gjelder kapasitet.



Filtrene kan også brukes til å avgrense listene etter geografisk plassering eller andre kriterier.



Denne siden er et ideelt utgangspunkt for å utforske Lightning Network og forstå dens generelle topologi.



![capture](assets/fr/05.webp)



![capture](assets/fr/06.webp)



## Utforske Lightning-noder



Hvis du vil utforske en node på 1ML, kan du begynne med å bruke søkefeltet øverst på siden. Du kan skrive inn **Node ID**, dvs. nodens unike identifikator, eller dens **alias**, som er et navn det er lettere å huske.



Når søket er fullført, klikker du på den aktuelle noden for å få tilgang til den detaljerte siden.



![capture](assets/fr/07.webp)



På denne siden vises flere viktige opplysninger:





- Node-ID**: Denne unike identifikatoren er en lang streng med tegn som gjør det mulig å identifisere noden nøyaktig i hele nettverket.



![capture](assets/fr/08.webp)





- Alias**: Dette er navnet som eieren av noden har valgt for å representere den offentlig.



![capture](assets/fr/09.webp)





- **antall kanaler** angir hvor mange forbindelser noden har med andre noder, mens **total kapasitet** representerer summen av tilgjengelige bitcoins i disse kanalene. En node med et stort antall kanaler og høy kapasitet har generelt gode forbindelser og er i stand til å overføre store pengebeløp raskt på tvers av nettverket.



![capture](assets/fr/10.webp)





- Oppetid**, eller tilgjengelighet, måler hvor lenge en node har vært aktiv og tilgjengelig på nettet, noe som gjenspeiler dens pålitelighet. Nodens **alder** angir derimot hvor lenge den har vært til stede i nettverket, noe som gjenspeiler dens stabilitet og erfaring i Lightning Network.



![capture](assets/fr/11.webp)



Disse dataene hjelper deg med å forstå hvor viktig og pålitelig en node er i Lightning Network. En node med et stort antall kanaler, høy kapasitet og høy oppetid er for eksempel ofte en viktig aktør i nettverket.



## Utforsking av lynkanaler



### Hva er en Lightning-kanal?



En Lightning-kanal er en direkte forbindelse mellom to nettverksnoder. Den gjør det mulig for disse to nodene å utveksle øyeblikkelige, rimelige betalinger uten å gå gjennom Bitcoin-hovedkjeden for hver transaksjon. Kanaler er fundamentet som gjør Lightning Network rask og skalerbar.



### Les kanalinformasjon på 1ML



På 1ML har hver kanal sin egen side eller beskrivelsesark som inneholder en rekke viktige data:



Fra siden til en node kan du få tilgang til en liste over kanalene. Ved å klikke på en kanal viser 1ML en egen side med flere viktige opplysninger.



![capture](assets/fr/12.webp)



![capture](assets/fr/13.webp)



De viktigste synlige dataene er som følger:





- Partnernoder**: Hver kanal kobler sammen to noder. 1ML viser begge identifikatorene og deres respektive alias.



![capture](assets/fr/14.webp)





- Kanalkapasitet**: Dette er den totale mengden bitcoins som er låst i denne kanalen. Denne kapasiteten representerer maksimumsgrensen for betalinger som kan transitteres gjennom denne kanalen.



![capture](assets/fr/15.webp)





- Kanalens alder**: angir hvor lenge kanalen har vært åpen. En gammel kanal er ofte et tegn på et stabilt forhold mellom to noder.



![capture](assets/fr/16.webp)



### Grenser for sikt i kanalen



Det er viktig å forstå at 1ML bare viser **en del** av Lightning Network. Utforskeren viser bare **offentlige kanaler**, dvs. de som har blitt annonsert i nettverket. Private kanaler, som ofte brukes av konfidensialitets- eller strategiske årsaker, er ikke synlige. 1ML viser heller ikke den nøyaktige fordelingen av midler på hver side av en kanal, og heller ikke de utførte betalingene eller den likviditeten som faktisk er tilgjengelig på et gitt tidspunkt. Informasjonen som vises, kan derfor brukes til å analysere den **generelle strukturen i nettverket**, men ikke den faktiske finansielle aktiviteten eller den detaljerte likviditetsstatusen.



## Utforsk Lightning Network etter plassering



### Noder etter land og region



1ML lar deg utforske Lightning Network i henhold til en **geografisk inndeling**. Fra startsiden eller via dedikerte seksjoner er det mulig å vise noder etter land eller region. Denne funksjonen er basert på stedsinformasjon som er oppgitt av nodeoperatørene.


I navigasjonsfeltet ser du lenken **Location**. På siden er nodene gruppert etter verdensdel, land og by.



![capture](assets/fr/17.webp)



Når du velger et land, viser 1ML en liste over tilknyttede noder, sammen med aggregert statistikk som antall noder og total synlig kapasitet for det geografiske området.



#### Hva dette sier om lokal adopsjon





- Innføring av teknologi**: Et stort antall noder i en region indikerer at Bitcoin-brukere, selskaper eller tjenester aktivt tar i bruk Lightning Network. Dette viser teknologisk modenhet og en vilje til å dra nytte av fordelene med Lightning (raske transaksjoner, lavere kostnader).
- Økonomisk økosystem** : Den tette tilstedeværelsen av noder kan også signalisere en lokal økonomisk struktur rundt Bitcoin: selgere som tar imot Lightning, nystartede bedrifter som utvikler verktøy, arrangementer i lokalsamfunnet osv.
- Sikkerhet og robusthet**: En variert geografisk distribusjon gjør nettverket mer robust i møte med lokale strømbrudd eller restriksjoner. Jo mer spredt nodene er, desto mer desentralisert og vanskeligere er det å sensurere nettverket.
- Politikk og regelverk**: Noen land kan oppleve raskere adopsjon takket være et gunstig regelverk eller et proaktivt samfunn. I områder der regelverket er strengt eller fiendtlig innstilt, vil antallet noder derimot være lavere.



#### Begrensninger i geografiske data



Husk imidlertid at geolokaliseringen av Lightning-noder har sine begrensninger og skjevheter:





- Omtrentlig IP-posisjon**: 1ML bruker vanligvis den offentlige IP-adressen til noder for å anslå hvor de befinner seg. Denne metoden kan imidlertid forvrenges av bruk av VPN-er, skyservere (AWS, Google Cloud) eller hosting i andre land enn nodeeierens faktiske bosted.
- Virtuelle noder**: Noen operatører hoster nodene sine på eksterne servere av hensyn til pålitelighet og tilgjengelighet, noe som kan gi en falsk følelse av fysisk plassering.
- Brukermobilitet**: En nodeoperatør kan skifte lokasjon, flytte infrastrukturen sin eller åpne flere noder i ulike regioner, noe som gjør dataavlesningen mer kompleks.
- Usynliggjøring av private noder**: Noen noder publiserer ikke IP-adressen sin eller bruker metoder for å skjule posisjonen sin, noe som gjør geolokalisering umulig.



## 1ML konkrete brukstilfeller



### Forstå nettverkstopologi



1ML lar deg visualisere den **generelle strukturen til Lightning Network**. Ved å observere forbindelsene mellom noder, antall kanaler og samlet kapasitet er det mulig å forstå hvordan nettverket er organisert, hvilke noder som spiller en sentral rolle og hvordan betalingsstrømmer teoretisk sett kan sirkulere.



Denne forståelsen er avgjørende for å kunne forstå hvordan Lightning Network fungerer, og ikke bare for porteføljebruk.



### Identifiser viktige noder



Takket være rangeringene som 1ML tilbyr (flest tilkoblede noder, høyest kapasitet, alder), er det mulig å identifisere noder som har en viktig plass i nettverket. Disse nodene fungerer ofte som viktige gatewayer for Lightning-betalinger.



![capture](assets/fr/18.webp)



### Sjekk den offentlige synligheten til en node



Som nodeoperatør kan du med 1ML sjekke om noden din er **offentlig annonsert** på Lightning Network. Hvis en node vises på 1ML, betyr det at den er synlig og tilgjengelig for andre noder som ønsker å åpne offentlige kanaler.


Dette kan være nyttig for å diagnostisere problemer med synlighet eller tilkobling.



### Se Lightning Network utvikle seg over tid



Ved å sammenligne global statistikk over ulike perioder gjør 1ML det mulig for oss å observere utviklingen av Lightning Network: økning eller reduksjon i antall noder, variasjoner i total kapasitet eller endringer i geografisk fordeling.


Disse observasjonene gir et interessant perspektiv på vekst, modenhet og trender i Lightning Network.



## 1ML beste praksis og begrensninger



### Offentlige data ≠ fullstendig virkelighet



1ML er utelukkende basert på de **offentliggjorte** dataene om Lightning Network. Dette betyr at verktøyet bare viser en del av virkeligheten. Mange kanaler kan være private, noen noder er kanskje ikke annonsert, og den faktiske likviditeten som er tilgjengelig i kanalene, er ikke synlig. Det er derfor viktig å bruke 1ML som et globalt analyseverktøy, ikke som en uttømmende representasjon av nettverket.



### Personvern og lynnedslag



Lightning Network er designet med et sterkt fokus på **personvern ved betaling**. Individuelle transaksjoner er ikke synlige på 1ML, og eksakte kanalsaldoer er ikke offentlige. Denne begrensningen er ikke en feil hos utforskeren, men en grunnleggende funksjon i Lightning Network, designet for å beskytte brukernes personvern.



### Ikke trekk forhastede konklusjoner



En node med høy kapasitet eller mange kanaler er ikke nødvendigvis mer "pålitelig" eller "effektiv" i alle tilfeller. På samme måte betyr ikke et midlertidig fall i den samlede nettkapasiteten nødvendigvis at det er et strukturelt problem. Tall bør alltid tolkes i ettertid og settes inn i en sammenheng.



### Komplementaritet med andre verktøy



1ML er et utmerket utgangspunkt for å utforske Lightning Network, men det er best å bruke det sammen med andre verktøy, for eksempel Lightning-porteføljer, grensesnitt for nodeadministrasjon og andre utforskere. Denne tilnærmingen gir et mer komplett og nyansert bilde av nettverket.



## mulighet for 1ML-tilkobling (avansert funksjonalitet)



1ML tilbyr et alternativ for **innlogging/opprett konto**, som er synlig på nettstedet, men dette er **ikke nødvendig** for å se Lightning Network-data. Alle funksjonene som er omtalt så langt i denne veiledningen, er tilgjengelige **uten konto**.



Tilkoblingen er primært rettet mot **Lightning node-operatører**. Den gjør det mulig å knytte en node til en 1ML-konto for å administrere visse offentlige opplysninger, for eksempel nodens presentasjon, kontaktlenker og andre metadata. Denne funksjonen er utformet for å forbedre synligheten og identifikasjonen av en node i utforskeren.



Det er viktig å merke seg at 1ML **ikke er en depottjeneste**. Opprettelsen av en konto gir ikke tilgang til midler, kanaler eller betalinger for en node. Den tjener kun til å samhandle med utforskeren fra et deklarativt og informativt synspunkt.



I forbindelse med læring eller oppdagelse av Lightning Network kan dette alternativet derfor betraktes som **valgfritt** og forbeholdt mer avansert bruk.



## Konklusjon



1ML er et verdifullt verktøy for å observere og forstå Lightning Network fra de offentlige dataene. Det lar deg utforske strukturen i nettverket, analysere noder og kanaler og spore den generelle utviklingen av Lightning Network-adopsjon over tid. Uten behov for en konto eller håndtering av midler, tilbyr 1ML en tilgjengelig inngangsport for alle som ønsker å få en dypere forståelse av hvordan Lightning fungerer.


Hvis du vil gå videre med Lightning Network, anbefaler jeg det komplette kurset Introduksjon til Lightning Network:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb