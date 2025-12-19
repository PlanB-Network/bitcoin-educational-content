---
name: COLDCARD Mk

description: Opprette, sikkerhetskopiere og bruke en Bitcoin privatnøkkel med en Coldcard-enhet og Bitcoin Core
---

![cover](assets/cover.webp)

Opprette, sikkerhetskopiere og bruke en Bitcoin privatnøkkel med en Coldcard-enhet og Bitcoin Core

## Komplett guide til å generere en privatnøkkel ved hjelp av en Coldcard og bruke den gjennom grensesnittet til din Bitcoin Core-node!

I kjernen av Bitcoins nettverksbruk ligger konseptet med asymmetrisk kryptografi: et par nøkler - én privat og én offentlig - som krypterer og dekrypterer data, et konsept som sikrer konfidensialiteten av kommunikasjon.

I tilfellet med Bitcoin, ved å generere et slikt par av private og offentlige nøkler, er vi i stand til å lagre bitcoins (UTXO eller Unspent Transaction Output) og signere transaksjoner for å bruke dem.

I dag finnes det flere verktøy tilgjengelig for å lette den tilfeldige genereringen av en privatnøkkel og dens sikkerhetskopiering i tekstform ved hjelp av BIP 39 - en standard som bestemmer hvordan lommebøker assosierer en mnemonic frase (seed phrase) med krypteringsnøkler. Ofte består mnemonic frasen av 12 eller 24 ord, som må sikkerhetskopieres på en sikker måte for å kunne gjenopprette en lommebok og dens bitcoins.

I denne artikkelen vil vi lære hvordan man genererer en privatnøkkel ved hjelp av en Coldcard Mk4, en av de mest brukte og sikre enhetene i Bitcoin-verdenen, ved å bruke terningkastmetoden for å sikre maksimal entropi, og hvordan man bruker den med Bitcoin Core på en luftgappet måte!

> 🧰| Skaff følgende verktøy for å følge guiden:
>
> - Coldcard-enhet (Mk3 eller Mk4)
> - MicroSD-kort (4GB er tilstrekkelig)
> - Strøm-kun magnetisk USB-kabel (mini-usb for Mk3, usb-c for Mk4)
> - En eller flere kvalitetsterninger

## Generere en ny mnemonic frase med en Coldcard

Vi starter prosessen med å skape en privatnøkkel fra bunnen av, og antar en nylig utpakket Coldcard der en PIN allerede har blitt satt opp (følg stegene på Coldcard under enhetsinitialisering).

> 🚨 | For å tilbakestille privatnøkkelen til en allerede konfigurert Coldcard, følg disse stegene:
> Avansert/Verktøy > Fareområde > Seed Functions > Destroy Seed> ✓
> _Oppmerksomhet_: din Coldcard vil glemme privatnøkkelen etter disse stegene. Sørg for at du har sikkerhetskopiert mnemonic frasen din ordentlig hvis du ønsker å kunne gjenopprette den senere.

## Steg å følge:

Koble til Coldcard med PIN > New Seed Words > 24 Word Dice Roll

Utfør 100 terningkast, og skriv ned resultatet oppnådd fra 1 til 6 på Coldcard etter hvert kast. Ved å praktisere denne metoden, skaper du 256 bytes med entropi, og favoriserer dermed skapelsen av en helt tilfeldig privatnøkkel. Coinkite gir også nødvendig dokumentasjon for uavhengig verifisering av deres entropigenereringssystem.

![Visual Cold Card Screenshot](assets/guide-agora/1.webp)

Når de 100 terningkastene er fullført, trykk ✓ og deretter skriv ned de 24 ordene oppnådd i rekkefølge. Verifiser to ganger og trykk ✓. Til slutt gjenstår det bare å fullføre verifiseringstesten av de 24 ordene på Coldcard, og voilà, din nye privatnøkkel er skapt!

Deretter velger du om du vil aktivere NFC (Mk4) og USB-funksjoner ved å følge de viste stegene. Når du er i hovedmenyen, er det nå på tide å oppdatere enhetens firmware. Gå til Avansert/Verktøy > Oppgrader Firmware > Vis Versjon, og sjekk det offisielle nettstedet for å validere og laste ned den nyeste tilgjengelige versjonen. Det anbefales å oppdatere Coldcard for å dra nytte av maksimal sikkerhet.
Før du fortsetter, anbefales det å notere Master Key Fingerprint (XFP) som er knyttet til den private nøkkelen. Disse dataene tillater rask validering hvis du er i riktig lommebok i tilfelle gjenoppretting, for eksempel. Gå til Avansert/Verktøy > Vis Identitet > Master Key Fingerprint (XFP) og skriv ned serien med åtte alfanumeriske tegn som er oppnådd. XFP kan noteres på samme sted som den mnemoniske frasen, det er ikke sensitiv data.
> 💡 Det anbefales å teste sikkerhetskopien av din mnemoniske frase i en annen programvare. For å gjøre dette på en sikker måte, se vår artikkel Verifiser sikkerhetskopien av en Bitcoin-lommebok med Tails på mindre enn 5 minutter.

## Sikkerhetsbonus: "Hemmelig Frase" (valgfritt)

'En passfrase (hemmelig frase) er et flott element å legge til i en lommebokkonfigurasjon for å legge til et lag med sikkerhet for å beskytte dine bitcoins. Passfrasen fungerer som en slags 25. ord til den mnemoniske frasen. Når den er lagt til, opprettes en helt ny lommebok sammen med en privat nøkkel og dens tilhørende mnemoniske frase. Det er ikke nødvendig å skrive ned den nye mnemoniske frasen, da denne lommeboken kan nås ved å kombinere den opprinnelige mnemoniske frasen med den valgte passfrasen.

Målet er å notere passfrasen separat fra den mnemoniske frasen fordi en angriper som har tilgang til begge elementene vil ha tilgang til midlene. På den annen side vil en angriper som bare har tilgang til ett av disse elementene ikke ha tilgang til midlene, og det er denne spesifikke fordelen som optimaliserer sikkerhetsnivået til lommebokkonfigurasjonen.

![Å legge til en passfrase fører til en helt annen lommebok](assets/guide-agora/2.webp)

## Trinn for å legge til en passfrase med Coldcard:

Passfrase > Legg til ord (anbefalt) > Bruk. Enheten vil vise XFP for den nygenererte lommeboken med passfrasen, som bør noteres ned sammen med passfrasen av de samme grunnene som nevnt tidligere.

> 💡 Tilleggsressurser relatert til passfrasen:

    https://blog.trezor.io/is-your-passphrase-strong-enough-d687f44c63af
    https://blog.coinkite.com/everything-you-need-to-know-about-passphrases/
    https://armantheparman.com/passphrase/

## Eksportere lommeboken til Bitcoin Core

Lommeboken er nå klar til å bli eksportert til programvare for å samhandle med Bitcoin-nettverket. I denne veiledningen vil vi bruke Bitcoin Core (v24.1).

Se våre installasjons- og konfigurasjonsguider for Bitcoin Core:

> Kjøre din egen node med Bitcoin Core - https://agora256.com/faire-tourner-son-propre-noeud-avec-bitcoin-core/
>
> Konfigurere Tor for en Bitcoin Core-node - https://agora256.com/configuration-tor-bitcoin-core/

Først, sett inn et micro SD-kort i Coldcard, deretter eksporter lommeboken for Bitcoin Core ved å følge disse trinnene: Avansert/Verktøy > Eksporter Lommebok > Bitcoin Core. To filer vil bli skrevet til micro SD-kortet: bitcoin-core.sig & bitcoin-core.txt. Sett inn micro SD-kortet i datamaskinen der Bitcoin Core er installert, og åpne .txt-filen. Du vil se linjen "For lommebok med master key fingerprint." Verifiser at den åtte-tegns XFP stemmer overens med den du noterte da du opprettet din private nøkkel.
Før du følger instruksjonene i filen, la oss starte med å forberede lommeboken i Bitcoin Core-grensesnittet ved å følge disse stegene: gå til Fil-fanen > Opprett en lommebok. Velg et navn for lommeboken din (utskiftbart uttrykk med "porte-monnaie" i Core) og sjekk alternativene Deaktiver private nøkler, Opprett en tom lommebok, og Lommebokbeskrivelser som vist på bildet nedenfor. Deretter, trykk på Opprett-knappen.
![opprett en lommebok](assets/guide-agora/3.webp)

Når lommeboken er opprettet i Bitcoin Core, gå til Vindu-fanen > Konsoll og sørg for at den valgte lommeboken øverst på siden viser navnet på den du opprettet.

Nå, i .txt-filen generert av Coldcard tidligere, kopier linjen som starter med importdescriptors, deretter lim den inn i Bitcoin Core-konsollen. Et svar inkludert linjen "success": true bør returneres.

![noder vindu](assets/guide-agora/4.webp)

Hvis svaret inneholder "message": "Ranged descriptors should not have a label", slett oppføringen "label": "Coldcard xxxx0000" i den kopierte linjen fra .txt-filen, deretter lim den komplette linjen tilbake inn i Bitcoin Core-konsollen.

Hjelp: [https://github.com/Coldcard/firmware/blob/master/docs/bitcoin-core-usage.md](https://github.com/Coldcard/firmware/blob/master/docs/bitcoin-core-usage.md)

## Validering av lommebokimport i Bitcoin Core

For å sikre at operasjonen var vellykket, er det nødvendig å validere at den ønskede lommeboken har blitt importert til Bitcoin Core. En enkel metode for å bekrefte dette er å verifisere at adressene generert i Coldcard tilsvarer adressene generert i Bitcoin Core.

Bitcoin Core: Motta > Opprett en ny mottaksadresse
Coldcard: Adresseutforsker > Velg adressen som starter med bc1q. Coldcard-adressen 'bc1q' bør matche adressen som vises i Bitcoin Core.
Motta og sende transaksjoner i 'air-gapped' modus

Å motta en transaksjon er ekstremt enkelt; bare trykk Motta, merk transaksjonen (valgfritt, men anbefalt), og Opprett en ny mottaksadresse. Deretter er alt som gjenstår å dele adressen med avsenderen.

Nå, det nøkkel elementet av denne Coldcard + Bitcoin Core oppsettet er å sende transaksjoner uten at Coldcard og dens private nøkkel er koblet til internett, en metode kalt air-gapped som bruker TBSP (PSBT - Partially Signed Bitcoin Transactions) funksjonen av Bitcoin.
I hovedsak bruker vi Bitcoin Core-grensesnittet til å konstruere en transaksjon, som vi deretter vil eksportere via micro SD-kortet til Coldcard for signering, og deretter returnere den signerte transaksjonsfilen til Bitcoin Core og kringkaste transaksjonen til nettverket. Vi må gjøre det på denne måten fordi lommeboken importert til Bitcoin Core ikke har en privat nøkkel, bare den offentlige nøkkelen (som lar oss generere våre mottaksadresser), så det er umulig for oss å signere en transaksjon direkte i programvaren for å bruke våre bitcoins.

Før du fortsetter, sørg for at følgende alternativer er aktivert i Innstillinger > Lommebok:

> - Aktiver myntkontrollfunksjoner
> - Bruk ubekreftede mynter (Valgfritt)
> - Aktiver TBPS-sjekker

![alternativ](assets/guide-agora/5.webp)

### Steg for å sende i air-gapped modus:
Send > Inndata > velg ønsket utxo, deretter skriv inn mottakerens adresse i Betal til. Transaksjonsgebyr: Velg... > Tilpasset > Skriv inn transaksjonsgebyret (Bitcoin Core beregner i sats/kilobyte i stedet for sat/byte som de fleste alternative lommebokløsninger. Så 4000 sats/kilobyte = 4 sats/byte). Opprett en usignert transaksjon > lagre filen på ditt mikro SD-kort og sett det inn i Coldcard.
I Coldcard, trykk Klar til å signere, verifiser transaksjonsdetaljene, deretter trykk ✓ og sett mikro SD-kortet tilbake i datamaskinen når de signerte filene er generert.

Tilbake i Bitcoin Core, gå til Fil-fanen > Last inn TBSP fra fil, og skriv inn den signerte transaksjonsfilen .psbt. PSBT Operasjonsboksen vil dukke opp på skjermen, og bekrefter at transaksjonen er fullstendig signert og klar til å bli kringkastet. Alt som gjenstår er å trykke Kringkast transaksjon.

![PSBT operasjoner](assets/guide-agora/6.webp)

### Konklusjon

Kombinasjonen av Coldcard-enheten med Bitcoin Core, der du kjører din egen node, er kraftfull. Legg til det en privat nøkkel generert med 100 terningkast og en hemmelig frase, og din lommebokkonfigurasjon blir en sofistikert og robust festning.

Ta gjerne kontakt med oss for å dele dine kommentarer og spørsmål! Vårt mål er å dele kunnskap og øke vår forståelse dag for dag.