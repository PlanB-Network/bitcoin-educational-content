---
name: Lipa
description: Sette opp og bruke den mobile lommeboken Lipa lightning
---
![cover](assets/cover.webp)

En Bitcoin Lightning-lommebok er en mobilapplikasjon som muliggjør umiddelbare, rimelige transaksjoner på Bitcoins Lightning-nettverk. I motsetning til transaksjoner på hovedblokkjeden (on-chain) er Lightning-betalinger nesten øyeblikkelige og krever minimale avgifter, noe som gjør dem spesielt egnet for små, daglige betalinger.

Lynlommebøker, som alle mobile lommebøker, regnes som "varme" lommebøker fordi de er koblet til Internett. De er derfor først og fremst beregnet på å håndtere små pengebeløp til daglig bruk. For større beløp er det å foretrekke å bruke sikrere lagringsløsninger som maskinvare-lommebøker.

Hvis du vil lære mer om Lightning-nettverket og forstå hvordan det fungerer rent teknisk, anbefaler jeg at du tar dette kurset:

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
I denne veiledningen tar vi en titt på **Lipa**, en enkel og effektiv lynlommebok utviklet i Sveits.

## Vi presenterer Lipa

Lipa er en ikke-frihetsberøvende lynlommebok som kjennetegnes av enkel bruk og et ryddig grensesnitt. Den er utviklet av et sveitsisk team, og legger vekt på konfidensialitet og brukervennlighet for nybegynnere.

Viktige funksjoner inkluderer:


- Intuitivt brukergrensesnitt
- Autonom styring av Lightning-kanaler
- Støtte for LNURL-protokollen
- Mulighet for å kjøpe bitcoins direkte i applikasjonen

## Installere og konfigurere Lipa

Det første trinnet er å laste ned Lipa-appen. For øyeblikket er den bare tilgjengelig på iOS :


- [For Apple] (https://apps.apple.com/app/lipa-bitcoin-lightning/id1602180066)

Android-versjonen er under utvikling og vil snart være tilgjengelig.

![Installation de Lipa](assets/fr/01.webp)

Når du har startet applikasjonen, kommer du til startskjermen, som tilbyr deg to alternativer:


- Opprett en ny portefølje
- Gjenopprett en eksisterende portefølje fra en sikkerhetskopi

Når du har valgt et alternativ, ber programmet deg om å aktivere varslinger. Dette trinnet er viktig, ettersom varslinger er nødvendige for :


- Motta varsler når betalinger mottas, selv når applikasjonen er lukket
- Bli informert om trinnene som er involvert i å kjøpe bitcoin via deres integrerte løsning

Deretter presenteres programmets hovedfunksjoner gjennom en rekke introduksjonsskjermbilder:


- Sømløs betalingskvittering**: Brukere kan motta Bitcoin-betalinger selv når applikasjonen er lukket, noe som garanterer pålitelighet og bekvemmelighet.
- Lightning-adresser uten frihetsberøvelse**: Lipa støtter nå ikke-frihetsberøvende Lightning-adresser, noe som forbedrer personvernet og sikkerheten ved å gi brukerne full kontroll over bitcoinsene sine.
- Kontroll over analysedata** : Med åpenhet og konfidensialitet i høysetet kan brukerne se hvilke typer data som samles inn, og velge hvilke data de ønsker å dele.
- Send via telefonnummer**: Ingen behov for komplekse adresser - bare velg en kontakt, angi beløpet, og send bitcoins direkte til telefonnummeret deres.

Applikasjonen drar også nytte av kontinuerlige forbedringer når det gjelder stabilitet, sikkerhet og pålitelighet, for å garantere en optimal brukeropplevelse.

## Navigasjon i applikasjonen

Lipas grensesnitt er organisert rundt fire hovedfaner som er tilgjengelige via navigasjonslinjen nederst på skjermen:

![Navigation principale](assets/fr/02.webp)


- Hjem**: Viser din nåværende saldo og transaksjonshistorikk
- Skanner**: Lar deg skanne QR-koder for å foreta betalinger
- Kart**: Viser et interaktivt kart over Bitcoin-aksepterende virksomheter i ditt område
- Innstillinger**: Tilgang til programinnstillinger, sikkerhetskopiering og preferanser

Du får tilgang til en ekstra meny ved å trekke ned startskjermen:

![Menu supplémentaire](assets/fr/03.webp)

Denne bevegelsen avslører tilleggsfunksjoner som f.eks:


- Kjøpe bitcoins
- Bitcoin-innskudd i kjeden
- Opprette Lightning-fakturaer for å motta bitcoins
- Lynbetaling av fakturaer

## Lagre porteføljen din

For å sikkerhetskopiere lommeboken din, gå til "Innstillinger" -fanen og velg "Gjenopprettingsfrase". Lipa bruker en gjenopprettingsfrase som det er viktig å skrive ned nøye på et fysisk medium (papir, metall). Denne setningen er den eneste måten å gjenopprette pengene dine hvis telefonen din går tapt eller blir stjålet. For å validere sikkerhetskopien din, vil applikasjonen be deg om å bekrefte 3 tilfeldige ord fra frasen din.

![Backup](assets/fr/04.webp)

Hvis du vil ha mer informasjon om hvordan du sikkerhetskopierer og administrerer gjenopprettingsfrasen din på riktig måte, anbefaler jeg på det sterkeste å følge denne andre veiledningen, spesielt hvis du er nybegynner:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
## Motta bitcoins

For å motta bitcoins har du to alternativer. For å få tilgang til disse alternativene, går du tilbake til startskjermen og trekker ned skjermen. Deretter kan du enten :


- Velg "Transfer BTC" for å motta bitcoins i kjeden. Deretter skanner du bare QR-koden med den andre lommeboken din og fullfører transaksjonen.
- Velg "Request" for å motta via Lightning-nettverket, og angi beløpet du ønsker å motta.

I begge tilfeller må du betale et gebyr som tilsvarer 0,4 % av beløpet, eller rundt 2500 sats hvis applikasjonen må åpne en ny betalingskanal (noe som uunngåelig vil være tilfelle for den første betalingen).

![Recevoir des bitcoins on chain](assets/fr/05.webp)

![Recevoir des bitcoins lightning](assets/fr/06.webp)

## Send bitcoins

For å sende bitcoins går du til startskjermen, trekker ned skjermen og velger "Betal". Deretter trykker du bare enten :


- skriv inn en lyn-LNURL-adresse
- skann en lyn QR-kode for å utføre betalingen.

Du kan også gå til den andre fanen nederst på skjermen for å skanne en QR-kode direkte.

![Envoi de bitcoins](assets/fr/07.webp)

## Kjøp bitcoins

Lipa tilbyr muligheten til å kjøpe bitcoins direkte i applikasjonen mot et gebyr på 1,5%. For å gjøre et kjøp, gå til startskjermen og trekk ned for å vise menyen. Velg deretter "Kjøp BTC". Tre introduksjonsskjermbilder vil veilede deg gjennom kjøpsprosessen.

![Menu d'achat](assets/fr/08.webp)

Deretter er det bare å legge inn bankopplysningene til kontoen du vil bruke til å gjennomføre kjøpet. Velg valuta og skriv inn e-postadressen din.

Etter innlastingsskjermen finner du referansenummeret som skal inkluderes i overføringen du skal foreta, samt bankopplysningene for vekslingen.

![Sélection du montant](assets/fr/09.webp)

Alt du trenger å gjøre er å bruke banken din til å overføre det ønskede beløpet, sette opp overføringen ved å angi RIB tidligere hentet og angi referansen på transaksjonstidspunktet, slik at Lipa kan knytte denne bankbevegelsen til Lipa-lommeboken din.

![Confirmation d'achat](assets/fr/10.webp)

## Fordeler og ulemper

### Fordeler


- Intuitivt grensesnitt
- Korrekte serviceavgifter
- Ikke-depot
- Integrert løsning for bitcoin-kjøp
- Integrering av BTCmap
- NFC-støtte

### Ulemper


- Det er ikke mulig å sende bitcoins på kjeden
- Litt lengre betaling enn gjennomsnittet

Lipa er et utmerket valg for å komme i gang med Lightning-nettverket, og egner seg spesielt godt for brukere som er ute etter en enkel løsning for hverdagsbetalinger. Det brukervennlige og oversiktlige grensesnittet gjør den til en ideell lommebok for nybegynnere, samtidig som den tilbyr de viktigste funksjonene for daglig bruk av Lightning.

## Ressurser


- [Lipas offisielle nettside] (https://lipa.swiss/)
- [Lipa-støtte] (https://getlipa.atlassian.net/servicedesk/customer/portal/1)