---
name: Tails

description: Installer Tails på en USB-nøkkel
---

![bilde](assets/cover.webp)

Et bærbart og amnestisk operativsystem som beskytter deg mot overvåkning og sensur.

## Hvorfor ha en USB-nøkkel med Tails installert?

Tails (https://tails.boum.org/) er den enkleste måten å alltid ha en sikker datamaskin tilgjengelig, som ikke vil etterlate noen spor på datamaskinen du bruker den med.

For å bruke Tails, slå av datamaskinen du har tilgang til (hos foreldrene dine, hos vennene dine, i et internettkafe...) og start den med din Tails USB-nøkkel i stedet for Windows, macOS, eller Linux.

Etter det vil du ha et arbeidsområde og kommunikasjonsmiljø som er uavhengig av det vanlige operativsystemet og aldri bruker harddisken.

Tails skriver aldri til harddisken og bruker kun datamaskinens RAM for å fungere. Denne minnet blir fullstendig slettet når Tails blir slått av, og fjerner dermed alle mulige spor.

## Noen konkrete bruksområder

For å gi deg konkrete ideer om fordelene med å alltid ha en USB-nøkkel med Tails, her er en liten ikke-uttømmende liste sammensatt av Agora256-teamet:

- Koble til internett og Tor på en usensurert og anonym måte for å surfe på nettsteder uten å etterlate spor;
- Åpne en PDF fra et mistenkelig nettsted;
- Teste din Bitcoin private nøkkelbackup med Electrum-lommeboken;
- Bruke et kontorpakke (LibreOffice) og arbeide på en datamaskin som ikke tilhører deg;
- Ta dine første skritt i et Linux-miljø for å lære hvordan du forlater verdenen av Microsoft og Apple.

## Hvordan stole på Tails?

Det er alltid et element av tillit i å bruke programvare, men det trenger ikke å være blindt. Et verktøy som Tails må strebe etter å gi brukerne sine midler til å være troverdig. For Tails betyr dette:

- Offentlig kildekode: https://gitlab.tails.boum.org/;
- Et prosjekt basert på anerkjente prosjekter: Tor og Debian;
- Verifiserbare og reproduserbare nedlastinger;
- Anbefalinger av forskjellige individer og organisasjoner.

## Installasjons- og bruksveiledning

Formålet med denne installasjonsveiledningen er å veilede deg gjennom hvert trinn av installasjonen. Vi vil ikke beskrive handlinger som skal tas mer enn den offisielle veiledningen, men vi vil peke deg i riktig retning mens vi gir deg tips og triks.

Av praktiske erfaringer vil disse tipsene være fokusert på macOS- og Linux-plattformer.
🛠️
Før du starter denne prosedyren, vennligst sørg for at du har en USB-nøkkel med en minimum lesehastighet på 150 MB/s og en kapasitet på minst 8 GB, ideelt USB 3.0.

Forutsetninger:

- 1 USB-nøkkel, kun for Tails, med en kapasitet på minst 8 GB
- En datamaskin koblet til internett med Linux, macOS, (eller Windows)
- Omtrent en time med ledig tid, avhengig av internettforbindelsens hastighet, inkludert ½ time for installasjon (1.3 GB fil å laste ned)

## Steg 1: Last ned Tails fra datamaskinen din

![bilde](assets/1.webp)

> 🔗 Offisiell Tails-seksjon: https://tails.boum.org/install/linux/index.fr.html#download

Nedlasting av installasjonsfilen med .img-utvidelsen kan ta litt tid avhengig av nedlastingshastigheten på internettet ditt, så planlegg i forveien. Med en moderne og effektiv tilkobling, vil det ta mindre enn 5 minutter.

Lagre filen i en kjent mappe, som Nedlastinger, da dette vil være nødvendig for neste steg.

## Steg 2: Verifiser nedlastingen din

![bilde](assets/2.webp)
> 🔗 Offisiell Tails-seksjon: https://tails.boum.org/install/linux/index.fr.html#verify
Å verifisere nedlastingen sikrer at den kommer fra Tails-utviklerne og ikke har blitt korrupt eller avlyttet under nedlastingen.

Det er mulig å manuelt verifisere at filen du nettopp lastet ned er den forventede ved å bruke PGP, men uten avansert kunnskap tilbyr denne verifiseringen samme sikkerhetsnivå som JavaScript-verifiseringen på nedlastingssiden, samtidig som den er mye mer komplisert og utsatt for feil.

For å verifisere filen, bruk "Velg nedlastingen din..."-knappen som er tilgjengelig i den offisielle seksjonen!

## Steg 3: Installer Tails på din USB-nøkkel

![bilde](assets/3.webp)

> 🔗 Offisiell Tails-seksjon:
>
> - Linux: https://tails.boum.org/install/linux/index.fr.html#install
> - macOS: https://tails.boum.org/install/mac/index.fr.html#etcher og https://tails.boum.org/install/mac/index.fr.html#install

Dette steget med å installere Tails på din USB-nøkkel er det vanskeligste i hele veiledningen, spesielt hvis du aldri har gjort det før. Det viktigste punktet er å velge riktig prosedyre i den offisielle seksjonen for ditt operativsystem: Linux eller macOS.

Når verktøyene er installert og forberedt som anbefalt, kan filen med .img-utvidelsen kopieres til nøkkelen din (og slette alle eksisterende data) for å gjøre den "bootbar" uavhengig.

Lykke til! og vi ses ved steg 4.

## Steg 4: Start på nytt på din Tails USB-nøkkel

![bilde](assets/4.webp)

> 🔗 Offisiell Tails-seksjon: https://tails.boum.org/install/linux/index.en.html#restart
> Det er på tide å starte en av datamaskinene dine ved hjelp av din nye USB-stikk. Sett den inn i en av USB-portene og start på nytt!

> 💡 De fleste datamaskiner starter ikke automatisk fra Tails USB-stikken, men du kan trykke på bootmeny-tasten for å vise en liste over mulige enheter å starte fra.

For å bestemme hvilken tast du skal trykke for å sikre at du har bootmenyen som lar deg velge USB-stikken i stedet for din vanlige harddisk, her er en ikke-uttømmende liste etter produsent:

| Produsent | Tast              |
| --------- | ----------------- |
| Acer      | F12, F9, F2, Esc  |
| Apple     | Option            |
| Asus      | Esc               |
| Clevo     | F7                |
| Dell      | F12               |
| Fujitsu   | F12, Esc          |
| HP        | F9                |
| Huawei    | F12               |
| Intel     | F10               |
| Lenovo    | F12               |
| MSI       | F11               |
| Samsung   | Esc, F12, F2      |
| Sony      | F11, Esc, F10     |
| Toshiba   | F12               |
| andre...  | F12, Esc          |

Når USB-stikken er valgt, bør du se denne nye oppstartsskjermen, som er et veldig godt tegn, så la datamaskinen fortsette å starte...

![bilde](assets/5.webp)

## Steg 5: Velkommen til Tails!

![bilde](assets/6.webp)

> 🔗 Offisiell Tails-seksjon: https://tails.boum.org/install/linux/index.en.html#tails

Ett eller to minutter etter oppstartslasteren og lasteskjermen, vises velkomstskjermen.

![bilde](assets/7.webp)

På velkomstskjermen, velg ditt språk og tastaturoppsett i Språk & Region-seksjonen. Klikk på Start Tails.

![bilde](assets/8.webp)
Hvis datamaskinen din ikke er koblet til nettverket ditt med kabel, vennligst se de offisielle Tails-instruksjonene for å hjelpe deg med å koble til nettverket ditt uten Wi-Fi (seksjon "Test din Wi-Fi").
Når du er koblet til det lokale nettverket, vises Tor Connection-veiviseren for å hjelpe deg med å koble til Tor-nettverket.

![bilde](assets/9.webp)

Du kan begynne å surfe anonymt, utforske alternativene og programvaren som er inkludert i Tails. Kos deg, du har rikelig med rom for feil, ettersom ingenting blir endret på USB-stikken... Din neste omstart vil ha glemt alle dine opplevelser!

## I en fremtidig guide...

Når du har eksperimentert litt mer med din egen Tails USB-stikk, vil vi utforske andre mer avanserte emner i en annen artikkel, som:

> Oppdatere en nøkkel med den nyeste versjonen av Tails; Konfigurere og bruke vedvarende lagring; Installere tilleggsprogramvare.
> Inntil da, som alltid, hvis du har noen spørsmål, føl deg fri til å dele dem med Agora256-samfunnet. Vi lærer sammen for å være bedre i morgen enn vi er i dag!