---
name: Bull Bitcoin Wallet
description: Finn ut hvordan du bruker Wallet Bull Bitcoin
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=6b0xTB2sE8E)


*Denne videoveiledningen fra BTC Sessions går gjennom prosessen med å sette opp og bruke Bull Bitcoin Wallet!


Denne veiledningen tar deg gjennom installasjon, konfigurasjon og bruk av Bull Bitcoin Wallet. Du lærer å sende og motta penger på Bitcoin On-Chain-, Liquid- og Lightning-nettverkene, samt hvordan du flytter Bitcoin mellom dem. wallets omfattende funksjoner gjør den til et kraftig alt-i-ett-verktøy for å administrere din Bitcoin. La oss komme i gang.


## Innledning


Bull Bitcoin Wallet, utviklet av [Bull Bitcoin](https://www.bullbitcoin.com/), er en **selvforvaltende** Bitcoin wallet, noe som betyr at du har full kontroll over de private nøklene dine og dermed pengene dine, uten å være avhengig av en tredjepart. Denne Wallet er basert på åpen kildekode og en Cypherpunk-filosofi, og kombinerer enkelhet, konfidensialitet og avanserte funksjoner som nettverksbytte og PayJoin-støtte. Den lar deg administrere bitcoins på tre nettverk: ** Bitcoin onchain**, ** Liquid** og ** Lightning**, hvert skreddersydd til spesifikke bruksområder. På [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49) kan du sjekke ut aktuelle emner og kommende utvikling. Siden prosjektet er 100 % åpen kildekode og "bygget i offentligheten", kan du også sende inn forslag og eventuelle feil du støter på. Mens noen lommebøker nå støtter flere nettverk, skiller Bull Bitcoin Wallet seg ut ved å integrere personvernfunksjoner på tvers av dem alle, noe som gjør den til et kraftig verktøy for å administrere Bitcoin på tvers av alle de store nettverkene


## 1️⃣ Forutsetninger


Før du begynner å bruke **Bull Bitcoin Wallet**, må du sørge for at du har følgende utstyr:



- Kompatibel smarttelefon**: En **iOS** (iPhone eller iPad) eller **Android**-enhet
- Internett-tilkobling
- Sikre sikkerhetskopieringsmedier**: Skriv ned **gjenopprettingsfrasen** (12 ord) på papir eller metall, og oppbevar den på et trygt sted.
- Grunnleggende kunnskap**: Et minimum av forståelse av Bitcoin-konsepter (adresser, transaksjoner, gebyrer) er nyttig, selv om denne veiledningen forklarer hvert trinn for nybegynnere.


## 2️⃣ Installasjon


Du kan installere programmet gjennom:



- [Apple App Store](https://apps.apple.com/app/bull-bitcoin/id6743380972)[ ](https://apps.apple.com/us/app/bitchat-mesh/id6748219622)(for iOS-enheter)
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&hl=en) (for Android-enheter)


Android-brukere har også alternative muligheter:



- Last ned APK direkte fra [GitHub Releases](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) eller
- Installer via den Nostr-kompatible [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqtxxmmd9e382mrvvf5hgcm0d9hzumt0vf5kcegnah0ap)


Etter at du har installert programmet, følger du opp på velkomstskjermen for å konfigurere kontoen din.


## 3️⃣ Innledende konfigurasjon


Når du åpner den, blir du bedt om å velge følgende alternativer:



- "Opprett ny Wallet
- "Gjenopprett Wallet" og
- "Avanserte alternativer


La oss begynne med å trykke på `Avanserte alternativer`.


Her kan vi konfigurere de avanserte innstillingene før vi oppretter eller gjenoppretter en wallet:


1. Aktiver `Tor-proxy` for å rute trafikk over Tor-nettverket.

1. [Orbot app](https://orbot.app/en/) må være installert og kjørt før aktivering

2. Tor Proxy gjelder bare for Bitcoin (ikke Liquid) og kan føre til en langsommere tilkobling.

2. Konfigurer en `Tilpasset Electrum Server`, eller

3. Juster innstillingene for `Recover Bull`. Vi vil lære mer om [Recover Bull](https://recoverbull.com/) senere.


Når du har gjort alle de valgfrie justeringene, trykker du på "Ferdig". Hvis du ønsker å gjenbruke en eksisterende Wallet, klikker du på `Gjenopprett Wallet` og fyller inn de 12 ordene i gjenopprettingsfrasen din.


Ellers klikker du på "Opprett en ny Wallet".


![image](assets/en/01.webp)


## 4️⃣ Startskjerm


Før vi går dypere inn i dette, la oss ta en titt på startskjermen for å orientere oss:



- transaksjonsoversikten og innstillingsmenyen er plassert øverst.
- Tilgjengelig saldo har et personvernalternativ som kan slås av eller på.
- Få tilgang til `Bitcoin Bull Exchange` for å `kjøpe, selge eller betale` (dette avhenger av jurisdiksjonen og kan kreve KYC).
- overføring av penger mellom lommebøker
- `Secure Bitcoin` er lik Onchain Bitcoin Wallet
- lynbetalinger via Lightning- / Liquid Network *(Merk: Bull Bitcoin Wallet gjør det mulig å foreta og motta betalinger via Lightning. Midler mottatt via Lightning lagres i [*Liquid-nettverket](https://liquid.net/) (i Wallet Instant Payments) takket være en automatisk utveksling via [*Boltz exchange](https://boltz.exchange/). Dette gir deg muligheten til å samhandle med Lightning uten å måtte administrere likviditetskanaler, samtidig som du forblir i egen depot)
- sende og motta penger


![image](assets/en/02.webp)


La oss først gjøre noen viktige konfigurasjoner og starte med `Backup`.


## 5️⃣ Sikkerhetskopiering


For å starte sikkerhetskopieringen trykker du på tannhjulikonet (⚙) øverst til høyre i appen og velger `Wallet Backup`. Du vil bli presentert for to metoder for å sikre wallet: `Encrypted Vault` og `Physical Backup`. La oss utforske hver av dem.


![image](assets/en/03.webp)


### Fysisk sikkerhetskopiering


Trykk på `Fysisk sikkerhetskopi` for å se en liste med 12 ord som representerer din recovery- eller seed-frase. Vennligst vurder følgende:



- Skriv ned "gjenopprettingsfrasen" din med den største forsiktighet. Skriv den ned på papir eller metall og oppbevar den på et trygt sted (bankboks, frakoblet sted). Denne frasen er din eneste mulighet til å få tilgang til bitcoinsene dine i tilfelle du mister enheten din eller sletter applikasjonen.
- Det er også viktig å merke seg at hvem som helst med denne frasen kan stjele alle bitcoinsene dine. Aldri lagre det digitalt:
- Ingen skjermbilde
- Ingen sikkerhetskopiering i skyen, e-post eller meldinger
- Ingen kopiering/liming (risiko for lagring i utklippstavlen)


![image](assets/en/25.webp)


I neste skjermbilde må du sette ordene i riktig rekkefølge for å sikre at du har fått riktig seed-frase. Du får en bekreftelse når testen er fullført og vellykket.


! **Dette punktet er kritisk**. For ytterligere hjelp :


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### Kryptert hvelv


Det er også mulig å ta en kryptert, anonym sikkerhetskopi i skyen. Men nevnte vi ikke i forrige avsnitt at sikkerhetskopiering i skyen er risikabelt og bør unngås? Bull Bitcoin-teamet har imidlertid utviklet en smart måte å gjøre prosessen trygg på. Her er hvordan det fungerer:


`Recoverbull` er en sikkerhetskopieringsprotokoll som forenkler sikringen av din Bitcoin wallet ved å dele opp sikkerhetskopieringen i to deler. Først krypteres wallet-sikkerhetskopifilen på enheten din ved hjelp av en sterk krypteringsnøkkel. Du kan lagre denne krypterte filen hvor du vil, for eksempel på Google Drive eller på enheten din. For det andre lagres krypteringsnøkkelen som trengs for å låse opp filen av Recoverbull Key Server. For å gjenopprette wallet trenger du både den krypterte sikkerhetskopifilen og nøkkelen, som du får tilgang til med PIN-koden eller passordet ditt. Denne konstruksjonen sikrer at sikkerhetskopien i skyen alene er ubrukelig, og at nøkkelserveren alene er ubrukelig uten din spesifikke sikkerhetskopifil. Dette gjør at pengene dine er trygge selv om en av delene skulle bli kompromittert.


Tenk på det som en bankboks. Den krypterte sikkerhetskopifilen er *boksen*, som du kan lagre hvor som helst (som Google Drive). Gjenopprettings-PIN-koden din er *nøkkelen*, som lagres separat av Recoverbull Key Server. En tyv må få tak i både din spesifikke boks og din spesifikke nøkkel for å åpne den. Denne konstruksjonen sikrer at selv om noen får tak i sikkerhetskopifilen din, er den ubrukelig uten nøkkelen fra serveren, og serverens nøkkel er ubrukelig uten din unike sikkerhetskopifil.


Finn ut mer om wallet-sikkerhetskopieringsprotokollen `Recoverbull` [her](https://recoverbull.com/).


Trykk på `Kryptert hvelv` og deretter `Fortsett` for å bekrefte at du bruker standardserveren. Tilkoblingen vil bli rutet gjennom `Tor`-nettverket for å sikre personvern og anonymitet.


**Forstå PIN-kodene dine**



- pIN-kode for opplåsing av app**:** Den valgfrie PIN-koden som angis i `Innstillinger > Sikkerhets-PIN-kode` for å låse appen på telefonen din.
- gjenopprettings-PIN-kode**:** Den obligatoriske PIN-koden som ble opprettet under sikkerhetskopieringen av `Encrypted Vault`, og som brukes til å dekryptere sikkerhetskopifilen din under gjenoppretting.


Dette er to separate PIN-koder. Ikke glem gjenopprettings-PIN-koden, da den er avgjørende for å gjenopprette wallet."


**Oppsett av PIN-kode for gjenoppretting:**



- Du må opprette en PIN-kode eller et passord for å få tilgang til wallet igjen.
- PIN-koden/passordet må være minst 6 sifre langt (unngå enkle sekvenser som 123456, som ikke godtas).
- Uten denne PIN-koden er det umulig å gjenopprette wallet.


Deretter velger du en hvelvleverandør:



- `Google Drive` eller
- en "tilpasset plassering" (f.eks. enheten din)


![image](assets/en/04.webp)


Lagre nå sikkerhetskopifilen. Trykk deretter på "Test gjenoppretting", velg den lagrede sikkerhetskopifilen eller hvelvet, og trykk deretter på "Dekrypter hvelv". Skriv inn PIN-koden eller passordet ditt. Hvis alt fungerte, vises skjermbildet "Test fullført".


### Etiketter for import/eksport


Nå som vi har opprettet sikkerhetskopien vår, la oss ta en titt på `Etiketter`.  Bull Bitcoin wallet forbedrer personvernet og organiseringen ved å tillate brukere å opprette egendefinerte etiketter for mottaksadresser og transaksjoner. Disse etikettene hjelper deg med å kategorisere midlene dine, ettersom transaksjoner som sendes til en merket adresse vil arve denne etiketten, og du kan også merke utgående transaksjoner for å spore endringen av dem. wallet støtter fullt ut [BIP-329](https://bip329.org/)-standarden, noe som betyr at du kan eksportere alle etikettene dine til en fil og importere dem til en annen wallet. Denne funksjonen sikrer at du sømløst kan sikkerhetskopiere transaksjonshistorikken og kategoriseringene dine, eller migrere dem mellom ulike instanser av wallet, uten å miste den personlige organiseringen din.


![image](assets/en/05.webp)


## 6️⃣ Innstillinger


Nå som den primære sikkerhetskopien er sikret, kan vi utforske de andre funksjonene som er tilgjengelige i innstillingene.


### A - Sikring av tilgang


For å sikre appen går du til `Innstillinger` og velger `Sikkerhets-PIN` for å velge PIN-kode. Opprett en sterk PIN-kode for å låse tilgangen til wallet. Selv om dette trinnet er valgfritt, anbefales det på det sterkeste for å forhindre uautorisert tilgang hvis noen andre bruker telefonen.


![image](assets/en/06.webp)


### B - Tilkobling til en personlig node (valgfritt)


Wallet BullBitcoin kobles som standard til Electrum-servere: den første administreres av Bull Bitcoin og en sekundær server fra Blockstream, som begge anses å ikke føre noen logger, noe som reduserer risikoen for sporing.


For større konfidensialitet kan du koble applikasjonen til din egen Bitcoin-node via en Electrum-server. Dette gjør du ved å trykke på `Innstillinger` > `Bitcoin-innstillinger` > `Electrum Server-innstillinger`, og deretter trykke på `+ Legg til egendefinert server` for å angi serverens adresse og legitimasjon.


![image](assets/en/07.webp)


### C - Valuta


Den tilgjengelige saldoen vises på hovedskjermen i både `sats` og `USD`. For å endre dette går du til `Innstillinger` > `Valuta`. Der kan du veksle mellom `sats/BTC` og velge din `standard fiat-valuta`.


![image](assets/en/08.webp)


### D - Bitcoin Innstillinger


Menyen `Bitcoin Settings` gir deg dyp tilgang til wallets kjernekonfigurasjoner og data. Her kan du inspisere de grunnleggende detaljene i `Secure Bitcoin` og `Instant Payments-lommebøkene`, noe som gir deg full åpenhet og kontroll. Nøkkelfunksjonene i denne menyen inkluderer:



- Wallet Detaljer:** Naviger til din sikre Bitcoin eller øyeblikkelige betalinger wallet for å se spesifikk informasjon.
- Wallet Fingeravtrykk:** En unik identifikator for din wallet.
- Offentlig nøkkel (Pubkey):** Nøkkelen som brukes til å generate dine Bitcoin-mottakeradresser.
- Descriptor:** Et teknisk sammendrag av wallets struktur.
- Avledningsbane:** Den spesifikke banen som brukes til å generate alle adresser fra din private hovednøkkel.
- Address View:** Få tilgang til en liste over ubenyttede mottaksadresser og endre adresser (kommer snart)


I tillegg har du muligheten til å:



- aktiver automatisk overføring-innstillinger for å angi en maksimal øyeblikkelig wallet-saldo, som deretter automatisk overføres til den sikre bitcoin wallet.
- Importer generiske lommebøker via `Mnemonic`-frase eller importer `watch-only`
- Koble til `Hardware-lommebøker`: enheter som for øyeblikket støttes er ColdcardQ, SeedSigner, Specter, Krux, Blockstream Jade og Foundation Passport


## 7️⃣ Bull Bitcoin Exchange


Direkte fra wallet har du tilgang til [Bull Bitcoin exchange](https://www.bullbitcoin.com/), slik at du kan kjøpe, selge og betale Bitcoin uten å forlate appen. Denne integrasjonen gir deg en praktisk løsning for å håndtere dine Bitcoin-behov. Vær oppmerksom på at tilgangen til børsen og dens tjenester kan være begrenset basert på din jurisdiksjon, og at det kan være nødvendig å fullføre KYC-verifisering (Know Your Customer) for å overholde regulatoriske standarder og bruke plattformens fulle funksjoner.


For å komme i gang trykker du på `Exchange` nederst i høyre hjørne, og deretter `Sign up` eller `Login` til kontoen din.


Børsen tilbyr følgende [funksjoner](https://www.bullbitcoin.com/):



- Kjøp Bitcoin med selvforvaring fra bankkontoen din
- Ikke-frihetsberøvende
- Privatpersoner eller selskaper
- Øyeblikkelig uttak
- Ingen skjulte avgifter
- Lightning Network tilgjengelig
- Ingen transaksjonsgrenser
- Tilbakevendende kjøpsalternativer


![image](assets/en/09.webp)


Hvis du vil lære mer, kan du gå til denne veiledningen:


https://planb.academy/en/tutorials/exchange/centralized/bull-bitcoin-europe-0ccf713e-efcd-44ec-8205-211f49ac7d53

## 8️⃣ Mottak av midler


Det er enkelt og fleksibelt å motta penger med **Bull Bitcoin Wallet**, som støtter tre forskjellige nettverk skreddersydd for ulike bruksområder:



- Bitcoin (onchain)-nettverket for sikker langtidslagring.
- Liquid-nettverket for raske og mer konfidensielle transaksjoner.
- Lynnettverket for øyeblikkelige og rimelige betalinger.


Appen genererer automatisk riktig adresse eller faktura basert på hvilket nettverk du har valgt. Slik går du frem for hvert nettverk.


### Mottak via Onchain (Bitcoin-nettverk)


For å motta on-chain-midler kan du enten velge `Secure Bitcoin Wallet` fra startskjermen og trykke på `Mottak`, eller trykke på hovedknappen `Mottak` og deretter velge `Bitcoin-nettverket`.


Du har to hovedmåter å generere en mottaksadresse på:


**Standardmodus (URI med ekstra inngangsparametere)


Som standard genererer wallet en [BIP21 URI](https://bips.dev/21/). Dette er et standardisert format som inneholder mer informasjon enn en enkel adresse, inkludert et beløp, en personlig merknad og PayJoin-parametere for å forbedre personvernet. Denne omfattende URI-en kodes inn i en QR-kode og gjøres tilgjengelig for kopiering. Formatet ser slik ut: `bitcoin:<adresse>?<parameter1>=<verdi1>&<parameter2>=<verdi2>`.



- Ytterligere inngangsparametere:**
    - Beløp:** Angi et ønsket beløp i BTC, sats eller en fiat-valuta.
    - Melding:** Legg til en personlig merknad som vil være synlig for avsenderen.
    - PayJoin:** Aktiver dette alternativet for å forbedre personvernet ved å kombinere inndata fra både avsender og mottaker i transaksjonen.


Eksempel på URI:


```
bitcoin:bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54xxxxx?amount=0.0005&message=Tip+for+tutorial&pj=HTTPS%3A%2F%2FPAYJO.IN%2F78UH9WZUP8KKJ%23RK1Q2H30FASCU9WW09DQY2LK0K8P2DPRJ99V72CA78ACQAEL675QYTMQ+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1L0LYV6G
```


*Viktig merknad: Vennligst ikke send penger til adressene i denne veiledningen, wallet vil bli slettet


![image](assets/en/10.webp)


**Alternativet Kopier eller skann kun Address aktivert


Når alternativet `Kopier eller skann kun Address` er aktivert, genererer programmet en enkel Bitcoin-adresse i SegWit (bech32)-format.


Eksempel:


```javascript
bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54x3g56
```


Selv om du skriver inn et beløp eller en merknad, vil de ikke bli inkludert i QR-koden eller den kopierte adressen.


![image](assets/en/11.webp)


### Mottak via Liquid Network


Du kan motta en betaling på Liquid Network. Når du er på skjermbildet "Motta", har du de samme to alternativene for å generere en betalingsforespørsel:


**1. Enkel Address:** Kopier standard `Liquid-adresse`. Dette er en unik identifikator for din wallet i Liquid-nettverket og inkluderer ikke noe spesifikt beløp eller melding.


Eksempel Address:


```javascript
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7xxxxxxx
```


**2. Detaljert betalingsforespørsel (URI):** For en mer strukturert forespørsel kan du spesifisere et beløp og en personlig merknad. Denne informasjonen blir automatisk kodet inn i en delbar URI og en tilhørende QR-kode.



- Beløp:** Du kan angi beløpet i Bitcoin (BTC), Satoshis (Sats) eller en fiat-valuta.
- Merk:** Legg til en personlig melding for å identifisere transaksjonen.


**Eksempel URI:**


```javascript
liquidnetwork:lq1qqdhgs7w537nun55a5sdy4gxkd08pclk3d7v4qz36sy4xp0cq6gvl52fcfv7kdgkgzmfycrud0zsygqgyjclycckpasxxxxxx?amount=0.00001&message=Test&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```


For å fullføre transaksjonen må du gi avsenderen `adressen` eller `URI`. Dette kan du gjøre ved å kopiere den til utklippstavlen eller ved å be dem skanne QR-koden direkte fra skjermen din.


![image](assets/en/12.webp)


### Mottak via Lightning



Bull Bitcoin Wallet lar deg også sende og motta betalinger via Lightning Network. En viktig funksjon er at midler som mottas via Lightning, automatisk byttes og lagres på Liquid Network i Wallet for øyeblikkelige betalinger. Denne tjenesten drives av `Boltz`. Dette designet gjør at du kan nyte godt av hastigheten og de lave kostnadene ved Lightning uten kompleksiteten ved å administrere likviditetskanaler, samtidig som du opprettholder full selvforvaring av midlene dine. Selv om denne hybridtilnærmingen er selvforvaltende og unngår kompleksiteten ved å administrere kanaler, introduserer den en tredjepartstjeneste (Boltz), et lite byttegebyr og avhengighet av Liquid Networks føderasjon av funksjonærer som nøkkelinnehavere, noe som er forskjellig fra en tradisjonell, ikke-forvaltende Lightning wallet der du administrerer dine egne kanaler. Du kan lese mer om Liquid og styringsmodellen her:


https://planb.academy/en/courses/e17ee350-41d4-49fa-b270-29e4d26d22f8/overview-of-liquid-architecture-and-governance-model-17650c4b-cd1f-4bc6-b490-708f92dc9306


- Grenser:**
    - Minimumsbeløp:** Det kreves et minimumsbeløp på fakturaen. Vennligst sjekk appen for gjeldende grense
    - Gebyrer:** Du som mottaker er ansvarlig for et lite byttegebyr. Dette gebyret trekkes fra beløpet avsenderen overfører, og kan endres
- Fordeler:**
    - Selvforvaltende:** Pengene dine er alltid under din kontroll, sikret i Liquid-nettverket.
    - Unngå høye On-Chain-gebyrer:** Ved å bruke Lightning og lagre på Liquid, unngår du on-chain-gebyrene som er forbundet med å åpne en tradisjonell Lightning-kanal. Du kan velge å flytte midler til en on-chain-kanal senere, når det akkumulerte beløpet rettferdiggjør utgiften.
    - Tips:** For å få den mest kostnadseffektive transaksjonen mellom to Bull Bitcoin-brukere kan du bruke **Liquid-nettverket direkte** for å unngå Lightning-byttegebyrene helt og holdent.


For å motta en betaling må du generate en `Lightning-faktura`:


1. angi beløpet du ønsker å motta i Bitcoin (BTC), Satoshis (Sats) eller en fiat-valuta.

2. legg til en merknad **(valgfritt):** Legg til et notat eller en merknad. Dette vil bli lagt inn i fakturaen og vises i transaksjonshistorikken når betalingen er fullført, noe som gjør det enklere å identifisere den.

3. `Invoice Gyldighet`**:** Lynfakturaen er tidssensitiv og utløper etter **12 timer**. Hvis den ikke betales innen denne perioden, blir den ugyldig, og du må generate en ny.


Gi avsenderen fakturaen ved å kopiere den til utklippstavlen eller ved å la dem skanne QR-koden som vises på skjermen din.


![image](assets/en/13.webp)


## 9️⃣ Sende midler


Du kan åpne sendeskjermen direkte fra startsiden eller fra hvilken som helst av lommebøkene dine. Bull Bitcoin Wallet forenkler prosessen ved automatisk å oppdage destinasjonsnettverket - `Bitcoin`, `Liquid` eller `Lightning` - basert på adressen eller fakturaen du skriver inn, enten den er limt inn eller skannet via QR-kode.


### On-Chain-overføring via Bitcoin-nettverket


Å sende penger on-chain betyr at transaksjonen din registreres direkte i Bitcoin-blokkjeden. Denne metoden er best for større overføringer eller overføringer som ikke er tidssensitive. For å begynne kan du trykke på `Send-knappen` nede til høyre, og skanne eller skrive inn en `standard Bitcoin-adresse`.


Hvis adressen du oppgir ikke inkluderer et spesifikt beløp, blir du bedt om å fylle ut detaljene på send-skjermen. Du kan angi beløpet i den enheten du foretrekker, for eksempel BTC, satoshis eller en fiat-ekvivalent. Du kan også legge til en personlig merknad, som er et privat notat som du kan bruke som referanse for å identifisere transaksjonen senere. Dette notatet deles ikke med mottakeren.


Hvis betalingsforespørselen du skanner eller limer inn allerede inneholder alle nødvendige opplysninger, for eksempel en BIP21 URI med et forhåndsdefinert beløp, vil wallet derimot omgå skjermbildet for dataregistrering og ta deg direkte til bekreftelsesskjermbildet for å godkjenne betalingen.


![image](assets/en/14.webp)


Før transaksjonen sendes, får du opp en bekreftelsesskjerm. Det er viktig at du tar deg tid til å gå nøye gjennom alle parametere, og at du legger merke til mottakeradressen, beløpet som sendes og nettverksavgiftene. Dette skjermbildet inneholder også kraftige verktøy for å tilpasse transaksjonen.


Du kan kontrollere gebyrene på to måter. Den første metoden er å velge ønsket transaksjonshastighet, for eksempel lav, middels eller høy, og wallet beregner automatisk det aktuelle gebyret for deg. Den andre metoden gir mer presis kontroll ved at du kan angi et spesifikt gebyr, enten som en absolutt sum i satoshis eller som en relativ sats per byte, som deretter gir en estimert bekreftelsestid.


For avanserte brukere tilbyr wallet flere innstillinger for å finjustere transaksjonen. "Replace-by-Fee" (RBF) er aktivert som standard, noe som er en verdifull funksjon som gjør at du kan fremskynde en transaksjon hvis den blir sittende fast i mempoolen, ved å sende den på nytt med et høyere gebyr. Du kan også velge manuelt hvilke UTXO-er (Unspent Transaction Outputs) du vil bruke penger fra. Dette er et kraftig verktøy for UTXO-konsolidering, en strategi der du kombinerer flere små innganger til én enkelt større. Selv om dette kan koste mer i gebyrer for den aktuelle transaksjonen, kan det redusere gebyrene for fremtidige transaksjoner betydelig, spesielt hvis nettverksgebyrene forventes å stige.


![image](assets/en/15.webp)


PayJoin forsøkes automatisk når du skanner en betalingsforespørsel fra en mottaker (en BIP21 URI) som inneholder en `pj=`-parameter. Hvis du bare limer inn en vanlig adresse uten ekstra parametere, blir ikke denne funksjonen aktivert. Denne samarbeidsmetoden forbedrer personvernet ved å kombinere input fra både avsender og mottaker, noe som bryter med heuristikken om felles input-eierskap og muliggjør bedre skalering og gebyrbesparelser i noen tilfeller.


### Sending til Liquid Network


Liquid Network er utviklet for raske, konfidensielle transaksjoner med minimale gebyrer. Når du sender penger via Liquid, blir de trukket fra din `Instant Payments Wallet`. Prosessen er enkel: Du skriver bare inn eller skanner mottakerens `Liquid-adresse`.


Hvis adressen ikke angir et beløp, blir du bedt om å oppgi et beløp på sendeskjermen. Du kan angi beløpet i BTC, satoshis eller fiat. En viktig fordel med Liquid er den lave minimumsgrensen. Som med on-chain-transaksjoner kan du legge til en valgfri personlig merknad for dine egne registreringer. Hvis betalingsforespørselen allerede inneholder et beløp, vil wallet gå direkte til bekreftelsesskjermen.


På bekreftelsesskjermen for en Liquid-transaksjon ser du detaljene. Gebyrene er bemerkelsesverdig lave og beregnes ut fra hvor kompleks transaksjonen er. De ligger vanligvis på rundt 0,1 sat/vB, noe som for en enkel transaksjon utgjør bare 20-40 satoshis (for eksempel 26 satoshis per 21. desember 2025).


![image](assets/en/16.webp)


### Sende til Lightning Network


Du kan enten skanne en Lightning Address (f.eks. `runningbitcoin@rizful.com`), som lar deg angi beløpet og en valgfri merknad til mottakeren, eller skanne en faktura med et forhåndsdefinert beløp, som tar deg direkte til bekreftelsesskjermbildet.


*Merk at minimumsbeløp og gebyrer gjelder*


Bull Bitcoin Wallet sender Lightning-betalinger ved å ta ut midler fra din `Instant Payments Wallet` (på Liquid) og bytte dem via `Boltz`. Denne hybridtilnærmingen er helt selvforvaltende og unngår de høye on-chain-gebyrene for å administrere en dedikert Lightning-kanal, men den krever at du betaler et `byttegebyr`. Den laveste kostnaden får du ved å sende direkte til en mottakers Liquid-adresse hvis de også bruker en Bull Bitcoin wallet.


## 🔟 Overføring av penger mellom lommebøker


Bull Bitcoin lar deg flytte din Bitcoin mellom din `Secure Bitcoin` wallet og din `Instant Payments Wallet` på Liquid Network eller til en `ekstern Wallet`. For å utføre en overføring navigerer du ganske enkelt til `Overføring`-delen, velger kilde- og destinasjonslommebøker, angir beløpet du ønsker å flytte, og bekrefter transaksjonen.


![image](assets/en/17.webp)


## 1️⃣1️⃣ Gjenopprette din Bull Bitcoin Wallet


Denne delen forklarer hvordan du får tilgang til Bull Bitcoin Wallet-pengene dine igjen hvis du mister enheten din, avinstallerer appen eller bare må bytte til en ny. Som allerede forklart, finnes det to primære metoder for gjenoppretting: ved hjelp av den unike `Recoverbull`-metoden og ved hjelp av en standard `BIP39 seed-frase`.


### Metode 1: Recoverbull


Oppsummering: Wallet-sikkerhetskopier krypteres lokalt. Den krypterte filen kan lagres i skylagring eller på en annen enhet. Krypteringsnøkkelen lagres av Recoverbull Key Server. Begge holdes atskilt og må kombineres for å gjenopprette en wallet.


For å starte vil jeg slette Wallet med alle midler på den og installere wallet på nytt. Vi vil lande på `Velkomstskjermen` igjen. Denne gangen velger du alternativet `Recover Wallet`. Naviger deretter til metoden `Encrypted Vault`, bekreft ved hjelp av `Default Key server`, og velg plasseringen eller `Vault provider` der du lagret sikkerhetskopifilen.


![image](assets/en/18.webp)


Det står at hvelvet ble importert. Trykk på "Dekrypter hvelv"-knappen og skriv inn PIN-koden. Det neste skjermbildet viser saldoen din og antall transaksjoner som ble gjenopprettet.


![image](assets/en/19.webp)


### Metode 2: Seed Phrase


Denne metoden bruker wallets hovedgjenopprettingsfrase, en standard 12-ordsliste som fungerer som den ultimate sikkerhetskopien for pengene dine. Det er den mest universelle måten å gjenopprette en Bitcoin wallet på, ettersom den ikke er knyttet til noen bestemt tjeneste eller server. Så lenge du har denne frasen, kan du gjenopprette wallet på en hvilken som helst kompatibel enhet, selv uten tilgang til Bull Bitcoin-nøkkelserveren.


Fra velkomstskjermbildet velger du "Gjenopprett Wallet". Denne gangen velger du metoden `Fysisk sikkerhetskopiering`. Appen viser et rutenett med ord. Velg nøye hvert ord i den 12-ord lange seed-frasen din i riktig rekkefølge. Vær nøye, da en eneste feil vil resultere i en feilaktig wallet.


## 1️⃣2️⃣ Koble til en Hardware Wallet


For å oppnå det høyeste sikkerhetsnivået velger mange Bitcoin-brukere å lagre pengene sine i "kald lagring". Dette betyr at de `private nøklene` som styrer Bitcoin-en din, oppbevares på en enhet som aldri er koblet til Internett. En `hardware wallet` (eller signeringsenhet) er en spesialisert fysisk enhet som er designet for akkurat dette formålet. Den fungerer som et digitalt hvelv for nøklene dine, og sørger for at de aldri blir utsatt for de potensielle truslene fra en datamaskin eller smarttelefon på nettet.


Ved å koble en maskinvare-wallet til Bull Bitcoin-appen får du det beste fra to verdener: den kompromissløse sikkerheten ved kald lagring av de private nøklene dine, kombinert med de kraftige funksjonene og det brukervennlige grensesnittet til Bull Bitcoin wallet for visning av saldoer og håndtering av transaksjoner. I dette siste kapittelet viser vi deg hvordan du kobler en maskinvare-wallet, for eksempel et [Coldcard Q](https://coldcard.com/q), til din Bull Bitcoin wallet. Denne veiledningen går ikke i dybden på hvordan du konfigurerer et Coldcard Q; det kan du lese mer om her:


https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

### Importerer en Wallet


![image](assets/en/26.webp)


Først velger du `Eksporter Wallet` fra hovedmenyen på Coldcard Q, og deretter velger du `Bull Wallet`. Coldcardet ditt vil generate en QR-kode.


![image](assets/en/20.webp)


Åpne Bull Bitcoin Wallet og naviger til `Innstillinger` > `Bitcoin-innstillinger` > `Importer wallet` og velg `Kortkort Q` på telefonen, og trykk på `Åpne kameraet` for å skanne denne QR-koden for å importere de offentlige nøklene til maskinvare-wallet.


![image](assets/en/21.webp)


### Mottak med Coldcard Q


For å motta Bitcoin ved hjelp av det tilkoblede Coldcard Q trenger du ikke at enheten er fysisk koblet til telefonen din. Bull Bitcoin Wallet har allerede importert de nødvendige offentlige nøklene, slik at den kan sende generate-adresser på egen hånd.


1. Trykk på den importerte Coldcard Q-signeringsenheten, og velg "Motta".

2. Appen vil automatisk vise en ny Bitcoin-adresse fra Coldcardets wallet.

3. Bruk denne adressen til å motta penger. Bitcoin vil bli sikret direkte til maskinvaren wallets nøkler, selv om enheten var frakoblet under prosessen.


![image](assets/en/22.webp)


### Sende med Coldcard Q


Når du sender Bitcoin med Coldcard Q, må du godkjenne transaksjonen med en fysisk bekreftelse. Mens Bull Wallet-appen brukes til å opprette transaksjonen, kan den endelige signaturen bare opprettes på selve maskinvaren wallet.


Til å begynne med åpner du `Coldcard Q` wallet og trykker på `Send`. Deretter åpner du kameraet for å skanne QR-koden til mottakeradressen. Etter skanning angir du beløpet du vil sende, og justerer gebyrprioriteten etter behov.


Du finner flere alternativer under Avanserte innstillinger. Her finner du alternativet "Erstatt med gebyr" (RBF), som er aktivert som standard og lar deg fremskynde en fastlåst transaksjon senere. Du har også alternativet `Coin Control`, som lar deg manuelt velge de spesifikke UTXO-ene du ønsker å bruke.


Når du har gått gjennom alle detaljene, trykker du på `Vis PSBT` for å forberede transaksjonen.


![image](assets/en/23.webp)


Trykk på "Skann"-knappen på Coldcard Q, og bruk kameraet til å skanne QR-koden som vises på telefonen. Coldcard-skjermen vil da vise deg alle transaksjonsdetaljene. Kontroller nøye beløpet, mottakeradressen og endringsadressen din. Hvis alt er riktig, trykker du på `Enter`-knappen på Coldcard Q for å signere transaksjonen. Deretter vises en QR-kode av den signerte transaksjonen på skjermen.


![image](assets/en/24.webp)


På Bull wallet trykker du på `Jeg er ferdig`, og deretter trykker du på `Kamera` for å skanne QR-koden til den `signerte transaksjonen` fra Coldcard Q. Bull Wallet viser nå et sammendragsskjermbilde av den signerte transaksjonen. Gå gjennom den en siste gang, og trykk deretter på `Broadcast` Transaction`. Dette fullfører prosessen ved å sende transaksjonen til Bitcoin-nettverket, og pengene dine vil være på vei.


## 🎯 Konklusjon


Du har nå fullført reisen gjennom Bull Bitcoin Wallet. Appen gir deg kraftige personvern- og sikkerhetsverktøy rett ved fingertuppene, og gjør avanserte funksjoner enkle å bruke. Den hjelper deg med å holde deg privat med funksjoner som `PayJoin`, som skjuler transaksjonene dine på blokkjeden, og `Tor-integrasjon`, som maskerer nettverksaktiviteten din fra nysgjerrige øyne. For de som ønsker full kontroll, kan du koble deg til din "egen personlige Bitcoin-node" for å slutte å være avhengig av tredjepartsservere, og bruke en "maskinvare-wallet" for å holde de private nøklene dine helt offline og trygge. Med smarte alternativer for sikkerhetskopiering og sømløs støtte for Bitcoin, Liquid og Lightning er Bull Bitcoin Wallet et sterkt alt-i-ett-valg for alle som er opptatt av å holde pengene sine private, sikre og helt under egen kontroll.


## 📚 Bull Wallet Ressurser


[Github](https://github.com/SatoshiPortal/bullbitcoin-mobile) | [Website](https://www.bullbitcoin.com/)| [Recoverbull](https://recoverbull.com/)