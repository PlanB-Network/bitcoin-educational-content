---
name: Blitz Wallet
description: Den enkleste Bitcoin-lommeboken.
---

![cover](assets/cover.webp)

Brukeropplevelsen er en av de avgjørende faktorene når man velger en Bitcoin-lommebok. I denne veiledningen presenterer vi Blitz Wallet, en lommebok som setter enkelhet i sentrum av sin tilnærming: takket være integrasjonen av **Spark**-protokollen, gir Blitz deg en av de enkleste og mest komplette Bitcoin-lommebøkene på markedet, med øyeblikkelige betalinger og uten teknisk administrasjon.

## Hva er Blitz Wallet?

Blitz Wallet er en **self-custodial** og **open source** Bitcoin-lommebok som satser på din suverenitet og en smidig og intuitiv brukeropplevelse.

[Blitz Wallet](https://blitz-wallet.com/) er en mobilapplikasjon tilgjengelig på Android (Play Store) og iOS (App Store).

I motsetning til tradisjonelle Lightning-lommebøker som krever at du administrerer betalingskanaler og innkommende likviditet, bruker Blitz Wallet **Spark-protokollen** for å eliminere disse tekniske kompleksitetene. Resultatet: øyeblikkelige betalinger fra den første satoshi du mottar, uten noen forhåndskonfigurasjon. Målet med Blitz er å gjøre bitcoin-betalinger like enkle som en vanlig betalingsapp, uten noensinne å kompromittere self-custody over midlene dine.

Blitz Wallet støtter også **lesbare adresser** i formatet `bruker@domene.com` (via LNURL), noe som gjør det mulig å sende bitcoin like enkelt som en e-post, uten å måtte håndtere lange invoices eller QR codes for hver transaksjon.

## Forstå Spark-protokollen

Før vi går videre til praksis, er det nyttig å forstå teknologien som driver Blitz Wallet under panseret: **Spark-protokollen**.

### Hva er Spark?

Spark er en open source overlaggsprotokoll bygget på Bitcoin, utviklet av teamet hos Lightspark. Den gjør det mulig å utføre øyeblikkelige transaksjoner med lave kostnader, samtidig som self-custody over dine bitcoin bevares.

I motsetning til Lightning Network som er basert på **betalingskanaler** mellom to parter, bruker Spark en teknologi kalt **statechain** (tilstandskjede). Det grunnleggende prinsippet er som følger: i stedet for å flytte bitcoin på blokkjeden for hver transaksjon, overfører Spark **retten til å bruke** fra én bruker til en annen, uten on-chain-bevegelser.

### Hvordan fungerer det?

For å forstå Spark på en intuitiv måte, la oss forestille oss at det å bruke en bitcoin på Spark krever at man fullfører et puslespill med to brikker:
- Én brikke holdes av brukeren (for eksempel Alice).
- Den andre brikken holdes av en gruppe operatører kalt **Spark Entity (SE)**.

Bare kombinasjonen av de to tilhørende brikkene gjør det mulig å bruke bitcoinene.

Når Alice vil sende sine bitcoin til Bob, skjer følgende: et nytt puslespill opprettes i fellesskap mellom Bob og SE. Puslespillet beholder samme form, men brikkene som utgjør det endres. Nå er det Bobs brikke som passer med SEs brikke. Alices gamle brikke blir ubrukelig, fordi SE har destruert sin tilhørende brikke. Eierskapet til bitcoinene har skiftet hender, **uten noen transaksjon på blokkjeden**.

Bob kan deretter gjenta den samme prosessen for å sende disse bitcoinene til Carol, og så videre. Hver overføring fungerer ved å erstatte brikkene i puslespillet, ikke ved en on-chain pengeoverføring.

### Hvorfor er det sikkert?

Et legitimt spørsmål melder seg: hva skjer hvis SE faktisk ikke destruerer sin gamle brikke?

Spark Entity er ikke en enkelt enhet: det er en gruppe av uavhengige operatører. SEs brikke holdes aldri av én enkelt operatør. Erstatningen av puslespillet krever samarbeid fra flere operatører. Det er nok at **én enkelt operatør er ærlig** under en overføring for å forhindre reaktivering av et gammelt puslespill. Ingen enkelt operatør kan i hemmelighet beholde et gammelt aktivt puslespill eller gjenskape det senere.

I tillegg inkluderer Spark en ensidig uttrekksmekanisme: du kan alltid hente ut dine bitcoin on-chain uten samarbeid fra SE. Denne sikkerhetsmekanismen er en integrert del av Spark-arkitekturen, og garanterer at du aldri er avhengig av nettverket for å få tilgang til midlene dine.

### Spark vs Lightning Network

Spark og Lightning konkurrerer ikke: de er **komplementære**. Blitz Wallet integrerer begge, noe som lar deg dra nytte av fordelene med hver av dem.

|                               | **Spark**                      | **Lightning Network**  |
| ----------------------------- | ------------------------------ | ---------------------- |
| **Teknologi**                 | Statechains (tilstandskjeder)  | Betalingskanaler       |
| **Kanaladministrasjon**       | Ikke nødvendig                 | Nødvendig              |
| **Innkommende likviditet**    | Ikke nødvendig                 | Nødvendig              |
| **Øyeblikkelige transaksjoner** | Ja                          | Ja                     |
| **Self-custody**              | Ja                             | Ja                     |
| **Lightning-kompatibilitet**  | Ja (via atomic swaps)          | Nativt                 |

Lightning Network er fortsatt en utmerket protokoll for øyeblikkelige betalinger, men den medfører tekniske begrensninger (kanaladministrasjon, innkommende likviditet, node som må være tilkoblet...) som kan bremse nybegynnere. Spark fjerner disse begrensningene, samtidig som den forblir kompatibel med Lightning.

## Installasjon og konfigurasjon

I denne veiledningen tar vi utgangspunkt i Android-versjonen av Blitz Wallet, men alle prosessene som presenteres nedenfor gjelder også for iOS.

![installation](assets/fr/01.webp)

Siden Blitz Wallet er en self-custody-lommebok, kan du velge mellom å **opprette en ny lommebok** eller **importere en gjenopprettingsfrase** (12 eller 24 ord) fra en eksisterende lommebok.

Her går vi for opprettelse av en ny lommebok. Nedenfor finner du våre anbefalinger for sikkerhetskopiering av gjenopprettingsfrasen din:

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

❗ **VIKTIG**: Disse 12 eller 24 gjenopprettingsordene er **den eneste tilgangsnøkkelen til dine bitcoin**. Blitz er en self-custodial lommebok: verken Blitz eller Spark har tilgang til gjenopprettingsfrasen din eller midlene dine. Hvis du mister disse ordene, vil du permanent miste tilgangen til dine bitcoin. Del dem ikke med noen: enhver som har dem kan bruke dine bitcoin.

Opprett deretter en **PIN-kode** for å sikre tilgangen til lommeboken din.

![setup-wallet](assets/fr/02.webp)

## Komme i gang med Blitz

Å utføre transaksjoner med Blitz er mer intuitivt enn i de fleste andre Bitcoin-lommebøker. Grensesnittet er minimalistisk og sentrert rundt tre hovedhandlinger: sende, skanne og motta.

### Motta bitcoin

For å motta bitcoin i Blitz-lommeboken din, trykk på **«Pil ned»**-ikonet (↓), skriv inn beløpet i satoshi du ønsker å motta, legg til en valgfri beskrivelse, og lommeboken vil generere en faktura (invoice) som du kan dele med avsenderen.

⚠️ **MERK**: Satoshi (eller «sat») er den minste enheten av bitcoin: **1 bitcoin = 100 000 000 satoshi**.

En av særegenhetene med Blitz Wallet er at den støtter flere nettverk og protokoller i Bitcoin-økosystemet:

- **Lightning Network**: Et av Bitcoins overlagringslag som gjør det mulig å utføre mikrobetalinger øyeblikkelig med svært lave gebyrer. Ideelt for små daglige beløp.

- **Bitcoin (on-chain)**: Hoveblokkjeden i Bitcoin-protokollen, tilpasset for transaksjoner med større beløp der maksimal sikkerhet og endelig oppgjør er prioritert.

- **Liquid Network**: En sidechain (parallellkjede) til Bitcoin utviklet av Blockstream, som muliggjør raske og konfidensielle transaksjoner ved bruk av Liquid Bitcoin (L-BTC).

https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

Som standard genererer Blitz en Lightning-faktura, men du kan velge hvilket nettverk du ønsker å motta satoshiene dine på ved å trykke på knappen **«Choose format»** (Velg format).

![receive-sats](assets/fr/03.webp)

### Opprette kontakter

Blitz Wallet forenkler gjentakende bitcoin-sendinger takket være sitt kontaktsystem.

I **Contacts**-menyen kan du lagre Blitz-brukernavn eller Lightning-adresser (LNURL) som du samhandler med ofte.

Du kan dermed sende satoshi til disse adressene med noen få trykk, uten å måtte skanne en QR code eller manuelt taste inn en adresse hver gang.

### Sende bitcoin

I tillegg til de klassiske metodene for å sende bitcoin (skanning av QR code, manuell inntasting av adresse), tilbyr Blitz flere praktiske alternativer:

- **Fra et bilde** (*From Image*): Importer en QR code fra bildegalleriet ditt.
- **Fra utklippstavlen** (*From Clipboard*): Lim inn en adresse eller faktura du har kopiert tidligere.
- **Manuell inntasting** (*Manual Input*): Skriv inn en Bitcoin-adresse, en Lightning-faktura eller en lesbar adresse direkte (for eksempel `bruker@walletofsatoshi.com`).
- **Fra kontaktene dine**: Velg en forhåndsregistrert mottaker for å sende med noen få trykk.

I **Wallet**-menyen, trykk på knappen **«Pil opp»** (↑), velg sendemetode, skriv inn beløpet du vil sende, legg til en beskrivelse og bekreft transaksjonen.

Minimumsbeløpet for å gjennomføre en sending er for tiden **1 000 satoshi**.

![send-bitcoin](assets/fr/05.webp)

## Blitz-butikken

Utover bitcoin-overføringer har Blitz Wallet en integrert butikk der du kan bruke dine bitcoin til å kjøpe digitale tjenester direkte fra applikasjonen.

Fra hovedmenyen, trykk på fanen **Store** for å få tilgang til butikken. Der finner du også tilgang til plattformen **Bitrefill**, som lar deg kjøpe gavekort hos tusenvis av forhandlere over hele verden, direkte med bitcoin.

- **Kunstig intelligens**: Få tilgang til de nyeste generative AI-modellene (Claude 3.5 Sonnet, GPT-4o, GPT-4o-mini, Gemini Flash 1.5) og betal kredittene dine direkte i satoshi. Flere abonnementer er tilgjengelige etter dine behov (Casual, Pro, Power).

![ia-credits](assets/fr/06.webp)

- **Anonyme SMS**: Send og motta SMS over hele verden uten å avsløre ditt personlige telefonnummer. Tjenesten faktureres i satoshi for hver sendt melding.

![sms-credit](assets/fr/07.webp)

- **VPN WireGuard**: Beskytt personvernet ditt på nett ved å abonnere på en VPN WireGuard-tjeneste (ukentlig, månedlig eller kvartalsvis), betalbar med bitcoin direkte fra Blitz-butikken. Du trenger bare å laste ned WireGuard-klientappen på enheten din for å ta den i bruk.

![wireguard](assets/fr/08.webp)

https://planb.academy/tutorials/exchange/centralized/bitrefill-8c588412-1bfc-465b-9bca-e647a647fbc1

## Blitz Wallet bak kulissene: gå dypere

Bak den enkle bruken av Blitz Wallet skjuler det seg en gjennomtenkt teknisk arkitektur som kombinerer flere lag i Bitcoin-økosystemet.

### Fordelingen av saldoen din

Blitz Wallet administrerer saldoen din på en transparent måte ved å fordele midlene dine mellom de ulike protokollene etter behov. Når saldoen din er under 500 000 satoshi, bruker Blitz **Liquid Network** og atomic swaps for å gi deg en smidig opplevelse og muliggjøre transaksjoner på Lightning Network selv med små beløp.

Denne tilnærmingen sikrer en enkel start for nye brukere, uten at de trenger å forstå de underliggende mekanismene. Du kan se fordelingen av saldoen din mellom de ulike lagene i menyen **Innstillinger > Balance Info**.

![balance](assets/fr/09.webp)

### Lightning-modus (valgfritt)

Som standard bruker Blitz Wallet Liquid Network og Spark-protokollen for å gi deg en smidig opplevelse uten teknisk konfigurasjon. Blitz gir deg imidlertid muligheten til å aktivere **Lightning-modus**, som automatisk vil åpne en betalingskanal når du når en saldo på **500 000 satoshi** (0,005 BTC).

For å aktivere Lightning-modus, gå til **Innstillinger**, deretter under seksjonen **Tekniske innstillinger**, trykk på alternativet **Node Info**.

![enable-lightning](assets/fr/10.webp)

Takket være Spark-protokollen er denne aktiveringen **valgfri**: Spark gjør det allerede mulig å utføre Lightning-kompatible betalinger uten å måtte åpne en kanal eller administrere innkommende likviditet. Nativ Lightning-modus er fortsatt nyttig for avanserte brukere som ønsker å ha sin egen Lightning-node integrert i applikasjonen.

### Utsalgssted (PoS)

Blitz Wallet har en integrert **utsalgssted**-funksjon som lar forhandlere akseptere bitcoin-betalinger direkte fra applikasjonen.

I menyen **Innstillinger > Point-of-sale** kan du konfigurere:

- Den unike identifikatoren for butikken din
- Den lokale fiatvalutaen som prisene skal vises i
- Instruksjoner for de ansatte
- Drikkepenge-alternativet for kundene dine

Kundene dine trenger bare å skanne den genererte QR code-en for å utføre sin bitcoin-betaling øyeblikkelig.

![pos](assets/fr/11.webp)

https://planb.academy/tutorials/wallet/mobile/speed-wallet-8715e454-1720-4a7f-8c1d-3da02cf67312

Ressurser brukt for å skrive denne veiledningen:
- Bloggen til [Breez](https://breez.technology/) Technology: [*Spark Explained Like You're Five*](https://blog.breez.technology/spark-explained-like-youre-five-8d554aad18d0).
