---
name: Minibits Wallet
description: Veiledning for Minibits Wallet
---

![cover](assets/cover.webp)


I denne veiledningen går jeg gjennom hvordan du konfigurerer Minibits Wallet til å bruke ecash. En kraftig personvernfokusert betalingsteknologi som fungerer sammen med Bitcoin. Minibits er en ecash og Lightning Wallet som muliggjør øyeblikkelige, billige og private verdioverføringer, noe som gjør den ideell for hverdagstransaksjoner der personvernet er viktig.


Før vi dykker ned i Minibits, må vi først etablere en klar forståelse av hva ecash er og ikke er. Mange forveksler ecash med Bitcoin- eller Blockchain-teknologi, men de er fundamentalt forskjellige konsepter.


Ecash er IKKE Bitcoin. Den erstatter ikke din selvforvaltende Bitcoin Wallet, men utfyller den. Ecash er IKKE en Blockchain og lever IKKE på noen offentlig Ledger. Interessant nok er ecash IKKE en ny teknologi - den er faktisk eldre enn det verdensomspennende nettet, med konsepter som ble utviklet på 1980- og 1990-tallet.


Hva ecash ER: utrolig privat (transaksjoner etterlater ingen sporbar historikk), peer-to-peer (direkte overføringer uten mellomledd), og fungerer som et digitalt ihendehaverinstrument (hvis du eier det, kontrollerer du det). En viktig fordel er at ecash KAN brukes offline - enten avsender eller mottaker kan være frakoblet internett under transaksjoner. Ecash KAN utstedes av en enkelt part eller av en føderasjon av betrodde enheter, og det ER en perfekt komplementær teknologi til Bitcoin, som håndterer små, hyppige transaksjoner mens Bitcoin fungerer som oppgjørs-Layer.


Vær oppmerksom på at dette Minibits-oppsettet representerer en "depotløsning", noe som betyr at du stoler på at Mint-operatøren forvalter midlene dine. Dette medfører spesifikke risikoer som du må forstå før du fortsetter.


Prosjektet viser denne viktige ansvarsfraskrivelsen:


- Denne Wallet skal kun brukes til forskningsformål.
- Wallet er en betaversjon med ufullstendig funksjonalitet og både kjente og ukjente feil.
- Ikke bruk den med store mengder ecash.
- Ecash lagret i Wallet er utstedt av myntverket
- du stoler på at myntverket vil støtte den med Bitcoin til du overfører beholdningen din til en annen Bitcoin-lyn Wallet.
- Cashu-protokollen som Wallet implementerer, har ennå ikke vært gjenstand for omfattende gjennomgang eller testing.


Behandle Minibits som en hverdags-Wallet, ikke som en sparekonto, og lagre aldri store verdier her.


## 1️⃣ Sette opp din Wallet


Du kan begynne med å gå til [Minibits Website](https://www.minibits.cash/), der du finner nedlastingsalternativer for alle større plattformer. iOS-brukere kan laste ned fra [App Store](https://testflight.apple.com/join/defJQgTD), mens iOS-brukere i EU har muligheten til å installere fra [Freedom Store](https://freedomstore.io/). Android-brukere kan hente appen fra [Google Play Store](https://play.google.com/store/apps/details?id=com.minibits_wallet) eller laste ned APK-filen direkte fra siden [GitHub Releases](https://github.com/minibits-cash/minibits_wallet/releases).


Når du installerer Minibits, vil du se introduksjonsskjermbilder som forklarer de grunnleggende konseptene - du kan lese gjennom disse eller hoppe over dem hvis du allerede er kjent med teknologien. Når du har fullført disse innledende trinnene, blir du bedt om å velge mellom:


- `Gjør det, ta meg til Wallet` for nye brukere eller
- gjenopprett tapte Wallet` hvis du gjenoppretter fra en sikkerhetskopi.


![image](assets/en/01.webp)

Etter at du har fullført det første oppsettet, kommer du til startskjermen, som har flere viktige Elements ting å legge merke til. profilikonet øverst i hjørnet tar deg til profilsiden din, der du kan få tilgang til dine Minibits Wallet Address og velge `batch mottak`-alternativer. ② I midten av skjermen ser du myntene du kan bruke, og Minibits-mynten er valgt som standard. ③ Handlingsraden nedenfor gir deg alternativer for å sende ecash- eller lynbetalinger, skanne en QR-kode og motta betalinger. ④ Til slutt inneholder den nederste navigasjonslinjen snarveier til startskjermen, transaksjonshistorikk, kontakter og innstillinger.


![image](assets/en/02.webp)


## 2️⃣ Administrer mynter


Som standard er Minibits myntenhet aktivert når du starter appen. En av styrkene til ecash er imidlertid muligheten til å bruke flere mynter for økt desentralisering og sikkerhet. For å legge til en ny mynte, naviger til "Innstillinger", velg deretter "Administrer mynter", og trykk til slutt på "Legg til mynte".


[Bitcoinmints.com] (Bitcoinmints.com) gir en omfattende liste over tilgjengelige mynter med brukervurderinger for å hjelpe deg med å velge anerkjente alternativer. Bruk av flere myntverk reduserer risikoen. Hvis en myntutsteder opplever problemer, forblir pengene dine på andre myntutstedere tilgjengelige.


![image](assets/en/04.webp)


## 3️⃣ Opprette en sikkerhetskopi


Sikkerhetskopiering er uten tvil det mest kritiske trinnet i hele installasjonsprosessen. For å få tilgang til alternativene for sikkerhetskopiering, naviger til `Innstillinger`-> `Backup` Her finner du to viktige alternativer:

1. "Din seed-frase", som inneholder "12 ord" som gjør at du kan gjenopprette ecash-saldoen din i tilfelle tap av enheten. Denne seed-frasen er din hovednøkkel til alle ecash på tvers av alle mynter du har lagt til. Skriv den ned på et fysisk medium (papir eller metall), og oppbevar den sikkert på flere steder. seed-frasen må aldri lagres digitalt der den kan bli kompromittert. Besøk denne [veiledningen] (https://planb.network/en/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270) for beste praksis for å beskytte din Wallet.

2. `Wallet backup` som inneholder en lang backup-streng.


**Attention**: Du trenger fortsatt seed-frasen din når du bruker denne sikkerhetskopien til å gjenopprette Wallet.


![image](assets/en/05.webp)


## 4️⃣ Create Minibits Wallet Address


Deretter navigerer du til `Kontakter` nederst og tilpasser din dedikerte `Minibits Wallet Address` ved å trykke på `Endre` -> `Endre Wallet Address`. Skriv inn ønsket Address og sjekk tilgjengelighet.


![image](assets/en/07.webp)


Etter at du har angitt Address, blir du bedt om å gi en liten "donasjon" for å støtte prosjektet. Dette er valgfritt, men jeg anbefaler på det sterkeste at du gjør det hvis du planlegger å bruke tjenesten regelmessig. Open source-prosjekter som Minibits er avhengige av støtte fra fellesskapet for å kunne fortsette utviklingen og vedlikeholdet. Selv et lite bidrag bidrar til å sikre prosjektets levetid.


![image](assets/en/08.webp)


## 5️⃣ Nostr-oppsett


Hvis du ønsker å tipse folk du følger på Nostr, kan du legge til npub-nøkkelen din ved å velge Kontakter og deretter Offentlig. Dette kobler Minibits Wallet til det sosiale nettverket Nostr, slik at du kan tipse sømløst.


Du har også muligheten til å `Bruke din egen profil` ved å gå til `Innstillinger` og deretter `Privacy` for å importere din egen Nostr Address og nøkkel. Vær imidlertid oppmerksom på at dette vil stoppe din Wallet fra å kommunisere med minibits.cash Nostr og LNURL Address-servere, noe som deaktiverer lyn Address-funksjoner for mottak av zaps og betalinger.


![image](assets/en/09.webp)


## 6️⃣ Motta midler


For å motta penger må du først fylle opp Wallet via en lyn-Invoice. Denne prosessen er enkel: trykk på `Topup` , skriv inn `Amount` du vil legge til, legg eventuelt til en `Memo` , og trykk deretter på `Create Invoice`. Du må deretter betale denne Invoice med en annen Lightning Wallet, som konverterer Bitcoin Lightning-betalinger til ecash-tokens i din Minibits Wallet.


![image](assets/en/10.webp)


## 7️⃣ Send midler


Nå som du har finansiert Wallet, kan du sende penger på to forskjellige måter.


### Send ecash


Det første alternativet er å sende ecash direkte. Trykk på "Send", velg deretter "Send ecash", skriv inn "Beløp" og trykk på "Opprett token." Dette vil generate gi deg en QR-kode som du kan dele med mottakeren eller få dem til å skanne direkte med enheten sin. Mottakeren vil se symbolene vises i Wallet nesten umiddelbart, uten Blockchain gebyrer eller bekreftelsesforsinkelser.


![image](assets/en/11.webp)


### Betal med Lightning


Det andre alternativet er å betale via Lightning. Trykk på `Send` , og velg deretter `Betal med Lightning`. Du kan velge fra Nostr-kontaktene dine (hvis du har koblet til npuben din), eller skrive inn/lim inn en Lightning Address-, Invoice- eller LNURL-betalingskode ved hjelp av alternativet "Lim inn" eller "Skann". Etter at du har "bekreftet" mottakeren, blir du bedt om å angi "Beløp å betale", eventuelt legge til et memo, og deretter trykke på "Bekreft" etterfulgt av "Betal nå" for å fullføre Lightning-transaksjonen.


![image](assets/en/12.webp)


## 8️⃣ Opprett en NWC-tilkobling


En annen kraftig funksjon i Minibits er muligheten til å opprette `Nostr Wallet Connect (NWC)`-tilkoblinger, som gjør det mulig for andre programmer å be om betalinger fra Wallet uten å eksponere de private nøklene dine.


For å konfigurere dette går du til `Innstillinger`, velger `Nostr Wallet Connect`, og trykker på `Legg til tilkobling`. Gi tilkoblingen et beskrivende navn som identifiserer både applikasjonen og den tilknyttede brukerkontoen. Angi en rimelig maksimal daglig grense for å kontrollere hvor mye som kan brukes gjennom denne tilkoblingen, og trykk deretter på "Lagre" for å fullføre oppsettet.


Denne funksjonen er spesielt nyttig for tjenester som Nostr Clients, der du ønsker å aktivere automatisk tipsing uten å måtte godkjenne hver transaksjon manuelt.


![image](assets/en/12.webp)


## 🎯 Konklusjon


Minibits er en lett tilgjengelig inngangsport til en verden av ecash, og tilbyr personvernfokuserte betalinger som utfyller Bitcoin-beholdningen din. Husk å alltid ta sikkerhetskopier, vurder å bruke flere mynter for redundans, og lagre kun passende mengder i denne depotløsningen.


For ytterligere ressurser, sjekk ut Minibits GitHub-depotet, den offisielle nettsiden og Telegram-kanalen deres, der fellesskapet aktivt diskuterer utvikling og feilsøking av problemer


- [Github] (https://github.com/minibits-cash/minibits_wallet)
- [Nettsted] (https://www.minibits.cash/)
- [Telegram] (https://t.me/MinibitsWallet)


Økosystemet for ecash er fortsatt under utvikling, men verktøy som Minibits gjør denne kraftige personvernteknologien stadig mer tilgjengelig for vanlige brukere.