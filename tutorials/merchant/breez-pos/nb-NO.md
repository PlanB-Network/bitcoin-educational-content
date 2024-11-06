---
name: Breez point of sales

description: Guide for å begynne å akseptere bitcoin ved bruk av Breez POS
---

![cover](assets/cover.webp)

_Denne teksten kommer fra Breez dokumentasjonsnettsted: https://doc.breez.technology/How-to-Get-Started-with-Breez-POS.html_

## Hva er Breez POS?

**Breez** er en fullservice, ikke-forvaringsbasert Lightning-app. La oss bryte det ned:

- **Lightning** er et bitcoin betalingsnettverk som reduserer transaksjonstider fra minutter til millisekunder og transaksjonsgebyrer fra flere dollar til noen få cent eller mindre. Lightning gjør bitcoin fra digitalt gull til digital valuta samtidig som alle fordelene som gjør bitcoin flott, bevares.
- **Ikke-forvaringsbasert** betyr at Breez ikke tar besittelse av brukernes penger. Mange Lightning-apper tar besittelse av brukernes penger. De er i bunn og grunn bitcoin-banker. Med en ikke-forvaringsbasert app som Breez, er alle brukere sine egne banker.
- **Fullservice** betyr at Breez tar seg av nesten alle de tekniske operasjonene automatisk og i bakgrunnen. Ting som kanalopprettelse, innkommende likviditet og ruting forblir under panseret. (Men Breez er også åpen kildekode, så de som er interessert i å revidere teknologien, er velkommen til å gjøre det!)

**Breez POS** er kort for vår point-of-sale-modus. Med andre ord fungerer Breez som en digital kasse for bedrifter og handlende som ønsker å akseptere Lightning-betalinger (i tillegg til sin "standard" modus, som er som den digitale versjonen av en lær-lommebok for bitcoin, og en neste-generasjons podcast-spiller). Nå skal vi se på hvordan du setter opp Breez som en Lightning-kasse for din bedrift.

## Hvordan komme i gang med Breez?

1. Det første steget er å laste ned appen. Den er tilgjengelig for Android og iOS (installer TestFlight og klikk på lenken fra enheten din).
2. Breez kan automatisk sikkerhetskopiere seg selv til Google Drive, iCloud, eller hvilken som helst WebDav-server.
   > Merk at hver enhet kjører sin egen Lightning-node. Du kan kjøre POS-modus på så mange enheter du vil, men saldoene vil forbli separate.
3. Med appen åpen, klikk på ikonet øverst til venstre for å finne Point of Sale-modus.

## Sette opp POS

1. Klikk på det ikonet øverst til venstre, og klikk Point of Sale > POS-innstillinger.

### Managerpassordet

I POS-innstillingene har du muligheten til å opprette et managerpassord. Managerpassordet gjør det umulig å sende utgående betalinger fra Breez-appen uten autorisasjon. Salgspersonell vil kun kunne motta betalinger fra enheten. Merk at hvis du bruker dette alternativet, vil du kanskje også forhindre tilgang til Breez sin sikkerhetskopi, så bruk av en ekstern WebDav-konto (f.eks. Nextcloud) anbefales for dette bruksområdet.

### Varelisten

Varelisten er en katalog over varer til salgs og deres priser. Det er to måter å legge til varer på listen:

- For å legge inn varer én om gangen, klikk på Varer nær toppen av hoved-POS-visningen, deretter på "+"-tegnet nederst til høyre. Her kan du angi navnet på en enkelt type vare, prisen (vist i valutaekvivalenten av ditt valg), og SKU (en unik intern identifikator for den typen vare; det er valgfritt).
- For å legge inn mange varer samtidig, klikk på kalkulatorikonet øverst til venstre, deretter Salgspunkt > Innstillinger > POS-innstillinger, og klikk så på de tre prikkene til høyre for Vareliste, og deretter på Importer fra CSV. Dette vil tillate deg å importere en CSV-fil som du har forberedt på forhånd som inneholder navnene, prisene, og SKUene til varene dine.

### Fiat-visning

Breez sender og mottar kun bitcoin, og for de fleste transaksjoner på Lightning, som ofte er for mindre beløp, vises summen vanligvis i Satoshis, også kjent som sats (1 BTC = 100,000,000 sats). Men mange handlende finner det praktisk å kunne se (og fortelle kundene) verdien av kjøpet vist i lokal fiat-valuta.

I hoved-POS-visningen er valutaen som for øyeblikket vises synlig på høyre side (standard er SAT). Det er også en nedtrekksliste med andre valutaer tilgjengelig for visning. For å legge til eller fjerne valutaer fra denne nedtrekkslisten, klikk på Salgspunkt > Innstillinger > Fiat-valutaer. Merk deretter av for valutaene du ønsker å ha i nedtrekksmenyen din og fjern merkingen for de du ønsker å utelate.

Verdiene som vises er fra yadio, en respektert kilde for valutakursdata, og de oppdateres i nær sanntid. Men husk: uansett hvilken valutaverdi som for øyeblikket vises, er betalingen selv i bitcoin.

### Ta betalt for en ordre

For å sette sammen ordren, legg til varer fra varelisten eller skriv rett og slett inn et beløp på tastaturet. Klikk deretter på Ta betalt øverst i hoved-POS-visningen. Du vil da se en QR-kode som kunden kan skanne med sin Lightning-app, som du kan dele direkte fra en annen app på enheten din, eller som du kan kopiere og lime inn der det er nødvendig.

Ved å skanne den koden eller klikke på den delte/limte inn fakturaen, vil kunden se fakturaen i sin Lightning-app og ha muligheten til å betale den og umiddelbart gjennomføre transaksjonen.

Når du ser animasjonen Betaling godkjent! i Breez-appen på handlende sin enhet, kan du klikke på skriverikonet for å generere en kvittering for kunden. For å bruke en kvitteringsskriver i Android, prøv å bruke denne driveren. Merk at du også kan skrive ut tidligere transaksjoner via Transaksjoner-skjermen.

### Salgsrapport

For å se en daglig/ukentlig/månedlig rapport av salgene dine (for regnskapsformål eller andre), klikk på ikonet øverst til venstre, og deretter klikk på Transaksjoner. Klikk på Rapport-ikonet for å vise rapporten og Kalender-ikonet for å endre det valgte datoområdet.

### Eksportere transaksjoner

For å se en liste over mottatte betalinger i Breez, klikk på ikonet øverst til venstre, og deretter klikk på Transaksjoner. Klikk på de tre prikkene øverst til høyre, deretter på Eksporter for å eksportere en liste over innkommende betalinger i CSV-format. For å begrense listen til en viss periode, klikk på kalenderikonet for å sette et datoområde.

### Skrive ut kvitteringer

For å skrive ut en salgskvittering, klikk på skriverikonet øverst til høyre i dialogboksen for betalingsbekreftelse. Alternativt, klikk på ikonet øverst til venstre, og deretter klikk på Transaksjoner. Finn salget du vil skrive ut, åpne det, og klikk på skriverikonet øverst til høyre.

> Merk: bruk denne driveren for å skrive ut på en bærbar 58mm/80mm Bluetooth/USB termisk skriver.

## Jeg vil lære mer

- For mer informasjon om Lightning og Breez, sjekk ut vår [blogg](https://breez.technology/blog).
- For flere tekniske tips om hvordan du får mest mulig ut av appen og utfører vanlige operasjoner, sjekk ut vår [dokumentasjon](https://breez.technology/documentation).
- Hvis du står fast og ikke finner svaret i noen av våre hjelpedokumenter, kan du finne oss på [Telegram](https://t.me/breez_labs) eller sende oss en [e-post](mailto:support@breez.technology).
- Hvis du ønsker å se noen demonstrasjonsvideoer av Breez POS-modusen i aksjon laget av våre fans og brukere, [her](https://www.youtube.com/watch?v=xxxx) er en flott kort en, og [her](https://www.youtube.com/watch?v=xxxx) er en lengre, mer detaljert en.