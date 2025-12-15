---
name: Nostr
description: Oppdag og begynn å bruke NOSTR
---


![En ny utfordrer har ankommet](assets/1.webp)

*På slutten av denne guiden vil du forstå hva Nostr er, du vil ha opprettet en konto, og du vil kunne bruke den.*

## Hva er Nostr?

Nostr er et protokoll som har kraften til å erstatte Twitter, Telegram og andre sosiale medieplattformer. Det er en enkel åpen protokoll som er i stand til å skape et globalt motstandsdyktig sosialt nettverk en gang for alle.

## Hvordan fungerer det?

Nostr er basert på tre komponenter: nøkkelpar, klienter og reléer.

Hver bruker har en eller flere identiteter, og hver identitet er bestemt av et kryptografisk nøkkelpar.

For å få tilgang til nettverket, må du bruke klientprogramvare og koble til reléer for å motta og overføre innhold.

![Nøkkelsystem](assets/2.webp)

## 1. Kryptografiske nøkler

I motsetning til Facebook eller Twitter, hvor brukere må oppgi en e-postadresse og en mengde informasjon til et privat selskap, opererer Nostr uten en sentral autoritet. Brukere genererer et kryptografisk nøkkelpar, en hemmelig nøkkel (også kjent som en privat nøkkel), og en offentlig nøkkel.

Den hemmelige nøkkelen, nsec, som bare er kjent av brukeren, brukes for autentisering og publisering av innhold.

Den offentlige nøkkelen, npub, er en unik identifikator som alt innhold publisert av en bruker er knyttet til. Din offentlige nøkkel er som et brukernavn som lar andre brukere finne deg og abonnere på din Nostr-feed.

## 2. Klienter

Klienter er programvare som tillater interaksjon med Nostr. De viktigste klientene er:

- iOS: damus
- Android: amethyst
- Web: iris.to; snort.social; astral.ninja

Klienter lar brukere generere et nytt nøkkelpar (tilsvarende å opprette en konto) eller autentisere med et eksisterende nøkkelpar.

## 3. Reléer

Reléer er enkle servere som du kan forlate når som helst hvis du ikke liker innholdet de leverer til deg. Du kan også kjøre ditt eget relé hvis du ønsker.

> 💡 Pro-tips: Betalte reléer er generelt mer effektive til å filtrere ut spam og uønsket innhold.

## Veiledning

Nå vet du nok om Nostr for å komme i gang og opprette din første identitet på denne protokollen.

For formålet med denne veiledningen vil vi bruke iris.to (https://iris.to/) ettersom denne webklienten fungerer på alle plattformer.

## Steg 1: Generering av nøkler

Iris vil opprette et sett med nøkler for deg uten at du trenger å gjøre noe mer enn å angi et navn (ekte eller fiktivt) for profilen din. Deretter klikker du på GO og du er ferdig!

![Hovedmeny](assets/3.webp)

> ⚠️ Oppmerksomhet! Du må holde styr på nøklene dine hvis du vil kunne få tilgang til profilen din igjen når økten er lukket. Jeg vil vise deg hvordan du gjør dette helt på slutten av denne veiledningen.

## Steg 2: Publisere innhold

Å publisere innhold er like enkelt og intuitivt som å skrive noen ord i publiseringsfeltet.

![Publisering](assets/4.webp)

Der har du det! Du har publisert din første notat på Nostr.

![Innlegg](assets/5.webp)

## Steg 3: Finn en venn

Finn meg på Nostr og vær aldri alene igjen. Jeg vil abonnere tilbake på alle som abonnerer på min feed. For å gjøre dette, skriv inn min offentlige nøkkel

npub1hartx53w6t3q5wv9xdqdwrk7h6r5866t8u775q0304zedpn5zgssasp7d3 i søkefeltet.
![Min profil](assets/6.webp)
Klikk på "følg", og i løpet av noen få dager vil jeg også abonnere på din feed. Vi vil bli venner. Jeg vil også være glad for å lese din melding hvis du ønsker å skrive en til meg.

Til slutt, sørg for å også abonnere på Agora256 sin feed for å motta en notis hver gang vi publiserer noe nytt: npub1ag0rawstycy7nanuc6sz4v287rneen2yapcq3fd06972f8ncrhzqx

## Steg 4: Tilpass profilen din

Du har fortsatt litt arbeid å gjøre for å tilpasse profilen din. For å gjøre dette, klikk på avataren som iris automatisk genererte for deg i øvre høyre hjørne av skjermen, og deretter klikk på "rediger profil".

![Profil](assets/7.webp)

Alt du nå trenger å gjøre er å fortelle iris hvor den kan finne bildet ditt og profilbanneret ditt på internett. Jeg anbefaler å hoste ditt eget innhold: beskytt det som er ditt.

![Et annet alternativ](assets/8.webp)

Hvis du foretrekker, kan du også laste opp bilder, de vil bli lagret for deg av iris på nostr.build, en gratis visuell innholdshostingtjeneste for Nostr.

Som du kan se, kan du også konfigurere klienten din til å kunne motta og sende sats. På denne måten kan du belønne forfatterne av innhold du likte eller, enda bedre, samle sats for det flotte innholdet du vil publisere.

## Steg 5: Sikkerhetskopier nøkkelparet

Dette steget er avgjørende hvis du ønsker å beholde tilgangen til profilen din etter at du har logget ut av klienten eller økten din har utløpt.
Først, klikk på "innstillinger"-ikonet representert ved et tannhjul
![Innstilling](assets/9.webp)

Deretter kopierer og limer du inn en etter en din npub, npub hex, nsec, og nsec hex inn i en tekstfil som du vil holde sikker. Jeg anbefaler å kryptere denne filen hvis du vet hvordan du gjør det.

![Nøkkel](assets/10.webp)

> ⚠️ Merk deg advarselen som iris gir deg. Mens du kan dele din offentlige nøkkel uten frykt, er det en annen historie for din private nøkkel. Alle som har sistnevnte vil kunne få tilgang til kontoen din.

## Konklusjon

Der har du det, lille struts, du har tatt dine første skritt på Nostr. Nå trenger du å lære å løpe i lynets hastighet. Vi vil snart publisere guider som vil vise deg hvordan du håndterer nøklene dine og hvordan du integrerer lyn i din Nostr-opplevelse ved hjelp av getalby.