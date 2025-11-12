---
name: Ashigaru
description: fork fra Samourai Wallet for å sikre, administrere og blande bitcoins
---

![cover](assets/cover.webp)



Ashigaru er en Bitcoin-mobil wallet-applikasjon som er en videreføring av Samourai Wallet-prosjektet, men i en ny form. Denne programvaren ble født i en spesiell kontekst: I april 2024 ble grunnleggerne av Samourai Wallet arrestert av amerikanske myndigheter, og serverne deres ble beslaglagt. Selv om selve Samurai-applikasjonen fortsatt var brukbar, blir den for tiden ikke lenger vedlikeholdt. Ashigaru er en gratis fork-versjon av Samurai Wallet, vedlikeholdt av et anonymt team for å garantere kontinuiteten i Samurais funksjonalitet og ivareta den opprinnelige filosofien: å forsvare personvernet og suvereniteten til Bitcoin-brukere.



Ashigaru tar opp mye av Samourais DNA: et lignende grensesnitt, en åpenbart selvforvaltende tilnærming, åpen kildekode og fokus på personvern. Koden distribueres under GNU GPLv3-lisensen, som sikrer at hvem som helst kan revidere, modifisere eller videredistribuere programvaren.



Ashigaru-applikasjonen integrerer et sett med avanserte verktøy for konfidensialitet og administrasjon av UTXO-ene dine:




- Whirlpool**, en coinjoin-protokoll basert på Zerolink, som gjør det mulig for deg å bryte de deterministiske koblingene mellom transaksjonsinnganger og -utganger uten å miste suvereniteten over midlene dine.
- PayNym**, som implementerer gjenbrukbare betalingskoder (BIP47), nå representert via et "*Pepehash*"-avatarsystem.
- Ricochet**, en funksjon som legger til mellomliggende hopp i transaksjoner for å gjøre dem vanskeligere å spore.
- Og selvfølgelig ***Coin Control*** for å velge, fryse og merke UTXO-ene dine nøyaktig.
- Batch Spending***, for å redusere kostnadene ved å samle flere betalinger i én enkelt transaksjon.
- **Stealth Mode**, som skjuler applikasjonen på mobilen din bak en dummy-startpakke, slik at den ikke blir lagt merke til under en fysisk inspeksjon av telefonen din.
- Avanserte utgiftsverktøy for å optimalisere konfidensialiteten din (payjoin, stonewall...).
- Et optimalisert gjenopprettingssystem ved hjelp av passordfrasen BIP39.
- Et system for automatisk optimalisering av valg av transaksjonsgebyrer.



![Image](assets/fr/01.webp)



Ashigaru er derfor rettet mot brukere som er klar over problemene rundt sporbarhet av transaksjoner på Bitcoin. Enten du er en personvernsbevisst bruker, en erfaren bitcoiner som er opptatt av selvoppbevaring, eller en person som er utsatt for risikoen ved økt overvåkning, gir denne wallet-applikasjonen deg verktøyene du trenger for å gjenvinne kontrollen over aktiviteten din på Bitcoin.



Ashigaru er tilgjengelig i en mobilversjon via appen, som vi skal se nærmere på i denne veiledningen. Men det kan også brukes på PC med ***Ashigaru Terminal***, som vi vil introdusere i en senere veiledning.



![Image](assets/fr/02.webp)



I denne veiledningen vil jeg introdusere deg for grunnleggende bruk av Ashigaru: installasjon, tilkobling til Dojo, sikkerhetskopiering, mottak og sending av bitcoins. Avanserte verktøy vil bli presentert i andre dedikerte veiledninger.



## 1. Forkunnskapskrav for Ashigaru



Applikasjonen krever noen forutsetninger for å fungere skikkelig. Først og fremst er det ikke et program som er tilgjengelig i klassiske butikker som Google Play Store eller App Store. Den installeres manuelt på telefonen din bare fra `.apk`-filen, som kan lastes ned via Tor-nettverket. Så hvis du bruker en iPhone, vil ikke denne metoden fungere: du trenger en Android-enhet.



For å laste ned `.apk`-filen via Tor, trenger du en nettleser som kan få tilgang til `.onion`-nettsteder. Den enkleste måten er å installere Tor Browser-applikasjonen på telefonen din, tilgjengelig fra [Google Play Store] (https://play.google.com/store/apps/details?id=org.torproject.torbrowser) eller direkte [via `.apk`] (https://www.torproject.org/download/#android).



![Image](assets/fr/03.webp)



De fleste nyere smarttelefoner blokkerer som standard installasjon av programmer fra ukjente kilder. Du må midlertidig aktivere dette alternativet for Tor Browser i enhetens innstillinger for å tillate installasjon. Når applikasjonen er installert, må du huske å deaktivere denne funksjonen for å styrke telefonens sikkerhet.



En annen viktig forutsetning for å bruke Ashigaru er en Bitcoin Dojo-node. Av sikkerhets- og suverenitetshensyn har ikke Ashigaru-teamet en sentralisert server for å koble til applikasjonen din. Du må derfor kjøre din egen Dojo-instans, eller koble deg til en betrodd instans.



Dojo gjør det mulig for Ashigaru-applikasjonen din å konsultere informasjon om blokkjeden, se adressesaldoen din og kringkaste transaksjonene dine på Bitcoin-nettverket.



Hvis du vil vite mer om Dojo og lære hvordan du installerer det, kan du følge denne dedikerte veiledningen :



https://planb.academy/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Hvis du virkelig ikke har råd til å drive din egen Dojo, kan du finne folk som er villige til å dele instansen sin gratis på [dojobay.pw] (https://www.dojobay.pw/mainnet/). Dette kan være en midlertidig løsning, men på lang sikt anbefaler jeg at du bruker din egen Dojo for å garantere din suverenitet og konfidensialitet.



## 2. Sjekk og installer Ashigaru-applikasjonen



### 2.1. Last ned Ashigaru-applikasjonen



Åpne Tor Browser på telefonen din og gå til [det offisielle Ashigaru-nettstedet] (https://ashigaru.rs/download/), i `Last ned`-delen. Klikk deretter på knappen `Download for Android` for å laste ned installasjonsfilen.



![Image](assets/fr/04.webp)



Før du installerer applikasjonen på enheten din, kontrollerer vi dens autentisitet og integritet. Dette er et svært viktig trinn, spesielt når du installerer et program direkte fra en .apk-fil.



### 2.2. Sjekk Ashigaru-applikasjonen



Gå tilbake til [det offisielle Ashigaru-nettstedet] (https://ashigaru.rs/download/) i `Download`-delen, og kopier deretter meldingen som vises under tittelen `SHA-256 Hash av APK-filen`. Kopier hele blokken, fra `BEGIN PGP SIGNED MESSAGE` til `END PGP SIGNATURE`.



![Image](assets/fr/05.webp)



Åpne en ny fane i Tor Browser mens du fortsatt er på telefonen, og gå til [Keybase-verifiseringsverktøyet] (https://keybase.io/verify). Lim inn meldingen du nettopp har kopiert inn i det angitte feltet, og klikk deretter på `Verify`-knappen.



![Image](assets/fr/06.webp)



Hvis signaturen er ekte, vil Keybase vise en melding som bekrefter at filen er signert av Ashigaru-utviklerne. Du kan også klikke på profilen `ashigarudev` som er angitt av Keybase og sjekke at deres nøkkelfingeravtrykk samsvarer nøyaktig med : `A138 06B1 FA2A 676B`.



Hvis det imidlertid vises en feil på dette stadiet, betyr det at signaturen er ugyldig. I dette tilfellet skal du **ikke installere APK-en**. Begynn på nytt fra begynnelsen, eller be fellesskapet om hjelp før du fortsetter.



![Image](assets/fr/07.webp)



Keybase har gitt deg hashen til applikasjonen. Vi skal nå sjekke at hashen til `.apk`-filen du har lastet ned stemmer overens med den som er verifisert på Keybase. For å gjøre dette, gå til [HASH FILE ONLINE] (https://hash-file.online/).



![Image](assets/fr/08.webp)



Klikk på knappen `BROWSE...` og velg filen `.apk` som ble lastet ned i trinn 2.1.


Velg deretter hash-funksjonen `SHA-256`, og klikk på `CALCULATE HASH` for å beregne hashen til filen din.



![Image](assets/fr/09.webp)



Nettstedet vil vise hashen til `.apk`-filen din. Sammenlign den med hashen du verifiserte på Keybase.io. Hvis de to hashene er identiske, har autentisitets- og integritetskontrollen vært vellykket. Du kan nå fortsette å installere applikasjonen.



![Image](assets/fr/10.webp)



### 2.3. Installer Ashigaru-applikasjonen



For å installere applikasjonen åpner du telefonens filbehandling og går til nedlastingsmappen. Klikk deretter på .apk-filen du nettopp har sjekket, og bekreft installasjonen når du blir bedt om det.



![Image](assets/fr/11.webp)



Ashigaru er nå installert på telefonen din.



## 3. Initialiser appen og opprett en Bitcoin-portefølje



Når du starter programmet for første gang, velger du `MAINNET`.



![Image](assets/fr/12.webp)



Klikk deretter på "Kom i gang".



![Image](assets/fr/13.webp)



Vi skal nå opprette en ny Bitcoin-portefølje. Trykk på knappen `Opprett en ny wallet`.



![Image](assets/fr/14.webp)



### 3.1. Opprett en Bitcoin-portefølje



Ashigaru krever en passphrase BIP39. Velg din passphrase og skriv den inn i de aktuelle feltene. Den må være så lang og tilfeldig som mulig for å motstå et brute-force-angrep.



Ta en fysisk sikkerhetskopi av denne passphrase umiddelbart. Dette er et svært viktig trinn: Hvis du mister telefonen din, **hvis du ikke lenger har denne passphrase, vil du ikke lenger kunne få tilgang til bitcoins** som er lagret med Ashigaru wallet. Den samme passphrase brukes også til å kryptere gjenopprettingsfilen til wallet.



Hvis du ikke vet hva en passphrase er, eller ikke helt forstår hvordan den fungerer, anbefaler jeg på det sterkeste at du leser denne ekstra veiledningen. Dette er viktig, fordi passphrase er et kritisk element i sikkerheten din: Hvis du misforstår bruken av den, kan det føre til permanent tap av pengene dine.



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Når du har tastet inn passphrase, klikker du på `NESTE`.



![Image](assets/fr/15.webp)



Velg deretter en PIN-kode. Denne koden brukes til å låse opp Ashigaru wallet og beskytter den mot uautorisert fysisk tilgang. Den er ikke involvert i den kryptografiske utledningen av wallet-nøklene dine. Dette betyr at selv uten å kjenne PIN-koden, vil alle som har minnefrasen din og passphrase kunne få tilgang til bitcoinsene dine.



Velg en lang, tilfeldig PIN-kode. Husk å oppbevare en sikkerhetskopi på et annet sted enn telefonen, for å forhindre at begge blir kompromittert samtidig.



![Image](assets/fr/16.webp)



Når PIN-koden er opprettet, viser Ashigaru den mnemoniske frasen til din wallet. Advarsel: Denne frasen, kombinert med din passphrase, gir full tilgang til bitcoinsene dine. Alle som har den, kan ta pengene dine i besittelse, selv om de ikke har tilgang til telefonen din. Denne sekvensen på 12 ord kan brukes til å gjenopprette wallet i tilfelle tap, tyveri eller ødeleggelse av telefonen din. Det er derfor viktig å lagre den med største forsiktighet på et fysisk medium (papir eller metall).



Lagre aldri denne setningen i digital form, da risikerer du at pengene dine blir utsatt for tyveri. Avhengig av sikkerhetsstrategien din kan du lage flere fysiske kopier, men del den aldri opp. Behold ordene i nøyaktig samme rekkefølge, og sørg for at de er nummererte.



Til slutt må du aldri lagre minnepennen og passphrase på samme sted. Hvis begge blir kompromittert samtidig, kan en angriper få tilgang til wallet.



![Image](assets/fr/17.webp)



Hvis du vil vite mer om hvordan du sikrer den mnemotekniske frasen, kan du lese denne utfyllende veiledningen :



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Ashigaru ber deg deretter om å bekrefte passphrase på nytt. Benytt anledningen til å sjekke at den fysiske sikkerhetskopien din er korrekt.



![Image](assets/fr/18.webp)



### 3.2. Koble til en dojo



Neste trinn er å koble til Dojoen din. Som forklart i innledningen, må Ashigaru være koblet til en Dojo for å kunne samhandle med Bitcoin-nettverket.



Logg deg på Dojoens "Maintenance Tool" og åpne menyen `PAIRING`.



![Image](assets/fr/19.webp)



På Ashigaru trykker du på "Skann QR"-knappen og skanner deretter QR-koden for tilkobling som vises av DMT-enheten. Klikk deretter på "Fortsett" for å bekrefte.



![Image](assets/fr/20.webp)



Skriv inn PIN-koden din for å låse opp wallet. Dette tar deg til synkroniseringssiden. Det er normalt å se *PayNym*-feil på dette stadiet, ettersom wallet er ny. Bare klikk på "Fortsett".



![Image](assets/fr/21.webp)



Du kommer da til startsiden for porteføljen din.



![Image](assets/fr/22.webp)



Før du går videre, anbefaler jeg at du utfører en testgjenoppretting mens wallet fortsatt ikke inneholder bitcoin. På denne måten kan du sjekke at papirbackupene fungerer som de skal. Følg denne veiledningen for å finne ut hvordan du gjør det:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 4. Sette opp Ashigaru-applikasjonen



For å få tilgang til applikasjonsinnstillingene klikker du på bildet av *PayNym* øverst i venstre hjørne, og velger deretter `Innstillinger`.



![Image](assets/fr/23.webp)



Her finner du flere alternativer for å tilpasse Ashigarus funksjon til dine behov. Jeg anbefaler imidlertid på det sterkeste at du aktiverer to viktige parametere helt fra starten av.



Start med å åpne menyen `Sikkerhet > Stealth-modus`, og aktiver deretter denne funksjonen hvis du trenger den. Den skjuler Ashigaru-programmet bak navnet, logoen og grensesnittet til et vanlig program som er installert på telefonen din. Målet er å forhindre at noen kan identifisere Ashigaru ved en eventuell fysisk inspeksjon av telefonen din.



![Image](assets/fr/24.webp)



Hver falske applikasjon som tilbys har en spesifikk metode for å låse opp det ekte Ashigaru-grensesnittet. Hvis du for eksempel velger kalkulatoren, forsvinner Ashigaru-applikasjonen fra startskjermen og erstattes av en falsk kalkulator. Når du åpner den, ser du et klassisk kalkulatorgrensesnitt, men for å få tilgang til Ashigaru, er alt du trenger å gjøre å trykke raskt på `=`-symbolet fem ganger.



Den andre viktige parameteren som må aktiveres, er [**RBF** (*Replace-by-Fee*)] (https://planb.academy/resources/glossary/rbf-replacebyfee). Med dette alternativet kan du øke kostnaden for en transaksjon hvis den blir sittende fast i mempools fordi kostnaden er for lav. Du kan aktivere det via menyen `Transaksjoner > Bruk RBF`.



![Image](assets/fr/25.webp)



Tips: Du kan endre visningsenheten for porteføljen din fra `BTC` til `sat` ved å klikke på den totale saldoen som vises på startsiden.



## 5. Motta bitcoins på Ashigaru



Nå som porteføljen din er i drift, kan du motta satss. Dette gjør du ved å trykke på `+`-knappen nederst til høyre i grensesnittet, og deretter på den grønne `Motta`-knappen.



![Image](assets/fr/26.webp)



Ashigaru viser deg deretter den første ubrukte mottakeradressen i wallet, for å forhindre gjenbruk av adresser (gjenbruk av adresser er en svært dårlig praksis for personvernet ditt). Du kan deretter videresende denne adressen til personen eller tjenesten som trenger å sende deg bitcoins.



![Image](assets/fr/27.webp)



Når transaksjonen er sendt ut i nettverket, vises den automatisk på startsiden til applikasjonen.



![Image](assets/fr/28.webp)



## 6. Send bitcoins med Ashigaru



Nå som du har bitcoins i Ashigaru wallet, kan du også sende dem. For å gjøre det, trykk på `+`-knappen nederst til høyre, og velg deretter den røde `Send`-knappen.



![Image](assets/fr/29.webp)



Velg deretter kontoen du ønsker å bruke penger fra. Foreløpig har vi ikke tatt for oss postmix-kontoen, som er reservert for coinjoins, og som vi skal se på i en senere veiledning. Så vi kommer til å sende penger fra hovedinnskuddskontoen.



![Image](assets/fr/30.webp)



Skriv inn transaksjonsopplysningene dine: beløpet som skal sendes og mottakerens Bitcoin-adresse.



![Image](assets/fr/31.webp)



Ved å klikke på de tre små prikkene øverst i høyre hjørne, og deretter på `Vis ubrukte utganger`, kan du også velge nøyaktig hvilke UTXO-er du ønsker å bruke, for å forbedre personvernet ditt.



![Image](assets/fr/32.webp)



Når du har fylt ut alle opplysningene, klikker du på den hvite pilen nederst i grensesnittet for å fortsette.



Du kommer da til en oppsummeringsside som viser alle detaljene i transaksjonen din. Flere viktige elementer vises:




- I `Destination`-blokken kontrollerer du en siste gang at mottakeradressen og det sendte beløpet er riktig;
- I blokken "Avgifter" kan du se avgiftssatsen som Ashigaru automatisk har valgt, og om nødvendig endre den ved å klikke på "ADMINISTRER";
- Transaksjonsblokken angir hvilken type transaksjon du er i ferd med å utføre. Her snakker vi om en enkel transaksjon, men Ashigaru støtter også andre typer personvernoptimaliserte transaksjoner, som vi vil gå nærmere inn på i en senere veiledning;
- Den røde blokken "Transaksjonsvarsel" advarer deg hvis transaksjonen din viser mønstre som kan gjenkjennes av verktøyene for kjedeanalyse, og som kan kompromittere personvernet ditt. Ved å klikke på den kan du se detaljene. I mitt tilfelle forteller Ashigaru meg for eksempel at beløpet som er sendt er rundt (`3000 sats`), slik at jeg kan utlede hvilken utgang som tilsvarer utgiften og hvilken som er utvekslingen. For å finne ut mer om disse kjedeanalyseheuristikkene, inviterer jeg deg til å følge BTC 204-opplæringen min på Plan ₿ Academy ;
- Til slutt kan du legge til en etikett på transaksjonen for å holde oversikt over formålet med den.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Når du har kontrollert all informasjonen, bruker du den grønne pilen til å sende bitcoins. Hold pilen nede, og dra den deretter til høyre for å bekrefte opplastingen.



![Image](assets/fr/33.webp)



Transaksjonen din har blitt sendt på Bitcoin-nettverket.



![Image](assets/fr/34.webp)



## 7. Gjenopprette din Ashigaru wallet



Gjenoppretting av en Ashigaru wallet skiller seg litt fra en klassisk Bitcoin wallet, ettersom applikasjonen bruker de samme metodene som Samurai Wallet. Hvis du mister tilgangen til din wallet (enten fordi du har glemt PIN-koden, avinstallert den eller mistet telefonen), finnes det flere måter å gjenopprette bitcoinsene dine på.



Hvis du fortsatt har tilgang til telefonen din, eller hvis du har tatt en sikkerhetskopi av denne filen, er den enkleste metoden å bruke sikkerhetskopifilen `ashigaru.txt`. Denne filen inneholder all informasjonen du trenger for å gjenopprette porteføljen din på en ny instans av Ashigaru (eller på Sparrow Wallet), men den er kryptert med passphrase som du definerte i trinn 3.1 i denne veiledningen. Du må derfor ha både filen `ashigaru.txt` og din passphrase for å bruke denne metoden.



Med disse to elementene kan du for eksempel gjenopprette porteføljen din på Sparrow Wallet.



![Image](assets/fr/35.webp)



Hvis du ikke har tilgang til filen `ashigaru.txt`, kan du likevel få tilbake tilgangen til midlene dine ved å bruke huskereglene fra passphrase, akkurat som du ville gjort for alle andre Bitcoin-porteføljer. Jeg anbefaler at du utfører denne gjenopprettingen enten på en ny Ashigaru-forekomst eller direkte på Sparrow Wallet, slik at du enkelt kan gjenopprette omkjøringsbanene fra Whirlpool hvis du brukte den. Alternativt kan du importere denne informasjonen til en hvilken som helst annen BIP39-kompatibel programvare ved å legge inn avledningsstiene manuelt.



For mer informasjon om denne prosessen, vennligst se den komplette veiledningen jeg har skrevet om å gjenopprette en Wallet Samurai wallet. Siden Ashigaru er en fork, er prosedyren identisk:



https://planb.academy/tutorials/wallet/backup/samourai-recover-23bb6221-ea3e-42e6-a5b7-e6dbef5073c3

Som du ser, er passphrase uunnværlig uansett hvilken restaureringsmetode du bruker. Så sørg for å sikkerhetskopiere den nøye. Du kan også lage flere kopier, avhengig av sikkerhetsstrategien din.



## 8. Oppdater søknad



For å oppdatere Ashigaru-appen, siden du installerte den fra en `.apk`-fil og ikke via Play Store som en vanlig app, må du laste ned den nye `.apk`-filen som tilsvarer den oppdaterte versjonen, og deretter installere den manuelt.



Gjenta trinnene som er beskrevet i del 2 av denne veiledningen, bortsett fra at når du klikker på .apk-filen for å starte installasjonen, skal ** Android-telefonen din tilby deg alternativet `Oppdater`, ikke `Installer`**.



![Image](assets/fr/41.webp)



Dette er et veldig viktig poeng: hvis Android viser `Install` i stedet for `Oppdater`, installerer du sannsynligvis en falsk versjon. I dette tilfellet må du avbryte installasjonsprosedyren umiddelbart.



Som med den første installasjonen, må du kontrollere ektheten og integriteten til `.apk`-filen før du fortsetter med oppdateringen.



For å finne ut når en ny versjon er tilgjengelig, kan du sjekke det offisielle Ashigaru-nettstedet fra tid til annen. Du kan være trygg på at Ashigaru er et stabilt, modent program, arvet fra Samourai Wallet, og oppdateringer er relativt sjeldne sammenlignet med yngre programvare.



## 9. Gi en gave til Ashigaru-prosjektet



Ashigaru er et prosjekt med åpen kildekode. Hvis du ønsker å støtte utviklingen, kan du gi en donasjon direkte fra applikasjonen via PayNym.



Dette gjør du ved å klikke på ditt PayNym øverst til høyre i grensesnittet, og deretter velge betalingskoden som begynner med `PM...`.



![Image](assets/fr/36.webp)



Trykk deretter på knappen `+` nederst til høyre på skjermen.



![Image](assets/fr/37.webp)



Velg `Ashigaru Open Source Project` som mottaker.



![Image](assets/fr/38.webp)



Klikk på `CONNECT`-knappen for å opprette en BIP47-kommunikasjonskanal (se mer om denne protokollen i veiledningen nedenfor).



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

![Image](assets/fr/39.webp)



Når varslingstransaksjonen er bekreftet, kan du sende donasjonene dine til prosjektet ved å klikke på den lille hvite pilen øverst til høyre i grensesnittet.



![Image](assets/fr/40.webp)



Du vet nå hvordan du bruker de grunnleggende funksjonene i Ashigaru-programmet. I fremtidige veiledninger vil vi se på hvordan du kan dra nytte av avanserte utgiftstransaksjoner, samt Whirlpool, coinjoin-implementeringen som er arvet fra Samurai Wallet.
https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add
