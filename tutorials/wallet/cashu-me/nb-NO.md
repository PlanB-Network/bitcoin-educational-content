---
name: Cashu.me
description: Cashu.me-veiledning for bruk av ecash
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=LIPw1c74LBU)


*Her er en videoveiledning fra BTC Sessions, en videoguide som går gjennom hvordan du setter opp og bruker Cashu.me Bitcoin Wallet, som gir deg tilgang til enkle, billige og private Bitcoin-transaksjoner - uten behov for en app store!


I denne opplæringen skal vi utforske Cashu.me, en nettleserbasert Wallet for private Bitcoin-betalinger ved hjelp av Chaumian ecash. Før vi går i gang, skal vi gi en kort introduksjon til ecash og hvordan det fungerer.


## Introduksjon til ecash


Tenk deg å ha digitale kontanter som fungerer akkurat som fysiske sedler i lommen - private, øyeblikkelige og brukbare peer-to-peer uten mellomledd. Det er det ecash muliggjør: en digital betalingsmetode som bringer personvernet til fysiske kontanter tilbake til den digitale verden. I motsetning til onchain-Bitcoin, som registrerer alle transaksjoner på en offentlig Ledger som er synlig for alle, skaper ecash private tokens som representerer reell Bitcoin-verdi, samtidig som forbruksvanene dine holdes konfidensielle.


Tenk på ecash som digitale ihendehaverinstrumenter som er lagret på enheten din - hvis du har dem, eier du dem, akkurat som fysiske kontanter. Disse tokens utstedes av betrodde tjenester kalt `Mints` som holder de underliggende Bitcoin-reservene. Når du bruker ecash, kringkaster du ikke transaksjonene dine til hele nettverket. I stedet utveksler du private tokens direkte med andre, noe som skaper en betalingsopplevelse som føles mer som å gi noen kontanter enn å foreta en tradisjonell digital betaling.


Cashu er en gratis og åpen kildekodebasert Chaumian ecash-protokoll bygget for Bitcoin. Teknologien bygger på David Chaums banebrytende kryptografiske forskning fra 1980-tallet, og bruker "blinde signaturer" for å sikre personvernet. Når du mottar ecash-tokens, signerer myntverket dem uten å vite hvor de skal brukes neste gang - en avgjørende funksjon som forhindrer sporing av transaksjoner. Det er viktig å merke seg at ecash ikke erstatter Bitcoin, men utfyller det ved å løse noen av de kritiske problemene som følger med Bitcoin-arkitekturkravene. Det gir personvernet som fysiske kontanter tilbyr (som Bitcoins gjennomsiktige Ledger mangler) og muliggjør umiddelbare mikrotransaksjoner uten Blockchain-gebyrer eller bekreftelsesforsinkelser.


Ecash integreres sømløst med Lightning Network. Du bruker Lightning til å sette inn Bitcoin i en mint (konverterer Bitcoin-verdien din til ecash-tokens) og til å ta ut senere (konverterer tokens tilbake til brukbar Lightning-saldo). Sammen utgjør de en kraftig kombinasjon: Bitcoin gir det sikre oppgjøret Layer, Lightning muliggjør raske transaksjoner og nettverksinteroperabilitet, og ecash legger til personvernet Layer som gjør at digitale betalinger føles virkelig private igjen.


## Cashu.me


Cashu.me er en progressiv webapp (PWA) som implementerer Cashu-protokollen - en spesifikk implementering av Chaumian ecash designet for Bitcoin. Som en PWA fungerer den direkte i nettleseren din uten å kreve installasjon fra appbutikker, selv om du kan "installere" den på enheten din for enklere tilgang. Denne nettbaserte tilnærmingen sikrer bred kompatibilitet på tvers av operativsystemer, samtidig som sikkerheten opprettholdes gjennom kryptografiske protokoller i stedet for plattformbegrensninger.


## 🎉 Viktige funksjoner


La oss dykke ned i funksjonene og utforske hva Cashu.me har å tilby:



- Chaumian ecash på Lightning**: Bruker blinde signaturer, slik at myntverket ikke kan spore brukersaldoer eller transaksjonshistorikk
- Selvoppbevaring av tokens**: Du kontrollerer ecash-tokens lokalt med din seed-frase
- seed-frasesikkerhetskopier**: 12-ords gjenopprettingsfrase for Wallet-gjenoppretting
- Uavhengighet av mynter**: Fungerer med flere uavhengige mynter - du er ikke låst til én leverandør
- Øyeblikkelige, gratis transaksjoner**: I samme myntsted fullføres betalinger på få sekunder uten gebyrer
- Personvernbevarende arkitektur**: Myntverket kan ikke se hvem som handler med hvem
- Frakoblet ecash**: Send/mottar tokens gjennom en lokal overføringsprotokoll, som NFC, QR-kode, Bluetooth osv. uten internettforbindelse
- Oppdag ecash-myntverk via Nostr**: Finn og verifiser pålitelige mynter gjennom Nostr-protokollen
- Bytt ecash mellom mynter**: Alle mynter snakker Lightning, noe som betyr at du kan overføre verdi mellom dem.
- Fjernstyr Wallet med Nostr Wallet Connect (NWC)**: Koble til andre apper som Nostr Client og start zapping via NWC


Den kritiske avveiningen er "tillit": Selv om du kontrollerer selve tokens, må du stole på at myntverket forvalter de underliggende Bitcoin-reservene. Som det står i Cashus dokumentasjon:


> ...mynten driver Lightning-infrastrukturen og forvalter satoshiene for myntens ecash-brukere. Brukerne må stole på at mynten Redeem deres ecash når de ønsker å bytte til Lightning.

- Cashu-dokumentasjon, [Generelle spørsmål om sikkerhet og personvern] (https://docs.cashu.space/faq#general-safety-and-privacy-questions)


Dette gjør ecash til en depotløsning for selve Bitcoin, selv om du beholder full kontroll over tokens.


## 1️⃣ Førstegangsoppsett


① Begynn med å besøke [Wallet.cashu.me] (https://Wallet.cashu.me) i nettleseren din. Siden Cashu.me er en `PWA`, trenger du ikke å laste den ned fra appbutikker, bare åpne nettstedet direkte i nettleseren din. For enklere tilgang kan du eventuelt installere den på enhetens startskjerm.


for å installere PWA trykker du på menyknappen ⋮ i nettleseren og velger "Legg til på startskjermen". Når du har installert, lukker du nettleserfanen og starter Cashu.me fra enhetens startskjerm. På velkomstskjermen trykker du på `Neste` for å fortsette.


③ Sikkerhet er avgjørende. Lagre seed-frasen på en sikker måte i en passordbehandler, eller enda bedre, skriv den ned på papir. Denne 12-ord lange gjenopprettingsfrasen er den eneste måten du kan få tilbake penger på hvis du mister tilgangen til denne enheten. Trykk på 👁️-ikonet for å vise seed-frasen din, skriv nøye ned alle 12 ordene i rekkefølge, og kryss deretter av i boksen merket med "Jeg har skrevet det ned". Trykk på `Neste` for å fortsette, og kryss av i boksen for å bekrefte at du godtar `vilkårene` på følgende skjermbilde.


![image](assets/en/01.webp)


Når du har fullført oppsettet, må du koble deg til en `Mint`. Trykk på `ADD MINT` etterfulgt av `DISCOVER MINTS` for å se mynter anbefalt av Nostr-fellesskapet. For ytterligere verifisering kan du se mint-rangeringer på [bitcoinmints.com] (bitcoinmints.com).


Trykk deretter på "Klikk for å bla gjennom mints" for å se hele listen. Velg en mynte ved å kopiere URL-adressen, lime den inn i URL-feltet og gi den et gjenkjennelig navn. I dette eksempelet bruker vi


URL: `https://mint.minibits.cash/Bitcoin`

Navn: `Minibits`


![image](assets/en/02.webp)


Trykk på `ADD MINT` for å fullføre prosessen. På bekreftelsesskjermen bekrefter du at du stoler på operatøren av denne mynten, og trykker deretter på `ADD MINT` igjen. Minibits mint vises nå på startskjermen. Når Wallet er satt opp, må du fylle penger på den før du kan foreta transaksjoner.


![image](assets/en/03.webp)


## 2️⃣ Finansiering av din Wallet


Cashu.me tilbyr to forskjellige metoder for å finansiere din Wallet. Når du trykker på `Mottak` på startskjermen, vil du se alternativer for å motta penger via `ECASH` eller via `LIGHTNING`.


![image](assets/en/04.webp)


### Finansiering via LIGHTNING


Det første alternativet er å finansiere Wallet via Lightning Invoice. velg et myntverk hvis du har lagt til forskjellige myntverk, og definer beløpet (Sats) du vil motta. Trykk deretter på "Opprett Invoice." Nå får du en QR-kode som du kan skanne med en annen lyn Wallet, eller du kan bare "kopiere" Invoice og lime den inn i en annen Wallet for å betale og finansiere din cashu.me Wallet.


![image](assets/en/05.webp)


### Motta ecash


Med ecash-metoden kan du motta tokens direkte fra en annen ecash Wallet. Begynn med å trykke på `Mottak`-knappen, og velg `ECASH`-alternativet. Du kan "lime inn" eller "skanne" eller bruke "NFC" for å sende inn en Cashu token fra en annen Wallet. Hvis du velger å lime inn, skriver du inn token-strengen du har kopiert fra en annen Wallet. Beløpet og mynten vises automatisk. Trykk på `RECEIVE` for å fullføre transaksjonen, og Sats vises i din Wallet. Legg merke til at saldoen din nå er fordelt på flere mynter. Du kan for eksempel ha 1 000 Sats i din Minibits `Mint` og ytterligere 1 000 Sats i en Coinos `Mint`. Denne separasjonen på tvers av ulike mynter er et viktig aspekt ved Cashus arkitektur.


![image](assets/en/06.webp)


### Bytte mellom mintpastiller


Hvis du ikke lenger stoler på en bestemt myntsort du har lagt til, tilbyr cashu.me en funksjon for å `bytte` penger fra en myntsort til en annen. Gå til fanen mynter og bla nedover til du ser `Multimint Swaps`. Velg mynten `FROM` og `TO` fra nedtrekksmenyene, og skriv inn beløpet du ønsker å overføre. Trykk på `SWAP` for å flytte tokens mellom mynter. Dette vil bli utført via Lightning-transaksjon, så du må ta høyde for potensielle Lightning-gebyrer. I mitt eksempel var 1 sat tilstrekkelig.


![image](assets/en/07.webp)


## 3️⃣ Sende midler


For å sende Sats tilbyr Cashu.me to alternativer. Å sende via `ecash` eller via `lyn`. La oss ta en titt på begge alternativene.


### Sende via Lightning


Følg disse trinnene for å sende via Lightning:


1. Trykk på `SEND` på startskjermen, og velg `Lightning`

2. Appen vil be deg om å angi en "Lightning Invoice" eller "Address". Du kan lime inn Invoice/Address direkte, eller bruke alternativet skann QR-kode for å fange den visuelt, og deretter bekrefte med `ENTER`

3. Velg mynten du vil betale fra ved hjelp av rullegardinmenyen, og trykk på "BETAL" for å bekrefte. **Merk**: Det er også mulig å bruke `Multinut` under `Innstillinger` -> `Eksperimentell`, slik at du kan betale fakturaer fra flere mynter samtidig.

4. Når du har fullført betalingen, vil du se en betalingsbekreftelse og beløpet som er trukket fra saldoen din.


![image](assets/en/08.webp)


### Sende via ecash


Det er like enkelt å sende ecash.


1. Trykk på `SEND` og velg denne gangen alternativet `ECASH`.

2. velg en myntseddel, skriv inn beløpet du vil sende i Sats, og trykk på "SEND" for å bekrefte

3. Dette skaper en "animert QR-kode" som du kan tilpasse ved å justere parametrene for hastighet og størrelse. Hvem som helst kan skanne denne QR-koden for å Redeem Sats umiddelbart, eller du kan trykke på KOPIER for å sende token-strengen til noen andre via alternative kanaler som Bluetooth, NFC eller standardmeldinger.

4. Jeg åpner en annen Wallet. Lim inn fra utklippstavlen og velg `Motta ecash` i den andre Wallet.


![image](assets/en/09.webp)


## 4️⃣ Tilleggsfunksjoner


Utover kjernefunksjonaliteten for sending og mottak tilbyr Cashu.me kraftige tilleggsfunksjoner som forbedrer Bitcoin-opplevelsen din i Nostr-økosystemet.


### Nostr Wallet Connect


Nostr Wallet Connect (`NWC`) endrer hvordan du samhandler med Nostr-applikasjoner ved å skape en sømløs forbindelse mellom din Wallet og sosiale apper. Denne protokollen gjør det mulig for applikasjoner som [Damus] (https://damus.io/) eller [Primal] (https://primal.net/home) å be om betalinger direkte gjennom Nostr-reléer uten at du trenger å forlate appen.


For å sette opp `NWC` i Cashu.me:


1. Gå til `Innstillinger` øverst til venstre i hamburgermenyen

2. Bla til `NOSTR Wallet CONNECT`-delen og trykk på `Enable`-knappen

3. Deretter setter du en kvote for å fastsette det maksimale beløpet du kan bruke fra Wallet.

4. Når du har konfigurert den, kan du kopiere tilkoblingsstrengen og lime den inn i en hvilken som helst Nostr-klient som støtter `NWC`, slik at du kan zappe og tippe umiddelbart.


![image](assets/en/10.webp)


### Lynet Address via npub.cash


Cashu.me integreres med [npub.cash] (https://npub.cash/) for å gi deg en Lightning Address som fungerer sømløst med Nostr-protokollen. Her kan du registrere deg og kreve brukernavnet ditt ved å oppgi Nostr `nsec`, som koster 5000 Sats og støtter npub.cash-prosjektet, eller du kan bruke en hvilken som helst Nostr-publikumsnøkkel (`npub`) uten registrering.


Først går du til `Innstillinger` og trykker på `Aktiver` Lyn Address med npub.cash. Dette vil generate en npub.cash Address ved hjelp av en `npub`-streng avledet fra din Wallet seed frase som standard.


Alternativt kan du gå til [denne nettsiden] (https://npub.cash/username) for å kreve et tilpasset brukernavn ved hjelp av din egen Nostr `nsec`, noe som gir deg et personlig Lightning Address som username@npub.cash.


![image](assets/en/11.webp)


## 🎯 Konklusjon


Cashu.me leverer private Bitcoin-betalinger som fungerer som fysiske kontanter - umiddelbart og peer-to-peer uten å eksponere transaksjonshistorikken din. Jeg setter personlig pris på PWA-arkitekturen fordi den fungerer uten begrensninger fra appbutikker. Ved å kombinere sikkerheten til Bitcoin, hastigheten til Lightning og personvernet til ecash, tilbyr Wallet bruksområder som kan øke den daglige bruken av Bitcoin.


Selv om du har full kontroll over ecash-tokens gjennom egen oppbevaring, må du huske at myntverk fungerer som betrodde tredjeparter som har de underliggende Bitcoin-reservene. Muligheten til å bruke flere myntverk og bytte mellom dem gir fleksibilitet samtidig som personvernet opprettholdes.


Takket være funksjoner som NWC og npub.cash-adresser er Cashu.me et tiltalende Wallet-alternativ for sosiale kunder som verdsetter personvern og suverenitet over store teknologipolitiske begrensninger.


## 📚 Ressurser


[https://github.com/cashubtc/cashu.me](https://github.com/cashubtc/cashu.me)


[https://github.com/cashubtc](https://github.com/cashubtc)


[https://github.com/cashubtc/awesome-cashu](https://github.com/cashubtc/awesome-cashu)


[https://cashu.space/](https://cashu.space/)