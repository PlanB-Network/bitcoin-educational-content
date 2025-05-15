---
name: Ledger U2F & FIDO2
description: Forbedre nettsikkerheten din med Ledger
---
![cover](assets/cover.webp)



Ledger-enheter er maskinvarelommebøker som opprinnelig ble utviklet for å sikre en Bitcoin Wallet, men de har også avanserte alternativer for sterk autentisering på nettet. Takket være kompatibiliteten med **U2F**- og **FIDO2**-protokollene gjør de det mulig å sikre tilgangen til nettkontoene dine ved å sette opp en ekstra autentiseringsfaktor.



U2F-protokollen (Universal 2nd Factor) ble introdusert av Google og Yubico i 2014, og ble deretter standardisert av FIDO Alliance. Den gjør det mulig å legge til en ekstra fysisk autentiseringsfaktor (2FA) ved innlogging. Når den er aktivert, må brukerne, i tillegg til det klassiske passordet, godkjenne hvert forsøk på å koble seg til kontoen sin ved å trykke på en knapp på Ledger. I denne sammenhengen fungerer Ledger på samme måte som en Yubikey. U2F er faktisk en delkomponent av FIDO2-standarden, og omfatter den samtidig som den gir betydelige forbedringer, blant annet støtte for moderne nettlesere og større fleksibilitet i autentiseringsnøkkelhåndteringen.



Disse metodene er basert på asymmetrisk kryptografi: Ingen hemmelige data overføres, noe som gjør phishing- eller avlyttingsangrep ineffektivt. U2F og FIDO2 støttes nå av mange nettbaserte tjenester.



I denne veiledningen viser vi deg hvordan du aktiverer U2F og FIDO2 for tofaktorautentisering med Ledger.



**U2F og FIDO2 støttes på alle Ledger-enheter som er utstyrt med nyere fastvare: fra versjon 2.1.0 for Nano X og Nano S classic, og fra versjon 1.1.0 for Nano S Plus. Stax- og Flex-modellene er opprinnelig kompatible.



## Installer Ledger Security Key-applikasjonen



Hvis du bruker en Ledger-enhet, vet du sannsynligvis at fastvaren alene ikke inneholder alle funksjonene som trengs for å administrere kryptolommebøker. Hvis du for eksempel skal bruke en Bitcoin Wallet, må du installere applikasjonen "*Bitcoin*". På samme måte må du installere applikasjonen "*Security Key*" for å administrere MFA-nøkler.



Før du begynner, må du sørge for at du har satt opp Bitcoin Wallet på Ledger. Det er viktig at du lagrer Mnemonic på riktig måte, ettersom nøklene som brukes til 2FA, er avledet fra denne Mnemonic. Hvis Ledger går tapt eller blir skadet, kan du få tilgang til nøklene dine igjen ved å skrive inn Mnemonic-frasen på en annen Ledger-enhet (for øyeblikket støttes ikke FIDO2-identifikatorer i "*passordløs*"-modus på Ledgers, så det finnes ingen residente identifikatorer).



Koble Ledger til datamaskinen og lås den opp.



![Image](assets/fr/01.webp)



For å installere applikasjonen åpner du [Ledger Live]-programvaren (https://www.Ledger.com/Ledger-live), og går deretter til "*My Ledger*"-fanen. Finn applikasjonen "*Security Key*" og installer den på enheten din.



![Image](assets/fr/02.webp)



Applikasjonen "*Security Key*" skal nå vises sammen med de andre applikasjonene som er installert på din Ledger.



![Image](assets/fr/03.webp)



Klikk på applikasjonen for å la den være åpen for de neste trinnene i veiledningen.



![Image](assets/fr/04.webp)



## Bruk U2F/FIDO2 for 2FA med en Ledger



Gå til kontoen du vil sikre med tofaktorautentisering. Jeg kommer for eksempel til å bruke en Bitwarden-konto. Du finner vanligvis 2FA-alternativet i tjenesteinnstillingene, under fanene "*autentisering*", "*sikkerhet*", "*innlogging*" eller "*passord*".



![Image](assets/fr/05.webp)



I delen som er dedikert til tofaktorautentisering, velger du alternativet "*Passkode*" (begrepet kan variere avhengig av hvilket nettsted du bruker).



![Image](assets/fr/06.webp)



Du vil ofte bli bedt om å bekrefte ditt nåværende passord.



![Image](assets/fr/07.webp)



Gi sikkerhetsnøkkelen et navn slik at den er lett å gjenkjenne, og klikk deretter på "*Les nøkkel*".



![Image](assets/fr/08.webp)



Kontodetaljene dine vises på Ledger-displayet. Trykk på "*Register*"-knappen for å bekrefte (eller begge knappene samtidig, avhengig av hvilken modell du bruker).



![Image](assets/fr/09.webp)



Tilgangsnøkkelen har blitt registrert.



![Image](assets/fr/10.webp)



Registrer denne sikkerhetsnøkkelen.



![Image](assets/fr/11.webp)



Fra nå av vil du bli bedt om å koble til Ledger i tillegg til det vanlige passordet når du logger inn på kontoen din.



![Image](assets/fr/12.webp)



Deretter kan du trykke på "*Log in*"-knappen på Ledger-skjermen for å bekrefte autentiseringen (eller begge knappene samtidig, avhengig av hvilken modell du bruker).



![Image](assets/fr/13.webp)



Fordelen med å bruke en Hardware Wallet Ledger for tofaktorautentisering er at du enkelt kan gjenopprette nøklene dine takket være Mnemonic-frasen. I tillegg til denne grunnleggende sikkerhetskopien kan du også bruke en nødkode som leveres av hver tjeneste der du har aktivert 2FA. Med denne nødkoden kan du koble deg til kontoen din hvis du mister sikkerhetsnøkkelen. Den erstatter derfor 2FA for en tilkobling om nødvendig.



På Bitwarden kan du for eksempel få tilgang til denne koden ved å klikke på "*Vis gjenopprettingskode*".



![Image](assets/fr/14.webp)



Jeg anbefaler at du oppbevarer denne koden på et annet sted enn der du lagrer hovedpassordet ditt, for å forhindre at de blir stjålet sammen. Hvis passordet ditt for eksempel er lagret i en passordbehandler, bør du oppbevare 2FA-nødkoden på papir, separat.



Denne tilnærmingen gir deg to nivåer av sikkerhetskopiering i tilfelle du mister Ledger for 2FA-autentisering: en første sikkerhetskopiering ved hjelp av Mnemonic-frasen for alle kontoene dine, og en andre kontospesifikk sikkerhetskopiering ved hjelp av nødkodene. Det er imidlertid viktig **ikke å forveksle rollen til Mnemonic med rollen til nødkoden** :




- Mnemonic-frasen på 12 eller 24 ord gir deg ikke bare tilgang til nøklene som brukes til 2FA på alle kontoene dine, men også til bitcoinsene dine som er sikret med Ledger ;
- Nødkoden lar deg midlertidig omgå 2FA-forespørselen bare på den aktuelle kontoen (i dette eksempelet bare på Bitwarden).



Gratulerer, du er nå i gang med å bruke Ledger for MFA! Hvis du synes denne veiledningen var nyttig, vil jeg være veldig takknemlig hvis du legger igjen en Green-tommel nedenfor. Del gjerne denne veiledningen på dine sosiale nettverk. Tusen takk skal du ha!



Jeg vil også anbefale denne andre veiledningen, der vi ser på en annen løsning for U2F- og FIDO2-godkjenning:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e