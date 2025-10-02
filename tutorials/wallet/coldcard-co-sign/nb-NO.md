---
name: COLDCARD - Co-Sign
description: Oppdag Co-Sign-funksjonen og bruk den på COLDCARD
---

![cover](assets/cover.webp)


*NB: Denne veiledningen er rettet mot personer som allerede har litt erfaring med multisignaturlommebøker, Coinkite-enheter og programvare som Sparrow wallet eller Nunchuk.*



![video](https://youtu.be/MjMPDUWWegw)




**Hvorfor ColdCard Co-Sign?



Med denne funksjonen kan du legge til **utgiftsbetingelser** på ColdCard-enheten (Q eller Mk4) på samme måte som en maskinvaresikkerhetsmodul (HSM), slik at du kan beskytte pengene dine samtidig som du beholder betydelig fleksibilitet og kontroll over dem.



Utgiftsbetingelser kan for eksempel være:





- Begrensninger på størrelsesorden**: Sett et tak på hvor mange bitcoins du kan bruke i én enkelt transaksjon.
- Hastighetsgrenser:** bestemmer hvor mange transaksjoner du kan utføre per tidsenhet (per time, dag, uke osv.), og krever et minimum antall blokker mellom dem.
- Forhåndsgodkjente adresser:** Tillat kun at bitcoins sendes til forhåndsgodkjente adresser.
- Tofaktorautentisering:** Krever bekreftelse fra en tredjeparts 2FA-mobilapplikasjon (TOTP [RFC 6238] (https://www.rfc-editor.org/rfc/rfc6238)) på en NFC-aktivert smarttelefon/nettbrett med internettilgang.



**Hvordan det fungerer



Ved å legge til en ekstra seed til ColdCard Mk4- eller Q-enheten, kalt "Spending Policy Key", som vi i denne veiledningen vil referere til som "C Key".


I tillegg til denne ekstra seed vil du bli bedt om å Supply minst én ekstra nøkkel (XPUB), som vi kaller en "Backup Key", for å kunne opprette en Wallet Multisig 2-on-N.



Kort oppsummert skal vi opprette en Wallet Multisig, og ColdCard-enheten din vil inneholde to av de private nøklene som trengs for å bruke pengene, enhetens seed-master og "Spending Policy Key".



Hver gang "C Key" blir bedt om å signere, gjelder de angitte utgiftsvilkårene, og ColdCard signerer bare hvis transaksjonen oppfyller dem.



Hvis du ønsker å fravike disse utgiftsvilkårene, kan du gjøre det:




- ved å signere med en av reservetastene og seed-hånden, eller 2 reservetaster avhengig av størrelsen på Multisig.
- ved å angi "Utgiftspolitikknøkkelen" eller "C-nøkkelen" i menyen "Co-Sign". **Sistnevnte kan ikke brukes direkte på enheten, ellers kan hvem som helst avbryte de innstilte utgiftsbetingelsene




## Konfigurere ColdCard Co-Sign



![video](https://youtu.be/MjMPDUWWegw)



### 1- Aktiver funksjonalitet



Først og fremst må du sørge for at enheten din har minst den nyeste fastvareversjonen:




- Mk4: v5.4.2
- Q: v1.3.2Q




På Mk4 eller ColdCardQ går du til *Avanserte verktøy > ColdCard Co-Signing*.



![Co-Sign](assets/fr/01.webp)



*I den følgende veiledningen vil skjermbilder bli tatt på en ColdCardQ for enkelhets skyld, men trinnene og menyene er identiske mellom Mk4 og Q.*



En oppsummering av funksjonaliteten vises.


Terminologien som brukes for å betegne nøklene, og som vi kommer til å bruke igjen i 2-på-3-multisignatur-Wallet som vi nå skal lage, er



Nøkkel A = Coldcard master seed


Nøkkel B = Backup-nøkkel


Nøkkel C = Nøkkel for utgiftspolitikk



Klikk på **"ENTER"**.



![Co-Sign](assets/fr/02.webp)



Neste trinn er å bestemme hvilken privat nøkkel som skal fungere som "Spending Policy Key" eller "Key C".



Vi ser at vi har flere muligheter:





- Eller trykk **"ENTER"** for å generate en ny seed setning på 12 ord.





- Klikk enten på **"(1)"** for å importere en eksisterende 12-ords seed, eller velg **"(2)"** for å importere en eksisterende 24-ords seed.





- Eller trykk **"(6)"** for å importere en seed fra enhetens hvelv.



I denne veiledningen har vi valgt å importere en eksisterende 12-ords seed ved å trykke **"(1)"**. Dette kan være en hvilken som helst seed BIP39 du allerede eier, og som du selvsagt har en sikkerhetskopi av.



Bruk tastaturet til å skrive inn de 12 ordene i seed. I dette eksemplet velger vi seeds gyldige frase biff x 12. Trykk deretter på **"ENTER"**.


*NB: Hvis du ikke har en sikkerhetskopi av denne seed, vil du ikke lenger kunne endre "Co-Sign"-innstillingene på enheten din for å endre utgiftsbetingelsene dine*



Funksjonen "Co-Sign" er nå aktivert på enheten. Nå må vi velge våre utgiftsbetingelser, og deretter fullføre opprettelsen av multisignatur Wallet.



![Co-Sign](assets/fr/03.webp)



### 2- Velg utgiftsbetingelser eller "*utgiftspolitikk*"



Her angir vi hvilke utgiftsvilkår som må oppfylles når **"C-nøkkelen"** eller **"Spending Policy Key**" signerer en transaksjon.



I menyen **"Medsignering"** klikker du på **"Utgiftspolitikk**".



Du kan deretter velge maksimal størrelse, dvs. det maksimale antallet satoshier som kan brukes i én enkelt transaksjon.



I dette eksemplet velger vi en maksimal magnitude på **21212** satoshis. Klikk på **"ENTER"** for å bekrefte.




![Co-Sign](assets/fr/04.webp)



Deretter velger vi å angi maksimal hastighet, dvs. hvor mange transaksjoner enheten skal kunne signere per tidsenhet. I denne veiledningen velger vi ubegrenset hastighet, dvs. ingen begrensning på antall transaksjoner.




![Co-Sign](assets/fr/05.webp)



### 3- Opprett Wallet Multisig 2-på-N



Vi må fortsatt velge den tredje nøkkelen for vår Wallet Multisig, dvs. **"Backup Key"** (nøkkel B), i tillegg til enhetens **master seed** (nøkkel A) og **"Spending Policy Key"** (nøkkel C).



Vår "B-nøkkel" må importeres enten via SD-kort, eller via QR-kode når det gjelder ColdCardQ.


For å gjøre dette trenger vi en annen ColdCard Mk4- eller Q-enhet, som vi bruker "Key B" på.



På den andre enheten som inneholder **"Backup Key"**, for eksempel et ColdCard Mk4 i dette eksemplet, går du fra hovedmenyen til **"Settings"**, deretter **"Multisig Wallet"**, og til slutt **"Export Xpub"**.


(Hvis den andre enheten din er en ColdCardQ, har du selvfølgelig mulighet til å eksportere Xpub via QR-kode).





![Co-Sign](assets/fr/06.webp)





På neste skjermbilde setter du inn et SD-kort og klikker på **"valider"**-knappen nederst til høyre. Klikk deretter på **"(1)"** for å lagre filen på SD-kortet.



Filen vil inneholde fingeravtrykket til den offentlige nøkkelen (*fingeravtrykk*) i navnet, og vil ha formen `ccxp-0F056943.json`.




![Co-Sign](assets/fr/07.webp)



Sett deretter SD-kortet inn i den "opprinnelige" ColdCardQ for å importere vår "Backup Key" (nøkkel B).


I menyen "ColdCard Co-Signing" velger du "Build 2-of-N", og på neste skjermbilde klikker du på **"ENTER"**, og deretter igjen **"ENTER"** for å importere "Backup Key" fra SD-kortet.



![Co-Sign](assets/fr/08.webp)



På neste skjermbilde lar du "Account Number" stå tomt (med mindre du vet nøyaktig hva du gjør) og klikker **"ENTER"** igjen.



![Co-Sign](assets/fr/09.webp)



Endelig er vi klare til å ta i bruk vår nye Wallet Multisig 2-sur-3, som er satt sammen på følgende måte:



Nøkkel A= Coldcard Q master seed


Nøkkel B= Backup-nøkkel (nettopp importert fra en annen Coldcard-enhet)


Nøkkel C= Utgiftspolitikknøkkel (hvis den brukes til å signere, pålegger forhåndsdefinerte utgiftsbetingelser)



## Signer sammen med Sparrow wallet



Hvis det er nødvendig, kan du se veiledningene nedenfor for å gjøre deg kjent med Sparrow wallet-programvaren:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

https://planb.network/tutorials/wallet/desktop/sparrow-multisig-5860333b-6dd8-4aaa-8ab6-89ebc6276f1f

### 1- Eksport Wallet Multisig 2-sur-3 til Sparrow wallet



Vi må nå eksportere Wallet Multisig til Sparrow, slik at vi kan plassere de første satoshiene våre der.



Fra hovedmenyen på ColdCardQ velger du **"Innstillinger"** og deretter **"Multisig lommebøker"**.


Settet med Multisig-lommebøker som er kjent for ColdCard vises nå, med antall involverte nøkler her "2/3" (2-sur3). Velg Multisig **"ColdCard Co-Sign"** som vi nettopp har opprettet, og klikk deretter på **"ColdCard Export"**.



![Co-Sign](assets/fr/10.webp)




Til slutt velger du metoden som lar deg eksportere Wallet til Sparrow. I vårt tilfelle velger vi SD-kort, og klikker på **"(1)"** etter å ha satt inn et SD-kort i spor A på enheten.



![Co-Sign](assets/fr/11.webp)



Velg deretter "Importer Wallet" i Sparrow wallet.



![Co-Sign](assets/fr/12.webp)



Klikk deretter på **"Import File"**. Velg deretter filen **"export-Coldcard_Co-sign.txt"** på SD-kortet ditt.



![Co-Sign](assets/fr/13.webp)



Gi Wallet et navn slik det vil vises i Sparrow, og velg et passord for å kryptere Wallet (eller ikke).



![Co-Sign](assets/fr/14.webp)



![Co-Sign](assets/fr/15.webp)



Vi er nå klare til å motta de første satoshiene våre og teste utgiftsbetingelsene vi har lagt inn i Wallet.



![Co-Sign](assets/fr/16.webp)



### 2- Testing av forhåndsdefinerte utgiftsretningslinjer



Som en påminnelse hadde vi bestemt oss for en maksimal størrelse på 21212 satoshier for vår Wallet Multisig. Dette betydde at hver gang den utgiftspolitiske nøkkelen (nøkkel C) signerte en transaksjon, ville transaksjonen bare være gyldig hvis beløpet som ble brukt var mindre enn eller lik 21212 satoshier.



La oss teste det.


La oss først klikke på "Receive"-fanen i Sparrow og slippe noen Satss på Wallet, som vi skal bruke gjennom hele denne opplæringen.



![Co-Sign](assets/fr/17.webp)



![Co-Sign](assets/fr/18.webp)



La oss deretter prøve å bruke mer enn de 21212 tillatte satoshiene ved å simulere en transaksjon på 50 000 Sats.



![Co-Sign](assets/fr/19.webp)



![Co-Sign](assets/fr/20.webp)



![Co-Sign](assets/fr/21.webp)



![Co-Sign](assets/fr/22.webp)



Etter å ha skannet QR-koden som representerer den *usignerte* transaksjonen med ColdCardQ for å importere transaksjonen, ser vi dette på skjermen. En advarsel forteller oss at vilkårene for å bruke penger ikke er oppfylt. Hvis vi likevel signerer transaksjonen, vil bare én av de to nøklene (seed-masternøkkelen på enheten, men ikke "Key C") signere.




![Co-Sign](assets/fr/23.webp)



Her, etter å ha importert transaksjonen vår til Sparrow, kan vi se at bare én av signaturene har blitt brukt på transaksjonen.



![Co-Sign](assets/fr/24.webp)




La oss nå gjenta eksperimentet, men for en transaksjon på 21 000 satoshier, dvs. mindre enn den maksimale størrelsen (21212 Sats) vi satte for denne Wallet.




![Co-Sign](assets/fr/25.webp)



![Co-Sign](assets/fr/26.webp)



![Co-Sign](assets/fr/27.webp)



![Co-Sign](assets/fr/28.webp)



La oss prøve å signere denne transaksjonen med ColdCardQ.



Ingen problemer denne gangen, ingen advarsel vises, og når vi importerer den signerte transaksjonen til Sparrow wallet, har de to signaturene denne gangen blitt brukt, noe som gjør transaksjonen gyldig og klar for distribusjon.




![Co-Sign](assets/fr/29.webp)




![Co-Sign](assets/fr/30.webp)






## Signer sammen med Nunchuk



https://planb.network/tutorials/wallet/mobile/nunchuk-6cbcb406-ec84-478f-afac-bb4da366a6fa

### 1- Web 2FA og hvitelistede adresser



I dette avsnittet bruker vi Wallet Multisig Co-Sign med Nunchuk, og benytter anledningen til å bruke nye utgiftsbetingelser for å se hvordan det går.



Gå til *Avanserte verktøy > ColdCard Co-Signing*.


Vi blir bedt om å taste inn vår "Spending Policy Key" for å få tilgang til menyen der vi kan endre utgiftsbetingelsene. I vårt tilfelle skriver vi inn 12 x "biff".



Vi har bestemt oss for å beholde en størrelse på 21212 Sats, og en maksimal "Limit Velocity" av praktiske årsaker knyttet til denne opplæringen. På den annen side kommer vi til å bruke menyen **"Whitelist Addresses"** til å bestemme hvilke adresser vi kan bruke pengene våre på.




![Co-Sign](assets/fr/31.webp)




Skann QR-kodene som er knyttet til adressene (vi velger 2) du ønsker å legge til i hvitelisten din, og klikk deretter på **"ENTER"**. Etter at du har validert adressene dine ved å trykke **"ENTER"** flere ganger, ser vi at det er lagt inn begrensninger på Magnitude- og mottakeradresser.



![Co-Sign](assets/fr/32.webp)



For å få et fullstendig bilde av mulighetene som "Co-Sign" gir, aktiverer vi til slutt alternativet "Web 2FA".


Med denne funksjonen kan du bruke et TOTP RFC-6238-kompatibelt program, for eksempel Google Authenticator / Ente Auth / Proton Authenticator / Authy 2FA / eller Aegis Authenticator, for å legge til en ekstra Layer av sikkerhet.



https://planb.network/tutorials/computer-security/authentication/ente-auth-1928e65a-3b43-40f3-9efd-457ee2d79bb9

https://planb.network/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.network/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc

Helt konkret må du, før du signerer en transaksjon, bringe den NFC-aktiverte, internettilkoblede enheten din i nærheten av Coldcard. Da kommer du automatisk til en nettside på coldcard.com, der du blir bedt om å taste inn den sekssifrede koden for søknaden din. Hvis du skriver inn riktig kode, vil nettsiden vise deg enten en QR-kode som du kan skanne for ColdCardQ, eller en 8-sifret kode som du kan skrive inn på Mk4-enheten din for å autorisere enheten din til å signere.





![Co-Sign](assets/fr/33.webp)



Etter at du har skannet QR-koden som vises i programmet for dobbel autentisering, og lagt til ColdCard Co-Sign (CCC)-kontoen din, blir du bedt om å bekrefte at alt er i orden ved å skrive inn 2FA-koden din.



Skriv inn ColdCard på baksiden av NFC-enheten.



![Co-Sign](assets/fr/34.webp)



På nettsiden som åpnes, skriver du inn 2FA-koden til favorittprogrammet ditt. Skann deretter QR-koden som vises med ColdCardQ (eller skriv inn den 8-sifrede koden som vises i Mk4).



![Co-Sign](assets/fr/35.webp)




Vi har nå innført en begrensning på størrelse (21212 Sats), destinasjonsadresser og dobbel autentisering.



![Co-Sign](assets/fr/36.webp)



### 2- Eksporter Wallet Multisig 2-mot-3 til Nunchuk



La oss eksportere Wallet Multisig 2-mot-3 til Nunchuk denne gangen, slik vi gjorde med Sparrow tidligere.


Gå til *Innstillinger > Multisig lommebøker > 2/3: ColdCard Co-sign > ColdCard Export*.



![Co-Sign](assets/fr/10.webp)



Denne gangen velger du NFC-alternativet for eksport ved å klikke på ColdcardQ-knappen med samme navn **"NFC"**.



![Co-Sign](assets/fr/37.webp)



Hvis du åpner programmet for første gang i Nunchuk, klikker du på **"Gjenopprett eksisterende Wallet"**.



![Co-Sign](assets/fr/38.webp)



Hvis du allerede har en Wallet i programmet, klikker du på **"+"** øverst til høyre og deretter på **"Gjenopprett eksisterende Wallet"**.



![Co-Sign](assets/fr/39.webp)




Velg deretter **"Gjenopprett Wallet fra COLDCARD"** og deretter **"Multisig Wallet"**.



![Co-Sign](assets/fr/40.webp)



Til slutt trykker du baksiden av smarttelefonen din mot skjermen på ColdCardQ for å importere Wallet via NFC.



![Co-Sign](assets/fr/41.webp)



Kontoen vår og satoshiene som tidligere ble satt inn via Sparrow wallet, er tilbake.



![Co-Sign](assets/fr/42.webp)



### 3- Testing av forhåndsdefinerte utgiftsretningslinjer



La oss nå prøve å foreta en transaksjon som bryter med de to utgiftsvilkårene vi har satt. **Vi prøver å bruke mer enn 21212 Sats til en Address som ikke har blitt godkjent, og vi prøver å sende 22 222 Sats til en tilfeldig Address.



![Co-Sign](assets/fr/43.webp)



Når transaksjonen er opprettet, klikker du på de tre små prikkene øverst i høyre hjørne for å eksportere den til ColdCard.



![Co-Sign](assets/fr/44.webp)



Velg deretter **"Eksporter via BBQR"**, og skann QR-koden som vises med ColdCardQ.



![Co-Sign](assets/fr/45.webp)



ColdcardQ viser deretter en advarsel som, når du blar til bunnen av skjermen, tydeliggjør at transaksjonen bryter med utgiftsvilkårene, som forventet.



**Merk at enheten ikke forteller oss hvilke utgiftsbetingelser som er involvert, for å forhindre at en potensiell angriper prøver å omgå restriksjonene




![Co-Sign](assets/fr/46.webp)



Hvis du fortsatt validerer ved å trykke **"ENTER"**, vises QR-koden som representerer den signerte transaksjonen. Hvis du importerer den på Nunchuk, kan du se at bare én signatur har blitt brukt.



![Co-Sign](assets/fr/47.webp)



![Co-Sign](assets/fr/48.webp)






La oss utføre nøyaktig samme operasjon, men denne gangen med en transaksjon som respekterer størrelsesgrensen (21212 Sats), og bruker satoshiene til en av de to adressene vi har forhåndskonfigurert.



Vi sender Nunchuk 12121 Sats til en av våre to adresser. Deretter eksporterer vi transaksjonen til ColdCard som tidligere gjort.



![Co-Sign](assets/fr/49.webp)




Etter å ha importert den usignerte transaksjonen til ColdCardQ, la oss se hva vi får se denne gangen.



En advarsel er alltid til stede, men denne gangen, når vi blar til bunnen av skjermen, ser vi at det handler om å validere transaksjonen via 2FA. Enheten ber oss om å holde ColdcardQ i nærheten av vår Internett-tilkoblede NFC-terminal (smarttelefon eller nettbrett), noe vi gjør.



![Co-Sign](assets/fr/50.webp)



En nettside åpnes på smarttelefonen vår, der vi blir bedt om å oppgi 2FA-koden vår, noe vi gjør takket være Proton Authenticator.



![Co-Sign](assets/fr/51.webp)





Skann deretter QR-koden som vises på nettsiden, for å autorisere ColdCard til å signere transaksjonen.


Transaksjonen er nå signert av de to nøklene og er derfor gyldig.



Hvis "Push Tx" er aktivert på ColdCardQ, kan du sende transaksjonen direkte til nettverket med et enkelt trykk på baksiden av smarttelefonen.



![Co-Sign](assets/fr/52.webp)




Hvis du ikke har "Push tx" aktivert, kan du trykke på "QR"-knappen på ColdCardQ for å vise den signerte transaksjonen som en QR-kode, og importere den til Nunchuk på samme måte som i det forrige eksemplet.



![Co-Sign](assets/fr/53.webp)



Denne gangen ser vi at to signaturer er brukt, så transaksjonen er klar til å sendes ut i Bitcoin-nettverket.



![Co-Sign](assets/fr/54.webp)




Vi har kommet til slutten av denne veiledningen, som vil gi deg en oversikt over mulighetene som ligger i Co-Sign-funksjonaliteten som er integrert i Coinkites ColdCardQ- og Mk4-enheter, samt bruken av den gjennom lommebøker som Sparrow og Nunchuk.