---
name: Jade

description: Hvordan sette opp din JADE-enhet
---

![bilde](assets/cover.webp)

## Veiledningsvideo

![video](https://www.youtube.com/watch?v=_U1jsTeqbTw)
Blockstream Jade - Mobil Bitcoin Hardware Wallet FULL VEILEDNING av BTCsession

## Fullstendig skriveguide

![bilde](assets/cover2.webp)

### Forutsetninger

1. Last ned den nyeste versjonen av Blockstream Green.

2. Installer denne driveren for å sikre at Jade blir gjenkjent av datamaskinen din.

### Oppsett for skrivebord

![full guide](https://youtu.be/0fPVzsyL360)

Åpne Blockstream Green, og klikk deretter på Blockstream-logoen under Enheter.

![bilde](assets/1.webp)

Koble Jade til skrivebordet ditt med den medfølgende USB-kabelen.

> Merk: Hvis Jade ikke blir gjenkjent av datamaskinen din, sørg for å laste ned driveren som finnes i guiden her.

Når din Jade vises i Green, oppdater Jade ved å klikke Sjekk for oppdateringer og velg den nyeste firmwareversjonen. Bruk rullehjulet eller veksle på Jade for å bekrefte og fortsette med oppdateringen. Sørg for at din Jade fortsatt viser "Initialiser"-knappen, ellers må du vente til etter oppsettet av Jade for å oppgradere den. Bruk tilbake-knappen for å komme til denne skjermen om nødvendig.

![bilde](assets/2.webp)

Etter at du har oppdatert Jades firmware, velg Oppsett Jade på nettverket og sikkerhetspolitikken du ønsker å bruke.

> Tips: Sikkerhetspolitikken er oppført under Type på innloggingsskjermen vist nedenfor. Hvis du ikke er sikker på om du skal velge Singlesig eller Multisig Shield, vennligst se vår guide her. (https://help.blockstream.com/hc/en-us/articles/4403642609433)

![bilde](assets/3.webp)

Velg deretter å opprette en Ny lommebok og velg 12 ord for å generere din gjenopprettingsfrase. Ved å klikke på Avansert vil du få muligheten til en gjenopprettingsfrase på 12 og 24 ord.

![bilde](assets/4.webp)

Skriv ned gjenopprettingsfrasen offline på papir (eller ved å bruke en dedikert enhet for sikkerhetskopiering av gjenopprettingsfrase for ekstra sikkerhet). Deretter, bruk hjulet eller veksle på toppen av din Jade for å verifisere gjenopprettingsfrasen din. Dette trinnet sikrer at du har skrevet den ned korrekt.

![bilde](assets/5.webp)

Sett og bekreft din seks-sifrede PIN. Denne brukes til å låse opp Blockstream Jade hver gang du logger inn på lommeboken din.

![bilde](assets/6.webp)

Nå, velg bare Gå til Lommebok på Green-skrivebordsappen, og du vil se lommeboken din åpen på Blockstream Green. Blockstream Jade vil også vise at den er Klar! Du kan nå bruke din Jade til å sende og motta Bitcoin-transaksjoner.

![bilde](assets/7.webp)

Etter at du har avsluttet bruken av lommeboken din, koble fra din Blockstream Jade fra enheten din. Neste gang du ønsker å bruke lommeboken på Blockstream Jade, bare koble til enheten din igjen og følg instruksjonene.

kilde: https://help.blockstream.com/hc/en-us/articles/17478506300825

### Vedlegg A - Verifisering av nedlastingsfilen for Green Wallet

Å verifisere nedlastingen betyr å sjekke at filen du lastet ned ikke har blitt endret siden den ble utgitt av utvikleren.

Dette gjør vi ved å sjekke at signaturen (produsert av utviklerens private nøkkel) sammen med den nedlastede filen og utviklerens offentlige nøkkel gir et SANT resultat når de passerer gjennom gpg –verify-funksjonen. Jeg vil vise deg hvordan du gjør det neste. Hvis du vil lære bakgrunnen til dette, har jeg denne guiden og denne.
For Linux, åpne terminalen og kjør denne kommandoen (du bør bare kopiere og lime inn teksten, og inkludere anførselstegnene):
```bash
gpg --keyserver keyserver.ubuntu.com --recv-keys "04BE BF2E 35A2 AF2F FDF1 FA5D E7F0 54AA 2E76 E792"
```

For Mac, gjør du det samme, bortsett fra at du først må laste ned og installere GPG Suite.

For Windows, gjør du det samme, bortsett fra at du først må laste ned og installere GPG4Win.

Du vil få en utskrift som sier at den offentlige nøkkelen har blitt importert.

![bilde](assets/9.webp)

Dette bildet har et tomt alt-attributt; filnavnet er image-3-1024x162.webp

Videre trenger vi å få tak i filen som inneholder hashen av programvaren. Den er lagret på Blockstreams GitHub-side. Gå først til deres informasjonsside her, og klikk på lenken for "desktop". Det vil ta deg til den siste utgivelsessiden på GitHub, og der vil du se en lenke til SHA256SUMS.asc-filen, som er et tekst-dokument som inneholder Blockstreams publiserte hash av programmet vi lastet ned.

![bilde](assets/10.webp)

GitHub:

![bilde](assets/11.webp)

Det er ikke nødvendig, men etter å ha lagret til disk, omdøpte jeg "SHA256SUMS.asc" til "SHA256.txt" for lettere å kunne åpne filen på Mac ved hjelp av teksteditoren. Dette var innholdet i filen:

![bilde](assets/12.webp)

Teksten vi er etter er på toppen. Avhengig av hvilken fil vi lastet ned, er det en tilsvarende hash-utskrift som vi vil sammenligne senere.

Den nederste delen av dokumentet inneholder signaturen som ble laget på meldingen ovenfor – det er en to-i-ett-fil.

Rekkefølgen spiller ingen rolle, men før vi sjekker hashen, skal vi sjekke at hash-meldingen er ekte (dvs. ikke har blitt tuklet med).

Åpne terminal. Du må være i riktig katalog der SHA256SUMS.asc-filen ble lastet ned. Antatt at du lastet den ned til "Nedlastinger"-katalogen, for Linux og Mac, endre til katalogen slik (case sensitive):

```bash
cd Downloads
```

Selvfølgelig må du trykke <enter> etter disse kommandoene. For Windows, åpne CMD (kommandoprompt), og skriv det samme (selv om det ikke er case sensitive).

For Windows og Mac, måtte du allerede ha lastet ned GPG4Win og GPG Suite, henholdsvis, som instruert tidligere. For Linux, kommer gpg med operativsystemet. Fra Terminal (eller CMD for Windows), skriv denne kommandoen:

```bash
gpg --verify SHA256SUMS.asc
```

Den eksakte stavemåten av filnavnet (i rødt) kan være forskjellig den dagen du henter filen, så sørg for at kommandoen stemmer overens med filnavnet som ble lastet ned. Du bør få denne utskriften, og ignorere advarselen om den pålitelige signaturen – det betyr bare at du ikke manuelt har fortalt datamaskinen at du stoler på den offentlige nøkkelen vi importerte tidligere.

![bilde](assets/13.webp)

Dette bildet har et tomt alt-attributt; filnavnet er image-4-1024x165.webp

Denne utskriften bekrefter at signaturen er god, og vi er trygge på at den private nøkkelen til "info@greenaddress.it" signerte dataene (hash-rapporten).
Nå bør vi hashe vår nedlastede zip-fil og sammenligne resultatet som er publisert. Merk at i SHA256SUMS.asc-filen, er det en bit tekst som sier "Hash: SHA512" som forvirrer meg, siden filen tydeligvis har SHA256-resultater inni, så jeg kommer til å ignorere det.
For Mac og Linux, åpne terminalen, naviger til hvor zip-filen ble lastet ned (sannsynligvis må du skrive "cd Downloads" igjen, med mindre du ikke har lukket terminalen siden). For øvrig kan du alltid sjekke hvilken mappe du er i ved å skrive PWD ("print working directory), og hvis dette er helt nytt for deg, er det nyttig å se en rask YouTube-video ved å søke på "hvordan navigere i Linux/Mac/Windows-filsystemet".

For å hashe filen, skriv dette:

```bash
shasum -a 256 BlockstreamGreen_MacOS_x86_64.zip
```

Du bør sjekke hva filen din heter nøyaktig, og endre teksten i blått ovenfor om nødvendig.

Du vil få et resultat som dette (ditt vil variere hvis filen er forskjellig fra min):

![bilde](assets/14.webp)

Deretter, sammenlign visuelt hash-resultatet med det som er i SHA256SUMS.asc-filen. Hvis de stemmer overens, da –> SUKSESS! Gratulerer.

kilde: https://armantheparman.com/jade/

### Bruke det på Sparrow

Hvis du allerede vet hvordan du bruker Sparrow, så er det som alltid:

> Merk: det er samme prosess med Specter for eksempel

Last ned Sparrow ved å bruke lenken som er gitt her.

![bilde](assets/14.5.webp)

Klikk Neste for å følge oppsettsveiledningen for å lære om de forskjellige tilkoblingsalternativene.

![bilde](assets/15.webp)

Velg din ønskede server og deretter velg Opprett Ny Lommebok.

![bilde](assets/16.webp)

Skriv inn et navn for lommeboken din og klikk Opprett Lommebok.

![bilde](assets/17.webp)

Velg din ønskede policy og skripttyper og deretter velg Tilkoblet Maskinvarelommebok.

> Merk: Hvis du tidligere har brukt Blockstream Jade som en Singlesig-lommebok med Blockstream Green og ønsker å se transaksjonene dine i Sparrow, sørg for at skripttypen stemmer overens med kontotypen som inneholder midlene dine i Green. Du vil også trenge at avledningsstien stemmer overens.

![bilde](assets/18.webp)

Koble til din Blockstream Jade og klikk Skann. Du vil deretter bli bedt om å skrive inn PIN-koden din på Jade.

> Tips: Før du kobler til din Jade, sørg for at Blockstream Green-appen ikke er åpen. Hvis Green er åpen, kan dette forårsake problemer med at din Jade blir oppdaget innenfor Sparrow.

![bilde](assets/19.webp)

Velg Importer Nøkkellager for å importere den offentlige nøkkelen til standardkontoen, eller velg pilen for å manuelt velge avledningsstien du ønsker å bruke.

![bilde](assets/20.webp)

Etter at din ønskede nøkkel har blitt importert, klikk Bruk.

![bilde](assets/21.webp)

Du har nå vellykket satt opp lommeboken din, og du kan begynne å motta, lagre og bruke dine bitcoin ved hjelp av Sparrow og Blockstream Jade.

> Merk: Hvis du tidligere brukte Jade med Blockstream Green som en Multisig Shield-lommebok, bør du ikke forvente at din nye Sparrow-lommebok viser samme saldo - disse er forskjellige lommebøker. For å få tilgang til din Multisig Shield-lommebok igjen, koble ganske enkelt din Jade tilbake til Blockstream Green.

![bilde](assets/22.webp)

kilde: https://help.blockstream.com/hc/en-us/articles/7559912660761-How-do-I-use-Blockstream-Jade-with-Sparrow-
Hvis du foretrekker å bruke en mobilguide, kan du bruke den sammen med Blockstream Green
- Hvordan sette opp Blockstream Jade med Green | Blockstream Jade - https://youtu.be/7aacxnc6DHg

- Hvordan motta bitcoin til en Jade-lommebok | Blockstream Jade - https://youtu.be/CVtcDdiPqLA