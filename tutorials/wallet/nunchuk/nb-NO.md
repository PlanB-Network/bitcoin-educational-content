---
name: Nunchuk
description: Wallet mobil egnet for alle
---
![cover](assets/cover.webp)



## En kraftig Wallet


Nunchuk kom i slutten av 2020 med en klar filosofi: å gjøre multisignatur til en standard. Den ble derfor designet for å utføre svært avanserte funksjoner, med det verdifulle valget å bygge designet direkte på Bitcoin Core, referanseprogramvaren for Bitcoin-økosystemet.



Etter mer enn fire år med utvikling og bruk er den nå klar til å prøves ut i stor skala. Hvis du er nybegynner og ikke er kjent med Nunchuk, vil denne veiledningen hjelpe deg med å ta de første skrittene og oppdage denne programvaren, hvis avanserte funksjoner du vil kunne lære om etter at du har kommet deg forbi det første støtet. Selve opplæringen er dedikert til mellombrukere som har de nødvendige ferdighetene for å følge alle trinnene, men den kan være en inspirasjon for alle til å finne ut hvordan man kan øke ferdighetene. Vi begynner med mobilversjonen, og dette er nødvendig å påpeke, siden Nunchuk har programvaren til å kjøre på datamaskiner også.



## Last ned


Det første trinnet er definitivt å bestemme hvor du skal laste ned appen. Gå til [official site](https://nunchuk.io/), der du finner litt dokumentasjon (ikke mye, men det er en begynnelse), en presentasjon av funksjonene samt, mot slutten av siden, alle nedlastingslenkene.



📌 For denne opplæringen bestemte jeg meg for å vise deg hvordan du laster ned Software Wallet fra Github-depotet og hvordan du verifiserer utgivelsen før du installerer den på mobiltelefonen din. **Følgende prosedyre kan bare gjøres fra datamaskinen din **, så jeg anbefaler at du gjør alle disse trinnene fra din stasjonære eller bærbare datamaskin og - etter alle bekreftelsene - overfører `.apk` -filen til mobiltelefonen din.



![image](assets/en/01.webp)



Hvis du ikke er veldig avansert, kan du velge å laste ned `.apk` fra de offisielle butikkene og hoppe direkte til konfigurasjonsdelen av denne veiledningen. Hvis du derimot ønsker å ta spranget, kan du fortsette å følge trinn for trinn.



Så fra datamaskinen din klikker du på _Besøk vårt arkiv for åpen kildekode_



Lenken tar deg til Nunchuks Github-side, hvor du finner en rekke repos. Vi vil fokusere på _nunchuk-android_



![image](assets/en/02.webp)



På neste skjermbilde finner du til høyre delen om _Releases_ og velger _Latest_



![image](assets/en/03.webp)



Under _Assets_ laster du ned utgivelsen (i dette eksempelet 1.67.apk), sammen med SHA256SUMS-filen og SHA256SUMS.asc.



![image](assets/en/04.webp)



For å finne utviklerens GPG-nøkkel, gå tilbake til _Releases_-delen av repositoriet og se etter 1.9.53 (eller tidligere) som inneholder lenken til å skaffe og laste ned _GPG Key_



![image](assets/en/05.webp)



Vi vil fortsette med verifiseringen ved hjelp av et praktisk verktøy som tilbys av Sparrow wallet, som har et eget vindu for dette formålet og støtter PGP-signaturer og SHA256 Manifests.



Start deretter Sparrow, og velg _Verify Download_ fra _Tools_-menyen.



![image](assets/en/06.webp)



I vinduet som dukker opp, finner du felter som skal "fylles ut": Velg _Browse_-knappen til høyre og velg, for hvert felt, de tilsvarende filene du nettopp har lastet ned fra Github. Når du har fullført alle trinnene, vil vinduet se ut som følger, med Green-avkrysninger og Hash-bekreftelse av manifestet.



![image](assets/en/07.webp)


**Skjermbildet er fra en Windows-PC, men samme fremgangsmåte kan brukes på alle operativsystemer på datamaskinen din, bare du har Sparrow wallet installert. Og verifisert!**



Du kan finne veiledningen til Sparrow wallet for å laste ned denne Software Wallet


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Deretter kan du overføre .apk-filen fra datamaskinen til telefonen



![image](assets/en/08.webp)



og installer Nunchuk



![image](assets/en/09.webp)



Før du starter Nunchuk på telefonen, åpner du Orbot og legger nykommeren i listen over apper som skal dirigeres under Tor.



![image](assets/en/11.webp)



Nå kan du kjøre Nunchuk. For prosjektfunksjoner - som ikke er tema for denne veiledningen - vil Nunchuk, når den er åpnet, invitere deg til å logge inn via en e-post eller Google-profil. Inntil du planlegger å dra nytte av Nunchuk Incs avanserte planer, **unngå å logge inn** og fortsett ved å velge alternativet _Continue as guest_.



![image](assets/en/12.webp)



## Innstillinger


Nunchuk presenterer seg med et _Home_-vindu, der det er lett å forstå betjeningsfilosofien, og som vi skal gå nærmere inn på om et øyeblikk.



Nederst finner du menyene, og som første trinn velger du _Profil_ for å få tilgang til innstillingene.



![image](assets/en/10.webp)



Velg deretter _Vis innstillinger_, og fortsett å ignorere invitasjonen til å opprette en konto.



![image](assets/en/14.webp)



I skjermbildet nedenfor kan du sjekke om Wallet er online, og du kan koble til serveren din ved å følge instruksjonene i lenken som tilbys ved å klikke på _denne veiledningen_.



![image](assets/en/15.webp)



Lagre innstillingene med kommandoen _Lagre nettverksinnstillinger_, gå tilbake til menyen _Profil_, og velg _Sikkerhetsinnstillinger_.



![image](assets/en/16.webp)



Fra denne menyen kan du angi hvordan du vil forsvare åpningen av appen. For å forhindre uønsket tilgang kan du beskytte Nunchuk med telefonens biometri og/eller legge til en sikkerhets-PIN-kode.



![image](assets/en/17.webp)



Ta også en titt på _Om_-menyen, som du alltid finner i _Profil_-vinduet



![image](assets/en/18.webp)



som lar deg sjekke versjonen av appen, eller kontakte utviklerne ved behov.



![image](assets/en/19.webp)



## Nøkkelgenerering og Wallet


Som det er lett å gjette ut fra Nunchuks filosofi, er programvaren ment som et nyttig verktøy for å administrere lommebøker med flere signaturer. For å utføre denne funksjonen gjør Nunchuk det mulig å opprette Wallet ved å skille dem fra nøklene som trengs for å arrangere digitale signaturer.



Faktisk innebærer den ideelle driften av Nunchuk opprettelsen av lommebøker som bare kan være ur, avhengig av nøkler som kan være "Colds"



I de foregående skjermbildene har du kanskje lagt merke til at det finnes en meny nederst som heter _Keys_. Hvis du nettopp har lastet ned Nunchuk, vil du i både _Home_ og _Keys_ se en stor knapp som inviterer deg til å legge til en nøkkel, _Add Key_.



![image](assets/en/20.webp)


![image](assets/en/21.webp)



**Slik fungerer Nunchuk:** Først generate/importerer du nøklene, og deretter oppretter du Wallet og konfigurerer den til å velge hvilke nøkler som skal autorisere opplåsing av midlene som er lagret på den.



Selv når det gjelder Wallet singlesig, lager du nøkkelen først og først deretter Wallet. Og det er akkurat det vi skal gjøre nå, og vi starter med en Wallet singlesig for å bryte isen og oppdage funksjonene til Nunchuk.



Klikk på _Legg til nøkkel_



![image](assets/en/22.webp)



Nunchuk viser en rekke støttede signaturenheter, men til å begynne med velger du _Software_.



![image](assets/en/23.webp)



Nunchuk vil generate en Mnemonic som vil bli lagret på enheten. Deretter må du skrive ned rekkefølgen av ord for sikkerhetskopieringen, skape de beste miljøforholdene og sørge for at du har tid til å gjøre det godt og stille. Programvaren viser Mnemonic bare én gang, enten du velger å vise den nå eller senere, så velg _Create and backup now_.



![image](assets/en/24.webp)



Nunchuk genererer 24 ords Mnemonic setninger, som vises umiddelbart på neste skjermbilde



![image](assets/en/25.webp)



og fortsatte deretter med en rask sjekk, der du ble bedt om å velge riktig ord, blant tre valg, som tilsvarer nummeret i Mnemonic-sekvensen.


Hvis du har skrevet Mnemonic riktig, blir _Continue_-knappen operativ. Trykk på den for å gå videre.



![image](assets/en/26.webp)



Gi nøkkelen et navn, og trykk på _Continue_.



![image](assets/en/27.webp)



På slutten av disse trinnene vil du bli spurt om du vil legge til en [passphrase](https://planb.academy/en/resources/glossary/passphrase-bip39) til Mnemonic-frasen din. Hvis du ikke har den nødvendige kunnskapen om hvordan du bruker passphrase, sørger for sikkerhetskopiering eller hvordan det fungerer, anbefaler jeg at du velger _Jeg trenger ikke en passordfrase_.



![image](assets/en/28.webp)



Nøkkelen er endelig opprettet og vises i menyen:




- Med _Key Spec_ angis hovedfingeravtrykket
- Du har innstillinger, de tre punktene øverst til høyre, der du kan slette nøkkelen eller signere en melding
- Ved siden av navnet på nøkkelen finner du et spiss-ikon som du kan klikke på for å redigere navnet på nøkkelen, for eksempel for å holde orden på nøklene dine i fremtiden.
- Som en siste kommando kan du sjekke nøkkelens helsestatus: Ved å trykke på _Run health check_ kan du få appen til å sjekke om en nøkkel er kompromittert.



Når du er ferdig, klikker du på _Done_



![image](assets/en/29.webp)



I _Keys_-menyen ser du den første tasten din.



![image](assets/en/30.webp)



Ved å gå til _Home_-menyen, vises muligheten til å opprette Wallet. Klikk på _Create new wallet_.



![image](assets/en/31.webp)



Nunchuk viser deg en rekke muligheter som for det meste har å gjøre med tjenester selskapet tilbyr, og som ikke er tema for denne veiledningen.



I denne veiledningen vil vi opprette en _Hot Wallet og en _Custom wallet_ ved å beskrive detaljene.


La oss begynne med _Custom wallet_.



![image](assets/en/32.webp)



På en enkel måte vil appen be deg om å navngi denne nye Wallet og velge skriptet for adressene. I denne veiledningen valgte jeg å la standardinnstillingen, _Native segwit_, stå. Når du er ferdig, velger du _Continue_



![image](assets/en/33.webp)



I konfigurasjonen av Wallet blir du bedt om å angi med hvilken nøkkel midlene til denne Wallet skal låses opp. Hvis det finnes flere nøkler, får du opp en liste som du kan velge mellom. Vi har for øyeblikket bare opprettet én, så vi velger å sette en hake ved den. Nederst i høyre hjørne kan du se hvordan Nunchuk vil be deg om å sette opp dine fremtidige Wallet multisignaturer, noe som øker antallet _Nødvendige nøkler_.



![image](assets/en/34.webp)



Siden vi oppretter en singlesig, lar vi `1` stå og klikker på _Continue_.



Til slutt vises et bekreftelsesskjermbilde der du kan sjekke funksjonene til Wallet:




- navnet
- 1/1 Multisig` tage, som er slik Nunchuk kaller Wallet singlesig
- skripttypen, `Native SegWit`
- nøkkelen `Keys`, med fingeravtrykk og avledningssti



Når du er fornøyd, trykker du på _Create wallet_



![image](assets/en/35.webp)



Wallet er opprettet, og du kan laste ned [.BSMS](https://github.com/Bitcoin/bips/blob/master/bip-0129.mediawiki)-filen som en sikkerhetskopi. For å gå tilbake til hovedmenyen klikker du på pilen i øvre venstre hjørne.



![image](assets/en/36.webp)



Du befinner deg i _Home_, der du ser den nyopprettede Wallet som rapporterer saldo og status for tilkoblingen. Ved å klikke i det blå feltet får du tilgang til hovedfunksjonene i Wallet.



![image](assets/en/37.webp)





- Med linseikonet øverst i høyre hjørne kan du gjøre et transaksjonssøk;
- `View Wallet config` gir tilgang til konfigurasjonsmenyen, der du kan redigere navnet på Wallet og aktivere avanserte alternativer, øverst til høyre (som du ikke kan få skjermbilder av). Her kan du eksportere Wallet-konfigurasjonen, etiketter, erstatte taster, endre [gap limit](https://planb.academy/en/resources/glossary/gap-limit) og mer.



## Transaksjoner med Nunchuk



Utmerkelser _Mottar__



![image](assets/en/38.webp)



Appen er programmert til å vise QR-koden til Address eller kopiere/dele scriptPubKey for å motta midler i kjeden.



![image](assets/en/39.webp)



Vi hadde en UTXO som ankom på denne første Address,



![image](assets/en/40.webp)



men vi klikker likevel på _Mottak_ for å motta en ny.



![image](assets/en/41.webp)



Hensikten er at du skal finne ut at Nunchuk rapporterer denne nye Address til deg som en _Ubenyttet adresse_, men også viser deg at du har _Brukte adresser_ og antallet av disse.



### Utgiftstransaksjon med myntkontroll



Når denne andre UTXO også har ankommet, går du tilbake til Wallet-hovedskjermbildet for å sjekke statusen til de to innkommende transaksjonene, og, viktigst av alt, klikk på alternativet _Vis mynter_



![image](assets/en/42.webp)



hvor du vil få vist individuelle UTXO-er. Her kan du velge å se en bestemt UTXO ved å klikke på den lille pilen ved siden av beløpet



![image](assets/en/43.webp)



og sjekk når den ankom, beskrivelsen, blokker UTXO slik at den ikke blir brukt og mer.



![image](assets/en/44.webp)



Men hvis du går tilbake til _Coins_-menyen ved å klikke på pilen øverst i høyre hjørne, kan du slå på "Coin Control" for å bruke UTXO-ene dine på en mer kontrollert måte.



I eksemplet nedenfor valgte jeg å velge UTXO av 21 000 Sats og deretter klikke på symbolet i nedre venstre hjørne.



![image](assets/en/45.webp)



Nunchuk åpner automatisk vinduet _Ny transaksjon_ for å bruke denne UTXO. I utgiftstransaksjonen må du først angi beløpet manuelt eller ved å velge _Send all selected_ for å sende hele myntkontrollsaldoen, uten å generere restbeløp. Når beløpet er angitt, velger du _Continue_



![image](assets/en/46.webp)



Nå viser Nunchuk hvor du skal lime inn Address som du skal overføre pengene til, angi en beskrivelse og fullføre transaksjonen.



![image](assets/en/47.webp)



Ved å velge _Create transaction_ delegeres automatisk gebyr- og transaksjonshåndtering til appen. Jeg anbefaler å velge _Custom transaction_ for å få mer kontroll.



I dette nye skjermbildet er det viktig å velge




- _Trekk gebyr fra sendebeløp_, for å forhindre at gebyrer betales av en annen UTXO som er til stede i Wallet, bruker det og genererer et restbeløp (som er et unngåelig tap av personvern);
- og deretter angi avgiftene manuelt etter å ha sjekket på utforskeren.



Når du har utført alle disse trinnene, klikker du på _Continue_



![image](assets/en/48.webp)



Det neste skjermbildet er et fullstendig sammendrag av transaksjonen. Hvis alt er i orden, bekrefter du ved å velge _Cbekreft og opprett transaksjon_.



![image](assets/en/49.webp)



Med _Venter på signaturer_ varsler Nunchuk deg om at transaksjonen venter på din signatur for å godkjenne utgiften, som du setter ved å klikke på _Signer_.



![image](assets/en/50.webp)



Kommandoen _Broadcast_ vises nederst for å spre den ferdigstilte og signerte transaksjonen.



![image](assets/en/51.webp)



### Bruk av transaksjon fra menyen _Send_



Mens vi på hovedsiden i Wallet ser at transaksjonen går ut og venter på bekreftelse, bruker vi _Send_-menyen til å simulere en daglig utgift.



![image](assets/en/52.webp)



Når du klikker på _Send_, får du nemlig opp skjermbildet for sending av transaksjonen, som er det samme som det du nettopp så, men uten å gå gjennom myntkontrollen.



Også i dette andre eksempelet valgte jeg å velge _Custom transaction_ og sende hele beløpet, men jeg kunne ha angitt det manuelt. Når du har bestemt deg for hvilket beløp du vil sende, trykker du på _Continue_.



![image](assets/en/53.webp)



Deretter må du alltid vurdere om gebyrene skal trekkes fra den aktuelle UTXO (i dette eksemplet er valget tvunget, fordi det bare finnes én), justere gebyrene manuelt i henhold til situasjonen på det aktuelle tidspunktet i Mempool, og trykke på _Continue_.



![image](assets/en/54.webp)



Hvis oppsummeringsskjermbildet er tilfredsstillende, velger du _Confirm and create transaction_.



![image](assets/en/55.webp)



Signer transaksjonen med _Sign_



![image](assets/en/56.webp)



og spre det til nettverket.



![image](assets/en/57.webp)



Wallet er på dette punktet med saldoen på null og historikken blir oppdatert.



![image](assets/en/58.webp)



## Opprettelse av en "Hot Wallet"



Til slutt, og for ikke å utelate noe fra de innledende stadiene av Nunchuk mobile, la oss se hvordan dette skaper det appen kaller "Hot Wallet"



I _Home_-menyen i Nunchuk, der listen over lommebøker vises, klikker du på `+` i øvre høyre hjørne.



![image](assets/en/59.webp)



Velg _Hot wallet_ fra alternativene



![image](assets/en/60.webp)



Nunchuk gir noen råd om håndtering av Hot Wallets på presentasjonssiden, der du velger _Continue_ for å gå videre.



![image](assets/en/61.webp)



Etter noen øyeblikk er Wallet opprettet og vises i listen med en brunaktig farge. Dette er fargen som Nunchuk bruker for å varsle deg om at du ennå ikke har sikkerhetskopiert Wallet.



![image](assets/en/62.webp)



Klikk på navnet til Wallet for å få tilgang til konfigurasjonene, og du vil kanskje legge merke til en invitasjon til å sikkerhetskopiere Mnemonic-setningen umiddelbart.



![image](assets/en/63.webp)



Fremgangsmåten er den samme som vi har sett før, så vi skal ikke gå gjennom den igjen. Når det er gjort, tar Nunchuk deg til den aktuelle nøkkelsiden, som du kan redigere som den du opprettet med _Custom_-prosedyren.



![image](assets/en/64.webp)



Prøv også _Kjør helsesjekk_



![image](assets/en/65.webp)



eller for å se hvordan du viser alle lommebøkene dine i _Home_ i appen.



![image](assets/en/66.webp)



## Å huske på å fortsette selvstendig


På samme måte som det er en rekkefølge for opprettelse, det vil si at du først genererer nøklene og deretter Wallet, må du opprettholde den omvendte rekkefølgen for sletting av disse elementene fra appen din.



Hvis du har behov for å slette en av nøklene, bør du først være forutseende nok til å slette Wallet, eller Wallets, som bruker en av signaturnøklene for transaksjoner: Først sletter du Wallets, og først deretter nøklene. Hvis du ikke følger denne rekkefølgen, vil du ikke kunne fjerne nøkkelen.



Nå som du vet hvordan du kommer i gang med Nunchuk, kan du fortsette å studere denne appen og oppdage dens hemmeligheter. I denne veiledningen har vi bare tatt de første stegene, men det finnes mer sofistikerte applikasjoner og avanserte behov som denne Software Wallet kan hjelpe deg med å dekke.