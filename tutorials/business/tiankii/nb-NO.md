---
name: Tiankii
description: Lynpakke med verktøy for forhandlere og forbrukere
---

![cover](assets/cover.webp)



I Bitcoin-økosystemet er det fortsatt en stor utfordring for bedrifter og privatpersoner å ta imot betalinger i sanntid. Tradisjonelle løsninger krever ofte avansert teknisk kunnskap, en kompleks infrastruktur å vedlikeholde eller at midlene oppbevares av mellommenn. Denne situasjonen hindrer at Bitcoin blir tatt i bruk som en hverdagsvaluta, til tross for de lovende teknologiske fremskrittene med Lightning Network.



Tiankii, et salvadoransk selskap grunnlagt i 2021, svarer på dette problemet ved å tilby en tilgjengelig, modulær Bitcoin-infrastruktur. I stedet for å tvinge frem et lukket økosystem, tilbyr Tiankii en pakke med sammenkoblede verktøy som gjør det mulig for alle å integrere Bitcoin Lightning i virksomheten sin uten å ofre kontrollen over midlene sine.



## Hva er Tiankii?



### Opprinnelse og filosofi



Tiankii - et nahuatl-begrep som betyr "friluftsmarked som er tilgjengelig for alle" - er El Salvadors første 100 % Bitcoin-oppstartsbedrift. Selskapet ble grunnlagt av Darvin Otero etter at Bitcoin ble vedtatt som landets lovlige betalingsmiddel, og har som mål å forvandle Bitcoin fra et verdioppbevaringsmiddel til en transaksjonsvaluta for hverdagslige kjøp. I motsetning til depotplattformer har Tiankii en ikke-depotbasert tilnærming, der brukerne beholder kontrollen over midlene sine, og infrastrukturen kun fungerer som et teknisk mellomledd.



### Teknisk arkitektur



Tiankii er posisjonert som en leverandør av Bitcoin-as-a-Service-infrastruktur basert på Lightning Network. Denne andrelagsteknologien muliggjør nesten øyeblikkelige transaksjoner med ubetydelige kostnader, noe som muliggjør mikrobetalinger og dagligdagse kjøp.



Arkitekturen er basert på tre pilarer:



**Lightning først**: Systematisk favorisering av Lightning-nettverket på grunn av hastighet og lavere kostnader, samtidig som vi beholder støtten for on-chain-transaksjoner for store beløp.



**Åpne standarder**: Bruk av LNURL for å automatisere betalingsforespørsler, Lightning Address for lesbare e-post-ID-er og Bolt Card for interoperable NFC-betalinger.



**wallet-agnostisk modularitet**: Mulighet for å koble til ulike Lightning-porteføljer (LNbits, Blink, BlueWallet) eller din egen node, noe som gir maksimal fleksibilitet avhengig av hvilket nivå av ekspertise og autonomi som kreves.



## Tiankiis økosystemverktøy



### Bitcoin POS - betalingsterminal i butikk



Applikasjonen gjør smarttelefonen eller nettbrettet om til en Lightning-terminal. Forhandleren taster inn beløpet i lokal valuta, og appen genererer en Lightning QR-kode eller aksepterer et Bolt-kort. Transaksjoner krediteres umiddelbart uten provisjon, med automatisk konvertering i over 150 valutaer, tipshåndtering og salgshistorikk.



### Merchant Dashboard - enhetlig salgsstyring



Interface websentralisert for å koble til wallet Lightning, spore transaksjoner i sanntid, utstede fakturaer og generate regnskapsrapporter. Plattformen samler alle kanaler: betalinger i butikk (POS), nettsalg (plug-ins for e-handel) eller API-integrasjoner. Betalinger samles på den valgte wallet.



### Bitcoin Kontaktløst kort (Bolt-kort)



NFC Bolt-kortet representerer Tiankiis viktigste innovasjon for å demokratisere Bitcoin for allmennheten. Det fungerer som et kontaktløst bankkort, og lar deg betale for Bitcoin Lightning-kjøp ved å trykke på en kompatibel terminal.



I motsetning til tradisjonelle depotløsninger følger dette kortet en åpen standard som garanterer interoperabilitet. Brukerne kan koble kortet til sin egen wallet via IBI-applikasjonen, og beholder dermed sine private nøkler og full kontroll over de tilknyttede midlene. Betalingen tar bare et sekund, og det er ikke nødvendig å ta frem smarttelefonen eller ha en aktiv internettforbindelse på betalingstidspunktet.



Denne løsningen er spesielt inkluderende for folk som ikke er kjent med smarttelefoner, og tilbyr en tilgjengelig inngangsport til Bitcoin-økonomien.



### IBI App - Interface individuell Bitcoin



IBI-applikasjonen (Individual Bitcoin Interface) er utviklet for enkeltpersoner som ønsker å bruke Bitcoin Lightning på daglig basis. Hovedfordelen ligger i genereringen av en personlig Address Lightning, en betalingsidentifikator som kan leses i e-postformat (eksempel: alice@ibi.me).



Denne identifikatoren forenkler mottak av betalinger drastisk: Du trenger ikke å generate en ny faktura for hver transaksjon, avsenderen kan ganske enkelt skrive inn Lightning-adressen. Grensesnittet lar deg også administrere Bolt-kortet ditt (aktivering, deaktivering, forbruksgrenser), koble til ulike Lightning-lommebøker og foreta betalinger ved å skanne QR-koder.



### Plugins for e-handel



Klar til bruk-integrasjoner for WooCommerce, Shopify og Cloudbeds. Installeres på få minutter for å legge til Bitcoin Lightning i kassen. Fordeler: null provisjon (mot 2-3 % for kredittkort), øyeblikkelig oppgjør, tilgang over hele verden, eliminering av tilbakeføringer. Betalinger ankommer direkte på selgerens tilkoblede wallet.



### Bitcoin API og utviklerverktøy



Tiankiis SDK gjør det mulig å integrere Bitcoin Lightning i eksisterende applikasjoner uten å vedlikeholde en egen node. API håndterer oppretting av fakturaer, betalingsbekreftelse og masseutsendelser via en robust infrastruktur i Google Cloud. Command Center kompletterer tilbudet for organisasjoner med Address Lightning på egendefinerte domener, massebetalinger og sentralisert administrasjon av NFC-terminaler og -kort.



## Installasjon og de første trinnene



### Viktige forutsetninger



Tiankii krever ingen kompliserte tekniske forutsetninger. Applikasjonene fungerer via en nettleser på en smarttelefon, et nettbrett eller en datamaskin. Det kreves ingen installasjon av en egen applikasjon: alt du trenger er internettilgang og en nyere nettleser for å få tilgang til IBI eller Merchant Dashboard.



**For private brukere (IBI-appen)**: Ingen tidligere wallet Lightning er påkrevd. Når du oppretter kontoen din, konfigurerer Tiankii automatisk en fungerende Address Lightning via [Breez SDK Liquid](https://sdk-doc-liquid.breez.technology/guide/about_breez_sdk_liquid.html), en nodeless-implementering som bruker Liquid-nettverket i bakgrunnen. Du kan umiddelbart motta og sende betalinger uten noen teknisk konfigurasjon. Denne løsningen forenkler tilgangen for nybegynnere drastisk, samtidig som den er selvforvaltende.



**For forhandlere (Merchant Dashboard)** : Tilkobling av en eksisterende wallet Lightning er obligatorisk for å kunne bruke Point of Sale-terminaler og motta betalinger. Tiankii støtter mange løsninger: mobile lommebøker (Blink, Strike), selv-hostede løsninger (LNbits, LND/CLN node) eller nettlommebøker (Alby). Detaljerte tilkoblingsveiledninger er tilgjengelige i delen Ressurser i denne opplæringen.



### For privatkunder: IBI App



**Opprettelse av konto



Gå til accounts.ibi.me for å opprette kontoen din. På denne siden kan du velge mellom to kontotyper: "Personal Use" for privat bruk, eller "Business Use" for kommersiell bruk. Velg "Personal Use" for å få tilgang til verktøyene for å motta og sende betalinger i Bitcoin.



![Choix du type de compte](assets/fr/01.webp)



Når du har valgt "Personlig bruk", blir du automatisk omdirigert til go.ibi.me for å fullføre registreringen. Dette kan gjøres via e-post, telefonnummer eller ved hjelp av Google-, Microsoft- eller Twitter-kontoen din. Når du er opprettet, kan du umiddelbart få tilgang til IBI-grensesnittet ditt, med Lightning Address allerede i drift.



![Création du compte](assets/fr/02.webp)



**Interface main**



IBI-grensesnittet viser saldoen din i satoshier og lokal valuta (USD). Tre knapper gir deg mulighet til å samhandle: "Receive" for å motta betalinger, "Scan" for å skanne en QR-kode og "Send" for å sende satoshier.



![Interface IBI](assets/fr/03.webp)



**Motta betaling**



For å motta satoshier trykker du på "Receive". Programmet genererer automatisk en QR-kode og viser din personlige Address Lightning (nom@ibi.me-format). Del denne adressen eller QR-koden med avsenderen: pengene kommer umiddelbart inn på IBI-kontoen din.



![Réception avec Lightning Address](assets/fr/04.webp)



Når saldoen din er kreditert, kan du bruke disse satoshiene til å foreta betalinger.



**Send en betaling**



Trykk på "Send" for å sende satoshier. Du kan enten skanne en Lightning QR-kode eller angi en Lightning Address-destinasjon direkte.



![Solde et boutons IBI](assets/fr/05.webp)



![Interface d'envoi](assets/fr/06.webp)



Angi ønsket beløp i satoshier, sjekk det tilsvarende beløpet i lokal valuta, og bekreft deretter betalingen.



![Confirmation du montant](assets/fr/07.webp)



En melding bekrefter forsendelsen med detaljer: sendt beløp, transaksjonsgebyr og mottaker.



![Paiement réussi](assets/fr/08.webp)



**Kontoadministrasjon



I Innstillinger kan du administrere Bitcoin NFC-kortene dine (Bolt-kort). Grensesnittet lar deg aktivere, deaktivere eller sette utgiftsgrenser for kortene dine.



![Historique des transactions](assets/fr/09.webp)



![Paramètres IBI](assets/fr/10.webp)



### For selgere: Merchant Dashboard og POS



**Opprettelse av bedriftskonto



Gå til accounts.ibi.me for å opprette kontoen din. Velg "Business Use" for å få tilgang til forhandlerverktøy. Denne kontotypen gir tilgang til Merchant Dashboard og POS-terminaler.



Når du har valgt "Business Use", blir du automatisk videresendt til Merchant Dashboard (pay.tiankii.com). Dette tar deg til grensesnittet for forretningsadministrasjon med inntektssporing, transaksjoner og betalingsverktøy. For å begynne å ta imot betalinger må du først koble til wallet Lightning ved å klikke på lenken øverst på siden (se pilen på bildet).



![Dashboard marchand](assets/fr/11.webp)



**wallet Lightning**-tilkobling



Avgjørende trinn i aktiveringen av utsalgsstedet ditt: koble til wallet Lightning for å motta betalinger. Grensesnittet tilbyr flere tilkoblingsalternativer. Vær oppmerksom på at noen alternativer (Bitcoin Onchain og Lightning Network) fortsatt er under utvikling og vises nedtonet i grensesnittet.



![Options de connexion wallet](assets/fr/12.webp)



I denne veiledningen bruker vi Lightning Address-tilkoblingen, som er kompatibel med Chivo, Blink Wallet og Strike. Skriv inn din Lightning Address (nom@domaine.com-format), for eksempel fra LN Markets, Alby eller en annen kompatibel leverandør.



![Saisie de la Lightning Address](assets/fr/13.webp)



Når du har logget inn, er kontoen din i drift. Du kan nå gå til POS eller gå tilbake til dashbordet for å konfigurere andre innstillinger.



![Connexion réussie](assets/fr/14.webp)



*betalingslenker** *Betalingslenker



Menyen "Betalingsverktøy" gir tilgang til "Betalingsforespørsel", der du kan opprette og administrere betalingslenker. Denne funksjonen er nyttig for å generere personlige betalingslenker som kan sendes via e-post eller melding: donasjoner, enkeltbetalinger, flere betalinger eller til og med betalingsmurer for å beskytte innhold. Du kan opprette ulike typer lenker for å tilpasse dem til bedriftens behov.



![Liens de paiement](assets/fr/15.webp)



**Konfigurasjon av salgsterminalen**



For å akseptere betalinger i butikk, åpner du menyen "Salgsterminal" fra "Betalingsverktøy". Her kan du opprette og administrere POS-terminaler (antall terminaler avhenger av abonnementet ditt, se Freemium vs. Business-abonnementer nedenfor). Klikk på "Åpne" for å åpne POS-grensesnittet i nettleseren din.



![Gestion des terminaux](assets/fr/16.webp)




**Generere et salg**



POS-terminalen viser et numerisk tastatur for inntasting av salgsbeløpet. Skriv inn beløpet i din lokale valuta (f.eks. 500 sats tilsvarer 630,74 ARS), og trykk deretter på "OK" for å bekrefte.



![Saisie du montant](assets/fr/17.webp)



Applikasjonen genererer umiddelbart en Lightning QR-kode og en Lightning Address for betaling. Kundene kan skanne QR-koden med wallet eller bruke Bolt-kortet på en NFC-terminal.



![QR code de paiement](assets/fr/18.webp)



Så snart betalingen er mottatt, vises en bekreftelse på skjermen som viser det mottatte beløpet i lokal valuta og satoshier. Du kan sende en kvittering via e-post, skrive ut billetten eller starte et nytt salg umiddelbart.



![Paiement encaissé](assets/fr/19.webp)



**Overvåking og administrasjon**



Alle transaksjoner registreres i Merchant Dashboard. Du har full oversikt over inntekter per periode, totalt antall salg og detaljert historikk for regnskapet ditt.



Innstillinger-grensesnittet har flere konfigurasjonsfaner. I fanen "Generelle innstillinger" kan du administrere forhandlerprofilen din og varslinger. Fanen "Brukere" lar deg legge til og administrere tilgang til Merchant Dashboard for teamet ditt (flerbrukeradministrasjon i henhold til planen din). Fanen "Development Workspace" gir tilgang til API-nøkler for avanserte integrasjoner, mens "Subscription" lar deg administrere abonnementet ditt.



![Paramètres du compte marchand](assets/fr/20.webp)



**Freemium vs. forretningsplaner



Tiankii tilbyr to pakker for Merchant Dashboard. **Freemium**-planen (gratis) er egnet for nystartede bedrifter med begrensninger: ett enkelt salgssted, én enkelt bruker, månedlig volum begrenset til 1 000 USD og ingen tilgang til e-handelskoblinger. **Business**-planen (0,5 % avgift per transaksjon) tilbyr ubegrenset antall terminaler, ubegrenset antall brukere, ubegrenset volum, tilgang til WooCommerce/Shopify/Cloudbeds-plugin-moduler og eksklusive WhatsApp-varsler.



![Comparaison plans Freemium et Business](assets/fr/21.webp)



## Fordeler og begrensninger



### Høydepunkter



**Selvforvaltende**: Du beholder dine private nøkler og full kontroll over midlene dine. Ingen risiko for kontofrysing eller konkurs hos tredjepartsplattformen.



**Enkelhet**: Lightning Address som en e-postadresse, NFC-betalinger med et enkelt trykk, intuitivt grensesnitt uten behov for teknisk ekspertise.



**Komplett økosystem**: Verktøy for alle profiler (privatpersoner, forhandlere, utviklere) med modulære integrasjoner som passer til dine behov.



**Profesjonell etterlevelse**: Sikker nettskyhosting, PCI-DSS-samsvar, overholdelse av salvadoranske forskrifter.



### Begrensninger



**Begrensninger knyttet til lynnedslag**: Krever permanent wallet-tilkobling, likviditetsstyring for store volumer, risiko for feil hvis mottakeren er offline. Tiankii reduserer disse aspektene med integrerte LSP-er.



**SaaS-avhengighet**: Hvis Tiankii ikke er tilgjengelig, er fakturagenerering midlertidig umulig (pengene dine forblir sikre).



**Privatlivets fred**: Tiankii kan observere transaksjonsmetadata (beløp, datoer). Mindre privat enn en selvbetjent løsning som BTCPay Server.



## Konklusjon



Tiankii illustrerer hvordan en veldesignet infrastruktur kan fjerne de tekniske barrierene som hindrer masseinnføring av Bitcoin som en hverdagsvaluta. Ved å kombinere kraften i Lightning Network med en ikke-frihetsberøvende tilnærming og tilgjengelige verktøy, tilbyr økosystemet en balansert vei mellom økonomisk suverenitet og brukervennlighet.



For kjøpmenn representerer Tiankii en mulighet til å redusere transaksjonskostnadene drastisk og samtidig få tilgang til en ny kundebase. For forbrukerne forvandler Lightning Address og NFC-kort Bitcoin til en praktisk valuta, uten teknisk kompleksitet.



Selv om utbredt bruk av Bitcoin fortsatt er en utfordring som krever utdanning og tid, viser infrastrukturer som Tiankii at de tekniske verktøyene allerede finnes. Målet om å forenkle Bitcoin-betalinger er ikke lenger en fjern visjon, men en realitet som er tilgjengelig for alle som er villige til å ta steget.



## Ressurser



### Offisiell dokumentasjon




- [Tiankiis offisielle nettside](https://tiankii.com)
- [Tiankiis hjelpesenter](https://help.tiankii.com)
- [IBI-applikasjon](https://go.ibi.me)
- [Merchant Dashboard](https://pay.tiankii.com)
- [Kommandosenter](https://cc.ibi.me)



### Wallet tilkoblingsguider




- [Koble til LNbits](https://help.tiankii.com/portal/en/kb/articles/connect-your-lnbits-wallet)
- [Koble til BlueWallet (LNDHub)](https://help.tiankii.com/portal/en/kb/articles/connect-your-lndhub-bluewallet)
- [Connect Alby Wallet](https://help.tiankii.com/portal/en/kb/articles/connect-your-alby-wallet)
- [Connect Strike Wallet](https://help.tiankii.com/portal/es/kb/articles/como-vincular-strike-wallet)



### Fellesskapet




- [Lightning Network Plus](https://lightningnetwork.plus) - Lightning educational resource
- [Bitcoin Beach](https://www.bitcoinbeach.com) - Salvadoriansk initiativ for sirkulær økonomi Bitcoin



### Relaterte verktøy




- [Blink Wallet](https://blink.sv) - Wallet Lightning-kompatibel anbefales
- [LNbits](https://lnbits.com) - Selvbetjent wallet-løsning
- [Standard Bolt-kort](https://github.com/boltcard) - Tekniske spesifikasjoner for NFC-kort