---
name: Trezor Model One
description: Sette opp og bruke Hardware Wallet Model One
---
![cover](assets/cover.webp)



*Bildekreditt: [Trezor.io](https://trezor.io/)*



Trezor Model One er den aller første Hardware Wallet som noensinne ble lansert, og ble lansert i 2014 av SatoshiLabs. Etter mer enn ti år er den fortsatt et interessant valg, spesielt for brukere som leter etter en Hardware Wallet som er tilgjengelig både teknisk og når det gjelder budsjett. Faktisk er den priset til €49 på den offisielle Trezor-nettsiden. Det er en av de eneste maskinvarelommebøkene i denne prisklassen. Den ligger midt mellom innstegsenheter til rundt €20, som Tapsigner, som ofte mangler skjerm, og mellomklasseenheter til rundt €80, som Ledger Nano S Plus eller Trezor Safe 3.



Model One har en 0,96-tommers monokrom OLED-skjerm og to fysiske knapper. Den fungerer uten batteri, og bruker kun en mikro-USB-tilkobling for strøm og data Exchange.



![Image](assets/fr/01.webp)



Den største ulempen med Model One er at den mangler Secure Element, noe som gjør den sårbar for en rekke fysiske angrep, hvorav noen er relativt enkle å utføre. Disse angrepene kan omfatte analyse av hjelpekanaler for å finne enhetens PIN-kode, eller mer avanserte teknikker for å hente ut den krypterte seed-koden for senere å brute-force den. Merk at disse angrepene krever fysisk tilgang til enheten. Denne sårbarheten kan imidlertid reduseres betraktelig ved å bruke en solid passphrase BIP39. Hvis du velger denne Hardware Wallet, anbefaler jeg på det sterkeste at du konfigurerer en passphrase.



Model One har to viktige fordeler:




- Den er basert på en arkitektur med helt åpen kildekode. I motsetning til nyere modeller med Secure Element er alle maskinvare- og programvarekomponenter i Model One reviderbare;
- Den er utstyrt med en skjerm. Så vidt jeg vet, er dette den eneste Hardware Wallet på markedet i denne prisklassen med skjerm. Dette er en svært viktig funksjon, ettersom den gjør det mulig å verifisere signert informasjon og mottaksadresser, og dermed forhindre mange digitale angrep.



Trezor Model One kan derfor være et godt valg for nybegynnere og viderekomne brukere med et begrenset budsjett. Det er imidlertid viktig å være klar over begrensningene når det gjelder fysisk beskyttelse, på grunn av fraværet av Secure Element. Hvis budsjettet ditt er begrenset, er dette et godt alternativ, men hvis du har råd til å velge en bedre modell, for eksempel Trezor Safe 3 til 79 euro, er den å foretrekke, siden den inkluderer et Secure Element.



## Utpakking av Trezor Model One



Når du mottar Model One, må du kontrollere at esken og Seal er intakte for å bekrefte at pakken ikke har blitt åpnet. En programvareverifisering av enhetens autentisitet og integritet vil også bli utført når den settes opp senere.



Esken inneholder blant annet :




- Trezor Model One;
- Kartongpapir til å skrive inn Mnemonic-frasen, klistremerker og instruksjoner;
- USB-A til mikro-USB-kabel.



![Image](assets/fr/02.webp)



Det er veldig enkelt å navigere i enheten:




- Høyreklikk for å bekrefte og gå videre til neste trinn;
- Bruk venstre knapp for å gå tilbake.



## Forutsetninger



I denne veiledningen skal jeg vise deg hvordan du bruker Trezor Model One sammen med [Sparrow Wallet portfolio management software] (https://sparrowwallet.com/download/). Hvis du ennå ikke har installert denne programvaren, bør du gjøre det nå. Hvis du trenger hjelp, har vi også en detaljert veiledning om hvordan du konfigurerer Sparrow Wallet :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Du trenger også Trezor Suite-programvaren for å konfigurere Model One, sjekke ektheten og installere fastvaren. Vi kommer kun til å bruke denne programvaren til dette, og etterpå vil den kun være nødvendig for fastvareoppdateringer. For daglig administrasjon av Wallet vil vi utelukkende bruke Sparrow Wallet, siden den er optimalisert for Bitcoin og enkel å bruke, selv for nybegynnere (Sparrow støtter kun Bitcoin, ikke altcoins).



[Last ned Trezor Suite fra det offisielle nettstedet] (https://trezor.io/trezor-suite)



![Image](assets/fr/03.webp)



For begge disse programmene anbefaler jeg på det sterkeste at du sjekker både ektheten (med GnuPG) og integriteten (via Hash) før du installerer dem på maskinen din. Hvis du ikke vet hvordan du gjør dette, kan du følge denne andre veiledningen :



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Starte Trezor Model One



Koble Model One til datamaskinen der Trezor Suite og Sparrow Wallet allerede er installert.



![Image](assets/fr/04.webp)



Åpne Trezor Suite, og klikk deretter på "*Set up my Trezor*".



![Image](assets/fr/05.webp)



Velg "*Bare Bitcoin-fastvare*", og klikk deretter på "*Installer bare Bitcoin*".



![Image](assets/fr/06.webp)



Trezor Suite vil deretter installere fastvaren på Model One. Vennligst vent under installasjonen.



![Image](assets/fr/07.webp)



Klikk på "*Fortsett*".



![Image](assets/fr/08.webp)



## Opprettelse av en Bitcoin-portefølje



I Trezor Suite klikker du på knappen "*Opprett ny Wallet*".



![Image](assets/fr/09.webp)



Godta vilkårene for bruk på Hardware Wallet.



![Image](assets/fr/10.webp)



I Trezor Suite klikker du på "*Fortsett å sikkerhetskopiere*".



![Image](assets/fr/11.webp)



Programvaren inneholder instruksjoner om hvordan du administrerer Mnemonic-frasen din.



Denne Mnemonic gir deg full, ubegrenset tilgang til alle bitcoinsene dine. Alle som er i besittelse av denne frasen kan stjele pengene dine, selv uten fysisk tilgang til Trezor Model One.



Frasen på 24 ord gjenoppretter tilgangen til bitcoinsene dine i tilfelle tap, tyveri eller ødeleggelse av Hardware Wallet. Det er derfor svært viktig å lagre den nøye og oppbevare den på et trygt sted.



Du kan skrive det på pappen som følger med i esken, eller for ekstra sikkerhet anbefaler jeg å gravere det på en sokkel i rustfritt stål for å beskytte det mot brann, oversvømmelse eller kollaps.



Bekreft instruksjonene, og klikk deretter på knappen "*Create Wallet backup*".



![Image](assets/fr/12.webp)



Model One oppretter Mnemonic-frasen din ved hjelp av en tilfeldig tallgenerator. Forsikre deg om at du ikke blir overvåket under denne operasjonen. Skriv ned ordene som vises på skjermen, på det fysiske mediet du ønsker. Avhengig av sikkerhetsstrategien din, kan du vurdere å lage flere fullstendige fysiske kopier av frasen (men ikke del den opp). Det er viktig å holde ordene nummerert og i rekkefølge.



***Du må selvsagt aldri dele disse ordene på Internett, slik jeg gjør i denne veiledningen. Dette eksemplet Wallet vil kun bli brukt på Testnet og vil bli slettet ved slutten av opplæringen



Hvis du vil ha mer informasjon om hvordan du lagrer og administrerer Mnemonic-frasen din, anbefaler jeg på det sterkeste å følge denne andre veiledningen, spesielt hvis du er nybegynner:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Høyreklikk for å gå videre til neste ord. Når du har skrevet ned alle ordene, høyreklikker du igjen for å gå videre til neste trinn.



![Image](assets/fr/13.webp)



Hardware Wallet viser deg igjen alle ordene dine. Sjekk at du har skrevet dem ned.



![Image](assets/fr/14.webp)



## Stille inn PIN-koden



Deretter kommer trinnet med PIN-koden. PIN-koden låser opp Trezor. Den gir derfor beskyttelse mot uautorisert fysisk tilgang. PIN-koden er ikke involvert i utledningen av de kryptografiske nøklene til Wallet. Så selv uten tilgang til PIN-koden vil du kunne få tilgang til bitcoinsene dine igjen hvis du er i besittelse av den 12-ord lange Mnemonic-frasen.



I Trezor Suite klikker du på "*Fortsett til PIN-kode*" og deretter på knappen "*Sett PIN-kode*".



![Image](assets/fr/15.webp)



Bekreft på Model One.



![Image](assets/fr/16.webp)



Vi anbefaler at du velger en PIN-kode som er så tilfeldig som mulig. Sørg for å lagre denne koden på et annet sted enn der Trezor er lagret (f.eks. i en passordadministrator). Du kan definere en PIN-kode på mellom 8 og 50 siffer. Jeg anbefaler at du velger en så lang PIN-kode som mulig for å øke sikkerheten.



PIN-koden må tastes inn i Trezor Suite på datamaskinen ved å klikke på punktene som tilsvarer sifrene, i henhold til tastaturkonfigurasjonen som vises på Trezor Model One.



Denne spesifikke PIN-koden kreves hver gang du låser opp Trezor Model One, enten det er via Trezor Suite eller Sparrow Wallet.



![Image](assets/fr/17.webp)



Når du er ferdig, klikker du på knappen "*Enter PIN*".



![Image](assets/fr/18.webp)



Skriv ned PIN-koden din igjen for å bekrefte.



![Image](assets/fr/19.webp)



I Trezor Suite klikker du på knappen "*Fullfør oppsett*".



![Image](assets/fr/20.webp)



Konfigurasjonen av Model One er nå fullført. Hvis du ønsker det, kan du endre navnet og startsiden til Hardware Wallet.



![Image](assets/fr/21.webp)



Vi trenger ikke Trezor Suite-programvaren lenger, bortsett fra for å utføre regelmessige fastvareoppdateringer på Hardware Wallet, eller hvis du ønsker å kjøre en gjenopprettingstest. Vi kommer nå til å bruke Sparrow til å administrere porteføljen, ettersom denne programvaren er perfekt egnet for bruk av Bitcoin.



## Sette opp porteføljen på Sparrow Wallet



Start med å laste ned og installere Sparrow Wallet [fra det offisielle nettstedet] (https://sparrowwallet.com/) på datamaskinen din, hvis du ikke allerede har gjort det.



Når du har åpnet Sparrow Wallet, må du sørge for at programvaren er koblet til en Bitcoin-node, noe som indikeres av krysset nederst i høyre hjørne av Interface. Hvis du har problemer med å koble til Sparrow, anbefaler jeg at du leser begynnelsen av denne veiledningen:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Klikk på fanen "*File*" og deretter på "*New Wallet*".



![Image](assets/fr/22.webp)



Gi porteføljen din et navn, og klikk deretter på "*Opprett Wallet*".



![Image](assets/fr/23.webp)



I rullegardinmenyen "*Script Type*" velger du hvilken type skript som skal brukes til å sikre bitcoinsene dine. Jeg anbefaler "*Taproot*", eller hvis du ikke klarer det, "*Native SegWit*".



![Image](assets/fr/24.webp)



Klikk på knappen "*Connected Hardware Wallet*". Model One må selvfølgelig være koblet til datamaskinen.



![Image](assets/fr/25.webp)



Klikk på "*Scan*"-knappen. Model One skal vises.



Når du kobler Model One til en datamaskin med Sparrow Wallet åpen, vil du bli bedt om å angi en passphrase BIP39 på Sparrow. Dette avanserte alternativet vil bli dekket i en fremtidig veiledning. Inntil videre kan du ganske enkelt velge "*Toggle passphrase Off*" for å forhindre at Trezor ber deg om å angi en passphrase hver gang du starter opp.



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

![Image](assets/fr/26.webp)



Klikk på "*Importer nøkkellager*".



![Image](assets/fr/27.webp)



Du kan nå se detaljene for din Wallet, inkludert den utvidede offentlige nøkkelen til din første konto. Klikk på "*Apply*"-knappen for å fullføre opprettelsen av Wallet.



![Image](assets/fr/28.webp)



Velg et sterkt passord for å sikre tilgangen til Sparrow Wallet. Dette passordet sikrer sikker tilgang til Sparrow Wallet-dataene dine, og beskytter de offentlige nøklene, adressene, etikettene og transaksjonshistorikken din mot uautorisert tilgang.



Jeg anbefaler deg å lagre dette passordet i en passordbehandler, slik at du ikke glemmer det.



![Image](assets/fr/29.webp)



Og nå er porteføljen din importert til Sparrow Wallet!



![Image](assets/fr/30.webp)



Før du mottar dine første bitcoins i din Wallet, ** anbefaler jeg deg på det sterkeste å utføre en tom gjenopprettingstest**. Skriv ned noe referanseinformasjon, for eksempel xpub, og tilbakestill deretter Trezor Model One mens Wallet fortsatt er tom. Prøv deretter å gjenopprette Wallet på Trezor ved hjelp av papirsikkerhetskopiene dine. Sjekk at xpuben som genereres etter gjenopprettingen, stemmer overens med den du opprinnelig skrev ned. Hvis den gjør det, kan du være sikker på at papirsikkerhetskopiene dine er pålitelige.



Hvis du vil lære mer om hvordan du utfører en gjenopprettingstest, anbefaler jeg at du leser denne andre veiledningen:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Hvordan motta bitcoins med Trezor Model One?



I Sparrow klikker du på fanen "*Mottak*".



![Image](assets/fr/31.webp)



Før du bruker Address foreslått av Sparrow Wallet, må du sjekke den på Trezor-skjermen. På denne måten kan du bekrefte at Address som vises på Sparrow ikke er falsk, og at Hardware Wallet faktisk har den private nøkkelen som trengs for å bruke bitcoins som er sikret med denne Address. Dette hjelper deg med å unngå flere typer angrep.



For å utføre denne kontrollen klikker du på knappen "*Vis Address*".



![Image](assets/fr/32.webp)



Kontroller at Address som vises på Trezor, stemmer overens med Wallet på Sparrow. Det anbefales også å utføre denne kontrollen rett før du kommuniserer Address til avsenderen, for å være sikker på at den er gyldig. Du kan trykke på høyre knapp for å bekrefte.



![Image](assets/fr/33.webp)



Du kan også legge til en "*Label*" for å beskrive kilden til bitcoins som skal sikres med denne Address. Dette er en god praksis som gjør at du bedre kan administrere UTXO-ene dine.



![Image](assets/fr/34.webp)



Du kan deretter bruke denne Address til å motta bitcoins.



![Image](assets/fr/35.webp)



## Hvordan sende bitcoins med Trezor Model One?



Nå som du har mottatt dine første Satss i din Model One-sikrede Wallet, kan du også bruke dem! Koble Trezor til datamaskinen, start Sparrow Wallet, og gå deretter til "*Send*"-fanen for å opprette en ny transaksjon.



![Image](assets/fr/36.webp)



Hvis du ønsker å *Coin Control*, dvs. velge spesifikt hvilke UTXOer som skal brukes i transaksjonen, går du til fanen "*UTXOer*". Velg UTXO-ene du ønsker å bruke, og klikk deretter på "*Send Selected*". Du blir omdirigert til det samme skjermbildet i "*Send*"-fanen, men med UTXO-ene du allerede har valgt for transaksjonen.



![Image](assets/fr/37.webp)



Skriv inn destinasjonen Address. Du kan også legge inn flere adresser ved å klikke på "*+ Legg til*"-knappen.



![Image](assets/fr/38.webp)



Skriv ned en "*Label*" for å huske formålet med denne utgiften.



![Image](assets/fr/39.webp)



Velg beløpet som skal sendes til denne Address.



![Image](assets/fr/40.webp)



Juster gebyrsatsen for transaksjonen i henhold til gjeldende marked. Du kan for eksempel bruke [Mempool.space] (https://Mempool.space/) for å velge en passende gebyrsats.



Kontroller at alle transaksjonsparametrene er riktige, og klikk deretter på "*Opprett transaksjon*".



![Image](assets/fr/41.webp)



Hvis du er fornøyd med alt, klikker du på "*Finalize Transaction for Signing*".



![Image](assets/fr/42.webp)



Klikk på "*Signer*".



![Image](assets/fr/43.webp)



Klikk på "*Sign*" ved siden av Trezor Model One.



![Image](assets/fr/44.webp)



Kontroller transaksjonsparametrene på Hardware Wallet-skjermen, inkludert mottakerens mottakende Address, det sendte beløpet og gebyret. Når transaksjonen er bekreftet på Trezor, høyreklikker du for å signere den.



![Image](assets/fr/45.webp)



Transaksjonen din er nå signert. Kontroller en siste gang at alt er i orden, og klikk deretter på "*Broadcast Transaction*" for å kringkaste den på Bitcoin-nettverket.



![Image](assets/fr/46.webp)



Du finner den under fanen "*Transaksjoner*" i Sparrow Wallet.



![Image](assets/fr/47.webp)



Gratulerer, du er nå oppdatert på den grunnleggende bruken av Trezor Model One med Sparrow Wallet! For å ta ting et skritt videre, anbefaler jeg denne omfattende veiledningen om bruk av en Hardware Wallet Trezor med en passphrase BIP39 for å forsterke sikkerheten din :



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Hvis du fant denne opplæringen nyttig, vil jeg være takknemlig hvis du legger igjen en Green-tommel nedenfor. Del gjerne denne artikkelen på dine sosiale nettverk. Tusen takk skal du ha!