---
name: COLDCARD Q
description: Sette opp og bruke et COLDCARD Q
---
![cover](assets/cover.webp)

En maskinvarelommebok er en elektronisk enhet som er dedikert til å administrere og sikre de private nøklene til en Bitcoin-lommebok. I motsetning til programvarelommebøker (eller hot wallets) som er installert på vanlige maskiner som ofte er koblet til Internett, gjør maskinvarelommebøker det mulig å isolere private nøkler fysisk, noe som reduserer risikoen for piratkopiering og tyveri.

Hovedmålet med en maskinvarelommebok er å redusere enhetens funksjonalitet så mye som mulig for å minimere angrepsflaten. Mindre angrepsflate betyr også færre potensielle angrepsvektorer, dvs. færre svake punkter i systemet som angripere kan utnytte for å få tilgang til bitcoins.

Det anbefales å bruke en maskinvarelommebok for å sikre bitcoinsene dine, spesielt hvis du har store mengder, enten i absolutt verdi eller som en andel av de totale eiendelene dine.

Maskinvare-lommebøker brukes sammen med programvare for lommebokadministrasjon på en datamaskin eller smarttelefon. Sistnevnte programvare administrerer opprettelsen av transaksjoner, men den kryptografiske signaturen som kreves for å gjøre transaksjonene gyldige, utføres utelukkende i maskinvarelommeboken. Dette betyr at private nøkler aldri blir eksponert for et potensielt sårbart miljø.

Maskinvare-lommebøker tilbyr dobbel beskyttelse for brukeren: På den ene siden sikrer de bitcoinsene dine mot eksterne angrep ved å holde de private nøklene offline, og på den andre siden tilbyr de generelt større fysisk motstand mot forsøk på å trekke ut nøklene. Og det er nettopp på disse to sikkerhetskriteriene at vi kan bedømme og klassifisere de forskjellige modellene på markedet.

I denne veiledningen vil jeg introdusere deg for en slik løsning: **COLDCARD Q**.

---
COLDCARD Q har mange funksjoner, og jeg foreslår derfor å dele bruken av COLDCARD Q inn i to veiledninger. I denne første veiledningen tar vi for oss den første konfigurasjonen og de grunnleggende funksjonene til enheten. Deretter, i den andre veiledningen, ser vi på hvordan du kan dra nytte av alle COLDCARDs avanserte alternativer.

https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0
---
## Vi introduserer COLDCARD Q

COLDCARD Q er en maskinvarelommebok som kun inneholder Bitcoin, utviklet av det kanadiske selskapet Coinkite, kjent for sine tidligere MK-modeller. Q representerer deres mest avanserte produkt til dags dato, og er posisjonert som den ultimate Bitcoin-maskinvare-lommeboken.

Når det gjelder maskinvare, er COLDCARD Q utstyrt med alle de funksjonene som kreves for en optimal brukeropplevelse:


- Et stort LCD-display forenkler navigering og betjening;
- Et komplett QWERTY-tastatur;
- Integrert kamera for skanning av QR-koder;
- To spor for microSD-kort ;
- Et helt isolert strømalternativ via tre AAA-batterier (ikke inkludert), eller via en USB-C-kabel ;
- To Secure Elements fra to forskjellige produsenter for ekstra sikkerhet;
- Muligheten til å kommunisere via NFC.

Etter min mening har COLDCARD Q bare to ulemper. For det første er den ganske klumpete på grunn av de mange funksjonene, og den er nesten 13 cm lang og 8 cm bred, noe som nesten er på størrelse med en liten smarttelefon. Den er også ganske tykk på grunn av batterirommet. Hvis du er ute etter en mindre, mer mobil maskinvarelommebok, kan den mye mer kompakte MK4 være et bedre alternativ. Den andre ulempen er åpenbart kostnaden for enheten, som er priset til ** $ 239,99 ** på det offisielle nettstedet, dvs. $ 72 mer enn MK4, noe som setter Q i direkte konkurranse med premium maskinvarelommebøker som Ledger Flex eller Foundation's Passport.

![CCQ](assets/fr/001.webp)

På programvaresiden er COLDCARD Q like godt utstyrt som Coinkites andre enheter, med en rekke avanserte funksjoner:


- Terningkast for å generere din egen gjenopprettingsfrase ;
- PIN-kode ;
- Nedtelling til endelig PIN-lås ;
- BIP39 passordfrase ;
- Endelig PIN-kode for låsing ;
- Nedtelling av tilkobling ;
- SeedXOR;
- BIP85...

COLDCARD Q gir kort sagt en bedre brukeropplevelse enn MK4, og kan være ideelt for middels til avanserte brukere som ønsker større brukervennlighet.

COLDCARD Q er tilgjengelig for salg [på Coinkites offisielle nettsted] (https://store.coinkite.com/store/coldcard). Det kan også kjøpes hos en forhandler.

## Forbereder opplæringen

Når du har mottatt COLDCARD, er det første trinnet å inspisere emballasjen for å forsikre deg om at den ikke har blitt åpnet. Hvis emballasjen er skadet, kan det tyde på at maskinvarelommeboken har blitt kompromittert og kanskje ikke er ekte.

![CCQ](assets/fr/002.webp)

Når du åpner esken, bør du finne følgende elementer:


- COLDCARD Q i en forseglet pose;
- Et kort til å skrive ned minnefrasen din.

![CCQ](assets/fr/003.webp)

Forsikre deg om at posen ikke har blitt åpnet eller skadet. Sjekk også at nummeret på posen stemmer overens med nummeret på papiret inni posen. Ta vare på dette nummeret for fremtidig referanse.

![CCQ](assets/fr/004.webp)

Hvis du foretrekker å drive COLDCARD uten å koble det til en datamaskin (air-gap), setter du inn tre AAA-batterier på baksiden av enheten. Alternativt kan du koble den til datamaskinen via en USB-C-kabel.

![CCQ](assets/fr/005.webp)

For denne opplæringen trenger du også Sparrow Wallet for å administrere Bitcoin-lommeboken din på datamaskinen din. Last ned [Sparrow Wallet] (https://sparrowwallet.com/download/) fra den offisielle nettsiden. Jeg anbefaler på det sterkeste at du sjekker både autentisiteten (med GnuPG) og integriteten (via hash) før du fortsetter med installasjonen. Hvis du ikke vet hvordan du gjør dette, kan du følge denne veiledningen:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
## Valg av PIN-kode

Du kan nå slå på COLDCARD ved å trykke på knappen øverst i venstre hjørne.

![CCQ](assets/fr/006.webp)

Trykk på "*ENTER*"-knappen for å godta vilkårene for bruk.

![CCQ](assets/fr/007.webp)

COLDCARD Q vil da vise et nummer øverst på skjermen. Sørg for at dette nummeret stemmer overens med nummeret på den forseglede posen og på plastbiten inne i posen. Dette sikrer at pakken ikke har blitt åpnet mellom det tidspunktet den ble pakket av Coinkite og det tidspunktet du åpnet den. Trykk på "*ENTER*" for å fortsette.

![CCQ](assets/fr/008.webp)

Gå til menyen "*Velg PIN-kode*", og bekreft med "*ENTER*"-knappen.

![CCQ](assets/fr/009.webp)

Denne PIN-koden brukes til å låse opp COLDCARD. Den er derfor en beskyttelse mot uautorisert fysisk tilgang. Denne PIN-koden er ikke involvert i utledningen av lommebokens kryptografiske nøkler. Så selv uten tilgang til denne PIN-koden vil du kunne få tilgang til bitcoinsene dine igjen hvis du er i besittelse av minnefrasen din.

COLDCARD PIN-koder er delt inn i to deler: et prefiks og et suffiks, som hver kan inneholde mellom 2 og 6 sifre, til sammen 4 til 12 sifre. Når du låser opp COLDCARD, må du først taste inn prefikset, og deretter vil enheten vise deg to ord. Deretter skriver du inn suffikset. Disse to ordene får du oppgitt under dette konfigurasjonstrinnet, og du bør lagre dem nøye, da du trenger dem hver gang du låser opp COLDCARD. Hvis de to ordene som vises under opplåsingen, stemmer overens med de du lagret under konfigurasjonen, bekrefter dette at enheten ikke har blitt kompromittert siden forrige gang den ble brukt.

Klikk igjen på "*Velg PIN-kode*"

![CCQ](assets/fr/010.webp)

Bekreft at du har lest advarslene.

![CCQ](assets/fr/011.webp)

Du skal nå velge PIN-koden din. Vi anbefaler en lang, tilfeldig PIN-kode. Sørg for at du oppbevarer denne koden på et annet sted enn der COLDCARD er lagret. Du kan bruke kortet som følger med i pakken til å registrere denne koden.

Skriv inn ønsket prefiks, og trykk deretter på "*ENTER*"-knappen for å bekrefte den første delen av PIN-koden.

![CCQ](assets/fr/012.webp)

De to anti-phishing-ordene vil deretter vises på skjermen. Ta godt vare på dem for fremtidig referanse. Du kan bruke kortet som følger med i pakken til å skrive dem ned.

![CCQ](assets/fr/013.webp)

Skriv deretter inn den andre delen av PIN-koden, og trykk på "*ENTER*".

![CCQ](assets/fr/014.webp)

Bekreft PIN-koden ved å taste den inn en gang til, og kontroller at de to anti-phishing-ordene stemmer overens med de du lagret tidligere.

![CCQ](assets/fr/015.webp)

Hver gang du låser opp COLDCARD fra nå av, må du huske å sjekke gyldigheten av de to anti-phishing-ordene som vises på skjermen etter at du har tastet inn PIN-koden din.

## Oppdatering av fastvare

Når du bruker enheten for første gang, er det viktig å sjekke og oppdatere fastvaren. Dette gjør du ved å gå til menyen "*Avansert/Verktøy*".

![CCQ](assets/fr/016.webp)

**Viktig:** Hvis du planlegger å oppgradere fastvaren og dette ikke er første gang du bruker COLDCARD (dvs. at du allerede har opprettet en lommebok på COLDCARD), må du sørge for at du har minnefrasen din og at den fungerer (i tillegg til den valgfrie passordfrasen, hvis aktuelt). Dette er viktig for å unngå å miste bitcoins hvis det skulle oppstå et problem under enhetsoppdateringen.

Velg "*Oppgrader fastvare*".

![CCQ](assets/fr/017.webp)

Velg "*Vis versjon*".

![CCQ](assets/fr/018.webp)

Du kan sjekke den gjeldende fastvareversjonen av COLDCARD. I mitt tilfelle er versjonen for eksempel "*1.2.3Q*".

![CCQ](assets/fr/019.webp)

Sjekk [på det offisielle COLDCARD-nettstedet] (https://coldcard.com/downloads) for å se om en nyere versjon er tilgjengelig. Klikk på "*Download*" for å laste ned den nye fastvaren.

![CCQ](assets/fr/020.webp)

På dette tidspunktet anbefaler vi på det sterkeste at du kontrollerer integriteten og ektheten til den nedlastede fastvaren. Dette gjør du ved å laste ned [dokumentet som inneholder hash-verdier for alle versjoner, signert av utviklerne] (https://raw.githubusercontent.com/Coldcard/firmware/master/releases/signatures.txt), verifisere signaturen med [utviklerens offentlige nøkkel] (https://keybase.io/dochex), og kontrollere at hash-verdien som er angitt i det signerte dokumentet, stemmer overens med fastvaren som er lastet ned fra nettstedet. Hvis alt stemmer, kan du fortsette med oppdateringen.

Hvis du ikke er kjent med denne verifiseringsprosessen, anbefaler jeg at du følger denne veiledningen:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Ta et microSD-kort og overfør fastvarefilen (dokument i `.dfu`) til det. Sett microSD-kortet inn i en av portene på COLDCARD.

![CCQ](assets/fr/021.webp)

Deretter velger du "*Fra MicroSD*" i fastvareoppdateringsmenyen.

![CCQ](assets/fr/022.webp)

Velg filen som tilsvarer fastvaren.

![CCQ](assets/fr/023.webp)

Bekreft valget ved å trykke på "*ENTER*"-knappen.

![CCQ](assets/fr/024.webp)

Vennligst vent mens fastvaren oppdateres.

![CCQ](assets/fr/025.webp)

Når oppdateringen er fullført, skriver du inn PIN-koden for å låse opp enheten.

![CCQ](assets/fr/026.webp)

Fastvaren din er nå oppdatert.

## COLDCARD Q-parametere

Hvis du ønsker det, kan du utforske COLDCARD-innstillingene ved å gå til menyen "*Settings*".

![CCQ](assets/fr/027.webp)

I denne menyen finner du ulike tilpasningsalternativer, for eksempel innstilling av lysstyrken på skjermen eller valg av standard måleenhet.

![CCQ](assets/fr/028.webp)

Vi skal se på andre avanserte innstillinger i neste veiledning:

https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0
## Opprette en Bitcoin-lommebok

Nå er det på tide å generere en ny Bitcoin-lommebok! For å gjøre dette må du opprette en mnemonisk frase. På Coldcard har du tre metoder for å generere denne frasen:


- Bruk kun den interne tilfeldige tallgeneratoren (TRNG);
- Bruk en kombinasjon av TRNG og terningkasting for å legge til entropi;
- Bruk kun terningkast.

**For nybegynnere og viderekomne brukere anbefaler vi at du kun bruker COLDCARDs interne generator for tilfeldige tall**

Jeg anbefaler ikke alternativet med bare terninger, ettersom dårlig utførelse kan føre til en setning med utilstrekkelig entropi, noe som kan sette sikkerheten til lommeboken din i fare.

Det beste alternativet er likevel det andre, som kombinerer bruken av TRNG med en ekstern entropikilde. Denne metoden garanterer en minimumsentropi som tilsvarer den som oppnås med TRNG alene, og gir et ekstra sikkerhetsnivå i tilfelle den interne generatoren skulle svikte (frivillig eller ikke). Ved å velge dette alternativet, som kombinerer TRNG og terningkasting, får du større kontroll over genereringen av setningen, uten å øke risikoen i tilfelle dårlig utførelse fra din side.

Klikk på "*Nye frøord*".

![CCQ](assets/fr/029.webp)

Du kan selv velge lengden på setningen. Jeg anbefaler at du velger en setning på 12 ord, ettersom den er mindre kompleks å administrere og ikke gir mindre porteføljesikkerhet enn en setning på 24 ord.

![CCQ](assets/fr/030.webp)

COLDCARD vil da vise den TRNG-genererte gjenopprettingsfrasen. Hvis du ønsker å legge til ytterligere ekstern entropi, trykker du på "*4*"-tasten.

![CCQ](assets/fr/031.webp)

Da kommer du til en side der du kan legge til entropi ved å kaste terningen. Kast så mange terningkast som mulig (minst 50 anbefales, men mindre er ikke så farlig ettersom du allerede drar nytte av entropien til TRNG), og registrer resultatene med tastene "*1*" til "*6*". Når du er ferdig, trykker du på "*ENTER*" for å bekrefte.

![CCQ](assets/fr/032.webp)

En ny mnemoteknisk frase vises, basert på entropien du nettopp har oppgitt, og TRNG-ens entropi.

**Advarsel: Denne huskeregelen gir full, ubegrenset tilgang til alle bitcoinsene dine**. Alle som er i besittelse av denne frasen kan stjele pengene dine, selv uten fysisk tilgang til COLDCARD. Frasen på 12 ord gjenoppretter tilgangen til bitcoinsene dine i tilfelle tap, tyveri eller ødeleggelse av COLDCARD. Det er derfor svært viktig å lagre det nøye og oppbevare det på et sikkert sted.

Du kan skrive det ned på kartongen som følger med COLDCARD, eller for ekstra sikkerhet anbefaler jeg at du graverer det inn på et underlag av rustfritt stål for å beskytte det mot brann, oversvømmelse eller kollaps. Du må uansett aldri lagre det på et digitalt medium, ellers kan du miste bitcoinsene dine.

Skriv ned ordene som vises på skjermen, på det fysiske mediet du ønsker. Avhengig av sikkerhetsstrategien din kan du vurdere å lage flere fullstendige fysiske kopier av setningen (men ikke del den opp). Det er viktig at ordene er nummererte og står i rekkefølge.

Du må selvsagt aldri dele disse ordene** på Internett, i motsetning til i denne veiledningen. Denne eksempelmappen vil kun bli brukt på Testnet, og vil bli slettet ved slutten av opplæringen.

Når du har skrevet ned ordene, trykker du på "*ENTER*".

![CCQ](assets/fr/033.webp)

For å forsikre deg om at du har lagret frasen riktig, vil systemet be deg om å bekrefte visse ord. Velg tallet som tilsvarer hvert ord på tastaturet.

![CCQ](assets/fr/034.webp)

Lommeboken din er nå opprettet! Øverst til høyre på skjermen kan du se fingeravtrykket til den private hovednøkkelen din. Trykk på "*ENTER*".

![CCQ](assets/fr/035.webp)

Du har nå tilgang til COLDCARDs hovedmeny.

![CCQ](assets/fr/036.webp)

## Opprette en ny portefølje på Sparrow

Det finnes flere alternativer for å opprette kommunikasjon mellom Sparrow Wallet-programvaren og COLDCARD. Det enkleste er å bruke en USB-C-kabel. Som standard er imidlertid kabel- og NFC-kommunikasjon deaktivert på COLDCARD. For å aktivere dem igjen, naviger til "*Innstillinger*", deretter "*Hardvare på/av*", og aktiver ønsket kommunikasjonsalternativ.

![CCQ](assets/fr/037.webp)

Hvis du foretrekker å holde COLDCARD helt isolert fra datamaskinen, kan du velge indirekte "air-gap"-kommunikasjon ved hjelp av QR-koder eller et microSD-kort. Det er denne metoden vi bruker i denne veiledningen.

Gå til "*Avansert/Verktøy*".

![CCQ](assets/fr/038.webp)

Velg "*Eksporter lommebok*".

![CCQ](assets/fr/039.webp)

Velg deretter "*Sparrow Wallet*".

![CCQ](assets/fr/040.webp)

Trykk på "*ENTER*" for å generere konfigurasjonsfilen.

![CCQ](assets/fr/041.webp)

Velg deretter hvordan du vil sende filen til Sparrow. I dette eksemplet har jeg satt inn et microSD-kort i spor "*A*", så jeg velger knappen "*1*". Du kan også vise informasjonen som en QR-kode på COLDCARD-skjermen ved å trykke på "*QR*"-knappen og skanne QR-koden med webkameraet på datamaskinen.

![CCQ](assets/fr/042.webp)

Start Sparrow Wallet og hopp over introduksjonssidene for å komme til hovedskjermen. Kontroller at du er riktig koblet til en node ved å sjekke bryteren nederst til høyre på skjermen.

![CCQ](assets/fr/043.webp)

Det anbefales på det sterkeste at du bruker din egen Bitcoin-node. I denne veiledningen bruker jeg en offentlig node (gul), siden jeg er på testnettet, men for produksjonsbruk er det best å bruke Bitcoin Core lokalt (grønn) eller en Electrum-server på en ekstern node (blå).

Gå til "*File*"-menyen og velg "*New Wallet*".

![CCQ](assets/fr/044.webp)

Gi lommeboken din et navn og klikk på "*Create Wallet*".

![CCQ](assets/fr/045.webp)

I rullegardinmenyen "*Script Type*" velger du hvilken type skript som skal sikre bitcoinsene dine.

![CCQ](assets/fr/046.webp)

Klikk på "*Airgapped Hardware Wallet*".

![CCQ](assets/fr/047.webp)

Under fanen "*Coldcard*" klikker du på "*Scan...*" hvis du planlegger å skanne QR-koden som vises på COLDCARD, eller på "*Import File...*" for å importere filen fra microSD-kortet (dette er `.json`-filen).

![CCQ](assets/fr/048.webp)

Etter importen må du kontrollere at "*Master fingerprint*" som vises på Sparrow, stemmer overens med det som vises på COLDCARD. Bekreft opprettelsen ved å klikke på "*Apply*".

![CCQ](assets/fr/049.webp)

Sett opp et sterkt passord for å sikre tilgangen til Sparrow Wallet. Dette passordet vil beskytte dine offentlige nøkler, adresser, tagger og transaksjonshistorikk mot uautorisert tilgang.

Det er lurt å lagre dette passordet slik at du ikke glemmer det (f.eks. i en passordbehandler).

![CCQ](assets/fr/050.webp)

Lommeboken din er nå satt opp på Sparrow Wallet.

![CCQ](assets/fr/051.webp)

Før du mottar dine første bitcoins i lommeboken din, ** anbefaler jeg deg på det sterkeste å utføre en tom gjenopprettingstest**. Skriv ned noe referanseinformasjon, for eksempel xpub, og tilbakestill deretter COLDCARD Q mens lommeboken fortsatt er tom. Prøv deretter å gjenopprette lommeboken til COLDCARD ved hjelp av papirsikkerhetskopiene dine. Kontroller at xpuben som genereres etter gjenopprettingen, stemmer overens med den du opprinnelig skrev ned. Hvis den gjør det, kan du være sikker på at papirsikkerhetskopiene dine er pålitelige.

Hvis du vil lære mer om hvordan du utfører en gjenopprettingstest, anbefaler jeg at du leser denne andre veiledningen:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895
## Motta bitcoins

For å motta dine første bitcoins, begynner du med å slå på og låse opp COLDCARD.

![CCQ](assets/fr/052.webp)

I Sparrow Wallet klikker du på fanen "*Mottak*".

![CCQ](assets/fr/053.webp)

Før du bruker adressen som foreslås av Sparrow Wallet, bør du sjekke den på COLDCARD-skjermen. På denne måten kan du bekrefte at adressen som vises på Sparrow ikke er falsk, og at maskinvarelommeboken faktisk har den private nøkkelen som trengs for å bruke bitcoins som er sikret med denne adressen. Dette hjelper deg med å unngå flere typer angrep.

For å utføre denne kontrollen klikker du på menyen "*Address Explorer*" på COLDCARD.

![CCQ](assets/fr/054.webp)

Velg typen skript du bruker på Sparrow. I mitt tilfelle er det Segwit P2WPKH. Jeg klikker på det.

![CCQ](assets/fr/055.webp)

Deretter kan du se de ulike avledede adressene i rekkefølge.

![CCQ](assets/fr/056.webp)

Sjekk med Sparrow at adressen stemmer overens. I mitt tilfelle er adressen med avledningsstien `m/84'/1'/0'/0/0` faktisk `tb1qwfwwvzssep4wyjg3vsgezmwa037ehvd4fhmjvr` på både Sparrow og COLDCARD.

![CCQ](assets/fr/057.webp)

En annen måte å verifisere eierskapet til denne adressen på, er å skanne QR-koden direkte inn i Sparrow fra COLDCARD. Fra COLDCARD-startskjermen velger du "*Scan Any QR Code*". Du kan også bruke "*QR*"-tasten på tastaturet.

![CCQ](assets/fr/058.webp)

Skann QR-koden til adressen som vises på Sparrow Wallet.

![CCQ](assets/fr/059.webp)

Kontroller at adressen som vises på COLDCARD, stemmer overens med den som vises på Sparrow. Trykk deretter på "*1*"-knappen.

![CCQ](assets/fr/060.webp)

Adressen er dermed bekreftet.

![CCQ](assets/fr/061.webp)

Du kan nå legge til en "*Label*" for å beskrive kilden til bitcoins som skal sikres med denne adressen. Dette er en god praksis som gjør at du bedre kan administrere UTXO-ene dine.

![CCQ](assets/fr/062.webp)

Hvis du vil ha mer informasjon om merking, anbefaler jeg også denne andre veiledningen:

https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52
Du kan deretter bruke denne adressen til å motta bitcoins.

![CCQ](assets/fr/063.webp)

## Send bitcoins

Nå som du har mottatt dine første sats i din COLDCARD-sikrede lommebok, kan du også bruke dem!

Som alltid starter du med å slå på og låse opp COLDCARD Q, deretter åpner du Sparrow Wallet og navigerer til "*Send*"-fanen for å forberede en ny transaksjon.

![CCQ](assets/fr/064.webp)

Hvis du ønsker å "myntkontrollere", dvs. velge spesifikt hvilke UTXO-er som skal brukes i transaksjonen, går du til fanen "*UTXO-er*". Velg de UTXO-ene du ønsker å bruke, og klikk deretter på "*Send Selected*". Du blir omdirigert til det samme skjermbildet i "*Send*"-fanen, men med UTXO-ene du allerede har valgt for transaksjonen.

![CCQ](assets/fr/065.webp)

Skriv inn destinasjonsadressen. Du kan også legge inn flere adresser ved å klikke på "*+ Legg til*"-knappen.

![CCQ](assets/fr/066.webp)

Skriv ned en "*Label*" for å huske formålet med denne utgiften.

![CCQ](assets/fr/067.webp)

Velg beløpet som skal sendes til denne adressen.

![CCQ](assets/fr/068.webp)

Juster gebyrsatsen for transaksjonen din i henhold til gjeldende marked.

![CCQ](assets/fr/069.webp)

Kontroller at alle transaksjonsparametrene er riktige, og klikk deretter på "*Opprett transaksjon*".

![CCQ](assets/fr/070.webp)

Hvis du er fornøyd med alt, klikker du på "*Finalize Transaction for Signing*".

![CCQ](assets/fr/071.webp)

Når du har opprettet transaksjonen i Sparrow, er det på tide å signere den med COLDCARD. Du har flere alternativer for å overføre PSBT (usignert transaksjon) til enheten din. Hvis kablet dataoverføring er aktivert, kan du sende transaksjonen direkte via en USB-C-tilkobling, akkurat som du ville gjort med en hvilken som helst annen maskinvarelommebok. I dette tilfellet, på Sparrow, må du klikke på "*Sign*"-knappen nederst i høyre hjørne. I mitt eksempel er denne knappen blokkert fordi COLDCARD ikke er koblet til med kabel.

![CCQ](assets/fr/072.webp)

Hvis du foretrekker å opprettholde en "luftspalte"-forbindelse uten direkte kontakt mellom maskinvarelommeboken og datamaskinen, har du to alternativer. Det første, og mer komplekse, er å bruke et microSD-kort. Sett inn microSD-kortet i datamaskinen, registrer transaksjonen via "*Save Transaction*"-knappen på Sparrow, og overfør deretter dette kortet til en port på COLDCARD.

![CCQ](assets/fr/073.webp)

Gå deretter til menyen "*Klar til å signere*".

![CCQ](assets/fr/074.webp)

Se gjennom transaksjonsdetaljene på COLDCARD, inkludert mottakeradressen, det sendte beløpet og transaksjonsgebyret.

![CCQ](assets/fr/075.webp)

Hvis alt er korrekt, trykker du på "*ENTER*"-knappen for å signere transaksjonen.

![CCQ](assets/fr/076.webp)

Sett deretter microSD-kortet tilbake i datamaskinen, og klikk på "*Load Transaction*" på Sparrow for å laste inn den signerte transaksjonen fra microSD-kortet. Deretter kan du utføre en siste kontroll før du laster den opp til Bitcoin-nettverket.

![CCQ](assets/fr/077.webp)

Den andre metoden for å signere med COLDCARD i Air-Gap, som er mye enklere enn microSD-metoden, er å skanne PSBT direkte via kameraet på enheten. På Sparrow velger du "*Vis QR*".

![CCQ](assets/fr/078.webp)

På COLDCARD velger du "*Scan Any QR Code*". Du kan også bruke "*QR*"-tasten på tastaturet.

![CCQ](assets/fr/079.webp)

Bruk COLDCARDs kamera til å skanne QR-koden som vises på Sparrow.

![CCQ](assets/fr/080.webp)

Transaksjonsdetaljene vises igjen for bekreftelse. Trykk på "*ENTER*" for å signere hvis alt er i orden.

![CCQ](assets/fr/081.webp)

COLDCARD vil da vise den signerte transaksjonen som en QR-kode. Bruk datamaskinens webkamera til å skanne denne QR-koden ved å velge "*Scan QR*" på Sparrow.

![CCQ](assets/fr/082.webp)

Den signerte transaksjonen din er nå synlig på Sparrow. Sjekk en siste gang at alt er riktig, og klikk deretter på "*Broadcast Transaction*" for å kringkaste den på Bitcoin-nettverket.

![CCQ](assets/fr/083.webp)

Du kan spore transaksjonen din i Sparrow Wallet-fanen "*Transaksjoner*".

![CCQ](assets/fr/084.webp)

Gratulerer, du har nå lært deg den grunnleggende bruken av COLDCARD Q med Sparrow Wallet!

Hvis du fant denne opplæringen nyttig, ville jeg være veldig takknemlig hvis du legger igjen en grønn tommel nedenfor. Del gjerne denne opplæringen på dine sosiale nettverk. Tusen takk skal du ha!

Jeg anbefaler også at du tar en titt på denne andre veiledningen, der vi diskuterer de avanserte alternativene i COLDCARD Q :

https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0