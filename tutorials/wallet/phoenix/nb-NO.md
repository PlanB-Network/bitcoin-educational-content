---
name: Phoenix

description: Oppsett av din Phoenix-lommebok
---

![phoenix](assets/cover.webp)

## Introduksjon

Phoenix er en ikke-forvaringsbasert lynlommebok skapt av Acinq, teamet bak Lightning Eclair-implementasjonen.

Husk at Phoenix er en mobilapp fokusert på lynbetalinger, men støtter fortsatt betalinger på kjeden, gjennom integrerte bytter. Dette betyr at ethvert innskudd på kjeden til Phoenix, vil bli byttet øyeblikkelig til en lynkanal.

Også hvis du ønsker å sende til en adresse på kjeden, vil Phoenix gjøre byttet internt fra din LN-kanal til destinasjonen på kjeden. Vær oppmerksom, alle disse byttene har en kostnad, fordi de involverer en avgift på kjeden.

Nedenfor i "Kom i gang-guiden" seksjonen vil vi gå gjennom oppsettsprosessen og også forklare mer om hvordan du kan håndtere lynlikviditeten med Phoenix.

## Viktige ressurser
- Phoenix offisielle nettside - [https://phoenix.acinq.co](https://phoenix.acinq.co)
- Dokumentasjon / FAQ-side - [https://phoenix.acinq.co/faq](https://phoenix.acinq.co/faq)
- [Github-side](https://github.com/ACINQ/phoenix/) | [Github utgivelser-side](https://github.com/ACINQ/phoenix/releases) (last ned apk direkte)
- [Støtte og diskusjoner](https://github.com/ACINQ/phoenix/discussions)
- [Acinq-blogg](https://acinq.co/blog) - kunngjøringer

## Videoveiledning

![Phoenix: Bitcoin Lightning Wallet Tutorial](https://youtu.be/cbtAmevYpdM?si=zctujxtI0hI-jKpC)

## Kom i gang-guide

Her er en steg-for-steg-guide om hvordan du starter med Phoenix, oppsett, gjøre / motta betalinger, håndtere likviditeten, sikkerhetskopiere / gjenopprette prosessen.

### Last ned & Sett opp
Du kan laste ned og installere Phoenix fra: [App Store](https://apps.apple.com/us/app/phoenix-wallet/id1544097028) | [Google Play Store](https://play.google.com/store/apps/details?id=fr.acinq.phoenix.mainnet) | [Direkte nedlasting apk](https://github.com/ACINQ/phoenix/releases)

Følg instruksjonene som starter med velkomstskjermen, steg for steg.

![](assets/screenshot2.webp)

Du vil bli informert om automatisk opprettelse av lynkanaler.
Fra og med v2.0 er en større oppgradering som bringer "splicing" til Phoenix:
- enkelt dynamisk kanal,
- ikke mer 1% avgift på innkommende likviditet
- bedre forutsigbarhet og kontroll
- tillitsløse bytter

Sjekk [Phoenix blogginnlegg](https://acinq.co/blog/phoenix-splicing-update) for flere detaljer, spesielt den nye avgiftsmodellen.

![](assets/screenshot3.webp)

### Lynlikviditet hurtigguide

Så når du mottar / setter inn sats i denne lommeboken, vil den automatisk åpne kanaler med ACINQ-node. Vanligvis vil størrelsen på kanalene være litt større enn beløpet du satte inn. Så du vil alltid ha en ny kanal for hvert innskudd, bortsett fra at når du ikke har helt tømt kanalen og du mottar en mindre betaling, vil den bli påfylt.

For Phoenix Lightning likviditet vil vi foreslå følgende scenario:

Med den nye versjonen v0.2.0 den nye LN-funksjonen splicing. Det betyr at fra nå av vil du ikke måtte håndtere mange nye små kanaler for hver betaling mottatt.

Hvis det ikke er nok innkommende likviditet, vil Phoenix øke størrelsen på din opprinnelige kanal, men det vil fortsatt medføre en avgift på kjeden. Du kan uansett sette opp den avgiften i Phoenix-innstillinger, betalingsalternativer og avgifter.
Så vi foreslår å starte med å bruke Phoenix med en stor kanal, som 1-3-5M sats. Dine forpliktelsesgebyrer vil være ubetydelige sammenlignet med størrelsen på kanalen og vil ikke påvirke deg for mye. Også i stedet for å betale 4-5 ganger (eller hvor mange ganger du setter inn små beløp) et minst 3000 sats gebyr for hver innskudd, vil du bare betale én gang åpningskanalgebyret.
Hvis du begynner å bruke fra den kanalen, ikke bruk alt, fordi Phoenix vil lukke den.

Hvis du lar noen sats i kanalen og gjør en annen påfylling fra en annen LN-lommebok / innskuddskilde, har vi to situasjoner å vurdere:
- med et nytt innskuddsbeløp større enn kanalkapasiteten din, vil Phoenix endre størrelsen på kanalen og du vil betale et ekstra gebyr.
- med et nytt innskuddsbeløp lavere enn kanalkapasiteten din, vil det ikke være noen gebyrer involvert.

Så prøv å dimensjonere din opprinnelige kanalkapasitet til dine personlige behov for utgifter. Å bruke og erstatte innenfor grensene av kanalen vil ikke medføre flere gebyrer, og opplevelsen av å bruke denne lommebokappen vil være jevn.

### Sikkerhetskopi
På følgende skjerm vil du bli informert om at Phoenix-appen vil generere en seed-frase som sikkerhetskopi for lommeboken din. Senere MÅ disse seed-ordene lagres på et sikkert sted!

![](assets/screenshot4.webp)

Den følgende skjermen indikerer om du vil opprette en ny lommebok eller gjenopprette en tidligere lommebok, fra seed-frase.

![](assets/screenshot5.webp)

Når den nye lommeboken er opprettet, blir du varslet om at du bør ta sikkerhetskopi av seed-frasen. Klikk på "Sikkerhetskopier lommebok"-knappen.

![](assets/screenshot6.webp)

Du vil bli varslet om at disse ordene fra seeden er veldig viktige og sensitive, og du bør holde dem private.

![](assets/screenshot7.webp)

Disse seed-ordene MÅ du lagre dem på et sikkert sted, som en passordbehandler ([KeePass](https://keepass.info/) eller [Bitwarden](https://bitwarden.com/)), og holde databasen til denne passordbehandleren på en offline USB-kryptert pinne for total sikkerhet.

![](assets/screenshot8.webp)

### Motta betalinger

Før du begynner å motta, vennligst les kapittelet ovenfor "Liquidity Quick Guide".

Så nå er du klar til å motta sats i din Phoenix-lommebok!

![](assets/screenshot9.webp)

For å motta en betaling, i Phoenix har du følgende alternativer:
- ved å bruke den viste QR-koden, som representerer en "tom" Lightning-faktura
- ved å redigere Lightning-fakturaen (se redigeringsknappen under QR-koden), hvor du kan legge til et beløp sats, legge til en kommentar vist til betaleren
- ved å bruke / skanne en LNURL-uttak QR-kode
- ved å generere en on-chain Bitcoin-adresse fra din Phoenix-lommebok. Husk at denne betalingen vil bli "konvertert" til en ny Lightning-kanal (hvis du ikke har åpnet en ennå) eller endre størrelsen på en eksisterende Lightning-kanal.

![](assets/screenshot10.webp)

Skjerm vist for å redigere en ny Lightning-faktura og generere en ny QR-kode for den:

![](assets/screenshot11.webp)

Dette er skjermen hvor du kan generere en on-chain BTC-adresse og informeres om at betalingen til denne adressen vil bli "konvertert" til lightning-likviditet og involvere noen gebyrer.

![](assets/screenshot12.webp)

Når betalingen var gjort, vil en bekreftelsesskjerm vises, alt gjort!

![](assets/screenshot13.webp)
Valgfritt kan du legge til en personlig merknad til hver mottatt betaling. Disse notatene lagres ikke noe annet sted, de beholdes kun på enheten din. Hvis du gjenoppretter din Phoenix-lommebok, vil ikke disse notatene bli gjenopprettet. Dette er en nyttig funksjon for å holde oversikt over dine sendte og mottatte betalinger.
![](assets/screenshot14.webp)

### Send betalinger

Å sende betalinger er en ganske enkel prosess, bare klikk på hovedskjermknappen "Send"

![](assets/screenshot15.webp)

Du vil bli bedt om å tillate Phoenix-appen å få tilgang til enhetens kamera, for å kunne skanne QR-koder.

![](assets/screenshot16.webp)

På betalingsskjermen har du 3 alternativer:
- skann en QR-kode fra en mottakers Lightning-faktura / LNURL
- manuelt inntasting (lim inn), Lightning-adresseinntasting eller LNURL-betalingskode
- last inn et QR-bilde fra lokal disk

![](assets/screenshot17.webp)

Som du kan se på denne skjermen, ble betalingsforespørselen skannet og detaljene er allerede fylt inn. Du trenger bare å trykke på "Betal"-knappen.

![](assets/screenshot18.webp)

Når betalingen er sendt og bekreftet, vil en bekreftelsesskjerm med korte detaljer om betalingen vises, inkludert gebyret som ble betalt. Hvis du vil se flere betalingsdetaljer, klikk på "Detaljer"-knappen.

![](assets/screenshot19.webp)

På detaljskjermen kan du se de tekniske detaljene om betalingen, inkludert: betalingshash og forespørsel, preimage, destinasjonsnode og varighet. Noen ganger er disse detaljene nyttige for å spore betalinger, feilsøke eller identifisere en spesifikk betaling med mottakeren.

![](assets/screenshot20.webp)

### Innstillinger

I Innstillinger-menyen er det ikke så mye å gjøre, Phoenix går for enkelhet. Men et viktig aspekt her er menyen for å administrere betalingskanaler og gebyrer, hvor du kan sette dine ønskede nivåer av gebyrer. Husk at i et mempool høyt gebyrmiljø bør du ikke bruke veldig lave gebyrer, ellers vil dine betalinger og åpning av kanaler bli forstyrret og/eller mislykkes.

Andre alternativer i Innstillinger-menyen:
- Visning - for å bytte til forskjellige fargetemaer
- Electrum-server - for å sjekke statusen til Electrum-serveren du er koblet til eller spesifisere en
- Tor - hvis du vil bruke Phoenix bak Tor-nettverket
- App-tilgangsinnstillinger - angi tillatelser for Phoenix til spesifikke enhetstjenester
- Gjenopprettingsfrase - hvis du vil sjekke seed-ordene og/eller lage en ny sikkerhetskopi
- Kanalliste - vis statusen til dine Lightning-kanaler og likviditet (inn/ut) tilgjengelig
- Logger - vis feilsøkingslogger
- Lukk alle kanaler - Farlig alternativ som BØR brukes KUN i tilfelle du ønsker å stenge din Phoenix-node for godt og gjenopprette midlene til din onchain-adresse. Den adressen kan senere hentes ved hjelp av Electrum-lommeboken, ved å bruke din Phoenix seed-frase.

![](assets/screenshot21.webp)

### Tilbakestille

Hvis du er i en situasjon der din Phoneix-app har problemer (ikke gjør betalinger, ikke kobler til Electrum-servere, kan ikke motta betalinger) eller du rett og slett ønsker å flytte den til en annen enhet, MÅ du være sikker på to aspekter:
- ha en sikkerhetskopi av din seed-frase
- stopp appen på enheten din - gå til appdetaljer og tving stopp tjenesten
- avinstaller den fra den gamle enheten hvis du vil flytte den til en ny
- IKKE kjør samme Phoenix-lommebok på flere enheter!

![](assets/screenshot22.webp)

Når du installerer den på nytt eller installerer den på de nye enhetene, klikk på "Gjenopprett"-knappen og følg instruksjonene

![](assets/screenshot23.webp)
Du kan ikke bruke en annen type frø, generert fra andre lommebok-apper. [Se mer detaljer her](https://walletsrecovery.org/) om andre lommeboktyper og deres type frø og avledningssti. Ikke alle er kompatible!
![](assets/screenshot24.webp)

Du må legge inn frøordene du tidligere har lagret, ett etter ett, i den spesifikke rekkefølgen. Når du er ferdig med å legge inn de 12 ordene, klikk på "Importer"-knappen og voilà.

![](assets/screenshot25.webp)

I løpet av få øyeblikk vil du se din tidligere saldo vist. Du vil også få en varsling om å ta sikkerhetskopi av ditt frø. Du kan bare gå til menyen og velge "Jeg har lagret sikkerhetskopien" hvis du allerede har gjort det.

![](assets/screenshot26.webp)

Ferdig! Lykkelig Lyn!