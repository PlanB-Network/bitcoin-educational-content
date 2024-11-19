---
name: YubiKey 2FA
description: Hvordan bruke en fysisk sikkerhetsnøkkel?
---
![cover](assets/cover.webp)

I dag har tofaktorautentisering (2FA) blitt essensielt for å forbedre sikkerheten til online kontoer mot uautorisert tilgang. Med økningen i cyberangrep, er det noen ganger ikke tilstrekkelig å kun stole på et passord for å sikre kontoene dine.

2FA introduserer et ekstra lag med sikkerhet ved å kreve en sekundær form for autentisering i tillegg til det tradisjonelle passordet. Denne verifiseringen kan ta ulike former, som en kode sendt via SMS, en dynamisk kode generert av en dedikert app, eller bruk av en fysisk sikkerhetsnøkkel. Bruk av 2FA reduserer betydelig risikoen for at kontoene dine blir kompromittert, selv i tilfelle passordet ditt blir stjålet.

I en annen veiledning forklarte jeg hvordan du setter opp og bruker en TOTP 2FA-applikasjon:

https://planb.network/tutorials/others/authy

Her vil vi se på hvordan du bruker en fysisk sikkerhetsnøkkel som en sekundær autentiseringsfaktor for alle kontoene dine.

## Hva er en fysisk sikkerhetsnøkkel?

En fysisk sikkerhetsnøkkel er en enhet som brukes til å forbedre sikkerheten til dine online kontoer gjennom tofaktorautentisering (2FA). Disse enhetene ligner ofte små USB-nøkler som må settes inn i en datamaskins port for å verifisere at det faktisk er den legitime brukeren som forsøker å koble seg til.
![SECURITY KEY 2FA](assets/notext/01.webp)
Når du logger inn på en konto beskyttet av 2FA og bruker en fysisk sikkerhetsnøkkel, må du ikke bare oppgi ditt vanlige passord, men også sette den fysiske sikkerhetsnøkkelen inn i datamaskinen din og trykke på en knapp for å validere autentiseringen. Denne metoden legger til et ekstra lag med sikkerhet, for selv om noen klarer å skaffe passordet ditt, vil de ikke kunne få tilgang til kontoen din uten å fysisk besitte nøkkelen.

Den fysiske sikkerhetsnøkkelen er spesielt effektiv fordi den kombinerer to forskjellige typer autentiseringsfaktorer: kunnskapsbevis (passordet) og besittelsesbevis (den fysiske nøkkelen).

Men, denne 2FA-metoden har også ulemper. For det første må du alltid ha sikkerhetsnøkkelen tilgjengelig hvis du ønsker å få tilgang til kontoene dine. Du må kanskje legge den til nøkkelknippet ditt. For det andre, i motsetning til andre 2FA-metoder, innebærer bruk av en fysisk sikkerhetsnøkkel en innledende kostnad siden du må kjøpe den lille enheten. Prisen på sikkerhetsnøkler varierer generelt mellom €30 og €100 avhengig av valgte funksjoner.

## Hvilken fysisk sikkerhetsnøkkel skal du velge?

For å velge din sikkerhetsnøkkel, må flere kriterier tas i betraktning.
Først og fremst må du sjekke hvilke protokoller enheten støtter. Som et minimum anbefaler jeg å velge en nøkkel som støtter OTP, FIDO2, og U2F. Disse detaljene er vanligvis fremhevet av produsentene i produktbeskrivelsene. For å verifisere kompatibiliteten til hver nøkkel, kan du også besøke [dongleauth.com](https://www.dongleauth.com/dongles/).
Sørg også for at nøkkelen er kompatibel med operativsystemet ditt, selv om kjente merker som Yubikey generelt støtter alle mye brukte systemer.

Du bør også velge nøkkelen basert på typen porter som er tilgjengelige på datamaskinen eller smarttelefonen din. For eksempel, hvis datamaskinen din kun har USB-C porter, velg en nøkkel med en USB-C-kontakt. Noen nøkler tilbyr også tilkoblingsmuligheter via Bluetooth eller NFC.
![SECURITY KEY 2FA](assets/notext/02.webp)
Du kan også sammenligne enheter basert på deres tilleggsfunksjoner som vann- og støvresistens, samt nøkkelens form og størrelse.
Når det gjelder merker av sikkerhetsnøkler, er Yubico det mest kjente med sine [YubiKey-enheter](https://www.yubico.com/), som jeg personlig bruker og anbefaler. Google tilbyr også en enhet med [Titan Security Key](https://store.google.com/fr/product/titan_security_key). For åpne kildekode-alternativer er [SoloKeys](https://solokeys.com/) (ikke OTP) og [NitroKey](https://www.nitrokey.com/products/nitrokeys) interessante valg, men jeg har aldri hatt sjansen til å teste dem.
## Hvordan bruke en fysisk sikkerhetsnøkkel?

Når du har mottatt din sikkerhetsnøkkel, kreves ingen spesifikk oppsett. Nøkkelen er normalt klar til bruk ved mottak. Du kan umiddelbart bruke den for å sikre dine online kontoer som støtter denne typen autentisering. For eksempel, jeg vil vise deg hvordan du sikrer min Proton mail-konto med denne fysiske sikkerhetsnøkkelen.
![SECURITY KEY 2FA](assets/notext/03.webp)
Du vil finne alternativet for å aktivere 2FA i kontoinnstillingene dine, ofte under "*Passord*" eller "*Sikkerhet*" seksjonen. Klikk på avkrysningsboksen eller knappen som lar deg aktivere 2FA med en fysisk nøkkel.
![SECURITY KEY 2FA](assets/notext/04.webp)
Koble nøkkelen din til datamaskinen.
![SECURITY KEY 2FA](assets/notext/05.webp)
Trykk på knappen på sikkerhetsnøkkelen din for å validere.
![SECURITY KEY 2FA](assets/notext/06.webp)
Skriv inn et navn for å huske hvilken nøkkel du brukte.
![SECURITY KEY 2FA](assets/notext/07.webp)
Og der har du det, din sikkerhetsnøkkel har blitt vellykket lagt til for 2FA-autentiseringen av kontoen din.
![SECURITY KEY 2FA](assets/notext/08.webp)
I mitt eksempel, hvis jeg prøver å koble til min Proton mail-konto på nytt, vil jeg først bli bedt om å skrive inn passordet mitt sammen med brukernavnet mitt. Dette er den første faktoren av autentisering.
![SECURITY KEY 2FA](assets/notext/09.webp)
Deretter blir jeg bedt om å koble til sikkerhetsnøkkelen min for den andre faktoren av autentisering.
![SECURITY KEY 2FA](assets/notext/10.webp)
Neste, jeg trenger å trykke på knappen på den fysiske nøkkelen for å validere autentiseringen, og jeg er koblet til min Proton mail-konto igjen.
![SECURITY KEY 2FA](assets/notext/11.webp)
Gjenta denne operasjonen for alle online kontoene du ønsker å sikre på denne måten, spesielt for kritiske kontoer som dine e-postkontoer, dine passordbehandlere, dine sky- og online lagringstjenester, eller dine finanskontoer.