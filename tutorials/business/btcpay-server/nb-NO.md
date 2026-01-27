---
name: BTCPay Server
description: Godta BTC-betalinger uten mellomledd
---

![cover](assets/cover.webp)



![video](https://youtu.be/KqsM-n-e4aY)



BTCPay Server er en gratis programvarepakke med åpen kildekode laget av Nicolas Dorier som gjør det mulig å akseptere bitcoin-betalinger uten mellomledd. Den er designet for å tilby autonomi og økonomisk suverenitet, installeres på sin egen server og gir komplett transaksjonshåndtering, fra fakturering til validering av on-chain- eller Lightning Network-betalinger og regnskap. Den integreres enkelt med e-handelsnettsteder (WooComerce, Shopify osv.) eller kan brukes som betalingsterminal for fysiske butikker (*POS*).



BTCPay Server er uten tvil den mest avanserte løsningen for selgere som ønsker å ta imot bitcoin. Det er den mest omfattende og robuste programvaren når det gjelder sikkerhet, suverenitet og konfidensialitet. På den annen side er det også den mest komplekse å installere og vedlikeholde. Det finnes også enklere alternativer: Noen er helt depotbaserte, som OpenNode, mens andre tilbyr et interessant kompromiss mellom brukervennlighet og suverenitet, som sveitsiske Bitcoin Pay :



https://planb.academy/tutorials/business/point-of-sale/swiss-bitcoin-pay-2-a78b057e-ed11-47ac-860c-71019fcb451a

Målet med denne veiledningen er å veilede deg trinn for trinn gjennom installasjon, konfigurasjon og bruk av BTCPay Server, slik at du kan distribuere en sikker, uavhengig betalingsinfrastruktur i tråd med Bitcoin-etikken.



## BTCPay Server-funksjoner



Sentraliserte Bitcoin-salgsstedsløsninger, som for eksempel *OpenNode*, tilbyr brukervennlighet, men er avhengige av et tredjepartsselskap siden de ikke kan være selvhostede og i de fleste tilfeller er proprietære. Selv om de gjør det enklere å sette opp betalinger, innebærer de provisjonsgebyrer og utsetter brukerne for større risiko enn en løsning som BTCPay Server, både når det gjelder oppbevaring av midler og konfidensialitet.



BTCPay Server er rettet mot nettbaserte eller fysiske selgere, foreninger og ideelle organisasjoner som ønsker å motta donasjoner i bitcoins. Det er også en ideell løsning for prosjekteiere og utviklere som ønsker direkte støtte fra samfunnet sitt.



De spesielle funksjonene til BTCPay Server inkluderer :




- sin **fullstendige autonomi**,
- fraværet av en **KYC**-prosedyre,
- full kontroll over midlene**,
- **eliminering av plattformavgifter**.



Ved å bli din egen betalingsbehandler eliminerer du enhver avhengighet av en sentralisert tredjepart mellom deg og kundene dine. Du kan ta imot betalinger direkte i bitcoins og generate-betalingsfakturaer. Dette sikrer at verken du eller selskapet ditt kan bli utestengt av noen andre. Du spiller rollen som både bank og betalingsbehandler, uten å måtte betale provisjon til en mellommann for hver transaksjon.



Transaksjonsgebyrene for **on-chain** består, men kan reduseres ved å bruke **Liquid**- eller **Lightning**-nettverket.



I tillegg :




- Grensesnitt og fakturaer som kan tilpasses fullt ut;
- Innebygd **Tor**-støtte for økt konfidensialitet;
- Støtte for **crowdfunding**, **POS** og **betalingsknapper**;
- Kompatibel med mange valutaer ;
- Bitcoin direktebetalinger og peer-to-peer-betalinger ;
- Full kontroll over de private nøklene dine;
- Forbedret personvern ;
- Forbedret sikkerhet ;
- Selvbetjent programvare ;
- Støtte for **SegWit** og **Lightning network** ;
- Intern, nodebasert portefølje, med integrering av maskinvareporteføljer.



## Installere og konfigurere BTCPay Server



### Velge hosting-modus



BTCPay Server kan installeres på en rekke forskjellige måter. Avhengig av dine behov og ressurser, finnes det tre hovedalternativer:




- BTCPay Server hostet av en tredjepart**: du bruker en plattform som hoster tjenesten for deg. Det er enkelt, men vanligvis ikke gratis.
- BTCPay Server er selvbetjent på en skyserver** (f.eks. via [btcpayprovider](https://btcpayprovider.com/), [Bitcoin People](http://bitcoinpeople.it/) eller en annen leverandør). Dette er den anbefalte løsningen for de fleste nybegynnere.
- BTCPay Server installert på din egen maskinvare (lokalt)**: på en datamaskin, mini-PC eller Umbrel. Denne metoden er mer teknisk, men gir total uavhengighet.



https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

For en nystartet forhandler er **distribusjon på en skyserver** det beste kompromisset mellom autonomi, enkelhet og sikkerhet, uten å måtte administrere hele den tekniske infrastrukturen.



BTCPay Server kan distribueres raskt fra en rekke hostingleverandører. Blant dem skiller **Voltage** seg ut som en referanseløsning for brukere som krever en **pålitelig**, **profesjonell** og **suveren** infrastruktur.



### Opprett en BTCPay Server-forekomst på Voltage



**Voltage** er en nøkkelferdig Bitcoin- og Lightning-hostingplattform som lar deg øyeblikkelig distribuere din egen BTCPay-server, uten kompleks konfigurasjon eller servervedlikehold.



Besøk [det offisielle nettstedet til Voltage](https://voltage.cloud).



![capture](assets/fr/03.webp)



Opprett en **brukerkonto** med en gyldig e-postadresse og et sterkt passord.



![capture](assets/fr/04.webp)



Voltage tilbyr en **gratis prøveperiode på 7 dager**. Vær oppmerksom på at etter vår 7-dagers gratis prøveperiode vil du bli invitert til å registrere deg for et fast abonnement på **25 USD per måned** for å fortsette å **holde nodene dine aktive**.



Når du har opprettet en Voltage-konto og logget inn for første gang, blir du omdirigert til startsiden, som har to hoveddeler:




- En **Infrastruktur**-seksjon for administrasjon av Lightning-noder, Bitcoin Core, BTCPay Server og andre Bitcoin-tjenester i skyen;
- og en **Payments**-seksjon som gir deg tilgang til Voltage's API Lightning for å integrere Bitcoin-betalinger i tilpassede applikasjoner.



For å distribuere din **BTCPay Server**-forekomst, klikk på **Access-infrastruktur**. Her kan du opprette, administrere og overvåke alle tjenestene dine, inkludert Bitcoin-noden og BTCPay Server.



#### Opprett en gruppe



Før du kan distribuere en tjeneste, vil plattformen be deg om å **opprette en gruppe**. En **gruppe** (arbeidsområde) er et arbeidsområde som grupperer alle Bitcoin- og Lightning-tjenestene dine (f.eks. en node, en BTCPay-server, en utforsker osv.). Det er litt som en mappe som inneholder de ulike prosjektene dine.



![capture](assets/fr/05.webp)



I denne veiledningen vil gruppen vi har opprettet hete **Genesis**. Du kan legge til et profilbilde hvis du ønsker det. Når dette er gjort, klikker du på knappen **Opprett**. Du kan invitere andre brukere til å bli med i gruppen, og du kan til og med endre gruppenavnet hvis du ønsker det.



På gruppens startside vises flere alternativer:




- Lightning Nodes** : for å distribuere en komplett Lightning-node (LND) ;
- Bitcoin Core Nodes** : for å starte en komplett Bitcoin-node ;
- BTCPay Server** : for å være vert for en BTCPay-forekomst som er klar til bruk;
- Nostr Accounts**: for å administrere Nostr-identiteter.



Aktiver **dobbel autentisering (2FA)** for å sikre kontoen og tjenestene dine (knappen er synlig i rødt hvis den er deaktivert).



![capture](assets/fr/06.webp)



Klikk på **BTCPay Server** blant alternativene, og deretter på **Launch a BTCPay Store**.



![capture](assets/fr/07.webp)



Voltage vil deretter be deg om å **opprette og konfigurere din BTCPay Server-forekomst** ved å velge et **tjenestenavn** (1) og aktivere Lightning-betalinger (2).



Du trenger en Lightning-node hvis du bestemmer deg for å godta Lightning-betalinger.



Hvis du ikke allerede har en Bitcoin- eller Lightning-node, vil Voltage foreslå at du oppretter en automatisk.



Klikk på **Opprett en Lightning-node** (3) .



![capture](assets/fr/08.webp)



Når du kommer til grensesnittet for oppretting av noder, blir du bedt om å velge mellom **standard** og **profesjonelt** oppsett.



Du kan opprette en ekte node (**Mainnet**) eller en testnode (**Testnet**). Klikk deretter på knappen **Fortsett**.



![capture](assets/fr/09.webp)



I denne veiledningen bruker vi standardplanen. Skriv inn **nodenavnet**, et **passord** og trykk på **Opprett**-knappen.



![capture](assets/fr/10.webp)



Etter noen få øyeblikk vil noden din være i drift, og du vil kunne åpne en gratis kanal med en mottakskapasitet på 500 000 sats.



![capture](assets/fr/11.webp)



Litt lenger ned til høyre finner du all informasjonen du trenger om knuten din!



![capture](assets/fr/12.webp)



Nå som vi har fått Lightning-noden vår i gang, la oss gå tilbake til å installere BTCPay-serveren vår. Du kan nå klikke på **Create BTCPay**-knappen.



![capture](assets/fr/13.webp)



Du får opp en side med standard påloggingsinformasjon og en melding der du blir bedt om å endre det opprinnelige passordet ditt. Når du har gjort dette, klikker du på knappen **Logg inn nå** for å få tilgang til grensesnittet ditt.



![capture](assets/fr/14.webp)



Nå er det klart! BTCPay-serveren din er klar til bruk. Du blir omdirigert direkte til BTCPay-serverens påloggingsside.



![capture](assets/fr/15.webp)



Når du har logget inn, konfigurerer du din første **butikk**:





- Gi det et **navn**.





- Velg **standardvaluta** (EUR, USD, CFA osv.).





- Velg en **valutakursleverandør** (f.eks. CoinGecko).



![capture](assets/fr/16.webp)



Du vil deretter bli omdirigert til butikkens dashbord. På dashbordet vil du legge merke til at **Opprett butikk**-knappen er merket med grønt, ettersom dette trinnet allerede er fullført.



![capture](assets/fr/17.webp)



Litt lenger ned har vi knappene **Konfigurer wallet** og **Konfigurer Lightning-node**. I vårt tilfelle har vi allerede koblet oss til en Lightning-node som kjører på spenning. Så vi trenger ikke å gjøre det her.



La oss gå videre til å konfigurere en portefølje. Klikk på knappen **Konfigurer en portefølje**.



Siden vi nettopp har kommet i gang med BTCPay Server, la oss koble til en eksisterende wallet. Så trykk på **Koble til en eksisterende portefølje**.



![capture](assets/fr/18.webp)



Deretter må du velge **importmetode**. Blant de tilgjengelige alternativene velger du **Enter extended public key**.



![capture](assets/fr/19.webp)



Ved å koble til en eksisterende wallet kan du motta betalingene dine **direkte på denne eksterne wallet**, uten at BTCPay-serveren har tilgang til den private nøkkelen din. Så selv om serveren skulle bli hacket eller den offentlige nøkkelen (`xpub`) kompromittert, kan en angriper se transaksjonshistorikken din, men det vil være **umulig å få tilgang til pengene dine**.



Når du klikker på knappen **Enter extended public key**, blir du **omdirigert** til siden der du må oppgi denne nøkkelen.



La oss nå hente den **utvidede offentlige nøkkelen**.



### Koble til en Bitcoin wallet



For å motta betalinger må du koble en Bitcoin wallet til butikken din. For å gjøre dette har du flere alternativer:





- Maskinvareportefølje** (Ledger, Trezor, Coldcard...) ;





- Programvareportefølje** (Blockstream App, Ashigaru, Electrum, Sparrow...)





- BTCPay Server** intern wallet (anbefales ikke, da det er mindre sikkert og eksponerer midlene dine mer i tilfelle serverhacking).



I denne veiledningen bruker vi en **programvareportefølje**, som er mer tilgjengelig for den første konfigurasjonen. Du kan velge mellom en rekke kompatible programmer: **Electrum**, **Phoenix**, **Zeus**, **Muun**, osv.



For demonstrasjonen bruker vi **Electrum**. Åpne **Electrum**, klikk på **Portfolio** og deretter på **Informasjon** :



![capture](assets/fr/20.webp)



Deretter kopierer du den **offentlige hovednøkkelen (xpub)**.



![capture](assets/fr/21.webp)



Når du har kopiert den offentlige hovednøkkelen, limer du den inn i feltet på BTCPay Server-siden.



![capture](assets/fr/22.webp)



Etter bekreftelse blir du omdirigert til butikkens dashbord.



![capture](assets/fr/23.webp)



### Generer et salgssted (PoS)



Når du har satt opp butikken og porteføljen din, kan du nå sette opp et **Point of Sale (PoS)** for å begynne å motta Bitcoin-betalinger direkte fra kundene dine.



Denne integrerte funksjonen i **BTCPay Server** er ideell for **selgere, håndverkere, restauratører eller tjenesteleverandører** som ønsker å ta imot Bitcoin **uten å ha et nettsted** eller spesielle tekniske ferdigheter.



### Hva er salgsstedet?



**PoS** er et **forenklet POS-grensesnitt** som fungerer som en **Bitcoin-betalingsterminal**.


Det gir deg mulighet til å :




- Opprett en **meny med produkter eller tjenester** med faste priser.
- Generer en **instantfaktura med QR-kode** som kan skannes.
- Del en **betalings-URL** som er tilgjengelig via smarttelefon, nettbrett eller datamaskin.



PoS gjør med andre ord BTCPay-serveren din til et **direkte salgsgrensesnitt**, der hver betaling mottas **i din egen Bitcoin wallet**, uten mellomledd.



### Konfigurere PoS



I BTCPay-dashbordet klikker du på **PLUGINS** og deretter på **Point of sale**.



Klikk deretter på **Opprett en ny PoS-applikasjon**. Denne handlingen legger til en **ny applikasjon** i BTCPay-butikken din, som om du skulle installere et internt minisalgssted.



En side åpnes for å opprette applikasjonen din. Definer et **applikasjonsnavn**: dette er et internt navn som kun er synlig fra dashbordet (f.eks. _Shoe Shop_).



Klikk på **Opprett** for å validere.



![capture](assets/fr/24.webp)



Når du har opprettet en konto, blir du videresendt til **Detaljert konfigurasjonsside** for Point of Sale.



### Tilpass salgsgrensesnittet ditt



På denne siden kan du definere de viktigste elementene i PoS-en din:





- Applikasjonsnavn** (internt administrasjonsnavn, kan endres når som helst).





- Visningstittel** (det kundene dine vil se øverst på siden).





- Point of sale style** (**Description**-modus er egnet for tjenester som hårklipp eller måltider, mens **Product catalog**-modus er ideell for butikker som tilbyr flere varer).





- Vis valuta** (velg **XOF**, **EUR** eller **USD** i henhold til dine vanlige priser).





- Produktliste** (legg til produkter, beskrivelser og priser her).



![capture](assets/fr/25.webp)



![capture](assets/fr/26.webp)



### Lagre og test PoS-en din



Når du er ferdig med å konfigurere, klikker du på **Lagre** for å lagre innstillingene, og deretter på **Vis** for å forhåndsvise PoS.



Du vil se en side som presenterer produktene dine, der hver knapp tilsvarer en vare eller tjeneste.



Så snart en kunde velger et produkt :



1. BTCPay genererer automatisk en Bitcoin- eller Lightning**-faktura.



2. En **QR-kode** vises på skjermen.



3. Kundene kan **skanne og betale direkte** med sin Bitcoin wallet.




![capture](assets/fr/27.webp)



### Endelig resultat



Du har nå et komplett **Bitcoin Point of Sale** som du kan :





- Åpne fra en smarttelefon eller et nettbrett i butikken din ;





- Vises på en skjerm som kunden kan skanne ;





- Eller del via en offentlig **URL**, for eksempel en forenklet bestillingsside.



Ved hver betaling krediteres beløpet automatisk til **din egen BTCPay wallet**, uten mellomledd eller tredjepartsgebyrer.


Dette gjør PoS-en din til en **selvstendig Bitcoin-betalingsterminal**.




## Hverdagsbruk



Før du tar ut reelle utbetalinger, anbefaler vi at du gjennomfører **en test** for å sjekke at alt fungerer som det skal.



### Test en betaling





- Opprett en faktura** fra PoS-grensesnittet (for eksempel et produkt på 1 satoshi eller et mindre beløp).





- Skann QR-koden** på skjermen med en Bitcoin eller Lightning wallet (for eksempel **Phoenix**, **Muun** eller **Wallet av Satoshi**).




![capture](assets/fr/28.webp)





- Valider betalingen** i wallet: Transaksjonen sendes umiddelbart.





- Gå tilbake til BTCPay Server**: fakturaen vil vises som **Betalt** i listen.



![capture](assets/fr/29.webp)



Gratulerer med dagen! Salgsstedet ditt er nå **funksjonelt**. Du kan begynne å motta Bitcoin-betalinger fra kundene dine, enkelt, raskt og uten mellomledd.



### Opprett en faktura for en kunde



I menyen **Fakturaer** klikker du på **Ny faktura**.



![capture](assets/fr/30.webp)



Angi **beløpet** og den **lokale valutaen** (BTCPay beregner automatisk motverdien i BTC), samt annen produktinformasjon.



![capture](assets/fr/31.webp)



Del **QR-koden** eller **URL** med kunden.



![capture](assets/fr/32.webp)



### Spor mottatte betalinger



I menyen **Fakturaer** ser du fremdeles en liste over alle transaksjonene dine.


De mulige statusene er :





- Avventer**: betalingen er ennå ikke bekreftet.





- Betalt**: betaling bekreftet.





- Utløpt**: faktura som ikke er betalt innen forfallsdato.



### Tilbakebetaling av en kunde



I menyen **Fakturaer** velger du fakturaen som skal refunderes.



![capture](assets/fr/33.webp)



Klikk på **Refund** og skriv inn Bitcoin-adressen som kunden har oppgitt.



![capture](assets/fr/34.webp)



![capture](assets/fr/35.webp)



### Rapporter og dataeksport



BTCPay Server lar deg **eksportere transaksjonene** (i CSV- eller Excel-format). Dette er veldig praktisk for regnskaps- og kasseoppfølging.



![capture](assets/fr/36.webp)



I menyen **Rapport** klikker du på **Eksporter**: Alle transaksjonene dine lagres i en CSV-fil som du deretter kan se lokalt.



## Sikkerhet og beste praksis



Autonomien som BTCPay Server gir (full suverenitet over midlene dine) er en reell styrke. Men med denne friheten følger også et større ansvar når det gjelder sikkerhet. Ved å administrere dine egne betalinger tar du på deg rollen som din egen bank. Derfor er det viktig å ta i bruk beste praksis for å beskytte midlene, dataene og infrastrukturen din. Her er de viktigste punktene du bør ta hensyn til.



### Sikker tilgang til serveren din





- Bruk et sterkt passord: kombiner store og små bokstaver, tall og spesialtegn. Unngå å gjenbruke et eksisterende passord.
- Aktiver tofaktorautentisering (2FA) for å få tilgang til BTCPay-grensesnittet ditt.
- Oppdater regelmessig operativsystemet, BTCPay Server-forekomsten og avhengighetene dine (Docker, Bitcoin-node, Lightning-node...). Oppdateringer retter ofte sikkerhetshull.



### Håndtering og sikkerhetskopiering av private nøkler





- Lagre private nøkler og seedphrases offline, på fysiske medier (papir eller metall).
- Bruk fortrinnsvis en wallet maskinvare wallet.
- Oppbevar flere kopier av sikkerhetskopiene dine på separate, beskyttede fysiske steder.



### Sikre betalinger og konfidensialitet





- Bruk Tor-nettverket eller et VPN for å skjule serverens IP-adresse og beskytte personvernet ditt.
- Deaktiver unødvendige porter på serveren, og begrens SSH-tilkoblinger til kun betrodde adresser.
- Aktiver HTTPS (SSL-sertifikat) for alle tilkoblinger til ditt BTCPay-nettgrensesnitt.
- Del aldri administrasjonsgrensesnittet med personell som ikke har fått opplæring i Bitcoin-porteføljeforvaltning.



### Implementering av beste praksis for Lightning-nettverket



Butikken din er koblet til en **Lightning-node som ligger på Voltage**, noe som forenkler den tekniske styringen av nettverket betraktelig. Det er likevel viktig å følge **gode overvåkings- og sikkerhetsrutiner**:





- Lagre Voltage-nodens API**-pålogging og tilgangsnøkler (som gjør det mulig for BTCPay å koble seg til).
- Beskytt Voltage-kontoen din** med tofaktorautentisering og et sterkt passord.
- Overvåk node- og kanalstatus** fra Voltage-dashbordet: Dette hjelper deg med å oppdage eventuelle avvik eller desynkronisering.
- Unngå å dele API**-legitimasjonen din eller eksponere den offentlig (f.eks. i nettstedskode).
- Ved migrering er det bare å **konfigurere koblingen mellom BTCPay og Voltage** på nytt: ingen kanal trenger å stenges manuelt.



Med Voltage drar du nytte av en **sikker, svært tilgjengelig** og **automatisk sikkerhetskopiert** infrastruktur, samtidig som du beholder **full suverenitet over Lightning-betalingene dine**.



### Organisere og strukturere interne prosedyrer





- Definer en klar policy for tilgangsstyring: hvem kan opprette en faktura, se betalinger, få tilgang til noden osv.
- Dokumenter rutinene for sikkerhetskopiering og gjenoppretting, slik at du kan reagere raskt i tilfelle en hendelse skulle inntreffe.
- Test regelmessig gjenopprettingen av sikkerhetskopiene for å sikre at de fungerer som de skal.
- Gi de ansatte eller samarbeidspartnerne opplæring i grunnleggende driftssikkerhet: årvåkenhet mot phishing, bruk av sikre passord og respekt for konfidensialitet.



### Overvåke og etablere løpende vedlikehold





- Overvåk serverens aktivitet kontinuerlig ved hjelp av logging eller overvåkingsverktøy.
- Planlegg en periodisk sikkerhetsgjennomgang: sjekk oppdateringer, tilgang, sikkerhetskopier og transaksjonskonsistens.



Vi gratulerer deg! Du har kommet til slutten av denne veiledningen. Du kan nå ta i bruk BTCPay Server på egen hånd, noe som gjør det enklere for deg å administrere butikken din.



Hvis du vil vite mer, anbefaler jeg at du tar vårt komplette opplæringskurs om integrering av Bitcoin i bedriften din:



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a