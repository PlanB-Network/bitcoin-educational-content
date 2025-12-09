---
name: Macadamia Wallet
description: Cashu mobile wallet for anonyme og øyeblikkelige BTC-betalinger
---

![cover](assets/cover.webp)



Macadamia Wallet er en iOS-mobil wallet som implementerer Cashu-protokollen, et Chaumian ecash-system som muliggjør helt anonyme Bitcoin-betalinger. Takket være blindsignaturer kan ingen observatører koble innskuddene dine til utgiftene dine, noe som gir konfidensialitet på linje med fysiske kontanter.



I denne veiledningen ser vi på hvordan du installerer og konfigurerer Macadamia, utfører dine første Cashu-transaksjoner (Mint, Send, Receive, Melt) og administrerer flere mynter for å sikre pengene dine.



## Hva er Macadamia Wallet?



### Cashu-protokollen



Cashu bruker blindsignaturer oppfunnet av David Chaum: Du setter inn bitcoins hos en "mint"-server, som utsteder tilsvarende tokens i satoshier. Myntserveren signerer disse tokens uten å se innholdet, noe som gjør det umulig å knytte en token til en bruker. Utvekslingen er off-chain, peer-to-peer og helt ugjennomsiktig - selv mynten kan ikke spore hvem som betaler hvem.



Macadamia er en åpen kildekode wallet iOS utviklet i Swift/SwiftUI. Den fungerer uten konto eller KYC, tokens lagres lokalt og beskyttes av en seed-frase. Koden kan revideres på GitHub, og tokens er interoperable med andre Cashu-lommebøker (Minibits, Cashu.me).



### Forvaltningsmodell og kompromiss



**Viktig**: Cashu opererer på en depotmodell. Jetongene er betalingsforpliktelser (IOUs) støttet av myntverkets Bitcoin-reserver. Hvis myntverket forsvinner, mister tokens sin verdi. Dette er kompromisset for maksimal konfidensialitet.



Bruk Macadamia som en fysisk wallet: kun små mengder. Spre midlene dine over flere mynter for å fortynne risikoen.



## Hovedfunksjoner



Macadamia implementerer de fire grunnleggende operasjonene i Cashu-protokollen. **Mint** konverterer satoshiene dine til tokens via en lynfaktura. **Send** lar deg sende tokens gratis via QR-kode eller lenke, helt off-chain. **Receive** lar deg motta tokens eller generate en Lightning-faktura. **Melt** betaler en lynfaktura ved å ødelegge symbolene dine.



wallet støtter administrasjon av flere mynter samtidig. Du kan bytte tokens mellom forskjellige mynter via Lightning.



## Støttede plattformer



Macadamia er kun tilgjengelig på iOS 17 eller nyere for iPhone og iPad. Den opprinnelige Swift/SwiftUI-applikasjonen gir optimal integrasjon med Apples økosystem.



Cashu-protokollen garanterer interoperabilitet mellom lommebøker. Du kan gjenopprette seed-frasen din i andre applikasjoner, for eksempel Minibits på Android eller Nutstash på PC.



Den nåværende versjonen distribueres via TestFlight. Bruk kun små mengder med denne betaversjonen.



## Installasjon



Macadamia er for øyeblikket tilgjengelig via TestFlight, Apples betatestingsprogram. Her kan du se hvordan du installerer den:



### Installasjon via TestFlight



**Trinn 1: Last ned TestFlight**



Hvis du ikke allerede har TestFlight-appen på enheten din, kan du søke etter "TestFlight" i App Store og installere den. TestFlight er Apples offisielle applikasjon for testing av betaversjoner av iOS-applikasjoner.



**Trinn 2: Bli med i Macadamia beta-program** (på fransk)



Når TestFlight er installert, følger du denne invitasjonslenken fra din iPhone eller iPad: [https://testflight.apple.com/join/RMU6PaRu](https://testflight.apple.com/join/RMU6PaRu)



Koblingen åpner automatisk TestFlight og tilbyr deg å installere Macadamia Wallet. Trykk på "Godta" og deretter på "Installer" for å starte nedlastingen. Programmet veier rundt ti megabyte og tar bare noen sekunder å installere.



![Installation TestFlight](assets/fr/01.webp)



### Viktig informasjon om betaversjoner



Macadamia er fortsatt i en aktiv utviklingsfase. TestFlight-versjoner oppdateres ofte og kan introdusere nye funksjoner eller rette feil. Som med alle betaversjoner kan det imidlertid oppstå feil. **Vi anbefaler på det sterkeste at du bare bruker små mengder**, som du aksepterer kan gå tapt i tilfelle et teknisk problem.



Macadamia samler ikke inn noen brukerdata i henhold til den viste personvernerklæringen. Sørg for å sjekke at utvikleren er cypherbase UG når du installerer.



## Opprinnelig konfigurasjon



Ved første oppstart genererer Macadamia en BIP-39 setning med 12 ord. Skriv dem ned på et trygt sted - aldri som et skjermbilde. Med disse ordene kan du gjenskape wallet og bruke jetongene dine.



![Configuration initiale](assets/fr/02.webp)



Følg de fire trinnene: Velkommen, godta vilkår, lagre seed-setning og endelig bekreftelse.



![Interface principale](assets/fr/03.webp)



Når konfigurasjonen er fullført, presenterer Macadamia tre hovedfaner. **Wallet** viser saldo og transaksjonshistorikk. **Mints** lar deg administrere Cashu-serverne dine. **Settings** gir tilgang til innstillinger og seed-frasen din.



![Ajout d'un mint](assets/fr/04.webp)



Du må nå konfigurere en mint, dvs. en Cashu-server som skal utstede tokens. Gå til "Mints"-fanen, trykk på "Add new Mint URL", og skriv inn adressen til den valgte mynten (f.eks. mint.cubabitcoin.org). Sjekk ut bitcoinmints.com eller cashu.space for anerkjente offentlige myntverk. Valider kun mynter du har sjekket omdømmet til, ettersom de vil ha ansvaret for satoshiene dine.



## Daglig bruk



### Opprettelse av nye tokens (Mint)



For å mate wallet Macadamia med ecash, må du utføre en "Mint"-operasjon (for å opprette tokens). Trykk på "Motta", og velg deretter alternativet "Lyn". Skriv inn ønsket beløp (f.eks. 1000 sats), velg mynten som skal brukes, og deretter generate Lynfakturaen.



![Opération Mint](assets/fr/05.webp)



Betal lynfakturaen som genereres med din vanlige wallet (Phoenix, Zeus, BlueWallet).



![Confirmation Mint](assets/fr/06.webp)



Cashu-tokens vises umiddelbart i saldoen din etter betaling.



### Send poletter



For å sende Cashu-tokens til en annen bruker, trykk på "Send"-knappen på hovedskjermen, og velg deretter "Ecash". Skriv inn beløpet som skal sendes (f.eks. 50 sats), og legg til et beskrivende memo om nødvendig.



![Envoi Ecash](assets/fr/07.webp)



Del QR-koden eller den genererte teksten via iMessage, Signal eller Telegram. Mottakeren gjør krav på pengene umiddelbart og kostnadsfritt.



### Motta tokens



For å motta Cashu-tokens sendt av en annen bruker, trykk på "Receive" og velg deretter "Ecash". Skann token QR-koden eller lim inn token-lenken du har mottatt.



![Réception Ecash](assets/fr/08.webp)



Trykk på "Redeem" for å gjøre krav på token.



### Lyn (smelte) betalinger



For å betale en lynfaktura med Cashu-tokens trykker du på "Send" og velger deretter "Lightning". Lim inn en BOLT11-faktura du ønsker å betale.



![Paiement Lightning](assets/fr/11.webp)



Myntverket ødelegger tokens og utfører Lightning-betalingen. Du kan altså betale for alle Lightning-tjenester samtidig som du bevarer anonymiteten din.



### Bytt mellom mynter



Når du mottar tokens fra et myntverk du ikke har konfigurert, tilbyr Macadamia deg flere alternativer for å administrere disse tokens.



![Swap inter-mints](assets/fr/09.webp)



Legg til den nye mynten eller bytt tokens til en eksisterende mynt. Byttet bruker Lightning som en bro for å overføre pengene dine anonymt.



### Avansert administrasjon av flere mynter



Macadamia tilbyr sofistikerte verktøy for å administrere flere mynter samtidig og fordele midlene dine strategisk.



![Gestion multi-mints](assets/fr/10.webp)



"Distribute Funds" fordeler automatisk saldoen din i henhold til prosentandeler (f.eks. 50/50). "Overfør" tillater manuelle overføringer mellom mynter for å spre risikoen din.



## Fordeler og begrensninger



**Høydepunkter** :





- Maksimal konfidensialitet**: Transaksjoner som ikke kan spores, selv ikke av myntverket. Ingen blockchain-metadata, sporløs peer-to-peer-utveksling.
- Rask og gratis**: Gratis øyeblikkelige overføringer innen en mynt, ideelt for mikrobetalinger.
- Interoperabilitet**: standardiserte Cashu-tokens for bruk med andre kompatible lommebøker (Minibits, Nutstash).
- Enkelhet**: Interface iOS native er tilgjengelig for nybegynnere, samtidig som den er reviderbar (åpen kildekode).



**Begrensninger** :





- Depotmodell**: Tillit til myntverk kreves. Hvis et myntverk forsvinner, mister tokens sin verdi.
- kun iOS**: Ingen Android/desktop-versjon. Cashu-interoperabilitet gir tilgang via andre lommebøker, men den optimale opplevelsen forblir iOS.
- Mint-avhengighet**: Mint offline = ikke i stand til å utføre transaksjoner som krever inngripen fra Mint (Mint, Melt).
- Ny teknologi** : Aktiv utvikling, mulige feil, standarder under utvikling.



## Beste praksis





- Diversifiser myntene dine**: Spre sjetongene dine på flere anerkjente myntselskaper for å redusere risikoen.
- Begrens beløp**: Bruk Macadamia som en fysisk wallet for daglige betalinger, ikke som en safe.
- Sikre seed**: Oppbevar 12-ordsfrasen på papir på et trygt sted. Test restaureringen av og til.
- Sjekk mynter**: Sjekk cashu.space og nettfora før du legger til en mint. Velg de med god oppetid og et solid omdømme.
- VPN eller Tor**: Skjul IP-en din med VPN/Tor for å maksimere nettverksvernet.
- Bli med i fellesskapet**: Telegram/Discord Cashu-grupper for oppdateringer, anbefalinger og beste praksis.



## Konklusjon



Macadamia Wallet tilfører egenskapene til fysiske kontanter til digitale Bitcoin. Ved å kombinere Chaum- og Lightning-blindsignaturer tilbyr den en elegant løsning for konfidensielle transaksjoner. Det innebygde iOS-grensesnittet gjør sofistikert kryptografisk teknologi tilgjengelig, samtidig som det er åpen kildekode og interoperabelt med Cashu-økosystemet.



Depotmodellen krever årvåkenhet og gode sikkerhetsrutiner. Brukt på riktig måte blir Macadamia et uvurderlig verktøy for dagligdagse betalinger som krever anonymitet, og et supplement til lommebøker uten depotmodell for sparing.



## Ressurser



### Offisiell dokumentasjon




- Offisiell nettside: [macadamia.cash](https://macadamia.cash)
- Vanlige spørsmål om macadamia: [macadamia.cash/faq] (https://macadamia.cash/faq)
- GitHub-kildekode: [github.com/zeugmaster/macadamia](https://github.com/zeugmaster/macadamia)



### Cashu-dokumentasjon




- Teknisk dokumentasjon: [docs.cashu.space] (https://docs.cashu.space)
- Liste over offentlige myntverk: [bitcoinmints.com](https://bitcoinmints.com)
- Offisielt nettsted for protokollen: [cashu.space] (https://cashu.space)



### Fellesskapet




- Telegram Cashu gruppe: [t.me/cashu_ecash] (https://t.me/cashu_ecash)