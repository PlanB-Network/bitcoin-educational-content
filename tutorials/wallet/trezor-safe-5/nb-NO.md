---
name: Trezor Safe 5
description: Konfigurere og bruke Hardware Wallet Safe 5
---
![cover](assets/cover.webp)



*Bildekreditt: [Trezor.io](https://trezor.io/)*



Trezor Safe 5 er siste generasjon Hardware Wallet designet av SatoshiLabs og ble lansert i 2024. Den er posisjonert som en avansert versjon av Safe 3, med fokus på ergonomi og holdbarhet. Den drar nytte av de samme sikkerhetsmessige fremskrittene som forgjengeren Safe 3, sammenlignet med Model One og Model T.



Med en pris på 169 euro er Safe 5 plassert i high-end Hardware Wallet-kategorien, og konkurrerer med modeller som Coldcard, Ledger Nano X og Flex, Jade Plus, Passport og Bitbox.



Safe 5 utmerker seg med en 1,54-tommers berøringsskjerm i farger, beskyttet av *Gorilla Glass 3*, som motstår støt og riper. Den er også utstyrt med en *Trezor Touch*-haptisk motor som avgir små vibrasjoner ved berøring. I likhet med Safe 3 har den et Secure Element og drives via en USB-C-tilkobling, med tillegg av en Micro SD-port.



Hovedforskjellen mellom Safe 3 og Safe 5 ligger i kvaliteten på enheten, bortsett fra sikkerhetsaspektene. Den forbedrer brukeropplevelsen betydelig, med jevnere betjening og en mer komfortabel skjerm. Når det gjelder sikkerhet, er de likeverdige.



![Image](assets/fr/01.webp)



Safe 5 har alle de viktigste funksjonene du forventer av en god Hardware Wallet, inkludert utmerket integrering av passphrase BIP39. Den støtter imidlertid ikke Miniscript ennå.



Denne modellen egner seg spesielt godt for nybegynnere og viderekomne brukere. På den annen side oppfyller den kanskje ikke alle forventningene til avanserte brukere som er ute etter mer spesifikke funksjoner som er tilgjengelige på enheter som Coldcard. Hvis du ikke trenger disse avanserte funksjonene, kan Trezor Safe 5 likevel være et utmerket valg.



## Sikkerhetsmodellen Trezor Safe 5



I likhet med Safe 3 er Trezor Safe 5 utstyrt med et EAL6+-sertifisert **Secure Element**, et betydelig fremskritt i forhold til tidligere modeller som Model One og Model T. Dette er OPTIGA Trust M V3-brikken, som ikke lagrer seed direkte, men som fungerer som en kryptografisk komponent for å sikre tilgangen til den. Secure Element lagrer en hemmelighet som bare er tilgjengelig når brukeren har tastet inn PIN-koden riktig. Denne hemmeligheten brukes deretter til å dekryptere seed, som lagres kryptert i enhetens hovedminne.



Dette hybride sikkerhetssystemet gir bedre fysisk beskyttelse, særlig mot uttrekksangrep eller invasiv analyse, problemer som Model One var utsatt for, spesielt i forbindelse med PIN-kodehåndtering. Disse sårbarhetene er nå omgått takket være bruken av Secure Element. Denne modellen har også en programvarearkitektur med åpen kildekode: Koden som styrer generering og bruk av private nøkler, forblir fullt tilgjengelig og verifiserbar. OPTIGA-brikken administrerer kun PIN-koden, et element som ligger utenfor Bitcoin Wallet-nøkkelhåndteringen. Den er begrenset til å frigjøre en hemmelighet som kan brukes til å dekryptere seed. OPTIGA Trust M V3-brikken drar også fordel av en relativt gratis lisens, som autoriserer SatoshiLabs til fritt å publisere potensielle sårbarheter (NDA-Free).



Denne sikkerhetsmodellen representerer etter min mening et av de beste kompromissene som finnes på markedet i dag. Den kombinerer fordelene ved et Secure Element med programvareadministrasjon med åpen kildekode. Tidligere måtte brukerne velge mellom økt fysisk sikkerhet med en chip og åpenhet med åpen kildekode; med Trezor Safe er det mulig å dra nytte av begge deler.



I denne veiledningen lærer du hvordan du konfigurerer og bruker Trezor Safe 5 på en sikker måte.



## Utpakking av Trezor Safe 5



Når du mottar Safe 5, må du kontrollere at esken og Seal er intakte for å bekrefte at pakken ikke har blitt åpnet. En programvarekontroll av enhetens autentisitet og integritet vil også bli utført når den settes opp senere.



Esken inneholder blant annet :




- Trezor Safe 5;
- En pose som inneholder kartong til å skrive inn Mnemonic-frasen, klistremerker og instruksjoner;
- USB-C til USB-C-kabel.



Når du åpner Trezor Safe 5, skal den være beskyttet av en beskyttende plast, og USB-C-porten skal være sikret med en holografisk Seal. Forsikre deg om at den er der.



![Image](assets/fr/02.webp)



Navigasjonen på enheten er ganske intuitiv:




- Trykk på den nederste halvdelen av skjermen for å bevege deg fremover;
- Skyv ned for å gå tilbake ;
- Trykk og hold på skjermen for å bekrefte en operasjon.



## Forutsetninger



I denne veiledningen skal jeg vise deg hvordan du bruker Trezor Safe 5 med [Sparrow Wallet porteføljeforvaltningsprogramvare] (https://sparrowwallet.com/download/). Hvis du ennå ikke har installert denne programvaren, bør du gjøre det nå. Hvis du trenger hjelp, har vi også en detaljert veiledning om hvordan du konfigurerer Sparrow Wallet :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Du trenger også Trezor Suite-programvaren for å konfigurere Safe 5, sjekke ektheten og installere fastvaren. Vi kommer kun til å bruke denne programvaren til dette, og etterpå vil den kun være nødvendig for fastvareoppdateringer. For daglig administrasjon av Wallet bruker vi utelukkende Sparrow Wallet, ettersom den er optimalisert for Bitcoin og enkel å bruke, selv for nybegynnere (Sparrow støtter kun Bitcoin, ikke altcoins).



[Last ned Trezor Suite fra det offisielle nettstedet] (https://trezor.io/trezor-suite)



![Image](assets/fr/03.webp)



For begge disse programmene anbefaler jeg på det sterkeste at du sjekker både ektheten (med GnuPG) og integriteten (via Hash) før du installerer dem på maskinen din. Hvis du ikke vet hvordan du gjør dette, kan du følge denne andre veiledningen :



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Oppstart av Trezor Safe 5



Koble Safe 5 til datamaskinen der Trezor Suite og Sparrow Wallet allerede er installert.



![Image](assets/fr/04.webp)



Åpne Trezor Suite, og klikk deretter på "*Set up my Trezor*".



![Image](assets/fr/05.webp)



Velg "*Bare Bitcoin-fastvare*", og klikk deretter på "*Installer bare Bitcoin*".



![Image](assets/fr/06.webp)



Trezor Suite vil deretter installere fastvaren på din Safe 5. Vennligst vent under installasjonen.



![Image](assets/fr/07.webp)



Klikk på "*Fortsett*".



![Image](assets/fr/08.webp)



Gå deretter videre til autentisitetstesten for å sikre at Hardware Wallet ikke er falsk eller kompromittert.



![Image](assets/fr/09.webp)



Trykk på skjermen på Safe 5 for å bekrefte.



![Image](assets/fr/10.webp)



Hvis Trezor er ekte, vises en bekreftelsesmelding i Trezor Suite.



![Image](assets/fr/11.webp)



Deretter kan du hoppe over vinduene med de grunnleggende bruksanvisningene.



![Image](assets/fr/12.webp)



## Opprettelse av en Bitcoin-portefølje



I Trezor Suite klikker du på knappen "*Opprett ny Wallet*".



![Image](assets/fr/13.webp)



For å opprette en standard BIP39 Wallet starter du med å velge "*Legacy Wallet backup types*" fra rullegardinmenyen, og deretter velger du mellom en Mnemonic-frase på 12 eller 24 ord (12 ord er for øyeblikket anbefalt). På denne måten kan du opprette en klassisk enkeltsignert portefølje. Jeg anbefaler at du velger BIP39-kompatible parametere her, for å gjøre det lettere å finne frem og unngå å bli begrenset til et bestemt miljø. Klikk på "*Opprett Wallet*" for å fullføre.



Hvis du vil lære mer om de andre alternativene for sikkerhetskopiering som er tilgjengelige på Trezor, inkludert *Multi-share Backup*, anbefaler jeg at du også leser denne veiledningen :



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e


![Image](assets/fr/14.webp)



Godta vilkårene for bruk på Hardware Wallet.



![Image](assets/fr/15.webp)



Trykk og hold nede skjermen for å opprette en ny portefølje.



![Image](assets/fr/16.webp)



I Trezor Suite klikker du på "*Fortsett å sikkerhetskopiere*".



![Image](assets/fr/17.webp)



Programvaren inneholder instruksjoner om hvordan du administrerer Mnemonic-frasen din.



Denne Mnemonic gir deg full, ubegrenset tilgang til alle bitcoinsene dine. Alle som er i besittelse av denne frasen kan stjele pengene dine, selv uten fysisk tilgang til Trezor Safe 5.



Frasen på 12 ord gjenoppretter tilgangen til bitcoinsene dine i tilfelle tap, tyveri eller ødeleggelse av Hardware Wallet. Det er derfor svært viktig å lagre den nøye og oppbevare den på et trygt sted.



Du kan skrive det på pappen som følger med i esken, eller for ekstra sikkerhet anbefaler jeg å gravere det på en sokkel i rustfritt stål for å beskytte det mot brann, oversvømmelse eller kollaps.



Bekreft instruksjonene, og klikk deretter på knappen "*Create Wallet backup*".



![Image](assets/fr/18.webp)



Safe 5 oppretter Mnemonic-frasen din ved hjelp av en tilfeldig tallgenerator. Forsikre deg om at du ikke blir overvåket under denne operasjonen. Skriv ned ordene som vises på skjermen, på det fysiske mediet du ønsker. Avhengig av sikkerhetsstrategien din, kan du vurdere å lage flere fullstendige fysiske kopier av frasen (men ikke del den opp). Det er viktig å holde ordene nummerert og i rekkefølge.



***Du må selvsagt aldri dele disse ordene på Internett, slik jeg gjør i denne veiledningen. Dette eksemplet Wallet vil kun bli brukt på Testnet og vil bli slettet ved slutten av opplæringen



For mer informasjon om hvordan du lagrer og administrerer Mnemonic-frasen din, anbefaler jeg på det sterkeste å følge denne andre veiledningen, spesielt hvis du er nybegynner:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/19.webp)



Klikk nederst på skjermen for å gå videre til neste ord. Du kan gå bakover ved å skyve nedover. Når du har skrevet ned alle ordene, holder du fingeren på skjermen for å gå videre til neste trinn.



![Image](assets/fr/20.webp)



Velg ordene i Mnemonic-frasen i henhold til rekkefølgen for å bekrefte at du har skrevet dem ned på riktig måte.



![Image](assets/fr/21.webp)



Når denne bekreftelsesprosedyren er fullført, klikker du på skjermen for å fortsette.



![Image](assets/fr/22.webp)



## Stille inn PIN-koden



Deretter kommer trinnet med PIN-koden. PIN-koden låser opp Trezor. Den gir derfor beskyttelse mot uautorisert fysisk tilgang. PIN-koden er ikke involvert i utledningen av de kryptografiske nøklene til Wallet. Så selv uten tilgang til PIN-koden vil du kunne få tilgang til bitcoinsene dine igjen hvis du er i besittelse av den 12-ord lange Mnemonic-frasen.



I Trezor Suite klikker du på "*Fortsett til PIN-kode*" og deretter på knappen "*Sett PIN-kode*".



![Image](assets/fr/23.webp)



Bekreft med Safe 5.



![Image](assets/fr/24.webp)



Vi anbefaler at du velger en PIN-kode som er så tilfeldig som mulig. Sørg for å lagre denne koden på et annet sted enn der Trezor er lagret (f.eks. i en passordadministrator). Du kan definere en PIN-kode på mellom 8 og 50 siffer. Jeg anbefaler at du velger en så lang PIN-kode som mulig for å øke sikkerheten.



Bruk berøringsplaten til å taste inn PIN-koden.



![Image](assets/fr/25.webp)



Når du er ferdig, klikker du på Green nederst til høyre og bekrefter PIN-koden en gang til.



![Image](assets/fr/26.webp)



PIN-koden din er registrert.



![Image](assets/fr/27.webp)



I Trezor Suite klikker du på knappen "*Fullfør oppsett*".



![Image](assets/fr/28.webp)



Konfigurasjonen av Safe 5 er nå fullført. Hvis du ønsker det, kan du endre navnet og startsiden til Hardware Wallet.



![Image](assets/fr/29.webp)



Vi trenger ikke Trezor Suite-programvaren lenger, bortsett fra for å utføre regelmessige fastvareoppdateringer på Hardware Wallet, eller hvis du ønsker å kjøre en gjenopprettingstest. Vi kommer nå til å bruke Sparrow til å administrere porteføljen, siden denne programvaren er perfekt egnet til bruk kun på Bitcoin.



## Sette opp porteføljen på Sparrow Wallet



Start med å laste ned og installere Sparrow Wallet [fra det offisielle nettstedet] (https://sparrowwallet.com/) på datamaskinen din, hvis du ikke allerede har gjort det.



Når du har åpnet Sparrow Wallet, må du sørge for at programvaren er koblet til en Bitcoin-node, noe som indikeres av krysset nederst i høyre hjørne av Interface. Hvis du har problemer med å koble til Sparrow, anbefaler jeg at du leser begynnelsen av denne veiledningen:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Klikk på fanen "*File*" og deretter på "*New Wallet*".



![Image](assets/fr/30.webp)



Gi porteføljen din et navn, og klikk deretter på "*Opprett Wallet*".



![Image](assets/fr/31.webp)



I rullegardinmenyen "*Script Type*" velger du hvilken type skript som skal brukes til å sikre bitcoinsene dine. Jeg anbefaler "*Taproot*", eller hvis du ikke klarer det, "*Native SegWit*".



![Image](assets/fr/32.webp)



Klikk på knappen "*Connected Hardware Wallet*". Safe 5 må selvfølgelig være koblet til datamaskinen og ulåst.



Når du kobler Safe 5 til en datamaskin med Sparrow Wallet åpen, vil du bli bedt om å angi en passphrase BIP39 på Hardware Wallet-skjermen. Dette avanserte alternativet vil bli dekket i en fremtidig veiledning. Inntil videre kan du bare klikke på Green-merket øverst i høyre hjørne for å bekrefte at du ønsker å bruke en tom passphrase (dvs. uten passphrase). For å forhindre at Trezor ber deg om å angi en passphrase hver gang du starter opp, går du til Trezor Suite, åpner innstillingene og endrer alternativet i "*Device*" > "*Wallet standard*" til "*Standard*" i stedet for "*passphrase*".



![Image](assets/fr/33.webp)



Klikk på "*Scan*"-knappen. Safe 5 skal vises. Klikk på "*Importer Keystore*".



![Image](assets/fr/34.webp)



Du kan nå se detaljene for din Wallet, inkludert den utvidede offentlige nøkkelen til din første konto. Klikk på "*Apply*"-knappen for å fullføre opprettelsen av Wallet.



![Image](assets/fr/35.webp)



Velg et sterkt passord for å sikre tilgangen til Sparrow Wallet. Dette passordet sikrer sikker tilgang til Sparrow Wallet-dataene dine, og beskytter de offentlige nøklene, adressene, etikettene og transaksjonshistorikken din mot uautorisert tilgang.



Jeg anbefaler deg å lagre dette passordet i en passordbehandler, slik at du ikke glemmer det.



![Image](assets/fr/36.webp)



Og nå er porteføljen din importert til Sparrow Wallet!



![Image](assets/fr/37.webp)



Før du mottar dine første bitcoins i din Wallet, ** anbefaler jeg deg på det sterkeste å utføre en tom gjenopprettingstest**. Skriv ned litt referanseinformasjon, for eksempel xpub, og tilbakestill deretter Trezor Safe 5 mens Wallet fortsatt er tom. Prøv deretter å gjenopprette Wallet på Trezor ved hjelp av papirsikkerhetskopiene dine. Sjekk at xpuben som genereres etter gjenopprettingen, samsvarer med den du opprinnelig skrev ned. Hvis den gjør det, kan du være sikker på at papirsikkerhetskopiene dine er pålitelige.



Hvis du vil lære mer om hvordan du utfører en gjenopprettingstest, anbefaler jeg at du leser denne andre veiledningen:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Hvordan kan jeg motta bitcoins med Trezor Safe 5?



I Sparrow klikker du på fanen "*Mottak*".



![Image](assets/fr/38.webp)



Før du bruker Address foreslått av Sparrow Wallet, må du sjekke den på Trezor-skjermen. På denne måten kan du bekrefte at Address som vises på Sparrow ikke er falsk, og at Hardware Wallet faktisk har den private nøkkelen som trengs for å bruke bitcoins som er sikret med denne Address. Dette hjelper deg med å unngå flere typer angrep.



For å utføre denne kontrollen klikker du på knappen "*Vis Address*".



![Image](assets/fr/39.webp)



Kontroller at Address som vises på Trezor, stemmer overens med Wallet på Sparrow. Det anbefales også å utføre denne kontrollen rett før du kommuniserer Address til avsenderen, for å være sikker på at den er gyldig. Du kan trykke på skjermen for å bekrefte.



![Image](assets/fr/40.webp)



Du kan deretter legge til en "*Label*" for å beskrive kilden til bitcoins som skal sikres med denne Address. Dette er en god praksis som gjør at du bedre kan administrere UTXO-ene dine.



![Image](assets/fr/41.webp)



Du kan deretter bruke denne Address til å motta bitcoins.



![Image](assets/fr/42.webp)



## Hvordan sender jeg bitcoins med Trezor Safe 5?



Nå som du har mottatt dine første Satss på din Safe 5-sikrede Wallet, kan du også bruke dem! Koble Trezor til datamaskinen, lås den opp med PIN-koden, start Sparrow Wallet, og gå deretter til "*Send*"-fanen for å opprette en ny transaksjon.



![Image](assets/fr/43.webp)



Hvis du ønsker å *Coin Control*, dvs. velge spesifikt hvilke UTXOer som skal brukes i transaksjonen, går du til fanen "*UTXOer*". Velg UTXO-ene du ønsker å bruke, og klikk deretter på "*Send Selected*". Du blir omdirigert til det samme skjermbildet i "*Send*"-fanen, men med UTXO-ene du allerede har valgt for transaksjonen.



![Image](assets/fr/44.webp)



Skriv inn destinasjonen Address. Du kan også legge inn flere adresser ved å klikke på "*+ Legg til*"-knappen.



![Image](assets/fr/45.webp)



Skriv ned en "*Label*" for å huske formålet med denne utgiften.



![Image](assets/fr/46.webp)



Velg beløpet som skal sendes til denne Address.



![Image](assets/fr/47.webp)



Juster gebyrsatsen for transaksjonen din i henhold til gjeldende marked. Du kan for eksempel bruke [Mempool.space] (https://Mempool.space/) for å velge en passende gebyrsats.



Kontroller at alle transaksjonsparametrene er riktige, og klikk deretter på "*Opprett transaksjon*".



![Image](assets/fr/48.webp)



Hvis du er fornøyd med alt, klikker du på "*Finalize Transaction for Signing*".



![Image](assets/fr/49.webp)



Klikk på "*Signer*".



![Image](assets/fr/50.webp)



Klikk på "*Signer*" ved siden av Trezor Safe 5.



![Image](assets/fr/51.webp)



Kontroller transaksjonsparametrene på Hardware Wallet-skjermen, inkludert mottakerens mottakende Address, beløpet som er sendt og kostnaden. Når transaksjonen er bekreftet på Trezor, trykker du på skjermen og holder den nede for å signere den.



![Image](assets/fr/52.webp)



Transaksjonen din er nå signert. Sjekk en siste gang at alt er i orden, og klikk deretter på "*Broadcast Transaction*" for å kringkaste den på Bitcoin-nettverket.



![Image](assets/fr/53.webp)



Du finner den under fanen "*Transaksjoner*" i Sparrow Wallet.



![Image](assets/fr/54.webp)



Gratulerer, du er nå oppdatert på den grunnleggende bruken av Trezor Safe 5 med Sparrow Wallet! For å ta ting et skritt videre, anbefaler jeg denne omfattende veiledningen om hvordan du bruker en Trezor Hardware Wallet med en passphrase BIP39 for å forbedre sikkerheten din:



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Hvis du fant denne opplæringen nyttig, ville jeg være takknemlig hvis du legger igjen en Green-tommel nedenfor. Del gjerne denne artikkelen på dine sosiale nettverk. Tusen takk skal du ha!