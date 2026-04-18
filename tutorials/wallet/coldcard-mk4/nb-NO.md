---
name: COLDCARD Mk4
description: En veiledning for oppsett og bruk av COLDCARD Mk4 med Sparrow Wallet
---

![cover-mk4](assets/cover.webp)


**Hardware wallets** er fysiske enheter som er laget kun for å lagre Bitcoins private nøkkel på en sikker måte. De lagrer de private nøklene offline, noe som betyr at hackere ikke kan nå dem via internett. Mens **programvare-wallet-er** hovedsakelig brukes til hverdagstransaksjoner, brukes **hardware-wallet-er** ofte til å lagre større mengder bitcoins sikkert over lang tid. Når du foretar en Bitcoin-transaksjon ved hjelp av **hardware wallets**, kan wallet signere transaksjonene inne i enheten, slik at den private nøkkelen aldri blir eksponert for internett-tilkoblede miljøer.


I denne opplæringen vil vi utforske en av de mest populære maskinvare-wallet-ene produsert av Coinkite, Coldcard Mk4. Vi skal se på hvordan du setter opp og bruker denne maskinvare-wallet til å utføre Bitcoin-transaksjoner.


## Coldcard Mk4 Oversikt


Coldcard Mk4 er en Bitcoin-bare maskinvare wallet produsert av Coinkite. Denne enheten er utstyrt med en skjerm, et numerisk tastatur og et beskyttende skyvedeksel. I tillegg tilbyr enheten flere måter å koble til og samhandle på, inkludert USB-C, luftgapet drift ved hjelp av et MicroSD-kort, NFC og en virtuell diskmodus. Mk4 inkluderer også avanserte sikkerhetsfunksjoner som BIP39 passphrase og lure-PIN-koder, noe som gir brukerne større kontroll og beskyttelse over Bitcoin.


## Første oppsett: PIN-kode og antihishing-ord


For å komme i gang kan Coldcard Mk4 kjøpes direkte fra [Coinkites nettsted] (https://store.coinkite.com/store). Kjøpere kan også velge å betale med fiat-valuta eller Bitcoin. I tillegg trenger du også et MicroSD-kort (4 GB er tilstrekkelig) og en strømkilde som kan kobles til via USB-C-kabel (Coldcard Mk4 har kun en USB-C-strøminngangsport). Merk at siden Mk4 ikke har et innebygd batteri, må den være koblet til strømkilden til enhver tid mens den brukes.


Du vil motta din Mk4 i en pose som er sikret mot manipulering. Vennligst forsikre deg om at posen ikke har blitt ødelagt. Hvis du oppdager noe som kan være et problem, for eksempel skader eller rifter på posen, kan du informere Coinkite ved å sende en e-post til support@coinkite.com. I tillegg finner du også et 12-sifret nummer på den sabotasjesikre posen, som vi vil referere til som Mk4s posenummer. Dette posenummeret vil bli brukt senere for å verifisere at enheten ikke har blitt tuklet med under forsendelsen, og at den kommer direkte fra Coinkite. Posenummeret lagres sikkert i Cold-kortets secure element ved hjelp av OTP (One-Time-Programmable) flashminne, noe som betyr at det ikke kan endres når det først er programmert. Når du slår på enheten for første gang, må nummeret som vises på skjermen, stemme overens med nummeret på posen. Dette sikrer at Mk4-enheten du har mottatt, er den originale enheten fra fabrikken og ikke har blitt byttet ut eller modifisert. Selv om denne verifiseringen bare bekrefter enhetens integritet når den slås på for første gang, fortsetter secure element å beskytte de private nøklene, PIN-koden og passphrase, noe som gjør det svært vanskelig for manipulasjon å kompromittere din Bitcoin. I tillegg vil god praksis, som å sikre dine wallet-relaterte data på riktig måte, være gunstig for den generelle sikkerheten til selve Cold-kortet. For ytterligere informasjon kan du se denne [artikkelen] (https://blog.coinkite.com/understanding-mk4-security-model/) som utdyper Cold-kortets sikkerhetsmodell.


Tastaturet består av 10 numeriske knapper, en OK-knapp (`✓`) og en avbryt-knapp (`✕`). Noen av de numeriske knappene kan også brukes til navigering: `5` for å navigere oppover (`^`), `7` for å navigere til venstre (`<`), `8` for å navigere nedover (`˅`) og `9` for å navigere til høyre (`>`).


![01](assets/en/01.webp)


Hvis det ikke er noen problemer med emballasjen, kan du åpne posen. Mk4 leveres med et wallet backup-kort som kan brukes til å lagre informasjon om enhetens PIN-kode, anti-phishing-ord og seedphrase. Følg følgende trinn for initialisering:


1. Finn frem et stykke papir og en penn.

2. Koble Mk4 til en strømkilde (USB-C-kabel), og sett inn MicroSD-kortet.

3. Når enheten er slått på for første gang, vises en melding om Coldcards salgs- og bruksvilkår på skjermen. Naviger nedover, og trykk deretter på `✓` for å fortsette.

4. Deretter vises et 12-sifret nummer på skjermen. Sammenlign dette nummeret med nummeret på posen med sabotasjesikring og den ekstra kopien av posenummeret som fulgte med i posen med sabotasjesikring, for å sikre at enheten ikke har blitt tuklet med. Hvis numrene ikke stemmer overens, må du kontakte Coinkite support umiddelbart før du fortsetter. Ellers trykker du på `✓` for å fortsette.


![02](assets/en/02.webp)


5. Velg `Velg PIN-kode`.

6. Naviger nedover mens du leser instruksjonene for å gå videre til neste trinn.


![03](assets/en/03.webp)


7. På Mk4 oppretter og skriver du inn PIN-kodeprefikset (må være mellom 2 og 6 tegn langt) og skriver det ned, og deretter trykker du på `✓` for å fortsette.

8. Skriv ned de to ordene som vises på skjermen. Dette er anti-phishing-ordene. Trykk på `✓` for å fortsette.


![04](assets/en/04.webp)


9. Opprett og skriv inn PIN-suffikset (eller resten av PIN-koden, må være mellom 2 og 6 tegn lang), og skriv det ned. Trykk på `✓` for å fortsette.

10. Skriv inn PIN-prefikset ditt på nytt. Trykk på `✓` for å fortsette.


![05](assets/en/05.webp)


11. Sjekk om anti-phishing-ordene er de samme som de du skrev i trinn 8. Trykk på `✓` for å fortsette.

12. Skriv inn PIN-koden på nytt (eller resten av PIN-koden). Trykk på `✓` for å fortsette.


![06](assets/en/06.webp)


13. PIN-koden og anti-phishing-ordene til din Mk4 er nå opprettet og lagret av enheten.


![07](assets/en/07.webp)


Merk at Mk4 alltid vil be deg om å taste inn PIN-koden din hver gang du slår på enheten. Uten denne PIN-koden får du ikke tilgang til Coldcard Mk4. Sørg derfor for at du tar tilstrekkelig sikkerhetskopi av PIN-koden og anti-phishing-ord.


## Sette opp din Wallet


Neste trinn er å konfigurere wallet. Det er tre måter du kan gjøre dette på:


- Opprette en ny wallet (standard)
- Opprette en ny wallet med terningkast
- Importerer en wallet


### Opprette en ny wallet (standard)


Gjør følgende for å opprette en ny wallet.


1. Velg `Nye Wallet` (eller `Nye seed-ord`) > Velg `12 ord` eller `24 ord (standard)`, avhengig av hva du foretrekker.


![08](assets/en/08.webp)


2. Enheten genererer 12 eller 24 ord som seedphrase, avhengig av hva du velger. Naviger nedover mens du skriver nøye ned hvert ord i riktig rekkefølge. Trykk deretter på `✓` for å fortsette.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

3. Enheten vil be deg om å verifisere din seedphrase ved å stille spørsmålene i en tilfeldig rekkefølge (for eksempel "Ord 1 er?", deretter "Ord 5 er?", deretter "Ord 12 er?", og så videre), og det vil være tre ordvalg for hvert spørsmål. Se notatet fra trinn 2 og velg ordene riktig (ved å trykke på `1`, `2` eller `3`, avhengig av hva som tilsvarer det riktige ordet) for å fullføre skapelsen av wallet.


![09](assets/en/09.webp)


4. Mk4 vil da spørre om du vil aktivere NFC/Tap eller ikke. For øyeblikket velger du `✕` for dette alternativet. Dette kan endres i innstillingene i fremtiden.

5. Til slutt vil Mk4 også spørre deg om du vil deaktivere USB-porten (som kan brukes til dataoverføring som ikke er luftgapet). For øyeblikket velger du `✓` for dette alternativet. Dette kan endres i innstillingene i fremtiden.

6. Skjermen vil nå vise hovedmenyen med "Klar til å signere" øverst. Dette markerer at opprettelsesprosessen for wallet er fullført.


![10](assets/en/10.webp)


### Opprette en ny wallet med terningkast


Alternativt kan du også velge å generere den nye seedphrase med entropi. Gjør det hvis du ikke stoler på Mk4s nygenererte seedphrase.


Fremgangsmåten på Coldcard Mk4 er som følger:


1. Velg `Nye Wallet` (eller `Nye frøord`) > Velg `12 ord terningkast` eller `24 ord terningkast`, avhengig av hva du foretrekker.

2. Du vil bli bedt om å oppgi resultatene av terningkastene dine. Hvert terningkast tilfører tilfeldigheter til wallet-opprettelsesprosessen, noe som sikrer at seedphrase genereres på en helt sikker og uforutsigbar måte. Minimum antall terningkast er 50 for seedphrase med 12 ord og 99 for seedphrase med 24 ord. Trykk på `✓` etter at du har lagt inn minst 99 terningkastverdier.


![11](assets/en/11.webp)


3. Enheten genererer 12 eller 24 ord som seedphrase, avhengig av hva du velger. Naviger nedover mens du skriver nøye ned hvert ord i riktig rekkefølge. Trykk deretter på `✓` for å fortsette.

4. Enheten vil be deg om å verifisere din seedphrase ved å stille spørsmålene i en tilfeldig rekkefølge (for eksempel "Ord 1 er?", deretter "Ord 5 er?", deretter "Ord 12 er?", og så videre), og det vil være tre ordvalg for hvert spørsmål. Se notatet fra trinn 3 og velg ordene riktig (ved å trykke på `1`, `2` eller `3`, avhengig av hva som tilsvarer det riktige ordet) for å fullføre skapelsen av wallet.


![12](assets/en/12.webp)


5. Mk4 vil da spørre om du vil aktivere NFC/Tap eller ikke. For øyeblikket velger du `✕` for dette alternativet. Dette kan endres i innstillingene i fremtiden.

6. Til slutt vil Mk4 også spørre deg om du vil deaktivere USB-porten (som kan brukes til dataoverføring som ikke er luftgapet). For øyeblikket velger du `✓` for dette alternativet. Dette kan endres i innstillingene i fremtiden.

7. Skjermen vil nå vise hovedmenyen med "Klar til å signere" øverst. Dette markerer at opprettelsesprosessen for wallet er fullført.


![13](assets/en/13.webp)


### Importerer en wallet


Det siste alternativet er at du importerer en wallet. Dette kan du gjøre hvis du vil gjenopprette en wallet fra en seedphrase som du allerede har. Du kan følge disse trinnene:


1. Velg `Importer eksisterende`.

2. Velg "24 ord", "18 ord" eller "12 ord", avhengig av antall ord i din seedphrase.


![14](assets/en/14.webp)


3. Coldcard Mk4 vil deretter spørre deg hva hvert ord er i fortløpende rekkefølge. For hvert ord navigerer du nedover eller oppover til du finner skriveprefikset for hvert ord. Enheten vil begrense mulighetene til du finner det riktige ordet. Gjør det samme for resten av ordene.

4. For det siste ordet vil Coldcard Mk4 bare vise et begrenset antall mulige ord. Hvis det ikke finnes noen treff, kan det hende at du har tastet inn ordene feil. I motsatt fall velger du det ordet som samsvarer med ordet på seedphrase.


![15](assets/en/15.webp)


5. Mk4 vil da spørre om du vil aktivere NFC/Tap eller ikke. For øyeblikket velger du `✕` for dette alternativet. Dette kan endres i innstillingene i fremtiden.

6. Til slutt vil Mk4 også spørre deg om du vil deaktivere USB-porten (som kan brukes til dataoverføring som ikke er luftgapet). For øyeblikket velger du `✓` for dette alternativet. Dette kan endres i innstillingene i fremtiden.

7. Skjermen vil nå vise hovedmenyen med "Klar til å signere" øverst. Dette markerer at opprettelsesprosessen for wallet er fullført.


![16](assets/en/16.webp)


Vær oppmerksom på at seedphrase er den eneste tilgangen til å gjenopprette wallet. Lag en sikkerhetskopi av din seedphrase og oppbevar den på et sikkert sted. **Ikke nøklene dine, ikke myntene dine**, den som har din seedphrase har tilgang til bitcoinsene dine!


## Sette opp din passphrase


En av de beste fremgangsmåtene i Bitcoin er å bruke en passphrase. passphrase fungerer som det 13. eller 25. ordet i tillegg til seedphrase. Det som gjør det annerledes, er at du kan velge hvilken frase du vil, mens seedphrase velges fra en forhåndsbestemt liste med 2048 ord. Når du har konfigurert wallet, starter du som standard med en wallet med en tom passphrase. For å sette opp en passphrase som ikke er tom, gjør du ganske enkelt følgende:


1. Gå til `Passphrase`.

2. Naviger ned for å lese beskrivelsen om passphrase, og trykk deretter på `✓` for å fortsette.

3. Velg "Rediger frase".


![17](assets/en/17.webp)


4. Skriv inn din passphrase:


   - Trykk på `1` (bokstaver), `2` (tall) eller `3` (symboler) for å velge tegntype.
   - Trykk på `4` for å veksle mellom små og store bokstaver (kan bare brukes når du skriver inn bokstaver).
   - Naviger ved hjelp av `^` eller `˅` for å velge tegnet for din passphrase.
   - Bruk `<` eller `>` for å navigere mellom tegn. Du kan også bruke `>` for å legge til mellomrom.
   - Trykk på `✕` for å slette tegnene.
   - Trykk på `✓` når du er ferdig med å redigere passphrase.

5. I tillegg har de andre alternativene følgende funksjoner:


   - Med "Legg til ord" eller "Legg til tall" kan du legge til bokstaver/numre i passphrase som du er i ferd med å redigere.
   - Trykk på `Clear ALL` for å nullstille passphrase som du er i ferd med å redigere.
   - Trykk på `CANCEL` for å gå tilbake til hovedmenyen.

6. Skriv ned passphrase som en sikkerhetskopi.

7. Trykk på `APPLY` for å få tilgang til wallet med den passphrase du nettopp har stilt inn.

8. Mk4 vil da vise et 8 tegn langt hovednøkkelfingeravtrykk. Dette kan betraktes som "ID-en" til wallet. Skriv ned dette fingeravtrykket, og trykk på `✓` for å fortsette.


![18](assets/en/18.webp)


9. Nå vil wallet vise hovedmenyen til wallet med passphrase som du har lagt inn.

10. Det er viktig å merke seg at en wallet ikke vil fortelle deg at du har tastet inn feil passphrase, fordi hver passphrase korresponderer med hver sin wallet med en unik identitet (hovednøkkelens fingeravtrykk). Derfor er det lurt å taste inn den samme passphrase-en på nytt og sjekke om den produserer det samme wallet-fingeravtrykket, slik at du er sikker på at du har tastet den riktig. Dette gjør du ved å utføre trinn 11 til 14.

11. På hovedmenyen velger du `Restore Master`, og trykker deretter på `✓`. Du er nå tilbake i hovedmenyen på wallet med den tomme passphrase.


![19](assets/en/19.webp)


12. Gå til `Passphrase` igjen, og trykk deretter på `✓` for å fortsette.

13. Skriv inn passphrase som du skrev ned i trinn 6, og trykk deretter på `APPLY`.

14. Kontroller det 8 tegn lange hovednøkkelfingeravtrykket mot det du skrev ned i trinn 8. Hvis begge fingeravtrykkene ikke stemmer overens, kan det hende at du har skrevet inn feil tegn. Du kan velge en ny passphrase i stedet og gjenta prosessen fra trinn 1. Men hvis begge fingeravtrykkene stemmer overens, betyr det at du har tastet inn passphrase på riktig måte.

15. wallet med den valgte passphrase er klar til bruk.


## Eksportere Wallet til Sparrow


I likhet med andre maskinvare-wallet-er kan ikke Coldcard Mk4 brukes alene. Det må kobles til en programvare-wallet som fungerer som et grensesnitt. Med programvaren wallet kan du se saldoen din, opprette transaksjoner og administrere adresser, mens Coldcard signerer transaksjonene på en sikker måte uten å eksponere de private nøklene dine.


I denne veiledningen vil vi bruke Sparrow Wallet som grensesnitt. Fremgangsmåten for å eksportere wallet er som følger:


1. Sørg for at du har satt inn et MicroSD-kort i Mk4.

2. Utfør trinnene i "Sette opp passphrase" på wallet med passphrase som du ønsker å eksportere. Hvis du vil eksportere wallet med den tomme passphrase, kan du hoppe over dette trinnet.

3. Gå til `Avansert/Verktøy` > Velg `Eksporter Wallet` > Velg `Generisk JSON` > Bla nedover mens du leser instruksjonene, og trykk deretter på `✓`.


![20](assets/en/20.webp)


4. Mk4 har nå opprettet en fil med `.json`-format på MicroSD-kortet.


![21](assets/en/21.webp)


5. Ta ut MicroSD-kortet fra Cold-kortet og sett det inn i enheten der Sparrow Wallet er installert.

6. Åpne Sparrow Wallet.

7. Klikk på `File`


![22](assets/en/22.webp)


Deretter klikker du på `Ny Wallet`


![23](assets/en/23.webp)


Skriv deretter inn navnet på wallet


![24](assets/en/24.webp)


Deretter klikker du på "Opprett Wallet


![25](assets/en/25.webp)


8. Velg `Script Type`.


![26](assets/en/26.webp)


9. Velg `Airgapped Hardware Wallet` i Keystore-delen.


![27](assets/en/27.webp)


10. Se etter Coldcard og klikk på `Importer fil...`.


![28](assets/en/28.webp)


11. Velg filen som ble opprettet i trinn 4 (den med formatet `.json`).


![29](assets/en/29.webp)


12. Gå tilbake til hovedmenyen på Mk4 og naviger til `Avansert/Verktøy` > `Vis identitet`. Kontroller at fingeravtrykket som vises på Mk4-skjermen, stemmer overens med fingeravtrykket på Sparrow Wallet (Master-fingeravtrykket i Keystore-delen)

13. Klikk på knappen `Apply` nederst i høyre hjørne.


![30](assets/en/30.webp)


14. Du kan også legge til et passord for den eksporterte wallet. Dette passordet kreves hver gang du åpner Sparrow Wallet-applikasjonen for å få tilgang til wallet. Hvis du glemmer passordet i fremtiden, kan du bare gjenta trinn 1-13 og velge et nytt passord.


![31](assets/en/31.webp)


15. wallet er nå eksportert og klar til bruk.


![32](assets/en/32.webp)


## Mottak av bitcoin


Nå skal vi lære hvordan du mottar Bitcoin ved hjelp av Mk4. Denne prosessen er ganske enkel fordi du ikke trenger å bruke selve Mk4-enheten. Så lenge du allerede har eksportert din wallet til Sparrow, kan du motta Bitcoin direkte gjennom Sparrow Wallet. Følg disse trinnene for å motta bitcoins med Mk4:


1. Åpne Sparrow Wallet.

2. Velg `Åpne Wallet` > Velg wallet-filen som du vil motta bitcoin til > Skriv inn passordet som er knyttet til den wallet.


![33](assets/en/33.webp)


3. I Sparrows grensesnitt klikker du på fanen `Receive` på venstre side av grensesnittet.


![34](assets/en/34.webp)


4. En adresse sammen med en QR-kode vises øverst. Du kan kopiere og lime inn adressen eller skanne QR-koden med wallet som du skal bruke til å sende bitcoin til Sparrow Wallet. Du kan eventuelt skrive inn en etikett for bitcoinene du mottar.


![35](assets/en/35.webp)


5. Etter at du har sendt bitcoins, klikker du på `Transaksjoner`-fanen på venstre side av grensesnittet i Sparrow. Du vil se en ny oppføring øverst i transaksjonshistorikken, som tilsvarer transaksjonen du nettopp foretok.


![36](assets/en/36.webp)


6. Du kan også navigere på `UTXOs`-fanen på venstre side av grensesnittet for å se bitcoinene du nettopp har mottatt.


![37](assets/en/37.webp)


## Sende bitcoin


I motsetning til å motta bitcoins, krever bruk av bitcoins tilknyttet Cold-kortet ditt at du bruker Cold-kortet til å signere transaksjonene. Fremgangsmåten for å sende bitcoins med Mk4 er som følger:


1. Sett MicroSD-kortet inn i enheten der Sparrow Wallet er installert.

2. Åpne Sparrow Wallet.

3. Velg `Åpne Wallet` > Velg wallet-filen du vil bruke til å sende bitcoins med > Skriv inn passordet som er knyttet til den wallet.


![38](assets/en/38.webp)


4. I Sparrows grensesnitt klikker du på fanen `Send` på venstre side av grensesnittet.


![39](assets/en/39.webp)


5. I fanen "Betal til" skriver du inn adressen du vil sende bitcoinsene til.

6. Legg til en etikett for transaksjonen.

7. Angi hvor mange bitcoins du vil sende.

8. Angi gebyret ved å veksle mellom `Range` eller skriv inn et tall direkte i `Fee`-delen.


![40](assets/en/40.webp)


9. Klikk på "Opprett transaksjon" nederst i høyre hjørne.


![41](assets/en/41.webp)


10. Du får opp en ny transaksjonsfane som heter det samme som etiketten du skrev inn i trinn 6. Klikk på "Fullfør transaksjon for signering".


![42](assets/en/42.webp)


11. Klikk på `Lagre transaksjon` og lagre transaksjonen på MicroSD-kortet. Gi filen et nytt navn om nødvendig. Dette trinnet lagrer transaksjonen som en PSBT-fil.


![43](assets/en/43.webp)


12. Ta ut MicroSD-kortet og sett det inn i Coldcard Mk4.

13. Slå på Mk4 ved å koble den til en strømkilde.

14. Tast inn PIN-koden din.

15. Gå til `Passphrase` og skriv inn passphrase for wallet som du vil bruke til å sende bitcoins med. Hvis du vil bruke wallet med den tomme passphrase, hopper du over dette trinnet.

16. Kontroller at hovednøkkelens fingeravtrykk er det samme som på din Sparrow Wallet. Du kan sjekke dette på Sparrow Wallets `Innstillinger`-fane på venstre side av grensesnittet. Trykk deretter på `✓` på din Mk4 for å fortsette. Dette tar deg til hovedmenyen.

17. På Mk4s hovedmeny velger du "Klar til å signere". Skjermen vil vise en melding om at du er klar til å sende. Kontroller at beløpet du vil sende i bitcoins og mottakeradressen er korrekt. Trykk på "✓" for å bekrefte eller "✕" for å avbryte.

18. Hvis det finnes flere PSBT-filer å velge mellom, vil Mk4 vise meldingen "Velg PSBT-fil som skal signeres". Trykk på `✓` for å fortsette. Velg deretter PSBT-filen du vil signere ved å navigere nedover eller oppover. Utfør trinn 17 på den aktuelle transaksjonen.


![44](assets/en/44.webp)


19. Mk4 vil nå vise meldingen `PSBT Signed` sammen med navnet på filen med den signerte PSBT. Trykk på `✓` for å fortsette.

20. Ta ut MicroSD-kortet fra Cold-kortet og sett det inn i enheten der Sparrow Wallet er installert.

21. På Sparrow Wallet klikker du på `Last inn transaksjon`.


![45](assets/en/45.webp)


22. Velg filen med samme navn som den som ble opprettet i trinn 19.


![46](assets/en/46.webp)


23. Klikk på "Send transaksjon".


![47](assets/en/47.webp)


24. Transaksjonen din har blitt sendt, og den er under behandling. Du kan gå til fanen `Transaksjoner` for å se status for bekreftelse av transaksjonen.


![48](assets/en/48.webp)


## Oppgradering av fastvare


### Kontrollere fastvareversjonen din


Coldcard Mk4s fastvare kan alltid oppgraderes til en nyere versjon. Utfør følgende trinn for å kontrollere om Mk4 er oppgradert til den nyeste versjonen eller ikke:

1. Slå på Mk4 ved å koble den til en strømkilde.

2. Tast inn PIN-koden din.

3. Gå til Avansert/Verktøy > Velg Oppgrader fastvare > Velg Vis versjon.


![49](assets/en/49.webp)


Sjekk versjonen som vises på Mk4-skjermen mot versjonen på [Coinkites nettsted] (https://coldcard.com/downloads). Hvis versjonen er forskjellig, kan du oppgradere fastvaren til den nyere versjonen.


![50](assets/en/50.webp)


### Oppgradering av fastvaren


Hvis du vil oppgradere fastvaren til den nyeste versjonen, gjør du følgende:


1. Sett MicroSD-kortet inn i den bærbare datamaskinen/PC-en.

2. Gå til [Coinkites nettsted] (https://coldcard.com/downloads) og last ned den nyeste fastvaren til MicroSD-kortet ditt (den røde knappen til høyre for Mk4-bildet med versjonsnummeret på).


![51](assets/en/51.webp)


Du kan også laste ned andre versjoner ved å klikke på `All Files on Mk4` og utforske den versjonen du vil laste ned. Den nedlastede filen vil være i `.dfu`-format.


![52](assets/en/52.webp)


3. Ta ut MicroSD-kortet, og sett det inn i Mk4.

4. Slå på Mk4 ved å koble den til en strømkilde.

5. Tast inn PIN-koden din.

6. Gå til "Avansert/Verktøy" > Velg "Oppgrader fastvare" > Velg "Fra MicroSD" > Bla nedover mens du leser instruksjonene, og trykk deretter på "✓".


![53](assets/en/53.webp)


7. Velg filen `.dfu` som du lastet ned i trinn 2.

8. Coldcard Mk4 vil vise en melding om å installere denne nye fastvaren. Bla nedover mens du leser instruksjonene, og trykk deretter på `✓`.


![54](assets/en/54.webp)


9. Vent til Mk4 er ferdig med å installere den nye fastvaren. Ikke koble fra strømkilden under installasjonen.

10. Når du er ferdig, vil Mk4 starte seg selv på nytt. Du kan taste inn PIN-koden din og utføre trinnene i "Checking your Firmware Version" for å kontrollere om fastvaren har blitt oppgradert eller ikke.


## Avanserte funksjoner


### Endre PIN-koden din


Hvis du vil endre PIN-koden for pålogging, gjør du følgende:


1. Finn frem en penn og et stykke papir.

2. Slå på Mk4 ved å koble den til en strømkilde.

3. Tast inn PIN-koden din.

4. Gå til `Innstillinger` > Velg `Påloggingsinnstillinger` > Velg `Endre hoved-PIN`

5. Naviger nedover mens du leser meldingen, og trykk deretter på `✓` for å fortsette.


![55](assets/en/55.webp)


6. Skriv inn den gamle PIN-koden din.

7. Skriv inn det nye PIN-prefikset (må være mellom 2 og 6 tegn langt), og skriv det ned.

8. Mk4 vil nå vise to nye anti-phishing-ord, skriv dem ned, og trykk deretter på `✓` for å fortsette.

9. Skriv inn den nye PIN-koden (eller resten av PIN-koden, må være mellom 2 og 6 tegn lang) og skriv den ned.


![56](assets/en/56.webp)


10. Skriv inn det nye PIN-prefikset på nytt.

11. Sjekk om anti-phishing-ordene stemmer overens med det du skrev i trinn 8.

12. Skriv inn den nye PIN-koden (eller resten av PIN-koden) på nytt.


![57](assets/en/57.webp)


13. PIN-koden din har blitt endret.


### PIN-koder for triks - Legg til nytt triks


En Trick PIN-kode er en alternativ PIN-kode som er forskjellig fra den du bruker for å konfigurere Coldcard Mk4 for aller første gang. Når du slår på Mk4, kan du taste inn Trick-PIN-koden(e) i stedet for hoved-PIN-koden for å utløse visse handlinger. For å konfigurere lure-PIN-koden i Mk4, kan du gjøre følgende:


1. Finn frem en penn og et stykke papir.

2. Slå på Mk4 ved å koble den til en strømkilde.

3. Tast inn PIN-koden din.

4. Gå til `Innstillinger` > Velg `Påloggingsinnstillinger` > Velg `Trick PIN-koder` > Velg `Legg til nytt triks`.


![58](assets/en/58.webp)


5. Skriv inn PIN-kodeprefikset ditt (må være mellom 2 og 6 tegn langt) og skriv det ned.

6. Mk4 vil nå vise to nye anti-phishing-ord, skriv dem ned, og trykk deretter på `✓` for å fortsette.

7. Skriv inn PIN-koden din (eller resten av PIN-koden, må være mellom 2 og 6 tegn lang), og skriv den ned.


![59](assets/en/59.webp)


8. Naviger nedover eller oppover for å velge handlingen du vil koble til PIN-koden du nettopp har opprettet. Listen over handlinger er:


    - når `Brick Self` er valgt, vil Mk4s brikker bli ødelagt etter at PIN-koden er tastet inn, noe som gjør Mk4 ubrukelig permanent.
    - `Wipe Seed`, kan du velge mellom følgende handlinger:
      - `Slett og start på nytt`: seed slettes, og Cold-kortet starter på nytt etter at PIN-koden er tastet inn.
      - `Silent Wipe`: seed slettes lydløst, men Cold-kortet vil oppføre seg som om PIN-koden ble tastet inn feil.
      - `Wipe -> Wallet`: seed slettes lydløst, og Cold-kortet tar deg inn i en tvangsmessig wallet.
    - `Tvang Wallet`, når dette er valgt, vil din Mk4 føre til en tvang wallet etter at PIN-koden er tastet inn.
    - `Login Countdown`, kan du velge mellom følgende handlinger:
      - `Slett og nedtelling`: seed slettes umiddelbart, og Mk4 begynner å vise en nedtelling.
      - `Nedtelling og murstein`: Nedtellingen begynner, og Mk4 murer seg selv når tiden er ute.
      - "Bare nedtelling": Mk4 starter nedtellingen og starter seg selv på nytt når tiden er ute.
    - når `Look Blank` er valgt, etter at PIN-koden er tastet inn, vil Cold-kortet oppføre seg som om seedphrase er slettet, men den er faktisk fortsatt i minnet.
    - `Just Reboot`, når dette er valgt, vil Coldcard starte seg selv på nytt etter at PIN-koden er tastet inn.
    - denne avanserte funksjonen er ment for erfarne brukere og er utviklet for å beskytte mot alvorlige trusler, som for eksempel tvang fra noen med innsidekunnskap. Når Delta-modus er aktivert, ser COLDCARD ut til å åpne den ekte wallet, slik at angriperen kan bla gjennom og bekrefte at den ser ekte ut. Den blokkerer imidlertid all transaksjonssignering i hemmelighet, slik at ingen bitcoin kan sendes. Den deaktiverer også tilgangen til seed-frasen, og ethvert forsøk på å vise den vil slette den fullstendig. For å få den falske wallet til å se mer overbevisende ut, må Trick PIN-koden som brukes for Delta-modus starte med de samme tallene som den ekte PIN-koden (slik at den viser de samme anti-phishing-ordene), men slutte annerledes.
    - `Policy Unlock`, når dette er valgt, vil Single Signer Spending Policy (SSSP) bli deaktivert etter at PIN-koden er tastet inn.
    - `Policy Unlock & Wipe`, når den er valgt, later den til å deaktivere SSSP, men den vil slette seedphrase i prosessen.

9. Etter at du har valgt handlingen du vil koble sammen med lure-PIN-koden, bekrefter du valget ved å trykke på `✓`. Triks-PIN-koden din er konfigurert.

10. I `Innstillinger` > `Påloggingsinnstillinger` > `Trick-PIN-koder` kan du se listen over trick-PIN-koder du har opprettet, og handlingene som er knyttet til dem. Du kan velge å konfigurere PIN-kodene og handlingene som er knyttet til dem på nytt. Du kan også skjule eller slette den ved å velge PIN-koden og deretter velge "Skjul triks" eller "Slett triks".


![60](assets/en/60.webp)


### Trick PIN-koder - Legg til hvis feil


Alternativt kan du legge til en "Legg til hvis feil" -handling som utløses etter at feil PIN-kode er tastet inn et visst antall ganger. Du kan konfigurere dette ved å utføre følgende trinn:


1. Slå på Mk4 ved å koble den til en strømkilde.

2. Tast inn PIN-koden din.

3. Gå til `Innstillinger` > Velg `Påloggingsinnstillinger` > Velg `Trick PIN-koder` > Velg `Legg til hvis feil`.


![61](assets/en/61.webp)


4. Mk4 vil vise en melding om denne innstillingen. Naviger nedover mens du leser gjennom forklaringen, og trykk deretter på `✓` for å fortsette.

5. Angi antall feilforsøk som kreves for å utløse handlingen. Merk: Maksimalt antall forsøk er `12`. Dette er fordi Mk4 er konstruert slik at når feil PIN-kode tastes inn `13` ganger, vil enheten mure seg selv, slik at den blir permanent ubrukelig. Etter at du har tastet inn nummeret, trykker du på `✓` for å fortsette.

6. Naviger opp eller ned for å velge handling. De tilgjengelige handlingene er som følger:


   - `Wipe, Stop`: seedphrase slettes, og enheten viser "Seed is wiped, Stop"
   - `Wipe & Reboot`: seedphrase slettes, og enheten starter på nytt uten noen melding.
   - `Stilt sletting`: seedphrase slettes stille, og enheten oppfører seg som et forsøk på å slette feil PIN-kode (ingen åpenbar slettingsmelding).
   - `Brick Self`: Enheten er permanent deaktivert og viser bare "Bricked"
   - siste sjanse: seedphrase slettes, men du får et siste forsøk på å taste feil PIN-kode; tast inn feil PIN-kode igjen, og enheten vil bli ødelagt.
   - "Bare start på nytt": Enheten starter ganske enkelt på nytt uten at noe annet endres.

Velg handlingen du vil bruke, og trykk på `✓` for å fortsette


![62](assets/en/62.webp)


7. Du kommer tilbake til katalogen `Innstillinger > Påloggingsinnstillinger > Trick PINs`. Under `Trick PINs:` finner du listen over trick-pins sammen med handlingen `FALSK PIN`. Du kan også skjule eller slette den ved å velge PIN-koden og deretter velge "Skjul triks" eller "Slett triks".


![63](assets/en/63.webp)



## Konklusjon


Denne veiledningen viser hvordan du setter opp Mk4, hvordan du gjennomfører Bitcoin-transaksjoner med Mk4 og hvordan du bruker noen avanserte funksjoner i Mk4. Mk4 tilbyr sikre og fleksible måter å lagre og administrere bitcoins på. Utformingen sørger for at private nøkler aldri forlater enheten, mens funksjoner som passphrase, lure-PIN-koder og luftgapede transaksjoner gir brukerne full kontroll over sikkerhetsoppsettet. Den kan sammenkobles med Sparrow Wallet for en brukervennlig opplevelse av å opprette, signere og administrere Bitcoin-transaksjoner uten at det går på bekostning av personvern eller sikkerhet.


Hvis du ønsker å utforske andre funksjoner, kan du sjekke dokumentasjonen på Coinkites nettsted [her] (https://coldcard.com/docs/). Jeg håper du finner denne veiledningen nyttig når du bruker Coldcard Mk4. Takk og på gjensyn neste gang!