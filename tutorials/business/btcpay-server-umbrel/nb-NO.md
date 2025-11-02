---
name: BTCPAY SERVER - Paraply
description: Installere og bruke BTCPAY SERVER på Umbrel for å ta imot Bitcoin og Lightning
---

![cover](assets/cover.webp)



I Bitcoin-økosystemet er det en stor utfordring for både selgere og bedrifter å ta imot betalinger. Tradisjonelle løsninger, enten det er bank (kredittkort, Stripe, PayPal) eller til og med Bitcoin (BitPay, Coinbase Commerce), pålegger mellomledd som krever betydelige gebyrer, samler inn sensitive forretningsdata og kan BLOCK eller sensurere transaksjonene dine etter eget forgodtbefinnende. Denne avhengigheten strider mot Bitcoins grunnleggende prinsipper om desentralisering, konfidensialitet og økonomisk suverenitet.



BTCPAY SERVER er i ferd med å bli åpen kildekode-svaret på dette problemet. Denne selvbetjente betalingsprosessoren gjør din egen Bitcoin-node om til en profesjonell infrastruktur, uten mellomledd, uten ekstra behandlingsgebyrer og uten å gå på kompromiss med personvernet. BTCPAY SERVER er utviklet av et globalt fellesskap av bidragsytere siden 2017, og lar deg motta Bitcoin- og Lightning-betalinger direkte i lommebøkene dine, samtidig som du beholder full kontroll over midlene dine til enhver tid.



Tradisjonelt sett krever installasjon av BTCPAY SERVER avanserte tekniske ferdigheter: Linux-serverkonfigurasjon, Docker-ferdigheter, SSL-sertifikatadministrasjon og nettverkssikkerhet. Umbrel revolusjonerer denne tilnærmingen med en ett-klikk-installasjon som er direkte integrert med Bitcoin og LIGHTNING NODE. Denne forenklingen gjør det som tidligere var forbeholdt erfarne teknikere, tilgjengelig for alle.



**Viktig å forstå**: BTCPAY SERVER på Umbrel fungerer som standard kun på ditt lokale nettverk. Du kan opprette fakturaer, godta Lightning- og Bitcoin-betalinger og administrere regnskapet ditt fra en hvilken som helst enhet som er koblet til hjemmenettverket ditt (datamaskin, smarttelefon, nettbrett). Denne konfigurasjonen er ideell for fakturering av personlige tjenester, håndtering av personlige betalinger eller bruk av BTCPAY SERVER fra det lokale nettverket. Hvis du derimot vil integrere BTCPAY SERVER i en nettbutikk som er offentlig tilgjengelig på Internett, kreves det en tilleggskonfigurasjon med offentlig eksponering (vi tar for oss dette problemet på slutten av veiledningen).



Denne veiledningen tar deg gjennom den komplette installasjonen av BTCPAY SERVER på Umbrel, konfigurering av Bitcoin, Wallet og LIGHTNING NODE, oppretting og betaling av fakturaer og håndtering av regnskapsrapportering. Du får vite hvordan du bruker BTCPAY SERVER effektivt i det lokale nettverket ditt, og så snakker vi om løsninger for offentlig visning hvis du ønsker å integrere det med et e-handelsnettsted.



## Forutsetninger



For å følge denne veiledningen må du ha Umbrel riktig installert og konfigurert. Hvis du ikke allerede har gjort det, kan du se vår veiledning om Umbrel-installasjon.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Bitcoin core-noden din må være fullstendig synkronisert med Blockchain (100 % i Umbrels Bitcoin-applikasjon). Denne første synkroniseringen tar vanligvis mellom 3 dager og 2 uker, avhengig av maskinvare og Internett-tilkobling.



For å akseptere lynbetalinger må du også installere LND (Lightning Network Daemon) på Umbrel. Se veiledningen vår om hvordan du installerer og konfigurerer LND på Umbrel hvis du ønsker å aktivere denne funksjonen.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Sørg for minst 50 GB ledig diskplass for BTCPAY SERVER, databasene og Lightning-dataene. En stabil Internett-tilkobling via Ethernet-kabel anbefales på det sterkeste for å unngå frakoblinger.



## Installasjon av BTCPAY SERVER på Umbrel



Fra Umbrel Interface (`umbrel.local`), gå til App Store og søk etter "BTCPAY SERVER" i Bitcoin-kategorien.



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



Klikk på Installer. Umbrel kontrollerer automatisk at Bitcoin core og LND er installert, og starter deretter installasjonen (2-5 minutter).



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



Når du har installert programmet, åpner du det. Du må opprette en administratorkonto med sterk legitimasjon.



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



Når kontoen din er opprettet, vil BTCPAY SERVER umiddelbart be deg om å sette opp din første butikk. Velg et profesjonelt navn og velg en referansevaluta (EUR, USD eller BTC).



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## Få tilgang til BTCPAY SERVER på ditt lokale nettverk



BTCPAY SERVER er tilgjengelig fra alle enheter i ditt lokale nettverk (WiFi eller Ethernet). Tilgang fra nettleseren din til :



```url
http://umbrel.local
```



Eller direkte til :



```url
http://umbrel.local:3003
```



**Fjerntilgang med Tailscale**: Bruk Tailscale for å få tilgang til BTCPAY SERVER fra hvor som helst i verden. Dette sikre VPN-et lar deg koble deg til Umbrel som om du var på ditt lokale nettverk. Se vår veiledning dedikert til Tailscale på Umbrel.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Konfigurere Bitcoin-porteføljen din



For å akseptere betalinger må du konfigurere en Bitcoin Wallet. BTCPAY SERVER viser konfigurasjonsalternativene i dashbordet.



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



For å konfigurere Wallet Bitcoin, gå til "Wallets" > "Bitcoin".



Du har to alternativer: opprette en ny portefølje direkte i BTCPay, eller importere en eksisterende portefølje. Det finnes flere metoder for import:




- Koble til Hardware Wallet** (anbefalt): Importer de offentlige nøklene dine via Vault-applikasjonen
- Importer Wallet-fil** (anbefalt): Last opp en eksportert fil fra porteføljen din
- Skriv inn utvidet offentlig nøkkel**: Skriv inn XPub/YPub/ZPub manuelt
- Skann Wallet QR-kode** : Skann en QR-kode fra BlueWallet, Cobo Vault, Passport eller Spectre DIY
- Skriv inn Wallet seed** (ikke anbefalt) : Skriv inn gjenopprettingsfrasen på 12 eller 24 ord



![Options de création de portefeuille](assets/fr/06.webp)



I denne veiledningen skal vi opprette en ny Hot Wallet: Den private nøkkelen vil derfor bli lagret på Umbrel-serveren vår. I dette tilfellet anbefaler vi deg på det sterkeste å flytte midlene regelmessig til en Cold Wallet for å unngå å lagre store beløp på serveren.



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



Når BTCPAY SERVER er konfigurert, bekrefter BTCPAY SERVER at Wallet er klar til å ta imot On-Chain-betalinger.



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## Aktiver Lightning Network



For å akseptere øyeblikkelige Lightning-betalinger går du til Wallets > Lightning. Ettersom LND-noden din allerede er på plass på Umbrel, klikker du bare på "Lagre"-knappen for å validere forbindelsen mellom BTCPAY SERVER og LIGHTNING NODE.



![Configuration du nœud Lightning](assets/fr/09.webp)



## Opprett og betal fakturaer



I Interface BTCPAY SERVER navigerer du til Fakturaer > Opprett Invoice. Angi beløpet, legg til en valgfri beskrivelse, og klikk på Opprett.



![Création d'une nouvelle facture](assets/fr/10.webp)



Du kan deretter klikke på "Checkout"-knappen for å vise Invoice. BTCPay genererer deretter en Invoice med en enhetlig QR-kode (BIP21) som inneholder Bitcoin Address og Lightning Invoice.



![Détails de la facture générée](assets/fr/11.webp)



Kunden din kan skanne QR-koden med en hvilken som helst kompatibel Wallet.



![Page de paiement avec QR code](assets/fr/12.webp)



Når den er betalt, blir Invoice "avregnet" i løpet av noen sekunder for Lightning.



![Confirmation de paiement réussi](assets/fr/13.webp)



## Håndtering og sporing av betalinger



I "Rapportering"-delen, fanen "Fakturaer", finner du en komplett historikk over fakturaene dine, med dato, beløp, status og betalingsmåte. Du kan eksportere den ved behov.



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## Lagre konfigurasjon



BTCPAY SERVER lar deg administrere flere butikker med forskjellige parametere. Hver butikk representerer en separat forretningsenhet: e-handelsbutikk, fysisk utsalgssted eller servicefakturering.



I butikkinnstillingene finner du flere viktige seksjoner:



![Paramètres du magasin](assets/fr/15.webp)





- Generelle innstillinger**: Butikknavn, referansevaluta (BTC, EUR, USD), utløpstid for Invoice (standard 15 minutter), antall Blockchain-bekreftelser som kreves
- Priser**: Konfigurasjon av Exchange-kurser og fiat/Bitcoin-konvertering
- Utseende i kassen**: Tilpass utseendet på kassesidene dine (logo, farger, personlige meldinger)
- E-postinnstillinger**: Konfigurasjon av e-postvarsler for mottatte betalinger
- Tilgangstokener**: API token-administrasjon for e-handelsintegrasjoner (WooCommerce, Shopify osv.)
- Brukere**: Administrer brukertilgang til butikken med ulike nivåer av tillatelser (eier, gjest)
- Webhooks**: Webhook-konfigurasjon for sanntidssynkronisering med regnskaps- eller ERP-systemet ditt



BTCPAY SERVER tilbyr også en Plugins-seksjon for å utvide funksjonaliteten med e-handelsintegrasjoner, kassasystemer og andre verktøy.



![Gestion des plugins](assets/fr/16.webp)



## Fordeler og begrensninger ved lokal bruk



**Fordelene med BTCPAY SERVER på Umbrel** :




- Total suverenitet: eksklusiv kontroll over private nøkler og midler, ingen tredjepart kan fryse eller sensurere betalingene dine
- Betydelige besparelser: kun Bitcoin nettverkskostnader (noen få cent på Lightning) mot 2-3 % på tradisjonelle prosessorer
- Maksimal konfidensialitet: ingen registrering, identitetsbekreftelse eller deling av data med tredjepartsselskaper
- Åpen kildekode-arkitektur garanterer åpenhet, etterprøvbarhet og bærekraft via et stort fellesskap av utviklere
- Enkel installasjon via Umbrel, uten behov for avanserte tekniske ferdigheter



**Viktige begrensninger** :




- Kun lokalt nettverk**: BTCPAY SERVER på Umbrel er kun tilgjengelig fra hjemmenettverket ditt. Perfekt for personlig fakturering, frilanstjenester eller små fysiske bedrifter, men uegnet for nettbutikker som er offentlig tilgjengelige på Internett.
- Fullt teknisk ansvar: vedlikehold av noder, regelmessig sikkerhetskopiering, overvåking av tilkoblinger
- Styring av lynlikviditet: åpne og administrere kanaler med tilstrekkelig inngående kapasitet
- Supporten er begrenset til felles dokumentasjon og fora, noe som krever mer selvstendighet enn en kommersiell kundeserviceavdeling



Denne LAN-begrensningen er det største hinderet for å integrere BTCPAY SERVER i en e-handelsbutikk, der kundene må kunne få tilgang til betalingssidene fra hvor som helst på Internett.



## Beste praksis og sikkerhet



Aktiver automatisk Umbrel-sikkerhetskopiering og lagre en kopi på et eksternt medium (USB-pinne, Hard-disk, kryptert nettsky). Oppbevar Bitcoin-frøene (gjenopprettingsfraser) på et trygt, fysisk adskilt sted. Lagre LND channel.backup-filen for lyngjenoppretting.



Overvåk jevnlig Bitcoin core-synkronisering, Lightning-kanaler og BTCPAY SERVER-respons. En enkel ukentlig test: generate og betal en regning på noen få satoshier. Hold Umbrel oppdatert (sikkerhetsoppdateringer, forbedringer). Ta en sikkerhetskopi før større oppdateringer. For profesjonell bruk, vurder ekstern overvåking (UptimeRobot) med e-post/SMS-varsler.



## Vis BTCPAY SERVER offentlig for en nettbutikk



For å integrere BTCPAY SERVER i en nettbasert e-handelsbutikk (WooCommerce, Shopify osv.) må kundene dine kunne få tilgang til betalingssidene fra hvor som helst, ikke bare fra det lokale nettverket.



**Løsning: Nginx Proxy Manager**



Du kan eksponere BTCPAY SERVER offentlig ved hjelp av Nginx Proxy Manager (tilgjengelig i Umbrel App Store). Denne løsningen krever :




- Et domenenavn (klassisk eller gratis via DuckDNS, No-IP, Afraid.org)
- Konfigurere portvideresending (port 80 og 443) på ruteren din
- Installasjon av Nginx Proxy Manager, som automatisk håndterer SSL-sertifikater



Denne konfigurasjonen eksponerer serveren din mot Internett og krever ekstra årvåkenhet (sterke passord, 2FA, regelmessige oppdateringer). Vi kommer til å utarbeide en egen veiledning som beskriver hele denne prosedyren.



## Konklusjon



BTCPAY SERVER på Umbrel kombinerer kraften til Bitcoin-noden med enkelheten til Umbrel for å skape en selvbetjent profesjonell betalingsinfrastruktur som er tilgjengelig for alle. Denne økonomiske suvereniteten kommer med et vedlikeholdsansvar, men Umbrel forenkler driftsbyrden i stor grad sammenlignet med fordelene: eliminering av behandlingsgebyrer, beskyttelse av personvernet ditt, motstand mot sensur og total kontroll over midlene dine.



Bruk av lokale nettverk dekker allerede et bredt spekter av bruksområder: fakturering av frilanstjenester, betalinger ansikt til ansikt, små fysiske butikker, eller rett og slett læring og eksperimentering med Bitcoin og Lightning i et kontrollert miljø. For e-handelsbehov som krever offentlig eksponering, finnes Nginx Proxy Manager-løsningen, men den krever ytterligere teknisk konfigurasjon, som vi vil beskrive i en egen veiledning.



Enten du driver en bedrift, et nystartet prosjekt eller bare eksperimenterer, tilbyr BTCPAY SERVER på Umbrel fullstendig økonomisk autonomi. Veien begynner med en første butikk, en første Invoice, en første betaling som mottas direkte inn i din suverene infrastruktur.



## Ressurser



### Offisiell dokumentasjon




- [BTCPAY SERVER offisielle nettside](https://btcpayserver.org)
- [Komplett BTCPAY SERVER-dokumentasjon] (https://docs.btcpayserver.org)
- [GitHub BTCPAY SERVER](https://github.com/btcpayserver/btcpayserver)
- [Tailscale-dokumentasjon] (https://tailscale.com/kb)


### Fellesskap og støtte




- [Forum BTCPAY SERVER](https://chat.btcpayserver.org)
- [Forum Umbrel](https://community.getumbrel.com)
- [Reddit r/BTCPayServer] (https://reddit.com/r/BTCPayServer)