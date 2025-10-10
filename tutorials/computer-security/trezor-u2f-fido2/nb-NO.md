---
name: "Trezor U2F & FIDO2"
description: Styrk sikkerheten på nettet med Trezor
---
![cover](assets/cover.webp)



Trezor-enheter er maskinvarelommebøker som opprinnelig ble utviklet for å sikre en Bitcoin Wallet, men de har også avanserte alternativer for sterk autentisering på nettet. Takket være kompatibiliteten med **U2F**- og **FIDO2**-protokollene gjør de det mulig å sikre tilgangen til nettkontoene dine uten å være avhengig av passord alene.



U2F-protokollen (*Universal 2nd Factor*) ble introdusert av Google og Yubico i 2014, og ble deretter standardisert av FIDO Alliance. Den gjør det mulig å legge til en ekstra fysisk autentiseringsfaktor (2FA) ved innlogging. Når den er aktivert, må brukerne, i tillegg til det klassiske passordet, godkjenne hvert forsøk på å koble seg til kontoen sin ved å trykke på en knapp på Trezor. I denne sammenhengen fungerer Trezor på samme måte som en Yubikey.



Denne metoden er basert på asymmetrisk kryptografi: Ingen hemmelige data overføres, noe som gjør phishing- eller avlyttingsangrep ineffektivt. U2F støttes nå av mange nettbaserte tjenester.



I tillegg til U2F, som muliggjør tofaktorautentisering, støtter Trezors også FIDO2 (*Fast IDentity Online 2.0*), som er en videreutvikling av U2F. Dette er en standardisert autentiseringsprotokoll fra 2018, som utvider logikken til U2F og tar sikte på å erstatte passord fullstendig. Den er basert på to komponenter: *WebAuthn* (nettleserens side) og *CTAP2* (den fysiske nøkkelens side). FIDO2 muliggjør "passordløs" autentisering: Brukerne identifiserer seg utelukkende via Trezor-enheten sin, som fungerer som et unikt kryptografisk token, uten noe ekstra passord. Denne protokollen er nå kompatibel med en rekke nettbaserte tjenester, særlig de som er rettet mot bedrifter.



I tillegg til "passordløs"-funksjonalitet muliggjør FIDO2 også tofaktorautentisering på samme måte som U2F.



FIDO2 introduserer også begrepet resident credentials, dvs. identifikatorer som er lagret direkte i Trezor, og som inkluderer både den private nøkkelen som muliggjør tilkobling og brukerens identifikasjonsinformasjon. Denne mekanismen muliggjør virkelig passordfri autentisering: Det er bare å koble til Trezor og bekrefte tilgangen, uten å oppgi verken ID eller passord. I motsetning til dette lagrer ikke-hjemmehørende legitimasjon, som er mer konvensjonell, bare den private nøkkelen på enheten; bruker-ID-en lagres på serversiden og må derfor oppgis ved hver tilkobling. Vi skal se på hvordan du lagrer dem med Trezor senere.



I denne veiledningen lærer du hvordan du aktiverer U2F eller FIDO2 for tofaktorautentisering, og deretter hvordan du konfigurerer FIDO2 for å få tilgang til kontoene dine uten passord, direkte med Trezor.



**U2F er kompatibel med alle Trezor-modeller, men FIDO2 støttes bare på Safe 3, Safe 5 og Model T, ikke Model One.**



## Bruke U2F/FIDO2 for 2FA på en Trezor



Før du begynner, må du sørge for at du har satt opp Bitcoin Wallet på Trezor. Det er viktig å lagre Mnemonic på riktig måte, ettersom nøklene som brukes for U2F og FIDO2 i tofaktorautentisering, er avledet fra denne Mnemonic. Hvis Trezor-enheten din går tapt eller blir skadet, kan du få tilgang til nøklene dine igjen ved å skrive inn Mnemonic-setningen på en annen Trezor-enhet (merk at for FIDO2-legitimasjon i "*passordløs*"-modus er ikke seed alene nok, som vi skal se i de neste avsnittene).



Koble Trezor til datamaskinen og lås den opp.



![Image](assets/fr/01.webp)



Gå til kontoen du vil sikre med tofaktorautentisering. Jeg kommer for eksempel til å bruke en Bitwarden-konto. Du finner vanligvis 2FA-alternativet i tjenesteinnstillingene, under fanene "*autentisering*", "*sikkerhet*", "*innlogging*" eller "*passord*".



![Image](assets/fr/02.webp)



I delen som er dedikert til tofaktorautentisering, velger du alternativet "*Passkode*" (begrepet kan variere avhengig av hvilket nettsted du bruker).



![Image](assets/fr/03.webp)



Du vil ofte bli bedt om å bekrefte ditt nåværende passord.



![Image](assets/fr/04.webp)



Gi sikkerhetsnøkkelen et navn slik at den er lett å gjenkjenne, og klikk deretter på "*Les nøkkel*".



![Image](assets/fr/05.webp)



Kontoopplysningene dine vises på Trezor-skjermen. Trykk på skjermen eller trykk på knappen for å bekrefte. Du vil også bli bedt om å bekrefte PIN-koden din.



![Image](assets/fr/06.webp)



Registrer denne sikkerhetsnøkkelen.



![Image](assets/fr/07.webp)



Fra nå av vil du bli bedt om å koble til Trezor i tillegg til det vanlige passordet ditt når du vil koble deg til kontoen din.



![Image](assets/fr/08.webp)



Deretter kan du trykke på Trezor-skjermen for å bekrefte autentiseringen.



![Image](assets/fr/09.webp)



Fordelen med å bruke en Hardware Wallet Trezor for tofaktorautentisering er at du enkelt kan gjenopprette nøklene dine takket være Mnemonic-frasen. I tillegg til denne grunnleggende sikkerhetskopien kan du også bruke en nødkode som leveres av hver tjeneste der du har aktivert 2FA. Med denne nødkoden kan du koble deg til kontoen din hvis du mister sikkerhetsnøkkelen. Den erstatter derfor 2FA for en tilkobling om nødvendig.



På Bitwarden kan du for eksempel få tilgang til denne koden ved å klikke på "*Vis gjenopprettingskode*".



![Image](assets/fr/10.webp)



Jeg anbefaler at du oppbevarer denne koden på et annet sted enn der du lagrer hovedpassordet ditt, for å forhindre at de blir stjålet sammen. Hvis passordet ditt for eksempel er lagret i en passordbehandler, bør du oppbevare 2FA-nødkoden på papir, separat.



Denne tilnærmingen gir deg to nivåer av sikkerhetskopiering i tilfelle du mister Trezor for 2FA-autentisering: en første sikkerhetskopi som bruker Mnemonic-frasen for alle kontoene dine, og en annen spesifikk sikkerhetskopi for hver konto med nødkodene. Det er imidlertid viktig **ikke å forveksle Mnemonic-frasen med nødkoden**:




- Mnemonic-frasen på 12 eller 24 ord gir deg ikke bare tilgang til nøklene som brukes til 2FA på alle kontoene dine, men også til bitcoinsene dine som er sikret med Trezor ;
- Nødkoden lar deg midlertidig omgå 2FA-forespørselen bare på den aktuelle kontoen (i dette eksempelet bare på Bitwarden).



## Bruke FIDO2 på en Trezor



I tillegg til tofaktorautentisering muliggjør FIDO2 også "passordløs" autentisering, dvs. at du ikke trenger å oppgi passord når du logger deg på et nettsted. Du trenger bare å koble Trezor til datamaskinen for å få tilgang til den sikre kontoen din på denne måten. Slik konfigurerer du denne funksjonen.



Før du begynner, må du sørge for at du har satt opp Bitcoin Wallet på Trezor. Det er viktig å lagre Mnemonic, ettersom FIDO2 "*passordløs*"-identifikatorene er kryptert med seed (vi finner ut hvordan du lagrer disse identifikatorene på riktig måte i neste avsnitt).



Koble Trezor til datamaskinen, og lås den opp.



![Image](assets/fr/01.webp)



Gå inn på kontoen du ønsker å sikre i "*passordløs*"-modus. Jeg bruker en Bitwarden-konto som eksempel. Dette alternativet finner du vanligvis i tjenesteinnstillingene, ofte under en "*autentisering*"-, "*sikkerhet*"- eller "*passord*"-fane.



På Bitwarden finner du for eksempel alternativet under fanen "*Master password*". Klikk på "*Turn on*" for å aktivere autentisering via FIDO2.



![Image](assets/fr/11.webp)



Du vil ofte bli bedt om å bekrefte passordet ditt.



![Image](assets/fr/12.webp)



Kontoopplysningene dine vises på Trezor-skjermen. Trykk på skjermen eller trykk på knappen for å bekrefte. Du må også bekrefte PIN-koden din.



![Image](assets/fr/13.webp)



Legg til et navn på nettstedet for å huske sikkerhetsnøkkelen din, og klikk deretter på "*Slå på*".



![Image](assets/fr/14.webp)



Du vil deretter bli bedt om å identifisere deg for å kontrollere at nøkkelen fungerer som den skal.



![Image](assets/fr/15.webp)



Fra nå av vil det ikke lenger være nødvendig å oppgi e-postadressen Address eller innlogging når du logger inn på kontoen din. Du trenger bare å klikke på knappen for å autentisere deg med en fysisk nøkkel i påloggingsskjemaet.



![Image](assets/fr/16.webp)



Bekreft tilkoblingen til Trezor ved å taste inn PIN-koden for Hardware Wallet.



![Image](assets/fr/17.webp)



Du vil bli koblet til kontoen din uten å måtte oppgi passordet ditt.



![Image](assets/fr/18.webp)



**Vær oppmerksom på at selv om du aktiverer "*passordløs*"-autentisering via FIDO2 på Trezor, vil hovedpassordet for nettkontoen din fortsatt være gyldig for påloggingsformål**



## Lagre FIDO2-påloggingsinformasjonen din (innbyggere)



Hvis du bruker FIDO2 eller U2F for tofaktorautentisering, dvs. for å logge inn på kontoer som krever passord i tillegg til 2FA-validering via Trezor, vil Mnemonic-frasen alene gi deg tilgang til nøklene dine. Hvis du imidlertid bruker FIDO2 i "*passordløs*"-modus som beskrevet i forrige avsnitt, må du ta en kopi av FIDO-legitimasjonen din i tillegg til å sikkerhetskopiere Mnemonic-frasen som krypterer denne legitimasjonen.



For å gjøre dette trenger du en datamaskin med Python installert. Åpne en terminal og kjør følgende kommando for å installere den nødvendige Trezor-programvaren:



```shell
pip3 install --upgrade trezor
```



Koble Trezor til datamaskinen via USB, og lås den opp ved hjelp av PIN-koden.



![Image](assets/fr/01.webp)



Kjør følgende kommando for å hente listen over FIDO2-identifikatorer som er lagret på Trezor:



```shell
trezorctl fido credentials list
```



Bekreft eksporten på Trezor.



![Image](assets/fr/19.webp)



FIDO2-påloggingsinformasjonen din vises på terminalen din. For eksempel fikk jeg denne informasjonen for Bitwarden-kontoen min:



```shell
WebAuthn credential at index 0:
Relying party ID:       vault.bitwarden.com
Relying party name:     Bitwarden
User ID:                6e315ebabc8b6945a253b1c50116538d
User name:              tutoplanbnetwork@proton.me
User display name:      PBN
Creation time:          2
hmac-secret enabled:    True
Use signature counter:  True
Algorithm:              ES256 (ECDSA w/ SHA-256)
Curve:                  P-256 (secp256r1)
Credential ID:          f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Kopier og lagre all denne informasjonen i en tekstfil. Det er ingen vesentlig risiko forbundet med denne sikkerhetskopien, annet enn at den avslører at du bruker disse tjenestene med FIDO2. "*Credential ID*" er kryptert ved hjelp av Wallets seed, noe som betyr at en angriper som får tak i denne sikkerhetskopien ikke vil kunne koble seg til kontoene dine, men bare legge merke til at du bruker disse kontoene. For å dekryptere disse ID-ene trenger du seed i din Wallet.



Du kan derfor lage flere kopier av denne tekstfilen og lagre dem på forskjellige steder, for eksempel lokalt på datamaskinen, på en filhostingstjeneste og på et eksternt medium, for eksempel en USB-pinne. Vær imidlertid oppmerksom på at denne sikkerhetskopien ikke oppdateres automatisk, så du må fornye den hver gang du oppretter en ny "*passordløs*"-tilkobling til Trezor.



La oss nå tenke oss at du har ødelagt Trezor-enheten din. For å hente FIDO2-påloggingsinformasjonen din må du først gjenopprette Wallet ved hjelp av Mnemonic-frasen din på en ny FIDO2-kompatibel Trezor-enhet.



Når gjenopprettingen er fullført, kjører du følgende kommando i terminalen for å importere FIDO2-identifikatorene dine på den nye enheten:



```shell
trezorctl fido credentials add <CREDENTIAL_ID>
```



Bare erstatt `<CREDENTIAL_ID>` med en av identifikatorene dine. I mitt tilfelle vil dette for eksempel gi:



```shell
trezorctl fido credentials add f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Trezor vil be deg om å importere FIDO2-identifikatoren din. Bekreft ved å trykke på på skjermen.



![Image](assets/fr/20.webp)



FIDO2-påloggingen er nå operativ på Trezor. Gjenta denne prosedyren for hver av identifikatorene dine.



Gratulerer, du er nå i gang med å bruke Trezor med U2F og FIDO2! Hvis du synes denne veiledningen var nyttig, vil jeg være veldig takknemlig hvis du legger igjen en Green-tommel nedenfor. Del gjerne denne veiledningen på dine sosiale nettverk. Tusen takk skal du ha!



Jeg vil også anbefale denne andre veiledningen, der vi ser på en annen løsning for U2F- og FIDO2-godkjenning:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e