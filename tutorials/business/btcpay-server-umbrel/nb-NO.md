---
name: BTCPay Server - Umbrel
description: Installere og bruke BTCPay Server på Umbrel for å akseptere Bitcoin og Lightning
---

![cover](assets/cover.webp)



I Bitcoin-økosystemet er det en stor utfordring for både selgere og bedrifter å ta imot betalinger. Tradisjonelle løsninger, enten det er banktjenester (kredittkort, Stripe, PayPal) eller til og med Bitcoin (BitPay, Coinbase Commerce), pålegger mellomledd som krever betydelige gebyrer, samler inn sensitive forretningsdata og kan blokkere eller sensurere transaksjonene dine etter eget forgodtbefinnende. Denne avhengigheten strider mot Bitcoins grunnleggende prinsipper om desentralisering, konfidensialitet og økonomisk suverenitet.



BTCPay Server er i ferd med å bli åpen kildekode-svaret på dette problemet. Denne selvhostede betalingsprosessoren gjør din egen Bitcoin-node til en profesjonell infrastruktur, uten mellommann, uten ekstra behandlingsgebyrer og uten kompromiss med personvernet. BTCPay Server er utviklet av et globalt fellesskap av bidragsytere siden 2017, og lar deg motta Bitcoin- og Lightning-betalinger direkte i lommebøkene dine, samtidig som du beholder full kontroll over midlene dine til enhver tid.



Tradisjonelt sett krever installasjon av BTCPay Server avanserte tekniske ferdigheter: Linux-serverkonfigurasjon, beherskelse av Docker, SSL-sertifikatadministrasjon og nettverkssikkerhet. Umbrel revolusjonerer denne tilnærmingen med en ett-klikk-installasjon som er direkte integrert med Bitcoin og Lightning-noden. Denne forenklingen gjør det som tidligere var forbeholdt erfarne teknikere, tilgjengelig for alle.



**Viktig å forstå**: BTCPay Server på Umbrel fungerer som standard kun på ditt lokale nettverk. Du kan opprette fakturaer, godta Lightning- og Bitcoin-betalinger og administrere regnskapet ditt fra hvilken som helst enhet som er koblet til hjemmenettverket ditt (datamaskin, smarttelefon, nettbrett). Denne konfigurasjonen er ideell for fakturering av personlige tjenester, administrering av betalinger ansikt til ansikt eller bruk av BTCPay Server fra ditt lokale nettverk. Hvis du derimot vil integrere BTCPay Server i en nettbutikk som er offentlig tilgjengelig på Internett, kreves det en tilleggskonfigurasjon med offentlig eksponering (vi tar for oss dette på slutten av veiledningen).



Denne veiledningen tar deg gjennom den komplette installasjonen av BTCPay Server på Umbrel, konfigurering av Bitcoin wallet og Lightning-noden, oppretting og betaling av fakturaer og håndtering av regnskapsrapportering. Du lærer hvordan du bruker BTCPay Server effektivt på ditt lokale nettverk, og deretter ser vi på løsninger for offentlig visning hvis du ønsker å integrere den med et e-handelsnettsted.



## Forutsetninger



For å følge denne veiledningen må du ha Umbrel riktig installert og konfigurert. Hvis du ikke allerede har gjort det, kan du se vår veiledning om Umbrel-installasjon.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Din Bitcoin Core-node må være fullstendig synkronisert med blokkjeden (100 % i Umbrels Bitcoin-applikasjon). Denne første synkroniseringen tar vanligvis mellom 3 dager og 2 uker, avhengig av maskinvaren og internettforbindelsen din.



For å akseptere lynbetalinger må du også installere LND (Lightning Network Daemon) på Umbrel. Se veiledningen vår om hvordan du installerer og konfigurerer LND på Umbrel hvis du ønsker å aktivere denne funksjonen.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Sørg for minst 50 GB ledig diskplass for BTCPay Server, databasene og Lightning-data. En stabil Internett-tilkobling via Ethernet-kabel anbefales på det sterkeste for å unngå frakoblinger.



## Installere BTCPay Server på Umbrel



Fra Umbrel-grensesnittet (`umbrel.local`), gå til App Store og søk etter "BTCPay Server" i Bitcoin-kategorien.



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



Klikk på Installer. Umbrel kontrollerer automatisk at Bitcoin Core og LND er installert, og starter deretter installasjonen (2-5 minutter).



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



Når du har installert programmet, åpner du det. Du må opprette en administratorkonto med sterk legitimasjon.



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



Når kontoen din er opprettet, vil BTCPay Server umiddelbart be deg om å sette opp din første butikk. Velg et firmanavn og velg en referansevaluta (EUR, USD eller BTC).



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## Få tilgang til BTCPay Server på ditt lokale nettverk



BTCPay Server er tilgjengelig fra alle enheter i ditt lokale nettverk (WiFi eller Ethernet). Tilgang fra nettleseren din til :



```url
http://umbrel.local
```



Eller direkte til :



```url
http://umbrel.local:3003
```



**Fjerntilgang med Tailscale**: For å få tilgang til BTCPay Server fra hvor som helst i verden, bruk Tailscale. Dette sikre VPN-et lar deg koble deg til Umbrel som om du var på ditt lokale nettverk. Se vår veiledning dedikert til Tailscale på Umbrel.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Konfigurere Bitcoin-porteføljen din



For å akseptere betalinger må du konfigurere en Bitcoin wallet. BTCPay Server viser konfigurasjonsalternativer i dashbordet.



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



For å konfigurere wallet Bitcoin, gå til "Wallets" > "Bitcoin".



Du har to alternativer: opprette en ny portefølje direkte i BTCPay, eller importere en eksisterende portefølje. Det finnes flere metoder for import:




- Koble til maskinvare wallet** (anbefalt): Importer de offentlige nøklene dine via Vault-applikasjonen
- Importer wallet-fil** (anbefalt): Last opp en eksportert fil fra porteføljen din
- Skriv inn utvidet offentlig nøkkel**: Skriv inn XPub/YPub/ZPub manuelt
- Skann wallet QR-kode** : Skann en QR-kode fra BlueWallet, Cobo Vault, Passport eller Spectre DIY
- Skriv inn wallet seed** (ikke anbefalt) : Skriv inn gjenopprettingsfrasen på 12 eller 24 ord



![Options de création de portefeuille](assets/fr/06.webp)



I denne veiledningen skal vi opprette en ny Hot wallet: Den private nøkkelen vil derfor bli lagret på Umbrel-serveren vår. I dette tilfellet anbefaler vi deg på det sterkeste å flytte midlene regelmessig til en kald wallet for å unngå å lagre store beløp på serveren.



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



Når den er konfigurert, bekrefter BTCPay Server at din wallet er klar til å ta imot on-chain-betalinger.



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## Aktiver Lightning Network



For å akseptere øyeblikkelige Lightning-betalinger går du til Wallets > Lightning. Ettersom LND-noden din allerede er på plass på Umbrel, klikker du bare på "Lagre"-knappen for å validere forbindelsen mellom BTCPay-serveren og Lightning-noden din.



![Configuration du nœud Lightning](assets/fr/09.webp)



## Opprett og betal fakturaer



I BTCPay Server-grensesnittet navigerer du til Fakturaer > Opprett Invoice. Angi beløpet, legg til en valgfri beskrivelse, og klikk på Opprett.



![Création d'une nouvelle facture](assets/fr/10.webp)



Deretter kan du klikke på "Checkout"-knappen for å vise fakturaen. BTCPay genererer deretter en faktura med en enhetlig QR-kode (BIP21) som inneholder Bitcoin-adressen og lynfakturaen.



![Détails de la facture générée](assets/fr/11.webp)



Kunden din kan skanne QR-koden med hvilken som helst kompatibel wallet.



![Page de paiement avec QR code](assets/fr/12.webp)



Når fakturaen er betalt, blir den "oppgjort" i løpet av noen sekunder for Lightning.



![Confirmation de paiement réussi](assets/fr/13.webp)



## Håndtering og sporing av betalinger



I "Rapportering"-delen, fanen "Fakturaer", finner du en komplett historikk over fakturaene dine med dato, beløp, status og betalingsmåte. Du kan eksportere den ved behov.



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## Lagre konfigurasjon



BTCPay Server lar deg administrere flere butikker med forskjellige parametere. Hver butikk representerer en separat forretningsenhet: e-handelsbutikk, fysisk utsalgssted eller tjenestefakturering.



I butikkinnstillingene finner du flere viktige seksjoner:



![Paramètres du magasin](assets/fr/15.webp)





- Generelle innstillinger**: Butikknavn, referansevaluta (BTC, EUR, USD), fakturaens utløpstid (standard 15 minutter), antall blockchain-bekreftelser som kreves
- Priser**: Konfigurasjon av valutakurser og fiat/Bitcoin-konvertering
- Utseende i kassen**: Tilpass utseendet på kassesidene dine (logo, farger, personlige meldinger)
- E-postinnstillinger**: Konfigurasjon av e-postvarsler for mottatte betalinger
- Tilgangstokener**: Administrasjon av API-tokens for e-handelsintegrasjoner (WooCommerce, Shopify osv.)
- Brukere**: Administrer brukertilgang til butikken med ulike nivåer av tillatelser (eier, gjest)
- Webhooks**: Webhook-konfigurasjon for sanntidssynkronisering med regnskaps- eller ERP-systemet ditt



BTCPay Server tilbyr også en Plugins-seksjon for å utvide funksjonaliteten med e-handelsintegrasjoner, kassasystemer og tilleggsverktøy.



![Gestion des plugins](assets/fr/16.webp)



## Fordeler og begrensninger ved lokal bruk



**Fordeler med BTCPay Server fremfor Umbrel** :




- Total suverenitet: eksklusiv kontroll over private nøkler og midler, ingen tredjepart kan fryse eller sensurere betalingene dine
- Betydelige besparelser: bare Bitcoin nettverkskostnader (noen få cent på Lightning) mot 2-3 % på tradisjonelle prosessorer
- Maksimal konfidensialitet: ingen registrering, identitetsbekreftelse eller deling av data med tredjepartsselskaper
- Åpen kildekode-arkitektur garanterer åpenhet, etterprøvbarhet og bærekraft via et stort fellesskap av utviklere
- Enkel installasjon via Umbrel, uten behov for avanserte tekniske ferdigheter



**Viktige begrensninger** :




- Kun lokalt nettverk**: BTCPay Server på Umbrel er bare tilgjengelig fra hjemmenettverket ditt. Perfekt for personlig fakturering, frilanstjenester eller små fysiske bedrifter, men uegnet for offentlig tilgjengelige nettbutikker.
- Fullt teknisk ansvar: vedlikehold av noder, regelmessig sikkerhetskopiering, overvåking av tilkoblinger
- Styring av lynlikviditet: åpne og administrere kanaler med tilstrekkelig inngående kapasitet
- Supporten er begrenset til felles dokumentasjon og fora, noe som krever mer selvstendighet enn en kommersiell kundeserviceavdeling



Denne lokale nettverksbegrensningen er det største hinderet for å integrere BTCPay Server i en e-handelsbutikk, der kundene må kunne få tilgang til betalingssidene fra hvor som helst på Internett.



## Beste praksis og sikkerhet



Aktiver automatisk Umbrel-sikkerhetskopiering og lagre en kopi på et eksternt medium (USB-pinne, harddisk, kryptert nettsky). Oppbevar Bitcoin-frøene (gjenopprettingsfraser) på et trygt, fysisk adskilt sted. Ta sikkerhetskopi av LND's channel.backup-fil for lyngjenoppretting.



Overvåk regelmessig Bitcoin Core-synkronisering, Lightning-kanaler og BTCPay Server-respons. En enkel ukentlig test: generate og betal en regning på noen få satoshier. Hold Umbrel oppdatert (sikkerhetsoppdateringer, forbedringer). Ta en sikkerhetskopi før større oppdateringer. For profesjonell bruk bør du vurdere ekstern overvåking (UptimeRobot) med e-post/SMS-varsler.



## Eksponere BTCPay Server offentlig for en nettbutikk



For å integrere BTCPay Server i en nettbasert e-handelsbutikk (WooCommerce, Shopify osv.) må kundene dine kunne få tilgang til betalingssidene fra hvor som helst, ikke bare fra ditt lokale nettverk.



**Løsning: Nginx Proxy Manager**



Du kan eksponere BTCPay Server offentlig ved hjelp av Nginx Proxy Manager (tilgjengelig i Umbrel App Store). Denne løsningen krever :




- Et domenenavn (klassisk eller gratis via DuckDNS, No-IP, Afraid.org)
- Konfigurere portvideresending (port 80 og 443) på ruteren din
- Installasjon av Nginx Proxy Manager, som automatisk håndterer SSL-sertifikater



Denne konfigurasjonen eksponerer serveren din mot Internett og krever ekstra årvåkenhet (sterke passord, 2FA, regelmessige oppdateringer). Vi kommer til å utarbeide en egen veiledning som beskriver hele denne prosedyren.



## Konklusjon



BTCPay Server on Umbrel kombinerer kraften til Bitcoin-noden med enkelheten til Umbrel for å skape en selvbetjent profesjonell betalingsinfrastruktur som er tilgjengelig for alle. Denne økonomiske suvereniteten kommer med et vedlikeholdsansvar, men Umbrel forenkler driftsbyrden i stor grad sammenlignet med fordelene: eliminering av behandlingsgebyrer, beskyttelse av personvernet ditt, motstand mot sensur og total kontroll over midlene dine.



Bruk av lokale nettverk dekker allerede et bredt spekter av bruksområder: fakturering av frilanstjenester, personlige betalinger, små fysiske butikker, eller rett og slett læring og eksperimentering med Bitcoin og Lightning i et kontrollert miljø. For e-handelsbehov som krever offentlig eksponering, finnes Nginx Proxy Manager-løsningen, men den krever ytterligere teknisk konfigurasjon, som vi vil beskrive i en egen veiledning.



Enten du driver en bedrift, et nystartet prosjekt eller bare eksperimenterer, tilbyr BTCPay Server på Umbrel fullstendig økonomisk autonomi. Veien begynner med din første butikk, din første faktura, din første betaling som mottas direkte inn i din suverene infrastruktur.



## Ressurser



### Offisiell dokumentasjon




- [Offisielt nettsted for BTCPay Server](https://btcpayserver.org)
- [Komplett BTCPay Server-dokumentasjon] (https://docs.btcpayserver.org)
- [GitHub BTCPay Server] (https://github.com/btcpayserver/btcpayserver)
- [Tailscale-dokumentasjon] (https://tailscale.com/kb)


### Fellesskap og støtte




- [Forum BTCPay Server] (https://chat.btcpayserver.org)
- [Forum Umbrel](https://community.getumbrel.com)
- [Reddit r/BTCPayServer] (https://reddit.com/r/BTCPayServer)